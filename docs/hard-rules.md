# The Three Hard Rules

Everything else in this guide is elaboration on these three. If a rule and a
convenience conflict, the rule wins — that is what makes the model hold.

---

## 1. Every project names the Key Result it moves, and by how much

A project exists to move a measure on an initiative. Name **which** KR and the
**delta** you expect (e.g. "activation 22% → 30%"). This turns "projects are the how"
from an aspiration into something checkable.

- **No KR named, no project.** Scoping can start; committed delivery cannot.
- **Completed** means delivered *and* the KR delta observed — not merely shipped.
- Genuinely standalone work is allowed but **questioned**: if it ladders to no
  initiative, either the work is wrong or the initiative is missing.

---

## 2. Every issue is in a project *or* carries one `flow/*` label — never both, never neither

Every issue is **classified**. Two ways are valid; two are failures.

| | State | Meaning |
|---|---|---|
| ✓ | In a project | Planned work, laddering to a KR |
| ✓ | One `flow/*` label, no project | Inbound work with its own front door |
| ✗ | Both at once | Pick one, drop the other |
| ✗ | Neither | **Unclassified** — invisible work, the defect the system chases |

`flow/*` is how unplanned work stays visible without faking a project around it.
Recurring flow themes get **promoted** into a project. The `linear-doctor` skill
reports every unclassified issue.

---

## 3. One named human owns each initiative and each project

Ownership is singular and named. **Not a team, not two people — a person.**

- **Initiative** owner: strategic seniority. Answers *why this matters* and *how we
  know it worked*.
- **Project** lead: the deliverer (eng lead or product owner). Answers *what, how,
  and by when*. Exactly one.
- Teams still own issues and a project can draw on several teams — but accountability
  for the project rests with its single lead.

---

These three are what the [`linear-doctor`](skills/index.md) skill checks first, and
what every other page here assumes. Back to the [cheat sheet](index.md).
