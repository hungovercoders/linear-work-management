#!/usr/bin/env python3
"""Diagram freshness guard — every D2 source has a committed SVG, and vice versa.

Diagrams are authored in docs/diagrams/*.d2 and pre-rendered to committed SVGs
by `task diagrams` (offline, via the d2 CLI — no Kroki, no build-time service).
The site build just serves the committed SVGs, so this check exists to catch the
one failure mode that decoupling introduces: a source added or renamed without
its SVG regenerated. It is version-agnostic (no d2 needed) — it checks pairing,
not pixels; content freshness is the author's job via `task diagrams`.
"""
import sys
from pathlib import Path

DIAGRAMS = Path(__file__).resolve().parent.parent / "docs" / "diagrams"


def main() -> int:
    sources = {p.stem for p in DIAGRAMS.glob("*.d2")}
    rendered = {p.stem for p in DIAGRAMS.glob("*.svg")}

    missing = sorted(sources - rendered)
    orphans = sorted(rendered - sources)

    for name in missing:
        print(f"  ✗ {name}.d2 has no {name}.svg — run 'task diagrams' and commit")
    for name in orphans:
        print(f"  ✗ {name}.svg has no {name}.d2 source — delete the stale SVG")

    if missing or orphans:
        print(f"\n{len(missing) + len(orphans)} diagram issue(s).")
        return 1
    print(f"Diagrams: {len(sources)} source(s), each with a committed SVG.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
