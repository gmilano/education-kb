---
industry: education
region: Global
updated: 2026-11-17
---

# Top AI agents — education

**Pass `p872`, 2026-11-17** (second pass of the day; builds on `p871` rather than redoing it).
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

> **No star counts appear in this file.** The star channel (`api.github.com`, `github.com`
> HTML) returned `403` for this session, so stars were **not measurable this pass**. Prior
> pass `p870` recorded DeepTutor at `59,922★` from a star-ranked sweep it could run; that
> figure is its measurement, not this pass's, and is not restated here as fact. Writing a
> star count sourced from a blog is how this KB previously recorded inflated numbers.

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

**7 education-native rows.** That is what verified; the table is not padded to a round
number. See the declared gap below on what is missing.

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
| **LibreChat** | https://github.com/danny-avila/LibreChat | MIT | `main` | Multi-model chat front end with per-user auth, agents and RAG. The usual choice when an institution needs a self-hosted, model-agnostic assistant it can put in front of students without sending data to a vendor. |
| **OpenHands** | https://github.com/All-Hands-AI/OpenHands | MIT | `main` | Coding agent. In education: autograding harnesses, scaffold generation for CS courses, and migration work on legacy LMS plugins. |
| **LangGraph** | https://github.com/langchain-ai/langgraph | MIT | `main` | Stateful graph orchestration. The control layer where a pedagogical policy (hint ladders, mastery gates, escalation to a human teacher) is expressed as explicit nodes you can audit. |
| **CrewAI** | https://github.com/crewAIInc/crewAI | MIT | `main` | Role-based multi-agent orchestration — maps cleanly onto teacher / tutor / assessor / moderator role splits. |
| **gpt-researcher** | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | `main` | Cited multi-source report generation; used for literature-review scaffolding and course-material drafting. |
| **STORM** | https://github.com/stanford-oval/storm | MIT | `main` | Stanford OVAL. Generates Wikipedia-style grounded articles from scratch with citations — a strong base for curriculum and explainer drafting with a traceable source trail. |

## Licence flags — read before proposing any of these to a client

| Project | Nominal licence | The actual constraint |
|---|---|---|
| **Open WebUI** | "Open WebUI License" | BSD-3-clause text **plus an added clause 4**: altering, removing or replacing Open WebUI branding is prohibited unless the deployment has **≤50 end users in any rolling 30 days**, or you hold written permission or an enterprise licence. Read the bytes: this is *not* plain BSD. A white-labelled campus deployment above 50 users is a material breach. |
| **MinerU** | **"MinerU Open Source License"** — Apache-2.0 + additional terms | **Terms read by `p872`.** A separate **commercial licence** is required above **100M MAU** or **USD 20M monthly revenue** (consolidated with affiliates), plus an **online-service attribution obligation**. Neither threshold binds a normal institutional deployment; the attribution obligation binds any hosted service immediately. This is the KB's one genuine "Apache-2.0 plus terms" case. |
| **MultiAgent-AI-Teaching-Assistant** | **none** | `github.com/YoussefMohAttia/MultiAgent-AI-Teaching-Assistant` exists but has **no licence file on its default branch**. No licence means no grant — Globant cannot build on it. Recorded so no later pass re-imports it from a blog listing. |
| **Frappe LMS** | **AGPL-3.0**, not MIT | Multiple 2026 LMS listicles state Frappe LMS is MIT. The licence bytes at `frappe/lms@develop/license.txt` are **GNU Affero GPL v3**. Corrected this pass. |
| **OpenProctor** | **AGPL-3.0**, not MIT | `github.com/kamlendras/OpenProctor` is listed as MIT in secondary sources. The licence bytes on `main` are **AGPL-3.0**. Corrected `p872`. |
| **os-taxonomy** | **ODbL**, not a code licence | `github.com/withmarbleapp/os-taxonomy` exists, but its `LICENSE` is the **Open Data Commons Open Database Licence** — share-alike on derived *databases*. It is a curriculum dataset, not permissive code. Do not file it beside MIT/Apache repos. |
| **Any Apache-2.0 repo** | *not* "Apache-2.0 + additional terms" | **Method warning.** Apache-2.0 §5 contains the phrase *"without any additional terms or conditions"*, so a substring grep for `additional terms` false-positives on **100%** of Apache-2.0 projects. `p872` hit this on seven repos (DeepTutor, agents-course, ltijs, Ed-Fi-ODS, oppia, OpenOlat, openedx-aspects) and **discarded the flag rather than publishing it**. MinerU remains the one genuine case, because its `LICENSE.md` adds substantive prose terms. Licence characterisation requires reading the bytes, not matching a substring. |

## Declared gaps — searched and not found

An informed gap is information; silence looks identical to coverage. Three of `p871`'s four gaps
moved this pass; what remains is stated as precisely as the evidence allows.

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
  Unchanged. For public-sector bids where Section 508 / EN 301 549 / WCAG conformance gates
  procurement, `CAHLR/OATutor` (MIT) is still the only verified starting point in this file.
- **Star counts unmeasurable for the second consecutive pass** (`403` on both
  `api.github.com` and `github.com` HTML). Not inferred from blogs. No star figure appears
  anywhere in this KB.
- **No LATAM-origin or Africa-origin education-native agent surfaced**, across `p871`'s six legs
  and `p872`'s further legs. `p872` adds a refinement: LATAM's contribution to this stack is a
  **sovereign foundation model, not an education agent** — **Latam-GPT**, CENIA-led, launched
  **10 Feb 2026**, Llama-3.1-70B base, 230B+ words of Spanish/Portuguese including education
  sciences, open weights, hosted under the `latam-gpt` Hugging Face org. Note the limit of its
  openness: **the training corpus is gated** — the research tier requires a request CENIA
  evaluates plus a signed NDA. So "open source" describes the weights, not the data.
  Education-native OSS in this window remains concentrated in East Asian university labs
  (HKUDS/HKU, THU-MAIC/Tsinghua) and US universities (CAHLR/Berkeley).
- **No agent in this file has published learning-outcome evidence for itself.** `p872` found the
  trial literature (see `intel/trends.md` **T9**) and none of it evaluates any repo named here.
  The largest trial — 2,379 undergraduates — found a **negative** effect from course-integrated
  AI tutor access. Treat every efficacy claim in this file as a capability description, not an
  outcome claim.
