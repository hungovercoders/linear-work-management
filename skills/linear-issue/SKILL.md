---
name: linear-issue
description: Capture a Linear issue to the Ways of Working standard: one discrete task got down clearly (the problem and what "done" means), classified in a project or under one flow/* label (never both), with a type/*, a priority and the product/* it inherits. Sets the native fields and lands it in Backlog, ready to refine. Use when capturing planned project work or writing up an inbound item. The how, the agent plan, comes later when the issue is picked up.
---

<!-- doc: issues/index.md -->

# linear-issue

Capture a Linear issue to the Ways of Working standard: get one discrete task down (the problem
and what "done" means), classified correctly, with the native fields set and landed in Backlog.
This is capture rather than planning; the *how* (the agent plan) is worked out later, when the
issue is picked up.

**Requires:** the **Linear MCP server** connected, to read the project, set the native fields
and create the issue.

> Issues have no status-update object. Progress shows through state and cycle, so there's no
> update skill. Create and edit issues with `save_issue`.

## What good looks like

- Rule 3, classified: in a project *or* carrying exactly one `flow/*` label, never both, never
  neither. This is the first decision, and it picks the whole rest of the shape.
- Understood before it starts, so the problem and what "done" means are clear enough to hand to
  someone (or something) without a follow-up question.
- A `type/*` for project issues, where `action` is the default (any work that needs doing) and
  `feature`, `bug`, `analysis` (a data question or report) or `spike` when it's specifically that.
- A priority, Urgent → Low, so it orders against the others.
- `product/*` inherited from the project, unchanged.
- A body that reads as a prompt: the problem and what "done" means, enough to act on. The plan
  for *how* is added at pickup, not now.

## The kind decides the shape

The skill's first job is to classify, and that fork decides everything after it:

- A project issue sits in a project and ladders to its KR. It gets a `type/*`, inherits the
  project's `product/*`, and carries no `flow/*`.
- An inbound issue arrived through Triage. It carries one `flow/*` label and no project, no
  `type/*`. Where inbound work arrives, the five outcomes and the SLA clocks live in **Flow &
  Triage** (GRI-74); this skill just sets the issue up correctly.

## Flow

1. Classify it (rule 3). Ask whether this is planned project work or something that arrived:
a project issue or an inbound issue. One or the other, never both.

2a. Project issue.

- Identify the project it belongs to (`list_projects` / `get_project`) so it ladders to a KR.
- Pick the `type/*`, defaulting to `action` (any work that needs doing); use `feature`, `bug`,
  `analysis` (a data question to answer or report to produce) or `spike` when the work is
  specifically that. `analysis` differs from `spike` in that it delivers an answer or report
  rather than a build decision.
- Write the body from the template for that `type/*`, one per type, beside this skill:
  [`template-action.md`](template-action.md) (default and base) ·
  [`template-feature.md`](template-feature.md) · [`template-bug.md`](template-bug.md) ·
  [`template-analysis.md`](template-analysis.md) · [`template-spike.md`](template-spike.md).
  Attach resources (docs, designs, logs, related issues) as the issue's native **Links** rather
  than a body section. `product/*` inherits from the project.
- `spike` is the free-wheeling one: a scratchpad for gathering context, notes and planning a
  backlog before the work is understood. Fill the sections only as far as they help, since the
  time box is what bounds it. Follow-ups become new issues in the project.

2b. Inbound issue.

- Pick the single `flow/*` label (`incident` · `vulnerability` · `defect` · `query` ·
  `compliance` · `support` · `toil`), with no project and no `type/*`. `flow/defect` is a fault
  reported from outside, and `flow/query` an ad-hoc data question or report from outside a
  project: the inbound counterparts of `type/bug` and `type/analysis`, named differently because
  Linear label names are unique across groups.
- Write the body from the template that matches the kind where one exists:
  [`template-bug.md`](template-bug.md) for `flow/defect`, [`template-analysis.md`](template-analysis.md)
  for `flow/query`, otherwise the general [`template-action.md`](template-action.md). Bespoke
  shapes for incident, vulnerability and the rest arrive with Flow & Triage (GRI-74). Triage
  decides its fate; see Flow & Triage.

3. Set the native fields. On the issue itself, never in the description: **assignee**,
**priority** (Urgent → Low), **status** (Backlog for new work), the project *or* `flow/*`
classification, the `type/*` (project issues) and the inherited `product/*`. Use `save_issue`.

That's capture, so stop here. The issue is down and classified. Two things happen *later*,
not in this skill:

- Refine to Todo: sharpen the problem, define done, size it, clear blockers. That's the
  **Backlog → Todo** readiness gate, and nothing starts from Backlog.
- Write the plan: when the issue is picked up, whoever works it (person or agent) works out the
  *how* and stores it in the description's `## Plan` section, left empty at creation so the
  approach is reviewable before the code is.

## The issue templates

One template per `type/*` beside this skill is the source of truth for the issue **description
body** at capture. Pick the one matching the type:

| `type/*` | Template | Body |
|---|---|---|
| `action` (default/base) | [`template-action.md`](template-action.md) | What needs doing? / Why? / When is it done? / Context / Plan |
| `feature` | [`template-feature.md`](template-feature.md) | What needs doing? / Why (user value) / Acceptance criteria / Context / Plan |
| `bug` | [`template-bug.md`](template-bug.md) | What's broken? / Steps to reproduce / Expected vs actual / Impact / Context / Plan |
| `analysis` | [`template-analysis.md`](template-analysis.md) | The question / Why it's needed / When it's answered / Context / Plan |
| `spike` | [`template-spike.md`](template-spike.md) | The question / Why (what it unblocks) / Time box / Notes / Plan |

`action` is the base and also serves inbound kinds with no bespoke template. Every template keeps
the same non-negotiables: the native-fields header, a why, and the `## Plan` section left empty
at creation and filled at pickup. Resources go in native Links, never a body section.

The assignee, priority, status, project or `flow/*` classification and `type/*` or `product/*`
labels are native Linear fields; set them on the issue, never in the description text. Keeping
them native is what lets Linear filter, sort and cycle them, and what lets `linear-doctor` check
classification.
