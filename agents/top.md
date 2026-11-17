---
industry: education
region: Global
updated: 2026-11-17
---

# Top AI agents — education

**Pass `p876`, 2026-11-17** (sixth pass of the day). **`p876` adds no agent row and corrects
three addresses and one liveness claim.** It ran a ten-leg star-ranked **discovery** sweep —
the first this KB has been able to run, since `p875` only measured addresses it already held —
and the result is worth stating plainly:

> **🔴 A star-ranked discovery sweep across ten education queries returned 126 repositories, 47 of
> them new to this KB, and NOT ONE is an education agent.** They are `awesome-*` lists, curricula,
> prompt collections and, repeatedly, the same anti-propaganda repository that ranks for anything.
> **This is `intel/trends.md` T12 confirmed from the discovery side rather than the measurement
> side:** the reason this file has two large agents and a tail of zeroes is not that the KB has
> been looking in the wrong place. **There is no hidden shelf.** The legs are recorded in
> `repos/trending.md` `p876` so a later pass does not re-buy them.

> **🟡 Three addresses in this file were canonical-stale, and the git protocol hid it.**
> `All-Hands-AI/OpenHands` → **`OpenHands/OpenHands`** (93,647★) and `danny-avila/LibreChat` →
> **`LibreChat-AI/LibreChat`** (47,237★). Both old addresses still answer `git ls-remote` and
> still serve correct licence bytes **via redirect**, so this KB's two-channel verification passed
> on them for passes on end. The detector is the search API's `422`. (`openedx/edx-platform` →
> `openedx/openedx-platform` is the third; it is cited elsewhere in this KB, and the rename was
> already in the trending log — it had simply never been propagated to the curated files.)

**Previous pass note (`p875`)** (fifth pass of the day). **`p875` adds NO row to this file and adds a
column instead** — the first adoption signal this KB has ever carried. After four passes declaring
star counts unmeasurable, the channel was found (`api.github.com/search/repositories`; see
`agents/trending.md` for why `p874` ruled it out). **78 addresses measured first-hand.**

> **The measurement reorders this file, and the finding is uncomfortable.** Two education-native
> agents have real user bases — **DeepTutor (59,972)** and **OpenMAIC (43,808)**. **Every other
> education-native agent listed below has fewer than 20 stars, and four have ZERO.** This file has
> been presenting a 60,000-star platform and a 0-star single-author repository in the same table,
> distinguished only by a maturity flag in prose. **The Adoption column makes that distinction
> unskippable.** Stars measure attention, not quality — but a 0-star repo has no community, no
> issue history and no evidence of a deployment, and that is a support-burden fact a client must
> hear before a statement of work is signed.

`p875` resolved four new addresses and promoted none: `withmarbleapp/os-taxonomy` (7,720 stars) is
**ODbL-1.0**, a share-alike *database* licence and not a software licence;
`patchy631/ai-engineering-hub` (41,955, MIT) is teaching material *about* AI, not an education
agent; `BlackyDrum/ai-tutor` (8, MIT) is the only MIT tutor found that speaks LTI and it is
**LTI 1.0, last pushed 2024**; `kevinnio/tutor` (15, MIT) is an agent skill with no LMS seam.
Reasons against each are in `agents/trending.md`.

> **🟢 OpenMAIC's licence is SETTLED — stop re-litigating it.** Three passes have re-checked it
> against sources that disagree. `p875` found the cause: the project **relicensed to MIT on
> 2026-06-28** (its own README changelog, `v0.3.0`), so every pre-July source — **including the
> project's own site `openmaic.io`, which still says AGPL-3.0** — describes a dead licence. A
> second mechanism compounds it: `kolbyzhu5/OpenMAIC`, a pre-relicence **AGPL-3.0 fork**, sits in
> the search index. Four channels now agree on **MIT**: licence bytes, no other licence file on
> the branch, the README badge and text, and SPDX detection.

> **🔴 Deployment hazard in OpenMAIC, from its own README.** Site-wide access is gated by a single
> `ACCESS_CODE` variable, and **unset is the default in `.env.example`**: `middleware.ts` then
> checks no credential and *"every route, the API included, is reachable… there is no second
> enforcement point."* A default OpenMAIC deployment in a school tenancy is a student-data
> exposure on day one. Any pattern shipping it must budget `ACCESS_CODE` provisioning and a second
> enforcement point — see `compose/patterns.md` **P12**.

