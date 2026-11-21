# Integrations

<div class="lwm-lead" markdown>
GitHub moves issues along as code ships, and Slack carries the updates. Both are set up once in
[Linear settings](https://linear.app/happydevs/settings/integrations).
</div>

## GitHub

Connected to the [hungovercoders](https://github.com/hungovercoders) organisation. For code
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

!!! warning "Not connected yet"
    Connecting Slack is a one-time sign-in under
    [settings](https://linear.app/happydevs/settings/integrations). After that, connect the two
    update channels to each initiative and project as you create them.

`#initiative-updates`
:   Monthly initiative updates. Connect the channel on each initiative.

`#project-updates`
:   Weekly project updates. Connect the channel on each project.

`#announcements`
:   Launches and incidents, posted by whoever ships or responds.

Channels get updates only, so nobody is pinged for every state change. And when a decision is
made in a Slack thread, write it on the issue: Slack is for talking, Linear is the record.

??? note "Linear Asks"
    Asks creates issues from Slack requests. It needs the Business or Enterprise plan, which we
    don't have, so requests come in through [Triage](issues/triage.md).

??? note "The GitHub link as a diagram"
    ![GitHub to Linear: branch, push, PR and merge driving issue state as a side effect.](diagrams/github-flow.svg)
