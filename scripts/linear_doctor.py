#!/usr/bin/env python3
"""Linear doctor — audit the workspace against the Ways of Working.

The headless, whole-workspace sweep: paginates the Linear GraphQL API directly, so it
covers what the interactive `linear-doctor` skill can't (initiatives; full-workspace scale)
and runs the same five hard rules + taxonomy/staleness/languishing checks in CI or from
`task doctor`.

Requires LINEAR_API_KEY in the environment. Exits 1 if violations are found, 0 if clean —
reports drift; does not fix.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.linear.app/graphql"

EXPECTED_LABELS = {
    "type": {"action", "feature", "bug", "analysis", "spike"},
    "flow": {"incident", "vulnerability", "defect", "query", "compliance", "support", "toil"},
    "spend": {"capex", "opex"},
    "product": None,  # open set — only the group itself is required
}

PROJECT_DELIVERY_STATUSES = {"planned", "started"}  # status *types* where rules 2 & 5 bite
PROJECT_STALE_DAYS = 10   # weekly cadence + grace
INITIATIVE_STALE_DAYS = 35  # monthly cadence + grace

# Languishing issues (see docs/flow.md). Keyed on shared state *names*, not types:
# only the additive-only rule's protection of shared names makes that safe, and it's
# the only way to tell Planning from Backlog (both backlog-type) or Todo from a
# team's local unstarted state. Backlog is deliberately absent — the unmeasured pool.
LANGUISHING_DAYS = {
    "Planning": 10,   # committed work-up with no visible movement for two working weeks
    "Todo": 14,       # refined two weekly cycles ago, still unstarted
    "In Review": 5,   # finished work waiting on review for a working week
}

# Prose that belongs in a native field, not the description body.
NATIVE_FIELD_PROSE = re.compile(
    r"^\s*\**\s*(owner|lead|status|priority|start date|end date|target date|due)\s*[:—-]",
    re.IGNORECASE | re.MULTILINE,
)


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


def paginate(q: str, root: str, variables: dict | None = None) -> list[dict]:
    nodes, cursor = [], None
    while True:
        data = query(q, {**(variables or {}), "after": cursor})[root]
        nodes.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = data["pageInfo"]["endCursor"]


def days_ago(iso: str | None) -> float:
    if not iso:
        return float("inf")
    then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - then).total_seconds() / 86400


def has_key_results(description: str | None) -> bool:
    if not description:
        return False
    return bool(re.search(r"key results?", description, re.IGNORECASE))


def has_kr_delta(description: str | None) -> bool:
    if not description:
        return False
    # Measured KRs carry a delta arrow; committed KRs a Definition of Done — both satisfy rule 2.
    return ("→" in description or "->" in description
            or re.search(r"committed|definition of done", description, re.IGNORECASE) is not None)


def main() -> int:
    findings: dict[str, list[str]] = {}

    def flag(rule: str, message: str) -> None:
        findings.setdefault(rule, []).append(message)

    # ---- Taxonomy presence (pre-model detection) --------------------------------------
    labels = paginate(
        """query($after: String) { issueLabels(first: 100, after: $after) {
             nodes { name isGroup parent { name } }
             pageInfo { hasNextPage endCursor } } }""",
        "issueLabels",
    )
    groups: dict[str, set[str]] = {}
    for lb in labels:
        if lb["parent"]:
            groups.setdefault(lb["parent"]["name"], set()).add(lb["name"])
    taxonomy_present = all(g in groups for g in EXPECTED_LABELS)
    for group, expected in EXPECTED_LABELS.items():
        if group not in groups:
            flag("taxonomy", f"label group `{group}/` is missing entirely")
        elif expected:
            for missing in sorted(expected - groups[group]):
                flag("taxonomy", f"label `{group}/{missing}` is missing")

    # ---- Initiatives (rules 1, 4, 5 + stale updates) ----------------------------------
    initiatives = paginate(
        """query($after: String) { initiatives(first: 50, after: $after) {
             nodes { name url status targetDate description content
                     owner { displayName }
                     lastUpdate: initiativeUpdates(first: 1) { nodes { createdAt } } }
             pageInfo { hasNextPage endCursor } } }""",
        "initiatives",
    )
    for ini in initiatives:
        label = f"{ini['name']} <{ini['url']}>"
        # Linear splits the short `description` from the markdown `content` body.
        ini_body = ini["content"] or ini["description"]
        if not has_key_results(ini_body):
            flag("rule 1 — initiatives declare Key Results", label)
        if not ini["owner"]:
            flag("rule 4 — single named owner", f"initiative {label}")
        if ini["status"] == "Active":
            if not ini["targetDate"]:
                flag("rule 5 — time-bounds", f"Active initiative with no target date: {label}")
            updates = ini["lastUpdate"]["nodes"]
            if days_ago(updates[0]["createdAt"] if updates else None) > INITIATIVE_STALE_DAYS:
                flag("stale updates", f"initiative (monthly while Active): {label}")
        if ini_body and NATIVE_FIELD_PROSE.search(ini_body):
            flag("native fields in prose", f"initiative {label}")

    # ---- Projects (rules 2, 4, 5 + stale updates) -------------------------------------
    projects = paginate(
        """query($after: String) { projects(first: 50, after: $after) {
             nodes { name url startDate targetDate description content
                     status { name type } lead { displayName }
                     lastUpdate: projectUpdates(first: 1) { nodes { createdAt } } }
             pageInfo { hasNextPage endCursor } } }""",
        "projects",
    )
    for p in projects:
        label = f"{p['name']} <{p['url']}>"
        stype = p["status"]["type"]
        p_body = p["content"] or p["description"]
        if stype in PROJECT_DELIVERY_STATUSES:
            if not has_kr_delta(p_body):
                flag("rule 2 — projects name a KR + delta", label)
            if not p["startDate"] or not p["targetDate"]:
                flag("rule 5 — time-bounds", f"{p['status']['name']} project missing dates: {label}")
        if not p["lead"]:
            flag("rule 4 — single named owner", f"project {label}")
        if stype == "started":
            updates = p["lastUpdate"]["nodes"]
            if days_ago(updates[0]["createdAt"] if updates else None) > PROJECT_STALE_DAYS:
                flag("stale updates", f"project (weekly while In Progress/Launching): {label}")
        if p_body and NATIVE_FIELD_PROSE.search(p_body):
            flag("native fields in prose", f"project {label}")

    # ---- Issues (rule 3 + languishing) ------------------------------------------------
    # One paginated pass serves both checks; the age check runs even pre-taxonomy.
    issues = paginate(
        """query($after: String) {
             issues(first: 100, after: $after,
                    filter: { state: { type: { nin: ["completed", "canceled"] } } }) {
               nodes { identifier title url updatedAt
                       state { name type }
                       project { id }
                       labels { nodes { name parent { name } } } }
               pageInfo { hasNextPage endCursor } } }""",
        "issues",
    )

    if not taxonomy_present:
        flag("rule 3 — every issue is classified",
             "not checkable: the label taxonomy is absent (see `taxonomy` findings) — "
             "rule 3 is unsatisfiable until the groups exist")
    for issue in issues:
        label = f"{issue['identifier']} {issue['title']} <{issue['url']}>"

        threshold = LANGUISHING_DAYS.get(issue["state"]["name"])
        if threshold is not None:
            idle = days_ago(issue["updatedAt"])
            if idle > threshold:
                flag("languishing issues",
                     f"{issue['state']['name']} with no activity for {idle:.0f}d "
                     f"(threshold {threshold}d): {label}")

        if not taxonomy_present:
            continue
        if issue["state"]["type"] == "triage":
            continue  # in-flight at the front door, not a rule-3 violation
        flow = [lb["name"] for lb in issue["labels"]["nodes"]
                if lb["parent"] and lb["parent"]["name"] == "flow"]
        if issue["project"] and flow:
            flag("rule 3 — every issue is classified", f"BOTH project and flow/*: {label}")
        elif not issue["project"] and not flow:
            flag("rule 3 — every issue is classified", f"unclassified: {label}")
        elif len(flow) > 1:
            flag("rule 3 — every issue is classified", f"multiple flow/* labels: {label}")

    # ---- Report -----------------------------------------------------------------------
    print("linear-doctor — reports drift; does not fix.\n")
    if not findings:
        print("Clean bill of health: no drift found.")
        return 0
    for rule in sorted(findings):
        print(f"{rule} ({len(findings[rule])}):")
        for item in findings[rule]:
            print(f"  - {item}")
        print()
    print("Not checked headlessly: Slack channel connections (verify in Linear settings).")
    print("Languishing checks use last activity as a proxy for time in state (Linear stores "
          "no entered-state timestamp outside per-issue history), so they understate the true "
          "wait — the Flow page's views measure the real durations.")
    total = sum(len(v) for v in findings.values())
    print(f"\n{total} finding(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