**Previous pass note (`p874`):** resolved 10 addresses and added no row — 4 had no licence file, 1
reserved all rights, 3 were shelved, 1 was Gemini-API-dependent, 1 was not education. It
re-confirmed OpenMAIC against two sources that disagreed; `p875` has now explained why they did.

**Previous pass note (`p873`):** targeted `p872`'s declared gaps rather than re-verifying its
seventy addresses.
Every row below was verified by two channels:
existence via `git ls-remote https://github.com/<slug>` (an HTTP 200 on the git smart
protocol), and licence via the actual licence bytes fetched from
`raw.githubusercontent.com/<slug>/<resolved-default-branch>/<licence-file>`. The default
branch was resolved with `git ls-remote --symref ... HEAD` rather than assumed to be `main`
— four of the repos below do **not** use `main`, so a guessed path would have 404'd.

### Verification channels this run

| Channel | Result |
|---|---|
| `git ls-remote` (existence, default branch) | **open** — used for all rows |
| `raw.githubusercontent.com` (licence bytes) | **open** — used for all rows |
| `github.com` HTML | **403** — blocked, session GitHub scope |
| `api.github.com` | **403** — blocked, session GitHub scope |
| `gh` CLI (`gh api repos/...`) | **403** — git proxy: *"not in this session's authorized repository set"* (added by `p873`) |
| `gh api search/repositories` | **empty result set** — no star-ranked discovery (added by `p873`) |

> **No star counts appear in this file.** The star channel returned `403` across **four distinct
> routes** — `api.github.com`, `github.com` HTML, the `gh` CLI and the GitHub search API — for a
> **third consecutive pass**, so stars were **not measurable this pass** either. Prior
> pass `p870` recorded DeepTutor at `59,922★` from a star-ranked sweep it could run; that
> figure is its measurement, not this pass's, and is not restated here as fact. Writing a
> star count sourced from a blog is how this KB previously recorded inflated numbers.

## Measured adoption — new in `p875`

Read this before the tables below. Measured `2026-11-17` via `api.github.com/search/repositories`.
🔴 marks no push since 2026-06-01.

| Agent | Stars | Licence (SPDX) | Last push | Read |
|---|---:|---|---|---|
| **HKUDS/DeepTutor** | **59,972** | Apache-2.0 | 2026-11-15 | Real platform, real community. Safe to propose. |
| **THU-MAIC/OpenMAIC** | **43,808** | MIT ✅ | 2026-11-17 | Real platform, real community. Ship with the `ACCESS_CODE` hardening task. |
| CaviraOSS/PageLM | 2,069 | `NOASSERTION` 🔴 | 2026-11-15 | Users exist; **licence does not auto-detect — re-read the bytes before naming it in a proposal.** |
| CAHLR/OATutor | 282 | MIT | 2026-11-17 | Small but alive, peer-reviewed, accessibility-conformant. The credible academic option. |
| AI-for-Education/pedagogy-benchmark | 13 | MIT | 2026-11-16 → 🔴 **HEAD `2025-10-15`** | An eval harness, not a tutor — low stars are expected and not disqualifying. 🔴 **`p876` liveness correction: the `2026-11-16` push did not touch the default branch, whose last commit is `2025-10-15` — 398 days, `0` commits in 12 months.** It is still the right instrument to cite to a ministry (1,143 questions from real teacher-qualification exams); it is a **frozen** one. Say so in the proposal rather than implying an active leaderboard. |
| wwrwbs/AI_AWE (ArguLens) | **2** | `NOASSERTION` 🔴 | 2026-07-29 | 🔴 **Two stars and no detectable licence.** Treat as a paper artifact, not a base. |
| PritK99/WriteRight | **1** | MIT | 2024-11-19 🔴 | Reference implementation only, as this file already said. Confirmed. |
| littlecookie0722/AI-Teaching-Agent | **0** | MIT | 2026-08-23 | No community. Bespoke-from-zero risk profile. |
| vulinh1704/ai-tutor-agent | **0** | MIT | 2026-11-16 | A starter template, as flagged. Confirmed by adoption. |
| LabSirius/TutorIA | **0** | MIT | 2026-10-27 | 🟡 **Zero stars, and this one is not a weekend project** — it is a funded Colombian university deliverable. The maturity caveat below (docs-only `main`) is the operative fact; the star count corroborates that nobody outside the lab has used it. |

