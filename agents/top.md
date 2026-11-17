---
industry: education
region: Global
updated: 2026-11-17
---

# Top AI agents — education

**Pass `p871`, 2026-11-17.** Every row below was verified this run by two channels:
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
| **MinerU** | Apache-2.0 **+ additional terms** | `LICENSE.md` states Apache-2.0 "subject to the additional terms below". Do not treat as clean Apache-2.0 without reading those terms. |
| **MultiAgent-AI-Teaching-Assistant** | **none** | `github.com/YoussefMohAttia/MultiAgent-AI-Teaching-Assistant` exists but has **no licence file on its default branch**. No licence means no grant — Globant cannot build on it. Recorded so no later pass re-imports it from a blog listing. |
| **Frappe LMS** | **AGPL-3.0**, not MIT | Multiple 2026 LMS listicles state Frappe LMS is MIT. The licence bytes at `frappe/lms@develop/license.txt` are **GNU Affero GPL v3**. Corrected this pass. |

## Declared gaps — searched and not found

An informed gap is information; silence looks identical to coverage.

- **No mature open-source grading / assessment agent exists.** Searched
  `open source AI tutor grading teaching assistant agent github 2026 self-hosted`. Everything
  returned in the grading category was either a starter template (`ai-tutor-agent`), had
  grading explicitly frozen (`AI-Teaching-Agent`), or was an unlicensed student project
  (`MultiAgent-AI-Teaching-Assistant`). For production grading, the realistic path today is
  `edx/edx-ora2` (AGPL-3.0, open-response assessment, battle-tested) wired to a model via
  LiteLLM — not an off-the-shelf agent. **This is an open build opportunity for Globant.**
- **No education-native agent carries an accessibility conformance statement except OATutor.**
  For public-sector education bids where Section 508 / EN 301 549 / WCAG conformance is a
  gating requirement, OATutor is the only verified starting point in this file.
- **Star counts unmeasurable this pass** (`403` on both star channels). Not inferred from blogs.
- **No LATAM-origin or Africa-origin education agent surfaced** in any of this run's six search
  legs. Education-native OSS in this window is concentrated in East Asian university labs
  (HKUDS/HKU, THU-MAIC/Tsinghua), US universities (CAHLR/Berkeley), and small independent
  teams. Recorded as a real absence, not as coverage.
