---
name: linear-team-setup
description: Check a Linear team against the recommended team setup and report what is still missing: a named owner, the shared issue states, Triage with someone on duty, an asks channel, an SLA rule and an issue template for each kind of BAU, steady cycles, and initiatives for this quarter's objectives. Reads what Linear exposes and asks the team owner about the rest. Use when setting up a new team, adopting the Ways of Working, or checking an existing team's setup.
linear_skill: true
---

<!-- doc: team-setup.md -->

# linear-team-setup

Walk a team owner through the recommended team setup and tell them what is still to do. This
skill reports and explains. It changes nothing in Linear.

**Requires:** the **Linear MCP server** connected, to read the team, its states, labels and
cycles.

> Some of the setup lives in Linear's settings and can't be read through the MCP: SLA rules,
> issue templates, Triage responsibility and the Slack asks channel. Ask the owner about those
> and record their answers as stated, not as verified.

## What good looks like

- Every item is marked done, missing, or not checkable, with one line on how to finish it.
- Nothing is reported as done on an assumption.
- The owner leaves with a short list in the order to do it.

## Flow

1. Ask which team, and read it (`list_teams`). Note its owner and members.
2. Check what Linear exposes:
   - The shared issue states exist: Triage, Backlog, Planning, Todo, In Progress, In Review,
     Done, Canceled, Duplicate (`list_issue_statuses`). Extra states are fine. A missing or
     renamed shared state is a finding.
   - The four label groups exist with their values (`list_issue_labels`): `type/*`, `bau/*`,
     `spend/*`, `product/*`.
   - Cycles are on, and their length is steady (`list_cycles`).
   - The team leads an initiative for each of this quarter's objectives, each with an owner, Key
     Results and a target date.
3. Ask the owner about what Linear doesn't expose:
   - Is Triage on, with Triage responsibility assigned to a named person?
   - Is the team's asks channel connected in Slack, with templates switched on?
   - Is there an SLA rule for each kind of BAU the team handles? At least `bau/incident`,
     `bau/support`, and `bau/vulnerability` by priority (Urgent 7 days, High 30, Medium 90).
   - Is there an issue template for each kind, setting its `bau/*` label and a priority?
   - Does each person have one home team?
   - Where does the team see its objectives every day?
4. Report using the headings below. Put what to do next first.

## The report

```text
<team>: setup check

To do next
1. <the most useful missing item, and how to do it>
2. <...>

Done
- <item>

Not checkable here (as the owner stated)
- <item>: <their answer>
```

Finishing any of these is the owner's job. Offer to help with the ones a skill covers, such as
drafting the quarter's initiatives.
