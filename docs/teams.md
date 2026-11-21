# States and labels

<div class="lwm-lead" markdown>
The shared lists every team uses. If a value isn't on this page, it isn't shared.
</div>

## What's shared, and what's yours

A few things have to mean the same everywhere, or cross-team views stop working: the
[five rules](hard-rules.md), the states and labels on this page, the
[update schedule](communications.md) and the [triage deadlines](issues/triage.md#two-clocks).

How your team runs day to day is up to you. You can add your own states and labels. You can't
remove or rename a shared one.

!!! example "For example"
    The `happydevs` team has a Review Requested state next to the shared ones, and that's fine.
    Renaming `Done` would not be.

## Labels { #the-label-taxonomy }

Browse them in [Linear settings](https://linear.app/happydevs/settings/labels). Linear's docs explain
[label groups](https://linear.app/docs/labels).

| Group | Values | Goes on |
|---|---|---|
| `type/*` | `action` · `feature` · `bug` · `analysis` · `spike` | Project issues |
| `bau/*` | `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil` | BAU issues, one each |
| `spend/*` | `capex` · `opex` | Projects |
| `product/*` | `hungovercoders` · `dogadopt` · `woolwitch` · `cheeserater` · … | Projects, and their issues inherit it |

An issue never has both a `type/*` and a `bau/*` label. The old Improvement label belongs to no
group, so don't use it on new work.

## States { #the-shared-state-sets }

The closing state is spelled `Canceled`, the way Linear spells it.

### Initiatives

<ol class="lwm-flow">
  <li class="is-quiet"><b>Proposed</b></li>
  <li class="is-gate"><b>Planned</b></li>
  <li><b>Active</b></li>
  <li class="is-done"><b>Completed</b></li>
</ol>

These are built into Linear, so there's nothing to set up. [More on initiatives](initiatives.md)

### Projects

<ol class="lwm-flow">
  <li class="is-quiet"><b>Idea</b></li>
  <li class="is-quiet"><b>Scoping</b></li>
  <li class="is-gate"><b>Planned</b></li>
  <li><b>In Progress</b></li>
  <li><b>Launching</b></li>
  <li class="is-done"><b>Completed</b></li>
</ol>

There are also `Paused` and `Canceled`. They're set once for the workspace under Settings →
Projects.
[More on projects](projects.md)

### Issues { #issue-states }

<ol class="lwm-flow">
  <li class="is-bau"><b>Triage</b></li>
  <li class="is-quiet"><b>Backlog</b></li>
  <li class="is-gate"><b>Planning</b></li>
  <li><b>Todo</b></li>
  <li><b>In Progress</b></li>
  <li><b>In Review</b></li>
  <li class="is-done"><b>Done</b></li>
</ol>

There are also `Canceled` and `Duplicate`. Each team sets its own. [More on issues](issues/index.md)

## Suggestions for teams { #team-settings-recommended-not-required }

None of these are required.

- Turn [Triage](issues/triage.md) on, keep a named person on duty, and connect an asks channel
  in Slack.
- Run weekly [cycles](https://linear.app/docs/use-cycles). Anything bigger belongs in project
  milestones.
- Keep your Current and Upcoming cycle views visible to other teams.
- If you estimate, use the numbers for your own planning and don't compare them across teams.

## Membership { #membership }

Every team has a named owner and named members. [Teams](how-teams-work.md) explains what a team
owns and what it doesn't. We suggest each person has one home team, even
if they work across several projects. Manage teams in
[Linear settings](https://linear.app/happydevs/settings/teams).
