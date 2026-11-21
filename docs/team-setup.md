# Recommended team setup

<div class="lwm-lead" markdown>
<span class="lwm-for">For team owners</span>

A starting point for setting a team up in Linear and running it quarter by quarter. Treat it as
a first draft. Run a retrospective on it like anything else, and change what doesn't work.
</div>

??? abstract "See it as a diagram"
    ![A team's rhythm: set objectives at the start of the quarter, run repeated cycles, then score and reflect at the end.](diagrams/team-rhythm.svg)

## What every team should have

<div class="lwm-need" markdown>

- A mission that rarely changes, and a few tenets for how the team works
- Three objectives a quarter, each with three Key Results
- An objective zero for keeping the lights on
- [Triage](issues/triage.md) switched on, one person on duty, and an asks channel in Slack
- [Cycles](https://linear.app/docs/use-cycles) at a steady length
- Its objectives somewhere every member sees them daily

</div>

## Set it up in Linear

1. Create the team with a named owner. Give each person one home team.
2. Keep the [shared issue states](teams.md#issue-states). Add your own only if you need them.
3. Turn Triage on, set Triage responsibility, and
   [connect the team's asks channel](integrations.md#linear-asks).
4. Turn cycles on. Start weekly, or fortnightly if a week is too short to finish anything.
5. Create one [initiative](initiatives.md) for each objective, with your team as its lead team.
6. Add the team's initiatives and current cycle to everyone's sidebar favourites, and keep the
   cycle views open to other teams.

## Objectives, one quarter at a time

An objective is an initiative. A Key Result measures it. A project is a hypothesis about how to
move a Key Result, and its issues are the work that tests the hypothesis.

Pick three objectives. More than that and none of them gets enough attention.

Give each one three Key Results with numbers, so partial success still counts. Getting to 70%
of a stretching target usually beats hitting an easy one. Aim for targets the team is 70 to 80%
likely to reach, and say which ones are must-haves. In this guide a must-have is a
[committed](initiatives.md#writing-key-results) Key Result and a stretch is a measured one.

Then use the objectives for every priority call. A request that serves none of them is a fair
"no", and because other teams can see your objectives, they can see why.

## Objective zero

Some work has to happen whatever the strategy says: fixing incidents, patching, answering
support. Give that work its own objective, numbered zero, whose Key Results are the service
levels you promise.

- No critical vulnerabilities open at the end of the quarter
- 99.95% uptime
- Nothing running within three months of its end of life

In Linear this is one more initiative led by the team. Its work is the team's
[BAU issues](issues/triage.md), which carry a `bau/*` label and need no project.

Treat objective zero as the most important objective, and expect it to be the smallest. If it
starts taking most of the team's time, don't absorb that quietly. Drop one of the three
objectives, or make next quarter's objective fixing whatever keeps breaking.

## The rhythm

| When | What | For how long |
|---|---|---|
| Start of the quarter | Scene setting: the company's strategy, the team's mission and tenets | Up to a day |
| | Choose objectives and Key Results. Sleep on them before confirming | Up to two days |
| | Impact planning: turn the best hypotheses into projects and first issues | Up to two days |
| Every cycle | Plan it around one goal that names the Key Result it serves | Up to 90 minutes |
| | Review what moved, then a retrospective | Up to an hour, then up to 90 minutes |
| Every week | Refinement: move issues through [Backlog, Planning and Todo](issues/index.md#backlog-planning-todo-commitment-then-readiness) | Up to two hours |
| | Zero tolerance: check errors, vulnerabilities and ageing software against objective zero | Up to an hour |
| Every day | Stand-up. Walk the board from right to left, so the talk is about finishing work | 15 minutes |
| End of the quarter | Score the Key Results, hold a retrospective, and celebrate | Up to four hours |

Each of these has a home in Linear. The cycle review feeds the weekly
[project update](communications.md). Zero tolerance uses the
[SLA health and drift views](dashboards.md). Refinement uses the [Flow](flow.md) views.

## What to avoid

A second way of prioritising
:   If objectives decide some things and a separate list decides others, the team is back to
    arguing in every planning session.

Key Results tied to anyone's pay
:   People start gaming the number, and the shared goal is lost. Reward what someone did for
    their own skills, their team and other teams.

Objectives nobody sees
:   If they only appear at the quarterly review, they won't steer the daily work.

Refining requests that serve no objective
:   Look at every unplanned request in refinement. If it serves no objective, decline it.

??? note "If this is new to the team"
    Start with monthly objectives. You'll find out sooner whether they're working, and you can
    change course before committing to a full quarter.

??? note "Choosing objectives: eight things to look at"
    Go through these with real numbers in front of you. If you find you're guessing, make
    getting the numbers your first objective.

    Precision
    :   Can we tell which of the others needs attention? Do we have the data?

    Performance
    :   How well are our products doing? Conversion, satisfaction, coverage.

    Deliverability
    :   How fast can we ship a change? Lead time, deploys a day, rollbacks.

    Cost
    :   What are we spending on cloud and contracts?

    Reliability
    :   Uptime, and how many alerts we get.

    Risk
    :   Critical vulnerabilities and compliance events.

    Developer experience
    :   Is the team happy building here? Complexity, skills coverage.

    Integration
    :   How easily can other teams use what we produce?

??? note "Where this comes from"
    The cadence, objective zero and the eight things to look at come from
    [Integrating OKR Cycles into the Agile Framework](https://hungovercoders.com/blog/2024-02-24-okr-agile-cycles/),
    adapted to how this guide uses Linear. A team leading an initiative needs Linear's Business
    or Enterprise plan. On other plans, name the team in the initiative's description.
