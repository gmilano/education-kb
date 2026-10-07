---
industry: education
region: Global
updated: 2026-10-07
---

## 🟢 Fortieth pass, 2026-10-07 — the fifth link in the assessment chain stops being a side-car, and the platform shelf is saturated for the ninth consecutive pass

**Licences read first-hand on 2026-10-07** from payload, registry and published artefact, named per row;
title-block classified (`P171`). ⏱️ **Seventh pass of this date.**

🔵 **This file's job is platforms that can be customised with AI on top.** 🔴 **No new LMS, SIS or ERP again
this pass — the platform shelf is saturated and this is the ninth consecutive pass to measure that rather
than assume it.** 🟢 **What changes is the *deployment shape* of the fifth link in the assessment chain that
pass 39 added.**

### 🔴 The mandated platform sweep, recorded in full so silence is not read as coverage

| Sweep | Returned | New platforms |
|---|---|---|
| `open source platform education ERP CRM MIT Apache student information system` | **OpenEduCat** (on Odoo; **LGPL-3.0**, payload `master/LICENSE` 8,241 B, shelved since pass 28) · **Odoo** · **`.LRN`/OpenACS** (**GPL-2.0**, shelved — dotLRN 2.10.1, release date 2024-09-02) · **ERPNext/Frappe** (**GPL-3.0**, shelved) | 🔴 **0** |

🔵 **The sweep's secondary sources repeated two claims this shelf has already corrected or qualified:**

| Claim in the returned summaries | 🟢 What this shelf holds |
|---|---|
| *"OpenEduCat … trusted by 3M+ users, 300 modules, 65 languages, 45 localisations"* | ⚠️ **Vendor marketing from the project's own site, not measured.** 🟢 **The licence is measured: LGPL-3.0 from payload — so it is a *side-car or fork* proposition, not an embeddable component** |
| *"Originally developed at MIT, `.LRN` claims to be the most widely adopted enterprise class open source LMS"* | 🔴 **"Developed at MIT" is an *institution*, not a *licence*** — a confusion this file should name explicitly, because the mandated query contains the word `MIT`. 🟢 **`.LRN`/OpenACS is `GPL-2.0`**, measured at an earlier pass, and lives in **CVS** |

> 🔵 **Worth stating as a standing caution: the mandated platform query contains the token `MIT`, and the
> single most prominent result it returns is a platform whose connection to "MIT" is that it was written at
> a university of that name.** 🟢 **Licence columns on this shelf come from payload, which is why the shelf
> never absorbed the claim.**

### 🟢 The assessment chain — pass 39's five links, with link 5's deployment shape corrected

| # | Layer | Implementation | Licence (channel) | 🆕 Deployment shape after this pass |
|---|---|---|---|---|
| 1 | **Item generation** | `openedx-course-generator` + LLM | per-component | in-product |
| 2 | **Delivery / proctoring** | Open edX (**AGPL-3.0**) · SEB Server · MIT proctoring side-cars | mixed | 🔴 **side-car** (platform is copyleft) |
| 3 | **Item calibration** | `py-irt` · `irtorch` · `girth` | 🟢 **MIT** | 🟢 in-product |
| 4 | **Subgroup fairness (DIF)** | `difair` · `aequitas` | 🟢 **MIT** | 🟢 in-product |
| 5 | **Comparability / linking** | 🆕 **`EqUMP`** (Python) · `meyerjp3/psychometrics` (Java) | 🟢 **MIT** · **Apache-2.0** | 🟢 **in-product — changed this pass.** 🔴 **Pass 39 could only offer this link as an R/GPL side-car or a JVM process** |
| 5b | **Observed-score & kernel equating** | `equate` · `kequate` · `SNSequate` | 🔴 **GPL-2/3** | 🔴 **side-car only — unchanged (`P500`)** |

🟢 **The whole chain is now permissive and in-process *except* delivery (link 2, platform copyleft) and
observed-score/kernel equating (link 5b).** 🔵 **That is a materially different architecture from pass 39's,
and the reason is one package: `EqUMP` 0.3.6, MIT, artefact-verified (`P499`).**

🔴 **The caveat that must travel with the row.** `EqUMP` ships **linking** (Mean-Mean, Mean-Sigma, Haebara,
Stocking-Lord) and **true-score equating**. 🔴 **Its `equating/kernel/`, `equating/obs/` and `scoring/`
directories are declared and contain 0-byte stubs (`P500`)** — so a design that needs observed-score
equating still needs the GPL R tier behind a process boundary, and link 5b stays where it was.

### 🔵 Why this matters for a platform engagement specifically

🟢 **A platform customisation project inherits the platform's licence at the boundary it crosses.** 🔵 **The
assessment chain above is the part a vendor *adds*, and until this pass its comparability link forced
either a GPL R process or a JVM process alongside a Python service.** 🟢 **With `EqUMP`, links 3–5 are one
Python dependency set, importable into the same service, with the GPL contact confined to `EqUMP`'s own
test suite (`P504`) rather than to the shipped runtime.**

---

## 🟢 Thirty-ninth pass, 2026-10-07 — the assessment tier gets its *comparability* layer, and the layer is an R/CRAN tier the platform shelf cannot absorb

**Licences read from payload on 2026-10-07**, title-block classified (`P171`); where no payload exists the
manifest and source-header channels are named (`P494`). ⏱️ **Sixth pass of this date.**

🔵 **This file's job is platforms that can be customised with AI on top. No new LMS or SIS again this
pass — that shelf is saturated.** 🟢 **What changes is the assessment tier `verticals` has been building
since pass 33: pass 38 declared it complete at four rows, and it was not.**

### 🔴 The assessment chain, corrected — pass 38 counted four links where there are five

🔴 **Pass 38's table had four layers and concluded *"all four permissive, no copyleft anywhere, so the
whole assessment chain is an in-product component rather than a side-car."*** 🔵 **The chain has a fifth
link between calibration and delivery, and it is the only one a regulator asks about by name:**

