---
industry: education
region: Global
updated: 2026-10-16
---

# P235 — the carried-row index: `ACTION UG` and `ACTION UH`, built

**Pass 235 of 2026-10-16** (the FOURTH pass of this date; p232, p233 and p234 all carry it).
Instrument: `carried_index.py`. Controls: `test_carried_index.py` — **23, all offline**, wired into
`make gate-offline`, so this stops being a one-off the way `ACTION QO` stayed one for eleven passes.

## Why this exists

p234's gap list closed with the action it had just earned:

> **`ACTION UG`** *(THE ONE THIS PASS EARNED)*: before publishing any "there is no X" claim, grep
> these shelves for X — the nine-pass LMS error needed no new evidence, only self-reading.
> […] this KB has no index of what it already carries, so every pass re-discovers rows and the
> shelves can argue against their own verified cells for `25` passes at a time.

Two predicates follow from that sentence, and this file is both of them:

| predicate | question it answers | the error it prevents |
|---|---|---|
| `carried(slug)` | is this row already on the shelves? | p234 drafted `20` rows and `9` were duplicates — caught only AFTER the shelves were written |
| `claims(token)` | do the shelves already mention X? | the nine-pass *"no `MIT`/`Apache` LMS"* error, and p235's own headline |

## What it reads, and what it refuses to read

**The ten shelves only.** Not `evidence/`, not `archive/`, not `compose/code/`. Both exclusions are
load-bearing and both are under control in the suite:

- a slug cited in an evidence TSV but absent from the shelves is **not carried** — it is a
  measurement, not a published row;
- a claim in an archived file is **not a live claim**, so `claims()` must not report it.

## `ACTION UH`, discharged

`fold()` lowercases and strips a trailing `.`, `,` or `)` before comparing. That is the whole of
`UH`, and it was not cosmetic: `OpenOLAT/OpenOLAT` vs `openolat/OpenOLAT` is the pair that defeated
p234's cheap duplicate check.

Measured over the shelves at this pass: **`1 965` raw spellings → `1 913` distinct rows**, with
**`51` rows carried under two or more spellings**. Full list in
[`p235-case-collisions`](../../../evidence/p235-case-collisions.2026-10-16-p235.tsv).

🔴 **The index is also how this pass found its own headline.** `claims("i-educar")` returns hits on
**nine of the ten shelves** while `README.md`'s gap list publishes *"LATAM: `0` open-source education
repositories"*. No new evidence was needed to see that — only this predicate.

## Running it

```sh
make index                        # rebuild, report row count + UH collisions
make carried SLUG=owner/repo      # before drafting a row
make claims  TOKEN=i-educar       # before publishing "there is no X"  ← THE GATE
```

`make claims` exits non-zero when the token is already on the shelves: a non-empty answer means
**stop and read those cells**, not "add a caveat".

## What it does NOT do

🔴 It matches **text**, not entities. `claims("LATAM")` cannot tell a Brazilian education platform
from a Brazilian weather API — [`p235-screen-false-positives`](../../../evidence/p235-screen-false-positives.2026-10-16-p235.tsv)
records `17` substring false positives from this pass's own census (`enem` inside `theopenem`, `peru`
inside `eperusteet`, `unb` inside `sunbird`). The index narrows what a pass must read by hand; it
does not replace reading it.

🔴 It indexes `github.com` slugs only. A row that lives on `edugit.org`, GitLab or a Maven
coordinate is invisible to `carried()` — which is `ACTION UA`/`UD` territory, still open.
