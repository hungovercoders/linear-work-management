---
name: linear-doctor
description: Audit a scoped slice of the Linear workspace for drift from the Ways of Working: the five hard rules, the label taxonomy, stale initiative/project updates, and native fields buried in description prose. Reports (does not fix), grouped by rule with links. Scope it to a team, project or filter; whole-workspace sweeps run headless via task doctor instead. Use for a health check before a review or when drift is suspected.
---

<!-- doc: hard-rules.md -->

# linear-doctor

Report drift from the [Ways of Working](https://linear-work-management.pages.dev/) model. The
doctor reports rather than fixes: it hands you a list, and you decide.

**Requires:** the **Linear MCP server** connected, to read the slice being audited.

> Two doctors share one rulebook. This skill is the interactive, scoped audit over a team, a
> project or a filter. The whole-workspace sweep is the headless `task doctor`
> (`scripts/linear_doctor.py` against the Linear API): it paginates in code, doesn't blow up a
> model context, and runs in CI. Don't point this skill at a large workspace; that's what the
> script is for.

## What it checks

The [five hard rules](https://linear-work-management.pages.dev/hard-rules/):

1. **Initiatives declare Key Results.** The description names measurable KRs with targets.
2. **Projects name a KR + delta**, once past discovery (`Planned` onward).
3. **Every issue is classified**: in a project or exactly one `flow/*` label. Flag
   *unclassified* (neither) and *both*.
4. **Single named owner.** Initiatives have an owner, projects a lead.
5. **Time-bounds.** Active initiatives have a target date; `Planned`-plus projects have a start
   and target-end.

Plus the operational layer:

- The taxonomy is present: the four label groups and their
  [canonical values](https://linear-work-management.pages.dev/teams/) exist.
- Stale updates: a project In Progress or Launching with no update in about 10 days, an Active
  initiative with none in about 35 ([the cadence](https://linear-work-management.pages.dev/communications/)).
- Native fields written into prose: owner, dates or priority put in a description body instead
  of set as fields.

## Known limitations (say them, don't skip silently)

- Initiative blind spot: this Linear MCP exposes no initiative-read tool, so rule 1 and the
  initiative side of rules 4 and 5 can't be checked here. The headless script covers them, so
  say so in the report.
- Triage-state exemption: issues sitting in **Triage** are in-flight and awaiting a decision,
  not rule-3 violations. Distinguish them from the truly unclassified.
- Pre-model workspaces: if the taxonomy groups don't exist yet, report *that* (rule 3 is
  unsatisfiable until they do) instead of drowning the user in per-issue findings.
- Slack connections aren't API-visible, so note them as unverified.

## How to run it

1. Scope first. Ask (or infer) the slice: a team, a project, or a filter, never "everything".
2. Read minimally. Call `list_projects` and `list_issues` with only the fields each check needs.
   The MCP has a query-complexity cap around 10k, and over-fetching nested fields (lead, members,
   teams, labels and initiatives together) trips it. Paginate explicitly and filter issues to
   non-terminal states.
3. Apply the checks above to the slice.
4. Report each finding with a direct link to the offending entity, grouped by rule, and state
   what this run could *not* check. Don't mutate anything.

## Related

- [The Hard Rules](https://linear-work-management.pages.dev/hard-rules/)
- [Teams, states & labels](https://linear-work-management.pages.dev/teams/) — the enums it tests against
- `task doctor` — the headless whole-workspace sweep (CI-friendly, covers initiatives)
