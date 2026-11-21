#!/usr/bin/env python3
"""Exercise the doctor's per-issue checks without a Linear workspace.

    task doctor:test      # or: python scripts/test_doctor.py
"""
import sys

import linear_doctor as doctor


def issue(*, labels=(), project=False, state="started", sla=None):
    return {
        "identifier": "GRI-1", "title": "t", "url": "u",
        "state": {"name": "x", "type": state},
        "project": {"id": "p"} if project else None,
        "slaBreachesAt": sla,
        "labels": {"nodes": [{"name": n, "parent": {"name": g}} for g, n in labels]},
    }


CASES = [
    ("project issue is fine", issue(project=True, labels=[("type", "bug")]), []),
    ("unclassified", issue(), ["rule 3"]),
    ("project and bau at once", issue(project=True, labels=[("bau", "defect")]), ["rule 3"]),
    ("two bau labels", issue(labels=[("bau", "defect"), ("bau", "query")]), ["rule 3"]),
    ("in Triage is skipped", issue(state="triage"), []),
    ("incident with no SLA", issue(labels=[("bau", "incident")]), ["BAU with no SLA"]),
    ("vulnerability with no SLA", issue(labels=[("bau", "vulnerability")]), ["BAU with no SLA"]),
    ("support with an SLA is fine", issue(labels=[("bau", "support")], sla="2026-01-01T00:00:00Z"), []),
    ("query needs no SLA", issue(labels=[("bau", "query")]), []),
]


def main() -> int:
    failed = 0
    for name, case, expected in CASES:
        got = [rule for rule, _ in doctor.issue_findings(case)]
        ok = len(got) == len(expected) and all(g.startswith(e) for g, e in zip(got, expected))
        print(f"  {'✓' if ok else '✗'} {name}" + ("" if ok else f": expected {expected}, got {got}"))
        failed += not ok
    print(f"\n{len(CASES) - failed}/{len(CASES)} doctor checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
