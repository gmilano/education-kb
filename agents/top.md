---
industry: education
region: Global
updated: 2026-10-11
---

# Education — AI agents shelf

**Pass 131, 2026-10-11.** Pass 130's rows retained and re-verified; **two tiers p130 declared absent
are restored below**, because this KB's own append-only pages already carried them (see
`README.md` → Pass 131, `P131-A`). Every row was verified against the GitHub
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

### Moodle connectors — the tier p130 declared absent

p130's declared gaps said *"no Moodle MCP server with a clear permissive licence"*. **That is
wrong, and this KB had already established it is wrong.** Moodle's web-service API is reachable
from a *standalone* MCP server, which needs no in-tree plugin and therefore inherits no GPL
obligation at all. p130 searched for in-Moodle plugins and web-service plugins and missed the
standalone tier.

| agent | repo | licence | stars | last push | what it actually does |
|---|---|---|---|---|---|
| **moodle-mcp-server** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | 43 | 2026-02-22 | The permissive Moodle connector. Standalone MCP server over Moodle's web-service API. **Verified at pass 30 of this KB as the licence-boundary exemplar** — MIT while in-tree Moodle plugins are GPL-3.0 — and re-verified this pass by repo search (`license.spdx_id = MIT`). Two independent instruments agree. **Caveat:** last push 2026-02-22, the quietest row here, and it publishes no tags. |
| **ictexam-mcp** | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | 17 | 2026-09-07 | Exam authoring, delivery, gradebooks and item analysis as MCP tools, with **writes off by default**. A corporate holder (ICT Innovations) and an LTI path, which makes it the most procurement-friendly assessment connector on the shelf. |
| **moodle-mcp** (template) | [`1alexandrer/moodle-mcp`](https://github.com/1alexandrer/moodle-mcp) | **MIT** | 18 | 2026-04-21 | MCP server *template* for Moodle — the cleanest starting skeleton rather than a finished product. |
| **moodle-mcp** (dev-facing) | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | **MIT** | 8 | 2026-06-06 | Not learner-facing: gives an agent live access to moodledev.io docs, the Hooks API, capabilities, XMLDB and the Moodle Jira tracker. Pairs with `claude-moodle-dev` below for delivery velocity. |
| **mydy-lms-helper** | [`Deeptanshuu/mydy-lms-helper`](https://github.com/Deeptanshuu/mydy-lms-helper) | **MIT** | 7 | 2026-09-29 | APAC (D.Y. Patil, India). TUI **and** MCP server over a Moodle-based institutional LMS: attendance, courses, assignments, grades, materials. A worked example of a single-institution deployment. |

**Unlicensed Moodle connectors — do not build on these:** [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp)
(**no licence field**, 40★ — the second-largest by stars and unusable as published),
[`haanhtuandev/vgu-mcp`](https://github.com/haanhtuandev/vgu-mcp) (**none**, 10★, Go, Vietnamese-German
University) and [`ink-waffle/moodle-mcp`](https://github.com/ink-waffle/moodle-mcp) (**none**, 6★).
The pattern on this tier is consistent: **the permissive ones are not the most-starred ones.**

### Evaluation and benchmark layer — p130 called this "the largest hole on the shelf"

**It is not a hole. It exists, it has been in this KB since pass 4, and the real constraint is
narrower and worse: neither member carries a usable grant.**

| benchmark | repo | licence | stars | last push | origin | what it measures |
|---|---|---|---|---|---|---|
| **MathTutorBench** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🔴 **no licence field at all** | 43 | 2026-08-27 | **EMEA (ETH Zurich, Learning & Reasoning in Education)** | Open-ended **pedagogical** capability of LLM tutors — scaffolding, hint quality, not answer accuracy. **EMNLP 2025 oral.** The closest thing to a real tutoring benchmark in open source. 🔴 **Its README states two different licences in one file** (badge: CC-BY-4.0; body: CC-BY-SA-4.0) and no `LICENSE` payload resolves, so its terms are genuinely indeterminate. |
| **Tutoring Accuracy Dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) | 🔴 **bespoke "Evaluation Dataset License"** (NOASSERTION) | 57 | 2024-08-29 | North America (**Khan Academy**) | Dataset + paper *"LLM Based Math Tutoring: Challenges and Dataset"* — where LLM tutors go wrong on maths. Read in full by an earlier pass: a **2 690-byte custom licence**, not an OSI one. 🔴 **Dormant: last push 2024-08-29, ~2 years.** |

**What this means for an engagement, stated precisely:** you can *run* both against a candidate
tutor and *cite* the results, and you cannot ship either one's data inside a client deliverable
without reading those terms with counsel. The honest claim is **"the measurement layer exists and
is unshippable"**, not "it does not exist". The evaluation harness a client needs is still a build
— but it is a build that starts from two real benchmarks, not from nothing. See `compose/patterns.md` → P6.

### Academic-integrity / proctoring tier — permissive, and uniformly immature

This KB has carried a standing claim that the proctoring tier has **zero permissive rows**. That
claim is false. There are at least four MIT rows; the real finding is that **none of them is
institution-backed and none exceeds 18 stars**, against an EU high-risk class that binds
2027-12-02.

| repo | licence | stars | last push | what it is |
|---|---|---|---|---|
| [`RakeshBabuGajula/Exam_Intellect`](https://github.com/RakeshBabuGajula/Exam_Intellect) | **MIT** | 18 | 2026-10-05 | The largest permissive row. Live exam-observation dashboard: computer vision + speech recognition, real-time alerts, session tracking, automated feedback. Multi-agent. |
| [`VIJAYAPANDIANT/online-examination-system`](https://github.com/VIJAYAPANDIANT/online-examination-system) | **MIT** | 11 | 2026-08-19 | 🆕 Full exam platform with AI proctoring; React/Vite + Spring Boot, Dockerised, multi-language code execution. The most complete *platform* of the four. |
| [`singhrajvardhan/SecureExam-Platform`](https://github.com/singhrajvardhan/SecureExam-Platform) | **MIT** | 10 | 2026-04-17 | 🆕 PHP. Face tracking, tab-switch monitoring, auto-proctoring. |
| [`vishal017/cheatshield`](https://github.com/vishal017/cheatshield) | **MIT** | 8 | 2025-04-03 | 🆕 The most interesting *architecture* of the four — YOLOv5 object detection, MTCNN faces, **YAMNet audio**, PyQt5 shell. 🔴 **Stale: last push 2025-04-03, ~18 months.** |

🔴 **Read the EU constraint before proposing any of these.** Behavioural monitoring in education is
Annex III high-risk from **2027-12-02**, and anything that infers *emotion* in an education setting
is **prohibited outright and has been since 2025-02-02** (AI Act Art. 5). Three of the four rows
above do affect/behaviour-adjacent inference by construction. The permissive licence is the easy
part; the deployability check is `intel/policy-matrix.tsv`.

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

## Declared gaps — restated, because three of p130's four were refuted by this KB's own pages

🔴 **Two of p130's four declared gaps were not gaps.** They are struck through below with what
refutes them, because a false absence is more expensive than a missing row: it tells a studio there
is nothing to start from when there is.

- ~~**No education-specific agent-evaluation or learning-outcome benchmark** in open source. This is
  the largest hole on the shelf.~~ 🔴 **REFUTED.** `eth-lre/mathtutorbench` (43★, ETH Zurich, EMNLP
  2025 oral) has been in this KB **since pass 4**; `Khan/tutoring-accuracy-dataset` (57★) had its
  bespoke 2 690-byte licence read in full by an earlier pass. 🟢 **The surviving gap is narrower and
  sharper: the benchmark layer carries no usable grant** — one repo has no licence field, the other
  a custom non-OSI one. And neither measures *learning outcomes*; both measure tutor behaviour.
  **"No outcome benchmark" is defensible. "No benchmark" was not.**
- ~~**No Moodle MCP server with a clear permissive licence.**~~ 🔴 **REFUTED.**
  `peancor/moodle-mcp-server` is **MIT** with 43★ and was verified by this KB at **pass 30** as the
  licence-boundary exemplar; `ictexam-mcp`, `1alexandrer/moodle-mcp`, `SaadRahman01/moodle-mcp` and
  `mydy-lms-helper` are MIT too. 🟢 **The surviving gap is maturity and ownership, not licence:**
  the permissive Moodle connectors are individually owned, the largest has not been pushed since
  February 2026, and the most-starred one of all (`loyaniu/moodle-mcp`, 40★) has no licence at all.
- **No LATAM-origin education agent above 11 stars.** 🟢 **SURVIVES.** `alejooroncoy/campus-cli`
  (ISC, 11★, Peru) is still the only one, and it is one person's university tool. An informed gap,
  not an absence of demand — see `intel/market.md`.
- **No agent targeting a student information system** (enrolment, records, timetabling). 🟢
  **SURVIVES as an AGENT gap, but the PLATFORM claim behind it was wrong** — see
  `repos/foundations.md`, where p130's *"`openeducat_erp` and `academico` are the whole field"* is
  refuted by a system-of-record tier this KB had already read. Administrative automation, the
  most-cited adoption driver, still has no open-source **agent**. That is the largest genuine hole
  on this shelf now.
- 🆕 **No permissive proctoring project with an institutional owner.** Four MIT rows exist (above);
  the largest is 18★ and all four are individual projects. Against an Annex III high-risk class
  binding 2027-12-02, this is the tier an EMEA client will ask for and the shelf cannot supply at
  production grade.

## How a row gets onto this page (rule added by p131)

🔴 **Repo search is authoritative for METADATA and blind to PAYLOAD.** It returns
`license.spdx_id`, stars, `pushed_at` and the fork flag correctly. It cannot tell you what a
`LICENSE` file actually grants when GitHub's matcher reports `NOASSERTION` ("Other"), and it cannot
see an address that an earlier pass found with a different query.

**So, before declaring anything absent:** grep this KB's own append-only pages for the class first.
Three of p130's four declared gaps would have failed that grep in under a second. A full rewrite
that re-derives every page from one instrument discards everything the KB established with the
others.
