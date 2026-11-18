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

**p894 (this pass) attacked this file's own declared gaps instead of re-measuring known
cohorts, and two of them were wrong in the same direction.** Special education and automated
grading were both recorded here as categories with *nothing in them*; both are populated, and
both were measured in one batch today — **special education tops out at 1 ★, automated grading
at 0 ★, with three of seven grading repos carrying no licence at all.** The registrarial gap
turned out to be half wrong in a more useful way: the agent layer really is missing, but the
**permissive platform underneath it exists** (`UniTime/unitime`, Apache-2.0, 360 ★, pushed
2026-11-17) and had fallen out of `verticals/solutions.md` in the 2026-11-18 rewrite. All three
gap entries below are rewritten with today's measurements, and the detail is in
`agents/trending.md`. Spot check only on the giants (`DeepTutor` 60,258 → **60,274**, `OpenMAIC`
43,874 → **43,878**, `LearnHarness` 10,002 → **10,020**) — a fifth consecutive confirmation of
the daily cadence. **Full sweep still due 2026-11-19.**

**p893 ran a full discovery leg and it changed the table's shape.** Ten agents were
added — the largest single-pass addition this KB has made — including **LearnHarness
(AGPL-3.0, 10,002 ★)**, which did not exist on 16 October 2026 and is now the third-largest open
education agent in the world. p893 also closed the table's most embarrassing hole: **there was
no Moodle MCP server in it**, despite Moodle being the most-installed LMS on earth. There are
now two, MIT, read-only and read-write. The two giants were spot-checked rather than fully
swept (`DeepTutor` 60,235 → **60,258**, `OpenMAIC` 43,868 → **43,874**), consistent with the
daily cadence finding below. **Full sweep still due 2026-11-19.**

**p892 spot-checked again** (`DeepTutor` 60,210 → **60,235**, `OpenMAIC` 43,859 → **43,868**,
every row below 40k ★ unchanged) — a third consecutive confirmation of the daily cadence. p892
spent its budget on the two gaps `intel/market.md` named highest-value (**India**, **Saudi
Arabia**) plus an agent-discovery leg, which found the two rows marked *Added p892*. **Full
sweep due 2026-11-19.**

**p891 acted on that note.** This pass ran **no full star sweep** — it spent the budget on four
gap-directed regional legs instead (Article 4 / Africa / Middle East / Canada), all four of
which closed a declared gap in `intel/market.md` or `intel/trends.md`. One spot check:
`HKUDS/DeepTutor` 60,186 → **60,210** (+24 in a day), consistent with the cadence finding.
**Star figures in this table are therefore as at p890 unless marked otherwise**, and one agent
(`Claw-ED`) was added with freshly measured figures. Full sweep due next calendar day.

## Education-specific agents

