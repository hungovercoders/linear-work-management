# The Cheat Sheet

<div class="lwm-lead" markdown>
One page. If you read nothing else, read this. The single source of truth for **how we
use Linear** — see also **[the hard rules](hard-rules.md)** and the
**[skills](skills/index.md)** that apply them for you.
</div>

---

## :material-sitemap: How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Three layers, top to bottom, and **two ways work reaches them**. Teams cut across all
layers — a team owns issues, a project can draw on several teams but has exactly one lead.

| Path | Flows | What it is |
|---|---|---|
| <span class="lwm-strat">Strategic</span> (left) | Initiative → Project → Issues | Planned work toward an outcome |
| <span class="lwm-inbound">Inbound</span> (right) | Triage → Issue (`flow/*`) | Work that arrives: incidents, requests, compliance, support, toil |

Neither path is superior or exceptional. Some teams (product, platform) live mostly on the
strategic path; others (customer support, operations) live mostly on the inbound path; most
do both.

!!! danger "The one failure"
    An issue on **neither** path is *unclassified* — invisible work, and the defect the
    whole system is built to chase. `linear-doctor` reports every one.

---

## :material-gavel: The hard rules

One per level, plus two cross-cutting invariants — ownership and time-bounds.

| # | Level | Rule |
|---|---|---|
| 1 | Initiative | **Declares its Key Results** — measurable outcomes with targets, before any project sits under it. A result, not a theme. |
| 2 | Project | **Names the Key Result it moves, and by how much.** No KR named, no project. |
| 3 | Issue | **In a project *or* one `flow/*` label** — never neither (the *unclassified* defect), never both. |
| 4 | Ownership | **One named human owns each initiative and each project.** Not a team, not two people. |
| 5 | Time-bounds | **Active initiatives are time-bound; projects carry start + end dates from `Planned` onward.** Undated work can't be prioritised or sequenced. |

!!! tip "The deal"
    If a rule and a convenience ever conflict, the rule wins — that's what keeps the model
    honest. Detail and rationale: **[The Hard Rules](hard-rules.md)**.

---

## :material-shape-plus: What am I making?

| Situation | Make a… |
|---|---|
| A strategic outcome we want by a date, with measures | **Initiative** |
| A bounded piece of work that moves one of those measures | **Project** under it |
| A discrete task within that work | **Issue** in the project |
| Something broke, arrived, or was reported | **Issue** via **Triage** |
| Genuinely standalone work with no initiative | Project, but expect to justify it |

Orphaned projects aren't banned — they're **questioned**. If it doesn't ladder to
an initiative, either the work is wrong or the initiative is missing.

---

## :material-account-check: Who owns what

| Layer | Owner | Answers |
|---|---|---|
| Initiative | Strategic seniority — director, head of | Why does this matter? How do we know it worked? |
| Project | The deliverer — eng lead, product owner | What are we doing, how, and by when? |
| Issue | The assignee | Is it done? |
| Triage | Named duty rota, one person per cycle | Does this belong to us, and where does it go? |

---

## :material-traffic-light-outline: States at a glance

**Projects** run a full lifecycle:

| State | Means |
|---|---|
| Idea | Someone's thought of it; nothing committed |
| Scoping | Being shaped; cost and value under investigation |
| Planned | Agreed, dated, resourced; not started |
| In Progress | Being built |
| Launching | Built; rolling out |
| Paused | Deliberately stopped, with a reason and a review date |
| Completed | Delivered **and** the KR delta observed |
| Cancelled | Stopped for good; reason recorded |

**Issues** stay minimal:

| State | Means |
|---|---|
| Triage | Arrived; awaiting a routing decision |
| Backlog | Accepted, but not yet refined enough to start |
| Todo | Understood and ready to go — refined, actionable, can be picked up now |
| In Progress | Being worked |
| In Review | Work done; under review |
| Done | Shipped and accepted |
| Cancelled | Won't do; reason recorded |
| Duplicate | Superseded by another issue |

Fuller definitions and the Linear status-type mapping live in the States reference (GRI-73).
Teams may **add** states locally, never rename or remove the shared ones — otherwise
cross-team insight breaks.

---

## :material-label-multiple-outline: Labels at a glance

Labels come in **groups** that behave like enums — pick **one value per group**, so they
filter and report cleanly.

