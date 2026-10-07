---
industry: education
region: Global
updated: 2026-10-07
---

# `p445-classifier-divergence` — this KB has two licence classifiers, and each is blind where the other sees

**P445: a hardened classifier that is not wired into the newer path protects nothing.**

## The specimen, measured on the same 19,329 bytes

[`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication)'s
root `LICENSE`:

| Classifier | Family | Commercial use |
|---|---|---|
| `lib/license_family.sh` → `osi_family_of` | 🟢 **`CC-BY-NC-4.0`** | 🔴 **NO** |
| `p436/sweep_payload.py` → `family_of` | 🔴 **`CC-BY`** | *(no such axis)* |

The shell classifier is the hardened one: **106/106** on its own suite, and **`P312`**'s
`test_nc_gate.sh` (**21/21**) exists *specifically* to assert that a payload with a
NonCommercial restriction answers `PROHIBITED` on the commercial axis **and keeps the
`NC` attribute in its family**.

🔴 **The Python `family_of` has no NonCommercial concept at all — and `family_of` is
what `p436` (the 503-slug payload sweep), `p441` (pass 26's tree enumeration) and
`p444` (this pass's root-vs-tree comparison) all call.** Every family verdict those
three instruments published passed through a classifier that cannot express the one
attribute deciding whether Globant may bill for the work.

🟢 **And `agents/top.md` has the row right**: *"**CC BY-NC-4.0** in `main/LICENSE` —
**non-commercial. Hard reject** for anything billable."* Pass 26's **trend 61** —
*"where this KB's prose and its instruments disagree about a licence, it has been the
instrument"* — holds for a fifth time, and this time the instrument was not merely
wrong but **structurally incapable**.

## Measured, 2026-10-07 — both classifiers over the same bytes of all 412 `LICENSED` roots

| Verdict | n | |
|---|---|---|
| `AGREE` | **369** | 89.6% |
| `VOCABULARY` | 25 | they name different families |
| `PYTHON-UNKNOWN` | 13 | the shell names one, Python declines |
| 🔴 `NC-ERASED` | **5** | the shell bars commercial use; Python asserts a usable family |

### 🔴 The 5 `NC-ERASED` rows — the class that reaches an invoice

| Slug | `family_of` says | the shell says |
|---|---|---|
| [`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication) | `CC-BY` | **CC-BY-NC-4.0** |
| [`openstax/osbooks-biology-bundle`](https://github.com/openstax/osbooks-biology-bundle) | `CC-BY` | **CC-BY-NC-SA-4.0** |
| [`sign/translate`](https://github.com/sign/translate) | `CC-BY` | **CC-BY-NC-SA-4.0** |
| [`Yunfeng-Wan/CSTutorBench`](https://github.com/Yunfeng-Wan/CSTutorBench) | `CC-BY` | **CC-BY-NC-4.0** |
| [`Jona-Zwetsloot/Somtoday-Mod`](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | `CC-BY` | **CC-BY-NC-SA-4.0** |

⚠️ **All five collapse to the same string, `CC-BY`** — a licence that *does* permit
commercial use. **A proposal filtering this shelf for commercially-usable rows on
`family_of`'s output picks up all five.**

### 🔵 And the blindness is symmetric — neither classifier is a superset

| Case | Python `family_of` | Shell `license_family.sh` | Who is right |
|---|---|---|---|
| **NonCommercial** (5 rows) | 🔴 erased to `CC-BY` | 🟢 `CC-BY-NC-*`, commercial `NO` | **shell** |
| **Elastic / PolyForm** (3 rows) | 🔴 `UNKNOWN` | 🟢 `Elastic`, `PolyForm` | **shell** |
| **EUPL** (9 rows) | 🟢 `EUPL` | 🔴 `UNCLASSIFIED` | **Python** |
| **MPL read as GPL** (4 rows) | 🟢 `MPL-2.0` | 🔴 `GPL-3.0` | **Python** |
| **GPLv2 read as LGPL** (4 rows) | 🔴 `LGPL` | 🟢 `GPL-2.0` | **shell** |
| `ankitects/anki` | 🟢 `AGPL-3.0` | 🔴 `CC-BY-SA-4.0` | **Python** |

Spot-checked by reading the title line of each payload:

```
oat-sa/qti-sdk      GNU GENERAL PUBLIC LICENSE Version 2     -> shell right
OpenEMIS/core       GNU GENERAL PUBLIC LICENSE Version 2     -> shell right
dequelabs/axe-core  Mozilla Public License, version 2.0      -> Python right
ankitects/anki      GNU Affero General Public License v3     -> Python right
```

🔵 **Each was hardened against the defect the other still has.** Pass 26 reordered the
Python classifier for *"the families that name other families"* — MPL §1.12 naming
GPL-2.0/LGPL-2.1/AGPL-3.0, EUPL-1.2's appendix naming five — and the shell classifier
never got that fix. The shell classifier gained NC and the Elastic/PolyForm
source-available families, and the Python one never got those. **No instrument in this
KB consults both.**

⚠️ **43 of 412 root families (10.4%) are wrong in one of the two classifiers**, and
which one is wrong depends on the licence family. **The correct verdict for this shelf
requires both**, which is the actionable output of this instrument.

## P445's own two defects, both caught by controls

| | Defect | What it did |
|---|---|---|
| 1 | 🔴 **`"NC" in "UNCLASSIFIED"` is `True`** | A bare substring test put **16** rows in `NC-ERASED`, of which **11 were `UNCLASSIFIED`** — eight of them Finnish national-agency repositories. The class meant to say *"forbids commercial use"* was **69% noise** |
| 2 | 🔴 **`commercial_use_ok` signals through its EXIT STATUS, not stdout** | Capturing stdout returned `""` for **all 412 rows, MIT included**, which read as *"commercial use not permitted"* for the entire shelf |

🔵 **Defect 2 is the more instructive: a column constant across every row is not a
measurement — and this one was constant at the alarming value.** A reader scanning it
would have concluded the whole shelf was unusable. The control is
`test_the_commercial_column_is_not_constant`.

🟢 **Fixing defect 1 properly meant changing the gate, not the regex.** `P250` built
family and commercial use as **two independent axes**, so the commercial question is
answered by `commercial_use_ok`, not by looking for `NC` in a name. Measured that way,
the shell bars commercial use on **11** of 412 payloads while only **5** carry a
visible `NC` token — the other 6 being `Elastic` ×2, `PolyForm`, and three whose family
is `UNCLASSIFIED` but whose text restricts commercial use. **The name-token gate would
have missed all six.**

⚠️ `NC-ERASED` deliberately **excludes** rows where Python says `UNKNOWN`: declining to
answer is not the same error as answering *"permissive"*, and only the second gets
quoted into a proposal.

## Limits

- **Root payloads only.** The tree payloads `p441`/`p444` read are not re-classified
  here; the same blindness applies to them and is unmeasured.
- **412 of 503.** The `UNLICENSED` side has no payload to compare.
- **Two classifiers, not three.** `lib/probe_payload.sh` and the per-file sweep
  `p199-perfile-license` are not compared.
- 🔴 **This instrument does not say which classifier to trust.** It says where they
  differ and, for six families, which one the payload's own title line supports.

## Run

```sh
python3 test_divergence.py                                      # 22/22
python3 -I divergence.py ../p444-root-vs-tree-family/payloads.licensed.2026-10-07.tsv
```

The payload is passed to the shell leg on **stdin, not argv**: several of these exceed
35 kB, an argv list has a hard limit, and silent truncation would look like a
classifier disagreement rather than a plumbing fault.