Built for teaching, tutoring or assessment — not general frameworks pointed at a classroom.
Sorted by stars.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 60,274 | 2026-11-18 | Agentic personalised tutoring grounded in the student's own material, with persistent learning history. Hit #1 on GitHub trending 28 Oct 2026; first released Dec 2025. Paper: arXiv 2604.26962. **The single largest open education agent in existence.** | APAC — HKU Data Intelligence Lab |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | 43,878 | 2026-11-18 | Multi-agent AI classroom: agents generate slides, quizzes and project-based activities and grade quiz answers. `v1.4.2` (2026-11-09) added course-level undo for manual edits and agent runs. Relicensed to MIT at `v0.3.0`, Jun 2026. | APAC — Tsinghua University |
| **LearnHarness** | https://github.com/amosblomqvist/learnharness | **AGPL-3.0** | 10,020 | 2026-11-12 | Desktop agent harness that *measures* what the learner understands before it teaches: probe → dependency-map the route to the goal → teach one reasoning step at a time → separate retrieval-practice sessions, all carried across sessions by a persistent knowledge graph. **Added p893. Created 2026-10-16 — 0 → 10,002 ★ in 27 days, the fastest growth this KB has recorded for any education repo**, and now the third-largest open education agent in existence. **AGPL-3.0, byte-read from `LICENSE@main`. Not usable in a closed derivative** — read it as the reference design for learner-state modelling, the capability every other tutor in this table lacks. No published learning-outcome study; users report being tested before being taught. | Global |
| **frametell** | https://github.com/sitor-ai/frametell | **AGPL-3.0** | 513 | 2026-11-12 | Turns source material into explainer videos via an "AI director" agent. Local-first and model-agnostic. **Added p893.** The only open *content-production* agent in this table — courseware generation rather than tutoring. AGPL. | Global |
| **ai-shifu** | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | 2026-11-18 | Author a course by typing it: the AI delivers the teaching and answers questions inside the flow the author scripted. **Added p893.** Permissive, pushed today, and the clearest open example of *authored* AI teaching — the script constrains the model, which is the control structure Oklahoma-style "no AI-only" rules actually require. | APAC |
| **Moodle-MCP** (Faixiang) | https://github.com/Faixiang/Moodle-MCP | MIT | 208 | 2026-11-01 | Zero-dependency MCP server over the Moodle Web Service API: courses, assignments, quizzes, deadlines, files. **Read-only by design.** **Added p893 — the first Moodle MCP server this table has ever carried**, which was a hole given Moodle is the most-installed LMS on earth. Ships a companion agent skill, https://github.com/Faixiang/Moodle-Course-Watch (MIT, 0 ★), that diffs new coursework and lists what is still unsubmitted. README localised into 10 languages. | APAC |
| **edumcp** | https://github.com/aieducations/edumcp | Apache-2.0 | 155 | 2025-05-05 | An attempt to standardise MCP for education applications. **Added p893 as a cautionary entry: 155 ★ and untouched since May 2025.** The idea was early and right; the project is dormant. Read the protocol sketch, do not depend on it. | Global |
| **gen-mentor** | https://github.com/GeminiLight/gen-mentor | **CC0-1.0** | 137 | 2026-10-23 | Reference implementation for *GenMentor* (WWW '25 oral): a multi-agent framework for goal-oriented, skill-gap-aware learning — it infers the gap between the learner's current skills and a target role, then plans content against it. **Added p893.** **Licence is CC0-1.0, byte-read** — a public-domain dedication, not a software licence, so it carries no patent grant and no warranty disclaimer. Legally the most permissive row here and the least conventional; have counsel confirm before shipping it. | APAC |
| **Mentingo** | https://github.com/Selleo/mentingo | MIT | 109 | 2026-11-18 | Self-hosted **AI-native LMS** with a built-in AI mentor and role-play, white-label and multi-tenant, Postgres + pgvector, one-click AWS Marketplace deploy. **Added p893.** Listed here *and* in `verticals/solutions.md` because it is genuinely both. **Its significance is the licence: an MIT LMS.** This KB's first structural finding is that the platforms clients run are copyleft — Mentingo is the counter-example, and therefore the shortest route to a closed, branded derivative. Corporate L&D and compliance training, not K-12. | EMEA — Poland |
| **canvas-mcp** (Sachdev) | https://github.com/vishalsachdev/canvas-mcp | MIT | 334 | 2026-11-18 | MCP server exposing Canvas LMS — courses, assignments, submissions — as agent tools. | North America — USA |
| **BloomTutor** | https://github.com/Li-Evan/BloomTutor | MIT | 315 | 2026-11-17 | Tutor that structures interaction around Bloom's taxonomy levels. | APAC |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | 282 | 2026-11-17 | Intelligent tutoring system with open problem banks and tutoring-effect instrumentation; built for A/B-testable learning research. | North America — UC Berkeley |
| **molly554/whiteboard-ai-tutor** | https://github.com/molly554/whiteboard-ai-tutor | MIT | 223 | 2026-11-17 | Whiteboard tutor with animated lessons and interactive playback. Created after Aug 2026 — one of the fastest-growing new entrants. | Global |
| **OpenPronounce** | https://github.com/OpenPronounce/OpenPronounce | MIT | 221 | 2026-11-09 | Open pronunciation assessment — the language-learning niche where open source is genuinely competitive with commercial APIs. | Global |
| **OpenTutor** | https://github.com/zijinz456/OpenTutor | MIT | 181 | 2026-11-17 | Open tutoring agent. | APAC |
| **canvas-mcp** (Cheng) | https://github.com/boyuchengz/canvas-mcp | MIT | 118 | 2026-10-27 | **Read-only** MCP server connecting Claude/ChatGPT to Canvas LMS. A second, independent `canvas-mcp` — read-only by design, which is the safer default for a student-data pilot. | North America |
| **Open TutorAI (CE)** | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 118 | 2026-06-26 | Community edition of a self-hostable tutor platform. Licence text carries an "All rights reserved" header over a BSD-style grant; SPDX confirms BSD-3-Clause. | EMEA |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 104 | 2026-11-17 | MCP server that turns any LLM into an Intelligent Tutoring System — the ITS loop (learner model, next-item selection, graduated hints) exposed as **tools** rather than as an application. **Added p892.** The most actively developed member of the "tutor as an agent skill" cohort, and it was missing from the cohort p890/p891 measured — see `agents/trending.md`. | Global |
| **EduAgent** (`AI_Tutor_Release`) | https://github.com/Zenglian990/AI_Tutor_Release | MIT | 93 | 2026-11-10 | RAG tutor built specifically for **K-9** (grades 1–9), self-described as the first open-source RAG tutor targeted at that band in China. **Added p892.** Notable because it is **age-banded by design** — a product requirement under the UAE's under-13 prohibition and several US state statutes — and because it is retrieval-over-curriculum, not training-on-student-data. | APAC — China |
| **TeachMeCoding** | https://github.com/liangxiao777/TeachMeCoding | Apache-2.0 | 73 | 2026-10-30 | Local-first AI coding tutor: personalised roadmaps, lessons, hands-on practice with execution. | APAC |
| **aula** | https://github.com/luumlabs/aula | AGPL-3.0 | 66 | 2026-11-17 | Turns notes, slides and past exams into lessons. **AGPL — not usable in a closed derivative.** | Global |
| **Claw-ED** | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | 2026-09-19 | Local-first AI teaching assistant: editable lesson drafts, student materials and slides, generated from the teacher's own curriculum with a model of their choice. Self-described teacher-reviewed beta. **Teacher-facing**, which this table is otherwise thin on, and **local-first + bring-your-own-model**, which is the posture EMEA sovereignty procurement now asks for. **Caveat: trending on stars through Oct 2026 while its last commit is 2026-09-19** — read it as a design reference, not a dependency. Licence byte-read from `LICENSE@main` (`Copyright (c) 2026 EDUagent Contributors`). | Global |
| **moodle-mcp** | https://github.com/G36maid/moodle-mcp | MIT | 30 | 2026-10-20 | Second Moodle MCP server, and the **read-write** counterpart to `Faixiang/Moodle-MCP`: it operates courses, assignments, forums and grades, and serves files as markdown. **Added p893.** The read-only/read-write split across two MIT servers is the useful part — pilot on the read-only one, graduate to this when the client accepts write scope. | APAC — Taiwan |
| **usp-mcp** | https://github.com/CaioCastro1/usp-mcp | MIT | 28 | 2026-11-13 | Portuguese-language MCP server over Universidade de São Paulo's student systems: e-Disciplinas (Moodle) coursework and deadlines, course catalogue, refectory menus. **Added p893.** **This is the second LATAM-origin education agent this KB has verified, and at 28 ★ it is nearly 3× the first** (`warleysr/ankipa`, 10 ★) — see `agents/trending.md` for what that does to the standing regional finding. | LATAM — Brazil |
| **wassce-benchmark** | https://github.com/acheamponge/wassce-benchmark | MIT | 4 | 2026-04-07 | Benchmark evaluating open LLMs on the **WASSCE**, the school-leaving exam about two million West Africans sit each year. **Added p893.** Not an agent — an eval gate, like `pedagogy-benchmark`. **It is the only African-curriculum open evaluation asset this KB has found**, and it is the thing to measure against before any West African claim. Licence byte-read MIT. | EMEA — Africa |
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

