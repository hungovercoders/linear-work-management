# Initiatives

<div class="lwm-lead" markdown>
<span class="lwm-for">For leadership</span>

An [initiative](https://linear.app/docs/initiatives) is an outcome we want, and the measures that
tell us whether we got it. You say why it matters. The [projects](projects.md) underneath work out
how.
</div>

[Open the initiatives list in Linear](https://linear.app/happydevs/initiatives){ .md-button }

??? abstract "See it as a diagram"
    ![Where an initiative comes from: one project graduating, several aggregating, or leadership naming an outcome.](diagrams/initiative-origin.svg)

## What every initiative needs

<div class="lwm-need" markdown>

- A name people can get behind, like "Make onboarding effortless"
- Three to five Key Results
- One owner. It can have a lead team too, but its projects may sit in other teams, so a person
  has to answer for it
- A target date

</div>

## Writing Key Results

Key Results say how you'll know it worked. There are two kinds. Use whichever fits, and don't
force a number where one doesn't belong.

Measured
:   For outcomes you can count. Give a baseline, a target and where the number comes from.
    *Activation rate: 22% → 30%, from signups reaching first value in 7 days.*

Committed
:   For work that has to happen. Give a definition of done.
    *SOC 2 Type II: report issued with no exceptions.*

Every project underneath picks one of these and says how far it will move it. At the end, you
score them.

!!! tip "New initiative, or part of an existing one?"
    If the work would move a Key Result you already have, link the project to that initiative.
    Start a new one only when the outcome is new.

## From proposal to done

<ol class="lwm-flow">
  <li class="is-quiet"><b>Proposed</b>Being considered</li>
  <li class="is-gate"><b>Planned</b>Agreed. Owner, Key Results and date are set</li>
  <li><b>Active</b>Projects are moving the Key Results</li>
  <li class="is-done"><b>Completed</b>Key Results met, or time's up and scored</li>
</ol>

An initiative can also be `Canceled`, with the reason recorded. Linear fixes these states, so
there's nothing to set up.

## Every month while it's active { #keep-everyone-posted }

The owner posts an [update](https://linear.app/docs/initiative-and-project-updates) to
`#initiative-updates`: how the Key Results have moved, whether it's on track, and any risks. Write
it on the initiative in Linear, or let the `linear-initiative-update` skill draft it.

You build your update from the weekly project updates beneath it. If a project has gone quiet,
say so in yours.

## Create one

=== "With the skill"

    Ask Claude to "draft an initiative". The [`linear-initiative`](skills/index.md) skill asks
    about the outcome, the Key Results, the owner and the date, then gives you a description to
    paste in.

=== "By hand"

    1. Create an initiative in [Linear](https://linear.app/happydevs/initiatives).
    2. Set the owner, status (`Proposed`) and target date in Linear's own fields.
    3. Paste [`template.md`](https://github.com/hungovercoders/linear-work-management/blob/main/skills/linear-initiative/template.md)
       into the description and fill it in.
    4. Connect the `#initiative-updates` Slack channel.

??? note "Where initiatives come from"
    <div class="lwm-cards">
      <div class="lwm-card is-slate"><span class="lwm-kicker">Most common</span><b>Graduation</b><span>One exploratory project grows big enough to stand alone.</span></div>
      <div class="lwm-card is-slate"><span class="lwm-kicker">Several into one</span><b>Aggregation</b><span>A few projects turn out to be parts of the same outcome.</span></div>
      <div class="lwm-card is-quiet"><span class="lwm-kicker">From the top</span><b>Spontaneous</b><span>Leadership names an outcome with nothing behind it yet.</span></div>
    </div>
    <div class="lwm-arrow">↓</div>
    <div class="lwm-node"><b>Initiative</b><span>Key Results, one owner and a target date, whichever way it began.</span></div>

    When an initiative grows out of projects, the skill reads them, uses what they found for the
    objective and baselines, and links them so the history is kept.

??? note "Sub-initiatives (Enterprise plan only)"
    On Linear's Enterprise plan you can nest initiatives as
    [sub-initiatives](https://linear.app/docs/sub-initiatives), up to five levels deep. A parent
    rolls up its children's projects and progress, while each child keeps its own owner and Key
    Results. Use them when one objective spans several teams or phases. Otherwise keep it flat.
