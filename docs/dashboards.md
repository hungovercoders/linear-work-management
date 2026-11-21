# Dashboards

<div class="lwm-lead" markdown>
Shared Linear views that show when something has slipped, so nobody has to go hunting.
</div>

## Is anything breaking the rules?

Each of these should be empty. Anything in one is worth a conversation.

[Unclassified issues](https://linear.app/happydevs/view/af5ea30a-d34e-4175-8410-8be8337441f8)
:   Open issues with no project and no `bau/*` label. Issues still in Triage don't count.

[Project and BAU at once](https://linear.app/happydevs/view/82cdb693-867e-455e-83ad-4a6feeb2c4a9)
:   Issues that are in a project and also carry a `bau/*` label.

[Ownerless projects](https://linear.app/happydevs/view/d07503b5-d1ea-4de2-9090-8b397b9787b0)
:   Open projects with no named lead.

[Ownerless initiatives](https://linear.app/happydevs/view/3b3f664d-ba6f-41e9-967b-1532aff6724b)
:   Initiatives with no named owner.

[Undated delivery projects](https://linear.app/happydevs/view/5e8e8163-9f0c-4fee-a210-c781f8c92707)
:   Projects that are `Planned` or later with a start or end date missing.

[Violated dependencies](https://linear.app/happydevs/view/4c475feb-953d-466e-af97-9dcc29bc2cfc)
:   Projects whose [dependency lines](projects.md#dependencies-native-never-prose) have turned
    red.

Views can't read descriptions, so they can't check rules 1 and 2. The doctor does that: run
the [`linear-doctor`](skills/index.md) skill on one team or project, or `task doctor` for
everything.

## How is the work going?

[SLA health](https://linear.app/happydevs/view/c51ef229-df32-4d64-970e-335c369c81ac)
:   Open issues with a deadline.

[Delivery ranking](https://linear.app/happydevs/view/4f97a6df-2be4-4e8a-b143-181cd18f7585)
:   Delivery projects by priority, with health alongside. Use it to decide what comes first.

[All projects](https://linear.app/happydevs/projects/all)
:   Group by status to see how many projects are at each stage. Switch to Timeline to see
    dependencies.

## When to look

Whoever is on triage duty looks over the drift views each week, and anything they find goes in
the [team digest](communications.md). Before a review, run the doctor on whatever is being
reviewed.

Stuck work has its own views on the [Flow](flow.md) page.
