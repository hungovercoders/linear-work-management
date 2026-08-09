#!/usr/bin/env python3
"""Prose linter — flag AI-generated-text tells in the guide.

Measures the countable tells from the style guide (STYLE.md) so "reads like AI"
becomes a gate rather than an opinion. Runs over the docs + skill prose, skips the
auto-generated skill index, and ignores fenced code, HTML comments (native-field
blocks), and table rows for the density counts.

Hard failures (exit 1): per-file em-dash and bold budgets, and any banned
vocab / pet metaphor over its cap. Heuristic patterns (fragments, colon-payoff,
antithesis) print as warnings only — regex can't judge them reliably.

    task lint:prose      # or: python scripts/prose_lint.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Per-file budgets on prose lines (tables, code fences and comment blocks excluded).
MAX_EMDASH_PER_FILE = 4
MAX_BOLD_PER_FILE = 8

# Pet metaphors / tell vocabulary: (pattern, cap across the WHOLE corpus).
BANNED = {
    r"\bfront door\b": 2,
    r"\bladders? up\b": 1,
    r"\bit lands\b|\blands in\b|\blands here\b": 2,
    r"\brots\b": 1,
    r"\bsprawl\b": 1,
    r"\bcheaply\b": 1,
    r"\bfirst-class\b": 1,
    r"\bat a glance\b": 1,
    r"\bleverage\b": 0,
    r"\bseamless\b": 0,
    r"\brobust\b": 0,
    r"\bdelve\b": 0,
}

# Heuristic (warning-only) patterns for the register tells.
WARN_PATTERNS = {
    "antithesis (X, not Y / never X, never Y)":
        re.compile(r"\bnot (a|an|the|just|only)\b[^.\n]{0,40}\b(but|,)\b[^.\n]{0,40}\bit'?s?\b"
                   r"|\bnever [a-z]+, never [a-z]+", re.I),
    "colon-payoff opener":
        re.compile(r"^\s*\*\*[A-Z][^*\n]{1,28}\*\*:\s", re.M),
    "verbless punchy fragment":
        re.compile(r"(?:^|\. )(Not a [a-z]+|A lesson|A wish|One [a-z]+ per [a-z]+)\.", re.M),
}

CODE_FENCE = re.compile(r"^```")
COMMENT_OPEN, COMMENT_CLOSE = re.compile(r"<!--"), re.compile(r"-->")
BOLD = re.compile(r"\*\*[^*\n]+\*\*")


def prose_lines(text: str):
    """Yield lines that are real prose: not code fences, HTML comments, or table rows."""
    in_fence = in_comment = False
    for line in text.splitlines():
        if CODE_FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if COMMENT_OPEN.search(line):
            in_comment = True
        if in_comment:
            if COMMENT_CLOSE.search(line):
                in_comment = False
            continue
        if line.lstrip().startswith("|"):  # table row
            continue
        yield line


def collect_files():
    files = [p for p in (ROOT / "docs").rglob("*.md") if p.name != "index.md" or p.parent.name != "skills"]
    files += list((ROOT / "skills").rglob("*.md"))
    files.append(ROOT / "README.md")
    return sorted(f for f in files if f.exists())


def main() -> int:
    failures, warnings = [], []
    banned_hits: dict[str, list[str]] = {pat: [] for pat in BANNED}

    for path in collect_files():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        prose = "\n".join(prose_lines(text))

        em = prose.count("—")
        if em > MAX_EMDASH_PER_FILE:
            failures.append(f"{rel}: {em} em-dashes in prose (budget {MAX_EMDASH_PER_FILE})")

        bold = len(BOLD.findall(prose))
        if bold > MAX_BOLD_PER_FILE:
            failures.append(f"{rel}: {bold} bold spans in prose (budget {MAX_BOLD_PER_FILE})")

        for pat in BANNED:
            for m in re.finditer(pat, text, re.I):
                banned_hits[pat].append(str(rel))

        for name, rx in WARN_PATTERNS.items():
            n = len(rx.findall(text))
            if n:
                warnings.append(f"{rel}: {n}× {name}")

    for pat, cap in BANNED.items():
        hits = banned_hits[pat]
        if len(hits) > cap:
            where = ", ".join(sorted(set(hits)))
            failures.append(f"banned /{pat}/: {len(hits)} uses (cap {cap}) — {where}")

    print("prose-lint — AI-tell gate for the guide.\n")
    if warnings:
        print(f"Warnings ({len(warnings)}) — review, not blocking:")
        for w in warnings:
            print(f"  · {w}")
        print()
    if failures:
        print(f"Failures ({len(failures)}):")
        for f in failures:
            print(f"  ✗ {f}")
        print(f"\n{len(failures)} failure(s). See STYLE.md for the fixes.")
        return 1
    print("Clean: every file within budget.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
