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
task model:check   # the guide and skills agree with docs/model.yml
task llms          # generate llms.txt and llms-full.txt, the guide as plain text
task doctor        # audit the Linear workspace against the hard rules
task doctor:test   # exercise the doctor's checks without a workspace
```

## The model file

`docs/model.yml` is the one source of the model's facts: states, labels, the SLA and template
for each kind of BAU, update cadences and the doctor's thresholds. Change a value there first.
`task model:check` (and CI) then names any page or skill that still states the old one. The
doctor reads its labels and thresholds from the same file.

## Diagrams

Each guide page has one summary diagram, in a collapsed `??? abstract "See it as a diagram"` block
under the lead. It shows the whole page in one picture, so it should add something the text and
cards don't: the branches, the order, what feeds what.

Diagrams are **D2** in `docs/diagrams/*.d2`, pre-rendered to committed SVGs with `task diagrams`
(offline via the d2 CLI) and embedded as images (`![alt](diagrams/<name>.svg)`; use
`../diagrams/…` from pages in subfolders). Edit the `.d2`, run `task diagrams`, commit the SVG
beside it. `task diagrams:check` (and CI) verifies every source has a committed SVG.

Every diagram imports `docs/diagrams/shared/classes.d2` (`...@shared/classes`) and styles its
nodes and arrows with those classes, so the colours match the site: use a class, never a one-off
colour. Text is set in IBM Plex Sans from `docs/diagrams/fonts/`. Mermaid is available via
` ```mermaid ` for sequence/gantt (client-side).

## Writing

Repo content and skill prose follow [`STYLE.md`](STYLE.md) — plain, varied, human writing that
doesn't read as machine-drafted. The countable tells are enforced by `task lint:prose`, which
also runs in CI (`.github/workflows/deploy.yml`) and blocks the build on failure. `STYLE.md` is
an authoring instruction for this repo, not part of the Ways of Working the guide teaches.

## Conventions

- Conventional commits (`feat:`, `fix:`, `chore:`, …).
- Branch, commit, and open a draft PR for changes; only mark ready/merge on request.
