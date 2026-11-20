# Triage and BAU

<div class="lwm-lead" markdown>
<span class="lwm-for">For whoever is on triage duty</span>

BAU (business as usual) is the work nobody planned: an incident, a request, a reported fault.
It arrives in Triage, and your job is to decide where it goes.
</div>

## Your job on duty

Triage is Linear's inbox for each team. New issues from integrations, customers and colleagues
arrive there before they join the team's work.

One named person owns it at a time. You decide what happens to each item. You don't have to do
the work yourself.

The [`linear-triage`](../skills/index.md) skill will go through the inbox with you.

## Five things you can do with an item

"Leave it there" isn't one of them.

Accept into a project
:   A project already owns the thing this touches. **Accept**, add it to the project and give it
    a `type/*` label.

Accept as BAU
:   It stands alone. **Accept**, and keep one `bau/*` label with no project.

Redirect
:   It belongs to another team. **Move to team**.

Merge
:   Another issue already covers it. **Merge** or **Mark duplicate**.

Decline
:   We won't do it. **Decline**, with a reason.

Work accepted as BAU joins the team's normal [states](index.md#the-shared-lifecycle) alongside
everything else. It isn't a lesser queue.

## The `bau/*` labels

BAU work gets exactly one, and no `type/*` label.

`incident`
:   Something is down or degraded and needs a response now.

`vulnerability`
:   A security weakness. Its severity sets the deadline.

`defect`
:   A fault someone reported.

`query`
:   A one-off data question.

`compliance`
:   A regulatory or policy obligation.

`support`
:   A user or customer request.

`toil`
:   Recurring manual work worth recording.

## How fast { #two-clocks }

| Deciding where it goes | Within |
|---|---|
| `incident` | Immediately |
| `vulnerability`, `support` | 1 working day |
| Everything else | 2 working days |

Vulnerabilities also have a fix deadline: 7 days for Critical, 30 for High, 90 for Medium.

Set a priority as you decide. It orders the work and can drive the deadline.

!!! tip "The same thing keeps arriving?"
    If one kind of BAU work comes back every cycle, propose a [project](../projects.md) for it
    in the usual way. There's no shortcut that turns it into one.

??? note "Turning Triage on, and how work reaches it"
    Enable it under **Team settings → Triage**, and use **Triage responsibility** to put a named
    person on duty and rotate them.

    Integrations such as Sentry, GitHub, Zendesk and Intercom create issues straight into
    Triage, as do customer requests, forms and the API. Anyone can move a stray issue there by
    hand. Linear Asks can send Slack requests too, but it needs a plan and a Slack connection we
    don't have yet ([Integrations](../integrations.md)).

    Triage Intelligence will suggest a label, a duplicate or an assignee. Treat it as a first
    guess.

??? note "Setting the deadlines up in Linear"
    Linear's SLA rules measure time to completion. That suits the fix deadline. There's no rule
    for "decide within a day", so that one relies on the rota and on showing time in status on
    the Triage state.

    The fix deadline is an SLA rule on the Business and Enterprise plans. Under
    *Settings → Issues → SLAs*, add a rule filtered to `bau/vulnerability`, with severity taken
    from priority and durations in business days. Rules apply only to new or updated issues, the
    first match wins, and an issue can't have both an SLA and a due date.

    On other plans the `linear-triage` skill sets the issue's `slaBreachesAt` date directly.

??? note "Why `defect` and `query`, when project work has `bug` and `analysis`?"
    Linear label names must be unique across the workspace. The `type/*` group already uses
    `bug` and `analysis`, so the BAU equivalents needed different names.

??? note "Writing up a BAU issue yourself"
    Most arrive without your help. When you do need to write one, the
    [`linear-issue`](../skills/index.md) skill sets the single `bau/*` label and writes the
    description. By hand, create it in the
    [team's view](https://linear.app/happydevs/team/GRI/all) with one `bau/*` label and no
    project, using `template-bug` for a defect, `template-analysis` for a query and
    `template-action` for anything else.
