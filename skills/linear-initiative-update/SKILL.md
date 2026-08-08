---
name: linear-initiative-update
description: Post the monthly status update for an active Linear initiative to #initiative-updates — Key Result movement, a health claim (on track / at risk / off track) backed by evidence, and any risks. Uses Linear's initiative status updates. Use monthly while an initiative is Active.
---

<!-- doc: initiatives.md -->

# linear-initiative-update

Post the monthly update for an **Active** initiative. Health is a claim with evidence, not a
colour someone picked — the Key Result movement is the evidence.

**Requires:** the **Linear MCP server** connected — to read the initiative and post the update.

> The update posts to the **`#initiative-updates`** Slack channel automatically, as long as that
> channel is connected to the initiative (done when the initiative is created).

## What to gather

- The initiative and its Key Results (their targets).
- The current value of each KR (measured) or done / not-done (committed), and the trend since
  the last update.
- The **projects under the initiative** and each one's **latest status update** — the KR
  movement rolls up from these.
- What materially changed; any risks; anything you need from leadership.

## Flow

1. Identify the initiative and read its Key Results and last update (`list`/`get`).
2. **Check the feeding projects.** List the initiative's projects and each one's latest
   status update (`get_status_updates`, `type: project`). Note any project with **no update**
   or a **stale** one (older than its weekly cadence).
3. Fill the update body from [`template.md`](template.md) — the KR movement table, what
   changed, risks & asks, and the **project-reporting** note (which projects are missing or
   stale, or that all reported).
4. Decide **health** — on track / at risk / off track — justified by the KR movement. **An
   initiative can't be greener than the projects moving its KRs**: if feeding projects are
   silent or stale, temper the health and say why.
5. Post with `save_status_update` (`type: initiative`, `initiative: <name or id>`, `health`,
   `body`).

## The update template

[`template.md`](template.md) beside this skill is the single source of truth for the update
**body**. **Health** is a native field on the status update — set it there, backed by the
movement shown in the body, never as a line of prose instead.
