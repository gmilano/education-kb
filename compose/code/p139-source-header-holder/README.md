---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-source-header-holder` — `ACTION CJ`: on the rows where the root file is the whole story, the root file names nobody

**Executes p138's pre-registered `ACTION CJ`** (carried unrun from `ACTION CH`), written as:

> Extend a licence-header read to **source-file headers** on the three largest `ROOT_ONLY`
> rows. 🔴 *Refuted if none carries a foreign header — which would make p137's 50% an estimate
> rather than a floor.*

## Verdict: **DISCHARGED, NOT REFUTED — 2 of 3, and the third fails differently**

| row (largest `ROOT_ONLY` by tree paths) | tree paths | source files read | own holders | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 1 411 | 2 | 🔴 **1 — `FOSS United`, 78 header lines** | `FOREIGN_HEADER_IN_SOURCE` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 450 | 1 | 🟢 0 | `OWN_HEADERS_ONLY` 🔴 *but see `P139-A2`* |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 660 | 🔴 **0** | 🔴 **3 — `Pusher`, `Chen Fengyuan`, `Chen, Yi-Cyuan`** | `FOREIGN_HEADER_IN_SOURCE` |

🔵 **p137's 50% is a floor, not an estimate.** Two of the three rows it cleared as `ROOT_ONLY`
carry a holder in their source that their licence file does not name. `ROOT_ONLY` was never a
statement about ownership — it was a statement about where licence *files* live.

## `P139-A1` — `frappe/lms`: the root licence names no holder of `frappe/lms`

Its `license.txt` is 33 893 bytes and contains exactly **three** lines with the word
`Copyright` in them. None of them is a grant by the project:

| line | text | what it is |
|---|---|---|
| 4 | `Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>` | the FSF's copyright **on the licence text** |
| 65 | `"Copyright" also means copyright-like laws that apply to other kinds of` | AGPL-3.0 **§0 definitions** |
| 633 | `Copyright (C) <year>  <name of author>` | 🔴 **the "how to apply" template — placeholder never filled in** |

🔴 **So the ownership of the row exists only in its source headers** — and there it is **two
distinct legal entities**: `Frappe` / `Frappe Technologies Pvt. Ltd.` (165 lines) and
🔴 **`FOSS United`** (78 lines), the Indian non-profit foundation, which is not Frappe. The split
is not cosmetic: 78 files of an AGPL-3.0 application are held by a different entity from the one
whose name is on the repository, and a notice obligation runs to both.

🔵 **This is the sharpest form of the class.** p137 found rows whose root file *under-reported*
ownership. This row's root file reports **none**, and a verdict taken from it — "AGPL-3.0,
Frappe" — is wrong in both halves on 78 files.

## `P139-A2` — `openeducat/openeducat_erp`: clean headers, and a delegation to a file that does not exist

The row is genuinely `OWN_HEADERS_ONLY`: **190** header lines, all `OpenEduCat Inc`, zero foreign.
🔴 **Its root `LICENSE` nevertheless does not answer the ownership question, because it delegates
it twice and both pointers dangle:**

> `For copyright information, please see the COPYRIGHT file.`

🔴 **There is no `COPYRIGHT` file anywhere in the tree** — `git ls-tree -r HEAD` over all 1 345
paths returns nothing matching, and the 15 licence-shaped paths the scan skipped do not include
one. The same file then delegates again:

> `Some external libraries and contributions bundled with OpenEduCat may be published under other
> GPL-compatible licenses. For these, please refer to the relevant source files and/or license
> files, in the source code tree.`

…and the source files carry only `OpenEduCat Inc`. 🔵 **The chain terminates nowhere.** The grant
is sound and legible — LGPL-3.0, stated in the first lines — but the row cannot tell a client whom
it owes, and it is the only row of the three that says out loud that it is not trying to.

## `P139-A3` — `academico-sis/academico`: zero own headers, three foreign ones

🔴 **No source file in this row carries its own holder.** The root `LICENSE` is a 1 094-byte MIT
grant held by `Thomas Debay and project contributors`; the only headers in the tree belong to
other people, all three in built Filament front-end bundles under `public/js/` — exactly the
paths a client redistributes:

| holder | path | upstream |
|---|---|---|
| `Pusher` | `public/js/filament/filament/echo.js` | Laravel Echo's Pusher client |
| `Chen Fengyuan` | `public/js/filament/forms/components/file-upload.js` | `cropperjs` |
| `Chen, Yi-Cyuan` | `public/js/filament/support/support.js` | `js-sha256` |

This is the **front-end vendoring** class p137 named, reproduced on a row p137 had cleared — and
it reaches it through `public/`, where no licence file would ever be looked for.

## 🔴 Two instrument errors caught before they published

Recorded because this KB's rule is that a probe's own failures are findings about the probe.

1. 🔴 **The first draft read the working directory and reported `Junio C Hamano` as a foreign
   holder of `openeducat/openeducat_erp`.** The line is real; it is in
   `.git/hooks/pre-rebase.sample`, which `git clone` writes and which is **git's own sample hook,
   not repository content**. The collector now walks `git ls-tree -r HEAD` and reads blobs with
   `git show`, so the working directory is never consulted; `is_vcs_artifact` keeps a second guard
   in tested code.
2. 🔴 **The first draft read licence bodies as headers and published five "foreign holders" of
   `frappe/lms` that are sentences of AGPL-3.0** — among them `also means copyright-like laws that
   apply to other kinds of` and `on the software, and (2) offer`. Two fixes: a year or `(c)` marker
   is now **mandatory** (none of the eight offending prose lines carries one), and licence FILES are
   excluded from a scan whose subject is source headers. All eight lines are now regression fixtures.

🟡 **And one false negative caused by that second fix, then corrected**: making the marker mandatory
*in front of* the holder dropped `@copyright Chen, Yi-Cyuan 2014-2023`, the JSDoc form where the
year trails the name. It is a real foreign grant (`js-sha256`); the trailing-year form is now matched
and tested. 🔵 **The fix for a false positive produced a false negative in the same file, and only
re-running against the same three rows showed it.**

## Channel note — 🟢 a lane that p138 recorded as closed is open

🟢 **`git clone --depth 1` against `github.com` works in this channel**, which is how all three rows
were read. p138 recorded `api.github.com`, `codeload.github.com` and `github.com` HEAD as `403` and
therefore published **UNMEASURED** for star counts and HEAD dates. 🔵 **Git smart-HTTP is a different
lane from the REST API, and it answers.** HEAD dates, taken this pass from the clones:

| row | HEAD commit | HEAD date |
|---|---|---|
| `frappe/lms` | `0f760e6` | **2026-10-11** |
| `openeducat/openeducat_erp` | `1c95cef` | **2026-09-07** |
| `academico-sis/academico` | `d0cd78c` | **2026-10-07** |

🔴 **Star counts remain UNMEASURED** — git carries no star count, so that half of p138's gap stands.

## Files

| file | role |
|---|---|
| `header_holder.py` | the classifier: `extract_holder`, `classify`, `is_steward`, `is_vcs_artifact`. No I/O |
| `test_header_holder.py` | **20 tests**, all fixtures taken from these three rows or from the probe's own two errors. `python3 -I test_header_holder.py` |
| `scan_headers.py` | the collector. Walks `git ls-tree -r HEAD`; skips licence files; reads a 120-line header window |
| `result.2026-10-12-p139.tsv` | per-row summary and per-holder detail, as published above |

### Reproduce

```sh
git clone --depth 1 https://github.com/frappe/lms /tmp/cj/frappe_lms
python3 -I scan_headers.py /tmp/cj/frappe_lms frappe/lms "Frappe,Frappe Technologies"
```

🔵 **`own_names` is an argument, not an inference.** No slug says that `frappe/lms` is also held by
`FOSS United`; a reader who disagrees with the list can change it and re-run, which is not true of a
probe that guesses the owner from the repository path.

## 🔴 What this probe does NOT establish

- 🔴 **Three rows, not eight.** Five `ROOT_ONLY` rows were not read: `Crosstalk-Solutions/project-nomad`,
  `overhangio/tutor`, `adaptlearning/adapt_framework`, `openedx/XBlock`, `openedx/codejail`.
  The registered action said "the three largest" and that is all that ran.
- 🔴 **A 120-line header window.** A holder named in the middle of a long file is not counted.
- 🔴 **Text suffixes only.** Binary assets, fonts and images carry holders too and were not read —
  which matters most for `academico`, whose foreign holders are all in `public/`.
- 🔴 **No region was measured for any holder.** `FOSS United` is Indian and `Frappe` is Indian, which
  would place the row in **APAC**, but that is an inference from a name and is not booked as region
  evidence. The LATAM-ownership gap is at **nine consecutive passes**.
- 🟡 **`OWN` vs `FOREIGN` is a judgement about legal identity.** `FOSS United` and
  `Frappe Technologies Pvt. Ltd.` are separate registered entities and are classified as such; a
  reader who treats the Frappe ecosystem as one holder gets 1 of 3 rather than 2 of 3, and the
  refutation condition is still not met.
