---
name: linear-team-digest
description: Draft the weekly team digest for a Linear team: current-cycle progress (done, in flight, stalled) plus the triage digest (what arrived, how it was routed, what's still waiting), ready to post to the team's channel. Rolls up from live issue and Triage state. Use weekly, at the team's cadence point.
---

<!-- doc: communications.md -->

# linear-team-digest

Draft the **weekly team digest**: what the cycle achieved, what's in flight, and what arrived in
Triage. It's the team-level rhythm in the
[cadence](https://linear-work-management.pages.dev/communications/), where project and initiative
updates have their own skills and this one is the team's.

**Requires:** the **Linear MCP server** connected, to read the team's cycle and Triage state.

## What to gather

- The current cycle (`list_cycles`, `list_issues` filtered to the team plus cycle): issues Done
  this week, In Progress or In Review, and anything stalled (no state change since last digest).
- Triage activity: issues that arrived in Triage this week, how they were routed (accepted into a
  project, accepted as flow, redirected, merged, declined), and what's still waiting, with the
  oldest item's age (the decision clock is watching).
- Anything the team should flag upward, such as a slipped milestone or a blocked dependency.

## Flow

1. Which team is this digest for, and what's its current cycle.
2. Read the week: gather the lists above with scoped, minimal queries (paginate, the team's slice
   only).
3. Fill the digest from [`template.md`](template.md) beside this skill, keeping each list to the
   items worth a sentence, with counts for the rest.
4. Hand it over to post to the team's channel. Team digests aren't a native Linear update type,
   so there's no connected-channel automation; the human posts it, or a scheduled agent does.

## Related

- [Communications](https://linear-work-management.pages.dev/communications/) — the cadence this serves
- [Triage work](https://linear-work-management.pages.dev/issues/triage/) — the five outcomes it reports on
