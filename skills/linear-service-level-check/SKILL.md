---
name: linear-service-level-check
description: Run a team's weekly service level check in Linear: BAU issues whose SLA is at risk or breached, BAU issues that should carry an SLA and don't, how many SLAs closed this week as achieved or failed, and the oldest item waiting in Triage. Asks about the measures Linear can't see, such as uptime and software near end of life, and proposes a BAU issue for each one that has slipped. Use weekly, or when someone asks how the team's BAU is doing.
linear_skill: true
---

<!-- doc: team-setup.md -->

# linear-service-level-check

Report how a team's BAU stands against its service levels this week. BAU exists to keep those
promises, and Linear's SLAs measure most of them.

**Requires:** the **Linear MCP server** connected, to read the team's BAU issues and their SLAs.

## What to gather

- Open BAU issues (one `bau/*` label, no project) for the team, with their SLA
  (`list_issues`, reading `slaBreachesAt` and the SLA status).
- Those at high risk or already breached. These come first.
- Open `bau/incident`, `bau/vulnerability` and `bau/support` issues with no SLA at all. They are
  unmeasured, usually because a priority is missing.
- BAU issues closed in the last seven days, and whether each SLA was achieved or failed.
- The oldest item still in Triage and its age.
- From the person running the check: the measures Linear can't see. Uptime against the team's
  target, critical vulnerabilities reported by scanners, and software within three months of
  its end of life.

## Flow

1. Ask which team, and gather the lists above with scoped queries.
2. Fill in [`template.md`](template.md).
3. For each service level that has slipped and has no issue yet, propose a BAU issue with its
   `bau/*` label and a priority. Create it only once the person agrees, because a priority is
   theirs to set.
4. If the share of SLAs achieved has fallen for several weeks, or BAU is taking most of the
   team's time, say so plainly. That is the evidence for making the cause an objective next
   quarter.

## The check template

[`template.md`](template.md) beside this skill is the report. Keep it short: name what needs a
decision, and count the rest.
