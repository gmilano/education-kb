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

**47 rows, all verified.** The 12 recorded in the morning pass of 2026-10-06, 2
added in the second pass, **17 added in the third pass** from the `ai-tutor`
GitHub topic page and a stars-sorted repository search, and **5 added in the
fourth pass** by tracing academic papers to their repositories and sweeping a
GitHub organisation, and **4 added in the fifth pass** by searching on funding
body, ministry and university name in English and Spanish instead of by topic or
star count, and **3 added in the eighth pass** from an
**institutional-event channel** — a university hackathon whose rules make an OSI
licence a condition of evaluation — five distinct channels, each new to this KB when it was used. One of the 17, OpenTutor, is a **reinstatement** of an entry this KB wrongly
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
| TutorIA | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | **MIT** (`main/LICENSE`, Grupo Sirius) | 0★ / 4 commits | **LATAM** — Universidad Tecnológica de Pereira, Sirius research group, **Colombia**; funded under Colombia's **SNCTI** | **Specification published, code not — corrected in the eighth pass.** `docs/` holds a **13-page MIT requirements spec (v1.0, April 2026)** and a 5-layer architecture diagram; the six code directories hold only `.gitkeep`. Earlier passes read this as "scaffold only" because they probed code filenames and never `docs/` | Specified as an autonomous tutor agent for **rural higher education in Risaralda**, delivered as an **Open edX XBlock/plugin** with Claude API, TTS audio replies, animated avatar, teacher statistics panel and cross-session context. Initial subjects: Programación I (Python) and Introducción a la Matemática. Named team includes a **dedicated pedagogical director** |
| Tutor Agente Local | [DannyAvilaL/agente_clases](https://github.com/DannyAvilaL/agente_clases) | **MIT** (`main/LICENSE`, 2026) | 0★ / 5 commits | Spanish-language, individual; **no institution or country stated in the repository** | Working single-author system | **100% offline** programming-class preparation: Ollama **Phi-3 (2 GB)** generates per-student explanations and exercises in Markdown, synthesises `.csv` datasets and injects them as tables into local **PostgreSQL**. Syncs Google Calendar into a **local Radicale CalDAV** server and keeps working with no internet. Streamlit dashboard; `cron` autopilot prepares classes a week ahead |
| EduFlow | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **see the holder warning below**) | 1★ / 41 commits | **LATAM** — Pontificia Universidad Católica de **Chile**, Centro de Alumnos de Ingeniería; HaCAIthon 2026, *Educación pública* track | **8-hour hackathon build with working code** — not a product; the only CAi UC education repo verified to contain a running backend and frontend | **Offline-first maths practice for schools with no reliable signal.** Teacher opens a room and shares a 6-character code; student downloads the assignment while in signal (**~8 KB for 10 exercises**), solves it **entirely offline** with immediate correction via **IndexedDB** + Service Worker app-shell cache, and answers **sync automatically** when connectivity returns. FastAPI backend (routers `auth`, `rooms`, `activities`, `answers`) + Next.js PWA + Supabase. Its README names **Kolibri** and **RACHEL** as prior art. **The concrete implementation of the constraint TutorIA's RNF-04 specifies and has no code for** |
| CPU-Benchmark | [caiuc/equipo-6-haCAIthon-2026](https://github.com/caiuc/equipo-6-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **holder warning below**) | 0★ | **LATAM** — PUC **Chile**, HaCAIthon 2026, *Educación y brecha digital* track | 8-hour build; `README.md` and devcontainer verified, no application code confirmed in-tree | Classifies **donated computers** by measuring their real performance, so a school receiving a hardware donation can tell what each machine is actually fit to run. The triage step in front of any low-resource deployment — the question TutorIA's **2 GB RAM / 3G** envelope assumes someone has already answered |
| OnlyUs | [caiuc/equipo-16-haCAIthon-2026](https://github.com/caiuc/equipo-16-haCAIthon-2026) | **MIT** (`main/LICENSE`, © 2026 CAi UC — **holder warning below**) | 0★ / 50 commits | **LATAM** — PUC **Chile**, HaCAIthon 2026, *Educación y orientación* track | 8-hour build; `README.md` and `frontend/package.json` verified in-tree | Simulates the Chilean university application and suggests degree programmes the applicant's score actually reaches. Guidance and admissions rather than tutoring — the one education function in this KB with **no** other permissive entry |

#### TutorIA: read this before you cite it

TutorIA is the **first LATAM-origin permissive education project this KB
found**, and it is institutionally real — a named university, a named research
group, a named pedagogical director, and public science funding.

**⚠️ CORRECTED IN THE EIGHTH PASS (2026-10-06). Earlier passes described this
repository as "a README and a licence" with "every code path 404". The first
half was wrong.** The code claim holds — and is now explained — but the
repository also publishes a **complete requirements specification** that five
passes never probed, because every probe used a *code* filename.

| Probed path | Result | What it is |
|---|---|---|
| `backend/`, `frontend/`, `openedx/`, `data/`, `infra/`, `tests/` | **`.gitkeep` only** | Deliberately placeholder-reserved — which is *why* the code paths 404 |
| `backend/main.py`, `frontend/package.json`, `openedx/setup.py`, `docker-compose.yml`, `.env.example` | 404 | Unchanged from earlier passes |
| **`docs/TutorIA_Requerimientos.pdf`** | **200** | **13-page requirements specification, v1.0, April 2026** — RF-01…RF-20, RNF-01…RNF-10, actors, use cases |
| **`docs/tutoria_architecture.svg`** | **200** | **5-layer architecture**, 19 KB: Usuarios → Open edX LMS → API → Servicios Core → IA & Media |
| **`CONTRIBUTING.md`** | **200** | Contribution guide — also missed by the code-path sweeps |

**The four requirements worth lifting, all under MIT:**

- **RNF-05** — *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with **TLS**
  in transit and **AES-256** at rest as the acceptance criterion. This KB's
  **first Colombian data-protection anchor**; `Ley 1581` appeared nowhere in it
  before the eighth pass.
- **RNF-04** — *"mínimo **2GB de RAM**; funcional con conectividad de **3G**"*.
  A testable low-resource envelope, where this KB previously had adjectives.
- **RNF-09** — agent responses must pass pedagogical review by **at least 2
  subject-expert teachers per subject before launch**. Not an automated
  evaluator, so the standing evaluator gap is unchanged — but it is a **written
  human quality protocol with a quorum**, which is the thing an engagement can
  actually ship.
- **RF-02** (priority *Alta*) — *"**Todo** el código fuente, configuraciones y
  documentación base … deben publicarse en un repositorio de acceso público"*.
  **Unmet as of 2026-10-06.** This reframes TutorIA from an abandoned-looking
  repository into a **tracked commitment**: watch RF-02, and make RF-02 the
  subject of any approach to the Sirius group.

**RNF-10** specifies Colombian Spanish for v1.0 *"con posibilidad futura de
soportar lenguas nativas"* — the layer the eighth pass found is almost entirely
**unlicensed** (see the LATAM substrate shelf in `repos/trending.md`).

Its own quickstart tells you to clone a **different repository**
(`Sof1SP/tutorIA`) from the one the README lives in — MIT © **Sofia Soto
Parra**, containing only `README.md` and `LICENSE`. Two locations, two
copyright holders, zero code. So: **cite TutorIA for its specification, which is
genuinely reusable and the most complete LATAM education-AI design document in
this KB; cite it as a partnership lead; and do not present it as a codebase you
can fork.** The
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


### Added in the sixth pass of 2026-10-06 — no new agents, and the layer that unblocks a whole class of them

**State the negative first: this pass added no new education agent to the table
above.** It swept the **speech and low-resource-language substrate** instead — 26
repositories probed, 26 resolved — and that shelf lives in
`repos/foundations.md`, not here, because none of it is an agent.

What it changes for this file is **what the agents above can now be composed
into.** Every tutor in the table is text-only and English-first by default. With
the sixth-pass shelf, three agent shapes stop being blocked on a proprietary API:

- **The speaking tutor.** [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)
  (**Apache-2.0**, 15.1k★) delivers STT, TTS, diarization and VAD **in one
  permissive tree, with no Internet connection**, on Android, iOS, Raspberry Pi
  and RISC-V. Voice tutoring on classroom-grade hardware is now a permissive
  build, not a vendor dependency.
- **The mother-tongue tutor, in two regions only.** India via
  [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) (**MIT**, 22 scheduled
  languages), [Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) (**MIT**, 13
  languages) and [IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec)
  (**MIT**, ASR); Uganda and Africa via [SunbirdAI/salt](https://github.com/SunbirdAI/salt)
  (**Apache-2.0**, studio-recorded TTS in six Ugandan languages) and
  [masakhane-mt](https://github.com/masakhane-io/masakhane-mt) (**MIT**).
  **Outside those two, the permissive language layer does not exist** — see
  `intel/market.md`.
- **The human-in-the-loop stage, finally with a tool.** Every pattern in this KB
  specifies teacher review; [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya)
  (**MIT**) is the first shelved implementation of it — *"an open source platform
  to annotate and label data at scale."*

**Three traps on that shelf are recorded here because they will be proposed as
agent components.** Full write-ups in `repos/foundations.md`:

| Component | Why it gets refused |
|---|---|
| [rhasspy/piper](https://github.com/rhasspy/piper) | **MIT** but **archived read-only 2025-10-06**; development moved to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl), which is **GPL-3.0**. The obvious offline-TTS pick is **either frozen or copyleft, never both permissive and maintained** |
| [facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication) | **CC BY-NC-4.0** in `main/LICENSE` — **non-commercial. Hard reject** for anything billable, and it is the top result for "open source multilingual speech" |
| [aisingapore/sea-lion](https://github.com/aisingapore/sea-lion) | **No `LICENSE` payload at all.** Its README defers the grant to each HuggingFace **model card** because terms *"may vary depending on the underlying base model's restrictions"*. **A sixth licence failure mode: the licence belongs to the checkpoint, not the project** |

### Declared gap, sixth pass — the oral reading fluency agent does not exist

Searched specifically for a permissive **oral reading fluency** assessor — a child
reads aloud, the system returns words-correct-per-minute. It is the
highest-volume literacy measurement in primary education and the most natural
application of the shelf above.

**Nothing permissive was found.** The category is entirely proprietary: **FLORA**,
**Literably** (IES-funded), Amplify **Text Reading Online**, **SoapBox Labs** — no
public repository for any of them; an Italian ASR fluency app implementing the
Cornoldi MT battery exists only as a paper. What *is* public is the **Ghana ORF
Dataset** — 130 students aged 9–18, passages, audio and human transcriptions, with
**Whisper V2 measured at 10.3% WER** on Ghanaian students reading aloud (*IJAIED*,
[10.1007/s40593-024-00435-9](https://doi.org/10.1007/s40593-024-00435-9)).

**This is the sharpest build opportunity in the KB:** permissive components all
present ([whisperX](https://github.com/m-bain/whisperX), BSD, for the word-level
timestamps that make fluency measurable; [faster-whisper](https://github.com/SYSTRAN/faster-whisper),
MIT, for the transcript), a public dataset, a published accuracy baseline to beat,
and no open competitor. Wired up as **P17** in `compose/patterns.md`.

### Added in the seventh pass of 2026-10-06 — a shelving audit, and the first Korea-origin permissive asset

**Channel new to this KB this pass: native-language search** (Japanese, Korean,
Arabic, Bahasa/Thai/Vietnamese). Earlier passes searched English, then Spanish
and Portuguese. The language substrate it turned up is in
`repos/foundations.md`; what it changes *here* is smaller and more awkward.

**The awkward part first: this file was behind its own trending log.** Five
permissive education MCP servers had been probed and verified by earlier passes
and recorded in `agents/trending.md` — and **never added to the shelf table
below**, which was still the Canvas/Moodle/Anki set. They are now in it, each
re-probed from payload this pass rather than trusted from history. One of them,
`toshieji/moodle-grading-mcp`, **refutes a gap this file was still asserting two
sections above** (see the gap updates at the end).

**The lesson is a maintenance one, and it has now bitten twice.** `repos/trending.md`
recorded the same failure in the sixth pass — *"a 38,046-commit MIT platform this
KB found and then forgot to shelve."* A finding recorded only in an append-only
log is **discoverable but not usable**: nobody scoping an engagement reads 13,000
lines of pass history. **A pass is not finished when the trending entry is
written; it is finished when the shelf, the gap list and the patterns agree with
it.** This pass added a consistency sweep across those four surfaces, and it
found two contradictions in this file alone.

#### The Korea finding, stated at its real size

[yongsoojoo/esd2026-agent-workflow](https://github.com/yongsoojoo/esd2026-agent-workflow)
— **MIT for code, CC BY 4.0 for documentation** (`main/LICENSE` read from
payload, © 2026 Yongsoo Joo), **0★ / 0 forks / 4 commits**, HTML static site.
Course material for *임베디드시스템설계 2026-2* (Embedded Systems Design) at
**Kookmin University**, Seoul: an AI-agent configuration-management tutorial
covering git, AI tooling and Raspberry Pi setup, written by the instructor
jointly with an AI coding agent.

**This is the first Korea-origin permissive education asset in seven passes, and
it is not an agent.** It is an enablement artefact — the same category as the
Microsoft and Hugging Face courses, at 1/10,000th the scale. Recording it
honestly:

- **Closed:** "no Korea-origin permissive education *asset*." One exists, from a
  named university, with a clean dual grant.
- **Still open:** "no Korea-origin permissive education *agent*." Nothing
  changed. And Korea is the jurisdiction with the **AI Framework Act in force
  since 22 January 2026**, so the mismatch between regulatory maturity and open
  supply is the widest of any market in this KB.
- **Worth noting for enablement work:** the **code/docs split grant** (MIT + CC
  BY 4.0) is the correct licensing shape for a teaching artefact, and almost
  nothing else in this KB's teaching-content shelf gets it right.

#### Measured rejections from the native-language sweep

| Candidate | Channel | Why it is not in a table |
|---|---|---|
| [781991937/TOFAN-AI-2026](https://github.com/781991937/TOFAN-AI-2026) | Arabic | **No `LICENSE` payload** (2 branches × 6 filenames). The most substantial Arabic-language education agent found in any pass — *"مساعد تعليمي ذكي"*, ingests lesson files, extracts and analyses content, generates summaries and interactive tests; FastAPI backend with a PWA/Web-App front end, explicitly not a Telegram bot. **Real, well-shaped, and legally unusable.** The single highest-value upstream ask in this KB right now |
| [biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent) | function-scoped (proctoring + grading) | **No `LICENSE` payload.** *"A fully local, mathematics-driven AI exam system for autonomous proctoring, explainable cheating-risk prediction, automated grading and student performance analysis — with no external AI APIs."* Fully local and explainable is exactly the shape Annex III and Vietnam's Decree 33 reward. No grant, no row |
| [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook) | GitHub weekly trending | **No `LICENSE` payload.** An open systems-programming textbook from **UIUC** that gained **~1,626★ in one week** — the highest-velocity education repository seen in any pass of this KB. A university's own trending course text, with no grant attached |

**The Arabic result is the one to act on, and it is a regional finding.** MEA is
the only region in this KB with **zero shippable permissive education assets**:
the fourth pass's Africa shelf (`AI-for-Education`, MIT, Sierra Leone and Uganda)
is research-grade at 1–12★, `Luganda-linguistic-benchmarks` is unlicensed, and
now the one real Arabic-language education agent is unlicensed too. **The MEA gap
is not an interest gap and not a build gap — it is a licensing-hygiene gap**, and
that is the cheapest kind to close. Three `LICENSE` files would change the
regional answer.

### Added in the ninth pass of 2026-10-06 — permissive proctoring, a gap this KB asserted for two passes

Channel: the **funder and procurement channel**, and a **licence-filtered
re-probe** of a gap the seventh pass declared and the eighth carried forward
explicitly marked *"not re-probed."* It was re-probed. **It was wrong.**

A search for `exam proctoring license:mit` returns **204 repositories**. Four,
licence read from payload:

| Agent / tool | Repo | Licence | ★ | What it does |
|---|---|---|---|---|
| exam-cheating-detection | [AarambhDevHub/exam-cheating-detection](https://github.com/AarambhDevHub/exam-cheating-detection) | **MIT** (`main/LICENSE`) | 47 | Computer-vision detection of suspicious exam behaviour: eye-movement tracking and face detection |
| Proctored-MCQ-Exam-Platform | [vincenzo-afk/Proctored-MCQ-Exam-Platform](https://github.com/vincenzo-afk/Proctored-MCQ-Exam-Platform) | **MIT** (`main/LICENSE`) | 36 | Browser-based MCQ exam platform with camera monitoring and certificate generation |
| MyProctorAI | [hemantkarekar/MyProctorAI](https://github.com/hemantkarekar/MyProctorAI) | **MIT** (`main/LICENSE`) | 22 | Flask portal: AI anti-cheating proctoring and invigilation system |
| Exam_Intellect | [RakeshBabuGajula/Exam_Intellect](https://github.com/RakeshBabuGajula/Exam_Intellect) | **MIT** (`master/LICENSE`) | 18 | Live exam observation dashboard; CV + speech recognition with automated feedback |

#### Read this shelf at its real size

**Existence is refuted; maturity is not.** The set tops out at **47★**, all four
are individual- or student-scale projects, **none has an institutional
maintainer**, and the only framework-grade implementation in the sweep —
[lebmatter/exampro](https://github.com/lebmatter/exampro), **72★**, *Proctored
Exams for Frappe Framework* — has **no licence payload** across 8 filenames × 2
branches. That is the sixth consecutive pass in which the most-adopted asset of
a sweep turned out to be the ungranted one.

**So the claim to make to a client is narrow and true:** a permissive proctoring
core exists and can be vendored and hardened, but there is no permissive
proctoring *product*, and anything client-facing is a build on top of a 20–50★
starting point. **Do not quote these as production components.** And before
proctoring enters any proposal, read the regional constraint: proctoring is
biometric processing, which puts it in scope for Annex III in the EU, for the
state-level rules in the US recorded in `intel/market.md`, and for age-gating in
the UAE/China shape of pattern P9.

#### Measured rejections from the same sweep

| Repo | ★ | Why rejected |
|---|---|---|
| [lebmatter/exampro](https://github.com/lebmatter/exampro) | 72 | **No licence payload** — `LICENSE{,.md,.txt}`, `COPYING`, `LICENCE{,.md,.txt}`, `COPYRIGHT` × `main`/`master` all 404 |
| [AI-EDU-LAB/E-EVAL](https://github.com/AI-EDU-LAB/E-EVAL) | 33 | **No payload.** Chinese K12 LLM education-evaluation benchmark — APAC's own evaluation asset, ungranted |
| `ubco-db/LLM_education_benchmark` | 2 | **No payload** |
| `OpenEduTech/EduPerf` | 6 | **No payload**; last updated November 2022 |
| `National-Tutoring-Observatory/National-Tutoring-Observatory.github.io` | 0 | **No payload** — and it is a *funded grantee's* only substantive repo (see gap updates below) |

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
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 43 | MIT (`main/LICENSE`, © 2026 Arnaud Guiovanna) | **The pedagogy engine as a side-car — the most architecturally significant row in this table.** Go, v0.6.1, 456 commits, 6 forks. Its own description: *"An open-source MCP server that turns any LLM into an Intelligent Tutoring System. 50 years of cognitive science, MIT licensed."* Implements **BKT** mastery estimation, **FSRS** spaced repetition, prerequisite-based paths, assessment-evidence tracking, misconception memory and session narrative, exposed through `get_next_activity` / `record_interaction`. **Added to this shelf in the seventh pass — see below.** |
| [Yuanpeng-Li/gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) | 8 | MIT (`main/LICENSE`, © 2026 Yuanpeng Li) | **The only MCP over a real production grading system.** Python, 82 commits, 6 forks. **39 tools** (24 read-only, 11 write-enabled, 4 local-cache), 3 resources, 7 prompts: batch grading with preview-first safety, rubric CRUD, answer-group clustering, regrade review, extension management, Canvas/Brightspace gradebook export. Small, and the strategic point is the direction — **orchestrate the proprietary incumbent, do not promise to replace it.** |
| [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) | 0 | MIT (`main/LICENSE`, © 2026 **Web Analytics Consultants Association (WACA)** and Toshiaki Ejiri) | **The human-gate reference implementation, and the row that refutes this KB's Japan gap.** 9 tools, Python, stdio. Its own description: *"The LLM client decides the grades; this server only fetches submissions and writes grades as unreleased drafts."* Writes `workflowstate=readyforreview` and **never releases a grade**; writes require `MOODLE_ALLOW_WRITE=1` **and** a non-empty `MOODLE_WRITE_COURSE_ALLOWLIST` (empty list = fail-closed, no write); every attempt, denial and success appended to a **JSONL audit log**; AI-disclosure footer appended if missing; draft state means **no student notification**. |
| [woodstocksoftware/student-progress-tracker](https://github.com/woodstocksoftware/student-progress-tracker) | — (not read this pass) | MIT (`main/LICENSE`, © 2026 Jim Williams) | Learning-analytics side-car: learner profiles and enrolments, assessment results, **mastery computed per topic**, learning-gap detection, focus-area recommendation, question-level telemetry. The analytics stage P3 specifies. |
| [54yyyu/school-mcp](https://github.com/54yyyu/school-mcp) | — | **NONE** — MIT claimed in the README only | **Do not use as-is.** Canvas **and** Gradescope in a single server, which is the shape a student-facing agent actually wants. **Independently re-probed this pass: no `LICENSE` payload on 2 branches × 6 filenames**, confirming an earlier pass's flag. The README's "MIT" is not a grant. **Cheapest high-value upstream contribution on this shelf: ask for a `LICENSE` file.** |

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

**Seventh pass of 2026-10-06 — that instruction was carried out, and the table
above grew by five rows.** Sweeping by function rather than vendor name returned
the **tutoring-engine** function (`tutor-mcp`), the **grading** function
(`gradescope-mcp`, `moodle-grading-mcp`) and the **analytics** function
(`student-progress-tracker`) — three shelves no vendor-name sweep could have
reached, because none of those servers is named after an LMS. **Four of the five
are MIT from payload; the fifth claims MIT in a README and has no grant.** Still
unswept: **library** and **video**. And the function with the sharpest commercial
edge, **proctoring**, was swept and came back empty of anything licensed — see
the new declared gap at the end of this file.

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
  unchanged, and now searched by name.**
  **⚠️ ALL FOUR CLAUSES NOW SUPERSEDED. India and ASEAN were refuted in the
  fifth pass (table at the end of this file); Japan and Korea in the seventh.**
  This bullet is left standing because it was wrong on all four and the shape of
  the error is worth keeping: every refutation came from a **new channel**, never
  from a deeper sweep of the old one.
  Original text follows. This pass queried those four
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

## Gap updates from the seventh pass of 2026-10-06

The native-language channel and a consistency sweep of this file against
`agents/trending.md`. **Two of the three corrections below are this file
disagreeing with its own trending log, not new research** — which is the finding.

| Gap as recorded above | State after the seventh pass |
|---|---|
| "No **Japan**-origin permissive education project found in any channel" | **REFUTED, and it was already refuted before this pass ran.** [toshieji/moodle-grading-mcp](https://github.com/toshieji/moodle-grading-mcp) is **MIT**, read from payload, © 2026 **Web Analytics Consultants Association (WACA)** and Toshiaki Ejiri — a named Japanese professional body, with a Japanese operations manual (`OPERATIONS-ja.md`) in-tree. It was probed and recorded in `agents/trending.md` by an earlier pass. **This file kept asserting the gap for several passes after its own KB had disproved it.** |
| "No **Korea**-origin permissive education project found in any channel" | **REFUTED on assets, STILL OPEN on agents.** [yongsoojoo/esd2026-agent-workflow](https://github.com/yongsoojoo/esd2026-agent-workflow) — MIT code + CC BY 4.0 docs, **Kookmin University**, 0★ / 4 commits — is course material, not an agent. See the seventh-pass section above for why the distinction is kept rather than smoothed over |
| "Mother-tongue AI is a **two-region** capability" (`intel/trends.md` trend 21, sixth pass) | **FALSIFIED. It is at least three.** ASEAN has a permissive language layer across **Vietnamese, Thai, Malay and Indonesian** — see `repos/foundations.md`, seventh pass. The sixth pass searched for sovereign **models** (and correctly found SEA-LION unlicensed); it never searched for language **toolkits** |
| "No shippable permissive evaluator of tutoring quality" (fourth pass) | **STILL OPEN, and unchanged.** `tutor-mcp` (MIT, 43★) is now shelved and implements BKT + FSRS + misconception memory, but it **drives** tutoring; it does not **score** it. The four pedagogy-evaluation instruments remain licensed as content or not licensed at all |
| "No LATAM-origin permissive education project" | **Unchanged this pass** — the native-language channel added Japanese, Korean, Arabic and Bahasa/Thai/Vietnamese, not Spanish or Portuguese, which the fourth pass had already used. `LabSirius/TutorIA` (MIT, Colombia, every code path 404) remains the state of the art |

### A new declared gap, from the function-scoped channel

**There is no permissive open-source exam proctoring agent.** This pass searched
the proctoring-plus-grading function directly — the one function-scoped shelf
the third pass had flagged as unswept — and the single substantial candidate,
[biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent),
has **no `LICENSE` payload**. The shelf otherwise holds only **Safe Exam Browser**
(recorded in `repos/trending.md`), which is a lockdown browser rather than an
agent.

**This gap now has a regulatory edge that makes it commercially sharp.**
Vietnam's **Decree 33** (in force 2026-08-15) classifies AI that *"monitors and
analyses learner behaviour with biometric data"* as high-risk, and EU Annex III
point 3 covers exam and behaviour monitoring. So the only category of proctoring
that is sellable in either regime is one whose decisions are **local, explainable
and human-gated** — which is precisely what the unlicensed candidate above
describes itself as being. **The design is right, the grant is missing, and no
competitor holds the space.** Ranked second to P17 (oral reading fluency) as a
build opportunity.

### The method note for this pass

The fifth pass's lesson was *change the channel when a gap persists*. The sixth
pass's was *change the layer*. This pass adds a third, and it is not about
discovery at all: **audit the shelf against the log before searching for anything
new.** Two of this pass's three corrections cost nothing but a `grep` — the
evidence was already in the tree, written by an earlier pass, and contradicted by
the file a reader would actually open. **A KB that only grows forward accumulates
contradictions at exactly the rate it accumulates findings.**

## The CAi UC holder warning — read this before vendoring EduFlow, CPU-Benchmark or OnlyUs

The three Chilean rows added in the eighth pass come from **HaCAIthon 2026**, run
by **CAi UC** (*Centro de Alumnos de Ingeniería*, Pontificia Universidad
Católica de Chile). The event's rules require, as a condition of being eligible
for evaluation:

> All projects must be released under an **OSI licence** (MIT, Apache 2.0 or
> GPLv3 recommended), with a **`LICENSE` file at the repository root**.

That rule worked: **20 team repositories, 19 MIT and one AGPL-3.0**, created in a
single eight-hour event. As a **channel** that is the most valuable thing the
eighth pass found — see `intel/market.md` and `repos/trending.md`.

**But every team repo's MIT payload reads `Copyright (c) 2026 CAi UC`** — the
organiser, not the authoring team. The grant is **inherited from the base
template**, not issued by the people who wrote the code. By this KB's own
`p184` rule — *the holder is the cheapest signal that a licence was inherited
rather than granted* — all 20 are flagged.

**What that means in practice.** Whether a student federation's template
copyright validly covers code written by independent teams during an event is a
**question for counsel, not for a probe.** So:

- ✅ **Read them, benchmark them, and copy the design** — EduFlow's offline-sync
  core in particular.
- ✅ **Cite them** as evidence that the LATAM licensing gap is fixable by rule.
- ❌ **Do not vendor them** into a client deliverable until the holder is
  cleared with CAi UC and the authoring team.

The organisers' own showcase repository, `caiuc/proyectos-hacaithon-2026`, has
**no `LICENSE` payload at all** — the mandate bound the teams and not the
vitrine, which is worth knowing before citing the event as a model of hygiene.

## Gap updates from the eighth pass of 2026-10-06

Channels: the **`docs/` directory** as a probe target, and the
**institutional-event channel**. **34 repository targets probed; 31 resolved** — `AngelitUX/EstudiaUni`, RACHEL and Latam-GPT did not resolve and are recorded as unverified rather than as findings.

| Gap as recorded above | State after the eighth pass |
|---|---|
| "No LATAM-origin permissive education project" — *the firmest finding in this KB* | **FULLY REFUTED, and now precisely resized.** Origin, licence and design are all refuted: **EduFlow** (MIT, PUC Chile) has **running code**; **TutorIA** (MIT, UTP Colombia) has a **13-page requirements specification**; **BERTimbau** (`neuralmind-ai/portuguese-bert`, MIT, **886★**, NeuralMind, Brazil) is a real Brazil-origin language asset with adoption. **What survives is maturity alone** — see the replacement gap below |
| "TutorIA is scaffold only / every code path 404s" | **CORRECTED — see the block above.** The code claim holds and is explained (`.gitkeep` in six directories); the `docs/` directory was never probed and holds the deliverable. **Third instance of the probe-vocabulary failure mode**, after the sixth pass's layer error and the seventh pass's noun error |
| "No shippable permissive evaluator of tutoring quality" (fourth pass) | **STILL OPEN on automated evaluation, PARTLY ANSWERED on protocol.** TutorIA's **RNF-09** specifies pedagogical review by **≥2 subject-expert teachers per subject before launch**, under MIT. That is a human quality gate, not an evaluator; the gap as written is unchanged, but the thing an engagement needs *first* now exists in citable form |
| "Mother-tongue AI is a two-region capability" (trend 21, falsified to three in the seventh pass) | **FOUR regions on capability, TWO on licensing.** LATAM has the capability — AmericasNLP corpora for Aymara, Nahuatl and Quechua, ASR for Quechua, Guaraní, Bribri, Kotiria and Wai'khana, MT for Peru, T5 for 10 indigenous languages — and **ten of twelve probed repositories in that layer carry no `LICENSE` payload**, including **all four probed AmericasNLP editions (2021, 2022, 2023, 2024)** — whose 2024 edition includes a shared task called *"Creation of Educational Materials for Indigenous Languages"*. The claim must now be split: *capability* is four regions, *redistributable* capability is still two |
| "MEA is the only region with zero shippable permissive education assets, and the constraint is licensing hygiene" (seventh pass) | **The diagnosis is confirmed and is no longer unique to MEA.** LATAM's indigenous-language layer has the identical shape: funded, published, benchmarked, ungranted. **And the eighth pass found the remedy** — a submission rule in an event's terms produced 20 licensed repositories in 8 hours (see the CAi UC block above). Cheaper and more prospective than filing `LICENSE` issues one repository at a time |
| "No permissive open-source exam proctoring agent" (seventh pass) | **Unchanged — not re-probed this pass.** The seventh pass's function-scoped sweep stands |

### The replacement LATAM gap, stated so it can be falsified

**There is no LATAM-origin permissive education product at production maturity.**
Not origin, not licence, not architecture — **maturity**, and nothing else:

- `LabSirius/TutorIA` — MIT, institutionally backed, **specification only**, 4 commits.
- `caiuc/equipo-19` (EduFlow) — MIT, **running code**, but an 8-hour build at 1★ with a flagged holder.
- `neuralmind-ai/portuguese-bert` — MIT, **886★ and genuinely adopted**, but a language model, not an education product.
- Four further LATAM education repositories found this pass and confirmed to exist (`Dreathward/sistema-de-aprendizaje-en-linea`, `InkuA-Pasantia/Proyecto-web-educativa`, `luisllacuaperez/PROYECTO-IA`, `AprendizajeProfundo/Diplomado`) — **none has a `LICENSE` payload.** A fifth search hit, `AngelitUX/EstudiaUni` (Chile), **did not resolve on any probe** and is excluded from the count rather than reported as unlicensed.

**So the LATAM engagement posture changes.** For four passes the honest line to a
client was *"nothing exists upstream in the region; we build."* The accurate line
now is: **"the region has published the design and the licence, not the
product"** — which makes a LATAM engagement a *productionisation* engagement with
citable local provenance, and makes the Universidad Tecnológica de Pereira and
PUC Chile named partnership leads rather than absences.

### A new declared gap, from the licence-scope channel

**The `LICENSE` payload — this KB's verification standard for eight passes — is
necessary and not sufficient for any repository whose value is data, audio,
corpus or model weights.**

[Llamacha/IWSLT2023_Quechua_data](https://github.com/Llamacha/IWSLT2023_Quechua_data)
serves a complete **Apache-2.0** text from `main/LICENSE`. Its README's licence
section says the audio is *"property of Siminchikkunarayku and Llamacha"* and
that the work is licensed **CC BY-NC-ND 3.0** — **NonCommercial and NoDerivs**,
which is unusable in commercial client work. The Apache file plausibly covers
the scripts; the data, which is the only reason to clone it, does not.

This is a **third distinct licence trap**, after `p184` (holder foreign to the
project) and the seventh pass's self-contradicting file: **a correct, complete,
unambiguous licence file applied to the wrong scope.** A reviewer following this
KB's own documented method gets a permissive answer and ships a violation.

**Verification method, updated to three points:** read the **payload**, read the
**asset-scope statement** in the README, and check the **holder**. Treat the
asset-scope statement as controlling for the asset. All three are cheap; any one
alone is wrong somewhere in this pass's findings.

### Also recorded: the regional flagship is not open source

**Latam-GPT** (CENIA Chile, launched February 2026, 60+ institutions across 15
countries, Llama-3.1-70B base, ~8 TB of regional data, ≈US$550k) is released
under the **Llama 3.1 Community License Agreement, © Meta Platforms** — **not
OSI-approved**, carrying an Acceptable Use Policy and the 700-million-MAU clause
that requires a separate licence at Meta's sole discretion. The EC's Open Source
Observatory, Brookings and the trade press all describe it as *"open source"*.
**It is open-weights under a bespoke corporate licence**, which is a different
commercial object: usable and valuable for Spanish and Portuguese grounding,
**not relicensable, not presentable to a client as open source**, and it inherits
Meta's AUP into the client's product.

**Provenance caveat.** The licence-to-Latam-GPT link is **single-source** —
`huggingface.co`, `latamgpt.org`, `interoperable-europe.ec.europa.eu` and
`opensourceforu.com` are all **EGRESS_BLOCKED** here (4/4), so the model card
was **not read**. The Llama 3.1 licence's properties are independently confirmed
from the OSI's published position. **Confirm the model card before any client
deliverable.**

### The method note for this pass

Seven passes probed repositories for **code** and for **licences**. This pass
probed one for a **specification** and found a 13-page document in a repository
this KB had written off — the fourth version of the same lesson: **change the
channel, change the layer, change the noun, and now change the file type.** A
project that publishes its design before its code is invisible to a code-shaped
probe, and in academic and ministry-funded work that is the *normal* publication
order.

The harder correction is to this KB's own standard. **The payload channel is not
ground truth.** It is wrong about `Llamacha` in the permissive direction, silent
about `caiuc`'s inherited holder, and it says nothing at all about the
label-versus-grant gap that makes Latam-GPT look open. Eight passes of
"read it from the payload" bought real accuracy and has now been shown to have a
ceiling.

## Gap updates from the ninth pass of 2026-10-06

Channel: the **funder and procurement channel** — philanthropic RFPs, state
education-agency procurement rubrics, district solicitations — which the eighth
pass declared necessary and which this KB had never swept. Plus the
**education-ministry engineering org** as its government twin.

**Evidence tiering applies to this block.** Repository and licence facts are
**Tier 1 (payload-verified)**. Every funder, dollar and procurement fact is
**Tier 2 (corroborated search summaries)** — 14 of the hosts carrying the primary
documents are **EGRESS_BLOCKED** here, including `k12-ai-infrastructure.org`,
`digitalpromise.org`, `unu.edu`, `arxiv.org` and `cosn.org`. **No RFP document
was read.** Confirm before any client deliverable.

| Gap as recorded above | State after the ninth pass |
|---|---|
| "No permissive open-source exam proctoring agent" (seventh pass, carried unchanged through the eighth) | **REFUTED on existence, RESIZED to maturity.** 204 MIT-licensed repositories match; **four verified from payload** (47★/36★/22★/18★ — see the shelf above). The framework-grade one, `lebmatter/exampro` (72★), is **ungranted**. The true gap is **no permissive proctoring agent at production maturity** |
| "No shippable permissive evaluator of tutoring quality" (fourth pass; re-declared in the eighth) | **STILL OPEN TODAY — and now funded, dated and licence-floored.** Measured: `tutoring quality evaluation benchmark license:apache-2.0` returns **0 repositories** (6 Oct 2026). But the **$26M K-12 AI Infrastructure Program** (Digital Promise + Gates Foundation) has **twelve named funded projects** under a floor of **"at least as permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)"**, and at least three land directly on this gap. **The gap now has an arrival window (2027), not just an absence** |
| "The oral reading fluency agent does not exist" (sixth pass) | **UNCHANGED today, and specifically funded.** Cohort 1 of the programme includes **National Tutoring Observatory / Cornell University** (PI Allison Koenecke) — *"Open Leaderboards for Benchmarking Automated Speech Recognition in Educational Contexts"*, 6–12 months from 29 Jun 2026. Measured: the org has **no code** — two repos, the substantive one a website at **0★ with no payload** |
| "RACHEL — repository path not established" (eighth pass) | **RESOLVED, and the verdict is: not shippable.** The org is **`rachelproject`**; `contentshell` **is** the RACHEL CMS. **No licence payload** across 8 filenames × 2 branches; the README's only grant statement is **"Creative Commons - BY, SA, NC"** — a **content licence applied to PHP software, with NonCommercial.** Kolibri (**MIT**, re-confirmed from payload) remains the platform answer; RACHEL is prior art to cite, not code to ship |
| "MEA/LATAM/APAC: built, published, benchmarked, ungranted" (seventh and eighth passes) | **Now confirmed in a third region from a fourth channel.** `AI-EDU-LAB/E-EVAL` (**33★**, Chinese K12 education evaluation benchmark) has **no payload**. The failure mode is not regional — it is what unfunded published work looks like everywhere |
| "North America's general-language channel is saturated; the next trend must come from district RFPs, state procurement portals or vendor filings" (eighth pass) | **TWO OF THREE SWEPT, and the channel paid immediately** — see `intel/market.md` (North America) for the procurement rubrics and `intel/trends.md` trends 25–26. **Vendor filings remain unswept** and are a distinct channel |

### The headline: this KB's oldest gap is being bought

**The K-12 AI Infrastructure Program** — **$26M**, multi-year, led by **Digital
Promise** with **Learning Data Insights**, **DrivenData**, the **Massive Data
Institute at Georgetown** and **Catalyst @ Penn GSE**; funded by the **Gates
Foundation**, which manages review and monitoring directly. Launched **3 Nov
2025**, first cycle opened **4 Feb 2026**.

Its licence condition is the reason it belongs in this file:

> All funded developments must be released under a licence **at least as
> permissive as CC-BY-4.0 (content) or Apache-2.0 (code/models)** — with
> **Apache-2.0** recommended for software and code *including evaluations, models
> and applications*, and **CC-BY** for datasets and knowledge products.

**Twelve projects are already funded.** Cohort 1 (29 Jun 2026): **Learning
Equality** (science-misconception benchmark), **Princeton** (simulated student
models), **National Tutoring Observatory / Cornell** (ASR leaderboards for
education), **Stanford** (KB-TutorBench, multimodal formative-assessment
dataset). Cohort 2 (21 Sept 2026): **eight** awards focused on **formative
assessment** plus math, literacy and writing, outputs stated to be **openly
licensed**; one named at Tier 2 — **MMSA & TERC** (*A Multimodal Dataset for
AI-Enhanced Formative Assessment*).

Separately, the **EDU AI** RFP — **up to $8M**, one award, closed **31 Jul
2026**, work from **Nov 2026** over 30–36 months — funds open-source
education-specific model(s) for **K-12 math tutoring as effective as human
experts**.

**One grantee is already this KB's recommendation. Learning Equality maintains
Kolibri** (`learningequality/kolibri`, **MIT**), the offline-first platform the
eighth pass selected. The organisation holding this KB's platform answer is now
funded to produce an openly-licensed benchmark — **a named partnership lead with
an existing permissive track record**, not a cold approach.

### A new declared gap: the funded pipeline is not a shelf yet

**Nothing from the twelve funded projects is publicly available.** Measured on
6 Oct 2026: `KB-TutorBench` → **0 repositories**; `learningequality` filtered on
`benchmark` → **0 repositories**; the National Tutoring Observatory org → a
website at 0★ with no payload.

So the engagement line changes shape without closing: **"the permissive
evaluation layer is funded and lands through 2027; today you build the harness,
and you design it so Apache-2.0 benchmarks drop in as they ship."** Pattern
**P23** in `compose/patterns.md` is that design. The highest-value single lookup
for the next pass is **the seven unnamed cohort-2 grantees** — each is an
Apache-2.0-or-better artefact with a named owner arriving inside twelve months.

### The method note for this pass — the probe set had a spelling bug

**Three of the six MIT grants on the new DfE shelf are in a file named
`LICENCE`**, the British spelling.

**The precise failure is worse than a missing filename: the check existed and was
never run.** Pattern **P22**'s licence gate, written in the eighth pass, *does*
list `LICENCE` in check 1. But every sweep this KB has recorded — including the
eighth pass's own 34-target probe — enumerates only `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING` and `license.txt`. **The gate documented the British
spelling; the sweeps never executed it.**

With the old set, this pass would have recorded
`DFE-Digital/apply-for-teacher-training` (38★),
`get-into-teaching-app` (25★), `register-trainee-teachers` (12★) and
`get-information-about-schools` (9★) as **four ungranted government
repositories**, and written another paragraph about ministries that publish code
without licensing it. **All four are MIT.**

That is the **seventh** instance of one failure mode: wrong channel → wrong layer
→ wrong noun → wrong file type → wrong scope → wrong assumption that a payload
exists at all (RACHEL) → **wrong spelling**. Every one produced a false negative
that read as a regional or categorical absence.

**Two corrections follow.** The probe set now includes `LICENCE`, `LICENCE.md`,
`LICENCE.txt` and `COPYRIGHT`; every negative in this pass was re-run against
them and all seven survived. And **earlier passes' "ungranted" conclusions were
produced by a query that could not have found a British-spelled grant** — they
are suspect until re-probed, which matters most for the MEA, Commonwealth and
ministry-adjacent repositories where that spelling is the norm.
