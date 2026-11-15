# :material-account-group: Teams, states and labels

<div class="lwm-lead" markdown>
The shared lists every team uses: which states work moves through, and which labels exist. If
a value isn't on this page, it isn't shared.
</div>

!!! abstract "In short"
    - The organisation sets a small number of things so that work looks the same across teams.
    - Teams decide the rest for themselves.
    - Teams can add their own states and labels. They can't remove or rename the shared ones.

---

## :material-scale-balance: What's shared and what's yours

Reports and cross-team views only work if a few things mean the same everywhere. These are set
for the whole organisation:

| Shared by everyone | Where it's described |
|---|---|
| The five hard rules | [The hard rules](hard-rules.md) |
| The states for initiatives, projects and issues | [States](#states), below |
| The labels | [Labels](#labels), below |
| Every issue being in a project or carrying one `flow/*` label | [Issues](issues/index.md) |
| When updates are posted, and where | [Communications](communications.md) |
| How fast inbound work is decided and fixed | [Triage work](issues/triage.md) |

How a team runs day to day is up to the team. The suggestions further down are only
suggestions.

### Add, but don't remove or rename

A team can add a state its workflow needs, or a label of its own. It can't remove or rename a
shared one, because then the same word would mean different things in different teams.

The shared lists do change now and then. When they do, every team adopts the change together,
which is how the `Planning` issue state arrived.

!!! example "For example"
    The `happydevs` team has a Review Requested state next to the shared ones, and that's fine.
    Renaming `Done` or deleting `Triage` would not be.

---

## :material-tag-multiple: Labels { #labels }

There are four groups, and you can browse them in
[Linear settings → Labels](https://linear.app/happydevs/settings/labels).

| Group | Values | Goes on | Set when |
|---|---|---|---|
| `type/*` | `action` (default) · `feature` · `bug` · `analysis` · `spike` | Project issues | The issue is created |
| `flow/*` | `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil` | Inbound issues, exactly one each | It arrives or is triaged |
| `spend/*` | `capex` · `opex` | Projects | The project is planned |
| `product/*` | `hungovercoders` · `dogadopt` · `woolwitch` · `cheeserater` · … (grows) | Projects, and their issues inherit it | The project is planned |

A few things to know:

- An issue never has both a `type/*` and a `flow/*` label. The first means project work and the
  second means inbound work ([rule 3](hard-rules.md)).
- `product/*` is decided once, on the project. Its issues take the same value.
- There's no `risk/*` group. The product labels replaced it.
- The old Improvement label belongs to no group. Don't use it on new work.

??? note "Why `flow/defect` and `flow/query`, when `type/*` has `bug` and `analysis`?"
    Linear label names have to be unique across the whole workspace, even between groups. The
    `type/*` group uses `bug` and `analysis`, so the inbound equivalents are `defect` (a fault
    reported from outside) and `query` (a one-off data question).

---

## :material-list-status: States { #states }

The [Initiatives](initiatives.md), [Projects](projects.md) and [Issues](issues/index.md) pages
all take their states from here. The closing state is spelled `Canceled` throughout, the way
Linear spells it.

### Initiative states

Linear's built-in statuses already match, so there's nothing to set up.

**Proposed → Planned → Active → Completed** (or **Canceled**)

### Project states

Set once for the workspace, under Settings → Projects.

| Phase | States |
|---|---|
| Discovery | **Idea** → **Scoping** |
| Delivery | **Planned** → **In Progress** → **Launching** (with **Paused** available) |
| Closed | **Completed** · **Canceled** |

### Issue states

Set for each team, matching this list.

**Triage → Backlog → Planning → Todo → In Progress → In Review → Done** (or **Canceled** ·
**Duplicate**)

Nobody counts how long an issue sits in `Backlog`. The counting starts at `Planning`, because
time spent there shows whether refinement is keeping up ([Flow](flow.md)).

---

## :material-tune: Suggestions for teams { #team-settings }

None of these are required.

- Turn [Triage](issues/triage.md) on, and assign Triage responsibility so that someone is always
  on duty.
- Run cycles at whatever length suits you. We suggest a week, which is short enough to show
  what got done. Anything bigger belongs in project milestones.
- Keep your Current and Upcoming cycle views visible to other teams, so people can see what's
  coming without asking.
- Estimates are optional. If you use them, use them for your own planning and don't compare
  them across teams.

## :material-account-multiple: Membership { #membership }

Every team has a named owner and named members. We suggest each person has one home team, even
if they work on several projects, so that the team digest and cycle views stay meaningful.

Manage teams in [Linear settings → Teams](https://linear.app/happydevs/settings/teams).

---

## Related

- [The hard rules](hard-rules.md): what these lists support
- [Issues](issues/index.md): how issues use the labels
- [Start here](index.md): the overview
