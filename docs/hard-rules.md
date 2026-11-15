# The hard rules

<div class="lwm-lead" markdown>
There are five. Everything else in this guide is detail on top of them, and if a rule and a
shortcut ever disagree, the rule wins.
</div>

---

## 1. Every initiative says how it will be measured

An initiative is an outcome we want, such as "make onboarding effortless". On its own, that is
only a good sentence. It becomes an initiative once it has Key Results (KRs): the few things that
will be true if it worked.

A Key Result is one of two kinds.

| Kind | What it is | Example |
|---|---|---|
| Measured | A number with a starting point and a target | Activation rate from 22% to 30% |
| Committed | Something that is either done or not, with a clear definition of done | SOC 2 Type II report issued |

Write the Key Results before any project goes underneath. Each project will pick one to move, so
they have to exist first.

---

## 2. Every project says which Key Result it moves, and by how much

A project exists to move a number on an initiative. So it names the Key Result and the change it
expects (its delta), for example "activation 22% → 30%". Anyone can then check whether the project did its
job.

You don't need this on day one, because a project starts life as an idea.

| Stage | What the project needs |
|---|---|
| `Idea` or `Scoping` | A named lead and a description of what it's exploring. No Key Result, no dates and no initiative yet |
| `Planned` onward | The Key Result it moves and by how much, plus dates |

Reaching `Planned` is the moment to decide what the idea turned into:

- Most projects join an initiative and name the Key Result they'll move. We call this
  graduating. The initiative can be an existing one, or a new one that the project's findings
  justify.
- A project can go ahead with no initiative. That's allowed, but expect to be asked why, because
  the work then connects to nothing above it.
- Or the project is dropped (`Canceled`). For an idea, that's a perfectly good result.

Two more details. A project that serves several initiatives names a Key Result and a change for
each one. And `Completed` means the work shipped and the Key Result moved, so shipping alone
doesn't close a project.

---

## 3. Every issue is in a project or has one `flow/*` label

Every issue has to belong somewhere, and there are two places it can belong.

| | The issue is… | Which means |
|---|---|---|
| ✓ | In a project | Planned work that connects to a Key Result |
| ✓ | Carrying one `flow/*` label, with no project | Unplanned work that arrived, visible in its own right |
| ✗ | Both | Pick one and drop the other |
| ✗ | Neither | Unclassified. Nobody can see where it belongs |

The `flow/*` labels exist so that unplanned work doesn't need a pretend project around it. The
`linear-doctor` skill lists every unclassified issue.

---

## 4. One named person owns each initiative and each project

When two people own something, each can assume the other has it. So ownership is always one
person, by name.

- An initiative has one owner, someone senior enough to say why it matters and how we'll know it
  worked.
- A project has one lead, the person delivering it (usually an eng lead or product owner). They
  answer what, how and by when.
- Teams still own issues, and a project can draw on several teams. The lead is the one who
  answers for the project.

---

## 5. Initiatives and projects have dates once they're `Planned`

Work with no date can't be put in order against other work. And nobody waiting on it can tell
whether it will arrive in time.

- Initiatives get a target date when they're agreed, which is `Planned`. Often that's a quarter,
  and sometimes a year or more. `Active` then means work is underway against that date. A
  `Proposed` initiative doesn't need one yet.
- Projects get a start date and a target end date at `Planned`. Projects in `Idea` and `Scoping`
  are still taking shape, so they're exempt.
- Dependencies between projects only tell you something once both projects have dates.

---

The [`linear-doctor`](skills/index.md) skill checks these five first. Back to
[Start here](index.md).
