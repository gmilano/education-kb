---
industry: education
region: Global
updated: 2026-11-18
---

# Top AI agents — education

Every repo below was verified on 2026-11-18 on two independent channels:

1. **Existence + licence text** — fetched the actual `LICENSE`/`COPYING` file from
   `raw.githubusercontent.com` and read the grant. A `200` proves the repo exists; the text
   tells us the licence verbatim rather than from a badge.
2. **Stars, SPDX licence, last push** — `gh api search/repositories` with batched `repo:`
   qualifiers.

Where the two disagree, both are shown. `github.com` HTML returns `403` through this
environment's proxy and `api.github.com/repos/` is session-scoped, so these are the two
routes that work. Stars are as at 2026-11-18, **remeasured in pass p890** (DeepTutor
60,165 → 60,186; OpenMAIC 43,856 → 43,859; BloomTutor 313 → 315; whiteboard-ai-tutor
222 → 223; every other row unchanged).

**Cadence note.** The largest intra-day move across ~30 tracked repos was +21 stars on a
60,000-star repo. Star counts are a **daily** metric; remeasuring hourly buys nothing and the
call budget belongs in regional research instead.

## Education-specific agents

Built for teaching, tutoring or assessment — not general frameworks pointed at a classroom.
Sorted by stars.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 60,186 | 2026-11-15 | Agentic personalised tutoring grounded in the student's own material, with persistent learning history. Hit #1 on GitHub trending 28 Oct 2026; first released Dec 2025. Paper: arXiv 2604.26962. **The single largest open education agent in existence.** | APAC — HKU Data Intelligence Lab |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | 43,859 | 2026-11-18 | Multi-agent AI classroom: agents generate slides, quizzes and project-based activities and grade quiz answers. `v1.4.2` (2026-11-09) added course-level undo for manual edits and agent runs. Relicensed to MIT at `v0.3.0`, Jun 2026. | APAC — Tsinghua University |
| **canvas-mcp** (Sachdev) | https://github.com/vishalsachdev/canvas-mcp | MIT | 334 | 2026-11-18 | MCP server exposing Canvas LMS — courses, assignments, submissions — as agent tools. | North America — USA |
| **BloomTutor** | https://github.com/Li-Evan/BloomTutor | MIT | 315 | 2026-11-17 | Tutor that structures interaction around Bloom's taxonomy levels. | APAC |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | 282 | 2026-11-17 | Intelligent tutoring system with open problem banks and tutoring-effect instrumentation; built for A/B-testable learning research. | North America — UC Berkeley |
| **molly554/whiteboard-ai-tutor** | https://github.com/molly554/whiteboard-ai-tutor | MIT | 223 | 2026-11-17 | Whiteboard tutor with animated lessons and interactive playback. Created after Aug 2026 — one of the fastest-growing new entrants. | Global |
| **OpenPronounce** | https://github.com/OpenPronounce/OpenPronounce | MIT | 221 | 2026-11-09 | Open pronunciation assessment — the language-learning niche where open source is genuinely competitive with commercial APIs. | Global |
| **OpenTutor** | https://github.com/zijinz456/OpenTutor | MIT | 181 | 2026-11-17 | Open tutoring agent. | APAC |
| **canvas-mcp** (Cheng) | https://github.com/boyuchengz/canvas-mcp | MIT | 118 | 2026-10-27 | **Read-only** MCP server connecting Claude/ChatGPT to Canvas LMS. A second, independent `canvas-mcp` — read-only by design, which is the safer default for a student-data pilot. | North America |
| **Open TutorAI (CE)** | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 118 | 2026-06-26 | Community edition of a self-hostable tutor platform. Licence text carries an "All rights reserved" header over a BSD-style grant; SPDX confirms BSD-3-Clause. | EMEA |
| **TeachMeCoding** | https://github.com/liangxiao777/TeachMeCoding | Apache-2.0 | 73 | 2026-10-30 | Local-first AI coding tutor: personalised roadmaps, lessons, hands-on practice with execution. | APAC |
| **aula** | https://github.com/luumlabs/aula | AGPL-3.0 | 66 | 2026-11-17 | Turns notes, slides and past exams into lessons. **AGPL — not usable in a closed derivative.** | Global |
| **wenflow** | https://github.com/wenflow-org/wenflow | MIT | 72 | 2026-11-12 | Writing-feedback workflow agent. | APAC |
| **wiki-rag** | https://github.com/moodlehq/wiki-rag | BSD-3-Clause | 54 | 2026-06-15 | **Moodle HQ's own** RAG service over Moodle documentation. Low stars, high significance: the Moodle organisation shipping a first-party retrieval agent. | EMEA — Moodle HQ |
| **ECNU EduWork** | https://github.com/ECNU/EduWork | MulanPSL-2.0 | 378 | 2026-11-18 | Education workflow agent. **Licence note:** Mulan Permissive Software License v2 is OSI-approved and permissive, but it is not MIT/Apache — check your client's approved-licence list. | APAC — ECNU, China |
| **socratic-workshop** | https://github.com/smashburger-dev/socratic-workshop | MIT | 24 | 2026-10-28 | Socratic tutoring delivered **as a skill inside a coding agent** (Claude Code / Codex): learn a topic by explaining it. | Global |
| **ls1intum/edutelligence** | https://github.com/ls1intum/edutelligence | MIT | 17 | 2026-11-17 | Umbrella suite of AI services for the Artemis learning platform. **The production-grade reference for "AI integrated into a real LMS"** — star count badly understates it. | EMEA — TU Munich |
| **pedagogy-benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | MIT | 13 | 2026-11-16 | Benchmark for the *pedagogical* ability of LLMs, as distinct from subject knowledge. An eval gate, not an agent. | Global |
| **Pyris** | https://github.com/ls1intum/Pyris | MIT | 12 | 2026-06-03 | LLM microservice behind Artemis's *Iris* tutor. Clean separation of the LLM tier from the LMS — the pattern to copy when the model layer must stay swappable. | EMEA — TU Munich |
| **ankipa** | https://github.com/warleysr/ankipa | MIT | 10 | 2026-11-07 | Pronunciation assessment as an Anki add-on; the "agent inside an existing study tool" pattern. **The only LATAM-origin education agent verified in this pass.** | LATAM — Brazil |
| **EDU AI Agent Suite** | https://github.com/virtualryder/edu-ai-agents | MIT (SPDX: NOASSERTION; licence text reads MIT) | 4 | 2026-10-10 | Eight reference agent workflows with deny-by-default authorisation, student-PII masking, human-in-the-loop enforcement and tamper-evident audit, aligned to FERPA, COPPA, IDEA/504 and ADA Title II. **Grading uses a deterministic rubric service, not an LLM** — which is what makes it legally usable in several US states. Targets Amazon Bedrock. Tiny and new; valuable as an architecture, not as a dependency. | North America |
| **ai-tutor-agent** | https://github.com/vulinh1704/ai-tutor-agent | MIT | 0 | 2026-11-16 | FastAPI + LangGraph tutoring starter: Socratic hints, rubric grading, session memory, offline demo mode; checks every draft for answer leaks. Zero stars — a skeleton to read, not a dependency. | APAC — Vietnam |

