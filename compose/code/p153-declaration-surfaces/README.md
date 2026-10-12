---
industry: education
region: Global
updated: 2026-10-12
---

# `p153-declaration-surfaces` — `ACTION FJ`: how many surfaces declare a licence, and do they agree

> 🟢 **`ACTION FJ`** *(registered p149, re-registered four times, FIRST on p153's list)* —
> audit the other three surface-bearing rows for a third declaration surface. Count
> surfaces per row.
> 🔴 *Refuted if no other row declares more than two* — which would make the
> three-surface shape unique to the best-governed row on the shelf.

🟢 **DISCHARGED. The falsifier is SILENT: 4 of 10 rows declare on more than two
surfaces**, so the three-surface shape is **not** a property of good governance.
🔴 **And the pass's real finding is that one of those rows CONTRADICTS ITSELF** — two of
its three surfaces say `MIT` and the one that governs says `GPL-3.0`.

    python3 surfaces.py <clones-dir> [subject ...]   # the audit
    python3 test_surfaces.py                         # 36 tests, offline, authored

## 🟢 The measurement

**[`result.surfaces.2026-10-12-p153.tsv`](result.surfaces.2026-10-12-p153.tsv)** ·
10 subjects, `git clone --depth 1 --single-branch`, **10 of 10 OK, 187 MB**.

| subject | surfaces | verdict | `LICENSE` says | the other surfaces |
|---|---|---|---|---|
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **3** | 🟢 `AGREE` | MIT | badge `README.md:6` · SPDX header `institution_config.go` |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **3** | 🟢 `AGREE` | MIT | `apps/api/pyproject.toml` · `apps/web/package.json` |
| [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | **3** | 🟢 `AGREE` | Apache-2.0 | `Cargo.toml` · badge `README.md:4` |
| 🔴 [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | **3** | 🔴 **`DISAGREE`** | 🔴 **GPL-3.0** | 🔴 `apps/backend/pyproject.toml` = **MIT** · 🔴 badge `README.md:13` = **MIT** |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 2 | 🟢 `AGREE` | MIT | badge `README.md:9` |
| [`BetterSEQTA/BetterSEQTA-Plus`](https://github.com/BetterSEQTA/BetterSEQTA-Plus) | 2 | 🟢 `AGREE` | MIT | `package.json` |
| [`admin978/canvas-mcp`](https://github.com/admin978/canvas-mcp) | 2 | 🟢 `AGREE` | MIT | `pyproject.toml` |
| [`nirholas/ai-tutor-mcp`](https://github.com/nirholas/ai-tutor-mcp) | 2 | 🟢 `AGREE` | Apache-2.0 | `package.json` |
| [`mohaneesh-03/mcp-tutor`](https://github.com/mohaneesh-03/mcp-tutor) | 2 | 🟢 `AGREE` | MIT | badge `README.md:5` |
| [`hesham0-0nasser/tutor-lms-mcp`](https://github.com/hesham0-0nasser/tutor-lms-mcp) | 🔴 **0** | 🔴 `NONE` | 🔴 **NONE** | — |

**`subjects=10 · with_more_than_two_surfaces=4 · DISAGREE=1`**

## 🔴 `ahmedEid1/lumen` — the finding, and why it is the most consequential on this shelf

Three surfaces, read from the tree at `HEAD` `07635d3` (2026-06-07):

| surface | what it says | where |
|---|---|---|
| 🔴 **the licence FILE** | **GPL-3.0** — *"GNU GENERAL PUBLIC LICENSE / Version 3, 29 June 2007"*, 674 lines | `LICENSE` |
| 🟢 the README **badge** | **MIT** — and the badge **links to `LICENSE`**, i.e. to the GPL-3.0 file | `README.md:13` |
| 🟢 package **metadata** | **MIT** — `license = { text = "MIT" }` | `apps/backend/pyproject.toml:13` |

🔴 **Two of three surfaces say MIT. The one that governs says GPL-3.0** — and the
rendered GitHub sidebar agrees with the file, because GitHub's own detector reads the
file and not the badge.

🔵 **Why the error direction matters.** The contradiction does not point in a safe
direction: it **understates copyleft**. A studio that shortlists by badge — which is what
a badge is for — or by package metadata, concludes `MIT` and builds proprietary work on a
strong-copyleft codebase. The reverse mistake would cost a conversation; this one costs a
remediation. 🟢 **This shelf's own census read it right** (`GPL-3.0`/`FILE`, p150), because
the census reads the tree. 🟢 **The rule is now measured rather than asserted: read the
file, never the badge.**

## 🔴 A defect in THIS instrument, found before publication

🔴 **The first run published `DISAGREE` on `zavora-ai/mcp-student-records` and it was
WRONG.** Its badge reads `license-Apache--2.0-blue.svg`: shields.io escapes a literal
hyphen as `--`, and a non-greedy capture stopped at the first one, reading **`Apache`**
instead of **`Apache-2.0`**. Two different families, one false contradiction.

🟢 **Fixed by decoding the badge grammar** (`--` → `-`, `_` → space, colour token
stripped), with **four tests** added for the escape, the underscore, a query string and a
colourless message. 🔵 **The lesson is `T39`'s** — *an exclusion is sound only relative to
the property measured* — applied to a matcher: **a licence id is not a token, it is an
encoded string, and the encoding is part of the measurement.**

🔵 **And one authored test was wrong, not the matcher.** `test_unclassified_file_only_is_not_agreement`
asserted `SINGLE` for a body that cannot be classified; the module returned
`UNCLASSIFIED`, which is what the docstring promises. 🟢 **The test was corrected and the
matcher left alone**, with the reason written into the test.

## 🟢 What the instrument will not do

🔴 **It does not resolve a contradiction** — resolution is a legal question and this is a
measurement. It reports `DISAGREE` and names every surface.
🟢 **It does not guess an owner or a jurisdiction** (`T67`/`T70` forbid it).
🟢 **The `-only`/`-or-later` election is NOT a disagreement** — that is `T81`'s question,
so surfaces are compared on the FAMILY. A test pins this.
🟢 **An unclassifiable body is `UNCLASSIFIED`, never silent agreement** — `P42`'s rule
(never publish a verdict without its denominator) applied to a licence body.
🔴 **`SPDX` header coverage is capped at 4 000 source files per subject**, so on a large
tree that surface is a sample and not a census. Declared, not hidden.

## 🟢 The suite

**36 tests, offline, no network, no clone.** Fixtures are transcribed from the three real
shapes this pass measured: `lumen`'s contradiction, `canvas-mcp`'s agreement, and
`tutor-lms-mcp`'s total absence. The GPL/AGPL/LGPL marker order is pinned by three tests,
because an AGPL body contains the string `GNU GENERAL PUBLIC LICENSE` in its own preamble
and a naive order reads `canvas-lms` as GPL.
