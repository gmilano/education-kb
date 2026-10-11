---
industry: education
region: Global
updated: 2026-10-11
---

# Education — AI agents shelf

**Pass 130, 2026-10-11.** Full rewrite. Every row below was verified this pass against the GitHub
repository-search API (existence, owner, star count, SPDX licence, last push, fork flag) and, where
noted, by reading the repository page. Rows are ordered by how useful they are to a studio
engagement, not by stars.

## How these rows were verified (and one instrument that does not work here)

- **Working instrument:** GitHub repo search via the session's GitHub tool. It returns the
  authoritative `license.spdx_id`, `stargazers_count`, `pushed_at`, `archived` and `fork` fields.
- **Working instrument:** fetching the rendered `github.com` repository page, used to confirm
  licence wording, releases and fork parentage.
- **BROKEN instrument — do not trust it in this environment:** `curl -sI https://github.com/<repo>`
  returns **HTTP 403 for every URL**, real or not. A control request for the deliberately
  nonexistent `zzz-not-a-real-org-9981/zzz-not-real-9981` also returned 403. **A 403 here is not
  evidence of anything**, so `curl -sI` cannot be used to tell a real repo from a typo. The KB's
  standing instruction to verify with `curl -sI` does not work from this runner; use repo search.
- The GitHub REST API for arbitrary repositories (`api.github.com/repos/...`) is blocked for this
  session, as is the `gh` CLI search path. Repo search is the only endpoint that reaches repos
  outside the session's own scope.

## Agents

