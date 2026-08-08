---
name: linear-project-update
description: Post the weekly status update for an active Linear project to the shared #project-updates channel — what changed, a health claim (on track / at risk / off track) backed by evidence, and any risks. Rolls up from the project's issue and cycle progress and flags stale or missing movement. Uses Linear's project status updates. Use weekly while a project is In Progress or Launching.
---

<!-- doc: projects.md -->

# linear-project-update

Post the weekly update for a project that's **In Progress** or **Launching**. Health is a claim
with evidence, not a colour someone picked — the issue and cycle progress is the evidence.

**Requires:** the **Linear MCP server** connected — to read the project and post the update.

> The update posts to the shared **`#project-updates`** Slack channel automatically, as long as
> that channel is connected to the project (done when the project is created).

## What to gather

- The project, its Key Result(s) + delta, and its last update.
- The **issues in the project** and their state / cycle progress — the movement rolls up from
  these.
- Whether the current cycle is on track, and any milestone that slipped.
- What materially changed; any risks; anything you need to unblock it.

## Flow

1. Identify the project and read its KR(s), dates and last update (`list`/`get`).
2. **Check the movement underneath.** List the project's issues and their states / cycle
   (`list_issues`, `list_cycles`). Note whether work is progressing or **stalled** — no issues
   moved, or the cycle slipped.
3. Fill the update body from [`template.md`](template.md) — what changed, KR/delta progress,
   risks, and the **progress-reporting** note (stalled work or a slipped cycle, or that it's on
   track).
4. Decide **health** — on track / at risk / off track — justified by that movement. **A project
   can't be greener than the issues moving its KR**: if work has stalled or the cycle slipped,
   temper the health and say why.
5. Post with `save_status_update` (`type: project`, `project: <name or id>`, `health`, `body`).

## The update template

[`template.md`](template.md) beside this skill is the single source of truth for the update
**body**. **Health** is a native field on the status update — set it there, backed by the
movement shown in the body, never as a line of prose instead.

See [`skills/README.md`](https://github.com/dataGriff/linear-work-management/tree/main/skills)
for the conventions every skill here follows.
