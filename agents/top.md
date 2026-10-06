---
industry: education
region: Global
updated: 2026-10-06
---

# AI Agents — Education

Open source AI agents and agent-adjacent tooling for education. Focus on MIT /
Apache-2.0 / BSD, the licenses Globant can build on and redistribute to clients.

**Verification method (2026-10-06):** every license below was read from the
repository's own `LICENSE` payload via `raw.githubusercontent.com`, not from a
listing sidebar, a badge, or a blog post. Star counts and descriptions were read
from the repository page the same day. `api.github.com` is not reachable from
this environment (403, session-scoped), so star counts come from the rendered
page; where a count was not read this pass, the cell says so rather than
carrying a stale or inferred number.

## Agents and tools

**40 rows, all verified.** The 12 recorded in the morning pass of 2026-10-06, 2
added in the second pass, **17 added in the third pass** from the `ai-tutor`
GitHub topic page and a stars-sorted repository search, and **5 added in the
fourth pass** by tracing academic papers to their repositories and sweeping a
GitHub organisation, and **4 added in the fifth pass** by searching on funding
body, ministry and university name in English and Spanish instead of by topic or
star count — five distinct channels, each new to this KB when it was used. One of the 17, OpenTutor, is a **reinstatement** of an entry this KB wrongly
withdrew earlier the same day; see the corrections section. The fourth pass added
the largest single asset in this KB (**OpenMAIC, MIT, 40.0k★**) and the first
**Africa-placed** repositories it has ever recorded. The fifth pass added the first
**India-, LATAM- and ASEAN-placed** permissive projects — and found all three at
**0–9★**, which is the finding, not a footnote.

