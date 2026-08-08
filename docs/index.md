# Linear Work Management

The single source of truth for **how we run work in Linear** — the operating model,
the expectations at each level, and the AI-ready skills that keep everything consistent.

Work should be visible, dependencies clear, and every task relatable to strategy —
with as little manual admin as possible. This guide is how we get there.

## How it fits together

```kroki-d2
direction: down

initiatives: Initiatives {
  style.fill: "#EEF2FF"
  style.stroke: "#6366F1"
}
projects: Projects {
  style.fill: "#E0E7FF"
  style.stroke: "#6366F1"
}
issues: Issues {
  style.fill: "#C7D2FE"
  style.stroke: "#6366F1"
}
teams: Teams {
  style.fill: "#FEF3C7"
  style.stroke: "#D97706"
}

initiatives -> projects: contain {style.stroke: "#6366F1"}
projects -> issues: contain {style.stroke: "#6366F1"}
teams -> issues: own {style.stroke: "#D97706"}

strategy: "Strategic seniority" {shape: text}
delivery: "Deliverers (eng / PO)" {shape: text}
strategy -> initiatives: own {style.stroke-dash: 3}
delivery -> projects: lead {style.stroke-dash: 3}
```

Initiatives set **what & why**. Projects set **what + how** and link up to an initiative.
Issues are the concrete work, owned by teams. One initiative can span many projects; one
project can involve many teams.

## Cheat sheet

| Level | Owns | Answers | Must have | Skill |
| ----- | ---- | ------- | --------- | ----- |
| **[Initiative](concepts/initiatives.md)** | Strategic seniority | *Why* & *what* (OKR-style) | Owner · importance · success measure · agreed before active | [`linear-initiative`](skills/index.md) |
| **[Project](concepts/projects.md)** | Single lead (eng / PO) | *What* + *how* + how it furthers the initiative | Link to initiative · lead · dates · milestones · capex/opex | `linear-project` |
| **[Issue](concepts/issues.md)** | A team | *What* / *why* / *when done* | A template (Action / Feature / Problem / Spike) · useful labels | `linear-issue` |
| **[Team](concepts/teams.md)** | — | Who does the work | Sensible settings · additive-only states/labels | — |

### Rules of thumb

- **No orphans.** A project without an initiative is the exception and gets questioned.
- **One lead per project.** Ownership is singular; contributors are many.
- **Consistency beats local optimisation.** Teams may *add* states/labels, never diverge —
  accurate insight depends on shared values. See [States](concepts/states.md) & [Labels](concepts/labels.md).
- **The issue is the prompt.** Write issues so an agent can act on them; store agent plans
  against the issue.
- **Unplanned work goes through [Triage](concepts/triage.md)** so it is visible, not lost.

### Communication cadence

| Level | Channel | Cadence |
| ----- | ------- | ------- |
| Initiative / strategic | [`#initiative-updates`](https://hungovercoders.slack.com/archives/C0BPS0WL7Q8) | Regular strategic update |
| Project / delivery | [`#project-updates`](https://hungovercoders.slack.com/archives/C0BNXKP69NE) | Regular delivery update |

Full patterns and the `linear-status-update` skill: [Communication](operating/communication.md).

## Start here

- **New to this?** Read [Hierarchy](concepts/hierarchy.md), then the level you work at.
- **Setting up work?** Use the [Skills](skills/index.md) — they apply these rules for you.
- **Keeping it healthy?** Run the `linear-doctor` skill / `task doctor` to catch drift.

!!! note "Expected views"
    Where this guide links to a Linear view (e.g. `linear.app/happydevs/projects/all`)
    that does not exist yet, that link is an **implementation target** — build the saved
    view to match the guidance. A missing view is a to-do, not a broken doc.
