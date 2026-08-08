# Triage work

<div class="lwm-lead" markdown>
For the triage duty rota. An **inbound issue** arrived rather than being planned — an incident, a
request, a reported bug, an ad-hoc analysis. It carries **no project** and exactly **one
`flow/*`** label ([rule 3](../hard-rules.md)), and **no `type/*`**. This page covers inbound work;
the [shared issue model](index.md) — the lifecycle, the body-as-prompt, native fields — applies
underneath.
</div>

`flow/*` is how inbound work stays visible without faking a project around it. `product/*` is
**optional** here — there's no project to inherit from, so set it only if the work clearly serves
a product.

---

## Labels — `flow/*`

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

## The front door — Triage

Inbound work enters through **Triage**, where a named **duty rota** gives each item a fast
routing decision — one of **five outcomes** ("leave it sitting there" isn't one):

| Outcome | What it means |
|---|---|
| Accept into a project | Becomes a **[project issue](project-work.md)** — gets a `type/*`, joins a project |
| Accept as flow | Stays here — one `flow/*` label, no project |
| Redirect | Route it to the right team's triage |
| Merge | Merge into an existing issue |
| Decline | Close with a reason |

## Two clocks

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

!!! note "This page grows with Flow & Triage"
    The issue-level shape lives here; the operational detail — how the SLA clocks are set up
    natively, how the duty rota runs, and the GitHub/Slack integrations that feed it — is being
    built out in **Flow & Triage** and **SLAs**.

---

## Create one

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
