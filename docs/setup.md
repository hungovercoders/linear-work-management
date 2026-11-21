# Setup checklist

<div class="lwm-lead" markdown>
Everything that needs switching on in Linear for this [way of working](index.md). Ticked items
are already done in `happydevs`, and each heading links to the page that explains it.
</div>

This is one-time setup. For keeping things in order afterwards, use the
[dashboards and the doctor](dashboards.md).

---

## Workspace level (once, for everyone)

#### Workflow states: [States and labels](teams.md#the-shared-state-sets)

- [x] Project statuses: Idea → Scoping → Planned → In Progress → Launching →
      Completed / Canceled ([settings](https://linear.app/happydevs/settings/projects))
- [ ] **Paused** project status added (the API can't create a `paused`-type; one click in settings)
- [x] Initiative statuses: Proposed / Planned / Active / Completed / Canceled, Linear-native
      with nothing to configure

#### Labels: [the label groups](teams.md#the-label-taxonomy) ([settings](https://linear.app/happydevs/settings/labels))

- [x] `type/` group: `action` (default) · `feature` · `bug` · `analysis` · `spike`
- [x] `bau/` group: `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil`
- [x] `spend/` group: `capex` · `opex`
- [x] `product/` group: one value per product (grows over time)
- [ ] Legacy flat labels retired (`Improvement` remains; retire when nothing depends on it)
- [x] Teams know they can add states and labels, but not remove or rename shared ones

#### Views: [Dashboards](dashboards.md)

- [x] The six drift views plus SLA health plus portfolio ranking exist and are shared

#### Integrations: [Integrations](integrations.md) ([settings](https://linear.app/happydevs/settings/integrations))

- [x] GitHub connected; PR → issue state automation per team
- [x] Slack connected
- [ ] `#initiative-updates` and `#project-updates` connected on each initiative and project
      (check the channel spelling first)
- [ ] `#announcements` channel exists for launches and incidents

#### Update reminders: [Updates](communications.md#making-the-cadence-stick)

- [ ] Native update reminders enabled (workspace settings): weekly, targeting project leads and
      initiative owners

#### SLAs: [Triage and BAU](issues/triage.md)

- [x] The `slaBreachesAt` fallback (the `linear-triage` skill), which works on every plan
- [ ] SLA rules for each kind of BAU the team handles, starting with `bau/vulnerability` by
      priority ([the rules](team-setup.md#service-levels))

---

## Per team (each team, on adoption)

#### Issue states: [the shared set](teams.md#issue-states)

- [ ] Triage · Backlog · Planning · Todo · In Progress · In Review · Done · Canceled · Duplicate
      (teams may add their own; Planning is a `backlog`-type state ordered after
      Backlog)

#### Triage: [where BAU work arrives](issues/triage.md)

- [x] Triage enabled for the team
- [ ] **Triage Responsibility** rota assigned (the duty is to decide)
- [ ] Priority required before an issue leaves Triage (team setting)
- [ ] **Triage Rules** auto-applying labels on arrival
- [ ] The team's asks channel connected to its Triage, with templates switched on
      ([how](integrations.md#linear-asks))

#### Cycles: [team-owned](teams.md#team-settings-recommended-not-required)

- [ ] Cycles configured at the team's cadence (weekly recommended); Current and Upcoming views
      visible to others

#### Ownership & membership: [rule 4](hard-rules.md) · [membership](teams.md#membership)

- [x] Team has a named owner and members
- [x] Every initiative and project carries a single named owner or lead (watched by the
      [drift views](dashboards.md))

---

## Check it worked

- Run `task doctor`, which checks the whole workspace. A clean run means the rules hold, and any
  findings point at the box above that still needs attention.
- Look over the [drift views](dashboards.md). Each one should be empty.

## Related

- [States and labels](teams.md): the shared lists this checklist sets up
- [Dashboards](dashboards.md): keeping things in order afterwards
- [Integrations](integrations.md): GitHub and Slack in detail
