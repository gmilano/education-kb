---
industry: education
region: Global
updated: 2026-10-22
---

# Foundational repos for education

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Prior version archived at
[`archive/2026-10-22-p383-pre-rewrite/repos-foundations.md`](../archive/2026-10-22-p383-pre-rewrite/repos-foundations.md).
Every address verified first-hand on this date — method and channel notes in
[`agents/top.md`](../agents/top.md#verification-method), raw results in
[`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv).

🆕 **Pass `p389` · 2026-10-22 — increment.** Every address on this shelf is now **dated**: a blobless
shallow clone (`git clone --depth 1 --filter=blob:none --no-checkout`, ~1.2 s, no API, no credentials)
returns the real default ref, the HEAD SHA and the **last commit date**, and `git show HEAD:LICENSE`
returns the grant from the payload at that ref. Method in
[`agents/top.md`](../agents/top.md#verification-method); **60 rows** in
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). **This changes the headline claim
of this file — see the paragraph after the table below** — and it adds three repos to *Tier 4*.

## 🔴 Read this before choosing a base: the licence frontier in education runs the wrong way

**The platform tier is copyleft. The agent tier is permissive.** That is the single most
consequential structural fact in this industry for a studio that needs to ship client-owned code:

| tier | licences actually found | what it means |
|---|---|---|
| **LMS / platform** | GPL-3.0 (Moodle, Chamilo, ILIAS, H5P), AGPL-3.0 (Open edX, Canvas, Tutor, Frappe LMS), ECL-2.0 (Sakai, Opencast), LGPL-3.0 (OpenEduCat) | Forking the platform pulls copyleft into the deliverable. AGPL additionally reaches **hosted** use. |
| **the one exception** | 🟢 **Apache-2.0 — [OpenOLAT](https://github.com/OpenOLAT/OpenOLAT)** | The only major open-source LMS a studio can extend with closed code. Underweighted by every roundup we read. |
| **agents / tooling** | MIT, Apache-2.0, BSD-3 almost throughout | Permissive. |

🆕 `p389` — **the "one exception" row is wrong, and the dating is what shows it.** There are **four**
permissive platform-tier bases on this shelf, not one, and the reason the claim survived this long is
that the other three were each filed as something narrower than a platform:

| permissive platform base | licence | last commit | the role it actually fills |
|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for an **institution**. Swiss, mature, full LMS. |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | 🔴 `master` | 🟢 **MIT** *(`LICENSE.md`)* | 🆕 `p390`. 🟢 **The permissive courseware engine, and the gap it fills is a licence gap rather than a feature gap.** **Torus** is the authoring-and-delivery platform behind **Carnegie Mellon's Open Learning Initiative** — the group whose course-effectiveness studies are the most-cited evidence base in the field. Pages, structured activities, adaptive **scripted "advanced authoring"** activities, mastery/proficiency reporting per learning objective, LTI 1.3 delivery into a host LMS, and a research-grade analytics surface. 🟢 **Everything else at this scale is copyleft** (Open edX AGPL-3, Canvas AGPL-3, Moodle GPL-3) — so when a client needs to *ship a modified platform* rather than host one, this is the only row on this shelf that lets them. Elixir/Phoenix + PostgreSQL. Dated **2026-10-22** — committed today. 🔴 **Mind the slug:** `CMU-OpenLearning/oli-torus` does not resolve; the canonical owner is `Simon-Initiative`. 🟡 Elixir is a real staffing constraint for most studio teams — cost it before proposing it. |
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 🟢 **2026-10-22 (0 d)** | The permissive base for **pedagogy**: misconception-aware branching lessons. Filed in *Tier 2* as content, but it is a platform. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **2026-10-22 (0 d)** | The permissive base for **low-connectivity delivery**, and the only MIT one. Filed as a runtime; it is the platform in any engagement where bandwidth is the constraint. |
| [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT** | 🟢 **2026-10-21 (1 d)** | The permissive base for a **course**. |

🔵 **What to say instead of "the platform tier is copyleft."** *The platform tier is copyleft wherever
the install base is* — Moodle, Canvas, Open edX, Chamilo, ILIAS are where the clients already are, and
those are GPL/AGPL/ECL. **Permissive platform bases exist, are all actively maintained, and all cost you
the install base.** That is a trade a client can be walked through; "there is one exception" was not.
The design consequence below is unchanged and is still the default — it is the *greenfield* branch of
the decision that just got three more options.

🆕 `p385` **And a third axis the table above cannot show: the grant can differ by *ref* within one
repository.** [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) reads **AGPL-3.0** at
`main` (34,523 B) and **MIT** at tag **`v0.1.0`** (1,081 B) — both read first-hand this pass. It relicensed on
**2026-08-16**. 🔵 So "what is this repository licensed as?" is not a well-formed question; **"what is it
licensed as at the ref I am shipping?"** is. That is now **Pattern L step 10**, and it cuts both ways: a
permissive grant can be *retrievable at a tag* after the project has moved away from it, and a repository
a prior audit cleared as MIT can be AGPL at `main` today.

**The design consequence**, not a preference: compose permissive agents **over** a copyleft platform
across a documented interop boundary — **LTI 1.3**, **MCP**, or the platform's web-services API —
rather than forking the platform. Recipes in [`compose/patterns.md`](../compose/patterns.md).

## Tier 1 — Learning platforms

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `main` | 🟡 **GPL-3.0** — 🔴 grant is in **`COPYING.txt`**, there is **no root `LICENSE`** | The install base. Moodle Pty Ltd reports 400M+ users and ~150,000 registered sites. Originates in Australia (APAC). Huge plugin catalogue, and now a first-party MCP path. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 `master` | 🔴 **AGPL-3.0** | The MOOC-scale platform: LTI 1.3, XBlocks, deep data control. Deploy via `tutor` below, not by hand. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | 🔴 `master` | 🔴 **AGPL-3.0** | Dominant in North American higher ed. Open-**core**: the published tree is not the commercial ecosystem, so scope assumptions break on integration. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🔴 `master` | 🟢 **Apache-2.0** | Swiss, mature, permissive. The default recommendation whenever a client needs to own closed extensions to the LMS itself. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 `master` | 🟡 **GPL-3.0** | The LATAM/EMEA public-sector base. Strongest Spanish/Portuguese-language footing of any platform here. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🔴 `master` | 🟡 **ECL-2.0** | Apache-2.0-derived **Educational Community License** — permissive-shaped with an education-specific patent/attribution twist. Read it; do not assume Apache. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | 🟡 **GPL-3.0** | German public-sector LMS and the learning component of the openDesk sovereign stack. Default ref is a release branch. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | 🔴 **`release`** | 🔴 **AGPL-3.0** *(`LICENSE.txt`)* | The Docker distribution for Open edX and the de-facto deployment path. Nobody should be installing `edx-platform` without it. |
| [inducer/relate](https://github.com/inducer/relate) | `main` | 🟢 **MIT** *(`LICENSE`, 1,145 B — "MIT/X Consortium license")* | 🆕 `p384`. Django courseware with autograding, flexible access rules, per-student statistics and multi-course support. 🟢 **Permissive at the platform level**, which almost nothing else in this tier is. 🟡 Courseware-scale: the permissive base for a **course**, where OpenOLAT is the permissive base for an **institution**. Do not pitch it as a Moodle replacement. |
| [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | `main` | 🔴 **AGPL-3.0-only** *(`LICENSE`, 34,523 B; `pyproject.toml` → `AGPL-3.0-only`)* | 🆕 `p387`. 🟢 **The platform's own AI extension point — read this before anyone proposes forking Open edX to add AI.** First-party `openedx` org, so the extension surface is maintained with the platform rather than against it; the grant matches the platform's, which is why it can exist inside it. 🟡 Marked **experimental, not for production** in its own docs, so treat it as the contract to build against, not the thing to ship. Compare [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) (`main`, AGPL-3.0, Aulasneo — Argentina) for the LATAM-maintained customisation route. |

## Tier 2 — Content, courseware and assessment

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 `develop` | 🟢 **Apache-2.0** | Structured interactive lessons with a real pedagogy engine (misconception-aware branching). Permissive, which is rare at this level of pedagogical depth. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🔴 `develop` | 🟢 **MIT** | Offline-first learning runtime for low-connectivity deployment. The single most important repo on this shelf for LATAM and African engagements. |
| [serlo/serlo.org](https://github.com/serlo/serlo.org) | `main` | 🟢 **Apache-2.0** | German open learning platform — permissive, EMEA-native, curriculum-aligned content model. 🔴 🆕 `p390` **Dated: last commit `2023-02-09` — 1,351 days.** Serlo the *service* is very much alive (`serlo.org` serves German schools daily); this *repository* is not where it is developed any more. Keep it as the **content-model reference** — the permissive, curriculum-aligned data shape is still the most useful thing here — but do not plan a fork or a dependency on it, and ask Serlo where the current code lives before quoting an EMEA-native platform base. |
| [openfun/richie](https://github.com/openfun/richie) | 🔴 `master` | 🟢 **MIT** | Course catalogue and portal front-end from France Université Numérique. Pairs with Open edX as the public face. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 `master` | 🟡 **GPL-3.0** *(`LICENSE.txt`)* | Interactive content types embedded in nearly every LMS. 🔴 **Routinely described as MIT; it is not.** Keep H5P as *content* loaded at runtime, not as linked code. |
| [openedx/edx-ora2](https://github.com/openedx/edx-ora2) | 🔴 `master` | 🔴 **AGPL-3.0** | Open-response and peer assessment. 🔴 `edx/openassessment` and `openedx/openassessment` are both **DEAD** — this is the live address. |
| [opencast/opencast](https://github.com/opencast/opencast) | 🔴 `develop` | 🟡 **ECL-2.0** | Lecture capture and video pipeline. 🔴 `apereo/opencast` is **DEAD**; use this org. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(`LICENSE.md`, 11,342 B; `composer.json` declares `"license": "Apache-2.0"`)* | 🟢 **THE LTI 1.3 DEPENDENCY TO INSTALL — and it corrects `p390`'s finding #1, which told three shelves there was none.** LTI 1.3 is *the* standards surface for putting an agent inside Moodle, Canvas, Blackboard or D2L, and this is a **live** implementation of it: HEAD `66d8e4e`, **2026-10-16 — 6 days**, shipping as packagist **`packbackbooks/lti-1p3-tool` v6.4.4, 68 versions, published 2026-09-23**. Same Apache-2.0 grant as the 1EdTech copy (byte-identical 11,342 B licence), under active maintenance. 🟢 It keeps the **copyleft-firewall** role intact: permissive code talks to a GPL/AGPL platform over the LTI boundary without linking to it. 🔵 Note the ref is **`master`**, not `main` — a `main`-assuming licence read fails silently. |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) 🆕 `p391` | `master` | 🟢 **Apache-2.0** *(11,360 B; `package.json` agrees)* | 🟢 **The Node LTI 1.3 route, and the better default for an agent stack.** HEAD `41f150c`, **2026-10-13 — 9 days**; npm **`ltijs` v7.0.7, 207 published versions, 2026-10-06** — the most actively released LTI implementation this base has read. A standalone LTI *tool* provider rather than a platform plugin, which is the shape an agent engagement actually needs: the agent is its own service, and the LMS launches into it. 🟢 Prefer this over the PHP line unless the client's platform work is already PHP (a Moodle plugin, an Open edX fork). |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | 🔴 `master` | 🟢 **Apache-2.0** | 🔴 **DEMOTED to a spec citation — do not install it.** Last commit `2020-06-03` — **2,333 days**, and `composer.json` carries no licence field. An unmaintained PHP library handling OAuth 2 / JWT signing and key rotation is a **security** dependency, not merely a compatibility one. 🟢 The architectural role it was shelved for is not lost: it moves to `packbackbooks/lti-1-3-php-library` (above), which is the maintained line. 🔴 🆕 `p391` **It also has an alias:** [`IMSGlobal/lti-1-3-php-library`](https://github.com/IMSGlobal/lti-1-3-php-library) returns the **identical HEAD sha `3a192de`** — an org rename, one project at two addresses. Counted **once**. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) 🆕 `p391` | `master` | 🟡 **MIT** | 🔴 **The Python LTI route, and it is genuinely dead — which is an architecture constraint, not a shelf note.** Last commit `2022-11-21` — **1,431 days**; PyPI **`PyLTI1p3` 2.0.0, published 2022-11-20**, 29 releases, none since. Almost every agent on these shelves is Python, so there is **no maintained in-process Python LTI option**: the edge must be **`ltijs` (Node) or `packbackbooks` (PHP) fronting the Python agent over HTTP**. 🆕 `Gap 391-A`. || [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main` | 🟡 **`(ODbL-1.0 AND CC-BY-SA-4.0)`** 🆕 `p390` *(exact SPDX expression, read from `package.json`; the tree carries **two** files — `LICENSE` (ODbL, 25,289 B) and `LICENSE-CONTENT`. There is still no separate permissive code grant.)* | 🆕 `p384`. **The curriculum prerequisite graph**: `v1` ships **1,930 micro-topics** and **4,102 prerequisite edges** as a DAG (`hard`/`soft`, each edge carrying a reason) over **9 subjects**, aligned to NGSS, Common Core, the UK National Curriculum and the Australian curriculum. Data at `data/topics.json`, `data/dependencies.json`, `data/teaching-research.json` (~24 MB). 🔴 **A share-alike *database* licence, not a code licence** — grounding a tutor on it is a §4.3 *Produced Work* (attribution notice only); shipping an extended taxonomy is a §4.4 *Derivative Database* (share-alike). See **Pattern H**. 🟡 Maintainer-stated gap: teaching research covers **1,049** topics, **881 have none**. 🔴 🆕 `p390` **The `CC-BY-SA-4.0` half is the one that reaches the client deliverable**: the *content* (topic prose, teaching research) is share-alike independently of the ODbL database right, so a curriculum document generated from it can inherit SA even where the DAG itself is only a Produced Work. Clear this with the client's legal team **before** it is a deliverable, not after. Dated `2026-10-22` — actively maintained. |
| [intellectif/learning-kit](https://github.com/intellectif/learning-kit) 🆕 `p391` | `main` | 🟢 **MIT** *(1,071 B; `package.json` agrees)* | 🟢 **A permissive, headless alternative to H5P — and the assessment component this shelf was thin on.** TypeScript-first SDK for interactive educational activities, described by its own README as *"a lightweight, composable, bring-your-own-backend alternative to H5P"*, for React 19. `@intellectif/lk-core` is the part that matters to a studio: **schemas, a pure scoring engine, rubric and deferred grading, assessment composition, attempt plans, redaction, and an xAPI statement builder — with zero runtime dependencies beyond Zod**. `@intellectif/lk-react` adds components and a resumable exam/review pager. 🟢 **Three properties that decide an engagement:** scoring is a *pure function* a client can unit-test and an auditor can read; **deferred grading** means a human marker stays in the loop by construction, which is the posture EU high-risk assessment obligations ask for; and **redaction** is in the core rather than bolted on. 🟢 Pairs directly with the xAPI/LRS rows on this shelf — it emits statements, it does not store them. HEAD `1e39e9e`, **2026-10-18 — 4 days**. 🔴 **It is deliberately not a CMS:** authoring UI, content storage, delivery, auth and the learner database are the consuming application's job. 🟡 The two packages' version numbers moved apart at 1.0, so a `lk-react` major is not by itself a breaking React API change — read its changelog. |

## Tier 3 — Grading, notebooks and the CS-teaching stack

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | `main` | 🟢 **BSD-3-Clause** | Multi-user notebook serving — the standard way a cohort gets identical compute. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | `main` | 🟢 **BSD-3-Clause** | Release / collect / autograde / return. The assignment lifecycle, already solved. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🔴 `master` | 🟢 **BSD-3-Clause** | Autograding at Berkeley cohort scale; container-isolated execution. |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Pedagogical assessment of *how* code was written. The missing half of autograding. 🔴 🆕 `p387`: **PyPI `pybryt` has had no release since v0.7.0 on 2022-04-28.** Keep it as the design it states, vendor the code, and do not sell a client a dependency that has not shipped in four and a half years. The maintained halves of this tier (`nbgrader`, `otter-grader`) are where the running infrastructure should sit. |

## Tier 4 — Measurement, memory and retrieval (what makes the agents honest)

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | 🟢 **MIT** *(`LICENSE.md`)* | The eval runner. Nothing in this industry should ship without a before/after on the client's own subject mix. |
| [hendrycks/test](https://github.com/hendrycks/test) | 🔴 `master` | 🟢 **MIT** | **MMLU** — 57 academic subjects. The subject-level breakdown is the useful part, not the headline score. |
| [openai/grade-school-math](https://github.com/openai/grade-school-math) | 🔴 `master` | 🟢 **MIT** | **GSM8K** — multi-step arithmetic reasoning; the canonical K-12 maths probe. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | 🟢 **MIT** | **FSRS** scheduler. A retention model with published parameters — the part of "personalisation" that is actually measurable. Note [ankitects/anki](https://github.com/ankitects/anki) itself is **AGPL-3.0**; the scheduler is the reusable piece. |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | 🟢 **Apache-2.0** | Document-aware RAG — handles the textbook/worksheet/PDF reality of course material. |
| [livekit/agents](https://github.com/livekit/agents) | `main` | 🟢 **Apache-2.0** | 🆕 `p390`. 🟢 **The realtime voice substrate — the piece a spoken tutor should never write itself.** Full-duplex STT → LLM → TTS pipelines with **turn detection, interruption handling and barge-in**, the three things that separate a tutor a child will talk to from a demo. Provider-agnostic on all three legs, so the ASR can be swapped for a local model where data residency demands it. This is what `Manu` (Tier 4, [`agents/top.md`](../agents/top.md)) is built on, and why that project is ~15 days old and already has a working voice loop. Dated **2026-10-22**. See 🆕 `Pattern V`. |
| [mozilla/common-voice](https://github.com/mozilla/common-voice) | `main` | 🟡 **MPL-2.0** *(code; the **corpora** are **CC0-1.0**)* | 🆕 `p390`. 🟢 **The licence answer to regional-language speech.** Crowd-sourced, CC0 speech corpora across ~130 language variants — including **pt-BR, es-419 variants, Kiswahili, Hindi and Bengali** — which is the fine-tuning and ASR-evaluation data a voice tutor needs outside English. 🟢 **CC0 on the data is the strongest possible position**: no attribution, no share-alike, usable in a commercial deliverable. 🟡 MPL-2.0 is weak file-level copyleft and applies to the **platform code**, not the corpora — do not conflate the two when quoting. Dated **2026-10-21**. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | `main` | 🟢 **Apache-2.0** *(`LICENSE.md`)* | Ingest for the formats education actually runs on: PDF, DOCX, PPTX, scans. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | 🟢 **MIT** | Programmatic prompt optimisation — turns "we tuned the tutor prompt" into something with a metric attached. |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | 🟢 **MIT** | The campus LLM gateway universities actually deploy: multi-provider, SSO, per-user quota, audit. MIT where the obvious alternative is not (see [`agents/top.md`](../agents/top.md)). |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | 🔴 `master` | 🟢 **MIT** | 🆕 `p389`. **Bayesian Knowledge Tracing, fitted from the client's own interaction logs** — and the maintained answer to a gap this base has carried for two passes. `Pattern B` stands on [microsoft/pybryt](https://github.com/microsoft/pybryt), whose published artefact has had **no release since 2022-04**; this is a *different* job (mastery estimation, not approach assessment) but it is the piece that makes "adaptive" a number instead of an adjective. 🟢 **Last commit 2026-10-21 (1 d)**, from UC Berkeley's CAHLR, who also maintain [`OATutor`](https://github.com/CAHLR/OATutor) (MIT) on [`agents/top.md`](../agents/top.md). 🟢 Per-skill learn/guess/slip/forget parameters are inspectable and defensible — which is what a district's procurement rubric asks for when it asks how the system decides a student is behind. |
| [docling-project/docling](https://github.com/docling-project/docling) | `main` | 🟢 **MIT** | 🆕 `p389`. **Course-material ingest, MIT, and committed today (0 d).** Layout-aware parsing of PDF, DOCX, PPTX, XLSX, HTML and images into a structured document model, with table structure and reading order preserved — which is the difference between a tutor that can cite page 7's table and one that cannot. 🟢 Chosen over [allenai/olmocr](https://github.com/allenai/olmocr) (Apache-2.0) **on the date**: olmocr's last commit is **2026-03-25, 211 days**. 🟢 Complements, not replaces, [`unstructured`](https://github.com/Unstructured-IO/unstructured) — docling is the stronger reader for textbook-shaped PDFs, `unstructured` has the wider connector set. |
| [jupyterlite/jupyterlite](https://github.com/jupyterlite/jupyterlite) | `main` | 🟢 **BSD-3-Clause** | 🆕 `p389`. **Jupyter with no server: the kernel runs in the browser via WebAssembly.** Last commit 2026-10-16 (6 d). 🟢 Two education problems it solves outright: a CS or data-science exercise that needs **no per-student compute, no container and no install** (the cost line that kills notebook teaching at scale), and a **lab that works offline once the page is cached** — the `Pattern D` constraint, met without shipping a server. 🟡 No server means no server-side autograding: pair it with [`nbgrader`](https://github.com/jupyter/nbgrader) on a submitted notebook rather than expecting it to assess in place. |
| [pipeworx-io/mcp-education-data](https://github.com/pipeworx-io/mcp-education-data) 🆕 `p391` | `main` | 🟢 **MIT** *(1,069 B; `package.json` agrees)* | 🟢 **The first row on these shelves that answers *which district*, rather than *what to build* — engagement targeting and funding data, not a classroom capability.** Four MCP tools over **keyless US federal data**: `education_find_schools` (NCES Common Core of Data via the Urban Institute — enrolment, charter/magnet status, grade range, free/reduced-price lunch counts), `education_find_districts` (LEA id, schools, enrolment, teacher counts), **`education_district_finance`** (revenue split **federal / state / local** and expenditure by function, with computed **per-pupil spending**) and **`education_child_poverty`** (Census SAIPE estimates of 5–17-year-olds in poverty — **the figures that drive federal Title I funding**). 🟢 **Why a studio cares:** a North America pitch can be priced against a named district's actual per-pupil budget and Title I eligibility before the first call. 🔴 **Three caveats that belong in the row:** it is an **unofficial** integration, not affiliated with the upstream provider; the default path is a **hosted gateway** (`gateway.pipeworx.io`), so a district deployment means self-hosting or accepting a third party in the data path — the data is public, but the *query pattern* may not be something a client wants off-premises; and a scoped endpoint also lists **~30 shared gateway meta-tools**, so the real context cost is far above four tools. 🟡 The finance survey **lags the directory data by 1–2 years** — never quote per-pupil spend as current-year. HEAD `060371b`, **2026-10-21 — 1 day**. |

## Tier 5 — Student information / administration

| repo | default ref | licence | note |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | 🟡 **LGPL-3.0** | Odoo-based education ERP/SIS. Default ref is a **version branch**, `19.0` — there is no `main`. 🔴 `OpenEduCat/OpenEduCat` is **DEAD**; this is the live address. Its Brazil and Mexico country pages are vendor marketing — treat feature claims as unverified. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | `main` | 🟢 **MIT** | Laravel school-management platform with **Spanish and French built in**. SME-scale, not university-scale. The only permissive, Spanish-native administration platform found in this pass — relevant to the LATAM supply gap recorded in [`intel/market.md`](../intel/market.md). |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | 🔴 **`master`** | 🟡 **GPL-2.0** — 🔴 grant is at **`docs/License.txt`** (17,286 B), **not** at any root path; `index.php` and `Modules.php` headers pin *"version 2 of the License"* | 🆕 `p384`. The most widely deployed open-source SIS in the K-12 tier. GPL-2.0 is survivable the same way Moodle is — reach it over its API, do not link to it. 🔵 **This repo is why the licence probe set grew from seven paths to eight**: a root-only read returns "ungranted" for a repository with a perfectly standard grant one directory down. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 `develop` | 🔴 **AGPL-3.0** — grant is in lowercase **`license.txt`** | Frappe/ERPNext-ecosystem LMS; attractive where the client already runs ERPNext. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | 🟡 **GPL-2.0-or-later** *(`2.12/LICENSE`, 18,092 B; `composer.json` → `GPL-2.0-or-later`)* | 🆕 `p387`. 🟢 **Brazil's largest free education software, and the SIS a LATAM public-sector engagement will actually meet** — *"o maior software livre educacional do Brasil"*, municipal-scale student records, enrolment, grades. 🔴 **Its real default ref is `2.12`** — a version branch, neither `main` nor `master`: resolved with `git ls-remote --symref` (HEAD `7903a3e`). A `main`-assuming clone or licence read fails or reads the wrong tree, and a `master`-assuming one reads a branch that is not HEAD. 🟡 GPL-2.0 at the platform, so reach it over its API and keep the agent a separate service (`Pattern O`). Sibling `portabilis/i-diario` is AGPL-3.0 — the grant is a per-repository fact, not an organisation-wide one. |

## 🆕 `p387` — Tier 6: the multi-tenant AI layer, which is the thing `p386`'s tenancy gap was asking for

`p386` replaced a licensing gap with a **tenancy** gap: every granted LMS MCP server authenticates
as the signed-in student, so *"a studio cannot deliver one of those to an institution."* On Moodle
the tenancy layer already exists, it is maintained by a state education authority, and this base
has never shelved it.

| repo | default ref | licence | why it is foundational |
|---|---|---|---|
| [bycs-lp/moodle-local_ai_manager](https://github.com/bycs-lp/moodle-local_ai_manager) | `main` | 🟡 **GPL-3.0-or-later — granted in the source headers** (`version.php`), no root licence file | 🟢 **A multi-tenant AI backend for Moodle, explicitly offered as the alternative to Moodle 4.5's own single-tenant AI subsystem.** Two subplugin types — `aitool` (connect ChatGPT, Gemini, Dall-E, **Ollama**…) and `aipurpose` (bind a *purpose* to a tool **per role**) — plus per-role rate limits, per-tenant user enable/disable, usage monitoring, teacher visibility of student prompts (capability-gated), and tenant-handling hooks. Release **5.1.1**, version code **2026102305**. 🟢 This is the component that turns "an agent talks to the LMS" into "an institution can deploy it": the **sovereign EMEA option in `Pattern E`**, from Bavaria's state school platform, with a local-model path via the Ollama tool. 🔵 **Cite this address.** The `mebis-lp` organisation serves the same repository at `mebis-lp/moodle-local_ai_manager`, which this base's alias register already records as **STALE** (canonical: `bycs-lp/moodle-local_ai_manager`, resolved `p350`, confirmed `p370`) — 🆕 `p387` re-confirms it mechanically: `git ls-remote --symref` returns the **identical HEAD sha `4ff5a87`** at both, and `version.php` the identical component, release **5.1.1** and version code **2026102305**, which upgrades `p226`'s sibling-set inference from *weak* to an identity read. One repository, one row. |
| [bycs-lp/moodle-block_ai_chat](https://github.com/bycs-lp/moodle-block_ai_chat) | `main` | 🟡 **GPL-3.0-or-later** in `version.php` | The chat frontend that consumes the manager's API. 🔵 Cited at the canonical org, as above; the manager's own README links the sibling set under `mebis-lp` — `tiny_ai`, `block_ai_control` — and both orgs answer, so resolve the ref before you pin one. The family also includes [marcusgreen/moodle-qtype_aitext](https://github.com/marcusgreen/moodle-qtype_aitext) (AI-marked question type, `main`, resolved this pass). **Deploy the manager first, then pick frontends** — not the other way round. |

🔵 **Second instance of `Pattern L` step 8, and it is now a Moodle-wide rule, not an anecdote.**
`p386` found [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp)
granted **only** in `version.php`. Both plugins above are the same: **no root licence file, a full
GPL-3.0-or-later header in `version.php`.** For a Moodle plugin that is the convention Moodle
requires, so *"no `LICENSE` file"* on a Moodle plugin means **read `version.php`**, never
"ungranted".

## 🆕 `p388` — Tier 7: the integration layer, reordered by maintenance rather than by tool count

`p387` dated this shelf and found its richest LMS integration was also its stalest. **This pass found
the replacements**, via a channel nobody here had asked: `registry.npmjs.org/-/v1/search` is open and
**indexes by relevance while reporting publish history**, so "does this exist?" and "is it
maintained?" are answered in one call. 29 education queries → 383 addresses absent from this base →
**22 granted**. Full method in [`repos/trending.md`](trending.md).

| repo | default ref · HEAD | licence | why it is foundational |
|---|---|---|---|
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` · `34e6156` | 🟢 **MIT** (1,070 B) | 🟢 **The maintained teacher/admin Canvas surface, and the new default for an institutional engagement.** 187 tools: grade, comment, rubrics, New Quizzes (LTI), gradebook *history*, enrollments, accounts, analytics, outcomes, grading standards, content exports/migrations, quiz **accommodations**, appointment groups — plus **link audit**, **accessibility audit** and **grade projection**, three deployment modes (stdio, HTTP, library import) and a one-click `.mcpb`. 🟢 **It ships a FERPA mode** — the first time compliance appears as a *product feature* on these shelves rather than a caveat in this base's prose. `canvas-lms-mcp` **v2.9.0 across 87 releases, 2026-04-13 → 2026-10-22 (today)**: the most actively published LMS integration here. |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) · [`-server`](https://github.com/Fireiscoolsolo/canvas-lms-mcp-server) | `main` · `c7e5725` / `8e424f1` | 🟢 **MIT** (1,091 B, both) | The **student-side** Canvas surface, 209 tools, shipped as a deliberate pair: **Local Edition** (stdio, *no port opened, nothing exposed*) and **Remote Edition** (ngrok, OAuth 2.1, multi-computer failover). Distinctive part is grade *intelligence* rather than grade retrieval: `what_if_grade`, `compute_needed_score`, `grade_impact_ranking`, `study_priority_ranking`, `semester_snapshot`, plus full `.imscc` export. 🔴 Remote Edition opens a **public HTTPS address** — a school's decision, never a default. |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` · `971d58f` | 🟢 **MIT** (1,067 B) | 🟢 **The first SIS-side integration on this shelf, and it opens the parent/guardian persona.** 20 tools over **Campus Parent** — schedule, assignments, grades, attendance *events with codes*, behavior, food service, documents, standardized assessment scores, fees, messaging from three sources — with linked districts auto-discovered via **CUPS SSO** and `FeatureDisabled`-awareness so it degrades per district. **47 releases**, → 2026-10-19. 🔵 Every SIS on this shelf until now was a *platform to deploy* (openSIS, i-educar); this is a *surface to read*. |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` · `428b78b` | 🟢 **MIT** (1,067 B) | The parent-observer scope over Canvas: 18 tools, `canvas_list_observees` as the hinge. 🟢 Download path is hardened in a way worth copying — host-pinned to the Canvas origin, confined to a download directory, never writes through a symlink, new files `0600`. **43 releases**, → 2026-10-16. |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` · `139bb11` | 🟢 **BSD-3-Clause** (1,532 B) | 🟢 **The live replacement for this shelf's most-depended-on stale artefact.** `Pattern B` rested on `pybryt`, last published **2022-04-28**. This is maintained (**v0.3.2, 7 releases, → 2026-09-25**) and from **QuantStack**, a known Jupyter-ecosystem maintainer. Per-cell **Explain Code** sends source, kernel language, **the traceback**, and preceding cells as the exercise statement; the tutor persona lives in a **`TUTOR.md` found by walking up from the notebook**, so it is per-course and version-controlled; `reference_solution` and `evaluation_criteria` ride in cell metadata, **ROT13-encoded** to keep them from the student. |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` · `687c55b` | 🟢 **MIT** (1,070 B) | 🟢 **The North American curriculum-data layer** — the third region to acquire one. 12 tools over the whole **BC Ministry of Education K–12 curriculum** in its real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search, and the **First Peoples Principles of Learning**. Hosted HTTP *or* local stdio. 🟡 2 releases, both **2026-03-27**, and the data is a crawl of `curriculum.gov.bc.ca` — **currency is the risk here, not the licence**. |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` · `3c680e0` | 🟢 **MIT** (1,070 B) | 🟢 **The EMEA institution-shaped integration, and the governance reference on this shelf.** One server spanning **Brightspace + OSIRIS (official records) + MyTimetable + the public Study Guide** behind a single browser sign-in **including MFA**, session self-renewing. 🟢 **Every write action shows a preview and requires confirmation** — the human-oversight control EU high-risk obligations ask for, implemented as the default rather than documented as advice. |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` · `ac0c75f` | 🟢 **MIT** (1,063 B) | Teacher-facing **semester refresh**: reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, emits Canvas-safe HTML. 🟢 The **no-token path is first-class** — generate the HTML, paste it in — so it delivers before anyone grants API access, which is how a pilot actually begins. |
| [gafapa/moodlia-cli](https://github.com/gafapa/moodlia-cli) | `main` · `7962e49` | 🟡 **GPL-3.0** (284 B short notice) | Node client and CLI for Moodle Core web services **plus the MoodlIA plugin — a 250-operation contract**, Moodle 4.5+, with an optional experimental **WebMCP** browser path. 🔵 A far wider surface than `webservice_mcp`, and GPL is survivable the same way: reached over REST/JSON-RPC, never linked. |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` · `a333415` | 🟢 **MIT** (1,094 B) | 🔵 **Not a teaching tool — a build-cost tool, which is why it is on a foundations shelf.** RAG over a **Moodle codebase** for developers: semantic code search, 7 agents, 9 slash commands, all local. `Pattern A`'s real cost is Moodle plugin work; this is aimed at exactly that. 🟡 v1.0.0, single publish 2025-10-12. |

🔵 **How to read this tier against Tier 1–6.** Those tiers are **systems to deploy**; this one is
**surfaces to read and write**. A studio picks one platform base from Tier 1 and then one integration
row here *per persona* — and the personas are no longer two. Teacher/admin (`bruchris`), student
(`Fireiscoolsolo`), parent/guardian (`chrischall`) are three distinct tool surfaces over the *same*
institutional data, and **the tool counts are scope, not quality**: 187 vs 209 vs 20 reflects who is
being served, not which is better built.

🔴 **The maintenance rule this tier is sorted by, stated so it survives the next pass.** `p387`
established that **recency replaces popularity** here, because no star channel is open. `p388` adds
the corollary: **where two integrations cover the same surface, prefer the one still publishing** —
`canvas-mcp-server` (54 tools, last shipped 2025-06-27) is now dominated on both axes by a 187-tool
server that published today. Tool count and maintenance pointed in opposite directions for one pass;
they no longer do.

🔴 **And a supply category this shelf could not previously name: published-but-unreadable.** Six
addresses from the same sweep **publish to npm from a repository that prompts for credentials** —
the dependency is installable, its provenance is not auditable. The costliest is
[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit) (**103
published versions**, manifest MIT, SCORM support), and the most instructive is
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit), whose manifest reads
**`"SEE LICENSE IN LICENSE"`** — pointing at a file in a repository nobody can read. 🔵 `Pattern L`
clears a repository by reading its subtree; **there is no subtree here to read**, so these cannot be
cleared that way. For an npm-only dependency the rule is: **the manifest is a claim, the tarball is
the evidence** — and `registry.npmjs.org/<pkg>/-/<pkg>-<v>.tgz` serves that tarball even when the
repository is closed. Full table and the Santillana case in
[`agents/top.md`](../agents/top.md#-no-licence-file--and-ungranted-is-three-different-things).

## 🔴 Dead addresses corrected this pass

Four addresses in common circulation do not resolve. Each has a live replacement:

| dead address | live replacement |
|---|---|
| `apereo/opencast` | [opencast/opencast](https://github.com/opencast/opencast) |
| `edx/openassessment` **and** `openedx/openassessment` | [openedx/edx-ora2](https://github.com/openedx/edx-ora2) |
| `OpenEduCat/OpenEduCat` | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) |

## 🔴 `p384` — an address that resolves but has no tree

[`projectfedena/fedena`](https://github.com/projectfedena/fedena) is listed by a vendor comparison
article as an **Apache-2.0** student information system. It is neither confirmed nor refutable from
a resolution check alone, which is the point:

| check | result |
|---|---|
| `git ls-remote --heads` | 🟢 **resolves** — two refs: `master`, `projectfedena-patch-1` |
| `master/README`, `README.md`, `LICENSE`, `Gemfile`, `app` | 🔴 **404, all five** |

🔵 **`ls-remote` proves a ref, not a tree.** The base's verification method pairs resolution with a
first-hand payload read precisely so this case is caught: there is no readable tree here to carry a
licence, so the Apache-2.0 claim is recorded as **unsubstantiated — nothing read**, not as a
licence of any kind. Any address census built on resolution alone over-counts the supply.

**Still absent from the supply, and it did not change this pass:** no platform is both an **LMS and
a SIS** under a permissive licence. The shape is permissive *courseware*
([`inducer/relate`](https://github.com/inducer/relate),
[`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors)), one permissive *major LMS*
([OpenOLAT](https://github.com/OpenOLAT/OpenOLAT), Apache-2.0), and copyleft everywhere else —
Moodle GPL-3, Open edX AGPL-3, Canvas CE AGPL-3, openSIS GPL-2.0, OpenEduCat LGPL-3. **Pairing two
bases is the only route**; the single permissive LMS+SIS does not exist to be found, and a pitch
that assumes it will be found is a pitch with a hole in it.

🆕 `p386` **— the claim survives a search aimed straight at it, and gains a third route.** The
prescribed ERP/CRM leg (`open source platform education ERP CRM MIT Apache 2026`) returned **no
permissive education platform**, which is this shelf's claim holding up under test rather than for
want of looking. What it did return is three **permissive general ERP/CRM bases**, licence payloads
read first-hand: [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (🟢 **MIT**, 1,077 B,
default ref **`master`**, Laravel 13 + FilamentPHP 5 **with a plugin system**),
[krayin/laravel-crm](https://github.com/krayin/laravel-crm) (🟢 **MIT**, 1,078 B, default ref
**`2.2`**) and [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) (🟢 **Apache-2.0**,
11,906 B, default ref **`trunk`**). 🔵 So the pairing routes are now three, not two: copyleft
LMS + copyleft SIS, copyleft LMS + permissive courseware, or **copyleft LMS + a permissive ERP base
whose education modules you build**. The trade is written out on
[`verticals/solutions.md`](../verticals/solutions.md) — and none of the three bases ships an
education module, so the third route is a **build**, costed as one.
