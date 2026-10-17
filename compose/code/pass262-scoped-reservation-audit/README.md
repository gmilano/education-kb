# `pass262-scoped-reservation-audit` — `ACTION ZI`

`ACTION ZI` (`p261`): *"Re-run `p260`'s `reservation_verdict()` over every payload this base
has ever graded as `RESERVED` or proprietary, with the SCOPED guard."*
**Falsified if no published retraction turns out to be third-party — in which case `nextSIS`
is one repository's aggregate and not a class.**

🟢 **DISCHARGED, NOT REFUTED.** It is a class. The second member was found on the first
sweep — and `p261`'s scoped guard **cannot see it**, because it is not an aggregate.

| | |
|---|---|
| cells harvested across `9` shelves | `87` |
| ├─ `RESTRICTIVE-GRADE` *(the population)* | `73` cells · **`39` distinct slugs** |
| ├─ `SCOPE-NOTE` *(cell leads with a usable family)* | `11` |
| └─ `QUOTED-CLAIM` *(a claim under test, not a verdict)* | `3` |
| payloads read first-hand on `ls-remote`-resolved refs | **`71`** |
| `NO-REF` · `NO-TREE` · `NO-PAYLOAD` · `FETCH-FAIL` | `0` · `0` · `0` · `0` — **coverage `100 %`** |
| verdicts changed against `p261`'s guard | 🟢 **`2`** |

## The two changed cells

| row | `p261` | `p262` | why |
|---|---|---|---|
| 🔴 [`sdv-dev/SDV`](https://github.com/sdv-dev/SDV) | `RESERVED` | 🟢 **`STEWARD-RESERVATION`** | the `All Rights Reserved` on line `34` of its `4 818` B `LICENSE` is **MariaDB Corporation Ab's** — *"License text copyright (c) 2017 MariaDB Corporation Ab, All Rights Reserved."* — the **steward of the BUSL form**, reserving rights in the DOCUMENT. DataCebo is the Licensor and is nowhere in that sentence |
| 🔴 [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | `RESERVED` | 🟢 **`CONDITIONAL-GRANT`** | it reserves on line `3` and then **grants** on line `5`: *"Permission to use, copy, modify, and distribute this software … is hereby granted"* — the **X11/academic variant**, which omits MIT's *"free of charge"* because the consideration is a field of use, not a fee |

## The three findings

### 1. 🔴 `nextSIS` is a class, and the scoped guard is keyed on the wrong thing

`p261` fixed the aggregate case by keying on `(payload, SECTION)`. A **steward notice is a
SENTENCE, not a SECTION** — `aggregate_sections()` returns `[]` for the BUSL payload, so
`subject_span()` returns the whole file and there is no span to scope to. 🔵 The verdict
`p261` published for `SDV` was **right** (BUSL-1.1 is not OSI) **from an unsound method** —
`p260`'s own named failure, third occurrence.

🔴 **And the notice is in every copy of the form**, including permissively-licensed projects
that merely vendor a BUSL dependency's text. The next false retraction of this class is a
matter of which payload arrives first.

### 2. 🔴 A grant test made of two literal phrases calls a real grant a refusal

`p261`'s permissive test is BSD's *"Redistribution and use in source and binary forms"* and
MIT's *"Permission is hereby granted, free of charge"*. Neither matches X11 or ISC.
🔵 `p257` already found *the grant classifier cannot tell `Apache-2.0` from a non-commercial
academic licence*; this is the same family one layer in. `CONDITIONAL-GRANT` keeps the two
questions apart — **there IS a grant** and **a studio may NOT ship it** are both true of
`dssg/student-early-warning`, and a single `RESERVED` says the first one wrongly.

### 3. 🔴 A row's state is not what the row QUOTES — and this was nearly a published regression

`intel/trends.md` l.`575` carries `BUSL-1.1, "source-available, not OSI"` for
[`twentyhq/twenty`](https://github.com/twentyhq/twenty) — **inside a column headed *"what the
secondary source said"***, beside the payload reading that refutes it. **`p249` already
corrected that row to `AGPL-3.0`.** This pass's first-cut harvester read the cell as a live
verdict; publishing it would have **re-asserted a claim this base refuted thirteen passes
ago**.

🔵 `ZD` taught that a row's state is what the NEWEST section says. **`p262`: it is also not
what the row QUOTES**, and the discriminator is the COLUMN HEADER, which costs one lookup.

🔴 Confirmed independently this pass: `twentyhq/twenty`'s `39 965` B `LICENSE` is AGPLv3 plus
an AGPLv3 §7 additional permission, with `/* @license Enterprise */` files under a commercial
licence and several `MIT` subpackages. **`0` occurrences of `"Business Source"` in the whole
tree.**

## Three things this module got wrong before it got them right

🔴 **Characters are not bytes.** The first sweep reported `len(payload.decode())` and
disagreed with two correct shelf cells by `4` B and `2 146` B. **The shelves were right.**
Across the full run **`43` of `71` payloads — `60.6 %` — carry a non-zero delta**, so this
was never a two-cell problem: it would have mis-stated most sizes this pass published.
🔵 `p261`'s *disbelieve the instrument before disbelieving the shelves*, applied to an
instrument written in the same hour.

🔴 **`CC-BY` is a prefix of `CC-BY-NC-SA`.** The first harvester filed
`anaistack/cefr-asag-corpus`'s non-commercial content licence as usable. The CC axes belong
to [`pass258-content-licence-family`](../pass258-content-licence-family/) and are now asked,
never re-implemented — a control asserts this module holds no second copy.

🔴 **`Unlicense` is a prefix of `unlicensed`, and they are OPPOSITES.** One dedicates to the
public domain; the other means there is no grant at all. The family matcher dropped
`barneslardo/sis-demo` and four others out of the population entirely. 🔵 Same shape as
[`p251-prefix-collision`](../p251-prefix-collision/)'s `maia` class and `p261`'s heading
namespaces — **third occurrence, first one in licence names**, and the remedy is the same:
match the whole token.

## Files

| file | what it is |
|---|---|
| `reservation_audit.py` | the predicates: byte accounting, the steward notice, the widened permissive test, `cell_role()` / `grade_class()`. **Offline.** |
| `sweep.py` | the online half: `ls-remote` → blobless tree → one fetch per in-tree ladder path → both guards → the delta. **Not in `make hooks`.** |
| `test_reservation_audit.py` | `63` controls. **In `make hooks`.** Run from this directory. |
| `fixtures-p262/` | nine payloads fetched first-hand at `p262` on resolved refs. Nothing hand-typed. |

## Mutation run

`20` mutants, `20` caught — **after one was not**. `M19` removed `harvest()`'s header reset
and all `56` controls stayed green, which meant the thing that stops one table's claim header
reaching a later table's rows was **unverified**. 🔵 The failure direction is the dangerous
one: a stale claim header does not add a false grade, it **silences a real one**.
`HeaderDoesNotLeakAcrossTables` pins it in three directions, including that the reset must
**not** fire between rows of the same table.

## Usage

```sh
cd compose/code/pass262-scoped-reservation-audit && python3 test_reservation_audit.py  # 63
python3 sweep.py <repo-root> <out.tsv>                                                 # online
```
