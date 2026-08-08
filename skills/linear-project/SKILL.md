---
name: linear-project
description: Draft or refine a Linear project to the Ways of Working standard — a bounded piece of work that names the Key Result(s) it moves and by how much, has a single named lead, start + target-end dates, a priority, and spend/product labels. Coaches the KR-delta and produces the project description ready to create in the happydevs workspace. Use when starting a new project, graduating one out of discovery, or tidying an existing one.
---

<!-- doc: projects.md -->

# linear-project

Draft or refine a Linear project to the Ways of Working standard: what you'll do and how, the
Key Result(s) it moves and by how much, a single named lead, dates from `Planned` onward.

**Requires:** the **Linear MCP server** connected — to read the workspace, link initiatives, set
fields, and post updates.

> A project can be created directly in Linear (unlike initiatives). This skill coaches it to
> standard and sets the native fields; link initiatives with `save_project` (`addInitiatives`)
> and post updates with `save_status_update` (`type: project`).

## What good looks like

- **Rule 2** — names the Key Result(s) it moves and the **delta** (e.g. "activation 22% → 30%").
  No KR named, no project — once it's past discovery.
- **Rule 4** — one named lead, the deliverer. Not a team, not two people.
- **Rule 5** — start + target-end dates from `Planned` onward, so it can be sequenced.
- Serves **one or more** initiatives (many-to-many); names the KR + delta on **each**.
  Standalone is allowed but questioned.
- Carries the *what & how* — the milestones, dependencies and scope — never the *why* (that's
  the initiative's) and never the individual tasks (those are its issues).

## Phase decides how hard the rules bite

- **Discovery** (`Idea` / `Scoping`) — exploring whether there's an outcome worth committing to.
  It may have **no initiative and no KR yet**, but it **always has a named lead** (rule 4 from
  day one). Don't force a KR onto an idea.
- **The `Planned` gate** — discovery resolves into **graduate** (link an existing initiative or
  seed a new one), **standalone** (questioned), or **drop** (Cancelled). From here rules 2 and 5
  bite: name the KR + delta, set the dates.
- **Delivery** (`Planned` / `In Progress` / `Launching`) — committed and linked.

## Flow

1. **Phase** — ask: *is this an idea to explore, or committed delivery?* An `Idea`/`Scoping`
   project needs a lead and a description, but not yet a KR or dates — stop there if that's what
   it is. Otherwise carry on to name the outcome.
2. **Outcome it serves** — which initiative(s)? If it's graduating from discovery, link the
   initiative it matures under (or, for a brand-new outcome, hand off to the `linear-initiative`
   skill to seed one, then link it). Standalone → note it's questioned.
3. **Key Result(s) + delta** — for each initiative it serves, name **which** KR and the delta it
   expects (baseline → target). This is rule 2.
4. **Lead** — one named person, the deliverer.
5. **Dates** — start + target-end, from `Planned` onward.
6. **Priority & labels** — a priority (Urgent → Low) to sequence it; `spend/*` (capex/opex) set
   at planning; `product/*` for the product it serves (it carries onto the issues).
7. **Create it in Linear.** Set the **lead**, **status**, **start + target-end dates**,
   **priority**, **initiative link(s)** and the **`spend/*`** / **`product/*`** labels as the
   project's native Linear fields — never as text — and connect the **`#proj-<slug>`** Slack
   channel so updates post there. Put only the **description body** (what & how · KR(s) + delta ·
   milestones · out of scope) from [`template.md`](template.md) into the description.

## The project template

[`template.md`](template.md) beside this skill is the single source of truth for the
**description body**. Fill each placeholder using the flow above; add a KR + delta row per
initiative served.

The **lead, status, dates, priority, initiative link(s) and labels are native Linear fields** —
set them on the project itself, never in the description text. Keeping them native is what lets
Linear filter, sort and roll them up, and what lets `linear-doctor` check them.

See [`skills/README.md`](https://github.com/dataGriff/linear-work-management/tree/main/skills)
for the conventions every skill here follows.
