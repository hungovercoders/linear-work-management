# Hierarchy

Everything in Linear hangs off three nested levels, with **teams** doing the work.

```kroki-d2
direction: right

initiatives: Initiatives\n(what & why) {
  style.fill: "#EEF2FF"
}
projects: Projects\n(what + how) {
  style.fill: "#E0E7FF"
}
issues: Issues\n(the work) {
  style.fill: "#C7D2FE"
}

initiatives -> projects
projects -> issues
```

| Level | Purpose | Time horizon | Owned by |
| ----- | ------- | ------------ | -------- |
| **Initiative** | The strategic *why & what* | Quarters+ | Strategic seniority |
| **Project** | The *what + how* that furthers an initiative | Weeks–months | A single lead |
| **Issue** | A concrete unit of work | Hours–days | A team |

**Relationships**

- One **initiative** → many **projects**.
- One **project** → many **issues**, and can involve **many teams**.
- A **team** owns issues and can belong to multiple projects.

**Why it matters:** this is what makes work visible and lets any issue be traced up to
the strategy it serves. Read on into [Initiatives](initiatives.md),
[Projects](projects.md) and [Issues](issues.md).
