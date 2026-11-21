---
name: linear-objectives
description: Help a team choose its objectives for the quarter and draft them as Linear initiatives: review the mission, look at eight areas with real numbers, pick three objectives, give each three Key Results that stretch, mark which are must-haves, and form a first hypothesis for each. Use at the start of a quarter, when a team is setting OKRs, or when its current objectives no longer fit.
linear_skill: true
---

<!-- doc: team-setup.md -->

# linear-objectives

Coach a team through choosing three objectives for the quarter, then draft each as an
initiative the team leads. The team chooses. This skill asks the questions and writes up the
answers.

**Requires:** the **Linear MCP server** connected, to read the team's current projects and
link new ones.

> Linear's API can't create initiatives, so this skill hands back a description for each
> objective to paste into a new initiative. Set the owner, the lead team and the target date in
> Linear's own fields.

## What good looks like

- Three objectives. With more than three, none gets enough attention.
- Three Key Results each, with numbers, so partial success still counts.
- Targets the team is 70 to 80% likely to reach, and each one marked as a must-have
  (committed) or a stretch (measured).
- Each Key Result names where its evidence comes from.
- No objective for keeping the lights on. That is BAU, and its SLAs measure it.

## Flow

1. Mission. Ask for the team's mission and tenets. They rarely change. If the team has none,
   write them first, in a sentence or two.
2. Look at the numbers. Go through eight areas and ask what the data says about each:
   precision (can we tell which area needs attention), performance, deliverability, cost,
   reliability, risk, developer experience, and integration with other teams. If the team is
   guessing, make getting the numbers the first objective.
3. **Pick three areas, then three objectives.** Check each against existing initiatives. If one
   already covers it, the team's work belongs there as a project.
4. **Key Results.** Three for each objective. For each, ask whether it is measured (baseline,
   target, evidence) or committed (a definition of done), and whether the target stretches.
5. Sleep on it. Suggest confirming the next day. Objectives often look different then.
6. First hypotheses. For each objective, ask what the team believes would move a Key
   Result. Each hypothesis becomes a project in `Idea`, with a lead and a line on what it
   explores.
7. Write them up. Fill [`template.md`](template.md) once for the quarter. Give the team an
   initiative description for each objective (why it matters, the Key Results, what's out of
   scope) to create in Linear with the team as lead team.

## The objectives template

[`template.md`](template.md) beside this skill is the one-page summary of the quarter, for the
team's channel and wherever the team sees its objectives daily.
