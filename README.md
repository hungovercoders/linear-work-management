# Linear Ways of Working

The single source of truth for how we use Linear: the guidelines, the expectations,
and the AI skills that go with them.

📖 **Published guide:** https://linear-work-management.pages.dev/
**Start here → [The Cheat Sheet](docs/index.md)**

---

## Why this exists

Work was invisible. Dependencies were unknown. Prioritising meant arguing from
memory, and nobody could draw a line from the strategy deck to what they'd be doing
on Tuesday. Project admin was manual. Stakeholder feedback was arduous. There was no
one place to look.

This repo is that place.

---

## The hard rules

1. Every initiative declares its Key Results (measured or committed, with targets).
2. Every project names the Key Result it moves, and by how much.
3. Every issue is either in a project or carries one `flow/*` label. Never both,
   never neither.
4. One named human owns each initiative and each project.
5. Initiatives and projects carry dates from `Planned` onward — initiatives a target
   date, projects start + end.

Everything else here is elaboration on those; see **[The Hard Rules](docs/hard-rules.md)**.

---

## What's in here

| Path | What |
|---|---|
| [`docs/index.md`](docs/index.md) | The cheat sheet — hierarchy, hard rules, states, labels, SLAs, cadence. |
| [`docs/diagrams/model.d2`](docs/diagrams/model.d2) | The operating model as a D2 source, rendered inline on the site. |
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
task doctor        # audit the workspace against the hard rules
```

Diagrams are **D2** via ` ```kroki-d2 ` fences (rendered inline as SVG through Kroki);
Mermaid is available via ` ```mermaid ` for sequence/gantt.

## Using the skills

```text
/plugin marketplace add hungovercoders/linear-work-management
/plugin install linear-work-management@linear-work-management
```

Then invoke by name, e.g. *"run linear-doctor on the workspace"*.

## Deployment

CI builds the site `--strict` and deploys it to **Cloudflare Pages**
(`.github/workflows/deploy.yml`). Requires repo secrets `CLOUDFLARE_API_TOKEN` and
`CLOUDFLARE_ACCOUNT_ID` and a Pages project named `linear-work-management`.

---

## Build roadmap

Tracked under **[GRI-68](https://linear.app/happydevs/issue/GRI-68)** — Foundation first
(this), then one sub-issue at a time, each on its own branch: initiatives, projects,
issues, flow & triage, teams/states/labels, SLAs, communication, dashboards, integrations,
and the full skills (author, triage, weekly-update, doctor).
