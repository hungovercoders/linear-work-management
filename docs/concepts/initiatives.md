# Initiatives

Initiatives describe the **what and why** at a strategic level. They lean into an
OKR style and steer away from *how* — that is the job of the projects beneath them,
unless something is an explicit top-down "must have".

## The standard

An initiative is compliant when it has:

- **What & why** — the outcome and why it matters, OKR-style.
- **A named owner** — typically strategic seniority. Never leave one ownerless.
- **Stated importance** — why this is worth doing now.
- **A success measure** — how you will know it worked.
- **A passed agreement gate** — it only moves `new → active` (or becomes time-bound)
  once agreed strategically.

## Owning and agreeing

Initiatives tend to be owned by strategic seniority. Moving an initiative from an idea
to active work is a deliberate, agreed decision — not a default. Projects below it then
determine the *how*.

!!! tip "Related skill: `linear-initiative`"
    Create or bring an initiative up to this standard automatically.

    ```text
    /plugin marketplace add dataGriff/linear-work-management
    /plugin install linear-work-management@linear-work-management
    ```

    Then ask Claude to *"use linear-initiative to review this initiative"*. See all
    [skills](../skills/index.md).

!!! note "Expected view"
    Initiatives should be monitored from a saved view (build to match if it does not
    exist yet): `linear.app/happydevs/initiatives`.
