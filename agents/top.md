---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI Agents — curated, license-verified

**18 real agents** below, up from 11 last pass. Every row was verified on
2026-11-13 by fetching the repository page and reading GitHub's own license
field and star count. Four candidates that circulate on "best open source AI
agent" lists are **rejected on license grounds** and listed in the exclusions
section rather than deleted silently — an excluded candidate is information.

**What changed this pass:** the Moodle MCP gap this KB declared open is
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
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT | 324 | Canvas LMS MCP server plus 8 agent skills for students and educators. The cleanest path to making an agent act inside Canvas. **Tool count is inconsistent on its own page: README says "up to 128 tools", the sidebar About says 102.** Default profile registers fewer; feature-gated tools raise the total. 106 forks. |
| Moodle-MCP | https://github.com/Faixiang/Moodle-MCP | MIT | 206 | **New this pass — closes this KB's declared Moodle gap.** Zero-dependency Python MCP server over the Moodle Web Service API. 10 **read-only** tools (courses, assignments, quizzes, deadlines, files), v1.4.0 dated 2026-11-02, docs in 10 languages, Moodle 3.x/4.x, verified by its author against Moodle 4.3.6. Read-only is a feature for a first engagement: no write path, no token escalation. |
| educhain | https://github.com/satvik314/educhain | MIT | 388 | Python package for generating educational content (questions, lesson plans, flashcards) with GenAI. Library, not an app — good as a content-generation node. |
| ai-shifu | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | AI-guided instruction: the agent teaches and answers in a scripted, author-controlled flow rather than free chat. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 280 | Open-source Intelligent Tutoring System with Bayesian Knowledge Tracing (UC Berkeley CAHLR). React + Firebase; mastery modelling is the asset. |
| Open TutorAI (CE) | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 117 | Community edition of an educational collaborative AI platform. |
| Tutor MCP | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 102 | MCP server that turns any LLM into an Intelligent Tutoring System; persistent, auditable learner state and progression governed outside the model. v0.7.0 adds institutional courses, invitations, enrollment. Small star count, unusually mature design. |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | **New this pass.** Local-first teaching assistant: starts from the teacher's own lesson plans, slides and assessments and drafts new lessons, student materials and decks. v9.18.2026.1 (Beta). **Explicitly single-teacher, not multi-tenant**, and student-facing features are experimental. README is honest that hosted models still receive the prompt content even though storage is local. 16 forks. |
| moodle-mcp (Rust) | https://github.com/G36maid/moodle-mcp | MIT | 29 | **New this pass.** Rust MCP server: courses, assignments, forums, grades, and files-as-markdown. Author reports live verification against **Moodle 3.7, 4.5 and 5.2** — the widest version coverage of any Moodle MCP server found. |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT | 4 | Evaluation framework for the *pedagogical* effectiveness of LLMs as tutors (mathematics domain). Tiny, but still the only pedagogy-specific eval harness found. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (per README + LICENSE; sidebar shows only a generic "License" link) | 2 | **New this pass — the only credible open grading system found.** Automated argumentative-essay scoring (1–6) with label-aware feedback: fine-tuned Qwen2.5-7B LoRA discourse-move classifier → LightGBM scorer over 31 linguistic/discourse features → feedback generator, with a Gradio UI for single and batch scoring. Locally deployable. **Naming trap: the arXiv paper calls this system "ArguLens"; the repository never uses that name.** Vendored TextComplexityToolkit is MIT. |
| moodle-mcp (browser-session) | https://github.com/falkenslab/moodle-mcp | MIT | 2 | **New this pass.** Claims **~260 Moodle tools** including grading and quiz building — by far the largest surface found. Authenticates by opening a real browser for the user's own interactive login, so it **supports SSO and 2FA and needs no web-service token, admin rights, or Moodle plugin** ("your login, never your password"). Targets Moodle 4.5 and 5.x. 2 stars: powerful design, unproven. |
| moodle-mcp (publishing) | https://github.com/MarcosNahuel/moodle-mcp | MIT | 1 | **New this pass.** Aimed at *writing* pedagogical content: 40 high-level tools plus a `ws_raw` escape hatch across courses, sections, content, quizzes, gradebook, messaging, calendar and badges. Writes are **upsert-by-`idnumber`, so republishing is idempotent** — the right primitive for generated course content. Requires companion plugin `local_italiciamcp` for the full set; self-reported ~80% operability at v0.5.2. |
| Manu (tutor-ai-agent) | https://github.com/Jeanikt/tutor-ai-agent | MIT | 0 | **New this pass — the first LATAM-origin education agent this KB has found.** Voice-first math tutor **in Brazilian Portuguese**, adapting from 1st grade to university; spoken explanations render to an on-screen chalkboard. TypeScript + LiveKit Agents with a Next.js front end. In development, no public deployment. 0 stars — a seed, not a dependency. |
| EDUKAI LongView | https://github.com/Keitous/EDUKAI-LONGVIEW | ISC | 0 | **New this pass — the first Africa-origin education agent this KB has found.** MCP-powered *longitudinal* learning intelligence: tracks a learner across multiple academic periods rather than single test scores, retrieves supporting evidence, flags sustained strengths and recurring difficulties, and recommends for teacher review ("agent recommends, teacher decides"). Bilingual FR/EN, author based in **Guinea**. Node.js/Express. **Synthetic data only** — a prototype. |

## Copyleft — usable, but the license propagates

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
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
| educational-agents | https://github.com/nifalconi/educational-agents | **No license file** | 1 | **New rejection this pass.** Spanish-language teaching library ("agents in 2 lines") from the *Niñas Pro* applied-AI course for girls in **Chile** — genuinely interesting as LATAM education provenance, and the kind of project worth contributing a LICENSE file to. As published it is all-rights-reserved and cannot be adopted. v0.1.0 prototype, built on the OpenAI Agents SDK via OpenRouter. |

## Declared gaps

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
