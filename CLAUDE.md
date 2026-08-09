# Repo instructions

Project-local guidance for anyone (human or agent) authoring in this repo. The published guide
lives in `docs/` and is the product; the notes here are about *building* it.

## Tooling

Everything humans, agents and CI run goes through [Task](https://taskfile.dev), so versions and
commands stay identical across contexts. Prefer a Taskfile target over an ad-hoc command.

```bash
task serve         # live-preview the docs at http://127.0.0.1:8000
task build         # strict static build into ./site
task skills:index  # regenerate docs/skills/index.md from skills/*/SKILL.md
task lint:prose    # AI-tell gate on the guide + skill prose
task doctor        # audit the Linear workspace against the hard rules
```

## Diagrams

Diagrams are **D2** in `docs/diagrams/*.d2`, pre-rendered to committed SVGs with `task diagrams`
(offline via the d2 CLI — no Kroki, no build-time service) and embedded as images
(`![alt](diagrams/<name>.svg)`; use `../diagrams/…` from pages in subfolders). Edit the `.d2`,
run `task diagrams`, commit the SVG beside it. `task diagrams:check` (and CI) verifies every
source has a committed SVG. Follow the house palette and layout already in that folder. Mermaid
is available via ` ```mermaid ` for sequence/gantt (client-side).

## Writing

Repo content and skill prose follow [`STYLE.md`](STYLE.md) — plain, varied, human writing that
doesn't read as machine-drafted. The countable tells are enforced by `task lint:prose`, which
also runs in CI (`.github/workflows/deploy.yml`) and blocks the build on failure. `STYLE.md` is
an authoring instruction for this repo, not part of the Ways of Working the guide teaches.

## Conventions

- Conventional commits (`feat:`, `fix:`, `chore:`, …).
- Branch, commit, and open a draft PR for changes; only mark ready/merge on request.
