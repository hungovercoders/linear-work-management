# Linear Ways of Working

The single source of truth for how we use Linear: the guidelines, the expectations,
and the AI skills that go with them.

📖 **Published guide:** https://hungovercoders.github.io/linear-work-management/
**[Start here](docs/index.md)**

---

## Why this exists

Work was invisible and dependencies unknown. Prioritising meant arguing from memory, and nobody
could draw a line from the strategy deck to what they'd be doing on Tuesday. Project admin was
manual, stakeholder feedback arduous, and there was no one place to look.

This repo is that place.

---

## The hard rules

1. Every initiative declares its Key Results (measured or committed, with targets).
2. Every project names the Key Result it moves, and by how much.
3. Every issue is either in a project or carries one `flow/*` label. Never both,
   never neither.
4. One named human owns each initiative and each project.
5. Initiatives and projects carry dates from `Planned` onward: initiatives a target
   date, projects start + end.

Everything else here expands on those; see **[The hard rules](docs/hard-rules.md)**.

---

## What's in here

| Path | What |
|---|---|
| [`docs/index.md`](docs/index.md) | Start here: the model, the five rules and where to go next. |
| [`docs/diagrams/model.d2`](docs/diagrams/model.d2) | The operating model as a D2 source, pre-rendered to `model.svg` and embedded on the site. |
| [`docs/hard-rules.md`](docs/hard-rules.md) | The hard rules, expanded. |
| `skills/` | Claude Code skills — the source of the installable plugin. |
| `scripts/` | Shared helpers used by skills, `Taskfile.yml` and CI (no duplication). |

---

## Local development

Uses [Task](https://taskfile.dev); everything humans, agents and CI run goes through it.

```bash
task serve         # live-preview the docs at http://127.0.0.1:8000
task build         # strict static build into ./site
task skills:index  # regenerate docs/skills/index.md from skills/*/SKILL.md
task diagrams      # re-render docs/diagrams/*.d2 to committed SVGs (needs the d2 CLI)
task doctor        # audit the workspace against the hard rules
```

Diagrams are **D2** in `docs/diagrams/*.d2`, pre-rendered to committed SVGs with `task diagrams`
(offline via the [d2](https://d2lang.com) CLI — no external service) and embedded as images. The
site build serves the committed SVGs and needs neither d2 nor Kroki. Edit a `.d2`, run
`task diagrams`, and commit the SVG alongside it. Mermaid is available via ` ```mermaid ` for
sequence/gantt (rendered client-side).

Content and skill prose follow [`STYLE.md`](STYLE.md) (enforced by `task lint:prose`); repo
authoring notes live in [`CLAUDE.md`](CLAUDE.md).

## Using the skills

```text
/plugin marketplace add hungovercoders/linear-work-management
/plugin install linear-work-management@linear-work-management
```

Then invoke by name, e.g. *"run linear-doctor on the workspace"*.

## Deployment

CI builds the site `--strict` on every pull request and push. A push to `main` also deploys it to
**GitHub Pages** (`.github/workflows/deploy.yml`). This needs no secrets, only Pages switched on
once with **GitHub Actions** as the source (repo Settings → Pages → Build and deployment).

---

## Build roadmap

Tracked under **[GRI-68](https://linear.app/happydevs/issue/GRI-68)** — Foundation first
(this), then one sub-issue at a time, each on its own branch: initiatives, projects,
issues, flow & triage, teams/states/labels, SLAs, communication, dashboards, integrations,
and the full skills (author, triage, weekly-update, doctor).
