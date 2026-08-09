---
name: linear-initiative
description: Draft or refine a Linear initiative to the Ways of Working standard: a defined outcome with declared Key Results (measured or committed), a single named owner, and a target date set from Planned onward. Coaches the KR table and produces the initiative description ready to create in the happydevs workspace. Use when starting a new initiative or tidying an existing one.
linear_skill: true
---

<!-- doc: initiatives.md -->

# linear-initiative

Draft or refine a Linear initiative to the Ways of Working standard: a defined outcome with
declared Key Results, a single named owner, and a target date from `Planned` onward.

**Requires:** the Linear MCP server connected, to read the workspace, link projects, and post
updates.

> Linear's API can't create initiatives directly, so this skill coaches the initiative and
> hands back a description to paste into a new initiative in Linear. Once it exists, link
> projects with `save_project` (`addInitiatives`) and post updates with `save_status_update`
> (`type: initiative`).

## What good looks like

- Rule 1: declares its Key Results before any project. A result, not a theme.
- Rule 4: one named owner with strategic seniority. Not a team, not two people.
- Rule 5: a target date, set now (from `Planned` onward), so it can be prioritised.
- It carries the *why* and *how it's judged*, never the *how it's built*, which is the
  projects' job.
- If it came from project work (one project graduating, or several aggregating) it's grounded
  in those findings and linked back to each.

## Key Results come in two kinds

Allow both, and don't force a number where one doesn't belong:

- **Measured** (aspirational): a metric with a baseline → target (say, "activation
  22% → 30%"). Scored on how far it moved (~0.7 = success). Use for outcomes you can quantify.
- **Committed**: a binary deliverable with a Definition of Done (say, "SOC 2 Type II report
  issued"). Done or not-done. Use for work that *just needs to happen*: compliance, contracted
  deliverables, hard-deadline ships.

Challenge each one:

- A measured KR written as an output ("launch X", "build Y") is usually a committed KR, or the
  metric it's meant to move is the better KR.
- A committed KR whose real purpose is to move a number should be measured instead.
- Every KR names where it's evidenced (dashboard or query for measured; PR, ticket or doc for
  committed). No source yet means that's a dependency; note it.

## Flow

1. **Origin.** Ask whether this outcome comes from project work (one discovery project, or
   several). Three cases:
   - Graduation (one project): read it (`get_project` + its issues) and ground the objective,
     the *why* and the KR baselines in its findings.
   - Aggregation (several projects): read each; the initiative is the larger outcome their
     findings share. Ground the KRs across all of them, and note which project moves which KR.
   - Spontaneous (no project): a fresh strategic bet; that's fine, carry on from a blank
     objective.
   For any project origin, record the lineage: link each discovery project to the new
   initiative (`save_project` → `addInitiatives`), and let each continue as a delivery project
   under it or close once its discovery job is done. Don't start from a blank page when there's
   project evidence to build on.
2. **Objective.** "What's the inspiring objective, and why does it matter?" A qualitative
   direction is right for the name (say, "Make onboarding effortless"). It isn't an initiative
   until it has Key Results (step 3), so don't stop at the objective.
3. **Key Results.** 3–5 of them. For each, ask measured or committed, then prompt for
   baseline → target (measured) or the Definition of Done (committed), plus an evidence source.
4. Owner. One named person, strategic seniority.
5. Timeframe. A target date. Often a quarter; some run a year or more. Set it now.
6. **State.** `Proposed` if not yet agreed; `Planned` once leadership agrees and the owner, KRs
   and date are all set. (`Active` comes later, when work starts against the date.)
7. **Create it in Linear.** Set the name (the outcome), owner/lead, status and target date as
   the initiative's native Linear fields, never as text, and connect the `#initiative-updates`
   Slack channel so updates post there. Put only the description body (why · Key Results · out
   of scope · context) from [`template.md`](template.md) into the description. Hand the filled
   body to the user to create the initiative.

## The initiative template

[`template.md`](template.md) beside this skill is the single source of truth for the description
body: the *why*, the Key Result table(s), *out of scope* and *context* (free-text background
that can grow as needed). Fill each placeholder using the flow above, omit whichever KR table is
unused, and keep 3–5 KRs total.

The name, owner, status and target date are native Linear fields: set them on the initiative
itself, never in the description text. Keeping them native is what lets Linear filter, sort and
roll them up, and what keeps the workspace auditable.
