# The Cheat Sheet

<div class="lwm-lead" markdown>
One page. If you read nothing else, read this. The single source of truth for how we
use Linear: the **[hard rules](hard-rules.md)** are the contract, the
[skills](skills/index.md) apply them for you, and the [glossary](glossary.md) decodes
any term you meet on the way.
</div>

!!! abstract "Why this matters"
    The point of all this is an **unbroken line from *why* to the work in your cycle**: every
    issue ladders up to a project's Key Result and the initiative it serves. People can see
    they're delivering the value expected of them, and why. That connection is the benefit;
    the rules just keep it intact.

    All of it lives in **[Linear](https://linear.app/happydevs)** — strategy, delivery and
    execution in one place, so no tool boundary breaks the line.

---

## :material-sitemap: How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Three layers, and two ways work reaches them (neither is superior or exceptional):

| Path | Flows | What it is |
|---|---|---|
| <span class="lwm-strat">Strategic</span> | Initiative → Project → Issues | Planned work toward an outcome |
| <span class="lwm-inbound">Inbound</span> | Triage → Issue (`flow/*`) | Work that arrives: incidents, requests, compliance, support, toil |

!!! danger "The one failure"
    An issue on **neither** path is *unclassified*: invisible work, the defect the whole
    system chases. The [drift views](dashboards.md) and `linear-doctor` report every one.

---

## :material-gavel: The hard rules

| # | Level | Rule |
|---|---|---|
| 1 | Initiative | **Declares its Key Results** before any project: measured (baseline → target) or committed (done/not-done). A result, not a theme. |
| 2 | Project | **Names the Key Result(s) it moves, and by how much** — by `Planned` (`Idea`/`Scoping` may still be exploring). |
| 3 | Issue | **In a project *or* one `flow/*` label** — never neither, never both. |
| 4 | Ownership | **One named human owns each initiative and each project.** Not a team, not two people. |
| 5 | Time-bounds | **Dated from `Planned` onward**: initiatives a target date, projects start + end. |

If a rule and a convenience conflict, the rule wins. Detail and rationale:
**[The Hard Rules](hard-rules.md)**.

---

## :material-shape-plus: What am I making?

| Situation | Make a… |
|---|---|
| A strategic outcome we want by a date, with measures | **[Initiative](initiatives.md)** |
| A bounded piece of work that moves those measures | **[Project](projects.md)** under the initiative(s) it serves |
| A discrete task within that work | **[Issue](issues/project-work.md)** in the project |
| Something broke, arrived, or was reported | **Issue via [Triage](issues/triage.md)** |
| An idea to explore before committing | **Project in `Idea`** — no initiative or KR needed yet |

**How work starts:** the cheapest way in is a project in `Idea` — discovery, no KR
required. By `Planned` it graduates under an initiative (existing, or one it seeds), goes
standalone (questioned), or drops. The [worked example](examples.md) walks the whole chain.

---

## :material-account-check: Who does what — start with the page that's you

| You are… | You own | Start with |
|---|---|---|
| Strategic leadership | An **outcome** and its measures | **[Initiatives](initiatives.md)** |
| A delivery lead | A **project** — the what, how and when | **[Projects](projects.md)** |
| On the delivery team | **Issues** — is it done? | **[Project work](issues/project-work.md)** |
| On triage duty | The **front door** — where does this go? | **[Triage work](issues/triage.md)** |

---

## :material-map: Where everything lives

- **[Examples](examples.md)** — one real chain, initiative → project → issues → a triage call
- **[Issues](issues/index.md)** — the shared lifecycle, templates and the agent-plan convention
- **[Teams, states & labels](teams.md)** — the canonical enums; org invariants vs team room
- **[Communications](communications.md)** — every update cadence, and Pulse
- **[Dashboards](dashboards.md)** — the drift and portfolio views
- **[Integrations](integrations.md)** — GitHub and Slack wiring
- **[Setup checklist](setup.md)** — everything Linear needs configured, tickable
- **[Skills](skills/index.md)** — the AI skills that do the above on demand
- **[Glossary](glossary.md)** — every term, one line each
