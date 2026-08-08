# The Cheat Sheet

One page. If you read nothing else, read this. The single source of truth for how we
use Linear — see also **[the hard rules](hard-rules.md)** and the
**[skills](skills/index.md)** that apply them for you.

---

## How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Three layers, top to bottom, and **two ways work reaches them**. Teams cut across all
layers — a team owns issues, a project can draw on several teams but has exactly one lead.

| Path | Flows | What it is |
|---|---|---|
| **Strategic** (left) | Initiative → Project → Issues | Planned work toward an outcome |
| **Inbound** (right) | Triage → Issue (`flow/*`) | Work that arrives: incidents, requests, compliance, support, toil |

Neither path is superior or exceptional. Some teams (product, platform) live mostly on the
strategic path; others (customer support, operations) live mostly on the inbound path; most
do both. What isn't legitimate is an issue on **neither** path — that's the *unclassified*
defect the doctor chases.

---

## The hard rules

One per level, plus ownership.

| # | Level | Rule |
|---|---|---|
| 1 | Initiative | **Declares its Key Results** — measurable outcomes with targets, before any project sits under it. A result, not a theme. |
| 2 | Project | **Names the Key Result it moves, and by how much.** No KR named, no project. |
| 3 | Issue | **In a project *or* one `flow/*` label** — never neither (the *unclassified* defect), never both. |
| 4 | Ownership | **One named human owns each initiative and each project.** Not a team, not two people. |

Detail and rationale: **[The Hard Rules](hard-rules.md)**.

---

## What am I making?

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

## Who owns what

| Layer | Owner | Answers |
|---|---|---|
| Initiative | Strategic seniority — director, head of | Why does this matter? How do we know it worked? |
| Project | The deliverer — eng lead, product owner | What are we doing, how, and by when? |
| Issue | The assignee | Is it done? |
| Triage | Named duty rota, one person per cycle | Does this belong to us, and where does it go? |

---

## States at a glance

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
| Backlog | Accepted; not yet scheduled |
| Todo | Scheduled and ready to start |
| In Progress | Being worked |
| In Review | Work done; under review |
| Done | Shipped and accepted |
| Cancelled | Won't do; reason recorded |
| Duplicate | Superseded by another issue |

Fuller definitions and the Linear status-type mapping live in the States reference (GRI-73).
Teams may **add** states locally, never rename or remove the shared ones — otherwise
cross-team insight breaks.

---

## Labels at a glance

Labels come in **groups** that behave like enums — pick **one value per group**, so they
filter and report cleanly.

| Applies to | Group | Answers |
|---|---|---|
| Issues | `type/*` | What kind of work is this? |
| Issues | `flow/*` | How did it arrive? (inbound, no project) |
| Projects | `spend/*` | Capex or opex? (set at planning) |
| Projects & issues | `product/*` | Which product? — **grows over time** |

`product/*` values are your live products (`hungovercoders` · `dogadopt` · `woolwitch` ·
`cheeserater` · …). A label only exists if it's filtered or reported on; the fixed groups'
canonical values live in the Labels reference (GRI-73).

---

## Service levels

| Thing | Within |
|---|---|
| Triage decision — incident | Immediately |
| Triage decision — vulnerability, customer support | 1 working day |
| Triage decision — everything else | 2 working days |
| Vulnerability remediated or risk accepted | Critical 7d · High 30d · Medium 90d |
| Project update posted | Weekly, while In Progress or Launching |
| Initiative update posted | Monthly, while active |

Triage has **five** outcomes, never four: accept into a project, accept as flow,
redirect, merge, decline. "Leave it sitting there" is not one of them.

---

## Comms cadence

| Who | Gets | When | Where |
|---|---|---|---|
| Leadership | Initiative updates — KR movement, risks | Monthly | `#initiatives` |
| Stakeholders | Project updates — on track / at risk / off track | Weekly | `#proj-<slug>` |
| Team | Cycle summary, triage digest | Weekly | Team channel |
| Everyone | Launches, incidents | On event | `#announcements` |

Health is a claim with evidence attached, not a colour someone picked.

---

## Getting started

| You are… | Start with |
|---|---|
| Joining a team | This page, then the issue templates |
| Leading a project | This page, then the project guidelines — know your KR |
| Owning an initiative | This page, then the initiative guidelines — write your KR table before your first project |
| Seeing something off | Run [`linear-doctor`](skills/index.md) — it reports, it doesn't fix |
