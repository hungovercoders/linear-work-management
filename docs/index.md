# The Cheat Sheet

<div class="lwm-lead" markdown>
One page. If you read nothing else, read this. The single source of truth for **how we
use Linear** — see also **[the hard rules](hard-rules.md)** and the
**[skills](skills/index.md)** that apply them for you.
</div>

!!! abstract "Why this matters"
    The point of all this is an **unbroken line from *why* to the work in your cycle** — every
    issue ladders up to a project's Key Result and the initiative it serves. People can see
    they're delivering the value expected of them, and why. That connection is the benefit;
    the rules just keep it intact.

    All of it lives in **[Linear](https://linear.app/happydevs)** — strategy, delivery and
    execution in one place, rather than strategy in Notion, delivery in a spreadsheet and
    status in Slack, so no tool boundary breaks the line. The **initiatives**, **projects**
    and **issues** below are the ones in Linear; this page is how we use them.

---

## :material-sitemap: How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Three layers, top to bottom, and **two ways work reaches them**. Teams cut across all
layers — a team owns issues, a project can draw on several teams but has exactly one lead.
A project serves **one or more** initiatives — it can move Key Results across several, not
just one.

| Path | Flows | What it is |
|---|---|---|
| <span class="lwm-strat">Strategic</span> (left) | Initiative → Project → Issues | Planned work toward an outcome |
| <span class="lwm-inbound">Inbound</span> (right) | Triage → Issue (`flow/*`) | Work that arrives: incidents, requests, compliance, support, toil |

Neither path is superior or exceptional. Some teams (product, platform) live mostly on the
strategic path; others (customer support, operations) live mostly on the inbound path; most
do both.

See it live in Linear: [initiatives](https://linear.app/happydevs/initiatives) ·
[projects](https://linear.app/happydevs/projects/all).

!!! danger "The one failure"
    An issue on **neither** path is *unclassified* — invisible work, and the defect the
    whole system is built to chase. `linear-doctor` reports every one.

---

## :material-gavel: The hard rules

One per level, plus two cross-cutting invariants — ownership and time-bounds. These are the
**org-level minimum to work together**; how each team runs *inside* them is theirs.

| # | Level | Rule |
|---|---|---|
| 1 | Initiative | **Declares its Key Results** before any project — **measured** (baseline → target) or **committed** (a deliverable, done/not-done). A result, not a theme. |
| 2 | Project | **Names the Key Result(s) it moves, and by how much** — one or more, across the initiative(s) it serves, **by `Planned`** (`Idea`/`Scoping` may still be exploring). |
| 3 | Issue | **In a project *or* one `flow/*` label** — never neither (the *unclassified* defect), never both. |
| 4 | Ownership | **One named human owns each initiative and each project.** Not a team, not two people. |
| 5 | Time-bounds | **Dated from `Planned` onward** — initiatives carry a target date, projects a start + end. Set when agreed, so work can be prioritised and sequenced before it starts. |

!!! tip "The deal"
    If a rule and a convenience ever conflict, the rule wins — that's what keeps the model
    honest. Detail and rationale: **[The Hard Rules](hard-rules.md)**.

---

## :material-shape-plus: What am I making?

| Situation | Make a… |
|---|---|
| A strategic outcome we want by a date, with measures | **Initiative** |
| A bounded piece of work that moves one or more of those measures | **Project** under the initiative(s) it serves |
| A discrete task within that work | **Issue** in the project |
| Something broke, arrived, or was reported | **Issue** via **Triage** |
| An idea to explore before committing | **Project** in `Idea` — no initiative or KR needed yet |
| Genuinely standalone work with no initiative | Project, but expect to justify it |

**How work starts:** the cheapest way in is a **project in `Idea`** — discovery, no initiative
or KR required. By `Planned` it resolves: **graduate** into delivery under an outcome (an
existing initiative or a new one it seeds), go **standalone** (questioned), or **drop**. A
parentless project is fine while it's an idea; only from `Planned` on is orphaning
**questioned**.

---

## :material-account-check: Who owns what

| Layer | Owner | Answers |
|---|---|---|
| Initiative | Strategic seniority — director, head of | Why does this matter? How do we know it worked? |
| Project | The deliverer — eng lead, product owner | What are we doing, how, and by when? |
| Issue | The assignee | Is it done? |
| Triage | Named duty rota, one person per cycle | Does this belong to us, and where does it go? |

The sections below tell each owner exactly what to do. **Read the one that's you.**

---

## :material-target: Initiatives — for strategic leadership

You own an **outcome**, not a task list. Keep initiatives about *what & why*; leave the
*how* to the projects beneath them. Full guidance, states and a template:
**[Initiatives](initiatives.md)**. Open [your initiatives in Linear](https://linear.app/happydevs/initiatives).

| Your job | Detail |
|---|---|
| Declare Key Results | Measured or committed, before any project — [rule 1](hard-rules.md) |
| Name yourself owner | One person, strategic seniority — [rule 4](hard-rules.md) |
| Set the target date | From `Planned` onward, so it can be prioritised — [rule 5](hard-rules.md) |
| Post the update | Monthly to `#initiative-updates` while active |

**States** (a fixed set — Linear doesn't let you customise these):

| State | Means |
|---|---|
| Proposed | Being considered; not yet agreed |
| Planned | Agreed & prioritised — owner named, KRs written, target date set — but not yet started |
| Active | Work is underway against the target date; projects are moving its KRs |
| Completed | KRs achieved, or the timeframe closed and scored |
| Canceled | Dropped; reason recorded |

**Proposed → Planned** is the *strategic agreement gate* (leadership agrees; owner, KRs and
target date set); **Planned → Active** is when work actually starts against that date.

---

## :material-clipboard-check-outline: Projects — for delivery leads (and the strategy that funds them)

A project is **what you'll do and how**. Every project moves through the same lifecycle; its
states group into phases — **discovery** while there's still a question to answer, **delivery**
once it's committed — and the `Planned` gate divides the two. Full guidance, the lifecycle
diagram and a template: **[Projects](projects.md)**. See
[all projects in Linear](https://linear.app/happydevs/projects/all).

**States** (full lifecycle):

| State | Phase | Means |
|---|---|---|
| Idea | Discovery | Someone's thought of it; nothing committed |
| Scoping | Discovery | Being shaped; cost and value under investigation |
| Planned | Delivery | Agreed, dated, resourced; not started |
| In Progress | Delivery | Being built |
| Launching | Delivery | Built; rolling out |
| Paused | Delivery | Deliberately stopped, with a reason and a review date |
| Completed | Closed | Delivered **and** the KR delta observed |
| Cancelled | Closed | Stopped for good; reason recorded |

### Discovery phase — is there something here? (`Idea` · `Scoping`)

Explore cheaply. A project in discovery may have **no parent initiative and no named KR** —
that's legitimate; it's where an initiative's groundwork gets recorded. It still has a
**single named lead** ([rule 4](hard-rules.md)) — ownership applies from day one; only the KR
and dates wait for `Planned`. At the **`Planned`** gate, it resolves into one of three:

| Outcome | What it means |
|---|---|
| **Graduate** | Mature into delivery under an outcome — link an existing initiative, or seed a new one |
| **Standalone** | Proceed with no initiative — allowed, but questioned |
| **Drop** | Cancel it; reason recorded |

### Delivery phase — build the committed outcome (`Planned` · `In Progress` · `Launching`)

Committed and linked to an outcome. Now the rules bite:

| Your job | Detail |
|---|---|
| Name the KR(s) it moves + delta | e.g. "activation 22% → 30%" — [rule 2](hard-rules.md); one or more, across the initiative(s) it serves |
| Link it to one or more initiatives | Standalone is the exception, and gets questioned |
| Be the single named lead | One person accountable — [rule 4](hard-rules.md) |
| Set start + end dates | From `Planned` onward — [rule 5](hard-rules.md) |
| Draw dependencies | So sequencing and risk are visible |
| Set a priority | To sequence projects against each other |
| Post the update | Weekly to `#project-updates` while In Progress or Launching |

**Labels** — two groups, both set on the project:

| Group | Values | What it records |
|---|---|---|
| `spend/*` | `capex` · `opex` | How the work is funded — set at planning |
| `product/*` | `hungovercoders` · `dogadopt` · `woolwitch` · … (grows over time) | Which product it serves — **also carried onto its issues** |

`type/*` and `flow/*` are *issue*-level groups, not project ones — they're in the Issues
section below.

---

## :material-checkbox-marked-circle-outline: Issues — the work itself

An issue is a **discrete task**, understood before it starts. Full guidance, the states, the
`type/*` templates and the agent-plan convention: **[Issues](issues.md)**. See
[all issues in Linear](https://linear.app/happydevs/team/GRI/all). Two things are true of
**every** issue, whichever path it came from:

- It is **classified** — in a project *or* carrying one `flow/*` label, never both, never
  neither ([rule 3](hard-rules.md)).
- The issue body is the **prompt** — store the agent's plan against it — and it carries a
  **priority** (Urgent → Low) that orders it.

**States** — the same lifecycle for every issue:

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

From here every issue is **one of two kinds** — and only one.

### <span class="lwm-strat">Project issues</span> — planned work (for the delivery team)

Live inside a **project** and ladder to its KR.

**Labels** — one `type/*` (what kind of work), plus the `product/*` inherited from the project:

| `type/*` | For |
|---|---|
| action | **The default** — any work that needs doing, from a code change to a reminder |
| feature | A new capability |
| bug | Something's broken |
| spike | A time-boxed investigation |

`product/*` carries down automatically — same value as the project. Refined from `Backlog`
to `Todo` before work starts — that's the readiness gate.

### <span class="lwm-inbound">Inbound issues</span> — flow work (for the triage duty rota)

Arrive through **Triage**, carry **no project** and exactly one **`flow/*`** label (no
`type/*` — that's a project-issue group):

| `flow/*` | For |
|---|---|
| incident | Something's down or degraded — needs a response now |
| vulnerability | A security weakness to remediate (severity drives the SLA) |
| bug | A fault reported from outside any project |
| compliance | A regulatory or policy obligation to meet |
| support | A user or customer request |
| toil | Recurring manual work worth capturing |

A named **duty rota** decides each one, fast — with one of **five outcomes** ("leave it
sitting there" isn't one):

| Outcome | What it means |
|---|---|
| Accept into a project | Becomes a **project issue** (above) |
| Accept as flow | Stays here — one `flow/*` label, no project |
| Redirect | Route it to the right team's triage |
| Merge | Merge into an existing issue |
| Decline | Close with a reason |

Inbound work runs on **two clocks** — a **decision** clock (route it) then, for some, a
**resolution** clock (fix it):

| Decision — set by `flow/*` | Decide within |
|---|---|
| `flow/incident` | Immediately |
| `flow/vulnerability` · `flow/support` | 1 working day |
| `flow/compliance` · `flow/bug` · `flow/toil` | 2 working days |

| Resolution — `flow/vulnerability` by severity | Remediate within |
|---|---|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |

Priority set at triage can drive the SLA, and Linear can require it before an item leaves
Triage. How the label maps to an SLA (and severity is encoded) lands in **SLAs (GRI-78)**.

---

## :material-rocket-launch-outline: Getting started

Top-down — find your row:

| You are… | Start with |
|---|---|
| Owning an initiative | This page, then **[Initiatives](initiatives.md)** — write your KR table before your first project |
| Leading a project | This page, then **[Projects](projects.md)** — know your KR |
| Delivering on a team | This page, then **[Issues → Project issues](issues.md#project-issues-planned-work)** |
| On triage duty | This page, then **[Issues → Inbound issues](issues.md#two-kinds-of-issue-and-only-one)** |
| Responsible for Linear workflows | Run [`linear-doctor`](skills/index.md) — it reports drift; it doesn't fix |
