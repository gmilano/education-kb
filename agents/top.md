---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI Agents — curated, license-verified

**34 real agents** below — **29 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**5 copyleft** — **unchanged through the tenth pass (`p805`, 2026-11-13)**.

🔵 **`p805` added zero rows. That is the third consecutive nil on agent supply, and
this pass stopped treating it as a result to re-derive and started treating it as a
budget to spend elsewhere.** All eight prescribed legs ran again. The global legs
returned `DeepTutor`, `OpenMAIC`, `ai-engineering-hub`, `ai-engineering-from-scratch`,
`OpenEduCat`, `RosarioSIS`, `OpenOLAT`, `Open edX`, `Moodle` and `Canvas` — 🟢 **every
education-specific name already curated here or in `repos/foundations.md`.** The only
non-generic candidate the battery produced that was *not* obviously held —
**GegoK12** — turned out to be verified by this base at `p802` already.

🔴 **So this pass audited the base against itself instead, and found a propagation
defect.** A diff of byte-verified, green-marked repository slugs in the two append-only
trending logs against the four files a studio actually reads returned **11 verified
repositories that had reached no shelf file at all** — including one,
`portabilis/i-educar`, that the log has claimed since `p667` was already shelved.
🟢 **All 11 were re-verified live this pass and the adoptable ones promoted**: three to
the xAPI layer, four to a new skills-and-credentials layer, one to the LMS table, three
to the SIS table in `verticals/solutions.md`. 🔵 **None belongs in *this* table** —
none is an agent. 🔴 **The underlying cause is structural and is not fixed:
`agents/trending.md` is 79,190 lines and `repos/trending.md` is 62,315. Append-only
preserves the trend and buries the finding.**

🔵 **`p804` added zero rows, and `p803`'s saturation finding reproduced exactly.** All
eight prescribed legs ran again; every education-specific name they returned was
already curated here. 🟢 **The two genuinely new repositories found this pass —
`rohitg00/ai-engineering-from-scratch` (MIT, `78.6k★`) and `patchy631/ai-engineering-hub`
(MIT, `41.8k★`) — are deliberately NOT in this table**, although both are larger than
every agent in it. They are **AI-engineering curricula**: no runtime, no learner model,
no integration surface. A row here asserts a studio could start a build from the
artifact, and it could not. They are shelved instead in `repos/foundations.md` under a
new **curriculum-corpus layer**, which exists because `T19` measured the demand:
**three dated AI-literacy mandates and no open education-licensed curriculum to meet
any of them.** 🔴 **Provenance caveat for this pass: `curl` to `github.com` is denied
by the session's egress proxy (`403`), so grants and sizes were read from the rendered
page via `WebFetch` — sidebar-verified, not payload-verified.** The pass's substantive
output is in `intel/market.md` (all five regions), `intel/trends.md` (`T18`, `T19`) and
`compose/patterns.md` (`P16`).

🔵 **`p803` added zero rows for a new reason: no candidate surfaced to assess.** The
eighth pass ran all eight prescribed search legs — four global, four regional — and
**every finding they returned was already curated here.** That is saturation, not
rejection, and it is distinct from `p802`, which assessed four candidates and
rejected all four. The pass's output is therefore recorded in `intel/trends.md`
(`T17`), `compose/patterns.md` (`P15`) and the two trending logs: **the education
tutor-*evaluation* cluster was probed at the byte level and five of its six members
carry no usable software grant.** The one that does — `Kobby-Adjei/ai-tutor-benchmark`,
MIT, payload-verified — is held off this table at `0★` / `0` forks, because a row here
implies a studio could start from it. 🟢 **Two regional facts verified in earlier
passes but never propagated to `intel/market.md` (PISA 2025; Vietnam's MOET Decision
`2422`) were found by audit and promoted.**

