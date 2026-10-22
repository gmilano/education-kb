---
industry: education
region: Global
updated: 2026-10-22
---

# Top education AI agents

**Pass `p383` · 2026-10-22 · FULL REWRITE.** Every row below was verified first-hand on this date
(see *Verification method*). The previous version of this file is kept at
[`archive/2026-10-22-p383-pre-rewrite/agents-top.md`](../archive/2026-10-22-p383-pre-rewrite/agents-top.md).

> **Why this file was rewritten.** Passes `p3xx` had turned this shelf into a journal about the
> knowledge base's own measurement apparatus — licence-reading instruments, channel-yield rates,
> pre-registered predictions — with a carried table of sub-1k-star hobby repositories. A studio
> opening a client engagement could not read a usable agent shortlist out of it. This pass restores
> the shelf to what it is for: **real agents, real licences, real descriptions, placed by region.**
> The one genuinely reusable result of that apparatus — that a repository's licence badge does not
> tell you what its payload grants — survives as `Pattern L` in
> [`compose/patterns.md`](../compose/patterns.md), as a procurement gate rather than a narrative.

**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p383.tsv) — 62 addresses,
58 live, 4 dead, every licence read from the raw payload at the repository's **real default ref**.

🆕 **Pass `p386` · 2026-10-22 — increment, and it overturns a recommendation on this shelf.** This pass
went straight at the two platforms the *Supply census* below called empty: **Blackboard — "nine servers and
not one verified grant"** — and **D2L — "six and the only one checked is ungranted."** Twenty-two addresses
were probed first-hand. **Both claims are now false: 6 MIT grants on Blackboard and 6 on D2L**, read from
the payload at each repository's real default ref.
**Evidence:** [`verified-repos`](../evidence/verified-repos.2026-10-22-p386.tsv) — 22 probes, 19 live-granted,
2 ungranted, 2 dead.
🔵 **But the gap did not disappear — it moved**, and the new shape is the finding. See
*[The Blackboard and D2L supply, measured](#the-blackboard-and-d2l-supply-measured)*.

## 🔴 No star counts are published this pass, and that is deliberate

Every popularity channel was closed in this sandbox: `api.github.com` → **403**,
`github.com` HTML → **403**, `img.shields.io/github/stars` → blocked, `api.star-history.com` →
blocked. The technology cycle (`v76`) had to publish a correction that earlier cycles' star counts
were **pipeline-inflated** across several industries. Carrying forward unverifiable numbers would
repeat exactly that error, so this shelf ranks by **what a studio can act on** — licence
permissiveness, maintenance signal and fit — and states the gap instead of filling it.

## Tier 1 — Tutoring and instruction agents

| agent | repo | default ref | licence | what it actually does | origin |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `main` | 🟢 **Apache-2.0** | Lifelong personalised tutoring: persistent learner memory plus RAG grounded in the learner's own uploaded materials. The most substantial permissive tutor in the open-source supply. | APAC — HKU Data Intelligence Lab, Hong Kong |
| **ai-shifu** | [AI-Shifu/ai-shifu](https://github.com/AI-Shifu/ai-shifu) | `main` | 🟢 **Apache-2.0** *(grant at `LICENSE.txt`, not `LICENSE`)* | AI-led chat-based course delivery — the agent drives the lesson script rather than waiting to be asked. | APAC — China |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | `main` | 🟢 **MIT** | Content generation for instructors: quizzes, lesson plans, question banks, YouTube-to-course. Teacher-facing, which is where the fastest-growing region's market actually is. | APAC — India |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | `main` | 🟢 **MIT** | AI-native LMS with an AI Mentor and role-play scenarios built in rather than bolted on. | EMEA — Selleo, Poland |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `main` | 🟢 **BSD-3-Clause** | Self-hostable tutoring platform with local RAG over textbooks and notes — the data-residency option. | not verified this pass |
| **tutor-gpt** | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | `main` | 🟡 **GPL-3.0** | Theory-of-Mind tutoring: models the learner's mental state to pitch the explanation, rather than retrieving a better paragraph. Pedagogically the most interesting approach here. | North America |
| **ChatTutor** | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | `main` | 🔴 **AGPL-3.0** | Visual, interactive tutor. Network copyleft — hosting it as a service triggers source obligations. | APAC |
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 🔴 **`dev`** | 🔴 **AGPL-3.0** | AI-native course platform. Note the default ref is `dev`: a `main`-assuming clone or licence read fails silently. | EMEA |
| **Learn Shell** | [sf-shenfeng/learn-shell](https://github.com/sf-shenfeng/learn-shell) | `main` | 🔴 **AGPL-3.0** at `main` — 🟢 **MIT at tag `v0.1.0`** | 🆕 `p385`. **Agent-native teaching OS: the classroom is the server and the agent is bring-your-own.** Courses, lessons, FSRS-scheduled flashcards, graded exercises, mindmap, document reader, and a memory layer the agent reads back (`get_context` / `get_learner_brief`) instead of re-deriving the learner each session. ~50 tools over MCP, self-describing via a `manifest://capabilities` resource. 🔴 v1 is explicitly **single-machine and unauthenticated** — not multi-tenant as it stands. | APAC — China (MCP tool descriptions and prep-report are Chinese-first; docs English-first) |
| **OpenTutor** | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | `main` | 🟢 **MIT** *(1,068 B, © 2026 Zijin Zhang)* | 🆕 `p386`. **Block-based adaptive workspace that runs entirely on the client's own machine.** Course material in (PDF), structured notes, flashcards, quizzes and an adapting tutor out; **FSRS** spaced repetition, a knowledge graph and cognitive-load detection are in the product rather than on the roadmap. Next.js 16 + Python 3.11, Docker, **runs on local open-weight models with no API key and no data leaving the host**. 🟢 The data-residency tutor with a *permissive* grant — which [Open TutorAI CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3) was the only other candidate for. 🟡 One maintainer; bilingual EN / zh-CN. | APAC — China |

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
| **pybryt** | [microsoft/pybryt](https://github.com/microsoft/pybryt) | `main` | 🟢 **MIT** | Assesses the **approach** a student's code takes, not only its output. Pairs with an LLM that explains *why* the approach was wrong. |
| **canvas-mcp** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | MCP server over Canvas LMS: courses, assignments, submissions, grading, rubrics, students. Fork [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) (MIT) adds office-hours, syllabus read/write and course-content copy. |
| **Flat** | [netless-io/flat](https://github.com/netless-io/flat) | `main` | 🟢 **MIT** | Open-source online classroom (interactive whiteboard, recording) — the live-session substrate an agent can sit in. |

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

## Build-on-this tier

The permissive shortlist: every agent on these shelves a studio can build on and still hand a
client closed, client-owned code. 🆕 `p386`: **19 permissive rows** — MIT, Apache-2.0 or BSD-3 only, no
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
🆕 `p386`: **6 LMS platforms** are reachable through the servers below — Blackboard joins the table
this pass, with a verified grant for the first time.

### Agents over the systems

**23 rows in the table below**, every one resolved and licence-read first-hand on 2026-10-22
(12 at `p383`–`p385`, **11 added at `p386`**).

| platform | server | ref | licence | note |
|---|---|---|---|---|
| **Moodle** | [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | `main` | 🟡 **GPL-3.0-or-later, in the source headers** (no root licence file) | 🟢 **The first-party path.** The GitHub home of the `webservice_mcp` plugin listed in **Moodle's own plugin directory** (Moodle 4.5–5.2, latest release 23 Jul 2026, gated on `webservice/mcp:use`). No root `LICENSE`, but `version.php` carries the full GPL-3.0-or-later header, as Moodle requires of every plugin. Granted — and GPL is survivable here, because the agent reaches it over JSON-RPC rather than linking to it. |
| **Moodle** | [lmscloud-io/moodle-mcp-server](https://github.com/lmscloud-io/moodle-mcp-server) | `main` | 🟡 GPL-3.0 | Vendor-maintained. GPL is survivable here: the agent talks to it over JSON-RPC, it is not linked. |
| **Moodle** | [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | `main` | 🔴 **UNGRANTED** | Course, announcement and assignment tools. No licence file **and** no `license` field in `pyproject.toml`. Do not ship. |
| **Canvas** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | `main` | 🟢 **MIT** | 🟢 **The clean default.** Courses, assignments, submissions, grading, rubrics, students. |
| **Canvas** | [mdweaver/canvas-mcp](https://github.com/mdweaver/canvas-mcp) | `main` | 🟢 **MIT** | Fork of the above: adds office-hour appointment groups, announcement editing, syllabus read/write, student groups, course-content copy. |
| **Canvas** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `main` | 🟢 **MIT** | Independent implementation — useful as a second opinion on tool shape. |
| **Canvas** | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | `main` | 🟡 **MANIFEST-ONLY MIT** | Advertises 54 tools and Streamable HTTP. No licence **file**, but `package.json` declares `"license": "MIT"` — and its `files` array names a `LICENSE` that is absent from the tree. Usable; get the file committed. |
| **Open edX** | [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | `master` | 🔴 AGPL-3.0 | Matches the platform's own licence, which is the reason it can exist. |
| **Open edX** | [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | `master` | 🔴 AGPL-3.0 | The `tutor` plugin that installs it — the realistic deployment route. |
| **Google Classroom** | [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | `main` | 🟢 **MIT** | Classroom is not an LMS a studio can fork, so MCP is the *only* integration surface. |
| **Brightspace / D2L** | [general-mudkip/d2l-mcp-server](https://github.com/general-mudkip/d2l-mcp-server) | `main` | 🟡 **MANIFEST-ONLY MIT** | The only D2L server verified this pass. No licence file; `package.json` declares `"license": "MIT"`. **D2L remains thin — one server, and its grant is a manifest line.** |
| **Blackboard** | [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | `main` | 🟢 **MIT** *(1,063 B)* | 🆕 `p386`. 🟢 **The only institution-grade LMS MCP server on this shelf.** Wraps the **official Blackboard Learn REST API**; README claims OAuth2, role gate, FERPA handling, rate limiting, PII scrub, JSON audit log, Prometheus `/metrics`, 40 tools incl. **grade write-back** and webhooks (self-claimed, read not executed). 🔴 Grade write-back is gated or prohibited in several jurisdictions — check [`policy-matrix`](../intel/policy-matrix.tsv) before enabling it. |
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

- [microsoft/autogen](https://github.com/microsoft/autogen) — root `LICENSE` is **CC-BY-4.0**
  (18,649 B, "Attribution 4.0 International"). The **code** grant is a *different file*,
  `LICENSE-CODE` = **MIT**. A tool that reads one file and reports "CC-BY" is wrong about the code,
  and a tool that reports "MIT" is wrong about the docs.
- [open-webui/open-webui](https://github.com/open-webui/open-webui) — `LICENSE` is **2,819 B**
  against stock BSD-3's ~1,500 B. It is BSD-3 text **plus a branding restriction and a Contributor
  License Agreement**, self-titled "Open WebUI License". Not an OSI-standard BSD grant. Prefer
  [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) (**MIT**, 1,065 B) as a campus
  LLM gateway where the licence has to be clean.

## Verification method

`curl -sI https://github.com/...` returns **403** through this sandbox's agent proxy, and
`api.github.com` returns **403** with an `add_repo` message, so the method prescribed in the run
brief was unavailable. Two stronger channels were used instead and are reproducible:

1. `git ls-remote --symref https://github.com/<slug> HEAD` — proves the address resolves **and**
   returns the **real default ref**. A renamed, deleted or private repository fails here; a HEAD
   request against GitHub's HTML would not have distinguished those.
2. `raw.githubusercontent.com/<slug>/<real-ref>/<path>` — the licence **text**, read first-hand and
   recorded with its byte length, so a hand-edited or non-stock grant shows up as a length anomaly.

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
