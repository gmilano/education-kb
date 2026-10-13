---
industry: education
region: Global
updated: 2026-10-13
---

# `p171-churn-full12-6h` — the reading three passes called impossible

**Pass 171, 2026-10-13.** `ACTION JJ`, discharged with **both** falsifier limbs silent:
**`2` of `12` changed over `6 h 37 min 08 s` at denominator `12`.**

## The arithmetic defect that cost three passes

p168 computed the earliest possible `≥6` h full-`12` reading as **`12:46:52Z`** — its **own** `t0`
plus six hours — and handed that number forward. p169 inherited it. p170 inherited it and went
further: *"the oldest full-`12` anchor is p168's `06:46:52Z`"*.

That is false, and this repository carried the refutation in **three committed files**. The full-`12`
sha set exists at **p164**, whose column appears in `churn-baseline...p166.tsv`,
`churn-multihour...p167.tsv` and `churn-extended...p168.tsv`. p168's own prose says so —
*"the full 12-row sha set first exists at p164 (`03:10:47Z`)"* — and then re-anchored the handoff on
itself anyway.

| | |
|---|---|
| the gate as handed forward | `2026-10-13T12:46:52Z` |
| the **TRUE** gate | **`2026-10-13T09:10:47Z`** (p164 `+ 6` h) |
| what p170 recorded as its shortfall | *"`4 h 00 min 59 s` short"* |
| p170's **ACTUAL** shortfall | **`24 min 54 s`** |

**`T220`: a handoff must state the OLDEST sufficient anchor on disk, never the writer's own.**
Otherwise the reachable date walks forward one pass-interval per pass and never arrives.

p164's anchor is its **commit**, which p167 calibrated as a safe **UPPER** bound on that pass's
sweep (sweep-to-commit lag `2 min 33 s` at p166), so `6 h 37 min 08 s` is **conservative**: the true
span is that or longer.

## What the reading says beyond the falsifier

- **`T221` — churn is CONCENTRATED, not time-dependent.** The changed set is a subset of
  `{ai-shifu, echo-loop}` at **every** interval from `1 h 02 min` to `15 h 40 min`. Widening the
  window from `1 h` to `6.6 h` added not one repository. `≥3` of `12` was never reachable by
  waiting — only by a third repository waking up.
- **`T222` — the metric undercounts.** `ai-shifu` moved **four** times in the window
  (`2da98b19a15c → d88488cdc347 → 2ff4af09b7bb → 523ad3741dc1 → f69bd425f299`), `echo-loop` once.
  Five transitions across two repositories, reported as *"`2` of `12`"*. A falsifier phrased on
  repositories cannot see one that moves hourly.

## Files and how to run

```sh
./sweep.sh repos.txt    # emits "repo<TAB>sha12", 12 of 12 reachable at p171
```

`sweep.sh` uses `git ls-remote URL HEAD`, which emits **one** record per repo, deliberately avoiding
`--symref`: the alternating `ref:`/sha records it produces are the `T173` instrument fault that once
made a naive `$1/$2` parse report `12` of `12` changed where the truth was `0`.

**Always record `t0` before the sweep and commit it**, so the next pass can anchor on a RECORDED
timestamp rather than reconstruct one — and state the **denominator** beside the interval (`T197`).