**34 education-specific agents, every URL and licence verified.** (p894 added no rows: its four
legs produced 14 verified repositories, every one at 0–2 ★, and the p893 rule that this table
carries only what a studio can actually build on was applied rather than relaxed. They are
measured and reasoned about in `agents/trending.md`.) (22 at p891; `tutor-mcp` and
`EduAgent` added in p892; **ten added in p893** — `LearnHarness`, `frametell`, `ai-shifu`,
`Moodle-MCP`, `edumcp`, `gen-mentor`, `Mentingo`, `moodle-mcp`, `usp-mcp` and
`wassce-benchmark` — every one of them star-measured via batched `repo:` qualifiers and
licence byte-read from `raw.githubusercontent.com`.)

**Three of p893's ten are AGPL or CC0, not MIT/Apache.** The table is no longer
overwhelmingly permissive at the top, and the largest new entrant is the least usable one.
Read the licence column before the star column.

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
| https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | 3 | 2026-10-22 | Open edX admin operations (staff/superuser) as an MCP facade, native `openedx-platform` APIs only, targeting the **Ulmo** release. Paired with its Tutor plugin https://github.com/blend-ed/tutor-contrib-openedxmcp (AGPL-3.0, 2 ★). **Added p893 — and with a correction.** Secondary coverage of the September 2026 Open edX blog announcement reads as though this is a first-party `openedx/*` project. **It is not**: both repos live under `blend-ed`, a vendor org. It is announced-on-the-official-blog, which is not the same as governed-by-the-foundation. Treat it as a credible vendor contribution with no foundation maintenance guarantee. |

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
a **skill or MCP server inside an existing coding agent** — `ArnaudGuiovanna/tutor-mcp`
(MIT, 104 ★), `boyuchengz/canvas-mcp` (MIT, 118 ★), `BaronCyrus/dsh-aha-tutor` (MIT, 46 ★),
`smashburger-dev/socratic-workshop` (MIT, 24 ★), `bayshores/godspeed` (AGPL-3.0, 22 ★),
`Aisland-SJL/Aisland-teach` (MIT, 18 ★). All are small, but the direction is consistent and it
shortens time-to-pilot dramatically: no front end to build, and the learner already has the
client installed.

