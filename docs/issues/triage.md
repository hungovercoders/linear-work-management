# Triage and BAU

<div class="lwm-lead" markdown>
<span class="lwm-for">For whoever is on triage duty</span>

BAU (business as usual) is the work nobody planned: an incident, a request, a reported fault.
It arrives in Triage, and your job is to decide where it goes.
</div>

## Your job on duty

[Triage](https://linear.app/docs/triage) is Linear's inbox for each team. New issues from Slack, integrations and
customers arrive there before they join the team's work.

One named person owns it at a time. You decide what happens to each item. You don't have to do
the work yourself.

The [`linear-triage`](../skills/index.md) skill will go through the inbox with you.

## How work arrives

Most of it comes from Slack. Each team has an asks channel, and anything raised there with
[Linear Asks](https://linear.app/docs/linear-asks-slack) becomes an issue in that team's Triage.

To raise a request, a colleague can:

- post in the team's asks channel and react with 🎫
- type `/asks` and pick a template
- mention `@Linear Asks` in a message

They don't need a Linear account. Linear replies in the Slack thread with a link to the issue,
and comments stay in step on both sides, so you can ask a question from Linear and they answer
in Slack.

Integrations, [customer requests](https://linear.app/docs/customer-requests) and the API also feed Triage, and
anyone can move a stray issue there by hand.

## Five things you can do with an item

<div class="lwm-node is-red"><b>Something arrives in Triage</b><span>From Slack, an integration or a customer.</span></div>
<div class="lwm-arrow"><small>whoever is on duty decides</small>↓</div>
<div class="lwm-cards">
  <div class="lwm-card is-slate"><span class="lwm-kicker">Accept</span><b>Into a project</b><span>A project already owns what this touches. Add it to the project with a <code>type/*</code> label.</span></div>
  <div class="lwm-card is-red"><span class="lwm-kicker">Accept</span><b>As BAU</b><span>It stands alone. Keep one <code>bau/*</code> label and no project.</span></div>
  <div class="lwm-card is-quiet"><span class="lwm-kicker">Move to team</span><b>Redirect</b><span>It belongs to another team.</span></div>
  <div class="lwm-card is-quiet"><span class="lwm-kicker">Merge or mark duplicate</span><b>Merge</b><span>Another issue already covers it.</span></div>
  <div class="lwm-card is-quiet"><span class="lwm-kicker">Decline</span><b>Decline</b><span>We won't do it. Give a reason.</span></div>
</div>

The small label on each card is the button to press in Linear. "Leave it there" isn't an
option.

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

??? note "Turning Triage on"
    Enable it under **Team settings → Triage**, and use **Triage responsibility** to put a named
    person on duty and rotate them.

    Integrations such as Sentry, GitHub, Zendesk and Intercom create issues straight into
    Triage. Setting up the asks channels is covered under
    [Integrations](../integrations.md#linear-asks).

    [Triage Intelligence](https://linear.app/docs/triage-intelligence) will suggest a label, a duplicate or an
    assignee. Treat it as a first guess.

??? note "Setting the deadlines up in Linear"
    Linear's [SLA rules](https://linear.app/docs/sla) measure time to completion. That suits the fix deadline. There's no rule
    for "decide within a day", so that one relies on the rota and on showing time in status on
    the Triage state.

    The fix deadline is an SLA rule. Under
    *Settings → Issues → SLAs*, add a rule filtered to `bau/vulnerability`, with severity taken
    from priority and durations in business days. Rules apply only to new or updated issues, the
    first match wins, and an issue can't have both an SLA and a due date.

    If you'd rather not depend on rules, the `linear-triage` skill sets the issue's
    `slaBreachesAt` date directly.

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