**22 education-specific agents, every URL and licence verified.**

**How to read the star column.** The distribution is extremely bimodal: two repos above 40k,
then a cliff to the low hundreds. Stars here measure consumer discovery, not institutional
fitness — `edutelligence` (17 ★) and `Pyris` (12 ★) run in production at TU Munich, while
several repos above them are weekend projects. Treat stars as evidence of momentum and the
origin column as evidence of durability.

## Adjacent: Open edX first-party AI

| Repo | Licence | ★ | Last push | Notes |
|---|---|---|---|---|
| https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | 2026-11 | **First-party Open edX AI extension point.** Newly surfaced this pass. AGPL, like the platform — fine for hosting, a problem for a closed derivative. |
| https://github.com/openedx/edx-ora2 | AGPL-3.0 | 64 | 2026-11-13 | Open-response assessment (peer/self/staff grading). The natural seam for an AI grading assist. |

## General-purpose agents worth composing into education work

Not education products, but what an engagement will actually reach for.

| Agent / framework | Repo | Licence | ★ | Why it matters here |
|---|---|---|---|---|
| **CrewAI** | https://github.com/crewAIInc/crewAI | MIT | 61,058 | Role-based multi-agent orchestration — maps cleanly onto instructor / tutor / grader / reviewer splits. |
| **LangGraph** | https://github.com/langchain-ai/langgraph | MIT | 45,093 | Graph-structured orchestration. The right primitive when a tutoring policy must be auditable: policy checks become explicit nodes. |
| **AI Engineering Hub** | https://github.com/patchy631/ai-engineering-hub | MIT | 41,974 | Not an agent: a large collection of worked agent projects. Useful as staff-upskilling material. |
| **STORM** | https://github.com/stanford-oval/storm | MIT | 31,906 | Generates cited, structured long-form articles. Repurposes well for courseware drafting. **Last push 2025-09-30 — effectively dormant;** pin a version. |
| **GPT Researcher** | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | 30,768 | Autonomous research agent with citation discipline — literature-review scaffolds in higher ed. |
| **OpenHands** | https://github.com/All-Hands-AI/OpenHands | MIT | *(unavailable — see note)* | Coding agent; the practical choice for automating LMS plugin and migration work. Canonical slug is `All-Hands-AI/OpenHands`; `OpenHands/OpenHands` is **not** the repo. Org also ships https://github.com/OpenHands/software-agent-sdk (MIT, 1,406 ★). |
| **LibreChat** | https://github.com/danny-avila/LibreChat | MIT | *(unavailable — see note)* | Multi-model chat front end with auth and per-user quotas; fastest route to a governed institutional chat tier. Canonical slug is `danny-avila/LibreChat`. |

