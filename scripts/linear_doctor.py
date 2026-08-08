#!/usr/bin/env python3
"""Linear doctor — audit the workspace against the documented operating model.

Placeholder wired into `task doctor` and the (future) linear-doctor skill so the
single-source pattern is visible from the Foundation onward. The rule checks are
implemented in GRI-77 once every rule-defining sub-issue has landed.
"""
import sys

RULES = [
    "initiatives have a named owner",
    "initiatives state what & why with a success measure",
    "projects link to an initiative (orphans flagged)",
    "projects have a single lead, dates and milestones",
    "issues use a known template and consistent states",
    "states and labels match the canonical taxonomy",
]


def main() -> int:
    print("linear-doctor: not yet implemented — see GRI-77.")
    print("Planned rule checks:")
    for r in RULES:
        print(f"  - {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
