---
name: linear-triage
description: Work a Linear team's Triage inbox to the Ways of Working standard — for each incoming issue give it one of the five outcomes (accept into a project · accept as flow · redirect · merge · decline), set the single flow/* label and a priority, and act within the decision clock. Drives Linear's native Triage; reuses the linear-issue templates when accepting. Use when you're on triage duty and clearing the queue.
---

<!-- doc: issues/triage.md -->

# linear-triage

Work the team's **Triage inbox**: give every incoming issue a fast routing decision — one of the
**five outcomes** — and clear the queue within the **decision clock**. This rides on Linear's
built-in Triage; it makes the decision to standard, it doesn't replace the native actions.

**Requires:** the **Linear MCP server** connected — to read the Triage queue and apply decisions.

> Triage is Linear's per-team inbox. This skill *drives* the native actions (Accept / Move to team
> / Merge / Mark duplicate / Decline) via `save_issue` — it doesn't invent a parallel process.

## What good looks like

- **Every item gets a decision** — "leave it sitting there" is not an outcome.
- **Rule 3 holds**: stays inbound → exactly one `flow/*` label and **no project**; or is accepted
  into a **project** with a `type/*` and **no `flow/*`**. Never both, never neither.
- **A priority** (Urgent → Low) is set — it orders the item and can drive the SLA.
- The decision is made **within the decision clock** for its `flow/*` kind.

## Flow

**1. Read the queue.** List the team's issues in the **Triage** state (`list_issues`,
`state: Triage`). Take the most time-critical first — `flow/incident`, then whatever's nearest its
decision-clock limit.

**2. Classify the kind.** Pick the single **`flow/*`** — `incident` · `vulnerability` · `defect` ·
`query` · `compliance` · `support` · `toil`.

**3. Decide the outcome (one of five).**

| Outcome | Do this |
|---|---|
| Accept into a project | Set the **project** + a **`type/*`**, drop the `flow/*` — it's planned work now. Shape the body with a [`linear-issue`](../linear-issue/SKILL.md) template if it needs one. |
| Accept as flow | Keep the **one `flow/*`** label, **no project**; set priority; leave it in the workflow. |
| Redirect | **Move it to the right team** (change `team`) — it lands in that team's Triage. |
| Merge | **Mark duplicate of** / merge into the existing issue (`duplicateOf`). |
| Decline | **Cancel** it with a reason. |

**4. Set priority.** Urgent → Low. It orders the item and can drive the SLA (Linear can require a
priority before an issue leaves Triage).

**5. Respect the clocks.** Decide within the **decision clock** (`incident` immediately;
`vulnerability`/`support` 1 working day; `compliance`/`defect`/`toil`/`query` 2) — the rota and
Triage's time-in-status keep that honest (it isn't a native SLA). For **`flow/vulnerability`**, set
the **resolution** SLA (severity → 7 / 30 / 90 days): a native SLA rule handles it on
Business/Enterprise, otherwise set **`slaBreachesAt`** directly (with `slaType: onlyBusinessDays`).

**6. Apply it.** Use `save_issue` for the state, team, project, `flow/*`/`type/*` labels, priority,
`duplicateOf` and (for vulnerabilities) `slaBreachesAt`. One decision per item, then move on.

## No template

Triage produces a **decision**, not a new artefact — so this skill has no `template.md`. When a
decision *creates or shapes* an issue body (accept into a project), it uses the
[`linear-issue`](../linear-issue/SKILL.md) templates (one per `type/*`).