🟢 **Zero rows
added at the sixth pass, deliberately.** Four candidates were assessed and all four
rejected (the reasons are in `agents/trending.md`; the headline one,
`tutornew/OpenTutor`, has **8 stars, 5 commits and no license at all**).
**Education agent supply did not move this window — platform-native AI did**,
and that finding is recorded in `verticals/solutions.md`, `repos/foundations.md`
and `intel/trends.md` `T15` rather than being forced into this table. Given this
file's documented history of miscounting its own rows across four editions, **a
pass that adds nothing and says so is the correct output.** 🔴 **Counting defect fixed this
pass:** every earlier edition of this file headlined a single figure ("26 real
agents", "20", "18", "11") that counted **only the build-safe table** while the
sentence said "agents below", which also covers the copyleft table. The two
numbers are now stated separately so a proposal cannot quote the wrong one.
Every row was verified on
2026-11-13 by fetching the repository page and reading GitHub's own license
field and star count. Four candidates that circulate on "best open source AI
agent" lists are **rejected on license grounds** and listed in the exclusions
section rather than deleted silently — an excluded candidate is information.

**What changed this fifth pass (2026-11-13):** the fourth pass replaced "no SIS
has an agent interface" with what it called a sharper claim — **"not one
*open-source* SIS has an agent interface."** That claim is **also withdrawn**,
and the reason is structural: every SIS search in four passes looked for an
*education-specific* server. **OpenEduCat (LGPL-3.0, 911 stars, 789 forks) is a
set of Odoo addons, and Odoo has two mature MCP servers whose tools take the
model name as a parameter** — `erpipe-org/mcp-odoo` (**MIT, 433 stars**, writes
gated behind a three-call approval protocol) and `ivnvxd/mcp-server-odoo`
(**MPL-2.0, 415 stars**, per-model allowlist in a companion Odoo module). At 433
stars the MIT one is the **fourth-largest agent in this KB** and larger than
every education-specific agent ever admitted here. The path is **architecturally
verified, not empirically run** — see the gap note. Two further entries:
`sabis-mcp-server` (ISC, Türkiye — EMEA's first agent-to-SIS path) and
`DeepTutor-MCP` (Apache-2.0 — the first MCP server in this base built over
another *agent's* data rather than a platform's).

**What changed at the fourth pass (2026-11-13):** the three earlier passes today
worked the LMS surface and then the learner-record surface, and all three
concluded that **no SIS anywhere has an agent interface** — the third pass
called it "a confirmed absence across two consecutive passes." **That conclusion
was over-generalized and is corrected here.** Two MIT MCP servers do reach a
student information system: `edupage-mcp` (31 tools, EduPage — Slovakia and
Czechia) and `mcp_hemis_student` (HEMIS — Uzbek universities). The precise
finding that survives: **no *open-source* SIS has an agent interface, while
national proprietary SIS products are getting them from individual developers.**
Four further entries: `janestreet/agent_skills` (MIT, **7.9k**) — the largest
permissively licensed education artifact in this base, and not a program at all;
`zavora-ai/mcp-education`, the only server that gates writes in its own tool
contract; and two 0-star repos admitted purely for design — `ai-tutor-agent`
for tutoring guardrails and `AI-Teaching-Agent` for its human review gate.

**What changed at the third pass:** the KB's attention so far has
been on the *LMS* surface — seven Moodle MCP servers, one Canvas server. This
pass went after the **learner record** instead, and found the layer that was
missing: `DavidLMS/learnmcp-xapi` (MIT) is an MCP server over any xAPI-compliant
Learning Record Store, and it is the only verified **agent↔learner-record write
path** in this base. It is the agent half of a gap closed on the infrastructure
side in `repos/foundations.md`, where two permissive LRS implementations are
also new. The **SIS MCP gap stays open and was re-probed, not assumed**. Second
new entry: `EduAgentic`, the only MCP **+ A2A** education example found.

**What changed at the second pass:** the Moodle MCP gap this KB declared open is
**closed** — `Faixiang/Moodle-MCP` (MIT, 206 stars) is a real, maintained,
significant Moodle MCP server, and six more Moodle MCP servers were verified
behind it. Three new agents entered above 60 stars, including
`teacher-to-skills` (Apache-2.0, 475) which is now the third-largest
education-specific agent on GitHub. The first LATAM-origin and Africa-origin
education agents were found — at 0 stars each, which is itself the finding.

Verification channel note: `curl -sI https://github.com/...` returns `403`
through this session's egress policy for repositories not attached to the
session, and `api.github.com` refuses the same way, so licenses and stars below
come from the rendered repository page (GitHub's own license detection).

## Build-safe agents (MIT / Apache-2.0 / BSD / ISC)

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 58.7k | Lifelong personalized tutoring; learner model persists across sessions and builds learning paths. **v1.7.2 released 2026-11-06**; 7.1k forks. Largest education-specific agent on GitHub. |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 43.4k | Open Multi-Agent Interactive Classroom (Tsinghua MAIC lab). Turns a topic or document into a multi-agent classroom — teacher, peers, assistant — in one click. **README News lists v1.5.0-rc.2 on 2026-11-12; GitHub Releases is empty**, so treat the version as pre-release. Ships pt-BR and es-MX locales. |
| teacher-to-skills | https://github.com/JuneYaooo/teacher-to-skills | Apache-2.0 | 475 | **New this pass.** Distills a specific teacher's materials (lecture video, notes, marked-up feedback) into a source-backed agent Skill that teaches to that teacher's standard and tapers support as the learner improves. Conclusions are tied to sources; unevidenced material is flagged, not filled in. Learner progress is stored outside the generated Skill. Runs under Claude Code / Codex / OpenClaw. 73 forks. |
| mcp-odoo (ERPipe) | https://github.com/erpipe-org/mcp-odoo | MIT | 433 | **New this pass — the largest build-safe agent in this KB that reaches an open-source SIS, and it is not an education project, which is why four passes of SIS searching missed it.** 41 tools over **Odoo 16-19** (smoke-tested against 16.0/17.0/18.0/19.0): `search_records`, `read_record`, `aggregate_records`, `get_model_fields`, `list_models`, plus module helpers, diagnostics, migration, audit and cross-instance fan-out. Because the tools take the **model name as a parameter**, OpenEduCat's `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` are reachable with no education-specific code. **Writes are gated by construction — this is the row's real value:** direct `create`/`write`/`unlink` are blocked, and an approved write must pass `preview_write` -> `validate_write` -> `execute_approved_write` carrying a **single-use, same-process, expiring approval token**, with `confirm=true`, live non-empty `fields_get` metadata, and `ODOO_MCP_ENABLE_WRITES=1`; `ODOO_MCP_ELICIT_WRITES=1` adds a native confirmation prompt, and `execute_method` runs allowlisted methods only. XML-RPC default, JSON-2 on Odoo 19. 198 forks, 118 commits, Releases empty. **Formerly `tuanle96/mcp-odoo`** — the old slug is what search results still return, so record the new one. **Caveat for any proposal: the maintainer sells a hosted product (ERPipe) built on this repo** — the MIT grant is real; the roadmap has a commercial owner. |
| sabis-mcp-server | https://github.com/hanifisenturk/sabis-mcp-server | ISC | 2 | **New this pass — the third agent-to-SIS path in this KB and the first from EMEA (Türkiye).** MCP server over **SABIS**, the student information system of **Sakarya University**. One tool, `get-grades`: course codes and names, assessment types and weights, final letter grades, academic year and semester. 🔴 **Reaches the SIS by Puppeteer web scraping, not an API, and reads the student's own `USERNAME`/`PASSWORD` from environment variables** — a credential-replay design to read and *not* reproduce. README states it is unofficial, unaffiliated with the university, and for personal/educational use. 0 forks. Admitted for the regional and topological record: with `edupage-mcp` (Slovakia/Czechia, undocumented endpoints) and `mcp_hemis_student` (Uzbekistan), the pattern is three-for-three — **individual developers reaching captive national or institutional SIS products by unofficial means.** |
| DeepTutor-MCP | https://github.com/Suyutao/DeepTutor-MCP | Apache-2.0 | 1 | **New this pass — the first MCP server in this base built over another education *agent's* data rather than over a platform.** 60 tools exposing a self-hosted DeepTutor install to any MCP client: status, courses, syllabus and linked resources; Mastery Paths with outlines, evidence and review settings; Question Bank and practice queues with answer checks and analytics; generated books and reading material with notes, highlights and bookmarks; notebooks; knowledge-base metadata with file search and vector passage retrieval; historical sessions and memory documents; plus an opt-in tool that posts into a DeepTutor conversation. 15 commits, no releases. **Two hard dependencies before it runs:** a reachable self-hosted DeepTutor HTTP API, and — for the Mastery tutor tools — upstream PR **`HKUDS/DeepTutor#1785`, which its README says is still open and unmerged**. Not a dependency yet; admitted as the first evidence that DeepTutor (58.7k) is growing a tool ecosystem. |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT | 324 | Canvas LMS MCP server plus 8 agent skills for students and educators. The cleanest path to making an agent act inside Canvas. **Tool count is inconsistent on its own page: README says "up to 128 tools", the sidebar About says 102.** Default profile registers fewer; feature-gated tools raise the total. 106 forks. |
| Moodle-MCP | https://github.com/Faixiang/Moodle-MCP | MIT | 206 | **New this pass — closes this KB's declared Moodle gap.** Zero-dependency Python MCP server over the Moodle Web Service API. 10 **read-only** tools (courses, assignments, quizzes, deadlines, files), v1.4.0 dated 2026-11-02, docs in 10 languages, Moodle 3.x/4.x, verified by its author against Moodle 4.3.6. Read-only is a feature for a first engagement: no write path, no token escalation. |
| educhain | https://github.com/satvik314/educhain | MIT | 388 | Python package for generating educational content (questions, lesson plans, flashcards) with GenAI. Library, not an app — good as a content-generation node. |
| ai-shifu | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | AI-guided instruction: the agent teaches and answers in a scripted, author-controlled flow rather than free chat. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 280 | Open-source Intelligent Tutoring System with Bayesian Knowledge Tracing (UC Berkeley CAHLR). React + Firebase; mastery modelling is the asset. |
| Open TutorAI (CE) | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 117 | Community edition of an educational collaborative AI platform. |
| Tutor MCP | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 102 | MCP server that turns any LLM into an Intelligent Tutoring System; persistent, auditable learner state and progression governed outside the model. v0.7.0 adds institutional courses, invitations, enrollment. Small star count, unusually mature design. |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | **New this pass.** Local-first teaching assistant: starts from the teacher's own lesson plans, slides and assessments and drafts new lessons, student materials and decks. v9.18.2026.1 (Beta). **Explicitly single-teacher, not multi-tenant**, and student-facing features are experimental. README is honest that hosted models still receive the prompt content even though storage is local. 16 forks. |
| moodle-mcp (Rust) | https://github.com/G36maid/moodle-mcp | MIT | 29 | **New this pass.** Rust MCP server: courses, assignments, forums, grades, and files-as-markdown. Author reports live verification against **Moodle 3.7, 4.5 and 5.2** — the widest version coverage of any Moodle MCP server found. |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 16 | **New this pass — the only agent↔learner-record write path in this KB.** MCP server over any **xAPI 1.0.3**-compliant Learning Record Store. Three tools: record a statement, retrieve progress, manage activity vocabulary. Ships the `practiced` / `mastered` / `experienced` / `achieved` verbs and separates learners by an `ACTOR_UUID`, so one server serves a cohort. **Verified LRS targets: SQL LRS, Ralph, Veracity** (TinCan and xAPI Wrapper are listed as planned, not shipped). Python 3.8+, 4 forks, Releases empty, author states active development. This is what makes an agent's activity *reportable* by the institution instead of invisible. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (per README + LICENSE; sidebar shows only a generic "License" link) | 2 | **New this pass — the only credible open grading system found.** Automated argumentative-essay scoring (1–6) with label-aware feedback: fine-tuned Qwen2.5-7B LoRA discourse-move classifier → LightGBM scorer over 31 linguistic/discourse features → feedback generator, with a Gradio UI for single and batch scoring. Locally deployable. **Naming trap: the arXiv paper calls this system "ArguLens"; the repository never uses that name.** Vendored TextComplexityToolkit is MIT. |
| moodle-mcp (browser-session) | https://github.com/falkenslab/moodle-mcp | MIT | 2 | **New this pass.** Claims **~260 Moodle tools** including grading and quiz building — by far the largest surface found. Authenticates by opening a real browser for the user's own interactive login, so it **supports SSO and 2FA and needs no web-service token, admin rights, or Moodle plugin** ("your login, never your password"). Targets Moodle 4.5 and 5.x. 2 stars: powerful design, unproven. |
| moodle-mcp (publishing) | https://github.com/MarcosNahuel/moodle-mcp | MIT | 1 | **New this pass.** Aimed at *writing* pedagogical content: 40 high-level tools plus a `ws_raw` escape hatch across courses, sections, content, quizzes, gradebook, messaging, calendar and badges. Writes are **upsert-by-`idnumber`, so republishing is idempotent** — the right primitive for generated course content. Requires companion plugin `local_italiciamcp` for the full set; self-reported ~80% operability at v0.5.2. |
| Manu (tutor-ai-agent) | https://github.com/Jeanikt/tutor-ai-agent | MIT | 0 | **New this pass — the first LATAM-origin education agent this KB has found.** Voice-first math tutor **in Brazilian Portuguese**, adapting from 1st grade to university; spoken explanations render to an on-screen chalkboard. TypeScript + LiveKit Agents with a Next.js front end. In development, no public deployment. 0 stars — a seed, not a dependency. |
| EDUKAI LongView | https://github.com/Keitous/EDUKAI-LONGVIEW | ISC | 0 | **New this pass — the first Africa-origin education agent this KB has found.** MCP-powered *longitudinal* learning intelligence: tracks a learner across multiple academic periods rather than single test scores, retrieves supporting evidence, flags sustained strengths and recurring difficulties, and recommends for teacher review ("agent recommends, teacher decides"). Bilingual FR/EN, author based in **Guinea**. Node.js/Express. **Synthetic data only** — a prototype. |
| EduAgentic (EduMCP) | https://github.com/kamalelafoui/Agentic-AI-EdTech-J33-J34 | MIT | 0 | **New this pass — the only MCP + A2A education example found.** FastMCP server on SSE exposing six tools (`search_courses`, `get_learner_profile`, `recommend_learning_path`, `generate_quiz`, `grade_quiz`, `get_learning_statistics`) **plus an A2A orchestrator** over three named agents (Tutor, Evaluation, Orientation). Every other education agent in this table is single-agent or MCP-only; this is the one place in the set to read an agent-to-agent education topology. **French-language** repo and docs — francophone provenance; the author's country is not stated on the page and is not asserted here. 0 stars, 0 forks, no releases: a course artifact. Take the **topology**, not the code. |
| socratic-tutor (Jane Street `agent_skills`) | https://github.com/janestreet/agent_skills | MIT | 7.9k | **New this pass — the largest permissively licensed education artifact in this KB, and it is not software.** Jane Street's first public agent skill: a strict Socratic tutor that runs a 3-5 question diagnostic, maps the topic into **4-10 sub-skills rated 0-5**, asks **one question at a time**, then adds spaced review and a final assessment. 510 forks, **2 commits** — it is a `SKILL.md` instruction set, so it needs an LLM host (coding agent or chatbot), ships no code and carries **no dependency or CVE surface**. Compare `education-agent-skills` (977 stars, CC BY-SA) in the rejected table: same artifact class, wrong instrument. This one is MIT and can go into a client deliverable as-is. Third-largest education agent here after DeepTutor and OpenMAIC, on two commits. |
| edupage-mcp | https://github.com/oliverhruby/edupage-mcp | MIT | 4 | **New this pass — the first verified agent-to-SIS path in this KB.** 31 tools over **EduPage**, the school information system used across Slovakia and Czechia: timetables, grades, homework and a daily summary, plus meal ordering, multi-school discovery, role-aware student switching and **2FA**. Distributed on PyPI (`edupage-mcp-full`), Docker/GHCR and the MCP Registry. **The caveat governs adoption:** it reaches EduPage through the community `edupage-api` library, which uses **undocumented endpoints** — there is no vendor contract, so it can break on any EduPage release. Python 3.10+, 1 fork, 123 commits. Take the topology; do not ship the dependency. |
| mcp_hemis_student | https://github.com/sukhrobyangibaev/mcp_hemis_student | MIT | 0 | **New this pass — the second agent-to-SIS path, and the first Central Asian project in this KB.** MCP server over **HEMIS** (Higher Education Management Information System), the student-information platform used by Uzbek universities: a student pulls their own academic record, schedule, grades and attendance. 9 commits, no repository description, no releases, 0 stars. Admitted **for the SIS topology only** — it is evidence that the student-record gap is closing from the national-platform direction, not a dependency. |
| mcp-education (zavora-ai) | https://github.com/zavora-ai/mcp-education | Apache-2.0 (per README; sidebar shows only a generic "License" link) | 1 | **New this pass — the only Rust education MCP server found, and the only server at any star count that gates writes in its tool contract.** Canvas LMS API: courses, assignments, grades, students, announcements. **12 tools split 9 read-only + 3 write operations that require approval** — the read/write boundary is declared by the server rather than left to the host's discretion, which is the design to copy for any education MCP server that writes to a gradebook. Built for "ADK-Rust Enterprise"; Rust 1.94.1, 1 fork. |
| ai-tutor-agent | https://github.com/vulinh1704/ai-tutor-agent | MIT | 0 | **New this pass — the clearest tutoring *guardrail* implementation found at any star count.** FastAPI + LangGraph, with three controls this KB has not found written down elsewhere: a **Socratic hint ladder** that escalates one level per turn up to a configurable cap; an **answer-leak guard** that regenerates a draft which reveals the final answer and substitutes a safe hint if it still leaks; and **rubric grading in which per-criterion scores are validated against the rubric and the totals are computed in code, not by the model**. A router node splits tutor / grader / clarify. SQLite checkpointing persists a session across restarts; a deterministic offline fake model runs the whole graph with no API key, which also makes it testable in CI. 0 stars — take the control design, not the repo. |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | 0 | **New this pass.** Compiles one Markdown teaching source into reviewable **Lab and Exam packages** plus short teaching decks, using structured DSLs, sandboxed evaluation and an MCP stdio server (`mcp_server/` with tool adapters, MCP manifest shipped in the wheel). **Nothing publishes automatically:** artifacts are validated, candidate-facing content is protected, and a human decision gates local export — the review-gate shape that `P6` (grading) and any assessment engagement needs. README states further MCP/Agent expansion is **frozen**, so treat it as a fixed reference rather than a growing project. |

## Copyleft — usable, but the license propagates

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| mcp-server-odoo | https://github.com/ivnvxd/mcp-server-odoo | MPL-2.0 | 415 | **New this pass — the governed alternative to `erpipe-org/mcp-odoo`, and the better choice where the *institution* must own the policy.** Reaches any Odoo model, so it too reaches OpenEduCat's student record. Access control lives in a **companion Odoo module** carrying a per-model allowlist with separate read / write / create / delete permissions, layered on Odoo's own access rights and record rules — so the client's Odoo administrator decides what an agent may touch, rather than an environment variable inside the agent's container. 17 tools including `create_records`/`update_records` batches, attachments, `aggregate_records`, `post_message` and (double-env-gated) `call_model_method`. Odoo 16.0+ in standard mode; JSON-2 with an API key on Odoo 19+. 190 forks. **Why it is in this table and not the one above: MPL-2.0 is *file-level* weak copyleft** — modifications to its own files must be published, but it combines freely with proprietary code, so unlike AGPL it needs a licence note in the deliverable rather than a redesign. 🔴 **Red flag to raise in every review: "YOLO mode" requires no companion module, bypasses all MCP-level access control and exposes 200+ models; full YOLO mode permits delete.** Its own README restricts it to development and testing. Never ship it, and grep for it in any inherited deployment. |
| LearnHarness | https://github.com/amosblomqvist/learnharness | AGPL-3.0 (**payload-verified this pass**: root `LICENSE`, `34,523 B`, `sha256:0d96a4ff68ad6d4b…`, affero×`16`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`; sidebar agrees) | 9.1k | **New this pass — the largest NEW education repository found in this window, and the fastest-growing artifact this base has tracked.** Desktop agent *harness* for learning hard material: agents plan and teach a lesson from the learner's current understanding toward a stated goal, and a **local knowledge graph stores ideas and the links between them rather than ability ratings** — a different persistence model from `DeepTutor`'s learner model and from `OATutor`'s Bayesian Knowledge Tracing, and the reason it is worth reading even though it cannot be shipped. Bring-your-own API keys; ships for macOS, Windows and Linux. `1,202` commits, `1.2k` forks. 🔴 **AGPL-3.0 is the whole adoption story: the network clause makes this unusable as the base of a distributed or hosted client product.** Take the knowledge-graph design, not the code. 🔵 Indexed write-ups are badly stale on size — one says `1.5k★`, another `5.7k★`; the rendered page said `9.1k★` this pass. |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | GPL-3.0 | 933 | AI tutor driven by Theory-of-Mind reasoning about the learner. GPL-3.0: fine for internal or hosted use, a problem for a distributed client product. |
| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | 3 | Open edX admin operations as an MCP facade for staff/superusers, native platform APIs only. Very early — reference, not dependency. |
| moodle-mcp-server (csmediapro) | https://github.com/csmediapro/moodle-mcp-server | AGPL-3.0 | 2 | Moodle MCP server over Web Services; 10 core tools plus cache management and `refresh_user_field_schema`. **Open-core: additional tools ship in a paid premium plugin.** AGPL plus a commercial upsell is the wrong base for a client deliverable — note it and move on. |
| moodle-mcp-server (lmscloud) | https://github.com/lmscloud-io/moodle-mcp-server | GPL-3.0 | 1 | Runs Moodle web services for administration and analysis; installs via `uvx`, authenticates with a Moodle web-service token. No repository description, no stated tool count. |

## Rejected candidates and why

Real and active projects that are **not** open-source-licensed in a way
Globant can build a client deliverable on.

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| PageLM | https://github.com/CaviraOSS/PageLM | CaviraOSS / "PageLM Community License" — **not OSI** | 2.1k | README requires prior written permission for commercial use or resale. Marketed as "open source"; it is source-available. Do not put it in a client stack. |
| llamatutor | https://github.com/Nutlope/llamatutor | **No license file** | 2.1k | Default all-rights-reserved. Good reference implementation of an AI personal tutor on Llama 3.1; not reusable without an explicit grant. |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 977 | 165 evidence-grounded education skills for Claude/Codex-style agents. CC BY-SA is a **content** license with share-alike — usable as pedagogy reference material, wrong instrument for shipped software. |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | **No licence file — re-verified at `HEAD` `a71078456a90` this pass** | 4 | 🔴 **Moved out of the build-safe table this pass, and the move is a correction of this base against itself.** `p801` (`T961`) established that this repository serves **no licence anywhere**, while its `EACL 2026` paper calls it *"MIT-licensed"*. The row in the build-safe table went on publishing `MIT` for a further pass. `p802` re-probed the clone channel and reproduced `T961` exactly — **same `HEAD`, still a `7`-entry tree, still no `LICENSE`, `COPYING` or equivalent in the root tree** — so the grant does not exist and the default is all-rights-reserved. Still the only pedagogy-specific eval harness found, so it remains worth reading and worth an upstream licence request; it cannot be adopted. 🔴 **This base has now carried a licence it had itself refuted for one full pass — see `ACTION p802-A`.** |
| educational-agents | https://github.com/nifalconi/educational-agents | **No license file** | 1 | **New rejection this pass.** Spanish-language teaching library ("agents in 2 lines") from the *Niñas Pro* applied-AI course for girls in **Chile** — genuinely interesting as LATAM education provenance, and the kind of project worth contributing a LICENSE file to. As published it is all-rights-reserved and cannot be adopted. v0.1.0 prototype, built on the OpenAI Agents SDK via OpenRouter. |

## Declared gaps

- **The learner-record gap is half closed, and the halves must not be
  confused.** `learnmcp-xapi` gives an agent a read/write path to the
  *learning-activity* record — xAPI statements: what the learner did, practiced
  and mastered. It does **not** reach the *student* record: enrolment,
  transcript, attendance, demographics, fees. Pattern `P9` needs the LRS
  and can be built today on permissive licenses; pattern `P8` needs the SIS.
  Scoping an advising engagement against the wrong one of
  these is the most expensive mistake available in this KB.
- **The SIS gap is CLOSED for one open-source SIS, and the reason four passes
  missed it is a search defect, not a market one (fifth pass).** The fourth pass
  withdrew "no SIS has an agent interface" and replaced it with "not one
  *open-source* SIS has an agent interface." **That is now withdrawn too.**
  OpenEduCat (LGPL-3.0, **911 stars, 789 forks** — the leading open-source
  education ERP) is a set of **Odoo addons**, and Odoo has two mature MCP servers
  whose tools take the **model name as a parameter**:
  `erpipe-org/mcp-odoo` (**MIT, 433 stars**, three-call gated writes) and
  `ivnvxd/mcp-server-odoo` (**MPL-2.0, 415 stars**, per-model allowlist in a
  companion Odoo module). `op.student`, `op.admission`, `op.exam.attendees` and
  `op.fees` are therefore reachable with no education-specific code.
  **The defect to learn from: every SIS search in four passes looked for an
  _education-specific_ server, so the largest relevant connector in the field —
  bigger than any education-specific agent in this KB except DeepTutor, OpenMAIC
  and `agent_skills` — was structurally invisible.** When a vertical gap looks
  empty, search the *platform* the vertical is built on.
- **What is still genuinely unserved, stated precisely so it can be priced.**
  **RosarioSIS** (GPL-2.0, 654 stars, PHP/Postgres, heavy LATAM K-12) and
  **Gibbon** (GPL-3.0, 638 stars, PHP/MySQL, international K-12) have **no
  agent interface and no generic connector of the Odoo kind** — searched by
  project name this pass and nothing returned. `frappe/education` (GPL-3.0, 707)
  sits on the Frappe framework, which is the next place to look for the same
  generic-connector trick. **The three servers that reach proprietary SIS
  products all do so unofficially** — `edupage-mcp` (undocumented endpoints via
  a community library), `mcp_hemis_student`, and new this pass
  `sabis-mcp-server` (Puppeteer scraping with the student's own credentials in
  environment variables). Three-for-three: **where the SIS is proprietary and
  national, the only agent paths are unsanctioned**, which is a contract risk,
  not an architecture.
- **`Gap 286` — the Odoo→OpenEduCat path is architecturally verified and has
  NOT been run.** The connectors' tools are model-generic and OpenEduCat is Odoo
  addons; both facts were read off the repository pages this pass. **No Odoo
  instance was stood up, OpenEduCat installed, and a tool called against
  `op.student`.** That run is the cheapest high-value experiment on this board.
  Until it is done, quote the path as *"the connector is generic and the SIS is
  Odoo addons"*, never as *"we have run it."*
- **Student-record *analytics* topology exists but could not be
  license-verified.** `EdyVision/student-services-mcp` (1 star) exposes 13
  tools including `fetch_student_dropout_risk`, `fetch_high_risk_students`,
  `fetch_attrition_statistics` and `fetch_attrition_feature_importance` — the
  closest thing found to a retention/early-warning tool surface, and a useful
  shape to copy for `P8`. **The rendered page shows no license field**, and it
  runs on **synthetic data** with no real SIS connection. Not admitted to the
  table: read it as a design sketch and do not adopt it without a license.
- **No pedagogy-specific eval harness at scale, and the only candidate is
  UNGRANTED.** `AITutor-EvalKit` (🔴 **no licence file — re-verified at `HEAD`
  `a71078456a90` in `p802`; the `MIT` this base published was refuted in `p801`
  and is withdrawn**, 4 stars, mathematics only) is still the only one found — unchanged across all
  three passes. Every agent in the table above claims pedagogical effect and
  none of them can be compared on it.

- **Grading is still nearly empty, but no longer absent.** `wwrwbs/AI_AWE`
  (Apache-2.0, **2 stars**) is the only credible open scoring *system* found —
  a real pipeline with a published paper behind it, at prototype scale.
  `nbgrader` (BSD-3-Clause, 1.4k) remains notebook autograding infrastructure,
  not an agent. The rest of the field is Kaggle-era TF-IDF/LSTM/DeBERTa
  coursework and single-star LLM wrappers, several of which are API-only
  (OpenAI/Azure/Cohere) and therefore unusable where data residency binds.
  **Nothing in grading is to grading what DeepTutor is to tutoring.**
- **Pedagogical evaluation is still the thinnest layer in education AI.**
  AITutor-EvalKit at 4 stars is the state of the art. Teams in every region are
  shipping tutors with no shared way to measure whether they teach.
- **The Moodle MCP field is now real but fragmented and unconsolidated.** Seven
  servers verified this pass, licenses split MIT / GPL-3.0 / AGPL-3.0, star
  counts 1–206, and **no two agree on tool surface**: 10 read-only
  (`Faixiang`), 40 idempotent-write + plugin (`MarcosNahuel`), ~260 via browser
  session (`falkenslab`), files-as-markdown in Rust (`G36maid`). There is a
  consolidation opportunity here, and in the meantime the choice is genuinely
  per-engagement — read-only vs write, token vs SSO, plugin vs no plugin.
- **LATAM and Africa now have education agents, both at 0 stars.** Manu
  (Brazil, MIT) and EDUKAI LongView (Guinea, ISC) exist and are the first this
  KB has found. They are prototypes, not foundations. The strategic reading is
  unchanged — localize permissively licensed APAC/North American agents — but
  the regional origin story has changed from *absent* to *nascent*, and a
  0-star repo by a Guinean author doing longitudinal learner analytics is worth
  watching.
- **The long tail is student coursework.** The `education-ai` GitHub topic lists
  71 repositories; the 20 most-starred run 475 down to 2 stars, and below
  `Claw-ED` (65) they are overwhelmingly single-author projects — Streamlit
  quiz generators, dropout-prediction notebooks, Chinese-language K-12 skill
  packs. Excluded here by design: a KB row implies "a studio could start from
  this."
