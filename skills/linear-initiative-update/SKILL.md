---
name: linear-initiative-update
description: Post the monthly status update for an active Linear initiative to #initiatives — Key Result movement, a health claim (on track / at risk / off track) backed by evidence, and any risks. Uses Linear's initiative status updates. Use monthly while an initiative is Active.
---

# linear-initiative-update

Post the monthly update for an **Active** initiative. Health is a claim with evidence, not a
colour someone picked — the Key Result movement is the evidence.

**Requires:** the **Linear MCP server** connected — to read the initiative and post the update.

> The update posts to the **`#initiatives`** Slack channel automatically, as long as that
> channel is connected to the initiative (done when the initiative is created).

## What to gather

- The initiative and its Key Results (their targets).
- The current value of each KR (measured) or done / not-done (committed), and the trend since
  the last update.
- What materially changed; any risks; anything you need from leadership.

## Flow

1. Identify the initiative and read its Key Results and last update (`list`/`get`).
2. Fill the update body from [`template.md`](template.md) — the KR movement table, what
   changed, and risks & asks.
3. Decide **health** — on track / at risk / off track — justified by the KR movement, not a
   gut feel.
4. Post with `save_status_update` (`type: initiative`, `initiative: <name or id>`, `health`,
   `body`).

## The update template

[`template.md`](template.md) beside this skill is the single source of truth for the update
**body**. **Health** is a native field on the status update — set it there, backed by the
movement shown in the body, never as a line of prose instead.
