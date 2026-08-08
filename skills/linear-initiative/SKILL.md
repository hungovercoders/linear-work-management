---
name: linear-initiative
description: Create or update a Linear initiative to the documented standard — what & why (OKR-style), a named owner, clear importance and success measures, and the strategic agreement gate before it goes active. Use when starting, reviewing, or tidying an initiative in the happydevs workspace.
---

<!-- doc: concepts/initiatives.md -->

# linear-initiative

Bring a Linear initiative up to the operating-model standard. The full rules and
rationale live in the guide: **[Initiatives](https://linear-work-management.pages.dev/concepts/initiatives/)**.

> Reference skill. This is the minimal, working version shipped with the Foundation
> sub-issue to prove the plugin + skill↔docs pattern. It is fully built out in GRI-70.

## The standard (what "good" looks like)

An initiative is compliant when it has:

1. **What & why, OKR-style** — the outcome and why it matters. Avoid *how* (that is the
   job of projects) unless it is an explicit top-down "must have".
2. **A named owner** — strategic seniority. Never leave an initiative ownerless.
3. **Why it is important** — the strategic rationale, stated plainly.
4. **How success is measured** — the signal(s) that tell you it worked.
5. **A passed agreement gate** — an initiative only moves `new → active` (or becomes
   time-bound) once it has been agreed strategically.

## How to apply

1. Identify the initiative (ask for the name/URL, or that a new one is needed).
2. Read it with the Linear MCP tools; check each of the five points above.
3. Draft the missing pieces with the user, keeping description to *what & why*.
4. Save via the Linear MCP `save_project`/initiative tools with the owner set.
5. Only set the state to active once the agreement gate is met.

## Related

- Guide: [Initiatives](https://linear-work-management.pages.dev/concepts/initiatives/)
- Hierarchy: [How it fits together](https://linear-work-management.pages.dev/concepts/hierarchy/)
