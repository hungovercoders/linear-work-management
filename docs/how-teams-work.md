# Teams

<div class="lwm-lead" markdown>
<span class="lwm-for">For everyone</span>

In Linear a [team](https://linear.app/docs/teams) owns issues. It doesn't own projects or
initiatives. Most confusion about who owns what clears up once you know that.
</div>

??? abstract "See it as a diagram"
    ![Where teams fit: an initiative has no team, a project can span teams, and each issue belongs to exactly one team.](diagrams/teams.svg)

## Loose at the top, strict at the bottom

Linear gets stricter about teams the further down you go.

<div class="lwm-levels">
  <div class="lwm-level"><b>Initiative</b><span>Belongs to no team. It can hold projects from anywhere in the company.<small>One owner</small></span></div>
  <div class="lwm-level"><b>Project</b><span>Belongs to one team, or is shared across several. It can hold issues from each of them.<small>One lead</small></span></div>
  <div class="lwm-level"><b>Issue</b><span>Belongs to exactly one team. It can't be shared.<small>One assignee</small></span></div>
</div>

That's deliberate. Outcomes don't follow the org chart: "Effortless rescue-dog adoption" needs
web, data and partnerships work. So the levels that describe outcomes are free to cross teams.
The restriction arrives at the issue, because that's where one person in one team has to do
something.

## What a team owns

Its issues
:   Every issue has exactly one team. You can see which in its ID: `WEB-12` belongs to Web.

Its Triage inbox
:   Requests to the team arrive in [its own Triage](issues/triage.md), from its own asks channel.

Its cycles
:   An issue is planned into its own team's cycle. You can't see two teams' cycles in one view.

Its states
:   Each team has the [shared states](teams.md#issue-states), and can add its own.

## What a team doesn't own

Projects
:   A project can be shared by several teams. One of them is its lead team, and Linear shows a
    tab for each team's issues. The project still has one lead.

Initiatives
:   These sit above every team, in one list for the whole workspace.

Labels
:   Our [label groups](teams.md#the-label-taxonomy) are set for the whole workspace, so `bau/support`
    means the same in every team.

## So who is accountable?

A team can't be, for anything above an issue, because projects and initiatives cross teams.
That's why [rule 4](hard-rules.md) asks for one named person.

An initiative
:   Its owner.

A project
:   Its lead, however many teams contribute.

An issue
:   Its assignee, inside the team it belongs to.

## Working across teams

You need something from another team
:   Add that team to your project and create the issue in their team. It arrives in their
    Triage, they decide when to do it, and it still shows in your project.

One piece of work needs two teams
:   Make two issues, one in each team, in the same project. Link them as blocking or related
    if the order matters.

An issue is in the wrong team
:   Move it. It gets a new ID (the old one still works), its status changes to the nearest
    match in the new team, and it may drop out of its cycle.

You're not sure whose cycle it's in
:   The issue's team. Projects don't live in cycles. Their issues do, each in its own team's.

??? note "Sub-teams and private teams"
    Linear lets you nest teams. A [sub-team](https://linear.app/docs/sub-teams) can inherit its
    parent's states, cycles and labels, and the parent's views show every sub-team's work. A
    team can also be private, which hides its issues from everyone outside it. Neither changes
    the rule above: each issue still belongs to exactly one team.
