#!/usr/bin/env python3
"""Linear doctor — audit the workspace against the hard rules.

Shared entrypoint reused by the `linear-doctor` skill, `task doctor`, and (later) CI, so
there is one source of truth for the rules. This Foundation version documents the checks;
the live workspace audit is wired up with the full skill in GRI-77.
"""
import sys

HARD_RULES = [
    "Every initiative declares its Key Results (measurable outcomes with targets).",
    "Every project names the Key Result it moves, and by how much.",
    "Every issue is in a project OR carries one flow/* label — never both, never neither.",
    "One named human owns each initiative and each project.",
    "Active initiatives are time-bound; projects carry start + end dates from Planned onward.",
]


def main() -> int:
    print("linear-doctor — reports drift; does not fix.\n")
    print("Checks (the hard rules):")
    for i, rule in enumerate(HARD_RULES, 1):
        print(f"  {i}. {rule}")
    print("\nFoundation stub — the live workspace audit lands with the full skill (GRI-77).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
