# :material-monitor-dashboard: Dashboards

<div class="lwm-lead" markdown>
Shared Linear views that show when something has slipped, so nobody has to go hunting. All of
them already exist in the `happydevs` workspace.
</div>

## Drift views: is anything breaking the rules?

Each of these should be empty. Anything that appears in one is worth a conversation.

| View | Shows | Rule |
|---|---|---|
| [Unclassified issues](https://linear.app/happydevs/view/af5ea30a-d34e-4175-8410-8be8337441f8) | Open issues with no project and no `bau/*` label. Issues still in Triage don't count | [3](hard-rules.md) |
| [Project and BAU at once](https://linear.app/happydevs/view/82cdb693-867e-455e-83ad-4a6feeb2c4a9) | Open issues that are in a project and also carry a `bau/*` label | [3](hard-rules.md) |
| [Ownerless projects](https://linear.app/happydevs/view/d07503b5-d1ea-4de2-9090-8b397b9787b0) | Open projects with no named lead | [4](hard-rules.md) |
| [Ownerless initiatives](https://linear.app/happydevs/view/3b3f664d-ba6f-41e9-967b-1532aff6724b) | Initiatives with no named owner | [4](hard-rules.md) |
| [Undated delivery projects](https://linear.app/happydevs/view/5e8e8163-9f0c-4fee-a210-c781f8c92707) | Projects that are `Planned` or later with a start or end date missing | [5](hard-rules.md) |
| [Violated dependencies](https://linear.app/happydevs/view/4c475feb-953d-466e-af97-9dcc29bc2cfc) | Projects whose [dependency lines](projects.md#dependencies-native-never-prose) have turned red | |

Rules 1 and 2 are about what's written in a description, and Linear views can't filter on that.
The doctor checks those two, and it also checks for overdue updates. Run the
[`linear-doctor`](skills/index.md) skill on one team or project, or `task doctor` for the whole
workspace.

The views for work that is stuck in a queue are on the [Flow](flow.md) page.

---

## Portfolio views: how is the work going?

| View | Use it to |
|---|---|
| [SLA health](https://linear.app/happydevs/view/c51ef229-df32-4d64-970e-335c369c81ac) | See open issues with a deadline, against the [fix deadlines](issues/triage.md#two-clocks) |
| [Delivery ranking](https://linear.app/happydevs/view/4f97a6df-2be4-4e8a-b143-181cd18f7585) | Put delivery projects in order. Group by priority and look down the health column. Leadership still makes the call, and this gives them something to make it with |
| [All projects](https://linear.app/happydevs/projects/all) | See how many projects are at each stage. Group by status |
| [Projects timeline](https://linear.app/happydevs/projects/all) | See dependencies. Switch the display to Timeline and the lines appear, blue while the dates work and red when they don't |

---

## When to look

- Every week, whoever is on triage duty looks over the drift views, and anything they find goes
  into the [team digest](communications.md).
- Before a review, run [`linear-doctor`](skills/index.md) on whatever is being reviewed, or
  `task doctor` for everything.
- Add the views to your sidebar favourites. Grouping and ordering are personal display settings,
  so arrange them however you like.

---

## Related

- [The hard rules](hard-rules.md): what the drift views check
- [Flow](flow.md): spotting where work gets stuck
- [Communications](communications.md): where findings get discussed
