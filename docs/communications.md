# :material-bullhorn: Communications

<div class="lwm-lead" markdown>
Who posts which update, where and how often. The aim is that people hear how things are going
without having to ask, and without being buried in messages.
</div>

## The schedule { #the-cadence }

| Update | Covers | Where | When | Who |
|---|---|---|---|---|
| Initiative update | Key Result movement, health, risks | `#initiative-updates` | Monthly, while `Active` | The initiative's owner |
| Project update | What changed, health, risks | `#project-updates` | Weekly, while `In Progress` or `Launching` | The project's lead |
| Team digest | The cycle and what came through Triage | The team's channel | Weekly | The team |
| Launches and incidents | What happened | `#announcements` | When it happens | Whoever ships or responds |

The skills can draft an update and the channel carries it, but a named person is responsible
for it going out.

![Communication cadence: project and initiative updates rolling up and pushing to channels, with Pulse as the pull feed.](diagrams/comms-cadence.svg)

Project updates feed initiative updates. So when a project goes quiet, the initiative above it
has less to go on.

---

## Health needs evidence { #health-is-a-claim-with-evidence }

Every update says whether the work is on track, at risk or off track. That's a claim, and you
should be able to back it up.

| For | The evidence is |
|---|---|
| A project | How its issues and cycle are moving, and whether its Key Result is shifting |
| An initiative | The weekly updates from its projects |

!!! warning "Don't report green on top of silence"
    If a project under an initiative hasn't reported, or its update is old, the initiative
    update says so and its health reflects that.

Each update skill has a template for the format:
[`linear-project-update`](skills/index.md) and [`linear-initiative-update`](skills/index.md).
You can write the update in Linear yourself or let the skill draft and post it. Both reach the
connected channel.

---

## How updates don't get forgotten { #making-the-cadence-stick }

Nobody has to remember the schedule, because three things back it up.

1. Linear reminds you. Switch on update reminders in workspace settings and pick a day and
   time. Project leads and initiative owners get a prompt, with follow-ups after one and two
   working days. An overdue project shows **Update Missing**, and its health icon fades the
   longer it stays quiet. A single project can change its reminders, or turn them off, from the
   bell icon.
2. The skills do the gathering. `linear-project-update` reads what has moved since the last
   update, and `linear-initiative-update` checks which projects have reported. That leaves you
   to check the draft and add your judgement. A scheduled agent can even have a draft waiting
   for each lead.
3. Silence shows up. The team digest and `task doctor` flag a project with no update for 10
   days and an initiative with none for 35.

---

## :material-rss: Pulse, for catching up

Linear's Pulse is a feed of project and initiative updates across the workspace. It has a
*For me* tab for work you're involved in, plus *Popular* and *Recent*. It can also send a daily
or weekly digest to your Inbox, and read it aloud if you'd rather listen.

Leads still post their updates, because Pulse has nothing to show without them. Everyone else
can catch up in [Pulse](https://linear.app/happydevs/pulse) and skip scrolling through channels.

Pulse is on every Linear plan. A workspace admin enables it in Settings, and you subscribe to
any project you want in your feed.

---

## Keeping the noise down

- There's one channel for each audience. All projects share `#project-updates`, and anyone who
  wants more on one project follows it in Linear or Pulse.
- Channel messages come from the updates themselves, so nobody posts a separate summary.
- `#announcements` is for launches and incidents only. A channel that stays quiet until
  something matters is one people keep reading.

---

## Related

- [Initiatives](initiatives.md) and [Projects](projects.md): where the updates are written
- [Integrations](integrations.md): connecting the Slack channels
- [Skills](skills/index.md): the skills that draft updates