| agent | repo | licence | stars | last push | region of origin | what it actually does |
|---|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | **41 136** | 2026-10-08 | APAC (HKUDS, Hong Kong) | Lifelong personalised tutoring agent. By far the largest education-specific agent in open source, and permissively licensed — the default starting point for a tutoring engagement. |
| **educhain** | [`satvik314/educhain`](https://github.com/satvik314/educhain) | **MIT** | 388 | 2026-10-09 | unplaced | Python package that generates educational content (lesson plans, question banks, MCQs) with an LLM. Useful as a content-generation library inside a larger system. **Caveat:** the repo publishes no GitHub releases and its README's own version history stops at v0.3.13 (October 2024). |
| **canvas-mcp** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | 288 | 2026-10-11 | unplaced | Canvas LMS MCP server — courses, assignments, submissions, rubrics, quizzes, grading — exposed as agent tools. **The canonical repo of a fork swarm** (see the fork warning below). |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | 264 | 2026-10-11 | North America (CAHLR lab, UC Berkeley) | Intelligent tutoring system with Bayesian Knowledge Tracing over a ReactJS + Firebase stack. The reference implementation when a client wants *auditable* mastery estimates rather than an LLM's opinion. |
| **moodle-ai-skill-navigator** | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | GPL-3.0 | 222 | 2026-09-29 | unplaced | Moodle plugin adding AI tutoring, quiz generation, mind maps and RAG over course materials. The most-starred *in-Moodle* AI plugin found. GPL-3.0 — copyleft, consistent with Moodle itself. |
| **GenMentor** | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | 133 | 2026-10-08 | unplaced | LLM multi-agent framework for goal-oriented learning in an ITS; the code behind a WWW 2025 industry-track paper. CC0 is a public-domain dedication — usable, but it carries no patent grant, unlike Apache-2.0. |
| **tutor-mcp** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | 44 | 2026-10-10 | unplaced | Go MCP server that gives any LLM durable learner state: BKT mastery, review scheduling, session memory, misconceptions, and auditable pedagogical decisions. LMS-agnostic, so it pairs with any connector below. Self-described alpha. |
| **claude-moodle-dev** | [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | 39 | 2026-06-22 | unplaced | Not a learner-facing agent: a toolkit of agent skills for *building* Moodle plugins (XMLDB, Hooks API, PHPUnit, Behat, privacy/GDPR, accessibility). Relevant to delivery velocity on a Moodle engagement. |
| **ideas** | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | **Apache-2.0** | 28 | 2026-09-05 | EMEA (Utrecht University, NL) | Feedback services for intelligent tutoring systems — domain reasoners that produce step-level hints for maths/logic exercises. Haskell. Narrow, old-school, and genuinely rigorous where LLM feedback is unacceptable. |
| **canvas-lms-mcp** | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | 9 | 2026-10-10 | unplaced | Second, independent Canvas MCP implementation (read courses/assignments/submissions/rubrics, grade and comment). Small, but a useful cross-check against the canonical one. |
| **campus-cli** | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) | ISC | 11 | 2026-10-11 | **LATAM (Peru)** | CLI + MCP server over **Blackboard Learn** — the only Blackboard connector in this KB, and the only LATAM-origin education agent found. Targets UPC's Aula Virtual (Universidad Peruana de Ciencias Aplicadas); Canvas and Moodle are on its roadmap. ISC is permissive (BSD-equivalent). |
| **openedx-mcp** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | AGPL-3.0 | 2 | 2026-08-28 | unplaced | Open edX admin/authoring operations as an MCP facade, reusing the platform's own `is_staff`/`is_superuser` checks per request. **Experimental — 2 stars.** Listed because it is the only Open edX MCP path found, not because it is ready. |

### Licence flags — read before building

| repo | flag | consequence |
|---|---|---|
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION** (GitHub reads the licence as "Other"), 847 stars | The single most-starred education *agent-skills* collection found — 165 evidence-grounded skills for teachers, leaders and EdTech builders, spanning pedagogy, learning science, curriculum and assessment. **But the licence is not an OSI-recognised identifier**, so terms must be read before any client reuse. Do not assume permissive. |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **No licence file at all**, 103 stars | A 54-tool Canvas MCP server with real traction and **no grant of rights**. Absent a licence, default copyright applies and Globant cannot build on it. Prefer `vishalsachdev/canvas-mcp` (MIT). |
| [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) | **No licence field**, 17 stars | Implements MCP as a Moodle *web-service plugin* and is listed on marketplace.moodle.com, which makes it architecturally the cleanest Moodle→MCP route found. Unlicensed as published; ask the author before use. |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | AGPL-3.0 | Network copyleft. Fine inside a client's own estate, a problem if the client intends to offer it as a hosted service without reciprocal source release. |
| [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | Public-domain dedication, no express patent grant and no warranty disclaimer of the Apache-2.0 kind. Legal review prefers Apache-2.0 for client deliverables. |

### Fork-swarm warning — `canvas-mcp` and `tutor-mcp`

Web search for Canvas MCP servers returns **at least five repositories carrying a byte-identical
description** ("Canvas LMS MCP server — up to 102 tools and 8 agent skills for students &
educators. Works with Claude, Cursor, Codex, and 40+ agents"): `vishalsachdev`,
`YeetingWaterbottle`, `papatistos`, `fdis111` and others. The same pattern appears for `tutor-mcp`
under both `kvnloo` and `ArnaudGuiovanna`.

GitHub repo search **excludes forks by default**. Running the fork-excluding search returns only
`vishalsachdev/canvas-mcp` and only `ArnaudGuiovanna/tutor-mcp`; every other owner of an identical
description is therefore a fork. One of those forks (`fdis111`) still advertises "80+ tools and 5
agent skills, v1.1.0" — an older state presented as current.

**Rule for later passes:** when two repos share a description, resolve the canonical one with a
fork-excluding search before writing a row. Citing a fork hands a client a stale dependency with
no upstream.

## Declared gaps — searched this pass, found nothing worth a row

- **No education-specific agent-evaluation or learning-outcome benchmark** in open source. Nothing
  measures whether a tutoring agent actually improves learning, so every engagement needs its own
  evaluation harness. This is the largest hole on the shelf.
- **No LATAM-origin education agent above 11 stars.** `campus-cli` is the only one, and it is one
  person's university tool. An informed gap, not an absence of demand — see `intel/market.md`.
- **No Moodle MCP server with a clear permissive licence.** The two routes found are GPL-3.0
  (in-plugin) or unlicensed (web-service plugin), despite Moodle being the most deployed LMS.
- **No agent targeting a student information system** (enrolment, records, timetabling) — only LMS
  connectors. Administrative automation, the most-cited adoption driver, has no open-source agent.
