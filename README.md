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

## The five rules

1. Every initiative says how it will be measured.
2. Every project says which Key Result it moves, and by how much.
3. Every issue is in a project or has one `bau/*` label. Never both, never neither.
4. One named person owns each initiative and each project.
5. Initiatives and projects have dates once they're `Planned`.

Everything else here expands on those; see **[The five rules](docs/hard-rules.md)**.

---

## What's in here

| Path | What |
|---|---|
| [`docs/index.md`](docs/index.md) | Start here: the model, the five rules and where to go next. |
| [`docs/hard-rules.md`](docs/hard-rules.md) | The hard rules, expanded. |
| [`docs/model.yml`](docs/model.yml) | The model as data: states, labels, SLAs, cadences and thresholds. The guide, skills and doctor are checked against it. |
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

Each page has one summary diagram. They are **D2** sources in `docs/diagrams/*.d2`, rendered to
committed SVGs with `task diagrams` (needs the [d2](https://d2lang.com) CLI) and styled from one
shared file so they match the site. Edit a `.d2`, run `task diagrams`, and commit the SVG with it.

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
issues, BAU & triage, teams/states/labels, SLAs, communication, dashboards, integrations,
and the full skills (author, triage, weekly-update, doctor).
