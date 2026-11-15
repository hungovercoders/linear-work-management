# Project work

<div class="lwm-lead" markdown>
For delivery teams. Project work is the planned kind: an issue that lives inside a
[project](../projects.md) and helps move its Key Result. Everything on the [Issues](index.md)
page applies here too.
</div>

!!! abstract "In short"
    - The issue sits in a project and takes that project's `product/*` label.
    - Give it one `type/*` label. If you're unsure, use `action`.
    - Give it a priority, so it's clear what gets picked up next.
    - Take it through `Backlog`, `Planning` and `Todo` before anyone starts.

---

## :material-tag-outline: Pick a type

The `type/*` label says what kind of work it is, and it decides which template the description
uses.

| `type/*` | Use it for | The description covers |
|---|---|---|
| `action` | Anything that needs doing: a code change, upkeep, a reminder to yourself. This is the default | What needs doing, why, and when it's done |
| `feature` | A new capability | What to add, the value to users, and acceptance criteria |
| `bug` | Something broken | What's broken, steps to reproduce, expected against actual, and impact |
| `analysis` | A data question or a report. The answer is the deliverable | The question, why it's needed, and what counts as answered |
| `spike` | A time-boxed investigation | The question, what it unblocks, the time box, and notes |

Every template also has a Context section and an empty `## Plan` section, which gets
[filled in when someone picks the issue up](index.md#prompt).

!!! tip "Feature or action?"
    Ask whether someone gets a new capability when this ships. If they do, it's a `feature`, and
    acceptance criteria are worth writing. Otherwise it's an `action`. If you pick wrong, just
    change the label.

The `product/*` label (`hungovercoders`, `dogadopt`, `woolwitch` and so on) comes from the
project, so you never decide it per issue. A `flow/*` label never goes on a project issue,
because that group is for [triage work](triage.md).

---

## :material-plus-circle-outline: Create one

1. The quick way is the [`linear-issue`](../skills/index.md) skill. It picks the type, writes
   the description from the matching template and sets the fields for you.
2. To do it by hand, create the issue in the
   [project's Linear view](https://linear.app/happydevs/projects/all). Set the project, the
   `type/*` label and the project's `product/*` label, then paste in the matching template from
   the [`linear-issue` skill folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue).
   They're the same files the skill uses.

Set the assignee and a priority (Urgent to Low) in [Linear's fields](index.md#fields). Then take
the issue through [`Backlog`, `Planning` and `Todo`](index.md#readiness) before anyone starts.

---

## Related

- [Issues](index.md): what every issue has in common
- [Projects](../projects.md): the project an issue lives in
- [Triage work](triage.md): the other kind of issue
