# `p221` — `ACTION RH`'s instrument: the unit of a licence is the **VERSION RANGE**

`ACTION RH` was p220's registered **highest-priority action for p221**: run `p220`'s
FILE-level read over every row whose grant was recorded from a root `LICENSE` or a
`README` **only**. Its limb `1` was *"`3`+ further rows come back `FILE-NARROWER` →
repository-level licence metadata is systematically wrong on this shelf"*.

🔴 **It fires limb `2`.** `22` redistribution-shaped rows read first-hand on `2026-10-15`
through `raw.githubusercontent.com`, and **`0`** came back `FILE-NARROWER`. The
`adlnet`/`microsoft` pair p220 found was the SCORM-and-Moodle distribution shape
specifically, not a general defect. p220's own prediction was the wrong one, and the
control that proves it is the `4` Moodle plugins below, which agree with their shelf cell
on family and on version.

🟢 **But the read did not come back empty, and what it found is larger than what was
registered — because `p220`'s instrument could not see it.**

## What `file_vs_repo()` is blind to

`p220`'s comparison maps every GNU variant onto one family, `RECIPROCAL`. So it reports
`AGREE` for every one of these:

| shelf cell | the file that ships says | `p220` says | the truth |
|---|---|---|---|
| `GPL-3.0` | *"either version 3 of the License, or (at your option) any later version"* | `AGREE` | **`GPL-3.0-or-later`** |
| `GPL-2.0` | *"under version 2 of the License (**non-upgradable**)"* | `AGREE` | **`GPL-2.0-only`** |
| `GPL-3.0` | header: *"GPLv2 or later"* · readme: *"GPLv3"* | `AGREE` | **two different grants** |

🔴 **Those are not the same grant.** `GPL-2.0-only` is incompatible with `GPL-3.0`, so a
row published as a bare `GPL-2.0` **cannot be combined with a GPLv3 host** — Moodle, for
one — and the shelf does not say so. `GPL-3.0-or-later` lets a studio move forward to a
future version; a bare `GPL-3.0` does not say whether it may.

So the deciding property is not the licence **family** and not the licence **file**. It is
the licence's **version range** — the `-only` / `-or-later` bound.

## The census

🔴 **`94.3%` of this KB's `2 342` GNU cell-mentions carry no bound**: `2 208` bare against
`134` qualified, across **`337` distinct rows**. Full breakdown in
[`rh-range-census`](../../../evidence/rh-range-census.2026-10-15-p221.tsv).

🟢 **One artefact rejected by the census guard, and it was this pass's own:** `AGPL-6 d` in
`repos/trending.md` l.`13998` is a liveness table's **day count**, not a licence at version
6. The first census counted it. The guard is kept as a test, because the next liveness
table will have more.

## `ACTION QX` lands here

`QX` asked for a **sentence-based** window and p220 recommended folding it into `RH`.
This is where it landed, and it is not a nicety. A GNU notice in a source file is wrapped
to ~80 columns inside a comment block:

```
 * Foundation; either version 3.0 of the License, or (at your option) any later
 * version.
```

🔴 **A line-based reading of `bigbluebutton`'s `MeetingService.java` identifies neither the
bound nor the family** — *"Lesser General Public License"* is on a different line from
*"version 3.0"*, which is on a different line from *"version."*. p221's first fixture was
cut at that wrap and the instrument correctly called it `unspecified`; both the wrapped and
the truncated readings are kept as tests. The file is also CRLF, so `\r` has to go first.

## Results, `22` rows

| state | rows | what it means |
|---|---|---|
| 🟡 `FILE-SILENT` | **8** | the shipped file carries **no notice at all** — `h5p.classes.php` at `196 920` B, `xblock/core.py` at `39 737` B, `fsrs4anki-helper/__init__.py` at `10 799` B. A file lifted out of these repos travels with no grant on it |
| 🔴 `RANGE-UNDERSPECIFIED` | **6** | the file carries a bound and the published cell does not. `1` of the `6` is an outright incompatibility: `oat-sa/lib-lti1p3-core` is **`GPL-2.0-only`** |
| 🟡 `BOTH-UNSPECIFIED` | **3** | bare on **both** sides — the ambiguity is at SOURCE, not a KB defect. `gocodebox/lifterlms` and `celtic-project/LTI-PHP` |
| 🔴 `GRANT-CONFLICT` | **1** | `themeum/tutor`: `tutor.php` **`GPLv2 or later`**, `readme.txt` **`GPLv3`**, `LICENSE` `GPL-3.0`. Three channels, three answers, and the shelf publishes one of them |
| 🟢 `OUT-OF-SCOPE` | **4** | not a GNU grant — the instrument declines rather than guessing |
| 🟢 `FILE-NARROWER` | **0** | 🔴 **`RH`'s registered limb `1`, and it does not fire** |

Row-by-row in [`rh-file-level-range`](../../../evidence/rh-file-level-range.2026-10-15-p221.tsv).

## Use

```python
from version_range import audit_cell, parse_range, range_compare, combinable_with

parse_range('GPL-3.0')['bound']                    # -> 'unspecified'
range_compare('GPL-2.0', oat_sa_file_header)       # -> 'RANGE-UNDERSPECIFIED'
combinable_with('only', '2.0', '3.0')              # -> False   <- the finding that pays
combinable_with('unspecified', '2.0', '3.0')       # -> None    <- not an optimistic True
```

## What it does NOT claim

🔴 **It does not decide which grant binds in law.** When a plugin header says `GPLv2 or
later` and its `readme.txt` says `GPLv3`, which one a downstream user received is for
counsel and the copyright holder. The instrument refuses to report either as settled, so
the ambiguity reaches an SOW instead of a client's build.

🔴 **`BOTH-UNSPECIFIED` is not a defect in this KB.** `gocodebox/lifterlms` writes a bare
`GPLv3` in the file too. The shelf cell is a faithful copy of an ambiguous source, and the
right record is `UNSPECIFIED-AT-SOURCE` with a question for the maintainer.

🔴 **`FILE-SILENT` is not an accusation either.** Most source files in most projects carry
no per-file notice, and that is normal practice. It matters here only because `8` of these
`22` rows are **redistributed as loose files into a host application's tree**, where the
repository's `LICENSE` does not travel with them.

## Tests

```sh
cd compose/code/p221-licence-version-range && python3 -m unittest test_version_range -v
```

`26` tests, all passing. Fixtures are verbatim readings taken `2026-10-15`. **Five are
controls that must not fire:** an already-qualified cell must come back `AGREE`; an
Apache-2.0 row must come back `OUT-OF-SCOPE` rather than be coerced into a GNU verdict;
the `AGPL-6 d` day-count artefact must not parse as a licence; a grant that is bare on
both sides must come back `BOTH-UNSPECIFIED` and not be blamed on the shelf; and the
line-truncated `bigbluebutton` reading must be declined rather than guessed.
