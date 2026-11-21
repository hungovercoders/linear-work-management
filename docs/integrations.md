# Integrations

<div class="lwm-lead" markdown>
GitHub moves issues along as code ships. Slack carries updates out and brings requests in. Both are set up once in
[Linear settings](https://linear.app/happydevs/settings/integrations).
</div>

## GitHub

The [GitHub integration](https://linear.app/docs/github-integration) is connected to the
[hungovercoders](https://github.com/hungovercoders) organisation. For code
work, you never need to move an issue by hand.

1. Copy the branch name from the issue (`Cmd/Ctrl` `Shift` `.`) and create your branch with it.
2. Push, open a pull request and merge as usual.

<ol class="lwm-flow">
  <li><b>Push the branch</b>Issue moves to In Progress</li>
  <li><b>Open a pull request</b>Issue moves to In Review</li>
  <li class="is-done"><b>Merge</b>Issue moves to Done</li>
</ol>

Didn't start from the issue's branch name? Write *Fixes GRI-123* in the pull request description
and it links and closes the issue on merge.

## Slack

[Slack](https://linear.app/docs/slack) does two jobs: it carries updates out, and it brings requests in.

### Updates going out

`#initiative-updates`
:   Monthly initiative updates. Connect the channel on each initiative.

`#project-updates`
:   Weekly project updates. Connect the channel on each project.

`#announcements`
:   Launches and incidents, posted by whoever ships or responds.

Channels get updates only, so nobody is pinged for every state change. And when a decision is
made in a Slack thread, write it on the issue: Slack is for talking, Linear is the record.

### Requests coming in { #linear-asks }

[Linear Asks](https://linear.app/docs/linear-asks-slack) turns a Slack message into an issue. Each team has its own
asks channel, connected to that team's [Triage](issues/triage.md). Whoever is on duty picks
requests up from there.

Colleagues raise a request by reacting to a message with 🎫, typing `/asks`, or mentioning
`@Linear Asks`. They don't need a Linear account, and replies stay in step between the Slack
thread and the issue.

To connect a team's channel:

1. In Linear, open **Settings → Features → Asks**.
2. Add the team's Slack channel and link it to the team.
3. Turn on the templates you want people to choose from. One for each common `bau/*` kind
   works well.
4. In Slack, run `/invite @Linear Asks` in that channel.

??? note "What depends on the Linear plan"
    Asks is on the Business and Enterprise plans. Linear's docs list per-channel settings,
    private channels and creating an Ask from every new message as Enterprise features. On
    Business, people can still raise an Ask from any public channel and choose the team's
    template, so a channel per team works as a habit even where Linear doesn't enforce it.

