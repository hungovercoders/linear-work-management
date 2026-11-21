# Issues

<div class="lwm-lead" markdown>
<span class="lwm-for">For anyone doing the work</span>

An issue is one task: small enough for one person to finish, and clear enough that everyone
agrees when it's done.
</div>

[Open the issues list in Linear](https://linear.app/happydevs/team/GRI/all){ .md-button }

??? abstract "See it as a diagram"
    ![Issue lifecycle: Triage and project work both lead to Backlog, then Planning, Todo, In Progress, In Review and Done.](../diagrams/issue-lifecycle.svg)

## Two kinds

Every issue is one or the other. Never both, never neither.

<div class="lwm-cards" markdown="block">

[<span class="lwm-kicker">Planned</span><b>Project work</b><span>Lives in a project and helps move its Key Result. Gets a <code>type/*</code> label.</span>](project-work.md){ .lwm-card .is-slate }

[<span class="lwm-kicker">Arrived</span><b>BAU work</b><span>An incident, a request, a reported fault. Gets one <code>bau/*</code> label and no project.</span>](triage.md){ .lwm-card .is-red }

</div>

Every issue also belongs to exactly one team, whichever kind it is. A project can span teams,
but an issue can't ([how teams fit](../how-teams-work.md)).

## Write it so someone can start { #the-body-is-the-prompt }

Write the description for whoever picks it up, whether that's a colleague or an AI agent. Say
what the problem is and what done looks like. If they'd have to come and ask you something, it
isn't finished.

Leave the `## Plan` section empty. Whoever picks the issue up works out how to do it and writes
the plan there, so the approach can be reviewed before any code is.

## Use Linear's fields { #native-fields-not-prose }

Assignee, priority, status, labels and links all have their own
[fields in Linear](https://linear.app/docs/issue-properties). Put them
there and keep them out of the description. Fields can be filtered, sorted and reported on.
Text in a description can't.

## The states { #the-shared-lifecycle }

<ol class="lwm-flow">
  <li class="is-bau"><b>Triage</b>Waiting for a decision</li>
  <li class="is-quiet"><b>Backlog</b>Written down, no promise</li>
  <li class="is-gate"><b>Planning</b>Committed, working out the details</li>
  <li><b>Todo</b>Ready to pick up</li>
  <li><b>In Progress</b>Being worked on</li>
  <li><b>In Review</b>Being reviewed</li>
  <li class="is-done"><b>Done</b>Shipped and accepted</li>
</ol>

Project work starts in Backlog. BAU work starts in Triage and joins Backlog once it's
accepted. An issue can also end as `Canceled` or `Duplicate`.

### Backlog, Planning and Todo { #backlog-planning-todo-commitment-then-readiness }

These three are easy to blur, so here's what separates them.

Backlog
:   A parking place. Nobody has promised anything, and nobody is counting how long it sits.

Planning
:   The team has said yes and is sharpening it: requirements, what done means, size, blockers.
    Time here is counted, because a growing Planning column means refinement can't keep up.

Todo
:   Ready. Someone can start without coming back to ask what it means.

Nothing starts from Backlog or Planning.

