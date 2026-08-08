# Triage work

<div class="lwm-lead" markdown>
For the triage duty rota. An **inbound issue** arrived rather than being planned — an incident, a
request, a reported bug, an ad-hoc analysis. It carries **no project** and exactly **one
`flow/*`** label ([rule 3](../hard-rules.md)), and **no `type/*`**. This page covers inbound work;
the [shared issue model](index.md) — the lifecycle, the body-as-prompt, native fields — applies
underneath.
</div>

!!! info "Triage is a Linear feature — not something we bolt on"
    **Triage** is Linear's built-in, per-team **inbox**: incoming issues — from integrations,
    customer requests, Slack, or the API — land there *before* they enter the workflow, so
    someone makes a routing decision instead of the work dropping straight into a backlog. It's
    turned on in the team's settings and has its own view in Linear. Everything below — the rota,
    the five outcomes, the clocks — is simply *how we use that native feature* as the front door
    for inbound work.

`flow/*` is how inbound work stays visible without faking a project around it. `product/*` is
**optional** here — there's no project to inherit from, so set it only if the work clearly serves
a product.

---

## :material-tag-outline: Labels — `flow/*`

Exactly **one** `flow/*` label, and no `type/*` (that's the [project-work](project-work.md) group):

| `flow/*` | For |
|---|---|
| `incident` | Something's down or degraded — needs a response now |
| `vulnerability` | A security weakness to remediate (severity drives the SLA) |
| `bug` | A fault reported from outside any project |
| `analysis` | A data question or report requested ad-hoc from outside a project |
| `compliance` | A regulatory or policy obligation to meet |
| `support` | A user or customer request |
| `toil` | Recurring manual work worth capturing |

---

## :material-door-open: The front door — Triage

Inbound work enters through **Triage**, where a named **duty rota** gives each item a fast
routing decision — one of **five outcomes** ("leave it sitting there" isn't one):

```kroki-d2
@from_file:diagrams/triage-outcomes.d2
```

| Outcome | What it means |
|---|---|
| Accept into a project | Becomes a **[project issue](project-work.md)** — gets a `type/*`, joins a project |
| Accept as flow | Stays here — one `flow/*` label, no project |
| Redirect | Route it to the right team's triage |
| Merge | Merge into an existing issue |
| Decline | Close with a reason |

### Each outcome is a native Triage action

The decision uses the buttons **already in Linear's Triage view** — we don't reinvent them, we
just say which to reach for:

| Our outcome | Native Triage action | Then |
|---|---|---|
| Accept into a project | **Accept** | add it to a **project** and give it a `type/*` |
| Accept as flow | **Accept** | keep the one `flow/*` label, no project |
| Redirect | **Move to team** | it lands in that team's Triage |
| Merge | **Merge** / **Mark duplicate** | folds into the existing issue |
| Decline | **Decline** | closes with a reason |

## :material-cog-outline: Set it up

Triage is enabled **per team** in **Team settings → Triage**. Once on, the team gets a **Triage**
inbox in its sidebar, separate from the backlog. Route inbound work into it:

- **Integrations** — Sentry, GitHub, Zendesk/Intercom and the like create issues straight into Triage.
- **Linear Asks** — requests raised from **Slack** land in Triage.
- **Customer requests** and the **API / forms** — external reports arrive here too.
- **Manually** — anyone can move a stray issue into Triage for a decision.

**Triage Intelligence** (Linear's built-in AI) can suggest a label, flag likely **duplicates**, and
propose the right team or assignee. Treat it as a fast first pass — accept or override its
suggestion; it speeds the decision, it doesn't make it.

## :material-account-clock-outline: The duty rota

One named person owns the Triage inbox at a time — the **duty rota** — so every item gets a fast
decision and nothing sits. Use Linear's **Triage responsibility** to assign the current owner and
**rotate** it on a schedule, so the front door is always staffed. The duty is to **decide** — accept,
route, merge or decline within the [decision clock](#two-clocks) — not necessarily to do the work.

On duty, the **[`linear-triage`](../skills/index.md)** skill walks the inbox with you — reading the
queue and applying each decision (the `flow/*` label, a priority, and the outcome) to standard.

## :material-label-outline: Accept as flow — and there's no "promotion"

**Accept as flow** keeps the issue inbound: **one `flow/*` label, no project**. From there it lives
in the team's normal workflow (Backlog → … → Done) and stays visible through `flow/*` filters and
dashboards — flow work is first-class, not a lesser queue.

When a *kind* of flow work keeps recurring — the same support theme, the same toil every cycle —
that's a signal to **plan** it, not to invent a shortcut. Propose a normal
[project](../projects.md) (or [initiative](../initiatives.md)) through the front door and let it
ladder to an outcome. There is **no "promotion"** mechanism that fast-tracks a flow theme into a
project — the front door is the only door.

## :material-timer-outline: Two clocks

Inbound work runs on **two clocks** — a **decision** clock (route it) then, for some, a
**resolution** clock (fix it):

| Decision — set by `flow/*` | Decide within |
|---|---|
| `flow/incident` | Immediately |
| `flow/vulnerability` · `flow/support` | 1 working day |
| `flow/compliance` · `flow/bug` · `flow/toil` · `flow/analysis` | 2 working days |

| Resolution — `flow/vulnerability` by severity | Remediate within |
|---|---|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |

Priority set at triage can drive the SLA, and Linear can require it before an item leaves Triage.

### Wire them as native Linear SLAs

The clocks above are the *policy*; Linear enforces them with its **native SLA** feature. Every
issue carries SLA fields — **started · medium-risk · high-risk · breaches** — that Linear counts
down and surfaces in views, so the rota can see what's about to breach. Set the per-team SLA rules
so each clock maps onto them:

- **Decision clock** — starts when an issue **enters Triage**, targeting the duration for its
  kind (immediate / 1 / 2 working days). Because the `flow/*` label may not be set on arrival,
  drive it from the **priority** required at triage (Urgent → the tightest tier, down to Low).
- **Resolution clock** — an SLA on **`flow/vulnerability`**, keyed to **severity** (encoded via
  priority or a severity label): **Critical 7 days · High 30 · Medium 90**.

Choose **all** vs **business-day** counting per rule (`slaType`) to match the obligation. Breaches
and near-breaches are what a dashboard and [`linear-doctor`](../skills/index.md) watch for.

---

## :material-plus-circle-outline: Create one

The description body is the only thing that lives as text; everything else is a
[native field](index.md#native-fields-not-prose).

1. **Use the [`linear-issue`](../skills/index.md) skill — preferred.** It sets the single
   `flow/*` label (no project, no `type/*`), writes the body, and sets the native fields for you —
   using the template that matches the kind (`bug` / `analysis`), else the base `action` template.
2. **By hand.** Create the issue in the [team's Linear view](https://linear.app/happydevs/team/GRI/all),
   set the one `flow/*` label and no project, then paste the matching template from the
   [`linear-issue` skill folder](https://github.com/hungovercoders/linear-work-management/tree/main/skills/linear-issue)
   into the description and fill it in.

---

## Related

- [Issues](index.md) — the shared model every issue follows
- [Project work](project-work.md) — the other kind of issue, for planned work
- [The Cheat Sheet](../index.md) — the one-page summary, including both paths
