# The Hard Rules

Everything else in this guide is elaboration on these. If a rule and a convenience
conflict, the rule wins — that is what makes the model hold. **One rule per level, plus
two cross-cutting invariants: ownership and time-bounds.**

---

## 1. Every initiative declares its Key Results

An initiative is a **defined outcome, not a theme**. State its Key Results before any
project sits beneath it. It carries the *why* and *how it's judged*, never the *how it's
built*. A Key Result is either:

- **Measured** — a metric with a baseline and the target it moves to; or
- **Committed** — a binary deliverable with a Definition of Done, for work that just needs
  to happen (compliance, contracted, hard-deadline).

Then:

- **No Key Results, no initiative** — it's a wish, not an initiative.
- Those KRs are exactly what the projects below will name and move (rule 2). This is the
  measurement chain: initiatives *declare* KRs → projects *name which one(s)* → issues *do
  the work*.

---

## 2. Every project names the Key Result it moves, and by how much

A project exists to move a measure on an initiative. Name **which** KR and the **delta**
you expect (e.g. "activation 22% → 30%"). This turns "projects are the how" from an
aspiration into something checkable.

**Work starts as a project in `Idea`.** That's the entry point for planned work — no
initiative or KR needed to begin. `Idea` and `Scoping` are *discovery*, where a project may
legitimately have **no parent and no named KR**; it's also where the work of *forming* an
initiative gets recorded. **The rule bites from `Planned`**, where discovery resolves into one
of four:

- **Link** to an existing initiative (and name the KR + delta it moves);
- **Graduate** into — or seed — a **new** initiative (a deliberate strategic step, distinct
  from the flow *promotion* we don't do);
- Proceed **standalone** — allowed, but questioned (nothing to ladder to);
- **Drop** it (Cancelled).

- A project can belong to **more than one initiative** — when it does, name the KR and delta
  it moves on **each**. Every committed KR carries a named delta.
- **Completed** means delivered *and* the KR delta observed — not merely shipped.

---

## 3. Every issue is in a project *or* carries one `flow/*` label — never both, never neither

Every issue is **classified**. Two ways are valid; two are failures.

| | State | Meaning |
|---|---|---|
| ✓ | In a project | Planned work, laddering to a KR |
| ✓ | One `flow/*` label, no project | Inbound work with its own front door |
| ✗ | Both at once | Pick one, drop the other |
| ✗ | Neither | **Unclassified** — invisible work, the defect the system chases |

`flow/*` is how inbound work stays visible without faking a project around it. The
`linear-doctor` skill reports every unclassified issue.

---

## 4. One named human owns each initiative and each project

Ownership is singular and named. **Not a team, not two people — a person.**

- **Initiative** owner: strategic seniority. Answers *why this matters* and *how we
  know it worked*.
- **Project** lead: the deliverer (eng lead or product owner). Answers *what, how,
  and by when*. Exactly one.
- Teams still own issues and a project can draw on several teams — but accountability
  for the project rests with its single lead.

---

## 5. Initiatives and projects carry dates from `Planned` onward

Undated work can't be prioritised or sequenced. Dates are what make **dependency mapping**
and **on-track delivery** possible — upcoming work can see what it depends on and whether
that will land in time. Because prioritisation happens *before* work starts, the date is set
when the work is **agreed**, not when it becomes active.

- **Initiatives:** from **`Planned`** onward, carry a timeframe / target date (OKR-style —
  often a quarter, but some run a year or more), set alongside the owner and KRs when the
  initiative is agreed. `Active` means work is now **underway against that date** — not that
  the date appears for the first time. A `Proposed` initiative that isn't agreed yet is
  exempt until it's planned.
- **Projects:** from **`Planned`** onward carry a **start** and a **target end** date.
  `Idea` and `Scoping` projects are still being shaped, so dates firm up as they commit —
  which is exactly what `Planned` means ("agreed, dated, resourced").
- Dependencies between projects (drawn at the project level) only tell you about risk once
  both ends have dates.

---

These are what the [`linear-doctor`](skills/index.md) skill checks first, and what every
other page here assumes. Back to the [cheat sheet](index.md).
