# `p448-pin-recency-calibration` — the instrument that corrected `Pattern AZ`

`Gap 447-C` registered that `Pattern AZ` (`p447`) was built on **n = 5** — one pinning per
repository, i.e. one coin flip each — and asked for the rule to be run over the shelved
population before being treated as calibrated. This is that run: **496 observations across 36
repositories**, and it refutes two of `AZ`'s three published claims plus the sign of the third.

## Why a retrospective simulation, and not a 24-hour wait

A pinning experiment appears to need two observations 24 h apart. It does not. Every repository
already contains the answer for every past moment, so one blobless clone yields fourteen
observations:

```bash
PIN=$(git -C repo rev-list -1 --before="$T" HEAD)          # what HEAD was at time T
NXT=$(git -C repo rev-list -1 --before="$T +1 day" HEAD)   # what HEAD was 24h later
AGE=$(git -C repo show -s --format=%cI "$PIN")             # how old was that commit when pinned
[ "$PIN" = "$NXT" ] && echo HELD || echo STALE
```

`--filter=blob:none --no-checkout` fetches the commit graph without file contents: ~1 s per
repository, **no GitHub API** (403 on this host class).

## Pre-condition, checked rather than assumed

The method requires committer dates to be monotone along history, or `rev-list --before` does
not reconstruct the historical HEAD. Measured over **9 438** adjacent commit pairs in the 36
repositories: **0 inversions, 36 of 36 clean**.

## Validation before use

`Apomera/AlloFlow`'s two refs date to `2026-10-24T12:35:30-04:00` and
`2026-10-25T18:50:44-04:00`, reproducing `p447`'s published *"pinned 10-24 12:35, HEAD 10-25
18:50"* to the minute.

## Result

| age of commit at pin time | n | P(pin still HEAD after 24 h) |
|---|---|---|
| < 1 h | 33 | 6.1 % |
| 1–6 h | 35 | 20.0 % |
| 6–24 h | 99 | 35.4 % |
| 1–3 d | 81 | 71.6 % |
| 3–7 d | 59 | 81.4 % |
| 7–30 d | 100 | **98.0 %** |
| > 30 d | 89 | 96.6 % |

Operating point: **age ≥ 7 d → 97.4 %** (n = 189) against **48.9 %** below 7 d (n = 307).
Base rate: **67.3 %** of pins survive 24 h — not the 94 % `Pattern AZ` published from an
already-survived sample.

Commit volume, which `AZ` declared refuted: **Spearman ρ = +0.886** against stale rate (n = 36
repositories). It is a *good* predictor. `AZ` read noise from one pin per repository as signal.
Volume vs mean age-at-pin is **ρ = −0.852** — volume proxies recency, so use recency.

## Files

| file | what it does |
|---|---|
| `pin_recency_calibration.py` | walks a directory of blobless clones, emits one JSON row per (repo, offset) observation |
| `analyse_calibration.py` | buckets by age-at-pin, scores `AZ`'s 24-h rule as a classifier, per-repo stale rates |
| `mcp_capability_census.py` | extracts MCP tool declarations from a tree and classifies read/write (`Gap 447-B`) |
| `read_only_hint_census.py` | counts self-declared `read_only_hint` per tool (`Gap 448-B`) |
| `population.txt` | the 36 shelved slugs sampled |

Raw data: `evidence/pin-recency-calibration.2026-10-26-p448.tsv` (496 rows),
`evidence/mcp-capability-census.2026-10-26-p448.tsv`.

## Known limits

- **`Gap 448-D`**: 36 repositories, one industry, one host, one 14-day window, 24-h horizon only.
  Nothing here calibrates a 1-week or 1-quarter pin.
- **`Gap 448-C`**: `mcp_capability_census.py` is regex over tool registries, not an AST walk. It
  over-counts `bruchris/canvas-lms-mcp` (222 vs a README-advertised 187) and needed three fixes
  before it saw three registration idioms — bare `@mcp.tool`, nested-paren decorator arguments,
  and a Go codebase. Every miss failed toward *"no write tools"* (`Trend 48`), so the 32.9 %
  write share is a **lower bound**.
