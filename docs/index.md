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

- **The strategic path** (left): planned work. An initiative sets the outcome, projects
  move it, issues do it.
- **The inbound path** (right): work that *arrives* — incidents, requests, compliance,
  support, toil — and is triaged.

Neither path is superior or exceptional. Some teams (product, platform) live mostly on the
strategic path; others (customer support, operations) live mostly on the inbound path; most
do both. What isn't legitimate is an issue on **neither** path — that's the *unclassified*
defect the doctor chases.

---

## The hard rules

One per level, plus ownership.

1. **Every initiative declares its Key Results** — measurable outcomes with targets,
   before any project sits under it. An initiative is a result, not a theme.
2. **Every project names the Key Result it moves, and by how much.** No KR named,
   no project.
3. **Every issue is either in a project *or* carries one `flow/*` label.** Never
   neither (the *unclassified* defect the doctor chases), never both.
4. **One named human owns each initiative and each project.** Not a team, not two
   people. Names, not squads.

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

`Idea → Scoping → Planned → In Progress → Launching → Completed` — plus `Paused` and `Cancelled`

**Issues** stay minimal:

`Triage → Backlog → Todo → In Progress → In Review → Done` — plus `Cancelled` and `Duplicate`

What each state means (and how it maps to Linear's status types) is in the States reference
(GRI-73). Teams may **add** states locally, never rename or remove the shared ones —
otherwise cross-team insight breaks.

---

## Labels at a glance

Labels come in **groups** that behave like enums — pick **one value per group**, so they
filter and report cleanly. Separate them by where they apply.

**On issues:**

- `type/*` — what kind of work is this?
- `flow/*` — how did it arrive? (inbound issues, no project)

**On projects:**

- `spend/*` — capex or opex? (decided at planning)

**Across projects and issues:**

- `product/*` — which product? (`hungovercoders` · `dogadopt` · `woolwitch` ·
  `cheeserater` · …) — the one group that **grows over time** as products are added.

A label only exists if it's filtered or reported on. The fixed groups' canonical values
live in the Labels reference (GRI-73).

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

- **Joining a team?** Read this page, then the issue templates.
- **Leading a project?** Read this page, then the project guidelines. Know your KR.
- **Owning an initiative?** Read this page, then the initiative guidelines. Write
  your KR table before your first project exists.
- **Something feels off?** Run [`linear-doctor`](skills/index.md). It reports; it
  doesn't fix.
