---
industry: education
region: Global
updated: 2026-10-12
---

# `p152-vertical-election` — `ACTION GA`: the election over the six vertical platforms

> 🟢 **`ACTION GA`** — run `p151-election-surface` over the SIX vertical platforms.
> 🔴 *Refuted if the verticals are also silent, 6 of 6* — which would promote `T81` from
> "true of this shelf's small rows" to a property of education copyleft generally.

🟢 **DISCHARGED. The falsifier is SILENT: 3 of 6 state an election.** 🔴 **And the pass's
real finding is not the verdict — it is that the verdict is WRONG on two of the six rows,
in two different ways, and this shelf could not have seen either.**

    python3 election_verticals.py <clones-dir> [subject ...]   # the port + the denominator
    python3 omission.py          <clones-dir> [subject ...]     # the third election form
    python3 test_election_verticals.py                          # 25 tests, offline, authored

## 🔴 Why this is a RE-IMPLEMENTATION, said before any result

🔴 **p151's `election.py` could not be executed in this pass's sandbox** — the attempt was
refused `[Code from External]`. 🟢 **The matcher semantics are re-implemented here**, and
the claim of independence is deliberately WEAK: 🔴 **this is a REPRODUCTION control, not an
independent second surface.** Agreement on p151's seven rows proves the re-implementation
is faithful; it does **not** corroborate the semantics.

🟢 **The reproduction is EXACT**, row for row:
[`result.repro-p151-seven.2026-10-12-p152.tsv`](result.repro-p151-seven.2026-10-12-p152.tsv)
— **1 513** files scanned, **7** `SILENT`, control **7 of 7** — the three figures p151
published.

🔵 **A note on the sandbox, because the shelf has mis-stated this twice** (`P970`,
`P151-S`): repo code is **not** globally refused. p151's `test_population.py` ran **31 of
31** in this same pass. 🔴 **One invocation was refused, not a channel.** 🟢 Per
`ACTION GE`, that is recorded as what was refused and what was tried, with a date.

## 🟢 `ACTION GA` — the measurement

**[`result.verticals.2026-10-12-p152.tsv`](result.verticals.2026-10-12-p152.tsv)** ·
**105 727** source files over 6 trees, `git clone --depth 1`, 6 of 6 OK.

| platform | shelf licence | scanned | 🆕 GNU notices | or-later | verdict as read | 🔴 **what it ACTUALLY is** |
|---|---|---|---|---|---|---|
| `moodle/moodle` | GPL-3.0 | **60 259** | **14 024** (23.3%) | **13 859** | 🟢 `OR_LATER` | 🟢 **correct — GPL-3.0-or-later, first-party notice** |
| `instructure/canvas-lms` | AGPL-3.0 | **19 286** | 🔴 **16 905 (87.7%)** | **0** | 🔴 `SILENT` | 🔴 **WRONG — AGPL-3.0-ONLY, elected by OMISSION in 16 896 files** |
| `sakaiproject/sakai` | ECL-2.0 | **11 620** | **12** (0.1%) | **1** | 🔴 `OR_LATER` | 🔴 **FALSE ATTRIBUTION — the one hit is VENDORED TrimPath (© Metaha, GPL-2.0-or-later)** |
| `bigbluebutton/bigbluebutton` | LGPL-3.0 | **3 083** | **263** (8.5%) | **255** | 🟢 `OR_LATER` | 🟢 **correct — LGPL-3.0-or-later, first-party notice** |
| `openedx/edx-platform` | AGPL-3.0 | **7 129** | 🟡 **1** (vendored) | **0** | 🟡 `SILENT` | 🟡 **right verdict, unmeasured reason — a ROOT-ONLY notice surface** |
| `learningequality/kolibri` | MIT | **4 350** | 🟢 **0** | **0** | 🟢 `SILENT` | 🟢 **right verdict, different reason — no copyleft notice exists to elect in** |

🟢 **So `T81` is CONFINED**, which is what the action asked. 🔴 **But three of the six
verdicts are correct only by accident, and the next three sections are why.**

## 🆕 🔴 `T85` — an election has THREE surface forms, and this shelf knows two

| form | surface | p151 reads it |
|---|---|---|
| **or-later** | the clause *"or (at your option) any later version"* is PRESENT | 🟢 yes |
| **only, worded** | the word *"only"* appears — *"version 3 of the License only"* | 🟢 yes |
| 🆕 🔴 **only, by OMISSION** | a COMPLETE GNU notice whose or-later clause is **ABSENT** | 🔴 **no** |

🔴 **The third form is the FSF's own `-only` form**, and `instructure/canvas-lms` carries it
in **16 896** files:

    # Canvas is free software: you can redistribute it and/or modify it under
    # the terms of the GNU Affero General Public License as published by the Free
    # Software Foundation, version 3 of the License.

