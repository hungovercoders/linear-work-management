# :material-chart-timeline-variant: Flow

<div class="lwm-lead" markdown>
How to tell where work is getting stuck. When one stage of the process can't keep up, issues
pile up in the state before it. Look at how long issues have been waiting and the bottleneck
shows itself.
</div>

"Flow" on this page means work moving through the [issue states](teams.md#states). It's a
different thing from the `flow/*` labels on [inbound work](issues/triage.md).

## What a long wait tells you

| State | A long wait here means |
|---|---|
| Triage | A decision is overdue. The [decision clock](issues/triage.md#two-clocks) covers this |
| Backlog | Nothing. It's a parking place, and nobody is counting |
| Planning | Refinement can't keep up. Work the team committed to is waiting for requirements or sizing |
| Todo | Ready work that nobody has started. You're refining faster than you deliver, or pulling too little into each cycle |
| In Progress | The issues are too big, or something is quietly blocking them |
| In Review | Finished work is waiting for a reviewer |

`Backlog` is left out on purpose. An old item there is an idea someone parked, and parking is
allowed. The count starts when the team commits and the issue moves to
[`Planning`](issues/index.md#readiness).

## What to do about it

| You see | Likely cause | Try |
|---|---|---|
| Planning issues ageing, or the column growing | Not enough time for refinement | Schedule refinement time. Pull less into Planning. Move things you won't do soon back to Backlog |
| Todo ageing while In Progress stays thin | Nobody is starting ready work | Start what's refined before refining more |
| In Review ageing | Not enough reviewing | Make changes smaller. Set up a review rota. Review before starting something new |
| In Progress ageing | Issues too big, or blocked | Split them. Record blockers as relations in Linear |

The numbers matter less than the conversation they let you have, with evidence in place of a
hunch.

## Set up the views

You don't need any new tools for this, only a few shared views in Linear.

- Make one view each for `Planning`, `Todo` and `In Review`. Filter to open issues, sort oldest
  first and turn on the **time in status** display property. The issue at the top is your
  longest wait.
- Make a board of open issues grouped by state. This shows how deep each queue is. A Planning
  column twice the size of Todo means refinement is falling behind.
- If your plan includes Linear Insights, chart open issues by state with their average age, and
  watch how it changes from week to week.

Add the views to the shared sidebar next to the [drift views](dashboards.md).

## What the doctor checks

`task doctor` flags issues that have waited a long time, so they get noticed even when nobody
is watching the views.

| State | Flagged after | Because |
|---|---|---|
| Planning | 10 days | Two working weeks with no visible progress |
| Todo | 14 days | Refined two weekly cycles ago and still not started |
| In Review | 5 days | A working week of finished work waiting on review |

??? note "How the doctor measures the wait"
    Linear doesn't record when an issue entered its current state, short of reading each
    issue's history. So the doctor uses the issue's last activity as a stand-in. Any edit resets
    that, which means the doctor can only underestimate a wait. Everything it flags really has
    waited at least that long. The views above show the true durations.

## Related

- [Issues](issues/index.md): the states being measured
- [Teams, states and labels](teams.md): the shared list of states
- [Dashboards](dashboards.md): the drift views
- [Triage work](issues/triage.md): the decision clock
