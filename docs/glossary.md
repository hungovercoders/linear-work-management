# Glossary

Every term the guide and the skills use, one line each.

## The model

Initiative
:   An outcome we want, with Key Results that say how we'll know it worked. [Initiatives](initiatives.md)

Project
:   A piece of work with one lead that moves a Key Result. [Projects](projects.md)

Issue
:   One task a person can pick up and finish. [Issues](issues/index.md)

Team
:   The group that owns a set of issues, with its own Triage, cycles and states. A team can lead projects and initiatives that other teams also work on. An issue belongs to one team only. [Teams](how-teams-work.md)

Lead team
:   The one team named as driving a project or an initiative. Other teams can still contribute

Service level
:   A standing promise a team keeps, such as uptime or how fast it fixes a vulnerability. It doesn't reset each quarter, and BAU work exists to keep it. [Team setup](team-setup.md#service-levels)

Key Result (KR)
:   How an initiative is measured. Either measured (a number with a baseline and a target) or committed (done or not done, with a definition of done)

Delta
:   How far a project promises to move a Key Result, such as "activation 22% → 30%". The guide mostly says "by how much"

Ladder
:   The skills' word for the line from an issue, through its project's Key Result, up to the initiative

Health
:   On track, at risk or off track. Always a claim backed by evidence. [Updates](communications.md#health-is-a-claim-with-evidence)

## Projects growing up

Discovery
:   The `Idea` and `Scoping` states, where a project explores. It needs a lead and a line on what it's exploring

The `Planned` gate
:   The point where a project commits. It now needs a Key Result, a delta and dates

Graduation
:   A discovery project becoming delivery work under an initiative

Seeding
:   The skills' word for starting a new initiative from what a discovery project found

Aggregation
:   Starting one initiative from what several projects found

## Issues and triage

Classification
:   Rule 3: every issue is in a project or carries exactly one `bau/*` label

Unclassified
:   An issue with neither, which nobody can place

BAU work
:   Business as usual: work nobody planned that arrived (incidents, requests, compliance, support, toil). It has a `bau/*` label and no project, and it's measured against the team's service levels. [Triage and BAU](issues/triage.md)

Linear Asks
:   Linear's way of turning a Slack message into an issue. Each team has an asks channel that feeds its Triage. [Integrations](integrations.md#linear-asks)

Triage responsibility
:   Linear's duty rota. The named person who decides what happens to each item in Triage

The five outcomes
:   What a triage decision can be: accept into a project, accept as BAU, redirect, merge or decline

Decision clock
:   How quickly an item in Triage must be routed. At once for incidents, one or two working days otherwise

Fix deadline
:   How quickly a vulnerability must be fixed: 7, 30 or 90 days by severity. The skills call it the resolution clock

Planning (issue state)
:   The state between Backlog and Todo, where the team has committed and is working out the details. Different from a project being `Planned`

Time in state
:   How long an issue has sat in its current state. Backlog isn't counted. [Flow](flow.md)

Agent-plan convention
:   The description is the brief, written when the issue is created. The `## Plan` section is filled in when someone picks it up. [Issues](issues/index.md#the-body-is-the-prompt)

Native fields
:   Anything Linear has a field for (owner, dates, priority, labels, milestones, dependencies) goes in that field and stays out of the description

## Labels

`type/*`
:   The kind of project issue: `action` (default), `feature`, `bug`, `analysis` or `spike`. [Labels](teams.md#the-label-taxonomy)

`bau/*`
:   The kind of BAU issue: `incident`, `vulnerability`, `defect`, `query`, `compliance`, `support` or `toil`

`spend/*`
:   How a project is funded: `capex` or `opex`

`product/*`
:   Which product the work serves. Set on the project and inherited by its issues

Additive-only
:   The rule that teams may add states and labels, but never remove or rename shared ones. [States and labels](teams.md)

## Keeping it honest

The doctor
:   `linear-doctor` (one team or project, interactive) and `task doctor` (the whole workspace). Both report problems and neither fixes them

Drift
:   Anything that has slipped out of line with the rules. [Dashboards](dashboards.md)

Pulse
:   Linear's feed of project and initiative updates. [Updates](communications.md)

