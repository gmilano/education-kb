---
industry: education
region: Global
updated: 2026-10-09
---

## 🟢 Eightieth pass, 2026-10-09 — **six new foundational repos**, and the finding is a REGRESSION: the measurement layer was archived on 2026-10-06 and never rebuilt

⏱️ **Twelfth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔴 The finding first, and it is about this shelf, not about a repository

🟢 **Measured across every live file, this pass:**

| phrase | live shelf (`agents/`+`repos/`+`verticals/`+`intel/`+`compose/`) | `archive/2026-10-06-pre-reset/` |
|---|---|---|
| `cognitive diagnosis` / `diagnóstico cognitivo` | 🔴 **0 occurrences** | 🟢 **23**, across **8 of 8** files |

🔴 **The live shelf cannot MEASURE mastery, and it used to be able to.** 🟢 The archive's own pass-87 entry records the layer being added deliberately — *"no son siete piezas sueltas sino UNA CAPA DE MEDICIÓN EDUCATIVA completa — trazado de conocimiento, diagnóstico cognitivo, testing adaptativo, datasets, NLP de ítems y simulación"* (the BigData Lab @USTC family: `EduData`, `EduCDM`, `EduKTM`, `EduNLP`, `EduSim`, `EduCAT`). 🔴 **The 2026-10-06 reset archived it, and eighty passes of the live shelf have shipped tutoring and — since pass 79 — retention scheduling on top of a hole where the measurement used to be.**

🔵 **Why that matters concretely:** pass 79's `R79a` sells *"retention is the measurable outcome an institution will actually buy."* 🔴 **FSRS schedules a review; it does not estimate whether a learner knows a concept.** Those are different quantities, and the live shelf has had only the scheduler.

🟢 **`P875` — "new to the live shelf" is NOT "new to this KB". The archive is part of the record and is checked before a row is called a first.** 🟢 Applied this pass: all **15** new rows were grepped against `archive/` as well as the live tree — **0 hits in either**, so they are genuine firsts. 🔴 **Had this pass only grepped the live tree, it would have announced "the measurement layer is new here" — and that sentence would have been false.** 🔵 A reset is not a blank slate; it is a *move*, and a shelf that forgets where it moved things re-buys them or, worse, declares a gap that is really a loss.

---

### 🟢 Added: the knowledge-tracing / cognitive-diagnosis layer, rebuilt from live payload reads

🔵 **These are the models that answer *"does this learner know concept X, and how sure are we?"*** — the input a tutor needs before it chooses what to teach, and the input a scheduler needs before it decides what to review.

| repo | grant (payload-read inline) | bytes | ref · sha | role |
|---|---|---|---|---|
| 🆕 [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) | 🟢 **MIT** | 1 071 | `main` · `6151f49` | **Reference implementations** of the main KT models (DKT, DKVMN, SAKT, …) in one PyTorch tree. **194★**. The cheapest way to get a working baseline rather than a paper. |
| 🆕 [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | 🟢 **MIT** | 1 085 | `main` · `20af796` | **The widest single library**: knowledge tracing **+ cognitive diagnosis + exercise recommendation** under one API. **82★**. 🟢 Actively the successor to `ZhijieXiong/dlkt`, which its own README marks as migrated here. |
| 🆕 [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) | 🟢 **MIT** | 1 064 | `main` · `d5862bd` | **Unified student cognitive-modelling framework** — the configurable harness (datasets, splits, metrics) rather than a model zoo. **78★**. This is the row that makes results comparable. |
| 🆕 [`jilljenn/ktm`](https://github.com/jilljenn/ktm) | 🟢 **MIT** | 1 071 | `master` · `12084d6` | **Factorization machines for knowledge tracing** — the strong classical baseline that repeatedly matches deep KT at a fraction of the cost. **140★**. 🔵 Worth having precisely because it is the thing to beat before buying a transformer. |
| 🆕 [`jhljx/GKT`](https://github.com/jhljx/GKT) | 🟢 **MIT** | 1 061 | `master` · `271c72d` | **Graph-based KT**: models the prerequisite graph between concepts instead of a flat skill vector. **141★**. The row that connects a curriculum map to a mastery estimate. |
| 🆕 [`r-dcm/measr`](https://github.com/r-dcm/measr) | 🟡 **GPL-3.0-*or-later*** | 34 904 | `main` · `93a2e87` | **Bayesian diagnostic classification models via Stan** — the psychometrics-grade option, with real uncertainty intervals instead of a point score. **13★**. 🔴 **Copyleft: see the grant note.** |

### 🔴 `yxonic/DTransformer` — probed, and REJECTED, with the reason recorded

| repo | layers probed | verdict |
|---|---|---|
| 🔴 [`yxonic/DTransformer`](https://github.com/yxonic/DTransformer) (`main` · `1dc4598`) | 🟢 **11** licence filenames → all **404**; `README.md` **200** with **zero** licence mentions; `pyproject.toml` **200** (417 B) with **no** licence field; `setup.py` **404** | 🔴 **NO GRANT AT ANY LAYER → all rights reserved** |

🟢 **46★ and a WWW '23 paper behind it, and it still cannot be used.** 🔵 It is written down as a named negative so that no later pass spends the probe again, and so that nobody reaches for the best-cited name in this layer without knowing it is closed.

### 🔴 The copyleft row, stated as the obligation rather than the tag

🟢 **`measr` is GPL-3.0-*or-later*, and the `or-later` exists ONLY in the manifest.** 🟢 Measured: `LICENSE.md` can say no more than *Version 3*; `DESCRIPTION` reads `License: GPL (>= 3)`. 🔴 **A payload-only read records this as GPL-3.0-only and throws away the downstream option the project actually granted.**

🔵 **What GPL-3.0 means where this row lands:** `measr` is an **R package**, so the realistic use is *analysis*, not linking. 🟢 **Running it to fit a model and acting on the numbers triggers nothing** — GPL obligations attach to **distributing** a combined work. 🔴 **Shipping it inside a client-delivered product does**, and then the whole combined work carries GPL-3.0. 🟢 **The permissive alternative in the same slot is `pyedmine`, which carries cognitive diagnosis under MIT** — so this shelf now has both a permissive and a psychometrics-grade option, and the choice is explicit rather than accidental.

### 🔴 `T1` paid harder here than anywhere on this shelf, and the reason is structural

🟢 **Measured, 11 of 11 candidates resolved with `git ls-remote --symref`:**

| default ref | count | which |
|---|---|---|
| `main` | 🟢 5 | `knowledge-tracing-collection-pytorch`, `pyedmine`, `EduStudio`, `DTransformer`, `measr` |
| 🔴 `master` | 🔴 **6** | `ktm`, `GKT`, `EdOptimize`, `my-learning-analytics`, `sagefy`, `stem-tutor-agent` |

🔴 **A hardcoded `main` writes off SIX of eleven rows — more than half.** 🟢 **Compare pass 79's platform layer: 2 of 12.** 🔵 **`P876` — the research-code layer defaults to `master` at roughly three times the platform layer's rate, because it is older code that was never migrated.** 🟢 **So `ref.sh` as Gate 0 is not a nicety on this layer; it is the difference between finding it and concluding it does not exist.** 🔴 **And this is a plausible partial cause of the fourteen-week agent drought `P795` diagnosed as query ambiguity: a `main`-only probe silently rejects the oldest half of exactly this layer.**

### 🟢 Byte counts across the MIT rows, and why the shelf's "1 079 B = MIT" shorthand has to go

🟢 **Measured this pass, six MIT payloads, all confirmed `MIT License` by title line:** `1 061` (`GKT`) · `1 064` (`EduStudio`, `TheGrandQuiz`) · `1 068` (`pruju-ai`) · `1 071` (`knowledge-tracing-collection-pytorch`, `ktm`) · `1 085` (`pyedmine`).

🔴 **That is a 24-byte spread, and the shelf has been writing `1 079 B` as if it were MIT's signature.** 🟢 **The variance is the copyright line — holder name and year — which is part of the licence text.** 🔵 **So bytes CORROBORATE an identity; they never establish one.** 🟢 `P859`'s regression cases (`OpenTutor` **1 068 B**, `aureuserp` **1 077 B**) were the first two sightings of this; six more in one pass settles it.

🟢 **`P877` — and this is the sharper half: a byte count OUTSIDE the canonical value can mean a NON-NORMATIVE section was stripped, not that the licence differs.** 🔴 Measured on [`sagefy/sagefy`](https://github.com/sagefy/sagefy): `LICENSE.txt` is **10 174 B** against Apache-2.0's canonical **11 358** — a **1 184-byte** shortfall that looks like a different licence. 🟢 **It is not.** The title block reads `Apache License / Version 2.0, January 2004`, `Grant of Copyright License` is present, and the file ends on `END OF TERMS AND CONDITIONS`; 🟢 **what is missing is the `APPENDIX` — 0 occurrences — the non-normative *"How to apply the License to your work"* boilerplate.** 🔴 **The grant is complete Apache-2.0; only the instructions for reusing the licence were cut.** 🔵 A byte-identity gate marks this unrecognised and the row is lost.

---

## 🟢 Seventy-ninth pass, 2026-10-09 — **three new foundational repos, and the shelf had the BINDING without the ENGINE for 79 passes**

⏱️ **Eleventh pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔴 The finding first: this shelf shipped a pattern on `py-fsrs` and never recorded what `py-fsrs` is a binding TO

🟢 **Measured, not inherited:** `compose/patterns.md` line ~14377 already builds on *"`py-fsrs` (MIT, el algoritmo moderno que reemplaza SM-2)"*. 🟢 That claim re-verified live this pass: **`py-fsrs` is MIT, 1 079 B**. 🔴 **But the engine Anki actually embeds is `fsrs-rs`, it is BSD-3-Clause, and it has never appeared on this shelf** — 0 occurrences across `agents/`, `repos/`, `verticals/`, `intel/`, `compose/`.

| repo | grant (payload-read inline) | bytes | ref | role |
|---|---|---|---|---|
| 🟢 🆕 [`open-spaced-repetition/fsrs-rs`](https://github.com/open-spaced-repetition/fsrs-rs) | 🟢 **BSD-3-Clause** | 1 509 | `main` · `0a57374` | **The FSRS engine in Rust** — the implementation Anki ships natively. This is the thing to vendor. |
| 🟢 🆕 [`open-spaced-repetition/fsrs-optimizer`](https://github.com/open-spaced-repetition/fsrs-optimizer) | 🟢 **BSD-3-Clause** | 1 509 | `main` · `ac2a82d` | **Parameter optimiser** — fits FSRS weights to a specific learner population's review log. The part that makes retention scheduling *yours* rather than generic. |
| 🟢 🆕 [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | 1 079 | `main` · `ff7c85c` | Reference scheduler + the algorithm's documentation home (**4.1k★**). |
| 🟡 already shelved | 🟢 **MIT** | 1 079 | `main` · `9446cb0` | [`py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs) — the Python binding the shelf already uses. |

### 🔴 🆕 A licence-family split INSIDE one organisation — and it changes the obligation, not just the label

🔵 **MIT** (`fsrs4anki`, `py-fsrs`) and 🔵 **BSD-3-Clause** (`fsrs-rs`, `fsrs-optimizer`) are both permissive and both in Globant's buildable set. 🔴 **They are not the same obligation:** BSD-3's third clause is the **no-endorsement** term — *the names of the copyright holder and contributors may not be used to promote derived products without written permission*. 🟢 **Operationally:** vendoring `fsrs-optimizer` into a client deliverable means the client's marketing may **not** say "powered by FSRS / open-spaced-repetition" without asking first. MIT carries no such restriction. 🔵 **This is exactly the distinction a single "permissive ✅" column erases**, which is why this shelf records the family and the bytes, not a tick.

### 🟡 And a correctness note on `fsrs4anki`, because the topic blurb is now stale

🔴 **GitHub's `ai-tutor` topic describes `fsrs4anki` as "a modern spaced-repetition scheduler for Anki" — as though you install it.** 🟢 **Read from the repo's own README this pass:** *"If you are using **Anki 23.10 or newer**, refer to this section of the Anki manual"*, and *"setting up FSRS is much easier in Anki 23.10 or newer"* — 🟢 **FSRS has been NATIVE in Anki since 23.10.** The standalone custom scheduler is the legacy path. 🔵 **So the foundational asset here is the ALGORITHM and its optimiser, not the Anki add-on** — which is precisely why `fsrs-rs` and `fsrs-optimizer` are the two rows that matter above.

🟢 **Provenance, from artefacts (`P800`):** the README credits **[墨墨背单词 (MaiMemo)](https://www.maimemo.com/)** for supporting FSRS development by allowing its research engineer **Jarrett Ye** to work on it, and the algorithm's two papers are MaiMemo papers (ACM KDD 2022, `10.1145/3534678.3539081`). 🟡 **Research origin is APAC (China); project governance is Global** — 32 credited contributors under an all-contributors table, no single institution. 🔴 **Recorded as Global with the APAC research origin stated, rather than forced into one bucket.**

### 🟢 One institutional platform repo added, and it is the shelf's first deployed-infrastructure row from EMEA

| repo | grant | bytes | ref | region |
|---|---|---|---|---|
| 🟢 🆕 [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 **Apache-2.0** | 10 785 | 🔴 **`dev`** · `072e646` | 🟢 **EMEA** (Germany) |

🔴 **T1 paid here:** its default branch is **`dev`**, not `main` — a hardcoded `main` records this repository as ungranted. 🟢 It ships a **Helm chart published on Artifact Hub**, a CI workflow and codecov gating: this is university-operated infrastructure, not a demo. 🟢 **Region from the payload itself:** *"Copyright 2021 Technische Hochschule Mittelhessen"*, the holder named inside the grant.

## 🟢 Seventy-eighth pass, 2026-10-09 — **one new foundational repo and a permissive voice substrate**, plus the pass's own subject: 🔴 **`P859`, where this repository's retroactive byte correction was applied as a rule and got 6 of 8**

⏱️ **Tenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 Added to the foundations tier — the **real-time voice** layer, which this shelf had empty

🔵 This shelf has carried tutoring logic, knowledge tracing, LMS substrates and LTI libraries. 🔴 **It had no voice substrate**, although every tutoring row on it describes a spoken interaction. 🟢 The pass's new agent row arrives on one, and the substrate is permissive.

| repo | grant, by **payload read** | bytes | ref | why it is foundational |
|---|---|---|---|---|
| [`livekit/agents`](https://github.com/livekit/agents) | 🟢 **Apache-2.0** | 11 357 | `main` `dbe555b` | Agent runtime for real-time voice: WebRTC rooms, server-side turn detection, STT → LLM(+tools) → TTS pipeline, VAD interruptions. Node and Python |
| [`livekit/components-js`](https://github.com/livekit/components-js) | 🟢 **Apache-2.0** | 11 357 | `main` `1ce6ca0` | The React component layer (`@livekit/components-react`). 🟡 **The npm scope is not the repo slug** — `P840`/`P791` |
| [`livekit/client-sdk-js`](https://github.com/livekit/client-sdk-js) | 🟢 **Apache-2.0** | 10 142 | `main` `20e478d` | Browser client (`livekit-client`) |
| [`KaTeX/KaTeX`](https://github.com/KaTeX/KaTeX) | 🟢 **MIT** | 1 107 | `main` `6ea2dc9` | Maths rendering — the on-screen chalkboard half of a spoken maths tutor |
| [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent) | 🟢 **MIT** | 1 103 | `main` `987f310` | 🟢 The worked reference: a pt-BR maths tutor assembled from the four rows above. LATAM |

🔴 **What the tier still lacks:** the pipeline above is permissive **code** calling a **hosted inference service** (LiveKit Inference: `google/gemini-3.5-flash`, `xai/tts-1`). 🔵 **`P26` — copyright is not access.** 🟢 A self-hosted substitution (local STT, a local LLM, a local TTS) is the first step of `R78a` in `compose/patterns.md`, and 🔴 **it has not been measured here** — nobody on this shelf has run that swap.

### 🔴 🆕 `P859` — the retroactive byte correction, re-measured row by row

🟢 Pass 74 adopted `P834` and then added **one byte to a list of eight figures at once**. 🟢 All eight were re-read first-hand this pass, byte-exact on the file, with each payload's trailing-newline run measured separately. 🔴 **Six correct, two wrong:**

🔴 `zijinz456/OpenTutor` → 🟢 **1 068 B** (shelf: 1 069). **Corrected twice** — pass 64's `P724` had already re-read it byte-exact at 1 068 B, and the batch added a byte to a figure that was already right. 🔴 This file carried **1 069** at line ~304 and **1 068** at line ~1 799, both about the same payload.
🔴 `aureuserp/aureuserp` → 🟢 **1 077 B** (shelf: 1 078). Its **trailing-newline run is 0**, so the stripped capture and the exact size are the same number and the correction's magnitude was **zero**.
🟢 Correct: `ofbiz` 11 906 · Huly 14 197 · `DeepTutor` 11 408 · `iblai/os` 1 070 · `iblai/lms` 1 063 · `openeducat` 8 241.

🔵 **The rule, stated so a list cannot be corrected again:** 🔴 **`P834`'s magnitude is per-FILE** (the length of that payload's trailing newline run — `lib/README.md` records it measured at 0/1/3 bytes), 🔴 **and its applicability is per-ROW** (whether that figure was already byte-exact). 🟢 **Neither is readable off a list.** 🔵 Shape: `P713` in the **correcting** direction — the rule was re-measured and the rows it applied to were **inherited**.

### 🔴 🆕 `P862` — the shared probe's filename ladder is all-uppercase, and `raw` is case-sensitive

🟢 Control, one repo and one ref: on `frappe/erpnext` @ `develop`, every name in `PROBE_NAMES` plus three more returns 🔴 **404**, and 🟢 **`license.txt` returns 200**. 🔴 **So the versioned ladder would report the most-deployed open-source ERP as `NO-PAYLOAD`.**

🟢 **Payload:** **GPL-3.0, 35 149 B**, `develop` `2e6b8ed`. 🟢 **And a live `P171` case** — the body says `affero` **3 times**; the title block says `GNU GENERAL PUBLIC LICENSE`. 🔵 The defect `license_family.sh` was written for, met in the wild on a repository this shelf has reason to cite.

🔴 **Fix named and deliberately not written** (`P126`, and `P860`: nothing here could be executed): add the lowercase forms to `PROBE_NAMES` and pin `frappe/erpnext` as the regression case.

### 🔴 Nothing new from the mandated foundations channel, and that is now a six-pass number

🟢 `open source platform education ERP CRM MIT Apache` ran in full. 🔴 **It returned no education-specific repository under MIT, Apache-2.0 or BSD — for the sixth consecutive pass.** 🟢 Its MIT hits were **general** business software, and 🔴 **two of the three are one vendor**: Krayin CRM (**MIT**, 1 078 B, `2.2` `fa4eeca`) and Aureus ERP (**MIT**, 1 077 B, `master` `070cacc`) both carry `Copyright 2010-2025, Webkul Software`. 🔴 Apache OFBiz (**Apache-2.0**, 11 906 B, `trunk` `3b63151`) is a general ERP framework with no education module; Huly is 🔴 **EPL-2.0** (14 197 B), not the Apache-2.0 the channel asserted again.

🟢 **The band that holds** is unchanged and is restated because this pass re-confirmed it byte-exact: [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) **LGPL-3.0, 8 241 B**, `19.0` `1c95cef` — 🟢 **the only weak-copyleft education substrate on this shelf**, and therefore the only one where a Globant addon may stay proprietary (`P750`).

### 🔴 🆕 `P864` — three slugs for one ERP, and one of them is dead

🟢 `openeducat/openeducat_erp` → **`19.0`**; `OpenEduCat/openeducat_erp` → **`19.0`** (owners are case-insensitive); 🔴 **`OpenEduCat-Inc/OpenEduCat` → UNRESOLVED.** 🔴 The dead one is the slug carried by the sibling shelf at `globant-kb/education/verticals/solutions.md:13`, a **v6 snapshot dated 2026-07-14**.

🔵 **And it surfaced the way `P861` predicts:** `raw` served the dead slug a **14-byte body reading `404: Not Found`**, which the hand-rolled read reported as a *payload* until the control caught it. 🟢 `lib/probe_payload.sh` guards that case in its own source — and could not be run.

### 🟢 Declared gaps

🔴 **`Gap 333` (🆕):** no instrument in `compose/code/` executed this pass, offline suites included.
🔴 **Still zero MIT / Apache-2.0 / BSD education system-of-record.** `Ed-Fi DMS` (Apache-2.0) remains the only permissive substrate and is a data-standard API (`Gap 309`).
🔴 **The self-hosted voice swap is unmeasured** — nobody here has replaced LiveKit Inference with local STT/LLM/TTS and reported latency.


## 🟢 Seventy-seventh pass, 2026-10-09 — the newly-bought `/trending` channel adds **8 permissive teaching repositories**, and the ninth one found **`P854`: the shelf's shared classifier invented commercial permission over a NonCommercial work**. 🆕 `Gap 332` opens on the limit that survives the fix

⏱️ **Ninth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 Added to the foundations tier — the **teaching-materials** layer, which this shelf had thin

🔵 These are not agents and are not frameworks. They are the **curriculum substrate** a studio builds a course engagement on, and all eight are permissive and payload-verified.

| repo | family | why it is foundational here |
|---|---|---|
| [`ageron/handson-mlp`](https://github.com/ageron/handson-mlp) | 🟢 **Apache-2.0** | the fullest permissive ML/DL notebook sequence; patent grant makes it the safest of the eight for a client deliverable |
| [`rasbt/machine-learning-book`](https://github.com/rasbt/machine-learning-book) | 🟢 **MIT** | textbook code, PyTorch + Scikit-Learn, holder-dated **2021-2026** (actively maintained) |
| [`guipsamora/pandas_exercises`](https://github.com/guipsamora/pandas_exercises) | 🟢 **BSD** (3-Clause) | a ready **graded exercise bank** — the asset type `P533`'s QTI3 emitter consumes |
| [`ed-donner/agents`](https://github.com/ed-donner/agents) | 🟢 **MIT** | a complete agentic-engineering curriculum; the teaching counterpart to the framework tier |
| [`ed-donner/llm_engineering`](https://github.com/ed-donner/llm_engineering) | 🟢 **MIT** | same author, LLM-engineering track |
| [`jamwithai/production-agentic-rag-course`](https://github.com/jamwithai/production-agentic-rag-course) | 🟢 **MIT** | production RAG curriculum; already shelved, **grant now payload-read** |
| [`anthropics/claude-cookbooks`](https://github.com/anthropics/claude-cookbooks) | 🟢 **MIT** | recipe notebooks, usable as lab material |
| [`wesm/pydata-book`](https://github.com/wesm/pydata-book) | 🟡 **MIT-SCOPED** | textbook code — **the grant covers the code examples only** (below) |

🟡 **`wesm/pydata-book` is recorded `MIT-SCOPED`, never bare `MIT`.** 🟢 `COPYING` opens *"Code examples from "Python for Data Analysis", 3rd Edition"* and then gives MIT. 🔴 **The prose of the book is O'Reilly's and is not granted.** 🔵 `P784`/`P322` again: the grant's **subject line** is as operative as its family, and a studio reusing *"the book"* takes what the grant never gave.

### 🔴 🆕 `P854` — **the hyphenated CC abbreviation lost its attributes, and then lost the commercial verdict**

🟢 **The artefact that exposed it:** [`xiaolai/the-craft-of-selfteaching`](https://github.com/xiaolai/the-craft-of-selfteaching), returned by the `jupyter-notebook` slice. 🟢 Ten grant filenames swept across `main` and `master` → **all 404**. 🟢 The only grant is README **line 83**: *"本书的版权协议为 [CC-BY-NC-ND license](https://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh)"*.

🔴 **Two chained defects, measured:**

**(1) The inner gate was stricter than the outer one.** 🟢 The CC branch is *entered* on `Creative Commons|creativecommons.org|CC BY|CC-BY` — the hyphen is accepted. 🔴 But the inner `if` that **emits** the attributes demanded `CC BY` with a **SPACE**, or the spelled-out `Attribution`. 🔴 **So the hyphenated sigla entered the branch, computed `nc`/`sa`/`nd` correctly, and then THREW THEM AWAY**, answering `CC-UNSPECIFIED`. 🔵 Three version channels (`P551`) sat just past that gate and were never reached — including canal 1, which reads `licenses/by-nc-nd/3.0` perfectly.

**(2) `CC-UNSPECIFIED` is a hole in `commercial_use_ok`.** 🔴 It falls to `CC-*|UNCLASSIFIED) : ;;` and then to a token-match on the **words** `non-commercial`/`noncommercial` — 🔴 **which a sigla does not contain.** 🟢 Verdict: **ALLOWED**, over a work whose own name says NonCommercial.

🔵 **This is the `P312` inversion surviving inside the branch `P312` and `P551` hardened**, and in the direction this base cannot afford: 🔴 `P308` over-restricts and costs an opportunity; **this invents permission and costs the deliverable.**

**(3) And the fix for (1) exposed a third.** 🔴 `BY..SA` required **exactly two** characters between `BY` and `SA`, and `-SA `/`-ND ` required a **trailing space**. 🔴 So `CC-BY-NC-SA-4.0` answered `CC-BY-NC-4.0` — **ShareAlike lost** — and `CC-BY-NC-ND-4.0` lost **NoDerivatives**. 🔵 **Losing ND declares that derivatives are permitted**: the `P845` direction, inside the same pass.

🟢 **Fixed, and the fix touches only the gate and the three attribute detectors** — no version channel and no attribute semantics changed, because those were already right and simply unreachable:

| payload | before | after |
|---|---|---|
| `CC-BY-NC-SA-4.0` | 🔴 `CC-UNSPECIFIED` / **ALLOWED** | 🟢 `CC-BY-NC-SA-4.0` / **PROHIBITED** |
| `CC-BY-NC-ND-4.0` | 🔴 `CC-UNSPECIFIED` / **ALLOWED** | 🟢 `CC-BY-NC-ND-4.0` / **PROHIBITED** |
| `CC-BY-SA-4.0` | 🔴 `CC-UNSPECIFIED` | 🟢 `CC-BY-SA-4.0` / ALLOWED (correct) |
| `CC-BY-ND-4.0` | 🔴 `CC-UNSPECIFIED` | 🟢 `CC-BY-ND-4.0` / ALLOWED (correct) |
| `licenses/by-nc-sa/4.0` URL only | 🔴 `CC-UNSPECIFIED` / **ALLOWED** | 🟢 `CC-BY-NC-SA-4.0` / **PROHIBITED** |
| `licenses/by-sa/3.0` URL only | 🔴 `CC-UNSPECIFIED` | 🟢 `CC-BY-SA-3.0` — 🔵 **version read, not stamped** (`P551` holds) |
| `CC BY-NC-SA 4.0` (spaced) | 🟢 `CC-BY-NC-SA-4.0` | 🟢 **unchanged** |
| MIT · Apache-2.0 · BSD · CC0 payloads | 🟢 correct | 🟢 **unchanged** |

🟢 **Regressed on the real payload**, `lib/fixtures-p854/cc-by-nc-nd-the-craft-of-selfteaching.README.md` (**5 869 B**, committed), with assertions that the fixture keeps **both** the sigla and the versioned URL — so the case cannot pass for the wrong reason.

🟢 **Every consumer re-run, not only the touched one:** `test_license_family.sh` **199/199** (was 178/178, **+21 cases**) · `p837` **27/27** · `p840` **37/37** · `p845` **55/55** · `p411` **11/11** · `mcp-allowlist-gateway` **34/34**.

🟢 **Blast radius bounded by measurement:** 🔴 **`CC-UNSPECIFIED` appears 0 times on the live shelf as a VERDICT** — measured `PRE`-write against pass 76's tree (`P428`). 🟡 **It appears 19 times `POST`-write, in 6 files, and every one is this pass's own prose DESCRIBING the defect**, not a classification of an asset. 🔵 **The subject of the count is the distinction that matters:** a verdict is contamination, a description is the fix. 🟢 The 23 129 `CC-BY-4.0` rows are OpenStax content censuses (`p348`, `p326`) — **BY-only, no attribute to lose** — and the 52 `CC-BY-NC-SA-4.0` and 10 `CC-BY-NC-ND-4.0` rows were classified from **legal texts**, which spell the attributes out and always took the working path. 🔵 **Latent exactly like `P845`: no prior pass had ever fed this classifier an abbreviation.**

### 🆕 🔴 `Gap 332` — **OPENED.** The fix is correct and the artefact is **still** mis-verdicted, by a different mechanism

🔴 **Measured:** the **full** README still answers `UNCLASSIFIED`, and `commercial_use_ok` on it still answers **ALLOWED**.

🟢 **Mechanism, and it is not a defect:** the classifier reads a window of `head -c 4000` (line 106 — a limit **measured** by `P308`, not chosen). 🟢 The grant sits at byte **5495** of a **5869 B** file — **1 495 B outside the window.**

🔴 **Widening the window is forbidden, and the reason is on the shelf:** `P308`'s window exists because a payload that mentions CC far below was hijacking the verdict. 🟢 **So the missing instrument is a README-GRANT READER (`P742` class), not a bigger window.**

🟢 **Asserted as a test rather than a note**, including the **offset itself**, so the day the fixture or the window changes the case fails instead of passing for the wrong reason:
```
P854 README completo contesta UNCLASSIFIED (ventana P308)           ok
P854 la concesion del fixture cae FUERA de la ventana de 4000 B     ok
P854 Gap 332 el README completo AUN vuelve ALLOWED (NC invisible)   ok
```
🔵 **A repo with no grant file and a late README grant is, to every instrument this shelf owns, indistinguishable from an unlicensed repo** — and `commercial_use_ok` resolves that ambiguity in the permissive direction. 🔴 **That is `Gap 332`.**

## 🟢 Seventy-sixth pass, 2026-10-09 — `Gap 330`'s **PyPI limb CLOSES**, and the first PyPI payload this shelf ever read found **a defect in the shelf's own shared classifier**. The LTI 1.3 seam is now priced in **all three ecosystems**

⏱️ **Eighth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 The gap, restated so the closure can be checked against it

🔴 **`Gap 330` limb 2:** *"PyPI and Packagist payload reads remain unexercised — only resolution was run there."*

🟢 Pass 75 payload-verified the `ltijs` npm closure from inside each `.tgz`. 🔴 **The equivalent read for the other two ecosystems had never been taken**, so every PyPI and Packagist licence on this shelf was a **declaration**, not a payload (`P843`).

### 🟢 Shipped, split on the seam `P838` requires

| artefact | what it gives |
|---|---|
| `compose/code/lib/dist_payload.sh` | the network-free half: `licence_paths_in`, `notice_hits_in`, `measure_dist_dir`, `declared_from_pypi_json`, `declared_from_packagist_json`. 🟢 **No `grep` for a licence name anywhere in it** — every family verdict delegates to `license_family.sh`, so `P171` is inherited |
| `compose/code/lib/distpayload` | argument-invocable fetch half — `--pypi`, `--packagist`, `--closure-pypi`, `--dir`, `--self-test`; `--wheel`/`--sdist` selector. 🔴 **non-zero on any row that is not a resolved payload verdict** (`P827`) |
| `compose/code/p845-dist-payload/test_dist_payload.sh` | 🟢 **55/55**, offline, single file (`Gap 300`) — green from its own directory, from `/`, and via `--self-test` |

🟢 **The verdict vocabulary is the point of the instrument:** `PAYLOAD-<family>` · `NOTICE-ONLY` · `NO-NOTICE` (the `sprightly` class) · `NO-PAYLOAD` · `FETCH-REFUSED-<code>` · `UNEXTRACTABLE`.

### 🔴 `P841` bought a third time, and this time the defect was in the SHARED instrument

🔴 **The suite was 45/45 green and the first live run was still wrong — twice**, both within minutes:

**(1) The declared read missed PEP 639.** 🔴 `jwcrypto` 1.6.1 leaves the legacy `license` field **null**, ships **no** `License ::` classifier, and declares `license_expression: "LGPL-3.0-or-later"`. 🔴 **The reader answered `-`.** 🟢 **`-` is the one verdict a licence audit waves through**, so the error direction was *reassurance about a copyleft dependency*. 🟢 Fixed, moved into the library where it is testable offline, and pinned as regressions **H1–H9**.

**(2) The family read was wrong about Python itself, and this one is not my instrument.** 🔴 **`lib/license_family.sh` — the hardened, shared classifier that five-plus instruments consume — answers `0BSD` on Python's own `LICENSE`.**

| what | measured |
|---|---|
| payload | 🟢 `typing_extensions-4.16.0`, `dist-info/licenses/LICENSE`, **13 936 B**, read from the live wheel |
| classifier said | 🔴 **`0BSD`** |
| operative grant actually is | 🟢 **PSF License Version 2** |
| mechanism | 🔴 the 4 000 B title-block window holds **both** strings: line 63 *"Python Software Foundation License Version 2."*, line 67 *"and the Zero-Clause BSD license."*, line 73 the title *"PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2"*. 🔴 **With no PSF branch, the 0BSD branch matched first and returned** |
| what the 0BSD section really is | 🟢 line 267: *"ZERO-CLAUSE BSD LICENSE **FOR CODE IN THE PYTHON DOCUMENTATION**"* — a **subordinate** grant, scoped to the docs |
| error direction | 🔴 **less obligation than real**: 0BSD asks nothing; PSF-2.0 §2 asks for the PSF copyright notice **and** *"a brief summary of the changes made"* |

🟢 **This is `P171` exactly, in a family the hardening never covered.** 🔵 `P171` fixed *"a licence BODY names other licences"* by classifying on the **title block**. 🔴 **Necessary, not sufficient:** here the title block itself is *"A. HISTORY OF THE SOFTWARE"*, which names no licence at all, and the window reaches a **second, real grant** belonging to a different scope. 🟢 **A composite licence document must be classified on its OPERATIVE grant** — `P845`.

### 🟢 Fixed, carried to the consumer, and regressed on the REAL payload

🟢 **`PSF-2.0` branch added ahead of the 0BSD branch**, anchored on the *Version 2* title rather than the word "Python" — 🔵 **a legitimate 0BSD payload never names the PSF License Version 2, so the new branch cannot steal one.**

🟢 **`P562` discharged in the same pass:** `PSF-2.0` added to **`OSI_RECONOCIDAS`** *and* **`PERMISIVAS`** in `p411-cession-identity-gate/gate_cesion.py`, 🔵 **or that gate would reject as unknown a string its own library emits** — the same move `P613` made for `GPL-UNVERSIONED` and `Gap 256` for `LGPL-2.1`. 🟡 **Stated explicitly because it is a judgement, not a measurement:** PSF-2.0 is **non-reciprocal**, so it is permissive; it carries **one condition MIT does not** — the change summary — so a closure containing it is buildable with **one more row in the notices file**.

🟢 **The fixture is the real artefact, not an invention:** `lib/fixtures-p845/psf-2.0-typing-extensions-4.16.0.LICENSE`, **13 936 B**, with assertions that it stays un-truncated **and** keeps both the subordinate 0BSD heading and the PSF anchor — 🔵 **so a later edit cannot make the regression stop testing what it claims.**

🟢 **Every consumer re-run, not just the one I touched:**

| suite | result |
|---|---|
| `lib/test_license_family.sh` | 🟢 **178/178** |
| `p837-payload-measure` | 🟢 **27/27** |
| `p840-package-repo` | 🟢 **37/37** |
| `p411-cession-identity-gate` | 🟢 **11/11, TODO VERDE** |
| `p845-dist-payload` | 🟢 **55/55** |
| `mcp-allowlist-gateway` | 🟢 **34/34** |

🟢 **And the blast radius is bounded by measurement, not by hope:** 🔴 169 lines on this shelf mention `0BSD`; 🟢 **0 of them in a Python or PyPI context.** 🔵 **The defect sat in the instrument for many passes and contaminated nothing, because no pass had ever read a PyPI payload.** 🟢 **Which is `P841`'s argument stated forward: an unexercised branch is a latent defect, and it surfaced within four commands of first use.**

### 🟢 The measurement the gap was opened for: the LTI 1.3 seam in all three ecosystems

🟢 **`PyLTI1p3` 2.0.0 runtime closure, wheel, payload-read:**

| member | declared | payload path | bytes | family |
|---|---|---|---|---|
| `PyLTI1p3` | 🟢 MIT | `PyLTI1p3-2.0.0.dist-info/LICENSE` | **1 070** | 🟢 MIT |
| **`jwcrypto` 1.6.1** | 🔴 **LGPL-3.0-or-later** | `jwcrypto-1.6.1.dist-info/licenses/LICENSE` | **7 651** | 🔴 **LGPL-3.0** |
| `pyjwt` 2.15.1 | 🟢 MIT | `pyjwt-2.15.1.dist-info/licenses/LICENSE` | **1 085** | 🟢 MIT |
| `requests` 2.34.2 | 🟢 Apache-2.0 | `requests-2.34.2.dist-info/licenses/LICENSE` | **10 142** | 🟢 Apache-2.0 |
| `typing-extensions` 4.16.0 | 🟢 PSF-2.0 | `typing_extensions-4.16.0.dist-info/licenses/LICENSE` | **13 936** | 🟢 PSF-2.0 |

🟢 **Cross-channel agreement worth recording:** the root's payload reads **1 070 B, MIT, "Copyright (c) 2019 Dmitry Viskov"** — 🔵 **byte-for-byte what a prior pass read from the REPOSITORY.** 🟢 **Two independent channels, one number.**

🟢 **And wheel vs sdist AGREE for this package** — both ship the grant at 1 070 B (`dist-info/LICENSE` vs `PyLTI1p3-2.0.0/LICENSE`). 🔵 **Asked because npm's `files:` defect taught that one artefact can ship a grant the other drops**, and on PyPI there are two artefacts built by different code paths. 🟡 **One package is not a base rate**, but the question is now one flag away.

🟢 **PHP route, priced for the first time:**

| member | declared (Packagist) | payload | family |
|---|---|---|---|
| `packbackbooks/lti-1p3-tool` **v6.4.4** | 🟢 Apache-2.0 | `master/LICENSE.md` **11 343 B** | 🟢 Apache-2.0 |
| `firebase/php-jwt` **v7.2.1** | 🟢 BSD-3-Clause | **1 529 B** | 🟢 BSD |
| `guzzlehttp/guzzle` **8.2.0** | 🟢 MIT | **1 460 B** | 🟢 MIT |
| `phpseclib/phpseclib` **4.0.2** | 🟢 MIT | **1 081 B** | 🟢 MIT |

🟢 **4 of 4 permissive, and declared == payload on every one.** 🟢 **The root's 11 343 B matches this shelf's existing record exactly** (`P839`/`P835` applied before writing: `packbackbooks` has **96** prior mentions, so the root grant is a **re-confirmation**, not a finding).

🆕 **What IS new here, measured against a 0-occurrence census:** 🔴 **`guzzle` 0 · `phpseclib` 0 · `php-jwt` 0 · `googleapis/php-jwt` 0.** 🟢 **The shelf held the root grant for many passes and had never priced what the library pulls in.**

🟡 **One provenance datum:** `firebase/php-jwt` resolves to **`googleapis/php-jwt`**. 🔵 **The package name says Firebase; the repository says Google.**

🟢 **And the AGS claim is now evidence instead of prose.** 🔵 This shelf has carried *"Names&Roles + Assignment&Grades"* about this library without enumerating it. 🟢 **Read at the pinned `a20c71b7`:** **11** public AGS methods (`createLineitem`, `putGrade`, `getGrades`, `findOrCreateLineitem`, `updateLineitem`, `deleteLineitem`, `getLineItems`, `getLineItem`, `findLineItem`, `getResourceLaunchLineItem`, `getScope`) and **all four** IMS AGS scopes — `lineitem`, `lineitem.readonly`, `result.readonly`, `score`. 🔴 **`lti-ags/scope` had 0 prior occurrences on this shelf.**

### 🔴 The Packagist limb does NOT close, and the mechanism is named rather than guessed

🔴 **`Gap 331` opens.** 🟢 **Measured:** Packagist's `dist.url` for `packbackbooks/lti-1p3-tool` is `https://api.github.com/repos/packbackbooks/lti-1-3-php-library/zipball/a20c71b7…`, which this session answers **403** with a first-party body: *"GitHub access to this repository is not enabled for this session."*

🟢 **That is `P844` mechanism #2 — SESSION SCOPE, not a gateway denial and not a classifier refusal.** 🔵 **The instrument was changed because of it:** a bare `UNEXTRACTABLE` reads as *"the archive is corrupt"* and would have **blamed the artefact for an access boundary**. 🟢 **Now the row says `FETCH-REFUSED-403` and carries the URL** — `P847`.

🟡 **So the PHP grants above were read at the PINNED COMMIT via `raw.githubusercontent.com` (open, 200), which is a REPOSITORY read, not a published-distribution read.** 🟢 **`P843` requires naming which measurement was taken, and this is the weaker one** — it proves the grant exists at the exact ref the dist pins, 🔴 **not that the published zip contains it.**

🔴 **And one self-inflicted trap, recorded because it nearly became data:** probing `LICENSE`, `LICENSE.md` and `COPYING` in a loop wrote **all three** response bodies to files. 🔴 **`LICENSE` 404'd, and its 14-byte body `404: Not Found` measured as a payload** — `UNCLASSIFIED`, 14 B. 🟢 **The real grant is `LICENSE.md`.** 🔵 **A 404 body written to a file is indistinguishable from a tiny licence unless the status is checked**, which is the same lesson as `P847` arriving from the other direction.

## 🟢 Seventy-fifth pass, 2026-10-09 — **`Gap 316(i)`'s licence limb is PRICED from payload**: the `ltijs` runtime closure is **10 packages, 9 payload-verified MIT under an Apache-2.0 root, and 1 assertion without a grant**. The third instance of `Gap 312`/`325` on this shelf, and the first found **mechanically**

⏱️ **Seventh pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 Why this number existed to be taken

🟢 This shelf has called [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) *"the library that would close"* `Gap 316`'s LTI 1.3 + AGS seam for five consecutive passes, and `Gap 316(i)` — **the real wiring cost** — *"the highest-value unmeasured number on this shelf."* 🔴 **What no pass had taken is the cheaper half of that number: what the dependency closure LICENSES.** 🟢 **`Gap 329`'s closure this pass (`lib/pkgrepo`, below) made it a single command**, and `73-C`'s `PyMuPDF` finding — an Apache-2.0 root over an AGPL-or-commercial core dependency, caught **by hand** — is exactly the hazard it had to be checked for.

### 🟢 The root grant, read from the artefact that actually ships

| what | measured |
|---|---|
| npm artefact | 🟢 `ltijs@7.0.7`, tarball `ltijs-7.0.7.tgz` |
| declared licence | 🟢 `Apache-2.0` |
| **payload** `LICENSE` | 🟢 **11 361 B**, family **`Apache-2.0`** by `P171` (`lib/measure --family`) |
| runtime dependencies | 🟢 **10** |
| `engines.node` | 🔴 **`">=24"`** — re-confirmed in the npm artefact, not just the git tree |

### 🟢 The closure, all ten, declared **and** payload-verified

🔵 **Both columns are taken because they are different facts.** The registry `license` field is a **declaration in metadata**; a `LICENSE` file inside the tarball is **the grant that travels with the installed artefact**. 🟢 This shelf's own `Gap 312`/`Gap 325` exist precisely because the first can be present while the second is absent.

| package | declared | payload file | bytes | family (`P171`) |
|---|---|---|---|---|
| [`expressjs/cors`](https://github.com/expressjs/cors) | MIT | `LICENSE` | 1 095 | 🟢 MIT |
| [`debug-js/debug`](https://github.com/debug-js/debug) | MIT | `LICENSE` | 1 139 | 🟢 MIT |
| [`expressjs/express`](https://github.com/expressjs/express) | MIT | `LICENSE` | 1 249 | 🟢 MIT |
| [`helmetjs/helmet`](https://github.com/helmetjs/helmet) | MIT | `LICENSE` | 1 089 | 🟢 MIT |
| [`redis/ioredis`](https://github.com/redis/ioredis) | MIT | `LICENSE` | 1 080 | 🟢 MIT |
| [`auth0/node-jsonwebtoken`](https://github.com/auth0/node-jsonwebtoken) | MIT | `LICENSE` | 1 121 | 🟢 MIT |
| [`Automattic/mongoose`](https://github.com/Automattic/mongoose) | MIT | `LICENSE.md` | 1 130 | 🟢 MIT |
| [`thlorenz/parse-link-header`](https://github.com/thlorenz/parse-link-header) | MIT | `LICENSE` | 1 078 | 🟢 MIT |
| [`obadakhalili/sprightly`](https://github.com/obadakhalili/sprightly) | MIT | 🔴 **none** | — | 🔴 **ASSERTION-ONLY** |
| [`colinhacks/zod`](https://github.com/colinhacks/zod) | MIT | `LICENSE` | 1 072 | 🟢 MIT |

🟢 **So the answer `Gap 316(i)`'s licence limb was waiting for is good, and it is the opposite of the `PyMuPDF` case: no copyleft anywhere in the closure, no `NON-GITHUB` member, no sourceless member.** 🟢 **Nine of ten carry their grant in the shipped artefact.**

### 🔴 The exception, and it is worse than a missing file

🟡 `sprightly@2.0.1` is a 100-line template renderer — the kind of dependency nobody reads. 🔴 **Measured in its tarball:**

| what | measured |
|---|---|
| `package.json` `license` | 🟢 `"MIT"` |
| `files` | 🔴 `["dist"]` |
| files shipped | **8** — `README.md`, `package.json`, `dist/*` |
| `LICENSE` / `COPYING` | 🔴 **absent** |
| any shipped file carrying a copyright notice | 🔴 **none** — `grep -rliE "copyright\|MIT License"` returns **0 files** |

🔴 **The consequence is not cosmetic.** The MIT licence's own operative sentence requires that *"the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."* 🔴 **The published artefact contains neither notice**, so a client redistributing it cannot satisfy the condition of the licence it is relying on — 🔵 **not because the grant is withheld, but because the text that constitutes it was never packaged.**

🟢 **And the mechanism is an idiom this shelf had already flagged for a different reason:** `files: ["dist"]`. 🔵 **Caution (b) below records that same field on `ltijs` as a *build* hazard. This is the same field with a *licence* consequence**, and `sprightly` is the member of the closure where it bites.

🟢 **Remedy, cheap and external, identical in shape to `Gap 325`:** ask upstream to add `LICENSE` and include it in `files`. 🟡 **Interim, and this is what a client engagement should actually do:** vendor the notice from the repository into the deployment's third-party notices file, and pin `sprightly@2.0.1`.

### 🟢 **RESOLVED within this same pass — the grant exists upstream, so this is a packaging bug and not a counsel question**

🔴 **This section was first written as an unmeasured limit**, on the shelf's standing record that `raw.githubusercontent.com` payload reads are refused in this environment. 🟢 **That record is out of date for this session: the channel answers 200** (see `intel/open-gaps.md`, `P844`). 🟢 **So the question was asked rather than deferred, and it has the better answer:**

| probe | result |
|---|---|
| `obadakhalili/sprightly` `main/LICENSE` | 🟢 **HTTP 200 · 1 070 B** |
| first lines | 🟢 `MIT License` / `Copyright (c) 2024 Obada Khalili` |
| family (`lib/measure --family`, `P171`) | 🟢 **MIT** |
| `main/package.json` `files` | 🔴 **`["dist"]`** — unchanged from the published artefact |

🟢 **The grant is real, it is MIT, it is attributable to a named holder, and it is in the repository.** 🔴 **It is simply not in the tarball**, because `files: ["dist"]` excludes it. 🟢 **So the verdict moves from "assertion without a grant" to a strictly better category: a grant that exists and is not packaged.**

🔵 **Which is the distinction this section said was commercially decisive, now settled in the cheap direction:**

| if | then |
|---|---|
| the grant existed nowhere | 🔴 a counsel question before any client ships it |
| 🟢 **the grant exists and is unpackaged** | 🟢 **a one-line upstream PR, and a notices-file entry in the interim** |

🟢 **Remedy, now exact:** upstream, add `"LICENSE"` to `files` (npm includes `LICENSE` automatically in most toolchains, which is why this is easy to miss when an explicit allowlist is set). 🟢 **Interim, and quotable in an SOW:** vendor the notice verbatim — **`MIT License · Copyright (c) 2024 Obada Khalili`** — into the deployment's third-party notices file, and pin `sprightly@2.0.1`.

🟡 **What this does NOT change:** the deployed artefact still carries no notice, so a client that ships it without the vendored entry is still out of compliance with the licence it relies on. 🟢 **The defect is real; only its remedy got cheaper.** 🔵 **And `Gap 312`/`Gap 325` are now distinguishable from it by evidence rather than by assumption** — `frappe/education` and `ec-issuer` have no grant *found*; `sprightly` has one *measured*.

### 🟢 A clarification to caution (b) below, not a correction

🔵 Caution (b) records `"files": ["dist"]` with `main: dist/index.js` on `ltijs`. 🟢 **Measured in the npm `7.0.7` artefact this pass:** `files` is 🟢 **`null`**, `main` is 🟢 **`"index.js"`**, and the tarball ships a flat `index.js`, `index.d.ts`, `index.js.map`, `README.md` **and `LICENSE`**. 🟢 **Both readings are true of different objects** — caution (b) describes the **git tree**, this describes the **published artefact** — and the difference *is* caution (c)'s point, that npm is ahead of the tagged history. 🟢 **So caution (b) is hereby scoped to a git-dependency install, which is exactly the install its own remedy tells you not to do**, and 🟢 **the npm artefact is now measured clean and complete, which makes "install from npm, not from GitHub" an instruction with a measurement under it.**

## 🟢 Seventy-fourth pass, 2026-10-09 — **no repository row is added**; the pass's foundation contribution is an **instrument**, and the LMS licence wall is re-confirmed from an independent channel: 🔴 **0 of 6 platforms permissive**

⏱️ **Sixth pass of this date.** Pass 73 and its correction `73-C` closed earlier today (commit `7ce7b79`). **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `P835` first, per `73-C`. Seventeen candidates, seventeen already here

🔴 **Every repository the prescribed battery returned is already on this shelf** — `DeepTutor` (24 files), `Open-TutorAi` (18), `ChatTutor` (13), `tutor-gpt` (10), `Study-Mate` (10), `freelingo` (8), `500-AI-Agents-Projects` (7), `ai-agents-for-beginners` (9), `classroomio` (20), `Frappe LMS` (11), `Sakai` (22), and the rest. 🟢 **Nothing is added and nothing is padded in to reach a minimum count.** 🔵 **The minimum-five rule exists to stop thin passes, not to license duplicate rows — and `73-C` is this shelf's proof that a count met with duplicates costs more than an honest zero.**

### 🆕 The one foundation this pass does add: `lib/payload_measure.sh`

🟢 **A foundational repo for this shelf is not only something to build a product on — it is something every later pass depends on.** By that test this pass adds one, and it is internal:

| Component | Licence | What it gives |
|---|---|---|
| `compose/code/lib/payload_measure.sh` | this repo | 🟢 `size_of_file` (byte-exact, `P834`-proof), `trailing_newlines`, `family_of_file` / `holder_of_file` (delegate to `license_family.sh`, so `P171` is inherited not re-implemented), `count_word_in_file` / `count_word_in_pathlist` (`P831`-proof), `measure_payload_file` → the same six-field TSV as `probe_repo` |
| `compose/code/lib/measure` | this repo | 🟢 argument-invocable front end: `--size`, `--newlines`, `--family`, `--count`, `--self-test`. **Exits non-zero on a missing payload** rather than printing `0` |
| `compose/code/p837-payload-measure/` | this repo | 🟢 **27/27 offline**. Runs in this environment, which `lib/test_probe_payload.sh` does not |

🔴 **It exists because the shelf's own probe was wrong.** `lib/probe_payload.sh` did `body=$(_raw …)` then `printf '%s' "$body" | wc -c`, and `$(…)` strips the trailing newline run — so 🔴 **every byte count the shared probe ever emitted for a newline-terminated payload is low by that run.** 🟢 Fixed; `_row_from_fetch` sizes the payload where it landed on disk.

⚠️ **Honest scope on the fix:** the fetch branch is 🔴 **unexecuted** — `curl` is refused in this environment. It is `bash -n` clean and its sizing, classifying and counting primitives are asserted 27/27, 🟢 **but no live repository passed through it this pass.** The first pass with network should run `test_probe_payload.sh` and **expect every byte count to return one byte higher** than the shelf's historical figure. 🔵 **That shift is the fix landing, not a new defect.**

### 🔴 The LMS licence wall, re-confirmed on an independent channel — and it did not move

🟢 **`Gap 316`'s licence half re-probed this pass through a different channel than the ones that established it.** 🔴 **Of every LMS/SIS platform the channel named, not one is MIT, Apache-2.0 or BSD:**

| Platform | Licence reported | 🔴 Permissive? |
|---|---|---|
| Moodle | **GPL-3.0** | 🔴 no |
| Canvas LMS (Instructure) | **AGPL** | 🔴 no |
| Open edX | **AGPL-3.0** | 🔴 no |
| Frappe LMS | **AGPL-3.0** | 🔴 no |
| OpenEduCat | **LGPL-3.0** | 🟡 weak copyleft — proprietary extensions permitted |
| Sakai | **ECL-2.0** | 🟡 Apache-derived, educational-community variant |

🔴 **Six platforms, zero permissive.** 🟢 **This is now a four-channel finding and the most stable thing on this shelf.** 🔵 **Read together with last pass's measurement — `DeepTutor` (Apache-2.0) and `OpenTutor` (MIT) hold zero LTI/xAPI/Caliper/SCORM/OneRoster paths between them — the seam is confirmed two-sided: the platforms that speak the protocols are all copyleft, and the permissive tutors do not reach for the protocols at all.**

🟡 **`classroomio` was named again by this channel with an AI-tutor claim and no licence.** 🔴 **Already shelved (20 files) and its licence is not re-asserted here from a secondary source** — the channel that named it also reported the EU Digital Omnibus as unpublished, which this shelf knows to be false. 🟢 **Recorded as a payload re-read for the first pass with network, not as a finding.**

## 🔴 Seventy-third pass, **correction (73-C)**, 2026-10-09 — the rows this file added were **already on this shelf**, and one build-on recommendation was published without its licence caveat

🔴 **`HKUDS/DeepTutor` and `zijinz456/OpenTutor` were already shelved before pass 73.** 🟢 Read the section below as a re-measurement. 🟡 Every byte count in it is **one byte low** (`P834`): `OpenTutor` MIT is **1 069 B**, `aureuserp` **1 078 B**, `ofbiz` **11 906 B**, `DeepTutor` **11 408 B**.

### 🔴 The omission that matters: `DeepTutor`'s dependency closure is **not** permissive

🔴 The section below calls `DeepTutor` *"Apache-2.0, so it can be carried."* 🟢 **This shelf has recorded since 2026-10-06 that `PyMuPDF>=1.26.0` is in its core dependency array, dual-licensed 🔴 *AGPL-3.0 or Artifex Commercial*, shelf verdict REVIEW-STRONG: "AGPL, or pay Artifex, or replace the PDF layer."**

🟢 **Corrected recommendation:** `DeepTutor` remains the strongest permissive tutoring foundation on this shelf **and** adopting it is a three-way decision on the PDF layer, not a free carry. 🔵 **A probe that reads `LICENSE` and stops cannot see this**, which is the same blind spot `Gap 327` names from the other side (permissive grant, no source) — here it is permissive grant, copyleft closure.

🟢 **Genuinely new and unaffected:** the `iblai` "permissive but sourceless" tier, `P832`, and `DeepTutor`'s **0-of-6** protocol census across 3 763 files.

## 🟢 Seventy-third pass, 2026-10-09 — the foundation layer gains a **multi-tenant tutoring runtime**, and a new rule for reading a licence off a package instead of a repository

⏱️ **Fifth pass of this date.** Pass 72 closed earlier today (commit `e99be83`). **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 Foundational repos added, every licence read from primary payload

| Repo | Licence (payload) | Default ref · HEAD · date | Scale | Why it is foundational |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** 11 407 B | `main` `6cf793bd` · **2026-10-08** | 🟢 **3 763 files**, **1 220 test files** | 🟢 Tutoring runtime **plus** a real multi-tenant access layer: `multi_user/{identity,grants,guardians,learner_profile,book_permission,knowledge_access,model_access,audit,device_credentials}.py`. Ships `compose.yaml`, `Dockerfile`, `pyproject.toml`, `CITATION.cff`, `THIRD_PARTY_NOTICES.md`, `.importlinter` |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** 1 068 B, holder *Zijin Zhang* | `main` `f0142f2` · **2026-10-08** | 890 files, 191 commits | Local-first adaptive workspace; 10+ LLM providers behind one interface |
| [`aureuserp/aureuserp`](https://github.com/aureuserp/aureuserp) | 🟢 **MIT** 1 077 B, holder *Webkul Software* | 🟡 **`master`** | — | 🟢 The only **permissive** ERP found in this pass's sweep; plugin architecture makes an education module additive rather than a fork |
| [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** 11 905 B | 🟡 **`trunk`** | — | Permissive ERP framework (accounting → CRM → MRP); 🔴 heavy Java implementation cost |

🟢 **`DeepTutor` is the most load-bearing addition this file has taken in several passes**, and the reason is `multi_user/`, not the tutoring. 🔵 **`guardians.py` + `learner_profile.py` + `audit.py` is the K-12 consent-and-oversight shape that every prior `P14-R` estimate on this shelf has had to price as greenfield work.** 🟢 **It is Apache-2.0, so it can be carried.**

🔴 **What `DeepTutor` does *not* have, and it is a hard zero:** no LTI, no xAPI, no Caliper, no SCORM, no OneRoster, no LMS path of any kind in 3 763 files. 🟢 **Censused word-bounded per `P831`.** 🟢 **So it is a foundation, not a drop-in: the LMS seam is supplied by `ltijs` and is the integration `P14-R` budgets for.**

### 🟡 Admitted to the census but **not** to the build-on shortlist — the "permissive but sourceless" tier

| Component | Licence | Source available? |
|---|---|---|
| [`iblai/os`](https://github.com/iblai/os) | 🟢 **MIT** 1 069 B, holder *iBL Education* | 🟢 Yes — `main` `cd556237`, 1 516 files |
| `@iblai/iblai-js` 2.33.2 *(holds the LTI component)* | 🟢 **ISC** | 🔴 **No `repository` declared** |
| `@iblai/iblai-api` 4.421.0-ai | 🟢 **ISC** | 🔴 **No `repository` declared** |
| `@iblai/iblai-web-mentor` 2.0.1 | 🟢 **MIT** | 🔴 Private SSH alias `git@ibl_connection:…` |
| ibl.ai backend (auth, agent APIs, data services) | 🔴 **Enterprise licence** | 🔴 **Not published** |

🟢 **`P832`, adopted this pass:** when a capability lives in a package rather than a repository, read the registry's **`repository`** field alongside its **`license`**. 🔴 **A permissive licence on an unfetchable artifact cannot be forked, audited or patched, and twice now it has nearly reached a build-on shortlist on the strength of the licence field alone.** 🟢 Full reasoning in `intel/open-gaps.md` `Gap 327`.

### 🟢 L&D curriculum shelf — carried from pass 72, unchanged

🟢 [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) (🟢 MIT, 1 141 B, `25b7985`) and [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) (🟢 MIT, 1 091 B, `da3f9df`) remain filed here as **L&D curriculum, not agents**. 🟢 This pass's control query returned the same category a third time (`microsoft/generative-ai-for-beginners`, `Bojieli/ai-agent-book`, `ai-engineering-from-scratch`). 🔴 **None is an agent deployed in an education setting; none is shelved as one.** 🟢 **`P826`, working as intended.**

## 🟢 Seventy-second pass, 2026-10-09 — the **credential layer gets a foundation row and it is a red one**: three Open Badges issuers, **zero clean permissive grants**. Two MIT L&D curricula added in their correct category

⏱️ **Fourth pass of this date.** Pass 71 closed earlier today (commit `1fe734a`). **Append-only: this section is new; nothing below it was rewritten.**

### 🔴 Digital credentials — censused, and there is no permissive foundation to build on (`Gap 324`)

🔵 **Why this matters here:** `intel/trends.md` has carried digital credentials as a live trend on two independent channels, and this shelf has never been able to name a permissive issuer. 🟢 **It now can name three issuers and must report that none of them is cleanly permissive.**

| Repo | Licence (read from payload) | Default ref · HEAD | Standards | ¿Base for AI? |
|---|---|---|---|---|
| [`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) | 🔴 **No `LICENSE` in a 141-file enumerated tree** · README §License asserts `MIT` | `main` `8bafc99` · 2026-08-28 | 🟢 **OB 3.0 + European Learner Model + OID4VCI** | 🔴 **Blocked on `Gap 325`** — no grant to rely on |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | 🔴 **AGPL-3.0** 33 820 B | `main` `6fd0a11` | OB 3.0 + W3C VC, Ed25519 | 🟡 Self-host for a client only |
| [`mint-o-badges/badgr-server`](https://github.com/mint-o-badges/badgr-server) | 🔴 **AGPL-3.0** 34 519 B | 🟡 **`develop`** `4c7080e` | 🔴 **OB 2.0** only | 🟡 Self-host for a client only |

🟢 **`ec-issuer` is the one worth watching**, because it is the only implementation covering **Open Badges 3.0, the European Learner Model and OID4VCI together** — relevant to any EMEA engagement touching learner mobility. Its tree: `templates/openbadge_credential_template.json`, `src/credential_configurations/` (7 modules including an SSI-agent client adapter), `tests/e2e/test_oid4vci.py`, committed Ed25519 issuer and holder keypairs, `docs/src/oidc4vci_issuer_agent.md`, and **53 of 141 files are tests**. 🔴 **And it ships no licence file.** 🟡 **Second instance of the `Gap 312` pattern** — pair the counsel question with `frappe/education`'s.

### 🟢 L&D curriculum — the right home for what the agent query keeps returning

🔵 **Recorded here, not in `agents/top.md`, and the distinction is deliberate.** These teach people to build agents; they are not agents deployed in an education setting. 🟢 **For a Globant upskilling or academy engagement they are genuinely the best permissive starting points available.**

| Repo | Licence (payload) | HEAD | Use |
|---|---|---|---|
| [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** 1 141 B | `25b7985` | 🟢 12-lesson agent curriculum — ready-made internal academy spine |
| [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | 🟢 **MIT** 1 091 B | `da3f9df` | 🟢 Agents from first principles on a **local LLM, no framework** — the sovereignty-friendly teaching track |

🔴 **Do not promote either into the agent layer.** 🟢 `P826` predicted this exact confusion and this pass observed it in output: the control query's "education" token selects *material about AI*, not *AI in teaching*.

### 🟢 LTI remains the seam, and the library remains the same

🟢 [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — **Apache-2.0**, `master` `0ec24fe` — re-verified this pass and still the only maintained permissive library implementing the full **LTI 1.3 + AGS** surface. 🟡 [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) — MIT, `master` `d8fa43e`, **still four years stale**; adopt only by owning the fork.

🔵 **Instrument note (`P829`):** file counts here were taken with `ls-tree -r HEAD --name-only` on blobless clones. 🔴 **`ls-files` reports `0` on a `--no-checkout` clone**, which would have published `ec-issuer` as an empty tree.

## 🟢 Seventy-first pass, 2026-10-09 — `Gap 316(i)` **ANSWERED**: the permissive tier's "LTI 1.3 ceiling" was never a protocol gap. **Two permissive LTI 1.3 + AGS libraries exist**, one Apache-2.0 and maintained three days ago, one MIT and complete but four years dead

⏱️ **Third pass of this date.** Pass 70 closed earlier today (commit `cf5c9bf`). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every licence below read as bytes from `raw.githubusercontent.com`; every HEAD from `git ls-remote --symref`; every tree from a blobless clone.**

### 🟢 The finding that changes the costing — **the 1.3 + AGS layer is solved, permissively, in both ecosystems**

🔵 **What this shelf has said for several passes:** the one real cross-LMS permissive component speaks **LTI 1.1 / Basic Outcomes**, nothing permissive speaks **1.3 + AGS**, and `Gap 316(i)` called the size of that port *"the most commercially urgent unmeasured number on this shelf."*

🔴 **The question was mis-framed.** 🟢 **It was never a protocol-implementation cost, because the protocol is already implemented under permissive licences:**

| Library | Licence (payload) | Head | LTI Advantage surface, read from the tree | Verdict |
|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** · `LICENSE` **11 361 B** (canonical text) · `package.json` `"license": "Apache-2.0"` | `master` **`0ec24fe`** · 🟢 **2026-10-06 — three days ago** | `src/services/`: 🟢 **`grading`** (AGS) · 🟢 **`deep-linking`** · 🟢 **`names-and-roles`** (NRPS) · 🟢 **`dynamic-registration`** · `launch` · `oidc` · `keyset` · `platform-manager` · `provider` · `request-handler` · `http-handler` · plus `shared/lti-scopes.constants.ts`. Infra: `cache-manager` (Redis + mock), `database-manager` (Mongo + mongo-legacy), `access-token-manager` | 🟢 **The recommended base.** Maintained, permissive, complete |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** · `LICENSE` 1 070 B | `master` **`d8fa43e`** · 🔴 **2022-11-21** | `pylti1p3/`: 🟢 **`assignments_grades.py`** (AGS) · **`grade.py`** · **`lineitem.py`** · **`deep_link.py`**, `deep_link_resource.py` · **`names_roles.py`** · `service_connector.py` · `message_validators/deep_link.py`. Tests: `test_grades.py`, `test_deep_link.py`, `test_names_roles.py` | 🟡 **Complete and permissive, but unmaintained for ~4 years.** Adopt only by owning the fork |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 **GPL-2.0** · `LICENSE` **18 025 B** | `develop` `d9d462a` | TAO's LTI 1.3 DevKit is **1EdTech-certified for AGS 2.0, dated 2026-01-15** | 🔴 **Copyleft — out for a closed deliverable.** Cited only as proof the certification path is live |

🟢 **`ltijs` v7.0.7 states it itself**, in `README.md`: *"implements a full LTI® 1.3 tool provider, including launches, Deep Linking, **Assignment and Grade Services**, Names and Role Provisioning, and Dynamic Registration, as a pluggable, TypeScript-first library."* 🟢 **And the tree corroborates the README rather than merely repeating it** — which is the standard this shelf applies to every other claim.

🟡 **Three operational cautions on `ltijs`, recorded now so nobody meets them in week two:** 🔴 **(a) `engines.node` is `">=24"`** — it will not run on a Node 20 LTS platform. 🔴 **(b) `"files": ["dist"]`** with `main: dist/index.js`, and `dist/` is **not committed** — so a git-dependency install has the same `prepublish` problem that produced the `ims-lti` fork (`Gap 319`); 🟢 **install from npm, not from GitHub.** 🟡 **(c) npm is at `7.0.7` but the newest git tag is `v7.0.1`** — the published artefact is ahead of the tagged history, so **pin the npm version, not a git ref.** 🔵 Branches `legacy-v5` and `legacy-v6` remain for the pre-rewrite line.

🟢 **So `Gap 316(i)` is answered in the form that matters:** the port is **wiring an existing maintained Apache-2.0 library into an agent**, not implementing a 1EdTech specification. 🔵 `compose/patterns.md` `P12-R` carries the concrete swap.

### 🟢 `Gap 319` — **CLOSED on all three limbs.** The fork is 39 bytes of divergence, and the real exposure is the *upstream*

🔵 **The gap:** OATutor's `aws/lti-middleware/package.json` declares `"ims-lti": "github:CAHLR/ims-lti"` — an unpinned fork — with three unmeasured exposures: (a) the resolved commit can change; (b) divergence from upstream unknown; (c) the fork's maintenance status unknown.

🟢 **(b) now measured exactly, by blobless-cloning both and comparing blob shas:**

| Probe | Result |
|---|---|
| Upstream [`omsmith/ims-lti`](https://github.com/omsmith/ims-lti) files | **30** |
| Fork [`CAHLR/ims-lti`](https://github.com/CAHLR/ims-lti) files | **43** |
| Files common to both | **30** — 🟢 **upstream is a strict subset; zero files are unique to upstream** |
| Files only in the fork | **13** — `lib/*.js` (**12 files**) + `package-lock.json` |
| `lib/` vs `src/` basenames | 🟢 **1:1 mirror confirmed** — `lib/` is the compiled output of `src/*.coffee` |
| Of the 30 common files, byte-identical | 🟢 **28** |
| Differing | **2** — `.gitignore` and `src/extensions/outcomes.coffee` |
| `LICENSE` | 🟢 **byte-identical, 1 094 B, MIT** — *"Copyright (c) 2014 Owen Smith / Original Copyright (c) 2013 OfficeHours"* |

🟢 **The two differences, read in full:**

- **`.gitignore`** — line 15 changes from `lib` to `# lib`. 🟢 **The build output is deliberately un-ignored.** Nothing else.
- **`src/extensions/outcomes.coffee`** — **7 513 B → 7 552 B, a 39-byte diff that is exactly one added line**: `'User-Agent': 'ims-lti/3.0.2'`, inserted into the OAuth-signed **`POST` headers of the Basic Outcomes `replaceResult` call.** 🟢 **One header. No logic change, no signature change, no behavioural change to the grade payload.**

🟢 **So the mechanism is fully explained, and the fork's own HEAD commit message says it verbatim** — `chore: commit compiled lib/ for git-dependency installs`, **2026-07-03**. Both `package.json` files declare `"version": "3.0.2"`, `"main": "./lib/ims-lti"`, `"scripts": {"prepublish": "make build"}`. 🔴 **`npm install github:…` does not run `prepublish`**, so without a committed `lib/`, `main` resolves to nothing and the install is simply broken. 🟢 **The fork exists to make a git dependency installable. That is all it is.**

🔴 **And that inverts the risk the gap was opened on.** 🟢 **(c) answered, and it is the real finding:** the fork is **three months old and purposeful**; 🔴 **upstream `omsmith/ims-lti` has HEAD `4df2936` dated `2016-09-05` — ten years dead.** 🔴 **The hazard was never the unpinned fork. It is that OATutor's LMS seam rests on a decade-abandoned CoffeeScript library implementing a superseded protocol version.** 🟢 **Pin `9b712f6` as the short-term fix; the actual remedy is `P12-R` — replace the dependency with `ltijs` and delete the fork question entirely.**

🔵 **One piece of good news for licence closure:** the fork's `LICENSE` is byte-identical to upstream's **MIT**, so OATutor's transitive LTI dependency is **cleanly MIT**, with no new obligation.

### 🟢 Foundational repositories for an education engagement — **re-stated with this pass's additions**

| Repo | Licence (payload) | Head | Layer it serves |
|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** 11 361 B | `master` `0ec24fe` · 2026-10-06 | 🆕 **LMS interoperability** — LTI 1.3, AGS, Deep Linking, NRPS, Dynamic Registration (Node ≥24) |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** 1 070 B | `master` `d8fa43e` · 🔴 2022-11-21 | 🆕 **LMS interoperability, Python side** — same surface, unmaintained |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** 1 105 B | `main` `939eb0e` · 2026-09-30 | **Mastery model (BKT) + tutoring dialogue + doc→learning-object compiler** (`Gap 321`, closed this pass) |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT** 1 068 B | `main` `f0142f2` · 2026-10-08 | 🆕 **Adaptive scheduling** — FSRS spaced repetition, knowledge graph, block-decision engine with cold start |
| [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 **MIT** 1 069 B | `main` `b90bd88` · 2026-08-23 | 🆕 **Grading pipeline + human-approval gate + MCP surface** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** 11 408 B | `main` `6cf793b` | Agent-native tutoring, layered memory, multi-engine RAG |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** 1 531 B | `main` `196c547` · 🟡 2026-06-26 | Full tutoring platform with **Ollama** (sovereign inference), HITL governance, `ar`/`fr`/`en` |
| [`CAHLR/ims-lti`](https://github.com/CAHLR/ims-lti) | 🟢 **MIT** 1 094 B | `master` `9b712f6` · 2026-07-03 | 🔴 **Legacy LTI 1.1 only.** Pin `9b712f6` if used at all; prefer `ltijs` |

🟢 **Eight rows, all real, all licence-verified this pass or sha-identical to a pass that verified them.** 🔴 **Deliberately excluded:** `oat-sa/tao-core` (GPL-2.0), `artcc/freelingo` (AGPL-3.0), `NiyatiDesai0747/personalized-adaptive-learning-tutor` (no licence file) — 🟢 named in `agents/top.md` so the exclusions are visible rather than silent.

## 🟢 Seventieth pass, 2026-10-09 — the permissive substrate gains a **real tutoring foundation with mastery estimation in-tree**, and the shelf's licence-reading method gains a hazard guard. `CAHLR/OATutor` (MIT) is the first foundation here that models a learner rather than moving a record

⏱️ **Second pass of this date.** Pass 69 closed earlier today (commit `abf91da`, 00:07 UTC). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Instruments:** `git ls-remote --symref` **13 of 13**; `git ls-remote --heads` used as the branch-existence authority (see `P819`); `git clone --depth 1 --filter=blob:none` enumerated **8 338 files** on OATutor; `raw.githubusercontent.com` served every licence payload. 🔴 **`api.github.com` serves `403` for unattached repositories** — no third-party star counts, nothing here ranked by popularity.

### 🆕 A new permissive foundation, and what makes it a *foundation* rather than an agent

[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — 🟢 **MIT**

| Probe | Result |
|---|---|
| `main` · HEAD | 🟢 **`939eb0e`** |
| `LICENSE` | 🟢 **MIT, 1 105 B** — *"Copyright (c) 2023 Zachary A. Pardos (@zpardos) - CAHL research lab"* |
| tree | 🟢 **8 338 files** (blobless clone) |
| mastery model | 🟢 **`src/models/BKT/BKT-brain.js`** — Bayesian Knowledge Tracing, in-tree, not a dependency |
| problem selection | 🟢 `src/models/BKT/problem-select-heuristics/defaultHeuristic.js` + `experimentalHeuristic.js` |
| LMS integration | 🟡 **`aws/lti-middleware/`** (25 422 B `index.js`) — **LTI 1.1**: `oauth_consumer_key` ×3, `replaceResult` ×1; 🔴 **no `id_token`, `jwks`, `lineitem`, `client_id`** |
| launch descriptor | 🟡 `public/lti-consumer-config.xml` — **`imslticc_v1p0` / `imsbasiclti_v1p0` cartridge** (LTI 1.1) |
| LTI library | 🔴 `"ims-lti": "github:CAHLR/ims-lti"` — **an unpinned fork: no tag, no sha** (`Gap 319`) |
| superseded code | 🟡 `old-lti-middleware/` still present in `main` — **two launch paths in-tree** |
| content grant | 🟡 problem content under **CC BY 4.0** — 🔴 **a different licence from the code; attribute accordingly** |

🟢 **Why this matters to this shelf specifically.** 🔵 Every permissive foundation recorded here so far is an **infrastructure** layer: Ed-Fi DMS moves records, `lrsql` stores learner evidence, `opensalt` anchors competencies, `conform-ed` gates conformance. 🔴 **None of them models a learner.** 🟢 **OATutor is the first MIT component on this shelf that estimates per-skill mastery and selects the next problem from that estimate** — the pedagogical core that every one of this shelf's recipes has so far had to specify as *"build this part."*

🔴 **Two caveats that must travel with it in any deliverable.** 🟡 **(i) The code is MIT and the content is CC BY 4.0** — a client shipping the bundled algebra content owes attribution, and the two grants must be tracked separately. 🔴 **(ii) The LTI layer is 1.1 and depends on an unpinned GitHub fork** — vendor the fork at a sha, or replace the layer outright, which is what `P12` already prescribes.

### 🟢 The permissive tutoring tier, now three components across three regions

| Component | Licence (payload) | Region | Layer it supplies |
|---|---|---|---|
| 🆕 [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT**, 1 105 B, `main` `939eb0e` | **North America** — UC Berkeley | 🟢 **Mastery estimation (BKT) + problem selection** |
| 🆕 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0**, 11 408 B (`P804`), `main` `6cf793b` | **APAC** — HKU | Agent-native tutoring orchestration |
| 🆕 [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause**, 1 531 B, `main` `196c547` | **EMEA** — R2D-dev | Multimodal/immersive tutoring surface |
| [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) | 🟢 **Apache-2.0**, 11 357 B, `main` `5b96722` | **EMEA** — UPV, Spain | LLM grading + LMS grade return (**LTI 1.1**) |

🟢 **Four permissive components, three regions, and for the first time a tutoring stack that is permissive end to end** — mastery model, orchestration, surface, grading. 🔴 **Its one shared weakness is the LMS seam: 2 of 2 components with an LTI layer speak 1.1, and none speaks 1.3 + AGS** (`Gap 316`).

### 🔴 The AGPL tier, recorded here because a foundation's licence decides whether it can be a foundation at all

| Component | Licence (payload) | Verdict for a closed deliverable |
|---|---|---|
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | 🔴 **AGPL-3.0**, 34 522 B, `main` `7d9e905` | 🔴 **Not usable.** Network copyleft: serving it triggers the source obligation |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 🟡 **AGPL-3.0**; `skills/*.md` **dual MIT-or-AGPL at the user's option**; `app/` **AGPL-only** | 🟡 **Content layer usable under MIT; application layer not.** 🟢 The only lawful permissive harvest here is the `skills/` curricula |

🟢 **This tier is new to the shelf and it is recorded as a foundation-layer fact, not a curiosity:** 🔴 **an AGPL component cannot be a foundation for a client who needs to keep their code closed**, however good it is. 🔵 **Twenty-one weeks of a query containing the token `MIT` hid this tier rather than clearing it.**

### 🟢 Substrate stability — all seven prior components unmoved

🟢 `moocupv/lti-ai-grader` `5b96722`/11 357 B · `1EdTech/lti-1-3-php-library` `3a192de`/11 343 B · `yetanalytics/lrsql` `cb794e4`/11 357 B · `opensalt/opensalt` **`develop`** `db41cc4`/1 080 B · `conform-ed/conform-ed` `3596bb5`/1 080 B · `THU-BPM/MarkLLM` `0a4fe8c`/11 357 B · `Ed-Fi-Alliance-OSS/Data-Management-Service` `ab82466`/11 357 B. 🔵 **Every sha and every byte count identical to pass 69.** 🟢 **Ed-Fi DMS: still pin `v8.0.0` (`d911abb`) explicitly — `main` tracks an unreleased 8.1.0 whose changelog opens under *"Breaking changes."***

## 🟢 Sixty-ninth pass, 2026-10-09 — a **new instrument** reads whole trees without the API, and with it the permissive substrate's **capability gaps** are read for the first time: the shelf's only Apache-2.0 system of record has **no rostering standard and no change feed**

⏱️ **First pass of this date (pass 68 closed 2026-10-08; the date rolled over during this pass's measurements, which are dated by their publication here). Append-only: this section is new; nothing below it was rewritten.**

🟢 **Instruments:** `git ls-remote --symref` **9 of 9**; `git ls-remote --tags` resolved **23 tags** on the Ed-Fi successor; `raw.githubusercontent.com` served every licence payload below.
🆕 **New instrument: `git clone --depth 1 --filter=blob:none`** — **5 846 files enumerated** on the Ed-Fi successor with no API access. 🔵 **Every prior pass guessed paths and recorded 404s; this reads the tree.**
🔴 **`api.github.com` CORRECTED:** resolves, **authenticated** (core **15 000**/hr), serves `200` — `403` **only** for repositories not attached to this session. 🟢 **No third-party star counts, so nothing here is ranked by popularity** — unchanged in effect, corrected in cause.

### 🟢 The permissive system-of-record substrate, re-read — and its licence is the best news in it

[`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service)

| Probe | Result |
|---|---|
| `main` · HEAD | 🆕 **`ab82466`** — 🔵 **moved from pass 68's `9203e19`** |
| `LICENSE` | 🟢 **Apache-2.0, 11 357 B** — canonical byte count, re-confirmed |
| tree | 🆕 **5 846 files** (blobless clone) |
| release tags | `v0.1.0`–`v0.7.0`, then **`v8.0.0`** (`d911abb`) |
| newest tags | 🆕 **`dms-pre-8.0.1-alpha.0.94`–`0.99`** |
| `docs/changelog/` | 🆕 **`8.1.0.md`, and nothing else** |

🟢 **The version line is explained from payload and `Gap 311(a)` closes.** `docs/PRD-v8.0.md`: *"**Ed-Fi API v8.0** is a ground-up rewrite of the platform's prior generation."* 🔵 **The tags carry the Ed-Fi API *product* version, not the DMS *component* version** — `v0.x` was the component's pre-product line. 🟢 **Pass 68 held this as an inference under `P722`; it is now a fact.**

🔴 **`main` is not the tag, and `main` is heading for 8.1.0 whose changelog opens under *"Breaking changes."*** 🟢 **In any deliverable, pin `v8.0.0` explicitly.**

### 🔴 The finding that changes how this substrate may be quoted — **v8.0 is missing capabilities the prior generation had**

🟢 `docs/PRD-v8.1.md` is a **gap-driven PRD**, and it enumerates what v8.0 **does not yet do** relative to the Ed-Fi ODS/API generation it replaces:

| Absent from v8.0 | The PRD's own words |
|---|---|
| 🔴 **Event streaming (Kafka/CDC)** | *"no equivalent way to consume data changes from v8.0 **without polling the API**"* |
| 🔴 **OneRoster rostering integration** | *"vendors and hosts who built workflows around them… have **no migration path** until these are restored"* |
| 🔴 **Unique-ID / Identities integration** | same clause |
| 🔴 Read replicas, high-performance paging, cache-refresh signalling | *"complete, operating capabilities in the prior generation — hosts running at scale were actively relying on them"* |
| 🔴 Ownership-based authorisation, custom access rules, configurable token limits | *"Hosts who depended on these… cannot yet replicate that posture in v8.0"* |
| 🔴 Custom validation | *"no supported way to enforce business rules beyond… built-in schema validation, without forking core code"* |

🟡 **One of them is already closing on `main` and not in any release:** `docs/changelog/8.1.0.md` documents **`IdentitySettings:BearerTokenPerClientLimit`** (default 15 tokens/client, `HTTP 429 Too Many Tokens`). 🔵 **So the capability list is live, and the gap between `v8.0.0` and `main` is where it is being closed** — which is precisely why `main` must not be tracked and the tag must be pinned.

🟢 **How to quote this substrate:** 🟢 **a genuinely permissive, actively developed Ed-Fi API implementation** — 🔴 **without a change feed, without OneRoster, and without the fine-grained authorisation the prior generation had.** 🔵 **`Gap 315`** records that the shelf can *conformance-test* OneRoster (`conform-ed`, MIT) but cannot *provide* it permissively.

### 🔴 Adoption is a re-platforming, not an upgrade — `Gap 303` **CLOSED** from primary payload

| Probe | Result |
|---|---|
| `docs/PRD-v8.0.md` **NFR-OPS-2** | 🔴 *"does not support **in-place migration of an already-provisioned database** to a new effective schema — **provisioning is create-only**"* |
| `docs/PRD-v8.0.md` line 19 | 🔴 *"a **ground-up rewrite** of functionality previously delivered via the Ed-Fi ODS/API"* |
| `docs/DATA-STRICTNESS.md` §*Migrating from the Ed-Fi ODS/API* | 🟡 **request-body casing guidance only** |
| `docs/DATABASE-SEGMENTATION-STRATEGY.md` §*Migration from ODS/API* | 🟡 **a configuration-equivalence table** — `dbo.OdsInstances` → `POST /v3/dataStores` |

🟢 **The repository documents a migration path at the configuration surface and nowhere at the data layer** — and NFR-OPS-2 says why: that is the design, not an omission. 🔴 **Never price Ed-Fi DMS adoption as an in-place cutover.**

🆕 **And a second fact worth more than the answer — `Gap 314`:** NFR-OPS-2 also means **a data-model extension requires database re-provisioning plus a service restart**. 🔵 **An AI deliverable that writes generated evidence back into the system of record *is* an extension.** 🟢 **Design that evidence into the LRS (`P8`, `P10`), not into an Ed-Fi extension.**

### 🟢 Permissive foundations, licences read from payload this pass — **5 of 5 verified**

| Repo | Licence | `LICENSE` bytes | Role |
|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | 🟢 **Apache-2.0** | **11 357** (canonical) | Ed-Fi API implementation; data-standard substrate |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | **11 357** (canonical) | xAPI LRS — where learner evidence belongs (`P8`, `P10`) |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | 🟢 **MIT** | **1 080** | Conformance coverage for xAPI 2.0, Caliper 1.2, **OneRoster 1.2**, Common Cartridge |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🟢 **MIT** | **1 080** | CASE competency-framework authoring and hosting |
| 🆕 [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | 🟢 **Apache-2.0** | **11 357** (canonical) | LLM watermarking — 🔵 the named occupant of the `P33` signature seam |

🟢 **Five rows, five real repos, five licences read as bytes.** 🔵 **`conform-ed` and `opensalt` are both MIT at 1 080 B — the same canonical MIT length, independently confirming each read.**

### 🆕 The licence law gets its sharpest instance yet: **one organisation, two tiers, two grants**

🟢 **Measured on the Frappe stack** (`Gap 312`'s remedy (i)):

| Component | Layer | Licence | Evidence |
|---|---|---|---|
| [`frappe/frappe`](https://github.com/frappe/frappe) | **framework** | 🟢 **MIT** | `LICENSE` **1 118 B** — *"The MIT License, Copyright (c) 2016-2021 Frappe Technologies Pvt. Ltd."* 🆕 |
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | **app** | 🔴 **GPL-3.0** | `license.txt` **35 149 B** — **full grant text** 🆕 |
| [`frappe/education`](https://github.com/frappe/education) | **app** | 🔴 **GPL-3.0 (asserted)** | `license.txt` **19 B**: `License: GNU GPL V3`; `LICENSE` **404** |

🔵 **The law, restated with this instance:** **the grant follows the author class, not the layer.** 🔴 **The framework's MIT terms do not rescue, override or impose anything on an app's grant** — so the 19-byte assertion stands alone. 🟢 **But the sibling app ships the real 35 149-byte GPL-3.0 grant, which is strong corroboration that GPL-3.0 is meant.** 🟢 **Record `frappe/education` as GPL-3.0 and assume every GPL-3.0 obligation; never as "unknown."**

🟡 **A corollary worth keeping:** 🔴 **a byte count alone does not identify a grant.** OpenEduCat's `LICENSE` is **8 241 B** and FenixEdu's is **7 652 B**; both are LGPL-3.0, and the difference is a prepended copyright pointer. 🟢 **Read the first lines, not only the length** — the canonical lengths (MIT 1 080–1 118, Apache-2.0 11 357, GPL-3.0 ~35 100, LGPL-3.0 7 652) are a **check**, not an identification.

## 🟢 Sixty-eighth pass, 2026-10-08 — the **system-of-record tier** is read for the first time and it is the shelf's **first wholly non-permissive layer** (5 of 5); `Ed-Fi`'s successor is confirmed **Apache-2.0 at the canonical byte count**, and the licence law gets a sharper shape: the grant follows the **author class**, not the layer

⏱️ **Twenty-second pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Instruments:** `git ls-remote --symref` **7 of 7**; `raw.githubusercontent.com` served every
payload below; `git ls-remote --tags` resolved **7 tags** on the Ed-Fi successor. 🔴 `api.github.com`
re-measured **`403`** — no star counts, nothing ranked by popularity.

### 🟢 🆕 The student-information-system tier — five systems of record, every grant read from payload

🔵 This KB has carried LMS, LRS, assessment, roster, credential and competency layers. 🔴 **It had
never read the layer that actually holds the student record.** 🟢 Read now, and the first thing to
report is the **ref**, because not one of these repositories answers to `main`:

| Component | default ref · HEAD | Licence (payload, bytes) | Grant layers | Verdict |
|---|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) (RosarioSIS) | 🔵 **`mobile`** · **`899f6da`** | 🔴 **GPL-2.0** (`LICENSE`, **15 214 B**, *"Version 2, June 1991"*) | 🟢 **three layers agree** — `LICENSE` + `composer.json` **and** `package.json`, both `"license": "GPL-2.0-or-later"` | 🟢 **the cleanest licence record in the tier**, 🔴 and copyleft 🆕 |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) (Gibbon) | 🔵 **`v31.0.00`** · **`683d2c4`** | 🔴 **GPL-3.0** (`LICENSE`, **35 121 B**, *"Version 3, 29 June 2007"*) | 🟢 **two agree** — `LICENSE` + `composer.json` `"license": "GPL-3.0"` | 🔴 copyleft; 🟡 **note the ref is a version** 🆕 |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (OpenEduCat) | 🔵 **`19.0`** · **`1c95cef`** | 🟡 **LGPL-3.0** (`LICENSE`, **8 241 B** — a *short notice*: *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"*) | 🟢 **two agree** — `LICENSE` + README prose (3×) | 🟡 **the one usable band in the tier** — see `P750` 🆕 |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) (openSIS CE 9.3) | `master` · **`5d546f2`** | 🔴 **GPL-2.0** — 🔴 **not at any conventional path**; found only at **`docs/License.txt`**, **17 286 B**, *"Version 2, June 1991"*, **BOM-prefixed** | 🟡 payload + README prose; 🔴 **no manifest, no root `LICENSE`** | 🔴 copyleft, 🔴 **and nearly mis-read — see below** 🆕 |
| [`frappe/education`](https://github.com/frappe/education) | 🔵 **`develop`** · **`444cc8e`** | 🔴 **GPL-3.0 *asserted*** — `license.txt` is **19 B** and reads, in full, **`License: GNU GPL V3`** | 🔴 **one layer, and it contains no grant** — `package.json` is `"private": true` with no `license` key; `pyproject.toml` has **no licence line at all**; README has **no licence mention** | 🔴 **the weakest grant this shelf has recorded** 🆕 |

🔴 **Five of five are non-permissive. There is no MIT and no Apache-2.0 anywhere in this tier.**
🔵 **This is the exact inverse of the two layers before it** — pass 66's LRS tier was four-of-six
permissive, pass 67's CASE tier was four-of-four — and it is the **first wholly non-permissive layer
in sixty-eight passes**.

### 🔵 🆕 Five of five default refs are **not `main`**, and two are version-shaped

🟢 **`develop` · `mobile` · `master` · `v31.0.00` · `19.0`.** 🔵 Gate 0 of the pre-flight
(`compose/patterns.md`, pass 63) says every gate below it takes a `[ref]` because `master` is a
pseudo-ref. 🟢 **This tier is the strongest evidence yet for that gate:** a client who clones
`GibbonEdu/core` without a ref gets **`v31.0.00`**, a ref whose name will be *wrong* at the next
release; one who clones `openeducat_erp` gets **`19.0`**, pinned to an Odoo major line; and
🔴 **one who clones `rosariosis` gets `mobile`** — a branch name that reads like a feature branch
and is in fact the default. 🔵 **Any instruction in a deck that says "clone and build" is incomplete
in this tier without a `[ref]`.**

### 🔴 🆕 The near-miss, recorded because it would have been this pass's false headline

🔵 A case-insensitive prose sweep for licence names reported **`Apache 2`** in
`OS4ED/openSIS-Classic`'s README and **`MIT`** in two others. 🔴 **All three were artifacts, and the
first would have published a *permissive system of record* — which would have been the pass's
headline and would have been false:**

| Reported hit | What it actually was | Class of error |
|---|---|---|
| `Apache 2` in openSIS README | 🔴 **`Apache 2.4 or above`** — the **web server**, in the Installation section | 🔴 **homonym** |
| `MIT` in rosariosis README | 🔴 **`ad`MIT`tance`** | 🔴 **sub-word** |
| `MIT` in Gibbon README | 🔴 **`sub`MIT`ting issues`** | 🔴 **sub-word** |

🟢 **Re-run with word boundaries (`\bMIT\b`): zero hits in both.** 🟢 **And openSIS's real grant was
then found where the README pointed** — `docs/License.txt`, GPL-2.0, 17 286 B. 🔵 Two practices fall
out of this and both are now in `compose/patterns.md`: **`P810`** (a substring licence grep fails in
two distinct ways — sub-word and homonym) and **`P811`** (**404 on every conventional licence path is
not "no licence"; it is "read the README"**).

### 🟡 🆕 Two GPL-2.0 payloads, two byte counts — so byte count is a **flag**, not an identity

🔵 `rosariosis` ships GPL-2.0 at **15 214 B**; `openSIS-Classic` ships GPL-2.0 at **17 286 B**.
🟢 **Same licence, same version line, different bytes** — openSIS's copy is **reflowed** (paragraphs
unwrapped onto single lines) and carries a **BOM**. 🔵 This refines `P804`, which read an
off-canonical Apache byte count as a question about the copyright holder: 🟢 **an off-canonical count
is a question, and "the text was reformatted" is one of its answers.** 🔴 **Byte count flags a
payload for reading; it never identifies one on its own.**

### 🟢 🆕 The Ed-Fi successor, confirmed — and the version line has a discontinuity

🔵 Pass 67 reported a shipped `v8.0.0` on the Ed-Fi **Data-Management-Service**. 🔴 **The slug pass 67
implied does not exist:** `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Management-Service` returns a credential
prompt (this environment's signature for *absent or private*). 🟢 **The repository is
[`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service)**, and it measures:

| Probe | Result |
|---|---|
| default ref · HEAD | `main` · **`9203e19`** 🆕 |
| Licence | 🟢 **Apache-2.0**, `LICENSE`, **11 357 B** — 🟢 **the shelf's canonical count, exactly** |
| README | **3 239 B**; *"These applications replace the legacy Ed-Fi ODS/API and Ed-Fi ODS Admin API"* |
| Tags | `v0.2.0` → `v0.7.0`, then 🔵 **`v8.0.0`** (**`d911abb`**) |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` (legacy) | `main` · **`e453cd2`** — 🟢 still resolves |

🔵 **Two things to flag.** 🟡 First, **`main` (`9203e19`) is not `v8.0.0` (`d911abb`)** — the tag pass
67 recorded is not the head a client clones. 🟡 Second, the tag line jumps **`0.7.0` → `8.0.0`**,
and 🔴 **no payload read this pass explains the jump** (`Gap 311`); the obvious reading is alignment
with the legacy ODS/API major line, but that is an inference and is left as one.

### 🟢 The law this pass sharpens: the grant follows the **author class**, not the functional layer

🔵 Pass 67 framed the shelf's licence law by *layer* — registries permissive, systems of record not.
🔴 **This pass breaks that framing with a counter-example from inside its own tier:** the Ed-Fi
Data-Management-Service **is** a system of record, and it is **Apache-2.0 at 11 357 B**.

🟢 **The framing that survives all sixty-eight passes is about *who wrote it*:**

| Author class | Examples read on this shelf | Grant |
|---|---|---|
| 🟢 **Standards bodies & alliances** | Ed-Fi DMS (Apache-2.0) · 1EdTech OpenCASE (Apache-2.0) · OpenSALT (MIT) · the xAPI/LRS tier | 🟢 **permissive, near-uniformly** |
| 🔴 **Sector product vendors & communities** | RosarioSIS · Gibbon · openSIS · frappe/education · OpenEduCat · Moodle · Open edX | 🔴 **copyleft, 5 of 5 this pass and essentially without exception before it** |
| 🔴 **Credential issuers** | `certo` · `Opencred` · `edubadges-server` | 🔴 **AGPL-3.0, to a repo** |

🟢 **`P809` states the consequence** (`compose/patterns.md`): **build on the substrate, integrate with
the product at arm's length.** 🔵 The arm's length already has an instrument on this shelf —
**LTI 1.3** (`P736`/`R57a`), which pass 57 established as the licence-isolation boundary. 🟢 **So the
negative result in this tier does not cost the shelf a deliverable; it tells it which side of the
boundary to build on.**


## 🟢 Sixty-seventh pass, 2026-10-08 — the **CASE tier** lands permissive-unanimous, a **cross-protocol conformance harness** arrives MIT, and the Ed-Fi substrate this shelf has carried since pass 13 turns out to have a **shipped successor** (`v8.0.0`)

⏱️ **Twenty-first pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **What pass 66 left open by construction.** It read the **store** tier for xAPI and closed the
telemetry arrow (spec → emitter → store). 🔴 **But a store full of statements answers *what
happened*, never *what it proves*.** 🟢 **This pass reads the tier that answers the second
question — the competency registry — and it is the shelf's second permissive-dominant tier and its
first unanimous one.**

### 🟢 🆕 The CASE / competency tier, every grant read from payload

| Registry | ref · HEAD | Licence (payload, bytes) | Engine / stack | Verdict |
|---|---|---|---|---|
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | **`develop`** · **`db41cc4`** | 🟢 **MIT** (`LICENSE`, **1 080 B**, © **2016 Public Consulting Group**) | PHP / Symfony, **docker-compose**, **MySQL** | 🟢 **the production default of this tier** |
| [`infosign/compeito`](https://github.com/infosign/compeito) | `main` · **`0656e10`** | 🟢 **Apache-2.0** (**two layers**: `LICENSE` **10 759 B** + `pyproject.toml`) | **Python 3.12 / FastAPI / PostgreSQL**, Docker | 🟢 **the forward path** |
| [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | `main` · **`97d0373`** | 🟢 **Apache-2.0** (`LICENSE`, **11 264 B**) | Monorepo: visual **editor** + publishing **server** + **Keycloak** + **Traefik**, single-command compose | 🟢 **the authoring front end** |
| [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | `main` · **`3596bb5`** | 🟢 **MIT** (`LICENSE`, **1 080 B**) | **Bun + turbo** monorepo, podman compose | 🟢 **the cross-protocol harness — see below** |

🟢 **Four of four permissive.** 🔵 **Unanimous, which no prior tier on this shelf has been.**

### 🟢 The row that changes what this tier is *for*: OpenSALT is no longer a competency editor

🔵 **This KB would have filed OpenSALT as "the CASE framework manager" from its name and history.**
🔴 **Its own README refutes that, in its first paragraph**, and the correction is the reason it
takes the default slot rather than a footnote:

> *"OpenSALT is an open-source **Learning and Employment Record (LER) registry platform** … It
> enables organizations to define, manage, align, publish, and exchange **competencies, standards,
> credentials, learning opportunities, jobs, pathways, and issuer information** … OpenSALT has
> **evolved from a competency framework management system into a standards-based registry
> service**."*

🟢 **Standards it names itself as aligned to:** **1EdTech CASE®** (1.1-compatible content structures
and extensions), **Credential Engine CTDL**, and **W3C Verifiable Credentials**. 🟢 **Interfaces:**
an interactive web application **and** headless **secure REST APIs** for system-to-system
integration.

🔵 **Why that is a foundations-level fact and not marketing.** The thing a skills-based engagement
needs is a **join** between a competency, a credential that asserts it, and an occupation or
pathway that demands it. 🔴 **This shelf has had no permissive component that holds that join** —
it had CASE-shaped nothing, badge issuers under AGPL, and an Ed-Fi substrate that models
*enrolment*, not *skills*. 🟢 **OpenSALT holds it, under MIT, from a named holder.**

🟢 **And it is the basis of the official registry.** 1EdTech's own announcement of the **CASE
Registry** states the Registry is **based on the OpenSALT open-source project**. 🔵 **So the
permissive component and the consortium's reference deployment are the same codebase** — a
provenance position this shelf has not been able to claim for any other 1EdTech-adjacent row
(contrast `1EdTech/openbadges-specification`, which carries **no licence file at all**).

🔴 **Two caveats priced rather than buried:** the grant rests on **one layer** (🔴 **no
`composer.json` at `develop`**, which for a Symfony application is an absence worth noting, and it
is **not on Packagist** — 404), and the **default ref is `develop`, not `main`** — so 🔴 **pinning
the commit is not optional here**, it is the grant. 🟡 Release tags resolve to **3.2.1** (plus a
stray `ky` tag, which is noise, not a version).

### 🟢 🆕 `conform-ed` — the first component on this shelf that spans **every protocol the shelf has censused**

🔵 Passes 60–66 read education's protocols **one implementation at a time**: LTI 1.3 (launch),
OneRoster (who), SCORM/cmi5 (content), xAPI (what happened), Open Badges (what it proves), Caliper
(unreadable). 🟢 **`conform-ed` declares all of them, in one MIT monorepo**, per its README
(4 295 B):

**xAPI 1.0.3 + IEEE 2.0 · QTI 2.1 / 2.2 / 3.0.1 · LTI 1.3 + Deep Linking 2.0 + AGS 2.0 + NRPS 2.0 +
Proctoring 1.0 · Common Cartridge · OneRoster 1.2 · CASE 1.1 · CLR 2.0 · Open Badges 3.0 · Caliper ·
cmi5 · SCORM.**

🟢 **It ships runners, not only schemas:** an **xAPI LRS conformance runner**, a **cmi5
conformance/oracle runner**, an **LTI 1.3 conformance runner**, and **reference adapter services**
for cmi5 and LTI 1.3.

🟢 **It also stands up pass 66's store itself.** Its `package.json` scripts drive
**`yetanalytics/lrsql`** under `podman compose` — `lrsql:up`, `lrsql:wait`, `lrsql:reset`,
`lrsql:reset:best-effort`, `lrsql:auth:check` — and it carries **`qti:corpus:fetch`**,
**`qti:coverage:report`**, **`qti:delivery:report`**. 🔵 **Two consecutive passes landed on two
halves of one toolchain**, which has not happened before on this shelf: the store read last pass is
the store this harness drives.

🔴 **What it is not, stated here because the word invites the error.** Its README says it is **not a
certification body** and produces **conformance *assessments*, not official certification**.
🔴 **And standards conformance is not EU AI Act conformity assessment** — different regime,
different assessor; full reading in `agents/top.md` and `intel/trends.md`. 🟢 Its honest value is
**regression evidence against a spec corpus**, which is exactly what this shelf's interop rows have
lacked.

🟡 **Grant caveat:** `LICENSE` is clean MIT at **1 080 B**, but `package.json` is
**`"private": true`** with **no `license` key**, and the package is **not on npm (404)**.
🔴 **One-layer grant on an unpublished monorepo — pin `3596bb5`.**

### 🟢 🆕 The Ed-Fi substrate has a **successor, and it has shipped** — this is a tier replacement, not an addition

🔵 **This KB has carried `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` and its four-repo substrate since the
thirteenth pass**, and completed the licence census of it at pass 62. 🔴 **Those repositories are
now the *legacy* line, and the shelf did not know it.**

| Repo | ref · HEAD | Licence (payload, bytes) | Reading |
|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | `main` · **`9203e19`** | 🟢 **Apache-2.0** (**two layers**: `LICENSE` **11 357 B** — canonical — + README prose) | 🟢 **The successor.** Resources + Descriptors + Discovery APIs 🆕 |
| [`Ed-Fi-Alliance-OSS/DMS-Configuration-Service`](https://github.com/Ed-Fi-Alliance-OSS/DMS-Configuration-Service) | `main` · **`782b0d3`** | 🟢 **Apache-2.0** (`LICENSE`, **11 357 B**) | 🟢 Implements the Ed-Fi **Management API** — successor to **ODS Admin API** 🆕 |

🟢 **The README states the replacement in its own words:** *"These applications **replace the
legacy** Ed-Fi ODS/API and Ed-Fi ODS Admin API."*

🟢 **And unlike the channel's account, 8.0 is not merely an alpha.** 🔴 The channel reported only
`dms-v8.0.1-alpha.0.188` pre-releases and said it *"can't confirm the exact release date of the
stable 8.0"*. 🟢 **`git ls-remote --tags` resolves a plain `v8.0.0` tag at `d911abb`** — a shipped
version tag, measured from the git protocol rather than inferred from a release feed this session
cannot read.

🟡 **Tag hygiene, recorded because it affects pinning:** the tag list is
`v0.1.0 · v0.2.0 · v0.4.0 · v0.5.0 · v0.6.0 · v0.7.0 · v8.0.0` — 🔴 **`v0.3.0` is absent and a bare
`temp` tag exists**. 🔵 The jump from `v0.7.0` straight to `v8.0.0` is deliberate: Ed-Fi aligned the
DMS version to the **Ed-Fi API version**, so "8.0" names the API contract, not the eighth major
release of this codebase. 🔴 **A proposal that reads `v8.0.0` as seven prior majors of maturity has
misread it.**

🟢 **Operational shape, from `GETTING_STARTED.md` (10 021 B) read as bytes:** 🔴 **.NET 10 SDK**
required to build; **PostgreSQL** for OLTP; `docker compose` (Docker Engine + Compose plugin
sufficient on Linux, Podman supported with a find-and-replace in `eng/docker-compose`). 🟡 The
release-candidate notes add **OpenSearch/Elasticsearch**, **Kafka** realtime streaming, and
**Keycloak** OAuth. 🟢 **Data Standard 5.2 out of the box**, with a `docs/DATA-STANDARD-VERSIONS.md`
matrix in-tree.

🔴 **The migration question this opens is not answered this pass**, and it is the expensive one:
whether a district on `Ed-Fi-ODS` can move to DMS without a data migration — the question pass 66
*could* answer for `lrsql → xapi-lrs` (it was a no-op). 🔴 **No equivalent claim was found in any
payload read.** 🟢 **`Gap 303` opened** to carry it.

🟢 **Shelf consequence, stated plainly:** the Ed-Fi rows below in this file remain **correct and
Apache-2.0**, and they are now **the legacy line**. 🟢 **A new engagement starting today should
read `Data-Management-Service` first and `Ed-Fi-ODS` as the system it will interoperate with or
replace** — and the whole path, old and new, stays **Apache-2.0**, so the licence does not change
across the migration either.

### 🟢 The protocol census, restated with this pass's tier

| Protocol | Permissive implementation on this shelf | Grant |
|---|---|---|
| **LTI 1.3** | `Cvmcosta/ltijs` | 🟢 Apache-2.0 (11 361 B) |
| **xAPI** — spec / emitter / **store** | `adlnet/xAPI-Spec` · `TinCanPython` · **`lrsql`** / **`xapi-lrs`** | 🟢 Apache-2.0 throughout |
| **QTI 2.x / 3.0** | `amp-up-io/qti3-item-player` (🟢 **1EdTech Certified**) · `longsightgroup/qti3` · `Kennisnet/php-qti3` | 🟢 MIT |
| **OneRoster 1.2** | `Ed-Fi-Alliance-OSS/edfi-oneroster` | 🟢 Apache-2.0 (10 173 B) |
| **SCORM / cmi5** | `jcputney/scorm-again` · `adlnet/CATAPULT` · `xapijs/cmi5` | 🟢 MIT / Apache-2.0 |
| **CASE 1.1** 🆕 | **`opensalt`** · **`compeito`** · **`OpenCASE`** | 🟢 **MIT / Apache-2.0** |
| **Open Badges 3.0** — *verify* | `credential-lens` | 🟢 MIT (1 080 B) |
| **Open Badges 3.0** — *issue* | 🔴 none — `certo` / `Opencred` / `edubadges-server` | 🔴 AGPL-3.0 |
| **CLR 2.0** — *aggregate* 🆕 | 🔴 **none on a default ref** — see `Gap 301` | 🔴 **empty** |
| **Caliper Analytics** | 🔴 none readable — `1EdTech/caliper-js` behind membership | 🔴 **unreadable, third consecutive pass** |
| **Conformance across all of the above** 🆕 | **`conform-ed/conform-ed`** | 🟢 **MIT (1 080 B)** |

🟢 **Eight of eleven edges are permissive and deployable.** 🔴 **Three are not, and they are the
three a credential engagement needs most:** badge **issuance** (AGPL), CLR **aggregation** (empty),
and Caliper (unreadable). 🔵 **That ratio, not any single row, is the shelf's honest answer to
"can Globant build this on open source?"** — the evidence and description layers yes, the issuance
layer no.

🔴 **Completeness of this pass.** 9 of 9 refs resolved; every licence above read as payload bytes.
🔴 **Not probed:** Common Cartridge (declared by `conform-ed`, no standalone implementation read),
and **Caliper was not re-attempted** — it has failed on three consecutive passes and `P798` says a
fourth identical probe is not a measurement. 🔴 **No star counts** — `api.github.com` returned
`SCOPE_DENIED` this pass (see `agents/top.md`).


## 🟢 Sixty-sixth pass, 2026-10-08 — the standards-layer census gains its **missing tier**: xAPI had a spec and a client on this shelf but **no store**, and the store tier turns out to be the one permissive tier in education infrastructure

⏱️ **Twentieth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **What pass 65 got wrong by omission.** Its five-protocol census read xAPI through
**`adlnet/xAPI-Spec`** (the specification) and **`RusticiSoftware/TinCanPython`** (a client that
*emits* statements). 🔴 **Neither of those stores anything.** A telemetry protocol with a spec and an
emitter and no store is not a usable foundation — it is half an arrow. 🟢 **This pass read the
store tier, and it is the richest permissive tier this shelf has.**

### 🟢 🆕 The LRS tier, every grant read from payload

| Store | ref · HEAD | Licence (payload, bytes) | Engine / stack | Verdict |
|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | `main` · **`cb794e4`** | 🟢 **Apache-2.0** (`LICENSE`, **11 357 B**) | Clojure; **SQLite 3.42 embedded** or **Postgres 14** | 🟢 **the production default** |
| [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | `main` · **`4d18e0c`** | 🟢 **Apache-2.0** (`LICENSE`, **11 357 B**) | TypeScript, **Hono** + Postgres (or **PGlite** embedded) | 🟢 **the forward path** |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | `master` · **`efa045e`** | 🟢 **Apache-2.0** (`LICENSE`, **11 357 B**) | Python / Django | 🟡 **conformance reference**, not a deployment |
| [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) | `main` · **`b1ad9a4`** | 🟢 **MIT** (**three layers**: `LICENSE` **1 066 B** + `composer.json` + packagist) | PHP / **Laravel package** | 🟢 **a package, not a server** — see caveat |
| [`openHPI/openLRS`](https://github.com/openHPI/openLRS) | `main` · **`db284a9`** | 🟢 **MIT** (`LICENSE`, **1 122 B**) | H5P-oriented | 🔴 **archived / read-only** |
| [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | `master` · **`5fec948`** | 🔴 **GPL-3.0** (`LICENSE`, **35 141 B**) | Node / Mongo | 🔴 **copyleft + unmaintained since 2021** |

🔵 **The `EscolaLMS/LRS` caveat matters for shelf placement.** Its README is explicit — install is
`composer require escolalms/lrs`, then a Laravel seeder, and the endpoints it exposes are
**`/api/cmi5/**`** returning `x-experience-api-version: 1.0.3`. 🟢 **So it is an LRS *inside a
Laravel application*, not a standalone store**, and it is **cmi5/xAPI 1.0.3**, not 2.0. 🔵 It earns
its row on the strength of its grant — **three agreeing layers, the cleanest on this shelf** — and
on being the only permissive option for a team already in PHP. 🔴 **It is not a drop-in for
`lrsql`.**

### 🟢 🆕 The one row that changes what this shelf can promise: a **migration path inside one licence**

🟢 `pelotech/xapi-lrs`'s README, read as bytes (18 968 B), states that its bundled schema is
**catalog-parity with `yetanalytics/lrsql` v0.9.5's Postgres shape, CI-enforced**, and that it can
**take over a live `lrsql` database in place** — no dump, no restore, point it at the same
`DATABASE_URL` and run migrations.

🔵 **Why this is a foundations-level fact and not a trivium:** the usual cost of adopting an
open-source store is that leaving it later is a data migration. 🟢 **Here the exit is a no-op**, and
**both ends of it are Apache-2.0** — so the licence does not change across the migration either.

🟢 **What ports, and what does not, from the README's own list:**

| Carries over | Does **not** carry over |
|---|---|
| 🟢 statements, actors, documents | 🔴 **admin accounts** — `lrsql` hashes with a buddy `bcrypt+sha512$...` format `xapi-lrs` cannot verify; existing admin logins **fail 401, not 500** |
| 🟢 **API credentials** — `api_key`/`secret_key` pairs and scopes read as-is from `lrs_credential` / `credential_to_scope`; statement traffic keeps working with **no key re-issuing** | 🔴 **pre-0.6 `xapi-lrs` databases** — v0.6.0 rewrote the schema to match `lrsql` v0.9.5 byte-for-byte; older ones **cannot migrate forward** and the startup probe **refuses to boot** rather than serve a mismatched schema |

🔵 **Bootstrap a fresh admin via `XAPI_LRS_ADMIN_USER` / `XAPI_LRS_ADMIN_PASSWORD`** on startup.
🟡 **Deprecated env prefixes still accepted with a startup warning:** `LRS_*` (shipped in 0.6.0) and
**`LRSQL_*`** (`lrsql`'s own names) both map to `XAPI_LRS_*`, which wins when both are set.

🟢 **`xapi-lrs` also carries what `lrsql` does not:** **xAPI 2.0** alongside 1.0.3, negotiated
per-request via the **`X-Experience-API-Version`** header and **verified in CI against the official
ADL conformance suite**; and **OpenTelemetry** export built in (🟡 default sampler is *every*
request — set `OTEL_TRACES_SAMPLER=parentbased_traceidratio` with `OTEL_TRACES_SAMPLER_ARG=0.1` or
lower before production ingest).
🔴 **Its PGlite mode is single-connection and serialises concurrent transactions** — the README says
local development and low-concurrency only, **not production**. 🔵 Recorded because "zero-dependency
embedded Postgres" reads like a deployment option and is not one.

### 🟢 The five-protocol census, restated with this pass's additions

| Protocol | Reference implementation | Grant | Verdict |
|---|---|---|---|
| **LTI 1.3** | `Cvmcosta/ltijs` — `master` · `0ec24fe` | 🟢 Apache-2.0 (11 361 B) | 🟢 buildable |
| **xAPI** — spec | `adlnet/xAPI-Spec` — `master` · `ca782a1` | 🟢 Apache-2.0 (11 525 B) | 🟢 buildable |
| **xAPI** — client | `RusticiSoftware/TinCanPython` — **`3.x`** · `bbc3f9d` | 🟢 Apache-2.0 (11 358 B) | 🟢 buildable ⚠️ `P793` |
| **xAPI** — **store** 🆕 | `yetanalytics/lrsql` — `main` · `cb794e4` · **and** `pelotech/xapi-lrs` — `main` · `4d18e0c` | 🟢 **Apache-2.0 both** (11 357 B each) | 🟢 **buildable — tier closed this pass** |
| **Open Badges 3.0 / W3C VC** — *verify* | `TanimowoObaloluwaDavid/credential-lens` — `main` · `d34f262` | 🟢 MIT (1 080 B) | 🟢 buildable |
| **Open Badges 3.0 / W3C VC** — *issue* | `certo` `6fd0a11` · `Opencred` `d14619e` · `edubadges-server` `9775cc2` | 🔴 **AGPL-3.0 all three** (33 820 / 34 523 / 34 519 B) | 🔴 **populated, not permissive** 🆕 |
| **Open Badges** — spec | `1EdTech/openbadges-specification` — `develop` · `04c4bc2` | 🔴 no licence file, no licence prose | 🔴 1EdTech Spec Document Licence |
| **Caliper Analytics** — sensor | `1EdTech/caliper-js` | 🔴 **auth challenge on `ls-remote`, second consecutive pass** | 🔴 **not publicly readable** |

🟢 **Score: xAPI is now readable end to end under Apache-2.0 — spec, emitter, and store.** 🔵 **It
is the only education protocol on this shelf that is.** LTI 1.3 is Apache but single-implementation;
Open Badges splits permissive-verify / copyleft-issue; Caliper is unreadable; the Open Badges
specification itself is not open-licensed.

🔴 **The uncomfortable shape, now with a second data point.** Pass 65 observed that the two
protocols analysts call central (Open Badges, Caliper) are the two with the weakest grants. 🟢 **This
pass adds the converse and it is the more actionable half:** the protocol nobody markets — **xAPI,
plumbing, invisible to a buyer** — is the one that is **completely and permissively implemented**.
🔵 **Licence freedom in this industry tracks how little commercial trust a layer carries**, not how
important the layer is. 🔴 **Issuance and analytics certification are where the fences are**, because
those are the layers someone sells.

## 🟢 Sixty-fifth pass, 2026-10-08 — the **standards layer** read by grant for the first time: three of five education protocols have an Apache-2.0 implementation, and the two that do not are the two the analysts call central

⏱️ **Nineteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **Why a standards-layer census, and why it belongs in `foundations`:** every pattern this KB ships
crosses a protocol boundary — a tutor reads a roster, a grader writes a grade, an issuer mints a
credential. 🔴 **Whether that boundary can be crossed in a closed deliverable is a licence question
about the PROTOCOL's implementations, not about the agent on top**, and this shelf had never read it
as one table.

### 🟢 The five protocols, every grant read from payload this pass

| Protocol | Reference implementation | ref · HEAD | Licence (payload, bytes) | Verdict |
|---|---|---|---|---|
| **LTI 1.3** (tool launch) | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | `master` · **`0ec24fe`** | 🟢 **Apache-2.0** (`LICENSE`, **11 361 B**) | 🟢 **buildable** |
| **xAPI** (statement spec) | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | `master` · **`ca782a1`** | 🟢 **Apache-2.0** (`LICENSE`, **11 525 B**) | 🟢 **buildable** |
| **xAPI** (client library) | [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | **`3.x`** · **`bbc3f9d`** | 🟢 **Apache-2.0** (`LICENSE`, **11 358 B**, *"Version 2.0, January 2004"*) | 🟢 **buildable** |
| **Open Badges 3.0 / W3C VC** — *verify* | [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) | `main` · **`d34f262`** | 🟢 **MIT** (`LICENSE`, **1 080 B**; manifest agrees) | 🟢 **buildable** 🆕 |
| **Open Badges 3.0 / W3C VC** — *issue* | `educredentials/ec-issuer` | `main` · **`8bafc99`** | 🟡 **prose-only MIT**, no file, no SPDX key, not on pypi | 🔴 **unprovable** |
| **Open Badges** (specification) | [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) | `develop` · **`04c4bc2`** | 🔴 **NO LICENCE FILE** — 6 names 404, and **no licence prose in the README either** | 🔴 **1EdTech Spec Document Licence** |
| **Caliper Analytics** (sensor) | [`1EdTech/caliper-js`](https://github.com/1EdTech/caliper-js) | — | 🔴 **no ref resolved** on an instrument that resolved 12 of 13 | 🔴 **behind membership** |

### 🔵 The shape of it, and it is uncomfortable

🟢 **The two OLDEST protocols are the two that are cleanly buildable.** LTI 1.3 and xAPI each have an
Apache-2.0 implementation, and xAPI has one at **both** the spec and client layers.

🔴 **The two protocols 1EdTech puts at the centre of 2026 — digital credentials and Caliper
analytics — are the two with no permissive reference implementation this shelf can reach.** Credential
*verification* arrived permissive this pass; credential *issuance* did not; Caliper resolves nothing.

🔵 **That inverts the usual assumption that newer standards are easier to adopt.** 🟢 **The reason is
structural, not accidental:** LTI and xAPI matured under ADL and vendor stewardship that shipped
Apache-licensed code, while the credential and analytics specs sit under the **1EdTech Specification
Document License** with member-gated repositories. 🔴 **A standard that is free to IMPLEMENT is not
the same as a standard with code you may LINK**, and this table is the first time this KB has
separated the two.

### 🟢 `P793` widened again — a **third** non-PHP instance, and this one is a foundation row

🔴 `RusticiSoftware/TinCanPython`'s default ref is **`3.x`** — a **version-named default branch**,
resolved by `ls-remote --symref`, not assumed.

🟢 Pass 63 measured this on 7 of 25 PHP/composer rows and called it ecosystem-concentrated; pass 64
widened it with two non-PHP instances. 🔵 **This is the third, in Python, and it sits on a
FOUNDATION row rather than a trending one** — so the defect reaches the rows most likely to be
copied into a build file. 🔴 **`P793` is no longer plausibly a PHP phenomenon**, and the practical
consequence is unchanged and cheap: **never hardcode `main` or `master` when pinning; resolve the
symref.** A `raw.githubusercontent.com/…/main/LICENSE` against this repository returns **404**, and
a sweep that reads that as *"no licence"* publishes the opposite of the truth.

### 🔴 What this census does NOT establish

🔴 **Currency.** Every row is a HEAD, not a release; nothing here says any of these libraries is
maintained. `TinCanPython` on a `3.x` branch is the row most in need of that check.
🔴 **Completeness.** Five protocols, seven rows — **OneRoster / rostering and SCORM were not probed
this pass**, and both carry client data. 🟢 **`Gap 299`.**
🔴 **Fitness.** A permissive licence says you may link it; it does not say it works. No row here was
executed.


## 🟢 Sixty-fourth pass, 2026-10-08 — **two foundational platforms have a licence file that is a POINTER, and one of the pointers is dangling**; and `P793`'s version-named-default-branch habit is **not PHP-specific**

⏱️ **Eighteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`, `P791`), from pairs:** `raw` four-way
discriminating on one repository (real file **200** / invented path **404** / invented **branch**
**404** / invented **repo** **404**), `pypi` **200 / 404**, `npm` **200 / 404**, `ls-remote --symref`
discriminates **and resolves the default ref**. 🔴 `api.github.com` **403** — no star counts
(`P745`). 🔴 Policy/report hosts **refused at the egress proxy** (`Gap 293`, `intel/market.md`).

### 🔴 `frappe/education` — the whole grant is **19 bytes**, and it is a reference with no body

🟢 **Default ref resolved from the oracle, not guessed:** `refs/heads/`**`develop`** · HEAD
**`444cc8e`**. 🔵 **Not `main`. Not `master`.**

| Grant layer | Measured at `develop` · `444cc8e` | Verdict |
|---|---|---|
| **File** | `license.txt` **200 — 19 B**, whose entire content is `License: GNU GPL V3`. 🔴 `LICENSE` **404**, `LICENSE.md` **404**, `COPYING` **404** | 🔴 **a reference, not a grant** |
| **Manifest** | `pyproject.toml` **200** — `name = "education"`, author *Frappe Technologies Pvt. Ltd.*, `dynamic = ["version"]`. 🔴 **no `license` key** | 🔴 **silent** |

🔴 **Nineteen bytes incorporate no terms.** 🔵 **And the string is under-specified in a way that
matters:** `GNU GPL V3` does **not** say *"or later"*, names **no copyright holder** and gives **no
year**, so the `-only` / `-or-later` question — the one that decides whether a downstream relicensing
path exists at all — **has no answer in the repository.** 🟢 **This is `P742`'s class exactly: a
licence *reference* is not a licence *body*.** 🔴 **Either way it is copyleft, so the practical verdict
does not move: Frappe Education is a self-host substrate, never a component linked into a proprietary
deliverable.** 🔵 **What moves is the confidence**: this row should read `GPL-3.0 (reference only,
19 B, version qualifier absent)` and not `GPL-3.0`.

### 🔴 `openeducat/openeducat_erp` — LGPL-3.0 **confirmed from the body**, while the file's own first line points at a file that **404s**

🟢 **Default ref resolved from the oracle:** `refs/heads/`**`19.0`** · HEAD **`1c95cef`**.
🔵 **A version-named default branch — on an Odoo/Python project.**

| What was read | Result |
|---|---|
| `LICENSE` @ `19.0` | 🟢 **200, 8 241 B** |
| its **first non-blank line** | 🔴 *"For copyright information, please see the COPYRIGHT file."* |
| `COPYRIGHT` @ `19.0` | 🔴 **404 — the pointer is dangling** |
| its **body**, line 4 | 🟢 *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* |
| its **title block**, lines 14–15 | 🟢 *"GNU LESSER GENERAL PUBLIC LICENSE / Version 3, 29 June 2007"* |

🟢 **So the grant is real and the label is right: LGPL-3.0, read from payload body.** 🔴 **And a
reader who trusts the file's own first line is sent to a 404.** 🔵 **The direction of this error is
the benign one** — a dangling pointer loses *attribution* data, not *permission* data — 🔴 **but it is
the same failure mode as `frappe/education` in the opposite order: one file is a pointer with no body,
the other has a body behind a pointer that does not resolve.** 🟢 **Both are only visible to a probe
that reads the payload instead of the first line.**

🟡 **One channel-reported discrepancy, NOT measured here:** OpenEduCat's marketing pages claim **73+
integrated modules** while its GitHub README lists a narrower set (admissions, exams, fees,
attendance, library). 🔴 **No tree enumeration was run this pass**, so this is recorded as a
description-drift *lead* for `compose/code/description-drift-audit/`, not as a finding.

### 🟢 `P793` generalises — the version-named default branch is **not a PHP habit**

🟢 **Pass 63 found 7 of 25 PHP/composer rows served from a ref that is neither `main` nor `master`
(`v31.0.00`, `mobile`, `2.2`, `0.7`, `3.x`, `2.12`, `public`) and concluded the defect was
concentrated in an ecosystem.** 🟢 **This pass adds two non-PHP instances:**

| Repository | Ecosystem | Default ref | A `{main,master}` probe would have reported |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | Odoo / Python | 🔴 **`19.0`** | 🔴 **no licence at all** |
| [`frappe/education`](https://github.com/frappe/education) | Frappe / Python | 🔴 **`develop`** | 🔴 **no licence at all** |

🔵 **So the correction to `P793` is a widening, not a reversal:** the habit tracks **release-branch
discipline**, which PHP/Composer projects adopt most consistently but ERP-shaped Python projects
adopt too. 🟢 **The operational rule is unchanged and now better supported: resolve the default ref
from `ls-remote --symref` before reading any payload, on every ecosystem.** 🔴 **Never probe
`{main,master}` and report an absence.**

🔴 **No rate from these numbers.** 2 of 2 non-PHP platforms probed this pass is not a sampling frame
(`P744`); it is two named repositories, and they are named.

### 🟢 Re-confirmed at a resolved ref — the OneRoster 1.2 server tier

| Repository | Ref · HEAD | Licence (payload, bytes) | Region | Note |
|---|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | `main` · **`6de5476`** | 🟢 **Apache-2.0** (`LICENSE`, **10 173 B**, *"Apache License"*) | **North America** | 🟢 Serves a **OneRoster 1.2** API from an **Ed-Fi ODS** (Data Standard 4.0 and 5.x). 🟢 **Already on this shelf; what is new is the resolved ref and the payload byte count.** 🔵 Channel-reported: its licence notice names **1EdTech Consortium** as copyright holder — a holder/licence pairing worth a `P184` check on a later pass |

🔴 **Still no reachable registry date for the Ed-Fi tier** — `Gap 286` is untouched this pass.

### 🟡 Standing gaps this pass did NOT advance, stated so no reader reads this section as progress

🔴 **`Gap 287`** — `p784` still reads 16 **rooted** filenames only, with no tree and no prose layer.
🔵 **This pass's two findings are exactly what that gap predicts it would miss**: `frappe/education`'s
grant is a non-rooted-name file (`license.txt` is rooted, but the *body* is absent) and
`openeducat`'s is a body behind a dangling pointer. 🔴 **Untouched.**
🔴 **`Gap 288`** — `p441`'s `LICENCE_RE` still matches `extensions/licenseExtension/…`. 🔴 Untouched,
and 🔴 **still the dangerous error direction**, because it *admits* rather than refuses.
🔴 **`Gap 290`** — the seams between this KB's 235+ instruments remain unmeasured.
🔴 **`Gap 257` / `Gap 258`** — the suite board remains unmeasured, and this pass must state **why**
rather than restate the gap: 🔴 **the session this pass ran in refuses to execute the repository's own
test scripts**, so not one suite could be run from the clone. 🟢 **Zero suites this pass, declared as
zero** — pass 63 ran three, and three were not 112; 🔴 **zero is not three.**


## 🟢 Sixty-third pass, 2026-10-08 — the **PHP/composer tier** gets a manifest-layer licence map (25 rows, 19 with a manifest, **10 permissive**), and the provenance under every one of them was wrong: `master` is a **pseudo-ref**

⏱️ **Seventeenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`), `n = 2`:** `raw` **200** against a
404-discriminating control, including **an invented *branch* → 404**; `packagist` **200 × 2 against
its own calibration pair** (`monolog/monolog` **200 × 2**, invented id **404 × 2**); `pypi`
**200 × 2**; `npm` **200 × 2**; `maven` **200 × 2**; `api.nuget.org` **200 × 2**; `ls-remote`
discriminates **and resolves the default ref**. 🔴 `api.github.com/repos/{third-party}` **403 × 2**
— **no star counts** (`P745`). 🔴 Policy and report hosts **`000`, 8 of 8, refused at the egress
proxy** — nothing was measured about those hosts (see `intel/market.md`).

### 🔴 The oracle map's own `packagist` line was wrong for two consecutive passes

| Pass | Line written into the map | What it actually probed |
|---|---|---|
| 61 | `packagist` **404** | `packbackbooks/lti-1-3-php-library` — the **repository slug** |
| 62 | `packagist` **200 × 2 — recovered from pass 61's `404`** | the same slug-shaped id |
| **63** | 🟢 **`packagist` 200 × 2 against a calibration pair** | `monolog/monolog` **200 × 2** · invented id **404 × 2** |

🔴 **Nothing publishes that slug-shaped id** — **404 × 2** on `packagist.org/packages/…json` and
**404 × 2** on `repo.packagist.org/p2/…json`, measured in the same minute the host answered 200 to
a real id and 404 to an invented one. 🟢 **The host never moved.**

🆕 **`P791`: reachability is read off a CALIBRATION PAIR — one id known to exist and one known not
to. A single code from a target id is a fact about that id.** 🔵 `P787` cut reachability by **host**;
this cut runs *underneath* it, because one host served both of pass 61's and pass 62's answers.

🟢 **And pass 62's datum survives, which is what makes this a correction and not a retraction:**
the tree's own `composer.json` at `master` declares **`packbackbooks/lti-1p3-tool`**, that id
answers **200**, newest non-dev release **`v6.4.4`, `2026-09-23T21:17:20Z`**, manifest licence
**`Apache-2.0`**, `repository` resolving back to `packbackbooks/lti-1-3-php-library`
(`master`, `a20c71b`). 🔵 **Right about the package, wrong about the host, and only the second half
went into the map.**

### 🟢 New instrument: `compose/code/p791-registry-id-provenance/` — **37/37 offline**, results committed

🟢 **It imports `p253-registry-first-identity/identity.py` UNCHANGED** and adds the probe layer
`p253` never had (`sweep_identity.sh` speaks only `registry.npmjs.org`). 🔵 **`P713` exactly: re-measure
the DATUM, REUSE the instrument.**

🆕 **`P792` — and this one is about `P713` itself.** 🔴 Running `p253` **end to end** fails:

```
$ sh p253-registry-first-identity/sweep_identity.sh ltijs
ltijs   200   7.0.7   cvmcosta   git+https://github.com/Cvmcosta/ltijs.git   -
→ identity.py: ('PUBLISHED-BY-OTHER',
   'ltijs existe pero apunta a git+https://github.com/Cvmcosta/ltijs.git, no a Cvmcosta/ltijs')
```

🔴 **`PUBLISHED-BY-OTHER` for a package that points at exactly its own repository.** 🔵 The gate
compares `pub_repo` to a **slug**; the probe layer emits a **URL**, which is how npm spells
`repository.url` for nearly everything. 🟢 **`p253`'s committed `result.2026-10-04.tsv` is NOT
wrong** — its `pub_repo` column holds slugs and its one `PUBLISHED-BY-OTHER`
(`algorithm0r/canvas-lms-mcp` → `bruchris/canvas-lms-mcp`) is real. 🔵 **The normalisation was done
by hand and never written into the script, so the committed table is right and a re-run of the
same two files is wrong.**

🔵 **`P792` as a precedent, and it is the complement of `P713`:** *reuse the instrument* is not
enough — **reuse it END TO END**, because the defect can live in the **seam**. 🟢 Pass 59 learned to
`grep` the instruments before announcing a property; pass 63 is the same lesson for an
**interface**. 🟢 **The gate was not edited** — its logic is correct; the fix is a normaliser in the
new probe layer, covering `git+https`, plain `https` and `git@…:` spellings.

🆕 **`P792a`, found the same way:** this script's own first run shifted two columns of
`krayin/laravel-crm`, reporting `latest = Jitendra Singh,devansh.bawari419@webkul.com`. 🔵 Cause:
`set -- $(…)` splits on whitespace and that maintainer string contains a space. 🟢 Fixed with TAB
delimiting; re-measured, the row is MIT, `2.2.x-dev`, `2026-10-07T05:55:14Z`.
🔴 **Both defects were found by RUNNING the thing, not by reading it.**

### 🟢 The PHP/composer tier, manifest layer, 25 slugs this shelf already cites

🔵 **Every `default_ref` below comes from `git ls-remote --symref … HEAD` (`P732`), not from a
branch name**, because of `P793` in the next block. 🔵 **Licence column is the `composer.json`
grant** — a *second, independent* channel from the licence-file reads this shelf already holds.

| Repository | Default ref · SHA | Manifest licence | Declared package | Registry date |
|---|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | `master` · `a20c71b` | 🟢 **Apache-2.0** | `packbackbooks/lti-1p3-tool` | 🟢 **v6.4.4, 2026-09-23** |
| [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | `main` · `0ba4f78` | 🟢 **MIT** | `wikiwijs/php-qti3` | 🟢 **v0.7.0, 2026-09-22** |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | `main` · `f54e292` | 🟢 **MIT** | `grantholle/powerschool-api` | 🟢 **v4.5, 2026-03-18** |
| [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | `main` · `a994e27` | 🟢 **MIT** | `kennisnet/oaipmh` | 🟡 v2.2.3, 2025-09-16 |
| [`php-xapi/model`](https://github.com/php-xapi/model) | 🔴 `3.x` · `e005084` | 🟢 **MIT** | `php-xapi/model` | 🟡 `3.x-dev`, 2025-01-20 |
| [`php-xapi/client`](https://github.com/php-xapi/client) | 🔴 `0.7` · `b39735b` | 🟢 **MIT** | `php-xapi/client` | 🔴 `0.7.x-dev`, 2021-03-24 |
| [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | `master` · `5f975bf` | 🟢 **MIT** | `kennisnet/edurepsearch` | 🔴 v1.0.7, 2022-12-19 |
| [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | `master` · `f328730` | 🟢 **MIT** | `kennisnet/nllom` | 🔴 v1.1.2, 2022-06-28 |
| [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🔴 `2.2` · `fa4eeca` | 🟢 **MIT** | `krayin/laravel-crm` | 🟢 `2.2.x-dev`, 2026-10-07 |
| [`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | `master` · `c9cbfdd` | 🟢 **Apache-2.0** | `imsglobal/lti` | 🔴 **v3.0.2, 2016-09-18** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `main` · `f205347` | 🔴 GPL-3.0-**or-later** | `moodle/moodle` | 🟢 v5.3.0, 2026-10-03 |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `mobile` · `899f6da` | 🔴 GPL-2.0-or-later | `francoisjacquet/rosariosis` | 🟢 `12.9.x-dev`, 2026-09-02 |
| [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | `master` · `7884c3c` | 🔴 **GPL-2.0-only** | `oat-sa/lib-lti1p3-core` | 🟢 v7.3.2, 2026-07-13 |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | `master` · `634a9b8` | 🔴 **GPL-2.0-only** | `qtism/qtism` | 🟢 v19.7.2, 2026-07-09 |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | `master` · `cb64a1f` | 🔴 GPL-3.0 | `h5p/h5p-core` | 🟢 v1.28.0, 2026-03-03 |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 `v31.0.00` · `683d2c4` | 🔴 GPL-3.0 | `gibbonedu/core` → 🔴 **404** | — |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 `2.12` · `cd1da68` | 🔴 GPL-2.0-or-later | `portabilis/i-educar` → 🔴 **404** | — |
| [`leogaggl/lxHive`](https://github.com/leogaggl/lxHive) | `master` · `cffee6d` | 🔴 GPL-3.0 | `g3i/lxhive` → 🔴 **404** | — |
| [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | 🔴 `public` · `e35b0ec` | 🔴 **`proprietary`** | `umich-its-tl/caliper-php` | 🔴 **v1.0.1, 2016-01-27** |
| [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | `master` · `3a192de` | 🟡 none in manifest | `imsglobal/lti-1p3-tool` → 🔴 **404** | — |
| [`3iPunt/wordpress-lti-1-3`](https://github.com/3iPunt/wordpress-lti-1-3) | `master` · `10313a1` | 🟡 none in manifest | `tresipunt/wordpress-lti-1-3` → 🔴 **404** | — |
| [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | `main` · `ab92d85` | 🟡 no `composer.json` | — | — |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | `master` · `5d546f2` | 🟡 no `composer.json` | — | — |
| [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🔴 `develop` · `db41cc4` | 🟡 no `composer.json` at the default ref | — | — |
| [`rachelproject/contentshell`](https://github.com/rachelproject/contentshell) | `master` · `1f3ca1f` | 🟡 no `composer.json` | — | — |

🟢 **10 of the 19 manifest-bearing rows are permissive** (MIT ×8, Apache-2.0 ×2); 🔴 8 are GPL in
four distinct flavours (`GPL-3.0`, `GPL-3.0-or-later`, `GPL-2.0-only`, `GPL-2.0-or-later`) and 1 is
`proprietary`. 🔵 **The `-only` rows matter most architecturally:** `GPL-2.0-only` cannot be
combined forward to GPL-3.0, so `oat-sa/qti-sdk` and `oat-sa/lib-lti1p3-core` are harder to live
beside than the `-or-later` substrates, despite reading as "the same licence" in prose.

### 🔴 `P793` — `master` is a PSEUDO-REF on `raw`, so "payload-read at `master`" was never provenance

🟢 **Measured, 3 of 3, with a 404-discriminating control:**

| Repository | `ls-remote --symref` default | `main` | `master` | `HEAD` | invented branch |
|---|---|---|---|---|---|
| `php-xapi/client` | 🔴 `refs/heads/0.7` (`b39735b`) | 404 | 🔴 **200** | 200 | 404 |
| `tl-its-umich-edu/caliper-php-public` | 🔴 `refs/heads/public` (`e35b0ec`) | 404 | 🔴 **200** | 200 | 404 |
| `portabilis/i-educar` | 🔴 `refs/heads/2.12` (`cd1da68`) | 404 | 🔴 **200** | 200 | 404 |

🔵 **`raw` 404s an arbitrary invented branch but resolves the literal name `master` to the
default**, so a 200 at `master` proves bytes exist and names nothing about where they came from.
🟢 **`P714` warned; this is the measurement.** 🟢 **Defaults that are neither `main` nor `master`:
7 of 25** — including **`v31.0.00`**, a *tag-shaped branch*, on the most widely deployed row in
the table after Moodle.

🟢 **It cuts both ways, and the rescue is the better half of the finding:**
`francoisjacquet/rosariosis` showed **no manifest at all** under a `{main,master}` probe; at its
real default ref `mobile` (`899f6da`) it carries a `composer.json` declaring `GPL-2.0-or-later`,
published **`12.9.x-dev`, 2026-09-02**. 🔵 **A false provenance and a false absence from one cause.**

### 🟡 What this pass does NOT establish

🔴 **No rate is published.** 25 slugs chosen because this shelf already cites them is not a
sampling frame for *"how often a PHP package id differs from its repo slug"* or for *"how often a
default ref is neither `main` nor `master`"*, and `P744`'s denial still forbids the sweep that
would build one. 🟢 **The counts above are over this named population and are stated as counts.**

🔴 **One ecosystem only.** npm, PyPI, Maven and NuGet each spell `repository` their own way; only
composer was swept. 🔵 **`P792`'s defect is npm-shaped**, so the seam most likely to be wrong next
is the one this pass did not re-run.

🔴 **A `404` on a *declared* id is an absence of THAT id, never of the project.** Four rows have no
`composer.json` at the default ref; a manifest may live at depth N and say so, which is precisely
`p253`'s subdirectory finding and was **not** probed here.

🔴 **The agent-discovery channel returned nothing education-specific for a fourteenth consecutive
week** — see `agents/top.md`. 🔵 **None of the rows above is an agent**; they are the integration
substrate agents would have to sit on.

## 🟢 Sixty-second pass, 2026-10-08 — the **credential** edge lands with a permissive stack (6 payload-read rows), the Ed-Fi substrate is completed (4 rows), and the licence gate that admitted them is shown wrong on 2 of 13

⏱️ **Sixteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`), `n = 2`:** `raw` **200** against a
404-discriminating control, `pypi` **200 × 2**, `npm` **200 × 2**, `maven` **200 × 2**,
🟢 `packagist` **200 × 2** (recovered from pass 61's `404`), 🆕 `api.nuget.org` **200 × 2**,
`ls-remote` **discriminates** (real → SHA, invented → fail). 🔴 `api.github.com` **403**.
🔴 Policy/report hosts **`000`, 4 of 4** — every regulatory or survey sentence in this pass is
`reported`, single-channel (`P784`).

### 🟢 Why a credential layer, and why it is the edge with the clearest buyer

🟢 **Pass 61 closed four edges — LTI 1.3 (launch), OneRoster (who), SCORM/cmi5 (content),
xAPI (what happened).** 🔴 **It then searched for the fifth, Caliper Analytics, and found no
permissive implementation at all — `Gap 284`, still open.** 🟢 **This pass went after a different
fifth edge and found the opposite: six permissive implementations, all payload-read.**

🔵 **The question this edge answers is the one that ends an engagement rather than starting it:
*when the learner finishes, what do they walk away with, and can anyone else verify it?*** 🟢 And
unlike the other four, its demand signal is a **named public programme** rather than an inference:
European Digital Credentials for Learning is a central Europass product, resting on the 2022
Council Recommendation on micro-credentials (`intel/market.md`, 🟡 `reported`).

| Repo | Licence (payload · bytes · ref) | Registry date | Region of origin | What it contributes |
|---|---|---|---|---|
| 🆕 [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) | 🟢 **BSD-3-Clause** · 1 524 B · `15fb018` | 🟢 npm **v10.0.2, 2025-11-19** | North America (US · MIT-hosted DCC) | **Issue and verify W3C Verifiable Credentials.** 🟢 The cryptographic core of the edge, and the row whose **registry licence agrees with its payload** — two channels, one answer. |
| 🆕 [`digitalcredentials/verifier-core`](https://github.com/digitalcredentials/verifier-core) | 🟢 **MIT** · 1 086 B (`LICENSE.md`) · `276ebd2` | 🟡 npm **v1.0.0-beta.11, 2025-12-16** | North America (US) | **Verification engine** — status lists, revocation, issuer registries. 🟡 **Beta at ten months**; usable, not stable. |
| 🆕 [`digitalcredentials/issuer-coordinator`](https://github.com/digitalcredentials/issuer-coordinator) | 🟢 **MIT** · 1 086 B · `e663eea` | 🟡 no registry row | North America (US) | **The deployable service** that batches signing behind an HTTP API — the piece that turns the libraries into something a registrar operates. |
| 🆕 [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 **MIT** · 1 091 B · `1c46a82` | 🟡 no registry row | North America (US) | **The learner-side wallet** (mobile). 🔵 The only row on this shelf, at any edge, that the *learner* installs rather than the institution. |
| 🆕 [`digitalcredentials/sign-and-verify`](https://github.com/digitalcredentials/sign-and-verify) | 🟢 **MIT** · 1 074 B · `6be5b41` | 🔴 npm **v0.0.1, 2020-11-08** | North America (US) | 🔴 **Superseded in practice — six years stale on npm while HEAD moves.** On the shelf so a later pass does not rediscover it as live; 🟢 use `vc` + `verifier-core` instead. |
| 🟢 [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 **Apache-2.0** · 13 184 B · `0a66b52` | 🟡 no registry row | North America (US · 1EdTech) | 🔵 **Re-confirmed, not admitted** — already on this shelf. **Conformance validation from the body that authored the spec**, which is the artefact a ministry buyer asks for. |

🟢 **Five admissions and one re-confirmation. Four MIT, one BSD-3-Clause, one Apache-2.0 — nothing
copyleft, nothing NonCommercial, every grant read from payload at a pinned ref.**

### 🟢 The Ed-Fi substrate, completed — and this is a *licence* completion with a measured date gap

🔵 **This KB has carried `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` since the thirteenth pass.**
🟢 **The four repos that make it runnable were never payload-read here. They are now, and all four
are Apache-2.0:**

| Repo | Licence (payload · bytes · ref) | What it contributes |
|---|---|---|
| 🆕 [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 **Apache-2.0** · 10 172 B · `e453cd2` | **The Operational Data Store + REST API** — the core of the US K-12 student-record stack. 3 478 tree paths. |
| 🆕 [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | 🟢 **Apache-2.0** · 10 172 B · `37ff595` | End-user applications and the **extension mechanism** — where a district's local fields live without forking the core. |
| 🆕 [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Docker`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Docker) | 🟢 **Apache-2.0** · 11 356 B · `29c571a` | **Container deployment.** 🔵 The cheapest way to stand the stack up for a pilot; PostgreSQL as well as SQL Server. |
| 🆕 [`Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher) | 🟢 **Apache-2.0** · 11 356 B · `dabdd14` | **ODS-to-ODS replication** between instances of the same version — the district → state-agency hop. |

🔴 **And the gap, measured rather than guessed: not one of them carries a version or date from any
channel this session can reach.** 🟢 The repo's own
`Utilities/SdkGen/EdFi.SdkGen.Console/EdFi.OdsApi.Sdk.nuspec` names the first-party package
**`EdFi.OdsApi.Sdk`, authored "Ed-Fi Alliance"**; 🔴 that exact id returns **`none`** on the
reachable, control-verified NuGet date oracle, `api.github.com` is **403**, `ed-fi.org` is **000**,
and `Application/Directory.Build.props` carries the placeholder `AssemblyVersion 1.0.0`.
🆕 **`Gap 286`** — and the commercial consequence is in `verticals/solutions.md`.

### 🔴 `P787b` / `P788` — the two licence instruments were run **against each other** over all 13 repos, and they disagree twice

🟢 **Both were run over the same 13 slugs, in the same pass: `p784-licence-scope-map` (16 rooted
filenames) and `p441-tree-licence-enumeration` (the complete `git ls-tree -r` of every path).**
🟢 **Reconciled against the committed run** (`compose/code/p786-scope-verdict-agreement/result.2026-10-08.tsv`), **which is stricter than the first reading of it**: the instruments **disagree on 1 of 13**, and are **jointly wrong on a second** — 🔴 **2 of 13 rows are wrong, but only one of them is a *disagreement*.** 🔵 **That distinction is the finding, not a correction of it:**

| Repo | `p784` says | `p441` says | 🟢 What is true, payload-read this pass |
|---|---|---|---|
| 🔴 [`1EdTech/openbadges-specification`](https://github.com/1EdTech/openbadges-specification) `@5f86f31` | 🔴 **`UNGRANTED`** (0 of 16) | 🔴 **`BUNDLED-GRANT-ONLY`**, families **`CC-BY;CC0-1.0`** | 🔴 **Two bespoke non-OSI grants, both of which `p441` found and *rejected*:** `ob_v3p0/license.md` — 🟢 **`200`, 12 324 B, "IMS GLOBAL LEARNING CONSORTIUM, INC. SPECIFICATION DOCUMENT LICENSE"** — and `ob_v2p1/LICENSE-INPROGRESS.md`, 🔴 **"for IMS Global Contributing Member and/or Invited Guests only"** |
| 🔴 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) `@e7736b6` | 🔴 `SINGLE — LGPL-3.0` | 🔴 `OWN-GRANT-AT-ROOT`, `LGPL?` | 🔴 **PARTITIONED, and declared only in prose** (`P786`): library **LGPL-3.0**, five CLI entry points **BSD-2-Clause**, per `wiki/Authors-License-and-FAQ.md` |

🆕 **`P788` — and it is the worse of the two defects, because it admits rather than refuses.**
🔴 **`p441`'s `LICENCE_RE` matches the path `extensions/licenseExtension/…`**, so three
documentation files became *confirmed* grant paths and the repo was reported as **CC-BY / CC0-1.0**.
🟢 **Read this pass, the matched file is not a grant at all** — `extensions/licenseExtension/README.md`
opens *"# Creative Commons Content License … enables **issuers** to indicate what permissions are
granted to the public to reuse **BadgeClass metadata**"*. 🔴 **It documents a badge metadata field.
`p441` turned a schema extension about licences into a licence.**

🔴 **A false *absence* makes a pass refuse a usable repo. A false *presence* makes it ship an
unlicensed one.** 🟢 **So the ordering of the two gaps follows the direction of the error:**
🆕 **`Gap 288`** (`p441`'s false presence, plus its silent rejection of bespoke non-OSI grants)
is declared ahead of 🆕 **`Gap 287`** (`p784` has no tree layer and no prose layer).

🔵 **And `Gap 287` is not a new idea — it is `P441`'s own warning, applied to the instrument built
after it.** `p441`'s README states it in as many words: ***"a filename list can only FIND a licence.
To sustain its ABSENCE you must ENUMERATE the tree"*** and ***"widening a list cannot fix a list."***
🔴 **`p784` was then built, one pass later, as a list of 16 rooted filenames.** 🟢 **This is the
fifth recorded instance of this defect family in this KB, and the first inside its newest gate.**

🔴 **This bears directly on `Gap 285`.** The 8 benchmark repos pass 61 reported as carrying **no
grant at all** were judged by `p784` alone. 🔴 **They have not been tree-enumerated, and there is
now a proven false-absence case to calibrate against** — so "8 ungranted" is an upper bound on
usable repos being refused, not a settled count.

## 🟢 Sixty-first pass, 2026-10-08 — the **content-packaging** layer lands (5 payload-read rows), and a bounded sweep of the benchmark frame finds **48 % of it unusable in a commercial deliverable**

⏱️ **Fifteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Oracle map re-measured before any datum (`P713`, `P745`), `n = 2`:** `raw` **200 × 2** against a
404-discriminating control, `pypi` **200 × 2**, `npm` **200 × 2**, `repo1.maven.org` **200**,
`ls-remote` **discriminates** (real → SHA, invented → fail). 🔴 `packagist.org/packages/{pkg}.json`
**404** this pass where pass 59 read it — recorded, not explained. 🔴 Primary policy hosts
**`000`, 12 of 12** — but see `Gap 270`, **re-posed** this pass: the cause is the **channel**.

### 🟢 Why a content-packaging layer, and why it was the last one missing

🟢 **Pass 60 closed the loop LTI → OneRoster → xAPI**: the tool launches, the roster says who the
learner is, the LRS records what happened. 🔴 **What no layer on this shelf answered is how the
*learning content itself* arrives and reports** — which is the one thing every incumbent client
already has thousands of units of, authored to **SCORM** and increasingly **cmi5**. 🔵 A
customisation engagement that cannot ingest a client's existing SCORM estate is not a
customisation engagement.

| Repo | Licence (payload · bytes · ref) | Registry date | Region of origin | What it contributes |
|---|---|---|---|---|
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** · 1 072 B · `a882b22` | 🟢 npm **v3.4.5, 2026-10-05** | North America (US) | **SCORM 1.2 / 2004 + AICC run-time, in JavaScript.** 🟢 **Three days old at this pass and the freshest row on the whole shelf** — the live option for replaying a client's existing SCORM estate beside a new agent. |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | 🟢 **Apache-2.0** · 11 358 B · `806c0ba` | 🟡 no registry | North America (US ADL Initiative) | **cmi5 player prototype + conformance test suites**, from the body that authored cmi5 and xAPI. 🔵 Value is **conformance evidence**, which is what a ministry or defence buyer asks for. |
| [`xapijs/cmi5`](https://github.com/xapijs/cmi5) | 🟢 **MIT** · 1 070 B · `5ea9bda` | 🟡 npm **v1.4.0, 2024-10-06** | 🟡 unplaced | cmi5 profile library, reported complete against **cmi5 Quartz 1st Edition**. 🔴 **Two years without a release** — carried as usable, not as live. |
| [`xapijs/xapi`](https://github.com/xapijs/xapi) | 🟢 **MIT** · 1 071 B · `5e28e9b` | 🟢 npm **v3.0.3, 2026-04-27** | 🟡 unplaced | The xAPI **client** under the same org, and the maintained half of the pair. 🟢 Pairs with pass 60's `lrsql` / `ralph` rows: client here, store there. |
| [`PerfectlyNormal/scorm`](https://github.com/PerfectlyNormal/scorm) | 🟢 **MIT** · 1 079 B · `9149389` | 🟡 no registry | EMEA (Norway) | Ruby SCORM **package** parser/builder. 🔴 **Copyright line reads 2013** — on the shelf for the Ruby estates that exist, not as a recommendation. |

🟢 **All five are permissive and none is copyleft**, which continues `P763`'s finding that the
**protocol edges are permissive while the substrates are copyleft** — now across four protocols.

### 🆕 `P780` — the **registry** layer resolves *slugs*, not just dates, and that makes it an identity oracle

🟢 **Measured this pass.** `ls-remote` could not find a Caliper or cmi5 implementation under any
name this pass guessed: `Brightspace/ims-caliper-python`, `xapijs/xAPI.js`, `1EdTech/caliper-java`
and `IMSGlobal/caliper-java` **all returned nothing**. 🟢 **`registry.npmjs.org/@xapi%2fcmi5`
returned the real slug in its `repository` field — `xapijs/cmi5`** — and the payload read followed
immediately. 🆕 **So the registry is not only the one *dated* oracle (`P741`); it is a *naming*
oracle, and it is the cheaper way in when a project has been renamed or re-orged.**

🔴 **And the counter-case, in the same pass, which keeps `P253` honest:** `pypi.org/pypi/caliper/json`
answers **200** — and it is **`vsoch/caliper`, "a tool for measuring and assessing change in
packages"**, nothing to do with 1EdTech Caliper Analytics. 🆕 **`P780b`: a registry `200` establishes
that *a package of that name* exists, never that it is the artefact you were looking for.** Identity
needs the `repository` field or the payload, not the HTTP status.

### 🟢 `Gap 282` — **CLOSED** by an instrument, and the phenomenon it names turns out to be **rare**

🟢 **`compose/code/p784-licence-scope-map/` enumerates all 16 licence filenames instead of breaking
on the first, and emits a `{path → family}` map with a `SINGLE | PARTITIONED | UNGRANTED` verdict.**
🟢 **17 assertions, offline, green.** It reproduces every verdict pass 60 derived by hand — including
`leogaggl/lxHive` as **GPL-2.0**, the licence that *three consecutive hand-rolled classifiers*
(passes 58, 59, 60) read as LGPL.

🟢 **Then it was run on a bounded, pre-declared frame** — the **23** benchmark / dataset / evaluation
repos on this shelf, selected by name before any payload was read, which is `P744`'s named-sample
method rather than the mass enumeration `P744` forbids. 🟢 **23 of 23 reachable.**

| verdict | n | share |
|---|---|---|
| 🟢 `SINGLE` | **14** | 61 % |
| 🔴 `UNGRANTED` — no grant at any of 16 filenames | **8** | **35 %** |
| 🟡 `PARTITIONED` | **1** | 4 % |

🔴 **So `Gap 282`'s phenomenon is 1 in 23 on the very frame where `P779` predicts it is most
likely.** 🟢 **That is a real result and it reprioritises:** the scope split is worth an instrument
(it now has one) and is **not** worth a pre-flight row of its own. 🔵 **The instrument earned its
cost by measuring that its own motivating phenomenon is rare — and by finding, in the same run,
something an order of magnitude more common.**

### 🆕 `P782` — **48 % of this shelf's benchmark frame cannot ship in a commercial deliverable**, and the reason is almost never a licence this KB was watching for

🟢 **Families across the frame, `n = 23`, every one payload-read:**

| grant | n | may Globant build a paid deliverable on it? |
|---|---|---|
| 🟢 **MIT** | 10 | 🟢 yes |
| 🟢 **Apache-2.0** | 2 | 🟢 yes |
| 🔴 **no grant at all** | **8** | 🔴 **no — all rights reserved** |
| 🔴 **CC BY-NC 4.0** | 1 | 🔴 no — *"Commercial use is strictly prohibited"*, read from a 312 B payload |
| 🟡 **MIT code / CC BY-NC-SA 4.0 data** | 1 | 🟡 architecture yes, corpus no |
| 🔴 **bespoke, non-SPDX** | 1 | 🔴 **no** — see `P783` |

🟢 **12 of 23 (52 %) are permissive. 11 of 23 (48 %) are not usable as-is in a paid deliverable.**
🔴 **And the dominant failure is not an awkward licence — it is the *absence* of one**: 8 repos,
**0 of 16 filenames and no packaging manifest**, which is `P760`'s young-research-repo shape and
means all rights reserved.

🔴 **The 8 ungranted, named so this is auditable:** `AI-EDU-LAB/E-EVAL` `@8351bd4`,
`AI-for-Education/Luganda-linguistic-benchmarks` `@d4f3a68`,
`AI-for-Education/fabdata-llm-retrieval` `@577f77c`, `aiverify-foundation/LLM-Evals-Catalogue`
`@cec508e`, `eth-lre/mathtutorbench` `@6faed17`, `kaushal0494/AITutor-EvalKit` `@a710784`,
`malaysia-ai/malaysian-dataset` `@87c0562`,
`master72o/universal-llm-evaluation-rubric-library` `@5a1500a`.

🔵 **The engagement consequence, stated plainly:** when a client asks *"how will you prove the
tutor is accurate?"*, half this shelf's answer cannot be used in the deliverable that answers.
🟢 **The 12 that can** are `AI-for-Education/edu-qurating` · `pedagogy-benchmark` ·
`voice-ai-evaluation-framework` (MIT), `DFE-Digital/education-benchmarking-and-insights` (MIT),
`baker-jr-john/automated-summary-evaluation-llm` (MIT), `eduagarcia/lm-evaluation-harness-pt` (MIT),
`latam-gpt/lm-evaluation-harness` · `latam-gpt/syco-bench` (MIT),
`markm-io/ai-essay-evaluator` (MIT), `shivanireddyk/tutoreval` (MIT),
`indobenchmark/indonlu` (Apache-2.0), `prometheus-eval/prometheus-eval` (Apache-2.0).

### 🆕 `P783` — the binding grant in education AI is often **not an SPDX family at all**, and a classifier that guesses here is the most expensive bug available

🔴 **`Khan/tutoring-accuracy-dataset` `@fbbeff8` ships a 2 690 B `LICENSE` that is a bespoke
Khan Academy *"Evaluation Dataset License"*, read in full this pass.** Its terms, quoted:

- 🔴 **"Use of the Dataset shall be restricted to internal non-commercial evaluation of models."**
- 🔴 **"use for model training, or any production use … is expressly prohibited"**
- 🔴 **"any re-distribution or publication … is expressly prohibited"**
- 🔴 **not sublicensable**
- 🔴 **viral:** *"any such modified, merged, or combined dataset containing any portion of the
  Dataset remains subject to this license"*
- 🟢 **permitted, and worth knowing:** evaluating products *intended* for commercial use, and
  commercial use of the *insights* gained.

🟢 **`p784` emitted `UNCLASSIFIED` on this payload, which is the correct answer and the designed
one** — `unknown → UNCLASSIFIED, never a guess` is an asserted case in its suite. 🔴 **Every
SPDX-shaped classifier on this shelf would have had to either guess or fall through**, and the
cheapest wrong guess here — "no recognised copyleft marker, treat as permissive" — would have
published a row licensing a client to do the two things this licence most explicitly forbids:
**train on it and ship it**.

🆕 **`P783` stated for reuse: in education AI, assume the corpus carries a bespoke evaluation
licence until a payload read says otherwise. The correct classifier output for a bespoke grant is
a refusal to classify, and the correct next step is a human reading the 2 690 B.**

## 🟢 Sixtieth pass, 2026-10-08 — the **learning-record / rostering** layer enters the shelf (6 rows, all payload-read), and a **dual-licence** repo defeats every probe this KB has written

⏱️ **Fourteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Why this layer is foundational and not an agent row:** every recipe in `compose/patterns.md`
ends at a model or an agent, and then has nowhere to *write*. An LRS (xAPI) is where learner events
land; OneRoster is how classes, teachers and enrolments arrive. 🔴 **Neither layer had a single row
on this shelf before this pass** — which is why the recipes integrated with "the SIS" in prose.

### 🆕 `P772` — a **scope-partitioned dual-licence** repo defeats a first-match licence-file probe, and `p759`'s four layers have no layer for it

🟢 **Measured first-hand, both payloads SHA-pinned at `865bc35`:**

| path | title line | bytes | scope, per README `## License` |
|---|---|---|---|
| `LICENSE` | `Attribution-NonCommercial-ShareAlike 4.0 International` | **2 244 B** | 🔴 **dataset** — graph, benchmark, training data |
| `LICENSE-CODE` | `MIT License` | **1 075 B** | 🟢 **code** — "this repository" |

🔴 **A probe that stops at the first of 15 filenames reads `LICENSE` and returns `CC BY-NC-SA 4.0`
— and wrongly rejects usable MIT code.** 🔴 **A probe that happened to order `LICENSE-CODE` first
would return MIT — and wrongly admit an NC dataset.** Both directions are wrong, and the repo is
honest: the README states the split at lines 291–292 and the badge points at the NC file.

🟢 **`p759`'s four layers are file → below-reference → manifest → headers.** 🔴 **None of them is
"more than one licence file, each governing a different artefact"** — the layers are about *where a
grant hides*, and this is about *what a grant covers*. 🆕 **Declared `Gap 282`: scope, not location,
is a fifth axis**, and the bounded remedy is to enumerate **all** matches of the 15 filenames rather
than break on the first.

🔵 **The engagement consequence, stated plainly:** for an education benchmark the **data licence is
usually the binding one**, because the asset a client wants is the corpus. 🟢 **MIT code + NC corpus
is a shippable architecture with an unshippable dataset** — the same shape as `Gap 272`'s ArguLens
(Apache-2.0 code, CC BY-NC-SA PERSUADE 2.0). 🟡 **Two instances in one pass makes it a pattern worth
a pre-flight, not a coincidence.**

### 🟢 Rows admitted — learning-record stores (xAPI), the layer that was missing

| Repo | Licence (payload · bytes · ref) | Region of origin | What it contributes |
|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** · 11 357 B · `cb794e4` | North America (Yet Analytics, US) | **SQL-backed LRS.** 🟢 **The permissive row this layer needed** — runs on an RDBMS the client already operates, so no new datastore in the architecture. |
| [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 **MIT** · 1 094 B · `53cc58c` | EMEA (France Université Numérique) | LRS **plus** a learning-analytics toolkit. 🟢 **The most permissive row on the layer, and EMEA-origin** — relevant where data residency and an EU-funded provenance both matter. |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 **Apache-2.0** · 11 357 B · `efa045e` | North America (US ADL Initiative) | The **reference** LRS from the body that authored xAPI. Python. 🟡 Value is conformance, not throughput. |
| [`leogaggl/lxHive`](https://github.com/leogaggl/lxHive) | 🔴 **GPL-2.0** · 18 092 B · `cffee6d` | APAC (Australia) | Lightweight PHP/MongoDB xAPI LRS, OAuth 2.0, pluggable storage. 🔴 **GPL-2.0, and the source that named it said "GPL v3"** — see `P773`. Carried as the measured correction, not as a build-on candidate. |

### 🟢 Rows admitted — OneRoster / rostering, the SIS-facing edge

| Repo | Licence (payload · bytes · ref) | Region of origin | What it contributes |
|---|---|---|---|
| [`longsightgroup/oneroster`](https://github.com/longsightgroup/oneroster) | 🟢 **MIT** · 1 090 B · `8c14777` | North America (Longsight, US) | TypeScript OneRoster client. 🟡 Reported **v0.3.0, July 2026**, adding **REST clients alongside CSV** — the two ways schools actually exchange rosters. 🟢 **The freshest row on this layer.** |
| [`TCI/OneRoster`](https://github.com/TCI/OneRoster) | 🟢 **MIT** · 1 079 B · `5f8a15a` | North America (TCI, US) | Ruby OneRoster API wrapper: students, teachers, classes, courses, enrolments. |

🔴 **Two rostering defects recorded rather than carried as rows:** the **ClassLink** Ruby/PHP
examples sit behind a developer centre its own notice says is **inaccessible after 2024-04-01**, and
the **Ed-Fi** OneRoster service is documented as *"built from the open-source project"* **without
naming a repository**. 🟢 **Neither becomes a row** (`P476`).

### 🟢 Dataset / benchmark row, with its split stated

| Repo | Licence (payload · bytes · ref) | Region | What it contributes |
|---|---|---|---|
| [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) | 🟢 **code MIT** (`LICENSE-CODE`, 1 075 B) · 🔴 **data CC BY-NC-SA 4.0** (`LICENSE`, 2 244 B) · both `865bc35` | APAC (Peking University) | **Curriculum-aligned knowledge graph for benchmarking educational LLMs.** 🔵 The first row on this shelf that is explicitly a *curriculum-aligned* evaluation asset — which is what a ministry-facing engagement is asked for. 🔴 **NC on the data**: usable to evaluate, not to resell. |

## 🟢 Fifty-ninth pass, 2026-10-08 — `Gap 273`'s **213 ungranted** splits into **three measured classes**, and the named-sample method `P744` demanded is the one that did it

⏱️ **Thirteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `P760` — the three classes, each from a named sample read first-hand

🔴 **Pass 58 left `Gap 273` with its bound "looser" and no method, because `P744` had ruled out
another whole-tree sweep (the request classifier denies mass third-party slug enumeration).**
🟢 **Named samples work, and four of them resolve the class structure:**

| Class | Named sample | What the layer found | Rescued? |
|---|---|---|---|
| **1 — grant below a reference, same file** | `openeducat/openeducat_erp` @ `1c95cef` | `LICENSE` 8 241 B opens with a `COPYRIGHT` pointer that `404`s; the grant is **below it, in the same file** | 🟢 **Yes — LGPL-3.0** (pass 58's `P742`, re-confirmed here) |
| **2 — grant only in source headers** | `onbirdev/moodle-webservice_mcp` @ `198246e` | **0 of 15** licence filenames; no manifest; **every** `.php` header carries *«GNU General Public License … either version 3 … or any later version»* | 🟢 **Yes — GPL-3.0-or-later** (`P757`) |
| **3 — genuinely ungranted** | `Hieub26/IELTS-Writing-Part-1-Scoring` @ `a988441`, `Guo-coding/llm-l2-essay-scoring` @ `d619b16`, `master72o/universal-llm-evaluation-rubric-library` @ `5a1500a` | **0 of 15** licence filenames **and** no `setup.py` / `pyproject.toml` / `package.json` / `LICENSES/` / `licenses/` / `docs/` / `src/` grant | 🔴 **No — all rights reserved**, 3 of 3 |

🟢 **So the registry/tree layer is not a uniform rescue:** it rescued **2 of 5** named samples, and
the **3 it did not rescue share a property** — they ship **no packaging manifest at all**, which is
typical of young research repos. 🔵 **That is the operational split `Gap 273` was missing:
the 213 contains a *packaged* sub-population the registry layer can adjudicate and an
*unpackaged* one where "no payload grant" is already the final answer.**

🔴 **No rate is published from this.** 🟢 **Five named samples are not a sample frame**, and
`P744`'s denial still forbids the sweep that would produce one. 🆕 **Succeeded by `Gap 277`.**

### 🟢 `P761` — the foundational shelf re-read from payload, with `P753`'s title-line rule applied

🔴 **This matters here more than anywhere else on the KB**, because this shelf's two most-used
substrates are the exact pair `P753` confuses:

| Repo | Licence (**title line**, not a substring test) | stored B | HEAD sha | layer |
|---|---|---|---|---|
| `moodle/moodle` | **GPL-3.0** — `COPYING.txt` | 35 147 | `f205347` | LMS substrate |
| `openedx/edx-platform` | **AGPL-3.0** | 35 136 | `bf699a5` | LMS substrate |
| `instructure/canvas-lms` | **AGPL-3.0** | 34 520 | `1c9f0bb` | LMS substrate |
| `openeducat/openeducat_erp` | **LGPL-3.0** | 8 241 | `1c95cef` | education ERP |
| `learningequality/kolibri` | **MIT** | 1 097 | `6cfad10` | offline-first delivery |
| `HKUDS/DeepTutor` | **Apache-2.0** | 11 408 | `6cf793b` | tutoring agent |
| `pykt-team/pykt-toolkit` | **MIT** | 1 066 | `77c3e90` | knowledge tracing |

🔴 **`moodle` ships its grant as `COPYING.txt`** — the exact filename `P727` identified as the
omission that biases a blind spot into the copyleft family. 🟢 **Read here deliberately, and
`moodle` is `GPL-3.0`, *not* AGPL**, despite its payload naming Affero three times (`P753`).

### 🟢 The grant-oracle layer, re-measured this pass (`P713` — never inherited)

| Oracle | Result | Discriminates? |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 `200` | 🟢 Yes — `404` on a non-existent slug |
| `git ls-remote` | 🟢 **OK** | 🟢 Yes — fails on a non-existent slug |
| `pypi.org` | 🟢 `200` | 🟢 Yes — `404` on `pylti1.3` (`P743`) |
| `registry.npmjs.org` | 🟢 `200` | — |
| `repo.packagist.org` | 🟢 `200` | — |
| `api.github.com` | 🔴 `403` | — |
| `arxiv.org` | 🔴 `000` | — |
| 6 named primary policy hosts | 🔴 `000`, **6 of 6** | — |

🔵 **`git ls-remote` works this pass.** 🟡 **That is the fourth recorded inversion of this one
capability** (pass 53 "only oracle that works" → pass 54 the one that fails → pass 56 noise →
here, working). 🟢 **It is load-bearing now, not incidental:** it is what supplies the `refs/heads`
SHA that `P732` requires, and with `api.github.com` at `403` it is **the only** SHA oracle
available here.

### 🔴 The mandated foundational query, and the honest result for the **seventh** pass running

🟢 `open source platform education ERP CRM MIT Apache` returned **OpenEduCat** (vendor glossary
pages in six languages), **CK-ERP** (a 2010 mailing-list post), a 2017 teaching-ERP paper, and a
general CRM directory. 🔴 **No Apache-licensed education ERP exists in the channel's answer, for
the seventh pass** — 🟢 **and `P761` now explains why that is a real property and not a query
defect: the education ERP band is `LGPL-3.0`, and `verticals/solutions.md` `P747a` is where that
pays.**


## 🔴 Fifty-eighth pass, 2026-10-08 — the census's **213 ungranted** is an upper bound that just got **looser**, and the first repo re-read moved out of it into **LGPL-3.0**

⏱️ **Twelfth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

> 🔵 **This pass's opening hypothesis was that `Gap 273` — "the 213 have not been run through the registry and tree layers, the cheapest remaining licence work on this KB" — could be closed this pass.
> 🔴 **REFUTED on feasibility (`P744`), and the sample that *was* readable immediately moved a repo out of the ungranted class.**

### 🔴 `P742` — one of the three named ungranted repos was never ungranted

🟢 **`openeducat/openeducat_erp`, re-read from payload this pass: **LGPL-3.0**, 8 241 B, the grant body present in the same `LICENSE` file whose `COPYRIGHT` reference `404`s.** 🔴 **Pass 57 resolved the reference, found it missing, and filed the repo as having no grant.** 🟢 **Line 4 of that file reads *"published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below"* — and it is included below.**

🔵 **Why this lands on the foundations shelf specifically:** 🟢 **OpenEduCat is an education-native ERP built on the Odoo framework, and it is one of the few education platforms this KB can place in the **weak-copyleft** band rather than the strong one.** 🔴 **Mis-filed as ungranted, it reads as unencumbered; read correctly, it is LGPL-3.0 — a materially different planning input from Moodle's GPL-3.0 and Canvas's AGPL-3.0 (`P734`), because LGPL's trigger is **linking**, not use or service (`verticals/solutions.md`, `P747`).**

🔴 **And the correction needed no oracle at all (`P752`):** 🟢 **eight instruments on this shelf already held `openeducat/openeducat_erp  LICENSE  8241  LGPL` in committed TSVs — 31 lines in total — and `licence-grant-gate/README.md` had recorded the exact `COPYRIGHT`-reference trap beside the correct `LGPL-3.0` verdict.** 🔵 **So this shelf's ungranted bound was loosened not by a better probe but by **reading what the repository already contained**.** 🟢 **New offline gate: `compose/code/p752-prose-vs-committed-results/`, `--self-test` 4/4.**

### 🟢 `P730` revisited — the census direction holds, the ungranted bound does not

🟢 **The payload census of pass 57 is **not** retracted. Re-stated with this pass's correction applied:**

| Census class (pass 57, 1 020 slugs) | Status after pass 58 |
|---|---|
| 🟢 **Permissive 74,0 %** of the 807 with a readable payload | 🟢 **HOLDS** — unchanged, and the mandate's "focus on MIT / Apache / BSD" remains satisfied by the shelf as it stands |
| 🔴 **Copyleft 16,9 %** | 🟡 **A floor, not a level** — every correction so far (`P727`'s three repos, now `openeducat`) has moved repos **into** this class, never out |
| 🔴 **213 with no grant locatable** | 🔴 **An upper bound, now demonstrably loose** — 🟢 **1 of the 3 named members re-read this pass carries a grant** |
| 🔴 **45 AGPL** | 🟢 **HOLDS** as the number to plan around |

> 🔴 **`P730a`.** *Every licence-instrument defect this KB has found points the **same way**: 🔴 **toward under-counting copyleft.** 🟢 **`P727` (`COPYING.txt` omitted) moved `moodle`, `nvda` and `languagetool` out of "ungranted" and into **GPL**. `P742` moves `openeducat` out and into **LGPL**.*** 🔵 **Four repos, four copyleft, zero permissive — because the conventions these instruments miss (`COPYING.txt`, attribution split from grant) **are** the GNU conventions.* 🟢 **So the honest reading of "213 ungranted" is not "213 unknown": it is **"213 unknown, skewed copyleft"**, and a team treating that bucket as low-risk has the risk exactly inverted.**

### 🟢 `P741` — the registry layer works, demonstrated on three named packages

🟢 **The half of `Gap 273` nobody had run. PyPI returns a grant from packaging metadata — a different host and a different artefact from the repository `LICENSE`:**

| Package | Registry grant | Field | Version | Last upload |
|---|---|---|---|---|
| `autorubric` | 🟢 **MIT** | `license_expression` + OSI classifier | 1.6.1 | 🟢 **2026-09-27** (11 days) |
| `rubric` | 🟢 **MIT** | `license_expression` + OSI classifier | 2.2.0 | 🟡 **2026-01-21** |
| `PyLTI1p3` | 🟢 **MIT** | `license` + OSI classifier | 2.0.0 | 🔴 **2022-11-20** |

🟢 **All three agree with the repository payload where one exists**, so the registry is a **corroborating** oracle here, not a contradicting one (contrast `P445` classifier-divergence). 🔴 **It also carries the one datum the payload never does: a date.**

### 🔴 `P744` — why `Gap 273` cannot be closed here, and what replaces it

🔴 **The commands that enumerate the shelf's 218 `NONE` slugs into a worklist were **denied by the environment's own request classifier**, twice, under two distinct reasons — while individually named probes stayed fully functional and `raw.githubusercontent.com` answered `200` on every probe of this pass.** 🟢 **Reachability and permission are orthogonal (`P744`, `agents/top.md`).**

🟢 **Stated as a planning fact for later passes:**

| `Gap` | Shape | Closeable here? |
|---|---|---|
| 🔴 **`Gap 273`** (213 ungranted → registry + tree layers) | Full-shelf sweep | 🔴 **No** — policy-denied. 🟢 **Re-scope to named samples** |
| 🔴 **`Gap 271`** (193 `UNPARSED_ASSERTION` + `NO_README`) | Full-shelf sweep | 🔴 **No** — same shape, same denial |
| 🟢 **`Gap 273a`** 🆕 | **Named-sample** grant-body re-read, `n` declared, **no rate published** | 🟢 **Yes — this pass performed it on 5 repos** |

🔴 **And the discipline that goes with it:** 🟢 **because the 213 could not be enumerated, this pass's five repos are a **named convenience sample**. 🔴 **One retraction in three named rows is not a 33 % shelf error rate, and no such rate is published.** 🔵 **Pass 57 earned its headline by publishing its sweep's false-positive rate alongside its count; the equivalent discipline for a convenience sample is to publish **no rate at all**.**

🆕 **`Gap 277` — the `tree` half of `Gap 273` (`p441-tree-licence-enumeration`, grants in `LICENSES/` subtrees and `setup.py` classifiers) is still unrun on **any** sample, named or swept.** 🟢 **It is now the cheapest remaining licence work, inheriting the title `Gap 273` held.**

---


## 🟢 Fifty-seventh pass, 2026-10-08 — the shelf's **licence-family census**, measured from payload for the first time: **74 % permissive**, and **one repo in five has no locatable grant**

> 🔵 **This pass's opening hypothesis was that the foundations shelf's licence column was broadly
> right and the question was which rows to add.
> 🟡 CONFIRMED on direction, REFUTED on completeness.** 🟢 **Sweeping all **1 020** shelved slugs
> (`P725`) produced the first payload-measured census this KB has ever had of what it is actually
> standing on — and the finding is not the permissive share, it is the **213 repos with no grant
> this environment can locate**.

### 🟢 `P730` — the census: what the 1 020 shelved repos actually grant

🟢 **Every family below read from the licence **payload** at `HEAD`, never from prose, a badge, or a
GitHub sidebar (which is `403` here). 🟢 **19 filenames tried per repo**, `COPYING.txt` included
after `P727`:**

| Family | n | % of 1 020 |
|---|---|---|
| 🟢 **MIT** | **423** | **41,5 %** |
| 🔴 **no payload locatable** | **213** | **20,9 %** |
| 🟢 **Apache-2.0** | **147** | 14,4 % |
| 🔴 GPL | 67 | 6,6 % |
| 🔴 **AGPL** | **45** | 4,4 % |
| 🟡 unclassified (`OTHER`) | 40 | 3,9 % |
| 🟡 CC (content) | 34 | 3,3 % |
| 🟢 BSD | 21 | 2,1 % |
| 🔴 MPL | 13 | 1,3 % |
| 🔴 LGPL | 8 | 0,8 % |
| 🟢 Unlicense · ISC · WTFPL | 3 · 2 · 1 | 0,6 % |
| 🔴 EPL | 3 | 0,3 % |

🟢 **Grouped, over the **807** slugs that have a readable payload:**

| Group | n | % of 807 with payload |
|---|---|---|
| 🟢 **Permissive** (MIT · Apache · BSD · ISC · Unlicense · WTFPL) | **597** | 🟢 **74,0 %** |
| 🔴 **Copyleft** (GPL · AGPL · LGPL · MPL · EPL) | **136** | 🔴 **16,9 %** |
| 🟡 Content (CC) | 34 | 4,2 % |
| 🟡 Unclassified | 40 | 5,0 % |

> 🟢 **`P730`.** *Three quarters of what this KB shelves is permissive, so the mandate's
> "focus on MIT / Apache / BSD" is **satisfied by the shelf as it stands**, not aspirational. 🔴 **But
> `AGPL` at 45 repos is the number to plan around**: it is the one family where *hosting* a service
> triggers the obligation, and education delivery is hosted by default.* 🔵 **`MIT` at 41,5 % is also
> the reason `P725`'s misgrants matter: MIT is what a README claims when it is wrong.**

🔴 **The 213 are an upper bound on "ungranted", not a count of it.** 🟢 **Stated precisely: *no grant
was locatable at 19 filenames at `HEAD`*.** 🔵 **A grant may still live in a subdirectory, a
`setup.py` classifier, a registry record, or a sibling `LICENSES/` tree** — this KB's own
`p441-tree-licence-enumeration` and `p440-unlicensed-registry-grant` exist precisely because those
layers carry grants. 🆕 **`Gap 273` — the 213 have not been run through the registry and tree
layers, which is the cheapest remaining licence work on this KB.**

### 🟢 `P727a` — three foundational repos were wrongly readable as ungranted, and all three are copyleft

🟢 **Corrected by `P727`'s filename fix and re-read first-hand:**

| Foundational repo | Grant, read first-hand | Bytes (stored) | Filename |
|---|---|---|---|
| **`moodle/moodle`** | 🔴 **GPL-3.0** | **35 147** | 🟢 `COPYING.txt` |
| **`nvaccess/nvda`** | 🔴 **GPL** (53 408 B — carries appended terms) | **53 408** | 🟢 `copying.txt` |
| **`languagetool-org/languagetool`** | 🔴 **LGPL family** | **26 432** | 🟢 `COPYING.txt` |

🔵 **Moodle is the single most-cited platform on this KB**, and a sweep that mis-filed it as
ungranted would have been the most consequential error of the pass. 🟢 **It was caught by the
filename fix, which is why `P727` is written as a sampling-frame rule rather than a typo.**

### 🟢 Foundational rows measured first-hand this pass, with the **AGPL** layer called out

🟢 **All read from payload at `HEAD`, stored bytes (`P704`):**

| Repo | Grant (payload) | Bytes | Note for a Globant engagement |
|---|---|---|---|
| **`INGInious/INGInious`** | 🔴 **AGPL** | **34 764** | Auto-grading platform. 🔴 **Hosted grading = §13 triggers.** Self-host for a client **on the client's own infrastructure**, or keep it an internal oracle |
| **`edx/ease`** | 🔴 **AGPL** | **35 136** | Essay-scoring library, archived. 🟢 **Channel claim and payload agree** — recorded as a positive control on the prose channel |
| **`codelitdev/courselit`** | 🔴 **AGPL** | **34 143** | Course platform — same hosting constraint |
| **`datacamp/catsim`** | 🔴 **GPL** | **35 147** | CAT / item-response simulation, via `COPYING` |
| **`SafeExamBrowser/seb-server`** | 🔴 **MPL** | **16 725** | File-level copyleft — safer than AGPL, still not permissive |
| **`Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration`** | 🟢 **Apache-2.0** | **11 357** | Rostering integration |
| **`eduNEXT/openedx-lti-tool-plugin`** · **`Pearson-Advance/openedx-lti-tool-plugin`** | 🟢 **Apache-2.0** | **11 357** each | LTI tool plugins for Open edX |
| **`dmitry-viskov/pylti1.3`** (+ django/flask examples) | 🟢 **MIT** | **1 070** each | 🟢 **LTI 1.3 in permissive Python** — the integration primitive |
| **`LibreTexts/LibreOne`** | 🟢 **MIT** | **1 067** | Identity / SSO for an OER estate |
| **`AI-for-Education/fabdata-parsedoc`** | 🟢 **MIT** | **1 065** | Document parsing aimed at education content |
| **`ScottDaniels/labaaoom`** | 🟢 **BSD** | **2 266** | — |
| 🟡 **`Khan/tutoring-accuracy-dataset`** | 🟡 **unclassified**, 2 690 B | 2 690 | 🔴 **Read before use** — a dataset grant, not a code licence; `p317-data-license-layer` applies |

> 🔵 **The engagement-relevant split is not permissive-vs-copyleft, it is **hosted**-vs-shipped.**
> 🔴 **Every AGPL row above is a platform a client would *host*, which is exactly where §13 bites**,
> while the permissive rows are libraries you *link*. 🟢 **So the shelf's AGPL concentration is in
> the platform layer and its MIT concentration is in the integration layer** — plan the architecture
> around that, not around a licence count.

## 🟢 Fifty-sixth pass, 2026-10-08 — **one row added**, and the shelf's provenance convention upgraded from branch name to **commit SHA**

⏱️ **Tenth pass of this date.** 🟢 **One row added** — the mandated foundations channel is saturated
for the seventh week, but a narrower assessment query yielded a repo that three oracles confirm.
🔴 **What changed structurally is more important than the row:** this shelf's provenance format was
**not reproducible**, and now is.

### 🔴 Why `main/LICENSE` was never provenance (`P714`)

🟢 **`raw.githubusercontent.com` aliases `master` to the default branch.** 🟢 **Four repos measured,
none with a `refs/heads/master`, all returning byte-identical `200` from `master/LICENSE`:**

| Repo | `master` head exists? | `main/LICENSE` | `master/LICENSE` | default ref |
|---|---|---|---|---|
| `The-LLM-Data-Company/rubric` | 🔴 no | **1 077 B** | 🔴 **1 077 B** | `refs/heads/main` |
| `CAHLR/OATutor` | 🔴 no | **1 105 B** | 🔴 **1 105 B** | `refs/heads/main` |
| `Dmoayad/essay-grader-llm` | 🔴 no | **35 149 B** | 🔴 **35 149 B** | `refs/heads/main` |
| `scaleapi/researchrubrics` | 🔴 no | **1 078 B** | 🔴 **1 078 B** | `refs/heads/main` |

🟢 **A nonexistent non-alias branch `404`s**, so the oracle discriminates *arbitrary* branch names
but not the `master` alias.

> 🔴 **`P714`.** *A branch name cannot be falsified by the payload it returns. 🟢 **Provenance on this
> shelf is therefore `repo + path + byte count (stored, `P704`) + commit SHA`**, and the SHA comes
> from `ls-remote`, which `P713` confirmed working `6/6`.* 🆕 **`Gap 268`: the 643 rows already
> shelved carry no SHA, so none is reproducible against a moved default branch.**

### 🟢 Row added this pass

| Repo | Licence (read first-hand) | Holder | Signal | What it is |
|---|---|---|---|---|
| https://github.com/The-LLM-Data-Company/rubric | 🟢 **MIT** · `LICENSE` **1 077 B** stored / 1 076 stripped · SHA **`eb0755a1`** | *The LLM Data Company, 2025* | **84 refs** · PyPI **v2.2.0**, `license_expression: MIT` | Provider-agnostic Python library scoring text against **weighted rubrics**. 🟢 **The missing scoring primitive under `P710`** — it does not know what a student is, which is exactly why it composes. |

🟢 **Admitted on three agreeing oracles** (payload, PyPI registry, `ls-remote`) — the shelf's standing
bar since `P456`. 🟢 **Its README badge points at a `LICENSE` that exists**, which is the
discriminator `P702` lacked.

### 🔴 Re-confirmed, and one correction propagated

🟢 **`CAHLR/OATutor` MIT `1 105 B` holds** (stored convention, `P704`).
🔴 **`CAHLR/OATutor-Content` remains the shelf's sharpest trap** — no licence file, a blanket
`CC BY 4.0` README grant, and a per-item grant holding for **75,7 %** of 13 371 problems (`P703`).
🟢 **The adoptable unit is the item, not the repo.**
🔴 **`Dmoayad/essay-grader-llm` is `GPL-3.0` (35 149 B payload), not the MIT its README claims**
(`P715`) — the existing `⚠️` row is confirmed, not changed.

### 🔴 Byte counts on this shelf corrected to the declared convention

🔴 **`P724` (`agents/top.md`): `P704` declared the **stored** convention (trailing newline included)
and 3 of its 4 rows were published **stripped**.** 🟢 **Corrected, re-read first-hand, SHA-pinned:**
`AITutorAgent` **1 072 B** (`09fdd672`), `open-learning-ai-tutor` **1 069 B** (`5709ef2c`),
`OpenTutor` **1 068 B** (`5fea390a`). 🟢 **`OATutor` **1 105 B** (`939eb0e3`) was already correct.**
🔵 **The figures moved by one byte each; the point is that a stated convention needs a check, not
that the licences changed — all four remain `MIT License` by payload.**

### 🔵 What the mandated foundations channel returned, and why nothing came from it

🟢 **`open source platform education ERP CRM MIT Apache`, globally and per region.** 🔴 **Every named
project is already shelved:** `openeducat/openeducat_erp` (**LGPL-3.0**, not permissive),
Frappe/ERPNext education module, Apache **OFBiz** (Apache-2.0), **Aureus ERP** (MIT),
**Huly** (Apache-2.0), Odoo. 🟢 **The channel's own conclusion matches this shelf's standing
finding:** *"None of the results show an education-specific ERP/CRM released under MIT or
Apache 2.0."* 🔵 **That is the seventh week of the same structural answer, and it is recorded as a
confirmed structural fact rather than as a channel failure.**

## 🟢 Fifty-fifth pass, 2026-10-08 — **no new row**, and the shelf's licence column re-derived from payload with its measurement convention named

⏱️ **Ninth pass of this date.** 🔴 **No row added**: the mandated foundations channel is saturated for
the sixth week and every education-specific repo it named is already shelved (`agents/trending.md`).
🟢 **What changed is provenance quality** — licences re-read first-hand, and the byte-count
convention that was silently producing contradictions is now stated.

### 🟢 Why this shelf can read grants this pass (`P700`)

🟢 **Measured, not inherited:** `raw.githubusercontent.com` **`200`** and `404`-discriminating,
`pypi.org` **`200`**, 🆕 `registry.npmjs.org` **`200`**, 🆕 `repo.packagist.org` **`200`**, and
🟢 **`git ls-remote` WORKS** — which pass 54 measured as failing. 🔴 `api.github.com` and `github.com`
remain `403`, and `codeload.github.com` is **`403`**, so no star figure is published.

🔵 **The two new registries matter to *this* shelf specifically:** 🟢 **Packagist answers for the PHP
platforms (Moodle, Krayin) and npm for the JS layer** — so a dependency-level licence question is
answerable here again without the GitHub API.

### 🟢 `P704` — the convention this shelf was missing

🔴 **`p322` published `1 104 B` and `agents/top.md:1284` published `1 105 B` for the same
`CAHLR/OATutor` `LICENSE`.** 🟢 **Both are correct: `1105` is the file as stored, `1104` is the
payload with its trailing newline stripped** — `curl | wc -c` versus `printf '%s' "$(curl)" | wc -c`.

> 🟢 **This shelf now publishes the file as stored, including the trailing newline, and says so.**
> 🔴 **A provenance figure without its convention invents disagreements between correct readings.**

### 🟢 Licences re-derived from payload this pass

| Repo | Licence (first-hand, file as stored) | Holder | Standing |
|---|---|---|---|
| https://github.com/CAHLR/OATutor | 🟢 **MIT** · `main/LICENSE` **1 105 B** | Zachary A. Pardos — CAHL research lab, 2023 | 🟢 holds · 🔴 **read `P703` on its content submodule before deploying** |
| https://github.com/Ebimsv/AITutorAgent | 🟢 **MIT** · `main/LICENSE` **1 071 B** | Ebrahim Mousavi, 2025 | 🟢 holds · 🟡 1 ref |
| https://github.com/mitodl/open-learning-ai-tutor | 🟢 **MIT** · `main/LICENSE` **1 068 B** | Romain Puech, 2024 | 🟢 holds · 🟢 66 refs, MIT Open Learning provenance |
| https://github.com/zijinz456/OpenTutor | 🟢 **MIT** · `main/LICENSE` **1 067 B** | Zijin Zhang, **2026** | 🟢 holds · 🟢 newest grant on the shelf |
| https://github.com/apache/ofbiz-framework | 🟢 **Apache-2.0** · `trunk/LICENSE` **11 905 B** | ASF | 🟢 holds — 🔴 **general ERP, not education** (`P708`) |
| https://github.com/delip/autorubric | 🟢 **MIT** — cross-checked on PyPI this pass: **v1.6.1**, `license: MIT`, 9 releases | Rao & Callison-Burch, UPenn | 🟢 **pass 54's row confirmed still live** |

🔴 **Explicitly NOT shelved, with reasons, so the next pass does not re-litigate them:**

| Repo | Why not |
|---|---|
| `kaushal0494/AITutor-EvalKit` | 🔴 **No grant text.** 5 licence paths `404`; `pyproject.toml`/`setup.py` `404`; README asserts MIT twice and its badge links to a missing `LICENSE` (`P702`). 🆕 `Gap 265` |
| `hulylabs/huly` | 🔴 **No payload.** 4 licence paths `404` on `main`; the Apache-2.0 claim is secondary prose only (`P709`) |
| `frappe/erpnext` | 🔴 **GPL-3.0** (`develop/license.txt`, **35 148 B**). 🟢 Education-specific and genuinely capable — but a copyleft decision, not a drop-in (`P708`) |

🔵 **Fewer real rows beat padding:** 🟢 **six verified rows re-derived and three explicit refusals is
this pass's honest yield**, and the refusals carry more decision value than a seventh row would.

## 🟢 Fifty-fourth pass, 2026-10-08 — **one new row**, and the shelf's whole licence column is promoted from *asserted* to *read*

⏱️ **Eighth pass of this date.** 🟢 **One row added** — the first in five passes. 🟢 **Seven licence
cells re-derived from their own payloads**, which this shelf has not been able to do since pass 51.

### 🟢 Why this shelf can suddenly do its job again (`P639`)

🔴 **Pass 53 recorded that no licence could be read first-hand here** and fell back to existence
checks. 🟢 **Measured this pass: `raw.githubusercontent.com` answers `200`** (and `404` on a
nonexistent repo, so it discriminates), and **`pypi.org` answers `200`**. 🔴 **What actually broke is
`git ls-remote`**, the oracle pass 53 named as the only working one.

🔵 **This shelf's question is *"may Globant build on it"*, and that question is answered by a
**grant**, never by a repository's existence.** 🟢 **So for three passes this shelf was confirming the
wrong property.** `P639` is the correction, and the lesson is that an environment capability must be
re-measured each pass rather than inherited.

### 🟢 `P640` — the new row, and it is a **layer**, not another entry

| Repo | Licence (read first-hand) | Why it is foundational |
|---|---|---|
| https://github.com/delip/autorubric | 🟢 **MIT** — 4 independent oracles | **Rubric-based evaluation of LLM/VLM output**: binary / ordinal / nominal criteria, configurable weights, single- and multi-judge ensembles, few-shot calibration, documented **position-** and **verbosity-bias** mitigations. COLM 2026, arXiv `2603.00077`. PyPI `autorubric` **v1.6.1**, uploaded **2026-09-27**, 9 releases. |

🟢 **The four oracles**, because a foundational row should carry its provenance: `main/LICENSE`
(1 402 B, `MIT License`); `README.md` line 195 (*"MIT License"*); `pyproject.toml`
(`license = "MIT"` **and** `License :: OSI Approved :: MIT License`); PyPI JSON
(`license_expression: MIT`). 🔵 **No third-party directory was trusted for any of them.**

🟡 **Declared about the row itself:** the MIT text names **two** copyright holders — Delip Rao for
changes after the fork from `rubric` v1.2.8, and The LLM Data Company for v1.2.8 and earlier.
🟢 **Forked-provenance MIT: one grant, two holders, split by version** — so an attribution line that
names only the fork author is incomplete (`P255`'s shape; detail at `P640`, `agents/top.md`).

🔵 **Why a foundations shelf wants a scorer.** 🔴 **Assessment is the one education function the EU
AI Act lists in Annex III as high-risk**, and this shelf could name a tutor, an authoring tool and an
SIS but **not one licensed thing that produces a grade**. 🟢 **That cell is now filled, permissively,
by a maintained package** — which is the difference between recommending an assessment pipeline and
being able to ship one.

### 🟢 Re-verified this pass — the six live recommendations, now **with their grants**

🟢 **6 / 6 reachable, and 6 / 6 licences read from the payload** (pass 53 could only prove they
resolved):

| Repo | Licence, first-hand | Shelf consequence |
|---|---|---|
| https://github.com/grant-mccurdy/instructional-ai-workflows | 🟢 **MIT** | 🟢 build on freely |
| https://github.com/MicroPyramid/Django-CRM | 🟢 **MIT** | 🟢 build on freely |
| https://github.com/wwrwbs/AI_AWE | 🟢 **Apache-2.0** (1 865 B) | 🟢 build on freely, patent grant |
| https://github.com/openeducat/openeducat_erp | 🟢 **LGPL-3.0** (8 241 B, named at line 4) | 🟡 link a separate process |
| https://github.com/macsnoeren/genai-open-assessment | 🟡 **GPL-3.0** (35 149 B) | 🔴 strong copyleft — do not vendor |
| https://github.com/GarethManning/education-agent-skills | 🔴 **CC-BY-SA-4.0** (1 230 B) | 🔴 **content licence, ShareAlike** |

🔴 **The last row changes a recommendation this shelf was making without qualification.** Its licence
scopes itself to *"the educational skills, documentation, examples, and curriculum materials in this
repository"*, and **nothing in its 1 230 B carves out code**. 🟢 **So ShareAlike reaches anything
derived from it** — usable **as material**, wrong shape to vendor into a product. 🆕 **`Gap 262`.**

🟢 **And one near-miss published with its method (`P644`):** this pass's first-line extraction on
`openeducat` returned *"For copyright information, please see the COPYRIGHT file."*, which **looks
like** a contradiction of pass 53's LGPLv3 quote. 🟢 **It is not** — the naming is at **line 4**, and
the payload is **8 241 B, byte-identical to pass 53's figure.** 🔵 **A first-line heuristic is not a
licence reading**, and recording the near-miss is cheaper than letting a later pass rediscover it.

### 🔴 The mandated foundational query, and the honest result for the fifth pass running

🔴 **`open source platform education ERP CRM MIT Apache` returned no new permissive education
platform** — **fifth consecutive pass.** 🔴 **This pass's run was worse than usual: ten of the ten
results were the same vendor's glossary page in ten languages** (`openeducat.org/*/glossary/*`),
which is a saturated index, not a channel.

🟢 **Stated rather than padded.** The channel's nearest permissive fits remain **Apache OFBiz**
(Apache-2.0) and **Aureus ERP** / **Krayin** (MIT) — all general-purpose, **none with an education
domain model** — and all already on this KB's shelves. 🟢 **`P631` is unmoved: this shelf is still
never both permissive and educational.** 🔵 **Fewer real rows beat padding — no second row was
added.**

🔴 **Declared limit on the new row's own neighbours:** `emorynlp/LLM-Grading` and
`wenjing1170/llm_grader` were both candidates for this shelf and **both were refused for cause** —
no `LICENSE` under four filenames on two branches, and no licence string anywhere in either README,
so they are **all rights reserved** rather than "unknown" (`P641`). 🟢 **A refusal with a measured
reason is a shelf result.**

## 🟡 Fifty-third pass, 2026-10-08 — **no new foundational row**, and the pass's contribution to this shelf is that its licence column got a reader it was missing

⏱️ **Seventh pass of this date.** 🔴 **Zero rows added.** 🟢 **One column strengthened across every
LGPL row this shelf will ever hold.**

### 🟢 `P634` — the licence column can now distinguish `LGPL-2.1` from `LGPL-3.0`

🔴 **Before this pass, every LGPL payload that named its version in a *title block* rather than in
the full licence text was recorded by the shared classifier as bare `LGPL`.** 🟢 **Now the version
is read** — from a title stub, a numeric stub, or a prose grant (`P634`, `agents/top.md`).

🔵 **Why a foundations shelf cares:** this shelf's job is to answer *"may Globant build on it"*, and
for the LGPL family the answer turns on the **version**, not the family. 🟢 **`LGPL-2.1` is now an
emittable, allow-listed answer** (`p411-cession-identity-gate`), where before it was a string this
KB's own gate would have rejected as unknown.

🔴 **Measured limits, declared:** the **declaration** branch (an SPDX-style `lgpl` token in a
manifest, not a licence text) still answers `LGPL (declaracion)` with **no version**. 🔵 **Out of
scope this pass and recorded so no later pass assumes it covered.**

### 🟢 Re-verified this pass — six live-layer recommendations, `6/6` reachable

🟢 `git ls-remote` over every repository named in the live opportunity blocks
(`P638`, `agents/top.md`): `grant-mccurdy/instructional-ai-workflows`,
`openeducat/openeducat_erp`, `MicroPyramid/Django-CRM`, `macsnoeren/genai-open-assessment`,
`wwrwbs/AI_AWE`, `GarethManning/education-agent-skills`. 🔴 **Existence only** — `github.com` HTML
is `400` here and every non-GitHub host is `000`, so no licence was re-read first-hand this pass.

### 🔴 The mandated foundational query, and the honest result

🔴 **`open source platform education ERP CRM MIT Apache` returned no new permissive education
platform for the fourth consecutive pass.** 🟢 **Stated rather than padded:** the channel's
nearest permissive fits are **Apache OFBiz** (Apache-2.0) and **Huly** (Apache-2.0), both
general-purpose and both already on this KB's shelves; **Aureus ERP** (MIT) likewise, with **no
education module**. 🔵 **Fewer real rows beat padding** — no row was added.

## 🟢 Fifty-second pass, 2026-10-08 — the foundational shelf gains **one** row, and the pass's real yield is a **verdict class** the shelf did not have

⏱️ **Sixth pass of this date.** Payloads read 2026-10-08 from `raw.githubusercontent.com`, status and
byte count per filename. **No star counts (`P479`).**

🔴 **The mandated foundations query returned nothing new**, for the fifth consecutive pass and for the
reason passes 48–51 recorded: the global channel answers with *courses* and *catalogues*
(`microsoft/generative-ai-for-beginners`, `LLMs-from-scratch`, `karpathy/nanochat`,
`developer-roadmap`, `caramaschiHG/awesome-ai-agents-2026`), all already filed. 🟢 **The row below
came from a task-shaped query instead** — see `agents/trending.md` for why that distinction is now
recorded as method.

### 🟢 The one admission

| Repo | Refs (`P510`) | Grant | Family | Why it is a *foundation* and not just an agent |
|---|---|---|---|---|
| 🟢 🆕 [`grant-mccurdy/instructional-ai-workflows`](https://github.com/grant-mccurdy/instructional-ai-workflows) | **1 head**, `refs/heads/main` = `a4c5e832` | `LICENSE` **1,070 B** `sha256 a8d6cd41…` | 🟢 **MIT** for code | 🟡 **Admitted as a *pattern source*, not a runtime.** It supplies the four-stage shape an assessment pipeline needs — rubric evidence → feedback drafting → reviewer packet → remediation action — with **human review named at each stage**. 🟢 That shape is the scarce thing; `compose/patterns.md` `P632` wires it |

🔴 **And the obligation that travels with it (`P627`):** the same repo ships **two further grants** —
`LICENSE-CONTENT.md` (**662 B**, `sha256 c8b2ae96…`) and `LICENSE-DATA.md` (**722 B**,
`sha256 79fe1044…`), both **CC BY 4.0**, covering the written documentation, diagrams, generated
charts and the **original synthetic datasets**. 🟢 **The code may ship closed. The rubric content and
the synthetic student records may not be used without attributing Grant McCurdy.**

### 🔴 `P629` — the shelf now has a verdict for *"exists, and grants nothing"*

🔵 **Two refusals were measured this pass, and they are different refusals.** The shelf had been
recording both as *"not added"*, which is a disposition, not a reading.

| Slug | Refs | What the tree says | Family | Shelf verdict |
|---|---|---|---|---|
| 🔴 [`GradeAI/gradeai`](https://github.com/GradeAI/gradeai) | **1 head**, `main` = `4de8e861` | 🔴 **full `--filter=blob:none` tree enumeration finds no licence path at all**, and `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`, `COPYING.txt`, `legal/LICENSE` return **404 ×6** | 🔴 **UNLICENSED** | 🔴 **Refused.** Absent a grant, the default is all rights reserved — a public repo is not a licensed one |
| 🔴 [`michael-borck/assessment-rubrics-for-ai`](https://github.com/michael-borck/assessment-rubrics-for-ai) | **1 head**, `main` = `00294979` | `LICENSE.md` **200**, **2,859 B**, 92 lines | 🔴 **PROPRIETARY** | 🔴 **Refused.** Curtin-University-internal; the payload itself lists `✗ Commercial use` and `✗ Distribution to other institutions` |

🟢 **The distinction is operational, not taxonomic.** `UNLICENSED` is *read the whole tree, there is
no grant*; `PROPRIETARY` is *read the grant, and it refuses*; `UNKNOWN` is *not read*. 🔴 **Only the
third justifies another probe.** The first two are settled, and a shelf that files them as `UNKNOWN`
will keep paying for probes that cannot change the answer — and will present them to a human as
*licence not determined*, which reads as permission.

### 🟢 `P629`'s negative control ran in the same sweep

🟢 `gmilano/education-kb-NEGATIVE-CONTROL-no-existe-52` → **0 refs**, while `Dolibarr/dolibarr` → **64**
(🔵 **63 last pass — the one movement a ref count showed this week**), `idempiere/idempiere` → 27,
`krayin/laravel-crm` → 7. 🟢 **So a 404 *path* on a live repo is distinguishable from a dead slug**,
and `GradeAI/gradeai`'s six 404s are a real repo's real silence rather than a bad slug. 🔵 **The
suite asserts exactly that**, `compose/code/p627-multi-grant-repo/` — 🟢 **31/31 green, offline**.

### 🟢 `P630` — the shelf's MIT rows, and why their byte counts must stop being compared directly

🔵 **The shelf carries three MIT payloads within 2 B of each other and had no account of the spread.**
🟢 Now it does, measured:

| Payload | Bytes | Final byte | Holder line | Length |
|---|---|---|---|---|
| 🆕 `grant-mccurdy/instructional-ai-workflows` | **1,070** | `0x0a` | `Copyright (c) 2026 Grant McCurdy` | **32** |
| `Django-CRM/Django-CRM` | 1,069 | `0x0a` | `Copyright (c) 2017 MicroPyramid` | 31 |
| `MicroPyramid/opensource-startup-crm` | 1,068 | 🔴 `0x2e` (no final newline) | `Copyright (c) 2017 MicroPyramid` | 31 |

🟢 **`diff` is clean apart from the copyright line in all three**, and the deltas decompose exactly:
`+1` holder character and `+1` newline for the first pair, a **pure newline** for the second.
🔴 **So the two 1 B steps on this shelf have different causes**, and no tolerance band on bytes
distinguishes an MIT payload from a non-MIT one. 🟢 **`P627` is a third independent MIT supplier** by
holder — Grant McCurdy, against `MicroPyramid` (pass 51) and `Webkul Software` (pass 46) — which is
what `P564` asked this shelf to find.

### 🔴 Declared gaps

- 🔴 **Still no permissively licensed, education-domain *platform* on this shelf** — the admission
  above is a pattern source, not a system. The ERP/CRM layer remains generic (see
  `verticals/solutions.md`).
- 🔴 **`package.json` is present in `grant-mccurdy/instructional-ai-workflows` and was not read for
  a `license` field this pass.** Single channel, stated rather than implied.
- 🔴 **`creativecommons.org` measured `000`**, so the CC BY 4.0 family is read from the repo's own
  side-car payloads and not corroborated against the licence steward.

## 🟢 Fifty-first pass, 2026-10-08 — the foundational shelf's **licence-version coverage** was overstated, and the 6.3 % of rows that broke it share one property

⏱️ **Fifth pass of this date.** Payloads read 2026-10-08 from `raw.githubusercontent.com` at `HEAD`,
status and byte count per filename. **No star counts (`P479`).**

🔵 **The mandated foundations query returned nothing new**, for the reason passes 48–50 recorded: the
global channel answers with *courses* and *catalogues* (`microsoft/generative-ai-for-beginners`,
`LLMs-from-scratch`, `rohitg00/ai-engineering-from-scratch`, `caramaschiHG/awesome-ai-agents-2026`),
all already filed. 🟢 **So this pass measured the shelf instead of extending it, and the measurement
moved five rows.**

### 🟢 `P620` — `6.3 %` of the shelf ships its grant as **Markdown or HTML**, and that is where the version column is empty

🔵 **The rule is `p419`'s and it is not changed here:** the family is read from the **header** — title
plus `Version N`, the first two non-empty lines — never from the body, because a pristine licence
text names its relatives (GPL-3.0 §13 names AGPL; GPL-2.0 closes naming the Lesser GPL). `p419`'s own
suite refuted a wider window, so `n=2` is measured, not chosen.

🔴 **The window was measured on plain text.** A `LICENSE.md` need not be plain text.
`idempiere/idempiere` opens its with `<center>`, so the two lines the window admits are `<center>`
and the title — and `Version 2, June 1991` falls outside. The answer is `GPL-?`: *names GPL without a
version, not inferred (`P286`)*. 🔵 **A legal answer, which is why no suite went red, and the one that
stops a commercial verdict.**

🟢 **`compose/code/p620-licence-header-window/` — suite 🟢 30/30, offline.** Repair is a pre-stage
(drop markup-only lines, strip inline tags and Markdown lead markers), then `p419`'s **unmodified**
`familia()` (`P126`). Measured over every `.md`/`.html` licence payload in
`p444-root-vs-tree-family/payloads.licensed.2026-10-07.tsv` — **26 of 412 rows** — plus the two
`idempiere` payloads: **28 payloads, all 200.**

| Verdict | n | |
|---|---|---|
| `AGREE` | **22** | no markup in the window; the repair is a no-op |
| 🟢 `REPAIRED` | **5** | a licence **version** recovered |
| 🔴 `WINDOW-STILL-SHORT` | **1** | `idempiere/idempiere` `license.html` — **declared blind spot** |

🔴 **The blind spot is published, not cured.** `license.html`'s first heading is
**`Compiere Public License`** (iDempiere's lineage runs Compiere → ADempiere → iDempiere) and its
second is `GNU General Public License`, so after the strip the window holds two licence **titles**
and the version is *still* outside. 🔴 **Widening to `n=3` would pass it and re-admit body text,
recommitting `P419`'s original defect** — the suite's own refuted `n=6` case. Left red.

🟡 **And the `22 AGREE` is not `22 identified`.** 7 of the 28 answer `UNCLASSIFIED` both raw and
unwrapped, two of which `p444`'s body-reading `family_of` calls `CC-BY`
(`Jona-Zwetsloot/Somtoday-Mod`, `sign/translate`). A header rule cannot name a grant that has no
title line; the two instruments answer different questions, and that is recorded rather than
reconciled.

### 🔵 `P621` — and this explains an anomaly the shelf's **size** column had been carrying unexplained

🟢 **The four repaired Moodle rows are exactly the GPL size outliers** — `35,178` ×3 and `32,477`
against a modal `35,149`. 🔵 **They are outliers because they are Markdown wrappers.** One property,
two symptoms: a missing version and an anomalous byte count. **The size column never carried a
file-format axis**, so the variance read as noise.

🔴 **Which collapses the byte tolerance this corpus had been using as corroboration.** Five GPL-3.0
payloads read today span **34,674 → 35,151 B** (SPDX's own reflowed canonical at the bottom,
`Dolibarr/dolibarr` `develop/COPYING` at the top), two *different* payloads measure exactly 35,148 B,
and the shelf's own GPL rows already spanned **35,065 → 35,199 B over 11 distinct sizes**.
🟢 **`P420` was right that size does not identify; this pass shows it from the other side — same
licence, five sizes — and names `Dolibarr`'s payload as the SPDX-conformant specimen to stage in
future.** Arithmetic: `agents/top.md`, `P621`.

## 🔴 Fiftieth pass, 2026-10-08 — the shared licence classifier read the **family** and invented the **version**, on the branch pass 46 did not audit

⏱️ **Fourth pass of this date.** Licences read first-hand on 2026-10-08 from payload and from model
metadata, HTTP status recorded per filename **and per git ref**. **No star counts** (`P479`).

### 🔴 `P613` — `GNU GENERAL PUBLIC LICENSE 3.0` answered **`GPL-2.0`**, and 152 passing assertions never saw it

🔵 **Found by a real payload, not by a test.** The `r2.8` tag of `UD_Spanish-AnCora` carries a
**68-byte** `LICENSE.txt`:

```
GNU GENERAL PUBLIC LICENSE 3.0
http://www.gnu.org/licenses/gpl.html
```

Fed to `lib/license_family.sh::family_of` — the **shared, hardened** classifier whose own header
says *"source this, do not rewrite it"* — the answer was 🔴 **`GPL-2.0`**.

🔴 **The defective line, verbatim, as it stood:**

```bash
if printf '%s' "$t" | grep -qi 'GNU GENERAL PUBLIC LICENSE'; then
   printf '%s' "$t" | grep -qi 'Version 3' && echo "GPL-3.0" || echo "GPL-2.0"; return; fi
```

🔴 **The version read required the WORD `version`.** A payload that names the version as a **number**
does not contain it, so the probe fell to the `||` and **stamped `GPL-2.0`**.

🟢 **This is `P561` verbatim** — *"the shared classifier read the licence family and invented the
version"* — which pass 46 found and closed **for MPL and EPL**. 🔴 **It did not audit the GNU
branch, and the GNU branch had the same defect all along.**

### 🔴 Why 152 assertions scored 152/152 while this was live — measured, not supposed

| Input class | Example | Verdict before the fix |
|---|---|---|
| **canonical full texts** | SPDX `GPL-3.0-only` (34 674 B), `GPL-2.0-only` (17 337 B), `AGPL-3.0-only`, `LGPL-3.0-only` | 🟢 **all four CORRECT** |
| **title stubs, numeric version** | `GNU GENERAL PUBLIC LICENSE 3.0` (the real AnCora payload) | 🔴 **`GPL-2.0`** |
| **title stubs, `v3` form** | `GNU General Public License v3.0` | 🔴 **`GPL-2.0`** |
| **title stubs, `GPLv3` form** | `GNU GENERAL PUBLIC LICENSE` + `GPLv3` | 🔴 **`GPL-2.0`** |
| **title stubs, spelled** | `GNU GENERAL PUBLIC LICENSE, Version 3` | 🟢 correct — **the only stub form that worked** |

🔴 **Four of five real stub forms failed.** 🟢 **And every canonical text passed**, because the FSF
texts all spell *"Version 3, 29 June 2007"* in words. 🔵 **This is `P126` pt. 2 exactly: a classifier
validated only on the shape you have fixtures for scores 100% while broken.** The stubs are what
**treebanks and datasets** publish, which is precisely the corpus tier this KB spent passes 45–49 on.

🔴 **The direction of the error is the commercial consequence.** GPL-2.0 and GPL-3.0 are **mutually
incompatible**, and the error pointed at the **older** licence — the one with no patent grant and no
anti-tivoization clause. 🔴 **A studio that priced an obligation off this verdict priced the wrong
licence.**

### 🟢 The fix, and the precision measurement that licensed it

🔵 **The easy fix is to widen the version probe, and the easy fix is how `P171` got introduced.** So
the widening was measured against the payload it could steal first:

| Token | Occurrences in the **canonical GPL-2.0** text (17 337 B) |
|---|---|
| `version 3` | 🟢 **0** |
| `v3` | 🟢 **0** |
| `gplv3` | 🟢 **0** |
| `3.0` | 🟢 **0** |
| `License 3` | 🟢 **0** |

🟢 **Zero across the board, so a wider version-3 discriminator cannot take a legitimate GPL-2.0
payload.** 🔵 **Measured before the edit, not asserted after it.**

🟢 **And `"names no version"` became its own answer, `GPL-UNVERSIONED`** — matching the convention
this KB already had for three other families: `CC-BY…-UNVERSIONED` (`P551`), `EPL-UNVERSIONED`
(`P560`), `MPL-UNVERSIONED` (`P561`). 🔴 **The GNU branch was the last one still guessing.**

🟢 **`P562` honoured: the correction travelled to the consumer.** `GPL-UNVERSIONED` is added to
`OSI_RECONOCIDAS` in `p411-cession-identity-gate/gate_cesion.py`, or that gate would have rejected as
unknown a string its own library had started emitting.

### 🟢 The validation, run rather than claimed

| Control | Result |
|---|---|
| `lib/test_license_family.sh` | 🟢 **152 → 168** assertions, **168/168**, exit 0 |
| **Mutants** on the new branch | 🟢 **6/6 killed** — revert to the bare `'Version 3'` grep (4 assertions fail), drop the numeric arm (3), drop the `GPLv3` arm (1), restore the `GPL-2.0` guess for unversioned (1), break the version-2 read (6), swap the v3 verdict (16) |
| **Regression sweep, all 110 suites in `compose/code/`** | 🟢 run on a **pristine clone of `HEAD`** and on this tree, and the two results are **identical**: **107 pass / 3 fail** before, **108 / 2** after. 🟢 **Zero regressions, zero accidental passes** |
| Fixtures | 🟢 `lib/fixtures-p613/` — 6 real payloads with `PROVENANCE.tsv` (URL, ref, HTTP, bytes, read date) |

🔵 **The one change in the regression diff is `p550` going red → green**, which is `P614` below and
not a side effect of `P613`.

### 🔴 `P614` — `p550` was **red at `HEAD`**, and it was accusing the shared control of a defect it does not have

🔵 **The regression sweep's real purpose was to prove `P613` safe. What it surfaced was that three
suites were already failing at `HEAD` before this pass touched anything.** One of them was lying.

`p550-duplicate-definition-sweep/test_sweep.sh` reported two failures:

```
FAIL live gate: Unlicense allowed  (returned PROHIBITED)
FAIL live gate: NO-CESSION branch present (hardened body is live)  (want=1 got=0)
```

🔴 **Both name `commercial_use_ok` in the shared control. Both are false.** Reproduced by hand with
the library sourced over a **relative** path, same payloads, same run:

```
osi_family_of(UNL)             = [Unlicense]
commercial_use_ok(UNL)         = ALLOWED
declare -f | grep -c NO-CESSION = 1
```

🟢 **The shared control is sound.** 🔴 **Line 144 of the suite was:**

```bash
. /home/user/education-kb/compose/code/lib/license_family.sh
```

🔴 **An absolute path to the repository root on the machine of the pass that wrote it.** In any other
clone the `source` **fails**, `commercial_use_ok` is left **undefined**, and then
`commercial_use_ok "$UNL"` is a *command not found* — non-zero exit, reported as `PROHIBITED` — while
`declare -f … | grep -c` counts **0**. 🔵 Lines 138 and 140 of the *same suite* already used the
relative form.

🔴 **The failure shape is worse than a crash.** A crash is read as broken tooling. This suite **runs,
reports, and names a culprit** — and the culprit it names is the one file every other instrument is
told to reuse. 🔴 **A pass that had acted on it would have "fixed" a correct classifier**, which is
`P597` (pass 49 paying to re-measure settled work) with a sharper edge.

🟢 **Fixed two ways.** The path is relative, and the `source` now **refuses** instead of degrading:

```bash
LIB=../lib/license_family.sh
[ -r "$LIB" ] || { echo "REFUSE: ..." >&2; exit 2; }
. "$LIB"
declare -F commercial_use_ok >/dev/null || { echo "REFUSE: ..." >&2; exit 2; }
```

🟢 **`p550`: 24/26 → 26/26.** 🔵 **The refusal is the part that matters** — `Gap 243`/`Gap 245` made
instruments honest about empty **argv**; this applies the same rule to a failed **source**, so a
missing dependency can never again dress itself as a defect in the thing it failed to load.

### 🟢 `P615` — and the sweep built to catch this class could not see it, by **vocabulary**

🟢 **Swept the whole tree** for hard-coded absolute repository paths in `*.sh` / `*.py` under
`compose/code/`: 🟢 **exactly one occurrence**, the `P614` specimen. 🔵 **A specimen, not yet a class
— and that is the honest reading, as `P352` was.**

🔴 **But `p355-cwd-portability` exists to answer exactly this question and has run for 112 passes
without flagging it.** Its detector was:

```python
EFIMERA = re.compile(r'/tmp/|\$TMPDIR|\bTMPDIR\b|/var/tmp')
```

🔴 **Ephemeral paths only.** An absolute path under `/home/<user>/<repo>-kb/` is the same class — *a
suite that only runs on the machine that wrote it* — and was outside the vocabulary. 🔵 **The
probe-vocabulary failure mode, for the fourth recorded time in this KB.**

🟢 **Extended this pass, and the original vocabulary left byte-identical** so
`resultado.2026-10-05.tsv` stays reproducible:

```python
ABSOLUTA = re.compile(r'^\s*(?:\.|source)\s+/(?:home|Users|root)/'
                      r'|^[^#]*\b(?:\.|source)\s+/(?:home|Users|root)/[^/\s]+/[^/\s]*-kb/')
```

🔴 **And the first version of it flagged the comment that documents the fix.** The `P614` repair
quotes the old path verbatim so a future reader knows what was wrong; a detector that marks that
comment teaches the next pass to **delete the documentation to get the gate green**. 🔵 **`P598` v1
paid for this lesson with 4 false positives of 6, and the lesson travelled this time.** 🟢 A comment
guard (`_es_comentario`) was added before publishing, not after.

🟢 **And the detector is prevented from accusing itself**: its own fixtures are **assembled from
parts** at runtime rather than written as literal paths, so the acceptance test — *"zero occurrences
in the live tree"* — does not match its own test file. 🔴 **The alternative was to exempt the test
file by name, and a by-name exemption is exactly where a real occurrence hides next.**

🟢 **`p355`: 16 → 24 tests, all passing**, including the acceptance test that the live tree is clean
of the class.

## 🟢 Forty-ninth pass, 2026-10-08 — `explosion/spacy-models` read as a licence **channel**, and it answers a question this KB had only asked for Portuguese

⏱️ **Third pass of this date.** Model metadata read first-hand on 2026-10-08 from
`raw.githubusercontent.com`; code licences from the repository **payload**. Existence by
`git ls-remote --heads` against a negative control in the same run (**0 refs**). **No star counts**
(`P479`).

### 🟢 `P595` / `P596` — the per-language licence table, measured across two minor versions

🔵 **Why two versions.** A single version's metadata could carry a typo; the same value at 3.7.0 and
3.8.0 is a **policy**, not an artefact of one release.

| Repo / artefact | Refs | Licence (first-hand) | Source |
|---|---|---|---|
| [`explosion/spaCy`](https://github.com/explosion/spaCy) | 78 | 🟢 **MIT**, **1,128 B**, © 2016-2024 ExplosionAI GmbH / spaCy GmbH / Matthew Honnibal | `master/LICENSE`, HTTP 200 |
| [`explosion/spacy-models`](https://github.com/explosion/spacy-models) | 2 | 🔴 **no licence payload** — `LICENSE`, `LICENSE.md`, `license.txt` all **404** | metadata repo; licences live *per model* in `meta/` |
| `en_core_web_sm` / `en_core_web_lg` | — | 🟢 **MIT** (3.8.0 **and** 3.7.0) | `meta/en_core_web_*-3.8.0.json` |
| `pt_core_news_sm` / `md` / `lg` | — | 🟡 **CC BY-SA 4.0** (3.8.0 **and** 3.7.0) | `meta/pt_core_news_*-3.8.0.json` |
| `es_core_news_sm` | — | 🔴 **GNU GPL 3.0** (3.8.0 **and** 3.7.0) | `meta/es_core_news_sm-3.8.0.json` |
| `xx_ent_wiki_sm` | — | 🟢 **MIT** (3.8.0 **and** 3.7.0) | `meta/xx_ent_wiki_sm-3.8.0.json` |
| [`UniversalDependencies/UD_Portuguese-Bosque`](https://github.com/UniversalDependencies/UD_Portuguese-Bosque) | 5 | 🟡 **CC BY-SA 4.0** | already recorded; re-confirmed as the PT models' `sources[]` entry |
| [`UniversalDependencies/UD_Spanish-AnCora`](https://github.com/UniversalDependencies/UD_Spanish-AnCora) | 4 | 🔴 **GNU GPL 3.0** | 🆕 **README from payload:** *"The GNU license is inherited from the original dataset, downloaded from the AnCora website"* |

🔴 **The repo that holds the models carries no licence of its own**, which is exactly the shape
`P502` warns about: a probe of `LICENSE` returns **404** and an instrument that reads 404 as *"no
grant"* would record the whole model family as ungranted, while a reader who trusts the roundups
would record it as MIT. 🟢 **Both are wrong, and the right answer is one level down, per artefact,
in `meta/`.**

### 🟢 `P599` — `Gap 245` partially closed, and the acceptance test was re-run rather than asserted

`Gap 245` enumerated **23** instruments in `compose/code/` that exit `0` having judged nothing
(`P541`), named the fix, and named the priority order: 🔵 *"`p370-gap-gate` and
`p471-gap-gate-language` first — they are the gates that exist to catch undeclared gaps."*

🟢 **Both are fixed this pass**, with the `p383` guard shape (`if not argv:` → refusal on stderr →
`return 2`) plus a **regression assertion in each suite**, because a usage contract you have to
remember is not a control (`P237`).

| Instrument | `p542` class, pass 44 | `p542` class, **re-run this pass** | Suite |
|---|---|---|---|
| `p370-gap-gate/gap_gate.py` | 🔴 `P541-FALSE-PASS` | 🟢 **`REFUSES`** (exit 2) | 🟢 **27/27** |
| `p471-gap-gate-language/gap_language.py` | 🔴 `P541-FALSE-PASS` | 🟢 **`REFUSES`** (exit 2) | 🟢 **25/25** |
| `p598-register-freshness-gate/freshness_gate.py` 🆕 | — | 🟢 **`REFUSES`** (exit 2) | 🟢 **58/58**, 7/7 mutants |

🟢 **The sweep was re-run, not reasoned about:** `P541-FALSE-PASS` **16 → 14**,
`P541-SILENT-SUCCESS` **7 → 7**, 🟢 **total defects 23 → 21**.

### 🟢 `P608` — incidental re-measurement: the Java/Maven education shelf has not drifted in four days

🔵 **Not planned — produced by the `p542` sweep invoking `p294-pom-in-production`**, which re-ran its
POM licence measurement against live upstream and wrote `result.2026-10-08.tsv` beside the existing
`result.2026-10-04.tsv`. 🟢 **Kept, because it is real measured output and the directory's convention
is dated results side by side.**

🟢 **Diffed rather than assumed.** 7 rows vs 7 rows, and **one byte** of difference in total:

| Repo | Declared in POM | Family | 10-04 → 10-08 |
|---|---|---|---|
| [`kuali/kc`](https://github.com/kuali/kc) | GNU Affero GPL v3 | 🔴 **AGPL-3.0** | 🟢 unchanged |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | Educational Community License v2.0 | 🟡 **ECL-2.0** | 🟢 unchanged |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | Apache Software License v2.0 | 🟢 **Apache-2.0** | 🟢 unchanged |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | *"Apache 2.0 Open Source L6icense"* (upstream's own typo, preserved) | 🟢 **Apache-2.0** | 🟡 POM **84,781 → 84,780 B** |

🟢 **Every licence verdict and every `ACUERDO` is identical**; the only change is one byte in
OpenOLAT's `pom.xml`. 🔵 **Worth one line rather than a section, and worth more than silence:** it
turns "we measured this four days ago" into "this has not moved", which is the claim a client
engagement actually needs.

🔴 **Scope stated honestly: 2 of 23.** The remaining **21** are untouched and are re-declared as
**`Gap 253`** rather than left inside a gap this pass can be read as having closed. 🔵 **And the new
instrument this pass adds classified `REFUSES` on its first sweep** — it did not reproduce the
defect it was built to document.

## 🟢 Forty-eighth pass, 2026-10-08 — upstream `qti3` re-read from a fresh clone: the measurement pass 43 recorded is still exactly current, and the *reason* the writer lacks the mechanism prices the upstream PR

⏱️ **Second pass of this date.** Licence and source read first-hand on 2026-10-08 from a **fresh
shallow clone** of upstream, not from this KB's own prose. Existence by `git ls-remote --heads`
against a negative control in the same run (`P510`). **No star counts** (`P479`).

🔵 **Why re-read something this KB already recorded.** `P582` (`agents/top.md`) found the open-gap
register asserting that nobody had measured the QTI 3 authoring layer, when passes 42 and 43 had.
🔴 **Re-adjudicating that from the KB's own text would be exactly the error `P469` names** — a status
asserted from prose rather than measured. So the upstream payload was read again, independently.

### 🟢 `P584` — upstream has not moved since pass 43, so the measurement is still live

| Measurement | This pass, 2026-10-08 | Pass 43 recorded | Verdict |
|---|---|---|---|
| `refs/heads/main` | `0ca7d6fc451393925ac8f1ba2b1dd2df5117cac5` | `0ca7d6fc` | 🟢 **identical — upstream has not moved in 5 passes** |
| `package.json` version | `0.13.2` | `0.13.2` | 🟢 match |
| `main/LICENSE.md` | **MIT**, © 2026 Longsight, Inc., **1,072 B** | MIT, © 2026 Longsight, Inc., 1,072 B | 🟢 match, byte-for-byte on size |
| `packages/writer/src/index.ts` exports | **33** | 33 | 🟢 match |
| …of which reference the template mechanism | **0** | 0 | 🟢 **match — the asymmetry is real and current** |
| `packages/core/src` files referencing it | **30** (hyphen forms) / **47** (incl. camelCase) | 34 | ⚠️ **pattern-dependent, not a discrepancy** — see note |
| `randomInteger` occurrences in `core/src` | **24** | — | 🟢 new this pass |
| `qti-template-constraint` parsed + enforced | 🟢 `parser-processing.ts:109`, `session.ts:464`, `validation-processing.ts:181` | — | 🟢 new this pass |

⚠️ **The one number that differs is the instrument, not the tree.** This pass counted `30` core files
with the hyphen-only pattern (`qti-template-declaration|qti-template-processing`) and `47` with
camelCase variants included; pass 43 recorded `34`. 🔵 **Three patterns, three counts, same corpus** —
recorded as a pattern sensitivity rather than as a correction to pass 43, because nothing here
establishes which pattern pass 43 used. 🟢 **The figure the gap actually turns on — writer `0` — is
pattern-insensitive and reproduced exactly.**

🟢 **Negative control in the same run:** `git ls-remote` against a non-existent
`LongsightGroup/qti3-does-not-exist-xyz` fails rather than returning refs, so the positive result is
not an artefact of the proxy answering everything.

### 🔴 `P585` — the writer references the mechanism zero times for a **structural** reason, and that changes what the upstream PR costs

🔵 **`Gap 238` described the zero as a missing feature. It is a missing *axis*.** Read end to end,
all 33 exports have the same two shapes:

```
export { buildQti3ChoiceItem,       validateQti3ChoiceItem }       from "./choice.js";
export { buildQti3GapMatchItem,     validateQti3GapMatchItem }     from "./gap-match.js";
export { buildQti3ExtendedTextItem, validateQti3ExtendedTextItem } from "./extended-text.js";
export { buildQti3HotspotItem,      validateQti3HotspotItem }      from "./hotspot.js";
```

🔴 **The writer's entire API surface is indexed by *interaction type*.** The template mechanism is
**orthogonal** to interaction type — `qti-template-declaration` parametrises a choice item, a
gap-match item or an extended-text item alike. 🟢 **So there is no "missing builder" to add next to
the other 33.** `P533`'s contribution is a **second axis** the writer's API shape does not currently
have, and that is why the zero is uniform rather than patchy.

**Why this matters beyond the gap.** It prices the contribution honestly for whoever lands it
upstream:

- 🟢 **Cheap, and genuinely cheap:** emitting the template elements themselves. `P533` did it in one
  pass, stdlib only, 43 assertions / 19 negative controls.
- 🔴 **Not cheap:** threading parametrisation through 33 per-interaction builders **without forking
  the API shape**. That is a design decision for the maintainer, not a patch. 🔵 **Record it as such
  in any proposal** — "we wrote the emitter" is true; "we extended the writer" would not be.

🟢 **The delivery half is confirmed independently and is not in doubt.** `core` parses
`qti-template-constraint` (`parser-processing.ts:109`), enforces it in the session
(`session.ts:464`) and validates it (`validation-processing.ts:181`), with `randomInteger` present
24 times across `core/src`. 🔵 **That corroborates `compose/patterns.md`'s standing claim through a
fresh clone rather than by citation** — the stack can *deliver* parametric variants, and now (via
`P533`) *author* them.

## 🔴 Forty-seventh pass, 2026-10-08 — the foundational shelf's **delivery risk** was mislabelled in both directions, and one row comes back from the dead

⏱️ **First pass of this date.** **Licences read first-hand on 2026-10-08 from payload, classified by
the shared hardened classifier `compose/code/lib/license_family.sh` (`P237`, title-block, `P171`),
commercial use by its `commercial_use_ok()` (`P250`). Existence by `git ls-remote --heads` against a
negative control in the same run (`P510`). **No star counts** (`P479`).

🔵 **No new foundational repo was admitted this pass** — the mandated queries returned curricula,
catalogues and job boards (see `repos/trending.md`). 🟢 **But the licence verdict attached to
foundational rows changed, because the gate that produces those verdicts was wrong on 18 of 29 real
payloads** (`P571`–`P579`, full instrument in `compose/code/p571-cession-family-delegation/`).

### 🟢 `P576` — Sakai is readmitted: `ECL-2.0`, permissive, and it was being refused by name

| | Measured 2026-10-08 |
|---|---|
| Repo | [`github.com/sakaiproject/sakai`](https://github.com/sakaiproject/sakai) |
| Existence (`P510`) | 🟢 **34 refs**; negative control `gmilano/nope-567-control` **0 refs** in the same run |
| Payload | `LICENSE`, **11 119 B** read live from `raw.githubusercontent.com` |
| Family | 🟢 **`ECL-2.0`** — Educational Community License v2.0, **OSI-approved** |
| Gate's old verdict | 🔴 `NO-OSI (community license)` |

🔴 **The cession gate was rejecting it because its licence is *named* "Educational Community
License", and `'community license'` was a NO-OSI trigger put there for `PageLM`.** A substring match
on a licence's own name. 🟢 **ECL-2.0 is Apache-2.0 plus a patent clause**, so it carries **no
reciprocal obligation** — a studio can build on Sakai and ship the result closed, which is the
opposite of what the shelf was recording.

🔵 **This is the most consequential row of the pass**, because Sakai is one of very few genuinely
permissive full LMS platforms. Moodle (`GPL-3.0`) and Open edX (`AGPL-3.0`) both impose reciprocity;
ECL-2.0 does not.

### 🟡 `P571` / `P572` — Moodle is `GPL-3.0`, not `AGPL-3.0`, and OpenEMIS is `GPL-2.0`, not `LGPL`

| Repo | Existence | Payload | Gate said | Is |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **40 refs** | `COPYING.txt`, **35 146 B** | 🔴 `AGPL-3.0` | 🟡 **`GPL-3.0`** |
| [`OpenEMIS/core`](https://github.com/OpenEMIS/core) | 🟢 **1 ref** | `LICENSE` | 🔴 `LGPL` | 🟡 **`GPL-2.0`** |

🔵 **The GPL-3.0 / AGPL-3.0 distinction is not cosmetic for a hosted engagement — it is the whole
question.** AGPL-3.0 §13 extends reciprocity to users who interact with the software **over a
network**, so a SaaS delivery of an AGPL component must offer its source. GPL-3.0 does not. 🔴 **A
shelf that labels Moodle `AGPL-3.0` tells a studio it cannot host a closed Moodle derivative, which
is false.** The cause is `P171`: **GPL-3.0 §13 is titled *"Use with the GNU Affero General Public
License"***, so a probe over the licence **body** finds the word *affero* in every GPL-3.0 text.

🔴 **`P572` is the same mistake in a second place:** GPL-2.0's closing paragraph recommends *"use the
GNU Lesser General Public License instead of this License"*, and the inlined ladder tested
`gnu lesser` **before** `gnu general public`.

### 🟡 `P573` / `P574` / `P575` — MPL and EPL were being read as GNU copyleft

MPL-2.0 §1.12 and EPL-2.0's *Secondary Licenses* clause **define their GPL compatibility by naming
GPL, LGPL and AGPL**, so every MPL-2.0 and EPL-2.0 payload carries the GNU marks. The inlined ladder
tested the GNU branches first:

| Payload | Gate said | Is |
|---|---|---|
| [`mozilla/rhino`](https://github.com/mozilla/rhino) | 🔴 `AGPL-3.0` | 🟡 **`MPL-2.0`** |
| [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) | 🔴 `GPL` | 🟡 **`EPL-2.0`** |
| [`eclipse-ee4j/jersey`](https://github.com/eclipse-ee4j/jersey) | 🔴 `GPL` | 🟡 **`EPL-2.0`** |
| canonical **MPL-1.1** (SPDX) | 🔴 `MPL-2.0` | 🟡 **`MPL-1.1`** |

🔵 **`lib/` already knew all of this** — it is `P454`, and its header says *MPL and EPL go before the
GNU family*. 🔴 **The gate inherited none of it, because it wrote its own ladder.** That is the exact
failure `lib/README.md` was created to prevent: *«a rule you have to remember is not a control»*.

🟢 **Fixed by delegation**, not by patching the ladder. 🔵 **And the delegation could not be blind:
the shared classifier reads `PageLM` as `MIT`**, the very payload the gate exists to refuse — so the
family question is delegated and the cession question is kept. If the shared classifier is missing,
`familia_compartida()` **raises** rather than falling back to an inlined ladder (`P197`).

🟡 **Open:** `Gap 249` — `h2database` offers **MPL-2.0 or EPL-1.0** and the answer is still only the
MPL arm (`P578`). 🟡 **`Gap 250`** 🆕 — `p419-copyleft-identity` inlines a **third** classifier.

## 🔴 Forty-sixth pass, 2026-10-07 — the licence **version** of a foundational repo was being invented, and two consumers were asking for a string the classifier could not produce

⏱️ **Thirteenth pass of this date.** **Licences read first-hand on 2026-10-07 from payload, classified
by the shared hardened classifier `compose/code/lib/license_family.sh` (`P237`, title-block, `P171`),
commercial use by its `commercial_use_ok()` (`P250`). Existence by `git ls-remote --heads` against a
negative control in the same run (`P510`). **No star counts** (`P479`).

🔵 **Both findings this pass are in the instrument, not the shelf, and both were found by RUNNING it
on new input rather than by reading it.** 🟢 **Both are fixed, with regression tests and five
mutants, and the shelf's published verdicts survive unchanged** — 🔵 **because this base holds no
EPL or MPL-1.1 foundational repo today.** 🔴 **That is luck, not design, and it is exactly what made
the defect invisible for forty-five passes.**

### 🔴 `P561` — the MPL branch **stamped** `-2.0` on every Mozilla payload

The shared control's header says *"source this, do not rewrite it"*: every licence verdict this KB
publishes is classified by it. 🔴 **Its MPL branch read the family and invented the version:**

```sh
printf '%s' "$t" | grep -qi 'Mozilla Public License' && { echo "MPL-2.0"; return; }
```

🟢 **Falsified first-hand against the canonical MPL-1.1 text** (SPDX `license-list-data`,
**23 668 B**, title block *"Mozilla Public License Version 1.1"*): it answered 🔴 **`MPL-2.0`**.
🔵 **This is `P551` verbatim — the defect pass 45 measured and fixed for the CC branch — sitting one
line above its own fix.** 🟢 **Fixed: `MPL-2.0` / `MPL-1.1` / `MPL-1.0` are read, and a Mozilla
payload that states no version answers `MPL-UNVERSIONED` rather than being guessed into 2.0**
(`P502`'s lesson: *"declares no version"* and *"declares 2.0"* are different answers).

🔵 **Negative control held:** `mozilla/rhino`'s real MPL-2.0 payload (**16 779 B**, and a *partial*
grant — it opens *"The majority of Rhino is licensed under the MPL 2.0"*) still answers `MPL-2.0`.

### 🔴 `P560` — the EPL branch **collapsed** two licences into one answer

```sh
printf '%s' "$t" | grep -qi 'Eclipse Public License' && { echo "EPL"; return; }
```

🔴 **Four real payloads, two versions, one answer.** Measured: `junit-team/junit4` (**EPL-1.0**,
11 374 B), `hcengineering/platform` (**EPL-2.0**, 14 196 B), `eclipse-ee4j/jersey` (**EPL-2.0**,
35 081 B), `eclipse/paho.mqtt.java` (**EPL-2.0**, 519 B) — 🔴 **all four `EPL`**.

🔵 **Why it matters here and not only in prose:** this file's own recommendations run on top of
copyleft education ERPs (`openeducat` LGPL-3.0, `frappe/education` + ERPNext GPL-3.0), so
GPL-combinability is a standing question — and **EPL-1.0 is GPL-incompatible while EPL-2.0 may be
GPL-compatible** via its *Secondary Licenses* clause, at the steward's designation. 🔴 **`EPL`
answers neither.** 🟢 **Fixed: `EPL-2.0` / `EPL-1.0` are read, `EPL-UNVERSIONED` when the payload
states no version.**

### 🔴 `P562` — the repair had to travel to the **consumers**, and there it had been waiting

🟢 **The pass's sharpest measurement, and it was not visible from the library at all.** Two
instruments test membership against literal family strings:

| Consumer | Set | 🔴 Before |
|---|---|---|
| `p429-cession-claim-audit/audit_claim.py` | `COPYLEFT` named **`EPL-2.0`** | 🔴 a string `family_of` **could not emit**; the real output `EPL` fell through to **`NO_CLASIFICADA`** |
| `p444-root-vs-tree-family/root_vs_tree.py` | `COPYLEFT` named `EPL-2.0`, `MPL-2.0`, `EUPL-1.2` | 🔴 same, and `EUPL-1.1` was never named although the EUPL branch resolves it |

🔴 **So the delivery-risk audit could not classify an EPL component as copyleft at any point in this
base's history.** It reported *"unclassified"* — the string reserved for *no verdict* — on a licence
family whose regime is well settled. 🟢 **Both sets repaired**, with the `*-UNVERSIONED` answers
placed in `COPYLEFT` deliberately: EPL and MPL are distribution copyleft in **every** version, so
*"it is some EPL"* already answers the delivery question, and leaving it in `NO_CLASIFICADA` would
report ignorance about something known.

🔵 **Third occurrence of the `P197`/`P237` thesis: a correction in a shared control is not a
correction until the consumer inherits it.** 🟢 **Pinned by 6 new cases in `p429`'s suite**, including
the negative control that a version discrepancy *within* one class (`EPL-2.0` claimed vs `EPL-1.0`
measured) stays **COSMETICA** and is not inflated to blocking.

### 🟢 What the suites say

| Suite | Before | 🟢 After |
|---|---|---|
| `lib/test_license_family.sh` | 141/141 | 🟢 **152/152** (11 new, incl. 4 negative controls) |
| `p560-epl-mpl-version-read/test_versions.sh` 🆕 | — | 🟢 **22/22**, **5 mutants** |
| `p429-cession-claim-audit/test_audit.py` | 12/12 | 🟢 **18/18** |
| `p444-root-vs-tree-family/test_root_vs_tree.py` | 24 OK | 🟢 **24 OK** |
| whole tree | — | 🟢 **106 suites pass** |

🔴 **Two red, neither caused by this pass, both verified red at pristine `HEAD` (`5dc22ad`) in a
separate worktree before anything was claimed:** `p351-star-digit-sweep` (5 failures — historical
`★` rows inside the append-only trending history, i.e. `P479`'s own accumulated debt, and a real
open item) and `p213-envelope-aad` (the environment's `cryptography` wheel panics on import:
`pyo3_runtime.PanicException` — 🔵 **an environment fault**). 🔵 **Neither instrument reads the shared
classifier, so neither could have been affected.**

### 🟡 The inlined classifier that still carries `P561`

🔴 **`p411-cession-identity-gate/gate_cesion.py` classifies licences INLINE** — `elif 'mozilla
public' in bajo: v['familia'] = 'MPL-2.0'` — which is both the `P237` violation the `lib/` README
forbids in writing (*"no se inlinea un clasificador de licencias"*) and 🔴 **a second live copy of
`P561`**: it stamps `2.0` on any Mozilla payload. 🟡 **NOT fixed this pass, and declared rather than
left silent:** rewriting `p411` onto the shared control changes what that gate reports and needs its
own pass and its own suite. 🔵 **Registered here so the next pass inherits it instead of
rediscovering it.**

### 🔴 The mandated foundational query, again

🔵 **`open source platform education ERP CRM MIT Apache` ran verbatim and returned, for the
twenty-seventh time, the generalist axis** — ERPNext/Frappe, Odoo, Apache OFBiz, Huly, AureusERP,
plus Dolibarr, Compiere and Krayin. 🔴 **Zero new education-native foundational repos.** 🟢 **What it
did yield is two licence corrections on that generalist axis** (`P563` Huly is EPL-2.0 not
Apache-2.0; `P564` Krayin and AureusERP ship one vendor's identical MIT file) — both in
`verticals/solutions.md`, which is where platforms live.

## 🔴 Forty-fifth pass, 2026-10-07 — the **shared control** carried two answers to its own question, and a second defect stamped a licence version it never read

⏱️ **Twelfth pass of this date.** **Licences read first-hand on 2026-10-07 from payload, classified
by the shared hardened classifier `compose/code/lib/license_family.sh` (`P237`, title-block, `P171`),
commercial use by its `commercial_use_ok()` (`P250`). Existence by `git ls-remote --heads` against a
negative control in the same run (`P510`). **No star counts** (`P479`).

🔵 **Both findings this pass are in the instrument, not the shelf, and both were found by RUNNING it
on new input rather than by reading it.** 🟢 **Both are fixed, with regression tests, and the shelf's
published verdicts survive unchanged.**

### 🔴 `P550` — `lib/license_family.sh` defined `commercial_use_ok()` **twice**, and the live gate was correct **only by source order**

The file's own header says *"source this, do not rewrite it"*: every licence verdict this KB
publishes is classified by it. It contained **two** definitions of the same function — the pass-82
**first cut** (a pure token-match over the payload body, **no family gate**) at line 429, and the
hardened `P299`/`P312` body at line 455.

🔵 **Bash keeps the LAST definition**, so the body that actually ran was the hardened one and **no
published verdict was ever wrong**. 🔴 **But it was correct by order of reading, and order of reading
is not a control.** The most uncomfortable detail: the comment block that explains *why the first cut
was wrong* sits **between the two definitions**. The fix was **appended, not substituted**.

🟢 **The hazard is measured, not hypothetical** — `p550-duplicate-definition-sweep/oracle_inversion.sh`
binds the shadowed body under a second name and runs both over **this KB's own 27 licence payloads**:

| | Result |
|---|---|
| Payloads judged | **27** (every `LICENSE`/`COPYING` payload in `compose/code/`) |
| 🔴 **Verdicts that invert if the order flips** | **7** |
| Direction of all 7 | 🟡 `ALLOWED` → `PROHIBITED` — **uniform** |
| `CC-BY-NC-4.0` control | 🟢 `PROHIBITED` under **both** bodies — the NC case does not move |

🔴 **The seven, named:** `openemis-core` (GPL-2.0), `kuali/kfs` (AGPL-3.0), `Ovsyanka83/autograder`
(GPL-3.0), `INGInious` (AGPL-3.0), `FWU-DE/mem-mcp` (**Unlicense**), `classroomio` (AGPL-3.0),
`lmscloud` (GPL-3.0). 🔵 **Moodle's GPL-3.0 payload and the Unlicense — the most permissive text that
exists — are both in the blast radius.**

🟢 **The direction BOUNDS the damage and is worth stating precisely.** All seven inversions
over-restrict: this is `P308`'s direction (*lose shelf, cost an opportunity*), **not** `P312`'s
(*invent permission, cost the deliverable*). 🔵 **That makes it expensive, not catastrophic** — and it
is the reason the fix is a cleanup rather than a recall of published rows.

🔵 **Dated, not guessed.** The duplicate is also present in the frozen
`p308-phrase-anchor-sweep/license_family.PRE-P308-CONTROL-2026-10-04.sh` snapshot, so it predates
**2026-10-04** and survived every `132/132` run since.

### 🟢 The instrument, and the two defects it found **in itself**

`compose/code/p550-duplicate-definition-sweep/` — **302 files** scanned, suite **26/26**, 4 mutants,
`REFUSES` empty input with exit `2` (`P542`'s lesson applied before publishing, not after).

| Class | n (pre-fix) | Reading |
|---|---|---|
| 🔴 `P550-SHADOWED-DIVERGENT` | **1** | 🔴 the shared control itself |
| `P550-FROZEN-CONTROL` | 1 | 🔵 the PRE-P308 snapshot — **declared, not accused**: reproducing old behaviour is its job |
| `P550-REDUNDANT-IDENTICAL` | 0 | 🟢 a byte-identical re-declaration is redundant, not dangerous — the sweep says so rather than padding its count |
| **after the fix** | **0** | 🟢 `sweep_dupdefs.sh` exits `0`; the oracle answers `SHADOW-ABSENT` |

🔴 **`P550b` — the sweep's first cut kept a private counter beside its published table.** Two mutants
walked straight through the suite (drop the increment; force the final test true) because both leave
the **rows correct** and only the **exit status** lies. 🔵 **That is `P541`'s shape reproduced inside
the instrument written to find `P541`'s cousin.** 🟢 **Fixed by construction:** the status is now
recomputed **from the emitted rows**, so there is no second number that can drift, and the suite
asserts on the **table** — the exit code is a convenience, the table is the evidence.

🔴 **`P550c` — the first cut reported three definitions that do not exist.** `f`, `g` and `k`: all of
them **fixture source quoted inside heredocs in the sweep's own suite**. A scanner that cannot tell a
definition from a string containing one **over-accuses**, which is `P543`'s error class. 🟢 **Fixed
with a heredoc-aware / triple-quote-aware pre-filter (`strip_quoted.awk`), and tested in BOTH
directions** — a quoted definition must not be reported, and a real duplicate *after* a heredoc must
still be.

### 🔴 `P551` — the CC branch **read the attributes and stamped the version**

The same control assembled `NC`/`SA`/`ND` by reading the payload and then concatenated **`-4.0`
literal**, so *every* Creative Commons text came back as 4.0 whatever its real version.

🟢 **Found on a real asset that `Gap 246` forces this KB to look at.**
`UniversalDependencies/UD_Portuguese-PUD` ships a `LICENSE.txt` of **19 556 B** whose title block
reads *"Creative Commons Attribution-ShareAlike **3.0** International Public License"*, with two
`by-sa/3.0` URLs and **zero** occurrences of "4.0" — and the classifier answered `CC-BY-SA-4.0`.

🔴 **Why it is the dangerous direction, and for a treebank specifically.** CC **4.0** covers *sui
generis* **database rights** explicitly (Art. 4) and adds a 30-day cure period; **3.0** does neither.
🔵 **A treebank IS a database.** Labelling 3.0 as 4.0 does not lose shelf — it **invents a grant the
text does not give**, which is `P312`'s direction.

🟢 **Fixed by reading the version in three channels**, and by refusing to guess: the canonical
`creativecommons.org/licenses/<codes>/<version>` URL, the version behind an attribute **name** in the
title, and the **acronym** form a README uses (`CC BY-SA 3.0`). 🔵 **The third channel was not
optional** — `P312` entered the CC branch by the acronym, and without it `P312`'s own fixture
regressed, which the suite caught on the first run. 🔴 **And "no version declared" now answers
`CC-BY-SA-UNVERSIONED`, never 4.0** — `P502`'s lesson: two different facts must not share a string.

🟢 **Suite: `141/141`** (9 new cases, 3 of them **real payloads** committed as fixtures, 5 of them
**negative controls** that pin the versions and attributes the fix must NOT move).

🔴 **A third defect, in the suite's own input channel, and it is the same shape again.** The first
cut of those fixture tests resolved their path from `${BASH_SOURCE[0]}`, which is **empty** at that
point in this suite — `dirname ""` left the path at `/fixtures-p551`, `cat` failed, and all four
cases returned **`UNCLASSIFIED`**. 🔵 **An absent fixture disguised itself as a verdict**: that is
`P502` on the suite's input channel, and a reader who saw `UNCLASSIFIED` would have concluded
something about the licence rather than about the path.

### 🟢 The foundational shelf is unchanged, and that is the finding

🔵 **Nothing is withdrawn.** The live gate was the hardened one throughout, `p312`'s NC-gate suite
(`21/21`), `p288` (`9/9`), `p255` (`13/13`) and `p308` (`100` pass / `0` fail) all re-run green after
both repairs. 🟢 **Every suite that sources the shared control was re-run, not assumed** — which is
the only reason this pass can say the shelf stands.

## 🟢 Forty-fourth pass, 2026-10-07 — `Gap 243` **CLOSED with code**, and the sweep found two defects **in itself** that reading it could not

⏱️ **Eleventh pass of this date.** **Licences read first-hand on 2026-10-07 from payload in cloned
trees via the shared hardened classifier `compose/code/lib/license_family.sh` (`P237`, title-block,
`P171`), commercial use via its `commercial_use_ok()` (`P250`). Existence by `git ls-remote --heads`
against a negative control in the same run (`P510`). **No star counts** (`P479`).

### 🟢 `P542` — `Gap 243` closed: `compose/code/p542-empty-input-sweep/`

`Gap 243` was declared *"mechanically closable"* and *"the one that would tell this KB how much of
its own evidence is real"*, with the remedy in one line: *"one pass, one loop — invoke every
argument-taking instrument with no arguments and assert a non-zero exit."* 🟢 **That loop now
exists, ran over the whole tree, and publishes its result** (`result.2026-10-07.tsv`).

| Class | n | Reading |
|---|---|---|
| `REFUSES` | 43 | 🟢 exits non-zero — correct, does not fake success |
| `P542-STDIN-FILTER` | 35 | 🔵 filter given EOF — correct, not judgeable by this harness |
| `P542-NOT-A-GATE` | 31 | 🔵 library module, no entry point — invoking it is a no-op by design |
| `P542-UNADJUDICATED-OUTPUT` | 31 | 🟡 shell that emitted something — **declared, not absolved** |
| 🔴 **`P541-FALSE-PASS`** | **16** | 🔴 exit `0` having opened **zero** judged files — **proved**, not inferred |
| `MEASURES` | 15 | 🟢 exit `0` and read real input (self-discovering, the `p355` shape) |
| 🔴 **`P541-SILENT-SUCCESS`** | **7** | 🔴 exit `0` with zero bytes on **both** streams |
| `P542-UNADJUDICATED-TIMEOUT` | 9 | 🟡 did not finish in 12 s — nothing asserted either way |
| **total** | **187** | 🔴 **23 confirmed `P541`-class defects** |

🔴 **The two most uncomfortable rows are this KB's own gap gates.** `p370-gap-gate/gap_gate.py` and
`p471-gap-gate-language/gap_language.py` each **print their own header and exit `0`** when invoked
with no arguments. 🔵 **The instruments that exist to catch undeclared gaps cannot themselves tell an
empty invocation from a clean tree.** 🟢 **Suite: 42/42, offline, 7 mutants killed.** 🟢 **The sweep
does not have the defect it detects** — `sweep_empty_input.py` and `readcount.py` both refuse empty
input with exit `2`, and the suite asserts both.

### 🔴 `P543` — the gap's one-line remedy **over-accuses**, and only running it showed that

🔵 **This is the finding, not a caveat.** The prescribed loop ("assert a non-zero exit") is wrong for
three shapes that exit `0` on empty input **correctly**, and a sweep that cannot separate them commits
the error class of `P502` — an instrument that could not tell *"no licence file"* from *"no
repository"*.

| Shape | Why exit `0` is correct | How it was found | Cost of missing it |
|---|---|---|---|
| **self-discovering gate** | resolves its corpus from `__file__`, not `argv` — the `p355` lesson; `p243` measures **146** files this way | known before the run | would have accused a correct gate |
| **library module** (no `__main__`) | its suite *imports* it; direct invocation is a no-op **by design** | 🔴 **the run** — **24 of the first 49** accusations | 49 → 25 |
| **stdin filter** (`sys.stdin`, `while read`) | given EOF it correctly does nothing, like `cat < /dev/null` | 🔴 **hand-checking ONE accusation** before publishing 34 | 34 → 23 |

🔴 **The first published number would have been 49 and the true number is 23.** 🟢 **Both
self-inflicted defects are now mutants in the suite** (`ignora_invocable`, `ignora_filtro`), so the
regression is covered rather than merely corrected — the `P480` lesson, where a new instrument
inherited the shared classifier's code but not its regression coverage.

### 🔵 The two oracles, and the one that is weaker — stated rather than blurred

| | Oracle | Applies to | Strength |
|---|---|---|---|
| **A** | `sys.addaudithook` counts the **non-code files under the repo the instrument opens**; `0` with exit `0` is the defect | `.py` | 🟢 **direct** — measures the read itself |
| **B** | **silence**: exit `0` with zero bytes on stdout **and** stderr | `.sh` | 🟡 **indirect** — a weaker claim, marked as such in every row |

🔴 **Why not a tracer.** `strace` is installed and works, but wrapping the cloned tree's code in a
tracer is **not permitted in this environment**. 🟢 **The audit hook is pure Python, runs inside the
instrument's own process, and measures the `open` rather than a proxy for it.** 🔴 **Oracle A does
not reach shell**, so a `.sh` run that exits `0` after printing 13 777 bytes is **not accused** — it
becomes `UNADJUDICATED-OUTPUT`. 🔵 **The sweep prefers to under-accuse**; every boundary resolves in
the instrument's favour. → **`Gap 244`**.

### 🟢 `P545` — counter-evidence the sweep produced by accident, and it is evidence **for** this KB

The sweep re-ran `p294-pom-in-production/sweep_pom_production.sh` with no arguments, which
**self-discovers a slug list and fetches live** — so it regenerated a dated result beside pass 39's
`result.2026-10-04.tsv`. 🟢 **The two files differ by exactly one byte**, in one field:

```
-OpenOLAT/OpenOLAT	84781	org.openolat	OWN	True	Apache 2.0 Open Source L6icense ...
+OpenOLAT/OpenOLAT	84780	org.openolat	OWN	True	Apache 2.0 Open Source L6icense ...
```

🔵 **The field that moved is `pom_bytes` — the fetched `pom.xml`'s size, an upstream property, not
instrument state.** Every licence verdict in all nine rows is unchanged. 🟢 **So the honest reading
of `Gap 243`'s closure is: 23 of 187 gates cannot tell empty from clean — NOT "this KB's evidence is
fake."** 🔵 **The instruments that measure, reproduce.** 🔵 **(Aside, recorded because it is in
upstream and not a transcription error: OpenOLAT's own `pom.xml` declares `Apache 2.0 Open Source
L6icense`.)** 🟢 **The regenerated artefact was removed; pass 39's remains the record.**

### 🟢 `P544` — the Portuguese feature tier, shelved here with licences read from payload

The five assets measured this pass are in `agents/top.md` `P544` with their channels and byte counts.
🔵 **Summary for this file's purpose — what a studio may build on:**

| Layer | Asset | Licence | Usable by Globant? |
|---|---|---|---|
| NLP pipeline | `explosion/spaCy` | 🟢 **MIT** | 🟢 yes |
| PT feature extractor | `nilc-nlp/nilcmetrix` (172 files) | 🟡 **AGPL-3.0** | 🔴 not as a hosted service without releasing the service |
| PT feature extractor (older) | `nilc-nlp/coh-metrix-port` | 🟡 **GPL-3.0** | 🟡 only if the deliverable is GPL |
| EN reference tool | `kristopherkyle/TAALED` | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no — NonCommercial** |

🔴 **This inverts the tier's assumed topology the way `P493` inverted the comparability tier's**: the
*intelligence* is available and the *licence* is the blocker, which is `P516`'s shape again. 🟢 **The
index definitions are publishable statistics and free to reimplement** — that is the path, and it is
reimplementation, not porting. → **`Gap 246`**.

## 🟢 Forty-third pass, 2026-10-07 — `Gap 238` **CLOSED with code**: the authoring half of QTI 3 parametric items now exists, and the build found three defects reading could not

⏱️ **Tenth pass of this date** (34–42 ran earlier). **Licences read first-hand on 2026-10-07 via the
shared hardened classifier `compose/code/lib/license_family.sh` (`P237`, title-block, `P171`) over the
**cloned working tree**. Existence by `git ls-remote --heads` against a negative control in the same run
(`P510`). **No star counts** (`P479`).

🟢 **Pass 42 declared `Gap 238` "the cheapest gap on this KB… the one a single pass could close
outright". This pass took it at its word and closed it — with a tested artefact, not a prescription.**

### 🟢 `P533` — `Gap 238` closed: `compose/code/p533-qti3-template-emitter/`

🔵 **The gap, reproduced before anything was built.** Pass 42's `P527` measured that
[`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) can **deliver** parametric item
variants and cannot **author** them. Re-measured this pass at HEAD `0ca7d6fc` (2026-10-07):

| Measurement | Value | Method |
|---|---|---|
| `packages/writer/src/index.ts` exports | **33** | `grep -c "^export"` |
| …referencing `qti-template-declaration` / `qti-template-processing` | 🔴 **0** | `grep -rl` over `packages/writer/src` |
| `packages/core/src` files referencing the same | 🟢 **34** | `grep -rl` over `packages/core/src` |
| Licence | 🟢 **MIT**, © 2026 Longsight, Inc. | `LICENSE.md` payload via shared classifier |
| Version | `0.13.2` | `package.json` |

🟢 **`P527` reproduces exactly.** The asymmetry is the gap: the runtime implements the whole
mechanism and the authoring package implements none of it.

**What was built:** `emit_template.py` — `qti-template-declaration`, `qti-template-processing`,
`qti-set-template-value`, `qti-set-correct-response`, `qti-template-constraint`,
`qti-random-integer`/`-float`, `qti-variable`, `qti-base-value` and n-ary operators, plus whole-item
assembly. Stdlib only, per `P237`'s shape: an instrument that needs a dependency to run is an
instrument that does not run.

**The grammar targets core's parser, not the specification prose**, so the contract is the one the
runtime enforces: `parser.ts:139-148`, `parser-processing.ts:47/73/109/258`,
`operator-attribute.ts:24`, `processing-evaluator.ts:163-172`, `session.ts:449-476`,
`validation-random-expression.ts`.

### 🔴 Why the oracle is **transitive**, stated rather than quietly substituted

`Gap 238` named core's parser plus the fixture as the oracle. **Two stronger instruments were tried
first and both are unavailable here:**

| Instrument | Outcome |
|---|---|
| Execute `qti3`'s own suite | 🔴 **Not permitted** — installing a third-party repository's dependencies is out of scope in this environment. Same limit `P527` recorded; `Gap 238` already carries it as a prerequisite |
| Validate against the official QTI 3.0.1 ASI schema | 🔴 **Blocked.** `qti3` pins it by sha256 in `packages/conformance/schemas/qti3/sources.json`, but the schema is **fetched, not vendored**, and `purl.imsglobal.org:443` is refused by this environment's egress proxy (`connect_rejected`, organization policy). 🔵 **Same class as `Gap 56`** (eur-lex) **and `Gap 92`** (docs.moodle.org) |

🟢 **So the oracle is transitivity through documents the upstream gate has already validated.**
`scripts/check-test-xsd.mjs` runs `xmllint --nonet --noout --schema <pinned official ASI xsd>` over
`packages/fixtures/xml/*.xml` and reports *"official ASI schema validation passed"*. A fixture is
therefore a **known schema-valid QTI 3 document**; regenerating one **node-for-node** makes the
emitter's output schema-valid by transitivity without reaching the schema.

🔵 **Two independent fixtures, not one**, so a hand-tuned success cannot pass as a general result —
and each fixture's comparison is controlled against the other's document.

**Result: `43` assertions, `0` failures, `19` of them negative controls.** Reproduce with
`python3 -I test_emit_template.py`.

### 🟢 `P536` — the three defects the build found that reading the repo could not

🔵 **Each is a property of the delivery runtime that an author cannot see in the XML they write.**

| | Defect | Consequence |
|---|---|---|
| **1** | 🔴 **`max` is frequently unattainable.** The draw is over a **grid**: `count = floor((max-min)/step)+1`, `draw = min + floor(random()*count)*step`. When `step` does not divide `max-min`, `max` **never occurs** — `min=1 max=10 step=4` draws from `{1,5,9}` | An author reading `max="10"` as "the largest value a student can see" **authors a different item from the one delivered** |
| **2** | 🔴 **An infeasible `qti-template-constraint` degrades silently into a wrong item.** `session.ts:449-476` restarts at most **100** times and then **proceeds with the violating draw** rather than raising | At acceptance probability `p`, exhaustion has probability `(1-p)**101` — ~0.5% at `p=0.05`, **~90% at `p=0.001`**. 🟢 `estimate_constraint_restarts` computes acceptance exactly over the declared grids, so it is checkable before publication |
| **3** | 🔴 **Parser order and schema order are different orders.** `core` finds children by name and accepts any order; the XSD declares a sequence | 🔴 **An emitter written against the parser produces documents that deliver correctly and fail validation** — the worst available failure mode, because the authoring tool's own test passes |

🔵 **Defect 3 is the one worth generalising**: this KB has repeatedly found that *reading the consumer*
is not the same as *satisfying the contract*. The consumer was more permissive than the schema, so
conformance to the consumer was not conformance.

### 🟡 What `P533` does **not** close, stated rather than implied

- 🔴 **The TypeScript is not executed.** `writer-contribution.ts` carries the same emitter in the host
  project's idiom so the upstream diff is a review rather than a translation, and it is
  **parse-checked only** (`node --experimental-strip-types --check`, imports stripped). 🔴 **That
  proves syntax, not types and not behaviour.** The Python module is the tested artefact.
- 🔴 **Nothing has been contributed upstream.** This KB produced the patch; opening a pull request
  against `LongsightGroup/qti3` is not something a KB pass should do unprompted. → **`Gap 240`**.
- 🟡 **`qti3` is `0.13.2`** — pre-1.0, and its HEAD moved on the same day it was read. The emitter
  targets a grammar that can still change.

## 🟢 Forty-second pass, 2026-10-07 — `Gap 235` closes on the **corpus**, not the scorer; and `Gap 39`'s first half is finally **tested** — the writer cannot emit what the runtime can execute

⏱️ **Ninth pass of this date** (34–41 ran earlier). **Licences read first-hand on 2026-10-07** from the
channel named per row — repository **payload** on `raw.githubusercontent.com` (title-block classified,
`P171`), **registry** metadata, and this pass additionally **the cloned working tree**. Existence by
`git ls-remote --heads` against a negative control in the same run (`P510`). **No star counts** (`P479`).

### 🟢 `P524` — the permissive asset in the essay-scoring tier is the **corpus**: `essay-br`, MIT, human-graded, peer-reviewed

🔵 **Why this is the shape of the answer rather than a consolation prize.** `P516` measured the
essay-scoring tier and found *permissive code over non-permissive intelligence*. 🟢 **This pass found the
one thing that inverts that, and it is not a scorer — it is the graded data a client needs in order to
own a scorer.**

| Field | Value, and the channel it came from |
|---|---|
| Repo | [`lplnufpi/essay-br`](https://github.com/lplnufpi/essay-br) — 🟢 **existence confirmed**, `git ls-remote --heads` serves exactly one ref, `refs/heads/main` (`P510`, `P511`) |
| Licence | 🟢 **MIT** — payload `main/LICENSE`, **1,114 B**, title block `MIT License`, holder *"Copyright (c) 2021 Laboratório de Processamento de Linguagem Natural - UFPI"* |
| Holder | **Laboratório de Processamento de Linguagem Natural, Universidade Federal do Piauí (UFPI)** — 🟢 **LATAM-origin, and a federal university lab rather than a vendor** |
| What it is | **Extended Essay-BR** — essays written by **Brazilian high-school students**, *"graded by humans professionals following the criteria of the ENEM exam"* (README, read from payload) |
| Grading scheme | 🟢 **The ENEM five-competency rubric (C1–C5)**, the instrument a Brazilian client actually reports against |
| Provenance | 🟢 **Peer-reviewed** — Marinho, Anchiêta & Moura, *"Essay-BR: a Brazilian Corpus to Automatic Essay Scoring Task"*, **Journal of Information and Data Management 13(1), 65–76 (2022)**, Sociedade Brasileira de Computação, [`doi:10.5753/jidm.2022.2340`](https://doi.org/10.5753/jidm.2022.2340) |
| Access surface | `build_dataset.py` exposing a `Corpus` class; Python ≥ 3.6 |

> **`P524`.** 🟢 **The first LATAM-origin permissive asset this KB has recorded in the essay-scoring
> tier, and it is MIT, human-graded against the national rubric, and citable.** 🔵 **It changes what
> `P516` means in practice: `P516`'s question was *where does the judgement live, and can the client keep
> it?* — and a graded corpus under MIT is precisely the artefact that lets the answer be "yes", because
> it is what you fine-tune and calibrate **your own** scorer against.** 🔴 **What it is not: a scorer.
> See `Gap 236`.**

### 🔴 `P525` — the LanguageTool path is **two licences deep**, the registry declares neither, and the Python wrapper is the restrictive one

🔵 **Why this row exists.** The one open component that measurably improves Portuguese essay scoring in
the pipeline `P526` reads is **LanguageTool**, used for competency C1 (formal register). 🔴 **Its licence
is not one fact, it is three, and they disagree in the direction that matters.**

| Layer | Artefact | Licence, and the channel | 🔴 Consequence |
|---|---|---|---|
| **Engine** | [`languagetool-org/languagetool`](https://github.com/languagetool-org/languagetool) | 🟡 **LGPL-2.1** — **two agreeing channels**: payload `master/COPYING.txt` **26,432 B**, title block *"GNU LESSER GENERAL PUBLIC LICENSE Version 2.1, February 1999"*; and `master/pom.xml` `<licenses>` → *"GNU Lesser General Public License"* | 🟢 **Library copyleft.** Usable as a **separate process or service** without reaching the caller |
| **Python wrapper** | [`jxmorris12/language_tool_python`](https://github.com/jxmorris12/language_tool_python) — the import the pipeline actually writes | 🔴 **GPL-3.0** — payload `master/LICENSE`, **35,151 B**, title block *"GNU GENERAL PUBLIC LICENSE"* | 🔴 **Full copyleft, and it is the layer a developer touches first** |
| **Registry** | `language-tool-python` **3.4.0** on PyPI | 🔴 **SILENT** — JSON API returns `info.license = None` **and an empty classifier list** | 🔴 **A registry-only sweep records this dependency as unlicensed-unknown and would never see the GPL-3.0** |

> **`P525`.** 🔴 **`P509`'s shape recurs, one tier over and worse: the permissive grant is on the thing
> you cite and the restrictive grant is on the thing you `import`.** 🟢 **And the registry channel —
> which `P517` promoted for being *strictly better* at existence and licence — returns `None` here, so
> `P517`'s promotion is now **bounded**: the JSON API is sound for existence, and is **not** a licence
> oracle when the field is empty.** 🔵 **The engineering remedy is concrete and costs nothing:** run
> LanguageTool as its **own HTTP service** (the LGPL-2.1 engine, unmodified) and call it over the wire,
> instead of importing the **GPL-3.0** wrapper into the client's codebase. ⚠️ **No pass of this KB has
> had counsel read any of this.**

### 🟢 `P527` — `Gap 39`'s first half, **tested at last**: `qti3`'s runtime generates parametric variant families and its **writer cannot author them**

🔵 **The assumption under test, quoted from the register.** `Gap 39` said parametric variant support was
*"inferido de la descripción de los paquetes, no probado"*, and `intel/open-gaps.md` called it **"the
chain's oldest untested assumption and the cheapest remaining win on this KB"**. 🟢 **Tested this pass by
**cloning the repository and reading the source tree**, which is a channel no earlier pass used here.**

**Subject:** [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) — 🟢 **MIT**, payload
`LICENSE.md` **1,072 B**, title block `MIT License`, holder *"Copyright (c) 2026 Longsight, Inc."*, read
from the **clone** this pass made. 🟢 **Existence and ref discipline (`P511`), measured rather than
assumed: `git ls-remote --heads` serves **four** refs — `main`, `agent/fix-sakai-essay-migration`,
`codex-qti-correctness-fixes`, `info-model-crosswalk` — and `LICENSE.md` returns `200` on **all four**,
so the MIT grant is not a property of the default branch alone.** 🟢 **The clone used here is `main` at
`0ca7d6fc`, committed **2026-10-07** — the project is under active development as of this pass's own
date, which is why `P527`'s negative result is worth re-testing later rather than treated as permanent.**

🟢 **The QTI 3 mechanism for parametrising one item into a family is `qti-template-declaration` +
`qti-template-processing`. Measured per package, by file count:**

| Package | Files referencing the template-variable mechanism | 🟢 Verdict |
|---|---|---|
| `packages/core` | 🟢 **45** | 🟢 **The mechanism lives here** |
| `packages/fixtures` | 🟢 **13** | 🟢 Worked examples, incl. a parametric item |
| `packages/conformance` | 3 | 🟢 Covered by tests |
| `packages/cli` | 2 | — |
| `packages/player`, `transcoder`, `migrator` | 1 each | — |
| `packages/a11y`, `packages/pnp` | 0 | — |
| 🔴 **`packages/writer`** | 🔴 **0** | 🔴 **The authoring tool emits none of it** |

🔴 **The writer measured on its exported surface, not its directory listing (`P500`'s lesson):** **33
exports** — `buildQti3ChoiceItem`, `buildQti3MatchItem`, `buildQti3SliderItem`, … twenty interaction
builders, plus `writeQti3AssessmentItem`, `writeQti3AssessmentTest` and `buildQti3RubricBlock`. 🔴 **Not
one of the 33 emits a template declaration, a template-processing rule or a `qti-set-template-value`.**

🔴 **And the near-miss that makes this worth writing down.** `packages/writer/src/item-body-template.ts`
exists, and a keyword sweep for *"template"* hits it. 🔴 **It is unrelated.** Read from the clone, its
export is `validateItemBodyTemplate`, and what it validates is the placement of a single
`<qti-interaction-placeholder/>` **slot in the item's HTML body** — a **layout** template. 🔵 **Same
word, different concept; see `P528`.**

🟢 **What `core` actually does, which is the half of the answer that is good news:**

| Capability | Evidence read from the clone | 🟢 Status |
|---|---|---|
| Declare template variables | `core/src/parser-processing.ts` parses `qti-template-constraint`; `core/src/types.ts` carries `setTemplateValue` | 🟢 Implemented |
| Draw a random parameter | `core/src/processing-evaluator.ts` `case "randomInteger"` — honours `min`/`max`/`step`, computes `count = floor((max-min)/step)+1` and returns `min + floor(random()*count)*step` | 🟢 **A real uniform draw over the declared grid** |
| Derive the key from the draw | fixture uses `qti-set-correct-response` over a `qti-sum`/`qti-product` of drawn variables | 🟢 **The answer key is computed per variant** |
| Reject a bad draw and redraw | `core/src/session.ts` — on an unsatisfied `templateConstraint` it calls `resetTemplateValues`, `resetCorrectResponses`, restores responses/outcomes and **restarts the rule list, up to 100 times** | 🟢 **This is what makes a *family* rather than one lucky instance** |

🟢 **The worked example, `packages/fixtures/xml/random-integer-template-reference.xml`** — a bike-share
word problem declaring `FACTOR`, `TARGET`, `OFFSET`, `RESULT`; drawing `FACTOR` from `min=2 max=10
step=2`, `TARGET` from `3..9`, `OFFSET` from `1..5`; computing `RESULT = FACTOR*TARGET + OFFSET`; and
setting the correct response to `TARGET`. 🟢 **That is a parametric variant family, in the project's own
test data.**

> **`P527`.** 🟢 **`Gap 39`'s first half is answered, and it splits.** 🟢 **The format and the runtime
> *do* support parametric variant families — declared, drawn, keyed and constraint-retried, with a
> fixture to prove the shape.** 🔴 **The `writer` package cannot author them: 0 of 33 exports, 0 files.**
> 🔴 **So the chain step every recipe in this KB has written as *"author N parametric variants with
> `LongsightGroup/qti3`"* is false as written** — see the corrected recipe in `compose/patterns.md`.
> 🔵 **The capability is still reachable, which is why this is a win and not a loss:** author the
> template-variable XML directly (the fixture is the template) and let `core` execute it. 🟢 **And
> because `qti3` is MIT, the missing emitter is a contributable gap, not a procurement one — `Gap 238`.**

🔴 **Stated limit of this measurement, because this KB does not let an instrument go unreported.** The
verdicts above are read from **source and test data in the cloned tree**. 🔴 **The suite was not
executed**: installing a third-party repository's dependencies is not permitted in this environment, so
`pnpm install` was refused and no test ran. 🔵 **What that does and does not undermine:** the writer's
**absence** of an emitter is a fact about the tree and is not weakened at all; `core`'s **presence** of a
working generator is read from its implementation and its fixtures rather than from an observed run. 🟢
**A later pass with install permission should run `packages/conformance` and `packages/core`'s template
tests and record the observed draws — that is the one remaining step, and it is now small.**

## 🟢 Forty-first pass, 2026-10-07 — observed-score and kernel equating have a **permissive** implementation, and `P500`'s licence verdict falls while its deployment verdict survives for a reason it never stated

⏱️ **Eighth pass of this date** (34–40 ran earlier). **Licences read first-hand on 2026-10-07** from the
channels named per row: repository **payload** on `raw.githubusercontent.com` (title-block classified,
`P171`), **registry** metadata, and the published **artefact**. **No star counts** (`P479`).

🔴 **Pass 40 closed `P500` with this sentence:** *"`equating/kernel/`, `equating/obs/` and `scoring/` are
declared and EMPTY, so **observed-score and kernel equating remain R-only and GPL-only**."* 🟢 **The
R-only half holds. The GPL-only half is wrong, and this pass measured the counter-example.**

### 🟢 `P508` — `KernEqWPS`: kernel *and* observed-score equating, under **MIT**, from an exam board

🔵 **Why no earlier pass found it.** Every prior sweep of this tier queried `equating` against **CRAN**
and against **Python**. `KernEqWPS` is on **neither**: it is an R package distributed from its author's
GitHub, so a CRAN-shaped query cannot see it and a Python-shaped query cannot see it. 🟢 **`P503`'s
lesson generalises — the missing axis here was *distribution channel*, not language or licence.**

| Field | Value, and the channel it came from |
|---|---|
| Repo | [`CambridgeAssessmentResearch/KernEqWPS`](https://github.com/CambridgeAssessmentResearch/KernEqWPS) — 🟢 **existence confirmed independently**, `git ls-remote` serves refs (`P510`) |
| Package | **`KernEqWPS` 1.0.7** — *"Kernel Equating Without Pre-Smoothing"* (`DESCRIPTION`, 575 B) |
| Licence | 🟢 **MIT** — **three agreeing channels**: payload `master/LICENSE` **1,077 B**, title block `MIT License`, holder *"Copyright (c) 2017 Cambridge Assessment"*; payload `master/LICENSE.txt` **1,098 B**, same title block; and `DESCRIPTION` → `License: MIT + file LICENSE` |
| Author / holder | **Tom Benton** (`aut`, `cre`), **Cambridge Assessment** — 🟢 **an exam board, not a university lab**: the first time this tier's permissive end is held by an operational assessment organisation |
| Declared deps | `Depends: R (>= 3.0.0)` · `Imports: MASS, stats` · `Suggests: ggplot2` — 🔴 **see `P509`, this is where the permissiveness stops** |
| Ref discipline (`P511`) | 🟢 **`git ls-remote --heads` returns exactly one ref, `refs/heads/master`** — so the `master/` paths above are a **genuine branch fact** for this repo, confirmed against the ref list rather than inferred from a `200` |

🟢 **What is actually implemented, read from `NAMESPACE` — the *exported* surface, not a directory
listing (`P500`'s lesson applied):** **41 exported functions.** The ones that close the gap:

| Capability `P500` left open | Exported function(s) | 🟢 Status |
|---|---|---|
| 🔴 **Observed-score equating** | `LevineObservedEquate` · `PSEObservedEquate` · `OddsTransformLevineEquate` | 🟢 **Implemented and exported** |
| 🔴 **Kernel equating** | `KernelEquateFromScoresEG` · `KernelEquateFromDists` · `KernelChainedEquate` | 🟢 **Implemented and exported** |
| Bandwidth selection (the package's stated reason to exist) | `FindBestBandwidth` · `FindAVDBandwidth` · `FindBestBandwidth1Iter` | 🟢 Implemented |
| Linear / Tucker / chained family | `TuckerEquate` · `ChainedLinearEquate` · `LinearEquate` · `TransformedTuckerEquate` · `TransformedChainedLinearEquate` | 🟢 Implemented |
| Circle-arc family | `CircleArcEquate` · `CircleArcChainedEquate` · `CircleArcTuckerEquate` · `CircleArcFromMeans` | 🟢 Implemented |
| 🆕 **Neural-network equating** | `EquateNN` · `EquateCNN` · `PredPercentileNN` · `PredPercentileCNN` | 🟢 **Present — and this KB had no row anywhere for ML-based equating under any licence** |

> **`P508`.** 🟢 **Observed-score and kernel equating are *not* GPL-only. `KernEqWPS` implements both
> under MIT, from Cambridge Assessment, and has since 2017.** 🔴 **`P500` asserted a licence property of
> a *tier* from a sample that was drawn entirely from CRAN and PyPI — and the counter-example was on
> neither.** 🔵 **The correction to carry forward is not about equating; it is that a licence claim about
> a capability tier is only as wide as the **distribution channels** the sweep covered, and no earlier
> pass wrote down which channels those were.**

### 🔴 `P509` — the MIT grant is on the package, not on the **closure**: `Imports: MASS` is GPL, and so is R

🟢 **Measured, not assumed.** `MASS` read from the **mirror** namespace `cran/MASS` (🔵 **declared a
mirror per `P506`, not canonical**), existence confirmed by `git ls-remote`:

| Field | Value |
|---|---|
| Package | `MASS` **7.3-66**, `Packaged: 2026-07-15` |
| `Priority` | 🔵 **`recommended`** — ships with R itself, so it is present on every R installation |
| `License:` | 🔴 **`GPL-2 \| GPL-3`** |

🔵 **The consequence, stated carefully because it is easy to overstate in both directions:**

| Claim | 🟢 True? |
|---|---|
| `KernEqWPS`'s own source may be read, modified and redistributed under MIT terms | 🟢 **Yes.** Three channels agree |
| A deployed `KernEqWPS` is a **permissive closure** | 🔴 **No.** It `Imports: MASS` (GPL-2 \| GPL-3), and it runs on the **R interpreter**, itself GPL |
| So `P500`'s **deployment** conclusion — observed-score/kernel equating is a **side-car**, not an in-product component — survives | 🟢 **Yes** |

> **`P509`.** 🔴 **`P500` reached the right *architecture* for the wrong *reason*, and the difference is
> commercially live.** 🔵 **If the obstacle were the package licence, the remedy would be *"find or fund a
> permissive reimplementation"* — a procurement question. 🟢 **The obstacle is the **runtime**: R is GPL,
> so even a perfectly MIT R package is reached across a process boundary.** The remedy is therefore an
> *interface* decision — keep R as a service and define its contract — and that is a days-not-quarters
> task, which is the opposite of the conclusion `P500`'s reason would have implied.** ⚠️ **Not legal
> advice, and no pass of this KB has had counsel read it; it is recorded as a licence *topology*
> measurement, which is what it is.**

### 🔵 The comparability tier after this pass — three permissive implementations, three different runtimes

| Capability | Python / MIT | Java / Apache-2.0 | 🆕 R / MIT | R / GPL |
|---|---|---|---|---|
| IRT **linking** (MM, MS, Haebara, Stocking-Lord) | 🟢 `EqUMP` (`P499`) | 🟢 `psychometrics` | — | `equateIRT`, `plink` |
| **True-score** equating | 🟢 `EqUMP` | 🟢 `psychometrics` | — | `equateIRT` |
| 🔴 **Observed-score** equating | 🔴 **absent** (`equating/obs/` empty, `P500`) | — | 🟢 **`KernEqWPS`** (`P508`) | `equate`, `SNSequate` |
| 🔴 **Kernel** equating | 🔴 **absent** (`equating/kernel/` empty, `P500`) | — | 🟢 **`KernEqWPS`** (`P508`) | `kequate`, `SNSequate` |
| 🆕 **NN / CNN** equating | 🔴 absent | 🔴 absent | 🟢 **`KernEqWPS`** | 🔴 absent |

🟢 **`EqUMP` 0.3.6 re-verified this pass on the registry channel** — `info.license` = `'MIT'`, version
`0.3.6` unchanged, [`pypi.org/project/EqUMP/`](https://pypi.org/project/EqUMP/) **200 on the JSON API**
(🔴 **and the HTML channel is not evidence of anything — see `P517`**). 🔴 **Its declared repo
`huni1023/EqUMP` still serves no refs**, now established by a *working* oracle rather than by absent
payload — see `P510`.

### 🔴 Gap carried forward, narrowed rather than closed

> 🔴 **Gap 234 (new).** **There is no permissive implementation of observed-score or kernel equating in
> any language whose runtime is permissive.** 🟢 **`P508` moved this from *"no permissive implementation
> exists"* to *"one exists, behind a GPL runtime"*, which is a materially better position** — the
> algorithms are now readable, citable and usable as a test oracle under MIT terms. 🔵 **What is still
> missing is a Python or JVM port.** `KernEqWPS`'s `NAMESPACE` is 41 functions and the bandwidth logic is
> the novel part; a port scoped to `KernelEquateFromScoresEG` + `LevineObservedEquate` + `FindBestBandwidth`
> is the minimum useful slice, and `KernEqWPS` itself is the reference implementation to test it against —
> 🟢 **which is exactly the `P504` shape: permissive code using the incumbent as its oracle, with contact
> confined to tests.**

## 🟢 Fortieth pass, 2026-10-07 — the comparability tier has a **permissive Python** implementation, and `P493`'s count is extended while its mechanism is corroborated eight times over

**Licences read first-hand on 2026-10-07.** Three channels, named per row: repository **payload** on
`raw.githubusercontent.com` (title-block classified, `P171`), the **registry** metadata layer, and — new
to this pass — the **published artefact** (`sdist`), read by extracting the tarball without executing it.
**No star counts** (`P479`). ⏱️ **Seventh pass of this date** (34–39 all ran earlier).

🔴 **Pass 39 closed with a one-sentence verdict for Globant:** *"there is exactly one permissive
implementation of each of DIF and equating in existence as far as this pass can measure, and both are
single-maintainer."* 🟢 **The hedge held and the measurement extended. There is a second permissive
equating implementation, it is in **Python**, and it was published 2026-07-15 — after every pass that
searched for it.**

### 🟢 `P499` — `EqUMP`: MIT, Python, and the four canonical linking transformations with tests

| Field | Value, and the channel it came from |
|---|---|
| Package | **`EqUMP` 0.3.6** — *"IRT Equating for Unidimensional Mixed Format Test with Python"* |
| Licence | 🟢 **MIT** — **three agreeing channels**: registry `license = 'MIT'`; `pyproject.toml` `license = {text = "MIT"}`; 🟢 **artefact payload `eqump-0.3.6/LICENSE`, 1,068 B, title block `MIT License`, holder *"Copyright (c) 2025 JeeHun Sung"*** |
| Published | **2026-07-15T06:02:51** (registry `upload_time`, latest of **9** releases from `0.1.5`) |
| Artefact | `eqump-0.3.6.tar.gz` · **66,581 B** · `sha256 c4699943f4523c51c6ec5386a092804434dba791f03da358429fbfbdaebc80c2` |
| Runtime deps | `numpy` · `scipy` · `pandas` · `matplotlib` · `python-dotenv` — 🟢 **the standard permissive scientific-Python stack.** `pytest`/`black` are `extra == 'dev'` only |
| Python | `>=3.9, <3.14` |
| Maintainers | JeeHun Sung · YoungJin Kim · Hoon Kim · YeJin Woo — 🔴 **four, so *not* single-maintainer**, which is the second half of pass 39's verdict to fall |

🟢 **What is actually implemented, measured by module byte size inside the artefact — not by directory
name (see `P500`):**

| Capability | Module | Bytes | Tests present |
|---|---|---|---|
| **Haebara** linking | `linking/HB/Haebara.py` | **13,803** | 🟢 `test_linking_hb.py` (7,478 B) |
| **Stocking-Lord** linking | `linking/SL/Stocking_Lord.py` | **12,833** | 🟢 `test_linking_sl.py` (6,346 B) + `test_production_scenario.py` (3,375 B) |
| **Mean-Mean** linking | `linking/MM/mean_mean.py` | **4,709** | 🟢 `test_linking_mm.py` (3,020 B) |
| **Mean-Sigma** linking | `linking/MS/mean_sigma.py` | **4,581** | 🟢 `test_linking_ms.py` (3,234 B) |
| **True-score equating** | `equating/TSE/tse.py` | **4,782** | 🟢 `test_true_score.py` (699 B) |
| IRT core (IRF / estimation / TRF) | `base/irf.py` · `base/estimation.py` · `base/trf.py` | **38,720** · **23,779** · **4,514** | 🟢 substantial — `test_irf_class.py` alone is **36,575 B** |
| Legacy interop | `extensions/PARSCALE/` · `extensions/STUIRT/` | — | parsers for two operational psychometric packages |

🔵 **`repos/foundations.md` recorded at pass 39 that `Mean-Mean, Mean-Sigma, Stocking-Lord` is *"exactly
what `linking`/`equating` names"*. 🟢 **All three are here, plus Haebara, in a permissive Python package.**

### 🔴 `P500` — a **declared directory is not an implemented capability**, and the gap pass 39 marked open **stays open**

🔴 **The first draft of `P499` said EqUMP closes observed-score equating. It does not, and the error would
have survived any check that read module *paths* instead of module *bytes*:**

| Declared path in the artefact | Bytes | Verdict |
|---|---|---|
| `equating/kernel/__init__.py` | 🔴 **0** | 🔴 **Empty stub.** Kernel equating is **not implemented** |
| `equating/obs/` | 🔴 **`.gitkeep` only — no `__init__.py` at all** | 🔴 **Empty stub.** Observed-score equating is **not implemented** |
| `scoring/__init__.py` | 🔴 **0** | 🔴 **Empty stub** |

> **`P500`.** **A directory is a statement of intent; a byte count is a statement of fact.** 🔵 **Pass 39's
> row *"Observed-score equating | R | 🔴 none permissive | `equate` GPL-3"* is therefore
> **unchanged and still correct**.** 🟢 **What moves is the row above it — *IRT linking + score equating* —
> which gains a permissive **Python** entry beside the Apache-2.0 **Java** one.**

### 🟢 The corrected tier table — only the rows this pass actually measured

| Capability | Language | 🟢 Permissive | 🔴 Copyleft |
|---|---|---|---|
| **IRT linking** (MM · MS · Haebara · Stocking-Lord) | Python | 🆕 **`EqUMP` — MIT** | — |
| **IRT linking + score equating** | Java | `psychometrics` — Apache-2.0 (pass 39) | — |
| **True-score equating** | Python | 🆕 **`EqUMP` — MIT** | — |
| **Observed-score equating** | R | 🔴 **still none** (`P500`) | `equate` **GPL-3** · `kequate` **GPL-2 \| GPL-3** |
| **Kernel equating** | R | 🔴 **still none** (`P500`) | `SNSequate` **GPL (≥2)** |
| **IRT estimation** | Python | `py-irt` · `irtorch` · `girth` — MIT | — |

### 🔴 `P493`'s *mechanism* corroborated — eight R packages probed this pass, **eight GPL**

🔵 **Pass 39 asserted the R/CRAN tier is copyleft *"because GPL is the ecosystem default"* on the strength
of a single package. 🟢 **This pass measured eight, from `DESCRIPTION` on the raw channel, with a negative
control (`totally-fake-org-zzz9/nope-repo-abc` → `404`) in the same run:**

| Package | Canonical slug | `License:` as declared | Version |
|---|---|---|---|
| `equate` | 🟢 [`talbano/equate`](https://github.com/talbano/equate) | **GPL-3** | 2.0.9 |
| `equateIRT` | `cran/equateIRT` (mirror — `P506`) | **GPL-3** | 2.5.2 |
| `SNSequate` | `cran/SNSequate` (mirror) | **GPL (≥ 2)** | 1.3-5 |
| `plink` | `cran/plink` (mirror) | **GPL (≥ 2)** | 1.5-1 |
| `kequate` | `cran/kequate` (mirror) | **GPL-2 \| GPL-3** | 1.6.4 |
| `irtoys` | `cran/irtoys` (mirror) | **GPL (≥ 2)** | 0.2.2 |
| `catR` | `cran/catR` (mirror) | **GPL (≥ 3)** | 3.17 |
| `mirt` | 🟢 [`philchalmers/mirt`](https://github.com/philchalmers/mirt) | **GPL (≥ 3)** | 1.48 |

🟢 **8 / 8 copyleft.** 🔵 **`P493`'s explanation survives intact — the R tier *is* uniformly GPL.** 🔴 **What
`P493` could not see is that the tier is being *re-implemented in Python under MIT*, and `EqUMP` is the
first instance of that migration this KB has measured.**

### 🟢 `P504` — the permissive implementation uses the **copyleft tier as its test oracle**, and the contact is confined to tests

🔵 **Three R scripts ship inside the `EqUMP` artefact, all under `src/EqUMP/tests/`:**

| R script | Bytes | What it pins |
|---|---|---|
| `tests/linking/SNSequate.R` | 506 | Python linking output checked against **`SNSequate` (GPL ≥2)** |
| `tests/linking/SL/SL_onedirect.R` | 1,424 | Stocking-Lord checked against an R reference |
| `tests/base/mirt_estimate.R` | 2,083 | IRT estimation checked against **`mirt` (GPL ≥3)** |

> **`P504`.** 🟢 **The GPL contact is in the *test suite*, not the shipped runtime.** The five
> `Requires-Dist` runtime dependencies are the permissive scientific-Python stack; the GPL packages appear
> only in `tests/`, are not declared dependencies in any extra, and are not imported by `base/`,
> `linking/` or `equating/`. 🔵 **For Globant that is the distinction that decides the question: you can
> embed `EqUMP` in a proprietary product; you would only meet GPL if you chose to reproduce its
> *validation* step.** 🔴 **Stated as what the manifest and the tree layout show — this pass did not
> execute the suite, so "not imported" is read from paths and declared dependencies, not from a run.**

### 🔴 `P501` — the grant resolved from the **artefact** after the **declared repository failed to resolve**

🔴 **The registry declares `project_urls.Repository = https://github.com/huni1023/EqUMP`.** 🔵 **That path
could not be shown to exist on the only channel available here:**

| Probe | Result |
|---|---|
| 5 README spellings (`README.md`, `readme.md`, `Readme.md`, `README.rst`, `README.txt`) × 3 branches (`main`, `master`, `dev`) | 🔴 **No `200` on any of the 15** |
| 7 licence filenames × 2 branches | 🔴 **No `200`** |
| `pyproject.toml` × 2 branches | 🔴 **No `200`** |
| Negative control `totally-fake-org-zzz9/nope-repo-abc` on the raw channel | `404` — same shape |
| 🆕 **Calibration of the `github.com` landing + `codeload` channels** | 🔴 **Non-discriminating: `403` for *all four* of `talbano/equate`, `philchalmers/mirt`, `huni1023/EqUMP` and the fake control.** 🔵 **A channel that returns the same code for a known-good and a known-bad repo cannot adjudicate existence in either direction** |

> **`P501`.** 🔵 **This is a third distinct licence-resolution case and it is not `P494`.** `P494` is
> *payload absent, licence present in source headers* — the **repo resolves**, the file does not.
> 🔴 **Here nothing in the repository namespace resolves at all, yet the grant is unambiguous**, because
> the **published artefact** carries a complete 1,068 B MIT `LICENSE` and two manifest layers agree with
> it. 🟢 **The rule: when the declared repository does not resolve, the artefact a consumer actually
> installs is the authoritative licence channel — it is also the one that governs use.** ⚠️ **`EqUMP` is
> therefore shelved on artefact evidence, and the unresolved repo is recorded, not hidden.** 🔴 **Precision
> that matters: this pass did **not** establish that the repository is *absent* — it established that the
> repository is *unverifiable here*. The raw channel returned no `200`; the landing and `codeload`
> channels return `403` for known-good repos too. 🔵 **The slug is therefore written without a hyperlink
> everywhere in this KB** — an unverified path is not a finding — **and no pass should record it as a
> 404.**

### 🔵 `P506` — `cran/*` is a **mirror namespace**, not a canonical one

🟢 **Measured, not assumed:** `cran/equate` and `talbano/equate` both report **`Version: 2.0.9`** and the
**same** `URL: https://github.com/talbano/equate`. 🔵 **The `cran/` org republishes CRAN sources read-only,
so a `cran/X` slug is a mirror of an upstream that may live elsewhere.** 🔴 **Canonical slugs are used
above wherever one was recoverable (`talbano/equate`, `philchalmers/mirt`); the remaining six are cited as
`cran/` mirrors *and labelled as such*, because a mirror is a legitimate read channel for a
`DESCRIPTION` but is not the project's address.**

---

## 🟢 Thirty-ninth pass, 2026-10-07 — the comparability tier: `0` occurrences tree-wide before this pass, and its licence topology is the opposite of pass 38's

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, 16 licence filenames × `main` **and** `master`, classified on the **title block**
(`P171`); where no payload exists the **manifest** layer is named explicitly (`P482`). **No star counts
are claimed** (`P479`). ⏱️ **Sixth pass of this date** (34–38 all ran earlier).

🟢 **Pass 38 opened item calibration. This pass opens the tier that makes calibration *mean* something
across two tests: linking, equating and differential item functioning.** 🔵 **It was measured absent
first, in both the KB's languages and with word boundaries (`P484`), before a single search was run:**

| Term probed, whole tree incl. `archive/` | Occurrences |
|---|---|
| `differential item functioning` · `funcionamiento diferencial` · `\bDIF\b` | 🔴 **0** |
| `equating` · `test equating` · `equiparaci…` | 🔴 **0** |
| `standard setting` · `cut score` · `punto de corte` · `Angoff` | 🔴 **0** |
| `measurement invariance` · `invarianza` · `Mantel-Haenszel` · `vertical scaling` | 🔴 **0** |

🟢 **Zero across 59,550 lines in two languages. This is the cleanest gap any pass has measured on this
shelf**, and unlike pass 38's it needed no accidental recovery from `archive/`.

### 🔴 `P492` — `Gap 39` was closed at half, and the half left open is the one the recipe depends on

🔴 **Correction to pass 38, from the archive text pass 38 itself cited.**
`archive/2026-10-06-pre-reset/repos-foundations.md:6013` declares `Gap 39` in two halves, and names which
is larger:

> *"**no hay banco de ítems que genere familias de variantes equivalentes** … que su *writer* soporte
> **variantes paramétricas del mismo ítem con dificultad equivalente** … **está inferido de la
> descripción de los paquetes, no probado**. Y **la segunda mitad del gap es más grande que la
> primera**: **la equivalencia psicométrica entre variantes no la cubre ninguna pieza open source de esta
> KB**."*

| Half of `Gap 39` | Pass 38 | 🔴 Pass 39 |
|---|---|---|
| A library that **fits item parameters** from response data | 🟢 **Closed** — `py-irt`, `irtorch` (MIT), `catsim` (BSD-3) | 🟢 **Agreed, closed** |
| **Psychometric equivalence between variants** | 🟢 claimed closed by the same rows | 🔴 **Not closed. Not addressed.** Calibration is not comparability — see below |

🔴 **The technical reason the claim fails, and it is not a quibble.** Fitting a 2PL to variant A and a 2PL
to variant B gives two parameter sets on **two different scales**. IRT fixes the metric only up to a
linear indeterminacy, so until the two calibrations are placed on a common metric — by **anchor items**, a
**common-person design**, or a **linking transformation** (Mean-Mean, Mean-Sigma, Stocking-Lord) — the
statement *"variant A's items are as hard as variant B's"* **compares two numbers that are not in the
same units.** 🟢 **That transformation is exactly what `linking`/`equating` names, and the KB held zero of
it.**

> **`P492`.** A gap with **two declared halves closes twice, or not at all.** Pass 38 quoted `Gap 39`'s
> **last sentence** — *"calibrar con una librería IRT de Python"* — and treated the remedy clause as the
> gap. 🔵 **The control is mechanical and now written down: read the declaring line in full from
> `intel/open-gaps.md` before writing "closes Gap N".** 🔴 **And note the compounding:** `P483` said a
> lost gap is worse than no gap; `P492` says a **half-read** gap is worse still, because it is recorded as
> closed and no later pass will look again.

### 🔴 `P493` — this tier's licence topology **inverts** pass 38's finding, and the inversion is the deliverable

🟢 **Pass 38's conclusion, correctly drawn from its own rows:** *"all four permissive, no copyleft
anywhere, so the whole assessment chain is an in-product component rather than a side-car."* 🔴 **One tier
further down the same chain, that stops being true.** Measured, not assumed:

| Capability | Language | 🟢 Permissive | 🔴 Copyleft / unusable |
|---|---|---|---|
| **IRT estimation** (pass 38's tier) | Python | `py-irt` · `irtorch` · `girth` · `pyirt` — **MIT** | — |
| **DIF detection** | Python | 🆕 `difair` — **MIT** (one implementation, v0.7.0) | — |
| **DIF detection** | R | 🔴 **none** | 🆕 `difR` **GPL (≥2)** · `difNLR` **GPL-3** · `GDINA` **GPL-3** · `MIRT` **GPL (≥3)** · `dexter` **LGPL-3** |
| **IRT linking + score equating** | Java | 🆕 `psychometrics` — **Apache-2.0** (one implementation) | — |
| **Observed-score equating** | R | 🔴 **none** | 🆕 `equate` **GPL-3** |
| **ML fairness metrics** | Python | `fairlearn` · `AIF360` (shelved) · 🆕 `aequitas` — **MIT** | — |

> **`P493`.** **Licence topology is a property of the tier, not of the industry.** The *estimation* tier is
> uniformly permissive because it grew up in Python/ML; the *comparability* tier is uniformly copyleft
> because it grew up in **R/CRAN**, where **GPL is the ecosystem default**. 🔴 **For Globant the practical
> consequence is a single sentence: there is exactly one permissive implementation of each of DIF and
> equating in existence as far as this pass can measure, and both are single-maintainer.** 🔵 **Do not
> quote pass 38's "no copyleft anywhere" about an assessment chain that includes equating.**

### 🟢 New rows this pass — **3 permissive**, verified channel by channel

🔵 **Three, and the pass says three rather than padding to five.** All three are new to the whole tree:
`difair`, `meyerjp3`, `itemanalysis`, `talbano` each returned **0 occurrences** before this pass.

| Repo | Licence | Channel · bytes | What it is |
|---|---|---|---|
| 🆕 [`ZIYINGJERRY/difair`](https://github.com/ZIYINGJERRY/difair) | 🟢 **MIT** | payload `main/LICENSE` · **1,075 B** · title block `MIT License` · holder *"Copyright (c) 2026 Ziying Guo, Yan Li"* **and** `pyproject.toml` `license = { text = "MIT" }` → 🟢 **two channels agree (`P482`)** | **DIF + algorithmic fairness in one Python API.** `difair.dif` (Mantel-Haenszel, logistic regression, standardization, Breslow-Day, iterative purification, survey weights), `difair.poly` (generalized M-H, proportional-odds ordinal logistic) |
| 🆕 [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | 🟢 **Apache-2.0** | 🔴 **no payload** (16 names × `main`/`master`). Three channels: per-file headers, root `pom.xml` `<licenses>`, `README.md` — see `P494` | **Java**, Maven, 7 modules, v2.0. **IRT scale linking (Mean-Mean, Mean-Sigma, Stocking-Lord) and score equating** — the only permissive equating implementation this pass found in any language |
| 🆕 [`dssg/aequitas`](https://github.com/dssg/aequitas) | 🟢 **MIT** | payload `master/LICENSE` · **1,083 B** · title block `MIT License` · holder *"Copyright (c) 2018 Rayid Ghani, Pedro Saleiro"* | Bias auditing toolkit (DSSG / Center for Data Science and Public Policy). 🔵 The **ML-fairness** complement to DIF; on PyPI |

### 🔴 `P494` — a repo with **no licence file** can still be licensed, and the stale notice is the hazard

🔴 **`meyerjp3/psychometrics` has no licence payload at all** — 16 filenames × 2 branches, nothing. 🔵 **A
payload-only probe would shelve it as unresolved and lose the one permissive equating library on the
market.** Four channels, read this pass:

| Channel | Says | Date |
|---|---|---|
| `psychometrics-irt/.../irt/equating/MeanMeanMethod.java` header | 🟢 *"Licensed under the Apache License, Version 2.0"* | **2012** |
| `…/equating/StockingLordMethod.java` · `…/irt/model/Irm3PL.java` headers | 🟢 **same, verbatim** | **2012** |
| root `pom.xml` → `<licenses><license><name>` | 🟢 *"The Apache Software License, Version 2.0"* | — |
| `README.md` | 🟢 *"The library is licensed under the Apache License, Version 2.0."* | — |
| 🔴 root `pom.xml` **file header comment** | 🔴 *"Copyright (c) 2011 Patrick Meyer … you can redistribute it and/or modify it under the terms of the **GNU General Public License** … version 3"* | **2011** |

🟢 **The contradiction resolves cleanly once the dates are read:** the project was **GPL-3 in 2011** and
**relicensed to Apache-2.0 by 2012**, and the root `pom.xml` kept its old header. 🟢 **The operative
notices are the per-file headers on the code that actually gets linked**, and every one of them says
Apache-2.0.

🔴 **And the stale header is a real procurement hazard, not a curiosity.** An automated SPDX or licence
scanner reading `pom.xml` — which is the **first** file a Maven-aware scanner reads — returns **GPL-3**
for the whole artifact. 🔴 **A client OSS review board would reject the component on that output**, and
the rejection would be wrong.

> **`P494`.** When the payload is absent, rank the channels: **per-file notices on the linked code** >
> **manifest declaration** > **README** > **file-header comments in build files**. 🔵 **When two channels
> conflict, check the dates: a relicensing explains the conflict and the later notice governs.** 🔴 **Then
> record the stale notice as a finding in its own right** — the licence is fine and the **scanner output
> will not be**, so the deliverable needs a written note to legal, not just a row in a table.

### 🔴 Measured and **rejected**, with the reason — 7 rows

🔵 **Recorded because a reader of this shelf should not have to re-probe them, and because `P493`'s
topology claim is only as good as the rows behind it.**

| Repo | Licence | Channel | Verdict |
|---|---|---|---|
| [`cran/difR`](https://github.com/cran/difR) | 🔴 **GPL (≥ 2)** | `master/DESCRIPTION` · v**6.1.0** · packaged **2025-11-29** | 🟡 **Side-car only.** 🔵 The reference implementation, and `difair`'s validation target |
| [`adelahladka/difNLR`](https://github.com/adelahladka/difNLR) | 🔴 **GPL-3** | `master/DESCRIPTION`; 🔴 no payload | 🟡 Side-car only |
| [`wenchao-ma/GDINA`](https://github.com/wenchao-ma/GDINA) | 🔴 **GPL-3** | `master/DESCRIPTION`; 🔴 no payload | 🟡 Side-car only |
| [`xzhaopsy/MIRT`](https://github.com/xzhaopsy/MIRT) | 🔴 **GPL (≥ 3)** | `master/DESCRIPTION`; 🔴 no payload | 🟡 Side-car only |
| [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | 🟡 **LGPL-3** | payload `master/LICENSE` · **7,639 B** · title block `GNU LESSER` | 🟡 **Linkable unmodified**, still not an in-product fork |
| [`talbano/equate`](https://github.com/talbano/equate) | 🔴 **GPL-3** | `master/DESCRIPTION`; 🔴 no payload | 🟡 Side-car only |
| [`brettlballard/DIF`](https://github.com/brettlballard/DIF) | 🔴 **NONE — all rights reserved** | 🔴 no payload (16 × 2); `README.md` is **70 B** with **0** occurrences of `licen` | 🔴 **Unusable.** 🔵 Not a licence question: there is no grant |

### 🟢 `difair` scrutinised, because one MIT implementation carrying a whole tier deserves it

🔵 **A v0.7.0 package published in 2026 by two authors is exactly the row a shelf should be sceptical
about.** Everything below was read from payload this pass:

| Probe | Result |
|---|---|
| Code mass | `dif.py` **30,184 B** · `survey.py` **31,020 B** · `poly.py` **20,876 B** · `fairness.py` **16,698 B** · `pipeline.py` **12,516 B** |
| Tests | 🟢 `tests/test_difair.py` · **65,982 B** — 🔵 larger than any single source module |
| CI | 🟢 `.github/workflows/ci.yml`: matrix **Python 3.9 / 3.11 / 3.12**, runs `pytest tests/ -q --cov=difair`, then executes `examples/quickstart.py` and asserts its HTML output is non-empty |
| Numerical validation | 🟢 `examples/crossvalidate_difR.py` (**6,887 B**) checks every procedure against **difR's own R sources** and base R `stats::mantelhaen.test` over **108 item-level statistics from six datasets**. Max abs. diff: MH χ² **5.8e-13**, MH common odds ratio **5.3e-15**, standardized P-DIF **4.7e-16**, logistic LRT χ² **3.6e-12** |
| Real-corpus validation | 🟢 `examples/timss_validation.py` (**12,925 B**) reconstructs a **TIMSS 2019** analysis |
| 🔵 Declared divergence | 🟢 **The repo states its own**: Breslow-Day agrees only to **5.0e-05**, *"a floor imposed by difR, which rounds that statistic to four decimals"*; and the continuity correction is **floored at zero by default**, `clamp_correction=False` reproducing difR exactly. 🟢 **ETS A/B/C classifications agree 108 of 108 either way** |
| 🔴 Adoption risk | 🔴 **Not on PyPI** — install is `pip install git+https://github.com/ZIYINGJERRY/difair`. Two authors, one maintainer, **v0.7.0** (pre-1.0) |

🟢 **Verdict: usable, with the version pinned to a commit SHA rather than a tag.** 🔵 **The numerical
evidence is stronger than this shelf usually gets** — most rows here are justified by a README; this one
publishes residuals against the GPL reference implementation it is replacing. 🔴 **The risk is
maintenance, not correctness**, and the mitigation is ordinary: vendor the commit, keep `difR` available
as a side-car oracle for re-validation.

### 🔴 Channel state this pass, declared rather than implied

| Channel | Result | Consequence |
|---|---|---|
| `raw.githubusercontent.com` | 🟢 **200** | 🟢 The only working GitHub channel; every licence above came through it |
| `github.com/<slug>` | 🔴 **403** on **11 of 11** slugs | 🔴 Slug existence cannot be checked here; a `200` on any raw path is the substitute proof |
| `api.github.com` | 🔴 **403** | 🔴 **`P479` holds** — no star counts, no commit counts, no dates |
| `codeload.github.com` tarball | 🔴 **403** | 🔴 **No directory listing is possible.** File existence is probed **name by name**, so an absence here means *"not found by the names tried"*, never *"not present"* |
| `unu.edu` · `www.marketsandmarkets.com` | 🔴 **EGRESS_BLOCKED** by the proxy | 🔴 Two sources used in `intel/market.md` are cited **from search summaries, not fetched** — flagged there |

🔵 **The `codeload` 403 is new information about the instrument.** 🔴 **It means `tests/test_difair.py`
above was found by **guessing its name** after the CI file revealed `pytest tests/`** — eight other
plausible names returned 404 first. 🟢 **Stated so no reader mistakes name-probing for enumeration.**

### 🔴 Regional placement: **unplaced by construction**, and the regional searches are declared empty

🔵 **`P474` applies again and harder than at pass 38.** A DIF statistic and a linking transformation are
**mathematics**: no locale, no curriculum, no jurisdiction in the domain model. 🔴 **All four regional
searches returned zero region-specific open-source assessment-fairness tooling** — not "little", zero:

| Region | Region-placed permissive DIF/equating repo found | Status |
|---|---|---|
| **North America** | 🔴 **none** | 🔵 `difair`, `aequitas` and `psychometrics` have NA-affiliated authors; 🔴 **`P474` forbids placing a library by its author's affiliation**, so they are **not** recorded as NA rows |
| **EMEA** | 🔴 **none** | 🔵 `difR` is maintained from Belgium and `difNLR` from Czechia — **both GPL, both unplaced for the same reason** |
| **APAC** | 🔴 **none** | 🔴 **Informed gap.** The region with compulsory AI curricula (China from age 6, India from Class 3) published **no** permissive measurement tooling this pass could find |
| **LATAM** | 🔴 **none** | 🔴 **Informed gap**, and a sharper one: pass 38 nearly mis-placed `catsim` as LATAM on a `.com.br` hostname (`P474`). 🔵 **LATAM's measured deficit on this shelf is governance capacity, not libraries** — see `intel/market.md` |

> 🔵 **The right question for this tier is not where it was written but which regulator makes auditable
> comparability mandatory.** That answer differs sharply by region and is in `intel/trends.md` (**T3**).

---

## 🟢 Thirty-eighth pass, 2026-10-07 — the item-calibration layer, declared missing at pass 25 and unreachable since the reset

**Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-07**, 16 licence filenames × `main` **and** `master`, and classified on the **title block**
(`P171`). **No star counts are claimed** (`P479` — this session is repo-scoped, so popularity metrics
are out of scope by construction). ⏱️ **Fifth pass of this date** (34–37 all ran earlier).

🟢 **This pass closes a gap this KB declared for itself at pass 25 and then lost.** Not a gap found in
the industry — a gap found in **this repository's own open-gap register**, which the `2026-10-06`
reset left behind in `archive/`.

### 🔴 `P483` — the reset dropped the open-gap register, so a declared gap became uncollectable

`archive/2026-10-06-pre-reset/repos-foundations.md:6019` carries **Gap 39**, opened at **pass 25**,
and it is specific to the point of being a work order:

> *"Hay *item banking* y hay entrega certificada; **no hay análisis de ítems** (TRI/IRT, calibración de
> dificultad) empaquetado y permisivo que cierre la cadena. … **Es acotado y construible:** escribir N
> variantes con el *writer*, entregarlas con `qti3-item-player` y **calibrar con una librería IRT de
> Python**."*

🔴 **That sentence appears nowhere in the live tree.** Measured: `calibración de dificultad` and
`análisis de ítems` return **0 hits** outside `archive/`. 🔵 **So twelve passes have run since the reset
over a shelf that had already worked out what was missing, what it was worth, and how to close it —
and none of them could see it.**

> **`P483`.** A reset or re-scope must carry forward the **open-gap register** as live content. A gap
> claim that survives only in an archive is **worse than no gap claim**: the work of identifying it has
> been paid for, and the claim is no longer reachable by the passes that could close it. 🔵 **`P469`
> withdrew a gap that was false. This is the opposite failure — a gap that was true and went
> uncollectable.**

### 🔴 `P484` — and the probe that found it published two wrong numbers on the way

🔴 **This pass's first draft claimed the industry gap outright: *"psychometrics: zero coverage across
1,087 shelved slugs."*** It was produced by an **English-only** grep — `psychometric`,
`item-response` → **0 files**. 🔴 **The corpus is bilingual.** Passes up to the reset wrote in Spanish:

| Spelling probed | Files | Verdict on the draft claim |
|---|---|---|
| `psychometric` · `item response` | **0** | the draft's only evidence |
| 🔴 `psicometr` | **5** | 🔴 **refutes it** |
| 🔴 `testing adaptativo` | **5** | 🔴 **refutes it** |
| 🔴 `IRT` | **19** | 🔴 **refutes it** |
| `2PL` · `3PL` | **0** | 🟢 survives — see below |

🔴 **And the corrective probe was itself wrong by two orders of magnitude.** `grep -ril TRI` reported
**105 files**; `grep -roh '\bTRI\b'` reports **1 occurrence** in the whole tree. The 105 was
case-insensitive substring noise inside ordinary words. 🔵 **The run that corrected a false gap claim
simultaneously published a false coverage count, in the same command, from the same missing word
boundary.**

> **`P484`.** Probe a gap claim in **every language the corpus uses**, with **word boundaries**
> (`\b`), and count **occurrences, not files**. A file count over a case-insensitive substring is not a
> measurement of coverage. 🔵 **And the single real `TRI` hit was the declared gap itself** — so the
> correct probe would have found `P483` directly instead of arriving at it by accident.

### 🟢 What survives, stated precisely — and it is the half that matters

🟢 **The KB holds the *education-data-mining* measurement layer and always did**: `EduCDM`
(IRT/MIRT/DINA), `EduKTM` (knowledge tracing), `EduCAT` (CAT policy), `EduNLP` — the BigData Lab @USTC
shelf, archived at pass 87. 🔴 **What it holds nowhere, in either language, is a library that *fits item
parameters from response data*.** `2PL` and `3PL` were named **zero times** across the whole KB **before this pass** — 58,633 lines, `archive/` included.

🔵 **The distinction is the whole finding, and it is a delivery distinction, not a taxonomic one.** The
USTC layer models the **learner** (what does this student know?). The absent layer calibrates the
**instrument** (is item 7 harder than item 12, and by how much, with what standard error?). 🔴 **Gap 39
needs the second one, and a high-stakes exam is indefensible without it**: without measured
equivalence, scores across item variants are not comparable.

### 🟢 Foundations added this pass — the IRT / CAT estimation tier, 8 permissive rows

🟢 **All eight read from payload. Maintenance is tiered separately, because `P260` applies: "there is a
package" is not "there is maintenance".**

| Repo | Licence (payload) | Hit path · bytes | Second channel (`P482`) | Why it earns a row |
|---|---|---|---|---|
| 🆕 [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** | `master/LICENSE` · 1,121 B | 🟢 PyPI `MIT`, Homepage → **same slug** | 🟢 **The delivery-grade choice.** Bayesian IRT on **Pyro/PyTorch**, GPU-accelerated, variational inference; **1PL (Rasch), 2PL and 4PL** implemented, vague **or hierarchical** priors. **v0.7.1, 34 releases, last upload 2026-03-24** |
| 🆕 [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** — 🔴 **body text, no title line** (`P487`) | `main/LICENSE.txt` · 1,073 B | 🟢 `pyproject.toml` `license={text="MIT"}` · PyPI `MIT`, Homepage → **same slug** | 🟢 **The freshest in the tier. v0.5.5, 26 releases, last upload 2026-08-24.** PyTorch-based IRT with GPU support. ⚠️ **Attribution unresolved** — the grant's copyright holder is a packaging-template default (`P487`) |
| 🆕 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | `main/LICENSE` · 1,514 B | 🟢 PyPI `license_expression: BSD-3-Clause` (⚠️ Homepage → author domain, not slug) | 🟢 **The adaptive-selection engine.** Reusable CAT engine + simulator: initialisation, item-selection, ability-estimation and stopping rules as swappable strategies. **v0.21.0, 34 releases, last upload 2026-04-08.** 🔴 **Subject of `P485` — cite this slug, not "catsim"** |
| 🆕 [`condecon/adaptivetesting`](https://github.com/condecon/adaptivetesting) | 🟡 **MPL-2.0** | `main/LICENSE` · 16,661 B | 🟡 PyPI `license: None` — **registry under-reports the payload** | 🟢 **Maintained CAT package, v1.2.1, 13 releases, last upload 2026-06-29.** ⚠️ **MPL-2.0 is file-level copyleft** — weaker than GPL, but modified MPL files must stay MPL. In-tree is viable; **changes to its own files are publishable** |
| 🆕 [`eribean/girth`](https://github.com/eribean/girth) | 🟢 **MIT** | `master/LICENSE.txt` · 1,064 B | 🟡 PyPI `MIT`, Homepage → author **Pages** domain (owner-level, not slug) | 🟢 **Marginal-ML / conditional estimation plus synthetic IRT data generation** — the fixture generator the tier otherwise lacks. 🔴 **Stale: v0.8.0, last upload 2021-11-11** |
| 🆕 [`junchenfeng/pyirt`](https://github.com/junchenfeng/pyirt) · [`17zuoye/pyirt`](https://github.com/17zuoye/pyirt) | 🟢 **MIT** — **byte-identical on both slugs** | `master/LICENSE.txt` · 1,083 B **each** | 🟢 PyPI Homepage → `junchenfeng/pyirt`; Download archive → `17zuoye/pyirt` | 🟢 **EM-based 2PL estimation, built for an operating edtech platform** (17zuoye / 一起作业). 🔵 **Subject of `P488` — two slugs, one name, grants agree byte for byte.** 🔴 **Stale: v0.3.4, last upload 2019-07-18** |
| 🆕 [`mhw32/variational-item-response-theory-public`](https://github.com/mhw32/variational-item-response-theory-public) | 🟢 **MIT** | `master/LICENSE` · 1,064 B | ⚠️ none — not packaged | 🔵 **Reference implementation, not a dependency.** PyTorch code for *"Variational Item Response Theory: Fast, Accurate and Expressive"* — the method `py-irt` productised. Shelve as the **method citation** for a defensibility annex |
| 🆕 [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy) | 🟢 **MIT** | `master/LICENSE` · 1,068 B | 🟡 PyPI `MIT` | 🔵 **Breadth reference: MIRT, GRM, CAT, CDM, FA and SEM in one package.** 🔴 **Effectively abandoned: v0.1.5, last upload 2016-04-04 (10 years).** Read it for **algorithm coverage**, do not ship it |

### 🔴 `P486` — a permissive repo payload does not license a vendored proprietary UI

🆕 [`hicsail/opencat-pro`](https://github.com/hicsail/opencat-pro) (**BYO-CAT**, Boston University SAIL)
probes clean: 🟢 **MIT**, `master/LICENSE`, **1,106 B**. 🔴 **And it is not usable as it stands.** Its own
`README.md` says so twice:

> *line 6:* *"The platform uses **Accessible+** to provide section 508 compliant user interface. Please
> **purchase a license** … if you wish to use BYO-CAT for development."*
> *line 176:* *"The UI framework is based on **Accessible+**. **A valid license is required to use this
> in production.**"*

🔴 **So the MIT grant covers the authors' code and not the interface the product ships.** A
filename-and-payload probe returns `LICENSED · MIT · OK` and is **right about the repository and wrong
about the deliverable**.

🟢 **This instrument already names the class as a known limit and this is its first measured education
instance.** `compose/code/p473-probe-commercial-gate/README.md` → *"Monorepo and open-core carve-outs
are not detected. A repo-level permissive payload can coexist with a proprietary `ee/` subtree."*
🔵 **The carve-out here is not a subtree — it is a purchased third-party asset named only in prose**,
which no path-aware read of the tree would catch either.

🔵 **The rule this yields is `P486`, and it is **defined once**, in `verticals/solutions.md` — the shelf it governs, since it is a statement about **platform** rows.** 🔴 **Cited here, not redefined: a duplicate definition makes every prior citation of the number ambiguous retroactively (`P481`).**

### 🟢 What the tier does to the in-tree / side-car decision

| Need | In-tree, permissive | Licence |
|---|---|---|
| Fit item parameters (1PL/2PL/4PL), maintained | 🟢 `nd-ball/py-irt` **or** `joakimwallmark/irtorch` | MIT |
| Adaptive item selection + simulation | 🟢 `douglasrizzo/catsim` | BSD-3-Clause |
| Synthetic response data for fixtures | 🟢 `eribean/girth` | MIT (stale) |
| CAT with file-level copyleft tolerated | 🟡 `condecon/adaptivetesting` | MPL-2.0 |
| 🔴 A ready-made CAT **web platform** | 🔴 **still none that is cleanly usable** | `opencat-pro` is MIT **+ paid UI** (`P486`) |

🟢 **The chain Gap 39 asked for is now permissive end to end**, and every link was re-read from payload
this pass:

| Link | Repo | Licence (payload) | Bytes |
|---|---|---|---|
| Write N parametric item variants | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · `main/LICENSE.md` | 1,072 |
| Deliver them (QTI 3) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · `main/LICENSE` | 1,076 |
| Calibrate difficulty / prove equivalence | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · `master/LICENSE` | 1,121 |
| Select adaptively from the calibrated bank | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · `main/LICENSE` | 1,514 |

🔵 **See `P491` in `compose/patterns.md` for the wiring.** 🟢 **MIT · MIT · MIT · BSD-3 — no copyleft
anywhere in the chain**, which is what makes it a product component rather than a side-car.

### ⚠️ Gaps this pass searched for and did **not** close — stated so silence is not read as coverage

| Gap | Searched | Result |
|---|---|---|
| 🔴 **A permissive CAT *web platform*** | `opencat-pro`, `EduCAT`, CAT platform searches | 🔴 **Open.** The only candidate carries a paid UI (`P486`) |
| 🔴 **Psychometric equivalence *between generated variants*** | the second half of Gap 39 | 🔴 **Still open, and still unmeasured.** This pass supplies the **calibration** library; nobody has published the **equivalence study** for an LLM-generated variant family on this stack |
| ⚠️ **An `R`-tier row (`philchalmers/mirt`)** | — | ⚠️ **Not probed this pass.** 🔵 `MIRT` appears 4× in the corpus but only as an **algorithm name inside `EduCDM`'s description** — the R package itself is unshelved. Stated as unprobed, not as absent |
| 🔴 **LLM item-generation agents with a real slug** | `ExamEow`, `S.E.S.`, `ExamGen` surfaced in prose | 🔴 **Unresolved — no owner slug recoverable for any of the three.** Recorded as leads, not findings |

## 🟢 Thirty-seventh pass, 2026-10-07 — the copyleft tier measured correctly for the first time, and the Java tier gets a second channel

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07** (16 filenames
× `main`/`master`), each verdict **anchored to the payload's title block** rather than to body tokens
(**`P171`**; the new-instrument fixture gap that let it recur is **`P480`**, written up in
`agents/top.md`). **No star counts** — see `P479` for why the stated reason
has been wrong for 36 passes.

### 🔴 Why this file needed a copyleft pass at all

🔵 **These shelves are overwhelmingly copyleft one tier down, and that tier had never been
payload-measured as a group.** `P171`'s third reopening is what forced the question: a bare-word NonCommercial test
reported **GPL-3.0 and AGPL-3.0 payloads as commercially prohibited**, because **§6 of both contains
*"allowed only occasionally and `noncommercially`"***. 🔴 **If the shelf's dominant family can be
silently mis-barred by the instrument, then the family's rows need to carry their own measured
evidence**, not an inherited label.

| Repo | 🟢 Licence (payload → title block) | Bytes · path | Why it is a foundation |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **GPL-3.0** — *"GNU GENERAL PUBLIC LICENSE Version 3"* | **35,146 B** · `main/COPYING.txt` | 🔵 **The reference every other LMS is measured against**, PHP, continuous since 2002, deepest plugin catalogue in the category. 🔴 **GPL-3.0: an AI deliverable is a *plugin* or an out-of-process service, never a fork you keep closed.** ⚠️ **Licence is at `COPYING.txt`, not `LICENSE`** — a probe that omits `COPYING*` reads the world's most deployed LMS as ungranted |
| [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | **10,982 B** · `master/LICENSE` | 🟢 **Re-confirmed independently this pass.** Still the **permissive full-LMS foundation** (pass 35, `P467` withdrawn) — Zurich-stewarded, Java. 🟢 **EMEA.** 🔵 **The only row in this tier where "extend it in-product" needs no licence conversation** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** — *"Educational Community License, Version 2.0"* | **11,340 B** · `develop/LICENSE` | Lecture capture, processing and delivery. 🟢 **Shelf slug confirmed correct**: `apereo/opencast` resolves nothing on any branch or filename; `opencast/opencast` resolves on **`develop` and `master`**. 🔵 **This file already recorded that correction at `:1123` — the probe reproduced it rather than finding it** |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟢 **GPL-2.0** | **15,214 B** · `master/LICENSE` | SIS / school ERP: students, grades, scheduling, attendance, billing, discipline, food service, **Moodle LMS integration in-tree**. 🔴 **GPL-2.0 — the strictest row in the SIS tier**; side-car only |
| [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟢 **LGPL** | **8,240 B** · `master/LICENSE` | Odoo-based education ERP — admissions, students, faculty, courses, **plus LMS delivery**, which most free SIS platforms omit. 🔵 **LGPL is the softest copyleft in this tier**: linking a separate AI service is clean, modifying the library is not |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | **1,096 B** · `master/LICENSE` | 🟢 **The permissive offline-first row.** Designed for low-connectivity and low-resource deployment — 🔵 **the only foundation here whose architecture already assumes the constraint that defines LATAM, EMEA-Africa and rural APAC engagements**, and it is **MIT**, so it can be extended in-product without a licence conversation |

### 🆕 The Java LMS tier finally has a second channel — `repo.maven.apache.org` is reachable

🔴 **Every prior pass cross-checked licences through PyPI or npm, which left the Java tier — Sakai,
OpenOLAT, Opencast, Kuali — on a single channel.** Measured this pass:

| Channel | Result |
|---|---|
| 🆕 `repo.maven.apache.org/maven2/org/sakaiproject/` | 🟢 **200** |
| 🆕 `repo.maven.apache.org/maven2/org/olat/` | 🟢 **200** |
| `search.maven.org/solrsearch/select` | 🔴 **403** — the Solr API is blocked |

🔵 **So the route exists but it is *browse by groupId path*, not search.** A POM's `<licenses>` block is
a **manifest-layer** declaration (`p289`, `p294`), which makes it a genuine independent channel for the
tier that has had none. ⚠️ **Not yet exercised on a POM payload this pass — recorded as a measured,
open route, not as a completed cross-check.** Next pass should close it on `OpenOLAT` and `Sakai`.

### 🔵 What the licence spread actually means for a delivery decision

| Tier | Permissive option | Reality |
|---|---|---|
| **LMS** | 🟢 **`OpenOLAT`** (Apache-2.0) | the rest — Moodle GPL-3.0, Canvas AGPL-3.0, Open edX AGPL-3.0, Sakai ECL-2.0 — is copyleft or patent-narrowed |
| **SIS** | 🟢 **`rubelw/OSSS`** (Apache-2.0, ⚠️ workflow logic unfinished) | openSIS GPL · RosarioSIS GPL-2.0 · OpenEduCat LGPL |
| **Offline / low-resource** | 🟢 **`Kolibri`** (MIT) | 🔵 **no copyleft competitor at all in this niche on these shelves** |

🔴 **The pattern is consistent and it is the single most useful sentence this file can give an
engagement: in open source education there is usually exactly *one* permissive option per tier, and
every other option is copyleft.** 🔵 **So the licence choice is not a preference, it is a selection of
one — and if that one is immature (`OSSS`) the honest answer is a side-car, not a fork.**

## 🟢 Thirty-sixth pass, 2026-10-07 — the permissive in-tree option reaches the SIS tier

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07** (16 filenames
× `main`/`master`), **re-classified through `compose/code/lib/license_family.sh`** and cross-checked
against the registry each project publishes. No star counts: `api.github.com` **403**, `github.com`
**403**. Cumulative channel census in `agents/top.md` — 🆕 **`registry.npmjs.org` is newly measured
reachable (200)** and is the second-channel route for the JS/PHP tier.

### 🟢 The structural find: the SIS tier now has an Apache-2.0 member

Pass 35 withdrew `P467` and promoted `OpenOLAT` (Apache-2.0, Zurich) as **the permissive full-LMS
foundation this KB had all along**. 🔵 **That left the parallel question open one tier down, and this
shelf never asked it: the LMS tier had an in-tree option, but did the *SIS* tier?** Every student
information system on these shelves is copyleft — **openSIS GPL, RosarioSIS GPL-2.0, OpenEduCat
LGPL-3.0** — so every engagement touching enrolment, attendance, grades or fees has been a side-car by
default.

| Repo | Licence (payload → shared classifier) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| 🆕 [`rubelw/OSSS`](https://github.com/rubelw/OSSS) | 🟢 **Apache-2.0** — `main/LICENSE`, **11,363 B** → `Apache-2.0`, commercial use **OK** | 🟢 **Three channels.** `pyproject.toml` → `license = { text = "Apache-2.0" }`; **PyPI `open-schools`** → `License :: OSI Approved :: Apache Software License`, with `repository` resolving back to this repo (identity confirmed, not just licence) | Python (FastAPI) + TypeScript (Next.js) | 🟢 **The first Apache-2.0 student information system on these shelves — the SIS counterpart to what `OpenOLAT` is for the LMS tier.** FastAPI + **Keycloak SSO** + SQLAlchemy + PostgreSQL; modules for governance, student info, accounting, activities and transportation. 🔵 **And the agent tier is inside the tree, not bolted on**: `Ollama + MetaGPT + A2A` are named in the stated architecture, so an AI deliverable extends the SIS **as a module** rather than integrating with it across a boundary. 🟢 **Region: North America**, placed on its **data model** — districts as top-level tenant, district transportation, district accounting, board governance (`P474`) |

⚠️ **The maturity caveat is load-bearing and belongs in any deck that names this repo.** The README opens
with a self-declared warning — *"OSSS is still being developed"* — and records, dated **7 Nov 2026**,
that the **state machine and workflow/gate logic are still being built**. 🔴 **For a system whose whole
job is enrolment and grade workflows, that is the core, not the periphery.** Shelve it as the
**pilot-tier permissive SIS and the architecture to study**, not as a production migration target. 🔵 **A
foundation can be the right *reference* while being the wrong *dependency*, and this shelf should say
which it means.**

### 🟢 Also added — two foundations that are corpora as much as code

| Repo | Licence | Region | Why it is a foundation |
|---|---|---|---|
| 🆕 [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | 🟢 **MIT** (`main/LICENSE`, **1,065 B** → `MIT` / **OK**), © Fab Data | 🟢 **EMEA** | 🟢 **A national curriculum as structured data.** Sierra Leone **MBSSE** Maths and Language Arts lesson plans — all grades, Primary + JSS + SSS — parsed from PDF into JSON and LLM-cleaned. **Ships the corpus** (raw, parsed, cleaned `.json.gz`), so it is a *dataset* foundation and not only a parser. 🔵 **Rule-based parsing with LLMs confined to the cleaning step** — the auditable division of labour, and the reason the output is trustworthy enough to build on |
| 🆕 [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT** (`main/LICENSE.md`, **1,067 B** → `MIT` / **OK**) | 🟢 **LATAM** | 🟢 **The measurement foundation for Portuguese-language delivery.** EleutherAI harness fork adapted to Portuguese; the evaluation suite behind the **Open Portuguese LLM Leaderboard**, backed by **CEIA, Federal University of Goiás (UFG), Brazil**. **Direct-response** evaluation (not log-probs only) so instruction-tuned chat models are measurable at all; automatic chat-template detection; **vLLM** and **LiteLLM** backends so local and API models are compared on one harness; F1-macro and Pearson aligned to each benchmark's own metric. 🔵 **This is the foundation that turns "which model for Brazil?" from a vendor conversation into a measurement** |

### 🔵 What this does to the in-tree / side-car table

| Tier | Permissive, in-tree option | Copyleft members forcing a side-car |
|---|---|---|
| **Full LMS** | 🟢 `OpenOLAT` (Apache-2.0, EMEA) · `Eloom LMS` (MIT, unplaced) | Moodle GPL-3.0+, Open edX AGPL-3.0, Chamilo GPL-3.0, ILIAS GPL |
| **Assessment delivery** | 🟢 `qtiworks` (BSD-3-Clause, EMEA) | — |
| 🆕 **SIS / school ERP** | 🟡 `OSSS` (Apache-2.0, NA) — **pilot-tier only** | openSIS GPL, RosarioSIS GPL-2.0, OpenEduCat LGPL-3.0 |
| **Offline-first** | 🟢 `Kolibri` (MIT) | — |
| **Evaluation** | 🟢 `AITutor-EvalKit` (MIT) · 🆕 `lm-evaluation-harness-pt` (MIT, LATAM) | — |
| **Curriculum corpora** | 🆕 `lesson-plan-parse-mbsse` (MIT, EMEA) | 🔴 **and this is the tier where `CC BY-NC` appears — see `P473`** |

🔴 **One standing caution this shelf must now carry, because it did not before.** The three tiers above
that hold **content** rather than code — curriculum corpora, item banks, courseware — are where
**NonCommercial** licences live. `CRSS-AI/agentic-se-course-early-2026` was probed this pass and is
**`CC-BY-NC-4.0`, commercial use prohibited**; a filename-based probe called it `GRANTED` (`P473`).
🟢 **Every content-tier row on this shelf must carry `P250`'s commercial-use column explicitly**, because
for content, unlike for code, a permissive-looking licence file is genuinely often not a permissive
grant.

### ⚠️ Gaps this pass searched for and did not close — stated so silence is not mistaken for coverage

- 🔴 **Mexico.** Searched explicitly (`open source education AI project Brazil Mexico Latin America
  github 2026`). **No Mexico-origin permissive education asset surfaced.** LATAM representation on these
  shelves remains **Brazil and Chile** (`lm-evaluation-harness-pt` UFG; `Latam-GPT`/CENIA recorded
  earlier). ⚠️ **Scope: this is a statement about what these queries reached, not about Mexico.**
- 🔴 **A permissive, production-maturity SIS.** `OSSS` is Apache-2.0 **and self-declared incomplete on
  exactly the workflow logic a SIS exists for.** The gap is **maturity**, not licence, and it is a
  different gap from the one pass 35 withdrew.
- 🔴 **`AI-for-Education/fabdata-llm-retrieval`** — an end-to-end RAG platform from an organisation whose
  **other seven repositories this KB already shelves**, and it serves **no licence payload**. 🔵 Worth a
  direct enquiry: this is the single highest-value ungranted repo on these shelves, and the fix is an
  email, not a search.

## 🔴 Thirty-fifth pass, 2026-10-07 — the EMEA gap this shelf declared for three passes is withdrawn

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, branch-
and case-aware (12–19 filenames × `main` and `master`), **cross-checked against the registry or
build descriptor each project publishes** where one exists. No star counts: `api.github.com` **403**,
`github.com` **403**, and the GitHub MCP route an earlier pass used is outside this session's
repository scope. Cumulative channel census in `agents/top.md`.

### 🔴 `P467` is WITHDRAWN. The EMEA permissive gap was a property of this shelf, not of the industry

> **Superseded text:** *"no EMEA-origin permissive education foundation."* Asserted here for three
> consecutive passes. 🔴 **It is false.** Two EMEA-origin, permissive, education-specific assets were
> already recorded elsewhere in this KB while this shelf denied their existence. Both were re-read
> from payload on 2026-10-07 and are **promoted onto this shelf below**. Root cause and the
> transferable rule: **`P469`** in `agents/top.md`. 🔴 **And the gate that should have caught this
> already existed and passed 27/27 while judging nothing — its filters are Spanish-only and this
> claim was written in English (`P471`).** Instrument: `compose/code/p471-gap-gate-language/`
> (**16/16**). Recipe: **`P45`** in `compose/patterns.md`.

🔵 **What survives from `P467`, unchanged and still valuable:** nine European and public-sector forges
(`code.europa.eu`, `gitlab.opencode.de`, `codeberg.org`, `framagit.org`, `git.fsfe.org`,
`forge.apps.education.fr`, `invent.kde.org`, `salsa.debian.org`, `joinup.ec.europa.eu`) return
**000** from this environment, re-confirmed this pass for `codeberg.org` and `joinup`. **The EUPL
tier really is invisible here.** 🔴 **What does not survive is the inference that was hung on it.**
Unreachable forges mean *this instrument is partially blind to EU public-sector code*; they never
meant *no permissive EMEA education asset exists*. The second claim was refutable by `grep` against
this KB's own shelves, and nobody ran it.

### 🟢 Foundations added this pass — the two that disprove the withdrawn claim

| Repo | Licence (payload) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`master/LICENSE`, **10,982 B**, verbatim Apache-2.0 preamble) | 🟢 `master/pom.xml` `<licenses>` → `Apache 2.0 Open Source L6icense` pointing at `apache.org/licenses/LICENSE-2.0`; 🟢 **second forge** `gitlab.com/olatorg/OpenOLAT` (payload Apache-2.0, 10,982 B) | Java | 🟢 **The permissive full-LMS foundation this KB has had all along and never shelved here.** Teaching, learning, **assessment**, curriculum management, QTI, SCORM, communication; modular course-authoring toolkit; architecture stated for low resource consumption and scalability. 🔴 **Origin: Switzerland** — OLAT began at the **University of Zurich**, now maintained by **frentix GmbH**. 🔵 **Licence consequence, and it is the big one: this is the only complete LMS on these shelves that an engagement can extend *inside the tree* without the copyleft conversation.** Moodle is GPL-3.0-or-later, Open edX AGPL-3.0, Chamilo GPL-3.0, ILIAS GPL, OpenEduCat LGPL-3.0 — all of which force the side-car architecture. **Apache-2.0 removes that constraint.** 🔴 **Branch is `master`** — a `main`-only probe reports it ungranted. |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (`master/LICENSE.txt`, **2,058 B** — *"distributed under the 3-clause BSD license… This license is famously liberal"*) | — not published to a registry | Java | 🟢 **A permissive, standards-based assessment-delivery foundation, EMEA-origin.** Three components: the **QTIWorks Engine** (QTI 2.1 delivery + rendering), **JQTI+** (Java library to read, write, model and manipulate QTI 2.1 items and tests), and the **MathAssess extensions** for advanced mathematical assessment. From the **University of Edinburgh**. 🔵 **This is the piece that makes assessment migration tractable**: QTI 2.1 in, QTI 2.1 out, with a permissive library for programmatic item manipulation — so item banks can be transformed without a vendor. 🔴 **`master`-only.** ⚠️ The licence text itself *urges* contributing back; **that is an exhortation in the preamble, not a condition** — the operative grant is plain BSD-3-Clause. |

### 🟢 Third permissive platform row — and the platform channel was not saturated after all

| Repo | Licence (payload) | Cross-channel | Why it is here |
|---|---|---|---|
| [`eloompty/Eloom-LMS-International`](https://github.com/eloompty/Eloom-LMS-International) | 🟢 **MIT** (`main/LICENSE`, **1,062 B**) | 🟢 `README` MIT badge agrees; 🔴 **not on Packagist** — so this row is **payload + badge**, not payload + registry, and says so | 🆕 Laravel **13**, PHP **8.3+**, **42 `nwidart/laravel-modules` modules all enabled by default**, **five web portals over a single codebase**, token-authenticated REST API for mobile clients, Laravel Reverb + standalone Socket.IO for realtime. Covers the vocational/HE lifecycle end to end: agent-sourced application → offer letter → enrolment → intake scheduling → attendance → **assessment** → fees → certificates → alumni. 🟢 **MIT, which makes it the most permissive full LMS on these shelves.** ⚠️ **Region not determinable** — the `README` names no country, governing body or qualifications authority. **Recorded as unplaced rather than guessed**, per this KB's closed-vocabulary rule. |

🔴 **Prior passes recorded the platform channel as "saturated, verified by grep"** (`repos/trending.md:1597`,
`:3751`). 🔵 **Two permissive platform rows arrived this pass through that same channel.** The grep
was over *this KB's contents*, which proves the shelf had those names — it was never evidence that
the world had no others. **`P469` is the same error in a second place.**

### 🔴 `P470` — Forma LMS: a confidently published Apache-2.0 claim that no channel here confirms

Secondary sources this pass name **Forma LMS** (Italian fork of Docebo, pre-commercialisation) as
**Apache-2.0**, and recommend it *specifically* for teams needing permissive licensing.
[`formalms/formalms`](https://github.com/formalms/formalms) **exists** (`master/README.md` → 200) and:

| Channel | Result |
|---|---|
| Payload — 19 licence filenames × `main` + `master` (incl. `LICENSE.TXT`, `gpl.txt`, `COPYING.txt`) | 🔴 **nothing** |
| `packagist.org/packages/formalms/formalms.json` | 🔴 **404** |
| `master/composer.json` | 🔴 **absent / unparseable** |

⚠️ **Recorded as `licence unverified`. It is NOT shelved as a permissive foundation.** 🔵 **This is a
sharper failure than a missing licence**: the claim is *specific*, *permissive* and *published as the
reason to adopt*. A dependency manifest that trusted the article would have carried an unverifiable
permissive assertion about a **platform tier** — the tier where a licence error is most expensive,
because it decides in-tree versus side-car. 🔵 **The rule: a licence is a document you read, not a
recommendation you inherit.**

### 🟢 Registry re-reads this pass — 2 rows, 0 disagreements

`canvasapi` → **MIT** free-text **+ OSI MIT classifier** · `kolibri` → **MIT** + **OSI MIT
classifier**. Both agree with the payload rows already on this shelf.

### 🆕 Instrument: the Rust registry is closed

| Stack | Endpoint | Pass-35 reachability | Consequence |
|---|---|---|---|
| Rust | `crates.io/api/v1/crates/{crate}` | 🔴 **403** — 🆕 **first measured this pass** | [`raif-s-naffah/xapi-rs`](https://github.com/raif-s-naffah/xapi-rs) and every future Rust row stay **payload-only**. 🔵 Recorded so no later pass counts Rust among the available second channels — the registry tier is **Python, Node, PHP and JVM, not five stacks** |
| JVM | `repo1.maven.org/maven2` | 🟢 **200** | 🔵 **No longer idle in effect**: OpenOLAT's licence was cross-checked against its `pom.xml` `<licenses>` block via `raw` — the same declaration Maven Central serves. The JVM tier now has a worked precedent |

## 🟢 Thirty-fourth pass, 2026-10-07 — the Canvas client was missing, and the EMEA gap gets its reach restated

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, branch-
and case-aware (13 filenames × `main` and `master`), **cross-checked against the registry each
project publishes to** where one exists. No star counts: `api.github.com` **403**, and the GitHub MCP
route an earlier pass used is **outside this session's repository scope** (see `agents/top.md`).
Consolidated 20-channel census in `agents/top.md`; `P465` records why it needed consolidating.

### 🟢 Foundations added this pass

| Repo | Licence (payload) | Cross-channel | Language | Why it is a foundation |
|---|---|---|---|---|
| [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **MIT** (`master/LICENSE`, 1,130 B) | 🟢 PyPI `canvasapi` → `MIT License` + **OSI MIT classifier** | Python | 🔴 **A real gap, and an awkward one: this KB carries six Canvas MCP servers and never carried the Canvas REST client they all sit on.** A maintained, MIT, object-oriented Python wrapper over the Canvas LMS API — courses, enrolments, assignments, submissions, **gradebook writes**, quizzes, LTI. From **UCF Open** (University of Central Florida), the same group as `UDOIT`, `Materia`, `Obojobo` and this shelf's `cookiecutter-python-lti`, all already here. 🔵 **Canvas itself is AGPL-3.0 and this client is MIT** — the client talks HTTP from outside the tree, so the deliverable inherits nothing. **Sixth independent instance of this KB's platform-copyleft / integration-permissive rule.** 🔴 **Branch is `master`** — a `main`-only probe reports it ungranted. |
| [`soumics/llm-rag-assistant`](https://github.com/soumics/llm-rag-assistant) | 🟢 **MIT** (`main/LICENSE`, 1,070 B) | — not published to any registry | Python | The retrieval / embedding / **citation-checking** core reused by the MIT `soumics/adaptive-ai-tutor` (`agents/top.md`). Local-first: embeddings and generation served by **Ollama**, `faiss-cpu` index, and **citation verification as a first-class component rather than a prompt instruction**. 🔵 **Citation checking is the piece most tutor prototypes skip and the first thing an education client asks about.** ⚠️ **`P466`** — distributed only as a pinned GitHub archive zip, **403** from this environment. |
| `edx-opaque-keys` (PyPI) | 🟡 **`AGPL-3.0-only`** (registry declaration) | — | Python | 🆕 **Not previously recorded in this KB.** A core Open edX key/identifier library, and **network copyleft**. Recorded because it extends the Open edX licence asymmetry by one brick: the platform tier is AGPL **including its small utility libraries**, so "it's just a helper package" is not a route out of the copyleft. |

### 🟡 `P467` — the EMEA gap: still a gap, with its reach now stated in full

This shelf has declared for three consecutive passes that it can find **no EMEA-origin permissive
education foundation**. This KB already records that the European Commission's **Joinup/OSOR**
catalogue and **Codeberg** are unreachable from this environment. This pass re-measured that and
**extended it with three forges never named here before**:

| European / public-sector forge | HEAD | GET | Previously recorded here? |
|---|---|---|---|
| `code.europa.eu` — the European Commission's own GitLab | **000** | **000** | yes |
| `gitlab.opencode.de` — German federal/state public-sector forge | **000** | **000** | yes |
| `codeberg.org` — EU-hosted, the main non-US community forge | **000** | **000** | yes |
| `framagit.org`, `git.fsfe.org` | **000** | **000** | yes |
| 🆕 `forge.apps.education.fr` — **French Ministry of Education** | **000** | **000** | 🆕 **no — first measured this pass** |
| 🆕 `invent.kde.org`, `salsa.debian.org` | **000** | **000** | 🆕 **no — first measured this pass** |

🔴 **Nine European and public-sector forges unreachable, against `raw.githubusercontent.com` 200 and
`gitlab.com` 200.** The EUPL tier this KB made machine-readable in pass 28 is, by construction, the
tier most likely to live where this instrument cannot look: **EUPL is the European Commission's own
licence, and the Commission publishes to `code.europa.eu`.**

⚠️ **This does not convert the gap into coverage. It is still a gap and it is now three passes old.**
What it fixes is the *wording*. The defensible sentence is: **"no EMEA-origin permissive education
foundation was found through the forges this environment can reach, and nine forges where EU
public-sector code is most likely to live returned 000."** 🔵 **Consequence: never quote this KB's
thin EMEA shelf to a client as market evidence.** It is partly an artefact of the collection
instrument. Ask the client's own procurement which national forge they publish to.

🟢 **One EMEA-origin asset did arrive this pass through a reachable channel** —
[`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment), **GPL-3.0**,
Netherlands (full row in `agents/top.md`). Copyleft, so it does not fill the *permissive* EMEA gap;
it is the first EMEA-origin higher-education assessment framework on any shelf here.

### 🟢 The registry tier by language — re-consolidated after `P465`

Earlier passes used these registries and proved they discriminate; the pass-33 census dropped them.
Restated here as one table so the next pass inherits the instrument rather than re-deriving it:

| Stack | Registry endpoint | Reachability | Read this pass | Education relevance |
|---|---|---|---|---|
| Python | `pypi.org/pypi/{pkg}/json` | 🟢 **200** | `kolibri` MIT · `xblock` Apache-2.0 · `openedx-learning` AGPL-3.0 · `edx-proctoring` AGPL-3.0 · 🆕 `edx-opaque-keys` **AGPL-3.0-only** · `nbgrader` BSD · `otter-grader` BSD-3-Clause · 🆕 `canvasapi` MIT · `pylti1p3` MIT · `frappe` MIT | Open edX, Jupyter-grading, Kolibri tiers |
| Node / TS | `registry.npmjs.org/{pkg}` | 🟢 **200** | `ltijs` **Apache-2.0, v7.0.7** · `@promptster/rubric` MIT | LTI tool-provider tier |
| PHP | `packagist.org/packages/{v}.json` | 🟢 **200** | `moodle/moodle` → **`GPL-3.0-or-later`** | **The Moodle tier — the largest installed base in this industry** |
| JVM | `repo1.maven.org/maven2` | 🟢 **200** | 🔴 **nothing — still unused** | Sakai, OpenOLAT, Opencast, all payload-verified only |

⚠️ **`P468` — the registry tier has a measured miss rate and never overrules payload.** `crewai`
publishes with **no licence metadata whatsoever**; `chamilo/chamilo-lms` is **404 on Packagist**
despite being a major PHP LMS on this shelf; **8 of 20** PyPI rows gave only free text with no OSI
classifier. 🔵 **Where both channels answer and agree, the row is as well-evidenced as this KB can
make it. Where only one answers, the row must say which one** — rather than reading as doubly
verified.

### 🟢 Substrate re-verification — twelve rows, second source, no movement

No new rows. Recorded because pass 32's T1 is that a licence claim decays, and this is the cheapest
way to re-check one:

| Package | Registry declaration | Note |
|---|---|---|
| `faster-whisper` | **MIT** + OSI classifier | the practical ASR choice for a local tutor |
| `openai-whisper` | **MIT** | reference implementation |
| `coqui-tts` | **MPL-2.0** + OSI classifier | 🟡 **weak copyleft, file-level.** Linking is fine; a quietly patched fork is not. |
| `sentence-transformers` | **Apache-2.0** | embeddings |
| `qdrant-client`, `chromadb` | **Apache-2.0** | vector stores |
| `vllm` | **Apache-2.0** | self-hosted inference — the sovereignty tier |
| `litellm` | **MIT** | provider abstraction |
| `docling` | **MIT** | 🔵 document → structured text; the curriculum-ingestion front door (`P2`) |
| `marker-pdf` | **Apache-2.0** | PDF → Markdown |
| `unstructured` | **Apache-2.0** | mixed-format ingestion |
| `librosa` | **ISC** | audio features — oral-fluency work |
| `mediapipe`, `opencv-python` | **Apache-2.0** both | on-device vision — the local proctoring tier |

🔵 **All twelve permissive or weak-copyleft, none a surprise.** A re-check is supposed to be boring;
when it is not, you have found something.

## 🟢 Thirty-third pass, 2026-10-07 — the regional-corpus layer, and a gap repo that was licensed all along

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07**, with a
branch- and case-aware prober (13 filenames × `main` and `master`). No star counts:
`api.github.com` **403**, github.com landing pages **403** on both HEAD and GET. 🆕 Two further
channels measured and **closed this pass**: `eur-lex.europa.eu` **000**, `huggingface.co` **000**.

### Foundations added this pass

| Repo | Licence (payload) | Region | Role |
|---|---|---|---|
| [`latam-gpt/anonymization-filter`](https://github.com/latam-gpt/anonymization-filter) | 🟢 **MIT** (1072 B, © 2025 GonzaloFuentes1) | LATAM | PII anonymisation filter from the **Latam-GPT** corpus pipeline. 🟢 **The regional primitive this shelf was missing:** a Spanish/Portuguese-language scrubber that sits *in front of* any model, which is what makes a student-data pipeline defensible under LATAM data-protection regimes and under CA A.B. 1159-style rules in North America |
| [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) | 🟢 **MIT** (1067 B, © 2020 **EleutherAI**) | LATAM | Regional evaluation entry point. ⚠️ **A fork** — the grant is EleutherAI's, so treat it as a regionally-configured upstream and cite accordingly |
| [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) | 🟢 **MIT-0** — *MIT No Attribution* (903 B, © 2025 Tim Duffy) | LATAM | Sycophancy benchmark. ⚠️ **MIT-0 is a distinct licence from MIT**: it waives attribution. Harmless here, but it must not be recorded as "MIT" in a licence inventory |
| [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | 🟢 **MIT** (1068 B, `master/LICENSE`, © 2026 Prem Biswal) | Global | 🔴 **Previously filed on this shelf's reject list.** Belongs in foundations as much as in agents: it is a **from-scratch, dependency-light reference implementation** of explainable behavioural risk scoring — logistic regression, anomaly detection, risk decay and fusion written out rather than imported. Read it as the maths layer under any assessment-integrity build |

🔵 **Why the anonymisation filter is the important one.** The other two LATAM rows are evaluation
tooling with upstream holders. This one is **original regional work** on the problem every education
engagement in the region hits first: student data cannot leave the institution un-scrubbed, and
English-trained PII detectors under-perform on Spanish and Portuguese names, document identifiers and
address forms. 🟢 **It composes directly with the local-first grading stack** already on this shelf —
scrub, then score on the client's own hardware, and no student text reaches a frontier API.

### ⚠️ What this pass could NOT establish, and will not imply

🔴 **The model layer of this industry is unverifiable from this environment.** `huggingface.co`
returns **000** (egress-blocked), so **no weights licence anywhere in this KB is payload-verified** —
including **Latam-GPT's** 70B SFT checkpoint, widely reported under the **Llama 3.1 Community
Licence**. That licence is **not OSI-approved** and carries acceptable-use and naming conditions.
**Treat every weights-licence statement in this KB as a secondary-source claim** (`P464`).

🔵 **The practical consequence for foundations work:** prefer compositions where the permissively
licensed *code* is yours to vendor and the *weights* are a swappable, client-chosen dependency. Every
pattern on the `compose/` shelf that names an open-weights model is one Hugging Face terms change
away from needing a re-read, and this pass cannot do that re-read.

### 🟢 The Open edX licence picture, extended to proctoring

The pass-32 split (AGPL-3.0 core, Apache-2.0 `XBlock`) now has a third measured layer:

| Layer | Repo | Licence (payload) | Bytes | Consequence |
|---|---|---|---|---|
| Core platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** | 35136 | self-host freely; redistribution of a modified platform is a licence event |
| Extension point | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | 11357 (`master/LICENSE.TXT`) | the surface an agent plugs into, and may keep proprietary |
| Proctoring subsystem | [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🟡 **AGPL-3.0** | 35119 (`master/LICENSE.txt`) | 🆕 **the integrity layer is copyleft too** — so an integrity *agent* must sit outside it |

🟢 **Which is exactly what the two MIT proctoring agents added this pass do.** The permissive
proctoring work lives *outside* both AGPL-3.0 trees and communicates over APIs — the fifth
independent instance of the rule that **the licence boundary is the integration boundary**.

## 🟢 Thirty-second pass, 2026-10-07 — the Open edX licence asymmetry, stated precisely

**Licences read from each repo's own payload on `raw.githubusercontent.com`, 2026-10-07.** No star
counts: `api.github.com` **403**, github.com landing pages **403 on both HEAD and GET** — three
channels measured, three closed.

### 🔵 The one thing to know before quoting an Open edX engagement

This shelf has carried Open edX components for many passes without stating the licence split in one
place. Both halves were read from payload this pass:

| Layer | Repo | Licence (payload) | Bytes | What it means commercially |
|---|---|---|---|---|
| Core platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** | 35136 | Network copyleft. Fine to **self-host for a client**; a licence event if you redistribute a modified platform or expose it as a modified service you own |
| Extension point | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | 11357 (`master/LICENSE.TXT`) | Permissive. The surface an agent plugs into, and the surface you can keep proprietary |

🟢 **The architecture follows from the table, not from taste.** Build the agent **as an XBlock, or as
an external service talking to Open edX over its APIs**, and the AGPL stays confined to a platform
the client self-hosts. Fork `edx-platform` to embed the agent and you have taken on AGPL-3.0 for the
whole deliverable. [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia, added
to `agents/top.md` this pass) is a working instance of the permissive shape: an MIT tutor agent
living inside an Open edX deployment without touching the platform's licence.

⚠️ **This is the same in-tree vs side-car boundary** this KB recorded for `peancor/moodle-mcp-server`
(MIT, *because* it sits outside the GPL-3.0 Moodle tree) and for `Jawadh-Salih/moodle-mcp-server`
(MIT, added this pass). 🔵 **Three independent instances now: the licence boundary *is* the
integration boundary.** When the platform is copyleft and the agent must not be, the agent goes
outside the tree and talks over an API. That is not a workaround — it is the design.

### Foundations added this pass

| Repo | Licence (payload) | Region | Role |
|---|---|---|---|
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (11350 B) | Global | Intel's education reference stack: libraries, microservices and **benchmarking** tools over **OpenVINO**, targeting Intel CPU / iGPU / NPU. 🔵 **The only foundation on this shelf that answers "what hardware does this need?"** — the question that decides whether an on-prem school deployment is affordable |
| [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) | 🟢 **Apache-2.0** (10141 B) | Global | Rubric-conditioned evaluator with **open weights**. The piece that lets assessment scoring run on infrastructure the client controls, instead of posting student work to a frontier API |
| [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | 🟢 **MIT** (1076 B, © 2025 The LLM Data Company) | Global | Weighted rubrics as a **data structure**, provider-agnostic. Makes a grading decision reproducible and auditable after the fact — which is what a conformity assessment asks for |

🔵 **Why these three belong on the *foundations* shelf rather than with the agents.** None of them is
an education product. Each is a layer underneath one, and together they close the gap this shelf has
had all along: **an education deliverable that must not send student data to a third party now has a
complete permissive stack** — `education-ai-suite` for the accelerated local inference and the
hardware sizing, `prometheus-eval` for open-weight scoring, `rubric` for the auditable criteria.
That stack is the direct technical answer to EU AI Act Annex III and to the US state student-data
statutes catalogued in `intel/market.md` this pass.

### 🔴 Correction to this shelf's verification instrument — `P453`, `P454`, `P458`

**`openedx/XBlock` was returned `ABSENT` by this KB's own prober**, and it is a real repository,
correctly licensed Apache-2.0, already on this shelf. Three independent defects produced that one
false negative:

- **`P453`** — `raw.githubusercontent.com` paths are **case-sensitive**. Proven by negative control:
  `pykt-team/pykt-toolkit/main/LICENSE` **200**, `…/license` **404**, `…/LiCeNsE` **404**. XBlock's
  licence file is **`LICENSE.TXT`** — caps extension — which was not in the probe list.
- **`P454`** — the existence fallback probed only `README.md`. XBlock ships **`README.rst`**
  (200; `README.md` 404), so the fallback also reported it missing.
- **`P458`** — XBlock's **own README links a licence path that 404s**
  (`…/blob/master/LICENSE.txt`, lowercase extension). A verifier that follows the README's link
  concludes "licence missing" on a correctly licensed repo. `pyproject.toml` is the tiebreaker:
  `license = "Apache-2.0"`, `license-files = ["LICENSE.TXT"]`.

⚠️ **The direction of this error is the expensive one.** Every defect here turns a **true row into a
deletion**. This KB has spent many passes guarding against *over*-claiming a licence; `P453`/`P454`
are the first recorded defects that destroy correct rows instead, and they would do it silently,
reported as a 404. 🔵 **Any `ABSENT` verdict recorded in this KB before this pass should be
re-probed with the corrected name list before it is acted on** — in particular for `.rst`-documented
and Python-packaging repos, where both defects land together.

### 🟢 Re-reads this pass — two foundations re-confirmed from payload

| Repo | Payload | Verdict |
|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `master/LICENSE`, 11120 B | 🟢 **ECL-2.0**. Payload opens *"Educational Community License, Version 2.0 … consists of the Apache 2.0 license, modified…"* — corroborates pass 30's lineage reading **from the payload text itself**, and the row stays on the permissive allowlist |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `master/LICENSE`, 8241 B | 🟢 **LGPL-3.0**, genuinely LGPL. Payload: *"published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 … Since the LGPL is a set of additional permissions on top of the GPL…"*. **Independently corroborates pass 28's negative half** — the linking conversation for this component is real, and the linking exception is really there |

🔵 **The `openeducat` re-read is worth more than a tick.** Pass 28 corrected seven rows `LGPL → GPL-2.0`
and kept four as genuinely LGPL; that correction inverted a commercial answer, so the negative half
needed independent confirmation rather than trust. One of the four is now confirmed by a separate
run, with the payload's own words. The remaining three are **not** re-measured here.

### 🔴 Declared gap — EMEA foundations, second consecutive pass

Searched for EUPL / Apache / BSD education foundations of EMEA origin (Germany, France, Nordics,
EU public sector). **Nothing new found.** Institutional activity exists — Central European
University announced a GitHub collaboration in April 2026 on open AI teaching materials — but it
produced **no repository with a verified permissive grant** in this window. The EUPL public-sector
tier that pass 28 made machine-readable gained **zero rows** this pass. ⚠️ **This is an informed
gap, not coverage**, and it is now two passes old: EMEA is the region where this KB's shelf is
thinnest while being the region with the hardest compliance requirements (`intel/market.md`).

# Foundational Repos — Education

Infrastructure Globant can build an education solution *on top of*. These are not
education products; they are the permissively licensed layers underneath one.
Licenses read from each repo's own `LICENSE` payload on 2026-10-06.

## 🟢 Thirtieth pass, 2026-10-07 — the flagged rows on this shelf were not wrong, and the three that still need a second look

🔴 **Execution of this tree's suites was DENIED this pass** (`[Code from External]`), so no total in
this file is affirmed as measured today (`P107`), and pass 28's four pre-registered sweeps — including
the downstream propagation of the corrected `family_of` to `holder.tsv`, `homepage.tsv`, the `p250`
commercial sweep and the `p419` copyleft census — **did not run**. They carry forward. 🔴 **Reporting
them as "nothing moved" would be a fabricated negative.**

🟢 **What did get settled.** Pass 28's reconciler flagged **29 rows** across this KB as the corpus
contradicting itself on licence; **13 were adjudicated first-hand this pass and none is a
contradiction.** Three of the flagged rows are foundations on this shelf, and all three are fine:

| Row | Flagged because | Verdict |
|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | prose names **MIT** and **LGPL** | 🟢 **MIT.** The LGPL is two *dependencies*, and the prose already scoped it (`REVIEW-WEAK`, *"two LGPL deps"*) |
| [`opencast/opencast`](https://github.com/opencast/opencast) | prose names **ECL-2.0** and **Apache-2.0** | 🟢 **Both true.** ECL-2.0 *is* an Apache-2.0 derivative — the sentence is a lineage statement, and the row stays on the permissive allowlist |
| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | prose names **GPL** and **MPL-2.0** | 🟢 **MPL-2.0.** The "GPL" is the **`Was` column of pass 28's own correction table** on this shelf |

⚠️ **The useful warning for this file specifically: a correction table manufactures a false
contradiction.** This shelf publishes `Was → Is` rows every time a classifier is fixed, and an
instrument that reads cells without reading which column they are in will count every `Was` as a live
claim. Four of the 29 abstentions were created *by* pass 28 in the act of fixing five rows correctly.

⚠️ **Still genuinely open on this shelf, unchanged from pass 28 and not re-measured here:** the seven
`LGPL → GPL-2.0` rows below are components an engagement **links against**, and the GPL-2.0 has no
linking exception. That is the one correction in this area that changes a commercial answer, and it
stands.

## 🔴 Licence corrections — twenty-eighth pass, 2026-10-07

**Seven repositories on this shelf are `GPL-2.0` and were filed `LGPL`** (`P452`), and the
difference is the whole reason the LGPL exists: it grants a linking exception that the plain GPL
does not. All seven are components an engagement **links against** rather than forks, which is
exactly the case the exception covers.

| Repo | Was | 🔴 Is | Region | Role |
|---|---|---|---|---|
| [`OpenEMIS/core`](https://github.com/OpenEMIS/core) · [`openemis/core`](https://github.com/openemis/core) | LGPL | **GPL-2.0** | Global | ministry-scale education MIS — 🔴 **two rows, one repository**, a live case collision |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | LGPL | **GPL-2.0** | LATAM | Brazilian municipal school system |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | LGPL | **GPL-2.0** | EMEA | QTI assessment SDK |
| [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | LGPL-2.1 | **GPL-2.0** | EMEA | certified LTI 1.3 core — see the regression note below |
| [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) · [`yunger7/enem-api`](https://github.com/yunger7/enem-api) | LGPL | **GPL-2.0** | LATAM | Brazilian national exam data |

🟢 **The negative half: four rows are genuinely LGPL and did not move** —
[`Tampere/trevaka`](https://github.com/Tampere/trevaka) (2.1),
[`untisapi/untis4j`](https://github.com/untisapi/untis4j) (3.0),
[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (3.0),
[`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) (REUSE notice). For those, the
dynamic-linking conversation is real.

**The cause.** `family_of` probed LGPL before GPL over `text[:4000]`. The GNU licences name each
other inside their own texts, so the window decided the verdict: GPL-2.0's Preamble recommends the
LGPL at character **784** (inside the window), GPL-3.0's closing notes do so at **34,143**
(outside). Every GPL-2.0 payload came back LGPL; every GPL-3.0 payload came back right. Fixed by
resolving the GNU family from the payload's title region first.

🔵 **A free cross-check this corpus already had the data for: the byte size refutes the label.**
GPL-3.0 is ~35 kB, GPL-2.0 ~18 kB, LGPL-2.1 ~26.5 kB, LGPL-3.0 ~7.6 kB. This file published
`Citolab/qti-components` as *LGPL-3.0 (35,199 B payload)* and `oat-sa/lib-lti1p3-core` as
*LGPL-2.1 (18,091 B)* — both sizes contradict both labels, and no fetch was needed to see it.

### 🔴 The regression, which is the finding worth carrying

`oat-sa/lib-lti1p3-core` was not mis-stated by accident. The pre-reset archive carries **GPL-2.0**
for it in **nine** places, with payload size and fingerprint (`18.091 B`, `f9c375a1be4a`), once as a
deliberate, argued finding:

> *"🔴 **La excepción que rompe la simetría y hay que mirarla:** `oat-sa/lib-lti1p3-core` **es**
> librería de protocolo y aun así es **GPL-2.0**. La regla «librería ⇒ permisivo» no es ley: es
> correlación de 3 de 4. Se dice en vez de redondearla."*

After the 2026-10-06 reset it was rewritten as LGPL-2.1 — the answer the defective classifier gives
— and `intel/market.md` published EMEA architecture advice on it concluding *"neither is a
blocker."* Both the row and that paragraph are corrected this pass. **A correct human reading was
destroyed by an instrument, and the instrument was wrong.**

### 🟡 The EUPL tier, now machine-readable, and it is nine repositories

Nine rows moved `UNKNOWN → EUPL`: eight `Opetushallitus/*` Finnish national education services
(🆕 including [`valtionavustus`](https://github.com/Opetushallitus/valtionavustus), the ninth, which
pass 26's prose did not name) plus
[`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model).
🔵 The eight Finnish grants are **short reference notices (296–654 B), not the full licence text**.
⚠️ **EUPL Article 1's "Communication" covers network use**, so the EUPL binds a hosted service the
way AGPL does — the fact that matters for a managed service delivered to a European ministry.

## Core stack

15 rows, all verified on 2026-10-06. Four further infrastructure rows were added in
the third pass of the same day — see the section below.

| Repo | License (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | MIT (`LICENSE`) | model serving | Runs open-weight models on-prem or on a classroom server. This is the answer to EMEA data-residency and to LATAM connectivity/cost constraints — student data never leaves the institution. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT (`LICENSE`) | agent framework | Typed, validated agent outputs. When an assessment decision must be defensible, a schema-checked output beats free text. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT (`LICENSE`) | orchestration | Graph-structured, checkpointed agent state. The checkpoints double as the audit trail a high-risk education deployment needs. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | MIT (`LICENSE`, body text — no title line) | orchestration | Role-based multi-agent teams; maps cleanly onto tutor / assessor / reviewer separations. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — ⚠️ **now `OpenHands/OpenHands`**; both paths serve head `9f05599`, see the canonical-name table below | MIT (`LICENSE`) | coding agents | For the build itself and for CS-education use cases where students need a sandboxed coding agent. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | agent framework | Python + .NET. The right default for clients already on a Microsoft stack, and the successor path off AutoGen. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | agent framework | Smallest auditable surface of the frameworks here. |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Apache-2.0 (`LICENSE.md`) | document ingestion | Turns textbooks, PDFs and scanned curricula into structured text. This is the front door of every content-generation pipeline in `compose/patterns.md`. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause (`LICENSE`, modified-BSD body) | lab environment | Multi-user notebook serving for a cohort. The standard way to hand 200 students an identical environment. |
| [jupyter/notebook](https://github.com/jupyter/notebook) | BSD-3-Clause (`LICENSE`) | lab environment | The notebook itself. |
| [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | MIT (`LICENSE`) | content pipeline | Python framework for packaging arbitrary content into Kolibri channels. The ETL half of the offline-first pattern. |
| [learningequality/studio](https://github.com/learningequality/studio) | MIT (`LICENSE`) | content authoring | Curriculum authoring and channel curation that feeds Kolibri. |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 (`LICENSE`) | LMS integration | LTI tool-provider implementation. The permissive doorway into a copyleft LMS — see the license-boundary note in `agents/top.md`. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) — 🟢 **the KB has the current name; PyPI `openbadges` still declares the pre-2022 `IMSGlobal/...`**, same head `0a66b52` | Apache-2.0 (`LICENSE`) | credentialing | Open Badges validation. Relevant to the skills-economy trend: competency claims a third party can verify. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 (`LICENSE`) | lecture capture | Video capture, processing and delivery for universities. ECL-2.0 is an Apache-2.0 derivative, so it is **permissive** — the recorded-lecture corpus it produces is the natural input to the P2 ingestion pipeline. |

## Added in the third pass of 2026-10-06

Four infrastructure rows, each probed this pass. Three of them exist because
`Selleo/mentingo` (MIT) demonstrated a leaner sovereign stack than the one this KB
had been assembling by hand — see `verticals/solutions.md`.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | **PostgreSQL License** (`LICENSE`) — permissive, BSD-like | retrieval | Vector similarity search **inside PostgreSQL**. Removes a whole component from a sovereign deployment: no separate vector database to host, secure, back up and keep in-region. Where this KB previously reached for a dedicated vector store, reach for this first. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT, with a carve-out** (`LICENSE`) — see the warning below, and ⚠️ **the holder on that payload is `ClickHouse, Inc.`, not Langfuse** (the dual-licence wrapper was copied in, holder line and all). The grant text is MIT-Expat and unaffected; the **named grantor is a company that does not own the code**, which is a line a legal review will stop on | LLM observability | Traces every model call with cost, latency and the actual output. In a high-risk education deployment this is the **audit trail produced as a by-product of normal operation**, rather than as a separate compliance project. The single highest-leverage addition to every pattern in this KB. |
| [livekit/livekit](https://github.com/livekit/livekit) | **Apache-2.0** (`LICENSE`) | real-time voice | WebRTC infrastructure for spoken practice, oral assessment and role-play. The permissive path to voice tutoring, which is otherwise a proprietary-API-shaped problem. |
| [KualiCo/rice](https://github.com/KualiCo/rice) | **ECL-2.0** (`LICENSE.txt`) — permissive | higher-ed middleware | Application framework, workflow and eDocLite document routing built for and by the higher-education community. Java, 4★, 12 forks. **In maintenance mode** by its own README — vendor and fork it, do not present it as a living upstream. Full estate breakdown in `verticals/solutions.md`. |

### Two licence warnings on the rows above

**Langfuse is MIT *except* its `ee/` directories, and the copyright holder is now
ClickHouse, Inc.** The `LICENSE` payload is explicit: content under `ee/`,
`web/src/ee/` and `worker/src/ee/` is governed by a separate enterprise licence at
`ee/LICENSE`; everything outside those paths is MIT Expat. The copyright line reads
**"Copyright (c) 2023-2026 ClickHouse, Inc."** Two consequences: a repo-level "MIT"
badge is **not** sufficient diligence on an open-core project — the carve-out is by
*directory*, so the probe has to read the payload and the paths, not the badge. And
the copyright holder on a dependency can change under you between passes, which
nothing in a licence probe will flag. Build against the MIT paths, exclude `ee/`
from any vendored copy, and record the holder as well as the licence.

**pgvector is under the PostgreSQL License, not MIT, Apache-2.0 or BSD by name.**
It is permissive and BSD-like, and a naive allowlist that string-matches
`MIT|Apache|BSD` will reject it. Together with ECL-2.0 (Sakai, Opencast, Kuali
Rice) that is **four** genuinely permissive licences this KB relies on that a
three-name allowlist throws away. The allowlist for an education engagement is:
**MIT, Apache-2.0, BSD (2/3-clause), ECL-2.0, PostgreSQL License, ISC** — and read
the payload for carve-outs before trusting any of them.

## Added in the fourth pass of 2026-10-06

Channels new to this KB: **paper-to-repository tracing** (arXiv, ACL Anthology)
and a **GitHub-organisation sweep**. Licences read from each repository's own
`LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in a build |
|---|---|---|---|
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** (`LICENSE`, © 2026 THU-MAIC) | **40.0k** | **The content-generation spine.** Tsinghua's Open Multi-Agent Interactive Classroom: topic or document → slides, quizzes, HTML simulations and PBL scenes, delivered by AI teacher + AI classmate agents with TTS and a shared whiteboard; exports PPTX and interactive HTML. v1.2.0-rc.1 (2026-10-04) is **server-first with PostgreSQL persistence**, so generation survives a closed tab or restart. TypeScript / Next.js / React. |
| [AI-for-Education/fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | **MIT** (`LICENSE`) | 9 | Multi-provider LLM interface and chatbot management. A small, readable alternative to a heavyweight gateway when the deployment has to stay auditable. Python. |
| [AI-for-Education/fabdata-parsedoc](https://github.com/AI-for-Education/fabdata-parsedoc) | **MIT** (`LICENSE`) | 2 | Document text extraction, parsing and summarisation — the ingest stage ahead of any content pipeline. Python. Pair with or compare against `opendatalab/MinerU` already on this shelf. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** (`LICENSE`) | 12 | **Model-selection instrument.** Scores LLMs on *pedagogical knowledge* using teacher-qualification exam questions, rather than on task accuracy. The only thing on this shelf that answers "which model should teach this?" with evidence. Python. |
| [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | **MIT** (`LICENSE`) | 1 | Evaluation harness for **voice** interfaces — the modality that binds where literacy, device cost or bandwidth do. Python. |

**Star counts, stated plainly.** OpenMAIC is a flagship at 40.0k★. The four
`AI-for-Education` libraries are **1–12★ research-grade code** and should be read
and vendored deliberately, not pinned as if they were maintained infrastructure.
They are listed because this KB had **no permissive entry at all** for pedagogical
model selection or voice evaluation, and because they are the **first
Africa-placed repositories it has recorded** — the organisation's work is built
for **Sierra Leone's MBSSE** and for **Uganda** (Luganda).

**One sibling in that organisation is not usable:**
[`Luganda-linguistic-benchmarks`](https://github.com/AI-for-Education/Luganda-linguistic-benchmarks)
has **no `LICENSE` payload** (`README.md` 200, `LICENSE` 404). Five MIT siblings do
not license the sixth.

## Added in the fifth pass of 2026-10-06

**Channel: institution-first search** — funding bodies, ministries, universities
and research groups, queried by name in English and Spanish. All licences read
from each repository's own `LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in the stack |
|---|---|---|---|
| [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`, © 2023 Coursemology.org) | **158** · 78 forks · **15,802 commits** | **LMS core, permissive.** NUS-origin gamified learning platform: Rails 8 API, React client, Keycloak auth. "Currently supported by the AI Centre for Educational Technologies" and the deployment host for Singapore's **Codaveri** programming tutor. The one MIT LMS in this KB with a decade-scale commit history |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** (`main/LICENSE`, 2026) | 8 · 2 forks · 98 commits | **Compliance scaffolding.** Six-tier risk classifier over the Act's decision tree, **61 conformity checklist items** (risk management, data governance, documentation, human oversight), **8 document templates**. CLI + zero-dependency TypeScript SDK + client-only Next.js UI. **No education content** — supply the Annex III point 3 profile yourself (pattern P13) |
| [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) | **Apache-2.0** (`main/LICENSE`) | not read this pass | **Compliance measurement.** ETH Zurich framework pairing a technical interpretation of the AI Act with a generative-model benchmarking suite. Use it for the evidence the checklist above asks for |
| [crpf-mitadt/Indian-AI-for-Education](https://github.com/crpf-mitadt/Indian-AI-for-Education) | **CC0-1.0** (`main/LICENSE`) | not read this pass | **Regional index, not a dependency.** Curated map of Indian education AI: datasets, models, ASR, TTS, OCR, machine translation, infrastructure, benchmarks, research. CC0 means the map is free of attribution obligations; **every item it indexes still needs its own payload probe** |

### Coursemology is the licence answer to the Moodle question

This KB's platform shortcut has sent "needs permissive IP with no copyleft
exposure" to Frappe LMS and Kolibri, because Moodle, Open edX, Chamilo, Sakai and
ILIAS are all GPL-family. Coursemology changes that answer for **higher-education
and CS-teaching** engagements specifically:

| | Moodle / Open edX | Coursemology |
|---|---|---|
| Licence | GPL-3.0 / AGPL-3.0 family | **MIT** |
| Client fork, rebranded and resold | copyleft obligations attach | **no copyleft exposure** |
| Commit history | very large | **15,802 commits** |
| Community size | enormous | **158★ — small, and that is the real risk** |
| AI integration today | plugin / XBlock side-car | AICET's Codaveri already runs on it, closed source |

**The honest trade.** You swap a copyleft obligation for a **maintenance
concentration risk**: 158★ means a small contributor base and, realistically,
NUS-dependent maintenance. Take Coursemology where the client wants to own and
rebrand the platform outright and has engineering capacity; stay on Moodle or Open
edX where community breadth and plugin supply matter more than licence purity.
Do not present it as a drop-in Moodle replacement — its data model and its Keycloak
dependency are not Moodle's.

### A licence warning that applies per model, not per repository

[aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) is the
substrate anyone would reach for to build a Southeast Asian education layer, and
it has **no `LICENSE` payload** at any probed path. Its README §Licensing says
the project embraces MIT "as much as possible; however, the exact licensing terms
may vary depending on the underlying base model's restrictions" — Llama3-derived
variants carry **commercial-use restrictions**, Gemma-derived variants carry
different terms again — and directs you to each model's **Hugging Face model
card**.

**So: clear rights per model, per release, before a SEA sovereign-model education
engagement is scoped.** A repository-level licence check on `sealion` returns
nothing, and a studio that stops there will have cleared nothing at all.

## Added in the sixth pass of 2026-10-06 — the speech and language substrate

Every tutor elsewhere in this KB is, by default, **mute and monolingual**. This
shelf is the layer that fixes that, and before this pass the KB had **no entry for
it at all**. Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page. Discovery narrative in `agents/trending.md`, sixth pass.

### Speech — recognition, synthesis, diarization

| Repo | Licence (payload) | ★ / commits | Role |
|---|---|---|---|
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) | **15.1k** / 2,092 | **The headline addition.** STT **+** TTS **+** speaker diarization **+** VAD in one permissive tree, running **with no Internet connection** on Android, iOS, HarmonyOS, Raspberry Pi, RISC-V and x86 servers, with bindings for 12 languages. Replaces four dependencies with one and is the component the offline-first pattern was missing |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **MIT** (`master/LICENSE`) | 25.7k / 267 | **The ASR to deploy.** CTranslate2 reimplementation of Whisper — faster, lower memory, same weights |
| [openai/whisper](https://github.com/openai/whisper) | **MIT** (`main/LICENSE`) | **110k** / 171 | The reference implementation and the accuracy baseline to quote |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | **BSD** (`main/LICENSE`) | — | **Word-level timestamps** plus diarization. The timestamps are what turn a transcript into a *fluency measure* — see P17 |
| [speechbrain/speechbrain](https://github.com/speechbrain/speechbrain) | **Apache-2.0** (`main/LICENSE`) | 11.9k / **10,611** | PyTorch toolkit: 200+ training recipes over 40+ datasets, 20 speech and text tasks. The bridge when a language needs a model trained rather than downloaded |
| [espnet/espnet](https://github.com/espnet/espnet) | **Apache-2.0** (`master/LICENSE`) | 10.0k / **27,378** | End-to-end speech toolkit with the deepest recipe archive here. First stop for a language nothing off-the-shelf covers |
| [huggingface/parler-tts](https://github.com/huggingface/parler-tts) | **Apache-2.0** (`main/LICENSE`) | 5.6k / 199 | Prompt-controllable TTS — the voice is described in text, so register can be tuned per age group without retraining |
| [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) — ⚠️ **now `NVIDIA-NeMo/NeMo`**; both paths serve head `50c71db`, see the canonical-name table below | **Apache-2.0** (`main/LICENSE`) | — | Full speech + LLM training stack where GPUs are available |
| [pytorch/audio](https://github.com/pytorch/audio) | **BSD** (`main/LICENSE`) | — | Audio primitives underneath the above |
| [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | **MPL-2.0** (`main/LICENSE.txt`) | 2.3k / **5,309** | Voice cloning and XTTS-class synthesis, **actively maintained** at Idiap Research Institute (Switzerland). PyPI `coqui-tts`. **Use this, not the 46.1k★ original** — see the warnings below |

### Language — translation and local-language models, placed by region

| Repo | Licence (payload) | ★ / commits | Region | Coverage |
|---|---|---|---|---|
| [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** (`main/LICENSE`) | 478 / 124 | APAC | Translation across **all 22 scheduled Indian languages**, with script unification across Devanagari, Perso-Arabic and others |
| [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | **MIT** (`master/LICENSE.txt`) | 406 / 58 | APAC | TTS in **13** languages: Assamese, Bengali, Bodo, Gujarati, Hindi, Kannada, Malayalam, Manipuri, Marathi, Odia, Rajasthani, Tamil, Telugu |
| [AI4Bharat/IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) | **MIT** (`main/LICENSE`) | 121 / 131 | APAC | ASR pretrained on **40** Indian languages; fine-tuned for Bengali, Gujarati, Hindi, Marathi, Nepali, Odia, Tamil, Telugu, Sinhala, plus Kannada and Malayalam |
| [AI4Bharat/IndicLLMSuite](https://github.com/AI4Bharat/IndicLLMSuite) | **MIT** (`master/LICENSE`) | — | APAC | Data and recipe suite for building Indic LLMs |
| [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) | 72 / 69 | APAC | *"Open source platform to annotate and label data at scale."* The **human-in-the-loop stage** every pattern in this KB specifies, and the only shelved tool that implements it |
| [SunbirdAI/salt](https://github.com/SunbirdAI/salt) | **Apache-2.0** (`main/LICENSE`) | 15 / 303 | EMEA | **Uganda.** Translation (~25k sentences), ASR (~5k) and **studio-recorded TTS data (~5k, professional voice actors)** across English (Ugandan/Kenyan accents), **Luganda, Swahili, Ateso, Lugbara, Acholi, Runyankole**. Two AfricaNLP papers |
| [masakhane-io/masakhane-mt](https://github.com/masakhane-io/masakhane-mt) | **MIT** (`master/LICENSE`) | 327 / 645 | EMEA | **Africa-wide.** Machine translation from a 1,000-participant, 30-country community. **226 forks against 327 stars** — a deployment signal, not a vanity one |
| [masakhane-io/masakhane-ner](https://github.com/masakhane-io/masakhane-ner) | **Apache-2.0** (`main/LICENSE`) | — | EMEA | Named-entity recognition for African languages |
| [Polygl0t/Polygl0t](https://github.com/Polygl0t/Polygl0t) | **Apache-2.0** (`main/LICENSE`) | 27 / 379 | EMEA | **University of Bonn** Polyglot initiative. LLM training/eval foundry, FineWeb-2 pipeline, "support for thousands of languages." Home of **Tucano 2** (0.5–3.7B Portuguese, arXiv 2603.03543) |
| [Nkluge-correa/Tucano](https://github.com/Nkluge-correa/Tucano) | **Apache-2.0** (`main/LICENSE`) | 86 / 29 | LATAM *(origin)* | Portuguese-native open LLM suite, peer-reviewed in *Patterns* ([10.1016/j.patter.2025.101325](https://doi.org/10.1016/j.patter.2025.101325)). **Archived 2026-02-24** — still usable, no longer developed. Successor is the Bonn-hosted row above |

### Five licence warnings on the rows above — read before selecting any of them

**1. Piper relicensed, and the permissive version is frozen.**
[rhasspy/piper](https://github.com/rhasspy/piper) is **MIT** (`master/LICENSE.md`,
© 2022 Michael Hansen), 11.3k★ — and **archived read-only since 2025-10-06**, its
notice pointing to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl),
which is **GPL-3.0** (`main/COPYING`). Piper is the offline-TTS default of Home
Assistant and NVDA and runs on a Pi 4, so it is the natural reach for low-cost
classroom voice. **There is no option that is both permissive and maintained.**
Deliberately **not shelved above**: use `sherpa-onnx` (Apache-2.0) or
`idiap/coqui-ai-TTS` (MPL-2.0) instead, and reach for Piper only with the
frozen-vs-copyleft trade made explicitly and in writing.

**2. The 46.1k★ Coqui repository is not the live one.**
[coqui-ai/TTS](https://github.com/coqui-ai/TTS) is **MPL-2.0** and **unmaintained**
— the company wound down. The Idiap fork shelved above has **5,309 commits against
the original's 4,668**. Depend on the fork; cite the original only for history.

**3. SeamlessM4T is non-commercial — a hard reject.**
[facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication)
carries **Attribution-NonCommercial 4.0 International** in `main/LICENSE`. It is
the first result for "open source multilingual speech" and **cannot be used in
billable work**. Compose Whisper (MIT) + IndicTrans2 (MIT), or sherpa-onnx
(Apache-2.0), to reach the same capability.

**4. SEA-LION has no repository-level grant, by design.**
[aisingapore/sea-lion](https://github.com/aisingapore/sea-lion) has **no `LICENSE`
payload** (3 branches × 6 filenames probed). Its README states the terms *"may
vary depending on the underlying base model's restrictions"* — Llama-derived
variants may carry Meta's commercial restrictions — and directs you to each
HuggingFace **model card**. **The licence is a property of the checkpoint, not the
project**, so an APAC engagement must review it per model file and **re-review on
every checkpoint change**. Not shelved as a dependency for this reason.

**5. An unlicensed catalogue is still unlicensed.**
[AI4Bharat/indicnlp_catalog](https://github.com/AI4Bharat/indicnlp_catalog) has
**no `LICENSE` payload** despite five MIT siblings in the same organisation. Use
it to *find* resources; probe every resource it names. (Same shape as
`AI-for-Education/Luganda-linguistic-benchmarks` in the fourth pass — and note
that `SunbirdAI/salt` above is the **Apache-2.0 answer to that specific
rejection**, covering Luganda and five more Ugandan languages.)

### Why this shelf changes the architecture, not just the feature list

Three consequences worth stating, because they are not obvious from the table:

- **Voice stops being a proprietary-API-shaped problem.** `sherpa-onnx` alone
  delivers STT, TTS, diarization and VAD under Apache-2.0 on embedded hardware.
  Spoken practice, oral assessment and role-play become deployable where there is
  no connectivity and no per-token budget.
- **Mother-tongue instruction becomes a permissive capability in two regions.**
  India (22 languages, MIT) and Uganda/Africa (6 Ugandan languages Apache-2.0,
  plus Masakhane's continental MT, MIT) can be served from the shelf. **Elsewhere
  it cannot** — see the regional honesty note in `intel/market.md`.
  **⚠️ SUPERSEDED by the seventh pass of 2026-10-06: it is at least three
  regions.** ASEAN has a permissive layer across **Vietnamese, Thai, Malay and
  Indonesian** — `underthesea` (Apache-2.0, 1.8k★), `pythainlp` (Apache-2.0,
  1.2k★, 6,649 commits), `malaya` + `malaya-speech` (both MIT) and `nusa-crowd`
  (Apache-2.0, 143 datasets). See the seventh-pass section below. The sixth pass
  reached "two regions" by searching for sovereign **models** and finding
  SEA-LION unlicensed; the toolkits were one query away in another language.
- **Masakhane licenses three repositories three ways** — MIT, Apache-2.0 and GPL
  inside one owner. The fourth pass's rule was "five MIT siblings do not license
  the sixth." The stronger rule: **sibling licences need not even share a
  class.** Probe every repository, every time.

## Added in the seventh pass of 2026-10-06 — the ASEAN language substrate, and trend 21 falsified

**Channel new to this KB this pass: native-language search.** Earlier passes
searched in English and, in the fourth pass, Spanish and Portuguese. This pass
searched in **Japanese, Korean, Arabic and Bahasa/Thai/Vietnamese**. The sixth
pass had closed with a clean, falsifiable claim — *"mother-tongue AI is a
two-region capability"*, India and Africa, with ASEAN explicitly named as the
place where *"the nearest thing, SEA-LION, has no repository-level licence at
all."*

**That claim is wrong, and this is the shelf that falsifies it.** ASEAN has a
permissive, self-hostable language layer covering **five languages across four
countries**, most of it Apache-2.0, some of it with more commits than anything
on the India shelf. It was invisible to six passes because **SEA-LION is a
sovereign *model* and these are language *toolkits*** — a different noun, and
nobody had searched for the noun.

Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page the same day. **13 repositories probed, 13 resolved.**

### Language — ASEAN, placed by country

| Repo | Licence (payload) | ★ / forks / commits | Country | Coverage |
|---|---|---|---|---|
| [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** (`main/LICENSE`) | **1.8k** / 307 / 1,276 | **Vietnam** | The largest asset on this shelf. 13 Vietnamese tasks — sentence segmentation, text normalization, **diacritics restoration**, word segmentation, POS, chunking, NER, classification, sentiment, language detection, dependency parsing, translation and TTS. **v9.3.0 rebranded the project to an "Open-source Agentic AI Toolkit"** with multi-provider agent support (OpenAI, Azure OpenAI, Anthropic Claude, Google Gemini) layered over the Vietnamese NLP core |
| [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** (`main/LICENSE`) | **1.2k** / 304 / **6,649** | **Thailand** | *"Thai natural language processing in Python."* Sentence, word and **subword** tokenization — the hard problem in a script with no spaces — plus POS tagging, romanization and **IPA transliteration**, spelling correction, soundex, collation, number-to-text, and a `thainlp` CLI. v5.3.8, Python 3.9+, self-declared **"Project Status: Active."** The deepest commit history of any language toolkit in this KB outside the general speech shelf |
| [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** (`master/LICENSE`, © 2018 huseinzol05) | 530 / 141 / 961 | **Malaysia** | *"Natural-Language-Toolkit library for bahasa Malaysia, powered by PyTorch."* NER with a named-entity framework, POS, sentiment, emotion, subjectivity, language detection and normalization. Pretrained models on HuggingFace (`mesolitica`); docs at `malaya.readthedocs.io` |
| [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** (`master/LICENSE`, © 2020 HUSEIN ZOLKEPLI) | 291 / 51 / 755 | **Malaysia** | *"Speech-Toolkit library for Malaysian language, powered by PyTorch."* The **only ASEAN-placed permissive speech toolkit** found; ships a `malay_vits` TTS path. Pair with `sherpa-onnx` for the offline runtime |
| [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** (`master/LICENSE`) | 292 / 64 / 992 | **Indonesia** | *"A collaborative project to collect datasets in Indonesian languages."* **143 registered datasets** behind standardized dataloaders, built by a credited multi-institution consortium; paper *NusaCrowd: Open Source Initiative for Indonesian NLP Resources* ([arXiv:2212.09648](https://arxiv.org/abs/2212.09648)). Contributors earn **co-authorship by contribution points** — a governance model worth copying for a ministry corpus engagement |
| [indobenchmark/indonlu](https://github.com/indobenchmark/indonlu) | **Apache-2.0** (`master/LICENSE`) | — (not read this pass) | **Indonesia** | Indonesian natural-language-understanding benchmark — the evaluation half of the row above |

### Read this shelf honestly — three qualifications

- **None of it is education-specific.** Exactly like AI4Bharat on the India
  shelf, these are general-purpose language toolkits. They make a mother-tongue
  tutor *possible*; they do not make one. The pedagogy layer is still yours to
  build, which is the opportunity (**P19**).
- **Only one covers speech.** `malaya-speech` is the single ASEAN-placed
  permissive speech toolkit here. Thai, Vietnamese and Indonesian have the
  **text** layer and no local **voice** layer, so spoken practice in those three
  languages routes through the general shelf — `sherpa-onnx` (Apache-2.0) or
  Whisper/faster-whisper (MIT) — and must be accuracy-tested per language rather
  than assumed.
- **Two of these are corpora-and-recipes, not runtimes.** `nusa-crowd` and
  `indonlu` give you data and evaluation; they are not something you deploy. Size
  the engagement accordingly.

### One more licence warning, and the first measured counter-example to it

[malaysia-ai/malaysian-dataset](https://github.com/malaysia-ai/malaysian-dataset)
— **no `LICENSE` payload** (2 branches × 6 filenames probed), and at **345★** it
is the organisation's **second most-starred repository**, ahead of
`malaya-speech`. Its two code siblings are both MIT. **Not shelved. Not
shippable.**

This is the **second time this KB has found the pattern in the same shape**: the
sixth pass recorded `AI4Bharat/indicnlp_catalog` as unlicensed among five MIT
siblings. Two independent organisations, two regions, and in both the repository
without a grant is the **data/catalogue** one while the **code** repositories are
permissive. A tempting rule follows — *the data layer is where the grant goes
missing* — and this pass **measured its counter-example in the same sweep**:
`IndoNLP/nusa-crowd` is a dataset hub of 143 corpora and it is **Apache-2.0**.

**So state it as a prior, not a law: on a data or catalogue repository, assume no
grant until the payload says otherwise — and probe it, because one in three
cedes.** The operational rule is unchanged and now carries three instances
instead of one: **probe every repository, every time, and probe the dataset
sibling separately from the code.**

## Added in the eighth pass of 2026-10-06 — the LATAM language substrate, and where it stops

The seventh pass falsified "mother-tongue AI is a two-region capability" by
searching ASEAN for language **toolkits** instead of sovereign **models**. The
eighth pass ran the same move at the one gap this KB called its firmest: **no
LATAM-origin permissive education project.**

**The move works at the majority-language layer and fails at the indigenous
layer — and it fails for a reason this shelf has seen before in MEA.**
Licences read from each repository's own `LICENSE` payload.

### Language — Spanish and Portuguese, permissive and real

| Repo | Licence (payload) | ★ / forks / commits | What it is |
|---|---|---|---|
| [neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert) | **MIT** (`master/LICENSE`, © 2020 NeuralMind — Fabio Capuano de Souza, Rodrigo Nogueira, Roberto de Alencar Lotufo) | **886** / 139 / 20 | **BERTimbau** — BERT-Base and BERT-Large for **Brazilian Portuguese**, trained on **BrWaC** for 1M steps with whole-word masking. State of the art on NER, STS and RTE at publication. **Brazil-origin, and the first Brazil-origin permissive asset on this shelf** |
| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | **Apache-2.0** (`master/COPYING`) | — | Offline ASR for 20+ languages including **Spanish and Portuguese**, Raspberry-Pi-class hardware, Python/Java/C#/Node bindings. Permissive, maintained — **global-origin, not LATAM** |

`speechbrain/speechbrain` (Apache-2.0) on the sixth-pass shelf remains the
bridge when a language needs a model **trained** rather than downloaded.

### Language — indigenous languages of the Americas: the capability is there, the grant is not

| Repo | Licence state (payload) | Coverage |
|---|---|---|
| [Llamacha/IWSLT2023_Quechua_data](https://github.com/Llamacha/IWSLT2023_Quechua_data) | ⚠️ payload **Apache-2.0**, README **CC BY-NC-ND 3.0** — **scope conflict, see below** | **Peru** — ~1h40m aligned Quechua–Spanish speech + pointers to 60h transcribed Siminchik audio. Southern Quechua |
| [pywirrarika/naki](https://github.com/pywirrarika/naki) | **GPL-3.0** (`master/LICENSE`) | Curated NLP research and engineering index for Native American languages |
| [AmericasNLP/americasnlp2021](https://github.com/AmericasNLP/americasnlp2021) | **No `LICENSE` payload** | Shared task — **Aymara** (6,531 pairs), **Nahuatl** (16,145), **Quechua** (125,008) |
| [AmericasNLP/americasnlp2022](https://github.com/AmericasNLP/americasnlp2022) | **No `LICENSE` payload** | Second probed edition |
| [AmericasNLP/americasnlp2023](https://github.com/AmericasNLP/americasnlp2023) | **No `LICENSE` payload** | Third probed edition |
| [AmericasNLP/americasnlp2024](https://github.com/AmericasNLP/americasnlp2024) | **No `LICENSE` payload** — 404 at root **and** in both task subdirectories | MT into indigenous languages, **plus Shared Task 2: "Creation of Educational Materials for Indigenous Languages"** — sentence-transformation and fill-in-the-blank exercise generation, data and baselines shipped. **No root `README.md`; existence confirmed via `master/ST1_MachineTranslation/README.md`** |
| [monirome/asr-indigenous-languages](https://github.com/monirome/asr-indigenous-languages) | **No `LICENSE` payload** | Fine-tuned ASR: **Quechua, Guaraní, Bribri, Kotiria, Wai'khana** |
| [UBC-NLP/IndT5](https://github.com/UBC-NLP/IndT5) | **No `LICENSE` payload** | Text-to-text transformer for **10** indigenous languages |
| [aoncevay/mt-peru](https://github.com/aoncevay/mt-peru) | **No `LICENSE` payload** | *"Peru is Multilingual, Its Machine Translation Should Be Too?"* |
| [aoncevay/quechua-nlp](https://github.com/aoncevay/quechua-nlp) | **No `LICENSE` payload** | Standard Southern Quechua data for NLP |
| [Llamacha/IWSLT2025_Quechua_data](https://github.com/Llamacha/IWSLT2025_Quechua_data) | **No `LICENSE` payload** | The 2025 edition — **same organisation, licensed 2023 and not 2025** |
| [jnehring/awesome-low-resource-languages](https://github.com/jnehring/awesome-low-resource-languages) | **No `LICENSE` payload** | Endangered / low-resource language resource index |

**Ten of twelve carry no grant at all.** **AmericasNLP** — the flagship academic
venue for the indigenous languages of the Americas — has run **four probed
editions (2021, 2022, 2023, 2024) without a `LICENSE` file in any of them**, and
its 2024 edition ships the one task on this shelf that is **explicitly an
education task**: *"Creation of Educational Materials for Indigenous
Languages"*, with data and baseline scripts and no grant. The same author
(`aoncevay`) licensed neither of two repositories; the same organisation
(`Llamacha`) licensed one edition and not the next.

### ⚠️ The `Llamacha` scope conflict — it defeats this shelf's own method

Every licence on this shelf is read from the repository's own `LICENSE` payload.
Do that to `Llamacha/IWSLT2023_Quechua_data` and you get **complete, unambiguous
Apache-2.0** from `main/LICENSE`.

**The README says otherwise:**

> All audio recordings are property of Siminchikkunarayku and Llamacha.
> This work is licensed under a Creative Commons
> **Attribution-NonCommercial-NoDerivs 3.0 Unported License**.

**NonCommercial and NoDerivs — unusable in commercial client work.** The Apache
file plausibly covers the repository's scripts; the **data**, which is the only
reason to clone it, is NC/ND.

**This is a third licence trap, distinct from the two this KB already tracks.**
`p184` catches a holder foreign to the project. The seventh pass's
MathTutorBench case catches a file that contradicts itself internally. This is
**a correct, complete licence file applied to the wrong scope.**

**Rule for this shelf, from this pass forward: for any repository whose value is
data, audio, a corpus or model weights, the payload is necessary and not
sufficient.** Read the README's licence section too, and treat the
**asset-scope** statement as controlling for the asset.

### Why this shelf matters even though most of it is unusable

**Because it is the exact layer a regional tutor needs next, and it is one
`LICENSE` file per repository away from being usable.**

`LabSirius/TutorIA`'s own **RNF-10** specifies Colombian Spanish for v1.0 *"con
posibilidad futura de soportar **lenguas nativas**"*. Latam-GPT lists indigenous
languages as roadmap. So the demand is written down in two places, and the
supply — corpora, ASR for five languages, MT, benchmarks, a T5 for ten
languages — **already exists, funded and published.** What is missing is
redistribution rights.

**This is the MEA diagnosis in a second region.** The seventh pass concluded of
MEA: *"the binding constraint is not interest, funding or capability — it is
licensing hygiene. Three `LICENSE` files would change the regional answer."*
That sentence is now true of the LATAM indigenous layer word for word, and the
eighth pass found a **remedy that works prospectively**: a submission rule in a
university event's terms produced **20 licensed repositories in eight hours**
(see `agents/top.md`, the CAi UC holder warning, and `intel/market.md`).

**For an engagement:** a Quechua or Guaraní tutor is blocked on **data rights,
not on modelling**. Budget the licence conversation with Llamacha,
Siminchikkunarayku and the AmericasNLP organisers as a project line item, not an
afterthought — and note that `vosk-api` (Apache-2.0) plus `speechbrain`
(Apache-2.0) give you a permissive *pipeline* into which licensed data can be
dropped the moment it exists.

## Added in the ninth pass of 2026-10-06 — a ministry's MIT estate, and the offline stack's real licence shape

Channel: the **funder and procurement channel** and its government twin, the
**education-ministry engineering organisation**. Nine passes had swept
hackathons, universities, ministries *by name*, funding bodies, GitHub topic
pages and academic papers. **None had swept a ministry's own GitHub org.**

### The UK Department for Education estate — government-grade, production, MIT

`DFE-Digital` is the UK Department for Education's engineering org. It runs
**live national education services** in the open, under MIT. Licences read from
payload:

| Repo | Licence | ★ | Lang | Role |
|---|---|---|---|---|
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** (`main/LICENCE`) | 38 | Ruby | The national service for applying to teacher-training courses |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** (`main/LICENSE`) | 27 | Ruby | National teaching job-listing service |
| [DFE-Digital/get-into-teaching-app](https://github.com/DFE-Digital/get-into-teaching-app) | **MIT** (`master/LICENCE`) | 25 | Ruby | Teacher-recruitment site and candidate journey |
| [DFE-Digital/publish-teacher-training](https://github.com/DFE-Digital/publish-teacher-training) | **MIT** (`main/LICENSE`) | 12 | Ruby | Provider course publishing + candidate discovery |
| [DFE-Digital/register-trainee-teachers](https://github.com/DFE-Digital/register-trainee-teachers) | **MIT** (`main/LICENCE`) | 12 | Ruby | Trainee registration for initial-teacher-training placements |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** (`main/LICENCE`) | 9 | C# | GIAS — the national schools register |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** (`main/LICENSE`) | 5 | C# | Compares one school's metrics against similar institutions |

### What this estate is good for, stated precisely

**It is administrative software, not AI, and it closes no AI gap in this KB.**
Taken for what it is, it is the first thing of its kind on these shelves:

1. **Reference architecture for education workflow at national scale.** Five of
   the seven are Ruby services that have run a country's teacher pipeline.
   For an EMEA public-sector engagement, *"here is how a ministry built this, and
   you may read and reuse the code"* is a stronger opening than a vendor demo.
2. **Schemas you will have to integrate with anyway.** GIAS is the UK's
   authoritative schools register; `register-trainee-teachers` and
   `publish-teacher-training` encode the ITT domain model. Any UK education
   engagement meets these data structures eventually — and here they are, MIT.
3. **A benchmarking component with the right shape.**
   `education-benchmarking-and-insights` does school-to-peer-group comparison —
   the data layer under any "how is my school doing" analytic, and the natural
   grounding source for a reporting agent.
4. **Procurement credibility.** An MIT licence from a ministry is the cleanest
   possible answer to the public-sector question *"can we actually own and audit
   this?"*

**What it is not:** none of it is AI, none of it is a tutor, and its star counts
(5–38★) reflect government repos that are consumed as services rather than
forked. **Do not read low stars as low maturity here** — these are production
systems for a national education system. It is the one place in this KB where
the star signal is actively misleading in the *opposite* direction to usual.

### ⚠️ The licence-filename warning that changes this KB's method

**Four of these seven grants are in a file spelled `LICENCE`.** Pattern **P22**'s
gate lists that spelling; **no recorded sweep in this KB has ever run it.** Every
probe set written down across nine passes — `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING`, `license.txt` — **matches none of these four files.** With the old set,
`apply-for-teacher-training`, `get-into-teaching-app`,
`register-trainee-teachers` and `get-information-about-schools` would all have
been recorded as **ungranted**. They are MIT.

**The probe set is now `LICENSE{,.md,.txt}`, `LICENCE{,.md,.txt}`, `COPYING`,
`COPYRIGHT`, `license.txt`, both branches.** Any earlier pass's "no grant"
verdict on a Commonwealth, MEA or ministry-adjacent repository should be treated
as **unconfirmed until re-probed** — those are exactly the repositories that
spell it the British way.

### Measured rejections from the same organisation

| Repo | ★ | Why rejected |
|---|---|---|
| `DFE-Digital/gias-query-tool` | 17 | **No licence payload.** The SQL query layer over GIAS — the most immediately useful tool in the org, and ungranted. Sixth pass running in which the most-reached-for asset of a sweep has no grant |
| `DFE-Digital/rsd-ai-libs` | 0 | **No payload.** *".NET library for building and evaluating Azure AI Foundry agents with guardrails, Azure AI Search, and MCP server support"* — a ministry building MCP agent tooling, which corroborates trend 4; unusable as code, citable as a signal |
| `DFE-Digital/sts-ai-support` | 1 | No licence shown on the org listing; not individually payload-probed |
| `DFE-Digital/ai-briefing-tool-prototype` | 0 | Non-production prototype; no licence shown |
| `DFE-Digital/rsd-common-ai-services` | 0 | Provisioning scaffolding; no licence shown |

**The asymmetry is the strategic finding:** the DfE's **administrative** tier is
production-grade and MIT; its **AI** tier is prototype-grade and unlicensed. A
consultancy's opening in EMEA public-sector education is therefore *not* "you
need a platform" — they built one — but **"your AI layer is five unlicensed
prototypes at zero stars, and your administrative layer is a licensed national
asset; let us build the first on top of the second."**

### The offline delivery stack, licence shape corrected

The eighth pass built the offline-first tier around Kolibri and EduFlow but could
not resolve RACHEL. Resolved this pass, and the stack's licensing is not what the
page implied:

| Repo | Payload | Licence | Usable? |
|---|---|---|---|
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `develop/LICENSE` | **MIT** | ✅ re-confirmed — the platform answer |
| [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft — see below |
| [kiwix/libkiwix](https://github.com/kiwix/libkiwix) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [kiwix/kiwix-android](https://github.com/kiwix/kiwix-android) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [openzim/libzim](https://github.com/openzim/libzim) | `main/COPYING` | **GPL-2.0** | ⚠️ copyleft, and GPL-2.0 ≠ GPL-3.0 for compatibility |
| [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **none** | README: *"Creative Commons - BY, SA, NC"* | ❌ **NonCommercial — do not ship** |

**Three warnings on that table:**

1. **RACHEL is out.** `contentshell` *is* RACHEL — the PHP CMS that serves
   content on RACHEL devices — and its only licence statement is a **content
   licence with NonCommercial, applied to software**, with no payload to weigh
   against it. Creative Commons advises against CC for software; either reading
   (unlicensed, or NC) stops a commercial deliverable. **Cite RACHEL as prior
   art for offline delivery; ship Kolibri.**
2. **The ZIM layer is GPL, and that is an architecture decision, not a
   footnote.** Offline Wikipedia/Wikibooks content ships as ZIM, and the entire
   reference implementation — `libzim` (GPL-2.0), `libkiwix`, `kiwix-tools`,
   `kiwix-android` (GPL-3.0) — is copyleft. You may deploy it; you may not
   statically link it into a proprietary client deliverable without taking the
   obligation. **Keep Kiwix as a separate process behind an HTTP boundary** —
   exactly the side-car reasoning this KB already applies to MCP — and the
   client's own code stays unencumbered.
3. **GPL-2.0 and GPL-3.0 in one dependency tree** (`libzim` vs `libkiwix`) is a
   combination to raise with counsel if anything is being linked rather than
   invoked. Process separation makes the question moot, which is a second reason
   for the side-car.

## Added in the twenty-first pass of 2026-10-06 — no new rows, and a second licence on the existing ones

🔵 **This pass adds no foundational repositories, and the reason is structural rather than a dry
sweep.** The declared-dependency channel does not discover projects; it **re-prices the ones already
here**. Every row on this shelf carried one licence — its own. The rows below now carry a second: the
licence of **what they install**.

⚠️ **The platform channel was re-probed and remains saturated**, verified by grep rather than
assumed: OpenEduCat, Open edX, Moodle, Sakai, OLAT/OpenOLAT, Chamilo, Gibbon, Frappe, `.LRN` all
already shelved. The one name new to the result set, **`CK-ERP`** — a 32-module education / ERP / CRM
/ MRP system — is recorded here as a **measured non-finding**: the most recent release note in the
result set is from **2010** and it is Drupal-6 era. 🔴 **Abandonware, not a shelf candidate.**

### What the foundation shelf installs

| Foundation row | Its licence | Direct deps | Closure verdict |
|---|---|---|---|
| `oppia/oppia` | Apache-2.0 | **152** | 🔴 **REVIEW-STRONG** — `mutagen` is `GPL-2.0-or-later`; `certifi` MPL-2.0; `orjson` `MPL-2.0 AND (Apache-2.0 OR MIT)`; `azure-cognitiveservices-speech` `Other/Proprietary License`. **148 of 152 clean** |
| `learningequality/kolibri` | MIT | **32** | ⚠️ **REVIEW-WEAK** — 2 LGPL rows, 2 unreadable. ⚠️ Measurable only via `[dependency-groups] base`; both canonical fields answer "nothing" and both are wrong |
| `huggingface/smolagents` | Apache-2.0 | 6 | 🟢 **CLEAN** — the smallest permissive surface on the shelf, now verified on both layers |
| `microsoft/agent-framework` | MIT | 1 | ⚠️ **CLEAN but uninformative** — `agent-framework-core[all]==1.20.0`; the closure is one level down |

🟢 **The operational consequence for foundation selection:** where two foundations are otherwise
comparable, **the one with the smaller declared surface is the cheaper one to clear legally**, and
that is now a measured property rather than an instinct. smolagents at 6 declared dependencies and
Oppia at 152 are not the same procurement task even when both say Apache-2.0.

### 🔴 The evidence tooling the twentieth pass went looking for is still absent — and now so is one more layer

⚠️ **The twentieth pass recorded zero occurrences of `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn` and `AIF360`.** 🔴 **A dependency-licence
audit is the same shape of missing instrument one layer further down:** this KB can now resolve a
licence per dependency, but it has **no SBOM layer** — no `syft`, no `cyclonedx`, no
`pip-licenses`/`license-checker` row anywhere on the shelf. 🔵 **Recorded as a declared gap with a
named next step rather than as a new row, because this pass did not verify any of those tools against
an education deployment and will not shelf what it has not read.**

## Teaching-content repos (for enablement, not for production)

| Repo | License (read from payload) | Note |
|---|---|---|
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 18 lessons, 76.5k★ |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | MIT (`LICENSE`) | the GenAI prerequisite track |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Apache-2.0 (`LICENSE.txt`) | builds a GPT-class model in PyTorch; >100k★ class resource |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Apache-2.0 (`LICENSE`) | roadmap + notebooks |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | agent track |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | APAC-origin, large cohort programme |
| [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | MIT (`LICENSE@main`) | production agentic-RAG — the missing middle between an agent demo and a deployed retrieval system |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | MIT (`LICENSE@main`) | AI-engineering track, trending through 2026 |

## Repos checked and deliberately not recommended

Recording these saves the next pass the probe.

| Repo | Finding |
|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Maintenance mode, no new features; `LICENSE` at HEAD is CC-BY-4.0 (dual with MIT). Use `microsoft/agent-framework` instead. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0**, not MIT. Widely mis-reported as MIT by LMS comparison blogs. The license lives at `license.txt` (lowercase) — `LICENSE` returns 404, which is how the misreport propagates. |
| [cloudtoolbox/deeptutor](https://github.com/cloudtoolbox/deeptutor) | 7★ fork of `HKUDS/DeepTutor`. Correct Apache-2.0 license, no history. Pin the HKUDS origin. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | **Unlicensed.** 103★, 54 tools, v2.3.0 — and no `LICENSE` on any branch, no license statement in the README. Default copyright: all rights reserved. The most dangerous repo in this KB precisely because it looks mature. |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | **Unlicensed.** 38★, Python, no `LICENSE` on any branch, none in README. |
| [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) | **Unlicensed.** 8★, 5 commits. Recorded in an earlier cycle of this KB as "MIT, ~900★" — wrong on both counts. Withdrawn; see `agents/top.md`. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 **plus** a paid premium-plugin tier. Legally usable, commercially the worst shape on the shelf for reusable studio IP. |
| [planejaia/OpenMAIC-Brasil](https://github.com/planejaia/OpenMAIC-Brasil) | **404 — does not exist.** Surfaced by search as a Brazil-origin multi-agent classroom, v1.0.0 "released 2026-08-27". Every file 404s on four branches and the repo page returns HTTP 404. Recorded so the next pass does not chase it again. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | GPL-3.0 at `license.txt` (lowercase) — usable, but listed here because it shares `frappe/lms`'s probe trap: `LICENSE` returns 404. |
| [kuali/kfs](https://github.com/kuali/kfs) | **AGPL-3.0** (`LICENSE`). Kuali Financial System. Same consortium as the permissive Kuali Rice — the licence is per repository, not per foundation. |
| [kuali/kc](https://github.com/kuali/kc) | **AGPL-3.0** (`license.txt`, lowercase). Kuali Coeus research administration. Third live instance of the lowercase-`license.txt` probe trap, after `frappe/lms` and `frappe/erpnext`. |
| [kuali/rice](https://github.com/kuali/rice) | Correct licence (ECL-2.0) but **DEPRECATED** by its own README, which points to `KualiCo/rice`. Pin the KualiCo location. |
| `kuali/student`, `KualiCo/student`, `kuali/coeus` | **Not reachable** — `README.md` 404s on all three. Kuali Student (the SIS) is not at the path its name implies; recorded so the next pass does not re-probe these. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **AGPL-3.0**, 563★. Competency skill tree, K-12 to career. Reference for competency-graph design only. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 156★. Self-hosted AI language learning. |
| [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | **GPL**, 88★. Learner-owned course generation. |
| [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | **AGPL-3.0**, 71★. Game-based course conversion. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | **Unlicensed**, 61★. Its README's licence section reads only *"This project is open source and available for educational purposes"* — prose that imitates a grant. No licence, no holder, no redistribution right. |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | **Unlicensed**, 24★. No `LICENSE` and no licence mention anywhere in the README. |

## Method note

License probes need both axes — filename *and* extension. `LICENSE`,
`LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING` and `COPYING.txt` are all
in live use across this shelf, and probing only `LICENSE` produces false
negatives (`frappe/lms` and `moodle/moodle` both hide from a single-path probe).
A badge or a comparison blog is not a license reading.

A licence probe also needs a third axis: **path depth**. `OS4ED/openSIS-Classic`
404s on every root-level candidate — `LICENSE`, `LICENSE.md`, `COPYING`,
`license`, `License.txt`, `GPL-LICENSE.txt` — while its real licence sits at
**`docs/License.txt`** (GPL-2.0), pointed to only by a Markdown link in the
README. So the probe order that actually works:

1. root filename × extension variants;
2. if all 404, **read the README for a licence link** before recording a gap;
3. follow that link and read the payload.

Skipping step 2 produces a false "unlicensed" verdict on a correctly licensed
project — the mirror image of the false-MIT error `frappe/lms` causes. Both
failure modes now have a live example. Only after step 3 fails is "unlicensed"
a finding: that is how `DMontgomery40/mcp-canvas-lms`, `loyaniu/moodle-mcp` and
`tutornew/OpenTutor` were confirmed above, each checked against eight filename
variants on three branches *and* its README.

**A fourth axis, added 2026-10-06 (third pass): the OWNER.** A 404 or an
unlicensed verdict on `owner/name` is evidence about *that owner's repository
only* — never about the project. The second pass of 2026-10-06 withdrew this KB's
OpenTutor entry after probing `tutornew/OpenTutor` (8★, unlicensed) and the real
project was `zijinz456/OpenTutor` (**MIT, 130★, FSRS 4.5, 12 blocks, LOOM knowledge
graph**) all along. Every other probe lesson in this file guards against a false
*positive*; that one was a **false negative that deleted a true finding**, which is
the more expensive direction because the result is a confident denial rather than a
wasted probe. So: **before withdrawing an entry, enumerate the owners publishing
under that project name.** A withdrawal needs a stronger probe than an addition.

**A fifth axis: the DIRECTORY.** An open-core project can be permissive at the root
and proprietary in a subtree. `langfuse/langfuse` is MIT except `ee/`,
`web/src/ee/` and `worker/src/ee/`, which carry a separate enterprise licence — and
its copyright holder is now ClickHouse, Inc. A repo-level licence badge cannot
express that. Read the payload, note the carve-out paths, and record the copyright
holder alongside the licence so a change of holder between passes is visible.

Repo *location* needs the same care: `apereo/opencast` is a **404**, and the live
repository is `opencast/opencast` (ECL-2.0). An org-renamed project will fail a
reachability probe while the project itself is perfectly healthy — re-probe the
name before recording a gap. The converse also happens: `planejaia/OpenMAIC-Brasil`
is a confident search result for a repository that genuinely does not exist —
**re-probed on 2026-10-06 it still 404s on all four** candidate branches (`main`,
`master`, `develop`, `v1.0.0`).

**Two rules added in the fourth pass of 2026-10-06, because that last example was
read wrongly for three passes.**

1. **A 404 on a suffixed name obliges you to query the base name before you record
   a gap.** `OpenMAIC-Brasil` is absent; **`OpenMAIC` is not.** The upstream is
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — **MIT, 40.0k★,
   Tsinghua University** — now the largest permissive asset in this KB and listed
   on the core shelf above. This KB carried the absence as evidence through three
   passes while a forty-thousand-star implementation of the same idea sat one query
   away.
2. **A repository name is not a provenance claim.** `-Brasil`, `-India`, `-LATAM`
   are strings an author typed. Attribute region from the **owner account, the
   commit history or the README** — never from the slug. The no-LATAM-origin gap
   was partly argued from this filename; it has since been re-established on
   channels that do not depend on one, including a Spanish/Portuguese-language
   search (see `agents/top.md`).

**And sweep the organisation behind any interesting repository.** Topic pages rank
by stars, so they structurally hide small orgs: the `AI-for-Education` sweep in the
same pass returned six repositories, five MIT, that no topic page had ever shown
this KB — and they are the only Africa-placed code it holds.

## Added in the tenth pass of 2026-10-06 — the interoperability tier, and the sync engine under the offline platform

Two shelves this pass, both payload-verified, both arriving from a demand signal
rather than from a search for interesting code.

**All licences below were read from the repository's own payload** via
`raw.githubusercontent.com`, probed across **10 filenames × 2 branches**
(`LICENCE`/`LICENSE`/`licence`/`license`/`COPYING`, `.md` and `.txt` variants, on
`main` and `master`). The probe was validated against 6 known-payload controls
first; **6 of 6 resolved.** Star counts read from the rendered repository page the
same day.

### The interoperability tier — because 39% of district RFPs score it

The ninth pass found the procurement number: **39% of districts score
interoperability in their RFP rubrics** (CoSN, Tier 2). That makes the integration
layer a **scored deliverable**, not plumbing — and this is the entire permissive
shelf for it, split by runtime.

| Repo | License (read from payload) | ★ (2026-10-06) | Runtime | What it is |
|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 (`master/LICENSE`) | 373 | Node / TypeScript | Turns an application into a fully integratable **LTI 1.3 tool provider**. The highest-starred genuine LTI project, and the default when the AI layer is a Node service. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 (`master/LICENSE.md`, 11,343 B) | — | PHP | LTI 1.3 library published by **the standards body itself**. The reference implementation; the natural pairing when the LMS is Moodle. | 🔵 **Row re-pointed, pass 24.** This was `1EdTech/lti-1-3-php-library`, whose head commit is **2020-06-03 — 2,317 d**. The live copy of the *same* library (byte-identical payload) is the `packbackbooks` original, head commit **2026-09-23 (14 d)**. ⚠️ The 124★ figure belonged to the 1EdTech copy and is not transferable, so it is withdrawn rather than moved — no ★ was readable this pass (`github.com` and `api.github.com` are 403 here). |
| [Unicon/tool13demo](https://github.com/Unicon/tool13demo) | Apache-2.0 (`master/LICENSE`) | 27 | Java / Spring Boot | LTI 1.3 tool in Spring Boot, from a long-standing higher-ed systems integrator. **The JVM entry point** — which is the stack most enterprise education clients already run. |
| [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) | Apache-2.0 (`master/LICENSE.txt`) | 25 | Java / Spring Security | LTI 1.3 for Spring Security, built on its OAuth2 support. Use this one when the client already has a Spring Security estate and wants LTI inside it rather than beside it. |
| [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) | **MIT** (`master/LICENSE`) | 6 (8 forks) | .NET | OneRoster 1.1 and 1.2 client. OAuth2 for 1.2, consumer credentials for 1.1. **Rostering calls only — gradebook is not implemented**, which is a scope limit to check against the rubric before you promise it. |

**Three warnings on this shelf.**

1. **Pin the right OneRoster.NET.** [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET)
   is **also MIT** (`master/LICENSE`) and serves a byte-identical `README.md`
   (md5 `110b2e3439d86b6055821de382d90d61`, 2,048 bytes) and byte-identical
   licence text. **Both licences name `theopenem` as holder.** One asset, two
   addresses; the fork direction is **not established** in this environment
   (`github.com` → 403 to `curl`, no fork banner in the rendered page). Pin
   `theopenem`, whose owner matches the copyright line.
2. **"Caliper" is a homonym and it will waste a sweep.** `OneRoster OR Caliper OR
   "LTI 1.3" license:apache-2.0` returns **184 repositories**, led by
   `google/caliper` (818★, deprecated Java micro-benchmarking) and
   `hyperledger-caliper/caliper` (708★, blockchain benchmarking). Four of the top
   eight have nothing to do with 1EdTech Caliper Analytics. **The result count is
   not the ecosystem size.**
3. 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07. This said "there is no Python LTI 1.3 library
   on this shelf". It is false, and there is now a live one.** Node, PHP, Java and .NET are
   covered, and so is Python: [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) —
   **MIT** (payload 1,098 B, © The Regents of the University of Michigan), head commit
   **2026-10-05 (2 d)**, published to PyPI as [`django-lti`](https://pypi.org/project/django-lti/)
   **v0.10.1 on 2026-08-07 (61 d)**. It is **Django**-coupled. For a JupyterHub tool,
   [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) (BSD-3-Clause,
   98 d) implements LTI 1.3 **and** 1.1 and is tested against Open edX, Canvas and Moodle.
   ⚠️ **What is genuinely absent is a live *framework-agnostic* Python implementation:** the only
   framework-neutral one, `dmitry-viskov/pylti1.3`, is **1,416 days cold on the commit channel and
   1,417 on the release channel**. 🔴 And the best-maintained Python LTI 1.3 implementation of all,
   [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) (committed and
   released 6 d ago), is **AGPL-3.0** — right inside Open edX, unusable as reusable IP. So the
   contribution opening narrows from "a library" to "a framework-neutral library", and the
   adapter-in-another-runtime workaround below is **no longer required** when the AI tier is
   Django. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`.

### The Learning Equality substrate — the sync engine, not just the app

This KB has recommended offline-first delivery for three passes while recording
the *application* (Kolibri) and not the machinery under it. The organisation holds
**238 repositories**. Probed this pass:

| Repo | License (read from payload) | ★ (2026-10-06) | What it is |
|---|---|---|---|
| [learningequality/morango](https://github.com/learningequality/morango) | **MIT** (`master/LICENSE`) | 15 (23 forks) | **Pure-Python peer-to-peer database replication engine for Django.** Marks chosen application models syncable; **certificate-based authentication** protecting data privacy and integrity; change-tracking and data-partitioning constructs designed for low-bandwidth links; works on **SQLite and PostgreSQL**. Branch `release-v0.9.x`. Built for Kolibri, **usable independently** — this is the component that makes an offline-first architecture real rather than aspirational. |
| [learningequality/le-utils](https://github.com/learningequality/le-utils) | **MIT** (`main/LICENSE.txt`) | not read this pass | Constants and utilities shared across Kolibri, Ricecooker and Studio. The shared vocabulary layer; required by anything that generates Kolibri channels. |

**And the two that came back ungranted, inside that same organisation:**

| Repo | License probe result | Consequence |
|---|---|---|
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | **no payload** (20 URLs) | Vue design system. Repository exists (`main/README.md` resolves). **Do not ship client UI from it** on the assumption that the org is MIT. |
| [learningequality/kolibri-server](https://github.com/learningequality/kolibri-server) | **no payload** (20 URLs) | Performance and caching access layer for Kolibri with multi-core support. **The repository exists** — its README is `main/README.rst`, not `README.md`. **No licence payload under any of 20 URLs.** Treat as unlicensed until a payload is read. |

**Two of four new probes in the MIT-friendliest organisation on these shelves came
back ungranted.** An organisation's licence posture is not inherited by its
repositories. "They're the Kolibri people" is not a licence.

**A scope concern raised and refuted.** `learningequality/studio`
([repo](https://github.com/learningequality/studio), already on these shelves)
declares `Copyright (c) 2021 Foundation for Learning Equality (internal apps)`.
A parenthetical qualifier inside a copyright line is exactly the shape this KB
treats as a possible narrowed grant. **Full text read this pass: the permission
body is standard, unmodified MIT with no field-of-use restriction.** The
parenthetical annotates the holder, not the grant. **Full MIT** — recorded so the
next pass does not re-litigate it.

### Why these two shelves belong on the same page

Morango answers *how the data gets there* when connectivity is intermittent. The
LTI/OneRoster tier answers *how it gets into the systems the client already runs*,
against a rubric that scores exactly that. Together they are the two ends of a
delivery that an RFP can actually score — and both ends are permissive, which is
the whole reason this file exists.

## Added in the eleventh pass of 2026-10-06 — the evaluation layer, and the Python protocol layer

Licences read from each repository's own payload on `raw.githubusercontent.com` on
2026-10-06; metadata (stars, forks, `default_branch`, `fork`, `pushed_at`) from the
GitHub REST search API, reachable this pass through the session's GitHub MCP server.

**All four rows are reinstatements of addresses this repository's own reset dropped
earlier the same day** — they are in `archive/2026-10-06-pre-reset/`. See
`repos/trending.md` for the 172-address audit.

### The evaluation layer — the one infrastructure tier this KB had been describing as missing

| Repo | Licence (read from payload) | ★ (2026-10-06) | Forks | Why it is foundational |
|---|---|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** (`main/LICENSE`) | **2,945** | 779 | **Inspect**, from the **UK AI Security Institute**. A general LLM-evaluation framework: datasets → solvers → scorers, with model-graded evals, tool use and multi-turn dialog built in, and third-party Python packages able to add scoring and elicitation techniques. **This is the harness.** An education engagement supplies the dataset and the rubric; it should not supply the runner, the logging, the sandboxing or the scoring plumbing. Pushed on the day of this pass. |
| [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** (`main/LICENSE.md`) | 355 | 72 | **Moonshot**, from the **AI Verify Foundation** (Singapore IMDA's AI-testing community). Benchmarking **and red-teaming** of any LLM application in one modular tool. The red-team half has no permissive equivalent in this KB, and for an education deployment — where the adversary is a bored fifteen-year-old with unlimited attempts — it is not optional. Pushed on the day of this pass. |

**Why both, rather than one.** Inspect measures whether the system is *right*;
Moonshot measures whether it can be made to *misbehave*. Education buyers in every
region this KB tracks now ask for both, and the two licences (MIT and Apache-2.0) are
compatible with each other and with a commercial deliverable. **Neither ships any
education content** — which is exactly why they are in `foundations.md` and the
benchmarks are not.

### The protocol layer — Python

| Repo | Licence (read from payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (`master/LICENSE`, 1,070 B) | **138** | `master` | `PyLTI1p3` — **LTI 1.3 Advantage** tool implementation with Django and Flask adapters. Most AI tutoring code in this KB is Python, and LTI 1.3 is how it reaches a learner inside an institution's LMS. ⚠️ **Last push 2024-08-18**: treat as a stable protocol library, pin the version, and budget for maintaining your own fork if the spec moves. |
| [Pearson-Advance/openedx-lti-tool-plugin](https://github.com/Pearson-Advance/openedx-lti-tool-plugin) | **Apache-2.0** (`main/LICENSE`) | 5 | `main` | Makes an **Open edX** instance act as an LTI 1.3 *tool*, so an existing Open edX estate can be consumed by another institution's LMS rather than replaced. Pushed 2026-09-11. |

### A probe-set correction that belongs in this file

Every licence in `foundations.md` is read from a payload URL, and a payload URL needs
a branch. The tenth pass probed `main` and `master`. **Read `default_branch` from the
API instead**: this pass found a 2,320★ platform on `dev` (`learnhouse`), a 718★
platform on `2.12` (`portabilis/i-educar`) and one repository on
`deployment/playstore`. On a `main`+`master` probe all three read as **ungranted**,
and two of them are merely **copyleft** — a delivery constraint, not an absence.

## Added in the twelfth pass of 2026-10-06 — the xAPI/LRS tier, the Ed-Fi stack, and the Apache-2.0 seam inside an AGPL platform

Every branch below came from `git ls-remote --symref … HEAD` and every licence from the
`raw.githubusercontent.com` payload on that branch, on 2026-10-06. No licence here was
taken from a sidebar, a badge or an organisation-level assumption — the
`aiverify-foundation` rows are the reason why: two repositories in that organisation are
Apache-2.0 and a third, in the same org, carries no licence at all.

### The row that changes platform strategy — Open edX's plugin SDK is Apache-2.0

| Repo | Licence (payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** (`master/`**`LICENSE.TXT`**) | **470** | `master` | The **XBlock SDK** — the component and plugin API every Open edX course component is written against. Python. |

**This matters out of proportion to the row.** Open edX's platform core
(`openedx/edx-platform`) is **AGPL-3.0**, and this KB has correctly priced the platform
as copyleft since its first pass. But the surface a studio actually writes on — a
client-specific interactive component, an AI tutor delivered inside a course, a
proctoring or analytics side-car — is an **XBlock**, and the XBlock SDK is
**Apache-2.0**. A component built against it is **your** component: Globant can build,
keep and redistribute it without inheriting the platform's AGPL obligations, provided it
stays a plugin and is not linked into the platform tree. The LATAM `TutorIA`
specification already on this KB's agent shelf specifies exactly this shape — *"delivered
as an Open edX XBlock/plugin"* — and this row is the licence evidence that the shape is
sound.

⚠️ **The boundary is the deliverable, not the repository.** AGPL-3.0 reaches anything
that becomes part of the platform process in a way that creates a derivative work; it
does not reach a separately licensed plugin consumed through a published plugin API. Get
the packaging reviewed before you promise a client a proprietary component — the
distinction is the whole engagement, and it is a legal review, not a licence-file read.

*Found at `LICENSE.TXT` — uppercase extension. A nine-name lowercase probe reports this
repository as ungranted; see the 13th failure mode in `agents/top.md`.*

### The xAPI / LRS tier — the learning-analytics half, recovered

The eleventh pass declared the learning-analytics side of the interoperability tier
behind a membership, on the evidence of Caliper. **That is true of Caliper and false of
xAPI.** xAPI's tooling is permissive and alive:

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** (`master/LICENSE`) | **77** (52 forks) | `master` | **The conformance instrument.** Node.js suite that tests an LRS against the **MUST** requirements of the xAPI specification. From **ADL** (Advanced Distributed Learning, the US Department of Defense initiative that authored xAPI). This is how you *prove* an analytics deliverable conforms rather than asserting it — and in a procurement where interoperability is a scored line item (trend 28), a conformance run is the evidence. |
| [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | **Apache-2.0** (`master/LICENSE`) | **60** (33 forks) | `master` | The **xAPI Profiles specification** — structure, communication and processing — plus context, library and ontology files. ADL also runs a public profile index at `xapi.vocab.pub`. The vocabulary layer: what a statement *means*, not just how it is transported. |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | **Apache-2.0** (`main/LICENSE`) | 17 (9 forks) | `main` | **LRSPipe** — xAPI statement forwarding and middleware, governed directly by xAPI Profiles. Clojure. ⚠️ **The product name is not the repository name**: `yetanalytics/lrspipe` is a 404 and this KB recorded that false negative twice. Pin the address, not the brand. |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | An LRS implementation. The store at the end of the pipe. |

**What this adds up to:** a permissive xAPI chain exists end to end — **profile**
(vocabulary) → **pipe** (transport and transformation) → **LRS** (store) →
**conformance suite** (proof). All four are MIT or Apache-2.0. An analytics deliverable
can be built, kept and redistributed by Globant on this chain. **Caliper cannot be, and
xAPI can** — and the two standards are not interchangeable, so this is a design decision
to make at proposal time, with the licence as one of the inputs.

### The Apereo learning-analytics tier — permissive, under a licence the filter misses, and dormant

| Repo | Licence (payload) | ★ | Branch | State |
|---|---|---|---|---|
| [Apereo-Learning-Analytics-Initiative/OpenLRS](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | **ECL-2.0** (`master/LICENSE`) | 47 (38 forks) | `master` | 🔴 **Archived by the owner on 2019-01-31, read-only.** Superseded by OpenLRW; the README says all new development moved there. |
| [Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |
| [Apereo-Learning-Analytics-Initiative/OpenDashboard-api](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |

🆕 **ECL-2.0 is the Educational Community License 2.0, and it belongs in this KB's
permissive set.** It is **OSI-approved** and it is **Apache-2.0 with one modification**:
the patent grant is narrowed so that a contributing university licenses patents only for
the contributed work, not across its whole portfolio — written precisely so that
universities could contribute to open source without their technology-transfer offices
blocking it. For redistribution and commercial use it behaves like Apache-2.0.

**This is trend 15 — "permissive is a bigger set than MIT, Apache, BSD" — with the
education sector's own licence as the example.** A `license:mit OR license:apache-2.0`
filter rejects the entire Apereo estate, and Apereo is the consortium behind Sakai and
much of higher education's shared infrastructure. **Add `ECL-2.0` to the permissive
allow-list.**

⚠️ **And then do not adopt these three anyway.** The licence is fine; the code has been
read-only since January 2019. They are a **reference architecture and a vocabulary
source**, and the live permissive alternative is the ADL/Yet Analytics xAPI chain above.
The useful lesson is the licence, not the repositories.

### The Ed-Fi stack — Apache-2.0, and the US K-12 data standard

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** (`v6.2.0/LICENSE`) | 46 (13 forks) | 🆕 **`v6.2.0`** | The **Ed-Fi Data Standard** — the schema that enables interoperability among US K-12 education data systems. Latest release v6.2.0, which is also the default branch. |
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | **OneRoster** over Ed-Fi — rostering interoperability, the 1EdTech standard that *did* stay open. |
| [Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Integration with **Clever**, the rostering provider most US districts actually run. The bridge between the standard and the installed base. |

**Why this is the North America procurement asset.** US K-12 procurement increasingly
scores interoperability directly (trend 26, trend 28), and Ed-Fi is the standard those
rubrics name. The schema, the OneRoster bridge and the Clever integration are all
**Apache-2.0**. ⚠️ **The MCP side-car is gone**: `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` is
recorded in this repository's archive and no longer resolves. Agent access to Ed-Fi over
MCP is a **build**, and it is a well-shaped, small one — the schema is published and
permissive.

*The default branch here is `v6.2.0`. This is the cleanest example in the KB of why the
branch must be read rather than guessed: the Apache-2.0 licence of the US K-12 data
standard is invisible to a `main`+`master` probe.*

### The interoperability tier — Python and Java LTI 1.3, measured exhaustively

The tenth pass declared *"no Python LTI 1.3 library exists on the permissive shelf"*;
the eleventh pass refuted it from this repository's own archive. This pass **measured the
whole tier** with the MCP search API — `lti 1.3 advantage language:Python` →
**`total_count: 4`**, which is the complete set, not a page of it:

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (1,070 B) | **138** (83 forks) | `master` | **The only viable one.** Django and Flask adapters. ⚠️ **51 open issues**, last push 2024-08-18. |
| [blackboard/BBDN-lti-1p3-tool-example](https://github.com/blackboard/BBDN-lti-1p3-tool-example) | **Apache-2.0** (`main/LICENSE`) | 1 | `main` | 🆕 **Blackboard's own** Python/Flask LTI 1.3 example with AWS deployment. A vendor-authored reference — useful for reading how a major LMS expects a tool to behave. Last updated 2022. |
| [glenn-watt/lti-1p3-reference-tool](https://github.com/glenn-watt/lti-1p3-reference-tool) | **MIT** (`main/LICENSE`) | 0 | `main` | 🆕 Flask reference tool implementing **OIDC, JWKS validation, AGS, NRPS and Deep Linking from first principles**. 0★ and three months old, so it is **code to read**, not a dependency — but it is the only one that covers all four LTI Advantage services explicitly. |
| [CNIT-Organization/ltitoolkit](https://github.com/CNIT-Organization/ltitoolkit) | **MIT** (`main/LICENSE`) — ⚠️ **the holder is `Dmitry Viskov`, not this project** | 0 | `main` | 🔴 **REWRITTEN, twenty-fifth pass of 2026-10-07 — this row said "PyPI-published" and that is wrong under this name.** `pypi.org/pypi/ltitoolkit` is **404**; the package is published as **[`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) 0.1.0, uploaded 2026-06-26 (103 d), one release ever**, and the repo's own README says *"Published via Git (no PyPI required)"*. **And the row omitted the only thing about it that matters: its `src/ltitoolkit/core/` is, in its README's words, the "vendored LTI 1.3 engine (PyLTI1p3, rebranded)".** See the correction block below. |

🔴 **CORRECTED, twenty-fifth pass of 2026-10-07 — two figures in the table above were
stale and the row that resolves the tier was mis-described.**

⚠️ *"has not been pushed since August 2024"* is wrong: `dmitry-viskov/pylti1.3`'s head commit
is **2022-11-21**, measured over `git` by pass 23 and re-measured this pass, and its last PyPI
release, `pylti1p3` **2.0.0**, is **2022-11-20**. Both channels agree and both are **1,416
days**. Pass 24 published the right figure in `agents/trending.md` and this table kept the
wrong one — the third reproduction of the propagation failure recorded in `intel/market.md`.

🟢 **And the KB's own answer to its most-repeated supply gap was already sitting in the last
row of this table.** Pass 24 spent its headline establishing that *"the only framework-neutral
Python LTI 1.3 implementation (`pylti1.3`) is abandoned on both channels"*. Measured this pass
by the **licence-holder channel** — `CNIT-Organization/ltitoolkit` ships a `LICENSE` whose
holder is `Dmitry Viskov`, which is the fork signal trend 56 defines — and then confirmed by
opening its README:

> `src/ltitoolkit/core/   # vendored LTI 1.3 engine (PyLTI1p3, rebranded) — internal`

**So the framework-agnostic path is not dead; it is early.** The honest shelf:

| | `ff-ltitoolkit` (`CNIT-Organization/ltitoolkit`) |
|---|---|
| licence payload | 🟢 MIT (`main/LICENSE`) |
| ⚠️ licence **holder** | 🔴 `Dmitry Viskov` — **the vendored engine's holder, carried over.** The repo publishes **no grant naming its own authors** for the new code |
| PyPI | 🟢 `ff-ltitoolkit` **0.1.0**, 2026-06-26, **103 d** — the only release |
| head commit | ⚠️ **2026-08-05, 63 d** — alive, but two months without a commit on a project whose README says three of its five subsystems *"are being built"* |
| scope today | 🟢 OIDC/JWT launch, AGS, NRPS, Deep Linking, Dynamic Registration declared; 🔴 **FastAPI adapter, Dynamic Registration and token minting are Phase 2–5, unbuilt** |
| declared status | 🔴 *"early development (v0.1.0)"*, `Development Status :: 3 - Alpha` |

🔵 **The sentence that replaces trend 28's, narrower and finally true in three directions:**
the **Django** path is alive (`academic-innovation/django-lti`, MIT, 2 d); the **JupyterHub**
path is alive (`jupyterhub/ltiauthenticator`, BSD-3-Clause, 98 d); and the **framework-agnostic**
path is a **single 0★ alpha that vendors the abandoned library rather than replacing it**, with
one release and no grant of its own. **Read as a procurement answer that is better than "there
is none" and much weaker than "there is one."** If an engagement's LMS integration is on the
critical path and the tool is not a Django app, budget for maintaining the vendored engine
yourself — the alpha has already done the vendoring, which is the work, and has not yet done
the adapters.

⚠️ **One figure in the table above is left as published and should not be re-used:** the
`total_count: 4` came from the MCP search API, which this environment no longer reaches.
`ff-ltitoolkit` is reachable only through PyPI and `git`, and `pypi.org/pypi/ltitoolkit` is a
404 — **a tier census run by repository search would have missed the package name entirely.**

**The Java side is healthier, and it is EMEA-placed:**

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) | **MIT** (`master/LICENSE`) | 8 (12 forks) | `master` | **EMEA / Spain** — a working LTI Advantage tool webapp built on the LTI libraries of the **Universitat Oberta de Catalunya**, a large European distance-learning university. The Java counterpart to `pylti1.3`, carrying a European institution's own production lineage. |

### The assessment-standards tier — QTI, and an ISC licence from a commercial vendor

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🆕 **ISC** (`master/LICENSE`, © 2026 **Renaissance Learning**) | 4 (1 fork) | `master` | **QTI player for 2.1, 2.2 and 3.0**, plus bidirectional QTI ↔ PIE transforms with a CLI for batch conversion. Ships an item player and a multi-item assessment player. TypeScript. |
| [Citolab/qti-convert](https://github.com/Citolab/qti-convert) | **GPL-3.0** (`main/LICENSE`) | not read this pass | `main` | QTI conversion tooling from **Cito** (the Dutch national assessment institute). Real and maintained — but GPL-3.0, so a conversion step built on it is a copyleft deliverable. |

🆕 **ISC belongs on the permissive allow-list too.** It is OSI-approved and functionally
equivalent to MIT — a two-clause permission grant with no added conditions — just shorter.
A `license:mit OR license:apache-2.0 OR license:bsd` filter misses it.

**And note who holds the copyright: Renaissance Learning**, a commercial assessment
vendor, publishing a QTI player under ISC. Trend 7 has called assessment "the regulated
frontier and the tooling gap" for eleven passes. The gap is narrower than that on the
**standards-conformance** side: a permissive QTI player exists, at 4★, from a vendor
with a real assessment business. It is still wide on **AI-generated grading**, where
`license:apache-2.0` + automated rubric grading measures **`total_count: 0`** this pass
and the only permissive answer in this KB remains `Selleo/mentingo` (MIT).

### Classroom-discourse and research infrastructure

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | **MIT** (`main/LICENSE`) | 117 (16 forks) | `main` | Stanford NLP: anonymise → annotate → analyse classroom talk. Full entry in `agents/top.md`. |
| [EduNLP/EduCoder](https://github.com/EduNLP/EduCoder) | **MIT** (`main/LICENSE`) | 3 | `main` | Human-vs-LLM transcript annotation workspace. Full entry in `agents/top.md`. |
| [jupyterhub/jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) | **BSD** (`master/LICENSE`) | not read this pass | `master` | 🆕 **Absent from every earlier pass of this KB**, live or archived, except one archive mention. Reference deployment of **JupyterHub for a teaching environment** — the standard way CS and data-science courses give every student a server-side notebook. BSD. The infrastructure layer under any coding-course engagement. |
| [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | **Apache-2.0** (`main/LICENSE`) | 98 (32 forks) | `main` | **APAC / Singapore** — AI governance *testing framework* from the **AI Verify Foundation** under **IMDA**, validating AI systems against internationally recognised principles through standardised tests. The compliance-evidence instrument for an APAC deployment, built by the regulator's own foundation. |
| [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Plugin and test-widget development kit for AI Verify. How you add an **education-specific** test to a government-recognised harness. |
| [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | **Apache-2.0** (`main/LICENSE.md`) | not read this pass | `main` | Test assets, datasets, metrics and attack modules for Moonshot (the red-teaming/benchmark harness already on this shelf). |
| `aiverify-foundation/LLM-Evals-Catalogue` | 🔴 **ungranted** | — | `main` | **No licence file**, under 30+ name variants on the real default branch. A catalogue of LLM evaluations — the index, not the code. **Treat as reading material, cite it, do not vendor it.** Three repos in one government foundation's organisation: two Apache-2.0, one ungranted. |

### One correction to this KB, with the payload as evidence

The 123rd-pass note in `repos/trending.md` records:

> *"Discrepancia registrada sin normalizar: el `LICENSE` de `edrys` mide 16.724 B y la
> AGPL íntegra mide ~34–35 KB en este corpus — es AGPL ABREVIADA."*

🔴 **`edrys-org/edrys` is `MPL-2.0`, not an abbreviated AGPL.** Read this pass from
`main/LICENSE` (16,725 B): the first line is **`Mozilla Public License Version 2.0`**,
and the full MPL-2.0 text is ~16.7 KB — the size is not a truncated AGPL, it is a
complete MPL. The only occurrence of "Affero" in the file is inside **MPL §1.12's
secondary-licence definition**, which names the LGPL and AGPL as compatible licences.
That boilerplate is what a substring search found.

**This changes the delivery constraint, not just the label.** MPL-2.0 is **file-level
weak copyleft**: modified MPL files must stay MPL and be published, but the work can be
combined with proprietary code in a larger program without that program becoming MPL.
AGPL would have added a network-use obligation that MPL has none of. `edrys` — a
live-classroom platform — is therefore **usable in a mixed-licence deliverable** with
per-file discipline on the files you touch. It was priced as unusable.

**The method lesson is the general one:** a size comparison identifies a *discrepancy*,
and only the first line of the payload identifies a *licence*. Size told pass 123 to look
again, which was right; it then answered the question it had only raised.

## Added in the thirteenth pass of 2026-10-06

One row, and it is on this shelf rather than the education shelf for a reason.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [bonafe/inteligencia-aberta](https://github.com/bonafe/inteligencia-aberta) | **MIT** (`LICENSE`) | reference architecture | **Not education software.** A Brazilian civic-analysis agent platform (Bonafé · Américo, 2★, Python) whose *stack* is the one this KB keeps assembling by hand for a sovereign deployment: **FastAPI + LangGraph + PostgreSQL + Qdrant, in Docker, multi-tenant, deployable locally and federating across machines**. Read it as a **worked reference for the LATAM sovereign pattern**, not as a component to ship. Its design goals — end-to-end source traceability, user control over what is shared, voice and natural-language access for low-literacy users — are the same requirements an education deployment under LATAM constraints carries, written out by someone who shipped them. |

### Why a 2★ repository is worth a row

Because this shelf's job is to answer *"what do we build on"*, and the scarce thing in a
sovereign education build is not a component — every component here is permissive and
available — it is a **worked wiring of them that someone has already debugged**. This KB
has four patterns (P4, P5, P26, P32) that specify a LATAM or data-residency stack
component by component. `inteligencia-aberta` is an independent implementation of
substantially that stack, by Brazilian authors, under MIT, with the traceability
requirement treated as a first-class design goal rather than an afterthought.

⚠️ **The star count is the correct signal to ignore here, and the fork count is the one to
watch.** It has **2 stars and 0 forks** — nobody has deployed it. Use it as a design
reference and a code read; do not present it to a client as a maintained dependency.

### What this pass did not add, and why

🔴 **No new serving, orchestration or retrieval layer was found.** The mandatory
infrastructure query (`open source platform education ERP CRM MIT Apache`) returned
**OpenEduCat, RosarioSIS, openSIS, Gibbon and Fedena** — *five returned, five already
inventoried on the SIS/ERP shelf in `verticals/solutions.md`*. That is the **fourteenth
consecutive pass** in which the generalist infrastructure query has returned zero new
rows, and it is now safe to say what that means: **the foundational layer for an education
build is saturated and stable.** The scarcity has moved entirely to the education-specific
layer above it, which is where the last several passes have correctly been spending their
probes.

🔴 **The non-GitHub forge channel could not be opened.** `codeberg.org`, `gitee.com` and
the European Commission's Joinup/OSOR catalogue are all **unreachable from this
environment** (403 at the egress proxy). Every licence fact on this shelf rests on
`raw.githubusercontent.com`, which is the only code-hosting payload this environment can
read. Two named Codeberg education projects were surfaced and **deliberately not shelved**,
because they could not be payload-verified. Full measurement in `agents/trending.md`,
Finding 4.

## Added in the fourteenth pass of 2026-10-06 — the sandbox layer, and the index that is not a shelf

One infrastructure row, and it is the highest-starred find of the whole pass. It arrived
through the platform-name channel (`agents/trending.md`, fourteenth pass) as a by-product:
searching for education platform integrations surfaced the layer underneath the one thing
education software does that no other industry's software does — **run a student's code**.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [taybenlor/runno](https://github.com/taybenlor/runno) | **MIT** (`LICENSE`, 1,106 B; © Benjamin Taylor) | code sandbox | **773★.** Runs code in many languages inside a **WebAssembly/WASI sandbox** — in the browser with no server, or in Node. Four published packages, all **MIT on npm**: `@runno/runtime` 0.10.0 (web components for runnable examples), `@runno/sandbox` 0.10.2 (secure sandbox for Node and other JS runtimes), `@runno/wasi` 0.10.0 (isomorphic WASI runner) and 🆕 **`@runno/mcp` 0.10.6 — the sandbox exposed as an MCP server**. |

### Why this is a foundations row and not a curiosity

Every CS-education pattern in this KB has had the same unsolved component: **where does the
student's code run?** The existing answers on this shelf are JupyterHub (a multi-user server
per cohort) and OpenHands (a coding agent with its own sandbox). Both are servers you operate.

Runno moves execution **into the learner's browser**, which changes three things an education
engagement is costed and audited on:

- **Data residency becomes trivial for the execution step.** Student code never reaches a
  server, so there is no execution-side transfer to document in an EMEA deployment. The
  sovereignty argument this KB makes with Ollama for inference, Runno makes for execution.
- **Per-seat cost goes to zero and scales with the cohort's own devices.** No container per
  student, no idle notebook servers — the LATAM and offline-first cost constraints in P5
  apply to execution too, and this is the component that answers them.
- 🆕 **`@runno/mcp` makes the sandbox agent-callable**, which is the piece that was missing:
  a tutor agent can now *execute* a learner's submission and reason about the actual output
  rather than predicting it. Pair it with the auto-grading assets in `agents/top.md`
  (fourteenth pass) and the grading loop has a real execution step under a permissive licence.

⚠️ **Two limits to state before it enters a proposal.** WASI sandboxing covers languages
with a WASI target — check the language a client's curriculum actually teaches against the
published package list rather than assuming coverage. And a browser sandbox is **not** an
anti-cheat boundary: it protects the host from the code, not the assessment from the student.
For proctored assessment the execution still belongs server-side.

### The MCP Registry — an index this KB now uses, and what it is not

`registry.modelcontextprotocol.io` is reachable here and was measured first-hand this pass
(method, traps and counts in `repos/trending.md`, fourteenth pass). It belongs on this page
only as a **channel**, never as a dependency:

- **11,505 unique servers** across 31,300 version rows — a record is not a server, and the
  figure is a **floor** because the page loop ended early.
- **102 education-vocabulary servers, of which 71 (70%) ship no source repository.** It is a
  catalogue of hosted endpoints with open-source entries mixed in, not a source shelf.
- 🔴 Its `?q=` parameter returns **HTTP 200 and the unfiltered page** — a silent no-op. Do
  not quote a count from it.
- 🔴 One listed server's repository **no longer exists**. A registry entry is not an
  existence proof; `ls-remote` still is.

**The rule for this page:** the registry is a good place to *find* candidates and a
disqualifying place to *source* them. Nothing enters this shelf from a registry listing
without an `ls-remote` resolution and a licence payload on its real default branch.

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS client layer, and why it belongs in *this* file

The assets found this pass are not education products and they are not agents. They are the
**client libraries that speak a student information system's protocol** — the layer an
education agent stands on when the engagement is administrative rather than instructional.
Full rows, stars and country placement in `agents/top.md` (fifteenth pass). This file records
what they are *for*, and the two things that decide whether you may use them.

Licences read from each repository's own payload on 2026-10-06; default branches confirmed
with `ls-remote --symref`.

### The layer, by protocol family

| Repo | Licence (payload) | Language | Speaks to |
|---|---|---|---|
| [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** | Python | PRONOTE (FR) |
| [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | **BSD-2-Clause** | Python | WebUntis (DE/AT) |
| [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **MIT** | Node.js | PowerSchool (US) |
| [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | **MIT** | Python | PowerSchool (US) |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | **MIT** | PHP | PowerSchool (US) |
| [`magister-api/magister`](https://github.com/magister-api/magister) | **MIT** | PHP | Magister 6 (NL) |
| [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | **MIT** | TypeScript | SOMtoday (NL) |
| [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | **MIT** | PHP | SUAP (BR) |
| [`Projeto-SIAC/suap-wrapper`](https://github.com/Projeto-SIAC/suap-wrapper) | **MIT** | Node.js | SUAP (BR) |
| [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | **MIT** | Python | SIGAA (BR) |
| [`untisapi/untis4j`](https://github.com/untisapi/untis4j) | ⚠️ **LGPL-3.0** | Java | WebUntis (DE/AT) |
| [`shinyquagsire23/InfiniteCampusAPI`](https://github.com/shinyquagsire23/InfiniteCampusAPI) | ⚠️ **WTFPL v2** | Java | Infinite Campus (US) |

🟢 **Ten of the twelve are MIT or BSD, and together they cover six countries in four
protocol families.** Measured by *placed* permissive infrastructure, this is the broadest
single shelf this KB has added in one pass.

### ⚠️ Two warnings, and the second one is the reason this shelf is not a green light

**1. The licence is not the binding constraint here. The vendor's Terms of Use is.**

Every library above talks to a **proprietary, closed SIS**. The MIT grant covers the client
code; it says nothing about whether you may call the endpoint. The tier documents this
itself — `GeovaneSchmitz/sigaa-api` describes itself as *"uma biblioteca de **Web
Scraping**"*, `kc0506/ntucool` as *"**unofficial** … use it at your own risk"*, and
`chrischall/infinitecampus-mcp` quotes Infinite Campus's ToU forbidding access *"by any
means other than our publicly supported interfaces (for example, scraping or using the
content to train artificial intelligence software)"* before stating that it does exactly
that. Full treatment in `agents/top.md`, Finding 2; the gate that operationalises it is
**P26** in `compose/patterns.md`.

🔵 **The practical rule: these libraries are excellent for a prototype, a migration, or a
one-off data rescue the institution itself authorises — and they are not a production
integration path unless the institution holds an API agreement with its vendor.** When it
does, the same libraries become legitimate, because the institution's own credentials and
contract cover the access. **The asset is fine. The access needs paperwork.**

**2. Three licence shapes on this shelf would fail an automated allowlist, two of them
wrongly.**

- ⚠️ **`WTFPL v2`** (`shinyquagsire23/InfiniteCampusAPI`, 474 B payload, Sam Hocevar
  copyright) — maximally permissive in effect, **not OSI-approved**, and rejected by name by
  many corporate allowlists. Usable in substance; expect to justify it, and expect some
  clients to refuse it on the name alone.
- ⚠️ **`LGPL-3.0`** (`untisapi/untis4j`) — the middle path this KB already documents for
  OpenEduCat: dynamic linking keeps your code yours, modifications to the library itself must
  be published.
- 🔴 **`CC BY-NC-SA 4.0`** (`Jona-Zwetsloot/Somtoday-Mod`) — **NonCommercial. Not usable in
  client work at all**, and a content licence applied to software besides.

⚠️ **And read these families with the shared classifier, not a fresh one.** This pass's
from-scratch probe script mislabelled four payloads on this shelf as
Creative Commons/NonCommercial — three GPL-3.0 and one AGPL-3.0 — because GPL-3.0 §6 contains
the word *"noncommercially"*. 🟢 **`compose/code/lib/license_family.sh` already gets all of
them right**, because it gates the Creative Commons branch on a CC marker before reading
NonCommercial as an attribute. **Source the library.** See `agents/top.md`, method note 2.

### The costliest absences on this shelf

| Repo | ★ | Why it matters |
|---|---|---|
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **214** | The JavaScript WebUntis client, highest-starred ungranted asset in the tier. 6 filenames probed on `master`: **nothing**. |
| [`Litarvan/pronote-api`](https://github.com/Litarvan/pronote-api) | 192 | The multi-language PRONOTE API. **Ungranted.** `pronotepy` (MIT, 241★) is the answer for Python. |
| [`IFRN/suapi`](https://github.com/IFRN/suapi) | 28 | ⚠️ Published by the **federal institute that operates SUAP** — and ungranted, while an individual's client is MIT. One file, one commit, a public institution: **the most answerable upstream ask in this pass.** |
| [`NCSIS/InfiniteCampus-Vendor-Integration`](https://github.com/NCSIS/InfiniteCampus-Vendor-Integration) | 13 | Vendor-integration PowerShell, ungranted. |

🔵 **Pattern across all four: the ungranted assets cluster at the *most useful* layer** — the
general-purpose client and the official-institution publication — while the permissive ones
are language-specific ports and student tools. The same shape this KB recorded in the Canvas
MCP cluster, now reproduced in a completely different tier.

### What this adds to the architecture menu

The interoperability tier added in the tenth pass (OneRoster, Ed-Fi, xAPI/LRS) and this
client layer answer the **same** question by **different** routes, and the difference is
entirely about who authorised the access:

| Route | Grant on the code | Grant on the data | Use it for |
|---|---|---|---|
| **Official API** (OneRoster / Ed-Fi, permissive implementations already shelved) | permissive | **the institution's contract with its vendor** | 🟢 production |
| **SIS client library** (this shelf) | permissive (10 of 12) | ⚠️ **none — often contrary to vendor ToU** | prototype, migration, authorised rescue |

🟢 **Read together, they are the strongest architectural recommendation this KB can make for
an administrative engagement: prototype on the client library to prove the workflow in days,
then ship on the official API path.** The prototype is cheap and the production path is
contractual, and conflating them is how an engagement discovers in month three that its
integration was never licensable.

---

## Added in the sixteenth pass of 2026-10-06 — the national curriculum tier, and a licence family this KB had no row for

The ministry channel (`repos/trending.md`, sixteenth pass) produced an infrastructure tier this
KB has described as *assumed* in two patterns and never shelved: **the national curriculum, as
a machine-readable service, with a written commercial grant.**

### The curriculum-data tier

| Repo | Branch | Licence (read from payload) | Bytes | What it gives you |
|---|---|---|---|---|
| [`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL) | `main` | 🟢 **NLOD** (`LICENSE.md`) — **commercial use granted in writing** | 1,783 | Norway's national curriculum (**LK20**) as **queryable RDF over a SPARQL endpoint, in production since 7 Dec 2020**. Competence aims, subjects, programmes, cross-curricular topics — addressable, not scraped. |
| [`Utdanningsdirektoratet/KL06-LK20-public`](https://github.com/Utdanningsdirektoratet/KL06-LK20-public) | `master` | 🔴 **NO-PAYLOAD** (30+ filename variants) | 0 | Documentation of the revised **Grep-data interface** for the LK20 reform, plus example files. The live service's own docs are in the repo wiki. |
| [`fnshr/kyo-kan`](https://github.com/fnshr/kyo-kan) | `master` | 🟢 **CC0-1.0** | 6,555 | Japan's **MEXT official kanji-by-grade tables** (*gakunenbetsu kanji haitōhyō*) as structured open data. Small, and the only MEXT-derived asset found. |
| [`NKAmapper/school2osm`](https://github.com/NKAmapper/school2osm) | `master` | 🟢 **CC0-1.0** | 6,555 | Extracts every school from Norway's **National School Register (NSR)**. An institution roster, free of restriction. |

### The education-microdata tier (LATAM)

| Repo | Branch | Licence (read from payload) | ★ | What it gives you |
|---|---|---|---|---|
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | `main` | 🟢 **MIT** — ⚠️ declared in **`DESCRIPTION`**, not `LICENSE` | 15 | **CRAN** package v1.2.0.9000. Download + process **INEP** microdata: Censo Escolar, ENEM, SAEB, Censo da Educação Superior, ENADE, ENCCEJA, IDD, CPC, IGC, CAPES, FUNDEB. **Eleven national instruments behind one MIT API.** |
| [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | `main` | 🟢 **MIT** (1,072 B) | 1,805 | 70 Brazilian public APIs as MCP tools, 13 of them education. 🟢 **Canonical — identity settled in the seventeenth pass** (root-commit comparison; `dasgltd/mcp-brasil` is a 0★ fork of this address). |
| [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) | `master` | 🔴 **GPL-2.0** (18,025 B) | 45 | Civil-society open-data API over INEP. ⚠️ **Created 2014** — treat as reference, not as a dependency, and note it is *not* INEP's own. |
| [`lucasmation/microdadosBrasil`](https://github.com/lucasmation/microdadosBrasil) | `master` | 🔴 **NO-PAYLOAD** | 174 | Reads Brazilian public microdata (CENSO, PNAD). The most-starred of this group and the one you cannot use. |

### 🟢 NLOD belongs on this KB's permissive allow-list — in the data tier

The twelfth pass added **ECL-2.0** and **ISC** to the allow-list because the standard
"MIT/Apache/BSD" filter rejected two licences that are permissive in substance. **NLOD is the
same correction, one tier down: it governs data, not code.**

Quoted from the payload (the licence ships bilingually, Norwegian and English):

> *"You are allowed to copy and make available, change and/or merge data sets described here
> with other data sets, and **to use them for commercial purposes**."*

| NLOD condition | What it costs a Globant deliverable |
|---|---|
| Attribution in a prescribed string — *"Contains data under NLOD, made available on data.udir.no"* | 🟢 A footer line. |
| **The Udir logo may not be used** without a separate agreement | 🟢 Trivial — and a trap only if a designer drops a ministry crest into a client deck to imply endorsement. |
| Data must not be presented misleadingly, distorted or misrepresented | 🟢 Already required by the EU AI Act transparency duties this KB tracks. |
| No liability for errors in the data | ⚠️ Real: a curriculum-alignment claim you make is **yours**, not the ministry's. Budget a validation step. |
| **No share-alike. No non-commercial clause.** | 🟢 **This is the whole point.** The output is yours to license as you wish. |

⚠️ **Read the boundary precisely, because it is easy to overclaim.** NLOD grants the **data**.
`Grep_SPARQL` is *documentation of an endpoint* — there is no substantial codebase to vendor.
The SPARQL client, cache, mapping layer and item generator are yours to write or to take from
the permissive shelves above.

### The public-sector application tier — permissive, and read correctly

| Repo | Branch | Licence (read from payload) | What it is |
|---|---|---|---|
| [`Utdanningsdirektoratet/PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public) | `master` | 🟢 **Apache-2.0** (11,325 B) | The openly published portion of Norway's **national exam administration system**. A ministry's production exam code, patent-granted. |
| [`Utdanningsdirektoratet/designsystem`](https://github.com/Utdanningsdirektoratet/designsystem) | `main` | 🟢 **MIT** (1,079 B) | The directorate's design system, on top of `digdir/designsystemet`. Active 2026-10-02. **A government-grade accessible component set for education UIs.** |
| [`Utdanningsdirektoratet/xmldataimport`](https://github.com/Utdanningsdirektoratet/xmldataimport) | `master` | 🟢 **MIT** (1,079 B) | Loads XML test data into SQL Server for data-driven automated tests. |
| [`Utdanningsdirektoratet/PAS-scoop-public`](https://github.com/Utdanningsdirektoratet/PAS-scoop-public) | `master` | 🟢 **Apache-2.0** (11,357 B) | Scoop bucket for the PAS toolchain. |
| [`Utdanningsdirektoratet/VFKL`](https://github.com/Utdanningsdirektoratet/VFKL), `VFKL_rebase` | `main` | 🟢 **MIT** (1,063 B) | ⚠️ **Both archived**, and the copyright holder is **Altinn** (Norway's national digital platform), not Udir — a cross-agency reuse worth knowing about, and a holder-mismatch of the kind `p184` exists to catch. |
| [`Utdanningsdirektoratet/pifu`](https://github.com/Utdanningsdirektoratet/pifu) | `master` | 🔴 **NO-PAYLOAD** | **PIFU** — Norway's person-data/rostering flow spec for education. ⚠️ **The interoperability tier's Norwegian entry, and it is ungranted.** |

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

The tenth pass shelved the interoperability tier and the twelfth pass the xAPI/LRS tier, both
on the finding that **39% of district RFPs score interoperability**. Both shelves were built
from *vendor-neutral standards bodies*. This one is built from **a state**, and it answers a
question those could not:

🔵 **In Norway, "curriculum-aligned" is a verifiable claim rather than a marketing one** — there
is a government endpoint to align *against*, and a licence that lets you bill for the
alignment. In every other country this KB covers, P15 and P16 have had to **assume** such a
source exists. ⚠️ **The sixteenth pass measured that it usually does not:** France publishes
teachers' material and no ministry estate, Japan publishes PDFs plus a CC0 kanji table, the
Gulf publishes nothing findable. **Norway is the exception that shows what the other four are
missing** — and `P25` is written so the Norwegian case is the reference implementation and the
others are a documented substitution.

---

## Added in the seventeenth pass of 2026-10-06 — a national standard you can lift, and a national estate you cannot

The channel was the **ministry tier as `org:`**. Two agencies had an estate; they split along a
line that decides how each one enters an engagement.

### 🟢 The permissive row — a national interoperability standard, Apache-2.0

| Repository | Branch | Licence (payload-verified) | ★ | Why it belongs on this shelf |
|---|---|---|---|---|
| [`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api) | `main` | 🟢 **Apache-2.0** (`LICENSE`, 11,339 B, full text) | 5 | **Reference implementation of SS 12000**, the Swedish national standard for information exchange between school administration systems — published by the national agency itself, Java, permissive. 🟢 **The rostering/SIS-interop layer this KB has been missing a permissive entry for:** `p230-rostering-layer-axis` exists because every prior candidate on that layer was copyleft, vendor-hosted or ungranted. |

🔵 **Why one row matters more than its star count.** Everything else this KB shelves on the
student-data layer is either a *platform* (which you adopt whole) or a *client* for someone's
proprietary API. A **standard with a permissive reference implementation** is the third thing:
you can implement it, ship it inside a closed product, and the other end of the wire is a
national specification rather than a vendor's roadmap. ⚠️ **5★ is not a maturity signal here** —
a reference implementation of a national standard is used by integrators who do not star it.

### 🟡 The Finnish estate — nine of 188, read correctly, and shelved with a condition

**`org:Opetushallitus` has 188 public repositories, all live on the day they were read.** Nine
payloads read from the real default branch (**six are `master`**):

| Repository | Branch | Licence (payload-verified) | ★ | Layer it supplies |
|---|---|---|---|---|
| [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | `master` | 🟡 **EUPL-1.1** (631 B) | 3 | **National core curriculum + qualifications** (ePerusteet). Finland's analogue of Norway's Grep. |
| [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) | `master` | 🟡 **EUPL-1.1** (653 B) | 23 | **National study records** — qualifications and study rights in one service. |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | `main` | 🟡 **EUPL-1.2** (303 B ×2, **in subdirectories**) | 0 | **National OER library** (`aoe.fi`), 6,829 commits. |
| [`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru) | `master` | 🟡 **EUPL-1.2** (295 B) | 11 | **Admissions application forms** — generic form generation. |
| [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) | `master` | 🟡 **EUPL-1.1** (631 B) | 4 | **Register of providers and institutions** — the join key for the rest. |
| [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **National learner identity** (learner-number registry). |
| [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **Personal competence-development plans** (vocational). |
| [`Opetushallitus/suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) | `main` | 🟡 **EUPL-1.2** (652 B) | 0 | **Attainment service** (2025, newest). |
| [`Opetushallitus/valtionavustus`](https://github.com/Opetushallitus/valtionavustus) | `master` | 🟡 **EUPL-1.1** (652 B, **(c) 2026**) | 8 | **State-grant administration** for providers. |

🔴 **179 of the 188 are unread, not absent.** This table is a sample chosen by stars and by
domain relevance, and it should be read as such.

### ⚠️ The condition on the Finnish rows, stated once and precisely

**The EUPL is OSI-approved, so these are open source.** What makes them different from every
other row on this shelf is **where the copyleft reaches**:

| Question | Answer |
|---|---|
| May we read, study, run and modify it? | 🟢 Yes. |
| May we **call these services** from our own agent over their APIs? | 🟢 **Yes, and the licence is irrelevant to that** — calling is not distribution. |
| May we fork it into a **hosted** client product and keep our changes closed? | 🔴 **No.** EUPL Art. 1 assimilates *"communication to the public"* to distribution, so **SaaS delivery triggers the copyleft, AGPL-style**. |
| May the combined work be relicensed? | 🟡 **Yes — EUPL Art. 5 carries a compatibility list** (GPL-2.0/3.0, AGPL-3.0, LGPL, MPL-2.0, EPL, CeCILL, OSL). ⚠️ Compatible-licence terms *prevail on conflict*, and the EC's own discussion notes the SaaS obligation can be circumvented that way. **Do not build a commercial plan on that route without counsel.** |

🔵 **The shelving rule this produces:** the Finnish estate belongs on this shelf as a **domain
model and an integration target**, not as a starting codebase. It is the most complete public
description of how a national education system's data actually fits together — curriculum,
provider register, learner identity, study records, attainment, plans, grants — and reading it
is free of licence consequence. **Forking it into a hosted product is the one move that is not.**

### 🔴 And the instrument cannot see any of it

`grep -c -i eupl compose/code/lib/license_family.sh` → **0**. Traced through the code (it could
not be executed this pass), every payload above lands on `UNCLASSIFIED`: the EUPL ships as a
**300–650 B grant notice with no title block**, and the classifier is a title-block classifier by
design. 🟢 **Until a grant-notice anchor exists, these nine rows are the only EUPL rows this KB
can defend, because they were read by hand.** That work is instruction 1 for the next pass.


## Added in the eighteenth pass of 2026-10-06 — the certified assessment tier, and a national agency's metadata layer

**Channel new to this KB this pass: the standards-body conformance register** — searching by
**standard + conformance certification** rather than by topic, star count, funder or institution.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com`
on 2026-10-06. Star counts, where given, were read the same day via `WebFetch`; cells that say
*not read this pass* say so rather than carrying an inferred number.

### QTI 3 — assessment item delivery, and the first externally certified permissive asset in this KB

Trend 28 swept LTI 1.3, OneRoster and Caliper and recorded **QTI as "not swept"**. Swept now, and
it is the **best-served** standard on the permissive shelf, not the worst.

| Repo | Licence (read from payload) | ★ / forks | Why it matters for an education engagement |
|---|---|---|---|
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (`main/LICENSE`, © 2022-2024 Amp-up.io, LLC) | 30 / 6 | 100% JavaScript QTI 3 item player, **1EdTech Certified for QTI 3 Basic *and* Advanced "Delivery" conformance**. 🟢 The only asset in this KB that is **both permissive and third-party certified** — fork it, brand it, and the conformance claim in the bid is somebody else's audit, not your assertion |
| [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (`main/LICENSE`, © 2024 Amp-up.io, LLC) | not read this pass | Vue 3 build of the same component. Use when the client front end is already Vue |
| [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (`main/LICENSE.md`, © 2026 Longsight, Inc.) | 5 / 2 | TypeScript reference implementation — **667 commits, 12 npm packages**: parsing, validation, rendering, **scoring**, and **migration from QTI 1.2 / 2.x into QTI 3**. The migrator is the part nobody else ships, and legacy item banks are the reason most assessment projects stall |
| [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (`main/LICENSE`, © 2026 AE Studio) | not read this pass | Framework-agnostic npm renderer with full response processing. The neutral option when the front-end framework is not yet chosen |
| [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | **MIT** (`main/LICENSE`, © 2026 metyatech) | not read this pass | QTI 3.0 item HTML rendering utilities. Smallest surface of the five |

#### Two QTI assets that are **not** permissive — read this before the architecture, not after

| Repo | Licence (read from payload) | The constraint |
|---|---|---|
| [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | **GPL-3.0** (`main/LICENSE.md`) | 19★ / 10 forks, **2,456 commits** — the most mature renderer here, and copyleft. Citolab is the software lab attached to **Cito**, the Netherlands' national assessment institute. ⚠️ Its README states: *"the licensing is GPLv3 — if you want to use it in another way, feel free to ask!"* The **payload is GPL-3.0** and the **holder advertises negotiability**. That is an *invitation to dual-license*, it is invisible to any payload-reading classifier, and it is a **conversation to have before you design around the licence**. See trends §43 |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`master/LICENSE`) | PHP SDK from the TAO assessment platform. **GPL-2.0, not 3.0** — so it is **not licence-compatible with GPL-3.0-only code**. Same trap as `francoisjacquet/rosariosis` in `verticals/solutions.md`. Check before combining |

🔴 **And one fork that nearly entered this shelf as a public-body asset.**
[`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) (1★, 0 forks) is **forked
from `Citolab/qti-components`** — identical root commit `de8b27b`, **2,377 commits against
upstream's 2,456, so 79 behind**. Caught by running `git clone --filter=blob:none --no-checkout`
**before the row was written**. Pin the Citolab address; do not cite the Kennisnet one.

### Kennisnet — the Dutch national education-ICT agency, metadata and vocabulary layer

**[Stichting Kennisnet](https://github.com/Kennisnet)**, the Netherlands' public agency for ICT in
education, publishes **29 repositories**. Nine probed this pass: **6 MIT, 1 GPL-3.0** (the stale
fork above), **2 NO-PAYLOAD**. These are the layer an AI content pipeline needs and that nobody
should write twice.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) | **MIT** (`master/LICENSE`, © 2017 Kennisnet) | metadata — **Python** | Reads and writes **IMS-LOM** learning-object metadata records. 🟢 **A permissive Python library for an education standard** — see the correction to trend 28 below |
| [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) | **MIT** (`master/LICENSE`, © 2018 Kennisnet) | curriculum vocabulary — **Python** | Client for **Eduterm**, the Dutch curriculum-vocabulary service. The curriculum-alignment tool call of P29, already written, in the language the agents are written in |
| [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (`main/LICENSE`, © **2026** Kennisnet) | assessment | QTI 3 support library, **published this year**. The permissive PHP path into QTI, where `oat-sa/qti-sdk` is GPL-2.0 |
| [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | **MIT** (`master/LICENSE`, © 2017 Stichting Kennisnet) | metadata | **NL-LOM**, the Dutch national application profile of LOM. The worked example of how a country profiles a global metadata standard |
| [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | **MIT** (`master/LICENSE`, © 2015 Stichting Kennisnet) | discovery | Client for **Edurep**, the national learning-resource search index. A national OER index with a permissive client is a **content source you may query without a licence negotiation** |
| [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | **MIT** (`main/LICENSE`, © 2024 Kennisnet) | harvesting | OAI-PMH implementation — the protocol national repositories actually expose |
| [`Kennisnet/qti-editor-angular`](https://github.com/Kennisnet/qti-editor-angular) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | authoring | QTI editor. **Ungranted — do not vendor it** |
| [`Kennisnet/edurep-xslt`](https://github.com/Kennisnet/edurep-xslt) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | transforms | Edurep XSLTs. **Ungranted** |

⚠️ **Nine of 29 probed, chosen by stars and domain relevance.** The estate's ungranted rate is
**sampled, not established** — the same shortfall pass 17 declared for Opetushallitus's 188
repositories, and it is carried as a declared gap rather than rounded off.

### 🔵 The correction this section forces on trend 28

Trend 28 concluded that the permissive shelf has a **"Python-shaped hole"** — *"Python, where
essentially all of the AI tutoring and agent code in this KB is written, is not [served]."*

**Half of that survives.** ~~There is still **no permissive Python LTI 1.3 library**, which is the
claim trend 28 actually measured.~~ 🔵 **WITHDRAWN, twenty-fourth pass of 2026-10-07** — [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
is **MIT**, head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. What survives is only the
narrow form: **no live *framework-agnostic* permissive Python LTI 1.3 library**. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`. And `pylom` and
`py-eduterm-client` are **MIT Python libraries for education standards**, so Python *is* served for
**metadata and curriculum vocabulary** as well.

🟢 **The hole is LTI-shaped, not Python-shaped — and that makes the contribution opening cheaper,
not smaller.** It is one protocol, with a procurement-scored buyer already attached (39% of US
districts score interoperability in the RFP rubric). Corrected in place in `intel/trends.md` §28.

## Added in the nineteenth pass of 2026-10-06 — the conformance-engine tier, which nineteen passes never recorded

**Channel: the regulatory-citation channel** — sweeping for implementations of the exact technical
standard a binding rule names (WCAG 2.1 AA, WCAG 2.2 AA, EN 301 549, PDF/UA) rather than by topic.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-06, across `main` / `master` / `develop` and 7–11 filename variants. Star and fork counts
were read from the rendered repository page the same day (`api.github.com` is 403 here).

**Why these belong in *foundations* and not in trending:** none of them is new, none is
education-specific, and that is the point — they are the deterministic substrate that every
accessibility claim in a client deliverable has to rest on, and this KB's accessibility work so far
recorded the **agent** layer (`Community-Access/accessibility-agents`, MIT) without the engines
underneath it. An agent that reports WCAG findings with no engine beneath it is producing an
opinion, not evidence.

### The permissive engines — Apache-2.0 and MIT

| Repo | Licence (read from payload) | ★ / forks | What it gives you |
|---|---|---|---|
| [IBMa/equal-access](https://github.com/IBMa/equal-access) | **Apache-2.0** (`master/LICENSE`) | **780 / 108** | IBM Equal Access Accessibility Checker. **Nine packages** in one repo: `accessibility-checker-engine` (the rules), `accessibility-checker` (Node), `accessibility-checker-extension` (browser devtools), **`java-accessibility-checker`**, `cypress-accessibility-checker`, `karma-accessibility-checker`, `vitest-accessibility-checker`, `rule-server`, `report-react`. JavaScript. 🟢 **The pick when the deliverable must run in the client's CI**, and the only engine here with a **JVM** binding — which matters on a Java LMS estate. |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | **Apache-2.0** (`main/LICENSE`) | **30.9k / 9.8k** | Audits pages for accessibility alongside performance and best practices. **Runs locally and sends nothing to a remote server** — which is what makes it quotable under an EMEA data-residency clause. CLI, Node module, or Chrome DevTools. 🟡 Its a11y category is axe-core-derived and deliberately partial: a gate, not an audit. |
| [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web) | **MIT** (`main/LICENSE`, © Microsoft Corporation) | **955 / 182** | Chrome/Edge extension for assessing web accessibility. TypeScript. 🟢 **The differentiator is the guided assessment workflow** — it walks a human through the criteria a scanner cannot decide, which is the half of a conformance claim that automation cannot produce. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (`main/LICENSE`) | **76.8k / 10.8k** | OCR engine, **100+ languages**, LSTM line recogniser. Outputs plain text, **hOCR**, **ALTO**, **PAGE**, PDF and text-only PDF. 🟢 **The entry point for scanned textbooks** — and the structured output formats are what make a downstream tagging step possible at all. ⚠️ Latest tagged release on the page is **5.0.0 (2021-11-30)** while development continues on `main`; pin a distribution package rather than the tag. |

### The weak-copyleft engines — usable, with two obligations

| Repo | Licence (read from payload) | ★ / forks | The obligation |
|---|---|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | ⚠️ **MPL-2.0** (`master/LICENSE`) | **7.6k / 954** | Accessibility engine for automated web UI testing; **WCAG 2.0, 2.1 and 2.2 at A, AA and AAA**, multi-locale, 5,586 commits on `develop`. 🟢 **MPL-2.0 is file-level copyleft: using it unmodified as a dependency does not reach the studio's own files.** ⚠️ **Two things do bite** — it must appear in the client's SBOM with its licence, and **editing a rule file puts that file under MPL-2.0 with source-disclosure attached**. Tune through configuration, never by patching rules. 🔵 **This is the engine inside every MIT accessibility agent in this KB** (`accessibility-agents` declares `@axe-core/cli`; `a11ymcp` declares `axe-core` and `@axe-core/puppeteer` at runtime), so the inheritance is not optional — it is the shelf. |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | ⚠️ **MPL-2.0** (`main/LICENSE`) | **34.9k / 2.4k** | Adds an OCR text layer to scanned PDFs, deskews, and emits **PDF/A**. Python; Linux/macOS/Windows/FreeBSD. Wraps Tesseract. 🟢 Same file-level reasoning as axe-core — invoke it as a tool and nothing propagates. 🔴 **Read the limit precisely: a searchable PDF is not an accessible PDF.** It produces no tags, no reading order and no structure, so it does **not** satisfy PDF/UA. |

### 🔴 The gap this tier makes visible — validation is served, remediation is not

| Need | Permissive option | Status |
|---|---|---|
| Scan web content against WCAG | equal-access (Apache-2.0), axe-core (MPL-2.0), Lighthouse (Apache-2.0) | 🟢 **Well served** |
| Guide the manual half of a claim | accessibility-insights-web (MIT) | 🟢 Served |
| OCR a scanned textbook | Tesseract (Apache-2.0) | 🟢 Served |
| Make a scanned PDF searchable | OCRmyPDF (MPL-2.0) | 🟡 Served, and **not the same thing** as accessible |
| **Validate PDF/UA** | [veraPDF/veraPDF-library](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL / MPL** — `LICENSE.GPL` and `LICENSE.MPL`, ⚠️ **filenames outside every shortlist this KB probes** (present on `master` and `integration`, absent from `main`), so an 11-filename sweep reports it ungranted while the grant is in the root |
| **Produce tagged, accessible PDF/UA** | — | 🔴 **Nothing permissive found.** Searched PDF/UA remediation, tagged PDF, structure tagging, accessible PDF generation |
| Reference the **EN 301 549** clause set | — | 🔴 **Nothing** except an MIT adapter to a paid API (`agents/top.md`) |

🔵 **The rule this yields for a proposal:** everything up to *"here is a per-criterion finding with
evidence"* can be built on Apache-2.0 and MIT with two MPL-2.0 tools invoked unmodified. Everything
past *"and here is the remediated PDF"* is **human labour on a copyleft validator**. ⚠️ **Scope and
price the document estate separately from the web estate.** They look like one deliverable in a
statement of work and they are not.

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

This KB has recorded, across several passes, that permissive education supply collects at the
*edges* of platforms it may not fork. The conformance tier is the clearest instance yet and it
inverts the usual complaint: **the measuring layer is permissive and the end-user application layer
is copyleft** (`cboard` GPL-3.0, `AsTeRICS-Grid` AGPL-3.0, `pa11y` LGPL-3.0, `nvda` GPL-2.0+ in
`copying.txt` — see `verticals/solutions.md`). 🟢 **Since the billable work is remediating the
client's own estate rather than shipping an assistive application, the half a studio needs is the
half that is permissive.** That is a better position than this KB has been able to report for any
other tier in education, and it is worth stating plainly in a capability deck.

---

## Added in the twentieth pass of 2026-10-06 — the evidence tier, which every transition article actually asks for

**Channel new to this KB this pass: the transition-provision channel** — reading each
binding instrument's **transitional article** instead of its entry-into-force date. Full
findings in `agents/trending.md`; the regional consequences in `intel/market.md`; the
delivery recipe in `compose/patterns.md` **P28**.

The channel produced a supply question this KB had never asked. Every transition regime
found this pass discharges on an **artefact**, not on a date:

| Regime | What the extension is conditional on | The artefact that proves it |
|---|---|---|
| **EU AI Act Art. 111** | the design of the high-risk system **remaining unchanged** | a versioned, dated record that the deployed system is the same system |
| **Vietnam** Decree 142/2026/ND-CP | a **transition plan** filed on the one-stop portal | the plan, plus the inventory behind it |
| **Vietnam** Decision 33/2026/QĐ-TTg, education category 1 | self-learning content **not** drawn from *"uncontrolled data sources"* | dataset provenance and validation records |
| **EU Annex III §3** (admissions, assessment, placement) | bias and accuracy obligations | fairness measurements over the decision, retained |
| **EMEA, per the nineteenth pass** | 🔴 **no harmonised standard cited under the EAA**, so no presumption of conformity | evidence is the *only* route — there is no standard number to point at |

🔴 **Nineteen passes recorded none of the tooling that produces these artefacts.** Grep
confirmed it before this shelf was written: `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn`, `AIF360` — **zero
occurrences across all eight files.** The KB had the obligations and the pedagogy, and
nothing in between.

### The shelf — all licences read from the repository's own payload on 2026-10-06

Stars and descriptions read from each repository page the same day via `WebFetch`
(`github.com` is 403 to `curl` through this environment's proxy; `raw.githubusercontent.com`
is not). **Ten rows, all verified.**

| Repo | Licence (payload path) | ★ / forks | Lang | What it does, and why an education engagement needs it |
|---|---|---|---|---|
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | **Apache-2.0** (`LICENSE.txt`) | 28.3k / 6.4k | Python | *"The open source AI engineering platform for agents, LLMs, and ML models."* Model registry with versioned stages. **This is the Art. 111 instrument**: the registry is what lets you state, with dates, that the system in service is the system that was placed in service. |
| [iterative/dvc](https://github.com/iterative/dvc) — 🔴 **now `treeverse/dvc`**; both paths serve head `56e5982` and PyPI `dvc` declares `Source: github.com/treeverse/dvc`. See the canonical-name table below | **Apache-2.0** (`LICENSE`) | 15.9k / 1.3k | Python | *"Data Versioning and ML Experiments."* Versions the **corpus** alongside the model, in Git. The answer to Vietnam's *"uncontrolled data sources"* trigger is a hash, and this produces it. |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | **Apache-2.0** (`LICENSE`) | 11.9k / 1.9k | Python | *"Always know what to expect from your data."* Declarative data validation. Turns "the curriculum corpus is controlled" from an assertion into a suite that fails a build. |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** (`LICENSE`) | 8.0k / 946 | Python | ML **and LLM** observability — evaluate, test and monitor any AI-powered system or pipeline. The regression baseline the nineteenth pass said a remediation contract has to ship. |
| [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) | **Apache-2.0** (`LICENSE`) | 2.9k / 912 | Python | Fairness metrics for datasets and models, explanations for them, and bias-mitigation algorithms. Annex III §3 is **admissions, assessment and placement** — decisions about people. |
| [whylabs/whylogs](https://github.com/whylabs/whylogs) | **Apache-2.0** (`LICENSE`) | 2.8k / 145 | Python | Data logging that emits **statistical profiles rather than raw records** — visibility into data quality over time with privacy-preserving collection. The shape that survives a student-data rule (see California **AB 1159**). |
| [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) | **Apache-2.0** (`LICENSE`) | 2.7k / 540 | Java | *"An Open Standard for lineage metadata collection."* A generic model of run, job and dataset entities. Lineage as a **standard**, so the evidence outlives your pipeline choice. |
| [fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) | **MIT** (`LICENSE`) | 2.3k / 522 | Python | *"A Python package to assess and improve fairness of machine learning models."* The **MIT** option on this shelf — the one with no notice obligation at all. |
| [NannyML/nannyml](https://github.com/NannyML/nannyml) | **Apache-2.0** (`LICENSE`) | ★ not read this pass | Python | Post-deployment performance estimation **without ground-truth labels**. Education's labels arrive a term or a year late; this is the tier that does not wait for them. |
| [mlcommons/croissant](https://github.com/mlcommons/croissant) | **Apache-2.0** (`LICENSE.md`) | 907 / 125 | Python | *"A high-level format for machine learning datasets."* Dataset metadata as a published format — the interchange layer for a provenance claim a regulator or a ministry can read. |

### Measured rejections from the same sweep

Recorded so a later pass does not re-probe them as options.

| Repo | Licence (payload) | Verdict |
|---|---|---|
| [deepchecks/deepchecks](https://github.com/deepchecks/deepchecks) | 🔴 **AGPL-3.0** (`LICENSE`) | Reject for reusable IP. Testing and validation for ML and LLM systems — capable, and the network clause reaches a hosted validation service. |
| [sodadata/soda-core](https://github.com/sodadata/soda-core) | 🔴 **Elastic License 2.0** (`LICENSE`) | Reject. **Not OSI-approved**; the payload opens *"Elastic License 2.0 … Acceptance: By using the software, you agree to…"*. A data-quality tool whose own licence is the risk it would be bought to manage. |

### Read this shelf honestly — three qualifications

🔵 **None of these is an education project.** This is general-purpose MLOps and
responsible-AI tooling. It earns a place in an education KB for one reason: the
transition articles found this pass are discharged by artefacts, and nothing already on
this KB's shelves produces them. ⚠️ **Do not present this tier as education IP** — present
it as the plumbing under a billable education-specific rubric, exactly as P27 treats
`inspect_ai`.

⚠️ **The fairness pair is a measurement tool, not a compliance verdict.** AIF360 and
Fairlearn compute metrics; which metric is the *right* one for an admissions decision is a
legal and pedagogical judgement that has to be made and documented per engagement. A
dashboard of eleven fairness metrics with no stated choice among them is not evidence.

🟢 **The licence shape of this tier is unusually clean** — nine of ten permissive, eight
Apache-2.0 and one MIT, every one read from its own payload. That is a better result than
the platform tier, the assistive tier or the language tier has ever returned in this KB,
and it means the evidence layer is the one part of an Annex III delivery with no licence
negotiation in it at all.

## Added in the twenty-second pass of 2026-10-06 — the interoperability layer, found on a forge this KB had never searched

Channel: the **GitLab REST API v4** (discovery + metadata + payload). Controls, limits and the
detector-error table are in `agents/top.md`; the instrument is in
`compose/code/gitlab-api-channel/`. 25 search terms → **534 unique projects** → the rows below are
the ones that are *infrastructure* rather than product.

🟢 **Why this shelf cared about the sweep at all:** trend 28 of this KB records an
**interoperability hole** — the standards (xAPI, LTI, 1EdTech) are scored line items in
procurement, and the permissive implementations were missing. **Three of the rows below are
standards plumbing**, and they were invisible to every previous pass because every previous pass
searched one forge.

| Repo | Licence (read from payload) | ★ · last activity | Placement | Why it is a foundation |
|---|---|---|---|---|
| [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) | ⚠️ **LGPL-3.0** (`LICENSE`; GitLab's detector says `other`) | 0 · 2026-05-15 | ⚠️ EMEA *(README names **Universis**; Greece inferred)* | **An implementation of the 1EdTech EduAPI specification**, built for the **Universis** Greek higher-education student-information project. The first EduAPI implementation in this KB. ⚠️ **LGPL-3.0** — the middle path this KB already documents for Odoo/OpenEduCat: link against it, do not fold it into a proprietary binary |
| [`eduplex-api/cake-api-xapi-proxy`](https://gitlab.com/eduplex-api/cake-api-xapi-proxy) | 🟢 **MIT** (`LICENSE`) | 0 · 2026-08-31 | ⚠️ **unplaced** — no country evidence in repo or README | PHP proxy that forwards **xAPI** statements to an **LRS**, as a CakePHP plugin over `cake-rest-api`. Tiny, single-purpose, permissive — the cheapest way to put a compliant statement pipe in front of an LRS when the LMS cannot speak xAPI itself |
| [`TIBHannover/oer/wordpress-oersi-plugin`](https://gitlab.com/TIBHannover/oer/wordpress-oersi-plugin) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | EMEA (Germany) | WordPress integration of **OERSI**, the German higher-education **search index for Open Educational Resources**, with Elasticsearch indexing. From **TIB Hannover** (the German National Library of Science and Technology) — a public-institution-maintained OER discovery layer, MIT, actively committed |
| [`adaptive-learning-engine/adlete-packages`](https://gitlab.com/adaptive-learning-engine/adlete-packages) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | ⚠️ EMEA *(inferred)* | ADLETE adaptive-learning engine, monorepo of components; sibling `adaptive-learning-engine/moodle/adleteh5p` binds it to **H5P** inside Moodle. Full entry in `agents/top.md` |
| [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** (`LICENSE`) | 8 · **2026-10-06** | EMEA (France) + NA (Québec) | Assignment-distribution and grading infrastructure over **any** GitLab instance, **nbgrader**-integrated. Pairs with [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (BSD-3-Clause, 1.4k★, v0.9.6 of 2026-09-30) already on this shelf. PyPI `travo` 2.1.1 |
| [`learntech-rwth/omilaxr-ecosystem/v2/omilaxr`](https://gitlab.com/learntech-rwth/omilaxr-ecosystem/v2/omilaxr) | 🔴 **AGPL-3.0** (`LICENSE`) | 1 · 2026-07-03 | EMEA (Germany) | **OmiLAXR** — authoring framework for modular **learning-analytics modules in XR** (VR/AR), from RWTH Aachen's Learning Technologies group. 🔴 Recorded and **excluded from delivery** on licence; kept because it is the only XR-learning-analytics framework this KB has located at all |
| [`particify/dev/foss/arsnova-lms-connector`](https://gitlab.com/particify/dev/foss/arsnova-lms-connector) | 🟢 **MIT** (`LICENSE`) | 3 · 🔴 **2022-09-12** | EMEA (Germany) | Proxy exposing **course-membership data from LMSs under one unified API** — from the ARSnova/Particify audience-response project. 🔴 **The first row in this KB marked dead by measurement rather than by inference:** `last_activity_at` is four years old. Read it as a design, not a dependency |
| [`git-classrooms/git-classrooms`](https://gitlab.com/git-classrooms/git-classrooms) | 🟢 **MPL-2.0** (`LICENSE`, detector agrees) | 3 · 2026-06-16 | ⚠️ **unplaced** (namespace only) | GitHub-Classroom-equivalent for self-hosted GitLab. ⚠️ **A publish-only mirror**: its own description points upstream to a GitHub repository, so the GitLab copy is a *host*, not the project. MPL-2.0 is file-level copyleft — usable alongside proprietary code, not inside the same file |

### ⚠️ The REUSE rows — where the root `LICENSE` is a map and not a grant

| Repo | Root `LICENSE` | The real licence set, enumerated from `/repository/tree?path=LICENSES` |
|---|---|---|
| [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | **517 B** REUSE pointer | **4**: `GPL-3.0-or-later`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC0-1.0` |
| [`oer/oer-reveal`](https://gitlab.com/oer/oer-reveal) | **516 B** REUSE pointer | **6**: the same four plus `LicenseRef-MIT-HEH-JL`, `LicenseRef-MIT-JL` — two **custom references**, which SPDX permits and no classifier can resolve |

🔵 **Pass 107 had already rejected `oer/emacs-reveal` on licence and kept it as a design.** What is
new is that the licence **set** is now enumerated rather than sampled: an OER toolchain splits
**code under GPL-3.0-or-later** from **content under CC-BY/CC-BY-SA/CC0**, and a `LicenseRef-`
entry means the project wrote its own terms. 🔴 **For this KB's method the consequence is blunt:
on a REUSE repository, reading the root payload — the rule that bought twenty passes of accuracy —
returns a notice board.** The answer lives in `LICENSES/` and in per-file SPDX headers, and only a
tree listing finds it.

### 🔴 What this sweep did **not** find, with the denominator attached

534 unique projects, 25 terms, one forge. **Not found, searched for explicitly:**

| Looked for | Terms used | Result |
|---|---|---|
| a permissive **LTI 1.3 tool provider** | `lms ai`, `learning management system`, `student information system` | 🔴 **0** — the LTI-shaped hole of trend 28 is still open on a second forge |
| a permissive **knowledge-tracing / BKT-IRT** library | `knowledge tracing`, `adaptive learning`, `learning analytics` | 🔴 **0** — `OATutor` (MIT) and the ADLETE engine above remain the only mastery assets in this KB |
| an **MCP server for education** on GitLab | `education agent`, `edtech ai`, `classroom ai` | 🔴 **1 candidate, unusable** — `sheikhcoders/interleaved-learning-mcp` carries **no licence payload at all**. Every education MCP server this KB holds is still GitHub-hosted |
| a **LATAM-origin** education project | all 25 terms | 🔴 **1 LATAM-plausible of 534**, and its placement is an inference from Portuguese-language naming, not a declaration — see `intel/market.md` |

---

## Added in the twenty-third pass of 2026-10-07 — the interoperability tier, re-picked by date

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; ages computed against the
reference date 2026-10-06.** Licences below were read from the repository's own payload via
`raw.githubusercontent.com` on 2026-10-06. Head-commit dates come from
`git fetch --depth 1 --filter=blob:none`, the channel that works while `api.github.com/repos/*`
returns 403.

🔴 **This file is the coldest shelf file in the KB: of its 230 GitHub references, 33.0% have not been
touched in a year and 18.3% not since before 2024** — against 18.8% and 6.6% for
`compose/patterns.md`. "Foundational" has been doing duty as a synonym for "long-established". This
section fixes the worst instance and dates the rest.

### 🔴 The correction: this file recommends the cold fork of a live library

| | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) |
|---|---|---|
| licence payload | **Apache-2.0**, 11,343 B, `sha256 78b49eea…` | **Apache-2.0**, 11,343 B, `sha256 78b49eea…` |
| composer `name` | `packbackbooks/lti-1p3-tool` | `imsglobal/lti-1p3-tool` |
| composer `description` | *"A library used for building IMS-certified LTI 1.3 tool providers in PHP."* | *(none)* |
| head commit | 🟢 **2026-09-23 (13 d)** | 🔴 **2020-06-03 (2,316 d)** |

🟢 **Byte-identical licence file. Same library. 2,303 days apart.** The consortium's republished copy
stopped; the author's original did not. **Use `packbackbooks/lti-1-3-php-library`.** Nothing in the
licence, the description or the ★ would have surfaced this — only the date.

### The permissive LTI 1.3 shelf, by runtime and by date

| Runtime | Repo | Licence (payload) | Head commit | Age | Verdict |
|---|---|---|---|---|---|
| **Node / JS** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** (11,360 B) | 2026-10-06 | 🟢 0 d | 🟢 **pick** |
| **PHP** | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B) | 2026-09-23 | 🟢 13 d | 🟢 **pick** |
| **Java / Spring** | [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | **Apache-2.0** (11,357 B) | 2026-10-06 | 🟢 0 d | 🟢 **pick** |
| **Python** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** (1,527 B) | 2026-07-01 | 🟢 97 d | 🟢 **pick** — LTI 1.3 **and** 1.1, tested against Open edX, Canvas, Moodle |
| **Python / Django** | [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti) | **MIT** (1,097 B) | 2025-08-27 | ⚠️ 405 d | ⚠️ usable; ageing |
| **Python (scaffold)** | [`ucfopen/cookiecutter-python-lti`](https://github.com/ucfopen/cookiecutter-python-lti) | **MIT** (1,129 B) | 2026-05-12 | 🟢 147 d | ⚠️ **Django template only** — see the warning below |
| **Elixir** | [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) | **MIT** (1,082 B, © Carnegie Mellon University) | 2026-03-13 | 🟢 207 d | 🟢 usable (OLI Torus) |
| **PHP (assessment vendor)** | [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | 🔴 **GPL-2.0** (18,091 B) — *corrected pass 28, `P452`; was filed LGPL-2.1* | 2026-07-16 | 🟢 82 d | 🔴 **strong copyleft, and it is a LIBRARY** — there is no LGPL linking exception here, so linking it into a deliverable carries the obligation. The archive called this *"the exception that breaks the symmetry"* and it was right |
| Python | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | MIT (1,069 B) | 2022-11-21 | 🔴 1,415 d | 🔴 **do not start here** |
| Python | [`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3) | MIT (1,069 B, © Dmitry Viskov) | 2023-01-12 | 🔴 1,363 d | 🔴 fork, also cold |
| PHP | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) | Apache-2.0 (11,343 B) | 2020-06-03 | 🔴 2,316 d | 🔴 **superseded by its own upstream** |
| PHP | [`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | — | 2016-11-28 | 🔴 3,599 d | 🔴 **9.9 years** — remove from any proposal |
| Java | [`UOC/java-lti-1.3-provider-example`](https://github.com/UOC/java-lti-1.3-provider-example) | MIT | 2022-11-18 | 🔴 1,418 d | 🔴 example only, cold |
| Java | [`Unicon/tool13demo`](https://github.com/Unicon/tool13demo) | — | 2024-10-31 | 🔴 705 d | 🔴 demo only, cold |

### 🔴 Three corrections this table forces on standing text in this file

1. **"There is no Python LTI 1.3 library on this shelf"** (stated **four** times in this file, the
   most of any file in this KB) is **false**. It was already false when a later pass reinstated `pylti1.3`; it is now false twice
   over, and the asset that closes it — `jupyterhub/ltiauthenticator`, BSD-3-Clause, 97 days — has
   been cited elsewhere in this KB three times without ever being counted. The gap was an artefact
   of **how this KB filed the repository**, not of supply. (Trend 29, applied to this KB's own
   index; trend 50, because the earlier correction never left its pass-scoped section.)
2. **The LTI-shaped hole of trend 28 is closed.** Five live permissive implementations across five
   runtimes. What remains is not a hole but a **selection discipline**: three of the four
   implementations this KB had been naming are cold.
3. ⚠️ **`Harvard-University-iCommons/django-lti` has a holder mismatch** — published by Harvard's
   iCommons organisation, MIT payload vesting copyright in **the Regents of the University of
   Michigan**. The grant is clean; the counterparty is not the one the URL implies. Record it in any
   provenance pack.

### ⚠️ Recency is not inherited — the rule this adds to the dependency work of the twenty-first pass

Pass 21 resolved 352 dependencies and measured them **by licence**. None were measured **by date**.
The first one checked shows why that matters.
[`ucfopen/cookiecutter-python-lti`](https://github.com/ucfopen/cookiecutter-python-lti) is MIT and
**147 days old**. Its Flask template's `requirements.txt` ends:

```
git+https://github.com/ucfopen/pylti1.3.git@master
```

| Defect | Detail |
|---|---|
| 🔴 stale | resolves to a fork whose head commit is **2023-01-12 — 1,363 days** |
| 🔴 not upstream | the fork, not `dmitry-viskov/pylti1.3`, and not PyPI |
| 🔴 unreproducible | pinned to **`@master`**, a moving branch, so two builds a month apart differ |

🟢 **Its Django template does it correctly**, pinning `django-lti==0.7.1`. **Rule: a component's own
head-commit date says nothing about the dates of what it installs. Run the P22 gate over the
dependency closure, not the dependency list.**

### The rest of the foundation shelf, dated

| Repo | Head commit | Age | Note |
|---|---|---|---|
| [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | 2026-10-06 | 🟢 0 d | **Apache-2.0**; ASR **and** TTS — the replacement for Piper in P18 |
| [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | 2026-10-06 | 🟢 0 d | 🔴 **GPL-3.0** (35,199 B payload) — *corrected pass 28; was filed LGPL-3.0.* 🔵 **The size already said so:** GPL-3.0 is ~35 kB and LGPL-3.0 is ~7.6 kB, so the byte count published beside the label refuted it without a fetch |
| [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) | 2026-07-20 | 🟢 78 d | |
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 2025-06-21 | 🔴 **472 d** | MIT, **1EdTech Certified** — certification does not lapse when maintenance stops, but disclose the date |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | 2025-09-04 | 🔴 397 d | |
| [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) | 2024-12-16 | 🔴 659 d | |
| [`theopenem/OneRoster.NET`](https://github.com/theopenem/OneRoster.NET) | 2023-10-13 | 🔴 1,089 d | the only OneRoster implementation on this shelf, and it is cold |
| [`rhasspy/piper`](https://github.com/rhasspy/piper) | 2025-08-26 | 🔴 406 d | MIT; superseded for new work by `sherpa-onnx` |
| [`AI4Bharat/IndicTrans2`](https://github.com/AI4Bharat/IndicTrans2) | 2025-10-03 | 🔴 368 d | liveliest member of a substrate that is **87.5% cold, 0% in 30 days** |
| [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) | 2024-02-10 | 🔴 969 d | already flagged for relicensing; now also dated |

### 🔴 Declared gaps from this pass, with the denominator attached

| Looked for | How | Result |
|---|---|---|
| a **live permissive OneRoster** implementation | head-commit date over every OneRoster reference in this KB | 🔴 **0 of 2** — `theopenem/OneRoster.NET` and `jdolny/OneRoster.NET`, both 1,089 d |
| a **live permissive Caliper** implementation | same | 🔴 **0** — and `1EdTech/caliper-java` now 404s because **the consortium announced a move to private repositories**; `1EdTech/caliper-spec` last touched 2019 |
| a **live** permissive **knowledge-tracing / BKT-IRT** library | recency over the mastery tier | ⚠️ `CAHLR/OATutor` is **6 days** old — 🟢 this gap is *not* a recency gap; it remains a breadth gap |
| anything on **LATAM self-hosted forges** (`.edu.br`, `.edu.mx`, `.cl`) | 15 hosts × 3 endpoints | 🔴 **unmeasurable** — 000 on all 45 requests, and a deliberately bogus host also returns 000, so the probe cannot separate "absent" from "egress denied". **No supply conclusion is drawn** |

⚠️ **That last row is recorded so it is not mistaken for coverage.** A channel that cannot
distinguish absence from denial produces no finding in either direction.

---

## Added in the twenty-fourth pass of 2026-10-07 — the interoperability tier re-pointed at its upstreams

⏱️ **Ages against the reference date `2026-10-07`.** Channel: the package registries
(`compose/code/registry-recency-channel/`), plus `git ls-remote` tag enumeration.

**Two rows on this shelf pointed at forks, and both forks were cold.** The rows are re-pointed
above; this section records what replaced them and why the detection generalises.

### The LTI 1.3 shelf, by runtime, both channels

| Runtime | Pick | Licence (payload) | Head commit | Age | Latest release |
|---|---|---|---|---|---|
| **Python / Django** | 🆕 [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **MIT** (1,098 B) | 2026-10-05 | 🟢 **2 d** | 🟢 [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1**, 61 d |
| **Python / JupyterHub** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** (1,528 B) | 2026-07-01 | 🟢 98 d | 🟢 v1.6.3, 195 d |
| **Node** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 (11,360 B) | 2026-10-06 | 🟢 **1 d** | 🆕 🟢 npm [`ltijs`](https://www.npmjs.com/package/ltijs) **7.0.7, 2026-10-06 — 1 d** |
| **PHP / Moodle** | 🔁 [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 Apache-2.0 (`master/LICENSE.md`, 11,343 B) | 2026-09-23 | 🟢 **14 d** | 🆕 🟢 Packagist [`packbackbooks/lti-1p3-tool`](https://packagist.org/packages/packbackbooks/lti-1p3-tool) **v6.4.4, 2026-09-23 — 14 d**, 68 releases |
| **JVM / Spring Security** | [`oxctl/spring-security-lti13`](https://github.com/oxctl/spring-security-lti13) | 🟢 Apache-2.0 (11,357 B) | 2026-10-06 | 🟢 1 d | 🆕 🟢 Maven Central `uk.ac.ox.ctl:spring-security-lti13` **0.3.7, 2026-10-06 — 1 d**, 23 versions |
| **Elixir** | [`Simon-Initiative/lti_1p3`](https://github.com/Simon-Initiative/lti_1p3) | 🟢 MIT (1,082 B, © Carnegie Mellon University) | 2026-03-13 | 🟢 208 d | 🆕 🟢 Hex [`lti_1p3`](https://hex.pm/packages/lti_1p3) **0.11.0, 2026-03-13 — 208 d** |
| **Python, framework-neutral** | ⚠️ [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) — **alpha, vendors `PyLTI1p3`** | 🟢 MIT, ⚠️ holder `Dmitry Viskov` | 2026-08-05 | ⚠️ 63 d | ⚠️ PyPI [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 — 103 d**, one release |

🆕 **The release column was four dashes until the twenty-fifth pass, and the reason was that this
KB had only ever used two registries.** `pypi.org` and `registry.npmjs.org` serve Python and Node;
the PHP, JVM and Elixir rows had no release channel at all. **Three further registries are
reachable from this environment and were probed for the first time on 2026-10-07:**

| Registry | Endpoint | Status |
|---|---|---|
| **Packagist** (PHP) | `repo.packagist.org/p2/<vendor>/<pkg>.json` | 🟢 200 |
| **Maven Central** (JVM) | `repo1.maven.org/maven2/<group path>/<artifact>/maven-metadata.xml` | 🟢 200 |
| **Hex** (Elixir / Erlang) | `hex.pm/api/packages/<name>` | 🟢 200 |
| RubyGems · Go module proxy | `rubygems.org/api/v1/gems/<n>.json` · `proxy.golang.org/<mod>/@v/list` | 🟢 200, no shelf row needs them yet |
| *(still blocked)* | `api.github.com/repos/*` · rendered `github.com` · `crates.io` | 🔴 403 |

🟢 **Every row on this shelf now agrees across two independent channels**, and on three of the
five rows the head commit and the release are the **same day** — the signature of a maintained
library, and the exact inverse of `pylti1.3`'s 1,416/1,417.

⚠️ **The PHP row carries the lesson that makes the channel usable: the package name is not the
repository name.** `repo.packagist.org/p2/packbackbooks/lti-1-3-php-library.json` is a **404**;
the composer package is **`packbackbooks/lti-1p3-tool`**, and only its own `composer.json` says so.
🔵 **A registry census keyed on repository slugs would have recorded "not published" for a library
with 68 releases.** Read the manifest for the name, then query the registry — never the other way.

🔴 **And the same probe closes the cold-fork case from a third direction.** `1EdTech`'s copy
declares the composer name **`imsglobal/lti-1p3-tool`**, which Packagist **404s**, and its
`composer.json` declares **no licence at all** while the repository ships Apache-2.0. Commit date,
payload identity and now registry presence all agree: the standards body's copy is the dead one.

🔵 **So the "framework-neutral Python" cell is no longer empty, and it is the only row on this
shelf whose two channels disagree in the dangerous direction** — a release 103 days old against a
commit 63 days old, on a project whose own README says three of its five subsystems are unbuilt.
`dmitry-viskov/pylti1.3` remains **1,416 days cold on the commit channel and 1,417 on the release
channel** (`pylti1p3` v2.0.0, 2022-11-20), and `ff-ltitoolkit` **vendors it rather than replacing
it**. The contribution opening is still one protocol binding wide; what changed is that someone
has started, alone, at `0★`.

### 🔴 Rows removed from this shelf, and the reason each was wrong

| Removed | Why |
|---|---|
| `1EdTech/lti-1-3-php-library` | 🔴 Head commit **2020-06-03 — 2,317 d**. It is the standards body's **fork** of `packbackbooks/lti-1-3-php-library`; pass 23 established byte-identical Apache-2.0 payloads (11,343 B) under two composer names. The upstream was committed **14 days** ago. ⚠️ Its **124★** was the fork's audience and is withdrawn rather than transferred |
| `IMSGlobal/LTI-Tool-Provider-Library-PHP` *(was cited by `compose/patterns.md` P1, not by this file)* | 🔴 Head commit **2016-11-28 — 3,600 d**, and its `README.md` states support for **"LTI 1.1 and the unofficial extensions to LTI 1.0"** — **it does not implement LTI 1.3**. ⚠️ `IMSGlobal` became **1EdTech in 2022**, so the org name alone dated it |
| `openedx/openedx-lti-tool-plugin` | 🔴 **The slug does not exist** — `git ls-remote` returns no ref, and PyPI 404s on that name. The real project is **`eduNEXT/openedx-lti-tool-plugin`** (Apache-2.0, 11,357 B) and it is ⚠️ **443 days cold and unpublished to PyPI**, so "available permissive Python option" overstated it |

### 🔵 The licence boundary this tier actually has — read this before quoting the shelf

[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) is the
**best-maintained Python LTI 1.3 implementation in any language**: head commit **6 d**, released
**6 d** ago as `lti-consumer-xblock` v11.4.2. Its payload is **AGPL-3.0, 34,520 B**.

🟢 Inside an Open edX deployment it is the correct component. 🔴 As reusable Globant IP it is
unusable, which is the premise of **P30**. **State it that way in a bid**: the permissive Python LTI
shelf is not empty, it is *younger and thinner than the copyleft one* — a materially different
sentence from "no Python LTI library exists", which this file asserted for fourteen passes.

### What the installed tier does to this shelf's foundation rows

The 293 depth-1 dependencies of the twelve repositories whose manifests pass 21 resolved were dated
this pass. **30.1% are more than a year old; 13.0% predate 2024; the median is 65 days.** Against
the citing tier's 23.0% / 11.1% / 42 days, **the installed tier is 1.31× colder on the cold bucket**
— the direction pass 23 predicted, at a smaller magnitude than its motivating example implied.

🔴 **Two foundation rows carry the divergence:** `learningequality/kolibri` (head commit 1 d, median
dependency **200 d**, 14/32 cold, including `json-schema-validator` at **3,894 d** and
`zeroconf-py2compat` at 1,156 d — Python-2-era compatibility shims still in the manifest) and
`CAHLR/OATutor` (head commit 7 d, median **604 d**). 🟢 Two read cleanly on both axes:
`towardsai/ai-tutor-app` (median 9 d, **0/20** cold) and `HKUDS/DeepTutor` (median 62 d).

⚠️ **Three licence corrections to the pass-21 closure**, all from the registry classifiers:
`python-dateutil` is **permissive** (Apache-2.0 **and** BSD classifiers) despite a `license` field
reading *"Dual License"*; `semver` is **BSD** despite a field containing the raw notice text; and
🔴 `azure-cognitiveservices-speech`, declared by `oppia/oppia`, is **proprietary** — *"License ::
Other/Proprietary License"*, empty licence field. Full census in `intel/trends.md` §57.

---

## Twenty-fifth pass, 2026-10-07 — the shelf measured whole: 503 slugs, one denominator

Every pass before this one measured a *sample* of the shelf. `p170`'s published denominator is
**200 slugs from 2026-10-03**, and pass 66 left the reservation *"the sweep is redone when
`slugs.input.txt` incorporates this pass's additions"* standing. It stood for twenty-four passes.

🔵 **The denominator this pass uses is every `github.com/owner/repo` cited in the six
non-append-only shelf files: 503 slugs. Only 62 of them are in `p170`'s 200. 441 had never been
measured.** Instrument: `compose/code/p436-fork-hypothesis/` (6 controls, offline).

| Layer | Result |
|---|---|
| licence payload, `raw.githubusercontent.com/<slug>/HEAD/<14 filenames>` | 412 `LICENSED` · 87 `UNLICENSED` · 4 `UNREACHABLE` |
| head commit date, `git fetch --depth 1 --filter=blob:none` | 🟢 **501 of 503 dated** |
| licence family | MIT 215 · Apache-2.0 72 · GPL 40 · AGPL-3.0 23 · LGPL 11 · BSD 10 · ECL-2.0 8 · CC-BY 7 · ISC 2 · CC0 2 · unclassified 22 |

### Liveness of the live-cited shelf, against the reference date `2026-10-07`

| | 503-slug live shelf | pass 24's 884-repo citing tier |
|---|---|---|
| median head-commit age | **48 d** | 42 d |
| committed in 2026 | 72.3% | 73.5% |
| 🔴 cold > 1 yr | **24.8%** | 23.0% |
| 🔴 cold > 2 yr | **16.6%** | 11.1% (pre-2024) |
| committed within 7 d | 31.5% | — |

⚠️ **Read the first comparison, not the headline.** You would expect what a KB *recommends* to be
fresher than what it merely *mentions*. **Measured, it is not** — the live shelf is 48 d against
42 d, and colder on both cold buckets. Nothing in this KB's selection process favours recency, and
this is the number that says so.

🔴 **The 25 coldest rows the KB still cites**, led by `foradian/fedena` **5,108 d (2012-10-12)**,
`inepdadosabertos/api` 4,525 d, `Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor`
3,808 d, `shinyquagsire23/InfiniteCampusAPI` 3,658 d,
`IMSGlobal/LTI-Tool-Provider-Library-PHP` 3,600 d (the row pass 24 removed from **P1**),
`kuali/kc` 3,561 d, `fnshr/kyo-kan` 3,518 d, `kuali/rice` 3,430 d. Full table:
`compose/code/p436-fork-hypothesis/recency.2026-10-07.tsv`.

### 🔴 Six rows on this shelf are cited at a repository's FORMER name

A GitHub rename or transfer leaves the old path working as a redirect, so nothing in a browser
shows that anything has moved. The discriminator costs one call and is exact:
`git ls-remote <old> HEAD == git ls-remote <new> HEAD` ⇒ **one repository, two names**. Found by
asking each repo's **package registry** which repository it declares as its homepage, then
comparing heads.

| Cited here as | The registry declares | Shared head | Direction |
|---|---|---|---|
| [`All-Hands-AI/OpenHands`](https://github.com/All-Hands-AI/OpenHands) | `OpenHands/OpenHands` | `9f05599` | 🔴 the project moved; the KB has the old name |
| [`NVIDIA/NeMo`](https://github.com/NVIDIA/NeMo) | `NVIDIA-NeMo/NeMo` | `50c71db` | 🔴 same |
| [`iterative/dvc`](https://github.com/iterative/dvc) | `treeverse/dvc` | `56e5982` | 🔴 same — and this one is a **transfer between companies**, not a rename |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | `TryxAPI/lrs-conformance-tests` | `5bc232d` | 🔴 same |
| [`stanfordnlp/edu-convokit`](https://github.com/stanfordnlp/edu-convokit) | `rosewang2008/edu-convokit` | `d845ffd` | ⚠️ one repository under two names, **537 d cold either way** |
| [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | `IMSGlobal/openbadges-validator-core` | `0a66b52` | 🟢 **the reverse** — the KB has the post-2022 name and the **registry metadata is stale** |

🔵 **The last row is why this is a channel and not a rule.** Five times the KB was behind the
repository; once the registry was behind the KB. **The head SHA settles it; neither source is
authoritative on its own.** The names are left as published above with a pointer, because both
paths resolve and rewriting a working citation buys nothing — what was missing was the note.

### 🔴 Seven MIT licence files on this shelf name no copyright holder at all

Under **P179**, a licence file is an *identifier* or a *cession*: a cession names a grantor, a year
and the terms. These seven are MIT texts with the terms and **no grantor**:

| Slug | What the copyright line says |
|---|---|
| [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | `Copyright (c) 2026` — a year and nothing else |
| [`AkizumiFox/NTU-COOL-Assignment-Status-Viewer`](https://github.com/AkizumiFox/NTU-COOL-Assignment-Status-Viewer) | `Copyright (c) 2025` — same |
| [`koukekoukej-glitch/feynman-tutor`](https://github.com/koukekoukej-glitch/feynman-tutor) | `Copyright (c) 2026` — same |
| [`r1ckyIn/canvas-ed-mcp`](https://github.com/r1ckyIn/canvas-ed-mcp) | `Copyright (c) 2025` — same |
| [`lebmatter/exampro`](https://github.com/lebmatter/exampro) | 🔴 `Copyright (c) [year] [fullname]` — **the template placeholder, shipped verbatim** |
| [`nguyentrieu210/edu`](https://github.com/nguyentrieu210/edu) | 🔴 same placeholder |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | the copyright line is **absent** |

⚠️ **This is a weaker defect than a wrong licence and a real one.** The MIT grant text is present
and unambiguous in all seven; what is missing is the party making the grant. For a client
redistribution review that is a question someone has to answer, and the repository does not.
🔵 **`adlnet/lrs-conformance-test-suite` is the one to care about** — ADL's xAPI conformance suite
is a standards artefact an engagement cites in a bid, and it is the one with no copyright line.

🔴 **The KB could not see any of this until this pass, because its own instrument could not return
the class.** `p184`'s copyright regex used `\s*` between the word *copyright* and the capture;
`\s` matches a newline, so `Copyright (c) 2026` followed by a blank line **reached across it and
published the next paragraph of the licence as the holder**. All seven were filed as
`HOLDER-UNRELATED` with a sentence of MIT boilerplate in the holder column. Fixed with four new
controls — three negatives and the positive that forbids an instrument answering `NO-HOLDER`
always — in `compose/code/p184-holder-mismatch/` (now 19/19).

## Nine repositories this shelf had written off have their own grant — found by enumerating the tree, 2026-10-07

Pass 25's licence probe used **14 filenames at the repository root** and published **87** slugs as
shipping no licence. `p441` replaces the filename list with a complete tree enumeration — a
`--filter=blob:none --no-checkout --depth 1` clone plus `git ls-tree -r`, which lists every path at
HEAD with no API and no truncation, in **13 seconds for all 87**:

| Instrument | Grants found in the 87 |
|---|---|
| 14 filenames, rooted (`p436`) | **0** |
| 41 filenames, rooted (`p440/widen.py`) | 1 |
| 🟢 complete tree enumeration (`p441`) | 🟢 **9** |

| Repo | Licence | Where it actually is | The axis a filename list cannot reach |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | `LICENSE.TXT` | **extension case** |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **MIT** | `License` | **a third capitalisation** |
| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | **GPL-2.0-or-later with two exceptions** | `copying.txt` | **lowercase `COPYING`**, which the probe list carries only in uppercase |
| [`veraPDF/veraPDF-library`](https://github.com/veraPDF/veraPDF-library) | ⚠️ **GPL-3.0 + MPL-2.0**, dual | `LICENSE.GPL` **and** `LICENSE.MPL` | **family suffix** — two grants cannot both live in a file called `LICENSE` |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | 🟡 **EUPL-1.2** | `aoe-web-backend/LICENSE` · `aoe-web-frontend/LICENSE`, 303 B each | **depth** |
| [`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) | 🔴 **NCSA** (code — *not* MIT, corrected in the twenty-seventh pass) **+ CC-BY-4.0** (content, output) | `LICENSE/LICENSE.code` · `LICENSE.original` · `LICENSE.output` | **a licence DIRECTORY holding three grants** |
| [`learningequality/kolibri-server`](https://github.com/learningequality/kolibri-server) | **GPL** | `debian/copyright` | **the Debian packaging convention** |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) · [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | 🔴 **unread — RTF** | `docs/License.txt` plus a `docs/LICENSE.rtf` the classifier cannot read | **format**, which is a limit and not an absence |

🔵 **[`cs341-illinois/coursebook`](https://github.com/cs341-illinois/coursebook) is the row that makes
the whole case.** Separate grants for the **code** (**NCSA** — corrected in the twenty-seventh pass from MIT; the
University of Illinois/NCSA licence quotes MIT's grant sentence verbatim, so a classifier probing
for that sentence returns MIT), the **original content** and the **output**
(CC-BY-4.0) is the *correct* structure for a course repository, and it is the structure a single `LICENSE`
file cannot express. A rooted filename probe therefore reports a teaching repository with exemplary
licensing hygiene as having none at all. For a client who wants a course scaffold whose content and
code licences are separable — which is what every corporate-academy engagement needs — this is the
shape to copy.

⚠️ **`nvaccess/nvda` is GPL-2.0-or-later *with two special exceptions*, and the exceptions are the
point.** The grant is not a plain GPL row: `copying.txt` opens *"NVDA is available under the GNU
General Public License version 2 or later, with two special exceptions"*, one of which permits linking
with certain non-GPL code. 🔴 **This KB's family classifier returns `LGPL` for that payload**, because
the exception text names the LGPL — see the limit recorded in trend 62. **Read the file before quoting
a verdict on NVDA**; it is the screen reader every accessibility engagement in the EMEA public sector
will meet, and "GPL" and "GPL with a linking exception" are different answers to a client's question.

### 🟡 The EUPL tier was machine-unreadable in this KB until this pass

[`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) is one of **eight Finnish national
education services** this shelf already lists under **EUPL-1.1 or EUPL-1.2** — `eperusteet`, `koski`,
`ataru`, `organisaatio`, `oppijanumerorekisteri`, `ehoks`, `suorituspalvelu` and `aoe`. Nine of this
KB's files discuss the EUPL in prose. 🔴 **And both of its licence classifiers returned `UNKNOWN` for
the string**, so the single tier a European public-sector engagement starts from was invisible to every
automated check this repository runs.

Both now recognise it, classified **STRONG-COPYLEFT**, with six controls:

- 🔴 **Article 5 carries a copyleft obligation, and Article 1's definition of "Communication" covers
  network use** — so the EUPL binds a **hosted service**, not only a shipped binary. For a SaaS
  deliverable built on an EUPL component that is the clause that decides the engagement.
- ⚠️ **EUPL-1.2's Appendix lists GPL-2.0, AGPL-3.0, LGPL-2.1, MPL-2.0 and EPL-1.0 as compatible
  licences**, which is a **re-licensing option for derivative works** and not a softening of the EUPL
  itself. Nothing in this KB treats it as one.
- 🔵 The Appendix is also why the classifier has to probe EUPL **first**: an EUPL payload carries the
  marks of five other families, exactly as an MPL-2.0 payload carries three GNU marks.
- 🟢 **Commercially it is workable and it is the licence the European Commission recommends for
  public-sector software**, so an EMEA public-sector engagement should expect it rather than treat it
  as an exception.

### 🔴 Five MPL-2.0 repositories were filed as GPL by this KB's own instrument, while its prose had them right

`p436`'s family classifier probed the GNU family before Mozilla's. MPL-2.0 **section 1.12** defines
*"Secondary License"* by naming the GNU **GPL-2.0, LGPL-2.1 and AGPL-3.0**, so every MPL-2.0 payload
carries all three marks:

| Repo | Filed | Actually, from the first line of its payload |
|---|---|---|
| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | GPL | **MPL-2.0** |
| [`ocrmypdf/OCRmyPDF`](https://github.com/ocrmypdf/OCRmyPDF) | GPL | **MPL-2.0** |
| [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) | GPL | **MPL-2.0** |
| [`idiap/coqui-ai-TTS`](https://github.com/idiap/coqui-ai-TTS) | GPL | **MPL-2.0** |
| [`edrys-org/edrys`](https://github.com/edrys-org/edrys) | GPL | **MPL-2.0** |

🟢 **Every one of the five is already described correctly as MPL-2.0 in this file and in
`agents/top.md`** — the prose was right and the measurement was wrong, which is trend 61. 🔴 **The
commercial verdict inverts between the two answers:** GPL is strong copyleft and a blocker for a
client deliverable; MPL-2.0 is **file-level** copyleft, so using the component unmodified as a
dependency does not reach the studio's own files. **Four of the five are tools a studio would reach
for** — `axe-core` is the engine inside every MIT accessibility agent on this shelf, and this KB's own
`a11ymcp` row declares it at runtime.

🔵 **The symptom needed no fetch: the published family distribution over 412 licensed payloads
contained ZERO MPL-2.0 rows.** Fixed by probing EUPL, then MPL and EPL, before the GNU family, with
**15 controls** that pair each positive against a GNU payload which must not move.

## Added in the twenty-ninth pass of 2026-10-07 — corrections to the licence column, and the EUPL tier gains a version

No new foundational layers. What changed is the **licence column on layers this page already
recommends** — and here a wrong licence is worse than a missing row, because these are the
pieces a client build links against.

🔵 **All of it came from one file pass 28 never opened.** Pass 28 repaired three defect
classes in `sweep_payload.family_of`. `lib/license_family.sh` — the **shared** classifier,
sourced by 27 instruments — still carried all three.

### 🟢 Five repositories are MPL-2.0, not GPL

| Repo | published | 🟢 corrected | Layer |
|---|---|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | `GPL-3.0` | **MPL-2.0** | accessibility testing |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | `GPL-3.0` | **MPL-2.0** | document ingestion |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | `GPL-3.0` | **MPL-2.0** | speech synthesis |
| [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | `GPL-3.0` | **MPL-2.0** | speech synthesis (maintained fork) |
| [edrys-org/edrys](https://github.com/edrys-org/edrys) | `GPL-3.0` | **MPL-2.0** | live classroom |

🔴 **The cause, and this is the second time this KB has paid for it.** MPL-2.0 **§1.12**
defines *"Secondary License"* by naming *"the GNU General Public License, Version 2.0, the
GNU Lesser General Public License, Version 2.1, the GNU Affero General Public License,
Version 3.0"* — so **every MPL-2.0 payload carries all three GNU marks**, and a classifier
probing the GNU family first takes the payload.

⚠️ **Pass 26 measured this, named these exact five repositories, fixed it, and wrote it up —
in the other classifier.** Three passes later the identical defect sat in
`lib/license_family.sh`, on the same five rows. `P237` said a correction living in prose is
not a control. `P454` adds: **a correction living in one of two implementations is not one
either.**

🟢 **Why it matters for selection, not bookkeeping.** MPL-2.0 is **file-level** copyleft: you
may link it into a proprietary application and must publish changes only to the MPL files.
GPL-3.0 is **project-level**. Recorded as GPL, all five looked like they would infect a
client deliverable; they do not. **Two of the five are the TTS layer**, so the speech
substrate this KB recommends for offline and mother-tongue tutoring was marked unusable and
is not.

### 🟢 The EUPL public-sector tier now resolves to a version — and it is mostly 1.1

`lib/license_family.sh` had **no EUPL branch at all** before this pass (`P453`), so all nine
EUPL payloads read `UNCLASSIFIED` from it. They now resolve, with the version:

| Repo | 🟢 family | Region | Country |
|---|---|---|---|
| [Opetushallitus/ehoks](https://github.com/Opetushallitus/ehoks) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/eperusteet](https://github.com/Opetushallitus/eperusteet) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/koski](https://github.com/Opetushallitus/koski) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/oppijanumerorekisteri](https://github.com/Opetushallitus/oppijanumerorekisteri) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/organisaatio](https://github.com/Opetushallitus/organisaatio) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/valtionavustus](https://github.com/Opetushallitus/valtionavustus) | **EUPL-1.1** | EMEA | Finland |
| [Opetushallitus/ataru](https://github.com/Opetushallitus/ataru) | **EUPL-1.2** | EMEA | Finland |
| [Opetushallitus/suorituspalvelu](https://github.com/Opetushallitus/suorituspalvelu) | **EUPL-1.2** | EMEA | Finland |
| [european-commission-empl/European-Learning-Model](https://github.com/european-commission-empl/European-Learning-Model) | **EUPL-1.2** | EMEA | EU |

⚠️ **Read this before building on the tier: six of nine are EUPL-1.1, not 1.2.** The two
versions carry **different compatibility lists** — 1.2's Appendix adds licences 1.1's does
not — so a build composing this tier with GPL, MPL or EPL components cannot treat the `EUPL`
label as uniform. Resolve the version per repository, which is now possible.

🔵 **Both of the tier's shapes need covering.** The eight Finnish services carry **no licence
title at all**: they open on a copyright line and concede in prose — *"Licensed under the
EUPL, Version 1.1 or — as soon as they will be approved by the European Commission —
subsequent versions"*. Only the Commission's own payload ships the full licence text with the
name as a title. A title probe alone misses eight of nine; a grant-phrase probe alone misses
the one that matters most.

🔴 **The consequence nobody had stated.** With the family `UNCLASSIFIED`, `P250`'s gate never
fired on these nine, so their **commercial-use verdict came from the body token match**
rather than from an identified family — the route `P171` declares unsafe. The answer it gave
is right (**the EUPL permits commercial use**), but it was right **by luck**, across the whole
EMEA public-sector tier, for every pass before this one.

### 🔴 And one correction where the grant is not in the root at all

| Repo | published | 🟢 corrected | Where the grant actually is |
|---|---|---|---|
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | `LGPL?` | **GPL-2.0** | `docs/License.txt`, 17,286 B — **no root licence exists** |
| [OS4ED/openSIS-Responsive-Design](https://github.com/OS4ED/openSIS-Responsive-Design) | `LGPL?` | **GPL-2.0** | same |

Neither appears among the 412 root payloads this shelf sweeps. They are the clearest case on
this page for why `p441`'s tree enumeration exists: **for these two the subtree is the only
licence evidence there is**, and until this pass the family read from it was wrong.

### ⚠️ One layer still unreadable by the Python classifier, declared not patched

[opendatalab/MinerU](https://github.com/opendatalab/MinerU) — the PDF/document → structured
text layer under curriculum parsing — answers **Apache-2.0** from the shell and `UNKNOWN`
from `sweep_payload.family_of`. Its `LICENSE.md` says *"MinerU is licensed under Apache
License 2.0"*, naming licence and version in one token, and the Python probe requires a
separate `"version 2.0"` string, so every **prose** declaration of Apache is excluded. The
row on this page is **Apache-2.0** and correct; the instrument disagrees, and the fix is
pre-registered rather than applied to a file pass 28 rewrote hours earlier.

## Added in the thirty-first pass, 2026-10-07 — the DIKSHA service tier

| Repo | Licence (read from payload) | ★ | Region | Why it is foundational |
|---|---|---|---|---|
| [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | **MIT** (`master/LICENSE`, "Copyright (c) 2018 Project Sunbird") | not read this pass | APAC | The LMS service tier of **Sunbird**, India's education digital public infrastructure and the stack behind **DIKSHA** — national-scale, and **MIT**, which is rare at this scale in public-sector education. With `Sunbird-Ed/SunbirdEd-portal` (MIT, already shelved) this gives a licence-clean LMS core to put agents on top of, rather than retrofitting Moodle's GPL-3.0 tree. |
| [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book) | **Apache-2.0** (`main/LICENSE`) | not read this pass | APAC | Redistributable agent-engineering curriculum — the enablement layer of an engagement, usable in client-facing training material because Apache-2.0 permits it. |

⚠️ **Not added, and why.** [`pawtograder/platform`](https://github.com/pawtograder/platform) is the
most architecturally interesting thing found this pass (MCP server over a real gradebook) but is
**GPL-3.0-or-later** — it belongs in `agents/top.md` with a copyleft flag, not in a foundations shelf
that implies a proprietary-safe base. `datawhalechina/hello-agents` is **CC BY-NC-SA 4.0** and
`a5anka/ai-lab-2026-africa-agent-manager` carries **no licence file**; neither is a foundation.

Verification: licence payloads over `raw.githubusercontent.com`, 404 negative control run in the same
pass. `curl -sI github.com` is 403 via this session's proxy; `api.github.com` is 403, so no star
counts were read.