**Teaching assets, measured for the first time in p890.** Not agents and not education
products, but the two largest permissively licensed *curricula* relevant to this KB, and both
usable as client-enablement or staff-upskilling courseware that can be rebranded and extended:
https://github.com/microsoft/ai-agents-for-beginners (MIT, **80,197 ★**, pushed 2026-11-17 —
larger than any education agent that exists) and https://github.com/huggingface/agents-course
(Apache-2.0, **35,115 ★**, pushed 2026-11-17).

**Note on three unavailable star counts.** `All-Hands-AI/OpenHands`, `danny-avila/LibreChat`
and `openedx/edx-platform` are consistently absent from `search/repositories` results in this
session across repeated query shapes, while their `LICENSE` files return `200` on
`raw.githubusercontent.com`. Existence and licence are confirmed; the star figure is simply
not retrievable here. Recorded as unavailable rather than filled from a blog.

## Emerging pattern worth naming: the tutor as an agent *skill*

A distinct cohort of repos created since August 2026 delivers tutoring not as a web app but as
a **skill or MCP server inside an existing coding agent** — `smashburger-dev/socratic-workshop`
(MIT, 24 ★), `Aisland-SJL/Aisland-teach` (MIT, 18 ★), `boyuchengz/canvas-mcp` (MIT, 118 ★),
`BaronCyrus/dsh-aha-tutor` (MIT, 46 ★), `bayshores/godspeed` (AGPL-3.0, 22 ★). All are small,
but the direction is consistent and it shortens time-to-pilot dramatically: no front end to
build, and the learner already has the client installed. Tracked in `agents/trending.md`.

## What we searched for and did not find

Recording gaps because an unrecorded gap looks exactly like coverage.

- **No open-source agent for student information systems or registrarial workflow.** Tutoring,
  grading and content generation are crowded; enrolment, timetabling, transcripts and financial
  aid have none. The clearest build-vs-adopt gap in the industry and the most defensible studio IP.
- **No dominant open agent for special education or accessibility accommodation**, despite
  `virtualryder/edu-ai-agents` naming IDEA/504 and ADA Title II as design goals.
- **Almost nothing from LATAM.** `warleysr/ankipa` (10 ★, Brazil) is the only LATAM-origin
  education agent verified. LATAM edtech searches returned companies (Teachy, Vetto, Ginia),
  not repos. For a LATAM engagement, expect to localise an APAC- or EMEA-origin agent.
- **Nothing from Africa or the Middle East**, which this KB's closed region vocabulary files
  under EMEA — so "EMEA" coverage here is in practice European coverage.
- **No confirmed November 2026 *launch*.** The newest dated release artefact is OpenMAIC
  `v1.4.2` (2026-11-09). Re-checked in pass p890 across four global and four regional search
  legs: unchanged.
- **The "tutor as an agent skill" cohort has no traction.** The previous pass set a watch
  threshold of 1,000 ★. Remeasured in p890: the cohort maximum is **118 ★**
  (`boyuchengz/canvas-mcp`) and **not one member gained a single star** in the interval. The
  form shortens time-to-pilot and belongs in the demo kit; it does not belong on a client
  roadmap yet.
- **No locatable repository for `AcademiClaw`** (arXiv 2605.02661, students setting challenges
  for AI agents). Paper only. Recorded so a later pass does not re-chase it.

## Corrections made this pass

- **`openedx/openedx-platform` does not exist** — 404 on every branch. It had propagated through
  `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` and `compose/patterns.md`
  in earlier passes. The real slug is **`openedx/edx-platform`**.
- **Single-author student projects removed from this table.** Earlier passes listed dozens
  alongside institution-backed platforms, which made the table useless for picking a starting
  point. They were real — `Abdulrahman-hayatu/lessonplan-ng` (Apache-2.0, 0 ★),
  `mayuribagga/ai-worksheet-maker` (MIT, 0 ★), `bishoynabilanis/jessica` (MIT, 0 ★) all verify
  `200` — but a studio cannot build on them. Preserved in
  `archive/2026-11-18-pre-cleanup/agents-top.md` rather than deleted.
- **Star counts are now measured, not asserted.** Earlier passes of this KB recorded star
  figures later found to be inflated, then a later pass concluded stars were unmeasurable. Both
  were wrong: batched `repo:` qualifiers against `search/repositories` work in this session
  (a *single* `repo:` qualifier returns `422`, which is what made it look impossible).
