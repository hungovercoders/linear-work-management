# Initiatives

<div class="lwm-lead" markdown>
For strategic leadership. An **initiative** in [Linear](https://linear.app/happydevs/initiatives)
is a defined outcome: the *why* behind a body of work and *how we'll know it worked*. It isn't
a task list, and it isn't the *how it's built*; that belongs to the [projects](projects.md)
beneath it. It sits alongside those projects and their issues, in the same tool.
</div>

[Every initiative in Linear sits on one screen.](https://linear.app/happydevs/initiatives)
That view is the whole of our strategy in one place: every outcome we're betting on, who owns
it, and how it's tracking. Scan it to see where the organisation is pointed, what's active
versus still proposed, and that your own work traces up to one of them.

---

## What an initiative is

You own an outcome, not a backlog. An initiative carries two things and delegates the rest:

- Why it matters: the strategic reason the work exists.
- How we'll know it worked: the Key Results that move.

Everything about *how* the outcome gets built belongs to the projects underneath. Keep the
initiative about ends, not means.

!!! danger "An objective isn't an initiative until it has Key Results"
    The name should be an inspiring objective. "Make onboarding effortless" is a good one. On
    its own, though, that's just a theme. It becomes an initiative only once it declares the
    Key Results that make it measurable (next section). You need both: an inspiring objective
    in the name, Key Results underneath.

---

## Where an initiative comes from

Initiatives rarely spring up fully formed. There are three ways one starts, and the question
behind all of them is the same: what evidence is this outcome built on?

```kroki-d2
@from_file:diagrams/initiative-origin.d2
```

- **Spontaneous**: a fresh strategic bet with no project behind it. Leadership names an outcome
  directly. Legitimate, but it still has to earn its Key Results like any other.
- **Graduation**: a single discovery project (`Idea`/`Scoping`) matures into an outcome big
  enough to stand on its own. At the [`Planned` gate](projects.md#discovery-phase-is-there-something-here-idea-scoping)
  it seeds a new initiative or links to an existing one. Most initiatives arrive this way.
- **Aggregation**: several discovery projects turn out to be facets of one larger outcome, and
  their findings combine into a single initiative that then coordinates them.

However it starts, the initiative declares its Key Results (below). The projects that fed it
either continue as delivery projects beneath it or close once their discovery job is done, so
the exploratory work always has a home.

When an initiative comes from project work, the `linear-initiative` skill asks whether it draws
on one or more discovery projects. If it does, the skill grounds the objective and the KR
baselines in their findings and links each one, so the lineage is recorded.

!!! tip "New initiative, or extend an existing one?"
    Ask whether this work would move a Key Result an existing initiative already declares. If
    yes, link the project there; no new initiative needed. Only when the outcome is genuinely
    new, with no existing KR to capture it, does it earn its own. Fewer, sharper initiatives
    beat a landscape of near-duplicates.

---

## Declare the Key Results first

[Hard rule 1](hard-rules.md) says every initiative declares its Key Results *before* any
project sits beneath it. Write them into the initiative's description.

A Key Result comes in one of two kinds. Use whichever fits, and don't force a number where one
doesn't belong:

- **Measured**: a metric with a baseline → target, scored on how far it moved. Use it for
  outcomes you can quantify.
- **Committed**: a binary deliverable with a Definition of Done. Done or not-done, for work
  that just needs to happen (compliance, contracted, hard-deadline).

| Measured KR | Baseline | Target | Evidence |
|---|---|---|---|
| Activation rate | 22% | 30% | Signups reaching first value in 7 days |
| Weekly active teams | 140 | 200 | Teams with ≥1 active member per week |

| Committed KR | Definition of Done | Evidence |
|---|---|---|
| SOC 2 Type II | Report issued with no exceptions | Auditor's signed report |

Those Key Results are exactly what the projects below will name and move; that's
[rule 2](hard-rules.md). The chain runs: initiatives *declare* KRs, projects *name which
one(s) and the delta*, issues *do the work*. Every issue in your cycle should trace back up
this line.

!!! abstract "The KR table is the contract"
    No KRs, no initiative. Once written, they're what your delivery leads commit against and
    what you'll score at the end.

---

## Own it

[Hard rule 4](hard-rules.md) puts one named human on the initiative: someone with the strategic
seniority to answer *why this matters* and *how we know it worked*. Not a team, not two people
sharing it. The owner is accountable for the outcome, not for building it.

---

## Time-bound it

[Hard rule 5](hard-rules.md) gives an initiative a target date from `Planned` onward, set when
it's agreed, alongside the owner and KRs. You need it then, because prioritising and sequencing
happen *before* any work starts. Reaching `Active` doesn't add the date; it means work is now
underway against it. Undated strategy can't be prioritised or sequenced against anything else.

Set the timeframe to the outcome, not a calendar habit:

- Many initiatives fit a quarter, a clean OKR rhythm.
- Some run a year or more, like a large programme or a multi-phase bet. That's fine; give it a
  real horizon and revisit the KRs as it progresses.

---

## States and the two gates

Initiative states are a fixed set; Linear doesn't let you customise them. Five states, each
with a plain definition of done:

| State | Means | Move on when |
|---|---|---|
| Proposed | Being considered; not yet agreed | Leadership agrees it's worth doing |
| Planned | Agreed & prioritised (owner named, KRs written, target date set); not yet started | Work actually begins |
| Active | Work is underway against the target date; projects are moving its KRs | KRs are achieved, or the window closes |
| Completed | KRs achieved, or the timeframe closed and scored | — |
| Canceled | Dropped; reason recorded | — |

Two transitions carry real weight:

| Gate | From → To | What has to be true |
|---|---|---|
| **Strategic agreement** | Proposed → Planned | Leadership agrees; a single owner is named; the KR table **and the target date** are set |
| **Kick-off** | Planned → Active | Work actually starts against the date already set at `Planned` |

Everything after Active is bookkeeping. Score the KRs and mark it Completed, or record why and
mark it Canceled.

---

## Sub-initiatives — optional, larger programmes only

!!! note "Enterprise-plan feature"
    Sub-initiatives are only available on Linear's Enterprise plan. If you're not on it, keep
    the model flat: initiative → project. Nothing below is required.

When a programme is large or long-running, you can nest initiatives: a parent with
sub-initiatives beneath it, up to five levels deep. A parent automatically rolls up all the
projects and progress of its children, so you get one view of the whole programme while each
sub-initiative stays independently owned and scored.

Reach for them when:

- a company objective spans several teams or departments, each needing its own owner and KRs;
  or
- a large goal breaks into phases or workstreams that are worth tracking on their own.

Keep the top-level initiative about the overall outcome, and let each sub-initiative carry its
own slice of the KR table.

---

## Keep everyone posted

While an initiative is Active, its owner sees that a monthly update reaches
`#initiative-updates`: KR movement, health, and any risks. The full cadence and formats live in
[Communications](communications.md); health is
[a claim with evidence](communications.md#health-is-a-claim-with-evidence).

!!! warning "An initiative is only as current as its projects"
    The monthly update rolls up from the weekly project updates beneath it, so the KR movement
    is only as trustworthy as those. If a feeding project hasn't reported, or its update is
    stale, say so and don't claim a health greener than the evidence. The
    `linear-initiative-update` skill flags missing or stale project updates for you.

Post it either way:

- Linear's initiative update UI: write the status update on the initiative and set its health,
  and it flows to the connected `#initiative-updates` channel.
- The `linear-initiative-update` skill drafts the standard update (KR movement, health and
  risks) and posts it for you. Find it in the [Skills](skills/index.md) catalogue.

---

## Create one

Both ways hold the same standard. Set the owner, status and target date as the initiative's own
Linear fields, not in the description, and connect the `#initiative-updates` Slack channel so
updates post there. The description carries only the *why*, the Key Results, *out of scope* and
*context*; that part is the template.

1. **Use the `linear-initiative` skill (preferred).** It coaches you through the outcome, the
   KR table(s) (measured and/or committed), the owner, status and timeframe, keeps the native
   fields native, and gives you the description body to drop in. Find it in the
   [Skills](skills/index.md) catalogue.
2. **By hand.** Create a new initiative in the [Linear initiatives view](https://linear.app/happydevs/initiatives),
   set its owner, status (`Proposed`) and target date as fields, connect the
   `#initiative-updates` Slack channel, then paste
   [`template.md`](https://github.com/hungovercoders/linear-work-management/blob/main/skills/linear-initiative/template.md)
   into the description and fill it in. It's the same file the skill uses.

---

## Related

- [The Hard Rules](hard-rules.md): rules 1 (declare KRs), 4 (single owner), 5 (time-bounds)
- [The Cheat Sheet](index.md): the one-page summary this expands
</content>
