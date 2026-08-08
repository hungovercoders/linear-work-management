---
name: linear-doctor
description: Audit a Linear workspace for drift from the Ways of Working operating model. Reports (does not fix) violations of the hard rules — initiatives with no Key Results, projects with no named Key Result, unclassified issues (in no project and no flow/* label, or both), initiatives/projects without a single named owner, and active initiatives or planned-or-later projects with no dates. Use for a health check of the happydevs workspace or before a review.
---

<!-- doc: hard-rules.md -->

# linear-doctor

Report drift from the [Ways of Working](https://linear-work-management.pages.dev/) model.
The doctor **reports; it does not fix** — it hands you a list, you decide.

> Foundation version: checks the [hard rules](https://linear-work-management.pages.dev/hard-rules/).
> Extended to the full taxonomy in GRI-77.

## What it checks (the hard rules)

1. **Initiatives declare Key Results.** Flag any initiative whose description names no
   measurable Key Results with targets.
2. **Projects name a KR + delta.** Flag any active/planned project whose description
   doesn't name the Key Result it moves and by how much.
3. **Every issue is classified.** Flag issues that are in **no** project **and** carry
   **no** `flow/*` label (*unclassified*), and issues that are in a project **and** also
   carry a `flow/*` label (*both*).
4. **Single named owner.** Flag initiatives without a lead/owner and projects without a
   single named lead.
5. **Time-bounds.** Flag active initiatives with no target date, and projects in
   `Planned`/`In Progress`/`Launching` with no start or no target end date.

## How to run it

1. Read the workspace with the Linear MCP tools (`list_projects`, `list_issues`,
   initiatives, labels).
2. Apply the five checks above.
3. Report each violation with a direct link to the offending entity, grouped by rule.
   Do **not** mutate anything.

The same checks are available headless via `task doctor` (`scripts/linear_doctor.py`) so
humans, agents and CI run one source of truth.

## Related

- [The Hard Rules](https://linear-work-management.pages.dev/hard-rules/)
- [The Cheat Sheet](https://linear-work-management.pages.dev/)
