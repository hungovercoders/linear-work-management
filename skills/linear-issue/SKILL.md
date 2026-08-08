---
name: linear-issue
description: Capture a Linear issue to the Ways of Working standard — one discrete task got down clearly (the problem and what "done" means), classified in a project or under one flow/* label (never both), with a type/*, a priority and the product/* it inherits. Sets the native fields and lands it in Backlog, ready to refine. Use when capturing planned project work or writing up an inbound item. The how — the agent plan — comes later, when the issue is picked up.
---

<!-- doc: issues.md -->

# linear-issue

Capture a Linear issue to the Ways of Working standard: get one discrete task **down** — the
problem and what "done" means — classified correctly, with the native fields set, landed in
Backlog. This is **capture, not planning**: the *how* (the agent plan) is worked out later, when
the issue is picked up.

**Requires:** the **Linear MCP server** connected — to read the project, set the native fields
and create the issue.

> Issues have **no status-update object** — progress shows through **state and cycle**, so there's
> no update skill. Create and edit issues with `save_issue`.

## What good looks like

- **Rule 3 — classified.** In a **project** *or* carrying exactly one **`flow/*`** label — never
  both, never neither. This is the first decision; it picks the whole rest of the shape.
- **Understood before it starts.** The problem and what "done" means are clear enough to hand to
  someone (or something) without a follow-up question.
- **A `type/*` (project issues).** `action` is the **default** (any work that needs doing);
  `feature` · `bug` · `spike` when it's specifically that.
- **A priority.** Urgent → Low, so it orders against the others.
- **`product/*` inherited** from the project, unchanged.
- **The body reads as a prompt** — the problem and what "done" means, enough to act on. The plan
  for *how* is added at pickup, not now.

## The kind decides the shape

The skill's **first** job is to classify — that fork decides everything after it:

- **Project issue** — sits **in a project**, ladders to its KR. Gets a **`type/*`**, inherits the
  project's **`product/*`**, no `flow/*`.
- **Inbound issue** — arrived through Triage; carries **one `flow/*`** label and **no project**,
  no `type/*`. The front door, the five outcomes and the SLA clocks live in **Flow & Triage**
  (GRI-74) — this skill just sets it up correctly.

## Flow

**1. Classify it (rule 3).** Ask *is this planned project work, or did it arrive?* — a project
issue or an inbound issue. One or the other, never both.

**2a. Project issue.**

- Identify the **project** it belongs to (`list_projects` / `get_project`) so it ladders to a KR.
- Pick the **`type/*`** — default to **`action`** (any work that needs doing); use `feature`,
  `bug` or `spike` when the work is specifically that.
- Write the **body** from [`template.md`](template.md): what needs doing, why, and when it's
  done. Attach any resources (docs, designs, logs, related issues) as the issue's native
  **Links**, not a body section. `product/*` inherits from the project.
- **`spike` is the free-wheeling one** — a scratchpad for gathering context, notes and planning a
  backlog before the work is understood. Fill the sections only as far as they help; the **time
  box** in *When is it done?* is what bounds it. Follow-ups become new issues in the project.

**2b. Inbound issue.**

- Pick the single **`flow/*`** label (`incident` · `vulnerability` · `bug` · `compliance` ·
  `support` · `toil`). **No project, no `type/*`.**
- Write the same body — what needs doing, why, and when it's done. Triage decides its fate; see
  Flow & Triage.

**3. Set the native fields.** On the issue itself, never in the description: **assignee**,
**priority** (Urgent → Low), **status** (**Backlog** for new work), the **project *or* `flow/*`**
classification, the **`type/*`** (project issues) and the inherited **`product/*`**. Use
`save_issue`.

**That's capture — stop here.** The issue is down and classified. Two things happen *later*, not
in this skill:

- **Refine to Todo.** Sharpen the problem, define done, size it, clear blockers — the
  **Backlog → Todo** readiness gate. **Nothing starts from Backlog.**
- **Write the plan.** When the issue is **picked up**, whoever works it (person or agent) works
  out the *how* and stores it in the description's **`## Plan`** section — left empty at creation,
  so the approach is reviewable before the code is.

## The issue template

[`template.md`](template.md) beside this skill is the single source of truth for the issue
**description body** at capture — What needs doing / Why / When it's done, with a per-type note
on what to emphasise. The `## Plan` section is left empty; it's filled at pickup. Everything else
— including **resources, as native Links** — is a native field.

The **assignee, priority, status, project / `flow/*` classification and `type/*` / `product/*`
labels are native Linear fields** — set them on the issue, never in the description text. Keeping
them native is what lets Linear filter, sort and cycle them, and what lets `linear-doctor` check
classification.