🔴 **There is no word "only" to match and no or-later clause to find.** Every matcher on
this shelf therefore reports `SILENT` — 🔴 **the same verdict it gives a tree with no
notice at all.** 🟢 The test is **structural, not lexical**: a notice that reaches the
grant verb (*"as published by the Free Software Foundation"*) and names a version, and then
does **not** continue into the or-later clause, has elected the stated version.

🟢 **Measured over both populations**
([`result.omission.2026-10-12-p152.tsv`](result.omission.2026-10-12-p152.tsv)):
**16 896** omission-form elections across the verticals, 🟢 **and 0 across p151's seven
small rows** — so the new form does not disturb p151's published null.

🔵 **What it changes in a room, and it is the opposite of what the shelf has been saying.**
`P38` step 4 says the election is UNSTATED, so ask the author. 🔴 **For Canvas LMS that
advice is wrong**: the election IS stated, 16 896 times, and it says **AGPL-3.0-only**. A
studio forking Canvas may **not** take "or later". 🟢 For Moodle it may. 🟡 For Open edX the
per-file surface is genuinely empty — 🔵 **though its README independently says *"version 3
of the AGPL unless otherwise noted"***, which points the same way as Canvas by a different
channel.

## 🆕 🔴 `T86` — an election read from a tree is not the SUBJECT's election

🔴 **Sakai's `OR_LATER` verdict belongs to a bundled third-party library.** The single hit
is `library/src/webapp/js/trimpath-template-latest.js` — *"TrimPath Template. Release
1.0.38. Copyright (C) 2004, 2005 Metaha"*, dual GPL-2.0-or-later / Apache-2.0. 🔴 **Sakai
itself is ECL-2.0 and elects nothing.**

🔴 **`SKIP_DIRS` does not catch it, and cannot**: it excludes `vendor/`, and this copy lives
under `library/src/webapp/js/`. 🟢 **The limit is pinned as a test** rather than left to be
rediscovered, and the signal a fix must read is in the notice itself — 🔵 **its own
copyright holder**, which is not the subject's.

🔴 **The same defect reaches `openedx/edx-platform`**, whose solitary "notice" is
`common/test/data/uploads/jschannel.js` — also vendored. 🟢 **So edx-platform's
FIRST-PARTY notice surface is ZERO**, and its `SILENT` is a root-only licence surface
rather than a declination.

## 🆕 🟢 `P42` — the notice DENOMINATOR, which is why this is not only a port

🔴 **p151 published "0 elections over 1 513 files" with no denominator.** A tree with
**zero** GNU per-file notices is silent for a completely different reason than a tree with
**16 905** notices that each decline to elect — 🔴 **and p151's instrument reports the two
identically.** 🟢 `notice_files` is that denominator, and it splits `SILENT` into three
classes that were one:

| class | example | notices | why it reads SILENT |
|---|---|---|---|
| **NO_NOTICE** | `kolibri` | **0 of 4 350** | 🟢 permissive; there is no copyleft notice to elect in |
| **ROOT_ONLY** | `edx-platform` | **0 first-party** | 🟡 the licence lives in the root file alone |
| 🔴 **DECLINING** | `canvas-lms` | **16 905 of 19 286** | 🔴 **it is not silent at all — `T85`** |

🟢 **And it re-reads p151's own seven rows.** All **17** of their notice-bearing files are a
fourth class — **`NOTICE_NO_VERSION`**: a notice that names a GNU licence and never reaches
a version. 🔴 **`Agso-o/sigaa-calendar` and `ahmedEid1/lumen` have ZERO notice files across
1 020 source files.** 🟢 **So `T81` HOLDS for the small rows, for a reason p151 did not
measure**: their notices had no version to elect from.

🔵 Same defect class as `T84`'s `LINK LAYER` / `PROMPT LAYER` split — two populations
reading zero on one instrument for different reasons.

## 🔴 What this module does NOT do

- 🔴 **It cannot attribute a notice to the subject rather than to a bundled dependency.**
  `T86` is measured and **not** fixed; the verdict on `sakai` stays known-wrong in the TSV
  rather than silently dropped. 🔵 **`ACTION GF`.**
- 🔴 **The positive control degrades on these subjects and the reason must be stated**:
  it fires on **10 of 161** licence bodies, not 7 of 7, because six large trees carry
  **161** licence files of which most are vendored MIT/Apache. 🟢 **A 10/161 control is not
  a failure and not a clean positive either** — the right control for a big tree is its own
  root licence file. 🔵 **`ACTION GG`.**
- 🔴 **`MIXED` is reportable and was never reached.** No subject here states two forms.
- 🔴 **No star count and no region is read by this module.** It reads licences only.
