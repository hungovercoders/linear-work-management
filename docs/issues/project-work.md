# Project work

<div class="lwm-lead" markdown>
For delivery teams. A **project issue** lives **inside a [project](../projects.md)** and moves
its Key Result — planned work on the strategic path. This page covers what's specific to project
issues; the [shared issue model](index.md) — the lifecycle, the body-as-prompt, native fields —
applies underneath.
</div>

A project issue sits **in a project** ([rule 3](../hard-rules.md) classification), inherits that
project's `product/*`, carries one `type/*`, and ladders to the project's KR. Like every issue,
it's refined **Backlog → Todo** before anyone starts — that's the [readiness
gate](index.md#backlog-vs-todo-the-readiness-gate).

---

## :material-tag-outline: Labels — `type/*` and `product/*`

One **`type/*`** label says what kind of work it is; **`product/*`** carries down from the
project unchanged. **`action` is the default** — reach for `feature`, `bug`, `analysis` or
`spike` only when the work is specifically one of those.

| `type/*` | For | The template emphasises |
|---|---|---|
| `action` | **The default** — any work that needs doing, from a code change to upkeep to a reminder to yourself | What needs doing, and when it's done |
| `feature` | A new capability | The change and its acceptance criteria |
| `bug` | Something's broken | Steps to reproduce, expected vs actual |
| `analysis` | A data question to answer or a report to produce — the deliverable is the answer, not shipped code | The question, and the answer/report |
| `spike` | A time-boxed investigation | The question and the time box |

`product/*` (`hungovercoders` · `dogadopt` · `woolwitch` · …) is **inherited from the project** —
same value, so work stays attributable to the product it serves without re-deciding it per
issue. `flow/*` never appears on a project issue — that's the [triage](triage.md) group.

## :material-sort-variant: Priority

Every issue carries a **priority** (Urgent → Low) that orders it within the project — what gets
picked up next when someone frees up. It's a native field, not a line in the description.

---

## :material-file-document-multiple-outline: The templates — one per `type/*`

The [`linear-issue`](../skills/index.md) skill writes the description body from the template that
matches the type. Every template keeps the same non-negotiables — a native-fields header, a
**why**, and a **`## Plan`** section left empty at creation and filled at pickup — and varies the
middle:

| `type/*` | Body |
|---|---|
| `action` (default/base) | What needs doing? / Why? / When is it done? / Context / Plan |
| `feature` | What needs doing? / Why (user value) / Acceptance criteria / Context / Plan |
| `bug` | What's broken? / Steps to reproduce / Expected vs actual / Impact / Context / Plan |
| `analysis` | The question / Why it's needed / When it's answered / Context / Plan |
| `spike` | The question / Why (what it unblocks) / Time box / Notes / Plan |

---

## :material-plus-circle-outline: Create one

The description body is the only thing that lives as text; everything else is a
[native field](index.md#native-fields-not-prose).

1. **Use the [`linear-issue`](../skills/index.md) skill — preferred.** It picks the `type/*`,
   writes the body from the template for that type, and sets the native fields — assignee,
   priority, status, project, labels — for you.
2. **By hand.** Create the issue in the [project's Linear view](https://linear.app/happydevs/projects/all),
   set the project, `type/*` and inherited `product/*`, then paste the **template for the `type/*`**
   from the
   [`linear-issue` skill folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue)
   into the description and fill it in. They're the same files the skill uses.

Refine it **Backlog → Todo** before anyone starts.

---

## Related

- [Issues](index.md) — the shared model every issue follows
- [Projects](../projects.md) — the project a project issue lives in and the KR it moves
- [Triage work](triage.md) — the other kind of issue, for inbound work
