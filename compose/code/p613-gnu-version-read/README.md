---
industry: education
region: Global
updated: 2026-10-08
---

# `p613-gnu-version-read/` — the GNU branch read the **family** and invented the **version**

**Pass 50, 2026-10-08.** No code of its own: the repair lives in `lib/license_family.sh` and its
assertions in `lib/test_license_family.sh`, because 🔴 **a licence classifier must not be forked to be
fixed** — that is `P237`, and the whole reason `lib/` exists.

**What it proves:** that **4 of 5** real-world spellings of a GNU GPL title stub were classified
`GPL-2.0` — *a version the payload never names* — while **152 passing assertions** and all **4
canonical SPDX texts** said the branch was sound.

## The payload that found it

`UD_Spanish-AnCora` at tag `r2.8`, `LICENSE.txt`, HTTP 200, **68 bytes**:

```
GNU GENERAL PUBLIC LICENSE 3.0
http://www.gnu.org/licenses/gpl.html
```

Not synthetic. 🔵 It is the corpus that `spaCy`'s `es_core_news_sm` pins, which is how `P609`/`P610`
reached it.

## The defect

```bash
printf '%s' "$t" | grep -qi 'Version 3' && echo "GPL-3.0" || echo "GPL-2.0"
```

🔴 **The version read required the WORD `version`.** A numeric spelling falls to the `||`.

🟢 **This is `P561` verbatim** — *"the shared classifier read the licence family and invented the
version"* — which pass 46 found and closed **for MPL and EPL**, and did not audit on the GNU branch.

## Why 152/152 coexisted with it — and why the canonical fixtures are the reason

| Input class | Verdict before |
|---|---|
| SPDX `GPL-3.0-only` · `GPL-2.0-only` · `AGPL-3.0-only` · `LGPL-3.0-only` | 🟢 **4/4 correct** |
| `GNU GENERAL PUBLIC LICENSE 3.0` (the real payload) | 🔴 `GPL-2.0` |
| `GNU General Public License v3.0` | 🔴 `GPL-2.0` |
| `GNU GENERAL PUBLIC LICENSE` + `GPLv3` | 🔴 `GPL-2.0` |
| `GNU GENERAL PUBLIC LICENSE 2.0` | 🟡 `GPL-2.0` — **right by accident** |
| `GNU GENERAL PUBLIC LICENSE, Version 3` | 🟢 correct — the only stub form that worked |

🔵 **`P126` pt. 2.** Every fixture was a canonical FSF text, and every canonical FSF text spells
*"Version 3, 29 June 2007"* in words. 🔴 **The stubs are what treebanks and datasets publish** — the
exact tier passes 45–49 were working in.

🔴 **And `GNU GENERAL PUBLIC LICENSE 2.0` being right by accident is the dangerous part**: a sweep over
a mixed corpus shows **no anomaly**, because the branch is correct for 2.0 and wrong for 3.0.

🔴 **The commercial consequence.** GPL-2.0 and GPL-3.0 are **mutually incompatible**, and the error
resolved to the **older** licence — no patent grant, no anti-tivoization clause. A studio pricing an
obligation off this verdict priced the wrong licence.

## The precision measurement that licensed the widening — taken BEFORE the edit

| Token | Occurrences in canonical **GPL-2.0** (17 337 B) |
|---|---|
| `version 3` · `v3` · `gplv3` · `3.0` · `License 3` | 🟢 **0, all five** |

🟢 **So a wider version-3 discriminator cannot steal a legitimate GPL-2.0 payload.** 🔵 **`P171` is this
KB's own record of what a widened licence probe costs when that measurement is skipped.**

## The repair

```bash
if printf '%s' "$t" | grep -qi 'GNU GENERAL PUBLIC LICENSE'; then
   if printf '%s' "$t" | grep -qiE 'version[[:space:]]+3|licen[cs]e[[:space:],]*v?3(\.0)?([^0-9]|$)|gpl[[:space:]]*-?v?3(\.0)?([^0-9]|$)'; then
      echo "GPL-3.0"; return; fi
   if printf '%s' "$t" | grep -qiE 'version[[:space:]]+2|licen[cs]e[[:space:],]*v?2(\.0)?([^0-9]|$)|gpl[[:space:]]*-?v?2(\.0)?([^0-9]|$)'; then
      echo "GPL-2.0"; return; fi
   echo "GPL-UNVERSIONED"; return; fi
```

🟢 **`"names no version"` became its own answer**, matching the convention this KB already had for
three other families — `CC-BY…-UNVERSIONED` (`P551`), `EPL-UNVERSIONED` (`P560`), `MPL-UNVERSIONED`
(`P561`). 🔴 **The GNU branch was the last one still guessing.**

🟢 **`P562` honoured:** `GPL-UNVERSIONED` added to `OSI_RECONOCIDAS` in
`p411-cession-identity-gate/gate_cesion.py`, or that gate rejects as unknown a string its own library
emits.

## Validation

| Control | Result |
|---|---|
| `lib/test_license_family.sh` | 🟢 **152 → 168**, **168/168**, exit 0 |
| Mutants | 🟢 **6/6 killed** |
| Regression sweep, 110 suites, vs **pristine `HEAD`** | 🟢 **identical diff except `p550` red → green**; 107/110 → 108/110 |
| Fixtures | 🟢 `lib/fixtures-p613/` — 6 real payloads + `PROVENANCE.tsv` (URL, ref, HTTP, bytes, read date) |

### The mutants, each with the assertions that killed it

| # | Mutation | Killed by |
|---|---|---|
| 1 | revert to the bare `'Version 3'` grep (**the original defect**) | 4 assertions |
| 2 | drop the numeric `LICENSE 3.0` arm | 3 |
| 3 | drop the `GPLv3` arm | 1 |
| 4 | restore the `GPL-2.0` guess for unversioned | 1 |
| 5 | break the version-2 read | 6 |
| 6 | swap the v3 verdict to 2.0 | 16 |

## 🔴 The limit, declared: `Gap 256`

The **LGPL** branch reads its version only from a full-text anchor, so an LGPL **stub** answers bare
`LGPL` **even when it names Version 3**, while the canonical text answers `LGPL-3.0`.

🔵 **Not the same defect:** GNU **invented** a version; LGPL **discards** one. 🟡 A version too few is
honest and coarse. 🔴 **Not repaired here** because the fix moves a second contract — `LGPL-2.1` is
absent from `p411`'s recognised vocabulary — and `P562` says you do not touch an instrument whose
contract you have not read. 🟢 **The suite asserts the current behaviour** so it cannot drift silently.
