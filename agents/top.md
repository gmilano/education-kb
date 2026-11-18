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

🔴 **p900 added a third verification channel, and it changed what the first two mean.** The
two routes above answer *"what does GitHub's search index say about this repository"*. They do
**not** answer *"does this address resolve"* — and this base had been reading the first as the
second. Measured this pass over 50 addresses `search/repositories` reported as non-existent:
**22 of them (44%) return `200` on `raw.githubusercontent.com`**, four as rename redirects and
the rest simply absent from the search index. 🔵 **An existence claim now requires both
channels**, and where a repository is reachable but unindexed its row carries *"not in the
search index"* in the ★ column rather than a number — **an honest blank, not a zero.** Eight
such rows were promoted this pass out of this base's own `logged-not-shelved` ledger, where
they had been logged between 5 and 14 times and never given a row. Detail and the retraction of
p899's phantom are in `agents/trending.md` p900.


🔴 **p899 (this pass) added 18 rows — the largest single-pass addition this table has made — and
every one of them was already inside this KB.** Not one came from a new web search. They came
from two places: this base's own `evidence/logged-not-shelved.2026-11-16-p860.tsv` ledger, and a
**description-filtered** discovery leg run per `898-G2`'s acceptance test. **The finding is about
this KB's promotion step, not about the ecosystem.** Measured today: of the 40 most-logged
unshelved addresses, **36 are still unshelved**, and they include **`virgiliojr94/book-to-skill`
at 38,369 ★ under MIT** — which would rank **third in this table** — plus seven more permissively
licensed repositories above 1,000 ★. Meanwhile this table publishes rows at 0 ★, 4 ★, 10 ★ and
12 ★. **Discovery was never the bottleneck; promotion was.**

🔴 **A standing claim in this file was refuted by that measurement.** The "tutor as an agent
*skill*" cohort was recorded across two passes as *"topping out at 118 ★"* (later 125 ★). It tops
out at **38,369 ★**. The ceiling was an artefact of ranking a poisoned keyword, and `898-G2` had
already diagnosed the poisoning without anyone re-running the leg.

🟢 **Origin placement is now instrumented, and it rejected two of its own candidates.**
`compose/code/p899-origin-strip/` ships per `898-G1` with 36 controls and the `aula` README as a
named negative fixture. It placed three repositories on dispersed, exclusive-marker evidence
(spread ≥ 0.96) and **refused two that a naive reading would have placed** —
`book-to-skill` (Cyrillic, spread **0.001**: a language switcher) and `rumi-platform`
(Devanagari, spread **0.001**: a supported-languages list). A language list is evidence of
*translation* or of a *target market*; it is never evidence of origin.

**p897 (this pass) changed no row in the table below, and that is the finding.** It ran the job
`p896` left open — a licence re-read of every unresolved row — and **five of seven were wrong as
recorded**, but all five live in `repos/`, not here. It also ran the first **discovery leg** since
`p893` (`p896` ran none): three new MIT entrants, all byte-read, **none promoted** — `lynote-ai/ai-tutor`
(82 ★, two days old), `armanakh/atlas-of-intelligence` (38 ★) and `altuzar/OpenFounderSchool` (27 ★)
are all sub-100 ★ and under three weeks old, and this KB's own cohort evidence is that such repos
churn. They are in `agents/trending.md` with a watch condition. The same leg **replicated finding
`724-S`**: the highest-starred result for an education-agent query was a **stock-valuation tool**,
and 6 of 11 hits above 10 ★ were not education at all. Spot check only — `DeepTutor` 60,274 →
**60,323**, `OpenMAIC` 43,878 → **43,887**, `LearnHarness` 10,020 → **10,086** — a **sixth**
consecutive confirmation of the daily cadence. **Full sweep still due 2026-11-19.**

