---
industry: education
region: Global
updated: 2026-10-07
---

# `p447` — the rooted probe answered, and the answer is not the whole grant

**Pass 28 of 2026-10-07.** Pre-registered action **A** and **B** of pass 26, plus the stage-0
re-measure pass 26's own closing instruction demanded.

## What it proves

| Stage | Question | Result |
|---|---|---|
| **0 — re-measure** | do the 412 published `LICENSED` rows still carry the right family? | 🔴 **21 move**: 9 `UNKNOWN → EUPL`, 7 `LGPL → GPL`, 5 `GPL → MPL-2.0` |
| **1 — action B** | how many payloads NAME more than one family? | **38 of 412** at window 6000 · **73 of 412** on full text (`P448`) |
| **2 — action A** | is there a second, different grant below the root? | 323 `ROOT-ONLY` · 47 `DIVERGENT-BUNDLED` · 33 `CONCORDANT` · **9 `DIVERGENT-OWN`** |

🔴 **`P452`** — the GNU family must be read from the payload's **title**, not from a window. GPL-2.0's
Preamble recommends the LGPL at char **784**; GPL-3.0's closing notes at **34,143**. Probing LGPL
before GPL over `text[:4000]` therefore filed **every GPL-2.0 payload as LGPL** and every GPL-3.0
payload correctly — decided entirely by the constant. Fixed in
`../p436-fork-hypothesis/sweep_payload.py`.

🔴 **`P447`** — `family_marks` matched literal spaces against prose wrapped at ~72 columns, so a
family name straddling a line break was invisible. Fixed in
`../p441-tree-licence-enumeration/enumerate_licence.py` by flattening whitespace.

🔴 **`P448`** — the 6000-character window misses the **EUPL-1.2 Appendix by 36 characters**: it
begins at char 5964 of the European Commission's 13,699-char payload, so a reader saw `['EUPL']`
where the truth is seven families.

🔴 **`P449`** — one label `CC-BY` covers plain Attribution, Attribution-NonCommercial,
Attribution-NonCommercial-ShareAlike and one document that is not Creative Commons at all. **5 of
the 7 rows carrying it are commercially unusable or mislabelled.**

## Reproduce

```sh
python3 test_divergence.py                                      # 61/61, offline
python3 divergence.py licensed.input.2026-10-07.tsv .           # the sweep, ~64 s
```

`divergence.py` needs network (`raw.githubusercontent.com` + `git clone`); `test_divergence.py`
never does.

## `payloads-corrected.2026-10-07-pass27.tsv` — the correction written back to the DATA layer

Pass 26 published its five `GPL → MPL-2.0` corrections as a **prose table** and left
`../p436-fork-hypothesis/payloads.2026-10-07.tsv` saying `GPL`. That is the defect this pass spent
most of its time on, so it is not repeated here: the corrected families are emitted in `p436`'s own
five-column format, as a **dated snapshot beside the original rather than over it**, because a dated
result file in this corpus is a historical record and overwriting one destroys the evidence that the
correction was needed.

```
slug <TAB> LICENSED <TAB> root_path <TAB> - <TAB> corrected_family
```

**412 rows.** Distribution: MIT 215 · Apache-2.0 72 · GPL 42 · AGPL-3.0 23 · UNKNOWN 13 · BSD 10 ·
**EUPL 9** · ECL-2.0 8 · CC-BY 7 · **MPL-2.0 5** · LGPL 4 · ISC 2 · CC0-1.0 2.

⚠️ **This closes the loop for `p436`'s payload census only.** The other censuses that consumed the
old `family_of` (`holder.tsv`, `homepage.tsv`, the `p250` commercial sweep, the `p419` copyleft
census) still carry pre-`P452` families, and that debt is **declared in `intel/trends.md` and
pre-registered as pass 29's action B** rather than left invisible.

## Declared limits

- RTF payloads (`docs/LICENSE.rtf`, `OS4ED/openSIS-*`) classify `UNKNOWN`. A limit, not an absence.
- A confirmed deeper grant proves a licence **text** is present at that path. It does not prove the
  project intends it to govern that subtree. The verdict is a **reading list**.
- `is_own_grant` narrows `p441`'s depth rule with a filename test, because
  `LICENSE-3RD-PARTY.txt` sits at root depth and is not a second grant. **That rule can only remove
  rows from `DIVERGENT-OWN`, the bucket this pass had a ">5" prediction over.** It was applied
  before scoring anyway, with 9 controls holding `LICENSE-MIT`, `LICENSE-APACHE`, `COPYING.LESSER`
  and `aoe-web-backend/LICENSE` as own grants.
- The commercial axis (`PERMISSIVE` / `COPYLEFT`) was written **before** the sweep ran and is not
  re-cut afterwards. Under it the pre-registered "interesting" class reads **1**; read for actual
  reciprocity it is **0**, because `CC-BY` is attribution-only. Both are published.
