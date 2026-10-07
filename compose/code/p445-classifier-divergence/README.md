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

---

## 🟢 Re-run, pass 28 of 2026-10-07 — both classifiers hardened, and the divergence all but closes

Pass 27's pre-registered action B was *"give `lib/license_family.sh` the **EUPL** patterns
it lacks and `sweep_payload.family_of` the **NC** axis it lacks, then re-run `p445`"*, with
the prediction:

> ⚠️ *"Expect `AGREE` to rise from 369 to **above 400** and the residual disagreements to be
> the **GPLv2-preamble** rows only — which would mean the two classifiers' remaining gap is
> a single, nameable defect rather than two vocabularies."*

⚠️ **Wrong twice, and narrowly on the number.**

| Verdict | pass 27 | pass 28 | |
|---|---|---|---|
| `AGREE` | 369 | **399** | 96.8% — the prediction said *above 400*, so it misses **by one row** |
| `VOCABULARY` | 25 | **0** | |
| 🔴 `NC-ERASED` | 5 | **0** | the class that reaches an invoice is closed |
| `BOTH-DECLINE` | *(not a verdict)* | 10 | `P458` — see below |
| `PYTHON-UNKNOWN` | 13 | **3** | |

🔴 **And the residual is not "the GPLv2-preamble rows only".** Those rows existed, were a
real defect (`P455`), and were **fixed** rather than tolerated. What is left is **3 rows** —
`canyongbs/advisingapp`, `digillab-lmu/smart-rag`, `sodadata/soda-core` — where the shell
names `Elastic` or `PolyForm` and the Python side's deliberately coarse p170 vocabulary has
**no token for them**. All three are commercial-use **PROHIBITED**, so the gap is on the
rows that matter — and it is a **vocabulary** gap, not a reading error. Two classifiers
built to be comparable with different published tables will always have one.

### 🔴 Five defects the re-run found, and in three of them the hardened classifier was the wrong one

Pass 27 cast the shell as hardened and the Python side as blind. Re-running after fixing
both inverted that:

| | Defect | Rows | Which side was wrong |
|---|---|---|---|
| `P453` | the shell had **no EUPL branch at all**, while the Python side had had one since pass 26 | 9 | 🔴 shell |
| `P454` | the shell probes the **GNU family before Mozilla/Eclipse**, and MPL-2.0 §1.12 names all three GNU licences — **the exact defect pass 26 fixed in Python and never ported** | 5 | 🔴 shell |
| `P455` | the Python side probes **LGPL before GPL over the whole body**, and GPL-2.0/3.0 both *close* by recommending the LGPL | 8 | 🔴 python |
| `P451` | `"apache license" and "version 2.0"` excludes every **prose** declaration (`"licensed under Apache License 2.0"`) | 1 | 🔴 python |
| `P457` | the **title-stripped** GNU payload — three repositories ship the full text with the title removed | 3 | 🔴 both |

🔴 **`P457` carries a shelf correction worth more than the convergence number.**
[`untisapi/untis4j`](https://github.com/untisapi/untis4j) is **LGPL-3.0** — its text says
*"this License refers to version 3 of the GNU Lesser General Public License"* — and the
shell reported it `GPL-3.0`. The LGPL permits linking from proprietary code and the GPL does
not, so the row was published **one tier more restrictive than it is**.

### 🔴 `P458` — `UNCLASSIFIED` is not a family, and counting it as one reported agreement as disagreement

The old branch asked only `sh and py == "UNKNOWN"`, and the string `"UNCLASSIFIED"` is
**truthy** — so a row where **both** classifiers declined was filed under
`PYTHON-UNKNOWN`, a verdict whose name asserts that the shell named one. Measured: **10 of
the 13** residual rows were this. Declining together is the one honest thing two
classifiers can do about a payload like
[`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka)'s, which is a REUSE-spec
**pointer** to per-file licensing and contains no grant at all.

### ⚠️ `P453` — and one row was lost to the network, silently

The first re-run reported `eduNEXT/openedx-lti-tool-plugin` as `UNREADABLE`. Probed
directly a minute later the same path returned **HTTP 200 and 11,357 bytes** of
Apache-2.0. `read_blob` swallowed every exception and answered `""`, and `family_of("")` is
`UNKNOWN` — so **a transient reset is indistinguishable from a repository that declines to
license its code**. A measurement whose failure mode imitates its most interesting finding
is unsound; `read_blob` now retries once, and never on a 404, which is an answer.

### Reproduce

```bash
python3 test_divergence.py          # 22/22 -- NOT `python3 -I`, see below
python3 divergence.py ../p444-root-vs-tree-family/payloads.licensed.2026-10-07.tsv \
        > result.2026-10-07.pass28.tsv
```

⚠️ **The command this README carried above is `python3 -I test_divergence.py`, and it cannot
work**: `-I` drops the script's own directory from `sys.path`, so `import divergence` raises
`ModuleNotFoundError`. A reproduction command that does not reproduce is a documentation
defect of the same family as the rest of this page, found the same way — by running it.