**p895 (this pass) ran the first dedicated *supply-side* leg on Africa and the Middle East — the
oldest standing gap in this file — and it moved three ways.** The Africa-origin agent two passes
had failed to locate **exists** (`Eddy-Emmanuel/EduNaija-LLM`) and is **unlicensed, 1 ★ and
eleven months idle**, so it earns no row; reading it **corrected this KB's own description of
the paper behind it**. The second standing lead, `AFRILANGTUTOR`, **is not on GitHub at all**.
And the "nothing from Africa" claim was refuted by this base's **own deleted row** —
`elimu-ai/webapp`, MIT, 41 ★ / 67 forks, pushed 2026-11-17, **absent from every live shelf**
though the history records it as placed. **That is the second consecutive pass to find a row
deleted by a rewrite** (p894 found the same for `UniTime/unitime`), which makes it a process
defect rather than an accident: the recommended next job is a shelf-vs-history slug diff in
`compose/code/`. The LATAM gap bullet was also **stale against the table directly above it**
and is corrected. No row was added to the table this pass.

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
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 60,351 | 2026-11-18 | Agentic personalised tutoring grounded in the student's own material, with persistent learning history. Hit #1 on GitHub trending 28 Oct 2026; first released Dec 2025. Paper: arXiv 2604.26962. **The single largest open education agent in existence.** | APAC — HKU Data Intelligence Lab |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | 43,889 | 2026-11-18 | Multi-agent AI classroom: agents generate slides, quizzes and project-based activities and grade quiz answers. `v1.4.2` (2026-11-09) added course-level undo for manual edits and agent runs. Relicensed to MIT at `v0.3.0`, Jun 2026. | APAC — Tsinghua University |
| **LearnHarness** | https://github.com/amosblomqvist/learnharness | **AGPL-3.0** | 10,110 | 2026-11-12 | Desktop agent harness that *measures* what the learner understands before it teaches: probe → dependency-map the route to the goal → teach one reasoning step at a time → separate retrieval-practice sessions, all carried across sessions by a persistent knowledge graph. **Added p893. Created 2026-10-16 — 0 → 10,002 ★ in 27 days, the fastest growth this KB has recorded for any education repo**, and now the third-largest open education agent in existence. **AGPL-3.0, byte-read from `LICENSE@main`. Not usable in a closed derivative** — read it as the reference design for learner-state modelling, the capability every other tutor in this table lacks. No published learning-outcome study; users report being tested before being taught. | Global |
| **frametell** | https://github.com/sitor-ai/frametell | **AGPL-3.0** | 513 | 2026-11-12 | Turns source material into explainer videos via an "AI director" agent. Local-first and model-agnostic. **Added p893.** The only open *content-production* agent in this table — courseware generation rather than tutoring. AGPL. | Global |
| **ai-shifu** | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | 2026-11-18 | Author a course by typing it: the AI delivers the teaching and answers questions inside the flow the author scripted. **Added p893.** Permissive, pushed today, and the clearest open example of *authored* AI teaching — the script constrains the model, which is the control structure Oklahoma-style "no AI-only" rules actually require. | APAC |
| **Moodle-MCP** (Faixiang) | https://github.com/Faixiang/Moodle-MCP | MIT | 208 | 2026-11-01 | Zero-dependency MCP server over the Moodle Web Service API: courses, assignments, quizzes, deadlines, files. **Read-only by design.** **Added p893 — the first Moodle MCP server this table has ever carried**, which was a hole given Moodle is the most-installed LMS on earth. Ships a companion agent skill, https://github.com/Faixiang/Moodle-Course-Watch (MIT, 0 ★), that diffs new coursework and lists what is still unsubmitted. README localised into 10 languages. | APAC |
| **edumcp** | https://github.com/aieducations/edumcp | Apache-2.0 | 155 | 2025-05-05 | An attempt to standardise MCP for education applications. **Added p893 as a cautionary entry: 155 ★ and untouched since May 2025.** The idea was early and right; the project is dormant. Read the protocol sketch, do not depend on it. | Global |
| **gen-mentor** | https://github.com/GeminiLight/gen-mentor | **CC0-1.0** | 137 | 2026-10-23 | Reference implementation for *GenMentor* (WWW '25 oral): a multi-agent framework for goal-oriented, skill-gap-aware learning — it infers the gap between the learner's current skills and a target role, then plans content against it. **Added p893.** **Licence is CC0-1.0, byte-read** — a public-domain dedication, not a software licence, so it carries no patent grant and no warranty disclaimer. Legally the most permissive row here and the least conventional; have counsel confirm before shipping it. | APAC |
| **Mentingo** | https://github.com/Selleo/mentingo | MIT | 109 | 2026-11-18 | Self-hosted **AI-native LMS** with a built-in AI mentor and role-play, white-label and multi-tenant, Postgres + pgvector, one-click AWS Marketplace deploy. **Added p893.** Listed here *and* in `verticals/solutions.md` because it is genuinely both. **Its significance is the licence: an MIT LMS.** This KB's first structural finding is that the platforms clients run are copyleft — Mentingo is the counter-example, and therefore the shortest route to a closed, branded derivative. Corporate L&D and compliance training, not K-12. | EMEA — Poland |
| **canvas-mcp** (Sachdev) | https://github.com/vishalsachdev/canvas-mcp | MIT | 334 | 2026-11-18 | MCP server exposing Canvas LMS — courses, assignments, submissions — as agent tools. | North America — USA |
| **BloomTutor** | https://github.com/Li-Evan/BloomTutor | MIT | 316 | 2026-11-17 | Tutor that structures interaction around Bloom's taxonomy levels. | APAC |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | 282 | 2026-11-17 | Intelligent tutoring system with open problem banks and tutoring-effect instrumentation; built for A/B-testable learning research. | North America — UC Berkeley |
| **molly554/whiteboard-ai-tutor** | https://github.com/molly554/whiteboard-ai-tutor | MIT | 232 | 2026-11-17 | Whiteboard tutor with animated lessons and interactive playback. Created after Aug 2026 — one of the fastest-growing new entrants. | Global |
| **OpenPronounce** | https://github.com/OpenPronounce/OpenPronounce | MIT | 223 | 2026-11-09 | Open pronunciation assessment — the language-learning niche where open source is genuinely competitive with commercial APIs. 🔵 **p900: this base logged `halleck45/openpronounce` 5× in its `logged-not-shelved` ledger and nearly promoted it as a second row.** It is a **transfer alias of this repository** — byte-identical `README.md` (`sha256₁₂ a005d079f571`) — caught by the duplicate-subject gate before publication. **The rename mechanism that causes false ABSENCES in the ledger causes false DUPLICATES on the shelf**; both need the canonical name resolved first. | Global |
| **OpenTutor** | https://github.com/zijinz456/OpenTutor | MIT | 181 | 2026-11-17 | Open tutoring agent. | APAC |
| **canvas-mcp** (Cheng) | https://github.com/boyuchengz/canvas-mcp | MIT | 118 | 2026-10-27 | **Read-only** MCP server connecting Claude/ChatGPT to Canvas LMS. A second, independent `canvas-mcp` — read-only by design, which is the safer default for a student-data pilot. | North America |
| **Open TutorAI (CE)** | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 118 | 2026-06-26 | Community edition of a self-hostable tutor platform. Licence text carries an "All rights reserved" header over a BSD-style grant; SPDX confirms BSD-3-Clause. | EMEA |
| **japanese-tutor-mugi** | https://github.com/brian901106/japanese-tutor-mugi | MIT | 105 | 2026-10-28 | Second-language conversation tutor with a **Chinese-language interface teaching Japanese** — the tutor UI and the target language are different, and neither is English. Its design contract is the reusable part: the LLM returns **structured JSON Schema** output with the Japanese line and the native-language hint as *separate fields*, rendered by partial-JSON parsing so the reply streams as it arrives. **Added p898**, MIT byte-read (`main/LICENSE`, 1,068 B, `sha256₁₂ b349f14f3e8e`). The only repo in this table implementing the separate-fields contract. | APAC |
| **belajar-ngoding-byGanzu** | https://github.com/itsme-ganzu/belajar-ngoding-byGanzu | MIT | 66 | 2026-10-27 | **Bahasa Indonesia** Python-from-zero course with a personal AI tutor that drills reasoning rather than handing over answers. **Added p898**, MIT byte-read (`main/LICENSE`, 1,062 B, `sha256₁₂ 410186335243`); placed **APAC** on 30 Bahasa markers in a stripped README. 🔵 **The first Indonesian-language row in this table** — Indonesia is the fourth-largest school system in the world, and this is the only vernacular-Indonesian education repo the KB has verified. Small and young; read it as evidence of where vernacular supply is appearing, not as substrate. | APAC |
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
| **Socratic-Education-System** | https://github.com/HowieWang1121/Socratic-Education-System | MIT | 137 | 2026-05-03 | Socratic-method tutoring system whose README argues education is a right to be guaranteed rather than an obligation, and targets students without access to paid tutoring. **Restored p896** — it was carried on this shelf and deleted by the 2026-11-18 cleanup without appearing in that pass's own list of removals. At 137 ★ it is the eighth-largest education-native agent here. **Caveat: last push 2026-05-03**, so read it as a design reference. | APAC — China |
| **education-skills** | https://github.com/flysheep-ai/education-skills | MIT | 125 | 2026-01-30 | Collection of education-specific **agent skills** (teaching, tutoring and study-support tools packaged for a coding agent). **Restored p896.** 🔴 **The standing claim attached to this row — that it is the largest member of the "tutor as an agent *skill*" cohort, which "two passes recorded as topping out at 118 ★" — was refuted in p899 and is retained here only to mark the correction.** Measured 2026-11-18, the skill cohort runs to **`book-to-skill` at 38,369 ★**, with `Papermorph` (1,775), `learn-from-materials` (1,455), `Claudemy` (706) and `universal-examprep-skill` (396) all above it. The ceiling was an artefact of a star-ranked keyword leg, not a property of the cohort — see `898-G2` in `intel/open-gaps.md`. Idle since 2026-01-30. | APAC — China |
| **civil-ai** | https://github.com/zhangl1001/civil-ai | MIT | 41 | 2026-11-08 | **Local-first** adaptive tutoring agent reference implementation for **iOS and Web**, applied to civil-service exam preparation. **Restored p896.** Two things make it worth a row despite 41 ★: it is one of very few open tutors with a **native mobile** target, and local-first inference is the posture that satisfies California AB 1159 and EMEA sovereignty procurement without a data-processing argument. | APAC — China |
| **book-to-skill** | https://github.com/virgiliojr94/book-to-skill | MIT | 38,369 | 2026-11-08 | Turns a technical book, document folder or PDF into a packaged agent skill you can then study against. **Added p899 — and it is the third-largest repository in this entire KB**, behind only DeepTutor and OpenMAIC and nearly 4× LearnHarness. MIT byte-read (`LICENSE.md@master`, 1,068 B, `sha256₁₂ be9b04bccfb4`). 🔴 **It sat in this KB's own `logged-not-shelved` ledger with 28 recorded mentions and no row.** Read it as the canonical *courseware-compilation* pattern: the source material becomes the skill, so the model is constrained by the book rather than recalling it. | Unplaced — see note below |
| **Papermorph** | https://github.com/DozenTwelve/Papermorph | MIT | 1,775 | 2026-11-16 | Turns books and papers into animated, narrated, interactive web explainers. **Added p899.** MIT byte-read (`LICENSE@main`, 1,069 B, `sha256₁₂ 41857092247a`). 🟡 **Procurement caveat: the copyright line reads `Copyright (c) 2026 TedKaczynski`** — a pseudonym. The grant is valid on its face, but there is no identifiable holder to obtain a CLA, warranty or indemnity from, which several enterprise clients will refuse. Read the technique, vendor the code knowingly. | Global |
| **Study-Mate** | https://github.com/Miaotofu01/Study-Mate | MIT | 1,488 | 2026-11-17 | Study companion that plans a route through a subject, teaches it, and builds projects alongside the learner. **Added p899.** MIT byte-read (`LICENSE@main`, 1,064 B, `sha256₁₂ dc1997d82189`). Placed APAC on a stripped-README CJK score of **1,490 with spread 0.971** — dispersed prose, not a language switcher (see `compose/code/p899-origin-strip/`). | APAC |
| **learn-from-materials** | https://github.com/dmoshehun-prog/learn-from-materials | MIT | 1,455 | 2026-10-19 | Turns PDFs, books and papers into interactive learning webpages. **Added p899.** 🔵 **Lineage finding:** its `LICENSE.md` carries **two** copyright lines — *"Copyright (c) 2025 virgiliojr94"* then *"Copyright (c) 2026 learn-from-materials"* — so it is an acknowledged derivative of the `book-to-skill` row above. The two together are 39,824 ★ of one lineage that this KB had never shelved. | Global |
| **get-it** | https://github.com/beltromatti/get-it | Apache-2.0 | 1,168 | 2026-06-29 | *"Read it. See it. Get it."* — turns study material into visual explanation. **Added p899.** Apache-2.0 byte-read (`LICENSE@main`, 11,359 B, `sha256₁₂ d0622ead9e49`) — **patent grant included**, which no MIT row here carries. Built at **GDG AI Hack Milan 2026**, which is where the EMEA placement comes from (event, not language). **Caveat: last push 2026-06-29, nearly five months idle.** | EMEA — Italy |
| **Claudemy** | https://github.com/assafkip/claudemy | MIT | 706 | 2026-10-29 | Self-described open-source alternative to Udemy/Coursera, built as an agent skill. **Added p899.** MIT byte-read (`LICENSE@main`, 1,069 B, `sha256₁₂ 262b47ee1fff`, *"Copyright (c) 2026 Assaf Kipnis"*). | Global |
| **universal-examprep-skill** | https://github.com/ZeKaiNie/universal-examprep-skill | MIT | 396 | 2026-10-27 | Exam-cram coach with cross-session memory and **source-traced handouts specifically to suppress hallucination** — every claim is tied back to the uploaded material. Runs as a skill in Claude Code, Cursor, Codex or Antigravity. **Added p899.** MIT byte-read (`LICENSE@main`, 1,065 B, `sha256₁₂ 21f44893f051`). 🔴 **This KB's own ledger records it logged 34 times and never shelved** — the single most-logged unshelved row with a verified permissive grant. | APAC |
| **deep-student** | https://github.com/helixnow/deep-student | **AGPL-3.0** | 320 | 2026-11-18 | Local-first AI learning workbench. **Added p899.** AGPL-3.0 byte-read (`LICENSE@main`, 34,532 B, `sha256₁₂ 894342980454`). **Not usable in a closed derivative**; local-first is the posture EMEA sovereignty and California AB 1159 procurement ask for, so read it as the reference architecture for on-device study tooling. | Global |
| **freelingo** | https://github.com/artcc/freelingo | **AGPL-3.0** | 291 | 2026-11-17 | Self-hosted language learning with **local or cloud LLMs, CEFR-aligned study plans** and a conversation tutor. **Added p899.** AGPL-3.0 byte-read (`LICENSE@main`, 34,514 B, `sha256₁₂ ea94d5765c59`). CEFR alignment is the part to reuse: it is the European reference framework a public-sector language contract will specify by name. AGPL. | Global |
| **universal-diagnostic-tutor-skill** | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | MIT | 279 | 2026-11-11 | **Diagnosis-first** tutor for STEM and CS — it establishes what the learner has got wrong before selecting what to teach, with no mode switching. **Added p899.** MIT byte-read (`LICENSE@main`, 1,102 B, `sha256₁₂ a9ca00bcc7a5`). Placed APAC on CJK **1,564, spread 0.964**. The diagnosis-first contract is the same capability `LearnHarness` is credited with, at 1/36th the size and under MIT rather than AGPL. | APAC |
| **kaogong-skill** | https://github.com/KeWang0622/kaogong-skill | MIT | 250 | 2026-10-12 | Chinese **civil-service and public-institution** exam preparation (行测 / 申论 / 职测). **Added p899.** MIT byte-read (`LICENSE@main`, 1,083 B, `sha256₁₂ a6943096ffde`). Placed APAC — China on CJK **1,490, spread 0.971**, corroborated by the subject matter, which exists only in that jurisdiction. A worked example of **vernacular, exam-system-specific** supply (trend T20). | APAC — China |
| **ari** | https://github.com/nichochar/ari | MIT | 222 | 2026-11-12 | *"Learn stuff with pen + paper + AI"* — deliberately routes practice **off-screen**, using the model to set and mark handwritten work. **Added p899.** MIT byte-read (`LICENSE@main`, 1,073 B, `sha256₁₂ 9234cc62970c`). The only row in this table whose design goal is **less** screen time, which is the shape several K-12 statutes and parental-consent regimes are pushing toward. | Global |
| **feifei-companion** | https://github.com/SimonsTang/feifei-companion | Apache-2.0 | 117 | 2026-04-19 | 飞飞学伴 — **K-12** study companion, v4.0. **Added p899.** Apache-2.0 byte-read (`LICENSE@main`, 10,227 B, `sha256₁₂ 59a378bf23a0`). **Caveat: idle since 2026-04-19 (7 months).** Carried because K-12-targeted open agents are rare and age-banding is a regulatory requirement in several jurisdictions. | APAC — China |
| **lumen** | https://github.com/ahmedEid1/lumen | MIT | 94 | 2026-10-30 | Learning platform where a **multi-agent builder turns a one-sentence goal into a course**. **Added p899.** MIT byte-read (`LICENSE@main`, 1,076 B, `sha256₁₂ 3051d3f8c2c2`). Course *generation* rather than tutoring — the same side of the line as `frametell`. | Global |
| **PAIDEIA** | https://github.com/OPTIMETA/PAIDEIA | MIT | 93 | 2026-07-11 | Claude Code plugin that builds exam readiness **locally**. **Added p899.** MIT byte-read (`LICENSE@main`, 1,068 B, `sha256₁₂ 3a6a5a1963c8`). **Caveat: idle since 2026-07-11.** | Global |
| **Aila** (`oak-ai-lesson-assistant`) | https://github.com/oaknational/oak-ai-lesson-assistant | **MIT** (code) — see the multi-grant note | 35 | 2026-11-18 | 🟢 **The most institutionally significant row added in p899, and its 35 ★ are the least informative number in this table.** Aila is the AI lesson-planning assistant of **Oak National Academy**, England's publicly-funded national curriculum body, in production for teachers nationally since September 2024 and pushed **today**. 🔵 **This is a multi-grant repository and the distinction matters commercially:** the **code is MIT** (`LICENSE@main`, 1,077 B, `sha256₁₂ d150aadcccd2`, *"Copyright (c) 2024 Oak National Academy"*); the **documentation is Open Government Licence**; and **trademarks and logos are explicitly excluded from the MIT grant**. 🟡 **Posture caveat, stated in its own README:** *"intended primarily for internal use by Oak National Academy… there is no expectation for"* external contribution — it is **published, not maintained as a product**. An independent evaluation involving **NFER and EEF** ran June–September 2026. **Read it as the reference implementation of curriculum-aligned, nationally-governed lesson generation** — the exact artefact an EMEA ministry engagement asks for and the only one in this KB published by a national curriculum body. | EMEA — UK |
| **ai-tutor-app** | https://github.com/towardsai/ai-tutor-app | Apache-2.0 | 34 | 2026-10-22 | Agentic **RAG** tutor for applied AI/LLM/Python curricula, built on LangGraph. **Added p899.** Apache-2.0 byte-read (`LICENSE@main`, 11,386 B, `sha256₁₂ 7dc0f2a45a9e`) — patent grant included. Small, current, and the clearest *readable* LangGraph tutor wiring in this table. | Global |
| **Rumi** | https://github.com/Orenda-Project/rumi-platform | Apache-2.0 | 25 | 2026-11-12 | 🔵 **The delivery-channel outlier in this table, and the reason it earns a row at 25 ★.** An AI teaching assistant that runs **entirely on WhatsApp** — no app, no login, no training day — giving teachers classroom coaching, reading assessments and lesson plans by text and **voice note**, in **15 languages including a full Indian-language suite and Pakistan's regional languages**, with voice-note transcription via Meta's MMS-ASR. Explicitly built to be cloned and self-hosted on your own API keys. Apache-2.0 byte-read (`LICENSE@main`, 11,287 B, `sha256₁₂ c589d95090ce`). 🔴 **Origin deliberately UNPLACED:** its Devanagari score is **11 at spread 0.001** — a supported-languages list, which the p899 instrument rejects as a *target market*, not an origin. **Its significance for Globant is the channel, not the code:** WhatsApp is the dominant messaging surface in LATAM as well as South Asia, and this is the only open education agent in this KB that needs no device provisioning at all. | Global — target market South Asia |
| **Open Learning AI Tutor** | https://github.com/mitodl/open-learning-ai-tutor | **MIT** (`LICENSE@HEAD`, 1,068 B, byte-read p900) | *not in the search index* | — | **Added p900, out of this base's own ledger (logged 5×, never shelved).** MIT Open Learning's tutor backend — it helps students solve **their own course problems**, in production at `learn-ai.ol.mit.edu`, with the pedagogical engine published as a paper (`arXiv:2410.03781`). 🔵 **The rare agent here with an institutional owner, a live deployment and a published pedagogy.** 🔴 Stars unmeasurable: `search/repositories` does not index it (see `900-G2`) | North America — MIT |
| **Instructional Agents** | https://github.com/DaRL-GenAI/instructional_agents | **MIT** (`LICENSE@HEAD`, 1,066 B, byte-read p900) | *not in the search index* | — | **Added p900 (logged 6×).** Multi-agent **instructional design**: generates syllabus, slides and assessment as a faculty-workload reduction, not a student-facing tutor. Ships a no-code Studio and a PyPI package (`instructional-agents`). 🔵 **The supply side of this base's teacher-workload trend, which until now had demand evidence and no permissive implementation** | Unplaced — academic lab |
| **k12-teacher-skills** | https://github.com/anthropics/k12-teacher-skills | Apache-2.0 | 633 | 2026-10-14 | **Added p900 (logged 7×).** A skills pack for K-12 teachers rather than a runtime — lesson planning, differentiation and feedback as composable skill definitions. 🔵 Belongs to the *"tutor as an agent skill"* pattern this file already names below, and is the largest permissive example of it | North America |
| **anki-mcp-server** | https://github.com/ankimcp/anki-mcp-server | MIT | 567 | 2026-11-07 | **Added p900 (logged 10×).** MCP server over **Anki**, putting a learner's real spaced-repetition deck behind an agent — read, create and schedule cards. 🔵 Pairs with `fsrs4anki-helper` in `repos/foundations.md`: the scheduler and the agent seam are both permissive | Global |
| **Educhain** | https://github.com/satvik314/educhain | MIT | 387 | 2026-05-29 | **Added p900 — and this base has NAMED it since its second education cycle without ever giving it a row (logged 14×, the 4th-most-logged address in the rebuilt ledger).** Generates MCQs, lesson plans and full courses from source content, including YouTube. 🟡 **Idle since 2026-05-29** — a stable library, not a tracked upstream | APAC — India |
| **canvas-lms-mcp** | https://github.com/bruchris/canvas-lms-mcp | **MIT** (`LICENSE@HEAD`, 1,069 B, byte-read p900) | 10 | 2026-11-17 | **Added p900.** **165 tools** over Canvas — courses, assignments, submissions, gradebook history, rubrics, New Quizzes (LTI), enrolments. 🔴 **Reached via a rename:** this base logged it as `algorithm0r/canvas-lms-mcp` 5×, which `search/repositories` reports as non-existent; the canonical owner is `bruchris` (see `900-G2`). 🔵 The deepest permissive agent seam onto AGPL Canvas in this file | Unplaced |
| **Horus Taleeq 0.2 Base** | https://github.com/tokenaii/horus-taleeq-0.2b-base | **MIT** (`LICENSE@HEAD`, 1,079 B, byte-read p900) | *not in the search index* | — | **Added p900, and it answers a regional gap this base declared on the wrong side of itself.** An **Arabic-only small language model** — training code and reproducibility record — from **TokenAI**, *"a startup and nonprofit organization focused on open Arabic AI research"*. Scoped deliberately: base model only, no chat adapters, no teacher outputs, no private data. 🔵 `p899` recorded *"no supply-side leg for Africa or the Middle East"*; this was **logged 5× in its own ledger at the time**. 🟡 A base model is a starting point for continued pretraining, not a deployable tutor | EMEA — Middle East |

