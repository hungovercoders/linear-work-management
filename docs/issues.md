# Issues

<div class="lwm-lead" markdown>
For delivery teams and the triage rota. An **issue** in
[Linear](https://linear.app/happydevs/team/GRI/all) is **one discrete task, understood before
it starts**. It's the unit of work — where a project's Key Result gets moved and where inbound
work lands. Everything above it (initiatives, projects) exists to give issues an outcome to
ladder to; the issue itself is where the work happens.
</div>

**[Every issue in Linear, on one screen.](https://linear.app/happydevs/team/GRI/all)** Same
tool as the strategy above it — no boundary between *why* and the task in your cycle.

---

## What an issue is

An issue is a **discrete task, understood before it starts** — small enough for one person to
pick up and finish, clear enough that "done" isn't ambiguous. Two things are true of **every**
issue, whichever path it arrived on:

- **It's classified** — in a project *or* carrying exactly one `flow/*` label, never both,
  never neither ([rule 3](hard-rules.md)). An issue that is neither is *unclassified*: invisible
  work, the defect the whole model chases.
- **Its body is the prompt** — the description says what to do and what "done" means, well
  enough that a person *or an agent* can act on it (the [agent-plan convention](#the-body-is-the-prompt)
  below). It carries a **priority** (Urgent → Low) that orders it.

Keep the issue about *the task* — the *why* belongs to the [initiative](initiatives.md), the
*what & how* to the [project](projects.md) above it.

---

## The shared lifecycle

Every issue moves through the **same states**, whichever path it came from:

| State | Means |
|---|---|
| Triage | Arrived through the front door; awaiting a routing decision |
| Backlog | Accepted, but **not yet refined** enough to start |
| Todo | **Refined, actionable, can be picked up now** |
| In Progress | Being worked |
| In Review | Work done; under review |
| Done | Shipped and accepted |
| Cancelled | Won't do; reason recorded |
| Duplicate | Superseded by another issue |

### Backlog vs Todo — the readiness gate

The line between **Backlog** and **Todo** is the one distinction worth being strict about.

- **Backlog** is *accepted but not ready* — the intent is captured, but the task isn't yet
  understood well enough to hand to someone. It might be vague, unestimated, or blocked.
- **Todo** is *ready now* — refined to the point that someone can pick it up and start without
  going back to ask what it means.

Moving an issue **Backlog → Todo is refinement**: sharpen the problem, define what "done" is,
size it, clear blockers. **Nothing starts from Backlog.** That gate is what keeps *In Progress*
honest — everything in it was understood before it began.

---

## Two kinds of issue — and only one

Every issue is exactly **one of two kinds**, set by how it's classified ([rule 3](hard-rules.md)):

| Kind | Classified by | Belongs to |
|---|---|---|
| <span class="lwm-strat">Project issue</span> | Sits **in a project** | Planned work, laddering to the project's KR |
| <span class="lwm-inbound">Inbound issue</span> | One **`flow/*`** label, **no project** | Work that arrived through Triage |

This page owns the **shared model** and **project issues**. Inbound `flow/*` work has its own
front door — the [Triage rota and the five outcomes](index.md#issues-the-work-itself), covered
in full in **Flow & Triage**.

---

## Project issues — planned work

A project issue lives **inside a project** and moves its Key Result. It carries two label
groups and a priority.

### Labels — `type/*` and `product/*`

One **`type/*`** label says what kind of work it is; **`product/*`** carries down from the
project unchanged. **`action` is the default** — reach for `feature`, `bug`, `analysis` or
`spike` only when the work is specifically one of those.

| `type/*` | For | The template emphasises |
|---|---|---|
| `action` | **The default** — any work that needs doing, from a code change to upkeep to a reminder to yourself | What needs doing, and when it's done |
| `feature` | A new capability | The change and its acceptance criteria |
| `bug` | Something's broken | Steps to reproduce, expected vs actual |
| `analysis` | A data question to answer or a report to produce — the deliverable is the answer, not shipped code | The question, and the answer/report |
| `spike` | A time-boxed investigation — and the free-wheeling home for context, notes and planning | The question and the time box |

`product/*` (`hungovercoders` · `dogadopt` · `woolwitch` · …) is **inherited from the project** —
same value, so work stays attributable to the product it serves without re-deciding it per
issue. `flow/*` never appears on a project issue — that's the inbound group.

!!! note "`spike` is the free-wheeling one"
    A `spike` is where thinking happens **before** the work is understood — gather context, keep
    running notes, sketch a backlog. It's deliberately loose: fill the template sections **as far
    as they help and no further**; the body is a scratchpad. What keeps it honest isn't structure
    but the **time box** in *When is it done?* — a spike is bounded even when its content isn't.
    Follow-up work it turns up becomes **new issues in the project**, linked back to the spike. (A
    whole body of work with its own backlog outgrows a spike — that's a [discovery
    project](projects.md#discovery-phase-is-there-something-here-idea-scoping).)

!!! note "`analysis` vs `spike`"
    Both produce understanding, but the **deliverable** differs: a `spike` reduces uncertainty to
    decide *how to build*; `analysis` answers a data question or produces a report as the outcome
    itself. Analysis happens in **discovery or delivery** — and, like `bug`, the same work can
    arrive **inbound** (as `flow/analysis`) when someone asks for a number or a report outside any
    project.

### Priority

Every issue carries a **priority** (Urgent → Low) that orders it within the project — what gets
picked up next when someone frees up. It's a native field, not a line in the description.

---

## The body is the prompt

An issue's description is written to be **acted on directly** — by a person or an agent. That's
the *agent-plan convention*, and it splits into **two moments**:

- **At capture — the body is the prompt.** State the problem and what "done" looks like clearly
  enough that the reader needs nothing else to start. Write it for whoever — or whatever — picks
  it up. This is all the creation step does: get the task down.
- **At pickup — store the plan against the issue.** *Later*, when the issue is picked up and an
  agent (or a person) works out *how*, that plan is captured in the issue's **`## Plan`** section
  — left empty at creation — so the approach is reviewable before code is, and the issue stays
  the single record of the task.

Keep the two apart: capturing an issue is *getting it down*; planning the how happens when it's
picked up. Either way the description carries both — everything Linear can model as a field is set
as one, leaving the body to hold the *prompt* and, later, the *plan*.

---

## Native fields, not prose

Everything Linear models as a field is a **native field**, never text in the description:

| Native field | Set to |
|---|---|
| Assignee | The one person doing it |
| Priority | Urgent → Low |
| Status | The lifecycle state above |
| Project **or** `flow/*` | The classification (rule 3) — one, never both |
| `type/*` | Project issues only — feature / bug / action / spike |
| `product/*` | Inherited from the project |
| Links | Resources — docs, designs, logs, prior art, related issues — attached, not pasted into the body |

The **description** carries only the *what / why / when*, any *context*, and — later — the
*plan*; that, and only that, is the [template](#create-one) — one per `type/*`. Resources are
**native Links**, not a section.

---

## Create one

The description body is the only thing that lives as text; everything else is a native field
(above).

1. **Use the [`linear-issue`](skills/index.md) skill — preferred.** It asks which kind (project
   issue or inbound), picks the `type/*` or `flow/*`, writes the body from the **template for that
   type**, and sets the native fields — assignee, priority, status, project/label — for you.
2. **By hand.** Create the issue in the [team's Linear view](https://linear.app/happydevs/team/GRI/all),
   set the classification and labels the kind calls for (above), then paste the **template for the
   `type/*`** — one each for `action`, `feature`, `bug`, `analysis` and `spike`, in the
   [`linear-issue` skill folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue)
   — into the description and fill it in. They're the same files the skill uses.

Refine it **Backlog → Todo** before anyone starts — that's the readiness gate.

---

## Related

- [The Hard Rules](hard-rules.md) — rule 3 (every issue classified)
- [Projects](projects.md) — the project a project issue lives in and the KR it moves
- [The Cheat Sheet](index.md) — the one-page summary this expands, including inbound `flow/*` work
