---
industry: education
region: Global
updated: 2026-10-12
---

# `p145-origin-bots` — `ACTION DW`: REFUTED. The contamination is real and changes nothing

🔴 **`ACTION DW` DISCHARGED and REFUTED.** 🟢 **0 of 44 rows change their dominant offset
when robots are stripped**, so `P144-P`'s contamination finding is a real defect with **no
consequence for any published placement** — which is the outcome the pre-registration said
should be recorded as a caveat rather than fixed.

🔴 **And `P144-P`'s own figure does not reproduce.**

## What was registered

> 🟡 **`ACTION DW`** — strip bots from `p142-origin-at-scale` and re-run the 44-row census.
> `P144-P` shows 9 rows contaminated and one at 32.4%. Re-run `origin_scale.py` with the
> bot filter `author_window.py` already uses, and record which rows change
> `dominant_offset` or region.
> 🔴 *Refuted if no row changes its region* — which would make bot contamination a real
> defect with no consequence, and it should be recorded as a caveat rather than fixed.

## 🟢 Result: nothing moves

| | |
|---|---|
| rows measured | **44** |
| rows with any robot commit | **7** |
| 🟢 **rows whose dominant offset changes when robots are stripped** | 🟢 **0** |
| 🟢 **rows whose region changes** | 🟢 **0** |

🔵 **The mechanism is that robots are a minority everywhere they appear except one row, and
on that row they do not win the mode either.** `nitsuah/bb-mcp` is **32.4% robot (78 of
241)** — reproducing `P144-P`'s headline figure exactly — and its dominant offset is the
same with and without them.

## 🔴 The correction: `P144-P` said 9 rows and 123 commits; the reproducible figure is 7 and 120

| row | robot commits | share |
|---|---|---|
| `nitsuah/bb-mcp` | **78** of 241 | 🔴 **32.4%** |
| `BetterSEQTA/BetterSEQTA-Plus` | 22 of 2255 | 1.0% |
| `alejooroncoy/campus-cli` | 11 of 582 | 1.9% |
| `BetterSEQTA/DesQTA` | 5 | — |
| `oliverhruby/edupage-mcp` | 2 of 111 | 1.8% |
| `krzysztofbury/librus-mcp` | 1 | — |
| `trindadetiago/sigaa-caiu` | 1 of 42 | 2.4% |
| **total** | 🔴 **120** | **7 rows** |

🔴 **Widening the pattern does not recover the missing two.** Adding `renovate`,
`actions-user`, `semantic-release` and `noreply@github.com` to `author_window.py`'s list
returns **the same 7 rows and the same 120 commits**. Counting committer identity as well
as author identity gives **126** commits across the same 7 rows.

🔵 **So `P144-P`'s "9 of 44 rows, 123 commits" is revised to 7 rows and 120 commits**, and
the revision is published because the sub-claim it was built on — `bb-mcp` at 32.4%, and
`dependabot` committing there at both `+0000` and `-0400` — reproduces exactly. 🟢 **The
aggregate was wrong; the finding inside it was right.**

## What this means for `P23` and the placement channel

🟢 **`P23`'s DST discriminator does not need a bot filter to be correct**, on this
population. 🔴 **It still needs one to be *sound***: a row that was 90% robot would place a
CI runner's timezone as a vendor's jurisdiction, and nothing in the current instrument
would say so. 🟢 **`origin_bots.py` reports `BOT_ONLY` for exactly that case** and no row
triggers it today.

🔵 **This is the honest shape of the result: a guard that fires on nothing is still worth
having, and saying "it fired on nothing" is the finding.**

## Limits

- 🟡 **Author identity only** in the headline figure; the committer-inclusive count is
  stated above rather than substituted, because `p142` mixed the two and the difference
  (120 vs 126) is smaller than the discrepancy being explained.
- 🔴 **An offset is not a region.** `AMBIGUOUS` carries `p142`'s own reasoning forward:
  `-0300`, `-0400`, `+0000` and `+0100` each span more than one region and place nothing on
  their own.

## Run it

```
python3 origin_bots.py "<subject>=<clone-path>" …
```

Results: [`result.2026-10-12-p145.tsv`](result.2026-10-12-p145.tsv).
