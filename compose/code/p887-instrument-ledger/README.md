# `p887-instrument-ledger` — `886-G5`'s acceptance test: diff what the INSTRUMENTS know against what the SHELVES say

## The case that opened it

`verticals/solutions.md` published `OS4ED/openSIS-Classic` as *"GPL per README; no licence file"* and
*"treat as all rights reserved"*. Its grant is **GPL-2.0, 17,286 B, at `master/docs/License.txt`** —
and the refutation was already committed here, in
`compose/code/pass275-grant-enumeration/enumeration_gate.py`'s own docstring, for roughly **611
passes**, while three live shelves published the false absence.

🔵 `gate-enumeration` was built on that row and **passes**. `gate-absence` **passes**. Both read the
shelves; **neither reads the instrument docstrings, which is where the answer lived.**

🔴 `p886` corrected the one row it found by accident and did not build the ledger, so **the size of
this class was UNKNOWN**. This measures it.

## The answer

```
raw (slug, family) mentions   699
  CLAIM        266      assertions about the world
  CORRECTION    72      records of a PAST error: refuted value beside the true one
  ENUMERATION  109      a candidate-family list, not a verdict
  FIXTURE      208      an instrument's own test data
  SNAPSHOT      44      a COPY of a shelf, kept for diffing
distinct instrument CLAIMS    206
AGREE                          24
DISAGREE                        1   <- the whole class
SLUG-NOT-ON-ANY-SHELF         181   <- registered as 887-G5
```

🟢 **The one finding is real:** `jupyterhub/jupyterhub` — `p314-untitled-payload-arm/README.md:12`
has recorded `BSD-3-Clause` since `p314`; `repos/foundations.md:533` published bare `BSD`; the
metadata channel returned `BSD-3-Clause` independently at `p887`. **Corrected.**

## 🔴 The first run reported `70` and `69` were false

`886-G5`'s acceptance test says *"names an `owner/repo` AND a grant verdict"* and **does not say what
binds the two**. The binding is the whole instrument. Four classes, each now a control:

| # | Defect | The case that showed it |
|---|---|---|
| 1 | **A markdown table row is a self-contained record** | a ±3-line window over `p441-tree-licence-enumeration/README.md`'s four-row table attributed **five** families to `openedx/XBlock`; its own row says `Apache-2.0` and agrees with the shelf |
| 2 | **A shelf SNAPSHOT is not instrument knowledge** | `p119-carried-column-audit/current/*.current.md` are copies of shelves, kept so that audit can diff them |
| 3 | **A family ENUMERATION is not a verdict** | a classifier's family table names eight families in six lines |
| 4 | 🔵 **A CORRECTION TABLE publishes the refuted family beside the true one** | `openedx/edx-ora2` (*"published 🟢 Apache-2.0 \| 🔴 actually AGPL-3.0"*), `openfun/ralph`, `portabilis/i-educar` — **shelf right on all three** |

🔵 **An instrument that RECORDS a past error is indistinguishable, to a token scan, from one that
ASSERTS it — and this base is full of the former by design.** `CORRECTION` scopes are therefore
**excluded rather than resolved by guessing which cell is the truth**: picking "the last family in
the row" would have worked on all three above and is still a guess (`886-G4`'s rule).

## `886-G3` compliance

Slugs come from `lib/slug_extract.py`, the tested helper — never from an inline
`grep -oE 'github\.com/<a>/<b>'`. That is the whole point of `886-G3`.

## Run

```
python3 test_ledger.py                       # 22 offline controls
python3 -I ledger.py --root ../../.. \
        --out ../../../evidence/instrument-ledger-886G5.2026-11-18-p887.tsv
```

Offline. No network.
