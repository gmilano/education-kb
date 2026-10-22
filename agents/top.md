---
industry: education
region: Global
updated: 2026-10-22
---

# Top education AI agents

**Pass `p390` · 2026-10-22.** The shelves below are the deliverable: real repositories, licences read
from the payload, and a **last-commit date on every row**. This pass trimmed the ~120-line pass
narrative that had grown back above the first table — a studio opening a client engagement should hit
a usable shortlist in the first screen, not a journal about how the shortlist was measured. The
trimmed text is kept verbatim at
[`archive/2026-10-22-p390-pre-trim/agents-top.md`](../archive/2026-10-22-p390-pre-trim/agents-top.md);
the method that survived it is one paragraph under *[How these rows were verified](#how-these-rows-were-verified)*,
and the durable licence lesson is `Pattern L` in [`compose/patterns.md`](../compose/patterns.md).

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p390.tsv) — **158 addresses
probed, 145 live, 13 unreadable**, every licence read from the payload at the repository's **real
default ref**, every live row dated. This pass audited **every slug carried as a recommendation**
across `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` and `compose/patterns.md`
(138 distinct addresses), which is why the corrections below are about *this base's own shelves*
rather than about the supply in general.

## What `p390` changes

| # | finding | where it bites |
|---|---|---|
| 1 | 🔴 **The LTI integration path on three shelves is abandoned.** [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) (Apache-2.0) last moved **2020-06-03 — 2,332 days**. LTI 1.3 is *the* standards surface for putting an agent inside Moodle, Canvas, Blackboard or D2L, and this base recommends it in `repos/foundations.md`, `verticals/solutions.md` **and** `compose/patterns.md`. | Treat as a **spec reference to vendor**, never a dependency to install. The grant is fine; the maintenance is not. |
| 2 | 🟢 **The Open edX copyleft firewall is in the platform's own packaging, and it is better than the stale LTI route.** [`openedx/edx-platform`](https://github.com/openedx/edx-platform) is **AGPL-3.0** — but the component API a plugin actually imports, [`openedx/XBlock`](https://github.com/openedx/XBlock), and its [`xblock-sdk`](https://github.com/openedx/xblock-sdk), are both **Apache-2.0** (read from `LICENSE.TXT`, both dated **2026-10-22**). So an XBlock can be **MIT or proprietary while running inside an AGPL platform**, with no LTI hop and no fork. 🔴 The boundary is per-package, not per-org: [`openedx/openedx-learning`](https://github.com/openedx/openedx-learning) and the frontend apps are **AGPL-3.0**, so importing those pulls copyleft back in. | This is the licence explanation for why [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) (MIT, Tier 4) can ship as an Open edX plugin at all. Recorded in `Pattern A`. |
| 3 | 🔴 **Two more shelved foundations are effectively abandoned.** [`serlo/serlo.org`](https://github.com/serlo/serlo.org) (Apache-2.0) → **1,351 days**; [`projectfedena/fedena`](https://github.com/projectfedena/fedena) → **3,746 days and no licence file at all**. | Both demoted in `repos/foundations.md`. |
| 4 | 🔴 **A wrong-slug trap, and it inverts the licence.** [`PeerTube/PeerTube`](https://github.com/PeerTube/PeerTube) is a **3,660-day** stale mirror reading **GPL-3.0**; the canonical project is [`Chocobozzz/PeerTube`](https://github.com/Chocobozzz/PeerTube) — **AGPL-3.0, 6 days**. Same for [`apache/ofbiz`](https://github.com/apache/ofbiz) (**3,539 days**) vs [`apache/ofbiz-framework`](https://github.com/apache/ofbiz-framework). | A slug that resolves is not a slug that is maintained, **and the two refs can carry different grants.** |
| 5 | 🟢 **A permissive courseware platform was missing from every shelf here.** [`Simon-Initiative/oli-torus`](https://github.com/Simon-Initiative/oli-torus) — **MIT**, committed **today**: Carnegie Mellon's Open Learning Initiative courseware engine with adaptive activities and learning analytics. Note the slug: `CMU-OpenLearning/oli-torus` **does not resolve**. | New row in `verticals/solutions.md` and `repos/foundations.md`. MIT courseware is rare; almost everything at this scale is AGPL. |
| 6 | 🟢 **A LATAM-native voice tutor, and it is the first voice-first row on these shelves.** [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent) ("Manu") — **MIT, 15 days**, Brazilian-Portuguese spoken maths tutor on **LiveKit Agents**, 1st grade → university. | New **Tier 4** row below, and 🆕 `Pattern V` in [`compose/patterns.md`](../compose/patterns.md). |
| 7 | 🟡 **A licence read corrected, in this base's favour.** [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) has **no root licence file**, which reads as ungranted — but `docs/License.txt` carries the full **GPL-2.0** text. | Granted, copyleft. Recorded in `verticals/solutions.md`. The root tree is not the whole payload. |
| 8 | 🔴 **The curriculum-taxonomy licence now has an exact SPDX pair, and it is worse than "a database licence."** [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) declares **`(ODbL-1.0 AND CC-BY-SA-4.0)`** in `package.json`, with a second `LICENSE-CONTENT` file. | **Share-alike on the content**: a curriculum derived from it inherits CC-BY-SA-4.0. That is a client-deliverable question, not an engineering one. |
| 9 | 🟡 **`instructure/canvas-lms` `master` is 175 days stale — and that is not the signal.** Canvas ships from **tags** (`v5.14.2` is current). A last-commit date on the default ref under-reports any project that releases off tags. | Dating caveat recorded; Canvas is *not* demoted. |
| 10 | 🟢 **`OpenMAIC` is MIT, and the AGPL claim in circulation is now sourced.** `p389` read MIT from the payload; this pass found the contradicting claim in the wild — **SourcePulse** and **AllClaw** both publish "AGPL-3.0, commercial licensing by contact." The payload `LICENSE` ("MIT License, Copyright (c) 2026 THU-MAIC") and `package.json` (`"license": "MIT"`) agree with each other and against them. | `Pattern L` holds: **read the payload, not the review site.** |

🔵 **One honest non-finding.** The five "published-but-unreadable" repositories `p388` recorded
([`thanh01pmt/interactive-quiz-kit`](https://github.com/thanh01pmt/interactive-quiz-kit),
[`Mckaroff/GraphLMS`](https://github.com/Mckaroff/GraphLMS),
[`ale-alejandro/beadkit`](https://github.com/ale-alejandro/beadkit),
[`AI-Matrix-Engine/aidream`](https://github.com/AI-Matrix-Engine/aidream),
[`yokowasis/autograder`](https://github.com/yokowasis/autograder)) plus
[`santillana-ai/tutor-sdk`](https://github.com/santillana-ai/tutor-sdk) **are all still unreadable**
— they are the 13 non-live rows in this pass's evidence, together with speculative slugs this pass
tried and missed. A blobless clone cannot tell *private* from *deleted*, so these are recorded as
`DEAD-OR-PRIVATE` and **no row claims they were removed from GitHub**. Nothing changed about them;
the status is confirmed, not new.

## How these rows were verified

No popularity channel is readable in this sandbox — `api.github.com` → **403**, `github.com` HTML →
**403** — so **no row here carries a star count**, with the single exception of OpenMAIC's `~41.3k ★`,
which `p389` read off a rendered page and is labelled as such. Ranking is by what a studio can act
on: licence permissiveness, maintenance date and fit. Dating and licence reads come from `git` read
access, which **is** open to every public repository:

```bash
# ~1.2 s per repository, no credentials, no API
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/&lt;owner&gt;/&lt;repo&gt; r
git -C r symbolic-ref --short HEAD    # the REAL default ref — not always main/master
git -C r log -1 --format='%H %cI'     # HEAD sha + last commit date  ← the maintenance signal
git -C r ls-tree --name-only HEAD     # root tree: is there a LICENSE at all?
git -C r show HEAD:LICENSE            # the GRANT, from the payload at that ref
git -C r show HEAD:package.json       # the manifest, which must agree with it
```

Two limits of that method, stated because they shape the rows: a **last-commit date under-reports
tag-shipping projects** (finding 9), and a **failed clone cannot distinguish private from deleted**
(the non-finding above).


## Tier 1 — Tutoring and instruction agents

| agent | repo | default ref | licence | what it actually does | origin |
|---|---|---|---|---|---|
| **OpenMAIC** 🆕 `p389` | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | `main` | 🟢 **MIT** *(1,066 B, "Copyright (c) 2026 THU-MAIC"; `package.json` also declares `"license": "MIT"`)* | **The whole classroom, generated — and the largest education-native repository in the open-source supply (~41.3k ★).** A topic or an uploaded document becomes a multi-agent lesson: an AI teacher with a voice, teaching assistants, simulated classmates, narrated slides, auto-graded quizzes, HTML interactives and a shared whiteboard, with **agentic mid-lesson chat about any slide element**. Grew out of **MAIC**, deployed inside Tsinghua and validated on **700+ real students**; paper in **JCST 2026**. 🟢 Three properties that decide a school deployment and that almost nothing else on this shelf has: **server-first** generation (v1.2.0) that survives closed tabs and restarts on PostgreSQL; **central model governance** — every AI use is a named *slot* in `openmaic.yml`, each slot pinned to a provider, with an option to **forbid user-supplied keys** outright and `video: null` to switch a capability off; and **export of a finished classroom as one offline HTML file** (or a PPTX that keeps every scene). 🟢 Local-model path is real: **Lemonade** for local inference, **FunASR** for local ASR. 🟢 **24 built-in skills** plus per-owner authored skills; the course agent works through validated tools (patch one scene atomically, reorder pages, import `.pptx` with layout) rather than rewriting opaque blobs. 🟢 Security is handled like a product, not an afterthought — five releases since September carry SSRF, DNS-rebinding and provider-redirect fixes under published GHSAs. 🔴 Current head is **v1.3.0-rc.1** (knowledge base, 2026-10-22) with **breaking upgrade conditions and no rollback below it**; pin **v1.2.1** (2026-10-18) for a pilot. 🔴 Needs Node ≥ 22.19, pnpm ≥ 10, PostgreSQL 16 and a long-running server — Vercel deployments are capped at the 1.1.x line. | APAC — Tsinghua University, China (EN + zh-CN) |
| **OATutor** 🆕 `p389` | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | `main` | 🟢 **MIT** | **The adaptive tutor with the mastery model in the open, and the one with an academic maintainer behind it** — UC Berkeley's CAHLR. Intelligent-tutoring scaffolds over an open problem bank, with **Bayesian Knowledge Tracing** driving what comes next, so "adaptive" is a parameterised model a client can inspect and re-estimate rather than a prompt. Pairs with [`pyBKT`](https://github.com/CAHLR/pyBKT) (MIT) on [`repos/foundations.md`](../repos/foundations.md), which fits the model from the client's own interaction logs. 🟢 Dated **2026-10-21** — this is a live project, not a paper artefact. 🟡 Content-first: the win is the scaffold-and-mastery machinery, not an LLM. | North America — UC Berkeley CAHLR |
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main` | 🟢 **Apache-2.0** | Lifelong personalised tutoring: persistent learner memory plus RAG grounded in the learner's own uploaded materials. The most substantial permissive tutor in the open-source supply. | APAC — HKU Data Intelligence Lab, Hong Kong |
| **ai-shifu** | [AI-Shifu/ai-shifu](https://github.com/AI-Shifu/ai-shifu) | `main` | 🟢 **Apache-2.0** *(grant at `LICENSE.txt`, not `LICENSE`)* | AI-led chat-based course delivery — the agent drives the lesson script rather than waiting to be asked. | APAC — China |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | `main` | 🟢 **MIT** | Content generation for instructors: quizzes, lesson plans, question banks, YouTube-to-course. Teacher-facing, which is where the fastest-growing region's market actually is. | APAC — India |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main` | 🟢 **MIT** | AI-native LMS with an AI Mentor and role-play scenarios built in rather than bolted on. | EMEA — Selleo, Poland |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main` | 🟢 **BSD-3-Clause** | Self-hostable tutoring platform with local RAG over textbooks and notes — the data-residency option. | not verified this pass |
| **tutor-gpt** | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main` | 🟡 **GPL-3.0** | Theory-of-Mind tutoring: models the learner's mental state to pitch the explanation, rather than retrieving a better paragraph. Pedagogically the most interesting approach here. 🔴 🆕 `p389` **Dated: last commit `2025-11-13` — 343 days.** Keep it on the shelf as the clearest *statement* of learner-state modelling, but it is no longer a maintained dependency, and GPL-3.0 was always the harder sell. | North America |
| **ChatTutor** | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | `main` | 🔴 **AGPL-3.0** | Visual, interactive tutor. Network copyleft — hosting it as a service triggers source obligations. | APAC |
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **`dev`** | 🔴 **AGPL-3.0** | AI-native course platform. Note the default ref is `dev`: a `main`-assuming clone or licence read fails silently. | EMEA |
| **Learn Shell** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | `main` | 🔴 **AGPL-3.0** at `main` — 🟢 **MIT at tag `v0.1.0`** | 🆕 `p385`. **Agent-native teaching OS: the classroom is the server and the agent is bring-your-own.** Courses, lessons, FSRS-scheduled flashcards, graded exercises, mindmap, document reader, and a memory layer the agent reads back (`get_context` / `get_learner_brief`) instead of re-deriving the learner each session. ~50 tools over MCP, self-describing via a `manifest://capabilities` resource. 🔴 v1 is explicitly **single-machine and unauthenticated** — not multi-tenant as it stands. | APAC — China (MCP tool descriptions and prep-report are Chinese-first; docs English-first) |
| **OpenTutor** | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main` | 🟢 **MIT** *(1,068 B, © 2026 Zijin Zhang)* | 🆕 `p386`. **Block-based adaptive workspace that runs entirely on the client's own machine.** Course material in (PDF), structured notes, flashcards, quizzes and an adapting tutor out; **FSRS** spaced repetition, a knowledge graph and cognitive-load detection are in the product rather than on the roadmap. Next.js 16 + Python 3.11, Docker, **runs on local open-weight models with no API key and no data leaving the host**. 🟢 The data-residency tutor with a *permissive* grant — which [Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3) was the only other candidate for. 🟡 One maintainer; bilingual EN / zh-CN. | APAC — China |
| **Aha Tutor** (开窍) | [BaronCyrus/dsh-aha-tutor](https://github.com/BaronCyrus/dsh-aha-tutor) | `main` | 🟢 **MIT** *(1,067 B)* | 🆕 `p388`. **The most complete statement of adaptive-tutoring design on these shelves.** Builds a course from one sentence or an uploaded textbook, establishing the learner's baseline, goal, time budget and desired course size *before* writing a unit → chapter → lesson blueprint. Delivery is a **narrated handwriting blackboard** (formula-driven curves computed point-by-point, draggable parameters). 🟢 Mid-lesson checks **record confidence**, so a lucky guess, a hesitant answer and a confident wrong answer are three different events; weak points earn an automatic consolidation lesson. 🟢 A **"this step is wrong?"** button re-checks, corrects the blackboard, and **re-grades past attempts and the mastery estimate**. FSRS review, printable cheat sheets, video/PDF export. Built as a **DeepSeek Harness** extension; npm `dsh-aha-tutor` v1.7.0, published **2026-10-22**. 🟡 Single maintainer. | APAC — China (Chinese-first) |

## Tier 2 — Research and literature agents (higher education)

| agent | repo | default ref | licence | what it actually does |
|---|---|---|---|---|
| **paper-qa** | [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main` | 🟢 **Apache-2.0** | Citation-grounded Q&A over a paper corpus that **declines to answer** without retrieved evidence. The refusal behaviour is the compliance story under EU AI Act Art. 50. |
| **OpenScholar** | [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main` | 🟢 **Apache-2.0** | Retrieval-augmented synthesis across scientific literature. |
| **ai2-scholarqa-lib** | [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main` | 🟢 **Apache-2.0** | The library behind AI2's Scholar QA — a production reference, not a demo. |
| **gpt-researcher** | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main` | 🟢 **Apache-2.0** | Autonomous multi-source research agent; the generic backbone for a guided-inquiry assignment. |

## Tier 3 — Assessment and classroom-infrastructure agents

| agent | repo | default ref | licence | what it actually does |
|---|---|---|---|---|
| **jupyter-ai** | [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main` | 🟢 **BSD-3-Clause** | LLM assistance inside JupyterLab — the surface where most CS and data-science teaching already happens. |
| **pybryt** | [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Assesses the **approach** a student's code takes, not only its output. Pairs with an LLM that explains *why* the approach was wrong. 🔴 🆕 `p387` **No PyPI release since `v0.7.0`, 2022-04-28 — four and a half years.** The idea is still the best available statement of approach-assessment and `Pattern B` still stands on it, but treat it as **a reference implementation to vendor and maintain, not a dependency to install**. Repository commit activity is unreadable here (`github.com` 403), so this is a statement about the *published artefact*, which is what a client would install. |
| **canvas-mcp** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | MCP server over Canvas LMS: courses, assignments, submissions, grading, rubrics, students. Fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT) adds office-hours, syllabus read/write and course-content copy. |
| **Flat** | [netless-io/flat](https://github.com/netless-io/flat) | `main` | 🟢 **MIT** | Open-source online classroom (interactive whiteboard, recording) — the live-session substrate an agent can sit in. |
| **jupyter-ai-tutor** | [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` | 🟢 **BSD-3-Clause** *(1,532 B)* | 🆕 `p388`. **The maintained notebook-tutor layer, and the replacement for `Pattern B`'s stale dependency.** Per-cell **Explain Code** button sends the cell source, kernel language, **the error traceback**, and the preceding cells up to the last markdown cell *as the exercise statement*. 🟢 Two pedagogically serious details: the tutor persona lives in a **`TUTOR.md` discovered by walking up from the notebook's directory**, so each course or folder carries its own in version control; and an optional **`reference_solution` + `evaluation_criteria` in cell metadata, ROT13-encoded** to keep it out of the student's view. From **QuantStack**, a known Jupyter-ecosystem maintainer. Requires `jupyter-ai-jupyternaut` (<0.1). v0.3.2, 7 releases, → 2026-09-25. |
| **BC Curriculum MCP** | [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p388`. **The North American curriculum-grounding instance** — the third region to get one, after Brazil's BNCC agent (`p387`) and `os-taxonomy` (`p384`). 12 MCP tools over the **entire BC Ministry of Education K–12 curriculum**, crawled into SQLite: Big Ideas / Curricular Competencies / Content in the real three-column **KDU** structure with elaborations, Core Competencies, grade progressions, cross-subject connections, full-text search — and the **First Peoples Principles of Learning**, a jurisdictional requirement no generic tutor carries. Hosted HTTP endpoint or local stdio via `npx`. 🟡 2 releases, both **2026-03-27**; the data is a crawl, so currency is the risk, not the licence. |
| **tudelft-mcp** | [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p388`. **The EMEA institution-specific pattern, and the best-governed write path read so far.** One server over **four** systems a real university runs — Brightspace, **OSIRIS** (official records), MyTimetable and the public Study Guide — behind a single browser sign-in **including MFA**, with a self-renewing session. 🟢 **Every write (submitting an assignment, joining a group, replying in a discussion, registering for a course or exam) shows a preview and requires confirmation** — the human-in-the-loop control EU high-risk obligations ask for, shipped as the default. v0.1.4, → 2026-10-07. |
| **Canvas Toolchain** | [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` | 🟢 **MIT** *(1,063 B)* | 🆕 `p388`. **Teacher-facing semester refresh** — `Trend 5`'s shape exactly. Reads a Canvas backup archive plus lecture transcripts, **scores topic currency**, plans the next semester, and emits Canvas-safe HTML. 🟢 The **no-token "generate the HTML and paste it in"** path is first-class, so it delivers value without an API token or admin approval — which is how a pilot actually starts. 🟡 Installer is not code-signed; `npx canvas-toolchain` avoids it. → 2026-08-29. |

## Tier 4 — 🆕 `p387` LATAM-native agents (the tier `Gap 386-C` said did not exist)

Every row re-read first-hand on 2026-10-22 at the repository's **real default ref**, resolved with
`git ls-remote --symref`. These are **not** English-language agents with Spanish strings bolted on:
each is built by a LATAM institution or developer against a LATAM curriculum, platform or
constraint, and the prose in the repository is Spanish or Portuguese first.

| agent | repo | ref | licence | what it actually does | origin |
|---|---|---|---|---|---|
| **TutorIA** | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main` | 🟢 **MIT** *(1,069 B, © 2026 Grupo Sirius)* | 🟢 **The one LATAM-native agent built as an LMS plugin rather than a standalone app.** Conversational tutor delivered **inside Open edX as an XBlock/plugin**, FastAPI backend, Claude API, TTS audio replies, animated avatar, **teacher statistics panel**, context persistence across sessions. Shipped for **rural higher education in Risaralda, Colombia**; first subjects Programación I (Python) and Introducción a la Matemática. Docker + Azure, GitHub Actions. 🟡 Read the licence boundary below before quoting it. | LATAM — Universidad Tecnológica de Pereira, Colombia |
| **Agente BNCC para professores** | [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main` | 🟢 **MIT** *(1,074 B; `package.json` also declares MIT)* | 🟢 **Curriculum-grounded generation with the hallucination gate in the product, not the roadmap.** Lesson plans and exams-with-answer-keys anchored to official **BNCC** skill codes (Brazil's national curriculum): the model writes the prose, but every code and skill description comes from the official base and **an invented code is discarded before it reaches the teacher**. 1st year of Fundamental → 3rd year of Ensino Médio, cross-term skill selection, student/teacher PDF pairs, keyed **API v1** so a school's own systems call the same agent, Gemini or DeepSeek per request. Next.js 16 + TypeScript. | LATAM — Brazil |
| **TechLead AI Tutor** | [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main` | 🟢 **MIT** *(1,069 B, © 2026 Thiago Silva)* | Programming and software-engineering tutor built to **refuse to hand over the code**: spec-driven planning before any line is written, and **the agent that teaches is not the agent that verifies** — mechanical sensors grade the build. The clearest open statement of anti-dependency tutoring design on these shelves. | LATAM — Universidade Federal do Agreste de Pernambuco (UFAPE), Brazil |
| **Manu** 🆕 `p390` | [Jeanikt/tutor-ai-agent](https://github.com/Jeanikt/tutor-ai-agent) | `main` | 🟢 **MIT** | 🟢 **The first voice-first row on these shelves, and it is LATAM-native.** A spoken maths tutor in **Brazilian Portuguese** that re-pitches the same concept from 1st grade to university, built on **[LiveKit Agents](https://github.com/livekit/agents)** (Apache-2.0) in TypeScript — so the realtime STT → LLM → TTS pipeline, turn detection and interruption handling are an upstream dependency rather than this project's own code. 🟢 Voice matters more here than in English-first markets: it reaches learners with low typing fluency and the shared-device households that `Trend 10` describes, and it sidesteps the written-Portuguese barrier for early grades. 🔴 **Early — the README states "in development" with no public deployment**, and the maths-correctness layer is the LLM itself, with no symbolic checker. Dated **2026-10-07 (15 days)**. Take it as a **working reference for the voice pipeline**, not a deployable tutor; see 🆕 `Pattern V`. | LATAM — Brazil (pt-BR) |

🟡 **The licence boundary on TutorIA, stated because a studio will hit it on day one.** The plugin's
own grant is MIT and a studio can keep its changes closed. **Open edX itself is AGPL-3.0**, and
TutorIA is delivered as an XBlock inside it — so the *platform* obligations are untouched by the
plugin's MIT grant. Deliver it the way `Pattern A` and `Pattern O` deliver every agent into a
copyleft LMS: **the agent is a separate service the plugin calls**, and the plugin stays thin.

🔴 **Ungranted, and recorded so nobody re-finds them as candidates** (no licence file at any of the
eight probed paths, no `license` field in any manifest):
[Daniel-ux1026/Tutor-Inteligente](https://github.com/Daniel-ux1026/Tutor-Inteligente) (Peru —
offline-first PWA, 1.°–5.° de secundaria, explainable decision-tree difficulty selection; **this is
the one that hurts**, because `Pattern D` wants exactly this and cannot use it),
[FXArth/Tutor-Programacao](https://github.com/FXArth/Tutor-Programacao) (Brazil),
[henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) (Brazil, RAG
tutor, default ref **`master`**).

## Tier 5 — 🆕 `p388` Parent and guardian agents (the persona no shelf here had)

These shelves have carried the learner, the teacher and the institution since they were built. **The
parent was absent** — the word "observer" appeared in exactly one file before this pass. The registry
discovery channel surfaced three granted servers for that persona, two by one maintainer working the
problem deliberately across two different platforms.

🔵 **Why it is a market fact, not a curiosity.** Every North American instrument this base tracks puts
**family transparency** in the statute — Oklahoma SB 1734 names it outright, and Maryland's act is
built around guidance districts must hand down. A parent-facing read surface is the one place where
"transparency" becomes a *product* instead of a policy document. It is also the only education
persona with **no incumbent vendor lock**, because the parent portal is a feature of the SIS rather
than a market of its own.

| agent | repo | ref | licence | what it actually does | platform |
|---|---|---|---|---|---|
| **infinitecampus-mcp** | [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | 🟢 **The first SIS-side parent portal on these shelves.** 20 tools over **Campus Parent**: schedule, assignments (`missingOnly`), grades plus a 14-day recent-grades window, **attendance events with codes and comments**, behavior, food service, documents, standardized **assessment scores**, fees, and messaging from three distinct sources. Linked districts auto-discovered via **CUPS SSO**, and it is `FeatureDisabled`-aware, so it degrades per district instead of erroring. **47 npm releases**, → 2026-10-19. | Infinite Campus |
| **canvas-parent-mcp** | [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | The same scope against Canvas: 18 `canvas_*` tools held deliberately to **the read-only parent-observer surface** (`canvas_list_observees` is the hinge), plus student self-access. Four auth modes tried in priority order. 🟢 The download tool is properly hardened — host-pinned to your Canvas origin, writes only inside a download directory, never through a symlink, new files `0600`. **43 npm releases**, → 2026-10-16. | Canvas |
| **mtgibbs/canvas-lms-mcp** | [mtgibbs/canvas-lms-mcp](https://github.com/mtgibbs/canvas-lms-mcp) | `main` | 🟢 **MIT** *(1,064 B)* | Canvas read access framed first at *"parents monitoring their child's academic progress"*: due-this-week, missing work across all classes, grade questions in natural language. 🟡 **Last published 2026-02-13** — eight months. Shelved for the framing; take the row above as the dependency. | Canvas |

🔴 **The compliance edge, stated before anyone builds on these.** All three are **personal-credential**
tools — a parent's own token, OAuth, or a scraped session. That is fine for a parent acting for their
own child. **The moment a studio hosts one on behalf of a district, the credential becomes
institutional and the read becomes a FERPA-governed disclosure of an education record.** The persona
is new; the obligation is not. `Pattern P` is built around that boundary.

## Courseware, not agents — but the fastest way to staff a team

| repo | default ref | licence | note |
|---|---|---|---|
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main` | 🟢 **MIT** | 12-lesson agent curriculum. Frequently mis-listed as an agent in roundups; it is a course. |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | `main` | 🟢 **Apache-2.0** | Hugging Face's agents course. |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | 🔴 **`development`** | 🟢 **MIT** | Open courseware delivery components. Default ref is `development`. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | `main` | 🟢 **MIT** *(1,070 B stock, © 2026)* | 🆕 `p384`. Model foundations → LLM systems → agents, with a retrieval-evaluation lab and local graders. A **staffing** asset for the studio, not a deliverable component. |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | `main` | 🟢 **MIT** *(1,070 B stock)* | 🆕 `p384`. Curated use-case index with an education section. 🟡 It is a **list** — roundups file it as an agent; it is not one. |

## 🔴 No licence file — and "ungranted" is three different things

Five repositories on these shelves have **no licence file at any of seven probed paths**. 🔵 **That
is where this pass's own first draft stopped, and it was wrong to.** This base's `gate-enumeration`
refused the draft, so the manifests and source headers were read too — and the five split into
three classes that call for three different decisions:

| repo | no licence file at 7 paths | but the manifest / headers say | verdict |
|---|---|---|---|
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | ✔ (`LICENSE` `LICENSE.md` `LICENSE.txt` `LICENCE` `COPYING` `LICENSE-MIT` `license`) | `pyproject.toml` present, **no `license` field** | 🔴 **UNGRANTED — do not ship** |
| [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | ✔ | no manifest found | 🔴 **UNGRANTED — do not ship** |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ✔ | `package.json` → **`"license": "MIT"`**, and its `files` array even **names a `LICENSE` that is not in the tree** | 🟡 **MANIFEST-ONLY MIT.** A published npm-style grant with the file missing. Reusable in practice, but ask the maintainer to commit the file — and record the manifest line you relied on |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | ✔ | `package.json` → **`"license": "MIT"`** | 🟡 **MANIFEST-ONLY MIT** |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | ✔ | **`version.php` carries the full GPL-3.0-or-later header** — *"either version 3 of the License, or (at your option) any later version"* | 🟢 **GPL-3.0-or-later, granted in the source headers.** Standard and required practice for a Moodle plugin; the missing root file is a packaging habit, not a missing grant |

🆕 `p386` — **three more ungranted addresses, and one of them matters more than the others.**

| repo | result | why it is recorded |
|---|---|---|
| [Nutlope/llamatutor](https://github.com/Nutlope/llamatutor) | 🔴 **UNGRANTED** — nothing at 9 paths, no manifest licence field | 🔴 **It circulates widely as "an open-source AI personal tutor"** and is still returned by the prescribed global search leg. It is not reusable as it stands. The most-cited tutor on the open web and the most-cited *granted* tutor are not the same repository. |
| [jarodise/Language-Transfer](https://github.com/jarodise/Language-Transfer) | 🔴 **UNGRANTED** | Surfaced by the LATAM search leg. 🔵 Also a category error worth naming: it teaches **Spanish to non-speakers** inside an agent CLI — it is not a Spanish-language tutor for Spanish-speaking learners, which is the thing the LATAM supply gap is actually about. |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | 🔴 **UNGRANTED** | The one ungranted server of the nine Blackboard addresses probed. |

🔵 **The lesson is now `Pattern L` step 8** in [`compose/patterns.md`](../compose/patterns.md):
*a missing `LICENSE` file is a reason to read the manifest and the source headers, not a verdict.*
Three of these five would have been wrongly rejected by a file-only read — including the one
plugin Moodle's own directory distributes.

For Moodle, use the **`webservice_mcp` plugin from Moodle's own plugin directory** instead
(Moodle 4.5–5.2, latest release 23 Jul 2026) — see [`compose/patterns.md`](../compose/patterns.md).

### 🆕 `p388` — a fourth class: **the licence can be missing from the payload while the manifest claims it, and the repository can be closed while the artefact is readable**

The discovery sweep turned up a case that none of the three classes above describes, and it involves
the largest organisation to appear on these shelves: **Santillana**, one of the biggest education
publishers in Spain and Latin America. It is the first time a major regional publisher's own AI
tutoring code has surfaced here. **It does not survive procurement.**

| package | npm history | declared licence | licence file **in the published tarball** | repository |
|---|---|---|---|---|
| `@santillana-ai/create-tutor-app` | **v5.9.0, 63 versions**, 2025-08-28 → 2025-10-21 | 🟡 **`"license": "MIT"`** in `package.json` | 🔴 **NONE** — tarball read first-hand (38,447 B): `README.md` and templates only | 🔴 [santillana-ai/tutor-sdk](https://github.com/santillana-ai/tutor-sdk) — `git ls-remote` **prompts for credentials** |
| `@santillana-ai/typescript-tutor-sdk` | **v5.9.0, 115 versions**, 2025-08-27 → 2025-10-21 | 🔴 **`license` field absent entirely** | 🔴 **NONE** — tarball read first-hand (896,006 B): `README.md` only | 🔴 no `repository` field at all |

🔴 **Verdict: UNGRANTED — do not ship.** Note *which* package fails. The MIT claim sits on the
**scaffolder**, a one-command project generator. The package a client's codebase would actually
depend on — **`typescript-tutor-sdk`, 115 published versions** — declares **no licence at all**,
ships no licence text, and names no repository. Both are in any case **clients for a proprietary
keyed API**, so even a clean grant would buy an SDK, not a tutoring engine.

🔵 **Three method points that generalise past this case:**
1. **`git ls-remote` separates *private* from *absent*.** A credentials prompt is not a 404 — the
   repository exists and is closed. This base can now write "closed" instead of "dead".
2. **The tarball is the artefact, and npm serves it even when the repo is closed.** The licence that
   *ships* is a different question from the licence the repository *states*. Here the tarball settles
   it; `raw.githubusercontent.com` could not have.
3. 🔴 **A scoped npm org is not a corporate attestation.** `@santillana-ai` is consistent with
   Santillana and the sole maintainer is a plausible individual account, but **nothing read this pass
   ties the scope to the company** — recorded as `Gap 388-E`. The licence verdict does not depend on
   resolving it.

🔴 **And the same sweep found five more repositories in the published-but-unreadable state** — the
package ships, the source prompts for credentials. The one that costs the most:
**[thanh01pmt/interactive-quiz-kit](https://github.com/thanh01pmt/interactive-quiz-kit)**,
`@thanh01.pmt/interactive-quiz-kit` **v1.4.10 across 103 published versions** (2025-06-12 →
2026-09-23), manifest MIT, source closed — interactive quizzes with AI generation **and SCORM
support**, which is genuinely scarce in permissive open source. Also
[Mckaroff/GraphLMS](https://github.com/Mckaroff/GraphLMS) (`rhizome-lms-mcp`, manifest MIT),
[ale-alejandro/beadkit](https://github.com/ale-alejandro/beadkit) — whose manifest reads
🔴 **`"SEE LICENSE IN LICENSE"`, pointing at a file in a repository nobody can read**, a perfectly
circular grant — [AI-Matrix-Engine/aidream](https://github.com/AI-Matrix-Engine/aidream) and
[yokowasis/autograder](https://github.com/yokowasis/autograder). Full table in
[`agents/trending.md`](trending.md).

🔵 **The procurement rule this yields, and it is `Pattern L`'s new step:** for an npm-only
dependency, **the manifest is a claim and the tarball is the evidence**. A grant that points into an
unreadable repository is not a grant — and it is the one case where re-reading the payload cannot
save it.

🟡 **Two more manifest-only grants found this pass** (`Pattern L` class 3, reusable with the caveat
recorded): [TecFancy/dsh-deeptutor](https://github.com/TecFancy/dsh-deeptutor) — no licence file at
10 probed paths, npm `dsh-deeptutor` declares **MIT**; a DeepSeek Harness learning extension — and
[nanobpm/nano-ide](https://github.com/nanobpm/nano-ide) — no licence file, `@nanobpm/agentic`
declares **Apache-2.0**.

## Build-on-this tier

The permissive shortlist: every agent on these shelves a studio can build on and still hand a
client closed, client-owned code. 🆕 `p387`: **23 permissive rows** (19 at `p386`, **+4: three LATAM-native agents and `d2l-cli`**) — MIT, Apache-2.0 or BSD-3 only, no
copyleft, no bespoke clause, every grant read first-hand at the repository's real default ref.

| repo | ref | licence | use it for |
|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main` | Apache-2.0 | tutoring with learner memory |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main` | MIT | 🆕 `p386` — local-first adaptive workspace; tutoring with **no data leaving the host** |
| [AI-Shifu/ai-shifu](https://github.com/AI-Shifu/ai-shifu) | `main` | Apache-2.0 | agent-led course delivery |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `main` | MIT | teacher-facing content generation |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main` | MIT | AI-native LMS starting point |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main` | BSD-3-Clause | self-hosted tutoring, data residency |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main` | Apache-2.0 | citation-grounded answers that refuse without evidence |
| [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main` | Apache-2.0 | literature synthesis |
| [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main` | Apache-2.0 | production scholar-QA reference |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main` | Apache-2.0 | guided-inquiry research scaffold |
| [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main` | BSD-3-Clause | LLM help inside the teaching notebook |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | MIT | assess the approach, not the output |
| [netless-io/flat](https://github.com/netless-io/flat) | `main` | MIT | live online classroom substrate |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main` | MIT | governed campus LLM gateway |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | `main` | MIT | give the prompt pipeline a metric |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | `main` | Apache-2.0 | document-aware RAG over course material |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | `main` | MIT | the before/after measurement |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | `main` | MIT | retention scheduling with published parameters |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | `development` | MIT | courseware delivery components |
| [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main` | MIT | 🆕 `p387` — Spanish-language tutor **inside Open edX**; the LATAM reference deployment |
| [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main` | MIT | 🆕 `p387` — BNCC-anchored teacher generation with a curriculum-code gate |
| [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main` | MIT | 🆕 `p387` — tutoring that withholds the answer; author ≠ verifier |
| [Jeanikt/tutor-ai-agent](https://github.com/Jeanikt/tutor-ai-agent) | `main` | MIT | 🆕 `p390` — **voice-first pt-BR maths tutor**; the reference for a spoken tutor |
| [livekit/agents](https://github.com/livekit/agents) | `main` | Apache-2.0 | 🆕 `p390` — the **realtime voice substrate** (STT→LLM→TTS, turn detection) under any spoken tutor |
| [Simon-Initiative/oli-torus](https://github.com/Simon-Initiative/oli-torus) | `master` | MIT | 🆕 `p390` — **permissive courseware engine** (CMU OLI) with adaptive activities + analytics |
| [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli) | `main` | MIT | 🆕 `p387` — read-only Brightspace client written **for agents** (PyPI `d2l-cli` 0.3.0) |
| [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | `main` | MIT | 🆕 `p388` — **187-tool teacher/admin Canvas surface with a FERPA mode**; 87 releases, published 2026-10-22 |
| [Fireiscoolsolo/canvas-lms-mcp-local](https://github.com/Fireiscoolsolo/canvas-lms-mcp-local) | `main` | MIT | 🆕 `p388` — 209-tool **student-side** Canvas surface, opens no port |
| [chrischall/infinitecampus-mcp](https://github.com/chrischall/infinitecampus-mcp) | `main` | MIT | 🆕 `p388` — **the parent/guardian persona, SIS-side**; 47 releases |
| [chrischall/canvas-parent-mcp](https://github.com/chrischall/canvas-parent-mcp) | `main` | MIT | 🆕 `p388` — parent-observer scope over Canvas, hardened downloads |
| [QuantStack/jupyter-ai-tutor](https://github.com/QuantStack/jupyter-ai-tutor) | `main` | BSD-3-Clause | 🆕 `p388` — notebook tutor with a version-controlled `TUTOR.md` persona; **replaces `pybryt` as the live dependency** |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | MIT | 🆕 `p388` — **North American** curriculum grounding (BC K–12, incl. First Peoples Principles of Learning) |
| [danieltyukov/tudelft-mcp](https://github.com/danieltyukov/tudelft-mcp) | `main` | MIT | 🆕 `p388` — **EMEA**; four university systems, one MFA sign-in, **every write preview-confirmed** |
| [Ryfter/canvas-toolchain](https://github.com/Ryfter/canvas-toolchain) | `main` | MIT | 🆕 `p388` — teacher-facing semester refresh with **topic-currency scoring**; works with no API token |
| [BaronCyrus/dsh-aha-tutor](https://github.com/BaronCyrus/dsh-aha-tutor) | `main` | MIT | 🆕 `p388` — adaptive tutoring that **records answer confidence** and re-grades on correction |
| [SuperPiTT/moodle-rag](https://github.com/SuperPiTT/moodle-rag) | `main` | MIT | 🆕 `p388` — RAG over the **Moodle codebase**; cuts `Pattern A`'s build cost |

🔴 Deliberately **not** here, and why: `plastic-labs/tutor-gpt` (GPL-3.0) and
`HugeCatLab/ChatTutor`, `learnhouse/learnhouse` (AGPL-3.0) are run as **separate services**, never
linked. `microsoft/autogen`'s code grant is MIT but lives in `LICENSE-CODE`, so it needs the
per-file check below before it enters a deliverable.
🆕 `p385` **[sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) is not here either, and it is the
interesting case:** `main` is **AGPL-3.0**, but the project was **MIT until it relicensed on 2026-08-16**, and that
MIT grant is still readable at tag **`v0.1.0`** (1,081 B, read first-hand this pass). A studio that needs permissive
*can* pin `v0.1.0` — but it inherits a frozen tree with **no upstream path**, because every commit since is AGPL.
🔵 Pinning a tag to dodge a relicence buys the licence and gives up the project. See **Pattern L step 10**.

## MCP servers by LMS platform

MCP reached the LMS in 2026 and this is the integration path that did not exist a year ago.
🆕 `p386`: **6 platforms** are reachable through the servers below — LMS platforms, counting Anki's
spaced-repetition loop separately because it is not an LMS. Blackboard joined the table at `p386`,
with a verified grant for the first time.

### Agents over the systems

🆕 `p387`: **25 distinct MCP server slugs appear in this section's table** — **23 platform rows**,
every one resolved and licence-read first-hand on 2026-10-22 (12 at `p383`–`p385`, 11 added at
`p386`), **plus two fork addresses named inside a row's note** (`lmgveerhoek/brightspace-mcp-server`
and `matthewliu10/brightspace-mcp-server`, both byte-identical to their upstream).
🔵 **The count and the scope are stated together on purpose.** `p278` registered this claim as
*"MCP server slugs in the MCP section's table"* but anchored it to a sentence about **rows**, so
the instrument measured 25 while the shelf said 23 and the gate read STALE with nothing actually
wrong. `p387` re-points the anchor at the quantity the instrument measures — slugs — and keeps the
row count in the same sentence, because a reader wants rows and the gate wants slugs.

| platform | server | ref | licence | note |
|---|---|---|---|---|
| **Moodle** | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | `main` | 🟡 **GPL-3.0-or-later, in the source headers** (no root licence file) | 🟢 **The first-party path.** The GitHub home of the `webservice_mcp` plugin listed in **Moodle's own plugin directory** (Moodle 4.5–5.2, latest release 23 Jul 2026, gated on `webservice/mcp:use`). No root `LICENSE`, but `version.php` carries the full GPL-3.0-or-later header, as Moodle requires of every plugin. Granted — and GPL is survivable here, because the agent reaches it over JSON-RPC rather than linking to it. |
| **Moodle** | [lmscloud-io/moodle-mcp-server](https://github.com/lmscloud-io/moodle-mcp-server) | `main` | 🟡 GPL-3.0 | Vendor-maintained. GPL is survivable here: the agent talks to it over JSON-RPC, it is not linked. |
| **Moodle** | [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | `main` | 🔴 **UNGRANTED** | Course, announcement and assignment tools. No licence file **and** no `license` field in `pyproject.toml`. Do not ship. |
| **Canvas** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | 🟢 **The clean default.** Courses, assignments, submissions, grading, rubrics, students. |
| **Canvas** | [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) | `main` | 🟢 **MIT** | Fork of the above: adds office-hour appointment groups, announcement editing, syllabus read/write, student groups, course-content copy. |
| **Canvas** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main` | 🟢 **MIT** | Independent implementation — useful as a second opinion on tool shape. |
| **Canvas** | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | 🟡 **MANIFEST-ONLY MIT** — 🆕 `p387` **also published to npm as MIT**, a second independent grant publication | 🔴 🆕 `p387`: npm `canvas-mcp-server` **v2.2.3, last published 2025-06-27 — ~16 months stale**, while [r-huijts](https://github.com/r-huijts/canvas-mcp) published 2026-09-21. Its tool count is the largest on the Canvas shelf and its release is the oldest; prefer the maintained one unless you need those tools. Advertises 54 tools and Streamable HTTP. No licence **file**, but `package.json` declares `"license": "MIT"` — and its `files` array names a `LICENSE` that is absent from the tree. Usable; get the file committed. |
| **Open edX** | [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | `master` | 🔴 AGPL-3.0 | Matches the platform's own licence, which is the reason it can exist. |
| **Open edX** | [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master` | 🔴 AGPL-3.0 | The `tutor` plugin that installs it — the realistic deployment route. |
| **Google Classroom** | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | `main` | 🟢 **MIT** | Classroom is not an LMS a studio can fork, so MCP is the *only* integration surface. |
| **Brightspace / D2L** | [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | `main` | 🟡 **MANIFEST-ONLY MIT** — 🆕 `p387` the npm record declares `MIT` too, so the grant is published twice | 🔴 🆕 `p387`: npm `d2l-mcp-server` **v1.0.1, published 2025-11-28 and never again — ~11 months stale.** The only D2L server verified this pass. No licence file; `package.json` declares `"license": "MIT"`. **D2L remains thin — one server, and its grant is a manifest line.** |
| **Blackboard** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | `main` | 🟢 **MIT** *(1,063 B)* | 🔴 🆕 `p387`: **it has never shipped a release.** Its `package.json` claims the npm name `blackboard-learn-mcp`, which is **404 on the registry**; the unrelated npm package `bb-mcp` (v1.0.0, 2026-06-19) carries **no licence field and no repository field** and must not be attributed to it. So the one institution-grade claim on this shelf is **unexecuted (`Gap 386-B`) *and* unpublished** — build from it, do not install it. 🆕 `p386`. 🟢 **The only institution-grade LMS MCP server on this shelf.** Wraps the **official Blackboard Learn REST API**; README claims OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log, Prometheus `/metrics`, 40 tools incl. **grade write-back** and webhooks (self-claimed, read not executed). 🔴 Grade write-back is gated or prohibited in several jurisdictions — check [`policy-matrix`](../intel/policy-matrix.tsv) before enabling it. |
| **Blackboard** | [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) | `main` | 🟢 **MIT** *(1,067 B)* | 🆕 `p386`. Blackboard **Ultra**, student-side: signs in through the user's own university SSO/MFA in a real browser, **no API key**, read-only. Courses, deadlines, announcements, lecture-slide download. Same author ships Canvas and Moodle siblings. 🟡 A personal tool, not a tenant deployment. |
| **Blackboard** | [alanwtom/blackboard-mcp](https://github.com/alanwtom/blackboard-mcp) | `main` | 🟢 **MIT** *(1,065 B)* | 🆕 `p386`. Local-first, read-only, reads the signed-in student's own Ultra data through their normal browser session. Upstream of the fork below. |
| **Blackboard** | [lukecarroll15/blackboard-mcp](https://github.com/lukecarroll15/blackboard-mcp) | 🔴 **`tcd`** | 🟢 **MIT** *(1,065 B)* | 🆕 `p386`. 🔵 **Two lessons in one row.** The default ref is **`tcd`**, not `main` — a `main`-assuming read returns "no licence". And the payload is **byte-identical to upstream with the holder still `alanwtom`**, so the fork lineage is readable from the grant alone. |
| **Blackboard** | [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | `main` | 🟢 **MIT** *(1,084 B, © "blackboard-mcp contributors")* | 🆕 `p386`. Ultra: courses, content, files, grades, deadlines over the user's own browser session. Collective copyright holder rather than a named individual. |
| **Blackboard** | [Loganxgreaves/blackboard-mcp](https://github.com/Loganxgreaves/blackboard-mcp) | 🔴 **`master`** | 🟢 **MIT** *(1,070 B)* | 🆕 `p386`. Read-only, defaulted to one university (Sheffield Hallam) — re-point via config. Non-`main` default ref. |
| **Blackboard** | [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | `main` | 🔴 **UNGRANTED** | 🆕 `p386`. No licence file at **any of 9 probe paths** and **no licence field in any manifest**. Do not ship. |
| **Brightspace / D2L** | [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | `main` | 🟢 **MIT** *(1,070 B)* | 🆕 `p386`. 🟢 **The most substantial D2L server found.** Multi-strategy auth (TOTP, OAuth, browser), retry / circuit-breaker / cache tiers, and **opt-in write operations**. The closest available base for an institution-grade D2L server. |
| **Brightspace / D2L** | [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | `main` | 🟢 **MIT** *(1,068 B)* | 🆕 `p386`. 🔵 **Upstream of a fork family — count it once.** [`lmgveerhoek`](https://github.com/lmgveerhoek/brightspace-mcp-server) and [`matthewliu10`](https://github.com/matthewliu10/brightspace-mcp-server) publish **byte-identical** payloads still holding `© 2026 Rohan Muppa`; several more forks share the npm name. Grades, due dates, assignments, announcements, rosters, syllabus. Automated login is wired per school. |
| **Brightspace / D2L** | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | `main` | 🟢 **MIT** *(🔵 **1,200 B** — non-stock)* | 🆕 `p386`. The extra bytes are **attribution, not restriction**: an inline notice *"Portions of this software are derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License."* See **Pattern L step 11**. |
| **Brightspace / D2L** | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | `main` | 🟢 **MIT** *(🔵 **2,181 B** — **two stacked grants**)* | 🆕 `p386`. The payload is **two complete MIT licences**: its own (© 2026 Robert McCrary) **plus** *"Portions of this project are derived from d2l-cli: Copyright (c) 2026 Aaryan Kapoor."* 🟡 Shipping it means carrying **both** notices. Go, read-only, pre-1.0. |
| **Anki** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | `main` | 🟢 **MIT** | Not an LMS — the spaced-repetition loop, which pairs with FSRS above. |

### 🆕 `p387` — Dated: which of these servers actually ships a release

Stars are unreadable here and always were a poor proxy. **A publish date is the signal a studio can
act on**: it dates the artefact the client would install. Method and every raw row:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

| server | package | latest | last published | read it as |
|---|---|---|---|---|
| [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | npm `brightspace-mcp-server` | **5.0.8** | **2026-10-22** (today) | 🟢 the most actively published LMS MCP server on this shelf — and a **v5** line, not a weekend project |
| [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | npm `brightspace-d2l-mcp` | 1.4.3 | 2026-10-21 | 🟢 active |
| [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | npm `brightspace-mcp` | 1.3.1 | 2026-09-28 | 🟢 active — corroborates `p386`'s pick as the most substantial D2L base |
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | npm `@r-huijts/canvas-mcp` | 1.5.1 | 2026-09-21 | 🟢 active — the Canvas default, now dated |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | npm `@ankimcp/anki-mcp-server` | 0.27.0 | 2026-10-04 | 🟢 active |
| [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | npm `blackboard-mcp` | 0.1.2 | 2026-09-10 | 🟡 one release, pre-1.0 — **and it is the only publication in its fork family** |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | npm `d2l-mcp-server` | 1.0.1 | 2025-11-28 | 🔴 ~11 months stale |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | npm `canvas-mcp-server` | 2.2.3 | 2025-06-27 | 🔴 ~16 months stale |
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | npm `blackboard-learn-mcp` | — | **never** | 🔴 no published release (see its row above) |
| [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) · [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | PyPI `blackboard-mcp` · npm `canvas-mcp-code-api` | — | **never** | 🟡 clone-and-run tools, not installable packages — fine, but say so to a client |

🔵 **The fork families collapse mechanically, and now there is a second way to see it.** `p386`
collapsed them by **licence bytes** (byte-identical payloads, upstream's copyright holder). The
registry collapses them by **publication**: four Blackboard addresses
([alanwtom](https://github.com/alanwtom/blackboard-mcp),
[lukecarroll15](https://github.com/lukecarroll15/blackboard-mcp),
[Loganxgreaves](https://github.com/Loganxgreaves/blackboard-mcp),
[felipedias-ie](https://github.com/felipedias-ie/blackboard-mcp)) all declare the package name
`blackboard-mcp`, and **exactly one publication exists** — its `repository` field points at
`felipedias-ie`. Same for [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp), whose fork
kept upstream's scoped name `@r-huijts/canvas-mcp`. **Four addresses, one artefact.** Two
independent instruments, same answer: count the project, not the slug.

🔴 **And this pass's own instrument error, published rather than tidied.**
[faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server)
declares the package name **`class`** — and npm's `class` is an unrelated **2013** package by
`deadlyicon` (MIT, v0.1.4). A registry lookup keyed on the manifest name alone would have printed
*"MIT, published 2013-08-15"* onto this shelf for a Google Classroom server. **A manifest name is
not a publication.** The gate is now `Pattern L` **step 14**: accept a registry row only when its
`repository` field — or its description links — point back at the same slug.

### 🔵 Supply census: how crowded each platform already is

Counts carried from this base's own cumulative harvest across `agents/top.md` and
[`agents/trending.md`](trending.md) (distinct slugs, not all individually re-verified this pass —
the twelve rows above are the verified subset):

| platform | distinct MCP server slugs harvested |
|---|---|
| Canvas | 35 |
| Moodle | 20 |
| Google Classroom / Workspace for Education | 12 |
| Blackboard | 9 |
| Brightspace / D2L | 6 |
| Open edX | 2 |
| Anki | 1 |

🆕 `p386` — **and the two rows that were only counts are now measured.** Of the nine Blackboard
slugs harvested, nine were probed first-hand this pass: **6 MIT, 1 ungranted, 2 dead**. Of the six
D2L slugs, **6 MIT** — three of them one upstream and two byte-identical forks. The census column
above counts *addresses*; it never counted *grants*, and for four passes the difference read as an
absence of supply.

🔵 **Read the shape, not the totals.** Canvas and Moodle are saturated with near-duplicate
community servers, of which a minority carry a usable licence — so the work there is **selection**,
not building. Open edX has two, both AGPL and both from one vendor.

## The Blackboard and D2L supply, measured

🆕 `p386`. Until this pass this shelf said **"Blackboard has nine servers and not one verified grant;
D2L has six and the only one checked is ungranted"**, and concluded that both were places where
*"a permissively-licensed server would be a genuine contribution."* 🔴 **That conclusion was wrong,
and it was wrong because nobody had read the grants — not because the grants were absent.**

| platform | probed this pass | 🟢 MIT, payload read | 🔴 ungranted | 🔴 address dead |
|---|---|---|---|---|
| **Blackboard** | 9 | **6** | 1 (`anastasasenov/bbmcps`) | 2 (`e9x/blackboard-mcp`, `parkseokjune/unist-blackboard-mcp`) |
| **Brightspace / D2L** | 6 | **6** | 0 | 0 |

🔵 **The gap moved, it did not close — and the new shape is the actionable part.** Eleven of the
twelve granted servers authenticate as **the signed-in student**: the user's own browser SSO/MFA
session or session cookies, no admin API key, read-only by design and by necessity. Those are
**personal tools**, and a studio cannot deliver one to an institution — it has no tenant identity,
no role boundary, no audit trail, and it breaks whenever the vendor changes a login page.

🟢 **Exactly one reads as institution-grade: [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp)
(MIT, 1,063 B).** It wraps the **official Blackboard Learn REST API** and its README's architecture
block claims OAuth2, a role gate, FERPA handling, rate limiting, PII scrubbing, a structured JSON
audit log, Prometheus `/metrics`, and 40 tools including **grade write-back** and webhook
subscriptions. 🟡 **Those are maintainer self-claims — read, not executed, this pass**; and the
grade-write-back surface is precisely what [`intel/policy-matrix.tsv`](../intel/policy-matrix.tsv)
gates or prohibits by jurisdiction, so the licence clearing it is the *first* gate, not the last.

🔵 **So the restated recommendation:** on Blackboard and D2L the work is **selection plus hardening**
— take a granted server and add tenant auth, role scoping and an audit trail — not greenfield
building. The genuine remaining contribution is **an institution-grade D2L server**: all six granted
Brightspace servers are student-side, and `JhostinAleck/brightspace-mcp` (opt-in writes,
TOTP/OAuth/browser auth strategies) is the closest thing to a base for one.

## 🟡 Two licence traps that a badge-read would miss

🆕 `p389` — **and a third kind: the trap is not in the repository at all, it is in the write-up.**

- [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — a 2026 third-party review of this
  project states it is "**AGPL-3.0**, with commercial licensing available by contact." **It is not.**
  Read first-hand at the real default ref (`main` @ `269fde2d991f`, 2026-10-22): `LICENSE` is **1,066 B
  of stock MIT text**, "MIT License / Copyright (c) 2026 THU-MAIC", and the root `package.json`
  independently declares `"license": "MIT"`. Two sources inside the payload agree; the review is
  simply wrong. 🔵 **Why this one matters more than a badge mismatch.** A badge mismatch is caught by
  the probe on this page. A *licence claim in a review* is caught by nothing — it is read by a studio
  lead doing exactly the sort of search that produced this pass, and "AGPL + commercial licence"
  reads as *do not propose this to a client*. The largest education-native repository in the supply
  was one secondary source away from being ruled out of every engagement. 🟢 **Procurement rule:
  never let a third-party write-up decide a licence. `Pattern L` is the gate, and it reads the
  payload.**


- [microsoft/autogen](https://github.com/microsoft/autogen) — root `LICENSE` is **CC-BY-4.0**
  (18,649 B, "Attribution 4.0 International"). The **code** grant is a *different file*,
  `LICENSE-CODE` = **MIT**. A tool that reads one file and reports "CC-BY" is wrong about the code,
  and a tool that reports "MIT" is wrong about the docs.
- [open-webui/open-webui](https://github.com/open-webui/open-webui) — `LICENSE` is **2,819 B**
  against stock BSD-3's ~1,500 B. It is BSD-3 text **plus a branding restriction and a Contributor
  License Agreement**, self-titled "Open WebUI License". Not an OSI-standard BSD grant. Prefer
  [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**, 1,065 B) as a campus
  LLM gateway where the licence has to be clean.

## 🆕 `p387` — The institution-grade Brightspace tooling exists, and it is not an MCP server

`Gap 386-A` is *"no institution-grade D2L MCP server exists"*, and that still holds. But the
adjacent question a studio actually asks — *has anyone automated Brightspace against the official
API at institutional scale?* — has an answer this base did not hold:

| tool | channel it was found and read on | licence | what it is |
|---|---|---|---|
| **`bscli`** — Brightspace Command Line Interface | **PyPI** `bscli` (`pypi.org/pypi/bscli/json`) — v**0.3.13**, published **2026-09-04** | 🟢 **MIT** — the *full payload* is carried in the PyPI `info.license` field, © 2024 Ciske Harsema, read first-hand | Grading **operations** at university scale: bulk-download submissions, process them, **distribute them to graders**, collect grades and **upload them back to Brightspace**. Author e-mails are `@ru.nl` — **Radboud University**, EMEA — and the README states it is designed for educational institutions and adaptable to any Brightspace instance. |
| **`d2l-cli`** | **PyPI** `d2l-cli` v0.3.0, published **2026-09-24**, `Homepage` → [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli); grant then read at `main/LICENSE` (MIT, 1,070 B, © 2026 Aaryan Kapoor) | 🟢 **MIT** | *"Read-only CLI client for D2L Brightspace student APIs, built for AI agents."* 🟢 **This closes `Gap 386-E`:** it is the address named in [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP)'s stacked grant, so anyone shipping that server now knows exactly what they are carrying attribution for. |

🔵 **Why these were invisible for four passes, stated as a method lesson.** Both were found by
**package-registry name**, not by a repository search. `bscli`'s own home,
`bscli.science.ru.nl`, is **DNS-unreachable** from this sandbox and no git address for it was
resolvable — so the *grant* is read, the *code* is installable, and the **source address remains
unresolved** (`Gap 387-B`). For `d2l-cli` the registry handed over the address that a repository
search for the string in a licence notice could not: `p386` was right not to guess a slug, and the
registry is where the slug actually lives.

## 🆕 `p389` — Dated: every address on these shelves, in days since last commit

The instrument is the blobless shallow clone described above. **60 addresses, 58 live, 2 dead**, each
dated at its **real default ref** on 2026-10-22. Full table:
[`verified-repos`](../evidence/verified-repos.2026-10-22-p389.tsv). What the dates change:

### 🔴 Stale — and four of them carry a recommendation on these shelves

| address | real ref | days since last commit | licence (payload) | what the date changes |
|---|---|---|---|---|
| [apache/ofbiz](https://github.com/apache/ofbiz) | `trunk` | 🔴 **3,539** *(2017-02-12)* | Apache-2.0 | **A lookalike at the obvious address.** This is the retired monolith. The ERP base recommended on [`verticals/solutions.md`](../verticals/solutions.md) is [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) — **dated 0 days, committed today**. 🟢 The shelf had the right address; a client's engineer typing the obvious one lands on a nine-year-dead tree. Name the `-framework` suffix in the proposal. |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main` | 🔴 **343** *(2025-11-13)* | 🟡 GPL-3.0 | Demoted in *Tier 1* above: a reference for learner-state modelling, not a dependency. |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | `main` | 🔴 **242** *(2026-02-22)* | 🟢 MIT | The Moodle MCP supply is **thinner than its address count** — see the *Supply census*. MIT and 8 months idle is a **vendoring candidate**, not an integration to depend on. |
| [allenai/olmocr](https://github.com/allenai/olmocr) | `main` | 🔴 **211** *(2026-03-25)* | 🟢 Apache-2.0 | 🆕 Not previously on these shelves and **not added as a dependency** because of this date. For parsing scanned course material prefer [docling-project/docling](https://github.com/docling-project/docling) (**MIT, 0 days**) — see [`repos/foundations.md`](../repos/foundations.md). |
| [pdg6/bc-curriculum-mcp-server](https://github.com/pdg6/bc-curriculum-mcp-server) | `main` | 🔴 **209** *(2026-03-27)* | 🟢 MIT | Confirms `p388`'s own caveat quantitatively: the risk is **currency**, not licence. A curriculum crawl 7 months old is a crawl to re-run, and the MIT grant means you may. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | 🔴 **144** *(2026-05-31)* | 🔴 **NO LICENCE FILE** | Both failure modes at once. It is cited in round-ups as "another open-source option" for Canvas; it is **ungranted and idle**. Not a Canvas option. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | `master` | 🔴 **175** *(2026-04-30)* | 🔴 AGPL-3.0 | 🔵 **The one that should change how the Canvas shelf is pitched.** Eleven Canvas integrations are catalogued on this page, and **the platform's own default ref has not moved in ~6 months** while its `stable/*` branches have. Nothing is wrong with Canvas — this is how Instructure ships — but *anyone cloning `master` to reason about the API surface is reading an April tree*. State the ref you integrated against. |

### 🟢 Live — dated, so the claim is now checkable rather than asserted

**Committed on 2026-10-22, the day of this pass:** [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
(MIT) · [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) (MIT) ·
[withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) (ODbL-1.0) ·
[apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) · [aureuserp/aureuserp](https://github.com/aureuserp/aureuserp) (MIT) ·
[learningequality/kolibri](https://github.com/learningequality/kolibri) (MIT) · [oppia/oppia](https://github.com/oppia/oppia) (Apache-2.0) ·
[OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0) · [docling-project/docling](https://github.com/docling-project/docling) (MIT) ·
[chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) · [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) ·
[openedx/edx-platform](https://github.com/openedx/edx-platform) · [opencast/opencast](https://github.com/opencast/opencast) ·
[frappe/erpnext](https://github.com/frappe/erpnext) · [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) ·
[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI).

**Within a week:** `HKUDS/DeepTutor` (3 d) · `chrischall/infinitecampus-mcp` (3 d) ·
`learningequality/ricecooker` (3 d) · `CAHLR/OATutor` (1 d) · `CAHLR/pyBKT` (1 d) ·
`vishalsachdev/canvas-mcp` (1 d) · `academico-sis/academico` (1 d) · `moodle/moodle` (1 d) ·
`jupyter/nbgrader` (1 d) · `krayin/laravel-crm` (1 d) · `langchain-ai/langgraph` (1 d) ·
`chroma-core/chroma` (1 d) · `ankitects/anki` (1 d) · `Mattlo0546/canvas-mcp` (2 d) ·
`mem0ai/mem0` (2 d) · `h5p/h5p-php-library` (2 d) · `overhangio/tutor` (2 d) ·
`francoisjacquet/rosariosis` (5 d) · `jupyterlite/jupyterlite` (6 d) · `microsoft/autogen` (6 d).

### 🔴 Two addresses that do not resolve

| address | correction |
|---|---|
| `openedx/tutor` | The Open edX deployment tool is **[overhangio/tutor](https://github.com/overhangio/tutor)** (AGPL-3.0, `release`, 2 d). The `openedx/` org does not carry it. |
| `edx/openedx-app-android` | The `edx/` org is not where the mobile apps live; the Open edX work is under `openedx/`. No mobile client is recommended on these shelves on the strength of a guessed address. |

🟡 **One limit of the instrument, stated.** A date tells you **someone pushed**, not that the project
is healthy, nor that the push was to the branch a release is cut from — `instructure/canvas-lms` is
the whole argument for that caveat. And the reverse: a repository that is *finished* (a
specification, a dataset) is not unhealthy for being quiet. Read the date against what the thing is.

## Verification method

`curl -sI https://github.com/...` returns **403** through this sandbox's agent proxy, and
`api.github.com` returns **403** with an `add_repo` message, so the method prescribed in the run
brief was unavailable. Two stronger channels were used instead and are reproducible:

1. `git ls-remote --symref https://github.com/<slug> HEAD` — proves the address resolves **and**
   returns the **real default ref**. A renamed, deleted or private repository fails here; a HEAD
   request against GitHub's HTML would not have distinguished those.
2. `raw.githubusercontent.com/<slug>/<real-ref>/<path>` — the licence **text**, read first-hand and
   recorded with its byte length, so a hand-edited or non-stock grant shows up as a length anomaly.
3. 🆕 `p389` — **`git clone --depth 1 --filter=blob:none --no-checkout`**, which subsumes both of the
   above and adds the signal they could not reach. One ~1.2 s call yields the real default ref, the
   **HEAD SHA**, the **last commit date**, the **whole root tree** (so "is there a `LICENSE` at all"
   is answered by listing, not by guessing eight paths), and any blob on demand via
   `git show HEAD:<path>` — the grant *and* the manifest that should agree with it. 🟢 It also fixes
   `p384`'s "resolves but has no tree" failure mode by construction: a clone that produces no `HEAD`
   is reported `EMPTY`, distinct from `DEAD`. 🔴 It does **not** give stars, forks, watchers, release
   metadata or an enumeration of the supply — `api.github.com/search/*` stays **403**, so *discovery*
   is still web-search and package registries, and only *verification* is first-hand.

🔵 **`p384` extended the probe set from seven paths to eight.**
[OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) carries a standard GPL-2.0 grant
at **`docs/License.txt`** — absent from all seven root paths, so the old read would have returned
"ungranted" for the most widely deployed open-source SIS in K-12. The probe now also checks
**`docs/License.txt`** and **`doc/LICENSE`** before any ungranted verdict is recorded. 🟡 **No
`p383` verdict is overturned:** the two repositories ruled UNGRANTED
([loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp),
[Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend)) were
re-probed at the new paths this pass and remain ungranted.

🔵 **And a second failure mode `p384` found: an address that resolves with no tree behind it.**
[projectfedena/fedena](https://github.com/projectfedena/fedena) returns refs from
`git ls-remote --heads` but 404s on every content path probed. **`ls-remote` proves a ref, not a
payload** — which is why channel 1 is never sufficient on its own, and why a census built on
resolution alone over-counts the supply.

### Grant read at — provenance for every agent-tier address

The exact ref-and-path each grant above was read from, so any reader can repeat the read.
`<ref>/<path>` resolves as `raw.githubusercontent.com/<slug>/<ref>/<path>`.

| repo | grant read at | licence |
|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main/LICENSE` | Apache-2.0 |
| [AI-Shifu/ai-shifu](https://github.com/AI-Shifu/ai-shifu) | `main/LICENSE.txt` | Apache-2.0 |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `main/LICENSE` | MIT |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main/LICENSE` | MIT |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main/LICENSE` | BSD-3-Clause |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main/LICENSE` | GPL-3.0 |
| [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | `main/LICENSE` | AGPL-3.0 |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | `dev/LICENSE` | AGPL-3.0 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | `main/LICENSE` | Apache-2.0 |
| [AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) | `main/LICENSE` | Apache-2.0 |
| [allenai/ai2-scholarqa-lib](https://github.com/allenai/ai2-scholarqa-lib) | `main/LICENSE` | Apache-2.0 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | `main/LICENSE` | Apache-2.0 |
| [jupyterlab/jupyter-ai](https://github.com/jupyterlab/jupyter-ai) | `main/LICENSE` | BSD-3-Clause |
| [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main/LICENSE` | MIT |
| [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | `main/LICENSE` | MIT — 1,069 B, © 2026 Grupo Sirius *(`p387`)* |
| [GuilhermeScarpini/agente-bncc-professores](https://github.com/GuilhermeScarpini/agente-bncc-professores) | `main/LICENSE` | MIT — 1,074 B *(`p387`)* |
| [thiagoudweb/techTutor](https://github.com/thiagoudweb/techTutor) | `main/LICENSE` | MIT — 1,069 B, © 2026 Thiago Silva *(`p387`)* |
| [Aaryan-Kapoor/d2l-cli](https://github.com/Aaryan-Kapoor/d2l-cli) | `main/LICENSE` | MIT — 1,070 B, © 2026 Aaryan Kapoor *(`p387`)* |
| `bscli` *(no git address resolved)* | PyPI `info.license` payload | MIT — © 2024 Ciske Harsema *(`p387`)* |
| [netless-io/flat](https://github.com/netless-io/flat) | `main/LICENSE` | MIT |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | `main/LICENSE` | MIT |
| [tutors-sdk/tutors](https://github.com/tutors-sdk/tutors) | `development/LICENSE` | MIT |
| [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main/LICENSE` | MIT |
| [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) | `main/LICENSE` | MIT |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main/LICENSE` | MIT |
| [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | `master/LICENSE` | AGPL-3.0 |
| [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master/LICENSE` | AGPL-3.0 |
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | `main/LICENSE` | MIT |
| [lmscloud-io/moodle-mcp-server](https://github.com/lmscloud-io/moodle-mcp-server) | `main/LICENSE` | GPL-3.0 |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | `main/LICENSE` | MIT |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | `main/LICENSE` | MIT |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | `main/LICENSE` | Apache-2.0 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | `main/LICENSE-CODE` | MIT (code); `main/LICENSE` is CC-BY-4.0 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | `main/LICENSE` | not stock BSD-3 — branding clause + CLA |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | — none at 7 paths; no `license` in `pyproject.toml` | UNGRANTED |
| [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | — none at 7 paths; no manifest | UNGRANTED |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main/package.json` (`"license": "MIT"`) | MIT, manifest-only — file absent |
| [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | `main/package.json` (`"license": "MIT"`) | MIT, manifest-only — file absent |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | `main/version.php` (GPL header) | GPL-3.0-or-later, header-granted |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | `main/LICENSE` | MIT *(`p384`)* |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | `main/LICENSE` | MIT *(`p384`)* |
| [inducer/relate](https://github.com/inducer/relate) | `main/LICENSE` | MIT *(`p384`)* |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | `main/LICENSE` | **ODbL** — share-alike database licence, no code grant *(`p384`)* |
| [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | `master/docs/License.txt` | GPL-2.0 — 🔵 **8th probe path**, absent from all seven root paths *(`p384`)* |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | — `master` resolves; `README`/`README.md`/`LICENSE`/`Gemfile`/`app` all 404 | **nothing read** — no tree to licence *(`p384`)* |
| [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | `main/LICENSE` **and** `v0.1.0/LICENSE` | 🔴 **AGPL-3.0** at `main` (34,523 B stock) · 🟢 **MIT** at tag `v0.1.0` (1,081 B, *"Copyright (c) 2026 Learn Shell contributors"*) — 🔵 **one repository, two refs, two grants**, both read first-hand; relicensed 2026-08-16 *(`p385`)* |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main/LICENSE` | MIT — 1,068 B, © 2026 Zijin Zhang *(`p386`)* |
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | `main/LICENSE` | MIT — 1,063 B *(`p386`)* |
| [Mattlo0546/blackboard-mcp](https://github.com/Mattlo0546/blackboard-mcp) | `main/LICENSE` | MIT — 1,067 B *(`p386`)* |
| [alanwtom/blackboard-mcp](https://github.com/alanwtom/blackboard-mcp) | `main/LICENSE` | MIT — 1,065 B *(`p386`)* |
| [lukecarroll15/blackboard-mcp](https://github.com/lukecarroll15/blackboard-mcp) | 🔴 **`tcd`**`/LICENSE` | MIT — 1,065 B, holder still `alanwtom` *(`p386`)* |
| [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | `main/LICENSE` | MIT — 1,084 B, © "blackboard-mcp contributors" *(`p386`)* |
| [Loganxgreaves/blackboard-mcp](https://github.com/Loganxgreaves/blackboard-mcp) | 🔴 **`master`**`/LICENSE` | MIT — 1,070 B *(`p386`)* |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) | — none at 9 paths; no manifest licence field | UNGRANTED *(`p386`)* |
| [JhostinAleck/brightspace-mcp](https://github.com/JhostinAleck/brightspace-mcp) | `main/LICENSE` | MIT — 1,070 B *(`p386`)* |
| [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | `main/LICENSE` | MIT — 1,068 B; `lmgveerhoek` and `matthewliu10` byte-identical *(`p386`)* |
| [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | `main/LICENSE` | MIT — 1,200 B, inline derivation notice *(`p386`)* |
| [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | `main/LICENSE` | MIT — 2,181 B, **two stacked MIT grants** (own + `d2l-cli`) *(`p386`)* |
| [Nutlope/llamatutor](https://github.com/Nutlope/llamatutor) | — none at 9 paths; no manifest licence field | UNGRANTED *(`p386`)* |
| [jarodise/Language-Transfer](https://github.com/jarodise/Language-Transfer) | — none at 9 paths; no manifest licence field | UNGRANTED *(`p386`)* |
| [e9x/blackboard-mcp](https://github.com/e9x/blackboard-mcp) · [parkseokjune/unist-blackboard-mcp](https://github.com/parkseokjune/unist-blackboard-mcp) | — `ls-remote` returns nothing | **DEAD / private** — both listed by search results as live MIT servers *(`p386`)* |
**13 of the 58 live addresses are not on `main`** (`master`, `develop`, `dev`, `release`,
`development`, `release_11`, `19.0`) — 🆕 `p386` adds **four more refs** to that list from 22 new
probes: **`tcd`** (`lukecarroll15/blackboard-mcp`), **`master`** (`Loganxgreaves/blackboard-mcp`,
`aureuserp/aureuserp`), **`2.2`** (`krayin/laravel-crm`, a version branch with no `main`) and
**`trunk`** (`apache/ofbiz-framework`). Resolving the ref **before** reading the licence is not
optional; a `main`-assuming read returns "no licence" for every one of them.
