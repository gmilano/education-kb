# `p151-election-surface` — `ACTION FO`: the `-only` / `-or-later` election

🔴 **REFUTED exactly as specified.** **7 of 7** GNU-family rows state **no election
anywhere** outside the licence body.

| measurement | value |
|---|---|
| subjects | **7** (5 GPL-family + 2 AGPL-3.0) |
| source files scanned (licence files excluded at any depth) | **1 513** |
| per-file `or (at your option) any later version` headers | 🔴 **0** |
| per-file `… version N … only` statements | 🔴 **0** |
| `SPDX-License-Identifier` lines carrying an election | 🔴 **0** |
| verdict | 🔴 **`SILENT`, 7 of 7** |
| 🟢 **positive control** — the same matcher over the licence BODIES | 🟢 **fires 7 of 7** |

## 🆕 `T81` — the election is inside the licence that is being interrogated

🔴 **Every GNU licence file contains the election.** GPL-3.0's appendix, *"How to Apply
These Terms to Your New Programs"*, reads *"either version 3 of the License, or (at your
option) any later version"*. 🔴 **So a body search for the election returns `OR_LATER` for
every verbatim GNU file — including one whose author elected `-only`.** That is `T77`'s
class one layer down: a phrase correct as a phrase and wrong as a test, because it occurs
inside the text it is meant to interrogate. The module therefore excludes licence files
from its walk at any depth, and proves the exclusion matters by running the same matcher
over them as its control.

## 🔴 Two instrument defects the fixtures caught BEFORE the sweep was published

1. 🔴 **A comment prefix breaks the match.** A real GNU notice is wrapped in a block
   comment, so the two halves of the phrase are separated by `"\n * "`, which `\s*` does
   not cross. The first version of this module read an authored `OR_LATER` fixture as
   `SILENT`. 🟢 `normalise()` strips comment markers and collapses whitespace before any
   matcher runs. **Without this fix the 1 513-file sweep would have published a false
   null.**
2. 🔴 **`license.svg` is not a licence.** `edwyj/ddl-killer` ships a badge image at
   `docs/assets/readme/license.svg`; an open extension suffix counted it, and the control
   reported *"7 of 8"* — one of the eight was a picture. 🟢 The extension list is closed.

🔵 **What this changes in a room.** For all seven rows the election is unstated, so a
downstream relicensor cannot rely on *"or later"*. 🟢 **`P38` step 4 now says the election
is UNSTATED on this shelf** rather than implying it is readable.

- instrument: [`election.py`](election.py) · **24 tests**, all offline, authored fixtures
- result: [`result.2026-10-12-p151.tsv`](result.2026-10-12-p151.tsv) ·
  [`summary.2026-10-12-p151.txt`](summary.2026-10-12-p151.txt)

```
python3 test_election.py
python3 election.py /tmp/edu-trees <subject> [<subject> …]
```
