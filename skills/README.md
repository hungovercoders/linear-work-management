# Skills — conventions

The AI-ready skills that create and maintain Linear work to the
[Ways of Working](https://linear-work-management.pages.dev/) operating model. They ship as a
Claude Code plugin and are the executable half of the guide, and every skill has a human-readable
companion page in the docs.

Each skill lives in `skills/<name>/` and follows the conventions below. New skills conform to
these, and `linear-doctor` (GRI-77) maintains them. Skill prose follows the
[writing style](../STYLE.md), checked by `task lint:prose`.

## Layout

```
skills/<name>/
  SKILL.md          # frontmatter (name, description) + the coaching flow
  template.md       # the artefact the skill produces — the description BODY, source of truth
  template-<x>.md   # OR a set, one per value of a native field, when the shape differs by kind
```

Most skills ship a single `template.md`. Where the artefact's shape genuinely differs by a
native field, a skill ships one template per value instead: `linear-issue` has one per `type/*`
(`template-action.md` is the default and base, then `feature` · `bug` · `analysis` · `spike`).
Skills that produce a decision or a report rather than a description carry no template at all;
`linear-doctor` (a drift report) and `linear-triage` (a routing decision) are `SKILL.md`-only.

The generated catalogue at `docs/skills/index.md` is built from each `SKILL.md` by
`scripts/gen_skill_index.py` (`task skills:index`); never hand-edit it.

## The conventions

1. **Template(s) beside the skill.** Any skill that produces a Linear artefact keeps its
   `template.md` in the same directory as the single source of truth, or one or more
   `template-<x>.md` when the artefact's shape differs by a native field (say `linear-issue`,
   one per `type/*`). The skill fills it and a human can copy it by hand. Same file, two paths.
2. **Native fields, not prose.** Templates are the description body only. Everything Linear
   models as a field, whether name, lead or owner, status, dates, priority, initiative links,
   labels or the connected Slack channel, is set as a native Linear field rather than baked into
   the description text. That's what lets Linear filter, sort and roll up, and lets
   `linear-doctor` check it. Each template opens with an HTML comment listing the fields to set.
3. **Self-contained.** A skill needs nothing but its own files and the tooling it declares. There's
   no "Related" section pulling in other skills, so the flow stands alone.
4. **Linear MCP is the prerequisite.** These skills act on the workspace through the **Linear MCP
   server**, and each `SKILL.md` states it under a `**Requires:**` line.
5. **Docs round-trip.** Each `SKILL.md` carries a `<!-- doc: <page>.md -->` marker pointing at its
   companion guide page. The skill is the *how* and the page the *why*, and they stay in lockstep.
6. **Deep links.** Link the live workspace (the `linear.app/happydevs/…` slug pattern) so people
   arrive where they act.
7. **Opt in to Linear's own Agent Skills.** A skill marked `linear_skill: true` in its frontmatter
   is mirrored into Linear as a team-shared Agent Skill by `task linear:skills`, so the Linear
   Agent (chat, Slack, loops) runs the same instructions Claude Code does. The repo stays the
   single source of truth; `scripts/linear_skills_sync.py` inlines each companion template (Linear
   skills can't reach repo files) and upserts idempotently. `task linear:skills -- --check` reports
   drift from a manual Linear edit; `-- --dry-run` prints the generated body without publishing.

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
