# linear-work-management

The single source of truth for **how we run work in Linear** — the operating model
(initiatives → projects → issues, owned by teams), the expectations at each level, and
the **AI-ready Claude Code skills** that keep it all consistent.

📖 **Published guide:** https://linear-work-management.pages.dev/

## What's here

| Path | What |
| ---- | ---- |
| `docs/` | The published guide (MkDocs Material + Kroki diagrams). |
| `skills/` | Claude Code skills — source of truth for the installable plugin. |
| `scripts/` | Shared helpers used by skills, `Taskfile.yml` and CI (no duplication). |
| `.claude-plugin/` | Plugin + marketplace manifests. |

## Local development

Uses [Task](https://taskfile.dev). Everything humans, agents and CI run goes through it.

```bash
task serve         # live-preview the docs at http://127.0.0.1:8000
task build         # strict static build into ./site
task skills:index  # regenerate docs/skills/index.md from skills/*/SKILL.md
task doctor        # audit the workspace against the rules (see GRI-77)
```

Diagrams: **D2** (and any Kroki type) via ` ```kroki-d2 ` fences; **Mermaid** via
` ```mermaid ` (rendered client-side by Material).

## Using the skills

```text
/plugin marketplace add dataGriff/linear-work-management
/plugin install linear-work-management@linear-work-management
```

Then invoke by name, e.g. *"use linear-initiative to review this initiative"*. The skill
catalogue is generated onto the site at `docs/skills/index.md`.

## Deployment

CI builds the site and deploys it to **Cloudflare Pages** (`.github/workflows/deploy.yml`).
Requires repo secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` and a Pages
project named `linear-work-management`.

## Roadmap

Tracked under **[GRI-68](https://linear.app/happydevs/issue/GRI-68)** — Foundation first
(this), then one concept area at a time (initiatives, projects, issues, teams, triage,
communication, dashboards/integrations, linear-doctor).
