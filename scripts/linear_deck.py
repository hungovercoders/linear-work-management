#!/usr/bin/env python3
"""Stakeholder deck — generate Marp slides from live Linear state.

Emits a Marp-flavoured markdown deck to stdout: a portfolio slide, one slide per
initiative (KRs, health from its latest update, owner, target date), and a drill-down
slide per initiative listing its projects (status, lead, dates, latest health).

Requires LINEAR_API_KEY. Render with Marp (or read as plain markdown):
    task deck > deck.md && npx @marp-team/marp-cli deck.md -o deck.html
"""
import json
import os
import sys
import urllib.request

API = "https://api.linear.app/graphql"

HEALTH = {"onTrack": "🟢 on track", "atRisk": "🟡 at risk", "offTrack": "🔴 off track"}


def query(q: str, variables: dict | None = None) -> dict:
    key = os.environ.get("LINEAR_API_KEY", "")
    if not key:
        sys.exit("LINEAR_API_KEY is not set.")
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


def latest_health(update_nodes: list[dict]) -> str:
    if not update_nodes:
        return "⚪ no update posted"
    upd = update_nodes[0]
    when = upd["createdAt"][:10]
    return f"{HEALTH.get(upd['health'], upd['health'])} ({when})"


def main() -> int:
    # Two passes — the nested initiative→project fan-out trips Linear's complexity cap.
    data = query(
        """query { initiatives(first: 50) {
             nodes { id name status targetDate description url
                     owner { displayName }
                     updates: initiativeUpdates(first: 1) { nodes { health createdAt } } }
           } }"""
    )["initiatives"]["nodes"]
    for ini in data:
        ini["projects"] = query(
            """query($id: String!) { initiative(id: $id) {
                 projects(first: 50) { nodes {
                   name url startDate targetDate
                   status { name } lead { displayName }
                   updates: projectUpdates(first: 1) { nodes { health createdAt } } } } } }""",
            {"id": ini["id"]},
        )["initiative"]["projects"]

    print("---\nmarp: true\npaginate: true\n---\n")
    print("# Portfolio review\n")
    if not data:
        print("_No initiatives in the workspace yet._")
        return 0

    print("| Initiative | Status | Health | Owner | Target |")
    print("|---|---|---|---|---|")
    for ini in data:
        print(f"| {ini['name']} | {ini['status']} | {latest_health(ini['updates']['nodes'])} "
              f"| {ini['owner']['displayName'] if ini['owner'] else '—'} "
              f"| {ini['targetDate'] or '—'} |")

    for ini in data:
        print(f"\n---\n\n## {ini['name']}\n")
        print(f"**{ini['status']}** · {latest_health(ini['updates']['nodes'])} · "
              f"owner {ini['owner']['displayName'] if ini['owner'] else '—'} · "
              f"target {ini['targetDate'] or '—'}\n")
        desc = ini["description"] or ""
        in_kr = False
        for line in desc.splitlines():  # lift the KR tables straight from the description
            if line.lower().startswith("## key results"):
                in_kr = True
                continue
            if in_kr and line.startswith("## "):
                break
            if in_kr and line.strip():
                print(line)

        projects = ini["projects"]["nodes"]
        if projects:
            print(f"\n---\n\n### {ini['name']} — projects\n")
            print("| Project | Status | Health | Lead | Dates |")
            print("|---|---|---|---|---|")
            for p in projects:
                dates = f"{p['startDate'] or '…'} → {p['targetDate'] or '…'}"
                print(f"| {p['name']} | {p['status']['name']} "
                      f"| {latest_health(p['updates']['nodes'])} "
                      f"| {p['lead']['displayName'] if p['lead'] else '—'} | {dates} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
