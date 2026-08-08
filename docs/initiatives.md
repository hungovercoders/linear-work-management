# Initiatives

<div class="lwm-lead" markdown>
For strategic leadership. An initiative is a **measurable outcome** — the *why* behind a
body of work and *how we'll know it worked*. It is never a task list, and never the *how
it's built*: that lives in the [projects](index.md) beneath it.
</div>

This page expands the [cheat sheet](index.md)'s Initiatives section. If the two ever
disagree, the cheat sheet wins and this page is wrong — tell us.

---

## What an initiative is

You own an **outcome**, not a backlog. An initiative carries two things and delegates the
rest:

- **Why it matters** — the strategic reason the work exists.
- **How we'll know it worked** — the Key Results that move.

Everything about *how* the outcome gets built belongs to the projects underneath. Keep the
initiative about ends, not means.

!!! danger "A theme is not an initiative"
    "Improve onboarding" is a theme — there's nothing to hit. "Raise activation from 22% to
    30% by Q4" is an initiative. If you can't tell whether you succeeded, it isn't one yet.

---

## Declare the Key Results first

**[Hard rule 1](hard-rules.md):** every initiative declares its Key Results *before* any
project sits beneath it. A Key Result is a metric with a target — the number that will move
and where it moves to. Write them as a table in the initiative's description.

| Key Result | Baseline | Target | How it's measured |
|---|---|---|---|
| Activation rate | 22% | 30% | Signups reaching first value in 7 days |
| Weekly active teams | 140 | 200 | Teams with ≥1 active member per week |
| Support load per team | 1.8 tickets/wk | < 1.0 | Triage volume ÷ active teams |

Those Key Results are exactly what the projects below will **name and move** — that's
[rule 2](hard-rules.md). The chain is: initiatives *declare* KRs → projects *name which
one(s) and the delta* → issues *do the work*. Every issue in your cycle should trace back up
this line.

!!! abstract "The KR table is the contract"
    No KR table, no initiative — it's a wish. Once written, it's what your delivery leads
    commit against and what you'll score at the end.

---

## Own it

**[Hard rule 4](hard-rules.md):** one named human owns the initiative — someone with the
strategic seniority to answer *why this matters* and *how we know it worked*. Not a team,
not two people sharing it. The owner is accountable for the outcome, not for building it.

---

## Time-bound it

**[Hard rule 5](hard-rules.md):** once an initiative is **Active**, it carries a target
date. Undated strategy can't be prioritised or sequenced against anything else.

Set the timeframe to the **outcome, not a calendar habit**:

- Many initiatives fit a **quarter** — a clean OKR rhythm.
- Some run a **year or more** — a large programme, a multi-phase bet. That's fine; give it
  a real horizon and revisit the KRs as it progresses.

---

## States and the two gates

Initiative states are a **fixed set** — Linear doesn't let you customise them. Five states,
each with a plain definition of done:

| State | Means | Move on when |
|---|---|---|
| Proposed | Being considered; not yet agreed | Leadership agrees it's worth doing |
| Planned | Agreed & prioritised, owner named, KRs written — not started | Work is ready to begin |
| Active | Underway — projects are moving its KRs; time-bound | KRs are achieved, or the window closes |
| Completed | KRs achieved, or the timeframe closed and scored | — |
| Canceled | Dropped; reason recorded | — |

Two transitions carry real weight:

| Gate | From → To | What has to be true |
|---|---|---|
| **Strategic agreement** | Proposed → Planned | Leadership agrees; a single owner is named; the KR table is written |
| **Kick-off** | Planned → Active | Work starts and the initiative becomes time-bound (target date set) |

Everything after Active is bookkeeping: score the KRs and mark it **Completed**, or record
why and mark it **Canceled**.

---

## Sub-initiatives — optional, larger programmes only

!!! note "Enterprise-plan feature"
    Sub-initiatives are only available on Linear's **Enterprise** plan. If you're not on it,
    keep the model flat: **initiative → project**. Nothing below is required.

When a programme is large or long-running, you can **nest** initiatives — a parent with
sub-initiatives beneath it, up to five levels deep. A parent automatically rolls up all the
projects and progress of its children, so you get one view of the whole programme while each
sub-initiative stays independently owned and scored.

Reach for them when:

- a company objective spans **several teams or departments**, each needing its own owner and
  KRs; or
- a large goal breaks into **phases or workstreams** that are worth tracking on their own.

Keep the top-level initiative about the overall outcome; let each sub-initiative carry its
own slice of the KR table.

---

## Keep everyone posted

While an initiative is **Active**, its owner ensures a **monthly update** goes to
`#initiatives` — KR movement and any risks. Health is a claim with evidence, not a colour
someone picked. The standard formats and the full cadence live in the Communication guide.

---

## The initiative template

Paste this into a new Linear initiative's description and fill it in. It captures the four
things an initiative must state: **why, the KR table, the owner, and the timeframe**.

```markdown
# <Initiative name — the outcome, not the theme>

**Why this matters:** <the strategic reason; what changes if we succeed>
**Owner:** <one named person, strategic seniority>
**Timeframe:** <target date — a quarter, or longer>

## Key Results
| Key Result | Baseline | Target | How it's measured |
|------------|----------|--------|-------------------|
| <metric>   | <from>   | <to>   | <the query/report that proves it> |

## Out of scope
<what this initiative is deliberately not doing, so projects don't sprawl>
```

---

## Related

- [The Hard Rules](hard-rules.md) — rules 1 (declare KRs), 4 (single owner), 5 (time-bounds)
- [The Cheat Sheet](index.md) — the one-page summary this expands
