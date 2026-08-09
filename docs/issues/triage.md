# Triage work

<div class="lwm-lead" markdown>
For the triage duty rota. **Inbound work** is the kind that arrived rather than being planned:
an incident, a request, a reported bug, an ad-hoc analysis. The other kind is
[project work](project-work.md). An inbound issue carries no project and exactly one `flow/*`
label ([rule 3](../hard-rules.md)), and no `type/*`. What follows is about inbound work; the
[shared model](index.md) (the lifecycle, the body-as-prompt, native fields) sits underneath it.
</div>

!!! info "Triage is a native Linear feature"
    **Triage** is Linear's built-in, per-team inbox. Incoming issues, whether from integrations,
    customer requests, Slack, or the API, arrive there before they enter the workflow, so someone
    makes a routing decision instead of the work dropping straight into a backlog. You turn it on
    in the team's settings and it gets its own view in Linear. Everything below (the rota, the
    five outcomes, the clocks) is how we use that native feature to receive inbound work.

`flow/*` is how inbound work stays visible without faking a project around it. `product/*` is
optional here: with no project to inherit from, set it only if the work clearly serves a
product.

---

## :material-tag-outline: Labels — `flow/*`

Exactly one `flow/*` label, and no `type/*` (that's the [project-work](project-work.md) group):

| `flow/*` | For |
|---|---|
| `incident` | Something's down or degraded; needs a response now |
| `vulnerability` | A security weakness to remediate (severity drives the SLA) |
| `defect` | A fault reported from outside any project |
| `query` | A data question or report requested ad-hoc from outside a project |
| `compliance` | A regulatory or policy obligation to meet |
| `support` | A user or customer request |
| `toil` | Recurring manual work worth capturing |

!!! note "Why `defect` and `query`, not `bug` and `analysis`?"
    Linear label names are unique across the whole workspace, even between groups, so the
    `type/*` group already owns `bug` and `analysis`. Inbound uses `defect` (a fault reported
    from outside) and `query` (an ad-hoc data ask). Same idea, different door.

---

## :material-door-open: Where inbound work arrives

Inbound work enters through Triage, where a named duty rota gives each item a fast
routing decision, one of five outcomes ("leave it sitting there" isn't one):

```kroki-d2
@from_file:diagrams/triage-outcomes.d2
```

| Outcome | What it means |
|---|---|
| Accept into a project | Becomes a **[project issue](project-work.md)**: gets a `type/*`, joins a project |
| Accept as flow | Stays here: one `flow/*` label, no project |
| Redirect | Route it to the right team's triage |
| Merge | Merge into an existing issue |
| Decline | Close with a reason |

!!! tip "Into a project, or stays as flow?"
    Ask whether an open project already owns the thing this touches. A bug in a project's scope,
    or a request the project will deliver anyway, gets accepted there. Self-contained work that
    just arrived (an incident, a one-off query, upkeep) stays flow. If the same flow theme keeps
    recurring, that's a signal to *propose* a project, never to silently promote.

### Each outcome is a native Triage action

The decision uses the buttons already in Linear's Triage view. We don't reinvent them, just say
which to reach for:

| Our outcome | Native Triage action | Then |
|---|---|---|
| Accept into a project | **Accept** | add it to a **project** and give it a `type/*` |
| Accept as flow | **Accept** | keep the one `flow/*` label, no project |
| Redirect | **Move to team** | it moves to that team's Triage |
| Merge | **Merge** / **Mark duplicate** | folds into the existing issue |
| Decline | **Decline** | closes with a reason |

## :material-cog-outline: Set it up

Triage is enabled per team in **Team settings → Triage**. Once on, the team gets a Triage
inbox in its sidebar, separate from the backlog. Inbound work reaches it a few ways:

- Integrations such as Sentry, GitHub and Zendesk/Intercom create issues straight into Triage.
- Linear Asks routes requests raised from Slack into Triage.
- Customer requests, and reports through the API or forms, arrive here too.
- Anyone can move a stray issue into Triage by hand when it needs a decision.

Triage Intelligence (Linear's built-in AI) can suggest a label, flag likely duplicates, and
propose the right team or assignee. Treat it as a fast first pass and accept or override its
suggestion. It speeds the decision without making it.

## :material-account-clock-outline: The duty rota

One named person owns the Triage inbox at a time (the duty rota), so every item gets a fast
decision and nothing sits. Use Linear's **Triage responsibility** to assign the current owner and
rotate it on a schedule, so the queue is always staffed. The duty is to decide, whether that's
accept, route, merge or decline within the [decision clock](#two-clocks), and not necessarily to
do the work.

On duty, the [`linear-triage`](../skills/index.md) skill walks the inbox with you, reading the
queue and applying each decision (the `flow/*` label, a priority, and the outcome) to standard.

## :material-label-outline: Accept as flow, with no "promotion"

Accept as flow keeps the issue inbound: one `flow/*` label, no project. From there it lives in
the team's normal workflow (Backlog → … → Done) and stays visible through `flow/*` filters and
dashboards. Flow work belongs to the same queue as everything else, not a lesser one.

When a *kind* of flow work keeps recurring, such as the same support theme or the same toil every
cycle, that's a signal to plan it rather than invent a shortcut. Propose a normal
[project](../projects.md) (or [initiative](../initiatives.md)) the ordinary way and let it ladder
to an outcome. No "promotion" mechanism fast-tracks a flow theme into a project; every project
starts the same way.

## :material-timer-outline: Two clocks

Inbound work runs on two clocks: a decision clock to route it, then, for some kinds, a
resolution clock to fix it.

| Decision — set by `flow/*` | Decide within |
|---|---|
| `flow/incident` | Immediately |
| `flow/vulnerability` · `flow/support` | 1 working day |
| `flow/compliance` · `flow/defect` · `flow/toil` · `flow/query` | 2 working days |

| Resolution — `flow/vulnerability` by severity | Remediate within |
|---|---|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |

Priority set at triage can drive the SLA, and Linear can require it before an item leaves Triage.

### Wiring them up

The two clocks aren't the same mechanism. Linear's native SLA rules measure time *to
completion*, so they fit the resolution clock but not the decision clock: there's no native
way to SLA "decide within X". Wire each accordingly.

- The decision clock is the rota plus visibility, not an SLA. Keep the queue prompt with
  **Triage Responsibility** (the duty rota, which integrates PagerDuty, Opsgenie and Incident.io)
  and the time-in-status display on the Triage state, so a lingering item is obvious. Linear can
  also require a priority before an issue leaves Triage.
- The resolution clock is a native SLA rule. On **Business/Enterprise**, add an SLA rule
  (*Settings → Issues → SLAs*) filtered by the **`flow/vulnerability`** label (with severity via
  priority) and business-day durations: Critical 7 days, High 30, Medium 90. Rules apply on
  create or update rather than retroactively, the first matching rule wins so order the most
  urgent first, and an issue can have an SLA or a due date but not both. **Triage Rules** can
  auto-apply the label on arrival, which is what triggers the SLA.

Not on Business/Enterprise, or want it deterministic? The
[`linear-triage`](../skills/index.md) skill sets the issue's `slaBreachesAt` directly per the
`flow/*` mapping. Either way, every issue carries native SLA fields
(started · medium-risk · high-risk · breaches) that dashboards and
[`linear-doctor`](../skills/index.md) watch for.

---

## :material-plus-circle-outline: Create one

The description body is the only thing that lives as text; everything else is a
[native field](index.md#native-fields-not-prose).

1. The [`linear-issue`](../skills/index.md) skill is the quickest route. It sets the single
   `flow/*` label (no project, no `type/*`), writes the body, and sets the native fields for you,
   using the matching template (`template-bug` for `defect`, `template-analysis` for `query`),
   else the base `action` template.
2. By hand, create the issue in the [team's Linear view](https://linear.app/happydevs/team/GRI/all),
   set the one `flow/*` label and no project, then paste the matching template from the
   [`linear-issue` skill folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue)
   into the description and fill it in.

---

## Related

- [Issues](index.md) — the shared model every issue follows
- [Project work](project-work.md) — the other kind of issue, for planned work
- [The Cheat Sheet](../index.md) — the one-page summary, including both paths
