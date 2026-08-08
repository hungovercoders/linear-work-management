# Projects

<div class="lwm-lead" markdown>
For delivery leads. A **project** in [Linear](https://linear.app/happydevs/projects/all) is
**what you'll do and how** — a bounded piece of work that moves a Key Result. One project, one
named lead, moving through one lifecycle. It sits alongside the initiative it serves and the
issues that build it, in the same tool.
</div>

**[Every project in Linear, on one screen.](https://linear.app/happydevs/projects/all)** This
is where strategy becomes delivery — what's being built, who leads it, which measure it moves,
and whether it's on track. Scan it to see what's committed versus still an idea, and that every
active project ladders up to an outcome.

---

## What a project is

A project is a **bounded body of work with one named lead** — the *what & how* between the
outcome above it and the tasks below. Two things hold across its whole life; a third arrives
when it commits:

- **One named lead** — named from the moment it exists, at `Idea` (rule 4). Always.
- **A defined scope** — what we're doing and how: the shape of the work, its milestones and
  dependencies.
- **A Key Result it moves, and by how much** — the measure it takes from an initiative and the
  delta it promises. This is the point of a project in **delivery**; in **discovery** that
  measure is exactly what it's still trying to find, so it isn't required yet.

Everything about *why the outcome matters* belongs to the [initiative](initiatives.md) above;
everything about *the individual tasks* belongs to the [issues](issues/index.md)
beneath. Keep the project about means, not ends.

---

## One project, three phases

A project isn't two kinds of thing — it's **one object that moves through a lifecycle**. Its
states group into three phases, and the **`Planned` gate** divides exploration from commitment:

```kroki-d2
@from_file:diagrams/project-lifecycle.d2
```

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

**A project can enter at either phase.** Most start in `Idea` and cross the gate as they mature
(discovery, below). But one whose outcome is **already agreed** can be created **straight into
`Planned`** — it skips discovery, yet still owes a lead, a named KR + delta and dates from the
moment it exists. **Graduation** is different again: it's a *transition* of a project that
already exists in discovery, not a fresh creation. The [`linear-project`](skills/index.md) skill
routes on exactly this — new idea, graduate an existing one, or born committed.

---

## Discovery phase — is there something here? (`Idea` · `Scoping`)

The cheapest way to start work is a project in **`Idea`**. Explore before you commit. A project
in discovery may have **no parent initiative and no named Key Result** — that's legitimate; it's
where an initiative's groundwork gets recorded.

One thing is **not** optional, even here: a **single named lead**. Rule 4 applies from day one —
ownership is named the moment the project exists, at `Idea`, not deferred to `Planned`. Only the
KR and the dates wait for commitment.

At the **`Planned` gate**, discovery resolves into one of three:

| Outcome | What it means |
|---|---|
| **Graduate** | Mature into delivery under an outcome — link an existing initiative, or seed a new one it justifies |
| **Standalone** | Proceed with no initiative — allowed, but questioned (nothing to ladder to) |
| **Drop** | Cancel it; reason recorded |

**Graduate** is a deliberate strategic step: a discovery project matures into delivery attached
to an outcome. When it seeds a *new* initiative, the [`linear-initiative`](initiatives.md) skill
draws on the discovery project's findings to ground the objective and KR baselines, and links
the two so the lineage is recorded. It's distinct from inbound triage — this is
project → initiative, not inbound → project.

---

## Delivery phase — build the committed outcome (`Planned` · `In Progress` · `Launching`)

Committed and linked to an outcome. Now the rules bite.

### Name the Key Result it moves — and by how much

**[Hard rule 2](hard-rules.md):** a project names **which** Key Result(s) it moves and the
**delta** it expects — e.g. "activation 22% → 30%". No KR named, no project. This is what turns
"projects are the how" from a slogan into something checkable, and what the initiative's update
rolls up from.

A project can serve **more than one initiative** — Linear's model is many-to-many. When it does,
name the KR **and delta on each** one it moves. Standalone (no initiative) is allowed but gets
questioned — there's nothing for the work to ladder up to.

### Own it, date it, sequence it

| Your job | Detail |
|---|---|
| Be the single named lead | One person accountable — the deliverer, eng lead or product owner — [rule 4](hard-rules.md) |
| Set start + target-end dates | From `Planned` onward — [rule 5](hard-rules.md); dependencies only tell you about risk once both ends are dated |
| Draw dependencies | At the project level, so sequencing and risk are visible |
| Set a priority | Urgent → Low, to sequence projects against each other |
| Post the update | Weekly to `#project-updates` while In Progress or Launching |

**Completed** means delivered **and the KR delta observed** — not merely shipped. A project that
launched but didn't move its measure isn't done; it's a lesson.

### Labels — two groups, both native project fields

| Group | Values | What it records |
|---|---|---|
| `spend/*` | `capex` · `opex` | How the work is funded — set at planning |
| `product/*` | `hungovercoders` · `dogadopt` · `woolwitch` · … (grows over time) | Which product it serves — **also carried onto its issues** |

`type/*` and `flow/*` are *issue*-level groups, not project ones — see
[Issues](issues/index.md).

---

## Health is a claim with evidence

A project's health — on track / at risk / off track — is a **claim you can defend**, not a
colour someone picked. The evidence is the KR movement and the issue/cycle progress beneath it.
If the work isn't moving the measure, the health says so, however much shipped.

---

## Keep everyone posted

While a project is **In Progress** or **Launching**, its lead ensures a **weekly update** reaches
the shared **`#project-updates`** Slack channel — what changed, the health claim, and any risks.

!!! warning "A project update is only as current as its issues"
    The weekly update **rolls up from the issue and cycle progress** beneath it — the same
    dependency an [initiative update](initiatives.md#keep-everyone-posted) has on its projects.
    If work has stalled or the cycle slipped, say so and don't claim a health greener than the
    evidence. The `linear-project-update` skill flags stale or missing movement for you.

Post it either way:

- **Linear's project update UI** — write the status update on the project and set its health; it
  flows to the connected `#project-updates` channel.
- **The [`linear-project-update`](skills/index.md) skill** — it drafts the standard update (what
  changed + health + risks) and posts it for you.

---

## Create one

What you set depends on the **phase** (above). Either way, one rule holds: everything Linear
models as a field — lead, status, dates, priority, initiative link(s), `spend/*` / `product/*`
labels, connected `#project-updates` channel — is a **native field**, never prose. The
**description** carries only the *what & how*, any **KR(s) + delta**, milestones and *out of
scope* — that part is the template.

- **An idea** (`Idea` / `Scoping`) needs only a **lead**, a **status**, and a description of the
  question it's exploring. No KR, no dates, no initiative yet.
- **A delivery project** (`Planned`+) also needs the **KR(s) + delta**, **initiative link(s)**,
  **start + target-end dates**, a **priority** and the **`spend/*`** / **`product/*`** labels.

1. **Use the [`linear-project`](skills/index.md) skill — preferred.** It routes on entry point
   (new idea · graduate an existing project · born committed), asks only for what the phase
   needs, keeps the native fields native, and gives you the description body to drop in.
2. **By hand.** Create a new project in the [Linear projects view](https://linear.app/happydevs/projects/all),
   set the fields the phase calls for (above), connect the **`#project-updates`** Slack channel,
   then paste [`template.md`](https://github.com/hungovercoders/linear-work-management/blob/main/skills/linear-project/template.md)
   into the description and fill it in. It's the same file the skill uses.

---

## Related

- [The Hard Rules](hard-rules.md) — rules 2 (name the KR + delta), 4 (single lead), 5 (dates)
- [Initiatives](initiatives.md) — the outcome a project graduates under and serves
- [The Cheat Sheet](index.md) — the one-page summary this expands
