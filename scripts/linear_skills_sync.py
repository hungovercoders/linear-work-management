#!/usr/bin/env python3
"""Sync repo skills → Linear Agent Skills (repo is the single source of truth).

The `skills/*/SKILL.md` files are the canonical, git-reviewed definition of how to work
in Linear. This publishes the opted-in ones as team-shared Linear Agent Skills so the
Linear Agent (chat, Slack, loops) runs the same instructions Claude Code does — mirroring
how gen_skill_index.py derives the site catalogue from the same source.

A skill opts in with `linear_skill: true` in its SKILL.md frontmatter. Because a Linear
Agent skill is self-contained markdown that can't reach repo files, any companion
`template*.md` is inlined into the published body.

Requires LINEAR_API_KEY in the environment. Team-shared skills need the API key's user to
hold the team's "Agent skills management" permission.

  python scripts/linear_skills_sync.py            # upsert opted-in skills into Linear
  python scripts/linear_skills_sync.py --dry-run  # print the generated bodies, no calls
  python scripts/linear_skills_sync.py --check     # diff against live Linear, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
MAP_FILE = SKILLS_DIR / ".linear-skills.json"
API = "https://api.linear.app/graphql"
GUIDE_BASE = "https://linear-work-management.pages.dev"
TEAM_KEY = os.environ.get("LINEAR_TEAM", "GRI")

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
DOC_MARKER = re.compile(r"^<!--\s*doc:\s*(?P<doc>\S+)\s*-->\s*$\n?", re.MULTILINE)
LEADING_H1 = re.compile(r"\A\s*#\s+\S.*\n")
TEMPLATE_LINK = re.compile(r"\[([^\]]+)\]\(template[^)]*\.md\)")


def field(block: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+?)\s*$", block, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def guide_link(doc: str) -> str:
    """Map a `doc: initiatives.md` / `issues/index.md` marker to its published URL."""
    if not doc:
        return ""
    path = doc[:-len("index.md")] if doc.endswith("index.md") else doc[:-len(".md")] + "/"
    return f"{GUIDE_BASE}/{path.lstrip('/')}"


def parse_skill(skill_md: pathlib.Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    fm = FRONTMATTER.search(text)
    block = fm.group(1) if fm else ""
    doc = DOC_MARKER.search(text)
    return {
        "name": field(block, "name") or skill_md.parent.name,
        "description": field(block, "description"),
        "opt_in": field(block, "linear_skill").lower() == "true",
        "doc": doc.group("doc") if doc else "",
        "dir": skill_md.parent,
        "text": text,
    }


def build_body(skill: dict) -> str:
    """Render the Linear Agent skill body from a repo SKILL.md."""
    body = FRONTMATTER.sub("", skill["text"], count=1)
    body = DOC_MARKER.sub("", body)
    body = LEADING_H1.sub("", body, count=1)          # title is a native Linear field
    body = TEMPLATE_LINK.sub(r"\1", body)             # drop links to files Linear can't see
    body = body.strip()

    parts = [f"_{skill['description']}_", "", body]

    templates = sorted(skill["dir"].glob("template*.md"))
    for tpl in templates:
        parts += [
            "",
            "---",
            "",
            f"## Template ({tpl.name})",
            "",
            "Copy this into the Linear description body; set every native field on the "
            "artefact itself, not in the text.",
            "",
            "```markdown",
            tpl.read_text(encoding="utf-8").strip(),
            "```",
        ]

    url = guide_link(skill["doc"])
    if url:
        parts += ["", "---", "", f"Reference: [{skill['name']} guide]({url})"]

    return "\n".join(parts).strip() + "\n"


# --- Linear API ---------------------------------------------------------------

def query(q: str, variables: dict | None = None) -> dict:
    key = os.environ.get("LINEAR_API_KEY", "")
    if not key:
        sys.exit("LINEAR_API_KEY is not set — create a personal API key in Linear "
                 "(Settings → Account → Security & access) and export it.")
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": q, "variables": variables or {}}).encode(),
        headers={"Authorization": key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        sys.exit(f"GraphQL error: {payload['errors'][0]['message']}")
    return payload["data"]


def team_id(key: str) -> str:
    data = query("query($k:String!){teams(filter:{key:{eq:$k}}){nodes{id key name}}}", {"k": key})
    nodes = data["teams"]["nodes"]
    if not nodes:
        sys.exit(f"No team with key {key!r} in the workspace.")
    return nodes[0]["id"]


def existing_skills(tid: str) -> dict[str, dict]:
    data = query("query{agentSkills(first:250){nodes{id title body teamId slugId shared}}}")
    return {n["title"]: n for n in data["agentSkills"]["nodes"] if n["teamId"] == tid}


CREATE = """mutation($input:AgentSkillCreateInput!){
  agentSkillCreate(input:$input){success agentSkill{id slugId title}}
}"""
UPDATE = """mutation($id:String!,$input:AgentSkillUpdateInput!){
  agentSkillUpdate(id:$id,input:$input){success agentSkill{id slugId title}}
}"""


def main() -> int:
    mode = "push"
    if "--dry-run" in sys.argv:
        mode = "dry-run"
    elif "--check" in sys.argv:
        mode = "check"

    skills = [parse_skill(p) for p in sorted(SKILLS_DIR.glob("*/SKILL.md"))]
    opted = [s for s in skills if s["opt_in"]]
    if not opted:
        print("No skills opted in (add `linear_skill: true` to a SKILL.md frontmatter).")
        return 0
    print(f"{len(opted)} skill(s) opted in: {', '.join(s['name'] for s in opted)}")

    if mode == "dry-run":
        for s in opted:
            print(f"\n{'='*72}\n# {s['name']}\n{'='*72}\n{build_body(s)}")
        return 0

    tid = team_id(TEAM_KEY)
    live = existing_skills(tid)

    if mode == "check":
        drift = []
        for s in opted:
            want = build_body(s).strip()
            have = (live.get(s["name"], {}).get("body") or "").strip()
            if s["name"] not in live:
                drift.append(f"  ✗ {s['name']}: not published to Linear yet")
            elif want != have:
                drift.append(f"  ✗ {s['name']}: Linear body differs from repo (run `task linear:skills`)")
        if drift:
            print("Drift:")
            print("\n".join(drift))
            return 1
        print(f"In sync: {len(opted)} skill(s) match Linear.")
        return 0

    mapping = json.loads(MAP_FILE.read_text()) if MAP_FILE.exists() else {}
    for s in opted:
        body = build_body(s)
        if s["name"] in live:
            res = query(UPDATE, {"id": live[s["name"]]["id"],
                                 "input": {"title": s["name"], "body": body, "teamId": tid}})
            got = res["agentSkillUpdate"]["agentSkill"]
            print(f"  ↻ updated {s['name']} ({got['slugId']})")
        else:
            res = query(CREATE, {"input": {"title": s["name"], "body": body, "teamId": tid}})
            got = res["agentSkillCreate"]["agentSkill"]
            print(f"  ✦ created {s['name']} ({got['slugId']})")
        mapping[s["name"]] = {"id": got["id"], "slugId": got["slugId"], "teamKey": TEAM_KEY}

    MAP_FILE.write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {MAP_FILE.relative_to(ROOT)} ({len(mapping)} skill(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
