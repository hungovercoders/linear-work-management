# Issues

<div class="lwm-lead" markdown>
For anyone who touches the work itself. An **issue** in
[Linear](https://linear.app/happydevs/team/GRI/all) is **one discrete task, understood before
it starts** — the unit of work where a project's Key Result gets moved and where inbound work
lands. This page is what's true of **every** issue; the two paths an issue can take are at the
bottom.
</div>

**[Every issue in Linear, on one screen.](https://linear.app/happydevs/team/GRI/all)** Same
tool as the strategy above it — no boundary between *why* and the task in your cycle.

---

## :material-checkbox-marked-circle-outline: What an issue is

An issue is a **discrete task, understood before it starts** — small enough for one person to
pick up and finish, clear enough that "done" isn't ambiguous. Two things are true of **every**
issue, whichever path it arrived on:

- **It's classified** — in a project *or* carrying exactly one `flow/*` label, never both,
  never neither ([rule 3](../hard-rules.md)). An issue that is neither is *unclassified*:
  invisible work, the defect the whole model chases.
- **Its body is the prompt** — the description says what to do and what "done" means, well
  enough that a person *or an agent* can act on it (the [agent-plan convention](#the-body-is-the-prompt)
  below). It carries a **priority** (Urgent → Low) that orders it.

Keep the issue about *the task* — the *why* belongs to the [initiative](../initiatives.md), the
*what & how* to the [project](../projects.md) above it.

---

## :material-timer-sand: The shared lifecycle

Every issue moves through the **same states**, whichever path it came from:

```kroki-d2
@from_file:diagrams/issue-lifecycle.d2
```

| State | Means |
|---|---|
| Triage | In **Linear's built-in Triage inbox**; awaiting a routing decision (see [Triage work](triage.md)) |
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

## :material-robot-outline: The body is the prompt

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
picked up.

---

## :material-table: Native fields, not prose

Everything Linear models as a field is a **native field**, never text in the description — the
same on both paths:

| Native field | Set to |
|---|---|
| Assignee | The one person doing it |
| Priority | Urgent → Low |
| Status | The lifecycle state above |
| Project **or** `flow/*` | The classification (rule 3) — one, never both |
| Links | Resources — docs, designs, logs, prior art, related issues — attached, not pasted into the body |

The kind-specific labels (`type/*`, `product/*` for project work; `flow/*` for triage) are on
the two pages below. The **description** carries only the *what / why / when*, any *context*,
and — later — the *plan*: that's the template, and the [`linear-issue`](../skills/index.md) skill
fills it.

---

## :material-directions-fork: Which work is it?

Every issue is exactly **one of two kinds**, set by how it's classified ([rule 3](../hard-rules.md)).
Pick your path — each page is written for the people who live on it:

<div class="grid cards" markdown>

-   :material-clipboard-check-outline: **[Project work](project-work.md)**

    ---

    <span class="lwm-strat">Planned work</span> that sits **in a project** and ladders to its
    Key Result. `type/*` + `product/*` labels, a priority, and a template per type.

    **For delivery teams.** [:octicons-arrow-right-24: Project work](project-work.md)

-   :material-bell-ring-outline: **[Triage work](triage.md)**

    ---

    <span class="lwm-inbound">Inbound work</span> that **arrived** — one `flow/*` label, no
    project. The front door, the five outcomes, and the two SLA clocks.

    **For the triage rota.** [:octicons-arrow-right-24: Triage work](triage.md)

</div>

---

## Related

- [The Hard Rules](../hard-rules.md) — rule 3 (every issue classified)
- [The Cheat Sheet](../index.md) — the one-page summary this expands