🟡 **How to use this column.** It separates *support burden* from *engineering quality*. A 0-star
repo may be excellent code; it will still have no external contributors, no issue history and
nobody to escalate to. Price that into the engagement or choose a different base.

## Education-native agents

These are built for teaching and learning as their primary purpose.

| Agent | Repo | Licence | Default branch | What it does |
|---|---|---|---|---|
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | `main` | Self-hosted lifelong tutoring agent from HKUDS (HKU Data Science lab). Grounds tutoring in the learner's own documents via LightRAG retrieval, tracks skill mastery, generates learning paths, narrated video lessons and question-bank practice. Ships a CLI "agent-native interface", desktop builds, Anki and calendar export, Kiwix offline-archive ingest, and an `EduHub` skills community. Release `v1.7.3` dated 2026-11-16 — weekly cadence. |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | `main` | Multi-agent classroom from Tsinghua's MAIC lab. Generates a complete course — AI teacher plus AI classmate agents — from a topic or an uploaded document, with project-based learning (PBL v3), a foldered knowledge base with `@`-mention, course-level undo, and export to PPTX and HTML. Release `v1.5.0-rc.3` dated **2026-11-17** (today). Server-first: generation survives a closed tab. |
| **PageLM** | https://github.com/CaviraOSS/PageLM | MIT | `main` | NotebookLM-style study platform: turns uploaded study material into quizzes, flashcards, notes and exam prep. Self-hostable. Smaller maintainer base than the two above — the README is actively recruiting volunteers. |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | `main` | Open adaptive tutoring system from UC Berkeley's CAHLR. Intelligent-Tutoring-System design using **Bayesian Knowledge Tracing** for mastery estimation; React, deployable to static pages with no backend; LTI middleware for LMS integration. **Section 508 / WCAG compliant** — the only row here with a published accessibility conformance document. Peer-reviewed (CHI '23, doi:10.1145/3544548.3581574). |
| **Pedagogy Benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | MIT | `main` | Not a tutor — the **evaluation harness for tutors**. 1,143 questions drawn from real teacher-qualification exams, split into CDPK (920, cross-domain pedagogical knowledge) and SEND (223, special educational needs and disabilities). Runs 100+ models, public leaderboards, paper arXiv:2506.18710. This is how you defend a tutoring claim to a ministry or a university procurement board. |
| **AI Teaching Agent** | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | `main` | Instructor-side rather than learner-side: generates labs, exams, grading workflows and presentations with structured DSLs, human review, sandboxed evaluation, and CLI/MCP tools, local-first. **Maturity flag:** its own README states automatic-grading productisation is frozen, so treat grading as incomplete. |
| **ai-tutor-agent** | https://github.com/vulinh1704/ai-tutor-agent | MIT | `main` | FastAPI + LangGraph starter for tutoring agents: Socratic hinting, rubric-based grading with structured output, session memory, offline demo mode. **Maturity flag: a starter template, not a product** — useful as a skeleton for a bespoke engagement, not as a platform. |
| **TutorIA** | https://github.com/LabSirius/TutorIA | MIT | `main` | **New in `p873` — the first verified LATAM-origin education-native agent in this KB.** Autonomous tutor for **rural higher education in Risaralda, Colombia**, from Grupo Sirius at Universidad Tecnológica de Pereira; built to run inside **Open edX**. v2 backend: **Ollama-default inference via the OpenAI-compatible interface** (`llama3.2`), **pgvector + `nomic-embed-text` RAG**, an Open edX→PostgreSQL sync gateway on APScheduler, and pedagogical prompt templates held in the database. Tag `informe-minciencias-2026-09` — a funded deliverable reported to Colombia's science ministry. **Maturity flag, and it is the operative fact: `main` contains documentation only. The code is on `feature/refactor-to-v2-requirements`, it is backend-only, and the React frontend, Open edX plugin and test suite its README describes do not exist in any branch.** See below. |

**8 education-native rows.** That is what verified; the table is not padded to a round
number. See the declared gap below on what is missing.

### TutorIA — why it is listed, and exactly what you get if you clone it

It is listed because it answers a question this KB had been answering with an absence: *is anyone
in LATAM building an education-native agent, or does the region only deploy other people's?* A
Colombian public university shipping an **MIT-licensed** tutoring agent aimed at **rural,
low-connectivity higher education**, with a **named pedagogical director** and a reporting
obligation to a national science ministry, is the counter-example. For a Spanish-language
engagement its pedagogical framing, language and deployment context already match the brief —
which is worth more than maturity at the proposal stage.

