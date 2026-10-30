# `p550-star-velocity` — the instrument `Gap 549-E` demanded

## The gap

`p549` graded the trending feeds and could not finish the job:

> **Registered as `Gap 549-E`:** this base has **no instrument for a star
> *velocity***, only for a star *level*, and every trending feed trades in
> velocity.

It also named the fix, correctly:

> The cheap fix is this base's own history: `git log` over its published figures
> already **is** a time series, at pass granularity — `DeepTutor` moved
> **49 850 → 51 247** between `p537` and `p549`. So velocity is derivable from
> the base itself and does **not** require the channel the feeds use.

## What this is

`star_velocity.py` reconstructs, per address, the series of star figures **this
base has published about itself** over its own 709-commit history. It calls
`git log` and `git show` and nothing else — **no network**. `Gap 547-E` cost
this base two passes to a channel outage; a history instrument cannot be taken
off the air.

```
./star_velocity.py HKUDS/DeepTutor                  # per-commit series
./star_velocity.py --summary HKUDS/DeepTutor ...    # one row per address
```

## The rule — `declared_star_cell/rev5`

A **star claim** is a table row that contains `github.com/<owner>/<repo>` *and*
sits in a table whose header row **declares** a `Stars` column. The header is
located as the row immediately above the `|---|` delimiter, so it **resets at
every table** — a table with no Stars column cannot inherit another's index.

**There is no positional fallback, by design.** `rev3` had one and it was
wrong: on this base's own pages it returned **11 408** for `DeepTutor` at `p521`
by picking a number out of a narrative table that declares no Stars column at
all. A table that does not declare stars is not making a star claim, and
guessing which cell meant stars manufactures data. Silence from a non-stars
table is **correct silence**.

### The identity-column constraint (`rev5`)

The address must appear in a cell **before** the `Stars` column — in the row's
identity columns — not in its trailing prose.

`rev4` lacked this and was wrong in the worst way available to an instrument:
it **manufactured a defect in the data it was auditing**.
[`repos/foundations.md`](../../../repos/foundations.md) carries a row for
[`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) (**291★**) whose description
reads *"the same lab behind [OATutor](https://github.com/CAHLR/OATutor)"*. rev4
matched that row for the address `CAHLR/OATutor`, took **pyBKT's** star figure,
compared it against OATutor's own **274**, and reported a `SPLIT` — accusing
this base of publishing two figures for one repository. Measured to settle it:
**pyBKT is 291★ exactly, OATutor is 274★ exactly.** The base was right on both
cells; the rule was wrong.

On every shelf layout here the identity columns precede `Stars`
(`| Agent | Repo | Licence | Stars | …`, `| Repo | Licence | Stars | …`), so
"before the stars column" is the portable spelling of *"is this row **about**
the address, or does it merely **cite** it?"* — registered as `Gap 550-D`,
**citation is not attribution**. A cross-reference inside a description cell is
the commonest thing on these pages, since this base's whole value is that its
rows explain each other; rev4 would have mis-attributed a figure to **every**
address this base cross-references.

Two further cell-parsing details are load-bearing, both found by being wrong first:

| Defect in `rev3` | Cause | Fix in `rev4` |
|---|---|---|
| `49 850 · 6 138 forks` → **498506138** | `·` was stripped as decoration, then the spaces were stripped as digit separators, concatenating stars and forks | the cell is **cut at the first `·`** before anything is removed |
| `50.5k *(rounded)*` → `UNPARSED` | a trailing parenthetical note was read as prose | a trailing `(...)` is stripped as an annotation **about** the figure |

U+202F and U+2009 appear **inside** published figures on these pages (`49 850`),
so they are removed as digit separators rather than treated as cell boundaries.
A blanket "strip non-ASCII" would eat them, which is why `GLYPHS` is narrow.

## What it guarantees

1. **No network.** Reproducible offline.
2. **The rule travels with the figure** (`Gap 549-B`): every row carries
   `declared_star_cell/rev4`.
3. **`UNPARSED` is never `0`** (`Gap 549-A` one level down). A declared star
   cell published as `UNREAD` or prose is emitted with its raw text preserved.
4. **Velocity carries its window.** `days` always prints beside `delta`;
   `per_day` is blank on a 0-day window. Many passes land on one date here, so
   most pass-to-pass windows are 0 days — the base's time resolution is
   *finer* than a day in pass count and *coarser* than a day in dating, and
   neither fact is hidden by this output.
5. **Intra-commit disagreement is a result, not a tie to break.** If one commit
   publishes two different figures for one address, **both** are emitted and
   marked `SPLIT`.

Guarantee 5 is the highest-value one, and it is what found `Gap 550-A`:
`p549` wrote *"stale by 1 397★ — **corrected here**"* and published `51 247` in
a re-attestation table **while leaving the shelf row at `49 850`**. One commit,
two figures, six passes running. No hand audit found that in six passes; the
first run of this instrument did.

## Results, `2026-10-30`, `p550`

- `result.series.2026-10-30-p550.tsv` — **696 observations**, 14 of 15 addresses queried
  (`OS4ED/openSIS-Classic` yields 0 — see `Gap 550-C`)
- `result.summary.2026-10-30-p550.tsv` — one row per address

Headlines, all derived from this repository's own committed bytes:

| Address | Series | 30-day sustained |
|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 149 observations, `40 600 → 50 500` | **+330 ★/day** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 24 observations, `39 700 → 41 800` | +72 ★/day |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 133 observations, `265 → 274` | +0.3 ★/day |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 **0 observations** | — |

The last row is `Gap 550-C`: that address is documented on this base and its
counter has **never** been published inside a table that declares a Stars
column, so it has no series and no staleness check. Prose-only counters are
invisible to every instrument that reads tables.