The third-pass rows sit in their own table below the core shelf, because most of
them are **Agent Skills rather than applications** and that distinction decides how
you deliver them.

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (`LICENSE`) | 40.8k | Agent-native lifelong tutoring. Two-layer plugin model (single-shot Tools + multi-stage Capabilities), exposed via CLI, WebSocket API and Python SDK. Per-learner TutorBot workspaces with persistent memory. Latest release v1.6.13 (2026-10-04). Python. |
| AI Agents for Beginners | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 76.5k | 18-lesson course on building AI agents; code samples now target Microsoft Agent Framework. The default enablement asset for client-staff upskilling. |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | 29.7k | Barebones library for agents that think in code. Small surface area makes it the cheapest framework to audit for a high-risk education deployment. |
| Microsoft Agent Framework (MAF) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | 14.0k | Building, orchestrating and deploying agents and multi-agent workflows, Python and .NET. Ships migration guides *from* AutoGen and Semantic Kernel. |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 (`LICENSE`) | 6.8k | Online learning platform for authoring interactive lessons ("explorations") with built-in misconception handling. One of only three permissively licensed full platforms in this KB. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT (`LICENSE`) | 278 (95 forks) | Canvas LMS MCP server: **up to 103 tools** and 8 agent skills for students, educators and learning designers. Includes a 20-check WCAG accessibility scanner and bulk-grading tools. Works with 40+ MCP clients. Latest release v1.13.0 (Sep 2026). The canonical repo — pin it against its forks. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT (`LICENSE`) | 264 | Intelligent tutoring system with Bayesian Knowledge Tracing, from CAHLR at UC Berkeley. Published at CHI '23 with a follow-up in PLOS ONE. ReactJS + Firebase. The auditable mastery model in this list. |
| Educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT (`LICENSE`) | 388 | Python package for generating educational content with generative AI — MCQs, open-ended items, lesson plans, flashcards. |
| Kolibri | [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) | MIT (`LICENSE`) | 1.1k | Offline-first learning platform for teaching and learning without an internet connection. The only fully permissive end-to-end platform here; the basis of the equity-deployment pattern. |
| Moodle MCP Server | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | MIT (`LICENSE`) | not read this pass | MCP server exposing Moodle data to agents from *outside* the Moodle tree — which is why it is MIT while in-tree Moodle plugins are GPL-3.0 (see the license-boundary note below). |
| Hugging Face Agents Course | [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | not read this pass | Open course on building agents with Hugging Face tooling. Pairs with the Microsoft course for a two-track enablement curriculum. |
| learn-agentic-ai | [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | not read this pass | Agentic-AI curriculum used at large scale by the Panaversity / GIAIC programme in Pakistan — a rare APAC-origin education asset in this space. |
| lineage-skill | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | Apache-2.0 (`LICENSE@main`) | 448 | Distils videos, PDFs, transcripts and notes into **source-backed teacher Agent Skills**: keeps source attribution, extracts instructor methodology, orders practice tasks progressively. Python. The highest-starred project on the `education-ai` topic, and the clearest example of Agent Skills used as a distribution format for pedagogy rather than for tooling. |
| Claw-ED | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | MIT (`LICENSE@main`) | 60 | Local-first AI teaching assistant for lesson drafts and classroom materials. Python. Small and early, but local-first + MIT is exactly the shape EMEA data-residency rules and LATAM cost constraints ask for. |

### Added in the third pass of 2026-10-06 — the `ai-tutor` channel

Stars as displayed 2026-10-06; licences read from each repo's own `LICENSE`
payload. Note how many are **skills, not applications**: that is the packaging
shift recorded as trend 12 in `intel/trends.md`, and it is now the majority shape
in this category.

| Project | Repo | Licence (payload) | ★ | Shape | What it does |
|---|---|---|---|---|---|
| StudyMate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT (`LICENSE`) | 624 | app | Chinese-language study partner for maths and CS (linear algebra, calculus, probability, C++, Python, ML, DL) on a "learn with doing" principle. Python; ships a DeepSeek harness and an Antigravity multi-agent plugin. The maintainer's README openly documents a vibe-coded origin and a manual rewrite in progress — read it before adopting. **The highest-starred permissive education agent found outside DeepTutor.** |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT (`LICENSE`) | 506 | MCP side-car | **53 tools** (42 essential + 11 GUI) over Anki, v0.27.0 beta, TypeScript. An agent can present cards, explain concepts and create or edit notes mid-session. Requires the Anki **desktop app plus the AnkiConnect plugin** — plan for that dependency. The highest-starred education MCP server in existence; see the shelf note below. |
| universal-examprep-skill | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT (`LICENSE`) | 300 | skill | "Exam Cram Coach" with **cross-session memory** and **citation-sourced** answers. Python. Memory + citations is the combination the high-risk regimes reward. |
| algo-sensei | [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | MIT (`LICENSE`) | 285 | skill | LeetCode / DSA mentor packaged for Claude Code and claude.ai. CS-education pedagogy shipped as a skill rather than an app. |
| universal-diagnostic-tutor-skill | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | MIT (`LICENSE`) | 238 | skill | **Diagnosis-first** tutor for STEM and CS: establishes the misconception before explaining. Pedagogically the strongest shape on this list, and the one closest to OATutor's mastery logic without the Bayesian machinery. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT (`LICENSE`) | 156 | skill | Chinese civil-service exam tutoring with **authority citations** — high-stakes prep with provenance attached. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT (`LICENSE`) | 130 | app | **Block-based local-first adaptive learning workspace.** 12 composable blocks (notes, quiz, flashcards, knowledge graph, study plan, analytics), **FSRS 4.5** spaced repetition with proactive review, **LOOM** concept-mastery/prerequisite graph generating learning paths, 10+ LLM providers **defaulting to Ollama**, FastAPI + Next.js, 27 forks. Runs entirely on the user's machine with no cloud transmission. **Reinstated this pass** — see corrections. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT (`LICENSE`) | 106 | skill **pack** | A curated collection of teaching-and-learning skills rather than a single skill. Shell. The first *pack* found in education — the distribution unit above the individual skill. |
| feifei-companion | [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) | Apache-2.0 (`LICENSE`) | 105 | app | "Trinity K12 AI Education System" for Chinese students. Permissive, China-origin, K-12. |
| mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT (`LICENSE`) | 91 | **full LMS** | Self-hosted AI-mentor LMS for enterprise L&D: voice and chat role-play scored automatically, **automated grading of open-ended behavioural and problem-solving answers**, AI course generation from existing documentation, Langfuse tracing of every model call, multi-tenant and white-label. TypeScript, Poland-origin. **This is the row that narrows this KB's standing "no permissive auto-grader" gap** — full entry in `verticals/solutions.md`. |
| Studivexa | [codeXsidd/Studivexa](https://github.com/codeXsidd/Studivexa) | MIT (`LICENSE`) | 72 | app | AI productivity workspace for students and developers. JavaScript. |
| AI_Tutor_Release | [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release) | MIT (`LICENSE`) | 57 | app | Open-source **RAG** tutor for K-9, adapted to the Chinese grade 1–9 curriculum. JavaScript. A rare **curriculum-aligned** permissive tutor — directly relevant to the curriculum-mandate demand recorded in `intel/market.md`. |
| civil-ai | [zhangl1001/civil-ai](https://github.com/zhangl1001/civil-ai) | MIT (`LICENSE`) | 43 | reference impl | **Local-first adaptive tutoring agent foundation reference implementation** for iOS and Web, with a civil-service-exam application on top. TypeScript. Earns a row at 43★ because it is explicitly a reference architecture, and a local-first one. |
| ai-tutor-app | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | Apache-2.0 (`LICENSE`) | 31 | app | Agentic-RAG tutor for applied AI/LLM/RAG/Python: **LangGraph agent + FastAPI + Next.js**, grounded in a curated course and library. The closest production-shaped reference for the P2 retrieval-tutoring pipeline. |
| feynman-tutor | [koukekoukej-glitch/feynman-tutor](https://github.com/koukekoukej-glitch/feynman-tutor) | MIT (`LICENSE`) | 29 | skill | Inverts the roles: **the learner teaches the AI** (Feynman technique) to expose gaps. Python. |
| anything-to-course | [lowwwbank/anything-to-course](https://github.com/lowwwbank/anything-to-course) | MIT (`LICENSE`) | 18 | skill | Turns any material into a **learning-science-based** self-study course with retrieval practice and spaced repetition. The skill-shaped sibling of pattern P2. |
| nanobot-study | [WangyiNTU/nanobot-study](https://github.com/WangyiNTU/nanobot-study) | MIT (`LICENSE`) | 18 | enablement | Guided 3-day study plan built on nanobot (~3k lines of Python) with a Socratic tutor. Small enough to read end-to-end, which is exactly what an enablement asset needs to be. |
| Scientific-learning-skills | [hwl668/Scientific-learning-skills-](https://github.com/hwl668/Scientific-learning-skills-) | MIT (`LICENSE`) | 15 | skill | Diagnosis-first skills that turn an assistant "from answer machine into learning tutor". |

### Measured rejections from the same sweep

High stars, unusable for reusable studio IP. Recorded so the next pass does not
re-probe them.

| Repo | ★ | Licence (payload) | Verdict |
|---|---|---|---|
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 563 | **AGPL-3.0** | Reject for reusable IP. Skill tree for lifelong learning, 30+ skills K-12 to career. Useful as a competency-graph *reference*. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | 156 | **AGPL-3.0** | Reject for reusable IP. Self-hosted AI language learning, local or cloud LLMs. |
| [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | 88 | **GPL** | Reject for reusable IP. Builds a private course in about a minute; take the idea, not the code. |
| [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | 71 | **AGPL-3.0** | Reject for reusable IP. Turns material into a game-based course. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 61 | **NONE** | **Do not use.** 6 specialised agents, adaptive roadmaps, quizzes, RAG — no `LICENSE` at root, and its README licence section reads only *"This project is open source and available for educational purposes."* |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | 24 | **NONE** | **Do not use.** 21-step Socratic-tutor workflow, no `LICENSE` and **no licence mention anywhere in the README**. |

**A third failure mode for the catalogue: the unenforceable prose grant.**
"Open source and available for educational purposes" names no licence, no copyright
holder and no grant to modify or redistribute, and "for educational purposes" would
*restrict* commercial use if it meant anything. It is worse than silence because it
reads like permission and survives a casual review. This KB's licence-failure
catalogue now has three entries: **no licence file at all**
(`DMontgomery40/mcp-canvas-lms`), **a licence hidden outside the root**
(`OS4ED/openSIS-Classic` at `docs/License.txt`, `frappe/*` at lowercase
`license.txt`), and **prose that imitates a grant** (the two rows above).

### Added in the fourth pass of 2026-10-06 — the OpenMAIC upstream, and the first Africa-placed shelf

**New channel this pass: paper-to-repository tracing** (arXiv and the ACL
Anthology demo track) plus a **GitHub-organisation sweep**. Neither had been used
by any earlier pass of this KB. Both licence columns below were read from the
repository's own `LICENSE` payload via `raw.githubusercontent.com` on 2026-10-06.

The headline is not a new discovery — it is the **resolution of a gap this KB has
carried through three passes**. See the corrections section.

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** (`LICENSE`, © 2026 THU-MAIC) | **40.0k** | Open Multi-Agent Interactive Classroom, from **Tsinghua University**. Turns a topic or an uploaded document into a generated lesson in one click: slides, quizzes, HTML simulations and project-based-learning scenes, delivered by AI teacher *and* AI classmate agents over a shared whiteboard with text-to-speech. Exports PPTX and interactive HTML. v1.2.0-rc.1 (2026-10-04) moves to a **server-first architecture with PostgreSQL persistence**, so a course generation survives a closed browser tab or a server restart. Integrates with agent workbenches (OpenClaw), so a classroom can be generated from a chat client or an IDE. TypeScript / Next.js / React. |
| AI-Teaching-Agent | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** (`LICENSE`, © 2026 littlecookie) | **0** | Turns Markdown teaching sources into **linked lab, exam and grading artefacts** through a structured DSL validated against JSON Schema. Three properties matter more than its star count: a **`WAITING_REVIEW` human-approval gate** before anything is published, **sandboxed grading execution with evidence generation**, and a **candidate-facing exam preview that strips answers and internal grading references**. CLI/JSON plus an MCP server; local-first, offline demo needs no API key. Python. |
| pedagogy-benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** (`LICENSE`) | 12 | Benchmarks the **pedagogical knowledge** of LLMs using real **teacher-qualification exam questions** — not task accuracy, but whether the model knows how to teach. Python. The only pedagogy-specific model-selection instrument on this shelf. |
| edu-qurating | [AI-for-Education/edu-qurating](https://github.com/AI-for-Education/edu-qurating) | **MIT** (`LICENSE`) | 3 | Educational content curation / quality-rating tooling. Python. |
| voice-ai-evaluation-framework | [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | **MIT** (`LICENSE`) | 1 | Evaluation harness for **voice-based** AI systems — the modality that matters where literacy and device constraints bind. Python. |

**Read the star counts honestly.** OpenMAIC at 40.0k is a flagship. The other four
are **1–12★ research-grade code**. They earn their rows because they are the only
permissive assets this KB has found for *pedagogical model selection*, *voice
evaluation* and *gated grading* — three functions the shelf had no entry for at
all. Treat `AI-Teaching-Agent` (0★, no releases) as a **reference architecture to
read and re-implement**, not a dependency to pin.

#### Why `AI-for-Education` is the most strategically placed find in this KB

It is a GitHub organisation whose stated mission is to **democratise access to AI
in education in low- and middle-income countries**, and its repositories are
**placed in named countries**: a lesson-plan parser built for **Sierra Leone's
MBSSE** (Ministry of Basic and Senior Secondary Education), and
**Luganda linguistic benchmarks** for **Uganda**. Through three passes this KB
recorded Africa as "almost entirely uncovered, greenfield, no deployed open source
African education AI shelf to recommend from." **That gap is now narrowed to a
specific, MIT-licensed, ministry-engaged starting point** — small, but real and
placed. See `intel/market.md`.

#### Licence flags from this pass — two assets you cannot ship

| Asset | Claim | What the payload actually says |
|---|---|---|
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | Its **EACL 2026 demo paper** describes it as "the first open-access, open-source model for pedagogical quality evaluation of AI tutor responses, released under an **MIT** license" | **No `LICENSE` payload exists.** `README.md` returns 200 on both `main` and `master`; `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` all **404 on both branches**. The repository is real and the paper is peer-reviewed, but **the grant is in the PDF, not in the repo** — so it is legally unlicensed, which is the worst state for client work. Its evaluation framework (MI = Mistake Identification, ML = Mistake Location, PG = Providing Guidance, AC = Actionability) is worth re-implementing; the code is not worth shipping until a `LICENSE` lands. **Ask the author to add one** — this is a cheap, high-value upstream contribution. |
| Open TutorAI (arXiv 2602.07176) | "An open-source platform for personalised and immersive learning with generative AI" — LLM tutoring with customisable 3D avatars | **CC BY-NC-SA 4.0** — **non-commercial and share-alike.** Not usable in a client engagement at all, under any architecture. "Open source" in a paper abstract is not a licence. |
| [AI-for-Education/Luganda-linguistic-benchmarks](https://github.com/AI-for-Education/Luganda-linguistic-benchmarks) | sits in an organisation whose other five repos are all MIT | **No `LICENSE` payload** (`README.md` 200, `LICENSE` 404). **Per-repo probing is not optional even inside a uniformly-licensed org** — five MIT siblings do not license the sixth. |

**This is the fourth distinct failure mode the catalogue has recorded**, after the
unlicensed repo, the AGPL-plus-paid-tier side-car and the unenforceable prose
grant: **the licence that exists only in the paper.** A peer-reviewed claim of MIT
is evidence about intent, never about rights.

### Added in the fifth pass of 2026-10-06 — the first India-, ASEAN- and LATAM-origin permissive projects

**Channel new to this KB this pass:** **institution-first search** — searching by
funding body, ministry and university name in English and Spanish rather than by
GitHub topic or star count. Four passes of topic sweeps had concluded that India-,
ASEAN- and LATAM-origin permissive education projects did not exist. They do. They
were invisible to topic sweeps because **none of them has a single star**, and
three were created in 2026.

Every licence below was read from the repository's own `LICENSE` payload via
`raw.githubusercontent.com`. Star and commit counts were read from the repository
page the same day. **Read the maturity column before the licence column** — this
pass's finding is that region coverage is now achievable and that almost nothing on
it is production-grade.

| Agent | Repo | License (read from payload) | ★ / commits | Origin | Maturity | What it does |
|---|---|---|---|---|---|---|
| Shiksha Copilot | [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) | **MIT** (`main/LICENSE`, Microsoft Corporation) | 9★ / 149 commits | **India** — Microsoft Research India, VELLM initiative; classroom validation with the **Sikshana Foundation** | Working full-stack system; GPT-4o dependency acknowledged in its own README | Teacher-side lesson planning: select curriculum, grade, subject and chapter, then generate lesson plans, real-world examples, analogies, hands-on activities, and formative and summative assessments. Compiles reviewed output to **DOCX, PPT and student handouts**, and generates **multi-chapter question banks against standard blueprint formats**. React + FastAPI + Azure durable functions; textbook ingestion pipeline with **human curator oversight** |
| CurriculumCraft AI | [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) | **MIT** (`main/LICENSE`, 2026) | 0★ / 7 commits | **India** — individual, Hacktoberfest 2026 | Public beta, real TypeScript codebase | **CBSE / NCERT grades 9–12** assessment engine: tests, lesson plans and marking keys. Runs on **open-weight Gemma only** (`gemma-4-26b-a4b-it`, failover `gemma-4-31b-it`), temperature 0.2, no Gemini. Model calls routed through backend endpoints so API keys never reach the browser; IP rate limit of 30 requests per 5-hour window. Ships an explicit **copyright analysis**: no NCERT text is stored or reproduced, syllabi are treated as public standards, all items synthesised on demand |
| TutorIA | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | **MIT** (`main/LICENSE`, Grupo Sirius) | 0★ / 4 commits | **LATAM** — Universidad Tecnológica de Pereira, Sirius research group, **Colombia**; funded under Colombia's **SNCTI** | **Scaffold only — see the warning below** | Specified as an autonomous tutor agent for **rural higher education in Risaralda**, delivered as an **Open edX XBlock/plugin** with Claude API, TTS audio replies, animated avatar, teacher statistics panel and cross-session context. Initial subjects: Programación I (Python) and Introducción a la Matemática. Named team includes a **dedicated pedagogical director** |
| Tutor Agente Local | [DannyAvilaL/agente_clases](https://github.com/DannyAvilaL/agente_clases) | **MIT** (`main/LICENSE`, 2026) | 0★ / 5 commits | Spanish-language, individual; **no institution or country stated in the repository** | Working single-author system | **100% offline** programming-class preparation: Ollama **Phi-3 (2 GB)** generates per-student explanations and exercises in Markdown, synthesises `.csv` datasets and injects them as tables into local **PostgreSQL**. Syncs Google Calendar into a **local Radicale CalDAV** server and keeps working with no internet. Streamlit dashboard; `cron` autopilot prepares classes a week ahead |

#### TutorIA: read this before you cite it

TutorIA is the **first LATAM-origin permissive education project this KB has
found in five passes**, and it is institutionally real — a named university, a
named research group, a named pedagogical director, and public science funding.
It is also, today, **a README and a licence**. Every code path in its own
documented tree returns HTTP 404:

| Probed path | Result |
|---|---|
| `backend/requirements.txt`, `backend/main.py`, `backend/app/main.py` | 404 |
| `frontend/package.json` | 404 |
| `openedx/setup.py` | 404 |
| `docker-compose.yml`, `.env.example` | 404 |

Its own quickstart tells you to clone a **different repository**
(`Sof1SP/tutorIA`) from the one the README lives in. So: **cite TutorIA as
evidence that the LATAM gap is a build gap rather than an interest gap, and as a
partnership lead. Never cite it as a starting point you can fork.** The
architecture it specifies — Open edX XBlock, side-car agent, teacher analytics —
is exactly pattern **P1** in this KB, which is the useful part: a Colombian public
university has independently specified this KB's default engagement shape and has
not built it.

#### What these four rows change, and what they do not

- **Three declared gaps move from "open" to "open at a different size."** This KB
  has recorded "no India-origin", "no ASEAN-origin" and "no LATAM-origin"
  permissive education project as its firmest findings, across four independent
  channels. All three were **artefacts of star-ordered discovery**. An
  institution-first search found all three in one pass.
- **Nothing here is a product shelf.** Three of the four rows have **0★**. The
  India row with institutional weight — Shiksha Copilot — has **9★ and 12 forks**.
  Globant cannot shop from this shelf; it can **partner** (MSR India, UTP
  Colombia, NUS) or **re-implement**.
- **Curriculum alignment is no longer China-only.** Before this pass,
  `Zenglian990/AI_Tutor_Release` (Chinese grade 1–9) was the only
  curriculum-aligned permissive tutor in this KB. CurriculumCraft AI adds
  **CBSE/NCERT grades 9–12**, and does it on **open-weight models only** — which
  makes it the first curriculum-aligned permissive asset here that is also
  deployable in a sovereignty-constrained engagement.
- **Two of them are built against the copyright problem, not around it.**
  CurriculumCraft's synthetic-generation argument and Shiksha Copilot's
  human-curator ingestion gate are both answers to the question every ministry
  engagement asks in week one. Reuse the arguments even where you do not reuse the
  code.

#### Measured rejections from the same sweep

Recorded so the absence is visible rather than silent.

| Candidate | Why it is not in the table |
|---|---|
| [vitorr2101/Projeto-Agente-IA-Educacional](https://github.com/vitorr2101/Projeto-Agente-IA-Educacional) | **Brazil-origin and therefore the row this KB most wanted** — and it has **no `LICENSE` payload** on `main` or `master` across five filenames. No rights, no row |
| "K.A.L.I." (described in search results as a sovereign AI learning engine with 3D logic visualisation) | **Could not be located.** A targeted search returned ten unrelated `sovereign`-named repositories and no K.A.L.I. Not recorded — an unverifiable name is not a finding |
| AICET's Codaveri, Softmark, ScholAIstic (NUS / AI Singapore) | **Closed source.** See the ASEAN note below — the mature ASEAN education AI is not open, but its host platform is |

#### The ASEAN finding is a platform, not an agent

Singapore has the most operationally mature education AI in APAC and almost none
of it is open. **AICET** — the AI Centre for Educational Technologies, hosted by
AI Singapore, funded by the Smart Nation and Digital Government Office, working
with Singapore's **Ministry of Education** — ships three products at real scale:
**Codaveri** (programming tutor, 30,000+ pieces of personalised feedback since
2024), **Softmark** (exam-script digitisation and concurrent team marking, 70,000+
scripts in 2025, now with computer-vision grouping of similar answers) and
**ScholAIstic** (multi-agent platform for educator-authored specialised chatbots,
deployed across Social Work, Law and Nursing at NUS since June 2024). **None has a
public repository.**

What is open is the platform underneath Codaveri:
[**Coursemology/coursemology2**](https://github.com/Coursemology/coursemology2) —
**MIT, read from `master/LICENSE` (Coursemology.org)**, 158★, 78 forks, 15,802
commits, Rails 8 + React, NUS-origin and "currently supported by the AI Centre for
Educational Technologies." It is recorded in `repos/foundations.md` and
`verticals/solutions.md` rather than here, because it is an LMS and that decides
how you deliver it. **The ASEAN gap was never that ASEAN lacks education AI. It is
that ASEAN's mature education AI is closed and its substrate is MIT** — which is a
much better commercial position than the gap this KB had recorded.


## The education MCP shelf — a side-car is permissive by choice, not by construction

The licence-boundary note below says an external MCP side-car keeps its permissive
licence while an in-tree plugin inherits copyleft. True of the canonical servers,
but it is the *author's* choice, not a property of the architecture. Every Canvas
and Moodle MCP server that surfaces in search was probed on 2026-10-06:

| Repo | ★ | Licence (read from payload) | Verdict |
|---|---|---|---|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 278 | MIT (`LICENSE@main`) | **Canonical Canvas side-car. Use this.** |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | ~42 | MIT (`LICENSE`) | **Canonical Moodle side-car. Use this.** |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 103 | **NONE** | **Do not use.** 54 working tools, v2.3.0, no `LICENSE` on any branch and no licence statement in the README. |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | 38 | **NONE** | **Do not use.** No `LICENSE` on any branch, none in README. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 1 | **AGPL-3.0** (`LICENSE@main`) | Avoid: AGPL **and** a paid premium-plugin upsell. |
| [CharlieCardenasToledo/mcp-canvas-server](https://github.com/CharlieCardenasToledo/mcp-canvas-server) | 0 | MIT (`LICENSE@main`) | Usable, unproven. README claims 117 tools / 21 categories while the repo description says 51 — its own numbers disagree. |
| [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | 0 | MIT (`LICENSE@main`) | Usable, unproven. Only Go implementation found. |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **506** | MIT (`LICENSE`) | **The biggest one, and it is not an LMS server.** 53 tools (42 essential + 11 GUI), v0.27.0 beta, TypeScript. Added third pass 2026-10-06. Needs the Anki desktop app **plus AnkiConnect**. |

**The shelf above was scoped wrong, and the third pass of 2026-10-06 proves it.**
It was assembled by sweeping *Canvas and Moodle* MCP servers — a scope defined by
LMS vendor name. The highest-starred education MCP server in existence is
`ankimcp/anki-mcp-server` at **506★**, which is **1.8× `vishalsachdev/canvas-mcp`**
and was invisible to every earlier sweep because it serves the **retention** layer
rather than the LMS layer.

It also confirms the licence boundary on a second, unrelated platform family:
**Anki itself is AGPL-3.0, and its MCP side-car is MIT.** The side-car keeps its
permissive licence across an AGPL host exactly as it does across GPL-3.0 Moodle.

**Scope the next sweep by learning *function*, not by vendor name:** LMS, SIS,
retention and spaced repetition, assessment, library, proctoring, video. Each is a
separate MCP shelf and this KB has now swept two of them.

**An unlicensed repo is worse than a copyleft one.** AGPL-3.0 is a constraint you
can architect around. No licence at all means default copyright — all rights
reserved, no grant to use, modify or redistribute. `DMontgomery40/mcp-canvas-lms`
is the trap: 103★ and 54 tools make it look mature, and it cannot legally ship in
a client deliverable. Probe the licence before the feature list.

Two further forks of the canonical Canvas server carry byte-identical
descriptions and the same MIT licence with none of the history:
[abr-Projects/canvas-mcp](https://github.com/abr-Projects/canvas-mcp) and
[BartMassey-upstream/canvas-mcp](https://github.com/BartMassey-upstream/canvas-mcp).
Pin `vishalsachdev/canvas-mcp`.

## The license boundary that decides your architecture

This is the single most reusable finding in this KB, and it is measured, not
inferred:

| Piece | Where it runs | License read from payload |
|---|---|---|
| [Limekiller/moodle-block_openai_chat](https://github.com/Limekiller/moodle-block_openai_chat) | in-tree Moodle plugin | GPL-3.0 |
| [yedidiaklein/moodle-local_aiquestions](https://github.com/yedidiaklein/moodle-local_aiquestions) | in-tree Moodle plugin | GPL-3.0 |
| [cgrevisse/moodle-qbank_genai](https://github.com/cgrevisse/moodle-qbank_genai) | in-tree Moodle plugin | GPL-3.0 |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | external process, talks to Moodle over its web API | **MIT** |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | external tool provider | **Apache-2.0** |

**Consequence:** AI built *inside* a copyleft LMS inherits that LMS's license.
The same capability built as an external service reached over LTI 1.3 or MCP
stays permissive and stays reusable across client engagements. Prefer the
side-car. This drives pattern P1 in `compose/patterns.md`.

## Corrections to earlier passes

- **RESOLVED: `OpenMAIC-Brasil` was a phantom, and the real OpenMAIC is a
  40.0k★ MIT project from Tsinghua.** Through three passes this KB recorded
  [planejaia/OpenMAIC-Brasil](https://github.com/planejaia/OpenMAIC-Brasil) as "a
  confident search result for a repository that genuinely does not exist" and used
  it as the lead evidence for the **no-LATAM-origin-education-agent** gap. Both
  halves of that now have a better answer.

  **Re-probed 2026-10-06 (fourth pass), the Brazilian repo is still gone:**
  `README.md` and `LICENSE` return **404 on all four** candidate branches
  (`main`, `master`, `develop`, `v1.0.0`). That claim stands, now on a fourth
  independent probe.

  **But the name was never Brazilian.** The upstream is
  [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — *Open Multi-Agent
  Interactive Classroom* — **MIT, 40.0k★, from Tsinghua University**, v1.2.0-rc.1
  dated 2026-10-04. The "Brazil-origin multi-agent classroom with a v1.0.0
  release" that search results kept asserting was almost certainly a **vanished
  fork or mirror of a Chinese project**, mis-attributed by its `-Brasil` suffix.

  **Two lessons, and the second is the expensive one.** First: when a probe 404s,
  search for the *upstream of the name* before recording a gap — this KB spent
  three passes treating an absence as evidence while a 40k★ MIT implementation of
  the same thing sat one query away. Second: **a repository name is not a
  provenance claim.** A `-Brasil`, `-India` or `-LATAM` suffix is a string an
  author chose; regional attribution has to come from the owner, the commit
  history or the README, never from the slug. This KB's LATAM gap was argued
  partly from a suffix.
- **AutoGen is no longer a starting point.** [microsoft/autogen](https://github.com/microsoft/autogen)
  (61.3k★) is explicitly in **maintenance mode**: *"AutoGen is now in maintenance
  mode. It will not receive new features or enhancements and is community managed
  going forward. New users should start with Microsoft Agent Framework."* Its
  `LICENSE` at HEAD is now **CC-BY-4.0** (the repo is dual CC-BY-4.0 / MIT), not
  the plain MIT recorded in earlier cycles. Earlier education cycles listed
  AutoGen as a top agent at ~60k★ — that recommendation is withdrawn in favour of
  MAF.
- **OpenTutor is REINSTATED. The withdrawal recorded earlier on 2026-10-06 was
  itself wrong, and this is the most important correction in this KB.**
  Cycle 3 recorded *"OpenTutor (MIT, ~900★, FSRS6 + KG + 12 blocks)"*. The second
  pass of 2026-10-06 withdrew that entry after probing
  [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) — 8★, 5 commits,
  no `LICENSE` on three branches across eight filename variants and none in its
  README — and concluded the project did not exist as described.

  **It does.** The project cycle 3 meant is
  [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor), probed directly on
  2026-10-06: **MIT** (read from `LICENSE`), **130★ / 27 forks**, Python,
  **12 composable learning blocks**, a **LOOM** concept-mastery and prerequisite
  graph, **FSRS 4.5** spaced-repetition scheduling, local-first with 10+ providers
  and an Ollama default, FastAPI + Next.js. Cycle 3 was right about every
  architectural claim — 12 blocks, knowledge graph, FSRS, MIT — and wrong only on
  the star count (~900 claimed, 130 actual) and the FSRS version (6 claimed, 4.5
  actual).

  **The lesson is new and it cuts the other way from every other licence lesson
  here.** The rest of this KB's probe discipline guards against *false positives* —
  a repo that looks licensed and is not, or looks MIT and is AGPL. This was a
  **false negative that deleted a true finding**, and it cost more than any false
  positive recorded here: a correct entry was removed and replaced with a confident
  denial. A 404, or an unlicensed verdict, on `owner/name` is evidence about **that
  owner's repository only** — never about the project. `OpenTutor` resolves to at
  least three distinct things: `zijinz456/OpenTutor` (MIT, 130★), `tutornew/OpenTutor`
  (unlicensed, 8★) and the unrelated Open TutorAI arXiv work.

  **Therefore: a withdrawal requires a stronger probe than an addition.** Before
  removing an entry, enumerate the owners publishing under that project name. An
  addition that is wrong wastes a probe next pass; a withdrawal that is wrong
  destroys knowledge and is believed. OATutor
  ([CAHLR/OATutor](https://github.com/CAHLR/OATutor), MIT, 264★, UC Berkeley)
  remains a separate project from all of them.
- **DeepTutor's canonical repo is `HKUDS/DeepTutor`.** Searching for it surfaces
  forks and mirrors first: `cloudtoolbox/deeptutor` (7★), `lucadeg/DeepTutor` and
  `q-qp-p/HKUDS-DeepTutor` all carry the same description and the same Apache-2.0
  license but none of the history. Pin the HKUDS origin.

## Declared gaps — searched this pass, nothing found

An informed gap is information; silence looks exactly like coverage.

- **NARROWED AGAIN (fourth pass, 2026-10-06): the gated-grading architecture now
  has a permissive reference implementation — with 0 stars.**
  [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent)
  (MIT) implements exactly the shape every regulator in this KB demands: a
  `WAITING_REVIEW` human-approval gate, sandboxed grading with evidence output,
  and an answer-stripped candidate view. **What is still missing is adoption, not
  design** — 0★, no releases, one author. So the gap changes character: it is no
  longer "nobody has built this", it is **"nobody has built this at production
  maturity"**. Read it, re-implement the gate, do not pin it.
- **NEW GAP, precisely sized (fourth pass): pedagogical evaluation is published but
  unlicensed.** `AITutor-EvalKit` (EACL 2026) is the one purpose-built instrument
  for scoring *tutoring quality* rather than answer accuracy, and it has **no
  `LICENSE` payload**. There is therefore **no shippable permissive tutor-quality
  evaluator** on this shelf. `AI-for-Education/pedagogy-benchmark` (MIT, 12★)
  covers the adjacent question — which model knows how to teach — but it scores
  **models against exam questions, not live tutor dialogue**. The evaluation gap
  is now split in two, and only the model-selection half is closed.
- **STILL OPEN after a fourth channel: no LATAM-origin permissive education
  project.** This pass searched in Spanish and Portuguese (`Brazil Mexico Chile
  open source educación IA agente github repositorio tutor 2026 MIT`) — a
  **language channel no earlier pass had used** — and returned **zero
  LATAM-origin projects**; the results were the same China-, India- and
  US-origin repositories already recorded. Four independent channels (the
  `education-ai` topic, the `ai-tutor` topic, a stars-sorted search, and now a
  Spanish/Portuguese-language search) agree. **And the single strongest piece of
  evidence for this gap has been withdrawn as unsound** — `OpenMAIC-Brasil` was a
  name, not a Brazilian project (see corrections). The gap survives its own best
  evidence being removed, which is what makes it the firmest finding in this KB.
- **No India-, Japan-, Korea- or ASEAN-origin permissive education project —
  unchanged, and now searched by name.** This pass queried those four
  jurisdictions explicitly and surfaced only China/Hong-Kong-origin assets plus
  the US- and Europe-origin research code above. OpenMAIC (Tsinghua) **widens the
  China lead rather than closing this gap**: the APAC shelf is still
  China-plus-Hong-Kong, now with a 40k★ flagship at its centre.
- **NARROWED on 2026-10-06 (third pass): a permissive auto-grader exists, but not
  a standalone academic one.** Every earlier pass recorded a flat "no permissive
  open source auto-grader exists". That claim is now too broad.
  [Selleo/mentingo](https://github.com/Selleo/mentingo) — **MIT**, read from
  payload, 91★ — states in its own README: *"Grade open-ended answers without an
  L&D queue. Behavioural and problem-solving tasks are analysed automatically and
  returned with actionable feedback."* It also traces every model call through
  **Langfuse**, so the grading decisions are inspectable for cost, latency and
  actual output.

  The precise state of the gap:
  - **Exists:** MIT-licensed automated grading of open-ended *behavioural and
    problem-solving* tasks, inside a full self-hosted LMS built for **corporate
    L&D** — plus a traced audit path over it.
  - **Still missing:** a standalone permissive grader for *academic* assessment,
    and anything curriculum- or rubric-aligned for K-12 or higher-ed exams.
  - **Unchanged:** the oversight requirement. EU AI Act Annex III, the Oklahoma and
    Maryland statutes and Korea's high-impact classification do not care what
    licence the grader carries. **Keep the human gate on any consequential score.**
    What moved is the build-vs-adopt answer for L&D work, not the compliance
    answer — and in an engagement that distinction is worth stating out loud,
    because a client who hears "an open source auto-grader exists" will hear
    "we can skip the review step".
- **No LATAM-origin open source education agent found — re-probed 2026-10-06 with
  evidence.** Chamilo has deep Spanish-language and LATAM deployment but is
  EU-origin and GPL-3.0. The regional opportunity is deployment and localisation,
  not upstream code. Two probes this pass:
  - A search surfaced `planejaia/OpenMAIC-Brasil` ("Open Multi-Agent Interactive
    Classroom", described as v1.0.0 released 2026-08-27). It is **unreachable**:
    `raw.githubusercontent.com` 404s for `README.md`, `LICENSE`,
    `requirements.txt` and `package.json` across `main`, `master`, `dev` and
    `develop`, and the repository page returns **HTTP 404**. Deleted, renamed or
    private. A search hit is not a repository.
  - The `education-ai` GitHub topic, swept in full, contains **no LATAM-origin
    project at all**. Its long tail is Chinese (`ASEpochs/ai-digital-teacher`,
    `SimonsTang/*`, `upstream1119/Traceable-Ideological-Education-RAG`), Indian
    (`brahm-ai-official/brahm-ai`, 5★) and German (`awesome-german/ai-tools`,
    4★), and nothing on the topic exceeds 448★.

  **Confirmed a third time by a new channel on 2026-10-06 (third pass):** the
  `ai-tutor` topic page and a stars-sorted education repository search — 30 repos
  read between them, 17 net new — returned **not one LATAM-origin project**. The
  permissive education shelf is now measured across three independent channels and
  is China-, US- and Europe-origin. This is the most firmly established gap in this
  KB.

  Latam-GPT (Chile-led, Spanish and Portuguese, published on Hugging Face and
  GitHub) is regional *foundation* infrastructure — the same shape as the APAC
  gap below: a base model with no pedagogy layer on top.
- **PARTLY REFUTED on 2026-10-06 (third pass): APAC-origin education agents do
  exist, and several are permissive and well-starred.** Earlier passes recorded
  `panaversity/learn-agentic-ai` as "the one APAC-origin education asset found".
  The `ai-tutor` topic sweep returned a China-origin cluster that contradicts this
  outright: [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) (MIT,
  **624★** — the highest-starred permissive education agent in this KB after
  DeepTutor), [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill)
  (MIT, 156★), [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion)
  (Apache-2.0, 105★) and
  [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release)
  (MIT, 57★, **aligned to the Chinese grade 1–9 curriculum**). DeepTutor itself is
  HKUDS — Hong Kong. The APAC shelf is the *strongest* regional shelf in this KB,
  not the weakest, and the earlier claim was an artefact of sweeping only the
  `education-ai` topic.

  **What survives of the gap, stated precisely:** no education agent layer built on
  top of an APAC **sovereign** model. The China-origin cluster above runs on
  commercial and open-weight models (StudyMate ships a DeepSeek harness) — none of
  it targets Sarvam, SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think, BharatGen,
  Fugaku-LLM or NTT Sarashina. And no India-, Japan-, Korea- or ASEAN-origin
  permissive education agent surfaced in either sweep; the APAC shelf is
  **China-plus-Hong-Kong**, which is a narrower finding and a more useful one.

- **APAC sovereign models are base models, not education agents.** Sarvam AI,
  SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think and NTT Sarashina are
  foundation models; none ships an education agent layer. Re-probed 2026-10-06
  and the list only grew: **BharatGen** (IndiaAI Mission), Japan's
  **Fugaku-LLM**, and South Korea's National Sovereign AI Initiative champions
  (LG AI Research, SK Telecom, Naver Cloud, NC AI, Upstage). Still all base
  models. `learn-agentic-ai` remains the one APAC-origin education asset found;
  the APAC long tail on the `education-ai` topic is individual-scale
  (`brahm-ai-official/brahm-ai`, 5★). The pedagogy layer on top of a sovereign
  model is still unbuilt, and that is the opportunity.
- **No open source EU AI Act compliance toolkit specific to education** surfaced
  this pass. The compliance work in pattern P4 is assembled from general-purpose
  parts (typed outputs, checkpointed audit trails, explainable mastery models).

## Gap updates from the fifth pass of 2026-10-06

The institution-first channel refuted three of this KB's firmest regional gaps.
They are left standing above, rather than deleted, so the correction is legible.

| Gap as recorded above | State after the fifth pass |
|---|---|
| "No India-origin permissive education project found in any channel" | **REFUTED.** [microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) (MIT, 9★, Microsoft Research India / VELLM, validated with the Sikshana Foundation) and [Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) (MIT, 0★, CBSE/NCERT grades 9–12 on open-weight Gemma only) |
| "No ASEAN-origin permissive education project found in any channel" | **REFUTED, and reframed.** [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) (MIT, 158★, 15,802 commits, NUS, supported by AICET) is a mature ASEAN-origin permissive platform. What is actually missing is ASEAN's **agent** layer: AICET's Codaveri, Softmark and ScholAIstic run at ministry scale and are **closed** |
| "No LATAM-origin permissive education project — the firmest finding in this KB" | **REFUTED on existence, confirmed on substance.** [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) (MIT, Universidad Tecnológica de Pereira, Colombia, SNCTI-funded) exists and specifies this KB's P1 architecture — and **every code path in its own documented tree 404s**. The gap is a build gap, not an interest gap |
| "No education agent layer on an APAC **sovereign** model" | **STILL OPEN, and now with a licence reason.** [aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) has **no `LICENSE` payload**; its README §Licensing states terms "may vary depending on the underlying base model's restrictions" — Llama3-based variants carry commercial-use restrictions, Gemma-based variants differ — and directs you to each **Hugging Face model card**. Anyone building an education layer on a SEA sovereign model must clear rights **per model, not per repository**. Related, verified this pass: **MaLLaM** (Malaysia's sovereign LLM, built with NVIDIA, 3M+ users via YTL/Yes) and **Gemma-SEA-LION-v4-27B-VL** (March 2026) |
| "No open source EU AI Act compliance toolkit specific to education" | **RE-SIZED, and much smaller than recorded.** The generic toolkit now exists and is permissive — [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) (**MIT**, 8★, TypeScript, six risk tiers, 61 conformity checklist items, 8 document templates, CLI + SDK + client-only web UI) and [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) (**Apache-2.0**, ETH Zurich). Neither mentions education or **Annex III point 3**. The missing piece is an education **profile** on an MIT base, not a toolkit from scratch — see pattern **P13** |
| "No shippable permissive evaluator of tutoring quality" (declared NEW in the fourth pass) | **STILL OPEN — and the reason is now structural, not accidental.** See the licence finding below |

### The licence pattern in pedagogy evaluation — four instruments, zero permissive software licences

The fourth pass found that `AITutor-EvalKit` claims MIT in a peer-reviewed paper
and has no `LICENSE` payload, and called it "a fourth licence failure mode." The
fifth pass searched for alternatives and found that **this is how the whole
subfield is licensed**:

| Instrument | Venue | Licence as claimed | `LICENSE` payload |
|---|---|---|---|
| [kaushal0494/AITutor-EvalKit](https://github.com/kaushal0494/AITutor-EvalKit) | EACL 2026 | "released under an MIT license" (in the paper) | **None** — probed both branches |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) (43★, 14 forks, ETH Zurich LRE, EMNLP 2025 oral) | EMNLP 2025 | **Contradicts itself inside one file**: README line 3 badge says **CC BY 4.0**, README line 199 says **CC BY-SA 4.0** | **None** — probed 10 filenames on `main` |
| [kaushal0494/UnifyingAITutorEvaluation](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | NAACL 2025 | not stated | **None** — probed both branches |
| Open TutorAI (arXiv 2602.07176) | arXiv | "open-source" | **CC BY-NC-SA 4.0** — non-commercial |

**The fifth failure mode, and the one most likely to catch a delivery team: the
licence that contradicts itself inside one file.** A reviewer who reads the badge
gets a permissive answer; a reviewer who reads to the bottom gets a ShareAlike
answer; a reviewer who probes the payload gets no answer at all. All three
reviewers are reading the same commit.

**So what.** MathTutorBench is the most useful of the four and the one you still
cannot vendor: 7 tasks across 3 skills (problem solving, Socratic questioning,
solution correctness, mistake location, mistake correction, scaffolding
generation, pedagogy following with hard variants), a **1.5B pedagogical reward
model** that scores win rates of a generated teacher utterance against ground
truth, and a published leaderboard over 20+ models. **Read the task design,
re-implement the harness, and do not vendor any of the four.** The cheapest
high-value upstream contribution available in this industry remains unchanged
and now applies to three repositories instead of one: **file an issue asking for
a `LICENSE` file.**
