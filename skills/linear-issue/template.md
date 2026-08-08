<!-- The issue DESCRIPTION only. Set these as native Linear fields, NOT in this text:
       • Assignee   → the one person doing it
       • Priority   → Urgent → Low, so it orders against the others
       • Status     → Backlog (new) → Todo once refined; nothing starts from Backlog
       • Classify   → in a PROJECT (project issue) OR one flow/* label (inbound) — rule 3, never both
       • type/*     → project issues only: feature | bug | action | spike
       • product/*  → inherited from the project, unchanged

     The body below is the same for every type — write it as a PROMPT someone (or an agent)
     can act on. Emphasis by type:
       • feature → the change and its acceptance criteria
       • bug     → steps to reproduce, expected vs actual
       • action  → the change and why now
       • spike   → the question to answer and the time box -->

## Problem
<what needs doing and why — clear enough to start without asking. For a bug: steps to
 reproduce, expected vs actual. For a spike: the question to answer and the time box.>

## Done when
<the acceptance criteria — how we'll know it's finished, not merely shipped>

## Agent plan
<!-- The body above is the prompt. Store the plan for HOW here once worked out, so it's
     reviewable before the code is. Leave empty until then. -->
<the approach; the steps; anything the implementer needs to know>
