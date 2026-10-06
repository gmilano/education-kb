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

## Gap updates from the tenth pass of 2026-10-06

This pass did not sweep outward for new agents. It **re-probed the 41
repositories this KB has recorded as ungranted**, because the ninth pass ended
by declaring its own back catalogue suspect:

> *"Earlier passes' 'ungranted' conclusions were produced by a query that could
> not have found a British-spelled grant — they are suspect until re-probed."*

They have now been re-probed. **41 repositories × 10 filenames × 2 branches**
(`LICENCE`/`LICENSE`/`licence`/`license`/`COPYING`, with `.md` and `.txt`
variants, on `main` and `master`), all via `raw.githubusercontent.com`, and the
probe was validated on **6 known-payload controls first — 6 of 6 resolved**,
including two British-spelling controls and three repositories whose licence sits
on `master`.

### The result: 1 flip in 41, and the spelling was not the cause

| Re-probe outcome | Count |
|---|---|
| Repositories re-probed | **41** |
| Flipped to granted | **1** |
| Confirmed ungranted under all 20 URLs | **40** |
| Flips attributable to the British `LICENCE` spelling | **0** |

**The ninth pass's correction generalised to nothing.** `LICENCE` is a house
style at one UK government organisation, not a defect in this KB's reach. It
stays in the probe set — it costs one URL per repository and two controls prove it
works — but it is a **special case, and this KB recorded it as a general
discovery.** That is corrected here.

**The defect that was general is the branch name.** The single flip resolved on
`master/LICENSE`: American spelling, non-default branch. Three of six controls sit
on `master` too. No pass before this one varied the branch. **Eighth failure
mode: wrong branch.**

### The correction to the catalogue

| Repo | Was | Is | Read from |
|---|---|---|---|
| [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) | recorded ungranted | **MIT** | `master/LICENSE` |

Caveat that travels with it: the MIT text names **`theopenem`** as copyright
holder, and [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET)
serves a byte-identical `README.md` (md5 `110b2e3439d86b6055821de382d90d61`) and
byte-identical licence. **One asset, two addresses** — pin the `theopenem` copy,
whose owner matches its copyright line. The fork direction is **not established**:
`github.com` returns 403 to `curl` here and the fork banner is absent from the
rendered page this environment receives.

### The row this pass adds — one, and why only one

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| prosody | [qazasd2518995/prosody](https://github.com/qazasd2518995/prosody) | **MIT** (`main/LICENSE`, **full text read**) | 0 | Oral reading assessment from speech. Aligns recorded audio to reference text at word level; reports accuracy and word error rate, speaking rate in WPM, misread/omitted/inserted words, and a fluency score from pause pattern and pace. Whisper for ASR (`PROSODY_ASR_MODEL`), Levenshtein alignment, Groq API for transcription. Python, **1 commit**, 0 forks, not a fork. Targets language learning and speech-language pathology. |

**One row, and the reason is the finding.** `oral reading fluency assessment
speech` returns **two repositories on all of GitHub**. The other,
[mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2)
(TypeScript, 0★), has **no payload under any of the 20 URLs** — the repository
exists, the grant does not. That is the entire denominator, and padding it would
destroy the only useful thing about it.

### The method finding: GitHub's licence field manufactures absences

`prosody` is listed in GitHub's repository search as **"License: Not
specified."** Its payload is a **complete, unmodified MIT licence**, read in full
this pass, body unqualified, `Copyright (c) 2026 Justin`.

This is the **ninth failure mode**, and it is the most consequential one yet
because it attacks the instrument this KB uses to *declare gaps*. A
licence-filtered search cannot return a repository GitHub believes is unlicensed.
Three such searches were run this very pass and all three returned zero. Those
zeros remain the best available measurement, but their meaning has changed:
they are **absence as GitHub's licence index sees it**, not absence.

Every gap in this file that rests on a `license:` filter inherits that caveat.

### What this does to the oral reading fluency gap (sixth pass)

Restated, because the old wording was wrong in the expensive direction:

- **Old:** *"an oral reading fluency agent does not exist."* Refutable by one
  repository, and now refuted by one.
- **New:** **two repositories exist in the whole of GitHub; one is MIT with a
  single commit; neither has a single star.** The *capability* gap is real and
  the shelf is empty for practical purposes — but it is empty in a way a client
  engagement can price, and `prosody` is a starting point rather than nothing.

And the funded answer now has a name. **Harvard University (Ying Xu)** is a
Cohort 2 grantee of the $26M K-12 AI Infrastructure Program for **"OpenLiteracy:
An Open-Source AI Infrastructure Suite for Advancing Speech Foundation Models for
Early Word Reading Assessment and Instruction"** (Tier 2, search-summary
corroborated). It lands on this gap exactly. **GitHub returns 0 repositories for
`OpenLiteracy`** (Tier 1, measured this pass) — funded, named, not shipped.

### The method note for this pass

Nine passes looked outward; this one audited the KB against itself, and the audit
cost it two of its own conclusions — the generality of the spelling fix, and the
wording of the oral-reading gap. Both corrections came from re-running rejections
rather than from new search, which is a cheaper channel than any this KB has used
and the only one that can find a **false negative**.

The limit is worth stating: **no primary document was read this pass either.**
Nine further hosts were attempted and all nine returned `EGRESS_BLOCKED`
(`digitalpromise.org`, `www.coe.int`, `rm.coe.int`, `www.prnewswire.com`,
`www.gse.upenn.edu`, `www.eunews.it`, `www.sec.gov`, `ess.iesalc.unesco.org`,
`openai.com`) — including three **syndicated mirrors** tried specifically to route
around a blocked primary host. With the ninth pass's fourteen, that is **23
distinct hosts, zero reachable.** `github.com` and `raw.githubusercontent.com` are
the only origins this environment serves, which is why this pass spent its budget
on payload work.

## Added in the eleventh pass of 2026-10-06 — the evaluation tier, and three ITS agents

