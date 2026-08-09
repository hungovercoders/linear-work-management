# The Cheat Sheet

<div class="lwm-lead" markdown>
One page. If you read nothing else, read this. It is the single source of truth for how we
use Linear. The [hard rules](hard-rules.md) are the contract, the
[skills](skills/index.md) apply them for you, and the [glossary](glossary.md) decodes
any term you meet on the way.
</div>

!!! abstract "Why this matters"
    We want an unbroken line from *why* to the work in your cycle. Every issue traces up to a
    project's Key Result and the initiative it serves, so people can see they're delivering the
    value expected of them, and why. That connection is the benefit; the rules exist to keep it
    intact.

    All of it lives in [Linear](https://linear.app/happydevs), where strategy, delivery and
    execution share one tool and no boundary between them breaks the line.

---

## :material-sitemap: How it fits together

```kroki-d2
@from_file:diagrams/model.d2
```

Start with **work** — the thing you actually do. In Linear a piece of work is an **issue**, and
work comes in two kinds. The only difference is how each one arrives, and neither kind is
superior:

| Kind of work | How Linear holds it | What it is |
|---|---|---|
| <span class="lwm-strat">Project work</span> | An issue in a project, under an initiative (Initiative → Project → Issue) | Planned work toward an outcome |
| <span class="lwm-inbound">Inbound work</span> | An issue that arrived through Triage, on one `flow/*` label | Work that arrives: incidents, requests, compliance, support, toil |

!!! danger "The one failure"
    An issue on neither path is *unclassified*. This is invisible work, the defect the whole
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

Where a rule and a convenience conflict, the rule wins. The detail and rationale sit in
[The Hard Rules](hard-rules.md).

---

## :material-shape-plus: What am I making?

| Situation | Make a… |
|---|---|
| A strategic outcome we want by a date, with measures | **[Initiative](initiatives.md)** |
| A bounded piece of work that moves those measures | **[Project](projects.md)** under the initiative(s) it serves |
| A discrete task within that work | **[Issue](issues/project-work.md)** in the project |
| Something broke, arrived, or was reported | **Issue via [Triage](issues/triage.md)** |
| An idea to explore before committing | **Project in `Idea`** — no initiative or KR needed yet |

How work starts: the easiest way in is a project in `Idea`, which is pure discovery with no
KR required. By `Planned` it either graduates under an initiative (existing, or one it seeds),
goes standalone (and gets questioned for it), or drops. The [worked example](examples.md) walks
the whole chain.

---

## :material-account-check: Who does what — start with the page that's you

| You are… | You own | Start with |
|---|---|---|
| Strategic leadership | An **outcome** and its measures | **[Initiatives](initiatives.md)** |
| A delivery lead | A **project** — the what, how and when | **[Projects](projects.md)** |
| On the delivery team | **The work** — is it done? | **[Project work](issues/project-work.md)** |
| On triage duty | Inbound work — where does this go? | **[Triage work](issues/triage.md)** |

---

## :material-map: Where everything lives

- [Examples](examples.md): one real chain, initiative → project → issues → a triage call
- [Work](issues/index.md): what an issue is, the shared lifecycle, templates and the agent-plan convention
- [Teams, states & labels](teams.md): the canonical enums; org invariants vs team room
- [Communications](communications.md): every update cadence, and Pulse
- [Dashboards](dashboards.md): the drift and portfolio views
- [Integrations](integrations.md): GitHub and Slack wiring
- [Setup checklist](setup.md): everything Linear needs configured, tickable
- [Skills](skills/index.md): the AI skills that do the above on demand
- [Glossary](glossary.md): every term, one line each
</content>
</invoke>
