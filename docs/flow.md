# Flow

<div class="lwm-lead" markdown>
How to tell where work is getting stuck. When one stage can't keep up, issues pile up in the
state before it. Look at how long they've waited and the bottleneck shows itself.
</div>

## What a long wait means

Planning
:   Refinement can't keep up. *Schedule refinement time, pull less in, and move what you won't
    do soon back to Backlog.*

Todo
:   Ready work nobody is starting. *Start what's refined before refining more.*

In Progress
:   Issues are too big, or quietly blocked. *Split them, and record blockers as relations.*

In Review
:   Not enough reviewing. *Make changes smaller, or review before starting something new.*

Backlog is left out on purpose. An old item there is an idea someone parked, and that's allowed.

Use the numbers to start a conversation with evidence behind it.

## Set up the views

You only need a few shared views in Linear.

1. One view each for `Planning`, `Todo` and `In Review`. Filter to open issues, sort oldest
   first and turn on **time in status** in the [display
   options](https://linear.app/docs/display-options). The top issue is your longest wait.
2. A board of open issues grouped by state, to see how deep each queue is.
3. With [Linear Insights](https://linear.app/docs/insights), chart open issues by state with average
   age and watch the trend.

## What the doctor flags

`task doctor` picks up long waits even when nobody is watching the views.

| State | Flagged after |
|---|---|
| Planning | 10 days |
| Todo | 14 days |
| In Review | 5 days |

??? note "How the doctor measures the wait"
    Linear doesn't record when an issue entered its state, so the doctor uses the last activity.
    Any edit resets that, so it can only underestimate. Everything it flags has waited at least
    that long.
