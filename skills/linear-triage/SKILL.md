---
name: linear-triage
description: Work a Linear team's Triage inbox to the Ways of Working standard: for each incoming issue give it one of the five outcomes (accept into a project · accept as BAU · redirect · merge · decline), set the single bau/* label and a priority, and act within the decision clock. Drives Linear's native Triage; reuses the linear-issue templates when accepting. Use when you're on triage duty and clearing the queue.
---

<!-- doc: issues/triage.md -->

# linear-triage

Work the team's Triage inbox: give every incoming issue a fast routing decision (one of the
five outcomes) and clear the queue within the decision clock. It uses Linear's built-in Triage and
its native actions; the skill's part is making each decision to standard.

**Requires:** the **Linear MCP server** connected, to read the Triage queue and apply decisions.

> Triage is Linear's per-team inbox. This skill *drives* the native actions (Accept, Move to
> team, Merge, Mark duplicate, Decline) via `save_issue`, and doesn't invent a parallel process.

## What good looks like

- Every item gets a decision; "leave it sitting there" is not an outcome.
- Rule 3 holds: it either stays BAU with exactly one `bau/*` label and no project, or is
  accepted into a project with a `type/*` and no `bau/*`. Never both, never neither.
- A priority (Urgent → Low) is set, so it orders the item and lets the SLA rule match.
- You can say which SLA applies to the item. One that no SLA covers can wait, or be declined.
- The decision is made within the decision clock for its `bau/*` kind.

## Flow

**1. Read the queue.** List the team's issues in the Triage state (`list_issues`,
`state: Triage`). Many will have come from the team's asks channel in Slack through Linear Asks.
A comment you add on such an issue appears in the requester's Slack thread, so ask your
questions on the issue. Take the most time-critical first, which is `bau/incident`, then whatever's
nearest its decision-clock limit.

**2. Classify the kind.** Pick the single `bau/*`: `incident` · `vulnerability` · `defect` ·
`query` · `compliance` · `support` · `toil`.

**3. Decide the outcome (one of five).**

| Outcome | Do this |
|---|---|
| Accept into a project | Set the **project** + a **`type/*`**, drop the `bau/*`; it's planned work now. Shape the body with a [`linear-issue`](../linear-issue/SKILL.md) template if it needs one. |
| Accept as BAU | Keep the **one `bau/*`** label, **no project**; set priority; leave it in the workflow. |
| Redirect | **Move it to the right team** (change `team`) — it moves to that team's Triage. |
| Merge | **Mark duplicate of** / merge into the existing issue (`duplicateOf`). |
| Decline | **Cancel** it with a reason. |

**4. Set priority.** Urgent → Low. It orders the item and can drive the SLA (Linear can require a
priority before an issue leaves Triage).

**5. Respect the clocks.** Decide within the decision clock (`incident` immediately,
`vulnerability` or `support` 1 working day, `compliance`, `defect`, `toil` or `query` 2). The
rota and Triage's time-in-status keep that in check, since it isn't a native SLA. Fixing is
measured by a Linear SLA. The team has an SLA rule for each kind of BAU it has promised a fix
time for, matched on the `bau/*` label and priority (`bau/vulnerability`: Urgent 7 days, High 30,
Medium 90). So after you set the label and priority, check the issue shows an SLA. If a kind
that should carry one (`incident`, `vulnerability`, `support`) has none, fix the label or
priority, or set `slaBreachesAt` directly (with `slaType: onlyBusinessDays`).

**6. Apply it.** The outcome and the priority are the duty person's call, so propose each one
and apply it once they agree. Use `save_issue` for the state, team, project, `bau/*` or `type/*` labels,
priority, `duplicateOf` and (for vulnerabilities) `slaBreachesAt`. One decision per item, then
move on.

## No template

Triage produces a decision, not a new artefact, so this skill has no `template.md`. When a
decision *creates or shapes* an issue body (accept into a project), it uses the
[`linear-issue`](../linear-issue/SKILL.md) templates (one per `type/*`).
