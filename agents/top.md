---
industry: education
region: Global
updated: 2026-10-21
---

# Education — AI agents worth building on

**Pass 356 · 2026-10-21.** Every row below was checked first-hand on two
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

## 🆕 Memory and scheduling agents — the layer that decides *when*, not *what*

🟢 **New tier, `p356`.** A `topic:spaced-repetition` leg returned **40 repositories**
and a coherent technical layer this base had measured and never shelved: agents whose
contribution is **scheduling the next review**, not generating content. The sector has
a de-facto standard — **FSRS**, the Free Spaced Repetition Scheduler — and it is MIT
at every rung, which makes it one of the cleanest things on this shelf to embed.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| Echo-Loop | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | **AGPL-3.0** | `main/LICENSE` | **4 222** | APAC | AI English listening/speaking trainer: intensive listening, shadowing, blind listening, retelling, spaced review. 🔴 Network copyleft |
| FSRS4Anki | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT (`LICENSE`) | `main/LICENSE` | **4 111** | Not placed | The FSRS scheduler as an Anki add-on. Its own topics name `intelligent-tutoring-system` |
| engram | [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | MIT (`LICENSE`) | `main/LICENSE` | **1 458** | Not placed | Free-recall verification *with receipts* + FSRS scheduling; ships as an agent plugin |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT (`LICENSE`) | `main/LICENSE` | **1 111** | APAC | AI study partner: plans the route, teaches, builds a project alongside the learner |
| trane | [trane-project/trane](https://github.com/trane-project/trane) | **AGPL-3.0** | `master/LICENSE` | **848** | Not placed | Deliberate-practice engine over a mastery dependency graph (Rust). 🔴 Network copyleft |
| FSRS (the algorithm) | [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | MIT (`LICENSE`) | `main/LICENSE` | **729** | Not placed | The DSR-model specification itself — the thing to implement against |
| human-skill-tree | [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 🟡 **AGPL-3.0 notice + MIT for `skills/`** | `master/LICENSE` | **575** | APAC | 30+ skills from K-12 to career, built on cognitive science. 🟡 Split grant — see the flags below |
| py-fsrs | [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | MIT (`LICENSE`) | `main/LICENSE` | **514** | Not placed | The embeddable Python scheduler. **This is the row to build on** |
| learn-anything | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | MIT (`LICENSE`) | `main/LICENSE` | **487** | Not placed | Recursive learning: Socratic deep-dives plus TDD-style exercises inside a coding assistant |
| learn-faster-kit | [hluaguo/learn-faster-kit](https://github.com/hluaguo/learn-faster-kit) | MIT (`LICENSE`) | `main/LICENSE` | **391** | Not placed | Learning coach: personalised syllabus, spaced repetition, progress tracking |

🔵 **Why this tier is worth more than its star counts.** Every tutoring agent on the
shelf above decides *what* to teach next and almost none decides *when* to return to
it. Retention is the outcome a client measures. [`py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
(MIT) is a few hundred lines with a published algorithm behind it, and it drops into an
existing tutor without touching its content pipeline — see `compose/patterns.md`
Pattern 10.

## 🆕 Item banks and rubric-bound grading

🟢 **New tier, `p356`,** from a `gradebook OR "question bank" OR "item bank"` leg. The
AI-native item bank — import a Word file or a photograph of a page, recognise the
formulae, match the knowledge point, generate the worked solution — is a real product
category and it is **almost entirely Chinese-language**.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| math-question-bank | [JudgePeach/math-question-bank](https://github.com/JudgePeach/math-question-bank) | **AGPL-3.0** | `main/LICENSE` | **330** | APAC | High-school maths item bank: live LaTeX rendering, LLM parsing and solving, formula OCR. 🔴 Network copyleft |
| MathCyclus (Lingxi) | [JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant](https://github.com/JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant) | 🔴 **no grant file — README prose only** | `main/` — none found | **147** | APAC | Streamlit + LaTeX item bank with OCR, TikZ rendering and automated paper assembly. 🔴 Not usable until a `LICENSE` exists |
| Grader-agent | [erictrainnlpinxihu/Grader-agent](https://github.com/erictrainnlpinxihu/Grader-agent) | MIT (`LICENSE`) | `main/LICENSE` | **101** | APAC | Five-stage grading loop (perceive→plan→act→observe→respond). **Write actions are not in the tool table — the agent can only emit proposals**, and each `GradingDraft` binds to a rubric line and a paragraph hash so a verdict is replayable |
| question-bank | [gygy-open/question-bank](https://github.com/gygy-open/question-bank) | **AGPL-3.0** | `main/LICENSE` | **73** | APAC | AI-native item bank: Word/Markdown/image import, knowledge-point matching, review workflow, desktop and Docker builds. 🔴 Network copyleft |

🟢 **[`Grader-agent`](https://github.com/erictrainnlpinxihu/Grader-agent) is the
architectural find, not the biggest one.** It is the only grading agent on this base
that makes the human-approval boundary **structural** rather than procedural: the four
write actions are absent from the tool table, so the model cannot take them even if it
decides to. That is precisely the posture the EU AI Act's high-risk regime asks for in
exam scoring, and it is MIT. 🔵 Its replay guarantee — rubric line plus paragraph hash
per draft — is also the audit trail `intel/trends.md` §1 says wins procurements.

## 🆕 Proctoring and exam integrity — read the warning before the table

🔴 **A large share of the proctoring supply is proctoring *evasion*.** The
`proctoring OR proctor` leg returned 30 repositories, and among the highest-starred
were [`Batlez/CloakBox`](https://github.com/Batlez/CloakBox) (408 ★, "make your virtual
machine invisible to proctoring software") and `SunnyCOdet/ofradr` (51 ★, "the ultimate
anti-proctoring software"). 🟢 **Neither is shelved and neither will be:** they are
detection-evasion tooling, not education software, and a studio has no use for them.
Recorded because the leg's apparent yield is roughly a third larger than its *usable*
yield, and a successor running the same leg will see the same thing.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| Proctoring-AI | [vardanagarwal/Proctoring-AI](https://github.com/vardanagarwal/Proctoring-AI) | MIT (`LICENSE`) | `master/LICENSE` | **633** | Not placed | Automatic monitoring: gaze and eye tracking, face spoofing, phone detection, speech-to-text |
| CBIT-AiExam-plus | [reneverland/CBIT-AiExam-plus](https://github.com/reneverland/CBIT-AiExam-plus) | 🔴 **NO GRANT — the README's MIT badge links to a `LICENSE` that 404s** | `main/` — none found | **277** | APAC | AI examination platform: item generation, adaptive difficulty, semantic scoring, analytics, proctoring. 🔴 **All rights reserved in practice** |
| exampro | [lebmatter/exampro](https://github.com/lebmatter/exampro) | 🟡 **MIT, unfilled template** (`license.txt`) | 🔴 `main/license.txt` | **72** | Not placed | Proctored exams for the Frappe framework — pairs with `frappe/lms` |
| edx-proctoring | [openedx/edx-proctoring](https://github.com/openedx/edx-proctoring) | **AGPL-3.0** | `master/LICENSE.txt` | **69** | North America | First-party Open edX proctoring subsystem |
| moodle quizaccess_proctoring | [eLearning-BS23/moodle-quizaccess_proctoring](https://github.com/eLearning-BS23/moodle-quizaccess_proctoring) | **AGPL-3.0** | `master/LICENSE.md` | **30** | APAC | Moodle quiz-access proctoring plugin (Brain Station 23) |

🔵 **The usable integrity story is not in this table.** Of five rows, one has no grant,
one has no identified licensor, and two are AGPL plugins to AGPL hosts. The row a
studio can actually ship on is [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
(MIT) on the shelf above — detect what the submission *is*, rather than surveil the
student taking it. That is a defensible recommendation and it is now evidence-backed.

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

**43 permissive rows** on this shelf — MIT, Apache-2.0, BSD, ECL-2.0 or NCSA, every
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
| `learn-anything` | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | **MIT** | `main/LICENSE` |
| `schoolinfo-mcp` | [chrisryugj/schoolinfo-mcp](https://github.com/chrisryugj/schoolinfo-mcp) | **MIT** | `main/LICENSE` |
| `knowledge-import-pipeline` | [clownjee/knowledge-import-pipeline](https://github.com/clownjee/knowledge-import-pipeline) | **Apache-2.0** | `main/LICENSE` |
| `dolos` | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | `main/LICENSE` |
| `Understand-Anything` | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | **MIT** | `main/LICENSE` |
| `Grader-agent` | [erictrainnlpinxihu/Grader-agent](https://github.com/erictrainnlpinxihu/Grader-agent) | **MIT** | `main/LICENSE` |
| `moodle-mcp` | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | **MIT** | `main/LICENSE` |
| `DeepTutor` | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | `main/LICENSE` |
| `learn-faster-kit` | [hluaguo/learn-faster-kit](https://github.com/hluaguo/learn-faster-kit) | **MIT** | `main/LICENSE` |
| `Smart-Study-Agent` | [HumphreySun98/Smart-Study-Agent](https://github.com/HumphreySun98/Smart-Study-Agent) | **MIT** | `main/LICENSE` |
| `yanki` | [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | **MIT** | `main/package.json` |
| `agent-skills` | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | **Apache-2.0** | `main/LICENSE` |
| `evaluators` | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **MIT** | `main/LICENSE.md` |
| `Bloom` | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | **MIT** | `main/LICENSE` |
| `canvas-lms-agent` | [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | **MIT** | `master/canvas-lms-mcp/LICENSE` |
| `Ares2` | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | **MIT** | `main/LICENSE` |
| `mcp-brasil` | [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) | **MIT** | `main/LICENSE` |
| `Study-Mate` | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | **MIT** | `main/LICENSE` |
| `engram` | [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | **MIT** | `main/LICENSE` |
| `free-spaced-repetition-scheduler` | [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | **MIT** | `main/LICENSE` |
| `fsrs4anki` | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | `main/LICENSE` |
| `py-fsrs` | [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | **MIT** | `main/LICENSE` |
| `OpenStudy` | [OpenStudy-dev/OpenStudy](https://github.com/OpenStudy-dev/OpenStudy) | **MIT** | `main/LICENSE` |
| `pykt-toolkit` | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `main/LICENSE` |
| `canvas-ed-mcp` | [r1ckyIn/canvas-ed-mcp](https://github.com/r1ckyIn/canvas-ed-mcp) | **MIT** | `main/LICENSE` |
| `learn-anything-with-AI` | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | **MIT** | `main/LICENSE` |
| `brightspace-mcp-server` | [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** | `main/LICENSE` |
| `classroom-mcp` | [sandraschi/classroom-mcp](https://github.com/sandraschi/classroom-mcp) | **MIT** | `master/LICENSE` |
| `educhain` | [satvik314/educhain](https://github.com/satvik314/educhain) | **MIT** | `main/LICENSE` |
| `Skill-Anything` | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | **MIT** | `main/LICENSE` |
| `Proctoring-AI` | [vardanagarwal/Proctoring-AI](https://github.com/vardanagarwal/Proctoring-AI) | **MIT** | `master/LICENSE` |
| `book-to-skill` | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **MIT** | `master/LICENSE.md` |
| `canvas-mcp` | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | `main/LICENSE` |
| `pyedmine` | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | **MIT** | `main/LICENSE` |

---

## 🔴 Licence flags — rows a Globant engagement cannot treat as permissive

🟢 **`p356` adds five, and one of them is a RECOVERY rather than a warning.** Each was
caught by reading the payload rather than the classifier, the badge or the README. 🔵 Note
what the new rows have in common with the old ones: **three of the five would read as MIT
to anyone who did not open the file**, and the two that do not read as MIT are the two
that turned out to be usable.

| Row | What it looks like | What the payload says | Consequence |
|---|---|---|---|
| [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | an open AI student-advising app, 340 ★ | 🔴 **Elastic License 2.0** | **Source-available, not OSI open source.** Cannot be offered as a managed/hosted service. Excluded from the tables above for this reason |
| [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | GitHub shows `NOASSERTION`, 1 704 ★ | 🔴 **CC-BY-NC-4.0** | NonCommercial. The single best Chinese K-12 curriculum graph found this pass, and it is **unusable in paid work** |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | "the data layer for educational AI" | 🟡 **MIT code, per-dataset data** | Some datasets are **Gated** and under no open licence. A build that assumes the repo licence covers the data is wrong |
| [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | a learning-analytics standard on GitHub | 🔴 **IMS Global specification document licence** | A *spec* licence, not a software grant. Implement the standard; do not vendor the document |
| [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | MIT, per the file in the tree | 🟡 **MIT at `canvas-lms-mcp/LICENSE`** | The grant licenses the **package**, not the repository. The root is unlicensed |
| [kitschpatrol/yanki](https://github.com/kitschpatrol/yanki) | MIT, per GitHub | 🟡 **MIT declared only in `package.json`** | No `LICENSE` file exists in the tree. The grant is a manifest field |
| 🆕 [reneverland/CBIT-AiExam-plus](https://github.com/reneverland/CBIT-AiExam-plus) | an MIT shields.io badge at the top of the README, 277 ★ | 🔴 **no grant anywhere** — the badge links to `LICENSE`, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` and `docs/LICENSE` **all 404** | **All rights reserved.** A badge is a picture, not a grant. The most capable AI exam platform found this pass and it cannot be used |
| 🆕 [JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant](https://github.com/JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant) | nothing on the landing page, 147 ★ | 🔴 **one Chinese prose sentence in `README.md`**: 本项目采用 MIT License 开源协议 | A README claim is a **pointer**, not a grant. Ask the author for a `LICENSE` file; until then, unusable |
| 🆕 [lebmatter/exampro](https://github.com/lebmatter/exampro) | MIT, per GitHub | 🟡 **stock MIT at `main/license.txt` with the holder fields never filled**: `Copyright (c) [year] [fullname]` | Family certain, **licensor absent**. Two hazards in one row: the lower-case path (the `frappe/lms` shape) and nobody to attribute |
| 🆕 [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | AGPL-3.0, per GitHub, 575 ★ | 🟡 **a 1 134-byte AGPL-3.0 *short-form notice*** — not the 34 kB text — **plus a dual-licensing note: `skills/*.md` may be used under AGPL-3.0 OR MIT at the user's option** | 🟢 **Split along a directory boundary.** The code is network copyleft; the 30+ curriculum `SKILL.md` files are MIT-usable in a closed deliverable. 🔴 And note the size: an AGPL notice that is MIT-sized defeats any byte-band heuristic |
| 🆕 [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GitHub shows no licence; the README says only *"the GNU General Public License"*, 346 ★ | 🟢 **GPL-2.0 recovered** — 17 286 B, BOM-prefixed, at `master/docs/License.txt`, after six root rungs all 404 | 🟢 **Usable, and the version matters:** GPL-**2**.0, not 3.0, so GPL-3.0 compatibility cannot be assumed. `p354` predicted this exact `docs/License.txt` shape |

## 🔴 One carried row is off-domain and should not be on an education shelf

[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)
is live and genuinely MIT (`LICENSE`, holders Yuxiang Lin / Infinite Universe, Inc.),
and at ~87 k ★ it is the largest address this base has carried on this shelf. Read
first-hand this pass, it is **a plugin for AI coding tools that maps a codebase or
document set into an interactive graph** — a developer comprehension tool. It is not
an education agent, and its star count has been inflating this shelf's apparent
education supply. Recorded here as a correction rather than deleted silently.

## 🟢 What changed on `p356` — nine legs aimed at FUNCTIONS, and three new tiers

`p355` established that a **topic intersection** is a channel where a prose phrase is
not, and registered `ACTION ZZ-ay`: run the legs by **function** — `autograder`,
`online judge`, `lecture capture`, `curriculum ontology`, `LTI`, `SIS`, `proctoring`,
`spaced repetition`, `rubric` — with the falsifier *"five such legs returning nothing
would refute T40"*.

🟢 **Not one leg refuted it. Seven of the nine returned, and they returned a sector.**
**36 repositories verified first-hand, 36 alive, 33 grants read from the payload** —
and the split that matters is this:

| Class | Rows |
|---|---:|
| 🟢 **absent from this base's entire corpus** (`archive/` and `evidence/` included) | **18** |
| 🔴 **measured by this base before and on NO live shelf** | **18** |
| already shelved | **0** |

🔴 **Read the second row as the more serious finding.** Half of what the function legs
found, this base had already measured and then lost — [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) appears in **237
files** of this corpus and on **no live shelf**; `Study-Mate` in 187,
`human-skill-tree` in 174, `otter-grader` in 141. 🔵 The `delivery-audit` target exists
for exactly this question (*"which rows did `evidence/` measure that no shelf ever
offered?"*) and **it is in no gate target**, so nothing has ever answered it on a
schedule. Registered as `ACTION ZZ-az`.

🔵 **And the two legs that failed, failed on their own syntax.** The `lecture capture`
and `curriculum ontology` legs returned **37 325** and **880** results headed by
`openclaw`, `n8n` and `firecrawl` — an unparenthesised `OR` in an index query binds
loosely and dissolves the leg. 🟢 **That is a query defect, not an absence**, and it is
recorded as such rather than published as a gap: `p351` declared a gap against an open
channel, and this is the same mistake one layer up.

## 🔵 What changed on `p355`, and why the "no new agents" streak was an artefact

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

🟢 **Counted over this shelf's own region cells as the last act before the commit**, not
over an inherited sentence — which is `gate-census-currency`'s discipline applied to a
distribution rather than to an address count:

| Region | Placed rows on this shelf |
|---|---:|
| **APAC** | **21** |
| EMEA | 6 |
| North America | 6 |
| **LATAM** | **2** |
| 🔵 Not placed | 27 |

- **APAC** is now the densest region on this shelf by a wide margin — **21 rows**, up
  from 11 one pass ago. China, Hong Kong, India, Korea, Bangladesh and Iran all have
  first-party education software, and the eight rows added this pass are *infrastructure*
  (item banks, judges, graders), not demos.
- **EMEA** holds 6, concentrated in university assessment tooling (Belgium ×2, Germany,
  Italy, Spain, UK), and gains Iran and Portugal on `repos/foundations.md`.
- **North America** holds 6, concentrated in the standards/skills/evaluator layer.
  🔴 **A correction while deriving this:** the sentence this replaces claimed **6** NA
  rows while the tables underneath it carried **5**. `p356` adds `edx-proctoring`, so
  the published figure is now 6 *and true*; it was off by one before. Nothing binds a
  **distribution** stated in prose, which is `ACTION ZZ-aw`'s shape on a third quantity.
- **LATAM** places **2** rows — `mcp-brasil` and `bncc-dados`, both Brazil, both MIT.
  🔴 **This pass ran the LATAM leg a new way and it still returned nothing shelvable,
  but the mechanism is now named.** Rather than prose ("agente educativo"), the leg used
  **function words** — `calificación`, `corrección`, `banco de preguntas`, `banco de
  questões`, `examen`. It returned **228 209 results and zero education tooling**: the
  Spanish and Portuguese hits are **exam-content archives** — FAMAF/UNC (Argentina),
  Instituto Tecnológico de Costa Rica, `111milprogramadores` — students sharing past
  papers, not software.
  🟢 **So the LATAM gap is specifically a TOOLING gap, and that is a more useful finding
  than "nothing found".** Spanish-language assessment *content* exists in volume; what
  does not exist is a Spanish-language item bank, autograder or judge. For the item-bank
  tier above, that is an input a build can use and a product gap a build can fill.
  🔵 Licences on those corpora were **not** verified this pass and must be before use.
