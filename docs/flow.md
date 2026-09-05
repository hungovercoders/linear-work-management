# :material-chart-timeline-variant: Flow

This page is about how work moves through the [issue states](teams.md#issue-states), which is a
different thing from the `flow/*` labels that classify [inbound work](issues/triage.md). A
bottleneck is a queue, and a queue is visible as time in state: when a stage of the process
can't keep up, work piles up in the state before it and sits. Measure the sitting and the
constraint names itself.

## What each state's age tells you

| State | Its age evidences |
|---|---|
| Triage | A routing decision overdue — the [decision clock](issues/triage.md#two-clocks) owns this one |
| Backlog | Nothing, deliberately. It's the default pool; nobody has committed to the work, so no clock runs |
| Planning | The planning bottleneck: committed work waiting on, or stuck in, requirements, refinement and sizing |
| Todo | Ready work nobody has started — refinement is outrunning delivery, or the cycle intake is too timid |
| In Progress | Execution time; long ages here usually mean oversized issues or hidden blockers |
| In Review | The review bottleneck: finished work waiting on a reviewer |

Backlog is exempt on purpose. Keeping it an unmeasured pool is what makes the other numbers
honest: an ageing item there is a parked idea, and parking is allowed. The moment the team
commits, the move to [Planning](issues/index.md#backlog-planning-todo-commitment-then-readiness)
starts the clock.

## Measure it in Linear

None of this needs new tooling, just a handful of shared views.

- One view per measured state (Planning, Todo, In Review) filtered to open issues, ordered
  oldest first, with the **time in status** display property switched on. The triage page
  already uses the same mechanism for its decision clock. The oldest item at the top of each
  view is the current worst case.
- A board of open issues grouped by state, which shows the *depth* of each queue where the
  views show the *wait*. A Planning column twice the size of Todo is refinement capacity
  failing to keep up.
- Where your plan includes Linear Insights, chart open issues by state with average age, and
  watch the trend rather than the snapshot. A Planning average that climbs week on week is
  exactly the evidence this page exists to surface.

Favourite the views into the shared sidebar beside the [drift views](dashboards.md), and record
their URLs there once they exist.

## Read it, then act

| Signal | Likely cause | Do |
|---|---|---|
| Planning ages, or its column grows | Refinement capacity is the constraint | Schedule refinement time; pull less into Planning; move honest not-nows back to Backlog |
| Todo ages while In Progress stays thin | Intake: nobody is starting ready work | Start what's refined before refining more; check cycle intake habits |
| In Review ages | Review capacity is the constraint | Smaller changes; a review rota; reviewing before starting new work |
| In Progress ages | Issues oversized or quietly blocked | Split them; surface blockers as native relations |

The number is never the point. Each row is a conversation the age lets you open with evidence
instead of a feeling.

## The doctor's part

`task doctor` flags issues that have sat unusually long, so a languishing item gets caught
between glances at the views:

| State | Flagged after | Why this threshold |
|---|---|---|
| Planning | 10 days | Two working weeks of committed work-up with no visible movement |
| Todo | 14 days | Refined two weekly cycles ago and still unstarted |
| In Review | 5 days | A working week of finished work waiting on review |

These checks read the issue's last activity as a stand-in for time in state, since Linear
doesn't store when an issue entered its current state short of per-issue history. Any touch
resets the proxy, so the doctor understates the true wait and every finding is real. The views
above measure the actual durations; the doctor catches what nobody happened to be watching.

## Related

- [Issues](issues/index.md) — the lifecycle these measurements hang off
- [Teams, states & labels](teams.md) — the shared state set, including Planning
- [Dashboards](dashboards.md) — the drift views these queues sit beside
- [Triage work](issues/triage.md) — the decision clock at the head of the pipe
