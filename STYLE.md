# Writing style

This repo's content is written for people, and it should read that way. Machine-drafted prose has a
handful of habits that give it away, and they crept into these pages more than once. This page
names them so the next edit avoids them, and `task lint:prose` checks the countable ones on
every build.

The aim is plain, varied, human writing. Not stiff, not breathless, not decorated.

## The tells, and what to do instead

| Tell | Why it reads as machine-written | Do this instead | Budget |
|---|---|---|---|
| Em-dash overuse | Dashes stand in for commas, colons and full stops, giving every sentence the same breathless break | Use the ordinary mark. Keep a dash for a real aside | ≤4 per page (prose; tables and field comments exempt) |
| Antithesis formula | "X, not Y", "isn't X; it's Y", "never X, never Y" manufactures contrast the reader didn't ask for | Say what a thing *is*. The contrast is usually clear without it | — (rule 3's "never both, never neither" is the one keeper) |
| Rule of three | Three parallel clauses in a row sound authoritative and land as filler | Use two items, or four. Break the parallelism | — |
| Punchy fragments | "Not a theme." "A lesson." A verbless line for effect reads as affected | Write the full sentence | — |
| Colon-then-payoff | "The deal:", "The one failure:" primes the reader for a reveal that rarely earns it | State it plainly | — |
| Parallel openings | Bullets or sentences that all start the same way | Vary the lead-in; let asymmetry carry the weight | — |
| Over-bolding | Bold on ordinary words turns documentation into advertising | Bold only a term where it's defined, or a native field name | ≤8 spans per page (prose) |
| Signposting | "This page covers…", "as noted above" restates what the layout already shows | Delete it; trust the structure | — |
| Pet metaphors | One image ("front door", "ladder up") repeated across pages becomes a tic | Vary it, or drop it | ≤2 uses of any one, corpus-wide |
| Aphoristic closers | Every section ending on a neat epigram | At most one memorable line per page; let the rest end on substance | — |
| One register | The same confident cadence in every paragraph | Vary sentence length on purpose. A plain concession where one fits | not linted; read for it |

## Keep

Tables, the label and state enums, the five hard rules, the worked example's real numbers,
skill templates, cross-links, and the Linear-native state name **Canceled**. The tells are a
prose problem, not a structure one.

## Check it

```bash
task lint:prose
```

It reports em-dash and bold budgets per file, caps on the banned words, and warns on the
register patterns it can spot. Green means the countable tells are in check. The register still
needs a human read.
