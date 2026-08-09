# :material-book-open-variant: Glossary

Every term the guide leans on, one line each. Terms link to the page that owns them.

| Term | Meaning |
|---|---|
| **Key Result (KR)** | A measurable outcome an [initiative](initiatives.md) declares — **measured** (a metric with baseline → target) or **committed** (a deliverable with a Definition of Done). |
| **Delta** | The movement a [project](projects.md) promises on a KR — "activation 22% → 30%". Rule 2 is the KR *plus* its delta. |
| **Ladder** | The traceable line from an issue up through its project's KR to the initiative it serves — the point of the whole model. |
| **Classification** | Rule 3's requirement: every issue is in a **project** or carries exactly one **`flow/*`** label — never both, never neither. |
| **Unclassified** | An issue on neither path — invisible work. |
| **Flow work** | [Inbound work](issues/triage.md) that *arrives* (incidents, requests, compliance, support, toil) rather than being planned — classified by a `flow/*` label, living outside projects. |
| **Graduation** | A discovery project crossing the `Planned` gate into delivery — linking an existing initiative or seeding a new one from its findings. |
| **Seeding** | Creating a new initiative *from* a discovery project's findings, rather than from a blank page. |
| **Aggregation** | Forming one initiative from the shared findings of **several** projects. |
| **The `Planned` gate** | The moment a project commits: rules 2 (KR + delta) and 5 (dates) switch on, and the graduate / standalone / drop decision is made. |
| **Discovery** | The `Idea` / `Scoping` phase — exploring at low cost; a named lead but no KR or dates required yet. |
| **Decision clock** | How fast [triage](issues/triage.md) must *route* an inbound issue — immediate for incidents, 1–2 working days otherwise. |
| **Resolution clock** | How fast certain flow work must be *fixed* — vulnerability remediation by severity (7 / 30 / 90 days). |
| **Triage Responsibility** | Linear's native duty rota — the named person whose job this cycle is to *decide* on each inbound item. |
| **The five outcomes** | Every triage decision is one of: accept into a project · accept as flow · redirect · merge · decline. "Leave it sitting there" isn't one. |
| **Agent-plan convention** | The issue body is the **prompt** (written at capture); the `## Plan` section is filled **at pickup**, so the approach is reviewable before the code. See [Issues](issues/index.md). |
| **Native fields, not prose** | Anything Linear models as a field (owner, dates, priority, labels, milestones, dependencies) is set as that field, never written into a description; that's what makes views, roll-ups and the doctor work. |
| **`type/*`** | The project-issue kind label: `action` (default) · `feature` · `bug` · `analysis` · `spike`. [Reference](teams.md#the-label-taxonomy). |
| **`flow/*`** | The inbound kind label: `incident` · `vulnerability` · `defect` · `query` · `compliance` · `support` · `toil`. |
| **`spend/*`** | Project funding: `capex` or `opex`, set at planning. |
| **`product/*`** | Which product the work serves — set on the project, inherited by its issues. |
| **Additive-only** | Teams may *add* to shared states/labels, never remove or rename them — cross-team views stay comparable. |
| **Health** | On track · at risk · off track — always a **claim with evidence** (KR movement, issue progress). [Communications](communications.md). |
| **Roll-up dependency** | An initiative's health is only as good as its projects' updates — silence tempers it. |
| **The doctor** | `linear-doctor` (scoped, interactive) and `task doctor` (headless, whole-workspace) — report drift from the rules; never fix. |
| **Pulse** | Linear's native feed of project/initiative updates — the *pull* surface beside the cadence's *push*. [Communications](communications.md). |
