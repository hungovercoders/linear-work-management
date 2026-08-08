---
name: linear-stakeholder-deck
description: Generate a stakeholder slide deck from live Linear state — the initiative portfolio with Key Results, health and owners, then a project drill-down per initiative. Runs the headless deck script for the data, then adds the narrative judgement (KR movement, risks, asks). Use before a stakeholder review or when someone asks "where are we?".
---

<!-- doc: communications.md -->

# linear-stakeholder-deck

Make stakeholder feedback cheap: a slide deck generated from **live Linear state**, so the
review reflects reality, not a hand-built snapshot that was stale on arrival.

**Requires:** `LINEAR_API_KEY` in the environment (initiatives aren't readable via the Linear
MCP; the data comes from the headless script).

## Flow

1. **Generate the data deck.** Run `task deck` (`scripts/linear_deck.py`); it emits a Marp
   markdown deck: portfolio table (initiative · status · health · owner · target), one slide
   per initiative with its KR tables lifted from the description, and a projects drill-down
   per initiative (status · health · lead · dates).
2. **Add the judgement.** The script gives the *state*; the deck needs the *story*. For each
   initiative, add a line of narrative: KR movement since last review, the biggest risk, the
   ask (decision, resource, unblock). Health stays [a claim with evidence](https://linear-work-management.pages.dev/communications/):
   don't upgrade a colour the updates don't support, and say when a feeding project hasn't
   reported.
3. **Trim to the audience.** A portfolio review keeps every initiative one slide; a deep-dive
   keeps one initiative and its project slides. Cut, don't shrink fonts.
4. **Render.** `npx @marp-team/marp-cli deck.md -o deck.html` (or present the markdown
   directly; it reads fine).

## What good looks like

- Every number traces to Linear: anyone can click through and see the same state.
- Health colours match the latest posted updates; silence is shown as "no update posted",
  never as green.
- The asks are explicit — a review that ends without decisions was a status email.

## Related

- [Communications](https://linear-work-management.pages.dev/communications/) — the updates this rolls up
- [Dashboards](https://linear-work-management.pages.dev/dashboards/) — the always-on counterpart