**p892 revised this cohort's reading, and the revision is about method.** p890 and p891 both
measured the cohort, found every member unmoved, and concluded the form had no traction.
**`tutor-mcp` (104 ★) was not in the set either pass measured** — it was found this pass by a
fresh discovery search rather than by re-measuring known rows. Including it, the cohort maximum
is unchanged at 118 ★, but the cohort is **not** static: `tutor-mcp` was pushed 2026-11-17 while
`boyuchengz/canvas-mcp` has been idle since 2026-10-27. **Star traction is still absent;
development activity is not.** The lesson is that re-measuring a set you did not re-enumerate
produces "nothing changed" by construction. Watch condition unchanged — 1,000 ★ marks the form
established — but re-enumerate before re-measuring. Tracked in `agents/trending.md`.

## What we searched for and did not find

Recording gaps because an unrecorded gap looks exactly like coverage.

- **No open-source *agent* for student information systems or registrarial workflow — but the
  permissive *platform* exists, and this file was wrong to imply otherwise (rewritten p894).**
  The agent half holds: a dedicated leg found only course-capstone prototypes
  (https://github.com/aabbiisshhaa/student-support-agent, **2 ★**, **no licence**, Makerere
  University, Uganda; https://github.com/vaibhav9895-lang/student-support-agent-assignment,
  0 ★, no licence; https://github.com/leechenwei/Ai-Agent-Timetable, 0 ★, no licence, idle
  since 2025-02-24). The platform half does not: **https://github.com/UniTime/unitime is
  Apache-2.0, 360 ★ and was pushed 2026-11-17** — Apereo's university course and exam
  timetabling and student scheduling system, designed to interface with an existing SIS or run
  standalone. It was verified and licence-hash-checked by an earlier pass, then dropped from
  `verticals/solutions.md` in the 2026-11-18 rewrite; it is restored there and in
  `repos/foundations.md` in this pass. **Caveat on the component licence:** its solver,
  https://github.com/UniTime/cpsolver, is **LGPL-3.0**, so a static link pulls the weaker grant
  into scope. This remains the clearest build-vs-adopt gap in the industry and the most
  defensible studio IP — **what you build is an agent tier over UniTime, not a platform.** See
  `compose/patterns.md` **P12**.
