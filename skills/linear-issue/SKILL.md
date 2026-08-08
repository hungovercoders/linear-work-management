---
name: linear-issue
description: Draft or refine a Linear issue to the Ways of Working standard — one discrete task, understood before it starts, classified in a project or under one flow/* label (never both), with a type/*, a priority and the product/* it inherits. The body is written as a prompt an agent or person can act on, and the plan is stored against the issue. Produces the issue description ready to create in the happydevs workspace. Use when capturing planned project work or writing up an inbound item.
---

<!-- doc: issues.md -->

# linear-issue

Draft or refine a Linear issue to the Ways of Working standard: one discrete task, understood
before it starts, correctly classified, with a body written as a prompt that a person — or an
agent — can act on directly.

**Requires:** the **Linear MCP server** connected — to read the project, set the native fields,
create the issue and store the plan against it.

> Issues have **no status-update object** — progress shows through **state and cycle**, so there's
> no update skill. Create and edit issues with `save_issue`; the agent plan lives in the
> description's `## Agent plan` section.

## What good looks like

- **Rule 3 — classified.** In a **project** *or* carrying exactly one **`flow/*`** label — never
  both, never neither. This is the first decision; it picks the whole rest of the shape.
- **Understood before it starts.** The problem and what "done" means are clear enough to hand to
  someone (or something) without a follow-up question.
- **A `type/*` (project issues).** `feature` · `bug` · `action` · `spike` — what kind of work.
- **A priority.** Urgent → Low, so it orders against the others.
- **`product/*` inherited** from the project, unchanged.
- **The body is the prompt**, and the **plan is stored against the issue** — so the approach is
  reviewable before the code is.

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
- Pick the **`type/*`** — `feature`, `bug`, `action` or `spike`.
- Write the **body** from [`template.md`](template.md): the problem and what "done" looks like,
  as a prompt. `product/*` inherits from the project.

**2b. Inbound issue.**

- Pick the single **`flow/*`** label (`incident` · `vulnerability` · `bug` · `compliance` ·
  `support` · `toil`). **No project, no `type/*`.**
- Write the same body — the problem and what "done" looks like. Triage decides its fate; see
  Flow & Triage.

**3. Set the native fields.** On the issue itself, never in the description: **assignee**,
**priority** (Urgent → Low), **status**, the **project *or* `flow/*`** classification, the
**`type/*`** (project issues) and the inherited **`product/*`**. Use `save_issue`.

**4. Store the plan against the issue.** The body is the prompt; when the *how* is worked out,
capture that plan in the issue's **`## Agent plan`** section — so it's reviewable before the
work is.

**5. Refine before it starts.** New project issues land in **Backlog**; sharpen the problem,
define done, size it and clear blockers to move it to **Todo**. **Nothing starts from Backlog** —
that's the readiness gate.

## The issue template

[`template.md`](template.md) beside this skill is the single source of truth for the issue
**description body** — the same body for every `type/*`, with a per-type note on what to
emphasise. Everything else is a native field.

The **assignee, priority, status, project / `flow/*` classification and `type/*` / `product/*`
labels are native Linear fields** — set them on the issue, never in the description text. Keeping
them native is what lets Linear filter, sort and cycle them, and what lets `linear-doctor` check
classification.