| Applies to | Group | Answers | Values |
|---|---|---|---|
| Issues | `type/*` | What kind of work is this? | feature · defect · chore · spike |
| Issues | `flow/*` | How did it arrive? (inbound, no project) | incident · defect · vulnerability · compliance · support · toil |
| Projects | `spend/*` | Capex or opex? (set at planning) | capex · opex |
| Projects & issues | `product/*` | Which product? (**grows over time**) | hungovercoders · dogadopt · woolwitch · cheeserater · … |

A label only exists if it's filtered or reported on. The canonical set lives in the Labels
reference (GRI-73); `product/*` grows as products are added.

---

## :material-flag-outline: Priority

Priority is **how urgent** work is to us — it drives ordering, and (via SLAs) deadlines.
It's set on **three things**, each at the moment the work is understood:

| Applies to | Set when | Job it does |
|---|---|---|
| Project | At planning | Sequence projects against each other |
| Project issue | At planning or refinement | Order the work inside a project |
| Inbound (`flow/*`) issue | At **triage** | Order it — and can drive the SLA |

Linear can require a priority before an issue leaves Triage.

| Priority | Use for |
|---|---|
| Urgent | Drop-everything — breaking or time-critical |
| High | Important; next up |
| Medium | Normal, planned work |
| Low | Nice-to-have; do when there's slack |
| No priority | Not yet decided — triage should resolve this |

Priority is distinct from a vulnerability's **severity** (Critical/High/Medium), though the
two usually track together. Full conventions land in **Projects (GRI-71)** and
**Issues (GRI-72)**.

---

## :material-timer-outline: Service levels

Inbound work runs on **two clocks**: a **decision** clock (how fast triage routes it) and,
for some types, a **resolution** clock (how fast it's fixed once accepted).

**1. Decision** — time to route an inbound item, set by its `flow/*` label:

| Inbound (`flow/*`) | Decide within |
|---|---|
| `flow/incident` | Immediately |
| `flow/vulnerability` · `flow/support` | 1 working day |
| `flow/compliance` · `flow/defect` · `flow/toil` | 2 working days |

**2. Resolution** — time to fix a `flow/vulnerability` once accepted, by **severity**:

| Severity | Remediate within |
|---|---|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |

So a vulnerability is **routed** within a working day (decision clock), then **remediated**
within its **severity** window (resolution clock) — two clocks, not a repeat. Severity here
is distinct from Linear *priority*, though the two usually track together; how it's encoded
and wired to an SLA is decided in **SLAs (GRI-78)**.

!!! note "How the clock is enforced"
    Linear maps a `flow/*` label to a deadline automatically via **SLA rules** (Settings →
    Issues → SLAs; Business/Enterprise) — no templates needed for the mapping, though
    templates / Linear Asks ensure the label is set on intake. Exact wiring (and the
    decision-vs-resolution nuance) lands in **SLAs (GRI-78)**.

---

## :material-call-split: Triage outcomes

Every triaged item leaves triage with a **decision** — five of them, never four.
"Leave it sitting there" isn't one.

| Outcome | What it means |
|---|---|
| Accept into a project | Planned-type work — attach it to a project; it becomes an issue there |
| Accept as flow | Inbound work that stays projectless — keep it with one `flow/*` label |
| Redirect | Not ours — route it to the right team's triage |
| Merge | A duplicate of existing work — merge into that issue |
| Decline | We won't do it — close with a reason |

In Linear these map to the built-in **Triage actions** (accept · mark duplicate · decline ·
move to team). Detail in **Flow & Triage (GRI-74)**.

---

## :material-bullhorn-outline: Comms cadence

The **owner/lead named on the work posts its update** on cadence — it's their job, not left
to chance.

| Update | Posted by | To | When |
|---|---|---|---|
| Initiative — KR movement, risks | Initiative owner | `#initiatives` | Monthly, while active |
| Project — on track / at risk / off track | Project lead | `#proj-<slug>` | Weekly, while In Progress or Launching |

!!! quote
    Health is a claim with evidence attached — not a colour someone picked.

---

## :material-rocket-launch-outline: Getting started

| You are… | Start with |
|---|---|
| Joining a team | This page, then the issue templates |
| Leading a project | This page, then the project guidelines — know your KR |
| Owning an initiative | This page, then the initiative guidelines — write your KR table before your first project |
| Seeing something off | Run [`linear-doctor`](skills/index.md) — it reports, it doesn't fix |
