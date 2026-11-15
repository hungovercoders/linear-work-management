# Projects

<div class="lwm-lead" markdown>
For delivery leads. A project is a piece of work with a start, an end and one person leading
it. Its job is to move a Key Result on an [initiative](initiatives.md).
</div>

[See every project in Linear.](https://linear.app/happydevs/projects/all) That list shows what's
being built, who leads each piece, which measure it moves and whether it's on track.

!!! abstract "In short"
    - Anyone can start a project in `Idea`. All it needs is a lead and a line on what it's
      exploring.
    - To become `Planned`, it names the Key Result it moves and by how much, and gets dates.
    - While it's being built, the lead posts an update every week.
    - It's `Completed` when the work shipped and the Key Result moved.
    - The `linear-project` skill walks you through all of it.

---

## The life of a project

A project is one thing that grows up. It starts as an idea and, if the idea holds, becomes
committed work.

![Project lifecycle: Idea, Scoping, Planned and In Progress, then into Done or Closed.](diagrams/project-lifecycle.svg)

| State | Phase | Means |
|---|---|---|
| Idea | Discovery | Someone's thought of it. Nothing is committed |
| Scoping | Discovery | Being shaped, with cost and value under investigation |
| Planned | Delivery | Agreed, dated and resourced, but not started |
| In Progress | Delivery | Being built |
| Launching | Delivery | Built and rolling out |
| Paused | Delivery | Stopped on purpose, with a reason and a review date |
| Completed | Closed | Delivered, and the Key Result moved |
| Canceled | Closed | Stopped for good, with the reason recorded |

A project whose outcome is already agreed can skip discovery and be created straight into
`Planned`. It then needs everything a planned project needs from its first day.

---

## Discovery: is there something here? { #discovery-phase-is-there-something-here-idea-scoping }

Starting a project in `Idea` is the easiest way to begin any work. Explore first and commit
later. At this stage the project needs no initiative, no Key Result and no dates.

It does need one named lead from the first day ([rule 4](hard-rules.md)), and a description of
the question it's exploring.

When the project is ready to become `Planned`, decide what the idea turned into.

| Decision | What it means |
|---|---|
| Graduate | It becomes delivery work under an initiative. Link an existing initiative, or start a new one that the findings justify |
| Go standalone | It goes ahead with no initiative. That's allowed, but expect to be asked why |
| Drop | Cancel it and record the reason |

When a project starts a new initiative, the `linear-initiative` skill uses the project's
findings to write the objective and the baselines, and links the two.

---

## Delivery: what a planned project needs

From `Planned` onward the project is a commitment, and every rule applies.

| You need | Detail |
|---|---|
| A Key Result and a delta | Which Key Result it moves and by how much, such as "activation 22% → 30%" ([rule 2](hard-rules.md)). If it serves several initiatives, name one for each |
| One named lead | The person delivering it, usually an eng lead or product owner ([rule 4](hard-rules.md)) |
| Start and target end dates | So it can be put in order against other projects ([rule 5](hard-rules.md)) |
| A priority | Urgent to Low |
| Two labels | `spend/*` (`capex` or `opex`) for how it's funded, and `product/*` for the product it serves. Its issues inherit the product label |
| Dependencies | Drawn in Linear as [relations between projects](#dependencies-native-never-prose) |

The project's description covers what you're doing and how, the Key Result table, what's out
of scope and any context. Why the outcome matters belongs to the initiative, and the individual
tasks belong to the [issues](issues/index.md).

A project is `Completed` when it has delivered and the Key Result has moved. If it launched and
the number didn't change, it isn't done yet, though what you learned is still worth having.

### Dependencies { #dependencies-native-never-prose }

If your project can't start until another finishes, record that with Linear's **Blocked by** and
**Blocking** relations. A dependency written into a description goes stale as soon as dates
move, whereas a relation shows up in views and warns you.

- Draw them when the project becomes `Planned` and both projects have dates. Look again whenever
  dates move.
- On the project, press `⌘K`, choose *Dependencies*, then *Blocked by…* or *Blocking…*. On the
  [timeline view](https://linear.app/happydevs/projects/all) you can drag from the end of one
  project's bar to another.
- The timeline draws a line between the two. It's blue while the dates work, and it turns red
  when the blocking project now ends after the blocked one starts. Red means the two leads need
  to talk.

---

## Weekly updates { #keep-everyone-posted }

While a project is `In Progress` or `Launching`, its lead posts an update to `#project-updates`
every week. It covers what changed, the health (on track, at risk or off track) and any risks.

You can write the update on the project in Linear and set its health there, and it posts to the
connected channel. Or let the [`linear-project-update`](skills/index.md) skill draft and post it.

!!! warning "Health has to match the evidence"
    Health is a claim you can back up with how the issues are moving and whether the Key Result
    is shifting. If work has stalled or the cycle slipped, say so. Plenty shipping while the
    number stays still is not "on track".

[Communications](communications.md) has the full schedule.

---

## Create one

1. The quick way is the [`linear-project`](skills/index.md) skill. It asks whether this is a new
   idea, an existing idea ready to be planned, or work that's already agreed, and then asks only
   for what that stage needs.
2. To do it by hand, create a project in the
   [Linear projects view](https://linear.app/happydevs/projects/all) and paste in
   [`template.md`](https://github.com/hungovercoders/linear-work-management/blob/main/skills/linear-project/template.md).
   It's the same file the skill uses.

Either way, anything Linear has a field for goes in that field and stays out of the description.
That covers the lead, status, dates, priority, initiative links, labels and milestones. Then
connect the `#project-updates` Slack channel so updates post there.

---

## Related

- [The hard rules](hard-rules.md): rules 2, 4 and 5 apply here
- [Initiatives](initiatives.md): the outcome a project serves
- [Project work](issues/project-work.md): the issues inside a project
- [Start here](index.md): the overview