It carries a flag because **a clone of its default branch ships nothing runnable**:

| Address | Branch | Contents |
|---|---|---|
| `LabSirius/TutorIA` | **`main` (default)** | `README.md`, `CONTRIBUTING.md`, `LICENSE`, `docs/`. `backend/`, `frontend/`, `docker-compose.yml`, `.env.example` **all 404** |
| `LabSirius/TutorIA` | `feature/refactor-to-v2-requirements` | **The v2 backend** — `backend/app/{main,config}.py`, `routers/chat.py`, `services/rag_service.py`, `gateways/openedx_gateway/sync_service.py`, `requirements.txt`, `docker-compose.yml` |
| `Sof1SP/tutorIA` (**the address its own README's `git clone` line points at**) | `main`, `dev` | **No code in either** — `README.md` + `LICENSE` only. Also MIT |

Also note: **the README is behind the code.** It describes Anthropic Claude API + Microsoft Azure;
`backend/app/config.py` defaults to **local Ollama** with Claude retained only as an optional
fallback, and the startup log states *"provider routing active; default: ollama"*. The default
inference path is **local and sovereign** — no learner text leaves the institution unless someone
configures it to. Requirement IDs (**RF-21** prompt templates, **RF-22** Open edX sync, **RF-23**
provider routing) are traceable to the project's requirements document, which is the kind of
engineering a ministry audit can follow, and the code carries honest `TODO(tech-debt)` comments
about its own Alembic migration debt.

**Treat it as a collaboration target and a regional reference, not as a base to promise a delivery
date on.** The highest-value contribution Globant could make to it is small and obvious: the
frontend, the Open edX plugin and the test suite that its README already specifies.

## Grading & assessment agents

`p871` recorded this category as empty. It is not — `p872` found and verified one real
permissive system. The table is one row long because one row verified.

| Agent | Repo | Licence | Default branch | What it does |
|---|---|---|---|---|
| **ArguLens** | https://github.com/wwrwbs/AI_AWE | Apache-2.0 | `main` | Automated essay scoring **with label-aware feedback** for argumentative essays. Scores 1–6, labels every sentence as `claim`/`data`/`counterclaim`/`rebuttal`, and generates written feedback. Three decoupled parts: a fine-tuned **Qwen2.5-7B LoRA** discourse classifier (`infer/infer_qwen.py`), a **grade-independent LightGBM scorer over 31 linguistic/discourse features** (`scoring_pipeline/scorer.py`) — not an LLM — and a feedback generator on local Qwen2.5-14B-Instruct via vLLM (`feedback/`). Gradio UI with batch upload and JSON/CSV/Markdown export; `hf`/`vllm`/`api` backends; `pytest` suite. Paper arXiv:2608.17356 (18 Aug 2026). |
| **WriteRight** | https://github.com/PritK99/WriteRight | MIT | `main` | Minimal MIT essay scorer (1–10 across several criteria). Lightly maintained — a reference implementation to read, not a base to build on. |

**Why ArguLens is worth the attention and the dozen other "AES" repos are not.** The score comes
from a **feature-based LightGBM model, not a language model**. That makes it inspectable,
reproducible, and defensible on appeal — which is precisely what every automated-decision regime
demands: Brazil's LGPD right to review of automated decisions, the EU AI Act high-risk tier for
assessment, and Vietnam's Decision 33/2026/QD-TTg. "The model said 4" cannot be defended to an
appeals board; "these 31 measured features produced 4, and here is the same result on re-run" can.

**Maturity flags — read before proposing it.**

- **v0.1.0 and early.** Adapter weights ship as a separate GitHub release asset, and the README
  states adapter weights must be published before public release.
- **README scopes it to "research and assistive" use** and says high-stakes decisions require
  human oversight. Honour that: wire it behind a human override, never as the deciding step.
- **Corpus is Persuade 2.0** — US middle-school argumentative essays, academic-use with
  attribution, not redistributed (prepared locally via `prepare_persuade.py`). The README's own
  bias and generalisation warning applies to any other learner population, and **doubly to any
  non-English deployment**: nothing in this system has been shown to transfer to Spanish or
  Portuguese, which is exactly the LATAM engagement case. Re-fitting the scorer on local graded
  essays is a required work item, not an optional refinement.
- **Dependency chain is clean:** code/adapter-config/scorer Apache-2.0; vendored
  `TextComplexityToolkit` MIT (wraps TAALED, QuanSyn, L2SCA/neosca, spaCy); Qwen2.5 base
  Apache-2.0; spaCy model MIT/CC. The closed-source TAMMI/TAALES/TAASSC tools are deliberately
  excluded, so there is no proprietary dependency to license.

## General-purpose agents composable into education builds

Education-native projects are thin above the tutoring layer, so most real engagements
compose a general agent framework. These were verified on the same two channels this run.

| Agent / framework | Repo | Licence | Default branch | Education role |
|---|---|---|---|---|
| **LibreChat** | https://github.com/LibreChat-AI/LibreChat | MIT | `main` | Multi-model chat front end with per-user auth, agents and RAG. The usual choice when an institution needs a self-hosted, model-agnostic assistant it can put in front of students without sending data to a vendor. |
| **OpenHands** | https://github.com/OpenHands/OpenHands | MIT | `main` | Coding agent. In education: autograding harnesses, scaffold generation for CS courses, and migration work on legacy LMS plugins. |
| **LangGraph** | https://github.com/langchain-ai/langgraph | MIT | `main` | Stateful graph orchestration. The control layer where a pedagogical policy (hint ladders, mastery gates, escalation to a human teacher) is expressed as explicit nodes you can audit. |
| **CrewAI** | https://github.com/crewAIInc/crewAI | MIT | `main` | Role-based multi-agent orchestration — maps cleanly onto teacher / tutor / assessor / moderator role splits. |
| **gpt-researcher** | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | `main` | Cited multi-source report generation; used for literature-review scaffolding and course-material drafting. |
| **STORM** | https://github.com/stanford-oval/storm | MIT | `main` | Stanford OVAL. Generates Wikipedia-style grounded articles from scratch with citations — a strong base for curriculum and explainer drafting with a traceable source trail. |

🟡 **`p876` corrected two addresses in the table above.** LibreChat is now
`LibreChat-AI/LibreChat` (**47,237★**, MIT, pushed 2026-11-17) and OpenHands is now
`OpenHands/OpenHands` (**93,647★**, MIT, pushed 2026-11-17). The previous addresses
(`danny-avila/`, `All-Hands-AI/`) are redirects: they clone, they serve licence bytes, and
`api.github.com/search/repositories?q=repo:<old>` returns **`422 Validation Failed`** — which is
the only signal this KB has that a slug has stopped being canonical. 🔵 **A verification method
built on bytes alone is structurally blind to a rename.**

## Licence flags — read before proposing any of these to a client

| Project | Nominal licence | The actual constraint |
|---|---|---|
| **Open WebUI** | "Open WebUI License" | BSD-3-clause text **plus an added clause 4**: altering, removing or replacing Open WebUI branding is prohibited unless the deployment has **≤50 end users in any rolling 30 days**, or you hold written permission or an enterprise licence. Read the bytes: this is *not* plain BSD. A white-labelled campus deployment above 50 users is a material breach. |
| **MinerU** | **"MinerU Open Source License"** — Apache-2.0 + additional terms | **Terms read by `p872`.** A separate **commercial licence** is required above **100M MAU** or **USD 20M monthly revenue** (consolidated with affiliates), plus an **online-service attribution obligation**. Neither threshold binds a normal institutional deployment; the attribution obligation binds any hosted service immediately. This is the KB's one genuine "Apache-2.0 plus terms" case. |
| **MultiAgent-AI-Teaching-Assistant** | **none** | `github.com/YoussefMohAttia/MultiAgent-AI-Teaching-Assistant` exists but has **no licence file on its default branch**. No licence means no grant — Globant cannot build on it. Recorded so no later pass re-imports it from a blog listing. |
| **EduTwin Africa** | **none** | `github.com/muskvdc/EduTwin-Africa` — curriculum-aware tutor with RAG, bounded multi-agent collaboration and guardrails, scoped to **South African Grades 8–12**. Exists on `main`; **no `LICENSE`, `LICENSE.md` or `COPYING`**. Africa-origin and legally unusable as it stands. Found by `p873`. |
| **multiagent-ai-tutor** | **none** | `github.com/giovanayngrid-gk/multiagent-ai-tutor` — Brazilian, Portuguese-language, LangChain + Llama 3 via local Ollama + Streamlit. Exists on `main`; **no licence file**. Found by `p873`. |
| **educational-agents** | **none** | `github.com/nifalconi/educational-agents` — Spanish-language teaching library with LATAM Spanish identifiers, from a *Niñas Pro* agents course. Exists on `main`; **no licence file**. Found by `p873`. |
| **Lenda AI** | **claimed Apache-2.0, unverifiable** | Self-describes as an Apache-2.0 LATAM-built open-source tutor (v0.1). **Not listed in this KB:** `lenda.ai` does not resolve from this session, no independent coverage exists, and `git ls-remote` found nothing at four plausible namespaces. **A licence claim on a project page is not a licence.** |
| **Frappe LMS** | **AGPL-3.0**, not MIT | Multiple 2026 LMS listicles state Frappe LMS is MIT. The licence bytes at `frappe/lms@develop/license.txt` are **GNU Affero GPL v3**. Corrected this pass. |
| **OpenProctor** | **AGPL-3.0**, not MIT | `github.com/kamlendras/OpenProctor` is listed as MIT in secondary sources. The licence bytes on `main` are **AGPL-3.0**. Corrected `p872`. |
| **os-taxonomy** | **ODbL**, not a code licence | `github.com/withmarbleapp/os-taxonomy` exists, but its `LICENSE` is the **Open Data Commons Open Database Licence** — share-alike on derived *databases*. It is a curriculum dataset, not permissive code. Do not file it beside MIT/Apache repos. |
| **Any Apache-2.0 repo** | *not* "Apache-2.0 + additional terms" | **Method warning.** Apache-2.0 §5 contains the phrase *"without any additional terms or conditions"*, so a substring grep for `additional terms` false-positives on **100%** of Apache-2.0 projects. `p872` hit this on seven repos (DeepTutor, agents-course, ltijs, Ed-Fi-ODS, oppia, OpenOlat, openedx-aspects) and **discarded the flag rather than publishing it**. MinerU remains the one genuine case, because its `LICENSE.md` adds substantive prose terms. Licence characterisation requires reading the bytes, not matching a substring. |

## Declared gaps — searched and not found

An informed gap is information; silence looks identical to coverage. `p873` moved the two
regional-origin gaps that had stood longest; what remains is stated as precisely as the evidence
allows.

- ~~**No mature open-source grading / assessment agent exists.**~~ **CLOSED by `p872`.**
  **ArguLens** (`wwrwbs/AI_AWE`, Apache-2.0, arXiv:2608.17356) is real, verified, decomposed and
  permissive. It is **v0.1.0 and research-grade**, and its corpus is US middle-school English —
  so the honest statement is now *"a permissive grading system exists and needs hardening and
  re-fitting"*, not *"nothing exists"*. `edx-ora2` (AGPL-3.0) remains the production substrate
  for the human-workflow half; ArguLens is the scoring half. **Still an open build opportunity
  for Globant — but now as hardening a real base, which is a far cheaper proposal than greenfield.**
- **No permissively licensed open-source proctoring platform exists — now evidenced, not assumed.**
  `p872` verified two real candidates and **both are AGPL-3.0**: `sudosylabs/proctor` (Go+React,
  the most complete) and `kamlendras/OpenProctor`. Copyleft is workable for a single
  institution's self-hosted deployment and unusable in a distributed product. Given that the EU
  has moved proctoring into the high-risk tier and Vietnam now lists biometric learner monitoring
  as a high-risk education system, the strategic answer is more likely **assessment redesign than
  better proctoring**.
- **No education-native agent carries an accessibility conformance statement except OATutor.**
  Still true after a dedicated `p873` search leg, but the gap now has an **architectural answer**
  rather than just a single fallback. `CAHLR/OATutor` (MIT) remains the only agent in this file
  with a published conformance document. What `p873` adds is that the **platform** layer has
  conformance even where the agent layer does not: **Moodle core and its mobile app are stated to
  be WCAG 2.2 AA certified** (vendor claim, Open LMS — unverifiable from this session, so treat as
  a claim to request the VPAT/ACR for, not as a fact). The consequence for a bid is concrete:
  **put the agent behind a conformant platform's UI over LTI 1.3 rather than shipping your own
  front end**, and the conformance story rides on the platform. Note also that the obligation is
  tightening — the **European Accessibility Act has applied since 28 June 2025**, and the next
  **EN 301 549** revision aligning it to WCAG 2.2 AA is reported as due in the Official Journal in
  late 2026 (secondary-sourced; all EU primary sources are unreachable from this session). And the
  standard failure mode is not the platform at all: an accessible platform routinely serves
  inaccessible embedded content — the SCORM package, the PDF workbook, the generated slide deck.
  **An AI content generator is a content generator: whatever it emits inherits the conformance
  obligation.** See `compose/patterns.md` **P10**.
- **Star counts unmeasurable for the third consecutive pass, now across four routes** —
  `api.github.com`, `github.com` HTML, the `gh` CLI (*"not in this session's authorized repository
  set"*) and `gh api search/repositories` (empty set). This is a session scope, not a GitHub
  outage. Not inferred from blogs: secondary sources this pass offered ~48.9k, ~54k and ~59.9k for
  the same project within three weeks, which is exactly why none of them is recorded. No star
  figure appears anywhere in this KB.
- **Every non-GitHub host is unreachable from this session**, on both `curl` (`000`) and `WebFetch`
  (`ENOTFOUND`): `arxiv.org`, `aclanthology.org`, `doi.org`, `sciencedirect.com`, `unesco.org`,
  `eur-lex.europa.eu`, `data.consilium.europa.eu`, `europarl.europa.eu`, `edworkingpapers.com`,
  `multistate.us`, `ipsos.com`, `lenda.ai`. So **repository facts and document facts in this KB
  sit on different evidential footings**: repos are read first-hand (existence, branch, tags,
  licence bytes, source files), while every paper, survey and regulatory date is a search engine's
  summary of a page that cannot be opened. Flagged wherever it matters. These hosts would need
  allowing in the session's network settings.
- ~~**No LATAM-origin education-native agent surfaced.**~~ **CLOSED by `p873`.** **TutorIA**
  (`LabSirius/TutorIA`, **MIT**, Universidad Tecnológica de Pereira, Colombia) is verified, listed
  above, and publicly funded. `p872`'s refinement — *"LATAM's contribution is a sovereign
  foundation model, not an education agent"* — **is retired as wrong.** Both are true at once, and
  they stack: **Latam-GPT** (CENIA-led, launched **10 Feb 2026**, Llama-3.1-70B base, 230B+ words
  of Spanish/Portuguese including education sciences, open weights under the `latam-gpt` Hugging
  Face org, **corpus gated behind a CENIA-evaluated request and an NDA** — so "open source"
  describes the weights, not the data) is the model layer, and TutorIA is an agent layer that
  already defaults to a locally served model. The residual gap is **maturity, not existence**:
  TutorIA is a backend in progress, so LATAM-origin OSS is real but not yet production-grade.
- **Africa-origin education agents exist, and not one of them has a licence.** `p873` resolved
  three Global-South tutors with **no licence file on their default branch** — `muskvdc/EduTwin-Africa`
  (South African Grades 8–12), `giovanayngrid-gk/multiagent-ai-tutor` (Brazil, Portuguese) and
  `nifalconi/educational-agents` (LATAM Spanish). No licence means no grant, so all three are
  legally unusable however good the code is. **The discriminating variable appears to be funding:**
  the one regional project that *is* licensed, documented and branch-managed (TutorIA) is the one
  with a national science ministry behind it. Two further Africa-origin research systems —
  **EduNaija AI Tutor** (AfricaNLP 2026; Nigerian curriculum; English/Yoruba/Hausa/Igbo) and
  **AFRILANGTUTOR** (Findings of EMNLP 2026, arXiv:2604.20996) — claim open releases but **no
  repository address could be resolved** and `aclanthology.org`/`arxiv.org` are unreachable from
  this session. Recorded as leads; **no address has been invented.** Next pass: try Hugging Face.
- **Education-native OSS origin is still concentrated** in East Asian university labs (HKUDS/HKU,
  THU-MAIC/Tsinghua) and US universities (CAHLR/Berkeley). TutorIA widens the map; it does not
  change the centre of gravity.
- **No agent in this file has published learning-outcome evidence for itself.** `p872` found the
  trial literature (see `intel/trends.md` **T9**) and none of it evaluates any repo named here.
  The largest trial — 2,379 undergraduates — found a **negative** effect from course-integrated
  AI tutor access. Treat every efficacy claim in this file as a capability description, not an
  outcome claim.
