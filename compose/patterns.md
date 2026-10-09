---
industry: education
region: Global
updated: 2026-10-09
---

## 🟢 Eighty-eighth pass, 2026-10-09 — two new recipes: a **permissive credentialing spine** that leaves the AGPL issuer alone, and a **high-risk assessment conformance pack** built once for Vietnam + EU Annex III

⏱️ **Nineteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every repo named below was payload-read at a pinned SHA this pass or an earlier one, and carries its
licence and ref inline.** 🔴 **No row in these recipes is a secondary-source claim.**

---

### 🟢 `R58` — Permissive credentialing spine on top of a client's existing issuer (EMEA-first)

🔵 **Why this shape:** `P942` — the credential **format** layer is MIT/Apache, the **issuing server** is
AGPL-3.0. 🔴 **Forking the issuer into a closed hosted product trips `§13`.** 🟢 **So the recipe leaves the
issuer alone and owns everything around it.**

**Wiring, concretely:**

1. 🟢 **Data model —** [`impierce/digital-credential-data-models`](https://github.com/impierce/digital-credential-data-models)
   (**Apache-2.0**, 11 357 B, 🔴 **`dev`** · `6ca306e`). Rust types for **OB v3.0 + the European Learner
   Model (ELM)**. 🔵 This is the typed spine; everything else converts into or out of it.
2. 🟢 **Conversion —** [`impierce/credential-converter`](https://github.com/impierce/credential-converter)
   (**Apache-2.0**, 11 356 B, `main` · `f3ff22a`). W3C VC ⇄ OpenBadges ⇄ ELM with a mapping CLI. 🟢 Same
   authors as the models, so the seam is upstream-maintained rather than yours.
3. 🟢 **Signing + selective disclosure —** [`brody-0125/signet-core`](https://github.com/brody-0125/signet-core)
   (**Apache-2.0**, 11 358 B, `main` · `5b3949d`). W3C VC 2.0, EdDSA, ECDSA. 🔵 **Selective disclosure is
   the feature that makes a credential privacy-safe for a minor** — a learner proves a competency without
   revealing the transcript.
4. 🟢 **Achievement definitions —** [`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget)
   (**MIT**, 1 080 B, `main` · `896596a`). The authoring surface for what a badge actually asserts.
5. 🟢 **Skills vocabulary —** [`BeBadges/escobadges`](https://github.com/BeBadges/escobadges)
   (**MIT**, 1 067 B, 🔴 `master` · `2f71bef`) binds achievements to **ESCO**, the EU skills
   classification. 🔵 **This is what makes the credential portable across EU employers instead of being
   a logo.**
6. 🟢 **Learner-held wallet —** [`iblai/wallet`](https://github.com/iblai/wallet) (**MIT**, 1 063 B,
   `main` · `0be99d0`). Next.js/TypeScript; the client surface you brand.
7. 🟢 **Verification —** [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens)
   (**MIT**, 1 080 B, `main` · `d34f262`). Zero-dependency, **works offline** — 🔵 which matters for a
   verifier run by an employer or a border authority with no network guarantee.
8. 🔴 **Issuer — INTEGRATE, DO NOT FORK.** [`edubadges/badgr-server`](https://github.com/edubadges/badgr-server)
   (**AGPL-3.0**, 34 519 B, 🔴 `develop` · `9419acc`) if the client is in Dutch/EU higher education
   (operator: **SURF**), or [`fedora-infra/tahrir`](https://github.com/fedora-infra/tahrir)
   (**AGPL-3.0**, 34 917 B, 🔴 `develop` · `ddbff5c`, **85★**) as a reference issuer. 🟢 **Run it
   unmodified behind its own API, or write your own issuer against the Apache-2.0 models in step 1.**

🟡 **Licence posture:** steps 1–7 are **MIT/Apache-2.0** and compose into closed deliverables.
🔴 Step 8 stays at arm's length across a network boundary. 🟢 **The whole spine except the issuer is
Globant's.**

⏱️ **Shape of effort:** 8–10 weeks to a credential issued, held and verified end-to-end, with the
issuer integrated rather than built. 🔴 **Add time if the client has no issuer at all** — writing one
against the Apache-2.0 models is a larger piece of work than the other seven steps combined.

🔵 **Where it sells:** EMEA higher education and sector skills bodies — the EU supplies the data model
(ELM), the taxonomy (ESCO) and a live consortium operator (SURF). 🟢 **North America variant:**
`opensalt/OB3DefinitionWidget`'s holder is **Public Consulting Group**, a US firm already in this layer.

---

### 🟢 `R59` — High-risk assessment conformance pack, built once for Vietnam + EU Annex III

🔵 **Why now:** 🔴 **Vietnam's Law on AI has been in force since 1 March 2026 and names education as one
of six high-risk sectors, with *automated assessment* and *behavioural monitoring* as its examples.**
🟢 The EU's Annex III says the same thing about education. 🔴 **Korea's penalty grace period expires in
January 2027.** 🔵 **One pack, three jurisdictions, and the engineering is the same.**

🔴 **Scope boundary first, because it is a prohibition and not a control:** `P764` — **in US public K-12
(NYC guidance) grading, promotion, discipline, crisis intervention, IEP/504 assembly and academic
placement are PROHIBITED uses. No human-in-the-loop converts a prohibited use into a permitted one.**
🟢 **So this pack is for the jurisdictions that CONDITION the use (EU, Vietnam, Korea), and the US K-12
deliverable is the teacher-facing green band instead.**

**Wiring, concretely:**

1. 🟢 **Autograding substrate —** [`autolab/Tango`](https://github.com/autolab/Tango) (**Apache-2.0**) or
   [`Submitty/Submitty`](https://github.com/Submitty/Submitty) (**BSD-3-Clause**, 1 542 B,
   `main` · `80d7d66`), both with named institutional operators (CMU, RPI). 🔴 **`P934`: `autolab/docker`,
   Tango's own installer, grants NOTHING — deploy from your own manifests, not theirs.**
2. 🟢 **Measurement layer —** `pyedmine` (**MIT**) for knowledge tracing + cognitive diagnosis, with
   `py-irt` / `catsim` for IRT and adaptive testing. 🔵 **This is the layer that produces the evidence a
   high-risk audit asks for: what was measured, on what model, with what uncertainty.**
3. 🟢 **Human-review gate —** the conditioning regimes require a human decision point on the
   consequential step. 🔵 **Build it as a state transition that cannot be skipped, not as a UI
   suggestion** — an auditor reads the state machine, not the screen.
4. 🟢 **Proctoring, only where lawful —** `SafeExamBrowser/seb-win-refactoring` (**MPL-2.0**, ETH Zürich
   consortium). 🔴 **`Gap 349` stands: this tier has not been audited against EU Art. 5(1)(f)
   emotion-inference prohibition.** 🟢 **Of the one row audited, `Proctoring-AI`, 0 of 7 functions infer
   affect.** 🔴 **Do not ship affect inference; it is prohibited, not high-risk.**
5. 🟢 **Credential out —** hand the result to `R58`'s spine so a passed assessment becomes a portable,
   ESCO-bound, selectively-disclosable credential.

🟡 **Deliverable that clients actually buy:** a **conformance dossier** — the model card, the
measurement provenance, the human-review state machine, the data-retention posture, and the
jurisdiction matrix (EU Annex III / Vietnam's six sectors / Korea's grace clock / NYC's red band).
🔵 **The code is half of it; the dossier is what passes an audit.**

⏱️ **Shape of effort:** 10–12 weeks, and 🟢 **it amortises** — the second jurisdiction is a matrix row,
not a rebuild.

---

### 🟡 `R60` — LATAM institutional AI-governance starter kit

🔵 **Why:** 🔴 **UNESCO measures >50% teacher adoption in Chile and Brazil against <10% of institutions
having formal guidelines.** 🟢 **The gap is the product, and it is not primarily software.**

1. 🟢 **Policy baseline:** acceptable-use, assessment-integrity posture, disclosure rules, data-retention
   defaults. 🔵 Anchor it to **UNESCO's Observatory on AI in Education for Latin America and the
   Caribbean** (launched Santiago, 2026) rather than a vendor framework.
2. 🟢 **Teacher-readiness path** — 🔴 **the binding constraint, and Korea proves it**: AI textbooks lost
   official status in August 2026 after sub-30% adoption *on teacher-preparedness grounds*. 🔵 **A
   governance kit without a training path reproduces Korea's outcome.**
3. 🟢 **Sovereign-model anchor:** **Latam-GPT**, coordinated by **CENIA** (Chile), which signed a
   cooperation agreement with **UNESCO Santiago in early 2026** on AI literacy and ethical AI.
4. 🟡 **Platform reality:** the region's deployed supply is copyleft — the `portabilis` suite (AGPL-3.0),
   `ipti/br.tag` (GPL-2.0), `JuezUN/INGInious` / UNCode (AGPL-3.0, Universidad Nacional de Colombia).
   🟢 **Build beside it; the studio's layer is the governance and the intelligence.**
5. 🔴 **Regulatory state: no national AI-in-education rule surfaced for Brazil, Chile or Colombia.**
   🟡 Brazil's **PL 2338** and a Chilean AI bill are **named as unprobed**, not reported as absent —
   🔵 which means the kit should be written to be re-pointed, not hard-coded to today's vacuum.

⏱️ **Shape of effort:** 6–8 weeks for the first institution, and 🟢 **most of it is reusable across the
>90% of institutions in the same position.**

## Recipes, 2026-10-09 — pass 87

Every repo named below was existence-checked with `git ls-remote` and licence-read from its payload at
`HEAD` this pass. **Licence class is stated for each component** because the copyleft boundary is the
design decision in education: LMS/SIS are copyleft, the interop layer is permissive.

🔴 **Blocked components — do not compose these** (verified this pass):
`DMontgomery40/mcp-canvas-lms` (no grant), `nirholas/ai-tutor-mcp` (proprietary),
`minouza/MathCrew` (PolyForm Strict), `vieanderes/understory` *content* (CC BY-NC-SA).

---

### P1 — Offline-first tutoring for low-connectivity public education → **LATAM, APAC**
*Grounded in the OECD Digital Education Outlook 2026 rural-Brazil pilot (offline SLMs on mobile).*

| Role | Component | Licence |
|---|---|---|
| Learning platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| On-device speech | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** |
| Tutor loop | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) or [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | **MIT** |
| Retention | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** |

**Wiring.** Kolibri is the content/progress system of record and already syncs opportunistically; run a
small quantised model under Ollama on the same device or a classroom hub, expose Anki-backed spaced
repetition as an MCP tool, and have the Bloom/OpenTutor loop generate practice from Kolibri's local
channel content. Sherpa-ONNX gives Spanish/Portuguese speech in/out with no network.
🟢 **Every component is MIT/Apache** — embeddable and redistributable for a ministry client.
**Why it wins:** connectivity is the binding constraint, and this stack never requires a round trip.

---

### P2 — AI tutor as a certified LTI tool beside an untouched LMS/SIS → **North America, EMEA**
*The pattern that avoids the copyleft problem and the SIS gap entirely.*

| Role | Component | Licence |
|---|---|---|
| LTI 1.3 tool provider | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) *(Node)* / [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) *(Python)* | **Apache-2.0 / MIT** |
| Tutoring engine | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** |
| Evidence store | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** |
| Standards binding | [opensalt/opensalt](https://github.com/opensalt/opensalt) | **MIT** |
| Agent orchestration | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | **MIT** |

**Wiring.** The tutor runs as its own LTI 1.3 tool; Moodle/Canvas/Open edX launches it with roster and
context, so **no GPL/AGPL code is modified or redistributed** and no SIS fork is needed. Every tutor
interaction is written to `lrsql` as xAPI statements; `opensalt` maps each activity to the official
competency framework. Grades return over LTI AGS.
🟢 **Licence boundary is clean and the audit trail is a by-product** — which is what the Dec-2027 EU
high-risk documentation duty and NA district policies actually ask for.

---

### P3 — Assessment with a provable human decision point → **North America (Idaho SB 1227), EMEA (high-risk)**
*Built to satisfy "AI may not be the primary basis for grading" and EU high-risk oversight.*

| Role | Component | Licence |
|---|---|---|
| Learning + assessment platform | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** |
| Sandboxed grading runner | [autolab/Tango](https://github.com/autolab/Tango) | **Apache-2.0** |
| Static-analysis grading | [kit-sdq/autograder](https://github.com/kit-sdq/autograder) | **MIT** |
| CI-based pilot | [uhafner/autograding-github-action](https://github.com/uhafner/autograding-github-action) | **MIT** |
| Decision log | [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** |
| Trace/eval | [langfuse/langfuse](https://github.com/langfuse/langfuse) | 🟡 **MIT Expat, except `ee/` dirs** |

**Wiring.** Tango/KIT-autograder produce a **recommendation plus evidence**, never a grade. Artemis
presents it to an instructor who confirms or overrides; the override is written to `lrsql` with actor,
timestamp and rationale. The released grade carries a human actor by construction.
🟢 **The compliance artefact is the decision log**, and it exists because of the architecture rather than
a policy document. Start with the GitHub action for a two-week pilot, then move to Artemis.
🔴 **Do not** ship autonomous release of grades, or any attention/emotion component (prohibited in the EU).

---

### P4 — Licensed agent desk over the institution's system of record → **all regions**

| Role | Component | Licence |
|---|---|---|
| Canvas access | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** |
| Moodle access | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | **MIT** |
| Agent runtime | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | **MIT** |
| Teacher-facing skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) · [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | **MIT** |
| Source-grounded materials | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** |

**Wiring.** MCP servers expose the LMS as tools; the agent drafts lesson materials, feedback and
announcements, with `lineage-skill` keeping every generated artefact traceable to the source document the
teacher supplied. Teacher approves before anything is published.
🔴 **Use `vishalsachdev/canvas-mcp`, not `DMontgomery40/mcp-canvas-lms`** — the latter has **no licence
grant** despite appearing 8× in this KB's earlier passes.
**Why it wins:** addresses the largest measured gap anywhere (≈86 % of SEA teachers using AI untrained,
18 % of US teachers given any guidance) without touching student-facing assessment risk.

---

### P5 — AI-literacy curriculum delivery against statutory mandates → **North America**
*Alabama HB 329 (AI instruction to graduate), Utah HB 218 (grade 7/8 course), Ohio district policy deadline.*

| Role | Component | Licence |
|---|---|---|
| Interactive courseware | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** |
| Component authoring | [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 *(README-declared)* |
| Standards alignment | [opensalt/opensalt](https://github.com/opensalt/opensalt) | **MIT** |
| Material generation | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | **Apache-2.0** |
| Quiz generation | 🔴 ~~`bobuel/bloom-taxonomy-quiz-builder-skill`~~ — **no licence grant**; use `lineage-skill` (Apache-2.0) for quiz generation instead | — |

**Wiring.** Oppia's misconception-handling lesson model suits AI-literacy content, where the goal is
correcting beliefs about AI rather than drilling procedure. `opensalt` binds each lesson to the state
standard the statute references, so the district can evidence compliance per student.
🟢 **Sells against a deadline with a named statute** — the easiest education procurement conversation in
North America this year, and notably it does **not** require student-facing AI at all.

---

### P6 — EMEA sovereign self-hosted stack → **EMEA**
*Uses the European permissive shelf end to end; no US SaaS dependency.*

| Role | Component | Licence | Origin |
|---|---|---|---|
| LMS | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | CH/DE |
| Assessment | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | TU München |
| Grading analysis | [kit-sdq/autograder](https://github.com/kit-sdq/autograder) | **MIT** | KIT |
| Learning records | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | France Université Numérique |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** | — |
| LTI boundary | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | — |

**Wiring.** Everything self-hosted, models local under Ollama, learning records in Ralph, assessment in
Artemis behind the P3 human-decision gate.
🟢 **The whole stack is MIT/Apache and European-governed** — a real data-sovereignty argument rather than
a hosting-region claim, and it carries no AGPL network-use exposure.
🔴 Must exclude any emotion/attention-recognition component: **prohibited in EU education institutions
since 2 February 2025**.

---

🟡 **`langfuse` is a split grant — read before you vendor it.** Its `LICENSE` (1 612 B) puts everything
under `ee/`, `web/src/ee/` and `worker/src/ee/` under a **separate enterprise licence**, with MIT Expat
for the remainder. Self-hosting the open core is fine; do not assume the whole repo is MIT.
🔵 **Its copyright holder is now `ClickHouse, Inc.` (2023-2026)** — ownership of this observability
dependency has changed, which is worth knowing before standardising on it.

🔵 **All component licences in the patterns above were payload-read at `HEAD` this pass**, including the
infrastructure rows (`ollama` MIT 1 058 B, `sherpa-onnx` Apache-2.0 11 358 B, `pydantic-ai` MIT 1 100 B).

## 🟢 Eighty-sixth pass, 2026-10-09 — **three recipes, and the first one is the shelf's first END-TO-END permissive stack from a single institution**: platform + test sandbox + OS confinement, all MIT. Plus a LATAM public-sector recipe where AGPL is an asset, and a district-scale US recipe built to run with the AI switched OFF

⏱️ **Eighteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🔵 **Every component named below was payload-read inline this pass at a recorded ref · sha, with the measurement method stated (`curl -w '%{size_download}'`, per `P929`).** 🔴 **No recipe here has been executed end to end** — these are compositions of verified grants, not delivered systems, and each closes with what that leaves unproven.

---

### 🟢 `P86-R1` — **Programming-course autograding, fully permissive, fully sandboxed** (EMEA-first)

🔵 **Why this recipe is different from every prior one on this shelf:** 🟢 **all three components are MIT, from the same research group, and one of them is in production at a named university.** 🔴 **Every earlier autograding composition here mixed licence families or stopped at the platform and left execution safety unspecified.**

| layer | component | grant · bytes · ref · sha | role |
|---|---|---|---|
| platform | 🟢 [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) · 816★ | 🟢 **MIT** · **1 091 B** · 🔴 `develop` · `760e2e1` | Course delivery, exercise management, automated feedback, live at **`artemis.tum.de`** |
| test isolation | 🟢 [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) · 5★ | 🟢 **MIT** · 1 345 B (5 holders, `P931`) · `main` · `47cbe8c` | Java test sandbox: static analysis + runtime instrumentation, hidden tests |
| OS confinement | 🟢 [`ls1intum/phobos`](https://github.com/ls1intum/phobos) · 🔴 **0★** | 🟢 **MIT** · 1 241 B · `main` · `945c76b` | **Landlock + network allow-list** — student code cannot reach the network |
| CI entry (optional) | 🟢 [`uhafner/autograding-github-action`](https://github.com/uhafner/autograding-github-action) · 32★ | 🟢 **MIT** · 1 095 B · `main` · `4e65432` | Grade against metrics in CI you already run |
| non-numeric answers | 🟢 [`rstudio/tblcheck`](https://github.com/rstudio/tblcheck) + [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 🟢 **MIT** (R `DESCRIPTION` rung) · `main` · `539b54e` / `70543ad` | Grade **tables** and **figures**, not just values |

🟢 **Wiring:**
1. 🟢 Deploy **Artemis** as the course platform; it already expects an external execution service.
2. 🟢 Run student submissions through **Ares2** for the test harness, and wrap that execution in **phobos** so the sandbox is enforced at the OS level rather than trusted at the JVM level. 🔴 **Do not skip phobos** — Artemis executes untrusted code by design, and `phobos` is the confinement boundary.
3. 🟡 For courses already on GitHub, put **`autograding-github-action`** in front as a zero-infrastructure on-ramp, then migrate to Artemis when the course outgrows it.
4. 🟢 Add **`tblcheck`/`ggcheck`** for data-science courses where the answer is a table or a plot.

🔴 **Why `phobos` is the load-bearing piece and why you would miss it:** 🔴 **it has zero stars and sits 90 rows deep in the channel.** 🔵 **Star-ordered discovery finds the platform and loses its security boundary** (`P935`).

🔴 **What this leaves unproven:** 🔴 none of the three has been deployed or run by this shelf — the composition is inferred from READMEs and payloads at the refs above. 🔴 **`develop` is Artemis's default branch (`T1`)**, so the pinned-release story is unverified. 🔴 Landlock requires a recent Linux kernel; no version floor was established. 🟡 **EU AI Act**: grading that influences qualification access is **high-risk** → a conformity assessment is required before placing on market, and that dossier is not part of this recipe.

---

### 🟢 `P86-R2` — **Public-university autograding for LATAM, where AGPL-3.0 is an ASSET** (LATAM-first)

🔵 **The premise this recipe inverts:** 🔴 **this shelf has treated AGPL as a disqualifier for 86 passes.** 🟢 **For a ministry or public-university engagement it is frequently the opposite** — §13's source-offer obligation is what a public body wants from a publicly funded system, and it blocks a vendor from later enclosing it.

| layer | component | grant · bytes · ref · sha | role |
|---|---|---|---|
| platform | 🟢 [`JuezUN/INGInious`](https://github.com/JuezUN/INGInious) — **UNCode** · 8★ | 🔴 **AGPL-3.0** · 34 840 B · 🔴 `master` · `4a45903` | 🟢 **In production at the Universidad Nacional de Colombia, Bogotá.** Grades C/C++, Java, Python 3, **Verilog/VHDL**, Jupyter. Has an **LMS bridge**. |
| big-data assignments | 🟢 [`iVishalr/BigHOST`](https://github.com/iVishalr/BigHOST) · 2★ | 🟢 **MIT** · 1 083 B · `main` · `0348cc7` | Parallel grading of Big Data jobs (PES University, CCGridW 2023) |
| item authoring | 🟢 [`asahi417/lm-question-generation`](https://github.com/asahi417/lm-question-generation) · 366★ | 🟢 **MIT** · 1 064 B · 🔴 `master` · `dde629c` | 🟢 **Multilingual** question generation — the Spanish/Portuguese path |
| formative loop | 🟢 [`athina-edu/athina`](https://github.com/athina-edu/athina) · 3★ | 🟢 **MIT** · 1 099 B (at **`LICENCE`**) · 🔴 `master` · `5c12c2f` | Formative-assessment microservice, sits beside the platform rather than inside it |

🟢 **Wiring:**
1. 🟢 Adopt **UNCode** as the platform — it is the only row on this shelf, in any region, that grades **hardware description languages**, which matters for engineering faculties.
2. 🟢 Keep **BigHOST** and **athina** as *separate services* behind the LMS bridge. 🔵 **This is the licence-hygiene move:** AGPL's reciprocity follows the modified work, so leaving the MIT components as independent services across a network boundary keeps them MIT.
3. 🟢 Use **`lm-question-generation`** for Spanish-language item authoring — 🔵 it is the only multilingual row in the item tier.
4. 🟢 Lead the engagement with the **governance framework**, not the platform: 🟢 **87% of LATAM institutions use AI, 74% to grade, and only 26% have any formal framework** (UNESCO IESALC). 🔵 **The platform is table stakes; the framework is the deliverable.**

🔴 **What this leaves unproven:** 🔴 **UNCode's upstream (`UCL-INGI/INGInious`) opens its LICENSE with "Most of the files … are distributed under the GNU AGPL v3 licence"** — 🔴 **the per-file exception list has NOT been read** (`P936`), and it must be before any redistribution. 🔴 UNCode tracks INGInious **v0.5**; upstream drift unmeasured. 🔴 The network-boundary argument in step 2 is a licensing *posture*, not legal advice — have counsel confirm it. 🔴 Colombia has **no AI statute** (CONPES 4144 is policy), so the compliance target is institutional, not statutory.

---

### 🟢 `P86-R3` — **District-scale US autograding that still works with the AI switched OFF** (North America-first)

🔵 **This recipe exists because of a regulatory finding, not a technical one.** 🔴 **NYC's March 2026 guidance prohibits AI for grading, discipline, placement and IEP development.** 🔴 **Oklahoma and Maryland require human oversight and bar AI from high-stakes decisions about students.** 🟢 **So the deliverable must degrade gracefully to deterministic grading and remain useful.**

| layer | component | grant · bytes · ref · sha | role |
|---|---|---|---|
| platform | 🟢 [`Submitty/Submitty`](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** · **1 542 B** · `main` · `80d7d66` | Autograding + course management (RPI) |
| grading service | 🟢 [`autolab/Tango`](https://github.com/autolab/Tango) · 49★ | 🟢 **Apache-2.0** · **11 324 B** · 🔴 `master` · `24558e3` | 🟢 **RESTful autograding service** — a clean service boundary (CMU Autolab) |
| deterministic checks | 🟢 [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) · 3★ · + [`earthlab/matplotcheck`](https://github.com/earthlab/matplotcheck) · 23★ | 🟢 **BSD-3-Clause** · 108 B stub (`P932`) / **1 508 B** · `master` · `693b3df` / `main` · `c1b6a3b` | R / notebook / **figure** grading, **no model in the loop** |
| 🟢 **AI layer, switchable** | 🟢 [`professor-john-fulton/repo-grading-assistant`](https://github.com/professor-john-fulton/repo-grading-assistant) · 🔴 0★ | 🟢 **MIT** · 1 070 B · `main` · `7fa9446` | 🟢 **Rubric-based AI feedback where the EDUCATOR sets the final grade** |
| local dev | 🟢 [`naasanov/gslocal`](https://github.com/naasanov/gslocal) · 4★ | 🟢 **MIT** · 1 071 B · `main` · `66ce3d1` | Run Gradescope-shaped autograders locally in Docker |

🟢 **Wiring:**
1. 🟢 **Submitty** (or Tango behind an existing LMS) as the platform; 🔵 **Tango is the better choice when the district already owns an LMS**, because it is a service rather than an application.
2. 🟢 Make **ottr + matplotcheck** the *default* grading path. 🔵 These are deterministic — they satisfy NYC's prohibition and Oklahoma/Maryland's human-oversight rules without any carve-out.
3. 🟢 Add **`repo-grading-assistant`** as a **feature-flagged** advisory layer: it generates rubric feedback and 🟢 **by design does not set the grade.** 🔴 **Flag it off by default**; turn it on only where district policy permits.
4. 🟢 Ship **`gslocal`** to instructors so they can develop autograders without the hosted service.
5. 🟢 **Package the evidence, not just the software:** AB 1159 (no student data to model training), Idaho S.B. 1227 (privacy), the human-oversight attestation, and the switch state per district. 🔵 **With 33–35 states issuing guidance and districts writing their own policy, the configuration-plus-evidence pack is the repeatable product** — there is no statewide procurement to win.

🔴 **What this leaves unproven:** 🔴 **`autolab/docker`, Tango's own official installer, declares NO licence across 14 probed paths** (`P934`) — 🔴 **so the documented install route is unlicensed and a Compose file must be written from scratch.** 🔴 Submitty's own install path was not probed this pass. 🔴 The feature-flag design is asserted from the README's "educator sets the final grade" claim; 🔴 **the repo has 0★ and no deployment evidence** — treat as a pattern to implement, not a component to depend on. 🟡 The reported NYC moratorium on student-facing AI through 8th grade could not be confirmed from a primary source.

---

### 🔴 Recipes this pass deliberately did NOT write

- 🔴 **No APAC recipe.** 🟢 Reason stated rather than left blank: APAC's statutory picture is now the most concrete of any region (`T5`), 🔴 **but it has no single posture** — Vietnam binding and education-specific, Korea in force with a grace period, Singapore and Japan voluntary. 🔵 **A recipe that averaged them would be wrong in every jurisdiction.** 🟢 **Costed for pass 87: one recipe per jurisdiction, starting with Vietnam, because its high-risk list names automated assessment explicitly.**
- 🔴 **No LMS-integration recipe.** 🔴 **`Gap 334` is unspent for a third pass**: Moodle, Open edX, Canvas, Sakai, OpenEduCat and Chamilo licences are asserted by sources that contradict each other. 🔵 **Writing an integration recipe onto an unverified licence base would be the most expensive error available on this shelf**, because the LMS is the component the client already owns.
- 🔴 **No recipe uses `kangwonlee/gemini-python-tutor`**, despite it being an on-topic APAC AI tutor — 🔴 its licence adds **field-of-use restrictions** (`P930`, `Gap 353`) and is unadjudicated.

## 🟢 Eighty-fifth pass, 2026-10-09 — **three new recipes, and the first one replaces a greenfield build with a permissive production platform a European university already operates.** The proctoring recipe pass 84 refused to write is now writable — and its constraint turns out to be the AI Act, not the licence

⏱️ **Seventeenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🔵 **Every component named below was payload-read inline this pass at a recorded ref · sha, or in a pass that recorded one.** 🔴 **No recipe here has been executed end to end** — these are compositions of verified grants, not delivered systems, and each one closes with what that leaves unproven.

---

### 🟢 `P926` — **The automated-feedback engagement, built ON Artemis rather than beside it** (primary region: 🟢 **EMEA**; directly reusable in 🟢 **North America**)

🔵 **Why now:** 🟢 `Gap 346` discharged this pass. 🔴 **For 84 passes the platform tier had no permissive production row, so every recipe in this file composed primitives into a greenfield build.** 🟢 **That is no longer the honest recommendation.**

**Components, all payload-read:**

| role | component | grant | ref · sha |
|---|---|---|---|
| 🟢 **platform core** | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | 🟢 **MIT** (1 090 B) | 🔴 `develop` · `760e2e1` |
| grading job runner, if Artemis's own is outgrown | [`autolab/Tango`](https://github.com/autolab/Tango) | 🟢 **Apache-2.0** (11 323 B) | 🔴 `master` · `24558e3` |
| style/structure grading for Java cohorts | [`kit-sdq/autograder`](https://github.com/kit-sdq/autograder) | 🟢 **MIT** (1 067 B) | `main` · `a439007` |
| notebook-native grading for data courses | [`google/prog-edu-assistant`](https://github.com/google/prog-edu-assistant) | 🟢 **Apache-2.0** (11 357 B) | `main` · `bc61a51` |
| figure grading, Python / R | [`earthlab/matplotcheck`](https://github.com/earthlab/matplotcheck) · [`rstudio/ggcheck`](https://github.com/rstudio/ggcheck) | 🟢 **BSD-3** (1 508 B) · 🟢 **MIT** (`DESCRIPTION`) | `main` · `c1b6a3b` · `main` · `70543ad` |
| LMS interoperability | `ltijs` (Apache-2.0), `1EdTech/lti-1-3-php-library` (Apache-2.0) | 🟢 permissive | carried, passes 71–76 |
| learning-record store | `yetanalytics/lrsql` | 🟢 **Apache-2.0** | `main` · `cb794e4` |

**Wiring:**
1. 🟢 **Stand up Artemis and integrate it to the client's existing LMS over LTI 1.3** — 🔵 **do not replace the LMS.** `Artemis` is the teaching-and-feedback layer; the LMS keeps enrolment and gradebook. 🟢 **This is `P913` made concrete with a real artefact underneath it.**
2. 🟢 Point Artemis at the client's own Git and CI. 🔵 Its exercise model already assumes per-student repositories, which is why it integrates rather than needing to be rebuilt.
3. 🟢 **Add graders by course type, not by preference:** `kit-sdq/autograder` for Java cohorts, `prog-edu-assistant` for notebook courses, `matplotcheck`/`ggcheck` where the artefact assessed is a *figure*. 🔵 **Figure grading is the capability clients ask for and nothing else on this shelf has.**
4. 🟢 Emit xAPI to `lrsql` from the start. 🔵 **This is the `9%` fix** — see `P928`.
5. 🟡 **If grading throughput outgrows Artemis's built-in runner**, put `Tango` behind it: 🟢 it is a standalone RESTful service, so it is the one component with a clean process boundary.

🟢 **Licence closure: MIT + Apache-2.0 + BSD-3 throughout. No copyleft, no NOTICE-only rows, no riders.** 🔴 **Deliberately excluded: [`foundation50/classroom50`](https://github.com/foundation50/classroom50) (GPL-3.0, 212★) and [`infomark-org/infomark`](https://github.com/infomark-org/infomark) (GPL-3.0)** — 🔵 **both are good systems and a client may name `classroom50` directly as "the GitHub Classroom alternative"; the answer is that it cannot be embedded in a resold product, and Artemis does the same job under MIT.**

🟢 **Why the reference matters as much as the code:** 🔵 **a European public buyer's hardest question is "who else runs this?"** 🟢 **Artemis answers it with TU München operating `artemis.tum.de`** — an institutional reference a studio cannot manufacture.

🔴 **What this recipe does NOT prove:** no component was cloned, built or run this pass (passes 78–85 measured script execution DENIED here). 🔴 **Artemis at 12 315 commits is a substantial operational commitment** — self-hosting cost, upgrade cadence and the `develop`-as-default-branch convention all need a real spike before a fixed-price quote. 🔴 **`Gap 350`: no evidence of APAC or LATAM deployment**, so an engagement in those regions would be the first and should be priced that way.

---

### 🟢 `P927` — **The exam-integrity engagement: the recipe pass 84 refused, now writable — and the binding constraint is the AI Act, not the licence** (primary region: 🟢 **EMEA**; reusable in 🟢 **APAC**)

🔴 **Pass 84 refused to write this recipe, correctly, on the evidence it had:** *"zero of the five probed proctoring rows is permissive … writing a recipe would mean composing a deliverable out of components that cannot be in a deliverable."* 🔴 **`Gap 344` is FALSIFIED this pass** — the two biggest rows in the tier were never read.

**Components, all payload-read this pass:**

| role | component | grant | ref · sha | ★ |
|---|---|---|---|---|
| 🟢 **behavioural detection** | [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) | 🟢 **MIT** (1 071 B) | 🔴 `master` · `4f284a3` | 633 |
| 🟡 **lockdown client** | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) | 🟡 **MPL-2.0** (16 726 B) | 🔴 `master` · `016d234` | 354 |
| item authoring (fresh items per sitting) | [`ramsrigouthamg/Questgen.ai`](https://github.com/ramsrigouthamg/Questgen.ai) · [`asahi417/lm-question-generation`](https://github.com/asahi417/lm-question-generation) | 🟢 **MIT** · 🟢 **MIT** | 🔴 `master` · `edf8f6a` · 🔴 `master` · `dde629c` | 951 · 366 |
| similarity / integrity analysis | `dolos` (MIT), `automoss` (MIT) | 🟢 permissive | carried, pass 84 |
| evidence log | `yetanalytics/lrsql` | 🟢 **Apache-2.0** | `main` · `cb794e4` | — |

**Wiring:**
1. 🔴 **Draw the prohibition boundary FIRST, before any component choice.** 🟢 **Art. 5(1)(f) bans AI inferring emotions in education institutions — in force since 2025-02-02, untouched by the Digital Omnibus.** 🟢 **`Proctoring-AI` was audited this pass: its seven functions are gaze direction, mouth-opening, person counting, phone detection, head pose, face spoofing and audio speech — 🟢 zero infer affect.** 🔴 **So the rule for this recipe is explicit: ship presence and behaviour signals, never affect, attention or engagement inference.** 🔵 **A vendor offering "engagement detection" is offering a prohibited product, and saying so is a differentiator.**
2. 🟡 **Keep the MPL-2.0 boundary at the file level, which is where MPL puts it.** 🟢 `seb-win-refactoring` may ship inside a commercial product; 🔴 **modifications to its own files must be published.** 🟢 **So: configure and wrap it, do not patch it** — and if patching is unavoidable, the patch is published and the rest of the product is not. 🔵 **This is categorically easier than the `JPlag` GPL problem (`Gap 345`), which needs a process boundary.**
3. 🟢 **Generate fresh items per sitting** rather than detecting reuse of a fixed bank. 🔵 **Item generation is the structural answer to leaked question banks**, and it is now permissive — use `lm-question-generation` where the language of instruction is not English.
4. 🟢 Run `dolos` for similarity analysis, as an external service where the deliverable is resold.
5. 🟢 **Log every signal to `lrsql` with the human decision attached.** 🔴 **Annex III makes this high-risk from 2027-12-02: risk management, logging and human oversight are legal requirements, not product polish.** 🟢 **And the conformity route is internal control, not a notified body — third-party assessment applies only to biometric systems under Annex III point 1.**

🟢 **Licence closure: MIT throughout except one MPL-2.0 file-scoped component, deliberately placed where its obligation is cheapest.** 🔴 **Deliberately excluded: the four GPL rows pass 84 found** (`Aankh`, `ITMOproctor`, `moodle-quizaccess_proctoring`, `devkit-lti1p3`) — 🟢 **no longer a gap, just the more expensive option.**

🔴 **What this recipe does NOT prove:** 🔴 **the affect audit covers ONE row.** `Gap 349` records that the rest of the tier is unaudited, and this recipe must not be extended with an unaudited detector. 🔴 **`Proctoring-AI` is research-grade** — its own README pins `sklearn==0.19.1` for the face-spoofing model and notes parts still use dlib; 🔴 **treat it as a validated approach with named components, not a deployable service.** 🔴 **Nothing was run.**

---

### 🟢 `P928` — **The evaluation-evidence engagement: selling the 9%** (primary region: 🟢 **LATAM**; directly reusable in 🟢 **North America**)

🔵 **Why now, and this is the strongest commercial case on the shelf:** 🟢 **UNESCO IESALC Working Paper 16 measures 87% of 200 LATAM institutions using AI and 9% with formal evaluation mechanisms.** 🟢 **In the same quarter, the US Dear Colleague letter of 20 Aug 2026 tells districts to remove tools that do not improve learning.** 🔴 **Two regions, one unmet requirement: nobody can demonstrate the tool worked.** 🔵 **Every other recipe in this file builds a capability. This one builds the evidence that a capability paid off** — which is what gets a renewal signed.

**Components:**

| role | component | grant | ref · sha |
|---|---|---|---|
| learning-record store | `yetanalytics/lrsql` | 🟢 **Apache-2.0** | `main` · `cb794e4` |
| knowledge tracing / cognitive diagnosis | `pyedmine` (MIT), `EduStudio` (MIT) | 🟢 permissive | carried, pass 80 |
| psychometrics — IRT, item quality | pass 84's IRT tier | 🔴 **GPL-dominant (`P907`)** — 🟡 **see the boundary note below** |
| grading signal | [`okpy/ok`](https://github.com/okpy/ok) (Apache-2.0, 🔴 multi-grant file `P916`) · [`matplotcheck`](https://github.com/earthlab/matplotcheck) (BSD-3) | 🟢 permissive | 🔴 `master` · `f5610a7` · `main` · `c1b6a3b` |
| retention scheduling + its own measurable outcome | [`free-spaced-repetition-scheduler`](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | 🟢 **MIT** (1 089 B) | `main` · `93ed713` |
| cohort reporting | `metabase` / `superset` | 🟡 carried — verify grant before use |

**Wiring:**
1. 🟢 **Instrument first, model later.** Emit xAPI from whatever the institution already runs into `lrsql`. 🔵 **The 9% figure is not a modelling deficiency, it is an instrumentation deficiency** — most institutions cannot answer the question because the events were never recorded.
2. 🟢 **Define the outcome before the dashboard**, and prefer one a registrar already tracks: gateway-course pass rates, time-to-competency, retention into the next term. 🔴 **A usage metric is not an outcome**, and a usage dashboard is what the 26%-with-a-strategy already have.
3. 🟢 Fit knowledge-tracing models with `pyedmine` / `EduStudio` on the recorded data to separate *learning* from *activity*.
4. 🟡 **Boundary note on psychometrics, stated because `P907` makes it unavoidable:** 🔴 **the IRT/CAT tier is GPL-dominant.** 🟢 **Run item-quality analysis as an INTERNAL analytical step producing reports, not as an embedded library in a resold product** — 🔵 the same external-service pattern `Gap 345` forces on `JPlag`, and it is unproblematic here because item calibration is a periodic analysis, not a runtime path.
5. 🟢 **Deliver the evidence file, not the dashboard:** instrumented outcome definitions, a baseline, a dated measurement, and the human decisions logged against it. 🔵 **That artefact satisfies the Dear Colleague duty in North America, the Annex III risk-management file in EMEA, and the governance deficit IESALC measured in LATAM — one build, three buyers (`T5`).**

🟢 **Licence closure for everything in the product boundary: Apache-2.0, MIT, BSD-3.** 🟡 **The GPL psychometrics tier is deliberately outside it.** 🔴 **`okpy/ok`'s LICENSE is a multi-grant bundle (`P916`) — its own grant is Apache-2.0, and a client's legal review should be handed that reading explicitly rather than the file.**

🔴 **What this recipe does NOT prove:** 🔴 nothing was run; 🔴 **`metabase`/`superset` grants are CARRIED, not payload-read this pass**, and must be verified before they enter a deliverable; 🔴 **the IESALC figures describe fieldwork from August–October 2025**, so they size the opportunity rather than describe today.

---

### 🔴 Recipes still deliberately NOT written

🔴 **No platform-REPLACEMENT recipe.** 🟢 **`P926` above is the answer and it is deliberately an integration, not a replacement:** the established LMS/SIS tier remains 8-of-8 copyleft (`Gap 334`), clients do not want it replaced, and `Artemis` sits above it by design.

🔴 **No recipe built on `Gego-K12/gegok12` or `foradian/fedena`**, despite both being permissive. 🟢 **`P924`: a platform row needs a permissive grant AND a maintained codebase AND a named operator.** 🔴 `GegoK12` has 123 commits and more forks than stars; `fedena` is copyright 2011. 🔵 **Both are recorded as verified rows and neither is a base to build on.**

🔴 **No affect- or engagement-detection recipe, and there never will be one.** 🟢 **Art. 5(1)(f) is a prohibition, not an obligation with a deadline.** 🔵 **Recorded here rather than left implicit, because it is the one place a client request should be refused on the spot.**

---


## 🟢 Eighty-fourth pass, 2026-10-09 — **three new recipes**, and the first one is the tier this shelf did not have yesterday: academic integrity, 7-of-8 permissive, with the GPL flagship deliberately held OUTSIDE the product boundary

⏱️ **Sixteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🔵 **Every component named below was payload-read inline this pass or in a pass that recorded its ref · sha.** 🔴 **No recipe here has been executed end to end** — these are compositions of verified grants, not delivered systems, and the distinction is kept explicit in each one's closing note.

### 🟢 `P911` — **The academic-integrity engagement, with an evasion threat model** (primary region: 🟢 **North America**; directly reusable in 🟢 **EMEA**)

🔵 **Why now:** integrity is the question every institution is asking in the LLM era, 🟢 **the permissive supply is unusually good (7 of 8)**, and 🔴 **a 400★ evasion tool (`CloakBox`) is the second-most-starred row in the proctoring channel** — so a scope without an evasion model fails on contact.

🟢 **Components, with the licence boundary stated:**

| layer | component | grant | role |
|---|---|---|---|
| 🟢 code similarity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | 🟢 **MIT** (1 084 B, `main` · `44925b8`) | 🟢 **Embedded.** Primary detector for programming submissions. |
| 🟢 Python-specific | [`fyrestone/pycode_similar`](https://github.com/fyrestone/pycode_similar) | 🟢 **MIT** (`master` · `34ecc94`) | 🟢 **Embedded.** Second opinion on intro-CS Python, where language-aware beats generic. |
| 🟢 cohort batching | [`automoss/automoss`](https://github.com/automoss/automoss) | 🟢 **MIT** (`main` · `67cd400`) | 🟢 **Embedded.** Whole-assignment sweeps — the shape a registrar needs. |
| 🟢 prose | [`NoplagLabs/noplag-engine`](https://github.com/NoplagLabs/noplag-engine) | 🟢 **Apache-2.0** (11 358 B, `main` · `aaf7839`) | 🟢 **Embedded.** Self-hosted verbatim + near-verbatim for essays. |
| 🔴 **evasion detection** | [`josemmo/plagpatrol`](https://github.com/josemmo/plagpatrol) | 🟢 **MIT** (`master` · `039e3b6`) | 🔴 **The layer most scopes omit.** Detects documents tampered to bypass detectors. |
| 🔴 **high-citation detector** | [`jplag/JPlag`](https://github.com/jplag/JPlag) | 🔴 **GPL-3.0** (35 141 B, `main` · `3ee7de9`), 2 000★ | 🔴 **DEPLOYED AS AN EXTERNAL SERVICE, called over HTTP — never linked.** |
| 🟢 LMS seam | `LTI 1.3` + AGS adapter | 🟢 studio-written (pass 78 recipe) | 🟢 Grade/artefact exchange with Moodle or Canvas. |
| 🟢 oversight record | `P891` evidence pack | 🟢 studio-written | 🟢 Satisfies Maryland/Oklahoma human-review and disclosure duties. |

🔴 **The one decision that must be made before any integration work starts:** 🟢 **`JPlag` is GPL-3.0 and 10× more cited than every permissive alternative.** 🟢 **Running it as a separate process the product calls keeps the GPL boundary outside the deliverable and still gives the client the detector their faculty will ask for by name.** 🔴 **Linking it as a library licenses the product.** 🔵 **Same binary, same results, two commercial outcomes — decided by process topology, at zero cost, if decided early.**

🟢 **Timeline: 8–10 weeks.** 🔵 Weeks 1–2 integrity policy + evasion threat model with the academic-conduct office (🔴 **not an engineering task, and it drives the rest**); 3–5 `dolos` + `pycode_similar` + `automoss` behind one submission API; 6–7 `noplag-engine` for prose and `plagpatrol` on every submission; 8 `JPlag` service deployment and the licence-boundary memo; 9–10 LTI 1.3 wiring and the `P891` oversight pack.

🟡 **What this recipe does NOT do:** 🔴 **it does not adjudicate.** 🟢 Every detector output is evidence for a human conduct process — which is also what Oklahoma's "no high-stakes decisions without human review" requires, 🔵 **so the compliance constraint and the right design are the same thing here.**

### 🟢 `P912` — **The permissive adaptive-testing spine** (primary region: 🟢 **APAC**, where curricula are now mandated at national scale; reusable 🟢 **Global**)

🔵 **Why this recipe exists:** this shelf has carried knowledge tracing for forty passes with no *testing* tier underneath it. 🟢 **`topics/item-response-theory` supplied one this pass** — 🔴 **and `P907` means the obvious route is the wrong one: the R psychometric stack is 1-of-8 permissive, so this recipe is deliberately all-Python.**

🟢 **Components:**

| layer | component | grant | role |
|---|---|---|---|
| 🟢 adaptive engine | `douglasrizzo/catsim` | 🟢 **MIT** (shelved) | 🟢 Computerised adaptive testing — item selection, stopping rules, simulation before a real learner sees it. |
| 🟢 IRT estimation | `eribean/girth` | 🟢 **MIT** (shelved) | 🟢 Item calibration from response data. |
| 🟢 **uncertainty** | [`eribean/girth_mcmc`](https://github.com/eribean/girth_mcmc) | 🟢 **MIT** (1 061 B, `main` · `911376e`) | 🔴 **The layer that makes a score defensible.** Bayesian posterior → "0.7 ± 0.3", not "0.7". |
| 🟢 latent structure | [`OpenMx/OpenMx`](https://github.com/OpenMx/OpenMx) | 🟢 **Apache-2.0** (🔵 `DESCRIPTION` rung) | 🟡 **Only where SEM is genuinely needed** — measurement invariance across cohorts. 🔴 R, so it sits in the analysis pipeline, not the product. |
| 🟢 calibrated instrument | [`englishcentral/ovlt`](https://github.com/englishcentral/ovlt) | 🟢 **MIT** (`main` · `f4487e4`) | 🟢 A ready vocabulary-level test — a working item bank to validate the pipeline against. |
| 🟢 constructed response | [`doheejin/ProTACT`](https://github.com/doheejin/ProTACT) | 🟢 **BSD-3-Clause** (1 496 B, `main` · `4038143`) | 🟢 Trait-aware essay scoring — per-rubric-dimension, which is what a rubric is. |
| 🟢 CJK writing | [`shibing624/judger`](https://github.com/shibing624/judger) | 🟢 **Apache-2.0** (`master` · `7c0817c`) | 🟢 **The only CJK-language scorer on this shelf** — load-bearing for a China or Japan engagement. |
| 🟢 item interchange | [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) + [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground) | 🟢 **MIT** / **MIT** | 🟢 Authors write Markdown, ship QTI 3.0; inspect the XML when it breaks. |
| 🟢 migration | [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert) | 🟢 **Apache-2.0** (`main` · `9d4f95a`) | 🟢 Lifts existing Canvas quiz banks in, so the client is not starting from zero. |

🔴 **Explicitly avoided, and this is the recipe's main design claim:** 🔴 `ShinyItemAnalysis` (GPL-3), `sirt`, `CDM`, `TAM`, `dina`, `ShadowCAT` (all GPL) — 🟢 **the R stack the client's institutional research office already uses.** 🟢 **Use it internally for analysis; keep it out of the deliverable.** 🔵 **`P907` priced this split before a line was written, which is the whole point of the pattern.**

🟢 **Timeline: 10–12 weeks.** 🔵 Weeks 1–2 blueprint + item bank audit, `qti-convert` on legacy banks; 3–5 `girth` calibration and `catsim` simulation against synthetic populations (🟢 pair with `theaiagent/SynthEd`, MIT, from pass 83 — **test the test before a learner meets it**); 6–7 `girth_mcmc` for posterior uncertainty and the appeals story; 8–9 constructed response via `ProTACT` (+ `judger` for CJK); 10–12 `markdown-to-qti` authoring pipeline and delivery integration.

🟡 **Honest limits:** 🔴 **`OpenMx`'s Apache-2.0 rests on a single `DESCRIPTION` field with no licence file** — confirm against CRAN metadata before it is load-bearing. 🔴 **`ovlt` is an instrument for ONE construct** (vocabulary); every other domain needs its own calibrated bank, and that is psychometric work, not engineering.

### 🟢 `P913` — **The copyleft-boundary analytics layer** (primary region: 🟢 **LATAM**; the pattern is 🟢 **Global** and applies to any GPL LMS)

🔵 **Why this is the LATAM recipe specifically:** 🟢 **`Gap 343`'s discharge measured Brazil's deployed school stack and it is AGPL-3.0 end to end** (`i-educar` 718★, `i-diario` 117★, `pre-matricula-digital` 21★) 🔴 **plus `ipti/br.tag` at GPL-2.0.** 🟢 **The client already runs these and should keep running them** — this recipe never touches them.

🟢 **The architecture, and it is one sentence:** 🟢 **a permissively-licensed client that reads the copyleft platform over its network API carries no copyleft obligation into the client.**

| layer | component | grant | role |
|---|---|---|---|
| 🔴 **client's platform — UNTOUCHED** | `portabilis/i-educar` + `i-diario`, or `ipti/br.tag` | 🔴 **AGPL-3.0 / GPL-2.0** | 🔴 **Stays the client's deployment. No fork, no plugin, no in-process extension.** |
| 🟢 **the boundary** | REST / API reads only | — | 🟢 **Where the licence obligation stops.** |
| 🟢 analytics client | [`yjx0003/UBUMonitor`](https://github.com/yjx0003/UBUMonitor) | 🟢 **MIT** (1 088 B, `master` · `7fde822`) | 🟢 **The reference implementation of this exact pattern** — a desktop learning-analytics client over a live Moodle. Spanish-language UI already. |
| 🟢 feature extraction | [`pnb/dlwed17`](https://github.com/pnb/dlwed17) | 🟢 **MIT** (UIUC) | 🟢 Autoencoder features from raw educational event data. |
| 🟢 prediction | [`gassantos/evolvedtree`](https://github.com/gassantos/evolvedtree) | 🟢 **MIT** (`master` · `9a9649a`) | 🟢 GA + decision tree — 🔵 **interpretable by construction**, which matters where the governance framework is still being written. |
| 🟢 curriculum anchor | `bncc-dev/bncc-dados` + `bncc-pacotes` | 🟢 shelved (BNCC as open data, MCP server) | 🟢 Aligns findings to Brazil's **national curriculum**, not a generic taxonomy. |
| 🟢 open-data layers | [`agn3si/ResultadosUNAM---data`](https://github.com/agn3si/ResultadosUNAM---data) · [`sumeedu/bancodeitinerarios`](https://github.com/sumeedu/bancodeitinerarios) | 🟢 **MIT** · **Apache-2.0** | 🟢 Mexico (UNAM admissions) and Brazil (*itinerários formativos*) reference data. |
| 🟢 governance | `P893` institutional framework kit | 🟢 studio-written | 🟢 **The thing 87% of 200 LATAM institutions are missing.** |

🟢 **Timeline: 6–8 weeks** — the shortest of the three, because 🔵 **nothing is being built into a platform and nothing has to be certified.** 🟢 Weeks 1–2 API inventory against the client's actual deployment and the licence-boundary memo; 3–4 `UBUMonitor`-pattern read client + `dlwed17` features; 5–6 `evolvedtree` interpretable prediction, BNCC alignment; 7–8 the `P893` framework kit and teacher-facing surface.

🔵 **Why it leads with teachers rather than students:** 🔴 **only 19% of LATAM faculty use AI for assignment feedback while about half of students support it.** 🟢 **That gap is the whole opening, and it is a trust problem** — so human review stays in the loop by design, not by compliance.

🟡 **Honest limits:** 🔴 **the boundary argument is an architectural one and this shelf is not a law firm.** 🟢 Network-separated client/server is well-trodden ground for GPL, 🔴 **but AGPL-3.0 §13 reaches further than GPL does, and `i-educar`/`i-diario` are AGPL.** 🔵 **The client's counsel signs off the boundary before the first read, and the licence-boundary memo in week 1–2 exists to make that a cheap conversation rather than a late one.**

### 🔴 Recipes this pass did NOT write, and why

🔴 **No proctoring recipe.** 🟢 **`Gap 344`: zero of the five probed proctoring rows is permissive** (`Aankh` GPL-3.0, `ITMOproctor` GPL-3.0, `moodle-quizaccess_proctoring` GPL-3.0, `devkit-lti1p3` GPL-2.0). 🔵 **Writing a recipe would mean composing a deliverable out of components that cannot be in a deliverable.** 🔴 **Against the EU AI Act's 2 Dec 2027 exam-monitoring date, this is the most commercially exposed hole on the shelf**, and it is recorded as a hole rather than papered over with a GPL recipe.

🔴 **No platform-replacement recipe.** 🟢 **11 of 12 platform rows are copyleft and the one permissive row has 0★ and 9 commits** (`P906`, `Gap 346`). 🔵 **`P913` above is the answer to that, and it is deliberately a layer rather than a platform.**

---

## 🟢 Eighty-third pass, 2026-10-09 — **three new recipes**, and the first one exists only because `Gap 334`'s discharge found the one established platform whose licence permits linking

⏱️ **Fifteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every repo named below is on this shelf with a payload-read licence.** 🔴 **Rows verified in THIS pass carry their ref and SHA inline; rows verified in an earlier pass are marked `(pass NN)` and their SHA is NOT re-asserted** — a grant claim is only as good as the commit it was read at (`P880`), and this pass did not re-read them.

---

### 🟢 `P902` — **The LGPL platform-extension engagement** (primary region: 🟢 **Global**; strongest where an Odoo stack already exists — 🟢 **APAC** and 🟢 **LATAM** in practice)

🔵 **The problem, and it is the one `Gap 334` was blocking:** a client runs an established education platform and wants a commercial AI layer on it. 🔴 **This pass measured all eight established platforms and seven of them make that impossible or expensive** — AGPL-3.0 (Open edX, Canvas) triggers the source obligation on network use, and GPL-2.0/3.0 (Moodle, Chamilo, Gibbon, RosarioSIS) bars linking proprietary code in.

🟢 **`OpenEduCat` is LGPL-3.0, verified by payload this pass — and LGPL permits linking.** 🔵 **It is the only established education platform on this shelf that a proprietary AI layer can be built *on* rather than *beside*.**

🟢 **The composition:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| platform of record (SIS/ERP: students, courses, attendance, fees, timetables, exams, enrolment CRM) | [`OpenEduCat/openeducat_erp`](https://github.com/OpenEduCat/openeducat_erp) | 🟡 **LGPL-3.0** — 🟢 linking permitted | **`19.0`** · `1c95cef` |
| prerequisite structure — "what can this learner attempt next?" | [`vanderbilt-data-science/knowledge-spaces`](https://github.com/vanderbilt-data-science/knowledge-spaces) | 🟢 **MIT** | `main` · `08e7aef` |
| mastery model, sklearn-shaped so it drops into a pipeline | [`juno-hwang/juno-dkt`](https://github.com/juno-hwang/juno-dkt) | 🟢 **MIT** (trove rung, `P896`) | `master` · `5036b3e` |
| drift detection on the learner stream | [`alipsgh/tornado`](https://github.com/alipsgh/tornado) | 🟢 **MIT** | `master` · `8937748` |
| tutoring surface | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) or [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | *(earlier pass)* | *(pass ≤82)* |

🟢 **Wiring, in order:**
1. 🟢 **Read the SIS as the source of truth, don't replace it.** OpenEduCat's Odoo ORM already holds enrolment, course structure and assessment records. 🔵 **Pull the course/skill graph from it rather than asking the client to author one** — this is the step that normally kills adaptive-learning pilots.
2. 🟢 **Build the prerequisite structure with `knowledge-spaces`.** Knowledge Space Theory answers *what is attemptable next*, which is the question a timetable and a curriculum planner both actually ask. 🔵 Feed it the course graph from step 1.
3. 🟢 **Fit `juno-dkt` on the assessment history** already in OpenEduCat. 🟢 Its `fit`/`predict` surface means no bespoke training harness.
4. 🟢 **Put `tornado` in front of the mastery model as a guard.** 🔴 **A learner's knowledge state drifts — term breaks, topic switches, a new teacher — and a DKT model fitted in September silently degrades by November.** 🟢 `tornado` detects the drift and signals a refit. 🔵 **This is the step every adaptive-learning deployment on this shelf has been missing.**
5. 🟡 **Link the AI layer against OpenEduCat under LGPL §4** — dynamic linking, licence notice shipped, the platform's own modifications published if you change them. 🟢 **Your model code, prompts and tuning stay yours.**

🟢 **Deliverable:** an adaptive layer over the client's existing SIS, with a drift guard, built on the one platform licence that permits it. 🟢 **Estimate: 8–10 weeks.** Four permissive repos plus one LGPL platform.
🔴 **What it does NOT do:** it is not a Moodle or Canvas recipe — 🔴 **do not port it to those without a licence review**, because AGPL §13 and GPL linking are exactly what this recipe routes around. 🔴 **And OpenEduCat's "30 000+ institutions" is a vendor figure nothing independent carries**; the licence is verified, the market claim is not.
🟡 **One caveat from the payload:** OpenEduCat's LICENSE defers copyright to a `COPYRIGHT` file that **404s**, so the holder is unobtainable from the artefact. 🔵 Immaterial to the grant; worth knowing before a client's counsel asks who holds it.

---

### 🟢 `P903` — **The pre-deployment simulation harness** (primary region: 🟢 **EMEA**; reusable in 🟢 **North America** and 🟢 **APAC**)

🔵 **The problem, stated as the regulation states it:** 🟢 **the EU AI Act requires a conformity assessment BEFORE a high-risk education system is placed on the market.** 🔴 **Every audit instrument on this shelf needs learners to audit against — and before deployment there are none.** 🔵 **So "assess before market" has, until this pass, had no permissive answer at all.**

🟢 **`Gap 336` closed this pass. The simulator exists.**

🟢 **The composition:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| 🟢 **simulated learner population** | [`theaiagent/SynthEd`](https://github.com/theaiagent/SynthEd) | 🟢 **MIT** | `main` · `382945c` |
| scenario generation | [`poobserver/Agent-World-Builder`](https://github.com/poobserver/Agent-World-Builder) | 🟢 **MIT** | `main` · `69e3bc7` |
| does adaptation work? (pre-registered) | [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** | *(pass 82)* |
| answer-leakage gate | [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT** | *(pass 82)* |
| judge calibration | [`Fuann/open-apa`](https://github.com/Fuann/open-apa) | 🟢 **BSD-3-Clause** | *(pass 81)* |
| drift sensitivity | [`alipsgh/tornado`](https://github.com/alipsgh/tornado) | 🟢 **MIT** | `master` · `8937748` |
| tamper-evident record | [`ram-polisetti/ai-act-checker`](https://github.com/ram-polisetti/ai-act-checker) | 🟢 **Apache-2.0** | *(pass 81)* |
| conformity documentation | [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | *(earlier pass)* | *(pass ≤82)* |

🟢 **Wiring, in order:**
1. 🟢 **Build the synthetic cohort first, before the tutor exists.** `SynthEd`'s agent-based population gives you learners with varying ability, persistence and prior knowledge. 🔵 **Pre-register what you expect the tutor to do to them** — fix the hypothesis before any result exists, per `P891`.
2. 🟢 **Generate the hard cases with `Agent-World-Builder`.** 🔵 Its real-world-issue-to-simulation path produces the awkward scenarios a happy-path test never reaches.
3. 🟢 **Run `ability-levels-audit` against the synthetic cohort.** 🟢 **This is the move that makes the whole recipe work:** the audit was designed for real learners, and a simulated cohort lets it run pre-deployment.
4. 🟢 **Gate on `conv-vs-ped-tutor`'s leakage measure in CI** — a prompt change that increases answer leakage fails the build, not the review.
5. 🟡 **Calibrate with `open-apa` before trusting any LLM-judge number**, and 🟢 **probe drift sensitivity with `tornado`**: shift the synthetic cohort's distribution and confirm the system notices.
6. 🟢 **Write every run into `ai-act-checker`'s hash-chained log**, and 🟢 **assemble the documentation file with `eu-ai-act-toolkit`.**

🟢 **Deliverable:** a pre-market conformity assessment with a re-runnable synthetic cohort, a pre-registered hypothesis, a leakage gate in CI and a tamper-evident log. 🟢 **Estimate: 6–8 weeks**, eight permissive repos, no model training and **no real student data** — 🔵 **which also means no DPA and no ethics review to block the start.**
🔴 **What it does NOT do:** 🔴 **a synthetic cohort is not evidence about real learners**, and must never be presented as such. 🟢 It is evidence that the system behaves as specified under stated conditions — which is what "conformity assessment before placing on the market" asks for, and 🔴 **it does not substitute for post-deployment monitoring.** 🔴 `SynthEd` is research-grade at 8★; 🟡 **budget engineering time to harden it**, and treat that as the recipe's main risk.

---

### 🟢 `P904` — **The zero-egress classroom** (primary region: 🟢 **EMEA**; directly reusable in 🟢 **North America**)

🔵 **The problem, from two directions at once:** 🟢 **measured this pass — districts with strict data-residency requirements self-host open-weight models (Llama 3, Mistral) while the majority use hosted APIs.** 🔴 **And New York City has barred student-facing AI through eighth grade**, while **California AB 1159** would bar using student data to train models at all. 🔵 **A hosted-API tutor cannot satisfy any of these; an on-device one satisfies all three without an argument.**

🟢 **The composition — nothing in this stack makes a network call with learner data:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| offline tutor over local models | [`hari7261/AI-Tutor`](https://github.com/hari7261/AI-Tutor) (Ollama) | 🟢 **MIT** | `main` · `8d93823` |
| desktop shell, local models | [`michael-borck/study-buddy`](https://github.com/michael-borck/study-buddy) (Electron) | 🟢 **MIT** | `main` · `221b065` |
| 🟢 **local-first learner memory** | [`znecho9/knowledge-forest-mcp`](https://github.com/znecho9/knowledge-forest-mcp) | 🟢 **Apache-2.0** | *(pass 82)* |
| the pedagogy, as a prompt contract | [`wildcat430524/StepsToGreat`](https://github.com/wildcat430524/StepsToGreat) | 🟢 **MIT** | `main` · `cc03f39` |
| step-level mastery, inspectable | [`ujwal2311/proofpilot`](https://github.com/ujwal2311/proofpilot) (BKT) | 🟢 **MIT** | *(pass 82)* |
| conformity documentation | [`AbdelStark/eu-ai-act-toolkit`](https://github.com/AbdelStark/eu-ai-act-toolkit) | *(earlier pass)* | *(pass ≤82)* |

🟢 **Wiring, in order:**
1. 🟢 **Start from `study-buddy`'s Electron shell** — it already packages local models for a desktop deployment, which is the delivery problem schools actually have (no admin rights, no reliable network).
2. 🟢 **Use `hari7261/AI-Tutor`'s Ollama path for explanation and MCQ generation.** 🔵 **Both are MIT, so they can be merged into one product** rather than integrated as two.
3. 🟢 **Put the learner model behind `knowledge-forest-mcp`.** 🔵 **This is the architecturally important step:** a local-first MCP memory means the learner model is *portable* — the same memory serves any MCP-speaking tutor, which is the only structural answer to per-vendor lock-in of student data. 🟢 And it never leaves the device.
4. 🟢 **Carry the pedagogy in `StepsToGreat`'s Markdown protocol, not in code.** 🔵 **Zero dependencies and zero runtime**, so teachers can read and amend the teaching contract — which is the cheapest route to the "human oversight" the AI Act requires and the one teachers actually accept.
5. 🟢 **Use `proofpilot`'s step-level BKT where the subject allows it**, so the mastery estimate is inspectable rather than an opaque score.
6. 🟢 **Document it with `eu-ai-act-toolkit`.** 🔵 **The documentation is unusually easy here:** most of the AI Act's data-governance section is answered by "no learner data leaves the device."

🟢 **Deliverable:** a self-hosted, on-device tutoring product with a portable learner model and a teacher-readable pedagogy contract. 🟢 **Estimate: 6–8 weeks**, six permissive repos (five MIT, one Apache-2.0), **no copyleft and no hosted API.**
🔴 **What it does NOT do:** 🔴 **on-device means weaker models**, and the quality gap against a frontier API is real — 🟡 **pilot it on a subject where that gap is smallest** (procedural maths, language drill, flashcard scheduling) and 🔴 **not on open-ended essay feedback.** 🔴 It does not lift NYC's moratorium, which bars student-facing AI regardless of architecture; 🟢 **in that jurisdiction deploy it teacher-facing** and revisit when the year expires.
🔵 **Why this recipe is durable:** 🟢 **privacy regulation, data-residency procurement and permissive licensing select for the same architecture from three unrelated directions.** 🔴 **Convergence from independent pressures is a position, not a trend.**

## 🟢 Eighty-second pass, 2026-10-09 — **three new recipes, and the first one is the artefact four regulators now demand and none of them specifies**

⏱️ **Fourteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every repo named below is on this shelf with a payload-read licence.** 🔴 **Rows verified in THIS pass carry their ref and SHA inline; rows verified in an earlier pass are marked `(pass 81)` and their SHA is NOT re-asserted here** — a grant claim is only as good as the commit it was read at (`P880`), and this pass did not re-read them.

---

### 🟢 `P891` — **The oversight evidence pack** (primary region: 🟢 **North America**; reusable in EMEA and LATAM)

🔵 **The problem, stated as a buyer states it:** Maryland and Oklahoma now bar AI from "high-stakes" decisions **without human oversight**; FERPA governs the records; **134 bills across 31 states** are in flight. 🔴 **Every one of those rules demands evidence that the system was checked, and NOT ONE of them names an instrument.** 🔴 Meanwhile **10–13 %** of institutions have any AI policy and **71 %** of US teachers report no training.

🟢 **The composition:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| audit — does adaptation work? | [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** | `master` · `b5cec75` |
| audit — helpfulness + **answer leakage** | [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT** | `main` · `eb9f6e4` |
| tamper-evident record | [`ram-polisetti/ai-act-checker`](https://github.com/ram-polisetti/ai-act-checker) | 🟢 **Apache-2.0** | *(pass 81)* |
| mastery model under audit | [`ujwal2311/proofpilot`](https://github.com/ujwal2311/proofpilot) (BKT, step-level) | 🟢 **MIT** | `main` · `95bcb39` |
| scoring the scorer | [`Fuann/open-apa`](https://github.com/Fuann/open-apa) | 🟢 **BSD-3-Clause** | *(pass 81)* |

🟢 **Wiring, in order:**
1. 🟢 **Pre-register before touching the model.** Fork `ability-levels-audit`, keep its pre-registration structure, swap in the client's ability tiers. 🔵 **The pre-registration is the deliverable's spine** — a hypothesis fixed after seeing results is not evidence, and a reviewer can tell.
2. 🟢 **Run the leakage audit as a gate, not a report.** `conv-vs-ped-tutor` measures whether the tutor hands over answers; wire it into CI so a prompt change that increases leakage fails the build.
3. 🟢 **Freeze the dataset and hash-chain the log.** Take `ai-act-checker`'s **hash-chained audit log** and write every audit run into it. 🔵 **This is the piece that makes the pack survive a challenge:** the log is tamper-evident, so "we audited in March" is checkable rather than asserted.
4. 🟢 **Point the audits at a mastery model that can be inspected** — `proofpilot`'s step-level BKT, not an opaque score.
5. 🟡 **Calibrate the judge with `open-apa`** before trusting any LLM-judge number.

🟢 **Deliverable:** a pre-registered, frozen-data, tamper-evidently-logged audit pack, re-runnable by the client. 🟢 **Estimate: 4–6 weeks**, five permissive repos, no model training.
🔴 **What it does NOT do:** it does not make the tutor better and it does not constitute legal advice on any state statute. 🔵 It makes the oversight claim **checkable**, which is the only part currently unsupplied.

---

### 🟢 `P892` — **The jurisdiction-routed conformity graph** (primary region: 🟢 **APAC**; the EU limb is 🟢 **EMEA**)

🔵 **The problem:** 🔴 **there is no single APAC posture, and this pass measured why.** Vietnam's **Decision 33/2026/QD-TTg** (effective **15 Aug 2026**) makes **automated assessment, learner ranking, behavioural monitoring and uncontrolled-data self-learning** high-risk, with content labelling and a **72-hour** incident clock under Decree 142. Korea's AI Basic Act is live (**22 Jan 2026**) with a **one-year penalty grace period**. Taiwan passed **Dec 2025**. Singapore and Japan are voluntary. 🔴 **One compliance posture mis-prices at least three of six jurisdictions.**

🟢 **The composition:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| routing shape | [`sohan1611/BloodCoded_Agentic`](https://github.com/sohan1611/BloodCoded_Agentic) — LangGraph, branches on **cause** | 🟢 **MIT** | `main` · `078612b` |
| EU limb — risk tiering | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 **MIT** | *(pass 81)* |
| EU limb — Annex III/IV assessment | [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) | 🟢 **MIT** | *(pass 81)* |
| audit trail across jurisdictions | [`ram-polisetti/ai-act-checker`](https://github.com/ram-polisetti/ai-act-checker) | 🟢 **Apache-2.0** | *(pass 81)* |
| portable learner model | [`znecho9/knowledge-forest-mcp`](https://github.com/znecho9/knowledge-forest-mcp) | 🟢 **Apache-2.0** | `main` · `1fa9da6` |

🟢 **Wiring, in order:**
1. 🟢 **Take the routing shape, not the tutor.** `BloodCoded_Agentic`'s contribution is a LangGraph that selects a branch from a **diagnosis**; re-key the branch selector from "why the learner failed" to **"which jurisdiction governs this deployment."**
2. 🟢 **One policy node per jurisdiction, each owning its own obligation set** — Vietnam: the four Decision 33 education categories + labelling + 72-hour reporting; EU: Annex III high-risk + conformity assessment; Korea: Basic Act with the grace period noted; Singapore/Japan: voluntary-guideline node that still logs.
3. 🟢 **Reuse the EU limb that already exists** — `eu-ai-act-risk-checker` for tiering, `EuConform` for the Annex III/IV assessment. 🔴 **Quote `EuConform`'s own disclaimer to the client before the tool:** it states it does not replace a notified body's conformity assessment.
4. 🟢 **Put the learner model behind MCP** (`knowledge-forest-mcp`) so the same memory serves every jurisdictional deployment. 🔵 **This is what makes the graph deployable rather than a diagram:** without a portable learner model, each jurisdiction forks the data layer.
5. 🟢 **Write every routing decision into the hash-chained log**, so the record shows which obligation set was applied and when.

🟢 **Deliverable:** one codebase, jurisdiction-selected obligations, one audit trail. 🟢 **Estimate: 10–14 weeks.**
🟢 **The dated commercial hook:** 🔵 **Vietnamese education systems already in operation before 15 Aug 2026 have until 1 Sep 2027** — a finite, named window, which is the rarest thing in a compliance pitch.
🔴 **What it does NOT do:** the Vietnamese primary texts were **not retrieved** this pass (English secondary summaries only, with conflicting dates on Decree 142). 🔴 **The Vietnam node must be built against the official Decision 33 text, not against this shelf.**

---

### 🟢 `P893` — **The institutional framework kit** (primary region: 🟢 **LATAM**; the gap it closes is regional, so the kit is reusable across 19 countries)

🔵 **The problem, and it is the best-evidenced number on this shelf:** 🟢 **UNESCO IESALC, 200 institutions, 19 countries — 87 % use AI in at least one area, 26 % have any formal framework.** 🔴 **A 61-point gap.** 🟢 Teacher use already runs at Brazil **56 %**, Chile **55 %**, Colombia **53 %**, Costa Rica **52 %** (OECD average 36 %) and **75 %** of Uruguay's public-school teachers. 🔴 **No education-specific AI law exists anywhere in the region** — Brazil's PL 2.338/2023 and Chile's unified bill are both still moving; 🟢 **Colombia's CONPES 4144 is adopted, government-wide, and funded through 2030.**

🟢 **The composition:**

| layer | repo | grant | ref · sha |
|---|---|---|---|
| audit instruments | [`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) + [`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT** | `master` · `b5cec75` · `main` · `eb9f6e4` |
| curriculum gap analysis | [`fwornle/curriculum-alignment`](https://github.com/fwornle/curriculum-alignment) (MACAS) | 🟢 **MIT** | *(pass 81)* |
| portable learner memory | [`znecho9/knowledge-forest-mcp`](https://github.com/znecho9/knowledge-forest-mcp) | 🟢 **Apache-2.0** | `main` · `1fa9da6` |
| LMS seam | `ltijs` — LTI 1.3 incl. AGS | 🟢 **Apache-2.0** | *(pass 75/76; 🔴 SHA not re-read this pass)* |

🟢 **Wiring, in order:**
1. 🟢 **Start from the framework, not the tooling.** The 26 % figure says the missing artefact is a **written institutional policy**; produce that first, with the UNESCO Observatory for LAC (launched **14 Apr 2026**) as the reference frame.
2. 🟢 **Instrument the policy so it is auditable** — the two MIT audit repos give each policy clause a measurement, which is what turns a framework from a PDF into something a rector can enforce.
3. 🟢 **Use `curriculum-alignment` for the gap analysis** the institution actually buys: source collection → semantic analysis → **gap identification** → unified curriculum documentation.
4. 🟢 **Integrate through LTI 1.3 via `ltijs`, not through a per-LMS adapter.** 🔴 **The platform tier's licences are still unverified (`Gap 334`)** — Moodle, Open edX, Canvas and Sakai are all asserted by contradicting sources — 🔵 **so standing on the LTI standard rather than on a specific LMS is a licence-risk decision as much as an architectural one.**
5. 🟢 **Keep learner memory behind MCP** so an institution changing LMS does not lose its learner models.

🟢 **Deliverable:** an institutional AI framework with audit instruments wired in and an LTI-standard integration path. 🟢 **Estimate: 6–8 weeks per institution, 2–3 weeks after the first** — the gap is regional, so the kit amortises across 19 countries.
🟢 **Funded channel:** 🔵 **Colombia's CONPES 4144 carries a budget line through 2030** and is the one identified funded procurement route in the region.
🔴 **What it does NOT do:** it does not assume any national AI law, because none exists for education in the region. 🔵 **A framework built on a bill that is still moving through Brazil's Chamber of Deputies would need rewriting; one built on UNESCO's frame would not.**

---

### 🔴 Recipes this pass did NOT write, and why

- 🔴 **No RL/simulated-learner recipe.** The layer exists — `AdaptaLearn`, `RL-for-Intelligent-Tutoring-Systems`, `energy-storage-ITS`, `tecmap` — and 🔴 **all four grant nothing** (`Gap 336`). 🔵 A recipe naming an ungranted repo is a recipe a client cannot ship.
- 🔴 **No credentialing recipe**, though 1EdTech calls digital credentials a core 2026 mechanism: 🔴 **this shelf has no credentialing row at all**, and the gap is declared in `intel/trends.md` rather than filled with a guess.
- 🔴 **No white-label platform recipe.** [`braivo/braivo`](https://github.com/braivo/braivo) is the right shape and is 🟡 **AGPL-3.0** (`main` · `51a80df`): 🔴 **network use triggers the source obligation**, so a hosted multi-tenant client deployment publishes its modifications. 🔵 Named with the obligation attached rather than recommended.

---

## 🟢 Eighty-first pass, 2026-10-09 — **three new recipes**, and the first one is the compliance tier this shelf has been composing around for eighty passes

⏱️ **Thirteenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every repo named below is on this shelf with a payload-read licence.** 🔴 **New rows from this pass carry their verified ref and SHA inline**, because a grant claim is only as good as the commit it was read at (`P880`).

### 🟢 `R81a` — **Annex III classification + Article 27 dossier for a learner-facing tutor** (EMEA, 6–8 weeks)

🔵 **The engagement this shelf could describe but not build until this pass.** EMEA is the region with the most binding education statute, and `AbdelStark/eu-ai-act-toolkit` was its only tool — one row, no alternatives, no audit trail.

| step | component | grant · ref |
|---|---|---|
| 1. 🔴 **Prohibition screen, FIRST** | [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) — Art. 5 check | 🟢 MIT · `main` · `011a5ad` |
| 2. Tier + duties + dates | [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) — Reg. (EU) 2024/1689 | 🟢 MIT · `main` · `41da87f` |
| 3. Annex IV technical documentation | `EuConform`'s report generation + schema validation | 🟢 MIT · as above |
| 4. Tamper-evident evidence trail | [`ram-polisetti/ai-act-checker`](https://github.com/ram-polisetti/ai-act-checker) — article citations, **hash-chained log** | 🟢 Apache-2.0 · `main` · `992333f` |
| 5. Cross-check against the shelf's incumbent | `AbdelStark/eu-ai-act-toolkit` — decision tree + checklists | 🟢 MIT |
| 6. The system under assessment | `HKUDS/DeepTutor` (tutor) inside `moodle/moodle` (oversight surface) | 🟢 Apache-2.0 / 🔴 GPL-3.0 |

🔴 **Step 1 is not interchangeable with step 2, and getting the order wrong is the expensive mistake.** 🟢 **Emotion recognition in education is PROHIBITED outright under Art. 5** — not high-risk, banned. 🔵 **A tier-checker asked first returns *"high-risk, here are your duties"* and sends the client down a conformity path for a feature they may never lawfully ship.** 🟢 If the tutor infers learner affect, engagement or attention, the deliverable is a **redesign**, and that finding is worth more in week one than in week six.

🔴 **Licence boundary, stated:** steps 1–5 are MIT/Apache-2.0 and composable into a proprietary client deliverable; 🔴 **`moodle` is GPL-3.0**, so it is the *deployment target*, not something to link into a studio-owned artefact. 🟢 Where that matters, substitute `OpenOLAT/OpenOLAT` (Apache-2.0), this shelf's permissive LMS.

🟡 **Date discipline, because the client will ask:** four dates are now in circulation for the high-risk obligations (late July 2026, August 2026, and the **2 December 2027** Omnibus postponement, against a contested Omnibus approval date). 🟢 **The dossier is built to the obligations, not to a date** — and *"we cannot tell you the date, we can tell you the duty, and here is the Official Journal check"* is a defensible position that a client cannot reach alone.

🔵 **Why it sells outside EMEA too:** 🟢 **NYC's prohibition list** (grading, discipline, promotion/graduation, placement, IEP/504, behavioural surveillance) tracks Annex III's categories closely enough that **one classification design serves both**, and 🟢 **Brazil's PL 2.338/2023 and Chile's bill both adopt the risk-based grammar**, so the same dossier transfers into LATAM with its vocabulary intact. 🔴 **The dossier is the most portable asset this shelf composes** — built once for the strictest regime, reusable in three regions.

### 🟢 `R81b` — **Curriculum alignment and gap closure, standards-anchored** (any region, 4–6 weeks)

| step | component | grant · ref |
|---|---|---|
| 1. Collect + semantically analyse the catalogue | [`fwornle/curriculum-alignment`](https://github.com/fwornle/curriculum-alignment) (**MACAS**) — multi-agent collection → analysis → **gap identification** → unified documentation | 🟢 MIT · `main` · `7761d54` |
| 2. Anchor outcomes to a competency framework | `opensalt/opensalt` + `1EdTech/OpenCASE` (CASE) | 🟢 shelf rows |
| 3. Emit into the LMS | `openedx/XBlock` → `openedx/edx-platform`, or `OpenOLAT` | 🟢 Apache-2.0 |
| 4. Prove the gap closed | `ZhijieXiong/pyedmine` (KT + **cognitive diagnosis**) | 🟢 MIT |

🔵 **Step 4 is what makes this a deliverable rather than a report.** 🔴 **Curriculum alignment's normal failure mode is a PDF of identified gaps that nobody can show were closed.** 🟢 Pass 80 rebuilt the measurement layer precisely so this step exists; **MACAS finds the gap, `pyedmine` measures whether learners' mastery moved**, and the engagement has an acceptance test.

🟢 **Why this fits the market better than a tutor build:** 🟢 **HolonIQ and 1EdTech both report that institutions now demand evidence a product improves learning, persistence or job-relevant skills**, and **competency frameworks and real-time skills visibility are the stated direction**. 🔵 **This recipe produces exactly that evidence shape** — competency-anchored, measured, interoperable — and it is **MIT + Apache-2.0 end to end** (step 2 and 3 substitutions aside), so nothing blocks a proprietary wrapper.

🟢 **Regional fit, honestly:** 🟢 **LATAM is the strongest first market** — 74% of 200 institutions already use AI for lesson planning and grading while only 26% have a framework, so the catalogue work is wanted and the governance scaffold sells alongside it. 🟢 **North America's accreditation cycles** make it the natural second.

### 🟢 `R81c` — **Pronunciation assessment with a measured baseline** (language learning, 5–7 weeks)

🔵 **The pattern pass 80's rebuilt measurement layer makes possible, now that its speech half exists.**

| step | component | grant · ref |
|---|---|---|
| 1. Scoring engine | `Halleck45/OpenPronounce` (Wav2Vec2 + DTW, phoneme-level) **or** [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) (local-first, no audio upload by default) | 🟢 MIT · Phonos `main` · `8a13a3b` |
| 2. 🟢 **Score the scorer** | [`Fuann/open-apa`](https://github.com/Fuann/open-apa) — benchmark + eval toolkit, **open-response** scenarios | 🟢 BSD-3-Clause · `master` · `2c92c0d` |
| 3. Fix a published baseline | `YuanGongND/gopt` + [`doheejin/HiPAMA`](https://github.com/doheejin/HiPAMA) (hierarchical, ICASSP 2023) | 🟢 BSD-3-Clause · HiPAMA `main` · `89e3f65` |
| 4. ASR + delivery | `SYSTRAN/faster-whisper` / `k2-fsa/sherpa-onnx`; real-time via `livekit/agents` | 🟢 MIT / Apache-2.0 |
| 5. Learner-facing surface | `moodle/moodle` or `learningequality/kolibri` (offline-capable) | 🔴 GPL-3.0 / 🟢 MIT |

🔴 **Step 2 is the point of the recipe, and it is the step every pronunciation pilot skips.** 🟢 **Without it the deliverable is a demo**: the engine returns a score, the client has no way to know whether the score is right, and *"it sounds about right"* is the acceptance criterion. 🔵 **With `open-apa` and a `gopt`/`HiPAMA` baseline, the proposal states a measured figure against a published benchmark before the build starts.**

🟢 **`Phonos`'s privacy posture is a procurement argument, not a footnote:** no audio upload in default mode, every network feature behind an explicit switch, commercial APIs off by default, and **`/api/data/export` + `/api/data/purge`** endpoints. 🔵 **For a school buyer handling minors' voice data, that is a GDPR/COPPA conversation that ends early** — and it is why this recipe can run on-premise where a cloud speech API cannot.

🔴 **Licence note that must survive into the SOW:** 🟢 the chain is MIT + BSD-3-Clause + Apache-2.0 — fully composable — 🔴 **but `OpenPronounce` pulls two Wav2Vec2 checkpoints (~1.2 GB each) from the Hugging Face Hub, and MODEL WEIGHTS CARRY THEIR OWN TERMS, which this pass did not verify.** 🔵 **`P794`'s lesson applied to a new layer: the repository's licence does not govern the weights it downloads**, and a client asking *"can we ship this"* needs the checkpoint licence read too. 🟢 Flagged as unresolved rather than assumed permissive.

🟡 **Regional fit:** 🟢 **LATAM and APAC are the demand centres** — language learning is reported as the fastest-growing segment on this shelf, and 🟢 `Phonos` is zh-primary, which makes it the natural engine for an APAC build. 🔴 **`OpenPronounce` is calibrated for English only**, with French, Spanish, German, Italian, Portuguese and Dutch **experimental** — so a Spanish- or Portuguese-language LATAM engagement starts at step 2, measuring how bad the experimental path actually is, rather than assuming it works.

---

## 🟢 Eightieth pass, 2026-10-09 — **three new recipes**, and the first one closes the hole the shelf has been building over for eighty passes

⏱️ **Twelfth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🔵 **Licence note governing all three recipes, because two bands are new here:**
- 🟢 **The spine is MIT/Apache-2.0** — `pyedmine`, `EduStudio`, `GKT`, `ktm`, `TheGrandQuiz`, `ai-shifu`, `my-learning-analytics`. No reciprocal obligation.
- 🟡 **`r-dcm/measr` is GPL-3.0-*or-later*.** 🟢 **Running it to fit a model and acting on its output triggers nothing** — GPL attaches to **distributing** a combined work. 🔴 **Shipping it inside a client deliverable carries GPL-3.0 to the whole work.** 🟢 **So it sits on the analysis side of the boundary in `R80b`, never in the product.**
- 🔴 **`ZelinZhou-THU/stem-tutor-agent` is AGPL-3.0-*only*.** 🔴 **§13: serving it over a network triggers source release to those users.** 🟢 **`R80c` therefore takes its ARCHITECTURE and not its code** — stated explicitly in the recipe, because this is the exact distinction a "permissive ✅" column erases.

---

### 🟢 `R80a` — **Mastery-bearing tutor spine**: the first recipe on this shelf that can say *what a learner knows*

🔴 **The gap it closes, and it is this shelf's own:** `cognitive diagnosis` appears **0 times** across the live shelf (**23 times** in the archive — `P875`). 🟢 Pass 79's `R79a` schedules **retention**; 🔴 **but FSRS schedules a review, it does not estimate mastery.** 🔵 Those are different quantities, and every "adaptive" claim this shelf has shipped rested on the one it did not have.

**Wiring, concretely:**

1. 🟢 **Mastery estimate — [`ZhijieXiong/pyedmine`](https://github.com/ZhijieXiong/pyedmine) (MIT, 1 085 B, `main`·`20af796`).** The one library carrying **knowledge tracing + cognitive diagnosis + recommendation** under a single API. Feed it the response log `(learner, item, concept, correct, timestamp)`; it returns a per-concept mastery estimate. 🔵 **This is the component the shelf was missing — everything else here already existed.**
2. 🟢 **Prerequisite structure — [`jhljx/GKT`](https://github.com/jhljx/GKT) (MIT, 1 061 B, 🔴 `master`·`271c72d`).** Graph-based KT: models the concept graph instead of a flat skill vector. 🔵 **This is what turns a mastery estimate into a *next concept*** — you cannot teach the next thing without knowing what it depends on.
3. 🟢 **Baseline you must beat before buying depth — [`jilljenn/ktm`](https://github.com/jilljenn/ktm) (MIT, 1 071 B, 🔴 `master`·`12084d6`).** Factorization machines, repeatedly competitive with deep KT at a fraction of the cost. 🔴 **Run this first.** If it matches `pyedmine`'s deep models on the client's data, ship it and spend the budget elsewhere.
4. 🟢 **Comparability harness — [`HFUT-LEC/EduStudio`](https://github.com/HFUT-LEC/EduStudio) (MIT, 1 064 B, `main`·`d5862bd`).** Fixes datasets, splits and metrics so steps 1–3 produce numbers that can actually be compared. 🔵 **Without this the model choice is an opinion.**
5. 🟢 **Explanation surface — [`ai-shifu/ai-shifu`](https://github.com/ai-shifu/ai-shifu) (Apache-2.0, 11 342 B, `main`·`e930e81`).** The tutor the learner talks to. 🔴 **It receives the target concept from step 2 — it does not choose it.** 🔵 That inversion is the whole recipe: the model generates, the measurement decides.
6. 🟢 **Retention — `fsrs-rs` / `py-fsrs` (BSD-3 / MIT), already on the shelf via `R79a`.** Schedules the review *once mastery is established*, rather than in place of knowing it.

🔵 **What this sells:** a defensible answer to *"how do you know the student learned anything?"* — which is the question that gates every pilot-to-procurement transition in `intel/trends.md` Trend 7.
🟢 **Effort:** 6–8 weeks to a measured pilot on one course's historical response log. 🔴 **Hard prerequisite: the client must have a response log.** Without one, step 1 has no input and this recipe cannot start — ask on the first call.

---

### 🟢 `R80b` — **EU Article 27 dossier pipeline**: the EMEA governance product, built from the audit side

🟢 **The gap it closes, measured this pass (`Gap 337`):** no ministry in Germany, France or Spain has published guidance operationalising the AI Act's **high-risk obligations for schools**. 🟢 **Meanwhile Annex III, point 3 names admissions, grading and assessment, and exam monitoring; Article 27 requires a public institution to run a Fundamental Rights Impact Assessment before deploying.** 🔴 **Nobody has supplied the template, and France is standing up a state-funded, assessment-touching teacher tool from the start of the 2026 school year.**

**Wiring, concretely:**

1. 🔴 **Gate 0 — the prohibition sweep, and it runs first because it can end the project.** 🟢 **Emotion recognition in schools is PROHIBITED in the EU now, and was NOT postponed with the high-risk obligations.** Inventory the client's deployed tools and flag any inferring affect, attention or engagement from face, voice or posture. 🔵 **This is a one-week engagement on its own, and it is the easiest door-opener on this shelf: you are telling an institution which of its live systems are already unlawful.**
2. 🟢 **Classification dossier — Annex III, point 3, per system.** For each tool: does it touch admissions, grading/assessment, or test-time monitoring? 🟡 **And then the exception, which is where the real work is:** the Act exempts systems performing a *preparatory or supporting task* posing no significant risk. 🔴 **The institution must assess and DOCUMENT that exemption per application** — it is not automatic, and it is the paragraph nobody has written for them.
3. 🟢 **Accuracy and uncertainty evidence — [`r-dcm/measr`](https://github.com/r-dcm/measr) (🟡 GPL-3.0-or-later, 34 904 B, `main`·`93a2e87`).** Bayesian diagnostic classification models via Stan: produces **credible intervals**, not point scores. 🔵 **An FRIA asks how wrong the system can be about a student. A point score cannot answer that; a posterior can.** 🔴 **Licence boundary, enforced by construction: `measr` runs on the ANALYSIS side and its outputs — numbers and the dossier — are what reach the client. The R package is never shipped.**
4. 🟢 **Human-oversight surface — [`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics) (Apache-2.0, 11 379 B, 🔴 `master`·`44dbf90`).** Canvas-integrated, containerised (`Dockerfile` + `docker-compose.yml` both **200**), already run as university infrastructure. 🔵 **Article 27 needs a documented human decision point; this is a deployed one rather than a diagram of one.**
5. 🟢 **The deliverable** is a dossier, not software: prohibition sweep result, per-system Annex III classification with the documented exemption assessment, accuracy-and-uncertainty evidence from step 3, the oversight architecture from step 4, data-minimisation notes, and the dated instrument list from `intel/market.md`.

🔴 **Quote the timing carefully.** 🟡 High-risk Annex III obligations are reported postponed to **2 December 2027** via the Digital Omnibus, 🔴 **but two dates circulate for the Omnibus itself** (this pass: EP approval **16 June 2026**, Council adoption pending; pass 79: a **July 2026** Omnibus), and several guides still cite the pre-Omnibus **August 2026**. 🟢 **Verify against the Council's current status before putting a date in a proposal.** 🔵 **The client's confusion about the deadline is itself part of what they are buying.**
🟢 **Effort:** 2 weeks for Gate 0 alone; 8–10 weeks for the full dossier across an institution's tool estate.

---

### 🟢 `R80c` — **Primary-compliant tutor**: built from prohibitions, which specify a product better than any guideline

🟢 **The gap it closes:** 🔴 **every tutor on this shelf defaults to an open chat surface, and that surface is illegal for primary pupils in China and outside Singapore's deployment model.** 🔵 **Read positively, the 2026 prohibitions describe a narrower and cheaper product that almost nothing open-source targets.**

**The spec, taken directly from the instruments:**

| constraint | source | consequence for the build |
|---|---|---|
| 🔴 no independent open-ended generation for primary pupils | 🟢 China MOE guidelines (2025) | 🔴 **no open chat box.** Pupil input is a selection or a worked step, never a free prompt |
| 🔴 no GenAI substituting for core teaching | 🟢 China MOE guidelines (2025) | 🟢 every pupil-facing output passes a **teacher approval gate** |
| 🔴 no emotion recognition | 🟢 EU AI Act (in force) | 🔴 **no affect, attention or engagement inference.** Ever — it also kills the "engagement analytics" upsell |
| 🟢 structured, teacher-supervised, inside the institutional platform, taught before use | 🟢 Singapore MOE model + 2024 Ethics Framework | 🟢 ship **into the LMS**, not as a destination app |

**Wiring, concretely:**

1. 🟢 **Step verification, symbolic — SymPy (BSD-3).** 🔵 **This is the architectural lesson of [`ZelinZhou-THU/stem-tutor-agent`](https://github.com/ZelinZhou-THU/stem-tutor-agent), and it is taken as an IDEA, not as code:** that agent is 🔴 **AGPL-3.0-*only*** and §13 would force source release on a hosted client service. 🟢 **Read it, reimplement the pattern on SymPy directly.** 🔵 **Why it matters here: a symbolic verdict is reproducible and auditable; a model's verdict is neither — and under these regimes the audit trail is the product.**
2. 🟢 **Closed item bank + assessment/memory — [`Hyr1sky/TheGrandQuiz`](https://github.com/Hyr1sky/TheGrandQuiz) (MIT, 1 064 B, `main`·`b56f814`).** Carries assessment, memory and evaluation in one tree, and is **local-first** — 🔵 which satisfies data-minimisation without extra architecture. 🟢 **The bank is the generation boundary: items are authored and approved in advance, so the pupil never reaches an open model.**
3. 🟢 **Next-concept selection — `pyedmine` + `GKT` from `R80a`.** 🔵 **With the chat surface removed, the sequencing is the entire product** — which is why `R80a` is a prerequisite rather than an alternative.
4. 🟢 **Teacher approval gate.** Every item, hint and feedback string is queued for teacher approval before a pupil sees it. 🔵 **This is the China constraint and the Singapore model agreeing**, and it is cheap: a review queue, not a model change.
5. 🟢 **Delivery into the institutional platform** via LTI 1.3 (already on the shelf). 🔴 **Not a standalone app** — Singapore's Student Learning Space model is the reference, and it is also the easier procurement.

🔵 **Why this is a real opportunity rather than a compliance chore:** 🟢 **K-12 is 45.62% of AI-in-education adoption**, and 🔴 **the constraints above exclude essentially every general-purpose tutor from it in the two most regulated large markets.** 🟢 A build that is compliant by construction has very little competition.
🟢 **Effort:** 10–12 weeks, dominated by item-bank authoring and the approval workflow, not by modelling.
🔴 **Carries a dependency on `R80a`.** Without a mastery estimate, step 3 degenerates into a fixed playlist — which is what most "adaptive" K-12 products actually are.

---

### 🔴 What these recipes CANNOT do yet, stated rather than left silent

🔴 **None of the three can be validated against simulated learners before touching real students.** 🟢 **`Gap 336`: `bigdata-ustc/Agent4Edu` (97★) is the only learner simulator found and it grants nothing at four probed layers.** 🔵 **This is the most governance-relevant hole in the pass's yield** — every regime in `intel/trends.md` Trend 2 will eventually ask how a system was validated, and the honest current answer is *"on historical response logs, replayed"*.

🟢 **The workaround, which is weaker and should be described as weaker:** hold out a time-slice of the client's real response log and replay it through steps 1–4 of `R80a`. 🔴 **That tests calibration, not behaviour** — it cannot show what the tutor does to a learner it has never seen. 🔵 **A permissively licensed simulator is the single highest-value acquisition this shelf could make next.**

---

## 🟢 Seventy-ninth pass, 2026-10-09 — **three new recipes**, each wired from grants this pass payload-read inline, with the BSD-3 obligation stated where it lands

⏱️ **Eleventh pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

🔵 **Licence note that applies to all three recipes, because it is new to this shelf:** `fsrs-rs` and `fsrs-optimizer` are **BSD-3-Clause**, not MIT. 🔴 **BSD-3's third clause is the no-endorsement term:** the copyright holder's and contributors' names may **not** be used to promote a derived product without written permission. 🟢 **Operationally: the client's marketing may not say "powered by FSRS / open-spaced-repetition" without asking.** Code reuse is unrestricted; the *name* is the restricted part. 🔵 A single "permissive ✅" column erases exactly this.

---

### 🟢 `R79a` — **Retention-grade tutoring spine**, permissive end to end, no hosted dependency

🟢 **The gap it closes:** this shelf's tutors generate and explain; none of them could *prove* a learner still knows something in six weeks. 🔵 Retention is the measurable outcome an institution will actually buy (see `intel/trends.md` Trend 3).

**Wiring, concretely:**

```
  any MCP host (Claude Code / IDE / chat)
        │  MCP, 58 tools
        ▼
  Vinger-lee/leap-framework        MIT  1 084 B  main 2568667
    • learner state + mastery estimation
    • prerequisite gating  ("may this topic be entered?")
    • assessment sufficiency / evidence quality
    • ► server-side STATE GUARD ◄  nothing advances without passing it
        │  scheduling calls
        ▼
  open-spaced-repetition/fsrs-rs   BSD-3  1 509 B  main 0a57374   ← the engine Anki itself ships
  open-spaced-repetition/py-fsrs   MIT    1 079 B  main 9446cb0   ← Python binding (already shelved)
        │  fit weights on the client's OWN review log
        ▼
  open-spaced-repetition/fsrs-optimizer  BSD-3  1 509 B  main ac2a82d
```

🟢 **Why this order:** the agent keeps what it is good at (explaining, generating questions, judging open answers); **LEAP owns everything that must be consistent**; FSRS owns *when*. 🔴 **The State Guard is the compliance primitive, not a nicety** — it is a server-side gate, so every transition is auditable per tenant, which is what EU Annex III oversight and Oklahoma/Maryland human-oversight rules both demand evidence of.
🟡 **Deliberate design constraint:** keep the system **formative**. The moment it emits a score of record it becomes **high-risk under EU Annex III** (exam scoring is named). Feedback and scheduling are not.
🟢 **`P26` (access ≠ copyright):** this spine has **no hosted-service dependency** — `leap-framework` is `pip install -e .`, FSRS is local arithmetic. Inference is the only external call and is swappable (self-hosted Ollama/vLLM). 🔵 **Contrast pass 78's `Jeanikt/tutor-ai-agent`, which is MIT but unshippable without LiveKit Inference.**
⏱️ **Estimate: 6–8 weeks** to a governed pilot. 🔴 Declared as an estimate, not a measurement.

---

### 🟢 `R79b` — **EMEA, AI-Act-ready assessment feedback**, built on the one deployed-infrastructure row this shelf has

🟢 **The gap it closes:** the EU high-risk education deadline is **2 December 2027** (July 2026 Omnibus; 🟡 Official-Journal status flagged in `intel/market.md`). That is a programme-sized build and nobody has a permissive, already-deployed European base for it — 🟢 **except this one.**

```
  thm-mni-ii/feedbacksystem      Apache-2.0  10 785 B   dev  072e646   ← NOTE: branch is `dev`
    • AI-driven personalised student feedback
    • Helm chart on Artifact Hub · CI · codecov      → deploy, don't rebuild
    • copyright: "Technische Hochschule Mittelhessen"  (EMEA, from the payload itself)
        +
  Vinger-lee/leap-framework      MIT  1 084 B  main 2568667
    • State Guard  →  the documented human decision point
        +
  open-spaced-repetition/fsrs-rs BSD-3  1 509 B  main 0a57374
    • retention, computed locally — no student data leaves the institution
```

🔴 **The single most important architectural decision in this recipe is a refusal:** 🟢 **do not let it score.** Keep it formative — feedback, misconception detection, retention — and the system **stays outside Annex III's exam-scoring trigger**, which converts a conformity-assessment programme into ordinary software delivery. 🟡 **The inverse is the trap to name to the client:** remote proctoring with facial recognition or behaviour analysis is squarely high-risk, and adding it late re-classifies the whole system.
🟢 **Obligations that apply regardless:** **AI literacy** duties on staff (in force now) and **transparency/labelling** of AI-generated content. 🔵 Both are documentation deliverables and should be priced as such.
🔴 **Deploy-time trap, measured:** `git clone` of `feedbacksystem` without `-b dev` gets the wrong ref. T1 paid on this repository this pass.
⏱️ **Estimate: 10–14 weeks.** 🔴 An estimate.

---

### 🟢 `R79c` — **Socratic engineering academy**, for reskilling rather than schooling

🟢 **The gap it closes:** Globant's own reskilling and bootcamp surface. 🔴 Every tutor on this shelf teaches *subjects*; this recipe teaches *engineering*, and its two components are built to **withhold** answers — which is what makes graduates' competence real and measurable.

```
  afri-bit/revibe                MIT  1 074 B  main 46b5047
    • refuses to write the learner's code, by design
    • generates a personalised curriculum; progress tracked in markdown
    • hosts inside GitHub Copilot  → meets engineers in the IDE they already use
        +
  PrepLabsAI/InterviewMentor     MIT  1 071 B  main 609d311
    • interview-prep agent skills: mock interviews, LeetCode/DSA progression
        +
  Vinger-lee/leap-framework      MIT  1 084 B  main 2568667
    • mastery + hint-dependency as the promotion gate, not a quiz score
        +
  open-spaced-repetition/fsrs-optimizer  BSD-3  1 509 B  main ac2a82d
    • fit the schedule to THIS cohort's review log, cohort over cohort
```

🟢 **Why `leap-framework` is the keystone and not decoration:** it exposes **hint dependency** as a first-class signal (`hint_dependency: 0.25` in its own quick-start output). 🔵 **A learner who answers correctly only after three hints has not learned it**, and a quiz score cannot see the difference — the runtime can, and promotion can be gated on it.
🟢 **Fully permissive, fully self-hostable**; MIT ×3 + BSD-3 ×1. 🔴 **The BSD-3 no-endorsement term lands here too:** academy marketing may not claim FSRS endorsement.
⏱️ **Estimate: 3–5 weeks** (the thinnest of the three — both agent components are skill packs, not platforms). 🔴 An estimate.

---

### 🔴 What these recipes deliberately do NOT claim

- 🔴 **None of the three was BUILT or RUN this pass.** `P866`: no code from this clone, and no script of my own, executed — only inline measurement. 🟢 Every component's **grant, bytes, branch and SHA are first-hand**; every **wiring claim is read from the component's own README**; every **week estimate is declared an estimate**.
- 🔴 **`leap-framework` is a 1★ repository.** 🟢 Its artefacts are strong (58 MCP tools, 260 passing tests, CI badge, 8 localisations) and its grant is clean — 🟡 but it carries **single-maintainer risk**, and a client engagement should either vendor it or budget to maintain it. 🔵 Stated because star count is exactly what this shelf has resolved to stop treating as a quality signal.
- 🟡 **`revibe` and `InterviewMentor` are region-UNPLACED** (`P800`): zero localisation artefacts, zero locale markers. They are shelved on their grants and their substance, not on a placement.

## 🟢 Seventy-eighth pass, 2026-10-09 — three new recipes, and all three are buildable from components **payload-read this pass**: a voice tutor that keeps **no server-side student record**, the **LTI 1.3 + AGS adapter `Gap 316` has been waiting for** (its upstream froze the seam, so the studio writes it), and the **oversight-record** deliverable Oklahoma and Maryland now require

⏱️ **Tenth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 What changed against what pass 77 left

🟢 Pass 77 left `P850` (the LTI 1.3 + AGS adapter, route-priced on licence), `P851` (the closure gate as a client deliverable) and the courseware screen `P854` made work. 🔴 **All three priced what a studio ships. None priced where the student's DATA rests** — and every regulatory limb measured this pass converges on exactly that.

🔴 **And one blocker on `P850` is now removed in a way worth stating precisely:** the permissive grading component `Gap 316` called missing **exists** — it is MIT — and its author has declared the LMS seam out of scope **in the README**. 🟢 **That turns a sourcing problem into a build.**

---

## R78a — Voice tutor with **no server-side student record** (the AB 1159 / SB 1227 / GDPR answer)

**Time**: 6–8 wk to a localised pilot | **Licences**: 🟢 MIT + Apache-2.0 throughout, every grant payload-read this pass

### The stack, with every grant measured and every ref pinned

| layer | component | grant | bytes | ref |
|---|---|---|---|---|
| tutor reference | [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent) | 🟢 **MIT** | 1 103 | `main` `987f310` |
| agent runtime | [`livekit/agents`](https://github.com/livekit/agents) | 🟢 **Apache-2.0** | 11 357 | `main` `dbe555b` |
| React layer | [`livekit/components-js`](https://github.com/livekit/components-js) | 🟢 **Apache-2.0** | 11 357 | `main` `1ce6ca0` |
| browser client | [`livekit/client-sdk-js`](https://github.com/livekit/client-sdk-js) | 🟢 **Apache-2.0** | 10 142 | `main` `20e478d` |
| maths rendering | [`KaTeX/KaTeX`](https://github.com/KaTeX/KaTeX) | 🟢 **MIT** | 1 107 | `main` `6ea2dc9` |
| mastery model (optional) | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) — FSRS 4.5 + BKT | 🟢 **MIT** | **1 068** (`P859`) | `main` `f0142f2` |

### The three things to copy, not re-invent

```
1. record: false on the agent session
   -> no audio, no transcript, no trace uploaded to the inference vendor

2. the student model lives in the BROWSER
   -> localStorage, returned as a LiveKit participant attribute at next
      session start (`manu.memoria`); the chalkboard rides its own text
      stream (`manu.lousa`), rendered client-side with KaTeX

3. pedagogy BANDS, not a single persona
   -> grades 1-5 / 6-9 / exam-prep, each with its own turn length,
      vocabulary and examples; variables spelled phonetically so every
      TTS voice pronounces them ("xis", "ipsilon")
```

🔵 **Point 2 is the deliverable.** 🔴 Every regime measured this pass asks the same question — *where does the student's data rest, and does it train a model?* 🟢 **This architecture answers "on the student's device, and no" without a data-processing annex**: California **AB 1159**, Idaho **SB 1227**, FERPA, GDPR, Vietnam's behavioural-monitoring clause.

### 🔴 The two steps that are actually work

1. 🔴 **Close `P26`: replace LiveKit Inference.** The reference calls a **hosted** pipeline (`google/gemini-3.5-flash`, `xai/tts-1` voice `luna`, `turnDetection: 'stt'`). 🔴 **MIT settles copyright and says nothing about access**, and a hosted inference vendor re-opens the data question point 2 just closed. 🟢 Substitute self-hosted STT → local LLM → local TTS behind the same `@livekit/agents` interfaces. 🔴 **Unmeasured on this shelf: the latency cost of that swap.** Budget a spike; do not quote a figure.
2. 🟢 **Localise, don't rewrite.** The structure is locale-shaped: TTS locale, pedagogy bands, exam anchor. 🟢 **es-MX**: swap `pt-BR` → `es-MX`, ENEM → the national exam, bands → the local stage names. 🟢 **en-US**: same move, and the data story is the selling point rather than a footnote.

🟡 **Declared limits:** the repo states **3 simultaneous lessons**, counted against open LiveKit rooms — a pilot number, not a platform number. 🔴 And both `package.json` files declare `"license": null`, so **run a closure read before legal review**, not after (`P742`/`P757`).

---

## R78b — The **LTI 1.3 + AGS grading adapter**, built rather than waited for (`Gap 316`)

**Time**: 8–10 wk | **Licences**: 🟢 MIT core, 🟡 one Apache-2.0 / LGPL route decision

### Why this is now a build and not a search

🟢 [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) — 🟢 **MIT, 1 069 B**, `main` `b90bd88` — supplies the whole generation-and-review core: Lab DSL → linked **Exam** and **Grading** DSLs, validation before anything continues, a `WAITING_REVIEW` task with recorded human approve/reject, a candidate-safe preview that strips answers and internal grading references, local export with **no automatic publishing**.

🔴 **And it has no LMS seam.** 🟢 Measured: **0 hits** for `lti|AGS|assignment and grade|QTI|caliper|xapi|moodle|canvas|open ?edx|blackboard` across its **12 334-byte** README, where `Grading` appears **23** times. 🔴 Its own words: *"Automatic grading productization, local entity expansion, MCP/Agent expansion, external platforms… remain frozen."*

🔵 **So the missing piece is one adapter, and the upstream has told you it will not build it.**

```
LMS (Moodle GPL-3.0 | Canvas AGPL-3.0 | Open edX AGPL-3.0)
   |  LTI 1.3 launch + AGS line items
   v
[ADAPTER - the studio writes this]            <- the only new code
   |  Deep Linking -> create assignment from an approved Exam DSL
   |  AGS Score    -> post the Grading DSL result back as a line item
   |  NRPS         -> roster for candidate-safe preview distribution
   v
littlecookie0722/AI-Teaching-Agent  (MIT)
   Lab DSL -> Exam DSL + Grading DSL -> validate -> WAITING_REVIEW
   -> human approve/reject (RECORDED) -> local export
```

### 🟡 The route decision, priced on licence and on closure

| route | grant | the catch |
|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | 🟢 Node; the shelf's existing frontier row for launch/auth |
| `PyLTI1p3` | 🟢 **MIT** | 🔴 **closure is not permissive** — `jwcrypto` **LGPL-3.0-or-later** (pass 76). Fine when the adapter is a separate process; a problem when it is statically bundled |

🔵 **Keep the adapter a separate process either way** — it isolates the LGPL question, and it keeps the MIT core replaceable.

### 🔴 The regulatory gate is NOT optional, and it decides what you may ship

🔴 **US public K-12 (NYC and any district following it): do not ship the grading path at all.** `P764`'s red tranche — grading, promotion, discipline, counselling, crisis intervention, IEP/504, placement — is **prohibition**. 🔴 **No human-in-the-loop converts a prohibited use into a permitted one.** 🟢 **Ship the teacher-facing green lane**: generate, validate, human-review, export for the teacher to enter. 🟢 That is exactly what the MIT component already does, and its frozen scope is a feature here.

🟡 **EU (Annex III) and Vietnam (Law 134/2025/QH15, in force 2026-03-01): conditioned**, and the condition is an engineering spec. 🟢 Vietnam's test — high-risk principally where output drives decisions **without meaningful human review** — is answered by the `WAITING_REVIEW` gate **because the gate is architectural**: nothing exports until a recorded human decision exists.

🆕 🟡 **Oklahoma and Maryland: oversight-mandated** — see `R78c`, because the deliverable there is different.

---

## R78c — The **oversight record** as the deliverable (Oklahoma · Maryland, and the third mode of `P764`)

**Time**: 3–4 wk as an add-on to `R78b` | **Licences**: 🟢 MIT

🔴 **This is a separate recipe because the artefact is different.** 🟢 Oklahoma and Maryland require **human oversight** and **bar AI from high-stakes decisions about students**. 🔵 **A gate that stops for a human and keeps no record satisfies the EU's condition and FAILS this one.** 🟢 What is being bought is not the pause — it is the **provable, reconstructible account** of who reviewed what, when, and what they changed.

```
AI-Teaching-Agent's WAITING_REVIEW task  (MIT, already there)
        + reviewer identity from the LMS (LTI 1.3 NRPS)
        + the artefact DIFF: generated vs approved
        + an append-only decision log, exported per term
        = the oversight record
```

🟢 **Two properties to design in from the start, because retrofitting either is expensive:** the log is **append-only** (a reversible approval record is not a record), and it stores the **diff**, not just the verdict — *"approved"* on an artefact nobody can reproduce proves nothing.

🔵 **And it composes with `R78a`'s data story rather than fighting it:** the oversight record is about the **teacher's** decisions and belongs to the institution; the **student's** model stays on the student's device. 🟢 **Two different subjects, two different homes** — and conflating them is how a privacy-clean design acquires a server-side student record by accident.

---

## 🔴 Corrections to recipes already published in this file

🔴 **Do not substitute ERPNext for OpenEduCat on "both are open source".** 🟢 [`frappe/erpnext`](https://github.com/frappe/erpnext) is **GPL-3.0** (35 149 B, `develop` `2e6b8ed`, at lowercase **`license.txt`**) — strong copyleft. 🟢 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) is **LGPL-3.0** (8 241 B, `19.0` `1c95cef`) — 🟢 **the only weak-copyleft band in this tier, and therefore the only place a client-specific proprietary AI addon is lawful** (`P750`). 🔴 The swap loses that band.

🔴 **Do not ship `HugeCatLab/ChatTutor` as a hosted service.** **AGPL-3.0, 34 522 B**, `main` `7d9e905` — 🔴 §13 means offering it over a network releases the source. 🟢 Use it as a reference UI; the permissive tutor rows are `Jeanikt/tutor-ai-agent` and `zijinz456/OpenTutor`.

🔴 **Do not ship `plastic-labs/tutor-gpt` in a product.** **GPL-3.0, 35 149 B**, `main` `5c2f924` — the discovery channel reported no licence at all. 🟡 Strong copyleft, no network clause: usable self-hosted internally, not as a deliverable.

🔴 **Screen "skills packs" as CONTENT, not code.** `GarethManning/education-agent-skills` is **CC-BY-SA-4.0** (1 230 B) — 🔴 **ShareAlike reaches the prompt text a studio ships.** `Jeremy-xuan/SocraticNovel` is **CC-BY-NC-SA-4.0** (1 227 B) — 🔴 **NonCommercial; it cannot enter an engagement at all.** 🟢 Run `P854`'s fixed courseware screen over every pedagogy asset, not only over code.

🔴 **`AarambhDevHub/exam-cheating-detection` is MIT and must not be sold.** Gaze / face-presence / talking detection is EU **Annex III** high-risk with bias-testing, human-oversight and notification duties; **behavioural monitoring** under Vietnam's law; and NYC's **red** tranche. 🟢 MIT answers copyright; it does not make a prohibited use permitted.

🔴 **Sakai is ECL-2.0, not Apache-2.0** (11 120 B, `master` `fadec10`) — an Apache derivative with a **narrowed patent grant**. 🔴 **Chamilo is GPL-3.0, not GPL-2.0** (35 147 B, `master` `671a800`). 🟢 Both already correct on this shelf; both **wrong in the v6 `globant-kb/education/` snapshot**, which also links the dead slug `OpenEduCat-Inc/OpenEduCat` (`P864`). 🔴 Do not build a licence argument from that tree.

🔴 **Two "independent" MIT verticals are one vendor.** Krayin CRM (**MIT**, 1 078 B, `2.2` `fa4eeca`) and Aureus ERP (**MIT**, 1 077 B, `master` `070cacc`) both carry `Copyright 2010-2025, Webkul Software`. 🟡 Neither is an education system of record.

### 🔴 Figures in this file that are NOT re-verifiable this pass

🔴 **No figure in this section comes from a suite, because no suite ran** (`P860`, `Gap 333`). 🟢 Every byte count, ref and SHA above is a **first-hand live read by this pass**; every licence family is a **direct read of the payload's title block** by this pass, **not** a `license_family.sh` output. 🔴 **`patterns-figure-audit/extract_figures.py --check` could not be executed**, so the suite-derived figures in the sections *below* this one are **carried, not re-verified** — the next pass with execution must re-run it before citing them.


## 🟢 Seventy-seventh pass, 2026-10-09 — the newly-bought `/trending` channel supplies a **permissive curriculum substrate**, and `P854` makes the courseware screen that assembling it requires actually work

⏱️ **Ninth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 What changed, restated against what pass 76 left

🟢 Pass 76 left two patterns — `P850` (the LTI 1.3 + AGS adapter, route-priced on licence) and `P851` (the closure gate as a client deliverable). 🔴 **Both price the CODE a studio ships. Neither prices the CONTENT it ships**, and an education engagement ships both.

🔴 **And the content screen was broken until this pass.** 🟢 `P854` (`repos/foundations.md`): a `CC-BY-NC-SA` or `CC-BY-NC-ND` pack declared as the **abbreviation** — the form a README uses — classified as `CC-UNSPECIFIED` and returned commercial use **ALLOWED**. 🔵 **`P856` below is the pattern that screen exists for, and it could not have been written honestly before today.**

---

### 🟢 `P856` — **the permissive course pack: assemble from trending curriculum repos, screen every asset on CC attributes, deliver through the gated AGS writer**

🔵 **The problem this solves.** A studio winning a "build us an AI/data curriculum" engagement has two bad defaults: 🔴 write every notebook from scratch (expensive), or 🔴 fork the best-looking repo on GitHub Trending (and inherit a grant nobody read). 🟢 This pass measured a third path: **eight permissive, payload-verified teaching repositories**, plus the instruments to screen and deliver them.

**Step 1 — the substrate, every grant read from the payload (`P843`), never from a badge**

| component | family, measured | role in the pack |
|---|---|---|
| [`ageron/handson-mlp`](https://github.com/ageron/handson-mlp) | 🟢 **Apache-2.0** (10 175 B) | the ML/DL notebook spine — 🔵 **pick this first: the patent grant is the only one in the table** |
| [`rasbt/machine-learning-book`](https://github.com/rasbt/machine-learning-book) | 🟢 **MIT** (1 079 B, `LICENSE.txt`) | PyTorch + Scikit-Learn depth, holder-dated **2021-2026** |
| [`guipsamora/pandas_exercises`](https://github.com/guipsamora/pandas_exercises) | 🟢 **BSD-3-Clause** (1 515 B) | 🟢 **the exercise bank** — the asset `p533` consumes |
| [`ed-donner/agents`](https://github.com/ed-donner/agents) · [`llm_engineering`](https://github.com/ed-donner/llm_engineering) | 🟢 **MIT** (1 066 B each) | the agentic-engineering and LLM tracks |
| [`jamwithai/production-agentic-rag-course`](https://github.com/jamwithai/production-agentic-rag-course) | 🟢 **MIT** (1 068 B) | the production-RAG module |
| [`anthropics/claude-cookbooks`](https://github.com/anthropics/claude-cookbooks) | 🟢 **MIT** (1 065 B) | lab recipes |

🔴 **Two rows that must NOT enter the pack, and both look fine from the trending list:**

| 🔴 excluded | why |
|---|---|
| [`xiaolai/the-craft-of-selfteaching`](https://github.com/xiaolai/the-craft-of-selfteaching) | 🔴 **`CC-BY-NC-ND-3.0`** — NonCommercial **and** NoDerivatives. No grant file; declared in README line 83. 🔵 **No commercial use, no adaptation: there is no version of this engagement that may include it.** |
| [`wesm/pydata-book`](https://github.com/wesm/pydata-book) | 🟡 **MIT-SCOPED** — `COPYING`'s subject line is *"Code examples from …, 3rd Edition"*. 🟢 **The code examples may ship; the book prose may not.** Take the notebooks, leave the text. |

**Step 2 — screen EVERY asset, including the ones that arrive as content rather than code**

```bash
. compose/code/lib/license_family.sh

# the grant as the payload gives it -- file, or the README line when there is no file
osi_family_of  "$(cat LICENSE)"        # -> MIT | Apache-2.0 | BSD | CC-BY-NC-SA-4.0 | ...
commercial_use_ok "$(cat LICENSE)"     # exit 0 = may ship commercially, 1 = may NOT
```

🔴 **This is the step `P854` repaired, and the one a pre-pass-77 run would have got wrong.** 🟢 Measured now: `CC-BY-NC-SA-4.0` and `CC-BY-NC-ND-4.0` as **abbreviations**, and `creativecommons.org/licenses/by-nc-*/<v>` as a **bare URL**, all return **PROHIBITED**; `CC-BY-4.0` and `CC-BY-SA-4.0` correctly stay **ALLOWED**.

🔴 **And the limit you must work around, because it is still open (`Gap 332`):** the classifier reads a **4000 B window** (`P308`, measured). 🔴 A grant declared **late in a long README** falls outside it and returns `UNCLASSIFIED` → **ALLOWED**. 🟢 **So for any repo with no grant FILE, grep the README yourself and classify the LINE:**

```bash
grep -m1 -iE 'licen[cs]e|CC[ -]BY|版权协议' README.md | xargs -0 -I{} true   # find it
osi_family_of "$(grep -m1 -iE 'CC[ -]?BY|licen[cs]e' README.md)"            # classify it
```

**Step 3 — the exercise bank becomes assessable**

🟢 `guipsamora/pandas_exercises` (BSD-3) is a bank of graded tasks; 🟢 `compose/code/p533-qti3-template-emitter` turns items into **QTI 3** so they load into Moodle or Open edX as real assessments rather than static notebooks.

**Step 4 — delivery and grade return, reusing `P850` unchanged**

🟢 Front the pack with the **Route A** adapter of `P850` (Apache-2.0 + BSD-3 + MIT + MIT, four permissive rows) for LTI 1.3, and 🟢 route every grade write through `compose/code/mcp-allowlist-gateway/gateway.py` with **`putGrade` floored** — refused *and never advertised* (**34/34** green this pass). 🔵 That single switch is what satisfies Maryland's and Oklahoma's human-oversight rules, NYC's grading bar, and the EU Annex III oversight duty **with one codebase** (`intel/market.md`).

**Step 5 — the notices file, reusing `P851` unchanged**

🟢 Run the `P851` closure gate over the code the studio writes, 🆕 **and extend its output with a CONTENT table** — one row per source repo, carrying family, holder and the scope note where there is one (`pydata-book`). 🔴 **An MIT/BSD/Apache notice condition is per-asset**, and six of the eight rows above carry one.

**Estimate**

| | |
|---|---|
| licence screen of the eight repos (step 2) | 🟢 **under a day** — the instrument is written and green |
| curriculum selection and de-duplication (steps 1, 3) | 🟡 **2–3 weeks** — judgement, not measurement |
| LTI 1.3 + floored AGS delivery (step 4) | 🟡 **4–6 weeks**, and 🔴 **`Gap 316(i)`'s wiring number is still unmeasured**, so this is the soft figure in the table |
| notices + obligations memo (step 5) | 🟢 **2–3 days** per `P851` |

🔵 **What makes this a pattern rather than a reading list:** 🔴 **the agent tier for education is empty** — four passes and three `/trending` slices found no education-domain agent (`intel/trends.md`). 🟢 **So the curriculum layer is REUSE and the agent layer is BUILD**, and this pattern is how the reuse half is made safe enough to sell.

## 🟢 Seventy-sixth pass, 2026-10-09 — **`P15` stage 3 now reads PAYLOADS, not just names**, and the LTI adapter pattern gets a **licence-priced route choice** instead of a language preference

⏱️ **Eighth pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 What changed in the gate, restated against what pass 75 left

🟢 Pass 75 closed `Gap 329`: `pkgrepo` maps a package name to a repository, so `P15` stage 3 could *reach* each dependency. 🔴 **But reaching is not reading.** On PyPI and Packagist the gate still stopped at the registry's licence **field**, which `P843` forbids treating as the payload — and which `jwcrypto` has now shown can be **empty while the real declaration lives in a different field entirely**.

🟢 **`distpayload` closes that for PyPI.** The gate's stages, as they now actually execute:

| stage | instrument | what it answers |
|---|---|---|
| 1 | `lib/measure --family` | the ROOT grant, from the payload |
| 2 | `pkgrepo --deps` / `--closure` | the runtime dependency names, by DISTRIBUTION name (`P842`) |
| 3 | 🆕 **`distpayload --closure-pypi`** | **each dependency's grant, read from the artefact that ships** |
| 4 | `lib/probe_payload.sh` | the repository read, when a distribution ships no grant (`Gap 330` limb 1) |

🔴 **Stage 3 is npm + PyPI only.** 🟡 Packagist resolves and declares but its published zip is `FETCH-REFUSED-403` here (`Gap 331`); use stage 4 at the **pinned commit** and say so.

---

### 🟢 `P850` — **the LTI 1.3 + AGS adapter, with the route chosen on licence rather than on language**

🔵 **The problem this solves.** `Gap 316` is a two-sided seam: closed vendors hold LTI 1.3 + AGS grade return; the permissive components on this shelf (`moocupv/lti-ai-grader`, `OATutor`) stop at **LTI 1.1**. 🟢 Pass 73 established the cheap side is to put a 1.3 + AGS adapter in front of a permissive tutor. 🔴 **What nobody had measured is that the three ways to write that adapter carry three different licence obligations.**

**Route A — PHP, and it is the recommended one for a closed deliverable**

| component | version | licence | measured |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) · composer `packbackbooks/lti-1p3-tool` | **v6.4.4** (2026-09-23) | 🟢 **Apache-2.0** | `master/LICENSE.md` **11 343 B** |
| `firebase/php-jwt` → repo `googleapis/php-jwt` | v7.2.1 | 🟢 **BSD-3-Clause** | **1 529 B** |
| `guzzlehttp/guzzle` | 8.2.0 | 🟢 **MIT** | **1 460 B** |
| `phpseclib/phpseclib` | 4.0.2 | 🟢 **MIT** | **1 081 B** |

🟢 **AGS surface, enumerated at `a20c71b7`:** `createLineitem`, `findOrCreateLineitem`, `updateLineitem`, `deleteLineitem`, `getLineItem(s)`, `findLineItem`, `getResourceLaunchLineItem`, `putGrade`, `getGrades`, `getScope` — with scopes `lineitem`, `lineitem.readonly`, `result.readonly`, `score`. 🟢 **Plus `LtiNamesRolesProvisioningService` (NRPS) and `LtiDeepLink` in the same tree.**

**Wiring, concretely:**
1. **Launch + grade return (PHP):** `packbackbooks/lti-1p3-tool` as the tool provider. `LtiServiceConnector` holds the client-credentials token; `LtiAssignmentsGradesService::putGrade` writes the score back.
2. **The teacher-approval gate, which is not optional:** put `compose/code/mcp-allowlist-gateway/gateway.py` (**MIT-era shelf artefact, 128 lines, 34/34 green**) between the tutor and the AGS writer, with `putGrade` **floored** — the gate's own floor semantics mean a tool in the allowlist is still refused and never advertised. 🔵 **This is the `P85` pattern's third instance**, after `unitime-mcp-gate` and `sebserver-mcp-gate`.
3. **The grading core (Python, kept on the other side of the wire):** any permissive tutor already on this shelf. 🔴 **Do NOT import `PyLTI1p3` into it** — that is where the LGPL enters (below).
4. **Boundary:** HTTP/JSON between (3) and (1). 🟢 **The licence boundary and the process boundary are the same line**, which is what makes this route clean.
5. **Notices file:** four rows — Apache-2.0, BSD-3-Clause, MIT, MIT.

**Route B — npm.** [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) **7.0.7**, Apache-2.0 (11 361 B), closure **9/10 payload-MIT**. 🔴 **Two caveats carried from pass 75:** `engines.node >= 24`, and **`sprightly@2.0.1` ships no notice** — 🟢 remedy is a one-line upstream PR (`files: ["dist"]` excludes a `LICENSE` that **does** exist upstream at 1 070 B), plus a notices-file entry meanwhile. 🟡 **Clean, with homework.**

**Route C — PyPI. 🔴 Use only when the deliverable can carry LGPL-3.0.**

| member | licence |
|---|---|
| `PyLTI1p3` 2.0.0 | 🟢 MIT (1 070 B, wheel **and** sdist) |
| **`jwcrypto` 1.6.1** | 🔴 **LGPL-3.0-or-later** (7 651 B) |
| `pyjwt` 2.15.1 · `requests` 2.34.2 · `typing-extensions` 4.16.0 | 🟢 MIT · Apache-2.0 · **PSF-2.0** |

🔴 **`jwcrypto` is LGPL-3.0, so a deliverable that links it owes the LGPL's relinking obligation.** 🟡 **It is LGPL, not GPL** — dynamic linking with a replaceable library is the intended accommodation — 🔴 **but that is a counsel question, not an engineering one, and `P12` says this shelf names it rather than resolves it.** 🟢 **`typing-extensions` adds one notices row MIT does not: PSF-2.0 §2 wants the copyright notice *and* a brief summary of changes.**

🟢 **The decision rule, which is the pattern's actual content:** 🔵 **pick the adapter's language from the closure, then put the tutor behind a process boundary.** 🔴 **Not the reverse** — choosing Python because the tutor is Python drags `jwcrypto` into the deliverable for no engineering gain.

**Estimate:** 🟢 **3–4 weeks** for Route A against one LMS (Moodle or Canvas), including the approval gate and an AGS line-item round trip. 🔵 Unchanged from `Gap 316(i)`'s standing figure — 🟢 **what this pass removed is the licence contingency behind it, not the engineering.**

---

### 🟢 `P851` — **the closure gate as a client-facing deliverable, runnable in one command**

🔵 **Why it is a pattern and not a chore:** an engagement that adopts an open-source LMS is asked *"what does this oblige us to publish?"* 🔴 **The honest answer needs a payload read of the components the studio writes, and until this pass that read had no instrument for two of three ecosystems.**

```bash
# 1. the root grant, from the payload (not the badge)
compose/code/lib/measure LICENSE --repo <owner>/<repo> --name LICENSE

# 2+3. the runtime closure, each grant read from the shipped artefact
compose/code/lib/distpayload --closure-pypi <distribution-name>
compose/code/lib/distpayload --packagist <vendor>/<package>
compose/code/lib/distpayload --pypi <name> --sdist   # the OTHER artefact

# 4. when a distribution ships no grant, fall back to the repository
. compose/code/lib/probe_payload.sh
```

🟢 **Read the rows as `P843` requires: declared FIRST, payload SECOND, and never let the first stand for the second.** The verdicts that must stop a build: 🔴 **`NO-NOTICE`** (the artefact cannot satisfy an MIT/BSD notice condition — `sprightly`), 🔴 **any copyleft family in `PAYLOAD-*`** (`jwcrypto`), 🔴 **`FETCH-REFUSED-<code>`** (unmeasured, not clean — and the code names which boundary answered, per `P844`).

🟡 **Two traps this pass walked into, so an engagement does not:** 🔴 **a 404 body written to a file measures as a payload** — 14 B of `404: Not Found` classified `UNCLASSIFIED` rather than erroring, which is why `P847` requires the status, not just the bytes. 🔴 **And `-` for a declared licence may mean PEP 639**, not "unlicensed" (`P846`).

**Estimate:** 🟢 **2–3 days** to produce a notices file and an obligations memo for a stack of ~40 runtime dependencies, 🔵 of which the measurement is hours and the reading is the rest.

## 🟢 Seventy-fifth pass, 2026-10-09 — **`P15` stage 3 is executable for the first time.** `Gap 329` closes with `lib/package_repo.sh` + `lib/pkgrepo` + `p840-package-repo` 🟢 **37/37**, and the fetch limb **ran live** against all three registries

⏱️ **Seventh pass of this date.** **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 The gap, restated so the closure can be checked against it

🔴 **`Gap 329`:** *"`P15` needs stage 3 — probe the payload of each core dependency. A PyPI/npm/Packagist name is not a GitHub path, and nothing on this shelf maps one to the other. `core_deps_of` and `repo_of_pypi` are named in `P15` and **not written**."* 🔴 **Consequence:** `P836`'s gate had its most expensive stage blocked on a human, which is the arrangement `Gap 328` existed to end — and `73-C`'s `PyMuPDF` catch was made by hand.

### 🟢 Shipped, and split on the seam `P838` requires

🟢 **`P838` says split a shared instrument on the capability the environment DENIES, not on its calling convention.** 🟢 **Measured this pass, not inferred:**

| host | result |
|---|---|
| `pypi.org/pypi/<name>/json` | 🟢 **200** |
| `registry.npmjs.org/<name>` | 🟢 **200** |
| `repo.packagist.org/p2/<vendor>/<pkg>.json` | 🟢 **200** |
| `eur-lex.europa.eu` | 🔴 **403 to CONNECT** (`Gap 308`, eighth refusal) |

🔵 **All three registries sit in the proxy's own `noProxy` list, so unlike `Gap 328`'s payload probe the network limb WORKS here.** 🟢 **The seam is kept anyway** — every parse lives in the network-free half and is asserted offline, so the suite stays green in a session whose egress differs. 🔴 **An instrument that only works where it was written is the failure `P838` names.**

| artefact | what it gives |
|---|---|
| `compose/code/lib/package_repo.sh` | `normalise_repo_url`, `repo_from_pypi_json`, `repo_from_npm_json`, `repo_from_packagist_json`, and **`core_deps_of_requirements` / `core_deps_of_package_json` / `core_deps_of_pyproject`** — the `core_deps_of` that `P15` named and nobody had written |
| `compose/code/lib/pkgrepo` | argument-invocable front end: `--pypi`, `--npm`, `--packagist`, `--parse`, `--deps`, **`--closure <eco> <manifest>`**, `--self-test`. 🔴 **Exits non-zero on anything that is not a resolved path** |
| `compose/code/p840-package-repo/test_package_repo.sh` | 🟢 **37/37**, offline, single file on purpose |

### 🟢 The verdict vocabulary, and why absence has to be loud

🟢 `lib/measure` set the precedent — a missing payload is `NO-PAYLOAD`, never `0 B`. Same discipline, and it buys this shelf something it has wanted:

| verdict | meaning |
|---|---|
| `owner/repo` | 🟢 resolved — the only verdict `P15` stage 3 can probe |
| `NO-REPO` | 🔴 metadata exists, declares **no source** → **this is `Gap 327`'s category** |
| `UNRESOLVABLE-HOST` | 🔴 source declared at an **SSH-config alias** — an address only the publisher can resolve |
| `NON-GITHUB` | 🟡 real source on GitLab/Bitbucket/other — not probeable by this shelf's instruments |
| `NO-METADATA` | 🔴 the registry has no such package |

🔵 **`NO-REPO` is the valuable one: `Gap 327` ("permissive but sourceless") was hit three times in one chain and caught by hand every time.** 🟢 **Now it is a measurement** — the chain reads, live:

```
npm:@iblai/iblai-js            NO-REPO              exit=1
npm:@iblai/iblai-api           NO-REPO              exit=1
npm:@iblai/iblai-web-mentor    UNRESOLVABLE-HOST    exit=1
npm:ltijs                      Cvmcosta/ltijs       exit=0
```

🔴 **Never collapse `NO-REPO` into `NO-METADATA`.** The first is a package that exists and publishes no source; the second is a name that does not exist. They license opposite next actions — *ask upstream for a repo* vs *correct the name* — and this shelf has written both in the same voice before (`P827`, `Gap 301`). 🟢 Asserted as a test, not only as a rule.

### 🔴 The finding that matters most, because the offline suite could not see it

🔴 **The suite was 32/32 green and the instrument was still wrong.** Pass 74 wrote the honest limit on `Gap 328`'s closure: *"the fetch branch is **unexecuted** … the first pass with network must run it."* 🟢 **This pass ran it, and that warning landed within four commands:**

🔴 `@iblai/iblai-web-mentor` declares `repository.url = "git@ibl_connection:iblai/iblai-web-mentor.git"` under a 🟢 `"license": "MIT"`. 🔴 **`ibl_connection` is not a host — it is an SSH-config alias resolvable only inside the publisher's own machine.** 🔴 **The parser emitted `ibl_connection:iblai/iblai-web-mentor` and exited 0**, so a caller would have gone on to probe a GitHub path **that was never declared**, and `P827` forbids exactly that. 🟢 Fixed, verdict `UNRESOLVABLE-HOST` added, both the alias case **and** the real `git@github.com:owner/repo` case asserted so the fix cannot swallow the good one.

🟢 **`P841` adopted — an offline suite green on fixtures is not evidence the fetch limb is correct.** 🔵 The fixtures encode the formats the author already knew; the registries hold the ones they did not. 🟢 **Every verdict class must be re-asserted against at least one live payload before the instrument is cited**, and the live-found cases go back into the suite as regressions (five were added this pass, 32 → 37).

🔵 **And it sharpens `Gap 327` rather than just detecting it:** an MIT grant over an address nobody outside the vendor can resolve is a *stronger* form of "permissive but sourceless" than a missing field. 🔴 **A missing `repository` is visibly absent. An alias address looks like provenance and is not.**

### 🟢 `P842` — the import name is not the package name, and the stub is real

🔴 Measured live on PyPI: **`fitz` is version `0.0.0`, with `license: null`, `home_page: null`, `project_urls: null`, and an empty summary** → `NO-REPO`. 🔴 **`fitz` is also PyMuPDF's *import* name.** 🟢 So a `requirements.txt` — or an LLM-generated manifest — that lists `fitz` because the code says `import fitz` pins **an unrelated empty stub**, and a licence audit of it returns a clean nothing while 🔴 **the actual dependency, `pymupdf` → [`pymupdf/pymupdf`](https://github.com/pymupdf/pymupdf), is the AGPL-or-commercial core `73-C` found by hand.**

🟢 **`P842`: resolve dependencies by DISTRIBUTION name, never by import name, and treat a `0.0.0` release with no URLs and no licence as a stub rather than a dependency.** 🔵 **This is the one place in the gate where a wrong answer is worse than no answer:** it does not fail, it returns *reassurance* about the wrong package.

### 🟢 `P15` stage 3, end to end, on the closure this shelf most needed

```sh
# runtime closure of the library that closes Gap 316's protocol hop
curl -sS https://registry.npmjs.org/ltijs > /tmp/ltijs.json      # dist-tags.latest → 7.0.7
#   ... write {"dependencies": …} of the latest version to ./package.json ...
bash compose/code/lib/pkgrepo --closure npm ./package.json
```

🟢 **Result: 10 of 10 resolved, exit 0** — `cors`→`expressjs/cors`, `debug`→`debug-js/debug`, `express`→`expressjs/express`, `helmet`→`helmetjs/helmet`, `ioredis`→`redis/ioredis`, `jsonwebtoken`→`auth0/node-jsonwebtoken`, `mongoose`→`Automattic/mongoose`, `parse-link-header`→`thlorenz/parse-link-header`, `sprightly`→`obadakhalili/sprightly`, `zod`→`colinhacks/zod`. 🟢 **The licence verdict that follows from it is in `repos/foundations.md`: 9 payload-verified MIT under an Apache-2.0 root, and `sprightly` an assertion without a grant.**

🔵 **Which is the point of the whole gate.** 🔴 **Stage 1 alone — read the root `LICENSE` — returns "Apache-2.0, clean" for `ltijs` and for `PyMuPDF` both.** 🟢 **Stage 3 is what separates them**, and it is now one command instead of a human.

### 🟡 Where the gate still stops

🔴 **Payload verification of a dependency's grant worked here only because npm publishes tarballs and `registry.npmjs.org` is reachable.** 🟢 The 9-of-10 column above was read from **inside the `.tgz` of each installed artefact**, which is the strongest form of this measurement — it is the file the client actually deploys. 🔴 **For PyPI and Packagist the equivalent read is unexercised this pass.** 🟢 **But the repository read is NOT blocked, contrary to what this shelf had recorded:** `raw.githubusercontent.com` answers **200** in this session, and `lib/test_probe_payload.sh` ran **12/12 green against 12 live repositories** — discharging pass 74's standing instruction. 🟢 **So stage 4 is available too: when a dependency ships no grant, read its repository.** Run that way, `sprightly` resolves to 🟢 **`main/LICENSE`, 1 070 B, MIT, Copyright (c) 2024 Obada Khalili** — a grant that exists and is merely unpackaged. 🔵 **`Gap 330` keeps only its PyPI/Packagist and `NON-GITHUB` limbs**, and `P844` records why a stale refusal record is expensive.

## 🟢 Seventy-fourth pass, 2026-10-09 — `P836` gets the **instrument it was missing**: a new pattern `P15` that gates a base on its **dependency closure**, built on the probe half this pass made runnable. `P14-R` is its first test case and **fails it**

⏱️ **Sixth pass of this date.** Pass 73 and its correction `73-C` closed earlier today (commit `7ce7b79`). **Append-only: this section is new; nothing below it was rewritten.**

### 🔵 Why this pattern exists, stated as the failure it prevents

🔴 **`73-C` adopted `P836`** — *"clear a pattern's base on its dependency closure, not its `LICENSE`"* — because `P14-R` was re-based onto `HKUDS/DeepTutor` with the sentence *"It is Apache-2.0, so it can be carried"*, while `PyMuPDF>=1.26.0` sat in that repository's **core dependency array**, dual-licensed **AGPL-3.0 or Artifex Commercial**, with this shelf's own verdict **REVIEW-STRONG** on record since 2026-10-06.

🔴 **`P836` is a rule with no control, which `lib/README.md` says is not a control at all:** *"una regla que hay que recordar no es un control."* 🟢 **The shelf had already measured the offending dependency and the pattern still shipped without it** — so the defect is not missing data, it is a missing gate. 🟢 **`P15` is that gate.**

### 🟢 `P15` — The licence-closure gate: never clear a base on its root payload alone

🟢 **What it is:** a four-stage check a studio runs **before** pricing any pattern on a candidate base, producing a one-page licence verdict for the base *and its declared dependencies*. 🟢 **Entirely composed of components this repository already versions.**

| Stage | Component | Licence | What it does |
|---|---|---|---|
| 1 — resolve | `lib/probe_payload.sh` → `probe_default_branch` | this repo | 🟢 Resolve the **real** default ref via `ls-remote --symref`. 🔴 Never assume `main` — measured counter-examples on this shelf: `GibbonEdu/core` → `v31.0.00`, `portabilis/i-educar` → `2.12`, `francoisjacquet/rosariosis` → `mobile`, `krayin/laravel-crm` → `2.2` |
| 2 — root grant | 🆕 `lib/measure --family` / `--size` | this repo | 🟢 Classify the root payload by **title block** (`P171` via `license_family.sh`), size it **byte-exact** (`P834`). 🔴 Not `$(…)` — see below |
| 3 — **closure** | 🆕 `lib/measure --family` over each manifest-declared dependency's payload | this repo | 🔴 **The stage `P14-R` skipped.** Parse `pyproject.toml` / `package.json` / `composer.json` for the **core** arrays only, then run stage 2 on each |
| 4 — protocol reach | 🆕 `lib/measure --count <pathlist> <protocol>` | this repo | 🟢 Word-bounded (`P831`) counts of `lti`, `xapi`, `caliper`, `scorm`, `oneroster` over the `ls-tree` enumeration (`P829`) |

🟢 **Wiring, concretely:**

```sh
# stage 1+2 — the base's own grant
. compose/code/lib/payload_measure.sh
probe_repo HKUDS/DeepTutor                 # -> repo branch LICENSE 11408 Apache-2.0 <holder>

# stage 3 — THE CLOSURE.  For each core dependency, probe ITS payload.
#   DeepTutor's core array yields pymupdf/PyMuPDF  -> AGPL-3.0 or Artifex Commercial
for dep in $(core_deps_of pyproject.toml); do
  probe_repo "$(repo_of_pypi "$dep")"
done

# stage 4 — does the base reach the LMS at all?
git ls-tree -r --name-only HEAD | lib/measure --count /dev/stdin lti
```

🟢 **Verdict rule, and it is the point of the pattern:** 🔴 **a base is cleared only if stage 2 AND every row of stage 3 are permissive.** 🟡 A copyleft row does not kill the pattern — it **prices** it, as one of three options (accept the copyleft, pay the commercial grant, or replace the layer).

### 🔴 `P15` run against `P14-R`, which is its first test case — and `P14-R` does not pass stage 3

| Stage | `HKUDS/DeepTutor` | Verdict |
|---|---|---|
| 1 — default ref | `main` · `6cf793bd` · 2026-10-08 | 🟢 resolves |
| 2 — root grant | **Apache-2.0**, **11 408 B**, holder *Data Intelligence Lab, The University of Hong Kong* | 🟢 permissive |
| 3 — **closure** | 🔴 **`PyMuPDF>=1.26.0` in the core array — AGPL-3.0 **or** Artifex Commercial** | 🔴 **FAILS** |
| 4 — protocol reach | 🔴 **0 LTI, 0 xAPI, 0 Caliper, 0 SCORM, 0 OneRoster** in 3 763 files | 🔴 adapter is net-new |

🟢 **So `P15` reproduces, mechanically, the finding `73-C` had to make by hand** — which is the test of whether a gate is worth having. 🔵 **Had `P15` existed one pass earlier, `P14-R` would not have shipped the sentence that needed correcting.**

🟢 **`P14-R`'s recommendation is unchanged and is now derived rather than asserted:** price the third option — **replace the PDF layer** — at `DeepTutor`'s plugin seam (single-shot Tools / multi-stage Capabilities). 🔵 It is the only branch that preserves what `P14-R` is *for*: an end-to-end auditable grade path with no copyleft and no closed component in it.

### 🟢 The two measurement fixes `P15` depends on, both landed this pass

🔴 **`lib/probe_payload.sh` committed `P834` itself.** `body=$(_raw …)` strips the trailing newline **run**, so `printf '%s' "$body" | wc -c` was low by that run on **every payload the shared probe has ever measured**. 🟢 Fixed: `_row_from_fetch` writes the payload to a file and sizes it with `wc -c < file`.

🔵 **And `P834`'s wording was an understatement.** Measured offline with the `P126`-2 negative control:

| trailing newlines | 0 | 1 | 3 |
|---|---|---|---|
| bytes lost via `$(…)` | 🟢 **0** | 🔴 **1** | 🔴 **3** |

🟢 **`P831`'s substring trap, re-measured:** word-bounded counting returns **1** on the five-path fixture where substring counting returns **4** — and 🔵 **the fourth hit is `src/utils/multiply.ts`** (mu-**lti**-ply), which the suite's own author did not think to write down. 🔴 **Three of the four false hits are invisible to inspection**, so stage 4 above is only trustworthy word-bounded.

🟢 **`Gap 328` CLOSED:** `lib/payload_measure.sh`, `lib/measure`, `p837-payload-measure/test_measure.sh` — **27/27, offline, runnable here.**

### ⚠️ What `P15` is not, and the honest limit on shipping it today

🔴 **Stages 1–3 need the network, and this environment refuses it** — `curl` is denied `[Exfil Scouting]` and sourcing `probe_payload.sh` is denied `[Code from External]` because it contains `curl`. 🟢 **Stage 2's classification and sizing, and stage 4's counting, are asserted 27/27 offline and run here.** 🔴 **The fetch and the manifest walk are specified and unexecuted.**

🔵 **`core_deps_of` and `repo_of_pypi` above are named, not written** — a PyPI name is not a GitHub path, and that mapping is the one piece of `P15` with no component on this shelf. 🟢 **That is `Gap 329`**, opened this pass rather than left as an implied to-do. 🟡 **Until it lands, stage 3 is a manual read of the manifest against the shelf's existing licence records — which is exactly how `73-C` found `PyMuPDF`, so the pattern is usable by hand today and automatable once `Gap 329` closes.**

## 🔴 Seventy-third pass, **correction (73-C)**, 2026-10-09 — `P14-R`'s re-base is sound, but it was published **without the AGPL dependency in its base's core**

### 🔴 `P14-R` — corrected. The tutoring runtime is Apache-2.0; its PDF layer is **AGPL-or-Artifex**

🔴 **The section below re-bases `P14-R` onto `HKUDS/DeepTutor` and says *"It is Apache-2.0, so it can be carried."*** 🟢 **The repository's grant is Apache-2.0. Its core dependency closure is not.** 🟢 **This shelf has held since 2026-10-06:** `PyMuPDF>=1.26.0`, **core array**, 🔴 **dual-licensed *GNU AGPL-3.0 or Artifex Commercial*** (v1.28.2) — shelf verdict 🔴 **REVIEW-STRONG**, *"AGPL, or pay Artifex, or replace the PDF layer."*

🟢 **`P14-R` stands with one row added to its build sheet, which the pattern cannot ship without resolving:**

| Decision | Option | Consequence |
|---|---|---|
| PDF ingestion | 🔴 Keep `PyMuPDF` under AGPL-3.0 | 🔴 Network copyleft reaches the deployed tutor — **fails the "no copyleft in the learner path" premise this pattern was built on** |
| | 🟡 Buy the Artifex commercial licence | 🟡 Per-deployment cost; keeps the stack permissive downstream |
| | 🟢 Replace the PDF layer (e.g. `pypdfium2`, BSD-3-Clause) | 🟢 Keeps the closure permissive; 🔴 net-new integration work against `DeepTutor`'s ingestion seam |

🟢 **Recommendation: price the third option.** 🔵 It is the only one that preserves what `P14-R` is *for* — an end-to-end auditable grade path with **no copyleft and no closed component in it** — and `DeepTutor`'s plugin model (single-shot Tools / multi-stage Capabilities) is the seam to do it at.

🔴 **Why this correction exists at all:** pass 73 re-based the pattern on a licence file and did not read the dependency closure, **although this shelf had already measured it and marked it REVIEW-STRONG.** 🟢 **`P836`: a pattern's base must be cleared on its dependency closure, not only on its `LICENSE`.** 🔵 Same lesson as `Gap 327` inverted: that gap is a permissive grant with no source; this is a permissive grant with a copyleft closure. 🟢 **Neither survives a probe that stops at `LICENSE`.**

### 🟡 `P26-R` and `P27` — unchanged by this correction

🟢 **`P26-R`** uses `OpenTutor` for *teacher-side* material prep, so the PDF-layer question does not reach a learner path; 🟡 it should still be resolved before deployment. 🔵 **Note `OpenTutor` was already on this shelf** — `P26-R` is a new *composition* of known components, which is what a pattern is, and that claim is unaffected. 🟢 **`P27`** is a refusal and rests on the `iblai` measurements, which stand.

## 🟢 Seventy-third pass, 2026-10-09 — `P14-R` is **re-based onto a repo with its own multi-tenant access layer**, and one new pattern exists only because this pass measured that the seam it needs is **absent on both sides**

⏱️ **Fifth pass of this date.** Pass 72 closed earlier today (commit `e99be83`). **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `P14-R` — **Re-based.** The permissive graded tutor, now standing on `DeepTutor` instead of greenfield multi-tenancy

🔵 **What changed:** every prior pricing of `P14-R` had to treat learner identity, guardian consent and per-learner authorisation as work to write. 🟢 **`HKUDS/DeepTutor` ships that layer, Apache-2.0.**

**Wire it like this:**

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Tutoring runtime | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) `main` `6cf793bd` | 🟢 **Apache-2.0** 11 407 B | 3 763 files, **1 220 test files**, `compose.yaml` + `Dockerfile` for self-hosting |
| Multi-tenant access | `deeptutor/multi_user/` — `identity.py`, `grants.py`, `guardians.py`, `learner_profile.py`, `book_permission.py`, `knowledge_access.py`, `model_access.py`, `audit.py` | 🟢 Apache-2.0 (same repo) | 🟢 **Guardian consent + audit trail already exist**; this is the K-12 shape prior passes priced as greenfield |
| LMS seam | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) `0ec24fe` | 🟢 **Apache-2.0** | 🟢 Ships **LTI 1.3 + AGS**; the only permissive component on this shelf that holds grade passback |
| Human approval gate | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) `main` `b90bd88` | 🟢 **MIT** 1 069 B | 🟢 `reviewGate.publishBlockedUntilApproved: true`, `autoPublishAllowed: false`, exercised by **25 test references** (pass 72, `Gap 323`) |
| Provider path | 🔴 **Supply your own** | — | 🔴 `AI-Teaching-Agent`'s contract declares `mode = MOCK_ONLY`, `safety.realLlmCalled = false` |

**The three joins, concretely:**

1. 🟢 **`ltijs` → `DeepTutor`.** Mount `ltijs` as the LTI 1.3 tool provider; map its launch claim `sub` (and `https://purl.imsglobal.org/spec/lti/claim/context`) onto a `multi_user/identity.py` principal. 🟢 **The identity model already exists, so this is a mapping, not a schema design.**
2. 🟢 **`DeepTutor` → `AI-Teaching-Agent` gate.** Route generated assessment artefacts through the contract's `WAITING_REVIEW` default; nothing reaches a learner unapproved. 🔴 **Attach at `cli/agent_entity_publish_review.py` and `cli/review_pre_approve.py` — and note both carry *zero* test references (`P830`, pass 72), which is exactly the publish-side seam an integration touches.**
3. 🟢 **Gate → `ltijs` AGS.** Only an approved score calls AGS `Score` publish. 🟢 **This is the audit chain a regulator asks for, end to end, with no closed component in it.**

🔴 **The one honest cost, now measured rather than assumed:** `DeepTutor` has **0 LTI, 0 xAPI, 0 Caliper, 0 SCORM, 0 OneRoster** paths in 3 763 files (word-bounded per `P831`). 🟢 **So join #1 is net-new code in every case.** 🔵 **`Gap 316(i)` — the real wiring cost of that hop — is still the highest-value unmeasured number on this shelf, and `P14-R` is where it should be paid once and recorded.**

### 🆕 `P26-R` — Local-first tutor for a jurisdiction that **bans student-facing AI**, with a teacher-facing control plane

🔵 **Why this pattern exists:** North America supplies two hard constraints this shelf had no recipe for — **NYC's one-year moratorium on student-facing AI through grade 8** and **Katy ISD's K-6 generative-chatbot ban with supervised access from grade 7**. 🟢 **Teacher-facing and administrative workflows sit outside both.**

| Layer | Component | Licence | Role |
|---|---|---|---|
| Authoring + grading | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | 🟢 MIT | 🟢 Teacher-facing only: labs, exams, grading workflows, human review. **No learner ever calls a model** |
| Local adaptive workspace | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) `f0142f2` | 🟢 **MIT** 1 068 B | 🟢 Runs **locally**, 10+ providers; deployed to *teachers* for material prep, not to learners |
| Delivery | 🟢 Existing LMS (Moodle / Open edX), **no AI in the learner path** | AGPL-3.0 | 🟢 Learners receive human-approved artefacts through the LMS they already use |

🟢 **The compliance claim is structural, not promissory:** there is no learner-to-model call anywhere in the topology, so the moratorium is satisfied by architecture rather than by policy text. 🟡 **Use `zijinz456/OpenTutor`, not the fork** — `adity982/OpenTutor` carries the same MIT payload and holder (*Zijin Zhang*) but is 8 commits behind; canonicality was settled by copyright holder this pass. 🔴 **`OpenTutor`'s own docs put multi-user/classroom mode out of scope**, which is a *feature* for this pattern and a blocker for `P14-R` — hence `DeepTutor` there and `OpenTutor` here.

### 🔴 `P27` — **Not published.** The ibl.ai shortcut, and why it is refused

🔵 **The temptation this pass had to resist.** [`iblai/os`](https://github.com/iblai/os) is 🟢 **MIT** (1 069 B, 1 516 files, `cd556237`) and it **already carries an LTI 1.3 configuration surface** — launch, login, deep-linking, JWKS. 🟢 On the licence field alone it looks like the fastest route to everything `P14-R` builds by hand.

🔴 **Refused on three measurements:**

1. 🔴 **The LTI implementation is not in the MIT repository.** The seam is a **1 664 B** wrapper importing `AgentLtiTab` from `@iblai/iblai-js` — 🟢 **ISC**, 🔴 **no `repository` declared on the registry**. Unforkable, unauditable, unpatchable.
2. 🔴 **There is no AGS.** Grade passback appears nowhere in the 1 516-file tree. 🟢 `P14-R`'s whole value is the auditable grade path; this supplies the launch and not the return leg.
3. 🔴 **The backend is an enterprise product.** `README.md` line 237: *"requires the ibl.ai backend platform for authentication, AI agent APIs, and data services … not included in this repository."* 🔴 Line 61 of the same file asserts *"no vendor lock-in — full ownership of the stack."*

🟢 **Recorded as a refused pattern rather than omitted, because the licence field alone would have sold it** — and `P832` (read the registry's `repository`, not just its `license`) exists because of this chain. 🟢 **ibl.ai remains a legitimate *integration* target where a client already owns the platform; it is not a component to build on.** 🔵 Full reasoning: `intel/open-gaps.md` `Gap 326` / `Gap 327`.

### 🟢 `P23` — carried, and its regional case strengthens again

🟢 **Unchanged in construction** (MCP-side grading with a human gate). 🟢 **The reason to run it now serves a fourth jurisdiction for a fourth legal reason:** 🟢 **Vietnam's 33/2026/QD-TTg names automated assessment as high-risk and has been in force since 2026-03-01** — the only in-force, education-specific high-risk designation this shelf has found anywhere. 🟡 **Korea's AI Basic Act (in force 2026-01-22) adds a one-year penalty grace period**, which makes 2026 the build year rather than the compliance year. 🟢 **North America's human-oversight mandates (Oklahoma, Maryland) and LATAM's 87 %-use / 26 %-framework gap are the other two.** 🟢 **One gate, four regions, four statutes — the strongest reuse argument on this shelf.**

## 🟢 Seventy-second pass, 2026-10-09 — `P14-R` and `P23` **get cheaper and more precisely scoped** now that the gate is measured; one pattern is **withdrawn** because its foundation has no licence

⏱️ **Fourth pass of this date.** Pass 71 closed earlier today (commit `1fe734a`). **Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `P23` — Policy-evidence grading gate (**re-priced down**, and it now serves four regions for four different legal reasons)

🔵 **What changed:** `Gap 323` closed. The gate is no longer "a component we think exists" — it is a contract-declared, test-exercised state machine.

```
AI-Teaching-Agent  (MIT, LICENSE 1 069 B, main b90bd88)
  ├── ai-workflows/phase2-grading-generation.contract.json   ← 3 200 B, the compliance artefact
  │     reviewGate.defaultGeneratedStatus      = WAITING_REVIEW
  │     reviewGate.publishBlockedUntilApproved = true
  │     reviewGate.autoPublishAllowed          = false
  │     safety.{realPublish,reviewBypassed,…}  = false  ×10
  ├── backend/grading_worker.py          ← produces      (3 test refs)
  ├── cli/review_batch.py                ← gates         (3 test refs)
  ├── cli/review_decision_note.py        ← gates         (6 test refs)
  ├── cli/review_detail.py               ← gates        (16 test refs)
  ├── cli/agent_entity_publish_review.py ← publish side  🔴 0 test refs — WRITE TESTS FIRST
  └── cli/review_pre_approve.py          ← publish side  🔴 0 test refs — WRITE TESTS FIRST
        │
        ├── REPLACE: mode=MOCK_ONLY, safety.realLlmCalled=false
        │     → your provider path (LiteLLM / Bedrock / Ollama per sovereignty need)
        └── ADD: LMS seam — none ships. Cvmcosta/ltijs (Apache-2.0, master 0ec24fe)
                 src/services/{grading,names-and-roles,deep-linking,dynamic-registration}
```

🟢 **Wire it:** take the gate and its contract as-is; **write tests against the two zero-reference publish-side modules before touching them**; replace the `MOCK_ONLY` provider with your own path; attach `ltijs` for grade return. 🟢 **Estimate moves to the cheaper pole** — the approval state machine, the artefact a registrar or auditor actually inspects, is already built and exercised. 🔴 **Two costs remain real:** the provider path, and the **LTI 1.3 + AGS wiring that no permissive component has ever carried** (`Gap 316(i)`).

🟢 **Why this pattern now sells in four regions on four rationales:** Korea's **AI Basic Act** (in force 2026-01-22) requires meaningful human intervention in education as a **high-impact** sector; **Chile and Mexico** data-protection law limits decisions made **solely** by automated processing; **EU** Annex III puts grading in high-risk (🔴 date contested — 2026-08-02 or 2027-12-02, `Gap 308`); and **US states** (Idaho, Oklahoma, Maryland, Virginia, plus Florida's BOG and 28 FCS institutions) require a written, auditable AI-use policy covering **academic integrity and grading**. 🟢 **The contract JSON is the deliverable that answers all four** — a policy you can diff, test and show.

### 🟢 `P14-R` — Mastery tutoring with an auditable grade path (**scope sharpened**)

🟢 Unchanged in shape — [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT, `main` `939eb0e`) supplies BKT mastery estimation, the tutoring dialogue, a document→courseware semantic compiler and a Bedrock in-region inference path. 🟢 **Now compose it with `P23`'s gate** rather than building an approval flow: OATutor tutors and estimates, `AI-Teaching-Agent`'s gate governs what reaches the gradebook. 🔴 **Carried risks unchanged:** OATutor's hardcoded `gpt-4o` default and **no Ollama path** (sovereignty served by Bedrock in-region, not local inference), and 🔴 **`P12-R` still deletes the decade-dead `ims-lti` dependency** rather than inheriting it.

### 🔴 `P-CRED` — Permissive credential issuance: **withdrawn before it was published**

🔵 **This pass set out to write a credential-issuance recipe** — the natural companion to `P23`, since a gated grade should terminate in a verifiable credential, and `intel/trends.md` has carried digital credentials as a live trend on two channels.

🔴 **It cannot be written permissively, and the census is why:**

| Candidate | Licence (payload) | Blocker |
|---|---|---|
| [`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) | 🔴 **No licence file** (141-file tree); README asserts MIT | 🔴 **No grant** — `Gap 325` |
| [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | 🔴 **AGPL-3.0** 33 820 B | 🟡 §13 network copyleft |
| [`mint-o-badges/badgr-server`](https://github.com/mint-o-badges/badgr-server) | 🔴 **AGPL-3.0** 34 519 B, ref `develop` | 🟡 Copyleft **and** OB 2.0 only |

🟢 **What is offered instead, honestly scoped:** 🟡 **`P-CRED-AGPL`** — compose `certo` (OB 3.0 + W3C VC, Ed25519 with a public verification endpoint) behind `P23`'s gate, **self-hosted for the client**, which is the same AGPL posture this shelf already priced for Open edX. 🔴 **Not available** if the client wants a Globant-operated multi-tenant credential service — there the answer today is a commercial issuer or a build. 🟢 **The moment `Gap 325` resolves, `ec-issuer` becomes the base**: it is the only implementation carrying **Open Badges 3.0 + European Learner Model + OID4VCI**, with 53 of 141 files tests and committed Ed25519 keypairs — 🟢 **the right spine for an EMEA learner-mobility engagement.**

🔵 **Recorded as a withdrawal rather than omitted,** because a pattern this shelf *would* recommend if the licence existed is useful intelligence, and because the blocker is a one-issue upstream ask rather than an engineering cost.

## 🟢 Seventy-first pass, 2026-10-09 — `P12` and `P14` are **revised from protocol builds into library swaps**, and three new patterns are added: MCP-side grading, a sovereign EMEA tutor, and an LLM-free adaptive substrate

⏱️ **Third pass of this date.** Pass 70 closed earlier today (commit `cf5c9bf`). **Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every component named below was licence-verified from payload this pass** (`agents/top.md`, `repos/foundations.md`). 🔴 **No pattern here names a component whose grant was not read as bytes.**

### 🟢 `P12-R` — **Revised.** Lift OATutor from LTI 1.1 to LTI 1.3 + AGS by **swapping the library, not writing the protocol**

🔴 **What `P12` said for several passes:** implement the LTI 1.3 launch-plus-AGS seam against a permissive component and record the effort — treating it as an unknown-size protocol build (`Gap 316(i)`).

🟢 **What this pass establishes:** the protocol is already implemented under Apache-2.0 and was committed to three days ago. **The pattern is now a replacement, and it is small.**

**Components**

| Role | Component | Licence | Pin |
|---|---|---|---|
| Tutor + mastery model + UI | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | `main` `939eb0e` |
| 🆕 LTI 1.3 tool provider | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** | 🔴 **npm `7.0.7`** — *not* a git ref |
| 🔴 **Removed** | `CAHLR/ims-lti` → `omsmith/ims-lti` | MIT | — |

**Wiring**

1. 🔴 **Delete `aws/lti-middleware/index.js`** (25 422 B) — it is LTI 1.1: `oauth_consumer_key` ×3, `replaceResult` ×1, zero `id_token`/`jwks`/`lineitem`/`client_id`/`deep_link`. 🔴 **Delete `public/lti-consumer-config.xml`** (`imslticc_v1p0` cartridge) and the `"ims-lti": "github:CAHLR/ims-lti"` dependency.
2. 🟢 Stand up `ltijs` `Provider`: `src/services/launch` + `services/oidc` + `services/keyset` for the 1.3 launch; `services/dynamic-registration` so platforms self-register instead of exchanging keys by email.
3. 🟢 Map OATutor's BKT mastery output to **`services/grading`** (AGS): a line item per lesson, a score per mastery update. `shared/lti-scopes.constants.ts` carries the scope strings.
4. 🟢 Use **`services/names-and-roles`** (NRPS) to populate the roster instead of OATutor's Firebase-side identity.
5. 🟢 Back it with `services/cache-manager` (**Redis**) and `services/database-manager` (**Mongo**) — both already in `ltijs`, so no new infrastructure decision.

🔴 **Three constraints that will bite in week one if unread:** 🔴 **`engines.node` is `">=24"`** — a Node 20 LTS platform will not run it. 🔴 **`"files": ["dist"]` with `dist/` uncommitted** — install from **npm**, never `github:`, or you reproduce the exact `prepublish` failure that created the `ims-lti` fork (`Gap 319`). 🟡 **npm `7.0.7` is ahead of the newest git tag `v7.0.1`** — pin the npm version.

🟢 **Why this is now the recommended path rather than pinning the fork:** pinning `9b712f6` fixes reproducibility and leaves OATutor's grade return on a **ten-year-dead** CoffeeScript library (`omsmith/ims-lti`, HEAD `2016-09-05`) speaking a superseded protocol. 🟢 **`P12-R` deletes that dependency outright.**

### 🟢 `P14-R` — **Revised.** The permissive graded-tutor stack, now with a human-approval gate in code

🟢 **This is the pattern that answers a US district mandate, and every component is permissive.**

| Layer | Component | Licence | What it contributes |
|---|---|---|---|
| Mastery model | `CAHLR/OATutor` | 🟢 MIT | Bayesian Knowledge Tracing |
| Tutoring dialogue | 🆕 OATutor `aws/aiAgentGeneration/` + `src/components/problem-layout/AgentChatbox.js` | 🟢 MIT | LLM tutor; `chatModel.js` gives **per-lesson model override** via `lesson.chat_model` |
| Courseware generation | 🆕 OATutor `schemas/learning-object.schema.json`, `documents/manifest.json`, `agent-logic.mjs` | 🟢 MIT | Document → learning-object compilation |
| Inference | 🆕 OATutor `providers/bedrock-provider.mjs` (`SEMANTIC_COMPILER_PROVIDER=bedrock`) | 🟢 MIT | **In-region** managed inference |
| 🆕 **Human-approval gate** | [`AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) — `grading_worker.py` → `review_batch.py` / `review_decision_note.py` / `agent_entity_publish_review.py` | 🟢 **MIT** | **No score reaches the LMS without a recorded human decision** |
| LMS seam | `Cvmcosta/ltijs` `services/grading` | 🟢 Apache-2.0 | LTI 1.3 + AGS |

🟢 **The ordering constraint is the whole point:** `grading_worker` produces a candidate score → the review CLI records an explicit human decision → **only then** does `ltijs` `services/grading` POST it. 🟢 **That sequence is what satisfies NYC's red tier (no AI grading), Oklahoma's and Maryland's human-oversight statutes, and Vietnam's automated-assessment high-risk class** — 🟢 **demonstrable in code, not asserted in a policy PDF.**

🔴 **Honest scoping caveat:** `AI-Teaching-Agent`'s own README declares automatic-grading productization **frozen**, so treat its review gate as a **proven pattern to re-implement**, not a drop-in service. 🟢 **The valuable part is the shape** — job → record → batch review → decision note → publish — **and it is readable under MIT.**

### 🆕 `P23` — MCP-side grading with a human gate, for a client who will not buy an LMS integration

🟢 **Shape:** skip LTI entirely. `AI-Teaching-Agent` (MIT) exposes `cli/dsl.py`, `grading_job_service.py` and the `review_*` CLIs as **MCP tools**, with its own `cli/mcp_audit.py` as the surface audit, fronted by this KB's existing **`mcp-allowlist-gateway`** pattern so only the reviewed-publish tool is callable.

🟢 **Why it exists:** two of the three distribution shapes measured this pass bypass the LMS (`intel/trends.md` trend 5). 🔴 **An LMS integration needs a procurement cycle; an MCP tool needs a laptop.** 🟢 **Use it as the four-week proof that produces the evidence for the `P14-R` business case.** 🔴 **Do not present it as a compliance deliverable** — without the LMS seam there is no gradebook of record, and 🟡 an agent that grades outside the institution's governance gate is the risk the trend section flags.

### 🆕 `P24` — Sovereign EMEA tutor, Article 4 ready, no data egress

| Layer | Component | Licence | Contribution |
|---|---|---|---|
| Tutoring platform | [`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** | Adaptive tutoring, avatar/voice/video, **`ar`/`fr`/`en`** |
| Inference | same — **Ollama** provider via `/api/v1/providers/*` | 🟢 BSD-3 | 🟢 **On-premise; no student data leaves the estate** |
| Governance | same — `/api/v1/self_regulation/*` | 🟢 BSD-3 | HITL evaluation **with export** — the Article 4 evidence artefact |
| Storage | same — PostgreSQL + **ChromaDB** | 🟢 BSD-3 | In-estate vectors |
| LMS seam (Python) | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) — `assignments_grades.py`, `lineitem.py`, `names_roles.py` | 🟢 MIT | LTI 1.3 + AGS in the platform's own language |

🟢 **Why this specific combination:** the platform is Python, so the Python LTI library avoids a second runtime; Arabic/French/English covers Gulf and Francophone engagements; Ollama answers data-residency without an AWS region decision. 🟢 **Article 4 (AI literacy) binds the institution today** — the self-regulation export is what evidences it.

🔴 **Two risks to price explicitly, not bury:** 🔴 **`pylti1.3`'s HEAD is `2022-11-21` — four years stale.** Adopting it means **owning the fork**; budget maintenance, or run `ltijs` in a Node sidecar instead and accept the second runtime. 🔴 **`open-tutor-ai-CE`'s HEAD is `2026-06-26` — 3½ months quiet**, and the EE delta includes an unbounded *"and more!"* (`verticals/solutions.md`). 🟢 **Re-read both before contracting.**

### 🆕 `P25` — Adaptive substrate that runs, and is testable, with **zero model spend**

🟢 **Components, one repo:** [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) (**MIT**, `main` `f0142f2`) — `services/block_decision/{engine,rules,preference,profile_mapper,cold_start}.py` as the scheduler, `services/spaced_repetition/fsrs.py` for review timing, `models/knowledge_graph.py` + `services/knowledge/graph_ops.py` for prerequisites.

🟢 **The trick that makes it a pattern:** `services/llm/providers/mock_client.py` ships alongside `anthropic_client.py` and `openai_client.py`. 🟢 **So the entire adaptive loop — cold start, block selection, FSRS scheduling, graph traversal — can be run, load-tested and demoed against the mock with no API key and no spend**, then switched to a real provider by configuration.

🟢 **Use it for:** a client who wants to see adaptivity before approving model budget; a CI suite that exercises pedagogy deterministically; a pilot in a jurisdiction whose data rules are unresolved. 🔴 **Correction to carry:** the project is promoted as *"10+ LLM providers"* — 🔴 **the tree holds two real providers and a mock. Do not repeat the "10+" figure.** 🟢 **Use `zijinz456`, not `adity982`** (a strict-subset fork, two weeks behind — `agents/top.md`).

### 🆕 `P26` — Plugin-shaped pilot: tutoring to a faculty cohort with no procurement cycle

🟢 **Component:** [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) (**MIT**, `main` `b391898`) — ships `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` **plus** a self-hostable FastAPI backend (`backend/Dockerfile`, `backend/app/courses.py`), with `README.zh.md` / `GUIDE.zh.md` alongside English.

🟢 **Shape:** distribute the tutor as a **Claude Code plugin** to a volunteer faculty cohort; collect usage and learning evidence from the self-hosted backend; use that evidence as the business case for `P14-R`. 🟢 **Bilingual docs make it the natural APAC pilot vehicle**, where three of this pass's eight new agents originate.

🔴 **Boundaries, stated so nobody oversells it:** 🔴 **no LMS seam, no gradebook of record, no AGS** — this is a pilot instrument, not a graded deployment. 🟡 And it is the shape that enters an institution **outside** its governance gate, so pair it with a written scope that says grades do not leave the pilot.

### 🟢 Pattern selection, in one table

| Client situation | Pattern | Why |
|---|---|---|
| US district under an AI-policy mandate (OH, OK, MD, NYC) | **`P14-R`** | Human-approval gate in code + AGS write-back |
| Existing OATutor / LTI 1.1 deployment to modernise | **`P12-R`** | Library swap; deletes a 10-year-dead dependency |
| EMEA, data-residency constrained, Article 4 live | **`P24`** | Ollama + HITL export + `ar`/`fr`/`en` |
| Will not fund an LMS integration yet | **`P23`** | MCP tools; four-week proof |
| Wants adaptivity demonstrated before model budget | **`P25`** | Mock provider; zero spend |
| APAC faculty pilot, no procurement appetite | **`P26`** | Plugin distribution, bilingual |

## 🟢 Seventieth pass, 2026-10-09 — `P14`: the first recipe on this shelf whose **pedagogical core is permissive and already written** — an MIT mastery-estimating tutor wired to a human-gated LTI 1.3 grade return; plus nine practices (`P819`–`P827`), three earned by instruments, three by licence anomalies and one by a retracted twenty-week reading

⏱️ **Second pass of this date.** Pass 69 closed earlier today (commit `abf91da`, 00:07 UTC). **Append-only: this section is new; nothing below it was rewritten.**

### 🆕 `P14` — A permissive **mastery-estimating tutor** with a human-gated **LTI 1.3 + AGS** grade return

🟢 **Why this recipe exists and why it is not `P12`.** 🔵 `P12` builds a **grading surface**: free-text work in, a model-proposed score, a teacher approval, a grade posted. 🟢 **`P14` builds the loop underneath it**: estimate per-skill mastery, choose the next problem from that estimate, and only then grade. 🔴 **Every prior recipe on this shelf had to specify the mastery model as *"build this part"*** — 🟢 **as of this pass it does not, because `CAHLR/OATutor` ships Bayesian Knowledge Tracing in-tree under MIT.**

🟢 **Every component licence-verified from payload this pass.**

| Role | Component | Licence | Verified |
|---|---|---|---|
| 🆕 **Mastery model + problem selection** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | `main` **`939eb0e`**; `LICENSE` **1 105 B**; **8 338 files**; `src/models/BKT/BKT-brain.js` + `problem-select-heuristics/{default,experimental}Heuristic.js` read from the tree |
| LTI 1.3 launch + AGS grade return | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) *(or a per-stack equivalent)* | 🟢 **Apache-2.0** | `master` **`3a192de`**; `LICENSE` **11 343 B** — 🟡 off-canonical by 14 B, resolved under `P804` (completed appendix, *"Copyright 2018 Turnitin, LLC"*) |
| Free-text grading core | [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) | 🟢 **Apache-2.0** | `main` **`5b96722`**; `LICENSE` **11 357 B** |
| Learner evidence stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | `main` **`cb794e4`**; **11 357 B** |
| Competency anchoring | [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🟢 **MIT** | **`develop`** `db41cc4`; **1 080 B** |
| Conformance gate (xAPI 2.0, Caliper 1.2, OneRoster 1.2) | [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | 🟢 **MIT** | `main` **`3596bb5`**; **1 080 B** |
| Article 50(2) structural marking | this KB's `compose/code/aiact-50-2-{marking,pack}` | 🟢 own code | 🟢 **23/23** and **27/27** |
| Signature seam (`P33`) | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | 🟢 **Apache-2.0** | `main` **`0a4fe8c`**; **11 357 B** |

🟢 **How it wires together:**

1. 🟢 **Take OATutor for the model, not the plumbing.** Its value is `src/models/BKT/BKT-brain.js` and the two problem-selection heuristics — a per-skill mastery estimate and a next-item decision derived from it. 🔴 **Its LMS seam is LTI 1.1**: `aws/lti-middleware/index.js` (25 422 B) signs with `oauth_consumer_key` and returns grades via `replaceResult`, and `public/lti-consumer-config.xml` is an `imslticc_v1p0` cartridge. 🟢 **Replace that seam; keep the model.**
2. 🔴 **Pin the fork before you quote.** `aws/lti-middleware/package.json` declares `"ims-lti": "github:CAHLR/ims-lti"` — **a GitHub fork resolved by branch name, with no tag and no sha.** 🟢 **Measured this pass: the fork is `master` `9b712f6` with 0 release tags; upstream `omsmith/ims-lti` is `master` `4df2936` with 24.** 🔴 **So it is an unreleased, diverged fork of a released library.** 🟢 **Pin `9b712f6` explicitly, or drop it with the 1.1 seam you are replacing anyway.** 🔴 **Never ship a client a `github:` dependency resolved by branch** (`Gap 319`).
3. 🟡 **Delete one of the two launch paths.** `old-lti-middleware/` is still in `main` beside `aws/lti-middleware/`. 🟢 **Choose, document, remove the other** — two launch paths in a graded system is an audit finding waiting to happen.
4. 🟢 **Put the LTI 1.3 tool in front.** OAuth 2.0 / JWKS launch validation; **AGS** (`Assignment and Grade Services`) for the score post; deep linking for item placement. 🔵 **This is the same port `P12` specifies, and the two recipes share it** — build it once, reuse it in both.
5. 🔴 **Gate the grade return on a recorded human approval.** 🟢 **Make it structural, not procedural:** the AGS post should be unreachable in code without an approval record carrying the approver's identity and a timestamp. 🔵 **In Oklahoma and Maryland this is law** — human oversight required, AI barred from high-stakes decisions about students — 🟢 **so the gate is a feature you can name in a bid, not overhead.**
6. 🟢 **Keep the two-pool isolation from `P12`** (`P812`): the LLM-blocking path and the LTI launch path must not share a worker pool, or one burst of grading stalls every launch.
7. 🟢 **Emit evidence as you go.** Every mastery update and every approved grade becomes an xAPI statement in `lrsql`, with skills referenced against an `opensalt` competency framework so the mastery estimate means something outside the tool. 🔵 **Gate the whole surface with `conform-ed` before delivery.**
8. 🔴 **Mark the generated text.** Any model-written feedback is synthetic content: run it through `aiact-50-2-marking`/`-pack` and declare the signature seam. 🔴 **Article 50's marking grace expires `2026-12-02`** — 🟢 and the same implementation answers **China's synthetic-content labelling** rules, which matters if the engagement is APAC.
9. 🟡 **Track two licences, not one.** 🟢 OATutor's **code is MIT**; its bundled problem content is **CC BY 4.0**. 🔴 **If the client ships the content, they owe attribution** — and if they replace it, the CC BY obligation disappears with it. 🟢 **Decide which, in writing, at the start.**
10. 🟡 **Price a re-host if the client is not on AWS.** The shipped middleware assumes Lambda (`aws-serverless-express`) and Firebase.

🟢 **Where this is sellable, by region, from this pass's measurements:**
- 🟢 **North America** — Oklahoma and Maryland **require** human oversight and bar AI high-stakes decisions; **Ohio** requires every district to hold an AI policy (`2026-07-01`). 🔵 OATutor's UC Berkeley provenance reads well in US higher ed.
- 🟢 **LATAM** — **assessment is the lowest-adoption use case** in the Digital Education Council's 30 000+ response survey, and **87%** of institutions already use AI somewhere (UNESCO IESALC). 🔵 `lti-ai-grader` already ships multi-language templates.
- 🟢 **EMEA** — only **16%** of 20 000+ teachers believe general-purpose AI improves outcomes, against **63%** using it. 🔵 A purpose-built, LMS-integrated, human-gated tool is the stated gap; AI Act readiness is the differentiator against the closed vendors.
- 🟡 **APAC** — **Korea's AI Basic Act names education inside "high-impact AI"** from January 2026. 🔵 `DeepTutor` (Apache-2.0, HKU) is the regionally-provenanced base if that matters to the buyer.

🔴 **What `P14` does not yet know:** the size of the LTI 1.3 port measured in real work (`Gap 316(i)` — **unmeasured, do not quote it**), whether `CAHLR/ims-lti` diverges from upstream (`Gap 319`), and whether **OATutor 2.0**'s GenAI chatbot layer — described in a Springer chapter, June 2026 — is in `main` at all (`Gap 321`).

### 🆕 Practices earned this pass

🟢 **`P819` — a `200` at `raw.githubusercontent.com/<repo>/master/<path>` does not prove a `master` branch exists.** 🔴 GitHub serves the **default branch** for the legacy ref `master` when the repo has none, with byte-identical content. 🟢 Measured with controls: `pguso/agents-from-scratch` (heads: `main` only) → `master/LICENSE` **`200`, 1 091 B, identical to `main`**, `bogus-xyz/LICENSE` → `404`; `24kchengYe/human-skill-tree` (heads: `master` only) → `main/LICENSE` → **`404`**. 🟢 **The aliasing is one-directional and specific to the legacy name.** 🟢 **Always resolve the branch with `git ls-remote --symref` (or `--heads`) before attributing a byte count to a branch.**

🟢 **`P820` — read the whole licence file, especially a short one.** 🔴 A **1 134 B** file whose first line says *"GNU AFFERO GENERAL PUBLIC LICENSE"* is a **grant by reference**, not the licence text, and the interesting terms live after it: `24kchengYe/human-skill-tree` dual-licenses `skills/*.md` **MIT-or-AGPL at the user's option** while keeping `app/` **AGPL-only**. 🔴 **A badge, an SPDX guess or a byte-count heuristic would each have missed a usable MIT harvest inside an AGPL repo.**

🟢 **`P821` — blobless clone, then one targeted fetch, settles a protocol question cheaply.** `git clone --depth 1 --filter=blob:none` → `ls-files | grep -iE 'lti|grade|outcome'` → **one** `raw` fetch of the single decisive file. 🟢 OATutor's LTI version settled in **two network operations** over an **8 338-file** tree. 🔴 Do **not** grep contents over a blobless clone — blobs fetch on demand and a content sweep costs real bytes; use `--depth 1` (full) for grep work.

🟢 **`P822` — a `-CE` / "Community Edition" suffix is a question about *parity*, never about the licence.** `open-tutor-ai-CE` is genuine **BSD-3-Clause** from payload; 🔴 what the non-community edition adds is unmeasured (`Gap 322`). 🟢 Verify the grant from bytes, then ask separately what the paid edition holds back.

🟢 **`P823` — determine an LTI version from payload signals, never from documentation.** 🔴 **LTI 1.1:** `oauth_consumer_key`, `oauth_signature`, `replaceResult`, and an `imslticc_v1p0` / `imsbasiclti_v1p0` cartridge XML. 🟢 **LTI 1.3 + AGS:** `id_token`, `jwks`, `client_id`, `lineitem`/`line_items`, `deep_link`. 🔵 The two are mutually exclusive in practice, so a single grep over the launch file is decisive.

🟢 **`P824` — a payload read beats a bibliographic record.** A ResearchGate entry listed *Open TutorAI* as **CC BY-NC-SA 4.0**, which would bar commercial use; the repository's `LICENSE` is canonical **BSD-3-Clause**. 🔴 **A paper's licence governs the paper, not the code it describes.** 🟢 Same rule already applied to vendor glossaries (Gibbon) — now it applies to academic records too.

🟢 **`P825` — discover licence-blind; decide on licence afterwards.** 🔴 A discovery query containing the token `MIT` cannot return AGPL projects, and for **twenty weeks** this shelf read that selection effect as an empty market. 🟢 **Query by capability** (`tutor`, `grading`, `knowledge tracing`, `LTI`, `adaptive`), **then read `LICENSE` bytes and decide.** 🔵 The licence-naming query is retained **only as a control**, where its constancy is the measurement.

🟢 **`P826` — follow a trending channel's roundups to the primary topic page before concluding a field is empty.** 🔴 The roundup layer of `github trending education AI` returns courses exclusively; 🟢 GitHub's own `ai-education` topic page, which those roundups cite, returned two real tutoring systems. 🔵 Prior passes read only the roundups and recorded *"zero systems."*

🟡 **`P827` — "run but do not redistribute" is a posture counsel confirms, not an assumption the architect makes.** 🟢 The clean split this pass measured — **copyleft systems of record, permissive delivery** — suggests taking a GPL SIS as infrastructure the client *operates* while owning only the delivery layer. 🔴 **AGPL and GPL diverge exactly here, and a SaaS wrapper is where the divergence bites.** 🟢 Confirm per licence **and** per deployment model, in writing, before the architecture depends on it.

### 🟢 Suites run this pass, and the one red is **proven pre-existing**

🟢 **Run directly (not under `unittest discover`, which mis-reports a self-executing script's `SystemExit: 0` as an error):**

| Suite | Result |
|---|---|
| `p370-gap-gate` | 🟢 **27/27** |
| `p471-gap-gate-language` | 🟢 **25/25** (132 s) |
| `aiact-50-2-pack` | 🟢 **27/27** (🟡 xmllint checks skipped — needs `--with-xmllint` plus `SCORM_SCHEMAS`) |
| `aiact-50-2-marking` | 🟢 **verified** — Article 50(2) span-level marking holds, 🔴 **signature seam declared and still NOT filled** (`P33`) |
| `p351-star-digit-sweep` | 🔴 **5 failures — pre-existing, not caused by this pass** |

🟢 **`p351`'s redness was isolated rather than inherited on trust.** 🔵 The suite was run against the **pristine pass-69 tree** (this pass's additions stashed) and against the tree with them:

| Measurement | Pristine (pass 69) | With pass 70 |
|---|---|---|
| failures | 🔴 **5** | 🔴 **5** — identical set |
| star-digit occurrences | **244** (threshold asks ≥ 254) | 🟢 **244 — unchanged** |
| unattributed occurrences | **74** | 🟢 **74 — unchanged** |
| the offending occurrence | `agents/trending.md:9512`, `'6.400 ★'`, pass 124 | 🟢 same occurrence at **`:9555`** — **shifted by exactly this pass's 43 inserted lines** |

🟢 **So this pass added zero star-digit occurrences** — which is the intended result, because it published no star count as a datum. 🔴 **The failing occurrence is pre-reset Spanish-era content (`'6.400 ★'` attributed to `pase 124`) carrying a measurement with no band and no date** — 🟢 **exactly what `p351` exists to catch, and it is still catching it.** 🔵 **Fixing it means editing history below this pass's section, which the append-only convention forbids without a declared correction** — 🟡 **recorded, not silently patched.**

## 🟢 Sixty-ninth pass, 2026-10-09 — `P12`: the shelf's **first recipe aimed at a measured market gap** rather than a standard — a wholly permissive **LTI 1.3 + AGS grading surface**, which six closed vendors sell and open source does not have; plus seven practices (`P812`–`P818`), three of them earned by instruments and two by corrections

⏱️ **First pass of this date (pass 68 closed 2026-10-08; the date rolled over during this pass's measurements, which are dated by their publication here). Append-only: this section is new; nothing below it was rewritten.**

### 🆕 `P12` — A permissive **LTI 1.3 + AGS human-in-the-loop grading surface**, zero copyleft

🟢 **Why this recipe exists, and it is not a standards gap — it is a market gap this pass measured.** 🔴 **Six commercial vendors** (EduGears AI, LearnWise, ibl.ai, campusmind.ai, Asyntai, edusageai) **sell AI grading over LTI 1.3 with AGS grade return behind a teacher-approval gate.** 🔴 **Open source has no cross-LMS equivalent:** the permissive exceptions are Moodle-only plugins, and the one real cross-LMS permissive component is on **LTI 1.1 / Basic Outcomes** (`Gap 316`, `Gap 317`). 🔵 **This is the capability with the least open competition and the most demand evidence in this KB** — LATAM alone shows **50% of students wanting AI-assisted feedback against 19% of faculty delivering it.**

🟢 **Every component below was licence-verified from payload this pass.**

| Role | Component | Licence | Verified |
|---|---|---|---|
| Grading core + prompt/model plumbing | [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) | 🟢 **Apache-2.0** | `main` **`5b96722`**; `LICENSE` **11 357 B** |
| LTI 1.3 launch + AGS grade return | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) *(or a per-stack equivalent)* | 🟢 **Apache-2.0** | `master` **`3a192de`**; `LICENSE` **11 343 B** — 🟡 **off-canonical by 14 B**, resolved under `P804`: the appendix is **completed** (*"Copyright 2018 Turnitin, LLC"*) rather than left as the `[yyyy] [name of copyright owner]` placeholder. 🟢 Genuine Apache-2.0 |
| Learner evidence stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | `cb794e4`; **11 357 B** |
| Competency anchoring | [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🟢 **MIT** | `db41cc4`; **1 080 B** |
| Conformance gate (xAPI 2.0, Caliper 1.2, OneRoster 1.2) | [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | 🟢 **MIT** | `3596bb5`; **1 080 B** |
| Article 50(2) structural marking | this KB's `compose/code/aiact-50-2-{marking,pack}` | 🟢 own code | 🟢 **23/23** and **27/27**, run this pass |
| Signature seam (`P33`) | [`THU-BPM/MarkLLM`](https://github.com/THU-BPM/MarkLLM) | 🟢 **Apache-2.0** | `0a4fe8c`; **11 357 B** |

🟢 **How it wires together:**

1. 🟢 **Replace the launch layer, keep the grading core.** `lti-ai-grader`'s value is not its LTI handshake — it is `aigrader.py` plus the prompt/template/model configuration and its operational hardening. 🔴 **Its handshake is one file (`lti-receiver.py`) speaking LTI 1.1 and returning grades via `replaceResult`.** 🟢 **Swap that one file for an LTI 1.3 tool: OAuth 2.0 / JWKS launch validation, and AGS (`Assignment and Grade Services`) for the score post.** 🔵 **The port surface is deliberately small, which is why this recipe is cheap** — measure it under `Gap 316(i)` before quoting.
2. 🟢 **Keep the two-pool FastCGI design, whatever the stack.** 🔴 *"AI evaluation requests can remain blocked waiting for an LLM response for several minutes. If `lti-receiver.py` shares the same small `fcgiwrap` pool, a burst of simultaneous evaluations can consume every worker and prevent the next LTI activity from loading."* 🟢 **Isolate the LLM-blocking path from the launch path** (`P812`).
3. 🟢 **Gate every score on a human.** 🔵 The closed vendors advertise teacher approval before an AGS post, 🟢 **and it is also the single cheapest hedge against Annex III**: a score a teacher approves is decision support, not automated assessment. 🔴 **Never post an unreviewed AI score to a gradebook.**
4. 🟢 **Write the *process*, not just the score.** Emit xAPI statements for the submission, the AI feedback and the teacher's decision into `lrsql`; anchor the criteria to CASE competencies in `opensalt`. 🔵 **This is what makes the deliverable serve process assessment** (the OECD *metacognitive laziness* trend) 🔴 **and it is also what puts `Gap 310` in play — treat the evidence stream as profiling and design for the conservative reading.**
5. 🟢 **Mark the generated feedback.** Run the AI feedback text through this KB's `aiact-50-2-marking`, pack it with `aiact-50-2-pack`. 🔴 **This yields a *structural* mark, not a signed one.** 🟢 **Fill the `P33` seam with MarkLLM if a cryptographic mark is required** — 🔴 **and until it is filled, present marking as readiness, never as compliance** (`P803`).
6. 🟢 **Gate the integration with `conform-ed` in CI**, so an LMS-side change surfaces as a conformance failure rather than a silent grade-passback regression.

🔴 **Licence posture: zero copyleft.** 🟢 Apache-2.0 and MIT throughout; the student record is never forked or linked — the tool reaches the LMS **only** over LTI 1.3 across a process boundary (`P736`, `P809`). 🟢 **Deliverable code can be kept closed.**

🔴 **What this recipe does not do:** 🔴 **it does not roster.** OneRoster is absent from the permissive substrate (`Gap 315`); this recipe consumes the roster the LTI launch hands it and nothing more. 🔴 **It does not own the student record**, and must not try to.

### 🆕 `P812` — an LLM call in a request path is an **operational hazard with a known shape**: isolate its worker pool

🟢 **Earned from payload, not from theory.** `lti-ai-grader`'s nginx design uses **two separate FastCGI pools** for exactly one reason: an LLM response can block a worker **for minutes**, so a burst of evaluations starves the pool and the *next launch* fails — 🔴 **the user-visible symptom is not "grading is slow", it is "the activity won't load."**

🔵 **Generalised:** any synchronous AI deliverable that shares a worker pool between its **LLM path** and its **control path** will fail at the control path first, and will be misdiagnosed. 🟢 **Separate the pools, or make the LLM path asynchronous.** 🟢 **Applies to `P11` and `P12` alike.**

### 🆕 `P813` — an unverified row in a verified table must be **marked or removed**, and the mark is a **work item**, not a disclaimer

🔴 **Earned inside this pass, by catching itself.** `P12` was first drafted carrying its LTI 1.3 library row as *"verify before use — not re-read this pass"*, beside six rows each with a sha and a byte count. 🔵 **A reader takes a table's authority as uniform**, so one unmarked unverified row borrows the credibility of every verified one.

🟢 **The mark did its job: the row was then probed before publication**, and the probe was not a formality — it returned **Apache-2.0 at 11 343 B**, **off-canonical by 14 B**, which needed `P804` to resolve (appendix completed with *"Copyright 2018 Turnitin, LLC"*, not a different licence). 🔵 **Had the row shipped unmarked, that 14-byte discrepancy would have shipped as a verified fact.**

🟢 **The practice, in two parts:** 🟢 **(i)** never let an unverified row sit beside verified ones without a visible mark; 🟢 **(ii)** **treat the mark as a queue** — it is there to be cleared before publication, not to excuse the gap. 🔴 **A mark that survives publication unexamined is worse than an omitted row**, because it looks like diligence. 🔵 **`P811`'s sibling: that one says what to do when a path 404s; this one says what to do when a path was never probed.**

### 🆕 `P814` — a blobless clone is the **default** instrument for tree questions; a full shallow clone is the default for **content** questions

🟢 **Measured this pass.** `git clone --depth 1 --filter=blob:none` enumerated **5 846 files** on a repository `api.github.com` refuses, **with no API access** — 🟢 and it closed `Gap 303` and `Gap 311(a)` on first use, after two passes of path-guessing had produced only 404s.

🔵 **But the two modes are not interchangeable:** 🔴 **a blobless clone fetches blobs on demand, so `grep -r` over one quietly downloads the tree** — the worst of both. 🟢 **Tree shape, path existence, tag and changelog layout → blobless. Content greps → `--depth 1` without the filter.** 🟢 **`Gap 313`'s three-component grep used the latter and cost three small clones.**

### 🆕 `P815` — a `403` from an API is a claim about **a resource**, not about **a host**, until a second endpoint is tried

🔴 **The correction this practice is named for.** Passes ≤68 recorded *"`api.github.com` re-measured `403`"* and drew the consequence *"no star counts, nothing ranked by popularity."* 🟢 **The consequence was right; the cause was wrong.** 🟢 **Measured this pass:** `/rate_limit` → **`200`, authenticated, 15 000/hr core**; an **attached** repo → **`200`** with full payload; a **third-party** repo → **`403`** with the message *"GitHub access to this repository is not enabled for this session."*

🔵 **So it was a per-repository authorisation boundary all along.** 🟢 **The practice: before recording a host as blocked, probe an endpoint that takes no resource argument** (`/rate_limit`, `/meta`, a status path). 🔴 **An instrument map with a wrong cause in it mis-prices every remedy that depends on it** — here it had been hiding the fact that this KB's *own* repository is fully API-readable.

### 🆕 `P816` — a **canonical byte count is a check, not an identification**

🔴 **Earned from a near-miss this pass.** FenixEdu's `LICENSE` is **7 652 B** and OpenEduCat's is **8 241 B**; 🟢 **both are LGPL-3.0**, and the difference is a prepended copyright pointer. 🔵 **Reading only the length would have made them two different licences.**

🟢 **The practice:** 🟢 **always read the first lines; use the length to confirm.** The canonical lengths this shelf relies on — **MIT 1 080–1 118**, **Apache-2.0 11 357**, **GPL-3.0 ~35 100**, **LGPL-3.0 7 652** — 🟢 **are strong corroboration when the header already matches** (this pass read Apache-2.0 at **11 357** on four independent repositories, and MIT at **1 080** on two), 🔴 **and prove nothing on their own.** 🔵 **`P805`'s converse: that one says a file too small to hold a grant is a name; this one says a file of the right size is still only a candidate.**

### 🆕 `P817` — a test harness that reports **zero tests** is a finding about the **harness**

🔴 **Measured twice this pass.** This KB's suites are **plain scripts** — `python3 test_x.py` from inside their directory. 🔴 **`pytest` is not installed here** (`No module named pytest`), and 🔴 **`python3 -m unittest` reported `Ran 0 tests … OK` for one suite and `FAILED (errors=1)` for the other.** 🟢 **Invoked correctly, both ran green: 23/23 and 27/27.**

🔴 **`Ran 0 tests … OK` is the dangerous one** — it is a **pass-shaped** result that measured nothing. 🟢 **The practice: a green with a zero count is a red.** 🔵 **And the README's board census — *"41 unread"*, attributed to `python3 -I` implying `-P`** — 🔴 **was an artefact of the same class of error, so the shelf does not currently know how many of its 106 suites pass** (`Gap 318`). 🟡 **Scope discipline: this pass ran two suites and claims two.**

### 🆕 `P818` — when a channel returns nothing for **twenty weeks**, suspect the **query**, and change one term to test it

🔴 **The control query** (`top open source AI agents {industry} {year} github MIT`) **has been empty for twenty consecutive weeks.** 🟢 **A targeted query using the industry's own vocabulary — `LTI`, `tutoring`, `grading`, `Moodle`, `Canvas` — returned a populated field on the first attempt**, and with it this pass's only real agent find and its central market finding.

🔵 **The diagnosis:** `github MIT` searches **how software is licensed**; the industry names itself by **what it integrates with**. 🔴 **A twenty-week null is more likely an instrument fault than an empty market**, and recording it twenty times does not test it. 🟢 **The practice: hold the industry term fixed and vary the *channel* term; if the field populates, the series was measuring the query.** 🟢 **Keep the null series — it is still the honest record of that channel — but stop reading it as a fact about the field.**

## 🟢 Sixty-eighth pass, 2026-10-08 — `P11`: the shelf's **first dated recipe**, because its deadline is **`2026-12-02`** and it is built from code this KB already wrote; plus seven practices (`P805`–`P811`) earned by this pass's measurements, two of them by errors caught before publication

⏱️ **Twenty-second pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🆕 `P11` — Article 50(2) marking readiness, **deadline `2026-12-02`**, zero copyleft

🔴 **Why this recipe has a date on it.** Regulation (EU) 2026/1744 deferred Annex III high-risk to
`2027-12-02` but **left Article 50 untouched**. 🔴 **Providers of generative AI systems placed on the
EU market before `2026-08-02` must have machine-readable marking in place by `2026-12-02`** — eight
weeks from this pass. 🔵 Systems placed from `2026-08-02` onward had **no grace at all**.

🟢 **Who this is for:** any edtech provider (or any Globant client shipping a generative education
feature into the EU) whose product predates August 2026. 🔵 **Deployers are a different role with
different duties — establish which the client is before quoting** (`P803` applies: this is Article 50
transparency, **not** a conformity assessment).

🟢 **Components, every grant read from payload on this shelf:**

| Step | Component | Licence | Why this one |
|---|---|---|---|
| 1. Exposure scan | 🟢 **this KB's `compose/code/aiact-50-2-exposure`** | 🟢 in-repo | Determines which surfaces emit generated content at all — the question that sizes the work |
| 2. Span identification | 🟢 **`compose/code/aiact-50-2-spans`** | 🟢 in-repo | Locates the generated spans inside mixed human/AI output |
| 3. Marking | 🟢 **`compose/code/aiact-50-2-marking`** | 🟢 in-repo | Applies the machine-readable mark; ships `fixtures-provenance-policy.md` |
| 4. Packaging + schema | 🟢 **`compose/code/aiact-50-2-pack`** (`aiact-50-2.xsd`) | 🟢 in-repo | Makes the marking record validatable rather than asserted |
| 5. Evidence store | 🟢 [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 **Apache-2.0** | Self-hostable xAPI LRS — the audit trail lives on the client's infrastructure, which EMEA sovereignty requires |
| 6. Conformance check | 🟢 [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | 🟢 **MIT** | Its `package.json` **already stands up `lrsql`** (`lrsql:up`, `lrsql:wait`, `lrsql:auth:check`) — step 5 and step 6 are one toolchain |
| 7. Competency anchoring | 🟢 [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🟢 **MIT** | Ties marked output to the competency it claims to serve, so the record answers *what was taught*, not only *what was generated* |
| 8. Platform integration | 🟡 **LTI 1.3** into the LMS/SIS | 🟢 permissive tool-side libs (`P766`) | 🔴 **The only lawful way to touch the copyleft tier** — see `P809` |

🟢 **Zero copyleft components. This is the shelf's third zero-copyleft recipe** (after `P8` and
`P10`) and the first with a **statutory deadline** attached.

🔴 **Three refusals built into the recipe, because each is one short step away:**

1. 🔴 **`conform-ed` output is not certification** (its own README says it is *not* a certification
   body). It evidences that you speak xAPI/QTI/LTI correctly.
2. 🔴 **None of this is a conformity assessment.** Article 50 transparency and Chapter III high-risk
   are **different regimes with different assessors** (`P803`). 🟢 Delivering `P11` does **not**
   advance the client's 2027 Annex III file beyond supplying substrate evidence.
3. 🔴 **Do not sell `P11` as "AI Act compliance".** It is **one article, one paragraph, one
   deadline**. 🟢 Say exactly that; it is sellable on its own.

🟢 **Sequencing advice, which is the part a client will actually thank you for:** run `P11` now
against the December date, and use the **sixteen-month Annex III deferral** to build the oversight
layer (`P10`, `P8`) calmly rather than under assessment pressure. 🔴 **`P808`: deferred is not
cancelled.**

### 🆕 `P805` — a licence file too small to contain a grant is a **name, not a licence**

🔵 **Measured:** `frappe/education` `[develop]` ships `license.txt` at **19 bytes**, reading in full:
**`License: GNU GPL V3`**. 🔴 **GPL-3.0's text is ~35 100 B.** 🔴 There is **no manifest licence key**
(`package.json` is `"private": true`; `pyproject.toml` has no licence line) and **no README
mention** — so the 19 bytes are the repository's **entire** licence evidence.

🟢 **The practice:** compare the licence payload's byte count against the canonical count for the
licence it names. 🔴 **An order-of-magnitude shortfall means the file *names* a licence without
*conveying* it**, and the question for counsel is whether a bare name grants anything.
🟢 **Operationally:** record it as the named licence (**assume GPL-3.0 and its obligations** — the
conservative reading), 🔴 **never as "permissive-unknown"**, and 🟡 **raise it in writing** before any
code is written against it (`Gap 312`).

🔵 **Why this is not pedantry:** the byte count is what catches it. A sweep that records *"licence:
GPL-3.0, present"* passes this repository and a sweep that records *bytes* does not.

### 🆕 `P806` — `refs/pull/N/head` is readable when `api.github.com` is not

🔵 **Measured:** `git ls-remote <repo> 'refs/pull/*'` returned **27 refs** on `arqueon/certo` and
`refs/pull/4/head` resolved to **`c62d8c9`**, in a session where `api.github.com` returns **`403`**.
🟢 **`raw.githubusercontent.com` then served the README at that bare sha** (15 618 B).

🟢 **The practice:** when a channel attributes a capability to a pull request, **do not stop at
`P786` ("a PR is a proposal")** — open the proposal. 🔵 Two refs, two readings: the **default ref**
tells you what a client would consume; the **PR head** tells you whether the capability exists at
all.

🔴 **And read the sizes against each other.** `arqueon/certo`'s PR-head README (**15 618 B**) is
*smaller* than its `main` README (**16 582 B**). 🟢 **A PR branch behind its own default branch is
stale or superseded, not pending** — which is a conclusion the default ref alone cannot support.

### 🆕 `P807` — `DNS_BLOCKED` is a fourth instrument state, and it is the one that touches the law

🔵 **Measured:** `eur-lex.europa.eu`, `digital-strategy.ec.europa.eu` and
`artificialintelligenceact.eu` **all failed DNS resolution** while `raw.githubusercontent.com` and
`api.github.com` resolved normally. 🟢 **The instrument states this shelf now distinguishes:**
`403` (refused) · `SCOPE_DENIED` (refused, allow-list named) · **`DNS_BLOCKED` 🆕** (host
unresolvable) · non-measurement (not attempted).

🟢 **The practice, and it is a publication rule rather than a probe rule:** 🔴 **a regulatory claim
that cannot be checked against primary text is published with its channel count attached, or not
published.** 🔵 This pass's AI Act correction carries **"four independent secondary channels in
agreement"** and names the single-channel items it refuses to build on. 🟢 **A gap is opened so a
later pass with DNS closes it in one fetch** (`Gap 308`).

🔵 **The asymmetry is the thing to remember:** this session can verify **code** to the byte and
cannot verify **statute** at all. 🔴 Those two confidences must never be reported in the same voice.

### 🆕 `P808` — deferred is not cancelled, and the surviving obligation is where the budget goes

🔵 **Measured:** Annex III high-risk moved `2026-08-02` → **`2027-12-02`**; Article 50 **did not
move**, and its 50(2) marking grace expires **`2026-12-02`**.

🔴 **Two symmetrical errors, and this pass caught the shelf making the first one:** pass 67 reported
an obligation as **live** that was deferred (a client would have bought a conformity assessment
sixteen months early); the opposite error reads the deferral as **relief** and builds nothing.

🟢 **The practice:** when a regime slips, re-read it **article by article** and find what *didn't*
slip. 🟢 **That is where the near-term deliverable is** — here, Article 50(2) on an eight-week clock,
which is exactly where this KB's own code tier already sits. 🔵 **A slipped deadline reallocates
work; it does not remove it.**

### 🆕 `P809` — the grant follows the **author class**, not the functional layer

🔵 **Measured across the shelf's layers:** standards bodies and alliances publish **permissively**
(Ed-Fi DMS **Apache-2.0, 11 357 B**; 1EdTech OpenCASE **Apache-2.0**; OpenSALT **MIT**; the xAPI-LRS
tier); sector product communities publish **copyleft** (this pass's system-of-record tier: **5 of
5**); credential issuers are **AGPL-3.0 to a repo**.

🔴 **This replaces pass 67's framing** ("the registry is permissive, the system of record is not"),
which **this pass's own tier refutes**: Ed-Fi DMS *is* a system of record and *is* Apache-2.0.

🟢 **The practice:** use author class as a **prior** — it predicts the grant before you read a byte,
and it tells you which side of the **LTI 1.3** boundary (`P736`) to build on: **on the substrate,
beside the product.** 🔴 **A prior is not a substitute for the payload read**; it tells you what to
expect and how surprised to be.

### 🆕 `P810` — a substring licence grep fails two ways: **sub-word** and **homonym**

🔴 **Both were caught this pass, and the second would have been the pass's false headline.**

| Reported | Actually | Class |
|---|---|---|
| `Apache 2` in `OS4ED/openSIS-Classic` README | 🔴 **`Apache 2.4 or above`** — the **web server**, under *Installation* | 🔴 **homonym** |
| `MIT` in `rosariosis` README | 🔴 **`ad`MIT`tance`** | 🔴 **sub-word** |
| `MIT` in `GibbonEdu/core` README | 🔴 **`sub`MIT`ting issues`** | 🔴 **sub-word** |

🟢 **The practice:** 🟢 use **word boundaries** (`\bMIT\b` — re-run gave **zero** hits in both
repositories); 🟢 for Apache, **require the licence form** (`Apache-2.0`, `Apache License`) and never
the bare `Apache 2`, because `Apache 2.x` is the **commonest web server on earth** and appears in
every LAMP install guide; 🔴 **and never let a prose grep stand in for a payload read.**

🔴 **The stakes, stated concretely:** trusting the first sweep would have published **openSIS as a
permissive system of record** — the inverse of this pass's actual finding, and the sort of error a
client builds on.

### 🆕 `P811` — 404 on every conventional licence path is **"read the README"**, not "no licence"

🔵 **Measured:** `OS4ED/openSIS-Classic` `[master]` returns **404** for `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `license.txt` and `COPYING`. 🔴 A sweep stopping there records *"no licence"*.
🟢 **Its README's own `## License` section points at `docs/License.txt`**, which served **17 286 B**
of **GPL-2.0** (*"Version 2, June 1991"*, BOM-prefixed).

🟢 **The practice:** on a conventional-path miss, **read the README's licence section and follow its
link** before recording an absence. 🔴 **"No licence file" and "licence in a non-standard path" have
opposite consequences** — the first means *no grant, do not build*; the second means *GPL-2.0, build
accordingly*.

🟡 **And a refinement to `P804`:** this GPL-2.0 payload is **17 286 B** while `rosariosis`'s is
**15 214 B** — same licence, same version line, different bytes, because openSIS's copy is
**reflowed and BOM-prefixed**. 🟢 **An off-canonical byte count is a question with more than one
answer** — a different copyright holder (`P804`) *or* a reformatted text. 🔴 **Byte count flags a
payload for reading; it never identifies one by itself.**


## 🟢 Sixty-seventh pass, 2026-10-08 — `P10`: the shelf's **second zero-copyleft recipe**, and the first that answers *what the evidence proves* rather than only *what happened*; plus three practices (`P802`–`P804`) earned by this pass's instrument states

⏱️ **Twenty-first pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **Rule applied, unchanged (`P759`/`P800`):** every named component has a **licence file read as
bytes** and a **HEAD pinned**, and no component enters a recipe on a README claim. 🔴 **A recipe
naming a prose-only grant is a proposal with an unpriced legal step in it.**

### 🆕 `P10` — Competency-anchored learning evidence, **MIT + Apache-2.0 throughout**

🟢 **The gap it fills.** `P8` (pass 66) built an Apache-2.0 evidence spine that records **what
happened** — statements, actors, review events. 🔴 **It could not say what any of it proved**, because
the competency layer was unread. 🟢 **`P10` adds the semantic anchor: every statement points at a
competency with a stable CASE identifier**, so the record answers *this learner demonstrated this
competency, on this evidence, reviewed by this person, on this date.*

🟢 **It is the second pattern on this shelf with no copyleft component anywhere**, and therefore the
second that can ship **inside** a closed client deliverable.

🟢 **It is also the direct answer to this pass's two strongest market signals:** 1EdTech naming
**digital credentials as the mechanism for skills-based learning and hiring**, and the **EU AI Act's
four-limb high-risk test**, whose limbs 1 and 4 (evaluates learners; influences access to
qualifications) are exactly the decisions this record makes auditable.

| Layer | Component | Grant (payload, bytes) | Pin |
|---|---|---|---|
| **Competency registry (default)** | [`opensalt/opensalt`](https://github.com/opensalt/opensalt) | 🟢 **MIT**, 1 080 B, © 2016 Public Consulting Group | **`develop`** · **`db41cc4`** 🆕 |
| **Competency provider (Postgres path)** | [`infosign/compeito`](https://github.com/infosign/compeito) | 🟢 **Apache-2.0**, 10 759 B + `pyproject.toml` | `main` · **`0656e10`** 🆕 |
| **Framework authoring UI** | [`1EdTech/OpenCASE`](https://github.com/1EdTech/OpenCASE) | 🟢 **Apache-2.0**, 11 264 B ⚠️ `P804` | `main` · **`97d0373`** 🆕 |
| Tool launch from the LMS | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0, 11 361 B | `master` · `0ec24fe` |
| Statement emitter | [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | 🟢 Apache-2.0, 11 358 B | **`3.x`** · `bbc3f9d` ⚠️ `P793` |
| Evidence store | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0, 11 357 B | `main` · `cb794e4` |
| Assessment delivery | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 MIT — 🟢 **1EdTech Certified**, QTI 3 Basic + Advanced Delivery | per `agents/trending.md` |
| Rostering | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 Apache-2.0, 10 173 B | `main` · `6de5476` |
| **Conformance regression** | [`conform-ed/conform-ed`](https://github.com/conform-ed/conform-ed) | 🟢 **MIT**, 1 080 B | `main` · **`3596bb5`** 🆕 |
| Orchestration | **LangGraph** | 🟢 MIT | per `agents/top.md` |
| LMS (optional, remote) | **Moodle / Canvas / Open edX** | 🔴 GPL/AGPL — **service, never a dependency** | deployment, not linkage |

🟢 **Wiring, concretely:**

1. **Define.** Load the client's standards into **OpenSALT** as CASE frameworks. 🟢 **The import path
   is measured, not assumed:** `compeito`'s CLI reads **OpenSALT-compatible CSV** and pulls
   frameworks straight from a live endpoint —
   `import case --tenant {uuid} --url https://opensalt.net/ims/case/v1p0/CFPackages/{id}` — and
   also takes `xlsx`, which is the format a ministry's standards actually arrive in. 🔵 Use
   **OpenCASE**'s visual editor when the client authors frameworks rather than importing them.
2. **Launch.** `ltijs` receives the **LTI 1.3** launch from the LMS (remote, never linked) and
   yields verified context: learner, course, role.
3. **Deliver.** `qti3-item-player` renders the assessment item. 🟢 **This is the one externally
   certified component in the recipe** — the only place the word *certified* is literally true.
4. **Emit, anchored.** `TinCanPython` writes an **xAPI statement per meaningful event**, and 🟢 **the
   statement's object or context carries the CASE competency URI** returned by the registry.
   🔵 **That single field is what distinguishes `P10` from `P8`:** the evidence is self-describing
   and survives the LMS it was produced in.
5. **Store.** `lrsql` persists statements — **SQLite 3.42 embedded for a pilot, Postgres 14 for
   production**, same binary.
6. **Review.** A **LangGraph** node holds the decision. 🔴 **Anything that would become a grade, a
   placement, a proctoring flag or a qualification gate stops here** — those are limbs 1–4 of the
   EU test — and the **human review event is itself written as an xAPI statement**.
7. **Prove it still works.** 🟢 **`conform-ed` in CI**: its `lrsql:up` / `lrsql:wait` /
   `lrsql:auth:check` scripts stand up the very store in step 5, and its `qti:coverage:report` /
   `qti:delivery:report` scripts measure the step-3 player against a QTI corpus. 🔵 **So the recipe
   ships with a regression harness for its own interop surface** — which no prior pattern here had.

🔴 **What `P10` does NOT do, priced explicitly:**

| Not included | Why | Lawful shape |
|---|---|---|
| 🔴 **Issuing a badge or verifiable credential** | 🔴 every issuer on this shelf is **AGPL-3.0** | **`P9`** — arm's-length hosted issuer, or write one |
| 🔴 **Aggregating into a CLR 2.0 record** | 🔴 **no verifiable implementation on any default ref** (`Gap 301`) | build, or wait |
| 🔴 **EU AI Act conformity assessment** | 🔴 **different regime from standards conformance** (`P803`) | name the assessor; this recipe builds the technical file |
| 🟡 **1EdTech certification of the CASE tier** | 🟡 OpenCASE is *"ready for"*, COMPEITO *"working toward"* | price the certification step |

🟢 **Effort, honestly banded: 8–10 weeks** for a single-tenant pilot (framework import is the
variable — a clean CSV is days, a PDF standards corpus is weeks), **12–16 weeks** multi-tenant with
`conform-ed` wired into CI and a documented AI Act technical file. 🔴 **Add discovery, not an
estimate, for anything touching issuance.**

🟢 **Regional fit:** **North America** — state competency registries, and OpenSALT is the codebase
1EdTech's own CASE Registry is based on. **EMEA** — the five national instruments read this pass are
curriculum-and-competence programmes (Italy, Ireland, Slovakia, France, Czechia), which is what this
models. **LATAM** — workforce reskilling needs the competency-to-occupation join, and OpenSALT
carries jobs and pathways natively. **APAC** — the per-jurisdiction policy nodes go in step 6.

### 🆕 `P802` — `SCOPE_DENIED` is a third instrument state, distinct from `403` and from non-measurement

🔴 **Earned this pass.** `api.github.com` has now failed three ways across four passes, and the
remedies are different: passes 64–65 recorded a **`403`** (gateway refusal), pass 66 recorded a
**non-measurement** (the probe was never issued), and this pass the GitHub tooling answered
**`Access denied: repository … is not configured for this session`** — an **allow-list of two
repositories**, naming them.

🟢 **The rule:** record *which* refusal, with its own words, never a generic "unavailable".
🔵 **`P798`'s lesson generalises** — the instrument's limit must not be published as the subject's
property, and *three different limits* must not be published as one. 🟢 **Practical consequence:**
`SCOPE_DENIED` is **not** fixable by waiting or retrying (unlike a rate-limit `403`) and **is**
fixable by attaching a repository — so it changes what a later pass should attempt, which is the
only reason an instrument state deserves a number.

### 🆕 `P803` — *conformance* and *conformity* are different regimes; never let the shared word bridge them

🔴 **Earned this pass, and it is the highest-consequence practice of the three.**

| | Standards **conformance** | AI Act **conformity assessment** |
|---|---|---|
| Authority | 1EdTech / ADL specifications | 🟢 EU AI Act, Annex III |
| Question | does it speak QTI/xAPI/LTI correctly? | is this high-risk AI system lawful to place in service? |
| Assessor | certification body — 🔴 or a **non-accredited harness** | 🟢 internal assessment or third-party audit |
| Timing | any time | 🔴 **before placing on market / putting into service** |

🟢 **The rule:** when a component's name or README contains *conform*, state which regime it serves
**in the same sentence**. 🔵 `conform-ed` says of itself that it is **not a certification body** and
produces **assessments, not official certification** — 🟢 **quote that, don't paraphrase it.**
🔴 **Never write that a `conform-ed` run contributes to AI Act compliance without naming the
assessor it does not replace.**

### 🆕 `P804` — an off-canonical Apache byte count is a question about the **copyright holder**, not a defect

🟢 **Earned by two rows this pass.** This shelf reads the canonical Apache-2.0 `LICENSE` at
**11 357 B**. Two new Apache components were neither that size nor each other's:

| Repo | bytes | Δ | APPENDIX | Holder line |
|---|---|---|---|---|
| canonical (e.g. `Data-Management-Service`) | 11 357 | — | 🟢 present | varies |
| `1EdTech/OpenCASE` | **11 264** | −93 | 🟢 present | 🔴 **`[yyyy] [name of copyright owner]` — unfilled** |
| `infosign/compeito` | **10 759** | −598 | 🔴 **removed** | 🟢 **`Copyright 2026 Infosign, Inc.`** |

🟢 **The rule:** when an Apache payload is off-canonical, **diff it and read the tail** before
recording anything. 🟢 **The grant is almost never the issue** — Apache-2.0 grants from the owner
whether or not the appendix names them. 🔵 **What changes is whether `P184` (holder/licence pairing)
can be run at all**: an unfilled placeholder means there is **no holder to pair**, so `P184` returns
*not applicable* rather than *clean*. 🔴 **Recording that as "clean" is the error this practice
exists to prevent.**

🟡 **And the counter-intuitive corollary, worth keeping:** provenance does not predict grant
completeness. 🔴 **The official standards-body repository left its holder as a template
placeholder; the community implementation named its own.**


## 🟢 Sixty-sixth pass, 2026-10-08 — the shelf's **first pattern with no copyleft component anywhere** (`P8`), and the AGPL credential fence priced into the **two lawful shapes** that remain (`P9`)

⏱️ **Twentieth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **Rule applied to both recipes (`P759`/`P800`):** every named component has a **licence file read as
bytes** and a **HEAD pinned**, and no component enters a recipe on a README claim. 🔴 **A recipe
naming a prose-only grant is a proposal with an unpriced legal step in it.**

### 🆕 `P8` — Apache-2.0 learning-evidence spine, **with a documented exit**

🟢 **The gap it fills.** Every pattern on this shelf before it contains a copyleft component —
`P7` keeps **Moodle (GPL-3.0)** at arm's length, and the rest inherit an LMS. 🟢 **`P8` contains no
copyleft at all**, because the entire xAPI tier read this pass is Apache-2.0. 🔵 **It is therefore the
first pattern here that can ship *inside* a closed client deliverable** rather than alongside one.

🟢 **It is also what all four regional governance figures are asking for** (86 % / 26 % / 10 % / 1 % —
see `intel/market.md`): an **auditable record of what the AI did and who reviewed it**.

| Layer | Component | Grant (payload, bytes) | Pin |
|---|---|---|---|
| Tool launch from the LMS | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0, 11 361 B | `master` · `0ec24fe` |
| Statement emitter | [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | 🟢 Apache-2.0, 11 358 B | **`3.x`** · `bbc3f9d` ⚠️ `P793` |
| **Store (default)** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0, 11 357 B | `main` · **`cb794e4`** 🆕 |
| **Store (forward path)** | [`pelotech/xapi-lrs`](https://github.com/pelotech/xapi-lrs) | 🟢 Apache-2.0, 11 357 B | `main` · **`4d18e0c`** 🆕 |
| Conformance reference | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | 🟢 Apache-2.0, 11 357 B | `master` · **`efa045e`** 🆕 |
| Spec of record | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | 🟢 Apache-2.0, 11 525 B | `master` · `ca782a1` |
| Orchestration | **LangGraph** | 🟢 MIT | per `agents/top.md` |
| LMS (optional, remote) | **Moodle** | 🔴 GPL-3.0 — **service, never a dependency** | deployment, not linkage |

🟢 **Wiring, concretely:**
1. **Launch.** `ltijs` receives the **LTI 1.3** launch from the LMS (Moodle, Canvas, Open edX — all
   remote services, none linked). It yields a verified roster context: who the learner is, which
   course, what role.
2. **Emit.** The tutor or assistant does its work; `TinCanPython` writes an **xAPI statement** per
   meaningful event — including **the human review event**, which is the artefact the regulators in
   `intel/trends.md` actually require.
3. **Store.** `lrsql` persists statements. 🟢 **SQLite 3.42 embedded for a pilot, Postgres 14 for
   production** — same binary, no re-architecture between the two.
4. **Review.** A **LangGraph** node holds the decision: anything that would be a grade, a discipline
   action or an IEP input **stops** and requires a human action, which is itself emitted as a
   statement in step 2. 🔵 **This node is the pattern's regulatory core**, not a feature — see the
   three-jurisdiction table in `intel/trends.md`.
5. **Exit, if needed.** Point `pelotech/xapi-lrs` at the **same Postgres database** (`DATABASE_URL`)
   and run `node dist/migrate.js` (or boot with `AUTO_MIGRATE=true`). 🟢 Its schema is **catalog-parity
   with `lrsql` v0.9.5, CI-enforced**, so this is a **no-op except for adding an SSE `NOTIFY`
   trigger** (`trg_xapi_statement_stored`). You gain **xAPI 2.0** (negotiated per request via
   `X-Experience-API-Version`) and **OpenTelemetry** export.

🔴 **The four things that will bite, all from the components' own documentation:**
- 🔴 **Admin accounts do not port.** `lrsql` hashes with a buddy `bcrypt+sha512$...` format
  `xapi-lrs` cannot verify. Existing admin logins **fail 401, not 500**. Bootstrap fresh via
  `XAPI_LRS_ADMIN_USER` / `XAPI_LRS_ADMIN_PASSWORD`. 🟢 **API credentials DO port** — `api_key` /
  `secret_key` pairs and scopes are read as-is from `lrs_credential` / `credential_to_scope`, so
  **statement traffic keeps working with no key re-issuing**.
- 🔴 **Pre-0.6 `xapi-lrs` databases are a dead end.** v0.6.0 rewrote the schema; older ones cannot
  migrate forward and the **startup probe refuses to boot**. Drop and re-provision.
- 🔴 **PGlite is not a deployment target.** Single connection, concurrent transactions serialised;
  the README says local development and low-concurrency only.
- 🔴 **Default OTel sampling is every request.** Set
  `OTEL_TRACES_SAMPLER=parentbased_traceidratio` with `OTEL_TRACES_SAMPLER_ARG=0.1` or lower.

🟡 **One grant caveat, and it is the reason the pin is mandatory:** `pelotech/xapi-lrs`'s Apache-2.0
rests on **one layer** — a clean `LICENSE` payload and a README `## License` section. 🔴 Its
`package.json` **omits the `license` key** and the package is **not on npm (404)**. 🟢 **Vendor the
commit, record the 11 357-byte payload hash in the engagement's licence file, and the grant is
documented.** 🔵 `lrsql` and `ltijs` need no such care.

🟡 **`ADL_LRS` is in the table as a conformance oracle only** — 🔴 its maintainers' own caution that it
targets a small number of users as a proof of concept is **channel-reported, not payload-read** (the
repository serves **no README at any canonical name**; `requirements.txt` 200 confirms it is live).
🟢 Use it to check statement conformance, **never as the deployment**.

🟢 **Effort: 6–8 weeks** for launch + emit + store + review node against one LMS. **+1–2 weeks** per
additional LMS (the LTI 1.3 launch generalises; the roster mapping does not).
🟢 **Why a client buys it:** it is the evidence layer that makes an existing, already-adopted AI
defensible — the deliverable the governance gap in all four regions is actually shaped for.

### 🆕 `P9` — Open Badges 3.0 credentialing, and the **two lawful shapes** past the AGPL fence

🔵 **The constraint, measured this pass and not negotiable.** The **verify** edge is permissive; the
**issue** edge is **AGPL-3.0 in every open implementation**:

| Edge | Component | Grant (payload, bytes) | Pin |
|---|---|---|---|
| **Verify** | [`TanimowoObaloluwaDavid/credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) | 🟢 **MIT**, 1 080 B | `main` · `d34f262` |
| **Issue** | [`schroedinger-Hat/certo`](https://github.com/schroedinger-Hat/certo) | 🔴 **AGPL-3.0**, 33 820 B | `main` · **`6fd0a11`** 🆕 |
| **Issue** | [`edubadges/edubadges-server`](https://github.com/edubadges/edubadges-server) (SURF) | 🔴 **AGPL-3.0**, 34 519 B | **`develop`** · **`9775cc2`** 🆕 |
| **Issue** | [`19otherrsh-dot/Opencred`](https://github.com/19otherrsh-dot/Opencred) | 🔴 **AGPL-3.0**, 34 523 B | `main` · **`d14619e`** 🆕 — 🔴 **do not use**, see below |
| **Issue** | `educredentials/ec-issuer` | 🟡 **prose-only MIT**, no file | 🔴 **unprovable — excluded** |
| Library | [`luisgf/openbadgeslib`](https://github.com/luisgf/openbadgeslib) | 🔴 **LGPL-3.0**, 7 650 B (`LICENSE.txt`) | `master` · **`e7736b6`** 🆕 |

🔴 **`P7`'s arm's-length move does not rescue an AGPL issuer, and this is the one place on this shelf
where that rule fails.** 🔵 GPL attaches to **conveyance**; calling a GPL Moodle over its API is
**use**, so the client's code stays clean. 🔴 **AGPL § 13 attaches to conveying a *modified* version
over a network — and a hosted issuer is exactly that shape.** 🟢 **So "just run it remotely" is the
*trigger* here, not the escape.**

🟢 **Shape (a) — issuer as an *unmodified* remote service.**
Deploy `certo` or `edubadges-server` **as published, at the pinned commit, with zero source
modification**; call it over HTTP from the client's own system. 🔵 The obligation AGPL § 13 creates is
a **source offer for the version being conveyed** — and an unmodified upstream version is satisfied
by **pointing at upstream**. 🟢 **The client's own code never links to it and is never AGPL.**
🔴 **The discipline this requires is real:** configuration only — themes, keys, issuer profiles,
environment. **The first patch to its source makes the deployment a modified conveyance** and the
offer becomes the client's to make.

🟢 **Shape (b) — verify inside the product, issue outside it.**
Ship **`credential-lens` (MIT, 1 080 B)** *inside* the deliverable: the product **consumes and
verifies** credentials — checks signatures, resolves `did:web` issuer identity, reads revocation
status. 🟢 **Issuance stays with the institution's own AGPL deployment or a commercial issuer**, and
never enters the client's codebase. 🔵 **This is the recommended default**, because it matches where
the value usually is: most engagements need to *trust* a credential, not *mint* one.

🔴 **What you cannot do, stated plainly because it is the shape clients ask for:** fork `certo`,
`Opencred` or `edubadges-server`, modify it, and ship it as a component of a closed product or a
hosted white-label service. 🔴 **Three independent licences forbid it and there is no permissive
alternative to substitute** — `Gap 294` stays open precisely here.

🔴 **`Opencred` is excluded on a second, independent ground, and it would fail even if AGPL were
acceptable:** its own README states that **`n8n` is source-available, not OSI open source**. 🟢 An
AGPL root with a **non-OSI leaf** fails dependency closure outright — run it through
`compose/code/dependency-licence-closure/` and it is a 🔴 verdict before the licence of the root is
even reached.

🟡 **`openbadgeslib` (LGPL-3.0) is the one middle option**, for signing and verifying assertions
embedded in SVG/PNG, including JWT-VC for 3.0. 🔵 LGPL permits **dynamic linking from
non-copyleft code** if the library stays replaceable. 🔴 **It is a library, not an issuer** — it does
not give you the issuance service, and 🔴 its grant lives at **`LICENSE.txt`, not `LICENSE`**, which
is the second repository this pass to hide its licence from a single-path probe.

🟢 **Effort: 3–4 weeks** for shape (b). **6–9 weeks** for shape (a), of which a meaningful share is
**deployment hygiene and a written no-modification policy**, not code.
🔴 **This is a licence reading, not legal advice.** 🔵 The hinge is AGPL § 13's
**modified/unmodified** line, and it is the single point a client's counsel must confirm per
engagement. 🟢 **Recorded as the pattern's named risk rather than buried in it.**

### 🟢 Pattern inventory after this pass

| Pattern | Copyleft component? | Shippable inside a closed deliverable? |
|---|---|---|
| `P7` Moodle read-scoped study assistant | 🔴 Moodle GPL-3.0 (remote service) | 🟡 **yes, around** a service the client deploys |
| 🆕 **`P8` Apache-2.0 learning-evidence spine** | 🟢 **none** | 🟢 **yes, entirely** |
| 🆕 **`P9(b)` verify-in / issue-out** | 🟢 none *in the deliverable* | 🟢 **yes** |
| 🆕 **`P9(a)` unmodified remote issuer** | 🔴 AGPL-3.0 (unmodified, remote) | 🟡 **yes, with a no-modification discipline** |

🟢 **Nothing was retired this pass.** 🔵 Pass 65 retired a pattern whose licence premise (`frappe/lms`
= MIT) proved false; **every premise under `P7`–`P9` is a payload reading at a pinned ref**, and none
of them moved.

## 🟢 Sixty-fifth pass, 2026-10-08 — two new patterns built **only** from components whose grant was read from payload this pass, and one pattern **retired** because its licence premise was false

⏱️ **Nineteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔵 **Rule applied to both recipes below (`P759`/`P800`):** every named component has a **licence file
read as bytes** and a **HEAD pinned**, and no component enters a recipe on a README claim. 🔴 **A
recipe naming a prose-only grant is a proposal with an unpriced legal step in it.**

### 🆕 `P7` — Moodle read-scoped study assistant, **permissive end to end**

🟢 **The gap it fills:** this shelf had **four Canvas side-cars and zero Moodle** before this pass,
and Moodle is the **largest LMS in the world** — the default in LATAM, strong across EMEA and APAC.

| Layer | Component | Grant (payload) | Pin |
|---|---|---|---|
| LMS | **Moodle** | 🔴 GPL-3.0 — **run as a service, do not link** | deployment, not dependency |
| LMS bridge | **`GhaithAlHallak8/moodler-mcp`** | 🟢 MIT, 1 072 B | `main` · `4e6139e` |
| Standards bridge | **`Cvmcosta/ltijs`** | 🟢 Apache-2.0, 11 361 B | `master` · `0ec24fe` |
| Telemetry | **`RusticiSoftware/TinCanPython`** | 🟢 Apache-2.0, 11 358 B | **`3.x`** · `bbc3f9d` ⚠️ `P793` |
| Orchestration | **LangGraph** | 🟢 MIT | per `agents/top.md` |

🟢 **Wiring, concretely:**
1. **Moodle stays a remote service.** 🔵 GPL-3.0 is a distribution condition; calling a Moodle
   instance over its Web Services API is **use**, not distribution, so the client's own code stays
   closed. 🔴 **Bundling a Moodle plugin into a deliverable is the step that changes that** — don't.
2. **`moodler-mcp` as the read surface**, launched with its write paths unset. 🟢 It is MIT, so it
   may be forked and trimmed. 🔵 **Trim rather than configure:** pass 64's `canvas-mcp` lesson is
   that **a tool withheld from the model's tool list cannot be argued into calling itself** — delete
   the write tools from the fork and the control becomes structural.
3. **`ltijs` for launch context** so the assistant is entered *from* a course with the learner's
   role already asserted, rather than re-authenticating.
4. **`TinCanPython` emits xAPI statements** for every assistant interaction. 🔵 **This is the
   deliverable that survives the engagement:** an xAPI stream is the evidence base for HolonIQ's
   *"proven instructional benefit"* and for the EU's Art. 14 human-oversight record.
5. **LangGraph node per jurisdiction**, reading `intel/policy-matrix.tsv` as data.
   🔴 **Hard-stop the `assessment_grading` and `admissions_access` functions in EU deployments** —
   Annex III, `2027-12-02`.

🔴 **Pin `3.x`, not `main`, for `TinCanPython`.** `raw.githubusercontent.com/.../main/LICENSE`
returns **404** on that repository; a build file assuming `main` fails and a licence sweep assuming
`main` reports *"unlicensed."* 🟢 **Resolve the symref.**

🟡 **Cost shape:** 4–6 weeks. 🔵 **The schedule risk is not the code, it is the Moodle Web Services
token scope** — institutions issue over-broad tokens by default, and narrowing one is a
committee conversation.

### 🆕 `P8` — Offline credential verification at the door, **EMEA-shaped**

🟢 **The gap it fills:** `Gap 294` says the credential **issue** edge is unbuildable permissively.
🔵 **It says nothing about the VERIFY edge, and that edge turned permissive this pass** — so this is
the credential pattern that can actually ship today.

| Layer | Component | Grant (payload) | Pin |
|---|---|---|---|
| Verifier | **`TanimowoObaloluwaDavid/credential-lens`** | 🟢 MIT, 1 080 B, **file + manifest agree** | `main` · `d34f262` |
| Spec | **Open Badges 3.0 / W3C VC** | 🟡 free to implement; 🔴 1EdTech spec repo has **no licence file** | — |
| LMS/host | **OpenOLAT** | 🟢 **Apache-2.0**, 10 982 B | `master` · `e2a733c` |
| Issuer | `educredentials/ec-issuer` | 🔴 **prose-only MIT** | 🔴 **NOT in the deliverable** |

🟢 **Wiring, concretely:**
1. **`credential-lens` is vendored, not depended on.** 🔵 **Zero dependencies and it runs from
   `file://`** — so it goes into the deliverable as source, with **no lockfile and no supply-chain
   surface**. 🟢 That is the single most procurement-friendly property in this entire KB.
2. **Verify at the admissions/enrolment door**, not at issuance: inspect an incoming OB 3.0 or W3C VC
   for the four defects its README names — **fake signature value, legacy 1.x badge no verifier
   accepts, award with no expiry, award with no revocation path**.
3. **Run it air-gapped.** 🔵 Offline verification means **the credential never leaves the
   institution** — which answers the EU data-boundary question before it is asked, and makes the
   component viable where connectivity is the constraint (LATAM, per `intel/market.md`).
4. **Host inside OpenOLAT** when the client wants it in the LMS: **Apache-2.0**, so a closed
   derivative is permitted.
5. 🔴 **Do NOT promise issuance in the same statement of work.** 🟢 Price it separately against
   `Gap 294`'s three options — email `ec-issuer` for a real grant (hours), accept a self-hosted AGPL
   issuer (free, constrains the client), or implement OB 3.0 from spec (weeks, the only closed-source
   path). 🔵 **A proposal that does not name which one it means is underpriced.**

🟡 **Cost shape:** 2–3 weeks for verification alone. 🔵 **It is deliberately small** — and `Gap 294`
is the reason the big version does not exist yet.

### 🔴 Retired: any pattern naming **Frappe Learning** as a permissive base

🔴 **The channel reported `frappe/lms` as MIT.** 🟢 **Measured: AGPL-3.0** — `license.txt`,
**33 893 B**, `sha256:db1a87ba81e8`, with `package.json` declaring `AGPL-3.0-or-later`. 🔵 **Two
layers agreeing against the channel.**

🔴 **A pattern built on that claim would have promised a closed-source LMS derivative on a
network-copyleft base** — and §13 is an **operating** condition for an LMS, which is network-facing
by definition. 🟢 **No such pattern was published**, because the licence was probed before the
recipe was written. 🔵 **Recorded as a near-miss on purpose:** the probe-before-recipe rule is what
made this a non-event, and the rule is the asset.

### 🟢 Pattern inventory, by whether the grant is PROVABLE

| | Patterns |
|---|---|
| 🟢 **Permissive end-to-end** | **`P7`** Moodle study assistant 🆕 · **`P8`** offline credential verification 🆕 · P4 EMEA sovereign stack |
| 🟡 **Permissive core, copyleft service** | P1 agentic platform · P5 PoC-to-production LATAM |
| 🔴 **Blocked on a grant** | credential **issuance** (`Gap 294`) · Caliper analytics (`Gap 284`) · permissive **SIS** (`Gap 298`) · Open edX agent bridge (`Gap 297`) |

🔵 **Three of the four blocked items are blocked by a LICENCE, not by missing technology.** 🟢 **That
is the single most useful sentence this shelf can hand a studio lead** — it means the unblocking work
is procurement and email, measured in hours, not engineering measured in quarters.


## 🟢 Sixty-fourth pass, 2026-10-08 — one new recipe for the **credential-issuance** edge, and it is the first recipe on this shelf whose **first step is a licence conversation**; plus a capability-gating pattern lifted from an implementation rather than a spec

⏱️ **Eighteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🟢 **Every repository named below is payload-read at a ref resolved by `ls-remote --symref` this pass.**
🔴 **No star counts** (`api.github.com` 403, `P745`). 🔴 **No suite was run this pass** — the session
refused to execute this repository's own test scripts, so every instrument referenced below is cited as
existing, 🔴 **not as having been re-run** (`Gap 257`/`Gap 258`, and `P752`: prose must not imply a
result it did not measure).

### 🆕 Recipe — **"Verifiable achievement, governed": OB 3.0 credentials out of an existing LMS, with the grant resolved before the build**

🔵 **Why this recipe exists:** 1EdTech puts digital credentials at the centre of 2026
(`intel/trends.md`), and this pass found that the edge has **no permissive, file-grant
implementation** (`verticals/solutions.md`). 🟢 **So the recipe is honest about starting with a
blocker, which is more useful than a recipe that pretends the blocker is not there.**

🟢 **The wiring, component by component, all payload-verified this pass:**

| Layer | Component | Ref · HEAD | Licence (payload) | What it contributes |
|---|---|---|---|---|
| Learning substrate | [`moodle/moodle`](https://github.com/moodle/moodle) | `main` · `f205347` (pass 63) | 🔴 **GPL-3.0-or-later** | Course, activity completion and competency data. 🔴 **Substrate, not component — deploy beside it, never link into it** |
| Rostering / identity | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | `main` · **`6de5476`** | 🟢 **Apache-2.0** (10 173 B) | Serves **OneRoster 1.2** from an Ed-Fi ODS (DS 4.0/5.x) — the authoritative "who the learner is", licence-clean |
| Achievement → credential | [`educredentials/ec-issuer`](https://github.com/educredentials/ec-issuer) | `main` · **`8bafc99`** | 🟡 **`MIT` in README prose ONLY** | Issues and signs **OB 3.0 + ELM**, delivers over **OID4VCI**, **revocation with reason tracking**, expiry-driven status. 🔴 **BLOCKED at the licence gate — see step 1** |
| Copyleft fallback | [`Schroedinger-Hat/certo`](https://github.com/Schroedinger-Hat/certo) | `main` · **`6fd0a11`** | 🔴 **AGPL-3.0** (33 820 B) | Issue **and verify**, Strapi + Nuxt. 🟢 Use when the client accepts a self-hosted AGPL deployment |
| Agent edge | [`zhenghh04/canvas-mcp`](https://github.com/zhenghh04/canvas-mcp) | `main` · **`0ef723f`** | 🟢 **MIT** (1 069 B) | Instructor-side read of gradebook/completion, **with its write tier pinned off for this path** |

🟢 **Steps, in the order that keeps a client out of trouble:**

1. 🔴 **Resolve `ec-issuer`'s grant BEFORE any integration work.** Its licence is a two-word README
   heading — no file, no manifest key, no registry publication, no holder, no year. 🟢 **Ask the
   maintainer for a `LICENSE` file or an SPDX `license` key in `pyproject.toml`.** 🔵 **This is a day
   of email, and it is the difference between a shippable component and an unprovable one.** 🔴 **If the
   answer does not come, do not substitute optimism — take the AGPL fallback and tell the client it is
   self-host-only, or build against the OB 3.0 / W3C VC specifications, which are open to implement.**
2. 🟢 **Stand up rostering first, not credentials.** `edfi-oneroster` over the client's Ed-Fi ODS gives a
   stable learner identity; a credential issued against an unstable identity is worse than no credential,
   because it is signed.
3. 🟢 **Define the achievement rule in the substrate, not the agent.** Moodle competency / activity
   completion is the evidence; the agent reads it. 🔴 **An LLM must not be the thing that decides an
   achievement was earned** — that is the function Annex III conditions.
4. 🟢 **Pin the agent edge read-only for this path.** With `zhenghh04/canvas-mcp`, set
   `CANVAS_ENABLE_WRITES=0`; its 24 read tools remain, its 18 write tools are **not published to the
   model's tool list at all**, and its 5 destructive tools are off by default and cannot bypass the write
   gate. 🔵 **A credential pipeline needs to read the gradebook and must never write it.**
5. 🔴 **Gate the function by jurisdiction — and know that the gate cannot answer yet.** Credential
   issuance *determines access to and progression through* education, which is the EU Act's **Annex III**
   trigger. 🔴 **`Gap 289` is exactly this: `credential_issuance` is NOT in `compose/code/p782-policy-gate/`'s
   14-function vocabulary**, so running the gate on this recipe today returns **no verdict**, not a
   permissive one. 🟢 **State that to the client as an open item**; 🔴 **do not read a silent gate as a
   green one.**
6. 🟢 **Issue to a wallet, not to a database.** OID4VCI delivery is what makes the credential portable
   and therefore worth issuing; an "achievement row" in the client's own schema is a report, not a
   credential.

🔴 **Known holes in this recipe, stated rather than smoothed over:** the best-fit component's licence is
unprovable (step 1); the policy gate has no vocabulary entry for the function (step 5); and the
verification side is only available under AGPL (`certo`), so **a closed-source verifier is a build, not
an integration.**

### 🆕 Pattern — **capability gating by non-publication**, taken from an implementation

🔵 **This shelf has taken patterns from specifications and from architectures. This one comes from a
single repository's configuration design, and it generalises past education entirely.**

🟢 **What [`zhenghh04/canvas-mcp`](https://github.com/zhenghh04/canvas-mcp) (MIT, `main` · `0ef723f`)
does, read from its own README:** three tiers — `read` (24 tools, always on), `write` (18 tools, **on by
default**, disabled by `CANVAS_ENABLE_WRITES=0`), `destructive` (5 tools, **off by default**, enabled by
`CANVAS_ALLOW_DESTRUCTIVE=1`). 🟢 **The destructive flag cannot bypass the write gate.** 🟢 **And the
load-bearing detail: a tool that is disabled is never published to the model's tool list at all** — it
is not refused at call time, it is **absent**.

🔵 **Why that is the stronger control, and it is an agent-design argument rather than a security one:**
🔴 **a tool the model can see is a tool the model can be argued into calling** — by a prompt, by a
document it reads, by a user's framing. 🟢 **A tool that was never published cannot be argued into
existence, and it also costs zero context.** 🔵 **Refusal is a runtime decision under adversarial
pressure; non-publication is a deployment decision made once, in the clear.**

🟢 **How to apply it on any engagement in this KB:** express the agent's tool surface as **tiers bound
to environment configuration**, not as per-call permission checks; make the destructive tier
**independently gated and subordinate** to the write tier, so one flag cannot unlock two levels; and
**emit the surface** — a `tools` listing that shows exactly what is published under the current posture,
so the deployed surface is auditable without reading code. 🔵 **For this industry, pin it to the
regulation: Korea's AI Basic Act requires meaningful human monitoring and intervention *at any time* in
high-impact systems, and a tiered, enumerable tool surface is how that requirement becomes something a
reviewer can inspect rather than something a vendor asserts.**

🔴 **One honest limit:** this is a **pattern read from a README**, not a measured property of the running
code. 🟢 The licence and the ref are payload-read; 🔴 **the behaviour is the repository's own
description**, and `P796` (this pass) is precisely the rule that a README's self-description is its
ambition. 🔵 **The pattern is worth adopting on its own logic; the claim that this repository implements
it correctly is unverified here.**

### 🟡 Recipes carried forward, with one correction to their pre-flight

🟡 **Every recipe on this shelf that touches scoring, essay evaluation or summary assessment keeps its
standing gate:** run `compose/code/p782-policy-gate/` first, and remember `P764` — 🔴 **NYC's
`2026-03-24` guidance *prohibits* student-facing AI in public K-12 through grade 8, and no
human-in-the-loop converts a prohibition into a condition.**

🔴 **The correction, and it applies to every recipe's citation style from here forward (`P797`):** where
a recipe's rationale cites a regulation or a market figure, it must now say **`EGRESS_DENIED
(allowlist)`** rather than **`000`** for the primary source. 🔵 **The difference is not cosmetic for a
client-facing document:** `000` reads as *"the source may be unreliable or down"*, 🟢 **while
`EGRESS_DENIED (allowlist)` reads as *"the source is fine; this build environment is fenced"*** — which
is the true statement, and the one a reviewer needs. 🟢 **`Gap 293` closed in `intel/market.md` with a
Wikipedia control; the band language follows it here.**


## 🟢 Sixty-third pass, 2026-10-08 — the pre-flight gains a **Gate 0**, because every gate below it takes a `[ref]` and `master` is a **pseudo-ref**; and `R63a` wires the assessment edge, the one place where the licence line and the policy line fall on the same component

⏱️ **Seventeenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🔴 The pre-flight, corrected again — and this time the defect is **upstream of every gate**

🔴 **Gates 1, 1b and 2 all take a `[ref]` argument, and this shelf has been handing them
`master`.** 🟢 **Measured this pass, 3 of 3, with a 404-discriminating control:**
`raw.githubusercontent.com` serves the **default branch** for the literal ref `master` even where
no `master` exists — `main` **404**, invented branch **404**, `master` **200**, `HEAD` **200** —
on repositories whose real defaults are `refs/heads/0.7`, `refs/heads/public`, `refs/heads/2.12`.

🔵 **So a `0 SINGLE` from Gate 1 "at `master`" was a grant read from *some* branch, named wrongly.**
🟢 **`P714` warned about exactly this; `P793` is the measurement, with a control, and a gate.**

```sh
# Gate 0 — NEW, and it runs FIRST: what ref are the gates below actually reading?   (P793)
sh compose/code/p791-registry-id-provenance/ref.sh <owner/repo> [...]
#   0 DEFAULT-IS-NAMED (main|master)  -> the usual assumption holds
#   3 DEFAULT-IS-NEITHER             -> 🔴 pass THIS ref to every gate below
#   5 UNRESOLVED                     -> 🔴 no gate below may claim an absence
#   🟢 7 of 25 PHP/composer rows exit 3 — v31.0.00, mobile, 2.2, 0.7, 3.x, 2.12, public
#   🟢 0 of 12 evaluation-tier rows exit 3 — the defect is ECOSYSTEM-shaped, not shelf-shaped

# Gate 1 — may we use the CODE and the DATA?   (Gap 282 / Gap 283)
bash compose/code/p784-licence-scope-map/probe.sh <owner/repo> <ref-from-Gate-0>
#   0 SINGLE · 3 PARTITIONED · 4 UNGRANTED · 5 unreachable
#   🔴 16 ROOTED filenames only — read `4 UNGRANTED` as "no grant AT THE ROOT" (Gap 287)

# Gate 1b — enumerate the TREE before trusting Gate 1's absence
cd compose/code/p441-tree-licence-enumeration && python3 enumerate_licence.py <slugs-file>
#   🔴 run it from ITS OWN directory — its sys.path insert is relative (P355)
#   🔴 distrust a CC-BY/CC0 family it reports: its regex matches `licenseExtension` (Gap 288)

# Gate 1c — NEW: read the MANIFEST, because it is the only layer that can say `-or-later`
echo "<owner/repo>" | sh compose/code/p791-registry-id-provenance/sweep_composer.sh
#   🟢 emits default_ref, head_sha, served_at, the composer.json grant, and the DECLARED package id
#   🟢 and it resolves the registry id from the TREE, never from the slug (P791)

# Gate 2 — may we DEPLOY this function in this jurisdiction?   (Gap 278)
bash compose/code/p782-policy-gate/gate.sh <function> [jurisdiction|region]
#   0 clear · 3 GATED · 4 PROHIBITED · 5 PROPOSED · 6 NEVER MEASURED · 2 bad region
#   🔴 `credential_issuance` is NOT in the 14-function vocabulary (Gap 289)
```

| Axis | Question | Instrument | Failure it prevents |
|---|---|---|---|
| 🆕 **Ref** | **which branch are we even reading?** | 🟢 `p791/ref.sh` | 🔴 **the `P793` failure**: a grant read at a pseudo-ref and cited as `master` |
| **Code** | is the grant permissive? | `p784` + `p441` | building on copyleft, or on a repo with no grant at all |
| 🆕 **Combination** | is it `-only` or `-or-later`? | 🟢 `p791/sweep_composer.sh` | 🔴 **the `P794` failure**: a file that cannot express the suffix that decides forward-combination |
| **Data** | is the *corpus* shippable? | `p784` (`PARTITIONED`/`UNCLASSIFIED`) | the `P783` failure: MIT code over a corpus that forbids training |
| **Policy** | may the function be deployed there? | `p782` | the `P764` failure: an MIT repo exposing a **prohibited** function |
| **Prose** | is the grant split where no probe reads? | 🔴 **a human, reading `README` + `wiki/`** | the `P786` failure |

🔴 **And a new worked instance for why Gate 1c is not optional.**
🟢 `tl-its-umich-edu/caliper-php-public` @ `refs/heads/public` (`e35b0ec`) — 🔴 no `main`, no
`master`, so Gate 0 is the only reason a gate reads the right tree at all:

| Layer | Says | Band |
|---|---|---|
| licence **file** (`LICENSE`, 7 438 B) | *"GNU LESSER GENERAL PUBLIC LICENSE / Version 3"* | 🔴 **LGPL-3.0** — open, copyleft |
| **manifest** (`composer.json`) | `"license": "proprietary"` | 🔴 **not open at all** |
| **registry** (packagist `umich-its-tl/caliper-php`) | `["proprietary"]`, latest `1.0.1` **2016-01-27** | 🔴 **not open at all** |

🔴 **A pre-flight that ran only Gate 1 would publish "LGPL-3.0" and a reviewer would read "open
source, copyleft, keep it at arm's length". 🔴 Two of three layers say there is no grant.**
🆕 **`P794`: two layers can land in opposite *bands*, not merely differ in precision.**

🟡 **The cheaper, commoner instance of the same gate:** `portabilis/i-educar`'s licence file at
`2.12` is bare **GPL-2.0** (*"Version 2, June 1991"*) and its manifest says
**`GPL-2.0-or-later`** — and `moodle/moodle` splits the same way (`GPL-3.0-or-later` in the
manifest). 🔵 **A licence file structurally cannot express `-or-later`:** the GNU text is
byte-identical either way, so the suffix lives in the manifest or the headers (`P620`).
🔵 **Which means the "can we combine this forward?" question has only ever been answerable at a
layer this pre-flight did not run.**

### 🟢 `R63a` — "automated assessment the client can actually deploy": a permissive QTI 3 pipeline behind a per-jurisdiction policy node

🔵 **Why this recipe, and why now:** 🟢 the assessment edge is the **only** place on this shelf
where the licence line and the policy line fall on the *same component*, and this pass measured
both. 🔴 The best-known PHP QTI component is **`GPL-2.0-only`**; 🟢 the permissive alternative
shipped **v0.7.0 on 2026-09-22**, the freshest release on the edge table. 🔴 And the function is
conditioned in the EU, Vietnam and (draft) Peru, labelled in South Korea, and **prohibited** in NYC
public K-12.

🔴 **What not to do:** reach for `oat-sa/qti-sdk`. 🔴 It is the most capable PHP QTI library and it
is **`GPL-2.0-only`** — *only*, so it cannot even be combined forward to GPL-3.0, and it cannot sit
inside a client deliverable. 🔴 **And do not build the grading decision at all** where `p782`
returns `4 PROHIBITED`: `P764` says no amount of human-in-the-loop converts a prohibited use into
a permitted one.

🟢 **The components, each payload-read at a ref Gate 0 resolved:**

| Layer | Component | Licence (both layers where both exist) | Ref · SHA | Registry date |
|---|---|---|---|---|
| Item model · parse · validate · write | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · `LICENSE.md` 1 072 B | `main` · `ab92d85` | 🟡 no composer manifest |
| QTI 3 support library (PHP) | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | 🟢 **MIT** · file **and** manifest | `main` · `0ba4f78` | 🟢 **`wikiwijs/php-qti3` v0.7.0, 2026-09-22** |
| Delivery / rendering | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · `LICENSE` 1 076 B | `main` · shelved | — |
| Launch (who may be told what) | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 🟢 **Apache-2.0** · manifest | `master` · `a20c71b` | 🟢 **`packbackbooks/lti-1p3-tool` v6.4.4, 2026-09-23** |
| Roster (who is in the class) | [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | 🟢 **MIT** · file **and** manifest | `main` · `f54e292` | 🟢 **v4.5, 2026-03-18** |
| Learning record (what the learner did) | [`php-xapi/model`](https://github.com/php-xapi/model) | 🟢 **MIT** · manifest | 🔴 **`3.x`** · `e005084` | 🟡 `3.x-dev`, 2025-01-20 |
| Policy node | `compose/code/p782-policy-gate/` + `p764` red/green split | 🟢 this KB | — | — |
| Provenance marking (Korea) | `compose/code/aiact-50-2-marking/` | 🟢 this KB | — | — |

🔵 **Wiring, and the policy node is not a feature flag — it is the control flow:**

1. **Gate 0 on all six repos.** 🔴 `php-xapi/model`'s default ref is **`3.x`**, not `main` — pin it
   or a later pre-flight reads a tree nobody chose.
2. **Launch** from the client's LMS over **LTI 1.3** with the Apache-2.0 tool library. 🔵 Nothing
   is installed inside Moodle (GPL-3.0) or Canvas/Open edX (AGPL-3.0), so `P747a` holds and the
   deliverable stays permissive.
3. **Resolve the roster** through the SIS client (MIT) or OneRoster, never by exporting students
   into the assessment service's own store — 🔴 `CA AB 1159` prohibits using student data to train
   models, which is a **data-flow** constraint, not a clause to paste into a contract.
4. **Author and bank items** with the MIT TypeScript toolchain; **deliver** with the MIT player;
   **parse and score server-side** with `Kennisnet/php-qti3`. 🟢 **MIT end to end, and the
   `GPL-2.0-only` SDK never enters the dependency graph.**
5. 🔴 **Branch on jurisdiction before the score becomes a decision**, by calling `p782` with the
   function, not the product:
   - `4 PROHIBITED` (NYC public K-12 and anywhere `p782` reports the red tier) → 🟢 **emit a
     teacher-facing draft and stop.** The score is an input to a person; it is never written to a
     record. 🔵 This is the green tier NYC left open in March and again in the 2026-09-02 K-8
     moratorium.
   - `3 GATED` (EU Annex III, Vietnam, 🆕 Peru draft) → 🟢 **build the Article 27 FRIA artefact and
     the human-review step as *products*, not as paperwork**: the conformity obligation moved to
     **2027-12-02**, 🔴 but the Article 4 literacy duty and the emotion-recognition ban are already
     in force, so **no affect-inference signal may enter the pipeline at all.**
   - South Korea → 🟢 **mark the generated artefact** with `aiact-50-2-marking/`; the labelling duty
     is the cheapest of the three to satisfy because it is a *provenance* requirement, and this KB
     already emits that shape.
6. **Record** the attempt as xAPI statements with the MIT model library, 🔵 so the learning record
   outlives the assessment service — the same argument `R62a` makes for credentials.

🟡 **What `R63a` does NOT claim.** 🔴 `Kennisnet/php-qti3` is **v0.7.0** — pre-1.0, and this shelf
has read its licence and its registry date, **not its QTI 3 conformance coverage.** 🔵 The honest
scoping line is *"permissive and current, coverage unmeasured"*, and measuring it means running its
own test suite, which is one pass's work and is **not** claimed here.
🔴 **`php-xapi/client` (MIT) is dated 2021-03-24 at `0.7`** — shelved as permissive and **stale**;
`R63a` uses the **model**, not the client, and a deployment needs a maintained transport.
🔴 **No Caliper analytics leg**, because `Gap 284`'s only reachable implementation is `proprietary`
in two layers of three and nine years stale.

## 🟢 Sixty-second pass, 2026-10-08 — the pre-flight gains a **third layer it cannot automate**, and `R62a` wires the credential edge into a deployable shape beside the LMS

⏱️ **Sixteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🔴 The pre-flight, corrected — two instruments and one **manual** read, because `P786` proved the third cannot be a probe

🔴 **Pass 61 shipped this as two runnable gates and called the licence axis closed. It is not.**
🟢 **Measured this pass over 13 repos and committed** (`compose/code/p786-scope-verdict-agreement/result.2026-10-08.tsv`): 🔴 **`p784` and `p441` disagree on 1, and agree-while-both-wrong on a
second** — and that second failure is unreachable by any file-enumerating probe, however complete
(`P786`). 🔴 **Which is why the gate below emits `NEEDS-PROSE-READ` on unanimity instead of a pass.**

```sh
# Gate 1 — may we use the CODE and the DATA?   (Gap 282 / Gap 283)
bash compose/code/p784-licence-scope-map/probe.sh <owner/repo> [ref]
#   0 SINGLE · 3 PARTITIONED · 4 UNGRANTED · 5 unreachable
#   🔴 16 ROOTED filenames only — read `4 UNGRANTED` as "no grant AT THE ROOT" (Gap 287)

# Gate 1b — NEW IN THE PRE-FLIGHT: enumerate the TREE before trusting Gate 1's absence
cd compose/code/p441-tree-licence-enumeration && python3 enumerate_licence.py <slugs-file>
#   🔴 run it from ITS OWN directory — its sys.path insert is relative (P355)
#   🔴 and distrust a CC-BY/CC0 family it reports: its regex matches `licenseExtension` (Gap 288)

# Gate 2 — may we DEPLOY this function in this jurisdiction?   (Gap 278)
bash compose/code/p782-policy-gate/gate.sh <function> [jurisdiction|region]
#   0 clear · 3 GATED · 4 PROHIBITED · 5 PROPOSED · 6 NEVER MEASURED · 2 bad region
#   🔴 `credential_issuance` is NOT in the 14-function vocabulary (Gap 289)
```

| Axis | Question | Instrument | Failure it prevents |
|---|---|---|---|
| **Code** | is the grant permissive? | `p784` + `p441` | building on copyleft, or on a repo with **no grant at all** |
| **Data** | is the *corpus* shippable? | `p784` (`PARTITIONED`/`UNCLASSIFIED`) | 🔴 **the `P783` failure**: MIT code over a corpus that forbids training |
| **Policy** | may the function be deployed there? | `p782` | 🔴 **the `P764` failure**: an MIT repo exposing a **prohibited** function |
| 🆕 **Prose** | is the grant **split**, in a place no probe reads? | 🔴 **a human, reading `README` + `wiki/`** | 🔴 **the `P786` failure**, measured this pass |

🔴 **The fourth row has no instrument and this pass is not pretending otherwise.**
🟢 **The worked instance:** `luisgf/openbadgeslib` declares **LGPL-3.0 library / BSD-2-Clause CLI**
in `wiki/Authors-License-and-FAQ.md` **only** — `LICENSE.txt` says LGPL-3.0 alone, `pyproject.toml`
carries one classifier, PyPI agrees, and **0 of 40 `.py` headers** name BSD. 🔴 **So a probe that
read every file in the tree would still return one family.** 🟢 **The remedy is two minutes of
reading per candidate, and it is cheaper than either gate.**

### 🟢 `R62a` — "issue verifiable credentials from the client's LMS, without touching the LMS"

🔵 **The recipe the EMEA micro-credentials mandate asks for, and the first on this shelf whose
demand signal is a named public programme** (`intel/market.md`: Council Recommendation 2022,
European Digital Credentials for Learning as a central Europass product, 🔴 providers *failing at
the issuing step*).

🔴 **What not to do:** build issuing *inside* Moodle (**GPL-3.0**) or Open edX / Canvas
(**AGPL-3.0**, §13 reaches network use). 🔴 **And specifically not here** — a credential must
outlive the platform that issued it, so putting the issuer inside a copyleft substrate couples the
one durable artefact to the one component you most expect to replace.

| # | Role | Component | Licence · ref | Wiring |
|---|---|---|---|---|
| 1 | **Trigger** — course completion | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 · npm **v7.0.7, 2026-10-06** | LTI 1.3 launch from the LMS into your service; the launch carries the user and context claims |
| 2 | **Who the learner is** | [`longsightgroup/oneroster`](https://github.com/longsightgroup/oneroster) | 🟢 MIT · `8c14777` | resolve the LTI subject to a roster identity — never trust a display name as a credential subject |
| 3 | **Evidence it happened** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | 🟢 Apache-2.0 · `cb794e4` | xAPI statements are the **evidence** field of the credential; the LRS is the audit trail a verifier may ask for |
| 4 | **Sign** | [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) | 🟢 BSD-3-Clause · `15fb018` · npm **v10.0.2, 2025-11-19** | issue a W3C VC / OpenBadgeCredential; `did:web` on the institution's own domain |
| 5 | **Operate the issuer** | [`digitalcredentials/issuer-coordinator`](https://github.com/digitalcredentials/issuer-coordinator) | 🟢 MIT · `e663eea` | the HTTP surface + batch issuance the registrar actually runs; keeps keys out of the LMS |
| 6 | **Verify** | [`digitalcredentials/verifier-core`](https://github.com/digitalcredentials/verifier-core) | 🟢 MIT · `276ebd2` · 🟡 npm **v1.0.0-beta.11** | status lists and revocation for the third party checking the badge |
| 7 | **Prove conformance** | [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core) | 🟢 Apache-2.0 · `0a66b52` | the artefact a ministry or employer buyer asks for; run it in CI against every issued credential shape |
| 8 | **Learner-side** | [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) | 🟢 MIT · `1c46a82` | optional, and the only component on this shelf the *learner* installs |

🟢 **Eight components, eight permissive grants, every one payload-read at a pinned ref. Nothing
copyleft touches the deliverable, and the LMS is never forked.**

🔴 **Three things to get right, each from a measurement in this pass:**
🔴 **(a) do not `npm install @digitalcredentials/sign-and-verify`** — the package is **v0.0.1 from
2020-11-08** while its repo HEAD moves; use steps 4 and 6 instead.
🔴 **(b) `verifier-core` is beta at ten months** — pin the version and own the upgrade.
🔴 **(c) run Gate 2 before promising a jurisdiction**: `credential_issuance` is **not measured
anywhere** (`Gap 289`), so the correct proposal sentence is *"we will establish the regulatory
position for issuance in your jurisdiction"*, not *"issuance is unregulated"*.

🔵 **Estimate shape:** 6–8 weeks for steps 1–5 against one LMS and one credential type;
🔴 **+2 weeks if the client wants `did:web` on a domain they do not already control**, which is a
procurement task rather than an engineering one.

### 🟢 `R62b` — "stand up a state-agency student-record spine" (North America), and why it is a *build*, not an install

🔵 **For the one edge on this shelf whose buyer is a state education agency rather than a campus.**
🟢 **All Apache-2.0, payload-read this pass.**

| # | Component | Licence · ref | Role |
|---|---|---|---|
| 1 | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Docker`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Docker) | 🟢 Apache-2.0 · `29c571a` | stand the ODS + API up on PostgreSQL for the pilot — the cheapest honest starting point |
| 2 | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | 🟢 Apache-2.0 · `e453cd2` | the Operational Data Store and REST API itself |
| 3 | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | 🟢 Apache-2.0 · `37ff595` | the **extension** mechanism — a district's local fields without forking the core |
| 4 | [`Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher) | 🟢 Apache-2.0 · `dabdd14` | district → state-agency replication between instances of the same version |
| 5 | [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | 🟢 Apache-2.0 · `3d24df6` | the standard the whole thing conforms to |

🔴 **The measured constraint that changes the estimate: there is no public first-party package
surface.** The Alliance's own `.nuspec` names **`EdFi.OdsApi.Sdk`**, and that id returns **`none`**
on the reachable, control-verified NuGet date oracle; `api.github.com` is **403**; `ed-fi.org` is
**000**. 🔴 **So the plan carries a source build, and no component in this recipe may be quoted with
a version** (🆕 `Gap 286`). 🟡 **The only public `EdFi`-named packages are third-party**
(`EdNexusData.EdFi.OdsApi.Sdk`, v1.0.19) 🔴 **whose GitHub org does not resolve** — do not take the
dependency.

🟢 **Where the AI goes, and it is the same `P736` shape as every other recipe here:** beside the
spine, across the REST API, never inside the ODS schema. 🔴 **And run Gate 2 first** — a model that
scores or flags students off this spine is `assessment_grading` or `admissions_access`, both of which
`p782` reports **GATED** in the EU, and the US-federal row for `admissions_access` is 🔴 **never
measured**, which is not a permission.

## 🟢 Sixty-first pass, 2026-10-08 — the pre-flight becomes **executable** (two gates, two instruments, 38 assertions), and `R61a` wires the four protocol edges into one deployable shape

⏱️ **Fifteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 The pre-flight, now three columns and **runnable** — `Gap 278` and `Gap 283` closed

🔴 **Passes 59–60 wrote this as prose and said so twice.** 🟢 **It is now two instruments:**

```sh
# Gate 1 — may we use the CODE and the DATA?   (Gap 282 / Gap 283)
bash compose/code/p784-licence-scope-map/probe.sh <owner/repo> [ref]
#   0 SINGLE · 3 PARTITIONED · 4 UNGRANTED · 5 unreachable

# Gate 2 — may we DEPLOY this function in this jurisdiction?   (Gap 278)
bash compose/code/p782-policy-gate/gate.sh <function> [jurisdiction|region]
#   0 clear · 3 GATED · 4 PROHIBITED · 5 PROPOSED · 6 NEVER MEASURED · 2 bad region
```

| Axis | Question | Instrument | Failure it prevents |
|---|---|---|---|
| **Code** | is the grant permissive? | `p784` | building on copyleft, or on a repo with **no grant at all** — 🔴 35 % of the benchmark frame |
| 🆕 **Data** | is the *corpus* shippable? | `p784` (`PARTITIONED`/`UNCLASSIFIED`) | 🔴 **the `P783` failure**: MIT code, and a corpus that forbids training and production |
| 🆕 **Policy** | may the function be deployed there? | `p782` | 🔴 **the `P764` failure**: an MIT repo exposing a **prohibited** function |

🔴 **Run both. Either one alone passes an architecture that cannot ship:** `p784` clears
`algorithm0r/canvas-lms-mcp` (MIT) whose grading function `p782` reports **GATED** in the EU and
Vietnam; `p782` clears a tutoring agent in Mexico whose evaluation corpus `p784` reports
**UNCLASSIFIED** and whose licence forbids training.
🔴 **And `6` is not `0`:** an unmeasured jurisdiction is an unmeasured jurisdiction (`P476`).

### 🟢 `R61a` — "customise the client's LMS with AI on top", as four edges instead of a fork

🔵 **The recipe every education engagement actually asks for, and the first version of it on this
shelf where every component is payload-read and permissive.**

🔴 **What not to do:** fork Moodle (**GPL-3.0**) or Open edX / Canvas (**AGPL-3.0**, §13 reaches
network use). 🟢 **What to do: sit beside the substrate and speak four protocols.**

| # | Edge | Component | Licence · ref | Wiring |
|---|---|---|---|---|
| 1 | **Launch / identity** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 · npm **v7.0.7 2026-10-06** | LMS launches the tool over **LTI 1.3** (OIDC + JWT). Globant's service is a separate deployable; the substrate's copyleft never reaches it (`P736`). |
| 2 | **Roster / scoping** | [`longsightgroup/oneroster`](https://github.com/longsightgroup/oneroster) (TS) or [`TCI/OneRoster`](https://github.com/TCI/OneRoster) (Ruby) | 🟢 MIT · `8c14777` / `5f8a15a` | **OneRoster** supplies sections, teachers, enrolments → the agent can be scoped to a section and audited per teacher. 🔵 Without this an AI tutor cannot be *assigned*. |
| 3 | 🆕 **Content ingest** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) + [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | 🟢 MIT · `a882b22`, npm **v3.4.5 2026-10-05** · 🟢 Apache-2.0 · `806c0ba` | Replay the client's **existing SCORM/AICC estate**; `CATAPULT` supplies the **cmi5 conformance suites** that evidence the migration. 🔵 This is the edge that makes it customisation rather than replacement. |
| 4 | **Record / evidence** | [`xapijs/xapi`](https://github.com/xapijs/xapi) → [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) or [`openfun/ralph`](https://github.com/openfun/ralph) | 🟢 MIT · `5e28e9b` · 🟢 Apache-2.0 · `cb794e4` · 🟢 MIT · `53cc58c` | Every interaction lands in an **LRS** as xAPI. 🟢 **This is the component that answers a regulator**, and mastery estimates stop dying with the session. 🔵 `ralph` for EU data residency; `lrsql` to run on an RDBMS the client already operates. |

🟢 **Pre-flight for `R61a`, run before the proposal:**

```sh
for r in Cvmcosta/ltijs longsightgroup/oneroster jcputney/scorm-again \
         adlnet/CATAPULT xapijs/xapi yetanalytics/lrsql openfun/ralph; do
  bash compose/code/p784-licence-scope-map/probe.sh "$r" || echo "REVIEW: $r"
done
bash compose/code/p782-policy-gate/gate.sh --region <the client's region>
```

🔴 **Then the function gate, per feature, not per product:** if the tool **grades**, `p782` returns
**GATED** in the EU and Vietnam → human oversight, bias testing and user notification are **scope
items**. 🔴 **If any feature infers engagement, attention or emotion and the client is in the EU,
it is `PROHIBITED` — cut it in the proposal, not in UAT.**

### 🟢 `R61b` — "prove the tutor works", with assets you are allowed to ship

🔵 **The recipe that `P782` says half this shelf cannot support — so this is the version that
survives the licence read.**

1. 🟢 **Pick the harness by *language*, not by stars**, because an evaluation in the learner's
   language is worth more than a better one in English:
   **Spanish →** [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) (MIT) ·
   **Portuguese →** [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) (MIT) ·
   **Indonesian →** [`indobenchmark/indonlu`](https://github.com/indobenchmark/indonlu) (Apache-2.0) ·
   **English/general →** [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) (Apache-2.0).
2. 🟢 **Add a *pedagogy* dimension, not just accuracy:**
   [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT).
   🔵 A tutor that is right and unteacherly fails the pilot.
3. 🟢 **Add the failure mode specific to tutors:**
   [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) (MIT) — sycophancy. 🔵 A tutor
   that agrees with a wrong answer is worse than no tutor, and this is the only asset on the shelf
   that measures it.
4. 🟢 **Voice deployments:**
   [`AI-for-Education/voice-ai-evaluation-framework`](https://github.com/AI-for-Education/voice-ai-evaluation-framework) (MIT).
5. 🔴 **Do not build on these, and know why before someone proposes them:**
   `Khan/tutoring-accuracy-dataset` — 🔴 **bespoke licence: evaluation only, no training, no
   production, no publication** (`P783`); `Yunfeng-Wan/CSTutorBench` — 🔴 **CC BY-NC 4.0**;
   `haolpku/K12-KGraph` — 🟡 **MIT code, CC BY-NC-SA data** (evaluate, don't resell);
   and the **8 ungranted** repos named in `repos/foundations.md`.
6. 🟢 **Gate the finished evaluation harness itself:**
   `bash p782-policy-gate/gate.sh assessment_grading <jurisdiction>` — 🔵 **an automated scorer is
   a regulated function even when it is only scoring your own system in a lab**, if its output
   reaches a learner's record.

### 🟢 `R61c` — the teacher-in-the-loop checkpoint, built once and lawful in three regions

🔵 **Trend 1 makes this the highest-leverage component to get right, because the same artefact
discharges three different obligations.**

🟢 **Build:** a review queue between the agent's output and any **write** to the learner's record —
LTI AGS grade passback, an LMS comment, or an xAPI statement of mastery. 🟢 **Each queued item
carries** the agent's proposal, its evidence, the teacher's accept/modify/reject, and the identity
of the teacher who decided. 🟢 **Persist the decision to the LRS as its own xAPI statement**, so
the audit trail and the learning record are the same store.

🟢 **What it discharges:** **US-Idaho** — AI has not replaced the teacher, the teacher decided ·
**Philippines** — AI is demonstrably supplementary · **Singapore** — teacher supervision is
structural, not procedural · **EU Annex III** — "human oversight" has an artefact from
**2027-12-02**, and 🟢 **the FRIA an EU public school owes under Article 27 can cite it.**

🔴 **The anti-pattern to name in the proposal:** a checkpoint the teacher can bulk-approve without
reading. 🔵 It satisfies an architecture diagram and none of the four obligations, because the
evidence it produces shows nobody looked.

## 🟢 Sixtieth pass, 2026-10-08 — `R60a`: the first recipe on this shelf that can **read a roster and write a learning record**, both permissively licensed

⏱️ **Fourteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

🔴 **Every recipe before this pass ended at a model or an agent and then integrated with "the SIS"
in prose.** 🟢 **The two standard edges now have payload-read permissive implementations**, so the
loop closes in named components.

### 🟢 `R60a` — governed AI tutoring on an existing LMS, evidence-first

**Target:** a district or university that already runs Moodle / Open edX / Canvas and must show a
regulator *what the AI did, to whom, and who reviewed it.*

| # | Layer | Component, pinned | Licence | Wiring |
|---|---|---|---|---|
| 1 | **Launch** | `Cvmcosta/ltijs` (npm **v7.0.7**, 2026-10-06) | 🟢 Apache-2.0 | LTI 1.3 tool provider. The LMS launches the tutor; `ltijs` validates the platform JWT and yields the user, context and roles. **Nothing downstream trusts a request without this.** |
| 2 | **Identity / scope** | [`longsightgroup/oneroster`](https://github.com/longsightgroup/oneroster) `8c14777` (TS) or [`TCI/OneRoster`](https://github.com/TCI/OneRoster) `5f8a15a` (Ruby) | 🟢 MIT | Resolves the launch context into **section, teacher-of-record and enrolment**. This is what makes per-teacher audit and per-section opt-out expressible. |
| 3 | **Mastery model** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) `5fea390` | 🟢 MIT | **BKT** for mastery + **FSRS 4.5** for scheduling, local-first (FastAPI + Next.js). Pin BKT per skill from the roster's course mapping. 🟢 Alternatives on the same licence: `tswsxk/TKT` `6f33e4a`, `jdxyw/deepKT` `985c67f`. |
| 4 | **Retrieval** | [`098765d/AI_Tutor`](https://github.com/098765d/AI_Tutor) `e7503b7` | 🟢 MIT | KG-RAG: course PDFs → `[Entity, Relation, Entity]` triples → graph traversal. Use **instead of** flat RAG where the curriculum has prerequisite structure, because the graph is also the explanation. |
| 5 | **Evidence** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) `cb794e4` (SQL) or [`openfun/ralph`](https://github.com/openfun/ralph) `53cc58c` (MIT, EMEA-origin) | 🟢 Apache-2.0 / MIT | **Every** tutor turn, mastery update and human override is an xAPI statement. 🔵 This is the layer that answers a regulator; steps 3–4 answer the learner. |
| 6 | **Human-review gate** | the deployment's own code | — | 🔴 **Non-negotiable, and jurisdiction-shaped** — see the gate below. |

🟢 **Why `lrsql` is the default at step 5:** it runs on an RDBMS the client already operates, so the
architecture adds no datastore and no new backup/retention story — the two things that stall a
public-sector review. 🟢 **Choose `ralph` instead when the buyer is EU public sector**: MIT, and its
provenance (France Université Numérique) is itself procurement evidence.

### 🔴 The two-axis pre-flight, and it is **still prose** (`Gap 278`)

🔴 **Licence clear ≠ lawful.** `algorithm0r/canvas-lms-mcp` is **MIT** and exposes grading, comments
and rubrics — it clears every licence check this KB has written and is **prohibited** in US K-12
public (`P764`). 🟢 **Run both axes before wiring step 6:**

| Axis | Question | Instrument |
|---|---|---|
| **Grant** | may we build on it? | 🟢 `p419-copyleft-identity` for the family; the four-layer locator for *where the grant is*; 🆕 **and now `Gap 282`: enumerate *all* licence files, because scope can be partitioned** |
| **Data** | may we ship the corpus? | 🆕 `P779` — **check the dataset licence separately.** ArguLens is Apache-2.0 over a **CC BY-NC-SA** corpus; K12-KGraph is **MIT code / CC BY-NC-SA data** |
| **Function** | is this function lawful *here*? | 🔴 prose only — `(function, jurisdiction) → GATED \| PROHIBITED \| UNREGULATED` is still unbuilt |

🟢 **Jurisdiction shape for step 6, as currently shelved:** **US K-12 public** — AI-assisted grading
of record is **prohibited** in the largest district and gated elsewhere, so the gate is *draft-only,
teacher commits*. **EMEA** — gated: Annex III conformity file, Art. 50 marking live. **APAC
(Vietnam)** — high-risk **only** where the output is the sole basis without meaningful human review,
so a logged human decision is the compliance artefact. **LATAM** — unregulated, so the gate is the
institution's own framework and the ~74 % without one are the buyers.

### 🟢 `R60b` — permissive automated essay scoring, with the corpus problem stated up front

| # | Component, pinned | Licence | Note |
|---|---|---|---|
| 1 | [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) `41ae3bd` (ArguLens) | 🟢 Apache-2.0 | Discourse-move classifier + **LightGBM** over 31 linguistic features + LLM feedback. 🟡 Reported mean QWK **0.813**, component-level under an oracle-feature protocol — **not** end-to-end. |
| 2 | 🔴 **the corpus** | 🔴 CC BY-NC-SA 4.0 | **PERSUADE 2.0 cannot ship commercially, and ShareAlike reaches derivatives.** 🟢 **The engagement must bring its own scored corpus** — which is normally the client's own historical marking, and that is a *better* asset anyway because it encodes their rubric. |
| 3 | [`haolpku/K12-KGraph`](https://github.com/haolpku/K12-KGraph) `865bc35` | 🟢 MIT code / 🔴 NC data | Curriculum-aligned evaluation. **Use to measure, not to resell.** |
| 4 | human-review gate + `lrsql` | 🟢 Apache-2.0 | Scores are **drafts**; the teacher commits; the LRS records both the draft and the override. 🔵 This is simultaneously the US prohibition work-around and Vietnam's exemption condition. |

🔴 **Do not reach for `edx/ease`** (`056da0a`): **AGPL-3.0** and **archived read-only since Feb
2024**. 🟡 **`markm-io/ai-essay-evaluator`** (`8ee5c7c`, MIT) is a usable harness — batch grading,
multi-pass consistency, fine-tuning on your exemplars — but it **wraps the OpenAI API**, so it is
permissive code and **not** a self-hostable scorer. 🔵 **State that distinction to any client who
said "on-prem".**

## 🟢 Fifty-ninth pass, 2026-10-08 — `R57a`'s stale authentication boundary gets a **live component released two days ago**, the pre-flight gains a **policy gate** beside its licence gate, and `R59a` is the first recipe whose selector starts with a jurisdiction

⏱️ **Thirteenth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

### 🟢 `P766` — `Gap 276` **CLOSED**: two actively-released permissive LTI 1.3 tool-side libraries exist, and `R57a` now has a component instead of a hole

🔴 **Pass 58 dated `R57a`'s authentication boundary at 3 y 11 mo stale and declared `Gap 276`
because no actively-released permissive alternative had been licence-measured.** 🟢 **Both halves
are now measured:**

| Component | Licence (payload, SHA-pinned) | Release oracle | Verdict for `R57a` |
|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0, `LICENSE` 11 361 B @ `0ec24fe` | 🟢 npm `ltijs` **v7.0.7, published 2026-10-06** | 🟢 **Adopt (Node).** Two days old at this pass. Deep Linking, AGS, NRPS, Dynamic Registration. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0, `LICENSE.md` 11 343 B @ `a20c71b` | 🟢 packagist `packbackbooks/lti-1p3-tool` **v6.4.4, 2026-09-23** | 🟢 **Adopt (PHP).** Maintained fork of the spec body's library; Names&Roles + AGS. |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | Apache-2.0, `LICENSE` 11 343 B @ `3a192de` | — | 🟡 Reference only — the spec body declines vendor-specific changes. |
| [UOC/java-lti-1.3](https://github.com/UOC/java-lti-1.3) | MIT, `LICENSE` 1 060 B @ `e673616` | — | 🟡 Viable on the JVM; no release oracle measured. |
| `PyLTI1p3` (the incumbent) | MIT | 🔴 PyPI **v2.0.0, uploaded 2022-11-20** | 🔴 **Replace.** 3 y 10,6 mo at this pass. |

🟢 **And `P743` is resolved while we are here:** the package is **`PyLTI1p3`**; `pypi.org/pypi/pylti1.3/json`
returns **`404`**, which is why pass 57's registry probe found nothing to date.

🔵 **Why this is load-bearing and not a version bump:** `R57a`'s whole claim is that LTI 1.3 keeps
the platform's copyleft away from Globant's code, and the thing standing on that boundary is the
JWT validation path. 🔴 **A 2022-frozen library on the authentication boundary is the worst place
in the recipe to carry staleness.** 🟢 **It is now a library released two days before this pass.**

### 🟢 `P767` — `R59a`: build on the **integration tier**, and choose the connector by licence *and* by jurisdiction

🔵 **The recipe this pass adds, concretely, with the measured components:**

```
GOAL: an AI capability over an existing institutional LMS, where Globant's code stays
      proprietary AND the deployed function is lawful in the buyer's jurisdiction.

STEP 1 — pick the boundary, not the platform.            (P763)
  Canvas / Open edX (AGPL-3.0) or Moodle (GPL-3.0) as substrate: do NOT fork it.
  Drive it from outside.  Two boundaries measured:
     LTI 1.3   -> Cvmcosta/ltijs            Apache-2.0  @0ec24fe  npm v7.0.7 2026-10-06
     MCP       -> vishalsachdev/canvas-mcp   MIT        @eeeb479  (Canvas, ~103 tools)
                  algorithm0r/canvas-lms-mcp MIT        @2a5a7f1  (Canvas, 165 tools)

STEP 2 — the Moodle trap, stated before you hit it.      (P763a)
  Moodle's own substrate is GPL-3.0: strong copyleft, NO network clause.
  But csmediapro/moodle-mcp-server is AGPL-3.0 (34 523 B @5a194a5) -> §13 binds a
  HOSTED service.  And onbirdev/moodle-webservice_mcp is GPL-3.0-or-later and is a
  PLUGIN -> inside the GPL boundary by construction.
  => On Moodle, the permissive route is LTI 1.3 with ltijs.  NOT MCP.

STEP 3 — the jurisdiction gate, BEFORE any grading capability is wired.  (P764)
  algorithm0r/canvas-lms-mcp exposes grading, comments and rubrics under MIT.
  MIT clears the LICENCE axis.  It does not clear the POLICY axis:
     US K-12 public (NYC red tier)  -> grading/promotion/discipline/IEP/placement
                                        PROHIBITED.  Do not wire these tools.
                                        Ship the green tier instead (step 4).
     EU                             -> Annex III high-risk: permitted, GATED.
                                        Wire it, plus the P710 conformity pipeline.
     Vietnam / Korea                -> high-risk listed / pilot year.  Wire it, gated.
     LATAM                          -> no education-specific instrument located.
                                        Specify against EU Annex III anyway (P765).

STEP 4 — the surface that is open everywhere, and is what NYC kept open twice.
  Teacher-facing: translation, organising information, lesson planning, drafting
  family/staff communications.  Read-only LMS access is sufficient for all four
  (csmediapro's server is read-only BY DESIGN -- but see step 2 on its AGPL).

STEP 5 — scoring, only where step 3 permitted it.
  The-LLM-Data-Company/rubric  MIT  @eb0755a  PyPI 2.2.0 2026-01-21  (weighted rubrics)
  akturkumut/Automated-Exam-Scoring-LLM  Apache-2.0 @5e141c4  (Qwen3-4B+SBERT+LoRA, OCR)
  microsoft/LLM-Rubric         MIT  @030ab16  (calibrated, multidimensional)
  Two independent scorers + disagreement escalation, per P720.
```

### 🟢 `P768` — the pre-flight gains a **policy gate**, and the licence gate gains the two layers that caught this pass

🔴 **Every pre-flight in this file (`P649`, `P712`, `P721`, `P737`, `P751`) checks licences only.**
🟢 **This pass found two failures neither shape could catch** — a prohibited *function* under a
permissive licence, and a grant that exists in no file at all. 🟢 **Replacement pre-flight:**

```bash
# ---------- AXIS 1: the GRANT.  Four layers, because filenames are only the first.
# layer 1 — licence file (15 names), SHA-pinned: ls-remote supplies the sha (api.github.com=403)
SHA=$(git ls-remote https://github.com/$SLUG HEAD | awk '{print $1}')
for n in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENSE-MIT LICENSE-APACHE \
         COPYING COPYING.txt COPYING.LESSER LICENSE.rst license license.md LICENSE.code LICENSE-CODE; do
  curl -s -o /dev/null -w "$n %{http_code}\n" https://raw.githubusercontent.com/$SLUG/$SHA/$n; done
# layer 2 — READ BELOW A REFERENCE.  A LICENSE that opens with "see the COPYRIGHT file"
#           may still carry the grant underneath it.  openeducat is LGPL-3.0 this way. (P742)
# layer 3 — manifest / registry: setup.py, pyproject.toml, package.json, then pypi/npm/packagist.
#           The registry is the only DATED oracle -- it is what revealed PyLTI1p3's 2022. (P741)
# layer 4 — SOURCE HEADERS.  0 licence files does NOT mean ungranted:
#           onbirdev/moodle-webservice_mcp grants GPL-3.0-or-later in every .php header. (P757)
curl -s https://raw.githubusercontent.com/$SLUG/$SHA/version.php | grep -i "General Public License"
# Only after all four layers come back empty: ALL RIGHTS RESERVED.  That is a verdict. (P476)

# ---------- CLASSIFY with the shelf's instrument.  Do NOT hand-roll this. (Trend 1, P753)
#   Use compose/code/p419-copyleft-identity/.  It windows to the TITLE LINE and quarantines
#   kinship in a separate field.  A "contains affero" or "§13 present" test reads GPL-3.0 as
#   AGPL -- GPL-3.0 names Affero 3 times and titles its §13 after it.
#   And byte count cannot break the tie: GPL-3.0 35 147 B vs AGPL-3.0 35 136 B, 11 B apart. (P754)

# ---------- AXIS 2: the FUNCTION.  New, and orthogonal to axis 1. (P764)
#   For the deployment jurisdiction, is the function GATED or PROHIBITED?
#   grading | promotion | discipline | counselling | IEP/504 | academic placement
#     -> US K-12 public (NYC):     PROHIBITED.  A permissive licence does not help.
#     -> EU:                       GATED (Annex III).  Build the conformity pipeline.
#   A tool can pass axis 1 and fail axis 2: algorithm0r/canvas-lms-mcp is MIT and grades.
```

### 🟢 `P769` — the named replacement queries `Gap 274` asked for, with this pass's measured yield

🔴 **`github trending {industry} AI {year}` has returned zero education repositories for ten
weeks.** 🟢 **It stays, because it is mandated.** 🟢 **These run *beside* it, and these are what
produced all 12 of this pass's rows:**

| Query | Yield this pass | Defect rate |
|---|---|---|
| `open source LTI 1.3 library MIT Apache tool provider {year} maintained` | **5 rows**, all permissive, 2 with live release dates | 🟢 **0 of 5** |
| `github open source LMS AI agent Moodle Canvas plugin MCP {year}` | **4 rows** — a category this KB did not have | 🟢 **0 of 4** |
| `github open source automated essay scoring rubric grading LLM {year} MIT license` | **3 rows** admitted, **4 refused** | 🔴 **4 of 7 = 57 %** |
| `github open source intelligent tutoring system agent knowledge tracing {year} release` | 0 admitted — 5 candidates named but not licence-measured | — (`Gap 279`) |

🔵 **The pattern across all four: name the *protocol* or the *function*, never the industry.**
🟢 **"LTI 1.3", "MCP", "rubric scoring" and "knowledge tracing" are the strings that return
education-native software; "education AI" returns courseware and general agent frameworks.**
🔴 **And pair every one of them with the four-layer grant check above — the productive channel is
also the dishonest one (Trend 4).**

### 🔴 `P770` — `curl -sI https://github.com/<slug>` is **not** an existence check in this environment, and a pass that trusted it would have published nothing

🔴 **The mandated quality bar says to verify every URL with `curl -sI` before writing it. Measured
here, that instruction is unsafe:**

| Probe | Real repo (`moodle/moodle`) | Non-existent slug | Discriminates? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | **403** | **403** | 🔴 **No — blind** |
| `git ls-remote https://github.com/<slug> HEAD` | 🟢 sha `f205347` | 🟢 fails | 🟢 **Yes** |
| `raw.githubusercontent.com/<slug>/<sha>/LICENSE` | 🟢 `200` | 🟢 `404` | 🟢 **Yes** |

🔴 **All 22 github.com URLs written this pass return `403`**, `moodle/moodle` and
`instructure/canvas-lms` among them. 🟢 **A `403` here carries no information about existence**, so
reading it as a pass would be as wrong as reading it as a `404`.

🟢 **How the 21 slugs in this pass were actually verified: both discriminating oracles, on every
one, with the negative control run in the same batch** — `ls-remote` returned a SHA for 21 of 21
and failed on the control, and every published SHA is the one the payload was read at.
🔵 **Same shape as `P745`** (probe the endpoint, not the host) and `P728` (identity proved
*through* a 403 channel, never *by* it).

### 🟢 Which recipe for which engagement — the one-line selector, updated

| Engagement | Recipe | Why |
|---|---|---|
| 🇺🇸 **US K-12 public**, any AI ask | 🟢 `R59a` **steps 1–2 and 4 only** | 🔴 Grading is prohibited, not gated (`P764`). Teacher green tier is the whole sellable surface. |
| 🇪🇺 **EU**, assessment or admissions | 🟢 `R59a` + `P710` conformity pipeline | Annex III gated; conformity artefacts are legally required and therefore billable. |
| 🇪🇺 **EU public tier**, procurement | 🟢 `R57b` pre-flight, EUPL band | Eight Finnish national education services are EUPL; it is a procurement precondition. |
| 🌏 **Vietnam / Korea** | 🟢 `R59a` + `P710`, with `P706`'s trigger condition | The clearest written assessment spec anywhere; Korea's grace year is a dated window. |
| 🌎 **LATAM**, institution with adopted tools | 🟢 Governance retrofit first, then `R59a` | 87 % adoption, lagging governance; assessment adoption still low, so no unwinding needed (`P765`). |
| **Any**, proprietary module on an education ERP | 🟢 `R58a` — Odoo + OpenEduCat, **LGPL-3.0** | The only weak-copyleft band on the shelf; an addon may stay proprietary. |
| **Any**, integrate without inheriting copyleft | 🟢 `R57a` with **`ltijs`** (Apache-2.0, 2026-10-06) | `P766` — the boundary finally has a live component. |


## 🟢 Fifty-eighth pass, 2026-10-08 — `R57a`'s LTI component is **3 y 11 mo stale** and gets a decision, and `R58a` is a **second substrate** on the LGPL band where a proprietary module is lawful

⏱️ **Twelfth pass of this date. Append-only: this section is new; nothing below it was rewritten.**

> 🔵 **This pass's opening hypothesis was that `R57a` needed only a freshness note.
> 🔴 **REFUTED twice over:** 🔴 **the staleness is worse than pass 57 could state (and its package name was wrong — `P743`), and the licence census correction (`P742`) opened a substrate `R57a` could not have used.**

### 🔴 `P746` — `R57a`'s `pylti1.3` row, measured and decided

🔴 **Pass 57 flagged the component stale and left the recipe pointing at it.** 🟢 **Measured this pass:**

| `dmitry-viskov/pylti1.3` | Reading |
|---|---|
| Repository payload | 🟢 **MIT**, `LICENSE`, **1 070 B**, *"Copyright (c) 2019 Dmitry Viskov"* |
| 🔴 **PyPI name** | 🔴 **not `pylti1.3`** — that returns `NOT_FOUND`. The distribution is **`PyLTI1p3`** |
| Registry grant | 🟢 **MIT** (`license` field + OSI classifier) — 🟢 **agrees with payload** |
| Version | **2.0.0** |
| 🔴 **Last release** | 🔴 **2022-11-20 — 3 years 11 months before this pass** |

🟢 **The licence is not the problem; the maintenance is.** 🔵 **LTI 1.3 is a *specification*, and `pylti1.3` implements the tool side of a spec that has itself moved (LTI Advantage services, `NDC`-style version increments on the 1EdTech side) — so a four-year gap is a security and conformance question, not merely a tidiness one.**

> 🟢 **`P746` — the decision, so no later pass re-litigates it.** *Keep `PyLTI1p3` in `R57a`, and **pin, vendor and own it**:*
> 🟢 **(1)** pin `PyLTI1p3==2.0.0` explicitly — 🔵 **MIT permits the fork, and an unmaintained MIT dependency is the cheapest possible thing to take over**;
> 🟢 **(2)** treat it as **Globant-maintained** from day one: budget the JWT/JWKS review in the engagement, do not assume upstream;
> 🔴 **(3)** do **not** swap it for a maintained alternative on licence grounds without reading payload first — 🔴 **`P733` and `P747` are two consecutive passes of a channel naming the wrong licence for a platform it recommended.**
> 🔵 **The boundary argument of `P736` is untouched by this**: LTI 1.3 is still a network protocol, and a stale *client library* is a maintenance liability inside Globant's own repository, not a copyleft exposure.

### 🟢 `P750` — `R58a`: build an education ERP module on the **LGPL band**, where the addon may stay proprietary

🟢 **New recipe, made possible only by this pass's correction (`P742`) and the band taxonomy (`P747`).** 🔴 **For eight passes the vertical channel's answer was *"no permissive education platform exists, so build it yourself"*, and this KB had no platform-layer answer but LTI isolation.** 🟢 **There is now a second one.**

| Layer | Component | 🟢 **Licence (payload, first-hand)** | Why it sits here |
|---|---|---|---|
| **ERP framework (client-hosted)** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🟡 **LGPL-3.0** · **43 529 B** · 97 heads | 🟢 **No network clause** — hosting triggers nothing |
| **Education domain layer** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** · **8 241 B** · **992 refs** | 🟢 **Education-native**: admissions, courses, faculty, exams already modelled |
| 🟢 **Isolation boundary** | **An Odoo addon directory** — a module the framework loads, never a core patch | 🟢 **n/a — a packaging boundary** | 🟢 **LGPL §4**: a work that *links* the library may ship under your own terms |
| 🟡 **Your module (Globant-built)** | custom models + AI endpoints | 🟢 **Globant's own terms — proprietary is lawful here** | 🟡 **Read `Gap 279` before relying on this** |
| 🟢 Grading core | [`delip/autorubric`](https://github.com/delip/autorubric) + [`The-LLM-Data-Company/rubric`](https://github.com/The-LLM-Data-Company/rubric) | 🟢 MIT **1 402 B** · MIT **1 077 B** | 🟢 `P720` two-scorer cross-check; 🟢 **`autorubric` released 2026-09-27 — 11 days (`P741`)** |
| 🟢 Human gate | `P710` steps 3–4 | 🟢 n/a | 🔴 **Non-negotiable** — and it is what the LATAM 19 %/79 % gap actually needs |

🟢 **Wiring, concretely:** 🔵 **(1)** client runs Odoo + OpenEduCat (their deployment, their LGPL obligations, unchanged); 🔵 **(2)** Globant ships `globant_edu_ai/` as an **addon directory** — `__manifest__.py`, new models inheriting `op.student` / `op.exam` via Odoo's ORM, no edits to core files; 🔵 **(3)** the addon calls `autorubric` → `rubric` for the two-scorer cross-check (`P720`); 🔵 **(4)** disagreement between scorers routes to the human gate and the decision is logged; 🔵 **(5)** the score is written back through OpenEduCat's own exam models, not a side table.

> 🟢 **`P750`.** *`R57a` and `R58a` are **not** alternatives — they answer different client estates.* 🟢 **`R57a` (LTI 1.3) is for an estate built on an **LMS**: Moodle GPL-3.0, Canvas and Open edX **AGPL-3.0** — where you must stay outside the process.** 🟢 **`R58a` (Odoo addon) is for an estate built on an **ERP/SIS**: Odoo and OpenEduCat **LGPL-3.0** — where you may stand inside the framework and keep your module.* 🔵 **The band, not the product, picks the recipe (`P747`).**

🔴 **Two conditions, or `R58a` leaks — the same structural discipline as `P736`:** 🔴 **(a)** the moment Globant patches an Odoo or OpenEduCat **core file**, that file is LGPL and owed back — *"a quick fix in core"* dissolves the boundary; 🔴 **(b)** 🆕 **`Gap 279` is open**: whether an Odoo addon is a *"work that uses the library"* (LGPL §4) or a derivative of it depends on how Odoo's ORM loads modules, and **this KB has not read that loader**. 🟡 **Odoo's own commercial addon ecosystem is strong practical evidence for the permissive reading, and practice is not a licence analysis.** 🟢 **`P744` does not block closing this — it is a single named repository to read, so a later pass can settle it.**

### 🟢 `P751` — the licence pre-flight gains the two checks that caught this pass's errors

🟢 **`P710`'s pre-flight is an instrument, not advice (pass 57). 🔴 **It would have passed `openeducat` as ungranted and `pylti1.3` as absent from PyPI.** 🟢 **Two steps added, both earned by a measured failure:**

| # | Check | 🔴 **The failure it prevents** |
|---|---|---|
| 🆕 **0** | 🟢 **Ask whether this KB already holds a committed verdict on the slug** — `compose/code/p752-prose-vs-committed-results/check_claim.sh owner/repo [family]` | 🔴 **`P752` — pass 57 published "ungranted" for `openeducat` against **31** committed TSV lines reading `LGPL`, in 8 instruments.** 🟢 **Costs nothing, needs no network, and is the only step that catches an error no probe can** |
| 1 | Try **19** filenames including `COPYING`, `COPYING.txt`, lowercase `license.txt` | 🔴 `P727` — 3 GPL repos read as ungranted |
| 2 | Classify from the **title window**, never the whole body | 🔴 `P726` — GPL-3.0 §13 names Affero 3×, inverting every GPL file |
| 3 | 🆕 **Scan the whole licence file for a *grant body*; never conclude from an unresolved *reference*** | 🔴 **`P742` — `openeducat` LGPL-3.0 read as ungranted because its `COPYRIGHT` pointer `404`s while the grant sat 2 lines below** |
| 4 | 🆕 **Resolve slug → **distribution name** before any registry query** | 🔴 **`P743` — `pylti1.3` returns `NOT_FOUND`; the package is `PyLTI1p3`** |
| 5 | Cross-check the registry record (`license_expression`, OSI classifier) **and its upload date** | 🟢 `P741` — a second grant oracle, and the only dated one |
| 6 | 🔴 **Never accept a channel's licence claim as the classification** | 🔴 `P733` (Huly: Apache→**EPL-2.0**) · 🔴 **`P747` (Twenty: BSL→**AGPL-3.0**)** |

🔴 **And one check this pass can specify but **not** automate (`P744`):** 🟢 **steps 1–6 run fine on a **named** repo and the environment denies running them over a **shelf**.** 🔵 **So the pre-flight is a per-engagement gate — which is in fact its real use — and not a monitoring sweep.** 🆕 **`Gap 276` — the named-sample instrument shape has no implementation on this KB; all 138 in `compose/code/` assume enumeration.**

### 🟢 Which recipe for which engagement — the one-line selector

| Client estate | Recipe | Boundary | Your code's licence |
|---|---|---|---|
| Moodle (**GPL-3.0**) · Canvas / Open edX (**AGPL-3.0**) | 🟢 **`R57a`** (`P736`) | 🟢 **LTI 1.3** — HTTP + JWT, a separate process | 🟢 **MIT / your own** |
| Odoo · OpenEduCat (**LGPL-3.0**) | 🟢 **`R58a`** (`P750`) | 🟢 **Odoo addon directory** — LGPL §4 linking | 🟢 **Your own, proprietary lawful** |
| ERPNext (**GPL-3.0**) · Twenty (**AGPL-3.0**) | 🔴 **Neither — treat as LMS-class** | 🔴 No weak-copyleft route: GPL derivative / AGPL §13 | 🔴 **Owed back if you modify or host** |
| Unknown platform | 🔴 **Run `P751` first** | — | 🔴 **Undecidable until payload is read** |

---


## 🟢 Fifty-seventh pass, 2026-10-08 — **LTI 1.3 is the licence-isolation boundary**, the licence pre-flight is now an instrument rather than advice, and `P710` gains a permissive substrate

> 🔵 **This pass's opening hypothesis was that the licence census would mostly reorder the shelf.
> 🟢 CONFIRMED, and it produced one recipe nobody had written:** 🟢 **the measured fact that
> education's **platform** layer is copyleft (Moodle GPL, Open edX and Canvas **AGPL**) while its
> **integration** layer is permissive (`pylti1.3` MIT) is not a coincidence to note — it is an
> architecture to adopt.**

### 🟢 `P736` — `R57a`: integrate through **LTI 1.3**, and the platform's copyleft never reaches your code

🔴 **The recurring question on this KB is "can Globant build on Moodle / Canvas / Open edX given
GPL and AGPL?"** 🟢 **Measured answer (`P734`): you do not build *in* them. You build *beside* them
and speak LTI.**

| Layer | Component | Licence (first-hand, stored bytes) | Why it sits here |
|---|---|---|---|
| **Platform (client-hosted)** | Moodle · Canvas · Open edX | 🔴 **GPL-3.0** 35 147 B · 🔴 **AGPL-3.0** 34 520 B · 🔴 **AGPL-3.0** 35 136 B | 🔴 **Never modified, never vendored, never linked** — the client already runs it |
| 🟢 **Isolation boundary** | **LTI 1.3 / LTI Advantage** — an HTTP + JWT protocol, not a library dependency | 🟢 **n/a — a specification** | 🟢 **This is the whole trick**: a separate process over a network protocol is not a derivative work |
| 🟡 **Your tool (Globant-built)** | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) + its django/flask examples | 🟢 **MIT** · **1 070 B** each | 🟢 LTI 1.3 tool-side in permissive Python. 🔴 **Read `P740` before adopting — it is stale** |
| 🟢 Grading core | [`delip/autorubric`](https://github.com/delip/autorubric) + [`The-LLM-Data-Company/rubric`](https://github.com/The-LLM-Data-Company/rubric) | 🟢 MIT **1 402 B** · MIT **1 077 B** | 🟢 `P720`'s two-scorer cross-check, unchanged |
| 🟢 Grade return | LTI **Assignment and Grade Services** (AGS) | 🟢 n/a | 🟢 Writes the score back without touching platform source |
| 🟢 Rostering, if needed | [`Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration) | 🟢 **Apache-2.0** **11 357 B** | 🟢 Permissive rostering |

🟢 **Wiring, concretely:** 🔵 **(1)** register the tool in the platform as an LTI 1.3 tool (client id,
deployment id, JWKS URL); 🔵 **(2)** `pylti1.3` validates the launch JWT and gives you the user,
context and resource-link claims; 🔵 **(3)** the launch hands off to `autorubric` → `rubric`
cross-check (`P720`); 🔵 **(4)** the human-review gate (`P710` steps 3–4) logs the decision; 🔵 **(5)**
AGS posts the score back. 🟢 **Your repository contains MIT code only.**

> 🟢 **`P736`.** *The licence question in education software is **architectural, not legal**. 🔴 **"Can
> we use Moodle?" is the wrong question** — you are not using it, the client is. 🟢 **LTI 1.3 is a
> process and network boundary, so GPL's and AGPL's derivative-work and §13 triggers do not reach a
> tool on the other side of it.*** 🔵 **This is why the shelf's licence split (AGPL in platforms, MIT
> in integration — `P730`) is the map of where to stand.** 🔴 **Two conditions, or the boundary
> leaks:** 🔴 **do not vendor platform code or link its libraries**, and 🔴 **do not ship a modified
> platform** — the moment you distribute a patched Moodle, you are inside GPL again.

### 🔴 `P740` — `R57a`'s LTI component is **MIT and four years stale**, and the registry is what reveals it

🔴 **`pylti1.3` is load-bearing in `R57a`, so it was measured properly rather than cited. The repo
channel looks healthy and the registry channel does not:**

| Oracle | Reading |
|---|---|
| `ls-remote` | exists · HEAD `d8fa43e1` · 🟡 **1** `refs/heads` · 🟢 **29** `refs/tags` · 88 `refs/pull` · 119 all |
| 🟢 Licence payload | 🟢 `MIT License`, **1 070 B** |
| 🟢 PyPI `PyLTI1p3` | 🟢 **v2.0.0**, `license: MIT`, homepage resolves to the same repo, **29 releases** |
| 🔴 **PyPI latest upload** | 🔴 **`2022-11-20`** — **no release in ~3 years 11 months** |

🟡 **88 inbound pull refs say people are still sending patches; 1 branch and a 2022 release say
nothing is being cut.** 🔵 **LTI 1.3 is a *stable specification*, so a stale implementation is far
less alarming here than it would be for a model-facing library** — the protocol it implements has not
moved either.

> 🔴 **`P740`.** *The repo channel cannot see staleness: `ls-remote` showed 29 tags and a valid HEAD.
> 🟢 **The registry's `upload_time` is the recency oracle**, and it is the only channel here that
> dates anything.* 🟢 **Adopt `pylti1.3` with eyes open**: pin the version, expect to maintain the
> fork, and budget a security review of the JWT validation path — 🔴 **which is the one part of an
> LTI tool where staleness is genuinely dangerous**, because it is the authentication boundary.
> 🆕 **`Gap 276` — no permissive, actively-released LTI 1.3 tool-side library has been identified;
> the alternatives on this shelf were not licence-measured this pass.**

### 🟢 `P737` — `R57b`: the licence **pre-flight**, now an instrument instead of advice

🟢 **Every recipe on this shelf has needed this and none had a runnable form. `P725` built it:
`compose/code/p725-readme-payload-sweep/`.**

🟢 **Run it before an engagement, over the client's existing edtech stack:**

```
grep -rhoE 'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' <client-manifests>/ \
  | sort -u > stack.txt
./readme_vs_payload.sh stack.txt stack.txt 12 > verdicts.tsv
```

| Then adjudicate, in this order | Because |
|---|---|
| 🔴 **`MISGRANTED` rows first** | 🔴 Copyleft believed permissive is the only direction that creates an obligation you did not plan for |
| 🔴 **`UNGRANTED` next** | 🔴 No grant means no right to use at all — but check the registry and tree layers first (`Gap 273`), a **15 %** artefact rate is measured |
| 🟡 `UNPARSED` / `NO_README` | 🟡 **193 of 1 020** land here — unadjudicated, not clean |
| 🟢 `AGREE` | 🟢 Still verify the **family**, not the string (`P734`: ECL-2.0 is Apache in substance) |

🔴 **Adjudicate by hand against the seven shapes** (`P725b`): the instrument's own false-positive rate
is **31 %** on its worst class, so 🔴 **never hand a client the raw TSV as a finding**.
🔵 **Cost: minutes of network time plus an hour of adjudication per ~50 repos.** 🟢 **Sellable on its
own in North America and EMEA** (`intel/market.md`).

### 🔴 `P738` — `R57c`: the **proctoring** recipe, which is the one place both risks land at once

🔴 **Measured convergence (`Trend 4`): proctoring is simultaneously EU Annex III, a Vietnamese
high-risk example, and the shelf's worst licence trap.**

| Decision | Recipe |
|---|---|
| 🔴 **`kamlendras/OpenProctor`** | 🔴 **Do not host it.** README says MIT; payload is **AGPL-3.0, 34 523 B**, §13 present. 🔴 **Hosting a proctoring service on it obliges you to offer source to every examinee.** 🟢 **Legitimate uses: run it on the *client's own* infrastructure as *their* deployment, or read it as a reference implementation and write your own** |
| 🟡 **`SafeExamBrowser/seb-server`** | 🟡 **MPL, 16 725 B** — reciprocal **per file**. 🟢 **Usable**: keep your code in new files, contribute back changes to theirs. 🔵 Materially safer than AGPL |
| 🟢 **The permissive path** | 🟢 Build the *decision log*, not the detector: LTI 1.3 launch (`pylti1.3`, MIT) → your evidence pipeline → human review gate → AGS. 🟢 **The regulated artefact in both jurisdictions is the human-review record, not the biometric model** |
| 🔴 **Biometrics boundary** | 🔴 **Facial recognition / behaviour analysis is what triggers Annex III duties and Vietnam's "behavioural monitoring" class.** 🟢 **Scoping it *out* is a legitimate product decision that removes a compliance tier** — say so in the proposal rather than treating it as a feature gap |

> 🔴 **`P738`.** *In proctoring the licence trap and the regulatory trigger attach at the **same
> moment** — hosting. 🟢 **So the architecture that solves one solves the other**: a separate,
> permissive, LTI-attached service whose output is a logged human decision, with biometrics
> explicitly out of scope.*

### 🟢 `P739` — `P710` gains a **permissive substrate**, which it never had

🔴 **`P710` has always assumed the client's platform, because every education-native platform on this
shelf was copyleft.** 🟢 **`P734` measured two that are not:**

| Substrate | Licence (first-hand) | Use it when |
|---|---|---|
| 🟢 **Sakai** | 🟢 **ECL-2.0**, 11 120 B — Apache-2.0 with a **narrowed patent grant** | 🟢 **A full LMS is needed and permissive is a hard constraint.** 🔴 **Read the patent clause** — it is the one real difference from Apache-2.0 |
| 🟢 **Kolibri** | 🟢 **MIT**, 1 097 B | 🟢 **Offline-first delivery** — the correct technical answer to uneven connectivity, which is the LATAM constraint by name |

🟢 **So `P710` now has three deployment shapes, not one:** 🔵 **(a)** LTI tool beside the client's
GPL/AGPL platform (`P736`, the default); 🔵 **(b)** full permissive stack on **Sakai**, when the
client has no platform and wants to own everything; 🔵 **(c)** **Kolibri** for offline/low-connectivity
cohorts. 🟡 **The 11-week estimate is unchanged** — the substrate choice moves integration risk, not
build effort.

🔴 **One correction to this shelf's own recipes:** 🔴 **any pattern here that cited `rubric`'s
"**84 refs**" as an activity signal was reading all advertised refs, of which **44 are pull
requests** (`P732`).** 🟢 **The honest figure is **19 branches + 20 tags**, and the real health signal
is PyPI **v2.2.0** with `license_expression: MIT`.**

## 🟢 Fifty-sixth pass, 2026-10-08 — `P710`'s **step 5 was the shelf's longest-standing open gap, and it now has an MIT component**, plus a pre-flight every recipe needs and a regional claim correction

### 🟢 `P719` — step 5 of `P710` ("evaluating the grader") is **no longer empty**

🔴 **`P710` has carried, for several passes:** *step 5, evaluating the grader — **nothing adoptable**,
budget ~2 of 11 weeks to build it.* 🔴 **Its three candidates all failed on licence:**
`AITutor-EvalKit` (**no grant**, `P702`), `mathtutorbench` (self-contradictory),
Open TutorAI (**CC BY-NC-SA 4.0** — non-commercial).

🟢 **A component admitted this pass fills it** (`P716`, `agents/top.md`):

| Step 5 component | Licence (first-hand) | Why it fits |
|---|---|---|
| [`The-LLM-Data-Company/rubric`](https://github.com/The-LLM-Data-Company/rubric) | 🟢 **MIT** · `LICENSE` **1 077 B** · SHA `eb0755a1` · PyPI **v2.2.0**, `license_expression: MIT` | Provider-agnostic **weighted-rubric scoring of LLM output**. 🟢 **Point it at the grader's own output** and the meta-rubric criteria become *"did it cite a span?"*, *"did it apply the stated weight?"*, *"is the justification consistent with the score?"* — which is exactly the evidence an Annex III technical file needs. |

🔵 **Why this is a real fit and not a forced one.** 🟢 **`autorubric` (step 2) scores *student work*;
`rubric` scores *model output against weighted criteria*.** 🔴 **They are not substitutes** — and
because step 5's job is to judge the step-2 grader, a library built to score model output is the
right shape. 🟢 **Both are MIT, so the pair carries no licence interaction.**

> 🟢 **`P719`.** *Step 5 drops from **~2 weeks of build** to **integration of an MIT library plus
> writing the meta-rubric** — and the meta-rubric is the part that was always the real work, because
> it is pedagogy and jurisdiction-specific, not code.* 🟡 **The gap is **narrowed, not closed**: there
> is still no education-specific *benchmark* (no items, no gold grades). 🟢 **`rubric` supplies the
> harness; the corpus is still yours** — and `OATutor-Content`'s **75,7 % `CC BY 4.0`** item-level
> grant (`P703`) is the cheapest legitimate source for it.

### 🟢 `P720` — the **two-independent-scorers** cross-check, which this shelf already trusts for licences, applied to grades

🟢 **This KB admits a licence only on agreeing oracles (`P456`, `P716`). 🟢 **The same discipline is
available for grades now that two independently implemented MIT rubric scorers exist:**

| Role | Component | Licence |
|---|---|---|
| Primary scorer | [`delip/autorubric`](https://github.com/delip/autorubric) — documented position/verbosity-bias mitigations | 🟢 MIT |
| Independent cross-check | [`The-LLM-Data-Company/rubric`](https://github.com/The-LLM-Data-Company/rubric) — different codebase, different prompt construction | 🟢 MIT |
| Divergence handler | route to the human approver (`P710` step 3/4) | — |

🟢 **Wire it as: score twice, compare, and escalate only on disagreement.** 🔵 **The operational
payoff is that the human-review budget stops being uniform** — agreement means a light touch,
divergence means a real look. 🟢 **And the divergence rate is itself the metric an EMEA conformity
file and a North American "educator supervision" audit both want**, because it quantifies how often
the machine was not trustworthy on its own.

> 🟢 **`P720`.** *Two independent MIT scorers turn "a human reviewed it" from a blanket cost into a
> **targeted** one, and produce the divergence statistic that the regional instruments ask for.*
> 🔴 **Do not ensemble them into one number** — that destroys the signal the review gate runs on.

### 🟢 `P721` — the pre-flight every recipe in this file now needs

🔴 **Two defects measured this pass mean a recipe built from this shelf can be wrong in ways nothing
downstream detects:**

| Before you build | Check | Why (`agents/top.md`) |
|---|---|---|
| 🟢 **Pin the SHA, not the branch** | `git ls-remote <repo> refs/heads/<branch>` | 🔴 `raw.githubusercontent.com` **aliases `master` to the default branch**, so a branch-pinned provenance claim returns correct bytes while being false about the ref (`P714`) |
| 🟢 **Read `LICENSE`, never the README** | `curl raw…/LICENSE \| head -4` | 🔴 README licence claims failed in **both** known shapes — *ungranted* (`AITutor-EvalKit`) and *mis-granted* (`essay-grader-llm`, README says MIT, payload is **GPL-3.0, 35 149 B**) (`P715`) |
| 🟢 **Probe each oracle `n ≥ 3`** | any success = success | 🔴 single probes produce **false negatives** at a measurable rate (`P713`); a false negative removes a working method (`P701`) |
| 🟢 **Check the item, not the repo, for content** | per-item licence field | 🔴 `OATutor-Content`: **75,7 %** `CC BY 4.0`, **24,3 %** unknown (`P703`) |

🟢 **Cost: four commands.** 🔵 **Each one corresponds to a mistake this KB actually made and
published.**

### 🔴 `P722` — the regional framing of `P710` needs one correction: the EU leg is **not** a runway

🔴 **`P710`'s regional table lists EMEA as 🟡 `2027-12-02`, which has been read as time in hand.**
🟢 **`P718` (`intel/market.md`) measured the mechanism: that date is an **absolute backstop** tied to
publication of harmonised standards, so Annex III duties can bite **earlier**.** 🟢 **And Article 50
marking is **not** deferred — live since `2026-08-02`, backstop `2026-12-02`, **three weeks out.**

🟢 **The sequencing consequence for anyone building `P710` today:**

| Build order | Why |
|---|---|
| 1️⃣ **Article 50 marking / provenance on generated feedback** | 🔴 **live obligation, backstop in three weeks** — the only genuinely urgent item |
| 2️⃣ **The human-review gate (`P706`)** | 🟢 satisfies North America (educator supervision, no sole-basis), buys **tier relief** in APAC, and is a required control in EMEA — one build, three claims |
| 3️⃣ **Rubric trace + divergence stats (`P719`/`P720`)** | 🟢 the evidence body of an Annex III technical file, and **standards-neutral**, so it survives whatever the harmonised standards say |
| 4️⃣ **The conformity file itself** | 🟡 assemble against `2027-12-02` **as a ceiling, not a date** |

🔴 **Never claim the APAC tier-relief argument in the EU.** 🔵 **Vietnam makes human review
*classification-determining*; Annex III attaches to the use case regardless. The same gate, two
different legal effects — `intel/market.md` states both.**


## 🟢 Fifty-fifth pass, 2026-10-08 — `P648` upgraded from a two-region pattern to a **four-region** one, a cheap pre-flight every recipe now needs, and a component correction that *restores* an asset

### 🟢 `P710` — the **defensible-grading pipeline** is now justified by four instruments, and the trigger condition tells you exactly what to build

🟢 **Pass 54 proposed `P648` on an EMEA + LATAM argument. This pass measured two more regions and the
pattern is the same build in all four** (`P705`, `intel/market.md`):

| Region | What forbids or exposes autonomous grading | Live? |
|---|---|---|
| APAC | Vietnam's 2026 decree — education high-risk, **automated assessment** named explicitly | 🔴 **2026-03-01** |
| North America | NYC DOE **red tier** — AI barred from grading, discipline, promotion, special-ed; Charleston County bars **sole basis** | 🔴 **live** |
| EMEA | EU AI Act **Annex III** — assessment high-risk, conformity assessment before market | 🟡 **2027-12-02** |
| LATAM | 🔴 no rule — and **74 %** of institutions grade with AI, **~25 %** have a framework | 🔴 **exposure now** |

🟢 **`P706` is the design specification, and it comes from Vietnam's own drafting:** the high-risk
flag attaches where output **drives decisions without meaningful human review**.

> 🟢 **`P710`.** *Build the grader as a **proposer**, never a decider. The regulated object in all four
> jurisdictions is an **unreviewed** machine grade; a proposed grade with a rubric trace, a cited
> span and a named human approver is a different object.* 🔵 **Human-in-the-loop is not the
> compliance cost — it is the mechanism that moves the artefact out of the prohibited class in four
> jurisdictions with one implementation.**

🟢 **The concrete wiring, with the licence of every component read first-hand this pass:**

| Step | Component | Licence | What it contributes |
|---|---|---|---|
| 1. Mastery state | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · 1 105 B | **Bayesian Knowledge Tracing** — an auditable per-skill mastery estimate, so "why this grade" has a model behind it, not a vibe. 🔴 **See `P711` for its content layer** |
| 2. Rubric scoring | [`delip/autorubric`](https://github.com/delip/autorubric) | 🟢 **MIT** · PyPI **v1.6.1** (re-confirmed this pass) | Binary / ordinal / nominal criteria, weights, multi-judge ensembles, documented **position-** and **verbosity-bias** mitigations — the scorer that produces a *rubric trace* rather than a number |
| 3. Tutoring / feedback | [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor) · [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) | 🟢 **MIT** · 1 068 B · 1 071 B | The learner-facing explanation layer; `AITutorAgent` is **LangGraph**-native, so the approver step is a graph node, not an afterthought |
| 4. Delivery surface | Moodle / Open edX gradebook | GPL-3.0 / AGPL-3.0 | 🔴 **The approver step must live in the LMS workflow** (`verticals/solutions.md`), because that is where the grade of record is written |
| 5. Evaluating the grader | 🔴 **nothing adoptable** | — | 🔴 **`AITutor-EvalKit` has no grant** (`P702`); `mathtutorbench` self-contradictory; Open TutorAI **CC BY-NC-SA 4.0**. 🟢 **Budget ~2 of 11 weeks to build it** — the gap is still open and still named |

🔴 **What NOT to put in this pipeline:** 🟢 **`plastic-labs/tutor-gpt` is GPL-3.0** — a reference for
its Theory-of-Mind approach, not a component. 🟢 **`GarethManning/education-agent-skills` is
CC-BY-SA-4.0** (pass 54, `P643`) — **ShareAlike reaches derivatives**, so it is reading material,
never a bundled step.

### 🟢 `P711` — the correction that **restores** an asset, and the licence distinction that makes it safe

🔴 **Every recipe here that warned OATutor's content was *"ungranted"* was repeating a shelf claim
this KB's own instrument had already falsified** (`P703`, `agents/top.md`). 🟢 **Measured:
`CAHLR/OATutor-Content` carries no licence *file*, a blanket **`CC BY 4.0`** grant in its README, and
a per-item grant that holds for **75,7 %** of 13 371 problems and fails for **24,3 %**.**

🟢 **So the corrected recipe instruction is per-item, and it is a build step:**

> 🟢 **`P711`.** *Gate OATutor's content **at the item**, not at the repository. Admit the **75,7 %**
> that declare `CC BY 4.0` — attribute and ship. 🔴 **Quarantine the 24,3 %**: 19,3 % empty licence
> fields, 3,6 % naming no clauses, and 1,4 % whose licence field holds an **exam-PDF URL** copied
> from the provenance field.* 🔵 **One pass over the item JSON, run once at ingest, converts a repo
> this KB was writing off into roughly ten thousand usable, attributed problems.**

🔵 **And the distinction a client needs in one sentence, because this KB now holds three CC-licensed
education corpora and they are not interchangeable:**

| Work | Licence | Reaches your derivative? | Usable in a client product? |
|---|---|---|---|
| `OATutor-Content` (the 75,7 %) | 🟢 **CC BY 4.0** | 🟢 **No** — attribution only | 🟢 **Yes, with attribution** |
| `education-agent-skills` | 🔴 **CC-BY-SA-4.0** | 🔴 **Yes** — ShareAlike | 🔴 **No** — reference only |
| `OATutor-Content` (the 24,3 %) | 🔴 **unknown** | 🔴 unknowable | 🔴 **No** — quarantine |

### 🟢 `P712` — the pre-flight every recipe in this file should start with

🔴 **Three passes in a row have been wrong about what this environment can do** (`P639`, `P700`), and
🔴 **many passes were wrong about whether work could be published at all** (`P701`). 🟢 **So every
recipe here inherits a nine-call pre-flight, and it is cheap:**

```sh
# oracles — run before trusting any licence or existence claim in this file
curl -sI -o /dev/null -w "raw=%{http_code}\n"  https://raw.githubusercontent.com/delip/autorubric/main/LICENSE
curl -sI -o /dev/null -w "raw404=%{http_code}\n" https://raw.githubusercontent.com/delip/zzz-no-repo/main/LICENSE  # must be 404: proves discrimination
curl -sI -o /dev/null -w "pypi=%{http_code}\n"   https://pypi.org/pypi/autorubric/json
curl -sI -o /dev/null -w "npm=%{http_code}\n"    https://registry.npmjs.org/h5p-standalone
curl -sI -o /dev/null -w "pkgst=%{http_code}\n"  https://repo.packagist.org/p2/moodle/moodle.json
git ls-remote --heads https://github.com/delip/autorubric >/dev/null 2>&1; echo "lsremote=$?"   # 0 = usable
```

> 🟢 **`P712`.** *A recipe that names a component is asserting a licence fact about today (`P478`).
> 🔴 **Re-probe at write time, and probe the oracle's ability to say "no" — a channel that answers
> `200` to everything confirms nothing.*** 🔵 **The `raw404` line is the whole point: it is the
> negative control, and `P700` only trusts `ls-remote` because exit `128` on a nonexistent slug
> proved it discriminates.**

## 🟢 Fifty-fourth pass, 2026-10-08 — one new recipe (`P648` the **defensible-grading pipeline**), one **correction** to every recipe that names `education-agent-skills`, and a cheap pre-flight every recipe should start with

### 🔴 The correction first, because it constrains recipes already published here

🔴 **Any recipe in this file that treats `GarethManning/education-agent-skills` as a component is
treating a **CC-BY-SA-4.0** work as if it were software.** 🟢 **Read first-hand this pass** (`P643`):
all **1 230 B** of its licence, which scopes itself to *"the educational skills, documentation,
examples, and curriculum materials in this repository"* and **carves out nothing for code**.

🔴 **Consequence for a delivery, stated plainly:** **ShareAlike reaches derivatives.** Prompts, skill
definitions, rubrics or curriculum adapted from that repo must be redistributed under CC-BY-SA-4.0.
🟢 **So it is usable as *material* — read it, learn from it, cite it — and is the wrong shape to
vendor into a client product or an Annex III technical file.** 🔵 **Creative Commons advises against
CC licences for software, which is the cleanest way to put it to a client.**

🟢 **Concretely, the fix in the recipes that name it:** keep it as a **reference** step, never as a
**bundled** step, and if an engagement wants its structure, re-derive the artefacts from the
client's own curriculum rather than adapting the files. 🆕 **`Gap 262`.**

### 🟢 `P648` — the **defensible-grading pipeline**, with the specific repos and what each contributes

🔵 **The problem it solves is the one `intel/market.md` measures in two regions at once:** LATAM's
**50 % of students want AI feedback / 19 % of faculty give it** asymmetry, and EMEA's **Annex III**
classification of assessment as high-risk. 🟢 **Both are the same engineering requirement — a grade a
human can defend — and neither is solved by a better model.**

🔴 **And it could not be built from this KB's shelves before this pass**, because the shelves named a
tutor, an authoring tool and an SIS but **no licensed thing that produces a score** (`P640`).

| Step | Component | Licence (first-hand) | What it contributes |
|---|---|---|---|
| 1 | https://github.com/delip/autorubric | 🟢 **MIT** | **the scorer**: binary / ordinal / nominal criteria, configurable weights, **multi-judge ensemble**, few-shot calibration, documented **position-** and **verbosity-bias** mitigation |
| 2 | open-weight model behind it (**Codestral-22B** class, or Llama-3.1 / Qwen) | 🟢 varies — **check per model** | **the judge**, self-hosted: **85 %** micro-accuracy vs instructor rubrics on code **with no fine-tuning** |
| 3 | https://github.com/openeducat/openeducat_erp | 🟡 **LGPL-3.0** (8 241 B) | **the system of record**: enrolment, cohorts, gradebook. 🔴 **Separate process, linked — never modified** |
| 4 | https://github.com/macsnoeren/genai-open-assessment | 🟡 **GPL-3.0** (35 149 B) | **assessment authoring**, run as a **standalone service**. 🔴 **Strong copyleft: do not vendor into the product** |
| 5 | https://github.com/grant-mccurdy/instructional-ai-workflows | 🟢 **MIT** | **the instructional wrapper**: workflow shapes a faculty member recognises |
| 6 | https://github.com/wwrwbs/AI_AWE | 🟢 **Apache-2.0** | **the writing-assessment surface**, with a patent grant — the one component safe to embed in a commercial deliverable |

**Wiring, and the ordering is the point:**

```
student artefact
  -> (5) instructional-ai-workflows   : frames the task + the rubric a human authored
  -> (1) autorubric                   : scores against THAT rubric, multi-judge, calibrated
        |  emits: per-criterion score + the criterion text + the judge + the mitigation applied
  -> (6) AI_AWE                       : renders the feedback surface the student sees
  -> (3) openeducat (separate proc)   : records the grade against the enrolment
  -> (4) genai-open-assessment (svc)  : authors the NEXT assessment from what the cohort missed
```

🟢 **What makes it *defensible* rather than merely automated**, and each is a property of step 1 and
not of the model: the **rubric is human-authored and stored**, the **per-criterion** score is emitted
rather than a single number, the **judge is named**, a **multi-judge ensemble** exists so one model's
quirk is visible, and the **bias mitigations applied are recorded**. 🔵 **That set is exactly what an
Annex III technical file has to assert and what a faculty member has to stand behind** — and it is
why the pipeline is built around a rubric library rather than a bigger model.

🔴 **The licence topology is load-bearing and is why the steps sit where they do.** 🟢 **Steps 1, 5 and
6 (MIT / MIT / Apache-2.0) are the only ones that may be *vendored*.** 🔴 **Steps 3 and 4 (LGPL-3.0,
GPL-3.0) must stay **separate processes** behind an interface** — LGPL-3.0 permits linking a separate
process, GPL-3.0 does not permit vendoring at all. 🟢 **A client asking "what ships in our product?"
gets the answer from the licence column, read first-hand, not from a vendor's claim.**

🔴 **Declared limits, so nobody inherits an untested recipe as tested:** this pipeline is **composed
from first-hand licence readings and published benchmark numbers; it has not been stood up
end-to-end.** 🔴 **No instrument of this repository was run this pass at all** (`Gap 261` — the
sandbox denied executing repo code), so there is **no suite behind `P648`**, unlike `P637`. 🟢 **Stated
rather than implied.** 🔵 **The benchmark figures (85 %, 88.56 %, 0.78 Pearson) are from papers, on
their datasets, and are not a promise about a client's rubric.**

### 🟢 `P649` — the five-call **oracle pre-flight** every recipe in this file should now open with

🔵 **Cost: five `curl` calls. Benefit, measured this pass: three passes of this KB stopped reading
licences because a capability claim was inherited instead of checked** (`P639`).

```
# run before any verification step; print the result, do not assume last pass's answer
curl -sS -o /dev/null -w '%{http_code}\n' https://raw.githubusercontent.com/<known-repo>/main/README.md   # expect 200
curl -sS -o /dev/null -w '%{http_code}\n' https://raw.githubusercontent.com/<owner>/<nonexistent>/main/README.md  # expect 404 -> it DISCRIMINATES
curl -sS -o /dev/null -w '%{http_code}\n' https://pypi.org/pypi/<known-package>/json                      # expect 200
curl -sSI -o /dev/null -w '%{http_code}\n' https://github.com/<known-repo>                                # 403 here
git ls-remote --exit-code -h https://github.com/<known-repo> HEAD >/dev/null 2>&1 && echo OK || echo FAIL  # FAIL here
```

🟢 **The second call is the one most often skipped and the only one that makes the first meaningful:**
an oracle that answers `200` for everything is not an existence oracle. 🔵 **`P641`'s refusals and
`P642`'s admission both depend on that `404`.**

🟢 **A licence is then read, never inferred — four filenames, both branches, then the README:**

```
for b in main master; do for f in LICENSE LICENSE.md LICENSE.txt COPYING; do
  curl -s -o lic -w "$b/$f %{http_code}\n" https://raw.githubusercontent.com/$SLUG/$b/$f ; done ; done
# all 404 across both branches?  then grep the README before concluding:
grep -inE 'licen[cs]e|MIT|Apache|BSD|GPL|copyright|all rights reserved' README.md
# still nothing -> ALL RIGHTS RESERVED.  That is a measured refusal, not "unknown licence".
```

🔵 **And a third, independent oracle when the project is packaged** — `pypi.org/pypi/<pkg>/json`
carries `license_expression` and the OSI classifier, which is how `P640` reached **four** agreeing
readings on `autorubric`. 🟢 **The `P637` lesson applies to oracles as much as to classifiers: run
them against each other on one real payload.**

## 🟢 Fifty-third pass, 2026-10-08 — one recipe (`P637` the **cross-instrument licence agreement check**) and a **correction** to every recipe that reads an LGPL component's licence as a family

### 🔴 The correction first, because it changes recipes already published here

🔴 **Any recipe in this file that recorded an LGPL component as `LGPL` was recording a family where
the delivery question needs a version.** 🟢 **Fixed at the source this pass** (`P634`):
`lib/license_family.sh` now emits `LGPL-2.1` or `LGPL-3.0` when the payload names a version, and
bare `LGPL` **only** when it genuinely does not.

🔵 **Concretely, for the one place it bites:** the side-car recipes that put an AI service beside
`openeducat/openeducat_erp` were correct in their conclusion (link a separate process, do not
modify the library) 🟢 **and are now correct for a checkable reason** — the component reads
**`LGPL-3.0`**, so the patent and anti-tivoisation clauses that distinguish it from `LGPL-2.1` are
known rather than assumed.
🔴 **`p411-cession-identity-gate` gained `LGPL-2.1` in `OSI_RECONOCIDAS`** (`P562`: the correction
travels to the consumer, or the gate rejects as unknown a string its own library produces — the
same move `P613` made for `GPL-UNVERSIONED`).

### 🟢 `P637` — the **cross-instrument agreement check**: run your own classifiers against each other on one real payload

🔵 **The problem this recipe solves is the one that cost this KB three passes.** `Gap 256` survived
because every instrument passed its **own** fixtures. 🔴 **Nothing compared the instruments to each
other**, and the disagreement was only visible on a real payload both of them could read.

**Wiring, with the specific files in this repository:**

| Step | Component | What it contributes |
|---|---|---|
| 1 | `lib/license_family.sh::osi_family_of` | the **shared** classifier the gates consume |
| 2 | `p419-copyleft-identity/identidad_copyleft.py::familia` | an **independent** header-window reader |
| 3 | `licence-grant-gate/grant_gate.py::family_of` | a **third**, deliberately coarse title map |
| 4 | the shelf row itself (`verticals/solutions.md`) | the human-read answer, which is the tie-breaker |
| 5 | `p411-cession-identity-gate` | the **consumer** whose allowlist must accept whatever 1 emits |

```
for payload in real LICENSE payloads this KB already recommends:
    a = osi_family_of(payload)          # shared
    b = identidad_copyleft.familia(payload)[0]
    c = grant_gate.family_of(payload)
    if a != b or a != c:
        report(payload, a, b, c)        # a disagreement is a finding, not a flake
        # then: which one does the SHELF say? that one is probably right.
```

🟢 **Run on `openeducat/openeducat_erp` this pass it returned `LGPL` / `LGPL-3.0` / `LGPL`** — and
the shelf said `LGPL-3.0`, so the **majority was wrong and the shelf was right.**
🔴 **A majority vote would have cemented the defect.** 🔵 **Hence step 4: the tie-breaker is the
first-hand read, never the count.**

🟡 **Step 3 legitimately disagrees and is NOT aligned** (🆕 **`Gap 259`**): `grant_gate.py`'s
contract is grant-versus-mention, where family granularity is not load-bearing. 🟢 **So the recipe
reports a *classified* disagreement, not a flat one** — a disagreement is either a defect or a
documented contract difference, and the recipe must name which.

**Cost and where it pays:** 🟢 **one sweep script, no new dependency, runs offline.** 🔵 **Pays on
any engagement where more than one tool answers the same compliance question** — which is the normal
condition in a client's estate, not a property of this KB.

### 🔵 Where this plugs into the delivery shape the live market block recommends

🟢 **The EMEA Annex III conformity sale (deadline **2027-12-02**) and the North American
policy-parameterised layer both require an auditable artefact per component.** 🔴 **A per-component
licence line that cannot distinguish `LGPL-2.1` from `LGPL-3.0` is not auditable.**
🟢 **`P637` is the cheapest way to show an auditor that the licence column was *derived twice
independently* and agreed** — and, when it did not, that the disagreement was adjudicated against
the payload and written down. 🔵 **Wire it beside `grant-mccurdy/instructional-ai-workflows`
(MIT), which supplies the human-review-at-every-stage shape the same regulations ask for.**

## 🟢 Fifty-second pass, 2026-10-08 — two recipes (`P632` the human-in-every-stage assessment pipeline; `P633` the grant-set gate) and a **correction** to every recipe that treated a repo's licence as a single value

⏱️ **Sixth pass of this date.** Both recipes name the exact repos, refs, payload filenames and byte
counts measured on 2026-10-08. **No star counts (`P479`).**

## 🔴 Correction — every recipe in this file read a repo's grant as a **value**, and a grant is a **set**

🔴 **No recipe here has ever asked whether a component ships more than one licence.** Each names a
component and a family — *"MIT"*, *"GPL-3.0"* — as though a repository had one. 🟢 **`P627` measured
a counter-example on a component this pass admits:**
[`grant-mccurdy/instructional-ai-workflows`](https://github.com/grant-mccurdy/instructional-ai-workflows)
ships **three** grants, and they govern different artefacts:

| Payload | Bytes | `sha256` | Family | Governs |
|---|---|---|---|---|
| `LICENSE` | **1,070** | `a8d6cd41…` | 🟢 **MIT** | the code |
| `LICENSE-CONTENT.md` | **662** | `c8b2ae96…` | 🟡 **CC BY 4.0** | documentation, diagrams, generated charts |
| `LICENSE-DATA.md` | **722** | `79fe1044…` | 🟡 **CC BY 4.0** | original **synthetic datasets** |

🔴 **Where this moves a deliverable:** a recipe that lifts this component's **code** is MIT-clean and
may ship closed. 🔴 **A recipe that lifts its rubric text or its synthetic student records into a
client deliverable incurs an attribution obligation that `LICENSE` does not mention.** 🟢 **For a
rubric component the content *is* the product**, so the obligation is the normal case, not the edge.

🟢 **The correction applied here, to every recipe in this file, as a rule rather than a re-edit:**
a component's licence line must state **which artefact class** the family covers, and a component
whose grant has not been enumerated (`P624` stage 1) carries the family **`GRANT-NOT-ENUMERATED`**
rather than a family guessed from `LICENSE`. 🔵 **No recipe below asserts a single family without
having enumerated.**

## 🟢 `P632` — the **human-in-every-stage assessment pipeline**, and the first recipe this KB can tie to a statute

🔵 **The problem.** Automated assessment is the one education AI use case that regulators in three
regions name explicitly — EU AI Act **Annex III** (access, assessment of learning outcomes,
educational path, exam monitoring; stand-alone high-risk, deferred to **2027-12-02**), **Vietnam**'s
AI law (effective **2026-03-01**, education among six high-risk sectors, *automated assessment and
behavioural monitoring* named), and **Oklahoma + Maryland**, which ban AI from making high-stakes
decisions about students. 🟢 **Vietnam's text is the useful one because it describes an
architecture**: a system is high-risk *only where its output is the sole basis for a decision without
meaningful human review*. 🔴 **So "human in the loop" is not a soft commitment here — it is the
property that changes the regulatory class.**

**The components, each with its grant enumerated this pass:**

| Stage | Component | Grant (enumerated, `P624` stage 1) | Why this one |
|---|---|---|---|
| 1. Rubric evidence | [`grant-mccurdy/instructional-ai-workflows`](https://github.com/grant-mccurdy/instructional-ai-workflows) `main` = `a4c5e832` | 🟢 **MIT** (code) + 🟡 **CC BY 4.0** (content, data) — **3 payloads, enumerated** | 🟢 **It is the only component this KB holds whose published shape already names human review at every stage.** Supplies the four-stage decomposition, not a runtime |
| 2. Feedback drafting | [`frappe/erpnext`](https://github.com/frappe/erpnext) Education module **or** Moodle | 🔴 **GPL-3.0** | 🟢 The domain model (students, enrolments, assessments) — 🔴 **side-car only, never linked** (`P631`) |
| 3. Reviewer packet | [`hcengineering/platform`](https://github.com/hcengineering/platform) (Huly) **or** [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework) | 🟢 **Apache-2.0** | 🟢 Permissive workflow/queue layer for the reviewer's inbox, so the **review step itself** is not inside a GPL boundary |
| 4. Remediation action | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) (7 heads) **or** [`MicroPyramid/opensource-startup-crm`](https://github.com/MicroPyramid/opensource-startup-crm) | 🟢 **MIT** (`LICENSE`, 1,068 B) | 🟢 Case/pipeline tracking for the intervention that follows a grade — two **independent** suppliers (`P564`) |

**The wiring, and the thing that makes each stage fail:**

1. **Stage 1 emits evidence, never a grade.** The model's output is a *rubric-criterion citation with
   a span*, written to an append-only store. 🔴 **If the pipeline can emit a grade at stage 1, stages
   2–4 are decoration and the system is high-risk under Vietnam's test.**
2. **Stage 3 is a blocking gate, not a notification.** The reviewer packet must be **acknowledged**
   before stage 4 can run. 🔴 **A packet that can be auto-approved on timeout re-creates the "sole
   basis" condition** — and that is the single most likely way this architecture quietly fails an
   audit.
3. **The audit trail is the deliverable.** Every stage writes who/what/when. 🟢 **This is also what
   Alabama's model procurement clause and North Carolina's DPI guidance ask a vendor to produce**, so
   one build serves the EU, Vietnamese and US-state asks.
4. **The GPL boundary is a process boundary.** Stages 2's domain data reaches the pipeline over HTTP
   from the GPL system; 🔴 **nothing in stages 1, 3 or 4 links GPL code**, which is what keeps the
   deliverable shippable to a client who cannot take copyleft.

🔵 **Cost, stated as a range because this KB has not built it:** 8–12 weeks for stages 1, 3 and 4
against an existing Moodle or ERPNext install; 🔴 **add the student/enrolment/assessment model itself
if the client refuses GPL** (`P631`'s empty cell), which is the larger number and must be quoted
separately.

🔴 **What this recipe does *not* have:** a graded corpus to evaluate stage 1 against. 🔵 **`Gap 237`
is still open** — no national Spanish essay exam, so no public rubric and no graded Spanish essay
corpus. 🟢 **The synthetic datasets in `LICENSE-DATA.md`'s scope are a scaffold, not an evaluation
set**, and the payload says so itself: *"provided for demonstration and evaluation and does not
represent real students."*

## 🟢 `P633` — the **grant-set gate**: refuse a component on what its payload says, not on whether a payload exists

🔵 **The problem, measured twice this pass.** Two components were offered and both had to be refused,
**for different reasons that a single `UNKNOWN` verdict would have merged:**

| Slug | Refs | What the probe found | 🔴 Verdict | Next action |
|---|---|---|---|---|
| [`michael-borck/assessment-rubrics-for-ai`](https://github.com/michael-borck/assessment-rubrics-for-ai) | 1 head, `00294979` | `LICENSE.md` **200**, 2,859 B, header `# License & Usage Terms` | 🔴 **PROPRIETARY** — Curtin-internal; `✗ Commercial use` | 🔴 **stop** |
| [`GradeAI/gradeai`](https://github.com/GradeAI/gradeai) | 1 head, `4de8e861` | 🔴 tree enumeration empty **and** six probes **404 ×6** | 🔴 **UNLICENSED** | 🔴 **stop** |

**The gate, four stages, each with the thing that makes it fail:**

1. **Exist first (`P510`).** `git ls-remote --heads`, **with a negative control in the same run**.
   🟢 This pass: `gmilano/education-kb-NEGATIVE-CONTROL-no-existe-52` → **0 refs** while
   `Dolibarr/dolibarr` → **64**, `idempiere/idempiere` → 27, `krayin/laravel-crm` → 7. 🔴 **Without
   the control, a proxy failure and a dead slug are the same observation** — and this pass proved the
   point the other way round: `pawtograder/pawtograder` → 0 refs, while the project is real and this
   KB already held the correct slug, [`pawtograder/platform`](https://github.com/pawtograder/platform).
2. **Enumerate, don't guess (`P624`).**
   `git clone --filter=blob:none --no-checkout --depth 1`, then
   `git ls-tree -r --name-only HEAD | grep -iE '(^|/)(licen[cs]e|copying|notice)'`. 🔴 **Six-filename
   probing filed `idempiere` as `UNKNOWN` (pass 51) on a project that ships its grant twice.**
3. **Read **every** path the enumeration returned (`P627`).** Expect a **set**. 🔴 **Reading only
   `LICENSE` returns a value that is true of the code and false of the deliverable.**
4. **Classify into three refusals, not one (`P628`, `P629`).** `UNKNOWN` = *not read* → probe again.
   `PROPRIETARY` = *read, and it refuses*. `UNLICENSED` = *whole tree read, no grant; default is all
   rights reserved*. 🔴 **Only the first justifies another probe; filing the other two as `UNKNOWN`
   spends probes that cannot change the answer and prints "licence not determined" where the answer
   is "determined, and it says no".**

🟢 **Suite: `compose/code/p627-multi-grant-repo/` — 🟢 31/31 green, offline.** It retains both
defective instruments as **controls**: `single_license_sweep()` still answers `MIT` for the
three-grant repo *and* still misses the CC BY obligation; `filename_keyed_classifier()` still calls
the Curtin `LICENSE.md` open. 🔵 **A fix that deletes the defect also deletes the detector**
(`P237`), so neither is removed.

🔴 **One defect the suite found in itself, kept because it is the transferable part:** the `P479`
no-star-counts check was first written `"star" not in blob.lower()` and went **red on clean data** —
`MicroPyramid/opensource-startup-crm` contains the substring `star`. 🟢 **A substring is not a
token.** The check now tokenises, and the substring form is retained as a control asserting it is
still the wrong instrument. 🔵 **Same class as `P409`**, whose case-sensitive regex passed by accident
for ~11 passes.

## 🟢 Fifty-first pass, 2026-10-08 — two recipes (`P624` the format-aware grant read; `P625` the two-supplier admissions layer) and a **correction** to every recipe that priced a GPL component without its version

⏱️ **Fifth pass of this date.** Both recipes name the exact repos, refs, payload filenames and byte
counts measured on 2026-10-08. **No star counts (`P479`).**

## 🔴 Correction — every recipe that named a Moodle AI plugin was pricing a **GPL of unknown version**

🔴 **Four components several recipes in this file reach for carried the family `GPL` and no
version**: [`caiocarvalhofre/moodle-mod_maici`](https://github.com/caiocarvalhofre/moodle-mod_maici),
[`cgrevisse/moodle-qbank_genai`](https://github.com/cgrevisse/moodle-qbank_genai),
[`yedidiaklein/moodle-local_aiquestions`](https://github.com/yedidiaklein/moodle-local_aiquestions),
[`michael-milette/moodle-local_aiid`](https://github.com/michael-milette/moodle-local_aiid).
🟢 **All four read GPL-3.0 under `P620`.** 🔵 **The correction does not move a deliverable here** —
GPL-3.0 was the working assumption, Moodle's own licence, and the side-car shape every recipe already
imposed. 🟢 **But it was an assumption, and now it is a reading.**

🔴 **Where the same defect *does* move a deliverable:**
[`idempiere/idempiere`](https://github.com/idempiere/idempiere) reads **GPL-2.0**, not GPL-3.0.
🔴 **GPL-2.0 carries no patent grant and is incompatible with Apache-2.0**, so any recipe that would
have combined it with an Apache-2.0 component on the assumption "GPL means GPL-3.0" was wrong about
the one thing that decides whether the combination may ship. 🟢 **No recipe in this file named it
before this pass; it is recorded so none does so unversioned.**

## 🟢 `P624` — the **format-aware grant read**: six filenames is not a probe, it is a guess

🔵 **The problem, measured.** A licence sweep that probes `LICENSE`, `LICENSE.txt`, `COPYING`,
`COPYING.txt`, `LICENSE.html`, `legal/LICENSE` — the shape most sweeps in this corpus use — returns
**404 six times** on `idempiere/idempiere`, a project that ships its grant **twice**. 🔴 **It would be
filed `UNKNOWN` ("grant not found") and dropped from a shortlist.** And where a probe *does* hit a
`.md` payload, the version is lost to the wrapper.

**The recipe, four stages, each with the thing that makes it fail:**

1. **Enumerate, do not guess.** `git clone --filter=blob:none --no-checkout --depth 1` then
   `git ls-tree -r --name-only HEAD` — `p441`'s `tree_paths`. 🔴 **Not a filename list:** that is the
   stage `idempiere` defeats. Add `.md` / `.html` / `.rst` to the grant-path pattern.
2. **Confirm existence separately.** `git ls-remote --heads` with a **negative control in the same
   run** (`P510`). 🔴 **Without it a 0-ref answer and a dead channel are indistinguishable** — which
   is exactly how `bottlecrm/bottlecrm` would have been read as "project does not exist" when the
   project is real and the *slug* is not (`P622`).
3. **Unwrap, then read the header.** `p620`'s pre-stage (drop markup-only lines, strip inline tags
   and Markdown lead markers) then `p419`'s **unmodified** `familia()`. 🔴 **Do not widen the header
   window to compensate** — at `n=3`+ body text re-enters it and GPL-3.0 §13 makes the payload read
   `AGPL`, which `p419`'s suite already refuted.
4. **Record format beside size.** 🟢 **`format` is the column that explains the size outliers**
   (35,178 ×3 and 32,477 against a modal 35,149 are Markdown wrappers, not anomalies).
   🔴 **Never use byte count as licence identity at any tolerance:** five GPL-3.0 payloads measured
   today span **34,674 → 35,151 B**, and two *different* payloads sit at exactly 35,148 B.

**Wire-up:** `compose/code/p620-licence-header-window/probe_window.py` over the output of
`p441-tree-licence-enumeration`, verdicts fed to `licence-grant-gate`. Suite 🟢 **30/30**, offline.
🔴 **Declared blind spot to carry into the client report, not to hide:** a payload that **names a
second licence above its own title** (`idempiere`'s `license.html` opens
`Compiere Public License`) still answers `GPL-?` and is classed `WINDOW-STILL-SHORT`. 🟢 **Route
those to a human read; there is one in 412 rows, so the queue is affordable.**

## 🟢 `P625` — the admissions/CRM layer with **two real suppliers**, which is what makes `P568` sellable

🔵 **`P568` (pass 46) built a permissive admissions/CRM layer over a copyleft academic core and its
"swap the CRM" clause was nominal**, because `P564` had just proved the shelf's two "independent MIT
options" shipped **byte-identical `LICENSE` payloads under one holder**, `Webkul Software`.
🟢 **This pass supplies the second supplier.**

| Layer | Component | Ref / payload | Licence |
|---|---|---|---|
| Academic core | `moodle/moodle` or ERPNext school module | — | 🔴 GPL-3.0 — **stays a separate process** |
| 🟢 **Admissions/CRM, supplier A** 🆕 | [`MicroPyramid/opensource-startup-crm`](https://github.com/MicroPyramid/opensource-startup-crm) | `main` = `master` = `b51c85d` (**one ref, two names** — `P511`); `LICENSE` **1,068 B** | 🟢 **MIT** — holder `MicroPyramid`, Django + DRF + SvelteKit |
| 🟢 **Admissions/CRM, supplier B** | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | `2.2` (🔴 **not `main`** — `P565`); `LICENSE` **1,077 B** | 🟢 MIT — holder `Webkul Software`, Laravel/PHP |
| Boundary | HTTP/REST between CRM and academic core | — | 🟢 **Keeps the copyleft core out of the deliverable's linkage** |

🟢 **Why two suppliers is the point and not a nicety:** EU public procurement asks for vendor
independence far more often than architecture does, so the second source is **commercially**
load-bearing (see `intel/market.md`, EMEA, this pass). 🔴 **Different holders also mean different
stacks** — Python/Django against PHP/Laravel — so "swap" is a port, not a drop-in; price it as a
port.

🔴 **Two things to put in the proposal, not bury.** (1) **Neither has an education domain model** —
no admissions funnel, cohort, programme or enrolment entity. Both are generic CRMs, filed exactly as
the archive filed Huly and Apache OFBiz: **a layer to be modelled**, and the modelling is the
engagement. (2) 🔴 **Supplier A's MIT grant is single-channel** — read from payload, with **no
manifest licence field anywhere in the tree** (`package.json`, `pyproject.toml`, `setup.py` all
404), and a 2026 third-party roundup claims GPL-3.0. 🟢 **The payload refutes the roundup; pin the
ref in the contract so the reading is reproducible.**

## 🟢 Fiftieth pass, 2026-10-08 — `P619`: the **two-ref licence read**, and the recipe that unpins a Spanish assessment build from GPL-3.0

⏱️ **Fourth pass of this date.** 🔵 **All licences read first-hand on 2026-10-08** from payload or model
metadata, **per git ref**, HTTP status recorded per filename.

### 🟢 `P619` — Recipe: the two-ref licence read (this **replaces** `P604` step 3)

🔴 **Why `P604` step 3 is being rewritten one pass after it was published.** It said *"each corpus's own
`LICENSE`"* and did not say **at which ref**. Pass 49 ran it against the default branch, got an answer
that agreed with the artefact's metadata, and retired the question. 🔴 **Both legs were wrong and they
agreed** (`P612`): the metadata was right about a **2021 tag**, and the default-branch read matched a
**vestigial prose sentence** that the relicensing left behind.

🔵 **The defect is not a missing probe. It is a missing *comparison*.**

**The pre-flight, four probes, minutes of work:**

| # | Probe | Command shape | What it answers |
|---|---|---|---|
| 1 | the artefact's own metadata | `curl …/meta/<model>-<ver>.json` → `.license` | the licence of the thing you actually ship |
| 2 | the artefact's **`sources[]`**, including **the version string in the name** | same payload → `.sources[].name`, `.sources[].license` | *which ref* the verdict was derived from |
| 3 | the upstream's `LICENSE*` **at that pinned ref** | `curl …/<upstream>/<PINNED-TAG>/LICENSE.txt` | 🟢 whether the artefact's claim is faithful |
| 4 | 🆕 the upstream's `LICENSE*` **at the default branch** | `curl …/<upstream>/master/LICENSE.txt` | 🟢 whether the restriction **still exists upstream** |

🟢 **Probe 2 is the one that was being skipped, and it is free** — the pinned version is already sitting
in the `sources[].name` string (`"UD Spanish AnCora v2.8"`). 🔴 **Probes 3 and 4 are worthless
individually and decisive together.**

**The verdict table — and the four cases are genuinely different engagements:**

| Probe 3 (pinned) | Probe 4 (live) | Verdict | What to do |
|---|---|---|---|
| permissive | permissive | 🟢 **CLEAN** | ship |
| restrictive | restrictive | 🔴 **STRUCTURAL** | re-architect or accept the copyleft |
| 🟡 **restrictive** | 🟢 **permissive** | 🟡 **STALE PIN** | 🟢 **retrain / rebuild at the newer ref — the cheapest fix in this table** |
| 🟢 permissive | 🔴 restrictive | 🔴 **UPSTREAM TIGHTENED** | 🔴 pin hard, vendor the artefact, and never bump blindly |

🔴 **Pass 49 placed Spanish in row 2 (STRUCTURAL) and priced three expensive routes against it.**
🟢 **Measured this pass, it is row 3 (STALE PIN).**

**Worked example, every value measured on 2026-10-08:**

```
# probe 1 + 2
curl -s raw.githubusercontent.com/explosion/spacy-models/master/meta/es_core_news_sm-3.8.0.json
  .license                -> "GNU GPL 3.0"
  .sources[0].name        -> "UD Spanish AnCora v2.8"      <-- THE PIN
  .sources[0].license     -> "GNU GPL 3.0"

# probe 3 -- at the pinned ref
curl -s .../UniversalDependencies/UD_Spanish-AnCora/r2.8/LICENSE.txt     # 200, 68 B
  -> "GNU GENERAL PUBLIC LICENSE 3.0"                        [faithful]

# probe 4 -- at the default branch
curl -s .../UniversalDependencies/UD_Spanish-AnCora/r2.18/LICENSE.txt    # 200, 189 B
  -> "...Creative Commons License Attribution 4.0 International"   [RELICENSED]
```

🟢 **Verdict: STALE PIN.** 🔵 **The changelog names the moment** (`r2.9`, 2021-11-15) and the
`README.md` **still carries the old GNU sentence in its Introduction**, which is why a prose read
reproduces the dead answer.

🔴 **Do not read prose for a licence verdict.** `LICENSE*` payload and the machine-readable
`License:` field were both correct at every ref; **only the narrative paragraph was stale.**

### 🟢 `P620` — Recipe: a permissive Spanish assessment feature layer, with the route `Gap 254` said did not exist

🔵 **`Gap 254` priced three routes and called C unavailable.** 🟢 **Route C is available and is now the
default recommendation.**

| Route | What it costs | Verdict after `P609`–`P611` |
|---|---|---|
| **A** — ship `es_core_news_sm` as GPL-3.0 | zero engineering | 🟢 **still right for most public-sector work.** 🔵 GPL-3.0 is OSI and permits commercial use; the obligation is reciprocity on derivatives, not a ban |
| **B** — `xx_ent_wiki_sm` (**MIT**) + reimplemented indices | 🔴 an **agreement study**, not an extractor | 🔴 **no longer the permissive route of choice** — it was only preferred because C looked closed |
| 🟢 **C** — **retrain on `UD_Spanish-AnCora` `r2.9`+ (CC BY 4.0)** | one training run on a **CC BY 4.0** corpus | 🟢 **AVAILABLE.** The corpus is the *same* one the shipped model already uses, five tags later |

**The wiring, concretely:**

1. 🟢 **Corpus** — `UD_Spanish-AnCora` at `r2.18` (or any ref `≥ r2.9`): **CC BY 4.0**, 189-byte
   `LICENSE.txt`, attribution only, **no ShareAlike**. 🔵 Cite Taulé, Martí & Recasens (2008) — the
   README makes that citation a condition, and CC BY makes attribution the whole obligation.
2. 🟢 **Trainer** — `spaCy` itself is 🟢 **MIT** (`master/LICENSE`, 1 128 B, © ExplosionAI GmbH /
   spaCy GmbH / Matthew Honnibal). 🟢 **The code was never the problem.**
3. 🟡 **NER, if you need it** — `es_core_news_sm` also sources **WikiNER** (🟢 CC BY 4.0). 🟢 Both
   non-code inputs for a retrained Spanish pipeline are therefore **CC BY 4.0**: attribution-only,
   permissive, shippable.
4. 🟢 **Verify the output artefact, not the plan** — emit your own `meta.json` with
   `license: "CC BY 4.0"` and `sources[].name: "UD Spanish AnCora r2.18"`. 🔴 **Name the ref, not the
   project**, or you have rebuilt the defect `P610` found.
5. 🟢 **Gate it** — `lib/license_family.sh::family_of` now answers `CC-BY-4.0` for that payload and
   `GPL-3.0` for the `r2.8` one (`P613`), so the two are **distinguishable by the shared control**
   rather than by a reader's eye.

🔴 **Scope stated honestly.** This recipe makes the **pipeline artefact** permissive. 🔴 **It does not
touch `Gap 237`**, which is the tier underneath: there is still **no national Spanish essay exam, so
no public rubric and no graded Spanish essay corpus.** 🟢 **Routes A and C differ in licence, not in
capability**, and neither produces a scorer without the data `Gap 237` says is missing.

### 🟢 `P621` — Recipe: a pre-commit gate run, which is `Gap 255`'s remedy done rather than described

🔵 **`Gap 255` asked for *"one invocation list — the gates every pass runs before committing, with
expected exit codes."*** 🟢 **Run this pass over all 110 suites, and the run is what found `P614`.**

```sh
# from compose/code/ -- every suite, from its own directory, exit code recorded
for t in $(find . -name 'test_*.sh' -o -name 'test_*.py' | sort); do
  d=$(dirname "$t"); b=$(basename "$t")
  case "$b" in
    *.sh) (cd "$d" && timeout 180 bash    "$b" >/dev/null 2>&1) ;;
    *)    (cd "$d" && timeout 180 python3 "$b" >/dev/null 2>&1) ;;
  esac
  echo "$t $?"
done
```

🔴 **Two things about this are not optional, and both were learned by getting them wrong in this run:**

| Rule | Why |
|---|---|
| 🔴 **run each suite from its OWN directory** | they resolve fixtures relatively (`p355`'s whole subject) |
| 🔴 **do NOT use `python3 -I`** | isolated mode drops the script's directory from `sys.path`, so **28 suites** reported `ModuleNotFoundError` against their own module. 🔴 **A harness defect that looks exactly like 28 broken instruments** |

🟢 **And the result is only interpretable against a baseline.** This pass ran the same sweep on a
**pristine clone of `HEAD`** and diffed:

| | Pristine `HEAD` | This pass |
|---|---|---|
| suites passing | **107 / 110** | 🟢 **108 / 110** |
| diff | — | 🟢 **one line: `p550` red → green** |

🟢 **That diff is the acceptance test for `P613`** — a change to the file 46 instruments source, with
**zero** regressions and zero accidental passes. 🔴 **Without the baseline, "107 passing" would have
been read as this pass breaking three suites.**

🔴 **`Gap 255` stays open and its scope is narrowed, not claimed closed.** The list exists and was run;
🔴 **nothing yet *obliges* a pass to run it**, and a convention a pass has to remember is not a control
(`P237`). 🟢 **What this pass can claim: the first full invocation found one red gate that had been
accusing the shared control, and two that are red for reasons now named** (`Gap 257`, `Gap 258`).

## 🟢 Forty-ninth pass, 2026-10-08 — `P604`: the **licence-by-language pre-flight**, and the recipe that routes a non-English assessment build around a GPL pipeline

⏱️ **Third pass of this date.** 🔵 **All licences read first-hand on 2026-10-08** from payload or from
model metadata (`explosion/spacy-models`, `meta/<model>-<version>.json`, HTTP 200).

### 🟢 `P604` — Recipe: licence-by-language pre-flight (run this before the architecture, not after)

🔴 **Why this is a recipe and not a checklist item.** `P596` measured that spaCy's **code** is MIT
while its **artefacts** are licensed per-language — MIT for English, CC BY-SA 4.0 for Portuguese,
**GPL-3.0 for Spanish** — and that the restriction gets *tighter* one tier down. 🔴 **A team that
reads "spaCy is MIT" and starts building a Spanish product has already made the wrong decision**, and
will discover it at delivery.

**The pre-flight, three probes, minutes of work:**

| # | Probe | Command shape | What it answers |
|---|---|---|---|
| 1 | the **artefact's own** metadata | `curl raw.githubusercontent.com/explosion/spacy-models/master/meta/<model>-<ver>.json` → `.license` | the licence of the thing you actually ship |
| 2 | the artefact's **`sources[]`** | same payload → `.sources[].license` | *why* it carries that licence, and whether it can change |
| 3 | each corpus's **own** `LICENSE` | `curl .../UniversalDependencies/<treebank>/master/LICENSE.txt` | corroboration one tier deeper (`P510` shape) |

🔴 **Probe 1 alone is not enough** — it tells you the verdict without the mechanism, so you cannot
tell a licence that *could* be renegotiated from one that is structural. 🟢 **Probe 2 is what told
this pass that English is permissive because Explosion bought OntoNotes**, which is the fact that
makes the whole table predictable instead of arbitrary.

**Verdict table, measured:**

| Language | Artefact | Licence | Ship permissively? | Route if not |
|---|---|---|---|---|
| English | `en_core_web_sm/lg` | 🟢 **MIT** | 🟢 yes | — |
| Portuguese | `pt_core_news_sm/md/lg` | 🟡 **CC BY-SA 4.0** | 🟡 publishable, ShareAlike travels to derivatives | accept SA, or retrain on a licensed corpus |
| Spanish | `es_core_news_sm` | 🔴 **GPL-3.0** | 🔴 **no** | see the three routes below |
| language-agnostic NER | `xx_ent_wiki_sm` | 🟢 **MIT** | 🟢 yes | 🔵 **the permissive escape hatch, with reduced capability** |

### 🟢 `P605` — the three routes for a **Spanish** assessment product, priced

🔴 **`Gap 237` framed Spanish as a *data* problem** — no national essay exam, so no rubric and no
graded corpus. 🟢 **True, and one tier too high.** `P595` adds that the **pipeline artefact** is
GPL-3.0, so the feature layer is blocked *before* the corpus question is reached.

| Route | What it is | Cost | When to choose it |
|---|---|---|---|
| **A · Copyleft delivery** | ship the product under GPL-3.0 | 🟢 **zero engineering** | 🔵 internal tooling, public-sector work where source delivery is already required — **the cheapest honest answer, and usually the right one** |
| **B · Permissive escape hatch** | `xx_ent_wiki_sm` (**MIT**) + reimplemented lexical indices from published definitions | 🟡 days, plus 🔴 **an agreement study** — accuracy is lower and must be measured, not assumed | a product that must ship permissively and can accept weaker features |
| **C · Retrain** | train a pipeline on a permissively-licensed Spanish corpus | 🔴 **expensive; and this KB has not found such a corpus** | only with corpus budget already approved |

🔴 **Route B's trap, stated so nobody walks into it:** the **index definitions** (TTR, MTLD, MATTR,
HD-D, syntactic-complexity indices) are published statistics and free to reimplement — 🟢 that part
is settled (`Gap 246`). 🔴 **What is not free is the validation**: the published tools carry years of
it and a reimplementation inherits none (`P504` shape). 🟢 **So Route B's real deliverable is an
agreement study, not an extractor.**

🔵 **Portuguese is the better LATAM first engagement, and now for a measured reason rather than
momentum:** its artefact is **ShareAlike, not GPL**, and `lplnufpi/essay-br` (**MIT**, human-graded
on ENEM C1–C5, peer-reviewed) gives it a corpus Spanish does not have. 🔴 **Do not quote a Spanish
timeline derived from a Portuguese one.**

### 🟢 `P606` — the assessment chain, with this pass's constraint folded in

🔵 **Unchanged and still permissive end to end for the *parametric* chain** (`P594`, pass 48):
`qti3` **MIT** authoring via this KB's emitter → `qti3` `core`/`player` **MIT** delivery →
`EqUMP` 0.3.6 **MIT** IRT linking → `grading-draft-gate` human decision point. 🔴 **Limit that
travels with it:** `EqUMP` closes **IRT linking only** — not observed-score or kernel equating
(`P500`, `Gap 234`).

🔴 **What this pass adds is the branch point.** The parametric chain is **language-neutral** (it
scores *items*, not *prose*); the essay chain is **language-bound** and inherits the table above.

| If the engagement needs… | Chain | Licence posture |
|---|---|---|
| parametric high-stakes items, any language | `qti3` + `EqUMP` + `grading-draft-gate` | 🟢 **permissive end to end** |
| English essay scoring | `wwrwbs/AI_AWE` (Apache-2.0) + `en_core_web_*` (MIT) | 🟢 **permissive end to end** |
| Portuguese essay scoring | `essay-br` (MIT) + `pt_core_news_*` (CC BY-SA 4.0) | 🟡 **ShareAlike travels** |
| Spanish essay scoring | 🔴 **no permissive chain exists** | 🔴 Route A / B / C above |

🟢 **Sell the parametric chain into a Spanish-language engagement first.** 🔵 It is the one assessment
capability this KB can deliver permissively in **any** language, and it sidesteps `Gap 237`,
`Gap 254` and the whole feature-layer question — 🔴 **which is a scoping decision, not a workaround,
and it should be made before the proposal rather than after the licence review.**

### 🟢 `P607` — governance recipe: the supersession marker, now with a control behind it

🔵 **Named in `P582`/`Gap 252`, mechanised this pass.** The artefact is
`compose/code/p598-register-freshness-gate/` — 58 assertions, 7/7 mutants, refuses empty input.

| Step | Component | Why |
|---|---|---|
| 1 | classify each register row's claim: **MEDICION** or **PRIORIDAD** | the two go stale for different reasons and need different evidence |
| 2 | 🔴 **exempt rows that carry their own correction** (`CITA`) | without this the tool flags *the act of correcting*, and gets switched off (`P598` v1: 3 of 4 false positives) |
| 3 | refute **MEDICION** with a measurement of its subject elsewhere in the tree | a status claim is falsified by a reading |
| 4 | refute **PRIORIDAD** with a later **closure** of that gap | 🔴 a licence measurement cannot tell you whether a gap is still open (`P598` v1's fourth error) |
| 5 | forward-point every flagged row; never rewrite history | 🟢 the cheap fix, per `Gap 252` |

🔵 **Client-facing form:** this is the audit any team with an ADR log, a risk register or a
compliance tracker needs **before** anyone trusts the document top-down. 🟢 **It is days of work, it
is demonstrable on their own repository on day one, and `P597` is the case study** — a register that
was being maintained correctly and still charged a reader for settled work.

## 🟢 Forty-eighth pass, 2026-10-08 — `P594`: the **parametric high-stakes assessment chain** is complete end to end on permissive components for the first time, and this pass is the one that can say so

⏱️ **Second pass of this date.** 🔵 **Licences read first-hand on 2026-10-08 from payload.** Upstream
`qti3` re-measured from a fresh clone at `main` = `0ca7d6fc` (`P584`, `repos/foundations.md`).

🔵 **Why this recipe only becomes writable now.** `P49` named this chain at pass 25 and `Gap 39`
named its two unmeasured links. The register still calls the first link *"the cheapest remaining
win"* (`P582`) — but passes 40, 42 and 43 closed **both** links, 18 passes apart and under three
different numbers. 🟢 **Nothing was missing except a pass that read all three results together.**

### 🟢 `P594` — the chain, link by link, with what closed it

| # | Link | Component | Licence (payload) | Status |
|---|---|---|---|---|
| 1 | **Author** N parametric variants of one item | 🟢 `compose/code/p533-qti3-template-emitter/` (this KB) | 🟢 **MIT** base (`qti3` `main/LICENSE.md`, 1,072 B) | 🟢 **`Gap 238` closed at pass 43.** 43 assertions, 19 negative controls |
| 2 | Write them as a **QTI 3 item-bank package** | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) `packages/writer` | 🟢 **MIT** · © 2026 Longsight, Inc. | 🟢 33 exports, bank writer verified first-hand |
| 3 | **Deliver** the variants, drawing per learner | same repo, `packages/core` + `packages/player` | 🟢 **MIT** | 🟢 **Verified this pass from a fresh clone:** `randomInteger` ×24, `qti-template-constraint` parsed (`parser-processing.ts:109`), enforced (`session.ts:464`), validated (`validation-processing.ts:181`) |
| 4 | **Equate** the variants so scores are comparable | `EqUMP` 0.3.6 | 🟢 **MIT** | 🟡 **`Gap 39` second half closed *for IRT linking*** — Mean-Mean, Mean-Sigma, Haebara, Stocking-Lord + true-score equating (`P499`). 🔴 **NOT closed for observed-score or kernel equating** — those dirs are 0-byte stubs (`P500`); only GPL implementations exist |
| 5 | Human decision point before any consequence lands | `compose/code/grading-draft-gate/` | 🟢 this KB | 🟢 required by NYC's red tier and by OK/MD human-oversight rules |

🟢 **Links 1–4 are permissive end to end.** 🔴 **Link 4 carries a method qualifier that must travel
with it** — see the caveat below, which is the one thing that can make this recipe wrong in front of
a psychometrician.

### 🟢 How to wire it

🔴 **Read this first: `emit_template.py` is a *library*, not a CLI.** It declares no `argparse` and no
`__main__`, so there is no `--spec` flag to pass — checked in the payload this pass, because quoting
an invented command line is how a recipe stops being reproducible. The entry point is
`build_parametric_item(**kwargs)`.

```python
# 1. AUTHOR — one item spec -> a parametric qti-assessment-item (this KB's emitter, stdlib only)
from emit_template import (
    build_parametric_item, RandomInteger, TemplateDeclaration,
    TemplateProcessing, SetTemplateValue, SetCorrectResponse, TemplateConstraint,
    qti_sum, qti_product, qti_gte,
)

a = TemplateDeclaration(identifier="A", base_type="integer")   # the drawn parameter
xml = build_parametric_item(
    identifier="add-two-ints", title="Add two integers",
    template_declarations=[a, ...],
    template_processing=TemplateProcessing(rules=[
        SetTemplateValue("A", RandomInteger(minimum=2, maximum=20, step=2)),
        TemplateConstraint(qti_gte(...)),      # reject degenerate draws; core retries
        SetCorrectResponse("RESPONSE", qti_sum(...)),   # the key follows the draw
    ]),
    response_declaration=..., outcome_declaration=...,
    item_body=..., response_processing=...,
)
# Child order is the XSD's required sequence, not core's parser order --
# core is order-insensitive, the schema is not. The emitter handles this.
```

```
# 2. BANK — package the family with the MIT writer (packages/writer)
#    buildQti3ChoiceItem / validateQti3ChoiceItem (+31 more, indexed BY INTERACTION TYPE)
#    NOTE (P585): the writer has no template axis of its own -- step 1 supplies it

# 3. DELIVER — packages/core draws per learner and enforces the constraints
#    randomInteger over min/max/step; templateConstraint retried until satisfied
#    (estimate_constraint_restarts() in step 1 prices that retry before you ship)

# 4. EQUATE — calibrate delivered responses, then link the variant forms
#    EqUMP 0.3.6 (MIT): Mean-Mean | Mean-Sigma | Haebara | Stocking-Lord | true-score

# 5. GATE — no score becomes a consequence without a human decision
python3 -I compose/code/grading-draft-gate/gate.py   # see that dir's README for arguments
```

🟢 **`estimate_constraint_restarts()` is the part a studio will actually thank the emitter for**: a
`TemplateConstraint` that rejects too many draws makes delivery stall, and this prices the restart
rate **before** the item reaches a learner.

### 🔴 `P595` — the delivery engine **silently delivers a constraint-violating item** on the 101st retry, confirmed in upstream source

🔵 **`P533`'s module docstring asserts this; this pass confirmed it in upstream's own source** at
HEAD `0ca7d6fc`, `packages/core/src/session.ts:464-477`:

```js
restarts += 1;
if (restarts <= 100) index = -1;   // restart the rule list
// ...and on the 101st failure: no reset, no throw, no log.
// The loop advances past the constraint and finishes with the VIOLATING draw.
```

🔴 **There is no error path.** A `qti-template-constraint` whose acceptance probability is too low
does not fail loudly — it **delivers a degenerate item to a learner as though it were valid**. At an
acceptance probability of `0.001`, `(1 - p)**101` ≈ **90%**: nine items in ten are wrong, and nothing
in the stack says so.

🟢 **The mitigation is already built and is the reason to use this emitter rather than hand-written
XML.** `estimate_constraint_restarts(draws, predicate)` returns the satisfying fraction of the
cartesian product of the declared grids, so the author prices the restart rate **before** an item
ships. 🔴 **Make it a gate in the build, not an optional check** — this is the single highest-value
line in the whole chain for a high-stakes deployment.

🔵 **Why it belongs in this file and not only in the emitter's README:** it is a property of
**upstream delivery**, so it applies to *every* parametric item delivered on this stack, including
items this KB's emitter did not author.

### 🔴 The caveats that must travel with this recipe

1. 🔴 **Step 4 is closed for *IRT linking* only.** If the client's psychometrics require
   **observed-score** or **kernel** equating, the permissive chain **breaks at link 4** and the only
   implementations are **GPL** (`P500`). 🔵 **Ask which method their standards body mandates before
   quoting this recipe as permissive end to end.**
2. 🔴 **Step 1 is this KB's code, not upstream's.** `P585` explains why that is unlikely to change
   cheaply: the writer's API is indexed by **interaction type** and parametrisation is **orthogonal**
   to it, so threading it through all 33 builders is a maintainer's design decision, not a patch.
   🟢 **Say "we wrote the emitter", never "the writer supports it".**
3. 🔴 **The whole chain is high-risk under the EU AI Act and under Vietnam's Law on AI** — both name
   automated assessment explicitly. 🟢 **Step 5 is not optional polish; it is the control that makes
   the rest deployable**, and the same control satisfies NYC's red tier.

### 🟢 Why this is the pass's most sellable output

🔵 **The thesis every trends source in this channel converged on** — OECD 2026's *purpose-built
educational AI with durable learning gains*, 1EdTech's *experimentation → governance* — describes
this chain. 🟢 **It replaces proctoring with equivalent-variant delivery**, which is the original
`Gap 39` motivation (*"que es lo que vuelve innecesario el proctoring"*), it is permissive at every
link that matters, and 🟢 **its weakest link is now named with its method qualifier rather than
hidden behind "IRT, closed"**.

## 🟢 Forty-seventh pass, 2026-10-08 — two recipes (`P576` the permissive-LMS AI overlay that can ship closed; `P578` the licence-regime intake gate) and a **correction** to every recipe that priced Sakai out or priced Moodle too dear

⏱️ **First pass of this date.** 🔵 **Licences read first-hand on 2026-10-08 from payload in the
repository, channel named per row (`P237`, `P250`, `P510`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed before allocation**: the occupied set was read from the
live tree **and** `archive/` at pristine `HEAD` (`bbf3f55`); this pass allocates **`P571`–`P581`**.
🔴 **The first attempt, `P567`–`P575`, COLLIDED with pass 46's own `P567`–`P570` in this very file** —
caught before the write and re-allocated.

## 🔴 Correction — every recipe that chose an LMS was choosing against two wrong licence labels

🔵 **Not a correction to a step, but to the constraint the steps were optimised under.** Until this
pass the cession gate reported **Sakai as `NO-OSI`** (`P576`) and **Moodle as `AGPL-3.0`** (`P571`).
Both are wrong, and they are wrong in the same direction: **toward telling a client it has less
freedom than it does.**

| | Before this pass | 🟢 After (payload read 2026-10-08) |
|---|---|---|
| `sakaiproject/sakai` | 🔴 `NO-OSI` — **not eligible for any recipe** | 🟢 **`ECL-2.0`**, permissive, **no reciprocity** |
| `moodle/moodle` | 🔴 `AGPL-3.0` — *"source must be offered to network users"* | 🟡 **`GPL-3.0`** — reciprocity on **distribution**, not on network use |
| `hcengineering/platform` (Huly) | 🔴 `GPL` | 🟡 **`EPL-2.0`** — file-level, weak |
| `FWU-DE/mem-mcp` | 🔴 `usable=NO` | 🟢 **`Unlicense`**, usable |

🔴 **The consequence is concrete: every recipe that needed a closed deliverable had to route around
the LMS layer entirely, because the one permissive LMS on the shelf was marked ineligible.** 🟢 **That
routing is no longer necessary**, and the recipe below is the one that was not previously
expressible.

## 🟢 `P576` — AI tutor/feedback overlay on a **permissive** LMS, deliverable closed

🔵 **The gap this sells into is measured, not inferred:** **19% of faculty use AI for assignment
feedback while 50% of students support it** (Digital Education Council, 30 000+ responses, 29
institutions) — and **institutions run AI at 87% while only 26% have a governance framework**
(UNESCO IESALC, 200 institutions / 19 countries).

**Wiring, every component licence-read from payload this pass or a prior pass:**

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| LMS core | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) — **34 refs** | 🟢 **ECL-2.0** | 🟢 **the only permissive full LMS on this shelf**; your overlay can stay closed |
| Grade/roster boundary | Sakai's own gradebook + roster services | 🟢 ECL-2.0 | no copyleft boundary to draw — the reason this recipe is simple |
| Agent runtime | a **horizontal** agent (`CrewAI`, `LangGraph`, `OpenHands`) | 🟢 MIT / Apache-2.0 | 🔴 **there is no education-native agent** — fifteenth consecutive nil (`T6`) |
| Draft-before-write gate | `compose/code/grading-draft-gate/` | this KB | 🔴 **no feedback reaches a student record without a human accept step** |
| Marking / provenance | `compose/code/aiact-50-2-marking/` + `-pack/` | this KB | EMEA: AI Act Art. 50 transparency marking, **high-risk, full effect Aug 2026** |
| Licence intake gate | `compose/code/p571-cession-family-delegation/` | this KB | 🟢 **run it before admitting any new dependency** (see `P578`) |

**Steps:**
1. Stand up Sakai; **do not fork the core** — bind through its service APIs so the overlay stays a
   separate work even though ECL-2.0 would permit a closed fork anyway.
2. Put the horizontal agent behind the **draft-before-write gate**: the agent emits a *draft*
   comment; a human accepts, edits or rejects; only an accepted draft is written to the gradebook.
   🔵 **That is what makes the 19%/50% gap addressable** — students want AI-assisted feedback, faculty
   will not cede the record.
3. Mark every generated artefact through `aiact-50-2-marking/` and pack provenance with
   `aiact-50-2-pack/`. 🟢 **Required for EMEA from August 2026; harmless elsewhere.**
4. Keep the overlay's own licence closed if the engagement needs it. 🟢 **ECL-2.0 permits it. This step
   was impossible in every previous pass of this file.**

🟡 **Moodle variant:** if the client is already on Moodle, the same overlay works, but the boundary
matters — **`GPL-3.0` reciprocity attaches on distribution**, so ship the overlay as a **separate
plugin**, not as a patched core, and do not link it into core GPL code. 🔵 **Hosting a closed overlay
against an unmodified Moodle is fine; `P571` was wrongly saying otherwise.** 🔴 **Open edX is the
exception: `AGPL-3.0` §13 reaches network users, so a closed hosted derivative is not available.**

**Regional fit:** 🟢 **LATAM** — the 26%/87% gap is the clearest buy in any region, and private
non-profits lead adoption at **84%**. 🟢 **EMEA** — lead with the Art. 50 conformance pack, not the
tutor. 🟡 **North America** — lead with policy and staff enablement (10% have guidelines, 71% of
teachers untrained). 🟡 **APAC** — self-host it; **sovereignty is the regional frame**, and the buyer
the channel actually surfaces is **corporate learning**, not a university.

## 🟢 `P578` — a licence-regime intake gate, because this pass proved the shelf cannot be trusted to self-report

🔵 **Why this is a pattern and not a chore:** this pass measured the gate that decides whether a
licence **cedes** anything and found it diverged from the hardened classifier on **18 of 29 real
payloads**, in eight classes, **three of which refuse usable software**. 🔴 **A studio that inherits a
component list without re-reading payloads inherits those errors silently.**

**Wiring:**
1. `compose/code/lib/license_family.sh` → `family_of <payload>` for the **family** question. 🔴 **Never
   write your own ladder**: a licence body *names* other licences (GPL-3.0 §13 names the Affero GPL;
   MPL-2.0 §1.12 and EPL-2.0 name GPL), so a keyword probe over the body reads the licence cited
   rather than the one granted (`P571`–`P575`).
2. `compose/code/p411-cession-identity-gate/gate_cesion.py` → `clasificar()` for the **cession**
   question: does this document actually grant those rights, at this size, under this title, without
   fatal limitations? 🔵 **Two different questions** — the shared classifier reads `PageLM` as `MIT`,
   and `PageLM` prohibits commercial use and demands revenue sharing.
3. `compose/code/p429-cession-claim-audit/` → delivery class (`PERMISIVA` / `COPYLEFT` / …) for the
   ship/no-ship decision.
4. `compose/code/p571-cession-family-delegation/medir.py --check` in CI. 🟢 **It refuses to pass unless
   the historical before/after reproduces**, so a regression in the shared classifier fails the build
   rather than quietly re-labelling the shelf.

**What it catches, with this pass's real examples:** a repo whose licence **name** contains a
NO-OSI phrase (`ECL-2.0`, `P576`); a **BSD header** read as proprietary (`P577`); the **Unlicense**
read as non-commercial (`P579`); an **MPL/EPL** component read as GNU copyleft (`P573`/`P574`); a
**dual** licence reported by one arm only (`P578` → 🟡 `Gap 249`, still open); and a repo with **no
licence payload at all** — `speedyapply/2026-AI-College-Jobs` exists, is public, and grants nothing
(`P440` class, not admitted).

🟡 **Known limits, declared:** `Gap 249` — a dual MPL-2.0-**or**-EPL-1.0 grant still reports only the
MPL arm, so a component whose EPL arm you actually need will be scored on the wrong one. 🟡 **`Gap 250`**
🆕 — `p419-copyleft-identity` inlines a **third** licence classifier; it classifies by header, which
is the correct method, so it does not carry `P571`–`P575`, but it inherits nothing from `lib/`.

## 🟢 Forty-sixth pass, 2026-10-07 — three recipes (`P568` a permissive admissions layer with the copyleft boundary **measured**; `P569` a cross-component contract suite; `P570` sell against a free tier) and a **correction** to every recipe that cited an EPL or MPL component

⏱️ **Thirteenth pass of this date.** 🔵 **Licences read first-hand on 2026-10-07 from payload in the
repository, channel named per row (`P237`, `P250`, `P510`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed before allocation**: the occupied set was read from the
live tree **and** `archive/`, and this pass allocates `P560`–`P570`. 🔵 **Verified free before use:**
`P568`–`P570` appear nowhere in either tree.

## 🔴 Correction — any recipe that named an EPL or MPL component carried a licence **regime** this base could not read

🔵 **Not a correction to a step, but to what the steps were CHECKED against.** Until `P560`/`P561`
this pass, the shared classifier answered the unversioned `EPL` for every Eclipse payload and
stamped `MPL-2.0` on every Mozilla one. 🔴 **And `p429`, the instrument that decides whether a
component can be SHIPPED, tested for the string `EPL-2.0` — which the classifier could not
emit — so every EPL component in any recipe was scored `NO_CLASIFICADA`, i.e. no verdict at all.**

| | Before this pass | 🟢 After |
|---|---|---|
| An EPL component's delivery class | 🔴 `NO_CLASIFICADA` | 🟢 `COPYLEFT`, with the version read |
| An MPL-1.1 component | 🔴 reported `MPL-2.0` | 🟢 `MPL-1.1` |
| GPL-combinability of an EPL link | 🔴 **unanswerable** — `EPL` does not distinguish 1.0 (GPL-incompatible) from 2.0 (compatible if the steward designates it) | 🟢 answerable |

🟢 **No published recipe's verdict changes**, because this base holds no EPL or MPL-1.1 component in
a live recipe today. 🔴 **That is luck rather than design** — the first EPL dependency to enter a
recipe would have been scored "no verdict" and shipped on it.

## 🟢 `P568` — permissive **admissions/CRM** layer over a copyleft academic core, with the boundary drawn by measurement

🔵 **The problem this solves is the trade `verticals/solutions.md` measures and that has not moved
in fourteen passes:** the education domain model exists only under copyleft, and every permissive
ERP/CRM on the shelf is empty of academic concepts.

| Layer | Component | Licence (payload, 2026-10-07) | Why this one |
|---|---|---|---|
| Academic core (SIS, programmes, assessment, fees) | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟡 **LGPL-3.0** (8 241 B) | 🟢 **LGPL links without infecting the caller** — the one copyleft on this shelf that lets a studio keep its own modules closed |
| Admissions / lead management | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) 🆕 | 🟢 **MIT** (1 077 B, holder `Webkul Software`; `composer.json` agrees) | 🟢 permissive, and the CRM layer is where the client's commercial process lives |
| Tutor / assistant surface | Moodle in-core `ai/provider` extension point (`P520`) | 🟡 GPL-3.0 (Moodle core) | 🟢 **the provider is a plug-in boundary**, so the model choice stays the institution's |
| Model serving | self-hosted (Ollama / vLLM) | 🟢 MIT / Apache-2.0 | 🟢 in-country data; satisfies the APAC sovereignty brief |

🔴 **The boundary is the whole recipe, and it is where a naive composition becomes undeliverable.**

- 🟢 **Build custom academic modules against OpenEduCat (LGPL-3.0), not against `frappe/education`.**
  `frappe/education` is **GPL-3.0** (its `license.txt` is a **19 B** declaration: *"License: GNU GPL
  V3"*), so modules built *inside* it are GPL and the client cannot keep them closed.
  🔵 **Both are real options; they differ on exactly this.**
- 🟢 **Keep Krayin a SEPARATE SERVICE behind an API**, not a package linked into the Odoo/Frappe
  process. 🔵 Its MIT grant is clean, but co-process linking is how a permissive component inherits
  its host's obligations.
- 🔴 **Do not substitute `aureuserp/aureuserp` for Krayin "for licence diversity".** `P564`:
  byte-identical licence payload, same holder. 🔵 **It is one supplier, measured by `cmp`.**
- 🔴 **Do not substitute `hcengineering/platform` (Huly) as "the Apache-2.0 option".** `P563`: the
  payload is **EPL-2.0** (14 196 B), weak copyleft with file-level reciprocity — the Apache-2.0
  claim is the secondary channel's, not the repository's.

**Wiring, concretely.** OpenEduCat (Odoo modules) owns student/programme/enrolment as the system of
record. Krayin runs beside it and owns the admissions funnel; the two reconcile on a single
`applicant_id` pushed from Krayin to OpenEduCat on *admitted*, over Odoo's JSON-RPC — one direction
only, so there is no shared schema and no linked code. Moodle consumes the enrolment feed and the
tutor runs as an `ai/provider` implementation pointed at a self-hosted model.

**Gate before shipping:** run `compose/code/dependency-licence-closure` over both trees, then
`p429-cession-claim-audit` on each resolved family. 🟢 **Both now read versions (`P560`/`P561`) and
`p429` now classifies the EPL/MPL families it previously dropped (`P562`)**, so the closure report is
answering the question for the first time. 🔵 **Estimate: 8–10 weeks**, the bulk of it the academic
model and the reconciliation, not the AI.

## 🟢 `P569` — a **cross-component contract suite**: assert the producer's output set against each consumer's expected set

🔵 **This is `T2`/`P562` turned into a reusable instrument, and it is the pattern this base most
needs on itself.** The defect it catches belongs to **neither** component: `family_of` emitted `EPL`,
`p429` expected `EPL-2.0`, both were internally consistent, both suites were green, and the
**intersection was empty** for forty-five passes.

**The recipe, four steps, no new dependencies:**

1. **Enumerate the producer's real output set.** Not from its documentation — from its code and its
   corpus. For `family_of`: every `echo "<FAMILY>"` in `lib/license_family.sh`, unioned with the
   families it actually returns over the tree's payload corpus.
2. **Enumerate each consumer's expected set.** The literal membership sets: `p429`'s `RED` /
   `COPYLEFT` / `PERMISIVA` / `SIN_CESION`, `p444`'s `COPYLEFT` / `PERMISSIVE`, `p411`'s inline
   families.
3. **Assert the join, in both directions.** 🔴 **Producer value in no consumer set** → it silently
   becomes "unclassified" (this was `EPL`). 🔴 **Consumer value the producer cannot emit** → dead
   expectation that looks like coverage (this was `EPL-2.0`). 🟢 **Both are findings; the second is
   the one every one-sided suite misses.**
4. **Fail on either.** A new family added to the classifier must break this suite until every
   consumer places it — which is the only mechanism that makes a correction *travel* (`T1`: proximity
   does not, a shared file does not, a suite that asks every branch does).

🔵 **Scope, measured:** this base has **three** consumers of `family_of`'s family strings (`p429`,
`p444`, and `p411`'s inline copy), so the suite is small. 🟡 **`p411` must be migrated onto the
shared control first** — it still inlines its own classifier and still carries `P561`, stamping
`MPL-2.0` on any Mozilla payload. 🔵 **Estimate: 1 week**, and it retires a class rather than an
instance.

## 🟢 `P570` — what a studio sells when the entry tier is **free from four directions**

🔵 **The commercial recipe implied by `P567`.** With OpenAI, Anthropic, Google and Amazon all giving
teacher/student tools away, and McGraw Hill buying the AI coaching layer outright, the generic
assistant is not a deliverable. 🟢 **The four things the free tier structurally cannot supply, each
mapped to something on this shelf:**

| What the free tier cannot do | What to build | Component |
|---|---|---|
| Live inside the institution's data boundary | self-hosted inference, in-country | Ollama / vLLM (🟢 MIT / Apache-2.0) |
| Know the academic domain | SIS-integrated student/programme/assessment model | OpenEduCat 🟡 LGPL-3.0 (`P568`) |
| Produce conformity evidence | a dossier against a **named, in-force** instrument | 🟢 **Vietnam's law (in force 2026-03-01)** names automated assessment and behavioural monitoring; a Vietnam dossier is most of an EU Annex III dossier early |
| Prove its own controls measure something | audit the gates, not just run them | `P541`/`P550`/`P562` pattern — 🔵 **this KB's own findings are the demo** |

🔴 **The one to lead with is the third.** 🟢 **Vietnam's qualifier is a product requirement, not a
compliance cost:** a system is high-risk **only when its output is the sole basis for a decision
without meaningful human review** — so an auditable human decision point in the assessment flow
*removes* the classification. 🔵 **That is a design deliverable a free chatbot cannot be retrofitted
into**, and it is billable in every region whose instrument is risk-based.

## 🟢 Definition index — pass 46's findings, so `pattern-citation-audit` can resolve them

🔵 **Why this block exists.** `pattern-citation-audit` collects definitions **only from this file**,
so a finding headed in `agents/top.md` or `verticals/solutions.md` and cited across the tree reads as
**dangling** to it. 🔴 **That is why the audit reports 505 dangling numbers and 2 273 bold citations:
it is the convention, not a defect in the passes** — pass 45's `P550`–`P557` are dangling by exactly
the same mechanism, measured this pass. 🟢 **Cheap to do better than the norm**, so this pass's
findings get one-line definitions here, in the convention the instrument actually parses
(`DEF_A_B`). 🔵 **Each line says where the finding is MEASURED; it does not restate the evidence.**

### `P560` — the shared classifier **collapsed** EPL-1.0 and EPL-2.0 into one unversioned answer
Measured on four real payloads in `agents/top.md`; fixed in `lib/license_family.sh`; instrument
`compose/code/p560-epl-mpl-version-read/` (**22/22**, 5 mutants).

### `P561` — the MPL branch **stamped** `-2.0` on a version it never read
`P551` verbatim, one line above its own fix. Falsified against the canonical MPL-1.1 text
(**23 668 B**); see `repos/foundations.md`.

### `P562` — two **consumers** tested for family strings the classifier could not emit
`p429`'s `COPYLEFT` set asked for `EPL-2.0`; the producer emitted `EPL`; the intersection was empty
and both suites were green. Repaired in `p429` and `p444`; see `intel/trends.md` `T2`.

### `P563` — `hcengineering/platform` (Huly) is **EPL-2.0**, not the Apache-2.0 the channel claims
Weak copyleft, not permissive. Measured in `verticals/solutions.md`.

### `P564` — Krayin and AureusERP ship a **byte-identical** MIT payload, same holder
One vendor behind two apparently independent options (`cmp` clean, 1 077 B, `Webkul Software`).
Measured in `verticals/solutions.md`.

### `P565` — Krayin's default branch is `2.2`, so a probe assuming `main`/`master` reads NO-PAYLOAD
Confirms `probe_default_branch()`; see `verticals/solutions.md`.

### `P566` — `krayin/krayin-crm` does not exist; the canonical path is `krayin/laravel-crm`
0 refs, identical to the negative control in the same run.

### `P567` — North America's education-AI supply side is **consolidating** and the entry tier is free
McGraw Hill→TeachFX, a four-way free teacher tier, AFT's USD 23 M academy. Measured in
`intel/market.md`; the commercial response is `P570` above.

## 🟢 Forty-fifth pass, 2026-10-07 — two new recipes (`P558` audit the **model and data** tier a code-licence review never reaches; `P559` detect a fix that was appended instead of substituted) and a **second correction** to every Portuguese-scorer recipe

⏱️ **Twelfth pass of this date.** 🔵 **Licences read first-hand on 2026-10-07 from payload in cloned
trees or publisher metadata, channel named per row (`P237`, `P250`, `P510`). No star counts
(`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed before allocation**: the occupied set was read from the
live tree and this pass allocates `P550`–`P559`.

## 🔴 Second correction to the Portuguese essay-scorer recipes — `P551` falsifies the **pipeline** step, as `P544` falsified the **feature** step

🔵 **Pass 44 corrected the verb** (*port* → *reimplement*) and published the corrected step as:
*"reimplement the index set over spaCy's `pt_core_news_*` pipeline, from the published definitions,
using NILC-Metrix only as a comparison oracle run locally."* 🟢 **The verb is still right.** 🔴 **The
pipeline it names is not the permissive component that step implies.**

| Component | Pass 44 published | Measured this pass |
|---|---|---|
| `explosion/spaCy` (code) | 🟢 MIT | 🟢 **MIT** — confirmed, 1 128 B payload |
| `pt_core_news_sm/md/lg` (**the model you load**) | 🔴 *"model artefact licences unmeasured"* → `Gap 246` | 🟡 **CC-BY-SA-4.0** |
| `UD_Portuguese-Bosque` (the training corpus) | not addressed | 🟡 **CC-BY-SA-4.0** — the source of the above |
| any permissive PT treebank | assumed available | 🔴 **does not exist** (Bosque/GSD/Petrogold SA-4.0, PUD SA-3.0, CINTIL **NC-ND**) |

🟢 **Corrected step, and this is what the recipes should say from now on:**

> Reimplement the index set (TTR, MTLD, MATTR, HD-D and the syntactic-complexity indices) from the
> published definitions, over spaCy (**MIT**) loading `pt_core_news_md` (🟡 **CC-BY-SA-4.0**).
> **Do not fine-tune the model inside a client deliverable** — a tuned artefact is an *adaptation*
> and carries ShareAlike. Ship **your own code** plus an **unmodified** model and its attribution;
> if the engagement requires a tuned Portuguese pipeline, that artefact is **CC-BY-SA-4.0** and the
> client must agree to publish it on those terms **before** the work starts, not at delivery.
> Keep `nilc-nlp/nilcmetrix` (**AGPL-3.0**) as a **locally run comparison oracle only** — never
> vendored, never shipped, never hosted (`P544`).

🔴 **The commercial gate says ALLOWED and that is not the same as "no obligation".**
`commercial_use_ok()` returns true for CC-BY-SA-4.0 and it is correct — ShareAlike is not
NonCommercial. 🔵 **The cost is attribution plus copyleft on adaptations**, and the only question that
changes the deliverable is *"does this engagement fine-tune?"*. 🔴 **Open, and stated rather than
assumed:** how far ShareAlike reaches into a *fine-tuned* model artefact is read off the licence text
here, not tested against a published CC interpretation or counsel → **`Gap 247`**.

## 🟢 `P558` — Recipe: audit the **model and data** tier a code-licence review never reaches

🔵 **The engagement this sells into:** a client (or a studio's own delivery) has run a licence review,
read every repo-root `LICENSE`, found MIT and Apache-2.0, and signed off. 🔴 **In education that
review looked in the wrong tier** (`P553`): the valuable assets are curricula, rubrics, item banks,
skill corpora, model artefacts and treebanks, and the academic and public bodies that publish them
default to **Creative Commons**, not to MIT.

**Wire it together like this — every component named, all of it in this repo:**

| Step | What to run | Repo / file |
|---|---|---|
| 1 | Enumerate the **artefacts**, not the repos: every model weight, pipeline, dataset, corpus, rubric and skill pack the deliverable loads at build or run time | — |
| 2 | For each, fetch the **publisher's own metadata**, not the repo root — for spaCy that is `meta/<model>-<ver>.json` in `explosion/spacy-models` (the `license` field *and* the `sources[]` array) | `explosion/spacy-models` |
| 3 | Classify each payload with the **shared hardened classifier** — title-block, `P171`-safe, and since `P551` it reads the CC **version** instead of stamping 4.0 | `compose/code/lib/license_family.sh` → `family_of()` |
| 4 | Gate each on commercial use as a **second, independent axis** — a family name is not an answer | same file → `commercial_use_ok()` (`P250`) |
| 5 | Walk **one tier deeper**: for a model, the training corpora in `sources[]`; for a corpus, its own `LICENSE.txt`. 🔴 **This is the step that pays** — the PT models are CC-BY-SA *because Bosque is* | `git ls-remote` + payload read (`P510`) |
| 6 | Verify existence with a **negative control in the same run**, so a dead URL cannot read as a clean result | `P510` |
| 7 | Split the verdict into **host / ship / tune**, because the three have different answers for the same licence | `verticals/solutions.md` (pass 44 `P544`, pass 45) |
| 8 | Prove the auditing instruments themselves measure something before you bill for them | `compose/code/p542-empty-input-sweep/`, `p550-duplicate-definition-sweep/` |

🟢 **Worked output of exactly this recipe, run this pass on this KB's own Portuguese stack:** spaCy
MIT → `pt_core_news_md` **CC-BY-SA-4.0** → Bosque **CC-BY-SA-4.0** + WikiNER CC-BY-4.0 + vectors
**CC0**; no permissive PT treebank exists; CINTIL **refused** by the commercial gate. 🔵 **Eight
assets, four licence families, one refusal — from a stack whose repo roots read "MIT".**

🟡 **Effort, stated honestly:** 1–2 weeks for a single-language assessment stack of this shape; the
cost driver is step 5, because `sources[]` is not standardised across publishers and some ship no
machine-readable provenance at all. 🔴 **Where it stops:** this recipe establishes *what the licence
says*. It does not give a legal opinion, and `Gap 247` is open precisely at the point a client will
push hardest (fine-tuned artefacts).

## 🟢 `P559` — Recipe addendum: detect a fix that was **appended instead of substituted**

🔵 **Pair this with `P549`** (audit whether a client's quality gates measure anything at all). 🟢 **The
new check is one loop and it found a real defect in this KB's most-trusted file on its first run:**

| Step | What to run |
|---|---|
| 1 | `compose/code/p550-duplicate-definition-sweep/sweep_dupdefs.sh <root>` — flags every duplicate function definition whose **bodies differ**, skipping byte-identical re-declarations and declared frozen snapshots |
| 2 | For each finding, bind the **shadowed** body under a second name and run **both** over the client's real corpus — `oracle_inversion.sh` is the worked example |
| 3 | Report the **direction** of every divergence, not just the count: over-restriction costs an opportunity, under-restriction costs the deliverable, and they are not the same severity |
| 4 | Fix by **deleting** the superseded body — keeping the explanation as a comment is fine, keeping the *code* is the defect |

🔵 **Why a client will recognise this immediately:** the shape is universal to long-lived
rule-engines — pricing rules, eligibility checks, licence gates, fraud filters — where a fix is added
next to the thing it replaces and the suite stays green because it only ever calls the **name**.
🟢 **Measured on this KB: 302 files, 1 live finding, 7 of 27 real verdicts in its blast radius, and
the file it was in is the one every other instrument is told to reuse.**

## 🟢 Forty-fourth pass, 2026-10-07 — one new recipe (`P549`: audit a client's own quality gates) and a **correction** to every Portuguese-scorer recipe in this file

⏱️ **Eleventh pass of this date.** 🔵 **Licences read first-hand on 2026-10-07 from payload in cloned
trees, channel named per row (`P237`, `P250`, `P510`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed before allocation**: the occupied set was read from the
live tree and this pass allocates `P542`–`P549`.

## 🔴 Correction to every Portuguese essay-scorer recipe in this file — `P544` falsifies the feature step as written

`P532` (pass 42) and the retarget path in `Gap 236` both contain a step of the form *"port
`AI_AWE`'s feature extractor to Portuguese"*, and pass 43's `Gap 239` wrote the remedy as *"measure
whether spaCy supports TAALED-equivalent metrics, and if so **port the extractor**."*

🔴 **The verb is wrong, and it is not a quibble — it changes the legal shape of the deliverable.**
Measured this pass from payload (`P544`):

| Implementation | Licence | Can a client deliverable include it? |
|---|---|---|
| `nilc-nlp/nilcmetrix` (23 metric modules, HTTP service) | **AGPL-3.0** | 🔴 not if Globant hosts it — §13 triggers on network interaction |
| `nilc-nlp/coh-metrix-port` | **GPL-3.0** | 🟡 only if the whole deliverable is GPL |
| `kristopherkyle/TAALED` (the tool the gap names) | 🔴 **CC-BY-NC-SA-4.0** | 🔴 **no — NonCommercial** |

🟢 **Corrected step, and it is what the recipes should say from now on:** *reimplement* the index set
(TTR, MTLD, MATTR, HD-D, and the syntactic-complexity indices) over spaCy's `pt_core_news_*`
pipeline, **from the published definitions**, using NILC-Metrix only as a **comparison oracle run
locally** — never vendored, never shipped, never hosted. 🔵 **This is exactly `P504`'s shape**, where
the permissive implementation used the copyleft tier as its test oracle and confined the contact to
tests. 🔴 **Cost, stated rather than implied:** the index definitions are free, the **validation** is
not — the published tools carry years of it and a reimplementation inherits none, so a human-scored
agreement study against `essay-br` is part of the work, not a follow-up to it.

## 🟢 `P549` — Recipe: audit whether a client's quality gates **measure anything at all**

🔵 **Why this is a recipe and not an internal note.** This pass closed `Gap 243` by running the audit
on **this KB's own** `compose/code/`, and the result was **23 of 187** gates reporting success over an
empty input — including both of its gap gates. 🟢 **Every CI estate has this defect class and almost
nobody tests for it**, because the failure mode is a **green check**, not a red one.

### What it produces

A per-gate classification of a client's CI and quality estate into: refuses empty input (correct),
self-discovers its corpus (correct), **reports success having read nothing** (the defect), and
**unadjudicated** (declared, not absolved) — plus the one-line guard that fixes each defect.

### The components, with licences read this pass

| Component | Licence | Role |
|---|---|---|
| `compose/code/p542-empty-input-sweep/` (this KB) | 🟢 KB-internal, reusable | the sweep: static axis + behavioural run + two oracles |
| CPython ≥ 3.8 `sys.addaudithook` | 🟢 **PSF** (stdlib) | **oracle A** — counts the files the gate actually opens, in-process |
| POSIX `timeout` + exit-code discipline | 🟢 **GPL** (coreutils, *used*, not shipped) | bounds a gate that waits on the network |
| `compose/code/p383-region-heading-gate/` | 🟢 KB-internal | the worked example of the fix: `if not argv: return 2` |

### How to wire it

1. **Enumerate invocation points**, not repositories — every `*.py` / `*.sh` a pipeline calls.
2. **Classify statically** on three axes: does it consume positional arguments; is it **invocable at
   all** (a library module has no `__main__`); does it read **stdin**.
   🔴 **Axes 2 and 3 are not optional** — skipping them produced **49** accusations where the true
   number is **23** (`P543`).
3. **Invoke each with no arguments**, bounded by `timeout`, capturing exit code and both stream sizes.
4. **Apply oracle A** to everything that exits `0`: run it under an audit hook and count the
   non-code files it opens. 🟢 **Zero opens with exit `0` is the defect, proved.**
5. **Fall back to oracle B** (exit `0` with zero bytes on both streams) only where A cannot reach —
   and **label those rows as weaker**, because they are.
6. **Fix each defect with the guard, not with a usage note**: refuse an empty argument list with a
   non-zero exit and a message naming the correct invocation. 🔵 **A contract that has to be
   remembered is not a control** (`P237`).
7. **Add the fix as a regression assertion plus a mutant**, or the next instrument inherits the code
   and not the correction (`P480`).

### What this costs, stated honestly

🟢 **Cheap**: one engineer, 2-4 days for an estate the size of this KB's 187 entry points, and the
sweep is written. 🔴 **The uncomfortable part is not technical** — the deliverable tells a client
that some portion of their green history was never measured, so the engagement needs an agreed
remediation path before the number is produced, not after. 🔵 **The honest framing is the one this
pass used on itself**: the gates that *do* measure reproduce byte-for-byte (`P545`), so the finding
is bounded, not an indictment.

### 🔴 What it does **not** do

🔴 **Oracle A does not reach shell** — 31 rows in this KB's own run exit `0` after printing real
output and are left **unjudged**, and 9 more time out. 🔵 **Remedy named: a `PATH` shim that logs
`grep`/`cat`/`curl`/`git` invocations**, or a tracer where one is permitted. → **`Gap 244`**. 🔴 **And
the 23 defects this pass identified are named, not fixed** → **`Gap 245`**.

## 🟢 Forty-third pass, 2026-10-07 — the item-bank recipe's broken step is **fixed with code**, not re-described; and the Portuguese scorer recipe gains a reference implementation

⏱️ **Tenth pass of this date.** 🔵 **Licences read first-hand on 2026-10-07 from payload or the cloned
tree, channel named per row (`P171`, `P494`, `P510`, `P511`, `P237`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed before allocation.** The occupied set across the live tree
**and** `archive/` was enumerated with word boundaries over the **committed** tree: **533 distinct
numbers**, highest contiguous run ending at **`P290`**, with occupancy continuing to **`P532`** and
**`P591`, `P592`, `P593`, `P679`, `P900`, `P999`** above it. 🟢 **So `P533`–`P590` was free, and this
pass allocates nine from the bottom of that block:**

| | Finding | Filed in |
|---|---|---|
| `P533` | 🟢 **`Gap 238` CLOSED with code** — the QTI 3 template emitter, `43/0` with 19 controls | `repos/foundations.md` |
| `P534` | 🔴 **Mutation testing found 2 defects in this pass's own oracle** — a value asserted from itself is not measured | `intel/trends.md` |
| `P535` | 🟢 **`wwrwbs/AI_AWE` (ArguLens) — an assembled Apache-2.0 essay scorer exists**, permissive throughout | `agents/top.md` |
| `P536` | 🔴 **Three runtime defects an author cannot see in the XML** (unattainable `max`, silent constraint exhaustion, parser≠schema order) | `repos/foundations.md` |
| `P537` | 🟢 **`Gap 237`'s premise refuted for Chile** — the PAES has no essay, so there is no rubric to automate | `intel/trends.md` |
| `P538` | 🔴 **EU Annex III education deadline deferred to December 2027**; Article 50 did not move | `intel/trends.md` |
| `P539` | 🟢 **First comparable four-region measurement** — and LATAM leads faculty intent, NA trails by 22 pts | `intel/market.md` |
| `P540` | 🟢 **The corrected item-bank recipe**, below | `compose/patterns.md` |
| `P541` | 🔴 **A gate in this tree reported success while measuring zero files** — fixed, 8/8 → 11/11 | `intel/trends.md` |

### 🟢 `P540` — Recipe: a parametric item bank whose variants are **authored**, not hand-written

🔴 **What was wrong with every version of this recipe before pass 42.** Step 1 read *"author N
parametric variants with `qti3`"*. 🔴 **`P527` proved that step false as written** — the `writer`
package has 0 of 33 exports touching the template mechanism — and pass 42 could only replace it with a
**manual workaround**: hand-author the template XML from the fixture (~35 lines per item family) and
let `core` execute it.

🟢 **This pass replaces the workaround with the missing tool.** The step is now real.

| Layer | Component | Licence (channel) |
|---|---|---|
| **Authoring** | 🆕 `compose/code/p533-qti3-template-emitter/emit_template.py` | 🟢 **This KB's own code**, stdlib only |
| **Delivery / execution** | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) `packages/core` `0.13.2` | 🟢 **MIT** — `LICENSE.md` payload, © 2026 Longsight, Inc. |
| **Item calibration** | `py-irt` / `irtorch` / `catsim` | per `P499` chain (`Gap 39` calibration half) |
| **Variant comparability** | `EqUMP` 0.3.6 — Mean-Mean, Mean-Sigma, Haebara, Stocking-Lord, true-score | 🟢 **MIT** (`P499`) |
| | 🔴 observed-score / kernel equating | 🔴 **`Gap 234` — no permissive runtime.** Use the R side-car (`P518`) |
| **Delivery platform** | Open edX / Moodle per the existing chain | as already filed |

**Wiring, concretely:**

1. 🟢 **Declare the variable family.** `TemplateDeclaration("FACTOR")` … one per parameter. Emits
   `qti-template-declaration` with `cardinality="single" base-type="integer"`.
2. 🟢 **Declare the draws.** `SetTemplateValue("FACTOR", RandomInteger(2, 10, step=2))`.
   🔴 **Check `RandomInteger.grid()` before you trust `max`.** The draw is over a **grid**: when
   `step` does not divide `max-min`, **`max` never occurs** (`P536` defect 1).
3. 🟢 **Derive the answer key from the draw** — `SetCorrectResponse("RESPONSE", Variable("TARGET"))`.
   🔴 **Skip this and every variant shares one authored key, so all but one variant is marked wrong.**
   This is the step that makes a family *gradable* rather than merely *varied*.
4. 🟡 **Add constraints only after checking feasibility.**
   `estimate_constraint_restarts(draws, predicate)` returns exact acceptance over the declared grids.
   🔴 **`core` restarts at most 100 times and then delivers the violating draw** (`P536` defect 2) —
   at acceptance `0.001` that is a ~90% chance of shipping an invalid item, silently.
5. 🟢 **Assemble with `build_parametric_item`**, which emits children in **schema** order.
   🔴 **Do not emit in parser order**: `core` accepts any order, the XSD does not, and the result
   delivers correctly while failing validation (`P536` defect 3).
6. 🟢 **Calibrate and equate** per the `P499`/`P507` chain, with the `Gap 234` caveat above.

🔵 **Honest cost.** Steps 1–5 are now a few lines per item family instead of ~35 lines of hand-written
XML, and the grid/feasibility checks are the part that was not previously possible at all. 🔴 **Step 6
is still where the money goes** — equating is a psychometric exercise, not a library call.

🟡 **Stated limit carried into the recipe**, because `P533` carries it: the emitter is tested against
two upstream fixtures that the `qti3` schema gate validates, **not** against the official XSD directly
(`purl.imsglobal.org` is proxy-blocked) and **not** by running `qti3`'s own suite (third-party
dependencies not installable here). 🟢 **Whoever productionises this should run both.**

### 🟢 `P532`'s recipe updated — the Portuguese essay scorer now starts from a reference implementation

🔵 **`P532` (pass 42) specified building a Portuguese scorer from `essay-br` + open weights.** 🟢
**`P535` adds a step-0 that did not exist yesterday:** start from
[`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) — **Apache-2.0**, permissive across its whole tree
(root Apache-2.0, vendored `TextComplexityToolkit` MIT), three modules, LoRA adapter shipped in-repo.

**What transfers and what does not — the distinction that sets the budget:**

| Layer | Transfers to Portuguese? |
|---|---|
| Three-module architecture (move classifier → feature scorer → feedback generator) | 🟢 **Yes.** Reusable as a design |
| Qwen2.5 base-model family + LoRA fine-tuning pipeline | 🟢 **Yes.** Same families have Portuguese capability |
| Discourse-move taxonomy (*claim / data / counterclaim / rebuttal*) | 🟡 **In principle** — language-independent as a construct, needs Portuguese annotation |
| 🔴 **The 31 TAALED/QuanSyn features** | 🔴 **No.** `dep_files/adj_lem_list.txt` and `real_words.txt` are **English wordlists** → **`Gap 239`** |
| 🔴 **The scorer head** | 🔴 **No.** ArguLens emits a holistic **1–6**; ENEM is **five competencies C1–C5**, which is what `essay-br` is graded on |

🟢 **Net effect on `Gap 236`'s cost**: the pipeline, the training harness and the licence are now
free. 🔴 **The two layers that carry the pedagogy — features and rubric head — are still a build**, and
`P532`'s realistic target stands at **QWK ~0.63** (mid-band of the published 0.60–0.73), not
state-of-the-art.

## 🟢 Forty-second pass, 2026-10-07 — one new recipe (`P532`, an essay scorer whose judgement the client keeps) and one **correction** to every item-bank recipe in this file

⏱️ **Ninth pass of this date.** 🔵 **Licences read first-hand on 2026-10-07 from payload, registry or the
cloned tree — the channel is named per row (`P171`, `P494`, `P510`, `P511`, and new this pass `P525`'s
bound on `P517`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s rule followed.** The occupied set across the live tree **and** `archive/`
was enumerated with word boundaries before allocation: **519 distinct numbers**, highest contiguous run
ending at **`P520`**, with **`P592`, `P593`, `P679`, `P900`, `P999`** occupied above it. 🟢 **So
`P521`–`P591` was free, and this pass allocates twelve from the bottom of that block:**

| | Finding | Filed in |
|---|---|---|
| `P521` | the missing sweep axis was the **language of the query**; `P503`/`P508` now make a progression | `intel/trends.md` |
| `P522` | six distinct Portuguese essay-scoring trees, **zero licence grants** — *ungranted*, not *absent* | `agents/top.md` |
| `P523` | 🔴 **`P517`'s slug was wrong**; a `0`-ref result refutes a **slug**, not an **artefact** | `intel/trends.md` |
| `P524` | 🟢 **`essay-br` — MIT, human-graded ENEM corpus, UFPI**; the tier's permissive asset is *data* | `repos/foundations.md` |
| `P525` | the LanguageTool path is **two licences deep** (LGPL-2.1 engine, **GPL-3.0** wrapper) and the registry is silent | `repos/foundations.md` |
| `P526` | 🟢 **open weights reach the proprietary baseline**; compute, not capability, was the constraint | `intel/trends.md` |
| `P527` | 🟢 **`Gap 39` first half tested** — `core` generates variant families, the **writer cannot author them** | `repos/foundations.md` |
| `P528` | a keyword sweep in a monorepo needs a **package** column; `item-body-template` is a homonym | `intel/trends.md` |
| `P529` | a **fourth** market denominator; the 2026 spread is **5.9×**; carry total-vs-increment-vs-segment | `intel/market.md` |
| `P530` | 🔴 **the earliest binding education-AI clock is APAC's**, not the EU's | `intel/market.md` |
| `P531` | the **Spanish** half of `Gap 235` is a measured negative, and it is **structural** | `intel/trends.md` |
| `P532` | the recipe below | this file |

---

## P532 — Portuguese essay scoring **whose judgement the client keeps**

🔵 **Region: `LATAM`** — specifically **Brazil**, because the rubric, the corpus and the exam are
Brazilian. 🔴 **Do not read this recipe as pan-LATAM: `P531` found no Spanish equivalent of any layer.**

🟢 **This is the recipe `P516` said could not be written.** `P516` measured the essay-scoring tier and
found permissive scaffolding around proprietary judgement, concluding that a client could not own the
scoring. 🟢 **`P524`, `P525` and `P526` together change that, and this is the assembly.**

### What it produces

🟢 **A scorer that returns the five ENEM competency scores (C1–C5, 0–200 each) plus formative feedback,
where every component that *decides* a score is one the client holds** — and a defensible answer to *"who
graded this, and can you show the same model next year?"*, which `P516` identified as the obligation an
exam board cannot discharge with a hosted API.

### The components, with licences read this pass

| Step | Component | Licence (channel) | 🔵 Who owns the judgement |
|---|---|---|---|
| 0 · **Graded reference data** | [`lplnufpi/essay-br`](https://github.com/lplnufpi/essay-br) — Extended Essay-BR, human-graded on C1–C5 | 🟢 **MIT** — payload `main/LICENSE`, **1,114 B**, © 2021 LPNLP-UFPI (`P524`) | 🟢 **Client** |
| 1 · **Scoring model** | an **open-weight** LLM — `gpt-oss-120B` reached the hosted-proprietary band in `P526`'s own measurements; the 7B–8B class is where calibration earned the most | 🔵 **Per-model; verify each weight licence at source — this pass did not** | 🟢 **Client** |
| 2 · **Per-competency prompting** | one call per competency with the rubric in the prompt, **not** one holistic call | 🟢 Your own code | 🟢 **Client** |
| 3 · **Anchor essays** | one exemplar per score band per competency, drawn from `essay-br` **outside the test split** | 🟢 **MIT** via step 0 | 🟢 **Client** |
| 4 · **C1 feature source** | **LanguageTool**, pt-BR, offline — formal-register deviations as an explicit C1 feature | 🟡 **LGPL-2.1** engine (`master/COPYING.txt`, 26,432 B). 🔴 **Call the HTTP service; do *not* import `language_tool_python`, which is GPL-3.0 (`P525`)** | 🟢 **Client** |
| 5 · **Scale calibration** | bias calibration learned on **theme-separated folds** | 🟢 Your own code; `scikit-learn` BSD-3 | 🟢 **Client** |
| 6 · **Metrics** | QWK + Pearson against held-out human scores, **paired bootstrap** for significance | 🟢 Your own code | 🟢 **Client** |

### How to wire it

1. **Split `essay-br` by theme, not at random.** 🔴 **This is the step that decides whether the
   evaluation means anything.** `P526`'s source evaluates **cross-prompt** — unseen essay themes — because
   a within-theme split lets the model memorise topic vocabulary and inflates every figure.
2. **Score one competency per call**, rubric text in the prompt. 🟢 **Worth ~0.06 QWK over holistic
   scoring (0.47 → 0.53 raw), the cheapest structural gain available.**
3. **Add anchor essays and an explicit C5 element checklist.** 🟢 Raw QWK 0.53 → 0.59; C1 0.29 → 0.35.
4. **Feed LanguageTool counts into the C1 prompt**, over HTTP per step 4's licence note. 🟢 Best raw
   figure measured: **QWK 0.63, Pearson 0.63**.
5. **Fit the bias calibration on the theme-separated folds and apply it as standard post-processing.**
   🟢 **The single largest effect in `P526`'s table: a 7B model moves from QWK 0.25 to 0.42 with no
   change of model.** 🔵 **Most of what looks like bad judgement in this tier is a mis-scaled output.**
6. **Freeze and version everything that decides a score** — weights, prompts, rubric text, anchors,
   calibration coefficients — as one tagged artefact. 🟢 **This is the step that answers `P516`'s
   comparability objection, and it is only possible because no layer is a third party's API.**

### What this costs, stated honestly

| | |
|---|---|
| 🔴 **GPU time, one-off** | 🟢 **The binding constraint, and the whole reason `P526`'s source ended up on hosted APIs**: it ran out of Colab Pro credit mid-run on the 70B/72B stage. 🔵 **Budget the fine-tune explicitly; it is a known one-off price, not a research risk** |
| 🔴 **Accuracy ceiling** | 🔵 **Published essay-br band is QWK 0.60–0.73. The best configuration above is 0.63 — mid-band.** 🔴 **Do not sell state-of-the-art** |
| 🔴 **Statistical honesty** | 🔵 At 300 essays, ~0.04 differences are **inside the noise** by paired bootstrap. 🟢 **Scale the eval set before claiming a gain of that size** |
| 🟡 **Copyleft adjacency** | 🔵 LanguageTool is LGPL-2.1 as a service and **GPL-3.0 through its Python wrapper**. 🟢 **The HTTP boundary is the whole mitigation, and it costs one container** |
| 🔴 **Human-in-the-loop is not optional** | 🟢 **LGPD gives a right to review of decisions made *solely* by automated processing.** 🔵 **A Brazilian deployment needs a reviewing human by law, so design the queue in from day one** |

🔴 **What this recipe deliberately does not use.** The six Portuguese corretor repos in `P522` — including
the UTFPR project whose **measurements** this recipe is built on. 🔵 **They carry no licence grant, so
they are prior art to read and not code to ship.** 🟢 **The numbers are facts about the world and are
freely citable; the implementations are not freely usable.** ⚠️ **No pass of this KB has had counsel read
any of this.**

---

## 🔴 Correction to every item-bank recipe in this file — `P527` falsifies step 1 as written

🔵 **`P496`, `P507` and `P518` all open with a step of the form *"author N parametric variants of one item
with `LongsightGroup/qti3`"*, each flagging it as inferred-not-tested.** 🟢 **It has now been tested
(`P527`), and the flag was warranted: the step is false as written.**

| | Status before `P527` | 🟢 After `P527` |
|---|---|---|
| `qti3` **writer** emits parametric variants | 🔴 *"No evidence"* — inferred from package descriptions | 🔴 **Refuted by measurement.** `packages/writer`: **0 of 33 exports**, **0 files** referencing `qti-template-declaration` / `qti-template-processing` |
| QTI 3 variant families are reachable **at all** on this stack | 🔵 unknown | 🟢 **YES — `packages/core` implements the full mechanism**: declaration parsing, a real `randomInteger` draw over `min`/`max`/`step`, `qti-set-correct-response` keying off the draw, and a **constraint-retry loop up to 100 restarts** |

🟢 **The corrected step 1, which costs one file instead of a dependency:**

1. **Hand-author the template-variable XML**, using
   `packages/fixtures/xml/random-integer-template-reference.xml` **as the template** — it declares
   `FACTOR`/`TARGET`/`OFFSET`/`RESULT`, draws three parameters, computes `RESULT = FACTOR*TARGET + OFFSET`
   and sets the correct response to `TARGET`. 🟢 **A working parametric item in ~35 lines.**
2. **Use `qti3`'s `writer` for everything it *does* export** — the 20 interaction builders,
   `writeQti3AssessmentTest`, `buildQti3RubricBlock`, packaging and the manifest. 🔵 **The writer is still
   the right tool; it just cannot produce this one element.**
3. **Deliver through `core`**, which executes the template processing per candidate.
4. **Then proceed unchanged** into calibration (`py-irt` / `irtorch` / `girth`, MIT), linking (`EqUMP`,
   MIT), and observed-score or kernel equating (`KernEqWPS`, MIT, over the R side-car of `P518`).

🟢 **And the contribution this opens, because `qti3` is MIT (© 2026 Longsight, Inc.):** the missing
emitter is **~one module** — a `buildQti3TemplateDeclaration` / template-processing writer — and
`core`'s parser plus the fixture above give it a **ready-made test oracle** (round-trip: write → parse →
execute → assert the draw lands on the declared grid). 🔵 **`Gap 238` records it with that scope.** 🔴
**Stated limit, per `P527`: the suite was not executed this pass — installing a third-party repository's
dependencies is not permitted in this environment — so `core`'s generator is verified by reading its
implementation and fixtures, not by an observed run.**

## 🟢 Forty-first pass, 2026-10-07 — two recipes: `P518` reopens `P507`'s seam as an **R** seam and prices it honestly, and `P520` delivers the chain **inside Moodle** instead of beside it

⏱️ **Eighth pass of this date.** 🔵 **Licences below were read first-hand on 2026-10-07 from payload or
registry — the channel is named per row (`P171`, `P482`, `P494`, `P501`, and new this pass `P510`,
`P511`, `P517`, `P519`). No star counts (`P479`).**

🔵 **Numbering.** 🟢 **`P490`'s interim rule followed.** The occupied set across the live tree **and**
`archive/` was enumerated with word boundaries before allocation: **496 distinct numbers**, highest
contiguous run ending at **`P507`**, with **`P593`, `P679`, `P900`, `P999`** occupied above it. 🟢 **So
`P508`–`P592` was free, and this pass allocates thirteen from the bottom of that block:**

| | Finding | Filed in |
|---|---|---|
| `P508` | `KernEqWPS` — **observed-score and kernel equating under MIT**; the GPL-only half of `P500` falls | `repos/foundations.md` |
| `P509` | an MIT grant is not a permissive **closure** — `Imports: MASS` is GPL and the R runtime is GPL | `repos/foundations.md` |
| `P510` | `git ls-remote` is a **working existence oracle**; `github.com` HTML is uniformly `403` here | `agents/top.md` |
| `P511` | `master` on the raw channel is an **alias for the default branch**, not a branch fact | `repos/trending.md` |
| `P512` | **supersedes `P497`** — the agent shelf is **saturated**, not the query broken | `agents/trending.md` |
| `P513` | the **region acronym** is the regional channel's defect; country-named queries work | `intel/market.md` |
| `P514` | `P505`'s stale Annex III date is a **corpus** property, not an EMEA one | `intel/market.md` |
| `P515` | three irreconcilable market denominators, two in one summary; `P477` is necessary, not sufficient | `intel/market.md` |
| `P516` | essay scoring: **permissive code, non-permissive intelligence**; the fully-open option is archived | `intel/trends.md` |
| `P517` | `pypi.org/project/<name>/` returns **200 for nonexistent packages**; use the JSON API | `intel/trends.md` |
| `P519` | a `404` on an **existing ref** is not evidence the file is absent from the project | `verticals/solutions.md` |
| `P518`, `P520` | the two recipes below | this file |

---

## P518 — The comparable item bank, **honestly seamed**: `P507`'s Python chain plus an R equating service

🔵 **Supersedes nothing. It *completes* `P507` and corrects its scope.** 🔴 **`P507` celebrated removing
the JVM and said the chain then ran "in one Python dependency set". 🟢 **That was true of everything
`P507` covered, and `P507` covered only *linking* and *true-score* equating.** 🔴 **Observed-score and
kernel equating were absent from every permissive implementation then known (`P500`), so `P507` did not
have to seam them. `P508` makes them available — in **R** — so the seam is back, in a new place, and this
recipe is `P507` with that seam drawn where it actually falls.**

🔵 **Region: unplaced by construction — this is a technical chain, and the regulatory calendar that prices
it is per-region (`intel/market.md`).**

### What it produces

🟢 **Two exam variants on one reported scale, with a defensible answer to three questions a regulator or
an exam board will ask:** *is form B as hard as form A?*, *does the conversion hold for every subgroup?*,
and *how would the conversion differ under another accepted method?* 🔵 **The third question is the one
`P507` could not answer at all, and it is the one that matters most in a dispute.**

### The components, with licences read this pass

| Step | Component | Licence (channel) | Runtime |
|---|---|---|---|
| 1 · **Calibrate** both forms (IRT) | `py-irt` / `irtorch` / `girth` | 🟢 **MIT** (held) | 🟢 Python |
| 2 · **Link** B onto A's scale | `EqUMP` 0.3.6 — `linking/SL/Stocking_Lord.py`, `linking/HB/Haebara.py`, `linking/MM`, `linking/MS` | 🟢 **MIT** — registry `info.license = 'MIT'` + artefact `LICENSE` 1,068 B (`P499`, `P501`) | 🟢 Python |
| 3 · **True-score** equate | `EqUMP` — `equating/true/` | 🟢 **MIT** | 🟢 Python |
| 4 · 🆕 **Observed-score** equate (cross-check) | 🆕 `KernEqWPS` 1.0.7 — `LevineObservedEquate`, `PSEObservedEquate` | 🟢 **MIT** — payload `LICENSE` **1,077 B** + `DESCRIPTION` `License: MIT + file LICENSE` (`P508`) | 🔴 **R** (`P509`) |
| 5 · 🆕 **Kernel** equate (second cross-check) | 🆕 `KernEqWPS` — `KernelEquateFromScoresEG`, `FindBestBandwidth` | 🟢 **MIT** | 🔴 **R** |
| 6 · **DIF / fairness** gate | `difair` (`difair.dif`, `difair.poly`) + `aequitas` | 🟢 **MIT** (held) | 🟢 Python |
| 7 · **Orchestrate + audit trail** | `temporal` | 🟢 **MIT** (held, `technology` shelf) | 🟢 Any |

### How to wire it — the seam, concretely

🔴 **Do not embed R in the product.** 🟢 **`P509` is the reason and it is a *runtime* reason: `KernEqWPS`
is MIT, but it `Imports: MASS` (**GPL-2 | GPL-3**, `Priority: recommended`, 7.3-66) and runs on the R
interpreter, which is GPL. The licence topology forces a process boundary whatever the package licence
says.** 🔵 **So make the boundary a deliberate, narrow contract instead of an accident:**

```
┌──────────────── in-product, all MIT, one Python env ────────────────┐
│  py-irt ──► EqUMP (link, true-score) ──► difair / aequitas (DIF)    │
│                     │                                               │
│                     └── writes: scores_A.csv, scores_B.csv,         │
│                         anchor_map.json, conversion_truescore.json  │
└─────────────────────────────┬───────────────────────────────────────┘
                              │  files on a volume + one HTTP call
                              ▼
┌──── side-car: r-equating (own container, GPL stays inside) ─────────┐
│  R 4.x + KernEqWPS 1.0.7 + MASS                                     │
│  POST /equate/observed  → LevineObservedEquate | PSEObservedEquate  │
│  POST /equate/kernel    → KernelEquateFromScoresEG                  │
│                           (bandwidth via FindBestBandwidth)         │
│  returns: conversion table + method label + bandwidth used          │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        Temporal activity compares the 3 conversions and GATES:
        max |true-score − Levine − kernel| across the score range
```

🟢 **Three rules that make the seam cheap to live with:**

1. 🟢 **The contract is *data*, not R objects.** Scores in as CSV, a conversion table out as JSON, plus
   **the method label and the bandwidth actually chosen**. 🔵 **Never return a fitted R object — that
   is what turns a boundary into a dependency.**
2. 🟢 **The side-car is a separate image with its own licence manifest.** 🔵 **GPL artefacts stay in one
   container whose provenance is auditable, and the product image stays provably MIT-only.** 🔴 **Run the
   `dependency-licence-closure` pattern against **both** images, not the repo.**
3. 🟢 **Treat disagreement between the three methods as the *product*, not an error.** 🔵 **If true-score,
   Levine and kernel agree to within a set tolerance across the reported range, that agreement **is** the
   comparability evidence. 🔴 **If they diverge, the forms are not comparable and no single number should
   be published** — which is precisely the finding an exam board needs before results day, not after.

### Effort, and what is genuinely unknown

| Piece | Estimate | Confidence |
|---|---|---|
| Steps 1–3, 6 (`P507`'s chain, unchanged) | 🟢 as `P507` scoped it | 🟢 **High** — `P507` shipped it |
| Side-car container + two endpoints | 🟢 **~1 week** | 🟢 **High** — `KernEqWPS` exports the functions directly; no R to write beyond the wrappers |
| Temporal comparison + gate | 🟢 **~1 week** | 🟢 High |
| 🔴 **Choosing the divergence tolerance** | 🔴 **unestimated** | 🔴 **Low — this is the real open question.** 🔵 **It is a measurement decision an exam board must own, not a parameter a studio picks**, and nothing in this KB can supply it |

🔵 **The alternative, for a client who will not accept a second runtime:** 🟢 **port the minimum slice —
`KernelEquateFromScoresEG` + `LevineObservedEquate` + `FindBestBandwidth` — to Python, testing against
`KernEqWPS` as the oracle.** 🟢 **That is the `P504` shape exactly (permissive code, incumbent as test
oracle, contact confined to tests) and it is **Gap 234**. 🔴 **Scope it from `NAMESPACE`: 41 exported
functions in total, but the bandwidth logic is the novel part and the rest is standard.**

---

## P520 — Deliver it **inside** Moodle: an `ai/provider` plugin instead of a portal nobody logs into

🔵 **The failure mode this recipe exists to prevent is not technical.** 🔴 **Every chain above ends in a
conversion table and a fairness report — artefacts that live in a studio's dashboard, which teachers do
not open.** 🟢 **`verticals/solutions.md` measured a third delivery shape in Moodle's own tree this pass,
and it changes the default.**

### The three shapes, and when each is right

| Shape | Component | Licence of **your** work | Survives upgrades | Choose it when |
|---|---|---|---|---|
| **Outside, agent-driven** | `peancor/moodle-mcp-server` | 🟢 **MIT** | 🟢 Yes | 🟢 **The client must own the IP**, or the consumer is an agent rather than a teacher |
| 🆕 **Inside, in-tree plugin** | 🆕 `ai/provider/*` + `ai/placement/*` against Moodle's published contract | 🔴 **GPL-3.0** | 🟢 **Yes** | 🟢 **Teachers must meet it in the UI they already use**, and the client runs its **own** models |
| **Fork and patch** | — | 🔴 GPL-3.0 | 🔴 **No** | 🔴 **Now the wrong default** |

### The wiring, measured in-tree on `MOODLE_500_STABLE` (release `5.0.11`, Build `20261005`)

🟢 **Three extension points, confirmed by payload with byte sizes as evidence of implementation
(`P500`'s lesson), not by documentation — 🔴 `docs.moodle.org` is `EGRESS_BLOCKED` from this session:**

```
ai/classes/provider.php        (7,710 B)  ◄── implement this: your backend
ai/classes/manager.php        (25,540 B)  ◄── the core that dispatches
ai/classes/aiactions/
    generate_text.php          (2,494 B)  ◄── an action = one thing a user does
ai/provider/openai/     ─┐
ai/provider/ollama/      ├── existing providers = your worked examples
ai/placement/courseassist/ ┘   (a placement = WHERE it is offered)
```

🟢 **The build:** a provider plugin whose backend is **not** a chat model but **the `P518` chain** — it
receives an item-bank or results request from a placement, calls the Python service, and returns the
comparability verdict and DIF flags as the action's result. 🔵 **`ai/provider/ollama` is the template to
copy: it is in core, so a **self-hosted** provider is a first-class citizen, which is what makes this
viable for a ministry or exam board that will not send student data to a third party.**

### Why this ordering is the commercial point

| | |
|---|---|
| 🟢 **Upstreamable** | A plugin against a published contract survives Moodle upgrades; 🔴 **a fork is re-paid every release**, and Moodle shipped `5.0.11` two days before this pass |
| 🟢 **Data stays home** | `ai/provider/ollama` in core means **"your models, your infrastructure"** is a configuration choice, not a custom build — the answer to the **EMEA** sovereignty objection and to **Vietnam's** pre-registration regime (`intel/market.md`) |
| 🔴 **The licence cost is real and should be quoted up front** | 🔴 **In-tree work is GPL-3.0.** 🟢 **Decide it on IP ownership before writing code, because the two shapes are not refactorable into each other** |
| 🟢 **Article 50 falls out of the placement** | 🔵 **A placement is the one point where the learner sees the AI** — so it is the natural home for the disclosure and synthetic-content marking that **Article 50 requires from 2026-08-02** (`compose/code/aiact-50-2-marking`), 🟢 **rather than a banner bolted on later** |

🔴 **What this recipe does not claim.** 🔵 **No pass has built this plugin.** 🟢 **The three extension
points, their byte sizes, the two provider examples, the placement example and the release string were
all read first-hand from the tree this pass.** 🔴 **Everything about the *authoring* workflow — how
actions are registered, what the provider interface's method signatures are — was **not** read, because
the documentation channel is blocked and this pass did not fetch the class bodies.** 🔵 **Next pass:
fetch `ai/classes/provider.php` and `ai/provider/ollama/` in full and write the signatures down.**

## 🟢 Fortieth pass, 2026-10-07 — one recipe, `P507`: the JVM seam `P496` called "the chain's only ugly seam" closes, because the Python reimplementation it proposed already exists and is MIT

⏱️ **Seventh pass of this date.** 🔵 **Licences below were read first-hand on 2026-10-07 from payload,
registry or published artefact — the channel is named per row (`P171`, `P482`, `P494`, and new this pass
`P501`). No star counts (`P479`).**

🟢 **One recipe, and it is an upgrade to a chain rather than a new chain.** 🔵 **`P496` (pass 39) shipped a
correct six-step chain and ended by naming its own worst property:** *"The JVM boundary is real and is the
chain's only ugly seam… reimplement Stocking-Lord in Python against `psychometrics` as the reference. The
second is a days-not-weeks task and removes the JVM from the deliverable."* 🟢 **That task is already done,
by someone else, under MIT, with tests — `P507` is `P496` with step 4 replaced.**

🔵 **Numbering.** The ceiling across the whole tree including `archive/` was `P498` before this pass. 🟢
**`P490`'s interim rule followed** — every number below was checked free in **both** the live tree and
`archive/` before allocation. This pass allocates nine:

| | Finding | Filed in |
|---|---|---|
| `P499` | `EqUMP` — a permissive **Python** implementation of IRT linking exists | `repos/foundations.md` |
| `P500` | a **declared directory** is not an implemented capability; observed-score equating stays open | `repos/foundations.md` |
| `P501` | when the declared repo does not resolve, the **published artefact** is the authoritative licence channel | `repos/foundations.md` |
| `P502` | a licence probe without an independent **existence check** collapses three states into one string | `agents/top.md` |
| `P503` | on a saturated shelf the productive variable is query **shape**, not query **topic** | `intel/trends.md` |
| `P504` | the permissive implementation uses the **copyleft tier as its test oracle**; contact confined to tests | `repos/foundations.md` |
| `P505` | the EMEA regulatory channel is **reproducibly stale** on the Annex III date | `agents/trending.md` |
| `P506` | `cran/*` is a **mirror namespace**, not canonical | `repos/foundations.md` |
| `P507` | the comparability chain runs **without a JVM**, in one Python dependency set | this file |

---

## P507 — The *comparable* item bank, all-Python: two exam variants, one scale, no subgroup penalty, no JVM

🟢 **Supersedes `P496` at step 4 only.** 🔵 **Everything `P496` says about anchor design is unchanged and
still carries the whole chain — read it there; it is not repeated here.** 🔵 **Region: unplaced by
construction — the chain is jurisdiction-neutral (`P474`); it is *driven* by regulation per region (see
`intel/market.md`).**

### The claim this chain defends — unchanged from `P496`

> 🟢 *"Variants A and B are on a **common scale**, their difficulty difference is **0.04 logits with a
> standard error of 0.06**, and **no item** shows DIF above ETS class **B** for any reported subgroup."*

### The chain

| Step | Component | Licence (channel) |
|---|---|---|
| 1 · author variants **with a frozen anchor set** | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · payload `main/LICENSE.md` · 1,072 B |
| 2 · deliver, capture responses | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · payload `main/LICENSE` · 1,076 B |
| 3 · calibrate each form separately | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · payload `master/LICENSE` · **1,121 B** |
| 🆕 **4 · link the two calibrations onto one scale — in Python** | **`EqUMP` 0.3.6** · `linking/SL/Stocking_Lord.py` (**12,833 B**) · `linking/HB/Haebara.py` (**13,803 B**) · `linking/MM/` · `linking/MS/` | 🟢 **MIT** · **artefact payload** `eqump-0.3.6/LICENSE` · **1,068 B** · 🔴 declared repo unresolvable (`P501`) |
| 🆕 **4b · convert linked parameters to comparable scores** | **`EqUMP`** · `equating/TSE/tse.py` (**4,782 B**) — true-score equating | 🟢 **MIT** (same artefact) |
| 5 · test every item for DIF | [`ZIYINGJERRY/difair`](https://github.com/ZIYINGJERRY/difair) | 🟢 **MIT** · payload `main/LICENSE` · **1,075 B** |
| 6 · audit the decision, not just the items | [`dssg/aequitas`](https://github.com/dssg/aequitas) | 🟢 **MIT** · payload `master/LICENSE` · **1,083 B** |
| 7 · adapt the form per learner (optional) | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** · payload `main/LICENSE` · **1,514 B** |
| 8 · run it all on the client's hardware | `ollama` / `vLLM` (shelved) | 🟢 **MIT** / **Apache-2.0** |

🟢 **Eight steps, one language, zero copyleft in the shipped runtime.** 🔵 **`meyerjp3/psychometrics`
(Apache-2.0, Java) stays on the shelf as the **reference implementation** — see "how to validate" below —
but it is no longer in the delivery path.**

### What actually changed, and why it is not cosmetic

| | `P496` (pass 39) | 🆕 `P507` (this pass) |
|---|---|---|
| Linking step runtime | 🔴 **JVM** — `psychometrics` invoked as a CLI over a TSV | 🟢 **In-process Python import** |
| Deliverable's language count | 🔴 **2** (Python + Java) | 🟢 **1** |
| Linking methods available | Mean-Mean · Mean-Sigma · Stocking-Lord | 🟢 **+ Haebara** (four, all with test files) |
| Score conversion | 🔴 **not in the chain** | 🟢 **true-score equating, step 4b** |
| `P496`'s proposed remedy | *"reimplement Stocking-Lord in Python — days not weeks"* | 🟢 **Unnecessary. It exists, tested, MIT** |

🔵 **The cost `P496` was willing to pay was a reimplementation plus the risk of getting Stocking-Lord
subtly wrong.** 🟢 **`EqUMP` removes both, and it validates its own output against the GPL R tier
(`tests/linking/SNSequate.R`, `tests/base/mirt_estimate.R`) — so the reference check `P496` wanted is
already wired into the package's test suite (`P504`).**

### How to wire step 4, concretely

🟢 **Install:** `pip install EqUMP` — **`numpy` · `scipy` · `pandas` · `matplotlib` · `python-dotenv`**,
all permissive. **Python `>=3.9, <3.14`.**

1. 🟢 **Calibrate form A and form B separately** with `py-irt` (step 3). Two parameter tables, two metrics.
2. 🟢 **Extract the anchor items' parameter pairs** — the subset present in both forms. 🔴 **`P496`'s anchor
   rules decide whether this step is possible at all: ≥20% of the form, ≥20 items, full difficulty range,
   and the anchor must be frozen and excluded from the generator's reach.**
3. 🟢 **Solve for the linking constants** with `EqUMP`'s `linking/` module. 🔵 **Prefer **Stocking-Lord** or
   **Haebara** over Mean-Mean/Mean-Sigma** — both are *characteristic-curve* methods, minimising the
   difference between the forms' response curves rather than matching parameter moments, and both are far
   more robust when the anchor contains a few misfitting items. 🟢 **`EqUMP` now gives you both**;
   `psychometrics` gave Stocking-Lord only.
4. 🟢 **Apply the transformation to *all* of form B's parameters**, then take the difficulty difference and
   its standard error — that is the number in the claim sentence.
5. 🟢 **Convert to comparable scores** with `equating/TSE` (step 4b) if the deliverable reports scores
   rather than abilities.
6. 🟢 **Then run DIF (step 5) on the linked parameters, not the raw ones** — 🔴 **this ordering matters and
   is easy to get backwards.** DIF asks whether an item behaves differently *for a subgroup at the same
   ability*, so "the same ability" must already be on one scale.

### 🔴 Where this chain still cannot go — stated so nobody discovers it in delivery

| Need | Status | What to do |
|---|---|---|
| **Observed-score equating** (equipercentile, frequency-estimation) | 🔴 **No permissive implementation in any language** (`P500`) — `EqUMP`'s `equating/obs/` is a **0-byte stub**, and `equate`/`kequate` are **GPL** | 🔴 **Side-car behind a process boundary, or scope it out.** 🔵 **True-score equating (4b) covers many IRT-based designs; confirm with the client's psychometrician which the programme requires** |
| **Kernel equating** | 🔴 **`EqUMP`'s `equating/kernel/` is a 0-byte stub**; `SNSequate` is **GPL (≥2)** | 🔴 Side-car only |
| **Scoring module** | 🔴 `EqUMP`'s `scoring/__init__.py` is **0 bytes** | Use `py-irt`/`catsim` ability estimates |
| **Proof the authoring tool emits *parametric* variants** | 🔴 **Still unproven** — `Gap 39`'s original text calls this *"inferido de la descripción de los paquetes, no probado"*, and no pass has tested it | 🔵 **Unchanged from `P496`. This is the chain's oldest untested assumption** |

### 🔵 Risk register for step 4, new this pass

| Risk | Severity | Mitigation |
|---|---|---|
| 🔴 **The declared repository does not resolve** (`P501`) — 15 README probes, 14 licence probes, no `200` | 🔴 **Supply-chain, real** | 🟢 **Pin the exact artefact: `eqump-0.3.6.tar.gz`, `sha256 c4699943f4523c51c6ec5386a092804434dba791f03da358429fbfbdaebc80c2`, 66,581 B**, and vendor it. 🔵 **The grant travels with the artefact** (`LICENSE` ships inside it), so the MIT right to vendor is not in doubt — but a project whose repo you cannot read is a project you cannot patch |
| **Young package** — 9 releases, latest **2026-07-15** | ⚠️ Moderate | 🟢 **Validate against the R reference the package itself uses** (`SNSequate`, `mirt`) on the client's own anchor data before trusting a production number. 🔵 **`psychometrics` (Apache-2.0) remains a second independent oracle** |
| **Four maintainers, one project** | 🔵 Low-moderate | 🟢 Better than the single-maintainer position pass 39 recorded for this tier; still vendor it |
| 🔴 **Run `--self-test`-grade validation yourself** | 🔴 — | 🔴 **This pass could not execute any in-tree instrument** (`P480`, fourth consecutive denial), so **no byte-level claim in this recipe was produced by a checked-in gate.** 🔵 Every byte count above was read directly from the artefact or the raw channel in this pass |

---

## 🟢 Thirty-ninth pass, 2026-10-07 — one recipe, `P496`: `P491` corrected, because calibration is not comparability

⏱️ **Sixth pass of this date.** 🔵 **Licences below were all read from payload on 2026-10-07 (`P171`), or
from the source-header channel where no payload exists (`P494`). No star counts (`P479`).**

🔴 **One recipe, and it is a correction rather than an addition.** 🟢 **`P491` (pass 38) promised to
*"prove two exam variants are equivalent"* and shipped a chain that cannot prove it.** 🔵 **`P496` is the
same chain with the missing link installed and the claim restated to what the evidence supports.**

🔵 **Numbering: `P496`.** The ceiling across the whole tree including `archive/` was `P491` before this
pass. 🟢 **`P490`'s interim rule followed** — every number below was checked free in **both** the live tree
and `archive/` before allocation. This pass allocates seven:

| | Finding | Filed in |
|---|---|---|
| `P492` | `Gap 39` was closed at half — calibration is not comparability | `repos/foundations.md` |
| `P493` | licence topology is a property of the **tier**, not the industry | `repos/foundations.md` |
| `P494` | absent payload ≠ absent licence; rank the channels, read the dates | `repos/foundations.md` |
| `P495` | a market series is **arithmetically falsifiable against itself** | `intel/market.md` |
| **`P496`** | **this recipe** | `compose/patterns.md` |
| `P497` | a topic-word query fails by returning a **homonym class** | `agents/trending.md` |
| `P498` | a control **prescribed but not executed** is indistinguishable from not found | `intel/trends.md` |

### 🔴 What `P491` got wrong, stated precisely

🟢 **`P491`'s diagnosis was right and is worth keeping**: *"if two students sat different variants and
nothing measured that the variants were equally hard, their scores are not comparable."* 🔴 **Its remedy
does not produce that measurement.**

| `P491`'s step | What it yields | 🔴 What it does **not** yield |
|---|---|---|
| Author N variants with `LongsightGroup/qti3` | QTI 3 item packages | 🔴 **No evidence the writer emits *parametric* variants** — the archived `Gap 39` says this is *"inferido de la descripción de los paquetes, no probado"*, and no pass has proved it |
| Deliver with `amp-up-io/qti3-item-player` | standards-compliant delivery | — |
| Calibrate each variant with `py-irt` / `irtorch` | 🟢 item parameters **per variant** | 🔴 **Parameters on *separate scales*.** IRT identifies the metric only up to a linear transformation |
| Compare the parameter tables | 🔴 **a comparison in mismatched units** | 🔴 **Not an equivalence claim** |

🔴 **The defect in one sentence: you cannot conclude "variant A is as hard as variant B" from two
independent calibrations, for the same reason you cannot conclude two buildings are the same height from
one measurement in feet and one in metres.** 🟢 **The fix is standard psychometrics and this KB simply did
not hold it: put both calibrations on a common metric first.**

---

## P496 — The *comparable* item bank: two exam variants, one scale, no subgroup penalty — permissively, on the client's own hardware

🟢 **Supersedes `P491`.** 🔵 **Closes the half of `Gap 39` that pass 38 left open (`P492`); the open half is
recorded in `intel/open-gaps.md`.** 🔵 **Region: unplaced by construction — the chain is
jurisdiction-neutral (`P474`); it is *driven* by regulation per region, see `intel/market.md` and
`intel/trends.md` T3.**

### The claim this chain can actually defend

> 🟢 *"Variants A and B are on a **common scale**, their difficulty difference is **0.04 logits with a
> standard error of 0.06**, and **no item** shows DIF above ETS class **B** for any reported subgroup."*

🔵 **That sentence is an accuracy-and-robustness claim with numbers attached, which is what Annex IV asks
for.** 🔴 **"Our AI writes good questions" is not, and neither is `P491`'s version.**

### The chain

| Step | Component | Licence (channel) |
|---|---|---|
| 1 · author variants **with anchor items** | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** · payload `main/LICENSE.md` · 1,072 B |
| 2 · deliver, capture responses | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** · payload `main/LICENSE` · 1,076 B |
| 3 · calibrate each form | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** · payload `master/LICENSE` · **1,121 B** |
| 🆕 **4 · link the two calibrations onto one scale** | [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) — **Mean-Mean, Mean-Sigma, Stocking-Lord** | 🟢 **Apache-2.0** · 🔴 no payload; per-file headers govern (`P494`) |
| 🆕 **5 · test every item for DIF** | [`ZIYINGJERRY/difair`](https://github.com/ZIYINGJERRY/difair) — Mantel-Haenszel + logistic + purification | 🟢 **MIT** · payload `main/LICENSE` · **1,075 B** + `pyproject.toml` |
| 🆕 **6 · audit the decision, not just the items** | [`dssg/aequitas`](https://github.com/dssg/aequitas) | 🟢 **MIT** · payload `master/LICENSE` · **1,083 B** |

🟢 **Every licence in the table above was re-read from payload on 2026-10-07**, not carried forward:
`qti3` **1,072 B**, `qti3-item-player` **1,076 B**, `py-irt` **1,121 B**, `catsim` **1,514 B** — 🟢 **all
four byte-for-byte identical to the pass-38 record**, plus the two new rows.

| 7 · adapt the form per learner (optional) | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3** · payload `main/LICENSE` · **1,514 B** |
| 8 · run it all on the client's hardware | `ollama` / `vLLM` (already shelved) | 🟢 **MIT** / **Apache-2.0** |

### How to wire it — the part that is not obvious

🔴 **Step 1 carries the whole design, and it is a *test-assembly* decision, not a software decision.** 🟢
**The anchor set is what makes step 4 possible at all:**

- 🟢 **Build each variant with a common subset of items** — the **anchor**. Rule of thumb from
  large-scale practice: **≥ 20% of the form, ≥ 20 items**, spanning the full difficulty range, **identical
  in wording and position-insensitive**.
- 🔴 **If the variants share no items and no students, nothing downstream can link them.** 🔵 The
  alternative design is **common-person**: a subsample sits **both** forms. More expensive, and the only
  option when item reuse is forbidden for security reasons.
- 🔴 **An LLM that paraphrases the anchor items has destroyed the anchor.** 🟢 **Freeze the anchor set and
  exclude it from the generator's reach** — this is the single most likely way an AI-authoring pipeline
  silently breaks this chain.

🟢 **Step 4, concretely.** Calibrate form A and form B separately with `py-irt`. Take the **anchor items'**
parameter pairs and feed them to `psychometrics`'s linking methods, which solve for the slope `A` and
intercept `B` that map form B's metric onto form A's. 🔵 **Prefer Stocking-Lord** — it minimises the
difference between the two forms' **test characteristic curves** rather than matching parameter moments,
and it is the more robust of the three when the anchor contains a few misfitting items. 🟢 **Apply the
transformation to *all* of form B's parameters, then compare.**

🔴 **The JVM boundary is real and is the chain's only ugly seam.** `psychometrics` is Java; the rest is
Python. 🟢 **Two honest options, both cheap:** run the linking step as a **CLI invocation** over a TSV of
anchor parameter pairs (the transformation is ~10 numbers in, 2 out — this is not a hot path), or
**reimplement Stocking-Lord in Python** against `psychometrics` as the reference. 🔵 **The second is a
days-not-weeks task and removes the JVM from the deliverable**, which is usually worth it; the first is
correct on day one.

🟢 **Step 5, concretely.** Run `difair.dif.mantel_haenszel` per item with the reported subgroup as the
focal group and the **linked** ability estimate as the matching variable. 🔴 **Match on the linked score,
not the raw score** — matching on a raw score that is not on a common scale re-introduces exactly the
error step 4 removes. 🟢 **Use `iterative purification`** so items that themselves show DIF stop
contaminating the matching criterion. 🔵 **Report ETS A/B/C classes**, because that is the vocabulary an
exam board and a regulator both already read.

🟢 **Step 6 answers a different question and both are needed.** DIF asks *"is this **item** unfair given
equal ability?"*; `aequitas` asks *"does the **decision** this system produces show a group gap?"* 🔴 **An
assessment can be free of item-level DIF and still produce a disparate pass rate**, because a real ability
difference upstream is not an item defect. 🔵 **`difair`'s own pipeline-attribution tab exists for exactly
this split** — it asks which stage of the pipeline produced an observed group gap.

### What it costs, and what it is worth

| | |
|---|---|
| 🟢 **Build** | **6–8 weeks** for the chain on an existing QTI stack: 1 wk anchor design, 1 wk calibration harness, 2 wk linking (3 if reimplementing Stocking-Lord in Python), 1 wk DIF + reporting, 1–2 wk evidence pack |
| 🔴 **Hard prerequisite** | **Response data at volume.** 🔴 Rough floor for stable 2PL: **~500 responses per item**, and the anchor needs it on **both** forms. 🔵 **No library substitutes for this**, and it is the real reason this chain is rare |
| 🟢 **Licence posture** | 🟢 **MIT · MIT · MIT · Apache-2.0 · MIT · MIT · BSD-3** — in-product, no copyleft. 🔴 **Keep `difR` (GPL) only as an offline validation oracle**, never linked |
| 🟢 **Deployment** | 🟢 **Fully on-premise.** No component calls out; `difair_studio.html` even runs air-gapped in a browser |
| 🔴 **What it does not do** | 🔴 **It does not prove the LLM writes good items.** It proves that **whatever was written** is on a known scale and carries no measured subgroup penalty. 🔵 **That is a stronger and much narrower claim — sell that one** |

### 🔴 The two residual risks, named so a client hears them first

| Risk | Reality | Mitigation |
|---|---|---|
| 🔴 **`difair` is v0.7.0, two authors, not on PyPI** | 🔴 Real. 🟢 But cross-validated against `difR`'s own R sources over **108 item-level statistics** (MH χ² agreeing to **5.8e-13**) and against **TIMSS 2019** | 🟢 **Pin a commit SHA**, vendor it, keep `difR` as the offline oracle for re-validation on upgrade |
| 🔴 **`psychometrics`'s root `pom.xml` carries a 2011 GPL-3 header** | 🔴 The code is **Apache-2.0** on three channels (`P494`); 🔴 **an SPDX scanner reading `pom.xml` will report GPL-3** | 🟢 **Brief legal in writing before the scan**, citing the per-file headers and the `<licenses>` element. 🔵 **Expect to have this conversation** — it is the predictable finding of any client OSS review board |

### 🔴 Still open, and `P496` does not pretend otherwise

🔴 **The first half of `Gap 39` remains unmeasured:** nobody has demonstrated first-hand that
`LongsightGroup/qti3`'s writer emits **parametric variants of the same item**. 🔵 **`P496` routes around it
— anchor-based linking works regardless of how the variants were authored** — but the KB should stop
implying the writer does something no pass has watched it do. 🟢 **Recorded as a live row in
`intel/open-gaps.md`.**

---

## 🟢 Thirty-eighth pass, 2026-10-07 — one recipe, `P491`: the chain Gap 39 asked for, closed end to end and permissively

⏱️ **Fifth pass of this date.** 🔵 **Licences below were all re-read from payload on 2026-10-07
(`P171` title-block classification). No star counts (`P479`).**

🟢 **One recipe this pass, not four, because it closes a gap this KB declared at pass 25 and then
archived (`P483`).** 🔵 **It is also the first recipe on these shelves whose every link is permissive —
MIT · MIT · MIT · BSD-3 — so it is a product component rather than a side-car.**

### 🔴 `P490` — the `P` namespace carries both patterns and findings, and the live tree re-used 15 numbers the archive had already assigned

🔴 **Found while taking the ceiling for this pass's recipe, and it is `P481`'s warning already realised
at scale.** `P481` (pass 37) said a duplicate definition *"makes every prior citation of that number
ambiguous, retroactively."* 🔴 **That has happened to **15** numbers:**

| | Live tree (`compose/patterns.md`) | Archive (`archive/2026-10-06-pre-reset/compose-patterns.md`) |
|---|---|---|
| `P49` | *EMEA: the conformity-assessment pack for a high-risk education system* (pass 37) | 🔴 *Integridad de examen sin AI de vigilancia … **EMEA primero por Annex III*** (pass 25) |
| `P50` | *APAC: the on-premise multi-agent classroom* | 🔴 *Perfil de competencia por MCP* |
| `P51` | *North America: assistive grading …* | 🔴 *El conector MCP de Moodle …* |
| `P52` | *LATAM: institution-scale text understanding …* | 🔴 *La capa agéntica de biblioteca …* |

🔴 **The `P49` collision is the dangerous one, because both patterns are EMEA/Annex III.** `Gap 39`'s own
cross-reference reads *"Ver **P49**"* — written at pass 25, pointing at the **archived** exam-integrity
pattern. 🔴 **A reader of the live tree today finds a different `P49` that is also about EMEA conformity,
and nothing signals the mismatch.** 🔵 **That is the precise harm `P481` described: the citation
resolves *plausibly*, to the wrong thing.**

🔴 **The root cause is that one `P` sequence is being used for two kinds of object.** Measured across
the whole tree: **pattern headings** occupy `P1`–`P125`, `P131`, `P136`–`P144`, `P150`–`P152`,
`P179`–`P185`; **findings** occupy most of `P186`–`P482`. 🔴 **Only six numbers below `P490` are free
anywhere in the tree: `291`, `292`, `422`, `440`, `442`, `443`.** The namespace is effectively full.

> **`P490`.** Patterns and findings must not share a number sequence. The durable remedy is a **prefix
> split** — `F###` for findings, `P###` for patterns — applied tree-wide. 🔴 **This pass does **not**
> perform that migration**, and deliberately: renumbering retroactively would break every existing
> citation, which is the harm being fixed. 🔵 **The safe interim rule, used by this pass: take the
> ceiling across the *whole tree including `archive/`*, for pattern headings **and** finding
> definitions, and allocate from a number that is free in both.** This recipe is therefore **`P491`**,
> not `P53` — 🔴 **`P53` is an archived pattern** (*predictive flow with a human deciding*), and this
> pass's first draft cited it before measuring.

---

## P491 — The calibrated item bank: prove two exam variants are equivalent, permissively, on the client's own hardware

🟢 **Closes `Gap 39`** (declared pass 25, archived at the reset, recovered this pass as `P483`). 🔵
**Region: unplaced by construction — the chain is jurisdiction-neutral (`P474`); it is *driven* by
regulation per region, see `intel/market.md`.**

### The problem, in the client's words

> *"Our AI generates unlimited practice and exam variants, so students can't copy from each other."*

🔴 **Under a high-risk regime that sentence is a liability, not a feature.** If two students sat
different variants and nothing measured that the variants were **equally hard**, their scores are not
comparable — and comparability is what an assessment system is for. 🔵 **The EU AI Act asks for
accuracy and robustness evidence (Annex IV); "the model writes good questions" is not evidence.**

### Why this could not be built on these shelves until now

🟢 **The KB had the two ends and not the middle.** Item banking (`LongsightGroup/qti3`, MIT) and
certified delivery (`amp-up-io/qti3-item-player`, MIT) were shelved; **nothing could fit item
parameters.** 🔴 **`2PL` and `3PL` were named zero times across the whole KB before this pass** (`P484`). The gap was
declared at pass 25 and prescribed its own fix — *"calibrar con una librería IRT de Python"* — and that
library is what pass 38 found.

### The stack — every licence read from payload, 2026-10-07

| # | Role | Repo | Licence | Hit path · bytes |
|---|---|---|---|---|
| 1 | Author N parametric variants of one item → QTI 3 bank package | [`LongsightGroup/qti3`](https://github.com/LongsightGroup/qti3) | 🟢 **MIT** | `main/LICENSE.md` · 1,072 B |
| 2 | Deliver variants, capture responses | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** | `main/LICENSE` · 1,076 B |
| 3 | 🆕 Fit item parameters (1PL/2PL/4PL), hierarchical priors | [`nd-ball/py-irt`](https://github.com/nd-ball/py-irt) | 🟢 **MIT** | `master/LICENSE` · 1,121 B |
| 3b | 🆕 Alternative / cross-check estimator, GPU | [`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) | 🟢 **MIT** | `main/LICENSE.txt` · 1,073 B |
| 4 | 🆕 Adaptive selection from the calibrated bank | [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | 🟢 **BSD-3-Clause** | `main/LICENSE` · 1,514 B |
| 5 | 🆕 Synthetic response data for the test fixtures | [`eribean/girth`](https://github.com/eribean/girth) | 🟢 **MIT** | `master/LICENSE.txt` · 1,064 B |

🟢 **No copyleft anywhere.** 🔵 **Contrast with the rest of this KB's platform tiers** — Moodle (GPL),
Open edX (AGPL), proctoring (copyleft) — which must be side-cars. **This chain ships inside the
product.**

### Wiring

```
                 ┌─────────────────────────────────────────┐
  topic/blueprint│  any shelved generator (tutor/LLM)      │
  ───────────────▶│  writes N variants of item i            │
                 └───────────────┬─────────────────────────┘
                                 │  QTI 3 item package
                                 ▼
                 ┌─────────────────────────────────────────┐
                 │  LongsightGroup/qti3        (MIT)       │  1. bank
                 └───────────────┬─────────────────────────┘
                                 ▼
                 ┌─────────────────────────────────────────┐
                 │  amp-up-io/qti3-item-player (MIT)      │  2. deliver
                 └───────────────┬─────────────────────────┘
                                 │  response matrix  (student × item → 0/1)
                                 ▼
                 ┌─────────────────────────────────────────┐
                 │  nd-ball/py-irt             (MIT)      │  3. calibrate
                 │  2PL: per-item difficulty b, discrim a │
                 │  + posterior SE per parameter          │
                 └───────────────┬─────────────────────────┘
                                 │  item-parameter table
                 ┌───────────────┴─────────────┬───────────────────────┐
                 ▼                             ▼                       ▼
     EQUIVALENCE GATE                 douglasrizzo/catsim      Annex IV evidence
     |b_v1 − b_v2| ≤ τ  ?               (BSD-3) 4. adapt       pack (the artefact
     fail ⇒ variant rejected            selection + stop       the regulator reads)
```

### The gate that makes it a pattern rather than a pipeline

🟢 **The equivalence gate is the deliverable.** Everything upstream is conventional; **the gate is what
converts "we generate variants" into "our variants are measurably equivalent".**

| Step | Concretely |
|---|---|
| 1 | Pilot each variant family on a sample. 🔵 **Sample size is the real constraint** — a 2PL fit needs enough responses per item for the posterior to be narrow, and `py-irt` reports the SE that tells you whether it is |
| 2 | Fit **one** model over the whole family with `py-irt` (2PL, hierarchical priors) |
| 3 | 🔴 **Gate:** reject variant `v` if `|b_v − b_family|` exceeds a tolerance **τ fixed in advance and written down**. A τ chosen after seeing the results is not a gate |
| 4 | 🟢 **Cross-check with `irtorch`** on the same matrix. 🔵 **Two independent MIT estimators agreeing is the same two-channel discipline this KB applies to licences** (`p289`, `P482`) — and disagreement between them is a finding, not noise |
| 5 | Feed surviving items to `catsim` for adaptive delivery; 🟢 **`girth` generates synthetic responses so the gate has regression fixtures that need no student data** |
| 6 | 🟢 **Emit the item-parameter table + τ + SEs as the accuracy/robustness annex.** That table *is* the compliance artefact |

### Why this sells, per region

| Region | The driver |
|---|---|
| **EMEA** | 🔴 **Annex IV accuracy/robustness evidence** for a high-risk assessment system; 🟡 **deferred to 2027-12-02**, so calibrating now is free and retrofitting later is not |
| **North America** | 🟢 **Human-oversight rules** (Oklahoma, Maryland): the system produces a *measurement*, a human holds the *determination*. 🟢 **And it is fitted on response patterns, not student text — architecturally compatible with California AB 1159** |
| **APAC** | 🔴 **Binding now** (Korea Basic AI Act, H2 2026) at national testing volumes — `catsim` + a calibrated bank is the ministry-scale shape |
| **LATAM** | 🟢 **Robust to a pending statute.** Brazil's PL 2.338/2023 can still change; accuracy evidence is required under every risk-based draft, and the whole chain runs **on-premise** |

### What this pattern does **not** claim

- 🔴 **Nobody has published the equivalence study for an LLM-generated variant family on this stack.**
  🔵 **The second half of `Gap 39` is still open** — this recipe supplies the **instrument**, not the
  result. The measurement is a few weeks of pilot data, not research.
- 🔴 **`girth` (2021) and `pyirt` (2019) are stale** (`P260`). Use them as **fixture generators and
  reference**, not as the production estimator.
- 🔴 **No CAT *web platform* is cleanly usable** — `hicsail/opencat-pro` is MIT code with a **purchased
  UI framework** (`P486`). This pattern deliberately uses an **engine + the client's own UI**.
- ⚠️ **`irtorch`'s grant is MIT and its attribution is unresolved** (`P487`): the `LICENSE` names *"The
  Python Packaging Authority"* as holder while `pyproject.toml` names the actual author. 🔵 **Cite the
  author from `pyproject.toml` in any warranty or indemnity clause.**

### 🔵 Cross-cutting gate update — and one that still cannot run

🟢 **`P485` joins the licence-reliability checks**: when a dependency is reachable at two slugs, resolve
**both** payloads before pinning either, and pin the **slug**, never the project name. 🔴 **`catsim` is
the live example — the `datacamp` fork serves GPL-3.0 while declaring LGPLv3 in its own `setup.py`**, so
a careless pin inverts the licence of this entire recipe from BSD-3 to copyleft.

🔴 **Still blocked, second pass running:** `./discover_probe.sh --self-test` is denied by the session's
auto-mode classifier (`Code from External`), so the `P480` fixture debt stays open and the gate stays
honest at **9/9** with the GPL/AGPL specimens parked in `fixtures-pending/`. 🔵 **Closing it is one
command in a session without that restriction — see the operational note in `agents/top.md`.**

## 🟢 Thirty-seventh pass, 2026-10-07 — four recipes, one per region: P49, P50, P51, P52

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com` on
2026-10-07**, with the family **anchored to the payload's title block** (**`P171`**). No star counts
(`P479`), so these recipes are composed on **licence and documented capability**, never popularity.
⚠️ **No model-weights licence is verified anywhere here — `huggingface.co` is `000`.** ⚠️ **Every
regulatory date below is secondary-sourced and every source domain is blocked from this environment**
— re-verify against the Official Journal, each national gazette and each state's legislative record
before any of it enters a client deliverable.

🔴 **Step 0 of every recipe, and it changed this pass.** `compose/code/p473-probe-commercial-gate/` is
the shelf instrument every candidate repo must pass — **but it could not be executed in this
environment**, and its fixture set holds **no GPL-3.0 and no AGPL-3.0 specimen** while reporting 9/9
(**`P480`**) — the exact pair `P171` exists to protect.
🟢 **So step 0 is: run the gate where it *can* execute, and calibrate it against known-answer controls
that include both GPL variants before believing any `PROHIBIDO`.** The 8 controls used this pass are
tabulated in `agents/top.md`. 🔵 **A `PROHIBIDO` on a 34 KB payload is a GPL-family false positive
until the title block says otherwise.**

### 🔵 Why these four and not one

The four recipes are **not variants of one build**. Each is anchored to the binding that actually
drives its region's buying decision — 🔴 **statutory artefacts in EMEA, data residency in APAC, a
list of prohibited functions in North America, institutional governance in LATAM** — and each uses a
*different* permissive foundation because, per `T4`, there is only one per tier.

---

## P49 — EMEA: the conformity-assessment pack for a high-risk education system

**Problem it solves.** 🔴 **The EU AI Act's high-risk obligations for education became fully
applicable on 2 August 2026** — admission decisions, evaluation of learning outcomes and exam scoring
are all in scope — **and institutions are, by their own published assessments, still in
pre-compliance.** 🔵 **The client does not need a better grader. They need the technical file,
and the deadline is already behind them.**

🟢 **The deliverable is a set of artefacts, not a model**: risk-management record, data-governance
record, human-oversight design, transparency documentation, conformity assessment.

| Component | Licence (payload) | Role |
|---|---|---|
| [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **Apache-2.0** · 10,982 B | 🟢 **The LMS the compliance layer lives *inside*.** The only tier-1 LMS with no copyleft conversation — and Zurich-stewarded, which matters to an EMEA procurement |
| `compose/code/aiact-50-2-marking/` + `-spans/` + `-pack/` + `-exposure/` | in-tree | 🟢 **Already built: marking, span provenance, the XSD-validated pack, and the exposure scan.** This recipe wires them to a platform rather than writing them |
| [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | 🟢 **MIT** · 1,071 B | **Rubric intake.** Teacher-uploaded rubric → the human-oversight artefact names *whose* rubric governed each decision |
| [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT** | **The evaluation record.** A high-risk technical file needs reproducible accuracy evidence; this is a harness, not a vibe check |
| **Lemonade** / **Ollama** local inference | — | 🔴 **Data governance is far cheaper to evidence when the data does not move.** See `T3` |

**Wiring.** `OpenOLAT` assignment hook → rubric resolved through `grading_assistant`'s intake → marking
through the `aiact-50-2-marking` path, which emits **spans** tied to rubric clauses → `-pack` produces
the XSD-validated provenance envelope per decision → `-exposure` scans the deployment for unmarked
surfaces → the harness produces the accuracy appendix. 🔴 **The human-oversight gate is a hard commit
step, not a notification**: no score leaves the system without a named human action recorded against
the span set.

⏱️ **8–10 weeks.** 🟢 **What makes it sellable: every artefact is a document the institution must
produce anyway**, and it is repeatable across institutions in the same member state.

⚠️ **Re-verify the 2 Aug 2026 applicability date and the Annex III scope against the Official
Journal.** `eur-lex.europa.eu` is `000` from here and this KB has **never** read that text first-hand.

---

## P50 — APAC: the on-premise multi-agent classroom, with jurisdiction gates

**Problem it solves.** 🔴 **Four jurisdictions, four regimes, one product**: Korea's AI Basic Act (in
force January 2026) names **education high-impact**; Japan and Korea mandate **student-data
encryption with penalties**; China runs the region's most developed binding regime; India has **no
dedicated AI statute** at all. 🔵 **A single cloud deployment cannot satisfy this set, and a
per-country rebuild cannot be priced.**

| Component | Licence (payload) | Role |
|---|---|---|
| 🆕 [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** · 1,064 B | 🟢 **The product.** Multi-agent classroom — AI teachers **and AI classmates**, whiteboard, live discussion; one-click slides / quizzes / simulations / PBL from any document. **LangGraph 1.1** on Next.js 16 / React 19 |
| **Lemonade** (local inference) + **FunASR** (local ASR) | — | 🟢 **Already first-class in `OpenMAIC`, not bolted on.** The classroom — speech included — runs inside the institution |
| [`BaijayantaRoy/bandup`](https://github.com/BaijayantaRoy/bandup) | 🟢 **MIT** | **The assessment half, jurisdiction-bound**: Singapore PSLE composition /40 and A-Level GP /50 against each paper's own band descriptors. ⚠️ **bands explicitly unofficial** |
| [`dikshant182004/MathTutor`](https://github.com/dikshant182004/MathTutor) | 🟢 **MIT** | **The India/JEE reference architecture** — 14-node LangGraph, **a critic agent that verifies its own answers**, Redis episodic/semantic/procedural memory, BM25 + dense + RRF retrieval |
| **LangGraph policy nodes** | — | 🔴 **One graph, per-jurisdiction gates** |

**Wiring.** `OpenMAIC` is the delivery surface. 🟢 **Insert a policy node immediately before every
egress and every assessment write**, parameterised per market: **Korea** → high-impact disclosure
record + encryption-at-rest assertion; **Japan/Korea** → student-data encryption gate; **China** →
binding-regime checks; **India** → privacy/consumer-law baseline. Assessment routes to `bandup` for
Singapore instruments and follows `MathTutor`'s **critic-agent** pattern elsewhere, so a marked answer
is verified before a learner sees it. 🔴 **Local inference is the default path; a cloud model is an
explicit per-tenant opt-in that trips the disclosure node.**

⏱️ **12–14 weeks.** 🟢 **The leverage: the classroom and the local-inference path are MIT and already
written** — the build is the policy layer and the rubric encoding.

⚠️ **`OpenMAIC`'s learning-outcome claim rests on a `JCST'26` paper that is unreadable from here.** Sell
the architecture and the residency posture; do **not** quote an effect size for it.

---

## P51 — North America: assistive grading that is architecturally incapable of the prohibited actions

**Problem it solves.** 🔴 **The regulation names the forbidden functions explicitly, and "we trained
staff not to do that" is not an answer.** NYC Public Schools' March 2026 Traffic Light Framework puts
**grading, discipline, promotion/graduation decisions and behavioural surveillance** on a **Red —
never permitted** list; Oklahoma and Maryland require human oversight and bar AI from high-stakes
student decisions; **Maryland's AI Ready Schools Act** gives 24 districts 120 days to adopt aligned
policies; **California AB 1159** prohibits training models on student data.

🔵 **So the product requirement is a negative capability** — and the only credible way to demonstrate
a negative capability is architecture.

| Component | Licence (payload) | Role |
|---|---|---|
| [`rubelw/OSSS`](https://github.com/rubelw/OSSS) | 🟢 **Apache-2.0** · 11,362 B | 🟢 **The substrate, and it already models the right tenant**: districts as top-level, board governance, accounting, transportation. **FastAPI + Keycloak SSO + PostgreSQL**, with **Ollama + MetaGPT + A2A in-tree**. ⚠️ **workflow/state-machine logic self-declared unfinished — pilot tier, side-car the writes** |
| [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | 🟢 **MIT** · 1,071 B | 🟢 **Rubric-agnostic intake is the correct shape here** — the district brings its rubric, so no rubric is encoded in a vendor's repo |
| **Ollama** (in `OSSS`'s stated architecture) | — | 🔴 **`AB 1159` makes no-train non-negotiable.** On-premise inference is how you evidence it |
| `compose/code/aiact-50-2-pack/` | in-tree | **Decision provenance.** Built for EU marking; the envelope is jurisdiction-neutral and carries the audit trail |
| `compose/code/action-gap-crosscheck/` | in-tree | 🟢 **The Red-list gate** — crosscheck every emitted action against the prohibited set |

**Wiring.** `OSSS` holds roster, enrolment and grade state; 🔴 **the AI layer is a side-car with
read access and *no* write path to promotion, discipline or graduation fields** — the negative
capability is enforced by **database grants**, not by prompt instructions. Scoring produces a
**recommendation plus the provenance envelope**; a human commit step writes it. `action-gap-crosscheck`
runs as the egress gate. 🟢 **Policy is a parameter set, one per district**, because 24 districts on
independent 120-day clocks is 24 policies, not one deployment.

⏱️ **8–10 weeks** for the first district, **~1–2 weeks** per district thereafter. 🟢 **The artefact
that wins the review: a schema-level demonstration that the Red-list fields are unreachable from the
AI service's credentials.**

---

## P52 — LATAM: institution-scale text understanding, offline-capable, with the governance pack

**Problem it solves.** 🔴 **79% of LATAM faculty use AI in teaching; fewer than 10% of institutions
have formal guidelines.** 🔵 **That gap is not a tooling gap, and the three named production
deployments in the region show what actually sells — none of them is student-facing tutoring:**
Lottus Education (Mexico) `LucIA` processes **90,000 students' feedback across 45 campuses in 15
minutes** against nearly two months manually; PUC-PR (Brazil) `AvalIA` classifies **270,000+ student
comments**; Universidad Panamericana (Mexico) `SyllabUP` validates **curricular programmes and
accreditation evidence** on an agent architecture.

🟢 **So build institution-scale text understanding plus the governance artefacts, delivered to run
where connectivity is intermittent.**

| Component | Licence (payload) | Role |
|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · 1,096 B | 🟢 **The only platform on these shelves that assumes intermittent connectivity as the normal case**, and permissive enough to ship the AI layer **inside** the product |
| [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT** | 🟢 **Portuguese evaluation, from CEIA / Federal University of Goiás.** Direct-response eval, chat-template autodetect, **vLLM + LiteLLM on one harness** — the accuracy evidence a Brazilian institution's governance document needs |
| [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | 🟢 **MIT** | 🔵 **The method, portable to any ministry curriculum**: rule-based parsing with **LLMs confined to the cleaning step** — the auditable division of labour, and why its output is trustworthy enough to build on |
| **Ollama / vLLM** local inference | — | 🔴 **With <10% of institutions holding guidelines, "the data never leaves" is the policy** — delivered as architecture instead of paperwork |
| `compose/code/aiact-50-2-pack/` | in-tree | **Provenance envelope**, reusable under **Brazil's PL 2.338/2023** risk-based transparency duties |

**Wiring.** Ministry or institutional curriculum → the **MBSSE parser pattern** (rules parse,
LLM cleans only) → structured curriculum as the retrieval spine. Feedback, course comments and syllabus
documents are classified at institution scale — the `LucIA` / `AvalIA` / `SyllabUP` shape — with every
classification emitting a provenance envelope. `Kolibri` carries delivery to low-connectivity sites;
the Portuguese harness produces the accuracy appendix. 🟢 **Ship the institution's AI-use guideline as
a deliverable of the engagement**, generated from the provenance records rather than written from
scratch — 🔵 **which converts the region's governance gap from an objection into the first invoice.**

⏱️ **6–8 weeks.** ⚠️ **Spanish-language evaluation has no equivalent to the Portuguese harness on
these shelves** — 🔴 **an explicit gap: a Mexico or Colombia engagement has no verified Spanish
evaluation asset here, and that should be scoped as build, not reuse.**

## 🟢 Thirty-sixth pass, 2026-10-07 — two recipes: P47, P48 — plus one new instrument

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com` on
2026-10-07**, branch- and case-aware, **and re-classified through `compose/code/lib/license_family.sh`**,
which is also what the new instrument does. No star counts (`api.github.com` **403**), so these recipes
are composed on **licence and documented capability**, not popularity. ⚠️ **No model-weights licence is
verified anywhere here — `huggingface.co` is 000.** ⚠️ **Every regulatory date is secondary-sourced and
every source domain is blocked from this environment** — re-verify against the Official Journal, each
national gazette and each state's legislative record before it enters a client deliverable.

### 🆕 New instrument — `compose/code/p473-probe-commercial-gate/` (**9/9**)

The discovery probe a pass runs **instead of writing a fresh sweep**. It emits `P250`'s **commercial-use
column** from the shared classifier, so a `CC BY-NC` payload cannot be written up as `GRANTED`
(`P473`), and it folds in `P475` by giving the existence check the same case-variation the licence check
gets. Fixtures are **real payloads**, including the 822-byte `CC-BY-NC-4.0` specimen that caused it and
the 11,120-byte **`ECL-2.0`** Sakai payload that a search summary called *"Apache 2.0"* (`P476`).
🔵 **Use it in step 0 of both recipes below** — every repo entering a client build passes through it first.

---

## P47 — A jurisdiction-bound marking service that never ships the student's work off-site

**Problem it solves.** A client does not buy "essay marking"; they buy *"marked against **our** rubric,
for **our** exam, without children's writing leaving **our** infrastructure."* 🔴 **Three constraints that
are usually treated as a compliance tax, and all three are architectural:** the rubric is the client's
and cannot be handed to a vendor, the data boundary is per-step rather than per-app, and somebody must be
able to show that the marking is pedagogically sound rather than merely fluent.

🟢 **Every component below is payload-verified permissive and already exists.** The build is the rubric
layer and the wiring — nothing here requires training a model.

| Component | Licence (payload) | Role |
|---|---|---|
| [`BaijayantaRoy/bandup`](https://github.com/BaijayantaRoy/bandup) | 🟢 **MIT**, 1,071 B | **The reference implementation and the starting fork.** Already marks named Singapore papers (**PSLE composition /40 = Content 20 + Language 20; A-Level GP /50 = Content 30 + Language 20**) against each paper's own band descriptors. Ships what is tedious to rebuild: **handwriting/OCR intake** (phone photos, scans, multi-page PDF, transcribed verbatim with mistakes preserved), **tracked-changes word-level diff**, per-error explanation with error-type breakdown, **next-band rewrite from the pupil's own words** |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT**, 1,064 B (payload, re-read this pass) | **The quality gate — the licensed one.** Pedagogical knowledge measured against teacher-qualification-exam questions. 🔵 **This is the shippable component; see the row below for the one that is not** |
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | 🔴 **NO LICENCE PAYLOAD** — probed again this pass, 19 filenames × 2 branches: `UNGRANTED` | ⚠️ **Specification only, never a dependency.** Its **four dimensions — Mistake Identification, Mistake Location, Providing Guidance, Actionability** — are published in its EACL 2026 demo paper and a rubric is an idea, not code. 🔴 **The paper says MIT; the repository does not. Do not vendor it** (`P478`) |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause**, 2,058 B | **Item-bank I/O without a vendor.** QTI 2.1 delivery engine + **JQTI+** for programmatic read/write/manipulate of QTI items and tests. Univ. of Edinburgh |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) **or** [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **Apache-2.0** (10,982 B) / 🟢 **ECL-2.0** (11,120 B) | **The system of record, extended in-tree.** Both are permissive, so the marking service is a **module**, not a side-car. 🔴 **Sakai is `ECL-2.0`, not Apache-2.0 — the patent grant in §3 differs and a legal review will ask (`P476`)** |
| Ollama | — | Local inference. **Two separately configured models**, per `bandup`'s own design: an **OCR/vision** model and a **marking** model |

**Wiring.**

1. **Gate every dependency** through `p473-probe-commercial-gate` (**9/9**). 🔴 **On a marking product this
   is not ceremony: the rubric descriptors, exemplar scripts and item banks you ingest are *content*, and
   content is where `CC BY-NC` lives.** An NC-licensed exemplar corpus inside a commercial deliverable is
   the failure this gate exists to prevent.
2. **Fork `bandup` and replace the rubric layer, not the pipeline.** Its papers are defined as band
   descriptors + mark allocation + word-count norms; a new jurisdiction is a new descriptor set. 🔵 **Keep
   its `/40` and `/50` structures as worked examples of what a descriptor set has to specify.**
3. **Set the data boundary per step, not per application.** Keep **OCR local always** — raw handwriting is
   the most sensitive artefact in the system and the step least improved by a frontier model. Let the
   *marking* model be configurable. 🟢 **Preserve `bandup`'s persistent on-screen warning when a non-local
   model is selected**; it is a one-line UI element that makes the data boundary visible to the teacher,
   and it is the thing an auditor asks to see.
4. **Put a pedagogical quality gate in CI, not in the demo — and build it, because you cannot buy it.**
   🔴 **This KB's standing gap "no shippable permissive evaluator of tutoring quality" is STILL OPEN and
   the reason is structural: the whole pedagogy-evaluation subfield is unlicensed.** `AITutor-EvalKit`
   (EACL 2026) claims MIT *in its paper* and serves **no `LICENSE` payload**; `eth-lre/mathtutorbench`
   contradicts itself inside one README; `UnifyingAITutorEvaluation` states nothing; Open TutorAI is
   **CC BY-NC-SA 4.0**. 🟢 **So: take the four dimensions from the published paper as a *specification*
   — Mistake Identification, Mistake Location, Providing Guidance, Actionability — and implement them
   over MIT-licensed `pedagogy-benchmark`.** A scoring rubric described in a paper is not copyrightable
   as code; the repository you must not vendor is. Hold a set of pre-marked scripts and **fail the build
   on regression in Mistake Location and Actionability** — those two degrade first and are the two a
   teacher notices. 🔵 **This converts "the AI seems good" into a number that moves when you change
   something**, and the implementation is ~2 of the 11 weeks below, which is why it is budgeted.
5. **Exchange items and results as QTI 2.1 via `qtiworks`/JQTI+**, and write grades back through the
   LMS's own gradebook. On `OpenOLAT` or Sakai this is an in-tree module; on Moodle (GPL-3.0+) or Open edX
   (AGPL-3.0) the **same service** runs as a side-car over LTI 1.3 — 🔵 **the licence of the LMS decides the
   deployment topology and nothing else about this build.**
6. **Ship the disclaimer as a product feature.** `bandup` states its bands are **unofficial**; keep that.
   🔴 **In Oklahoma- and Maryland-pattern jurisdictions, AI is barred from high-stakes decisions about
   students, so "advisory, teacher-confirmed" is the only lawful posture** — and the tracked-changes diff
   plus per-error explanations are what make the teacher's confirmation a real review rather than a
   rubber stamp.

**Where it sells, and why the regions differ.**

- 🟢 **North America** — **Ohio HB 96's deadline passed 1 July 2026**, so districts hold board-adopted AI
  policies *today* and their tooling does not comply. 🔵 **The opening is an audit against *this district's*
  policy text**, because the statute does not prescribe content and the policies differ. California
  **AB 1159**'s bar on training models with student data makes step 3 a **compliance feature**.
- 🟢 **APAC** — Korea's AI Basic Act (**in force 22 Jan 2026**, education = high-impact) and Vietnam's Law
  on AI (**1 Mar 2026**, naming **automated assessment** explicitly). 🔴 **A marking deliverable is in scope
  today**, and steps 4 and 6 are how you evidence oversight.
- 🟢 **EMEA** — the **2 Dec 2027** deferral makes this a design window rather than a remediation. Article 50
  transparency still applies from Aug 2026. Both permissive LMS options are EMEA-origin.
- 🟡 **LATAM** — run **P48's step 1 first**: at 26% of institutions holding a formal AI strategy, a marking
  service lands without a policy to land in.

⏱️ **8–11 weeks** for one jurisdiction's paper set: 1 week gating and rubric extraction, 3–4 rubric layer,
2 eval harness in CI, 2–3 LMS integration and write-back, 1 pilot. **Each additional paper: ~2 weeks**,
because the pipeline is already there.

---

## P48 — Measure the model before building the tutor: a national curriculum as grounded retrieval

**Problem it solves.** The usual order is backwards. A tutor gets built on whichever model the vendor
demonstrated, then someone asks whether it is any good in the language of instruction and against the
national curriculum — and there is no instrument to answer with. 🔴 **In a non-English, low-resource or
Global-South engagement, model choice is the single highest-variance decision and the one made with the
least evidence.** Two artefacts verified this pass invert that order.

| Component | Licence (payload) | Role |
|---|---|---|
| [`eduagarcia/lm-evaluation-harness-pt`](https://github.com/eduagarcia/lm-evaluation-harness-pt) | 🟢 **MIT**, 1,067 B | **Step 1, and the step that is usually skipped.** The evaluation suite behind the Open Portuguese LLM Leaderboard (**CEIA / Federal University of Goiás, Brazil**). Portuguese task suite; **direct-response** evaluation so instruction-tuned chat models are measurable at all; chat-template autodetection; **vLLM *and* LiteLLM backends, so a local open-weight model and a hosted API are scored on one harness**; F1-macro and Pearson aligned to each benchmark's own metric |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 already shelved | **Measures pedagogical knowledge, not language fluency** — questions drawn from teacher-qualification exams. 🔵 **Orthogonal to the harness above and both are needed: fluent and pedagogically wrong is the common failure** |
| [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | 🟢 **MIT**, 1,065 B | **The grounding corpus and the template for building another.** Sierra Leone **MBSSE** Maths + Language Arts lesson plans, all grades Primary/JSS/SSS, PDF → structured JSON → cleaned. **Ships the corpus itself**, so step 2 starts with data rather than a scraper |
| [`dikshant182004/MathTutor`](https://github.com/dikshant182004/MathTutor) | 🟢 **MIT**, 1,068 B | **The architecture to copy, not the product to deploy.** 14-node LangGraph: intent routing → ReAct tool loop → **a critic agent that verifies the answer before it is shown** → explanation. **Episodic + semantic + procedural memory in Redis**; hybrid **BM25 + dense + reciprocal rank fusion**; SymPy for symbolic checking. ⚠️ README at **`master/Readme.md`** (`P475`) |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT**, 1,097 B (re-read this pass) | **Offline-first delivery.** The tier where this recipe is most needed is the tier with the least connectivity |

**Wiring.**

1. **Score candidate models *first*, on two axes, before any tutor code exists.** Run
   `lm-evaluation-harness-pt` (or the same harness pattern retargeted to the language of instruction) for
   **language competence**, and `pedagogy-benchmark` for **pedagogical knowledge**. 🟢 **Use the vLLM and
   LiteLLM backends to put a self-hostable open-weight model and a frontier API on one scoreboard** — that
   comparison is the deliverable, and it decides deployment topology, cost and data residency in one
   measurement. ⚠️ **Model *weights* licences are unverifiable from this environment (`huggingface.co`
   000)** — gate them separately before shipping.
2. **Turn the national curriculum into structured JSON** following `lesson-plan-parse-mbsse`: **rule-based
   parsing, LLMs confined to the cleaning pass.** 🔵 **That division is why the output is trustworthy enough
   to ground on** — a fully LLM-driven parse produces a corpus whose errors you cannot find later. Ships
   as a reusable asset the ministry can keep.
3. **Ground retrieval on that corpus with `MathTutor`'s hybrid pattern** — BM25 for curriculum
   terminology, dense for paraphrase, **reciprocal rank fusion** to combine. 🔵 **Curriculum documents are
   exactly the case where lexical retrieval beats dense** (grade codes, syllabus references, prescribed
   terms), which is why the hybrid matters here more than in open-domain RAG.
4. **Copy the critic node.** `MathTutor` verifies its own answer with a dedicated agent before showing it,
   with SymPy for symbolic steps. 🔴 **This is the cheapest available mitigation for the failure that
   destroys trust fastest — a confident wrong answer to a child** — and it is a graph node, not a research
   project.
5. **Carry memory, but carry the *right* memory.** Redis episodic + semantic + procedural, tracking which
   topics a learner struggles with and which strategies work for them. 🔵 **An earlier shelf find
   (`Gnos`) names the distinction that makes this meaningful: "saw the explanation" / "solved with help" /
   "solved alone". Without it, "mastery" is unmeasured.**
6. **Deliver through `Kolibri`** where connectivity is intermittent, and re-run step 1 as a **regression
   gate** whenever the model changes — the scoreboard from step 1 is a CI artefact, not a one-off slide.

**Where it sells.**

- 🟢 **EMEA, low-resource tier** — `lesson-plan-parse-mbsse` is **already Sierra Leone**, and the template
  repeats against any ministry publishing lesson plans as PDF, which is most of them. Fits the
  capacity-building posture of **Egypt, Morocco, Jordan** and the national-programme posture of
  **Saudi Arabia, UAE, Qatar**. 🔵 **The Rwanda–Anthropic MoU (Feb 2026, health/education/public sector)
  is the shape of counterparty to expect** — ⚠️ secondary, single-sourced.
- 🟢 **LATAM** — `lm-evaluation-harness-pt` is **Brazilian and Portuguese-native**, and the
  **87% using / 26% with a strategy** pair means step 1's scoreboard is *also* the evidence base for the
  institution's first AI policy. 🔵 **Sell the measurement as governance, then the tutor.** Plan
  **build-and-transfer with documented handover** — the regional talent gap has widened since 2022.
- 🟢 **APAC** — India's JEE is `MathTutor`'s native target, so step 3–5 are closest to as-built there.
- 🟡 **North America** — step 1's local-vs-API scoreboard is the direct answer to **AB 1159**-pattern
  prohibitions on training with student data.

⏱️ **10–13 weeks**: 2 weeks model scoring (step 1 — **do not compress this one**), 3 curriculum parsing,
3 grounded retrieval + critic, 2 memory and mastery instrumentation, 2 offline delivery and CI gating.

## 🟢 Thirty-fifth pass, 2026-10-07 — two recipes: P45, P46

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com` on
2026-10-07** with the branch- and case-aware probe (12–19 filenames × `main` **and** `master`), **and
cross-checked against the registry or build descriptor it publishes** where one exists. No star
counts (`api.github.com` **403**), so these recipes are composed on **licence and documented
capability**, not popularity. ⚠️ **No model-weights licence is verified anywhere here —
`huggingface.co` is 000.** ⚠️ **Every regulatory date in `P46` is secondary-sourced — `eur-lex` is
000 — and must be re-verified against the Official Journal and each national gazette before it
enters a client deliverable.**

## P45 — Make a declared gap fail the build, in whatever language it was written

**Problem it solves.** This KB spent three passes telling readers that **no EMEA-origin permissive
education foundation exists**, while holding an **Apache-2.0 Swiss LMS** and a **BSD-3-Clause
Edinburgh assessment engine** on its own shelves (`P469`). 🔴 **The instrument that should have
caught it already existed and was already correct.** `p370-gap-gate/` was built for exactly this,
passes **27/27**, and reported **0 CONTRADICHOS** — because the KB had shifted from writing its gap
claims in Spanish to writing them in English, and **two independent filters in the gate are
Spanish-only** (`P471`).

🔵 **This is the recipe worth taking to a client, because the shape is completely general: an
absence has no payload to re-read, so nothing contradicts it except your own corpus — and the
checker that compares them has to be able to *parse* the claim.**

| Component | Role |
|---|---|
| `compose/code/p370-gap-gate/` — `gap_gate.py` | **The gate.** Classifies a declared gap's **scope** (`INDICE` vs `CANAL`), resolves the region against the closed five-value vocabulary, and searches the corpus for repo rows that **place** an asset in that region |
| 🆕 `compose/code/p471-gap-gate-language/` — `gap_language.py` | **The coverage meter and the speech-act classifier.** Reports, per gap sentence, whether the gate can scope it **as shipped** and **with English markers** (`language_blind = True` is the untested class); ships `MARKERS_EN` as the patch; and provides `assertion_class()` → `QUOTED` / `QUALIFIED` / `ASSERTED` plus `build_verdict()`, which is what step 4–5 below actually call. **25/25** |
| `compose/code/lib/region.py` | The closed vocabulary. 🔴 **Not reimplemented** (`P237`) — and note the gate deliberately does **not** use its strict cell detector on repo rows, because this KB's region cells mix region with attribution and strict mode would reject them as residue, making the gate sustain a false gap by false negative |
| Any CI runner | `python3 gap_language.py --self-test` → **16/16** (nesting the gate's **27/27**); `--coverage <root>` in the pre-commit path |

**Wiring.**

1. **Extract** candidate sentences with **both** patterns — `GAP_SENTENCE` (Spanish) and
   `GAP_SENTENCE_EN` (English). 🔴 **Either alone loses half the corpus**; the `P467` sentence is
   invisible to the first.
2. **Scope** each one. An **index** gap (*"no EMEA-origin permissive education foundation"*) is a
   claim about the corpus and **is** refutable by its rows. A **channel** gap (*"…through the forges
   this environment can reach"*) is a claim about the **query** and is **not**. 🔵 **The channel
   marker must win when a sentence carries both** — the narrower scope is the one that was actually
   evidenced.
3. **Refute** index claims against placed rows. Measured on this tree: the `P467` sentence →
   **CONTRADICHO, 94 rows, 77 placed**.
4. **Classify the speech act before failing anything** (`assertion_class`). 🔴 **This step is not
   optional and this pass proved it: with it omitted, the gate fails the build 11 times on this tree
   and 0 of the 11 are real** — **9** are **quotations** and **2** are narrowed by a **maturity
   qualifier**. 🔵 **The correct way to retract a false gap is to quote it in the retraction**, so a
   detector without this step **punishes the fix** and trains people to fix things silently. And
   *"no LATAM-origin permissive product **at production maturity**"* is a claim about **maturity**:
   placed rows prove assets exist and say nothing about whether any is production-grade, so the gate
   must not refute a claim quantified on a dimension it never measured. **Quotation wins over
   qualifier** — a retraction quoting a qualified claim is still a retraction.
5. **Fail the build only on `INDICE` + `CONTRADICHO` + `ASSERTED`** (`build_verdict`). Pass
   `SOSTENIDO`. 🔴 **Report `language_blind` separately and loudly** — it is neither a pass nor a
   fail, it is *"this gate cannot read this claim."*
6. **Print the denominator.** 29 → 5 candidate sentences was the only visible symptom of the decay,
   and nothing surfaced it.

**The design rule this pass paid for.** 🔴 **`NO-CLAIM` must not be the same verdict as
"unparseable."** The gate returned, for a claim it could not read, the identical verdict it returns
for prose that is not a claim at all — so the sweep read as *"nothing to judge."* 🔵 **Any
classifier gets a third outcome: pass, fail, and *I could not parse this*.** A passing suite
measures the cases you wrote, never the class you stopped writing.

**Where it pays outside this KB.** Any corpus where a team asserts absence — *"no supported driver
for X"*, *"no customer in segment Y"*, *"no library does Z"* — and where the corpus is bilingual or
changed language, tooling, or template at some point. 🔵 **The bug is never in the assertion; it is
in the checker's reach, and the checker reports health.**

**Effort.** 1–2 weeks to port onto a client corpus, assuming their index has structured rows.
🔴 **Non-negotiable precondition:** the corpus must *place* assets in a **closed** region vocabulary.
Against free prose ("Brazil", "Europe", "Latam") step 3 has nothing to compare and the gate degrades
to a word counter — which is this KB's `P135`/`P368` lesson, already paid for.

## P46 — Jurisdiction-pinned assessment: one pipeline, four regulatory clocks

**Problem it solves.** A grading, placement or proctoring deliverable is **high-risk or high-impact
AI in every major jurisdiction**, and as of 2026 the clocks have **diverged**: the EU moved education
Annex III obligations to **2 Dec 2027**, while **Korea (22 Jan 2026)** and **Vietnam (1 Mar 2026)**
are **already in force**, with Vietnam naming **automated assessment** and **behavioural monitoring**
explicitly. 🔴 **The failure mode is reading the EU deferral as global relief.** A single
"compliant" pipeline is now wrong in at least two directions at once.

**The architecture: one assessment core, a policy layer that is pinned per jurisdiction.**

| Component | Licence (payload-verified) | Role |
|---|---|---|
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | 🟢 **BSD-3-Clause** (`master/LICENSE.txt`, 2,058 B) | **The assessment core.** QTI 2.1 delivery + rendering; **JQTI+** to read, write, model and manipulate items and tests programmatically; MathAssess for maths. 🔵 **Permissive, so the policy layer can be compiled in rather than bolted on** |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** (`master/LICENSE`, 10,982 B; `pom.xml` `<licenses>`; second forge on `gitlab.com`) | **The platform, extended IN-TREE.** The only complete LMS on these shelves that permits this — Moodle GPL, Open edX AGPL, Chamilo GPL, ILIAS GPL all force a side-car. 🟢 **EMEA-origin** (Zurich → frentix), which matters for an EU data-residency bid |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | MIT | **The policy graph.** One node per jurisdiction gate; the graph is the auditable artefact — `P46`'s whole point is that the policy is a **data structure**, not scattered `if` statements |
| [`ollama/ollama`](https://github.com/ollama/ollama) or [`vllm-project/vllm`](https://github.com/vllm-project/vllm) | MIT / Apache-2.0 | **Local inference.** 🔵 Required, not preferred, where **California AB 1159** bars training on student data and EU/APAC residency rules bite. ⚠️ **The engine licence is verified; no model weight licence is** |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`openfun/ralph`](https://github.com/openfun/ralph) | Apache-2.0 / MIT | **xAPI learning-record store.** The **post-market monitoring** evidence every one of these statutes demands |
| [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) | 🟡 **AGPL-3.0** (PyPI declaration) | ⚠️ **Side-car only.** Network copyleft — reachable over HTTP, never linked into an Apache/BSD tree |

**The policy layer, as four pinned configurations.**

| Jurisdiction | Binding date | What the gate must enforce |
|---|---|---|
| 🇪🇺 **EU** | **2 Dec 2027** (Annex III) — **but Article 50 transparency from Aug 2026** | Risk-management file, data governance, technical documentation, **human oversight**, post-market monitoring. 🔵 **Ship the Article 50 disclosure now**; build the rest against the 2027 date |
| 🇰🇷 **Korea** | 🔴 **in force 22 Jan 2026** | Education = **"high-impact"**. Obligations apply **today** |
| 🇻🇳 **Vietnam** | 🔴 **in force 1 Mar 2026** | Education high-risk, **automated assessment and behavioural monitoring named**. 🔴 **This is the clause that catches proctoring directly** |
| 🇺🇸 **US states** | **Ohio: 1 July 2026** | District-level AI policy mandatory; **AB 1159** — no student data in training; **OK/MD** — human oversight, **no AI in high-stakes student decisions**; **134 bills / 31 states** in flight |

**Wiring, in order.**

1. **Pin the jurisdiction at the top of the request**, from the tenant, not from a locale header.
   Every downstream node reads it. 🔴 **A deployment with no pin defaults to the *strictest* profile**
   — the only safe default, since the cost of over-complying is latency and the cost of
   under-complying is the engagement.
2. **Core scores against the rubric** (`qtiworks` + JQTI+), emitting the item, the rubric version and
   the model version.
3. **Human-oversight node is non-bypassable where required** (EU, OK, MD, Korea, Vietnam). It is a
   **queue with an override and a reason field**, not a confirmation dialog. 🔵 **Oklahoma and
   Maryland bar AI from high-stakes student decisions outright** — so for those, the model output is
   advisory input to a human decision, and the data model has to say so.
4. **Residency node** chooses inference: local (Ollama/vLLM) wherever training-on-student-data is
   barred or residency is required; vendor API only where the pin permits.
5. **Every step writes xAPI to the LRS.** 🔵 **This is the single component that serves all four
   jurisdictions at once** — post-market monitoring, the audit trail Ohio district policies ask for,
   and the evidence base for an EU technical file.
6. **Emit the conformity pack per pin.** Same core, four document sets.

**Effort.** 10–14 weeks for the core plus two jurisdictions; **+2–3 weeks per additional
jurisdiction**, which is the number to quote — the marginal cost is a policy profile and a document
set, not a rebuild. 🔵 **That marginal cost *is* the sales argument**, and it is only true because
the core is BSD/Apache and the policy lives in a graph.

⚠️ **Two honest limits.** The team this needs is **Java/Maven** (OpenOLAT, JQTI+), not the Python
most of this KB's agent rows assume. And **every date above is secondary-sourced**: `eur-lex` is
**000** from this environment, so the EU dates in particular carry a re-verification obligation
before they go in front of a client.

## 🟢 Thirty-fourth pass, 2026-10-07 — two recipes: P43, P44

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com` on
2026-10-07** with the branch- and case-aware probe, **and cross-checked against the registry it
publishes to** (see `agents/top.md` for the 20-channel census). No star counts (`api.github.com`
**403**), so these recipes are composed on **licence and documented capability**, not popularity.
⚠️ **No model-weights licence below is verified — `huggingface.co` is 000.**

## P43 — The two-channel licence gate: make a disagreement fail the build

**Problem it solves.** Every engagement eventually ships a dependency manifest to a client's legal
team, and the question is always the same: *how do you know?* Pass 32 established that *"we read the
`LICENSE` file"* is no longer a sufficient answer — a file with that name can contain bespoke terms,
a web-server notice or Creative Commons text. This KB has used both payload and registry channels for
several passes; **what it has not had is one written-down gate with an explicit disagreement rule**,
which is what `P465` made obvious was missing. This is that gate.

**Why two channels.** Payload is evidence that a *document* exists and says certain words. A registry
classifier is the publisher's own **machine-readable assertion** about what the licence *is*. They
fail differently, and the gate's value is in the disagreement rule, not in either channel alone.

| Repos and endpoints | Role |
|---|---|
| `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file}` | **Channel A — payload.** 13 filenames (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `MIT-LICENSE`, `UNLICENSE`, …) × `main` **and** `master`. 🔴 **Both branches are mandatory**: `ucfopen/canvasapi`, `dmitry-viskov/pylti1.3` and `ucbds-infra/otter-grader` are all **`master`-only**, and a `main`-only probe reports them as ungranted. |
| `https://pypi.org/pypi/{pkg}/json` → `info.license_expression`, `info.license`, `classifiers[]` | **Channel B — Python.** Prefer `license_expression` (SPDX), then the OSI classifier, then free text. |
| `https://registry.npmjs.org/{pkg}` → `versions[dist-tags.latest].license` | **Channel B — Node.** Verified: `ltijs` → Apache-2.0 at v7.0.7. |
| `https://packagist.org/packages/{vendor}/{pkg}.json` → `package.versions[latest].license[]` | **Channel B — PHP.** Verified: `moodle/moodle` → `GPL-3.0-or-later`. |
| `https://repo1.maven.org/maven2/...` | **Channel B — JVM.** Reachable (200); use for Sakai / OpenOLAT / Opencast. |

**The decision table — this is the part worth copying.**

| Channel A | Channel B | Verdict | Build action |
|---|---|---|---|
| permissive | same, OSI classifier | 🟢 **verified permissive** | pass |
| permissive | **`Other/Proprietary`** | 🔴 **reject** | **fail the build** — this is the `open-webui` case |
| permissive | silent (no metadata) | 🟡 **single-source** | pass **with the row flagged "payload only"** — the `crewai` and Chamilo case |
| copyleft | same | 🟡 **verified copyleft** | pass **only** on the side-car path; fail if the manifest is the embedded deliverable |
| **no payload found** | any | 🔴 **no grant** | **fail** — 7 of 15 candidates this pass |
| permissive | **different licence** | 🔴 **disagreement** | **fail and escalate to a human.** 0 of 10 this pass — and finding zero is what makes a non-zero meaningful |

**Two checks that are not about licences and belong in the same gate.**

1. 🔴 **Resolvability.** Issue a request for every pinned artefact URL, not just the manifest. A
   dependency can be licence-clean and still unobtainable: `soumics/adaptive-ai-tutor` pins its MIT
   RAG core as `github.com/.../archive/<sha>.zip`, which is **403** from this environment. Licence-
   resolvable ≠ install-resolvable (`P466`).
2. 🔴 **Manifest emptiness.** A 200 on `requirements.txt` is evidence the file exists, never that it
   declares anything — Kolibri serves one that is deliberately empty and a `pyproject.toml` with
   `dependencies = []`, while the real set is in PEP 735 `[dependency-groups]`. **An empty answer must
   raise, not return zero.**

**Wiring.** Run it as a CI job over the lockfile on every dependency change, emit one TSV row per
package (`package · channel-A verdict · channel-B verdict · agreement · source URLs`), and **archive
the TSV with the release** — that artefact, not an assertion, is what goes to the client's legal
team. This KB's own `compose/code/dependency-licence-closure/` is the natural home for it.

**Effort:** 1–2 weeks to build and wire, then effectively free. **Sell it inside** `P4`, `P13` and
`P38`, where "prove it" is already the deliverable.

## P44 — The all-permissive Canvas grading path: MIT end to end, on the client's own hardware

**Problem it solves.** Canvas is **AGPL-3.0**. North American statutes now require that **student
data not train models** (California AB 1159) and that **a human make high-stakes decisions**
(Oklahoma, Maryland); EU Annex III requires documented **human oversight** and transparency for
assessment. The usual answer — an SaaS grading product — fails the first requirement and cannot
evidence the second. This recipe builds the whole path from permissively licensed parts that run on
infrastructure the institution owns, **without inheriting Canvas's AGPL**.

🔵 **This is the Python counterpart to `P39`.** `P39` pins one of six MIT **MCP servers** for the
gradebook write path. `P44` is for the engagement where the deliverable is a service rather than an
agent tool, and nobody wants a third-party MCP server in the trust boundary.

**The stack — every licence read from payload and confirmed in a registry this pass:**

| Layer | Component | Licence | Verified |
|---|---|---|---|
| LTI 1.3 launch | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** | payload 1,070 B + PyPI `pylti1p3` MIT. 🔴 **Install name is `pylti1p3`, not `pylti1.3`.** ⚠️ Last push 2024-08-18 — stable, not actively developed. |
| Canvas read/write | [`ucfopen/canvasapi`](https://github.com/ucfopen/canvasapi) | 🟢 **MIT** | payload 1,130 B (`master`) + PyPI OSI MIT classifier |
| Grading core | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) **or** [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** both | payload + PyPI OSI BSD classifier |
| Submission ingestion | [`docling`](https://pypi.org/project/docling/) | 🟢 **MIT** | PyPI |
| Model access | `litellm` | 🟢 **MIT** | PyPI |
| Local inference | **Ollama** (dev) / **vLLM** (prod, Apache-2.0) | 🟢 permissive | PyPI `vllm` Apache-2.0 |
| Rubric vocabulary (optional) | [`promptster-ai/rubric`](https://github.com/promptster-ai/rubric) | 🟢 **MIT** | ⚠️ anchors only — **scoring weights are deliberately not published** |

🟢 **No AGPL anywhere in the deliverable.** Canvas stays AGPL on the institution's own servers; every
line Globant writes sits outside its tree and speaks HTTP.

**The flow, and where the statute is satisfied:**

1. **Launch.** Instructor opens the tool from a Canvas assignment; `pylti1p3` validates the LTI 1.3
   launch and yields the course, assignment and instructor identity. *No student data has moved yet.*
2. **Fetch.** `canvasapi` pulls the submissions for that assignment only. 🔵 **Scope the API token to
   the course** — the boundary is enforced by the token, not by application logic.
3. **Normalise.** `docling` converts PDF/DOCX submissions to structured text.
4. **Score.** The rubric is **data, not a prompt** (the `P38` rule). `otter-grader` or `nbgrader`
   handles anything executable; the model, reached through `litellm` against **Ollama or vLLM on the
   institution's hardware**, scores the open-response criteria and must emit **per-criterion evidence
   spans**, not a single number. 🟢 **AB 1159 is satisfied structurally**: the weights are local, the
   provider is the institution, and there is no third party to train on the data.
5. 🔴 **Gate.** Nothing is written back unattended. The instructor sees proposed score, per-criterion
   evidence and the rubric cell that fired, and **accepts, edits or rejects**. 🟢 **This is the
   Oklahoma/Maryland human-decision requirement and the EU Annex III human-oversight requirement, and
   it is the same gate** — build it once.
6. **Write back.** `canvasapi` writes the accepted grade and comment to the Canvas gradebook. 🔵
   **Prove this path on day one against a Canvas sandbox** — the write path is where these projects
   fail, and a demo that only reads looks identical to one that works.
7. **Log.** Every proposal, the evidence, the human's decision and the final grade, appended
   immutably. 🟢 **That log is the Annex III audit trail and the AB 1159 evidence**, and it is the
   artefact that renews the contract.

**Swap-ins by platform.** Moodle (**GPL-3.0-or-later**, confirmed on Packagist this pass) → replace
steps 1–2 with the MIT `moodle-mcp-server` side-cars already on the agents shelf. Open edX → keep the
AGPL platform untouched and extend through **Apache-2.0 `XBlock`**; never fork `edx-platform`.

**Effort:** **6–8 weeks** to a production pilot on one course, assuming the institution supplies the
Canvas sandbox and the GPU. **Regions:** 🟢 strongest in **North America** (named statutes, named
budget owner) and **EMEA** (Annex III); works in **APAC** and **LATAM** wherever data residency is
the constraint.

### 🔵 Cross-cutting gate update — the two-channel check joins the existing licence gates

`P43`'s decision table applies to the dependency gate in **every** pattern on this page, not just to
new work. Three concrete additions:

- **`master`-only repos are a live failure mode.** `ucfopen/canvasapi`, `dmitry-viskov/pylti1.3` and
  `ucbds-infra/otter-grader` are all on `master`. **Probe both branches or lose true rows.**
- **Install name ≠ repo name.** `pylti1.3` → `pylti1p3`. Pin the distribution, not the repository.
- **Flag single-source rows explicitly.** Chamilo (Packagist 404) and `crewai` (no PyPI licence
  metadata) are **payload-only** and must say so on the row, rather than silently reading as
  double-verified.

## 🟢 Thirty-third pass, 2026-10-07 — two recipes: P41, P42

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com` on
2026-10-07**, with a branch- and case-aware probe (13 filenames × `main` and `master`). No star counts
(`api.github.com` **403**, github.com **403** on HEAD and GET), so these recipes are composed on
**licence and documented capability**, not popularity. ⚠️ **No weights licence below is
payload-verified** — `huggingface.co` → **000** from this environment (`P464`). Durations are
**estimates for a Globant squad**, not measurements.

---

## P41 — The defensible integrity layer: local proctoring that survives Annex III and Decree 33

🔵 **The problem.** Exam integrity is the most regulated function in education AI and the one clients
ask for most often. EU **Annex III point 3** covers exam and behaviour monitoring; Vietnam's
**Decree 33** (in force 2026-08-15) classifies AI that *"monitors and analyses learner behaviour with
biometric data"* as high-risk; Idaho's 2026 law provides that **no AI may replace a human teacher**.
Meanwhile the commercial proctoring market is built on exactly what all three regimes penalise:
cloud biometric APIs returning an unexplained *"87% cheating probability"*. 🔴 **And this KB spent 26
passes telling readers no permissive option existed. It was wrong** — see `P461`/`P462`.

🟢 **The recipe.** Everything permissive, everything verified this pass:

| Component | Repo | Licence (payload) | Job in the stack |
|---|---|---|---|
| Integrity agent | [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | **MIT** (1068 B, `master/LICENSE`) | On-device OpenCV/MediaPipe, **22-dimension behavioural vector**, from-scratch logistic regression + anomaly detection, risk decay and fusion, TF-IDF, SQLite. Emits an **evidence breakdown** |
| Cross-check implementation | [`SuyashMore/AI-Proctored-Examination-System`](https://github.com/SuyashMore/AI-Proctored-Examination-System) | **MIT** (1068 B) | Second independent MIT implementation — use it as a **differential oracle** on the risk signals, not as a second deployment |
| Exam delivery | **Safe Exam Browser** / `SafeExamBrowser/seb-server` | already on this KB's shelf | lockdown delivery; the agent scores, SEB constrains |
| Human gate + rubric trail | [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | **MIT** (1076 B) | the appeal record: weighted criteria as data, versioned in git |
| Gradebook write-back | one of the six MIT LMS MCP servers (**P39**) | **MIT** | return only **human-confirmed** outcomes to the system of record |

⚠️ **Do not deploy [`openedx/edx-proctoring`](https://github.com/openedx/edx-proctoring) (AGPL-3.0,
35119 B) or [`kamlendras/OpenProctor`](https://github.com/kamlendras/OpenProctor) (AGPL-3.0, 34523 B)
inside a redistributed deliverable.** Self-hosting either for a client is fine; embedding either in a
product you ship is a network-copyleft event. **The MIT agent outside the tree is the whole point.**

**Wiring.**

1. **Run every frame locally and discard it.** Extract the 22-dimension feature vector on-device;
   persist features and scores, never imagery. This single decision is what moves the deployment out
   of the worst of Decree 33's biometric exposure, and it is the repo's default behaviour.
2. **Keep the from-scratch models, resist the urge to "upgrade" to an API.** The explainability is
   not a feature bolted on; it is a consequence of logistic regression and anomaly detection with
   inspectable coefficients. A frontier-API rewrite would be MIT-licensed and unsellable in both
   regimes.
3. **Emit per-signal evidence for every risk score**, with the decay and fusion terms shown. *"Gaze
   off-screen 14× plus atypical typing cadence → 0.73"* is contestable; *"0.73"* is not.
4. **Gate every consequential decision on a human**, and record the override. Idaho's human-teacher
   guarantee, Annex III human-oversight evidence and a student's right of appeal are all satisfied by
   the same stored tuple: features, score, explanation, reviewer, decision, timestamp.
5. **Cross-check with the second MIT implementation during calibration only.** Where the two
   disagree on a signal, that signal is not ready to carry a consequence.
6. **Write back only confirmed outcomes** through the MCP gradebook path from **P39**, version-pinned
   and tested against a staging course.

🔵 **Sells in APAC on Decree 33 and the Korean AI Basic Act, in EMEA on Annex III point 3 (due
2027-12-02, with Article 50 labelling live since 2026-08-02), and in North America on the Idaho
human-teacher guarantee.** Same build, three arguments. **Estimate: 6–9 weeks** for a calibrated
single-institution pilot; the calibration, not the code, is the long pole.

⚠️ **The honest caveat.** Both repos are small-team projects, not products. The licence is clean and
the architecture is right; the hardening, accessibility review and bias testing across cohorts are
the engagement. **Audit the risk-fusion maths before it carries a consequence for a student.**

---

## P42 — Scrub-then-score: a LATAM student-data pipeline with no English-first assumptions

🔵 **The problem.** LATAM is the most AI-positive region measured — **87% of institutions use AI in at
least one area** — and the least governed: **only 26% have a formal AI strategy**, and **88% of
faculty report minimal-to-moderate engagement**. So the typical regional engagement does not start
with a greenfield build; it starts with **AI already running on student data that nobody governs**.
⚠️ **And the first technical problem is specific to the region:** PII detectors trained on English
under-perform on Spanish and Portuguese names, national identifier formats (RUT, CPF, CURP, DNI) and
address conventions — so the scrubbing step most pipelines inherit does not actually scrub.

🟢 **The recipe.** Regional where it must be, permissive throughout:

| Component | Repo | Licence (payload) | Job in the stack |
|---|---|---|---|
| PII scrub | [`latam-gpt/anonymization-filter`](https://github.com/latam-gpt/anonymization-filter) | **MIT** (1072 B, © 2025 GonzaloFuentes1) | Anonymisation filter from the **Latam-GPT** corpus pipeline — built for regional text, not adapted to it |
| Regional evaluation | [`latam-gpt/lm-evaluation-harness`](https://github.com/latam-gpt/lm-evaluation-harness) | **MIT** (1067 B, © EleutherAI) | ⚠️ **a fork** — regional task configuration over EleutherAI's harness; cite upstream |
| Sycophancy check | [`latam-gpt/syco-bench`](https://github.com/latam-gpt/syco-bench) | **MIT-0** (903 B) | ⚠️ **MIT-0, not MIT.** A tutor that agrees with a wrong answer is a pedagogical failure; this measures it |
| Rubric store | [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | **MIT** (1076 B) | auditable weighted criteria |
| Scorer | [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) | **Apache-2.0** (10141 B) | rubric-conditioned judging on client hardware |
| Tutor surface, Open edX estate | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** (1068 B) | the proven LATAM shape: MIT agent inside an Open edX deployment |

⚠️ **Model choice is deliberately left open, and that is the design.** **Latam-GPT's weights are
reported under the Llama 3.1 Community Licence — not OSI-approved — and could not be verified from
this environment** (`P464`). **Treat the model as a swappable, client-chosen dependency behind an
interface**; the permissive code above is what you actually vendor.

**Wiring.**

1. **Start with an inventory, not a build.** Against the 87%/26% gap, the first deliverable is a map
   of what AI is already touching student data and under whose authority. Point at UNESCO's
   **Observatory on AI in Education for Latin America and the Caribbean** (launched **2026-04-14**)
   as the external framework, so the governance work is not Globant's opinion.
2. **Put `anonymization-filter` in front of everything**, before any model sees a record. Validate it
   against the identifier formats of the actual countries in scope — do not assume one regional
   filter covers RUT, CPF, CURP and DNI equally. **Measure the miss rate and write it down.**
3. **Score with `prometheus-eval` against rubrics held in `rubric`**, on institution-owned hardware.
   Scrubbed input plus local inference is the argument that student data never left the institution.
4. **Gate the tutor on `syco-bench`.** Regional-language tutoring that validates wrong answers is
   worse than no tutoring; run it as a release gate, not a one-off.
5. **Deliver inside the existing estate.** Where the institution runs Open edX, follow `TutorIA`'s
   shape — MIT agent as an XBlock or external service against Apache-2.0 surfaces, leaving
   `edx-platform`'s AGPL-3.0 exactly where it already is.
6. **Hand over the governance artefact,** not just the system: data flows, scrub miss rates, rubric
   versions, model and weights provenance, human-review log. **That document is what turns a 26%
   strategy-coverage institution into one that has a strategy**, and it is the reason the engagement
   can be funded in a market where capital is selective.

🔵 **Why this is fundable where a platform build is not.** Edtech venture funding is down and
institutional appetite is high but shallow. This recipe retires a **specific, nameable** risk —
ungoverned student data in a pipeline already running — on an installed base the client already paid
for. **Estimate: 4–6 weeks** for the inventory plus a scrubbed, locally-scored pilot on one faculty;
the regional PII validation in step 2 is the part not to compress.

## 🟢 Thirty-second pass, 2026-10-07 — three recipes: P38, P39, P40

**Every repo named below had its licence read from its own payload on `raw.githubusercontent.com`
on 2026-10-07.** No star counts (`api.github.com` **403**, github.com **403** on HEAD and GET), so
these recipes are composed on **licence and documented capability**, not on popularity. Durations are
**estimates for a Globant squad**, not measurements.

---

## P38 — The auditable grader: rubric-as-data, scored on hardware the client owns

🔵 **The problem.** EU AI Act **Annex III** makes AI that assesses learning outcomes **high-risk**,
with conformity duties due **2 December 2027** — ⏸️ **[Corrected in the thirty-third pass, 2026-10-07:
this recipe read *"full enforcement from **August 2026**"*. That date was already superseded when the
recipe was written. Regulation (EU) 2026/1744 (*Digital Omnibus on AI*, CELEX 32026R1744) deferred
**Annex III stand-alone high-risk from 2026-08-02 to 2027-12-02**, and Annex I embedded to
2028-08-02. **Article 50 transparency was NOT deferred** — it applies from 2026-08-02, with the
backstop for already-deployed systems at 2026-12-02. See `P284` and `P464`.]** — namely: risk
management, data governance, human oversight,
transparency and a **conformity assessment**, all *before* deployment. In the US, California
**A.B. 1159** would bar student data from training models unless the school benefits, and Idaho
**S.B. 1227** mandates data-privacy requirements for K-12 AI tools. A grader built on a frontier API
with the rubric inside a prompt satisfies none of it: the decision is not reproducible, the criteria
are not inspectable, and student work left the building.

🟢 **The recipe.** Three permissive components, all verified this pass:

| Component | Repo | Licence (payload) | Job in the stack |
|---|---|---|---|
| Rubric store | [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | **MIT** (1076 B) | Weighted rubric as a **data structure**, provider-agnostic — the auditable criteria |
| Scorer | [`prometheus-eval/prometheus-eval`](https://github.com/prometheus-eval/prometheus-eval) | **Apache-2.0** (10141 B) | Rubric-conditioned LLM-as-judge with **open evaluator weights** |
| Runtime + sizing | [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | **Apache-2.0** (11350 B) | OpenVINO pipelines on Intel CPU/iGPU/NPU, **plus benchmarking to size the hardware** |
| Gradebook write | one of the six MIT MCP servers (**P39**) | **MIT** | Return the grade to the system of record |

**Wiring.**

1. Author each assessment's rubric in `rubric` as weighted criteria — **versioned in git**. This is
   the artefact a conformity assessment asks for, and the reason it must not be a prompt string.
2. Size the deployment with `education-ai-suite`'s **benchmarking** tools before buying anything:
   decide CPU vs iGPU vs NPU against real throughput for the cohort size.
3. Score with `prometheus-eval` against the rubric, **on the client's own hardware**. Open weights
   mean the deployer can audit the evaluator rather than cite a vendor attestation.
4. Persist, for every scored submission: rubric **version**, per-criterion score, model and weights
   **version**, and the reviewing human's decision. This tuple *is* the transparency and
   human-oversight evidence.
5. Gate on a human. Under Annex III the human must be able to **override and have that recorded** —
   so the override path is a product requirement, not a UX nicety.
6. Write back through the MCP server of P39 — never directly against the gradebook API.

⚠️ **Scope discipline that keeps you out of the high-risk band entirely.** Annex III attaches to
assessment that determines **access**, evaluates **learning outcomes**, or shapes an **educational
path**. **Formative** feedback that never contributes to a grade of record is a materially lighter
regime. 🟢 [`baker-jr-john/automated-summary-evaluation-llm`](https://github.com/baker-jr-john/automated-summary-evaluation-llm)
(**MIT**, Llama 3.1 8B, validated on middle-school informational summaries) is the reference for the
formative-only shape — and the only component on this shelf tested against real K-12 student
writing. **Ship formative first, summative second**, and the first release carries a fraction of the
compliance load.

⏱️ **Estimate: 8–10 weeks.** 2 for rubric modelling with the client's assessment leads, 2 for
hardware sizing and the OpenVINO deployment, 3 for the scoring pipeline plus the evidence store,
2 for the human-review UI and override trail, 1 for the conformity-file handover.
🔵 **Sells in EMEA on Annex III, and in North America on A.B. 1159 / S.B. 1227.** Same build.

---

## P39 — The gradebook agent, pinned: pick one of six MIT MCP servers and prove the write path

🔵 **The problem.** Six independent MIT MCP servers for LMS gradebooks appeared in one window
(`agents/top.md`), each by a **different author**. They are the fastest route to an agent that does
the administrative work teachers actually lose time to. ⚠️ **But none of them is a standard**: tool
counts span **3×** (51 / 102 / 165), there is no shared schema, no conformance suite, and no
agreement on whether a grade write is **idempotent**. And two repos circulated as part of the same
"all MIT" set have **no licence at all**.

🟢 **The recipe — choose by audit surface, not by tool count.**

| If the engagement needs | Pick | Licence |
|---|---|---|
| The widest write surface (gradebook history, rubrics, admin workflows) | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** (© Christian Bru) |
| Packaged workflows — bulk grading of 10+ submissions as a first-class skill | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** (© Vishal Sachdev) |
| Spanish-language delivery team, HTTP transport + Swagger | [`CharlieCardenasToledo/mcp-canvas-server`](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | **MIT** (© Charlie Cárdenas Toledo) |
| 🟢 **The smallest surface to audit line-by-line before it gets credentials** | [`mtgibbs/canvas-lms-mcp`](https://github.com/mtgibbs/canvas-lms-mcp) | **MIT** (© mtgibbs) |
| **Moodle**, not Canvas | [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** (© Jawadh) |

🔴 **Do NOT use** [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp) or
[`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) — **no licence
payload** under 12 probed filenames. Public is not a grant.

**Wiring.**

1. **Pin the commit, not the tag.** None of the six has a stability guarantee; a tool rename
   mid-engagement is a silent break.
2. **Run the P37 two-reader licence gate** on the chosen repo before it reaches a client branch.
3. **Build the conformance suite that does not exist.** Against a **staging course**, assert for
   every write tool: a repeated write is idempotent; a partial failure does not half-apply; a grade
   write is rejected when the submission is missing; an unauthorised scope fails closed. 🔵 **This
   suite is the deliverable's most reusable asset** — it survives switching servers, and nobody in
   this cluster has published one.
4. **Read-only credentials until the suite is green.** Grades are contested, audited and appealed;
   an agent that silently mis-writes one is a legal problem, not a bug.
5. **Keep it a side-car.** For Moodle this is a licence requirement, not a style choice: the MCP
   server stays **outside** the GPL-3.0 tree and talks over the API.
6. **Log every write** with actor, tool, version and before/after value. Feeds P38's evidence store.

⏱️ **Estimate: 4–6 weeks.** 1 for selection + licence gate, 2 for the conformance suite against
staging, 1–2 for agent wiring and the audit log, 1 for supervised rollout to a pilot cohort.
🔴 **Do not skip step 3 to save two weeks.** It is the only thing separating this from an agent with
write access to the institution's most consequential data and no test for what it does.

---

## P40 — Offline-capable local tutor for a connectivity-constrained region

🔵 **The problem.** LATAM demand is already near-universal while institutions are not: **73%** of
Mexican university students use AI for coursework, and **over 80%** of Mexican higher-education
institutions have **no normative framework** (`intel/market.md`). Rural deployments add bandwidth
and cost limits, and funding is **down 26% YoY** — so per-call API pricing is the wrong shape
regardless of policy.

🟢 **The recipe.**

| Component | Repo | Licence (payload) | Job |
|---|---|---|---|
| Reference implementation | [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** (© 2026 Grupo Sirius) | Open-edX-native tutor for **rural** Colombian higher ed: TTS voice, avatar, teacher analytics, context persistence |
| Platform | [`openedx/XBlock`](https://github.com/openedx/XBlock) on Open edX | 🟢 **Apache-2.0** (`LICENSE.TXT`) | The **permissive** extension point — see the licence note below |
| Local workspace | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** (© Zijin Zhang) | Runs **locally**, 10+ providers, **no API key**: FSRS spaced repetition, knowledge graph, cognitive-load detection |
| Local inference + sizing | [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | **Apache-2.0** | OpenVINO on commodity Intel hardware, **with benchmarking** |
| Spanish enablement | [`0xnavarro/IA-PARA-TODOS`](https://github.com/0xnavarro/IA-PARA-TODOS) | **Apache-2.0** | Spanish-language teaching substrate for staff and student onboarding |

🔴 **The licence constraint that decides the build.** `openedx/edx-platform` is **AGPL-3.0** (35136 B,
read this pass); `openedx/XBlock` is **Apache-2.0** (11357 B, `master/LICENSE.TXT`). **Build the
agent as an XBlock or as an external service** and the AGPL stays on a platform the client
self-hosts. **Fork `edx-platform` to embed it and AGPL-3.0 attaches to the whole deliverable.**
🟢 `TutorIA` is a working instance of the permissive shape, which is why it anchors this recipe.

**Wiring.**

1. Start from `TutorIA`'s shape — it already solved the hard parts for this context: voice output for
   low-literacy and low-bandwidth use, an avatar for face-to-face expectation, and a **teacher**
   analytics panel. ⚠️ Note it ships pointed at a hosted model API; **swapping the language engine
   for a local one is the main integration work**, not a bonus.
2. Size with `education-ai-suite`'s benchmarking, then run inference locally. Capital cost replaces
   per-call cost — the only shape that survives a −26% funding market.
3. Use `OpenTutor` for the **offline study loop** (FSRS spaced repetition, knowledge graph) so the
   student keeps working when the link drops; sync when it returns.
4. Deliver the **governance artefacts alongside the software** — academic-integrity policy,
   assessment redesign that assumes AI availability, staff AI-literacy training in Spanish via
   `IA-PARA-TODOS`. 🔵 In LATAM this is not an add-on: **80%+ of institutions have no framework**, so
   the policy is the differentiator and the software is the easy half.
5. **Lead with augmentation, never substitution.** Korea mandated AI textbooks, reached **under
   30%** adoption, and the National Assembly **stripped their official status** in August after
   union pushback. Idaho **S.B. 1227** legislates the same conclusion from the other direction by
   prohibiting AI from replacing teachers. 🟢 India's **DIKSHA** is the durable model — AI as
   **accessibility** (read-aloud, in-video search) — and runs on
   `project-sunbird/sunbird-lms-service` (MIT), already on this shelf.

⏱️ **Estimate: 10–12 weeks.** 2 for `TutorIA` assessment and local-model substitution, 2 for
hardware sizing and deployment, 3 for Open edX/XBlock integration and the offline sync loop, 2 for
governance artefacts and Spanish enablement, 2 for a teacher-led pilot with evidence collection.

⚠️ **The reusability caveat, stated plainly.** Three of the four LATAM repos found this pass carry
**no licence** — `a-bobadilla/Asistente-Pedagogico-IA`, `henriquebotelhogomes/educacao` (Brazil),
`virginiandujar/educa-ia`. Relevant work exists that **no client can legally use**, so this recipe
is built on **one** verified LATAM component plus Global ones. 🟢 **The cheapest upstream
contribution available to Globant in this industry: help those teams add a grant.** It is one file,
and it converts regional work into reusable regional assets.

---

### 🔵 Cross-cutting gate update — `P455` and `P456` join the licence-reliability checks

Both findings below belong to the **P22 / P22.5 / P37** family of licence gates and apply to every
recipe on this shelf:

- 🔴 **`P455` — existence is not the grant.** [`murderszn/open-tutor`](https://github.com/murderszn/open-tutor)
  serves a 869-byte `main/LICENSE` that **declares no licence**: *"A public GitHub repository is not
  itself a declaration of an open-source or open-content license."* **Add to the gate: read the
  payload's grant, never just its HTTP status.**
- 🔴 **`P456` — check the word's role, not just its presence.** [`formalms/formalms`](https://github.com/formalms/formalms)
  publishes **no licence payload**; the only "Apache" in its README is
  **`- Apache (recommended) with mod_rewrite enabled`** — a **web server** in a requirements list,
  which a secondary source converted into "Apache 2.0 … without the copyleft obligations GPL and
  AGPL carry." **Add to the gate: a licence family in a requirements/install/stack section is not a
  licence claim.**
- 🔴 **`P457` — de-duplicate on the licence copyright holder, not the README hash.**
  `algenlab/adaptive-tutor` is a **renamed** fork of `zijinz456/OpenTutor` with an **edited** README
  (different md5), so hash comparison passes it through; its `LICENSE` still reads
  **© Zijin Zhang**. **Add to the gate: before shelving a repo as new, compare its licence holder
  against every repo already shelved.**
- 🔴 **`P459` — a holder must be a party, not a clause.** The long-form licences name *copyright*
  inside their own body, so an unrestricted scrape returns `owner or entity authorized by` for every
  Apache-2.0 payload and **merges two unrelated repos as a fork pair**. **Add to the gate: read the
  holder from the payload's head region only, and reject clause fragments.** Instrument and suite:
  `compose/code/licence-grant-gate/` (`47/47` offline, `12/12` live).
- ⚠️ **`P453` / `P454` / `P458` — re-probe old `ABSENT` verdicts.** `raw.githubusercontent.com` is
  **case-sensitive**, `.rst` projects were invisible to the README fallback, and a repo's own README
  can link a licence path that 404s. All three produced a false `ABSENT` on `openedx/XBlock`, a real
  Apache-2.0 repo already on this shelf. **These defects delete true rows silently** — any
  pre-pass-32 `ABSENT` should be re-checked before it is relied on.

# Compose Patterns — Education

Concrete recipes built only from repos verified in `agents/top.md`,
`repos/foundations.md` and `verticals/solutions.md` on 2026-10-06. Every
component names its license, because in this industry the license decides the
architecture.

**The rule behind patterns P1–P6:** the education platform shelf is mostly
copyleft (Moodle GPL-3.0, Open edX / Canvas / Frappe AGPL-3.0). AI built as an
in-tree plugin inherits that license; the same AI built as an external service
over LTI 1.3 or MCP stays permissive. Globant's reusable IP lives in the
side-car.

---

## P1 — LTI + MCP side-car tutor (the default engagement shape)

**Use when:** the client already runs an LMS, which is almost always.
**Outcome:** AI tutoring inside the existing LMS, with Globant's code permissive.

**Wiring:**
1. Leave the LMS untouched — Moodle (GPL-3.0), Canvas (AGPL-3.0) or Open edX
   (AGPL-3.0). No fork, no in-tree plugin.
2. Register a tool provider for launch, identity and grade passback.
   🔴 **CORRECTED, twenty-fourth pass of 2026-10-07 — this step named the wrong protocol.** It
   previously specified
   [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP)
   (Apache-2.0, payload 11,357 B). Its head commit is **2016-11-28 — 3,600 days, 9.9 years**, the
   oldest component in any pattern in this KB, and its `README.md` states it supports
   **"LTI 1.1 and the unofficial extensions to LTI 1.0"** — **it does not implement LTI 1.3 at
   all.** LTI 1.1's security model is retired; LTI 1.3 / Advantage is what Canvas, Moodle and
   Open edX certify against and what the procurement rubrics in `intel/market.md` score.
   ⚠️ The organisation name was the tell: **IMSGlobal renamed itself 1EdTech in 2022.**
   🟢 **Use instead, by estate:**
   - **Python / Django** (the usual case here, since steps 4–6 are Python):
     [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) — **MIT** (1,098 B), head commit
     **2026-10-05 (2 d)**, PyPI [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1
     (61 d)**. Launch in-process; **no second runtime**.
   - **JupyterHub**: [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator)
     — **BSD-3-Clause** (1,528 B), 98 d, LTI 1.3 **and** 1.1, tested against Open edX, Canvas, Moodle.
   - **PHP / Moodle estate**: [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library)
     — **Apache-2.0** (11,343 B), **14 d**.
   - **Node estate**: [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) — Apache-2.0, 1 d.
3. Expose LMS data to the agent over MCP:
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
   up to 103 tools, 8 agent skills) for Canvas, or
   [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server)
   (MIT) for Moodle.
4. Tutoring engine: [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
   (Apache-2.0) via its WebSocket API or Python SDK, one TutorBot workspace per
   learner so memory is per-student.
5. Orchestrate with [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
   (MIT); type every boundary with [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT).
6. Serve models through [ollama/ollama](https://github.com/ollama/ollama) (MIT)
   when residency is required, or a commercial API when it is not.

**Why this order:** step 1 is what keeps steps 4–6 permissive. Reverse it — write
a Moodle plugin — and the tutor becomes GPL-3.0 and stops being reusable IP.

**Watch:** LTI grade passback is a consequential decision path. Put the P4
human-oversight gate in front of it before any grade is written back.
**Effort:** 6–8 weeks for a single-LMS pilot.

---

## P2 — Curriculum ingestion → item bank

**Use when:** the client has curriculum in PDFs and textbooks and needs
assessment items or lesson content at volume.

**Wiring:**
1. [opendatalab/MinerU](https://github.com/opendatalab/MinerU) (Apache-2.0)
   parses PDFs, textbooks and scanned material into structured text.
2. [satvik314/educhain](https://github.com/satvik314/educhain) (MIT) generates
   MCQs, open-ended items, lesson plans and flashcards from that text.
3. Validate every generated item against a schema with pydantic-ai (MIT) —
   reject rather than repair malformed items.
4. Route items into the LMS question bank: Moodle qbank, or Open edX via
   [overhangio/tutor](https://github.com/overhangio/tutor) (AGPL-3.0) for
   deployment.
5. **Human review before any item goes live.** Not optional — see below.

**Hard constraint:** there is no permissive open source auto-grader (declared gap,
re-searched 2026-10-06). Generate items and feedback automatically; keep scoring
human-gated. This also satisfies Oklahoma/Maryland human-oversight statutes and
EU AI Act Annex III.
**Effort:** 4–6 weeks.

---

## P3 — Mastery-tracked adaptive practice

**Use when:** the client needs adaptive sequencing *and* has to justify why a
learner was judged to have mastered something.

**Wiring:**
1. [CAHLR/OATutor](https://github.com/CAHLR/OATutor) (MIT) supplies Bayesian
   Knowledge Tracing — an inspectable, parameterised mastery estimate per skill,
   published at CHI '23 with follow-up in PLOS ONE.
2. LangGraph (MIT) runs the per-skill state machine: practice → BKT update →
   branch to remediation, hinting or advance.
3. DeepTutor (Apache-2.0) generates hints and explanations at the remediation
   node; its Capabilities layer is the right place for a multi-turn
   remediation dialogue.
4. Persist BKT parameters and LangGraph checkpoints together — that pairing *is*
   the audit record of why the system decided what it decided.

**Why BKT rather than asking a model:** under EU AI Act high-risk assessment
rules and Brazil's PL 2.338 risk tiers, "the LLM said so" is not a defensible
mastery claim. A BKT posterior with known priors is.
**Effort:** 6–10 weeks.

---

## P4 — EMEA sovereign, Annex III-ready deployment

**Use when:** EU client, assessment or access decisions in scope. The AI Act
defers stand-alone high-risk obligations to **2 December 2027** — that deferral
is the design window, not a reason to wait.

**Updated in the fifth pass of 2026-10-06.** The deferral has a regulation number
and a catch: **Regulation (EU) 2026/1744** (*Digital Omnibus on AI*, in force
27 July 2026, CELEX 32026R1744) moved Annex III to 2 December 2027 and Annex I to
2 August 2028, **but left Article 50 transparency untouched — the watermarking
and synthetic-content-marking deadline is still 2 December 2026.** So the
sovereign build below is the December 2027 programme, and there is a small,
separate, nearly-immediate obligation in front of it. **Run P13 before this
pattern**, not after: it classifies the estate and ships the labelling layer.

**Wiring:**
1. Inference stays in-region: ollama (MIT) or vLLM on-prem, open-weight models
   (Llama, Mistral). No student data to a third-party API.
2. pydantic-ai (MIT) for typed, schema-validated outputs at every boundary —
   structured decisions are auditable, prose is not.
3. LangGraph (MIT) checkpoints as the immutable decision trail: inputs, model
   version, intermediate state, output, timestamp.
4. OATutor (MIT) BKT for any mastery or progression claim, so the assessment
   logic is explainable independently of the model.
5. **A human-oversight gate as a required graph node** before any grade, access
   or progression decision is committed. The gate records who approved what.
6. [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core)
   (Apache-2.0) if competency claims leave the institution.

**Deliverable is two things:** the system, and the Annex III conformity
documentation it generates. Sell both.
**Effort:** 10–14 weeks. Reuses directly for Brazil PL 2.338 readiness.

---

## P5 — Offline-first equity deployment (LATAM and low-connectivity)

**Use when:** connectivity, device or budget constraints are real — which per
CEPAL covers much of LATAM, where >50% of Chilean and Brazilian teachers already
use AI but <10% of institutions have the capacity to support it.

**Wiring — a fully MIT stack, no copyleft anywhere:**
1. [learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT)
   as the platform; runs offline on a classroom server or a single laptop.
2. [learningequality/studio](https://github.com/learningequality/studio) (MIT)
   for curriculum authoring and channel curation.
3. [learningequality/ricecooker](https://github.com/learningequality/ricecooker)
   (MIT) to package existing client or ministry content into Kolibri channels.
4. ollama (MIT) with a small quantised model on the local server for offline
   tutoring and question answering — no egress, no per-token cost.
5. Sync opportunistically when connectivity appears; never assume it.
6. **Added in the fifth pass of 2026-10-06 — read a working implementation of
   steps 4 and 5 before building them.**
   [DannyAvilaL/agente_clases](https://github.com/DannyAvilaL/agente_clases)
   (**MIT**, Spanish-language, 0★, 5 commits) is the most concrete offline-first
   education agent this KB has recorded: **Ollama Phi-3 (2 GB)** generating
   per-student Markdown material and exercises, synthesised `.csv` datasets
   injected as tables into local **PostgreSQL**, Google Calendar syncing *down*
   into a local **Radicale** CalDAV server so the system keeps running with no
   internet, a **Streamlit** dashboard for teachers, and a `cron` autopilot that
   prepares classes a week ahead. Two design choices worth copying outright: the
   **2 GB model floor** (it names the laptop-class hardware it runs on), and
   **calendar sync in the offline-safe direction** — cloud is a source, never a
   dependency. 0★ and single-author: **read it, do not pin it.**
6. For Spanish-first public-sector clients that require a conventional LMS
   instead, substitute [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms)
   (GPL-3.0) — accepting the copyleft, and keeping the AI as a P1 side-car.

**Positioning:** pair with UNESCO's LAC AI-in-Education Observatory (launched
14 April 2026) and lead with teacher enablement and governance, which is the
measured gap, rather than with software alone.
**Effort:** 4–6 weeks for a pilot site; the content pipeline dominates.

---

## P6 — Client capability build (enablement)

**Use when:** the client's own staff must own the system afterwards — which is
how an engagement becomes a programme rather than a project.

**Wiring:**
1. [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
   (MIT, 18 lessons) as the core track; its samples target MAF, which is the
   framework you want taught.
2. [huggingface/agents-course](https://github.com/huggingface/agents-course)
   (Apache-2.0) as the second track for framework-agnostic grounding, and
   [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai)
   (MIT) for a cohort-tested syllabus.
3. [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)
   (MIT) as the prerequisite for non-AI staff;
   [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
   (Apache-2.0) or [mlabonne/llm-course](https://github.com/mlabonne/llm-course)
   (Apache-2.0) for the deep track.
4. [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub)
   (BSD-3-Clause) to give the whole cohort an identical environment on day one.
5. Teach on **Microsoft Agent Framework (MIT)**, not AutoGen — AutoGen is in
   maintenance mode and will not receive new features.

**Effort:** 3–4 weeks to stand up, then runs continuously.

### P6 update, twenty-ninth pass of 2026-10-07 — three assets that change the first week

The mandatory query set produced new repositories for the first time in seventeen passes, and
all three land on this pattern rather than on any product tier. Verified payload-first:

6. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
   (**Apache-2.0**, 140,891★, pushed 2026-09-30) — **100+ runnable agents, Agent Skills and
   RAG apps.** Put this *before* the lesson tracks above, not after: a cohort that has run a
   working agent on day one argues about architecture in week two instead of week five.
   ⚠️ It is an *examples* corpus — fork it as curriculum and read each app's own dependencies
   before anything from it enters a deliverable.
7. [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML)
   (**MIT**, 49,696★) — the **deploy-and-iterate** track this pattern was missing. Steps 1–3
   teach agents; this teaches what happens after the demo works, which is the part a client
   programme actually fails at. ⚠️ Last pushed **2026-03-04**: teach the method, re-pin the
   dependencies.
8. [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
   (**Apache-2.0**, 29,517★) — the clearest permissive treatment of embeddings, retrieval and
   fine-tuning on this shelf; the right deep track for staff who will own the RAG layer in
   `P1` or `P8`. ⚠️ Last pushed **2026-04-24**; a book's companion repo is *meant* to freeze.

🟢 **All three are Apache-2.0 or MIT**, so the training materials themselves can be forked,
rebranded and left with the client — the difference between enablement and a course licence.

---

## P7 — Admin automation on an LGPL platform (the module, not the side-car)

**Added 2026-10-06.** The first six patterns all route around copyleft by building
a side-car. On the *administrative* shelf that is not forced, and routing around a
constraint that is not there costs you integration depth for nothing.

**Use when:** the client's pain is administrative — admissions triage, enrolment,
fee reconciliation, attendance follow-up, exam scheduling — rather than tutoring,
and they do not already run a committed SIS.

**Outcome:** AI-assisted administration inside the ERP, with Globant's module able
to stay proprietary.

**Wiring:**
1. Platform: [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp)
   (**LGPL-3.0**, 884★, 775 forks, v19.0, Odoo/Python). Admissions, student info,
   courses, exams, finance, attendance, library, HR already exist — do not rebuild
   them.
2. **Respect the LGPL boundary, because it is what buys you the proprietary
   option.** Do not fork OpenEduCat's own files: changes to them stay LGPL-3.0.
   Build a *separate* Odoo module that links against it through documented
   interfaces. That module can be proprietary.
3. Agent layer in the module: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
   (MIT) for typed, validated outputs on every record it writes, orchestrated with
   [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (MIT) so each
   administrative decision carries a checkpointed trail.
4. Documents in: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
   (Apache-2.0) for transcripts, certificates and application attachments.
5. Inference: [ollama/ollama](https://github.com/ollama/ollama) (MIT) on-prem —
   admissions data is exactly the category California AB 1159, EU residency
   practice and India's DPDP constrain.
6. If the client needs admin automation with **zero** copyleft exposure anywhere
   in the tree, substitute [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework)
   (Apache-2.0, Java) and accept that you are building the education domain model
   yourself.

**Watch:** admissions is an Annex III high-risk use case under the EU AI Act —
"AI used in education access" is named explicitly. An admissions agent is a
high-risk system, not back-office convenience. Put the P4 oversight gate on any
admit/reject path, and keep the agent on triage, completeness checking and
summarisation rather than the decision.

**Watch also:** if the client already runs an SIS, do not migrate them. Gibbon
(GPL-3.0), RosarioSIS (GPL-2.0) and openSIS (GPL-2.0) are all copyleft, so there
P1's side-car shape returns. RosarioSIS being GPL-**2.0** also means it is not
license-compatible with GPL-3.0-only code — check before combining anything.
**Effort:** 5–7 weeks for a single-process pilot (admissions triage is the usual
first one).

---

## P8 — Course materials → source-backed Agent Skills

**Added 2026-10-06.** P2 turns curriculum into an *item bank*. This turns it into
**portable agent skills**, which is a different and more reusable asset: the
institution's own pedagogy, loadable by any of the 40+ MCP-speaking clients.

**Use when:** the client's differentiator is *how they teach* — a methodology, a
sequencing, a body of worked examples — and it currently lives only in lecture
recordings, slide decks and a few senior instructors' heads.

**Outcome:** the institution's teaching method as versioned, source-attributed
skills, usable inside the LMS and outside it.

**Wiring:**
1. Capture: [opencast/opencast](https://github.com/opencast/opencast) (ECL-2.0,
   permissive) for the lecture corpus if it is not already recorded.
2. Structure: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
   (Apache-2.0) for PDFs, textbooks and scanned handouts.
3. Distil: [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill)
   (**Apache-2.0**, 448★, Python) — videos, PDFs, transcripts and notes into
   source-backed teacher Agent Skills. It preserves source attribution, extracts
   instructor methodology and orders practice tasks progressively, which is
   precisely the part a generic summariser throws away.
4. Deliver into the LMS: the 8 agent skills already shipped by
   [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
   up to 103 tools, v1.13.0) are the reference shape and the delivery path for
   Canvas; [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server)
   (MIT) for Moodle.
5. Deliver offline too: package the same distilled material into Kolibri channels
   with [learningequality/ricecooker](https://github.com/learningequality/ricecooker)
   (MIT) → [learningequality/kolibri](https://github.com/learningequality/kolibri)
   (MIT). One distillation, two delivery modes — this is what makes the pattern pay
   in LATAM and low-connectivity contexts.
6. Local authoring assist: [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED)
   (MIT, 60★) for local-first lesson drafting, so draft materials never leave the
   institution.

**Why source-backed is the whole point:** provenance back to the instructor's own
materials is defensible under the high-risk regimes in a way a fine-tune is not,
and it is what lets a faculty member accept the output. A skill that cannot cite
its source will not survive faculty review.

**Watch:** IP and consent. Lecture recordings carry instructor performance rights
and student voices and faces; third-party course content carries licensing terms.
Settle who owns a distilled skill — institution, instructor, or Globant — in the
SOW, before the first ingest. This is also the LATAM depth play: with 92% of
students and 79% of faculty already using AI but 88% of faculty engaging only
shallowly, the gap is integration into real teaching practice, which is exactly
what a skill built from their own course does.
**Effort:** 4–6 weeks for one programme; the second programme is roughly half,
because the pipeline is reused and only the corpus changes.

---

## P9 — Curriculum-mandate delivery with age-gated capability (UAE / China shape)

Added in the third pass of 2026-10-06. This is the only pattern in this KB driven
by a **funded obligation** rather than by a constraint, and the only one where the
regulator has specified the access-control model for you.

**Use when:** a ministry or provincial authority has made AI instruction
compulsory and the institution has to deliver curriculum-aligned material and
trained teachers against a deadline. Live today in the **UAE** (Cabinet, May 2025 —
KG to Grade 12 from the 2025–26 school year, seven content areas, inside an
existing subject with no added school hours, specially trained teachers) and in
**China at provincial level** (Beijing: ≥8 hours a year in every primary and
secondary school from 1 September 2025; Guangdong: 6 hours a year in lower grades
rising to one hour a fortnight in grades 10–11).

**Outcome:** curriculum-aligned content across the mandated areas, a teacher
enablement track, and a system that **structurally cannot** give a younger cohort
unmediated generative AI.

**Wiring:**
1. **Ingest the official curriculum framework first, not the textbooks.**
   [opendatalab/MinerU](https://github.com/opendatalab/MinerU) (Apache-2.0) over
   the ministry's published framework — for the UAE, the seven areas: foundational
   concepts, data and algorithms, software use, ethical awareness, real-world
   applications, innovation and project design, and policies and community
   engagement. The framework is the schema everything else is checked against.
2. **Generate against the framework, with the area as a required field.**
   [satvik314/educhain](https://github.com/satvik314/educhain) (MIT) for items,
   lesson plans and flashcards;
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT) to make
   `curriculum_area`, `grade_band` and `source_reference` **non-optional** on every
   generated artefact. An item that cannot name its area and grade band is not
   deliverable, and a typed boundary is what makes that a build error rather than a
   review finding.
3. **Produce the ethics and civics material deliberately.** Two of the UAE's seven
   areas — ethical awareness, and policies and community engagement — are not
   technique. Generic AI-literacy content does not cover them, and they need
   age-appropriate treatment per grade band. Budget for them as their own content
   stream; this is the part a competitor's pipeline will skip.
4. **Build the age gate as a routing layer, not a prompt instruction.**
   [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (MIT) with
   the cohort's grade band as graph state, and **distinct graphs per band**:
   - primary → **no independent generative-AI path exists in the graph.** The pupil
     reaches teacher-mediated and pre-generated material only. Beijing bars
     independent generative-AI use by primary pupils, so this must be a structural
     absence, not a refusal the model is asked to perform;
   - secondary lower → generated content with teacher review before release;
   - secondary upper → interactive tutoring, still with the teacher as approver on
     anything that lands in a grade.
   A capability tier the system cannot exceed is auditable; a system prompt asking
   it not to is not. **No permissive component implements this** — see the declared
   gap in `intel/trends.md` — so it is yours to build, and it is the reusable part.
5. **Protect the teacher's role in the design.** China prohibits teachers from
   substituting AI for core instructional duties, so the teacher-facing surface is
   preparation, differentiation and review — never autonomous delivery to the class.
   [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill)
   (Apache-2.0) to turn the ministry framework and the teacher's own materials into
   source-backed skills is the right shape here: it amplifies the teacher's method
   instead of replacing it.
6. **Run inference in-country.** [ollama/ollama](https://github.com/ollama/ollama)
   (MIT) or vLLM. For the UAE and China alike, assume the student-data boundary is
   non-negotiable and that this is also what makes the deployment affordable at
   provincial scale.
7. **Trace everything.** [langfuse/langfuse](https://github.com/langfuse/langfuse)
   (MIT outside `ee/`) on every call. The mandate will be inspected, and per-call
   cost, latency and output is the evidence. Exclude `ee/` from any vendored copy.
8. **Deliver the teacher track as a product, not a slide deck.** The UAE mandate
   funds "specially trained teachers".
   [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
   (MIT) and [huggingface/agents-course](https://github.com/huggingface/agents-course)
   (Apache-2.0) as the base; localise it and map each module to the mandated areas
   so the client can evidence coverage.

**Why this order:** the framework in step 1 is what makes steps 2 and 3 auditable,
and the graph topology in step 4 is what makes the age restriction a property of
the system rather than a promise about it. Reverse steps 4 and 2 — generate first,
gate later — and you end up filtering outputs at runtime, which is both weaker and
harder to evidence.

**Watch:** the mandates are **provincial in China**, so hour counts and grade
boundaries differ between Beijing and Guangdong. Parameterise the hour allocation
and the grade bands; do not hard-code one province's numbers. And verify the
current framework text with the client's ministry contact — a curriculum mandate is
revised more often than a statute.

**Reuse:** build this once and it satisfies the oversight requirements of EU AI Act
Annex III, the Oklahoma and Maryland human-oversight statutes, Korea's high-impact
classification and Singapore's IMDA agentic framework, because **Beijing's
restriction is the strictest of them.** The age-gating layer is the genuinely novel
asset — nothing permissive implements it.
**Effort:** 10–14 weeks for one grade band across the mandated areas, plus 3–4
weeks per additional band once the graph topology exists.

---

## P10 — Enterprise L&D on a permissive platform (fork it, brand it, resell it)

Added in the third pass of 2026-10-06. Every other platform pattern in this KB
assumes the platform is copyleft and routes around it. This one does not, and the
commercial shape is different as a result.

**Use when:** the client is a corporate L&D, onboarding or compliance-training
buyer — not an academic institution — and wants a platform they own rather than a
per-seat subscription.

**Outcome:** a white-labelled, self-hosted, AI-native LMS. Globant's extensions are
MIT, the platform is MIT, and **the deliverable is the whole product** rather than a
side-car attached to someone else's.

**Wiring:**
1. **Fork [Selleo/mentingo](https://github.com/Selleo/mentingo) (MIT).** 91★, 29
   forks, TypeScript, maintained by Selleo (Poland). Its README states the intent
   directly: *"MIT — modify, white-label and resell, no copyleft obligation."* There
   is no copyleft to architect around, so **do not build a side-car here** — that is
   P1's answer to a problem this platform does not have.
2. **Keep its stack and extend it.** PostgreSQL 16 +
   [pgvector/pgvector](https://github.com/pgvector/pgvector) (PostgreSQL License)
   for retrieval, Redis, S3-compatible storage, Node.js 22+. One database, no
   separate vector store.
3. **Swap the model layer for residency.** It ships Vercel AI SDK + OpenAI and
   LangChain; replace with [ollama/ollama](https://github.com/ollama/ollama) (MIT)
   or vLLM where the client's data cannot leave. This is the one substitution the
   architecture expects.
4. **Keep Langfuse and treat it as the compliance artefact.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) is already wired in and
   traces every call's cost, latency and output. Exclude `ee/`, `web/src/ee/` and
   `worker/src/ee/` from the vendored copy — those directories are **not** MIT.
5. **Use the automated grading where it belongs, and gate it where it does not.**
   Mentingo grades open-ended behavioural and problem-solving answers automatically
   with actionable feedback. For formative practice, ship it. For anything that
   gates certification, promotion, pay or a regulatory qualification, **put a human
   approval checkpoint in front of it** — the licence changed, the oversight
   obligation did not.
6. **Lean on the voice layer for compliance training.**
   [livekit/livekit](https://github.com/livekit/livekit) (Apache-2.0) under
   Mentingo's AI mentor runs real-time role-play for sales, compliance and
   customer-support scenarios and scores the attempt. Role-play with a scored
   transcript is a far better compliance-evidence artefact than a completion tick.
7. **Integrate rather than replace, via SCORM 1.2 export.** Mentingo exports SCORM
   1.2 and ships an OpenAPI/Swagger spec with a generated typed client. When the
   client already runs an incumbent LMS, author in Mentingo and **feed** the
   incumbent — a much easier sale than a platform migration.
8. **Multi-tenancy is already there.** It is multi-tenant and white-label out of the
   box, which is what makes one build serviceable across several client brands.

**Why this order:** step 1 is the whole pattern. The instinct this KB has trained —
never touch the platform, always build the side-car — is correct against Moodle,
Canvas and Open edX and **wrong here**, and following it costs integration depth
for no legal benefit.

**Watch:** Mentingo is an **L&D** product. No LTI 1.3, no SIS integration, no
gradebook semantics for credit-bearing courses, no institutional reporting; SCORM
1.2 is the L&D interchange format, not an academic one. **Do not sell it to a
university as a platform** — there it is a reference implementation and a component
donor. Also note it is 91★ and single-company-maintained: budget for carrying your
own fork, and read the upstream commit history before committing a client to it.

**Effort:** 6–8 weeks to a branded pilot with the model layer swapped; 10–12 weeks
with in-region inference and a human-approval gate on certification paths.

---

## P11 — Gated lesson generation (one oversight gate, sold in every region)

Added in the fourth pass of 2026-10-06. This is the pattern that **trend 16**
argues is the highest-reuse build in this KB: four US state legislatures, the EU
AI Act and Beijing all converge on *teacher-in-the-loop plus
no-high-stakes-automation*, so the gate is built once and sold everywhere.

**Use when:** the client has to produce teaching or assessment material at volume
**and** has a statutory human-oversight obligation. That is now the default, not
the exception — Idaho (SB 1227, *"human judgment remains the final authority"*),
Oklahoma (SB 1734, educator supervision + annual parent disclosure), Maryland (AI
Ready Schools Act, 24 districts / 120 days), Ohio (HB 96, deadline **passed**
1 July 2026, so districts are in implement-and-audit), the EU AI Act Annex III, and
China's bar on primary pupils using generative AI independently.

**Outcome:** generated lessons and assessments that **cannot reach a student or a
gradebook** without a named human approving them, with an evidence trail per
decision and a disclosure report the client can file.

**Wiring:**
1. **Generate with OpenMAIC, self-hosted from a reviewed fork.**
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) (**MIT, 40.0k★**,
   Tsinghua) turns a document or topic into slides, quizzes, HTML simulations and
   PBL scenes. **Pin v1.2.0 or later specifically**: that line is server-first with
   PostgreSQL persistence, so a generation is a **durable job** rather than a
   browser session — which is the only reason a review queue can be bolted on
   without rewriting its execution model. Point inference at whatever model the
   client's data-residency posture permits.
2. **Take the gate design from AI-Teaching-Agent, and re-implement it.**
   [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
   (MIT) is the only permissive implementation of this shape in this KB, and it
   is **0★ with no releases — read it, do not pin it.** Take four things: the
   **`WAITING_REVIEW` task state** that blocks publication, the **JSON-Schema-validated
   DSL** for lab/exam/grading artefacts, **sandboxed grading execution that emits
   evidence**, and the **candidate-facing view that strips answers and internal
   grading references**. That last one is the detail teams forget and leak on.
3. **Make the gate unskippable at the type level.**
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT): every
   publishable artefact carries non-optional `approved_by`, `approved_at` and
   `source_reference`. An unapproved artefact should fail to **construct**, not
   fail review. Typed boundaries are what turn a policy into a build error.
4. **Choose the generating model on pedagogical evidence, not vibes.**
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) — see **P12**. Record the score in the engagement's decision log; it is
   the cheapest defensible answer to "why this model?"
5. **Trace every generation and every approval.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) (MIT — **excluding
   `ee/`, `web/src/ee/` and `worker/src/ee/`**, which carry a separate enterprise
   licence; stay out of those paths). The trace is the Annex III technical
   documentation and the Oklahoma parent-disclosure evidence, from one store.
6. **Deliver into the LMS the client already runs** via the Canvas or Moodle MCP
   servers in `agents/top.md` — **probing each one's `LICENSE` payload first**, as
   three of seven in this KB turned out unusable.
7. **Where you cannot host the generator, export instead.** OpenMAIC emits **PPTX
   and interactive HTML**, so a buyer who will not run a Chinese-origin application
   can still take the artefact. Generate in Globant's environment, gate it, hand
   over the deck.

**Effort:** 6–8 weeks for a gated pipeline on one subject and one grade band;
10–12 weeks with multi-cohort capability tiering (compose with **P9**).

**Why this beats competing with Khanmigo.** North Carolina is spending **$10M+
recurring, sole-sourced** on Khanmigo (SB 1006). The tutor is bought; the
**oversight, integration and evidence layer around it is not**, and every statute
above requires one. Sell the gate, not the tutor.

## P12 — Pedagogy-aware model selection and tutor evaluation

Added in the fourth pass of 2026-10-06. Short, cheap, and it answers a question
clients ask in week one that this KB previously could not answer with evidence:
**"which model should teach?"**

**Use when:** scoping any tutoring or content build, and whenever a client asks you
to justify a model choice — or when a regulator asks how tutoring quality is
measured.

**Outcome:** a defensible model choice backed by pedagogical measurement rather
than general-purpose benchmarks, plus a repeatable harness for scoring tutor
behaviour as the deployment evolves.

**Wiring:**
1. **Score candidate models on pedagogical knowledge, not task accuracy.**
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (**MIT**, 12★) evaluates models against **real teacher-qualification exam
   questions**. A model that tops a reasoning leaderboard can still not know how to
   teach, and this is the only instrument in this KB that distinguishes the two.
2. **Score the deployed tutor's *dialogue* on a rubric you re-implement yourself.**
   The one published scheme for this is `AITutor-EvalKit` (EACL 2026):
   **MI** (Mistake Identification), **ML** (Mistake Location), **PG** (Providing
   Guidance), **AC** (Actionability). **Re-implement the four dimensions; do not
   vendor the code** — its paper claims MIT but the repository has **no `LICENSE`
   payload on either branch**, which leaves it legally unlicensed. The rubric is
   published research and free to apply; the code is not safe to ship.
   Filing an issue upstream asking for a `LICENSE` is a cheap, high-value
   contribution — do it at the start of the engagement and the blocker may clear
   before delivery.
3. **Evaluate the voice path separately where it is the primary modality.**
   [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework)
   (MIT) — relevant wherever literacy, device cost or bandwidth binds, which is the
   **LATAM offline-first (P5)** and **African** context rather than the EMEA one.
4. **Run it as a regression gate, not a one-off.** Wire both scores into CI over a
   fixed dialogue set and trace with Langfuse (MIT, minus the `ee/` paths). A model
   or prompt change that lowers PG or AC should **fail the build**; otherwise
   tutoring quality silently decays and nobody can date the regression.

**Effort:** 1–2 weeks as a scoping add-on; 3–4 weeks to run as a standing CI gate.

**Caveat, stated plainly:** these are **1–12★ research-grade repositories**. Vendor
them deliberately, read the code before trusting a score, and expect to maintain
your fork. They are in this KB because they are the only permissive options that
exist for these two functions — not because they are robust.

## P13 — The EU AI Act education profile (the December 2026 / December 2027 split)

Added in the fifth pass of 2026-10-06. **This is the highest ratio of billable
clarity to engineering effort in this KB**, and it has a deadline weeks away.

**Use when:** the client deploys AI anywhere near European education — admission
and access, evaluation of learning outcomes, student level placement, or exam and
behaviour monitoring (Annex III point 3). Also use it as the opening diagnostic on
any EMEA education account, because most of them now believe the deadline was
cancelled.

**The fact the engagement turns on.** **Regulation (EU) 2026/1744** (in force
27 July 2026, CELEX 32026R1744) moved Annex III stand-alone high-risk obligations
from 2 August 2026 to **2 December 2027**, and Annex I embedded to 2 August 2028.
**Article 50 transparency did not move: the watermarking and
synthetic-content-marking deadline is still 2 December 2026.** Clients who heard
"delayed" deferred the labelling work along with the conformity work. The labelling
work is the one that is imminent.

**Outcome:** two deliverables with two dates. **(A)** By December 2026 — every AI
interaction disclosed, every generated artefact marked, every system classified.
**(B)** By December 2027 — Annex III conformity evidence: technical documentation,
risk management, data governance, human oversight, conformity assessment, CE
marking, EU-database registration.

**Wiring:**
1. **Classify first, with the MIT toolkit, not a spreadsheet.**
   [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit)
   (**MIT**, TypeScript, 98 commits) walks the Act's decision tree across six risk
   tiers and emits **61 conformity checklist items** plus **8 document templates**.
   Run its CLI — `npx @eu-ai-act/cli classify`, then `checklist`, then `gaps` —
   over every AI system in the estate. Its web UI is **client-side only, with no
   backend**, which matters: you can hand it to a client's compliance team without
   a data-processing conversation.
2. **Write the education profile. This is the billable artefact and it does not
   exist anywhere.** The toolkit has **no education content and never mentions
   Annex III point 3**. Map its four education categories — admission/access,
   learning-outcome evaluation, level placement, exam/behaviour monitoring — onto
   the 61 checklist items, as a data file in the toolkit's own shape. Ship it as a
   **pull request upstream** as well as a client deliverable: it costs nothing
   extra, and a merged education profile in the canonical MIT toolkit is a
   positioning asset no competitor can take back.
3. **Do the December 2026 labelling work now, because it is small.** Every
   generated lesson, item, feedback string and tutor turn carries a
   machine-readable marker and a learner-visible disclosure. Make it structural
   rather than a convention: reuse **P11 step 3** — artefacts carry non-optional
   `ai_generated`, `disclosure_shown` and `marked_at` fields via
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT), so an
   unlabelled artefact fails to construct.
4. **Generate the Annex III evidence from traces you are already keeping.**
   [langfuse/langfuse](https://github.com/langfuse/langfuse) (MIT — stay out of
   `ee/`, `web/src/ee/`, `worker/src/ee/`) is the technical-documentation and
   human-oversight record. The checklist items from step 1 tell you exactly which
   spans you must be able to produce.
5. **Measure the model against the Act's data-governance and robustness asks.**
   [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) (**Apache-2.0**, ETH
   Zurich) pairs a technical interpretation of the Act with a benchmarking suite.
   It is the measurement half of step 1's checklist half.
6. **Keep the human gate from P11.** Annex III human-oversight evidence and the
   gate are the same artefact. Do not build two.

**Effort:** 2–3 weeks for classification plus the education profile on an estate
of a handful of systems; 4–5 weeks to add the December 2026 labelling layer;
10–12 weeks for the full Annex III evidence programme (compose with **P4** and
**P11**).

**Verify before you quote.** EUR-Lex and the Commission's notice are unreachable
from the environment this KB is built in. Every date here is corroborated across
several independent legal analyses and the CELEX id is given for one-step
verification — **check it against EUR-Lex before it reaches a client.**

## P14 — ASEAN: the permissive LMS under the closed products

Added in the fifth pass of 2026-10-06. For Singapore, Malaysia and the wider SEA
higher-education and polytechnic market.

**Use when:** the client is an ASEAN institution teaching **programming or
computer science**, wants to own and rebrand its platform, and has engineering
capacity. Also use it when a client has seen Singapore's AICET products and asked
for "that, but ours."

**The situation.** Singapore has APAC's most operationally mature education AI and
**none of it is forkable**: AICET's **Codaveri** (30,000+ pieces of personalised
programming feedback since 2024), **Softmark** (70,000+ exam scripts in 2025, with
computer-vision grouping of similar answers) and **ScholAIstic** (educators
authoring their own roleplay chatbots, deployed across Social Work, Law and
Nursing at NUS since June 2024) are closed, ministry-funded products. The LMS
beneath Codaveri is **MIT**.

**Outcome:** a client-owned, rebrandable CS-teaching platform with an agent
side-car, built on a permissive substrate that already carries an autograder and
gamification — with the AICET deployment cited as the proof the shape works.

**Wiring:**
1. **Fork [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2)**
   — **MIT, read from `master/LICENSE`, 158★, 78 forks, 15,802 commits.** Note the
   default branch is `master`; `main/LICENSE` 404s. Three components, not one:
   Rails 8 API, React client, **Keycloak** auth. Scope the Keycloak-to-client-IdP
   work in week one; it is the integration that surprises teams.
2. **Size the concentration risk out loud, in week one.** 158★ means a small
   contributor base and realistically NUS-dependent maintenance. If the client's
   engineers will not own the fork, **stop and propose Moodle instead** — this
   pattern is wrong for them. Trading copyleft for a maintenance cliff is only a
   good trade when somebody is standing at the top of it.
3. **Put the tutor beside it, not inside it.** Build the programming-feedback
   agent as a side-car against Coursemology's own submission and assignment
   models — the **P1** shape — so platform upgrades and agent iterations stay
   independent. Codaveri is the existence proof that this integration point works
   at scale on this codebase.
4. **Gate the grading with P11.** Korea's **AI Basic Act** (in force **22 January
   2026**) requires human oversight and documentation for high-impact systems, and
   **Australia's TEQSA** requires an institutional genAI action plan from every
   higher-education provider. The gate is the deliverable both ask for.
5. **Clear model rights per model, never per repository.** If the client wants a
   SEA sovereign model, [aisingapore/sealion](https://github.com/aisingapore/sealion)
   has **no repository `LICENSE` payload** and its README states terms vary by base
   model — Llama3-derived variants restrict commercial use, Gemma-derived variants
   differ. Clear each **Hugging Face model card**, per release, and put the
   result in the decision log. **MaLLaM** (Malaysia, with NVIDIA, 3M+ users via
   YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL** (March 2026) are the current
   candidates.
6. **The ScholAIstic-shaped gap is the follow-on sale.** No permissive project
   anywhere in this KB lets a **non-technical educator author and publish their
   own agent**. P8 produces Agent Skills *for* educators; it does not give them an
   authoring surface. Build that on top of this platform and it is a product, not
   a project.

**Effort:** 8–10 weeks for a branded fork with IdP integration and one side-car
tutor; +4 weeks for the gated-grading layer.

**Why it beats greenfield.** The autograder, submission pipeline, gamification and
a decade of commits are already there under a licence that lets the client resell
the result. Rebuilding that to avoid a 158★ dependency is the more expensive risk.

## P15 — Curriculum-aligned item generation under a sovereignty constraint

Added in the fifth pass of 2026-10-06. India-first, and portable to any
jurisdiction with a national curriculum body and a data-residency requirement.

**Use when:** the client is a ministry, board, state system or publisher that
needs assessment items and lesson material **aligned to a named national
curriculum**, cannot send student or textbook data to a frontier API, and will be
asked in week one whether the output infringes the curriculum body's copyright.

**Outcome:** curriculum-tagged lesson plans, items and marking keys, generated on
open-weight models the client can host, with a written copyright position and a
human-curator gate — i.e. the three things that stop this kind of programme, all
answered.

**Wiring:**
1. **Take the teacher-side workflow from
   [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot)**
   (**MIT**, Microsoft Research India / VELLM, validated with the **Sikshana
   Foundation**). Two things specifically: the **selection model** —
   curriculum → grade → subject → chapter, which is how a teacher actually thinks
   and how the artefact must be tagged — and the **ingestion pipeline gated by
   human curators**, which is the answer to "where did the source material come
   from?" Its output set is the right target too: lesson plans, real-world
   examples, analogies, hands-on activities, formative and summative assessments,
   exported to **DOCX, PPT and handouts**, plus multi-chapter question banks
   against blueprint formats. **Note its own declared GPT-4o dependency** and
   replace that layer in step 2.
2. **Take the sovereignty and copyright posture from
   [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI)**
   (**MIT**, CBSE/NCERT grades 9–12). It runs on **open-weight Gemma only**
   (`gemma-4-26b-a4b-it`, failover `gemma-4-31b-it`, temperature 0.2, explicitly
   zero Gemini), routes every model call through a backend so keys never reach the
   browser, and ships a **written copyright argument**: no curriculum-body text is
   stored or reproduced, syllabi and blueprints are treated as public standards,
   and every item is synthesised on demand. **Reuse the argument even when you do
   not reuse the code** — it is the artefact that unblocks procurement.
   *(0★, 7 commits: read it, do not pin it.)*
3. **Serve the weights yourself.** [ollama/ollama](https://github.com/ollama/ollama)
   or [vllm-project/vllm](https://github.com/vllm-project/vllm) inside the
   client's boundary. Low temperature and structured pedagogical prompts are doing
   real work here; keep both.
4. **Make curriculum tags and provenance structural**, via
   [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) (MIT): every
   item carries non-optional `curriculum`, `grade`, `subject`, `chapter`,
   `blueprint_section` and `generated_by`. Untagged items are exactly the ones that
   fail an audit.
5. **Gate it with P11 and label it with P13.** The human gate satisfies the
   oversight rules; the labelling satisfies Article 50 if any of this touches
   Europe.
6. **Evaluate the teaching, not the answer.** Re-implement the MathTutorBench
   rubric (trend 18 — read it, do not vendor it) and use
   [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark)
   (MIT) to pick which open-weight model teaches best, per **P12**.

**Effort:** 6–8 weeks for one board, one grade band and one subject, self-hosted;
+3–4 weeks per additional subject once the tagging schema is settled.

**Portability.** The pattern is curriculum-shaped, not India-shaped. Substitute the
curriculum body and it serves the UAE's seven-area mandate — which this KB records
as having **no curriculum-aligned permissive pipeline at all** — or any LATAM
ministry, where **P6** should precede it (see `intel/market.md`: 87% of LAC
institutions use AI and only 26% have a strategy for it).

## P16 — The all-MIT national/state stack (APAC, India shape)

Added sixth pass, 2026-10-06. **The only pattern in this KB whose every component
is MIT** — platform, language layer, orchestration and review tool. That matters
because it removes the licence conversation from a public-sector procurement
entirely.

**When to propose it:** a ministry, state education department or large public
system in India or an Indic-language market, where curriculum alignment and
multilingual delivery are requirements rather than features.

| Layer | Component | Licence (payload) |
|---|---|---|
| Platform | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** (`master/LICENSE`) |
| Deployment | [project-sunbird/sunbird-devops](https://github.com/project-sunbird/sunbird-devops) | **MIT** |
| Translation | [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** (`main/LICENSE`) |
| Speech out | [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | **MIT** (`master/LICENSE.txt`) |
| Speech in | [AI4Bharat/IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) | **MIT** (`main/LICENSE`) |
| Teacher review | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |
| Orchestration | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **MIT** |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | **MIT** |
| Inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Lesson generation | [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) | **MIT** — India-built, teacher-side, human-curated by design |

**Wiring.** Sunbird is the system of record and the delivery surface; do not fork
it. Lesson generation runs as a side-car on the Shiksha Copilot shape — curriculum
→ grade → subject → chapter, producing lesson plans, examples, activities and
assessments. LangGraph orchestrates with checkpoints as the audit trail;
pydantic-ai schema-checks every generated item so a malformed assessment cannot
reach a learner. **Shoonya is the mandatory gate**: no generated item publishes
to Sunbird without a named teacher's approval recorded against it. IndicTrans2
translates the approved artefact into the 18+ languages Sunbird already serves;
Indic-TTS voices it; IndicWav2Vec takes spoken answers back. Ollama keeps all
inference inside the ministry's own infrastructure.

**Sequence:** Sunbird + DevOps stand-up (4–5 wk, the real cost — 100+
micro-services) → generation side-car and schema contracts (3 wk) → Shoonya review
loop with named approvers (2 wk) → language layer, two languages first (3 wk) →
remaining languages (1 wk each, parallel). **12–14 weeks** to a reviewed,
multilingual pilot.

**Say this in the pitch:** every line of this stack is MIT, so there is no
copyleft obligation, no per-seat licence and no vendor in the critical path — and
the platform is already a recognised **Digital Public Good** running at national
scale. **Do not propose this outside Indic markets:** NCERT/CBSE/SCERT alignment
is embedded, and undoing it costs more than starting from Coursemology.

## P17 — Oral reading fluency assessment (two repositories in the whole category, one of them MIT)

Added sixth pass, 2026-10-06. This is the one pattern here that builds into a
**declared void**: oral reading fluency (ORF) is the highest-volume literacy
measurement in primary education and **every system doing it is proprietary** —
FLORA, Literably, Amplify Text Reading Online, SoapBox Labs, none with a public
repository. The permissive components all now exist.

**The measurement:** a child reads a grade-levelled passage aloud; the system
returns **words correct per minute (WCPM)**, accuracy, and a per-word error list a
teacher can inspect.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Transcript | [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **MIT** (`master/LICENSE`) | CTranslate2 build — faster and lighter than reference Whisper, same weights |
| Word timings | [m-bain/whisperX](https://github.com/m-bain/whisperX) | **BSD** (`main/LICENSE`) | **The load-bearing choice.** WCPM is a rate, so it is uncomputable without word-level timestamps |
| Offline variant | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) | Same measurement on a tablet or Pi with **no connectivity**, where the assessment is most needed |
| Alignment/scoring | your code | — | Align transcript against the known passage; classify omissions, insertions, substitutions, self-corrections |
| Evidence trail | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT** (with carve-out) | Every scored attempt traceable — an assessment decision must be defensible |
| Teacher override | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** | Human adjudication of disputed words; the scores it corrects become your eval set |

**Wiring.** The passage is known in advance, which makes this far more tractable
than open transcription: you are doing **forced alignment against a reference
text**, not open-vocabulary ASR. faster-whisper produces the transcript, whisperX
attaches word-level timestamps, your aligner diffs transcript against reference
and emits WCPM plus a typed error list. **The teacher's judgment is final** — the
system proposes a score and a teacher confirms or overrides it, which is also what
keeps it on the right side of US state law (trend 16) and the EU AI Act's
human-oversight requirement for education (trend 17; P13).

**Evaluate against a public baseline, and say the number.** The **Ghana ORF
Dataset** is publicly available — 130 students aged 9–18, original passages, audio
and human transcriptions — and the published baseline is **Whisper V2 at 10.3%
WER** on Ghanaian students reading aloud (*IJAIED*,
[10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)). Report
agreement with human raters, not WER alone: the client cares whether the system
and a trained rater assign the same WCPM.

**Sequence:** aligner and WCPM scorer against the Ghana dataset (3 wk) →
human-agreement evaluation and error taxonomy (2 wk) → teacher override UI and
Langfuse trail (2 wk) → offline build on sherpa-onnx (2 wk) → classroom pilot
(3 wk). **10–12 weeks** to a measured, reviewable assessor.

**Two warnings.** Accented and child speech is where ASR degrades most, so **the
evaluation is the deliverable** — a fluency score nobody has validated against
human raters is worse than no score. And ORF is **high-stakes assessment**: in the
EU this is Annex III point 3 territory, so run it through P13 before it touches a
real pupil.

### P17 update, tenth pass of 2026-10-06 — the void has prior art and a funded competitor

Two corrections to the framing above, both measured this pass.

**1. "No open competitor" is no longer accurate — there is prior art, and it is
MIT.** The whole GitHub result set for `oral reading fluency assessment speech` is
**two repositories**:

| Repo | Licence (payload) | ★ | Relevance to P17 |
|---|---|---|---|
| [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody) | **MIT** (`main/LICENSE`, full text read) | 0 | **Implements this pattern's core loop already**: aligns speech to reference text at word level, reports accuracy and WER, **speaking rate in WPM**, misread/omitted/inserted words, and a fluency score from pause pattern and pace. Whisper for ASR, **Levenshtein alignment**, Groq for transcription. Python, **1 commit**. |
| [mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) | **no payload** (20 URLs) | 0 | Oral reading + comprehension support, TypeScript. Unusable — repository exists, grant does not. |

**Use `prosody` as a reference implementation, not as a dependency.** One commit
and zero stars is not a maintained component, and the licence permits reading it
freely. What it gives you is a **validated shape** for the aligner-and-scorer stage
that the table above leaves as "your code": Levenshtein alignment against the
reference passage, with fluency derived from pause pattern as well as rate. That is
a day of reading that removes a week of design.

Note also that `prosody` calls the **Groq API** for transcription. For the P17
build keep `faster-whisper`/`whisperX` local — the offline and data-residency
properties are the reason this pattern exists.

**2. The funded competitor now has a name, and it is the closest match in the
whole $26M programme.** **Harvard University (Ying Xu)** is a Cohort 2 grantee for
**"OpenLiteracy: An Open-Source AI Infrastructure Suite for Advancing Speech
Foundation Models for Early Word Reading Assessment and Instruction"** (Tier 2),
under the programme's **Apache-2.0-or-better licence floor**. **GitHub returns 0
repositories for `OpenLiteracy`** (Tier 1, 6 Oct 2026) — funded, named, not
shipped.

**What this does to the sequence: nothing, and that is the point.** The 10–12 week
build above stays as specified, because the deliverable that survives OpenLiteracy's
arrival is the **evaluation and the error taxonomy**, not the ASR stack. Structure
the engagement so the transcript-and-timestamp stage is replaceable behind an
interface (**P23**'s socket discipline), and OpenLiteracy becomes a drop-in upgrade
to a validated harness instead of a reason the client's project was wasted.

**And state the licence floor to the client.** Anything the programme funds must be
**at least as permissive as Apache-2.0**, so the upgrade path is contractually safe
to promise — which is a rare thing to be able to say about a dependency that does
not exist yet.

## P18 — Offline voice tutoring (P5 with a voice, LATAM and low-connectivity)

Added sixth pass, 2026-10-06. **Supersedes the voice question left open in P5.**
P5 established offline-first delivery as an equity requirement; it had no
permissive way to make the tutor speak or listen. It does now.

| Layer | Component | Licence (payload) |
|---|---|---|
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`LICENSE`) |
| Content pipeline | [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | **MIT** |
| **Voice, all of it** | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) |
| Higher-quality TTS | [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | **MPL-2.0** (`main/LICENSE.txt`) — the **live fork**, not `coqui-ai/TTS` |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Local retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence — permissive |
| Portuguese model | [Polygl0t/Polygl0t](https://github.com/Polygl0t/Polygl0t) / Tucano 2 | **Apache-2.0** (`main/LICENSE`) |

**Wiring.** Kolibri serves content on a classroom server with no internet;
ricecooker packages the curriculum into channels. **sherpa-onnx provides STT, TTS,
diarization and VAD from a single Apache-2.0 dependency** on the same box — a Pi,
a low-end laptop or an Android tablet — so a learner speaks, is transcribed, gets a
spoken reply, and nothing leaves the room. Ollama runs the tutor model locally;
pgvector keeps retrieval in the Postgres instance already there, with no separate
vector store to host. For Brazil, Tucano 2 (Apache-2.0, 0.5–3.7B) is the
Portuguese-native option and the small sizes are the point on this hardware.

**Why sherpa-onnx and not Piper.** Piper is the better-known offline TTS and the
obvious reach — **and [rhasspy/piper](https://github.com/rhasspy/piper) (MIT) has
been archived read-only since 2025-10-06**, with development moved to
[OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl) under **GPL-3.0**.
Frozen or copyleft, no third option. sherpa-onnx is Apache-2.0, maintained
(2,092 commits), and covers three more capabilities besides. If a client
specifically wants Piper voices, make the frozen-vs-GPL trade explicit in writing
before committing.

**Sequence:** Kolibri + content channels (2 wk) → local inference and retrieval
(2 wk) → sherpa-onnx voice loop with push-to-talk and VAD (3 wk) → language/model
selection and pedagogical tuning (2 wk) → offline-hardware field pilot (3 wk).
**10–12 weeks.**

**The honest regional caveat.** For Spanish and Portuguese this works today. For
most of the world's teaching languages **it does not** — the permissive language
layer exists for Indic languages (MIT) and six Ugandan languages plus Masakhane's
continental MT (Apache-2.0/MIT), **and, added in the seventh pass, ASEAN:
Vietnamese, Thai, Malay and Indonesian (Apache-2.0/MIT — see P19)**. Outside
those three regions, essentially nowhere. Check the target
language against `repos/foundations.md` **before** promising mother-tongue
delivery; where it is missing, the honest scope is data collection first, and
`SunbirdAI/salt` is the model for how that was done well.

## P19 — ASEAN mother-tongue tutor on an all-permissive national stack

Added seventh pass, 2026-10-06. **This pattern did not exist before this pass
because the KB believed its language layer did not exist.** The sixth pass
recorded ASEAN as having no permissive self-hostable language layer, having
searched for sovereign models and correctly found
[SEA-LION](https://github.com/aisingapore/sea-lion) carrying no repository-level
grant. Searching for **toolkits** instead returns a full shelf.

**Every layer below is MIT or Apache-2.0, read from payload on 2026-10-06.**

| Layer | Component | Licence (payload) |
|---|---|---|
| LMS substrate | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`) — NUS-origin, 15,802 commits |
| Pedagogy engine | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** (`main/LICENSE`) — BKT + FSRS + prerequisites + misconceptions |
| **Language — Vietnamese** | [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** (`main/LICENSE`) — 1.8k★, 13 tasks incl. diacritics restoration |
| **Language — Thai** | [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** (`main/LICENSE`) — 1.2k★, 6,649 commits, subword tokenization |
| **Language — Malay** | [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** (`master/LICENSE`) |
| **Voice — Malay only** | [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** (`master/LICENSE`) |
| **Language — Indonesian** | [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** (`master/LICENSE`) — 143 datasets |
| Voice runtime (all other languages) | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) |
| Local inference | [ollama/ollama](https://github.com/ollama/ollama) | **MIT** |
| Human review stage | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |

**Wiring.** Coursemology holds courses, submissions and roster and is the system
of record. `tutor-mcp` runs as an **external MCP side-car** — the licence
boundary from `agents/top.md` applies here as everywhere: the pedagogy stays MIT
because it never enters the LMS tree — and owns mastery state (BKT), review
scheduling (FSRS) and the prerequisite graph. The **language toolkit for the
target country sits in front of the model**, doing the work a frontier model does
badly in these languages: `pythainlp` tokenizes Thai (which has no spaces between
words, so this is not optional); `underthesea` restores diacritics and segments
Vietnamese; `malaya` normalizes and tags Malay. Ollama serves the tutor model
locally. For spoken practice, **Malay routes through `malaya-speech`; everything
else routes through `sherpa-onnx`** and must be accuracy-tested per language.
Shoonya is the annotation and review stage for the curriculum corpus — which in
Vietnam is also a compliance artefact, see **P20**.

**Why this is the clearest build-and-own opportunity in APAC outside India.**
The fifth pass established that ASEAN's operationally mature education AI is
**closed** — AICET's Codaveri, Softmark and ScholAIstic run at ministry scale
with no public repository — over an **MIT substrate**. Add the language shelf and
the asymmetry is unusually favourable: **the LMS layer is MIT, the language layer
is Apache-2.0/MIT, and the national-language pedagogy layer is unbuilt by anyone,
open or closed.** There is no incumbent to displace and no licence to negotiate.

**Sequence:** Coursemology deployment and roster integration (3 wk) → `tutor-mcp`
side-car wired over LTI/MCP with mastery state (3 wk) → language toolkit
integration and per-language quality evaluation (3 wk) → curriculum corpus
ingestion through Shoonya review (3 wk) → voice layer, Malay first (2 wk) →
classroom pilot (3 wk). **15–17 weeks.**

**Three honest constraints — state all three in the proposal.**

1. **None of the language shelf is education-specific.** These are general
   toolkits, exactly like AI4Bharat. They make a mother-tongue tutor possible;
   the pedagogy is yours to build. That is the opportunity and also the cost.
2. **Voice is Malay-only on the regional shelf.** Thai, Vietnamese and Indonesian
   have the text layer and no local permissive voice layer. Do not promise spoken
   practice in those three until `sherpa-onnx` or Whisper has been measured on
   the target language with real learner audio.
3. **`nusa-crowd` and `indonlu` are corpora and benchmarks, not runtimes.** For
   Indonesian the shelf gives you data and evaluation, not a deployable
   component. Scope Indonesian as a heavier build than Thai or Vietnamese.

**Do not use `malaysia-ai/malaysian-dataset`** (345★, the organisation's second
most-starred repo) — **no `LICENSE` payload**, while both its code siblings are
MIT. And do not treat SEA-LION as a blanket-licensed option: its grant lives on
each HuggingFace **model card**, so licence review there is **per checkpoint and
recurring**.

## P20 — The corpus-provenance gate (Vietnam Decree 33, and the artefact every regime now wants)

Added seventh pass, 2026-10-06. **P13 is the EU AI Act education profile, built
around the *decision* an AI makes about a learner. This pattern covers the axis
P13 does not have: the *provenance of the corpus*.**

**The rule that creates it.** Vietnam's **Decree 33** (signed 2026-06-30, in
force 2026-08-15), implementing Law No. 134/2025/QH15, lists 46 high-risk AI
systems across six sectors. Its **first** education category is AI providing
**self-learning content from uncontrolled data sources** — so a RAG tutor is
high-risk **even if it grades nothing, ranks nobody and monitors no one**. EU
Annex III point 3 has no equivalent category. **This reaches the default
architecture in this KB directly:** every RAG tutor in `agents/top.md`, and the
ingestion pipeline in **P2**, are in scope in Vietnam on corpus grounds alone.

| Layer | Component | Licence (payload) |
|---|---|---|
| Ingestion + item generation | **P2** pipeline as built | — |
| Human curation gate | [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) |
| Grading human-gate reference | [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) | **MIT** (`main/LICENSE`) — writes `readyforreview`, never releases |
| Risk-tier classification + checklist | [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** — six tiers, 61 conformity items, CLI + SDK |
| Model-call trace | Langfuse (as used by [Selleo/mentingo](https://github.com/Selleo/mentingo), **MIT**) | per Langfuse terms — check before shipping |
| Signed provenance | C2PA tooling as recorded in `intel/trends.md` | per implementation |

**The deliverable is a source manifest, and it is billable.** For every document
in the tutor's corpus, record: **what** was ingested (hash and version), **from
where** (URI, publisher, retrieval date), **under what rights** (licence or
permission, with the payload read rather than the badge), **who reviewed it**
(named human, timestamp, approve/reject), and **which generated artefacts derive
from it** (so a withdrawn source can be traced forward to every item it
produced). Shoonya is the only shelved permissive implementation of the review
stage; the rest is schema and plumbing.

**Wiring.** P2 ingests as before, but nothing enters the retrieval index until it
carries a manifest row with a review decision — **fail-closed, on the pattern
`moodle-grading-mcp` uses for grades**: writes require an explicit enable flag
*and* a non-empty allowlist, and every attempt, denial and success is appended to
an audit log. Generated items inherit their sources' manifest IDs, so a
conformity assessor can ask "where did this question come from?" and get an
answer without a code reading. The `eu-ai-act-toolkit` CLI produces the risk-tier
classification and checklist artefacts; run it in CI so the compliance evidence
regenerates with the corpus rather than being assembled once before an audit.

**What it buys you in each region — this is the reason to build it once.**

| Region | What the manifest satisfies |
|---|---|
| **APAC** | Vietnam Decree 33 category 1 directly — the conformity assessment consumes exactly this. Report the risk level to the **Ministry of Science and Technology before use**; assessment before deployment and **maintained throughout** |
| **EMEA** | EU Annex III point 3 data-governance and technical-documentation obligations under P13, and the copyright question every ministry engagement asks in week one |
| **North America** | California **AB 1159** — student data must not train models — is a provenance question in the other direction, and the same manifest answers it |
| **LATAM** | The governance deficit is the measured regional opportunity: **87% of institutions using AI, 26% with a formal strategy, under 10% with formal guidelines.** This is the artefact that closes that gap, and it sells without any regulation compelling it |

**Sequence:** manifest schema and rights-capture fields (1 wk) → Shoonya review
loop with named reviewers (2 wk) → fail-closed index gate with audit log (2 wk) →
forward-tracing from source to generated item (2 wk) → `eu-ai-act-toolkit` run
wired into CI (1 wk) → conformity-assessment dry run against Decree 33's three
education categories (2 wk). **10 weeks**, and it is reusable across every
subsequent engagement in the practice.

**Two things to get right.**

- **Vietnam's biometric narrowing is an opportunity, not a loophole to lean on.**
  Decree 33 category 3 is qualified to behaviour monitoring **using biometric
  data**, so non-biometric analytics — time on task, attempt counts, mastery
  curves — sit outside it, unlike the EU's broader "behaviour monitoring". Scope
  analytics more freely in Vietnam **and** keep the human gate on consequential
  scores regardless: category 2 still captures automated evaluation and ranking.
- ⚠️ **Verify Decree 33 against its own text before this reaches a client.**
  Every legal-publisher domain carrying it is **EGRESS_BLOCKED** in this
  environment (6/6 refused). The three education categories here come from **two
  independently-phrased searches that agreed on all three**; the **biometric**
  qualifier appeared in only one of the two and is the least-confirmed element in
  this pattern. The *engineering* is sound whatever the decree says in detail —
  a source manifest is required by EMEA and useful in all four regions — but do
  not quote the categories as law without reading the law.

## P21 — The LATAM productionisation engagement (a published spec + a working offline core)

**Added in the eighth pass of 2026-10-06.** This pattern exists because the
LATAM gap changed shape: the region has published **the design and the licence,
not the product**. P21 is the engagement that closes that distance, and every
component is MIT and locally authored.

**Use it when:** a LATAM client (Colombia, Chile, Peru, Brazil) wants a tutoring
or practice system for low-connectivity public education, and wants local
provenance in the architecture rather than a US SaaS wrapper.

### Components

| Role | Component | Licence | Why this one |
|---|---|---|---|
| **Requirements baseline** | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) `docs/TutorIA_Requerimientos.pdf` + `docs/tutoria_architecture.svg` | **MIT** © Grupo Sirius | **13-page spec, v1.0 April 2026**, RF-01…RF-20 + RNF-01…RNF-10, 5-layer architecture. Universidad Tecnológica de Pereira. **The only citable LATAM-authored education-AI requirements document in this KB** |
| **Offline delivery platform** | [learningequality/kolibri](https://github.com/learningequality/kolibri) (+ `kolibri-installer-android`) | **MIT** | Purpose-built, deployed, maintained offline-first LMS; the Android build is the 2 GB-RAM target |
| **Offline-sync reference** | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) (EduFlow) | **MIT** © CAi UC — **holder flagged** | ~41 commits showing room-code + IndexedDB + Service Worker + auto-sync in readable form. **Read it; do not vendor it** until the holder is cleared |
| **LMS integration surface** | Open edX XBlock / plugin | AGPL-3.0 (platform) — side-car stays separate | The integration shape TutorIA's RF-01 specifies |
| **Portuguese language layer** | [neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert) | **MIT** © NeuralMind | **886★**, BERTimbau, BrWaC-trained. Brazil-origin, for pt-BR classification/NER/retrieval work |
| **Offline ASR / TTS** | [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) **Apache-2.0** (11,358 B) | 🟢 permissive, single grant | 🔵 **Re-picked, pass 24.** Was `vosk-api` + a Piper fork decision (`rhasspy/piper` **archived**, head commit **407 d**; `OHF-Voice/piper1-gpl` **GPL-3.0**). `sherpa-onnx` does **ASR *and* TTS** — plus VAD, keyword spotting and diarization — locally, on **Raspberry Pi and Android**, head commit **2026-10-06 (1 d)**. 🟢 **The Piper fork decision disappears**: one component, one permissive licence, no copyleft branch to argue about |
| **Human quality gate** | TutorIA **RNF-09** | **MIT** (as text) | *"Al menos **2 docentes por asignatura**"* must pass pedagogical review **before launch**. A written protocol with a quorum — the thing to ship while no automated evaluator exists |

### Wiring

1. **Adopt RNF-04 and RNF-05 as the acceptance criteria, verbatim.** Target
   **2 GB RAM / 3G**; implement **TLS** in transit and **AES-256** at rest under
   **Ley 1581 de 2012 (Habeas Data)**. These are the client's own regulator's
   terms, quoted from a Colombian university's specification — far stronger in a
   proposal than a vendor's own non-functional requirements.
2. **Deploy Kolibri as the delivery platform**, Android build first. Do not
   retrofit sync onto a network-assuming LMS (see `verticals/solutions.md`).
3. **Implement the sync core on EduFlow's design:** teacher-created room +
   6-character join code; assignment packaged as text (**~8 KB per 10
   exercises**); client-side **IndexedDB** store; **Service Worker** app-shell
   cache; queued answers flushed on reconnection. Re-implement from the design —
   the holder flag makes vendoring unsafe.
4. **Keep the agent as a side-car** behind the API layer of TutorIA's
   architecture (CAPA 3), so the Open edX AGPL-3.0 boundary is never crossed —
   identical to P1 and P7's rule.
5. **Gate every consequential output through RNF-09.** Two subject teachers per
   subject sign off before launch; log the sign-off. This is also the artefact
   that satisfies the US human-oversight statutes and EU Annex III if the client
   later operates across regions.
6. **Language:** Spanish-only for v1, per TutorIA's RNF-10. For pt-BR work add
   BERTimbau. **Do not promise indigenous-language support** — see the
   warning below.

### Deliverables

A Kolibri deployment with an offline-capable practice module, a side-car agent
behind the API layer, a signed pedagogical review record per subject, and a
compliance note citing **Ley 1581** with the TLS/AES-256 evidence.

### ⚠️ Two warnings that are the point of this pattern

**1. Do not promise Quechua, Guaraní, Aymara or Nahuatl.** TutorIA's RNF-10
names native languages as a future possibility and Latam-GPT lists them as
roadmap, so a client may well ask. **The capability exists and the rights do
not:** ten of twelve probed repositories in that layer — including **all four
probed AmericasNLP editions, whose 2024 shared task is literally "Creation of
Educational Materials for Indigenous Languages"**, the ASR covering Quechua/Guaraní/Bribri/Kotiria/Wai'khana,
and the Peru MT work — carry **no `LICENSE` payload**, and
`Llamacha/IWSLT2023_Quechua_data` serves an **Apache-2.0** file over data its
README licenses **CC BY-NC-ND**. Scope it as a **data-rights workstream**
(licence conversations with Llamacha, Siminchikkunarayku and the AmericasNLP
organisers) or scope it out. `vosk-api` + `speechbrain`, both Apache-2.0, give
you a permissive pipeline ready for licensed data when it exists.

**2. Latam-GPT is not open source.** If the client asks for the regional
sovereign model: it is **Llama 3.1 Community License** © Meta — **not
OSI-approved**, carrying an Acceptable Use Policy and the 700M-MAU clause.
Usable and genuinely good for Spanish/Portuguese grounding; **not
relicensable**, and it inherits Meta's AUP into the client's product. Do not let
it into a slide that says "open source stack". *(Licence is single-source in this
KB — confirm the model card; see `agents/top.md`.)*

## P22 — The licence-reliability gate (three points, run before any component enters a deliverable)

**Added in the eighth pass of 2026-10-06.** This is not an architecture pattern;
it is the check that protects every other pattern on this page, and it exists
because the eighth pass found **four live cases where this KB's own verification
method returns the wrong answer**.

**Use it when:** any repository is about to become a dependency, a vendored
component, or a named asset in a client deliverable. Always.

### The gate

| # | Check | How | Fails when |
|---|---|---|---|
| **1** | **Payload** | `curl raw.githubusercontent.com/<repo>/<branch>/LICENSE` across `main`/`master` × `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `license`, `license.txt`, `LICENCE` | No file → **no grant.** `AmericasNLP/americasnlp{2021,2023,2024}`, 9 of 11 LATAM indigenous-layer repos |
| **2** | **Asset scope** | Read the README's own licence section. Ask: *what is the thing of value here — code, or data/audio/corpus/weights?* | Payload governs the scripts, README governs the asset, and they disagree. **`Llamacha/IWSLT2023_Quechua_data`: Apache-2.0 payload, CC BY-NC-ND data.** The asset-scope statement is **controlling** |
| **3** | **Holder** | Read the copyright line. Does the holder belong to the project? | Holder is foreign or upstream → grant **inherited, not issued**. `MaybeItsAdam/tutors` (tldraw Inc.); **all 20 `caiuc/equipo-*` repos (© CAi UC, the organiser, not the authoring teams)** |

**Plus one question that no probe answers:** *is this open **source**, or open
**weights** under a bespoke licence?* **Latam-GPT** is described as open source
by the trade press, Brookings and **the European Commission's own Open Source
Observatory**, and is licensed **Llama 3.1 Community** — not OSI-approved. Model
releases are the standing exception to every licence heuristic on this page;
check the model card, never the coverage.

### Why run all three

Each check catches a case the others miss, and in this KB's measured sample each
one has a live failure attached:

- Payload alone → ships a **CC BY-NC-ND** corpus believing it is Apache-2.0.
- Payload + scope → ships 20 MIT repositories whose **copyright belongs to
  someone who did not write them**.
- All three → still calls a **Llama-licensed** model "open source" unless the
  weights question is asked separately.

### Outputs, and what to do with each verdict

- 🟢 **All three clean** → cleared for vendoring. Record repo, branch, filename,
  licence family, holder and probe date in the deliverable's licence register.
- 🟡 **Scope conflict** → usable for the layer the payload actually covers
  (usually scripts), **not** for the asset. Re-implement or license the asset
  separately.
- 🟡 **Holder mismatch** → **read-and-learn only.** Re-implement from the design.
  Clearing it is a question for counsel, not for another probe.
- 🔴 **No payload** → not a dependency. Two options, and the eighth pass
  established which is cheaper: file an upstream `LICENSE` issue
  (**retrospective**, one repo at a time), or — where the work has not been
  written yet — **get the licence into the rules**. CAi UC made an OSI licence a
  condition of hackathon evaluation and **20 licensed repositories appeared in
  eight hours**. For engagements touching LATAM's indigenous layer or MEA, that
  clause is the highest-leverage intervention in this KB. **Name the authors as
  holders, not the organiser** — CAi UC's own template got that wrong and
  flagged all 20 of its outputs at check 3.

## P22 update, thirtieth pass of 2026-10-07 — the fourth check: a licence claim has a SUBJECT, and the label may have been stripped of the qualifier that decides it

🔴 **Execution of this tree's instruments was DENIED this pass** (`[Code from External]`), so nothing
below is a re-measurement (`P107`); it is a first-hand reading of this KB's prose against pass 28's
29 flagged rows — **14 adjudicated, 0 contradictions**.

### Check 4 — subject, and the qualifier

| # | Check | How | Fails when |
|---|---|---|---|
| **4** | **Subject + qualifier** | For every licence family you are about to record: ask *whose* licence it is, and whether the label kept its **qualifier**. Compare the **full** string in the source prose against the family you are filing | The family belongs to a **neighbour** (successor, dependency, alternative, ancestor, doc layer, in-tree vs side-car), is a **refutation** (*"not MIT"*, *"WRONG"*, *"mis-reported"*), is a **query string** (`license:mit OR …`), or the label **lost its qualifier** — 🔴 **`CC BY-NC-ND 3.0` filed as `CC-BY` inverts the commercial answer** |

🔴 **The live case, and it is the same repository P22 check 2 already uses.**
[`Llamacha/IWSLT2023_Quechua_data`](https://github.com/Llamacha/IWSLT2023_Quechua_data) is recorded
in this KB's prose, in five places and with explicit scope-conflict warnings, as **payload
Apache-2.0 / README CC BY-NC-ND 3.0**. Pass 28's reconciler recorded its prose families as
`Apache-2.0, CC-BY` — **`NC` and `ND` dropped**. 🔴 **`CC-BY` permits commercial use and
derivatives; `CC BY-NC-ND` forbids both.** A register built from the flattened label clears a corpus
for a paid deliverable that its licence prohibits, and **the Quechua audio is exactly the asset an
engagement would want to fine-tune on.**

🔵 **This is pass 28's pre-registered action D confirmed by instance rather than by sweep.** Its
prediction was that a `CC-BY` label wrong 5 times in 7 is a commercial defect, not a vocabulary gap.
The sweep still has to run (it needs execution). **One confirmed instance is already enough to change
the gate**, which is why check 4 goes in now rather than waiting for the count.

### What check 4 catches that checks 1–3 do not

Checks 1–3 all ask *what does the source say?* Check 4 asks the two questions that make an answer
usable: **about whom**, and **with what qualifier**. Nine of the ten shapes found this pass are
subject errors — a family that is true, but true of something else:

| Shape | Example | The real subject |
|---|---|---|
| successor named in the sentence | `rhasspy/piper` **MIT, archived** → `OHF-Voice/piper1-gpl` **GPL-3.0** | the fork |
| dependency | `learningequality/kolibri` is **MIT** with *"two LGPL deps"* | the deps |
| either/or alternative | *Fairlearn (**MIT**) **or** AIF360 (**Apache-2.0**)* | the alternative |
| ancestor licence | `sakai`, `opencast` — **ECL-2.0** *is* **Apache-2.0** | both, truthfully |
| doc layer | `yongsoojoo/esd2026-agent-workflow` — MIT code, `LICENSE-docs` **CC BY 4.0** | the docs |
| in-tree vs side-car | `peancor/moodle-mcp-server` **MIT** outside Moodle's **GPL-3.0** tree | the boundary — **this is P1** |
| `Was` column of a correction table | `dequelabs/axe-core` is **MPL-2.0** | the superseded reading |
| refutation marker | `frappe/lms` is **AGPL-3.0, *not MIT*** | a mis-report being corrected |
| `license:` filter | `aryankeluskar/canvas-mcp` is **ISC** | a query string |
| 🔴 **stripped qualifier** | `Llamacha/IWSLT2023_Quechua_data` — **CC BY-NC-ND 3.0**, not `CC-BY` | **the commercial answer** |

### How to run it, concretely

1. **Record the full licence string, never the normalised family**, in the deliverable's licence
   register: `CC BY-NC-ND 3.0`, not `CC-BY`; `GPL-2.0`, not `GPL` (`P452` — the LGPL's linking
   exception does not exist in GPL-2.0, and seven rows on this shelf moved on that distinction).
2. **Attach the subject to every family you record.** One column: `applies-to = repo | deps | docs |
   fork | alternative | superseded | refuted | filter`. Anything not `repo` is **not** the component's
   licence.
3. **Treat a two-family row as a question, not a conflict.** Nine times in ten here it is one correct
   sentence about two things; the tenth is a stripped qualifier, and that one is the expensive one.
4. 🟢 **Prefer the prose over the table when they disagree.** This KB's standing record is **32 of
   33** in favour of the sentence a human wrote, for a structural reason: prose carries the scope word
   (`deps`, `docs`, `in-tree`, `README`) that a family column has nowhere to put.

## P23 — The benchmark-ready evaluation harness (build the socket before the plug exists)

> ⚠️ **Superseded in part by P27 (eleventh pass, 2026-10-06).** This pattern was
> written on the premise that no permissive evaluation harness and no pedagogy
> benchmark existed. Both were search artefacts: **Inspect** (MIT, 2,945★, UK AI
> Security Institute) and **Moonshot** (Apache-2.0, Singapore IMDA) are the harness,
> and four tutoring benchmarks exist — **none of them OSI-licensed**. Read **P27**
> for the corrected component list and the build-system rule that keeps a
> non-redistributable dataset out of the deliverable. The reasoning below about
> building the socket first still holds for the *rubric*; it no longer holds for the
> *runner*.

**Added in the ninth pass of 2026-10-06.** This pattern exists because of a fact
no earlier pass could state: **the permissive evaluation layer this KB has
declared missing since its fourth pass is funded, dated and licence-floored** —
and **has not shipped.**

**Use it when:** a client needs to evidence that its tutoring or assessment AI
works — for a procurement rubric, an EU Annex III file, a board, or a ministry —
and you have found (correctly) that **no Apache-2.0 tutoring-quality evaluator
exists today.** Measured 6 Oct 2026: `tutoring quality evaluation benchmark
license:apache-2.0` → **0 repositories.**

**The strategy:** do not build an evaluator and do not wait for one. **Build the
socket.** Twelve funded projects under a floor of *"at least as permissive as
CC-BY-4.0 (content) or Apache-2.0 (code/models)"* land through 2027; the
engineering job today is a harness whose benchmark layer is a swappable adapter,
so each one drops in as it publishes.

### Components

| Layer | Component | Licence | Status |
|---|---|---|---|
| Harness + adapter interface | **client-owned**, written Apache-2.0 to match the incoming layer | Apache-2.0 | you build this |
| Human quality gate (today's substitute for an automated one) | **TutorIA `RNF-09`** — pedagogical review by **≥2 subject-expert teachers per subject before launch** ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA)) | **MIT** | ✅ citable now |
| Speech scoring, where oral fluency is in scope | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`, payload-verified) | ✅ now |
| Content + curriculum grounding | [learningequality/kolibri](https://github.com/learningequality/kolibri) + [studio](https://github.com/learningequality/studio) | **MIT** | ✅ now |
| Interaction log (the artefact rubrics omit and regulators want) | client-owned, append-only | Apache-2.0 | you build this |
| **Benchmark slot 1** — science misconceptions in free-form responses | **Learning Equality** (PI Jamie Alexandre) | ≥ Apache-2.0 / CC-BY by grant condition | ⏳ funded 29 Jun 2026, 6–12 mo |
| **Benchmark slot 2** — multimodal formative assessment (**KB-TutorBench**) | **Stanford** (PI Hariharan Subramonyam) | ≥ Apache-2.0 / CC-BY | ⏳ funded, **0 repositories** today |
| **Benchmark slot 3** — ASR leaderboards for education | **National Tutoring Observatory / Cornell** (PI Allison Koenecke) | ≥ Apache-2.0 / CC-BY | ⏳ funded; org has a website, **no code** |
| **Benchmark slot 4** — multimodal formative-assessment dataset | **MMSA & TERC** (Heidi Cian, Ibrahim Dahlstrom-Hakki) | openly licensed per programme | ⏳ funded 21 Sept 2026 |
| Simulated learners for regression testing | **Princeton** (PI Tammy Kwan) — simulated student models | ≥ Apache-2.0 | ⏳ funded |

### Wiring

1. **Define one adapter interface** — `(items, model_under_test) → per-item
   scores + aggregate + provenance`. Every slot above is a dataset plus a scoring
   rule; an adapter that accepts both is all the abstraction needed. Resist a
   framework.
2. **Implement the human gate first, and ship it.** TutorIA's RNF-09 is MIT,
   citable, and the only pedagogical quality protocol in this KB. Two
   subject-expert teachers per subject, reviewing before launch, with sign-off
   recorded. **This is the deliverable that satisfies "human judgment is final"**
   (trend 16) and the oversight columns of the Maryland and Vermont rubrics.
3. **Stand up the interaction log on day one.** Append-only, per-turn, with model
   version, prompt provenance and the grounding documents cited. It costs little
   at the start and is unreconstructible later — and it is the artefact **no
   published US rubric requires and the EU profile does** (**P13**).
4. **Write one reference adapter against a public education benchmark you can
   legally use, to prove the socket works.** Do **not** use
   [AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) (33★, Chinese K12
   education evaluation) as a dependency — **it has no licence payload.** Read it
   for its criteria design, implement your own items, keep your implementation.
5. **Pin the slots in the architecture document by name, owner and expected
   window.** This is the part clients value: the gap is attributed and dated, not
   hidden.
6. **Re-probe the slots each quarter** with P22's gate before vendoring anything
   that lands. A grant condition is a promise about the licence; the **payload is
   still the proof**, and a funder's floor does not exempt a repository from
   checks 2 and 3 (asset scope and holder).

### Deliverables

- An Apache-2.0 harness with a documented adapter interface and one working
  reference adapter.
- A signed RNF-09-style pedagogical review record per subject.
- An append-only interaction log with provenance, plus a short output-generation
  disclosure.
- A **dated gap register**: each benchmark slot, its funded owner, its expected
  window, and what the harness does in the meantime.

### ⚠️ Three warnings that are the point of this pattern

1. **Do not present the funded pipeline as an existing shelf.** Nothing has
   shipped: `KB-TutorBench` → **0 repositories**, `learningequality` filtered on
   `benchmark` → **0 repositories**, the Cornell grantee's org → a website at 0★
   with no payload. Say *funded and expected*, never *available*.
2. **Every funder fact here is Tier 2.** `k12-ai-infrastructure.org` and
   `digitalpromise.org` are EGRESS_BLOCKED in this environment; **no RFP was
   read.** Confirm the licence floor against the primary document before it
   appears in a contract — the whole pattern rests on that one clause.
3. **Apache-2.0, not MIT, is the target licence for your harness.** The incoming
   layer is Apache-2.0 by grant condition. Matching it keeps combination trivial
   and gives the client the patent grant MIT lacks — the one case on this page
   where this KB recommends Apache-2.0 over MIT for new code.

## P24 — Procurement-rubric-ready delivery (North America, and the artefact pack that also clears the EU)

**Added in the ninth pass of 2026-10-06.** In the US the binding specification is
no longer only the statute — it is the **state-mandated evaluation rubric** the
district scores you against.

**Use it when:** the client is a US district, charter network, state agency or a
vendor selling into one — especially in **Maryland** (SB 720, effective 1 Jun
2026: state rubric, local policy within **120 days**, a designated **AI
coordinator**, ~24 districts on the clock for Fall 2026), **Vermont** (rubric of
23 Jan 2026), or **Idaho** / **Alabama** (statutory capability assessments and
pre-training verification).

**The insight:** the rubrics converge on seven criteria — educational value, data
privacy, usability and accessibility, cost, scalability, vendor reputation, age
restrictions — and they **omit** three things: an auditable interaction record,
disclosure of how outputs are generated, and evidence of bias/accuracy/
reliability evaluation. **Ship the omitted three and you exceed every published
rubric, pre-empt its next revision, and produce most of an EU Annex III file at
the same time.**

### Components

| Need | Component | Licence |
|---|---|---|
| Integration that *scores points* (39% of districts rubric-score interoperability) | **LTI + MCP side-car** per **P1** — no fork of the LMS | permissive by construction |
| No vendor training on student records (Idaho / Maryland / Alabama) | **self-hosted inference**, the sovereign stack of **P4** | — |
| Accessibility evidence | WCAG audit against the rubric's own accessibility criterion | — |
| Human-final decisions | **TutorIA RNF-09** review protocol ([LabSirius/TutorIA](https://github.com/LabSirius/TutorIA)) | **MIT** |
| Evaluation evidence | **P23** harness + dated gap register | Apache-2.0 |
| Offline/equity criterion, where present | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** |
| Proctoring, **only if** explicitly required | [AarambhDevHub/exam-cheating-detection](https://github.com/AarambhDevHub/exam-cheating-detection) (47★) or [vincenzo-afk/Proctored-MCQ-Exam-Platform](https://github.com/vincenzo-afk/Proctored-MCQ-Exam-Platform) (36★) | **MIT**, payload-verified |

### Wiring

1. **Obtain the actual rubric before designing.** Maryland's is state-published;
   Vermont's is in its January guidance. **Build the deliverable's evidence index
   as a one-to-one map onto the rubric's rows** — a reviewer scoring your bid
   should never have to search.
2. **Satisfy "no training on student records" architecturally, not
   contractually.** A contractual promise is a clause someone must trust;
   self-hosted inference (**P4**) is a fact they can inspect. Where a hosted model
   is unavoidable, isolate it behind the side-car so student records never cross
   the boundary, and document the boundary.
3. **Integrate via LTI + MCP (P1), never by forking the LMS.** This is now worth
   points, not just maintenance savings.
4. **Add the three missing artefacts** — interaction audit log,
   output-generation disclosure, bias/accuracy/reliability evaluation report (from
   **P23**). Name them in the bid as *exceeding* the rubric.
5. **Name the AI coordinator's workflow.** Maryland requires a designated
   coordinator; a tool that produces a report that person can actually file is
   differentiated from one that produces a dashboard they must interpret.
6. **Reuse the pack in EMEA.** The three omitted artefacts are substantially the
   Annex III evidence of **P13**. Build once, file in both regions — and note the
   direction of travel: **this is the first cross-region compliance reuse in this
   KB that runs from EMEA into North America**, because the EU profile is the
   stricter parent.
7. **Where proctoring is required, scope it carefully.** The MIT proctoring
   options are **18–47★ individual-scale projects**, not products: vendor the
   core, harden it, own it. Do **not** use `lebmatter/exampro` (72★, the
   framework-grade one) — **no licence payload**. And proctoring is biometric
   processing: it pulls the deliverable into Annex III in the EU and into the
   age-restriction row of the Vermont rubric.

### Deliverables

- A rubric-indexed evidence pack, one section per rubric row.
- An architecture note showing where student records do and do not travel.
- Interaction audit log, output-generation disclosure, evaluation report.
- A licence register (**P22** output) for every component, with probe dates.

### ⚠️ Warnings

- **Every statutory and rubric fact in this pattern is Tier 2.**
  `marylandpublicschools.org`, `cosn.org`, `njsba.org`, `web.ped.nm.gov` and
  `excelined.org` are **EGRESS_BLOCKED** here; **no rubric and no RFP was read.**
  Confirm each citation — *especially effective dates and the 120-day clock* —
  against the primary document before it enters a bid.
- **Rubrics are state-specific and moving.** Do not generalise Maryland's to a
  neighbouring state. The *pattern* generalises; the rows do not.
- **Outcomes-based contracting is appearing in tutoring solicitations** (NJSBA RFP
  2026-02). If an outcome clause is in scope, the **P23** harness stops being a
  compliance artefact and becomes the instrument your payment depends on — price
  and staff it accordingly.

## P25 — The interoperability tier, built to be scored (North America, and anywhere with an LMS)

> 🔵 **Re-corrected in the twenty-fourth pass, 2026-10-07.** The eleventh pass fixed the
> "no Python option" error by naming [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3)
> (MIT, 138★). 🔴 **That library is 1,416 days cold on the commit channel and 1,417 on the release
> channel** (`pylti1p3` v2.0.0, 2022-11-20) — so the correction closed the gap with an abandoned
> project. **Take [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) instead:**
> **MIT** (payload 1,098 B), head commit **2026-10-05 (2 d)**, PyPI
> [`django-lti`](https://pypi.org/project/django-lti/) **v0.10.1, 2026-08-07 (61 d)**, 17 releases.
> ⚠️ Two further corrections to the sentence this replaces: `openedx-lti-tool-plugin` is real and
> Apache-2.0 (payload 11,357 B) but lives at **`eduNEXT/openedx-lti-tool-plugin`**, is **443 days
> cold** and is **not published to PyPI** under that name; and `ucfopen/cookiecutter-python-lti`
> (MIT, 147 d) is a live template whose Flask path **installs a 1,364-day-cold fork at a moving
> branch** — take its Django path. 🔴 The best-maintained Python LTI 1.3 implementation of all,
> [`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) (6 d), is
> **AGPL-3.0** and therefore off this shelf by design, not by accident.

Added tenth pass, 2026-10-06. This pattern exists because of a procurement number,
not a technology: **39% of districts score interoperability in their RFP rubrics**
(CoSN, Tier 2, ninth pass). If a third of your buyers assign points to roster and
activity exchange, the integration layer is a **scored deliverable** and it needs to
be specified, licensed and demonstrable — not discovered in integration testing.

**The deliverable:** an AI service that launches from inside the client's LMS with
real identity and course context, reads rosters from the SIS, and produces an
artefact pack that answers an interoperability rubric line by line.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Tool launch, Node estate | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** (`master/LICENSE`) | 373★, the highest-starred genuine LTI 1.3 implementation; turns a service into a full tool provider |
| Tool launch, Moodle estate | [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (`master/LICENSE.md`, 11,343 B) | 🔵 **Re-picked, pass 24.** The same library the standards body ships — byte-identical payload — but the **live** copy: head commit **2026-09-23 (14 d)** against `1EdTech/lti-1-3-php-library`'s **2,317 d**. Composer name `packbackbooks/lti-1-3-php-library` |
| Tool launch, Python/Django estate | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | **MIT** (1,098 B) | 🆕 **Added pass 24.** Head commit **2 d**, PyPI `django-lti` v0.10.1 (61 d). Removes the second runtime when the AI tier is Django |
| Tool launch, JVM estate | [Unicon/tool13demo](https://github.com/Unicon/tool13demo) | **Apache-2.0** (`master/LICENSE`) | LTI 1.3 in Spring Boot, from a higher-ed systems integrator |
| Tool launch, existing Spring Security | [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) | **Apache-2.0** (`master/LICENSE.txt`) | LTI inside an existing Spring Security estate rather than beside it |
| Rostering | [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) | **MIT** (`master/LICENSE`) | OneRoster 1.1 + 1.2 client, OAuth2 for 1.2. **Rostering only — no gradebook** |
| Audit trail | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT** (with carve-out) | The rubric gap the ninth pass found: **no rubric requires an interaction audit trail**, so it is the differentiator (P24) |
| Evaluation socket | P23 harness | — | The other half of the differentiator, and the EMEA conformance file (trend 27) |

**Wiring, and the decision that comes first.** **Pick the LTI runtime from the
client's estate, not from your preference** — the four implementations are not
interchangeable in effort once a stack exists. Then: LTI 1.3 launch carries
identity, course context and role; your Python AI service sits **behind** that
adapter over an internal API; OneRoster.NET syncs the roster on a schedule;
Langfuse records every interaction with the launch context attached, so an audit
trail is a by-product of the architecture rather than a feature nobody funded.

**The gap you must price, not hide.** 🔵 **CORRECTED, twenty-fourth pass of 2026-10-07: "there is
no Python LTI 1.3 library" was false.** [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti)
is **MIT**, head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. 🟢 **If the AI layer is
Django, launch LTI in-process and budget no adapter at all** — that line item disappears from the
bid. ⚠️ The two-process architecture is still right when the AI tier is neither Django nor
JupyterHub, because the only framework-neutral Python implementation is 1,416 days cold; price the
adapter **only after** checking the framework. 🔵 **NARROWED, twenty-fifth pass of 2026-10-07 — "none" is now "one alpha".** [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) (MIT) **vendors `PyLTI1p3`, rebranded** — its README says so — and publishes it as [`ff-ltitoolkit`](https://pypi.org/project/ff-ltitoolkit/) **0.1.0, 2026-06-26 (103 d), one release ever**; head commit **63 d**; **0★**; `Development Status :: 3 - Alpha` with the FastAPI adapter and token minting **unbuilt**; and its `LICENSE` holder is **`Dmitry Viskov`, not its own authors**. **Not "no option", and not a safe dependency either.** Full row in `repos/foundations.md`. Equally: if the
rubric scores **grade passback**, OneRoster.NET does not implement the gradebook,
and if it scores **learning-analytics event streams**, there is **no permissive
Caliper Analytics implementation at all** — both are builds against the spec. Say
so in the response. A rubric line you answered with a library that does not cover
it is worse than one you answered with a costed build.

**Sequence:** estate assessment and runtime choice (1 wk) → LTI 1.3 launch with
identity and context, end to end (2 wk) → OneRoster sync and reconciliation
(2 wk) → Langfuse trail bound to launch context (1 wk) → rubric artefact pack,
line by line (1 wk) → conformance dry-run against the client's own rubric (1 wk).
**8 weeks** to something a procurement officer can score.

**Two warnings.** **Pin `theopenem/OneRoster.NET`**, not the byte-identical
`jdolny/OneRoster.NET` — both are MIT and both name `theopenem` as copyright
holder, so they are one asset at two addresses, and the fork direction is not
establishable from this environment. And **do not sweep for components with the
word "Caliper"**: the search is dominated by `google/caliper` (Java
micro-benchmarking) and `hyperledger-caliper/caliper` (blockchain), which is how a
184-result count turns into five real repositories.

## P26 — Offline-tolerant sync without a platform migration (LATAM, APAC, anywhere intermittent)

Added tenth pass, 2026-10-06. For three passes this KB has answered "offline-first"
with **Kolibri**, which is correct when the client is choosing a platform and wrong
when they already have one. The separable component underneath it is now verified,
and it is MIT.

**The deliverable:** an existing Django application that keeps working, and keeps
syncing, across intermittent connectivity — without adopting a learning platform.

| Stage | Component | Licence (payload) | Why this one |
|---|---|---|---|
| Replication engine | [learningequality/morango](https://github.com/learningequality/morango) | **MIT** (`master/LICENSE`) | **Pure-Python peer-to-peer DB replication for Django.** Marks chosen models syncable; **certificate-based authentication** for data privacy and integrity; change tracking and **data partitioning** designed for low-bandwidth links; SQLite **and** PostgreSQL. 15★, 23 forks, `release-v0.9.x` |
| Shared vocabulary | [learningequality/le-utils](https://github.com/learningequality/le-utils) | **MIT** (`main/LICENSE.txt`) | Constants and utilities shared across the Kolibri toolchain — needed if you ever exchange content with it |
| Content pipeline (optional) | [learningequality/ricecooker](https://github.com/learningequality/ricecooker) | **MIT** (`main/LICENSE`) | Generates Kolibri channels, if the client wants interoperability with that ecosystem |
| Full platform (the alternative) | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`master/LICENSE`) | Where this pattern stops and the platform choice starts |
| Local inference | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) · [ollama/ollama](https://github.com/ollama/ollama) | **Apache-2.0** · **MIT** | The AI layer has to run where the connectivity is not |

**Wiring.** Morango is a Django app: you declare which models are syncable, give
each device or site a certificate, and let it reconcile. The **partitioning** is
the part to design deliberately — it decides what a given school or device is
allowed to hold, which is a data-protection control as much as a performance one.
Pair it with local inference so tutoring continues while the link is down, and let
only the records sync, not the model traffic.

**Why it is a smaller engagement than it looks.** Nothing here asks the client to
migrate. **Morango is usable independently of Kolibri**, under MIT, with
certificate-based auth already built — which is normally the expensive half of a
sync design. For a ministry or network that already runs a Django SIS or LMS, this
is weeks, not a platform programme.

**Sequence:** syncable-model and partition design (2 wk) → morango integration and
certificate provisioning (2 wk) → conflict and reconciliation testing on forced
disconnection (2 wk) → local inference for the degraded path (2 wk) → multi-site
pilot (2 wk). **10 weeks.**

**Two warnings, both licence-shaped.** **Probe every sibling repository before you
depend on it.** Inside this same organisation,
[kolibri-design-system](https://github.com/learningequality/kolibri-design-system)
and [kolibri-server](https://github.com/learningequality/kolibri-server) returned
**no licence payload** under 20 probed URLs — so the Vue design system in
particular must not be used for client UI on the assumption that the org is MIT.
And `learningequality/studio` carries `Copyright (c) 2021 Foundation for Learning
Equality (internal apps)`: the parenthetical looks like a scope restriction, but
the **full text was read this pass and the permission body is unmodified MIT**.
Use it; the qualifier annotates the holder, not the grant.

## Pattern selection

| Situation | Pattern |
|---|---|
| Client already has an LMS | P1 |
| Needs content or item volume from existing curriculum | P2 |
| Must justify mastery/progression decisions | P3 |
| EU client, assessment in scope | P4 (P1 for the integration) |
| Connectivity/budget constrained, equity mandate | P5 |
| Client must evidence that its tutoring AI works, and no permissive evaluator exists yet | **P23** |
| US district / state agency bid, or selling into one | **P24** (with P1 for integration, P4 for inference) |
| Any repository about to become a dependency | **P22**, always |
| Client staff must own it afterwards | P6, alongside any other |
| Pain is administrative, no committed SIS yet | **P7** (module on LGPL-3.0 OpenEduCat) |
| Pain is administrative, SIS already committed | P1's side-car shape — Gibbon/RosarioSIS/openSIS are all copyleft |
| Differentiator is *how they teach*, locked in recordings and senior staff | **P8** |
| LATAM higher ed: adoption already universal, integration shallow | **P8** for depth, P6 for faculty capability |
| Singapore/APAC agentic-governance requirement in scope | any pattern, built to the IMDA four dimensions (see `intel/trends.md` §11) |
| Ministry/province has **mandated** AI instruction (UAE, Beijing, Guangdong) | **P9** — the only pattern driven by a funded obligation rather than a constraint |
| Cohort includes primary-age pupils, or China is in scope | **P9**, for the age-gating graph specifically — a prompt instruction will not do |
| Corporate **L&D** buyer who wants to own the platform | **P10** (fork Mentingo, MIT) — explicitly *not* P1 |
| Academic institution, however L&D-shaped the ask sounds | P1; Mentingo is a component donor here, not a platform |
| Needs spaced repetition / retention reached by an agent | `ankimcp/anki-mcp-server` (MIT, 53 tools) inside P1, or OpenTutor (MIT) for FSRS 4.5 built in |
| US district or state with a 2026 AI statute (ID, OK, MD, OH, CA) | **P11** — one oversight gate satisfies all five, the EU Annex III and Beijing |
| Needs whole lessons generated, not just tutoring dialogue | **P11** (OpenMAIC, MIT, 40.0k★ — pin v1.2.0+ for durable server-side jobs) |
| Competing against an incumbent AI tutor already bought (e.g. Khanmigo) | **P11** — sell the oversight, integration and evidence layer, not a rival tutor |
| Client asks "which model should teach?" or must justify a model choice | **P12** (`pedagogy-benchmark`, MIT) — 1–2 weeks as a scoping add-on |
| Tutoring quality must be measured or must not silently regress | **P12** — re-implement the MI/ML/PG/AC rubric; `AITutor-EvalKit` code is unlicensed |
| Voice is the primary modality (low literacy, low bandwidth, Africa) | **P12** step 3 + **P5** |
| **Any EMEA education account, as the opening diagnostic** | **P13** — most of them believe the August 2026 deadline was cancelled; the 2 December 2026 labelling obligation was not |
| Client must evidence EU AI Act conformity for an education system | **P13** (MIT toolkit + the Annex III point 3 profile you write), then P4 |
| ASEAN institution teaching programming/CS that wants to own its platform | **P14** (fork Coursemology, MIT, 15,802 commits) — and size the 158★ concentration risk in week one |
| Client has seen Singapore's AICET products and wants "that, but ours" | **P14** — the products are closed, the LMS beneath them is MIT |
| Korea or Australia in scope | **P11** gate + **P14** step 4 — Korea's AI Basic Act is live since 22 Jan 2026; TEQSA requires an action plan from every provider |
| National curriculum body **plus** a data-residency constraint | **P15** — open-weight only, with a written copyright position |
| Client asks whether generated items infringe the curriculum body's copyright | **P15** step 2 — reuse CurriculumCraft AI's argument even if you reuse none of its code |
| Teacher-side artefacts (lesson plans, question banks) rather than a student tutor | **P15** step 1 (`microsoft/shiksha-copilot`, MIT) — not P1 |
| LATAM higher ed, and you are choosing where to start | **P6 first** — 87% of LAC institutions use AI, 26% have a strategy; the gap is governance, not technology |
| India or a state/national programme wanting an end-to-end permissive stack | **P16** — AI4Bharat (MIT) + Sunbird (MIT); permissive from language layer to platform |
| Primary literacy, oral reading fluency, or "measure whether the child can read" | **P17** — permissive components, a public dataset and a published baseline; the whole existing category is **two repositories, one MIT at 1 commit** (`prosody`), and Harvard's **OpenLiteracy** is funded to fill it (0 repos today) |
| Offline/low-connectivity **and** the tutor must speak or listen | **P18** — `sherpa-onnx` (Apache-2.0) gives STT+TTS+diarization+VAD in one dependency; **not** Piper |
| ASEAN institution wanting a tutor in Vietnamese, Thai, Malay or Indonesian | **P19** — MIT LMS substrate, Apache-2.0/MIT language shelf, pedagogy layer unbuilt by anyone open or closed |
| Spoken practice in Thai, Vietnamese or Indonesian specifically | **P19 constraint 2** — only Malay has a regional permissive voice toolkit; measure `sherpa-onnx` on real learner audio before promising |
| **Vietnam in scope, at all** | **P20** — Decree 33 makes a RAG tutor high-risk on **corpus provenance alone**, even with no grading, ranking or monitoring |
| Client asks "where did this generated question come from?" | **P20** — the source manifest, with forward tracing from source to item |
| Any engagement that ingests client or curriculum content into a tutor | **P20** alongside **P2** — build the manifest once, it satisfies Vietnam, EMEA Annex III, California AB 1159 and the LATAM governance gap |
| RFP or rubric that **scores interoperability** (39% of US districts do) | **P25** — pick the LTI runtime from the client's estate, and price the Python adapter instead of hiding it |
| Client already runs a **Django** SIS/LMS and needs offline tolerance | **P26** — `morango` (MIT) gives P2P replication with certificate auth; **no platform migration** |
| "We need offline" but the client is **not** choosing a platform | **P26**, not P5 — Kolibri is the answer to a platform question, morango to a sync question |
| Rubric scores **grade passback** or **learning-analytics event streams** | **P25**, costed as a build — OneRoster.NET has no gradebook and there is no permissive Caliper implementation |
| Any absence you are about to put in a client deliverable | **P22**, plus trend 29 — state the instrument that measured it; GitHub's licence field reports MIT repos as unlicensed |

**Index consistency note (seventh pass, 2026-10-06):** this table was missing
**P16, P17 and P18** — three patterns written by earlier passes and never indexed
here. They are added above with P19 and P20. This is the same failure the seventh
pass found in `agents/top.md` and that `repos/trending.md` recorded in the sixth:
**a finding written into one surface and not propagated to the one a reader
opens.** Checking the index against the pattern headings is now part of a pass.

## Anti-patterns

- **Writing an in-tree LMS plugin for reusable IP.** It inherits GPL-3.0/AGPL-3.0.
  Use P1.
- **Promising autonomous grading.** Amended 2026-10-06: a permissive auto-grader
  now *does* exist — `Selleo/mentingo` (MIT) grades open-ended behavioural and
  problem-solving answers — but **only for corporate L&D**, with no academic,
  rubric- or curriculum-aligned grader on the shelf, and the oversight obligation
  is unchanged. Annex III, the Oklahoma and Maryland statutes and Korea's
  high-impact classification are indifferent to licence. Keep the human gate on
  any consequential score, and when you tell a client the grader exists, tell them
  the gate stays in the same breath.
- **Building a side-car against a permissive platform.** Against Mentingo (MIT)
  there is no copyleft to route around, and the side-car reflex costs integration
  depth for no legal benefit. Use P10 and fork it. The mirror of the OpenEduCat
  anti-pattern below.
- **Enforcing an age restriction with a system prompt.** Beijing bars primary
  pupils from independent generative-AI use. A refusal the model is asked to
  perform is not a control; a graph with no generative path for that cohort is.
  Use P9 step 4.
- **Withdrawing a KB entry on a single-owner probe.** The second pass of
  2026-10-06 removed OpenTutor after probing `tutornew/OpenTutor` (8★, unlicensed)
  when the real project was `zijinz456/OpenTutor` (MIT, 130★, FSRS 4.5, 12 blocks,
  LOOM knowledge graph). A 404 is evidence about one owner's repository, never
  about a project. Enumerate owners before withdrawing — a withdrawal needs a
  stronger probe than an addition.
- **Allowlisting only `MIT / Apache-2.0 / BSD`.** That filter rejects Sakai,
  Opencast and Kuali Rice (all **ECL-2.0**, the Apache-2.0 text with an
  education-narrowed patent grant) and pgvector (**PostgreSQL License**) — four
  genuinely permissive components. Allowlist MIT, Apache-2.0, BSD, ECL-2.0,
  PostgreSQL License and ISC.
- **Trusting a repo-level licence badge on an open-core project.**
  `langfuse/langfuse` is MIT *except* `ee/`, `web/src/ee/` and `worker/src/ee/`,
  and its copyright holder is now ClickHouse, Inc. Read the carve-out paths and
  record the holder, then exclude those directories from any vendored copy.
- **Reading "Kuali is ECL-2.0" off the brand.** True of Kuali Rice, false of Kuali
  Financial System and Kuali Coeus (both AGPL-3.0). The diligence unit is the
  repository, never the foundation or the vendor.
- **Specifying AutoGen.** Maintenance mode; `LICENSE` at HEAD is CC-BY-4.0.
- **Taking `frappe/lms` as MIT.** It is AGPL-3.0 at `license.txt`; the comparison
  blogs are wrong.
- **Pinning a DeepTutor fork.** `cloudtoolbox/deeptutor` (7★) and others mirror
  the description and license without the history. Pin `HKUDS/DeepTutor`.
- **Treating an APAC sovereign model as an education product.** They are base
  models with no pedagogy layer; that layer is the work.
- **Depending on an unlicensed repo because it looks mature.**
  `DMontgomery40/mcp-canvas-lms` has 103★, 54 tools and **no license**;
  `loyaniu/moodle-mcp` has 38★ and none either. No license means all rights
  reserved — it cannot ship in a client deliverable. Probe the license in week one,
  before the feature comparison.
- **Recording "unlicensed" after probing only the repo root.**
  `OS4ED/openSIS-Classic` 404s on every root-level license filename while its real
  GPL-2.0 license sits at `docs/License.txt`, linked only from the README. Probe
  filename × extension, then read the README for a license link, then conclude.
- **Building a side-car against an LGPL-3.0 platform out of habit.** On OpenEduCat
  a separate proprietary module is permitted; routing around a constraint that is
  not there costs integration depth for nothing. Use P7.
- **Selling adoption into LATAM higher education.** 92% of students and 79% of
  faculty already use AI. The gap is depth — 88% of faculty engage only minimally.
  Sell integration and faculty capability, not enablement-from-zero.
- **Telling an EMEA client the AI Act does not apply yet.** General application
  started 2 August 2026. Only the high-risk obligations are deferred (Annex III
  stand-alone to 2 December 2027, embedded to 2 August 2028).
- **Chasing a search hit without a reachability probe.** `planejaia/OpenMAIC-Brasil`
  reads like a Brazil-origin multi-agent classroom with a v1.0.0 release and
  returns HTTP 404 on every branch and file. `curl -sI` before it reaches a
  proposal.
- **Concluding a region has no permissive shelf from a popularity-ordered
  channel.** Added in the fifth pass of 2026-10-06. GitHub topic pages and
  stars-sorted searches rank by adoption, so a 2026 project with four commits from
  a public university in Risaralda is structurally invisible to both. Four passes
  of this KB declared "no India-origin", "no ASEAN-origin" and "no LATAM-origin"
  permissive education project; **one institution-first search refuted all three.**
  When a gap survives several passes, change the channel — and pick one that is
  not ordered by stars.
- **Clearing a model's licence at the repository level.**
  [aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no
  `LICENSE` payload** and its README says terms vary by base model — Llama3-derived
  variants restrict commercial use, Gemma-derived variants differ. A repo-level
  check returns nothing and clears nothing. **Clear rights per model, per release,
  from each Hugging Face model card**, and log the result.
- **Trusting a licence badge.** [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench)
  carries a **CC BY 4.0** badge on README line 3 and a **CC BY-SA 4.0** statement on
  README line 199, with **no `LICENSE` payload** behind either. Three reviewers
  reading the same commit get three different answers. The payload is the licence;
  a badge is a claim about it.
- **Forking a repository because its README is good.**
  [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) is MIT, institutionally
  funded, architecturally sound — and **every code path in its own documented tree
  404s**, with a quickstart pointing at a different repository. Probe the paths the
  README promises, not just the repository root.
- **Telling an EMEA client the high-risk deferral bought them 16 quiet months.**
  **Regulation (EU) 2026/1744** left **Article 50 transparency untouched**: the
  watermarking and synthetic-content-marking deadline is still **2 December 2026**,
  and the duty to classify systems against Annex III is immediate. The clients who
  heard "delayed" and stopped are unlabelled *and* unclassified. Run **P13**.

## P27 — The tutor-quality evidence pack (the harness is free; the benchmarks are borrowed, never shipped)

**Replaces the "wait for the artefact" half of P23.** P23 was written when this KB
believed no permissive evaluation harness and no pedagogy benchmark existed. Both
beliefs were wrong in different ways, measured 2026-10-06: **the harness exists,
MIT, from a government, at 2,945★**, and **the benchmarks exist and are licensed
shut.** P27 is the pattern that follows from the real situation.

**Sell it when:** the buyer asks "how do we know it teaches?" — a North American
district or university with no mandated evaluation, an EMEA ministry facing AI Act
high-risk classification, an APAC buyer with a sovereignty requirement, or a LATAM
institution among the 91% with no formal evaluation mechanism.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) | Why this one |
|---|---|---|---|
| Evaluation harness | [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** | 2,945★, 779 forks, UK AI Security Institute, pushed 2026-10-06. Datasets → solvers → scorers, model-graded evals, tool use, multi-turn dialog. **Do not write a runner.** |
| Red-team harness | [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** | Singapore IMDA's AI Verify Foundation. Benchmarking **and** adversarial probing in one tool. The only permissive red-teaming harness in this KB. |
| Pedagogical scorer (yours) | written against Inspect's scorer interface | **your client's** | The billable artefact. Encodes the rubric: does it scaffold, does it withhold the answer, does it detect and correct a misconception, does it over-validate. |
| Reference benchmark #1 | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) | 🔴 **custom Evaluation Dataset License** | 57★, Khan Academy's own math-tutoring benchmark. **Borrowed at measurement time.** |
| Reference benchmark #2 | [`shivanireddyk/tutoreval`](https://github.com/shivanireddyk/tutoreval) | ✅ **MIT** | 0★, one author — but the **only** OSI-licensed pedagogical benchmark found. Vendorable. |
| 🔴 Excluded | `eth-lre/mathtutorbench` (no payload; README claims CC BY 4.0 *and* CC BY-SA 4.0) · `Yunfeng-Wan/CSTutorBench` (CC BY-NC-4.0) | — | Named here so a later pass does not rediscover them as options. |
| Delivery into the LMS | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | ✅ **MIT** (1,098 B) | 🔵 **Re-picked, pass 24.** Was `dmitry-viskov/pylti1.3`, which is **1,416 d cold (commit) / 1,417 d (release)**. This is head commit **2026-10-05 (2 d)**, PyPI `django-lti` **v0.10.1 (61 d)**. Django; the harness is Python, so it launches in-process. |

### Wiring

```
                        ┌─────────────────────────────────────┐
  client's tutor ──────▶│ Inspect (MIT)                       │
  (any model/arch)      │  tasks → solvers → scorers          │
                        │                                     │
   your rubric ────────▶│  custom pedagogical scorer          │──▶ eval logs
                        │   · scaffolding present?            │     (client's,
                        │   · answer withheld?                │      exportable)
                        │   · misconception corrected?        │
                        │   · sycophancy / over-validation?   │
                        └──────────────┬──────────────────────┘
                                       │
          ┌────────────────────────────┴───────────────────────┐
          │                                                    │
  ┌───────▼─────────────┐                        ┌─────────────▼──────────┐
  │ tutoreval (MIT)     │                        │ Khan dataset (🔴)      │
  │ VENDORED into the   │                        │ MOUNTED read-only at   │
  │ deliverable         │                        │ eval time; NEVER in    │
  └─────────────────────┘                        │ the repo, the image,   │
                                                 │ the training set, or   │
  ┌─────────────────────┐                        │ the handover           │
  │ Moonshot (Apache-2) │                        └────────────────────────┘
  │ adversarial pass:   │
  │ jailbreak → answer  │──▶ red-team report
  │ leakage → unsafe    │
  └─────────────────────┘
```

**The licence boundary is a build-system boundary, not a policy document.** Enforce it
mechanically:

1. The Khan dataset lives **outside** the repository — a mount, a fetch step gated on
   an explicit `--external-benchmarks` flag, or an operator-run command. It must not
   be a git submodule, a vendored directory, a Docker layer, or a fixture.
2. CI fails the build if any path under the benchmark mount is reachable from the
   packaging target. One rule in the packaging config; ten minutes to write.
3. The **eval logs are the deliverable** — scores, traces, per-item verdicts. Those
   are "insights and learnings," which clause 3 of Khan's licence expressly permits
   you to use commercially. The dataset rows are not, and must not appear verbatim
   in a report appendix.
4. **Never fine-tune on it.** The licence prohibits model training in terms, and this
   is the mistake most likely to be made by a well-meaning engineer three sprints in.

### Deliverables

- An Inspect task suite + the custom pedagogical scorer — **MIT/client-owned,
  shippable**.
- A Moonshot red-team configuration and its report.
- The **evidence pack**: scores on the client's own content, scores on `tutoreval`,
  comparative findings from the borrowed benchmarks, and the adversarial report.
- A **licence register** naming each component's grant, and the mechanical rule that
  keeps the borrowed datasets out of the artefact.

### ⚠️ Three warnings that are the point of this pattern

- **Do not quote harness construction as the deliverable.** It is free, MIT, and
  maintained by a government. Quoting it is how a proposal loses on credibility.
  Quote the rubric, the scorer, the evidence pack and the licence hygiene.
- **"We benchmarked against Khan Academy's dataset" is sayable; publishing a
  comparative league table from it is not.** The licence prohibits publication and
  redistribution. Keep the comparison inside the engagement.
- **`mathtutorbench` will be suggested to you.** 43★, ETH Zurich, an EMNLP oral —
  it looks like the obvious choice and it has **no licence payload** and two
  contradictory README claims. Treat as ungranted; say so once, in writing, early.

## P28 — Brazilian public-sector school management with AI on top (GPL-2.0 is the feature)

**Sell it when:** the buyer is a Brazilian municipality, state secretariat or public
school network — the engagement most likely to be mispriced by assuming a copyleft
platform is a problem.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) | Note |
|---|---|---|---|
| School management / SIS | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **GPL-2.0** (`2.12/LICENSE`) | **718★, 547 forks** — the most-forked platform in this KB. Laravel/PHP, tagged `software-publico`. ⚠️ **Default branch is `2.12`**; `main` serves nothing. |
| Offline sync | [`learningequality/morango`](https://github.com/learningequality/morango) | ✅ **MIT** | Peer-to-peer Django model replication, certificate-authenticated, built for low-bandwidth links. SQLite **and** PostgreSQL. |
| Learner-facing delivery | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | ✅ **MIT** | Offline-first learning platform. |
| Evaluation | **Inspect** (MIT) + the P27 scorer | ✅ | The 9%-with-evaluation-mechanisms gap is the differentiator in this region. |
| LMS-side delivery, if any | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | ✅ **MIT** (1,098 B) | 🔵 **Re-picked, pass 24** (was `pylti1.3`, 1,416 d cold). Python, matches the AI tier's language; head commit **2 d**, PyPI `django-lti` **v0.10.1 (61 d)**. |

### Wiring, and why the licence works in your favour

```
  ┌──────────────────────────┐        ┌─────────────────────────────┐
  │ i-educar (GPL-2.0)       │        │ AI tier — SEPARATE PROCESS  │
  │ enrolment · attendance   │◀──────▶│ (your licence)              │
  │ grades · school records  │  REST  │  · early-warning scoring    │
  │ branch 2.12              │        │  · PT-BR tutoring agent     │
  └───────────┬──────────────┘        │  · evaluated via Inspect    │
              │                       └─────────────────────────────┘
       morango (MIT) ──── certificate-authenticated P2P sync ───▶ school servers
              │
      ┌───────▼────────┐
      │ Kolibri (MIT)  │  offline learner delivery in classrooms
      └────────────────┘
```

**GPL-2.0 has no network clause.** Hosting a modified i-educar for a municipality
triggers **nothing** — unlike the AGPL-3.0 platforms (LearnHouse 2,320★, CourseLit
1,269★, Obojobo, Materia), where serving a modified instance obliges you to offer
source to its users. Obligations attach to **distribution**: if you hand the
municipality a modified i-educar, you hand them its source under GPL-2.0.

**And in Brazilian public procurement that is usually what they are asking for.**
`software-publico` is a classification the platform already carries; a buyer who
expects to own and inspect what they bought is a buyer whose requirement the licence
satisfies for free. **Keep the AI tier in a separate process across a REST boundary**
so it carries your own licence, and the question of whether linking occurred never
arises.

### Deliverables

- i-educar deployment pinned to a branch that exists (**`2.12`** — verify before
  every release; this platform does not use `main`).
- The AI tier as an independently licensed service, PT-BR first.
- morango-based sync so school sites work through intermittent connectivity.
- The P27 evidence pack, in Portuguese — **the artefact 91% of LAC institutions
  cannot produce.**

### ⚠️ Warnings

- **Probe the branch, not the convention.** `main` on i-educar serves no licence and
  no README. A `main`+`master` licence probe reports Brazil's largest free education
  platform as ungranted, which is how a real option gets struck off a shortlist.
- **Do not stage this on the Spanish-language GitHub shelf.** Measured 2026-10-06:
  `educación IA aprendizaje` → 10 repositories, **all 0–1★**, one a satirical art
  project. There is no regional component shelf. The components above are global and
  the regionalisation is yours to build.
- **i-educar is PHP/Laravel and your AI tier is Python.** That is a feature here —
  the process boundary that keeps the licences apart is the same boundary the
  language split would have forced anyway.

## P29 — The permissive xAPI analytics spine, with conformance as the deliverable

**When to use it.** A client needs learning analytics and the procurement scores
interoperability (US K-12 and higher-ed rubrics; EU tenders increasingly the same). The
instinct is to reach for Caliper because 1EdTech brands it. **Caliper has no surviving
public reference implementation in any language** (twelfth-pass gap). xAPI does, and the
whole chain is permissive.

### Components — all verified from payload, 2026-10-06

| Role | Repo | Licence | Branch |
|---|---|---|---|
| **Vocabulary / profile** | [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | Apache-2.0 | `master` |
| **Transport / transform** | [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | Apache-2.0 | `main` |
| **Store (LRS)** | [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | Apache-2.0 | `main` |
| **Conformance proof** | [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** | `master` |
| **LMS event source (Open edX)** | [openedx/event-routing-backends](https://github.com/openedx/event-routing-backends) | ⚠️ AGPL-3.0 | `master` |
| **LMS event source (Sunbird)** | [project-sunbird/sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | MIT | `master` |
| **Rostering / SIS context** | [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | Apache-2.0 | `main` |

### Wiring

1. **Define the profile before emitting anything.** Write an xAPI Profile for the client's
   verbs and activity types using `xapi-profiles` as the structural spec and ADL's public
   index (`xapi.vocab.pub`) to reuse existing vocabulary rather than invent verbs. This step
   is what makes the data answerable later; skipping it produces a statement pile.
2. **Emit.** On Open edX, `event-routing-backends` already produces xAPI — but it is
   **AGPL-3.0 and in-platform**, so treat it as *deployed infrastructure you configure*, not
   code you fork into a deliverable. On Sunbird, use the MIT telemetry SDK. For a bespoke
   tutor, emit directly from your own agent code.
3. **Pipe with `xapipe`**, configured **by the profile from step 1** — that is the design
   point of LRSPipe, and it is what keeps transformation rules out of application code.
   ⚠️ **Pin `yetanalytics/xapipe`. `yetanalytics/lrspipe` is a 404** — the product name is
   not the repository name, and this KB logged that false negative twice.
4. **Store** in `xapi-lrs`, or in the client's existing LRS if they have one.
5. 🟢 **Run `lrs-conformance-test-suite` in CI and ship the report.** This is the step that
   makes the pattern worth more than its parts: the suite tests the MUST requirements of the
   xAPI specification, so the deliverable includes **third-party-specified evidence of
   conformance** rather than a claim. In a rubric-scored procurement (trend 26, trend 36)
   that report is the line item.
6. **Join to roster/SIS context via `edfi-oneroster`** so a statement about a learner can be
   resolved to a class, a school and a term — which is what makes the analytics answer an
   administrator's question rather than a developer's.

### Deliverables

- An xAPI Profile document for the client's domain, published.
- A configured pipe + LRS, deployed.
- 🟢 **A conformance report, re-generated by CI on every change.**
- A roster-joined query layer.

### ⚠️ Warnings

- **Do not promise Caliper.** Price a 1EdTech membership or a clean-room build if the client
  insists, and put the choice in the proposal.
- **AGPL reaches `event-routing-backends`.** Configure and deploy it; do not vendor it into a
  proprietary product.
- **The conformance suite tests an LRS, not your pipeline.** It proves the store conforms. If
  the client needs end-to-end assurance, the profile-validation step in `xapipe` is where you
  add it, and that is custom work.

## P30 — The Apache-2.0 component inside an AGPL platform (how education IP stays reusable)

**When to use it.** A client runs Open edX or Moodle — most do — and wants a bespoke AI
component: a tutor inside a course, an analytics panel, a proctoring or accessibility
side-car. Globant wants the component to be **reusable studio IP** across later engagements.

**The insight (trend 34):** the platform's copyleft binds code *in the platform tree*. The
**plugin SDK** does not have the platform's licence.

### Components

| Role | Repo | Licence | Note |
|---|---|---|---|
| **Plugin SDK (Open edX)** | [openedx/XBlock](https://github.com/openedx/XBlock) | 🟢 **Apache-2.0** (`master/`**`LICENSE.TXT`**) | 470★. The API your component is written against. |
| Platform core | `openedx/edx-platform` | ⚠️ AGPL-3.0 | Deployed, configured — **never forked into the deliverable**. |
| **Out-of-tree Moodle access** | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | 🟢 MIT | Reaches Moodle data from outside the tree, which is why it can be MIT. |
| In-tree Moodle plugins | 8 verified this pass | ⚠️ GPL-3.0 | Correct and unavoidable for in-tree work. |
| **LTI 1.3 delivery (Python)** | [`academic-innovation/django-lti`](https://github.com/academic-innovation/django-lti) | 🟢 MIT (1,098 B) | 🔵 **Re-picked, pass 24.** Was `dmitry-viskov/pylti1.3` with *"fork and maintain"* — unnecessary now. Head commit **2026-10-05 (2 d)**, PyPI `django-lti` **v0.10.1 (61 d)**, 17 releases. 🔴 **Do not reach for `openedx/xblock-lti-consumer`** here, however well maintained (6 d): it is **AGPL-3.0**, which defeats this pattern's entire purpose. |
| **LTI 1.3 delivery (Java)** | [UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) | MIT | EMEA/Spain lineage. ⚠️ **1,418 days cold** (measured pass 23) — a reference, not a dependency. |
| Reference specification | `LabSirius/TutorIA` (`docs/`) | MIT | A 13-page spec that already chose this shape. |

### Wiring — the decision tree, in order

1. **Can the component live entirely outside the platform?** Then deliver it over **LTI 1.3**
   (`django-lti` / UOC's Java tool) or **MCP** (`moodle-mcp-server` shape). Cleanest IP
   position, works across LMSs, and it is the only option that is portable between a Moodle
   client and a Canvas client.
2. **Does it need to render inside a course page?** Then write an **XBlock** against the
   Apache-2.0 SDK. Your component, your licence.
3. **Does it need to modify platform behaviour?** Then it is in-tree, it is GPL/AGPL, and
   **it is a client deliverable, not studio IP**. Say so in the proposal and price it as
   bespoke.

Order matters: each step down the tree costs IP, so exhaust step 1 before step 2.

### Deliverables

- A component package under a licence Globant chooses.
- A deployment that configures — never forks — the copyleft platform.
- 🔴 **A written packaging review by counsel**, attached to the engagement.

### ⚠️ Warnings

- **The licence file's location does not settle the AGPL question.** Whether a plugin is a
  derivative work turns on linkage and distribution. **This pattern needs legal sign-off
  once per client architecture** — then it is reusable.
- `XBlock`'s licence is at **`LICENSE.TXT`**, uppercase. A lowercase probe will tell you this
  repository is ungranted. It is not.
- **Moodle's in-tree plugin API gives you no such seam.** For Moodle, step 1 (MCP/LTI from
  outside) is the only route to reusable IP.

## P31 — The education test profile for AI Verify (APAC compliance as an upstream contribution)

**When to use it.** An APAC engagement — Singapore, or any client that accepts IMDA's
framework as a reference — needs demonstrable AI governance for an education deployment.

**The insight (trend 36):** APAC is the only region where the **regulator's own conformance
harness is permissively licensed and designed to be extended**. Compliance evidence can be
produced *by the regulator's instrument* instead of asserted by the vendor.

### Components

| Role | Repo | Licence |
|---|---|---|
| **Governance test framework** | [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | Apache-2.0, 98★ |
| **Plugin / test-widget kit** | [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | Apache-2.0 |
| **Red-team / benchmark assets** | [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | Apache-2.0 |
| **Pedagogy-knowledge probe** | `AI-for-Education/pedagogy-benchmark` | MIT |
| **Classroom-discourse measurement** | [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | MIT |
| ⚠️ Evals index | `aiverify-foundation/LLM-Evals-Catalogue` | 🔴 **ungranted** — cite, do not vendor |

### Wiring

1. **Stand up `aiverify`** against the client's education model or agent.
2. **Build an education test plugin** with `aiverify-developer-tools`. There is **no
   education-specific profile in AI Verify today** (declared gap, twelfth pass), so define
   one: age-appropriateness, curriculum-alignment fidelity, refusal behaviour on assessment
   integrity, and **human-override reachability** — the property US state law and Korea's AI
   Basic Act both require.
3. **Source the test content from permissive instruments, not from benchmarks you cannot
   ship.** `pedagogy-benchmark` (MIT) for pedagogical knowledge; `moonshot-data` for
   adversarial cases; `edu-convokit` to measure discourse quality on real transcripts after
   anonymisation. ⚠️ Several named education benchmarks in this KB are **licence-shut**
   (trend 31) — the harness is free, the benchmarks are often not. Check each one before it
   enters a deliverable.
4. 🟢 **Contribute the profile upstream.** Once merged it becomes a reference other
   implementers must meet, and the client's compliance artefact is then produced by a
   government-recognised tool carrying Globant's contribution.
5. **Pair with national readiness documents**: Korea (AI Basic Act, in force 22 Jan 2026),
   Vietnam (Law 134/2025/QH15, 1 Mar 2026), Australia (TEQSA institutional action plans).

### Deliverables

- A deployed AI Verify instance with an education profile.
- Test reports per release.
- 🟢 An upstream PR to `aiverify-developer-tools`.
- National readiness documents per jurisdiction.

### ⚠️ Warnings

- **Do not infer licences from the organisation.** Two of the three `aiverify-foundation`
  repositories used here are Apache-2.0; `LLM-Evals-Catalogue` in the same org has **no
  grant**.
- **AI Verify validates against principles; it does not confer legal compliance.** Korea's
  and Vietnam's statutes impose duties a test report alone does not discharge.
- **Upstream contribution is a commitment.** A merged profile that then rots is worse for
  the client's evidence than one maintained privately. Budget maintenance.

## P32 — The Portuguese-language permissive component (the LATAM position with no incumbent)

**When to use it.** A Brazilian engagement, or a Globant investment decision about durable
regional IP.

**The insight (trend 37):** measured with `total_count`,
`tutor inteligência artificial educação aprendizagem` returns **0**. The
Portuguese-language permissive AI-tutoring shelf **does not exist** — and Brazil is the
largest education system in the region. There is no incumbent to displace.

### Components

| Role | Repo | Licence | Why this one |
|---|---|---|---|
| **Architecture to copy** | [thiagoluzin/pemara-edu-mira](https://github.com/thiagoluzin/pemara-edu-mira) | **MIT**, 0★ | The only Portuguese permissive asset in this KB. **School-LAN deployment, offline-capable, optional AI** — the architecture Brazilian school infrastructure actually supports. |
| **Offline delivery base** | Kolibri | MIT | Proven offline-first platform. |
| **Exam-domain data** | [yunger7/enem-api](https://github.com/yunger7/enem-api) | ⚠️ GPL-2.0 | **ENEM**, Brazil's national entrance exam. Copyleft — run it as a service, do not vendor it. |
| **School management** | `portabilis/i-educar` (branch **`2.12`**) | ⚠️ GPL-2.0 | Brazil's largest free school-management platform. Fork is published — usually acceptable for a public client (P28). |
| **Local inference** | Ollama | MIT | Per-seat cloud inference is the binding cost constraint in this market. |
| **Lesson generation** | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | MIT, 313★ | Runs **local models**; video lessons where bandwidth is scarce but a projector is not. |
| **Project-based LMS** | [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | MIT, 978★ | If the engagement needs a full platform rather than a component. |

### Wiring

1. **Scope it as a component, not a platform.** The gap is a *component* gap; a platform
   competes with `i-educar` and Moodle, which are entrenched and free.
2. **Build Portuguese-first, not Portuguese-translated.** Brazilian curriculum structure
   (BNCC), Brazilian grade levels, Brazilian assessment conventions. A Spanish component with
   translated strings is what the 0 count already reflects — the Spanish shelf has 2 live
   repositories and none of them crossed the language boundary.
3. **Default to local inference (Ollama) with cloud as an opt-in.** Cost, not capability, is
   the constraint.
4. **Deploy to a school LAN**, following `pemara-edu-mira`: no dependence on public internet
   during a lesson.
5. **Publish under MIT**, in Portuguese, with a Portuguese README. 🟢 **The licence and the
   language are the differentiators** — the code is the easy part.
6. **Integrate, do not absorb, the copyleft layer.** Call `enem-api` and `i-educar` over their
   interfaces.

### Deliverables

- An MIT, Portuguese-language, offline-capable education component, published.
- A BNCC-aligned content mapping.
- A school-LAN deployment guide.

### ⚠️ Warnings

- **`pemara-edu-mira` is 0★ and a one-person project.** Copy the *architecture*; do not pin it
  as a dependency.
- **Publishing is the point.** An internal-only component does not take this position — the
  gap is a published-supply gap.
- ⚠️ **Licence hygiene is the regional failure mode, not licence choice.** Two LATAM
  repositories probed this pass carry **no grant at all**. Whatever is built here, attach the
  licence in the first commit.

## P33 — Sovereign avatar-and-voice tutoring, on a platform that already ships it (EMEA first; the same build serves LATAM)

**When to use it.** A public-sector or university client wants conversational AI tutoring
with a **spoken or embodied** interface, and student data **cannot leave the institution or
the region**. Previously this KB answered that request by specifying the stack component by
component (P4) and accepting a 10–12 week build. **It is now mostly a configuration
exercise**, because a permissive platform ships the sovereign path as a setting.

**Why this pattern exists now.** Two facts found in the thirteenth pass:

1. [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
   (**BSD-3-Clause**) ships **local RAG**, **voice / video / 3D-avatar modes**, **RBAC** and
   **Ollama serving** in the same configuration surface as hosted APIs — and is funded by
   Morocco's Ministry of Higher Education, the DDA and the CNRST.
2. The research alternative is **not obtainable**. The **VTutor** animated-pedagogical-agent
   SDK has three papers and a live demo, but no licence payload and an **empty**
   `VTutorTools` organisation. **Do not plan around it.**

### The stack — every component payload-verified permissive

| Layer | Component | Licence | Role |
|---|---|---|---|
| Tutoring platform | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | Tutoring loop, learner onboarding, per-learner assistant, avatar presentation, RBAC |
| Model serving | [`ollama/ollama`](https://github.com/ollama/ollama) | MIT | Open-weight models on institutional hardware. **Already a first-class target of the platform** — not an integration |
| Serving at cohort scale | [`vllm-project/vllm`](https://github.com/vllm-project/vllm) | Apache-2.0 | Swap in when concurrency outgrows Ollama |
| Retrieval | [`pgvector/pgvector`](https://github.com/pgvector/pgvector) | **PostgreSQL Licence** (permissive) | Vectors **inside Postgres** — no separate vector store to host, secure and keep in-region |
| Document ingestion | [`opendatalab/MinerU`](https://github.com/opendatalab/MinerU) | Apache-2.0 | Curriculum, textbooks and scanned material into structured text for the local RAG |
| Real-time voice | [`livekit/livekit`](https://github.com/livekit/livekit) | Apache-2.0 | WebRTC transport for spoken practice and oral assessment beyond what the platform ships |
| Audit trail | [`langfuse/langfuse`](https://github.com/langfuse/langfuse) | MIT **outside `ee/`** | Every model call with cost, latency and output — the Article 50 evidence, produced as a by-product |
| Typed decisions | [`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai) | MIT | Any assessment-adjacent output as a validated schema, never free text |
| LMS seam | [`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 | The permissive doorway into an incumbent Moodle / Canvas / Open edX — **side-car, never a fork** |

### Wiring

1. **Stand the platform up against local inference first.** Deploy `open-tutor-ai-CE` with
   **Ollama** as the only configured provider and no hosted API key present. This is the
   step that is a setting rather than a build, and doing it first means the sovereign
   posture is the default configuration rather than a later hardening pass. Prove a tutoring
   turn end to end before adding anything.
2. **Point the local RAG at real curriculum.** Run the client's syllabi, textbooks and past
   papers through **MinerU**, load them into **pgvector** in the platform's own Postgres.
   One database for relational and vector state — one thing to host in-region, back up and
   certify.
3. **Put Langfuse in front of every model call, before the pilot opens.** Retrofitting an
   audit trail after a pilot has run means the pilot has no trail. **Exclude `ee/` from any
   vendored copy and record the holder as ClickHouse, Inc.** as well as the licence.
4. **Wrap every assessment-adjacent output in a `pydantic-ai` schema.** Grades, mastery
   estimates, placement and progression as validated objects with the inputs that produced
   them. This is the P22/P24 artefact the procurement rubric and the Annex III file both
   consume, and it is what makes **human-final** (trend 16) enforceable in code rather than
   in policy.
5. **Add voice only where it is assessed.** The platform's own voice/avatar modes cover
   conversational practice. Reach for **LiveKit** when you need multi-party sessions, oral
   examination with recording, or latency control you must own.
6. **Keep the incumbent.** Enrolment, roster and gradebook stay in the institution's
   existing LMS; integrate over **LTI 1.3** so none of the above inherits AGPL or GPL. The
   tutoring platform is a tool the LMS launches, not a replacement for it.

### Compliance, mapped to the real clock

🟢 **The near-term EU deliverable is labelling, not conformity.** **Article 50 transparency
duties have applied since 2 August 2026.** The Digital Omnibus
(**Regulation (EU) 2026/1744**) deferred **Annex III stand-alone high-risk** obligations to
**2 December 2027** and **Annex I embedded** to **2 August 2028**.

- **Now:** AI interaction is disclosed to the learner, and synthetic output is marked. Steps
  1–3 deliver this.
- **By December 2027:** if the deployment touches admission, evaluation of learning
  outcomes, placement, or exam/behaviour monitoring, it is **Annex III high-risk**. Steps 3
  and 4 are the risk-management, data-governance, human-oversight and record-keeping
  evidence — built in, not retrofitted.
- ⚠️ **Scope the boundary explicitly in the SOW.** A tutor that *practises* is not
  high-risk; the moment its output informs a grade or a progression decision, it is. The
  cheapest compliance decision available is **keeping the tutor on the practice side of that
  line** and routing assessment through the LMS.

### Timeline and the honest caveats

**6–8 weeks** to a governed pilot: ~1 week platform and local inference, ~2 weeks curriculum
ingestion and retrieval, ~1 week observability and typed outputs, ~1 week LTI integration,
2–3 weeks hardening and evidence pack. 🔵 **That is 4 weeks faster than the P4 build it
replaces**, and the saving is entirely in steps 1–2.

- 🔴 **Pin a commit.** 192 forks against 108 stars means much real-world use sits in
  divergent forks nobody tracks.
- 🔴 **Raise the holder question before contract.** The payload reads *"Mohamed El hajji On
  behalf of all **R2D-dev**"*, and **R2D-dev appears in no public artefact of the project**.
  On a redistribution engagement that is the party an indemnity question routes to.
- ⚠️ **Check the open-core line against the client's must-haves.** Theming, SLA and LTS sit
  in the paid Enterprise Edition. The CE grant is unqualified and **this is not a directory
  carve-out like Langfuse's `ee/`** — but the roadmap is set by a party with an incentive to
  keep features above the line. Get the answer in writing at proposal time.
- ⚠️ **Cite the payload, not a catalogue.** Third-party catalogues list this project as
  Apache-2.0; it is **BSD-3-Clause**, confirmed from the payload by two passes at the same
  1,531 bytes. Both are permissive, but the attribution clauses differ.
- 🟢 **For LATAM, this is the same build with a localisation workstream.** The thirteenth
  pass found no LATAM-origin permissive equivalent — the Portuguese channel returned two MIT
  assets at 2★ and 0★. **Localise this platform** (it already serves local models and local
  RAG) rather than waiting for one; pair with **P32** if the localisation work is published
  back as the permissive Portuguese-language component that shelf still lacks.

## P1 update, fourteenth pass of 2026-10-06 — the default engagement shape now has four platform doors, not two

P1 (LTI + MCP side-car tutor) was written when the only platforms with a permissive,
payload-backed MCP side-car were **Canvas** and **Moodle**. Measured this pass, the door
list is four, and the choice is now made on the client's existing LMS rather than on what the
shelf happens to carry:

| Client runs | Side-car to start from | Licence (payload) | ★ |
|---|---|---|---|
| Canvas LMS | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 278 |
| Moodle | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) · [1alexandrer/moodle-mcp](https://github.com/1alexandrer/moodle-mcp) 🆕 | MIT · MIT | 43 · 18 |
| 🆕 **Brightspace / D2L** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) (features, npm) · [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) (**opt-in writes**, circuit breaker, multi-auth) · [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) (**Apache-2.0**) | MIT · MIT · Apache-2.0 | 57 · 12 · 6 |
| 🆕 **Blackboard Learn / Ultra** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) — **RBAC middleware in the MCP layer** | MIT | 2 |

⚠️ **Two selection rules this adds.** On Brightspace, take the **feature** server for scope
and read the **multi-auth** one before designing any write path — it is the only asset in the
tier that models TOTP/OAuth/browser auth, retries and circuit-breaking, and LMS auth is where
these integrations actually fail. On Blackboard the tier is five repositories deep, so expect
to fork rather than adopt — and start from `bb-mcp` **because of its RBAC middleware**, which
is the control an education deployment is audited on and which no other asset in the
98-address cluster implements.

## P28 — The K-12 administrative integration (the empty tier, built properly)

**When to use.** A school district, a ministry, or a K-12 group asks for an agent over its
own administrative systems — Google Classroom, a student information system, guardians,
enrolment, accommodations. **This is the pattern for a tier with no incumbent**: Google
Classroom measures 17 open-source integration repositories whose best dedicated server has
**6★**, and PowerSchool measures **`total_count: 0`** (trend 39).

### Components

| Component | Repo | Licence (payload read 2026-10-06) | Role |
|---|---|---|---|
| Workspace-for-Education surface | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** (1,087 B) | Docs, Sheets, Slides, **Forms**, Drive, Classroom. **Start here, not from a Classroom-only server** — Forms is where K-12 assessment lives. |
| Classroom reference implementation | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** (1,063 B) | The tier's best dedicated server (6★, 9 forks). Read it for the Classroom API surface; expect to extend it. |
| **Role separation** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | **MIT** (1,063 B) | Not for Blackboard here — **lift its RBAC middleware pattern.** Teacher, student, guardian and administrator must be distinct principals in the MCP layer, not in the prompt. |
| Accommodations vocabulary | [GarphenGate/moltline-mcp](https://github.com/GarphenGate/moltline-mcp) | **MIT** (1,072 B) | 8 skills across curriculum, classroom, **accommodations**, exam prep. The only asset in this KB that names accommodations as a surface. |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | Every record-touching decision returns a validated schema, never free text. |
| Orchestration + audit | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Checkpoints are the audit trail. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT outside `ee/`** | Trace every call, cost and output. ⚠️ Keep the deployment out of `ee/`. |
| Retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence | Vectors inside the district's existing Postgres — no second datastore to secure. |

### Wiring

1. **Scope to read-only for the whole of phase one.** Every component above supports it;
   `edu-workspace-mcp` and the Classroom server are read-first by design. No write path ships
   until the oversight gate in step 5 exists and has been exercised.
2. **Authenticate as the institution, not as a user.** This is the barrier that emptied the
   tier (trend 39) and the one an integrator clears: Google Workspace for Education
   domain-wide delegation, scoped to the minimum API set, with the scope list in the SOW.
3. **Put RBAC in the MCP layer** — the `bb-mcp` pattern. One principal per role; a tool a
   guardian may call is a *different tool* from the teacher's, not the same tool with a
   different prompt. Guardian access to another child's record must be impossible by
   construction, not by instruction.
4. **Index curriculum and policy documents through MinerU → pgvector**, keeping the source
   document id on every chunk so an answer can always be traced to a page.
5. **Gate every write and every consequential read behind a named human.** US state law has
   converged on one testable rule — human judgment is final (trend 16) — and the EU treats
   these systems as high-risk. The gate is a LangGraph node that cannot be bypassed, and
   Langfuse records who passed it.
6. **Handle accommodations as a first-class, logged capability**, using the moltline
   vocabulary. An accommodation is a legal entitlement; an agent that silently fails to apply
   one is a compliance incident, not a bug.

### Deliverables

- A read-only Workspace-for-Education / SIS MCP server deployed inside the district's
  boundary, with per-role tool sets and the scope list documented.
- An RBAC matrix (role × tool × data class), reviewed by the client's counsel.
- A Langfuse trace archive demonstrating every access and every gate decision.
- A written accommodations-handling note: which entitlements the system reads, which it
  applies, and which it explicitly refuses to decide.
- The P22 licence-reliability gate output for every component.

### ⚠️ Three warnings that are the point of this pattern

- 🔴 **Do not start from the ungranted assets in this tier, however convenient.**
  `zainf2327/mcp-classroom` **auto-grades submissions and carries no licence of any kind**;
  `shimahikojin/google-classroom-mcp` likewise; `AStheTECH/mewcp-google-classroom` carries a
  bespoke **"Community License"** that forbids commercial use, hosted service, rebranding and
  anything competitive, with automatic termination on breach. All three are unusable in a
  Globant deliverable and the third is the one most likely to be mistaken for usable.
- ⚠️ **`total_count: 0` for PowerSchool means no *open-source* asset, not no integration.**
  The client may already pay for a vendor integration. Ask before positioning the work as
  greenfield.
- 🔵 **The empty tier is empty because of authorisation, so the credential conversation is
  the critical path.** Start it in week one; it will outlast the build.

## P29 — Curriculum alignment as a tool call (the Skolverket shape, and how to port it)

**When to use.** Any engagement where *"aligned to the national curriculum"* is a
procurement requirement — which, in EMEA and in the APAC mandate regimes, is most of them.
Replaces a human-written mapping that is stale on the day it ships with a call the product
makes on every run (trend 42).

### Components

| Component | Repo / source | Licence | Role |
|---|---|---|---|
| National curriculum surface | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP) | **MIT** (payload, 1,093 B) | Sweden: Läroplan/syllabus API, Skolenhetsregistret school-unit register, Planned Educations. The reference implementation to copy. |
| The counter-case to plan for | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** | Norway's equivalent public data, **no grant**. Read it as the expected state, not the exception. |
| Document ingestion | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Apache-2.0 | For the parts of a curriculum published as PDF rather than API — i.e. most countries. |
| Typed alignment claims | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | An alignment is a schema — `{objective_id, source_uri, confidence, evidence_span}` — never prose. |
| Orchestration | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | Re-run alignment as a graph step with checkpoints. |
| Retrieval | [pgvector/pgvector](https://github.com/pgvector/pgvector) | PostgreSQL Licence | Curriculum objectives indexed in-region. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | MIT outside `ee/` | Every alignment claim traceable to the call that produced it. |

### Wiring

1. **Check for an authority API first, then for a wrapper, then expect to write one.** The
   three outcomes, in order of likelihood: public API with no wrapper (write a thin MIT one —
   small, bounded, reusable); public API with an ungranted wrapper (fork the shape, write your
   own grant, or ask for one — see Udir); public API with a permissive wrapper (Sweden — the
   lucky case).
2. **Pin the curriculum version.** A syllabus API returns *today's* curriculum. An assessment
   decision made last term must be explainable against the curriculum as it stood then, so
   persist the objective set with a retrieval timestamp and never resolve historical claims
   against a live call.
3. **Make the alignment claim auditable, not confident.** Each generated item or lesson
   carries `{objective_id, source_uri, evidence_span}` pointing into the authority's own text.
   A reviewer must be able to click from an item to the clause it claims to satisfy.
4. **Re-run alignment on a schedule and diff it.** When the authority changes a syllabus, the
   diff is the client's change notice — and producing it automatically is a sellable
   capability on its own.
5. **Keep the data-terms diligence separate from the licence check**, per the warning below.

### Deliverables

- A curriculum-alignment service with a typed claim schema and per-claim provenance.
- A pinned, versioned local objective set with retrieval timestamps.
- A **data-terms memo**: what the authority's own terms permit for the data (distinct from the
  wrapper's licence), signed off before launch.
- An alignment-diff report, scheduled.
- P22 gate output for the wrapper.

### ⚠️ Two warnings that are the point of this pattern

- 🔴 **The wrapper's licence is not the data's licence, and this is the error the pattern
  exists to prevent.** Skolverket-MCP's copyright line reads **"Skolverket Syllabus MCP
  Contributors"**, *not the agency*. MIT covers the **code**; the **agency's terms govern the
  corpus**. A proposal citing "MIT" for a national-curriculum capability is citing the
  connector and implying the corpus — trend 22's corpus-pricing error arriving through a
  cleaner door.
- ⚠️ **Do not generalise "a permissive wrapper exists" from one country.** Two Nordic
  authorities, same idea, same public-data quality: one MIT, one ungranted. Budget the wrapper
  as work in every country until proven otherwise.

## P30 — Gated auto-grading with a real execution step

**When to use.** Assessment work — the regulated frontier this KB has tracked since trend 7,
and the one where the open-source tier has been thinnest. Three components verified this pass
make a complete loop possible under permissive licences **for the first time in this KB**:
grading from a vendor, execution in a sandbox, and mastery tracking.

### Components

| Component | Repo | Licence (payload read 2026-10-06) | Role |
|---|---|---|---|
| Exam authoring, delivery, **auto-grading** | [ictinnovations/ictexam-mcp](https://github.com/ictinnovations/ictexam-mcp) | **MIT** (1,114 B, **corporate holder**) | Read exams, gradebooks and **per-question item analysis**; parse a paper into a structured exam; publish to students. **Writes are off unless explicitly enabled** — adopt that default, do not reinvent it. |
| 🆕 **Code execution** | [taybenlor/runno](https://github.com/taybenlor/runno) | **MIT** (1,106 B) | WASM/WASI sandbox. **`@runno/mcp` 0.10.6 (MIT on npm)** makes the sandbox agent-callable, so the grader executes the submission instead of predicting its output. |
| Mastery, two families | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) · [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | MIT · **MIT** (1,067 B) 🆕 | Bayesian Knowledge Tracing (auditable, published) and **RL policy + FSRS scheduling**. Two different defensible answers to *"why this item next"*. |
| Standards conformance | [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | ISC | QTI 2.1/2.2/3.0 player, bidirectional QTI ↔ PIE. Keeps the item bank portable. |
| Typed outputs | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT | A grade is a schema with evidence, never a sentence. |
| Orchestration + gate | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT | The oversight gate is a node, and it cannot be routed around. |
| Observability | [langfuse/langfuse](https://github.com/langfuse/langfuse) | MIT outside `ee/` | The evidence pack is a by-product of running. |

### Wiring

1. **Author and deliver through the exam platform's read surface**; keep its write scope off
   until step 5 is in place. Pull **per-question item analysis** — it is the signal that tells
   you whether the *item* is bad rather than the cohort.
2. **Execute, do not predict.** For any submission that is code, run it in `@runno/sandbox`
   via `@runno/mcp` and grade the **actual** output. The model reasons about observed
   behaviour; it never asserts what the code "would" do.
3. **Grade into a typed claim**: `{score, rubric_id, evidence_span | execution_trace,
   confidence}`. Free-text justification is an attachment to the claim, never the claim.
4. **Route low confidence and every high-stakes item to a human**, and record the routing
   decision. US state law has converged on human judgment being final (trend 16); the EU
   treats this as high-risk.
5. **The write-back gate**: no grade reaches the gradebook except through a node that records
   a named human's decision. This is where the ICTExam write scope is finally enabled, and
   never before.
6. **Feed accepted outcomes into the mastery model** — BKT for an auditable, published
   instrument; RL+FSRS where review scheduling matters more than explainability. **Name which
   one, and why, in the deliverable.**

### Deliverables

- An auto-grading pipeline with writes gated behind a named human and traced end to end.
- Execution traces for every code-graded submission, retained with the grade.
- A rubric registry with per-rubric accuracy against the human-reviewed sample.
- Item-analysis reports distinguishing a weak cohort from a bad item.
- A mastery-model selection note: which family, what it can and cannot explain.
- P22 gate output for every component; P27's evidence pack as the external-facing artefact.

### ⚠️ Three warnings that are the point of this pattern

- 🔴 **A browser or WASM sandbox is not an anti-cheat boundary.** Runno protects the host from
  the code, not the assessment from the student. For proctored or high-stakes assessment,
  execution stays server-side; use Runno for formative practice, feedback and teaching.
- ⚠️ **Check Runno's language coverage against the client's actual curriculum.** WASI
  sandboxing covers languages with a WASI target; verify against the published packages
  rather than assuming.
- 🔴 **Borrow no benchmark into the deliverable.** The pedagogy benchmarks this KB has
  measured are licensed shut — Khan's dataset permits evaluation and forbids redistribution,
  production use and training; `CSTutorBench` is CC BY-NC. Evaluate with them where their
  terms allow, ship **none** of them, and keep the harness (P23) as the asset.

## P25 — The SIS integration engagement (wrap an MIT client; do not build the client, do not wait for a licensed MCP server)

**When to use it.** The client is a school district, a university or a federal institute, and
the ask is administrative rather than instructional: attendance, grades, scheduling,
guardian communication, enrolment, "an assistant that answers questions about our student
data." This is the shape of most K-12 engagements and most public-sector higher-education
engagements in Brazil.

**The finding it is built on** (fifteenth pass, `agents/top.md` Finding 4): in the
PowerSchool tier, **both MCP servers are ungranted and three of four API clients are MIT**.
The grant sits exactly one layer below the layer an agent engagement wants. So the cheapest
correct move is to take the licensed layer and write the thin one yourself.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) |
|---|---|---|
| SIS client — Python | [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | **MIT** |
| SIS client — Node | [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **MIT** |
| SIS client — PHP | [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | **MIT** |
| SIS client — FR | [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** |
| SIS client — DE/AT | [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | **BSD-2-Clause** |
| SIS client — NL | [`magister-api/magister`](https://github.com/magister-api/magister) · [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | **MIT** |
| SIS client — BR | [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) · [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | **MIT** |
| **MCP wrapper** | 🔧 **Globant-built** — ~300 lines over the client above | your client's terms |
| Reference design for the wrapper | [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) (20 tools, RBAC-aware) · [`kc0506/ntucool`](https://github.com/kc0506/ntucool) (Rust) | **MIT** — read them, do not necessarily deploy them |
| **Production access path** | OneRoster / Ed-Fi permissive implementations (interoperability tier, tenth pass) | permissive |
| Oversight gate | **P11** (gated generation) | — |
| Access-rights gate | **P26** — **run this first** | — |

### Wiring

1. 🔴 **Run P26 before writing any code.** If the institution has no API agreement with its
   SIS vendor, everything below is a prototype and must be labelled one in the SOW.
2. Pick the MIT client that matches the client's SIS and your delivery language. Vendor it,
   do not fork it — these libraries are small and stable, and the licence lets you.
3. Write the MCP server yourself over the client's own method surface. **Read
   `infinitecampus-mcp` first for its tool decomposition** (academics / daily life /
   documents / messaging / healthcheck) and for its RBAC middleware shape — this is the one
   governance-aware design in the tier.
4. 🔴 **Writes off by default.** Every tool that mutates a student record is opt-in, behind an
   explicit configuration flag, and routed through P11's oversight gate. The SIS is the
   system of record for regulated data; an agent that writes to it without a human gate is
   the single highest-liability thing in this entire KB.
5. Swap the transport, not the tools, when the official API arrives: keep your MCP tool
   signatures stable and re-point them from the community client to the OneRoster/Ed-Fi
   endpoint. **This is the whole reason to own the wrapper layer** — the access path changes
   and your deliverable does not.
6. Scope data egress explicitly: student records are FERPA (US), and under-13 data is
   additionally COPPA; in EMEA this is GDPR Article 9-adjacent and the EU AI Act's Annex III
   education classification applies. **Do not route student records through a shared LLM
   context and do not train on them.**

### Deliverables

- An MCP server the client owns, over a vendored MIT client, with writes gated.
- A P26 access-rights memo naming the vendor, the ToU clauses read, the date read, and
  whether an API agreement exists. **This is a deliverable, not an internal note.**
- A migration note: what changes when the official API entitlement lands (transport only, if
  step 5 was respected).

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **The community client's licence does not grant API access.** See **P26** and trend 33.
   An MIT licence on a scraper is a grant to copy the scraper.
2. ⚠️ **`GeovaneSchmitz/sigaa-api` (MIT, 61★) is archived and self-describes as a web
   scraper.** It is excellent reference material for how SIGAA's surface works and a poor
   production dependency. Prefer `PucaVaz/sigaa-tools` (MIT, 24★, active).
3. ⚠️ **`shinyquagsire23/InfiniteCampusAPI` is WTFPL** — permissive in substance, not
   OSI-approved, and rejected by name by some corporate allowlists. If the client runs an
   automated licence gate, expect to justify it or choose another client.

---

## P26 — The access-rights gate (run before any component that talks to a system you do not own)

**This is the gate trend 33 made necessary, and it is the first gate in this KB that does not
look at a licence.** P22 (the licence-reliability gate) answers *may we copy this code?*
P26 answers *may we call this system?* **A component must pass both.** Most of the SIS tier
passes P22 cleanly and fails P26.

### The gate — four checks, in order, all cheap

| # | Check | How | 🔴 Fail condition |
|---|---|---|---|
| **A1** | **Is the access path official?** | Read the component's README and source for the endpoints it calls. Compare against the vendor's published API documentation. | The component calls endpoints absent from the vendor's public API docs — mobile-app JSON, portal internals, HTML scraping. |
| **A2** | **What does the vendor's ToU say?** | Fetch the vendor's Terms of Use and search for: *publicly supported interfaces*, *scraping*, *automated access*, *crawl*, *train*, *artificial intelligence*, *reverse engineer*, *derivative*. **Record the URL and the date read.** | The ToU prohibits the means of access the component uses — or prohibits AI training on the content. |
| **A3** | **Does the institution hold an API agreement?** | Ask the client directly: *"do you have an API entitlement with your SIS vendor, and may we see its scope?"* | No agreement, or an agreement that does not cover programmatic third-party access. |
| **A4** | **What regulation attaches to the data?** | Classify the records the component reaches. | Student records without a lawful basis for the processing: **FERPA** (US), **COPPA** (US, under-13), **GDPR** + EU AI Act Annex III (EMEA), LGPD (Brazil). |

### Why all four, and in that order

**A1 is the cheapest and it predicts the other three.** A component that calls undocumented
endpoints will almost always fail A2, and A1 takes one README and one docs page. Run it
first and most candidates resolve in minutes.

**A2 is the one that is invisible to every tool in this KB.** It is not in the repository.
No licence scanner, SBOM, allowlist or payload probe reaches it — it lives on the vendor's
website, and it changes without notice, which is why the gate requires the **date read** to
be recorded next to the verdict.

**A3 is the one that converts a failure into a pass.** The same community client that is
unusable for a district with no entitlement becomes legitimate for a district with one,
because the institution's own contract covers the access. **This is the question that
decides whether the engagement is scoped as a prototype or as production.**

**A4 survives a pass on A1–A3.** Lawful access is not lawful processing. An institution may
be perfectly entitled to its own data and still unable to route it through a third-party
model.

### Outputs, and what each verdict means

| Verdict | Condition | What you may deliver |
|---|---|---|
| 🟢 **PRODUCTION** | A1 official **or** A3 agreement in place, A2 clean for the intended use, A4 lawful basis documented | Ship it. Normal P22 licence rules apply on top. |
| ⚠️ **PROTOTYPE ONLY** | A1 fails, A3 absent, A4 satisfiable | Build it, demo it, **label it in the SOW as a non-production proof of workflow**, and quote the official-API path as the production phase. |
| 🔴 **BLOCKED** | A2 prohibits the use and A3 cannot cure it, **or** A4 has no lawful basis | Do not deliver. Propose the official API or an open platform (⚠️ GPL — see `verticals/solutions.md`). |

### The worked example, from this pass

`chrischall/infinitecampus-mcp`, MIT, 20 tools:

- **A1** 🔴 fails — calls `/campus/api/oneRosterCampus` and `/portal/api/...`; the maintainer
  states these *"are not publicly supported interfaces."*
- **A2** 🔴 fails — [Infinite Campus ToU](https://www.infinitecampus.com/terms/terms-of-use)
  (quoted in the repository's README, read by the maintainer 2026-05-23) forbids access *"by
  any means other than our publicly supported interfaces (for example, scraping or using the
  content to train artificial intelligence software)"*; the maintainer adds that *"IC may
  treat this as a ToS violation."*
- **A3** — unknown per engagement; **this is the question to ask the district.**
- **A4** 🔴 FERPA and COPPA both attach; the repository itself says *"do not… train AI models
  on student records."*

⚠️ **Provenance:** the ToU wording above is quoted from the **repository's README** (the
maintainer dates their reading 2026-05-23); `infinitecampus.com` is egress-blocked from this
environment, so it is **not** first-hand verified here. **A2 therefore carries an explicit
re-read instruction** — that is exactly why the check requires the URL *and the date read*
to be recorded beside the verdict.

**Verdict: 🔴 BLOCKED as a deliverable; ⚠️ PROTOTYPE ONLY where a district authorises it on
its own data; 🟢 the production path is PowerSchool's or Infinite Campus's OneRoster
entitlement.** The licence was never the problem — and that is the whole point of this gate.

🔵 **Note for the proposal, not just the gate.** A cookie-bridge in a repository — such as
the browser extension `infinitecampus-mcp` uses to lift a session token from a logged-in tab
— is evidence that an install base wants agent access its vendor does not yet sell.
**That is a product opportunity to raise with the vendor, and an anti-pattern to decline in
client delivery.**

---

## P25 — Curriculum alignment against a government endpoint (EMEA, Norway shape — and the substitution for everywhere else)

**The problem every other curriculum pattern in this file has had to assume away.** `P9`, `P15`,
`P16` and `P19` all generate or align content "to the national curriculum" — and each one
quietly assumes a lawful, authoritative, machine-readable source of curriculum truth exists.
The sixteenth pass measured that assumption across five ministries: **it holds in one of them.**

In Norway it holds *completely*, and with a written commercial grant.

### Components (every licence payload-verified 2026-10-06)

| Role | Component | Licence |
|---|---|---|
| **Curriculum source of truth** | [`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL) — Grep SPARQL endpoint, Norway's **LK20** curriculum as RDF, **in production since 2020-12-07** | 🟢 **NLOD** — *"you are allowed to … use them for commercial purposes"* |
| Curriculum interface docs | [`Utdanningsdirektoratet/KL06-LK20-public`](https://github.com/Utdanningsdirektoratet/KL06-LK20-public) (wiki is the live reference) | 🔴 **ungranted** — read it, do not vendor it |
| Institution roster | [`NKAmapper/school2osm`](https://github.com/NKAmapper/school2osm) — every school in Norway's National School Register | 🟢 **CC0-1.0** |
| UI components | [`Utdanningsdirektoratet/designsystem`](https://github.com/Utdanningsdirektoratet/designsystem) | 🟢 **MIT** |
| Orchestration | LangGraph | 🟢 MIT |
| Local/sovereign inference | Ollama / vLLM | 🟢 MIT / Apache-2.0 |
| Vector + cache | Qdrant | 🟢 Apache-2.0 |
| Delivery surface | Moodle plugin (GPL-3.0, in-tree) **or** an MCP side-car (MIT, external) | see `P1` |
| Oversight gate | `P11` gated-generation gate | — |

### Wiring

1. **Pin the curriculum, do not live-query it.** Pull the LK20 competence aims, subjects,
   programme structures and cross-curricular topics from the Grep SPARQL endpoint **once per
   release**, and store the result with the query, the retrieval date and a content hash.
   🔵 **NLOD permits copying and reshaping, so a pinned local copy is licensed — and a pinned
   copy is the only way a tutor's alignment claim is reproducible three months later.**
2. **Materialise competence aims as addressable entities**, each carrying its official Grep
   identifier. The identifier is the whole point: it is what makes "aligned to LK20 aim
   *X*" checkable by someone who does not trust you.
3. **Index into Qdrant** keyed by competence-aim identifier, not by free text. Alignment is a
   join on an identifier, never an embedding similarity score.
4. **Generation runs through `P11`'s gate**: the model proposes items, each item must cite at
   least one competence-aim identifier that exists in the pinned snapshot, and **an item citing
   an unknown identifier is rejected mechanically, not reviewed.**
5. **Attribution is a build artefact.** Emit the NLOD string — *"Contains data under NLOD, made
   available on data.udir.no"* — into the UI footer and into the export metadata. ⚠️ **No Udir
   logo anywhere**, including slides.
6. **Teacher review before publication** (`P11`), with the citation visible in the review UI so
   the reviewer checks the *aim*, not the prose.

### Deliverables

* A pinned, hashed, dated curriculum snapshot plus the SPARQL queries that produced it.
* An item bank in which **every item cites a real competence-aim identifier**.
* A rejection log: items the identifier gate refused, which is the evidence the gate runs.
* An NLOD attribution and logo-restriction compliance note.
* ⚠️ **A data-liability note**: NLOD disclaims accuracy, so the alignment claim is *yours*.
  Budget a sampling validation and say who signs it.

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Do not port this pattern by analogy.** It works because a *specific* state publishes a
   *specific* endpoint under a *specific* licence. France: **no ministry estate** (the one
   curriculum RAG index found is ungranted). Japan: **documents only** — which is exactly why
   `compose/code/jp-cos-curriculum-gate` had to be built. The Gulf: nothing findable.
   🔵 **So in most countries the substitution is: ingest curriculum documents, build the
   alignment index yourself, and evidence it** — billable work in Japan, a free lookup in
   Norway. **The same proposal cannot be priced the same way in both.**
2. ⚠️ **NLOD grants the data, not a system.** `Grep_SPARQL` is endpoint documentation. There is
   no platform here; the client, cache, mapper and generator are yours.
3. ⚠️ **`KL06-LK20-public` and `pifu` are ungranted.** Use them as specifications to read, never
   as code to ship. 🟢 **And ask**: a ministry adding a `LICENSE` file is a one-commit change,
   and it is the highest-leverage upstream request in this KB.

---

## P26 — Early-childhood administration with an assistive-only AI layer (EMEA, municipal)

**A platform tier this file had no pattern for, and a buyer it had no shape for.** Every other
platform pattern here targets K-12, higher education or enterprise L&D. Early-childhood
education (ECEC) is bought by **municipalities**, runs on placement queues and income-based fee
decisions, and is subject to statutory child-ratio compliance.

🟢 **And it has a production open-source platform, adapted by a second city** — which is the
hardest test a public-sector codebase can pass.

### Components

| Role | Component | Licence |
|---|---|---|
| **ECEC platform** | [`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) — in production for the **City of Espoo** (Kotlin) | **LGPL-2.1-or-later** — ⚠️ grant is in **`LICENSES/`**, not `LICENSE` (REUSE spec v3.0) |
| **Adaptation precedent** | [`Tampere/trevaka`](https://github.com/Tampere/trevaka) — the same platform for the **City of Tampere**, active 2026-10-06 | **LGPL-2.1** (full 27,030-byte text) |
| Forecasting / analytics | your own module, **linked** against eVaka | 🟢 your licence — see wiring step 1 |
| Orchestration | LangGraph | 🟢 MIT |
| Oversight gate | `P11` | — |
| Compliance profile | `P13` (EU AI Act education profile) | — |

### Wiring

1. **Link, do not fork the core — this is the licence doing architecture.** LGPL-2.1-or-later
   means modifications *to eVaka's own files* must be published, while **your separate modules
   linking against it may stay proprietary**. 🔵 Same middle path this page already argues for
   LGPL-3.0 platforms: **put client-specific value in new modules, contribute core fixes back.**
   ⚠️ **eVaka is REUSE-compliant, so check per-file SPDX headers before assuming every file is
   LGPL** — the repository's default is LGPL-2.1-or-later, not a guarantee about each file.
2. **Read `trevaka` before you quote a timeline.** It is the only existing evidence of what
   adapting eVaka to a second municipality actually costs, and it is a real, current repository
   rather than a vendor estimate.
3. **Build the AI layer on capacity, not on eligibility.** Demand forecasting for placement
   capacity, staffing projections against statutory child ratios, anomaly review on attendance
   records, and caseworker drafting assistance.
4. **Every output is a draft with a named human decision-maker** (`P11`). The gate here is not
   a formality: it is the compliance position.
5. **Run `P13`'s profile** and document the determination.

### Deliverables

* A linked analytics/forecasting module with its own licence boundary documented file-by-file.
* A forecasting model with its training window, inputs and error characteristics stated.
* An oversight-gate record: every AI-touched decision, its human decision-maker, timestamp.
* A `P13` AI Act determination for each AI-touched function.
* ⚠️ A REUSE/SPDX licence inventory of the files you touched — produced by reading
  `LICENSES/` and per-file headers, **not** by reading `LICENSE`.

### ⚠️ Warnings

1. 🔴 **Do not automate placement or fee determination.** These are decisions about access to a
   public service for **small children** — a protected group under the most scrutiny of any
   population in this KB. Automating them is the one thing that converts a municipal reference
   client into a regulatory incident. **Assistive only, human decides, and say so in the
   proposal before the client asks.**
2. ⚠️ **The grant is not where your tooling looks.** eVaka's 1,001-byte `LICENSE` states
   verbatim that it contains *"never the original license texts"*. A probe reads NO-GRANT or
   guesses from prose; the real text is `LICENSES/LGPL-2.1-or-later.txt`. 🔵 **Validate any
   licence instrument against `compose/code/p432-fromscratch-fixture-gate/` first — `evaka` is
   fixture 4 there precisely because the correct answer is "I don't know from this file."**
3. ⚠️ **Child data is the most sensitive category this KB touches.** GDPR, national ECEC law and
   municipal data-protection officers all apply before the AI Act does. Scope the DPO
   conversation into week one.

---

## P27 — Curriculum-aligned tutoring on a national service estate, without forking it (EMEA, Finland shape)

**The pattern this page has needed since the EU AI Act's high-risk duties came into force in
August 2026, and the pass that found the substrate also found the reason not to fork it.**
`P25` works against Norway's Grep because **NLOD grants commercial reuse of the data outright**.
Finland's estate is bigger — **188 live repositories covering curriculum, learner identity, study
records, attainment, admissions and a national OER library** — and is **EUPL**, whose copyleft
reaches network delivery. 🟢 **So this pattern's thesis is a boundary: everything you fork is
MIT/Apache; everything EUPL you only ever call.**

### Components (every licence payload-verified 2026-10-06)

| Role | Component | Licence | Fork or call? |
|---|---|---|---|
| **Curriculum objectives** | [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) — national core curriculum + qualification requirements (`master`) | 🟡 **EUPL-1.1** (631 B) | 🔴 **CALL ONLY** |
| **OER content pool** | [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) — the national OER library, `aoe.fi` (`main`) | 🟡 **EUPL-1.2** (303 B, in subdirectories) | 🔴 **CALL ONLY** |
| **Prior attainment** | [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) — national study records (`master`) | 🟡 **EUPL-1.1** (653 B) | 🔴 **CALL ONLY** |
| **Identity / provider model** | [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) + [`organisaatio`](https://github.com/Opetushallitus/organisaatio) | 🟡 **EUPL-1.1** (631 B each) | 🟡 **READ THE MODEL**, write your own code — reading carries no obligation |
| Agent runtime | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | 🟢 fork freely |
| Tutoring loop | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** | 🟢 fork freely |
| **Auditable mastery model** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — Bayesian Knowledge Tracing | 🟢 **MIT** | 🟢 fork freely |
| Item generation | [`satvik314/educhain`](https://github.com/satvik314/educhain) | 🟢 **MIT** | 🟢 fork freely |
| Source-backed pedagogy | [`JuneYaooo/lineage-skill`](https://github.com/JuneYaooo/lineage-skill) | 🟢 **Apache-2.0** | 🟢 fork freely |
| Tool allowlist | `compose/code/mcp-allowlist-gateway/` | — | — |
| Oversight gate | `P11` | — | — |
| AI Act profile | `P13` | — | — |

### Wiring

1. **Put the licence boundary in the architecture diagram, not in a footnote.** Draw one line:
   north of it, the four Finnish services, reached **only** over HTTP. South of it, your
   Apache/MIT code. 🔵 **Nothing EUPL is ever compiled, vendored, copied or containerised into the
   deliverable** — and because "communication to the public" is Distribution under EUPL Art. 1,
   *hosting* a modified copy for the client is exactly the move that triggers the copyleft.
   **Calling an API is not.**
2. **Pull the objectives from `eperusteet` and cache them as your own derived index**, keyed by
   qualification and objective id. ⚠️ The *data* served by a EUPL-licensed service is not itself
   covered by the code's licence — but **do not assume it is open**: unlike Norway's NLOD, this
   pass established the **code** licence, not a data licence. 🔴 **Establish the terms of the data
   before a commercial deliverable depends on it** — that is one document, and it is not in this
   KB yet.
3. **Retrieve learning material from AOE** over its API and keep AOE's per-resource licence tag
   with every retrieved item. AOE exists to express OER licences (`edit-license` is a first-class
   component of its UI), so the metadata you need is already in the payload — **carry it through
   to the learner-facing citation** rather than discarding it at ingest. `p345-oer-four-forms`.
4. **Build the tutoring loop on `DeepTutor` + `smolagents`**, with the agent's tool surface
   restricted by `mcp-allowlist-gateway` to exactly: curriculum lookup, OER search, prior
   attainment read, item generation. 🟢 **smolagents is the right runtime here specifically
   because its surface is small enough to audit** — which is a conformity argument, not a
   preference.
5. **Do mastery estimation in `OATutor`'s BKT, not in the LLM.** 🔴 **This is the step that makes
   the deployment defensible.** Student evaluation is a **high-risk** function under the AI Act
   from August 2026; a Bayesian knowledge-tracing model has inspectable parameters and a stated
   error characteristic, and an LLM's judgement of mastery has neither. **The LLM explains and
   converses; the BKT decides what the learner knows.**
6. **Read `koski` for prior attainment, never write to it.** Treat it as the system of record it
   is.
7. **Gate every assessment-shaped output through `P11`** with a named human decision-maker, and
   **run `P13`** to produce the AI Act determination per function.

### Deliverables

* An agent layer whose entire dependency tree is MIT/Apache — **auditable in one `pip`/`npm`
  licence report**, with the EUPL services appearing as *endpoints*, not dependencies.
* A derived curriculum index with the provenance of every objective (service, qualification,
  retrieval date).
* A BKT mastery model with parameters, training window and error characteristics stated.
* OER citations carrying each resource's own licence tag end-to-end.
* A `P13` AI Act high-risk determination for the assessment and tutoring functions, plus the
  `P11` oversight record.
* 🟢 **A one-page licence-boundary memo** naming every EUPL service called and asserting that no
  EUPL code is distributed. ⚠️ **This is the document that makes the engagement sellable to a
  public buyer's lawyer** — produce it in week one, not at handover.

### ⚠️ Warnings

1. 🔴 **Do not fork the Finnish estate into a hosted product, and do not route around the
   copyleft via EUPL Art. 5.** The compatibility list is real (GPL-2.0/3.0, AGPL-3.0, LGPL,
   MPL-2.0, EPL, CeCILL, OSL) and the EC's own discussion notes the SaaS obligation **can be
   circumvented** by combining with GPL-3.0. **It is documented, it is contested, and selling it
   as a plan puts the client's compliance on a disputed reading.** Counsel decides, not an
   architect.
2. ⚠️ **The six EUPL-1.1 notices point at `http://www.osor.eu/eupl/`, which returns 403.** The
   repositories do not contain their own terms. **Pin the EUPL text from the EC's dated version**
   in the licence memo; do not cite the repository's URL.
3. 🔴 **Six of the nine repositories' default branch is `master`, not `main`.** Any script in this
   pattern that resolves a branch must use `git ls-remote --symref`. Hardcoding `main` writes
   two thirds of the estate down as missing.
4. ⚠️ **179 of the 188 repositories are unread.** If the engagement needs a service not in the
   component table, **probe its payload before designing against it** — the estate's licence
   picture is sampled, not established.
5. 🔴 **This pattern is Finland-shaped, and the substitution is not automatic.** For Norway use
   `P25` (Grep, NLOD, commercial reuse granted). For everywhere else, **the curriculum substrate
   has to be found before this pattern applies** — and four passes of ministry channels say most
   countries do not publish one.

---

## P28 — A standards-conformant student-data bridge with a no-training attestation (EMEA Sweden shape; the attestation travels to North America)

**Two findings this pass combine into one engagement.** Sweden publishes **SS 12000** — its
national standard for information exchange between school administration systems — with an
**Apache-2.0 reference implementation** from the national agency. North America's procurement
question, meanwhile, has hardened into a contractual term: **California AB 1159 prohibits using
student data to train AI models**, and Idaho SB 1227 imposes data-privacy requirements on school
AI tools. 🟢 **A conformant bridge plus a provable no-training boundary is the same build.**

### Components (licences payload-verified 2026-10-06)

| Role | Component | Licence |
|---|---|---|
| **Standards bridge** | [`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api) — SS 12000 reference implementation, Java (`main`) | 🟢 **Apache-2.0** (11,339 B, full text) — 🟢 **liftable into a closed product** |
| LMS tool surface | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — up to 103 Canvas tools, WCAG scanner, bulk grading | 🟢 **MIT** |
| Moodle surface (out-of-tree) | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** |
| Tool allowlist + egress control | `compose/code/mcp-allowlist-gateway/` | — |
| Oversight gate | `P11` | — |
| AI Act profile | `P13` | — |

### Wiring

1. **Lift the SS 12000 reference API as the canonical data shape** for roster, group, enrolment,
   person and activity. 🟢 Apache-2.0 means it can ship inside a closed, hosted product with
   attribution and notices — **no copyleft, no delivery-model constraint.** This is the one
   national-agency asset in this KB you can simply take.
2. **Map every LMS surface onto that shape, not onto each other.** Canvas via `canvas-mcp`,
   Moodle via `moodle-mcp-server` (⚠️ **MIT precisely because it sits outside the GPL Moodle
   tree** — keep it there; an in-tree plugin inherits GPL-3.0).
3. **Terminate all student-data egress at `mcp-allowlist-gateway`.** One process, one allowlist,
   one log. 🔵 **The attestation in step 5 is only as good as the number of places data can
   leave** — make that number one.
4. **Make the no-training boundary a configuration, not a promise:** no student-identifying field
   crosses the gateway to a model provider; retrieval sends objective ids and de-identified
   features; retention windows are declared per field and enforced at the gateway.
5. **Produce the attestation as a build artefact**, generated from the gateway's own allowlist and
   schema — so it cannot drift from the running system. ⚠️ **A hand-written attestation that the
   code can contradict is worse than none**: it is a representation about personal data.
6. **Run `P13`** where the bridge feeds any assessment function, and **`P11`** on every graded
   output. Note `canvas-mcp`'s bulk-grading tools are exactly the surface that turns this into a
   high-risk system — **gate them explicitly**.

### Deliverables

* An SS 12000-conformant bridge with a per-source field-mapping table.
* A gateway allowlist, as code, with the egress log it produces.
* 🟢 **A generated no-training-on-student-data attestation**, traceable to the allowlist and
  schema that enforce it — the artefact AB 1159 makes procurement-relevant and that most
  competitors answer with a sentence in a brochure.
* Per-field retention declarations enforced at the gateway.
* `P13` determinations and `P11` oversight records for graded outputs.

### ⚠️ Warnings

1. ⚠️ **SS 12000 is Swedish.** It is not an EU or Nordic standard by fiat, and **this KB has not
   established** that Finland's services can be reached through an SS 12000 shape. 🔴 **Do not
   imply a regional standard in a deck** — propose it as a data shape you have chosen and can
   defend, which is a true and sufficient claim.
2. 🔴 **The two most interesting Swedish documents are ungranted.**
   `Skolverket/dnp-usermanagement` (7★) and `dnp-provplattform` — the national digital-assessment
   platform and user-management specifications — are **NO-PAYLOAD**. Design against the
   Apache-2.0 reference API, **not** against those specs.
3. ⚠️ **"AI training is prohibited" is a per-vendor fact.** The fifteenth pass read one SIS
   vendor's Terms of Use; four remain unread and egress-blocked. **Cite the district's own
   vendor's ToU, dated, and price the verification** — do not assert a sector norm.
4. 🔴 **Do not let the attestation imply more than it covers.** It is a statement about **this
   deployment's egress**, not about the client's other systems, and the memo must say so in the
   first sentence.


## P34 — Certified-conformant assessment delivery (the first pattern in this KB built on a third party's audit)

**Added in the eighteenth pass of 2026-10-06.** Every component licence below was read from the
repository's own payload on `raw.githubusercontent.com` the same day.

**The engagement this serves:** a client — most often North American K-12 or higher ed, but the
shape travels — is procuring assessment delivery against a rubric that **scores interoperability**
(39% of US districts do, trend 28). They have a legacy item bank in QTI 1.2 or 2.x, an LMS they are
not replacing, and an AI item-generation ambition they cannot yet evidence as safe.

**Why this pattern exists and P11/P15 do not cover it:** those patterns *generate* items. This one
**delivers and scores** them, standards-conformant, with the conformance claim **certified by
1EdTech rather than asserted by us**.

### Components

| Role | Component | Licence (payload-verified 2026-10-06) |
|---|---|---|
| Item player (default) | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (© 2022-2024 Amp-up.io, LLC) — 🟢 **1EdTech Certified, QTI 3 Basic + Advanced "Delivery"** |
| Item player (Vue front end) | [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (© 2024) |
| Item player (framework-neutral) | [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (© 2026 AE Studio) |
| **Legacy migration + scoring + validation** | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (© 2026 Longsight, Inc.) — 12 npm packages, **QTI 1.2 / 2.x → 3 migrator** |
| PHP-side QTI support | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (© 2026 Kennisnet) |
| LMS doorway | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) or [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | Apache-2.0 — 🔵 **re-picked pass 24**: was `1EdTech/lti-1-3-php-library`, the **2,317-day-cold copy** of the same library (byte-identical payload); this one is **14 d** |
| Item generation | P11's gated generation chain | — |
| Audit trail | [`langfuse/langfuse`](https://github.com/langfuse/langfuse) | MIT **outside `ee/`** — exclude `ee/` from any vendored copy |
| Typed agent outputs | [`pydantic/pydantic-ai`](https://github.com/pydantic/pydantic-ai) | MIT |

### Wiring

1. **Migrate the item bank first, and make it the first deliverable.** `longsightgroup/qti3`'s
   migrator converts QTI 1.2 / 2.1 / 2.2 packages into QTI 3. Run its **validator** over the output
   and treat the validation report as a client-facing artefact. This is the step that stalls
   assessment projects, and it is the step that proves the engagement is real in week one.
2. **Deliver items through the certified player**, served as a side-car behind LTI 1.3 — the P1
   shape. The LMS keeps the roster and the gradebook; the player renders and runs response
   processing. **Do not fork the LMS.**
3. **Score with the player's own response processing**, not with a model. A QTI item carries its
   declared correct responses; scoring it is **deterministic and inspectable**. Keep the model out
   of the scoring path entirely — this is what makes the deployment defensible under the EU AI
   Act's high-risk assessment obligations and under US state law's "human judgment is final" rule
   (§16).
4. **Generate new items with P11's gated chain, then validate them with `qti3` before they ever
   reach a learner.** The generator proposes QTI 3 XML; the validator is the gate; a human approves.
   **A generated item that fails validation never renders** — the standard does half your oversight
   work.
5. **Trace every generation call through Langfuse.** The audit trail is a by-product of normal
   operation, not a separate compliance project.

### Deliverables

- A migrated, **validated** QTI 3 item bank, with the validation report.
- A certified-player delivery tier behind LTI 1.3, with **the issuer and scope of the 1EdTech
  certificate cited by name** in the bid.
- A deterministic scoring path with the model demonstrably outside it.
- A generation pipeline whose output is gated by standards validation **and** human approval.

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Verify the certificate at the issuer, not in the README.** This KB read the conformance
   claim from the vendor's own repository. By §23's rule that is a claim to check against its
   issuer — **read 1EdTech's certified-products register and record the certificate's scope and
   date** before it goes in a bid. Declared gap 6 of this pass.
2. 🔴 **Two QTI components on the shelf are copyleft, and one of them is the most mature.**
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components) is **GPL-3.0** (2,456
   commits, Cito's lab) and [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) is **GPL-2.0** —
   *not* compatible with GPL-3.0-only code. If the renderer is on the critical path and Citolab's
   maturity is what you want, **read §43 and ask them**: their README advertises willingness to
   relicense. That is an invitation to negotiate, **never a grant** — settle it in writing before
   any architecture depends on it.
3. 🔴 **Do not cite [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components).** It
   is a **stale fork** of the Citolab repository, 79 commits behind, 1★. Pin the upstream address.

## P35 — The national open-data MCP client (LATAM, and portable to every CKAN portal in the region)

**Added in the eighteenth pass of 2026-10-06.** This is the pattern that follows from §44: in LATAM
the state publishes **data**, not code, and the only clients that reach it are third-party.

**The engagement this serves:** a LATAM ministry, university system or edtech client needs an agent
that can answer questions against **national education data** — enrolment, establishment directory,
teaching staff, graduates — and there is **nothing to fork from the state**.

### Components

| Role | Component | Licence / status |
|---|---|---|
| The data | **Mineduc Chile, Centro de Estudios** — **21 datasets** via [`datos.gob.cl`](https://datos.gob.cl) and its own *Datos Abiertos* portal | 🔴 **Portal terms of use — read them; the dataset's licence is not the wrapper's licence (§42)** |
| Reference client | [`pipeworx-io/mcp-datos-cl`](https://github.com/pipeworx-io/mcp-datos-cl) | **MIT** (© 2026 **Mojibake Inc.**) — a CKAN **MCP server** for `datos.gob.cl` |
| Second reference | [`gerardbourguett/mcp-chilegob-dataset`](https://github.com/gerardbourguett/mcp-chilegob-dataset) | **MIT** (© 2025, **an individual**) |
| Agent layer | `pydantic-ai` (MIT) or `smolagents` (Apache-2.0) | typed/auditable outputs |
| Local inference | [`ollama/ollama`](https://github.com/ollama/ollama) | MIT — keeps queries in-country |
| Audit trail | `langfuse/langfuse` | MIT outside `ee/` |

### Wiring

1. **Read the portal's terms of use before writing a line.** CKAN is the software; the **dataset
   licence and the portal ToU are separate instruments** and they govern what the client may do with
   the answers. This is step one, not diligence to be done later.
2. **Treat the two existing MCP servers as reference implementations, not dependencies.** Read them,
   credit them, and write a maintained one. Both are MIT so this is permitted; the point is that
   **neither is a supply chain you should put a client on** — see the warnings.
3. **Target CKAN, not Chile.** `datos.gob.cl` is a CKAN instance, and so are most LATAM national
   open-data portals. A client written against **CKAN's API** with the portal as configuration is
   portable across the region at near-zero marginal cost; one written against Chile is not.
4. **Put the agent behind typed outputs and local inference.** Education statistics answered by an
   agent are a reporting artefact; schema-checked outputs beat free text, and `ollama` keeps the
   queries in-country where the procurement asks for it.
5. **Cache and version the data pulls.** National statistical datasets are **revised**. An answer
   that cannot name which release it came from is not usable in a ministry report.

### Deliverables

- A maintained, permissively licensed **CKAN MCP client**, portal-configurable, with the Chilean
  education datasets as the first configuration.
- A terms-of-use memo distinguishing **dataset licence** from **portal ToU** from **wrapper
  licence**.
- A versioned data-pull layer with release identifiers in every answer.

### ⚠️ Four warnings that are the point of this pattern

1. 🔴 **The incumbent is one company and one individual.** `mcp-datos-cl` is held by **Mojibake
   Inc.** and `mcp-chilegob-dataset` by a single named person. Putting a ministry client on either
   is a **supply-chain risk**, and saying so is the honest version of this opportunity — not a
   reason to disparage either repository, both of which are MIT and useful.
2. 🔴 **The data's licence is not the wrapper's licence.** §42, confirmed in a second region this
   pass. An MIT MCP server over a dataset with restrictive terms **grants you nothing about the
   data**. Both instruments must be read.
3. 🔴 **The portal itself was never reached from here.** `datos.gob.cl` is **EGRESS_BLOCKED**
   in this environment, so the **21 datasets** figure and the dataset inventory are **Tier 2** — search
   results, not a first-hand read. The two MCP repositories were verified first-hand. **Confirm the
   portal's contents and its terms of use from a host that can reach it before step 1 is billable.**
4. ⚠️ **This pattern is specified from Chile and Mexico only.** Colombia, Brazil, Peru and Argentina
   were **not** probed this pass. The CKAN-first design is what makes the untested regions cheap to
   add — it is not evidence that they are the same.

## P36 — The accessible-courseware remediation line (North America Title II shape; ports to EMEA under the EAA and to APAC unchanged)

**Added in the nineteenth pass of 2026-10-06.** The first pattern in this KB whose trigger is an
**accessibility** obligation rather than an AI one, and the first whose entire toolchain is
permissive while its *outcome* depends on priced human labour. Read `repos/foundations.md` (engine
tier) and `agents/top.md` (agent tier) before scoping it.

**The buyer and the trigger.** A public school district, community college or public university in
the United States, covered by the **DOJ rule under ADA Title II** (published 2024-04-24, technical
standard **WCAG 2.1 Level AA**). ⚠️ **The date is the thing most proposals will get wrong:** the DOJ
**Interim Final Rule of 2026-04-20** extended compliance to **2027-04-26** for entities serving
≥50,000 people and **2028-04-26** for smaller entities and special districts — DOJ's own reason
being that it had *"overestimated the capabilities (whether staffing or technology) of covered
entities to comply."* 🔵 **Sell the capacity, not the date.** The backlog did not shrink; the buyer
was simply told it has another year, and the extension is documentary evidence that the buyer
cannot staff this alone.

### Components (every licence read from the repository's own payload, 2026-10-06)

| Role | Component | Licence | Why this one |
|---|---|---|---|
| Deterministic web scan, in CI | [IBMa/equal-access](https://github.com/IBMa/equal-access) | **Apache-2.0** | 9 packages: Node CLI, Cypress, Karma, Vitest and **Java** bindings — it runs inside the client's existing pipeline, including a JVM LMS |
| Second opinion / gate | [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | **Apache-2.0** | Local-only execution, so it is quotable under a data-residency clause |
| The criterion ledger | [tomaszboloz/WCAG-Accessibility-Skills](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) | **MIT** | **All 86 active WCAG 2.2 criteria**, each classed automated / semi-automated / **manual**, with a per-criterion manual queue and **zero production dependencies**. This is the component that makes the deliverable an audit rather than a scan |
| Guided human assessment | [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web) | **MIT** | Walks a human through what no engine can decide |
| Agent orchestration | [Community-Access/accessibility-agents](https://github.com/Community-Access/accessibility-agents) | **MIT** (engine: axe-core, **MPL-2.0**) | v7.0.3, 11 agents, **39 MCP tools**, WCAG 2.2 AA, and it reaches **Office documents, PDF and ePub** — where courseware lives |
| Agent scan tool, no account | [ronantakizawa/a11ymcp](https://github.com/ronantakizawa/a11ymcp) | **MIT** (engine: axe-core, **MPL-2.0**) | 6 tools, `npx`, no API key — the fallback when the client forbids a vendor account |
| OCR for scanned material | [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** | 100+ languages, and **hOCR / ALTO / PAGE** output that a tagging step can consume |
| Searchable-PDF pass | [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | ⚠️ **MPL-2.0** | Text layer + PDF/A. 🔴 **Searchable ≠ accessible** — see warning 2 |
| PDF/UA validation | [veraPDF](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL/MPL** (`LICENSE.GPL` / `LICENSE.MPL`) | **Invoke as a CLI only** |
| Captions and audio description | [`whisper.cpp`](https://github.com/ggml-org/whisper.cpp) + [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) 🔵 *(re-picked pass 24; was `rhasspy/piper`, archived, head commit 407 d)* | **MIT** + **MIT** | Already on this KB's shelf. Title II's final rule covers **captioning and audio description**; both run on-premise, which is what an education-records clause requires |
| Screen-reader verification | [nvaccess/nvda](https://github.com/nvaccess/nvda) | GPL-2.0+ — **as a test client** | Free and scriptable; "verified with NVDA" costs nothing and is the line a scanner report cannot produce |

### Wiring

1. **Inventory before anything else.** Crawl the estate and classify by *artefact type*, not by
   page: LMS pages, PDFs, ePubs, Office documents, video. ⚠️ **The four have different standards,
   different tools and different unit costs; a single "pages remediated" number is how this
   engagement loses money.**
2. **Gate the web tier in CI.** `equal-access` Node CLI (or its Cypress/Vitest binding) on every
   build, Lighthouse as a second opinion. Fail the build on new violations only — a legacy estate
   will never pass from a standing start, and a permanently red gate gets switched off.
3. **Open the criterion ledger.** Initialise `WCAG-Accessibility-Skills` over the estate. It
   partitions the 86 WCAG 2.2 criteria into automated, semi-automated and manual. 🟢 **The manual
   partition is the quote**: it is the labour nobody can automate away, enumerated per criterion
   before the contract is signed rather than discovered in month three.
4. **Run the agent layer over documents, not pages.** `accessibility-agents` via MCP across the
   Office/PDF/ePub corpus. Its 39 tools produce findings with locations; the agent **triages and
   drafts fixes**, it does not certify.
5. **Scanned material:** Tesseract → structured output (hOCR/ALTO) → OCRmyPDF for a searchable
   PDF/A → **human tagging** → veraPDF CLI to validate PDF/UA. 🔴 **Step four is a person.** There is
   no permissive engine that produces tagged, structurally accessible PDF (searched this pass).
6. **Media:** `whisper.cpp` for captions, human correction pass, `sherpa-onnx` for audio description
   tracks. On-premise throughout.
7. **Verify, then claim.** `accessibility-insights-web` for the guided human assessment, NVDA for a
   real screen-reader run, then a conformance report that states **pass / fail / undetermined per
   criterion** — WCAG-EM's own vocabulary.

### Deliverables

- An estate inventory partitioned by artefact type, with a unit cost per type.
- A CI gate the client owns, on Apache-2.0 components, running in their pipeline.
- **A per-criterion ledger** with the automated / semi-automated / manual split made explicit, and
  the manual queue sized in hours.
- Remediated web tier, remediated document tier, captioned and described media.
- A conformance report in pass / fail / **undetermined** form, naming engine versions and dates.
- An SBOM listing **axe-core (MPL-2.0)**, **OCRmyPDF (MPL-2.0)** and every Apache-2.0/MIT component.
- A regression baseline so the next content upload does not undo the work.

### ⚠️ Five warnings that are the point of this pattern

1. **Never claim "compliant" from a tool.** Automated testing finds a fraction of barriers. Every
   component here says so in its own README — `WCAG-Accessibility-Skills` encodes it as data, and
   even the MIT-over-SaaS adapter this KB rejected ships a coverage disclaimer in every response.
   🔴 **A conformance claim is a human's signature over an engine's evidence.** Say "WCAG 2.1 AA
   conformance claim, supported by X and verified by Y", never "we ran a scanner and it is green".
2. **A searchable PDF is not an accessible PDF.** OCRmyPDF gives you text and PDF/A; **PDF/UA needs
   tags, reading order and structure**, and nothing permissive produces them. ⚠️ **If a proposal
   implies the document estate is automatable, it has mispriced the largest line item in the job.**
3. **MPL-2.0 is fine until someone edits a rule file.** axe-core and OCRmyPDF are **file-level**
   copyleft: unmodified use does not reach the studio's code. **Patching an axe-core rule puts that
   file under MPL-2.0 with source disclosure.** Tune through configuration, and put both in the SBOM.
4. **Do not fork the assistive application.** Cboard is GPL-3.0, AsTeRICS Grid is AGPL-3.0, NVDA is
   GPL-2.0+. Integrate at the **file-format** boundary — generate board sets as data, test against
   NVDA — and no obligation reaches the deliverable (`verticals/solutions.md`).
5. **Do not demo sign-language translation on `sign/translate`.** Its licence is **non-OSI and
   entity-tiered**: free for educational institutions, **separate commercial licence required for
   for-profit organisations**. The client may run it; **the studio may not deliver it.**

### 🔵 Porting the pattern

| Region | What changes | What does not |
|---|---|---|
| **North America** | 🟢 **Nothing — this is the base case the pattern is written from.** The trigger is the DOJ rule under **ADA Title II**, whose deadlines the **2026-04-20 interim final rule** extended by a year to **2027-04-26** (public entities serving ≥50,000) and **2028-04-26** (below that, and special districts); the standard remains **WCAG 2.1 Level AA**, unchanged. 🔵 **Row added in the twentieth pass** because a porting table that omits its own origin reads, from outside, like a region that was never measured | Everything below |
| **EMEA** | The trigger becomes the **European Accessibility Act** (in force **2025-06-28**) and the standard becomes **EN 301 549**. ⚠️ **As of 2026-07-20 no EN 301 549 version had been cited in the Official Journal under the EAA** (v4.1.0 of Nov 2025 still in Public Enquiry and Vote to Aug 2026), **so there is no presumption of conformity to lean on** — which makes the per-criterion evidence ledger *more* valuable, not less. 🔴 **No permissive tool maps findings to EN 301 549 clauses**; the mapping is a studio artefact, and it is reusable IP | The toolchain. EN 301 549 is substantially WCAG 2.1 AA for web content |
| **APAC** | The trigger is a standing mandate, not a deadline: **India** RPwD Act 2016 + **GIGW 3.0** (WCAG 2.1 AA, government portals including education); **Japan** **JIS X 8341-3:2016** ≈ WCAG 2.0 AA, mandatory for government; **Australia** AHRC guidance (April 2025) affirming **WCAG 2.2 AA** under the 1992 DDA, plus the DTA Digital Experience Policy. ⚠️ **Three countries, three WCAG versions — the ledger must be configurable by target version** | Everything else |
| **LATAM** | 🔴 **There is no accessibility deadline to sell against.** The demand driver is a programme — UNICEF's **Accessible Digital Textbooks** — and the economics are the pitch: a conventional accessible textbook takes **6–9 months and up to USD 50,000 per title**, Paraguay has embedded ADTs in national inclusive-education policy, **Uruguay produced the world's first AI-led ADT prototype in 2025**, and Brazil's **PNLD** reaches **40M+ students**. 🟢 **Here the deliverable is the production line itself**, benchmarked against that 6–9-month baseline | The document pipeline (steps 5–6), which *is* the ADT production problem |

---

## P-TRANSITION-EVIDENCE — The transition-evidence mandate (bank the extension instead of spending it)

> ⚠️ **This pattern deliberately carries a name instead of a number.** `compose/patterns.md`
> already defines **P28 three times** (lines 1790, 2205, 2777), and this file's own audit
> (`compose/code/pattern-citation-audit/`) reports **36 patterns defined** against citations
> running into the **P60s** inherited from the pre-reset era. Taking another number would add a
> fourth P28 or a second dangling P37. 🟢 **Cite this pattern as `P-TRANSITION-EVIDENCE`** — the
> prescription of trend 47 ("A knowledge base that corrects itself needs unambiguous pointers"),
> applied to itself rather than only recommended.

**Twentieth pass of 2026-10-06.** Follows from trend **46** ("The date that governs a client's
system is in the transition article…"). Every transition regime this KB found discharges on an
**artefact**, not on a date — and in the EU the extension survives only while *"the design remains
unchanged"*. P28 is the engagement that produces the artefact **without** triggering the change.

🔵 **It is the first pattern in this KB whose selling point is what it does not touch.** Every other
pattern here adds a capability to a client's estate. P28 wraps a frozen high-risk core in evidence,
so the client keeps an extension worth up to **2030-08-02** (EU public authority) or **2027-09-01**
(Vietnam, education) instead of forfeiting it on the day a tutor ships.

**Sell it when:** the client operates an AI system that is **already in service** and falls in a
high-risk category — admissions or placement scoring, automated assessment or grading, proctoring or
behaviour monitoring — and asks what the AI Act, Vietnam's Decision 33 or Peru's reglamento means for
it. ⚠️ **Sell it *before* P1, P3, P11 or P13 on the same system**, because those modify it. P28 is
the phase that establishes the baseline the later phases will be measured against — and if the
client decides not to modify, it is the whole engagement.

### Components

All licences read from the repository's own payload on 2026-10-06; full rows in
`repos/foundations.md`.

| Role | Component | Licence (payload-verified) | Why this one |
|---|---|---|---|
| **System-identity record** | [`mlflow/mlflow`](https://github.com/mlflow/mlflow) | **Apache-2.0** (`LICENSE.txt`) | 28.3k★. **The Art. 111 instrument.** Register the deployed model and its config as a versioned, dated entry. The extension's condition is *"design unchanged"* — this is what makes that a statement with evidence behind it rather than an assurance. |
| **Corpus identity** | [`iterative/dvc`](https://github.com/iterative/dvc) | **Apache-2.0** (`LICENSE`) | 15.9k★. Hashes the training and retrieval corpus in Git. Vietnam's Decision 33 education category 1 turns on *"uncontrolled data sources"*; a hash is the only non-rhetorical answer to it. |
| **Corpus control gate** | [`great-expectations/great_expectations`](https://github.com/great-expectations/great_expectations) | **Apache-2.0** (`LICENSE`) | 11.9k★. Expectation suites over the corpus, run in CI. Turns "the sources are controlled" into a build that fails when they are not. |
| **Behaviour baseline** | [`evidentlyai/evidently`](https://github.com/evidentlyai/evidently) | **Apache-2.0** (`LICENSE`) | 8.0k★. ML **and LLM** observability. Captures how the frozen system behaves *now*, which is what any later modification gets compared against. |
| **Label-free performance watch** | [`NannyML/nannyml`](https://github.com/NannyML/nannyml) | **Apache-2.0** (`LICENSE`) | Estimates performance **without ground truth**. Education's outcome labels arrive a term or a year late; a monitoring plan that waits for them is not a monitoring plan. |
| **Privacy-shaped telemetry** | [`whylabs/whylogs`](https://github.com/whylabs/whylogs) | **Apache-2.0** (`LICENSE`) | 2.8k★. Emits **statistical profiles, not raw records** — the only shape that survives California **AB 1159** (student data may not be used to train models) and the EU data-minimisation posture. |
| **Fairness evidence over the decision** | [`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn) **or** [`Trusted-AI/AIF360`](https://github.com/Trusted-AI/AIF360) | ✅ **MIT** / **Apache-2.0** | 2.3k★ / 2.9k★. Annex III §3 is admissions, assessment, placement and test monitoring — decisions **about people**. Pick Fairlearn when the client wants MIT and a smaller surface; AIF360 when they want the metric catalogue and mitigation algorithms. |
| **Lineage as a standard** | [`OpenLineage/OpenLineage`](https://github.com/OpenLineage/OpenLineage) | **Apache-2.0** (`LICENSE`) | 2.7k★. So the evidence outlives your pipeline choice and a successor supplier can read it. |
| **Published provenance format** | [`mlcommons/croissant`](https://github.com/mlcommons/croissant) | **Apache-2.0** (`LICENSE.md`) | 907★. Dataset provenance in a format a ministry or an auditor can read without your toolchain. |
| **Accessibility queue (non-modifying)** | [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) + the engine tier from the nineteenth pass | **MIT** | Remediating the *presentation* estate is billable work that does **not** change the high-risk system's design. The nineteenth pass established there is **no cited standard under the EAA**, so the deliverable is per-criterion evidence — which is what this produces and the big engines do not. |
| 🔴 **Excluded** | [`deepchecks/deepchecks`](https://github.com/deepchecks/deepchecks) (**AGPL-3.0**) · [`sodadata/soda-core`](https://github.com/sodadata/soda-core) (**Elastic License 2.0**, non-OSI) | — | Named so a later pass does not rediscover them as options. |

### Wiring

```
  ┌───────────────────────────────────────────────────────────────┐
  │  CLIENT'S HIGH-RISK SYSTEM — FROZEN. NOT TOUCHED BY P28.      │
  │  admissions scoring · auto-grading · proctoring · placement   │
  └───────────┬───────────────────────────────┬───────────────────┘
              │ read-only telemetry           │ read-only config/model read
              ▼                               ▼
      whylogs (profiles,            MLflow registry entry
      not raw records)              = "this is the system,
              │                       as of this date"
              ▼                               │
      Evidently  ──────┐                      │
      NannyML    ──────┤                      │
      Fairlearn/AIF360 ┤                      │
                       ▼                      ▼
              ┌──────────────────────────────────────┐
              │  EVIDENCE PACK (the deliverable)     │
              │  · design-stability attestation      │
              │  · corpus manifest (DVC + Croissant) │
              │  · GX suite results                  │
              │  · behaviour + fairness baseline     │
              │  · OpenLineage event log             │
              │  · per-criterion WCAG queue          │
              └──────────────────────────────────────┘
                       │
                       ▼
        filed where the regime wants it:
        EU → the client's technical documentation
        Vietnam → the one-stop portal transition plan
        Peru → the algorithmic-transparency mechanism
```

⚠️ **The arrows are deliberately one-way.** The moment a component writes back into the high-risk
system — a retrained model, a changed threshold, a new retrieval source — the pattern has become a
modification and the extension is gone. **Enforce it in the architecture, not in the statement of
work:** read-only credentials on the model and corpus stores, and a separate repository for the
evidence pipeline.

### Deliverables

1. **The design-stability attestation** — a dated, versioned record of the system as it stands, with
   the registry entry and corpus hashes behind it. ⚠️ Written so that a *later* change is detectable
   by comparison, which is the only form that is worth anything.
2. **The corpus manifest** — DVC hashes plus a Croissant description, naming every source and
   whether it is controlled.
3. **The behaviour and fairness baseline** — Evidently reports, NannyML estimates and a **stated
   choice of fairness metric with the reasoning for it**.
4. **The filing** — Vietnam's portal notice and transition plan; the EU technical documentation
   section; Peru's algorithmic-transparency mechanism. 🔵 **Jurisdiction decides the artefact's
   form, not its content.**
5. **The accessibility remediation queue** — per-criterion, with engine, version and who judged what.
6. **The modification register** — the running list of changes the client *wants*, each annotated
   with whether it forfeits the extension. 🟢 **This is the document that sells the next phase**, and
   it is honest: it tells the client what their roadmap costs in compliance terms before they commit.

### ⚠️ Three warnings that are the point of this pattern

🔴 **One. P28 does not make the client compliant, and must never be sold as if it did.** It preserves
an extension and builds the evidence a conformity assessment will need. The assessment itself is
P13's scope. A proposal that blurs the two is the kind of over-claim a regulator reads closely.

🔴 **Two. Check whether the client is a public authority before pricing this.** The EU's
**2030-08-02** date attaches to high-risk AI **intended to be used by public authorities** — a state
university or a ministry gets it; a private tutoring company does not, and for them the governing
date is **2027-12-02** with only the design-stability route available. ⚠️ **The same engagement is
worth four years to one buyer and two months to another.**

🔴 **Three. Two deadlines in this pattern have already passed.** Vietnam's Decree 142 filing was due
**before 2026-06-30**, and Peru's education-sector obligations activated **2026-09-10**. 🟢 **For a
client in either market the first task is not a plan, it is establishing what was missed** — and
saying so in week one is the difference between a remediation engagement and a discovered failure.
⚠️ **And the dates themselves came to this KB through search summaries, not primary texts** (the
legal sources are `EGRESS_BLOCKED` from this environment) — **re-read the instrument before quoting
any of them to a client.**

### How P28 changes by region

| Region | What changes | What does not |
|---|---|---|
| **EMEA** | The prize is the **2030-08-02** public-authority date, and most education buyers qualify. The filing is technical documentation under the AI Act. ⚠️ **No harmonised standard has been cited under the EAA**, so the accessibility half cannot be discharged by naming a standard — it must be per-criterion evidence | The design-stability condition, which is the whole mechanism |
| **APAC** | **Vietnam**: the prize is **2027-09-01** (education's 18-month extension), the filing is the one-stop portal transition plan, and Decision **33/2026/QĐ-TTg** names the three education categories — uncontrolled-source self-learning content, automated assessment/grading/ranking, and **biometric** behaviour monitoring. **Korea**: fines are deferred to ~**2027-07-21**, but 🔴 **generated-content labelling has no grace at all**, so the labelling limb ships immediately | The artefact set |
| **LATAM** | **Peru** is the one market with a live, education-naming obligation — **activated 2026-09-10**, staged **1–4 years from September 2025** by sector and size, requiring algorithmic-transparency mechanisms for high-risk systems. 🔴 **Brazil has no AI statute in force** (PL 2338/2023 still in the Chamber, vote deferred past the October elections), so there the pitch is readiness, not compliance | The evidence pack, which is cheap to re-file once a statute lands |
| **North America** | ⚠️ **There is no transition article, because there is no binding federal high-risk statute.** P28 sells against the **procurement rubric** (see P24) and against **state** duties that attach at enactment — California **AB 1159** on student data, Oklahoma and Maryland on human oversight. The one real date is the DOJ ADA Title II IFR: **2027-04-26** for entities serving ≥50,000, **2028-04-26** below that | The accessibility queue, which is the North American half of this engagement |

---

## P-DEPENDENCY-CLOSURE — The dependency-closure clearance (run it before the proposal, not after the build)

> 🟢 **Cite this pattern as `P-DEPENDENCY-CLOSURE`**, not as a number. The pattern-number space in
> this file has **6 numbers carrying 2–3 competing definitions each** (`P25`–`P30`), and
> `compose/code/pattern-citation-audit/` now asserts against adding a seventh. A content key cannot
> collide and cannot dangle.

**The engagement problem.** Every recommendation in this KB rests on a licence read from the
repository's own `LICENSE` payload — rigorously, reproducibly, and **one declaration short.** A
client contract is not signed against the code a maintainer wrote; it is signed against **the build
you hand over**, which includes everything the manifest pulls in. Measured on this shelf: **4 of 13**
audited projects install something their own licence does not cover, and the single most-starred
asset in this KB — **DeepTutor, Apache-2.0, 40.8k★** — installs **AGPL-3.0-or-pay-Artifex** through
`PyMuPDF`.

**When to run it.** During discovery, before any fixed-price commitment on an open-source education
build. ⚠️ **The cost asymmetry is the entire argument: one command during discovery, versus a
source-disclosure obligation or an emergency commercial licence after a hosted tutor has shipped.**

### The recipe, concretely

| Step | Component | Licence | What it does |
|---|---|---|---|
| 1 | `compose/code/dependency-licence-closure/resolve.py` | this KB | Reads each candidate's manifest from `raw.githubusercontent.com/<slug>/<ref>/<path>` at a **pinned ref**, parses the direct runtime deps, resolves each one against `pypi.org/pypi/<name>/json` or `registry.npmjs.org/<name>`, and classifies it into five classes |
| 2 | `dep_licence.py` classifier | this KB | `NONCOMMERCIAL` → `STRONG-COPYLEFT` → `WEAK-COPYLEFT` → `PERMISSIVE` → `UNKNOWN`, **in that order** — `AGPL`, `GPL` and `LGPL` all contain the substring `GPL`, and collapsing them is the difference between one real finding and forty false ones. **48/48 offline assertions** |
| 3 | the four manifest shapes | — | `pyproject.toml` (PEP 621), `pyproject.toml#<group>` (**PEP 735** — required for Kolibri, whose `[project].dependencies` is literally `[]`), `requirements.txt`, `package.json` (runtime `dependencies` only, never `devDependencies`) |
| 4 | **the positive control** | — | ⚠️ **Do not ship a closure report without one.** At least one target must come back a **genuine zero** — here, `tomaszboloz/WCAG-Accessibility-Skills`, whose manifest confirms its own documented *"no production dependencies"*. An instrument that cannot tell "zero declared" from "I read the wrong file" is measuring nothing |
| 5 | the verdict, written for counsel | — | `BLOCKER` (non-commercial — no linkage argument rescues it) · `REVIEW-STRONG` · `REVIEW-WEAK` · `REVIEW-UNKNOWN` · `CLEAN`. ⚠️ **`REVIEW-*` means "a lawyer should read this row", never "this is a violation"** |
| 6 | the remediation choice | — | For a `REVIEW-STRONG` row: **comply** for the embedding service, **buy** the commercial grant, or **replace** the component. For DeepTutor's `PyMuPDF` the third is usually cheapest — the PDF layer is swappable, and `pypdf` (**BSD-3-Clause**, verified this pass via `license_expression`) is the drop-in candidate to evaluate |

### What the deliverable is

🟢 **A one-page table per candidate: its licence, its declared direct dependency count, its verdict,
and the specific rows that produced the verdict** — plus the three limits stated on the page itself,
because a verdict quoted past its limits becomes wrong data:

1. **Depth 1 only.** Transitive dependencies are not measured. `certifi` (MPL-2.0) is in nearly
   every Python deployment and surfaced here only where it was declared directly.
2. **Linkage is not analysed.** Whether an AGPL import makes the importer a derivative work depends
   on how the thing is used and distributed.
3. ⚠️ **"Not measured" is never reported as "clean."** Workspace roots (`mentingo`, `OpenTutor`)
   keep their runtime deps in `apps/*` and were left explicitly unmeasured.

### Why it sells in all four regions, and differently in each

| Region | The buying reason |
|---|---|
| **North America** | No sector regulator to point at, so **counsel and procurement** are the gate. The closure report is the artefact that clears a district's or university's legal review |
| **EMEA** | Lands inside obligations that already exist — the **EAA** evidence route (no harmonised standard cited) and **AI Act** Annex III duties from **2027-12-02** both reward documented provenance, and a resolved manifest is that class of evidence |
| **APAC** | **Sovereignty is the buying criterion**, and this report is a sovereignty document: it names every third-party grant entering a national deployment. Attaches directly to Vietnam's portal transition plan and Korea's high-impact filings |
| **LATAM** | The permissive stack **is** the budget strategy, so a copyleft dependency threatens the **cost case**, not just the legal one. ⚠️ **Kolibri — the platform this KB's equity pattern is built on — came back `REVIEW-WEAK` with two LGPL rows**, in the region where that matters most |

### Sizing

**2–4 days** for a shelf of 10–15 candidates, most of it reading rather than coding, since the
instrument already exists and runs offline except for the two registry endpoints. 🟢 **Best sold as a
bundled discovery artefact rather than a standalone engagement** — it is a trust signal the client
can verify in one command, and on this KB's own shelf it surfaced a real finding in **4 of 13**
projects.

## P-ONPREM-CLASSROOM — The zero-egress classroom (assignment, grading and mastery with no third-party service in the loop)

**Added in the twenty-second pass of 2026-10-06.** Every component's licence was read from its own
payload this pass or an earlier one; the three new ones came from the GitLab API channel documented
in `agents/top.md`.

**The constraint this answers, in two regions at once.** California's proposed **A.B. 1159** would
bar student data from training AI models unless the use directly benefits the school; a district's
counsel cannot verify that about a SaaS tutor and can verify it about a system with no outbound
calls. In EMEA the same architecture answers **Annex III** deployer duties and data-residency rules
without a transfer assessment. 🟢 **The deliverable is not software, it is a provable data-flow
statement** — and this stack makes it true by construction rather than by contract.

### Components

| Layer | Component | Licence (payload-verified) | Why this one |
|---|---|---|---|
| **Forge** | [`gitlab-org/gitlab-foss`](https://gitlab.com/gitlab-org/gitlab-foss) (GitLab CE), self-hosted | 🟢 **MIT Expat** — ⚠️ with directory carve-outs: `doc/` is **CC BY-SA 4.0**, `ee/` and `jh/` carry their **own** licences (payload, 2,001 B) | The institution already has Git hosting or can stand it up. ⚠️ **Deploy `gitlab-foss`, not the EE package** — the carve-out is the scope-split failure mode of trend 23, in the foundation layer |
| **Assignment workflow** | [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** | fetch/submit over the GitLab REST API, terminal **or** Jupyter widget dashboard; works against **any** instance incl. self-hosted; in production in a dozen classes at Paris-Saclay and UQAM. PyPI `travo` 2.1.1 |
| **Notebook grading** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** | automatic + manual grading with **hidden tests**; Travo drives it directly. v0.9.6 of 2026-09-30 |
| **Non-notebook grading** | [`cjaikaeo/elabsheet`](https://gitlab.com/cjaikaeo/elabsheet) | 🟢 **BSD-2-Clause**, holders named in payload | exercise/exam authoring with automatic answer checking, incl. a compiled-language component. Dockerised in `cjaikaeo/elab-docker` |
| **Mastery / next-task** | [`adaptive-learning-engine/adlete-packages`](https://gitlab.com/adaptive-learning-engine/adlete-packages) + its `moodle/adleteh5p` sibling | 🟢 **MIT** | competence estimation and next-exercise recommendation, with an **H5P** binding already written — the integration P3 has had to hand-build |
| **LMS of record** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) *(confirmed this pass at [olatorg/OpenOLAT](https://gitlab.com/olatorg/OpenOLAT))* | 🟢 **Apache-2.0**, payload read on **two forges** | the only complete LMS in this KB with no copyleft conversation; QTI, SCORM, curriculum, assessment |
| **Standards edge** | [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) *(optional)* · [`eduplex-api/cake-api-xapi-proxy`](https://gitlab.com/eduplex-api/cake-api-xapi-proxy) | ⚠️ **LGPL-3.0** · 🟢 **MIT** | 1EdTech **EduAPI** for SIS-side interop (link, do not fold) · **xAPI → LRS** pipe when the LMS cannot emit statements |
| **Inference** | Ollama or vLLM, on the institution's own hardware | 🟢 MIT · Apache-2.0 *(this KB's foundation shelf)* | the only layer that would otherwise call out. **No hosted model endpoint anywhere in this pattern** |
| **Offline tier** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) *(optional)* | 🟢 **MIT** — ⚠️ `REVIEW-WEAK`, two LGPL deps (pass 21) | where connectivity is the constraint rather than residency |

### Wiring

1. **Stand up `gitlab-foss`** inside the institution's network. One group per course; one project
   per assignment template; students' submissions are **forks inside that group**, so every artefact
   stays on the institution's disk.
2. **`pip install travo`** on the student image (JupyterHub, lab machine or BYOD). `travo fetch`
   clones the assignment; `travo submit` pushes the student's fork. The dashboard widget means the
   student never touches Git directly.
3. **Grading splits by artefact type.** Notebooks → nbgrader's autograde + hidden tests, manual
   tranche for the rest. Code and short-answer exercises → **elabsheet**, which authors the task and
   checks the answer. Both run as CI jobs **on the institution's own runners**.
4. **Mastery loop:** push each grading outcome into **ADLETE**; it returns the next task. If the LMS
   is Moodle, `adleteh5p` renders that task as an H5P activity in place; if it is OpenOLAT, drive it
   through QTI items.
5. **The model layer stays local.** Feedback drafting, hint generation and rubric-assisted marking
   call **Ollama/vLLM on-premises**. 🔴 **The oversight gate of `P11` applies unchanged: no
   model-generated mark is final.** This is also the only way the Oregon-style design duties and the
   A.B. 1159-style training-data rule are satisfiable at the same time.
6. **Standards edge last**, and only if procurement scored it: EduAPI for SIS interop, the xAPI proxy
   for statement export to an LRS the institution already runs.

### Deliverables

* A **data-flow statement** naming every egress point — ideally the empty set — reproducible by the
  client in one command (`ss -tunp` on the runner during a grading job).
* A course **pilot**: one real assignment, fetched, submitted, autograded and mastery-routed
  end-to-end.
* A **fork-ownership plan** for elabsheet and ADLETE (see the warnings) with a named maintainer and a
  budgeted hour-count.
* The **licence file set** for the deliverable: BSD-2, BSD-3, MIT, MIT Expat, Apache-2.0 — and, if
  EduAPI is in, the LGPL-3.0 linking note written out.

### ⚠️ Four warnings, which are the point of this pattern

1. 🔴 **Two components are small, and the stack's risk is concentrated there.** elabsheet is **14★**
   with a 2013 copyright line and two named holders; ADLETE is **1★**. Both were committed within the
   last month, both are permissive enough to fork outright, and **the engagement must price owning
   the fork** rather than assume upstream. This is a *deliberate* trade against a SaaS grader: the
   licence and the egress property are worth the maintenance.
2. ⚠️ **`gitlab-foss` is MIT Expat *outside* three directories.** `doc/` is CC BY-SA 4.0 and `ee/`
   carries its own terms. If the client's platform team installs the EE package "because it is the
   same product", the licence premise of this whole pattern changes. Check which package is running
   before writing the licence section of any proposal.
3. ⚠️ **Travo's trust model is GitLab tokens.** Each student authenticates to the forge; the
   workflow's security is the instance's access control, not the tool's. On a self-hosted instance
   that is an advantage — it is the institution's own IAM — but it must be configured, not assumed.
4. 🔵 **Nothing here is an agent, and that is on purpose.** The agentic layer in this pattern is a
   local model doing feedback and hint drafting behind a human gate. **A pattern whose selling point
   is "no data leaves" cannot have an autonomous component calling out**, and every hosted-tutor
   component in this KB does.

### Where it sells, and where it does not

| Region | Fit |
|---|---|
| **North America** | 🟢 **Strongest.** A.B. 1159-shaped data rules, Ohio's district-policy mandate (deadline **2026-07-01**, passed) and Maryland's AI coordinators give it a named buyer with a written obligation. Travo is already a Québec production tool |
| **EMEA** | 🟢 **Strong.** Answers Annex III deployer duties and residency without a transfer assessment; **11 of the 18 rows this pass added are EMEA-origin** (5 verified from a README, 6 inferred), so the local reference base exists |
| **APAC** | 🟢 **Strong where sovereignty is the criterion.** BSD-2 on the grading core means a ministry can fork and localise without publishing — the shortest grant in this KB |
| **LATAM** | ⚠️ **Fits the budget case, with an added step.** The cost argument is the point here, but 🔴 the regional supply this pass measured is **ungranted, not absent** (0 licensed education projects of 674), so a LATAM delivery imports this stack rather than building on local assets. Pair it with the **licence-grant clinic** in `intel/market.md` |

---

## Component currency update, twenty-third pass of 2026-10-07

⏱️ **Measurement window 2026-10-06 ~21:00 UTC → 2026-10-07 00:00 UTC; ages computed against the
reference date 2026-10-06.** Every GitHub repository cited anywhere in this KB was dated via
`git ls-remote` and `git fetch --depth 1 --filter=blob:none`.

🟢 **Read this first, because it is the reassuring half.** Of the **181** repositories wired into
the patterns in this file, **54.7% were touched in the last 30 days and only 18.8% are more than a
year old** — against **33.0%** for `repos/foundations.md`. **These patterns were already composing
from the live subset of the shelf, without ever reading a date.** What follows is a short list of
exceptions, not a rebuild.

### 🔴 P1 — the default engagement shape: both LTI picks are cold, and both have live replacements

| Currently named | Head commit | Age | 🟢 Replace with | Licence (payload) | Head commit |
|---|---|---|---|---|---|
| `1EdTech/lti-1-3-php-library` | 2020-06-03 | 🔴 2,316 d | [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B) | **2026-09-23** (13 d) |
| `dmitry-viskov/pylti1.3` | 2022-11-21 | 🔴 1,415 d | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** (1,527 B) | **2026-07-01** (97 d) |

🟢 **The PHP swap is free.** The two repositories' `LICENSE` payloads are **byte-identical**
(`sha256 78b49eea…`, 11,343 B) and the composer packages are the same library under two names
(`packbackbooks/lti-1p3-tool` vs `imsglobal/lti-1p3-tool`). **This is an upstream swap, not a
migration** — the consortium's republished copy went cold, the author's original did not.

🟢 **The Python swap is a real choice and it closes this KB's most-repeated gap.**
`ltiauthenticator` implements **LTI 1.3 and LTI 1.1** and its README names **Open edX, Canvas and
Moodle** as tested platforms — the three this KB documents. If the tool must be Django rather than
JupyterHub-hosted, use [`Harvard-University-iCommons/django-lti`](https://github.com/Harvard-University-iCommons/django-lti)
(**MIT**, 2025-08-27, ⚠️ copyright vests in the **University of Michigan** despite the Harvard
organisation — note it in the provenance pack).

⚠️ **Do not reach for `ucfopen/cookiecutter-python-lti` without reading its requirements file.** The
template is MIT and 147 days old; its **Flask** path pins
`git+https://github.com/ucfopen/pylti1.3.git@master` — a **fork, 1,363 days cold, at a moving
branch**. Its **Django** path pins `django-lti==0.7.1` and is fine.

### 🔴 P18 — offline voice tutoring: Piper is 406 days cold and the replacement is already in this KB

| Currently named | Head commit | Age | 🟢 Replace with | Licence | Head commit |
|---|---|---|---|---|---|
| `rhasspy/piper` (TTS) | 2025-08-26 | 🔴 406 d | [`k2-fsa/sherpa-onnx`](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (11,357 B) | **2026-10-06** (0 d) |

🟢 **`sherpa-onnx` is already the ASR component of this pattern**, and it does **TTS as well**, so
the swap *removes* a dependency rather than exchanging one. Piper stays usable — MIT, and a frozen
TTS model is a far smaller risk than a frozen protocol library — but new builds should not add it.

### ⚠️ P2 / P24 — the certified QTI player is 472 days old, and that is a disclosure, not a swap

[`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (MIT, 2025-06-21) is
the **only 1EdTech-Certified permissive asset in this KB**. 🟢 **Keep it.** Certification does not
lapse when maintenance pauses, and the certificate is the strongest procurement artefact on this
shelf. 🔴 **But the date goes in the deck**, because "certified" and "maintained" are now different
facts about the same repository. The live alternative,
[`Citolab/qti-components`](https://github.com/Citolab/qti-components) (0 d), is 🔴 **GPL-3.0** (*corrected pass 28, `P452`; was filed LGPL-3.0*) — a
different licence conversation, not a drop-in.

### ⚠️ P12 and P16 — two further cold components, flagged without a replacement

| Pattern | Component | Head commit | Age | Status |
|---|---|---|---|---|
| **P12** (pedagogy-aware evaluation) | `ai-edu-lab/E-Eval` | 2024-02-19 | 🔴 960 d | 🔴 **no live permissive replacement found.** `AI-for-Education/pedagogy-benchmark` is 356 d and also ageing |
| **P16** (all-MIT national/state stack) | `project-sunbird/sunbird-lms-mw` | 2020-05-05 | 🔴 2,345 d | ⚠️ the `project-sunbird/*` namespace is **75% cold**; current work is in `sunbird-ed/*`. **Confirm which namespace the client's distribution tracks before week one** |
| **P24** | `theopenem/OneRoster.NET` | 2023-10-13 | 🔴 1,089 d | 🔴 **no live permissive OneRoster implementation exists** — both known ones are 1,089 d. Price the maintenance |

### 🟢 Added to the P22 gate — a fourth point, and it runs over the closure

P22 (the licence-reliability gate) has three points: payload, manifest, detector. **Add a fourth:**

> **P22.4 — currency.** For every component entering a deliverable, record the head-commit date
> (`git ls-remote` + `git fetch --depth 1 --filter=blob:none`; no API needed, and it works where
> `api.github.com/repos/*` returns 403). **Run it over the dependency closure, not the dependency
> list** — a 147-day-old MIT template installing a 1,363-day-old fork at a moving branch is the
> shape this catches, and neither the template's licence nor its own date reveals it.

**Output:** three verdicts. 🟢 **current** (<180 d) — no action. ⚠️ **ageing** (180 d–2 y) —
disclose in the deck with the date. 🔴 **cold** (>2 y) — either name a live replacement or price
the maintenance explicitly as a line item. **Never prune on date alone**: a finished conformant
implementation and an abandoned one look identical to this probe, and only reading the project tells
you which it is.

---

## P-GRANT-CLINIC — the licence-grant clinic (small, fast, and it sells in every region)

**Added in the twenty-third pass of 2026-10-07**, executing pass 22's pre-registered action C and
re-scoping it from a LATAM offer to a global one.

### The finding it monetises

Across the last two passes, **four real, active education projects were measured as carrying no
grant of any kind** — not a restrictive licence, *no licence file at all*. They cannot be adopted,
contributed to, forked, resold or deployed by anyone, **including their own institutions'
partners**, until one file is added.

| Project | Origin | Last activity | What it is |
|---|---|---|---|
| [`angeelrdz-group/nova-aula`](https://gitlab.com/angeelrdz-group/nova-aula) | LATAM (Spanish) | 🟢 2026-10-05 | full-stack education platform: courses, quizzes, analytics |
| [`evertonwilliam/plataforma-de-educacao`](https://gitlab.com/evertonwilliam/plataforma-de-educacao) | LATAM (Portuguese) | 🟢 2026-09-08 | AI-guided software-engineering training track |
| [`ccsl-ufpa/educacaovigiada-org-br`](https://gitlab.com/ccsl-ufpa/educacaovigiada-org-br) | **Brazil — Federal University of Pará** | ⚠️ 2025-12-09 | *Educação Vigiada*, surveillance in education; five years old |
| [`cderda/cargogetgraded`](https://gitlab.com/cderda/cargogetgraded) | 🔴 **North America** (UChicago) | 2026-07-28 | **Carriage** — step-level algebra autograder, Python/SymPy, **piloting Fall 2026** |

🔴 **The fourth row is why this is not a LATAM pattern.** Ungranted-but-real is a **global condition
with a LATAM concentration** — and in LATAM it carries a measured denominator (674 projects across
English, Spanish and Portuguese; **0 with a permissive payload**) that makes the pitch sharper
there than anywhere else.

### Components

Nothing to build. This pattern is **entirely artefact and process**, which is why it fits in a week:

| Artefact | Source |
|---|---|
| licence selection note (MIT / Apache-2.0 / BSD-2 / BSD-3, with the consequence of each stated in one paragraph) | this KB's `repos/foundations.md` licence-boundary section |
| `LICENSE` payload, correct holder line, correct year | the project's own commit history and institutional owner |
| `LICENSES/` directory + **REUSE**-style per-file headers where the project has mixed provenance | the pattern pass 22 measured on `gitlab.com` |
| manifest alignment — `composer.json` / `package.json` / `pyproject.toml` `license` field matching the payload | prevents pass 22's class-3 defect (*the project contradicts itself*) |
| dependency-licence closure report | **P22** gate, points 1–3 |
| currency report | **P22.4**, added above |

### Wiring — the one-week shape

1. **Day 1 — establish there is genuinely no grant.** 🔴 **Enumerate the repository root tree via
   the forge API; do not guess filenames.** This is how Carriage was established as ungranted (21
   root entries, no licence file). Guessing `LICENSE`/`LICENSE.md`/`COPYING` across two branches
   misses `LICENSES/` directories and mis-reports REUSE projects as ungranted.
2. **Day 1 — identify the actual holder.** ⚠️ Rarely the account name. Measured counter-examples:
   `django-lti` is published by **Harvard** and vests copyright in the **University of Michigan**;
   `Verbix-Flutter` is published by `Wahid7852` and names **Swati Sharma**;
   `ucfopen/pylti1.3` names the upstream author. **For a university project the holder is usually
   the institution, and the grant needs the institution's assent, not the committer's.**
3. **Days 2–3 — licence selection workshop.** For a ministry or university the decision is nearly
   always between **MIT** (shortest, most permissive, zero obligations) and **Apache-2.0** (adds an
   explicit patent grant — the one a public institution's counsel usually wants). **BSD-2** is the
   answer when the institution wants the shortest possible text, as `cjaikaeo/elabsheet` chose.
4. **Days 3–4 — add the files and align the manifests.** Payload, holder, year, `LICENSES/`,
   manifest `license` field. Run the P22 gate against the result so the project passes its own
   check.
5. **Day 5 — the closure report.** What the project *installs* may be less permissive than what it
   *grants* (pass 21: 15 of 352 dependencies not permissive). **The grant is not finished until the
   closure is reported**, or the institution has been told, in writing, which dependency constrains
   redistribution.

### Deliverables

- A merged licence grant, or — where the holder is an institution and the repository is quiet — a
  **written grant recommendation addressed to the institution**, which is the realistic output for
  `ccsl-ufpa/educacaovigiada-org-br` (ten months idle).
- Dependency-licence closure report and currency report.
- A one-page reusable licence-selection note the institution can apply to its remaining repositories
  — **this is the part that turns one clinic into a programme.**

### ⚠️ Three warnings that are the point of this pattern

1. 🔴 **Target by activity, not by prestige.** The federal university's project has the best story
   and the worst odds: **ten months idle** means there is no maintainer to accept a merge request,
   so it must be routed through the institution's free-software centre as a policy conversation.
   `nova-aula`, committed the day before measurement, is a merge request and a chat. **Open with the
   live one; the institutional one is the follow-on.**
2. 🔴 **A `LICENSE` file is not a grant.** `Wahid7852/Verbix-Flutter` carries one — 208 bytes
   reading *"No permissions are granted for reuse, distribution, or modification."* Any clinic that
   screens on *presence* will skip the projects that most need it and "fix" nothing. **Screen on
   payload.**
3. ⚠️ **This is not free legal advice, and it should not be priced as a giveaway.** The deliverable
   is a licence decision made by the institution's own counsel with the engineering facts in front
   of them. 🟢 **The commercial logic is that the clinic creates the asset the later engagement is
   built on** — a client cannot buy a platform engagement on code nobody is allowed to modify.

### Regional fit

| Region | Fit |
|---|---|
| **LATAM** | 🟢 **Strongest, and the only region with a measured denominator**: 674 projects, three languages, **0 permissive payloads**. Three named targets, one of them a federal university. Pair with the offline-first and cost arguments of P5 and P21 |
| **North America** | 🟢 **Real and newly evidenced** — Carriage is piloting in US classrooms in Fall 2026 with no grant. Sells alongside the procurement-rubric component register of trend 26 and P24 |
| **EMEA** | 🟢 **Different buyer, same work.** Public-sector publishers here mostly *do* grant, often via **REUSE** and `LICENSES/` directories; the clinic's EMEA form is **correctness and closure** (manifest alignment, REUSE conformance, dependency closure) rather than adding a first grant |
| **APAC** | ⚠️ **Thinnest fit of the four, stated rather than padded.** The region's permissive assets measured in this KB — OpenMAIC, `elabsheet`, the Sunbird estate — already carry grants. The APAC version of this engagement is the **currency** check of P22.4, not the grant |

---

## Added in the twenty-fourth pass of 2026-10-07 — component currency, applied to the patterns rather than reported about them

⏱️ **Ages against the reference date `2026-10-07`.** Channels: the package registries
(`compose/code/registry-recency-channel/`) and `git ls-remote`.

Pass 23 pre-registered action **C**: *"re-pick the cold components in P1 and P18 and re-measure,
rather than only flagging them."* Done, and the pre-registration was wrong about both patterns.

### 🔴 P1 did not have a cold component — it had the wrong protocol

P1 is described here as *"the default engagement shape"*, for when *"the client already runs an LMS,
which is almost always"*. Its step 2 named
[`IMSGlobal/LTI-Tool-Provider-Library-PHP`](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP):

| | measured this pass |
|---|---|
| head commit | 🔴 **2016-11-28 — 3,600 days (9.9 years)**, the oldest component in any pattern here |
| licence payload | 🟢 Apache-2.0, `master/LICENSE`, 11,357 B — the grant was never the problem |
| 🔴 protocol | `master/README.md`: *"support for **LTI 1.1** and the unofficial extensions to **LTI 1.0**"* — **no LTI 1.3** |

🔴 **LTI 1.1's security model is retired. LTI 1.3 / Advantage is what Canvas, Moodle and Open edX
certify against and what every procurement rubric in `intel/market.md` scores.** An engagement
following P1 literally would have built its LMS integration on a withdrawn protocol generation and
then failed the interoperability line of the rubric that justified the project.

⚠️ **Pass 23 dated this repository correctly** — it is the last row of that pass's interoperability
table, at 3,599 d — **and no pass had opened it.** Its licence column there reads `—`, and nothing
checked its protocol version against the step that cited it. **Dating a component and qualifying it
are different acts.**

🟢 **P1 step 2 is rewritten above**, with the pick made from the client's estate: `django-lti`
(Python/Django, MIT, 2 d), `ltiauthenticator` (JupyterHub, BSD-3, 98 d), `packbackbooks` (PHP, 14 d)
or `ltijs` (Node, 1 d). Because P1's steps 4–6 are already Python, **the usual answer is `django-lti`
and the second runtime P1 assumed disappears.**

### 🔵 P18 needed nothing, and pass 23's flag was the error

Pass 23 listed `rhasspy/piper` as *"wired into P18"*. **It is not.** P18 already selected
`sherpa-onnx` and already carries the paragraph *"Why sherpa-onnx and not Piper"*, recording Piper's
archival and its GPL-3.0 successor. 🟢 The commit channel confirms it independently: `piper`'s head
commit is **2025-08-26 (407 d)** and nothing has landed since. **P18 was correct before this pass
and is unchanged.**

### 🟢 Where the cold components actually were

| Pattern | Component | Age | Re-picked to | Age | What the pattern gains |
|---|---|---|---|---|---|
| **P1** | `IMSGlobal/LTI-Tool-Provider-Library-PHP` (🔴 LTI 1.1 only) | 🔴 **3,600 d** | `academic-innovation/django-lti` | 🟢 **2 d** | the right protocol, and **one fewer runtime** |
| **P25**, **P34** | `1EdTech/lti-1-3-php-library` | 🔴 2,317 d | `packbackbooks/lti-1-3-php-library` | 🟢 **14 d** | the **same library**, live copy |
| **P25**, **P27**, **P28**, **P30** | `dmitry-viskov/pylti1.3` | 🔴 1,416 d | `academic-innovation/django-lti` | 🟢 **2 d** | no *"fork and maintain"* caveat |
| **P21** | `vosk-api` **+ an unresolved Piper fork decision** | 🔴 407 d | `k2-fsa/sherpa-onnx` | 🟢 **1 d** | **one component instead of two**, one permissive licence, decision closed |
| **P36** | `rhasspy/piper` (audio description) | 🔴 407 d | `k2-fsa/sherpa-onnx` | 🟢 **1 d** | — |

🟢 **Two of these are simplifications, not swaps.** P21 loses a component *and* a standing
architectural argument: `sherpa-onnx` does ASR **and** TTS — plus VAD, keyword spotting and
diarization — *"running the following functions locally"* on **Raspberry Pi and Android**, under one
Apache-2.0 grant. P1 loses the entire second runtime its two-process architecture existed to host.

### 🔴 The licence boundary that is now explicit in P30

[`openedx/xblock-lti-consumer`](https://github.com/openedx/xblock-lti-consumer) is the
**best-maintained Python LTI 1.3 implementation in any language** — committed and released **6 days**
ago as `lti-consumer-xblock` v11.4.2 — and it is **AGPL-3.0** (payload 34,520 B). It is the right
component **inside** an Open edX deployment and disqualified from a reusable-IP deliverable, which is
exactly P30's thesis. It is named in P30 as a boundary so that no later pass re-discovers it as a
pick.

## P22.5 — the currency-and-provenance point, added to the licence-reliability gate

**P22** runs three points before a component enters a deliverable, and pass 23 added **P22.4**
(currency over the dependency closure). This pass adds the fifth, because P22.4 would not have caught
either defect found above:

> **P22.5 — Resolve provenance before you trust a date, and read the protocol before you trust the
> provenance.**
>
> 1. **Is the payload's copyright holder the publishing account?** If not, treat it as a **fork
>    hypothesis** (trend 56). Resolve the upstream from the package registry's declared homepage —
>    PyPI `project_urls`, npm `repository`, the composer name — which works where `api.github.com`
>    is 403.
> 2. **Do the remote's tags reach the registry's current release?** `git ls-remote` the tags. A copy
>    topping out six minor versions below the published release is a fork.
> 3. **Is the organisation name current?** An org that has been renamed (`IMSGlobal` → 1EdTech,
>    2022) dates its repositories by construction.
> 4. **Does the component implement the version the rubric scores?** Open the README. A library can
>    be permissive, popular and the wrong protocol generation — which is **three green checks and a
>    failed bid**.
> 5. **Both recency channels, not one.** Head commit **and** latest release. Cold commits with fresh
>    releases means development happens off the default branch — look harder. **Cold on both is
>    abandonment** (`pylti1.3`: 1,416 d and 1,417 d).

⚠️ **And one bound on every date this gate produces:** the registry channel reads the **latest**
release, not the **pinned** one, so an age is a **lower bound on staleness**. A manifest pinning an
old version installs something older than the gate reports, never newer.

## P-UPLIFT — the dependency-uplift engagement (small, honest, and it precedes every adoption)

**Added in the twenty-fourth pass of 2026-10-07.** Not a new capability — a line item this KB has
been recommending adoptions without, in every region.

**Use when:** a client is adopting a permissive education platform or ITS from this KB's shelf
(OATutor, Kolibri, Oppia, Coursemology, Mentingo) and the proposal treats "it is actively
maintained" as sufficient diligence.

**The premise, measured.** A repository's head-commit date and its dependency set's release dates
are **different facts** (trend 57). Across 293 depth-1 dependencies: **30.1% cold over a year,
13.0% pre-2024, median 65 days** — and the per-repository spread is **30× wide**:

| Adoption target | Head commit | Median dependency age | Cold > 1 yr | Sprint-one reality |
|---|---|---|---|---|
| `CAHLR/OATutor` | 🟢 7 d | 🔴 **604 d** | 21/35 | Material-UI **v4** (superseded 2021); `random-seed` 3,967 d |
| `learningequality/kolibri` | 🟢 1 d | ⚠️ 200 d | 14/32 | Python-2-era shims: `zeroconf-py2compat` 1,156 d |
| `oppia/oppia` | 🟢 1 d | 🟢 60 d | 40/152 | bimodal; App Engine tail (`crcmod` 5,923 d) **and** a proprietary Azure Speech SDK |
| `towardsai/ai-tutor-app` | — | 🟢 **9 d** | **0/20** | 🟢 nothing to uplift |

**Wiring.**
1. Run `compose/code/dependency-licence-closure/` over the target's manifests — the licence census.
2. Run `compose/code/registry-recency-channel/` over the result — the age census.
3. Run **P22** including **P22.5** on every component the target itself wires in.
4. Partition the result: **permissive-and-fresh** (adopt), **permissive-and-cold** (uplift, estimate
   it), **copyleft** (architecture decision), **proprietary or ungranted** (replace — and name the
   substitute; for Azure Speech it is `k2-fsa/sherpa-onnx`, Apache-2.0).
5. Deliver the four-way partition as the adoption decision record.

**Deliverables.** The two censuses, the uplift estimate by dependency, the replacement list with
named permissive substitutes, and a one-page adoption recommendation that quotes **the median and
discloses the maximum**.

**Effort:** 1–2 weeks, before the adoption decision rather than after it.

⚠️ **Two warnings that are the point of this pattern.**
🔴 **A green head commit is not a priced adoption.** OATutor is the right technical pick and its
first sprint is a dependency uplift. Saying so wins trust; discovering it in sprint three loses the
account.
🟢 **A cold dependency is not a defect by itself.** `defusedxml` at 2,039 days is a finished security
library. **The deliverable is the partition, not the age**, and the partition requires reading.

---

## P-UPLIFT addendum, twenty-fifth pass — price the uplift from the **pin**, and the number is four times bigger

**P-UPLIFT** was written against the *latest-release* ages of a component's dependencies, which is
the number `registry-recency-channel` produces. This pass resolved the **version specifiers**
(`compose/code/p437-pinned-version/`, 47 controls) and the number a client is actually quoted
changes:

| Across 327 dependency rows of the twelve target repositories | Latest release | **Pinned** |
|---|---|---|
| median age | 57 d | 🔴 **220 d** |
| cold > 1 yr | 27.2% | 🔴 **42.5%** |

🔵 **Why it is this large, and the condition for transferring it: 52% of these rows are pinned
exactly** (`==1.2.3`) and another 30% are capped (`^`, `~`, `<`). Only the remaining 18% resolve
to the latest release. **Check the specifier mix before quoting the ratio**; a `>=`-heavy manifest
shows no gap at all, and `pinned.py` prints the mix.

🔴 **Two rows to re-scope in any live proposal.** `CAHLR/OATutor`: median **604 d → 1,839 d**,
29 of 35 dependencies cold by more than a year. `ronantakizawa/a11ymcp`, which the previous pass
filed as the **cleanest** row in the corpus (0 of 5 cold): it pins `puppeteer` and `puppeteer-core`
at **13.5.0, 2022-03-05 — 1,675 days and twelve major versions behind**. Its median moves from
**14 d to 686 d**. ⚠️ **A clean latest-release row is not a clean build.**

**Added to the pattern's step 1:** run `pinned.py` over the candidate's manifests and deliver the
specifier-class histogram with the age table. The histogram is what tells the client whether the
gap is a maintenance choice (exact pins, a deliberate freeze) or neglect (caps nobody has raised).

---

## P-REGISTRY-ID — resolve a component's identity through its registry before you put it in a bid

**Use when:** you are about to name an open source component in a proposal, an SBOM, an
architecture page or a vendor questionnaire — which is every engagement.
**Outcome:** the name you write is the one its publisher uses, it is not a fork of something
better maintained, and its governance is current.
**Effort:** minutes per component. Every step is one HTTP or `git` call.

**Why it exists.** Measured over the 503 repositories this KB cites, **21 name a repository other
than the one cited**, and of the **494 distinct repositories** those 503 references name, **9
were cited under two different spellings**.
None of that is visible in a browser: GitHub redirects renames and resolves owner names
case-insensitively, so every wrong citation still works. It stops working when a compiler, an SBOM
tool or a procurement reviewer keys on the string.

**Wiring — four calls, in this order, and the order matters:**

1. **Read the manifest for the package NAME.** `pyproject.toml` / `setup.cfg` / `setup.py` /
   `package.json` / `composer.json` / `mix.exs` / `pom.xml`.
   🔴 **Never assume the package is named after the repository.**
   `repo.packagist.org/p2/packbackbooks/lti-1-3-php-library.json` → **404**; the package is
   `packbackbooks/lti-1p3-tool`, **68 releases**. A census keyed on slugs records a maintained
   library as unpublished.
   ⚠️ **`"private": true` ends the resolution here** — a workspace root is never published and its
   `name` is a local label. Skipping this check produced a fork hypothesis against a *deleted*
   repository for an *unrelated* project.
2. **Ask the registry which repository it declares.** `project_urls` / `repository.url` /
   `source.url`. Reachable from this environment: **PyPI · npm · Packagist · Maven Central ·
   Hex · RubyGems · Go proxy**. Not reachable: `api.github.com`, the rendered `github.com` page,
   `crates.io`.
3. **If the declared slug differs, compare heads.**
   `git ls-remote https://github.com/<a> HEAD` against `<b>`.
   🟢 **Same SHA ⇒ one repository under two names** — a rename or a transfer. Update the name;
   there is no lineage question. 🔴 **Different SHAs ⇒ two repositories**, and only now is
   "which is upstream" worth asking.
4. **Date both channels.** Head commit via `git fetch --depth 1 --filter=blob:none`; latest
   release from the registry. 🟢 **Agreement on the same day is the signature of a maintained
   library** — three of the five rows on this KB's LTI shelf do that. 🔴 **Both cold and equal is
   the signature of abandonment**: `pylti1.3` is 1,416 d on one and 1,417 d on the other.

**What it catches, with the counts from 2026-10-07:**

| | n | Example |
|---|---|---|
| component cited at a former name | 6 | `iterative/dvc` → **`treeverse/dvc`**, a transfer between companies |
| component is a derivative of a better-maintained upstream | 9 | `ucfopen/pylti1.3` → `dmitry-viskov/pylti1.3` |
| the registry name collides with an unrelated project | 5 | `frappe/lms` → `molobrakos/lms`, *a Squeezebox interface* |
| component vendors another project wholesale | 2 | `CNIT-Organization/ltitoolkit` vendors `PyLTI1p3`; `Polygl0t/Polygl0t` vendors `llm-foundry` |
| one repository cited under two spellings | 9 | `LearningEquality/kolibri` and `learningequality/kolibri` |

⚠️ **Steps 2 and 3 are a reading list, not a verdict.** The registry can be stale in the other
direction: PyPI's `openbadges` still declares `IMSGlobal/openbadges-validator-core`, the name
1EdTech left behind in 2022, while this KB has the current one. **The head SHA settles which of
the two is out of date; nothing else does.**

🔵 **Sell it as the first hour of a due-diligence engagement, not as a separate line.** It costs
minutes, it is fully evidenced, and the output — *"these four components have moved owner, this
one is a fork, this one vendors a library its licence does not mention"* — is exactly the content
of the governance section a client's procurement team has to fill in and usually cannot.

## `P-GRANT-ENUMERATION` — resolve a component's licence on three channels before you discard it

**The problem it solves.** A candidate component is rejected because a scan reported no licence. On
this KB's own shelf that verdict was wrong for **15 of 87** repositories, and the ones it was wrong
about include an Open edX core API, a dual-licensed PDF/UA validator and a national OER library.

**Why a filename probe is not enough.** Measured 2026-10-07 over the 87 repositories this shelf had
published as unlicensed:

| Channel | Grants found |
|---|---|
| 14 licence filenames, repository root | **0** |
| 41 licence filenames, repository root | 1 |
| 🟢 complete tree enumeration | **9** |
| 🟢 package registry, with an ownership check | **6 more** |

### The recipe

| Step | Tool | Command | What it decides |
|---|---|---|---|
| 1 | `git` | `git clone --filter=blob:none --no-checkout --depth 1 <url>` then `git ls-tree -r --name-only HEAD` | every path at HEAD — no API, no pagination, **13 s for 87 repos** |
| 2 | `compose/code/p441-tree-licence-enumeration/enumerate_licence.py` | pattern-match `licen[cs]e\|copying\|copyright` over all paths, case-insensitively | candidates at **any depth and any capitalisation** |
| 3 | same | fetch each candidate blob, classify with `p436/sweep_payload.py:family_of` | **a path whose payload is not a licence text is a name, not a grant** |
| 4 | same | reject depth > 2 and the container segments (`assets/`, `libraries/`, `plugins/`, `lib/`, `fonts/`…) | the **project's own** grant versus a **vendored dependency's** |
| 5 | `compose/code/p440-unlicensed-registry-grant/grant.py` | read the publisher's declared `license` on PyPI · npm · Packagist · Maven · Hex | a grant made **only in the registry** |
| 6 | same | compare the registry's declared repository URL against the slug | 🔴 **the ownership gate — without it, 7 of 15 grants belong to someone else** |
| 7 | `compose/code/dependency-licence-closure/dep_licence.py` | classify the string | PERMISSIVE · WEAK- · STRONG-COPYLEFT · NONCOMMERCIAL · **NO-GRANT** · UNKNOWN |

### The four verdicts to wire into a gate, and what each means for a deliverable

| Verdict | Meaning | Action |
|---|---|---|
| `OWN-GRANT-*` | a licence text in the project's own tree | 🟢 the strongest evidence; quote the path |
| `REGISTRY-GRANT` | declared by the publisher, absent from the tree | ⚠️ usable; **`P314`** — one written confirmation citing the publisher's own metadata |
| `BUNDLED-GRANT-ONLY` | every grant found belongs to a vendored dependency | 🔴 the project's own grant is still absent — do not quote the dependency's |
| `ABSENCE-ENUMERATED` | no licence text in the **complete** tree and no registry grant | 🔴 now a sustainable finding, which a filename probe could never produce |

### Three failure modes this pattern exists to prevent, each measured

- 🔴 **A name is not a grant.** The first run of step 2 published an **icon component** called
  `copyright/baseline.vue`, an **XSLT transform**, three **vendored** licences and the European
  Commission's `licence-EUPL 1.2-brightgreen.svg` — a **README badge image**. Step 3 removes all six.
- 🔴 **A package is not necessarily yours.** `pnp-v/bo-google-classroom-mcp-server` declares
  `"name": "class"`; npm's `class` is a 2013 Ruby-style class helper at `deadlyicon/class.js`. And
  `Opetushallitus/aoe` resolves to a 2016 hobby package declaring **GPL-3.0**, while the agency's own
  grant is **EUPL-1.2**. Step 6 is the only thing between those and a wrong licence in a client's SBOM.
- 🔴 **A classifier's order is a verdict.** MPL-2.0 §1.12 names the GPL, LGPL and AGPL; EUPL-1.2's
  Appendix names five families. Probe **EUPL, then MPL and EPL, then the GNU family**, or five MPL-2.0
  components get filed as GPL blockers — which is what happened here. ⚠️ And where a payload names more
  than one family and the granting one is not identifiable from the head — `nvaccess/nvda`'s *"GPL v2 or
  later, with two special exceptions"* — **count the marks and hand over a reading list; do not guess.**

🟢 **Effort: 2–3 days to wire steps 1–7 into an existing SBOM step, on any repository corpus.** The
instruments are in `compose/code/` with **70 offline controls** between `p440` and `p441`, and the whole
sweep over 87 repositories runs in under a minute.

⚠️ **Declared limits.** RTF licence payloads are not read (`docs/LICENSE.rtf`, both `OS4ED/openSIS-*`
rows). Maven Central's POM layer answers **429 intermittently**, so a single-shot probe cannot tell a
POM with no licence from a POM that was rate-limited — retry before recording silence. And for **57 of
87** repositories the registry channel has nothing to say at all, because a project that publishes no
package has no metadata to read.

## `P-GRANT-ENUMERATION` step 8 — twenty-seventh pass: classify with BOTH classifiers, because neither is a superset

🔵 **Added 2026-10-07.** Steps 1–7 above answer *"is there a grant, and whose is it?"* — and they
answer it well: 15 of 87 rejected components recovered. **This step answers "what does it say?",
and the measurement behind it is that this repository cannot answer that with one tool.**

⚠️ **Step 3 classifies each payload with `p436/sweep_payload.py:family_of`. That function has no
NonCommercial axis.** Step 7's `dep_licence.py` does carry a `NONCOMMERCIAL` verdict, but it
classifies a **dependency string**, not a licence **payload** — so nothing in steps 1–7 can see a
non-commercial restriction in a repository's own `LICENSE` file.

```sh
# 8. CLASSIFY WITH BOTH, on the same bytes, and reconcile  (P445 / trend 64)
compose/code/p445-classifier-divergence/divergence.py
#    lib/license_family.sh  -> osi_family_of + commercial_use_ok   (NC, Elastic, PolyForm)
#    p436/sweep_payload.py  -> family_of                           (EUPL, MPL-not-GPL)
#    over 412 LICENSED roots: AGREE 369 · VOCABULARY 25 · PYTHON-UNKNOWN 13 · NC-ERASED 5
```

### 🔴 Why one classifier is not enough, measured over 412 payloads

| Case | `family_of` (Python, step 3) | `lib/license_family.sh` | Who is right |
|---|---|---|---|
| **NonCommercial** (5 rows) | 🔴 erased to `CC-BY` | 🟢 `CC-BY-NC-*`, commercial `NO` | **shell** |
| **Elastic / PolyForm** (3) | 🔴 `UNKNOWN` | 🟢 named | **shell** |
| **EUPL** (9) | 🟢 `EUPL` | 🔴 `UNCLASSIFIED` | **Python** |
| **MPL read as GPL** (4) | 🟢 `MPL-2.0` | 🔴 `GPL-3.0` | **Python** |
| **GPLv2 read as LGPL** (4) | 🔴 `LGPL` | 🟢 `GPL-2.0` | **shell** |

🔵 **Each was hardened against the defect the other still has.** Step 7's note above — *"probe EUPL,
then MPL and EPL, then the GNU family"* — is the Python classifier's fix, and the shell classifier
never received it. The shell classifier gained the NC axis in pass 101 (`P312`, 21/21) and the
source-available families in pass 82, and the Python one never received those.
⚠️ **43 of 412 (10.4%) are wrong in one of the two, and which one depends on the family.**

### 🔴 The eight rows this step exists to catch before they reach a bid

A shelf filtered for *redistributable* components on step 3's output **includes all five of these**,
because all five report as plain `CC-BY` — a licence that permits commercial use:

| Repo | Actually | What it is |
|---|---|---|
| [`facebookresearch/seamless_communication`](https://github.com/facebookresearch/seamless_communication) | **CC-BY-NC-4.0** | multilingual speech — the top hit for "open source multilingual speech" |
| [`openstax/osbooks-biology-bundle`](https://github.com/openstax/osbooks-biology-bundle) | **CC-BY-NC-SA-4.0** | open textbook content |
| [`sign/translate`](https://github.com/sign/translate) | **CC-BY-NC-SA-4.0** | sign-language translation |
| [`Yunfeng-Wan/CSTutorBench`](https://github.com/Yunfeng-Wan/CSTutorBench) | **CC-BY-NC-4.0** | CS-tutoring benchmark |
| [`Jona-Zwetsloot/Somtoday-Mod`](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | **CC-BY-NC-SA-4.0** | NL SIS client |

Plus three that bar commercial use with **no `NC` token at all**:
[`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) and
[`sodadata/soda-core`](https://github.com/sodadata/soda-core) (**Elastic**),
[`digillab-lmu/smart-rag`](https://github.com/digillab-lmu/smart-rag) (**PolyForm**) —
source-available, not OSI. **11 of 412 root payloads restrict commercial use; step 3 flags none.**

### 🟢 Two rules for the write-up

1. **Report the commercial axis separately from the family.** `P250` built them as two independent
   axes, and `commercial_use_ok` is the one answering the question a client is actually asking.
   Searching for `NC` inside a family *name* misses the Elastic and PolyForm rows entirely — and
   matches `UNCLASSIFIED`, which contains those letters.
2. **Name the classifier beside the verdict.** *"MIT, per `lib/license_family.sh` on
   `LICENSE@HEAD`"* is auditable; *"MIT"* is not, and on this shelf it is wrong once in ten.

### What step 8 adds to the scoping

| | |
|---|---|
| **Cost** | under an hour on top of steps 1–7 — both classifiers already exist and it needs **no network** |
| **Changes** | the **redistributable** count, which is the number a bid is built on: 11 of 412 move from "usable" to "not billable" |
| **Controls** | `compose/code/p445-classifier-divergence/` — **22 offline**, on top of the 70 between `p440` and `p441` |
| **Sells hardest in** | **EMEA**, where the 9 EUPL rows the shell cannot name are the public-sector tier and the AI Act already imposes documentation duty; and in any engagement that redistributes modified source |
## `P-FAMILY-QUALIFIER` — read the licence QUALIFIER before you bid, because the family does not carry the answer

**Added in the twenty-eighth pass of 2026-10-07.** This is the pattern that would have caught every
licence defect this KB found this pass, and it is the cheapest one in this file: it is three greps
and a byte count, and it runs before anybody opens an architecture document.

**The problem it solves, stated as the three live failures it would have caught:**

| Failure | What the KB said | What the payload says | Cost if un-caught |
|---|---|---|---|
| `oat-sa/lib-lti1p3-core` | LGPL-2.1 | **GPL-2.0** | the certified LTI 1.3 library has **no linking exception** — a linked deliverable inherits copyleft |
| `sign/translate` | CC-BY | **paid dual-tier**, free only for non-profits and schools | a demo built on it is a **licence violation** by a for-profit |
| `openstax/osbooks-biology-bundle` | CC BY | **CC BY-NC-SA 4.0** | **NonCommercial** — the courseware cannot be resold |

**The recipe, concretely.**

1. **Fetch the payload, not the badge, not the sidebar.**
   ```sh
   curl -s "https://raw.githubusercontent.com/$SLUG/HEAD/$PATH" -o payload.txt
   ```
   Use `compose/code/p441-tree-licence-enumeration/enumerate_licence.py` to find `$PATH`, because a
   filename list cannot sustain a licence's absence (`P441`) — `openedx/XBlock` ships `LICENSE.TXT`
   and `Opetushallitus/aoe` ships `aoe-web-frontend/LICENSE`.

2. **Read the TITLE, which is the first non-blank line, and never a mid-document match.**
   ```sh
   grep -v '^[[:space:]]*$' payload.txt | head -2
   ```
   This single step separates `GNU GENERAL PUBLIC LICENSE Version 2` from
   `GNU LESSER GENERAL PUBLIC LICENSE Version 2.1`, which is the distinction seven rows on this
   shelf got wrong. The reason a window fails is in
   `compose/code/p436-fork-hypothesis/sweep_payload.py` (`P452`).

3. **Cross-check against the byte size — free, and it caught two rows this pass.**

   | Licence | Payload size |
   |---|---|
   | GPL-3.0 | ~35 kB |
   | LGPL-2.1 | ~26.5 kB |
   | GPL-2.0 | ~18 kB |
   | AGPL-3.0 | ~34 kB |
   | LGPL-3.0 | **~7.6 kB** |
   | Apache-2.0 | ~11.3 kB |
   | MPL-2.0 | ~16.7 kB |
   | MIT | ~1.1 kB |
   | EUPL reference notice | 0.3–0.7 kB |

   A row reading *"LGPL-3.0 (35,199 B)"* is wrong on its face. Both of this pass's prose errors were
   visible this way with no network at all.

4. **For Creative Commons, the qualifier IS the finding (`P449`).**
   ```sh
   head -3 payload.txt | grep -Eoi 'noncommercial|sharealike|attribution'
   ```
   `CC-BY` is four licences. Four of the seven CC rows on this shelf are **NonCommercial**. Publish
   `CC BY-NC-SA 4.0`; never publish `CC`.

5. **For GNU, record the VERSION and whether an exception is attached.** `GPL-2.0` and `GPL-3.0`
   differ on patent and compatibility terms; `GPL + Classpath/linking exception` behaves like the
   LGPL and a substring classifier cannot see the exception at all (`nvaccess/nvda`'s
   `copying.txt`). If the payload names more than one family, the row is a **reading list**, not a
   verdict — 73 of 412 payloads here name two or more.

6. **Scan for a second grant below the root before you write a repository off.**
   ```sh
   git clone --filter=blob:none --no-checkout --depth 1 "https://github.com/$SLUG" t
   git -C t ls-tree -r --name-only HEAD | grep -Ei '(^|/)(un)?licen[cs]e|(^|/)copying'
   ```
   On this shelf the second grant is usually the **documentation** and usually **more** permissive:
   `microsoft/autogen` is CC-BY at the root and **MIT in `LICENSE-CODE`**; `learnhouse/learnhouse`
   is AGPL-3.0 with **MIT in `docs/`**. **Zero of 412** repositories hide a reciprocal grant under a
   permissive root, so this step only ever opens doors. Ignore anything under `node_modules/`,
   `vendor/`, `third_party/`, and any file whose own name says `THIRD-PARTY`, `NOTICE` or
   `dependencies` — a notice about other people's licences is not a grant (`P342`).

7. **Gate the answer against what your own knowledge base already says.**
   ```sh
   cd compose/code/p449-prose-tsv-reconciliation
   python3 reconcile.py ../../../agents/top.md … <measured.tsv> <published.tsv>
   ```
   This is the step nobody had. Where prose and data disagree on a licence in this corpus, **the
   prose has been right 18 times out of 19** — so a disagreement is a signal to re-read the payload,
   and the one case where the prose lost was prose a defective classifier had overwritten.

**Wiring, as an engagement artefact.** Run steps 1–6 as a pre-bid gate over the client's candidate
component list and deliver the output as a two-column table — `family` for comparability, `qualifier`
for the decision — plus a third column naming the **channel** each answer came from. Budget: one
day for up to ~80 components at the measured rates (412 payloads read and 412 trees enumerated in
64 s; the human time is reading the ~10% that name more than one family). Step 7 only applies if the
client keeps a knowledge base of their own, and when they do it is the step that finds the
regressions.

**What this pattern is NOT.** It does not produce a legal opinion, and it does not resolve a
`GPL + exception` payload or an RTF grant — both are declared limits of the instruments it calls.
It produces the **reading list** a lawyer should be given, and it refuses rather than guessing: 13
of 412 payloads here still classify `UNKNOWN`, and `UNKNOWN` is published as a refusal, not as
"permissive".

### How this pattern changes the three patterns above it

- **`P34` (certified-conformant assessment delivery)** was built on `oat-sa/lib-lti1p3-core` and
  `Citolab/qti-components` as **LGPL** components behind a linking boundary. Both are **plain GPL**.
  🔴 **The linking boundary is not a defence any more.** Re-wire `P34` to call both across a
  **process** boundary — a separate service with its own repository and its own source offer — or
  price a commercial licence from OAT. This is the one place in this KB where a licence correction
  invalidates a published architecture.
- **`P35` (national open-data MCP client, LATAM)** reads `inepdadosabertos/api` and `yunger7/enem-api`,
  both now **GPL-2.0**. The pattern already consumes them **over HTTP as data sources**, not as
  linked libraries, so it is unaffected — stated explicitly so a later pass does not re-open it.
- **`P36` (accessible-courseware remediation)** depends on `dequelabs/axe-core` and
  `ocrmypdf/OCRmyPDF`, both of which moved **GPL → MPL-2.0**, which is *less* restrictive than
  filed. MPL-2.0 is file-level copyleft, so invoking either as an unmodified tool propagates
  nothing. 🟢 **The pattern gets cheaper, and its original reasoning was already correct in prose.**

---

## P37 — The two-reader licence gate (due diligence you can hand to procurement)

**Use when:** an engagement will ship, resell or embed open-source education components — so
someone will eventually ask, in writing, which licences the deliverable carries. Which is
every engagement on this shelf.

**Why two readers rather than a better one.** Measured on this KB's own 412 education
repositories, across two concurrent passes: two independently hardened licence classifiers,
each with a passing regression suite, **disagreed on 43 payloads (10.4%)**. After repairs on
both sides the disagreement fell to **10 (2.4%)** — and every row that moved was a real
defect. 🔴 **The five rows that can put a non-commercial asset into a billable deliverable
are still open**, because each pass fixed the classifier it was looking at. A single scanner
does not have a lower error rate than 10.4% — it has an **unmeasured** one. The deliverable
here is not a green dashboard; it is a **named list of contested rows**, which is the only
licence artefact that survives a procurement conversation.

### Components

| Role | Component | Licence | Why this one |
|---|---|---|---|
| Reader A — fine vocabulary | `compose/code/lib/license_family.sh` | this KB | answers `CC-BY-NC-SA-4.0`, `EUPL-1.1`, `Elastic`, `PolyForm`; carries the independent **commercial-use axis** |
| Reader B — coarse vocabulary | `compose/code/p436-fork-hypothesis/sweep_payload.py` | this KB | deliberately coarse so its output stays comparable with a published table; different blind spots by construction |
| Composition | `compose/code/p459-unified-verdict/unified.py` | this KB | one verdict, disagreements **printed not resolved** |
| Divergence report | `compose/code/p445-classifier-divergence/divergence.py` | this KB | the artefact procurement actually wants |
| Third opinion (optional) | [licensee/licensee](https://github.com/licensee/licensee) (MIT) or [nexB/scancode-toolkit](https://github.com/nexB/scancode-toolkit) (Apache-2.0) | MIT / Apache-2.0 | an outside reader, so the pair does not share a lineage |

### Wiring

1. **Enumerate, do not guess at filenames.** Walk the repository tree and treat *every*
   grant-shaped path as a candidate — `p441`'s enumeration found 9 grants where two filename
   lists found zero and one. Two platforms here (`OS4ED/openSIS-Classic`,
   `OS4ED/openSIS-Responsive-Design`) have **no root licence at all**; their grant is only at
   `docs/License.txt`.
2. **Read both layers.** Root payloads *and* every grant below the root. On this corpus the
   tree layer held no NonCommercial surprise — 0 of 76 — but it held the only licence evidence
   two real platforms have.
3. **Run both readers over the same bytes.** Pass the payload on **stdin**, never as an argv
   string: several licence texts exceed 35 kB and argv truncation would present as a
   classifier disagreement rather than a plumbing fault.
4. **Compose conservatively, and put the restriction before the gate.** Commercial use is
   ALLOWED only if both readers allow it. A payload whose family **neither** reader can name
   can still forbid commercial use — three rows here are exactly that — so *"we could not
   name this licence"* must never overwrite *"this licence forbids what you want to do with
   it."*
5. **Decline on containers.** A licence shipped as RTF or PDF puts markup in the title block;
   every family probe declines, and an unclassified family is precisely the state in which
   tools fall back to token-matching the body. On this shelf that read GPL-2.0 §3(c)'s
   *"allowed only for noncommercial distribution"* — a condition on one distribution option —
   as a restriction, and turned a usable SIS platform into a reject. Report `CONTAINER-RTF`
   and **ask the vendor for plain text**; that request is itself a due-diligence finding.
6. **Resolve EUPL to its version.** Six of the nine EUPL repositories here are **1.1**, not
   1.2, and the two carry different compatibility lists. For any EMEA public-sector build this
   is a procurement fact, not a detail.
7. **Pin the gaps you do not close.** Where one reader is known blind, assert the
   one-sided flag in a test **and state that the assertion must flip when the gap closes** —
   `p459/test_unified.py` does exactly this for the NonCommercial axis. A test that goes red
   when a defect is *fixed* is how a known gap cannot be closed silently and the flag left
   behind as noise.
8. **Publish three lists, not one score:** 🟢 agreed-and-usable, 🔴 agreed-and-restricted,
   ⚠️ **contested** — with both readers' answers side by side for every contested row.

### What it produces

- A per-component licence table where every row names **which reader said what**.
- A contested list — on this corpus **10 of 412** — small enough for a lawyer to read in an
  afternoon, and a **5-row subset explicitly marked as the commercially dangerous class**.
- A declined list (containers, pointer files, `REUSE`-spec repositories), stated as a limit
  rather than hidden inside a pass.

**Effort:** 1 week to stand up against a client's dependency set; a few hours per re-run.
Re-run it on **every dependency bump**, because the grant moves — and re-run it after *your
own* fixes, because this pattern's own history is two concurrent repairs that each left the
other's blind spot in place.

⚠️ **What this pattern is not.** It is not legal advice and does not replace counsel. It
replaces what most engagements actually do — **one scanner, once, and a green tick** — and
gives counsel a list worth reading instead of a dashboard worth ignoring.

## P-31.1 — Permissive-base AI learning platform on MIT Sunbird (APAC-first, redistributable)

**Problem it solves.** A client needs an AI-assisted learning platform **they can redistribute or
resell**. A Moodle (GPL-3.0) or Open edX (AGPL-3.0) base makes that a licence event; most engagements
discover this after the architecture is set.

**Wiring.**

1. **LMS core — MIT, in-tree modification permitted.**
   [`project-sunbird/sunbird-lms-service`](https://github.com/project-sunbird/sunbird-lms-service)
   (MIT) + [`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal) (MIT).
   National-scale provenance via DIKSHA.
2. **Learner state — persistent, not stateless.** Pattern the state model on
   [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, **canonical** —
   not the `kvnloo` fork): durable learner state, review scheduling, misconception tracking,
   auditable pedagogical decisions. Expose it to the LLM over MCP.
3. **Serving — self-hosted open weights,** per the regional substrate already shelved in
   `repos/foundations.md` (Indian/ASEAN language stacks, passes 6–7). Self-hosting is what satisfies
   EU AI Act documentation duties and Korean/Japanese EdTech privacy rules in the same build.
4. **Oversight gate — mandatory, not optional.** Every assessment-affecting output is a *suggestion*
   with a logged human decision. This is the **OK/MD** "AI may not make high-stakes decisions" shape
   and the EU AI Act human-oversight obligation, satisfied by one mechanism.
5. **Data boundary.** Store learner state; **never route it into training.** This is **CA AB 1159**
   literally, and good practice everywhere.
6. **Enablement.** Ship faculty training built from
   [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book) (**Apache-2.0**, redistributable).
   🔴 **Do not use** `datawhalechina/hello-agents` in client material — **CC BY-NC-SA 4.0**,
   NonCommercial.

**Why this composition:** steps 1 and 6 are the only two education components verified this pass that
are *both* buildable and redistributable. Steps 4 and 5 are the two constraints that appear in all
four regions' rules, so building them in once avoids four divergent forks.

---

## P-31.2 — Compliant autograding: propose-and-review, with the grader itself under test

**Problem it solves.** Autograding is the highest-value education workflow and the one most directly
restricted: Oklahoma and Maryland **ban AI from high-stakes decisions about students**, the EU AI Act
treats *assessing learning outcomes* as high-risk, and several APAC statutes name **automated
assessment** explicitly. Meanwhile LATAM data shows **assessment is the lowest-adoption area** and
**61% of students fear peer misuse** — so trust, not throughput, is the blocker.

**Wiring.** Take the architecture from
[`pawtograder/platform`](https://github.com/pawtograder/platform) — **study it, self-host it, or
re-implement the separation; do not link it into a proprietary deliverable (GPL-3.0-or-later)**:

1. **Deterministic CI layer first.** Tests run in CI per
   [`pawtograder/assignment-action`](https://github.com/pawtograder/assignment-action): objective,
   reproducible, explainable to a student. No model in this path.
2. **Model layer proposes only** — rubric-aligned draft feedback and a suggested band, never a
   committed grade.
3. **Handgrading as a distinct human-authority step**, with the rubric as the interface and the human
   decision recorded. Pawtograder already separates these two; adopt the separation.
4. **Regression-test the graders themselves.** Pawtograder's assignment-action regression-tests
   graders — in a regulated setting this doubles as your **evaluation evidence** for conformity
   documentation.
5. **Staff-side MCP context, not student-side autonomy.** Course context to instructors over MCP
   (Pawtograder's own posture) sits in UNESCO's *teacher-supporting* tier — medium-high confidence —
   rather than the lowest-confidence student-facing tier.
6. **Appeal path and audit log** as first-class features. This is what converts the LATAM integrity
   anxiety into a selling point instead of a risk.

**Deliverable framing by region.** Same build, four evidence packages: **NA** — per-state matrix
(CA training-data prohibition, OK/MD oversight); **EMEA** — high-risk technical documentation,
logging and human-oversight evidence under the Act enforcing since 2 Aug 2026; **APAC** — KR/VN/TW
statutory mapping plus Korean EdTech privacy protocols; **LATAM** — institutional governance
starter mapped to the UNESCO LAC Observatory framing, addressing the **~55% of institutions with no
AI guidance**.
