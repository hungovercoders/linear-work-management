# :material-school: Worked example

<div class="lwm-lead" markdown>
One real chain from top to bottom, using the **dogadopt** product: an initiative, the project
under it, three of its issues, and one item that arrived through Triage.
</div>

![Worked example: the dogadopt initiative down through a project to three issues, plus one item that arrived through Triage.](diagrams/example-chain.svg)

Each quoted block is a description as it appears in Linear. The Fields line before it lists
what was set in Linear's own fields.

---

## 1. The initiative

Fields: owner Richard · status `Active` · target date 30 Sep 2026 · Slack channel
`#initiative-updates` connected.

> ## Why this matters
>
> Finding a rescue dog in the UK means trawling dozens of rescue websites that don't talk to
> each other. Adopters give up and dogs wait longer. One place to search every rescue changes
> both.
>
> ## Key Results
>
> ### Measured
>
> | Key Result | Baseline | Target | Evidence |
> |---|---|---|---|
> | ADCH-registered Welsh rescues live in the portal | 0% | 100% | Coverage report (TBD, a dependency) |
> | Monthly active users searching dogs | 0 | 100/month | Plausible dashboard |
> | Outbound click-throughs to a rescue per month | 0 | 1 | Click tracking (TBD) |
>
> ## Out of scope
>
> Completed-adoption tracking (it happens on the rescue's side); rescues outside Wales this
> quarter.
>
> ## Context
>
> Consent from each rescue is part of the bar. Scraping without it is a relationship and legal
> risk, so onboarding includes a consent step.

How it measures up:

- Rule 1 ✓ It has Key Results, each with a baseline, a target and a place to find the evidence.
  Two evidence sources are still TBD, and those need sorting out before they can be scored.
- Rule 4 ✓ It has one owner.
- Rule 5 ✓ It has a target date.

---

## 2. The project

This began as an idea ("could we bring Welsh rescues together?") and joined the initiative above
when it became `Planned`.

Fields: lead Richard · status `In Progress` · dates 11 Aug → 12 Sep 2026 · priority High ·
labels `spend/capex` and `product/dogadopt` · milestones "First rescue live" and "All 12
consented" · Slack channel `#project-updates` connected.

> ## What we're doing and how
>
> Onboard every ADCH-registered Welsh rescue: obtain consent, ingest their available dogs
> via feed or manual entry, refresh at least weekly, and show them in the portal search.
>
> ## Key Results it moves
>
> | Initiative | Key Result | Delta (baseline → target) |
> |---|---|---|
> | Effortless rescue-dog adoption | Welsh rescues live in the portal | 0% → 100% |
>
> ## Out of scope
>
> Non-ADCH rescues; England/Scotland; adopter accounts.
>
> ## Context
>
> 12 rescues on the ADCH register at last count; the denominator may move, so recount at each
> update.

How it measures up:

- Rule 2 ✓ It names the Key Result it moves and by how much.
- It's **Blocked by** the Consent process project. That's recorded as a
  [dependency in Linear](projects.md#dependencies-native-never-prose), so it shows on the timeline.

---

## 3. Three of its issues

| Type | Title | Where it is |
|---|---|---|
| `type/feature` | Show a rescue's dogs on the search page | In `Todo`, refined and ready. It has acceptance criteria and takes `product/dogadopt` from the project |
| `type/bug` | Refresh job drops dogs with no photo | `Urgent`, next to be picked up. It has steps to reproduce and the impact: listings shrink without anyone noticing |
| `type/action` | Nightly confirmation email to rescues | Picked up, with its plan written |

Here is the third one in full. The first four sections were written when the issue was created.
The assignee added the Plan when they picked it up, so the approach could be reviewed before
any code:

> ## What needs doing?
>
> Nightly job emailing each consented rescue a link to confirm their listings are current.
>
> ## Why does it need doing?
>
> "Live" only counts if refreshed; stale listings break the coverage KR's definition.
>
> ## When is it done?
>
> Every consented rescue gets the nightly mail, and a bounce or 14-day silence flags the rescue
> as stale in the coverage report.
>
> ## Context
>
> Rescues asked for email over a portal login, so meet them where they are.
>
> ## Plan
>
> Cloudflare Worker cron 02:00 → for each consented rescue, send confirm-link (Email
> Service) → confirmation hits a Worker route stamping `last_confirmed` → coverage report
> reads the stamp. No login needed; link is signed, 14-day expiry.

All three meet rule 3 ✓ They're in the project, with one `type/*` label and no `bau/*` label.

---

## 4. Something arrives through Triage

An email arrives: "Your site shows a dog we rehomed last week." Whoever is on
[triage duty](issues/triage.md) puts it into Triage and decides what happens to it.

| Question | Answer |
|---|---|
| What kind of thing is it? | `bau/defect`, a fault reported from outside |
| Where does it go? | Into the onboarding project. It's a bug in the refresh job that project is building, so it becomes a `type/bug` there and the `bau/*` label comes off |
| How urgent is it? | High. It damages trust, but nothing is down. An outage would be a `bau/incident` and decided at once |

If the email had been a one-off question, such as "how many collies are listed in Powys?", it
would have stayed BAU: `bau/query`, no project, decided within two working days.

---

## What this shows

Every piece connects to the one above it. The nightly email keeps listings fresh, and fresh
listings are what the coverage Key Result counts. The project promises to move that Key Result
from 0% to 100%. And the initiative says why anyone cares. Ask "why am I doing this?" at any
level and the answer is one step up.

## Related

- [Start here](index.md): the model this follows
- [Initiatives](initiatives.md), [Projects](projects.md) and [Issues](issues/index.md): how to write each piece
- [Glossary](glossary.md): any term above, one line each
