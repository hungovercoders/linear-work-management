# :material-account-group: Teams, states & labels

The canonical reference for who owns what in the workspace. It holds the shared sets the
organisation defines so the whole works together, and the room teams keep for their own ways of
working. The [doctor](skills/index.md) and the dashboards test against this page, so if a value
isn't here, it isn't shared.

---

## :material-scale-balance: Org invariants vs team room

The organisation defines the invariants every team honours, because cross-team visibility and
roll-ups break without them:

| Org-defined (shared) | Where it's specified |
|---|---|
| The five hard rules | [The Hard Rules](hard-rules.md) |
| The shared state sets (initiative · project · issue) | [below](#the-shared-state-sets) |
| The label taxonomy | [below](#the-label-taxonomy) |
| Issue classification (project XOR `flow/*`) | [Issues](issues/index.md) |
| Update cadence to the shared channels | [Initiatives](initiatives.md) · [Projects](projects.md) |
| SLAs (decision + resolution clocks) | [Triage work](issues/triage.md) |

Teams own their own internal ways of working. For those the org recommends and makes options
available without mandating them. Everything below is marked as one or the other.

### The additive-only rule

Teams may add to the shared sets, whether an extra state their workflow needs or a local label,
but never remove or rename shared values. Insights only stay comparable across teams if the
shared values mean the same thing everywhere.

!!! example "A live example"
    The `happydevs` team carries a Review Requested state alongside the shared set, a legitimate
    local addition. Renaming shared Done or deleting Triage would not be.

---

## :material-tune: Team settings (recommended, not required)

- Triage on: every team enables [Triage](issues/triage.md) so inbound work has somewhere to
  arrive, with a **Triage Responsibility** rota so the duty is named.
- Cycles (team-owned): teams run cycles at their own cadence. The org recommends weekly, a short
  feedback loop that shows a week's worth of achievement; anything larger belongs to project
  milestones rather than longer cycles. Whatever the cadence, keep the team's Current and
  Upcoming cycle views visible to others, which is where the team's near-term work can be seen
  without asking.
- Estimates are optional. If used, keep them for the team's own planning rather than cross-team
  comparison.

## :material-account-multiple: Membership

- Every team has a named owner and members, since accountability needs names (org-level).
- Recommended: a person has one home team, even when active on several projects. A project can
  draw on multiple teams while the person's home stays singular, so the team digest and cycle
  views mean something.

Manage teams in [Linear settings → Teams](https://linear.app/happydevs/settings/teams).

---

## :material-tag-multiple: The label taxonomy

Four groups, workspace-level, created and maintained to exactly these values; browse them in
[Linear settings → Labels](https://linear.app/happydevs/settings/labels).

| Group | Values | Lives on | Set |
|---|---|---|---|
| `type/*` | `action` (default) · `feature` · `bug` · `analysis` · `spike` | Project issues | At capture |
| `flow/*` | `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil` | Inbound issues (exactly one) | At arrival / triage |
| `spend/*` | `capex` · `opex` | Projects | At planning |
| `product/*` | `hungovercoders` · `dogadopt` · `woolwitch` · `cheeserater` · … (grows) | Projects, carried onto their issues | At planning |

- `type/*` and `flow/*` never meet: a `type/*` means project work, a `flow/*` means inbound
  ([rule 3](hard-rules.md)).
- `product/*` is decided once, on the project, and issues inherit it rather than re-deciding it.
- There is no `risk/*` group; product attribution replaced it.

!!! note "Why `flow/defect` + `flow/query` (not `bug` + `analysis` again)?"
    Linear label names are unique across the whole workspace, even between groups, so
    the `type/*` group owns `bug` and `analysis`, and the inbound counterparts take their own
    names: `defect` (a fault reported from outside) and `query` (an ad-hoc data ask).

!!! warning "Legacy label"
    The flat Improvement label predates the taxonomy and belongs to no group. Don't use it on
    new work, and retire it once nothing depends on it.

---

## :material-list-status: The shared state sets

The single source the [Initiatives](initiatives.md), [Projects](projects.md) and
[Issues](issues/index.md) pages reference. The terminal state is spelled **Canceled**
(Linear-native) throughout.

### Initiative states

Linear's native initiative statuses match the model's five with no configuration needed:

**Proposed → Planned → Active → Completed** (or **Canceled**)

### Project states

Workspace-level project statuses (Settings → Projects), configured to:

| Phase | States |
|---|---|
| Discovery | **Idea** → **Scoping** |
| Delivery | **Planned** → **In Progress** → **Launching** (with **Paused** available) |
| Closed | **Completed** · **Canceled** |

### Issue states

Per-team workflow states, matching the shared set:

**Triage → Backlog → Todo → In Progress → In Review → Done** (or **Canceled** · **Duplicate**)

Teams may add local states (additive-only) while the shared ones stay untouched, so cross-team
views stay comparable.

---

## Related

- [The Cheat Sheet](index.md) — the one-page summary
- [The Hard Rules](hard-rules.md) — the invariants these sets serve
- [Issues](issues/index.md) — how classification uses the label groups
