# `p920` — the cell-level licence divergence sweep

Discharges `919-G3`. Controls `919-G9`. Instrument: [`ingest/p920-cell-divergence.py`](../../../ingest/p920-cell-divergence.py).

## What it is for

`919-F1` swept for duplicate **rows** and found none — 786 row-subjects across the five delivery
files, zero subjects appearing twice in one table. The live class is one table away: **the same
repository carried in two tables with licence CELLS that disagree.** `919-F2` is the instance.

## 🔴 Why `919-G3`'s specification does not work, and what replaced it

`919-G3` prescribed comparing the licence **token set** per cell. Built to that specification and
run against the real pre-fix tree, **it does not fire on its own fixture**:

```
verticals/solutions.md:141  {AGPL-3.0, MIT, PROPRIETARY}   "AGPL-3.0 CE + proprietary EE. NOT MIT"
verticals/solutions.md:193  {AGPL-3.0, MIT, PROPRIETARY}   "NOT MIT. MIT + AGPL-3.0 conjunction..."
```

Both cells contain the token `MIT` — one **asserts** it, the other **negates** it. 🔵 So
`919-G9`'s diagnosis ("the gate compares tokens, and both cells contained `AGPL-3.0`") was one level
too shallow: **no bag-of-tokens comparison can represent polarity**, and the prescribed correction
inherits the defect it was written to fix.

Two arms replace it:

| Arm | Compares | Status |
|---|---|---|
| **SET** | the **polarity-tagged** token set — `¬MIT` is a different token from `MIT` | 🔴 **a gate.** Adjudicate against a fresh byte-read and fix |
| SEQUENCE | the polarity-tagged token **sequence**, with multiplicity and order | 🟡 **a measurement, never a failure.** Two cells stating the same grant at different lengths always differ here |

Measured on the live shelf at `p920`: SET **2 hits, 2 true (2/2)**; SEQUENCE **2 hits, 0 true
(0/2)**. After the two corrections the SET arm is **empty** across all 450 address-bearing rows and
both fixed subjects fall to the sequence arm.

## Rules inherited from this base's own history

- **`918-G4` / `919-F1`** — a row's SUBJECT is the **first** repository address in the row. A slug
  the row merely *talks about* is not the subject.
- **`920-F2`** — the licence cell is the **leftmost** cell carrying a licence token, **not the
  densest**. Picking the densest hands you `Submitty`'s prose cell, which names `Apache-2.0` only to
  contrast it with Autolab, over its actual `BSD-3-Clause` cell one column to the left. This defect
  was in the first run of this instrument and was caught by the fixture, not by review.
- **`919-G4`** — no token in `VOCAB` matches on the bare word `noncommercial`, so this instrument
  cannot reproduce `918-G0`'s false positive on stock GPL/AGPL §6(c).

## Offline control

```
python3 -I ingest/p920-cell-divergence.py --selftest
```

The fixture is `fixtures/verticals-solutions.p918.md` — `verticals/solutions.md` at commit
`8bc72dd` (`p918`), the last tree in which the PrairieLearn divergence was live. **It exits
non-zero if the control does not fire**, which is what `919-G9` asked for. On that file it raises
exactly one subject out of 99 address-bearing rows.

## Live run

```
python3 -I ingest/p920-cell-divergence.py agents/top.md repos/foundations.md verticals/solutions.md
```

Exit 1 if any subject diverges. 🔵 Read the arm before acting: only **SET** is a failure.
