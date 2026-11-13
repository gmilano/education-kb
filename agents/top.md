---
industry: education
region: Global
updated: 2026-11-13
---

# Education AI Agents — curated, license-verified

**11 real agents** below. Every row was verified on 2026-11-13 by fetching the
repository page and reading GitHub's own license field and star count. Three
further candidates that circulate on "best open source AI agent" lists were
**rejected on license grounds** and are listed in the exclusions section rather
than deleted silently — an excluded candidate is information.

Verification channel note: `curl -sI https://github.com/...` returns `403`
through this session's egress policy for repositories not attached to the
session, so HTTP-status checking is not available here. Licenses and stars below
come from the rendered repository page (GitHub's own license detection). Anki's
license was additionally read from its `LICENSE` file because the sidebar does
not name it.

## Build-safe agents (MIT / Apache-2.0 / BSD)

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 58.6k | Lifelong personalized tutoring system; learner model persists across sessions and builds learning paths. Largest education-specific agent on GitHub. |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 43.4k | Open Multi-Agent Interactive Classroom (Tsinghua MAIC lab). Turns a topic or document into a multi-agent classroom — teacher, peers, assistant — in one click. |
| educhain | https://github.com/satvik314/educhain | MIT | 388 | Python package for generating educational content (questions, lesson plans, flashcards) with GenAI. Library, not an app — good as a content-generation node. |
| ai-shifu | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | AI-guided instruction: the agent teaches and answers in a scripted, author-controlled flow rather than free chat. |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT | 324 | Canvas LMS MCP server — up to 102 tools plus 8 agent skills for students and educators. The cleanest path to making an agent act inside Canvas. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 280 | Open-source Intelligent Tutoring System with Bayesian Knowledge Tracing (UC Berkeley CAHLR). React + Firebase; mastery modelling is the asset. |
| Open TutorAI (CE) | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 117 | Community edition of an educational collaborative AI platform. |
| Tutor MCP | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 102 | MCP server that turns any LLM into an Intelligent Tutoring System; persistent, auditable learner state and progression governed outside the model. v0.7.0 adds institutional courses, invitations, enrollment. |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | MIT | 4 | Evaluation framework for the *pedagogical* effectiveness of LLMs as tutors (mathematics domain). Tiny, but it is the only pedagogy-specific eval harness found. |

## Copyleft — usable, but the license propagates

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | GPL-3.0 | 933 | AI tutor driven by Theory-of-Mind reasoning about the learner. GPL-3.0: fine for internal or hosted use, a problem for distributed client product. |
| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | 3 | Open edX admin operations exposed as an MCP facade for staff/superusers, native platform APIs only. Very early (3 stars) — reference, not dependency. |

## Rejected candidates and why

These appear on 2026 "best open source AI agent" roundups. They are real and
active; they are **not** open-source-licensed in a way Globant can build a
client deliverable on.

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| PageLM | https://github.com/CaviraOSS/PageLM | CaviraOSS / "PageLM Community License" — **not OSI** | 2.1k | README requires prior written permission for commercial use or resale. Marketed as "open source"; it is source-available. Do not put it in a client stack. |
| llamatutor | https://github.com/Nutlope/llamatutor | **No license file** | 2.1k | No license shown on the repo page — default is all-rights-reserved. Good reference implementation of an AI personal tutor on Llama 3.1; not reusable without an explicit grant. |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 977 | 165 evidence-grounded education skills for Claude/Codex-style agents. CC BY-SA is a **content** license with share-alike — usable as pedagogy reference material, wrong instrument for shipped software. |

## Declared gaps

- **No dominant open-source agent for assessment/grading.** `nbgrader`
  (BSD-3-Clause, 1.4k) is autograding infrastructure for notebooks, not an
  agent. Nothing in the searched window is to grading what DeepTutor is to
  tutoring. This is an opportunity, not an absence of need.
- **Pedagogical evaluation is nearly empty.** AITutor-EvalKit at 4 stars is the
  only education-specific eval harness found. Teams are shipping tutors with no
  shared way to measure whether they teach.
- **The long tail is student coursework.** A search for education AI agents
  returns hundreds of 0–5 star single-author repos. They are excluded here by
  design; a KB row implies "a studio could start from this."
