# Skills — conventions

The AI-ready skills that create and maintain Linear work to the
[Ways of Working](https://linear-work-management.pages.dev/) operating model. They ship as a
Claude Code plugin and are the executable half of the guide; every skill has a human-readable
companion page in the docs.

Each skill lives in `skills/<name>/` and follows the conventions below. New skills conform to
these; `linear-doctor` (GRI-77) maintains them.

## Layout

```
skills/<name>/
  SKILL.md          # frontmatter (name, description) + the coaching flow
  template.md       # the artefact the skill produces — the description BODY, source of truth
  template-<x>.md   # OR a set, one per value of a native field, when the shape differs by kind
```

Most skills ship a single `template.md`. Where the artefact's shape genuinely differs by a
native field, a skill ships **one template per value** instead: `linear-issue` has one per
`type/*` (`template-action.md` is the default/base, then `feature` · `bug` · `analysis` · `spike`).
Skills that produce a **decision or a report** rather than a description carry no template at
all: `linear-doctor` (a drift report) and `linear-triage` (a routing decision) are `SKILL.md`-only.

The generated catalogue at `docs/skills/index.md` is built from each `SKILL.md` by
`scripts/gen_skill_index.py` (`task skills:index`); never hand-edit it.

## The conventions

1. **Template(s) beside the skill.** Any skill that produces a Linear artefact keeps its
   `template.md` in the same directory as the single source of truth — or **one or more
   `template-<x>.md`** when the artefact's shape differs by a native field (e.g. `linear-issue`,
   one per `type/*`). The skill fills it; a human can copy it by hand. Same file, two paths.
2. **Native fields, not prose.** Templates are the **description body only**. Everything Linear
   models as a field — name, lead/owner, status, dates, priority, initiative links, labels,
   connected Slack channel — is set as a **native Linear field**, never baked into the
   description text. That's what lets Linear filter, sort and roll up, and lets `linear-doctor`
   check it. Each template opens with an HTML comment listing the fields to set in Linear.
3. **Self-contained.** A skill needs nothing but its own files and the tooling it declares. No
   "Related" section pulling in other skills — the flow stands alone.
4. **Linear MCP is the prerequisite.** These skills act on the workspace through the **Linear MCP
   server**. Each `SKILL.md` states it under a `**Requires:**` line.
5. **Docs round-trip.** Each `SKILL.md` carries a `<!-- doc: <page>.md -->` marker pointing at its
   companion guide page. The skill is the *how*, the page the *why* — they stay in lockstep.
6. **Deep links.** Link the live workspace (the `linear.app/happydevs/…` slug pattern) so people
   land where they act.

## The skills

| Skill | Produces | Companion page |
|-------|----------|----------------|
| `linear-initiative` | An initiative description (why + Key Results) | [Initiatives](https://linear-work-management.pages.dev/initiatives/) |
| `linear-initiative-update` | The monthly `#initiative-updates` update | [Initiatives](https://linear-work-management.pages.dev/initiatives/) |
| `linear-project` | A project description (what & how + KR delta) | [Projects](https://linear-work-management.pages.dev/projects/) |
| `linear-project-update` | The weekly `#project-updates` update | [Projects](https://linear-work-management.pages.dev/projects/) |
| `linear-issue` | An issue description (problem + agent plan) | [Issues](https://linear-work-management.pages.dev/issues/) |
| `linear-triage` | A routing decision per inbound issue (five outcomes) | [Triage work](https://linear-work-management.pages.dev/issues/triage/) |
| `linear-team-digest` | The weekly team digest (cycle + triage roll-up) | [Communications](https://linear-work-management.pages.dev/communications/) |
| `linear-doctor` | A drift report — hard rules, taxonomy, stale updates | [The Hard Rules](https://linear-work-management.pages.dev/hard-rules/) |
| `linear-stakeholder-deck` | A Marp slide deck of the live portfolio | [Communications](https://linear-work-management.pages.dev/communications/) |
