# :material-monitor-dashboard: Dashboards

The model is only honest if drift is **visible without going looking**. These shared Linear
views surface hard-rule breaches and portfolio state at a glance — each exists in the
`happydevs` workspace exactly as documented here.

---

## Drift views — the hard rules, watched

| View | Catches | Rule |
|---|---|---|
| [Drift — unclassified issues](https://linear.app/happydevs/view/af5ea30a-d34e-4175-8410-8be8337441f8) | Open issues in **no project** with **no `flow/*`** label (Triage-state exempt — that's the front door working) | [3](hard-rules.md) |
| [Drift — project and flow at once](https://linear.app/happydevs/view/82cdb693-867e-455e-83ad-4a6feeb2c4a9) | Open issues in a project **and** carrying `flow/*` — never both | [3](hard-rules.md) |
| [Drift — ownerless projects](https://linear.app/happydevs/view/d07503b5-d1ea-4de2-9090-8b397b9787b0) | Open projects without a single named lead | [4](hard-rules.md) |
| [Drift — ownerless initiatives](https://linear.app/happydevs/view/3b3f664d-ba6f-41e9-967b-1532aff6724b) | Initiatives without a named owner | [4](hard-rules.md) |
| [Drift — undated delivery projects](https://linear.app/happydevs/view/5e8e8163-9f0c-4fee-a210-c781f8c92707) | `Planned`-or-later projects missing a start or target-end date | [5](hard-rules.md) |
| [Drift — violated dependencies](https://linear.app/happydevs/view/4c475feb-953d-466e-af97-9dcc29bc2cfc) | Projects whose [dependency lines](projects.md#dependencies-native-never-prose) have gone red | — |

Empty views are the goal. Anything in one is a conversation, not a decoration.

!!! note "Rules 1 and 2 belong to the doctor"
    "Initiative declares Key Results" and "project names a KR + delta" live in **description
    content**, which Linear views can't filter on. The [`linear-doctor`](skills/index.md)
    (interactive, scoped) and `task doctor` (headless, whole-workspace) check those — plus
    stale updates against the [cadence](communications.md). Views watch the native fields;
    the doctor reads the prose.

---

## Portfolio views — running the work

| View | Shows |
|---|---|
| [SLA health](https://linear.app/happydevs/view/c51ef229-df32-4d64-970e-335c369c81ac) | Open issues carrying an SLA, watched against the [resolution clock](issues/triage.md) |
| [Portfolio — delivery ranking](https://linear.app/happydevs/view/4f97a6df-2be4-4e8a-b143-181cd18f7585) | Delivery projects for sequencing — group by **priority**, eye the **health** column; prioritisation stays a leadership judgment, this view just makes it answerable |
| [All projects](https://linear.app/happydevs/projects/all) | Lifecycle spread — group by **status** to see Idea → Launching → Completed at a glance |
| [Projects timeline](https://linear.app/happydevs/projects/all) | The dependency graph — switch the display to **Timeline** and the connector lines appear, blue while dates work, red when violated |

---

## The rhythm

- **Weekly** — whoever's on triage duty glances at the drift views; findings land in the
  [team digest](communications.md).
- **Before any review** — run the [`linear-doctor`](skills/index.md) on the slice under
  review, or `task doctor` for the whole workspace.
- Views are **shared, workspace-level** — favourite them into your sidebar; grouping and
  ordering are display settings, so set them once per your taste.

---

## Related

- [The Hard Rules](hard-rules.md) — what these views enforce
- [Communications](communications.md) — where findings get talked about
- [Teams, states & labels](teams.md) — the enums the filters rely on
