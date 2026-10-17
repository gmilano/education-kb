# `pass257-restriction-scan` — the restriction vocabulary, unscoped

**What it closes:** `p1054.classify()` returns early when the payload is not shaped
like MIT and hardcodes `"hits": []`. The restriction vocabulary therefore only ever
runs *inside* the MIT-body branch, and a licence that restricts without reciting the
MIT grant is reported with no evidence at all.

## The measurement that justifies it

Three payloads, all read first-hand from `raw.githubusercontent.com` at `p257` on
`ls-remote --symref`-resolved refs, in the same hour, on the same transport:

| payload | bytes | `sha256`₁₆ | `p1054` verdict | `p1054` hits |
|---|---|---|---|---|
| `opentutor/opentutor-classifier` (USC academic) | `1 812` | `9b3b1802a09113ab` | `NOT-MIT-BODY` | `[]` |
| `yetanalytics/project-persephone` (Apache-2.0) | `11 356` | `43070e2d4e532684` | `NOT-MIT-BODY` | `[]` |
| `moodlehq/moodle-plugin-ci` (GPL-3.0) | `35 146` | `c53a65c2fd561c87` | `NOT-MIT-BODY` | `[]` |

A permissive grant, a copyleft grant and a **non-commercial academic licence** are
byte-for-byte distinguishable, and `p1054` reports them identically.

`is_usable_permissive` was never wrong — `USABLE_VERDICTS` is a closed set holding
only `MIT`, so nothing restricted has been published as permissive through it. **The
defect is in the EVIDENCE**, and the cost is a reader's: `NOT-MIT-BODY` with no hits
reads as *"not MIT, probably fine, check later"*, when the correct reading of the USC
payload is *"non-profit use only; commercial use requires a written agreement with
the USC Stevens Center for Innovation."*

`p255` caught `CaviraOSS/PageLM` only because PageLM recites the MIT grant verbatim
and diverges at the eleventh word. A bespoke academic licence never recites it, so it
never reaches the vocabulary. This is `ACTION YM`/`ACTION YH`'s hole met in the wild
for the first time with a real payload — and **wider than either was registered**:
the gap is not a missing title anchor, it is the SCOPE of the scan.

## Four tokens the vocabulary did not carry

Present in the USC body, absent from `p1054.RESTRICTION_TERMS`:
`non-profit` · `all rights reserved` · `without a written agreement` ·
`research purposes`. An academic licence restricts in a different register than a
commercial source-available one: it says **non-profit**, not **non-commercial**.

## The trap that makes a naive fix wrong

Verbatim `GPL-3.0` contains `noncommercial` in its own anti-circumvention text. A
scanner that reports any vocabulary hit as a restriction flags every GPL payload. So
each family carries its **measured** benign hit set, and the verdict is computed on
hits *minus* that set. `hits` is always reported; `effective_hits` is what grades.

## The correction this instrument's own controls forced

The first draft matched family anchors **body-wide**, with `agpl` ordered before
`gpl` so an AGPL payload could not grade as GPL. It graded the real GPL-3.0 fixture
as `AGPL` — because **GPL-3.0 section 13, at line 552 of its own text, is titled
"Use with the GNU Affero General Public License."** Every GPL-3.0 payload carries
that string.

A body-wide anchor for a family whose name another family's own text *quotes* can
only ever be wrong. The family is now taken from the payload's **title line**, with
the BSD/ISC operative clauses as a second stage for grants that open on a bare
copyright line. Ordering became a tiebreaker instead of load-bearing: the fix
removes the dependence on order rather than getting the order right.

Pinned as controls, so the body-wide form cannot come back.

## Verdicts

| verdict | meaning | usable? |
|---|---|---|
| `PERMISSIVE` | title names a permissive family, no effective hit | 🟢 yes |
| `COPYLEFT` | title names a copyleft family, no effective hit | 🔴 no |
| `RESTRICTED:added-restriction` | no family, and restriction vocabulary hits | 🔴 no |
| `FAMILY-PLUS-RESTRICTION:needs-a-human` | a known family **plus** an effective hit | 🔴 no |
| `UNCLASSIFIED:no-family-no-restriction` | neither — includes the `14` B `404` body | 🔴 no |

`USABLE_VERDICTS` is a closed allow-list for `p248`'s reason: a verdict added later
must not fall through into the usable branch. A control iterates `ALL_VERDICTS` and
asserts every non-permissive one is excluded.

## Running it

    cd compose/code/pass257-restriction-scan && python3 -I test_restriction_scan.py

`57/57`, and in `make hooks`. Run it from this directory — `python3 -I` strips the
script's directory from `sys.path` (`p355-cwd-portability`).

**Failure capability proven, not asserted** (`ACTION XV`'s class): reverted to the
pre-`p257` body-wide draft in a scratch copy, the suite reports `46/49` and exits
`1`, naming `gpl.family`, `GPL fixture is not graded AGPL` and
`a deep mention is not a title`.

That mutation run also exposed a second defect, now fixed: with `p1054` off the
expected relative path the control count dropped `57` → `49` **silently**. A skip
that does not announce itself is indistinguishable from coverage, so the absent-path
branch now prints `NOTE … SKIPPED, not passed`.

## Fixtures

`fixtures-p257/` holds the four real payloads plus the `404` body. The `404`
fixture's `sha256`₁₆ is `d5558cd419c8d46b` — **independently reproducing the
constant this base recorded at `p222`.**
