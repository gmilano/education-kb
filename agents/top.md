---
industry: education
region: Global
updated: 2026-10-31
---

# Top AI agents for education

Every row below was verified on 2026-10-31. **The fourth pass changed the
verification method again, and this time decisively:** star counts and metadata
come from the **GitHub REST index** (`search_repositories` via MCP,
`minimal_output: false`), and **licences are now read from the licence file
itself** over `raw.githubusercontent.com`, which answers HTTP 200 from this
session while `api.github.com` and `github.com` HTML both return 403. Earlier
passes could read only GitHub's *determination* of a licence; this one reads the
**text**, with byte counts recorded. Twenty-one licence files were read.

**Nineteen agents qualified, up from fourteen.** The five new rows were not a
market movement — they were a **blind axis**. The fourteen-row shelf was swept
from `topic:ai-tutor` and `topic:agent-skills topic:education`; adding
`topic:ai-education stars:>150 pushed:>2026-10-20` returned six repositories of
which **five were not on the shelf**, the largest at 1,034★. The previous pass's
saturation reading was true of its axes and false as a claim about the
population. Six candidates were rejected and are listed with reasons.

## The shelf

| Agent | Repo | Licence | ★ | Region | What it is |
| --- | --- | --- | --: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 52,208 | APAC | Lifelong personalised tutoring; multi-agent pipelines over LLM + RAG. Python, created 2025-12-28. Data Intelligence Lab, University of Hong Kong. **Still the largest education agent on GitHub.** Fourth-pass reading, 2026-10-31 10:42 UTC: **52,208★**, **6,394 forks** (6,388 at 09:40), 256 open issues, pushed 10:39 the same day; the homepage field now carries `arxiv.org/abs/2604.26962`. |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,984 | APAC | **The most consequential new row in this KB.** "Open Multi-Agent Interactive Classroom" — turns a topic or uploaded documents into an interactive lesson with AI teachers *and* AI classmates: slides, quizzes, simulations, speech, whiteboard, live discussion. Exports PPTX, single-file offline HTML, or classroom ZIP. TypeScript (Next.js 16/React 19), **6,501 forks** read at 10:10 UTC (6,502 at 09:40), 212 open issues, `v1.3.0` dated 2026-10-29. Created **2026-03-11** — 42k★ in under eight months. `LICENSE` reads "MIT License, Copyright (c) 2026 THU-MAIC"; contact domain is `tsinghua.edu.cn`. |
| DIO Agent | [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | ⛔ **NO LICENCE** — see note | 2,750 | LATAM | **The first LATAM-origin education agent found in three passes, and it cannot be built on.** A study-mentor agent bundle: `AGENTS.md`, `CLAUDE.md`, and `skills/` with one `SKILL.md` per skill (study planning, hinting without answering, concept explanation, web search, portfolio review, career guidance). Runs on Claude Code, Codex, OpenCode, Antigravity, Hermes. 347 forks, created 2026-05-27. README is Portuguese; org links `dio.me`, a bootcamp/`formações` platform. **Licence defect, now verified by three methods:** the API returns **no `license` field at all**, the repo page names none, and this pass fetched all five standard licence filenames on both branches over `raw.githubusercontent.com` — all 404. Default is exclusive copyright, i.e. all rights reserved. Fork and read, do not ship. |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1,280 | APAC | Self-study companion agent: builds a route through a subject, teaches it, and sets projects, with spaced repetition. JavaScript, 60 forks, created 2026-09-17. Chinese-language. |
| learn-from-materials | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | MIT | 1,201 | APAC | Turns PDFs, books and papers into interactive learning webpages that stay traceable to the source and carry quizzes and notes. Python, 109 forks, created 2026-09-08. The closest thing on the shelf to a document-to-course pipeline. |
| Papermorph | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | MIT | 1,034 | Global | **The fastest-growing education agent on this shelf: 1,034★ in four weeks.** "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created 2026-10-03. Topics include **`scorm`** and `interactive-textbook` — it targets the installed courseware base, not only the web. MIT read first-hand from `main/LICENSE` (1,069 B). ⚠️ The copyright line reads "Copyright (c) 2026 TedKaczynski", a pseudonym: the grant is valid, the holder is unidentifiable, and that is a diligence item for a client deliverable. |
| Claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT | 557 | Global | "An open-source alternative to Udemy and Coursera": give Claude a topic, it researches the web and builds a course of **2-minute audio lessons with cited sources**. Python, 67 forks, created 2026-10-14, ElevenLabs TTS. **Cited sources as a design feature** is rare here and makes it the one content-generating agent that starts from provenance rather than retrofitting it. MIT, `main/LICENSE` 1,069 B, "Copyright (c) 2026 Assaf Kipnis". |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 539 | Global | MCP server giving an agent control of **Anki**, the spaced-repetition flashcard system. TypeScript, 39 forks, created 2025-09-29. The retention layer: the one verified way to hand an agent a real SRS scheduler instead of reimplementing one. Origin not stated. |
| SocialCoach | [GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach) | Apache-2.0 | 463 | Global | Social-emotional learning by role-play: conflict handling and communication skills with personalised feedback. TypeScript, 60 forks, created 2026-09-03. The only verified **SEL** agent found; SEL is a budget line in K-12 that no other row addresses. Origin not stated. |
| Exam Cram Coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 364 | APAC | Exam-prep tutor that teaches **from the instructor's own slides with page citations**, crops figures, and quizzes from real homework. Explicitly engineered against hallucination (`anti-hallucination` topic) and to run on small cheap models. Python, created 2026-06-24. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 310 | North America | The most established Canvas LMS MCP server. Sidebar: "up to 102 tools and 8 agent skills"; README has said 128. Python, 101 forks, created 2025-02-28. Ships agent skills including pre-semester course audit and accessibility auditor. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 295 | APAC | Socratic private tutor that reads how a learner actually learns; Bloom's 2-sigma research packaged as an agent skill **plus** a self-hostable FastAPI/React app. 44 forks, created 2026-03-10. The clearest instance of the skill-and-app dual shape (see [`../intel/trends.md`](../intel/trends.md)). |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America | Intelligent tutoring system with **Bayesian Knowledge Tracing**, React + Firebase. 164 forks — the highest fork-to-star ratio on the shelf, which is what a teaching-materials project looks like in use. Published at CHI '23. Owning org CAHLR; a UC Berkeley connection is indicated by the authors, not stated on the repo page. |
| WordLink | [orionsheep/wordlink](https://github.com/orionsheep/wordlink) | MIT | 262 | Global | Vocabulary learning on a **fine-tuned 1.5B model (SFT+DPO) that runs entirely offline in the browser** via WebGPU. TypeScript, 38 forks. Topics include **`sdg4`** (UN Sustainable Development Goal 4) and the Qwen/ModelScope stack. **The only in-browser offline model in this KB**, and therefore the only agent here that works with no connectivity and no inference bill. MIT, `main/LICENSE` 1,093 B. |
| AI Learning Guide | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | MIT | 242 | Global | Interactive desktop app with **51 labs** across ML fundamentals, transformers, RAG, agents, fine-tuning and quantisation. TypeScript + ONNX, **offline-first**, 23 forks, created 2026-10-05. Not a tutor — **AI-literacy delivery as a shippable artefact**, which is what Singapore's and the UAE's mandates actually procure. MIT, `main/LICENSE` 1,081 B. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT | 213 | APAC | High-stakes civil-service exam preparation (行测/申论/职测/综应), including a wrong-answer review loop. Python, created 2026-04-06. Shelved as the reference example of **one named credential, fully modelled** — the shape a client asks for by name. |
| Cram Engine | [liuliu667/cram-engine](https://github.com/liuliu667/cram-engine) | MIT | 176 | APAC | A **four-stage interactive cram skill grounded in learning science**: get the material understood, retained, and usable on exam answers inside a fixed time budget. Chinese-language; topics `learning-sciences`, `aied`. Created 2026-06-06. Shelved because it is the only row that models **time-boxed revision** — the request a client actually receives before an exam season. MIT, `main/LICENSE` 1,064 B. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 158 | Global | Block-based adaptive learning workspace that runs **locally**: upload material, get notes, quizzes, flashcards and an adaptive tutor, over 10+ LLM providers, with a knowledge graph. Python/TypeScript, 38 forks. **Star-count correction:** an earlier cycle of this KB recorded OpenTutor at ~900★; the API says **158**. The earlier figure was wrong. |
| Pedagogy Benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | Not a tutor — an **evaluator**. 1,143 questions from real teacher-qualification exams: CDPK (920, general pedagogy) and SEND (223, Special Educational Needs and Disabilities). Code for *Benchmarking the Pedagogical Knowledge of Large Language Models*. Its parent organisation is the LMIC-focused supply side this KB spent three passes failing to find — see [`../repos/foundations.md`](../repos/foundations.md). |

### Carried with a known defect

| Agent | Repo | Licence | ★ | Region | Note |
| --- | --- | --- | --: | --- | --- |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ⛔ MIT claimed in README only — **no LICENSE file** | 104 | North America | Canvas LMS MCP server, `v2.2`, 54 tools, containerised. **Defect now confirmed by three independent methods.** (1) Earlier passes 404-ed every licence filename on both branches. (2) GitHub's own licence index (`license:mit repo:DMontgomery40/mcp-canvas-lms`) returns **zero results**. (3) This pass fetched all five standard filenames on **both** `main` and `master` over `raw.githubusercontent.com` — the channel that successfully returned 21 other licence files the same hour — and every one 404s. There is no MIT grant. Prefer `vishalsachdev/canvas-mcp`. |
| moodle-mcp | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | 27 | APAC | Rust MCP server operating Moodle: courses, assignments, forums, grades, files-as-markdown. Validated against Moodle 3.7 → 5.x. Only Rust implementation found. No defect — listed here because at 27★ and created 2026-10-12 it is too young to carry an engagement alone. |

### Agent-skill bundles verified MIT this pass — components, not shelf rows

Six more education skill bundles clear the licence gate but are deliberately
**not** shelved: each is a single narrow instruction set rather than an agent an
engagement would be built around, and padding the shelf with them would
misrepresent the agent population. They are recorded because they are real,
MIT-licensed, and immediately usable as components inside a larger deliverable —
and because the licence text of every one was read this pass.

| Bundle | Repo | Licence | ★ | Region | Use it for |
| --- | --- | --- | --: | --- | --- |
| learn-anything-with-AI | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | MIT (1,065 B) | 203 | Global | Project-driven **mastery learning** with mastery checks and authoritative sources — the scaffolding layer under a subject tutor. |
| awesome-student-ai-skills | [cuic19053-hue/awesome-student-ai-skills](https://github.com/cuic19053-hue/awesome-student-ai-skills) | MIT (1,070 B) | 147 | APAC | 35 Chinese university application-document skills (大创申报书, 挑战杯, 国家奖学金, 保研). The reference example of **one national paperwork regime, fully modelled**. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT (1,068 B) | 119 | APAC | Teaching and tutoring collection including *gaokao* preparation. |
| montessori-skill | [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | MIT (1,063 B) | 78 | APAC | **Montessori pedagogy as a skill** — child education, self-directed learning, environment design. The only named pedagogical *philosophy* in this KB. |
| research-field-onboarding | [ljx-chase/research-field-onboarding](https://github.com/ljx-chase/research-field-onboarding) | MIT (1,111 B) | 75 | Global | Onboarding a learner into an unfamiliar research field; literature review. Higher-ed and R&D clients. |
| assignment-check | [henryyu333/assignment-check](https://github.com/henryyu333/assignment-check) | MIT (1,086 B) | 53 | Global | **Pre-submission checking against the brief, the rubric, evidence and citations.** The closest thing in open source to a student-side quality gate, and the cheapest row here to wire into pattern P-568-K. |

And one that cannot be shelved but can be **partly** used:
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree)
(586★) is **AGPL-3.0** — but its `skills/` directory is **dual-licensed AGPL-3.0
or MIT at the adopter's option**, read first-hand from `master/LICENSE`. The
platform is disqualified for a proprietary derivative; **the skill bundles inside
it are not.** See the resolution note below.

## Why this shelf is shaped the way it is

**The agent layer is permissive; the platform layer is not.** Of the nineteen
shelf rows, **16 are MIT, 2 Apache-2.0, and 1 has no licence at all** — all five
new rows this pass are MIT, read from the licence file. Every platform of record
these agents attach to is copyleft, with two exceptions now documented in
[`../repos/foundations.md`](../repos/foundations.md). The integration surface is
buildable; the substrate mostly is not forkable on commercial terms. The
composition pattern that follows is in [`../compose/patterns.md`](../compose/patterns.md).

**Education AI has stopped shipping as applications.** **Nine of nineteen** shelf
rows are **agent skills** — markdown instruction bundles loaded by an existing
harness (Claude Code, Codex, OpenCode, Cursor, Antigravity) rather than
deployable services: `dio-agent`, `Study-Mate`, `learn-from-materials`,
`Papermorph`, `Claudemy`, `Exam Cram Coach`, `Bloom`, `kaogong-skill` and
`Cram Engine`. `Bloom` ships as a skill **and** a self-hostable app, which is the
hybrid shape to expect next. Counting the six component bundles above, **15 of
the 25 agents on this page have no runtime at all.**
This is measured, not reported: `topic:agent-skills topic:education stars:>50`
returns **13 repositories** — the same count as the previous pass, so that axis is
genuinely saturated — and this pass read **all thirteen licence files**. The
distribution is the finding: **11 MIT, 1 CC BY-SA 4.0, 1 unlicensed, 1
dual-grant — and the two non-permissive members are the two largest, at 4,843★
and 2,750★.** In this cohort, popularity is anti-correlated with licence
usability. Consequences for an engagement are in
[`../intel/trends.md`](../intel/trends.md); the short version is that the
"product" a client now adopts may be a prompt contract, with no runtime to host
and no API to version.

**Origin has concentrated in APAC — but the new rows are unplaceable, and that
is its own finding.** Of the nineteen shelf rows, **8 are APAC**, and the two
largest (52k★, 42k★) are both Chinese-university projects, HKU and Tsinghua. The
rest: **Global 7, North America 2, LATAM 1 (unlicensed), EMEA 1 (13★)**. Adding
the two defect-table rows puts North America at 3 and APAC at 9.

**Global is now the largest bucket after APAC, and it grew because the
instrument shrank, not because origin diversified.** Four of this pass's five
new rows are Global because owner location **cannot be read from this session at
all**: `search_users` returns login, id and avatar with no `location` field, and
`api.github.com` is 403. Region was assigned only where the artefact itself
states it. Do not read "Global 7" as geographic spread — read it as **seven rows
whose provenance is unknown**, which for client-facing use is a diligence
backlog, not a feature.

**MCP is still the integration shape, but no longer the dominant one.** Two shelf
rows are MCP servers (`canvas-mcp`, `anki-mcp-server`), and so are both rows in
the defect table (`mcp-canvas-lms`, `moodle-mcp`) — four of the twenty-one
shelved-and-defect agents on this page, and four of twenty-five counting the
component bundles. Where an agent must *reach into* a system of record, assume MCP; where
it must *teach*, assume a skill bundle.

## Rejected this run, with reasons

| Candidate | Why it is not on the shelf |
| --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | **4,843★ — would be the third-largest row — and rejected on licence.** A library of 23,000+ agent skills for empirical research across eight social-science disciplines, maintained by CoPaper.AI from Stanford REAP (North America). **Evidence upgraded this pass from the README badge to the licence file itself:** `main/LICENSE`, 620 bytes, "Creative Commons Attribution-ShareAlike 4.0 International" — a *content* licence with share-alike. Derivatives of the skill text must be released under the same terms, which is the opposite of what a client wants from a billable methodology asset. |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **932★ — the most substantively relevant rejection in this KB — and also CC BY-SA 4.0.** **165 evidence-grounded AI skills for teachers, school leaders and EdTech builders**: pedagogy, learning science, curriculum design, assessment, competency-based education, inclusive design, retrieval practice, systems thinking. TypeScript, 131 forks, created 2026-03-01, pushed 2026-10-31, runs on Claude, Codex and Hermes. On substance this is the best-targeted education skills library found in four passes — written for the *professional* buyer rather than the student. `main/LICENSE`, 1,230 bytes: "Creative Commons Attribution-ShareAlike 4.0 International, Copyright (c) 2026 Gareth Manning". **Two share-alike libraries now sit at the top of this category (4,843★ and 932★), which makes it a pattern rather than an instance:** authors of large pedagogical skill libraries reach for CC licences because the artefact reads as writing. The consequence is fixed — **the best-curated pedagogy content in open source cannot be absorbed into a proprietary methodology asset.** Use it internally, reference it, point clients at it; do not rebadge it. |
| [ystemsrx/sql-to-ER](https://github.com/ystemsrx/sql-to-ER) | **192★ — not an education agent.** Converts SQL or DBML to ER diagrams; tagged `education` because it is used in database courses. It surfaces inside `topic:agent-skills topic:education` and is the clearest instance of **topic-tag dilution** in that cohort. Logged so the next pass does not re-triage it. |
| [bayshores/godspeed](https://github.com/bayshores/godspeed) | **AGPL-3.0, 7★.** An MCP-native tutor that runs inside Claude Code, Codex or any MCP client and keeps mastery in a knowledge graph. Re-read this pass: still **7★**, created 2026-10-27, pushed 2026-10-31. Copyleft and too young. It is also, as of this pass, **the only repository returned by `topic:ai-tutor created:>2026-10-25 stars:>3`** — i.e. the six-day fresh-tutor cohort is a population of one. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 217★. Self-hosted AI language-learning platform (CEFR plans, voice conversation, flashcards, spaced repetition, local or cloud LLMs) — technically a good fit and licence-disqualified for a proprietary derivative. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned to it. Recorded so the next pass does not re-discover it. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **Licence RESOLVED this pass — `AGPL-3.0`, with a per-directory dual grant.** 586★, 33 forks, TypeScript. "AI-Powered Skill Tree for Lifelong Human Learning", 30+ skills K-12 → career, cognitive-science framing, ships an MCP server. `master/LICENSE`, 1,063 bytes: "GNU AFFERO GENERAL PUBLIC LICENSE Version 3 … Copyright (c) 2026 Human Skill Tree Contributors", followed by a `DUAL LICENSING NOTE`: *"The SKILL.md files in the `skills/` directory may be used under either this AGPL-3.0 license OR the MIT license, at your option."* **So the platform is rejected and the skill bundles are usable** — the fifth distinct licence shape catalogued in this KB, and the first a licence *column* cannot express. **Note the branch:** its default is `master`; every `main/LICENSE*` probe 404s. Probing only `main` manufactures false "no licence" readings, which is how two passes left this unresolved. |
| [AFRICAN-AI-NETWORK/learnhouse](https://github.com/AFRICAN-AI-NETWORK/learnhouse) | **A 0★ fork, and the trap this pass nearly fell into.** It surfaced as the leading hit for an African education-AI search and the organisation name reads as African supply side. It is a fork of [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) (**AGPL-3.0** plus a separate Enterprise Licence, 2.4k★, maintainer Badr B. / `@swve`, country not stated), with 0 stars and 1 fork and no stated African content. The African signal is the **org name only**. Same failure mode as the `NelsonSpencer/canvas-mcp` fork rejected on the previous pass: an organisation name is not provenance. |
| [profitsylivester-ux/tujifunze-agent](https://github.com/profitsylivester-ux/tujifunze-agent) | **MIT (README), 0★, 11 commits, no releases, empty Languages panel.** LangGraph + MCP + Qwen 2.5 decision-support agent tracking multi-term learner trajectories and producing cited plain-language student profiles with human-in-the-loop oversight. Built for the **African Agentic AI Design Challenge, Education track**; "Tujifunze" is Swahili; no country stated. Below the shelf bar, but **logged as a watch item and as evidence**: it is the first African-context education agent this KB has located in three passes, and its design — citations plus mandatory human review over learner records — is the right shape for ministry work. |

## Method note — the two channels that work, and the three that do not

**Existence and metadata: the GitHub REST index.** Every repository URL on this
page was confirmed by `search_repositories` with `repo:owner/name`, which returns
id, licence determination, star count, fork count and push date in one call.

**Licence text: `raw.githubusercontent.com`, new this pass and the better
instrument.** `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/LICENSE`
returns **HTTP 200** from this session. Twenty-one licence files were read
byte-for-byte this pass, which closed two licence questions that three earlier
passes could not answer (`evaluators`, `human-skill-tree`) and added a third
confirmation to two standing defects. **Read the file, on every plausible
filename and on every branch** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
`licence`, `COPYING`, against both `main` and `master`. `human-skill-tree` is
AGPL-3.0 on `master` and 404 on `main`.

**Three channels that do not work from this session, each failing in a way that
could be mistaken for a finding:**

- **`curl` to `github.com` or `api.github.com` → uniform HTTP 403.** A sweep of
  all 57 github.com URLs on this page returned 403 for every single one,
  including `moodle/moodle` and `odoo/odoo`. That is the outbound proxy, not the
  repositories. **If a check returns a uniform status for every URL, it is
  measuring the network, not the data.** A pass that treated those 403s as
  findings would have deleted the entire KB.
- **MCP `get_file_contents` → access denied for any third-party repo.** It is
  **repo-scoped** to the session's own attached repositories. It cannot be used
  to read a licence; `raw.githubusercontent.com` is the substitute.
- **`search_users` → no `location` field.** It returns login, id and avatar
  only, so a maintainer's country is unobtainable and region cannot be inferred
  from the owner profile. This is why four of this pass's five new rows are
  **Global**.

## Declared gaps

- **No published ranking of education AI agents exists.** The prescribed search
  `top open source AI agents education 2026 github MIT` returned, for the
  **fourth** consecutive pass, general-purpose agent listicles (OpenHands, CrewAI,
  AutoGen, Hermes) with an education angle bolted on, plus
  `ashishpatel26/500-AI-Agents-Projects`, a catalogue of use cases rather than
  agents. Four passes is enough to call it a property of the commentary layer
  rather than a gap in the search.
- **But "query the index, not the listicles" was too strong, and this pass
  disproved it.** The prescribed `github trending education AI 2026` search
  surfaced [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) — **MIT,
  71,498★**, the largest permissively licensed repository anywhere in this KB —
  which **no index sweep found**, because it carries no education topic. It is
  shelved in [`../repos/foundations.md`](../repos/foundations.md) as a
  content-production component rather than here, because it is not an education
  agent and padding this shelf with it would misrepresent the agent population.
  **Index sweeps find what is tagged; the open web finds what is famous.** Both
  channels are required.
- **The sweeps have a blind axis, now measured.** This shelf was built from
  `topic:ai-tutor` and `topic:agent-skills topic:education`. Adding
  `topic:ai-education stars:>150 pushed:>2026-10-20` returned **6 repositories,
  5 of them not on the shelf**, the largest at 1,034★. The previous pass's
  saturation finding was true of its axes and wrong as a claim about the
  population. **Next pass: sweep by capability (`topic:pptx`,
  `topic:text-to-speech`, `topic:pdf`, `topic:ocr`) and licence, not only by
  industry topic** — that is where the rest of the horizontal supply is hiding.
- ~~**LATAM: no LATAM-origin education agent qualified.**~~ **Closed, with a
  sting.** Two prior passes searched in English and in Spanish/Portuguese prose
  and concluded the absence was real. It was not — it was a *search-surface*
  gap. Querying GitHub directly with Portuguese and Spanish terms
  (`tutor OR educación OR educacao OR escola OR aprendizaje IA agente stars:>20`)
  returned [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent)
  at **2,750★** — larger than every North American row on this shelf. It is
  **unlicensed**, so the finding is simultaneously a closure and a new blocker.
  Correction to this KB's record: the earlier "two independent search strategies
  support this gap" was overconfident. Both strategies searched the *web*; neither
  searched the *index*.
- **EMEA agent origin is still effectively empty.** The one EMEA row
  (`pedagogy-benchmark`, 13★) is an evaluator, not a tutor. The previous pass's
  only EMEA candidate, `braiinz94/braiinz-education`, remains 0★ alpha. For EMEA
  engagements the *agent* layer is imported; the *platform* layer is now local
  and permissive — see `Selleo/mentingo` (MIT, Poland) in
  [`../repos/foundations.md`](../repos/foundations.md).
- **Seven rows have no stated geographic origin** — `anki-mcp-server`,
  `SocialCoach`, `OpenTutor`, and this pass's `Papermorph`, `Claudemy`,
  `WordLink` and `AI Learning Guide` — and are recorded as **Global** rather than
  guessed at. The count rose because the **instrument shrank**, not because
  origin diversified: `search_users` exposes no `location` in this session and
  `api.github.com` is 403, so owner country is unobtainable by any route.
  Guessing from a maintainer's name would have placed `Claudemy` and
  `Papermorph`; both are left Global. Region is a closed vocabulary here, and
  inventing a value to fill a column is how a filter starts lying.
- **No shelf candidate remains licence-unresolved — a first.** Both standing
  questions closed this pass from the licence text:
  `human-skill-tree` is **AGPL-3.0 with a dual-licensed `skills/` directory**,
  and `Auto-Empirical-Research-Skills` is **CC BY-SA 4.0 in the file**, not just
  the badge. One shelved row stays licence-defective (`mcp-canvas-lms`, now on
  three independent methods). Across four passes, **every licence defect found
  has been in the agent layer** — platforms state copyleft clearly; agents claim
  MIT loosely, ship share-alike, or say nothing, and do so at thousands of stars.
- **`Papermorph`'s copyright holder is a pseudonym** ("TedKaczynski"). The MIT
  text is a valid grant; the holder is unidentifiable. Recorded as a diligence
  item on a 1,034★ row, not as a disqualification.
- **Star counts for the two leaders are timestamped readings, not levels — and
  one circulating growth rate does not reproduce.** DeepTutor: **52,167★ at
  09:40 UTC**, **52,208★ at 10:42 UTC** — **+41 in ~62 minutes**. OpenMAIC:
  41,981★ at 09:40, **41,984★ at 10:10**. A third-party trend digest reports
  DeepTutor at **+2,282 stars on 2026-10-31**, which sustained would be ~95★/hour
  against the 41★/hour measured here. One hour is a thin sample and star arrivals
  cluster by timezone, so this does not refute the daily total — but **no pass
  should quote +2,282 as a rate.** The same digest family was recorded emitting
  "0 total stars with +2,870 today" at an earlier pass.
- **No education-specific agent *observability* or *regression* tooling was
  found — fifth consecutive pass, and this pass the gap got slightly worse.**
  `pedagogy-benchmark` (MIT, knowledge) and `learning-commons-org/evaluators`
  (rubric scoring) remain the only evaluation assets located, and neither is a
  runtime monitor. `evaluators`' licence is now **resolved and partly
  restrictive**: code **MIT**, prompts **CC BY 4.0**, but its two annotated
  corpora (CLEAR, PERSUADE 2.0) are **CC BY-NC-SA 4.0 — non-commercial**. So the
  hand-built regression suite that pattern **P-568-K** prescribes must **source
  its own corpus**; it cannot ship the one that exists. A tutor in production
  still has no open-source way to detect that it has drifted. This remains the
  clearest unmet build opportunity in the industry.
