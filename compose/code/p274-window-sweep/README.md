---
industry: education
region: Global
updated: 2026-10-17
---

# `p274-window-sweep` — a threshold is a filter on which cells get checked, and the defects were under the filter

> New in **pass 274 of `2026-10-17`**. Discharges `p273`'s backlog item 1 (*"read `market.md`
> top-to-bottom as a reader"*) on the arithmetic side, and applies `p272`'s own amendment — *"a 10%
> mismatch is not automatically noise; test the window before writing it off"* — **to `p272`'s own
> ledger**, which marked four such mismatches `ok` without running it.

## What it measures

For every market cell on these shelves: does `baseline × (1 + CAGR)^span` reach the published horizon?

```
PASS        |projected/published − 1| ≤ 1 %  at the labelled span
ROUNDING    ≤ 2 %                            publishers print baselines to 2–3 s.f.
WINDOW_FIX  closes at span ± 1 year          → a YEAR LABEL on the row is wrong
SPLICE      closes at neither                → TWO REPORT VINTAGES, never publish as a series
```

It also prints, per cell, the 2026 point read **forward from the printed base** and **backward from the
horizon**. 🔵 **Where those two disagree, a published "2026 market size" is not one number** — which is
how Grand View's LATAM 2026 point turns out to be both `$455M` and `$490M`.

## Run it

```sh
python3 -I compose/code/p274-window-sweep/window_sweep.py
```

No network, no searches, no arguments. Ledger committed as
[`evidence/arithmetic-sweep.2026-10-17-p274.tsv`](../../../evidence/arithmetic-sweep.2026-10-17-p274.tsv).

## Result: 28 cells — `PASS 14` · `ROUNDING 2` · `WINDOW_FIX 3` · `SPLICE 9`

| finding | detail |
|---|---|
| 🔴 **Two M&M cells were never swept and both are one-year-mislabelled** | NA `$951M → $2.3B @ 15.9%` closes at **+0.22 %** across six years (−13.53 % as labelled); LATAM `$105.6M → $204.7M @ 11.7%` at **+0.20 %** (−10.30 % as labelled). 🔵 **So the window defect is a property of this LITERATURE, not of Grand View** — `T38` is too narrow |
| 🔴 **The GLOBAL headline cell has the house signature too** | `$8.3B (2025) → $57.2B (2033) @ 25.9%` → **−8.40 %**, beside NA's **−9.07 %** and APAC's **−9.12 %**. Three databooks, one house, a 0.7-point band |
| 🔴 **Nine cells are SPLICES** | Including LATAM Grand View (−7.12 %), which `T32` had filed as *"window rounding 🟢"* |
| 🟢 **MarketDataForecast is the only regional cell that closes AS LABELLED** | −0.13 % over nine years, −0.18 % on its own 2026 point. And it **cannot** be reproduced from Grand View's curve (GVR's 2025 Europe point is `$2 005M` against MDF's `$1 590M`, −21 %) — which discharges `p273`'s backlog item 2 |

## The method note that matters more than any cell

⚠️ **Sign conventions.** `p272`'s ledger reports `published / projected − 1`; this one reports
`projected / published − 1`. **The same LATAM cell reads `+11.5 %` there and `−10.3 %` here.** A single
*"10 % threshold"* compared across the two conventions was never comparing anything, and every ledger on
this base now states its convention in its header.

🟢 **Retire the threshold.** `p271` set *">25 % flag, >50 % investigate"*. **Not one of the five
established window defects would have fired it** — because a one-year offset on a 25–32 % CAGR produces a
mismatch of roughly `CAGR ÷ span`, i.e. **8–14 %**, which is exactly the band that was defined as noise.
**The threshold was tuned to exclude the defect's own signature.** A window test is one multiplication:
run it on every cell and classify by **mechanism**, not by size. See `T42`.
