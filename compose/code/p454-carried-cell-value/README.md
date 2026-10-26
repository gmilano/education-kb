# `p454-carried-cell-value` — the licence VALUE sweep, and the reader it needed

`Gap 453-A` named this pass's cheapest closure: the **71 carried registry-sourced
licence cells** had been swept by `p452` for **address** (63/71 `AGREE`, 0 `DISAGREE`)
and never for **value**.

## What it found

`value_sweep.py` over all 71 cells
(`evidence/carried-cell-licence-value.2026-10-26-p454.tsv`):

| verdict | n | share |
|---|---|---|
| `AGREE` | 41 | 57.7 % |
| `MANIFEST_ONLY` | 10 | 14.1 % |
| `NO_ADDRESS` | 8 | 11.3 % |
| `REGISTRY_SILENT` | 5 | 7.0 % |
| `DISAGREE` | 3 | 4.2 % |
| `NO_GRANT_ANYWHERE` | 2 | 2.8 % |
| `COMPOSITE` | 2 | 2.8 % |

**The first run said 6 `DISAGREE` (8.5 %) and three were the reader's.** 4.2 % is
indistinguishable from `p453`'s 3.0 % on novel packages (3/71 vs 5/166), which refutes
the premise that curated cells are cleaner.

`MANIFEST_ONLY` then split **8 `ADDRESS_DEAD` / 4 `REPO_LIVE_NO_GRANT`** when re-probed
on non-licence paths (`Gap 454-H`), so the honest decay figure is **16 of 71 (22.5 %)
cells pointing at nothing readable**.

## Files

| file | what it is |
|---|---|
| `value_sweep.py` | the sweep. Forge-aware (gitlab ≠ raw.githubusercontent), gates every read on `%{http_code}`, follows an in-repo pointer one hop |
| `family_title.py` | the licence-family reader. **Title-block anchored**, with `NOT-OSI`, `COMPOSITE` and `POINTER_IN_REPO` classes |
| `family_delta.py` | measures the carried reader against this one over 179 payloads → `evidence/family-reader-delta.2026-10-26-p454.tsv` |
| `controls.py` | 31 controls for the sweep, both directions; 8 assert payload digests earlier passes published |
| `family_controls.py` | 23 controls for the reader, both directions, one per defect below |
| `verify_contracts.py` | the shelf contracts re-implemented from the gate sources, because `make hooks` is denied |

## The four reader defects, each with its control

1. **Inherited (`Gap 454-A`).** `p450`'s remedy for `Gap 450-C` (a) truncates to the
   first 40 non-empty lines so GPLv3's closing LGPL recommendation falls outside it.
   **GPLv2's PREAMBLE recommends the LGPL at non-empty line 15** — inside the window.
   The window fixes GPLv3 and breaks GPLv2. Cost: 1 of 179 (`oat-sa/tao-core`).
2. **Composite by heading count.** Graded `nakafaai/aksara`'s 15 numbered sections as a
   composite, and lost `bncc-dev/bncc-pacotes`'s MIT half. A composite is **two or more
   distinct families named**.
3. **`all rights reserved` as evidence of closure.** It is the opening line of
   `davepacheco/node-extsprintf`'s **MIT** payload. The first cut would have condemned a
   permissive dependency.
4. **A pointer read as a refusal.** `ckeditor/ckeditor5` serves a 170 B root `LICENSE.md`
   naming `packages/ckeditor5/LICENSE.md`; the repo really does serve a 17 983 B
   `COPYING.GPL`. A pointer is an **absence** of a grant here, never a refusal.

`Gap 454-I` records a fifth defect, in `verify_contracts.py`'s own header-row control:
it flagged legitimate data rows of **transposed** tables. Fixed by walking back to the
nearest separator row.

## Known limits

- **`Gap 454-C`** — `canon()` collapses GPL **versions**, so `edu-sharing/Edu-Sharing`
  (npm `GNU GPL v2`, payload **GPL-3.0**) grades `AGREE` although the two are
  incompatible. The 4.2 % is a family-level floor.
- **`Gap 453-C`** — no ecosystem routing to R's `DESCRIPTION`; the 71-cell population
  contains no CRAN address, so there was nothing to route.
- Nothing here is gate-attested: `make hooks` was **DENIED** (`Code from External`) for
  the ninth time in ten passes.

## Running it

    cd compose/code/p454-carried-cell-value
    python3 -I controls.py          # 31 controls, both directions
    python3 -I family_controls.py   # 23 controls, one per defect
    python3 -I value_sweep.py       # the sweep
    python3 -I family_delta.py      # the reader delta
    python3 -I verify_contracts.py  # shelf contracts