- **Special education and accessibility accommodation: a populated category with a 1 ★ ceiling
  (rewritten p894 — the previous "no dominant open agent" phrasing understated what is there and
  overstated what it is worth).** Measured today:
  https://github.com/robotros/California-IEP-AI-project-kit (MIT, **1 ★**, 2026-10-27),
  https://github.com/SudhanvaJ-bit/project-samarth (**no licence** at any candidate path, 1 ★,
  2026-11-15, 14-section IEP drafting baselined on India's RPwD Act 2016),
  https://github.com/dougdevitre/access-to-education (MIT, 0 ★, 2026-10-24) and
  https://github.com/AaronGrace978/EduHelp (**AGPL-3.0**, 0 ★, 2026-10-14). **Ceiling 1 ★; half
  the cohort unlicensed or AGPL.** None is a dependency and none earns a row above. The durable
  asset is one design rule, taken from `project-samarth` and already generalised into
  `compose/patterns.md` `P496-1`: **merge the statutory accommodation baseline into agent state
  so the model can add but cannot remove a required accommodation.** The build-vs-adopt answer
  here is *build*, from that rule. `virtualryder/edu-ai-agents` remains the only entry in the
  table above that names IDEA/504 and ADA Title II as design goals, and its deterministic WCAG
  pre-flight is the accessibility counterpart to the same idea.

- **Automated grading has zero open-source traction, and it is the one use case every
  jurisdiction regulates (new p894).** Seven repos measured in one batch:
  https://github.com/asu2304/auto-assessment-agent (MIT),
  https://github.com/macsnoeren/genai-open-assessment (**GPL-3.0**),
  https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent (MIT),
  https://github.com/littlecookie0722/AI-Teaching-Agent (MIT),
  https://github.com/Atmankhyar/AI-agent-for-automatic-exam-grading (**no licence**),
  https://github.com/omerbbbb/ai-graded-assessment-platform (**no licence**),
  https://github.com/timothyheeeee/Autonomous-Grading-Engine (**no licence**). **Every one is at
  0 ★ and three of seven have no licence.** Set that against the regulatory map — EU Annex III
  high-risk, Vietnam's high-risk list, Oklahoma's and Maryland's human-oversight rules — and the
  conclusion is commercial, not academic: **the most regulated education use case has nothing to
  adopt, so grading is a build and the regulation is its specification.** Two ideas in the cohort
  are worth more than its code, and both are already in this KB's patterns: confine the LLM to
  evidence extraction and keep scoring deterministic, and anchor evidence per criterion with a
  separate regrade path — the second is what makes an appeal procedure possible, which is what
  Annex III actually requires.
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
- **No open education agent originates from India, Africa or the Middle East.** p891 and p892
  ran dedicated legs for Africa, the Middle East, Saudi Arabia and India. All four returned
  substantial policy and national-programme evidence (see `intel/market.md`) and **not one
  repository.** India mandates AI across Classes III–VIII from 2026–27 and Saudi Arabia is
  training 240,000 teachers; neither has produced an open education agent this pass could find.
  With the standing LATAM result (`warleysr/ankipa`, 10 ★) the pattern is firm: **open education
  agents come from East-Asian and European universities; every other region is a consumer of
  them.** Stated as a finding rather than a hole — it defines the localisation market, and it
  is why `compose/patterns.md` **P10** treats language and curriculum corpus as the swappable
  parts.
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
