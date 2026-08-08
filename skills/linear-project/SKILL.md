---
name: linear-project
description: Draft or refine a Linear project to the Ways of Working standard — a bounded piece of work that names the Key Result(s) it moves and by how much, has a single named lead, start + target-end dates, a priority, and spend/product labels. Coaches the KR-delta and produces the project description ready to create in the happydevs workspace. Use when starting a new project, graduating one out of discovery, or tidying an existing one.
---

<!-- doc: projects.md -->

# linear-project

Draft or refine a Linear project to the Ways of Working standard: what you'll do and how, the
Key Result(s) it moves and by how much, a single named lead, dates from `Planned` onward.

**Requires:** the **Linear MCP server** connected, to read the workspace, link initiatives, set
fields, and post updates.

> A project can be created directly in Linear (unlike initiatives). This skill coaches it to
> standard and sets the native fields; link initiatives with `save_project` (`addInitiatives`)
> and post updates with `save_status_update` (`type: project`).

## What good looks like

- **Rule 2** — names the Key Result(s) it moves and the **delta** (e.g. "activation 22% → 30%").
  No KR named, no project (once it's past discovery).
- **Rule 4** — one named lead, the deliverer. Not a team, not two people.
- **Rule 5** — start + target-end dates from `Planned` onward, so it can be sequenced.
- Serves **one or more** initiatives (many-to-many); names the KR + delta on **each**.
  Standalone is allowed but questioned.
- Carries the *what & how* — the milestones, dependencies and scope — never the *why* (that's
  the initiative's) and never the individual tasks (those are its issues).

## The phase decides which rules apply

A project can enter the model at any point and move on its own timeline, so the skill's **first**
job is to locate it on the lifecycle; that's what decides which rules bite, not a fixed
checklist run every time:

- **Discovery** (`Idea` / `Scoping`) — needs only a **single named lead** (rule 4, from day one)
  and a description of what's being explored. **No KR, no dates, no initiative required.** Don't
  force them onto an idea.
- **The `Planned` gate** — crossing into delivery is where rules **2** (KR + delta) and **5**
  (dates) switch on, and where the initiative decision is made: **graduate** (link an existing
  initiative or seed a new one), **standalone** (allowed, questioned), or **drop** (`Canceled`).
- **Delivery** (`Planned` / `In Progress` / `Launching`) — fully committed; every rule applies.

So the flow **forks up front** into the three ways a project actually shows up, rather than
assuming a create-from-scratch path.

## Flow

**1. Locate it.** Ask two things (*new or existing?* and *which phase is it in, or entering?*),
then take one of three routes.

**Route A · a new idea (enters discovery).** Create the project in `Idea` (or `Scoping`) with a
**single named lead** and a description of the question it's exploring. Set nothing else — no KR,
no dates, no initiative. It crosses the gate later, via Route B. **Stop here.**

**Route B · graduate an existing project (crossing the `Planned` gate).** The project already
exists in discovery; this is a **transition, not a creation**. Decide its fate at the gate:

- Read the project and its issues / findings (`get_project`, `list_issues`).
- **Graduate** → link the initiative it matures under (`save_project` → `addInitiatives`); for a
  brand-new outcome, run `linear-initiative` to seed one *from those findings*, then link it.
  **Standalone** → proceed with no initiative, note it's questioned. **Drop** → move to
  `Canceled`, record why, **stop**.
- Then run the **gate checklist** below and move the status to `Planned`.

**Route C · a new delivery project (born committed).** The outcome is already known, so it skips
discovery. Create it and run the **gate checklist** straight away.

**The gate checklist (Routes B & C — rules 2 · 4 · 5):**

- **Key Result(s) + delta** — for each initiative served, name **which** KR and the delta
  (baseline → target). This is rule 2. Serving several initiatives → a row per initiative.
- **Lead** — one named deliverer (rule 4).
- **Dates** — start + target-end (rule 5).
- **Priority & labels** — a priority (Urgent → Low) to sequence it; `spend/*` (capex/opex) at
  planning; `product/*` for the product it serves (carries onto its issues).
- **Dependencies** — any Blocked by / Blocking relations to other projects, as **native project
  relations** (never prose); now that both ends have dates, the timeline can warn on conflicts.

**Final · create or update it in Linear.** Set the **lead**, **status**, **dates**, **priority**,
**initiative link(s)**, the **`spend/*`** / **`product/*`** labels and any **milestones** (dated
checkpoints) as the project's native Linear fields, never as text, and connect the
**`#project-updates`** Slack channel so updates post there. Put only the **description body**
(what & how · KR(s) + delta · out of scope · context) from [`template.md`](template.md) into the
description.

## The project template

[`template.md`](template.md) beside this skill is the single source of truth for the
**description body**. Fill each placeholder using the flow above; add a KR + delta row per
initiative served.

The **lead, status, dates, priority, initiative link(s), labels and milestones are native Linear
fields**: set them on the project itself, never in the description text. Keeping them native is
what lets Linear filter, sort and roll them up, and what lets `linear-doctor` check them.
