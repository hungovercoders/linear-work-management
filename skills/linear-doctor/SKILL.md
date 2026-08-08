---
name: linear-doctor
description: Audit a scoped slice of the Linear workspace for drift from the Ways of Working — the five hard rules, the label taxonomy, stale initiative/project updates, and native fields buried in description prose. Reports (does not fix), grouped by rule with links. Scope it to a team, project or filter; whole-workspace sweeps run headless via task doctor instead. Use for a health check before a review or when drift is suspected.
---

<!-- doc: hard-rules.md -->

# linear-doctor

Report drift from the [Ways of Working](https://linear-work-management.pages.dev/) model.
The doctor **reports; it does not fix**. It hands you a list, you decide.

**Requires:** the **Linear MCP server** connected, to read the slice being audited.

> **Two doctors, one rulebook.** This skill is the **interactive, scoped** audit — a team, a
> project, a filter. The **whole-workspace sweep** is the headless
> `task doctor` (`scripts/linear_doctor.py` against the Linear API): it paginates in code,
> doesn't blow up a model context, and runs in CI. Don't point this skill at a large
> workspace; that's what the script is for.

## What it checks

The [five hard rules](https://linear-work-management.pages.dev/hard-rules/):

1. **Initiatives declare Key Results** — description names measurable KRs with targets.
2. **Projects name a KR + delta** — once past discovery (`Planned` onward).
3. **Every issue is classified** — in a project **or** exactly one `flow/*` label; flag
   *unclassified* (neither) and *both*.
4. **Single named owner** — initiatives an owner, projects a lead.
5. **Time-bounds** — Active initiatives have a target date; `Planned`+ projects have
   start + target-end.

Plus the operational layer:

- **Taxonomy present** — the four label groups and their
  [canonical values](https://linear-work-management.pages.dev/teams/) exist.
- **Stale updates** — a project In Progress/Launching with no update in ~10 days, an Active
  initiative with none in ~35 ([the cadence](https://linear-work-management.pages.dev/communications/)).
- **Native fields in prose** — owner/dates/priority written into a description body instead
  of set as fields.

## Known limitations (say them, don't skip silently)

- **Initiative blind spot** — this Linear MCP exposes no initiative-read tool, so rule 1 and
  the initiative side of rules 4/5 **can't be checked here**. The headless script covers
  them; say so in the report.
- **Triage-state exemption** — issues sitting in **Triage** are in-flight at the front door,
  not rule-3 violations. Distinguish them from truly unclassified.
- **Pre-model workspaces** — if the taxonomy groups don't exist yet, report *that* (rule 3 is
  unsatisfiable until they do) instead of drowning the user in per-issue findings.
- **Slack connections** aren't API-visible — note them as unverified.

## How to run it

1. **Scope first.** Ask (or infer) the slice: a team, a project, or a filter. Never "everything".
2. **Read minimally.** `list_projects` / `list_issues` with only the fields each check needs:
   the MCP has a query-complexity cap (~10k), and over-fetching nested fields (lead + members +
   teams + labels + initiatives together) trips it. Paginate explicitly; filter issues to
   non-terminal states.
3. Apply the checks above to the slice.
4. Report each finding with a direct link to the offending entity, grouped by rule, and state
   what this run could *not* check. Do **not** mutate anything.

## Related

- [The Hard Rules](https://linear-work-management.pages.dev/hard-rules/)
- [Teams, states & labels](https://linear-work-management.pages.dev/teams/) — the enums it tests against
- `task doctor` — the headless whole-workspace sweep (CI-friendly, covers initiatives)
