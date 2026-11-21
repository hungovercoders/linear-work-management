# Project work

<div class="lwm-lead" markdown>
<span class="lwm-for">For delivery teams</span>

Project work is the planned kind: an issue inside a [project](../projects.md) that helps move
its Key Result.
</div>

## What a project issue needs

<div class="lwm-need" markdown>

- A project. The issue takes that project's `product/*` label
- One `type/*` [label](https://linear.app/docs/labels). If you're unsure, use `action`
- A priority, so it's clear what gets picked up next
- A description [someone could start from](index.md#the-body-is-the-prompt)

</div>

## Pick a type

The type decides which [template](https://linear.app/docs/issue-templates) the description uses.

`action`
:   Anything that needs doing: a code change, upkeep, a reminder to yourself. This is the default.

`feature`
:   A new capability. Write acceptance criteria.

`bug`
:   Something broken. Give steps to reproduce, and what you expected.

`analysis`
:   A data question or a report. The answer is the deliverable.

`spike`
:   A time-boxed investigation. Say what it unblocks and how long you'll spend.

!!! tip "Feature or action?"
    If someone gets a new capability when this ships, it's a `feature`. Otherwise it's an
    `action`. If you pick wrong, change the label.

## Create one

=== "With the skill"

    Ask Claude to "write up this issue". The [`linear-issue`](../skills/index.md) skill picks
    the type, writes the description from the matching template and sets the fields.

=== "By hand"

    1. Create the issue in the [project](https://linear.app/happydevs/projects/all).
    2. Set the `type/*` label, the project's `product/*` label, an assignee and a priority.
    3. Paste the matching template from the
       [`linear-issue` folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue)
       into the description.

Then take it through [Backlog, Planning and
Todo](index.md#backlog-planning-todo-commitment-then-readiness) before anyone starts.