| # | Layer | Platform / library | Licence (channel) | Status before this pass |
|---|---|---|---|---|
| 1 | Author + bank items (QTI 3) | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · payload `main/LICENSE.md` · 1,072 B | 🟢 shelved |
| 2 | Deliver items (QTI 3 player) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · payload `main/LICENSE` · 1,076 B | 🟢 shelved |
| 3 | Calibrate difficulty / discrimination | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · payload `master/LICENSE` · **1,121 B** 🟢 re-verified this pass | 🟢 shelved (pass 38) |
| 4 | Adapt the test to the learner | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3** · payload `main/LICENSE` · **1,514 B** 🟢 re-verified this pass | 🟢 shelved (pass 38) |
| 🔴 **5** | 🔴 **Put two tests on the same scale** (linking / equating) | 🆕 [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) | 🟢 **Apache-2.0** · 🔴 **no payload** — source headers govern (`P494`) | 🔴 **absent** |
| 🔴 **5b** | 🔴 **Prove no item disadvantages a subgroup** (DIF) | 🆕 [`ZIYINGJERRY/difair`](https://github.com/ZIYINGJERRY/difair) | 🟢 **MIT** · payload `main/LICENSE` · **1,075 B** + `pyproject.toml` | 🔴 **absent** |

🟢 **All six are permissive, so pass 38's conclusion survives — but only because exactly one permissive
option exists at layer 5 and exactly one at 5b.** 🔴 **Everything else at this layer is GPL** — see
`P493`. 🔵 **"No copyleft anywhere" was true of a four-link chain and is a one-deep accident on a six-link
one.**

### 🔴 Why layer 5 cannot be customised the way this file's platforms are

🔵 **Every other row in this file is a platform you fork, theme and extend** — Moodle, Open edX,
OpenEduCat, Odoo-based SIS. 🔴 **Layer 5 is not that.** `meyerjp3/psychometrics` is a **Java library with
no UI, no API, no container** and a 2012 codebase; `difair` is a **Python package plus a single
155,170 B self-contained HTML file** (`difair_studio.html`) that runs in a browser with no install and no
network calls.

| | A platform (rows elsewhere in this file) | 🔴 Layer 5 |
|---|---|---|
| Customisation model | fork · plugin · theme | 🔴 **embed as a dependency** |
| Who operates it | an institution's IT | 🔴 **a psychometrician, or nobody** |
| What the AI sits on top of | the platform's data model | 🔴 **a response matrix** |

> 🔵 **The deliverable consequence, and it is the useful sentence from this pass.** 🔴 **There is no
> open-source *platform* for assessment comparability** — no equivalent of Moodle for psychometrics.
> `hicsail/opencat-pro` was the nearest candidate and `P486` disqualified it (MIT code, **paid** Accessible+
> UI framework). 🟢 **So this layer ships as a **service** behind an existing LMS, not as a product a
> client's IT department operates**, and that is a sizing and staffing fact, not a licensing one.

### 🟢 `difair_studio.html` — the one row in this file that needs no platform at all

🔵 **Worth separating out, because it is unusual on this shelf.** A **155,170 B** single HTML file, shipped
in the repo rather than in the Python distribution, with five tabs (dichotomous DIF, polytomous DIF,
fairness metrics, survey design, pipeline attribution), each with a CSV template and a synthetic sample
generator. 🟢 **Its own README states the engineering honestly:** every procedure is a from-scratch
JavaScript port checked against the Python implementation, agreeing to **five or more decimal places** for
Mantel-Haenszel, standardization, Breslow-Day, generalized M-H, fairness and survey/jackknife, while the
logistic-regression procedures *"use their own solver … and so are close but not bit-identical."*

| Why it matters for an engagement | |
|---|---|
| 🟢 **No install, no Python, no network calls** | 🔵 A ministry or exam board can audit items on an **air-gapped** machine, which is the common constraint in public-sector education procurement |
| 🟢 **Data never leaves the browser** | 🔵 Directly relevant where student data cannot be processed off-premise — **California AB 1159**, and the EU AI Act's data-governance obligations |
| 🔴 **Not a substitute for the package** | 🔴 Logistic DIF is *"close but not bit-identical"*; for an evidence pack that a regulator will read, run the **Python** path and cite its residuals |

### 🔴 Rejected at this layer, with the reason — so no later pass re-probes them

| Candidate | Licence | Why it is not a `verticals` row |
|---|---|---|
| [`cran/difR`](https://github.com/cran/difR) v**6.1.0** | 🔴 **GPL (≥ 2)** (`master/DESCRIPTION`) | 🟡 **Side-car only.** 🔵 Keep it as the **validation oracle** for `difair`, never in the product |
| [`talbano/equate`](https://github.com/talbano/equate) | 🔴 **GPL-3** | 🟡 Side-car only |
| [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | 🟡 **LGPL-3** · payload **7,639 B** | 🟡 Linkable unmodified; 🔴 an R runtime inside a product is an operational cost this chain does not otherwise carry |
| [`brettlballard/DIF`](https://github.com/brettlballard/DIF) | 🔴 **no grant** (no payload; README **70 B**) | 🔴 **Unusable** |
| [`hicsail/opencat-pro`](https://github.com/hicsail/opencat-pro) | 🟢 MIT code 🔴 **+ paid UI framework** | 🔴 **Still disqualified** (`P486`, pass 38) — unchanged this pass |

---

## 🔴 Thirty-eighth pass, 2026-10-07 — the assessment-delivery tier gets its measurement half, and a platform whose MIT grant stops at the UI

**Licences read from payload on 2026-10-07**, title-block classified (`P171`). ⏱️ **Fifth pass of this date.**

🔵 **This file's job is platforms that can be customised with AI on top. This pass adds no new LMS or
SIS — the platform shelf is saturated — and instead closes a hole *inside* the assessment tier that
`verticals` has been carrying for several passes.**

### 🟢 The assessment tier was half a platform, and this pass says which half was missing

🔵 **Shelved already: item banking and certified delivery.** 🔴 **Absent until now: the measurement that
makes a delivered item mean anything.**

| Layer | Platform / library | Licence (payload) | Status before this pass |
|---|---|---|---|
| Author + bank items (QTI 3) | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · `main/LICENSE.md` · 1,072 B | 🟢 shelved |
| Deliver items (QTI 3 player) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · `main/LICENSE` · 1,076 B | 🟢 shelved |
| 🔴 **Calibrate difficulty / discrimination** | 🆕 [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · `master/LICENSE` · 1,121 B | 🔴 **absent** |
| 🔴 **Adapt the test to the learner** | 🆕 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · `main/LICENSE` · 1,514 B | 🔴 **absent** |

🟢 **All four permissive, no copyleft anywhere, so the whole assessment chain is an in-product
component rather than a side-car.** 🔵 **That is rare on this shelf** — the LMS, SIS and proctoring tiers
are overwhelmingly GPL/AGPL, and the KB has repeatedly had to route around them (`T4`, passes 33–37).

### 🔴 `P486` — a repo's MIT payload does not license the interface the platform ships

🆕 [`hicsail/opencat-pro`](https://github.com/hicsail/opencat-pro) (**BYO-CAT**, Boston University
Software & Application Innovation Lab) is the only open-source **CAT web platform** this pass found. It
probes **clean**:

| Probe | Result |
|---|---|
| Licence payload | 🟢 **MIT**, `master/LICENSE`, **1,106 B** |
| Family (title block) | 🟢 **MIT**, unambiguous |
| Commercial use, from the payload | 🟢 **`OK`** |

🔴 **And it cannot be used in production without buying something.** Its own `README.md`, twice:

> *line 6:* *"The platform uses **Accessible+** to provide **section 508 compliant** user interface.
> Please **purchase a license** of the platform suitable to your needs if you wish to use BYO-CAT for
> development."*
>
> *line 176:* *"The UI framework is based on **Accessible+**. **A valid license is required to use this
> in production.**"*

🔵 **The grant is honest and the probe is honest; they are answering different questions.** The payload
answers *"may I use the authors' code?"* — yes. The deliverable question is *"may I ship this
platform?"* — **not without a third-party licence the repo does not contain.**

🔴 **And the non-free component sits exactly where the education buyer's requirement is.** Section 508 /
WCAG conformance is a **procurement precondition** for US public-sector education, so the one part a
public buyer cannot drop is the one part that is not free.

> **`P486`.** For a **platform** row, payload is necessary and **not sufficient**. Read the `README`'s
> own licence section for **vendored-asset obligations** before writing `OK`. 🔵 **This is the
> probe's own documented limit** — *"monorepo and open-core carve-outs are not detected"* — met for the
> first time in education, and in a form **no path-aware read of the tree would catch either**, because
> the obligation is stated only in prose.

### 🟢 The CAT platform question, answered honestly

| Option | Licence reality | Verdict |
|---|---|---|
| [`hicsail/opencat-pro`](https://github.com/hicsail/opencat-pro) | 🟢 MIT code 🔴 **+ paid UI framework** | 🔴 **Not cleanly usable.** Viable only if the UI is **replaced**, which is most of a web platform |
| [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) + own UI | 🟢 **BSD-3-Clause**, no vendored assets | 🟢 **The recommended route.** `catsim` is an **engine**, not a platform — pair it with the QTI player above and the UI is the client's |
| [`condecon/adaptivetesting`](https://github.com/condecon/adaptivetesting) | 🟡 **MPL-2.0** · 16,661 B | 🟡 **Usable in-tree**, with file-level copyleft: modifications **to its own files** must be published; your surrounding code is unaffected |

> 🔵 **Selection rule this pass adds.** For assessment, prefer an **engine + your own UI** over a
> **platform**. The engines in this tier are permissive and jurisdiction-neutral; the one platform
> carries a purchased dependency. 🟢 **And an engine is what a regulated buyer wants anyway** — the
> auditable artefact is the calibration, not the chrome.

### 🔵 What did not change this pass, stated so the shelf is not re-litigated

| Tier | Status |
|---|---|
| LMS (Moodle, Open edX, Chamilo, ILIAS, Sakai, `classroomio`) | 🔵 **unchanged.** Re-surfaced by this pass's platform search; **all already shelved with payload-read licences** (pass 37 re-licensed the whole shelf from payload) |
| SIS (`rubelw/OSSS` Apache-2.0, openSIS, RosarioSIS) | 🔵 **unchanged** |
| ERP-for-education (`OpenEduCat`, LGPL, Odoo-based) | 🔵 **unchanged.** ⚠️ Still the shelf's only **LGPL** platform, and still **without a fixture** in the licence gate (`fixtures-pending/README.md` names this) |
| Proctoring / integrity | 🔵 **unchanged** — still copyleft, still a side-car (pass 33) |

## 🟢 Thirty-seventh pass, 2026-10-07 — the whole platform shelf re-licensed from payload, and the rule it reveals

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07**, branch- and case-aware,
each verdict **anchored to the payload's title block** (**`P171`**; the fixture-coverage gap that let
this slip in a new instrument is **`P480`**). No star counts (`P479`).
⚠️ **No in-tree instrument was executable this pass**; verdicts were calibrated against 8 known-answer
controls instead.

### 🔴 Why every row in this file had to be re-measured

🔵 **`P171` is reopened in the exact place this file lives, and `P480` is why a green gate missed it.** A bare-word NonCommercial test reported
**AGPL-3.0 and GPL-3.0 payloads as commercially prohibited**, because **§6 of both says *"allowed only
occasionally and `noncommercially`"***. 🔴 **This file is almost entirely GPL/AGPL** — so the defect's
blast radius was *this shelf*, and a false `PROHIBIDO` deletes a platform from consideration without
leaving a row behind.

### 🟢 The platform shelf, by tier, with the licence read from the payload

| Tier | Platform | 🟢 Licence (title block) | Bytes · path | What AI on top looks like |
|---|---|---|---|---|
| **LMS** | 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** | 10,982 · `master/LICENSE` | 🟢 **The one tier-1 LMS you can extend in-product.** Java; Zurich-stewarded. 🟢 **EMEA** |
| **LMS** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **GPL-3.0** | 35,146 · ⚠️ `main/COPYING.txt` | Deepest plugin catalogue in the category. 🔴 **Deliver as a *plugin* or an out-of-process service** — never a closed fork. 🟢 **Two MCP routes now verified**: `SaadRahman01/moodle-mcp` (MIT, dev-docs + guarded WS) and `lmscloud-io/moodle-mcp-server` (GPL-3.0, WS execution) |
| **LMS** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 11,120 · `master/LICENSE` | ⚠️ **`P476` stands: ECL is Apache-2.0 with the §3 patent grant narrowed to education.** "Basically Apache" is true of copyright and false of patents — and patents are what legal review argues about |
| **LMS** | 🆕 [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🟢 **AGPL-3.0** | 34,522 · `main/LICENSE` | 🆕 **Positioned directly against Moodle, EdX, Thinkific and Teachable**, and **AI-native in its own packaging**: the MCP layer ships separately as **`@classroomio/mcp` on npm, 🟢 MIT v0.0.9**. 🔵 **Two licences, two conversations** — an MIT integration layer bolted to an AGPL core. 🔴 **AGPL is network-use copyleft: hosting it for a client triggers source obligations on your modifications** |
| **SIS** | 🟢 [`rubelw/OSSS`](https://github.com/rubelw/OSSS) | 🟢 **Apache-2.0** | 11,362 · `main/LICENSE` | 🟢 **The one permissive SIS** (pass 36). FastAPI + Keycloak SSO + PostgreSQL; **Ollama + MetaGPT + A2A in-tree**. ⚠️ **self-declared active development, workflow/state-machine logic unfinished — pilot tier, study the architecture** |
| **SIS** | 🆕 [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🟢 **GPL-2.0** | 15,214 · `master/LICENSE` | Students, grades, scheduling, attendance, billing, discipline, food service, **Moodle integration in-tree**. 🔴 **Strictest row on this shelf** — side-car only |
| **SIS / ERP** | 🆕 [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟢 **LGPL** | 8,240 · `master/LICENSE` | Odoo-based: admissions, students, faculty, courses **plus LMS delivery**. 🔵 **LGPL is the softest copyleft here — linking a separate AI service is clean, modifying the library is not** |
| **Lecture capture** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** | 11,340 · `develop/LICENSE` | Capture → process → deliver. 🔵 **Its recorded-lecture corpus is the natural input to any ingestion pipeline.** ⚠️ default branch is **`develop`**; `apereo/opencast` resolves nothing |
| **Offline / low-resource** | 🆕 [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1,096 · `master/LICENSE` | 🟢 **The most permissive platform on the shelf, and the only one whose architecture already assumes intermittent connectivity.** 🔵 **That is the default condition in LATAM public education, EMEA-Africa and rural APAC — and it is MIT, so the AI layer can ship inside the product** |

### 🟢 The rule this file can now state, because it was measured rather than assumed

> **In open source education there is, per tier, essentially *one* permissive platform — and
> everything else is copyleft.**
> **LMS → `OpenOLAT` (Apache-2.0).** **SIS → `OSSS` (Apache-2.0, immature).**
> **Offline → `Kolibri` (MIT).** Everything else: GPL-2.0, GPL-3.0, LGPL, AGPL-3.0 or ECL-2.0.

🔵 **That turns the platform choice from a preference into a selection of one**, and it makes the
follow-up question the real one: **when the single permissive option is immature, is the honest
deliverable a side-car or a fork?** 🟢 **For `OSSS` today the answer is side-car** — its own README
dates unfinished workflow and state-machine logic, which for a system whose job is enrolment and grade
workflows is the core, not the periphery.

### 🔵 What the copyleft spread actually costs, stated per obligation rather than per label

| Obligation | Triggered by | Platforms | Practical effect on a Globant deliverable |
|---|---|---|---|
| **None** | — | `OpenOLAT`, `OSSS`, `Kolibri` | 🟢 AI layer ships **inside** the product |
| **Patent grant narrowed** | distribution | `Sakai`, `Opencast` | 🟡 copyright is Apache-shaped; **the §3 patent scope is education-specific** and must reach legal review as ECL, not Apache |
| **Source on distribution** | shipping modified binaries | `Moodle`, `RosarioSIS` | 🟡 deliver as **plugin / separate service**; modifications to core are publishable |
| **Source on linking** | linking the library itself | `OpenEduCat` | 🟡 separate-process AI service is clean |
| 🔴 **Source on network use** | **hosting it for the client** | `ClassroomIO`, Canvas, Open edX | 🔴 **The one obligation that fires on SaaS.** A hosted engagement publishes your modifications — decide this **before** architecture, not at delivery |

🔴 **AGPL is the row that surprises clients, because it is the only one where simply *operating* the
platform — not shipping it — creates the obligation.** 🔵 **And it is spreading on this shelf: Canvas,
Open edX and now ClassroomIO are all AGPL-3.0**, which means the LMS tier's *most AI-native* entrants
carry its strictest terms.

## 🔴 Thirty-sixth pass, 2026-10-07 — the SIS tier gets an in-tree option, and a secondary source tried to overwrite a verified licence

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07** (branch- and case-aware),
**each payload re-classified through `compose/code/lib/license_family.sh`** and cross-checked against
PyPI where published. No star counts: `api.github.com` **403**. Channel census in `agents/top.md`.

### 🔴 `P476` — the search summary said "Sakai, Apache 2.0". The payload and this KB both said ECL-2.0

The query `open source platform education LMS SIS ERP MIT Apache 2026` returned, in prose, *"Sakai is an
open-source LMS stewarded by the Apereo Foundation … under Apache 2.0 license."* 🔴 **That sentence was
written into this pass's own trending row before anything checked it.** Measured minutes later:

| Channel | Verdict |
|---|---|
| Secondary source (search summary) | 🔴 **"Apache 2.0"** |
| 🟢 Payload `sakaiproject/sakai` `master/LICENSE`, **11,120 B** | 🟢 **`ECL-2.0`** — title block: *"Educational Community License, Version 2.0 (ECL-2.0)"* |
| 🟢 This KB's own `repos/foundations.md:527` | 🟢 **already recorded `ECL-2.0` (Sakai, Opencast, Kuali Rice)** |

🔵 **The payload explains exactly why the confusion is structural, and it is not a typo in the source.**
ECL-2.0 states its own relationship to Apache in its preamble: *"The Educational Community License
version 2.0 ('ECL') consists of the Apache 2.0 license, **modified to change the scope of the patent
grant in section 3** to be specific to the needs of the education communities using this license."* 🔴 **So
"it's basically Apache 2.0" is true about the copyright grant and false about the patent grant — and the
patent grant is the clause a client's legal review actually argues about.** A summary that flattens ECL
to Apache is not merely imprecise; it erases the one section that differs.

🔴 **And this is a recurrence, not a new defect.** `agents/trending.md` records that **Sakai was missing
from this KB for ten passes because of a misread licence line** — *"faltaba por una línea de licencia mal
leída, no por falta de búsqueda."* The same platform, the same clause, the same direction of error.

> **`P476`.** A secondary source's licence string **never** overwrites a payload-verified shelf row. When
> prose and payload disagree the payload wins, and when the shelf already holds the payload-verified
> answer the shelf wins over a fresh search. Order of precedence: **payload > shelf > secondary prose**.
> 🔵 **Corrected inside the same pass that introduced it** — the row in `agents/trending.md` now reads
> `ECL-2.0` and says why.

🟢 **The consequence for the allowlist is one this KB already got right and should keep loud.** Sakai is
**permissive and commercially usable** (`commercial_use_ok` → **OK** on the real payload); it is simply
not called Apache. The standing education allowlist stays: **MIT, Apache-2.0, BSD (2/3-clause), ECL-2.0,
PostgreSQL License, ISC** — a three-name `MIT|Apache|BSD` match throws Sakai, Opencast and Kuali Rice away.

### 🟢 The platform licence table — rows re-read from payload this pass

| Platform | Licence (payload, this pass) | Commercial use | Architecture consequence |
|---|---|---|---|
| **Sakai** | 🟢 **ECL-2.0** — `master/LICENSE`, **11,120 B**, re-read this pass | 🟢 **OK** | 🟢 **IN-TREE**, with the ECL patent-grant note above. Apereo Foundation; higher-ed consortia, peer assessment, portfolios |
| **OpenOLAT** | 🟢 Apache-2.0 (pass 35; 10,982 B, `master`) | 🟢 OK | 🟢 **IN-TREE** — full LMS incl. assessment, QTI, SCORM. **EMEA** (Univ. Zurich → frentix GmbH) |
| **Kolibri** | 🟢 **MIT** — `master/LICENSE`, **1,097 B**, re-read this pass | 🟢 **OK** | 🟢 in-tree — offline-first, not a full LMS |
| 🆕 **OSSS** | 🟢 **Apache-2.0** — `main/LICENSE`, **11,363 B**; 🟢 PyPI `open-schools` OSI classifier | 🟢 **OK** | 🟢 **IN-TREE — and the first permissive SIS on this shelf.** See below |
| **Eloom LMS** | 🟢 MIT (pass 35; 1,062 B) | 🟢 OK | 🟢 in-tree; region **unplaced** |
| **Open edX** platform / extension | 🔴 AGPL-3.0 / 🟢 Apache-2.0 (XBlock) | 🟢 OK both | 🔴 side-car for the platform, 🟢 in-tree via **XBlock** |
| **Moodle** | 🔴 GPL-3.0-or-later (Packagist `moodle/moodle`) | 🟢 OK | 🔴 **side-car only** — largest installed base. ⚠️ **`moodle/moodle` serves no payload at `LICENSE*` on `main`/`master` this pass** — its text is at `COPYING.txt`; the Packagist channel is what carries this row |
| **Chamilo** · **ILIAS** | 🔴 GPL-3.0 / GPL | 🟢 OK | 🔴 side-car |
| **OpenEduCat** | 🟡 LGPL-3.0 (declared) | 🟢 OK | 🟡 Odoo-module model; weaker copyleft, still copyleft. ⚠️ **`OpenEduCat/openeducat` serves no licence payload** — declared-only, unchanged |
| **Frappe / Frappe Education** | 🟢 MIT (PyPI `frappe`, OSI classifier) | 🟢 OK | 🟢 in-tree. ⚠️ **`frappe/lms` serves no payload at the probed filenames** — the PyPI channel carries it |
| **Forma LMS** | 🔴 **UNVERIFIED** (`P470`) | ⚠️ unknown | ⚠️ **do not place in either column.** 🆕 **`registry.npmjs.org` is reachable this pass (200)** — the JS half of this tier can finally get a second channel |

### 🟢 `OSSS` — what changes now that the SIS tier has a permissive member

🔵 **Pass 35 established that a full LMS can be extended in-tree (`OpenOLAT`). That left the tier where
most education engagements actually land still entirely copyleft.** Enrolment, attendance, gradebook,
fees, timetabling — the *administrative* system — has been **openSIS GPL, RosarioSIS GPL-2.0, OpenEduCat
LGPL-3.0**, so an AI deliverable touching student records has always been a side-car by default.

[`rubelw/OSSS`](https://github.com/rubelw/OSSS) is **Apache-2.0 on three channels** and is a **K-12 SIS
with the agent tier inside the tree** — `Ollama + MetaGPT + A2A` named in its own architecture, over
FastAPI + **Keycloak SSO** + SQLAlchemy + PostgreSQL, with a Next.js front end. Modules: governance,
student info, accounting, activities, **transportation**. 🟢 **Region: North America**, placed on the data
model — districts as top-level tenant, district transportation, district accounting, board governance
(`P474`), which is US district structure rather than a generic school.

🔴 **And the caveat has to travel with it every time, or this row does harm.** The README's own banner:
*"OSSS is still being developed"*, with a dated note (**7 Nov 2026**) that the **state machine and
workflow/gate logic are still being built**. 🔴 **For a student information system, enrolment and grade
workflows are not a feature — they are the product.** So:

| Use `OSSS` as | Verdict |
|---|---|
| 🟢 The **reference architecture** for "how does an agent tier live *inside* a SIS rather than beside it" | 🟢 **Yes — it is the only permissive example on this shelf** |
| 🟢 A **pilot / greenfield** base where workflow logic is being written anyway | 🟡 **Defensible, with the maturity disclosed in writing** |
| 🔴 A **migration target** for a district running openSIS or RosarioSIS today | 🔴 **No.** The workflow engine it would have to replace is the part that is unfinished |

🔵 **The honest framing for a client: `OSSS` changes what is *architecturally possible* in the SIS tier
without yet changing what is *operationally safe*.** That is still a real change, because it means the
side-car is now a choice rather than a licence consequence.

### ⚠️ The content tier needs `P250`'s second column, and this is the shelf where that bites

This shelf lists **platforms**, and platforms are code. 🔴 **But the KB's adjacent tiers hold curricula,
item banks and courseware, and that is where `CC BY-NC` lives.** `CRSS-AI/agentic-se-course-early-2026`
was probed this pass: a normal `LICENSE` at a normal size, **`CC-BY-NC-4.0`, commercial use
`PROHIBIDO`**, reported `GRANTED` by a filename-based probe (`P473`). 🟢 **For code, "has a permissive
licence file" is nearly always a permissive grant. For content, it is often not** — so every
content-tier row must carry the commercial-use column explicitly, not inherit the code tier's prior.

## 🔴 Thirty-fifth pass, 2026-10-07 — the permissive platform tier is bigger than this shelf said, and one Apache claim collapses

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07** (branch- and case-aware,
12–19 filenames × `main`/`master`), **cross-checked against the registry or build descriptor each
platform publishes.** No star counts: `api.github.com` **403**. Cumulative channel census in
`agents/top.md`.

### 🔴 The platform licence table, corrected

This shelf's standing rule has been that **the platform tier is copyleft and the integration tier is
permissive**, which forces a side-car architecture on every engagement. 🔵 **That rule is still right
about most of the tier and wrong about the whole of it.** Two permissive full LMS platforms are
payload-verified, and one is EMEA-origin:

| Platform | Licence (payload, this pass or prior) | Second channel | Architecture consequence |
|---|---|---|---|
| **Moodle** | GPL-3.0-or-later | 🟢 Packagist `moodle/moodle` → `GPL-3.0-or-later` | 🔴 **side-car only** — largest installed base in the industry |
| **Open edX** platform tier | AGPL-3.0 | 🟢 PyPI `openedx-learning`, `edx-proctoring`, `edx-opaque-keys` → AGPL | 🔴 **side-car only**, incl. helper libraries |
| **Open edX** extension tier | Apache-2.0 | 🟢 PyPI `xblock` → Apache-2.0 | 🟢 in-tree via XBlock |
| **Chamilo** | GPL-3.0 | 🔴 Packagist **404** | 🔴 side-car; payload-only row |
| **ILIAS** | GPL | — | 🔴 side-car — widely used in German universities and public agencies |
| **OpenEduCat** | LGPL-3.0 (declared) | — | 🟡 Odoo-module model; weaker copyleft but still copyleft |
| 🆕 **OpenOLAT** | 🟢 **Apache-2.0** — `master/LICENSE`, **10,982 B**, re-read this pass | 🟢 `pom.xml` `<licenses>` **+ second forge** `gitlab.com/olatorg/OpenOLAT` | 🟢 **IN-TREE. The single most consequential licence fact on this shelf** — and it is **EMEA-origin** (OLAT from the **University of Zurich**, maintained by **frentix GmbH**, Switzerland) |
| 🆕 **Eloom LMS** | 🟢 **MIT** — `main/LICENSE`, **1,062 B** | 🟢 README badge agrees; 🔴 not on Packagist | 🟢 **IN-TREE**, and the most permissive full LMS here. Laravel 13 / PHP 8.3+ |
| 🆕 **Forma LMS** | 🔴 **UNVERIFIED** — see `P470` | 🔴 payload ∅, Packagist **404**, no `composer.json` | ⚠️ **Do not place in either column.** Secondary sources call it Apache-2.0; nothing here confirms it |
| **Kolibri** | MIT | 🟢 PyPI `kolibri` → MIT + **OSI classifier** (re-read this pass) | 🟢 in-tree — offline-first, not a full LMS |
| **Frappe / Frappe Education** | MIT | 🟢 PyPI `frappe` → OSI MIT classifier | 🟢 in-tree |

### 🟢 What changes in practice — the in-tree option now exists for a full LMS

🔵 **Until this pass, every full LMS on this shelf forced the same conversation**: the deliverable
sits *outside* the platform tree, talks to it over LTI 1.3 / REST / xAPI, and the client's legal team
reviews a side-car. That architecture is sound and most of this KB's patterns assume it.

🟢 **With OpenOLAT (Apache-2.0) and Eloom (MIT), an engagement has a real second option**: build the
AI capability **as a module inside the platform**, ship it as part of the product, and keep
proprietary logic proprietary.

⚠️ **Three honest caveats, so this is not oversold:**

1. **Installed base is the counterweight.** Moodle's footprint dwarfs OpenOLAT's and Eloom's
   combined. 🔵 **A permissive licence does not relocate the client's existing LMS.** In-tree is an
   option for a *greenfield* or *replatforming* engagement, not a retrofit argument.
2. **Eloom's region is unknown.** The `README` names no country or qualifications authority, so it is
   **unplaced** in this KB, not assigned. It also has **no registry presence**, so its row rests on
   payload + a README badge.
3. **OpenOLAT is Java/Maven**, Eloom is **Laravel/PHP 8.3+**. Neither matches the Python skill base
   most of this KB's agent rows assume. 🔵 **The licence unblocks the architecture; it does not supply
   the team.**

### 🔴 `P470` — Forma LMS, and why a recommendation is not a grant

Articles this pass recommend Forma LMS **because** it is Apache-2.0 — the permissive licence is the
stated reason to choose it. The repository exists (`master/README.md` → 200) and **19 licence
filenames across `main` and `master` return nothing**, Packagist is **404**, and there is no parseable
`composer.json`.

⚠️ **Forma LMS is therefore recorded as `licence unverified` and is excluded from the permissive
column.** 🔵 **Platforms are exactly where this costs most.** A licence error in the integration tier
changes a dependency note; a licence error in the platform tier changes **whether the deliverable can
be a module at all**. This KB's discipline holds: **payload or a machine-readable declaration, or the
row says "unverified".**

### 🟢 Assessment-delivery tier — a permissive standards engine, shelved at last

[`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks), 🟢 **BSD-3-Clause** (`master/LICENSE.txt`,
2,058 B), **University of Edinburgh**: the **QTIWorks Engine** (QTI 2.1 delivery + rendering),
**JQTI+** (read/write/model/manipulate QTI 2.1 items and tests programmatically) and the
**MathAssess** extensions for advanced mathematical assessment.

🔵 **Why this belongs on the platform shelf rather than the library shelf:** item-bank migration is
one of the hardest commitments in an assessment engagement, and JQTI+ makes it **programmatic and
permissive** — QTI 2.1 in, transformed QTI 2.1 out, no vendor in the path. Paired with the
`1EdTech`/`oat-sa`/`citolab` QTI rows already here, the standards tier is now permissive **end to
end**: authoring, transformation and delivery.

## 🟢 Thirty-fourth pass, 2026-10-07 — the platform licences re-read against a second channel, and the Canvas integration layer was missing

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07** (branch- and case-aware,
13 filenames × `main`/`master`), **and cross-checked against the registry each platform publishes
to.** No star counts: `api.github.com` **403**, and the GitHub MCP route an earlier pass used is
outside this session's repository scope. Consolidated 20-channel census in `agents/top.md`; `P465`
records why it needed consolidating.

### 🔵 Why the second channel matters more for platforms than for agents

A platform's licence is the most consequential fact on this shelf — it decides whether the
deliverable can be a module inside the tree or must be a side-car outside it. And platforms are
exactly where payload-reading is least comfortable: a 35 KB `LICENSE` blob has to be text-matched,
and GPL-2.0, GPL-3.0, AGPL-3.0 and LGPL share most of their prose. **A packaging declaration says
which one in a machine-readable string.**

| Platform | Payload verdict (this KB's record) | 🆕 Registry declaration | Agreement |
|---|---|---|---|
| **Moodle** | GPL-3.0-or-later | Packagist `moodle/moodle` → **`GPL-3.0-or-later`** | 🟢 agrees |
| **Open edX platform tier** | AGPL-3.0 | PyPI `openedx-learning` → **AGPL 3.0** (OSI AGPLv3+); `edx-proctoring` → **AGPL 3.0**; 🆕 `edx-opaque-keys` → **AGPL-3.0-only** | 🟢 agrees — 🆕 **`edx-opaque-keys` is a new row** |
| **Open edX extension tier** | Apache-2.0 | PyPI `xblock` → **Apache-2.0** | 🟢 agrees |
| **Kolibri** | MIT | PyPI `kolibri` → **MIT** (OSI MIT classifier) | 🟢 agrees |
| **Frappe / Frappe Education** | MIT | PyPI `frappe` → **OSI MIT classifier** | 🟢 agrees |
| **Chamilo** | GPL-3.0 | 🔴 Packagist **404** — not published there | ⚠️ payload only |

🔵 **`GPL-3.0-or-later` is this KB's existing record for Moodle, and the point of the re-read is that
it did not move.** The distinction matters on every Moodle engagement — *"GPL-3.0"* alone leaves open
whether a downstream work may be distributed under a later GPL version, and `-or-later` settles it —
so it is worth confirming from Moodle's own packaging metadata rather than inheriting it.

⚠️ **Chamilo is the counter-example that keeps this honest** (`P468`): a major PHP LMS on this shelf
with **no Packagist presence**. The registry route has coverage holes, and a 404 is not a licence
finding.

### 🟢 The integration layer this shelf was missing

| Layer | Repo | Licence | Cross-channel | Why it belongs on the platform shelf |
|---|---|---|---|---|
| **Canvas LMS API client (Python)** | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **MIT** (`master/LICENSE`, 1,130 B) | 🟢 PyPI `canvasapi` → MIT + **OSI MIT classifier** | 🔴 **This shelf carried six Canvas MCP servers and not the client they sit on.** Object-oriented Python over the Canvas REST API: courses, enrolments, assignments, **submissions and gradebook writes**, quizzes, LTI. From **UCF Open** — the same group as `UDOIT`, `Materia` and `Obojobo`, all already here. 🔵 **Canvas itself is AGPL-3.0; this client is MIT.** Sixth independent instance of this KB's platform-copyleft / integration-permissive rule: the client talks over HTTP from outside the tree, so your deliverable does not inherit Canvas's licence. Branch is `master`. |

### 🟡 A standalone assessment platform, EMEA-origin, and copyleft

| Platform | Repo | Licence | Stack | Where it fits |
|---|---|---|---|---|
| **genai-open-assessment** | [`macsnoeren/genai-open-assessment`](https://github.com/macsnoeren/genai-open-assessment) | 🟡 **GPL-3.0** (`main/LICENSE`, 35,149 B) | Apache + PHP + **SQLite**, one-command Docker start | Rubric-driven automated grading of **open-ended** higher-education questions, with role-separated UIs for teachers, assessors, admins and students. 🟢 **Its design principle is the one EMEA buyers ask for first:** educational validity, transparency and **auditability** — every prompt, criterion, input and output storable and reviewable, with the human educator accountable for the decision. **Netherlands-origin** (Dutch interface, `@school.nl` seed accounts). 🟡 **GPL-3.0 — deploy it or extend it as its own system; do not embed it in a permissive deliverable.** 🔵 **Its real value to an engagement may be the rubric-and-audit data model rather than the PHP**: it is the clearest worked example on this shelf of what Annex III "assessment of learning outcomes" compliance looks like in a schema. |

### 🔵 The selection rule this pass adds

**Verify a platform's licence twice, and prefer the sharper statement.** Where payload and registry
agree, the row is as well-evidenced as this KB can make it, and the registry often carries the more
precise SPDX expression (`GPL-3.0-or-later` beats `GPL-3.0`). Where only payload answers — Chamilo,
and every platform not published to a registry — say so on the row rather than implying both.

## 🟡 Thirty-third pass, 2026-10-07 — the integrity layer is copyleft, and that decides where the agent goes

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07**, branch- and case-aware
probe (13 filenames × `main` and `master`). No star counts: `api.github.com` **403**, github.com
landing pages **403** on HEAD and GET. 🆕 `eur-lex.europa.eu` **000** and `huggingface.co` **000** —
both egress-blocked, both newly recorded.

### 🔵 Proctoring and exam integrity, stated as a licence layer

This shelf has carried **Safe Exam Browser** and **SEB Server** as the integrity tier and treated the
category as otherwise unavailable. Three measurements this pass change the menu:

| Layer | Repo / platform | Licence (payload) | Bytes | Commercial consequence |
|---|---|---|---|---|
| Platform (Open edX subsystem) | [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🟡 **AGPL-3.0** | 35119 (`master/LICENSE.txt`) | Network copyleft. Deploy it for a client; **do not embed it in a product you redistribute** |
| Platform (standalone) | [`kamlendras/OpenProctor`](https://github.com/kamlendras/OpenProctor) | 🟡 **AGPL-3.0** | 34523 (`main/LICENSE`) | 🆕 First measurement. Same constraint, no Open edX dependency |
| **Agent** | [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | 🟢 **MIT** | 1068 (`master/LICENSE`) | 🟢 **Permissive, fully local, explainable.** Vendorable into a deliverable |
| **Agent** | [`SuyashMore/AI-Proctored-Examination-System`](https://github.com/SuyashMore/AI-Proctored-Examination-System) | 🟢 **MIT** | 1068 (`main/LICENSE`) | 🟢 Permissive; second independent implementation (© 2020) |

🔴 **Both MIT rows were previously on this KB's reject list, and the gap built on them is withdrawn.**
See `P461` (a `main`-first probe files a `master`-default repo as absent) and `P462` (a declared gap
that rests on one verdict inverts when that verdict does).

🟢 **So the integrity menu for an Open edX or standalone deployment is now three options, ranked:**

1. **MIT proctoring agent outside the platform**, talking to it over APIs — 🟢 **Preferred.** No
   copyleft contact, fully local inference, explainable risk output.
2. **Deploy `edx-proctoring` or `OpenProctor` for the client and self-host** — 🟡 fine; the AGPL
   obligation stays with the instance the client runs.
3. **Embed either AGPL-3.0 platform in a redistributed deliverable** — 🔴 takes network copyleft onto
   the whole product.

⚠️ **This is the same plugin/side-car boundary, now with a fifth and sixth instance:**
`peancor/moodle-mcp-server` and `Jawadh-Salih/moodle-mcp-server` (MIT outside GPL-3.0 Moodle),
Apache-2.0 `XBlock` against AGPL-3.0 `edx-platform`, and now **two MIT proctoring agents outside two
AGPL-3.0 integrity platforms.** 🟢 **Six independent instances: when the platform is copyleft and the
deliverable must not be, the AI goes outside the tree and talks over an API.** That rule has now
survived every category this shelf covers — LMS, gradebook, courseware and exam integrity.

### ⚠️ A customisation caveat specific to proctoring

🔴 **Proctoring is the one category where the permissive licence is not the binding constraint.**
EU **Annex III point 3** covers exam and behaviour monitoring, and Vietnam's **Decree 33** (in force
2026-08-15) classifies AI that *"monitors and analyses learner behaviour with biometric data"* as
high-risk. **An MIT licence does not make a biometric proctoring deployment lawful.** What keeps it
sellable is the *architecture* both MIT agents already have: **on-device processing, frames discarded
after feature extraction, explainable per-signal evidence, and a human gate on every consequential
decision.** 🔵 **Customise toward that shape, never away from it** — a cloud-API rewrite of either
repo would be permissively licensed and unsellable in both regimes.

⏸️ **And the EMEA clock is not the one this shelf used to quote:** Annex III conformity duties are due
**2027-12-02**, deferred by Regulation (EU) 2026/1744; **Article 50 transparency was not deferred** and
has applied since **2026-08-02**. Primary text unverifiable from here (`eur-lex.europa.eu` → **000**).

## 🟢 Thirty-second pass, 2026-10-07 — the Open edX licence split, and a platform claim that was a web server

**Licences read from payload on `raw.githubusercontent.com`, 2026-10-07.** No star counts:
`api.github.com` **403**, github.com landing pages **403** on both HEAD and GET.

### 🔵 Open edX, stated as two licences instead of one

This shelf has carried Open edX for many passes as a single "platform" row. It is **two licences**,
and the split decides the architecture of every engagement on it. Both halves read from payload this
pass:

| Layer | Repo | Licence (payload) | Bytes | Commercial consequence |
|---|---|---|---|---|
| Core platform | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟡 **AGPL-3.0** | 35136 | Network copyleft. **Self-hosting for a client is fine.** Redistributing a modified platform, or running a modified one as your own service, is a licence event |
| Extension point | [`openedx/XBlock`](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** | 11357 (`master/LICENSE.TXT`) | Permissive. This is the surface an agent plugs into — and the surface your deliverable can keep proprietary |

🟢 **So the customisation menu for Open edX is not a matter of preference:**

1. **Agent as an XBlock** — Apache-2.0 extension point, the platform stays untouched. 🟢 Preferred.
2. **Agent as an external service** over Open edX APIs — no copyleft contact at all. 🟢 Preferred.
3. **Fork `edx-platform` to embed the agent** — 🔴 takes AGPL-3.0 onto the whole deliverable.

🔵 **[`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Colombia, added this pass) is a
working instance of shape 1–2**: an MIT tutor agent with TTS, avatar and a teacher analytics panel
living inside an Open edX deployment at Universidad Tecnológica de Pereira, without taking on the
platform's licence. **It is the first Open edX AI reference on this shelf that is both LATAM-origin
and permissively licensed.**

⚠️ **This is the same plugin/side-car boundary pass 30 called this KB's best-evidenced architectural
rule, now with a third and fourth instance:** `peancor/moodle-mcp-server` (MIT *because* it sits
outside GPL-3.0 Moodle), `Jawadh-Salih/moodle-mcp-server` (MIT, Moodle side-car, added this pass),
and now the Apache-2.0 XBlock point against the AGPL-3.0 Open edX core. 🟢 **Four independent
instances: when the platform is copyleft and the deliverable must not be, the AI goes outside the
tree and talks over an API.**

### Platforms added and re-confirmed this pass

| Platform | Repo | Licence (payload) | Region | Role |
|---|---|---|---|---|
| Intel Education AI Suite | [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (11350 B) | Global | Not an LMS — the **AI layer you put on top of one**. Smart Classroom (multimodal session capture → summarisation) and Teaching Assistant (voice-first), on OpenVINO pipelines for Intel CPU / iGPU / NPU, **with benchmarking tools to size the hardware**. 🔵 The only row on this shelf that answers "what will this cost to run on-prem?" |
| Sakai | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** (11120 B) | Global | Apereo-stewarded academic LMS. 🟢 Payload re-read this pass: *"consists of the Apache 2.0 license, modified…"* — **permissive, stays on the allowlist** |
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** (8241 B) | Global | K-12-native **LMS + SIS + fees + parent app on one database**, on the Odoo stack. 🟢 Genuinely LGPL, re-read this pass — **independently corroborates pass 28's negative half**, so the dynamic-linking path for this component is real |

🔵 **Why `education-ai-suite` belongs on the *verticals* shelf and not only with the agents.** Every
other AI row here assumes an API you pay per call. This one assumes **hardware you already own**, and
ships the benchmarking to prove which hardware suffices. For a school district or a public
university — the buyers in this industry — that converts an unbounded recurring cost into a
one-time, sizeable, budgetable capital line. With edtech funding **down 26% YoY**
(`intel/market.md`), that is the difference between a project that gets approved and one that does
not.

### 🔴 `P456` — Forma LMS: the "Apache 2.0" platform claim was a web-server requirement

A secondary source presented **Forma LMS** as *"built for corporate teams that specifically need
Apache 2.0 permissive licensing … an open-source fork of Docebo with Apache 2.0 license, so modified
versions deploy and distribute without the copyleft obligations GPL and AGPL carry."* Probed
first-hand:

- [`formalms/formalms`](https://github.com/formalms/formalms) publishes **no licence payload**.
  `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENSE.TXT`, `LICENCE`, `COPYING`, `COPYING.txt`,
  `license.txt`, `licence.txt`, `docs/LICENSE` and six more names all **404** across `master`,
  `main` and `develop`. The repository is real (`master/README.md` **200**).
- The **only** occurrence of "Apache" in that README is an install prerequisite:
  **`- Apache (recommended) with mod_rewrite enabled`.**

🔴 **A web server in a requirements list became a licence grant, and then became a commercial
conclusion.** The claimed consequence — "deploy and distribute without the copyleft obligations GPL
and AGPL carry" — is exactly what someone would write if they believed *Apache httpd* meant
*Apache-2.0*. ⚠️ Forma LMS's upstream Docebo lineage is **GPL**, the opposite of the claim. **This
pass did not establish Forma's own effective licence** — only that **the repository publishes no
grant**, which is sufficient to keep it out of a deliverable until someone establishes otherwise.

🔵 **The generalisable rule for this shelf, and it applies to every row here.** *Apache*, *nginx*,
*MIT* and *BSD* are each simultaneously the name of a licence and the name of something that is not
a licence. **A licence family appearing in a README's requirements, install or stack section is not
a licence claim.** Combined with pass 30's subject-model finding, the gate is now two questions:
**who is the subject of this licence claim, and what role is the word playing in the sentence?**
Both must be answered before a cell on this shelf is used as a commercial answer.

### 🔴 `P453` / `P454` / `P458` — a correction that affects this shelf's own history

`openedx/XBlock` — a real, correctly licensed Apache-2.0 repository already on this shelf — was
returned **`ABSENT`** by this KB's prober. Three defects stacked:

- **`P453`** `raw.githubusercontent.com` is **case-sensitive**; XBlock's licence is `LICENSE.TXT`
  (caps extension), which was not in the probe list. Negative control:
  `pykt-team/pykt-toolkit/main/LICENSE` **200**, `…/license` **404**, `…/LiCeNsE` **404**.
- **`P454`** the existence fallback probed only `README.md`; XBlock ships **`README.rst`**.
- **`P458`** XBlock's **own README links a licence path that 404s** (lowercase `LICENSE.txt`).
  `pyproject.toml` is the tiebreaker: `license = "Apache-2.0"`,
  `license-files = ["LICENSE.TXT"]`.

⚠️ **Every one of these errs toward deleting a true row**, reported as a 404 — the silent direction.
🔵 **Any `ABSENT` verdict recorded in this KB before this pass should be re-probed** with the
corrected filename list before it is acted on, especially for `.rst`-documented and Python-packaging
projects, where `P453` and `P454` land together.

# Vertical Platforms — Education

Real, deployed education systems that can be customised and extended with AI —
the equivalent of Odoo for ERP or OpenMRS for healthcare. Licenses read from each
repo's own payload on 2026-10-06.

**Read the license column before you plan the architecture.** Most of the
education platform shelf is copyleft. That is not a blocker, but it decides
whether your AI work is a plugin (and inherits the license) or a side-car (and
does not).

## 🟢 Thirtieth pass, 2026-10-07 — the plugin/side-car boundary is now the KB's best-evidenced architectural rule

🔴 **Execution of this tree's suites was DENIED this pass** (`[Code from External]`); nothing below is
a re-measurement (`P107`). It is a reading of this KB's own prose against pass 28's flagged rows.

🟢 **The sentence at the top of this file turns out to be the single most load-bearing claim in the
KB, and pass 29 found it independently.** Pass 28's reconciler flagged
[`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) as self-contradictory
because the corpus names both **MIT** and **GPL-3.0** for it. It is not a contradiction — it is this
file's rule, stated correctly:

> *"MCP server exposing Moodle data to agents from **outside** the Moodle tree — which is why it is
> **MIT** while in-tree Moodle plugins are **GPL-3.0**."*

🔵 **Both licences are true, of two different things, and the boundary between them is the deliverable
decision.** Same shape, same conclusion, three more rows:

| Platform | In-tree licence | Side-car option | What it means for an engagement |
|---|---|---|---|
| **Moodle** | **GPL-3.0** (plugins inherit) | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) — **MIT**, external process over the web API | the canonical case: keep AI work out of the tree and the studio's IP stays the studio's |
| **Sakai** | **ECL-2.0** — permissive | in-tree is already safe | 🟢 **ECL-2.0 is the Apache-2.0 text**; pass 28's reconciler flagged Sakai and Opencast for naming both, and **both families are true** |
| **Opencast** | **ECL-2.0** — permissive | in-tree is already safe | same lineage; stays on the permissive allowlist |
| **Open edX** | **AGPL-3.0** — the strongest copyleft on this shelf | side-car only | the AGPL's network clause is why the side-car pattern is not optional here |

⚠️ **The `license:` filter trap, which belongs in this file because it decides shortlists.** A
shortlist built with `license:mit OR license:apache-2.0 OR license:bsd` **silently drops ECL-2.0**,
and with it Sakai and Opencast — the only copyleft-free options among the traditional big LMSs. This
KB has now hit that filter defect twice from opposite directions: once as a dropped platform, and
once as [`aryankeluskar/canvas-mcp`](https://github.com/aryankeluskar/canvas-mcp), whose **ISC**
licence was read *as three licences* because the filter string sat in its description. 🔵 **Put
`ECL-2.0`, `ISC` and `PostgreSQL` on the allowlist explicitly** — the note further down this file
already says so, and pass 29 is the second independent arrival at it.

## 🔴 Licence corrections — twenty-eighth pass, 2026-10-07

Two platforms on this shelf were filed **LGPL** and are **GPL-2.0** (`P452`), and both are
administrative systems a client deploys and extends rather than links as a library — so the
correction tightens rather than relaxes the architecture:

| Platform | Was | 🔴 Is | Region | Consequence |
|---|---|---|---|---|
| [`OpenEMIS/core`](https://github.com/OpenEMIS/core) · [`openemis/core`](https://github.com/openemis/core) | LGPL | **GPL-2.0** | Global | ministry-scale education MIS. 🔴 **Two rows, one repository** — this shelf double-counts it under two case spellings |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | LGPL | **GPL-2.0** | LATAM | Brazil's most-deployed municipal school system. A ministry deliverable that **links** it inherits the obligation; extending it in-place and returning the source does not |

**The cause** was a truncation window, not a misreading: `family_of` probed LGPL before GPL over the
first 4000 characters, and GPL-2.0's Preamble recommends the LGPL at character 784 while GPL-3.0's
closing notes do so at 34,143. Every GPL-2.0 payload was filed LGPL.

⚠️ **And the EMEA assessment tier, for the same reason:** `oat-sa/lib-lti1p3-core` (**GPL-2.0**) and
`Citolab/qti-components` (**GPL-3.0**) are the certified, most complete LTI 1.3 and QTI options and
**neither is LGPL**. There is no linking exception on either. See `repos/foundations.md`.

🔵 **The OpenStax split, re-confirmed through a new channel.** This file already says to *"take the
content, not the CMS"* because `openstax/openstax-cms` is AGPL-3.0. The content side now needs the
same precision: [`openstax/osbooks-biology-bundle`](https://github.com/openstax/osbooks-biology-bundle)
is **`CC BY-NC-SA 4.0`**, not `CC BY` — **NonCommercial**, so it cannot be resold inside a
commercial courseware product. That independently corroborates `P328` (OpenStax cession narrows
between editions). Verify cession **per collection**, not per bundle.

🟡 **The EUPL tier binds hosted services.** Nine EMEA public-sector repositories on this shelf are
EUPL (eight Finnish national services plus the European Commission's data model), and **EUPL
Article 1's "Communication" covers network use** — so for a managed service delivered to a European
ministry the EUPL behaves like the AGPL, not like the MPL.

## Learning platforms

| Platform | Repo | License (read from payload) | Position |
|---|---|---|---|
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 (`COPYING.txt`) | Still the most widely deployed and most customisable open source LMS in 2026: 2,000+ plugins, 20-year community. The default incumbent you will meet in an engagement. |
| Open edX | [openedx/edx-platform](https://github.com/openedx/edx-platform) | AGPL-3.0 (`LICENSE`) | Built at Harvard/MIT scale. Strong assessment engine, cohorts, analytics. Used by edX, IBM, Microsoft. Pick it when the cohort is large and assessment is central. |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 (`LICENSE`) | Dominant in North American higher ed. Ruby on Rails; needs real Rails operations capability to self-host. Best AI entry point is its API via MCP, not a fork. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 (`LICENSE`) | 30M+ users, unusually strong Spanish-language and LATAM institutional presence. The pragmatic choice for a Spanish-first public-sector deployment. |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** (`LICENSE`) | Higher-ed collaboration and learning environment. Educational Community License 2.0 is an Apache-2.0 derivative — **permissive**, and the only copyleft-free option among the traditional big LMSs. Underrated for this reason. |
| ILIAS | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 (`LICENSE`) | Strong in German-speaking Europe, workplace training and SCORM-heavy compliance training. |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** (`license.txt`) | Modern, fast to deploy via Docker. **Commonly mis-reported as MIT** by LMS comparison articles — it is AGPL-3.0. Verified at `license.txt`; `LICENSE` is a 404, which is how the error spreads. |
| Kolibri | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`LICENSE`) | Offline-first platform for teaching without internet. Default choice for low-connectivity, low-budget and equity-driven deployments. *(Earlier passes called this "the only fully permissive end-to-end platform on this shelf" — no longer true: see Mentingo below, MIT, and Oppia, Apache-2.0.)* |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** (`LICENSE`) | Authoring and delivery of interactive lessons with misconception handling built into the pedagogy. Permissive, and designed for learners with limited educational resources. |
| Mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** (`LICENSE`) | **Added third pass, 2026-10-06 — and it changes the shape of this shelf.** Self-hosted, multi-tenant, white-label LMS with a **built-in AI mentor**, built for corporate L&D, onboarding and compliance rather than academic use. 91★, 29 forks, TypeScript, maintained by Selleo (Poland). The second fully permissive end-to-end platform here and **the only AI-native one**. |
| Coursemology | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`, © 2023 Coursemology.org) | **Added fifth pass, 2026-10-06.** NUS-origin gamified LMS — Rails 8 API, React client, Keycloak auth, **15,802 commits**, 158★, 78 forks. "Currently supported by the AI Centre for Educational Technologies" and the host platform for Singapore's **Codaveri** AI programming tutor. The **third** fully permissive end-to-end platform here, the only one with a decade-scale commit history, and the strongest fit for **CS and programming teaching in higher education**. Read the concentration-risk note below before proposing it. |
| Sunbird | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** (`master/LICENSE`) | **Added sixth pass, 2026-10-06 — found in an earlier pass and never shelved here.** EkStep Foundation's platform, deployed as India's **DIKSHA** national school platform and recognised a **Digital Public Good**. **41★ / 317 forks / 38,046 commits** — a 7.7x forks-to-stars inversion. 18+ languages, NCERT/CBSE/SCERT curricula, 100+ micro-services. The **fourth** fully permissive end-to-end platform here and **the only one proven at nine-figure learner scale**; its 100+ services are the operational cost. Full entry at the end of this file. |

## Content, assessment and delivery components

| Component | Repo | License (read from payload) | Use |
|---|---|---|---|
| Open edX deployment | [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 (`LICENSE.txt`) | The Docker-native way to actually run Open edX. Do not hand-roll an edX deployment. |
| Open edX analytics | [openedx/openedx-aspects](https://github.com/openedx/openedx-aspects) | Apache-2.0 (`LICENSE`) | Learning analytics stack for Open edX — permissive even though the platform is AGPL. |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 (`LICENSE.txt`) | Interactive content types; embeds in Moodle, Canvas and Drupal. The common currency of interactive exercises. |
| Anki | [ankitects/anki](https://github.com/ankitects/anki) | AGPL-3.0 (`LICENSE`) | Spaced repetition with a mature scheduling algorithm. Reference implementation for retention mechanics. |
| Open Badges validation | [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 (`LICENSE`) | Verifiable credentials and competency claims. |
| LTI 1.3 tool provider | [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 (`LICENSE`) | The permissive integration doorway into any of the copyleft platforms above. |
| Opencast | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (`LICENSE`) | Lecture capture and video management, widely deployed in higher ed. Permissive (Apache-2.0 derivative). Integrates with Moodle, Canvas and Sakai. |

## Administrative systems — SIS and education ERP

Added 2026-10-06 (second pass). The learning shelf above is only half the estate.
Admissions, enrolment, fees, attendance, examinations, library and HR run on a
*student information system* or an education ERP, and this is where a large share
of real institutional spend and automation work sits. Licences read from each
repo's own payload.

| Platform | Repo | Licence (read from payload) | Position |
|---|---|---|---|
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (`LICENSE@master`) | Education ERP on the Odoo framework. Python, v19.0, 884★, 775 forks, 1,710 commits. Admissions, student info, courses, exams, finance, attendance, library, HR. **The licence is the point — see below.** |
| ERPNext | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (`license.txt@master`) | General ERP with an education module (students, programmes, fees, assessment). Same lowercase-`license.txt` trap as `frappe/lms`: a probe of `LICENSE` returns 404. |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 (`LICENSE@main`) | School management: timetabling, attendance, markbook, pastoral care. Strong K-12 fit. |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** (`LICENSE@master`) | Student information system, PHP/PostgreSQL, strong multilingual support including Spanish — relevant to LATAM public sector. GPL-**2.0**, so it is not licence-compatible with GPL-3.0-only code. Check before combining. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (`docs/License.txt@master`) | Student information system: scheduling, grades, attendance, billing. Its licence lives in a **subdirectory**, not at the repo root — see the method note in `repos/foundations.md`. |
| Apache OFBiz | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | **Apache-2.0** (`LICENSE@master`) | Not education-specific, but a genuinely permissive ERP/CRM framework (Java). The fallback when an institution needs admin automation with no copyleft exposure and no Odoo dependency. |

### LGPL-3.0 is the middle path, and it changes the architecture menu

This KB has treated licences as binary: permissive, so build reusable IP; or
copyleft, so build a side-car. OpenEduCat's **LGPL-3.0** is a third position, and
the project chose it deliberately — LGPLv3 lets an institution extend the
platform with **proprietary modules** (an integration with a confidential research
system, licensed third-party content) without being forced to open-source those
modules.

**Consequence:** against an LGPL-3.0 platform, an in-tree-style *module* is a
viable commercial shape. You are not pushed to a side-car to protect your IP the
way Moodle (GPL-3.0) and Canvas/Open edX (AGPL-3.0) push you. Changes to
OpenEduCat's own LGPL files stay LGPL; a separate module linking against it need
not. On the admin side the menu is two options, not one — and OpenEduCat is a
live, maintained platform (884★, 775 forks, v19.0), not a curiosity.

**The boundary still has to be real.** LGPL's distinction between *modifying the
library* and *linking to it* is only as sound as your module boundary. Fork
OpenEduCat's own files and you are in LGPL territory for those files. Keep the
module separate, talk to it through documented interfaces, and the proprietary
part stays proprietary.

## Mentingo — the first MIT, AI-native LMS on this shelf, and what it breaks

Added in the third pass of 2026-10-06. Licence read from payload: **MIT**. It
deserves its own section because three of this KB's standing positions have to be
restated around it.

### Verified specification

| Axis | Value (2026-10-06) |
|---|---|
| Licence | **MIT**, read from `LICENSE`. Its own README states the intent plainly: *"MIT - modify, white-label and resell, no copyleft obligation"* |
| Scale | 91★, 29 forks, TypeScript |
| Maintainer | **Selleo** (Poland) — a product engineering company, building learning platforms since 2005. EMEA-origin |
| Target | Corporate L&D, employee onboarding, compliance training — **not** academic |
| Tenancy | Multi-tenant, white-label |
| AI | Voice **and** chat AI mentor running real-time role-play for sales, compliance and customer-support scenarios, **scored automatically**; automated grading of open-ended behavioural and problem-solving answers with actionable feedback; AI-assisted course generation from existing documentation |
| AI stack | Vercel AI SDK + OpenAI, LangChain, **pgvector** retrieval, **LiveKit** real-time voice, **Langfuse** tracing of every model call |
| LMS core | Course catalogues, lesson delivery, enrolment, learner progression, role-based access (admin / content creator / learner), group-based course-access inheritance, completion records, per-learner analytics, certificates with expiry and recertification |
| Interop | **SCORM 1.2 export**, OpenAPI/Swagger with a generated typed client, CSV and XLSX bulk import/export |
| Runtime | Node.js 22+, PostgreSQL 16 + pgvector, Redis, S3-compatible storage. One-click CloudFormation deployment from AWS Marketplace |

### What it breaks, and what it does not

**1. The licence menu on the platform layer is no longer "copyleft or side-car."**
This KB's central architectural finding — AI built inside a copyleft LMS inherits
that LMS's licence, so prefer the permissive side-car — was derived from Moodle
(GPL-3.0), Canvas and Open edX (AGPL-3.0). Against Mentingo there is no copyleft to
route around: you can fork the platform itself, extend it in TypeScript, brand it
and **resell** it. For an enterprise L&D engagement that is a different commercial
shape from everything else on this shelf, and a stronger one than the side-car,
because the deliverable is the whole product rather than an attachment to someone
else's.

**2. The "no permissive auto-grader" gap is narrowed, not closed.** Mentingo grades
open-ended behavioural and problem-solving answers automatically, under MIT. It
does **not** supply a rubric- or curriculum-aligned academic grader, and it changes
nothing about oversight: EU AI Act Annex III, the Oklahoma and Maryland statutes
and Korea's high-impact classification are indifferent to the licence. Keep the
human gate on consequential scores. See the narrowed gap statement in
`agents/top.md`.

**3. It is an L&D product, so do not mis-sell it into academia.** No SIS
integration, no LTI 1.3, no gradebook semantics for credit-bearing courses, no
institutional reporting. It exports **SCORM 1.2**, which is the L&D interchange
format, not an academic one. The honest framing: *for a corporate client,
Mentingo is a candidate platform; for a university, it is a reference
implementation and a component donor.*

### What to take from it even when you do not deploy it

Two engineering choices generalise to every pattern in this KB:

- **pgvector inside PostgreSQL instead of a separate vector database.** One fewer
  component to host, secure and keep in-region — which matters most in exactly the
  EMEA residency and LATAM cost scenarios where the component budget is tightest.
- **Langfuse tracing from day one.** Per-call cost, latency and actual model output,
  inspectable. This is an EU AI Act Annex III-shaped audit artefact produced as a
  by-product of normal operation rather than assembled as a compliance project.
  Wire it into the side-car patterns too.


## Added in the eighth pass of 2026-10-06 — the offline-first delivery tier, and why it is a platform question

Every platform on this page assumes a network. **The eighth pass found the tier
underneath that assumption**, and it changes the LATAM and MEA architecture
conversation from a feature trade-off into a platform selection.

### The constraint, now with numbers instead of adjectives

`LabSirius/TutorIA`'s requirements specification (**MIT**, Universidad
Tecnológica de Pereira, Colombia — see `agents/top.md`) states the rural-access
envelope as a **testable acceptance criterion**, which no platform page in this
KB previously had:

> **RNF-04** — *"Compatible con dispositivos con mínimo **2GB de RAM**;
> funcional con conectividad de **3G**."*

And it states the governing privacy regime for the same deployment:

> **RNF-05** — *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with
> **TLS** in transit and **AES-256** at rest.

**Use these two lines as the intake questions for any LATAM education platform
selection.** They are citable, institutionally authored, and permissively
licensed.

### The platform answer, which is Kolibri — and the reference implementation, which is new

| System | Repo | Licence (payload) | Role in this tier |
|---|---|---|---|
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`master/LICENSE`, © 2021 Learning Equality and other contributors) | **The platform.** Purpose-built for schools with no reliable internet; the only permissive, maintained, genuinely deployed offline-first LMS on this page |
| Kolibri Studio | [learningequality/studio](https://github.com/learningequality/studio) | **MIT** (`master/LICENSE`, Foundation for Learning Equality) | Curriculum authoring and channel curation for Kolibri |
| Kolibri for Android | [learningequality/kolibri-installer-android](https://github.com/learningequality/kolibri-installer-android) | **MIT** (`master/LICENSE`, © 2023) | The 2 GB-RAM delivery target of RNF-04 |
| **EduFlow** | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) | **MIT** (© 2026 CAi UC — **holder flagged**, see `agents/top.md`) | **Not a platform — a readable reference implementation** of the offline-sync pattern, 41 commits |
| RACHEL | [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **CC BY-SA-NC — README only, no payload** | **RESOLVED in the ninth pass, and it is NOT shippable.** The org is `rachelproject`; `contentshell` *is* the RACHEL CMS. No licence payload across 8 filenames × 2 branches; the README declares *"Creative Commons - BY, SA, NC"* — a content licence over PHP software, carrying **NonCommercial**. Cite as prior art, never ship. See the ninth-pass section below |

All three Learning Equality licences were **re-confirmed from payload this
pass**.

### What EduFlow contributes that Kolibri does not

Kolibri is the right platform and it is a large system. **EduFlow is ~41 commits
and shows the mechanism in a form an architect can read in an afternoon:**
teacher opens a room and shares a **6-character code**; the student downloads
the assignment while in signal — **~8 KB for 10 exercises**, because a maths
problem is text — solves it **entirely offline** with immediate correction via
**IndexedDB** plus a **Service Worker** app-shell cache, and answers **sync
automatically** on reconnection. FastAPI + Next.js PWA + Supabase.

Its own problem statement is the sharpest on this page: *"Las plataformas
educativas que existen — Khan Academy, Google Classroom, Kahoot — **asumen
conexión permanente**. En un colegio municipal con internet intermitente eso las
vuelve inservibles."*

### The selection rule this adds to the page

**If the deployment has intermittent connectivity, offline-first is a platform
decision and not a feature you add later.** Retrofitting sync onto a
network-assuming LMS means rebuilding its data layer; choosing Kolibri means
accepting its content model from day one. **Decide this before the LMS
shortlist, not after** — and note that this is the one tier of the education
platform shelf where the permissive option (**Kolibri, MIT**) is also the best
option, which is not true of the LMS tier (Moodle, Chamilo, ILIAS — all
copyleft) or the ERP tier (**OpenEduCat, LGPL-3.0**).

## The Kuali estate — one higher-ed consortium, three different licences

Added in the third pass of 2026-10-06. The admin shelf above was missing the
institutional-grade higher-education option, so this pass probed **Kuali** (formed
2004 on an Andrew W. Mellon Foundation grant, backed by 24+ universities).

| Repo | Product | Licence (read from payload) | Status |
|---|---|---|---|
| [KualiCo/rice](https://github.com/KualiCo/rice) | Kuali Rice — higher-ed application framework and middleware | **ECL-2.0** (`LICENSE.txt`) — **permissive** | 4★, 12 forks, Java. **Maintenance mode** by its own README: maintained for "security, bug fixes, and minor enhancements while its replacements are being developed" |
| [kuali/rice](https://github.com/kuali/rice) | same, older location | **ECL-2.0** (`LICENSE.txt`) | **DEPRECATED** — its README's first line points to `KualiCo/rice`. Pin the KualiCo location |
| [kuali/kfs](https://github.com/kuali/kfs) | Kuali Financial System | **AGPL-3.0** (`LICENSE`) | network copyleft |
| [kuali/kc](https://github.com/kuali/kc) | Kuali Coeus — research administration | **AGPL-3.0** (`license.txt`, lowercase) | network copyleft, **and** the lowercase-`license.txt` trap again |
| `kuali/student`, `KualiCo/student`, `kuali/coeus` | Kuali Student (the SIS) | — | **not reachable**: `README.md` 404s on all three. The SIS is not at the path its name implies |

**Two usable conclusions.**

**ECL-2.0 belongs on your permissive allowlist.** It is the Apache-2.0 text with
the patent grant narrowed to education, and it now appears three times on this
shelf — Sakai, Opencast and Kuali Rice. A licence filter that allowlists only
`MIT / Apache-2.0 / BSD` will **reject three genuinely permissive higher-education
platforms.** Fix the filter, not the finding.

**A consortium is not a licence.** "Kuali is ECL-2.0" is true of Rice and false of
KFS and Coeus. The diligence unit is the repository — never the foundation, the
vendor or the brand. This is the `frappe/lms` (AGPL) beside `frappe/erpnext` (GPL)
lesson, now in its harder form: here the **permissive** member is the one you meet
first in the documentation, so the optimistic reading is the one that sticks.

**And read the maintenance banner before the licence.** Rice is permissive *and*
parked. Permissive-but-parked is a real category: fine to vendor and fork, wrong to
present to a client as a living upstream. Recorded as qualified, not recommended.

## OpenMAIC — a permissive platform that generates the course, not just the tutoring

Added in the fourth pass of 2026-10-06. Every other platform on this shelf is a
**container** for content a human authored (Moodle, Canvas, Open edX, Mentingo).
[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) is the first entry that
**produces the content itself**, which puts it in a different column of the
selection table rather than in competition with the LMSs.

### Verified specification

| Axis | Value (read 2026-10-06) |
|---|---|
| Repo | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) |
| Licence | **MIT**, read from the `LICENSE` payload (© 2026 THU-MAIC) |
| Stars | **40.0k** — the largest permissive asset in this KB |
| Origin | **Tsinghua University** (THU-MAIC) |
| Version | **v1.2.0-rc.1**, pre-release, 2026-10-04 |
| Stack | TypeScript, Next.js, React, **PostgreSQL** |
| Input | a topic description, or an uploaded document |
| Output | slides, quizzes, interactive **HTML simulations**, project-based-learning scenes; **exports PPTX and interactive HTML** |
| Delivery | **AI teacher agent + AI classmate agents**, shared whiteboard, text-to-speech |
| Integration | exposed to agent workbenches (OpenClaw) — generate a classroom from a chat client or IDE |

### Why the v1.2.0 architecture change is the part that matters commercially

v1.2.0 moves generation **server-first with PostgreSQL persistence**, so a course
build **survives a closed browser tab or a server restart.** Everything else on
the agent shelf in this KB generates in-session.

Three consequences:

1. **It is the only generator here you can put behind a review queue without
   rebuilding its execution model.** A durable server-side job is already the right
   shape for the `WAITING_REVIEW` gate that trend 16 and the EU AI Act both
   require. Pattern **P11** does exactly this.
2. **PPTX and HTML export means the artefact outlives the platform.** A district
   that will not host a Chinese-origin application can still take the deck. That
   makes a **generate-then-export** engagement viable where a deployment is not.
3. **It composes with, rather than replaces, the LMS shelf.** OpenMAIC authors;
   Moodle, Canvas or Open edX deliver and record. Wire them with the MCP servers
   already catalogued in `agents/top.md`.

### The one thing to settle in week one

**It is MIT, and it is Chinese-origin.** The licence is clean and permissive —
there is no legal obstacle. But a public-sector buyer in EMEA or North America
will ask about provenance and data residency, and the honest answer is that
**generation is server-side**, so where that server runs is a decision, not a
default. Self-host it, pin a **reviewed fork**, and point inference at whatever
model the client's data-residency posture allows (the KB's sovereign and local
inference options apply unchanged). Raise this yourself in week one; do not let a
procurement reviewer raise it in week eight.

## What the permissive platforms install — twenty-first pass of 2026-10-06

⚠️ **This file's job is to say which platforms can be customised with AI on top. That recommendation
has always rested on the platform's own licence. For the two permissive platforms measured this pass,
the platform's licence is not the whole answer.**

Measured first-hand from PyPI on 2026-10-06, depth 1. Instrument:
`compose/code/dependency-licence-closure/`.

| Platform | Platform licence | Direct deps | Closure verdict | What a deployment has to decide |
|---|---|---|---|---|
| **Oppia** | Apache-2.0 | **152** | 🔴 **REVIEW-STRONG** | `mutagen` is **`GPL-2.0-or-later`** (audio metadata). Clear that one path, or drop the feature that reaches it. 148 of 152 deps are clean |
| **Kolibri** | MIT | **32** | ⚠️ **REVIEW-WEAK** | 2 LGPL (`json-schema-validator`, `zeroconf-py2compat`) — linkable, shippable, but they travel with the offline bundle |
| **Mentingo** | MIT | **not measured** | ⚠️ **UNMEASURED** | pnpm **workspace root**: its root manifest carries only `devDependencies`, so the runtime closure is in `apps/*` and this pass did not reach it. ⚠️ **Unmeasured is not clean** |

🔵 **Why this belongs in the verticals file and not only in the agents file.** The copyleft platforms
here — Moodle GPL-3.0, Open edX and Canvas AGPL-3.0 — are *already* copyleft, so this KB's standing
advice is to keep Globant IP in an external side-car over LTI 1.3 or MCP. That advice is unchanged.
🔴 **What changes is the advice for the permissive platforms**, which were the escape hatch: *"pick
Kolibri or Oppia and you avoid the copyleft question entirely"* was the shortcut, and at depth 1 it is
**not quite true for either of them**. The escape hatch is still the right call — the obligations are
narrow and attach to specific features — but it is **narrow, not absent**, and a proposal that
promised "no copyleft anywhere" on an Oppia build would have been wrong.

⚠️ **Limits, so the table is not over-read:** depth 1 only (transitive deps unmeasured), linkage not
analysed, and `REVIEW-*` means *"look at this row"*, not *"violation"*. The one hard class,
`BLOCKER` (a non-commercial grant), **was not triggered by any platform on this shelf.**

## AI integration surfaces, by strategy

Two ways to put AI on a platform, with different license outcomes:

**In-tree plugin — inherits the host license.** All three Moodle AI plugins
probed this pass are GPL-3.0: [moodle-block_openai_chat](https://github.com/Limekiller/moodle-block_openai_chat),
[moodle-local_aiquestions](https://github.com/yedidiaklein/moodle-local_aiquestions),
[moodle-qbank_genai](https://github.com/cgrevisse/moodle-qbank_genai). Use these
as references and as drop-in capability for a single client; do not use them as
the base of reusable studio IP.

**External side-car over MCP or LTI — stays permissive.**
[peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) (MIT)
and [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
102 tools, 8 agent skills, WCAG scanner) reach the same data from outside the
tree and keep their permissive license. This is the recommended shape for
anything Globant intends to reuse across engagements.

## Platform selection shortcut

| If the client… | Start from |
|---|---|
| already runs an LMS (most of them) | leave it alone; integrate via MCP / LTI 1.3 side-car |
| needs permissive IP with no copyleft exposure | Sakai (ECL-2.0), Oppia (Apache-2.0) or Kolibri (MIT) |
| has low or intermittent connectivity | Kolibri + ricecooker, fully MIT |
| is Spanish-first public sector in LATAM | Chamilo (GPL-3.0) — deployment and localisation work |
| needs assessment at cohort scale | Open edX via Tutor, plus openedx-aspects for analytics |
| is a Microsoft-stack enterprise L&D buyer | Moodle or Frappe LMS with a MAF-based side-car |
| needs admin/SIS automation (admissions, fees, exams) | OpenEduCat (LGPL-3.0) — and a proprietary module is a legitimate shape here |
| needs admin automation with zero copyleft exposure | Apache OFBiz (Apache-2.0) |
| is Spanish-first K-12 public sector needing an SIS | RosarioSIS (GPL-2.0) — note GPL-2.0, not 3.0 |
| is a corporate L&D / onboarding / compliance-training buyer | **Mentingo (MIT)** — fork it, white-label it, resell it; no copyleft to route around |
| needs permissive higher-ed middleware / workflow | Kuali Rice (**ECL-2.0**) at `KualiCo/rice` — permissive, but in maintenance mode |
| needs spaced-repetition / retention mechanics reached by an agent | `ankimcp/anki-mcp-server` (MIT, 53 tools) over Anki, or OpenTutor (MIT) for FSRS built in |
| needs a whole course generated from documents, not just a tutor | **OpenMAIC (MIT, 40.0k★)** — self-host a reviewed fork; put the gate of pattern P11 in front of it |
| needs generated teaching material but cannot host the generator | **OpenMAIC's PPTX / interactive-HTML export** — generate outside, deliver the artefact in the client's own LMS |
| needs to choose *which model* should teach | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT) — scores pedagogical knowledge, not task accuracy |
| teaches **programming or CS** in higher ed and wants to own the platform | **Coursemology (MIT)** — autograded assignments, gamification, 15,802 commits; accept the 158★ concentration risk, see below |
| needs teacher-side lesson plans and question banks, not a student tutor | **[microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) (MIT)** — curriculum → lesson plan + assessments → DOCX/PPT/handouts, with a human-curator ingestion gate |
| is **CBSE/NCERT**-aligned and model-sovereignty constrained | **[Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) (MIT)** — grades 9–12 on open-weight Gemma only; reuse its synthetic-generation copyright argument either way |
| must evidence **EU AI Act** conformity for an education system | **[AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) (MIT)** + an Annex III point 3 profile you write — pattern **P13** |

## Coursemology — the third permissive platform, and the first with a long commit history

**Added in the fifth pass of 2026-10-06.** Found by institution-first search, not
by topic page or star ranking, which is why four earlier passes missed it.

### Verified specification

| Axis | Value |
|---|---|
| Repo | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) |
| Licence | **MIT**, read from `master/LICENSE` (© 2023 Coursemology.org). `main/LICENSE` is a 404 — the default branch is `master` |
| Scale | 158★, 78 forks, **15,802 commits** |
| Stack | Rails 8.0.5.1 API + React client + **Keycloak** authentication — three components, not one |
| Origin | National University of Singapore; Prof Ben Leong, NUS Computing |
| Current backing | "Currently supported by the **AI Centre for Educational Technologies**" (AICET) |
| AI today | **Codaveri**, AICET's personalised programming tutor, is deployed on coursemology.org — 30,000+ pieces of personalised feedback since 2024. **Codaveri itself is closed source** |
| Design centre | Gamified learning: autograded programming assignments, achievements, levels, experience points |

### Why it matters commercially

It resolves a tension that has run through this whole shelf. Every mature,
widely-deployed LMS here is GPL-family — Moodle, Open edX, Canvas, Chamilo,
ILIAS, Frappe LMS. Every permissive one has been either young (Mentingo, 91★),
offline-specialised (Kolibri) or authoring-focused (Oppia). Coursemology is the
first that is **both permissive and long-lived**: a client can fork it, rebrand
it, embed proprietary modules and resell it, with a codebase that has over
fifteen thousand commits behind it.

For a **programming or computer-science teaching** engagement it is the strongest
fit on this shelf, because that is what it was built for: the autograder,
submission handling and gamification are native, not bolted on.

### The risk, stated plainly

**158★ is a small contributor base for a platform of this size, and maintenance
is realistically NUS-dependent.** You are trading a copyleft obligation for a
concentration risk. Size that trade explicitly in week one:

- Will the client's own engineers maintain the fork? If not, Coursemology is the
  wrong answer and Moodle is the right one.
- Does the engagement need a plugin ecosystem? Moodle's 2,000+ plugins have no
  equivalent here.
- Is the Keycloak dependency compatible with the client's identity estate? This is
  not a single-container deployment.

### What AICET tells you about the AI layer

AICET's three products — **Codaveri** (programming tutor, 30,000+ feedback items
since 2024), **Softmark** (exam-script digitisation and concurrent team marking,
70,000+ scripts in 2025, now grouping similar answers with computer vision) and
**ScholAIstic** (multi-agent platform letting educators author their own
specialised chatbots; deployed in Social Work, Law and Nursing at NUS since June
2024) — are **all closed source**, all funded by Singapore's Smart Nation and
Digital Government Office, and all working with the **Ministry of Education**.

Two things follow:

1. **The reference architecture is validated and the implementation is not
   available.** A ministry-scale deployment of exactly the shapes this KB
   recommends — side-car tutor on an open LMS (P1), gated grading (P11),
   educator-authored agents (P8) — exists, works at 70,000-script scale, and
   cannot be forked. Cite it as proof the shape works; build the shape yourself.
2. **ScholAIstic is the most interesting of the three to replicate.** Educators
   authoring their own roleplay chatbots for professional-skills training, scaled
   across unrelated faculties, is a product shape with no permissive equivalent
   anywhere in this KB. Pattern **P8** (course materials → Agent Skills) is the
   closest thing here, and it stops short of letting a non-technical educator
   author and publish one.

## Sunbird — the fourth permissive platform, and the only one at nine-figure scale

Promoted to this file in the sixth pass of 2026-10-06. **It was found in an
earlier pass, recorded in `repos/trending.md`, and never shelved here** — so five
rebuilds of this file presented Moodle, Open edX, Canvas, Mentingo, OpenMAIC and
Coursemology without it. The filing failure is written up in `repos/trending.md`,
sixth pass, Finding 1.

### Verified specification

| Field | Value |
|---|---|
| Repo | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) |
| Licence | **MIT**, read from `master/LICENSE` |
| Signals | **41★ · 317 forks · 38,046 commits** · not archived |
| Built by | **EkStep Foundation** (India) |
| Deployed as | **DIKSHA** — India's national school-education platform, run with NCERT/CIET |
| Status | **Digital Public Good**, recognised by the Digital Public Goods Alliance |
| Scale | README mission: *"improve learning outcomes for 200 million children across India"* |
| Localisation | **18+ languages**; **NCERT, CBSE and SCERT** curricula |
| Architecture | **100+ micro-services** offered as building blocks, not a monolith |

### Why it belongs on the shortlist

**It is the only platform on this shelf that is simultaneously MIT and proven at
national scale.** Coursemology's 15,802 commits made it this KB's "permissive LMS
with real history"; Sunbird has **38,046** and a deployment measured in hundreds
of millions of learners. For a ministry, state or large-system engagement, that
combination — permissive licence, DPG status, curriculum alignment already built,
multilingual by construction — is the strongest commercial position in this file.

**The forks-to-stars inversion is the signal to read.** 41 stars against **317
forks** is **7.7×**, the pattern an earlier pass established for infrastructure
that people deploy rather than admire. Judged on stars, Sunbird looks like a
hobby project; judged on forks and commits, it is the most-deployed platform here.

**It pairs directly with the sixth pass's language shelf.** Sunbird is already
18-language; `AI4Bharat/IndicTrans2` (MIT, 22 scheduled languages),
`Indic-TTS` (MIT, 13 languages) and `IndicWav2Vec` (MIT, ASR) are all MIT and all
from IIT Madras. **A Sunbird deployment and its language layer can be assembled
entirely from MIT components** — the only place in this KB where that is true of a
whole stack. See `repos/foundations.md` and pattern **P16**.

### The risks, stated plainly

- **The micro-service count is the cost.** 100+ services is an operations
  commitment, not a convenience. Scope the DevOps work explicitly; the
  `project-sunbird/sunbird-devops` repository (MIT, 62★ / 392 forks) exists
  precisely because this is the hard part.
- **It is built around Indian curricular structures.** NCERT/CBSE/SCERT alignment
  is a feature in APAC and **work to be undone** elsewhere. Do not propose it for a
  North America or EMEA engagement as a drop-in; propose Coursemology or Mentingo
  there.
- **41 stars means a thin public community relative to its scale.** Expect
  institutional documentation and ministry-grade deployment guides rather than
  Stack Overflow answers. Budget for reading source.

## Added in the seventh pass of 2026-10-06 — the Fedena question, closed properly

Earlier passes left this open, and it is worth closing because **Fedena is one of
the names a client will raise** when asked about open source school ERP: a
secondary source calls `projectfedena/fedena` *"the official GitHub repository"*
and attributes **Apache-2.0** to it, while the probe of that owner returned
nothing. This pass enumerated the owners.

| Owner | Does the tree resolve? | Licence payload |
|---|---|---|
| `projectfedena/fedena` — the "official" org per the secondary source | **No.** 404 on `README.md`/`readme.md` and on five licence filenames, across `main` and `master` | None readable |
| [`foradian/fedena`](https://github.com/foradian/fedena) — **Foradian, the vendor that built Fedena** | **Yes.** `README.md` 404s on every branch, but `master/config/routes.rb` and `master/Gemfile` return **200** — the Rails tree is there | **None.** 7 licence filenames probed across 8 branches |
| [`mazhar266/fedena`](https://github.com/mazhar266/fedena) — mirror, 5★ | **Yes**, on `master` only (`main` 404s) | **Apache-2.0 at `master/LICENSE.md`** — and `master/LICENSE` is **404** — plus `master/NOTICE`: *"Fedena — Copyright 2011 Foradian Technologies Private Limited"* |

**The answer, and it is more favourable than the earlier passes could show.** The
grant is **Apache-2.0 and it is the vendor's own**: the `NOTICE` file in the
mirror names **Foradian Technologies Private Limited** as the copyright holder,
and Apache-2.0 §4(d) is precisely the clause that requires that NOTICE to travel
with redistributions. So this is not a third party attaching a licence to someone
else's code — **it is Foradian's Apache-2.0 release, preserved in a mirror while
the vendor's own current GitHub org no longer carries the file.**

**What to do with it.** Fedena is usable under Apache-2.0. Vendor
`mazhar266/fedena@master`, record the commit SHA, and **keep copies of both
`LICENSE.md` and `NOTICE`** as read — the NOTICE is the part that makes the
provenance argument, and Apache-2.0 obliges you to carry it anyway. For a
*greenfield* engagement still prefer
[OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0, 73+
modules): not because Fedena's licence is weak, but because an actively
maintained platform with a live upstream beats a 2011-era Rails codebase whose
grant survives only in a mirror. Choose Fedena when a client is already on it.

### Two method notes, and the first one is a correction to this pass

**1. A one-filename probe produces a false negative.** This pass initially read
`master/LICENSE` for the mirror, got **404**, and briefly concluded the grant had
gone. It had not — it is at **`LICENSE.md`**. The KB's standing discipline is a
filename *sweep* (this pass used 6–9 names across 2–8 branches) and the moment it
was shortcut to a single `curl`, it produced exactly the kind of confident
denial the third pass's `OpenTutor` correction warned about. **A 404 on one
filename is evidence about that filename.** Recorded here rather than quietly
fixed, because the near-miss is the useful part.

**2. Enumerate owners in both directions.** The third pass learned that a 404 on
one owner is not evidence about a project — a wrong withdrawal destroyed a true
finding. Fedena shows the same enumeration cutting the other way: **the "official"
org and the original vendor both carry no grant, and the mirror carries the
vendor's own.** Both errors come from treating `owner/name` as the project.
Enumerate the owners, read the NOTICE, then decide.

## The OER content layer — one row, and the licence is correct for the artefact

Net new to this KB in the seventh pass.

| Asset | Licence (payload) | ★ | Use |
|---|---|---|---|
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | **CC BY 4.0** (`main/LICENSE`, "Attribution 4.0 International") | ~392k | A curated index of free programming books and courses across many languages. **Content for enablement (P6), cited — never a dependency** |

**Why it is shelved here rather than rejected.** CC BY 4.0 is attribution-only:
no non-commercial clause, no share-alike. The *material* is therefore usable in a
commercial curriculum provided attribution travels with it. It is not a software
licence — and there is no software here to license, only a reading list.

**The contrast worth keeping.** This KB's fifth pass found that pedagogy
evaluation is *"published as research and licensed as content"* and treated that
as a defect — correctly, because a benchmark harness under CC BY-SA is code you
cannot vendor. Here the content licence is **right**, because the artefact really
is content. **Judge the licence against the artefact, not against a preference
ordering of licences.** A reading list under CC BY is well licensed; an
evaluation harness under CC BY is mis-licensed. Same licence, opposite verdict.

## Added in the ninth pass of 2026-10-06 — RACHEL closed, and a ministry's estate as the public-sector reference

### RACHEL, resolved: the answer is NonCommercial

The eighth pass left RACHEL as *"path unresolved, no licence claim made."*
Starting from the project rather than a guessed path, the org is
**`rachelproject`** and the verdict is settled:

| System | Repo | Payload probe | Stated grant | Verdict |
|---|---|---|---|---|
| **RACHEL** (the CMS) | [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **none** — `LICENSE{,.md,.txt}`, `LICENCE{,.md,.txt}`, `COPYING`, `COPYRIGHT` × `main`/`master` | README: *"Creative Commons - BY, SA, NC"* | ❌ **NonCommercial on the software — not shippable** |
| RACHEL module template | [rachelproject/module-template](https://github.com/rachelproject/module-template) | **none** — same sweep | none found | ❌ no grant |

`contentshell` is RACHEL itself: *"The RACHEL Content Management System"*, the PHP
that serves and manages content on RACHEL devices (as of 2024, chiefly RACHEL 5).
Its only grant statement is a **content licence applied to software, carrying
NonCommercial**, with no payload to weigh against it.

**Why this is a platform finding and not just a licence note.** RACHEL's README
names its own dependency set: ZIM modules need **Kiwix**, and other modules need
**KA-Lite**, **Kolibri** or **Moodle**. So RACHEL is a *shell* over software this
page already shelves — and the shell is the one layer you cannot ship. Underneath
it, payload-verified this pass: `kiwix/kiwix-tools`, `kiwix/libkiwix` and
`kiwix/kiwix-android` are **GPL-3.0**, `openzim/libzim` is **GPL-2.0**, and
`learningequality/kolibri` is **MIT**.

**The selection rule the eighth pass wrote is unchanged, and now it has a
reason.** Kolibri was recommended on an absence of evidence about RACHEL; it is
now recommended on evidence. **Ship Kolibri. Cite RACHEL as prior art for
offline delivery in the proposal, and never as a component.** If offline
Wikipedia-class content is in scope, run **Kiwix as a separate process behind an
HTTP boundary** — the same side-car reasoning this page applies to MCP — so the
GPL obligation stays with Kiwix and off the client's codebase.

### The public-sector reference estate — UK Department for Education, MIT

New tier on this page. `DFE-Digital` is the UK Department for Education's
engineering org, and it operates **live national education services** in the open
under MIT (licences read from payload; full table and star counts in
`repos/foundations.md`):

| Service | Repo | Licence | What it is |
|---|---|---|---|
| Apply for teacher training | [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** | The national ITT application service |
| Teaching Vacancies | [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | National teaching job-listing service |
| Publish teacher training | [DFE-Digital/publish-teacher-training](https://github.com/DFE-Digital/publish-teacher-training) | **MIT** | Provider course publishing + candidate discovery |
| Register trainee teachers | [DFE-Digital/register-trainee-teachers](https://github.com/DFE-Digital/register-trainee-teachers) | **MIT** | Trainee registration for ITT placements |
| GIAS | [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** | The authoritative national schools register |
| Benchmarking & insights | [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** | School-to-peer-group metric comparison |

**Where this sits in the platform menu.** It is **not an LMS and not an SIS** —
it is the **administrative and workflow tier** of a national education system:
recruitment, registration, course publication, school registry, benchmarking.
Nothing here replaces Moodle, Kolibri, OpenEduCat or Kuali. What it provides is a
**reference estate**: a working, readable, permissively licensed implementation
of education workflow at country scale, maintained by a state.

**Three concrete uses in an engagement:**

1. **Public-sector proposals in EMEA.** The ministry question is always *"can we
   own, audit and exit this?"*. An MIT licence from a peer ministry is the
   strongest available answer, and it is a precedent rather than an argument.
2. **Domain models you will meet anyway.** GIAS and the ITT services encode the
   UK schools and teacher-training data model. Any UK engagement integrates with
   these; here they are, readable and reusable.
3. **The grounding layer for a reporting agent.**
   `education-benchmarking-and-insights` already does peer-group comparison —
   the data tier under any "how is my school performing" question, which is the
   natural thing to put an agent in front of.

**The asymmetry to lead with.** The DfE's administrative tier is production-grade
and MIT; its **AI** tier is five prototypes at **0–1★ with no licence payload**
(`rsd-ai-libs`, `sts-ai-support`, `ai-briefing-tool-prototype`,
`rsd-common-ai-services` — see `repos/foundations.md` for the rejections). One of
them, `rsd-ai-libs`, describes *"building and evaluating Azure AI Foundry agents
with guardrails, Azure AI Search, and **MCP server support**"* — a ministry
independently arriving at this KB's MCP side-car pattern, and leaving it
unlicensed at zero stars.

So the public-sector pitch is not *"you need a platform."* They built one. It is:
**"your administrative layer is a licensed national asset and your AI layer is
unlicensed prototypes — let us build the second on top of the first, under a
licence you already use."**

**Star-count warning specific to this tier.** These repositories sit at **5–38★**
because government services are *consumed*, not forked. On this page that is the
one place where low stars do **not** indicate low maturity — the opposite of the
reading this KB applies everywhere else, and the opposite of the trap in
`agents/top.md` where a 72★ repository turned out to be the ungranted one.

## Added in the tenth pass of 2026-10-06 — the integration tier is a scored line item, not plumbing

Every section above this one picks a **platform**. This one is about the layer
between the platform and whatever Globant builds on top of it, and it is here
because of a procurement number rather than a technology trend.

**CoSN: 39% of districts score interoperability in their RFP rubrics** (Tier 2,
corroborated, recorded in the ninth pass). A third of the North American K-12
buying market **assigns points** to how well a system exchanges roster and
activity data. That moves the integration layer out of the implementation plan and
into the bid.

### The standards, and which ones actually have permissive implementations

| Standard | What it carries | Permissive implementation shelf (payload-verified, tenth pass) |
|---|---|---|
| **LTI 1.3** (1EdTech) | Launching an external tool from inside an LMS, with identity and context | **Four**, across four runtimes — see below |
| **OneRoster 1.1 / 1.2** (1EdTech) | Rosters: orgs, schools, students, teachers, terms, enrolments | **One** (.NET), **rostering only** |
| **Caliper Analytics** (1EdTech) | Learning activity event streams | **None found on a permissive licence this pass** — and the search term is a homonym trap |
| **QTI** (1EdTech) | Assessment item and test interchange | Not swept this pass |

The runtime split for LTI 1.3 and OneRoster, with licences read from payload:

| Runtime | Repo | License |
|---|---|---|
| Node / TypeScript | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (373★) | Apache-2.0 |
| PHP (Moodle-side) | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) 🔵 *(re-picked pass 24; was `1EdTech/…`, the 2,317-day-cold copy of the same library — this one is 14 d)* | Apache-2.0 |
| Java / Spring Boot | [Unicon/tool13demo](https://github.com/Unicon/tool13demo) (27★) | Apache-2.0 |
| Java / Spring Security | [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) (25★) | Apache-2.0 |
| .NET | [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) (6★) | MIT |
| **Python** | **none found** | — |

### What this adds to platform selection

1. **The LMS choice now implies the integration runtime.** Moodle pulls toward the
   1EdTech PHP library; a Spring estate pulls toward `oxctl` or `Unicon`; a Node
   AI service pulls toward `ltijs`. That is a decision to make in week one
   alongside the platform, not after it.
2. 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07.** Python is where the AI layer lives, and
   **there is a Python LTI 1.3 library**: [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti),
   **MIT**, head commit **2026-10-05 (2 d)**, PyPI [`django-lti`](https://pypi.org/project/django-lti/)
   **v0.10.1 (61 d)**. **If the AI tier is Django, the two-runtime shape below is unnecessary** —
   launch in-process and skip the adapter. The adapter shape is still correct when the AI tier is
   **not** Django and not JupyterHub, because the only framework-neutral Python implementation
   (`pylti1.3`) is **1,416 days cold**. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`. ⚠️ **So budget the adapter only after checking the AI
   tier's framework** — it is a conditional line item now, not a certainty.
3. **OneRoster.NET does rostering only — the gradebook is not implemented.** If
   the rubric scores grade passback, this shelf does not cover it and the honest
   answer is a custom build against the spec.
4. **Caliper has no permissive implementation on this shelf, and the word is a
   trap.** `OneRoster OR Caliper OR "LTI 1.3" license:apache-2.0` returns **184
   repositories** dominated by `google/caliper` (deprecated Java
   micro-benchmarking, 818★) and `hyperledger-caliper/caliper` (blockchain
   benchmarking, 708★). If an RFP scores learning-analytics event streams, treat
   it as a build, not a selection.
5. **Pin `theopenem/OneRoster.NET`, not the identical copy.**
   [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) is also MIT and
   byte-identical (same `README.md` md5, same licence text, **same `theopenem`
   copyright holder**). One asset, two addresses.

### The offline-first stack gains its missing layer

The eighth pass made **Kolibri** the platform answer for offline-first delivery.
What it did not record is the component that makes the synchronisation work:
[learningequality/morango](https://github.com/learningequality/morango) — **MIT**,
15★, a pure-Python **peer-to-peer database replication engine for Django** with
**certificate-based authentication**, change tracking and data partitioning built
for low-bandwidth links, on SQLite or PostgreSQL.

This matters for platform selection because it is **separable**. A client who
needs offline-tolerant sync for an existing Django system does not have to adopt
Kolibri to get it — morango is usable on its own, under MIT. That is a smaller,
faster engagement than a platform migration, and it is now on the shelf.

**One warning inside the same organisation:**
[kolibri-design-system](https://github.com/learningequality/kolibri-design-system)
and [kolibri-server](https://github.com/learningequality/kolibri-server) returned
**no licence payload** under any of 20 probed URLs. Kolibri itself, `morango`,
`le-utils`, `studio` and `ricecooker` are MIT, read from payload. **The
organisation's posture does not license its repositories** — probe each one.

## Added in the eleventh pass of 2026-10-06 — nine platforms recovered from this repository's own archive, re-verified on their real default branch

All nine addresses below sit in `archive/2026-10-06-pre-reset/` and were dropped by
this repository's reset earlier on 2026-10-06 (172 real addresses lost; the audit is
in `repos/trending.md`). Each licence was re-read this pass from the repository's
payload, **on the branch the GitHub API reports as `default_branch`** — not a guessed
`main`/`master` pair, which is what made two of these look ungranted.

### The permissive end — what Globant can customise and redistribute

| Platform | Repo | Licence (read from payload) | ★ / forks | What it is, and what AI goes on top |
|---|---|---|---|---|
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (`master`) | ✅ **Apache-2.0** | 446 / 166 | Full Swiss LMS: course authoring, **assessment**, curriculum management, QTI, SCORM, lecture and roll-call. Java. Pushed 2026-10-06. **The most permissively licensed complete LMS in this KB** — Moodle is GPL-3.0 and Open edX is AGPL-3.0, so OpenOLAT is the only one you can extend without the copyleft conversation. AI layer: QTI item generation, assessment scoring, curriculum-gap analysis. |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) (`master`) | ✅ **MIT** | 316 / 95 | Django CMS purpose-built for **education portals** — course catalogue, programmes, organisations, teacher pages — designed to sit *in front of* Open edX or Moodle rather than replace them. From **France Université Numérique**. AI layer: catalogue search, programme recommendation, multilingual course descriptions. **MIT at the portal tier is the cleanest place to put client-visible AI**, because the copyleft lives behind it in the LMS. |
| **Sunbird** | [project-sunbird/sunbird-lms-mw](https://github.com/project-sunbird/sunbird-lms-mw) · [sunbird-analytics](https://github.com/project-sunbird/sunbird-analytics) (`master`) | ✅ **MIT** | 6 / **41** · 3 / 28 | The stack under **India's DIKSHA** national platform: LMS middleware plus a learning-analytics framework. **The most permissive national-tier education stack this KB has recorded.** ⚠️ **Dormant** — middleware last touched 2024-08-30, analytics 2023-02-08, and `sunbird-learning-platform-devops` is **archived**. Forks (41) exceeding stars (6) is the signature of infrastructure that is *deployed* rather than starred. **Use as a licence-clean reference architecture; do not expect upstream patches.** |
| **Ed-Fi ODS/API** | [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) (`main`) | ✅ **Apache-2.0** (`LICENSE.txt`) | 28 / 47 | Reference implementation of the **Ed-Fi** US K-12 data standard: an operational data store plus a REST API over a shared student-data model. C#. **The data tier a North American district RFP assumes you already speak** — see trend 26 and P24. AI layer: early-warning models, intervention targeting, anything that needs cross-system student records without a bespoke integration per source. |
| **OpenTutor** | [LEARNableLabs/opentutor](https://github.com/LEARNableLabs/opentutor) (`main`) | ✅ **MIT** | 0 / 0 | *"Compounding Deliberate Curiosity."* JavaScript, 72 open issues, created 2026-02-28, pushed 2026-10-02. **Measured at 0★.** Noted precisely because earlier KB cycles recorded an "OpenTutor" at ~900★ — **a different project of the same name.** Treated here as an early-stage MIT asset, not as an established platform. |

### The copyleft end — real platforms, and the clause decides the engagement

| Platform | Repo | Licence (read from payload) | ★ / forks | The delivery constraint, stated plainly |
|---|---|---|---|---|
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) (**`dev`**) | 🔴 **AGPL-3.0** | **2,320** / 564 | *"The next-gen open source learning platform for everyone."* Python + React, headless, explicitly AI-native. Pushed 2026-10-06 — the most actively developed AGPL platform here. ⚠️ **Network clause**: hosting a modified LearnHouse for a client triggers the obligation to offer the modified source **to its users**. Viable where the client accepts an open deliverable; fatal where they expect proprietary differentiation. ⚠️ Default branch is **`dev`**. |
| **CourseLit** | [codelitdev/courselit](https://github.com/codelitdev/courselit) (`main`) | 🔴 **AGPL-3.0** (`LICENSE.md`) | **1,269** / 260 | Course sales, digital downloads and blogging on a branded site — the open alternative to Teachable/Thinkific/Podia. TypeScript. Same network clause as above. **The right base for a client whose product *is* the open platform**, wrong for one reselling it. |
| **i-educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) (**`2.12`**) | 🔴 **GPL-2.0** (*"Version 2, June 1991"*) | **718** / **547** | *"O maior software livre de educação do Brasil."* A full school-management/SIS platform — enrolment, attendance, grades — Laravel/PHP, tagged `software-publico`. **The only genuine LATAM-origin education platform in this KB**, and with 547 forks it is the most-forked platform on these shelves. GPL-2.0 is **no network clause**: hosting a modified i-educar for a Brazilian municipality triggers nothing; **distributing** a modified binary or source does. For public-sector LATAM work, where the client often *wants* the source, this is close to ideal. ⚠️ Default branch is the version number **`2.12`**; `main` serves nothing, which is why a `main`+`master` probe reports this platform as ungranted. |
| **Obojobo** | [ucfopen/Obojobo](https://github.com/ucfopen/Obojobo) (`master`) | 🔴 **AGPL-3.0** | 72 / 35 | Next-generation course content delivered into an LMS over LTI. React + SlateJS. From the **University of Central Florida**. |
| **Materia** | [ucfopen/Materia](https://github.com/ucfopen/Materia) (`master`) | 🔴 **AGPL-3.0** | 52 / 41 | Embeddable learning widgets and educational games for LMS courses, also LTI-delivered. Same organisation; note that UCF's own LTI **template** (`cookiecutter-python-lti`) is **MIT** while its *applications* are AGPL-3.0. **An organisation's licence posture is not uniform across its repositories** — probe each one. |
| **OpenEMIS** | [OpenEMIS/core](https://github.com/OpenEMIS/core) (`main`) | 🔴 **GPL** — **version not read this pass** | — | Education management information system deployed at ministry tier. Recorded with the licence version explicitly open rather than guessed; resolve before it enters a proposal. |

### What this table changes about platform selection

The KB's standing advice has been Moodle (GPL-3.0) or Open edX (AGPL-3.0) with AI on
top. Two corrections:

1. **If copyleft is the blocker, the answer is OpenOLAT, not a negotiation.**
   Apache-2.0, 446★, full assessment and curriculum management, pushed the day of
   this pass. It has been absent from this KB's live files since the reset.
2. **If the engagement is LATAM public sector, i-educar's GPL-2.0 is a feature.**
   No network clause, 547 forks, Brazilian, already classified as `software-publico`.
   The licence that blocks a SaaS product is the licence a municipality asks for.

And one procurement note that spans both tables: **the portal tier is where
permissive licences survive.** Richie (MIT) in front, a copyleft LMS behind, and the
AI in the MIT layer — that is the pattern that lets a client keep what they paid for
without anyone misreading a clause.

## Added in the twelfth pass of 2026-10-06 — nine more platforms off the archive, on their real default branch

Branches from `git ls-remote --symref … HEAD`; licences from the
`raw.githubusercontent.com` payload on that branch, 2026-10-06.

### The permissive end — customise and redistribute

| Platform | Repo | Licence (payload) | ★ | Branch | What it is, and where it fits |
|---|---|---|---|---|---|
| **Pupilfirst** | [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | **MIT** (`master/LICENSE`) | **978** (280 forks) | `master` | 🆕 **A full LMS under MIT, at nearly 1,000★ — the largest permissive end-to-end platform this KB has recorded after Kolibri.** Built to run an **asynchronous online school**: learning through focused tasks, directed feedback, an iterative submit-review-resubmit workflow, and community interaction. Ruby on Rails. **Why it matters for engagements:** the other permissive platforms here are offline-first (Kolibri) or lesson-authoring (Oppia). Pupilfirst is the first permissive platform whose core model is **coached, reviewed project work** — which is the shape of corporate L&D, bootcamps and competency programmes, i.e. the shape of most of Globant's own education-adjacent demand. |
| **Sunbird (mobile + components)** | [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | **MIT** (`main/LICENSE`) | 10 (**92 forks**) | `main` | **APAC / India.** The Cordova mobile client for the Sunbird stack, handling **both offline and online** consumption. TypeScript, **12,921 commits**. ⚠️ **Read the ratio, not the stars: 10★ against 92 forks.** This is a deployment artefact, not a GitHub-popularity artefact — forks are what national and state implementers create. Sunbird is already on this KB's shortlist as the nine-figure-scale platform; **this is the client address**, which the reset had dropped. |
| **Sunbird consumption components** | [Sunbird-Ed/SunbirdEd-consumption-ngcomponents](https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents) | **MIT** (`master/LICENSE`) | not read this pass | `master` | Angular content-consumption components — the reusable player/renderer layer of the Sunbird client. |
| **Sunbird telemetry SDK** | [project-sunbird/sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | **MIT** (`master/LICENSE`) | not read this pass | `master` | The telemetry SDK. Pairs with the xAPI chain in `repos/foundations.md`: Sunbird's own event model, MIT, at national scale. |
| **LibreTexts Conductor** | [LibreTexts/conductor](https://github.com/LibreTexts/conductor) | **MIT** (`master/LICENSE.md`) | 4 (3 forks) | `master` | **North America.** The platform behind LibreTexts' **Commons** catalogue, Campus Commons multi-tenancy, library integration, Meilisearch search, adoption reporting, and an **AI knowledge-base feature built on LangChain with vector embeddings**. TypeScript/React/Express/MongoDB. **Multi-tenant from a single codebase** — one deployment serving many institutions by configuration, which is exactly the shape a consortium or ministry engagement needs. |
| **LibreTexts LibreOne** | [LibreTexts/LibreOne](https://github.com/LibreTexts/LibreOne) | **MIT** (`main/LICENSE.md`) | not read this pass | `main` | The identity and account layer for the LibreTexts estate. The piece you need if Conductor is going to serve more than one institution. |
| **Edrys** | [edrys-org/edrys](https://github.com/edrys-org/edrys) | **MPL-2.0** (`main/LICENSE`, 16,725 B) | not read this pass | `main` | **Live-classroom platform** (remote labs, shared classroom modules). 🔴 **Corrected this pass: this is MPL-2.0, not the "abbreviated AGPL" an earlier pass recorded** — see `repos/foundations.md`. MPL-2.0 is **file-level** weak copyleft, so Edrys **can** sit inside a mixed-licence deliverable provided modified Edrys files stay MPL and are published. It was priced as unusable; it is usable with per-file discipline. |

### The copyleft and non-OSI end — real platforms, and the clause is the engagement

| Platform | Repo | Licence (payload) | Branch | What the clause does to the deal |
|---|---|---|---|---|
| **OpenEMIS Core** | [OpenEMIS/core](https://github.com/OpenEMIS/core) | **GPL-2.0** (`master/LICENSE`) | `master` | **Education Management Information System** — the ministry-level estate layer (schools, students, staff, institutions), the system UNICEF-supported deployments use. GPL-2.0: a modified OpenEMIS must be published under GPL-2.0, which for a **public-sector ministry client is usually a feature, not a cost** — the same argument pattern 28 makes for `i-educar` in Brazil. Price it as a public-good deliverable, not as lost IP. |
| **Edlib** | [cerpus/Edlib](https://github.com/cerpus/Edlib) | **GPL-3.0** (`master/LICENSE`) | `master` | **EMEA / Norway** (Cerpus). Content-authoring and sharing platform, the H5P-adjacent layer for interactive learning content. GPL-3.0 — a fork is a published fork. |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | **GPL-3.0** (`main/LICENSE`) | `main` | **North America** — University of Central Florida's **accessibility scanner for Canvas** courses: finds and helps fix WCAG issues in course content. GPL-3.0. Accessibility is a procurement requirement in US public education, and this is the installed-base tool. Pair it with the WCAG scanner already in `canvas-mcp` (MIT) when the deliverable must be permissive. |
| **OpenStax CMS** | [openstax/openstax-cms](https://github.com/openstax/openstax-cms) | **AGPL-3.0** (`main/LICENSE`) | `main` | The CMS behind OpenStax's open-textbook estate. AGPL-3.0 — **network-use copyleft**, so a hosted deployment triggers the source obligation. Content is separate: [openstax/osbooks-biology-bundle](https://github.com/openstax/osbooks-biology-bundle) is **Creative Commons**, which is correct for a textbook and useless as a code licence. Take the content, not the CMS. |
| **Nextcloud AI apps** | [nextcloud/assistant](https://github.com/nextcloud/assistant) · [nextcloud/context_chat](https://github.com/nextcloud/context_chat) | **AGPL-3.0** (`main/COPYING`) | `main` | **EMEA / Germany.** On-premises assistant and RAG-over-your-documents for a Nextcloud estate — the self-hosted European answer to a cloud AI assistant, and relevant wherever data residency binds. AGPL-3.0, and the licence sits in **`COPYING`**, not `LICENSE`. For a school or university already running Nextcloud this is a **deployment and integration** engagement, which AGPL does not obstruct; it obstructs shipping a proprietary derivative. |
| **Advising App** | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** (`main/LICENSE`) | `main` | **Not open source.** Student-advising CRM for higher education. Elastic 2.0 **prohibits providing it as a managed service** and prohibits circumventing its licence keys. It looks open on GitHub and is not. Already recorded in pass 123; confirmed here from the payload. **Do not put it in a proposal as open source.** |
| **Leemons** | [leemonade/leemons](https://github.com/leemonade/leemons) | 🔴 **Composite / "Fair code"** (`main/LICENSE.md`) | `main` | **EMEA / Spain.** The payload opens *"Portions of this software are licensed as follows"* — an **open-core split by directory**, not one grant. Already recorded in pass 123. **Per-directory review before any reuse**; there is no single answer to "what licence is Leemons". |

### The Moodle AI plugin cluster, measured — 11 of ~16

Moodle's core is GPL-3.0 and an in-tree plugin inherits it. That is expected and is not
a finding. **What the sweep found is that the cluster is not uniformly licensed:**

| Licence state | Count | Repos |
|---|---|---|
| **GPL-3.0** (correct for in-tree) | 8 | [microsoft/o365-moodle](https://github.com/microsoft/o365-moodle) · [surlabs/AIChatForMoodle](https://github.com/surlabs/AIChatForMoodle) · [saylordotorg/moodle-local_ai_course_assistant](https://github.com/saylordotorg/moodle-local_ai_course_assistant) · [michael-milette/moodle-local_aiid](https://github.com/michael-milette/moodle-local_aiid) · [Universita-di-Ferrara/moodle-aiprovider_gemini](https://github.com/Universita-di-Ferrara/moodle-aiprovider_gemini) · [caiocarvalhofre/moodle-mod_maici](https://github.com/caiocarvalhofre/moodle-mod_maici) (**LATAM / Brazil**) · [moodlehq/moodle-tool_dataprivacy](https://github.com/moodlehq/moodle-tool_dataprivacy) (branch **`MOODLE_34_STABLE`**) · [Citolab/qti-convert](https://github.com/Citolab/qti-convert) |
| 🔴 **Ungranted** | 3 | `marcusgreen/moodle-tool_aiconnect` · `jeanlucio/moodle-local_aihub` · `alvarogregori/moodle-ai-graded-assignment` |

⚠️ **`moodle-ai-graded-assignment` is the one to notice.** AI-graded assignments is the
function trend 7 has flagged as the regulated frontier and the tooling gap since the
seventh pass. A plugin for it exists in the Moodle ecosystem and **carries no licence**.
It cannot be adopted, and that is a supply fact rather than a search failure — it was
probed on its real default branch against 30+ filename variants.

🆕 **And the licence-hygiene asymmetry is now visible as a pattern.** Across this pass's
66 archive addresses, **11 were ungranted** — and the ungranted set is concentrated in
exactly two places: **individual-maintainer LMS plugins** and **public-sector metadata
and vocabulary repositories** (FWU Germany, DG EMPL, DINI-AG-KIM, IMDA's evals
catalogue). The organisations whose output is *most* reusable in principle — ministries
and standards groups publishing vocabularies — are the ones least likely to attach a
grant. **For an EMEA public-sector engagement, "can we have a licence on this?" is a
cheap, early, high-leverage ask**, and one a client ministry can usually satisfy with a
single commit.

### The platform-selection table, updated

| If the client needs… | Take | Licence | Why |
|---|---|---|---|
| Coached, reviewed **project-based** learning at scale | **Pupilfirst** | **MIT** | Only permissive platform built around submit → review → resubmit. 978★. |
| **Offline-first** / low-connectivity delivery | **Kolibri** | MIT | Unchanged; still the equity-deployment base. |
| **National / state** scale with an existing implementer community | **Sunbird** | MIT | 92 forks on the mobile client; India-proven. |
| **Multi-tenant OER** for a consortium or ministry | **LibreTexts Conductor** + **LibreOne** | MIT | One codebase, many institutions, AI KB already wired. |
| **Live/remote-lab classrooms** | **Edrys** | MPL-2.0 | File-level copyleft only — mixed deliverable is fine. |
| **Ministry-level EMIS** | **OpenEMIS Core** | GPL-2.0 | Publishing the fork is acceptable, often preferable, for a public client. |
| **Interactive content authoring** | **Edlib** / H5P | GPL-3.0 | Fork is published. |
| A **student-advising CRM** | ⚠️ **not `advisingapp`** | Elastic 2.0 | Source-available, no managed service. Build on a permissive base instead. |

## Added in the thirteenth pass of 2026-10-06 — the fifth fully permissive platform, and the first AI-native one that is also sovereign-ready

| Platform | Repo | Licence (read from payload) | Position |
|---|---|---|---|
| **Open TutorAI (CE)** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** (`LICENSE`, 1,531 B — body text, **no title line**) | **Promoted onto this shelf this pass.** Personalised tutoring platform: multi-model conversation, **local RAG**, **voice / video / 3D-avatar modes**, per-learner assistant configured through structured onboarding, and **role-based access control**. Serves **Ollama** local models as well as OpenAI / Groq / Mistral. Python, 380 commits, **108★ / 192 forks**. From the **IRF-SIC Laboratory, Ibn Zohr University, Agadir, Morocco**, with Morocco's Ministry of Higher Education, the **Digital Development Agency** and the **CNRST** as funders. **Open core** — a paid Enterprise Edition adds theming, SLA and LTS. |

### Why this changes the shelf, and what it does not change

The permissive end of this shelf has been **four platforms** — Kolibri (MIT),
Oppia (Apache-2.0), Mentingo (MIT), Coursemology (MIT), plus Sunbird (MIT) at national
scale. Every one of them is a **platform that AI can be added to**. Mentingo was recorded
as *"the only AI-native one"*, and on a corporate-L&D footing that remains true.

Open TutorAI is the **fifth**, and it is a different proposition from all of them:

- 🟢 **AI-native and academic**, not AI-added and corporate. The tutoring loop,
  the retrieval layer and the avatar presentation are the product, not a plugin.
- 🟢 **Sovereign by construction.** It ships **local RAG** and serves **Ollama** in the
  same configuration surface as the hosted APIs. Every other AI-native option on this
  shelf requires the sovereign path to be *built*; here it is a setting. That makes it the
  shortest route to the EMEA data-residency posture this KB has been assembling by hand
  since pattern **P4**.
- 🟢 **RBAC is already there**, which is the unglamorous blocker that stops a pilot
  becoming an institutional deployment.
- 🟢 **It is a state-funded public-sector reference.** A Moroccan ministry, the DDA and the
  CNRST stand behind it. For a public-sector buyer in EMEA or LATAM, a sovereign-stack
  tutoring platform that a government already funds is a materially stronger reference than
  a vendor pilot.

What it does **not** change:

- ⚠️ **It is open core.** The CE is the base for a commercial Enterprise Edition. The
  BSD-3-Clause grant on the CE is unqualified and **this is not a directory carve-out like
  Langfuse's `ee/`** — but the roadmap is set by a party with an incentive to keep features
  above the line. Check which side of that line a client's must-haves fall on **before**
  proposing it, and record the answer.
- 🔴 **The copyright holder in the payload is not identifiable.** The licence reads
  *"Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev"*, and **R2D-dev
  appears in no public artefact of the project** — not the README, not the documentation,
  not the search index. The grant is real; the entity holding it is opaque. On a
  redistribution engagement that is the party an indemnity question routes to, so **raise
  it upstream before it reaches a contract**.
- ⚠️ **It is published as Apache-2.0 in third-party catalogues and it is BSD-3-Clause.**
  Both are permissive and both are on this KB's allowlist, so nothing architectural turns
  on the error — but a diligence pack that cites a catalogue instead of the payload will
  state the wrong licence, and the attribution clauses differ.
- ⚠️ **192 forks against 108 stars.** The twelfth pass established the reading: in the
  education layer, forks exceeding stars means **deployed as a base**, not watched. That is
  a point in its favour, and it also means a meaningful share of real-world use is in forks
  whose divergence nobody is tracking. **Pin a commit.**

### The platform-selection table, updated

| If the engagement is… | Start from | Licence posture |
|---|---|---|
| **Academic tutoring, AI-native, data must stay in-region** | **Open TutorAI CE** | 🟢 BSD-3-Clause — build and redistribute; verify the open-core line |
| Corporate L&D / onboarding / compliance, AI-native | Mentingo | 🟢 MIT |
| CS and programming teaching, higher ed | Coursemology | 🟢 MIT |
| Low connectivity, equity-driven, offline | Kolibri | 🟢 MIT |
| Interactive lessons with misconception handling | Oppia | 🟢 Apache-2.0 |
| National / nine-figure learner scale | Sunbird | 🟢 MIT (100+ services is the cost) |
| The incumbent is already there | Moodle / Canvas / Open edX | 🔴 Copyleft — **side-car via LTI or MCP**, never a fork |

## Added in the fourteenth pass of 2026-10-06 — the proprietary platforms a client already runs, and what their integration tier now costs

Every platform on this page up to here is one Globant can **deploy**: permissive ones to
customise and redistribute, copyleft ones whose clause decides the engagement. That framing
has a hole in it, and it is the most common engagement in higher education: **the client
already runs a proprietary LMS and is not replacing it.** Canvas, Brightspace, Blackboard
and Google Classroom are not on this shelf as platforms because they cannot be — and the
question a studio is actually asked is not *"what should we deploy"* but *"what can you build
against what we have."*

This pass measured that answer, platform by platform. The licence that matters is no longer
the platform's; it is **the licence of the integration tier**, and that tier is now large
enough to inventory.

### The integration tier, by platform

Measured with GitHub REST `total_count`, one platform name per query, 2026-10-06. Licences
read from each repository's own payload. Full rows in `agents/top.md` (fourteenth pass).

| Platform the client runs | Integration repos | Best permissive, payload-backed server | Verdict for a Globant engagement |
|---|---|---|---|
| **Canvas LMS** (Instructure) | **117** | `vishalsachdev/canvas-mcp`, **MIT**, 278★, up to 103 tools | 🟢 **Adopt.** Deepest tier in education. Pin the canonical repo against its forks. |
| **Moodle** (GPL-3.0 platform) | **86** | `peancor/moodle-mcp-server`, **MIT** — plus `1alexandrer/moodle-mcp`, MIT, 18★ 🆕 | 🟢 **Adopt, from outside the tree.** The MCP side-car is MIT precisely because it is not an in-tree plugin — the licence-boundary note in `agents/top.md` is the whole architecture. |
| 🆕 **Brightspace / D2L** | **23** | `RohanMuppa/brightspace-mcp-server`, **MIT**, 57★, on npm | 🟢 **Adopt.** New to this KB. A real tier: a feature-complete server on npm, an engineering-grade alternative with opt-in writes (`JhostinAleck/brightspace-mcp`, MIT) and an **Apache-2.0** option (`pranav-vijayananth/...`) where a client's policy wants the explicit patent grant. |
| 🆕 **Blackboard Learn / Ultra** | **5** | `nitsuah/bb-mcp`, **MIT**, 2★, **RBAC middleware** | ⚠️ **Thin — build on the best of five.** Large university install base, five repositories. `bb-mcp` is the one to start from: it is the only asset in the whole 98-address cluster that puts **role-based access control** in the MCP layer, which is the control an education deployment is audited on. |
| 🆕 **Google Classroom** | **17** | `faizan45640/google-classroom-mcp-server`, **MIT**, **6★** | 🔴 **Build.** The widest K-12 reach of any platform here and its best dedicated server has six stars. `Kimmahone/edu-workspace-mcp` (MIT) is the more useful starting point because it covers **Google Forms**, and Forms is where K-12 assessment actually lives. |
| **Open edX** (AGPL-3.0 platform) | **1** | — (`blend-ed/tutor-contrib-openedxmcp`, **AGPL-3.0**) | ⚠️ **Copyleft all the way down.** The one integration asset inherits the platform's AGPL. Already recorded; unchanged this pass. |
| 🔴 **PowerSchool** (dominant US K-12 SIS) | **0** | **none** | 🔴 **Empty tier.** `total_count: 0`. There is nothing to adopt, nothing to fork and nothing to compete with. |

### What this table changes about platform selection

🔵 **Integration depth is inversely related to engagement opportunity.** Canvas and Moodle
hold **203 of the 249** repositories measured. Everything a client is likely to ask for
against those two already exists under MIT, so the studio's value there is configuration,
governance and pedagogy — **not** the connector.

The money is in the thin and empty tiers, and they are the **K-12 administrative** ones:

- **Google Classroom and PowerSchool together cover most of US K-12**, and their open-source
  integration tier is 17 repositories and 0 repositories respectively.
- That tier's data is **student records, guardians, enrolment and accommodations** — i.e. the
  regulated surface. The reason it is empty is not that nobody wants it; it is that a
  hobbyist cannot get credentials to a district SIS. **An enterprise integrator can**, and
  that is the asymmetry.
- Price it as a build, not an adoption, and put the governance artefacts in the statement of
  work from day one (see P24 and P25 in `compose/patterns.md`).

### 🆕 The ministry tier — a national curriculum as a callable platform

New on this page and new to this KB: the platform is not an LMS but a **state education
authority's own API estate**, and in two Nordic countries it is already wrapped as an MCP
server.

| Authority | Wrapper | Licence (payload) | What it exposes |
|---|---|---|---|
| **Skolverket** — Swedish National Agency for Education (**EMEA**) | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP), 12★ | 🟢 **MIT** (`LICENSE`, 1,093 B) | *All* of Skolverket's open APIs: the **Läroplan / syllabus API**, the **Skolenhetsregistret** school-unit register, and the Planned Educations API. Published in the official MCP Registry. |
| **Udir** — Norwegian Directorate for Education (**EMEA**) | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** — 0 of 20 filenames, no manifest field | School (NSR) and kindergarten (NBR) registry data. |
| **Smartschool** — dominant LMS in Flemish education (**EMEA**, Belgium) | [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP), 5★ | 🟢 **MIT** (`LICENSE`, 1,069 B) | Platform integration with real release engineering: PyPI package, CI, codecov. |

⚠️ **Read the Skolverket copyright line before this goes in a proposal.** It says
**"Skolverket Syllabus MCP Contributors"**, not Skolverket. The MIT grant covers **the
wrapper**; the **agency's own terms govern the data** the wrapper returns. Two consequences
for an EMEA engagement: the code is safe to fork and ship, and the data terms are a separate
diligence item that the MIT licence does not answer.

🔵 **This is the reusable shape, and it generalises past Sweden.** A national curriculum
published as an open API, wrapped thinly under a permissive licence, turns
*"align this to the national curriculum"* from a consulting deliverable into a **tool call**.
It is the missing input to P15 (curriculum-aligned item generation) and the cleanest
instance yet of trend 13: the mandate specifies the architecture. **Udir is the counter-case
in the same region** — same idea, same quality of public data, no grant — so the pattern is
"check for a wrapper, expect to write one," not "a wrapper exists."

### The university tier, and the two APAC assets that prove it is a channel

The same shape one level down: a single institution's portal, wrapped permissively.

| Institution | Wrapper | Licence | Note |
|---|---|---|---|
| **Korea University** (KUPID portal), **APAC** | [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp), 13★ | 🟢 **MIT** | Notices, library seat availability, weekly assignments. On PyPI. Korean-language README — and the thirteenth pass's **Korean-language query did not find it**; the platform name did. |
| **National Taiwan University** (NTU COOL), **APAC** | [kc0506/ntucool](https://github.com/kc0506/ntucool), 10★ | 🟢 **MIT** | One `cool` binary = CLI + MCP server + SDK, **plus a Claude Code plugin** shipping skills and commands. ⚠️ Self-declared **unofficial**. |

⚠️ **"Unofficial" is a diligence item, not a disqualifier** — but it is the one that decides
whether a university client can deploy it. An unofficial wrapper of an institution's own
portal depends on undocumented endpoints and on credentials the institution controls; it can
be broken by the institution at any time, deliberately. Fork it for the shape, then get the
integration sanctioned.

### 🔴 And the competition is now hosted, closed, and in the same catalogue

The MCP Registry census this pass (`repos/trending.md`, fourteenth pass) found **102
education-vocabulary servers, 71 of them with no source repository at all**. One of those 71
is **`com.moodlemcp/moodle`** — *"Connect your Moodle to AI assistants: courses, content,
grading and more"* — a **closed, hosted Moodle MCP endpoint competing directly with the 86
open repositories in that tier.** Others: `io.cubite/lms` (hosted LMS with SCORM/xAPI) and
`com.skillsail/mcp` (SCORM authoring and export).

🔵 **The strategic read, and it belongs on this page rather than in trends.** For two years
the open-source platform shelf competed with proprietary *platforms*. It now also competes
with proprietary **connectors to open platforms** — someone selling a hosted MCP endpoint in
front of the client's own Moodle. That is a thin, high-margin layer, and it is exactly the
layer a Globant deliverable occupies.

**So the pitch changes.** Against a hosted connector, the differentiator is not features; it
is the three things a client cannot get from an endpoint they do not host: **the code**, **the
deployment inside their own boundary**, and **the audit trail**. Lead with those, and keep
`langfuse` (MIT outside `ee/`) in the stack so the third one is produced automatically.

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS platform tier, and why none of it is permissive

This KB's platform shelf has been built around the **learning** platform — Moodle, Open edX,
Canvas, Sunbird, Coursemology, Mentingo, Kolibri. The administrative platform — the student
information system — had only OpenEduCat (LGPL-3.0, on Odoo), i-Educar and the Fedena
question. This pass measured the tier properly, because the fifteenth pass's SIS integration
work made the platform question unavoidable: *if we must integrate with a proprietary SIS,
is there an open one to deploy instead?*

**There is. It is substantial. And not one of it is permissive.**

### The tier, licence read from the payload on 2026-10-06

| Platform | ★ / forks | Licence (payload) | Default branch | Country / scope |
|---|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **644** / 391 | ⚠️ **GPL-2.0** (15,214 B) | 🔴 `mobile` | Global, PHP — full SIS: gradebook, attendance, scheduling, billing |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | **634** / 417 | ⚠️ **GPL-3.0** (35,121 B) | 🔴 `v31.0.00` | Global, PHP — school management platform |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | **345** / 286 | ⚠️ **GPL-2.0** (17,286 B, at `docs/License.txt`) | `master` | Global, PHP — multi-institution SIS |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | *(already shelved)* | ⚠️ **GPL-2.0** (18,092 B) | 🔴 `2.12` | **LATAM** — Brazilian municipal SIS |
| [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | — | 🔴 **no payload found** | `master` | sibling repo of the above |

🔴 **Four platforms, 1,600+ stars and 1,000+ forks between them, and the licence set is
`{GPL-2.0, GPL-3.0}` with one ungranted sibling. Zero MIT. Zero Apache. Zero BSD.**

### 🟢 This is the finding that explains the whole pass

The fifteenth pass found **24 permissive assets** in the SIS space (`agents/top.md`) and
**zero permissive SIS platforms**. That is not a coincidence, and it is the most useful
structural fact in this file:

> **You cannot fork an open SIS permissively, so all the permissive work happens at the
> edges.** The MIT supply is in clients, wrappers, timetable decoders, MCP servers and
> browser extensions — everything that *talks to* a student information system without
> *being* one.

🔵 **Which means the architecture decision is forced, and it is the same in every region:**

| If the client wants | The answer is | Licence reality |
|---|---|---|
| To **replace** a proprietary SIS with open source | RosarioSIS, Gibbon or openSIS | ⚠️ **GPL — plan for it.** A Globant-delivered module that is a derivative work must be published under the same terms. The Odoo/OpenEduCat LGPL-3.0 route remains the only middle path on this page. |
| To **add AI to** the SIS the client already runs | the integration tier (`agents/top.md`, `repos/foundations.md`) | 🟢 MIT/BSD on the code — 🔴 **and the vendor's ToU on the access.** See below. |
| To **avoid both constraints** | official API + your own code | 🟢 permissive OneRoster/Ed-Fi implementations, already shelved in the interoperability tier |

### ⚠️ The warning that outranks every licence on this page

For the **second** route above, the licence is not the binding constraint. A proprietary SIS
vendor's Terms of Use can forbid exactly the access an AI integration needs, regardless of
how the client library is licensed. Infinite Campus's ToU — quoted in full in
`agents/top.md`, Finding 2 — prohibits access *"by any means other than our publicly
supported interfaces (for example, scraping or using the content to train artificial
intelligence software)"*, and the one MIT-licensed MCP server for that platform states that
it violates it.

🔵 **Platform selection therefore acquired a new question this pass, and it goes before the
licence question:** *does the institution hold an API agreement with its SIS vendor?* If yes,
the integration route is open and the permissive shelf is usable. If no, the honest options
are the official API (procure it), an open SIS (accept the GPL), or a prototype that is
explicitly not a production path. **Run P26 before scoping either.**

### A platform-tier instrument finding — 3 of 5 default branches are not `main` or `master`

| Platform | Default branch |
|---|---|
| `GibbonEdu/core` | 🔴 **`v31.0.00`** — a version number |
| `portabilis/i-educar` | 🔴 **`2.12`** — a release series |
| `francoisjacquet/rosariosis` | 🔴 **`mobile`** — a feature name |

🔴 **The fourteenth pass found one agent-generated default branch and called `ls-remote
--symref` non-optional. This tier makes it unarguable: a probe that assumes `main` or
`master` returns 404 on the three highest-starred open SIS platforms in existence** and
writes all three down as ungranted. They are not; they are GPL, which is a very different
engagement from unlicensed.

🟢 **And one licence sat at `docs/License.txt`** (mixed case, in a subdirectory, with a
byte-order mark) — `OS4ED/openSIS-Classic`. No filename ladder in this KB would have found
it. **It was found by reading the README's own licence link**, which is a better instrument
than guessing filenames: it is one request, it is authoritative, and the maintainer wrote it
on purpose. Add it to the method ahead of the ladder.

---

## Added in the sixteenth pass of 2026-10-06 — the education-ERP shelf, and the grant that was hiding in a Python manifest

The mandatory vertical query (`open source platform education ERP CRM MIT Apache student
information system`) **passed for the first time in this KB's history** — it named platforms
instead of returning tutorials. Every candidate below was probed on its real default branch on
2026-10-06.

### The platforms, with their licences read correctly

| Platform | Repo | Branch | Licence (payload-verified) | ★ | What it is |
|---|---|---|---|---|---|
| 🟢 **Joanie** | [`openfun/joanie`](https://github.com/openfun/joanie) | `main` | 🟢 **MIT** (1,086 B, *"(c) 2021 France Université Numérique"*) | 30 | A **headless education ERP**: course enrolment/subscription, **payment**, and **certificate delivery**. From the same state-backed org as Richie. |
| 🟢 **eVaka** | [`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) | `master` | **LGPL-2.1-or-later** — ⚠️ via **`LICENSES/`**, not `LICENSE` | 58 | **Finland's early-childhood-education ERP**, in production for the City of Espoo. Kotlin. Enrolment, placement, fee decisions, daily attendance. |
| 🟢 **treVaka** | [`Tampere/trevaka`](https://github.com/Tampere/trevaka) | `main` | **LGPL-2.1** (27,030 B — the full text) | 2 | eVaka adapted for the **City of Tampere**. Active 2026-10-06. 🔵 **Its existence is the finding: eVaka is a multi-municipality platform, not one city's internal tool.** |
| 🔴 **OdooEduERP** | [`JayVora-SerpentCS/OdooEduERP`](https://github.com/JayVora-SerpentCS/OdooEduERP) | `19.0` | 🔴 **AGPL-3.0** — ⚠️ declared in **`school/__manifest__.py`**, top level is NO-PAYLOAD | **157** | The most-starred open-source education ERP found this pass. Admissions, attendance, exams, library, transport, fees — on **Odoo**. Active 2026-10-03. |
| 🔴 **CybroOdoo EducationalERP** | [`CybroOdoo/EducationalERP`](https://github.com/CybroOdoo/EducationalERP) | `16.0` | 🔴 **GPL-3.0** (35,147 B) | 16 | A second Odoo education suite. Branch pinned to Odoo 16. |
| ⚠️ **Frappe edu** | [`nguyentrieu210/edu`](https://github.com/nguyentrieu210/edu) | `main` | 🟢 **MIT** (`license.txt`, 1,069 B) | 6 | Education ERP as a **Frappe app + Vue 3 SPA**. ⚠️ Self-described **"(demo)"**, created 2026-06-20 — a starting point, not a platform. |

### ⚠️ Read this before anyone proposes "the Odoo education ERP" to a client

**`OdooEduERP` reads as unlicensed to every instrument this KB owns, and it is AGPL-3.0.**

Its real default branch is `19.0` — neither `main` nor `master` — and there is **no licence
payload at the top level** on it. A probe returns NO-PAYLOAD, which in this KB's conventions
means *"ask upstream."* The grant is one directory down, in the Odoo module manifest:

    # school/__manifest__.py
    "license": "AGPL-3",

🔴 **This is the expensive direction to be wrong in.** A NO-PAYLOAD verdict invites a team to
proceed while an upstream ask is pending; the truth is a **network-copyleft** licence that
reaches any hosted deliverable built on it. 157★ and active last week means somebody *will*
propose it.

⚠️ **A staleness tell in the same file:** the branch is `19.0` and the manifest inside it still
declares `"version": "18.0.1.0.0"`. Verify which Odoo release it actually targets before
sizing any engagement.

🔵 **Generalised:** this is the third non-`LICENSE` grant location found in one pass (R's
`DESCRIPTION`, REUSE's `LICENSES/`, Odoo's `__manifest__.py`). **In the Odoo ecosystem the
module manifest is the licence of record, and the repository root is often silent.** Any
Odoo-based row in this KB must be probed at the module level.

### 🟢 Joanie is the row that changes the platform menu

This KB's existing shortcut says **MIT at the portal tier is the cleanest place to put
client-visible AI, because the copyleft lives behind it in the LMS** — the Richie
recommendation. Joanie extends that from *presentation* to **transaction**:

| Tier | Permissive option | Licence |
|---|---|---|
| Portal / catalogue | [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** |
| **Enrolment, payment, certificates** | **[`openfun/joanie`](https://github.com/openfun/joanie)** | 🟢 **MIT** |
| LMS / delivery | Open edX (AGPL core, 🟢 **Apache-2.0 plugin SDK**) or Moodle (GPL-3.0) | copyleft |

🔵 **So the whole commercially sensitive surface — catalogue, checkout, credential — can be MIT,
with copyleft confined to course delivery.** Both halves come from **France Université
Numérique**, so they are designed to compose, and both are state-backed rather than
venture-backed. ⚠️ **Joanie is 30★ and issue-heavy (61 open)**: treat it as a solid foundation
to fork, not a turnkey product, and read `payment` integration code before promising a date.

### 🟢 eVaka — and why LGPL-2.1 is a *different* answer from LGPL-3.0 here

The page already argues that **LGPL-3.0 is the middle path** for administrative platforms:
link against it, keep your own modules proprietary, publish changes to the library itself.
eVaka is **LGPL-2.1-or-later**, which lands in the same architectural place — but note what
eVaka actually is:

* 🟢 **A production national-scale ECEC system.** Espoo is Finland's second-largest city, and
  **Tampere runs a derivative** — so the platform has survived being adapted by a second
  municipality, the single hardest test of a public-sector codebase.
* 🟢 **Early childhood is a tier this KB's platform shelf did not cover at all.** Every other
  platform here is K-12, higher-ed or L&D. Placement queues, fee decisions by income, daily
  attendance and statutory child-ratio compliance are a genuinely different domain.
* ⚠️ **The licence is not in `LICENSE`.** eVaka follows the **REUSE specification v3.0**: the
  1,001-byte `LICENSE` is a *pointer* that says, verbatim, *"never the original license
  texts"*, and the grant lives in `LICENSES/LGPL-2.1-or-later.txt` (verified, HTTP 200) plus
  per-file SPDX headers. A payload probe reads NO-GRANT or guesses from prose. **REUSE is an
  FSFE standard and is spreading through EU public-sector code — expect this shape again in
  exactly the region this matters for.**

⚠️ **AI integration point, stated honestly:** eVaka is an administrative system holding data
about **small children**. Under the EU AI Act the attractive automations here — placement
prioritisation, fee determination — are decisions about access to a public service for a
protected group. 🔵 **The defensible AI layer is assistive**: demand forecasting for placement
capacity, caseworker drafting with a human decision gate, anomaly review on attendance. **Not
automated placement.** Pattern `P11` (one oversight gate) is the shape; `P13` sets the
compliance profile.

### Platform selection shortcut — sixteenth-pass additions

| If the client is… | Take | Licence reality |
|---|---|---|
| A **European municipality running early-childhood education** | 🟢 **eVaka** (+ treVaka as the adaptation precedent) | LGPL-2.1-or-later — link, don't fork the core; grant is in `LICENSES/` |
| Selling **courses** and needing catalogue + checkout + certificates | 🟢 **Richie + Joanie** | 🟢 **MIT both** — the commercial surface is clean |
| Asking for **"the Odoo education ERP"** | ⚠️ **OdooEduERP, with the AGPL-3.0 conversation first** | 🔴 AGPL-3.0, declared in the module manifest — network copyleft reaches a hosted deliverable |
| A **Norwegian** institution needing curriculum alignment | 🟢 **Grep SPARQL endpoint** (`repos/foundations.md`) | 🟢 **NLOD — commercial use granted** |

---

## Added in the seventeenth pass of 2026-10-06 — the national-platform tier, and the first licence on this page whose problem is *delivery model*, not permission

Pass 15 found the SIS/MIS tier and reported that **none of it is permissive**. Pass 16 found the
education-ERP shelf. This pass found something the page has not had: **a complete national
platform estate, published by the state, under an OSI licence — where the blocker is neither
"closed" nor "copyleft" but *how you intend to deliver it*.**

### The tier, licence read from the payload on 2026-10-06

| Platform | Owner | Licence (payload-verified) | Scale | What it runs in production |
|---|---|---|---|---|
| **AOE — Avointen oppimateriaalien kirjasto** ([`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe)) | 🇫🇮 Finnish National Agency for Education | 🟡 **EUPL-1.2** (`aoe-web-backend/LICENSE` + `aoe-web-frontend/LICENSE`, 303 B each) | **6,829 commits**, HEAD 2026-10-06, TypeScript | **Finland's national library of open educational resources** (`aoe.fi`) — upload, describe, license-tag and search OER, with a full editorial metadata model. |
| **ePerusteet** ([`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet)) | 🇫🇮 same | 🟡 **EUPL-1.1** (631 B) | Java, active | **The national core curriculum and qualification requirements**, as a service rather than a PDF. |
| **Koski** ([`Opetushallitus/koski`](https://github.com/Opetushallitus/koski)) | 🇫🇮 same | 🟡 **EUPL-1.1** (653 B) | Scala, 23★ | **National study-records service**: every study right and completed qualification, one API. |
| **Ataru** ([`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru)) | 🇫🇮 same | 🟡 **EUPL-1.2** (295 B) | Clojure, 11★ | **The national admissions application engine** — generic form generation driving real intake. |
| **eHOKS** ([`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks)) | 🇫🇮 same | 🟡 **EUPL-1.1** (631 B) | Clojure | **Personal competence-development plans** for vocational learners. |
| **SS 12000 reference API** ([`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api)) | 🇸🇪 Swedish National Agency for Education | 🟢 **Apache-2.0** (11,339 B) | Java, 5★ | Not a platform — **the standard every Swedish school-administration system exchanges data through**, with a working implementation. |

### 🔴 Read this before anyone proposes "the Finnish stack, customised with AI" to a client

The EUPL is **OSI-approved open source** and nothing here is a permission problem. The problem is
that **EUPL copyleft reaches network delivery**, and almost every engagement this page describes
is network delivery.

| Delivery model the studio is actually proposing | EUPL consequence |
|---|---|
| **Call** AOE / Koski / ePerusteet APIs from an agent we build | 🟢 **No obligation.** Using a service is not distribution. This is the safe default and it is where the value is. |
| Deploy an **unmodified** instance for the client, on-prem or hosted | 🟢 Fine; ship the licence and the notices. |
| **Modify** it and run it as the client's **hosted** product | 🔴 **Copyleft triggers.** Art. 1 counts *"communication to the public"* — making functionality available to others, including over a network — as Distribution. Our modifications must be offered under the EUPL. **This is the AGPL shape, and most studio proposals land here.** |
| Modify it, combine with a GPL-3.0 / AGPL-3.0 / MPL-2.0 component, relicense the combined work | 🟡 **Permitted — Art. 5 compatibility list.** ⚠️ And the EC's own published discussion notes that because the compatible licence prevails on conflict, routing through **GPL-3.0** (which has no network clause) can **circumvent the SaaS obligation**. 🔴 **Do not sell this route.** It is documented, it is contested, and it is a question for the client's counsel, not for an architecture deck. |

🔵 **The honest sales line, and it is a better one than a fork would have been:** *"We do not
fork Finland's national services; we build the agent layer that calls them, and we can do that
because the state published the interfaces."* **That proposal has no copyleft exposure at all**,
and the national platform becomes an asset of the engagement rather than a licensing risk.

### 🟢 Why the Swedish row changes the platform menu differently

`dnp-ss12000-reference-api` is **Apache-2.0**, so it carries none of the above. It can go into a
closed, hosted product, and what it gives is the thing integration projects actually burn budget
on: **a national-standard conformant rostering/SIS data exchange, already implemented.**

⚠️ **The limit, stated plainly:** SS 12000 is **Swedish**. It is not an EU standard and not a
Nordic one by fiat. Whether the Finnish services can be reached through an SS 12000 shape — which
would turn one country's standard into a regional integration layer — **is not established in
this KB and should not be implied in a deck.**

### Platform selection shortcut — seventeenth-pass additions

- **Client wants a national OER library** → **AOE** is the only state-run, OSI-licensed one here.
  Call it or deploy it unmodified; do not fork it into a hosted product.
- **Client wants curriculum alignment in EMEA** → **Grep/NLOD (Norway)** if commercial reuse of the
  *data* is the requirement (NLOD grants it outright); **ePerusteet (Finland)** if the requirement is
  depth of the curriculum model. `P25` and `P27` in `compose/patterns.md`.
- **Client wants Swedish school-data integration** → **SS 12000 reference API**, Apache-2.0, lift it.
- **Client wants a learner-identity or study-records model to copy** → read **`oppijanumerorekisteri`**
  and **`koski`**; take the model, write your own code. Reading carries no obligation.
- 🔴 **Client wants to white-label a national platform as their SaaS** → **stop.** That is the one
  cell in the table above that is red, and it is the most common thing to be asked for.


## Added in the eighteenth pass of 2026-10-06 — the assessment delivery tier, and a national agency's service clients

**No new platform this pass.** `open source platform education LMS SIS MIT Apache 2026` returned
the shelf above — Open edX, Sakai, OpenOLAT, OpenEduCat — and nothing new. What it did return is a
**component tier that was never swept**, because the sweeps were organised by topic and these are
filed under a **standard**. Licences read from each repository's own payload on 2026-10-06.

### QTI 3 — assessment item delivery

This is the layer that sits *between* the LMS and the learner, and it is the one place where a
permissive component now carries **third-party conformance certification**.

| Component | Repo | Licence (read from payload) | Use |
|---|---|---|---|
| QTI 3 item player | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (`main/LICENSE`, © 2022-2024 Amp-up.io, LLC) | 🟢 **1EdTech Certified — QTI 3 Basic *and* Advanced "Delivery"**. The default. 30★ |
| QTI 3 item player, Vue 3 | [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (`main/LICENSE`, © 2024) | Same component for a Vue front end |
| QTI 3 toolchain | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (`main/LICENSE.md`, © 2026 Longsight, Inc.) | 12 npm packages — parse, validate, render, **score**, and **migrate QTI 1.2 / 2.x → 3**. The migrator is the part nobody else ships |
| QTI 3 renderer, framework-neutral | [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (`main/LICENSE`, © 2026 AE Studio) | Full response processing, no framework commitment |
| QTI 3 HTML utilities | [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | **MIT** (`main/LICENSE`, © 2026 metyatech) | Smallest surface of the five |
| QTI 3 support, PHP | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (`main/LICENSE`, © 2026 Kennisnet) | The permissive PHP path, where `oat-sa/qti-sdk` is GPL-2.0 |
| QTI item renderer (mature, copyleft) | [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | **GPL-3.0** (`main/LICENSE.md`) | 2,456 commits, 19★ — the most mature here. From **Citolab**, the software lab of **Cito**, the Dutch national assessment institute. ⚠️ README invites relicensing on request — read trends §43 before designing around the licence |
| QTI SDK, PHP | [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`master/LICENSE`) | From the TAO assessment platform. **GPL-2.0**, so **not compatible with GPL-3.0-only code** — the same trap as RosarioSIS above |

🔴 **Do not cite [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components).** It is a
**stale fork** of the Citolab repository — identical root commit `de8b27b`, **79 commits behind**,
1★ against upstream's 19. Pin the upstream address.

### Kennisnet — clients for the Dutch national education services

**[Stichting Kennisnet](https://github.com/Kennisnet)** is the Netherlands' public agency for ICT in
education. Its repositories are not a platform; they are **clients for national services**, which is
a shape this shelf had no entry for. **29 repositories, nine probed: 6 MIT, 1 GPL-3.0, 2 ungranted.**

| Component | Repo | Licence (read from payload) | The national service it reaches |
|---|---|---|---|
| Edurep search client | [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | **MIT** (© 2015 Stichting Kennisnet) | **Edurep**, the national learning-resource index. 🟢 A national OER index you may query under a permissive client |
| Eduterm client | [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) | **MIT** (© 2018 Kennisnet) | **Eduterm**, the national curriculum vocabulary — **in Python** |
| LOM metadata | [`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) | **MIT** (© 2017 Kennisnet) | IMS-LOM records, read and write — **in Python** |
| NL-LOM profile | [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | **MIT** (© 2017 Stichting Kennisnet) | The Dutch national application profile of LOM — the worked example of how a country profiles a global standard |
| OAI-PMH harvesting | [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | **MIT** (© 2024 Kennisnet) | The protocol national repositories actually expose |
| QTI editor | [`Kennisnet/qti-editor-angular`](https://github.com/Kennisnet/qti-editor-angular) | 🔴 **NO-PAYLOAD** | Ungranted — **do not vendor** |
| Edurep transforms | [`Kennisnet/edurep-xslt`](https://github.com/Kennisnet/edurep-xslt) | 🔴 **NO-PAYLOAD** | Ungranted |

⚠️ **Nine of 29 probed**, chosen by stars and domain relevance. The estate's ungranted rate is
**sampled, not established** — carried as declared gap 5 of this pass.

### 🔵 What this adds to the shelf, stated as a rule

The platforms above are mostly **copyleft**, and that decides whether your AI work is a plugin or a
side-car. This tier is different: **assessment delivery and national-service clients are
overwhelmingly permissive**, and they sit exactly at the seam §34 identified — *education's reusable
IP lives at the plugin seam of copyleft platforms, not beside them.* **You will not get a permissive
LMS. You can get a permissive, certified assessment tier and a permissive metadata layer to bolt
onto the copyleft one you inherit.**

## Added in the nineteenth pass of 2026-10-06 — the assistive-technology tier, and the licence verdict that applies to all of it

This page exists for **real systems a client already runs or could run, that AI can be layered
onto**. The assistive-technology estate qualifies on both counts and was never on it: these are the
applications a disabled learner actually operates, they are deployed in schools today, and three of
the four are customisable. Licences read from each repository's own payload on
`raw.githubusercontent.com`, 2026-10-06; counts from the rendered page the same day.

### The tier

| Platform | Repo | Licence (read from payload) | ★ / forks | What it is, and where it sits |
|---|---|---|---|---|
| **Cboard** | [cboard-org/cboard](https://github.com/cboard-org/cboard) | 🔴 **GPL-3.0** (`master/LICENSE.txt`) | **759** | AAC communication board with symbols and text-to-speech, browser-based PWA. **33 languages, 3,400+ Mulberry symbols.** Backed by **UNICEF's Office of Innovation and Microsoft**; © Assistive Technology LLC. Used for cerebral palsy, intellectual disability and autism. 🟢 **The reference AAC deployment in LATAM and the one a ministry will already have heard of.** |
| **AsTeRICS Grid** | [asterics/AsTeRICS-Grid](https://github.com/asterics/AsTeRICS-Grid) | 🔴 **AGPL-3.0** (`master/LICENSE`) | **124 / 65** | AAC app with **offline support**, flexible input (switch, eye-gaze, touch), multilingual TTS, media and smart-home control. JavaScript. **AsTeRICS Foundation + UAS Technikum Wien, funded by the City of Vienna (2018–2025).** 🟢 **EMEA-placed, EU-funded, and offline-capable** — the shape a European municipal tender asks for. ⚠️ **AGPL-3.0: network use triggers source disclosure.** |
| **NVDA** | [nvaccess/nvda](https://github.com/nvaccess/nvda) | 🔴 **GPL-2.0-or-later, with two stated exceptions** (⚠️ `master/copying.txt`) | not read this pass | The dominant free screen reader on Windows, and therefore **the client against which a remediated LMS is actually tested**. ⚠️ **Licence filename note:** `copying.txt` is outside every shortlist this KB probes (`LICENSE*`, `LICENCE`, `COPYING`), so an 11-filename sweep over `main`/`master` reports NVDA as **ungranted** unless lowercase `copying.txt` is in the list. **Add it.** |
| **veraPDF** | [veraPDF/veraPDF-library](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL / MPL** (`LICENSE.GPL` + `LICENSE.MPL`) | not read this pass | The reference **PDF/A and PDF/UA validator**. ⚠️ **Both licence files are named outside every shortlist this KB probes** — `LICENSE.GPL` and `LICENSE.MPL`, present on `master` and on `integration`, absent from `main` — so an 11-filename sweep calls it ungranted while the grant is in the repository root. 🟡 **Invoke it as a CLI, do not vendor it** — then the dual licence stays outside the deliverable. |

### 🔴 The verdict that applies to every row above — do not propose forking any of them

**All four are copyleft, and that is not an accident of this sample.** Searched this pass by
standard, by assistive-technology topic, by AAC, by screen reader and by sign language: **no
permissive end-user assistive application was found in education.** The one apparent exception,
[`sign/translate`](https://github.com/sign/translate), is worse than copyleft — a **non-OSI,
entity-tiered licence** that grants educational institutions free use and **requires a separate
commercial licence for for-profit organisations**, i.e. the client is granted and the integrator is
not (`agents/top.md`).

🟢 **What to do instead, and it is the better business anyway.** The AT applications are the
*client's* deployment, not the studio's product. The permissive work sits **around** them:

1. **Remediate the estate they read.** An LMS, its course content, its PDFs and its ePubs have to
   be navigable by NVDA and by Cboard's switch input. That remediation pipeline is **Apache-2.0 and
   MIT** end to end (`repos/foundations.md`), and it is the deliverable in `compose/patterns.md` P36.
2. **Integrate, don't fork.** Cboard and AsTeRICS Grid both export and import board sets; an
   AI layer that *generates* symbol boards from a lesson plan and hands them over as data touches
   no GPL code. ⚠️ **Generating data for a GPL application does not make your generator GPL.
   Linking into it does.** Keep the boundary at the file format.
3. **Test against them.** NVDA is free and scriptable, so "verified with NVDA" is an evidence line
   a studio can produce at no licence cost — and it is the line that distinguishes a real
   conformance claim from a scanner report.

### Platform selection shortcut — nineteenth-pass additions

| If the client needs… | Take | Why |
|---|---|---|
| An AAC deployment a LATAM ministry will recognise | **Cboard** (GPL-3.0), unforked | UNICEF/Microsoft backing, 33 languages, PWA — deploy and configure, build the AI layer outside it |
| An AAC deployment for a European municipal tender | **AsTeRICS Grid** (AGPL-3.0), unforked | EU-funded, offline-capable, alternative input methods. ⚠️ AGPL on network use |
| To prove a remediated LMS actually works for a blind student | **NVDA** (GPL-2.0+) as a *test client* | Free, scriptable, and the screen reader the user actually has |
| To validate that a PDF is genuinely PDF/UA | **veraPDF** as a *CLI*, not a dependency | Dual-licensed; invoking it keeps the obligation out of the deliverable |
| **To produce** an accessible tagged PDF | 🔴 **Nothing permissive exists** | Searched and not found. Price the tagging as human labour (`repos/foundations.md`) |

---

## Added in the twentieth pass of 2026-10-06 — the transition bucket is a platform-selection input, and nobody had treated it as one

**From the transition-provision channel** (findings in `agents/trending.md`, trend **46** in
`intel/trends.md`, delivery in `compose/patterns.md` under **`P-TRANSITION-EVIDENCE`**).

🔵 **The question this adds to platform selection.** Every selection table in this file asks what a
platform *is* — its licence, its scale, its AI surface. None asks **which transition bucket the
client's deployment of it falls into**, and that is now the variable with the longest lever on cost:
it can be worth four years.

### The three buckets, and what each one makes of the same platform

| Bucket | Who is in it | What the regime gives them | What it costs to leave |
|---|---|---|---|
| **Already in service, public authority** | a ministry, a regional authority, a state university running Moodle, Open edX, Sunbird or an SIS with an AI module already live | 🟢 **EU: until 2030-08-02.** Vietnam: **2027-09-01** for education. Peru: a staged 1–4-year window from Sept 2025 | 🔴 **a change in design** — and the extension does not come back |
| **Already in service, private provider** | a tutoring company, a corporate L&D platform, a private school group | ⚠️ **EU: no extended date — 2027-12-02**, with only the design-stability route available while it lasts | the same change, with two months of runway instead of four years |
| **Not yet in service** | any new deployment, and **any significantly modified existing one** | 🔴 **nothing.** Full Annex III §3 obligations on the day it ships | — |

🔴 **The consequence for this file's own platform shortlist.** A platform is not "AI Act ready" or
not; **a deployment is.** Kolibri, Oppia, Mentingo, Coursemology, Sunbird and OpenMAIC all sit in
whichever bucket the client's circumstances put them in — and the identical technical choice carries
a 2030 date for a state university and a 2027-12-02 date for a private operator. ⚠️ **So record the
buyer's legal form in the selection note, next to the licence.** It is the second field that changes
the answer and the only one this file has never captured.

### What this changes about a platform *migration*

🔴 **A migration is a change in design by construction**, so the standard "move them off the legacy
SIS onto a permissive platform" engagement **forfeits the extension** on the high-risk functions it
carries — admissions scoring, automated grading, placement, proctoring.

🟢 **The sequencing that preserves it, and it is a real delivery option rather than a dodge:**
migrate the **non-high-risk** estate first — content delivery, rostering, administration,
accessibility remediation — and leave the high-risk decision functions on the frozen legacy system,
wrapped in the evidence tier, until the client is ready to pay for conformity on them deliberately.
⚠️ **This is the opposite of the usual advice**, which is to migrate the hard parts first while
budget exists, and the difference is worth stating to the buyer explicitly rather than deciding for
them.

🔵 **And one platform-level note that follows from Vietnam's Decision 33.** Its education category 1
is *"AI systems providing self-learning content using uncontrolled data sources"* — a **corpus**
test, not a decision test. ⚠️ **That catches an RAG tutor bolted onto any of the permissive
platforms on this page**, however benign its pedagogy, unless the corpus is enumerated and
controlled. 🟢 **The platform is not the exposure; the ingestion pipeline is** — which is why
`iterative/dvc` and `great-expectations/great_expectations` (see `repos/foundations.md`) now belong
in a platform conversation that used to be only about licences.

## Added in the twenty-second pass of 2026-10-06 — the platforms a second forge holds, and the first liveness numbers in this KB

Channel: the **GitLab REST API v4**. Licences read from each project's own payload; `★` and
**`last_activity_at` served by the API**, which is the field `api.github.com` would give this KB and
cannot (403 since pass 37). Controls and the detector-error table: `agents/top.md`. Instrument:
`compose/code/gitlab-api-channel/`.

| Platform | Repo | Licence (payload) | ★ · last activity | Placement | What it is, and what it is for |
|---|---|---|---|---|---|
| **ELabSheet** | [cjaikaeo/elabsheet](https://gitlab.com/cjaikaeo/elabsheet) | 🟢 **BSD-2-Clause** | 14 · 2026-09-19 | APAC (Thailand) | **Exercise and examination platform with automatic answer checking** — task authoring plus grading, Python/HTML with a C++ component for compiled-language exercises. Runs standalone; Dockerised in `cjaikaeo/elab-docker`. 🟢 **The most permissively licensed assessment platform on this page** — looser than mentingo (MIT, full LMS) and far smaller, which is the trade |
| **LMS42** | [saxionnl/42/lms42](https://gitlab.com/saxionnl/42/lms42) | 🔴 **AGPL-3.0** | 10 · **2026-10-06** | EMEA (Netherlands) | The LMS **and most of the curriculum** for the Associate degree in Software Development at **Saxion University of Applied Sciences**. A university's production teaching system, committed to daily. 🔴 AGPL-3.0, so not a delivery base — 🟢 but as a *curriculum* artefact under an open licence it is the only one of its kind in this KB |
| **OpenOLAT** *(second host)* | [olatorg/OpenOLAT](https://gitlab.com/olatorg/OpenOLAT) | 🟢 **Apache-2.0** (10,982 B) | 2 · **2026-10-06** | EMEA (Switzerland) | 🟢 **Confirms the Apache-2.0 reading this page already carries for `OpenOLAT/OpenOLAT`, from an independent forge.** The "extend it without the copyleft conversation" recommendation is now double-sourced |
| **RosarioSIS** *(second host)* | [francoisjacquet/rosariosis](https://gitlab.com/francoisjacquet/rosariosis) | ⚠️ **GPL-2.0**, **15,214 B** | 65 · **2026-10-06** | Global (LATAM-relevant) | 🟢 Payload **byte-identical** to this page's GitHub reading. 🔴 GitLab's own detector calls it **`AGPL-1.0`** — a two-family error on a row this page already publishes, which is why the GPL-2.0-not-3.0 warning above stays sourced to the payload and never to a forge field |
| **MoodleNet** | [moodlenet/moodlenet](https://gitlab.com/moodlenet/moodlenet) | 🔴 **AGPL-3.0** | 9 · 🔴 **2023-07-07** | EMEA | Moodle's federated resource-sharing network. 🔴 **Dead by measurement:** three years without a commit on this host. Recorded so no later pass proposes it as the OER-sharing tier |
| **Leitor de Gabaritos** | [elizeubarbosaabreu/leitor-de-gabaritos](https://gitlab.com/elizeubarbosaabreu/leitor-de-gabaritos) | 🔴 **AGPL-3.0** | 0 · 2026-09-23 | ⚠️ LATAM-**plausible**, not declared | **Optical mark recognition (OMR)**: reads hand-filled answer sheets with computer vision, ships through **F-Droid** as an Android app. 🟢 The paper-to-digital assessment tier this KB has never held — the one that matters where exams are still printed. 🔴 AGPL-3.0, and ⚠️ its placement is an inference from Portuguese-language naming only |
| **GitClassrooms** | [git-classrooms/git-classrooms](https://gitlab.com/git-classrooms/git-classrooms) | 🟢 **MPL-2.0** | 3 · 2026-06-16 | ⚠️ **unplaced** (namespace only) | Self-hosted GitHub-Classroom equivalent for GitLab, with a web UI. ⚠️ A **publish-only mirror** of a GitHub repository — pin the upstream, not this copy |

### 🟢 The first liveness distribution this KB has ever measured

Not of its own shelf — of the 534 projects this sweep returned. **It is the shape of a forge's
education corpus, and it is the number no GitHub pass could produce:**

| Measure | Count | Share |
|---|---|---|
| unique projects returned | **534** | 100% |
| touched in **2026** | **254** | **47.6%** |
| touched in the **last 30 days** | **100** | **18.7%** |
| untouched since **before 2024** | **179** | **33.5%** |

🔴 **One education project in three on this forge has not been touched in over two years, and the
only reason this KB can say so is that it finally called an API that answers.** Every GitHub row in
this KB — 475 references, audited for liveness in the nineteenth pass by *licence-payload
reachability* — still has **no commit-recency measurement at all**, because the endpoint that serves
it is 403. 🔵 That is an asymmetry, recorded as trend **52**, not a claim that the GitHub shelf is
stale.

### ⚠️ And the precision of this channel, so no later pass over-reads it

| Defect in the returned set | Count of 534 |
|---|---|
| **no description at all** | **149 (27.9%)** |
| projects sharing a description with another project (12 texts, 67 projects) | **67** |
| — RosarioSIS's own description, cloned | **23 times** |
| — `oer/emacs-reveal`'s description, cloned | **14 times** |
| — ELabSheet's description, cloned | **7 times** |
| slugs matching `ecoscan-*deletion_scheduled*` — scratch clones queued for deletion | **37** |

🔵 **The three most-cloned descriptions in the corpus belong to three projects this pass actually
publishes**, which is a useful accident: on this forge, *being copied* is a weak adoption signal,
and it points at the same rows a human reviewer would pick. 🔴 **But 27.9% of the corpus describes
itself not at all**, so a description-driven triage — the one used here — silently skips more than a
quarter of what it searched. **The 18 published rows are a floor, never a census.**

---

## Added in the twenty-third pass of 2026-10-07 — the platform shelf, dated

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; ages computed against the
reference date 2026-10-06.** Head-commit dates read with `git fetch --depth 1 --filter=blob:none`.

Across the **137** GitHub repositories cited in this file: **54.7% touched in the last 30 days,
73.7% in 2026, 24.1% cold more than a year, 14.6% cold since before 2024.** The headline platforms
are in excellent shape. The ageing is concentrated in two places, and both are places this file
sends clients.

### 🟢 The platform shortlist is alive

| Platform | Repo | Head commit | Age |
|---|---|---|---|
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 2026-10-06 | 🟢 0 d |
| **Coursemology** | [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 2026-10-07 | 🟢 0 d |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 2026-10-07 | 🟢 0 d |
| **OpenMAIC** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 2026-10-07 | 🟢 0 d |
| **Mentingo** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 2026-10-02 | 🟢 4 d |

🟢 **Every permissive platform on the shortlist was committed within the last four days.** The
"permissive platforms are hobby projects" objection, which this file has been answering with ★ and
commit *history*, can now be answered with a date.

### 🔴 Where the ageing actually is

**1. The Sunbird estate — on the shortlist as the only nine-figure-scale permissive platform, and 75% cold.**

| Repo | Head commit | Age |
|---|---|---|
| [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | 2025-09-16 | ⚠️ 385 d |
| [`Sunbird-Ed/SunbirdEd-consumption-ngcomponents`](https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents) | 2023-09-07 | 🔴 1,125 d |
| [`project-sunbird/sunbird-devops`](https://github.com/project-sunbird/sunbird-devops) | 2023-04-26 | 🔴 1,259 d |
| [`project-sunbird/sunbird-telemetry-sdk`](https://github.com/project-sunbird/sunbird-telemetry-sdk) | 2021-07-22 | 🔴 1,902 d |
| [`project-sunbird/sunbird-lms-mw`](https://github.com/project-sunbird/sunbird-lms-mw) | 2020-05-05 | 🔴 **2,345 d** |
| [`project-sunbird/sunbird-analytics`](https://github.com/project-sunbird/sunbird-analytics) | 2020-02-28 | 🔴 2,412 d |

⚠️ **Read this precisely, because it is easy to over-read.** Sunbird's scale claim is real and its
deployments are real. What the dates say is that **the `project-sunbird/*` component repositories
this KB cites are not where current work happens** — the newer `sunbird-ed/*` namespace is. 🔴 **A
proposal that cites `sunbird-lms-mw` is citing a 6.4-year-old repository.** Before Sunbird goes into
a deck, confirm which namespace the client's distribution actually tracks.

**2. The Kuali estate — 100% of it predates 2024, and 100% predates 2021.**

| Repo | Head commit | Age |
|---|---|---|
| [`KualiCo/rice`](https://github.com/KualiCo/rice) | 2020-07-01 | 🔴 2,288 d |
| [`kuali/kfs`](https://github.com/kuali/kfs) | 2018-03-22 | 🔴 3,120 d |
| [`kuali/rice`](https://github.com/kuali/rice) | 2017-05-17 | 🔴 3,429 d |
| [`kuali/kc`](https://github.com/kuali/kc) | 2017-01-06 | 🔴 3,560 d |

🟢 **This confirms rather than overturns the existing "Kuali estate" section**, which already treats
it as a licence lesson (one consortium, three licences) rather than a build target. The dates make
it unambiguous: **the Kuali repositories are a case study, not a shelf.** The same applies to
`foradian/fedena` (**2012-10-12, 5,107 days** — the oldest reference in this entire KB), which this
file already closed as a question.

**3. The Kennisnet metadata layer — 66.7% cold, and it is the layer this file recommends for
curriculum alignment.**

`Kennisnet/pylom` (2020-10-03, 2,194 d), `Kennisnet/py-eduterm-client` (2020-05-23, 2,327 d),
`Kennisnet/phpnllom` (2022-06-28, 1,561 d), `Kennisnet/phpedurepsearch` (2022-12-19, 1,387 d) are
cold; 🟢 `Kennisnet/qti-components` (2026-07-20, 78 d) and `Kennisnet/oaipmh` (2025-09-16, 385 d) are
not. ⚠️ **A national agency's estate ages unevenly** — the QTI work is current, the LOM/Eduterm
Python clients are five to six years old. Pick per repository, never per organisation.

### ⚠️ What this does *not* change

🔵 **A cold platform repository is not a dead platform, and this file should not start pruning on
date alone.** Moodle, Open edX and Canvas are large multi-repository estates whose activity lives in
namespaces this KB does not enumerate; a single cold mirror says nothing about them. What the dates
*do* change is the **citation**: when this file points a client at a specific repository, that
repository's date is now a disclosable fact, and three of the pointers above need replacing with a
live namespace rather than defending.

### The method note

🟢 The channel is `git`, not an API: `api.github.com/repos/*` returns **403** to this environment
(while `api.github.com/` itself returns 200, so it is the resource paths that are denied), and the
rendered `github.com` page returns **403**. `git ls-remote` and a blob-filtered depth-1 fetch both
work, and four invented control slugs swept blind alongside the real ones all failed to resolve —
so the probe discriminates. ⚠️ **No ★ was readable this pass**; every star count in this file
remains pass-22's or older.

---

## Added in the twenty-fourth pass of 2026-10-07 — the integration row on this page pointed at a fork

⏱️ **Ages against the reference date `2026-10-07`.**

The PHP (Moodle-side) row in the integration table above is re-pointed from
`1EdTech/lti-1-3-php-library` to
[`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library). **Same
library, same Apache-2.0 payload, byte-identical** (11,343 B, established pass 23) — the difference
is that the 1EdTech copy's head commit is **2020-06-03 (2,317 d)** and the `packbackbooks` original's
is **2026-09-23 (14 d)**. ⚠️ The 124★ figure belonged to the 1EdTech copy and is **withdrawn, not
transferred**: ★ measures a host's audience for one repository, and no ★ was readable this pass
(`github.com` and `api.github.com` both return 403 here).

### 🟢 The platform-selection consequence, which is the part that changes a bid

Item 2 of the integration guidance on this page said *"Python is where the AI layer lives, and there
is no Python LTI 1.3 library here"*, and concluded that the realistic shape is a Python AI service
plus an LTI adapter in a second runtime, **budgeted as a component**. That is corrected above. The
decision now has three branches, and only one of them still carries the adapter cost:

| AI tier framework | LTI 1.3 launch | Second runtime needed? |
|---|---|---|
| **Django** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — MIT (1,098 B), head commit **2 d**, PyPI [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1 (61 d)** | 🟢 **No.** Launch in-process |
| **JupyterHub** | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) — BSD-3-Clause (1,528 B), 98 d; LTI 1.3 **and** 1.1, tested against Open edX, Canvas and Moodle | 🟢 **No** |
| **Anything else in Python** (FastAPI, Flask, bare ASGI) | ⚠️ one alpha only — [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0 (103 d)**, which **vendors** the 1,416-d-cold `dmitry-viskov/pylti1.3` and leaves its FastAPI adapter unbuilt | ⚠️ **Probably** — `ltijs` (Node, 1 d) or `packbackbooks` (PHP, 14 d) unless you are willing to own the vendored engine |

🔵 **So the adapter is a conditional line item, not a certainty.** Ask which framework the AI tier
uses **before** pricing it. On a Django engagement this removes a component, a second runtime and an
internal API boundary from the architecture that this page previously described as unavoidable.

🔴 **And one boundary to state out loud when the platform is Open edX.**
[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) is the
best-maintained Python LTI 1.3 implementation anywhere — committed and released **6 days** ago — and
it is **AGPL-3.0** (payload 34,520 B). Inside an Open edX deployment it is the right component;
inside a reusable-IP deliverable it is not. That distinction is the whole of **P30**, and it is the
real reason this page read the Python shelf as empty for fourteen passes: the shelf was not empty,
the **well-maintained** part of it was copyleft.

---

## Twenty-fifth pass, 2026-10-07 — a platform is not on one clock, and Sunbird is the proof

Every platform on this page has been dated as a **single row**. Dating the components of one of
them separately, over `git`, changes what a proposal has to say:

| Sunbird component | Head commit | Age |
|---|---|---|
| [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) | 2025-12-16 | 🟢 295 d |
| [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | 2025-09-19 | 🔴 **383 d** |
| [`Sunbird-Ed/SunbirdEd-consumption-ngcomponents`](https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents) | 2023-09-07 | 🔴 **1,126 d** |
| [`project-sunbird/sunbird-lms-mw`](https://github.com/project-sunbird/sunbird-lms-mw) | 2020-05-05 | 🔴 **2,346 d** |
| [`project-sunbird/sunbird-analytics`](https://github.com/project-sunbird/sunbird-analytics) | 2020-02-28 | 🔴 **2,413 d** |

> 🔴 **The portal is current, the mobile app is a year behind, the shared Angular components are
> three years behind, and the original microservice estate is six.** The platform entry on this
> page says *"100+ micro-services are the operational cost"*. **This is that cost, dated.** Scope a
> Sunbird engagement by component and put the `ngcomponents` uplift in the plan before anyone
> demos the portal.

🔵 **The method point generalises past Sunbird.** Any platform published as an estate of
repositories — Open edX, Sunbird, Frappe, Apereo — has a *distribution* of component ages, not an
age. **A single date on a platform row is the age of whichever repository someone happened to
measure.** Where this page shows one date for a multi-repository platform, read it as a sample.

**Dated this pass, every platform on this page, against the reference date `2026-10-07`:**

| Platform | Head commit | Age |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) · [`Coursemology/coursemology2`](https://github.com/Coursemology/coursemology2) | 2026-10-07 | 🟢 **0 d** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) · [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) · [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) · [`oppia/oppia`](https://github.com/oppia/oppia) · [`learningequality/kolibri`](https://github.com/learningequality/kolibri) · [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 2026-10-06 | 🟢 **1 d** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 2026-10-03 | 🟢 4 d |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 2026-10-02 | 🟢 5 d |
| 🔴 [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | **2026-04-30** | 🔴 **160 d** |

🔴 **One row does not look like the others, and it is the one most likely to be in the room.**
Every open source LMS on this page committed within five days — **except Canvas**, at **160 days**,
and this page describes Canvas as *"dominant in North American higher ed"*. ⚠️ **Do not read that
as an abandoned product.** Instructure develops Canvas commercially and publishes to the open
repository in batches, so a long gap on the public mirror is a **release-cadence** fact, not a
maintenance one — which is precisely why this page's existing advice holds: *"the best AI entry
point is its API via MCP, not a fork."* 🔵 **A fork of a batch-published mirror inherits the batch
cadence**, and that is the sentence to put in a bid, with the date attached. Full table:
`compose/code/p436-fork-hypothesis/recency.2026-10-07.tsv`.

⚠️ **And one citation defect fixed on this page.** `sunbird-ed/sunbirded-mobile-app` and
`Sunbird-Ed/SunbirdEd-mobile-app` are the **same repository** — GitHub resolves owner and repo
names case-insensitively — and this page cited both spellings. Nine such pairs existed across the
six non-append-only files, **18 references for 9 repositories**, each of which a compiler keying on
the reference string would have emitted twice. All normalised, with
`compose/code/p439-case-collision-gate/` (9 controls) added so they cannot come back.

## The EUPL national-stack tier — a complete public education data layer under one licence family

Measured 2026-10-07. These are not components to build on top of in the usual sense; they are the
**systems of record** a European public buyer already runs, and an AI layer is procured as integration
with them.

| Platform | Repo | Licence | What it is of record for |
|---|---|---|---|
| ePerusteet | [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | 🟡 **EUPL-1.1** | national core curriculum and qualifications |
| Koski | [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) | 🟡 **EUPL-1.1** | national study records — qualifications and study rights |
| AOE | [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | 🟡 **EUPL-1.2** | national OER library (`aoe.fi`), 6,829 commits |
| Ataru | [`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru) | 🟡 **EUPL-1.2** | admissions application forms |
| Organisaatio | [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) | 🟡 **EUPL-1.1** | register of providers and institutions — the join key for the rest |
| Oppijanumerorekisteri | [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | 🟡 **EUPL-1.1** | national learner identity |
| eHOKS | [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | 🟡 **EUPL-1.1** | personal competence-development plans (vocational) |
| Suorituspalvelu | [`Opetushallitus/suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) | 🟡 **EUPL-1.2** | attainment service (2025, the newest) |

🔵 **Read the set, not the rows.** Identity (`oppijanumerorekisteri`), the institution register
(`organisaatio`), curriculum (`eperusteet`), admissions (`ataru`), records (`koski`), attainments
(`suorituspalvelu`), vocational plans (`ehoks`) and open content (`aoe`) is a **complete national
education data stack**, published by one agency under one licence family, with `organisaatio` as the
join key. 🟢 **For an EMEA public-sector engagement this is the integration surface**, and it is far
more specific than "integrate with the LMS".

🔴 **Three things to settle before the proposal, not during delivery:**

1. **The EUPL binds a hosted service.** Article 5 carries the copyleft obligation and Article 1's
   definition of *"Communication"* covers network use, so a SaaS deliverable incorporating an EUPL
   component triggers it where a shipped binary would. ⚠️ The Appendix's compatibility list (GPL-2.0,
   AGPL-3.0, LGPL-2.1, MPL-2.0, EPL-1.0) is a **re-licensing option for derivative works**, not relief.
2. **`aoe`'s grant is in subdirectories**, `aoe-web-backend/LICENSE` and `aoe-web-frontend/LICENSE`,
   303 B each — invisible to any rooted licence probe, including the one this KB ran until this pass.
3. 🔴 **npm's `aoe` package is NOT this project.** It is v0.1.1, published 2016-01-05 by
   `exolution@163.com`, with no description and no declared repository, and it declares **GPL-3.0**.
   A tool that resolves the name would hand a procurement team the wrong licence for a national service.

🟢 **And this is the normal case in EMEA rather than an exception**: the EUPL is the licence the
European Commission recommends for public-sector software, so a studio that can answer the
hosted-service question in writing is ahead of one whose scanner reports `UNKNOWN` — which is what both
of this KB's classifiers did until this pass.

⚠️ **Adjacent, same region, and unresolved:**
[`european-commission-empl/european-digital-credentials`](https://github.com/european-commission-empl/european-digital-credentials)
asserts **EUPL-1.2 in a README badge** (`edci-issuer/licence-EUPL 1.2-brightgreen.svg`) and ships **no
licence text anywhere in its tree**, which a complete enumeration confirms. That is `P314`: a grant to
request in writing from DG EMPL, citing the Commission's own badge. Its Maven artefacts are reachable
for metadata but **the POM layer answers 429 intermittently** from this environment, so its
machine-readable licence field is unmeasured rather than absent.

## The platform tier's restrictive licences are hand-recorded and invisible to the automated classifier — twenty-seventh pass, 2026-10-07

🔵 **Why this belongs in the verticals file.** The rows most likely to carry a **non-OSI,
source-available** licence are platforms, not libraries: a vendor with a managed-service business
picks Elastic or BSL precisely so a competitor cannot host it. This file records those correctly,
**by hand**. The classifier three of this KB's instruments call does not see them at all.

Measured over all 412 `LICENSED` root payloads
(`compose/code/p445-classifier-divergence/`, instrument note **P445**, trend **64**):

| Platform | This file says | `p436/sweep_payload.py:family_of` says | `lib/license_family.sh` says |
|---|---|---|---|
| **Advising App** ([`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp)) | 🟢 **Elastic License 2.0** — *"Not open source"* | 🔴 **`UNKNOWN`** | 🟢 **`Elastic`**, commercial **NO** |
| **Leemons** ([`leemonade/leemons`](https://github.com/leemonade/leemons)) | 🟢 **Composite / "Fair code"** | 🔴 **`UNKNOWN`** | ⚠️ `UNCLASSIFIED`, commercial **NO** |
| [`sodadata/soda-core`](https://github.com/sodadata/soda-core) | — | 🔴 **`UNKNOWN`** | 🟢 **`Elastic`**, commercial **NO** |
| [`digillab-lmu/smart-rag`](https://github.com/digillab-lmu/smart-rag) | — | 🔴 **`UNKNOWN`** | 🟢 **`PolyForm`**, commercial **NO** |

🟢 **This file was right about both platforms before either classifier was pointed at them**, which
is pass 26's **trend 61** holding again — *where this KB's prose and its instruments disagree about
a licence, it has been the instrument.* ⚠️ **But "right by hand" does not scale**, and the two rows
with no entry above are the proof: `soda-core` and `smart-rag` carry the same class of licence and
nobody had written them down.

### 🔴 The asymmetry that matters for this tier

`family_of` returns `UNKNOWN` for all four. **`UNKNOWN` is not a warning** — it reads as *"needs a
look"*, and in a 412-row sweep it sits beside thirteen other `UNKNOWN`s that are merely unparsed.
The shell classifier returns `Elastic`, `PolyForm` and a **commercial-use verdict of `NO`**, which
is a *decision*.

⚠️ **And the reverse blindness bites this same file.** Nine **EUPL-1.2** rows — the Finnish National
Agency for Education's eight repositories and the European Commission's `European-Learning-Model`,
all of them public-sector platform assets recorded in this file and in `repos/foundations.md` — are
reported `UNCLASSIFIED` by the shell classifier and correctly as `EUPL` by the Python one.
**Neither tool alone can audit this tier.**

### 🟢 The rule for a platform engagement

1. **Never conclude a platform is permissively licensed from one classifier.** Run both
   (`P-GRANT-ENUMERATION` step 8, under an hour, no network).
2. **Treat `UNKNOWN` on a platform as a strong signal, not a weak one.** Of the 13
   `PYTHON-UNKNOWN` rows in this shelf, **3 are source-available licences that forbid the
   deliverable** and the rest are unparsed permissive text. The base rate for a *platform* in that
   bucket is nothing like the base rate for a library.
3. **Quote the classifier beside the verdict and the path beside both** — *"Elastic 2.0, per
   `lib/license_family.sh` on `main/LICENSE`"*. On this shelf a bare family name is wrong once in
   ten.

## Corrected in the twenty-ninth pass of 2026-10-07 — openSIS is GPL-2.0, and its licence is not where a sweep looks

[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) and
[`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) are
real, deployed Student Information Systems and belong on this page's **SIS tier**. Two things
about them were wrong or unstated, and both matter for platform selection.

### 🔴 The licence is GPL-2.0, and this KB had it as `LGPL?`

Read first-hand from `docs/License.txt` (**17,286 bytes**, opening on a plain
`GNU GENERAL PUBLIC LICENSE / Version 2, June 1991`):

| Platform | published | 🟢 corrected | Commercial use | Tier |
|---|---|---|---|---|
| openSIS-Classic | `LGPL?` | **GPL-2.0** | 🟢 allowed | SIS |
| openSIS-Responsive-Design | `LGPL?` | **GPL-2.0** | 🟢 allowed | SIS |

The `?` was honest about its own uncertainty, and the uncertainty had a cause: the classifier
probed the LGPL over the whole payload body, and **GPL-2.0's closing paragraph recommends the
LGPL** (*"If this is what you want to do, use the GNU Lesser General Public License instead of
this License"*). One sentence of advice inside the licence decided the family (`P455`).

⚠️ **The correction tightens the architecture menu rather than loosening it.** GPL-2.0 is
**project-level** copyleft, so the LGPL reading was the *more* permissive one: an LGPL
platform could be linked from a proprietary module, and a GPL-2.0 one cannot. **Extend
openSIS the way this page already prescribes for strong-copyleft platforms — a side-car over
its API, not a module inside it** — and keep the client's own code outside the copyleft
boundary.

### 🔴 There is no root licence file, which changes how you audit it

Neither repository carries a licence at the repository root. Both are absent from the 412 root
payloads this KB sweeps, and `p441` files them `OWN-GRANT-IN-SUBTREE`.

🔵 **For a platform decision that is a due-diligence note, not trivia.** A client's own
procurement scan — and most automated licence scanners — look at the root. On openSIS they
find nothing and may report the platform as **unlicensed**, which it is not. **Point the audit
at `docs/License.txt` explicitly, in writing, in week one.**

⚠️ **And ignore `docs/LICENSE.rtf`.** It is 61,575 bytes of RTF wrapping the same GPL-2.0
text. Because the RTF header occupies the title block, this KB's own classifiers cannot read
it and the commercial-use question falls through to a body token match that finds GPL-2.0
**§3(c)**'s *"allowed only for noncommercial distribution"* — a condition on one distribution
option, not a restriction on the licensee — and answers **PROHIBITED** (`P460`). Both
repositories are now reported `CONTAINER-RTF (no legible)` rather than guessed at. **The
authoritative file is the plain-text one.**

## Added in the thirty-first pass, 2026-10-07 — a permissive LMS base, and a production autograder

### Sunbird / DIKSHA — the MIT-licensed national-scale LMS base

| Component | Repo | Licence (payload) | Region |
|---|---|---|---|
| LMS service tier | [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service) | **MIT** (`master/LICENSE`) | APAC |
| Learner portal | [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** (`master/LICENSE`) — already shelved | APAC |

**Sunbird** is India's education digital public infrastructure and the stack behind **DIKSHA**,
operating at national scale. **Why it matters more than its star count:** it is **MIT**. Every other
customisable LMS base on this shelf carries a copyleft or non-OSI condition —
**Moodle is GPL-3.0**, **Open edX is AGPL-3.0** (with some Apache-2.0 components), **OpenEduCat is
LGPLv3**, **frappe/lms is AGPL-3.0** (corrected on this shelf; *not* MIT, despite being
mis-reported). **Sakai is Apache-2.0 / ECL-2.0** and remains the other permissive option.

**Customisation posture:** with Sunbird you can build an AI layer *in-tree* and redistribute it under
your own terms. With Moodle or Open edX you cannot, which is exactly why the **side-car MCP boundary**
(`peancor/moodle-mcp-server`, MIT *because* it sits outside the GPL-3.0 Moodle tree) exists on this
shelf. **Choose the base from the redistribution requirement, not the feature list.**

### Pawtograder — autograding + CourseOps, with MCP already wired in

| Component | Repo | Licence (payload) | Region |
|---|---|---|---|
| Platform | [`pawtograder/platform`](https://github.com/pawtograder/platform) | 🟡 **GPL-3.0-or-later** | North America |
| CI grading action | [`pawtograder/assignment-action`](https://github.com/pawtograder/assignment-action) | 🟡 **GPL-3.0-or-later** | North America |

A real system — in production at **Northeastern**, built by educators (© 2025 Jonathan Bell), lineage
from **Autolab** and **Autograder.io** for grading plus **GitHub Classroom** for repo workflow. It
bundles CI autograding, rubric handgrading, Q&A, an office-hours queue and a gradebook, and **exposes
course context to staff-side LLMs through an MCP server**.

⚠️ **GPL-3.0-or-later.** Self-hosting it for an institution is unproblematic and is the normal
deployment. Linking it into a proprietary product, or shipping a derived closed platform, is a
licence event. The **transferable design idea** — autograding in CI, handgrading as a separate
human-authority step, graders that are themselves regression-tested — carries no licence at all, and
in a jurisdiction with OK/MD-style human-oversight rules that separation is the compliant shape.
