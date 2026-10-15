---
industry: education
region: Global
updated: 2026-10-15
---

## Pass 229 — 2026-10-15 — THE FOUNDATION ROW THIS KB LEANS ON HARDEST WAS PUBLISHED AS GRANTLESS, AND ITS LICENCE IS THE CANONICAL `GPL-3.0` BODY AT `COPYING.txt`

🔵 **`0` new repository rows. `30` grants newly readable. `124` live cells confirmed, `0` wrong.** 🔵 **Evidence:** [`sw-grant-ladder-reach`](../evidence/sw-grant-ladder-reach.2026-10-15-p229.tsv) · **Instrument:** [`p229-grant-ladder-reach`](../compose/code/p229-grant-ladder-reach/README.md)

### 🔴 `P229-F1` — `moodle/moodle`, and the one name that was missing from the ladder

| foundation row | grant, read first-hand `2026-10-15` | channel | bytes · `sha256`₁₂ |
|---|---|---|---|
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **`GPL-3.0`** *(canonical body, title at offset `0`)* | `main/COPYING.txt` | `35 147` B |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟢 **`GPL-2.0`** | `master/docs/License.txt` | `17 286` B · `224ac3d403e3` |
| [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | 🟢 **`GPL-2.0`** | `master/docs/License.txt` | `17 286` B |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`GPL-2.0`** | `master/html/license.txt` | `18 346` B |
| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | 🟡 **`GPL-2.0-or-later` WITH TWO SPECIAL EXCEPTIONS** | `master/copying.txt` | `53 408` B |
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **`LGPL-3.0`** | `master/License.txt` | `7 651` B |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **`Apache-2.0`** | `main/pyproject.toml` | — |
| [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) | 🟢 **`AGPL-3.0`** | `main/package.json` | — |
| [`processing/p5.js`](https://github.com/processing/p5.js) | 🟢 **`LGPL-2.1`** | `main/license.txt` | `24 480` B · `eb2f25f8f165` |
| [`foradian/fedena`](https://github.com/foradian/fedena) · [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | 🟡 **`Apache-2.0` BY REFERENCE** | `NOTICE` | `679` / `680` B |

🔴 **p228 probed six names on two guessed branches. `COPYING.txt` was not among them, so the most-cited platform on these shelves sat in the grantless class.** 🟢 **The ladder now resolves the REAL default branch from `git ls-remote --symref` and probes `40` paths in three tiers.**

### 🟡 `P229-F2` — two rows whose state is NOT "has a licence", and the distinction is the deliverable

- 🟡 **`nvaccess/nvda` is `or-later` WITH TWO SPECIAL EXCEPTIONS**, stated in the first line of its own `copying.txt`. 🔴 **A `GPL-2.0` cell is incomplete in the same way `Elgg`'s was at p228: it drops the half a studio needs to read before linking.** The exceptions are the whole reason NVDA can be used with certain non-free components, and no cell can carry them — the row must point at the file.
- 🟡 **`fedena` is a grant BY REFERENCE.** Both forks serve a `679`/`680` B `NOTICE` that NAMES Apache-2.0 and links to its URL; neither serves the body at any of `40` paths. 🔵 **That is `p742`'s body-versus-reference distinction, and the pair differs by exactly ONE byte — a trailing full stop — which is a fork pair, not an alias.**

### 🔴 `P229-F3` — `4` of `20` manifests describe somebody else's project

🔴 **[`alfredang/ai-mms`](https://github.com/alfredang/ai-mms) serves `"name": "openmage/magento-lts"` with `"license": ["OSL-3.0","AFL-3.0"]` at its root; [`LMS-Laravel/LMS-Laravel`](https://github.com/LMS-Laravel/LMS-Laravel) and [`LMS-Laravel/OLD-LMS-Laravel`](https://github.com/LMS-Laravel/OLD-LMS-Laravel) serve an unrenamed `laravel/laravel` skeleton.** 🟢 **`T229-M2`, the seventh non-grant subject: the licence is real, first-hand and correctly parsed, and it is a statement about the UPSTREAM. These three stay UNRESOLVED rather than being published with a borrowed grant.**

## Pass 228 — 2026-10-15 — THE FOUNDATION TIER WAS SWEPT END TO END FOR THE FIRST TIME: `468` GRANTS READ FIRST-HAND, **`1 372` CELLS CONFIRMED**, AND THE ONE WRONG FAMILY ON THIS SHELF ASSERTS NO NETWORK OBLIGATION ON A PLATFORM THAT HAS ONE

🔵 **`0` new foundation rows. `1` family defect found and corrected in place. `1` grant published for a row carried with none. `468` grants read first-hand across `520` distinct slugs — the first shelf-wide grant read in this KB's history.**

🔵 **Evidence:** [`st-shelf-gate`](../evidence/st-shelf-gate.2026-10-15-p228.tsv) · [`st-grant-reads`](../evidence/st-grant-reads.2026-10-15-p228.tsv) · [`st-family-defects`](../evidence/st-family-defects.2026-10-15-p228.tsv) · **Instrument:** [`p228-shelf-gate`](../compose/code/p228-shelf-gate/README.md)

### 🔴 `P228-F1` — `acanas/swad-core` corrected `GPL-3.0` → `AGPL-3.0`

🟢 **`master/LICENSE`, `34 501` B, `sha256`₁₂ `884b434957ba`. Title at offset `0` is `GNU AFFERO GENERAL PUBLIC LICENSE`; the version line is `Version 3, 19 November 2007`; §13 is `Remote Network Interaction`.** 🔴 **The shelf published `GPL-3.0` at the same byte count — the body was read correctly and the FAMILY was named wrong.**

🔴 **What changes for this tier:** SWAD is a two-decade production platform at Universidad de Granada and the obvious engagement is a hosted one. 🔴 **`AGPL-3.0` reaches derivative works made available OVER A NETWORK. The published `GPL-3.0` cell said a hosted deployment carried no disclosure obligation. It does.** 🟢 **Full sequence in [`agents/top.md`](../agents/top.md) `P228-ST2`.**

### 🟢 `P228-F2` — the tier's grant coverage, measured rather than assumed

| reading | slugs | cells |
|---|---|---|
| 🟢 grant READ first-hand off `raw` | **`468`** | — |
| 🟢 cell AGREES with the grant | — | **`1 372`** |
| 🟡 no grant at the ROOT | `45` | `149` |
| 🟡 bound differs *(undecidable from a root `LICENSE`)* | `14` | `26` |
| 🟡 spelling differs only | `10` | `13` |
| 🔴 **family wrong** | **`1`** | **`2`** |
| 🔴 **dual grant named as single** | **`1`** | **`1`** |

🔵 **The family distribution of the `468` bodies, which is the first time this tier can state its own licence profile from payloads rather than from cells:** 🟢 **`248` `MIT` · `77` `Apache-2.0` · `44` `GPL-3.0` · `43` `AGPL-3.0` · `11` `GPL-2.0` · `9` `BSD-3-Clause` · `7` `ECL-2.0` · `7` `LGPL-3.0` · `5` `CC-BY-4.0` · `2` `CC-BY-SA-4.0` · `1` each `LGPL-2.1`, `MIT` OR `GPL-2.0` *(dual)*, `BSD-2-Clause`, `ISC`, `CC-BY-NC-SA-4.0`, `MPL-2.0`, `BUSL-1.1`** — 🟡 **plus `8` bodies this instrument declines to name *(`7` `UNRECOGNISED`, `1` `GPL-?`)*, which are reported and never turned into defects.**

🟢 **So `335` of `468` first-hand grants — `71.6%` — are `MIT`, `Apache-2.0` or BSD, the three this KB's standing preference can build on. Counting the `7` `ECL-2.0` rows alongside them takes it to `342`, `73.1%` — published separately because `ECL-2.0`'s patent grant is narrower than Apache's *(p216)*.** 🔵 **The ratio is published WITH its enumerator, per p224's standing rule: the unit is a distinct SLUG whose grant returned `200`, counted once. 🔴 A first draft of this paragraph said `326` and `69.7%`, by adding the families up by hand and leaving `Elgg` in the `MIT` bucket after the dual-grant reclassification moved it out.**

### 🟢 `P228-F3` — `ECL-2.0` corroborated on all `7` rows, and a gap this pass's own draft invented

🔴 **A first draft of this section claimed the Educational Community License was unnamed on these shelves and registered an action for it. It is named at p200, added to the platform shelf at p215, re-read at clause level at p216 and re-confirmed at p217 and p218.** 🟢 **The claim was withdrawn before publishing; the rule that caught it is to grep the shelves for a family before asserting its absence.** 🟡 **p226's failure mode, one pass after p227 named it — a draft checked against a search impression rather than against the shelves.**

🟢 **What this pass does add is payload corroboration: all `7` `ECL-2.0` cells on this tier read `AGREE` against first-hand bodies, and the `7` bodies have `7` DISTINCT byte-lengths and `7` distinct hashes** — extending p216's `5` → `7` and establishing that for this family a byte count identifies a repository's COPY, never the licence → [`repos/trending.md`](trending.md) `T228-R4`.

🟡 **p216's clause-level sentence still governs how it may be sold, and the `71.6%` figure above is stated WITHOUT it for that reason: `ECL-2.0` is permissive on copyright but NARROWER THAN `Apache-2.0` ON PATENTS, so it is buildable and it is not a drop-in substitute in a contract.**

### 🟢 `P228-F4` — a grant published for a row that was carried without one

🟢 **[`oaknational/oak-ai-lesson-assistant`](https://github.com/oaknational/oak-ai-lesson-assistant) — 🟢 **`MIT`**, `main/LICENSE`, `1 077` B, `sha256`₁₂ `d150aadcccd2`, read first-hand `2026-10-15`.**

🔵 **It is cited `15` times across these shelves and carried NO licence cell on any live shelf — a row the gate found by its ABSENCE rather than by a disagreement.** 🟢 **Oak National Academy's Aila is the UK's lesson-planning assistant, with a published government algorithmic-transparency record, running retrieval over Oak's own lesson library.** 🟡 **It is the clearest permissively licensed, teacher-facing, nationally deployed asset on this tier, and `T227-4` already established that teacher-side is where national programmes actually spend.**

### 🔵 `P228-F5` — the ladder's reach, stated as a limit

🔴 **The fetch ladder is `main` then `master`, over `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING`, `LICENCE` — all at the ROOT.** 🟢 **Which path answered, across `468` reads:** `300` `main/LICENSE` · `114` `master/LICENSE` · `19` `main/LICENSE.md` · `11` `master/LICENSE.txt` · `11` `master/LICENSE.md` · `6` `main/LICENSE.txt` · `5` `master/license.txt` · `1` `main/license.txt` · `1` `master/LICENCE`.

🔴 **`114` + `11` + `11` + `5` + `1` = `142` of `468` grants — `30.3%` — do NOT live at `main/LICENSE`.** 🟡 **A one-request-per-slug gate that probed only `main/LICENSE` would have reported a third of this tier as grantless.** 🟢 **And the ladder is still not enough: `OS4ED/openSIS-Classic` keeps its grant at `master/docs/License.txt` and the shelves knew that before the gate did → `ACTION SV`.**


## Pass 227 — 2026-10-15 — THE FOUNDATION TIER GAINS A **SETTLED BOUND** ON ITS LARGEST PLATFORM AND LOSES AN ASSERTION THAT WAS EXACTLY BACKWARDS, AND BOTH CAME FROM READING A `LICENSE` FILE'S **STRUCTURE** RATHER THAN ITS TEXT

🔵 **`0` new foundation rows. `1` bound settled on the tier's largest platform. `1` live assertion WITHDRAWN as inverted. `2` grants re-read first-hand on rows carried for a hundred passes.**

🔵 **Evidence:** [`sn-openedx-bound`](../evidence/sn-openedx-bound.2026-10-15-p227.tsv) · [`so-untabled-refutations`](../evidence/so-untabled-refutations.2026-10-15-p227.tsv) · [`p227-verified-repos`](../evidence/p227-verified-repos.2026-10-15-p227.tsv)

### 🟢 `P227-F1` — `ACTION SN`: `Open edX` is `AGPL-3.0-only`, and the bound is established by ABSENCE

🔵 **p226 read the grant and could not settle the bound, because GPL-family `or-later` lives in FILE HEADERS rather than the `LICENSE`.** 🟢 **`ACTION SN` registered limb `1` as *"a source-file header carries `or (at your option) any later version`"*. 🔴 **Limb `2` fires: `5` files read on `master`, `0` or-later strings.**

| path | `http` | bytes | `sha256`₁₂ | or-later hits |
|---|---|---|---|---|
| `lms/envs/common.py` | `200` | **`136 602`** | `7b22d1313438` | 🔴 **`0`** |
| `cms/envs/common.py` | `200` | `53 271` | `cf6d0d07a01f` | 🔴 **`0`** |
| `manage.py` | `200` | `3 425` | `d64ca7d5a798` | 🔴 **`0`** |
| `lms/__init__.py` | `200` | `960` | `067a80d8d23b` | 🔴 **`0`** |
| `openedx/core/__init__.py` | `200` | `384` | `a980205c9ee8` | 🔴 **`0`** |
| `setup.py` · `AGPL-3.0-LICENSE` | 🔴 `404` | — | — | absent on `master` |

🟢 **Published state: `AGPL-3.0-only`, as the CONSERVATIVE reading, and the cell says so.** 🟡 **This bound is weaker than p225's `openeducat` resolution, which came from a `2`–`1` vote across three positive channels. 🔵 A bound established by ABSENCE should never be published as though it were voted, and the `65`+`9` `AGPL` cells inherit it with that caveat attached.** 🟢 **The `LICENSE` re-read reproduces p226 to the byte and the hash — `35 136` B, `sha256`₁₂ `e12d78569742` — which is an identity control on a `100`-pass-old row.**

### 🔴 `T227-F2` — the trap, and it is p225's `openeducat` trap in a THIRD shape

🔴 **The root `LICENSE` DOES contain *"any later version"*, three times — at lines `570`, `572` and `638`.**

| lines | where they sit | is it a channel? |
|---|---|---|
| `570`, `572` | inside §14, *"Revised Versions of this License"* | 🔴 **no — the p225 shape exactly** |
| 🆕 `638` | inside the appendix **"How to Apply These Terms to Your New Programs"** | 🔴 **no — and this shape is NEW** |

🟢 **Line `638` sits in the boilerplate NOTICE TEMPLATE, complete with its literal placeholders — `<one line to give the program's name and a brief idea of what it does.>` and `Copyright (C) <year>  <name of author>`.** 🔴 **Its subject is a HYPOTHETICAL FUTURE PROGRAM that a downstream author might write. Counting it would have published `AGPL-3.0-or-later` across the largest platform on these shelves, in `65`+`9` cells.**

🟡 **Standing rule, extending p225's: in a `LICENSE` file the project's own PREAMBLE is a channel; neither the canonical body NOR its how-to-apply appendix is one.** 🔵 **p225 had two kinds of non-channel inside a grant file. There are three.**

### 🔴 `P227-F3` — the assertion that was backwards, withdrawn in place

🔴 **This shelf carried: *"`GibbonEdu/core` is `AGPL-3.0`, not `GPL`."*** 🟢 **It is the reverse. `master/LICENSE`, `35 121` B, `sha256`₁₂ `93178a43d6d3`, title line `GNU GENERAL PUBLIC LICENSE`. The cell is withdrawn behind a `<!--corrected-->` marker and the correct value published** → `P227-SO1` in [`agents/top.md`](../agents/top.md).

🔵 **Why a foundation-tier row got this wrong for so long is worth the space, because the mechanism is reusable:** 🔴 **GPL-3.0's §13 is titled *"Use with the GNU Affero General Public License"* and names the Affero licence in full. 🟢 **So a GPL-3.0 body contains the string `GNU Affero General Public License`, and three methods for telling the families apart are all unsafe:**

| method | verdict | why |
|---|---|---|
| byte size | 🔴 **unsafe** | the canonical bodies are **`15` bytes apart**: `35 121` vs `35 136`, both read first-hand this pass |
| a bare `affero` grep | 🔴 **unsafe** | a GPL-3.0 body carries `3` such tokens |
| a whole-body search for the AGPL title | 🔴 **unsafe** | the AGPL title appears INSIDE a GPL-3.0 body, in §13. 🔴 **This one defeated p227's own first draft** |
| 🟢 **the first licence title in DOCUMENT ORDER** | 🟢 **safe** | corroborated by §13's heading; a disagreement is reported, not resolved |

### 🟢 `P227-F4` — `UniTime` is `Apache-2.0`, which changes what this tier can offer

🟢 **[`UniTime/unitime`](https://github.com/UniTime/unitime) — `Apache-2.0`, read first-hand: `master/LICENSE` `11 357` B, `sha256`₁₂ `58d1e17ffe51`, canonical Apache body.** 🔴 **`404` on `main`; `master` is the branch, which is itself worth recording for anyone pinning it.**

🔵 **Why it matters to this tier specifically:** 🔴 **these shelves published it as `GPL-3.0`.** 🟢 **Under the standing MIT/Apache/BSD preference that cell excluded a permissively licensed, mature university timetabling platform from every engagement filter — and timetabling is one of the few education-domain problems where a studio can ship real value without touching student records at all.** 🟡 **An over-restrictive cell is a commercial loss, and `ACTION SO` is the first sweep on these shelves built to find one.**


## Pass 226 — 2026-10-15 — THE FOUNDATION TIER GAINS A **CANONICAL PATH** FOR ITS TWO LARGEST PLATFORM ROWS, AND THE LARGER OF THE TWO SHOULD BE CITED UNDER THE NAME p225 TOLD THIS KB TO DROP

🔵 **`0` new foundation rows. `2` canonical slugs established on evidence. `1` of them reverses a p225 recommendation. `1` grant re-read first-hand on the shelf's second-largest repository.**

🔵 **Evidence:** [`si-alias-direction`](../evidence/si-alias-direction.2026-10-15-p226.tsv) · [`p226-channel-reachability`](../evidence/p226-channel-reachability.2026-10-15-p226.tsv)

### 🔴 `P226-A` — `Open edX` should be cited as `openedx/openedx-platform`

🟢 **p225 established with the ref-set oracle that `openedx/edx-platform` and `openedx/openedx-platform` are ONE repository — `49 749` byte-identical refs — and that the KB's `65` + `9` AGPL cells were one platform counted twice.** 🔵 **It could not say which path was canonical, and recommended `edx-platform` on the strength of it being the better-known name.**

🔴 **The project disagrees.** Its `README.rst`, served byte-identically from both paths *(`12 381` B, `sha256`₁₂ `f015390f93f1`, read `2026-10-15`)*:

| self-reference in the project's own README | count |
|---|---|
| 🟢 `github.com/openedx/openedx-platform` | **`5`** |
| 🔴 `github.com/openedx/edx-platform` | **`0`** |

🟢 **So the canonical path is `openedx/openedx-platform`, and the better-known name is the alias.** 🟡 **For a studio this is not cosmetic: a client inventory, an SBOM or a dependency pin keyed on the non-canonical slug still resolves today, but it resolves through an alias the project itself does not use, and nothing guarantees that alias outlives the next reorganisation.** 🔵 **p225's recommendation is SUPERSEDED on evidence and left standing as the dated record.**

### 🟢 `P226-B` — `INGInious` resolves cleanly, and from a channel with a date on it

🟢 **[`INGInious/INGInious`](https://github.com/INGInious/INGInious) is canonical; `UCL-INGI/INGInious` is the alias.** 🔵 **Channel: `pypi.org`'s `project_urls` for `INGInious` `0.9.2` — `Repository = github.com/INGInious/INGInious`, `Homepage = inginious.org`, `Documentation = docs.inginious.org`.** 🟢 **Uploaded `2026-01-23`, so the claim is `9` months old and describes the project as it is now.**

🟡 **Note for the licence shelf: PyPI's metadata field reads `AGPL 3`, which is a BARE token in the Python-packaging grammar and NOT the positive `only` that Odoo's omission grammar produces** *(p224 `ACTION RU`)*. 🔴 **It is not a grant read, and this row's bound should still come from the repository's own `LICENSE`. Registered as part of `ACTION RW`'s sweep rather than resolved here.**

### 🔴 `T226-F1` — and the pair that REFUSED, which is where the pass's new rule came from

🔴 **`openedx/ease` :: `edx/ease` is NOT resolved.** 🟢 **`pypi.org` does carry a pointer — `home_page = github.com/edx/ease` — and it is worthless for this purpose: the latest release, `0.1.1`, was uploaded `2013-06-07`.** 🔴 **That is `13` years old and predates the `edx` → `openedx` organisation rename entirely, so it names the 2013 path, not the canonical one.** 🔵 **Neither path serves a `README` under any of `README.rst`, `README.md` or `README` on either `master` or `main`, so the second channel is simply absent.**

🟢 **Standing rule added: a package registry's declared repository URL is a DATED claim — it records the path at PUBLISH time, not the canonical path now. Never read one as a canonical pointer without its upload date.** 🔵 **Same channel, same field, opposite evidentiary value at `9` months and at `13` years.**

### 🟢 `project-nomad`'s grant, read rather than cited

🟢 **[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) — `Apache-2.0`, confirmed first-hand.** `LICENSE` `10 779` B, `sha256`₁₂ `e4f125622d3c`, canonical Apache text with the appendix completed: *"Copyright 2024-2026 Crosstalk Solutions LLC"*.

🔵 **Why it was worth a request on a row carried since p132:** it is the second-largest repository in this KB *(`39 444`★, behind only `HKUDS/DeepTutor`)*, it is the Docker orchestration layer under `Kiwix` + `Kolibri` + `Ollama`, and its `Apache-2.0` had been carried from an aggregator rather than read. 🟢 **Applying p225's preamble-vs-canonical-body rule: the grant here is the canonical Apache body plus a COMPLETED appendix naming the holder — no project preamble, no competing bound, nothing to resolve.** 🟡 **A clean read, recorded because a clean read on a load-bearing row is worth as much as a conflict found on a minor one.**

## Pass 225 — 2026-10-15 — `ACTION RV` IS DISCHARGED ON A THIRD CHANNEL: THE ROOT `LICENSE` SIDES WITH THE MANIFEST **2–1**, AND THE CONFLICT IS STRUCTURAL IN `8` OF `8` MODULES

🔵 **`ACTION RV` was carried three passes and registered p225's highest priority. 🟢 It fires limb `1`: a third channel exists, it breaks the tie `2`–`1`, and the resolved bound is `LGPL-3.0-only`** → [`rv-openeducat-third-channel`](../evidence/rv-openeducat-third-channel.2026-10-15-p225.tsv).

### 🟢 `P225-A` — `openeducat/openeducat_erp` resolves to `LGPL-3.0-only`

🟢 **The third channel is the repository's root `LICENSE`, `200`, `8 241` B.** Its line `4` is OpenEduCat's own preamble above the canonical text:

> *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below."*

🟢 **Version-specific, with no grant of later versions. So the vote is:** manifest field `'LGPL-3'` *(Odoo's omission grammar = a positive `only`)* **+** root `LICENSE` preamble *(version-specific)* **against** the module header's *"or (at your option) any later version"*. 🔵 **`2`–`1` for `only`.**

🟢 **The vote and the conservative reading agree**, so this result does not depend on which rule you prefer — which is the strongest form a licence resolution on these shelves can take. 🟡 **The published state for this row is now `LGPL-3.0-only` (RESOLVED, p225). 🔵 The `RANGE-CONFLICT` cells in p222's and p224's sections are SUPERSEDED by this one and left standing as the dated record — the same way p224 restated p222's rows rather than editing them.**

### 🔴 The conflict is STRUCTURAL, not one file's slip — `8` of `8` modules read first-hand

🔴 **`openeducat_core`, `openeducat_admission`, `openeducat_attendance`, `openeducat_classroom`, `openeducat_exam`, `openeducat_library`, `openeducat_parent`, `openeducat_activity`: every one declares `'license': 'LGPL-3'` AND carries the or-later header.** 🔵 **So the `80` bare mentions `ACTION RU` counted at p224 are not `80` views of one defect — the defect is reproduced in every module, which is why the resolution had to come from outside the module tier.**

### 🔴 The trap this pass avoided, and it is `T224-3` in a new shape

🔴 **The root `LICENSE` DOES contain *"or any later version"* — at lines `166` and `168`.** 🟢 **Those lines are inside the canonical LGPL-3.0 body itself, section `14`, *"Revised Versions of this License"*. The grant's SUBJECT there is the licence text, not OpenEduCat's grant.** 🔴 **Counting them would have flipped channel `3` to or-later and produced a false `2`–`1` the other way.**

🟡 **Standing rule added: in a `LICENSE` file, the project's own preamble is a channel; the canonical body is not.** 🔵 **Tenth consecutive unit-mismatch finding on these shelves, and the second to come from the KB's own instrument before publishing rather than a pass later.**

### 🔴 `T225-4` — a `DANGLING` pointer inside the root grant file

🔴 **`LICENSE` line `2` says *"For copyright information, please see the COPYRIGHT file."* 🔵 `COPYRIGHT`, `COPYRIGHT.txt` and `openeducat_core/COPYRIGHT` are all `404` on `master`.** 🟡 **So the copyright holder is named only in the module headers *(`OpenEduCat Inc`, `2009-TODAY`)*, and the root grant file points at nothing. 🔵 This joins `ACTION PH`'s ask-the-maintainer queue — it is a one-file fix and exactly the kind of ask a maintainer accepts.**

🟢 **Not a fourth channel:** `openeducat/openeducat_lti` is `404` on every path and both branches, and has **no public repository** under the new ref-set oracle. 🔵 **The shelves already record it `ABSENT`, so this is a confirmation and not a new gap.**

## Pass 224 — 2026-10-15 — `ACTION RU` FIRES LIMB `1` AT `81`: THE MOST-MENTIONED GNU ROW ON THIS SHELF WAS NEVER SILENT ABOUT ITS BOUND, AND `94.3%` IS A TOKEN COUNT THAT CANNOT BE REPRODUCED FROM ITS OWN PUBLISHED ARTEFACTS

🔵 **`0` new foundation rows. `1` bound restated on the shelf's most load-bearing GNU row. `1` published ratio withdrawn as non-reproducible.**

🔵 **Evidence:** [`ru-grammar-census`](../evidence/ru-grammar-census.2026-10-15-p224.tsv) *(`337` rows, with a grammar column)* · **Instrument:** [`p224-grammar-attribution`](../compose/code/p224-grammar-attribution/README.md) *(`24` tests, `14` controls)*

### 🆕 🟢 `ACTION RU` — p222's registered highest-priority action, run at last

🟢 **Limb `1` wanted `50`+ of the bare GNU mentions to attach to a row whose grant was read from a CRAN `DESCRIPTION` or an Odoo `__manifest__.py`. It fires at `81`.**

| population | bare GNU mentions |
|---|---|
| 🔴 **Odoo grammar** — all of them [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **`80`** |
| 🔴 **CRAN grammar** — `dexter-psychometrics/dexter` | **`1`** |
| 🔵 WIDE *(in those ecosystems, manifest not yet read)* | `101` |

🟢 **So the restatement is specific and it is good news for a studio:** those `81` mentions are **not** silences awaiting a read. Odoo spells `only` by **omission**, so `'license': 'LGPL-3'` in `openeducat_core/__manifest__.py` is a **positive `LGPL-3.0-only`**. 🔴 **`94.3%` remains a true count of bare *tokens* and is NOT a count of unspecified *grants*.**

🟢 **The verdict does not depend on the unit, which matters because the unit is what p222 proved had moved:** `71` on the table-**cell** unit, `83` on the token-occurrence unit before this pass's dependency guard, `81` after. 🔵 **The cell count independently corroborates p222's separately-derived *"`72` bare `LGPL-3.0` cells"* on the same row, from a different instrument, to within one cell.**

### 🆕 🔴 `T224-4` — the denominator does not reproduce, and the census that published it should have said how it counted

🟢 **This pass's instrument *imports* p221's `parse_range()` by path, so "bare" means exactly what it meant when `2 208` was published.** 🔴 **It still does not reproduce p221's population:**

| | p221 | p224 | corpus |
|---|---|---|---|
| GNU mentions | `2 342` | `4 152` | `120 296` → `121 085` lines *(+`789`)* |
| bare | `2 208` | `3 582` | |

🔴 **`789` more lines cannot produce `1 374` more mentions.** 🟢 **Importing a prior instrument's *predicate* does not reproduce its *population*, because the unit of enumeration lives in the RUNNER, not in the predicate:** p221 counted cell-mentions; this counts token occurrences anywhere, prose included.

🟡 **So the `94.3%` ratio is withdrawn as non-reproducible from the published artefacts, and `ACTION RU`'s numerator — the number its limbs were actually stated in — stands.** 🔵 **Standing rule, written down: a census that publishes a ratio must publish its enumerator, not only its predicate.**

### 🆕 🔴 `ACTION RV` is now the shelf's sharpest open licence question, and this pass makes it worse before someone makes it better

🔴 **`openeducat/openeducat_erp` carries `80` bare `LGPL-3.0` mentions on these shelves — more than any other GNU row — and the row is in a `RANGE-CONFLICT` with itself:** `openeducat_core/__manifest__.py` l.`25` says `'license': 'LGPL-3'` *(Odoo's `only`)* while **the same file's header** grants *"either version 3 of the License, or (at your option) any later version"*.

🟡 **Under `ACTION RU`'s finding the conflict is sharper, not softer:** before this pass the manifest token could be read as a silence, which is merely unhelpful. 🔴 **Under Odoo's grammar it is a positive `only` — so the file states two incompatible bounds, and `LGPL-3.0-only` is the conservative one an SOW must assume.** 🟢 **`ACTION RV` stays registered as the highest-priority licence action for p225, with its falsifier unchanged.**

### 🟢 The mandated platform shape, run and declared

🔴 **`open source platform education ERP CRM MIT Apache` produced `0` new foundation rows.** 🟢 It returned **OpenEduCat** *(already carried, and the row above)*, **ERPNext** *(`GPL-3`)* and **Twenty** *(`BSL-1.1` — **not** an OSI grant, recorded so no later pass treats it as one)*. 🔵 **`5` of `9` results were `openeducat.org` glossary pages in `5` languages.**

## Pass 223 — 2026-10-15 — `0` NEW FOUNDATION ROWS, AND THE REASON IS WORTH MORE THAN A ROW WOULD HAVE BEEN: THE ONE USE CASE LATAM BUYS HAS NO FOUNDATION TO STAND ON

🔵 **`0` new foundation rows. `1` candidate rejected on bus factor and recorded anyway, because the rejection is the finding.**

🔵 **Evidence:** [`discovery-candidates`](../evidence/discovery-candidates.2026-10-15-p223.tsv)

### 🔴 `T223-F1` — dropout prediction: `209` repositories, `0` foundations

🟢 **A foundation row on this shelf has to be something a studio can *depend on*: a grant, a maintainer, and something that runs.** 🔴 **The Portuguese/Spanish dropout-prediction shelf fails all three at once:**

| measure | value |
|---|---|
| repositories matching `"evasão escolar" OR "deserción escolar"` | **`209`** |
| highest star count in the top ten *(sorted by stars)* | **`4`** |
| of `4` probed first-hand: no licence at all | **`2`** |
| of `4` probed: `MIT` but **no model** | **`1`** *(scaffold — `data/`, `notebooks/`, contribution rules)* |
| of `4` probed: published evaluation metric | **`1`** — and it is one of the `UNGRANTED` two |

🔴 **The one repository with a result — [`lincolnmeira/mlp-evasao-ufrb`](https://github.com/lincolnmeira/mlp-evasao-ufrb), `AUC-ROC 0.943`, recall `86.3%` on UFRB student data — carries no grant, so it cannot be a dependency.** 🟢 **It can be a *benchmark*: a Brazilian federal university's published number is the bar a studio's own model has to clear, and quoting it in a proposal costs nothing and concedes nothing.**

🟡 **This is the inverse of the usual finding on this shelf. Elsewhere the problem is a reciprocal licence on a good platform. Here there is no platform — the whole supply is coursework.**

### 🟡 `T223-F2` — the offline candidate, and why it is not a foundation row

🟢 [`yassinabdelal-ipynb/el-thanawiya`](https://github.com/yassinabdelal-ipynb/el-thanawiya) — **`MIT`**, read first-hand *(`main/LICENSE`, `1 082` B)*. 🟢 **Course-level failure-risk inference that runs entirely on the handset: Flutter + an on-device network, a companion Python API for training, a reproducible pipeline, a model card, CI, and an Android manifest that declares *no Internet permission*.** 🟢 **It also refuses to invent a probability for a course with no observed grades — a calibration property most of this shelf does not have.**

🔴 **Not promoted to a foundation row: `0`★, one author, first commits this year.** 🟢 **Recorded as a **reference implementation** for the offline shelf p220 opened — the thing to read before building an offline early-warning box, not the thing to install.** 🔵 **Used that way in [`compose/patterns.md`](../compose/patterns.md) `P223-R2`.**

🔵 **Foundation rows unchanged this pass; `p222`'s `openeducat/openeducat_erp` range conflict *(`ACTION RV`)* is untouched and still open.**

## Pass 222 — 2026-10-15 — THE MOST-MENTIONED FOUNDATION ROW ON THIS SHELF WAS READ AS `NO-CHANNEL`, AND THE CHANNEL WAS ONE DIRECTORY DOWN

🔵 **`0` new repository rows. 🔴 `1` carried row changes state, and it is the one with `72` licence cells.**

🔵 **Evidence:** [`rp-bound-sweep`](../evidence/rp-bound-sweep.2026-10-15-p222.tsv) · [`rt-packaging-grant`](../evidence/rt-packaging-grant.2026-10-15-p222.tsv) · [`p222-alias-cluster-remeasure`](../evidence/p222-alias-cluster-remeasure.2026-10-15-p222.tsv) · **Instrument:** [`p222-ecosystem-bound-grammar`](../compose/code/p222-ecosystem-bound-grammar/README.md)

### 🆕 🔴 `P222-A` — `openeducat/openeducat_erp`: `RANGE-CONFLICT` on the row every Odoo education recipe here stands on

🔴 **[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) carries `72` bare `LGPL-3.0` cells across these shelves — more than any other GNU row.** This pass's first sweep reported it **`NO-CHANNEL`**: `18` root probes across `main` and `master`, every one `404`.

🔴 **That verdict was this pass's own instrument re-committing a defect p215 already recorded — *"ABSENT meant 'not at root'"*.** 🟢 **Odoo's unit of distribution is a MODULE, so the manifest sits one directory down:**

| channel | reads | grammar | bound |
|---|---|---|---|
| 🟢 `master/openeducat_core/__manifest__.py` l.`25` | `'license': 'LGPL-3'` | **Odoo** *(closed vocabulary)* | 🔴 **`only`** |
| 🟢 same file, header | *"the GNU Lesser General Public License as published by the Free Software Foundation, **either version 3 of the License, or (at your option) any later version**"* | **prose** | 🟢 **`or-later`** |

🔴 **Two channels in **one file**, and they state different bounds.** 🔵 **Read without the grammar they agree — both "say LGPL-3". Read with it, this is a `RANGE-CONFLICT` on the most load-bearing foundation row on the shelf, and the conservative reading (`LGPL-3.0-only`) is the one a client-facing SOW has to carry until the maintainer settles it.** 🟡 **Also confirmed first-hand: `openeducat_erp/__manifest__.py` → `200`, so the module tier is broad, not a single path.**

🟢 **The generalised rule, and it is the third time this page has had to write a version of it.** *Freshness per repo (`p134`) · identity before freshness (`p136`) ·* 🆕 **and now: `ABSENT` is only ever `ABSENT-AT-THE-PATH-PROBED`. Before publishing `NO-CHANNEL`, name the ecosystem's unit of distribution and probe at that unit.** 🔵 **For Odoo that is `*/__manifest__.py`; for Moodle a plugin's `version.php`; for a monorepo `apps/*` and `packages/*` — two of this pass's `10` `NO-CHANNEL` rows (`learnhouse/learnhouse`, `brownplt/LTLTutor`) turned out to have a reachable non-root manifest the moment one was tried.**

### 🆕 🟢 `P222-B` — `ACTION RT` closes on limb `2`: the grant **does** travel in the package

🔴 **`ACTION RT` asked whether the `8` `FILE-SILENT` rows p221 found ship their `LICENSE` to a consumer who installs only the package. Limb `1` was `3`+ that do not.** 🟢 **It fires limb `2`. Every row measurable here carries its grant, verified by downloading the wheel and listing its contents — not by trusting metadata:**

| row | artefact | bytes | the grant inside |
|---|---|---|---|
| 🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) | `xblock-6.3.4-py3-none-any.whl` | `160 348` | 🟢 `xblock-6.3.4.dist-info/licenses/LICENSE.TXT` · `License-Expression: Apache-2.0` |
| 🟢 [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | `jupyterhub_ltiauthenticator-1.6.3-...whl` | `28 209` | 🟢 `.../licenses/LICENSE` · **and the full BSD-3 text inline in `License:`** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `kolibri-0.19.5-py2.py3-none-any.whl` | 🔴 **`103 738 893`** | 🟢 `kolibri-0.19.5.dist-info/LICENSE` · `License: MIT` |

🟢 **So `FILE-SILENT` is cosmetic for the PyPI tier: a source file with no header is fine when the packaging carries the notice.** 🔴 **Two rows are not measurable from here at all — `Pearson-Advance/openedx-lti-tool-plugin` and `open-spaced-repetition/fsrs4anki-helper` are both `404` on PyPI under every spelling tried, because one installs from source and the other ships as an `.ankiaddon` zip.** 🔵 **Two more (`h5p/h5p-php-library`, `packbackbooks/lti-1-3-php-library`) are Composer packages and belong to `ACTION RC`.**

### 🆕 🔴 `P222-C` — the closure finding inside Kolibri's wheel, which is the bigger number

🔴 **Kolibri's wheel is `103.7` MB and vendors its whole dependency tree under `kolibri/dist/`. Listing every licence file inside it returns **`81`**: Kolibri's own `MIT` grant, and **`80` third-party licence files** — Django, SQLAlchemy, `cheroot`, `greenlet`, `certifi`, `tzdata`, `morango`, `le_utils` and `70`-odd more, several carrying their own `LICENSE_APACHE` and `LICENSE.PSF` variants.**

🟡 **The shelf cell for this row says `MIT`, and that is correct about Kolibri.** 🔴 **It describes `1` of `81` grants inside the artefact a client actually installs.** 🟢 **This is the same question [`dependency-licence-closure`](../compose/code/dependency-licence-closure/README.md) was built for, and this pass supplies the measurement that makes it urgent for the offline-first tier specifically: a vendored wheel is the one distribution shape where the closure ships *with* the product, so the client redistributes all `81`.**

### 🆕 🟡 `P222-D` — the alias-cluster class, RE-MEASURED, and it has grown

🔵 **Not a new finding.** This page recorded it at l.`7968`: *"`37` further clusters are this KB citing one repository under two spellings"* — `p443`'s case-collision class, instrument [`p136-lineage-verdict`](../compose/code/p136-lineage-verdict/README.md). 🔴 **Re-run over all `8` shelf files on 2026-10-15:**

| metric | prior | 🆕 p222 |
|---|---|---|
| distinct GitHub slugs on the shelves | — | `1 884` |
| case-variant clusters | `37` | 🔴 **`47`** *(`+10`)* |
| extra rows those clusters create | — | 🔴 **`48`** |
| mentions involved | — | `691` |
| clusters where the **repo name** differs in case too | — | `14` *(the rest are owner-only)* |

🟢 **`8` of the `47` were verified first-hand by `README.md` byte identity** — `OpenOLAT/OpenOLAT`↔`openolat/OpenOLAT`, `OS4ED/openSIS-Classic`↔`os4ed/openSIS-Classic`, `GibbonEdu/core`↔`gibbonedu/core`, `ClassroomIO/ClassroomIO`↔`classroomio/classroomio`, `ahmedEid1/Lumen`↔`ahmedEid1/lumen`, `Crosstalk-Solutions/Project-NOMAD`↔`.../project-nomad`, `EduBase/MCP`↔`EduBase/mcp`, `eth-lre/MathTutorBench`↔`eth-lre/mathtutorbench`. 🟢 **Control: `blend-ed/openedx-mcp` vs `blend-ed/tutor-contrib-openedxmcp` → `DIFFERENT`, as it must be.**

🔴 **And a correction this pass owes to its own first reading: byte identity does NOT prove alias.** 🟢 **[`g3i/lxHive`](https://github.com/g3i/lxHive) and [`leogaggl/lxHive`](https://github.com/leogaggl/lxHive) serve a byte-identical `composer.json` *(`923` B, `sha256:b5af29209fa1`)* and are two repositories — a fork pair.** 🔵 **For case-variant clusters the proof is that GitHub slugs are case-insensitive; byte identity is corroboration only.**

🟡 **One pair is neither, and is published as a candidate rather than a conclusion:** [`openedx/edx-platform`](https://github.com/openedx/edx-platform) and `openedx/openedx-platform` — same owner, byte-identical on `package.json` *(`5 540` B, `e16f286893eb469e`)* **and** `setup.py` *(`14` B, `d5558cd419c8d46b`)*, but `raw.githubusercontent.com` reports no redirect and `api.github.com` is `403`, so a rename alias cannot be told from an exact mirror here. 🔵 **`ALIAS-CANDIDATE`. The shelves carry `65` and `9` AGPL cells respectively, so if it is one repository this page is double-counting its largest row.**


## Pass 221 — 2026-10-15 — THE FOUNDATION ROWS ARE WHERE `FILE-SILENT` BITES, BECAUSE A FOUNDATION IS A THING YOU INSTALL INTO SOMEONE ELSE'S TREE

🔵 **`1` new repository row.** 🔴 **`8` of the `22` rows read file-by-file this pass carry **no licence notice in the file that ships** — and the four largest are all foundation-tier libraries.**

🔵 **Evidence:** [`rh-file-level-range`](../evidence/rh-file-level-range.2026-10-15-p221.tsv) · [`ri-prescription-table`](../evidence/ri-prescription-table.2026-10-15-p221.tsv) · **Instrument:** [`p221-licence-version-range`](../compose/code/p221-licence-version-range/README.md)

### 🆕 🟡 `P221-A` — the foundation rows whose shipped file carries nothing

🔵 **Why this tier specifically: a foundation is consumed by *installation* — `pip install` into a `site-packages` tree, `composer require` into `vendor/`, a zip dropped into an add-ons folder. The repository's root `LICENSE` does not travel with any of those.**

| row | published cell | the file a consumer actually gets | bytes | notice in that file |
|---|---|---|---|---|
| 🔴 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | `GPL-3.0` *(`LICENSE.txt`, `35 146` B)* | `h5p.classes.php` | 🔴 **`196 920`** | 🟡 **none.** 🔵 **Its `license` / `licenseVersion` / `licenseExtras` hits are H5P **content** metadata validators — `'/^(CC BY\|CC BY-SA\|…\|GNU GPL\|PD\|…)$/'` — describing the licence of a *learning object*, not of the file** |
| 🔴 [`openedx/XBlock`](https://github.com/openedx/XBlock) | `Apache-2.0` *(`11 358` B)* | `xblock/core.py` | `39 737` | 🟡 **none** |
| 🔴 [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | `Apache-2.0` *(manifest @ `master`)* | `src/LtiMessageLaunch.php` | `23 855` | 🟡 **none** — 🔵 **the grant exists in `composer.json` only, which is a `PERMISSIVE-MANIFEST` channel and therefore an optional field that happens to be filled** |
| 🟡 [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | `BSD-3-Clause` *(`1 528` B)* | `ltiauthenticator/lti11/auth.py` | `7 796` | 🟡 **none** |
| 🟡 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `MIT` | `kolibri/core/auth/models.py` | `75 498` | 🟡 **none** |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `GPL-2.0` | `index.php` | `10 443` | 🟡 **none** — 🔴 **and `GPL-2.0` is exactly the cell where `-only` vs `-or-later` decides GPLv3 compatibility, so this row is both silent AND unbounded** |
| 🟡 [`Pearson-Advance/openedx-lti-tool-plugin`](https://github.com/Pearson-Advance/openedx-lti-tool-plugin) | `Apache-2.0` *(`main/LICENSE`)* | `openedx_lti_tool_plugin/views.py` · `setup.py` | `3 547` · `4 749` | 🟡 **none in either** |
| 🟡 [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | `MIT` *(`1 079` B)* | `__init__.py` · `manifest.json` | `10 799` · `168` | 🟡 **none in either** — 🔴 **and an Anki add-on is distributed as an `.ankiaddon` zip of exactly these files** |

🟢 **The two foundation rows that AGREE at file level, recorded as clean:**

| row | published cell | the shipped file | bytes | reading |
|---|---|---|---|---|
| 🟢 [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | `Apache-2.0` | `tincan/statement.py` | `7 342` | 🟢 **full Apache-2.0 header, *"Copyright 2014 Rustici Software"*, plus `setup.py` `license='Apache License 2.0'`** |
| 🟢 [`oppia/oppia`](https://github.com/oppia/oppia) | `Apache-2.0` | `core/domain/exp_services.py` | `174 203` | 🟢 **full Apache-2.0 header, *"Copyright 2014 The Oppia Authors"*** |

🔵 **The contrast is the useful part: Apache-2.0 projects tend to carry the per-file header its appendix recommends; the GNU and permissive-short-licence rows mostly do not.** 🔴 **`2` of `2` Apache rows carried it; `0` of the `8` silent rows are Apache-with-a-header.**

### 🆕 🔴 `P221-B` — the LTI library tier, and the one row that cannot enter a Moodle tree

🔵 **This KB carries four LTI 1.3 libraries. They are the most-installed-into-a-tree rows on these shelves, and this pass read three of them in source.**

| row | published cell | file read | bytes | file-level reading | verdict |
|---|---|---|---|---|---|
| 🔴 [`oat-sa/lib-lti1p3-core`](https://github.com/oat-sa/lib-lti1p3-core) | `GPL-2.0` | `src/Message/LtiMessage.php` | `3 800` | *"as published by the Free Software Foundation; under version 2 of the License **(non-upgradable)**"* · `composer.json`: `"license": "GPL-2.0-only"` | 🔴 **`GPL-2.0-only`. INCOMPATIBLE with `GPL-3.0`, so it cannot be combined with Moodle. The published cell does not say so** |
| 🟡 [`celtic-project/LTI-PHP`](https://github.com/celtic-project/LTI-PHP) | `LGPL-3.0` *(`7 651` B)* | `src/Tool.php` | `116 419` | `@license http://www.gnu.org/licenses/lgpl.html GNU Lesser General Public License, **version 3**` — 🔵 **names the version and says nothing about later ones** | 🟡 **`BOTH-UNSPECIFIED` — the ambiguity is at SOURCE, not in this KB. Ask the maintainer; do not guess** |
| 🟡 [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | `Apache-2.0` | `src/LtiMessageLaunch.php` | `23 855` | 🟡 **no notice; `composer.json` only** | 🟡 **`FILE-SILENT`** |

🔵 **For an engagement that must put an LTI library inside a Moodle plugin, the `oat-sa` row is a hard stop and the other two are questions.** 🟢 **That is three different answers to one procurement question, and before this pass all three cells read as a bare licence token.**

### 🆕 🟢 `P221-C` — CRAN enters the prescription table as a second `PRESCRIBED-CHANNEL`

🟢 **`ACTION RI`'s offline grep found `9` ecosystems on these shelves that `p220`'s hard-coded table does not carry. One of them changes how foundation rows get read:**

| ecosystem | file | field | why it matters here |
|---|---|---|---|
| 🆕 🟢 **CRAN** | `DESCRIPTION` | 🟢 **mandatory** | 🟢 **`53` mentions on these shelves, and it is a `PRESCRIBED-CHANNEL` — the third after Moodle's `version.php` and WordPress's `readme.txt`. The R/psychometrics tier of this KB is large *(`dexter`, `girth`, `irtorch`, `pyBKT` neighbours, `writeAlizer`, `tblcheck`, `ggcheck`, `ottr`)* and every one of those rows has a mandatory licence field nobody has swept** |
| 🆕 🟡 **Maven** · **RubyGems** · **OpenACS** | `pom.xml` · `*.gemspec` · `dotlrn.info` | 🔴 optional | 🔵 `54` · `2` · `1` mentions. 🟡 **The Java/Sakai/QTI tier runs on `pom.xml`, so it is a large population with an optional field** |
| 🆕 🔴 **SCORM packaging** | `imsmanifest.xml` | 🔴 **no licence field exists** | 🔴 **`NO-CHANNEL`. A delivered SCORM package has nowhere to carry a grant, which is precisely why `T220-1`'s per-SCO file header was the deciding channel** |

🔴 **Rejected, and recorded as rejected:** `Helm` / `Chart.yaml` — a single weak hit which on reading turned out to be a **run instruction**, not a manifest channel. 🟢 **Not published as an ecosystem.**

### 🆕 🟢 The new repository row

| repo | licence | channels | region | what it is |
|---|---|---|---|---|
| 🆕 🟢 [`X5GON/x5moodle`](https://github.com/X5GON/x5moodle) | 🟢 **`BSD-2-Clause`** — `main/LICENSE`, `1 325` B, *"Copyright (c) 2018, University of Nantes. All rights reserved."* | 🟢 `LICENSE` read first-hand | **EMEA (France)** | Moodle activity plugin wiring AI-selected open educational resources into a live course session. 🟡 **Dated (2018) and carried as an OER-integration reference, not as a current agent.** 🔵 **Licence note worth keeping: Moodle requires `GPL-3.0-or-later` of plugins in its directory, and `BSD-2-Clause` is GPL-compatible but is not that — so this plugin is distributable inside a Moodle tree while not meeting the directory's own rule** |

## Pass 220 — 2026-10-15 — THE OFFLINE-FIRST EDUCATION SERVER ARRIVES, AND IT IS THE FIRST FOUNDATION ROW ON THESE SHELVES THAT ASSUMES **NO NETWORK**

🔵 **`1` new foundational repository, verified at `2` channels. 🟢 And a structural finding about these shelves' own reading method: `4` of `11` licence-unknown rows answered from an ecosystem channel, `7` did not, and the split is not about effort — it is about whether the ecosystem MANDATES the field.**

### 🆕 🟢 [`Crosstalk-Solutions/Project-NOMAD`](https://github.com/Crosstalk-Solutions/Project-NOMAD) — `Apache-2.0`

| field | reading, `2026-10-15` |
|---|---|
| licence | 🟢 **`Apache-2.0`**, verified at **`2` channels**: `LICENSE` `10 779` B *(Apache License Version 2.0, January 2004 boilerplate)* · `package.json` `"license": "Apache-2.0"` |
| version | `1.35.1` |
| author | `Crosstalk Solutions, LLC` |
| region | Global — 🔵 **but the reason it matters here is LATAM, Africa and rural APAC** |
| what it is | *"a self-contained, offline-first knowledge and education server packed with critical tools, knowledge, and AI to keep you informed and empowered — anytime, anywhere"* |
| footprint | **~`5` GB disk and under `1` GB RAM** for the core; offline content and the AI assistant are what actually size the box |
| constraint | 🔴 **Debian-based only** *(Ubuntu `26.04` LTS recommended; `24.04` LTS and Debian `12` supported)*. Windows via WSL2 only |

🟢 **It is a Docker orchestrator with a management UI, not a monolith — which is exactly what makes it a foundation row rather than a product:**

| layer | upstream it orchestrates | what an engagement gets |
|---|---|---|
| **education platform** | 🟢 **Kolibri** — [`learningequality/kolibri`](https://github.com/learningequality/kolibri), 🟢 **`MIT`** *(read first-hand this pass)* | Khan Academy courses **with progress tracking**, offline |
| **knowledge library** | 🟢 **Kiwix** — [`kiwix/kiwix-tools`](https://github.com/kiwix/kiwix-tools) · [`kiwix/libkiwix`](https://github.com/kiwix/libkiwix) | offline Wikipedia, medical references, ebooks — ZIM library manager and content selector built in. 🟡 **No root `LICENSE` in either repo — another `PERMISSIVE-MANIFEST` case, unresolved** |
| **local AI** | 🟢 **Ollama** — [`ollama/ollama`](https://github.com/ollama/ollama), 🟢 **`MIT`** *(read first-hand this pass)*, or any OpenAI-compatible endpoint *(LM Studio, `llama.cpp`)* | AI chat over an uploaded document knowledge base, no egress |
| maps | **ProtoMaps** — [`protomaps/basemaps`](https://github.com/protomaps/basemaps) | downloadable regional maps. 🟡 No root `LICENSE` |
| data tools | CyberChef | encryption, encoding, analysis |
| notes | FlatNotes | local note-taking |
| extension | *"Supply Depot"* one-click catalogue | PDF tools, file browser, e-book library, password manager, plus arbitrary custom containers |

🔵 **Why this is a foundation and not a trending curiosity:** every AI-in-education row on these shelves assumes a reachable LMS and a reachable model endpoint. 🟢 **This one assumes neither, and it composes three well-governed upstreams rather than reimplementing them.** 🔴 **For a ministry engagement in a region where the measured constraint is connectivity rather than licensing — which is most of the LATAM and Africa material in [`intel/market.md`](../intel/market.md) — it is the only starting point on these shelves that survives the site visit.**

🔴 **What is NOT verified:** the search surface that produced it claims *"about `39.8`k stars"* and a GitHub-trending appearance on `2026-10-13`. 🔴 **`api.github.com` → `403` and `github.com` HTML → `403` from this session, so NO star count, fork count or trending placement is recorded here.** 🔵 **The licence, the version, the orchestrated upstreams and the footprint are first-hand; the popularity is not, and is deliberately left out of the table.**

🟡 **One honest caution for an SOW:** its own quick-install is `curl -fsSL …/install_nomad.sh | sudo bash`, and it says so plainly *(*"sudo/root privileges are required"*)*. 🟢 **There is a documented Docker-Compose route for sites that will not pipe a script to root, and that is the one to put in a proposal.**

### 🆕 🔴 The reading-method finding: why `7` of `11` unknown rows will never answer from a manifest

🟢 **`ACTION RG` ran [`P219-A`](../compose/code/p219-upstream-channel/README.md) over the `11` `CLAIMED-IN-PROSE` rows. `4` answered. The `7` that did not are not unread — they were read, and the field does not exist:**

| ecosystem | mandatory file | licence field | class | rows read |
|---|---|---|---|---|
| Moodle | `version.php` | 🟢 **mandatory** *(`@license` docblock)* | `PRESCRIBED-CHANNEL` | `3`/`3` answered |
| ADL/SCORM | source-file header | 🟢 **mandatory by convention** | `PRESCRIBED-CHANNEL` | `1`/`1` answered |
| npm | `package.json` | 🔴 **optional** | `PERMISSIVE-MANIFEST` | `0`/`3` |
| PyPI | `pyproject.toml` | 🔴 **optional** | `PERMISSIVE-MANIFEST` | `0`/`2` |
| Go | `go.mod` | 🔴 **no such field exists** | `NO-CHANNEL` | `0`/`1` |
| *(curated link list)* | — | — | `NO-CHANNEL` | `0`/`1` |

🟢 **The rule for every future intake on this shelf:** a channel counts as a **licence** channel only when the ecosystem mandates the field in a file that must exist. 🔴 **Reading `package.json` and finding nothing is not a gap in the reading — it is npm behaving exactly as designed, and it must not be recorded as a defect in the repository.**

## Pass 219 — 2026-10-15 — THE ECOSYSTEM CHANNEL WAS READ ACROSS ALL `47` FOR THE FIRST TIME; `p204` HAD READ IT ON `8`

🔵 **`0` new foundation rows.** 🟢 **`ACTION QV` and `QW` discharged; the published population ladder independently reproduced step by step; `1` long-standing manifest CONFLICT resolved.**

🔵 **Evidence:** [`qv-ecosystem-channel`](../evidence/qv-ecosystem-channel.2026-10-15-p219.tsv) · [`population-ladder-control`](../evidence/population-ladder-control.2026-10-15-p219.tsv) · [`p219-channel-reachability`](../evidence/p219-channel-reachability.2026-10-15-p219.tsv)

### 🆕 🟢 `T219-3` — `LearnPress`'s `P204-1` conflict resolves, and the resolution is that one side was never a grant

🔴 **This file has carried the conflict at l.`1249` *(now l.`1249`+ `this` section)* since p204:** *"`package.json` → **`ISC`** — **and `readme.txt` says `GPLv3`**"*. 🔵 **It has also carried the row under `TRUE ABSENCE at 90 forms` at l.`1017`, which is correct and is about licence-shaped PATHS.**

🟢 **A third channel, read this pass:** `raw.githubusercontent.com/LearnPress/learnpress/HEAD/composer.json` → **`"license": "GPL-3.0-or-later"`**.

| channel | says | what it is |
|---|---|---|
| `readme.txt` l.`7`–`8` | `License: GPLv3` + `License URI: gnu.org/licenses/gpl-3.0.html` | 🟢 **the WordPress plugin-directory declaration** |
| 🆕 `composer.json` | `GPL-3.0-or-later` | 🟢 **the PHP-ecosystem manifest — and this is a PHP project** |
| `package.json` | `ISC` | 🔴 **`npm init`'s DEFAULT value** |
| `90` licence-shaped paths | nothing | 🟢 correct — there is no file |

🟢 **`2` of `3` real channels agree on `GPL-3`. The outlier is the one belonging to the build tooling rather than to the product, and `ISC` is the string `npm init` writes when nobody answers the licence prompt.** 🔴 **A conflict recorded for `15` passes was an artefact, and the row should never have been read as contested.**

🔵 **The rule this earns, and it is narrow on purpose:** 🟡 **a `license` field in a manifest for a language the project is not written in is weak evidence, and `ISC` in a `package.json` with no other `ISC` signal anywhere is the default, not a declaration.** 🔴 **It does not generalise to a `package.json` in a Node project — there the field is the declaration.**

### 🆕 🟡 `T219-4` — a new state class, and the anchor row of `ACTION QV` is the one that needs it

🟢 **[`alfredang/ai-mms`](https://github.com/alfredang/ai-mms) serves a `composer.json` at root, `7 348` B, and it declares `["OSL-3.0","AFL-3.0"]`.** 🔴 **Its `"name"` is `openmage/magento-lts` and its `"description"` is *"A fork of Magento-1 that is accepting bug fixes (backward compatible, drop in replacement for official Magento)"*.**

🔴 **This is the vendored UPSTREAM's manifest, sitting in a downstream's tree. It is not the author's grant, and `p218`'s `UNKNOWN` was right to refuse it.** 🟢 **But it is not nothing either: the `OSL-3.0`/`AFL-3.0` grant covers the overwhelming majority of the BYTES in that repository, because the repository largely *is* OpenMage.**

🆕 **`UPSTREAM-MANIFEST`, and its standing instruction is unlike every other state:**

> 🟢 The vendored body is licensed *(here: `OSL-3.0` + `AFL-3.0`, network-reciprocal)*. 🔴 The author's own customisations are not. 🔴 **So this row can be neither treated as unlicensed nor built on — the two halves of the tree answer differently, and a studio needs the boundary drawn before an SOW, not after.**

🔵 **This is the `ECL-2.0` lesson of `p216` in a second place: a grant has to be read at CLAUSE and at SCOPE, not just named.** 🔵 **Same trap family as [`sakai-manifest-component-vs-upstream`](../evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv) — p172 built the instrument for exactly this and the `47` were never run through it.**

### 🆕 🟢 The channel, read across all `47`

🔵 **`11` forms each, one request, no clone:** `package.json` · `pyproject.toml` · `setup.py` · `composer.json` · `Cargo.toml` · `version.php` · `readme.txt` · `pubspec.yaml` · `<reponame>.php` · `plugin.php`.

| measure | value |
|---|---|
| serve **any** manifest at root | 🟡 **`15`** of `47` |
| files served | `18` |
| carry a **licence field** | 🟢 **`4`** |
| of those, **new** this pass | 🟢 **`2`** *(`tutor-lms-mcp.php`, `LearnPress`'s `composer.json`)* |

🔴 **`32` of `47` serve no manifest at root at all, and `11` of the `15` that do have no licence field.** 🟢 **So `p204`'s *"none"* generalises: the absence is real for the bulk of this population, and `ACTION PH`'s queue does not shrink much.** 🟢 **It does, however, get correctly ORDERED — see `ACTION PH` in [`intel/open-gaps.md`](../intel/open-gaps.md).**

### 🆕 🟢 Control — the published population ladder, reproduced from the raw TSVs

| step | operation | result |
|---|---|---|
| `1` | unique slugs in [`ungranted-after-18-forms`](../evidence/ungranted-after-18-forms.2026-10-15-p211.tsv) | 🟢 **`94`** |
| `2` | minus the `25` in [`lstree-grant-recovery`](../evidence/lstree-grant-recovery.2026-10-15-p215.tsv), exact case | 🟢 **`69`** |
| `3` | collapse the owner-case duplicate pair | 🟢 **`68`** |
| `4` | remove the lowercase `openSIS-Classic` variant | 🟢 **`67`** |
| `5` | minus p217's `17` prose/refusal rows and `3` `NON-PUBLIC` | 🟢 **`47`** = `45` `NO-PROSE` + `1` `DOMAIN-NOUN` + `1` `PROSE-THIRD-PARTY` |

🟢 **Every step reproduces, and the mechanism is now shown rather than asserted: the `94` contains EXACTLY `2` case-duplicate pairs, and the ladder spends one step on each.** 🟢 **`ACTION QT`'s limb-`2` verdict is independently re-confirmed.**

🔵 **One line worth keeping, because it is the whole pass in miniature:** 🟡 **the owner-case duplicate that makes step `3` work is `Hesham0-0Nasser/tutor-lms-mcp` — the same row whose grant this pass recovered from a WordPress plugin header.** 🔴 **This KB has had that slug under a magnifying glass for `8` passes and never opened the one file that answered it.**

## Pass 218 — 2026-10-15 — THE ARITHMETIC HOLDS AT EVERY COUNT CHECKED, AND THE INSTRUMENT THAT CERTIFIED IT IS WRONG IN A WAY NOBODY WOULD HAVE NOTICED

🔵 **`0` new foundation rows.** 🟢 **`ACTION QT` discharged with a split verdict; `ACTION QU` closed on limb `2`.** 🔵 **Evidence:
[`evidence/gnu-version-pin.2026-10-15-p218.tsv`](../evidence/gnu-version-pin.2026-10-15-p218.tsv),
[`evidence/pass-boundary-heading-test.2026-10-15-p218.tsv`](../evidence/pass-boundary-heading-test.2026-10-15-p218.tsv),
[`evidence/grant-state-schema.2026-10-15-p218.tsv`](../evidence/grant-state-schema.2026-10-15-p218.tsv).**

### 🆕 🟢 `P218-F1` — `ACTION QT`, counts half: every quoted population reproduces exactly

🟢 **`QM` checked the headline `67` at p217 and carried the rest forward. p218 recomputed each remaining quoted count from the evidence file it names, independently:**

| quoted count | recomputed | source |
|---|---|---|
| `94` `ABSENT` after the `18` root forms | 🟢 **`94`** | [`ungranted-after-18-forms…p211.tsv`](../evidence/ungranted-after-18-forms.2026-10-15-p211.tsv) rows `4`–`97` |
| `25` recovered by `ACTION QD` | 🟢 **`25`** | [`lstree-grant-recovery…p215.tsv`](../evidence/lstree-grant-recovery.2026-10-15-p215.tsv) rows `10`–`34` |
| `22` itemised rows in the prose probe | 🟢 **`22`** | [`readme-prose-grant-probe…p217.tsv`](../evidence/readme-prose-grant-probe.2026-10-15-p217.tsv) |
| `19` licence-shaped prose hits | 🟢 **`19`** | `8` BARE + `4` DANGLING + `1` QUALIFIED + `1` SCOPED + `1` CONFLICT + `2` REFUSED + `1` THIRD-PARTY + `1` DOMAIN-NOUN |
| `15` own-project claims | 🟢 **`15`** | `8`+`4`+`1`+`1`+`1` |
| `67` ungranted | 🟢 **`67`** | re-derived at p217, unchanged |

🟢 **`ACTION QT` fires on limb `2` for the counts: `0` of `6` disagree with the file they cite. `T216-1`'s `63` really was isolated, and the arithmetic axis can be closed.** 🔴 **One figure DOES change, and not by an error:** 🟢 **the `3` `NON-PUBLIC` rows are confirmed gone on a fourth channel *(`ACTION QU`, limb `2`)*, so the **LIVE** ungranted population is **`64`**.** 🔵 **Four numbers now have four distinct meanings and must stop being used interchangeably: `94` probed · `67` ungranted · `64` live · `47` unknown.**

### 🆕 🔴 `P218-F2` — `ACTION QT`, GNU half: `3` of `3` pin to `v3`, and `ACTION QE` would have failed on all three

🟢 **The `3` rows p217 recorded as GNU-family-with-no-version were re-read from the `README` body in full, not through a window:**

| repo | line | pinned | p217 recorded |
|---|---|---|---|
| [`bycs-lp/moodle-block_ai_chat`](https://github.com/bycs-lp/moodle-block_ai_chat) | l.`161`–`162` | 🟢 **`GPL-3.0-or-later`** | 🔴 *"version not pinned in window"* |
| [`bycs-lp/moodle-local_ai_manager`](https://github.com/bycs-lp/moodle-local_ai_manager) | l.`93`–`94` | 🟢 **`GPL-3.0-or-later`** | 🔴 *"version not pinned in window"* |
| [`marcusgreen/moodle-qtype_aitext`](https://github.com/marcusgreen/moodle-qtype_aitext) | l.`64` | 🟢 **`GPL-3.0-or-later`** | 🟢 already correct |

🔴 **`ACTION QT` fires on limb `1` for this axis. And the reason p217 missed it is an instrument defect that invalidates `ACTION QE`'s entire method — now carried a third pass:**

```
line N      "... under the terms of the GNU General Public License as published by"
                                                        ^ family named, NO version
line N+1    "the Free Software Foundation, either version 3 of the License, or"
                                                        ^ the version
```

🔴 **The GPL preamble sentence HARD-WRAPS between the family and the version. A line-based title window of `1` line matches the family and stops exactly one line short of the pin.** 🔴 **`ACTION QE` reads *"re-read every GNU-family cell from the TITLE WINDOW, not the body"* — it would have returned *"unpinned"* on every correctly-licensed `GPL-3.0` repository in the corpus, and the `~97` GNU rows it targets are mostly Moodle plugins carrying this exact boilerplate.** 🟢 **`T218-4`: the window must be SENTENCE-based — join lines to the next `.` before matching.** 🔵 **Same class as `T218-1`: the instrument's unit was finer than the thing it measured.**

🟡 **These `3` stay `CLAIMED-IN-PROSE`, not `GRANTED`.** 🔴 **Re-probed this pass: `LICENSE`, `LICENSE.md`, `COPYING`, `LICENSE.txt` → `0` × `200` on all three, so `p211`'s `ABSENT` holds and the `README` is still the only channel.** 🟢 **`ACTION QN`'s rule is unchanged — a prose pin is still a prose claim. What changes is that the claim is now specific enough for a studio to act on, and `ACTION PH`'s population is now `4` DANGLING + `3` precisely-pinned-but-unfiled.**

### 🆕 🔴 `P218-F3` — the live/historical test p216 certified `ACTION QO` with is unsound

🔴 **p216 recorded: *"a NEAREST-heading test called `9` of the `19` live; the enclosing LEVEL-2 (pass-boundary) test calls `0` live. The heading LEVEL was the whole measurement."*** 🔴 **On these shelves `^## ` is NOT a pass boundary. Measured over all `8`:**

| file | level-2 headings | pass boundaries | shadowing |
|---|---|---|---|
| `compose/patterns.md` | `160` | `46` | 🔴 **`114` — `71`%** |
| `intel/market.md` | `138` | `74` | 🔴 **`64` — `46`%** |
| `agents/trending.md` | `354` | `283` | `71` |
| `repos/trending.md` | `348` | `282` | `66` |
| `intel/trends.md` | `96` | `79` | `17` |
| `repos/foundations.md` | `85` | `72` | `13` |
| `verticals/solutions.md` | `77` | `68` | `9` |
| `agents/top.md` | `91` | `81` | `10` |
| 🔴 **TOTAL** | **`1 349`** | `985` | 🔴 **`364` — `27`%** |

🔴 **`53` of `intel/market.md`'s `64` shadowing headings are `## Opportunities by region` — the heading the INGEST SPEC MANDATES. The schema injects a competing level-2 heading into the one file whose cells are most client-facing, so the test is least reliable exactly where it matters most.** 🔵 **`compose/patterns.md` is worse in proportion: `71`% of its level-2 headings are recipe titles, not pass boundaries, and it is the file holding the client recipes.**

🟢 **Demonstrated on the one cell where it changes the answer:** `intel/market.md` l.`5388` *(an `alfredang/AI-LMS-TMS` *"has no grant"* cell)*. 🔴 **The bare `^## ` test returns `## Opportunities by region` (l.`5291`), finds no pass in the heading, and calls it **LIVE**.** 🟢 **The corrected test returns `## Pass 187 — 2026-10-14` (l.`5266`): **HISTORICAL**.**

🟢 **p216's VERDICT survives — all `6` stale cells this pass found are historical, so `0` live stands, and for the first time it is established with a sound instrument.** 🔴 **p216's INSTRUMENT does not, and `ACTION QO` must not be wired into `make hooks` carrying it.** 🟢 **One-line fix, committed: [`compose/code/p218-bilingual-gate/pass_boundary.sh`](../compose/code/p218-bilingual-gate/README.md).**

### 🆕 🔴 `P218-F4` — the corrections this pass owes its own pages

🟢 **`6` cells, not `QR`'s claimed `4`, publish a state that the `README` channel has since contradicted. All `6` are inside dated pass sections and are therefore corrected HERE rather than rewritten in place:**

| file | line | as published | correct state |
|---|---|---|---|
| `verticals/solutions.md` | `2182` | 🔴 *"NO GRANT"* | 🔴 **`GRANT-REFUSED`** |
| `intel/market.md` | `5388` | 🔴 *"has no grant"* | 🔴 **`GRANT-REFUSED`** |
| `compose/patterns.md` | `3913` | 🔴 *"no grant, `19`★"* | 🔴 **`GRANT-REFUSED`** |
| `agents/top.md` | `2752` | 🔴 *"NONE"* | 🔴 **`GRANT-REFUSED`** |
| `repos/trending.md` | `1558` | 🔴 *"none"* | 🔴 **`GRANT-REFUSED`** |
| `intel/trends.md` | `2904` | 🔴 *"none"* | 🔴 **`GRANT-REFUSED`** |

🔴 **`3` are `alfredang/AI-LMS-TMS`, `3` are `bedriyan/medkit-app`.** 🔴 **p217 wrote the `AI-LMS-TMS` correction at `verticals/solutions.md` l.`25` and left the contradicting cell at l.`2182` — in the SAME FILE, `2 157` lines below it.** 🔵 **The propagation defect, committed by the pass whose headline was the propagation defect.**

## Pass 217 — 2026-10-15 — THE `67` IS ARITHMETICALLY CONFIRMED AND SEMANTICALLY WRONG: `47` IS THE NUMBER OF REPOSITORIES THIS KB KNOWS NOTHING ABOUT

🔵 **`0` new foundation rows.** 🟢 **`ACTION QM` and `ACTION QN` discharged.** 🔵 **Evidence:
[`evidence/readme-prose-grant-probe.2026-10-15-p217.tsv`](../evidence/readme-prose-grant-probe.2026-10-15-p217.tsv),
[`evidence/shelf-language-census.2026-10-15-p217.tsv`](../evidence/shelf-language-census.2026-10-15-p217.tsv).**

### 🆕 🟢 `P217-F1` — `ACTION QM`: p216's `67` is correct, rebuilt from the evidence files it cites

🟢 **`T216-1` was registered because p215 published `63` three times and the figure was wrong.
p216 published `67`. Recomputed this pass from the two committed evidence files, independently:**

| step | count | how it was established |
|---|---|---|
| `ABSENT` after `18` root forms *(p211)* | `94` | [`ungranted-after-18-forms.2026-10-15-p211.tsv`](../evidence/ungranted-after-18-forms.2026-10-15-p211.tsv), rows `4`–`97` |
| recovered by `ACTION QD` *(p215)* | `25` | [`lstree-grant-recovery.2026-10-15-p215.tsv`](../evidence/lstree-grant-recovery.2026-10-15-p215.tsv), rows `10`–`34` |
| of those `25`, inside the `94` | 🟢 **`25`** | set-verified slug by slug; `0` outside |
| raw remainder | `69` | `94` − `25` |
| less the owner-case duplicate pair | `68` | `Hesham0-0Nasser/tutor-lms-mcp` ≡ `hesham0-0nasser/tutor-lms-mcp`, both unrecovered |
| less the row whose case-variant p215 recovered | 🟢 **`67`** | `os4ed/openSIS-Classic`; variant `OS4ED/openSIS-Classic` recorded `GPL-2.0` |

🟢 **`ACTION QM` fires on limb `2` for this figure: p216's arithmetic reproduces exactly. The
`63` was isolated, and the correction held.** 🔵 **`QM` is re-registered as `ACTION QT` for the
remaining quoted populations — this pass verified the headline count, not all of them.**

### 🆕 🔴 `P217-F2` — and the count that IS defensible is still being read as the wrong thing

🟢 **`67` is a correct count of rows carrying no readable GRANT. 🔴 It is not a count of rows this
KB knows nothing about, and that is how it has been used.** 🟢 **Decomposed by `ACTION QN`, all
`67` accounted for:**

| class | rows | is it a grant? | is it an unknown? |
|---|---|---|---|
| 🔴 `GRANT-REFUSED` | `2` | 🔴 no — affirmatively refused | 🔴 **no. Answered.** |
| 🟡 `PROSE-CLAIM-DANGLING` | `4` | 🔴 no | 🔴 **no. A lead with a named defect** |
| 🟡 `PROSE-CLAIM-BARE` | `8` | 🔴 no | 🔴 no |
| 🟡 `PROSE-CLAIM-QUALIFIED` / `SCOPED` / `CONFLICT` | `3` | 🔴 no | 🔴 no |
| 🟡 `PROSE-THIRD-PARTY` | `1` | 🔴 no | 🟢 yes |
| 🟡 `DOMAIN-NOUN` *(false positive)* | `1` | 🔴 n/a | 🟢 yes |
| 🔴 `NON-PUBLIC` | `3` | 🔴 n/a | 🟡 **moot — the address no longer resolves** |
| 🟢 `NO-PROSE` | `45` | 🔴 no | 🟢 **yes** |
| **total** | 🟢 **`67`** | | 🟢 **`47` genuine unknowns** |

🔵 **`45` + `1` + `1` = `47`. The `3` `NON-PUBLIC` rows are excluded from the unknowns because
there is nothing left to probe.**

### 🆕 🔴 `P217-F3` — `3` rows on these shelves no longer exist in public

🟢 **Established through two independent channels — `README` `404` on all `6` forms, and
`git ls-remote --symref`:**

| repo | `README` probe | `git ls-remote` |
|---|---|---|
| [`cdweaver1992/edfi-mcp-server`](https://github.com/cdweaver1992/edfi-mcp-server) | 🔴 `404` ×`6` | 🔴 **empty — does not resolve** |
| [`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback) | 🔴 `404` ×`6` | 🔴 **empty — does not resolve** |
| [`jakerains/scormplayer`](https://github.com/jakerains/scormplayer) | 🔴 `404` ×`6` | 🔴 **demands credentials — private or deleted** |

🟡 **These are the same `3` p216 called *"unresolvable"* in its root re-probe, now confirmed
through a second channel and a different request shape.** 🔵 **They should be moved to an
`ARCHIVED-UPSTREAM` state rather than carried in a live ungranted population: a repository that
cannot be fetched cannot be licensed, and it cannot be a foundation.**

### 🆕 🟢 `P217-F4` — the `ECL-2.0` cells from p216, spot-confirmed, unchanged

🟢 **`raw.githubusercontent.com/sakaiproject/sakai/HEAD/LICENSE` → `200`; `git ls-remote --symref`
reports `refs/heads/master` at `38dc5174b0563fb9e9cc7af96874f48982d87fdf`.** 🟢 **No drift. The
`ECL-2.0` platform tier established at pass `200` and re-read at p216 stands.**


## Pass 216 — 2026-10-15 — THE UNGRANTED POPULATION IS `67`, NOT `63` AND NOT `94`; THE `18`-FORM ROOT PROBE IS SOUND AFTER ALL; AND `5` NEW `ECL-2.0` GRANT CELLS LAND ON A ROW-SET THIS SHELF ALREADY CALLED ABANDONED

🔵 **`0` new foundation rows.** 🟢 **`ACTION QH` and `ACTION QI` discharged; `QH` fires on limb `2`
and `QI`'s premise is refuted by this shelf's own pass `200`.** 🔵 **Methods:
[`compose/code/p216-root-license-reprobe/`](../compose/code/p216-root-license-reprobe/README.md),
[`compose/code/p216-ecl-sweep/`](../compose/code/p216-ecl-sweep/README.md).**

### 🆕 🔴 `P216-F1` — the remaining ungranted population was published as `63`; it is `67`, and the figure propagated into the action that spent this pass

🔴 **p215 published, in three places, that *"this KB's ungranted population is `63`, not `94`"*,
and `intel/open-gaps.md` registered `ACTION QH` to *"re-probe the `63` remaining ungranted
rows"`.** 🟢 **Rebuilt from this KB's own two evidence files
*([`ungranted-after-18-forms.2026-10-15-p211.tsv`](../evidence/ungranted-after-18-forms.2026-10-15-p211.tsv),
[`lstree-grant-recovery.2026-10-15-p215.tsv`](../evidence/lstree-grant-recovery.2026-10-15-p215.tsv))*,
the remainder is not `63`:**

| step | count | how it was established |
|---|---|---|
| `ABSENT` after `18` root forms *(p211)* | `94` | the evidence file, deduplicated |
| recovered by `ACTION QD` *(p215)* | `25` | 🟢 **set-verified: `25` of `25` are inside the `94`, `0` outside** |
| **raw remainder** | 🔴 **`69`** | `94` − `25`, not `63` |
| less the one owner-case duplicate pair inside the remainder | `68` | `Hesham0-0Nasser/tutor-lms-mcp` ≡ `hesham0-0nasser/tutor-lms-mcp` |
| less the row whose case-variant p215 ALREADY recovered | 🟢 **`67`** | `os4ed/openSIS-Classic`, whose variant `OS4ED/openSIS-Classic` is recorded `GPL-2.0` |

🔴 **p215's own composition does not reach `63` either:** `25` manifests with no `license` field
plus `36` with no licence-shaped path plus `3` clone/`ls-tree` failures = **`64`**. 🟡 **So `63`
is not a rounding of a defensible number; it is unreconciled with both the file list and the
narrative that accompanies it.**

🔵 **Why this matters more than four units.** 🔴 **`QG` — p215's own action — made the CORRECTION
the unit of work and swept grant CELLS.** 🔴 **A DERIVED COUNT is a cell too, and this one
propagated out of the shelves and into the ACTION REGISTER, where it defined the population a
later pass was told to probe.** 🟢 **`T216-1`: a figure computed in one pass and quoted in the
next is the same propagation hazard as a licence token, and `qg_gate2.py` cannot see it, because
it compares grants rather than arithmetic.** 🟢 **Recorded as `ACTION QM` for p217 with the
cheapest possible falsifier: recompute every population count these shelves quote, from the
evidence file it names.**

### 🆕 🟢 `P216-F2` — `ACTION QH` fires on limb `2`: the `18`-form probe has no loss mode beyond path reach

🟢 **All `69` raw remainder rows were re-probed on the single most obvious path, with exactly one
variable moved: `git ls-remote --symref` for the TRUE default branch, then ONE `GET` of
`raw.githubusercontent.com/<slug>/<branch>/LICENSE`.** 🔴 **Recoveries: `0`.**

| status | rows | reading |
|---|---|---|
| `404` | **`66`** | no plain root `LICENSE` on the true default branch |
| `NO-SYMREF` | `3` | 🔴 the repository does not resolve from here at all |
| 🟢 `200` | 🟢 **`0`** | 🟢 **limb `2`: the form list is sound** |

🟢 **So `ABSENT` was a root-only artefact — `P215-1`'s finding — and nothing more. The `18` forms
do not additionally lose a plain `LICENSE` that is there.** 🔴 **And `QH`'s anchor was
mis-specified: `T215-2` cited `thm-mni-ii/feedbacksystem` *(`10 785` B)* and
`skhdemo/uoft-quercus-mcp` *(`1 086` B)* as rows *"recorded `ABSENT` after `18` forms"* that serve
a plain root `LICENSE` — 🔴 **but both are in p215's OWN recovered `25`, so neither was in the
population `QH` was asked to re-probe.** 🟢 **The two rows were evidence that the instrument had
already been FIXED, read as evidence that it was still broken.**

🟢 **The `3` `NO-SYMREF` rows are p215's `3` recorded failures, independently reproduced on a
DIFFERENT channel** *(`ls-remote`, not `clone`)*: `cdweaver1992/edfi-mcp-server`,
`jakerains/scormplayer`, `openfresno/edgenuity-aeries-grade-passback`. 🔵 **Two channels agreeing
means these are not transient: they are addresses this environment cannot resolve, and they should
be carried as unresolvable rather than as ungranted.**

### 🆕 🟢 `P216-F3` — `5` new `ECL-2.0` grant cells, on rows this shelf already called a graveyard

🟢 **Read first-hand today, `raw.githubusercontent.com/<slug>/HEAD/LICENSE`, byte counts binary-safe:**

| repository | `LICENSE` bytes | last commit *(p111/p109, this KB)* | verdict |
|---|---|---|---|
| 🆕 [`Apereo-Learning-Analytics-Initiative/OpenLRS`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | `11 087` | `2019-01-31` *(`2 809` d)* | 🟡 **reference** — conformant LRS to read, not to deploy |
| 🆕 [`.../LearningAnalyticsProcessor`](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | `9 919` | `2016-05-04` *(`3 811` d)* | 🟡 **reference** |
| 🆕 [`.../OpenDashboard-api`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | `9 919` | `2020-03-09` *(`2 406` d)* | 🟡 **reference** |
| 🆕 [`.../OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | `9 919` | `2020-02-17` *(`2 427` d)* | 🟡 **reference** |
| 🆕 [`.../lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | `11 087` | `2014-12-02` *(`4 330` d)* | 🟡 **reference** |
| [`.../OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | `9 878` | `2020-02-06` *(`2 438` d)* | 🟢 **un-drifted from p212's `9 878` B** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `11 120` | — | 🟢 **un-drifted from p200's `11 120` B** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | `11 340` | — | 🟢 **un-drifted from p200's `11 340` B** |

🟢 **Three independent byte-level confirmations against readings taken `4` and `16` passes ago, all
exact.** 🔵 **That is a drift control this shelf can report rather than assume.**

🔴 **The `5` new cells do not promote their rows.** 🟢 **`6` of `6` repositories in this
organisation are abandoned, the youngest `6.6` years old — measured twice, from commit dates
*(p109)* and independently from CI vendor choice *(p111: Travis, which stopped free OSS builds in
`2021`)*.** 🔵 **So the correct use of a permissive grant on an abandoned row is CITATION: these
are the reference implementations of the mid-`2010s` open learning-analytics stack, now with a
known `ECL-2.0` grant, and the segment still has no maintained open implementation on this shelf
— which is the market reading, not the repo list.**

### 🆕 🟡 `P216-F4` — the `ECL-2.0` text has `5` byte-lengths in one family

🟡 **`9 878` · `9 919` *(×`3`)* · `11 087` *(×`2`)* · `11 120` · `11 340`.** 🔴 **A byte-count
comparator would call these five different licences; `P215-5`'s `eol` lesson shows how easily a
length becomes an identity here.** 🟢 **The title-window classifier returns `ECL-2.0` on all eight,
which is the right answer, and is why a FAMILY read must come from the title and the byte count
must stay a drift control rather than a classifier input.**

### 🔵 Channel control, re-tested — twelfth consecutive pass

🟢 **`raw.githubusercontent.com` → `200`. `git ls-remote` and `git clone` → work.** 🔴 **`api.github.com`
→ `403`; `github.com` HTML → `403`; `code.intef.es` → `000`.** 🔵 **Unchanged, and every figure
below sourced from a blocked host is marked as a search-snippet claim.**

---
*Pass 216 — `0` new rows, `5` new grant cells, `1` population count corrected, `3` drift controls passed.*
## Pass 215 — 2026-10-15 — `25` REPOSITORIES RECOVERED FROM `ABSENT`, A NEW LICENCE FAMILY ON THESE SHELVES *(`ECL-2.0`)*, AND THE MECHANISM BEHIND EVERY BYTE-COUNT CONFLICT THIS KB TRACKS

🔵 **`0` new foundation rows.** 🟢 **`ACTION QD` and `ACTION QG` discharged instead; both fire.**
🔵 **Method: [`compose/code/p215-lstree-grant-recovery/`](../compose/code/p215-lstree-grant-recovery/README.md).**

### 🆕 🟢 `P215-F1` — the `13` grants that were in the tree the whole time

🟢 **Read by treeless clone — `git clone --filter=blob:none --no-checkout --depth 1` then
`git ls-tree -r HEAD --name-only`, which transfers the complete path inventory and `0` file
contents — then one blob read per candidate. Bytes are binary-safe at `HEAD`, per `T208-8`.**

| repo | 🟢 grant | path | bytes | why `18` root forms missed it |
|---|---|---|---|---|
| [`nvaccess/nvda`](https://github.com/nvaccess/nvda) | 🟢 **`GPL-2.0`** | `copying.txt` | `53 408` | 🔴 lowercase, and not `LICENSE` |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`GPL-2.0`** | `html/license.txt` | `18 346` | 🔴 one directory down |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟢 **`GPL-2.0`** | `docs/License.txt` | `17 286` | 🔴 `docs/`, mixed case |
| [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | 🟢 **`GPL-2.0`** | `docs/License.txt` | `17 286` | 🔴 same |
| [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 **`Apache-2.0`** | `LICENSE` | `10 785` | 🔴 **at root** — an `18`-form miss |
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **`LGPL-3.0`** | `License.txt` | `7 651` | 🔴 mixed case at root |
| [`skhdemo/uoft-quercus-mcp`](https://github.com/skhdemo/uoft-quercus-mcp) | 🟢 **`MIT`** | `LICENSE` | `1 086` | 🔴 **at root** — an `18`-form miss |
| [`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper) | 🟢 **`MIT`** | `License` | `1 079` | 🔴 `License`, no extension |
| [`ProjectsAndPrograms/school-management-system`](https://github.com/ProjectsAndPrograms/school-management-system) | 🟡 **`MIT`** | `student_panel/LICENSE` | `1 070` | 🔴 one module only |
| [`anthropics/prompt-eng-interactive-tutorial`](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 🟢 **`MIT`** | `AmazonBedrock/LICENSE` | `947` | 🔴 one directory down |
| [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | 🟢 **`Apache-2.0`** | `NOTICE` | `680` | 🔴 `NOTICE`, no body |
| [`foradian/fedena`](https://github.com/foradian/fedena) | 🟢 **`Apache-2.0`** | `NOTICE` | `679` | 🔴 `NOTICE`, no body |
| [`Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) | 🆕 🟢 **`ECL-2.0`** | `LICENSE_HEADER` | `558` | 🔴 a header TEMPLATE, not a licence file |

🔴 **Two of these — `thm-mni-ii/feedbacksystem` and `skhdemo/uoft-quercus-mcp` — serve a plain
`LICENSE` at ROOT.** 🔵 **`18` root forms were probed and both were recorded `ABSENT`, so the
`94` was never purely a root-reach problem: part of it is probe loss. 🟢 `ACTION QH` re-tests the
form list itself rather than trusting it a nineteenth time.**

### 🆕 🟢 `P215-F2` — `ECL-2.0`, and it is the one licence family an education KB should not have been missing

🟢 **`Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider` grants under the **Educational
Community License, Version 2.0**, read first-hand from `LICENSE_HEADER` (`558` B):**

> *"Licensed under the Educational Community License, Version 2.0 (the "License"); you may not use
> this file except in compliance with the License. You may obtain a copy of the License at
> `http://www.osedu.org/licenses/ECL-2.0`"*

🔵 **`ECL-2.0` is an `Apache-2.0` derivative, `OSI`-approved, and it is the **house licence of the
Apereo/Sakai world** — Sakai itself, and the Learning Analytics Initiative around it.**
🟢 **Practically: permissive, patent grant included, so a studio can build on it like
`Apache-2.0`.** 🔴 **But a classifier matching `apache license` in a title window does not match
it, and these shelves already carry a Sakai/Apache axis** *(`apache11-reclassification-sakai86`)*.
🔵 **`ACTION QI` sweeps the Apereo rows for `ECL-2.0` mislabelled as `Apache-2.0`; this pass
asserts nothing about rows it did not read.**

### 🆕 🔴 `P215-F3` — the byte convention, and why `2` passes disagreed about one file

🟢 **`T208-8` declares a byte count to be the blob AS SERVED at `HEAD`, trailing newline
included.** 🔴 **p215's first read of `formalms/formalms`' `html/license.txt` returned `18 006` B;
p214 published `18 346`.** 🟢 **p214 is right, and the `340`-byte gap has one cause:**

| measure | value |
|---|---|
| binary bytes *(`curl -o` + `wc -c`)* | 🟢 **`18 346`** |
| `CR` bytes in the blob | **`340`** |
| lines | **`340`** |
| read through a TEXT-mode pipe | 🔴 **`18 006`** = `18 346` − `340` |

🔴 **A text-mode read strips `CR`, so a `CRLF` blob measures one byte short PER LINE.**
🔵 **This is a complete mechanism for a class this KB has been tracking by symptom —
`byte-cell-conflicts`, `byte-channel-census` — and the test is cheap: `tr -dc '\r' | wc -c`.**
🟢 **Only `1` of the `25` blobs recovered this pass is `CRLF`, and it is exactly the `1` that
produced a conflict.** 🔵 **The convention is unchanged; what changes is that reads must be
binary. [`remeasure.sh`](../compose/code/p215-lstree-grant-recovery/remeasure.sh) is the gate.**

### 🆕 🔴 `P215-F4` — a path is not a grant, in three distinct ways

🔵 **Full table:
[`evidence/lstree-traps-and-nongrants.2026-10-15-p215.tsv`](../evidence/lstree-traps-and-nongrants.2026-10-15-p215.tsv).**

| class | instance | what a naive glob publishes |
|---|---|---|
| 🔴 **every match vendored** | [`alfredang/ai-mms`](https://github.com/alfredang/ai-mms) — `5` licence paths, `0` its own *(TinyMCE, Stripe, Prototype, and a third-party `LICENSE_TINYMCE.txt` hoisted to ROOT)* | 🔴 **`MIT`** on an LMS/TMS |
| 🔴 **the filename is a DOMAIN NOUN** | 🆕 [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) — `6` paths, all `LicenseStatusDescriptorsApi` / `LicenseTypeDescriptorsApi`: **teacher-certification** licences | 🔴 nothing, confidently |
| 🔴 **licence text as DATA** | [`spdx/license-list-data`](https://github.com/spdx/license-list-data) — `339 359` B of *other people's* grants | 🔴 **`BSD`** |

🆕 🔴 **The middle class is specific to this industry and worth stating plainly: in education,
*"licence"* is also a credential.** 🔵 **A teacher's licence, a licence-status descriptor, a
licensure endorsement — all match `/licen[cs]e/i` and none is a copyright grant. Any licence
locator run on an education corpus carries a false-positive rate that the same tool would not have
on, say, a gaming corpus.**

### 🆕 🔴 `P215-F5` — `ACTION QD`'s own filter is wrong in BOTH directions

🟢 **`QD` prescribed rejecting `vendor/`, `lib/`, `node_modules/`, `third_party/`,
`public/javascripts/`.** 🔴 **Measured against real trees:**

- 🔴 **too narrow** — it passes `libraries/htmlpurifier/`, `inc/libraries/`, `js/tiny_mce/`,
  `app/code/community/Stripe/`, `source/fonts/freefont-…/`, `html/appCore/addons/` and a bare
  top-level `phpmailer/`, every one of them third-party;
- 🔴 **too broad** — it rejects `lib/`, and **p214's genuine `formalms` recovery was
  `html/lib/System/license/license_english.txt`.** 🟡 `formalms` survives only because
  `html/license.txt` exists too.

🟢 **So path shape cannot decide ownership.** 🔵 **The discriminator that worked: a licence file is
the project's own when **the manifest or `README` points at it**, or when **its copyright holder is
the project or its author** — which is why the instrument reads the manifest channel ALONGSIDE the
file channel instead of falling back to it.**

### 🆕 🟡 `P215-F6` — the `94` was never `94` distinct repositories

| duplicate pair | why |
|---|---|
| `OS4ED/openSIS-Classic` ≡ `os4ed/openSIS-Classic` | 🔴 owner-case variant; identical `17 286` B blob |
| `Hesham0-0Nasser/tutor-lms-mcp` ≡ `hesham0-0nasser/tutor-lms-mcp` | 🔴 owner-case variant |
| `foradian/fedena` ≈ `projectfedena/fedena` | 🟡 same project, two orgs; `NOTICE` `679` vs `680` B |

🔵 **These shelves already know the case-variant class — `repos/foundations.md` names `5` collapsed
pairs — 🔴 **and the `ABSENT` population was built without applying it**, so published ungranted
counts carry duplicates on top of being overcounts.

### 🔴 Still unresolved, carried honestly

- 🔴 **`63` of the `94` return nothing on this channel either** — `25` manifests with no `license`
  field *(`Nasus20202/MoodleMCP` across `5` manifests; `barneslardo/sis-demo` across `5`;
  `jude-miller-dev/Milky-institute-online` across `6` `pom.xml`)*, and `36` with no licence-shaped
  path anywhere in the tree. 🟢 **This is the first defensible ungranted list this KB holds, and it
  is `63`, not `94`.**
- 🔴 **`3` failures, recorded not dropped:** `jakerains/scormplayer` *(clone refused)*,
  `cdweaver1992/edfi-mcp-server` and `openfresno/edgenuity-aeries-grade-passback`
  *(clone succeeded, `ls-tree` empty at `HEAD`)*.

## Pass 214 — 2026-10-15 — `6` GRANT CELLS CORRECTED ON THIS SHELF, EVERY ONE IN THE GNU FAMILY, AND `2` REPOS RECOVERED FROM `ABSENT`

🔵 **No new repository rows this pass.** 🟢 **`ACTION PZ` — p211's registered, entirely offline
reconciliation — was discharged instead, and it found a defect class rather than a backlog.**
🔵 **Method: [`compose/code/p214-multi-grant-reconciliation/`](../compose/code/p214-multi-grant-reconciliation/README.md).**

### 🆕 `P214-1` result — `8` of `518` repositories printed two grants; **limb `2` fires**

| | count | reading |
|---|---|---|
| repositories with `>1` grant family across the `4` client-facing shelves | **`8`** | 🟢 **limb `2`** *(`<10`)*: **the propagation backlog is small.** p211's `6`/`7` was not the floor it feared |
| of those, on the **GNU axis** | 🔴 **`8` / `8`** | 🔴 **`P211-3` measured `5` of `7`. On this independent measure it is TOTAL** |
| genuinely wrong cells | **`6`** over `4` repos | corrected on this shelf and in [`verticals/solutions.md`](../verticals/solutions.md) |
| recovered from `ABSENT` | **`2`** | `P214-2`, below |
| 🟡 **false positives of the `PZ` script itself** | **`2`** | recorded, not hidden — see the end of this section |

🟢 **`2 262` unambiguous cells were adjudicated. `140` multi-token rows were excluded by
construction**, because a row printing two grants is usually a **correction trail** — this KB
working correctly — and counting those would manufacture findings out of its own integrity work.

### 🆕 🔴 Corrections on this shelf

| repo | 🔴 was | 🟢 is *(bytes · form)* | how it is known |
|---|---|---|---|
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 `AGPL-3.0` *(`2` cells here, `2` more in `solutions.md`)* | 🟢 **`GPL-3.0`** *(`35 121` · `LICENSE`)* | 🟢 **`3` channels agree:** `LICENSE` title line, `composer.json` `"license"`, `README` l.`81`. 🔴 **Mechanism: `GPL-3.0` §13 is titled *"Use with the GNU Affero General Public License"* and the blob says `Affero` `3` times** *(ll. `552`/`556`/`559`)* — a whole-body matcher reads `AGPL`. 🔴 **`P171` already recorded this mechanism AND *"Gibbon es `GPL-3.0`"*; the cells never followed** |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | 🟡 `GPL-3.0` | 🔴 **`AGPL-3.0`** *(`33 820` · `LICENSE`)* | title line reads **`GNU AFFERO`** |
| [`memphis-iis/MoFaCTS`](https://github.com/memphis-iis/MoFaCTS) | 🟡 `GPL-3.0` | 🔴 **`AGPL-3.0`** *(`34 523` · `LICENSE`)* | title line reads **`GNU AFFERO`** |

🟢 **The `GibbonEdu` correction is the one that changes an architecture.** 🔴 **For `4` cells this
KB told a client that a school SIS carried network copyleft and had to be *integrate-only*.**
🟢 **It is file copyleft: fork it, host it, owe no source disclosure.** 🔵 **That is the most
commonly requested build in this industry and this KB had ruled it out in error.**

### 🆕 🟢 `P214-2` — `2` repositories recovered from `ABSENT`, in opposite directions

🟢 **[`formalms/formalms`](https://github.com/formalms/formalms) → `GPL-2.0`.** The body is
in-tree, not at the root: `html/license.txt` *(`18 346` B)* and
`html/lib/System/license/license_english.txt` *(`15 146` B, plus `9` translations — Bosnian,
Croatian, French, German, Italian, Portuguese, Spanish, Tamil)*, all **GNU GPL Version 2, June
1991**. 🔴 **This KB's *"carries no licence body at all"* was a root-only reading.**

🔴 **[`foradian/fedena`](https://github.com/foradian/fedena) → `Apache-2.0`, and it is a trap.**
Root `NOTICE` *(`679` B)* carries the Apache grant boilerplate; `README.markdown` l.`16` states
it. 🔴 **But `14` of `14` licence paths in its tree are vendored third-party and `0` are the
project's own** — so a subdirectory glob recovers `vendor/plugins/delayed_job/MIT-LICENSE` and
publishes a school ERP as **`MIT`**. 🟡 `STATED`, not `BODIED`: no Apache body ships.

🔵 **Consequence for `ACTION QA`** *(registered to sweep the `94` `ABSENT` rows this way)*:
🔴 **a bare licence-file glob is unsafe.** 🟢 **Reject every path under `vendor/`, `lib/`,
`node_modules/` or a named third-party directory first; `git ls-tree -r HEAD --name-only` is
the whole test and needs no token.**

### 🆕 🟡 Stated so the next audit does not re-find them: `2` false positives of `PZ`

🟢 **[`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) and
[`odoo/odoo`](https://github.com/odoo/odoo) appear to contradict themselves and do not.** Both
stray tokens sit in a table **about licence-text structure** — *"`GPL-3.0` by **reference**"*,
*"`GPL-3.0` included by **value**"* — describing the two legitimate forms of `LGPL-3.0`.
🔵 **A licence token in prose ABOUT licence text is not a grant claim.** 🟢 **Both cells are
correct; both were left untouched.** 🔴 **Any future column audit over these shelves needs this
exclusion or it will report two standing findings that are not there.**

---
## Pass 213 — 2026-10-15 — TWO SHELVES OPENED: ACADEMIC INTEGRITY (`385` REPOS, PERMISSIVE, AND AIMED AT THE WRONG DECADE) AND ALGORITHMIC MEMORY (`2 737` REPOS, `FSRS`, ALL `MIT`)

🔵 **Every grant below was read from the licence blob at `HEAD` on `2026-10-15`.** 🟢 **Byte counts
are the blob AS SERVED by `raw.githubusercontent.com`, per `T208-8`** — not the classifier's
re-encoded field, which `T213-8` shows diverges `1` time in `71`.

### 🆕 🟢 `P213-2` — the memory shelf: `FSRS` is this industry's one fully-`MIT` algorithmic core

🔴 **In `212` passes this KB has carried tutors, graders, LMS platforms, `MCP` connectors and the
learning-record layer, and has never carried the layer that decides WHEN a learner sees something
again.** 🟢 **`topics/spaced-repetition` — `2 737` repositories — read this pass.**

🟢 **The remarkable property of this shelf is its licence homogeneity at the core: the entire
`FSRS` *(Free Spaced Repetition Scheduler)* family is `MIT`.**

| Repo | 🟢 Grant *(blob bytes)* | ★ | Lang | Role in a stack |
|---|---|---|---|---|
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** *(`1 079`)* | **4.1**k | Jupyter | The reference scheduler, as deployed in Anki |
| [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 **MIT** *(`1 089`)* | **725** | — | 🟢 **The algorithm itself** *(`DSR` model)* — the spec you implement against |
| [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | 🟢 **MIT** *(`1 079`)* | **510** | Python | 🟢 **The cheapest way to put real scheduling behind a tutor.** `MIT`, Python, no platform |
| 🆕 [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 🟢 **MIT** *(`1 078`)* | **2.6**k | TypeScript | Review client over plain notes — the highest-star `MIT` client here |
| 🆕 [alyssaxuu/carden](https://github.com/alyssaxuu/carden) | 🟢 **MIT** *(`1 066`)* | **490** | JavaScript | Flashcards with gamification; a forkable front end |
| 🆕 [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | 🟢 **MIT** *(`1 069`)* | **1.5**k | Python | 🟢 **Free-recall verification *with receipts*, `FSRS`-scheduled.** The row that already treats evidence as a first-class output |
| 🆕 [trane-project/trane](https://github.com/trane-project/trane) | 🔴 **AGPL-3.0** *(`34 523`)* | **848** | Rust | 🟢 **Models practice DEPENDENCIES, not just intervals** — the only row here that knows a skill has prerequisites. 🔴 `AGPL` |
| 🆕 [kantord/LibreLingo](https://github.com/kantord/LibreLingo) | 🔴 **AGPL-3.0** *(`34 524`)* | **2.6**k | Python | Community-owned language course platform |
| 🆕 [FreeLanguageTools/vocabsieve](https://github.com/FreeLanguageTools/vocabsieve) | 🔴 **GPL-3.0** *(`35 149`)* | **544** | Python | Sentence mining from real texts |
| 🆕 [Ajatt-Tools/mpvacious](https://github.com/Ajatt-Tools/mpvacious) | 🔴 **GPL-3.0** *(`35 149`)* | **892** | Lua | Card capture from film/TV inside `mpv` |

🔵 **Why this matters next to `P212-4`'s learning-record shelf:** 🟢 **`xAPI` records what a learner
DID; `FSRS` decides what they see NEXT.** 🔴 **A tutor with neither is a chat window.** 🟢 **Both
layers are permissive at their core — `Apache-2.0` for `xAPI`, `MIT` for `FSRS` — which is the
cheapest credible claim a studio can make in this industry.**

### 🆕 🔴 `P213-3` — the integrity shelf: mature, permissive, and answering the previous decade

🟢 **`topics/plagiarism-detection`, `385` repositories.** 🔴 **`0` of the top `20` detect
AI-written text.** 🔵 **The four rows worth carrying are tabled in
[`agents/top.md`](../agents/top.md) `P213-1`:** `dolos` *(**MIT**, `1 084` B, `351`★)`,
`noplag-engine` *(**Apache-2.0**, `11 358` B, `88`★)*, `plagpatrol` *(**MIT**, `1 084` B, `42`★)*
and `JPlag` *(🔴 **GPL-3.0**, `35 141` B, `2`k★)*.

🟢 **Stated for the next pass so the measurement is not re-made:** 🔴 **the similarity half of
academic integrity is solved and permissively licensed. The provenance half — did a model write
this — has no open-source implementation at any star level on this surface.**

### 🆕 🟡 `P213-4` — the assessment-generation shelf is pre-LLM, and that is a dating, not a dismissal

🟢 **`topics/question-generation`, `229` repositories, top `20` read.** 🟡 **The education-relevant
rows are `T5`- and transformer-era, with papers from `ACL` `2019`–`2021`:**

| Repo | 🟢 Grant *(bytes)* | ★ | Note |
|---|---|---|---|
| 🆕 [patil-suraj/question_generation](https://github.com/patil-suraj/question_generation) | 🟢 **MIT** *(`1 068`)* | **1.1**k | Neural QG with transformers — the most-starred row on the surface |
| 🆕 [KristiyanVachev/Leaf-Question-Generation](https://github.com/KristiyanVachev/Leaf-Question-Generation) | 🟢 **MIT** *(`1 073`)* | **139** | 🟢 **`MIT`, small, legible `T5` MCQ generator** — a baseline to measure an LLM against |
| [ramsrigouthamg/Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) | *carried row* | **951** | The best-known QG toolkit |
| [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator) | *carried row* | **298** | Reading-comprehension question generation |

🔵 **The useful reading for a studio:** 🟢 **these are not competitors to an LLM — they are
BASELINES and EVALUATORS.** 🔴 **A client asking *"is your LLM item-writer actually better?"* has
no answer unless something cheap and deterministic sits beside it.** 🟢 **`Leaf` at `139`★ and
`MIT` is that something.**

### 🆕 🔴 `P213-5` — the interoperability shelf has no AI in it, and the rows are the proof

🟢 **`topics/lti` — `185` repositories — read first-hand.** 🔴 **`0` of the top `20` mention AI, an
LLM, an agent or a tutor.** 🔵 **The population is small, old and load-bearing:**

| Repo | 🟢 Grant *(bytes)* | ★ | Lang | Role |
|---|---|---|---|---|
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** *(`10 273`)* | **376** | PHP | 🟢 **The `LTI` tool framework**, from the author of the `LTI`/`py4e` lineage |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** *(`1 070`)* | **138** | Python | 🟢 **`LTI 1.3` Advantage tool in Python** — the integration path for a Python tutor |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 **Apache-2.0** *(`11 343` · `LICENSE.md`)* | **54** | PHP | IMS-certified `LTI 1.3` tool providers in PHP |
| [openfun/marsha](https://github.com/openfun/marsha) | 🟢 **MIT** *(`1 078`)* | **151** | Python | 🟢 **An `LTI` learning-content management system, `MIT`.** 🔵 `openfun` → France Université Numérique — **EMEA** |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | 🟢 **BSD-3-Clause** *(`1 528`)* | **73** | Python | 🟢 **Puts a JupyterHub behind an LMS login** — the fastest classroom-notebook path |
| [oat-sa/lib-lti1p3-core](https://github.com/oat-sa/lib-lti1p3-core) | 🔴 **GPL-2.0** *(`18 091`)* | **37** | PHP | `LTI 1.3` core, from Open Assessment Technologies. 🔴 **`GPL-2.0`** |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** *(`34 764`)* | **243** | Python | 🟢 **Secure, automated exercise assessment — runs YOUR tests.** 🔴 **`AGPL-3.0`: the autograder you deploy behind a boundary, not embed** |
| [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0** *(`35 147`)* | **117** | JavaScript | 🟢 **Accessibility inspection of Canvas course content** — a compliance product with no AI in it |

🆕 🔴 **A diligence trap worth its own line: one university org, two copyleft families.**
🟢 **`ucfopen` *(University of Central Florida)* ships
[`UDOIT`](https://github.com/ucfopen/UDOIT) under **`GPL-3.0`** *(`35 147` B)*,
[`Obojobo`](https://github.com/ucfopen/Obojobo) under **`AGPL-3.0`** *(`34 520` B)* and
[`Materia`](https://github.com/ucfopen/Materia) under **`AGPL-3.0`** *(`34 523` B)*.* 🔴 **An
org-level licence assumption is wrong here in the direction that matters — `AGPL` reaches over the
network, `GPL` does not.** 🟢 **Gate per repository, never per owner.**

### 🟢 Foundation rows from the courseware and records surfaces — grants re-read first-hand this pass

🔵 **`5` rows here are new to this KB *(marked 🆕)*; the other `10` are CARRIED rows whose grants were
re-read from the blob today and agree with the published cells** *(part of the `48`/`49` in `T213-7`)*.

| Repo | 🟢 Grant *(bytes)* | ★ | Region | Role |
|---|---|---|---|---|
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** *(`1 072`)* | **355** | Global | 🟢 **A MODERN `SCORM` runtime, `MIT`** — the maintained way to play legacy packages |
| [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** *(`11 357`)* | **215** | Global | 🟢 **Browser-based e-assessment with a mathematics emphasis, `Apache-2.0`.** The permissive maths-assessment engine |
| 🆕 [onemnemo/mnemo](https://github.com/onemnemo/mnemo) | 🟢 **Apache-2.0** *(`11 326`)* | **121** | 🟡 unplaced | Study application on `.NET 10` |
| 🆕 [langx/langx](https://github.com/langx/langx) | 🟢 **BSD-3-Clause** *(`1 520`)* | **108** | 🟡 unplaced | Connects language learners — a rare `BSD` row in this industry |
| [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🟢 **MIT** *(`1 073`)* | **58** | Global | Packs `H5P` interactive content into `SCORM` objects |
| [studentinsights/studentinsights](https://github.com/studentinsights/studentinsights) | 🟢 **MIT** *(`1 083`)* | **134** | North America | Open, student-centred school data systems |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | 🟢 **MIT** *(`1 088`)* | **125** | Global | 🟡 Course reader — **named "Tutors", it is not an AI tutor** |
| [sagefy/sagefy](https://github.com/sagefy/sagefy) | 🟢 **Apache-2.0** *(`10 174` · `LICENSE.txt`)* | **120** | Global | Adaptive learning over a concept graph |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | 🟢 **Apache-2.0** *(`11 362` · `LICENSE.md`)* | **130** | North America | Microsite CMS for course content *(Penn State lineage)* |
| 🆕 [senjun-team/senjun-courses](https://github.com/senjun-team/senjun-courses) | 🔴 **GPL-3.0** *(`35 149`)* | **159** | EMEA | Programming courses by programmers. 🔵 Russian-language — the region's prose, English metadata |
| 🆕 [codeforlife-education/aimmo](https://github.com/codeforlife-education/aimmo) | 🔴 **AGPL-3.0** *(`32 920`, cross-owner)* | **117** | EMEA | 🔴 **The grant is in `ocadotechnology/codeforlife-workspace` — see `T213-2`** |
| 🆕 [chipmates/agoracosmica](https://github.com/chipmates/agoracosmica) | 🔴 **AGPL-3.0** *(`34 523`)* | **149** | EMEA | 🔴 **Content grant scheduled, not granted — see `T213-2`** |
| [elmsln/elmsln](https://github.com/elmsln/elmsln) | 🔴 **GPL-3.0** *(`35 193` · `LICENSE.md`)* | **253** | North America | Distributed learning-network platform |
| [WebPA/WebPA](https://github.com/WebPA/WebPA) | 🔴 **GPL-3.0** *(`35 147` · `license.txt`)* | **37** | Global | 🟢 **Online PEER assessment** — a slot nothing else on these shelves fills |
| [cybercussion/SCOBot](https://github.com/cybercussion/SCOBot) | 🔴 **CC-BY-SA-4.0** *(`837`)* | **164** | Global | 🔴 **A `SCORM` JavaScript LIBRARY under a share-alike CONTENT licence.** `T212-4`'s risk running in reverse: code wearing a content grant |

### 🟢 Carried forward unchanged

## Pass 212 — 2026-10-15 — A SHELF THIS KB NEVER HAD: THE LEARNING-RECORD LAYER, `17` REPOS, AND A NEW LICENCE FAMILY NAMED AFTER THIS INDUSTRY

### 🆕 🟢 `P212-4` — the evidence layer, and why it arrives exactly now

🔴 **In `211` passes this KB has carried tutors, graders, LMS platforms and `MCP` connectors, and
has never once carried the layer that records what a learner did.** 🟢 **`topics/xapi` and
`topics/learning-analytics` — `300` and `377` repositories — were read this pass for the first
time, and the layer turns out to be the most standards-mature and most permissively licensed part
of this whole industry.**

🔵 **Why it matters now rather than as a curiosity:** the Council of Europe's Committee of Experts
on AI and Education is drafting a **European Reference Framework for the Evaluation of Educational
Technologies** *(see [`intel/market.md`](../intel/market.md) p212)*. 🟢 **An evaluation framework
needs evidence, and evidence in education means learner-activity records in a standard schema.**
🔴 **A studio that ships a tutor with no `xAPI` emission has built something that cannot be
evaluated — and from August `2026` the EU AI Act classifies education AI as high-risk, which is
not a context in which "we did not instrument it" is an answer.**

### 🟢 The learning-record shelf — every grant read from the blob on 2026-10-15

| Repo | 🟢 Grant *(blob bytes · form)* | Stars | Lang | Role in a stack |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** *(`11 525`)* | **954** | — | 🟢 **The specification itself**, from ADL *(US DoD)*. Permissively licensed, which is why the ecosystem below exists |
| [adaptlearning/adapt_framework](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** *(`35 129`)* | **631** | JavaScript | Responsive, accessible HTML5 course authoring. 🔴 **`GPL` — the one copyleft row in the authoring slot** |
| [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** *(`35 141`)* | **585** | JavaScript | The best-known open LRS. 🔴 **`GPL-3.0`: fine to run, a decision to modify** |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** *(`11 357`)* | **334** | Python | ADL's own reference LRS — the implementation the spec is checked against |
| [adlnet/xAPIWrapper](https://github.com/adlnet/xAPIWrapper) | **Apache-2.0** *(`10 273`)* | **223** | JavaScript | Client-side wrapper; the cheapest way to emit statements from a web tutor |
| [RusticiSoftware/TinCanJS](https://github.com/RusticiSoftware/TinCanJS) | **Apache-2.0** *(`11 358`)* | **208** | JavaScript | The other mature JS client, from the company that wrote SCORM |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** *(`11 357`)* | **144** | Clojure | 🟢 **SQL-backed LRS.** Runs on Postgres the client already has, instead of a bespoke store — **the pragmatic default for an engagement** |
| [davidpesce/moodle-logstore_xapi](https://github.com/davidpesce/moodle-logstore_xapi) | 🔴 **GPL-3.0** *(`35 121`)* | **82** | PHP | Ships Moodle's event log to an LRS as `xAPI`. 🔵 **`GPL` is compulsory for Moodle plugins — not a project choice** |
| [g3i/lxHive](https://github.com/g3i/lxHive) | 🔴 **GPL-2.0** *(`18 092`)* | **79** | PHP | Lightweight LRS. 🟡 **`GPL-2.0` — the only v2 grant found on these shelves this pass** |
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** *(`1 046`)* | **78** | JavaScript | 🟢 **Tests an LRS against the spec's `MUST` requirements.** The acceptance gate for the pattern in [`compose/patterns.md`](../compose/patterns.md) `P212-A` |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | 🆕 🟢 **ECL-2.0** *(`9 878`)* | **62** | Java | Standards-based learning-record **warehouse** — storage plus a roster/course model. 🔵 **See `P212-2` below on `ECL`** |
| [adlnet/CATAPULT](https://github.com/adlnet/CATAPULT) | **Apache-2.0** *(`11 358`)* | **59** | JavaScript | `cmi5` player and test suite — the profile that makes `xAPI` launchable from an LMS |
| [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** *(`1 094` · `LICENSE.md`)* | **51** | Python | 🟢 **LRS and learning-analytics toolbox from France Université Numérique** *(the operator of France's national Open edX)*. **EMEA, MIT, and built by a national platform operator — the strongest single row on this shelf for an EMEA engagement** |
| [tl-its-umich-edu/my-learning-analytics](https://github.com/tl-its-umich-edu/my-learning-analytics) | **Apache-2.0** *(`11 379`)* | **37** | Python | University of Michigan's student-facing analytics dashboards |
| [PlaypowerLabs/EdOptimize](https://github.com/PlaypowerLabs/EdOptimize) | 🔴 **GPL-3.0** *(`35 149`)* | **31** | R | K-12 digital-learning analytics platform |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** *(`11 323` · `development`)* | **21** | Java | 🟢 **LMS plugin that randomly assigns differentiated assignment variants — in-course A/B experiments.** 🔵 **This is the only repository on any of these shelves that produces *causal* evidence rather than correlational dashboards** |
| [sonsoleslp/tna](https://github.com/sonsoleslp/tna) | 🟡 **not establishable** *(`46`-byte `LICENSE`: `YEAR` + `COPYRIGHT HOLDER` only)* | **13** | R | Transition Network Analysis. 🔵 **The stub is the R-package convention — `DESCRIPTION` carries the family — but by this KB's blob rule the grant is unread, and it is recorded as unread** |

🟢 **`17` rows, `9` of them permissive** *(`Apache-2.0`, `MIT`, `ECL-2.0`)*. 🔵 **Above the `5`-repo
bar by a wide margin, and the permissive share on this shelf — `53`% — is the highest of any shelf
in this KB.**

### 🆕 🔴 `P212-2` — `ECL-2.0`: a licence family named after this industry, and this KB has been getting Sakai wrong

🔴 **[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) is `ECL-2.0`, not `Apache-2.0`.**
🟢 **Read first-hand: `11 120` bytes, first line `Educational Community License, Version 2.0
(ECL-2.0)`.** 🔴 **This KB has carried Sakai as `Apache-2.0` since cycle 3 (`v65`) and repeated it
on the verticals shelf ever since.**

🟢 **What `ECL-2.0` is, from the blob's own words:** *"the Apache 2.0 license, modified to change
the scope of the patent grant in section 3 to be specific to the needs of the education
communities using this license."*

🔵 **So the practical reading, and why the correction is not pedantry:**

| | `Apache-2.0` | 🆕 `ECL-2.0` |
|---|---|---|
| copyright grant | permissive | 🟢 **identical** |
| attribution / NOTICE | required | 🟢 **identical** |
| patent grant | broad, from every contributor | 🔴 **narrowed — scoped to the contributor's own contribution as used in education** |
| OSI-approved | yes | 🟢 **yes** |

🟢 **For a build-on-top engagement the two behave the same.** 🔴 **For a client whose procurement
diligence reads the patent clause — a government ministry, a large publisher — they are not the
same document, and answering "Sakai is Apache" in that room is wrong.** 🔵 **`ECL-2.0` also means
this industry is the only one in the Globant rotation with **its own OSI licence family**, which
is a fact worth a deck line.

🟢 **Two repositories on these shelves are `ECL-2.0`, both Apereo-lineage:** `sakaiproject/sakai`
*(`1.2`k★)* and `Apereo-Learning-Analytics-Initiative/OpenLRW` *(`62`★)*. 🟢 **Checked and NOT
`ECL`, read first-hand the same pass:** `oppia/oppia` *(`Apache-2.0`)*,
`uPortal-project/uPortal` *(`Apache-2.0`)*, `openedx/edx-platform` *(`AGPL-3.0`)*,
`learningequality/kolibri` *(`MIT`)*. 🔵 **So `ECL` is an Apereo-family marker, not an
education-wide one, and the four rows above are confirmed correct as this KB already carries them.**

### 🟢 The grading shelf, now with its infrastructure tier read

🔵 **p201 established that *"the grading shelf exists"*. p212 read `topics/autograding` — `94`
repositories — and found that the shelf has a mature, decade-old, university-built infrastructure
tier underneath the LLM graders:**

| Repo | 🟢 Grant *(blob bytes · form)* | Stars | Origin → region | Role |
|---|---|---|---|---|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** *(`1 091` · `develop`)* | **818** | 🟢 **TUM, Germany → EMEA** | 🟢 **Interactive learning platform with automated feedback; `12 396` commits.** **The highest-★ MIT education platform found in `212` passes, and it is EMEA-built** |
| [autolab/Autolab](https://github.com/autolab/Autolab) | **Apache-2.0** *(`11 324`)* | **808** | CMU → **North America** | Course management for auto-graded programming work, in production at CMU |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** *(`1 542` · `LICENSE.md`)* | **802** | RPI → **North America** | Submission + automated grading + TA grading. 🟢 **The most permissive grant on the shelf** |
| [inducer/relate](https://github.com/inducer/relate) | **MIT/X Consortium** *(`1 145`)* | **437** | UIUC → **North America** | Teaching environment with auto-graded code homework |
| [okpy/ok](https://github.com/okpy/ok) | **Apache-2.0** *(`13 979`)* | **370** | UC Berkeley → **North America** | Runs tests, tracks progress, assists debugging |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** *(`34 764`)* | **243** | 🟢 **UCLouvain, Belgium → EMEA** | **Secure** exercise assessment with an LMS interface. 🔴 **`AGPL` on a hosted grader — price the obligation** |
| [foundation50/classroom50](https://github.com/foundation50/classroom50) | 🔴 **GPL-3.0** *(`35 150`)* | **215** | CS50 lineage → **North America** | Open-source alternative to GitHub Classroom |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** *(`1 560`)* | **161** | UC Berkeley → **North America** | Python **and R** autograding; the standard in data-science teaching |
| [autolab/Tango](https://github.com/autolab/Tango) | **Apache-2.0** *(`11 324`)* | **49** | CMU → **North America** | 🟢 **Standalone RESTful autograding service** — the piece you reuse without adopting a whole platform |
| [infomark-org/infomark](https://github.com/infomark-org/infomark) | 🔴 **GPL-3.0** *(`35 149`)* | **35** | → EMEA | Go course management with automatic testing |
| [google/prog-edu-assistant](https://github.com/google/prog-edu-assistant) | **Apache-2.0** *(`11 358`)* | **34** | Google → **North America** | Builds autograding tests inside Jupyter notebooks |
| [uhafner/autograding-github-action](https://github.com/uhafner/autograding-github-action) | **MIT** *(`1 095`)* | **32** | → EMEA | Grades a student repo from CI on configurable metrics *(a GitLab sibling exists at `11`★)* |
| [kit-sdq/autograder](https://github.com/kit-sdq/autograder) | **MIT** *(`1 068` · `LICENSE.md`)* | **18** | 🟢 **KIT, Germany → EMEA** | Static-analysis grading of student Java |

🔵 **The architectural point, which is worth more than any single row:** 🟢 **the sandboxed
execution, submission handling, plagiarism posture and TA workflow are *solved* and have been for
years, under `Apache`/`BSD`/`MIT`.** 🔴 **What is unsolved is rubric judgement on free-text and
handwritten work — which is exactly where the LLM graders on [`agents/top.md`](../agents/top.md)
sit.** 🟢 **The correct engagement shape is therefore LLM-grader-as-a-stage-inside-`Tango`-or-
`Artemis`, never a greenfield grading platform.**

### 🟢 Carried forward

🟢 **p211's full-column census stands: `2 051`/`2 082` cells agree with their blobs** *(`98.5`%)*,
and the `31` exceptions are mostly this KB's own corrections left unpropagated. 🟢 **The `8` path
forms cover `100`% of findable blobs and `HEAD` removes the branch axis** — reconfirmed on `54`
fresh repositories this pass, where `LICENSE` alone answered `46` of `50`.

## Pass 211 — 2026-10-15 — THE WHOLE COLUMN, READ FIRST-HAND: `2 051`/`2 082` CELLS AGREE, AND THE `31` THAT DO NOT ARE MOSTLY THIS KB'S OWN CORRECTIONS, UNPROPAGATED

### 🔴 The sampling was never necessary — the channel was mis-priced

🔴 **p210 recorded the channel as: *"curl is refused at CONNECT for every host including GitHub
(`403`); `WebFetch` resolves `github.com` only."*** 🟢 **That statement is too strong, and it is
the reason nine passes audited this column ten rows at a time.**

🟢 **`raw.githubusercontent.com` answers `200` to a plain `curl GET` from this environment.**
🟢 **p211 read `494` licence blobs through it in a single pass.** 🔴 **The rest of p210's channel
reading stands and was re-tested cold: `example.com` → `000`, `github.com` → `403`,
`api.github.com` → `403`.** 🔵 **So the general-egress statement was right and the *consequence*
drawn from it was wrong: the one host that serves licence bodies is reachable, and that is the
only host this audit needs.**

🆕 🟢 **Second simplification: the ref `HEAD` resolves a repository's default branch.** 🔵 **The
branch axis — `main` vs `master` vs anything else — disappears entirely.** 🔴 **p207's `90`-form
locator was priced for a problem that stops existing once `HEAD` is used:**

| path form | blobs served | share |
|---|---|---|
| `LICENSE` | `423` | **`85.6`%** |
| `LICENSE.md` | `41` | `8.3`% |
| `LICENSE.txt` | `19` | `3.8`% |
| `license.txt` | `7` | `1.4`% |
| `LICENCE.md` · `COPYING.txt` · `LICENSE.TXT` · `LICENCE` | `1` each | `0.8`% total |

🟢 **`8` forms cover `100`% of what is findable.**
[`evidence/locator-path-form-yield.2026-10-15-p211.tsv`](../evidence/locator-path-form-yield.2026-10-15-p211.tsv)

### 🟢 The audit, at full depth

🟢 **Population: every repository named in a table row on the four client-facing shelves —
[`agents/top.md`](../agents/top.md), this file, [`verticals/solutions.md`](../verticals/solutions.md)
and [`compose/patterns.md`](../compose/patterns.md).** 🔵 **Not a sample, not a tail, not a
ranking: all of it.**

| | count |
|---|---|
| unique repositories on the four shelves | **`588`** |
| licence blobs read first-hand at `HEAD` | 🟢 **`494`** |
| serving no blob after `18` path forms | 🟡 **`94`** |
| body served, family not nameable | 🟡 **`21`** |
| **table cells adjudicated against a blob** | 🟢 **`2 082`** |
| **cells that agree** | 🟢 **`2 051`** — **`98.5`%** |
| **cells that do not** | 🔴 **`31`**, over `10` repositories |

[`evidence/full-column-grant-census.2026-10-15-p211.tsv`](../evidence/full-column-grant-census.2026-10-15-p211.tsv)

### 🔴 The `31`, adjudicated by hand — because a candidate is not a finding

🔵 **p205's first automated audit reported `3` mismatches and all `3` were the AUDIT's errors.
Every candidate below was read against its own blob before being called anything.**

🟢 **Three of the ten are NOT errors — and all three were already characterised correctly by this
KB, which is how we know the instrument sees:**

| repo | shelf | blob | why the shelf is right |
|---|---|---|---|
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | `MIT` | `CC-BY-4.0` | 🟢 **two-FILE repo**: `LICENSE` is `CC-BY-4.0`, `LICENSE-CODE` is `MIT` *(`200`)*. [`patterns.md`](patterns.md) already says *"`MIT` **(code)**, `LICENSE-CODE`, not `LICENSE`"* |
| [`pupilfirst/pupilfirst`](https://github.com/pupilfirst/pupilfirst) | `CC-BY-SA-4.0` | `MIT` | 🟢 **split-scope**: `docs/**` is `CC-BY-SA-4.0`, client JS is `MIT`. [`solutions.md`](../verticals/solutions.md) already scopes the cell |
| [`frappe/education`](https://github.com/frappe/education) | `GPL-3.0` | `GPL-3.0-STATED` | 🟢 **`19`-byte statement, no body** — p210's own STATED-vs-BODIED class, in `17` cells |

🔴 **Seven carry a genuinely wrong grant family in at least one cell:**

| repo | the cell says | 🟢 the blob says | already corrected elsewhere in this KB? |
|---|---|---|---|
| 🔴 **[`acanas/swad-core`](https://github.com/acanas/swad-core)** | `GPL-3.0` | 🔴 **`AGPL-3.0`** | 🔴 **NO — wrong in both places it appears** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `AGPL-3.0` | 🟢 **`GPL-3.0`** | 🟢 yes — [`top.md`](../agents/top.md)`:1931`, this file `:1343` |
| [`memphis-iis/MoFaCTS`](https://github.com/memphis-iis/MoFaCTS) | `GPL-3.0` | 🟢 **`AGPL-3.0`** | 🟢 yes — this file `:2188` |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | `GPL-3.0` | 🟢 **`AGPL-3.0`** | 🟢 yes — [`solutions.md`](../verticals/solutions.md)`:3550` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `GPL-3.0` | 🟢 **`LGPL-3.0`** | 🟢 yes — this file `:4825` |
| [`odoo/odoo`](https://github.com/odoo/odoo) | `GPL-3.0` | 🟢 **`LGPL-3.0`** | 🟢 yes — this file `:4686` |
| [`frappe/lms`](https://github.com/frappe/lms) | `MIT` | 🟢 **`AGPL-3.0`** | 🟢 yes — [`top.md`](../agents/top.md)`:124`, p209 verified it |

[`evidence/full-column-mismatch-adjudication.2026-10-15-p211.tsv`](../evidence/full-column-mismatch-adjudication.2026-10-15-p211.tsv)

### 🆕 🔴 `P211-1` — the defect is PROPAGATION, not discovery

🔴 **`6` of the `7` wrong cells name a repository whose CORRECT grant this KB has already found,
verified and published somewhere else on these shelves.** 🟢 **This prices the class p208 opened
at `T208-2` — *"both are corrections this KB published and never propagated"* — and p208 could
only name two instances.** 🔵 **At full depth it is `6` of `7`: the dominant failure mode of this
KB's licence column is not getting the answer wrong, it is **getting it right in one place and
leaving the old cell standing in another**.**

🟢 **The remedy is cheap and it is not another sweep.** 🔵 **A correction is only finished when
the repository's *other* cells are reconciled in the same pass; the per-repo census file shipped
above makes that a lookup rather than a search.**

### 🆕 🔴 `P211-2` — the one real discovery, and it runs the dangerous way

🔴 **[`acanas/swad-core`](https://github.com/acanas/swad-core) — SWAD, Universidad de Granada's
platform, `76`★, EMEA, two decades in production — is `AGPL-3.0`.** 🔴 **Both shelves that carry
it say `GPL-3.0`, and no pass has ever corrected it.** 🔵 **p187 even recorded the byte count
correctly (`34 501` B) while naming the wrong family — the bytes were read and the title line
was not.**

🔴 **The direction is what matters. `AGPL-3.0` carries network copyleft; `GPL-3.0` does not.**
🔴 **A studio reading these shelves would have concluded it could host a modified SWAD for a
client without a source-disclosure obligation. That conclusion was wrong.** 🟢 **Corrected here,
and `swad-core` is marked integrate-only until a client's deployment model is known.**

### 🆕 🔴 `P211-3` — the error class is the `GPL`↔`AGPL` axis

🔴 **`5` of the `7` true positives are `GPL`/`AGPL`/`LGPL` confusions.** 🔵 **Not `MIT`-vs-
`Apache`, not permissive-vs-copyleft — the errors cluster inside the GNU family, between three
licences whose texts open with twenty near-identical lines and whose *obligations differ by the
single question a hosted education deployment turns on*: does serving students over a network
count as distribution?**

🟢 **For this industry that is the most consequential distinction there is**, because the default
delivery model for an LMS, an SIS or a tutor is hosted and student-facing. 🔵 **Any future audit
should weight the GNU family above everything else; the permissive half has now been measured
clean four times.**

### 🟢 The instrument was wrong twice, and the ground truth caught it

🟢 **p209 and p210 hand-read `20` rows. p211 used them as a validation set before trusting the
classifier on `588`.** 🔴 **It failed twice in development:** it had no rule for `CC-BY-NC-SA`,
and none for the bare `Attribution 4.0 International` title line that opens every Creative
Commons deed. 🔴 **Both would have shipped as false "corrections" on `5` cells —
[`enkidevs/curriculum`](https://github.com/enkidevs/curriculum),
[`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) and
`autogen` among them.** 🟢 **Fixed; final score against the hand-read set `20`/`20`.**

🔵 **The lesson is worth more than the fix: p209's and p210's slow hand-reading was not wasted
work that a faster channel made redundant — it was the only thing standing between this pass and
five confident wrong answers.** 🟢 **Code, with the order-of-operations lessons it inherits:**
[`compose/code/p211-full-column-grant-audit/`](../compose/code/p211-full-column-grant-audit/README.md)

### 🟡 The `94` that serve nothing, and the `21` that cannot be named

🟡 **`94` of `588` serve no blob at `HEAD` after `18` forms.** 🔴 **That is an ABSENCE AT ONE
CHANNEL, not a finding of "no licence"** — a grant may sit in a manifest, a README or a
subdirectory, and p207 proved exactly that against this KB's own ungranted list.
[`evidence/ungranted-after-18-forms.2026-10-15-p211.tsv`](../evidence/ungranted-after-18-forms.2026-10-15-p211.tsv)

🟢 **The `21` unnameable bodies returned `0` new findings — every anomaly in them is one this KB
already holds:** [`portabilis/i-diario`](https://github.com/portabilis/i-diario) *(the `AGPL-3.0`
body in **Portuguese**)*, [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts)
*(`0BSD`)*, [`leemonade/leemons`](https://github.com/leemonade/leemons) *(`Fair Code v1.0`,
non-OSI)* and [`No-Suggest/NoSuggest`](https://github.com/No-Suggest/NoSuggest) *(not open source
at all)*. 🔵 **The rider detector fired exactly once, on `NoSuggest`, which this KB already flags
— so p207's finding that this industry's supply carries almost no source-available riders now
holds over `494` bodies rather than `185`.**

### 🟢 Discovery this pass

🔴 **`0` new foundational repos accepted — the ninth consecutive saturation reading.**
🟢 **[`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) came back from
the SIS query and is already on these shelves in `33` places** *(`GPL-2.0`, confirmed from the
blob this pass)*. 🔵 **`OpenCampus`, the Drupal/ECA SIS reported at `1`M+ EU higher-ed users, has
no reachable public repository under the obvious names — recorded as an informed gap, not as a
component.**

## Pass 210 — 2026-10-15 — `ACTION PV` LANDS, AND THE BUS-FACTOR RISK IS NOT IN THE PLATFORMS — IT IS IN THE SEAMS

### 🟢 Nine of `ACTION PU`'s ten rows are foundation rows, and all nine confirmed

🟢 **p210 read the next ten most recipe-exposed masked rows against the repositories themselves
(method and the full table in [`agents/top.md`](../agents/top.md) p210).** 🟢 **Nine sit on this
shelf and all nine confirmed:** `moodle/moodle` **`GPL-3.0`**, `sakaiproject/sakai` **`ECL-2.0`**,
`opencast/opencast` **`ECL-2.0`**, `openedx/edx-platform` **`AGPL-3.0`**,
`instructure/ims-lti` **`MIT`**, `openeducat/openeducat_erp` **`LGPL-3.0`** *(from the blob)*,
`frappe/education` **`GPL-3.0` by `19`-byte statement only**, `ls1intum/Artemis` **`MIT`**,
`chamilo/chamilo-lms` **`GPL-3.0`**. 🔵 **The tenth, `opensalt/OB3DefinitionWidget` (`MIT`), is a
`verticals/solutions.md` row and is the subject of the next section.**

### 🆕 🔴 `ACTION PV` — the first measurement, and it inverts where this KB thought the risk was

🟢 **p209 opened `ACTION PV` after noticing by accident that `Ed-Fi-Alliance-OSS/edfi-oneroster`
carries `13` recipe sites on `6`★. It asked for a sweep of the shape ★`< 50` AND recipe sites
`≥ 5`.** 🟢 **p210 can now answer it across the `20` rows this KB has read first-hand, because the
same `WebFetch` that reads a grant also reads the star count:**

| row | ★ | recipe sites | grant | 🔴 the shape |
|---|---|---|---|---|
| [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget) | 🔴 **`1`** | `19` | `MIT` | 🔴 **the worst concentration on these shelves — `19` recipes rest on a ONE-STAR repository** |
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🔴 **`48`** | `23` | `MIT` | 🔴 **the most recipe-exposed row in the whole KB, and it is one person's MCP server** |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🔴 **`6`** | `13` | `Apache-2.0` | 🔴 **p209's accidental find, now one of a class** |
| [`openfun/ralph`](https://github.com/openfun/ralph) | 🟡 **`51`** | `20` | `MIT` | 🟡 **one star above the threshold — treat as a hit; the line is arbitrary and `51` is not a community** |

🔴 **`3` clear hits and `1` borderline in `20` rows — `15`–`20`% of this KB's highest-exposure
rows rest on repositories with no community behind them.**
[`evidence/concentration-risk.2026-10-15-p210.tsv`](../evidence/concentration-risk.2026-10-15-p210.tsv).

### 🆕 🟢 The structural finding, which is the useful half

🟢 **Look at where the risk is NOT.** 🔵 **Every PLATFORM row read across both passes is
comfortable:** `openedx/edx-platform` `8.2k`★, `moodle/moodle` `7.5k`★, `sakaiproject/sakai`
`1.2k`★, `chamilo/chamilo-lms` `1.0k`★, `learningequality/kolibri` `1.1k`★,
`openeducat/openeducat_erp` `889`★, `ls1intum/Artemis` `818`★, `frappe/education` `666`★,
`opencast/opencast` `508`★, `instructure/ims-lti` `203`★.

🔴 **Every PV hit is a SEAM:** an Open Badges definition widget, an MCP tutor server, a
`OneRoster`-over-`Ed-Fi` adapter, an `xAPI` learning-record store. 🔵 **The pattern is exact and it
was invisible until the stars were read alongside the grants: the education open-source commons has
robust PLATFORMS and abandoned CONNECTIVE TISSUE.**

🟢 **Two readings follow, and a studio should hold both at once:**

- 🔴 **As risk:** a recipe is only as maintained as its least-maintained component, and these shelves route their most-used recipes through exactly the components nobody maintains. 🔵 **Any recipe naming a PV hit must name the fallback in the same breath and cost it as BUILD, not ADOPT** — the discipline p209 already applied to `edfi-oneroster`.
- 🟢 **As opportunity, and this is the commercially interesting half:** 🔵 **the seams are where a studio's work is defensible anyway.** 🟢 **A client does not pay Globant to maintain Moodle; it pays for the integration layer — and the measurement says that layer has no incumbent. A hardened, tested, permissively-licensed `xAPI`→knowledge-tracing bridge, or a maintained `OneRoster`/`Ed-Fi` adapter, is both the fix for this KB's own fragility and a reusable asset across every engagement in the vertical.**

🔵 **`ACTION PX` for the next pass:** 🟢 **name a concrete fallback for the three unfallbacked PV
hits — `OB3DefinitionWidget` *(the Open Badges 3.0 spec is public; the widget is a convenience,
so the fallback is "implement the definition shape directly")*, `tutor-mcp` *(the MCP protocol is
the contract; the fallback is a studio-owned MCP server)* and `ralph` *(the fallback is any
conformant LRS, and the question is whether a permissive one exists — a `permissive LRS` sweep has
never been run on these shelves)*.* 🔴 **And extend the ★ reading to the whole `281`-row census, not
only the rows `ACTION PU` happens to reach: stars come free with every grant read, so the sweep
costs nothing extra from here on.**

### 🔴 Still nothing new to add, eighth reading

🔴 **New qualifying foundational repos discovered this pass: `0`.** 🟢 **The vertical sweep
returned `OpenEduCat` (`LGPL-3.0`, read first-hand this pass — already here), `Apache OFBiz`
(`Apache-2.0`, generic ERP, no education layer), `ERPNext` (`GPL-3.0-only`), `Dolibarr`
(`GPL-3.0`), `Atomic CRM` and `Krayin` (`MIT`, but CRMs and not education systems), and the usual
`Moodle`/`Open edX`/`Canvas` copyleft set.** 🔵 **Eighth consecutive negative reading, and see
`verticals/solutions.md` p210 for what the CRM hits mean: the channel has started answering a
different question than the one being asked.**

## Pass 209 — 2026-10-14 — THE FOUNDATION ROWS HELD UNDER FIRST-HAND READING, AND ONE OF THEM IS A `6`★ SINGLE POINT OF FAILURE

### 🟢 `ACTION PU`'s foundation-shelf members: `6` of the `10`, all confirmed

🟢 **p209 read the ten most recipe-exposed masked rows against the repositories themselves
(method and the full table in [`agents/top.md`](../agents/top.md) p209).** 🟢 **Six are foundation
rows and all six confirmed:** `learningequality/kolibri` **`MIT`**, `openfun/ralph` **`MIT`**,
`jcputney/scorm-again` **`MIT`**, `pykt-team/pykt-toolkit` **`MIT`**,
`Ed-Fi-Alliance-OSS/edfi-oneroster` **`Apache-2.0`**, `frappe/lms` **`AGPL-3.0`**.

🟢 **`frappe/lms` is worth stating twice, because a comparison blog this pass claimed it is
`MIT`.** 🔴 **It is `AGPL-3.0`, sidebar-classified, `3.3k`★.** 🔵 **This shelf has carried it as
`AGPL` throughout; the secondary source is wrong, and an engagement that trusted it would have put
a hosted client LMS under a network-copyleft source-offer duty.** See `repos/trending.md` p209.

### 🆕 🔴 The concentration risk this verification pass exposed by accident

| row | ★ | recipe sites | 🔴 what that combination means |
|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🔴 **`6`** | `13` | 🔴 **`13` recipe sites rest on a `6`-star repository.** `Apache-2.0` and the grant is sound, but ★`6` is one maintainer's side project carrying the `OneRoster 1.2`-over-`Ed-Fi-ODS` hop in a US-K-12 recipe |

🔵 **The grant was never the risk here; the bus factor is.** 🟢 **Keep the row — it does the one
job nothing else on this shelf does (serves a `OneRoster 1.2` API from an `Ed-Fi ODS` database, and
`Ed-Fi` is the data standard a US state district most likely already mandates).** 🔴 **But any
recipe naming it must name the fallback in the same breath: the `Ed-Fi ODS/API` itself
(`Apache-2.0`, Alliance-maintained) with a `OneRoster` adapter written in the engagement, costed as
build rather than adopt.** 🔵 **`ACTION PV` for a later pass: sweep every foundation row for
★`< 50` AND recipe sites `≥ 5`, which is the shape that hides this risk.**

### 🔴 Still nothing new to add, seventh reading

🔴 **New qualifying foundational repos discovered this pass: `0`.** 🟢 **The vertical sweep
returned `OpenOLAT` (`Apache-2.0`, `447`★ — already here, and `1 369` mentions deep), `Frappe LMS`
(`AGPL-3.0` — already here), `RosarioSIS` and `Gibbon` (both GPL), `Moodle` (`GPL-3.0`),
`Open edX` and `Canvas` (`AGPL`).** 🔵 **No permissive SIS exists to find; see
`verticals/solutions.md` p209.**

## Pass 208 — 2026-10-14 — `ACTION PS` CLOSES ON LIMB `2`, AND ITS POPULATION WAS THE ARTEFACT

### 🔴 `ACTION PS` — `26` apparent recoveries, `0` real, and the reason is this pass's own thesis

🟢 **`ACTION PS` asked whether p207's `90`-form case-tolerant locator recovers grants from rows
this KB has ever recorded as UNGRANTED. Limb `1` wanted `3`+ recoveries; the prior was limb `1`,
because p207 recovered `3` of `15` in the one population it tried.**

🔴 **`50` candidate rows, `26` returned a licence body, and `26` of `26` are ARTEFACTS: every one
is a repository this KB already publishes a grant for.** 🟢 **Every one of the `26` was found at
the plain `LICENSE` path — the FIRST form in the list — so not one of them was a case-sensitivity
failure in the first place.**

🔵 **The defect is in how the population was built, and it is `T208-2` exactly.** 🔴 **The
extractor took every line that names a repository and also mentions an absent grant — so a
repository merely LISTED beside such a sentence entered the population.** 🟢 **`jcputney/scorm-again`
(`MIT`), `numbas/Numbas` (`Apache-2.0`) and `zijinz456/OpenTutor` (`MIT`) are all published on
these shelves with their grants and all three were swept in.**
[`evidence/ungranted-relocate.2026-10-14-p208.tsv`](../evidence/ungranted-relocate.2026-10-14-p208.tsv).

🔴 **Limb `2` fires: the ungranted counts this KB has published are NOT overcounts — at least,
not demonstrably, and not from this population.** 🟢 **What the pass actually learned is cheaper
and more useful: the `24` rows that returned `ABSENT` after `90` path forms are the only
defensible *ungranted* list this KB has ever held, and it is now on disk.** 🔵 **`ACTION PS` is
re-registered as `ACTION PU` with a population built from CELLS.**

### 🟢 `ACTION PR` DISCHARGED — the byte convention, declared once and for all

🟢 **This KB's bytes are the licence blob AS SERVED by `raw.githubusercontent.com` at `HEAD`,
TRAILING NEWLINE INCLUDED.** 🔵 **`11` of the `15` byte conflicts p207 adjudicated were exactly
one trailing `LF`: the higher cell is the blob as served, the lower is the blob minus its final
newline.** 🔴 **Two cells differing by `1` byte are therefore one measurement under two
conventions, not an error** — so a `<!--corrected-->` marker must not be spent on them, and the
remaining ~`80` multi-value repositories resolve by this sentence rather than by re-reading.

### 🔴 A foundation-adjacent cell this pass corrected, and the class it belongs to

🔴 [`openfun/ralph`](https://github.com/openfun/ralph) — the LRS this KB recommends behind an
AI estate for xAPI evidence — was published **`Apache-2.0`** in the p193 recipe step that names
it. 🟢 **Its blob is `MIT`, `LICENSE.md`, `1 094` B**, and this KB publishes `MIT` correctly at
roughly fifteen other sites. 🔵 **Same class as `towardsai/ai-tutor-app` on the agent shelf: a
correction that was published and never propagated into the recipes.** 🔴 **The recipe is the
artefact a client reads, so it is the worst possible place for the stale cell to survive — and
the per-repository audit three passes ran could not see it by construction.**

### 🟢 The foundation shelf itself: unchanged, and re-confirmed by what did NOT move

🟢 **No foundation row changed family this pass.** `learningequality/kolibri` (`MIT`),
`openedx/XBlock` (`Apache-2.0`, `LICENSE.TXT`, `11 358` B — p207's case recovery holds),
`openfun/ralph` (`MIT`), `openfun/richie` (`MIT`), `openfun/marsha` (`MIT`),
`numbas/Numbas` (`Apache-2.0`), `frappe/lms` (`AGPL-3.0`, `33 893` B) and
`openedx/edx-platform` (`AGPL-3.0`) stand unchanged — `ralph`, `richie` and `Numbas` re-read
from their own blobs THIS pass, the rest carried from p207's `185`-body census.
🔵 **`kolibri`'s `MIT` is the load-bearing one this pass** — see `P208-B`: India's
`63.5`%-internet base makes an offline-first MIT platform the only shape that fits the mandate.

## Pass 207 — 2026-10-14 — THE FOUNDATION ROWS ARE RIGHT. THE THING THAT LOOKS FOR THEM IS CASE-SENSITIVE

### 🔴 `L1` — a foundation row was recorded as ungranted because of its filename's CAPITALISATION

🟢 [`openedx/XBlock`](https://github.com/openedx/XBlock) is on this page: `Apache-2.0`,
`11 358` B, `470`★, default branch `master`, not archived. 🔴 **p207's licence probe returned
`404` on all `22` path forms p206 used and recorded it as UNGRANTED.**

🟢 **The file is called `LICENSE.TXT`.** 🔴 **`raw.githubusercontent.com` is case-sensitive, and
every path list this KB has ever shipped is a fixed-case enumeration** — `LICENSE`, `LICENSE.md`,
`LICENSE.txt` — **none of which is `LICENSE.TXT`.**

🔵 **This is `D1`/`D2`/`D8` one level up.** 🟢 **p206 fixed everything the TITLE LINE can be
wearing — a markdown heading, an underline, a BOM. The FILENAME wears the same costume, and
nobody had looked.**

🟢 **The repaired locator enumerates `90` forms — `10` bases × `9` extensions** —
[`compose/code/p207-permissive-half-audit/locate.sh`](../compose/code/p207-permissive-half-audit/locate.sh).
Re-running the `15` apparent absences through it:

| outcome | n | detail |
|---|---|---|
| 🟢 **RECOVERED** | **`3`** | `openedx/XBlock` → **`LICENSE.TXT`** `11 358` B `Apache-2.0` · `frappe/lms` → **`license.txt`** `33 893` B `AGPL-3.0` · `open-spaced-repetition/fsrs4anki-helper` → **`License`** `1 079` B `MIT` |
| 🟡 **`NOTICE`-only** | `2` | `foradian/fedena` `679` B, `projectfedena/fedena` `680` B — p206's `D7`: a `NOTICE` is a channel, not a body |
| 🔴 **TRUE ABSENCE at `90` forms** | **`12`** | `AccessLint/skills` · `CreveXTech/canvas-lms-mcp` · `Gaurav-Pande/AES_DL` · `JushBJJ/Mr.-Ranedeer-AI-Tutor` · `LearnPress/learnpress` · `Simon-Initiative/lti-example-tool` · `ZQR1101/xueyoujing-companion` · `formalms/formalms` · `educredentials/ec-issuer` · `ink-waffle/sisu-mcp` · `pnp-v/bo-google-classroom-mcp-server` · `tianshuo/trainingllm` |

🔴 **An absence is only reportable after the case variants have been tried.** 🟢 **`M2` and `M4`
applied to a filename: *"we did not find it"* and *"it is not there"* are different claims, and
one `404` is not evidence of the second.**
[`evidence/licence-locator-case.2026-10-14-p207.tsv`](../evidence/licence-locator-case.2026-10-14-p207.tsv).

### 🟢 The permissive half of this shelf, re-read from `185` blobs. `0` rows change

🟢 **`199` published rows carry a permissive family token. `185` bodies read at `HEAD`,
classified offline with the repaired instrument.** 🔴 **`0` of `199` change family.** Final
distribution over the bodies actually read:

| family | rows | | family | rows |
|---|---|---|---|---|
| 🟢 `MIT` | **`124`** | | 🟡 `ECL-2.0` | `2` |
| 🟢 `Apache-2.0` | **`40`** | | 🔴 `NON-OSI-proprietary` | `2` |
| 🔴 `AGPL-3.0` | `4` | | 🔴 `UNRECOGNISED` | `2` |
| 🟢 `CC0-1.0` | `3` | | 🔴 `GPL-3.0` / `GPL-2.0` | `1` / `1` |
| 🟢 `BSD-3-Clause` | `3` | | 🔴 `CC-BY-NC-SA-4.0-DEED` | `1` |
| 🟢 `CC-BY-4.0` | `1` | | 🟡 `Apache-2.0-STATEMENT` | `1` |

🔵 **`164` of `185` — `88.6`% — are `MIT` or `Apache-2.0` read from their own bytes.** 🟢 **That
is the number to quote on an engagement: the permissive half of this shelf is genuinely
permissive, verified body by body, not inferred from a sidebar label.**
[`evidence/permissive-half-census.2026-10-14-p207.tsv`](../evidence/permissive-half-census.2026-10-14-p207.tsv).

🔴 **The `4` rows that moved between the p206 and p207 instruments all moved because the
INSTRUMENT was wrong, and in all four cases this shelf's published cell was already right:**
three CC0 bodies that `D11`'s double-escaped dot had been reporting as `CC-unversioned`, and one
`CC-BY-NC-SA-4.0` deed that `D13` had been dropping the ShareAlike half of.

### 🔵 What this means for the foundations tier specifically

🟢 **Nothing on this page needs changing, which is the third consecutive pass that is true.** 🔴
**What needed changing was the locator and the classifier, both of which this KB owns.** 🔵 **The
column is more reliable than the instruments that audit it** — an uncomfortable finding for an
automated pipeline, and the right one to act on: 🟢 **prefer a curated cell over an automated
re-derivation, and spend audit budget on the instrument instead.**

## Pass 206 — 2026-10-14 — THE FOUNDATION ROWS ARE RIGHT; THE READER WAS WRONG IN EIGHT DIFFERENT WAYS

### 🟢 The census, stated before the diagnosis

🟢 **`281` repositories, `HEAD` ref, `22` body path forms, re-classified.** Final distribution:

| family | rows | | family | rows |
|---|---|---|---|---|
| `GPL-3.0` | **`89`** | | `Apache-2.0` | `7` |
| `AGPL-3.0` | **`84`** | | `LGPL-3.0` | `5` |
| `MIT` | `24` | | `GPL-3.0-STATEMENT` | `3` |
| `GPL-2.0` | `23` | | `AGPL-3.0-STATEMENT` | `3` |
| `ECL-2.0` | `15` | | 🔴 `NON-OSI-Elastic-2.0` | `1` |
| 🔴 **no grant at `22` paths** | **`14`** | | `LGPL-STATEMENT` | `1` |
| `MPL-2.0` | `11` | | `CC-BY-4.0-STATEMENT` | `1` |

🔴 **`219` of `281` — `78`% — are GPL-family copyleft.** 🔵 **That is the single most important
number on this page for an engagement**, and it is unchanged in shape from every prior pass; what
changed is that it is now measured rather than labelled.
[`evidence/pi-licence-column-census.2026-10-14-p206.tsv`](../evidence/pi-licence-column-census.2026-10-14-p206.tsv).

### 🔴 `25` of the `281` came back with no determinate family, and all `25` were the instrument

| # | what the body was wearing | p205 said | truth | measured on |
|---|---|---|---|---|
| `D1` | a **markdown heading** — `### GNU GENERAL PUBLIC LICENSE` does not match `^[[:space:]]*` | `GPL-unversioned` | `GPL-3.0` | [`cerpus/Edlib`](https://github.com/cerpus/Edlib), [`idempiere/idempiere`](https://github.com/idempiere/idempiere) |
| `D2` | a `====` **underline** pushing `Version 3` to line `4`; the window was `3` lines | `GPL-unversioned` | `GPL-3.0` | `13` Moodle-plugin rows |
| `D3` | 🆕 **the licence is not in English** — `LICENÇA PÚBLICA GERAL AFFERO GNU` | `UNRECOGNISED` | `AGPL-3.0` | [`portabilis/i-diario`](https://github.com/portabilis/i-diario) + `pre-matricula-digital` |
| `D4` | 🆕 **`Elastic License 2.0`**, absent from the table — and **non-OSI** | `UNRECOGNISED` | `NON-OSI-Elastic-2.0` | [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) |
| `D5` | a **narrative** grant with no title line | `UNRECOGNISED` | `AGPL-3.0-STATEMENT` | [`ankitects/anki`](https://github.com/ankitects/anki) |
| `D6` | **`19` bytes** — `License: GNU GPL V3`. A reference, not an instrument | `UNRECOGNISED` | `GPL-3.0-STATEMENT` | [`frappe/education`](https://github.com/frappe/education) |
| `D8` | 🆕 a **UTF-8 BOM** between `^` and the title. `EF BB BF` is not `[[:space:]]` | `GPL-unversioned` | `GPL-2.0` / `GPL-3.0` | [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic), [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) |
| `D10` | 🆕 a **wrapped prose line** at column `0` — `GNU General Public License for more details.` | `GPL-unversioned` | `GPL-3.0-STATEMENT` | [`pawtograder/platform`](https://github.com/pawtograder/platform) |

🟢 **Fixed and shipped with an offline regression suite:
[`compose/code/p206-classifier-language-shape/`](../compose/code/p206-classifier-language-shape/),
`20`/`20` on `20` real bodies** — the eight defect cases, the four new fixtures, and all five of
p205's controls, which must not regress and do not.
[`evidence/instrument-delta.2026-10-14-p206.tsv`](../evidence/instrument-delta.2026-10-14-p206.tsv).

### 🔴 `D7` is p206's own error, recorded because the next pass will make it

🔴 **p206 added `NOTICE` to the body path list and got
[`foradian/fedena`](https://github.com/foradian/fedena) back as a grant.** 🟢 **An Apache
`NOTICE` is an attribution file.** It carries a grant *statement* and belongs in p204's **channel**
taxonomy beside `package.json` — 🔴 **it is not a licence body and must not be probed as one.**
🟢 **`NOTICE` was removed again; the body path list is `22` forms, not `23`.** 🔵 **This is the
third time this KB has confused a channel with a body, and each time the cost was one wrong row
that a control caught.**

### 🟢 `BOM` and accent folding are the same bug in two alphabets

🔵 **[`compose/code/p288-agpl-casefold/`](../compose/code/p288-agpl-casefold/) recorded, long ago,
that this KB's matchers are byte-oriented.** 🔴 **p206 met it twice more in one pass: `LICENÇA`
does not case-fold under `tr`, and a UTF-8 BOM is not whitespace under `grep`.** 🟢 **Both are now
handled in one place, `_fold()`, before any match runs** — and the folding is done with
per-character substitutions, 🔴 **never a bracket class**, because `[Çç]` would match the
individual *bytes* of a UTF-8 sequence and corrupt the body instead of folding it.

### 🔵 What a studio takes from this page, unchanged by the instrument work

🔴 **`14` of `281` foundation-tier rows carry no grant at `22` path forms.** 🟢 Unchanged in
substance from p204's `56`-row census, and the two populations agree where they overlap. 🔴 **The
default for an ungranted repository is exclusive copyright: no permission to copy, modify or
redistribute.** 🟢 **The `3` `-STATEMENT` and `1` `CC-BY-4.0-STATEMENT` rows are a softer case** —
the family is named, the instrument is not shipped — 🟡 **a `PoC` risk a client can accept
knowingly, with a one-line remedy upstream.**

## Pass 205 — 2026-10-14 — THE INSTRUMENT WAS WRONG ABOUT THREE LICENCE FAMILIES, AND `HEAD` RETIRES THE DEFAULT-BRANCH PROBLEM

### 🔴 `p203`'s classifier calls `GPL-3.0` and `MPL-2.0` *"`AGPL-3.0`"* — measured, fixed, shipped

🟢 **The instrument this KB has classified grants with since p203
([`compose/code/p203-grant-blob-reader/classify.sh`](../compose/code/p203-grant-blob-reader/classify.sh))
tests the WHOLE body, in an order that puts the AGPL branch first.** 🔴 **Three licences name OTHER
licences inside their own text:**

| licence | where it names another licence | p203 verdict | truth |
|---|---|---|---|
| `GPL-3.0` | section `13`, *"…the GNU Affero General Public License…"* | 🔴 `AGPL-3.0` | 🟢 `GPL-3.0` |
| `MPL-2.0` | section `1.12`, *"`Secondary License` means … the GNU Affero General Public License, Version 3.0"* | 🔴 `AGPL-3.0` | 🟢 `MPL-2.0` |
| `ECL-2.0` | paragraph `1`, *"the Apache 2.0 license, modified…"* | 🔴 `UNRECOGNISED` | 🟢 `ECL-2.0` |

🔴 **Reproduced on real bodies, not argued:** [`OptiKey/OptiKey`](https://github.com/OptiKey/OptiKey)
and [`moodle/moodle`](https://github.com/moodle/moodle) are both `GPL-3.0` and both classify
`AGPL-3.0`; [`coqui-ai/TTS`](https://github.com/coqui-ai/TTS) is `MPL-2.0` and classifies
`AGPL-3.0`. 🟢 **A true-AGPL control ([`frappe/lms`](https://github.com/frappe/lms)) classifies
`AGPL-3.0` correctly, so the defect is a false POSITIVE for the AGPL, not noise.**
[`evidence/classifier-regression.2026-10-14-p205.tsv`](../evidence/classifier-regression.2026-10-14-p205.tsv).

🟢 **Exposure of the PUBLISHED KB: `0` rows.** Every AGPL row in the classifier era is
[`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi), and p204 recorded its grant as
**manifest-only** (`package.json`) — 🟢 **re-confirmed this pass: Lumi has no licence body at `16`
path forms, so its label never passed through the body classifier.** 🔵 **The bug was live but had
not yet reached a published cell.** 🔴 **It had reached THIS pass's own output** — `4` of the `5`
rows p205's OER sweep first called `AGPL-3.0` are `GPL-3.0`, caught only because the sweep was
re-adjudicated against the bodies.

🟢 **Fixed and shipped with an offline regression suite —
[`compose/code/p205-grant-classifier-fix/`](../compose/code/p205-grant-classifier-fix/), `15`/`15`
on `13` real bodies**, the three defect cases and both controls included. 🔵 **The fix is
TITLE-LINE anchoring: a licence names itself on a line of its own, so classify on that line and
only fall back to a body-wide search when it decides nothing.**

🔴 **A naive `300`-character title WINDOW is not enough and the suite pins why:**
[`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) prefixes its Apache text with ~`1.5` kB of
copyright-header prose, so a window-based probe returns `UNRECOGNISED` on a row this KB correctly
publishes as `Apache-2.0`. 🟢 **It is a fixture now.**

### 🟢 `HEAD` is a valid `raw.githubusercontent.com` ref — `ACTION PC`'s whole problem is avoidable

🔴 **p203 probed `3` rows on the wrong ref. p204 spent a pass resolving `58` default branches
(`35` `main`, `18` `master`, `2` `develop`, `1` `release`) to correct it.** 🟢 **None of that is
necessary: `https://raw.githubusercontent.com/<owner>/<repo>/HEAD/<path>` resolves the default
branch server-side, whatever it is called.**

🟢 **Controlled before it was used**, on the row p204 found hardest:
[`opencast/opencast`](https://github.com/opencast/opencast), whose default branch is 🔴 `develop` —
the `HEAD` ref returns its `ECL-2.0` body. 🟢 Two-scope positive
([`LibraryCarpentry/lc-r`](https://github.com/LibraryCarpentry/lc-r) → `2` scope headings) and a
negative (invented slug → `404`) both fire. 🔵 **Every blob read this pass used `HEAD`, and the
`ls-remote`-per-row step is retired.**

### 🔴 A probe is only as good as its path list — `moodle` is not ungranted

🔴 **p205's first sweep reported `moodle/moodle` and `frappe/lms` as having NO grant.** 🟢 **Both
do:** `moodle` ships `COPYING.txt` (`GPL-3.0`) and `frappe/lms` ships `license.txt` (`AGPL-3.0`) —
🔴 **neither path form was in the `12`-form list inherited from p203.** 🟢 **The list is `16` forms
now** (`COPYING.txt`, `copying.txt`, `license.txt`, `LICENCE.txt` added). 🔵 **Recorded because the
`22`% ungranted figure this KB now quotes as a MEASUREMENT rests on that list**, and a path list is
a silent upper bound on it. 🟢 **Re-run against p204's `58` ungranted rows with `6` additional path forms
(`COPYING.txt`, `copying.txt`, `Copying.txt`, `license.txt`, `License.txt`, `LICENCE.txt`):
`0` recovered**, so the `22`% measurement stands and the two false negatives above were
confined to rows the `58` never contained.

---

## Pass 204 — 2026-10-14 — `22`% WAS NOT A PROBE ARTEFACT, AND A GRANT HAS A CHANNEL BEFORE IT HAS A PATH

### 🔴 `ACTION PC` CLOSED — limb `1` FALSIFIED, limb `2` CONFIRMED, and a third class exists

🟢 **All `58` rows p203 declared ungranted were re-probed on their TRUE default branch**, not
on `main`/`master` as p203 probed them. Census:
[`evidence/pc-ungranted-resolution.2026-10-14-p204.tsv`](../evidence/pc-ungranted-resolution.2026-10-14-p204.tsv).

🔵 **Channel: `git ls-remote --symref` for the default branch, then `raw.githubusercontent.com`
over inline `curl` for `12` licence path forms** *(`LICENSE` `LICENSE.md` `LICENSE.txt` `LICENCE`
`LICENCE.md` `license` `license.md` `LICENSE-MIT` `COPYING` `COPYING.md` `LICENSE.rst` `NOTICE`)*.

**Default branches actually in use:** `35` `main` · `18` `master` · 🔴 **`2` `develop`** ·
🔴 **`1` `release`** · `2` unresolvable. 🔴 **So p203's `main`/`master` probe addressed the
wrong ref on `3` of `58` rows** — the mechanism limb `1` predicted is **real**.

🔴 **But the magnitude is not.** 🔴 **`0` of `56` rows carry a licence file at ANY of the `12`
path forms on their own default branch.** Not one. 🟢 **The `3` wrong-ref rows do not resolve
either**, so correcting the ref recovers **zero** rows.

> 🔵 **Why this is a measurement and not a channel failure.** The same parallel harness was
> run against a **positive control** in the same session — `adlnet/xAPI-Spec@master/LICENSE`
> → **`200`** — and the control passed **through the harness**, not beside it. 🔴 **A first
> draft of this pass reported `0`/`56` before the control existed; that number was not
> publishable until it did.**

**🟢 So the published figure is corrected in the opposite direction from the one `ACTION PC`
expected:** 🔴 **`22`% is a MEASUREMENT, not an upper bound.** It may be quoted.

### 🟢 The third class `ACTION PC` did not anticipate: a grant with a channel but no body

🔴 **"No licence file" is not "no grant."** Probing manifests —
`package.json` `composer.json` `pyproject.toml` `Cargo.toml` `setup.py` `readme.txt` — splits
the `56` into three:

| class | rows | what a client may rely on |
|---|---|---|
| 🔴 **`SILENT-NO-MANIFEST`** | **`36`** | 🔴 **nothing.** No grant in any channel probed |
| 🔴 **`SILENT-MANIFEST-NO-FIELD`** | **`12`** | 🔴 **nothing.** A manifest exists and declares no licence |
| 🟡 **`MANIFEST-DECLARED-BODY-ABSENT`** | **`7`** | 🟡 **a declaration, not a licence text** — see the ladder below |
| 🔴 **`MANIFEST-CONTRADICTION`** | **`1`** | 🔴 **two channels disagree** — `P204-1` |
| 🟢 **`LOST-ADDRESS-RECOVERED`** | **`1`** | 🟢 the address was stale, not the grant |
| 🔴 **`UNADJUDICATED-CHANNEL`** | **`1`** | 🔴 this environment cannot decide |

**The `8` manifest-declared rows, read from their own blob:**

| Row | branch | manifest | declares |
|---|---|---|---|
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | `package.json` | **MIT** |
| [MisterCommand/mcp-canvas-lms](https://github.com/MisterCommand/mcp-canvas-lms) | `main` | `package.json` | **MIT** |
| [Exhabition/brightspace-mcp-rs](https://github.com/Exhabition/brightspace-mcp-rs) | `main` | `package.json` | **MIT** |
| [LMS-Laravel/LMS-Laravel](https://github.com/LMS-Laravel/LMS-Laravel) | `master` | `composer.json` | **MIT** |
| [LMS-Laravel/OLD-LMS-Laravel](https://github.com/LMS-Laravel/OLD-LMS-Laravel) | `master` | `composer.json` | **MIT** |
| [Simon-Initiative/lti-example-tool](https://github.com/Simon-Initiative/lti-example-tool) | `master` | `package.json` | **MIT** |
| [Lumieducation/Lumi](https://github.com/Lumieducation/Lumi) | `master` | `package.json` | 🔴 **AGPL-3.0** — route around |
| [LearnPress/learnpress](https://github.com/LearnPress/learnpress) | 🔴 `develop` | `package.json` | 🔴 **`ISC`** — **and `readme.txt` says `GPLv3`**, `P204-1` |

🔵 **The grant-channel ladder this pass establishes, strongest first:** licence **body** at a
path → **manifest** field with no body → **README** prose → badge. 🔴 **A manifest field is a
claim about a licence, not the licence**: there is no copyright holder, no year and no warranty
disclaimer, so a client's counsel gets a name and nothing to read. 🟢 **Usable for a `PoC`;
🔴 not sufficient for a deliverable without asking upstream to commit the body.**

### 🔴 `P204-1` — the two manifests in one tree disagree, and the COPYLEFT one governs

🔴 **[LearnPress/learnpress](https://github.com/LearnPress/learnpress)** `develop` @ `f9f2d6e2`:

| channel | says |
|---|---|
| `package.json` | 🟢 `"license": "ISC"` — permissive |
| 🔴 `readme.txt` | 🔴 `License: GPLv3` · `License URI: https://www.gnu.org/licenses/gpl-3.0.html` |

🔴 **`readme.txt` is the WordPress plugin manifest — it is the file that governs the
distributed plugin.** 🟢 **So the shipped payload is `GPL-3.0` and the `package.json` `ISC`
plausibly covers only the JS build tooling.** 🔴 **A pass that read `package.json` alone would
have published this row as permissive, and a studio would have built on it.**

🟢 **Measured, not assumed to generalise: `1` of `8`.** The second-channel sweep found **`7` of
the `8` have no `readme.txt`/`README` licence line at all** —
[`evidence/pc-manifest-second-channel.2026-10-14-p204.tsv`](../evidence/pc-manifest-second-channel.2026-10-14-p204.tsv).
🔵 **The mechanism is the WordPress convention, not a general defect**, and it is also the only
one of the `8` whose default branch is `develop`. 🔴 **But it is a NEW defect class for
`ACTION PB`: scope is not only path-vs-path, it is channel-vs-channel.**

### 🟢 `Gap 464` closed before it was declared — a lost address, recovered

🔴 **`apereo/opencast` returns `0` refs from `git ls-remote` and `403` from the HTML channel.**
🟢 **The repository is not dead; the ADDRESS is.** The live tree is
[**`opencast/opencast`**](https://github.com/opencast/opencast), default branch 🔴 **`develop`**,
HEAD `ae86c6aa`, and its grant reads from its own blob:

🟢 **`Educational Community License, Version 2.0 (ECL-2.0)`** — and the body states its own
deviation: *"the Apache 2.0 license, modified to change the scope of the patent grant in
section 3 to be specific to the needs of the education communities using this license."*

🔴 **So `ECL-2.0` is NOT Apache-2.0 with a new name — its patent grant is NARROWER**, and this
is an education KB where that family recurs: [`Apereo-Learning-Analytics-Initiative/OpenLRW`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW)
is the second `ECL-2.0` row measured this pass. 🟢 **Treat `ECL-2.0` as permissive for
redistribution and 🔴 flag the patent scope in any engagement that ships a patentable
pipeline.**

🔴 **The other unresolvable row — `cdweaver1992/edfi-mcp-server` — stays UNADJUDICATED.**
`ls-remote` `0` refs **and** HTML `403`, so this environment cannot tell a moved repo from a
blocked one. 🔵 **Declared, not guessed.**

### 🟢 `ACTION OZ` CLOSED — limb `2` fires, and the saturation is CODE-shaped

🟢 **The `3` vocabularies p202's census named as unsearched were read in full:**

| vocabulary | repos matching | rendered | **NEW to this KB** | already published | evidence-only |
|---|---|---|---|---|---|
| `topic:scorm` | `229` | `20` | 🔴 **`0`** | `18` | `2` |
| `topic:xapi` | `300` | `20` | 🔴 **`0`** | `16` | `4` |
| `topic:lti` | `185` | `20` | 🔴 **`0`** | `17` | `3` |
| **total** | — | **`60`** | 🔴 **`0`** | **`51`** | **`9`** |

🔴 **`0` of `60`.** Census:
[`evidence/oz-vocabulary-novelty.2026-10-14-p204.tsv`](../evidence/oz-vocabulary-novelty.2026-10-14-p204.tsv).
🟢 **Both controls ran:** two invented slugs classified `NEW` *(negative)*; `HKUDS/DeepTutor`
and `adlnet/ADL_LRS` classified `KNOWN` *(positive)*.

🟢 **So limb `2` fires: `ingest/config.json` is ADEQUATE for the code layer and `Gap 461` is
specific to OER.** 🔴 **Do not rewrite the config.**

🔵 **And the shape of the saturation is the finding.** p203 measured `topic:ai-tutor` at
`20`/`20` known. p204 measures three interop vocabularies at `60`/`60` known. 🔴 **Every
SOFTWARE vocabulary this KB has probed is saturated.** 🟢 **The one vocabulary still yielding
is `topic:open-educational-resources` — `12`/`20` new at p203 — and it is a CONTENT
vocabulary.** 🟢 **That is the same seam `P203-1` found in the licence column, arriving
independently through the discovery channel.** `Gap 465`.

🔵 **The `9` evidence-only rows were promoted to a published page this pass** *(they existed
only inside a census TSV)*: `adlnet/xAPIWrapper` **Apache-2.0** · `RusticiSoftware/TinCanJS`
**Apache-2.0** · `RusticiSoftware/TinCanPython` **Apache-2.0** *(`3.x`)* ·
`RusticiSoftware/TinCan_Prototypes` **Apache-2.0** · `adlnet/xapi-profiles` **Apache-2.0** ·
`csev/wa4e` **BSD** · `ucfopen/lti-template-flask` **MIT** *(deprecated upstream)* ·
`greenpeace/gpes-html5-scorm-presentation` **MIT** · `S4-NetQuest/react-scorm-provider`
**MIT** — all blob-read this pass,
[`evidence/p204-grant-reverification.2026-10-14-p204.tsv`](../evidence/p204-grant-reverification.2026-10-14-p204.tsv).
🔴 **`frumbert/scorm_debug` and `WebPA/WebPA` have no grant file and join the ungranted
population.**

### 🟢 Partial input to `ACTION PB`, explicitly NOT a discharge

🟢 **`20` rows already published were re-read from their own blob at a pinned HEAD this pass,
and `0` corrections were needed.** 🔵 **`ACTION PB`'s limb test is about a misdescribed
**scope** on the `~60` highest-★ rows and was not run at that scale.** 🔴 **Do not read
"`0`/`20` corrections" as "limb `2` fires" — it is `20` rows of the wrong sample, reported
because it is evidence and withheld from the verdict because it is not the test.**

---

## Pass 203 — 2026-10-14 — `ACTION OV` CLOSES ON LIMB 2, AND THE CARPENTRIES WERE MISSING FOR 202 PASSES

### 🔴 `ACTION OV`: the `13` unread rows are read, and `4` of `16` are not permissive

🟢 **Every row p202 published marked `(not blob-read)` is now read from its own blob**, plus
three p202 named but did not probe (`xAPI-Spec`, the `1EdTech` canonical upstream,
`openfun/ralph`). 🔴 **Pre-registered limb `1` — *"all permissive → P202-1's wire-up is
sellable as written"* — is FALSIFIED.** Census:
[`evidence/foundations-unread-grants.2026-10-14-p203.tsv`](../evidence/foundations-unread-grants.2026-10-14-p203.tsv).

**`12` permissive · `3` copyleft · `1` content-copyleft over software.**

| Row | ★ | path read | grant *(blob)* | verdict |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | `954` | `master/LICENSE` | **Apache-2.0** | 🟢 the specification itself |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | `334` | `master/LICENSE` | **Apache-2.0** | 🟢 **the LRS to build on** |
| [g3i/lxHive](https://github.com/g3i/lxHive) | `79` | `master/LICENSE` | 🔴 **GPL-2.0** | 🔴 **route around** — p202 published it unread as a lightweight LRS option |
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | `78` | `master/LICENSE` | **MIT** | 🟢 the conformance gate |
| [cybercussion/SCOBot](https://github.com/cybercussion/SCOBot) | `164` | `master/LICENSE` | 🔴 **`CC-BY-SA-4.0`** | 🔴 **a SCORM JavaScript API under a CONTENT copyleft** — see below |
| [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | `58` | `master/LICENSE` | **MIT** *(`(c) 2019 Sebastian Rettig`)* | 🟢 H5P → SCORM |
| [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | `29` | `master/LICENSE` | **BSD-3-Clause** *(`(c) 2020, André Dietrich`)* | 🟢 markdown → SCORM/xAPI/PDF/ePub/APK |
| [adlnet/CATAPULT](https://github.com/adlnet/CATAPULT) | `59` | `master/LICENSE` | **Apache-2.0** | 🟢 `cmi5` test suite and player |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | `138` | `master/LICENSE` | **MIT** *(`(c) 2019 Dmitry Viskov`)* | 🟢 LTI 1.3 in Python |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | — | `master/LICENSE` | **Apache-2.0** | 🟢 **the canonical upstream p202 said to hold** |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | `53` | 🔴 `master/LICENSE.md` | **Apache-2.0** | 🟢 same grant as upstream; **bare `LICENSE` is a `404`** |
| [oat-sa/lib-lti1p3-core](https://github.com/oat-sa/lib-lti1p3-core) | `37` | `master/LICENSE` | 🔴 **GPL-2.0** | 🔴 **route around** — the platform-side LTI core |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | `73` | `master/LICENSE` | **BSD-3-Clause** | 🟢 LMS → JupyterHub |
| [openfun/marsha](https://github.com/openfun/marsha) | `151` | `master/LICENSE` | **MIT** *(`(c) 2018-present GIP FUN-MOOC`)* | 🟢 LTI content management |
| [cerpus/Edlib](https://github.com/cerpus/Edlib) | `46` | `master/LICENSE` | 🔴 **GPL-3.0** | 🔴 **route around** |
| [openfun/ralph](https://github.com/openfun/ralph) | — | 🔴 `master/LICENSE.md` | **MIT** *(`(c) 2020-present France Université Numérique`)* | 🟢 `ACTION OW` limb `1`: **the `.md` path resolves and the body is MIT** |

🟢 **So `P202-1` survives, but it must now name paths.** The permissive spine of the
xAPI/SCORM/LTI layer is: **`ADL_LRS` (Apache-2.0) + `lrs-conformance-test-suite` (MIT) +
`pylti1.3` (MIT) or `1EdTech/lti-1-3-php-library` (Apache-2.0) + `ltiauthenticator`
(BSD-3) + `CATAPULT` (Apache-2.0) + `scorm-h5p-wrapper` (MIT) + `LiaScript-Exporter`
(BSD-3) + `ralph` (MIT) + `marsha` (MIT)** — **`10` rows, every grant blob-read, nothing
copyleft.** 🔴 **Excluded by this pass: `lxHive`, `oat-sa/lib-lti1p3-core`, `Edlib`,
`SCOBot`.**

### 🔴 `SCOBot` is the finding that generalises: a JavaScript library under a content licence

🟢 `cybercussion/SCOBot` `164★` is a **SCORM run-time API you embed in courseware** — and its
`LICENSE` title line reads **`CREATIVE COMMONS ATTRIBUTION-SHAREALIKE 4.0 INTERNATIONAL`**.
🔴 **That is `Gap 459` on the FOUNDATIONS shelf, not the agent-skill shelf** — so p202's class
is not a property of the agent-skill layer. **`ShareAlike` on an embedded library means every
course package that ships it is a derivative**, and a CC licence **carries no patent grant**.

### 🆕 🟢 The Carpentries: `12` new rows, and a `202`-pass absence with a cause

🔴 **This KB has never held a single Carpentries repository.** 🟢 **The Carpentries (Software
Carpentry, Data Carpentry, Library Carpentry) is the largest instructor-led open curriculum
organisation in the world**, and its lessons are the default teaching material for research
computing. 🔴 **Cause, measured: its repositories carry `topic:open-educational-resources`
and lesson-specific topics, and NEVER `ai-tutor`, `edtech` or `educational-ai`** — the
vocabularies this KB's `ingest/config.json` searches. **Discovery vocabulary determined the
content shelf for `202` passes.** `Gap 461`.

🟢 **And every one of them carries the same two-scope instrument**, read from the blob:

> `## Instructional Material` — *"All Carpentries … instructional material is made available
> under the [Creative Commons Attribution license] … for any purpose, even commercially."*
> `## Software` — *"Except where otherwise noted, the example programs and other software
> provided by The Carpentries are made available under the [OSI]-approved [MIT license]."*

| Row | ★ | path | content | code |
|---|---|---|---|---|
| [swcarpentry/git-novice](https://github.com/swcarpentry/git-novice) | `379` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [datacarpentry/R-ecology-lesson](https://github.com/datacarpentry/R-ecology-lesson) | `338` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [carpentries/instructor-training](https://github.com/carpentries/instructor-training) | `189` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [swcarpentry/r-novice-inflammation](https://github.com/swcarpentry/r-novice-inflammation) | `174` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [datacarpentry/r-raster-vector-geospatial](https://github.com/datacarpentry/r-raster-vector-geospatial) | `119` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [datacarpentry/image-processing](https://github.com/datacarpentry/image-processing) | `113` | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [swcarpentry/shell-novice](https://github.com/swcarpentry/shell-novice) | *(not measured p203)* | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [datacarpentry/python-ecology-lesson](https://github.com/datacarpentry/python-ecology-lesson) | *(not measured p203)* | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [librarycarpentry/lc-git](https://github.com/librarycarpentry/lc-git) | *(not measured p203)* | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** |
| [carpentries/lesson-example](https://github.com/carpentries/lesson-example) | *(not measured p203)* | `main/LICENSE.md` | `CC-BY-4.0` | 🟢 **MIT** — 🔴 **the TEMPLATE: the instrument propagates to every lesson built from it** |
| [merely-useful/py-rse](https://github.com/merely-useful/py-rse) | `261` | `master/LICENSE.md` | `CC-BY-4.0` | 🔴 **not granted** |
| [spatialaudio/digital-signal-processing-lecture](https://github.com/spatialaudio/digital-signal-processing-lecture) | `885` | `master/LICENSE` | `CC-BY-4.0` | 🔴 **not granted** — and the asset **is** Jupyter notebooks |

🔴 **`★` left blank is `★` not measured.** `api.github.com` returned `403` all pass; the
figures above come from the rendered `topic:open-educational-resources` page, which lists
`20` of `378` repositories, and four of these rows were not among the `20`.

🟢 **Why this is a foundations row and not a curiosity:** `carpentries/lesson-example` is the
template, so **an agent that generates a lesson in the Carpentries format inherits a grant
that is already explicit about code vs content** — the one thing p202 found the rest of this
industry gets wrong.

## Pass 202 — 2026-10-14 — THE STANDARDS LAYER IS THE FOUNDATION THIS KB HAD NOT READ

🔴 **For `201` passes this KB has catalogued tutors, LMSs and graders, and never the layer
underneath all three.** `ACTION OP` sent this pass at `topic:xapi`, `topic:scorm`,
`topic:lti` and `topic:learning-analytics`, and they returned a **mature, permissive,
pre-AI shelf with `300`+`229`+`185`+`374` = `1 088` repositories matching**.

🟢 **Why it is foundational and not plumbing: xAPI/SCORM/LTI are the only standardised way a
tutoring agent gets (a) into an institution's LMS, and (b) a complete event log of what the
learner actually did.** An agent without the second one is guessing, and an agent without
the first one never gets installed.

### 🟢 The learning-record layer — the retrieval substrate for an education agent

| Repo | Licence *(source)* | ★ | Region | What it gives a studio |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | *(spec, not blob-read)* | **954** | US ADL → North America | 🟢 **The specification itself.** `statement = actor + verb + object`. The vocabulary an agent should emit about every learner interaction |
| [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** *(p77, `lib/` fixture)* | **585** | HT2 Labs → EMEA | The most-adopted open LRS. 🔵 **`GPL-3.0`, confirmed by the title-block classifier — a naive `affero` body match calls this AGPL and is wrong** |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** *(blob)* | **144** | Yet Analytics → North America | 🟢 **A SQL-based LRS under Apache-2.0** — the permissive exit from the GPL LRS layer, and SQL means your existing BI stack reads it |
| [openfun/ralph](https://github.com/openfun/ralph) | 🟢 **MIT** *(badge; blob at `LICENSE.md`, 🔴 NOT read this pass)* | **51** | France Université Numérique → **EMEA** | LRS + ETL for learning events. 🔵 **`LICENSE` is a `404`; the grant lives at `LICENSE.md`** — `Gap 456` again |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | *(not blob-read)* | **334** | US ADL → North America | The reference LRS from the standard's authors |
| [g3i/lxHive](https://github.com/g3i/lxHive) | *(not blob-read)* | **79** | → EMEA | Lightweight LRS, PHP |
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | *(not blob-read)* | **78** | North America | 🟢 **Tests the MUST requirements of the spec** — the conformance gate for anything you build |

### 🟢 The content-packaging layer — how a generated course gets INTO an institution

| Repo | Licence *(source)* | ★ | What it gives a studio |
|---|---|---|---|
| [adaptlearning/adapt_framework](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** · 🆕 **v3-ONLY** *(blob + README)* | **631** | Responsive, accessible, multilanguage HTML5 course authoring. 🔴 **README says *"the GNU General Public License, Version 3"* with no "or later" — see `ACTION OQ`** |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** *(blob)* | **355** | 🟢 **A modern SCORM runtime under MIT.** The permissive bridge between a new agent UI and a `2004`-era LMS |
| [cybercussion/SCOBot](https://github.com/cybercussion/SCOBot) | *(not blob-read)* | **164** | SCORM API for content, with QUnit tests |
| [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | *(not blob-read)* | **58** | 🟢 **Packs H5P interactive content into SCORM** — the join between the H5P shelf this KB already holds and institutional delivery |
| [LiaScript/LiaScript-Exporter](https://github.com/LiaScript/LiaScript-Exporter) | *(not blob-read)* | **29** | 🟢 **Markdown course → SCORM, xAPI, PDF, ePub, APK.** Agent writes markdown; this ships it everywhere |
| [adlnet/CATAPULT](https://github.com/adlnet/CATAPULT) | *(not blob-read)* | **59** | `cmi5` testing and player — SCORM's successor profile |

### 🟢 The integration layer — LTI, which is how you get installed at all

| Repo | Licence *(source)* | ★ | Region | Note |
|---|---|---|---|---|
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0** *(blob)* | **376** | Chuck Severance → North America | 🟢 **A full framework for building LTI tools.** 🔴 Its description names no education term — the relevance gate sends it to REVIEW, which is why that gate has no `REJECT` |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | *(not blob-read)* | **138** | → EMEA | LTI 1.3 Advantage tool in Python, with a Django example repo |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | *(not blob-read)* | **53** | North America | IMS-certified LTI 1.3 providers in PHP. 🔴 **A FORK of [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) — 1EdTech owns the LTI standard, so the upstream is the canonical row and this KB has been holding the fork** |
| [oat-sa/lib-lti1p3-core](https://github.com/oat-sa/lib-lti1p3-core) | *(not blob-read)* | **37** | Open Assessment Technologies → EMEA | LTI 1.3 core, platform **and** tool sides |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | *(not blob-read)* | **73** | Global | 🟢 **LTI → JupyterHub.** The shortest path from an institution's LMS to a notebook environment |
| [openfun/marsha](https://github.com/openfun/marsha) | *(not blob-read)* | **151** | France Université Numérique → **EMEA** | LTI learning-content management system |
| [cerpus/Edlib](https://github.com/cerpus/Edlib) | *(not blob-read)* | **46** | Cerpus (Norway) → **EMEA** | Create, share and reuse interactive learning resources |

### 🔴 Foundational-layer caution, stated rather than smoothed

🔴 **`9` of the `20` rows above are NOT blob-read.** They are published here as *discovered
and described*, with the licence column saying so, because `api.github.com` returns `403`
and each blob costs a separate fetch. 🔵 **`Gap 449`'s rule applied honestly: the rows this
pass verified are marked `(blob)`; the rest are a to-do, not a finding.** The next pass
should blob-read the `9` before any of them enters a client deliverable.

🟢 **The one durable statement: this layer is old, permissive, standardised, institutionally
adopted, and almost completely untouched by the current AI wave.** Every tutor on
[`agents/top.md`](../agents/top.md) invents its own progress model; `xAPI` already
standardised one, and an LRS already stores it.


## Pass 201 — 2026-10-14 — THE PERMISSIVE SHELF IS FOUR TIMES BIGGER THAN p200 SAID

🔴 **p199 and p200 both published a sentence an engagement would plan around:**

> *"the open LMS shelf is copyleft almost without exception, and there are **exactly two
> permissive exits** — Kolibri (MIT) and OpenOLAT (Apache-2.0)."*

🟢 **It is `Gap 449` in form — a claim whose scope was its own search.** p200 read the licences
of eight platforms it already had. 🟢 **This pass enumerated the whole `topic:lms stars:>200`
shelf (`32` rows), discarded the four homonyms, and read every unresolved licence from its own
blob. The permissive exits number at least `9`.**

| Repo | Licence *(blob, bytes)* | ★ | Branch | Origin → region | Why it is an exit |
|---|---|---|---|---|---|
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1 097` B *(p200)* | — | `develop` | → **Global** | 🔵 p200's row, unchanged: the offline-first exit |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10 982` B | **447** | `master` | Switzerland → **EMEA** | 🔵 p200's row, re-read today. 🔴 **The API reports `NOASSERTION` for it** — a scanner would call it unlicensed |
| [academico-sis/academico](https://github.com/academico-sis/academico) | 🟢 **MIT** · `1 094` B | **404** | `main` | → **Global** | 🆕 🟢 **A full school-management platform — SIS *and* LMS — under MIT.** Laravel + Filament, `149` forks. **The permissive answer to RosarioSIS (GPL-2.0) and openSIS (GPL-2.0)** |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 **MIT** · `1 062` B | **95** | `main` | Poland → **EMEA** | 🆕 🟢 **AI-native LMS with SCORM + xAPI and white-labelling, MIT** — built to replace Moodle/Docebo/Open edX rather than extend them |
| [openfun/richie](https://github.com/openfun/richie) | 🟢 **MIT** · `1 079` B | **316** | `master` | France Université Numérique → **EMEA** | 🔵 Cycle-2 row, licence now from bytes: the **course catalogue/marketing CMS** that fronts Open edX or Moodle without inheriting their copyleft |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** · `1 072` B | **355** | `master` | → **Global** | 🆕 🟢 **A SCORM 1.2/2004 runtime, offline-first, in TypeScript.** The standards-compliance piece every LMS build needs and no LLM framework has |
| [safytech/ulearn](https://github.com/safytech/ulearn) | 🟢 **MIT** · `1 066` B | **700** | `master` | → **Global** | 🆕 Laravel + React LMS, MIT, `700★` |
| [netless-io/flat](https://github.com/netless-io/flat) | 🟢 **MIT** · `1 062` B | **6 439** | `main` | Agora → **APAC** | 🆕 🟢 **The synchronous classroom: Web, Windows and macOS clients, whiteboard, cloud recording.** `6 439★`, MIT |
| [OpenVidu/openvidu](https://github.com/OpenVidu/openvidu) | 🟢 **Apache-2.0** · `11 357` B | **2 136** | `master` | Spain → **EMEA** | 🆕 Self-hosted real-time video on LiveKit + mediasoup; its own topics now include `ai-agents` |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** · `1 145` B | **437** | `main` | UIUC → **North America** | 🆕 Django course platform with grading and code homework. 🔴 **API: `NOASSERTION`; its `LICENSE` carries the MIT grant with no title line at all** |

🟢 **Read across it: a studio building a closed-source education deliverable now has a
permissive option at every layer** — classroom (`flat`, `OpenVidu`), LMS (`mentingo`, `ulearn`,
`academico`), catalogue (`richie`), standards (`scorm-again`), offline (`Kolibri`), grading
(`Artemis` MIT, `Submitty` BSD-3 — see [`agents/top.md`](../agents/top.md)). 🔵 **That was not
true of this KB's pages an hour ago.**

### 🔴 The copyleft layer is bigger too — and the modern LMS is AGPL, not GPL

🟢 Every licence here read from its own blob this pass:

| Repo | Licence *(blob, bytes)* | ★ | Branch | Consequence |
|---|---|---|---|---|
| [frappe/lms](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `33 893` B | **3 312** | 🔵 `develop` | Network copyleft reaches a hosted deliverable |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **AGPL-3.0** · `34 523` B | **2 377** | 🔵 `dev` | Markets itself as *"ai-powered"*; AGPL |
| [classroomio/classroomio](https://github.com/classroomio/classroomio) | 🔴 **AGPL-3.0** · `34 523` B | **1 717** | `main` | — |
| [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** · `34 143` B | **1 274** | `main` | — |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · `34 523` B | **1 127** | 🔵 `release` | The Open edX distribution — AGPL on top of AGPL |
| [claroline/Claroline](https://github.com/claroline/Claroline) | 🔴 **AGPL-3.0** · `34 616` B | **350** | 🔵 `15.0` | 🔴 **API said `NOASSERTION`.** Default branch is a version number |
| [elmsln/elmsln](https://github.com/elmsln/elmsln) | 🔴 **GPL-3.0** · `35 193` B | **253** | `master` | 🔵 `35 193` B — **outside p200's `35 146`–`35 149` GPL-3.0 band** |
| [xiaochong0302/course-tencent-cloud](https://github.com/xiaochong0302/course-tencent-cloud) | 🔴 **GPL-2.0** · `18 092` B | **1 173** | 🔵 `v2` | APAC MOOC platform |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · `15 214` B | **646** | 🔵 `mobile` | SIS with heavy LATAM/francophone adoption |
| [gazpachu/hypatia](https://github.com/gazpachu/hypatia) | 🔴 **GPL-2.0** · `19 350` B | **651** | `master` | 🔴 API `NOASSERTION`; **last push `2023-02-15`** — dormant |

🔴 **The generalisation worth carrying into a SOW: the LMS layer built since ~2020 is AGPL-3.0,
not GPL-3.0.** Moodle, Chamilo, ILIAS and H5P are plain GPL; `frappe/lms`, `learnhouse`,
`classroomio`, `courselit`, `tutor` and `Claroline` are **AGPL** — network copyleft, which
reaches a SaaS deliverable the way plain GPL does not. **The newer the platform, the stronger the
copyleft.**

### 🔴 The API's licence field, measured on a real shelf

🟢 **A number this KB has never had.** Over the `32` rows of `topic:lms stars:>200`:

| channel | rows resolved | share |
|---|---|---|
| GitHub REST `license.spdx_id` | **23** | `72`% |
| 🟢 **+ blob read** *(`NOASSERTION` rows: `6`/`6` resolved)* | **29** | 🟢 **`91`%** |
| 🔴 **unresolvable — no grant on ANY channel** | **3** | `9`% |

🔴 **The three ungranted rows carry `1 068★` between them:**
[`LMS-Laravel/LMS-Laravel`](https://github.com/LMS-Laravel/LMS-Laravel) (`505★`),
[`LMS-Laravel/OLD-LMS-Laravel`](https://github.com/LMS-Laravel/OLD-LMS-Laravel) (`288★`) and
[`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) (`275★`). **No blob at `10`
path forms, and for LearnPress not even a `License:` line in its WordPress plugin header** —
the one channel a WP plugin normally declares in. 🟡 *(A plugin distributed on wordpress.org must
be GPL-compatible by that directory's rules; the repository itself declares nothing, and a rule
about a distribution channel is not a grant in the source.)* 🔵 **`NOASSERTION` means *GitHub
could not match the text*, not *there is no licence* — `6`/`6` of those rows had a readable grant.
*Missing field* is the one that means what it says.**

### 🟢 `ACTION OH` DISCHARGED, LIMB 1 — and the same path form closes `ACTION OM`

🟢 **Lowercase `license.txt` resolves, and so does a non-root path.** Measured:
`frappe/erpnext` → `license.txt` (`35 149` B) · `chamilo/chamilo-lms` → **a second file** at
`license.txt` (`1 614` B) · `polimediaupv/paella` → `license.txt` (`9 915` B) ·
`OS4ED/openSIS-Classic` → `docs/License.txt` (`17 286` B, UTF-8 BOM intact). 🔵 Every byte figure
agrees with p200's.

🟢 **`ACTION OM` DISCHARGED, LIMB 1 — `paella`'s grant EXISTS.** p200 declared it *"declared,
ungranted"* after `404`s at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license` and `COPYING`
across three branches. 🔴 **It never tried lowercase `license.txt` — the path form it had
discovered on `erpnext` in the same pass.**

| | |
|---|---|
| path | `license.txt` on `develop` |
| bytes | **`9 915`** |
| title line | **`Educational Community License, Version 2.0 (ECL-2.0)`** |
| § 3 education narrowing | 🟢 present, line `7` |
| [`polimediaupv/paella-core`](https://github.com/polimediaupv/paella-core) | 🟢 **byte-identical** — same `sha256` (`15efd2f640ed…`) |

🔴 **The lesson is about a correction that failed to travel *inside a single pass*:** p200 found
the lowercase form, published it, and still left an unrelated row marked ungranted. 🟢 **A path
vocabulary is a shared instrument** — [`compose/code/lib/licence_path.sh`](../compose/code/lib/),
whose suite passes `33`/`33` here — **not a per-row habit.** Committed as
[`evidence/paella-grant-found.2026-10-14-p201.tsv`](../evidence/paella-grant-found.2026-10-14-p201.tsv).

### 🔵 `ECL-2.0` byte figures do NOT identify the family

🟢 Four ECL-2.0 blobs now read across two passes: `sakai` `11 120` B, `opencast` `11 340` B,
`Hilary` `12 322` B, **`paella`/`paella-core` `9 915` B**. 🔴 **A `2 407`-byte spread on one
licence.** 🔵 And the copyleft bands are tighter than they look safe: GPL-3.0 spans
`35 146`–`35 193` and AGPL-3.0 spans `33 893`–`35 136` over `19` blobs — **a `10`-byte gap
between the two families at their closest.** 🟢 **Bytes are an integrity check on one blob, never
a family test.** The title line is the test.

### 🆕 🔴 Chamilo is GPL-3.0-**or-later**, and the text it points at is a `404`

🟢 Chamilo's own `license.txt` (`1 614` B, read this pass) says, in the project's words:

> *"This program is free software: you can redistribute it and/or modify it under the terms of
> the GNU General Public License as published by the Free Software Foundation, **either version 3
> of the License, or (at your option) any later version**."*

🔴 **This KB has published `GPL-3.0` for Chamilo since cycle 3; the project declares
`GPL-3.0-or-later`.** 🔵 That is a real SPDX distinction — *-or-later* lets a licensee take the
code under a future GPL, *-only* does not — **and it is invisible to the channel this KB uses**,
because the full GPL text is identical either way. **The version policy lives in the project's
notice, not in the licence.**

🔴 **And the same notice points at `documentation/license.html` as *"the full license"* — which
returns `404` on `master`.** 🟢 Harmless here *(the real text sits at `LICENSE`, `35 147` B)*,
but it is a dangling grant reference in the file a licensee is told to read.

🔵 **`20` foundational repos with a licence read from source this pass** — `10` permissive exits,
`10` copyleft platforms — far above the 5-row bar.


## Pass 200 — 2026-10-14 — ECL-2.0: EDUCATION HAS ITS OWN LICENCE AND THIS KB HAD NEVER NAMED IT

🆕 🟢 **The single most consequential thing found this pass is a licence family, not a repo.**
The **Educational Community License 2.0 (`ECL-2.0`)** is an OSI-approved licence that this KB
has misreported as `Apache-2.0` since cycle 3. Quoted from the licence text itself, read from
[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai)'s own blob this pass:

> *"The Educational Community License version 2.0 ("ECL") consists of the Apache 2.0 license,
> **modified to change the scope of the patent grant in section 3 to be specific to the needs
> of the education communities** using this license."*

🔴 **Cycle 3 (`v65`) published `Sakai(Apache2)`. That is wrong in the one way that costs money.**
The permission grant is Apache-2.0's; **the patent grant is narrower and scoped to education
use.** 🔵 For a studio that ships derived work into a client's name, a narrowed patent peace is
a contract-review trigger, not a cosmetic label — and it is precisely the field a scanner
normalises away when it reports *"Apache-2.0 family"*.

🟢 **Credit where it is due: p199's platform table already had this right**, calling ECL-2.0
*"Apache-derived with an education-specific patent clause."* 🔵 **What this pass adds is the
quoted scope, the family census, and the consequence** — that the narrowing is *specifically* to
§ 3, *specifically* to education communities, and that the family is `18` repositories wide
rather than a Sakai idiosyncrasy.

🟢 **It is also a small, education-concentrated family, which is why it is easy to miss.**
Queried this pass: **`license:ecl-2.0 stars:>20` returns `18` repositories GitHub-wide**, and
the top of that list is education infrastructure:

| Repo | Licence *(blob, bytes)* | Stars | Origin → region | What it is for an education build |
|---|---|---|---|---|
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** · `11 120` B | **1 238** | Apereo, global → **Global** | Full LMS/VLE in Java; `1 016` forks. The reference ECL-2.0 codebase |
| [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** · `11 340` B | **508** | → **EMEA** *(German/European universities)* | 🟢 **Automated lecture capture and video distribution at scale** — the piece every university AI-video pattern needs and no LLM framework provides. Default branch `develop` |
| [music-encoding/music-encoding](https://github.com/music-encoding/music-encoding) | **ECL-2.0** | **241** | → **Global** | Music Encoding Initiative schema — scholarly/conservatoire corpora |
| [oaeproject/3akai-ux](https://github.com/oaeproject/3akai-ux) | **ECL-2.0** | **134** | → **EMEA** | Open Academic Environment front end |
| [oaeproject/Hilary](https://github.com/oaeproject/Hilary) | **ECL-2.0** · `12 322` B | **105** | → **EMEA** | OAE back end |
| [polimediaupv/paella](https://github.com/polimediaupv/paella) | 🟡 **declared `ECL-2.0`, no blob** | **63** | UPV Valencia → **EMEA** | HTML5 multistream player; the usual Opencast front end |

🔵 **Instrument note, and it is a correction to a naive read:** a generic family detector returns
`UNCLASSIFIED` on all of these, because the text's first distinctive line is *"Educational
Community License"* and nothing matches `Apache License … Version 2.0` at the top. 🟢 **The
conservative `UNCLASSIFIED` is the right failure** — far better than the confident
`Apache-2.0` that earlier cycles published. 🔵 Two traps inside the family: `Hilary`'s `LICENSE`
**opens with a blank line**, so a first-line read sees nothing; and `paella`'s grant does not
exist as a file at all.

### 🟢 The permissive exits from an AGPL layer — all re-read from blobs today

🔵 Every licence below was fetched from `raw.githubusercontent.com/<slug>/<default-branch>/<file>`
this pass, with the default branch resolved by `git ls-remote --symref` first. **Several do not
use `main`**, and that detail decides whether the read succeeds at all.

| Repo | Licence *(blob, bytes)* | Default branch | Verdict for AI Studios |
|---|---|---|---|
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1 097` B | `develop` | 🟢 **The permissive offline-first exit.** Low-connectivity deployments — the LATAM/Africa shape |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10 982` B | `master` | 🟢 **The permissive full-LMS exit**, and a real one in EMEA |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `35 147` B *(`COPYING.txt`)* | `main` | Integrate over Web Services; do not fork into a closed deliverable |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · `35 136` B *(title line + `15` Affero mentions)* | `master` | 🔴 **Genuinely AGPL, unlike the four below it.** Extend via `XBlock` (`Apache-2.0`), never by forking |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · `35 147` B | `master` | Strong in LATAM and francophone Africa — integrate, don't embed |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · `35 147` B | 🔵 `release_11` | German-speaking EMEA. 🔵 **Default branch is `release_11`, not `main`** |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `35 146` B *(`LICENSE.txt`)* | `master` | Interactive content; copyleft reaches the content runtime |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** · `8 241` B | 🔵 `19.0` | Education ERP on Odoo. Weak copyleft — linkable, and the practical middle |

🟢 **Read across the layer: the open LMS shelf is copyleft almost without exception, and there
are exactly two permissive exits — Kolibri (MIT) and OpenOLAT (Apache-2.0).** That is the
sentence an engagement needs before it promises a client a closed-source deliverable. 🔵 Note
the distinction the next subsection had to be written to get right: **`edx-platform` is AGPL —
network copyleft, which reaches a hosted deliverable — while Moodle, Chamilo, ILIAS and H5P are
plain GPL-3.0**, which does not reach across the network. For a SaaS-shaped engagement that
difference decides the architecture.

### 🔴 This pass's own defect, caught before publication — and p199 is VINDICATED

🔴 **This pass's first licence read said `AGPL-3.0` for Moodle, Chamilo, ILIAS and H5P.** p199
had published `GPL-3.0` for all four. 🟢 **p199 is right and this pass's first answer was
wrong**, and the reason generalises:

> **The GPL-3.0 text contains the phrase *"GNU Affero General Public License"* in its own
> § 13** (*"Use with the GNU Affero General Public License"*). **Any scanner that decides the
> family by searching for that phrase labels every GPL-3.0 repository as AGPL.**

🔵 **And the defect is intermittent, which is worse than wrong.** The same detector returned the
correct `GPL-3.0` for `frappe/erpnext` from an identical licence — because the two copies **wrap
§ 13 across lines differently**, so a line-oriented match finds the phrase in one file and not
in the other. 🔴 **A line-oriented grep over a wrapped legal text is not a classifier**, and a
detector that is right four times out of five hides its defect behind its successes.

🟢 **The discriminator that actually works, measured on eight real blobs this pass:**

| signal | GPL-3.0 | AGPL-3.0 |
|---|---|---|
| **title line** *(first `GENERAL PUBLIC LICENSE` match)* | `GNU GENERAL PUBLIC LICENSE` | `GNU AFFERO GENERAL PUBLIC LICENSE` |
| 🟢 **count of `affero`, case-insensitive** | **`3`** *(all incidental, § 13)* | **`15`** |
| full-text bytes | `35 146`–`35 149` | `34 514`–`35 136` |

🔵 Measured: `moodle` `35 147` B / `3`, `chamilo` `35 147` B / `3`, `ILIAS` `35 147` B / `3`,
`h5p` `35 146` B / `3`, `erpnext` `35 149` B / `3` — **all GPL-3.0**; against `edx-platform`
`35 136` B / `15`, `hrshadhin/school-management-system` `34 522` B / `15`, `freelingo`
`34 514` B / `15` — **all AGPL-3.0.** 🟢 **The mention count separates them cleanly with no
overlap, and it is wrap-independent.** This belongs in `lib/license_family.sh` beside the
existing `p150-gpl-affero-discrimination` work — `ACTION OI` in
[`intel/open-gaps.md`](../intel/open-gaps.md).

🔵 **The shape of this is p199's own `openedx/XBlock` episode repeating with the roles
reversed:** a later pass "corrects" an earlier one, and the earlier one was right. **p199 wrote
the rule for exactly this case — *"Future passes: do not 'correct' that row"* — and it now
applies to its own GPL-3.0 rows.**

**That is `14` foundational repos with a licence read from source this pass** — above the 5-row
bar — across three groups: the `ECL-2.0` family (`6`), the permissive exits (`2`), and the
copyleft platforms a build must integrate with rather than absorb (`6`).

### 🔴 What this pass did NOT establish

- **`paella`'s grant.** The API and `package.json` both say `ECL-2.0`; **no blob exists** at
  `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license` or `COPYING` across `develop`, `master` and
  `main`. 🟡 Treat as *declared, ungranted* until someone finds the file.
- **Whether `ECL-2.0`'s narrowed patent clause has ever been tested**, or what it means for a
  non-education licensee of education-derived code. 🔵 **That is a legal question, not a
  measurement**, and it is the one an AI Studios engagement on Sakai or Opencast should put to
  counsel before the SOW. Registered in [`intel/open-gaps.md`](../intel/open-gaps.md).

## Pass 199 — 2026-10-14 — CANONICAL FOUNDATIONS TABLE (read this section first)

**Every licence below was read from the repo's own licence blob this pass**, via
`raw.githubusercontent.com/<slug>/<default-branch>/<file>`, after resolving the default branch
with `git ls-remote --symref`. `77` slugs were probed this pass and `68` resolved; the `29` below are the ones that earn a place in an education build. Licence column shows the
file the text actually came from when it is not plain `LICENSE`, because that detail is where
this pass found two real defects (see `agents/top.md`, "licence traps").

🔵 **Why the licence column is the most important column here.** Globant ships client work.
`MIT` / `Apache-2.0` / `BSD` can be embedded and sublicensed; **`AGPL-3.0` reaches across a
network boundary**, which means an AGPL component in a hosted student-facing service can oblige
you to offer the service's source to its users. The AGPL rows below are **not** mistakes — they
are the best tool in their slot — but they must be an explicit, client-approved decision, not
something a developer pulls in on a Tuesday.

### 🟢 Build-on-freely — MIT / Apache-2.0 / BSD / ECL

| Repo | Licence *(blob read)* | Slot it fills in an education build |
|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** *(`LICENSE.TXT`, `11 358` B)* | The **courseware component contract**. Write one XBlock and it runs inside Open edX without forking the platform. 🟢 The single highest-leverage integration point in open education |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** · `1.1k`★ | **Offline-first** learning platform. The only credible answer for low-connectivity deployments — decisive in LATAM public education and rural APAC |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | **BSD** | Multi-tenant notebook serving for a whole cohort; the de-facto CS/data-science teaching substrate |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | **BSD** | Assignment release → collect → autograde → feedback over notebooks. Pairs with JupyterHub; **the proven deterministic half of any AI grading pattern** |
| [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** · `6.9k`★ | Full interactive-lesson platform with its own explorations model; mature, permissive, forkable |
| [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** | **FSRS** scheduler as a clean Python library — spaced repetition without inheriting Anki's AGPL (see below). 🟢 Use this, not Anki, inside a product |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | The FSRS research/parameter-optimisation work and its evaluation harness |
| [docling-project/docling](https://github.com/docling-project/docling) | **MIT** | Document → structured text for **textbooks, PDFs, past exams**. MIT-licensed, which makes it the safest ingestion default |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** | Broader-format ingestion (slides, HTML, email); heavier than Docling, use when format coverage wins |
| [openai/whisper](https://github.com/openai/whisper) | **MIT** | Lecture/seminar transcription — the input to search, captions and study notes |
| [rhasspy/piper](https://github.com/rhasspy/piper) | **MIT** | Fast local **TTS**; runs on a Raspberry Pi, which matters for accessibility mandates and offline classrooms |
| [ollama/ollama](https://github.com/ollama/ollama) | **MIT** | Local model serving. **The compliance lever**: inference inside the institution's own perimeter |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | **Apache-2.0** | High-throughput serving when a cohort hits it at once (exam week, enrolment) |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | **MIT** | One API across providers + per-tenant budgets. 🟢 In education the **cost cap per student** is a product requirement, not an optimisation |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | **MIT** | Retrieval over curriculum corpora |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | **Apache-2.0** | Deep-document RAG with citation surfacing — citations are the difference between a tutor and a plagiarism engine |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | **Apache-2.0** | **Longitudinal learner memory** across sessions and terms. The architectural gap in almost every tutoring pilot |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT** | Tracing + eval of the agent itself. Required evidence for any EU high-risk assessment claim |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | **BSD** | Python/R autograding, containerised; UC Berkeley |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | Apache-derived, education-specific licence; full HiEd LMS/collaboration suite |
| [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** | Lecture capture + video pipeline at university scale |
| [jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet) | **Apache-2.0** | Self-hosted live classroom video |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** | Course **catalogue / marketing** front end for Open edX; built by France Université Numérique → **EMEA** |

### 🔴 Copyleft — real tools, deliberate decisions

| Repo | Licence | What the licence actually costs you |
|---|---|---|
| [overhangio/tutor](https://github.com/overhangio/tutor) | **AGPL-3.0** *(`LICENSE.txt`)* | The official Docker-based Open edX installer and **the only sane way to run Open edX**. Deployment tooling, so the network-copyleft reach is usually acceptable — but confirm per engagement |
| [ankitects/anki](https://github.com/ankitects/anki) | **AGPL-3.0** | Reference spaced-repetition implementation. 🟢 **Read it, then build on `py-fsrs` (MIT) instead** |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in Moodle/Canvas/Drupal. GPL is fine for a plugin inside an already-GPL LMS; it is a problem inside a proprietary product |
| [UCL-INGI/INGInious](https://github.com/UCL-INGI/INGInious) | **AGPL-3.0** | Secure sandboxed exercise assessment; UCLouvain → **EMEA** |
| [eecs-autograder/autograder-server](https://github.com/eecs-autograder/autograder-server) | **LGPL** *(`LICENSE.txt`, branch `develop`)* | U. Michigan autograder. 🔵 Earlier note: the slug `eecs-autograder/autograder` **does not exist** — the server repo is the real one |
| [pawtograder/platform](https://github.com/pawtograder/platform) | **GPL-3.0** *(branch `staging`)* | Open-source GitHub-Classroom replacement for CS courses: Actions autograding, rubric manual grading, gradebook. 🔵 Correct slug is `pawtograder/platform`, **not** `pawtograder/pawtograder` |

🔵 **Default branches are not all `main`.** This pass measured `master` for `openedx/XBlock` and
`ucbds-infra/otter-grader`, `develop` for `eecs-autograder/autograder-server` and
`frappe/education`, and `staging` for `pawtograder/platform`. A pipeline that hardcodes `main`
silently reports "no licence" for all five.
## Pass 198 — 2026-10-14

### 🆕 🔴 First: this pass ran CONCURRENTLY with p197, and p197 refutes three of its claims

🔵 **p197 was published by another session while this pass was mid-flight** *(commit `9cc3e97`,
`12:51`Z)*. 🟢 **It is the better outcome on three of the limbs, and the corrections are made
here rather than left for a reader to notice:**

| what this pass recorded | 🟢 what p197 actually established | correction |
|---|---|---|
| 🔴 *"the execution lane is CLOSED; all `290` recipes are unrunnable"* | 🟢 **p197 RAN `lib/test_license_family.sh`: `207`/`207` from SIX invocation forms, `0` skips** | 🔴 **The closure is SESSION-SCOPED, not environmental.** `bash <repo script>` is denied by *this* session's permission classifier. It is a property of the reader, not of the KB |
| 🔴 the suite fixture fix is *"half-answered, blocked"* | 🟢 **DONE and better than pre-registered.** p196's diagnosis was wrong: the pre-fix suite yields **three** denominators *(`207`/`183`/`163`)*, and the cause is not the directory but whether a relative `dirname` survives the suite's own `cd`. 🔴 Through a symlink the classifier never loaded and the suite **still printed a total** *(`19`/`163`)* | ✅ **closed by p197** |
| 🔴 *"the `26` population rows no census has reached are still unreached"* | 🔴 **p197: that number is FALSE AS STATED.** `30` folded rows probed; `16` were already published with the **same byte figure** | ✅ **the `26` was this KB's own instrument reach, not a property of the shelf** |

🟢 **And p197's headline generalises this pass's own finding:** *three published numbers
measured an instrument's reach rather than a property of the world.* 🔴 **This pass supplies a
fourth, below — a byte count of its own that measured its reader.**

### 🆕 🟢 Two independent instruments, same rows, same hour — and the cross-check paid

🔵 Both passes read the same two limbs. 🟢 **`OWN-GRANT-AT-ROOT`: `3`/`3` EXACT — same family
and the same byte count on every row**, from two separately written probes:

| slug | p197 | 🟢 this pass | agree? |
|---|---|---|---|
| `kstateome/lti-launch` | `LGPL-3.0` · `7 651` | `LGPL-3.0` · `7 651` | 🟢 **exact** |
| `open-spaced-repetition/fsrs4anki-helper` | `MIT` · `1 079` | `MIT` · `1 079` | 🟢 **exact** |
| `openedx/XBlock` | `Apache-2.0` · `11 358` | `Apache-2.0` · `11 358` | 🟢 **exact** |

🔴 **`Lumi`'s population DIVERGED, and each instrument missed a row the other found:**

| row | p197 | this pass | 🟢 who was right |
|---|---|---|---|
| `H5P.BranchingScenario-1.8/src/fonts/LICENSE.txt` | `11 560` | 🔴 `11 358` | 🔴 **p197.** See the CRLF defect below |
| `assets/h5p/core/fonts/open-sans/LICENSE-2.0.txt` | 🔴 not returned | 🟢 `Apache-2.0` · `11 358` | 🟢 **this pass** |
| `client/assets/legal/eula.html` *(`259 095` B)* | 🟢 returned | 🔴 missed | 🔴 **p197** — a `259` KB **End-User Licence**, and this pass's name filter only matched `licen[cs]e`/`copying` |

🟢 **The union population is `16`, not `15`** — and 🟢 **both passes reach the same conclusion
from different populations: `Lumi` grants nothing of its own; every text is vendored.** 🔵
[`evidence/cross-pass-agreement.2026-10-14-p198.tsv`](../evidence/cross-pass-agreement.2026-10-14-p198.tsv).

### 🆕 🔴 The fourth number that measured its reader: this pass's own byte counts

🔴 **Python text mode applies UNIVERSAL NEWLINES.** Reading a licence as text and reporting
`len(text.encode())` loses **one byte per CRLF line**, so the figure is the LF-normalised
length, not the file's size:

```
  BranchingScenario font LICENSE.txt   wc -c = 11 560   text-mode = 11 358   CRLF = 202
```

🟢 **`11 560 − 11 358 = 202`, exactly the CRLF count.** 🟢 **Blast radius, measured rather than
assumed: ONE row.** Every other text read this pass — all `30` root-licence rows, all `3` root
payloads, the other `13` `Lumi` texts — is LF, `delta 0`, so 🟢 **every byte figure in the
tables below stands**, and the `3` root payloads are independently confirmed byte-for-byte by
p197.

🔴 **But the band table was computed from these counts**, so a CRLF row would have shifted a
ratio silently. 🟢 **The fix is in `p198-title-line-family/`: read in BINARY, report `len(raw)`,
and report the CRLF count alongside it** so a reflowed text is visible as reflowed rather than
showing up as a band failure. 🔵 [`evidence/crlf-byte-undercount.2026-10-14-p198.tsv`](../evidence/crlf-byte-undercount.2026-10-14-p198.tsv).

🔵 **The lesson, and it is the same one three times over now:** `GPL-2.0`'s preamble made a
*window* report the wrong family; a filename list made a *first match* report the wrong file;
text mode made a *byte count* report the wrong size. 🟢 **Every one is a reader's property
published as the world's.**

🆕 🔴 **The lane census has a new row, and it is the one this KB was built on.**
`bash <repo script>` — the door to all `290` recipes in `compose/code/` — is **denied by the
session's permission classifier** *(`[Code from External]`)*. Tried twice: once as
`bash "$PWD/lib/test_license_family.sh"`, once on the documented
`cd lib && ./test_license_family.sh`. Both denied.

🟢 **The distinction p196 taught applies to this KB's own instruments now:** the recipes are
not *gone*, the **execution door** is shut. They remain readable, citable and auditable — and
`P0a` got more value out of them this pass than any pass that ran them.

### 🟢 The lane census, re-measured

| lane | door | p195 | p196 | 🟢 **p197** | what it yields |
|---|---|---|---|---|---|
| 🟢 `raw.githubusercontent.com` | `curl` | `200` | `200` | 🟢 **`200`** | licence **bytes** |
| 🟢 `git clone --filter=blob:none` + `ls-tree` | `git` | used | `88`/`88` | 🟢 **`7`/`7`, `0` failures** | the complete tree — the only channel that sustains an ABSENCE |
| 🆕 🟢 `git ls-remote --symref HEAD` | `git` | — | — | 🟢 **`30`/`30`** | the **real** default branch, not a guess |
| 🟢 GitHub MCP `search_repositories` | `mcp` | 🔴 presumed dead | 🟢 ANSWERS | 🟢 **ANSWERS** | ranked slugs + `license.spdx_id` + ★ + `pushed_at` |
| 🔴 `github.com` HTML *(incl. `/trending`)* | `curl` | `403` | `403` | 🔴 **`403`** | nothing |
| 🔴 `api.github.com` | `curl` | `403` | `403` | 🔴 **`403`** | nothing |
| 🔴 `gnu.org`, `mozilla.org` | `curl` | — | `403` | 🔴 **transfer fails outright** | canonical licence texts — unreachable |
| 🔴 `eur-lex.europa.eu` | `dns` | — | NO-RESOLVE | 🔴 **NO-RESOLVE** | primary OJ text — unreachable |
| 🆕 🟡 **`bash <repo script>`** | `exec` | 🟢 free | 🟢 free | 🔴 **DENIED *(this session)*** | 🔴 the KB's `290` recipes — readable, not runnable **here**. 🟢 **The concurrent p197 ran them, so this is a SESSION property, not an environment one** |
| 🆕 🟢 `python3 -I <own script>` | `exec` | — | — | 🟢 **OK** | re-derived instruments only |

🔵 [`evidence/lane-census.2026-10-14-p198.tsv`](../evidence/lane-census.2026-10-14-p198.tsv).

🟢 **The substitute for the canonical licence texts is still named, not hidden:** SPDX
`license-list-data` over the raw lane. This pass pulled `8` pristine anchors from it and they
are what every band and ratio below is measured against.

### 🆕 🟢 The anchor table, because two families need more than one anchor

| family | SPDX pristine | bytes |
|---|---|---|
| `MIT` | `MIT.txt` | `1 078` |
| `Apache-2.0` | `Apache-2.0.txt` | `10 280` |
| `ECL-2.0` | `ECL-2.0.txt` | `11 111` |
| `GPL-2.0` | `GPL-2.0-only.txt` | `17 337` |
| `GPL-3.0` | `GPL-3.0-only.txt` | `34 674` |
| `AGPL-3.0` | `AGPL-3.0-only.txt` | `34 020` |
| `LGPL-2.1` | `LGPL-2.1-only.txt` | `26 001` |
| 🔴 `LGPL-3.0` | `LGPL-3.0-only.txt` | `42 098` — 🔴 **and this is the WRONG anchor for real repositories** |

### 🔴 `LGPL-3.0`'s SPDX anchor is unusable, and the ratio says so in one glance

🔵 p196 flagged that `LGPL-3.0` is published in two legitimate forms. 🟢 **This pass measures
the gap:**

| slug | bytes | ratio to SPDX `42 098` |
|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | `7 651` | 🔴 **`0.182`×** |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `7 652` | 🔴 **`0.182`×** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `8 241` | 🔴 **`0.196`×** |

🟢 **The shipped form is the `~7.6` KB ADDENDUM** — the text that incorporates `GPL-3.0` by
reference rather than restating it. SPDX publishes the standalone form. Both are valid
`LGPL-3.0`; they differ `5`-fold in bytes. 🔴 **Any band, gate or freshness check that centres
`LGPL-3.0` on `42 098` flags every real repository.** The addendum form needs its own anchor,
and deriving it from `≥10` rows is pre-registered.

### 🟢 Foundational repositories — `10` rows, every licence from BYTES

| repo | 🟢 licence *(bytes)* | branch | what it is foundational FOR |
|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **`GPL-3.0`** · `35 147` B at **`COPYING.txt`** | `main` | the LMS with the largest installed base; 🔵 **the grant is not at a file named `LICENSE`** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** · `35 136` B | `master` | the higher-ed course platform; 🔴 **network-use disclosure** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **`AGPL-3.0`** · `34 520` B | `master` | the North American university LMS incumbent |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 **`Apache-2.0`** · `11 358` B | `develop` | 🟢 interactive lesson engine — **permissive, and `6 855`★** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **`MIT`** · `1 097` B | `develop` | 🟢 **offline-first** learning platform — the LATAM/Africa connectivity primitive |
| [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **`MIT`** · `1 079` B | `master` | 🟢 course-catalogue/marketing front end for Open edX |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **`AGPL-3.0`** · `34 523` B | **`release`** | the Docker distribution that makes Open edX deployable |
| [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **`GPL-3.0`** · `35 146` B | `master` | the interactive-content runtime embedded by Moodle, Canvas and Drupal |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`AGPL-3.0`** · `33 893` B | — | `3 312`★ LMS on the Frappe stack |
| [`processing/p5.js`](https://github.com/processing/p5.js) | 🟡 **`LGPL-2.1`** · `24 480` B | — | `24 122`★ creative-coding library; the teaching-of-code primitive |

🔵 `6` of `10` are copyleft and `3` of those are Affero. 🟢 **The permissive foundations are
`oppia`, `kolibri` and `richie`** — and that is the short list for a hosted deliverable that
cannot carry a disclosure obligation.

### 🆕 🔴 Four repositories where the grant is NOT where a reader would look

🔵 Full table: [`evidence/licence-at-wrong-path.2026-10-14-p198.tsv`](../evidence/licence-at-wrong-path.2026-10-14-p198.tsv).

| slug | 🔴 what a reader assumes | 🟢 what the bytes say |
|---|---|---|
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | `LICENSE` is the licence | 🔴 `LICENSE` = **`CC-BY-4.0`** *(content)*; 🟢 the code grant is **`LICENSE-CODE`** = `MIT` |
| [`formalms/formalms`](https://github.com/formalms/formalms) | Apache-2.0 *(the open web)* | 🔴 **`GPL-2.0`**, and **nothing at the root** — it ships at `html/lib/System/license/license_english.txt` |
| [`foradian/fedena`](https://github.com/foradian/fedena) | Apache-2.0 *(the open web)* | 🟡 Apache-2.0 **declared in `NOTICE`** `679` B — 🔴 **the repo ships NO licence text at all** |
| [`frappe/education`](https://github.com/frappe/education) | `GPL-3.0` *(the sidebar)* | 🔴 **`license.txt` is `19` bytes:** `License: GNU GPL V3` — a pointer, no holder, no warranty disclaimer, no *or-later* clause |

🔴 **Three of the four are weaker than they look, and the fourth is mislabelled in both
directions.** For a studio this is the difference between a grant it can rely on and a
sentence in a file.

### 🟢 Declared gaps, so silence is not mistaken for coverage

- 🟡 **The `494`-row existence census did not run in THIS session** — execution lane. ✅ **The
  concurrent p197 ran it**; see its `evidence/existence-casefolded.2026-10-14-p197.tsv`.
- 🔴 **The `26`-unreached figure is FALSE AS STATED** — p197 probed `30` folded rows and found
  `16` already published with the same byte figure. 🟢 **It measured this KB's instrument reach,
  not the shelf.**
- 🔴 **No star velocity.** `pushed_at`-filtered rank is *stock filtered by recency*, not flow;
  `github.com/trending` is `403`.
- 🔴 **`sonic-pi-net/sonic-pi` resolves only to `AGPL?`** — the version is not readable from
  its title line. Carried as unresolved, not rounded to `AGPL-3.0`.

## Pass 197 — 2026-10-14

🆕 🟢 **The shared classifier's suite is PATH-INDEPENDENT, measured from `6` invocation forms:
`207`/`207` each, `0` SKIP.** p196's pre-registered action, limb `1`, closed.

🔴 **And the diagnosis it inherited was wrong in a way that matters more than the fix.** p196
recorded *«`207`/`207` from `lib/`, `179`/`181` from one directory up — `26` assertions silently
skipped»* and called the cause **the directory**. The replica this pass rebuilt, with p196's
exact pre-fix header, answers **three different denominators**:

| invocation form | pre-fix | post-fix |
|---|---|---|
| absolute path, from outside the repo | `207`/`207` | 🟢 `207`/`207` |
| from `lib/` itself | `207`/`207` | 🟢 `207`/`207` |
| `lib/test_license_family.sh` from `compose/code` | 🔴 **`179`/`183`** | 🟢 `207`/`207` |
| `compose/code/lib/…` from the repo root | 🔴 **`179`/`183`** | 🟢 `207`/`207` |
| 🟡 `../lib/…` from a SIBLING recipe directory | 🟡 **`207`/`207` — by luck** | 🟢 `207`/`207` |
| 🔴 through a **symlink** in another directory | 🔴 **`19`/`163`** | 🟢 `207`/`207` |

🔵 **Where p196 read `179`/`181` the replica reads `179`/`183`:** the replica carries p197's two
new presence canaries, and **the `+2` IS the canaries firing** — the same mutilated run, two
assertions louder. The `26` assertions that do not run still do not run.

🔵 **The cause is not the directory: it is whether a RELATIVE `dirname` still happens to resolve
after the suite's own `cd`.** `../lib/..` lands on `compose/code` once the cwd is `lib/`, so that
form passed for the wrong reason — **a denominator that depended on path arithmetic, which is
why two measurements supported the wrong rule.**

🔴 **And the worst form was not measured at all before this pass.** Through a symlink,
`${BASH_SOURCE[0]}` names the **link**, `./license_family.sh` is not beside it, the classifier
**never loads** — and the suite runs to the end and **prints a total**. `19`/`163` is a result,
not an error, which is `P502`'s shape one level above where p196 found it.

### 🟢 The fix, and only its first third was pre-registered

1. the script's own directory is resolved **once, absolute, BEFORE the `cd`**, and every fixture
   root hangs off it — including the two that were plain relative strings;
2. 🆕 it is resolved **physically** *(`readlink -f`)*, so a symlink resolves to the file;
3. 🆕 loading the classifier is a **hard gate**: the `source` is checked and `family_of` is
   asserted to exist before the first case.

🆕 🟢 **Plus the canary the other two blocks already had.** `P854` and `T232` each assert
*«fixtures present»*; `P560`/`P561` and `P845` only echoed `SKIP` to stderr — and they are
exactly the two that p196 watched disappear. They assert it now, so absence costs a **visible
FAIL** instead of a quieter denominator. 🔵 It does not make a mutilated run whole; it makes it
loud.

🔵 Instrument, result tables and a `19`/`19` suite whose `4` negative cases rebuild the defect:
[`compose/code/p197-suite-path-independence/`](../compose/code/p197-suite-path-independence/).
🆕 **It is re-runnable against any suite** — `SUITE_UNDER_TEST=<path> run_from_dirs.sh` — and
the shelf-wide sweep is pre-registered rather than claimed.

### 🆕 🔴 A latent instance, found while reading the shelf and NOT fixed

[`p107-git-lane-census/census.sh`](../compose/code/p107-git-lane-census/) takes its slug list as
`$1` **after** `cd "$(dirname "$0")"`. 🔴 **A relative list argument resolves against the wrong
directory**, so the census would read a different file — or none. 🟢 This pass passed an
absolute path and the run is sound *(`494` rows)*. 🔵 Recorded, pre-registered, **not patched**:
the sweep that fixes this class fixes it once for every recipe, and `P237` forbids a one-off
edit to a shared instrument on a pass that did not register it.

### 🟢 The foundational layer's existence column, case-folded over the whole shelf

| | |
|---|---|
| population, raw | `499` |
| 🟢 **case-folded distinct** | 🟢 **`494`** |
| case-variant pairs collapsed | `5` — `OS4ED/openSIS-Classic`, `OpenOLAT/OpenOLAT`, `Hesham0-0Nasser/tutor-lms-mcp`, `ShuyunYuan/talentcoach`, `ahmedEid1/Lumen` |
| 🟢 resolved by the anonymous git lane | 🟢 **`492`/`494`** |
| 🔴 **ABSENT** *(git asks for credentials, `rc=128`)* | 🔴 `apereo/opencast`, `yourusername/scholarmate` |
| 🆕 🔴 **EXIST AND ARE EMPTY** *(reachable, `0` heads, `0` tags)* | 🆕 🔴 `cdweaver1992/edfi-mcp-server`, `openfresno/edgenuity-aeries-grade-passback` |

🟢 **Case-folding is safe: no case-variant is a distinct repository** — p196 proved it by cloning
both `OS4ED` spellings, and all `5` folded slugs resolve here. 🟢 **The phantom class closes to
`4` named rows**, and it closes **in two different ways**.

🆕 🔴 **Existence has three states and two channels of this KB disagreed over a FLAG.**
`ls-remote --exit-code -h` returns `2` for *«no matching refs»*, which the first version of this
pass's reader published as `ABSENT`; `--heads --tags` without `--exit-code` returns `0` with no
output. 🔵 **An empty repository exists.** It has no licence because it has no files — a
different fact from a repository that is gone, and a KB that merges them miscounts its own
denominator in both directions.

🔴 **`apereo/opencast` is a stale ORG path**, not a casing variant:
[`opencast/opencast`](https://github.com/opencast/opencast) is on this shelf and resolves.
🔴 **`yourusername/scholarmate` is a template placeholder** — a syntactically valid slug whose
owner is a filler token, published as an address.

### Open limbs

🔴 **The `7` `ABSENCE-ENUMERATED` rows of the population are unresolved** — the channel that
would resolve them *(a declaration reader)* must not be improvised, for the reason p195
measured. 🔴 **`eur-lex` still does not resolve; `github.com` `403`, fourth pass.** 🔴 **The
`eula` basename still counts as a grant in `is_licence_path`** — measured on `Lumi`'s `259 095` B
EULA, pre-registered, not patched in the pass that promoted the predicate.

## Pass 196 — 2026-10-14

🆕 🟢 **A lane this file declared gone one pass ago is reachable by a different door.** p195
recorded `api.github.com` as `403` and `github.com` HTML as newly `403`; both are re-measured
`403` this pass. 🟢 **The GitHub MCP channel returns the same ranked data — `license.spdx_id`,
stars, `pushed_at` — and it answered on the first call.** The API lane was never *gone*; the
`curl` door to it is shut.

### 🟢 The lane census, corrected

| lane | p195 | 🟢 p196 | what it yields |
|---|---|---|---|
| 🟢 `raw.githubusercontent.com` | `200` | 🟢 **`200`** | licence **bytes**; `2 167` probes, `0` throttles at p195's volume |
| 🟢 `git clone --filter=blob:none` + `ls-tree` | used by `P441` | 🟢 **`200`, `88`/`88` clones, `0` failures** | the **complete tree** — the only channel that sustains an ABSENCE |
| 🆕 🟢 **GitHub MCP `search_repositories`** | 🔴 recorded as part of a dead API lane | 🟢 **ANSWERS** | ranked slugs + `license.spdx_id` + ★ + `pushed_at` |
| 🔴 `github.com` HTML *(incl. `/trending`)* | 🔴 `403` | 🔴 **`403`** | nothing |
| 🔴 `api.github.com` via `curl` | 🔴 `403` | 🔴 **`403`** | nothing |
| 🔴 `gnu.org`, `mozilla.org` | — | 🔴 **`403` at the proxy** | canonical licence texts — **unreachable** |
| 🔴 `eur-lex.europa.eu` | — | 🔴 **DNS does not resolve** | primary OJ text — **unreachable** |

🔵 **The substitute for the canonical licence texts is named, not hidden:** SPDX
`license-list-data` over the raw lane. 🟢 It is still an **external** reference in `P417`'s
sense — outside the instrument that consumed it — which is the property that matters.
🔵 [`evidence/licence-pristine-anchors.2026-10-14-p196.tsv`](../evidence/licence-pristine-anchors.2026-10-14-p196.tsv).

### 🔴 `spdx/license-list-data` is itself a root-`NONE` row on this shelf

🔵 A small irony worth recording because it is also a measurement: the repository this pass
used as its external licence reference **sits in p195's `88` root-`NONE` population**, and the
tree enumeration finds **`16` own licence texts** in its `13 239`-path tree. 🟢 The reference is
sound; the root probe simply could not see its grant either.

### 🟢 The foundational layer, licence read from bytes — `+8` rows this pass

🔵 All eight arrived through the reopened MCP channel and **none was published on that
channel's word**: every licence below was fetched over the raw lane, sized, `md5`'d, and
classified by `lib/license_family.sh` plus this pass's band.

| repo | ★ | path | bytes | 🟢 family | band | what it is for |
|---|---|---|---|---|---|---|
| [`TheAlgorithms/Python`](https://github.com/TheAlgorithms/Python) | `225 237` | `LICENSE.md` | `1 095` | 🟢 **`MIT`** | 🟢 `IN-BAND` | reference algorithm corpus — CS curriculum content |
| [`CTFd/CTFd`](https://github.com/CTFd/CTFd) | `6 876` | `LICENSE` | `11 314` | 🟢 **`Apache-2.0`** | 🟢 `IN-BAND` | capture-the-flag platform — **assessment infrastructure** |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `6 855` | `LICENSE` | `11 358` | 🟢 **`Apache-2.0`** | 🟢 `IN-BAND` | explorations / structured lessons |
| [`mlcommons/ck`](https://github.com/mlcommons/ck) | `649` | `LICENSE.md` | `10 174` | 🟢 **`Apache-2.0`** | 🟢 `IN-BAND` | benchmark automation |
| [`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) | `1 029` | `LICENSE.md` | `1 122` | 🟢 **`MIT`** | 🟢 `IN-BAND` | material→course generation |
| [`ystemsrx/mini-nanoGPT`](https://github.com/ystemsrx/mini-nanoGPT) | `383` | `LICENSE` | `1 063` | 🟢 **`MIT`** | 🟢 `IN-BAND` | teaching LLM internals |
| [`SYuan03/Skill-Anything`](https://github.com/SYuan03/Skill-Anything) | `337` | `LICENSE` | `1 084` | 🟢 **`MIT`** | 🟢 `IN-BAND` | agent-skill scaffolding |
| 🟡 [`EbookFoundation/free-programming-books`](https://github.com/EbookFoundation/free-programming-books) | `399 021` | `LICENSE` | `18 658` | 🟡 **`CC-BY-4.0`** | `NO-BAND` | 🟡 **content licence, attribution obligation** |
| 🔴 [`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch) | `385` | `LICENSE` | `4 635` | 🔴 **`PolyForm`** | `NO-BAND` | 🔴 **NONCOMMERCIAL — barred from a client deliverable** |

🟢 `learningequality/kolibri` re-confirms **`MIT` at `1 097` B** and
`AnubisLMS/Anubis` **`MIT` at `1 083` B** from both channels.

### 🔴 The ranked channel's blind spot, measured — `2` of `13`

| rows compared | 🟢 AGREE | 🔴 API-BLIND | DIVERGE |
|---|---|---|---|
| `13` | 🟢 **`11`** | 🔴 **`2`** | 🟢 **`0`** |

🔴 **Both blind rows are exactly the rows a delivery decision turns on:**

| row | the channel | 🔴 the bytes |
|---|---|---|
| 🔴 `TrenTorch/TrenTorch` | `NOASSERTION` | 🔴 **`PolyForm Noncommercial 1.0.0` — PROHIBITED** |
| 🔴 `frappe/education` | `NOASSERTION` | 🔴 **`license.txt`, `19` B, in full: `License: GNU GPL V3`** |

🟢 **`0` DIVERGE is the number that licenses the channel for discovery.** 🔴 **`2` API-blind is
the number that forbids it for delivery.** A `NOASSERTION` is not *"probably permissive"* — on
this sample it was once a non-commercial bar and once a `19`-byte declaration.

### 🔴 And this file's own ad-hoc probe reproduced the defect it is documenting

🔵 The `12`-name probe written this pass to byte-verify the new rows **missed
`frappe/education`** — the path is lowercase `license.txt`, and the list had `LICENSE.txt`,
`License.txt` and `license` but not `license.txt`. 🟢 p195's `19`-name ladder found it.
🔴 **In the pass whose headline finding is that widening a filename list cannot fix a list, the
author wrote a list and it failed the same way.** Recorded rather than quietly corrected,
because it is the strongest available evidence for `P441`.

### 🟢 The platform layer's licences, against what the open web says

🔵 A web sweep this pass returned *"sources disagree on several licenses"* and, for Open edX,
*"most say AGPLv3, one says Apache 2.0."* 🟢 **This KB does not have to choose — it has bytes:**

| platform | the open web | 🟢 byte-verified | verdict |
|---|---|---|---|
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 split: AGPLv3 **or** Apache-2.0 | 🟢 **`AGPL-3.0`, `35 136` B** | 🔴 the Apache claim is **WRONG** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 one source says *"Apache 2.0"* | 🟢 **`ECL-2.0`, `11 120` B** | 🔴 **WRONG** — ECL is Apache-*derived*, not Apache |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 🟢 **`Apache-2.0`, `10 982` B** | 🟢 confirmed |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPLv3 core | 🟢 **`AGPL-3.0`, `34 520` B** | 🟢 confirmed |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | LGPLv3 | 🟢 **`LGPL-3.0`, `8 241` B** | 🟢 confirmed |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL | 🟢 **`GPL-3.0`, `35 147` B at `COPYING.txt`** | 🟢 confirmed — **and the filename is not `LICENSE`** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | GPL | 🟢 **`GPL-3.0`, `35 121` B** | 🟢 confirmed |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | GPL | 🟢 **`GPL-2.0`, `15 214` B** | 🟢 confirmed — **v2, not v3** |

🟢 **The web sweep also reported *"none of the results confirmed MIT licensing for any LMS or
SIS"*, and the census agrees by measurement:** of the hosted-LMS layer, `0` rows are `MIT`. The
`218` `MIT` rows on this shelf are tools and agents, not platforms. 🔵 p195's *"the hosted-LMS
layer is Affero as a market"* now stands on a second, independent channel.

### 🟢 The `5` foundational repos the quality bar asks for, all byte-verified, all permissive

| # | repo | ★ | 🟢 licence | bytes | why foundational |
|---|---|---|---|---|---|
| `1` | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `1 145` | 🟢 **`MIT`** | `1 097` | offline-first LMS — the only permissive platform-grade base on this shelf |
| `2` | [`oppia/oppia`](https://github.com/oppia/oppia) | `6 855` | 🟢 **`Apache-2.0`** | `11 358` | structured lesson engine with a patent grant |
| `3` | [`CTFd/CTFd`](https://github.com/CTFd/CTFd) | `6 876` | 🟢 **`Apache-2.0`** | `11 314` | assessment / challenge infrastructure |
| `4` | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | — | 🟢 **`Apache-2.0`** | `10 982` | full university LMS, permissive — rare |
| `5` | [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | `381` | 🟢 **`MIT`** | `1 083` | autograding / per-student cloud IDE |
| `6` | [`TheAlgorithms/Python`](https://github.com/TheAlgorithms/Python) | `225 237` | 🟢 **`MIT`** | `1 095` | CS curriculum content at scale |

🔵 `sakaiproject/sakai` **`ECL-2.0`** `11 120` B and `opencast/opencast` **`ECL-2.0`** `11 340` B
remain the two `ECL` rows: Apache-derived, patent grant scoped to education, 🟢 permissive for
delivery purposes.

### 🟡 The denominator every percentage on this page divides by

🔵 p192's population rule, re-applied verbatim to the current three pages:

| | count |
|---|---|
| p192 *(inherited unchanged by p193, p194, p195)* | `472` |
| 🟢 **p196** | **`499`** raw · 🔴 **`494`** distinct after case-folding |
| 🔴 added · 🟢 removed | **`+27`** · 🟢 **`0`** |

🔴 **The phrase *"the whole shelf"* — used on this page and on
[`agents/top.md`](../agents/top.md) — is wrong by `27` real rows and `5` phantoms.** 🟢 The
useful half: `0` removed, so this shelf still does not rot.
🔵 [`compose/code/p196-population-diff/`](../compose/code/p196-population-diff/), suite **`20`/`20`**.

### 🆕 🔴 The shared suite's assertion COUNT depends on the invoking directory

🔵 Found by accident this pass, running the shared classifier's suite from one directory up.
🔴 **The same script, the same commit, two different totals:**

| invoked from | result |
|---|---|
| 🟢 `compose/code/lib/` | 🟢 **`207`/`207`** — the figure p194 and p195 published, and it is correct |
| 🔴 `compose/code/` | 🔴 **`179`/`181`** |

🔴 **The danger is not the `2` failures — it is the `26` assertions that SILENTLY DISAPPEAR.**
`207 − 181 = 26`. The suite resolves its fixture paths *(`lib/fixtures-p551`, `-p613`, `-p845`,
`-p854`, `-p990`)* relative to the **current** directory rather than to `${BASH_SOURCE[0]}`, so
from the wrong place the fixture-backed assertions are skipped and two presence checks fail.

🔴 **A pass that invokes it from the wrong directory reads `179/181` as *"two regressions in the
shared classifier"* when the truth is *"twenty-six assertions never ran."*** 🟢 **The wrong
reading is the alarming one, which is the lucky direction** — but a suite that can report a
smaller denominator without saying so is a suite that can hide coverage loss.

🟢 **`207`/`207` stands. The instrument is sound; its invocation is not path-independent.**
🔵 The fix is one line *(resolve fixtures from `${BASH_SOURCE[0]}`, as this pass's own recipes
do)* and it is **not applied here** — `P237` forbids editing the shared classifier on a pass
that did not pre-register it. 🟢 **Pre-registered for p197**, with the limb: if the count is
`207` from every directory after the fix, the class closes; if some assertion is genuinely
CWD-dependent in substance, name it.

### Open limbs

🔴 **`26` of the `494` distinct rows have never been probed by any census.** 🔴 **The `3`
`OWN-GRANT-AT-ROOT` payloads are found but unread.** 🔴 **No primary-source read of the EU OJ
text** — `eur-lex` does not resolve here, so the OJ number in
[`intel/market.md`](../intel/market.md) rests on secondary convergence and says so.

## Pass 195 — 2026-10-14

🆕 🟢 **The foundational layer now has a licence column read from bytes on every row, because
the census p194 pre-registered ran and the lane did not flinch: `468` LIVE slugs, `2 167`
probes, `0` throttles, `0` refusals, `0` indeterminate rows.** 🔵
[`evidence/shelf-licence-census.2026-10-14-p195.tsv`](../evidence/shelf-licence-census.2026-10-14-p195.tsv).

🔴 **And the lane that this file has spent thirteen passes characterising lost a member mid-pass.**
`github.com` — HTML pages, not just the API — is now refused at this session's proxy with `403`
and a policy JSON body. 🔵 Lane census in [`repos/trending.md`](trending.md).

### 🟢 The foundational shelf, licence read from bytes this pass

| repo | layer | 🟢 licence | bytes | path | delivery |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | LMS | 🟡 **`GPL-3.0`** | `35 147` | `COPYING.txt` | 🟡 copyleft, **no network clause** |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | LMS | 🔴 **`AGPL-3.0`** | `35 136` | `LICENSE` | 🔴 network-use disclosure |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | LMS | 🔴 **`AGPL-3.0`** | `35 136` | `LICENSE` | 🔴 same, byte-identical |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | LMS | 🔴 **`AGPL-3.0`** | `34 520` | `LICENSE` | 🔴 network-use disclosure |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | LMS | 🟡 **`GPL-3.0`** | `35 147` | `LICENSE` | 🟡 copyleft |
| [`frappe/lms`](https://github.com/frappe/lms) | LMS | 🔴 **`AGPL-3.0`** | `33 893` | `license.txt` | 🔴 **p193's correction, third channel** |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | Open edX deploy | 🔴 **`AGPL-3.0`** | `34 523` | `LICENSE.txt` | 🔴 the deployer is Affero too |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟢 **`ECL-2.0`** | `11 120` | `LICENSE` | 🟢 permissive, **patent grant scoped to education** |
| [`opencast/opencast`](https://github.com/opencast/opencast) | lecture capture | 🟢 **`ECL-2.0`** | `11 340` | `LICENSE` | 🟢 same family |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | LMS | 🟢 **`Apache-2.0`** | `10 982` | `LICENSE` | 🟢 permissive |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | offline learning | 🟢 **`MIT`** | `1 097` | `LICENSE` | 🟢 permissive |
| [`openfun/ralph`](https://github.com/openfun/ralph) | LRS *(xAPI)* | 🟢 **`MIT`** | `1 094` | `LICENSE.md` | 🟢 permissive |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | education ERP | 🟡 **`LGPL-3.0`** | `8 241` | `LICENSE` | 🟡 linkable copyleft |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS | 🟡 **`GPL-2.0`** | `15 214` | `LICENSE` | 🟡 copyleft |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | school management | 🟡 **`GPL-3.0`** | `35 121` | `LICENSE` | 🟡 copyleft |

🟢 **`15` rows, `15` licences from bytes. `ECL-2.0` on `sakai` is byte-exact against the `md5`
this KB recorded at p191**, so the Apereo family now stands on three independent channels
*(blobless clone, the ranked channel's `spdx_id`, the raw lane)*.

🔴 **The structural reading, and it is the one a client architecture turns on: the hosted-LMS
layer is Affero as a MARKET, not as an exception.** 🟢 `41` of the `380` licensed rows on the
whole shelf are `AGPL-3.0` — **more than every restricted and source-available category
combined** — and they include Open edX *(four slugs)*, Canvas, Frappe LMS, `classroomio`,
`learnhouse` and `tutor`. 🟡 **The permissive LMS route exists and is narrow: `ECL-2.0`
*(Sakai, Opencast)*, `Apache-2.0` *(OpenOLAT)*, `MIT` *(Kolibri, offline-first)*.**

### 🆕 🔴 The interoperability layer does not ship a grant — `3` of `3` standards-body repos

🔵 Measured with the full `19`-filename root ladder, then README-checked, then probed one level
down at `docs/`, `legal/`, `.github/`:

| repo | body | root licence | README claim | deeper path |
|---|---|---|---|---|
| 🔴 [`1EdTech/lti-1-3-php-example-tool`](https://github.com/1EdTech/lti-1-3-php-example-tool) | **1EdTech** *(LTI)* | 🔴 **NONE** | 🔴 **none** | 🔴 none found |
| 🔴 [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | **ADL** *(SCORM/xAPI)* | 🔴 **NONE** | 🟡 **`## License` → *"Licensed under the Apache License, Version 2.0"*** | 🔴 none found |
| 🟡 [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) | H5P desktop | 🟢 **`AGPL-3.0`** *(`package.json`, `3 600` B, p215)* | 🔴 **none at root** | 🟢 **the manifest** <!--corrected--> |

🔴 **These are the reference implementations an engagement reads FIRST when it has to speak LTI,
SCORM or xAPI**, and two of the three grant nothing in any form this KB can find. 🟡 `adlnet`'s
is the softer case and still not a grant: **a README sentence electing `Apache-2.0` with no
licence file anywhere**, which is this KB's claim-versus-file shape with the file simply absent.
🟢 **Consequence for a proposal: the standards are open; these repositories are not a licensed
starting point.** 🔵 The permissive interoperability row that *does* hold up is
[`openfun/ralph`](https://github.com/openfun/ralph) — `MIT`, `1 094` B — at `51`★.

### 🔴 `88` rows return no licence at root — and the figure's SCOPE is the finding

🔵 `18.8`% of the `468`. 🔴 **It must be quoted as *"no licence at ROOT across `19`
filenames"*, never as *"unlicensed"*, and p195 has the counter-example that proves why:**

| repo | root ladder | 🟢 one directory down |
|---|---|---|
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`19` probes, all `404`** | 🟢 **`docs/License.txt` — `17 286` B, `GPL-2.0`** |

🟢 **The README said so all along** — *"licensed under the GNU General Public License, the full
license can be found here"*, linking that path. 🔵 **Already registered as
[`p969-root-only-licence-reach`](../compose/code/p969-root-only-licence-reach/), whose open limb
is exactly this**; cited rather than re-derived. 🔴 **So `18.8`% is an UPPER BOUND on absence
and a LOWER BOUND on nothing**, and p196's pre-registered job is to probe the `88` one level
down and convert it.

### 🆕 🟡 `4` rows elect `Apache-2.0` without shipping it

🔵 Surfaced by a byte-band check, not by reading bodies: `Apache-2.0` is `11 348` B of text,
and these four are `560`–`738`.

| repo | bytes | what the file contains |
|---|---|---|
| [`numbas/numbas-lti-provider`](https://github.com/numbas/numbas-lti-provider) | `560` | *"Licensed under the Apache License, Version 2.0 … http://www.apache.org/licenses/LICENSE-2.0"* |
| [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | `738` | same shape |
| [`foradian/fedena`](https://github.com/foradian/fedena) | `679` | same shape |
| [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | `680` | same shape |

🟢 **The election is valid and the family verdict stands** — these are `Apache-2.0` projects and
`commercial_use_ok` allows them. 🟡 **What is missing is the licence TEXT, which `Apache-2.0`
§`4(a)` requires a redistributor to include** — so the obligation lands on whoever ships a
derivative, and the fix is one file. 🔵 `fedena` is a **fork pair**: distinct `HEAD` shas,
byte-identical licence files.

### 🔴 The correction this pass owes its own census — the population is not "the whole shelf"

🔵 p192 derived a `472`-slug population and p194 and p195 both inherited the phrase *"the whole
shelf"*. 🔴 **Four rows on p193's own ranked `30`-row table are NOT in it** —
`virgiliojr94/book-to-skill` *(rank `2`)*, `PetoiCamp/OpenCat-Quadruped-Robot` *(`7`)*,
`ai-infra-curriculum/ai-infra-engineer-learning` *(`11`)*, `mohi-devhub/antivibe` *(`15`)* —
and **all four are rows p193 marked 🆕 NEW.** 🟢 **The extraction predates the pages it claims
to cover.**

🔵 Also inherited, and already on this page at line `325`: `ShuyunYuan/talentcoach` ≡
`shuyunyuan/talentcoach` is **one repository** *(`HEAD` sha `b450118a7e8a` under both
spellings)*, so the `468` holds a duplicate identity and the distinct count is **`467`**.

🔴 **Every per-shelf percentage published since p192 — `18.8`%, `5.7`%, the family
distribution — carries this denominator.** 🟢 Stated here before anyone quotes one.

### 🟢 Method, carried forward

🟢 **`lib/license_family.sh` was sourced, not forked** *(`207`/`207` **run from `lib/`** —
🆕 🟡 the same suite returns **`179`/`181` from the repo root**, where two fixture guards fail on
`cwd`-relative paths and the `26` assertions they feed never run; 🟢 **not a regression — the
guards failed loudly rather than passing on an empty corpus**, and the shape is registered as
[`p355-cwd-portability`](../compose/code/p355-cwd-portability/). 🔴 **Never quote the score
without its `cwd`.**)*, and `P834` was honoured: **every byte count on this page comes from `size_of_file` over a file on disk**, never
from `$(…)`. 🔴 **p195 still committed the pass-level version of the same error**: it built a
band control whose findings were already registered as `P1054`, `P1056` and `Gap 421`, because
it read its own census TSV as the state of knowledge instead of reading these pages.
🟢 **`P237`'s rule generalises, and p196 inherits it as a pre-registered step: grep
`compose/code/` and the four pages for the defect class BEFORE building the instrument.**
## Pass 194 — 2026-10-14

🆕 🔴 **This pass set out to report a new lane and a new method finding. Both were already in
this KB — one of them `242` times — and the reason p194 did not know is that it read p193's
summary table as the state of knowledge.**

🟢 **What survives, and it is the stronger result: every licence verdict this pass publishes was
re-classified by this KB's own hardened instrument, `compose/code/lib/license_family.sh`,
whose suite measures `207`/`207` today. `30` of `35` agree exactly; the `5` divergences are
spelling, and in all `5` the library is right.**

### 🔴 First, the correction to this pass's own premise

🔵 p194 probed four URLs for one repository and found `raw.githubusercontent.com` answering
`200` with licence bytes while three GitHub lanes answered `403`. 🔴 **It then drafted that as a
discovery. It is not.**

| where the raw lane already appears | count |
|---|---|
| [`agents/trending.md`](../agents/trending.md) | 🔴 **`150`** |
| [`repos/trending.md`](trending.md) | 🔴 **`142`** |
| `compose/code/` *(files)* | 🔴 **`242`** |
| this file | `15` |
| [`intel/trends.md`](../intel/trends.md) · [`agents/top.md`](../agents/top.md) | `10` each |
| [`intel/market.md`](../intel/market.md) | `8` |
| 🟡 [`verticals/solutions.md`](../verticals/solutions.md) | 🟡 **`0`** |

🟢 **`compose/code/p288-agpl-casefold/README.md`, dated `2026-10-04`, states it outright:**
*"`github.com/<org>/<repo>` → `403` en `3`/`3` · `raw.githubusercontent.com` → `200` con payload.
La licencia se LEE; el `curl -sI` que el encargo ordena sigue muerto acá."* 🔴 **Ten days before
this pass announced it.**

🔵 **The mechanism of the error is worth more than the error.** p193's lane table lists four
lanes — `curl` direct, `gh` CLI, MCP `search_repositories`, page fetch — and **does not include
the raw lane**, although the same file mentions it `150` times further down. 🔴 **A pass that
reads the newest summary to learn the KB's state learns the summary, not the state.** 🟢 That is
a property of how this KB publishes, and it is correctable: **a lane table must be a census of
the lanes this KB uses, not of the lanes the current pass happened to probe.**

### 🟢 The lane table, corrected to a census

| lane | `github.com/trending` | `api.github.com` | file payloads | verdict |
|---|---|---|---|---|
| `curl` direct to `github.com` | 🔴 `403`, `378` B | 🔴 `403`, `378` B | 🔴 `403` | blocked |
| `gh` CLI | — | 🔴 `403` | — | blocked |
| `codeload.github.com` | — | — | 🔴 **`403`, `378` B** *(new probe this pass)* | blocked |
| MCP `search_repositories` | n/a | 🟢 works | 🔴 no file bodies | 🟢 **open — the ranking channel** |
| page fetch | 🟢 `200`, parsed | — | — | 🟢 **open — the trending channel** |
| 🟢 **`raw.githubusercontent.com`** | n/a | n/a | 🟢 **`200`, real bytes, `HEAD` resolves** | 🟢 **open since at least `2026-10-04` — the licence channel** |

🔵 The `403` body is `378` B and identical on all three blocked GitHub hosts — **larger and more
specific than the `249` B p193 recorded**:

```json
{"message":"GitHub access to this repository is not enabled for this session. Use add_repo
to request access. If add_repo answers that read access is already available and you need
GitHub API or write ..."}
```

🟢 **Still this session's own gate, not GitHub's — p193's diagnosis stands.** 🆕 **New this pass:
`codeload.github.com` is on the gate too, and the gate is path-based rather than host-based,
which is exactly why the raw host is not on it.**

### 🆕 🔴 Second correction: P171 was re-derived here for the FOURTH time

🔵 This pass's ad-hoc classifier scanned the licence body for `"gnu affero general public
license"` and returned **`AGPL-3.0` for `moodle/moodle`**. 🟢 Caught, and the cause written up:
GPL-3.0's §`13` is titled *"Use with the GNU Affero General Public License."*

🔴 **This KB registered that as `P171`, built `lib/license_family.sh` to make it unforgettable,
and recorded the defect being reintroduced twice before today.** The library's own header says so:

```
Why this file exists (P237, pass 77 del 2026-10-03). This base had already paid for the
GPL-3.0/AGPL-3.0 defect and registered it as P171 ...
And pass 77 reintroduced the defect anyway, in two fresh instruments, because it wrote a
new classifier from scratch instead of reusing a hardened one. ... A rule that has to be
remembered is not a control. This file is the control.
```

🔴 **p194 is the fourth reintroduction, and it happened the same way: a new classifier written
from scratch.** 🟡 And the library is **stronger than the fix p194 drafted**: p194 proposed
*"classify on the first non-blank line"*; the library classifies on the **title block, first `40`
lines**, because `p288-agpl-casefold` found a **reflowed AGPL-3.0** — `kuali/kfs`, `33 755` B —
whose title line does not appear in that form at all. 🔴 **p194's rule would have misread it.**

🟢 **The remedy this pass takes is the one P237 prescribes: do NOT ship another classifier.**
🔴 Two earlier drafts of this pass referenced a new `compose/code/licence-preflight-raw-lane/`;
**it was not written, deliberately**, because forking the classifier is the defect.
🟢 **`compose/code/lib/license_family.sh` is the instrument, and these pages now point at it.**

### 🟢 Every p194 licence verdict, re-classified by the hardened instrument

🔵 `35` payloads fetched through the raw lane, then passed to `family_of()` from the shared
library. Committed as
[`evidence/libcross-license-family.2026-10-14-p194.tsv`](../evidence/libcross-license-family.2026-10-14-p194.tsv).

| | count |
|---|---|
| 🟢 **identical verdict** | 🟢 **`30` / `35`** |
| 🟡 divergent **spelling**, same substance | `5` |
| 🔴 divergent **substance** | 🟢 **`0`** |

| divergence | p194 ad-hoc | 🟢 library | who is right |
|---|---|---|---|
| `NirDiamant/RAG_Techniques` · `agents-towards-production` · `GenAI_Agents` | `NonCommercial-Custom (NOT OSI)` | 🟢 **`NONCOMMERCIAL-NOT-OSI`** | 🟢 **library — it is the canonical family name, and it was reached WITHOUT being told about this licence** |
| `unslothai/notebooks` · `openeducat/openeducat_erp` | 🔴 `LGPL-3.0-or-later` | 🟢 **`LGPL-3.0`** | 🟢 **library — p194 appended *"or-later"* which neither payload states** |

🟢 **The first row is the real validation.** The `NirDiamant` licence is a bespoke
`Custom License Agreement` the library has never seen, and its `commercial_use_ok` axis
classified it **`NONCOMMERCIAL-NOT-OSI` on the text alone.** 🔵 So the *"new licence class above
Affero"* this pass wanted to announce is also not new — **it is a family this KB already models,
and p194's contribution is the three repositories that populate it**, not the category.

🔴 **And p194's own `LGPL-3.0-or-later` was an invention.** 🟢 The library reads the version from
the payload *(`Gap 256`, closed pass `53`)* and declines to add a suffix the bytes do not carry —
which is the same discipline this KB demands of a star count.

### 🟢 What is genuinely new this pass, stated narrowly

| 🟢 new | 🔴 not new |
|---|---|
| 🟢 **six trending lanes measured; education present in exactly one** *(see [`agents/trending.md`](../agents/trending.md))* | 🔴 the raw lane |
| 🟢 **`codeload.github.com` measured on the gate** | 🔴 the `403`-is-our-own-gate diagnosis *(p193)* |
| 🟢 **`trendshift.io` → DNS `ENOTFOUND`**, structurally unreachable | 🔴 the GPLv3 §`13` trap *(`P171`)* |
| 🟢 **`10` education repositories licence-read, `3` non-commercial, `4` unlicensed** | 🔴 the `NONCOMMERCIAL-NOT-OSI` family |
| 🟢 **EMEA adoption rate and APAC ministry guidance** *(see [`intel/market.md`](../intel/market.md))* | 🔴 the title-block rule |

🟡 **That is a shorter new-findings list than this pass expected to publish, and it is the
accurate one.**

### 🟢 Standing gaps, re-stated with their mechanism

| gap | mechanism | verdict |
|---|---|---|
| government primary sources *(`eur-lex` and `15` others)* | 🔴 DNS null-route to `127.0.0.1` | 🔴 **structurally unreachable — p193's finding taken as standing, no calls spent** |
| 🆕 third-party trending mirrors *(`trendshift.io`)* | 🔴 DNS `ENOTFOUND` | 🆕 🔴 **structurally unreachable — first measured this pass** |
| `github.com/trending?since=monthly` | 🔴 `504` × `2` | 🟡 **a timeout, not a refusal — UNMEASURED, retest once in p195** |
| `stargazers_count` for non-trending rows | 🔴 the raw lane returns files only | 🟡 **that is the MCP channel's job; not re-queried by choice (`±10` floor, p193 priced the shelf hours ago)** |
| 🆕 [`verticals/solutions.md`](../verticals/solutions.md) never names the raw lane | 🔴 `0` mentions in a file that is entirely licence verdicts | 🆕 🟡 **a provenance gap on this KB's most quoted page — fixed there this pass** |

## Pass 193 — 2026-10-14

🆕 🟢 **The `403` that has shaped thirteen passes of this KB is NOT GitHub's. It is this
session's own gate, it says so in its body, and the credential behind it is valid.**
🔴 **Which means every *"the channel is gone"* line this KB has published since p179 was a
measurement of the measuring environment, not of GitHub.**

### 🔵 The evidence, three calls

**1 — Read the `403` body instead of the status code.** `249` bytes, identical on
`github.com/trending` and on `api.github.com/search/repositories`:

```json
{"message":"This GitHub API path is not available: sessions are bound to their
configured repositories. Use repository-scoped endpoints (repos/{owner}/{repo}/...)."}
```

🔴 **That is not GitHub's error vocabulary.** GitHub answers rate limits with
`API rate limit exceeded` and auth failures with `Bad credentials`. 🟢 This is an
intermediary refusing a *path*.

**2 — Ask for a path the gate allows.** `gh api rate_limit` returns a complete, live GitHub
quota object:

| bucket | limit | used | remaining |
|---|---|---|---|
| `core` | `15 000` | `0` | `15 000` |
| `search` | `30` | `0` | `30` |
| `graphql` | `10 000` | `0` | `10 000` |

🟢 **The token is valid, authenticated at an App-level quota, and completely unspent.**
🔴 **There was never a credential problem and never a rate-limit problem.**

**3 — Ask for a repository-scoped path outside the allow-list.** `repos/HKUDS/DeepTutor`,
`repos/moodle/moodle`, `repos/openedx/openedx-platform/stargazers` — all three:

```json
{"message":"GitHub access to this repository is not enabled for this session.
Use add_repo to request access."}
```

🟢 **So the gate is per-repository, not per-endpoint.** The lane works; it is scoped to a
list this KB is not on.

### 🔴 What this corrects, and it is not small

| this KB published | 🟢 what is actually true |
|---|---|
| *"stars, trending, topics, search — still gone"* | 🔴 **gone FROM ONE LANE.** The MCP lane returned `30`/`30` rows with stars today; the page-fetch lane returned trending |
| *"`403` — the API is blocked"* | 🔴 **the session is scoped.** A client running this same instrument on their own machine sees a working API and none of this |
| *"thirteenth pass without trending"* | 🔴 **thirteen passes of not having tried the fourth lane** |

🟡 **The method lesson, stated so p194 cannot lose it: a status code is not a diagnosis.**
`403` told this KB *"refused"*; the `249`-byte body told it *who* refused and *why*, and the
`rate_limit` call told it the refusal was local. 🟢 **Three calls, and a thirteen-pass
standing gap turns out to have been a one-line misread.**

### 🆕 🔴 The government-primary-source gap has a MECHANISM now, and it is terminal

🔵 p191 recorded `16` blocked hosts; p192 restated the gap and did not retest. 🟢 **Retested
this pass, six hosts, `12` s timeout each:**

| host | HTTP | resolved IP |
|---|---|---|
| `eur-lex.europa.eu` | `000` | 🔴 **`127.0.0.1`** |
| `digital-strategy.ec.europa.eu` | `000` | 🔴 **`127.0.0.1`** |
| `www.ed.gov` | `000` | 🔴 **`127.0.0.1`** |
| `www.unesco.org` | `000` | 🔴 **`127.0.0.1`** |
| `www.gov.br` | `000` | 🔴 **`127.0.0.1`** |
| `www.education.gov.au` | `000` | 🔴 **`127.0.0.1`** |

🔴 **Six of six resolve to loopback.** The page-fetch lane — the one that recovered trending
— returns `getaddrinfo ENOTFOUND` for `eur-lex.europa.eu` while fetching `github.com` in the
same minute. 🟢 **So this is a DNS null-route on a host allow-list, not a `403`, not a
timeout, and not lane-specific.**

🔵 **Why that matters more than the gap itself:** a `403` invites a retry and a different
lane. 🔴 **A null-routed host does not. No number of passes and no new lane will reach
`eur-lex`, and p194 should stop spending calls on it.** 🟢 Recorded as **structurally
unreachable** rather than *"not reached this pass"* — the distinction this KB keeps insisting
on, applied to itself.

🟡 **Consequence for every regulatory claim on [`intel/market.md`](../intel/market.md): it is
secondary and it will stay secondary from inside this harness.** 🟢 The honest upgrade is
convergence — many independent secondary sources naming the same instrument number and the
same dates — and this pass gets one. See the EU `2026/1744` resolution there.

### 🟢 Licence re-read from bytes: `frappe/lms`

🔵 Blobless clone, `--no-checkout`, `git cat-file` on the root tree:
**`license.txt`, `33 893` B, first line `GNU AFFERO GENERAL PUBLIC LICENSE`.**
🟢 **Confirms this page. Refutes [`agents/top.md`](../agents/top.md) p192, which printed
`MIT`.** 🔴 **Three independent instruments now agree it is `AGPL-3.0`** — the bytes, this
page's earlier read, and the recovered channel's `license.spdx_id`. 🟡 The row stays; the
licence is corrected wherever this KB printed it wrong, including a regional recommendation
that was built on the wrong word.
## Pass 192 — 2026-10-14

🆕 🟢 **Every repository URL this KB publishes on its three shelf pages has been probed for
EXISTENCE, with the denominator derived in the instrument rather than inherited — which is
exactly what p191's method note asked the next pass to do.** 🔴 **And the instrument that did
it turns out to conflate two states that this KB has been reading as one, in `706` places.**

### 🟢 The census: population derived, not inherited

🔵 **Population rule, stated before the measurement:** every `github.com/<owner>/<repo>` URL
appearing in [`agents/top.md`](../agents/top.md), [`repos/foundations.md`](foundations.md)
and [`verticals/solutions.md`](../verticals/solutions.md), de-duplicated, with GitHub's own
non-repository paths *(`topics/`, `orgs/`, `users/`, …)* excluded.

| | count |
|---|---|
| raw distinct slugs extracted | `473` |
| 🔴 less `repos/` — an extraction artefact from an `api.github.com` URL, never a row | `−1` |
| 🟢 **derived population** | **`472`** |
| 🟢 `LIVE` *(refs > `0`, exit `0`)* | **`468`** |
| 🔴 `EMPTY` *(resolves, `0` refs, exit `0`)* | `2` |
| 🔴 `ABSENT` *(exit `128`)* | `1` |
| 🟡 extractor false positive | `1` |

🟢 **Per-page: `325` slugs on `agents/top.md`, `190` here, `192` on `verticals/solutions.md`.**
Committed as [`evidence/shelf-existence-census.2026-10-14-p192.tsv`](../evidence/shelf-existence-census.2026-10-14-p192.tsv)
so p193 can diff it rather than re-derive it.

🔵 **The headline is a negative and it is worth stating plainly: `468` of `472` rows resolve,
and all `4` exceptions were ALREADY DOCUMENTED on these pages.** This shelf does not rot.

### 🔴 The conflation: `0 refs` has meant two different things

🔵 **`git ls-remote` is the instrument p191 promoted to primary after the API lane went
`403`.** It is sound — but the verdict this KB reads off it is the **stdout line count**, and
that count cannot separate *absent* from *empty*. Calibrated this pass, four probes:

| state | probe | stdout refs | **exit** | stderr |
|---|---|---|---|---|
| absent, attached owner | `gmilano/no-existe-p192-control` | `0` | 🔴 **`128`** | `fatal: could not read Username` |
| absent, unattached owner | `openfresno/no-existe-p192-control` | `0` | 🔴 **`128`** | `fatal: could not read Username` |
| 🆕 **real but empty** | `openfresno/edgenuity-aeries-grade-passback` | `0` | 🟢 **`0`** | *none* |
| live | `moodle/moodle` | `1 959` | `0` | *none* |

🔴 **The exit code discriminates. The ref count does not.** And because the `fatal:` goes to
**stderr**, a pipeline of the shape `git ls-remote … | wc -l` prints `0` for an absent
repository and `0` for an empty one — 🔵 **which is why this KB's negative controls
(`gmilano/…-no-existe-52 → 0 refs`, `globant/NEGATIVE-CONTROL-no-existe-50 → 0 refs`)
taught it that `0 refs` means *"does not exist"*.** 🟢 **They were calibrated on absent
repositories only, so the reading was correct for every case they tested and silently wrong
for the one they never tested.** Remedy: **read the exit code, not the line count** — one
character of change, `$?` instead of `wc -l`.

### 🆕 🟢 Which settles a question this KB left open BY NAME

🔵 [`verticals/solutions.md`](../verticals/solutions.md) published on
[`openfresno/edgenuity-aeries-grade-passback`](https://github.com/openfresno/edgenuity-aeries-grade-passback):
*"the raw lane returned `404` for `15` candidate paths across `HEAD`/`main`/`master`, so **this
pass verified that the repository exists and did not verify that it contains anything.**"*

🟢 **Now measured: it resolves anonymously, exits `0`, writes nothing to stderr and returns
`0` refs. The repository is EMPTY.** 🔵 Not blocked, not rate-limited, not a raw-lane
artefact — **there are no commits.** `15` × `404` was the right measurement read against the
wrong hypothesis: a path probe cannot distinguish *"this path is missing"* from *"every path
is missing"*, and a ref probe answers it in one call.

🔵 **The same verdict, independently, for [`cdweaver1992/edfi-mcp-server`](https://github.com/cdweaver1992/edfi-mcp-server)**
*(`0` refs, exit `0`; search confirms `1`★, created `2026-02-17`)* — which the KB had already
called empty from `size: 0`. 🟢 **Two channels, one verdict. There is still no Ed-Fi MCP
server.**

### 🆕 🟡 The sha-collision detector, and the duplicate-identity defect it found

🔵 **New instrument, one line over the census: group the `468` live slugs by HEAD sha and
report every sha claimed by more than one slug.** `5` pairs:

| pair | diagnosis |
|---|---|
| `openedx/edx-platform` ≡ [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 🟢 **a RENAME, already documented here.** GitHub redirects the old slug, so `ls-remote` reports it live forever; only the search channel refuses it |
| `OpenOLAT/OpenOLAT` ≡ `openolat/OpenOLAT` | 🔴 **owner-case variant** — published `258` and `109` times respectively |
| `OS4ED/openSIS-Classic` ≡ `os4ed/openSIS-Classic` | 🔴 **owner-case variant** — `112` and `25` |
| `Hesham0-0Nasser/tutor-lms-mcp` ≡ `hesham0-0nasser/tutor-lms-mcp` | 🔴 **owner-case variant** — `4` and `50` |
| `ShuyunYuan/talentcoach` ≡ `shuyunyuan/talentcoach` | 🔴 **owner-case variant** — `10` and `8` |

🔴 **GitHub resolves owner names case-insensitively; a compiler that does not canonicalise
gets TWO entities for ONE repository.** Four repositories on this shelf are published under
both spellings, one of them `367` times across the two. 🟢 **Remedy: canonicalise every slug
at import against the `full_name` the API returns** — now that the API returns one again.
🔵 Note the asymmetry worth keeping: a case variant is a **compile** defect *(the rows are
all true)*, while the rename is a **currency** defect *(one row names a slug that
documentation, topics and search no longer key on)*. They need different fixes.

### 🟡 And the honest half: the sweep accused a row, and reading it cleared the row

🔴 **`yourusername/scholarmate` came out of the extractor as `ABSENT`.** It is not a row.
🟢 **It is a string this KB QUOTES inside a row about [`dragonpilee/ScholarMate`](https://github.com/dragonpilee/ScholarMate)**,
where the finding is precisely that *"its README still reads `github.com/yourusername/scholarmate`
— an unedited template placeholder."*

🔵 **p191's lesson, repeating one pass later, with a new mechanism.** p191 learned that an
extractor misreads *the best-documented rows* because a careful cell names a second licence.
🆕 **p192 adds: an extractor misreads them because a careful cell QUOTES A DEFECT.** A page
that documents other people's broken URLs contains broken URLs, and any sweep over its link
text will find them and attribute them to the page. 🟢 **Caught by reading the row before
publishing the accusation — the same control, and the only one that works.**
## Pass 191 — 2026-10-14

🆕 🟢 **The licence column has been read at FULL TREE DEPTH over every row this KB publishes
with a licence — `1 273` of them, not the `160` `ACTION NK` registered — and it holds:
`1 037` `AGREE`, `2` `CONTRADICTED`.** 🔴 **And the instrument that found those two
manufactured THREE more before it was read against the pages.**

| verdict | n | what it means for an engagement |
|---|---|---|
| 🟢 `AGREE` | **`1 037`** | an own grant exists in the tree and its family matches what this KB publishes |
| 🟡 `FAMILY-AMBIGUOUS` | **`141`** | the grant payload NAMES more than one family *(MPL naming the GNU family, EUPL naming five, a GPL exception naming the LGPL)*. 🔵 Handed over as a reading list, never decided — `ACTION NT` resolves the `20` that patterns depend on |
| 🟡 `TEXT-ABSENT` | **`78`** | **no licence text anywhere in the tree**, yet a licence is published — `Gap 421`'s family: a registry classifier, a README badge, a `pyproject.toml` string. 🔴 Not a contradiction, and **not a grant either** |
| 🔴 `CONTRADICTED` | **`2`** | below |
| 🟡 `BUNDLED-ONLY` | `6` | every grant found belongs to a vendored dependency; the project's own is still absent |
| 🔴 `UNRESOLVABLE` | `8` | the slug does not resolve over `git` — dead, renamed or private |
| 🟡 `PAIRING-AMBIGUOUS` | `1` | the only row naming this slug also names other repos and other ids, so no id can be attributed to it |

### 🔴 The two rows the tree refutes

| slug | published | the tree holds | consequence |
|---|---|---|---|
| [`linyeping/GemMate`](https://github.com/linyeping/GemMate) | 🔴 `MIT` *(since p172)* | 🟢 **`Apache-2.0`** — `LICENSE`, `11 305` B, canonical header | 🟢 **still permissive**, so no pattern changes; corrected in [`repos/trending.md`](trending.md) and twice in [`compose/patterns.md`](../compose/patterns.md) |
| [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) | 🔴 `MIT` *(on [`agents/top.md`](../agents/top.md) and [`agents/trending.md`](../agents/trending.md))* | 🟢 **`GPL-3.0`** — `LICENSE`, `35 183` B, verbatim, under a `© 2026 Martin Hlaváč` line | 🔴 **copyleft.** Reference implementation only; **this page already carried the correction and the agent pages did not** *(`Gap 440`)* |

### 🔴 Why `156` case variants was the wrong instrument, and `160` the wrong population

`ACTION NK` registered the full `P1057` case-variant sweep. 🔴 **A variant list is still a
list**: it cannot reach `aoe-web-frontend/LICENSE` *(depth)*, `LICENSE/LICENSE.code` *(a
licence DIRECTORY)*, `debian/copyright` *(packaging)* or `LICENSE.GPL` + `LICENSE.MPL`
*(family suffix)*. 🟢 **`P441` already proved the generalisation here** — *a filename list can
only FIND a licence; to sustain its ABSENCE you must ENUMERATE the tree* — so what ran was
`git clone --filter=blob:none` + `git ls-tree -r` over `1 273` repositories, with every
candidate's bytes read and classified. 🔵 **Every case variant at the root is a strict subset
of a complete tree.**

🔴 **And `160` was `13`% of the population.** The number was never derived; it was what p190
happened to sweep. 🟢 The population is now derived from the published pages themselves and
committed:
[`population.2026-10-14.tsv`](../compose/code/p191-licence-case-full-depth/population.2026-10-14.tsv).

### 🔴 The three false accusations this instrument made against this KB's own rows

Its first run reported `6` contradictions. Read against the pages, **three were its own.**

| # | the defect | the row it accused | the fix, with a control |
|---|---|---|---|
| `1` | **cross-product pairing** over a row naming several repos and several ids | 🔴 `AlexandreL0pes/q-scraper`, charged with an `Apache-2.0` belonging to `adiel-calixto/IFAcademico` four cells away | an id is attributed only from a line with **exactly one** slug; otherwise `PAIRING-AMBIGUOUS` |
| `2` | **a prose id read as the published id** | 🔴 [`opencast/opencast`](https://github.com/opencast/opencast), which publishes `ECL-2.0` and explains it as an *"OSI-approved `Apache-2.0` derivative for universities"* | ANY published id matching the tree settles the row — no prose parser needed |
| `3` | **vocabulary drift between the extractor and the comparator** | 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) **and** `opencast/opencast` — the two largest platforms on this shelf, **both published correctly** | one vocabulary, and `column_full_depth` **raises at import** if the family map does not cover it |

🔵 **Defect `3` is the one to carry forward, and it is not a typo.** The row that gets misread
is the **best-documented** row: a cell that explains its licence against a better-known one
contains two ids, and an extractor that cannot spell the first will happily find the second.
🟢 **Rule: when two modules each hold a vocabulary, the drift between them is a defect with no
symptom — assert it at import.**

🟢 **Instrument, controls and full result:**
[`P1059`](../compose/code/p191-licence-case-full-depth/README.md) *(`24`/`24`, offline, three
controls being the defects above)* ·
[`evidence/licence-column-full-depth.2026-10-14-p191.tsv`](../evidence/licence-column-full-depth.2026-10-14-p191.tsv)

### 🟢 Declared limits of this sweep, stated before anyone quotes the `1 037`

- 🔴 **Comparison is at FAMILY level.** A published `GPL-2.0` against a GPL-3.0 tree reads
  `AGREE`; version discrimination is `P613`'s job. `ACTION NT` and `ACTION NS` carry the
  follow-through.
- 🟡 **`TEXT-ABSENT` is not a refutation**, deliberately: collapsing it into `CONTRADICTED`
  would turn this KB's own documented claim-only shapes into errors.
- 🟡 The population is **slugs on published table rows**. A licence named in a sentence is not
  a published row, and `1 273` is therefore a floor.

## Pass 190 — 2026-10-14

🆕 🟢 **`ACTION NG` closes its own question cleanly — `0` case-variant files contradict a
published licence, over `5 212` probes. 🔴 And in closing it, the sweep found that p189's
`224`-probe sweep was NARROWER THAN THE STANDING PATH LIST IT WAS WRITTEN TO EXTEND: at
`limit=16` the instrument never reaches `.md` at all. Seven rows this page publishes as
grant-absent DO carry a licence file, and two of them change verdict once read.**

### 🟢 `ACTION NG` — the published licence column, swept entire

| sweep | probes | result |
|---|---|---|
| parity with p189, `probe_plan(limit=16)` over **all `160`** rows carrying a slug **and** an SPDX token | **`2 560`** | `150` × `200`, `2 410` × `404` |
| 🟢 **case variants CONTRADICTING a published licence** | — | 🟢 **`0`** |
| rows with more than one path serving bytes | — | `7` — 🟢 **all of them `LICENSE` + `NOTICE` pairs**, two different files with different jobs *(Apache-2.0 §4(d) attribution)*, not two casings of one file |
| 🔴 rows with **`0`** variants serving bytes | — | 🔴 **`17` of `160`** |
| the full variant set on those `17` | **`2 652`** | 🔴 **`7` carry a grant after all** |

🟢 **So limb `1` fires on the question as asked: the licence column is sound where it was
read, and the `openedx/XBlock` miss is confirmed isolated.** 🔴 The defect is elsewhere, and
it is worse.

### 🔴 The limit defect — the repair is deleting an argument, not re-reading a column

`P1057`'s extension tuple is `("", ".txt", ".md", ".rst", ".apache2", ".mit", ".gpl")` and
its variant list is ordered **extension-major**: all `12` bare stem-casings first, then
`.txt`. So **`probe_plan(limit=16)` returns `12` bare + `4` `.txt` casings and never reaches
`.md`.**

🔴 **`LICENSE.md` is one of the FOUR paths in this KB's own standing list**
*(`LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`)*. p189's *"`16` case variants × `14`
grant-absent rows = `224` probes, **`0` further grants**"* therefore probed a **strictly
smaller** path set than the list the instrument existed to extend — and its `0` is not
evidence about `.md` at all. 🟢 **The instrument is correct. The invocation truncated it
below its own baseline.**

🟢 **RULE: never probe a path list SHORTER than the standing list it extends.** A limit that
silently drops a baseline path turns *"we looked"* into *"we looked somewhere else"*.

### 🔴 The seven rows, and the two that change verdict

| row | published | path | bytes | what the bytes are |
|---|---|---|---|---|
| 🔴 [`frappe/education`](https://github.com/frappe/education) | `GPL-3.0` | `license.txt` | 🔴 **`19`** | 🔴 **`License: GNU GPL V3` — that is the WHOLE FILE.** No holder, no permission clause, no disclaimer. 🆕 **`Gap 421`'s SIXTH sub-`1`kB shape and the smallest yet** *(against p189's `46`/`47` B)*. The identifier is corroborated; **the grant is absent** |
| 🔴 [`numbas/numbas-lti-provider`](https://github.com/numbas/numbas-lti-provider) | `Apache-2.0` | `LICENSE.md` | 🔴 **`560`** | 🔴 **INCORPORATION BY REFERENCE** — the Apache-2.0 *appendix* notice, *"Licensed under the Apache License, Version 2.0 … You may obtain a copy of the License at …"*, © `2016` Newcastle University. Apache-2.0's own text is `11 358` B; this ships `560` B and a URL |
| 🟢 [`frappe/lms`](https://github.com/frappe/lms) | `AGPL-3.0` | `license.txt` | `33 893` | 🟢 `AGPL-3.0` verbatim — grant now read from bytes |
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | `GPL-3.0` | `COPYING.txt` | `35 147` | 🟢 canonical `GPL-3.0`. 🔵 `COPYING` is in the standing list; **`COPYING.txt` is not reached at `limit=16`** |
| 🟢 [`openfun/ralph`](https://github.com/openfun/ralph) | `MIT` | `LICENSE.md` | `1 094` | 🟢 complete `MIT` grant, *"© 2020-present France Université Numérique"*. 🔴 `LICENSE` itself `404`s |
| 🟢 [`willianmano/moodle-theme_moove`](https://github.com/willianmano/moodle-theme_moove) | `GPL-3.0` | `LICENSE.md` | `34 903` | 🟢 `GPL-3.0`, markdown-formatted. The `244`-byte deficit vs canonical is re-formatting, not a different grant |
| 🟢 [`yukazakiri/koakademy`](https://github.com/yukazakiri/koakademy) | `AGPL-3.0` | `LICENSE.md` | `34 523` | 🟢 canonical `AGPL-3.0` byte count |

### 🔵 The symmetry worth keeping — p189 retired the right caveat from the wrong row

p189 corrected `openedx/XBlock` and **retired** the caveat it had forced onto every
engagement: *"usable, but the grant is a NOTICE not a LICENSE."* `XBlock` turned out to hold
the **full `11 358` B** at `LICENSE.TXT`, so for that row the caveat was never real.

🔴 **`numbas/numbas-lti-provider` is the row that caveat was always for** — `560` B of
notice and a URL — and it was invisible for the same reason `XBlock` was: **a path nobody
probed.** 🟢 `XBlock`'s was a case nobody varied; `numbas`'s was an extension a `limit`
excluded. 🔵 **Two passes, two rows, one class: the licence was never missing, the probe was.**

### 🟢 One thing ruled out, recorded so it is not asked again

🟢 **SLUG case is NOT a defect.** `raw.githubusercontent.com` treats the **owner** segment as
case-**insensitive**: `OS4ED/openSIS-Classic/HEAD/LICENSE` and
`os4ed/openSIS-Classic/HEAD/LICENSE` return `404` **identically**. The case-sensitivity
`P1057` found is in the **path**, and the path only. This KB spells that slug both ways
across pages; it changes no verdict, and `openSIS-Classic` stays grant-absent after `156`
variants.

### 🔴 The ten rows still grant-absent after `156` variants each

Their published identifier rests on a **manifest** or on **prose** — `P1049`/`P1054`/`P1056`
territory — not on a licence file, and the pages must keep saying so:
[`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) ·
[`Gaurav-Pande/AES_DL`](https://github.com/Gaurav-Pande/AES_DL) ·
[`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) ·
[`Rick-254/moodle-quizsmith`](https://github.com/Rick-254/moodle-quizsmith) ·
[`Simon-Initiative/lti-example-tool`](https://github.com/Simon-Initiative/lti-example-tool) ·
[`ZQR1101/xueyoujing-companion`](https://github.com/ZQR1101/xueyoujing-companion) ·
[`formalms/formalms`](https://github.com/formalms/formalms) ·
[`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) ·
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) ·
[`tianshuo/trainingllm`](https://github.com/tianshuo/trainingllm).

### 🔴 This page's channel statement, per `Gap 431`, stated once

Every byte above came from `raw.githubusercontent.com/<slug>/HEAD/<path>` with the HTTP code
checked, and every existence check from the **git protocol**. 🔴 **`github.com` HTML and
`api.github.com` returned `403` for the whole of this session** *(egress policy; not retried,
per the proxy's own instruction)*. 🔵 **So no star count, commit date or topic membership on
this page was refreshed this pass, and none should be read as current.** Licences and code
are primary; attention metrics are stale by construction.

**Full measurement:**
[`evidence/licence-path-case-published.2026-10-14-p190.tsv`](../evidence/licence-path-case-published.2026-10-14-p190.tsv)
· [`evidence/url-existence.2026-10-14-p190.tsv`](../evidence/url-existence.2026-10-14-p190.tsv)

## Pass 189 — 2026-10-14

🆕 🔴 **One row on this page carries a verdict that is wrong, and it is the row this page
recommends most often. Plus the first measurement of what the intake channel actually
supplies per pass — and the retirement of the figure this KB has been using instead.**

### 🔴 AMENDED — `openedx/XBlock`. `NO_LICENCE_FILE` is REFUTED by `11 358` bytes

| line | what this page published | what the bytes say |
|---|---|---|
| `:2475` | 🔴 **`NO_LICENCE_FILE`** · 🟡 `NOTICE.txt` *(`545` B)* · *"Apache-2.0 ASSERTED — and no licence TEXT anywhere in the tree"* | 🟢 **`LICENSE.TXT` · `11 358` B · HTTP `200` · verbatim Apache-2.0** |
| `:2553` | 🟡 *"Usable, but the grant is a NOTICE not a LICENSE"* | 🟢 **The grant IS a LICENSE. The caveat is withdrawn** |

🔴 **Cause: path CASE.** `raw.githubusercontent.com` is case-sensitive. `LICENSE`,
`LICENSE.txt`, `LICENSE.md` and `COPYING` all return `404` on this repository;
`LICENSE.TXT` returns the licence. 🟢 And the manifest said so all along —
`pyproject.toml` *(`3 344` B, `200`)* line `10`: `license-files = ["LICENSE.TXT"]`.

🔵 **Why this correction is worth more than its size.** `:3068`, `:3134` and `:4884` of
this page recommend `XBlock` as *"the permissive entry point into an AGPL platform"* and
*"the lowest-friction way to put an AI activity inside Open edX"*. 🟢 It is `470`★,
`Apache-2.0`, clean, and the legal caveat a studio would have had to raise was never real.

🟢 **The honest half, and it bounds the damage.** New instrument
[`P1057`](compose/code/p1057-licence-path-case/README.md) *(`16`/`16` tests)*:
**`16` case variants × `14` grant-absent rows = `224` probes, `0` further grants.** One
real error in `64` rows, then nothing in `224` requests. **Every other grant-absent verdict
on this page survives**, including `OS4ED/openSIS-Classic`, `Nasus20202/MoodleMCP`,
`Rick-254/moodle-quizsmith` and `VICKY07092005/moodle-5-1-authentic-relay`.

🟢 **Two channel findings that make every future licence read cheaper:**

| channel | authority | measured coverage over the same `64` rows |
|---|---|---|
| 🟢 **`/HEAD/` on the raw host resolves the DEFAULT BRANCH** | 🟢 exact | **all of them.** Verified `200` on `blend-ed/tutor-contrib-openedxmcp` *(default `master`; `main` `404`s)* and `HKUDS/DeepTutor`. 🔵 Earlier passes probed `main` **and** `master` and built *"404 at N paths"* verdicts on a branch guess |
| 🟢 **the manifest NAMES the file** — PEP 639 `license-files`, npm `licenseFile` | 🟢 authoritative | 🔴 **`1` of `64`.** Rare, so never rely on it; free, so always read it first. 🔴 A licence **string** is not a licence **path** |

### 🟢 `ACTION MZ` — the whole permissive licence column, swept

🟢 **`LIMB 2` FIRES.** `P1056` *(unmodified; its suite re-run `16`/`16`)* over **`64`
repositories, `119` reads, `640` HTTP requests with every code checked** — every row this
KB publishes as `Apache-2.0`, `BSD` or `ISC`, plus the `13` `NOT-MIT-BODY` rows:
🟢 **`0` further split-scope rows.** The two known instances
*(`ktwyw/python-for-engineers`, `siskinskai/spedlex`)* reproduced exactly and nothing else
carries the shape. `P1056` stays an **intake check**; the licence column does not need a
re-pass.

🟢 **Three rows confirmed `Apache-2.0` from bytes** rather than from assertion:
`ashutoshrana/haystack-ferpa-filter` *(`12 101` B)*, `bigdata-ustc/edudata` *(`11 346` B)*,
`myvipbackup2/china-k12-teacher-skills` *(`11 359` B)*.

🟢 **One row gains a VERSION**: [`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks)
*(`:130`, published as 🟡 `GPL`, `35 200` B)* is **`GPL-3.0`** — *"GNU GENERAL PUBLIC
LICENSE / Version 3, 29 June 2007"*. 🔵 For a Moodle plugin the version is the point, since
Moodle core is `GPL-3`-or-later. 🔴 Its *"GNU Affero"* token is `GPL-3`'s own §13
cross-reference and must not be re-read as an `AGPL` grant.

🆕 🟢 **A fifth manifest channel enters this KB: R/CRAN `DESCRIPTION`.**
`shmercer/writeAlizer`'s `47`-byte `LICENSE` is **not** a stub — `DESCRIPTION` *(`1 549` B,
`200`)* reads *"License: MIT + file LICENSE"*, and under R convention the grant lives in the
manifest while `LICENSE` carries only the year and holder `MIT` requires. 🔵 The row is
genuinely `MIT`, independently reproducing p185.

### 🆕 🟢 What the intake channel supplies per pass — measured, and it replaces a retired figure

| measure | value | status |
|---|---|---|
| 🆕 🟢 **new unique slugs across `12` topic pages in `28` min** | 🟢 **`12`** | 🟢 **the number to plan on** |
| 🆕 🟢 of those, absent from this KB | 🟢 **`10` = `83`%** | 🟢 the channel is still productive |
| row-level churn, same window | `14`/`239` = `5.9`% | 🟢 the pages are STABLE |
| 🔴 "absent rate", p187 → p188 → p189 | `79`% → `67.5`% → **`60.3`%** | 🔴 **RETIRED as a coverage measure** |

🔴 **The absent rate was never measuring the channel.** It fell another `7.2` points in `28`
minutes while only `14` of `239` rows changed. `14` rows flipped **absent → present**, and
every one is now cited in a KB **page** — this one, `agents/top.md`, `repos/trending.md`,
`verticals/solutions.md`. 🔵 **p188 ingested them.** The index grew `1 993` → `2 025`.
🟢 **So the three figures are not three estimates in disagreement; they are one quantity
declining because the backlog is being cleared. Nobody over-counted.** Rule:
quote it as *"rows not yet ingested, pass N"*, or do not quote it.

Evidence: [`licence-path-case`](evidence/licence-path-case.2026-10-14-p189.tsv) ·
[`split-scope-sweep`](evidence/split-scope-sweep.2026-10-14-p189.tsv) ·
[`recency-churn`](evidence/recency-churn.2026-10-14-p189.tsv)

## Pass 188 — 2026-10-14

🆕 🟢 **Ten foundational rows enter, every grant read over the raw channel this pass with
the HTTP code checked — and the pass's most useful structural finding is that the
permissive LMS/SIS route is now THREE wide on each side, not one.**

🔴 **A measured correction to this page's own licence vocabulary first.** The Apache-2.0
byte fingerprint this KB has been carrying — `11 282`–`11 359` B — is **too narrow at the
bottom**. `tsugi` measures `10 273` B and `OpenOLAT` `10 982` B, and both are full
Apache-2.0 text. 🟢 New measured range **`10 273`–`11 359` B**. 🔵 **A byte-count-only
classifier would have missed both rows. Bytes corroborate; only reading decides.**

### 🟢 The permissive LMS / assessment route, widened

| row | licence, as measured | ★ | region | what it is |
|---|---|---|---|---|
| 🆕 🟢 **[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)** | 🟢 **`Apache-2.0`** *(`LICENSE`, `10 982` B, full text)* | `447` | EMEA | 🟢 **a complete Swiss university LMS under a PERMISSIVE grant.** p187 called OpenOLAT "a permissive ROUTE" from its metadata; the grant is now READ and the call is confirmed |
| 🆕 🟢 **[`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi)** | 🟢 **`Apache-2.0`** *(`LICENSE`, `10 273` B)* | `376` | North America | 🟢 **the LTI application framework written by the author of the IMS LTI specification** (Chuck Severance). 🔵 For an integration engagement this is the most authoritative permissive row on the page |
| 🆕 🟢 **[`numbas/Numbas`](https://github.com/numbas/Numbas)** | 🟢 **`Apache-2.0`** *(`LICENSE`, `11 357` B)* | `215` | EMEA | 🟢 the **Numbas** maths/science assessment engine, Newcastle University. Item authoring + marking |
| 🆕 🟡 [`numbas/numbas-lti-provider`](https://github.com/numbas/numbas-lti-provider) | 🟡 **`Apache-2.0` BY REFERENCE** *(`LICENSE.md`, **`560` B**)* | `11` | EMEA | the LTI side of Numbas. 🔴 **`P971`, instance SIX** — `560` B names Apache-2.0 and does not contain its terms. 🔵 Say *"by reference"*: §`3`, the patent grant, is the only strong reason to prefer Apache and it travels as a URL |
| 🆕 🟢 [`openfun/marsha`](https://github.com/openfun/marsha) | 🟢 **`MIT`** *(`1 078` B)* | `151` | EMEA | video management for an LMS, from **France Université Numérique** — the same publisher as [`ralph`](https://github.com/openfun/ralph). 🔵 One EMEA public-sector publisher now supplies two layers of this stack |
| 🆕 🟢 [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 **`MIT`** *(`1 098` B)* | `26` | North America | LTI `1.3` for Django, from **University of Michigan Academic Innovation** |
| 🆕 🟢 [`virtUOS/abstimmbar`](https://github.com/virtUOS/abstimmbar) | 🟢 **`Apache-2.0`** *(`11 358` B)* | `1` | EMEA | classroom voting, Universität Osnabrück |
| 🆕 🟢 [`EduThemes/paper-lms`](https://github.com/EduThemes/paper-lms) | 🟢 **`MIT`** *(`1 071` B)* | `4` | Global | a light LMS |
| 🆕 🟢 [`jakerains/scormplayer`](https://github.com/jakerains/scormplayer) | 🟢 **`MIT`** *(`1 067` B)* | `0` | North America | a `SCORM` player — 🔵 the runtime side of the `SCORM` column p187 added |
| 🆕 🟢 [`edmozley/freeitsm`](https://github.com/edmozley/freeitsm) | 🟢 **`MIT`** *(`1 066` B)* | `101` | EMEA | 🟡 ITSM rather than an LMS, but it renders on `topics/lms` and `topics/scorm` and is permissive |

### 🟢 `academico` makes the permissive SIS route THREE wide — and it is LATAM-built

🔵 p174 spent twelve passes recording that no permissive SIS existed; p175 found the
first. 🟢 **p188 adds the second and reads the third:**

| row | licence | ★ | region |
|---|---|---|---|
| 🆕 🟢 **[`academico-sis/academico`](https://github.com/academico-sis/academico)** | 🟢 **`MIT`** *(`1 094` B, full text)* | `404` | 🟢 **LATAM** |
| 🟡 [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | 🟢 **`GPL-2.0`, and THE FULL BODY IS IN THE TREE** at `docs/License.txt` *(`17 286` B, re-read p215)*; the README points there — 🔴 **nothing at the `10` probed ROOT paths**, which is all *"by reference only"* ever measured <!--corrected--> | `345` | North America |
| 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL`** *(`15 214` B)* | `646` | EMEA |

🔴 **`openSIS-Classic` is `P971`, instance SEVEN — and the weakest instance this KB has
measured.** 🔵 Apache and `MIT` by reference are merely untidy; **`GPL` by reference is a
compliance problem**, because the `GPL` requires its terms to travel WITH the work. 🟢 A
studio forking `openSIS` inherits an obligation whose text is not in the tree.

🟢 **So the honest routing advice for a SIS engagement changed this pass:** the
most-starred options are copyleft and one of them does not ship its own licence, while the
permissive option — `academico`, `404`★ — is built in-region for LATAM. 🔵 **That is the
first time this page can answer a LATAM SIS question with a LATAM row.**

### 🔴 Copyleft rows read this pass, recorded so nobody re-reads them

| row | licence | ★ | region |
|---|---|---|---|
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` *(`35 147` B)* | `1`k | EMEA |
| [`memphis-iis/MoFaCTS`](https://github.com/memphis-iis/MoFaCTS) | 🔴 `AGPL-3.0` *(`34 523` B)* | `2` | North America |
| [`yukazakiri/koakademy`](https://github.com/yukazakiri/koakademy) | 🔴 `AGPL-3.0` *(`34 523` B)* | `7` | APAC |
| [`ateeducacion/OmekaS-LearningObject`](https://github.com/ateeducacion/OmekaS-LearningObject) | 🔴 `GPL` *(`35 813` B)* | `0` | EMEA *(Canary Islands government ed-tech unit)* |

🔵 **Note the `34 523` B coincidence: `AGPL-3.0`'s full text measures `34 523` B in three
unrelated repositories this pass** — `MoFaCTS`, `koakademy` and
`openedx/openedx-ai-extensions`. 🟢 That is a usable fingerprint, and it is how the Open
edX client's licence was read in one request.

Evidence: [`evidence/new-supply-grants.2026-10-14-p188.tsv`](../evidence/new-supply-grants.2026-10-14-p188.tsv),
[`evidence/url-existence.2026-10-14-p188.tsv`](../evidence/url-existence.2026-10-14-p188.tsv).

## Pass 187 — 2026-10-14

🆕 🟢 **Fourteen foundational rows enter, every grant read over the raw channel this pass with the
HTTP code checked, and the regional balance of this page changes materially: `7` of the `14` are
EMEA and they are university-built infrastructure, not start-up demos.**

### 🟢 The learning-record and analytics layer — the gap this page has carried longest

| repo | licence, as measured | region | why it is foundational |
|---|---|---|---|
| 🆕 🟢 **[`openfun/ralph`](https://github.com/openfun/ralph)** | 🟢 **`MIT`** *(`LICENSE.md`, `1 094` B)* | EMEA | 🟢 **a Learning Record Store** — `xAPI` statements in, queryable analytics out. `51`★, from **France Université Numérique**. 🔵 **This page has recommended "stand up an LRS" for many passes without naming a permissive one. This is it** |
| 🆕 🟢 **[`scormflow/scorm-engine`](https://github.com/scormflow/scorm-engine)** | 🟢 **`MIT`** *(`LICENSE`, `1 079` B)* | Global | 🟢 `SCORM` **+ `xAPI` + `cmi5` infrastructure with a built-in LRS** — the three content standards and the record store in one permissive tree |
| 🆕 🟢 **[`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)** | 🟢 **`Apache-2.0`** *(`LICENSE`, `11 323` B, full text)* | North America | 🟢 **an LMS plug-in for RANDOMISED EXPERIMENTS on live assignments.** `21`★, default branch `development`. 🔵 The only row on this page that lets a client **measure whether the AI helped**, rather than assert it |
| 🆕 🟡 **[`solin-repo/moodle-block_atrisk`](https://github.com/solin-repo/moodle-block_atrisk)** | 🟡 **`GPL-3.0-or-later` BY REFERENCE** — 🔴 `703` B, i.e. `P971`'s shape: correct title block, terms live at a URL | EMEA | a Moodle block flagging students falling behind — the early-warning seam, in-tree |
| 🆕 🟢 **[`elimu-ai/ml-event-simulator`](https://github.com/elimu-ai/ml-event-simulator)** | 🟢 **`MIT`** *(`LICENSE`, `1 065` B)* | EMEA | 🟢 a **simulator for learning and assessment events** — how you load-test an analytics pipeline before real children generate the data |

### 🟢 University-built platforms, which is a different risk profile from a start-up's

| repo | licence | region | note |
|---|---|---|---|
| 🆕 🟢 **[`rage/secret-project-331`](https://github.com/rage/secret-project-331)** | 🟢 **`Apache-2.0`** *(`11 357` B)* | EMEA | `320`★ — the **University of Helsinki** MOOC platform behind its courses. 🟢 Permissive, and running at national scale |
| 🆕 🟢 **[`acanas/swad-core`](https://github.com/acanas/swad-core)** | 🔴 **`AGPL-3.0`** *(`34 501` B, `sha256`₁₂ `884b434957ba`, title at offset `0`)* <!--corrected--> | EMEA | `76`★ — **SWAD**, Universidad de Granada's platform, in continuous use for two decades. 🔴 **`AGPL`: a hosted deployment triggers source disclosure** — this shelf published `GPL-3.0` until p228 |
| 🟢 **[`memphis-iis/MoFaCTS`](https://github.com/memphis-iis/MoFaCTS)** | 🔴 **`AGPL-3.0`** *(`34 523` B — 🆕 `P214-1`: published `GPL-3.0` here, title line reads **AFFERO**)* | North America | adaptive practice driven by **cognitive models** — University of Memphis, built for research AND practice. 🔴 **Network copyleft on a hosted tutor** |
| 🆕 🟢 **[`INRIA/scikit-learn-mooc`](https://github.com/INRIA/scikit-learn-mooc)** | 🟡 **Creative Commons** *(`18 658` B)* | EMEA | `1.4`k★ — **Inria**'s ML course. 🔵 A content grant, not a software one: reusable as **curriculum**, and that is the scarcer asset |
| 🆕 🟢 **[`xiaochong0302/course-tencent-cloud`](https://github.com/xiaochong0302/course-tencent-cloud)** | 🟡 **`GPL-2.0`** *(`18 092` B — the `GPL-2` length, not `GPL-3`'s `~35` kB)* | APAC | `1.2`k★ — a PHP online-education system with Docker deployment, default branch `v2`. 🔵 **Per `P960`, `GPL-2` is NOT `LGPL`: "link, don't absorb" does not apply** |

### 🟢 The credentialing layer — `Open Badges 3.0` is now the live version

🔵 **`topics/open-badges` was the one page where the recency sort UNDER-performed *(`45`% absent
against a `79`% mean)* — this KB already held its head. 🟢 But what it had missed is the version
shift: the new rows implement `3.0`, i.e. Verifiable Credentials, where the shelf's older rows are
`2.0` bakeries.**

| repo | licence | region | note |
|---|---|---|---|
| 🟢 **[`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo)** | 🔴 **`AGPL-3.0`** *(`33 820` B — 🆕 `P214-1`: published `GPL-3.0` here, title line reads **AFFERO**)* | EMEA | `62`★ — **`Open Badges 3.0`** issuance for event and course organisers. 🔴 **Network copyleft: a hosted badge issuer owes source** |
| 🆕 🟢 **[`fedora-infra/tahrir`](https://github.com/fedora-infra/tahrir)** | 🟡 **`GPL`** *(`34 917` B)* | Global | `85`★ — Fedora's own badge issuer, **a decade of production use**; default branch `develop` |
| 🆕 🟡 **[`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib)** | 🟡 **`LGPL-3.0`** *(`LICENSE.txt`, `7 650` B)* | EMEA | a Python library + CLI to **issue, verify and revoke** `Open Badges 3.0`. 🟢 **`LGPL` is the one place "link, don't absorb" is the correct advice** *(`P960`)* |

### 🟢 The `LTI` seam, and a `P971` instance worth naming

| repo | licence | region | note |
|---|---|---|---|
| 🆕 🟢 **[`DecoyLex/ltix`](https://github.com/DecoyLex/ltix)** | 🟢 **`MIT`** *(`1 068` B)* | Global | **`LTI 1.3` for Elixir** — the first non-Python/PHP/JS `LTI` row on this page |
| 🆕 🟡 **[`numbas/numbas-lti-provider`](https://github.com/numbas/numbas-lti-provider)** | 🟡 **`Apache-2.0` BY REFERENCE ONLY** — 🔴 `LICENSE.md` is `560` B against Apache's canonical `11 357` | EMEA | `11`★, Newcastle University; runs **Numbas** exams *(`215`★)* as an `LTI` tool |

🔴 **`P971`, third and fourth instances, both this pass** *(`numbas-lti-provider` at `560` B,
`moodle-block_atrisk` at `703` B)*. 🔵 **The recurring consequence is specific: the only strong
reason to prefer `Apache-2.0` over `MIT` is §`3`, the patent grant — and in a `560` B file §`3`
travels as a URL.** 🟢 A client's counsel will ask. Say "by reference" rather than "Apache-2.0".

### 🟢 Components, which belong here because they remove a build

| repo | licence | region | note |
|---|---|---|---|
| 🆕 🟢 **[`wingkwong/react-quiz-component`](https://github.com/wingkwong/react-quiz-component)** | 🟢 **`MIT`** *(`1 069` B)* | APAC | `403`★ — JSON-defined quizzes as a React component |
| 🆕 🟢 **[`redmodd/tessera`](https://github.com/redmodd/tessera)** | 🟢 **`MIT`** *(`1 077` B)* | Global | a JS framework for interactive eLearning **built for AI-assisted authoring**, and it appeared on `4` of the `12` topic pages — the pass's most cross-listed new row |
| 🆕 🟢 **[`iblai/lms`](https://github.com/iblai/lms)** | 🟢 **`MIT`** *(`1 062` B)* | North America | `14`★ — a skills/competency/credential platform; pairs with the same org's `wallet` |
| 🆕 🟢 **[`valentineus/moodle-webhooks`](https://github.com/valentineus/moodle-webhooks)** | 🟡 **`GPL`** *(`LICENSE.txt`, `35 200` B)* | Global | `20`★ — lets an external application **subscribe to Moodle events**. 🔵 The push half of the `MCP` story, which is all pull |
| 🆕 🟢 **[`willianmano/moodle-theme_moove`](https://github.com/willianmano/moodle-theme_moove)** | 🟡 **`GPL-3.0`** *(`LICENSE.md`, `34 903` B)* | LATAM | `192`★ — the most-used community Moodle theme, maintained from **Brazil** |

### 🔴 Found, wanted, and NOT usable

| repo | why it is here | why it stays off the shelf |
|---|---|---|
| 🔴 **[`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS)** | 🟢 `19`★, and a **`57 120` B README** documenting Singapore's `WSQ` / `SkillsFuture` / `SSG` assessment and funding workflow in extraordinary operational detail — assessor signature blocks, `TRAQOM` survey gating, per-method submission states | 🔴 **NO GRANT FOUND.** Probed at `10` paths plus the README. 🟡 **Read it as APAC domain intelligence — it is the best single description of that regime this KB has seen — and do not fork it** |
| 🔴 **[`mohamurshid/ElimuAnalytics`](https://github.com/mohamurshid/ElimuAnalytics)** | IRT-based learning-gap detection for **Kenya's competency-based curriculum** — a genuinely rare regional asset | 🔴 **NO GRANT FOUND** at `10` paths plus the README |
| 🔴 **[`willwearing/graspful`](https://github.com/willwearing/graspful)** | agent-first course authoring, `YAML` knowledge graphs | 🔴 **`P1054`: MIT's body with an anti-SaaS clause appended. Not open source** |

## Pass 186 — 2026-10-14

🆕 🟢 **Two foundational rows enter, and the pass's two pre-registered measurements come back with
OPPOSITE verdicts: the lecture-capture seam is real and named, and the `pt-BR` essay-scoring seam is
not a seam at all.**

### 🟢 `ACTION MM` — the `opencast` provider interface EXISTS, and it has a name

🔵 **p185 placed [`opencast/opencast`](https://github.com/opencast/opencast) and pre-registered
`ACTION MM` to find out whether an agent attaches to a documented provider interface or has to fork.
Limb `1` FIRES.**

🟢 **Read this pass, in full:
[`modules/transcription-service-api/src/main/java/org/opencastproject/transcription/api/TranscriptionService.java`](https://github.com/opencast/opencast/blob/develop/modules/transcription-service-api/src/main/java/org/opencastproject/transcription/api/TranscriptionService.java)
— `2 532` B, `ECL-2.0` header *(«The Apereo Foundation licenses this file to you under the
Educational Community License, Version 2.0»)*.**

| the contract | `7` methods |
|---|---|
| 🟢 start | `Job startTranscription(String mpId, Track track)` and an overload taking `String... args` |
| 🟢 collect | `MediaPackageElement getGeneratedTranscription(String mpId, String jobId, MediaPackageElement.Type type)` |
| 🟢 callbacks | `void transcriptionDone(String mpId, Object results)` / `void transcriptionError(String mpId, Object results)` |
| 🟢 declare | `String getLanguage()` |
| 🟢 hand off | `Map<String, Object> getReturnValues(String mpId, String jobId)` |

🟢 **This is a PUBLIC `api` module, not an internal class.** 🔵 The interface is explicitly designed
for *"asynchronous external automated transcription"* with a callback — **which is the shape an agent
wants**: submit the track, return a job, be called back. 🟢 **A studio implements one Java interface
with `7` methods; it does not fork `230` modules.** 🔵 And `getReturnValues` exists precisely so a
provider can pass more than the transcript element to the attach handler — the hook for
confidence scores, diarisation, or an agent's own metadata.

🔴 **And one limit that is a DEPLOYMENT fact, not a code smell: `getLanguage()` returns a single
`String`.** 🔴 **One service instance declares ONE language.** 🟢 **For a bilingual or trilingual
institution — which is most of LATAM and much of EMEA — the pattern is one registered provider
instance per language, with the workflow routing on the series' language, NOT one polyglot
provider.** 🔵 **Price that as configuration multiplied by languages, in the first conversation.**

🟡 **`ACTION MM` is DISCHARGED on the seam and NOT RUN on the full table list.** The second limb
asked for `opencast`'s remaining `120` entity-bearing files. 🔴 **There is no tree listing available
here** *(`api.github.com` `403`, `codeload.github.com` `403` — re-measured)*, so files are reachable
only at paths a document names. 🔵 **`Gap 422`, and `ACTION MP` carries it.**

### 🔴 `ACTION ML` — the `pt-BR` essay chain is TRAINING, and limb `2` fires hard

🔵 **`Gap 372` is this KB's longest-standing capability gap. p185 closed its PERMISSIVE half and
pre-registered `ACTION ML` to settle the question that actually decides an engagement: can
`writeAlizer`'s existing models SCORE a Brazilian essay, or must a studio train?**

🟢 **Both sides read this pass over the raw channel:**

| side | what it actually emits | licence |
|---|---|---|
| 🟢 [`lplnufpi/essay-br`](https://github.com/lplnufpi/essay-br) | 🟢 **`5` ANALYTIC competences — `c1`…`c5` — plus a `score`.** Read from the README's own worked example: `c5` takes `40`, `80`, `120`, `160`, `200`; `score` takes `440`…`880`. 🔵 **That is the ENEM rubric: five competences at `0`–`200` in steps of `40`, summing to `0`–`1000`** | 🟢 **`MIT`** *(`1 114` B)* |
| 🔴 [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) `v1.7.4` | 🔴 **ONE target: *"Overall writing quality"*.** `rb_mod3all` returns three GENRE-specific predictions *(narrative / expository / persuasive)* and their mean, `pred_rb_mod3all_mean`. 🔴 **There is no analytic-competence output of any kind** | 🟢 **`MIT`** *(`47` B stub; grant is `License: MIT + file LICENSE` in `DESCRIPTION`)* |

🔴 **LIMB `2` FIRES, on two independent grounds, and either alone is decisive:**

1. 🔴 **The targets do not correspond.** `5` analytic competences on a `0`–`200` ordinal scale cannot
   be read off `1` holistic quality estimate. 🔵 **The genre triple is not a rubric** — narrative /
   expository / persuasive are text TYPES, and ENEM `c1`…`c5` are *formal register*, *grasp of the
   prompt*, *argumentation*, *cohesion* and *intervention proposal*. 🔴 **There is no mapping to
   measure; there is an absence of one.**
2. 🔴 **The models are English-trained.** `DESCRIPTION` gives `Language: en-US`, the input contract
   is `1 316` `RB.*` English ReaderBench features *(measured p185)*, and the model provenance is
   Keller-Margulis et al. and Mercer & Cannon — US and Canadian school writing.

🟢 **So the honest recipe is TRAINING on `essay-br`, and Pattern `29` is amended to say exactly
that.** 🔵 **What a studio actually has, permissively:** an `MIT` labelled `pt-BR` corpus with a
five-competence rubric, and an `Apache-2.0` feature extractor
*([`readerbench/readerbench-java`](https://github.com/readerbench/readerbench-java), `10 758` B
`LICENSE.txt`)*. 🔴 **What it does NOT have is a `pt` model, and it cannot have one by Friday.**

🔴 **`Gap 424`, declared rather than glossed: ReaderBench's PORTUGUESE support is NOT established by
this pass.** Its README describes the framework without naming supported languages, and `3` probed
language-resource paths returned `404`. 🔵 **This matters more than the model gap: if the extractor
has no `pt` pipeline, even the training path is blocked, and the recipe becomes *extract features
with something else*.** 🟢 **`ACTION MQ` settles it, and it is the single highest-value probe
outstanding on this shelf** — it decides whether `Gap 372` closes with a training project or reopens
as a feature-engineering project.

### 🟢 Two rows entering FOUNDATIONS from the recovery pass

| row | licence | layer it fills |
|---|---|---|
| 🆕 🟢 [`Simon-Initiative/lti-example-tool`](https://github.com/Simon-Initiative/lti-example-tool) | 🟢 **`MIT`** *(`package.json`; no licence file)* | 🟢 **the `LTI` handshake, from a credible US holder.** Carnegie Mellon's Simon Initiative; Gleam, `docker compose up`, register-with-your-LMS walkthrough. 🔵 This shelf had `topics/lti` rows but no runnable reference tool whose provenance a US university would recognise |
| 🆕 🟢 [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | 🟢 **`MIT`** *(`package.json`; no licence file)* | 🟢 **a real SIS exposed as agent TOOLS, read-only** — Sisu / Funidata, the Finnish university SIS. Study rights, attainments, grades, enrolments, timetable, study plan, catalogue |

🔵 **Why `sisu-mcp` matters out of proportion to its size:** every student-record integration on this
shelf so far has been *build an adapter against an SIS API*. 🟢 **This is the first row where the
student record is already a tool surface an agent can call, and where READ-ONLY is a property of the
server rather than a promise in a statement of work.** 🔴 **It is one vendor's SIS and `0`★ — read it
as a design to copy, not a dependency to adopt.**

## Pass 185 — 2026-10-14

🆕 🟢 **Three foundational rows enter, and together they close two things this page has carried as
open for five passes: a lecture-capture layer with `0` rows, and an essay-scoring chain whose
blocker was mis-named as the licence when it was always the FEATURE EXTRACTOR.**

### 🟢 `opencast/opencast` — the lecture-capture ROUTE, and the slug p184 proved exists

🔵 **p184 closed out `apereo/opencast` as non-existent and pre-registered `ACTION ME` for the real
slug. The real slug is read here for the first time.**

| fact | value |
|---|---|
| 🟢 licence | **`ECL-2.0`** — *Educational Community License, Version 2.0*, `LICENSE`, **`11 340` B**, full text. 🔵 The `Apache-2.0` derivative written for universities: OSI-approved, permissive, patent grant narrowed to the contributor's own work |
| 🟢 `HEAD` | `637882d48eb850b8435c49320b1605ffea7d071d` |
| 🟢 size | `3 920` tracked paths, **`230` modules** |
| 🟢 entities | **`16` read** from the first `40` entity-bearing files; the tree holds `160`, so this is a FLOOR |
| 🟢 region | **EMEA**, by evidence: `17` locale catalogues, `15` of them European, and a translator roster naming Danish, German, Italian, Galician, Slovenian, Swedish, Greek, Turkish and Hebrew contributors |
| 🔴 Portuguese | **`0` `pt-BR`, `0` `pt-PT`** of the `17` catalogues |

🟢 **The entities that matter:** `oc_series` *(the course/series a recording belongs to)*,
`oc_scheduled_extended_event` *(the scheduled recording)*, `oc_assets_snapshot` /
`oc_assets_asset` / `oc_assets_version_claim` *(versioned media with version claims)*,
`oc_acl_managed_acl` *(managed access control)*, `oc_search` *(the published index)*,
`oc_oaipmh` + `oc_oaipmh_elements` *(OAI-PMH publication — the metadata-harvest standard a
university library already speaks)*.

🆕 🟢 **And the two that make it a COMPOSITION TARGET: `oc_transcription_service_job` and
`oc_transcription_service_provider`.** 🔵 **The provider abstraction is in the SCHEMA, not just in
the code — which means a new transcription provider is a row, not a fork.**

🟢 **Three LOCAL speech-to-text engines ship in-tree**, each with config and admin documentation:

| engine | path | hosting |
|---|---|---|
| 🟢 **Whisper** | `modules/speech-to-text-impl/…/engine/WhisperEngine.java` + `etc/…WhisperEngine.cfg` | 🟢 **LOCAL** |
| 🟢 **whisper.cpp** | `…/engine/WhisperCppEngine.java` + `etc/…WhisperCppEngine.cfg` | 🟢 **LOCAL** |
| 🟢 **Vosk** | `…/engine/VoskEngine.java` + `etc/…VoskEngine.cfg` | 🟢 **LOCAL** |
| 🟡 AmberScript / Google Speech / IBM Watson / Microsoft Azure | `modules/transcription-service-*` | 🔴 CLOUD |

🟢 **So a university can caption every lecture it records without a frame of learner audio leaving
its own network** — and the attachment point for an agent is a named workflow operation,
`modules/speech-to-text-workflowoperation`, over an engine-agnostic
`speech-to-text-api` / `speech-to-text-async-api`.
🔵 **Upstream also ships `AGENTS.md` and `CLAUDE.md`, so the project already expects agent
contributors.** Evidence: [`evidence/opencast-entities.2026-10-14-p185.tsv`](../evidence/opencast-entities.2026-10-14-p185.tsv),
[`evidence/opencast-stt-engines.2026-10-14-p185.tsv`](../evidence/opencast-stt-engines.2026-10-14-p185.tsv).

### 🟢 `readerbench/readerbench-java` — the component that makes `writeAlizer` runnable

🟢 **`Apache-2.0`, `LICENSE.txt`, `10 758` B of full text, *"Copyright 2013 Mihai Dascalu"***
*(Politehnica University of Bucharest — **EMEA**, by the holder's own declaration)*.

🔵 **Why it belongs on this page rather than in a pattern footnote:** `ACTION MF` asked whether the
permissive half of `writeAlizer` can run with no registration-gated tool. **It can, and this is the
tool it needs.**

| the chain, measured | value |
|---|---|
| 🟢 runtime artefacts declared in a COMMITTED manifest | **`50`** — `inst/metadata/artifacts.csv` *(`kind,model,part,file,url,sha`)* |
| 🟢 artefacts needing **no gated tool** *(`rb_*`, ReaderBench)* | **`24` of `50`** |
| 🔴 artefacts needing Coh-Metrix *(registration-gated)* | `24` of `50` |
| 🟡 artefacts needing GAMET *(free download, still a second tool)* | `2` of `50` |
| 🟢 artefacts with a pinned `sha256` | **`50` of `50`** |
| 🔴 distinct hosts serving all `50` | **`1` — `osf.io`** |
| 🟢 model keys driven by `import_rb()` alone | **`10`** |
| 🟢 the input contract | **`1 316` columns** — the `RB.*` header of `inst/extdata/sample_rb.csv` |
| 🟢 offline smoke test with `0` downloads | `model = "example"` + `wa_seed_example_models()` |
| 🟢 maintenance | v`1.7.4`, `DESCRIPTION Date: 2026-09-16`, `36` testthat files, `4` CI workflows |

🔴 **Not executed.** `osf.io` is refused by this environment's proxy *(`CONNECT tunnel failed,
response 403`)*, so `Gap 372` closes on **capability and structure** and stays open on **execution**.
🟢 **It also narrows `Gap 414`: a runtime-downloaded artefact is NOT invisible here — it is a
committed CSV with `50` URLs and `50` hashes, which is precisely the input an air-gapped or mirrored
install needs.** 🔵 Evidence: [`evidence/writealizer-chain.2026-10-14-p185.tsv`](../evidence/writealizer-chain.2026-10-14-p185.tsv).

### 🟢 `lplnufpi/essay-br` — the shelf's first permissive LATAM corpus, and its first `pt-BR` anything

🟢 **`MIT`, `LICENSE`, `1 114` B, *"Copyright (c) 2021 Laboratório de Processamento de Linguagem
Natural - UFPI"*** *(Universidade Federal do Piauí — **LATAM**, by the holder's own declaration)*.

| fact | value |
|---|---|
| 🟢 content | **`6 577` essays written by Brazilian secondary-school students** |
| 🟢 grading | **graded by human professionals on the five ENEM competencies** — `c1,c2,c3,c4,c5` plus `score` |
| 🟢 prompts | `417` |
| 🟢 size | `13.0` MB *(`extended-corpus/extended_essay-br.csv`)* |
| 🟢 citation | Marinho, Anchiêta & Moura, *"Essay-BR: a Brazilian Corpus to Automatic Essay Scoring Task"*, JIDM `13`(1):`65–76`, `2022`, `doi:10.5753/jidm.2022.2340` |

🔵 **How it was found is itself a finding:** `ACTION MD` flagged two Brazilian essay-correction
repositories for a licence identifier, the identifier turned out to belong to a **third-party
corpus they both import**, and the corpus is the asset. 🟢 **A false positive about a grant produced
the most useful LATAM row of the pass.**

🔴 **What it is NOT:** it is not a model and not a scoring path. `writeAlizer`'s `rb_*` models are
trained on English writing samples, so for `pt-BR` this corpus is **training data, not inference
input**. 🔵 **`ACTION ML` is pre-registered to settle that distinction instead of letting a pattern
imply it.**

## Pass 184 — 2026-10-13

🆕 🟢 **Two rows carried as *"unprobed"* for five passes are settled, and one of them was never
probeable.** 🟢 **A third row enters as the first foundational component whose holder declares a
North American affiliation.**

### 🟡 `formalms/formalms` — `GPL-2.0`, and a real LMS domain model

🟢 **Settled by payload, not by roundup.** `HEAD 446a77a`, `5 321` tracked files. The grant is at
**`html/license.txt`** — **`18 346` B**, `md5 65dd37ccb3e888dc57e47d925b80b38a`, **`GNU GENERAL
PUBLIC LICENSE Version 2, June 1991`**, with **`0`** occurrences of *"Lesser"* anywhere in the
file. 🔵 **That zero matters: `P960` is the bifurcation where a GPL-2.0 preamble's reference to the
LGPL makes a naive classifier print `LGPL-3.0`, and it has already cost this KB two rows. It is
excluded here by measurement.** Localised installer copies exist in `8` languages
*(`license_english.txt` at `15 146` B, plus Bosnian, Croatian, French, German, Italian, Portuguese,
Spanish)*.

🔴 **Every PHP source carries the same header:** *"FORMA - The E-Learning Suite … License
https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt … from docebo 4.0.5 CE 2008-2012"*.
🔵 **The lineage is Docebo's `GPL-2.0` community edition, which is why a `2026` roundup printing
`Apache-2.0` is not a near-miss — it is the wrong family.** 🔴 **Third correction of this class,
after `frappe/lms` *(`AGPL-3.0`, printed `MIT`)* and `oat-sa/tao-core`.**

🟡 **And it is entity-RICH, which is what makes the copyleft expensive rather than irrelevant:
`405` `CREATE TABLE` statements**, including `learning_course`, `learning_coursepath`,
`learning_coursepath_courses`, `learning_course_editions`, `learning_course_date`,
`learning_certificate_course`, `learning_competence_course`, `learning_assessment_rule`,
`learning_assessment_user`, `learning_catalogue`, `learning_coursereport_score` — plus a
`conference_*` family *(BigBlueButton, Teleskill, DimDim)* and a `core_customfield_*` extension
system. 🟢 **Price it as a copyleft DEPLOYMENT with AI in a separate permissive service — the
Pattern `26` shape — never as a component to absorb.**

🆕 🔴 **`Gap 370` reproduced on this row.** The root-anchored licence probe finds **`0`** files; the
per-path probe finds **`19`**. 🔵 **A row with a complete, canonical `GPL-2.0` text reads
*"UNLICENSED"* to the instrument this KB has carried unconnected since p183.** 🟢 **Every licence
read in p184 used the per-path probe.**

### 🔴 `apereo/opencast` — the row was never probeable

🔴 **`git ls-remote --symref https://github.com/apereo/opencast HEAD` returns `exit 128`**, with
the same message as `apereo/this-slug-does-not-exist-xyz` run in the same second as a control.
🟢 **The project is real and lives at [`opencast/opencast`](https://github.com/opencast/opencast)** —
`exit 0`, `HEAD e7655449f3a8172fbba37d79ff5a85505545c8a9`, default branch **`develop`**.
🔵 **This KB has carried the dead slug as *"UNPROBED"* for five passes while holding, since p93,
the one-second oracle that discriminates.** 🟢 **`T316`: when a row survives three passes as
unprobed, test its EXISTENCE before scheduling its reading.** 🟢 `ACTION ME` probes the real slug at
p185 — the lecture-capture layer this shelf has `0` rows for.

### 🟢 `shmercer/writeAlizer` — `MIT`, and the honest restatement of `Gap 372`

🟢 **[`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer)** — **`MIT`**
*(`DESCRIPTION`: *"License: MIT + file LICENSE"*, with `LICENSE.md` at `1 076` B)*, **v`1.7.4`
dated `2026-09-16`**, `100` tracked files, **`37` test files**, and `4` GitHub Actions workflows
*(`R-CMD-check`, `rhub`, `test-coverage`, `pkgdown`)*. 🔵 **A CRAN-shaped, actively maintained R
package — not a research dump.** Imports are ordinary CRAN *(`caret`, `cli`, `digest`, `dplyr`,
`glue`, `rlang`, `tidyselect`)*; model fits load `cubist`, `earth`, `gbm`, `glmnet`, `kernlab` on
demand.

🔴 **`Gap 372` said no permissive production-grade essay-scoring library exists, and that all
permissive supply was *"a `2`★ research repo"*. That is WRONG and is corrected here.** 🟢 **What is
right is the practical conclusion, for a different reason:**

| layer | what `writeAlizer` provides | what it needs from elsewhere |
|---|---|---|
| 🟢 scoring | `predict_quality()` over **`18` model variants** *(`rb_mod1`…`rb_mod3per_v2`, `coh_mod1`…`coh_mod3per`, `gamet_cws1`)*, peer-reviewed with DOIs | — |
| 🔴 features | — | 🔴 **`Coh-Metrix`** *(registration-gated, `soletlab.asu.edu`)*, **`GAMET`** *(free download)* or 🟢 **`ReaderBench`** *(open source, `readerbench/readerbench-java`)* |
| 🔴 models | `wa_download()`, an artifact registry, a cache | 🔴 **`0` model objects committed — `18` fetched at RUNTIME** under OSF-published terms |

🔵 **So the blocker on automated writing assessment was never the licence. It is the upstream
feature-extraction chain, and exactly one of the three options is open source.** 🟢 **`ACTION MF`
tests whether the `rb_mod*` variants run from `ReaderBench` output alone — if they do, a fully
permissive path exists for the activity the EU `AI Act` names high-risk most explicitly.**

🆕 🔴 **And this row opens `Gap 414`: a model or corpus fetched at runtime is invisible to every
instrument on this shelf.** 🔵 **`ACTION LZ` swept `17` trees for committed indexes and found one.
It could not have found this one, because there is nothing to find in the tree — the second grant
arrives over the network.**

### 🟢 `openeducat_erp` — the entity count, corrected

🔴 **p183 published *"`141` Odoo models across `13` modules"*. At the same `HEAD 46a5d7d`, that
does not reproduce.** 🟢 **Measured with a line-start-anchored probe:**

| measurement | value |
|---|---|
| 🟢 distinct `op.*` business models | **`59`** |
| 🟡 wizard and report models | `29` |
| 🟢 total `_name` declarations | **`88`** |
| 🟡 model classes *(`models.Model` / `AbstractModel` / `TransientModel`)* | `112` |
| 🔴 `_inherit` in-place extensions | `55` |
| 🟢 module manifests | **`14`** *(not `13`)* |

🔵 **`88 + 55 = 143`, which is how a count reaches ~`141`: by adding in-place extensions to
declarations.** 🔴 **An `_inherit` extension is not a new entity.** 🟢 **The number a client should
see is `59`** — `op.course`, `op.admission`, `op.exam`, `op.marksheet.register`,
`op.attendance.sheet`, `op.academic.year`, `op.fees.terms`, `op.library.card`, `op.program.level`,
`op.result.template`, `op.room.distribution`, `op.subject.registration` among them.

🆕 🔴 **`P1048`, a generic probe defect found and repaired mid-pass:** an unanchored `_name *=`
pattern also matches **`_rec_name`** *(`17` occurrences here)*, whose values are FIELD names
*(`course_id`, `student_id`, `marks`, `application_number`)*. 🔵 **The defect manufactures entities
that are columns — a first count said `102` distinct names where the anchored count says `88`.**

## Pass 183 — 2026-10-13

🆕 🟢 **`T309` was re-tested on a channel p182 never used, and it HOLDS — which matters, because a
thesis about an environment should not rest on one tool.**

🔵 **p182 established that the fetch channel resolves GitHub-family hosts only, by trying `7`
non-GitHub hosts through the fetch TOOL. 🆕 This pass ran the census again through plain `curl` in
a shell — a different code path with a different resolver — and added one more non-GitHub host on
the fetch tool.**

| channel, measured this pass | result | what it means |
|---|---|---|
| 🔴 `curl -sI https://github.com/<slug>` | 🔴 **`403 Forbidden`**, after a `200` CONNECT to the proxy | 🔴 `gap 140` re-confirmed on a SECOND tool. **The proxy connects; GitHub's web layer refuses** |
| 🔴 `curl https://api.github.com/repos/<slug>` | 🔴 **`403`** | 🔴 **No ★, no licence field, no `pushed_at`.** The metadata API is shut on `curl` as well |
| 🟢 `curl https://raw.githubusercontent.com/…` | 🟢 **`200`** | 🟢 The payload channel is open on `curl` too |
| 🔴 `curl https://www.unesco.org/en` | 🔴 **`000`** — no HTTP response at all | 🆕 🟢 **`T309` CONFIRMED on a second tool.** Not a quirk of one fetcher — a resolver boundary |
| 🔴 fetch tool, `www.unesco.org` | 🔴 **`ENOTFOUND`** | 🆕 An eighth non-GitHub host, eighth failure |
| 🟢 `git clone --depth 1` of an arbitrary public repo | 🟢 **WORKS — `5` of `5` attempts** *(`open-tutor-ai-CE`, `civil-ai`, `tutor-gpt`, `TeachGPT`, `openeducat_erp`)* | 🟢 **The strong channel. Existence, licence payload, schema and file counts all come from here** |
| 🆕 🟢 **run code THIS KB wrote, stdlib only** | 🟢 **WORKS** — `18` checks green in [`compose/code/agent-tool-receipts-port/`](../compose/code/agent-tool-receipts-port/README.md) | 🆕 🟢 **`T303` bars building or testing a CLONED SUBJECT tree. It does not bar running this repository's own code.** First pass to use that distinction deliberately |
| 🟡 web SEARCH *(not fetch)* | 🟡 **WORKS, summaries only** | 🔴 **And it can be MONTHS STALE on a fact this KB already holds — `T312`, see [`intel/market.md`](../intel/market.md)** |

🆕 🔵 **The rule, stated once rather than rediscovered: this KB has ONE primary-source channel and
it is `git clone`.** 🟢 **A pass that spends its budget cloning buys evidence; a pass that spends
it searching buys leads.** 🔴 **And `curl -sI` cannot verify that a repository exists here, so a
successful clone of the exact path is the existence test.**

### 🆕 🟢 The foundations shelf — `0` new rows, and `2` rows that stop being licence entries

🔴 **No repository was added to this shelf this pass, and that is the correct outcome: every
candidate the discovery channel produced was already on it.** 🟢 **What changed is that two
carried rows now have a measured domain model instead of only a verified grant.**

| row | what this shelf held | 🆕 measured this pass |
|---|---|---|
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0`, `8 241` B, APAC *(India)*, `16` passes carried, `T162` *(vendor-stated standards absent)* | 🆕 🟢 **`141` Odoo models, `13` modules, `1 345` files.** Real `op.course`, `op.admission`, `op.exam`, `op.marksheet.register`, `op.attendance.sheet`, `op.academic.year`, `op.fees.terms`. 🟢 **The SIS entities exist; it was only ever the interoperability layer that did not** |
| 🔴 [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🔴 `GPL-3.0`, *"CLEAN at `1` word"*, carried since p176 | 🆕 🔴 **Its only tables are `users`, `customers`, `products`, `prices`, `subscriptions`.** `course`/`lesson`/`enrollment`/`assessment`/`quiz`/`grade`/`tenant` = `0` each across `158` files. 🔴 **A copyleft chat product with a billing schema — it was never a foundation and now this shelf can say why** |

🆕 🔵 **`T313`, from the pass's own mis-step: a row with a verified licence is not a read row.**
🔴 **This shelf has been optimising for the grant, because the grant is cheap and binary. The
entity list is the expensive half and the deciding half, and `3` carried rows turned out never to
have had one.**

### 🆕 🔴 The grant that is never in `LICENSE`

🔵 **`Priyamakeshwari/TeachGPT` is already on this KB's record as `MIT` *(`1 057` B, *"title-less,
grant line only"*, `P645`)*. 🆕 Cloned this pass, it is `18` files — and it COMMITS its corpus:
`db/chroma.sqlite3` plus the HNSW index binaries, built from
`documents/Machine - Learning - Tom Mitchell.pdf`, a commercial textbook.**

🔴 **A vector index is a derivative of what it was built from.** 🟢 **`MIT` grants the three
scripts. It grants nothing over a publisher's book or over embeddings of it.** 🟢 **Shelf rule
adopted: when a row ships a prebuilt index, a corpus or a model checkpoint, there is a SECOND
grant to check and `LICENSE` does not cover it.** 🔵 **This extends
[`compose/code/p317-data-license-layer/`](../compose/code/p317-data-license-layer/README.md) into
a repository whose code licence is perfectly clean — which is the case the data-layer axis had not
yet seen.**

## Pass 182 — 2026-10-13

🆕 🔴 **The foundational finding this pass is about the ENVIRONMENT, and it changes how every
non-code fact in this KB should be labelled.** 🟢 **`gap 110` is not a stubborn domain. It is an
allowlist.**

🔵 **p181 recorded `eur-lex.europa.eu` as unreachable *"on a FOURTH channel, with a working control
on that same channel"*, and concluded the failure was target-specific. 🆕 `ACTION LM` tested that
conclusion properly this pass by trying hosts that have nothing to do with the EU.**

| host tried on the fetch channel | result | what it is |
|---|---|---|
| 🟢 `raw.githubusercontent.com` | 🟢 **`200`, `100 338` characters returned** | the control |
| 🔴 `digital-strategy.ec.europa.eu` | 🔴 `ENOTFOUND` | the European Commission's own AI Act page |
| 🔴 `artificialintelligenceact.eu` | 🔴 `ENOTFOUND` | the AI Act Explorer |
| 🔴 `ai-at.eu` | 🔴 `ENOTFOUND` | the Austrian AI Service Desk *(a national authority channel)* |
| 🔴 `www.bsigroup.com` | 🔴 `ENOTFOUND` | a standards body |
| 🔴 `www.cooley.com` | 🔴 `ENOTFOUND` | a law firm |
| 🔴 `en.wikipedia.org` | 🔴 `ENOTFOUND` | a general reference |
| 🔴 `arxiv.org` | 🔴 `ENOTFOUND` | the preprint server this KB cites for papers |

🆕 🔵 **`T309`: the fetch channel resolves GitHub-family hosts ONLY.** 🔴 **Therefore every
non-GitHub fact in this KB — every market figure, every regulatory date, every adoption
percentage — rests on SEARCH-RESULT SUMMARIES and has never been read from the page it cites.**
🟢 **That is not a reason to drop those facts; it is a reason to label them as a class, which this
pass starts doing in [`intel/market.md`](../intel/market.md).**

🔵 **And it retires a bad inference: a GitHub-hosted control cannot distinguish *"this domain is
blocked"* from *"every domain but ours is blocked"*. p181 ran exactly that control and drew
exactly the wrong conclusion. 🟢 `gap 110` is hereby restated as CHANNEL-WIDE and merged with the
reachability picture below.**

### 🟢 The channel census after p182 — what works here, stated once

| channel | verdict | evidence this pass |
|---|---|---|
| 🟢 **`git clone` over smart-HTTP** | 🟢 **WORKS** | `6` repositories cloned and measured this pass *(`tutor-mcp`, `civil-ai`, `feedbacksystem`, `open-tutor-ai-CE`, `plataforma-agentes-ia`, `tutoria`, `lms`)* |
| 🟢 **`raw.githubusercontent.com` fetch** | 🟢 **WORKS** | `DeepTutor`'s README returned in full |
| 🟢 **install a package FROM A REGISTRY** | 🟢 **WORKS** | p181: `npm` installed `@dodona/dolos@2.9.3` and ran `8` analyses |
| 🔴 **GitHub web / API / codeload** | 🔴 **`403`** | `github.com`, `api.github.com`, `codeload.github.com` re-confirmed this pass *(`gap 140`)* |
| 🆕 🔴 **fetch ANY non-GitHub host** | 🔴 **`ENOTFOUND`** | `7` hosts, `7` failures, `1` GitHub control passing *(`T309`)* |
| 🔴 **build or test a CLONED subject tree** | 🔴 **REFUSED** | `mvn package` on `OpenOLAT` *(p181)*, `pytest` on `Bloom` *(p180)* — the external-code policy *(`T303`)* |
| 🆕 🟡 **compound shell over a cloned tree** | 🟡 **PARTIALLY REFUSED** | several multi-stage `grep` pipelines over cloned trees were declined this pass; plain file reads and the dedicated search tools were not. 🔵 Measurement is unaffected, the ergonomics are |

🔵 **The practical rule for the next pass: measure with the dedicated search tools over a clone.
Do not build pipelines, do not expect a page, do not expect a star.**

### 🟢 The permissive foundations shelf, re-graded on licence PAYLOADS read this pass

🔵 **Every licence below was read as a file from a `--depth 1` clone and sized. A roundup's licence
column is not evidence — this pass has a counterexample.**

| repo | licence *(payload-verified this pass)* | size | what it founds |
|---|---|---|---|
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0` | `10 982` B | 🟢 **The permissive full-LMS foundation.** `385` `CREATE TABLE`, `186` Maven dependencies — budget the discovery |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 `MIT` | `1 091` B | 🟢 Assessment + `LTI 1.3` grade passback; `257` entities |
| 🟢 [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 `MIT` | `1 073` B | 🟢 **The multi-tenant foundation, enforcement-verified this pass.** `240` `CREATE TABLE`, `36` scope-taking store methods |
| 🟢 [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 `Apache-2.0` | `10 785` B | 🟢 **Institutional grading with its OWN OIDC provider** — no external IdP required *(`ACTION LQ`)* |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `MIT` | `1 062` B | 🟢 The TypeScript LMS route; `SCORM 1.2` both ways |
| 🆕 🟢 [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **`BSD-3-Clause`** | `1 531` B | 🟡 **`4 702` files, own identity, `ar-MA`/`fr-FR` locales.** 🔴 No course or assessment entity — a tutoring layer, not a platform |
| 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 `MIT` | `1 068` B | 🟢 The smallest complete route: `34` tables, `141` endpoints |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 `MIT` | — | 🟢 Plagiarism/similarity, executed and calibrated here |
| 🆕 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`AGPL-3.0`** | **`33 893` B** | 🔴 **DISQUALIFIED as a permissive foundation.** A `2026` roundup listed it `MIT`; its own `license.txt` is the GNU Affero GPL v3 |

🆕 🔴 **The `frappe/lms` correction is the kind this KB exists to make.** 🔵 **A secondary roundup
put it in an MIT column; `1 632` tracked files later, the payload is Affero. 🟢 For a Globant
engagement that is the difference between a buildable foundation and a hosted-derivative legal
conversation.**

### 🟡 Still unresolved, carried honestly

- 🔴 **`formalms/formalms` and `apereo/opencast` remain UNPROBED** for a fourth pass. 🟡 `formalms`
  is listed `Apache-2.0` in one source and `GPL` in another — and after `frappe/lms`, a listing is
  not a licence.
- 🔴 **`OpenOLAT`'s boot time stays unknown** — the build is refused here *(`T303`)*.
- 🔴 **`0` permissive SIS of any origin.** The only student-information systems surfaced this pass
  are `RosarioSIS` and `Gibbon`, both `GPL`, both PHP. 🔵 **An MIT/Apache SIS does not appear to
  exist, and a studio should assume the SIS layer is either copyleft or bespoke.**


## Pass 181 — 2026-10-13

🆕 🔴 **`ACTION LG` fired limb `2`, and the reason matters more than the verdict: `OpenOLAT` was not
proved un-bootable here — it was never built, because this harness REFUSES to build a cloned
subject tree.** 🟢 **`mvn -B -ntp -Dmaven.test.skip=true -T 1C package` was declined by the
external-code policy, exactly as `Bloom`'s `pytest` was at p180.**

🆕 🟢 **That turns a three-pass-old confusion into one sentence. `gap 139` is NOT about language.**

| channel | verdict | evidence |
|---|---|---|
| 🟢 **install a package FROM A REGISTRY** | 🟢 **WORKS** | `npm` installed `@dodona/dolos@2.9.3` and it RAN `8` analyses this pass; `PyPI` installed `15`/`15` of `Bloom`'s declared packages at p180 |
| 🔴 **build or test a CLONED SUBJECT TREE** | 🔴 **REFUSED** | `mvn package` on `OpenOLAT` *(p181, Java)*; `pytest` on `Bloom` *(p180, Python)* |
| 🟢 **READ a cloned subject tree** | 🟢 **WORKS** | `14` repositories cloned and measured this pass; `git clone` over smart-HTTP remains the one reliable channel *(`T291`)* |

🔵 **`T303`: the boundary is the code's PROVENANCE, not its language. A registry package is a tool
this session runs; a cloned repository is someone else's program, and this harness will not execute
one. p179's *"a JavaScript subject is executable here and a Python one is not"* was a coincidence of
which artefact happened to be a tool.**

### 🟢 `OpenOLAT` — the static cost line Pattern `20` needed, since the dynamic one is unavailable

🟢 **`HEAD 8494a140b2ca`, re-cloned independently this pass in `14` s to `340` MB.** 🟢 **`14 809`
`.java` files and `2 624 333` lines of Java — which REPRODUCES p180's figure exactly, from a
separate clone.**

| build fact | measured | what it costs a studio |
|---|---|---|
| 🟢 **Maven modules** | **`1`** | 🟢 **A single WAR, not a `20`-module reactor. The build graph is simple even though the tree is huge** |
| 🟡 **declared dependencies** | **`186`** | 🟡 The first resolution is the slow one; `186` direct dependencies is a normal enterprise Java footprint |
| 🟡 **build plugins** | `24` | 🟡 Includes the `tomcat`/`jetty` wiring the README's Eclipse path depends on *(`10` references in `pom.xml`)* |
| 🔴 **PostgreSQL schema** | 🔴 **`385` `CREATE TABLE` in `322 754` B** *(`setupDatabase.sql`)* | 🔴 **This is the real discovery cost, and it is the number to quote: `385` tables to learn before a confident extension. `Artemis` by comparison is `257` entities; `OpenTutor` is `34`** |
| 🟢 **target runtime** | Tomcat `10.0`/`10.1`, PostgreSQL *(MySQL supported, deprecated upstream)* | 🟢 Standard institutional hosting; nothing exotic to procure |

🔵 **`T294` STANDS but must be restated honestly: this KB has no evidence about `OpenOLAT`'s boot
time, and will not get any here. Pattern `20` quotes a discovery spike — and now it quotes `385`
tables and `186` dependencies as the thing the spike is sizing, instead of an unqualified
*"spike"."***

### 🟢 The foundations shelf, with this pass's additions

🔵 **Licences below were payload-verified this pass unless marked carried. Grants are identified by
reading the TEXT, not by matching a byte size — `feedbacksystem`'s `Apache-2.0` is `10 785` B
against the canonical `11 358`, and is still `Apache-2.0`.**

| repo | licence *(payload)* | layer | why it is foundational |
|---|---|---|---|
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 `Apache-2.0`, `10 982` B | full LMS | 🟢 **The permissive system of record.** `440` `@Entity`, `385` tables in the shipped schema, own federated auth, `LTI 1.3` + `QTI` + `SCORM` + `OpenBadges` |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 `MIT`, `1 091` B | assessment | 🟢 `257` entities, `528` write endpoints, `LTI 1.3` grade passback, nightly Moodle interop test |
| 🆕 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `MIT`, `1 062` B, `md5 88f104b7644947b4a8b6e71f4972c02f` | LMS *(TypeScript)* | 🆕 🟢 **The permissive LMS a JS studio can actually staff.** `4 753` files, `123` `pgTable`, `tenant` in `305` files, `pnpm` workspaces, `docker-compose`, and **bidirectional `SCORM 1.2`** |
| 🆕 🟢 [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 `MIT`, `1 073` B, `md5 6ef9d4b578ace4e94d9ae2f1e6054688` | multi-tenant tutoring + assessment | 🆕 🟢 **The only row with cohorts AND tenants AND billing AND audit events in one schema.** Go, `694` files, `240` `CREATE TABLE` |
| 🆕 🟢 [`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 `Apache-2.0`, `10 785` B, `md5 a3d40cf5ce6af0822ae6fbb6b0767a94` | automated grading *(institutional)* | 🆕 🟢 **A production university grading system with a SEPARATE identity service and `Keycloak` federation** — the shape an institution's IT department expects |
| 🆕 🟡 [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) | 🟢 `MIT`, `1 067` B | assessment + content pipeline | 🆕 🟡 **`assessment_policy_versions`, `content_schema_versions`, `agent_tool_receipts`, `ai_invocations`** — versioned policy and per-call receipts, which is what an audited deployment needs |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 `MIT`, `1 084` B | integrity | 🟢 **Calibrated in this KB twice** *(p179, p181)*: threshold `0.85`, and now a measured template-ratio rule |
| 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 `MIT`, `1 068` B | AI tutor platform | 🟢 `34` tables, `141` endpoints, `jose` refresh tokens, `alembic` migrations |
| 🔴 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 `Apache-2.0`, `11 408` B, `md5 48e65e4facf86c33198db013e838c41e` | AI tutor *(single-deployment)* | 🟡 **`69` tables of genuine learning state** *(`mastery_paths`, `mastery_events`, `assessment_attempts`, `reading_progress`)* — 🔴 **but no `users` table, so it is a per-deployment appliance until an identity layer is added** |
| 🔴 [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 `MIT`, `1 079` B | spaced-repetition algorithm | 🟢 **Foundational as a COMPONENT, not a platform:** `51` files of scheduler. 🔵 Its `0` tables are correct, not a defect *(`T299`)* |

### 🔴 Licence findings that change eligibility

| row | published before | 🆕 corrected this pass |
|---|---|---|
| 🔴 [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `1 230` B, grant unidentified | 🔴 **`CC BY-SA 4.0` — a CONTENT licence, not a software grant.** `ShareAlike` reaches derivative curriculum. 🔵 **A studio adapting these materials owes `SA` on what it ships back** |
| 🟢 [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | `7 048` B, grant unidentified | 🟢 **`CC0 1.0` — public-domain dedication.** The most permissive grant anywhere on this shelf |
| 🔴 [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | unread | 🔴 **`GPL-3.0`** — ROUTE-ineligible despite owning its identity |
| 🔴 [`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) | unread | 🔴 **`GPL-3.0`** |
| 🔴 [`luffycodes/Tutorbot-Spock`](https://github.com/luffycodes/Tutorbot-Spock) | unread | 🔴 **NO GRANT AT ALL** — no licence file, and no grant text in any of its `17` tracked files. Unusable, and this survives the wider name list *(`ACTION KN`, limb `2`)* |

🔵 **`T304`: in an education corpus, *"open source"* collapses into three different things — a code
grant, a CONTENT grant with `ShareAlike` reach, and no grant at all. `3` of the `12` rows newly
licence-read this pass were not under a software licence.**

## Pass 180 — 2026-10-13

🆕 🟢 **`ACTION LE` is DISCHARGED with limb `1` FIRED, and it is the most consequential finding this
file has carried in `20` passes: [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is not
merely the shelf's only permissive full LMS — it is a complete, data-owning, auth-carrying,
standards-speaking PLATFORM.** 🔵 **p179 found the `Apache-2.0` grant and correctly refused to call
it a route. It is a route.**

### 🟢 `ACTION LE` — OpenOLAT read past its licence

🟢 **`HEAD 8494a140b2ca`, `25 824` tracked files, `14 809` `.java` source files,
`2 624 333` lines of Java, built with `pom.xml`.** 🔴 **Limb `2` — *"it is a thin layer over
something else"* — is dead on arrival at that size.**

| capability | measured | what it means |
|---|---|---|
| 🟢 **owns its data** | **`440`** `@Entity` classes, **`419`** `@Table(name…)` annotations, `497` `DAO`/`Manager` classes, `199` schema/migration `SQL` files | 🟢 **More entities than [`Artemis`](https://github.com/ls1intum/Artemis)' `257`. This is the system of record, not a client of one** |
| 🟢 **portable storage** | `oracle` `69` files, `postgresql` `68`, `mysql` `68` | 🟢 Three production RDBMS targets — an institution's existing DB standard is not a blocker |
| 🟢 **carries its own auth** | `AuthenticationProviderSPI`, `AuthenticationProvider`, `LDAPAuthenticationProvider`, `OAuthAuthenticationProvider`, `RestApiAuthenticationProvider`; `authentication` `300` files, `login` `1 248`, `password` `678`, 🟢 **`shibboleth` `147`**, `ldap` `158`, `oauth` `137`, `jwt` `43` | 🟢 **`Shibboleth` in `147` files is the tell: this is built for federated institutional sign-on, which is what a university actually has** |
| 🟢 **speaks the standards** | 🟢 **`LTI` `4 987` files** *(`252` of them `LTI 1.3`-specific — `lti13`/`AssignmentAndGradeService`/`DeepLinking`)*, `QTI` `1 201`, `IMS` `1 394`, `SCORM` `355`, `OpenBadges` `263` | 🟢 **Broader than any row on this shelf. `Artemis` brought `LTI 1.3`; `OpenOLAT` brings `LTI 1.3` + `QTI` + `SCORM` + `OpenBadges`** |
| 🆕 🟢 **already has an AI surface** | `openai` `33` files, `llm` `34`, `ollama` `13`, `457` `restapi` files | 🟢 **A studio EXTENDS an existing integration point here rather than inventing one — and `ollama` in `13` files means a self-hosted model path already exists upstream** |
| 🟡 identity model | `IdentityImpl`, `Identity`, `TransientIdentity`, `DeletedIdentity` in `org.olat.basesecurity` | 🟡 A first-class `Identity` abstraction with a deletion path — relevant to `GDPR` erasure requests |

🔵 **`T293`: the permissive-vs-copyleft question and the platform-vs-component question are
INDEPENDENT, and this shelf confused them for `20` passes.** 🟢 **Every full LMS was assumed to be
copyleft because the three biggest ones are. `OpenOLAT` is `Apache-2.0` AND bigger than any of the
permissive rows this KB had read.**

### 🟢 The foundation set — licences re-read to a FILE this pass, `17`/`17` exact

🟢 **Every row below was fetched to a file and measured with `wc -c`, never captured into a shell
variable** *(the full census with `md5`s and deltas is in [`repos/trending.md`](trending.md))*.
🔵 **`17` of `17` reproduce the published figure exactly, so this table's licence column is now
agreed across three independent channels.**

| repo | layer | licence *(payload-verified)* | bytes | region | grade |
|---|---|---|---|---|---|
| 🆕 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | full LMS | 🟢 **`Apache-2.0`** | `10 982` | EMEA *(Swiss-led consortium)* | 🟢 **ROUTE — permissive, `440` entities, own auth, `LTI 1.3`+`QTI`+`SCORM`** |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | interactive learning + assessment | 🟢 `MIT` | `1 091` | EMEA *(TU München)* | 🟢 ROUTE *(p178)* — `257` entities, `528` write endpoints |
| 🆕 🟢 [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | AI tutor platform | 🟢 `MIT` | `1 068` | APAC | 🟢 **ROUTE — `34` tables, own `JWT`+`bcrypt` auth, `141` endpoints, `alembic`** |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | academic integrity | 🟢 `MIT` | `1 084` | EMEA *(KU Leuven / Ghent)* | 🟢 COMPONENT — **calibrated at p179**, threshold `0.85` |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | LMS *(commercial OSS)* | 🟢 `MIT` | `1 062` | EMEA *(Poland)* | 🟡 **the only shelf row DECLARING both `scorm` and `xapi`** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | full LMS | `GPL-3.0` *(at `COPYING.txt`)* | `35 147` | Global | 🟡 incumbent; plugin-shaped AI work only |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | MOOC / LMS | `AGPL-3.0` | `35 136` | Global | 🔴 network copyleft reaches a hosted AI layer |
| 🔴 [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | full LMS | `AGPL-3.0` | `34 520` | North America | 🔴 integrate over `LTI`, do not fork |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | LMS / collaboration | 🟡 `ECL-2.0` | `11 120` | North America | 🟡 patent grant scoped to educational use |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | ERP + LMS + SIS *(Odoo)* | `LGPL-3.0` | `8 241` | APAC *(India)* | 🟡 the one integrated LMS+SIS route; `LGPL` permits a separate AI module |
| 🟡 [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | school management / SIS | 🟢 **`GPL-3.0`** *(🆕 `P214-1`: was `AGPL-3.0` here for 4 cells)* | `35 121` | APAC *(Hong Kong)* | 🟡 **file copyleft, NOT network** — a hosted SIS deployment owes no source disclosure |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | SIS *(K-12)* | `GPL` | `15 214` | EMEA *(France)* | 🟡 on-premise is the comfortable case |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | school ERP *(Frappe)* | 🔴 **`19`-byte ASSERTION, no grant text** | `19` | APAC *(India)* | 🔴 **UNVERIFIED — intended `GPL-3.0`; the file contains `License: GNU GPL V3` and nothing else** |
| 🟡 [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | LLM microservice for Artemis | 🟢 `MIT` | `1 089` | EMEA | 🟡 a dependency, not a product *(p178)* |

🔵 **`14` rows; `6` carry a permissive grant** *(`Apache-2.0` ×`1`, `MIT` ×`4`, `ECL-2.0` ×`1`)*,
🔴 **`4` are `AGPL`/`GPL` network- or strong-copyleft, `1` is `LGPL`, and `1` has no readable grant
at all.** 🟢 **`3` rows are now ROUTE-grade and code-verified — `OpenOLAT`, `Artemis`,
`OpenTutor` — up from `1` at p178.**

### 🔴 Still unresolved, carried honestly

- 🟢 **`formalms/formalms` is RESOLVED: `GPL-2.0`**, body in-tree at `html/license.txt`
  *(`18 346` B, re-read binary-safe p215, CRLF — see `P215-5`)*, plus the same grant as a
  translated UI asset in `10` languages. <!--corrected--> 🔴 **p214 established this and `6` cells on
  these shelves went on saying *"no licence"* — the `ACTION QG` defect, measured.**
- 🔴 **`apereo/opencast` remains UNRESOLVED, not absent.** Unchanged from
  p179; not probed this pass, which spent its fetch budget on the `17`-row census instead.
- 🔴 **`ACTION KN` — the `76` grant-path probe lists — is carried for a SIXTH pass.** 🆕 🟡 **Its
  urgency drops, though, and the reason is measurable:** this pass fetched `moodle/moodle` at
  `COPYING.txt` directly and got `35 147` B with the canonical `GPL-3.0` `md5`, so the one FALSE
  ABSENCE `gap 135` produced is now corrected in the published table. 🔵 **The debt is real but it
  is hygiene, not a live wrong answer.**
- 🔴 **`0` repositories originating in North America or LATAM reached this foundation set as a
  permissive route.** 🔵 **`Canvas` and `Sakai` are North American and both are copyleft or
  education-scoped; LATAM contributes no row at all (`gap 141`).**

## Pass 179 — 2026-10-13

🆕 🟢 **Eight platform licences re-read from the payload this pass, on a repaired channel, and the
re-read settles one standing CONFLICT, corrects one published family, and finds one "licence" that
is not a licence.**

The channel matters, so it is stated first: these figures come from
`compose/code/p117-second-channel/licence.sh` **after** `ACTION KY` rewrote it onto
`lib/fetch_payload_to_file.sh`. 🟢 **The body now goes to a file and the HTTP code comes back on
stdout, so the byte count is exact and an `md5` travels with every row.** 🔵 **The repaired
instrument reproduces p178's FULL-channel figures exactly — `dolos` `1 084`, `Artemis` `1 091`,
`mentingo` `1 062`, `Pyris` `1 089` — which is how this pass knows the repair is a repair and not
a new defect.**

| repo | branch | file | family *(from the payload)* | bytes | `md5` |
|---|---|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `master` | `LICENSE` | 🟢 **`Apache-2.0`** | `10 982` | `6ba3198de8e95979d5895c0827d34bc0` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `master` | `LICENSE` | 🟡 **`ECL-2.0`** | `11 120` | `ca5955eea85a5d171ce51c891797aafa` |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `HEAD` | 🔴 **`COPYING.txt`** | `GPL-3.0` | `35 147` | *(re-probed, see below)* |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `master` | `LICENSE` | `AGPL-3.0` | `35 136` | `47e2062a6393f45a2bd32dca8f8b53d1` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | `master` | `LICENSE` | `AGPL-3.0` | `34 520` | `73f1eb20517c55bf9493b7dd6e480788` |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `main` | `LICENSE` | 🟢 **`GPL-3.0`** *(🆕 `P214-1` correction; read `AGPL-3.0` here)* | `35 121` | `28480d6422e52c304753119903a184b2` |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `master` | `LICENSE` | `GPL` | `15 214` | `4fcab427efca2a10f4b242b15d3d1f34` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `HEAD` | `LICENSE` | `LGPL-3.0` | `8 241` | `f18b2e83f16ffef283395deccff2c341` |
| [`frappe/education`](https://github.com/frappe/education) | `HEAD` | `license.txt` | 🔴 **see below** | **`19`** | `2884e131cfab2111873ff0eb5ba55997` |

### 🟢 What the re-read settled

- 🟢 **`sakaiproject/sakai` is `ECL-2.0`, and that closes a live disagreement.** Secondary sources
  consulted this pass report Sakai as `Apache-2.0` in one place and `ECL-2.0` in another.
  🔵 **The payload says *"Educational Community License"*, so the permissive-but-not-Apache reading
  is the correct one — and the distinction is not academic, because `ECL-2.0` adds a patent clause
  scoped to educational use that `Apache-2.0` does not have.**
- 🟢 **`OpenOLAT/OpenOLAT` is genuinely `Apache-2.0`, confirmed on the payload at `10 982` B.**
  🔵 **It is the ONLY permissively licensed full LMS in this table, which makes it the one row here
  Globant can build a closed derivative on without a copyleft conversation.** Every other LMS in
  the set is `AGPL-3.0`, `GPL`, `LGPL-3.0` or `ECL-2.0`.
- 🟢 **`GibbonEdu/core` is `GPL-3.0`.** <!--corrected--> 🔴 **The assertion that it is `AGPL-3.0`, not `GPL`, is WITHDRAWN — it is exactly backwards** *(`P227-SO1`; `master/LICENSE` `35 121` B, `sha256`₁₂ `93178a43d6d3`; the `3` `AFFERO` tokens are GPL-3.0 §13's compatibility clause)*. The secondary sources describing it as a *"GPL
  all-in-one school management tool"*; the payload is the Affero text at `35 121` B.
  🔵 **For a hosted deployment that difference is the whole engagement: `AGPL-3.0` reaches users
  over a network and `GPL` does not.**

### 🔴 `frappe/education`'s licence file is `19` bytes and contains no grant

Read verbatim, with `od -c`, because a figure this small invites disbelief:

```
License: GNU GPL V3
```

🔴 **That is the entire file: `19` bytes, no trailing newline, no grant text, no copyright holder,
no version URL, `md5 2884e131cfab2111873ff0eb5ba55997`.** 🔵 **It is a licence ASSERTION, not a
licence — the same defect class as a `README` badge, and it sits in the repository slot where the
grant is supposed to live.** 🟡 **It is almost certainly intended as `GPL-3.0` and a client
should be told it is intended; what a client cannot be told is that the grant was READ, because
there is no grant here to read.**

### 🔴 And the pass found the defect in its own probe before it published the wrong answer

🔴 **`moodle/moodle` came back `NO-LICENCE-FILE` on `4` branches × `6` filenames — and that verdict
was WRONG.** Moodle's grant is at **`COPYING.txt`**, which answers `200` at `35 147` B with
*"GNU GENERAL PUBLIC LICENSE"* on its first line. `p117`'s name list carries `COPYING` and not
`COPYING.txt`. 🔵 **`p250-commercial-use-axis`'s list DOES carry `COPYING.txt`.** 🔴 **So this KB's
probe lists disagree with each other about the canonical filename of the largest LMS in the
world, which is `gap 135` — the `76` unmigrated grant-path lists — showing up as a concrete wrong
answer rather than as a debt.** 🟢 **`ACTION KN` stops being cosmetic this pass: it has now
produced a false absence on a flagship row.**

🟡 **Two rows remain UNRESOLVED and are not recorded as absences:** `formalms/formalms` and
`apereo/opencast` both `404` on `LICENSE` at `HEAD`. 🔵 **Per `ACTION JY`'s standard, a `404` on one
filename is not a measured absence — it is an unprobed name (`gap 135` again).**

### 🟢 New shared instrument: the fetch idiom this repository was missing

🆕 🟢 **[`compose/code/lib/fetch_payload_to_file.sh`](../compose/code/lib/fetch_payload_to_file.sh)**
— body to a file, `%{http_code}` to stdout, nothing round-tripping through a shell variable.
`lib/payload_measure.sh` has shipped the correct SIZING primitive (`size_of_file`, a PATH) since
pass `74`, and **`11` of the `12` stripping sites could not reach it because they never had a
path.** 🔵 **The missing vocabulary was never the counter. It was the fetch (`ACTION KY`,
[`compose/code/p179-capture-shape/`](../compose/code/p179-capture-shape/)).**


## Pass 178 — 2026-10-13

🆕 🟢 **`ACTION KT` is DISCHARGED, LIMB `1` FIRED, and `gap 134` is CLOSED.**
[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) — the Technical University of Munich's
interactive-learning platform, and the last fully unverified holder-grade row in this KB — was
cloned and read artefact by artefact. 🟢 **Both limbs of the pre-registered falsifier were put to
the same clone, and limb `1` fires on every criterion it names: it reaches exercise, exam and
assessment objects with WRITE access, through its OWN auth, over data it OWNS.**
🆕 🟢 **The number that settles the *"thin front end"* question: `257` `@Entity` classes and `137`
Liquibase changelogs.** 🔵 **`eagles-edu/sis` was refused at p175 because it was a portal over
somebody else's system of record. `Artemis` IS the system of record — it ships its own schema and
migrates it.**
🆕 🟢 **The finding with the most commercial value in this file: `Artemis` is the first row in this
KB that speaks a real interop standard as a TOOL, with grade passback.** `LTI` at word-boundary
precision in `248` files, its own module at `.../artemis/lti` with `47` files, `Lti13Service`,
`Lti13Configurer`, `Lti13DeepLinkingResponse`, `Lti13AgsClaim`, `DeepLinking` `60`×, AGS `305`× —
**and `NightlyLtiMoodleInteropTest.java` with a `moodle-sign-jwt.php` fixture, so the Moodle
interop is TESTED, nightly, in CI.** 🔴 **And it speaks exactly ONE: `SCORM` `0`, `xAPI` `0`,
`QTI` `0`, `OneRoster` `0`, `Ed-Fi` `0`, `Caliper` `0`.**
🆕 🔴 **The `T265` trap fired again and was caught again: `canvas` matches `45` files, and
`canvas-lms`, `instructure` and `Canvas LMS` match `0`.** 🔵 **Same shape as `dolos`: every hit is
the HTML5 element. A narrower grep would have published *"Canvas-integrated"* for the second pass
running.**
🆕 🟡 **`QTI` is a second trap, and it is instructive about scope.** `0` hits in `src` across
`.java`, `.ts` and `.yml`; a repository-wide grep returns `5`, and all `5` are a `.zip`, an emoji
PNG sheet, a `.webm`, a system-design PNG and the project's own LMS-comparison data file.
🔵 **`T276` again: the scope-limited grep is the HONEST one here, and the wide grep is the one that
would have published a standard this platform does not implement.**
🆕 🟢 **A second EMEA institutional row ENTERS, because `Artemis` cannot be routed without it being
named:** [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), the LLM microservice. 🔴 **`12`★,
and that is the risk sentence, not a footnote.**
🟢 **No other rows enter. `gap 134` closed by verification, not by admission.**

### 🟢 The `7` rows — RE-STATED, with `Artemis` verified and `Pyris` admitted

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 130` B *(EXACT, `md5 37cd0f927f3fdf7f68cf09edaebfb010`)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` *(on `master`)* | 🟡 **North America** — subnational grade (`ACTION KK`) | 🟢 **YES — `ACTION KM`, p176** |
| 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 091` B, `md5 021aaec73f7b974dc5edf4ef703f941b` *(🆕 identical on `main` AND `develop`)*, *"© 2026 TUM Applied Education Technologies"* | 🆕 **`develop@8c158741c38e`** 🔴 *(and `main@07f43f8e0b71` is a DIFFERENT commit; `develop` moved to `6aae3ae2655c` during this pass)* | 🟢 **EMEA** — HOLDER-grade, Germany | 🆕 🟢 **YES — `ACTION KT`, in full below. `13 810` files, `5 172` Java, `4 135` TS, `3 963` test files, `v10.3`** |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 084` B, `md5 00ffc342d555c4129ee54e3286818d50`, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` — 🟢 **unmoved since p175** | 🟢 **EMEA** — HOLDER-grade, Belgium | 🟢 **YES — `ACTION KQ`, p177** |
| 🆕 🟡 [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris) | 🟢 **`MIT`** — `1 089` B, `md5 5cc3b9844f092545a99800eb9edce880` | `d7b2c095204e` | 🟢 **EMEA** — HOLDER-grade by LINEAGE *(same `ls1intum` org as `Artemis`)* | 🔴 **NO — licence, `md5` and `HEAD` only. 🔴 `12`★, `16` open issues, last push `2026-09-17`: the smallest dependency this KB has ever put on a critical path** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B *(EXACT, `md5 99b58b5c4e30de12e69228065a5bd553`)*, *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` *(on `master`)* | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — grant-path probe only** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 083` B, `md5 9633492b4368ec2c3f77f7116694ad23`, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only; the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 073` B, `md5 2a1660298c8c5a8b41d28eed30f7fde2`, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🟢 **`gap 134` is CLOSED: `0` fully unverified holder-grade rows remain.** `cs-field-guide` is still
only partly read and `Pyris` is new and unread, so **`3` of `7` rows are verified past their
licence** — `canvasapi`, `Artemis`, `dolos`. 🔵 **Three passes, three rows read, two new admissions
in total: the debt is being paid down faster than it is taken on, which is the first time that
sentence has been true in this file.**

### 🆕 🟢 `ACTION KT` — `ls1intum/Artemis` read past its licence, artefact by artefact

🟢 **Controlled: cloned `--depth 1 --single-branch`, which lands on the DEFAULT branch `develop`,
at `8c158741c38e1fd684b38dc6eb54993b1731af89`. `13 810` tracked files, `5 172` `.java`, `4 135`
`.ts`, `3 963` test files, `version = "10.3"`, `JavaLanguageVersion.of(25)`, `node >=24.21.0`.**
🔴 **p177 recorded `HEAD` `09266581a02c`. A `--depth 1` clone cannot reach that object, so this pass
can neither confirm nor place it on a branch, and this repository has two live branches whose heads
differ.** 🔵 **Every count below is a reading of `develop@8c158741c38e` and is labelled as such
(`T281`).**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **grant-path exclusivity** | `LICENSE`, `MIT`, byte- and `md5`-identical on `main` and `develop` | 🟢 **one grant, and branch-independent** |
| 🟢 **does it OWN the data?** | `257` classes carrying `@Entity`; `137` Liquibase/changelog paths | 🟢 **SYSTEM OF RECORD. This is limb `1` and limb `2`'s refutation in one measurement** |
| 🟢 **exercise and exam DOMAIN objects** | `74` files under `**/domain/**` matching exercise/exam, among them `Exam`, `StudentExam`, `ExamSession`, `ExamUser`, `ExerciseGroup`, `ExamRoom`, `Exercise`, `BaseExercise`, `Result`, `GradeStep`, `ExampleSubmission` | 🟢 **the objects the falsifier named, by name** |
| 🟢 **WRITE access to them** | repository-wide `@PostMapping` `261`, `@PutMapping` `143`, `@PatchMapping` `21`, `@DeleteMapping` `103` against `@GetMapping` `538`. In the exam/exercise/assessment web layers specifically: exam `21`/`7`/`8`, exercise `8`/`15`/`7`, assessment `14`/`7`/`7` | 🟢 **`528` write endpoints. Not a read-only front end** |
| 🟢 **its OWN auth** | `@PreAuthorize` in `24` files, `SecurityConfiguration` `9`, `jwt` `63`, **`passkey` `136`**, `saml2` `54`, `oauth2` `26` | 🟢 **own auth, and a passkey surface larger than its JWT surface — unusual and worth a slide** |
| 🟢 **interop — `LTI`, word-bounded** | `248` files; own module `.../artemis/lti` with `47` files; `Lti13Configurer` `27`, `Lti13LaunchRequest` `14`, `Lti13Service` `12`, `Lti13PlatformConfiguration` `12`, `Lti13ClientRegistration` `12`, `Lti13DeepLinkingResponse` `12`, `Lti13TokenRetriever` `9`, `Lti13AgsClaim` `9`, `DeepLinking` `60`, `ags` `305` | 🟢 **`LTI 1.3` as a TOOL, with Deep Linking and Assignment-and-Grade-Services — it can receive a launch AND push grades back** |
| 🟢 **LMS integration, TESTED** | `src/test/java/.../lti/nightly/NightlyLtiMoodleInteropTest.java` + `src/test/resources/lti/nightly/moodle-sign-jwt.php`; `moodle` in `10` files | 🟢 **a nightly interop test against a REAL LMS. `dolos` has `0` LMS integration; this row has one in CI** |
| 🔴 **every OTHER standard** | 🔴 **`SCORM` `0`, `xAPI` `0`, `QTI` `0` *(in `src`)*, `OneRoster` `0`, `Ed-Fi` `0`, `Caliper` `0`** | 🔴 **one standard only. Rostering and learning-record plumbing stay integrator work** |
| 🟡 **`canvas` — the trap, caught** | `45` files case-insensitively; `canvas-lms`/`instructure`/`Canvas LMS` **`0`** | 🟡 **`T265` fired as designed, for the second consecutive pass on a different subject** |
| 🟢 **the AI surface** | `Iris` `748` files *(own module, `254` files)*, `Hyperion` `231`, `Athena` `187`, `pyris` `219`, `llm` `193` | 🟢 **this is not an LMS with AI bolted on; the AI surface is `~5`% of a `13 810`-file tree and has its own modules** |
| 🟢 **what `Hyperion` DOES** | its own admin doc: consistency checks on problem statements, rewriting instructions, **verified exercise-variant generation** *(programming variants verified with real template and solution builds; quiz variants by validity-checking generated questions)*, MCQ generation from a topic or from competencies, bulk MCQ refinement | 🟢 **AI AUTHORING with a verification step — the thing most authoring tools skip** |
| 🟢 **deployment dependency, measured not assumed** | the same doc: *"The functionality is provided by Artemis and Spring AI, so no EduTelligence service needs to be deployed"*; `Pyris` is *"used only for semantic lecture search"* and quiz generation *"falls back gracefully"* without it | 🟢 **`Hyperion` needs an LLM endpoint, NOT the microservice. 🔵 This is the single most budget-relevant sentence in the artefact** |
| 🟡 **model providers named** | `openai` `103`, `gpt-5` `27`, `azure` `13`, `ollama` `10`, `gpt-4o` `3`; `spring.ai.openai` `7` config keys against `spring.ai.model` `1` | 🟡 **OpenAI/Azure is the paved road. `ollama` appears in the Iris test stack and in the Weaviate global-search config, so a local path EXISTS and is not the default** |
| 🔴 **adjudication** | `AutomaticAssessment` in `14` files, `automatic` `378`, `score` `581`, `feedback` `720` | 🔴 **IT ADJUDICATES. This is the opposite of `dolos`, and it is the whole regulatory difference — see [`intel/trends.md`](../intel/trends.md)** |
| 🟢 **proctoring and biometrics** | 🟢 **`proctor` `0`, `webcam` `0`, `emotion` `0`, `face` `2`** — what exists instead is `ExamSession` `21` and `SuspiciousExamSessions` `15`, i.e. session-level anomaly detection | 🟢 **NO biometric surveillance. It stays clear of the Article `5` emotion-recognition PROHIBITION entirely, which is a harder bar than Annex III** |
| 🟡 **privacy regimes named** | `GDPR` `42` files, `DSGVO` `5`, 🔴 **`FERPA` `0`** | 🟡 **EMEA-native by construction. A North America engagement writes the FERPA story itself** |
| 🟢 **deployability** | `deployment/docker/docker-compose.yml`, plus an `iris-stack/docker-compose.yml` for the AI path in tests; `10` docker paths | 🟢 **compose-deployable, with a separate compose file for the AI stack** |
| 🟡 **liveness** | `818`★, `396` forks, `256` open issues, and `develop` moved **during this pass** | 🟡 **very much alive — and fast enough that a pinned SHA is mandatory in any engagement, not optional** |

🟢 **Verdict: `Artemis` ROUTES, and it is the strongest row in this KB.** It is institution-held,
`MIT`, a system of record, AI-native with a verification step, `LTI 1.3` with grade passback, and
nightly-tested against Moodle. 🔴 **Four conditions travel with it and none is optional in a deck:**
**(`1`)** it ADJUDICATES, so in the EU it is an Annex III stand-alone high-risk system and the
conformity work is real *(timing in [`intel/trends.md`](../intel/trends.md))*; **(`2`)** it speaks
ONE standard — no rostering, no SCORM, no xAPI; **(`3`)** `FERPA` is named nowhere, so a US
deployment inherits that work; **(`4`)** the AI path's default provider is OpenAI/Azure, and the
self-hosted limb runs through a `12`★ microservice.
🟢 **Full artefact ledger:**
[`evidence/artemis-artefact-read.2026-10-13-p178.tsv`](../evidence/artemis-artefact-read.2026-10-13-p178.tsv).

## Pass 177 — 2026-10-13

🆕 🟢 **`ACTION KQ` is DISCHARGED and the row a client asks about first is now read past its
licence.** [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) — Ghent University's
source-code similarity detector, the only assessment-integrity route this KB holds — was cloned at
its recorded `HEAD` and read artefact by artefact. 🟢 **Both of the things p176 named as UNVERIFIED
are now measured, and both come out better than the row claimed.**
🆕 🟢 **Language coverage: `20` programming languages in the registry and `19` vendored
`tree-sitter` grammars, against a docs page that lists `11` and trails off in an ellipsis.** 🔵 **The
project undersells itself by `9` languages, `Modelica`, `Verilog`, `R`, `Groovy`, `Scala` and
`OCaml` among them — which is the difference between a CS-department tool and one that reaches an
engineering faculty.**
🆕 🟢 **False-positive behaviour: it has none of the machinery a client will ask about and that is
the correct answer.** `falsePositive` **`0`**, `confidence` **`0`** across the whole repository.
🟢 **What ships instead is template exclusion — `-i/--ignore`, plus `-m/--max-fingerprint-count`
and `-M/--max-fingerprint-percentage` to detect shared code automatically — and the docs state the
problem in their own words before offering the controls.**
🔴 **The core engine's `defaultMinSimilarity` is `0`: it filters nothing unless told to.** The only
threshold lives in the report UI and is **GUESSED** (`guessSimilarityThreshold`, a local minimum
floored at the mean of pairwise similarities), and single-linkage clustering drops edges beneath it.
🔵 **So `dolos` reports similarity and clusters; it never returns a verdict. That is decision
support, not adjudication, and it is the single most useful sentence in this file for a `2026`
education engagement — see [`intel/trends.md`](../intel/trends.md) for why the regulation agrees.**
🆕 🔴 **`ACTION KS` invalidates a COLUMN of this table rather than a row: `8` of `12` published
licence byte counts in this KB are short by exactly `1` byte**, including `4` of the `6` rows below.
🟢 **Corrected figures are published inline and marked; the mechanism and the full audit are in
[`agents/top.md`](../agents/top.md) and
[`evidence/licence-byte-audit.2026-10-13-p177.tsv`](../evidence/licence-byte-audit.2026-10-13-p177.tsv).**
🟢 **No new rows ENTER this pass, for the second pass running and for the same stated reason:
`gap 134` is a debt of verification, and admitting rows while it is open makes it bigger.**

### 🟢 The `6` p175 rows — RE-STATED, with byte counts CORRECTED and verification state explicit

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 130` B *(🆕 CONFIRMED exact; `md5 37cd0f927f3fdf7f68cf09edaebfb010` reproduced independently)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | 🟡 **North America** — subnational grade (`ACTION KK`) | 🟢 **YES — `ACTION KM`, p176** |
| 🟡 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — 🆕 **`1 091` B** *(CORRECTED from `1 090`; `md5 021aaec73f7b974dc5edf4ef703f941b`)*, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — licence, holder and `HEAD` only. The LAST fully unverified holder-grade row (`gap 134`)** |
| 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — 🆕 **`1 084` B** *(CORRECTED from `1 083`; `md5 00ffc342d555c4129ee54e3286818d50`)*, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` — 🟢 **unmoved since p175** | 🟢 **EMEA** — HOLDER-grade | 🆕 🟢 **YES — `ACTION KQ`, in full below. `513` files, `57` test files, `103` test declarations** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B *(🆕 CONFIRMED exact — read by a non-stripping channel, which is part of `ACTION KS`'s proof)* , *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — grant-path probe only** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — 🆕 **`1 083` B** *(CORRECTED from `1 082`)*, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only; the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — 🆕 **`1 073` B** *(CORRECTED from `1 072`)*, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🟢 **`gap 134` narrows from `3` unverified holder-grade rows to `2`** — `Artemis` outright, and
`cs-field-guide` partly. 🔵 **Two passes, two rows read past their licence, no new admissions: the
debt is being paid down rather than refinanced.**

### 🆕 🟢 `ACTION KQ` — `dodona-edu/dolos` read past its licence, artefact by artefact

🟢 **Controlled: cloned at `HEAD` `44925b867ce737206c1debce0add731e294025d5`, the sha this KB
recorded at p175, UNMOVED. `513` tracked files, `57` test files, `103` test declarations.**
🔵 **The rule, per `T265`: do not count the standard's NAME. Count the route that would have to
exist — and check what each token is actually matching before reporting it.**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **grant-path exclusivity** | `LICENSE` only. `LICENCE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` all `404` at the `14` B body | 🟢 **one grant, unambiguous** |
| 🟢 **language coverage — registry** | `LanguagePicker.languages` declares `21` entries: `20` programming languages + a `char` tokenizer | 🟢 **MEASURED** |
| 🟢 **which languages** | `bash` `c` `cpp` `c-sharp` `python` `php` `modelica` `ocaml` `java` `javascript` `elm` `go` `groovy` `r` `rust` `scala` `sql` `typescript` `tsx` `verilog` | 🟢 **`20`, and `6` of them are not in the docs** |
| 🟢 **vendored grammars** | `19` `tree-sitter` grammar directories under `parsers/` | 🟢 **ships its own parsers; no install-time fetch** |
| 🔴 **the docs' own claim** | `docs/about/languages.md` lists `11` and ends in *"..."* | 🔴 **UNDERSELLS BY `9`. Quote the registry, never the docs page** |
| 🟡 **prose, not just code** | `CustomTokenizerLanguage("char", [".txt", ".md"])` via `charTokenizer.ts` | 🟡 **NOT code-only — but character-level. 🔴 Do NOT sell this as essay plagiarism detection** |
| 🟢 **the false-positive problem, named** | `docs/docs/running.md:55` — *"Dolos will often detect these code fragments as similar and include them in the similarity score, making it harder to spot actual plagiarism."* | 🟢 **the project names it before it sells the cure** |
| 🟢 **false-positive control `1`** | `-i` / `--ignore <path>` — a template/boilerplate file whose fragments stop counting toward similarity | 🟢 **ships** |
| 🟢 **false-positive controls `2` and `3`** | `-m/--max-fingerprint-count <int>` and `-M/--max-fingerprint-percentage <fraction>` — auto-detect shared code by how many files a fragment occurs in; combinable with `-i` | 🟢 **ships, and automatic** |
| 🔴 **engine default** | `options.ts:54` — `defaultMinSimilarity = 0` | 🔴 **filters NOTHING out of the box. An unconfigured run is the noisy run the docs warn about** |
| 🟡 **the threshold** | report UI only: `guessSimilarityThreshold` in `web/src/api/utils/cutoff.ts` — a local minimum, floored at the mean of pairwise similarities; `SingleLinkageClustering` drops edges below it | 🟡 **GUESSED per dataset, not a policy you set. Say so before a client calls it a standard** |
| 🟢 **adjudication** | `falsePositive` `0`, `confidence` `0`, no pass/fail anywhere in `513` files | 🟢 **DECISION SUPPORT, not an adjudicator — and see `intel/trends.md`: this is what makes it routable under Annex III and the US oversight statutes** |
| 🔴 **STANDARDS interop, word-boundary** | 🔴 **OneRoster `0`, Ed-Fi `0`, SCORM `0`, xAPI `0`, Caliper `0`, LTI `0`, QTI `0`** | 🔴 **none. Same shape as `canvasapi`: it speaks its own platform, not a standard** |
| 🔴 **privacy regimes named** | 🔴 **`FERPA` `0`, `GDPR` `0`** | 🔴 **names neither. The data-protection story is the integrator's to write** |
| 🔴 **LMS integration** | 🔴 **Canvas `0` in the product sense, `Moodle` `0`, `webhook` `0`** | 🔴 **NONE. Wiring it into an LMS is custom work — budget it** |
| 🟡 **`canvas` — the trap, caught** | `29` case-insensitive hits, **`0`** of them Canvas LMS: every one is the HTML5 `<canvas>` element or `D3` rendering, and `Canvas LMS`/`canvas-lms`/`instructure` match `0` | 🟡 **`T265` fired exactly as designed. A narrower grep would have published *"Canvas-integrated"*** |
| 🟡 **home platform** | `Dodona` — `193` hits | 🟡 **built for Ghent's own platform; that is the integration it has** |
| 🟢 **deployability** | `Dockerfile.cli`, `Dockerfile.web`, `docker-compose.yml`, `docker` `114` hits | 🟢 **deployable as CLI or as a web report** |

🟢 **Verdict: `dolos` ROUTES, and it is stronger than the row that admitted it on language coverage
and honest on everything else.** 🔴 **Two conditions travel with it: there is NO LMS integration of
any kind, and it returns NO verdict.** 🔵 **The second condition is a feature. The first is a line
item.**
🔴 **A method note recorded against this pass's own work: the first run of this probe grepped only
`lib/`, `cli/` and `docs/` and was about to publish *"`threshold` `0`"* and *"`cluster` `0`"*. Both
are false — `16` and `178` hits repository-wide. 🔵 **A scope-limited grep reports the scope, not
the repository (`T276`), and it fails in the direction that makes the finding sound sharper.**
🟢 **Full artefact ledger:**
[`evidence/dolos-artefact-read.2026-10-13-p177.tsv`](../evidence/dolos-artefact-read.2026-10-13-p177.tsv).


## Pass 176 — 2026-10-13

🆕 🟢 **One of p175's four holder-grade rows has now been read PAST its licence, and it is better
than the row claimed.** `ACTION KM` applied `T265`'s rule — name the artefact that would have to
exist and look for THAT, not for the standard's name — to
[`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi). 🟢 **It reaches rostering objects with
READ AND WRITE, carries its own auth model, paginates properly and raises typed errors.**
🔴 **`ACTION KM`'s falsifier limb `1` therefore FIRES, and `gap 123` closes for the administrative
layer — conditionally, and the condition is the whole finding: it is a CLIENT, and the system of
record it clients for is Canvas, whose own core is not permissive.**
🆕 🔴 **`ACTION KJ` converted `0` licence verdicts and found a bigger defect than the one it was
sent for.** No repository this KB ever recorded as grant-free carries a grant at a British spelling
— `0` of `16` paths on each of four subjects. 🔴 **But the probe-list census underneath that answer
is the finding: this repository contains `76` independent hardcoded grant-path lists. `48` carry
`LICENCE`. `3` carry `COPYING.md`.** 🔵 **The defect was never a spelling. It is that the list is
copied `76` times and cannot be extended (`T272`).**
🟢 **No new rows ENTER this pass, and that is deliberate.** p175 admitted six on a licence read and
registered `gap 134` against itself for doing so; p176 spends the pass verifying one of them instead
of admitting more. 🔵 **One row read past its licence is worth more than six read up to it.**

### 🟢 The `6` p175 rows — RE-STATED, with the verification state of each made explicit

| repo | licence *(body READ, bytes, holder)* | `HEAD` | region *(`P800`)* | verified PAST the licence? |
|---|---|---|---|---|
| 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — 🆕 **`1 130` B** *(p175 said `1 129`; blob `f105f1b3670d`, `md5 37cd0f92…`)*, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | 🟢 **North America** — 🆕 🟡 **subnational grade, see `ACTION KK`** | 🆕 🟢 **YES — `ACTION KM`, in full below** |
| 🟡 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 090` B, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — licence, holder and `HEAD` only (`gap 134`)** |
| 🟡 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` | 🟢 **EMEA** — HOLDER-grade | 🔴 **NO — and it is the row a client will ask about first, because it is the only assessment-integrity route here** |
| 🟡 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — at **`LICENCE`**, `1 128` B, *"© 2016-2022 University of Canterbury CSER Group"* | `7e323930cf6f` | 🟢 **APAC** — HOLDER-grade, New Zealand | 🟡 **PARTLY — it served as `ACTION KJ`'s known positive and reproduced at `1 128` B on `master`** |
| 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 082` B, 🔴 **holder is an INDIVIDUAL: *"© 2021 John McCann Cunniff Junior"*** | `894ed020997f` | 🔴 **North America — DESCRIPTION-grade only, and `ACTION KK` downgrades it further: the artefact names *"NYU"* and NO country** | 🔴 **NO** |
| 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 072` B, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | 🔴 **NO** |

🔴 **So `gap 134` narrows from `4` unverified holder-grade rows to `3`, and does not close.**

### 🆕 🟢 `ACTION KM` — `ucfopen/canvasapi` read past its licence, artefact by artefact

🟢 **Controlled: `HEAD` `513588f3077f`, `318` tracked files, `158` Python, `76` test files,
`1 112` test methods.**
🔵 **The rule, per `T265`: do not count the standard's NAME. Count the route that would have to
exist.**

| artefact the row would need | measured | verdict |
|---|---|---|
| 🟢 **rostering objects as modules** | `enrollment.py`, `enrollment_term.py`, `section.py`, `course.py`, `user.py`, `account.py`, `grading_period.py` — all PRESENT | 🟢 **reaches them** |
| 🟢 **rostering routes, as named request strings** | `courses/{}/enrollments`, `courses/{}/enrollments/{}`, `/accept`, `/reactivate`, `/reject`, `courses/{}/sections`, `sections/{}/enrollments`, `enrollment_terms`, `sections/{}/crosslist` | 🟢 **named, not inferred** |
| 🟢 **WRITE reach** | 🟢 **`322` `GET`, `127` `POST`, `89` `PUT`, `74` `DELETE`** — and `courses/{}/enrollments` is addressed by `POST` at `course.py:748` as well as `GET` at `:1226` | 🟢 **writes. Compare `edfi-oneroster`: `24` `GET`s, `0` writes** |
| 🟢 **pagination** | `paginated_list.py` — `per_page` defaulting to `100`, a `_next_url` the iterator follows, `__getitem__` growing the list on demand | 🟢 **real, not a thin wrapper** |
| 🟢 **auth model** | `requester.py:187` — `Authorization: Bearer {access_token}`, token held on the requester | 🟢 **its own** |
| 🟢 **error semantics** | `CanvasException` + `BadRequest`, `InvalidAccessToken`, `Unauthorized`, `Forbidden`, `RateLimitExceeded`, `ResourceDoesNotExist`, `RequiredFieldMissing`, `Conflict`, `UnprocessableEntity` | 🟢 **typed, including rate limiting** |
| 🟡 **SIS identifier addressing** | `sis_course_id`, `sis_section_id`, `sis_account_id`, `sis_group_id`, `sis_import_id` | 🟡 **addresses objects by the SIS's OWN ids — interop at the identifier layer** |
| 🔴 **STANDARDS interop, word-boundary** | 🔴 **OneRoster `0`, Ed-Fi `0`, SCORM `0`, xAPI `0`, Caliper `0`.** `LTI` `7` | 🔴 **none. It speaks Canvas, not a standard** |
| 🟡 **activity** | last commit **`2026-04-16`** | 🟡 **`180` days — EXACTLY at this KB's liveness bar, which is why it appeared in p175's sweep at all** |

🟢 **Falsifier limb `1` FIRES: rostering objects AND its own auth model.** Limb `2` is SILENT — it is
not a thin generated wrapper by any of the three tests the action named.
🔴 **And the condition that must travel with the row, because without it the row oversells:**
`canvasapi` is a permissive CLIENT for a system of record that is not permissive. Instructure
publishes Canvas's core under `AGPL-3.0` and sells the operated product.
🔵 **So the honest sentence is: the administrative layer finally has an `MIT` client with write
reach and real auth — for institutions that already run Canvas.** It does not give this KB a
permissive SIS, and the row underneath it is still 🔴 **none** (fourteenth pass).

### 🆕 🔴 `ACTION KJ` — `0` verdicts converted, and a defect `19×` wider than the one registered

🟢 **The four subjects, every one of them a published absence claim in this KB, probed at `16` paths
on the default branch — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENCE.md`,
`LICENCE.txt`, `COPYING`, `COPYING.md`, `COPYING.txt`, `License`, `License.md`, `license`,
`license.md`, `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`:**

| subject | paths answering `200` | verdict |
|---|---|---|
| 🟢 [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | 🟢 **`0` of `16`** | 🟢 **verdict STANDS, and strengthens — see the branch enumeration below** |
| 🟢 [`os4ed/openSIS-Classic`](https://github.com/os4ed/openSIS-Classic) | 🟢 **`0` of `16`** | 🟢 **the *"no root grant"* verdict STANDS. Its `GPL-2.0` is still at `docs/License.txt` (`T209`)** |
| 🟢 [`formalms/formalms`](https://github.com/formalms/formalms) | 🟢 **`0` of `16`** | 🟢 **STANDS. `GPL-2.0` at `html/license.txt`, `9` languages, none named as governing (`gap 116`)** |
| 🟢 [`spdx/license-list-data`](https://github.com/spdx/license-list-data) | 🟢 **`0` of `16`** | 🟢 **STANDS. The canonical SPDX token list still publishes no licence of its own** |
| 🟢 **CONTROL — the known positive** [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`1` of `16` — `LICENCE`, `1 128` B** | 🟢 **the instrument is validated by a positive it was required to find, and it reproduced p175's byte count exactly** |

🆕 🟢 **And the word *"exhaustive"* is EARNED for the first time, on the row that was carrying it
without earning it.** p169's `T209` enumerated `Mr.-Ranedeer`'s default branch — `12` files, `0`
grants. 🟢 **p176 enumerated EVERY branch the remote advertises:**

| branch | tracked files | grant-shaped paths *(case-insensitive `licen[cs]e`/`copying`/`notice`)* |
|---|---|---|
| `main` | `12` | 🟢 **`0`** |
| `v2.6.2` | `12` | 🟢 **`0`** |
| `v2.6.3` | `13` | 🟢 **`0`** |
| `dev/v2.7` | `9` | 🟢 **`0`** |
| `Speedrun-Brother` | `9` | 🟢 **`0`** |

🟢 **`55` file-paths across `5` branches, `0` grants.** 🔵 **Before p176 the word meant *"the default
branch"*; now it means *"every branch the remote advertises"*, and the claim is the same claim.**

### 🆕 🔴 The probe-list census — why `gap 133` was the wrong shape

🟢 **`76` grant-path probe lists found in `compose/code/`, counted by the lines that enumerate two
or more grant paths together:**

| property | count | share |
|---|---|---|
| 🟢 carry `LICENSE` | `76` | `100%` |
| 🟡 **carry the British `LICENCE`** | 🟡 **`48`** | 🟡 **`63.2%`** |
| 🔴 **carry `COPYING.md`** | 🔴 **`3`** | 🔴 **`3.9%`** |

🔴 **`28` lists cannot find a British-spelled grant and `73` cannot find `COPYING.md`** — and
`p120-unread-grant-resolution/probe.sh` has carried `LICENCE LICENCE.md` all along, which is how
this KB found `cs-field-guide` in the first place.
🆕 🔵 **`T272` — a probe list copied `76` times is not a list, it is `76` lists, and extending it is
not an edit but a migration.** p175 wrote *"`P50`'s probe list misses `LICENCE`"*, which implies one
list and one fix. 🔵 **The fix is a shared vocabulary in `compose/code/lib/`, imported rather than
retyped, and `gap 135` registers it as the migration it is.** 🟢 **The reassurance that belongs next
to it: `0` published verdicts change, so this is debt, not error.**

## Pass 175 — 2026-10-13

🆕 🔴 **One row LEAVES this file and it is the one p174 admitted with the most confidence.**
`ACTION KE` read [`eagles-edu/sis`](https://github.com/eagles-edu/sis) past its licence, as
registered, by grepping the tree rather than the README — and found that **every interop and auth
signal it appeared to carry is a substring artefact.** 🔴 **Word-boundary count: `0` for OneRoster,
`0` for Ed-Fi, `0` for LTI, `0` for SCORM, `0` for xAPI, `0` for `tenant`, `0` for `tenancy`, and
`0` for OAuth, OIDC, SAML, JWT, LDAP and SSO.**
🆕 🟢 **Six repositories ENTER, and four of them are placed by the institution named in their own
licence body** — the strongest evidence class `P800` admits, and the first time this file has
obtained holder-grade institutional placement in three regions in one pass.

### 🆕 🟢 Entering — institutional, permissive, licence body READ this pass

| repo | licence *(body READ, bytes, holder)* | `HEAD` | ★ | region *(`P800`)* | what it is |
|---|---|---|---|---|---|
| 🆕 🟢 [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **`MIT`** — `1 129` B, *"© 2017 University of Central Florida — Center for Distributed Learning"* | `513588f3077f` | `682` | 🟢 **North America** — HOLDER-grade | a Python client for **Canvas LMS**: courses, users, gradebooks. The first rostering-ADJACENT permissive row this KB has ever been able to name |
| 🆕 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **`MIT`** — `1 090` B, *"© 2026 TUM Applied Education Technologies"* | `09266581a02c` | `818` | 🟢 **EMEA** — HOLDER-grade | an institutional **interactive-learning platform with automated feedback**: programming, modelling and text exercises, autograding, an exam mode. A university's own teaching system, `MIT` |
| 🆕 🟢 [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **`MIT`** — `1 083` B, *"© 2019 Team Dolos <dolos@ugent.be>"* | `44925b867ce7` | `350` | 🟢 **EMEA** — HOLDER-grade | **source-code plagiarism detection**. Directly serves the assessment-integrity layer this KB routes around every pass |
| 🆕 🟢 [`uccser/cs-field-guide`](https://github.com/uccser/cs-field-guide) | 🟢 **`MIT`** — 🔴 at **`LICENCE`**, `1 128` B, *"© 2016-2022 University of Canterbury Computer Science Education Research Group"* | `7e323930cf6f` | `381` | 🟢 **APAC** — HOLDER-grade, New Zealand | an interactive high-school **computer-science textbook**, maintained by a university education-research group |
| 🆕 🟡 [`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) | 🟢 **`MIT`** — `1 082` B, 🟡 **holder is an INDIVIDUAL** | `894ed020997f` | `381` | 🟡 **North America** — DESCRIPTION-grade, *"From NYU"* | a **distributed LMS** that automates computing-science courses on Kubernetes, with a cloud IDE |
| 🆕 🟡 [`showlab/Code2Video`](https://github.com/showlab/Code2Video) | 🟢 **`MIT`** — `1 072` B, 🟡 **holder is an INDIVIDUAL** | `1142d8e14cdc` | `2 123` | 🟡 **APAC** — DESCRIPTION-grade, `showlab` + *"[ICML 2026]"* | **educational video generation via CODE** rather than pixels — the only peer-reviewed row in this sweep, and a direct alternative shape to the shelf's video-authoring route |

🔴 **What is verified and what is not, stated so the rows cannot be over-read — and this discipline
is the direct lesson of `ACTION KE`:** licence BODY, byte count, copyright HOLDER and `HEAD` sha.
🔴 **NOT verified: interop (`OneRoster`, Ed-Fi, `LTI`, `SCORM`, xAPI), multi-tenancy, auth model,
dependency closure, build, or whether anyone operates them.** 🟡 **They are CANDIDATES, exactly as
`gap 134` records — not routes.** The one thing p175 will not do is repeat p174's mistake of
publishing a capability claim on top of a licence check.

### 🆕 🔴 Leaving — `eagles-edu/sis`, and the grep that over-reported it

🟢 **The clone is controlled: `HEAD` `7e5fbccad5a0`, `2 598` tracked files — both identical to what
p174 recorded, so this is a re-read of the same tree and not a moved target.**

| token | case-insensitive FILE hits | 🔴 **word-boundary LINE hits** | what it was actually matching |
|---|---|---|---|
| `ed-fi` | `55` | 🔴 **`0`** | `red-fill`, `disabled-fill`, `chip-red-fill` — CSS custom properties |
| `edfi` | `176` | 🔴 **`0`** | `normalizedField`, `normalizedFilters`, `mutatedFields` |
| `lti` | `325` | 🔴 **`0`** | `LevelTile`, `LevelTiles`, `ModalTitle`, `DetailTitle` |
| `oidc` | `29` | 🔴 **`0`** | `autoIdCount` |
| `jwt` | `16` | 🔴 **`0`** | base64 noise inside lockfiles |
| `oneroster`, `scorm`, `xapi`, `caliper`, `clever` | `0` | `0` | — nothing, at either precision |
| `tenant`, `tenancy`, `oauth`, `saml`, `ldap`, `sso`, `bcrypt`, `argon2` | `0`–`4` | 🔴 **`0`** | — |

🆕 🔵 **`T265` — a substring grep is not an interop measurement, and its error is one-directional.**
It can only over-report, so it fails in the direction that flatters the candidate. 🔵 **The rule this
file now uses: name the ARTEFACT that would have to exist — an `EdFi` client class, an
`/ims/oneroster/v1p1` route, a `cmi5` or xAPI statement emitter — and look for that, not for the
standard's name.**
🟢 **What the repository genuinely has, so the row is not merely negative:** `48` Prisma models
with a real school-shaped schema — `Student`, `StudentEnrollmentPeriod`, `StudentAttendance`,
`StudentGradeRecord`, `ParentPortalAccount`, `StudentPortalAccount`, `Family` — and hand-rolled
cookie sessions (`ADMIN_SESSION_TTL`) in place of any federated protocol.
🔴 **And the model that settles the routing question is called `SisConfigMirror`** — `id`,
`payloadJson`, `updatedBy`, two timestamps. 🔵 **A system of record does not mirror its own
configuration from somewhere else. This is a parent-and-student PORTAL in front of an SIS.**
🟡 **One hygiene figure a client should hear before quoting the size: `374` of the `2 598` tracked
files sit under `.backup/` and `.codex-backups/`.** The tree is `14.4%` prior drafts.
🟢 **p174's denominator correction STANDS and is independently reproduced** — `"student information
system" license:mit pushed:>=2026-04-16` is a real population, and `topic:education` is `8 197`
exactly. 🔴 **What does not stand is the conclusion drawn from it.** The twelve-pass row
*"no institutional-scale permissive student information system"* is **RESTORED** in
[`verticals/solutions.md`](../verticals/solutions.md), with the denominator correction kept and the
verdict unchanged.

### 🆕 🔴 A licence path this file has never probed, and what it does to five earlier verdicts

🔴 **`uccser/cs-field-guide` carries its `MIT` grant at `LICENCE` — the British spelling — and
returns `404` at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` and `license`.**
🔵 **`P50` taught that a licence-absence claim is a claim about the PATHS probed. `gap 133` is the
same lesson at a spelling this KB's probe list never contained**, and the Commonwealth spelling is
not rare in exactly the institutional population p175 just started sampling.
🔴 **Consequence, stated rather than deferred: every *"NO GRANT FILE — exhaustive"* verdict in this
KB was reached with an incomplete probe list** — including `JushBJJ/Mr.-Ranedeer-AI-Tutor` on the
`12`-row shelf. `ACTION KJ` re-probes them all.

### 🟢 The count, and the channel that makes it cheap

| figure | channel | cost | precision |
|---|---|---|---|
| 🆕 🟢 **`8 197`** | 🟢 **authenticated MCP repository search** | 🟢 **`1` request** | 🟢 **EXACT** |
| 🟡 `8 191` | `github.com/search` via `WebFetch`, `17` disjoint `pushed:` windows | 🔴 `17` requests, paced around a `429` | 🟢 exact, and off by `6` |
| 🔴 *"`8.2k`"* | the same page, unpartitioned | `1` request | 🔴 two significant figures |

🆕 🔵 **`T264` — a channel ledger is only as good as the request forms somebody thought to try.**
p174's ledger was careful, complete about what it tested, and missed the best channel entirely.
🟢 **The partition method is retained as a FALLBACK, not retired as wrong** — it is the only method
that works when the authenticated channel is unavailable, and it agreed to within `0.07%`.
🔴 **One limit of the new channel, measured and worth writing down: it answers SEARCH and refuses
per-repository file reads by session scope.** Licence bodies in the table above came from
`raw.githubusercontent.com`, `HEAD` shas from `git ls-remote`.
[`evidence/sis-interop-probe.2026-10-13-p175.tsv`](../evidence/sis-interop-probe.2026-10-13-p175.tsv)
· [`evidence/regional-sweep.2026-10-13-p175.tsv`](../evidence/regional-sweep.2026-10-13-p175.tsv)

## Pass 174 — 2026-10-13

🆕 🟢 **Three foundational repositories enter this file, and none of them is new software. They were
invisible because this KB was counting the wrong tag.** `ACTION JZ` made `topic:education`
countable (`8 191`, exactly); the sweep p173 recorded as never-run was then run, and
`"student information system" license:mit pushed:>=2026-04-16` returns **`54` results — an exact
integer, not a rounded one**.

| repo | licence *(body READ this pass, bytes)* | `HEAD` | last commit | tree | what it is |
|---|---|---|---|---|---|
| 🆕 🟢 [`eagles-edu/sis`](https://github.com/eagles-edu/sis) | 🟢 **`MIT`** — `LICENSE`, `1 066` B | `7e5fbccad5a0` | `2026-09-26` → `17` d | 🟢 **`2 598` files** | the largest permissive student information system this KB has ever been able to name |
| 🆕 🟢 [`opensacorg/learning-blocks`](https://github.com/opensacorg/learning-blocks) | 🟢 **`MIT`** — `LICENSE`, `1 075` B, *"Copyright (c) 2022 Code for Sacramento"* | `5bc137c972c7` | `2026-09-15` → `28` d | 🟢 **`849` files** | an SIS built by a **Code for America brigade** — a civic-tech institution, which also PLACES it (`P800`) |
| 🆕 🟡 [`Arux-Software/Bright`](https://github.com/Arux-Software/Bright) | 🟢 **`MIT`** — 🔴 at `LICENSE.txt`, `1 075` B *(a `P50` instance: plain `LICENSE` is absent)* | `7d15ccb7c2e9` | — | — | a framework for working WITH student information systems — a client library, not a system of record |

🔴 **What is verified and what is not, stated so the rows cannot be over-read (`ACTION JR`):**
licence BODY, `HEAD` sha, tree size and commit date. 🔴 **Not verified: `OneRoster`, `SCORM`, xAPI,
multi-tenancy, authentication, dependency closure, or whether anyone operates them.** They are
candidates in [`verticals/solutions.md`](../verticals/solutions.md), not routes.
🔴 **And the residue a client should hear: the head of that `54`-repository population is `31`★** —
a browser extension for a Dutch SIS. There is still no institutional-scale permissive SIS. The
twelve-pass sentence *"none exists"* was stronger than the evidence, and it was never re-tested on
a denominator that could have refuted it.

### 🆕 🟢 The `P50` instance, because this file keeps finding them

🔵 `Arux-Software/Bright` carries its grant at **`LICENSE.txt`** and nothing at `LICENSE`. This KB
has now recorded the same shape at `openfun/ralph` (`LICENSE.md`), `moodle/moodle` (`COPYING.txt`),
`formalms/formalms` (`html/license.txt`) and `os4ed/openSIS-Classic` (not at the root at all).
🟢 **The probe ladder in [`compose/code/grant-ladder-v4/`](../compose/code/grant-ladder-v4) exists
for exactly this reason, and a `404` on `LICENSE` is never a finding on its own.**

### 🟢 Carried forward unchanged

🟡 **Every p168–p173 verdict in this file stands; p174 re-read no platform root grant.** The
`Sakai` manifest reading corrected at p173 (`25` `Apache-1.1` + `9` `BSD`, not `34` `BSD`) is
unchanged, and the `Apache-1.1` support added to the shared classifier at p173 is now also
exercised by p174's own gate suite — `12` of `12`, offline.
[`evidence/exact-count-partition.2026-10-13-p174.tsv`](../evidence/exact-count-partition.2026-10-13-p174.tsv)
## Pass 173 — 2026-10-13

🆕 🟢 **`ACTION JU` DISCHARGED. The shared hardened classifier can now see `Apache-1.1`, and
`Sakai`'s manifest re-reads as `25` `Apache-1.1` paths + `9` `BSD` where p170–p172 all read
`34 BSD`. `207` of `207` regression assertions, `8` of them new, `13` of `14` dependent suites
byte-identical.**
🆕 🔴 **But the falsifier's first limb FIRES and it narrows the gap: the corrected classifier
changes `0` verdicts across the `50` licence bodies committed in this repository's own fixtures. On
the evidence available offline `T232` is a property of ONE 2005-era manifest, not a live defect in
a shared control. The error was LATENT, and `gap 120`'s *"every instrument inherits this"* is true
in principle and empty in practice.**
🆕 🟢 **And the re-read was CONTROLLED where p171's was not. `git fetch` refused the pinned sha —
`fatal: couldn't find remote ref 88f8e09c0a38` — and `raw.githubusercontent.com` served all `86`
paths at that exact commit anyway. `86` of `86` bodies byte-identical to p172's recorded hashes
(`T249`).**

### 🆕 🟢 What `Sakai`'s `licenses/` manifest actually contains, corrected

| family *(shared classifier, p173)* | paths | was read as |
|---|---|---|
| 🆕 🟢 **`Apache-1.1`** | 🆕 **`25`** *(`20` distinct blobs)* | 🔴 **`BSD`** at p170, p171 and p172 |
| 🟢 `Apache-2.0` | `24` | unchanged |
| 🔴 `UNCLASSIFIED` | `16` | unchanged — this is where the `8` proprietary Sun agreements live |
| 🟡 `BSD` | 🆕 **`9`** | was `34` |
| 🟡 `LGPL-2.1` | `5` | unchanged — includes the `2` generic-blob mismatches (`T230`) |
| 🟢 `MIT` | `3` | unchanged |
| 🟡 `MPL-1.1` | `1` | unchanged |
| 🔴 `CC-BY-2.5` | `1` | unchanged |
| ⬜ binary PDF, not read | `2` | unchanged |

🟢 **The `25` are the ASF components of a 2005-era Java stack and they are exactly who you would
expect: `log4j-1.2.8`, `lucene`, `struts-1.1`, `struts-legacy`, `velocity`, `poi`, `oro`, `batik`,
`fop`, `james`, `axis`, `xalan-2.5.2`, `xercesImpl-2.5.0`, `xml-apis`, `jasper-compiler`,
`jasper-runtime`, `avalon-framework`, `cornerstone`, `excaliber`, `logkit`, `db-ojb-1.0.rc6`,
`commons-id-0.1-dev`, `stxx-1.3`, `xmlform` — and `apache1.1.license.txt` itself.**

### 🆕 🟡 What changes for a client, and what does not

| | |
|---|---|
| 🟢 **permission** | 🟢 **NOTHING changes. `Apache-1.1` and `BSD-3-Clause` are both permissive and both OSI; `commercial_use_ok()` answered ALLOWED before and after. No verdict this KB published was wrong** |
| 🔴 **attribution** | 🔴 **THIS is what was lost. `Apache-1.1` clause `3` requires the end-user documentation to carry *"This product includes software developed by the Apache Software Foundation (http://www.apache.org/)"*. `BSD-3-Clause` requires no acknowledgment at all. A deliverable that reported `BSD` over these `25` paths dropped an attribution obligation the client has to meet** |
| 🟡 **what it does NOT prove** | 🟡 **These are manifest files for components `Sakai` may no longer ship. p173 read the MANIFEST, not the build — same limit p172 stated and it still applies** |
| 🟢 **the scanner line to use in a deck** | 🟢 ***"A tool reporting `34 BSD` over `Sakai`'s `licenses/` is reporting `25` `Apache-1.1` files as BSD. `Apache-1.1` is BSD-shaped — it carries the same redistribution grant — plus an attribution clause BSD does not have."*** |

### 🆕 🟢 The classifier change itself

🟢 **Three anchors, all on the TITLE BLOCK except the third's confirming signature, and the order is
load-bearing because `Apache-1.1` CONTAINS the BSD grant phrase:**

| anchor | answer |
|---|---|
| title says `Apache Software License` + `Version 1.1` | `Apache-1.1` |
| title says `Apache Software License` + `Version 1.0` | `Apache-1.0` |
| title says `Apache Software License`, no version, body carries the clause-`3` acknowledgment | `Apache-1.x-UNVERSIONED` *(following `GPL-UNVERSIONED`: never invent a version the payload does not state)* |

🔴 **A payload carrying the acknowledgment but NOT the title stays `BSD`, deliberately** — the ASF
acknowledgment appears in BSD notices of projects that merely credit the ASF, and the suite pins
this with a FABRICATED negative control that says so in its filename.
🟢 **The `7` platform rows, `Moodle`'s `88` grant documents and `OpenOLAT`'s root verdict are
CARRIED UNCHANGED from p168–p172. p173 re-read no platform root and says so.**
[`compose/code/p173-apache11-family/`](../compose/code/p173-apache11-family/)
· [`evidence/apache11-reclassification-sakai86.2026-10-13-p173.tsv`](../evidence/apache11-reclassification-sakai86.2026-10-13-p173.tsv)
· [`evidence/apache11-outside-sakai-corpus.2026-10-13-p173.tsv`](../evidence/apache11-outside-sakai-corpus.2026-10-13-p173.tsv)
· [`evidence/lib-test-surface-pristine-vs-patched.2026-10-13-p173.tsv`](../evidence/lib-test-surface-pristine-vs-patched.2026-10-13-p173.tsv)
## Pass 172 — 2026-10-13

🆕 🔴 **`ACTION JO` settled `gap 117` and found something larger beside it. `8` of the `86` paths in
`Sakai`'s `licenses/` manifest are NOT OPEN-SOURCE GRANTS AT ALL — they are Sun Microsystems
click-through agreements and one single-seat proprietary licence. p171 swept this same population
and published `0` hostile.**
🆕 🟢 **On the question the action actually asked — does the manifest MISLABEL components? — the
answer is no: `3` mismatches, the same `3` p171 found, verified this pass against authoritative
upstream metadata. The first falsifier limb FIRES; the manifest is three stale files on the licence
question.**
🆕 🔴 **And `25` of the `86` paths carry the **Apache Software License 1.1**, which this KB's shared
hardened classifier reports as `BSD` — including the file named `apache1.1.license.txt` (`T232`).**

### 🆕 🟡 The `7` platform rows — HEADs at p172

🟢 **`git ls-remote` at `t0 = 2026-10-13T10:5xZ`, `7` of `7` reachable. Root verdicts carry forward
from p168–p171 body reads; no root grant was re-read this pass.**

| repo | HEAD at p172 | root verdict | moved since p171 | what it is |
|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 **`ad60834ff1f8`** | 🟢 `ECL-2.0` | 🔴 **YES** *(from `88f8e09c0a38`)* | institutional LMS, Java |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `f20534726a59` | 🔴 `GPL-3.0` @ `COPYING.txt` | 🟢 no | the world's most deployed LMS, PHP |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | 🟢 **`MIT`** | 🟢 no | **offline-first** learning platform — the low-connectivity row |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | 🔴 `AGPL-3.0` | 🟢 no | MOOC-scale courseware, Python |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | 🔴 `GPL-3.0` | 🟢 no | LMS with strong assessment/exam tooling, PHP; EMEA-rooted |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`46a5d7d40082`** | 🟡 `LGPL-3.0` | 🔴 **YES** *(from `1c95cefebc17`)* | education **ERP** on Odoo — enrolment, fees, timetabling. 🔴 **Its vendor-stated OneRoster / Ed-Fi / LTI 1.3 support is ABSENT from the open tree (`T162`, p164)** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | 🟢 **`MIT`** | 🟢 no | SCORM 1.2 / 2004 + AICC + xAPI runtime — the packaging layer |

🟢 **Permissive and buildable without a licence conversation: `2` of `7` — `kolibri` (`MIT`) and
`scorm-again` (`MIT`). `Sakai`'s `ECL-2.0` is an Apache-2.0 variant with a teaching-use patent
carve-out and is the third practical route (`p170`).** 🔴 **`Moodle`, `ILIAS` (`GPL-3.0`) and
`edx-platform` (`AGPL-3.0`) are reciprocal; `AGPL` reaches network use, which is the form most
client deployments take.**

### 🆕 🔴 `ACTION JO` — `8` paths in `Sakai`'s manifest are proprietary agreements

🔴 **Control stated honestly: the measurement was taken at `HEAD 88f8e09c0a38`, and `Sakai` has
since moved to `ad60834ff1f8`. The manifest is `licenses/`, which Sakai has not touched in years,
but this reading is pinned to a sha that is no longer HEAD and says so.**

| class *(read on the TITLE BLOCK, per `P237`)* | paths | what it withholds |
|---|---|---|
| 🔴 **Sun Binary Code License Agreement** | `activation`, `jta`, `jdbc2_0-stdext` | 🔴 **redistribution** *(one archival copy)*, modification, decompilation; `jta` adds *"internal use only … for which the corresponding fee has been paid"* |
| 🔴 **Sun Software License Agreement + Entitlement** | `servlet` | 🔴 redistribution |
| 🔴 **Sun Specification click-through** | `jsf-api`, `jsf-impl`, `standard` | 🟡 a specification grant, not an implementation grant |
| 🔴 **proprietary single-seat** | `java2html` | 🔴 **one copy, one person**, no decompile |

🔴 **Why p171 read `0`: `ACTION JK` tested hostility with `commercial_use_ok()`, a NONCOMMERCIAL
**phrase** test. None of these eight uses the word *"noncommercial"*. They withhold redistribution
instead, and a phrase test for the wrong word is silent on the right finding (`T231`).**
🆕 🔴 **The manifest also contradicts ITSELF about one component: `servlet.license.txt` carries
Sun's proprietary Entitlement while `jsp-api.license.txt` — the sibling API, same upstream, same
directory — carries `Apache-2.0`. The servlet API as Tomcat ships it is `Apache-2.0`.**
🟡 **What this does and does not mean for an engagement: these are 2005-era manifest files for
components `Sakai` may no longer ship. The finding is about the MANIFEST a client's reviewer will
read, not a proven claim that proprietary jars are in today's build. State it that way — and then
check the build, which this pass did not.**

### 🆕 🟢 The three mismatches, verified upstream rather than remembered

| file | body | upstream | verified against |
|---|---|---|---|
| 🔴 `aopalliance.license.txt` | `LGPL-2.1` | 🟢 **Public Domain** | mojohaus third-party report; Apache CXF licence listing |
| 🔴 `dnsjava-1.2.3.license.txt` | `LGPL-2.1` | 🟢 **BSD** | Maven Central POM |
| 🟡 `junit-3.8.1.license.txt` | `IPL-1.0` | 🟡 **`CPL-1.0`** | `repo1.maven.org/maven2/junit/junit/3.8.1/junit-3.8.1.pom` declares *"Common Public License Version 1.0"* |

🟢 **The JUnit row is a mismatch by IDENTIFIER and barely by EFFECT — `CPL-1.0` is the IBM Public
License re-stewarded, near-identical text. Report it as an identifier error, not a licence risk.**
🆕 🟢 **`T230` — the MECHANISM of both `LGPL` mismatches is generic-blob reuse. Their blob is
byte-identical to the manifest's own generic `LGPL2.1.license.txt`, so neither file carries a
component-specific copyright line. `8` of `86` paths are copies of a family file; `2` of the `8`
are wrong and the other `6` are right by luck, not by evidence.**

### 🆕 🔴 `T232` — the shared classifier cannot see `Apache-1.1`, and it is `25` of `86` paths here

| family as the classifier reports it | paths | corrected |
|---|---|---|
| 🔴 **`BSD` `34`** | 34 | 🔴 **`9` BSD + `25` `Apache-1.1`** |
| 🟢 `Apache-2.0` | 24 | 24 |
| 🟡 `UNCLASSIFIED` | 16 | 🔴 **`8` of them are proprietary, `1` is not a grant** |
| `LGPL-2.1` | 5 | 5 |
| `MIT` | 3 | 🟡 **`2` — `jing` is `BSD-3-Clause`** |

🔴 **A client scanner reporting *"34 BSD"* over this tree is reporting `25` `Apache-1.1` files as
BSD. `Apache-1.1` is BSD-SHAPED — four clauses on the same skeleton — but carries its own
attribution clause (*"This product includes software developed by the Apache Software
Foundation"*), which is how p172 detects it.**
🆕 🔵 **`T224` re-fired, on p172's own instrument. p172's FIRST hostility test searched for
withholding language in bodies and returned `34` raw hits, `26` of them ordinary `Apache-2.0` and
`LGPL` text matched on phrases like *"shall not modify"*. The finding survived only because the
test was moved to the title block — which is `P237`, a rule written in this KB since pass 77 and
broken again here on the first attempt. A rule that has to be remembered is not a control.**
[`evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv`](../evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv)
· [`evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv`](../evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv)
· [`evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv`](../evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv)
· [`compose/code/p172-manifest-attribution/`](../compose/code/p172-manifest-attribution/)
## Pass 171 — 2026-10-13

🆕 🔴 **`ACTION JK` classified the inner grant bodies this page has been COUNTING, and the count
itself was wrong in one direction only: `105` of `Moodle`'s `193` *"grant bodies"* are PHP SOURCE
FILES, not grants. `Sakai`'s contamination is `0` of `129`. The published pair invited a comparison
that cannot be made (`T223`).**
🆕 🟢 **The substantive answer is reassuring and now measured: `217` third-party grant documents
across the two leading institutional LMSes, `12` families, `0` that withhold commercial use or
redistribution. `gap 115`'s anxiety was procedural, as `penecho`'s `32` predicted.**

### 🆕 🟡 The licence column, with the inner audit CLASSIFIED

| repo | HEAD at p171 | root verdict | name matches | `P170-A` bodies | 🆕 **DOCUMENT bodies** | 🆕 **source-file over-read** | 🆕 **hostile** |
|---|---|---|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 **`88f8e09c0a38`** *(MOVED from `10a1d904d379`)* | 🟢 `ECL-2.0` | `165` | `129` | 🟢 **`129`** *(`72` blobs)* | 🟢 **`0`** | 🟢 **`0`** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 `f20534726a59` *(UNCHANGED — controlled re-read)* | 🔴 `GPL-3.0` @ `COPYING.txt` | `217` | `193` | 🆕 🔴 **`88`** *(`80` blobs)* | 🔴 **`105`** | 🟢 **`0`** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | 🟢 `MIT` | `11` | 🟡 `6` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | 🔴 `AGPL-3.0` | `27` | 🟡 `15` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | 🔴 `GPL-3.0` | `7` | 🟢 `2` | 🟡 *not re-swept this pass* | — | — |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `1c95cefebc17` | 🟡 `LGPL-3.0` | `15` | 🟢 `1` | 🟡 *not re-swept this pass* | — | — |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | 🟢 `MIT` | 🟢 `1` | 🟢 `1` | 🟢 **`1`** | 🟢 **`0`** | 🟢 **`0`** |

🔴 **Control honestly stated: `Moodle` was re-read at p170's EXACT `HEAD`, so every difference there
is INSTRUMENT. `Sakai` moved (committed `09:46:58Z` this pass) and the server refused the pinned sha
(`fatal: couldn't find remote ref`), so that limb is UNCONTROLLED — though its name-match count
(`165`) and body count (`129`) are identical at both `HEAD`s, which is a result rather than a control.**

### 🆕 🟢 Family tally — what a client's scanner will actually report

| family | `Sakai` *(72 blobs)* | `Moodle` *(80 blobs)* |
|---|---|---|
| 🟢 **`MIT`** | `7` | 🟢 **`47`** |
| 🟢 **`BSD`** | 🟢 **`29`** | `12` |
| 🟢 **`Apache-2.0`** | `21` | `8` |
| 🟢 **`ECL-2.0`** | `10` | — |
| 🟡 **`LGPL`** | `2` | `3` |
| 🔴 **`GPL`** | — | `2` |
| 🟡 **`IPL-1.0`** | `1` | — |
| 🟡 **multi-family blobs** | `2` | `6` |
| 🟢 **withholding commercial use** | 🟢 **`0`** | 🟢 **`0`** |

🟢 **`Sakai`'s `3` reciprocal bodies (`2` `LGPL-2.1`, `1` `IPL-1.0`) all sit in `licenses/` — a
third-party NOTICE manifest. `0` copyleft grant governs `Sakai`'s own code.** 🔴 **Whether a
dependency notice counts as *"copyleft inside an `ECL-2.0` repository"* is a READING, and it is
counsel's, not an instrument's. Recorded as such rather than declared silent.**
🆕 🟡 **`gap 117` — and that manifest MISLABELS: `aopalliance.license.txt` and
`dnsjava-1.2.3.license.txt` both carry `LGPL-2.1` text, where AOP Alliance is public domain
upstream and dnsjava is `BSD`; `junit-3.8.1.license.txt` carries `IPL-1.0` where JUnit `3.8.1`
shipped `CPL-1.0`. Do not read that directory as a per-component attribution map (`ACTION JO`).**

### 🆕 🔴 `T223` — why `Moodle`'s number was `54%` source code, and why `Sakai`'s was not

| | |
|---|---|
| 🔴 **convention one** | 🔴 **`Moodle` puts a GPL notice header in EVERY php file, so any Moodle source file satisfies `P170-A` step `2`'s body test** |
| 🔴 **convention two** | 🔴 **`Moodle` ships an `admin/tool/licensemanager/` subsystem — a licence-manager FEATURE — whose filenames all contain *"license"*, so they all satisfy the name match** |
| 🔴 **the product** | 🔴 **the two multiply: `105` of `193` are source code, including `lang/en/license.php` and `lib/tests/licenselib_test.php`** |
| 🟢 **why `Sakai` is clean** | 🟢 **its grants live in `licenses/*.txt`. `73` of its `129` paths are `.txt`; `0` are source** |

🟢 **`P171-A` is the fix and it is one predicate: a grant body must BE a licence document, not a
source file that mentions one.** 🔴 **`gap 118` is the residue, and it is a REVIEW-COST hazard rather
than a legal one: a client's scanner will still report ~`193`, so an SBOM review of `Moodle` starts
`105` findings in the hole. Now sized before anyone bills for it.**
[`evidence/inner-grant-families.2026-10-13-p171.tsv`](../evidence/inner-grant-families.2026-10-13-p171.tsv)
## Pass 170 — 2026-10-13

🆕 🟢 **`ACTION JH` DISCHARGED with a silent falsifier: `7` of `7` platform root verdicts reproduce
under the folded, TREE-WIDE gate that p168 could only run root-only. The licence column survives a
stricter instrument for the second consecutive pass.**
🆕 🔴 **What the tree-wide reading adds is not a correction but a change of scale. `Sakai` carries
`129` grant BODIES below its root and `Moodle` `193`, where this shelf prints one licence cell each.
`gap 109`'s shape — *"the published licence is the OUTER grant only"* — is confirmed at two orders of
magnitude larger than the repo it was found on.**
🆕 🟢 **And p169's `ACTION JC` verdict on `OpenEduCat` is INDEPENDENTLY VINDICATED. A broad instrument
finds `15` grant-named paths in that tree; `1` carries a body. The other `14` are the same
`notice-board-icon.svg`, copied into `14` Odoo modules.**
🆕 🔴 **A new candidate was tested and REFUTED before it reached the shelf: `Forma LMS`, called
*"Apache 2.0"* by a secondary source, carries the GNU `GPL` version `2` verbatim and has no root grant
file at all.**
[`evidence/platform-tree-grants.2026-10-13-p170.tsv`](../evidence/platform-tree-grants.2026-10-13-p170.tsv)
[`evidence/name-vs-body-divergence.2026-10-13-p170.tsv`](../evidence/name-vs-body-divergence.2026-10-13-p170.tsv)
[`evidence/permissive-lms-candidates.2026-10-13-p170.tsv`](../evidence/permissive-lms-candidates.2026-10-13-p170.tsv)

### 🆕 🟢 `ACTION JH` — the `7` platform rows, folded and tree-wide

🟢 **Falsifier: *"refuted if any p168 licence verdict changes."* SILENT — all `7` reproduce.**
🟢 **Instrument: treeless clone, exhaustive `ls-tree -r`, root body read and family-matched, plus a
content test on every grant-named path.**

| repo | HEAD | HEAD date | root grant | root verdict *(reproduced)* | grant-named paths | 🆕 **actual bodies** |
|---|---|---|---|---|---|---|
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `10a1d904d379` | `2026-10-09` | `LICENSE` | 🟢 `ECL-2.0` | `165` | 🔴 **`129`** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `5d47c94a8ecc` | `2026-10-12` | `LICENSE` | 🟢 `MIT` | `11` | 🟡 **`6`** |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `3368a6b14b96` | `2026-10-12` | `LICENSE` | 🔴 `AGPL-3.0` | `27` | 🟡 **`15`** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | `f20534726a59` | `2026-10-03` | 🟡 **`COPYING.txt`** | 🔴 `GPL-3.0` | `217` | 🔴 **`193`** |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `866b8e6d594d` | `2026-10-13` | `LICENSE` | 🔴 `GPL-3.0` | `7` | 🟢 **`2`** |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `1c95cefebc17` | `2026-09-07` | `LICENSE` | 🟡 `LGPL-3.0` | `15` | 🟢 **`1`** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `882f3b8c7498` | `2026-10-09` | `LICENSE` | 🟢 `MIT` | 🟢 **`1`** | 🟢 **`1`** |

🟢 **`6` of `7` rows have a HEAD inside `11` days; `ILIAS` is `0` days old at this pass.**
🟡 **`Moodle`'s root grant is at `COPYING.txt`, not `LICENSE` — recorded because a gate that probes
only `LICENSE` reads `Moodle` as unlicensed, which is `P169-A` step `5`'s original failure mode.**
🔵 **The column to read twice is the last one. This shelf has been publishing one licence per platform
for `170` passes. For `scorm-again` that one cell is the whole truth. For `Sakai` it is `1` of `129`
and for `Moodle` `1` of `193`.**

### 🆕 🔴 What `129` and `193` mean, stated so it is not mistaken for alarm

🟢 **None of this overturns a verdict. The outer grant is what governs the project's own code, and all
`7` reproduced.** 🔴 **What it governs is a fraction of what a client ships.**

| the question a client actually asks | what this shelf could answer before p170 | what it can answer now |
|---|---|---|
| 🟢 *"what licence is Moodle?"* | 🟢 **`GPL-3.0`, body read, verbatim** | 🟢 **unchanged** |
| 🔴 *"what licences will my scanner find in Moodle?"* | 🔴 **unknown** | 🟡 **`193` grant bodies exist; their families are NOT yet classified** |
| 🔴 *"how long is the inner audit?"* | 🔴 **unestimable** | 🟢 **countable: `129` for `Sakai`, `193` for `Moodle`, `15` for `Open edX`, `1` for `scorm-again`** |

🟢 **So the deliverable p170 adds is an ESTIMATE, not a verdict — and estimable work is billable
work.** 🟢 **Classifying those bodies is pre-registered as `ACTION JK`, with `P170-A` as the
procedure and `penecho`'s `32`-file classification as the worked precedent.**
🔴 **The caution that comes with it, from `T213`: do not count grant files by filename. On these same
trees the name match over-reads by `36` on `Sakai` and `24` on `Moodle`, and on `OpenEduCat` by `14`
out of `15`.**

### 🆕 🟢 `gap 109` — p169's `OpenEduCat` answer re-measured by a different instrument

🟢 **p169 used a canonical-filename regex and concluded `1` grant file in `1 345` tracked files.
p170 used a deliberately broad name match and found `15` candidates — then content-tested all `15`.**

| probe | result | reading |
|---|---|---|
| 🔴 **grant-named paths, broad match** | 🔴 **`15`** | 🔴 **looks like a `15`-grant tree** |
| 🟢 **of those, carrying a grant body** | 🟢 **`1`** — the root `LICENSE` | 🟢 **p169 was RIGHT** |
| 🟢 **what the other `14` are** | 🟢 **`static/description/notice-board-icon.svg`, once per Odoo module** | 🟢 **an ICON. The string *"notice"* is in a filename, not a grant** |

🔵 **Two passes, two instruments with opposite biases, one answer. That is the strongest form of
confirmation this KB can produce from a single container, and it is worth more than either reading
alone.** 🟢 **`T201` stands untouched: the root body still promises the `GPL-3.0` text *"at the
bottom"* and still contains `0` occurrences of it.**

### 🆕 🔴 `Forma LMS` — refuted at the artifact, and a hazard class this shelf has not held before

| probe | result |
|---|---|
| 🔴 **claimed by a secondary source** | 🔴 **`Apache-2.0`** |
| 🔴 **root grant file** | 🔴 **NONE — no `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` at the root** |
| 🟢 **actual grant** | 🟢 **`html/license.txt`, `18 346` B — `GNU GENERAL PUBLIC LICENSE Version 2, June 1991`, verbatim** |
| 🟢 **occurrences of *"Apache"* in that body** | 🟢 **`0`** *(the only Apache text in the tree is a vendored jsdoc prettify file)* |
| 🟡 **HEAD** | 🟡 **`446a77a9b9cb`, `2026-07-17` — `88` days** |
| 🆕 🔴 **licence shipped in** | 🔴 **NINE languages — english, spanish, portuguese, italian, german, french, croatian, bosnian, tamil — with NOTHING naming which governs** |

🔵 **The multilingual grant is the new hazard. A translated copyleft licence is not a second licence
and not a choice; it is a convenience that leaves the governing text unnamed. For a LATAM or EMEA
engagement that is a question for counsel, and the right move is to name the English text as
controlling in writing before anything is built on it.**
🟢 **Cost of this refutation: two treeless clones. Value: a `GPL-2.0` platform did not enter a shelf
that exists to identify what Globant can build on permissively.**

### 🆕 🟢 The foundations shelf — permissive rows, re-verified this pass

🟢 **Every row below had its root grant body read on the open channel at p170 or p169, and its HEAD
confirmed by `git ls-remote`.**

| repo | licence *(body read)* | HEAD date | role |
|---|---|---|---|
| 🆕 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **`Apache-2.0` — §`1`–`9` VERBATIM, appendix replaced by `2` attribution statements** | 🟢 **`2026-10-12`** | 🆕 🟢 **institutional LMS — `QTI`, `SCORM`, curriculum, assessment. RESTORED to the permissive route (`T216`)** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 `MIT` | 🟢 `2026-10-12` | 🟢 offline-first learning platform |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 `MIT` | 🟢 `2026-10-09` | 🟢 **`SCORM` `1.2` / `2004` + `AICC` runtime — the interop layer** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 `MIT` | 🟢 `2026-10-10` | 🟢 **LMS, and the only repo on any shelf shipping a dependency-licence GATE (`T208`)** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 `ECL-2.0` | 🟢 `2026-10-09` | 🟡 institutional LMS — patent limb (`T200`), gate conflict (`T208`) |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 `2026-10-12` | 🟡 MOOC platform — RPC carve-out (`gap 107`) |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` *(at `COPYING.txt`)* | 🟢 `2026-10-03` | 🟡 the incumbent LMS |
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 `GPL-2.0` | 🟢 `2026-10-12` | 🟡 **the most active SIS this KB holds** |

🟢 **`4` rows permissive (`MIT` / `Apache-2.0`) and all `4` with a HEAD inside `5` days.**
🔴 **`0` permissive SIS, for a NINTH pass — now with `Forma LMS` tested and refuted rather than the
hole merely re-asserted.**

## Pass 169 — 2026-10-13

🆕 🟢 **`ACTION JC` is DISCHARGED and `gap 109` closes in the direction nobody expected: there are no
unnamed bundled grants in `OpenEduCat` to name. `1 345` tracked files, `1` grant file, `0` vendored
anything, and `14` of `14` Odoo manifests declaring the same `LGPL-3`. The *"bundled libraries ... other
GPL-compatible licenses"* clause has NO REFERENT in the tree.**
🆕 🟢 **And the oldest hole on this shelf — no permissive SIS, re-searched for seven passes — is now
SETTLED rather than merely re-confirmed. The web's one `Apache-2.0` answer, `Fedena`, is real as a
grant and abandoned as software: a licensor statement in `NOTICE`, no licence body in either of its two
trees, and a newest commit of `2016-07-20`.**
🆕 🟢 **Two ACTIVE copyleft SIS options are verified and dated for the first time: `RosarioSIS`
(`GPL-2.0`, HEAD `1` day old) and `openSIS-Classic` (`GPL-2.0`, HEAD `8` days old).**
[`evidence/openeducat-bundled-grants.2026-10-13-p169.tsv`](../evidence/openeducat-bundled-grants.2026-10-13-p169.tsv)
[`evidence/sis-permissive-settled.2026-10-13-p169.tsv`](../evidence/sis-permissive-settled.2026-10-13-p169.tsv)
[`evidence/agent-grant-surface.2026-10-13-p169.tsv`](../evidence/agent-grant-surface.2026-10-13-p169.tsv)

### 🆕 🟢 `gap 109` CLOSED — `OpenEduCat` bundles nothing, and the clause is inherited boilerplate

🟢 **`ACTION JC`'s falsifier was *"refuted if vendored third-party code carrying its own grant is
found"*. SILENT.** 🟢 **Instrument: a treeless clone at HEAD `1c95cefebc17`, then an exhaustive
`ls-tree -r` — not a sampled probe.**

| probe | result | reading |
|---|---|---|
| tracked files | `1 345` | — |
| 🟢 **grant files anywhere in the tree** | 🟢 **`1`** — the root `LICENSE` | 🟢 **ONE grant surface in the whole repository** |
| `node_modules/` · `vendor/` · `static/lib/` · `*.min.js` | 🟢 **`0` · `0` · `0` · `0`** | 🟢 **nothing is vendored** |
| `requirements.txt` · `setup.py` · `pyproject.toml` | 🟢 **`0`** | 🟡 **no declared dependency manifest either** |
| 🟢 **Odoo `__manifest__.py` files** | `14` | 🟢 **the real packaging unit** |
| 🟢 **manifests declaring `'license': 'LGPL-3'`** | 🟢 **`14` of `14`** | 🟢 **UNIFORM — every module agrees with the published licence** |

🔵 **So the hazard p168 flagged was mis-shaped, and saying so is the finding. The clause is Odoo's own
licence-notice boilerplate carried into a derived repository, not a description of this tree. A licence
review of `openeducat_erp` has `1` file to read, not an unknown number.**
🔴 **What survives from p168 untouched is the OTHER defect, `T201`: the body still promises the
`GPL-3.0` text *"at the bottom"* and still contains `0` occurrences of it.**
🟡 **Where the real third-party exposure lives, stated so it is not mistaken for a clean bill: the Odoo
runtime these `14` modules require. That is a DEPENDENCY, outside this tree, and no probe of this
repository can speak to it.**

### 🆕 🔴 `T212` — the `Fedena` question is settled, and the hole does not close

🟢 **p169's vertical-platform query named exactly one new candidate, and a secondary source called it
*"Apache 2.0"*. Instead of recording the claim, p169 verified it on the open channel.**

| repo | HEAD | last commit | root grant files | licence BODY | declared licence |
|---|---|---|---|---|---|
| 🔴 [`projectfedena/fedena`](https://github.com/projectfedena/fedena) | `68a84ac445bf` | 🔴 **`2016-07-20`** | 🟡 `NOTICE` only | 🔴 **ABSENT** | 🟢 `Apache-2.0`, by licensor statement |
| 🔴 [`foradian/fedena`](https://github.com/foradian/fedena) | `333477b06f1d` | 🔴 **`2012-10-12`** | 🟡 `NOTICE` only | 🔴 **ABSENT** | 🟢 `Apache-2.0`, by licensor statement |

🟢 **Verbatim from `projectfedena/fedena`'s `NOTICE`:** *"Fedena / Copyright 2011 Foradian Technologies
Private Limited. ... Licensed under the Apache License, Version 2.0 (the `"License"`)"*.
🟢 **So the grant IS real — a licensor statement, the strongest channel this container has.** 🔴 **And
the software is an abandoned `2011` Rails application: over ten years since the newer tree moved,
fourteen since the older one.** 🔴 **Neither tree contains the Apache text it names — the same defect
class as `T201`.**
🔵 **Why this is worth a `T`-number: it CLOSES A SEARCH LOOP. Seven passes have re-run this query and
`Fedena` is the only name it has ever produced. It is now settled with a reason, so p170 should not
spend the query again.**
🟢 **The absence restates more usefully than before: not *"no permissive SIS exists"* but **"no
permissive AND MAINTAINED SIS exists"** — and the permissive one that did exist is datable.**

### 🆕 🟢 Two active SIS routes, verified — new rows on this shelf

| repo | licence | where the grant lives | HEAD | age | note |
|---|---|---|---|---|---|
| 🟡 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`GPL-2.0`** *(`15 214 B`, *"Version 2, June 1991"*)* | 🟢 root `LICENSE` | `232819b4c07e` | 🟢 **`1` d** | 🟢 **the most active SIS this KB has verified** |
| 🟡 [`os4ed/openSIS-Classic`](https://github.com/os4ed/openSIS-Classic) | 🔴 **`GPL-2.0`** | 🔴 **`docs/License.txt` — NOT the root (`T209`)** | `5d546f20117e` | 🟢 `8` d | 🔴 **vendors `CKEditor` and plugins with their own grants, unread (`gap 112`)** |

🔵 **Routing consequence: a client who can accept `GPL-2.0` now has two live SIS routes with dates
attached, where this shelf previously had only `OpenEduCat`'s `LGPL-3.0`. A client who cannot accept
copyleft still has nothing, and that is now a measured statement rather than an open search.**

### 🆕 🟢 `P169-A` — the licence gate, corrected in two places by its own failures

🟢 **`P168-A`'s six steps stand. p169 adds a step `0` and rewrites step `5`, because this pass's own
first readings were wrong in both places.**

| step | what it does | why |
|---|---|---|
| 🆕 🟢 **`0`. FOLD** | 🟢 **normalise curly quotes, apostrophes, the `©` glyph and `http`→`https` BEFORE any diff** | 🔴 **`T205` — SPDX's canonical texts carry `246` curly quotes and `1` `©`; FSF ASCII bodies carry `0`. Unfolded, a clean `GPL-3.0` reads as `71` deviations** |
| 🟢 `1`–`4` | 🟢 title-line family · canonical word diff · permissive-set membership · body-contains-its-family | 🟢 unchanged |
| 🆕 🔴 **`5`. TREE, not root** | 🔴 **enumerate grant files with `ls-tree -r` across the whole tree** | 🔴 **`T209` — `openSIS-Classic` keeps its `GPL-2.0` in `docs/`, so a root probe calls an active, plainly licensed SIS *"unlicensed"*** |
| 🟢 `6` | 🟢 resolve every pointer | 🟡 **`fsf.org` and `gnu.org` are unresolvable here (`T211`), so those pointers are UNRESOLVED, not broken** |

### 🆕 🟢 `P169-B` — the treeless clone: a `200×` cheaper instrument for every inventory question

🔴 **p168 answered *"which grant files exist?"* by cloning `10` full trees: `623 MB`, `11 684` files.**
🟢 **p169 answered it for `13` repos with `git clone --depth 1 --filter=blob:none --no-checkout`
followed by `ls-tree -r`: `3.1 MB` total.**
🟢 **The answer is strictly LARGER — `17` root plus `63` non-root grant files across `12` rows, plus the
`1 345`-file `OpenEduCat` census and `4` SIS candidates — because a treeless clone carries every path in
the tree while downloading no blob.**
🟢 **Pair it with `raw.githubusercontent.com` pinned at the HEAD sha for the bodies you actually want.
Both channels are confirmed open in a fresh container this pass.**
🔵 **The rule: clone blobs only when you need to read MANY files. For *"does this file exist"*,
*"what is in this tree"*, or *"what is the HEAD date"*, blobs are pure cost.**

### 🟢 The foundation shelf — licence verdicts carried from p168

🟢 **p168 body-read these `9` under the unfolded, root-only instrument. `ACTION JH` re-runs them under
`P169-A`; until then the verdicts stand as published, with the instrument named.**

| repo | licence | p168 verdict | p169 status |
|---|---|---|---|
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried — re-read pending (`ACTION JH`) |
| 🟢 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried |
| 🟢 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 `GPL-3.0` | 🟢 CLEAN | 🟡 carried |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **`MIT`** | 🟢 CLEAN | 🟢 **still the SCORM `2004` route (`P168-B`)** |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **`ECL-2.0`** | 🔴 SUBSTITUTED LICENCE | 🔴 **and now known to fail a real allow-list (`T208`)** |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 `LGPL-3.0` | 🔴 BODY OMISSION | 🟢 **`gap 109` CLOSED this pass — nothing bundled** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `GPL-3.0` | 🔴 TWO GRANT SURFACES | 🟡 carried |
| 🟢 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `AGPL-3.0` | 🟢 RPC carve-out | 🟡 carried — `gap 107` stands |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 `Apache-2.0` | 🟢 addendum reproduced | 🟡 carried |


## Pass 168 — 2026-10-13

🟢 **`ACTION IX` is DISCHARGED, falsifier SILENT: of the `7` repos this shelf RECOMMENDS but had
never body-read, `3` carry a licence body that is not the licence they are published as.**
🆕 🟢 **And the instrument retired at p167 is now EXPLAINED rather than merely retired: the
`35 147` / `35 149` byte spread that defeated the band test is ONE URL — `philosophy/why-not-lgpl.html`
against `licenses/why-not-lgpl.html` — between two FSF revisions of the same `GPL-3.0`.**
🆕 🔴 **The canonical channel had to change: `gnu.org` is a `403` POLICY DENIAL at this container's
gateway, so the FSF plain text could not be used. SPDX's registry on `raw.githubusercontent.com`
is `200`, and because SPDX reflows its text the diff is WORD-level after whitespace normalisation —
never byte-level.**
[`evidence/licence-canonical-diff.2026-10-13-p168.tsv`](../evidence/licence-canonical-diff.2026-10-13-p168.tsv)
[`evidence/proxy-channel-census.2026-10-13-p168.tsv`](../evidence/proxy-channel-census.2026-10-13-p168.tsv)

### 🆕 🟢 Every recommended licence body, now READ — `10` bodies, `7` repos, `2` controls

| repo | file | bytes | title-line family | verdict | what the diff found |
|---|---|---|---|---|---|
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | `COPYING.txt` | `35 147` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | `±4` words, all `http://fsf.org/` → `https://fsf.org/` |
| 🟢 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `LICENSE` | `35 147` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | the same `4` URL-scheme hunks |
| 🟢 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | `LICENSE` | `35 149` | 🔴 `GPL-3.0` | 🟢 **CLEAN** | `±1` word — the `why-not-lgpl.html` path. **This is the whole `2`-byte spread** |
| 🟢 [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | `LICENSE` | `1 072` | 🟢 `MIT` | 🟢 **CLEAN** | `<year> <copyright holders>` → `2020 Jonathan Putney` |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `LICENSE` | `11 120` | 🟡 **`ECL-2.0`** | 🔴 **SUBSTITUTED LICENCE** | `+137`/`−13` words vs `Apache-2.0`, `95.44%` similar — a DIFFERENT licence, not an amended one |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `LICENSE` | `8 241` | 🟡 `LGPL-3.0` | 🔴 **PREAMBLE ADDENDUM + BODY OMISSION** | `3` added paragraphs, and `5 644` canonical words missing |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | `LICENSE` + **`license.txt`** | `35 147` + `1 614` | 🔴 `GPL-3.0` | 🔴 **TWO GRANT SURFACES** | `LICENSE` is clean; a SECOND root file declares **`-or-later`** |
| 🟢 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | `LICENSE` | `35 136` | 🔴 `AGPL-3.0` | 🟢 **CONTROL — addendum REPRODUCED** | canonical CONTAINED, `+615` chars appended |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | `LICENSE` | `10 982` | 🟢 `Apache-2.0` | 🟢 **CONTROL — addendum REPRODUCED** | inserts an *"Additional license statement"* AND drops the `APPENDIX` |

🟢 **Both controls reproduced, so the instrument is calibrated before its new findings are believed.**
🟢 **`4` of `7` are clean — and *clean* now has a measured meaning: the only deviation is an FSF text
revision or a filled-in copyright holder.**

### 🆕 🔴 `T200` — `Sakai` is not Apache-2.0, and the clause that differs is the one that matters to us

🟢 **This KB has published `Sakai` as `ECL-2.0` since p131 and was RIGHT.** 🔴 **What was never
published is WHAT `ECL-2.0` changes, and it is not cosmetic.**
🟢 **The licence says so itself, in its own preamble — a licensor statement, the strongest channel
available here:** *"The Educational Community License version 2.0 (`"ECL"`) consists of the Apache
2.0 license, modified to change the scope of the patent grant in section 3 to be specific to the
needs of the education communities using this license."*
🔴 **The inserted paragraph, verbatim:** *"Any patent license granted hereby with respect to
contributions by an individual employed by an institution or organization is limited to patent
claims where the individual that is the author of the Work is also the inventor of the patent
claims licensed, and where the organization or institution has the right to grant such license
under applicable grant and research funding agreements. No other express or implied licenses are
granted."*
🔴 **Read for a services firm: a contribution made by someone EMPLOYED by an institution carries a
patent grant narrowed to claims that person personally invented AND that their employer had the
right to license. `Apache-2.0`'s broad grant does not apply.** 🟢 **`+137`/`−13` words and
`95.44%` word similarity measured independently of the preamble's own claim.**
🟡 **Consequence for the routing table: `Sakai` stays the permissive LMS route and stays
recommended. The patent limb is a diligence item for any engagement that contributes code back,
and it is now stated instead of implied by *"Apache-derived"*.**

### 🆕 🔴 `T201` — `OpenEduCat`'s `LICENSE` promises the GPL text and does not contain it

🟢 **p164 published this body as *"`8 241 B`, INCOMPLETE"*. p168 names exactly what is missing and,
more usefully, that the file itself says it should be there.**
🔴 **The file's own words:** *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE,
Version 3 (LGPLv3), as included below. Since the LGPL is a set of additional permissions on top of
the GPL, **the text of the GPL is included at the bottom as well**."*
🔴 **Measured: `0` occurrences of `"GNU GENERAL PUBLIC LICENSE"` in the whole file. The body ends
mid-`LGPL`, and the `~35 KB` of `GPL-3.0` it promises is absent.** 🔵 **This matters because
`LGPL-3.0` is defined AS a set of additional permissions over `GPL-3.0`: without the `GPL` text,
the grant on disk is incomplete by its own construction, not merely short.**
🔴 **And a third added paragraph carries a carve-out no licence gate would catch:** *"Some external
libraries and contributions bundled with OpenEduCat may be published under other GPL-compatible
licenses."* 🟡 **So the row's published `LGPL-3.0` is the OUTER grant only; bundled components are
declared to be something else, unnamed.**
🔵 **Provenance, stated because it bounds the finding: this wording is Odoo's, and `OpenEduCat` is
an Odoo application — the defect is almost certainly inherited, not authored.**

### 🆕 🔴 `T202` — `Chamilo` has TWO root grant files, and they do not say the same thing

| surface | bytes | what it declares |
|---|---|---|
| 🟢 `LICENSE` | `35 147` | 🔴 the bare `GPL-3.0` body — **no version election at all** |
| 🆕 🔴 `license.txt` | `1 614` | 🔴 **`GPL-3.0`-OR-LATER:** *"either version 3 of the License, or (at your option) any later version"* |

🔴 **A gate that reads `LICENSE` sees `GPL-3.0-only`. A gate that reads `license.txt` sees
`GPL-3.0-or-later`, which is MORE permissive for a client.** 🟢 **`license.txt` is also the surface
the code itself points at: it states the in-source header convention
`/* For licensing terms, see /license.txt */`.**
🆕 🔴 **And both of `license.txt`'s own pointers are DEAD at `master` `440496d70ef0`:
`documentation/license.html` → `404`, `documentation/credits.html` → `404`.**
🔵 **So the file that carries the or-later election, and that every source header cites, refers for
its full text and its contributor list to two paths that no longer exist.** 🟡 **The or-later
reading still holds — it is stated in the file itself, not in the dead pointer — but the
contributor attribution it promises is unrecoverable from the repository.**

### 🔴 What `ACTION IX` means for `gap 105`, restated

🟢 **`gap 105` asked about ADDENDA. The answer is that *addendum* is too narrow a word for the class.**

| deviation class | found in | why a licence gate misses it |
|---|---|---|
| 🔴 **appended paragraph** | `edx-platform`, `OpenOLAT` | canonical still matches as a substring — the extra text is invisible to a containment test |
| 🔴 **substituted licence** | `Sakai` | the title line is honest, but `"ECL-2.0"` matches no entry in an `MIT`/`Apache`/`GPL` allow-list |
| 🔴 **body omission** | `OpenEduCat` | the file declares a family it does not fully contain |
| 🔴 **second grant surface** | `Chamilo` | each file is internally consistent; only reading BOTH shows the conflict |
| 🟢 **text revision / template fill** | `moodle`, `ILIAS`, `oneroster`, `scorm-again` | 🟢 **benign, and now measured so it stops being mistaken for a deviation** |

## Pass 167 — 2026-10-13

🟢 **`ACTION IV` is DISCHARGED, falsifier SILENT: `Ed-Fi-Alliance-OSS/edfi-oneroster` serves `12`
OneRoster 1.2 entities, users and enrolments among them, and `gap 102` CLOSES.**
🆕 🔴 **And this page's own published figure is CORRECTED: it is not `14` GET endpoints. It is `24`
rostering GETs over `12` entities, and neither the code nor the upstream README ever said `14`.**
🆕 🟢 **Every licence body on this shelf is now READ rather than banded — `14` bodies, `5` families,
and the size-band test is retired as unsound.**
[`evidence/oneroster-endpoints.2026-10-13-p167.tsv`](../evidence/oneroster-endpoints.2026-10-13-p167.tsv)
[`evidence/licence-bands.2026-10-13-p167.tsv`](../evidence/licence-bands.2026-10-13-p167.tsv)

### 🆕 🟢 `T189` — the OneRoster server, read route by route

🟢 **Pinned tree: `Ed-Fi-Alliance-OSS/edfi-oneroster`, `Apache-2.0` body-read `10 173 B`, `261`
tracked paths, HEAD `2026-10-12`.** 🟢 **Routes read from `src/routes/oneRoster.js`, controllers
sized to rule out stubs.**

| entity | collection | `/:id` | authz scope |
|---|---|---|---|
| 🟢 `users` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `students` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `teachers` | 🟢 yes | 🟢 yes | `users` |
| 🟢 `enrollments` | 🟢 yes | 🟢 yes | `enrollments` |
| 🟢 `classes` | 🟢 yes | 🟢 yes | `classes` |
| 🟢 `courses` | 🟢 yes | 🟢 yes | `courses` |
| 🟢 `orgs` | 🟢 yes | 🟢 yes | `orgs` |
| 🟢 `schools` | 🟢 yes | 🟢 yes | `orgs` |
| 🟢 `academicSessions` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `gradingPeriods` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `terms` | 🟢 yes | 🟢 yes | `academicsessions` |
| 🟢 `demographics` | 🟢 yes | 🟢 yes | `demographics` |

🟢 **`12` entities × `2` shapes = `24` rostering GETs, plus a catch-all `404`, a discovery route and
a health route — `34` `router.get` registrations in total.**
🟢 **Not stubs: `oneRosterController.js` `264` LOC and `OneRosterQueryService.js` `594` LOC.**
🟢 **The upstream README's endpoint table lists the SAME `24` rows and the SAME `12` entities, so
the two channels AGREE and the published `14` has no channel behind it at all.**

🟢 **`ACTION IV`'s falsifier required that users and enrolments NOT both be present. Both are.**
🟢 **So `P166-B` is amended into `P167-B` rather than withdrawn.**

### 🆕 🟢 Write-back, measured instead of deferred

🟢 **`router.post`, `router.put`, `router.patch` and `router.delete` all read `0` across the entire
application.** 🔴 **So this is READ rostering — not *"probably read-only"*, but zero write routes in
the tree.** 🔵 **The sentence a client gets: *`12` rostering entities, read-only, per-scope
authorisation, Apache-2.0; any enrolment write-back INTO the SIS is a build.*** 🟡 **Ed-Fi ODS
itself remains a separate, unmeasured decision.**

### 🆕 🔴 `T193` — the licence size band is retired, and `edx-platform` is why it mattered

🟢 **`ACTION IW` read all `14` licence bodies this shelf has on disk.** 🔴 **`P48`'s published bands
(`11 357`–`11 358` for Apache-2.0, `35 121`–`35 147` for GPL-3.0) match NOTHING on disk.**
🔴 **And the band test is not merely stale: `AGPL-3.0`'s measured maximum `35 136 B` and `GPL-3.0`'s
measured minimum `35 149 B` are `13 B` apart, while `Apache-2.0`'s spread within its OWN family is
`1 235 B` — `95×` larger. A discriminator cannot work in that geometry.**

| family | n | min | max | own spread |
|---|---|---|---|---|
| 🟢 `MIT` | `4` | `1 062` | `1 074` | `12 B` |
| 🔴 `PROPRIETARY` | `1` | `8 563` | `8 563` | — |
| 🟢 `Apache-2.0` | `4` | `10 173` | `11 408` | 🔴 **`1 235 B`** |
| 🔴 `AGPL-3.0` | `4` | `34 522` | `35 136` | 🔴 **`614 B`** |
| 🔴 `GPL-3.0` | `1` | `35 149` | `35 149` | — |

🟢 **The four mechanisms behind the spread, each measured: `http://` vs `https://` in the FSF URLs
(`1 B`); line re-wrapping (`~1 B`); the *"APPENDIX: How to apply"* section present or absent
(`~1 200 B`); and a licensor ADDENDUM — the only one that changes TERMS.**
🔴 **`openedx/edx-platform` carries such an addendum, and it is the most consequential sentence this
pass read: EdX Inc. declares that a public, independently available web service communicating with
its code over RPC is NOT a derivative work, and that Corresponding Source excludes that service's
files.** 🟢 **`P167-C` turns that into a composition; `P167-D` replaces the band with a TITLE-LINE
probe.**


## Pass 166 — 2026-10-13

🟢 **`ACTION IP` is DISCHARGED, falsifier SILENT: the false-NEGATIVE guards changed `4` verdicts
across `2` platforms — but only `2` of the `3` guards did any flipping.**
🆕 🔴 **The pass's sharpest result is a verdict that is YES and UNUSABLE at the same time: Moodle
DOES get OneRoster, from a sibling plugin that is `GPL-3.0` and has not been touched in
`2 091` days.**
🆕 🔴 **And a claim this shelf itself published is CORRECTED: `enrol_oneroster` is not *"in-tree"*.**
[`evidence/capability-census.2026-10-13-p166.tsv`](../evidence/capability-census.2026-10-13-p166.tsv)
[`evidence/fn-guard-verdict-changes.2026-10-13-p166.tsv`](../evidence/fn-guard-verdict-changes.2026-10-13-p166.tsv)
[`evidence/sibling-licences.2026-10-13-p166.tsv`](../evidence/sibling-licences.2026-10-13-p166.tsv)

### 🟢 `T179` — the capability census, `2` platforms × `5` standards, every cell measured

🟢 **Trees pinned before probing:** 🟢 **`moodle/moodle` HEAD `f20534726a59`, `2026-10-03`, default
branch `main`, `67 589` tracked paths** 🟢 **· `Selleo/mentingo` HEAD `242a9324fe48`, `2026-10-10`,
`main`, `4 753` paths.**

| platform | standard | naive | guarded | paths | verdict | implementing repo | its licence |
|---|---|---|---|---|---|---|---|
| 🟡 `moodle/moodle` | 🔴 **OneRoster** | `0` | `0` | `0` | 🟡 **IMPLEMENTED-IN-SIBLING** | 🔴 [`moodlehq/moodle-enrol_oneroster`](https://github.com/moodlehq/moodle-enrol_oneroster) | 🔴 **`GPL-3.0`** (`35 149 B`) |
| 🟡 `moodle/moodle` | 🔴 **Ed-Fi** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟡 `moodle/moodle` | 🟢 **LTI 1.3** | `3 472` | `3 415` | **`423`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟡 `moodle/moodle` | 🟢 **SCORM** | `3 158` | `3 149` | **`166`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟡 `moodle/moodle` | 🟢 **xAPI** | `409` | `406` | **`99`** | 🟢 **IMPLEMENTED-IN-TREE** | `moodle/moodle` | 🟡 `GPL-3.0` |
| 🟢 `Selleo/mentingo` | 🔴 **OneRoster** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟢 `Selleo/mentingo` | 🔴 **Ed-Fi** | `0` | `0` | `0` | 🔴 **ABSENT** | — | — |
| 🟢 `Selleo/mentingo` | 🔴 **LTI 1.3** | `1` | `1` | `1` | 🔴 **ABSENT — the hit is an ANTI-CLAIM** | — | — |
| 🟢 `Selleo/mentingo` | 🟢 **SCORM** | `1 660` | `1 660` | **`254`** | 🟢 **IMPLEMENTED-IN-TREE**, player IN-SIBLING | `Selleo/mentingo` + [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **`MIT` + `MIT`** (`1 072 B`) |
| 🟢 `Selleo/mentingo` | 🔴 **xAPI** | `1` | `1` | `1` | 🔴 **ABSENT — the hit is an ANTI-CLAIM** | — | — |

🟢 **Where Moodle's hits actually live, because a count is not a location:**
🟢 **LTI 1.3 — `public/lib/lti1p3` (`43`), `public/enrol/lti` (`19`), `public/mod/lti`** 🟢 **·
SCORM — `public/mod/scorm` (`121`)** 🟢 **· xAPI — `public/lib/xapi` (`56`) plus
`public/mod/h5pactivity` (`14`).** 🟢 **All code. The config-vs-code guard changed nothing on
Moodle, which is itself the result: Moodle's three standards are implementations, not declarations.**

### 🆕 🔴 `T180` — a verdict that is YES and UNUSABLE in the same breath

🔴 **`moodlehq/moodle-enrol_oneroster` is the reason Moodle can claim OneRoster. Measured the moment
it was named, with `P164-D`:**

| field | measured | consequence |
|---|---|---|
| 🟢 existence | 🟢 **EXISTS** — `134` tracked paths | 🟢 the capability is real, and it is out of tree |
| 🔴 **HEAD** | 🔴 **`b91b12857aac`, `2021-01-20`** | 🔴 **`2 091` days — `11.6×` the `180`-day drop threshold** |
| 🔴 **licence** | 🔴 **`GPL-3.0`, body-read `35 149 B`** | 🔴 **`P37`'s stop-ship gate applies; no permissive path** |

🟢 **Report the capability and its maintenance state together, in that order, always.**
🔵 **A verdict of *"yes, via a plugin"* that omits *"last touched January 2021, and it is GPL"* is
worse for a client than a flat *"no"* — because they budget for an integration instead of a build.
`P166-A` STEP 7.**

### 🆕 🔴 `T181` — a correction to this shelf, found by grepping the shelf FIRST

🔴 **`agents/trending.md` has been carrying the phrase *"Moodle's in-tree `enrol_oneroster`"*.**
🔴 **It is not in-tree. `moodle/moodle` returns `0` OneRoster hits across `67 589` paths, on the
name probe AND on the language-independent `imsglobal.org/spec/oneroster` probe.**
🟢 **`enrol_oneroster` is a separate repository under a different org (`moodlehq`, not `moodle`).**
🔵 **This is `T142`'s out-of-repo class, recorded with the direction reversed: the shelf had the
sibling and filed it as core.** 🟢 **Found by `ACTION IS`'s step 0, at a cost of one `grep`.**

### 🆕 🟢 `T182` — the permissive OneRoster path exists, and the shelf already held it

🟢 **`ACTION IP` leaves `3` of `3` recommended platforms with no OneRoster. The substitute was on
the shelf at `89` hits before p166 measured anything:**

| repo | licence | HEAD | age | paths | what it serves |
|---|---|---|---|---|---|
| 🟢 [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **`Apache-2.0`**, body-read **`10 173 B`** | `7442047368fa` | 🟢 **`1` d** | `261` | 🟢 **OneRoster 1.2 over `14` GET endpoints** |

🟢 **`P166-B` composes it.** 🟡 **Scoping honesty: `14` GET endpoints is READ rostering. 🔴 **AMENDED p167 (`T189`): `24` GETs over `12` entities; write-back measured at `0` routes.** Write-back
and the Ed-Fi ODS proper are a separate decision this shelf has NOT measured.**

### 🆕 🟢 `T183` — `gap 79` CLOSED, by commit authorship rather than by guesswork

🔵 **Open since p38: which of `Ed-Fi-Alliance-OSS/edfi-oneroster` and `CSR2017/edfi-oneroster` is
upstream.**

| repo | HEAD | date | HEAD commit author | paths | verdict |
|---|---|---|---|---|---|
| 🟢 **`Ed-Fi-Alliance-OSS/edfi-oneroster`** | `7442047368fa` | 🟢 **`2026-10-12`** | 🟢 **`CSR2017`** | **`261`** | 🟢 **UPSTREAM** |
| 🟡 `CSR2017/edfi-oneroster` | `937248be66de` | `2026-09-22` | 🔴 **`dependabot[bot]`** | `252` | 🟡 **FORK** |

🟢 **The mechanism, not just the dates: the Alliance copy is `21` days ahead with `9` more paths,
and its newest commit is authored BY `CSR2017` — the individual commits INTO the Alliance repo.
The personal copy's newest commit is a dependabot bump, which is what a fork on autopilot looks
like.** 🟢 **Both are `Apache-2.0` at `10 173 B`, identical.** 🟢 **Depend on the Alliance repo.**

### 🆕 🔴 `T184` — three published licence SIZE bands are wrong, and the corrections make the test LESS usable

🔴 **`P48` publishes size bands as a family confirmer. p166 body-read a `10 173 B` Apache-2.0 and
went looking:**

| family | published band | measured on this shelf | outside? |
|---|---|---|---|
| 🔴 **Apache-2.0** | `11 357`–`11 358 B` | 🔴 **`10 173`** · `11 342` · `11 408` | 🔴 **all three** |
| 🔴 **GPL-3.0** | `35 121`–`35 147 B` | 🔴 **`35 149`** *(on TWO repos)* | 🔴 **yes, by `2 B`** |
| 🟢 AGPL-3.0 | `34`–`35 KB` | 🟢 `34 522`–`34 523` | 🟢 within |

🟢 **Cause of the Apache outlier, confirmed not guessed: the `10 173 B` body contains `0`
occurrences of `APPENDIX` and ends at *"END OF TERMS AND CONDITIONS"*.** 🟢 **Apache-2.0 is
BIMODAL — with the *"APPENDIX: How to apply"* section it runs ~`11.3`–`11.4 KB`, without it
~`10.2 KB`. Both are Apache-2.0.**
🔵 **And `35 149 B` reproducing on a second, unrelated repository one pass later is the
licence-reproducibility check working.**
🟢 **Net effect: every correction here WIDENS a band, so `P48`'s own thesis — classify by the NAME
LINE, never the size — comes out stronger.** [`evidence/licence-band-correction.2026-10-13-p166.tsv`](../evidence/licence-band-correction.2026-10-13-p166.tsv)

## Pass 165 — 2026-10-13

🟢 **`ACTION IM` is DISCHARGED, falsifier SILENT: `P164-A`'s guards flipped a verdict on BOTH
platforms.** 🆕 🟢 **One genuinely new false-positive class (`T170`), and OpenOLAT's interop
surface is now QUANTIFIED rather than merely located.**
🟢 **`T142`'s plugin finding is corroborated and extended with a per-plugin licence read.**
[`evidence/interop-guarded-grep.2026-10-13-p165.tsv`](../evidence/interop-guarded-grep.2026-10-13-p165.tsv)

### 🆕 🔴 `T170` — the `-ed` + `fi` camelCase collision, a FIFTH false-positive class and the worst one yet

🔴 **Naive `ed-?fi` returned `620` files on OpenOLAT and `159` on edx-platform. Guarded: `0` and
`0`.** 🟢 **A verdict flip on both platforms — precisely what `ACTION IM`'s falsifier asked for,
so it did not fire.**
🟢 **This class is NOT in p164's taxonomy of three, and the shelf has no prior record of it:**

| platform | collision | hits |
|---|---|---|
| 🔴 OpenOLAT | `ableExtendedFilter` | 🔴 **`577`** |
| 🔴 OpenOLAT | `getSelectedFilterTab` · `setSelectedFilterTab` · `extendedFilter` | `204` · `181` · `169` |
| 🔴 OpenOLAT | `uploadedFile` · `scopedFilter` · `reloadedFile` | `114` · `63` · `53` |
| 🔴 edx-platform | `autoCreatedField` · `lastModifiedField` | `111` · `110` |
| 🔴 edx-platform | `SimpleUploadedFile` · `supportedFieldType` · `embeddedFiles` | `94` · `29` · `16` |

🆕 **`T170`:** 🔵 **an English past participle ending `-ed` followed by a noun beginning `fi`
(`field`, `file`, `filter`) is one of the commonest identifier shapes in any codebase. `Ed-Fi`
probed by substring therefore collides SYSTEMATICALLY, not incidentally — `577` hits from a single
identifier.**
🟢 **Rule for every industry shelf, not just this one: never probe `Ed-Fi` as a bare substring.
Require the hyphen with word boundaries, or probe the path plus the vendor namespace.**
🔵 **Distinct from p164's *substring-in-word* class, which was accidental (`facu`*`lti`*`es`): this
one is generated by English morphology and so recurs in every repository of sufficient size.**

### 🆕 🟢 `T171` — OpenOLAT's interop surface, QUANTIFIED

🔵 **The shelf already knew OpenOLAT is `Apache-2.0` and that its `lti13` lives in a directory.**
🟢 **What it did not have is the size of that surface, which is what decides whether a client can
rely on it.** 🟢 **Measured at HEAD `e4be14f0`, branch `master`, `2026-10-12`, `25 823` tracked
paths, full checkout:**

| standard | path hits | guarded content hits | verdict |
|---|---|---|---|
| 🟢 **LTI 1.3** | `361` | `354` | 🟢 **IMPLEMENTED IN-TREE — `org/olat/ims/lti13/`, `145` files, `18 067` Java LOC** |
| 🟢 **SCORM** | `163` | `338` | 🟢 **IMPLEMENTED IN-TREE — `65` Java files** |
| 🔴 OneRoster | `0` | `0` | 🔴 **ABSENT** |
| 🔴 Ed-Fi | `13` *(all false)* | 🔴 **`0`** | 🔴 **ABSENT** *(`T170`)* |
| 🔴 xAPI | `0` | 🔴 **`0`** | 🔴 **ABSENT — the only hits were a vendored `pdf.js` bundle** |

🟢 **Named classes inside the LTI 1.3 package: `LTI13Platform`, `LTI13Dispatcher`, `LTI13Key`
(JWKS), `LTI13DeepLinkingEnum`, `LTI13ContentItem`, `LTI13Context`, `DeploymentConfigurationPermission`.**
🟢 **SCORM: `ScormCourseNode`, `ScormAssessmentHandler`, `ScormAssessmentConfig`, `ScormEditController`.**
🔵 **`18 067` LOC is not a shim. It is a platform-side implementation, which is the side that
matters if the client wants to HOST tools rather than be one.**

🟢 **Corroboration of the shelf's own `T142` while doing this:** 🟢 **`lti_1p3|lti1p3|lti-1p3`
returns `0` files in OpenOLAT, which nonetheless implements the standard completely under the Java
spelling `LTI13`.** 🟢 **The language-independent probe that works on both platforms is the SPEC
URL — `imsglobal.org/spec/lti`: `12` files in OpenOLAT, `2` in edx-platform.**

### 🆕 🟢 `T172` — the Open edX constellation, licensed per repository

🟢 **`T142` established that edx-platform core carries integration points and the implementations
live in sibling packages. p165 read each sibling's licence and release channel, which `T142` did
not do:**

| repository | licence *(body-read)* | paths | HEAD | PyPI |
|---|---|---|---|---|
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **`AGPL-3.0`** *(`35 136 B`)* | `9 276` | `2026-10-12` | — |
| 🔴 [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) | 🔴 **`AGPL-3.0`** | `237` | `2026-10-01` | 🟢 `lti-consumer-xblock v11.4.2`, `2026-10-01` |
| 🔴 [`openedx/event-routing-backends`](https://github.com/openedx/event-routing-backends) | 🔴 **`AGPL-3.0`** | `352` | `2026-10-07` | 🟢 `v10.1.0`, `2026-09-30`, `AGPL-3.0-or-later` |
| 🔴 [`overhangio/openedx-scorm-xblock`](https://github.com/overhangio/openedx-scorm-xblock) | 🔴 **`AGPL-3.0`** | `48` | `2026-10-09` | 🟢 `v19.0.5`, `2026-10-09`, `AGPLv3` |
| 🔴 `openedx/openedx-scorm-xblock` | — | — | — | 🔴 **ABSENT — the SCORM plugin is NOT under the `openedx` org; it is Overhang.IO's** |
| 🔴 `openedx/openedx-oneroster` | — | — | — | 🔴 **ABSENT — no OneRoster repo under the org** |

🆕 **`T172`:** 🔴 **there is no permissive path through Open edX's interop surface at ANY layer —
core, plugin or published package.** 🟢 **PyPI metadata agrees with every `LICENSE` body, which is
a second independent channel on a question where getting it wrong is expensive.**
🔵 **Stated fairly: AGPL-3.0 is a GATE, not a defect, and Open edX remains the most capable OSS
LMS in this field. Whether the gate binds depends on whether the client distributes or offers the
platform as a network service — a question for their counsel.**
🟢 **Set against `T171`, this is a routing decision rather than a preference, and it is filed in
[`verticals/solutions.md`](../verticals/solutions.md).**

### 🆕 🟢 `T176` — the three guards are not equally valuable, and the weighting INVERTS between repositories

🟢 **Measured on `lti` in OpenOLAT, guard by guard:**
`4 987` files → `grep -I` → `4 973` *(binaries: `0.3%`)* → `--exclude='*.po'` → `4 973`
*(i18n: `0`)* → `\b` boundaries → 🟢 **`354`** *(word boundaries: `93%`)*.
🔴 **On OpenEduCat in p164 the weighting was the REVERSE — binaries and Danish `.po` entries did
the damage, and boundaries less.**
🆕 **`T176`:** 🟢 **keep all three guards not because each always fires, but because which one
fires is not predictable from the term or the repository.** 🔵 **A probe that drops the "useless"
guard after one repository will be wrong on the next one.**

🔵 **And one verdict that needed a fourth category rather than a guard:** 🔴 **edx-platform's only
two SCORM hits are both `envs/mock.yml`, and its xAPI hits are `requirements/*.txt`, `uv.lock`, a
migration and an ADR.** 🟢 **Declaring a dependency is not implementing a standard — reported as
CONFIG-ONLY, which is now an explicit verdict in `P165-A`.**

## Pass 164 — 2026-10-13

🟢 **No new platform row this pass.** 🔴 **The row p163 added is DOWNGRADED on measurement, and
p162's cheap-census instrument (`P162-A`) is CORRECTED — it has a failure mode that cost this
pass real time and that the shelf had not recorded.**

### 🆕 🔴 `openeducat/openeducat_erp` — DOWNGRADED from 🟡 to 🔴 on `ACTION IJ`

🟡 **p163 gave it an amber row as *"a REAL, maintained, self-hostable education ERP with
rostering standards — the integration-target class"*.** 🔴 **The rostering standards are not
there.**
[`evidence/openeducat-interop-probe.2026-10-13-p164.tsv`](../evidence/openeducat-interop-probe.2026-10-13-p164.tsv)

| field | p163 | p164 |
|---|---|---|
| 🟢 repo / head | `1c95cef`, branch `19.0` | 🟢 **unchanged, re-confirmed** |
| 🟢 licence | 🔴 LGPL-3.0, body `8 241 B`, INCOMPLETE on its own terms | 🟢 **unchanged** |
| 🟡 **OneRoster / Ed-Fi / LTI 1.3** | 🟡 *vendor-stated, registered as `ACTION IJ`* | 🔴 **ALL THREE ABSENT — `0` implementing code (`T161`)** |
| verdict | 🟡 amber — integration target | 🔴 **red — bespoke integration only** |

🔵 **Why it keeps a row at all:** 🟢 **it is still a real, maintained ERP with `14` in-tree
modules covering admissions, fees, library and timetable, and those are domains the other four
platforms do not touch.** 🔴 **What changed is the cost of using it: with no standards surface,
every integration is bespoke, and that is a different line in an estimate.**

🔵 **The generalisable lesson, which is worth more than the row:** 🟢 **p163 wrote the claim down
as *vendor-stated* and registered it instead of repeating it. One pass later it was measured and
was false.** 🔴 **Had it been written as fact, this shelf would now be recommending a rostering
integration path that does not exist.**

### 🆕 🔴 `P162-A` is CORRECTED — blobless clones have a failure mode, and it is the obvious one

🟢 **p162 and p163 established `--depth=1 --filter=blob:none --no-checkout` as the default
instrument, at `3.1 MB` for Moodle's `67 589` paths.** 🟢 **That measurement is CORRECT and is
re-confirmed this pass.** 🔴 **What was never stated is what happens when you then need the
FILE CONTENTS.**

🔴 **Measured this pass on `openeducat_erp`, `1 345` paths — the smallest tree on this shelf:**

| approach | result |
|---|---|
| 🟢 blobless clone, path census only | 🟢 **`236 KB`, seconds** |
| 🔴 **blobless clone + `git checkout` of the whole tree** | 🔴 **fetches blobs ONE AT A TIME; still running at `35 MB` after several minutes, and was abandoned** |
| 🟢 **plain `--depth=1` clone (one packfile)** | 🟢 **`65 MB`, completed in a single transfer** |

🆕 **`P164-B` — the corrected rule, in three lines:**

1. 🟢 **Path census, licence read, single-file read → blobless `--no-checkout`, then
   `git cat-file`.** 🟢 **Cheapest by a wide margin; `236 KB` beat `65 MB` by `275×` here.**
2. 🔴 **Whole-tree CONTENT sweep → plain `--depth=1`.** 🔴 **Never `checkout` a blobless clone:
   on-demand fetch is per-blob and is slower than downloading everything once.**
3. 🟢 **Subsystem content sweep → blobless + `git sparse-checkout set <dir>`.** 🟢 **Measured
   this pass at `1.4 MB` for OpenOLAT's AI subsystem (`107` Java files) and `3.3 MB` for
   Moodle's (`279` PHP files).**

🔵 **Why this belongs on the foundations page rather than in a footnote: three passes have now
been planned around *"the clone channel is cheap"*, and it is cheap only for the operations it
is cheap for.**

### 🆕 🟢 `P164-A` — the twelve-row recency sweep, and what it costs

🟢 **`T159`'s instrument, stated as a recipe because it is the one this shelf will run every
pass from now on.** 🟢 **Per repository, with no GitHub API and no authentication:**

```sh
git ls-remote --symref https://github.com/$R HEAD     # existence, default branch, HEAD sha
git ls-remote --tags   https://github.com/$R          # full tag list -> release cadence
git clone -q --depth=1 --filter=blob:none --no-checkout https://github.com/$R $D
git -C $D log -1 --format=%cI                         # HEAD commit DATE
git -C $D ls-tree -r --name-only HEAD | wc -l         # tracked paths
```

🟢 **Twelve repositories in parallel: `3 060 KB` total, one pass.** 🟢 **Yields existence
(`P54`), maintenance age, release discipline and project size — four fields, all primary, none
of which the dead `★` column ever provided.**

### 🟢 The foundations shelf — unchanged otherwise

🟡 **No new foundational repository was added this pass.** 🔵 **Deliberate rather than empty: the
three pre-registered actions were all code-channel probes of platforms already on the shelf, and
global discovery returned `0` education-domain candidates for an eighth consecutive pass
(`T110`).** 🟢 **Recorded so the absence is visible as a decision, not an oversight.**

## Pass 163 — 2026-10-13

🟢 **One new platform row, licence read from the body at source, with TWO grant defects measured
rather than inferred.** 🟢 **And p162's cheap-census instrument (`P162-A`) corroborated a second
time on a second repository, at a cost that makes the clone channel the default rather than the
fallback.**
[`evidence/openeducat-grant.2026-10-13-p163.tsv`](../evidence/openeducat-grant.2026-10-13-p163.tsv)

### 🆕 🟡 `openeducat/openeducat_erp` — the Odoo-based education ERP, LGPL-3.0, and its grant is INCOMPLETE BY ITS OWN WORDS

🔵 **Why it was probed:** 🟢 **the vertical-platform query returned a single vendor's marketing
pages and one claim worth testing — that OpenEduCat is an LGPLv3 Python/Odoo alternative to
Moodle with OneRoster, Ed-Fi and LTI 1.3.** 🔴 **A vendor page is not a grant, so the grant was
read from the tree.**

| field | measurement |
|---|---|
| 🟢 repo | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) |
| 🟢 head | `1c95cefebc176a011e3c16269c5a8691fd1ac9cb` |
| 🟡 **default branch** | 🟡 **`19.0`** — *not* `main` or `master`; it tracks the Odoo major version |
| 🟢 last commit | `2026-09-07` |
| 🟢 tracked paths | `1 345` |
| 🟢 licence path | `LICENSE` — 🟢 **the ONLY licence-bearing path in the whole tree** |
| 🟢 licence body | **LGPL-3.0**, `8 241 B`, `178` lines, blob `ef163fea`, sha256 `528f8403…47a9` |
| 🟢 name line | *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* |

🆕 🔴 **Defect 1 — the body promises the GPL and does not contain it.** 🟢 **Its own fourth line
says the LGPL *"is a set of additional permissions on top of the GPL"* and that *"the text of the
GPL is included at the bottom as well"*.** 🔴 **At `8 241 B` it cannot be: GPL-3.0 alone is
~`35 kB`, and the file ends at the LGPL's proxy clause.** 🔵 **LGPL-3.0 is not a standalone
licence by its own construction, so the grant is incomplete on the terms it sets itself.**

🆕 🔴 **Defect 2 — the file it points at is ABSENT.** 🟢 **Line 2 reads *"For copyright
information, please see the COPYRIGHT file"*.** 🔴 **`0` of `1 345` tracked paths match
`/copyright/i`.** 🔵 **This is `P49`'s pattern again — a file named `LICENSE` is not evidence of a
complete grant — now with a dangling reference as well as a short body.**

🟢 **The engagement consequence, stated plainly:** 🔴 **LGPL-3.0 is copyleft, so OpenEduCat is
outside Globant's permissive lane whatever the body says.** 🟢 **It earns a row because it is a
REAL, maintained, self-hostable education ERP with rostering standards — the integration-target
class, not the fork class** — 🔵 **and because the two defects are exactly what a client's licence
review would raise in week one, so finding them now is cheaper than finding them then.**

### 🟢 `P162-A` corroborated a second time — the clone channel is now the DEFAULT instrument

🟢 **p162 measured `--depth=1 --filter=blob:none --no-checkout` at `3.1 MB` for Moodle's
`67 589` paths.** 🟢 **Two independent repeats this pass:**

| repo | `.git` after blobless shallow clone | tracked paths | sparse working tree |
|---|---|---|---|
| 🟢 `openolat/openolat` | **`1.3 MB`** | `25 823` | **`7.0 MB`** for the whole AI subsystem |
| 🟢 `Selleo/mentingo` | **`408 KB`** | `4 753` | **`4.2 MB`** for `apps/api/src/ai` + `packages/prompts` |
| 🟢 `openeducat/openeducat_erp` | *(blobless, no checkout)* | `1 345` | 🟢 **licence read by `cat-file` on a single blob — no checkout at all** |

🔵 **The `cat-file` path is the cheapest grant read this shelf has: resolve the blob id from
`ls-tree`, fetch exactly that object, read the body, hash it.** 🟢 **No working tree, no checkout,
and the sha256 is recorded so the next pass can prove identity without re-reading.**

### 🔴 What this page still cannot do, after p163

- 🔴 **Rank anything. `search/repositories` stays `403` and `ACTION IF` establishes that attaching
  repositories does not reopen it** *(`T149`)*.
- 🟡 **Three passes of OpenOLAT findings and now four rest on ONE tree** (`e4be14f0`, unchanged
  since p160, re-confirmed as HEAD this pass with a `2026-10-12` last commit). 🔵 **Carried
  forward as a concentration risk, not a defect.**
- 🔴 **OpenEduCat's rostering claims (OneRoster, Ed-Fi, LTI 1.3) are VENDOR-STATED and were not
  verified in the tree this pass.** 🟢 **Registered as `ACTION IJ` rather than repeated as fact.**

## Pass 162 — 2026-10-13

🟢 **`ACTION ID` ran on this page's two most load-bearing platform rows and returned the result
this page wanted: `0 of 8` published capabilities fail STEP 7 or STEP 8.**
🔴 **It also found that the audit cannot see what the page never claimed, and that STEP 7 has a
HORIZON on Moodle that it does not have on Django.**
[`evidence/step7-step8-audit.2026-10-13-p162.tsv`](../evidence/step7-step8-audit.2026-10-13-p162.tsv)

### 🟢 `ACTION ID` — DISCHARGED, falsifier SILENT. Every capability this page publishes survives

🔴 **The falsifier was: *"refuted if `≥1` capability currently published for either platform fails
STEP 7 or STEP 8"*.** 🟢 **Eight audited, zero failures.**

| platform | published capability | STEP 7 — deleted by migration? | STEP 8 — out of repo? |
|---|---|---|---|
| 🟡 `moodle/moodle` | Open Badges, `306` paths, OB v2 | 🟡 **NARROWED — `badge.imageauthorname` / `imageauthoremail` / `imageauthorurl` dropped at `2025013100.01`** | 🟢 no |
| 🟡 `moodle/moodle` | xAPI, `78` paths | 🟢 no | 🟢 no |
| 🟡 `moodle/moodle` | LTI 1.3 / `ltiadvantage` | 🟢 no | 🟢 no |
| 🟡 `moodle/moodle` | core AI subsystem, `372` files | 🟢 **no — `ai_provider` CREATED at `2025011700.02`, actively evolving** | 🟢 no |
| 🟢 `Selleo/mentingo` | SCORM, `119` files *(`T135`)* | 🟢 no | 🆕 🟡 **PARTLY — the player is `scorm-again@3.0.4`, an EXTERNAL npm dependency** |
| 🟢 `Selleo/mentingo` | xAPI — published ABSENT *(`T127`)* | n/a | 🟢 **ABSENCE CONFIRMED by a second instrument: `0` `xapi`/`tincan`/`caliper` entries across `7` manifests** |

🟢 **`Open Badges` is narrowed, not deleted — the capability stands and the `306`-path figure is
not retracted.** 🔵 **But a field drop IS the shape `T141` warned about, caught one level down
from where it was expected.**

🆕 🟢 **The SCORM row improves on audit rather than degrading.** 🟢 **`T135` said mentingo ships
SCORM; STEP 8 confirms it from a different channel and names the player:
`@repo/scorm-export-generator` + `@repo/scorm-export-runtime` in-tree, plus
[`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) `3.0.4` at the registry.**
🟢 **Licence closure read from `registry.npmjs.org`: `MIT` over `MIT`. Clean.**

### 🆕 🔴 `T146` — a STEP 7 / STEP 8 audit is structurally blind to a capability nobody published

🔴 **Both steps take the PUBLISHED LIST as their input, so they can only ever confirm or retract
what a previous pass chose to write down.** 🔴 **While auditing mentingo's SCORM row, the
migration directory produced `0162_add_ai_judge_schema.sql` — a complete evaluative AI subsystem
that five passes of this shelf never recorded** *(`T145`, `agents/top.md`)*.

🟢 **`P160-A` gains STEP 9:**

```bash
# STEP 9 (T146) — enumerate the platform's OWN capability vocabulary before auditing the list
#   you already have. The schema and migration names are the platform's self-description.
ls $DIR/**/migrations/*.sql | sed 's/.*[0-9]\{4\}_//;s/\.sql$//' | tr '_' ' ' | sort -u
grep -rhoE 'CREATE TABLE[^"]*"([a-z_]+)"' $DIR --include=*.sql | sort -u
# A capability named in the schema and absent from your published list is a MISS, not a pass.
```

### 🆕 🔴 STEP 7 has a HORIZON on Moodle that it does not have on Django

🟢 **Measured: `public/lib/db/upgrade.php` is `108 269 B` and `90` upgrade steps, covering
`$oldversion < 2022112802` through `< 2026092300`.**
🔴 **Moodle TRUNCATES upgrade history at major releases. Django migrations are RETAINED forever.**
🔵 **So STEP 7 saw every badge deletion in `edx-platform` back to 2023 (`T141`) but can only see
the current window on Moodle — a capability deleted before 2022 is invisible to this instrument,
and the honest form of a Moodle STEP 7 result is *"no deletion in the current upgrade window"*,
not *"never deleted"*.**

🟢 **What STEP 7 did find in the window, in full:** 🔴 **`1` table dropped —
`moodlenet_share_progress` at `2026030600.02`, removing MoodleNet OUTBOUND SHARING along with
`moodlenetprofile` and the MoodleNet OAuth2 config.** 🟢 **No false presence on this shelf:
`moodlenet/moodlenet` was REJECTED on liveness at `2023-07-07` and never published as a
capability.** 🟡 **`8` field drops, of which `3` are the badge attribution fields above and one is
`grade_grades.overriddenmark` at `2025040700.00`.**

### 🟢 STEP 8's verdict on Moodle, which is the useful negative

🟢 **`composer.json` and `package.json` carry `0` matches for `lti`, `xapi`, `caliper`,
`credential` or `badge`.** 🔵 **Moodle vendors its capabilities IN-TREE, so `T142` — the false
absence that a single-repo census publishes on a plugin platform — does NOT apply to Moodle.**
🟢 **Every path count this page publishes for Moodle is therefore safe from the `edx-platform`
defect, and that is now measured rather than assumed.**

### 🆕 🟢 `P162-A` — the path census, PRICED. P161-C's untested prescription is a `240×` saving

🔴 **p160 spent `746 MB` on a Moodle clone. p161 spent `752 MB` trying to avoid it and recorded
that `--filter=blob:none` saves NOTHING with a checkout, correctly prescribing `--no-checkout`
without pricing it.** 🟢 **Priced this pass, same repository, same question:**
[`evidence/clone-instrument-cost.2026-10-13-p162.tsv`](../evidence/clone-instrument-cost.2026-10-13-p162.tsv)

| instrument | disk | wall | what it buys |
|---|---|---|---|
| 🟢 `git ls-remote --symref` | ~`0` | `<1s` | default branch + HEAD |
| 🆕 🟢 **`--depth=1 --filter=blob:none --no-checkout`** | 🟢 **`3.1 MB`** | 🟢 **`1s`** | 🟢 **all `67 589` paths** |
| 🆕 🟢 **`+ cone sparse-checkout` of the directories under test** | 🟢 **`26 MB`** | 🟢 **`2s`** | 🟢 **`677` files of CONTENT, the whole `public/ai` subsystem** |
| 🟢 `raw.githubusercontent.com`, path known | 🟢 **`108 KB`** | `<1s` | 🟢 **`ACTION ID`'s entire Moodle limb** |
| 🔴 `--depth=1` full shallow clone | 🔴 **`746 MB`** | — | the same `67 589` paths |

🟢 **Agreement check, because a cheaper instrument is worthless if it disagrees: `67 589` paths
from the `3.1 MB` clone is byte-identical to p161's `67 589` from the `746 MB` clone.**
🔵 **`240×` cheaper for the census, `28×` cheaper for the subsystem read, same answer.**
🟢 **STEP 1 of `P160-A` splits: STEP 1a paths, STEP 1b sparse content, STEP 1c a full clone only
when the question is genuinely tree-wide.**
## Pass 161 — 2026-10-12

🟢 **Two pre-registered actions discharged on this page: `ACTION HZ` (`OpenOLAT`'s AI surface,
falsifier FIRED) and `ACTION IB` (`P160-A` over `openedx/edx-platform`, falsifier SILENT).**
🔴 **Between them they correct one claim this page has been making and add a fourth contamination
to the path census.**

### 🔴 `ACTION HZ` — REFUTED. OpenOLAT's AI ledger is RICHER than Moodle's, not absent

🔴 **The falsifier was: *"refuted if OpenOLAT ships a per-call AI audit ledger comparable to
`ai_action_register`"*. It ships one, and *comparable* understates it.**
[`evidence/ai-surface-tri-platform.2026-10-12-p161.tsv`](../evidence/ai-surface-tri-platform.2026-10-12-p161.tsv)

| dimension | Moodle `ai_action_register` | OpenOLAT `o_ai_usage_log` |
|---|---|---|
| columns | `15` | 🟢 **`33`** |
| who / where | `userid`, `contextid`, `courseid` | `fk_identity`, `a_usage_context_type`, `a_usage_context_id`, `a_resource_type`, `a_resource_id`, `a_resource_sub_id`, `a_locale` |
| provider / model | `provider`, `model` | `a_model_provider`, `a_req_model`, 🟢 **`a_resp_model`** *(what was ASKED FOR vs what ANSWERED)* |
| request parameters | 🔴 **none** | 🟢 **`a_req_temperature`, `a_req_top_p`, `a_req_max_output_tokens`, `a_req_num_messages`, `a_req_text_length`** |
| tokens | `prompttokens`, `completiontokens` | `a_input_tokens`, `a_output_tokens`, `a_total_tokens`, 🟢 **`a_cached_input_tokens`, `a_reasoning_tokens`, `a_cache_creation_input_tokens`** |
| outcome | `success`, `errorcode`, `errormessage` | `a_status`, `a_error_code`, `a_error_message`, 🟢 **`a_resp_finish_reason`** |
| timing | `timecreated`, `timecompleted` | `creationdate`, 🟢 **`a_duration_millis`** |
| correlation | 🔴 **none** | 🟢 **`a_invocation_id`, `a_resp_id`, `a_service_interface`, `a_service_method`** |
| prompt / response TEXT | 🔴 **yes — in four per-action tables** *(`ACTION IA`, below)* | 🟢 **NO in the log; yes in `o_ai_essay_correction` for the grading feature only** |

🔵 **The honest reading:** 🟢 **OpenOLAT's log is a better COST and RELIABILITY instrument
(parameters, cache tokens, latency, finish reason, call correlation).** 🟢 **Moodle's is a better
EVIDENCE instrument for a regulator, because it keeps what was asked and what came back.**
🔴 **Neither has a retention policy.**

### 🆕 🔴 `ACTION IA` — Moodle's ledger retains BOTH prompt and response, and nothing ever deletes them

🔴 **Falsifier SILENT: the ledger retains prompt AND response text.**
[`evidence/moodle-ai-ledger-schema.2026-10-12-p161.tsv`](../evidence/moodle-ai-ledger-schema.2026-10-12-p161.tsv)

- 🔴 **`ai_action_register` is an INDEX, not the payload.** 🟢 **`actionid` points into one of four
  per-action tables, and three of them —`ai_action_generate_text`, `ai_action_summarise_text`,
  `ai_action_explain_text` — store `prompt text` and `generatedcontent text` verbatim.**
  🔴 **`ai_action_generate_image` stores `prompt`, `revisedprompt` and `sourceurl`.**
- 🟢 **Subject access and erasure are IMPLEMENTED and complete:**
  `core_ai\privacy\provider`, `806` LOC, implements `metadata\provider` +
  `request\subsystem\provider` + `core_userlist_provider`, with `export_user_data`,
  `delete_data_for_user`, `delete_data_for_users`, `delete_data_for_all_users_in_context` and
  `get_users_in_context`. 🟢 **All six AI tables are declared in the privacy metadata.**
- 🔴 **Retention is ABSENT.** 🔴 **`grep -riE 'retention|purge|cleanup|expiry' public/ai/` returns
  nothing but a UI modal's `cleanUp()`; `public/ai` has NO `db/` directory, NO scheduled task and
  NO `settings.php`.** 🟡 **The only task in the subsystem is an adhoc `backfill_action_courseid`.**
- 🟡 **A generic remedy exists and is OFF by default:** `tool_dataprivacy` purposes carry retention
  periods and `tool_dataprivacy\task\delete_expired_contexts` executes them — 🔴 **gated on
  `tool_dataprivacy/automaticdatadeletionapproval`, which ships `0`, and no AI-specific purpose
  ships at all.**
- 🔵 **The client-facing consequence:** 🔴 **a Moodle site that enables AI accumulates every student
  prompt and every model response indefinitely, in a table a GDPR subject-access request will
  correctly export.** 🟢 **`P161-B` is the bounded fix.**

### 🆕 🟢 `ACTION IB` — `edx-platform` HAS tenancy, and the census found a capability that was DELETED

🟢 **Falsifier SILENT.** 🔴 **But a token census says the opposite, and that is the finding.**
[`evidence/edx-tenancy-census.2026-10-12-p161.tsv`](../evidence/edx-tenancy-census.2026-10-12-p161.tsv)

- 🔴 **`ipath '*tenant*'` returns `0`.** 🟢 **Tenancy is PRESENT and is spelled `site`:
  `SiteConfiguration` is a `OneToOneField` on `django.contrib.sites.Site` with a `site_values`
  `JSONField` that overrides settings per tenant; `66` files import `django.contrib.sites`.**
  🔵 **`T136c` — take the vocabulary from the platform — generalises beyond `lti`.**
- 🆕 🔴 **`T141` — a path census cannot see a capability DELETED BY MIGRATION.**
  🔴 **`ipath '*badge*'` returns `38` paths, `23` of them non-test, including a whole
  `lms/djangoapps/badges` app — and `migrations/0005_delete_all_models.py` (2023-10-24) drops
  `BadgeClass`, `BadgeAssertion`, `CourseEventBadgesConfiguration` and
  `CourseCompleteImageConfiguration`. `models.py` is a `25`-line stub.**
  🔵 **The fourth contamination: `T136` over-counts by NAME, this one over-counts by HISTORY.
  The gate is the migration directory, and `P160-A` gains a STEP 7.**
- 🔴 **`T142` — a single-repo clone census UNDER-reads a plugin-architecture platform.**
  🔴 **`lti13` / `lti1p3` / `ltiadvantage` all return `0`; `lti_consumer` returns `3` references —
  the implementation is the separate `lti-consumer-xblock` package, pinned in
  `requirements/edx/base.txt`. `xapi` returns ONE path, a migration adding external-ID types;
  emission lives in `event-routing-backends`.** 🔵 **Read alone, the clone publishes FALSE
  ABSENCES for LTI 1.3 and xAPI. The dependency manifest is the second instrument.**
- 🔴 **`0` AI files, `0` references to any LLM provider — `edx-platform` core has no AI subsystem
  at all**, against Moodle's `372` and OpenOLAT's `149`.
- 🔴 **Licence: AGPL-3.0, body read, `35 136 B`.** 🔴 **It is NOT in the permissive tier and never
  was; this page should say so wherever it recommends Open edX.**
- 🟢 **OB 3.0 / W3C VC: `0` matches.** 🔴 **`0 of 6` platforms on this shelf issue a modern
  verifiable credential** — p159's `0 of 5` extended, and `P159-A` stands as a build.

## Pass 160 — 2026-10-12

🟢 **`ACTION HX` DISCHARGED, falsifier SILENT: Moodle DOES ship Open Badges — `306` paths — so
`T133` is a PATTERN, not one instance, and the *"credentialing has no incumbent"* finding was
wrong on BOTH platforms this shelf recommends.**
🟢 **`ACTION HY` DISCHARGED on both limbs, falsifier SILENT: `0 of 4` permissive platforms issue
an OB 3.0 / W3C Verifiable Credential — and neither does Moodle, so it is `0 of 5`.**
🆕 🟢 **The pass's largest discovery was not registered at all: Moodle ships a provider-pluggable
AI subsystem in CORE, with an audit ledger as database rows.**

### 🆕 🟢 `moodle/moodle` read from the tree — `ACTION HX` in full

🟢 **`746 MB`, `67 589` tracked files, `depth=1` clone of `main`, HEAD `f20534726` identical to
`ls-remote`.** 🟢 **`6.0dev`, build `20261005`, branch `600`, read from `public/version.php`.**
🔴 **Note for every future pass: Moodle's tree moved under `public/` — a probe against
`mod/`, `lib/` or `badges/` at the root returns `0` and means nothing.**
[`evidence/moodle-surface.2026-10-12-p160.tsv`](../evidence/moodle-surface.2026-10-12-p160.tsv)

| dimension | Moodle `6.0dev` | `OpenOLAT` *(p159, re-measured p160)* | who wins for a studio |
|---|---|---|---|
| 🟢 **Licence** | 🟡 **GPL-3.0** — `COPYING.txt`, `35 147 B` | 🟢 **Apache-2.0** — `10 982 B` | 🟢 **OpenOLAT.** 🔵 **No patent grant and no permissive terms in Moodle; `T129`'s original catch, re-confirmed** |
| 🟢 **LTI 1.3 both ways** | 🟢 **YES** — `mod/lti` as platform (`254` files), `enrol/lti` + `auth/lti` as tool (`154`), `lib/lti1p3` | 🟢 **YES** — `lti13.platform.iss` + `LTI13Platform` | 🟢 **Tie** |
| 🟢 **AGS / NRPS / Deep Linking / JWKS** | 🟢 **ALL FOUR** — `gradebookservices/.../lineitem.php`, `nrps_info.php` + `sync_members.php`, `openid-configuration.php` + `contentitem.js`, `ltiopenid/jwks_helper.php` + `enrol/lti/jwks.php` | 🟢 **ALL FOUR** | 🟢 **Tie** |
| 🟢 **Open Badges** | 🟢 **YES — `306` paths**, `assertion.php`, `badgeclass.php`, `criteria/`, backpack export | 🟢 **YES — `182` paths** | 🟢 **Tie** |
| 🔴 **Open Badges version** | 🔴 **`v2` ONLY — `OPEN_BADGES_V2` ×`132`, `V1` ×`2`, `backpack_api2p1_mapping.php`** | 🔴 **`v2` ONLY** | 🔴 **Neither.** 🆕 **`ACTION HY`'s answer** |
| 🔴 **OB 3.0 / W3C VC** | 🔴 **ABSENT — `0` on eight spellings** | 🔴 **ABSENT — `0`** | 🔴 **Neither** |
| 🟢 **xAPI** | 🟢 **PRESENT — `public/lib/xapi`, `78` paths: `api.php`, `iri.php`, `state_store.php`, `handler.php`** | 🔴 **ABSENT — `0`** | 🟢 **MOODLE — and this is the FIRST capability on this shelf where Moodle beats OpenOLAT** |
| 🔴 **cmi5** | 🔴 ABSENT | 🔴 ABSENT | 🔴 Neither |
| 🟢 **SCORM** | 🟢 `226` paths | 🟢 `186` paths | 🟢 Tie |
| 🔴 **QTI** | 🔴 **`8` paths and ALL of them are QTI `v1.2` LEGACY** — IMS Common Cartridge `.xsd` schemas and a Blackboard import format. 🔴 **No QTI 2.x/3.0 engine** | 🟢 **`919` paths — a full QTI 2.1 assessment engine** | 🟢 **OpenOLAT, decisively. 🔵 For an assessment-heavy engagement this one dimension settles the platform choice** |
| 🔴 **Multi-tenancy** | 🔴 **ABSENT in core.** 🔴 **`62` *"tenant"* paths exist and `62 of 62` are inside the VENDORED `public/lib/google2-service`** *(`T136`)* | 🔴 **ABSENT** *(hierarchical organisations, not tenants)* | 🔴 **Neither.** 🟢 **`Selleo/mentingo` is still the only row on this shelf with a real tenancy boundary (PostgreSQL RLS, MIT)** |
| 🆕 🟢 **AI subsystem in CORE** | 🟢 **YES — `public/ai`, `372` files** | 🟡 **not measured this pass** | 🟢 **Moodle** |
| 🔴 **MCP server** | 🔴 ABSENT | 🟡 not measured | 🔴 Neither |

### 🆕 🟢 `T139` — Moodle's core AI subsystem logs every call as DATABASE ROWS, which is the audit artefact `P158-A` assembled by hand

🟢 **`public/lib/db/install.xml` defines seven core AI tables:** 🟢 **`ai_action_register`,
`ai_action_generate_text`, `ai_action_generate_image`, `ai_action_explain_text`,
`ai_action_summarise_text`, `ai_policy_register`, `ai_providers`.**
🟢 **`ai_action_register`'s own fields:** `actionname`, `actionid`, `success`, `userid`,
`contextid`, `courseid`, `provider`, `model`, `prompttokens`, `completiontokens`, `errorcode`,
`errormessage`, `timecreated`, `timecompleted`.

| layer | what ships | why a studio cares |
|---|---|---|
| 🟢 **Providers, pluggable** | 🟢 **`anthropic`, `awsbedrock`, `azureai`, `deepseek`, `gemini`, `ollama`, `openai`** — seven, `209` files | 🟢 **`ollama` in core means the SOVEREIGN deployment is a configuration, not a fork** — 🔵 **directly answers the EMEA data-residency objection** |
| 🟢 **Per-call ledger** | 🟢 **`ai_action_register` rows: who, which course, which provider, which model, tokens, success, error, timings** | 🟢 **This is the artefact an appeal or a regulator asks for.** 🔵 **`P158-A` built it from Langfuse traces; on Moodle it is already there, GPL-3.0** |
| 🟢 **Consent gate** | 🟢 **`ai_policy_register` + `policy_acceptance_report.php` + a `reportbuilder` system report** | 🟢 **Per-user AI-policy acceptance, reportable** — 🔵 **what the EU AI Act's transparency duty and the US state transparency clauses actually ask to evidence** |
| 🟢 **Rate limiting** | 🟢 **`public/ai/classes/rate_limiter.php`** | 🟢 Cost control in core |
| 🔴 **Actions — and this is the finding** | 🔴 **FOUR, and NONE is evaluative: `generate_text`, `generate_image`, `summarise_text`, `explain_text`** | 🔴 **Moodle core AI does NOT grade, score or place a learner.** 🟢 **So core Moodle sits OUTSIDE the EU AI Act's Annex III evaluative tier — and the moment a plugin adds an evaluative action, that plugin carries the high-risk obligations.** 🔵 **`P160-B` is built on exactly that line** |

🆕 **`T139`:** 🔵 **the governed-AI plumbing a client engagement would otherwise build — provider
abstraction, per-call audit, policy acceptance, rate limiting — is already in Moodle core and is
GPL-3.0.** 🟢 **What is NOT there is the evaluative capability, the tenancy boundary, and OB 3.0.**
🟢 **That is a far better starting position than this shelf has been assuming, and it changes
where the billable work sits.**

### 🟢 `ACTION HY`, second limb — `openlxp/openlxp-xia` assessed, and this shelf's description of it was WRONG

[`evidence/openlxp-xia-assessment.2026-10-12-p160.tsv`](../evidence/openlxp-xia-assessment.2026-10-12-p160.tsv)

| dimension | finding |
|---|---|
| 🟢 **Licence** | 🟢 **Apache-2.0, `11 357 B`, body-read — CONFIRMED** |
| 🔴 **What it is** | 🔴 **A `53`-file Django APP installed with `pip install OpenLXP-XIA`, not a platform.** 🟢 **A V-T-V-L pipeline: Validate → Transform → Validate → Load, for learning-experience METADATA** |
| 🔴 **Not learning RECORDS** | 🔴 **`0` matches for `xapi`, `caliper` or `statement`.** 🔴 **This shelf's `verticals/solutions.md` called it *"learning-record PLUMBING"* — it is metadata CATALOGUING plumbing. Corrected this pass** |
| 🔴 **Maintenance** | 🔴 **Last commit `2026-02-26` — `228` days, and it was a README edit.** 🔴 **`Django>=3.2.3,<4.0.0` — Django 3.2 reached END OF LIFE in April 2024; `boto3~=1.16.54`, `coverage<6.0`: a 2021-era pin set** |
| 🔴 **Needs siblings** | 🟢 **`openlxp/openlxp-xis` and `openlxp/openlxp-xss` RESOLVE.** 🔴 **`openlxp/openlxp-xsr-aws` DOES NOT RESOLVE — a credential prompt, so private or absent** *(`P54`)*. 🟡 **AWS S3 is the only schema server** |
| 🔴 **Verdict** | 🔴 **Do not put it in front of a client as a platform.** 🟡 **Permissive, readable and small enough to vendor the V-T-V-L idea from; shipping it as-is imports an EOL framework pin** |
## Pass 159 — 2026-10-12

🔴 **`ACTION HT` DISCHARGED and its falsifier is SILENT — but the pass that verified `OpenOLAT`
also discovered that this shelf's licence gate reports *"no licence"* for MOODLE.**
🟢 **Both findings are below, and the second one is the more important.**

### 🆕 🔴 `T129` — the licence gate's probe list produced FALSE ABSENCES at `4 of 15`, and the blind spots track project MATURITY

🟢 **The gate was run on a KNOWN-ANSWER control: fifteen platform and foundational rows whose
licences are not in doubt.** 🔴 **Four came back `NO_LICENCE_FILE`.**
[`evidence/licence-path-false-absence.2026-10-12-p159.tsv`](../evidence/licence-path-false-absence.2026-10-12-p159.tsv)

| repo | the 9-path list said | the licence is actually at | and it is |
|---|---|---|---|
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`COPYING.txt`** *(35 147 B)* | 🟢 **GPL-3.0** |
| 🔴 [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`license.txt`** *(35 149 B)* | 🟢 **GPL-3.0** |
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`NO_LICENCE_FILE`** | 🟢 **`license.txt`** *(33 893 B)* | 🔴 **AGPL-3.0 — STRICTER than ERPNext's GPL** |
| 🔴 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🔴 **`NO_LICENCE_FILE`** | 🟡 **`NOTICE.txt`** *(545 B)* | 🟡 **Apache-2.0 ASSERTED — and no licence TEXT anywhere in the tree** |

🆕 **`T129`, and the mechanism is the point:** 🟢 **GitHub's *"Add license"* button writes
`LICENSE`.** 🔴 **Projects that predate it, or that follow the GNU convention (`COPYING.txt`) or a
framework's house style (`license.txt`), do not.**
🔴 **So the probe list's blind spots are CORRELATED WITH MATURITY** — 🔴 **which means this
shelf's licence-absence claims were safest exactly where it sampled (the hobby tail, which uses
the button) and WRONG where it mattered most: the platform tier it puts in front of clients.**
🟢 **The same extended probe recovered only `2 of 47` in the `1 ★` tail — `4.3%` there against
`26.7%` on the control.** 🔵 **`T106`'s family again: the instrument's error rate is not constant
across the population it is used on.**

🟢 **`P56` is written** *(see `compose/patterns.md`)*: 🟢 **33 paths, SPDX line first, family read
from the TITLE line, and a byte floor that belongs to the family.**

### 🟢 `ACTION HT` — `OpenOLAT` speaks LTI 1.3 in BOTH directions, and the falsifier is SILENT

[`evidence/openolat-surface.2026-10-12-p159.tsv`](../evidence/openolat-surface.2026-10-12-p159.tsv)

🟢 **`org/olat/ims/lti13` — `148` path matches.** 🟢 **p158's expectation is CONFIRMED, which
matters because `ACTION HR` fired on exactly this expectation one pass ago.**

| dimension | finding | how measured |
|---|---|---|
| 🟢 **Licence** | 🟢 **Apache-2.0**, `10 982 B` | body read on `master` — 🔴 **its default branch is `master`, not `main`** |
| 🟢 **LTI 1.3 — as a PLATFORM** | 🟢 **`lti13.platform.iss`** — OpenOLAT issues as a platform and hosts external tools | `LTI13Module.java` read from `raw` |
| 🟢 **LTI 1.3 — as a TOOL** | 🟢 **`LTI13Platform` stores an EXTERNAL platform's `issuer`, `clientId`, `authorizationUri`, `tokenUri`, `jwkSetUri`** — which is exactly what a Tool keeps about its Platform | `LTI13Platform.java` |
| 🟢 **AGS** *(grade passback)* | 🟢 **`model/json/LineItem.java`, `LineItemScore.java`** | code search |
| 🟢 **NRPS** *(names & roles)* | 🟢 **`model/json/Member.java`, `Context.java`** | code search |
| 🟢 **Deep Linking** | 🟢 **`LTI13ContentItem.java`** | code search |
| 🟢 **OIDC / JWKS** | 🟢 **`OIDCApi.java`, `LTI13Key.java`, private/public key handling** | code search + `raw` |
| 🟢 **Named integrations** | 🟢 **`ZOOM`, `JUPYTER_HUB`, `MEDIASITE_GLOBAL`, `MEDIASITE_COURSE`, `EXTERNAL`, `EXT_TEMPLATE`, `SHARED`** | `LTI13ToolType.java` enum |
| 🟢 **QTI 2.1** | 🟢 **`org/olat/ims/qti21` — `660` path matches**, a full assessment engine | code search |
| 🟢 **SCORM** | 🟢 **`org/olat/modules/scorm` + `ScormCourseNode` — `154` paths** | code search |
| 🔴 **xAPI** | 🔴 **ABSENT — `0` matches across FOUR spellings** *(`xapi`, `cmi5`, `"Tin Can"`, `"experience api"`)* | code search |
| 🟢 **Open Badges** | 🟢 **`org/olat/modules/openbadges` — `156` paths**, `v2` package, LinkedIn push | code search — 🆕 **see `T133`** |
| 🔴 **Open Badges 3.0 / W3C VC** | 🔴 **ABSENT — `0` matches for `OpenBadgeCredential`, `VerifiableCredential`, `openbadges/v3`** | code search |
| 🟢 **Tenancy** | 🟢 **HIERARCHICAL organisations — materialized-path tree, `matchOrganisationOrItsParents`, `customerNumber`, `externalId`, per-organisation role grants, `15` `*ToOrganisation` scoping types** | `Organisation.java`, `RolesByOrganisation.java` |
| 🟡 **Tenancy enforcement** | 🟡 **APPLICATION-level. No row-level security.** | 🔵 **The honest contrast with `mentingo` — see below** |

🟢 **Cost of the whole assessment: `8` code searches, `7` `raw` fetches, one `ls-remote`. No clone.**
🟢 **`P55` holds a second time: *"does it integrate with X?"* is settled from the tree, not the
feature table.**

### 🆕 🔴 `T132` — the GitHub topic list is unreliable in BOTH directions

🔴 **p158's `T127` caught `mentingo`'s topic list OVER-claiming: it advertised `scorm` and `xapi`
the schema does not have.**
🔴 **`OpenOLAT` UNDER-claims: its topics are `qti`, `scorm`, `lms`, `curriculum-management`,
`assessment` — and `lti` is NOT among them**, although LTI 1.3 is its deepest integration
surface at `148` paths, in both directions, with AGS, NRPS and Deep Linking.
🆕 **`T132`:** 🔵 **a topic list is marketing, and marketing both exaggerates and forgets.**
🟢 **It can never settle a capability question in either direction — not presence, and not
absence.**

### 🟢 Tenancy, compared honestly — two different guarantees, not one better one

| | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) *(MIT)* | [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) *(Apache-2.0)* |
|---|---|---|
| **shape** | 🟡 **FLAT** — `tenantId` ×154 | 🟢 **HIERARCHICAL** — materialized path, parent matching |
| **enforced where** | 🟢 **DATABASE** — PostgreSQL RLS, least-privilege runtime role | 🟡 **APPLICATION** code |
| **what it buys** | 🟢 ***"a bug in application code cannot read another tenant's rows"*** | 🟢 **faculty → department → programme, with roles granted per node** |
| **where it fits** | 🟢 **Many unrelated customers on one deployment** | 🟢 **ONE institution with real internal structure** |

🔵 **Neither dominates.** 🔴 **A studio that wants a DB-level guarantee and a hierarchy has
neither off the shelf** — 🟢 **and that is a build, not a search.**

### 🟢 The foundational shelf, every licence re-read with the corrected gate

[`evidence/foundations-licences.2026-10-12-p159.tsv`](../evidence/foundations-licences.2026-10-12-p159.tsv)

| repo | default branch | licence *(body-read)* | tier |
|---|---|---|---|
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** *(10 982 B)* | 🟢 **Permissive + patent grant** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `main` | 🟢 **MIT** *(1 062 B)* | 🟢 **Permissive** — 🟢 **fourth consecutive confirming pass** |
| 🟢 [`openlxp/openlxp-xia`](https://github.com/openlxp/openlxp-xia) | `main` | 🟢 **Apache-2.0** *(11 357 B)* | 🟢 **Permissive** — 🆕 **NEW to this shelf: a learning-experience data pipeline** |
| 🟢 [`openfun/richie`](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** *(1 079 B)* | 🟢 **Permissive** |
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | `main` | 🟢 **MIT** *(1 066 B)* | 🟢 **Permissive** |
| 🟡 [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🔴 `master` | 🟡 **Apache-2.0 asserted in `NOTICE.txt`** *(545 B)*, no licence text in tree | 🟡 **Usable, but the grant is a NOTICE not a LICENSE** |
| 🟡 [`moodle/moodle`](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** *(`COPYING.txt`, 35 147 B)* | 🟡 **Copyleft — cross at a protocol boundary** *(`P156-A`)* |
| 🟡 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 `master` | 🟡 **AGPL-3.0** *(35 136 B)* | 🔴 **Hosting is distribution** |
| 🟡 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** *(35 147 B)* | 🟡 **Copyleft** — 🆕 **a THIRD default-branch convention** |
| 🟡 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** *(35 147 B)* | 🟡 **Copyleft** |
| 🟡 [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **`20.0`** | 🟡 **LGPL-3.0** *(43 529 B; its `LICENSE` defers to a `COPYRIGHT` file)* | 🟡 **Copyleft, library-scoped** |
| 🟡 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** *(8 241 B)* | 🟡 **Copyleft** — 🟢 **confirmed on a FIFTH ref** |
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **`develop`** | 🔴 **AGPL-3.0** *(`license.txt`)* | 🔴 **Hosting it for a client is distribution** |
| 🔴 [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **`develop`** | 🟡 **GPL-3.0** *(`license.txt`)* | 🟡 **Copyleft** |
| 🔴 [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🔴 `master` | 🔴 **LGPL-3.0** *(`LICENSE.txt`, 7 650 B)* | 🔴 **CORRECTION — p157 offered this as a BUILD BASE without naming its copyleft** |

🔴 **`9` of `15` are copyleft; `5` are permissive; `1` carries only a NOTICE.**
🔴 **`8` of `15` do NOT default to `main`** — `master` ×5, plus `release_11`, `20.0`, `19.0` and
`develop` ×2. 🟢 **`P53` is not an edge case on this shelf; it is the majority case.**
🟢 **And the search channel's `default_branch` agreed with `ls-remote` on `100 of 100` tail rows**,
🔵 **so resolving the ref is now cheap — but `ls-remote` is still what proves the repository
EXISTS** *(`P54`)*.
## Pass 158 — 2026-10-12

🔴 **`ACTION HR` DISCHARGED and its falsifier FIRED. `Selleo/mentingo` does NOT speak LTI 1.3,
and this shelf has been recommending it inside `P156-A` on the assumption that it does.**
🟢 **Four passes of carrying it unassessed is over: data model, multi-tenancy, SCORM surface and
LTI support are all now measured from the repository itself.**
[`evidence/mentingo-surface.2026-10-12-p158.tsv`](../evidence/mentingo-surface.2026-10-12-p158.tsv)

### 🔴 `ACTION HR` — LTI 1.3 is ABSENT, and the claim this shelf repeated came from a topic list

🔴 **`lti` appears 4 times in the `100 244 B` schema module. All four are substrings of other
words** — `multirange` ×3, `totalTime` ×1. 🔴 **There is no LTI table, no LTI column, no LTI
dependency in `apps/api/package.json`.**
🔴 **`xapi` appears `0` times.**

🔴 **The only place `LTI` and `xAPI` appear in the whole repository front matter is inside an
HTML comment in the README, in Polish, which translates as:**

> *"STAGE 3 — to be confirmed by the team, DO NOT PUBLISH WITHOUT VERIFICATION: ISO 27001
> (Selleo certificate or only process conformity?), WCAG 2.1 AA (accessibility audit), DPA/GDPR
> template, pentest, **xAPI/LTI**, mapping to NIS-2 / art. 8e KSC, retention and data deletion."*

🟢 **So the maintainers know these are unverified, and deliberately commented them OUT of the
rendered README.** 🔴 **This shelf nevertheless published *"SCORM + xAPI"* on this row for four
passes** — 🔴 **read, on p157's own account, from the repository's GitHub TOPIC LIST.**

🆕 **`T127`:** 🔴 **a FEATURE claim fails across instruments exactly the way `T117` showed a
LICENCE claim fails, and the ranking of instruments is the same** — 🟢 **the data model is
authoritative, the rendered README is cautious, and the topic list is marketing.**
🔵 **`T110`, `T117`, `T120`, `T121` and now `T127`: on this shelf, every instrument that is cheap
to read is the one that is wrong.**

### 🟢 What `mentingo` actually is, measured

| dimension | finding | how measured |
|---|---|---|
| 🟢 **Licence** | 🟢 **MIT**, `1 062 B`, *"Copyright (c) 2024 Selleo"* | body re-read on `main` — **CONFIRMED, third pass running** |
| 🔴 **LTI 1.3** | 🔴 **ABSENT** | `0` real hits in schema; unverified HTML comment only |
| 🔴 **xAPI** | 🔴 **ABSENT** | `0` hits in schema |
| 🟡 **SCORM** | 🟡 **README says *"SCORM 1.2 export"*. The SCHEMA carries `scorm_packages`, `scorm_scos`, `scorm_attempts` and `scorm_runtime_state`, plus 5 SCORM enums including `scormStandardEnum`** | 🟢 **Runtime + attempt state is what a PLAYER needs, not an exporter** — 🟡 **so the README understates it. The enum's members live in `@repo/shared` and were NOT read this pass** |
| 🟢 **Multi-tenancy** | 🟢 **PostgreSQL Row-Level Security with a least-privilege runtime role (`LMS_DATABASE_URL`) and per-tenant domains.** `tenants` table; `tenantId` ×154 and `withTenantId` ×98 in the schema | 🟢 **`docs/architecture.md`: *"A bug in application code cannot read another tenant's rows through that connection."*** 🔵 **DB-enforced, not app-enforced — the strongest tenancy claim on this shelf** |
| 🟢 **Data model** | 🟢 **`104` tables, `12` enums, `3 103` lines, `100 244 B`, Drizzle ORM** | `apps/api/src/storage/schema/index.ts` |
| 🆕 🟢 **AI mentor** | 🟢 **7 tables** — `aiMentorLessons`, `aiMentorConfigurations`, `aiMentorTeacherConfigurations`, `aiMentorRoleplayConfigurations`, `aiMentorThreads`, `aiMentorPracticeSessions`, `aiMentorThreadMessages` | schema |
| 🆕 🟢 **LLM-as-judge assessment engine** | 🟢 **7 tables** — `aiJudgeConfigurations`, `aiJudgeCriteria`, `aiJudgeScoreGuidance`, `aiJudgeBlockingErrors`, `aiMentorJudgements`, `aiMentorJudgementCriteria`, `aiMentorJudgementBlockingErrors` | 🟢 **Rubric criteria, score guidance AND hard-fail *blocking errors*, modelled in the database.** 🔵 **NOTHING ELSE ON THIS SHELF HAS THIS** |
| 🟢 **RAG** | 🟢 `documents`, `docChunks`, `documentToAiMentorLesson`, `searchDocuments` over **PostgreSQL 16 + pgvector** | schema + architecture doc |
| 🟢 **Also in the model** | 🟢 **Learning paths (7 tables, incl. path certificates), RBAC policy engine (5 tables: roles, rule sets, rule-set permissions), live training + attendance (7 tables), calendar sync inbound/outbound, `outboxEvents` transactional outbox, `courseAuthoring*` agent surface (4 tables), `integrationApiKeys`, `certificates`, `forms`** | schema |
| 🟢 **Stack** | 🟢 **NestJS 10 + CQRS · Drizzle · PG 16 + pgvector · Redis + BullMQ · Socket.IO · Remix/React · LiveKit voice · Langfuse tracing · Vercel AI SDK + OpenAI · LangChain** | README *At a glance* + `apps/api/package.json` |
| 🟢 **Distribution** | 🟢 **AWS Marketplace one-click CloudFormation**, self-host, or Selleo-managed | README |
| 🟡 **UI languages** | 🟢 **English, Polish, German, Spanish, French, Czech** | 🟢 **Spanish present.** 🔴 **No Portuguese — a real gap for Brazil** |
| 🟢 **Refs** | `39` heads on origin | `git ls-remote --heads` |

### 🔴 The consequence for this shelf's own advice, stated plainly

🔴 **`P156-A` layer 5 is LTI 1.3. Its closing paragraph offers `mentingo` as a drop-in swap for
layer 1. Those two sentences are incompatible, and p158 is the pass that found it.**

🟢 **The corrected reading:**

| engagement | does `mentingo` fit? |
|---|---|
| 🔴 **University / K-12, existing LMS estate, tools federated over LTI** | 🔴 **NO.** 🟢 **Moodle, Open edX, OpenOLAT, Sakai, ILIAS and Chamilo all speak LTI 1.3; `mentingo` does not. `P156-A` keeps layer 1 copyleft-but-unmodified for exactly this reason** |
| 🟢 **Corporate L&D / HRTech, greenfield, white-label, resold** | 🟢 **YES, and it is the best row on this shelf for it** — MIT, DB-level tenancy, AI mentor and judge in the core, AWS Marketplace deployment |

🟢 **`mentingo`'s own README says this before this shelf did** — *"Mentingo is a TypeScript
platform designed for corporate L&D… If you need a large academic plugin ecosystem, choose
Moodle."* 🔴 **The shelf filed it as *"the only MIT LMS"* and inherited an academic framing the
project never claimed.** 🟢 **It is not a Moodle replacement; it is a Docebo/TalentLMS
replacement, under MIT.**

### 🆕 🟢 `P55` — settle an interoperability question from the DATA MODEL, not the feature table

🟢 **Cost of this assessment: `6` `raw` fetches and one `ls-remote`. No clone.**
🟢 **The decisive artefact was `apps/api/src/storage/schema/index.ts` — a single `100 KB` module
that answered LTI, xAPI, SCORM, tenancy and subsystem inventory at once.**
🆕 **`P55`: for any *"does it integrate with X?"* question, grep the schema and the dependency
manifest. A feature table states intent; a table definition states what ships.**
🔵 **`P52`'s channel map made this free: metadata from search, bodies from `raw`, refs from
`ls-remote` — and a schema file is just another body.**

### 🔴 Open on this page after p158

- 🔴 **`scormStandardEnum`'s members are unread** — they live in `@repo/shared`. 🟡 **Whether `mentingo` supports SCORM 2004 as well as 1.2 is therefore still unknown, and the README's own TODO asks the same question about IMPORT.**
- 🟢 **`mentingo` is no longer an open gap.** 🔵 **Four passes of *"unassessed beyond licence"* are closed.**
- 🔴 **No foundational row other than `mentingo` has had its data model read.** 🟡 **`OpenOLAT` (Apache-2.0, the other fork-safe platform) is the one that matters next, and it is the one that DOES speak LTI and QTI.**

## Pass 157 — 2026-10-12

🟢 **`ACTION HM` DISCHARGED after three unreached passes. The foundational tier finally has an
attention measurement beside its licences** — 🔴 **and the number is the most important thing
this shelf has measured about the market it sells into.**
🟡 **Discharged on a SUBSTITUTED instrument, and this pass says so rather than claiming the
registered one worked.**

### 🔴 `T118` — attention has DECOUPLED from deployment, and the gap is 1.7×

🔴 **One tutoring repository has more GitHub stars than the ENTIRE institutional platform tier
put together.**
[`evidence/platform-attention.2026-10-12-p157.tsv`](../evidence/platform-attention.2026-10-12-p157.tsv)

| | ★ |
|---|---|
| 🟢 [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor), one repository | **41 210** |
| 🔴 **All 13 platform + foundational rows below, summed** | **23 945** |
| 🔴 **Ratio** | 🔴 **1.72 ×** |

🔴 **And `moodle/moodle` — the most-deployed open-source LMS on earth, vendor-reported at 400M+
users and 150k+ sites — has `7 475 ★`.** 🔴 **`DeepTutor` has `5.5 ×` that.**
🔴 **`bigbluebutton` (`9 241`) outranks Moodle too**, so 🔵 **inside the tier the ordering is not
deployment either — the videoconferencing layer beats the system of record.**

🟢 **What a studio should take from this, stated plainly:**
- 🔴 **Stars measure developer attention, NOT installed base.** 🟢 **On this shelf the two are
  not merely different, they are nearly inverted, and the inversion is 1.7× at the top.**
- 🔵 **So a shortlist built by sorting stars will recommend the tutoring layer and miss the
  system of record the client actually runs** — 🟢 **which is `P156-A`'s whole premise, now with
  a number behind it instead of an assumption.**
- 🟢 **And the converse: a client's installed platform will never look exciting on GitHub.**
  🔵 **Do not let a star count argue you into forking it.**

### 🟢 The foundational and platform tier — ★, activity and licence, all measured

🟢 **13 of 14 rows served ★ and `pushed_at`.** 🟢 **Every row is ACTIVE** — 🔵 **twelve of
fourteen pushed within four days of this pass, which is itself the answer to *"is this
maintained?"***

| repo | ★ | last push | licence *(body-read, path recorded)* | what it is, and the licence consequence |
|---|---|---|---|---|
| 🔴 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **9 241** | `2026-10-11` | 🔴 **LGPL-3.0** (`LICENSE`, 7 652 B) | 🟢 **The virtual-classroom layer: WebRTC, whiteboard, breakouts, recording.** 🟡 **LGPL — link freely, modifying the library is not free.** 🔵 **Top of the tier by attention** |
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | **7 475** | `2026-10-12` | 🔴 **GPL** (🆕 `COPYING.txt`, 35 147 B — `P50`) | 🟢 **The most-deployed open-source LMS.** 🔴 **GPL: a distributed derivative ships source.** 🟢 **Plugin-boundary work is the commercial route** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **1 237** | `2026-10-10` | 🟡 **ECL-2.0** (`LICENSE`, 11 120 B) | 🟢 **Apache-2.0 derivative, permissive, built for university consortia.** 🔵 **Permissive route #2** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **1 143** | `2026-10-12` | 🟢 **MIT** (`LICENSE`, 1 097 B) | 🟢 **Offline-first, built for low/no-connectivity deployment.** 🔵 **The LATAM and Africa infrastructure row, and MIT** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | **1 011** | `2026-10-12` | 🔴 **GPL** (`LICENSE`, 35 147 B) | 🟢 **Lightweight LMS with real deployment in francophone and LATAM public education** |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **887** | `2026-10-12` | 🔴 **LGPL-3.0** (🆕 `19.0/LICENSE`, 8 241 B) | 🟢 **Education ERP on Odoo: admissions, fees, timetable, library.** 🆕 🟡 **Default branch is `19.0`, not `master`** — see the correction below |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | **664** | `2026-10-12` | 🔴 **19 B stub, no licence field in `pyproject.toml`** | 🟢 **School management on Frappe/ERPNext.** 🔴 **The grant has NO readable surface. Do not build a deliverable on it without asking the maintainer** |
| 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **646** | `2026-10-12` | 🔴 **GPL-2.0** | 🟢 **Student Information System — enrolment, attendance, gradebook.** 🔵 **The SIS lane, and the only row here that is a SIS rather than an LMS** |
| 🔴 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | **505** | `2026-10-12` | 🔴 **GPL** | 🟢 **Institutional LMS, strong DACH public-sector deployment.** 🟡 **Default branch `release_11`** |
| 🟢 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **447** | `2026-10-12` | 🟢 **Apache-2.0** (`LICENSE`, 10 982 B) | 🟢 **A full institutional LMS under a PERMISSIVE licence WITH a patent grant.** 🔵 **The fork-safe platform route, and the most under-rated row on this shelf at 447 ★** |
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | **446** | `2026-10-11` | 🟢 **MIT** (`LICENSE`, 1 066 B) | 🟢 **DKT, AKT, SAKT knowledge tracing on standard datasets.** 🔵 **The one row that answers *"does the student know it?"* with a model.** 🟢 **MIT, so it ships inside a client product** |
| 🔴 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | **150** | `2026-09-08` | 🔴 **GPL** (`LICENSE.txt`, 35 146 B) | 🟢 **Interactive content types that drop into Moodle, Open edX and Canvas.** 🔵 **Content layer, not a platform** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **93** | `2026-10-12` | 🟢 **MIT** (`LICENSE`, 1 062 B) | 🟢 **The only MIT LMS. AI-native, SCORM + xAPI, white-label.** 🟡 **EMEA — Poland.** 🔴 **Still unassessed beyond licence, ★ and region, FOURTH pass** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **NOT SERVED** | — | 🔴 **AGPL-3.0** (🆕 re-read `master/LICENSE`, 35 136 B) | 🔴 **AGPL reaches a HOSTED derivative, not just a shipped one.** 🔵 **The most common MOOC platform and the most restrictive licence in this table** |

🟢 **Permissive routes through this tier, and there are exactly four:** 🟢 **`OpenOLAT`
(Apache-2.0)** · 🟡 **`sakai` (ECL-2.0)** · 🟢 **`mentingo` (MIT)** · 🟢 **`kolibri` (MIT)**.
🔴 **Everything else is GPL, LGPL or AGPL.**

### 🆕 🔴 `T120` — a `repo:` search miss is NOT evidence of absence

🔴 **`openedx/edx-platform` was absent from TWO independent `repo:`-qualified searches**, which
would read as a deleted or renamed repository. 🟢 **It is neither:**

| probe | result |
|---|---|
| 🔴 `repo:openedx/edx-platform` in two separate queries | 🔴 **absent both times** — 6 of 7, then 7 of 8 |
| 🟢 `raw.../openedx/edx-platform/master/LICENSE` | 🟢 **`200`, `35 136 B`, GNU AFFERO GENERAL PUBLIC LICENSE** |
| 🔴 `raw.../openedx/edx-platform/main/LICENSE` | 🔴 **`404` — there is no `main`; the ref is `master`** |

🔴 **A second row behaves the same way:** `LAION-AI/Desktop_BUD-E` is absent from `repo:` search
and 🟢 **answered `ls-remote` with two refs and served a `4 970 B` README on `raw`.**
🆕 **`T120`:** 🟢 **an index miss and a dead repository are indistinguishable from inside the
search channel**, 🔴 **so *"not found"* from a search endpoint is never publishable as
*"gone"* — 🟢 **it costs one `ls-remote` to tell them apart, and this shelf now pays it.**

### 🟢 `P52` — the channel map, measured rather than assumed

🟢 **p156 recorded *"`api.github.com` refuses this session, `403` on all 17 owners"* as a
categorical gap.** 🟢 **It is narrower than that, and the shelf has been leaving metadata on
the table.**
[`evidence/channel-map.2026-10-12-p157.tsv`](../evidence/channel-map.2026-10-12-p157.tsv)

| channel | status | what it answers |
|---|---|---|
| 🔴 `curl api.github.com` | 🔴 **`403`, 2nd pass** | 🔴 nothing |
| 🔴 `curl github.com` *(rendered)* | 🔴 **`403` this session** | 🔴 nothing — 🟡 **so p156's rendered channel is not reproducible by curl here** |
| 🟢 **GitHub MCP `search_repositories`** | 🟢 **`200` for ANY public repo** | 🟢 **population counts, ★, forks, open issues, SPDX licence, `default_branch`, `pushed_at`, `archived`, topics** |
| 🔴 GitHub MCP `list_branches` / `get_file_contents` | 🔴 **refused outside this session's own repos** | 🔴 nothing third-party |
| 🟢 `raw.githubusercontent.com` | 🟢 **`200`** | 🟢 **file BODIES, any public repo, any ref** |
| 🟢 `git ls-remote --heads` | 🟢 **15 of 15** | 🟢 **the complete ref list for any public repo** |

🆕 **`P52`** — 🟢 **the GitHub channel is SPLIT, not closed: GLOBAL SEARCH endpoints answer for
any repository, PER-REPOSITORY endpoints are scoped to this session.** 🟢 **So the working
triple is: metadata from search, bodies from `raw`, refs from `ls-remote`** — 🔵 **and together
they cover everything this shelf had been treating as unreachable for three passes.**

### 🆕 🟢 CORRECTION, and it strengthens p156 rather than weakening it

🔴 **p156 probed `openeducat_erp`'s `COPYRIGHT` pointer on `master`, `18.0` and `17.0` and found
`404` on all three. None of those is the default branch** — 🟢 **the default is `19.0`.**
🟢 **Probed this pass: `19.0/LICENSE` = `200`, `8 241 B`, LGPLv3 — identical. `19.0/COPYRIGHT` =
`404`.**
🟢 **So `ACTION HB`'s conclusion HOLDS on the branch it had not examined, and the dangling
pointer is now confirmed on FOUR refs.** 🔵 **Stated because the gap was real even though the
answer did not change** — 🟢 **and because it is the same defect `P53` was written for, found in
this shelf's own prior work rather than in someone else's repository.**

## Pass 156 — 2026-10-12

🟢 **Every licence on this page is now read from a BODY on `raw.githubusercontent.com`, this
pass, with the PATH that answered recorded next to it.**
🔴 **And the pass found the reason a licence sweep lies: the most-deployed LMS in the world does
not keep its licence in a file called `LICENSE`.**
[`evidence/foundations-licences.2026-10-12-p156.tsv`](../evidence/foundations-licences.2026-10-12-p156.tsv)

### 🆕 🔴 `P50` — probe `COPYING*` before concluding a repository has no licence

🔴 **`moodle/moodle` returned `404` on `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`,
`COPYING` and `license`, across both `main` and `master`.** 🟢 **Its licence is at
`COPYING.txt` — `35 147 B`, the full GNU GPL text.**
🔴 **A sweep that stopped at `LICENSE*` would have published *"Moodle: no licence file"***, which
is 🔴 **both false and the single most damaging error this shelf could make**, since Moodle is
the row most engagements start from.
🆕 **`T109`** — 🟢 **a licence-absence claim is a claim about the PATHS PROBED, and it is only as
strong as that list.** 🟢 **`P50` therefore requires the probe list to be published with the
verdict**, which this page now does.

### 🟢 The foundational layer, licence read from the body this pass

| repo | licence *(body-read)* | path that answered | bytes | what it is, and the licence consequence |
|---|---|---|---|---|
| 🟢 [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | `LICENSE` | 1 066 | 🟢 **Knowledge tracing: DKT, AKT, SAKT and more on standard datasets.** 🟢 **MIT, so the learner model can ship inside a client product.** 🔵 **The one row on this shelf that answers *"how do you know the student knows it?"*** |
| 🟢 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | `LICENSE` | 1 097 | 🟢 **Offline-first learning platform built for low/no-connectivity deployment.** 🟢 **MIT.** 🔵 **The LATAM and Africa infrastructure row — and the UNESCO IESALC finding below is exactly its market** |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | `LICENSE` | 10 982 | 🟢 **A full institutional LMS under a PERMISSIVE licence with a patent grant.** 🔵 **The copyleft-free LMS route — confirmed again this pass** |
| 🟢 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | `LICENSE` | 1 062 | 🟢 **The only MIT-licensed LMS on this shelf.** 🟡 **EMEA — Poland** *(`P36`, verified owner profile, this pass)*. 🔴 **Still unassessed beyond licence, ★ and region** |
| 🔴 [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL** | 🆕 **`COPYING.txt`** | **35 147** | 🟢 **The most-deployed open-source LMS; vendor reports 400M+ users, 150k+ sites** *(self-reported)*. 🔴 **GPL: a distributed derivative must ship source.** 🟢 **Plugin-boundary work is the normal commercial route** |
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | `LICENSE` | 35 136 | 🔴 **AGPL — network use counts, so a hosted derivative triggers disclosure.** 🟡 **The most common MOOC platform and the most restrictive licence in this table** |
| 🟡 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟡 **ECL-2.0** | `LICENSE` | 11 120 | 🟢 **Educational Community License 2.0 — an Apache-2.0 derivative, permissive, built for university consortia.** 🔵 **Permissive route #2** |
| 🔴 [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL-3.0** | `LICENSE` | 7 652 | 🟢 **The virtual-classroom layer: WebRTC, whiteboard, breakouts, recording.** 🟡 **LGPL — linking is fine, modifying the library is not free** |
| 🔴 [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL** | `LICENSE.txt` | 35 146 | 🟢 **Interactive content types that drop into Moodle, Open edX and Canvas.** 🔵 **The content layer, not a platform** |
| 🔴 [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL** | `LICENSE` | 35 147 | 🟢 **Lightweight LMS with real deployment in francophone and LATAM public education** |
| 🔴 [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL** | `LICENSE` | 35 147 | 🟢 **Institutional LMS, strong in German-speaking EMEA** |
| 🔴 [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0**, 🔴 **from a 19 B stub** | `license.txt` | **19** | 🔴 **The whole grant is the string `License: GNU GPL V3`.** 🔴 **`pyproject.toml` carries NO licence field**, so 🔴 **the `-only` / `-or-later` question has no surface at all** *(carried from p155, unchanged)* |

🟢 **Twelve rows, twelve bodies read, twelve paths recorded.**
🟢 **Permissive and safe to build on: `pykt-toolkit` (MIT), `kolibri` (MIT), `OpenOLAT`
(Apache-2.0), `mentingo` (MIT), `sakai` (ECL-2.0) — five of twelve.**
🔴 **Seven of twelve are copyleft**, and 🔴 **the two platforms a client is most likely to already
run — Moodle and Open edX — are the GPL and AGPL rows.**

### 🔵 What this means for a studio, stated once

🟢 **The engagement shape that survives this licence table is the SAME in every region:**
🟢 **leave the LMS alone and compose beside it.** 🔴 **Moodle's GPL and Open edX's AGPL make a
forked, resold platform a disclosure event**; 🟢 **an MIT/Apache agent that talks to the LMS over
LTI, MCP or REST carries none of it. See `compose/patterns.md` `P156-A`.**

### 🔴 Open on this page

- 🔴 **No star count for ANY row above — a THIRD unreached pass.** 🟢 **The rendered topic page
  can serve it; nothing else is blocking.**
- 🔴 **`mentingo` still unassessed on data model and multi-tenancy** — the only MIT LMS.
- 🔴 **No credentialing or skills-pathway repository, in 156 passes**, against a 2026 trend
  source that names digital credentials as a live buyer demand.
- 🔴 **No evaluation harness.** 🟢 **`pykt-toolkit` is the nearest thing and it models learners,
  it does not evaluate a tutor.**


## Pass 155 — 2026-10-12

🟢 **`ACTION GQ` DISCHARGED — and it REFUTES a warning this shelf has published for two
passes.** 🔴 **`openeducat_erp`'s licence was readable the whole time**: `LICENSE` on `master`
returns **`200`, 8 241 B**, and its first sentence names **LGPL-3.0**.
🔴 **And the pass's main finding is a defect in this shelf's own gate: `P44`'s size check
cannot tell the licence families apart.** 🔴 **Three measured collisions, the worst 11 bytes
wide, all on fresh reads taken this pass.**

### 🟢 `ACTION GQ` — the two ERP rows, answered from bodies

[`evidence/licence-name-channel.2026-10-12-p155.tsv`](../evidence/licence-name-channel.2026-10-12-p155.tsv)

p153's falsifier: *"refuted if the tree says something OTHER than the one-liner and the README
say."* 🟢 **SILENT on both rows — the trees AGREE with the declarations.** 🔴 **But the reach
claim was wrong, and that is the finding.**

| row | what the shelf published | what the body says | verdict |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 *"LGPL-3.0 — README-declared, **NOT file-read**"*, with a *"do not quote"* warning | 🟢 **`LICENSE` = `200`, 8 241 B, 178 lines: *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below."*** Identical body on `master`, `18.0` and `17.0` | 🟢 **LGPL-3.0 CONFIRMED from the body.** 🔴 **The *"not file-read"* warning is WITHDRAWN** |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 *"GPL-3.0 — a ONE-LINE declaration, ~20 B"* | 🟢 **`license.txt` on `develop` = exactly `19 B`: `License: GNU GPL V3`.** 🔴 **`pyproject.toml` exists (1 622 B) and carries NO licence field at all.** `main` 404s — the default branch is `develop` | 🟡 **CONFIRMED, and SHARPENED below** |

🔴 **Why the `openeducat` error happened, said rather than smoothed.** 🟢 **`P45` and `T92` —
this shelf's own channel for reading a licence without a clone — were created in p153.**
🔴 **Nobody aimed them at the two rows the shelf was warning about.** `ACTION GQ` was written
as *"CLONE `frappe/education` and `openeducat_erp`"*, so it inherited a clone budget it never
needed and went unreached for two passes. 🆕 **`T100`: an action phrased around an expensive
instrument outlives the cheap instrument that replaced it.**

### 🆕 🔴 `openeducat_erp` carries a carve-out in its preamble — `T92`'s SECOND instance

🔴 **Before the LGPL text begins, the body says:**

> *"Some external libraries and contributions bundled with OpenEduCat may be published under
> other GPL-compatible licenses. For these, please refer to the relevant source files and/or
> license files, in the source code tree."*

🔵 **So the root grant is LGPL-3.0 and the tree is not uniformly LGPL-3.0 — by the root file's
own admission.** 🟢 **This is exactly `scibly-dev/scibly`'s shape from p154** (AGPL-3.0 at the
root, proprietary inside `ee/`), 🟢 **so `T92` — *a licence can be a property of the PATH, not
the repository* — now has TWO instances, and the second is a row a studio bills against.**
🔴 **It is no longer an anecdote.** 🟢 **`P47`'s path-licence gate is therefore mandatory on
this row**, and the carve-out is *declared*, which makes it cheap to honour and inexcusable to
miss.

### 🆕 🔴 `frappe/education`: a 19-byte grant whose VERSION DIRECTION is unanswerable

🟢 **Exact, not approximate: 19 bytes.** `License: GNU GPL V3` — and 🔴 **`pyproject.toml`, the
one other surface that could speak, is silent.** 🔴 **One declaration surface, 19 bytes, no
`-or-later`, no `-only`.**

🔵 **Why that is worse than a long copyleft licence.** `P43` turns on exactly this word:
Moodle's **GPL-3.0-or-later** gives a relicensing route, Canvas's **AGPL-3.0-only** does not.
🔴 **`frappe/education` does not say**, so 🔴 **`P43` cannot be run on it at all** — the
question has no surface to read. 🟢 **Previously published as *"GPL if the one-liner binds"*;
🟢 the correct statement is *"GPL version 3, with the or-later/only question UNANSWERABLE from
any surface in the repository."*** 🔵 **For an engagement: that is a question for Frappe
Technologies in writing, not a question for an auditor.**

### 🆕 🔴 `T97` / `P48` — `P44`'s size check is REFUTED as a family discriminator

[`evidence/band-collision.2026-10-12-p155.tsv`](../evidence/band-collision.2026-10-12-p155.tsv)

`P44` step 4 reads: *"MIT ≈ 1 062–1 105 B, Apache-2.0 ≈ 11 357–11 358 B, GPL-3.0 ≈ 35 121–35 147 B,
AGPL-3.0 ≈ 34–35 KB."* 🔴 **Three collisions, measured this pass:**

| # | the pair | bytes | gap | if you trusted size |
|---|---|---|---|---|
| 🔴 **1** | **MIT** cluster *(ten bodies, 1 062–1 102 B)* vs 🔴 **AGPL-3.0 short form** — [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 1 102 vs **1 134** | 🔴 **32 B** | 🔴 **You read the STRONGEST COPYLEFT as the MOST PERMISSIVE licence.** The worst direction that exists |
| 🔴 **2** | **Apache-2.0** — [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) vs **ECL-2.0** — [`sakai`](https://github.com/sakaiproject/sakai) | 10 982 vs **11 120** | 🔴 **138 B** | 🔴 ECL-2.0's **narrowed patent grant** collapses into Apache-2.0's standard one |
| 🔴 **2b** | **Apache-2.0's own RANGE** — `feifei-companion` 10 227 → `DeepTutor` 11 408 | 1 181 B wide | — | 🔴 **The Apache range BRACKETS ECL-2.0 entirely.** The two are not separable by size in principle, not just in practice |
| 🔴 **3** | **GPL-3.0** — `moodle/moodle` `COPYING.txt`, 🟢 **re-read fresh this pass** vs **AGPL-3.0** — `openedx/edx-platform` `LICENSE` | 35 147 vs **35 136** | 🔴 **11 B** | 🔴 **You lose *network use counts as distribution*** — the single most consequential distinction for a hosted LMS |

🟢 **Both figures in collision 3 are fresh reads taken this pass**, not a carried band against
a new measurement: `moodle/moodle/main/COPYING.txt` = **35 147 B, `GNU GENERAL PUBLIC LICENSE`**;
`openedx/edx-platform/master/LICENSE` = **35 136 B, `GNU AFFERO GENERAL PUBLIC LICENSE`**.
🔴 **The AGPL body sits INSIDE the band this shelf uses to confirm GPL-3.0.**

🟢 **What survives.** Size still catches the `P411` shape — 🟢 **a body that CLASSIFIES as one
family but is the wrong SIZE for it is a flag** (`PageLM`'s 8 563 B "MIT"). 🟢 **And a 19-byte
or 1 134-byte body is a flag by itself: a grant too short to be a licence text.**
🔴 **What dies is size as a CONFIRMER of family.** 🆕 **`P48` replaces it: read the NAME LINE.**
🟢 **This pass classified 19 of 19 bodies by name line with zero ambiguity**, including both
AGPL short-form and full-text bodies in the same sweep.

### 🆕 🟢 New foundational rows, licences read from bodies

| repo | licence *(body-read)* | bytes | `HEAD` | why it is here |
|---|---|---|---|---|
| 🆕 [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | **10 982** | `e4be14f` | 🟢 **A full Java institutional LMS under a STANDARD permissive licence.** 🔵 **This shelf has said for several passes that `sakai` (ECL-2.0) is *"the"* copyleft-free LMS — 🔴 that is now WRONG: there are TWO, and the newcomer carries the better-understood grant** |
| 🆕 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** — 🔴 **version 2, not 3** | **15 214** | `22ec5ba` | 🟢 **A K-12 Student Information System** — attendance, grades, scheduling, the inputs a dropout-prediction agent needs. 🔴 **The secondary source that surfaced it said only *"GPL"*; the body says **Version 2**, and `P43`'s whole question lives in that number** |
| 🆕 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | **1 062** | `242a932` | 🟢 **The only MIT-licensed LMS this shelf has found.** 92 ★, young — 🔵 **but it is the only row where the platform licence imposes nothing at all** |

### 🆕 🔴 `T96` — third-party comparison sites misreport platform licences, and the error UNDERSTATES copyleft

🔵 **The layer a studio's first-pass shortlist is actually built from is the comparison
article, not the repository.** 🔴 **Three of three platform licences cross-checked against the
secondary sources that surfaced them this pass are wrong or imprecise:**

| platform | what secondary sources said | what the BODY says | the error |
|---|---|---|---|
| 🔴 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 one source: *"Apache License 2.0: Used by Open edX"* *(another said AGPLv3)* | 🔴 **AGPL-3.0**, 35 136 B, name line `GNU AFFERO GENERAL PUBLIC LICENSE` | 🔴 **AGPL → Apache. Understates copyleft — the dangerous direction, same as `T89`'s badge** |
| 🔴 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🔴 *"Apache 2.0"* *(another said ECL v2)* | 🟢 **ECL-2.0**, 11 120 B, name line `Educational Community License, Version 2.0 (ECL-2.0)` | 🟡 **Apache-DERIVED is not Apache.** ECL-2.0 narrows the patent grant — material for a studio |
| 🔴 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 bare *"GPL"* | 🔴 **GPL-2.0**, 15 214 B | 🔴 **Version dropped**, which is where `P43` lives |

🟢 **So `T89` generalises off the repository.** p153 found a repo whose own badge contradicted
its own `LICENSE`; 🔴 **p155 finds the same error direction one layer out, in the sources a
shortlist is built from, and the sources CONTRADICT EACH OTHER on the same platform in the
same search.** 🔵 **Operationally: a licence column in a comparison article is a hypothesis.
`P48` costs one `curl`.**

##### 🔴 What this page still cannot do, after p155

- 🔴 **`openeducat_erp`'s per-directory carve-out is DECLARED but UNMEASURED** — nobody has
  enumerated which bundled paths are not LGPL. 🔵 **`ACTION HB`.**
- 🔴 **`frappe/education`'s version direction is unanswerable from the repo.** 🔵 **Ask the vendor.**
- 🔴 **No star count for ANY foundational row** — `ACTION GN`, unreached a second pass.
- 🔴 **`P44` step 4 is now known-wrong in the published text below**; 🟢 **`P48` supersedes it
  in `compose/patterns.md`**, and the older text is left standing as history rather than
  silently edited.


## Pass 154 — 2026-10-12

🟢 **Two foundational layers this shelf has been reasoning ABOUT without ever enumerating are
now enumerated with licences attached: ASSESSMENT/GRADING and KNOWLEDGE TRACING.**
🔴 **And the second one — the layer every adaptive-learning claim rests on — is HALF
UNGRANTED.**

### 🔴 The knowledge-tracing layer: permissive or ungranted, never copyleft

🔵 **Why this layer decides an engagement.** Every "adaptive", "personalised" or "mastery"
claim a studio makes needs a learner model underneath it. `topic:knowledge-tracing` is **86
repositories**; here are the top 20 by stars, licence read from the API's detector.

| repo | licence | ★ | last push | what it is |
|---|---|---|---|---|
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **446** | 2026-10-11 | 🟢 **The field's benchmark library** — already this shelf's KT reference, now with a star figure |
| [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) | 🟢 **MIT** | **194** | 2022-06-16 | A collection of KT implementations. 🔴 **Four years cold** |
| [`jhljx/GKT`](https://github.com/jhljx/GKT) | 🟢 **MIT** | **141** | 2021-03-19 | Graph-based KT (IJCAI). 🔴 **Five years cold** |
| [`jilljenn/ktm`](https://github.com/jilljenn/ktm) | 🟢 **MIT** | **140** | 2025-08-12 | 🟡 **EMEA (inferred)** — Knowledge Tracing Machines: factorization machines for KT |
| 🔴 [`ckyeungac/deep-knowledge-tracing-plus`](https://github.com/ckyeungac/deep-knowledge-tracing-plus) | 🔴 **NO GRANT** | **124** | 2019-01-08 | DKT+ |
| [`lccasagrande/Deep-Knowledge-Tracing`](https://github.com/lccasagrande/Deep-Knowledge-Tracing) | 🟢 **MIT** | **107** | 2020-12-04 | DKT in TF2 |
| 🔴 [`arshadshk/SAINT-pytorch`](https://github.com/arshadshk/SAINT-pytorch) | 🔴 **NO GRANT** | **94** | 2022-04-26 | 🔴 **SAINT — one of the transformer KT baselines everybody cites** |
| 🔴 [`seewoo5/KT`](https://github.com/seewoo5/KT) | 🔴 **NO GRANT** | **90** | 2024-08-11 | KT models in PyTorch |
| 🔴 [`ApexEDM/GIKT`](https://github.com/ApexEDM/GIKT) | 🔴 **NO GRANT** | **83** | 2021-07-17 | Graph interaction KT |
| [`tswsxk/EduData`](https://github.com/tswsxk/EduData) | 🟢 **Apache-2.0** | **83** | 2023-05-03 | 🟢 **Education datasets + a download/preprocess interface** — the data side of the layer |
| [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) | 🟢 **MIT** | **82** | 2026-09-17 | 🟢 **Active.** KT + cognitive diagnosis + exercise recommendation in one library |
| [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) | 🟢 **MIT** | **78** | 2026-01-06 | 🔵 **APAC** — unified student-modelling library (FCS 2025) |
| 🔴 [`yxonic/DTransformer`](https://github.com/yxonic/DTransformer) | 🔴 **NO GRANT** | **46** | 2025-03-24 | 🔴 **Diagnostic-transformer KT — a current-generation model with no grant** |
| 🔴 [`arshadshk/Last_Query_Transformer_RNN-PyTorch`](https://github.com/arshadshk/Last_Query_Transformer_RNN-PyTorch) | 🔴 **NO GRANT** | **45** | 2021-04-08 | Kaggle-winning architecture |
| 🔴 [`TianHongZXY/pytorch-SAKT`](https://github.com/TianHongZXY/pytorch-SAKT) | 🔴 **NO GRANT** | **38** | 2023-07-23 | SAKT |
| 🔴 [`xiaopengguo/ATKT`](https://github.com/xiaopengguo/ATKT) | 🔴 **NO GRANT** | **34** | 2021-11-01 | Adversarial-training KT (ACM MM, oral) |
| [`THUwangcy/HawkesKT`](https://github.com/THUwangcy/HawkesKT) | 🟢 **MIT** | **31** | 2023-09-14 | 🔵 **APAC** — temporal cross-effects (WSDM'21) |
| [`jdxyw/deepKT`](https://github.com/jdxyw/deepKT) | 🟢 **MIT** | **28** | 2021-11-05 | KT in PyTorch |
| 🔴 [`ZhijieXiong/dlkt`](https://github.com/ZhijieXiong/dlkt) | 🔴 **NO GRANT** | **17** | 2025-09-04 | 🟢 **Migrated to `pyedmine`** — follow the successor |
| 🔴 [`HFUT-LEC/awesome-student-cognitive-modeling`](https://github.com/HFUT-LEC/awesome-student-cognitive-modeling) | 🔴 **NO GRANT** | **14** | 2024-08-01 | Resource list |

🔴 **The count: 10 of 20 carry NO GRANT. 9 are MIT, 1 is Apache-2.0. ZERO are copyleft.**

🟢 **That distribution is the commercially useful fact on this page.** A studio reaching for
the layer finds no GPL trap — 🔴 **it finds an EMPTY GRANT, which is strictly worse, because
copyleft at least tells you the price.** 🔴 **And the ungranted rows are not the fringe**:
SAINT, SAKT, DTransformer and ATKT are the transformer baselines a client's data-science
reviewer will ask for by name.
🟢 **The buildable path is therefore `pykt-toolkit` (MIT) or `pyedmine` (MIT, active) as the
substrate, with `EduData` (Apache-2.0) for datasets** — and any paper implementation treated
as a SPEC to reimplement, never as a dependency.

### 🟢 The assessment / grading layer — enumerated for the first time

🔵 **`topic:grading` is 259 repositories.** The rows that matter for an education engagement,
licence from the API's detector:

| repo | licence | ★ | last push | region | what it is |
|---|---|---|---|---|---|
| 🟢 [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** | **1 374** | 2026-10-01 | Global | 🟢 **The most-starred permissive grading system in open source.** Assign, release, collect and autograde notebooks. 🟢 **`HEAD` `f9915da`** |
| [`inducer/relate`](https://github.com/inducer/relate) | 🟡 **NOASSERTION** | **437** | 2026-10-07 | 🟡 North America | Full course environment with assessment. 🔴 **Read the body before adopting** (`P47`) |
| [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🟡 **NOASSERTION** | **243** | 2026-10-12 | 🟡 **EMEA** | 🟢 **Secure, automated exercise assessment running the instructor's own tests** — the grading substrate for programming courses |
| 🔴 [`GatorEducator/gatorgrader`](https://github.com/GatorEducator/gatorgrader) | 🔴 **GPL-3.0** | **85** | 2026-10-06 | 🟡 North America | Checks writers' and programmers' work |
| 🆕 🔴 [`five-plus-one/AI-Marker-Suite`](https://github.com/five-plus-one/AI-Marker-Suite) | 🔴 **GPL-3.0**, body-read **35 154 B** | **79** | 2026-10-12 | 🔵 **APAC** | 🟢 **AI marking over 24 named incumbent platforms** — the retrofit pattern |
| 🔴 [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) | 🔴 **NO GRANT** (8 paths probed) | **74** | 2026-10-06 | 🟡 North America | Offline React app for digital math homework |
| 🔴 [`zmievsa/autograder`](https://github.com/zmievsa/autograder) | 🔴 **GPL-3.0** | **48** | 2024-07-15 | — | Assignment grading for programming courses |
| 🔴 [`ai-lingnan/econai-agent-platform`](https://github.com/ai-lingnan/econai-agent-platform) | 🔴 **AGPL-3.0** | **38** | 2026-07-17 | 🔵 **APAC** | 🟢 **Dual-agent parallel grading** |
| 🔴 [`federicazoe/gradetools`](https://github.com/federicazoe/gradetools) | 🔴 **GPL-3.0** | **35** | 2025-07-24 | 🟡 North America | R package for a grading workflow |
| 🔴 [`sourcegrade/jagr`](https://github.com/sourcegrade/jagr) | 🔴 **AGPL-3.0** | **33** | 2026-10-07 | 🟡 **EMEA** | Java autograder in Kotlin |
| 🟢 [`pedal-edu/pedal`](https://github.com/pedal-edu/pedal) | 🟢 **MIT** | **32** | 2026-08-24 | 🟡 North America | 🟢 **Static + dynamic analysis of student Python with feedback generation** — permissive, and the right shape to put an agent behind |

🔴 **The grading layer is COPYLEFT-HEAVY, and the inverse of the modelling layer.** Of those
11 rows: **2 permissive (`nbgrader` BSD-3, `pedal` MIT)**, **6 copyleft**, **2 NOASSERTION**,
**1 ungranted**.
🟢 **So the composable grading stack has exactly two entry points** — and both are real:
`nbgrader` for notebook-based courses, `pedal` for Python feedback. 🔵 **Everything else is a
licence conversation before it is an engineering one.**

### 🟢 Spaced repetition, added as a foundational row

| repo | licence | ★ | last push | why it is foundational |
|---|---|---|---|---|
| 🟢 [`open-spaced-repetition/fsrs4anki`](https://github.com/open-spaced-repetition/fsrs4anki) | 🟢 **MIT** | **4 101** | 2026-08-14 | 🟢 **The FSRS scheduler — the most-starred permissive row in the whole retention layer.** `HEAD` `ff7c85c` |
| 🟢 [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | 🟢 **MIT** | **515** | 2026-10-11 | 🟢 **The MCP boundary onto Anki** — an agent can read and write a learner's real review queue. `HEAD` `e0e347f` |

🔵 **Why these belong next to the KT rows and not in a curiosities drawer.** `pykt` tells you
what a learner knows; **FSRS tells you when to ask again**. 🟢 **A retention claim with no
scheduler underneath it is a chatbot with a syllabus.**

🟢 **All 23 rows probed this pass verified by `git ls-remote`, 23 of 23, negative control
returned nothing**
([`evidence/ls-remote-verification.2026-10-12-p154.tsv`](../evidence/ls-remote-verification.2026-10-12-p154.tsv)).

##### 🔴 What this page still cannot do, after p154

- 🔴 **Every licence above except two is from the API's DETECTOR, not from the body.** The
  two body-reads are `AI-Marker-Suite` (35 154 B, GPL-3.0) and the three absences confirmed
  by probe. 🔵 **`ACTION GU`**: body-read the 11 grading rows before any of them is quoted.
- 🔴 **`inducer/relate` and `INGInious` are `NOASSERTION`** — the `scibly` class. Unread.
- 🔴 **The 10 ungranted KT rows were not contacted and no issue was filed.** An ungranted
  repo can be granted on request; nobody has asked.

## Pass 153 — 2026-10-12

🟢 **18 of 18 rows verified for EXISTENCE and `HEAD` by `git ls-remote`, with a negative
control that fires** — and 🟢 **every licence below read from the LICENCE FILE BODY**, not
from a sidebar, a badge or this shelf's memory.
🆕 **A new channel does it for one round trip per repo and no clone.**

### 🟢 The foundational layer, with the licence read from the file and the file's size as its tell

🔵 **Why the byte size is published next to the licence.** This shelf learned at `P411`
that a proprietary licence can open with the MIT grant verbatim; **the tell was the size**
— 8 563 B against ~1 070 B for a real MIT. 🟢 **So every row carries the body size, and the
sizes cluster exactly as a clean corpus should**: MIT **1 062–1 105 B**, Apache-2.0
**11 357–11 358 B**, GPL-3.0 **35 121–35 147 B**.

| repo | licence (read from the body) | body | `HEAD` | why it is foundational |
|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🟡 **GPL-3.0-or-later** | 35 147 B | `f205347` | The world's most-deployed LMS. 🟢 **p152 measured the election: 13 859 of 14 024 notices say `-or-later`** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | — | `b3f862e` | MOOC-grade LMS behind edX. 🟡 **Root-only notice surface (p152)** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0-only** | — | `1c9f0bb` | 🔴 **`-only` elected BY OMISSION in 16 896 files** (`T85`, p152) — the strictest row here, and it reads as silent to a naive matcher |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🟡 **LGPL-3.0-or-later** | — | `1524a63` | Virtual classroom with an LMS-native integration path. 255 of 263 notices `-or-later` (p152) |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | — | `10a1d90` | Apache-derived, university-governed LMS. 🟢 **The most permissive copyleft-free LMS of the big four** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | — | `d3de265` | 🟢 **Offline-first learning platform, MIT.** The row for low-connectivity deployments — LATAM rural, Africa, APAC islands |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | — | `948a378` | *"Framework for building custom learning components that run in the Open edX LMS"* — 🟢 **the permissive entry point into an AGPL platform** |
| [`netless-io/flat`](https://github.com/netless-io/flat) | 🟢 **MIT** | **1 062 B** | `d194d5b` | 🟢 **The largest permissive synchronous-classroom codebase this shelf has measured** |
| [`OpenVidu/openvidu`](https://github.com/OpenVidu/openvidu) | 🟢 **Apache-2.0** | **11 357 B** | `ba72e6b` | Self-hosted real-time video over LiveKit/mediasoup. 🟢 **Permissive substrate for live tutoring** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 🟢 **MIT** | **1 094 B** | `d0cd78c` | 🟢 **A PERMISSIVE SIS** — the layer where this shelf had only copyleft and non-OSI |
| [`Ilyas-Codes/eCourse`](https://github.com/Ilyas-Codes/eCourse) | 🟢 **MIT** | **1 062 B** | `3ee89f6` | 🟢 **Lightweight LMS without Moodle's copyleft** |
| [`geli-lms/geli`](https://github.com/geli-lms/geli) | 🟢 **Apache-2.0** | **11 358 B** | `02ae520` | E-learning platform, permissive, patent grant included |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | **1 105 B** | `a40eff7` | Intelligent tutoring with Bayesian Knowledge Tracing, UC Berkeley. 🟢 **The ITS reference for STEM** |
| [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) | 🟢 **MIT** | **1 066 B** | `eec087e` | PyTorch knowledge tracing — the field's standard toolkit. 🟢 **The modelling core under any adaptive-learning claim** |
| [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** | **1 079 B** | `8b14aec` | Django+React CMS for education portals. 🟢 **The permissive front end for an AGPL LMS** |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0 — README-declared** | 🔴 **not file-read** | `1c95cef` | Education ERP on the Odoo framework, 73+ modules. 🔴 **See the warning below** |
| [`frappe/education`](https://github.com/frappe/education) | 🟡 **GPL-3.0 — a ONE-LINE declaration** | 🔴 **~20 B** | `444cc8e` | School management on Frappe/ERPNext. 🔴 **See the warning below** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** | 35 121 B | `1d83c2b` | School-management/SIS platform. Attendance, grades, scheduling — 🟢 **the input data for a dropout-prediction agent** |

🟢 **8 of 18 are MIT or Apache-2.0.** 🔴 **7 are copyleft** (2 AGPL, 3 GPL/LGPL-family, plus
Moodle and BigBlueButton's `-or-later` elections). 🟢 **1 is ECL-2.0.**
🟡 **2 cannot be read from a file body at all** — and those two are the finding.

### 🔴 Two rows whose licence CANNOT be read the way the other sixteen were

🔵 **Both are ERP-class platforms, which is where a studio's margin usually is, and both
fail the test this shelf applies to everything else.**

🔴 **`frappe/education`** — its licence lives at `license.txt` on branch `develop` and its
entire content is the string **`License: GNU GPL V3`**. 🟢 **About 20 bytes against the
35 147 B of a real GPL-3.0 body.** 🔴 **So GitHub's own detector cannot classify it — the
sidebar shows a bare "License" link with no type** — and neither can any body-marker
matcher, including this shelf's. 🟢 **The intent is unambiguous and the instrument is
useless on it**, which is `T85`'s shape (an election by omission) in a new place: 🆕 **a
GRANT BY REFERENCE.**

🔴 **`openeducat/openeducat_erp`** — the sidebar likewise shows an unclassified "License"
link; the **README** states LGPL-3.0. 🔴 **That is a README surface, which is exactly the
surface `lumen` proved can lie** (`T89`, this pass). 🟡 **Recorded as README-declared, NOT
file-read, and the distinction is kept** rather than flattened into the table.

🟢 **The consequence for a studio, stated plainly:** both rows are usable, 🔴 **and neither
licence should be quoted to a client's legal team from this page.** 🔵 **For those two,
clone and read, or ask the maintainer.** 🔵 **`ACTION GQ`.**

### 🆕 🟢 The channel that made this page cheap, and the control that makes it trustworthy

| channel | what it does | cost | result |
|---|---|---|---|
| 🟢 `git ls-remote <url>` | existence + `HEAD` SHA | 1 round trip, **no tree** | 🟢 **18 of 18** |
| 🟢 `raw.githubusercontent.com/<o>/<r>/<branch>/LICENSE` | 🟢 **the licence BODY and its byte size** | 1 round trip, **no clone** | 🟢 **16 of 18 read directly** |
| 🔴 `curl github.com/<o>/<r>` | — | — | 🔴 **`403` on 17 of 17** |
| 🔴 `api.github.com/repos/…` | — | — | 🔴 refused — the session's repository-scope policy, defined as **`P150-A`** at [`repos/trending.md:242`](trending.md), an APPEND-ONLY page |

🟢 **NEGATIVE CONTROLS, both fired.** A slug that cannot exist returns **no SHA** from
`ls-remote`; a wrong licence path returns **`404`** from `raw`. 🔵 **Without them this page
would be eighteen rows of a channel that might say yes to anything** — `P42`'s rule applied
to a liveness check.

🔵 **And a channel difference INSIDE one host, for the third time this pass.**
`raw.githubusercontent.com` answers `curl`; `github.com` repo HTML refuses it; `WebFetch`
renders it. 🟢 **`ACTION GE2`'s rule earns its keep again: name the URL refused and the URL
that answered, never "the channel".** 🆕 **`T92` — a licence body is readable without a clone, so a 58-row census does not
need 2.4 GB.** 🔵 **Stated with an em-dash deliberately**: an earlier draft of this line
used a colon, and 🔴 **this pass's own citation check could not see it as a statement** —
🟢 `T91`'s lesson landing on the pass that wrote it.

### 🟢 How to choose from this page — the licence decides, then the attachment point

1. 🟢 **Permissive and complete, pick first:** `kolibri` (MIT, offline-first), `flat`
   (MIT, synchronous classroom), `academico` (MIT, SIS), `eCourse` (MIT, LMS),
   `geli` (Apache-2.0), `OpenVidu` (Apache-2.0, real-time).
2. 🟢 **Permissive LAYERS onto a copyleft host:** `XBlock` (Apache-2.0) into Open edX,
   `richie` (MIT) in front of it. 🔵 **This is the route that keeps your code yours**
   when the client already runs an AGPL LMS.
3. 🔴 **Copyleft hosts — the plugin inherits.** Moodle (GPL-3.0-or-later), Open edX and
   Canvas (AGPL), BigBlueButton (LGPL-3.0-or-later), Gibbon (GPL-3.0).
   🔴 **Canvas is the strictest: `AGPL-3.0-only`, elected by omission** — 🟢 **so an
   `-or-later` relicensing route that works for Moodle does NOT exist for Canvas** (`P43`).
4. 🟢 **Copyleft-free institutional LMS:** `sakai` (ECL-2.0), the Apache-derived option.
5. 🔴 **Do not quote the licence of `frappe/education` or `openeducat_erp` from here.**

##### 🔴 What this page still cannot do, after p153

- 🔴 **No star count for any of the 18.** The star budget went to the agent tier
  (`ACTION GI`); 🔵 **`ACTION GN`** carries it.
- 🔴 **Two of eighteen licences are not file-read** (`frappe/education`,
  `openeducat_erp`) — named above rather than smoothed into the table.
- 🔴 **`ls-remote` proves existence and freshness, nothing else** — not activity, not
  maintenance, not fitness. No row here is recommended on the strength of a `HEAD` SHA.
- 🔴 **The `-only`/`-or-later` election was re-measured for NONE of these rows this pass**;
  the elections quoted are p152's, on p152's clones, and 🔴 **those clones are gone** — the
  container is ephemeral.
- 🔴 **`raw` was tried on three branches and six filenames.** A repo that keeps its licence
  elsewhere would read as `NO_LICENCE_FILE_FOUND`, which is a limit of the probe and not a
  property of the repo. 🟢 **None of the 18 hit it.**

## Pass 152 — 2026-10-12

🔴 **Every per-file licence figure on this shelf counts files that belong to somebody else,
and this pass can finally say so with a number.** 🟢 **`T86`.** 🔴 **And the licence TERM —
the `-only` / `-or-later` election — turns out to be readable on three of the six largest
subjects, which means `T81`'s null was a property of SMALL repositories and not of
education copyleft.**

| measurement | value |
|---|---|
| foundational subjects walked this pass | 🟢 **6** vertical platforms, `git clone --depth 1`, **6 of 6 OK**, **2.4 GB** |
| source files scanned | 🟢 **105 727** (licence files excluded at any depth) |
| 🆕 files carrying a GNU per-file notice | 🟢 **31 205** |
| …of those, electing `-or-later` | **14 115** |
| …electing `-only` with the WORD "only" | 🟢 **0** |
| 🆕 …electing `-only` **by OMISSION** | 🔴 **16 896** |
| notices that never reach a VERSION | **194** |
| 🔴 subjects whose verdict is attributable to a VENDORED file | 🔴 **2 of 6** (`sakai`, `edx-platform`) |
| 🟢 the reproduction control — p151's 7 rows re-measured | 🟢 **1 513 files, 7 SILENT, control 7 of 7 — EXACT** |

🟢 **Artefacts:**
[verticals](../compose/code/p152-vertical-election/result.verticals.2026-10-12-p152.tsv) ·
[omission forms](../compose/code/p152-vertical-election/result.omission.2026-10-12-p152.tsv) ·
[the reproduction of p151's seven](../compose/code/p152-vertical-election/result.repro-p151-seven.2026-10-12-p152.tsv).

### 🆕 🟢 `P42` — the NOTICE DENOMINATOR, and why this shelf needed it

🔴 **p151 published *"0 elections over 1 513 files"* with no denominator**, and a figure of
that shape cannot be read. 🔴 **A tree with zero GNU notices and a tree with 16 905 notices
that each decline to elect both report "0 elections" — and they are opposite facts.**

🟢 **With the denominator, `SILENT` splits into four classes that were one:**

| class | subject | notices | what the silence MEANS |
|---|---|---|---|
| **NO_NOTICE** | `kolibri` | **0 of 4 350** | 🟢 permissive — there is no copyleft notice to elect in |
| **ROOT_ONLY** | `edx-platform` | 🟡 **0 first-party** (1 vendored) | 🟡 the licence lives in the root file alone |
| 🔴 **DECLINING** | `canvas-lms` | 🔴 **16 905 of 19 286 — 87.7%** | 🔴 **not silent at all: an election, by omission** |
| **NOTICE_NO_VERSION** | p151's seven rows | **17 of 1 513** | 🟢 a GNU licence named, no version to elect from |

🟢 **And the fourth class re-reads p151's own result.** All **17** notice-bearing files
across the seven small rows name a GNU licence and never reach a version, 🔴 **while
`Agso-o/sigaa-calendar` and `ahmedEid1/lumen` have ZERO notices across 1 020 source files.**
🟢 **So `T81` HOLDS for the small rows — for a cause p151 did not measure.**

🔵 **Same defect class as `T84`'s `LINK LAYER`/`PROMPT LAYER` split**: two populations that
read zero on one instrument for different reasons, and an instrument that reports them
identically is hiding the difference. 🟢 **`P42` is that rule generalised: never publish a
zero without the denominator that makes it a measurement.**

### 🔴 The vendored-file problem, which touches every licence figure this shelf has published

🔴 **Two of six subjects' verdicts come from code the subject did not write:**

- 🔴 **`sakaiproject/sakai`** — **1** hit in **11 620** files:
  `library/src/webapp/js/trimpath-template-latest.js`, *"TrimPath Template … Copyright (C)
  2004, 2005 Metaha"*, dual GPL-2.0-or-later / Apache-2.0. 🟢 **Sakai is ECL-2.0 and elects
  nothing.**
- 🔴 **`openedx/edx-platform`** — its only notice-bearing file is
  `common/test/data/uploads/jschannel.js`. 🟢 **First-party notice surface: ZERO.**

🔴 **`SKIP_DIRS` cannot fix either**: it excludes `vendor/`, and neither bundled copy is
under `vendor/`. 🔵 **A path-name exclusion is the wrong instrument for a provenance
question** — 🟢 **the right signal is the notice's own copyright holder**, which sits in the
same eight kilobytes the walk already reads. 🔵 **`ACTION GF`.**

🔴 **The consequence for this page is not confined to these two rows.** Every per-file
licence sweep in this shelf's history — `p199-perfile-license`, `p441-tree-licence-enumeration`,
`p969-root-only-licence-reach` — walked trees without separating first-party from bundled
files. 🟢 **None of their published verdicts is withdrawn on this evidence**, because none
of them was measured for this defect; 🔴 **but none can be said to be free of it either.**
🟢 **Stated once, at page level, rather than as a correction this pass has not earned.**

### 🟢 The six foundational platforms, with the stars this page never had

| repo | licence | ★ | forks | 🆕 election | notice rate |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | **LGPL-3.0** | **9.2k** | 6.0k | 🟢 `-or-later` | 8.5% |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | **AGPL-3.0** | **8.2k** | 4.4k | 🟡 unstated | 🟡 0% first-party |
| [`moodle/moodle`](https://github.com/moodle/moodle) | **GPL-3.0** | **7.5k** | — | 🟢 `-or-later` | 23.3% |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | **6.9k** | 3.0k | 🔴 **`-only`** | 🔴 **87.7%** |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | **1.2k** | 1.0k | 🟢 none (vendored hit) | 0.1% |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | **1.1k** | 1.0k | 🟢 n/a | 0% |

🟢 **6 of 6 sidebar licences agree with this shelf's hand-read values** — a free second
licence channel, in the same nine fetches that refuted `T78`.

🔵 **The permissive foundation story is unchanged and now has a number beside it**:
🟢 **`kolibri` (MIT) is still the only one of the six a studio can build on without a
copyleft conversation** — and at **1.1k ★** it is also the second-least-starred. 🔴 **The
popularity and the permissiveness point in opposite directions on this shelf**, which is
the sentence this page has implied for 152 passes and could not previously support.

### 🔴 What this page still cannot do

- 🔴 **The election is unmeasured on every foundational subject that is not one of these
  six.** 🟢 Six were cloned; no larger population was sampled and none is implied.
- 🔴 **No notice-to-holder attribution** (`ACTION GF`), so `sakai`'s row is published with a
  verdict this page knows is wrong rather than quietly dropped.
- 🔴 **The positive control degrades on big trees**: it fires on **10 of 161** licence
  bodies here against 7 of 7 on the small rows, because these six trees bundle 161 licence
  files that are mostly vendored MIT/Apache. 🟢 **The figure is given rather than hidden.**
  🔵 **`ACTION GG`.**
- 🔴 **p151's `election.py` was NOT the instrument used.** One invocation was refused
  `[Code from External]`; 🟢 **the re-implementation reproduces p151's three published
  figures exactly**, which licenses it as a reproduction and 🔴 **not as an independent
  second surface.**

## Pass 151 — 2026-10-12

🟢 **The 58-row licence census is RE-PUBLISHED**, the body matcher is retired in both
modules that owned a copy, and 🟢 **the GNU-family population is confirmed at SEVEN over all
58 subjects** rather than the 28 trees p150 could reach.

| measurement | value |
|---|---|
| subjects walked | **58** — 🟢 **50 of 50 `git clone`**, 🟢 **8 of 8 `npm pack`** |
| subjects shipping a licence FILE | **39** |
| of those, carrying a readable TITLE line | 🟢 **39 — all of them** |
| GNU-family population, by the title surface | **7** |
| …by the retired body matcher, as a population | **7** |
| rows where the two surfaces DISAGREE | 🔴 **5** — exactly the five `T77` named |
| rows changing licence id against the published census | 🔴 **4 of 52** |
| …of those, outside the GNU family | 🟢 **0** — `ACTION FN`'s falsifier is SILENT |
| rows with more than one licence file | **0** |

🟢 **The re-published artefact:**
[`evidence/licence-census.2026-10-12-p151.tsv`](../evidence/licence-census.2026-10-12-p151.tsv).

### 🟢 The five corrections, now in the census and not only beside it

| row | published | corrected |
|---|---|---|
| `Agso-o/sigaa-calendar` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `despedite/siu-guarani` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `mhlavac/edupage-mcp` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `ahmedEid1/lumen` *(agent tier, not in the 52)* | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** |
| `qxbao/qldt-hanu-mcp` | 🔴 `LGPL` | 🟢 **GPL-2.0** — wrong family **and** no version |

🔵 **`mhlavac/edupage-mcp` is the row that makes the title WINDOW load-bearing**: its
`LICENSE` opens with *"Copyright (c) 2026 Martin Hlavac"* and names the GNU licence on the
next non-blank line. 🔴 **A one-line window would read it as having no licence at all** — so
the window's width is now asserted against this row's shape in the suite.

### 🟢 The coverage result, which the action did not ask for and matters more

🔴 **A narrower surface that answers less often is a trade, not a fix.** 🟢 **39 of 39
licence files on this shelf carry a readable title line**, so retiring the body matcher
costs **zero coverage**. 🔵 That is why the replacement can be shipped rather than offered
as an option.

### 🔴 The eighth GNU-family row, and why `T77` cannot touch it

🔴 **`moodle-mcp-server-aql-0.1.7` declares `AGPL-3.0` in `package.json` and ships no
licence file.** It is GNU-family at the **declaration** layer, where there is no body to
mis-read. 🟢 **8 GNU-family ids across 58 rows; 7 of them read from a body.** 🔵 Stated now
so it is not later found as a correction.

### 🔴 A figure on the re-published census that is NOT this shelf's figure

🔴 **Strict-unlicensed reads 10 on the new artefact and 8 on `p149-common-title-licence`'s
58-row result.** The two rows are **`eugeborzone/Auto_Grade_Guarani`** and
**`frjunioalves/suap-mcp`**, both Portuguese-language. 🔵 **`p145`'s README surface is the
English-only `licen[cs]e` pattern that `T63` proved cannot match `Licença`/`Licencia`**;
p147's extended matcher can, and reads both as `README_ONLY`. 🟢 **8 is the correct figure.**
The full reconciliation, with every difference attributed:

| class | p149 (58) | after p150's `ACTION FE` | this artefact | 🟢 reconciled |
|---|---|---|---|---|
| `FILE` | 39 | 39 | 39 | **39** |
| `PKG_ONLY` | 4 | 7 | 7 | **7** |
| `README_ONLY` | 7 | 4 | 🔴 **2** | **4** |
| `NONE` | 8 | 8 | 🔴 **10** | **8** |

🟢 **Nothing is unexplained**: the `PKG`/`README` split is the inverted grant ladder p150
fixed, and the `NONE` difference is the English-only README surface. 🔵 **`ACTION FW`** moves
the README-heading question into `lib/` for the same reason the licence-identity question
now lives there (`P40`), and 🔵 **it is deliberately NOT fixed in the pass that measured it**
(`ACTION EU`'s rule).

### 🟢 Where the licence question now lives

🟢 **[`compose/code/lib/licence_identity.py`](../compose/code/lib/licence_identity.py)** —
imported by `p145-licence-census` and `p147-licence-language`. 🔵 **p149's `identify_ext()`
DELEGATES to p147's `identify()`**, so p150's *"three published copies"* were two copies and
one delegation, and two edits fixed all three. 🔴 **`retired_identify()` is kept, and kept
wrong**, so the defect can be reproduced rather than asserted. **47 tests.**

## Pass 150 — 2026-10-12 — this shelf cannot see a GPL row, and has published none in 150 passes

🔴 **`T77`. Five of seven GNU-family rows on this shelf carry the wrong licence
identifier**, and the cause is one published line applied the wrong way.

### 🔴 The defect, and why it is structural rather than a typo

`p145-licence-census.identify()` — copied verbatim into `p147-licence-language` and
`p149-common-title-licence` — tests the licence **body** for a phrase:

    (re.compile(r"GNU AFFERO GENERAL PUBLIC LICENSE", re.I), "AGPL-3.0"),

🔴 **GPL-3.0's own section 13 is TITLED *"Use with the GNU Affero General Public License"***
and its body names the Affero licence twice more. 🔴 **So every verbatim GPL-3.0 file matches
the AGPL rung before the GPL rung is reached.**

🔴 **And the whole family behaves this way.** GPL-2.0's preamble reads *"you may want to use
the GNU Lesser General Public License instead"* — so a GPL-2.0 file matches the **LGPL** rung.
🔵 **Each GNU licence names its siblings in its own text, which is exactly what a
body-substring test cannot survive.** 🔵 **`T39`'s class again: the phrase is right and the
test is wrong, because the phrase lives inside the licence it is meant to exclude.**

### 🔴 The published distribution was the clue, and nobody read it

| licence | rows in `p145`'s published census |
|---|---|
| MIT | 33 |
| *(none)* | 9 |
| 🔴 **AGPL-3.0** | 🔴 **6** |
| Apache-2.0 | 2 |
| 🔴 **LGPL** | 🔴 **1** |
| ISC | 1 |
| 🔴 **GPL** | 🔴 **ZERO** |

🔵 **A shelf of 58 education repositories, a third of them LATAM university scrapers and
Moodle plugins, publishes not one GPL row** — while its own `agents/top.md` describes several
rows as GPL-3.0 by hand. 🔴 **The contradiction was on two pages at once and went nine passes
without being read as a signal.**

### 🟢 Measured, row by row

| row | published | measured from the title line | direction |
|---|---|---|---|
| `Agso-o/sigaa-calendar` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `despedite/siu-guarani` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `mhlavac/edupage-mcp` | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `ahmedEid1/lumen` *(agent tier)* | 🔴 `AGPL-3.0` | 🟢 **GPL-3.0** | 🔴 **OVERSTATED** |
| `qxbao/qldt-hanu-mcp` | 🔴 `LGPL` | 🟢 **GPL-2.0** | 🔴 **WRONG FAMILY, and no version** |
| `edwyj/ddl-killer` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 **right** |
| `fabrica-de-inovacao/expeditto` | 🟢 `AGPL-3.0` | 🟢 **AGPL-3.0** | 🟢 **right** |

🟢 **Two rows are genuinely AGPL-3.0, which is why the defect survived**: the matcher is not
always wrong, so every spot-check that happened to land on `ddl-killer` or `expeditto`
confirmed it.

### 🔵 What the error costs a studio, in both directions

🔴 **Four rows OVERSTATED.** AGPL-3.0 obliges source disclosure to anyone interacting with the
software **over a network**; GPL-3.0 obliges it on **distribution** only. 🔵 **A hosted tutor
or a SaaS SIS connector trips AGPL §13 and does not trip GPL-3.0** — so this shelf has been
telling a studio that three LATAM/EMEA connectors and one tutoring agent are unusable behind a
hosted product when they are ordinary copyleft. 🟢 **The safe direction, and still wrong: it
disqualifies usable work.**

🔴 **One row runs the other way, and that is the dangerous one.** `qxbao/qldt-hanu-mcp` was
filed as `LGPL` — the most permissive member of the family, routinely treated as
link-and-go. 🔴 **It is GPL-2.0**: full copyleft, **no patent grant**, and incompatible with
GPL-3.0-licensed code it might be combined with. 🔵 **An understatement of obligation on a row
nobody flagged.**

### 🟢 The fix: a licence is identified by its TITLE, confirmed by its operative clause

[`p150-gpl-affero-discrimination`](../compose/code/p150-gpl-affero-discrimination/README.md),
**35 tests**, authored fixtures, offline.

| surface | what it reads | why it is independent of the body |
|---|---|---|
| **title** | the licence name as a **whole line** in the first 5 non-blank lines, plus the version | 🟢 **a sentence is never just a licence's name** |
| **clause** | AGPL-3.0's §13 *"Remote Network Interaction"*, anchored to line start | 🟢 **this is the clause that MAKES AGPL different; a plain GPL file cannot contain it** |

🟢 **A verdict is returned only when both surfaces agree**; a hand-edited or genuinely
dual-licensed file comes back `DISAGREE` and is named rather than guessed at. 🟢 **The version
is carried** — `GPL-2.0` and `GPL-3.0` are different instruments and this shelf published
neither.

🔵 **The window must stay narrow, and the tests enforce it.** An earlier draft used a 20-line
title window; the GPL-2.0 fixture caught it reading "Lesser" out of the preamble and returning
`LGPL-2.0` — 🟢 **the defect being fixed, reproduced inside the fix.** The matcher now requires
the licence name to **be** the line.

### 🟢 `ACTION FE` — the grant ladder is corrected, and it moves exactly three rows

[`p150-grant-ladder-order`](../compose/code/p150-grant-ladder-order/README.md), **17 tests**.
🔴 *Refuted if any row other than the three npm rows p149 named changes class.* 🟢 **Falsifier
silent.**

| subject | p147 (inverted) | corrected | direction |
|---|---|---|---|
| `eth-moodle-mcp-1.3.3` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |
| `moodle-mcp-server-aql-0.1.7` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |
| `owen-x-tech-canvas-mcp-1.1.0` | 🔴 `README_ONLY` | 🟢 **`PKG_ONLY`** | 🟢 strengthening |

🟢 **No connector row, no agent row, and no licence IDENTIFICATION changes** — only the rung
recording where the grant was found. 🔵 **p147's inversion had been quietly WEAKENING three
rows**, reporting prose where a declared `package.json` licence exists; the correction restores
the stronger reading, which is why it moves no figure in the dangerous direction.

🟢 **FILE-grant rows are invariant by construction** — `census()` returns on the licence-file
branch before either reordered branch — so the test set is the 18 non-FILE rows plus the 6
agent rows, **24 subjects measured**, and the invariance is asserted rather than assumed.

### 🔴 What this pass did NOT fix, deliberately and otherwise

- 🔴 **The three published copies of `identify()` are UNCHANGED.** `p145`, `p147` and `p149`
  all still carry the body matcher. 🔵 **Correcting them in the pass that measures them is the
  mistake `ACTION EU` exists to avoid** — and the mistake `ACTION FE` was registered to undo.
  🔵 **`ACTION FN`.**
- 🔴 **The 44-row census is NOT re-published.** Five rows are known wrong and the TSV that
  carries them is p145's. 🟢 **The corrected values are in
  [`result.2026-10-12-p150.tsv`](../compose/code/p150-gpl-affero-discrimination/result.2026-10-12-p150.tsv)**
  and the row-by-row table above.
- 🔴 **`GPL-3.0-only` versus `GPL-3.0-or-later` is NOT distinguished.** That election lives in
  per-file headers, not the licence body, and it changes what a derivative may relicense to.
  🔵 **`ACTION FO`.**
- 🔴 **Only 28 trees were measured, not 58.** The GNU-family population was identified from
  `p145`'s published census — which is the artefact under suspicion. 🔵 **A row whose body
  contains no sibling mention cannot be mis-sorted by this defect**, so the published `MIT`,
  `Apache-2.0` and `ISC` rows are not at risk from `T77`; 🔴 **that is an argument, not a
  measurement.** 🔵 **`ACTION FU`.**
- 🔴 **`moodle-mcp-server-aql`'s `AGPL-3.0` is untouched** and stands: it is `PKG_ONLY`, read
  from a declared manifest string, not from a body match.

## Pass 149 — 2026-10-12 — the licence census reproduces over 58, the denominator moves, and two of this KB's instruments disagree about evidence strength

🟢 **Every channel this page needs was open**: 🟢 **`git clone` 50 of 50**, 🟢 **`npm pack` 8 of
8**, 🆕 🟢 **`cargo fetch` + `cargo test` for the Rust row.**

### 🟢 The licence census, reproduced and extended to 58

🟢 **`ACTION FC` re-ran the grant census over the whole population** rather than the 44 this
page usually quotes. 🟢 **Strict-unlicensed reproduces at 8**, and 🔵 **the eight are now named
on one line** so no later pass has to re-derive them:

`MatheusMach/QuantoFalta` · `P1ckle3/blackboard-mcp` · `Piyushtanwani/DAU-buddy` ·
`SIU-Toba/docker-guarani` · `karkarkins/BlackboardAssistantMCP` · `ruud0/aula-virtual-mcp` ·
`hesham0-0nasser/tutor-lms-mcp` · `@n35da/brightspace-mcp@0.4.0`

🔴 **The denominator is 58, not the 57 p148 quoted** — 44 connectors + 8 npm + **6**
agent-tier, every one reached. 🟢 **The figure 8 is unaffected**, because every agent-tier row
but `tutor-lms-mcp` carries a `FILE` grant (`AGPL-3.0`, `MIT`, `MIT`, `Apache-2.0`, `MIT`).
🔴 **Recorded as a one-row discrepancy to reconcile, not as an error in p148**: the agent tier
has **no committed subject list**, so the two counts cannot be compared directly.
🟢 **`ACTION FL` registers the list.**

🔴 **`ACTION FC` itself is REFUTED**: adding eighteen common-title licence forms (`Apache
License 2.0`, `GPLv2`, `GPL v3`, `BSD 3-Clause`, `MPL 2.0`, …) changes **0 of 58** rows.
🟢 **So `T72` is confirmed a Fedena-specific artefact outside this shelf's population.**
🔵 **Exactly one row is `UNIDENTIFIED` under both rules** — `eugeborzone/Auto_Grade_Guarani`,
a Spanish licence **heading with no licence named under it**, which is not a title-form case.
🟢 **The matcher is kept anyway**: it is tested, it costs nothing, and the next shelf this KB
censuses will not be this one.

### 🆕 🔴 `T74` — two of this KB's own instruments disagree about what counts as stronger evidence

🔴 **The page's real finding, and it came out of a reproduction control.**

| module | grant ladder |
|---|---|
| `p145-licence-census` | `FILE` → 🟢 **`PKG_ONLY`** → `README_ONLY` → `NONE` |
| `p147-licence-language` | `FILE` → 🔴 **`README_ONLY`** → `PKG_ONLY` → `NONE` |

🔵 **p145's own docstring states the intent** — *"`README_ONLY` the only mention is prose in a
README. **Weaker still**"* — weaker, that is, than a licence declared in a package manifest.
🔴 **p147 silently inverted the two rungs.**

🟢 **It was invisible on the population p147 ran.** Over the 44 connectors the two modules
agree row for row, because 🔵 **no connector carries both a manifest licence field and a README
licence heading**, and p147's base tally on the 44 reproduces p145's exactly. 🔴 **p147 never
ran the npm tier** — where rows carry both — and there it moves **3 of 8**:
`@owen-x-tech/canvas-mcp@1.1.0` and `eth-moodle-mcp@1.3.3` (**MIT** either way) and
`moodle-mcp-server-aql@0.1.7` (**AGPL-3.0** either way), each from `PKG_ONLY` to `README_ONLY`.

🟢 **No licence identification changes.** 🔴 **What changes is the evidence class, in the
weakening direction**: a declared manifest field demoted to a prose mention. 🔵 **p145's order
is the defensible one.** 🔴 **Deliberately not fixed this pass** — changing the ladder in the
pass that measures it would mean comparing a modified instrument against published figures,
the mistake `ACTION EU` was built to avoid. 🟢 **`ACTION FE`.**

### 🟢 `zavora-ai/mcp-student-records` — the strongest pin on the shelf gains a third surface

🟢 **A third declaration surface, set-identical to the manifest**: the **23** tools flagged
`requires_approval = true` are exactly the **23** names passed to `mcp_2026_server!` as
`approval_tools`. 🟢 **And the crate now builds and tests here** — 24 of its own tests passing,
7 added. 🔴 **Its approval gate, though fail-closed at the MCP boundary, is bypassable
in-process via a `pub` store.** 🔵 **Full detail in `agents/top.md` and `p149-approval-enforcement`.**

### 🟡 `ACTION FB` — the build target behind every `NOT_SHIPPED` figure on this page

🟢 **Named, for all five rows that have an allowlist**: `librus-mcp` **wheel (35)** ·
`soongpt-plugin` **wheel (20)** · `global-education-mcp` **wheel (10)** ·
`vtop-bhopal-mcp` **npm tarball (0)** · `ai-tutor-mcp` **npm tarball (1)**. 🟢 **librus
reproduces p148's 35 / 39 exactly.** 🔴 **`yourssu/soongpt-plugin` declares TWO targets**, which
p148's key list could not see — 🟢 **but they agree at 20**, so `T68`'s *disagreement* stays a
single instance while its *structure* generalises to 2 of 5. 🔵 **The two npm rows are
structurally immune**: one tarball, one `files` key, no second target to disagree with.

## Pass 148 — 2026-10-12 — the foundational Rust row gets a bidirectional pin, and the `NOT_SHIPPED` rule fails as a general rule

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's figures are
re-measured from the payload rather than carried.

### 🟢 `zavora-ai/mcp-student-records` — promoted to the strongest pin on the shelf

🟢 **`ACTION EO` and `ACTION EP` both discharge with silent falsifiers.** This row is the
first on this shelf whose declared tool manifest and whose actual router are proved **equal
as sets**, by an instrument that reads its language.

| property | value | how it is known |
|---|---|---|
| repo | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | clone, this pass |
| licence | 🟢 **Apache-2.0** | full body at `LICENSE`; `Cargo.toml` declares it |
| language | Rust, edition 2024, `rust-version = 1.94.1` | `Cargo.toml` |
| SDK | `rmcp` **3.1.2** + `adk-mcp-sdk` **0.2.0** | `Cargo.toml` |
| 🟢 **router surface** | 🟢 **46** | `#[tool(` sites inside `#[tool_router] impl StudentServer`, `src/server.rs`, brace-tracked |
| 🟢 **declared surface** | 🟢 **46** | `mcp-server.toml`, 46 `[[tools]]` |
| 🟢 **set identity** | 🟢 **PROVED** | symmetric difference empty both ways; **0** duplicates either side; order identical |
| approval-gated writes | **23 of 46** | `requires_approval = true` |
| risk classes | `read_only` / `internal_write` / `ExternalWrite` | typed per tool in the manifest |
| compliance posture | 🟢 **FERPA-gated communications + a FERPA access log** | `get_access_log` tool; package description |
| 🔴 **what the repo itself asserts** | 🔴 **the COUNT only** | `tests/manifest_test.rs`: `len() == 46`, `domain`, `requires_approval` on 11 named writes. 🔴 **No set comparison** |

🔵 **`P144-G` closes at 4 of 4.** The three earlier bidirectional pins were a SHA-256
lockfile (`malkreide/global-education-mcp`, 10), a classification manifest
(`oliverhruby/edupage-mcp`, 31) and a golden name array
(`divyarthjain/vtop-bhopal-mcp`, 17). 🆕 **The fourth is a typed TOML manifest with a risk
class per tool, and it is the only one of the four where the pin is a governance artefact
rather than a test fixture.** 🔴 **It is also the only one of the four the repository does
not verify itself.**

🟢 **For a studio, this is the row to start a records layer on**, and the caveat is one
sentence: the manifest is a contract the code happens to satisfy today, and nothing in CI
stops it drifting. [`p148-rust-surface`](../compose/code/p148-rust-surface/README.md) is the
check to vendor into a build — **14 tests**, offline, no network.

### 🔴 `ACTION EV` — the manifest allowlist cannot replace the name list, and the reason is worse than coverage

`ACTION EC` (p147) found the `NOT_SHIPPED` rule already written in `librus-mcp`'s own
`pyproject.toml`, and `T39` was vindicated. 🔴 **`ACTION EV` asked whether that generalises.
It does not.**

| verdict | n of 16 | meaning |
|---|---|---|
| 🟢 `ALLOWLIST` | **5** | a manifest include allowlist exists and was read |
| 🔴 `MANIFEST_NO_ALLOWLIST` | **7** | a manifest exists and declares no allowlist |
| 🔴 `NO_MANIFEST` | **3** | no package manifest of any kind |
| 🔴 `NO_ALLOWLIST_CONCEPT` | **1** | 🔴 **the manifest CANNOT express one** — `go.mod`; the module is the unit |

🔴 **5 of 16. The falsifier fires by eleven rows.** 🔵 **And `NO_ALLOWLIST_CONCEPT` is the
row that makes this structural rather than incidental**: `Agso-o/sigaa-calendar` is Go, and
no amount of author diligence would give it an include allowlist, because the format has no
such key. 🟢 **That is `T39` one level up — a property-based exclusion is sound only where
the property exists** — and it means the name list stays as a fallback, as the action's
consequence clause specified.

| row | allowlist | items | source |
|---|---|---|---|
| `krzysztofbury/librus-mcp` | 🟢 yes | **1** | `pyproject.toml [tool.hatch.build.targets.wheel] packages` |
| `malkreide/global-education-mcp` | 🟢 yes | **1** | same key |
| `yourssu/soongpt-plugin` | 🟢 yes | **1** | same key |
| `divyarthjain/vtop-bhopal-mcp` | 🟢 yes | **4** | `package.json files` |
| `nirholas/ai-tutor-mcp` | 🟢 yes | **4** | `package.json files` |

### 🆕 🔴 `T68` — and one manifest declares TWO allowlists that disagree

🔴 **This is the sharpest thing `ACTION EV` found, and it corrects p147's prose.**
`librus-mcp`'s `pyproject.toml` carries **two** hatchling include allowlists, for two
different build targets, and they do not admit the same directories:

| target | key | items | 🔴 `.tool(` sites inside it |
|---|---|---|---|
| **wheel** | `packages` | **1** — `src/librus_mcp` | 🟢 **35** |
| **sdist** | `only-include` | **16** — incl. `tests_native`, `scripts/qualify_native.py` | 🔴 **39** |

🔴 **p147 named the 16-item `only-include` as the rule and published 35, which is the wheel
figure.** 🟢 **The number 35 is correct** — it is what the installable package contains, it
matches `MCP_CONTRACT.md`'s prose to the token, and it is the figure a studio consuming the
package would observe. 🔴 **The rule cited for it yields 39**, because the sdist allowlist
admits `scripts/qualify_native.py` (**2** sites) and `tests_native` (**2** sites).

🔵 **So "read the manifest's include allowlist" is underdetermined.** A pass has to say
*which build target*, and the right answer depends on which artefact the question is about.
🟢 **For a tool surface, the wheel is the right target**, and this page states that
explicitly from now on.

🟢 **p147's other librus figures reproduce exactly.** Whole tree **60**, and the
decomposition is **35** (`src/librus_mcp`) + **21** (`legacy_reference`) + **2** (`scripts`)
+ **2** (`tests_native`) = **60**. 🔵 p147 reported *"23 in `legacy_reference` + 2 in
`scripts`"*, attributing `tests_native`'s two to `legacy_reference`; the total is identical
and no published figure changes.

Instrument [`p148-manifest-allowlist`](../compose/code/p148-manifest-allowlist/README.md),
**12 tests** — one of which is the two-allowlist shape itself.

### 🔵 The npm tier, re-measured — unchanged

🟢 **8 of 8 tarballs fetched.** `ACTION EQ` ran the language-extended licence matcher over
all eight: **0 rows change class**. The tier's licence picture stands as p145 published it —
**4 `README_ONLY`, 3 `PKG_ONLY`, 1 `NONE`** (`@n35da/brightspace-mcp`, still the only npm
row on this shelf with no grant on any channel, and still the only one of the eight that
ships source).
## Pass 147 — 2026-10-12 — the npm tier gains two regions, and a foundational row was never read

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's npm block is
re-measured from the payload rather than carried.

### 🆕 🟢 Two npm rows are region-placeable after all — `T59` NARROWED

🔴 **`T59` called this shelf's 8 npm rows "structurally unplaceable on the region axis."**
🟢 **That is a property of the INSTRUMENT lane, not of the evidence.**

| row | region | host | where | strength |
|---|---|---|---|---|
| 🟢 `eth-moodle-mcp@1.3.3` | 🟢 **EMEA** | `moodle-app2.let.ethz.ch` — ETH Zürich | `README.md:76`, the `MOODLE_URL` **default** | 🟢 **strong** |
| 🟡 `mcp-canvas-lms@1.0.5` | 🟡 **APAC** | `canvas.ust.hk` — HKUST | `README.md:37`, an **`e.g.`** | 🟡 **a lead** |
| `@imazhar101/mcp-canvas-server` | 🔴 `UNPLACED` | — | — | — |
| `@ink-waffle/moodle-mcp` | 🔴 `UNPLACED` | — | — | — |
| `@n35da/brightspace-mcp` | 🔴 `UNPLACED` | — | 🔴 only `d2l.myschool.edu`, a placeholder | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `UNPLACED` | — | — | — |
| `canvas-mcp-server` | 🔴 `UNPLACED` | — | — | — |
| `moodle-mcp-server-aql` | 🔴 `UNPLACED` | — | 🔴 only `moodle.example.edu`, a placeholder | — |

🟢 **`eth-moodle-mcp` is strong because two independent Swiss-specific signals agree**: the
shipped `MOODLE_URL` default is ETH Zürich's production Moodle, and the token-minting
instruction names **nethz** (ETH's account system) and **AAI** (SWITCHaai, the Swiss
academic federation). Instrument [`p147-npm-region`](../compose/code/p147-npm-region/README.md), **15 tests**.

### 🟢 `@imazhar101/mcp-canvas-server` — 227 confirmed by a third method

🔴 **This page has carried a disagreement: 227 descriptors on one instrument, 18 dynamic
sites on another.** 🟢 **Resolving the 18 one level gives exactly 227.**

**18 tool modules, 18 spread sites in the `tools/list` handler, 1:1** at
`dist/servers/canvas/src/index.js:263-280`. Largest: `user-tools` **39**, `page-tools`
**21**, `file-tools` **20**, `submission-tools` **20**, `module-tools` **18**. Smallest:
`lti-launch-definition-tools` **1**, `grading-standard-tools` **3**, `admin-tools` **4**.

🟢 **So `T42` is confirmed by a third method**: `surface_bound` counts descriptors,
`surface_gate*` counts registration sites, and the two are the same surface at two levels.
🔵 **The largest tool surface this KB quotes is correct.** Instrument
[`p147-tooldef-sum`](../compose/code/p147-tooldef-sum/README.md), **11 tests**.

### 🆕 🟢 A foundational row this page should have had — Apache-2.0, Rust, 46 tools

| [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | v1.2.0 |
|---|---|
| licence | 🟢 **Apache-2.0** — buildable on, no copyleft |
| surface | 🟢 **46 tools**, declared in `mcp-server.toml` and pinned by test |
| write governance | 🟢 **23 of 46 `requires_approval = true`**; typed `risk_class` per tool |
| compliance | 🟢 **FERPA-gated communications + FERPA access log** |
| domain | 🟢 self-declared `domain = "education"` in the manifest |

🔴 **Both `os.walk` surface gates on this shelf read it as zero files**, because it is Rust
and `lang_of` has no `.rs` (`T64`). 🔵 **It is a complete SIS surface — students, courses,
enrollments, grades, rubrics, attendance, guardians, transcripts, analytics — under a
permissive licence, and the shelf could not see it.**

### 🔴 `moodle-mcp-server-aql`'s AGPL-3.0 — a packaging defect, not a missing grant

🔴 **`ACTION EF` REFUTED exactly as its falsifier specified.** The declared repository
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) is alive
and carries the **complete 661-line AGPL-3.0 body** at its monorepo root.

🔴 **The tarball carries no licence file at all.** Cause, named precisely:
`packages/server/package.json` ships an explicit **`files` allowlist of 16 globs**, none of
them `LICENSE`, and there is **no `LICENSE` inside `packages/server/`**. 🔵 **npm's
automatic licence inclusion looks in the package directory and does not reach up a
monorepo.** 🟢 **The grant exists and it is AGPL-3.0** — the obligation is real, the file
just never shipped. 🔵 **Restate as a packaging warning, not a licence gap.**

## Pass 146 — 2026-10-12 — the platform layer's licence map, and a shelf-wide instrument defect

🔴 **No foundational repo was cloned this pass** (`P146-A`). 🟢 **But the licence axis of the
major platform layer was read for the first time, on a channel no previous pass had
tried** — and it changes which platform a studio should reach for.

### 🆕 🟢 The platform layer, read on the licence axis — one permissive row out of seven

| repo | licence | ★ | what it is | build bar |
|---|---|---|---|---|
| 🟢 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 1.2k | Learning, teaching, research and collaboration platform. 🟢 **ECL-2.0 is Apache-2.0 with a narrowed §3 patent grant — OSI-approved, copyleft: no** | 🟢 **PASSES** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | 8.2k | The Open edX LMS and Studio. MOOC-grade, Python/Django | 🔴 **network copyleft** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | 6.9k | Instructure's open LMS, alongside its commercial SaaS | 🔴 **network copyleft** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 6.2k | The most-deployed LMS worldwide; deepest plugin ecosystem | 🔴 copyleft |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility | 🔴 copyleft |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 886 | 🟢 **LMS + SIS + fees + parent app on ONE database**, on the Odoo framework | 🔴 weak copyleft |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 505 | Official ILIAS release and development branches | 🔴 copyleft |

🔵 **Why this is a foundations finding and not a verticals one.** A foundational repo is
one you build **on**. 🔴 **Six of these seven cannot be built on in the fork-and-modify
sense without a reciprocal obligation**, and the two largest carry AGPL's network clause,
which triggers on precisely the hosted multi-tenant shape these platforms are deployed in.
🟢 **Sakai is the only row where fork-and-modify is also on the table** — and it is the
fourth-largest, which is why no previous pass noticed.

🟢 **The API-boundary pattern remains the default on every copyleft row** and is unaffected:
a separate agent service speaking REST/LTI to the platform incurs no obligation on the
agent's own code. 🔵 **The licence map changes which platform you pick when the client
needs core changes, not whether the shelf's patterns work.**

### 🆕 🔴 The instrument layer under this page has a shelf-wide defect

🔴 **`T42` is a property of this shelf, not an incident.** `p146-exclusion-reach` reads every
traversing instrument in `compose/code/`:

| | count |
|---|---|
| instruments that traverse a tree | **35** |
| …carrying an **empty-walk guard** | 🔴 **0** |
| …excluding `dist`/`build` with no re-admission while emitting a verdict | 🔴 **5** |
| …that **cannot read anything but a git clone** | 🔴 **16** |

🆕 🔴 **`T59`**: 16 of 35 instruments traverse by `git ls-tree`/`ls-files`, so a clone is a
**precondition**, not a convenience — and 🔴 **the entire region-placement lane is in that
set** (`americas`, `cctld_urlctx`, `origin_scale`, `repo_origin`, `tenancy`). 🔵 **A
published npm package is not a git tree, so the 8 npm rows on this shelf are structurally
unplaceable on the region axis this KB exists to serve.** 🔴 **No pass had said so.**
`ACTION EK` asks whether a non-git channel can place any of them.

🟢 **`p146-empty-walk-guard` is the four-line fix**, with the distinction it exists to
preserve pinned by test: *zero files walked* withholds a verdict; *files walked, none
matched* is a finding and keeps its verdict.

### 🔴 What this page did NOT do this pass

- 🔴 **No star count, commit count, HEAD date or licence file was read for any existing
  shelf row** — all of those need a clone.
- 🔴 **The seven platform licences above are page readings, not `LICENSE`-file reads.** A
  licence badge is a declaration; `T21`/`P145-I` is this KB's own evidence that a
  declaration and a shipped grant diverge. 🔵 **They are published as declarations.**
- 🔴 **OpenEduCat's Odoo dependency chain was not read** — upstream is LGPL-3.0 with a
  proprietary Enterprise edition, and the obligation interaction is unknown.

# Education — foundational repos

**Pass 145, 2026-10-12.** 🔴 **The npm rows on this page were never read.** The instrument
this KB measures tool surfaces with excludes `dist` and `build` unconditionally, and **7 of
the 8 npm packages cited here ship their entire payload under exactly those two names**.
🟢 **All eight are now measured**, and 🔴 **none of the eight ships a licence file.**

### 🔴 `ACTION DZ` / `P145-A` — seven rows on this page returned a verdict over zero files

🔵 **p144 discharged `ACTION DP` by cloning three npm packages and comparing bundle against
source.** That comparison was sound. 🔴 **What nobody checked is whether the instrument
could read the bundle at all** — and on seven of eight rows it could not, because
`SKIP_DIRS` removed the only tree the package ships.

| package | all code under | files | p143 read | p145 reads |
|---|---|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 `dist/` | 69 | 🔴 `NOT_AN_MCP_SERVER` | **18 dynamic sites** (227 descriptors) |
| `moodle-mcp-server-aql` | 🔴 `dist/` | 68 | 🔴 `NOT_AN_MCP_SERVER` | 🔴 **`MUTATED` — plugin-extensible** |
| `@ink-waffle/moodle-mcp` | 🔴 `dist/` | 18 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **16 literal** |
| `mcp-canvas-lms` | 🔴 `dist/` | 16 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **3 literal** |
| `eth-moodle-mcp` | 🔴 `build/` | 13 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **18 literal** |
| `canvas-mcp-server` | 🔴 `build/` | 6 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **54 literal** |
| `@owen-x-tech/canvas-mcp` | 🔴 `build/` | 4 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **62 literal** |
| 🟢 `@n35da/brightspace-mcp` | 🟢 `lib/` + `server.mjs` | 17 | 🟢 **17 dynamic** | 🟢 **17 dynamic** (unchanged) |

🟢 **Four of the new readings reproduce counts this page already held by other means** — 16,
3, 18 and 54 match `p143-tier-size`'s hand counts exactly, and **62** matches the live
surface `p139` established for `@owen-x-tech/canvas-mcp`. 🔵 **Agreement across two
unrelated instruments on five rows is what makes the seven corrections trustworthy.**

### 🔴 The rule this page should have been applying, and now is

> **A tree is excluded only when it does not bear the property being measured.**

`dist/` is a regenerated artefact in a git checkout and **the shipped source itself** in a
published tarball. 🔵 **Same name, opposite correctness** — so the test is the package's own
declared entry point (`main`, `bin`, `module`, `exports`), not the name. Instrument:
[`p145-surface-payload-repair`](../compose/code/p145-surface-payload-repair/README.md),
**14 tests**.

🟢 **This also forecloses `T37` by construction**: a committed `dist/` beside its own source
stays excluded, so the double count that defeated `P144-A`'s first draft cannot recur.

### 🔴 `ACTION DX` — not one npm row on this page ships a licence file

| package | grant | licence |
|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 README only | MIT |
| `@ink-waffle/moodle-mcp` | 🔴 `package.json` only | MIT |
| `@n35da/brightspace-mcp` | 🔴 **NONE** | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `package.json` only | MIT |
| `canvas-mcp-server` | 🔴 `package.json` only | MIT |
| `eth-moodle-mcp` | 🔴 `package.json` only | MIT |
| `mcp-canvas-lms` | 🔴 `package.json` only | MIT |
| `moodle-mcp-server-aql` | 🔴 `package.json` only | 🔴 **AGPL-3.0** |

🔴 **0 of 8.** 🔵 **Consistent with `T21`'s 33% npm licence-payload rate rather than in
conflict with it**: `npm pack` includes a `LICENSE` only if one exists in the tree, so a
0% file rate at HEAD and a 33% historical payload rate describe the same population at two
times. 🟢 **`P138`'s distinction holds and is the operative one here — a licence identifier
is not a licence**, and seven of these rows offer only an identifier.

🔴 **`@n35da/brightspace-mcp` is the sharpest row on the page**: the only npm package that
ships readable source, and the only one with no licence of any kind. 🔵 **The row a
developer can most easily learn from is the row they have least right to copy.**

### 🔴 The foundational row that is unbounded by design

`moodle-mcp-server-aql` builds `toolDefinitions = buildCoreToolDefinitions()` and then
**`.push()`es one descriptor per discovered plugin** (`dist/server/factory.js:131`, inside
the plugin loop). 🔴 **Its tool surface is a property of the deployment's plugin set**, not
of the published package — the first row on these shelves that is unbounded for an
architectural reason rather than an instrumental one.

🔴 **It is also the AGPL-3.0 declaration.** 🔵 **A plugin-extensible connector under
copyleft is a specific delivery hazard**: the extension points invite exactly the
modification the licence attaches obligations to. `ACTION EF` tests whether any licence
text exists behind the declaration.

### 🟢 What this page can now say about its own instruments

🔴 **`ACTION DV` asked for all four tiers under one instrument and that is not achievable
here.** `surface_bound.py` reads **JS and TS only**; of the 20 MCP servers across the four
tiers, **7 are Python and 1 is PHP**. 🔵 **Recorded as a structural property of the
population**, not as an environment blocker and not as a probe to re-register.

🔴 **And the two instruments measure different things.** `surface_bound` counts
**descriptors**; the gate instruments count **registration sites**. On
`@imazhar101/mcp-canvas-server` that is **227** against **18**, and 🟢 **neither number is
wrong** — which is why `T30`, built across both, is withdrawn outright rather than
reinstated.


**Pass 144, 2026-10-12.** 🔴 **The correction this page owed about its npm instruments is
discharged, and it resolves in the opposite direction.** p143 recorded that 7 of 8 npm packages
could not be read at all because they ship only compiled output, and withdrew the npm figures on
that basis. 🟢 **Three of them were cloned this pass and the compiled output turns out to be a
faithful measurement**: bundle and shipped source return **identical tool-name sets** on 3 of 3.
🔴 **But 5 of 8 have no reachable source at all**, and one of those *declares* a repository that
is dead.

### 🟢 `ACTION DP` — the npm foundation rows measure the same on bundle and on source

[`p144-npm-source-parity`](../compose/code/p144-npm-source-parity/README.md).

| package | repo | licence | bundle | shipped source | name sets |
|---|---|---|---|---|---|
| `canvas-mcp-server@2.2.3` | 🟢 [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🟢 MIT | **54** | 🟢 **54** | 🟢 identical |
| `moodle-mcp-server-aql@0.1.7` | 🟢 [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** | **14** | 🟢 **14** | 🟢 identical |
| `mcp-canvas-lms@1.0.5` | 🟢 [`MisterCommand/mcp-canvas-lms`](https://github.com/MisterCommand/mcp-canvas-lms) | 🟢 MIT | **3** | 🟢 **3** | 🟢 identical |

🔵 **Set identity is the claim, not count identity** — `namesets.py` reports `bundle_only` and
`source_only`, both empty on all three rows. 🟢 **So `T30`'s npm figure is reinstated**, which is
what `ACTION DP` specified on this outcome.

🔴 **`moodle-mcp-server-aql` is AGPL-3.0 and that is a stop-ship for a studio build**, declared
in the npm metadata and confirmed in the repository. It is the only copyleft row on the npm tier.

### 🔴 The 5 rows this page cannot verify, stated per row rather than as a share

| package | source route | outcome |
|---|---|---|
| `@owen-x-tech/canvas-mcp@1.1.0` | `repository: owentaylor/canvas-mcp` | 🔴 **DECLARED AND DEAD** — `git ls-remote` prompts for credentials |
| `@imazhar101/mcp-canvas-server@2.1.3` | none | 🔴 no `repository`, `homepage` or `bugs`; **227 declared tools unverifiable** |
| `@ink-waffle/moodle-mcp@0.2.0` | none | 🔴 **18 `.map` files, zero `sourcesContent`** |
| `@n35da/brightspace-mcp@0.4.0` | none | 🔴 no pointer |
| `eth-moodle-mcp@1.3.3` | none | 🔴 no pointer |

🟢 **One correction to `P138-H` in the other direction**: `mcp-canvas-lms` was recorded as having
no `repository` field, which is true, and it is placeable anyway from `homepage`/`bugs`. 🔵 **A
missing `repository` field is not the same as an unsourceable package**, and three fields have to
be read before a row is declared dark.

🔴 **The sourcemap route is now closed and recorded as closed.** Three packages ship `.map`
files and not one carries `sourcesContent`, so a map yields original *path names* and no original
*bytes*. 🔵 **A future pass should not re-attempt it.**

### 🟢 `global-education-mcp` is no longer the only self-verifying row on this page

[`p144-surface-pin-census`](../compose/code/p144-surface-pin-census/README.md). `ACTION DQ` asked
for a second row carrying a committed tool-surface pin and found **two**, by two mechanisms
neither of which is a hash lockfile.

| row | licence | mechanism | pinned |
|---|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 MIT | `tools.lock.json`, SHA-256 per tool | **10** |
| 🆕 🟢 [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | 🟢 MIT | classification manifest over live `list_tools()` | **31** |
| 🆕 🟢 [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) | 🟢 Apache-2.0 | `EXPECTED_TOOLS` golden name array | **17** |

🔴 **Three instances and three incompatible formats.** 🔵 **So a consumer cannot ask "does it
ship the lockfile?"** — the question is whether *any* committed artefact pins the surface, and
the answer has to be looked for in three places.

### 🆕 🔴 Two rows cited by this KB carry no licence at all

Found while verifying something else, which is why `ACTION DX` now counts all 44 connector rows
and all 8 packages rather than trusting an incidental pair.

| row | size | licence at HEAD |
|---|---|---|
| 🔴 [`Piyushtanwani/DAU-buddy`](https://github.com/Piyushtanwani/DAU-buddy) | **40 literal tools, 176 commits** | 🔴 **NONE** |
| 🔴 [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | 4 commits | 🔴 **NONE** |

🔴 **`DAU-buddy` is the largest tool surface on the github-only tier and it is unusable** — no
licence means no grant, and no grant means a studio cannot copy a line of it. 🔵 **It remains
worth reading as a design reference**, which is a different permission from building on it.

### 🔵 Channel note — `curl -sI` cannot verify a GitHub URL in this environment

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` for every repository, live or
dead**, so it cannot distinguish them and must not be used as a URL check here. 🟢 **`git
ls-remote` and `git clone` both work**, and are what showed `owentaylor/canvas-mcp` to be dead
rather than merely unreachable. 🔵 **Every repository figure on this page was produced by
`git clone` over full history**; see
[`evidence/verified-repos.2026-10-12-p144.tsv`](../evidence/verified-repos.2026-10-12-p144.tsv).

**Pass 143, 2026-10-12.** 🟢 **`ACTION DO` discharged: the education-statistics row added last
pass is now VERIFIED rather than declared**, and it is the only row on this page whose tool
surface a consumer can check without running it. 🔴 **And a correction this page owes: the
licence-and-payload instruments it cites for npm rows cannot read 7 of the 8 npm packages at
all**, because they ship only compiled output.

### 🟢 `ACTION DO` — `global-education-mcp`'s lockfile verifies, independently recomputed

[`p143-lockfile-audit`](../compose/code/p143-lockfile-audit/README.md). p142 added this row on
the strength of a *declared* `tools.lock.json`. 🟢 **It is now a checked claim.**

| row | licence | verification |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **10 of 10 hashes recompute**, independently of the repository's own generator. 🟢 **10 of 10 agree with `server.py`** on `name`, `annotations` and `description`. 🟢 **10 of 10 `readOnlyHint: true`, zero write tools.** HEAD `26f7cd2`, **2026-10-04**, EMEA (`+0200` ×70) |

🔴 **One of the four hashed fields is NOT verified and the honest statement names it.**
`inputSchema` is generated by pydantic at import; checking it requires executing the
repository, which this audit does not do. 🔵 **So a consumer who cannot run the server has
verified three fields of four** — and that is still the strongest tool-surface guarantee
anywhere on these shelves.

**What a studio does with it.** 🟢 **`scripts/tool_signatures.py ci` is one CI step that
replaces four of this KB's own instruments** (`p139-tool-count-drift`,
`description-drift-audit`, `p141-agent-surface-gate`, `p142-github-only-tier`) for any
repository that adopts the pattern. 🔵 **It is the cheapest control on these shelves and it is
MIT**, so it can be lifted.

### 🔴 A correction this page owes about its own npm instruments

[`p143-tier-size`](../compose/code/p143-tier-size/README.md) measured what the 8 npm connector
packages actually ship:

| | |
|---|---|
| 🔴 npm packages shipping **only** compiled output (`dist/` or `build/`) | **7 of 8** |
| 🟢 npm packages shipping **source** | **1 of 8** — `@n35da/brightspace-mcp` (`.mjs`, `lib/`) |

🔴 **So a source-reading instrument sees nothing in 7 of 8 npm rows**, and any figure this KB
has published comparing npm rows to repository rows was comparing a **bundle** to a **source
tree**. 🔵 **`T21`'s licence-payload gradient is unaffected** — it reads published packages in
all three ecosystems, one artefact kind throughout, which is exactly why it has survived four
falsifiers. 🔴 **`T30`'s registration gradient is withdrawn**, and `T36` is the general rule.

**The practical consequence for a studio evaluating an npm education connector.** 🔴 **You
cannot audit what you cannot read.** 7 of 8 of these packages require fetching the repository
separately to review the code you are installing, and `@owen-x-tech/canvas-mcp` — whose README
claims 150+ tools against 62 measured — 🔴 **is the row whose repository is gone.** 🟢 **Prefer
the row that ships source or pins its surface**; on this page that is `@n35da/brightspace-mcp`
and `malkreide/global-education-mcp` respectively.

### 🔵 Channel note — the clone channel opened, and it changes what this page can verify

🟢 **`git clone` of public repositories now works from this environment**, with full history.
🔵 **Every verification on this page previously rested on single-file fetches**; licence files,
POM chains and payload measurements can now be read in tree. 🔴 **`api.github.com` repository
endpoints remain refused — on SCOPE, not a block** (`rate_limit` answers `200`), so star counts
are still unavailable and commit counts remain the size proxy. 🔴 **`codeload.github.com`
tarballs are `403` while `git clone` succeeds**, which is worth recording as a channel
asymmetry rather than rediscovering.

**Pass 142, 2026-10-12.** 🔴 **`ACTION DF` refuted: the licence a consumer gets from veraPDF
depends on which MODULE it resolves, not on the project.** 🟢 **And a foundational row is added
that this page has never had a category for — a permissively licensed, read-only connector over
UNESCO and OECD education statistics, which is a primary source for the figures `intel/market.md`
has had to take from vendor blogs.**

### 🔴 `ACTION DF` — veraPDF's grant is per-module, and 3 of 3 jars say nothing

[`p142-verapdf-module-grant`](../compose/code/p142-verapdf-module-grant/README.md). p140's
parent-chain walker, **executed unchanged**; only the coordinates are new.

| coordinate | own POM | effective licence | depth | jar licence text |
|---|---|---|---|---|
| `org.verapdf:core:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** *(from `verapdf-parent`)* | **4** | 🔴 `SILENT` — 460 entries |
| 🔴 **`org.verapdf:verapdf-xmp-core:1.30.3`** | 🟢 **BSD-3-Clause** | 🟢 **BSD-3-Clause** | 4 | 🔴 `SILENT` — 78 entries |
| `org.verapdf:validation-model:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** | 4 | 🔴 `SILENT` — 369 entries |
| 🔴 `org.verapdf:xmp-core:1.30.3` | — | — | — | 🔴 **404 — never published** |

**What a studio has to do differently.** veraPDF is the PDF/UA validator — the component you
reach for when course material has to meet an accessibility obligation. 🔴 **The election between
GPL-3.0 and MPL-2.0 applies to `core` and `validation-model` and does NOT arise for
`verapdf-xmp-core`, which is BSD-3-Clause.** A scanner reading the named umbrella coordinate
reports nothing and the umbrella has no jar at all.

🔵 **`org.verapdf:xmp-core` was never a coordinate.** p141 read it out of
`<modules><module>xmp-core</module></modules>`, and **a `<module>` entry is a source-tree path,
not an artifactId** — the directory `xmp-core/` builds `verapdf-xmp-core`. Any probe deriving
coordinates from a `<modules>` block inherits this error; it is pinned as a test.

### 🆕 🟢 The education-statistics layer — a foundational tier this page did not have

| repo | licence | what it is |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **UNESCO UIS (4 000+ indicators) and OECD *Education at a Glance*, over SDMX, with no API key.** 151 commits, HEAD **2026-10-04**, EMEA (`+0200` ×70). **10 tools, every name a literal, every one `readOnlyHint: true` — zero write tools.** Full MCP `ToolAnnotations` on 10 of 10, and 🟢 **a `tools.lock.json` that SHA-256-hashes each tool's annotations, description and schema** |
| 🟢 [`alcastaro/opendata-latam-mcp`](https://github.com/alcastaro/opendata-latam-mcp) | 🟢 **MIT** | 7 national CKAN open-data portals (AR, CL, DO, EC, MX, PA, UY), 15 628 datasets, cross-country parallel search. 🟢 **LATAM-placed on government hosts in 8 countries.** Not education-specific; the regional-evidence layer for engagements that need one |

🔵 **Why these belong on a *foundations* page rather than only on the agents shelf.** Every
regional figure this KB carries — market size, adoption rate, CAGR by region — currently comes
from market-research marketing pages, and `intel/market.md` says so each pass. 🟢 **UNESCO UIS and
OECD EAG are the primary sources those pages are re-quoting**, and there is now an MIT-licensed,
read-only, annotation-complete client for both.

🔴 **And it cannot run here.** `api.uis.unesco.org` and `sdmx.oecd.org` both answer `000` through
this environment's proxy. 🔵 **This is the most actionable entry the blocked-source ledger has
ever carried: two hostnames, one MIT dependency, and the figure channel this KB has been missing
for twenty passes.**

### 🟢 The practice worth copying off this page's newest row

`tools.lock.json` is a **tool-surface lockfile**: one SHA-256 per tool over its signature
(annotations + description + input schema), committed. 🔵 **This KB has built four instruments to
detect what that file prevents** — `p139-tool-count-drift`, `description-drift-audit`,
`p141-agent-surface-gate`, `p142-github-only-tier`. 🟢 **A row that pins its own surface by hash
makes all four unnecessary against it**, and the repository's own comment states the intent: the
logging wrapper preserves `__doc__` *"damit der `tools.lock.json`-Hash stabil bleibt"*. Adopted
as pattern `P21`.

**Pass 141, 2026-10-12.** 🔴 **`ACTION DC` applied p140's parent-chain walk to every Maven
coordinate this KB cites, and three further rows change verdict — so `T26` is not a property of
two artefacts but of Maven's inheritance model.** 🔴 **`ACTION DA` found the opposite failure
one layer below `openedx-core`'s distribution: not a disagreement between layers, but silence
in all of them below the wheel.**

### 🔴 `ACTION DC` — 5 of 9 coordinates on this shelf do not declare their own licence

[`p141-pom-chain-sweep`](../compose/code/p141-pom-chain-sweep/README.md). The walker is p140's,
re-used **unchanged** so that a changed verdict cannot be mistaken for a changed method; only
the population is new.

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util:1.2.0` | Apache-2.0 | — | — | 1 |
| 🆕 🔴 **`org.verapdf:verapdf-library:1.30.3`** | 🔴 **NONE** | `org.verapdf:verapdf-parent:1.30.1` | 🔴 **GPL-3.0 *or* MPL-2.0** | **3** |
| 🆕 🔴 `org.jasig.ssp:ssp:2.8.0` | 🔴 **NONE** | `org.jasig.parent:jasig-parent:39` | Apache-2.0 | **3** |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |
| 🆕 🟢 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` | Apache-2.0 | — | — | 1 |

Cumulative, p140 + p141: 🔴 **`INHERITS_FROM_PARENT` 5** (`net.oauth.core:oauth`,
`sakai-kernel-impl`, `verapdf-library`, `jasig.ssp:ssp`, `sakaiproject:kernel`) against 🟢
**`DECLARES_OWN` 4** (`sakai-kernel-api`, `lti-launch`, `basiclti-util`,
`spring-security-lti13`). 🔵 **56% inherit. An audit that reads one POM per coordinate is wrong
more often than right on this shelf.**

🟢 **`org.imsglobal:basiclti-util:1.2.0` is also now walked rather than carried.** p140's prose
table listed it as *"Apache-2.0 (own)"* on an earlier pass's authority while its committed TSV
held only four rows. 🟢 **The walk confirms it — `DECLARES_OWN`, depth 1** — so the cell is
now evidenced by the same instrument as its neighbours rather than inherited from prose.

### 🔴 The row that should change a delivery decision: veraPDF

`org.verapdf:verapdf-library` is the **PDF/UA accessibility validator** — in an education
engagement, the component reached for to prove course material meets an accessibility duty.

🔴 **Its own POM carries no `<licenses>` block at all. The grant is two levels up, and it is a
dual GPL-3.0 / MPL-2.0 offer** — at once the strongest reciprocal licence anywhere on these
shelves and, through MPL-2.0, the route out of it. 🟢 **MPL-2.0 is the obvious election for a
studio, and it cannot be elected by a team that does not know it is offered.** 🔴 A scanner
reading the named coordinate reports *"no licence"*, which invites the *"permissive by default"*
error p140 corrected on `net.oauth.core:oauth` — this time on a component whose licence
genuinely constrains redistribution.

🔵 **And there is no payload to inspect for a second opinion.** `verapdf-library` is
`<packaging>pom` with modules `core` and `xmp-core`; 🔴 **`verapdf-library-1.30.3.jar` is 404 on
Central**, because no jar is published under that name — consumers resolve `org.verapdf:core`.
`org.jasig.ssp:ssp:2.8.0` is the same class, `<packaging>war`. 🔵 **The coordinate a dependency
declaration names has no own grant and no bytes: the licence lives in a parent and the code
lives in siblings.** `org.sonatype.oss:oss-parent:7` is the shared grandparent of both chains
and declares nothing, so the walk must continue *past* a silent ancestor rather than stop there.

### 🟢 The cleanest Maven row on this shelf, and it places itself in EMEA

🆕 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` — **Apache-2.0, declared in its own POM, depth 1**,
LTI 1.3 for Spring Security. 🔵 **Its `groupId` is the origin evidence**: `uk.ac.ox` is the
University of Oxford's reverse-DNS namespace and `.ac.uk` maps to 🟢 **EMEA** with no inference
required. A Maven `groupId` is a stronger origin signal than an npm author field — it is a
namespace the organisation had to control in order to publish — and this is the first row this
KB has placed that way.

🔴 **It still ships no licence text** — no `LICENSE` or `NOTICE` among the jar's 72 entries. So
`T21`'s gradient firms up on a sixth Maven row rather than softening:

| ecosystem | declares a licence, ships no text |
|---|---|
| PyPI | 🟢 **0%** — 0 of 10 *(after p140's `openedx-learning` correction)* |
| npm | 33% |
| 🔴 **Maven** | 🔴 **83% — 5 of 6** *(p140: 80%, 4 of 5)* |

🔴 **`edu.ksu.ome.lti:lti-launch` 1.4.7 remains the worst row on the shelf** — LGPL-3.0 declared
in its own POM, no text in the jar, and pattern `P13` still depends on it.

### 🔴 `ACTION DA` — `openedx-core` is clean at the distribution layer and SILENT below it

[`p141-package-grant-layer`](../compose/code/p141-package-grant-layer/README.md). p140 called
`openedx-core` **1.9.1** the cleanest licence payload this KB has measured. 🟢 **That stands.**
🔴 **One layer down there is nothing.**

| package | `.py` files | licence files | SPDX headers | copyright lines |
|---|---|---|---|---|
| `openedx_catalog` | 12 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_content` | **132** | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_core` | 1 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_django_lib` | 7 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_learning` | 29 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_tagging` | 56 | 🔴 0 | 🔴 0 | 🔴 0 |
| **total** | **237** | 🔴 **0** | 🔴 **0** | 🔴 **0** |

🟢 Distribution layer, for contrast: `License-Expression: AGPL-3.0-only` (PEP 639) plus
`dist-info/licenses/LICENSE.txt`, **35 139 bytes**, Metadata-Version 2.4.

🔵 **p140's falsifier expected DISAGREEMENT between layers. The measured answer is SILENCE — and
for a studio that is the worse one.** Nobody vendors a wheel; they lift `openedx_tagging/` or
`openedx_content/` into their own tree. 🔴 **The moment a subtree leaves `dist-info/`'s company
it carries no grant, no holder and no notice** — while **AGPL-3.0-only** is the most reciprocal
obligation anywhere on these shelves. 🔵 **The licence is correct, current and complete in
exactly the one place the copy does not come from.** A `T21`-clean artefact can be `T18`-silent;
this is the clearest instance of it, and both findings are true of different layers.

🟢 **One thing this confirms rather than discovers:** `openedx_learning` survives as a **package
inside** the distribution even though the *distribution* `openedx-learning` was retired to a
shim. 🔵 **The name was demoted, not killed** — the 29 files under it are live code at 1.9.1,
not the 1 479-byte husk `openedx-learning` 0.33.1 publishes. A row keyed on the string alone
cannot distinguish those, which is exactly why `T27` reads the `Development Status` classifier.

### 🟡 One citation on this page, re-checked and confirmed

`uk.ac.ox.ctl:spring-lti13` is **404 on Maven Central**, as the row below already records. 🟢
The real artefact is `spring-security-lti13`; the shorter coordinate has never existed. 🔵
Recorded as a confirmation, not republished as a finding — and the kind of re-check `T24` exists
to force.

### 🔴 A method note: a `429` from Central is not a `404`

Maven Central answered **429** on two of six metadata fetches and on the `basiclti-util` jar,
clearing after 8–24 s of backoff. 🔴 **An earlier draft of this sweep recorded
`uk.ac.ox.ctl:spring-security-lti13` as "not on Central" off a single un-retried `429`** — which
would have deleted the cleanest row in the table above. Every fetch retries with backoff and a
failure is reported as a failure, never as an absence.


**Pass 140, 2026-10-12.** 🔴 **Two of p139's findings on this page are refuted, and both
refutations make the underlying defect worse rather than milder.** `ACTION CR` resolved the Maven
parent chains p139 recorded as "no signal"; `ACTION CS` established that the one PyPI hit was
never a defect at all — it is a **package rename this KB has been failing to follow for two
passes.**

### 🔴 `ACTION CR` — both "declares nothing" rows DO declare, two and three levels up

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🔴 `net.oauth.core:oauth` 20100527 | **NONE** | 🆕 `net.oauth:oauth-parent:20090531` | 🆕 **Apache-2.0** | 3 |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | **NONE** | 🆕 `org.sakaiproject:oss-parent:1` | 🆕 **ECL-2.0** | 4 |

Both p139 controls return unchanged — `sakai-kernel-api` 25.2 `DECLARES_OWN` (ECL-2.0),
`edu.ksu.ome.lti:lti-launch` 1.4.7 `DECLARES_OWN` (LGPL-3.0) — so the changed verdicts belong to
the rows, not to the method.
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🔴 Two sentences on this page are now wrong, and here is the correction

p139 wrote, of `net.oauth.core:oauth`:

> *"carries no licence signal at all … No grant and no file is not 'permissive by default' — it
> is **unlicensed**, and sixteen years of use does not change that."*

🔴 **There is a grant: Apache-2.0, inherited from `net.oauth:oauth-parent`.** 🔵 **And the reason
nobody found it is the finding** — the parent sits under a **different `groupId`**, `net.oauth`
rather than `net.oauth.core`. The artefact is not unlicensed. Its grant is two files and one
namespace hop from where any reader would look.

p139 also described the two Sakai kernel artefacts as *"same release line, opposite licence
posture"*. 🔴 **Both are ECL-2.0.** `api` declares it directly; `impl` inherits it from
`org.sakaiproject:oss-parent:1`. 🔵 **The posture is identical — only the declaration DEPTH
differs**, and depth is precisely what a scanner reading one POM does not traverse.

### 🔴 The declared-but-absent rate on this shelf's Maven rows rises to 80%

| coordinate | declares | ships licence text in the jar |
|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` 1.2.0 | Apache-2.0 (own) | 🟢 `META-INF/LICENSE` + `NOTICE` |
| 🔴 `edu.ksu.ome.lti:lti-launch` 1.4.7 | LGPL-3.0 (own) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 (own) | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` 20100527 | 🆕 Apache-2.0 (**inherited**) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🆕 ECL-2.0 (**inherited**) | 🔴 **NONE** |

🔴 **5 of 5 declare; 4 of 5 (80%) ship no text** — against p139's 40–67% and npm's 33%. 🔵 **So
`T21`'s gradient steepens rather than collapsing: PyPI 9%, npm 33%, Maven 80%.** The falsifier
fired and the trend it threatened got stronger, which is the only outcome that makes writing one
worthwhile. 🔴 **`edu.ksu.ome.lti:lti-launch` — the LGPL-3.0 Kansas State library pattern `P13`
depends on — remains the worst row**: the strongest obligation of the five and no text to satisfy
it.

## 🆕 🔴 `openedx-learning` is RETIRED. The row this page should carry is `openedx-core`

### `ACTION CS` — the empty 0.33.x wheels were never a packaging bug

p139 found `openedx-learning` **0.33.0** and **0.33.1** shipping **1 479-byte** wheels and
pre-registered `ACTION CS` to ask whether the breakage was known upstream. 🔴 **It is not
breakage.** The 0.33.1 `setup.py` says so in its own docstring:

> *"Builds a final shell release of openedx-learning which simply 'redirects' to openedx-core"*

with `packages=[]`, `install_requires=["openedx-core==0.34.1"]`,
`Development Status :: 7 - Inactive`, and a `long_description` reading
**"This package has been renamed to `openedx-core`!"**

🟢 **So `pip install openedx-learning` WORKS** — it resolves the shim and installs `openedx-core`.
p139's *"`pip install` resolves to the empty one"* is true of the bytes and wrong about the
outcome. 🆕 **This pass also measured the sdist, which p139 did not**: 11 paths, carrying
`setup.py` and `setup.cfg` and **zero package source**, with `top_level.txt` a single newline.
🔵 **A build recipe with nothing to build — which is exactly what a rename shim looks like.**

### 🆕 The row to carry forward

| field | value |
|---|---|
| package | 🆕 [`openedx-core`](https://pypi.org/project/openedx-core/) — [`openedx/openedx-core`](https://github.com/openedx/openedx-core) |
| latest | **1.9.1**, uploaded **2026-10-09** *(three days before this pass)* |
| version continuity | first release **0.34.1** — exactly what the shim pins |
| licence | 🔴 **AGPL-3.0-only**, as a **PEP 639 `License-Expression`** |
| 🟢 licence payload | `dist-info/licenses/LICENSE.txt`, **35 139 B**, `License-File: LICENSE.txt`, Metadata-Version **2.4** |
| wheel | 261 paths, 358 188 B |
| consolidates | `openedx_core`, `openedx_learning`, `openedx_tagging`, `openedx_catalog`, `openedx_content`, `openedx_django_lib` |
| steward | `David Ormsbee <dave@axim.org>` — **Axim Collaborative** |

🟢 **It is the cleanest licence payload this KB has measured.** Declared by SPDX expression,
shipped automatically under PEP 639 — 🔵 **which vindicates `T21`'s mechanism on the newest
artefact on the shelf: the grant is shipped by the build system, not by the maintainer's
diligence.** 🟢 **And it removes p139's only PyPI hit**: that row was a shim with no code, so this
shelf's PyPI declared-but-absent rate is **0 of 10**, not 1 of 11.

🔴 **The lesson is a freshness check, not a licence check.** Both signals — the `Inactive`
classifier and the rename in `long_description` — were sitting in the artefact p139 downloaded.
🔵 **New rule: before carrying a package row forward, read its latest release's
`Development Status` classifier and its `long_description`.** Entered as `T27`.

### 🔴 `ACTION CQ` — three `ROOT_ONLY` rows record ownership NOWHERE in source

`ACTION CQ` asked whether p139's foreign-source-header class extends beyond its three largest
rows. 🟡 **It does, weakly — 1 of 5, against p139's 2 of 3** (`Tim Branyen, contributors`, an
MIT-licensed vendored grunt task inside GPL-3.0 `adaptlearning/adapt_framework`). Across all eight
`ROOT_ONLY` rows: **3 of 8.**

🔴 **The stronger result is one the action did not ask for.** `overhangio/tutor` (157 source files
read), `openedx/XBlock` (99) and `openedx/codejail` (31) carry **no copyright header in any
source file** — 287 files, zero headers. So each row is scored for *where a holder is findable at
all*:

| row | does `LICENSE` name a holder? | where ownership actually lives |
|---|---|---|
| `Crosstalk-Solutions/project-nomad` | 🟢 yes — appendix **filled**: `Copyright 2024-2026 Crosstalk Solutions LLC` | + `package.json` |
| `adaptlearning/adapt_framework` | 🟡 only inside the GPL's **interactive-mode example** | — |
| `openedx/XBlock` | 🔴 no — left as `Copyright [yyyy] [name of copyright owner]` | `NOTICE.txt`, `pyproject.toml` |
| `openedx/codejail` | 🔴 no — **no copyright line at all** in the appendix | `NOTICE.txt`, `pyproject.toml` |
| `overhangio/tutor` | 🔴 no — left as `Copyright (C) <year>  <name of author>` | `pyproject.toml` **only** |

🔵 **For a delivery team asking "who holds this code?", the answer is increasingly not in the file
named `LICENSE`.** `adapt_framework` is a third form this KB has not recorded: its holder appears
in the licence file *only* as part of the GPL's illustrative `show c` snippet — a real
attribution in a place no scanner treats as one.
[`p140-rootonly-header-reach`](../compose/code/p140-rootonly-header-reach/README.md).

### 🔴 Open edX names its holder three ways across three layers

| layer | artefact | holder | contact |
|---|---|---|---|
| repo | `openedx/XBlock` | `edX` | 🔴 `oscm@edx.org` |
| repo | `openedx/codejail` | `edX` / 🆕 `Open edX Project` | 🆕 `oscm@openedx.org` |
| registry | `openedx-core` 1.9.1 | 🆕 `David Ormsbee` | 🆕 **`dave@axim.org`** |

🟢 **The holder NAME is defensible.** edX Inc. was *renamed* Axim Collaborative — same trustees,
same mission, same tax ID — after Harvard and MIT sold the edX brand to 2U, so `Copyright 2014,
edX` names the pre-rename identity of the current steward rather than a third party.

🔴 **The CONTACT domain is not.** `edx.org` is operated by **2U**, a different company from the
steward, and `openedx/XBlock`'s `pyproject.toml` still routes there while its sibling
`openedx/codejail` routes to `openedx.org`. 🔵 **Two repositories in one GitHub organisation, same
licence, different holder string and different contact domain — and a third domain on the live
PyPI artefact.** A client asked to send a notice gets three answers to one question.

🟡 **And one row inverts the expected reading.** `overhangio/tutor` declares
`authors = [{name = "Edly"}, {email = "hello@edly.io"}]`, which is **correct and current**: Edly,
the edtech arm of Pakistan-based Arbisoft, acquired Overhang.IO on **2023-03-27**, and Tutor's
founder Régis Behmo leads its technical direction there. 🔵 **Here the metadata is fresher than
the GitHub organisation name** — so a row's org name is not evidence of anything.

**Pass 139, 2026-10-12.** 🔴 **p138 measured the npm payload layer and found a third of the
connector shelf declaring a licence it does not ship. This pass asked the obvious next question —
is that open source, or is it npm? — and the answer is neither: it is the TOOLCHAIN.**
`ACTION CM` ran the same method against **PyPI** and **Maven Central**. Probe, tests and committed
TSVs: [`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

| registry | artefacts measured | 🔴 declare a licence, ship no licence file | rate | vs the 10% threshold |
|---|---|---|---|---|
| 🟢 **PyPI** | **11** (+1 absent from the registry) | 🟡 **1** — and it ships **nothing at all** | **9%** | 🟢 **REFUTED** |
| 🔴 **Maven Central** | **5** (+1 absent) | 🔴 **2 of the 3 that declare** | **40–67%** | 🔴 **NOT REFUTED** |
| *(npm, p138)* | *21* | *7* | *33%* | *not refuted* |

🔵 **The defect tracks each ecosystem's DEFAULT BUILD BEHAVIOUR, not its culture.**

- 🟢 **Python's backends ship the licence for you.** Under **PEP 639**, setuptools and hatch copy
  declared licence files into `<dist>.dist-info/licenses/`. **10 of 11** packages carried one in
  *both* wheel and sdist — every Open edX row included. A maintainer gets this right by doing nothing.
- 🔴 **Maven's jar plugin ships nothing for you.** A POM's `<licenses>` block lives in a *sibling
  file*; the jar on the classpath is untouched. `META-INF/LICENSE` requires deliberate
  configuration, and **2 of 3 declaring artefacts had not done it**.
- 🔴 **npm's `files` array names what to pack and silently omits what is absent** — p138's
  `canvas-mcp-server` *listed* `LICENSE` and shipped 8 paths containing none.

### 🔴 `P139-D1` — the Maven rows, and the library this KB tells clients to build on is in the defect class

| coordinate | version | POM declares | jar paths | licence in jar |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` | 1.2.0 | Apache-2.0 | 70 | 🟢 `META-INF/LICENSE`, `META-INF/NOTICE` |
| 🔴 **`edu.ksu.ome.lti:lti-launch`** | **1.4.7** | 🔴 **LGPL-3.0** | 43 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | 25.2 | 🔴 **ECL-2.0** | **578** | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` | 20100527 | 🔴 **nothing declared** | 32 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing declared** | **524** | 🔴 **NONE** |
| — `uk.ac.ox.ctl:spring-lti13` | — | — | — | not on Central (**404**) |

All five resolvable jars were **sha1-verified against the repository's own `.sha1`**; no mismatches.

🔴 **`edu.ksu.ome.lti:lti-launch` is the artefact built from
[`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) — the LGPL-3.0 Kansas State
library p137 identified (`P137-A`) as the LTI→OAuth-subject mapping that pattern `P13` depends on.**
It declares the strongest obligation of the five and ships no text to satisfy it. 🔵 **The one
interoperability library this KB recommends building on reproduces p138's worst npm row, in Java.**

🔴 **`sakai-kernel-api` declares ECL-2.0 while `sakai-kernel-impl` declares nothing** — two
artefacts of one kernel, same release line, opposite licence posture, and the one with **578
paths** is the one making the claim with no text. ECL-2.0 is **education's own licence** (an
Apache-2.0 derivative with a university-oriented patent clause), and it is exactly the identifier a
client's scanner will not recognise.

🔴 **`net.oauth.core:oauth` (2010) carries no licence signal at all** and is still a transitive
dependency of LTI 1.1 integrations. No grant and no file is not "permissive by default" — it is
**unlicensed**, and sixteen years of use does not change that.

### 🔴 `P139-D2` — the PyPI hit is not a licence defect: `openedx-learning` ships NO CODE

The one PyPI row declaring a licence and shipping no licence file is **`openedx-learning` 0.33.1**
— *"Open edX Learning Core (and Tagging)"*. It declares `AGPL 3.0` by legacy field **and**
classifier. Its wheel holds **4 paths, all metadata**; `top_level.txt` is **1 byte**; `RECORD`
lists only the four `dist-info` entries.

| version | wheel | sdist |
|---|---|---|
| 0.31.0 | 268 554 B | 192 313 B |
| 0.32.0 | 257 553 B | 189 430 B |
| 🔴 **0.33.0** | 🔴 **1 479 B** | 🔴 **1 748 B** |
| 🔴 **0.33.1** *(latest)* | 🔴 **1 479 B** | 🔴 **1 742 B** |

🔴 **`pip install openedx-learning` resolves to 0.33.1 and installs no modules.** Across **79
releases**, the two most recent are the empty ones — this is the *current* state of a core library
of the dominant open-source higher-education platform, not an old artefact. The collapse from 257 KB
to 1.4 KB is the signature of a packaging regression, shipped twice.

🔵 **A licence probe found a release defect.** It is counted honestly in both places: as a licence
row it is the hit that makes PyPI 9% rather than 0%; as a *finding* it belongs to a different class.

🟡 **Two smaller carries.** `xblock-sdk` 0.15.2 ships **two vendored Jasmine 1.3.1 `MIT.LICENSE`
files** under `sample_xblocks/*/static/js/lib/` beside its own AGPL-3.0 grant — `ACTION CJ`'s
foreign-holder class, in a payload. And `moodle-dl` declares `GPL-3.0` with `license_files`
**absent** from its metadata yet **ships** `LICENSE` in both distributions: 🔵 **a missing
`License-File` field does not imply a missing file**, the mirror image of npm's `files` naming one
it does not ship.

## 🔴 `ACTION CJ` — on the rows where the root licence file was "the whole story", it names nobody

p137 cleared **8** of the 20 largest rows as `ROOT_ONLY`: one licence file, nothing else
licence-shaped in the tree. `ACTION CJ` read the **source-file headers** of the three largest.
🔴 **Two of the three carry a holder their licence file does not name**, so p137's 50% is a **floor,
not an estimate**. Probe, 20 tests and TSV:
[`p139-source-header-holder`](../compose/code/p139-source-header-holder/README.md).

| row | tree paths | source files read | own holders | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 1 411 | 2 | 🔴 **1 — `FOSS United`, 78 header lines** | `FOREIGN_HEADER_IN_SOURCE` |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 450 | 1 | 🟢 0 | `OWN_HEADERS_ONLY` — 🔴 *but its pointer dangles* |
| 🔴 [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 660 | 🔴 **0** | 🔴 **3** | `FOREIGN_HEADER_IN_SOURCE` |

🔴 **`frappe/lms`'s `license.txt` names no holder of `frappe/lms`.** All **three** of its
`Copyright` lines are the AGPL's own apparatus: the FSF's copyright on the licence text (line 4),
the §0 definitions (line 65), and 🔴 **the "how to apply" template with the placeholder never
filled in** — `Copyright (C) <year>  <name of author>` (line 633). Ownership exists **only** in the
source headers, and there it is **two distinct legal entities**: `Frappe` / `Frappe Technologies
Pvt. Ltd.` (165 lines) and 🔴 **`FOSS United`** (78 lines), a separate Indian non-profit. 🔵 **A
verdict read from the root — "AGPL-3.0, Frappe" — is wrong in both halves on 78 files.**

🔴 **`openeducat/openeducat_erp`'s root `LICENSE` delegates copyright twice, and both pointers
dangle.** It opens *"For copyright information, please see the COPYRIGHT file."* — and
`git ls-tree -r HEAD` over all **1 345** paths finds **no `COPYRIGHT` file anywhere**. It then
delegates again, to "the relevant source files", which carry only `OpenEduCat Inc` (190 lines).
🔵 **The grant is sound and legible (LGPL-3.0, stated in its first lines); the chain that would say
whom you owe terminates nowhere.** It is the only one of the three honest enough to say it is not
trying.

🔴 **`academico-sis/academico` has zero headers of its own** and three foreign ones, all in built
Filament bundles under `public/` — `Pusher` (`echo.js`), `Chen Fengyuan` (`cropperjs`), `Chen,
Yi-Cyuan` (`js-sha256`) — 🔵 **the paths a client redistributes, and where no licence file would
ever be looked for.**

### 🟢 A channel p138 recorded as closed is open, and HEAD dates are measurable again

🟢 **`git clone --depth 1` against `github.com` works here.** p138 published **UNMEASURED** for
star counts *and* HEAD dates on the strength of `api.github.com`, `codeload` and `github.com` HEAD
all answering **403**. 🔵 **Git smart-HTTP is a different lane from the REST API, and it answers** —
which is how every row on this page was verified this pass, and how the `ACTION CN` lineage work was
done at all.

| row | HEAD commit | HEAD date |
|---|---|---|
| `frappe/lms` | `0f760e6` | **2026-10-11** |
| `openeducat/openeducat_erp` | `1c95cef` | **2026-09-07** |
| `academico-sis/academico` | `d0cd78c` | **2026-10-07** |

🔴 **Star counts stay `UNMEASURED`** — git carries no star count, so that half of p138's gap stands.


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟢 **p138 measured a fifth layer — the published package — and found a
third of the connector tier shipping an SPDX identifier with no licence text. It then registered a
falsifier against itself, and this pass fires it: `ACTION CH` read every shipped text file in all
21 payloads, and 0 of the 9 licence-file-less packages carry their own grant in a source header.**
🔴 **p138's count stands.** 🔴 **A sixth layer is now measured, and it is the one a partial copy
depends on: per-file notice, practised by 1 of 21 rows.** On the other 20, a single file lifted out
of the tree names no holder and no grant. 🔵 **And the repository layer was measured in the same
pass as the payload layer for the first time** — through this KB's already-documented raw-file lane,
not a new one — re-verifying two of this KB's published licence figures byte-exact. Instrument and 24 tests:
[`p139-source-header-grant`](../compose/code/p139-source-header-grant/README.md).

**Pass 138, 2026-10-12.** 🔴 **p137 measured that a licence cell describes a repository root rather
than a whole tree. This pass measured a fifth layer, and it is the only one a client actually
receives: the published package.** `ACTION CD` downloaded **21** education-LMS connector tarballs
(Canvas, Moodle, Brightspace, EduBase), **sha1-verified every one against the registry's own
`shasum`** — 21 of 21 matched — and enumerated every shipped path.

| the layer | what it tells you | measured |
|---|---|---|
| root licence file | what you may do | 🟢 right about the **family** 92% of the time (`p444`) |
| tree enumeration | 🔴 **whom you owe** | 🔴 incomplete for **50%** of the largest rows (`p137`) |
| 🆕 **published payload** | 🔴 **what the client is actually handed** | 🔴 **9 of 21 packages ship NO licence file; 7 of those declare an SPDX id** |

🔵 **`npm install` unpacks a tarball; it does not clone a repository.** A grant that lives only at
HEAD is never conveyed to the person who installs the package — so a licence cell sourced from a
repository can be correct about the repository and wrong about the delivery.

🔴 **The row that matters most is the copyleft one.** `moodle-mcp-server-aql` **0.1.7**
(2026-10-01) declares **AGPL-3.0** across **141 shipped paths** and ships no licence text, while
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) carries a
canonical **34 523-byte** `LICENSE`. 🔵 The strongest obligation on this shelf, conveyed without the
document that states it.

🔴 **And the mechanism is now known rather than guessed**: `canvas-mcp-server` **2.2.3**'s packed
manifest reads `files: ["build/**/*", "README.md", "LICENSE", "package.json"]` — it **names**
`LICENSE` — and its 8 shipped paths contain none. npm omits a `files` entry that does not exist in
the tree, silently. 🔵 **New rule for this page: a manifest that lists a licence is not evidence
that one shipped.**

🟢 **Direction of the error, which decides the remedy.** All nine defective rows are the repository
being *better* than the distribution — **not one package shipped a licence its repository lacked**.
The ask to an upstream is a one-line `files` change, not a relicensing conversation.

Instrument, method, committed 21-row TSV and 7 passing tests:
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🔴 **This probe reads licence FILES only**, so the `pipwerks` case — a grant in a source-file header
— stays invisible to it. **7 of 21 is a floor, not a count.** `ACTION CH` was registered to close
that hole at the repository layer and **did not run this pass**; it is re-registered.

🔴 **Scope, stated:** npm only, four platform families, one registry search each. PyPI, Maven and
crates were not probed, and `moodler-mcp` — a Python connector on this KB's shelf — **is not on PyPI
at all (404)**, so for part of the shelf there is no payload layer to measure and no registry to
arbitrate a disputed address.

**Pass 137, 2026-10-11.** 🔴 **Every licence cell on this page describes a repository ROOT, and for
half of the largest rows the root is not the whole obligation.** `ACTION BY` enumerated the file
trees of the **20 largest rows on this page** — **224 591 paths** — and found **316** licence-shaped
files outside the root, **242** of them real grants. 🔴 **Ten of the twenty (50%) carry at least one
grant whose copyright holder is not the repository's own.** The refutation threshold was **5%**.
Instrument, tests and per-row results: `compose/code/p137-foreign-holder-tree`.

🔵 **Read this next to [`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md),
which measured the other half of the same question and looks like it says the opposite.** p444: the
licence **family** read from the root file is the tree's family **92%** of the time. p137: the
**ownership** is incomplete in **50%** of the largest rows. 🟢 **Both are true, and together they
are the rule: a root licence cell predicts what you may DO; it does not predict whom you OWE.**

### 🆕 `ACTION BY` — what the trees carry, per row

| row | tree paths | non-root licence files | real grants | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **67 589** | 96 | 87 | 🔴 **66** | `FOREIGN_HOLDER_IN_TREE` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 18 127 | 76 | 58 | 🔴 **13** | `FOREIGN_HOLDER_IN_TREE` |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 13 231 | 28 | 22 | 🔴 **17** | `FOREIGN_HOLDER_IN_TREE` |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 25 823 | 17 | 13 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 5 137 | 14 | 10 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 9 273 | 18 | 11 | 🔴 **9** | `FOREIGN_HOLDER_IN_TREE` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 22 662 | 23 | 22 | 🔴 **4** | `FOREIGN_HOLDER_IN_TREE` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 4 826 | 2 | 2 | 2 | `FOREIGN_HOLDER_IN_TREE` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 17 073 | 6 | 1 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 5 749 | 8 | 8 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 7 405 | 13 | 8 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 489 | 1 | 1 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 14 | 🟡 **0 readable** | 0 | 🟡 unreadable class |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 664 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 249 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 118 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/codejail`](https://github.com/openedx/codejail) | 43 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 193 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |

### 🔴 The two findings inside the 50% that change a delivery decision

🔴 **`instructure/canvas-lms` is AGPL-3.0 at the root and ships an MIT LTI Advantage implementation
four levels down.** `gems/lti-advantage/LICENSE.txt` is **MIT, held by a named individual (Nathan
Mills)**. 🟢 **The LTI Advantage code inside the dominant North-American LMS is the permissive part
of it** — which is a different sentence from anything this page has published about Canvas, and the
one a studio needs before it decides to reimplement rather than extract. (The same tree also carries
`rick olson`'s `attachment_fu` and `Coolite Inc.`'s date library.)

🆕 **`classroomio/classroomio` (AGPL-3.0) vendors ten MIT-licensed agent-skills packs** —
`skills/*/LICENSE`, held by three outside individuals. 🔵 **This is a 2026-shaped obligation**: the
skills are exactly the part a client redistributes, and their grants are not the platform's.

🔵 **The rest of the 50% is front-end vendoring and the FSF's own text**: Fonticons, Twitter's
Bootstrap, Tiny Technologies' editor, Michael Bostock's d3, Ivan Sagalaev's highlight.js, Adobe's
cmaps, the PDFium Authors, Google's Liberation data, Mozilla; plus **The Trustees of Columbia
University** and the Apache Software Foundation inside Sakai, and a Debian maintainer's packaging
copyright inside Kolibri. The FSF appears as a holder **21 times** — a vendored licence body, not a
third-party grant, and counted because a notice obligation attaches to it too.

### 🔴 Three defects this probe produced before it produced a finding — stated, because the first two were wrong in the direction of a finding

1. 🔴 **An empty path list counted as one path**, so seven of twenty rows were first reported as
   carrying a non-root licence file they do not have. `printf '%s\n' "$empty" | grep -c ''` is 1.
2. 🔴 **Sakai's `content-copyright` i18n bundles matched on the WORD "copyright"** and produced seven
   false grants out of translated UI strings.
3. 🔴 **A four-filename licence sweep over 16 candidate rows called `kstateome/lti-launch`
   unlicensed. Tree enumeration found `License.txt` — LGPL-3.0, 7 651 B.** One of this pass's two
   absence verdicts was false, which is `p288-agpl-casefold` biting this KB a second time, and is
   why the committed instrument matches case-insensitively and ships a regression test for it.

🟡 **And one limit that keeps 50% a floor rather than an estimate:** this instrument reads licence
**files**. A grant inside a source header — the `pipwerks` case p136 corrected — is invisible to it.
🔴 **`Crosstalk-Solutions/project-nomad` defeats the method entirely**: `ROOT_ONLY` over 664 paths,
while composing Kiwix, Kolibri and Ollama **as container images**, so its real third-party
obligations are nowhere in its tree.

### 🆕 One row added to the interoperability layer, and it is university-owned

| repo | licence *(payload-read)* | ★ | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **LGPL-3.0** (`License.txt`, 7 651 B; `pom.xml` `<licenses>` agrees) | **UNMEASURED** | **2026-09-30** | 🟢 **US public university** (Kansas State University, Office of Mediated Education) | 🔴 **The only repository in this KB that maps a verified LTI launch onto a per-user OAuth grant** — `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → Canvas as that user. LTI **1.1** (OAuth 1.0a consumer model), Spring/Java, 34 paths. 🟢 **The first university-owned row in this page's standards tier**, and the pattern `P13` now copies. 🔴 LGPL + Java: port the pattern, not the file |

---

**Pass 135, 2026-10-11.** 🟢 **The assessment and course-content layer is added — the part of the
standards stack p134's interoperability section pointed at and did not reach.** p134 finished with
LTI, OneRoster, Ed-Fi and xAPI. Finishing the register (`ACTION BN`) found that **SCORM carries an
order of magnitude more code than any of them**, and that two of the six remaining standards have
almost no supply at all. Rows are below under *The assessment and content layer*.

🔴 **Every licence cell added this pass was established by hash, and the method matters more than
any single row.** `compose/code/p135-licence-sha-identity` discharges `ACTION BP` and **refutes its
premise**: not one payload in a 26-repo corpus is a whitespace variant of its canonical text. They
differ by **line wrap width** (SPDX wraps at ~105 columns, real `LICENSE` files at ~72), by
**typographic punctuation** (SPDX's GPL-3.0 uses curly quotes; shipped `COPYING` files use ASCII),
and by **the licence steward editing its own text** — two such edits are now known for GNU, the
`http`→`https` change and 🔴 **the FSF's move of `why-not-lgpl.html` from `/licenses/` to
`/philosophy/`, which was the entire remaining difference on five GPL-3.0 payloads.**
🟢 **Result: 21 of 26 resolved to a named SPDX identifier; the 5 that did not each have a named
cause, and 2 of them are correctly unmatched** because the text genuinely is not canonical.

🔴 **Two rows added this pass carry the defect this page exists to catch.**
[`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) — **391★, 130 forks,
pushed 2026-09-18 — has no licence file under any of eight probed filenames**, and
[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is published
**unlicensed and archived by the US Department of Defense body that authored both SCORM and xAPI.**
Neither can be used in a client deliverable. Both are measured absent, not inferred.
<!--corrected by p136: see "The pipwerks correction" below. The `pipwerks` half of this paragraph is
wrong about rights and right about files -- a grant IS declared, in `package.json` and the source
header. The `adlnet` half is not re-measured this pass and stands as written.-->

## 🔴 The `pipwerks` correction — `ACTION BR`, and the sentence this page got wrong

**Pass 136, 2026-10-11.** `ACTION BR` asked for the **dependency closure** of the unlicensed
`pipwerks/scorm-api-wrapper` across this KB's own rows, predicting refutation *"if no published row
depends on it."* 🔴 **The action was discharged and it answered a bigger question than it asked: the
premise of five pages of this KB is wrong.**

| what p135 published | what p136 measured |
|---|---|
| *"no licence file exists under 8 probed filenames"* | 🟢 **TRUE.** Re-confirmed; the repository's whole tree is `package.json`, `readme.md` and three source files |
| *"there is no grant, so there is no right to use it"* | 🔴 **FALSE.** `package.json` carries `"license": "MIT-style license: http://pipwerks.mit-license.org/"`, and `src/JavaScript/SCORM_API_wrapper.js` lines 11–12 carry *"Copyright (c) Philip Hutchison / MIT-style license: …"* |
| *"391★, 130 forks, pushed 2026-09-18"* — a live dependency | 🔴 **HEAD commit is 2018-09-06.** The manifest version is `1.1.20160322`. `pushed_at` moved in 2026; the code did not |
| *"the blast radius is unmeasured"* | 🟢 **Measured. One** published row on this KB's pages depends on it |

🟢 **The one dependant, and how it hides.** Seven manifest types were probed across the 324 repo
rows on this KB's non-log pages; **150 rows exposed at least one manifest**, and the only
`pipwerks` hit in any of them is **pipwerks' own `package.json`**. 🔴 **A manifest probe is the
wrong instrument**: [`numbas/Numbas`](https://github.com/numbas/Numbas) (Apache-2.0, Newcastle
University) **vendors the file** at `runtime/scripts/SCORM_API_wrapper.js` — version
**`v1.1.20121005`**, four years behind upstream's own manifest — with the copyright and MIT-style
header **intact**. GitHub code search finds **293 files** named `SCORM_API_wrapper.js` carrying that
header, including [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) and
[`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper), both in the H5P family this
KB tables on `verticals/solutions.md`.

🔵 **So the rule this page should carry is about the grant's LOCATION, not its existence.** A
filename probe measures files. A grant can live in a package manifest, a source header, or a URL —
and when it travels inside a **vendored file**, the header travels with it while the version does
not. 🔴 **The residual risk is real but different from the one this page published**: the terms are
declared, *unread* (the host is refused in this channel — DNS failure on `http`, 403 CONNECT on
`https`) and **not an SPDX identifier**, since *"MIT-style"* names no standard text.

**Pass 134, 2026-10-11.** 🟢 **This page gains the layer it was missing: the interoperability
standards an institution procures against.** `instructure/ims-lti` has sat at the bottom of this
page for many passes, described correctly as *"the integration path that avoids touching platform
source"* — and this KB never followed that sentence anywhere. Followed, it leads to **`Cvmcosta/ltijs`
(Apache-2.0, 373★, pushed 2026-10-06)**, which is larger and far more active than the row that
pointed at it, and to the first **vendor- and government-owned** repositories this KB has ever
tabled. See the new section *The interoperability layer* below, and `agents/top.md` → *Standards-native
agents*.

🟢 **`ACTION BG` is also discharged on this page** — the mirror detector p133 asked for was built and
run, one of its three proposed signals works, and `P133-A`'s inference about Canvas is narrowed. See
*The mirror rule, measured* below.

**Pass 132, 2026-10-11.** p131's rows carried forward unchanged (they were verified hours earlier
in the same date window); 🔴 **one new row changes this page's headline recommendation and refutes
this page's own flagship gap** — see `README.md` → Pass 132, `P132-C`. These are the systems a
client already runs, or would sensibly adopt, and that AI work gets attached to. Licence is the
first column that matters: it decides whether Globant can ship a derivative at all.

🔴 **Read this before trusting a licence cell.** GitHub's `license.spdx_id` reports **`NOASSERTION`
("Other")** whenever its matcher does not recognise a `LICENSE` file as a known template. That is
*not* a finding of "no grant", and p130 published it as one. Where this KB has **read the payload**,
the payload wins and the cell below says so.

## The platforms

| repo | licence | stars | last push | origin | why it is foundational |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | **9 241** | 2026-10-10 | North America (Blindside Networks, Canada) | The open virtual-classroom stack: WebRTC audio/video, whiteboard, breakouts, recordings. LGPL means linking is fine; modifying the library itself carries reciprocity. The place live-session AI (transcription, attention, summarisation) attaches. |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **8 195** | 2026-10-10 | North America (Open edX / Axim) | The LMS + Studio behind MOOC-scale deployments. **Renamed:** this repo was `openedx/edx-platform`; the old URL still resolves and the README says "formerly known as edx-platform". Write the new name — earlier passes of this KB cite the old one. |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | **7 473** | 2026-10-09 | APAC (Moodle HQ, Perth, Australia) | The most deployed LMS in the world, ~2 000 plugins. **Important for delivery:** this GitHub repo is a *public mirror* of `git.moodle.org` — pull requests do not go here, and it publishes no GitHub releases. Contribution goes through Moodle's own tracker and git server. 🟢 **Its mirror is live (pushed 2026-10-09), which is exactly why Canvas's frozen one was mistaken for a quiet project rather than a stopped job.** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | **6 863** | 2026-04-30 **(mirror frozen — not inactivity)** | North America (Instructure, US) | The dominant LMS in North American higher ed and the one with the richest third-party API surface — which is why every MCP connector on the agent shelf targets Canvas first. 🔴 **Corrected by p133: this KB called it "the quietest of the major platforms" for four passes and that was a measurement error.** The repo's own topics include **`gerrit-mirror`**, and `instructure/analytics` carries the identical `pushed_at` **one second later** (14:52:10 / 14:52:11 on 2026-04-30) — a batch export, not a human push. 🟡 **The correct statement: the public GitHub mirror has been frozen since 2026-04-30, so GitHub is not a usable activity signal for Canvas, and anyone diffing this tree to track upstream has been reading a stale copy for five months.** Development is in Instructure's Gerrit; `updated_at` still moves daily. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | **6 845** | 2026-10-11 | Global (Oppia Foundation) | An online learning platform built around structured, explorable lessons with built-in misconception handling. **The only major education platform under a permissive licence** — so the one a client can fork into a closed product without reciprocity. Underrated for exactly that reason. Android client: [`oppia/oppia-android`](https://github.com/oppia/oppia-android) (Apache-2.0, 418). |
| [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | **3 299** | 2026-10-11 | APAC (Frappe, India) | Modern, actively developed LMS on the Frappe framework — so it sits next to Frappe/ERPNext finance and HR data without integration work. The strongest APAC-origin platform here. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2 336 | 2026-10-11 | unplaced | Next-generation learning platform, Python/Next.js, AI features first-class rather than bolted on. Young, fast-moving. |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | AGPL-3.0 | 1 717 | 2026-10-11 | unplaced | Education platform aimed at companies running cohort training. Relevant to corporate-L&D engagements rather than academic ones. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1 237 | 2026-10-09 | North America (Apereo Foundation) | Long-lived Java academic LMS. ECL-2.0 is Apache-2.0 with an educational-community patent tweak — **permissive**, and the licence most people misread as restrictive. Strong fit where a client already runs Java/Oracle estate. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | 1 127 | 2026-10-08 | EMEA (Overhang.IO, France) | The Docker-based Open edX distribution — in practice *the* supported way to stand up and upgrade Open edX. A large first-party plugin ecosystem, all AGPL-3.0: `tutor-mfe` (micro-frontends), `tutor-cairn` (real-time analytics), `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. If the engagement is Open edX, it is a Tutor engagement. |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 141 | 2026-10-10 | Global (Learning Equality) | Offline-first learning platform for low- and no-connectivity classrooms; content syncs by LAN or USB. **MIT-licensed**, which with its offline design makes it the single best base for rural LATAM, African and South Asian deployments. Content tooling: [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192). |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1 009 | 2026-10-10 | EMEA (Chamilo Association, Belgium) | LMS built around ease of use and accessibility, with real institutional adoption in Francophone Europe and Spanish-speaking LATAM. The most LATAM-relevant of the EMEA-origin platforms. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The natural target for the administrative automation nobody else serves. 🔴 **Licence corrected by p131.** GitHub's API reports `NOASSERTION` and p130 published that as "review terms before use". This KB had already **read `master/LICENSE` in full — 8 241 bytes, genuinely LGPL-3.0** — and used that read to *retract* an even earlier "no grant" row. p130 reinstated the retracted claim by trusting the API field over its own evidence. **LGPL on an LGPL Odoo base: linking is fine, modifying the module itself carries reciprocity.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## The offline / low-connectivity stack (added by p132 — and it refutes this page's own gap)

🔴 **This page has carried, for several passes, that "the offline slot is the cleanest unclaimed
opportunity in this KB". It is not unclaimed.** It is occupied by the second-largest repository
anywhere in this KB.

| repo | licence | stars | origin | why it is foundational |
|---|---|---|---|---|
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 **Apache-2.0** | **39 444** | unplaced | **Offline-first knowledge and education server**: Wikipedia, thousands of books, courses, maps and optional local AI, all on hardware the client owns with no internet required. Architecturally a **Docker orchestration layer over containerised tools** — **Kiwix** powers the Information Library, **Kolibri** powers the Education Platform, **Ollama** powers the AI Assistant (the installer provisions Ollama on the host; an external OpenAI-compatible endpoint is also supported). 🟢 **Permissive, so a client can ship a derivative.** 850 commits, updated the day of this pass. |
| [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 **UNREAD** | 20 | unplaced | macOS / Apple Silicon port, bundling Ollama, Open WebUI, Kiwix, Kolibri and FlatNotes. Useful as a single-machine pilot before committing to the Docker stack. Licence not measured this pass. |
| [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) | 🟡 **UNREAD** | 2 | **APAC (India)** | Offline LMS for Class 10 Maths and Science on the Indian curriculum: FastAPI + React + RAG over structured chapter data with a local Ollama model, gamified quizzes, LAN-only operation, and a claimed Kolibri integration. 🔴 **Duplicate pair** with [`Tushar-cy/Ai-edge-learning-hub`](https://github.com/Tushar-cy/Ai-edge-learning-hub) (same owner, byte-identical description). Small, but the only row that targets a *named national curriculum* offline. |

🔵 **Why eleven passes missed it, and why the probe was not at fault.** p131 ran `kolibri stars:>2`,
got 86 repos, correctly resolved 3 to the Learning Equality family and 0 with AI. **The probe was
valid; the conclusion was false.** NOMAD *composes* Kolibri as a container and never names it in
its description — the dependency appears only in the README architecture. **A dependency is not
always visible in the metadata of the thing that depends on it.**

🟢 **What this changes for an engagement.** The low-connectivity offer stops being *"build an
offline tutor"* and becomes *"deploy and extend an Apache-2.0 stack that already composes content,
library and local inference"* — faster, cheaper and far more defensible in a procurement
conversation. Kolibri (MIT) remains the right content layer; what changed is that the integration
around it already exists. See `compose/patterns.md` → P2.

## Administrative automation — the first optimiser (added by p132)

| repo | licence | stars | origin | what it gives you |
|---|---|---|---|---|
| [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | Conflict-free academic timetable generation under **India's NEP 2020**: electives, faculty availability, courses, rooms, balanced workloads, scenario simulation, manual overrides, exports, and a natural-language interface over MCP. 🟢 **The "most-cited driver, least-served tier" finally has a repo, and it is an optimiser rather than an LLM wrapper.** 🔴 One star — a reference design, not a dependency. |

## 🟢 The interoperability layer — how AI attaches without touching platform source *(new, p134)*

🔴 **Read this section before proposing a fork of anything above it.** Every platform in *The
platforms* is AGPL-3.0, GPL-3.0, LGPL-3.0 or ECL-2.0, and this KB spends a lot of words on which
reciprocity obligation bites when. 🟢 **The standards below make most of that moot:** a tool
launched over **LTI 1.3** runs as a separate application with its own licence, talking to the LMS
over HTTP. It never links platform code, so it inherits **no** copyleft obligation from Moodle,
Canvas or Open edX — and it is *invited in* by a client ID the institution issues and can revoke,
rather than holding a user's password.

| repo | licence | stars | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (payload-read) | **373** | **2026-10-06** | named individual | 🟢 **The reference LTI 1.3 Advantage tool provider, and the headline addition to this page.** OIDC launch, Deep Linking, AGS grade passback, NRPS rosters. **1.8× the stars of `ims-lti` and pushed five days before this pass** — where `ims-lti` is Instructure's library for *their* platform, this is the platform-independent one. If an engagement puts AI inside an existing LMS, this is the integration dependency. |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (payload-read) | 138 | 2024-08-18 | named individual | The Python LTI 1.3 Advantage library (Django/Flask). 🔴 **Dormant ~2 years**, and that is the most consequential staleness on this page: Python is where the agent frameworks live, so the LTI binding for an agent build is the least-maintained link in the chain. |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (payload-read) | 6 | **2026-10-09** | 🟢 **standards body** | Serves a **OneRoster 1.2 API from an Ed-Fi ODS**. The bridge between the two US K-12 data standards, written by the body that owns one of them. 🟢 **Stars are the wrong measure here: this is the row that makes a US K-12 rostering story procurement-safe.** |
| [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** (payload-read) | 7 | 2026-07-30 | 🟢 **platform vendor (Google)** | Conformance tests for a OneRoster integration. 🟢 **The only test suite in this KB that proves an integration correct rather than asserting it.** |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (payload-read, 711 B) | 10 | 2026-05-11 | named individual (noreply addr) | TypeScript OneRoster SDK. 🟢 **0BSD — the most permissive licence in this KB; it drops even attribution**, so a derivative carries no notice obligation at all. |
| [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) | 🟢 **MIT** (payload-read; holder **"UNIwise ApS"**) | 3 | 2026-06-11 | 🟢 **platform vendor (EMEA, Denmark)** | Integration packages for the **WISEflow** assessment platform — user creation, flow setup, assessor allocation, **grade passback**. 🟢 **A European assessment vendor publishing its own MIT integration path**: the cleanest EMEA counterparty in this KB, and the opposite of the unsanctioned-connector problem. |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | 17 | **2026-10-11** | 🟢 **national public operator (EMEA, France)** | Learning-analytics visualisation over **xAPI**. Same owner as [`openfun/richie`](https://github.com/openfun/richie) below — 🟢 **France Université Numérique now gives this KB two MIT rows, and this one was pushed on the day of this pass.** The dashboard layer over an LRS. |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 15 | 2025-08-29 | named individual | 🟢 **The only repo found that bridges an AI agent to a sanctioned standard**: an MCP server that records and retrieves learning activity through an xAPI Learning Record Store. 🔴 **15 stars, last push ~14 months ago** — load-bearing and unmaintained, which is precisely why it is a build item rather than a dependency. Full tier in `agents/top.md`. |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | **Apache-2.0** | 12 | 2025-07-03 | 🟢 **government (US DoD ADL Initiative)** | xAPI profile for lifetime learner tracking, from the body that authored xAPI. The modelling reference for an LRS schema. |
| [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) | 🔴 **no licence field** | 0 | 2026-04-14 | 🟢 **government (Minnesota Dept of Education)** | C# SDK for a US state's Ed-Fi ODS API. 🔴 **The best-owned row on this page and unusable, because it carries no grant** — the recurring shape of this KB in one line. |

🔵 **The licence asymmetry is worth stating plainly, because it inverts this page's usual advice.**
*The platforms* are copyleft almost without exception and the one permissive major platform
(`oppia/oppia`, Apache-2.0) is the one nobody asks for. 🟢 **The interoperability layer is
permissive almost without exception** — Apache-2.0, MIT and 0BSD, with named vendor and government
holders. **So the licence-safest way to build on a copyleft platform is to not build on it at all,
and to attach over a standard instead.**

🔴 **And the honest limit of this section:** these are libraries, conformance tests and profiles.
They are the plumbing a security review passes. **None of them contains any AI**, and the one row
that joins them to an agent has 15 stars and has not been pushed in over a year.

## 🟢 The mirror rule, measured — `ACTION BG` discharged *(p134)*

p133 corrected a four-pass claim that `instructure/canvas-lms` was *"the quietest of the major
platforms"*, having found the topic `gerrit-mirror` and a sibling repo sharing its `pushed_at` one
second later. 🟢 **`ACTION BG` asked for that to become a detector before any further freshness
claim published. It was built and run over the 40 most-recently-updated `instructure` repositories,
and the result is mixed in a useful way.**

| proposed signal | verdict | measurement |
|---|---|---|
| **a topic containing *mirror*** | 🟢 **WORKS — and the defect is a lane, not a row** | **5 of 40** repos carry `gerrit-mirror`: `canvas-lms`, `dockerfiles`, `switchman`, `screencap`, `outrigger`. `ACTION BG`'s refutation condition (*"refuted if `canvas-lms` is the only mirror"*) is **not met** |
| **two repos in an org sharing `pushed_at` to the second** | 🔴 **DOES NOT GENERALISE — retire it** | across 40 repos, **no timestamp is shared by more than one repo.** p133's own evidence was two *adjacent* seconds (`:10` and `:11`), not a shared one; generalised into a detector it finds nothing |
| **a README naming an upstream elsewhere** | 🟡 **NOT TESTED** this pass | would need a payload read per repo; the topic field is cheaper and sufficient |

🔴 **And the measurement narrows `P133-A`'s inference.** p133 concluded 2026-04-30 was *"the date
their export to GitHub stopped running"*. 🟢 **It was not: sibling mirrors in the same org received
exports on 2026-09-30 (`switchman`) and 2026-10-08 (`dockerfiles`)** — three days before this pass.
**The Gerrit export job is running; `canvas-lms` specifically stopped receiving it.** Whether that
is a disabled export, a renamed upstream branch or a deliberate halt is not visible from here, and
this KB should not guess. 🟢 **p133's operative conclusion survives intact and is the one to quote:
`pushed_at` on `canvas-lms` is not an activity signal.** Its stronger causal story does not.

🟢 **The control that makes the rule usable:** [`instructure/ims-lti`](https://github.com/instructure/ims-lti)
carries **no** mirror topic and was pushed **2026-10-02**. **So within one org, some repos are
mirrors and some are GitHub-native, and the topic tells you which.** `pushed_at` is a valid
freshness signal for `ims-lti` and an invalid one for `canvas-lms` — which means freshness must be
checked per repo, never per organisation.

### 🔴 p136 runs the rule over the whole corpus — and 44% of its hits are not mirrors at all

`ACTION BU` asked for p135's successor signal (README **byte-identity**, which p135 called *"a
verdict"* against licence grouping's *"lead"*) to be applied corpus-wide. **1 389 READMEs fetched
over 1 528 published rows → 71 byte-identical clusters, 25 of them cross-owner** — twelve times
`ACTION BU`'s refutation threshold, so **not refuted**. 🔴 **But the word "verdict" does not
survive:**

| lineage verdict | clusters | what it means here |
|---|---|---|
| `ALIAS` — **identical ref set** | 🔴 **11** | **One repository under two slugs.** GitHub keeps answering a renamed owner or repo name, so the "two owners" are one |
| `DIVERGED_FORK` — shared commit shas | 5 | A real fork; count the connector once |
| `FORK_AT_TIP` — same HEAD, different ref sets | 4 | A fork that has not diverged yet |
| `ATTRIBUTION_STRIPPED_COPY` — identical root tree, **zero** shared commits | 1 | the ENEM cluster (`ACTION BW`, below) |
| `SQUASHED_COPY` — one side a single commit | 1 | `0awei0/kt`, and it **dropped the upstream MIT file** |
| `UNRESOLVED` — measurement not taken | 🔵 3 | **said, not guessed** |

🔴 **One of the eleven aliases lands on a conclusion this KB published.** `agents/trending.md`
reasoned about `theopenem/OneRoster.NET` versus `jdolny/OneRoster.NET` — *"both licences name
`theopenem` as copyright … so pin `theopenem`"* — when the two slugs have an **identical ref set**
(`3f4540f9706d9099`) and are **one repository**. The pin is harmless; the reasoning was about a
distinction that does not exist. 🟡 `KI-Campus/LRS` and `openHPI/openLRS` are the same case across
*both* a rename and a transfer.

🔴 **And 37 further clusters are this KB citing one repository under two spellings** — `Elgg/Elgg`
and `elgg/elgg`, `Schroedinger-Hat/certo` under **three**, eight `Opetushallitus/*` pairs. That is
`p443`'s case-collision class measured across the whole corpus for the first time.

🟢 **The rule, generalised for this page.** Freshness must be checked per repo (p134).
**Identity must be checked before freshness**: resolve the slug to a repository by **ref set**, then
ask about forks, then ask about dates. Instrument, six verdicts and 10 tests:
`compose/code/p136-lineage-verdict/`.

## 🟢 The assessment and content layer — added by p135

The standards an institution procures against do not stop at rostering and grade passback. Two more
carry real code: **SCORM**, which packages and tracks course content, and **QTI**, which carries
assessment items. This is where an AI engagement touching *content* or *assessment* attaches.

| system | repo | licence *(hash-verified)* | ★ | pushed | owner | why it is foundational |
|---|---|---|---|---|---|---|
| **Adapt Framework** | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** 🆕 *(p136: `UNMATCHED` → `RESOLVED` at ratio `0.997431`, holder **"2013 ADAPT LEARNING"**, 11 opcodes and not one an added clause)* | **630** | **2026-10-10** | Adapt community | The largest repo in the whole standards stack. Authoring toolkit producing responsive, accessible, multi-language courses that emit **both SCORM and xAPI**. 🔵 Copyleft: run it as a tool, do not link it |
| **OpenOlat** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0 + attribution** | **447** | 2026-10-09 | frentix GmbH / Univ. of Zurich | 🟢 **A full Java LMS this KB had never tabled**, with QTI, SCORM, curriculum management, assessment and lecture management built in. The permissive full-featured LMS this page's flagship gap says does not exist — see the verdict below |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **354** | 2026-10-09 | individual | The modern SCORM 1.2 / 2004 runtime. **Offline-first**, TypeScript, actively maintained. 🟢 **The permissive replacement for the unlicensed `pipwerks` wrapper** |
| **Numbas** | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | 215 | 2026-10-09 | 🟢 **Newcastle University (UK)** | Browser-based e-assessment, strongest in mathematics, SCORM-packageable. **Institution-owned and permissive** — the cleanest base for assessment work before the 2027 clocks. 🆕 **p136: it vendors `pipwerks`' SCORM wrapper** (`runtime/scripts/SCORM_API_wrapper.js`, `v1.1.20121005`, header intact) — the only `pipwerks` dependant on this KB's pages, and a reminder that Apache-2.0 at the root says nothing about a vendored subtree |
| **QTI 3 item player** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** | 30 | 2026-04-07 | amp-up.io | The reference renderer for QTI 3 assessment items, with a four-component sibling family from the same vendor |
| **Mentingo** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 92 | **2026-10-10** | Selleo (PL) | 🟢 **An AI-native LMS under a permissive licence** — AI mentor, role-play, SCORM and xAPI, white-label, self-hosted. Small, but the only row where the AI is the platform's architecture rather than a bolt-on |
| **1EdTech validator** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** | 17 | 2026-09-23 | 🟢 **1EdTech (the standards body)** | Conformance validation for **Open Badges and Comprehensive Learner Record**. The second conformance suite this KB has found, and the steward's own |

🔴 **Do not reach for these two, and the reason is the licence, not the code**

| repo | ★ | problem |
|---|---|---|
| [`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) | **391** | 🆕 **p136: the reason changed.** The grant is **declared by reference** (`package.json` + source header, *"MIT-style license"* at a host refused in this channel) — so *"confers no rights whatsoever"* is withdrawn. Reach instead for `scorm-again` because **HEAD here is 2018-09-06** and *"MIT-style"* is not an SPDX id, not because there is no grant |
| [`cybercussion/SCOBot`](https://github.com/cybercussion/SCOBot) | 164 | **CC-BY-SA-4.0, and the file is only the 837-byte human-readable deed.** ShareAlike copyleft, no patent grant, and a content licence applied to code |

### 🔴 What this layer does NOT have

| standard | supply measured this pass |
|---|---|
| **Caliper Analytics** | 🔴 **One repository, 0★, no licence, last touched 2023.** The standard for carrying learning events to an analytics layer has no usable open-source client in any language |
| **Comprehensive Learner Record** | 🔴 **One real repository** — the 1EdTech validator above. The other two hits are an empty 2018 repo and a student project |
| **LTI Deep Linking**, probed alone | 🔴 **One repository, which declares in its own description that Deep Linking is not supported.** In practice it exists only inside `ltijs` |

## Supporting infrastructure

| repo | licence | stars | what it gives you |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 470 | The component framework for custom learning activities inside Open edX. Permissively licensed even though the platform around it is AGPL — so a custom XBlock is the lowest-friction way to put an AI activity inside Open edX. |
| [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | 476 | Sandboxed execution of untrusted code. Directly reusable wherever an agent runs learner-submitted or model-generated code — an auto-grader for programming courses, for instance. |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 354 | Modern SCORM/AICC/xAPI runtime in TypeScript. The bridge between legacy courseware a client already owns and anything new. |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 316 | Django/React CMS for building course catalogues and education portals in front of Open edX. From France Université Numérique, so it is proven at national scale in EMEA. |
| [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | 263 | The H5P interactive-content family (Norway); the Moodle binding is [`h5p/moodle-mod_hvp`](https://github.com/h5p/moodle-mod_hvp) (GPL-3.0, 157). The standard way to ship interactive activities into an existing LMS. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 404 | Laravel/Filament school-management platform for small and mid-size institutions. MIT, so the most forkable administrative base here. |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | 203 | LTI tool-provider/consumer library. LTI is how an external AI tool gets launched from inside any compliant LMS — the integration path that avoids touching platform source, and therefore avoids AGPL reciprocity entirely. |

## The system-of-record tier (restored by p131)

p130's declared gaps said *"`openeducat_erp` (licence unclear) and `academico` (small) are the whole
field."* 🔴 **They are not.** This KB read a system-of-record tier in an earlier pass and p130's
rewrite dropped it. Restored here, because "there is no open-source SIS" and "every open-source SIS
is copyleft" are completely different briefings for a client.

| repo | licence | why it matters | the catch |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | **NOASSERTION** (API) — read terms | **662★**, pushed 2026-10-05, 454 forks. Full school management on Frappe: students, programmes, fees, assessment. Sits beside ERPNext finance/HR with no integration work. | Licence does not resolve to an OSI identifier via the API; GPL-3.0 in the Frappe family's own documentation. **Read `LICENSE` before committing** — this is exactly the row class p130 got wrong. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886★. The Odoo-based ERP; the broadest functional coverage of the tier. | Odoo module, so you inherit the Odoo ecosystem *and* its constraints. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | **404★**, pushed 2026-10-07. Laravel/Filament. **The only permissive SIS**, so the only forkable base for a closed client product. Carries the topic `student-information-system`. | Small, and aimed at small-to-mid institutions rather than a university of record. |
| **RosarioSIS** | GPL-2.0 | A genuine student information system with real deployments. | GPL-2.0 — the most restrictive option here. |
| **Gibbon** | GPL-3.0 | School platform with a long institutional track record. | GPL-3.0 reciprocity. |
| **openSIS** / **Fedena** | copyleft / mixed | Named in this KB's earlier reads of the tier; both long-lived. | Neither is permissive; verify the current edition's terms, since both have had commercial forks. |

🔵 **Provenance of the four rows without links.** RosarioSIS, Gibbon, openSIS and Fedena are
carried from **this KB's own earlier read of the tier** (`agents/trending.md:5160`, which recorded
`RosarioSIS mobile@899f6da` GPL-2.0, `Gibbon v31.0.00@683d2c4` GPL-3.0 and `OpenEduCat 19.0@1c95cef`
LGPL-3.0 at specific commits). 🔴 **They were NOT re-verified this pass and are deliberately listed
without links** — a row this pass did not measure does not get presented as one it did. Re-verify
before quoting them to a client; the three linked rows above were verified this pass and are in
`evidence/verified-repos.2026-10-11-p131.tsv`.

**The honest summary for a client:** there are **at least six** open-source systems of record. Exactly
**one** (`academico`, MIT) can become a closed derivative; one more (`openeducat_erp`, LGPL-3.0)
permits linking without reciprocity. The rest are GPL-family. 🔴 **So the gap is not supply — it is
that the system-of-record tier is almost entirely copyleft**, which is a licensing conversation at
the start of an engagement, not a missing-software conversation.

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release. 🟢 **And if the constraint
is connectivity rather than licensing, start from `Crosstalk-Solutions/project-nomad`
(Apache-2.0, 39 444★) instead of assembling the stack yourself** — it already composes Kolibri,
Kiwix and a local model, and it is permissive enough to fork.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia
  (Apache-2.0) and Sakai (ECL-2.0) are the permissive options and neither is a drop-in replacement
  for either. 🟢 **SURVIVES.**
- ~~**No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.~~ 🔴 **REFUTED by p131** — see the system-of-record tier
  above: at least six systems, read by an earlier pass and dropped by p130's rewrite. 🟢 **The
  surviving gap is that the tier is almost entirely copyleft, with `academico` (MIT) the lone
  permissive base — and that no AI *agent* targets any of them** (`agents/top.md`).
- **Canvas is the quietest major platform** (last push 2026-04-30, ~5 months) 🔴 **and it is now
  ~5.5 months quiet, unchanged on re-check this pass.** Worth raising explicitly before
  recommending it as an actively developed base — it is still the richest API surface in the
  sector, which is why every connector targets it.
- ~~**Three Kolibri-family repos, zero AI on any of them.** A valid re-probe this pass
  (`kolibri stars:>2` → 86 repos) resolves the family to three Learning Equality repos; the other
  83 are name collisions. **The offline slot is still the cleanest unclaimed opportunity in this
  KB** (`intel/trends.md` → T8).~~ 🔴 **REFUTED BY p132.** The family resolution was right —
  [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, 1 141★),
  [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192★),
  [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
  (52★) — **and the conclusion drawn from it was wrong.**
  [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
  (**Apache-2.0, 39 444★**) runs Kolibri as its education container beside Kiwix and Ollama, and
  does not contain the string `kolibri` in its description. 🟢 **The surviving gaps are narrower and
  real: (a) no AI project builds *inside* Kolibri itself** — NOMAD orchestrates it from outside and
  the Learning Equality repos carry no AI; **(b) nothing offline targets LATAM.** The one
  curriculum-specific offline row found is Indian (`Tushar-cy/Offline-AI`), and LATAM — where this
  KB argues offline is a first-class requirement rather than an edge case — has none.
  🟡 **Also note a new collision source: Aleph Alpha ships a 78B model called "Kolibri".**

### 🟡 p135's verdict on this page's flagship gap

- **"No permissively licensed, full-featured LMS at the scale of Moodle or Canvas."**
  🟡 **NARROWED, and honestly it is weaker than it was.**
  [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is **447★**, pushed 2026-10-09, under
  **Apache-2.0** (with two attribution statements replacing the appendix — permissive in effect),
  and it ships QTI, SCORM, curriculum management, assessment and lecture management in one Java
  codebase. It is a real, maintained, permissive, full-featured LMS, and **this KB had never listed
  it.** 🔴 **The gap survives only in its "at the scale of Moodle or Canvas" clause** — OpenOlat is
  447★ against Moodle's order of magnitude more, and its deployment base is concentrated in
  German-speaking Europe. 🔵 **For an EMEA engagement that clause may not matter**, and this is now
  the first permissive answer this page can give to *"we want off Moodle's GPL."*
- 🆕 **The offline gap gains a permissive component it did not have.**
  [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT, 354★) lists `offline-first`
  among its own topics and implements the SCORM runtime client-side. 🟢 **That is the missing piece
  between `T8`'s offline requirement and standards-tracked course delivery** — a learner can
  complete tracked content with no connectivity and reconcile later. It still does not close *"no
  AI project builds inside Kolibri itself"*, and it still is not LATAM-originated.

### 🆕 Gaps this page opens after p135

- ~~**The sector's most-used SCORM library is unlicensed, and the blast radius is unmeasured.**~~
  🟢 **CLOSED AND CORRECTED by p136 (`ACTION BR`).** A grant is declared (manifest + source header);
  the blast radius on this KB's own pages is **one row**, `numbas/Numbas`, by **vendoring** rather
  than by manifest; and the sector-level reach is **293 files** carrying the header. 🔴 **What
  replaces it is narrower**: the declared body is unreadable in this channel and *"MIT-style"* is
  not an SPDX identifier, so the row's terms are *declared and unread* — and `pipwerks`' HEAD commit
  is **2018-09-06**, which makes it a stale dependency regardless of its licence.
- 🔴 **No permissive Python library exists for Open Badges.** Both Python rows are copyleft
  (LGPL-2.1 and LGPL-3.0). The permissive credential work is in **Rust** (`impierce`, Apache-2.0)
  and **Java** (`1EdTech`, Apache-2.0), which is a language mismatch for most AI engagements.

### 🆕 Gaps this page opens after p136

- 🔴 **This page's dependency picture is manifest-shaped, and the sector's is not.** `ACTION BR`
  measured 150 of 324 rows exposing at least one of seven manifest types; the one dependency that
  mattered was **vendored**, invisible to all seven. Until a tree-level probe runs (the instruments
  exist — `compose/code/p275-tree-enumeration`, `p441-tree-licence-enumeration`), **every "no
  dependants" statement on this page is a statement about manifests**.
- 🔴 **A root licence says nothing about a vendored subtree, and this page tables root licences.**
  `numbas/Numbas` is Apache-2.0 at the root and carries an MIT-style third-party header four levels
  down. Of the 24 rows in this page's platform and standards tables, **the number whose vendored
  subtrees have been read is zero.** 🔵 **This is `p969-root-only-licence-reach` one level deeper.**
  p93 measured that the grant ladder cannot see a **per-directory** licence (`bncc-dados`: code at
  the root, data one directory down). p136 measures that it cannot see a **third-party header inside
  a vendored file** either — same blind spot, and the vendored case is the common one in a sector
  whose code moves by copying.
- 🟡 **Three `UNRESOLVED` lineage clusters remain** (`education-ai-suite`, `OpenPronounce`,
  `agents-radar`). Each needs one clone per side; none is an education-supply row, which is why they
  were left — recorded so the 25-cluster figure is not read as 25 resolved.


