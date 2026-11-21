#!/usr/bin/env python3
"""Check that the guide and the skills agree with docs/model.yml.

The model file is the one source of the operating model's facts. This fails when prose
states a label the model doesn't have, or when a page that should carry a model value
(a state, a label, a deadline, a threshold) no longer does.

    task model:check      # or: python scripts/check_model.py
"""
import re
import sys

import model

ROOT = model.ROOT
LABEL_TOKEN = re.compile(r"\b(type|bau|spend)/([a-z][a-z-]*)")


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    m = model.load()
    problems: list[str] = []

    def need(rel: str, needle: str, what: str) -> None:
        if needle not in text(rel).replace("`", ""):
            problems.append(f"{rel}: missing {what} ({needle!r})")

    # 1. No prose names a label the model doesn't have.
    labels = model.expected_labels(m)
    prose = [p for p in (ROOT / "docs").rglob("*.md")] + [p for p in (ROOT / "skills").rglob("*.md")]
    prose.append(ROOT / "README.md")
    for path in prose:
        for group, value in LABEL_TOKEN.findall(path.read_text(encoding="utf-8")):
            if labels[group] is not None and value not in labels[group]:
                problems.append(f"{path.relative_to(ROOT)}: `{group}/{value}` is not in the model")

    # 2. Every label value is listed where the guide defines it.
    for group in ("type", "bau", "spend"):
        for value in sorted(labels[group]):
            need("docs/teams.md", value, f"{group}/ value")
    for value in sorted(labels["bau"]):
        need("docs/issues/triage.md", value, "bau/ value")
    for value in sorted(labels["type"]):
        need("docs/issues/project-work.md", value, "type/ value")

    # 3. Every state is on the states page.
    for kind, states in m["states"].items():
        for state in states:
            need("docs/teams.md", state, f"{kind} state")

    # 4. The five rules head the rules page.
    for number, rule in m["rules"].items():
        need("docs/hard-rules.md", f"## {number}. {rule.rstrip('.')}".replace("bau/*", "bau/*"), f"rule {number}")

    # 5. Thresholds and deadlines.
    for state, days in m["doctor"]["languishing_days"].items():
        need("docs/flow.md", f"| {state} | {days} days |", "languishing threshold")
    stale = m["doctor"]["stale_update_days"]
    need("docs/communications.md", f"{stale['project']} days", "stale project threshold")
    need("docs/communications.md", f"none for {stale['initiative']}", "stale initiative threshold")
    for priority, days in m["bau"]["vulnerability"]["sla_days_by_priority"].items():
        need("docs/issues/triage.md", str(days), f"vulnerability SLA ({priority})")
        need("docs/team-setup.md", f"{priority} | {days} days", f"vulnerability SLA rule ({priority})")
    for kind in m["sla_required"]:
        need("docs/team-setup.md", f"bau/{kind}", f"SLA rule for {kind}")

    if problems:
        print("Model check: the guide or skills disagree with docs/model.yml.\n")
        for p in problems:
            print(f"  ✗ {p}")
        print(f"\n{len(problems)} problem(s).")
        return 1
    print("Model check: the guide and skills agree with docs/model.yml.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