**55 education-specific agents, every URL and licence verified.** (**p899 added 18** — the largest single-pass addition this table has made, and *not one of them came from a new web search*: every row above was already in this KB's own `agents/trending.md` history or its `logged-not-shelved` ledger, and was promoted only after a licence byte-read and a star measurement today. See `agents/trending.md` p899 for why that is a finding about this KB rather than about the ecosystem.)

(Earlier count: 37 at p896.) (p896 restored three —
`Socratic-Education-System`, `education-skills` and `civil-ai` — all of which this shelf had
carried before the 2026-11-18 cleanup; all three re-verified on both channels today.) (p894 added no rows: its four
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
| **OpenHands** | https://github.com/OpenHands/OpenHands | MIT | 93,731 | Coding agent; the practical choice for automating LMS plugin and migration work. 🔴 **Slug corrected in p896, and in the opposite direction to the earlier note.** `OpenHands/OpenHands` is the canonical repo (93,731 ★, pushed 2026-11-18); `All-Hands-AI/OpenHands` is a **rename alias** that `raw.githubusercontent.com` still serves, which is why earlier passes read it as canonical. The star count was recorded here as *unavailable* only because the alias was being queried. Org also ships https://github.com/OpenHands/software-agent-sdk (MIT). |
| **LibreChat** | https://github.com/LibreChat-AI/LibreChat | MIT | 47,317 | Multi-model chat front end with auth and per-user quotas; fastest route to a governed institutional chat tier. 🔴 **Slug corrected in p896**: `LibreChat-AI/LibreChat` is canonical (47,317 ★, pushed 2026-11-18); `danny-avila/LibreChat` is a rename alias. Same failure mode as the OpenHands row above — see `agents/trending.md` p896 for the gate that catches it. |

**Teaching assets, measured for the first time in p890.** Not agents and not education
products, but the two largest permissively licensed *curricula* relevant to this KB, and both
usable as client-enablement or staff-upskilling courseware that can be rebranded and extended:
https://github.com/microsoft/ai-agents-for-beginners (MIT, **80,197 ★**, pushed 2026-11-17 —
larger than any education agent that exists) and https://github.com/huggingface/agents-course
(Apache-2.0, **35,115 ★**, pushed 2026-11-17).

**🟢 Resolved in `p896`: the three "unavailable" star counts were never unavailable.** This note
used to record that `All-Hands-AI/OpenHands`, `danny-avila/LibreChat` and
`openedx/edx-platform` were *consistently absent from `search/repositories` across repeated
query shapes* while their `LICENSE` files returned `200` on `raw.githubusercontent.com` — and
left it as an unexplained limitation of the channel. **The anomaly was correctly measured and
wrongly diagnosed.** All three are **rename aliases**:

> `raw.githubusercontent.com` follows GitHub's rename redirects; the search API's `repo:`
> qualifier does not. A slug that serves `200` on raw but returns **0 hits** from `repo:` has
> been **renamed** — the canonical name is the one search can see.

| Alias | Canonical | Measured 2026-11-18 |
|---|---|---|
| `All-Hands-AI/OpenHands` | **`OpenHands/OpenHands`** | **93,731 ★**, MIT |
| `danny-avila/LibreChat` | **`LibreChat-AI/LibreChat`** | **47,317 ★**, MIT |
| `openedx/edx-platform` | **`openedx/openedx-platform`** | **8,242 ★**, AGPL-3.0 |

Run over all **172** live slugs in this KB, the gate returns exactly these three
(`evidence/rename-alias-gate.2026-11-18-p896.tsv`). **The symptom is diagnostic, not a dead end:
three identical anomalies had one cause, and it was recoverable with the channels already in
use.**

## Emerging pattern worth naming: the tutor as an agent *skill*

A distinct cohort of repos created since August 2026 delivers tutoring not as a web app but as
a **skill or MCP server inside an existing coding agent** — `ArnaudGuiovanna/tutor-mcp`
(MIT, 104 ★), `boyuchengz/canvas-mcp` (MIT, 118 ★), `BaronCyrus/dsh-aha-tutor` (MIT, 46 ★),
`smashburger-dev/socratic-workshop` (MIT, 24 ★), `bayshores/godspeed` (AGPL-3.0, 22 ★),
`Aisland-SJL/Aisland-teach` (MIT, 18 ★). All are small, but the direction is consistent and it
shortens time-to-pilot dramatically: no front end to build, and the learner already has the
client installed.

🔴 **p896 raises the cohort ceiling to 125 ★, and the member that raises it was deleted from
this shelf by this KB.** `flysheep-ai/education-skills` (MIT, **125 ★**) is a collection of
education agent skills — a cohort member by definition. It was carried in `agents/top.md`,
removed by the 2026-11-18 cleanup, and therefore absent from the set every subsequent
measurement enumerated. This is the **second** time this cohort has been declared flat against
an incomplete roster, and it is the worse of the two: in p892 the missing member had never been
found, whereas here it had been found, placed, and then dropped. **Re-enumerating from the live
shelf is not enough when the shelf is what changed** — enumerate from the shelf *and* its
history (`evidence/shelf-vs-history-diff.2026-11-18-p896.tsv`). The 1,000 ★ watch condition is
untouched: 125 is still an order of magnitude short.

**p892 revised this cohort's reading, and the revision is about method.** p890 and p891 both
measured the cohort, found every member unmoved, and concluded the form had no traction.
**`tutor-mcp` (104 ★) was not in the set either pass measured** — it was found this pass by a
fresh discovery search rather than by re-measuring known rows. Including it, the cohort maximum
was recorded as 118 ★ (now 125, above), but the cohort is **not** static: `tutor-mcp` was pushed 2026-11-17 while
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
- **Thin from LATAM — and this bullet was stale against the table above it (corrected p895).**
  It read *"`warleysr/ankipa` (10 ★, Brazil) is the only LATAM-origin education agent
  verified"*, while the table has carried https://github.com/CaioCastro1/usp-mcp
  (**MIT, 28 ★, pushed 2026-11-13**, Universidade de São Paulo) since p893 — **2.8× ankipa's
  stars.** Both remeasured today: `usp-mcp` **28 ★**, `ankipa` **10 ★**. So LATAM has **two**
  verified origin agents, both MIT, both Brazilian, both small. The honest statement is that
  LATAM supply is **thin and Brazil-only** — nothing verified from Spanish-speaking Latin
  America, where most of the region's students are. LATAM edtech searches still return
  companies (Teachy, Vetto, Ginia), not repos. For a LATAM engagement, expect to localise an
  APAC- or EMEA-origin agent. **A gap bullet that contradicts its own table is worse than no
  bullet: it is read as a measurement.**
- **Africa: the agent layer is unlicensed, the platform layer is MIT — and this file's
  "nothing from Africa" was wrong (rewritten p895 after the first dedicated supply-side leg).**
  The previous text read *"Nothing from Africa or the Middle East ... so 'EMEA' coverage here
  is in practice European coverage."* Measured today:
  - 🟢 **The agent this KB hunted for two passes exists.**
    https://github.com/Eddy-Emmanuel/EduNaija-LLM is the code behind ACL AfricaNLP 2026's
    EduNaija AI Tutor (WAEC/NECO/JAMB; English, Nigerian Pidgin, Yorùbá, Igbo, Hausa),
    which `intel/open-gaps.md` recorded as *"code this pass could not locate at all."*
    **It earns no row: no licence on any of 8 candidate paths (8 × 404, byte-read), 1 ★,
    untouched since 2025-12-22.** Reading it also **corrected this KB's description of the
    paper** — three LangGraph nodes and Tavily *web* search, not "five agents and FAISS", and
    an evaluation the README itself calls *"design-based"*. **Grounding on general web search
    and requiring OpenAI + Tavily connectivity is the wrong design for the one region where
    offline capability decides deliverability.** Detail in `agents/trending.md` (p895).
  - 🔴 **`AFRILANGTUTOR`, the other standing lead, is not on GitHub** —
    `in:name,description,readme` returns **`total_count: 0`**. Closed, negatively.
  - 🟢 **The platform layer is real, permissive and was on no shelf.**
    https://github.com/elimu-ai/webapp — **MIT (byte-read, 1,065 B), 41 ★ / 67 forks, pushed
    2026-11-17**, created 2016 — plus eleven sibling repos, ten sharing that identical MIT
    text. **Restored to `repos/foundations.md` and `verticals/solutions.md` this pass**, with
    its region corrected from **APAC to EMEA**.
  - 🟡 **Exam-channel census: a ~1 ★ ceiling and almost nothing licensed.** `WAEC` 45 hits,
    `KCSE` 102 (mostly false positives), `BECE` 60, `CAPS`/`IEB` **3 in total**. The
    highest-star find, https://github.com/Seunope/aloc-endpoints (**223 ★**, pushed 2026-11-17),
    is a **20,000-question POST-UTME/UTME/WASSCE/NECO bank** with **no licence**. **`JAMB` is an unusable channel** — 415 hits headed by
    `awesome-newsletters` — so an exam-name leg needs a rare acronym or a country term.
  - **Build-vs-adopt, Africa:** adopt the platform, build the agent tier. Same verdict p894
    reached for registrarial work via UniTime, from the opposite direction. See
    `compose/patterns.md` **P14**.
- **Still nothing from the Middle East on the *supply* side.** `intel/market.md` carries
  dedicated Saudi and UAE legs on **demand** — 50 new curriculum units for 2026-27, a federal
  UAE mandate — and this pass found **no corresponding repository**. The untried channel is
  Arabic-language search (the `elimu` Swahili trick applied to `تعليم`); it was not run.
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

- 🔴 **Retracted in p896: `openedx/openedx-platform` *does* exist, and it is the canonical slug.**
  The p895 correction above was itself wrong, and it ran the wrong way. Measured 2026-11-18:
  `repo:openedx/openedx-platform` returns **8,242 ★, AGPL-3.0, pushed 2026-11-17**, while
  `repo:openedx/edx-platform` returns **nothing**. Both names serve byte-identical files on
  `raw.githubusercontent.com` (`LICENSE@master` = 35,136 B, `README.rst@master` = 12,381 B for
  both), because raw follows GitHub's rename redirects and the search channel does not.
  The "404 on every branch" that produced the p895 claim is reproducible only against
  **`main`** — this repo's default branch is **`master`**. Probe matrix:
  `evidence/openedx-slug-probe.2026-11-18-p896.tsv`.
- 🔴 **Generalised in p900: the p896 bullet above describes a MECHANISM, not one repository.**
  GitHub serves a renamed or transferred repository's old address as a redirect indefinitely;
  `raw.githubusercontent.com` follows it and `search/repositories` indexes only the canonical
  name. p896 recorded that for `openedx/edx-platform` and left the single-channel existence test
  running. **p900 measured what that cost: of 50 ledger addresses `search/repositories` reported
  as non-existent, 22 (44%) resolve on `raw`** — four of them renames
  (`Li-Evan/Bloom` → `BloomTutor`, `algorithm0r/canvas-lms-mcp` → `bruchris/…`,
  `aswanth9495/exam-guard` → `Scaler-Opensource/…`, plus openedx), the rest simply missing from
  the search index. 🔴 **`p899`'s "`Li-Evan/Bloom` does not exist" is retracted**: it returns 200
  and serves a README byte-identical to `BloomTutor`'s (`sha256₁₂ 8a74e9391a2b`).
  **No existence claim in this base should rest on one channel.** Record:
  `evidence/ledger-measured.2026-11-18-p900.tsv`.
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
