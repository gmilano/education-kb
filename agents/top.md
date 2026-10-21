---
industry: education
region: Global
updated: 2026-10-21
---

# Education — AI agents worth building on

**Pass 355 · 2026-10-21.** Every row below was checked first-hand this pass on two
channels: liveness and default branch via `git ls-remote --symref`, and the licence
**read from the payload** at `raw.githubusercontent.com` — never from a badge, a
README claim or GitHub's own classifier. Where the classifier disagreed with the
payload, the payload wins and the disagreement is recorded.

**Channel state this pass:** 🟢 `git ls-remote` OPEN · 🟢 `raw.githubusercontent.com`
OPEN · 🟢 authenticated search index OPEN · 🔴 `github.com` HTML **403** ·
🔴 `api.github.com/repos/*` **403**.

**★ discipline.** A star figure appears only where it was re-derived from the
authenticated index **this pass**. Rows reading `not re-derived` are live and
licence-verified, but their star count was not measured today — the row is
publishable, the number is not.

---

## Tutoring and learning agents

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **41 938** | APAC | Agent-native tutoring with lifelong memory. Published by HKU Data Science lab (Hong Kong) |
| book-to-skill | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | MIT (`LICENSE.md`) | `master/LICENSE.md` | **35 503** | Not placed | Turns a technical book PDF into a Claude Code skill — ready to study, reference and use |
| PageLM | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | MIT (`LICENSE.md`) | `main/LICENSE.md` | **2 035** | Not placed | Community NotebookLM: course material → quizzes, flashcards, study guides. 🟡 GitHub classifies this `NOASSERTION`; the payload is stock MIT |
| get-it | [beltromatti/get-it](https://github.com/beltromatti/get-it) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **1 124** | EMEA | "Read it. See it. Get it." multimodal explainer, built at GDG AI Hack Milan 2026 (Italy) |
| education-agent-skills | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **CC-BY-SA-4.0** (`LICENSE`) | `main/LICENSE` | **885** | EMEA | 165 evidence-grounded skills for teachers, school leaders and EdTech builders (UK). 🟡 Content licence, share-alike — not a code grant |
| educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT (`LICENSE`) | `main/LICENSE` | **387** | APAC | Course generation from source material incl. YouTube → structured course (India) |
| frametell | [sitor-ai/frametell](https://github.com/sitor-ai/frametell) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **356** | Not placed | Idea or source material → explainer video, driven by an AI director agent |
| Skill-Anything | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT (`LICENSE`) | `main/LICENSE` | **339** | APAC | Any source (PDF, video, web, audio, text) → interactive learning package with quizzes and flashcards |
| claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT (`LICENSE`) | `main/LICENSE` | **338** | Not placed | Open alternative to Udemy/Coursera: give it a topic, it researches and builds the course |
| ai-shifu | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 (`LICENSE.txt`) | `main/LICENSE.txt` | **327** | APAC | AI-led teaching and Q&A driven by typing; Chinese-language project |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT (`LICENSE`) | `main/LICENSE` | **290** | APAC | Private AI tutor that reads how a learner actually learns and sequences the next lesson |
| deep-student | [helixnow/deep-student](https://github.com/helixnow/deep-student) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **286** | Not placed | Local-first open AI learning workbench |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT (`LICENSE`) | `main/LICENSE` | **268** | North America | Open intelligent tutoring system with Bayesian Knowledge Tracing mastery. UC Berkeley CAHLR |
| learn-anything-with-AI | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | MIT (`LICENSE`) | `main/LICENSE` | **201** | Not placed | Reusable AI learning skill for project-driven mastery of a subject |
| freelingo | [artcc/freelingo](https://github.com/artcc/freelingo) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **192** | EMEA | Self-hosted AI language learning with local or cloud LLMs, CEFR-aligned (Spain) |
| Smart-Study-Agent | [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | MIT (`LICENSE`) | `main/LICENSE` | **57** | Not placed | RL picks the study action, FSRS picks the timing — spaced repetition as a policy problem |

## LMS-connected agents (the MCP layer)

This tier barely existed two cycles ago. It is now the densest supply in education
AI: every major LMS has at least one community MCP server, which means an engagement
can reach a client's existing LMS without building a connector.

### Agents over the systems

**11 rows in the table below** carry an MCP server in the slug itself, and
across them **5 platforms** are reachable without writing a connector.
🔵 The count is scoped deliberately: it is the rows of *this table*, not every MCP
address this shelf mentions — a bare count cannot be checked, because several
defensible scopes give different answers. The whole-file figure is on
`intel/trends.md` §7 and the full cross-shelf census is in the `recount` gate.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | Target system |
| --- | --- | --- | --- | ---: | --- | --- |
| OpenStudy | [OpenStudy-dev/OpenStudy](https://github.com/OpenStudy-dev/OpenStudy) | MIT (`LICENSE`) | `main/LICENSE` | **76** | Not placed | Self-hostable study dashboard with a built-in MCP server |
| brightspace-mcp-server | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | MIT (`LICENSE`) | `main/LICENSE` | **59** | Not placed | D2L Brightspace — grades, due dates, assignments, rosters |
| schoolinfo-mcp | [chrisryugj/schoolinfo-mcp](https://github.com/chrisryugj/schoolinfo-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **48** | APAC | Korea's 학교알리미 school-disclosure OpenAPI + CLI (meals, enrolment, assessment plans) |
| canvas-ed-mcp | [r1ckyIn/canvas-ed-mcp](https://github.com/r1ckyIn/canvas-ed-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **18** | Not placed | Canvas LMS + Ed Discussion |
| ku-portal-mcp | [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **12** | APAC | Korea University KUPID portal + Canvas (notices, schedules, library) |
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | Not placed | Canvas LMS |
| moodle-mcp | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | Not placed | Moodle |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | Not placed | Tutor (Open edX distribution) |
| openedx-mcp | [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | **AGPL-3.0** (`LICENSE`, branch `master`) | `master/LICENSE` | not re-derived | Not placed | Open edX. 🔴 Copyleft — the only non-permissive row on this tier |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | Not placed | Anki spaced repetition |
| classroom-mcp | [sandraschi/classroom-mcp](https://github.com/sandraschi/classroom-mcp) | MIT (`LICENSE`, branch `master`) | `master/LICENSE` | not re-derived | Not placed | Google Classroom |
| canvas-lms-agent | [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | MIT **at depth** — `canvas-lms-mcp/LICENSE` | `master/canvas-lms-mcp/LICENSE` | not re-derived | Not placed | Canvas. 🔴 Repository **root carries no grant**; the MIT text licenses the `canvas-lms-mcp` package, not the repository |
| mcp-brasil | [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | **LATAM** | Brazilian public-data MCP; education datasets among them |

## Assessment, integrity and learning analytics

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| Dolos | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT (`LICENSE`) | `main/LICENSE` | **353** | EMEA | Source-code plagiarism detection for programming assignments. Ghent University, Belgium |
| INGInious | [INGInious/INGInious](https://github.com/INGInious/INGInious) | **AGPL-3.0 — "most of the files"** (`LICENSE`) | `main/LICENSE` | **243** | EMEA | Secure automated exercise assessment. UCLouvain, Belgium. 🟡 The grant text itself scopes to *most* files — treat as mixed |
| pyedmine | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT (`LICENSE`) | `main/LICENSE` | **82** | APAC | Educational data mining framework (knowledge tracing, exercise recommendation) |
| Ares2 | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | EMEA | Automated grading / secure test execution. TU Munich chair of applied software engineering |
| pykt-toolkit | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (`LICENSE`) | `main/LICENSE` | not re-derived | APAC | Knowledge-tracing benchmark and model library |
| k12-teacher-skills | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | not re-derived | North America | K-12 teacher skill pack |
| agent-skills | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | not re-derived | North America | Education agent skills from Learning Commons |
| evaluators | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **MIT for code**, stated in `LICENSE.md` prose | `main/LICENSE.md` | not re-derived | North America | Evaluators for educational AI output. 🟡 Split grant — the file is a licensing *statement*, not a stock licence |

## Curriculum and knowledge layers (what the agents reason over)

An agent is only as good as the curriculum model behind it. These are the data
assets — and they are where the licence traps live.

| Asset | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | Substance |
| --- | --- | --- | --- | ---: | --- | --- |
| os-taxonomy | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | **ODbL-1.0** (`LICENSE`) | `main/LICENSE` | **6 752** | Not placed | Open subject/skills taxonomy. Share-alike binds a derivative *database*, not a produced work |
| cn-math-taxonomy | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC-BY-NC-4.0 — NonCommercial** (`LICENSE`) | `main/LICENSE` | **1 704** | APAC | China K-12 maths + English knowledge graph, 人教版/课标-aligned: 1 244 nodes, 5 123 items, adaptive diagnosis. 🔴 **Not usable in a paid client engagement** |
| knowledge-graph | [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | **MIT code / data is per-dataset** (`LICENSE.md`) | `main/LICENSE.md` | **161** | North America | Instructional-content + research data layer. 🔴 Datasets are labelled Open, Open+Gated or **Gated**; Gated content is **not** under CC BY 4.0 or CC0. Check the licence per download |
| bncc-dados | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | MIT (`LICENSE`) | `main/LICENSE` | **22** | **LATAM** | Brazil's BNCC national curriculum as verified open data: 1 721 learning objectives in JSON, SQLite and CSV |
| knowledge-import-pipeline | [clownjee/knowledge-import-pipeline](https://github.com/clownjee/knowledge-import-pipeline) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **18** | APAC | China compulsory-education textbook → AI knowledge extraction, interactive KG, vector retrieval, prerequisite graph, MCP query service |
| polymath | [aclascollege/polymath](https://github.com/aclascollege/polymath) | **ODbL-1.0** (database) + **CC-BY-SA-4.0** (authored text) | `main/LICENSE` | absent from default index | APAC | Curriculum taxonomy: disciplines, courses, prerequisites, degrees, skills, careers. Placed APAC by commit stream (+08:00) |

---

## Build-on-this tier

**34 permissive rows** on this shelf — MIT, Apache-2.0, BSD, ECL-2.0 or NCSA, every
grant read from the payload at the path given. These are the rows a Globant engagement
can fork, embed and ship inside a closed client deliverable with no copyleft reach.
🔵 The tier is bounded structurally by this heading, so correcting the number cannot
delete the boundary that checks it.

| Row | Repo | Licence (payload) | Grant read at |
|---|---|---|---|
| `ai-shifu` | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | **Apache-2.0** | `main/LICENSE.txt` |
| `anki-mcp-server` | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | **MIT** | `main/LICENSE` |
| `k12-teacher-skills` | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** | `main/LICENSE` |
| `tutor-mcp` | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | `main/LICENSE` |
| `claudemy` | [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** | `main/LICENSE` |
| `get-it` | [beltromatti/get-it](https://github.com/beltromatti/get-it) | **Apache-2.0** | `main/LICENSE` |
| `bncc-dados` | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | **MIT** | `main/LICENSE` |
| `OATutor` | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | **MIT** | `main/LICENSE` |
| `PageLM` | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **MIT** | `main/LICENSE.md` |
| `schoolinfo-mcp` | [chrisryugj/schoolinfo-mcp](https://github.com/chrisryugj/schoolinfo-mcp) | **MIT** | `main/LICENSE` |
| `knowledge-import-pipeline` | [clownjee/knowledge-import-pipeline](https://github.com/clownjee/knowledge-import-pipeline) | **Apache-2.0** | `main/LICENSE` |
| `dolos` | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | `main/LICENSE` |
| `Understand-Anything` | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | **MIT** | `main/LICENSE` |
| `moodle-mcp` | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | **MIT** | `main/LICENSE` |
| `DeepTutor` | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | `main/LICENSE` |
| `Smart-Study-Agent` | [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | **MIT** | `main/LICENSE` |
| `yanki` | [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | **MIT** | `main/package.json` |
| `agent-skills` | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | **Apache-2.0** | `main/LICENSE` |
| `evaluators` | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **MIT** | `main/LICENSE.md` |
| `Bloom` | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | **MIT** | `main/LICENSE` |
| `canvas-lms-agent` | [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | **MIT** | `master/canvas-lms-mcp/LICENSE` |
| `Ares2` | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | **MIT** | `main/LICENSE` |
| `mcp-brasil` | [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) | **MIT** | `main/LICENSE` |
| `OpenStudy` | [OpenStudy-dev/OpenStudy](https://github.com/OpenStudy-dev/OpenStudy) | **MIT** | `main/LICENSE` |
| `pykt-toolkit` | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `main/LICENSE` |
| `canvas-ed-mcp` | [r1ckyIn/canvas-ed-mcp](https://github.com/r1ckyIn/canvas-ed-mcp) | **MIT** | `main/LICENSE` |
| `learn-anything-with-AI` | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | **MIT** | `main/LICENSE` |
| `brightspace-mcp-server` | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** | `main/LICENSE` |
| `classroom-mcp` | [sandraschi/classroom-mcp](https://github.com/sandraschi/classroom-mcp) | **MIT** | `master/LICENSE` |
| `educhain` | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** | `main/LICENSE` |
| `Skill-Anything` | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | **MIT** | `main/LICENSE` |
| `book-to-skill` | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **MIT** | `master/LICENSE.md` |
| `canvas-mcp` | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | `main/LICENSE` |
| `pyedmine` | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | **MIT** | `main/LICENSE` |

---

## 🔴 Licence flags — rows a Globant engagement cannot treat as permissive

Four of this pass's findings are grants that a casual read would get wrong. Each was
caught by reading the payload rather than the classifier or the README.

| Row | What it looks like | What the payload says | Consequence |
|---|---|---|---|
| [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | an open AI student-advising app, 340 ★ | 🔴 **Elastic License 2.0** | **Source-available, not OSI open source.** Cannot be offered as a managed/hosted service. Excluded from the tables above for this reason |
| [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | GitHub shows `NOASSERTION`, 1 704 ★ | 🔴 **CC-BY-NC-4.0** | NonCommercial. The single best Chinese K-12 curriculum graph found this pass, and it is **unusable in paid work** |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | "the data layer for educational AI" | 🟡 **MIT code, per-dataset data** | Some datasets are **Gated** and under no open licence. A build that assumes the repo licence covers the data is wrong |
| [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | a learning-analytics standard on GitHub | 🔴 **IMS Global specification document licence** | A *spec* licence, not a software grant. Implement the standard; do not vendor the document |
| [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | MIT, per the file in the tree | 🟡 **MIT at `canvas-lms-mcp/LICENSE`** | The grant licenses the **package**, not the repository. The root is unlicensed |
| [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | MIT, per GitHub | 🟡 **MIT declared only in `package.json`** | No `LICENSE` file exists in the tree. The grant is a manifest field |

## 🔴 One carried row is off-domain and should not be on an education shelf

[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)
is live and genuinely MIT (`LICENSE`, holders Yuxiang Lin / Infinite Universe, Inc.),
and at ~87 k ★ it is the largest address this base has carried on this shelf. Read
first-hand this pass, it is **a plugin for AI coding tools that maps a codebase or
document set into an interactive graph** — a developer comprehension tool. It is not
an education agent, and its star count has been inflating this shelf's apparent
education supply. Recorded here as a correction rather than deleted silently.

## 🟢 What changed this pass, and why the "no new agents" streak was an artefact

Passes 343–354 reported **twelve consecutive windows with no new agent row**, and
`p354` published a denominator to justify it. That streak was a property of the
**query**, not of the supply. Those legs asked prose questions ("AI education
agents", "top open source AI agents education") and got listicles back.

This pass changed channel and asked the authenticated index for **topic
intersections** instead:

| Leg | Returned | New rows promoted |
|---|---:|---:|
| `topic:education topic:llm stars:>200` | 10 | **6** |
| `topic:edtech stars:>80` | 33 | **9** |
| `topic:education topic:mcp` | 328 | **7** |
| `topic:lti stars:>40` | 14 | **4** |
| `educación/educativo/escola/aprendizaje` + agente | 10 | **0** — see the regional note below |

**26 new rows on one pass**, against zero across the previous twelve. The lesson is
recorded for successors: on this base, a **topic intersection is a channel and a
prose phrase is not**. Prose legs return commercial listicles; `topic:` legs return
repositories.

## 🔵 Regional honesty

Placement here is by evidence — an institution domain, a national curriculum the repo
targets, the language of its own documentation, or a commit-stream timezone — never
by guessing from a name.

- **APAC** is the densest region on this shelf (11 placed rows): China, Hong Kong,
  India and Korea all have first-party education agents.
- **EMEA** places 6 rows, concentrated in university assessment tooling (Belgium ×2,
  Germany, Italy, Spain, UK).
- **North America** places 6, concentrated in the standards/skills/evaluator layer.
- **LATAM** places **2** rows — `mcp-brasil` and `bncc-dados`, both Brazil, both MIT.
  The Spanish/Portuguese-language discovery leg run this pass returned **10
  repositories and promoted none**: the hits were general-purpose agents (a personal
  OS, an email agent, a WhatsApp book recommender, a pentest tool), not education.
  🔴 **This is a real supply gap, not a search failure** — and it is stated here
  rather than left as apparent coverage. Brazil has first-party curriculum data;
  Spanish-speaking LATAM has, on this evidence, essentially none.