New channel this pass: **the GitHub REST search API**, reachable through this
session's GitHub MCP server. Ten previous passes probed it with an HTTP client
(`curl https://api.github.com/search/repositories` → **403**, *"sessions are bound to
their configured repositories"*) and concluded it was blocked. It is not — the MCP
path returns `total_count`, `stargazers_count`, `default_branch`, `fork`, `archived`
and `license.spdx_id`. Every licence below was still read from the repository's own
payload on `raw.githubusercontent.com`; the API supplied the metadata and, crucially,
**the real `default_branch`** to probe.

**8 rows added. 7 are reinstatements of assets dropped by this repository's reset
earlier the same day** (see the gap-update section below) — which is why the count is
high and why none of them is a discovery.

### The evaluation tier — permissive, government-built, and what P23 was told to wait for

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| Inspect | [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** (`main/LICENSE`) | **2,945** | LLM evaluation framework from the **UK AI Security Institute** (`aisi.gov.uk`). Prompt engineering, tool use, multi-turn dialog and **model-graded evals**; scorers and elicitation techniques extend from separate Python packages. 779 forks, 348 open issues, pushed 2026-10-06. **The harness every evaluation pattern in this KB needs, and the single highest-starred MIT asset on the evaluation shelf.** |
| Moonshot | [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** (`main/LICENSE.md`) | 355 | Modular tool to **evaluate and red-team any LLM application**, from the **AI Verify Foundation** (the Singapore IMDA AI-testing community). Benchmarking + red-teaming in one surface. 72 forks, pushed 2026-10-06. **The APAC-origin half of the evaluation tier, and the only permissive red-teaming harness here.** |
| tutoreval | [shivanireddyk/tutoreval](https://github.com/shivanireddyk/tutoreval) | **MIT** (`main/LICENSE`, 1,074 B) | 0 | *"Measuring whether an AI tutor teaches, rather than whether it answers."* Deterministic pedagogical evaluation with a hand-labelled benchmark. **The only MIT-licensed pedagogical benchmark found — and it is one author's project.** Listed because the licence is the scarce thing here, not the stars. |

### Intelligent tutoring system agents

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| GenMentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | ⚠️ **CC0-1.0** (`main/LICENSE`, 7,048 B, read in full) | **131** | *"LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System"* — **WWW 2025 Industry Track, Oral.** Skill-gap identification → learner modelling → tailored content generation. TypeScript, 22 forks, updated 2026-10-04. **Highest-starred purpose-built ITS agent framework in this KB.** See the CC0 warning below — it is permissive on copyright and **silent on patents**. |
| Open Learning AI Tutor | [mitodl/open-learning-ai-tutor](https://github.com/mitodl/open-learning-ai-tutor) (live **fork**) · upstream [MIT-OL-AI-Tutoring/Open_Learning_AI_Tutor](https://github.com/MIT-OL-AI-Tutoring/Open_Learning_AI_Tutor) | **MIT** (`main/LICENSE`, md5 `cb5f766beb2db853d5b69328279ccb1b` on **both**, © 2024 Romain Puech) | 1 (fork) · 0 (upstream) | **MIT Open Learning's** AI tutor backend — the pedagogical engine behind `learn-ai.ol.mit.edu` (paper: arXiv 2410.03781). **Use the `mitodl` fork**: it was pushed 2026-10-03 and its README points at MIT's production domain, while the upstream has been still since 2025-02-26. ⚠️ The maintained copy is a **fork**, so fork-excluding search cannot see it. |
| MITS | [Siesher/MITS](https://github.com/Siesher/MITS) | **MIT** (`main/LICENSE`) | 3 | Math ITS: **Socratic** multi-agent STEM tutor over an RL-trained Qwen3.5-9B. FastAPI + Next.js. The clearest small example of Socratic-constraint-as-architecture rather than as a prompt. |
| Intellicode | [Redomic/intellicode-backend](https://github.com/Redomic/intellicode-backend) | **MIT** (`main/LICENSE`) | 5 | Adaptive learning platform **bridging a classical ITS with coordinated LLM agents** — the hybrid, not a chat wrapper. Python. Frontend at `Redomic/Intellicode-frontend` (MIT per payload probe pending; 1★). |

### The Python LTI 1.3 row this KB declared missing eight hours earlier

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| PyLTI1p3 | [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (`master/LICENSE`, 1,070 B) | **138** | LTI 1.3 Advantage tool implementation for Python with **Django and Flask** adapters. **The canonical Python LTI 1.3 library.** ⚠️ Last push **2024-08-18** — stable and widely used, not actively developed. Branch is `master`. |

### Measured this pass and NOT usable — read this before quoting a benchmark in a proposal

Four tutoring-evaluation instruments exist and are real work by serious
institutions. **Not one carries an OSI-approved licence.** This table is the whole
reason pattern **P27** exists.

| Repo | ★ | What the payload actually says | Verdict for client work |
|---|---|---|---|
| [Khan/tutoring-accuracy-dataset](https://github.com/Khan/tutoring-accuracy-dataset) | **57** | Custom **"Evaluation Dataset License"** (`main/LICENSE`, 2,690 B, read in full). Grants internal use/copy/modify/merge **solely to evaluate AI models**. Prohibits **re-distribution, publication, use for model training, and any production use**; no sublicensing; clause 4 makes it **viral** over any combined dataset. Clause 3 expressly permits evaluating **products intended for commercial use** and **commercial use of the insights gained**. | ⚠️ **Borrow, never ship.** Usable to measure a client's tutor; the findings are yours. It must not enter a deliverable, a training set, or any dataset you hand over. |
| [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 43 | **No licence payload** under 10 filenames × 2 branches. README carries a **CC BY 4.0 badge** *and* body text saying **CC BY-SA 4.0**. Two incompatible claims, nothing authoritative to adjudicate. **ETH Zurich**, EMNLP 2025 Oral. | 🔴 **Treat as ungranted.** The ShareAlike reading would attach to derivatives. |
| [Yunfeng-Wan/CSTutorBench](https://github.com/Yunfeng-Wan/CSTutorBench) | 2 | **CC BY-NC-4.0** (`main/LICENSE`). 2,970 multi-turn QA dialogues from real university forums. | 🔴 **NonCommercial — out.** |
| [ScottDaniels/labaaoom](https://github.com/ScottDaniels/labaaoom) | 1 | **BSD-2-Clause body** (`master/LICENSE`, 2,266 B) behind a preamble: *"Contributions to this source repository must be published with the same license."* Android oral-reading-fluency app, © 2017, last touched 2024-12-12. | ⚠️ **Usable.** The reciprocity clause binds **contributions back**, not derivatives; the two-clause body governs redistribution. Flag it in the licence register and do not vendor it as "BSD" without the qualifier. |

### Measured and still ungranted

| Repo | Probe | Result |
|---|---|---|
| [mendezjerick/ReaDirect-V2](https://github.com/mendezjerick/ReaDirect-V2) | re-probed on its **real** `default_branch` — `deployment/playstore`, not `main` or `master` | **No payload.** The tenth pass's verdict was right; its two-branch method could not have established it. |
| [Kaylazagelbaum/ORF_Calculator_6th](https://github.com/Kaylazagelbaum/ORF_Calculator_6th) | `main`, 6 filenames | **No payload.** 0★, HTML, created 2026-08-25. |
| `imsglobal/caliper-python` · `concentricsky/badgr-server` | `README.md` on `main` and `master`; search index | **404 / invisible.** 1EdTech moved Caliper to **private repositories on 2023-06-17** (notice preserved in a surviving fork). Public forks are 0★ and unmaintained. |

### ⚠️ The CC0 warning — read before vendoring GenMentor

**CC0-1.0 is a public-domain dedication, not a software licence.** For copyright it is
broader than MIT. But the instrument states that **no patent or trademark rights held
by the Affirmer are waived.** Apache-2.0 grants patent rights expressly; MIT's
"deal in the Software without restriction" is generally read as implying them. CC0
does neither.

**The rule:** CC0 components are fine in a deliverable and must be recorded in the
licence register **as CC0, not as "MIT-equivalent"**. For anything patent-sensitive —
assessment scoring methods, adaptive-sequencing algorithms, anything a client may
want to defend — prefer an Apache-2.0 component for the same function if one exists.

## Gap updates from the eleventh pass of 2026-10-06

### The reset of 2026-10-06 dropped 172 repository addresses, and the tenth pass re-declared one of them as a gap

This repository was reset earlier on 2026-10-06; the previous estate is preserved in
`archive/2026-10-06-pre-reset/`. Measured by extracting every
`github.com/{owner}/{repo}` address from the eight live KB files and from the nine
archived ones:

| Address set | Distinct `owner/repo` |
|---|---|
| The eight live KB files | **627** |
| The nine pre-reset archive files | **678** |
| In the archive, absent from the live KB | **179** |
| of those, not real repositories (placeholders and negative controls) | 7 |
| **Real repository addresses dropped** | **172** |

The cost is not hypothetical. The tenth pass declared, eight hours before this one:

> *"**No Python LTI 1.3 library exists on the permissive shelf.** [...] Most AI
> tutoring code is Python. Searched, not found, recorded as a gap — and as a
> candidate contribution."*

`archive/2026-10-06-pre-reset/` contains `dmitry-viskov/pylti1.3` — **MIT, 138★** —
with a note that the KB *"already had it registered from an earlier pass."*
**The gap was refuted by this repository's own archive before it was declared.**

**The rule this adds, and it needs no external instrument:** after a reset, a gap
claim is not publishable until it has been diffed against `archive/`. This is the
**eleventh failure mode** in this KB's list.

**Reinstated this pass: 17 addresses**, 8 of them as rows above (`inspect_ai`,
`moonshot`, `pylti1.3`, `gen-mentor` is new, `mitodl/open-learning-ai-tutor`,
`tutoreval`, `MITS`, `intellicode-backend`) and 9 in `verticals/solutions.md` and
`repos/foundations.md`. **~155 remain unrecovered**, in clusters a later pass should
take one at a time: the **Ed-Fi** stack, **LibreTexts** and **OpenStax**, the
**Nextcloud** AI apps, the **xAPI/LRS** tier, the ~16-plugin **Moodle AI** cluster,
and the ~20-server **education MCP** cluster.

### The method note for this pass — three kinds of zero, all of them wrong

| What produced the zero | Why it was not an absence |
|---|---|
| A **ranked web surface** (`WebSearch`, `github.com/search` rendering) | Ranked, truncated and cached. The REST API returns `total_count`, which is a count. Ten passes measured absences without it. |
| A **`repo:` qualifier** | **GitHub repository search excludes forks unless `fork:true` is passed.** `repo:mitodl/open-learning-ai-tutor` → 0; the same query with `fork:true` → 1, and that fork is MIT Open Learning's production tutor. **Twelfth failure mode.** |
| A **keyword-heavy or licence-filtered query** | `tutoring quality evaluation benchmark` → 0. Drop the single word *quality*: **20 results**, led by Khan Academy and ETH Zurich. The zero described the filter. |

And one correction to the probe set itself: the tenth pass fixed `main`-only probing
by adding `master`. **Two guesses is still a guess.** Read `default_branch` from the
API and probe *that*: this pass found `dev` (`learnhouse`, 2,320★), a version number
(`portabilis/i-educar`, 718★, branch `2.12`) and `deployment/playstore`
(`ReaDirect-V2`). A `main`+`master` probe reports "ungranted" about Brazil's largest
free education platform, which is **GPL-2.0**.


## Added in the twelfth pass of 2026-10-06 — the instrument that needs no API, and 4 agent rows

**New instrument this pass, and it is the durable contribution:** the eleventh pass's
method note ends *"Read `default_branch` from the API and probe *that*."* Correct — but
this pass the HTTP API answered **403** again
(*"sessions are bound to their configured repositories"*), so that instruction was not
executable through the path the note assumed. It does not need an API at all:

```
git ls-remote --symref https://github.com/{owner}/{repo} HEAD
# → ref: refs/heads/{default_branch}	HEAD
```

`ls-remote` is **plain git over HTTPS**, reachable wherever `github.com` is, and it
returns the default branch **authoritatively** rather than by guess. It also doubles as
an existence check: a repository that no longer resolves returns nothing at all. Every
branch and licence in the tables below was obtained this way and then read from
`raw.githubusercontent.com`. **Four default branches found this pass that neither
`main` nor `master` would have caught:**

| Repo | Real default branch | What a `main`+`master` probe reports |
|---|---|---|
| `Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard` | **`v6.2.0`** | ungranted — it is **Apache-2.0** |
| `moodlehq/moodle-tool_dataprivacy` | **`MOODLE_34_STABLE`** | ungranted — it is **GPL-3.0** |
| `datakind/student-success-tool` | **`develop`** | ungranted — it is **MIT** |
| `mendezjerick/ReaDirect-V2` | **`deployment/playstore`** | ungranted (as the eleventh pass found) |

A **version number**, a **vendor release-branch convention** and **`develop`** are all
in that list. The guess-set is not two names wide, and it is not enumerable — read it.

### The agent rows

| Agent | Repo | Licence (read from payload) | ★ (2026-10-06) | Branch | What it does |
|---|---|---|---|---|---|
| AI-Powered-Video-Tutorial-Generator | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | **MIT** (`main/LICENSE`, **1,070 B**) | **313** (65 forks) | `main` | Generates **illustrated video lessons** with expressive presenters, distinct voices and lip-sync, on a native timeline editor. Desktop app (Tauri/Rust + Python + React) that runs **local models** as well as cloud providers. **New to this KB** — it appears in no earlier pass. The only permissive **video-lesson generator** on this shelf, and the local-model path is what makes it usable where per-seat inference cost is the binding constraint. |
| Edu-ConvoKit | [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | **MIT** (`main/LICENSE`) | **117** (16 forks) | `main` | Stanford NLP's framework for **education conversation data**: pre-process (with participant anonymisation), annotate (talk time, student reasoning, teacher uptake), analyse. Python. This is the **measurement instrument for trend 10** — "human connection is becoming the measured outcome" — and the anonymisation step is what makes classroom audio usable under the privacy regimes in all four regions. |
| Student Success Tool | [datakind/student-success-tool](https://github.com/datakind/student-success-tool) | **MIT** (`develop/LICENSE.md`) | 8 (2 forks) | **`develop`** | DataKind's predictive-advising pipeline: identifies students at risk of not graduating and routes advisor interventions. Ships automated ML pipelines, EDA, feature engineering and explicit **bias-reduction** steps, built around transparency of model variables and an advisor **in the loop**. Python. Funded by **Google.org**; named partner **John Jay College** reports a 32% rise in senior graduation rates over two years. **North America**-placed, and the clearest permissive answer to a retention engagement. |
| EduCoder | [EduNLP/EduCoder](https://github.com/EduNLP/EduCoder) | **MIT** (`main/LICENSE`) | 3 (1 fork) | `main` | Annotation system for **classroom transcript data**: human annotation workspaces, admin assignment, and side-by-side comparison of **human versus LLM-generated** annotations with evidence notes tied to individual transcript lines. Next.js/Prisma/PostgreSQL. Pairs with Edu-ConvoKit as the labelling front end to its analysis back end. |

**Read the placement honestly.** One of these four is a traction asset (313★); the
other three are 3–117★ research-grade code. They earn rows because *classroom discourse
measurement* and *permissive predictive advising* were functions with no entry on this
shelf, and because the Stanford and DataKind rows come with named institutional
backing rather than a star count.

### The 13th failure mode — the licence filename is case-sensitive

`raw.githubusercontent.com` is case-sensitive, and a licence-filename probe is a
case-sensitive guess. This pass probed nine lowercase-conventional names
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, …) across every
recovered address and reported **13 repositories as ungranted**. Re-probed with
case variants:

| Repo | Name of the actual licence file | Real licence | What the first probe said |
|---|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **`LICENSE.TXT`** (uppercase extension) | **Apache-2.0**, 470★ | ungranted |
| [european-commission-empl/European-Learning-Model](https://github.com/european-commission-empl/European-Learning-Model) | **`license`** (lowercase, **no extension**) | **EUPL-1.2** | ungranted |

This KB's licence-failure catalogue already held *a licence hidden outside the root*
(`OS4ED/openSIS-Classic` at `docs/License.txt`, `frappe/*` at lowercase `license.txt`).
The new entry is narrower and nastier: **the right directory, the right word, the wrong
case.** `LICENSE.TXT` is two characters away from a name the probe already tried.

**`openedx/XBlock` is the row that makes this failure mode expensive.** Open edX's
platform core is **AGPL-3.0** and this KB has priced it as copyleft for eleven passes.
`XBlock` — the component and plugin SDK, the surface a studio actually writes against —
is **Apache-2.0** at 470★. A `main`+`master`+lowercase probe reports the plugin SDK of
the most widely deployed LMS in this KB as ungranted. It is permissive, and it is the
seam that lets a client-specific component be built and redistributed without
inheriting the platform's AGPL obligations. Full entry in `repos/foundations.md`.

### An independent reproduction, and a size floor that holds

This pass's payload classifier read `CaviraOSS/PageLM` (**2,000★**, 277 forks) as
**MIT** — exactly the misclassification `P411` predicted on 2026-10-05. The payload
opens with the literal MIT grant and is titled *"PageLM Community License"*:
**non-commercial only**, **redistribution prohibited**, a **revenue-sharing agreement
required** before any commercial deployment, and the licence is **revocable**. Nothing
new is claimed here — the finding is pass 123's. What this pass adds is that an
independently written classifier fell into it the same way, so the **size tell is the
load-bearing check, not the grant phrase**: this pass measured a real MIT at
**1,070 B** (`AI-Powered-Video-Tutorial-Generator`, and `pylti1.3` at the same figure)
against PageLM's 8,563 B. 🔴 **PageLM remains DO-NOT-VENDOR for any Globant
engagement**, at any star count.

### Measured this pass and genuinely ungranted — 11 addresses, after 30+ filename variants

Each probed on its **real default branch** from `ls-remote`, against both the
conventional names and the case variants above. These are absences of a grant, not
absences of a probe:

| Repo | Branch | Note |
|---|---|---|
| [CAHLR/OATutor-Content](https://github.com/CAHLR/OATutor-Content) | `main` | ⚠️ **Read this before deploying OATutor.** The *engine* (`CAHLR/OATutor`) is **MIT** and sits on this KB's core shelf. Its **content repository — the problem bank and hint trees — carries no licence at all.** The pedagogy is the asset; it is the part that is not granted. |
| [FWU-DE/schulfach-ontologie](https://github.com/FWU-DE/schulfach-ontologie) · [FWU-DE/schulart-ontologie](https://github.com/FWU-DE/schulart-ontologie) | `main` | **Germany**, FWU (the federal states' media institute). School-subject and school-type ontologies — the vocabulary a German curriculum alignment needs. Ungranted. |
| [european-commission-empl/european-digital-credentials](https://github.com/european-commission-empl/european-digital-credentials) | `master` | **EU Commission**, DG EMPL. Ungranted, while its sibling `European-Learning-Model` carries EUPL-1.2 in a file named `license`. |
| [dini-ag-kim/school-curriculum-pg](https://github.com/dini-ag-kim/school-curriculum-pg) | `main` | **Germany**, DINI-AG-KIM metadata group. Curriculum vocabulary. Ungranted. |
| [aiverify-foundation/LLM-Evals-Catalogue](https://github.com/aiverify-foundation/LLM-Evals-Catalogue) | `main` | **Singapore**, IMDA. Ungranted — while `aiverify` and `moonshot-data` in the same organisation are **Apache-2.0**. Organisation-level licence inference is unsafe even inside a government foundation. |
| [marcusgreen/moodle-tool_aiconnect](https://github.com/marcusgreen/moodle-tool_aiconnect) · [jeanlucio/moodle-local_aihub](https://github.com/jeanlucio/moodle-local_aihub) · [alvarogregori/moodle-ai-graded-assignment](https://github.com/alvarogregori/moodle-ai-graded-assignment) | `main` | 3 of the ~16-plugin Moodle AI cluster. The other 8 probed this pass are **GPL-3.0** (correct for in-tree plugins); these 3 are ungranted. `moodle-ai-graded-assignment` is the painful one — AI-graded assignments is the regulated function this KB has been hunting since the seventh pass. |
| [Kaiman-p/tutor-adaptativo-ia](https://github.com/Kaiman-p/tutor-adaptativo-ia) · [mietiainvestigacion-creator/API-EduAdapt](https://github.com/mietiainvestigacion-creator/API-EduAdapt) | `main` | **LATAM**, Spanish-language. Both ungranted. Consistent with the regional finding in `intel/market.md`: the LATAM constraint is licence hygiene, not absence of code. |

### Gone, not merely unfound — 5 addresses that no longer resolve

`ls-remote` returns nothing for these. They were live when the archive recorded them:

| Address | What it was | Consequence |
|---|---|---|
| `IMSGlobal/caliper-python` | Caliper reference implementation, Python | Confirms the eleventh pass's declared gap, with a second instrument. |
| **`1EdTech/caliper-php`** | Caliper reference implementation, **PHP** | 🆕 **Extends that gap.** The eleventh pass established that the Python implementation went private on 2023-06-17. The **PHP** one is gone too. There is no surviving public reference implementation of Caliper in any language this KB has checked. **Do not promise Caliper emission without pricing a 1EdTech membership or a clean-room build** — and now there is no second language to fall back to. |
| `concentricsky/badgr-server` | Open Badges server | Confirms the eleventh pass. The verifiable-credential half of trend 8 has no permissive server. |
| **`Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP`** | An **MCP server for the Ed-Fi SDK** | 🆕 Recorded in this repository's own archive; does not resolve now. The rest of the Ed-Fi stack is alive and **Apache-2.0** (see `repos/foundations.md`); the MCP side-car is what disappeared. If an engagement needs Ed-Fi over MCP, that is a **build**, not an adoption. |
| `junjie1005/Plataforma-IA-Educativa-Rutas-Personalizadas` | LATAM Spanish-language adaptive platform, 0★ | 🆕 **The search index still lists it; `ls-remote` cannot reach it.** A repository can be in `total_count` and not exist. The index is a snapshot, so a count from it is an upper bound — worth remembering before quoting one as a measurement. |

### The method note for this pass

| What this pass used | Result |
|---|---|
| `git ls-remote --symref … HEAD` | **The default-branch instrument.** No API, no key, reachable wherever `github.com` is. 4 non-obvious default branches found, 5 dead addresses identified. |
| `curl` on `api.github.com/search/*` | **403** — *"sessions are bound to their configured repositories"*. Same as passes 1–10. |
| `curl` on `api.github.com/repos/{owner}/{repo}` | **403**, for repositories outside this session's scope. |
| GitHub **MCP** `search_repositories` | **200 with `total_count`.** Reproduces the eleventh pass's finding: the MCP path works where the HTTP path does not. Both statements in this KB about the API are true, of different clients. |
| Payload reads from `raw.githubusercontent.com` | **200** throughout, on every branch `ls-remote` named. |

**The honest summary of the archive recovery:** of the ~155 addresses the eleventh pass
left unrecovered, this pass probed **66** and resolved **every one** of them to a real
default branch and a licence state — **28 permissive** (12 MIT, 10 Apache-2.0,
3 ECL-2.0, 1 ISC, 1 BSD, 1 MPL-2.0), **17 copyleft** (10 GPL-3.0, 4 AGPL-3.0,
2 GPL-2.0, 1 EUPL-1.2), **11 ungranted**, **3 CC** content licences, **3 non-OSI**
source-available, and **4 dead**. Seven further addresses were probed from outside the
archive, from the search index. The clusters
now closed are the **xAPI/LRS tier**, the **Ed-Fi stack**, **LibreTexts**, **OpenStax**,
the **Nextcloud AI apps**, the **Moodle AI plugin cluster** and the **interoperability
tier**. The **~20-server education MCP cluster remains the largest untouched block**,
and the next pass should take it: two of this pass's five dead addresses were MCP
servers, so that cluster is the one most likely to have decayed.

---

## Added in the thirteenth pass of 2026-10-06 — the non-English-language channel, and a platform promoted out of trending

**Channel used this pass:** search in the **language of the country**, not in English or
Spanish. Passes 1–12 searched in English and (from the fifth pass) Spanish. This pass ran
the mandatory queries again in **Japanese, Korean, Arabic and Portuguese**. That is a new
channel for this KB, and the measured yield is in `agents/trending.md`.

**One row is promoted, not discovered.** `Open-TutorAi/open-tutor-ai-CE` was already
recorded in `repos/trending.md` by the twelfth pass, with the correct licence and star
count. It had never been shelved in `agents/top.md` or `verticals/solutions.md`. It is the
most capable permissive AI-native education platform in this KB and it was sitting in a
trending log. That is a shelving failure, and this pass fixes it.

| Agent | Repo | Licence (read from payload) | ★ / forks (2026-10-06) | What it does |
|---|---|---|---|---|
| Open TutorAI (Community Edition) | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** (`LICENSE`, 1,531 B — **body text, no title line**) | 108 / **192** | Personalised tutoring platform: multi-model conversation, **local RAG**, **voice / video / 3D-avatar modes**, structured learner onboarding that configures a per-learner assistant, and **role-based access control**. Serves **Ollama** local models as well as OpenAI / Groq / Mistral APIs. Python, 380 commits on `main`. **Morocco** — see provenance below. Open core: a paid Enterprise Edition adds theming, SLA and LTS. |
| SAEP 2026 — Agentes de IA e Ferramentas | [armandokeller/SAEP2026-Agentes-IA-e-Ferramentas](https://github.com/armandokeller/SAEP2026-Agentes-IA-e-Ferramentas) | **MIT** (`LICENSE`) | 0 / 0 | Eight-step agent-engineering curriculum (`ex0`–`ex8`): environment check, chat, conversation memory, tool calling, agentic loop, LangGraph, **MCP integration**, **human-in-the-loop approval**, then an exercise implementing custom MCP tools. Runs on a **small local model (Qwen 3.5-4B via LM Studio)** with **no cloud dependency**. Workshop material from the Escola Politécnica academic week at **Unisinos, Brazil**. Python. |

### Provenance of Open TutorAI, which this KB had not recorded

The twelfth pass recorded the repository, its licence and its fork inversion. It did not
record **who stands behind it**, and that is the part a client conversation turns on.

- **Origin: Agadir, Morocco.** The **IRF-SIC Laboratory, Ibn Zohr University**, with the
  **Regional Centre for Education and Training Professions (CRMEF) Souss-Massa**. Authors
  El Hajji · Ait Baha · Dakir · Fadili · Es-Saady (`arXiv:2602.07176`).
- **It is state-funded.** The work is supported by Morocco's **Ministry of Higher
  Education, Scientific Research and Innovation**, the **Digital Development Agency (DDA)**
  and the **CNRST**.

Both facts were absent from this KB: `Agadir` and `Ibn Zohr` returned **zero** matches
across every file before this pass. The consequence is a market fact, not a trivia fact:
**the most capable permissive AI-native education platform on this shelf is an African,
government-sponsored project**, which is a reference a public-sector buyer in EMEA or
LATAM can be pointed at directly.

### The licence warning on the row above — the holder is not identifiable

The payload reads:

```
Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev
All rights reserved.
```

**`R2D-dev` appears nowhere else.** Not in the README, not in the repository
documentation, and not in any search result this pass could reach. The licence is a clean
BSD-3-Clause and the grant is real; the **legal entity named as the holder is
unidentifiable from any public artefact of the project**. For an engagement that
redistributes this code to a client, the holder is the party a warranty or indemnity
question routes to — so this is the diligence item to raise upstream before it is proposed.

Two further details on the same payload:

- **`All rights reserved.` sits directly above a permissive grant.** The phrase contradicts
  nothing legally — it is vestigial — but it is exactly the string that makes a
  procurement reviewer stop. Expect to explain it.
- **The copyright range ends at 2025** while the repository is active in 2026, and the
  repository is **published as Apache-2.0 in third-party catalogues** while the payload is
  BSD-3-Clause. The twelfth pass caught the catalogue error; this pass confirms it from the
  payload independently, at the **same 1,531 bytes**.

### The 14th failure mode: a permissive body with no title line reads as unclassified

This pass's probe classified licence family by matching the **title line** of the payload
(`MIT License`, `Apache License`, …). `open-tutor-ai-CE` returned **HTTP 200 with a
payload that matched nothing** — because BSD-3-Clause is frequently distributed as the
**bare three-condition body with no heading at all**. A title-line classifier reports that
as *unclassified* and an automated gate would reject a genuinely permissive component.

This KB already knew the shape — `crewAIInc/crewAI` is recorded as *"MIT (`LICENSE`, body
text — no title line)"* — but it had not been written down as a **failure mode of the
instrument**. It is one: **classify on the operative clauses, not on the heading.** The
three-condition BSD body is identifiable by its third clause (*"Neither the name of the
copyright holder nor the names of its contributors may be used to endorse"*) with no
heading present anywhere.

### Recorded and excluded: ClawTeam

[HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) — **MIT** (`LICENSE`), **5.5k★**,
Python, v0.2.0 (Mar 2026). Agent-swarm orchestration: agents spawn sub-agents, divide
tasks, communicate over a file and P2P transport, isolated per-agent workspaces via git
worktrees. **It is not education software** and it is not shelved as one.

It is recorded because of **how it was found**: `HKUDS` is the organisation that publishes
**DeepTutor**, the largest agent in this KB. An **organisation sweep** — a channel this KB
used in its fourth pass — pulls ClawTeam in on the strength of the org name alone, and a
5.5k★ MIT repository from a known-good education org is precisely the kind of row that
gets shelved without being read. **The org is not the subject.** Logged here so the next
org sweep does not re-find it as a discovery.

## Added in the fourteenth pass of 2026-10-06 — the platform-name channel, and 24 verified rows

The thirteenth pass closed with four instructions. This pass took the first three and the
first one came back with a different answer than the pass that ordered it expected.

**Instruction 1 was: "take the ~20-server education MCP cluster from `archive/`."** The
cluster is **98 addresses**, not ~20 — the estimate was low by a factor of five. Every one
was probed: `git ls-remote --symref` for existence and real default branch, then up to
**20 licence filenames** on `raw.githubusercontent.com` against that branch, then
`package.json` / `pyproject.toml` / `setup.py` for a manifest declaration.

### Finding 1 — the archive MCP cluster is not decayed, and it is not ungranted

| Verdict | Count of 98 | Detail |
|---|---|---|
| **Licence payload read** | **76** | 68 MIT · 2 Apache-2.0 · 2 Unlicense · 2 GPL-3.0 · 2 AGPL-3.0 |
| No payload under 20 filenames | 17 | of which **7 declare a licence in a manifest only** |
| 🔴 **Gone — `ls-remote` cannot reach them** | **5** | listed below |

🟢 **72 of 98 addresses (73%) carry a permissive payload.** The pass that ordered this work
predicted decay ("expect decay and record it as supply data") on the strength of 2 dead MCP
servers in a sample of 4 dead addresses. Measured across the whole cluster, **decay is 5%**,
and the cluster is the most uniformly permissive block this KB has ever censused — 68 of 76
payloads are a plain 1.0–1.1 KB MIT. **The prediction was wrong, and it was wrong because a
2-of-4 ratio was read as a rate.**

🔴 **The 5 that no longer resolve:**

| Address | What it was |
|---|---|
| `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` | MCP server for the Ed-Fi SDK. Confirms the thirteenth pass. The rest of Ed-Fi is alive and Apache-2.0; Ed-Fi-over-MCP remains a **build**. |
| `appliedrelevance/frappe_mcp_server` | Frappe/ERPNext MCP server. The KB's note on its 3-byte PyPI licence field now has no upstream to re-read. |
| `imazhar101/mcp-canvas-server` | Canvas MCP server. |
| `owentaylor/canvas-mcp` | Canvas MCP server. |
| `radhepa/Teacher-MCP` | Teacher-facing MCP server. |

**Three of the five are Canvas or teacher-facing servers** — the densest, most duplicated
part of the cluster. Decay here concentrates in the tier where many authors built the same
thing, not in the tier that is hard to build.

### Finding 2 — the case-variant hypothesis does not reproduce, and that is worth as much as if it had

The thirteenth pass's instruction 2 was to re-probe ungranted verdicts with case variants,
because `LICENSE.TXT` had turned a 470★ Apache-2.0 repository into a false absence. This
pass probed all 98 addresses with the full case ladder — `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `LICENSE.TXT`, `LICENSE.MD`, `License`, `License.md`, `License.txt`,
`license`, `license.md`, `license.txt`, `LICENCE`, `LICENCE.md`, `LICENCE.txt`, `COPYING`,
`COPYING.txt`, `LICENSE-MIT`, `LICENSE.rst`, `docs/LICENSE`.

🔵 **76 of 76 payloads were at plain `LICENSE`.** Not one case variant, British spelling or
`COPYING` fallback paid out across 98 repositories.

**So the 13th failure mode is real but rare, and this is the number to carry:** the case
ladder costs ~19 extra requests per ungranted repository and buys, in this cluster, nothing.
Keep it in the gate for a **single high-value asset** whose absence would change a
recommendation; do not pay it across a census. The 470★ Apache-2.0 repository remains the
exception that justified finding the mode, not evidence of a systematic bias.

### Finding 3 — one default branch is an agent-generated branch, and `main` would have lied

`DaviPac/Classroom-mcp` resolves, and its default branch is:

```
claude/publish-classroom-aluno-mcp-9g61ee
```

🔴 **There is no `main`.** A probe hardcoding `main` or `master` — which is what this KB's
earlier passes did — returns 404 on every filename and writes the repository down as
ungranted. It is not: its `package.json` declares MIT (see Finding 4 for what that is
worth).

🟢 **This is the concrete vindication of instruction 3.** `ls-remote --symref` is now the
standing first step not because it is tidy but because **an agent-published branch is a
default branch in the wild**, and that is a new fact about the supply this KB measures.

### Finding 4 — 7 of the 17 "ungranted" repositories are *declared and ungranted*, which is worse than silent

Of the 17 addresses with no licence payload under 20 filenames, 7 carry a licence
**identifier in a build manifest** and nothing else:

| Address | Declares | Where | ★ |
|---|---|---|---|
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | MIT | `package.json` | **103** |
| [`DaviPac/Classroom-mcp`](https://github.com/DaviPac/Classroom-mcp) | MIT | `package.json` | not read |
| [`SalShah20/classroom_mcp`](https://github.com/SalShah20/classroom_mcp) | MIT | `package.json` | 1 |
| [`ink-waffle/moodle-mcp`](https://github.com/ink-waffle/moodle-mcp) | MIT | `package.json` | not read |
| [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | MIT | `package.json` | not read |
| [`pnp-v/bo-google-classroom-mcp-server`](https://github.com/pnp-v/bo-google-classroom-mcp-server) | ISC | `package.json` | not read |
| [`vnschneider/suap-mcp`](https://github.com/vnschneider/suap-mcp) | AGPL-3.0-or-later | `pyproject.toml` | not read |

🔴 **`DMontgomery40/mcp-canvas-lms` is the second-highest-starred Canvas MCP server on
GitHub at 103★, and it ships no licence text.** The GitHub API returns
`license: null` for it; the `package.json` says MIT. This KB has already established the
rule (a manifest identifier is an **identifier**, not a grant) — what is new is its **cost**:
the rule disqualifies the most-starred asset in the second-largest platform tier.

**This is a one-commit fix for the maintainer and it is worth asking for.** 7 of 17 is not a
licensing culture problem; it is a packaging default — `npm init` writes a `license` field
and no file. For a Globant engagement the practical rule stands unchanged: **no payload, no
deliverable.** `vnschneider/suap-mcp` is the one to read twice — it declares **AGPL-3.0**,
so if the payload ever lands it is a copyleft constraint, not a permissive win.

### Finding 5 — the platform-name channel: 80% licensed, against 25% for the language channel

**Instruction 4's channel question, answered.** The thirteenth pass varied the *language* of
the query and concluded the language was the wrong variable (3 licensed of 12, and only 1 was
education software). This pass varied the **platform name** instead — Canvas, Moodle,
Brightspace, Blackboard, Google Classroom, Skolverket, Smartschool, KUPID, NTU COOL — and ran
each one **alone**.

| Channel | Candidates | Licensed | Rate | Education software |
|---|---|---|---|---|
| Language (13th pass) | 12 | 3 | **25%** | 1 of 3 |
| **Platform name (this pass)** | **20** | **16** | **80%** | **16 of 16** |

🟢 **Every licensed find is education software, because the platform *is* an education
platform** — the channel cannot drift into the generalist agent layer the way a topic or
star-count query does. And it **places each find by region for free**: a platform is an
institution in a country. That is the property this KB has been missing, and it is the
answer to its own standing complaint that findings arrive unplaced.

### The rows — 24 verified assets, 22 of them new to this KB

Licences read from each repository's own payload on the real default branch, 2026-10-06.
Stars from the GitHub REST search API the same day.

#### The platform tier — Brightspace and Blackboard, which this KB had never recorded

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **Brightspace MCP Server** | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** (`LICENSE`, 1,068 B) | **57** (27 forks) | **North America** | **The fourth major LMS arrives on this shelf.** D2L Brightspace: grades, due dates, assignments, announcements, rosters, syllabus, course content. Published to npm (`npx brightspace-mcp-server@latest`), CI green, Node ≥ 20, "works with any school". Author at Purdue; D2L is Canadian. **The reference row for any Brightspace engagement.** |
| Brightspace MCP (multi-auth) | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | **MIT** (`LICENSE`, 1,070 B) | 12 | Global | The **engineering** reference rather than the feature reference: multi-strategy authentication (TOTP, OAuth, browser), retry / circuit-breaker / cache tiers, and **opt-in write operations**. Read this one before designing a write path into any LMS. |
| Brightspace MCP (Purdue) | [pranav-vijayananth/brightspace-mcp-server](https://github.com/pranav-vijayananth/brightspace-mcp-server) | **Apache-2.0** (`LICENSE`, 11,357 B) | 6 | North America | Python. The only **Apache-2.0** asset in the Brightspace tier — relevant where a client's policy prefers an explicit patent grant over MIT. |
| Blackboard Learn MCP + RBAC | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | **MIT** (`LICENSE`, 1,063 B) | 2 | Global | Blackboard Learn REST API over HTTP or stdio, with **RBAC middleware for role-based access control**. 2★ and the most governance-aware design in the whole 98-address cluster: role separation is the control an education deployment is actually audited on. |
| Blackboard Learn Ultra MCP | [NiccoloSalvini/mcp-blackboard-ucsc](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) | **MIT** (`LICENSE`, 1,073 B) | 0 | EMEA | Blackboard Learn Ultra over the public REST API. Python. |

#### The ministry and national-platform tier — the first of its kind in this KB

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **Skolverket MCP** | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP) | **MIT** (`LICENSE`, 1,093 B) | 12 | **EMEA** (Sweden) | 🟢 **A national curriculum as an agent-callable surface.** Exposes *all* of Skolverket's (Swedish National Agency for Education) open APIs: the **Läroplan / syllabus API**, the **Skolenhetsregistret** school-unit register, and the Planned Educations API. Published in the **official MCP Registry** (`io.github.isakskogstad/Skolverket-MCP`). ⚠️ The copyright line reads *"Skolverket Syllabus MCP Contributors"*, **not the agency** — this is a third-party wrapper of a public API, so the MIT covers the wrapper and the agency's own terms govern the data. |
| Udir MCP (Norway) | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** — no payload under 20 filenames, no manifest field | not read | **EMEA** (Norway) | Norwegian Directorate for Education (Udir) school (NSR) and kindergarten (NBR) registry data. **Found in the MCP Registry, and ungranted.** Recorded as the EMEA counter-case to Skolverket: two Nordic education-ministry wrappers, one usable, one not. |
| Smartschool MCP | [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP) | **MIT** (`LICENSE`, 1,069 B) | 5 | **EMEA** (Belgium) | Smartschool, the dominant LMS in Flemish education. Python ≥ 3.10, on **PyPI** (`smartschool-mcp`), with CI, codecov and a published MCP name (`io.github.MauroDruwel/smartschool-mcp`). Small star count, real release engineering. |
| KUPID portal MCP | [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp) | **MIT** (`LICENSE`, 1,068 B) | 13 | **APAC** (Korea) | Korea University's KUPID portal: notices, library seat availability, weekly assignments. On **PyPI** (`ku-portal-mcp`). Korean-language README. **The thirteenth pass's Korean-language query did not find this; the platform name did** — see the method note below. |
| NTU COOL | [kc0506/ntucool](https://github.com/kc0506/ntucool) | **MIT** (`LICENSE`, 1,066 B) | 10 | **APAC** (Taiwan) | National Taiwan University's COOL platform: a single `cool` binary that is CLI, MCP server (`cool mcp`) and SDK, **plus a Claude Code plugin** (`/plugin marketplace add kc0506/ntucool`) shipping skills and commands. ⚠️ Its own README states it is **unofficial**. The first asset in this KB to ship a Claude Code plugin as a distribution channel. |

#### Assessment, study and tutoring agents

| Agent | Repo | Licence (payload) | ★ | Region | What it does |
|---|---|---|---|---|---|
| **ICTExam MCP** | [ictinnovations/ictexam-mcp](https://github.com/ictinnovations/ictexam-mcp) | **MIT** (`LICENSE`, 1,114 B) | 16 | **APAC** (Pakistan) | 🟢 **A vendor shipping MIT into the assessment gap.** MCP server for **ICTExam**, a commercial AI exam authoring, delivery and **auto-grading** platform: read exams, gradebooks and per-question item analysis; parse a question paper into a structured exam with AI and publish to students — **only when writes are explicitly turned on**. On npm. Holder is a company (ICT Innovations), so the grant is corporate, not a student project. **The write gate is the design this KB has been asking for in trend 7.** |
| SmartStudy Agent | [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | **MIT** (`LICENSE`, 1,067 B) | 57 | Global | A **reinforcement-learning policy** chooses what to study next, an **FSRS** memory model schedules review, an LLM generates the quizzes between. Browser, terminal and MCP. The second auditable mastery instrument in this KB after OATutor's Bayesian Knowledge Tracing — and a different family (RL + FSRS vs BKT), which matters when a client asks why a sequencing decision was made. |
| Shiori (栞) | [kaorii-ako/Shiori-v1](https://github.com/kaorii-ako/Shiori-v1) | **MIT** (`LICENSE`, 1,073 B) | 45 | Global | Study companion: Google Classroom sync, SRS flashcards, weighted grade calculator with GPA prediction, syllabus-to-study-plan, quiz generation, MCP server. React/Vite + Supabase, PWA, Docker, self-hostable. **Bring-your-own Gemini key** — the cost model, not a subscription. The highest-starred asset in the Google Classroom tier. |
| OpenStudy | [OpenStudy-dev/OpenStudy](https://github.com/OpenStudy-dev/OpenStudy) | **MIT** (`LICENSE`, 1,068 B) | **75** | EMEA | Self-hostable personal study dashboard — courses, schedule, lectures, topics, deliverables, tasks — reachable by an agent from browser, phone, desktop or Claude Code. FastAPI + React 19 + Postgres 16. Bilingual DE/EN README. The cleanest **self-hosted + agent-reachable** reference stack on this shelf. |
| mydy LMS helper | [Deeptanshuu/mydy-lms-helper](https://github.com/Deeptanshuu/mydy-lms-helper) | **MIT** (`LICENSE`, 1,070 B) | 7 | APAC (India) | LMS assistant for the mydy platform. |

#### The Canvas and Moodle tiers — the duplicated middle, with the licensed ones named

| Agent | Repo | Licence (payload) | ★ | What it does |
|---|---|---|---|---|
| canvas-ed-mcp | [r1ckyIn/canvas-ed-mcp](https://github.com/r1ckyIn/canvas-ed-mcp) | **MIT** (`LICENSE`, 1,056 B) | 15 | Canvas LMS MCP server. ⚠️ Its MIT copyright line carries **a year and no holder name** — valid, but name the holder before vendoring. |
| canvas-mcp (Huijts) | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | **MIT** (`LICENSE`, 1,065 B) | 12 | Canvas LMS MCP server, © 2024 R. Huijts — the earliest copyright year in this pass's set. |
| canvas-mcp (Keluskar) | [aryankeluskar/canvas-mcp](https://github.com/aryankeluskar/canvas-mcp) | **ISC** (`LICENSE`, 746 B) | 11 | Canvas LMS MCP server. **The second ISC asset in this KB** — functionally MIT, OSI-approved, and still rejected by a `license:mit OR license:apache-2.0 OR license:bsd` filter. Reinforces the thirteenth pass's allow-list finding. |
| moodle-mcp (Ribeiro) | [1alexandrer/moodle-mcp](https://github.com/1alexandrer/moodle-mcp) | **MIT** (`LICENSE`, 1,074 B) | **18** | Moodle MCP server. The highest-starred **permissive** Moodle MCP server found this pass after `peancor/moodle-mcp-server` (43★), which this KB already carries. |
| moodle-mcp (Lefebvre) | [Snaw80/moodle-mcp](https://github.com/Snaw80/moodle-mcp) | **MIT** (`LICENSE`, 1,072 B) | 4 | Moodle MCP server. |
| Google Classroom MCP | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** (`LICENSE`, 1,063 B) | 6 (9 forks) | 🔵 **The highest-starred *dedicated* Google Classroom MCP server on GitHub.** 6★ — and that is the finding, not the row; see Finding 6. More forks than stars, which is what a utility people deploy rather than watch looks like. |
| Google Workspace for Education MCP | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** (`LICENSE`, 1,087 B) | 1 | Docs, Sheets, Slides, **Forms**, Drive and Classroom in one server. TypeScript. The Forms surface is the one the others lack, and Forms is where K-12 assessment actually lives. |
| AI School (course catalogue) | [Lilly-Tech-Collab/ai-school-mcp](https://github.com/Lilly-Tech-Collab/ai-school-mcp) | **MIT** (`LICENSE`, 1,405 B) | not read | Search and read 550+ free AI course tracks and 21,000+ lessons. Found in the **MCP Registry**. An enablement-content surface, not a platform integration. |
| Moltline Educator | [GarphenGate/moltline-mcp](https://github.com/GarphenGate/moltline-mcp) | **MIT** (`LICENSE`, 1,072 B) | not read | 8 skills across curriculum, classroom, **accommodations** and exam prep. Found in the MCP Registry. Accommodations is a vocabulary no other asset in this KB covers, and it is a legal requirement in both US and EU school systems. |

### Finding 6 — the supply map, and the hole is K-12 administration

Measured with GitHub REST `total_count`, one platform name per query, 2026-10-06:

| Platform tier | `total_count` | Highest ★ | Highest-starred **permissive, payload-backed** asset |
|---|---|---|---|
| Canvas LMS | **117** | 278 | `vishalsachdev/canvas-mcp`, MIT (already shelved) |
| Moodle | **86** | 43 | `peancor/moodle-mcp-server`, MIT (already shelved) |
| **Brightspace / D2L** | **23** | 57 | `RohanMuppa/brightspace-mcp-server`, MIT 🆕 |
| **Google Classroom** | **17** | 45 (Shiori) | `faizan45640/...`, MIT, **6★** 🆕 |
| **Blackboard Learn** | **5** | 2 | `nitsuah/bb-mcp`, MIT 🆕 |
| Open edX | **1** | 1 | — (AGPL-3.0; already recorded) |
| 🔴 **PowerSchool (US K-12 SIS)** | **0** | — | **none — the tier does not exist** |

🔵 **Open-source MCP coverage tracks the higher-education install base and ignores K-12.**
Canvas and Moodle together hold **203 of the 249** repositories measured. Blackboard, with a
large global university estate, has **5**. Google Classroom — the widest K-12 reach of any
platform on this table — has **17**, and its best dedicated server has **6★**. PowerSchool,
the dominant US K-12 student information system, measures **`total_count: 0`**.

**This is the clearest build-versus-adopt signal in this KB.** For a higher-ed engagement on
Canvas or Moodle, adopt: the shelf is deep, permissive and duplicated. For **K-12
administration**, there is nothing to adopt and nothing to compete with — a Globant-built
Google Classroom or PowerSchool MCP server enters an empty tier, and the governance surface
(student records, guardians, accommodations) is exactly the regulated part.

### Finding 7 — a bespoke "Community License" in the education MCP tier, and it is unusable

[`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom)
carries **`LICENSE.md`, 6,489 B**, titled **"AStheTECH Community License (ACL)"**. Read in
full. It is not OSI-approved and it is not near-miss permissive:

- Grant: *"limited, non-exclusive, non-transferable"*; *"All rights not expressly granted are reserved."*
- Prohibited without written authorisation: **sell, license, sublicense, lease or otherwise commercially exploit**; **offer the software as part of any hosted service, SaaS platform or API service**; **rebrand or white-label**; build anything *"substantially similar to or competitive with"* it.
- Distribution permitted only where *"strictly non-commercial in nature."*
- **Termination is automatic and immediate on any breach**, with destruction of derivatives.

🔴 **Verdict: unusable in client work, under every clause that matters.** A Globant
deliverable is commercial, is usually hosted, and is usually rebranded. The word
*"Community"* in the title is doing the opposite of what a reader skimming a repository
listing would assume, and GitHub's sidebar shows such a file as a generic "License".

**This is trend 23's label-versus-grant finding at its sharpest**: not a mislabelled
permissive licence, but a **bespoke proprietary licence whose name reads as an open one**.
The gate is unchanged and it caught this: read the payload, and when the first line is not a
known licence title, read all of it.

### Finding 8 — 11 addresses measured this pass and genuinely ungranted

Probed with the full 20-filename ladder on the real default branch, plus manifests. No grant
of any kind:

| Address | Platform | ★ |
|---|---|---|
| [`lucanardinocchi/canvas-mcp`](https://github.com/lucanardinocchi/canvas-mcp) | Canvas | **22** |
| [`plyght/canvas-mcp`](https://github.com/plyght/canvas-mcp) | Canvas | 14 |
| [`joshuasoup/d2l-mcp`](https://github.com/joshuasoup/d2l-mcp) | Brightspace | 13 |
| [`haanhtuandev/vgu-mcp`](https://github.com/haanhtuandev/vgu-mcp) | Vietnamese-German University (APAC) | 10 |
| [`zainf2327/mcp-classroom`](https://github.com/zainf2327/mcp-classroom) | Google Classroom — **auto-grades submissions** | 6 |
| [`kesaruhasun/mcp-sliit-courseweb`](https://github.com/kesaruhasun/mcp-sliit-courseweb) | SLIIT, Sri Lanka (APAC) | 6 |
| [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) | Blackboard, Univ. of Queensland + Okta SSO | 0 |
| [`shimahikojin/google-classroom-mcp`](https://github.com/shimahikojin/google-classroom-mcp) | Google Classroom | 0 |
| [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | Udir, Norway (EMEA) | not read |
| [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | US school districts (North America) | not read |
| [`710git/course-drift-oracle`](https://github.com/710git/course-drift-oracle) | course-drift reports | not read |

⚠️ **`zainf2327/mcp-classroom` auto-grades student submissions and carries no licence.** Of
everything ungranted in this pass, that is the one whose function is most regulated and
whose grant is most needed.

### The method note for this pass

**Four instrument facts, three of them cautionary.**

1. 🔴 **Boolean `OR` in GitHub repository search destroys specificity.** The LATAM probe
   `sigaa OR suap OR siga mcp server` returned **`total_count: 160,659`** — the generalist
   MCP layer (`awesome-mcp-servers` 95.9k★, `headroom`, `private-gpt`, `playwright-mcp`).
   The same platform names queried **one at a time** return tiers in the single and double
   digits. **Never OR platform names.** Every count in Finding 6 was measured with one name
   per query for exactly this reason.
2. 🔵 **`minimal_output: true` on the search API returns stars, forks, topics and the real
   default branch, and omits the licence.** That is the right shape for this KB: the licence
   must come from the payload anyway, and the full objects overflow a single tool result at
   ten rows.
3. 🟢 **`ls-remote --symref` first, every time** — it answers existence and default branch in
   one call with no API dependency, and Finding 3 is what happens without it.
4. ⚠️ **A language channel and a platform channel answer different questions.** The Korean
   asset `SonAIengine/ku-portal-mcp` (MIT, 13★) existed when the thirteenth pass ran its
   Korean-language query and that query did not surface it. The platform name **KUPID** did.
   The thirteenth pass's conclusion — *"the language was the wrong variable"* — holds and
   gets sharper: **what places an asset is the institution, and the institution's name is
   usually searchable in English even when its README is not.**

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS tier, and the first non-licence blocker in this KB

The fourteenth pass handed this pass two instructions. This section answers the second:
*"run the platform-name channel against the SIS and ministry tiers, which this pass only
sampled."* It was the right instruction and it overturns the finding that produced it.

**Every licence below was read from the repository's own payload** on 2026-10-06, on the real
default branch confirmed by `ls-remote --symref`. 44 addresses probed, 36 carried forward.

### Finding 1 — "the tier does not exist" is wrong, and this KB already held the refutation

The fourteenth pass's Finding 6 recorded `powerschool` at **`total_count: 0`** and concluded
**"none — the tier does not exist"**. Measured again today, four query shapes:

| Query | `total_count` |
|---|---|
| `powerschool` | **590** |
| `powerschool in:name` | **354** |
| `powerschool mcp` | **3** |
| `powerschool mcp server` | **1** |

🔴 **The minimum over four shapes is 1, not 0.** The zero is not reproducible as a
query-shape artifact; it was an instrument error written down as a property of the world.

🔴 **And the refutation was already inside this KB before the claim was made.** An earlier
pass had shelved [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool)
and [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) under
*"MCP over SIS"*. The fourteenth pass wrote "the tier does not exist" over its own record.

🔵 **The method rule this adds:** a zero from a search channel is a claim about the channel.
Before it is written as a property of the supply, **grep this KB for the thing claimed
absent.** That check costs one command and would have caught this.

### Finding 2 — the headline: MIT is granted, and the tier is still not deployable

[`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) — MIT,
`LICENSE`, 1,067 B, holder *"Chris Hall"*, 20 tools over Infinite Campus — is the one
payload-backed MCP server on a US K-12 SIS. Its own README quotes the vendor's Terms of Use:

> Users may not access, use, or search the Services by any means other than our publicly
> supported interfaces (for example, scraping or using the content to train artificial
> intelligence software).

And then states, of itself:

> This server uses Infinite Campus's mobile-app JSON endpoints (`/campus/api/oneRosterCampus`,
> `/portal/api/...`) which are not "publicly supported interfaces" — IC may treat this as a
> ToS violation.

It further restricts itself to **"personal, parent/student use only"**, is *"not affiliated
with, endorsed by, sponsored by, or in partnership with Infinite Campus, Inc. or any school
district"*, says **"do not use it to bulk-extract student data … or train AI models on
student records"**, and invokes **FERPA and COPPA** on the output.

🔴 **This is a new axis, and it is the first blocker in this KB that is not a licence.**
Twenty-three recorded licence failure modes all answer one question: *may we copy and
redistribute this code?* Here the answer is **yes, MIT, unambiguously** — and the component
is still not shippable, because a different grant is missing: **the right to reach the data.**
The copyright holder gave us the code. The SIS vendor did not give us the API.

⚠️ **The two grants are orthogonal, and only one of them is in the repository.** No licence
audit, however rigorous, detects this. It is not in `LICENSE`; it is in a third party's ToU.

⚠️ **Provenance of the quotation, stated precisely.** The ToU text above was read today from
**the repository's own README**, where the maintainer records having read the vendor's terms
on **2026-05-23**. The vendor's page itself — `infinitecampus.com/terms/terms-of-use` — is
**blocked by this environment's egress proxy** (`connect_rejected`), so this KB has **not**
verified it first-hand, and a ToU can change without notice. 🔵 **The finding does not
depend on the quotation being current**: the maintainer's own statement that the server
calls non-public endpoints and may violate the vendor's terms is first-hand evidence from
the party best placed to know. **Next pass: re-read the vendor page from an unblocked
network and date it.**

🔵 **What it does to the fourteenth pass's conclusion.** That pass said *"for K-12
administration there is nothing to adopt… a Globant-built PowerSchool MCP server enters an
empty tier."* The tier is **not** empty — and the build recommendation **survives anyway, for
a stronger reason**: what you cannot adopt is not the code but the access path. Building your
own MCP server does not fix it either. **What fixes it is a contract and the vendor's official
API** (PowerSchool and Infinite Campus both publish OneRoster endpoints; this KB's
interoperability tier already carries the permissive OneRoster/Ed-Fi implementations).

### Finding 3 — the access-legitimacy axis, read from the repositories' own words

This is not one maintainer being unusually careful. The tier is built on unofficial access and
says so:

| Asset | What it says about itself |
|---|---|
| [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | *"Unofficial — not affiliated with Infinite Campus. AI-maintained."* + the ToU quotation above |
| [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api) | *"Uma biblioteca de **Web Scraping**, para acessar o SIGAA"* — and it is **archived** |
| [`kc0506/ntucool`](https://github.com/kc0506/ntucool) | *"This is an **unofficial** project. Use it at your own risk, and responsibly."* |
| [`elisaado/somtoday-api-docs`](https://github.com/elisaado/somtoday-api-docs) | repository topic: **`reverse-engineering`** |
| [`Underlyingglitch/SomtodaySSOLogin`](https://github.com/Underlyingglitch/SomtodaySSOLogin) | topics `reverse-engineering`, `sso-authentication` — **archived** |
| [`cqm3ron/bromcom-scraper`](https://github.com/cqm3ron/bromcom-scraper) | *"a python script to host an API to get bromcom homework assignment data"* |

🔴 **And a cookie-bridge architecture, which is the mechanism the ToS language targets.**
`infinitecampus-mcp`'s no-password auth path installs a browser extension
([`nullnet-app/contextmint-bridge`](https://github.com/nullnet-app/contextmint-bridge), the
former `fetchproxy`), which reads the HttpOnly `JSESSIONID` and `XSRF-TOKEN` from a
logged-in tab and hands them to the MCP server, which then calls the API directly. It is an
elegant answer to *"the vendor has no agent API"* — and it is precisely *"means other than
our publicly supported interfaces."*

🔵 **Record it as an anti-pattern for client work and a signal for roadmaps.** A cookie bridge
in a repository is evidence that the install base wants agent access the vendor does not yet
sell. That is a product opportunity, not a deliverable component.

### Finding 4 — the PowerSchool grant is one layer down from where you want it

| Layer | Asset | ★ | Payload |
|---|---|---|---|
| MCP server | [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) | 2 | 🔴 **none** (6 filenames, `main`) |
| MCP server | [`zuvy/ps-mcp-server`](https://github.com/zuvy/ps-mcp-server) | 1 | 🔴 **none** (6 filenames, `main`) |
| API client (Node) | [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **34** | 🟢 **MIT**, 1,072 B — *Ayden Panhuyzen* |
| API client (PHP) | [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | 20 | 🟢 **MIT**, 1,101 B |
| API client (Python) | [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | 16 | 🟢 **MIT**, 1,082 B |
| API client (Python) | [`TEAMSchools/powerschool`](https://github.com/TEAMSchools/powerschool) | 23 | ⚠️ **GPL-3.0**, 35,149 B — **archived** |

🔴 **Both PowerSchool MCP servers are ungranted. Every PowerSchool API client but one is MIT.**
The grant exists exactly one layer below the layer an agent engagement wants.

🟢 **So the recipe writes itself, and it is the opposite of "build the integration":** take an
MIT client, write the thin MCP wrapper yourself, and spend the saved effort on the access
contract. Shipped as **P25** in `compose/patterns.md`.

### The rows — 36 addresses, placed by country, licence read from the payload

**North America** — US K-12 and higher-ed SIS

| Repo | ★ | Licence (payload) | What it is |
|---|---|---|---|
| [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | 34 | **MIT** (1,072 B) | Node.js client, PowerSchool SIS API |
| [`TEAMSchools/powerschool`](https://github.com/TEAMSchools/powerschool) | 23 | GPL-3.0 (35,149 B) | Python client — **archived** |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | 20 | **MIT** (1,101 B) | PHP client |
| [`shinyquagsire23/InfiniteCampusAPI`](https://github.com/shinyquagsire23/InfiniteCampusAPI) | 20 | ⚠️ **WTFPL v2** (474 B) | Java Infinite Campus client |
| [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | 16 | **MIT** (1,082 B) | Python client |
| [`sas-fossdev/saspes`](https://github.com/sas-fossdev/saspes) | 13 | AGPL-3.0 (34,522 B) | PowerSchool browser extension |
| [`NCSIS/InfiniteCampus-Vendor-Integration`](https://github.com/NCSIS/InfiniteCampus-Vendor-Integration) | 13 | 🔴 none | PowerShell vendor integration |
| [`chrischall/infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) | 4 | **MIT** (1,067 B) | **MCP server, 20 tools** — ⚠️ see Finding 2 |
| [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) | 2 | 🔴 none | MCP server |
| [`zuvy/ps-mcp-server`](https://github.com/zuvy/ps-mcp-server) | 1 | 🔴 none | MCP server |
| [`bnnadi/Sky`](https://github.com/bnnadi/Sky) | 1 | 🔴 none | React Native **demo** — not an integration |

**EMEA** — placed by country

| Repo | ★ | Licence (payload) | Country / system |
|---|---|---|---|
| [`SapuSeven/BetterUntis`](https://github.com/SapuSeven/BetterUntis) | **300** | ⚠️ GPL-3.0 (35,149 B) | DE/AT — WebUntis, Kotlin Android |
| [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **241** | 🟢 **MIT** (1,062 B) | FR — PRONOTE, Python wrapper |
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **214** | 🔴 **none** (6 filenames, `master`) | DE/AT — the costliest absence in this tier |
| [`Litarvan/pronote-api`](https://github.com/Litarvan/pronote-api) | 192 | 🔴 none | FR — PRONOTE |
| [`JonasJoKuJonas/homeassistant-WebUntis`](https://github.com/JonasJoKuJonas/homeassistant-WebUntis) | 148 | 🟢 **MIT** (1,062 B) | DE/AT |
| [`delphiki/hass-pronote`](https://github.com/delphiki/hass-pronote) | 105 | 🔴 none | FR |
| [`elisaado/somtoday-api-docs`](https://github.com/elisaado/somtoday-api-docs) | 87 | 🔴 none | NL — SOMtoday API documentation |
| [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | 81 | 🟢 **BSD-2-Clause** (1,505 B) | DE/AT — *Markus Unterwaditzer* |
| [`magister-api/magister`](https://github.com/magister-api/magister) | 49 | 🟢 **MIT** (1,085 B) | NL — Magister 6, PHP |
| [`ninocss/UntisPlus`](https://github.com/ninocss/UntisPlus) | 44 | 🟢 **MIT** (1,064 B) | DE/AT — Flutter, **on-device AI assistant** |
| [`untisapi/untis4j`](https://github.com/untisapi/untis4j) | 33 | ⚠️ LGPL-3.0 (7,378 B) | DE/AT — Java |
| [`Jona-Zwetsloot/Somtoday-Mod`](https://github.com/Jona-Zwetsloot/Somtoday-Mod) | 16 | 🔴 **CC BY-NC-SA 4.0** (17,056 B) | NL — **NonCommercial: unusable** |
| [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | 15 | 🟢 **MIT** (1,066 B) | NL — SOMtoday REST client |
| [`sikkepitje/TeamSync`](https://github.com/sikkepitje/TeamSync) | 9 | ⚠️ GPL-3.0 (35,149 B) | NL — Magister → MS School Data Sync |
| [`RichardSlater/bromcom-timetable-formatter`](https://github.com/RichardSlater/bromcom-timetable-formatter) | 1 | 🟢 **MIT** (1,071 B) | UK — Bromcom, Rust |
| [`DPlazma/assessapp`](https://github.com/DPlazma/assessapp) | 0 | 🟢 **MIT** (1,064 B) | UK — Arbor MIS + **AI tagging**, Django |

**APAC** — and the whole tier is one university

| Repo | ★ | Licence (payload) | Country / system |
|---|---|---|---|
| [`AkizumiFox/NTU-COOL-Assignment-Status-Viewer`](https://github.com/AkizumiFox/NTU-COOL-Assignment-Status-Viewer) | 19 | 🟢 **MIT** — at **`LICENCE`** (1,056 B) | TW — NTU COOL |
| [`kc0506/ntucool`](https://github.com/kc0506/ntucool) | 10 | 🟢 **MIT** (1,066 B) | TW — **Rust CLI + MCP server** |
| [`kuang-che/NTU-COOL-Preview-Tool-extension`](https://github.com/kuang-che/NTU-COOL-Preview-Tool-extension) | 8 | 🟢 **MIT** (1,066 B) | TW |

🔵 **NTU COOL is Canvas-based**, which is why this is the one APAC institution with a tier:
the asset authors inherit Canvas's documented API. The platform channel found an institution;
the *reason* it had something to find is the LMS underneath it.

**LATAM** — Brazil, and it is the deepest national tier in this pass

| Repo | ★ | Licence (payload) | Institution / system |
|---|---|---|---|
| [`aquario-ufpb/aquario`](https://github.com/aquario-ufpb/aquario) | 84 | 🟢 **MIT** (1,070 B) | UFPB — student information hub, TypeScript |
| [`luthierycosta/ConsertandoHorariosSIGAA`](https://github.com/luthierycosta/ConsertandoHorariosSIGAA) | 75 | 🟢 **MIT** (1,082 B) | UnB — SIGAA timetable decoder |
| [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api) | 61 | 🟢 **MIT** (1,108 B) | SIGAA — ⚠️ **archived**, self-described scraper |
| [`ernestosrf/sigaa-horarios-extension`](https://github.com/ernestosrf/sigaa-horarios-extension) | 58 | 🔴 none | UFBA |
| [`rodrigmatrix/sigaa_ufc_android`](https://github.com/rodrigmatrix/sigaa_ufc_android) | 33 | 🟢 **Apache-2.0** (11,357 B) | UFC — Android |
| [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | 33 | 🟢 **MIT** (1,071 B) | IFRN — SUAP client |
| [`IFRN/suapi`](https://github.com/IFRN/suapi) | 28 | 🔴 **none** | ⚠️ **the institution's own org, ungranted** |
| [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | 24 | 🟢 **MIT** (1,065 B) | SIGAA tooling, Python |
| [`Projeto-SIAC/suap-wrapper`](https://github.com/Projeto-SIAC/suap-wrapper) | 12 | 🟢 **MIT** (1,061 B) | SUAP, Node.js |

🟢 **The LATAM entry the fourteenth pass could not measure is real and it is the largest
national cluster this pass found: `sigaa` 677 repositories, `suap ifrn` 27, nine addresses
carried forward, seven of them permissive.** The fourteenth pass's only attempt OR'd the
names and collapsed into the generalist layer at `total_count: 160,659`. One name per query
returns a tier.

⚠️ **And the ungranted one is the institution's own.** [`IFRN/suapi`](https://github.com/IFRN/suapi)
— *"Clientes para acesso à API do SUAP"*, published by the federal institute that **operates**
SUAP — carries no licence payload, while an individual's `suap-api-php` is MIT. This is the
single most answerable upstream ask in this pass: a public institution, a public repository,
one missing file.

### Finding 5 — the channel's yield is a property of the name, not of the supply

The fourteenth pass priced the platform channel at 80% licensed and recommended it broadly.
It works, and it has one failure mode that must be stated with it:

| Platform name | `total_count` | Verdict |
|---|---|---|
| `pronote` | **907** | 🟢 real tier |
| `sigaa` | **677** | 🟢 real tier |
| `powerschool` | **590** | 🟢 real tier |
| `webuntis` | **401** | 🟢 real tier |
| `somtoday` | **112** | 🟢 real tier |
| `"ntu cool"` | **54** | 🟢 real tier |
| `infinitecampus` | **43** | 🟢 real tier |
| `bromcom` | **36** | ⚠️ thin — nothing above 2★ |
| `suap ifrn` | **27** | 🟢 real tier |
| `"arbor mis"` | **7** | ⚠️ all 0★, mostly coursework clones |
| `"skyward" student information system` | **1** | 🔴 a demo app, no integration |
| `"capita sims" school` | **0** | 🔴 empty |
| `samarth ugc` | **0** | 🔴 empty |
| 🔴 `diksha` | **2,864** | 🔴 **name collision — zero are the platform** |

🔴 **`diksha` is the channel's worst case and it is not thinness, it is a false positive at
scale.** India's national platform shares its name with a common Indian given name: the 2,864
results are personal portfolios, a fitness studio, a coaching website. **A tier that looks
deep and contains nothing.** The real upstream for that platform is **Sunbird**, which this
KB already shelves.

🔵 **The qualification to carry forward: the platform channel's yield tracks the
*distinctiveness* of the platform's name.** `webuntis`, `somtoday`, `pronote`, `bromcom` are
coined words and return clean tiers. `diksha`, `arbor`, `skyward`, `compass`, `clever` are
ordinary words and return noise or nothing. Before trusting a count, ask whether the name is
a word.

⚠️ **Boolean `OR` failed again, twice, exactly as the fourteenth pass warned**:
`arbor bromcom sims mis school` → **0**; `sentral compass school australia api` → **0**. Two
more data points for a rule this KB already has.

### The method note for this pass

**Three instrument findings, and the first one invalidates an instruction in the brief.**

1. 🔴 **`curl -sI https://github.com/<repo>` returns HTTP 403 for every repository through
   this environment's egress proxy — all 36, including ones whose payloads were then read
   successfully.** The standing instruction to verify URLs with `curl -sI` **cannot be
   satisfied here**, and worse, it returns a *uniform* 403 that looks like a verdict. A
   constant response is not evidence. **The instruments that do work:**
   `git ls-remote --symref` (existence + real default branch, no API, no auth) and
   `raw.githubusercontent.com` (payload). All 36 rows above were verified with both;
   36/36 exist and every default branch was confirmed, not assumed.
2. 🔴 **This pass reproduced a defect this KB had already found, fixed and built a control
   for — and the control was correct.** The probe script written for this pass classified
   four payloads as Creative Commons/NonCommercial (`SapuSeven/BetterUntis` 300★,
   `TEAMSchools/powerschool`, `sikkepitje/TeamSync`, `sas-fossdev/saspes`); all four are
   **GPL-3.0 or AGPL-3.0**, because GPL-3.0 §6 contains the word *"noncommercially"*. An
   earlier pass of this KB had already measured that exact string at **line 259** of the
   payload, diagnosed it as **P171** (*a token read over the body cannot be believed*), and
   fixed it in `compose/code/lib/license_family.sh` with a **gate** — `osi_family_of()`
   resolves the family first, and the Creative Commons branch is entered only on
   `Creative Commons|creativecommons.org|CC BY|CC-BY`, after which NonCommercial is read as
   an attribute. 🟢 **Tested this pass, that library is right on all three hard payloads
   first time: `GPL-3.0`, `AGPL-3.0`, `CC-BY-NC-SA-4.0`.** 🔴 **The failure was bypassing it.**
   The library's own header records the previous instance (pass 77, *"the correction did not
   travel"*); this is the second. **The rows published above are unaffected — all four were
   re-read by hand and carry their true families** — but the lesson is a process one: source
   `lib/license_family.sh`, and better, give `lib/` a probe harness so no future pass writes
   the loop by hand at all.
3. 🟢 **One payload sat at `LICENCE`, British spelling** —
   `AkizumiFox/NTU-COOL-Assignment-Status-Viewer`, MIT, 1,056 B. The fourteenth pass measured
   the full case-variant ladder at **76 of 76 on plain `LICENSE`** and priced it as worthless.
   That stands, with one amendment: **1 in 44 this pass sat at the British spelling.** Carry
   `LICENCE` as a second probe — it is one extra request — and leave the other eleven variants
   off the census, exactly as that pass instructed.

### Added later in the fifteenth pass — the MCP Registry channel, filtered, and it closes two of this pass's own gaps

Instruction 1 (*"finish the MCP Registry census"*) was run with the retry fix described in
`repos/trending.md`. The census itself is a channel-economics finding and lives there. **What
belongs here are the rows**, because once the index is filtered the channel is high-precision:
**13 of 16 probed addresses carry a licence payload, 12 of them MIT.**

All rows below were probed with the new shared harness
(`compose/code/lib/probe_payload.sh`), which resolves the real default branch first and
classifies with `lib/license_family.sh`.

| Repo | ★ | Licence (payload) | Region | What it is |
|---|---|---|---|---|
| [`JohannsenLum/canvas-api-mcp`](https://github.com/JohannsenLum/canvas-api-mcp) | 3 / **13 forks** | **MIT** (1,069 B) | Global | 16 curated student tools **plus a gateway to all 1,116 Canvas API endpoints** |
| [`Smartoire/paxaver-mcp`](https://github.com/Smartoire/paxaver-mcp) | 0 | **Apache-2.0** (11,344 B) | Global | School-community platform adapter — **streamable HTTP + OAuth 2.1**, capability-scoped |
| [`KSAklfszf921/skolverket-mcp`](https://github.com/KSAklfszf921/skolverket-mcp) | 0 | **MIT** (1,092 B) | **EMEA** (SE) | Skolverket open APIs — curriculum, school units, **adult education**. The *second* permissive Skolverket server in this KB |
| [`MartinSA04/ntnu-mcp`](https://github.com/MartinSA04/ntnu-mcp) | 0 | **MIT** (1,076 B) | **EMEA** (NO) | NTNU course data on Cloudflare Workers — timetables, grade statistics, conflict checks |
| [`Cogniledger/cogniledger-mcp-makuri`](https://github.com/Cogniledger/cogniledger-mcp-makuri) | 0 | **MIT** (1,084 B) | **EMEA** (EU) | ⚠️ **"EU-compliant AI tutoring platform for immigrant children"** — the most regulated user group in this KB, permissively licensed |
| [`EquateItAu/classquill-mcp`](https://github.com/EquateItAu/classquill-mcp) | 0 | **MIT** (1,077 B) | **APAC** (AU) 🆕 | ClassQuill tutoring-business data — **read-only by design** (sessions, students, tutors, invoices, reports) |
| [`Eason0in/classdojo-mcp`](https://github.com/Eason0in/classdojo-mcp) | 0 | **MIT** (1,065 B) | **North America** | ⚠️ ClassDojo roster import/verify, **unofficial, local-first** — a **K-12** asset |
| [`SidneyBissoli/uis-mcp-server`](https://github.com/SidneyBissoli/uis-mcp-server) | 0 | **MIT** (`LICENSE.md`, 1,079 B) | Global | UNESCO UIS statistics **with full provenance and pinned releases** |
| [`Lilly-Tech-Collab/ai-school-mcp`](https://github.com/Lilly-Tech-Collab/ai-school-mcp) | 0 | **MIT** (1,404 B) | Global | 550+ free AI course tracks / 21,000+ lessons, **answers cite a real lesson** |
| [`CSOAI-ORG/education-ai-mcp`](https://github.com/CSOAI-ORG/education-ai-mcp) | 0 | **MIT** (1,068 B) | Global | Lesson-plan + quiz generation |
| [`CSOAI-ORG/quiz-generator-ai-mcp`](https://github.com/CSOAI-ORG/quiz-generator-ai-mcp) | 0 | **MIT** (1,080 B) | Global | Quiz generation + answer validation |
| [`CSOAI-ORG/flashcard-ai-mcp`](https://github.com/CSOAI-ORG/flashcard-ai-mcp) | 0 | **MIT** (1,080 B) | Global | Flashcards + **spaced repetition** |

**Measured and ungranted from the same filter** — including **two addresses the fourteenth
pass listed as "not read", now read:**

| Repo | Verdict |
|---|---|
| [`3121n/nor-data-udir-mcp`](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **no payload** on `master`. Udir (Norway) registry data. *Pass 14 left this "not read" — it is now read.* |
| [`DistrictAPI/districtapi-mcp`](https://github.com/DistrictAPI/districtapi-mcp) | 🔴 **no payload** on `main`. US public school districts by address — enrolment, demographics, boundaries. *Also "not read" in pass 14.* |
| [`Capmus-Team/supost-mcp`](https://github.com/Capmus-Team/supost-mcp) | 🔴 **no payload** on `master`. Stanford student marketplace. |
| `lockinplanner/lock-in` | 🔴 **does not resolve** — `ls-remote` returns nothing. A registry entry pointing at an address that is not there. |

### 🟢 Two gaps this pass declared, and then closed in the same pass

This matters more than the rows, because it is a check on this KB's own method.

1. 🔴 **Declared gap 3 of this pass said: *"no Japan-, Korea-, Australia- or India-placed SIS
   integration asset was found."* The Australia half is now wrong.**
   [`EquateItAu/classquill-mcp`](https://github.com/EquateItAu/classquill-mcp) is MIT,
   payload-verified, and Australian. 🔵 **The gap was true of the platform-name channel and
   false of the world** — exactly the error Finding 1 of this pass corrected in the
   fourteenth pass's work, reproduced here within hours. **A single-channel gap is a
   statement about that channel.** The gap is restated correctly in `intel/trends.md`:
   Japan, Korea and India remain unfound; **Australia is found.**
2. ⚠️ **The fourteenth pass's "the hole is K-12 administration" needs the same qualification.**
   [`Eason0in/classdojo-mcp`](https://github.com/Eason0in/classdojo-mcp) (MIT) is a K-12
   classroom asset, and ClassDojo reaches a very large K-12 install base. It is unofficial
   and roster-scoped, so the *administration* claim survives in substance — but the tier is
   not empty, and it was not empty when it was called empty.

🔵 **The channel lesson, stated for the next pass.** The registry is **low-density and
high-precision**: ~160 education-matching servers in a 17,000+-name index (under 1%), most of
those false positives — and once filtered by hand, **13 of 16 carried a payload and 12 were
MIT**. It also reached **three regions the platform-name channel missed in the same pass**
(Australia, Norway, EU-regulated tutoring). **Run both channels; they fail differently.** The
platform channel finds institutions; the registry finds products.

---

## Added in the sixteenth pass of 2026-10-06 — one agent-adjacent row, and the honest count

The channel this pass ran was the **ministry tier** (`agents/trending.md`, Finding 1). It is a
good channel for **data, specs and platforms** and a poor one for agents: a directorate
publishes a curriculum API, not a tutor.

**So this pass adds one row, and says so rather than padding the table.**

| Name | Repo | Licence (payload-verified) | ★ | Region | Description |
|---|---|---|---|---|---|
| **MCP Brasil** | [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) (`main`) | 🟢 **MIT** (`LICENSE`, 1,072 B, *"(c) 2025-2026 MCP Brasil"*) | 🟢 **1,805** | **LATAM** (BR) | MCP server over **70 Brazilian public-sector APIs** (Python / FastMCP), **13 of its endpoints education**. The largest education-data tool surface placed in LATAM in this KB. 🟢 **Canonical address, settled in the seventeenth pass by root-commit comparison** — see the resolution below. |

🟢 **RESOLVED in the seventeenth pass of 2026-10-06 — and the resolution corrects this KB,
not the repository.** All three addresses were cloned with full history and share the root commit
`8b786bfab09f2637bf842571250f4beb8ff5d216` (2026-03-22). `Mcp-Brasil/mcp-brasil` is **upstream**
(1.8k★, 278 forks, no fork banner). [`dasgltd/mcp-brasil`](https://github.com/dasgltd/mcp-brasil)
is a **fork of it** — its page reads *"forked from Mcp-Brasil/mcp-brasil"* — sitting at **0★** and
in exact sync (same `HEAD` `2efb258`, same 246 commits, same 23 tags), which is why refs alone
could not separate them. `marcellodesales/mcp-brasil` is a second fork, 8 commits behind.

🔴 **Two pass-16 statements were wrong and are withdrawn here.** (1) *"the GitHub API reports
neither as a fork of the other"* — the rendered page states the fork relationship plainly.
(2) **`dasgltd/mcp-brasil` was recorded at "246★"; it has 0★, and 246 is its commit count** — the
same figure this KB carries, correctly labelled, in a **commits / tags** column of
`repos/trending.md`. A commit count was imported into the star column and carried for seven
weeks. 🔵 **There was therefore never a 7.3× star gap between two projects: there is one project,
and the KB was comparing it with a 0★ fork of itself.**

🟢 **What to do in a deliverable:** pin `Mcp-Brasil/mcp-brasil` and pin a commit — the
pin-a-commit advice stands, for versioning reasons rather than identity ones.

### What this pass searched for and did not find — stated as a gap, not as silence

| Looked for | Where | Result |
|---|---|---|
| A ministry-published **tutoring or assessment agent** | 5 ministry names; `org:Utdanningsdirektoratet` (18 repos, all read) | 🔴 **none.** Udir publishes a curriculum endpoint, an exam-admin system, a design system, two Moodle plugins and CI tooling. **No agent.** |
| A **French** curriculum agent | `eduscol`, 107 results | 🔴 **none licensed.** ⚠️ One real candidate: `VictorNain26/tomai-curriculum` — *"Index RAG de TomIA — l'index des programmes du collège"*, a **RAG index over the French national curriculum**, **NO-PAYLOAD**. The nearest thing to a French curriculum agent in this KB, and it is ungranted. |
| A **Japanese** curriculum agent | `mext`, `monbukagakusho`, 1,701 results | 🔴 **none.** Only MEXT's kanji-by-grade tables as CC0 data (`fnshr/kyo-kan`). |
| A **Gulf** ministry agent | `"ministry of education"` + Gulf, 7,228 results | 🔴 **none** — and the count is void (it matches funding acknowledgements). |

🔵 **The shape across four regions is one finding: where a ministry publishes, it publishes the
substrate and leaves the agent to the market.** That is a sales fact, not a disappointment —
`P25` in `compose/patterns.md` is built on exactly that division of labour.

### 🟢 A connection worth recording: one LATAM author, two permissive education-data assets

[`SidneyBissoli/uis-mcp-server`](https://github.com/SidneyBissoli/uis-mcp-server) (MIT, UNESCO
UIS statistics with pinned releases and full provenance) is already on the MCP shelf above.
The same author published [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR)
— **MIT, on CRAN**, covering eleven INEP instruments (Censo Escolar, ENEM, SAEB, ENADE, CAPES,
FUNDEB and more). 🟢 **One identifiable individual is supplying both the global and the
Brazilian education-statistics access layer, permissively.** ⚠️ Which is also a
**bus-factor-of-one** note for anything built on either.

---

## Added in the seventeenth pass of 2026-10-06 — no new agent rows, one correction, and the reason both are the right outcome

**This pass adds zero rows to the tables above, and that is a finding rather than a shortfall.**
The channel it ran was the **ministry tier queried as `org:`** (`agents/trending.md`, Finding 4):
eight national bodies, of which two have a code estate — **188 repositories from Finland's
Opetushallitus and 6 from Sweden's Skolverket**. Not one of the 194 is an agent. They are
curriculum services, study registries, learner-identity registries, admissions form engines,
grant administration and an OER library.

🔵 **Four consecutive passes have now run a state channel and none has found a state-published
agent.** That is no longer a sampling result; it is the division of labour this KB sells into,
and it is already written as `P25` in `compose/patterns.md`: **the state ships the substrate and
leaves the agent to the market.** A fifth pass looking for a ministry tutor should expect to
find a ministry *API*.

### What this pass changed in the table above

| Change | Row | Why |
|---|---|---|
| 🟢 **Caveat lifted** | **MCP Brasil** | Identity settled by root-commit comparison. `Mcp-Brasil/mcp-brasil` is upstream and is the address to pin. |
| 🔴 **Figure withdrawn** | (prose) `dasgltd/mcp-brasil` **"246★"** | It has **0★**. 246 is its **commit count**, imported into the star column and carried since 2026-08-18. |
| 🔴 **Claim withdrawn** | (prose) *"the API reports neither as a fork"* | The rendered page reads *"forked from Mcp-Brasil/mcp-brasil"*. |

⚠️ **Nothing else on this shelf moved, and no row was re-measured this pass.** Star counts above
still carry their **2026-10-06** morning readings; `curl` on `github.com` returned **403**
throughout this pass, so a full re-read was not available at the price of one request per repo.

### 🔴 The licence finding that decides whether 188 repositories can ever appear on this shelf

Every Finnish payload read is **EUPL** (v1.1 or v1.2) — ten of ten. The EUPL is **OSI-approved**,
so this is not an exclusion; but it is **copyleft whose reach includes network use**, and
`lib/license_family.sh` — this KB's hardened classifier — contains **zero EUPL patterns**, so it
returns `UNCLASSIFIED` for all of them. The full trace is Finding 6 of `agents/trending.md`; the
commercial consequence is in `verticals/solutions.md` and `intel/trends.md` (§38).

🟢 **For an agent builder the practical reading is short:** an agent that **calls** these services
over their APIs is unaffected by their licence. An agent that **embeds or forks** their code into
a hosted client product inherits an AGPL-shaped obligation. **That boundary, not the star count,
is what decides the architecture** — and it is why this pass added a pattern (`P27`) rather than
a row.


### Eighteenth pass of 2026-10-06 — state the negative first: **no new agent**

**This pass added no row to the agent tables above, and that is the correct outcome rather than a
shortfall.** The channel run was the **standards-body conformance register** — searching by
*standard + conformance certification* instead of by topic, star count, funder, institution or
ministry name. It returned a substantial amount of permissive software, and **none of it is an
agent**: five MIT **QTI 3 item players and toolchains**, six MIT **national-service clients** from
the Dutch agency Kennisnet, and two **MCP servers** over a Chilean national open-data portal.

Those are shelved where they belong — `repos/foundations.md` and `verticals/solutions.md` — because
**putting components in the agent table is how a KB starts counting libraries as capabilities.**

**Three things from this pass do bear on the agents already listed:**

1. 🟢 **The assessment agents now have a deterministic scoring path, which they did not have.**
   [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (**MIT**, 30★,
   **1EdTech Certified** for QTI 3 Basic and Advanced "Delivery") runs a QTI item's **declared**
   response processing. Any generation agent in this KB — Educhain, the P11 chain, the item-bank
   patterns — can now be wired so that **the model proposes and the standard scores**, with the
   model demonstrably outside the scoring path. That is the single cheapest way to make an
   assessment deployment defensible under the EU AI Act's high-risk obligations and under the US
   "human judgment is final" rule (§16). Recipe: **P34**.
2. 🟢 **Curriculum alignment gains a permissive Python client.**
   [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) (**MIT**, © 2018)
   reaches **Eduterm**, the Dutch national curriculum vocabulary — the P29 "curriculum alignment as
   a tool call" shape, already written, in the language the agents here are written in.
3. 🔴 **A fork nearly entered this file as a public-body asset, for the second consecutive pass.**
   [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) is **forked from
   [`Citolab/qti-components`](https://github.com/Citolab/qti-components)** — identical root commit
   `de8b27b`, **2,377 commits against upstream's 2,456, so 79 behind**, 1★ against 19. Caught by
   running `git clone --filter=blob:none --no-checkout` **before** the row was written rather than
   after. Pass 17 spent a whole pass correcting the same class of error in `mcp-brasil`. **The
   instrument did not change; when it was run did.** Fork-lineage is a **pre-write** check.

⚠️ **The star counts and licences in the tables above were not re-read this pass.** They carry the
2026-10-06 readings recorded by the passes that took them. A cell saying *not read this pass* in an
earlier section still means exactly that.
