# :material-clipboard-check: Setup checklist

Everything Linear needs configured to run the [Ways of Working](index.md), in one place you can
self-check for readiness. The checklist summarises, and each item links to the page that owns the
why. This is the one-time setup; ongoing drift belongs to the
[doctor and the dashboards](dashboards.md).

Current `happydevs` state is reflected below, and ticked items are done.

---

## Workspace level (once, for everyone)

#### Workflow states: [Teams, states & labels](teams.md)

- [x] Project statuses: Idea → Scoping → Planned → In Progress → Launching →
      Completed / Canceled ([settings](https://linear.app/happydevs/settings/projects))
- [ ] **Paused** project status added (the API can't create a `paused`-type; one click in settings)
- [x] Initiative statuses: Proposed / Planned / Active / Completed / Canceled, Linear-native
      with nothing to configure

#### Labels: [the taxonomy](teams.md#the-label-taxonomy) ([settings](https://linear.app/happydevs/settings/labels))

- [x] `type/` group: `action` (default) · `feature` · `bug` · `analysis` · `spike`
- [x] `flow/` group: `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil`
- [x] `spend/` group: `capex` · `opex`
- [x] `product/` group: one value per product (grows over time)
- [ ] Legacy flat labels retired (`Improvement` remains; retire when nothing depends on it)
- [x] Additive-only understood: teams add, never remove or rename shared values

#### Views: [Dashboards](dashboards.md)

- [x] The six drift views plus SLA health plus portfolio ranking exist and are shared

#### Integrations: [Integrations](integrations.md) ([settings](https://linear.app/happydevs/settings/integrations))

- [x] GitHub connected; PR → issue state automation per team
- [ ] Slack connected, with `#initiative-updates` and `#project-updates` wired to their objects
      (check the channel spelling first)
- [ ] `#announcements` channel exists for launches and incidents

#### Update reminders: [Communications](communications.md#making-the-cadence-stick)

- [ ] Native update reminders enabled (workspace settings): weekly, targeting project leads and
      initiative owners

#### SLAs: [Triage work](issues/triage.md)

- [x] The `slaBreachesAt` fallback (the `linear-triage` skill), which works on every plan
- [ ] Native SLA rules for `flow/vulnerability` severity windows, Business/Enterprise only;
      skip until upgraded

---

## Per team (each team, on adoption)

#### Issue states: [the shared set](teams.md#issue-states)

- [x] Triage · Backlog · Todo · In Progress · In Review · Done · Canceled · Duplicate
      (local additions allowed, additive only)

#### Triage: [where inbound work arrives](issues/triage.md)

- [x] Triage enabled for the team
- [ ] **Triage Responsibility** rota assigned (the duty is to *decide*)
- [ ] Priority required before an issue leaves Triage (team setting)
- [ ] **Triage Rules** auto-applying labels on arrival, Business/Enterprise; manual until then

#### Cycles: [team-owned](teams.md#team-settings-recommended-not-required)

- [ ] Cycles configured at the team's cadence (weekly recommended); Current and Upcoming views
      visible to others

#### Ownership & membership: [rule 4](hard-rules.md) · [membership](teams.md#membership)

- [x] Team has a named owner and members
- [x] Every initiative and project carries a single named owner or lead (watched by the
      [drift views](dashboards.md))

---

## Verify it

- Run **`task doctor`** (headless, whole workspace). A clean bill of health means the invariants
  hold; findings tell you exactly which box above is lying.
- Glance at the [drift views](dashboards.md), where empty is the goal.

## Related

- [Teams, states & labels](teams.md) — the canonical enums this checklist verifies
- [Dashboards](dashboards.md) — the ongoing-drift counterpart
- [Integrations](integrations.md) — the wiring items in detail
