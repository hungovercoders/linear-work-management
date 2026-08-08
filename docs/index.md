# The Cheat Sheet

One page. If you read nothing else, read this. The single source of truth for how we
use Linear — see also **[the three hard rules](hard-rules.md)** and the
**[skills](skills/index.md)** that apply them for you.

---

## How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Three layers, top to bottom. **Teams cut across all of them** — a team owns issues,
a project can draw on several teams but has exactly one lead.

The right-hand lane is the one people forget. Work that arrives unplanned is not a
failure of planning; it is a permanent category with its own front door. Both paths
are legitimate. What isn't legitimate is an issue on neither path.

---

## The three hard rules

1. **Every project names the Key Result it moves, and by how much.** This is what
   makes "projects are the how" enforceable instead of aspirational. No KR named,
   no project.
2. **Every issue is either in a project *or* carries one `flow/*` label.** Never
   neither, never both. "Neither" is the defect the system chases — we call it
   *unclassified*, and the doctor reports it.
3. **One named human owns each initiative and each project.** Not a team, not two
   people. Names, not squads.

Detail and rationale: **[The Three Hard Rules](hard-rules.md)**.

---

## What am I making?

| Situation | Make a… |
|---|---|
| A strategic outcome we want by a date, with measures | **Initiative** |
| A bounded piece of work that moves one of those measures | **Project** under it |
| A discrete task within that work | **Issue** in the project |
| Something broke, arrived, or was reported | **Issue** via **Triage** |
| Recurring inbound that keeps costing us | Raise a **promotion** — turn the theme into a project |
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

**Projects** — full lifecycle, idea to closed:

| Status | Type | Means |
|---|---|---|
| Idea | Backlog | Someone's thought of it. Nothing committed. |
| Scoping | Backlog | Being shaped. Cost and value under investigation. |
| Planned | Planned | Agreed, dated, resourced. Not started. |
| In Progress | Started | Being built. |
| Launching | Started | Built, rolling out. |
| Paused | Started | Deliberately stopped, with a reason and a review date. |
| Completed | Completed | Delivered *and* the KR delta observed. |
| Cancelled | Cancelled | Stopped for good. Reason recorded. |

**Issues** — minimal and measurable:

`Triage` → `Backlog` → `Todo` → `In Progress` → `In Review` → `Done`
(plus `Cancelled`, `Duplicate`)

Teams may **add** states locally. They may not rename or remove shared ones —
otherwise cross-team insight breaks.

---

## Labels at a glance

Use label **groups**. Groups are mutually exclusive, so they behave like enums and
report cleanly.

| Group | Values | Applies to |
|---|---|---|
| `type/*` | feature · defect · chore · spike | Issues — *what the work is* |
| `flow/*` | incident · defect · vulnerability · compliance · support · toil | Projectless issues — *how it arrived* |
| `spend/*` | capex · opex | Projects — set at planning, not retrofitted |
| `risk/*` | low · medium · high | Optional, where release care differs |

`type/defect` and `flow/defect` are not duplicates. A dependency bump is
`type/chore` arriving as `flow/vulnerability`.

If a label won't be filtered on or reported on, it shouldn't exist.

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
