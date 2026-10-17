# `pass261-current-state-tier-run` — `ACTION ZD` + `ACTION ZE`

Two ACTIONs in one instrument, because the second cannot be measured without the first.

| ACTION | asked for | outcome at `p261` |
|---|---|---|
| **`ZD`** | a CURRENT-STATE row harvester — a row's state is what the newest section says, not every historical mention | 🟢 **DISCHARGED.** `183` rows by `p260`'s whole-file method, `131` by this one, `52` already answered — **`28.4 %`**, above the `20 %` falsifier |
| **`ZE`** *(`p260`'s highest priority)* | run the ladder's EXISTING tiers over every grantless carried row and record `tier_coverage()` per `(path, row)` | 🟢 **DISCHARGED, NOT REFUTED.** `27` rows resolved *(falsifier: `< 20`)*, `84` of `84` in-tree cells `RUN`, `0` `NOT-RUN` |

## Files

| file | what it is |
|---|---|
| `current_state.py` | the predicates: the shelf index, the `(path, row)` coverage matrix, the three ecosystem vocabularies, the scoped reservation guard. **Offline.** |
| `tier_run.py` | the online sweep: `ls-remote --symref` → blobless tree → one payload fetch per in-tree ladder path. **Not in `make hooks`.** |
| `test_current_state.py` | `166` controls. **In `make hooks`.** Run from this directory. |
| `fixtures-p261/` | nine payloads read first-hand at `p261` on resolved refs. Nothing hand-typed. |

## What this module refuses to do

- **Hold its own copy of the ladder.** `ladder_tiers()` parses `p229-grant-ladder-reach/ladder.sh` at call time, because `p229`'s own header says *a probe list copied is a probe list forked*. A control asserts no second copy exists in this file.
- **Classify a licence payload.** `family_of()` shells out to `lib/license_family.sh`, the shared classifier (P237), and reports `CLASSIFIER-UNAVAILABLE` when it cannot be sourced — which is a different measurement from a classifier that ran and said nothing.
- **Guess.** `controlled_vocabulary()` recognises only documented ecosystem vocabularies and answers `None` outside them, because the next pass cannot tell a guess from a read.

## The four findings it exists to make unrepresentable

1. 🔴 **A payload is not one grant.** `reservation_verdict_scoped()` keys on `(payload, section)`. `nextSIS`'s `All rights reserved.` is EllisLab's, `700` lines below nextSIS's own `GPL-3.0`, and `p260`'s payload-wide guard retracted a correct cell.
2. 🔴 **"NOT SPDX" is not "prose".** `controlled_vocabulary()` reads npm's `SEE LICENSE IN`, PyPI's trove classifiers and CRAN's `License:` grammar. `3` of `11` declarations this pass were specified values reported as unreadable.
3. 🔴 **Tier A can hold a parameter sheet.** `cran_parameter_sheet()` refuses to grade `sonsoleslp/tna`'s `46`-byte `YEAR:` / `COPYRIGHT HOLDER:` file as a licence.
4. 🔴 **Three `P###` namespaces live in these headings** — pass numbers, pattern ids, finding ids. `PASS_IN_HEADING` requires the word `Pass`; a loose reader reported `7` of `8` shelves out of order.

## Mutation run

`17` mutants, all caught — **after two of them were not**. `M4` (`>` → `>=` in `already_answered`) and `M17` (the slug segment-count guard removed) both left `164` controls green. `M4` earned two controls for a correction written *beside* the thing corrected. `M17` showed the guard was unreachable code — neither capture class in `SLUG_RX` can match a `/` — so it is deleted and the real mechanism is pinned instead.

## Usage

```sh
cd compose/code/pass261-current-state-tier-run && python3 test_current_state.py   # 166 controls
python3 tier_run.py <population-file> <out.tsv>                                   # online
```
