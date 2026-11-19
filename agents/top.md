---
industry: education
region: Global
updated: 2026-11-19
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

**Latest sweep — `p901`.** `HKUDS/DeepTutor` **60,405** `Apache-2.0`, `THU-MAIC/OpenMAIC`
**43,894** `MIT`, `patchy631/ai-engineering-hub` **41,998** `MIT` (pushed `2026-11-01`),
`withmarbleapp/os-taxonomy` **7,725** 🔴 **`ODbL-1.0`** — a *database* licence on a
curriculum graph, correct for the asset and a trap for anyone who reads the repo as software.
🔴 **`openedx/edx-platform` returned `422` — "resources do not exist" — from
`search/repositories` in this sweep, while `raw.githubusercontent.com` returned `200` on
`master/README.rst`.** That is `p900`'s false-absence class landing on the AGPL anchor of the
whole LMS tier; the two-channel rule caught it. See `agents/trending.md` `901-F3`.

🔴 **`p902` refused three rows that would have landed in this file, and they were fabricated.**
`p901` recommended growing this base by auditing it against a stranger's curated list. `p902` ran
that method over five unaudited indexes. The most topically-relevant one —
`brandonhimpfen/awesome-ai-in-education`, republished byte-for-byte as
`awelist/awesome-ai-in-education` (both `sha256₁₂ 98e1aef693cd`) — has an **"Intelligent Tutoring
Systems" section in which all three entries are unusable**: `CTAT/CTAT` and
`tutoringkit/tutoringkit` **do not exist on any channel** (`404` on every `raw` path, `422` on repo
search, and for `tutoringkit` no such owner), and `github.com/khan` is an **owner page** described as
*"reference architectures and pedagogical prompt structures"*. The third fabricated slug,
**`CAI-BKT/pyBKT`, is a wrong-owner variant of `CAHLR/pyBKT` — which this base already holds, with a
byte-read MIT grant** — so an importing pass would have published a dead link beside the working row
for the same software. 🟢 **Nothing from that list entered this file.** The existence gate this
implies is `902-G2`; the full audit is `agents/trending.md` `902-F2` and
[the record](../evidence/curated-index-fabrication.2026-11-18-p902.tsv).

🟡 **`p902` also found the first repository this base can prove is real and cannot measure.**
`mwouts/jupytext` returns `raw` `200` with an `MIT License` title line and `422` from
`gh api search/repositories`, which is this base's only star channel. It is published in
`repos/foundations.md` with **stars recorded as `unmeasurable`, not estimated** — see `902-G3` for
the appendix change that makes that a first-class value.

**Latest sweep — `p909`, and it is the first census of *every* address in this file rather than a
cohort.** All **345** distinct repository addresses across this file, `repos/foundations.md` and
`verticals/solutions.md` were probed on both channels: **343 resolved**, 1 was a metasyntactic
artefact of the gate rather than a row (`909-G3`), and 1 returned `NORESOLVE` on a 9-path ladder
**while being alive** — `projectfedena/fedena`, `404` on `README.md`/`.gitignore`/`LICENSE` and
`200` on `Rakefile` (`909-F1`). 🔴 **The star-unmeasurable class `p902` opened with one
repository is seven**: `darl-genai/instructional_agents`, `mitodl/open-learning-ai-tutor`,
`mwouts/jupytext`, `digitalcredentials/learner-credential-wallet`, `longsightgroup/qti3`,
`openolat/qtiworks`, `tokenaii/horus-taleeq-0.2b-base` — every one `raw` `200`, every one `422`
from the only star channel **when queried individually**. They keep their rows and **none gets an
estimate**. 🔵 **Both channels now have a measured failure direction**, which is why the
two-channel rule is load-bearing rather than belt-and-braces: `fedena` is search-measurable and
raw-unresolved; those seven are raw-alive and search-unmeasurable.

🟢 **The shelf's licence posture, measured for the first time (337 addresses the search channel
could read):** MIT **151**, Apache-2.0 **65**, BSD-3-Clause 13, ISC 3 → **232 permissive =
68.8%**. `NOASSERTION` **29** (8.6%, byte-read required — `906-G1` showed that field errs in
*both* directions), AGPL-3.0 26, **`NONE` 18**, GPL-3.0 16, LGPL-3.0 4, GPL-2.0 3, ECL-2.0 3,
MulanPSL-2.0 3, and ODbL-1.0/CC0-1.0/CC-BY-4.0 one each — 🟡 **those last three are data and
content licences, not software grants.** 🔴 **23.3% of this shelf is copyleft or carries no grant
at all**, which turns this base's long-standing impression that education's open supply is
licence-trapped into a measured share.

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
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 60,478 | 2026-11-18 | Agentic personalised tutoring grounded in the student's own material, with persistent learning history. Hit #1 on GitHub trending 28 Oct 2026; first released Dec 2025. Paper: arXiv 2604.26962. **The single largest open education agent in existence.** 🔴 **Not reproducible from its own manifests (measured p905):** `requirements.txt` is a 104-byte `-r` pointer into `requirements/full.txt`, which fans out to 19 generated `requirements/modules/*.txt` files; **74 unique packages, 1 exactly pinned** (79 `>=`, 36 `<`). Vendoring it at a SHA pins the source and not the dependency set. 🔴 Its `LICENSE` is a hand-edited Apache-2.0 (`560-D`) and will trip a byte-identity scanner. | APAC — HKU Data Intelligence Lab |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | 43,899 | 2026-11-18 | Multi-agent AI classroom: agents generate slides, quizzes and project-based activities and grade quiz answers. `v1.4.2` (2026-11-09) added course-level undo for manual edits and agent runs. Relicensed to MIT at `v0.3.0`, Jun 2026. 🔴 **Not reproducible from its own manifests (measured p905):** `package.json` declares **178 npm packages** (145 prod + 33 dev) with no lockfile on any path probed. | APAC — Tsinghua University |
| **LearnHarness** | https://github.com/amosblomqvist/learnharness | **AGPL-3.0** | 10,213 | 2026-11-12 | Desktop agent harness that *measures* what the learner understands before it teaches: probe → dependency-map the route to the goal → teach one reasoning step at a time → separate retrieval-practice sessions, all carried across sessions by a persistent knowledge graph. **Added p893. Created 2026-10-16 — 0 → 10,002 ★ in 27 days, the fastest growth this KB has recorded for any education repo**, and now the third-largest open education agent in existence. **AGPL-3.0, byte-read from `LICENSE@main`. Not usable in a closed derivative** — read it as the reference design for learner-state modelling, the capability every other tutor in this table lacks. No published learning-outcome study; users report being tested before being taught. | Global |
| **frametell** | https://github.com/sitor-ai/frametell | **AGPL-3.0** | 513 | 2026-11-12 | Turns source material into explainer videos via an "AI director" agent. Local-first and model-agnostic. **Added p893.** The only open *content-production* agent in this table — courseware generation rather than tutoring. AGPL. | Global |
| **ai-shifu** | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | 2026-11-18 | Author a course by typing it: the AI delivers the teaching and answers questions inside the flow the author scripted. **Added p893.** Permissive, pushed today, and the clearest open example of *authored* AI teaching — the script constrains the model, which is the control structure Oklahoma-style "no AI-only" rules actually require. | APAC |
| **Moodle-MCP** (Faixiang) | https://github.com/Faixiang/Moodle-MCP | MIT | 208 | 2026-11-01 | Zero-dependency MCP server over the Moodle Web Service API: courses, assignments, quizzes, deadlines, files. **Read-only by design.** **Added p893 — the first Moodle MCP server this table has ever carried**, which was a hole given Moodle is the most-installed LMS on earth. Ships a companion agent skill, https://github.com/Faixiang/Moodle-Course-Watch (MIT, 0 ★), that diffs new coursework and lists what is still unsubmitted. README localised into 10 languages. | APAC |
| **edumcp** | https://github.com/aieducations/edumcp | Apache-2.0 | 155 | 2025-05-05 | An attempt to standardise MCP for education applications. **Added p893 as a cautionary entry: 155 ★ and untouched since May 2025.** The idea was early and right; the project is dormant. Read the protocol sketch, do not depend on it. | Global |
| **gen-mentor** | https://github.com/GeminiLight/gen-mentor | **CC0-1.0** | 137 | 2026-10-23 | Reference implementation for *GenMentor* (WWW '25 oral): a multi-agent framework for goal-oriented, skill-gap-aware learning — it infers the gap between the learner's current skills and a target role, then plans content against it. **Added p893.** **Licence is CC0-1.0, byte-read** — a public-domain dedication, not a software licence, so it carries no patent grant and no warranty disclaimer. Legally the most permissive row here and the least conventional; have counsel confirm before shipping it. | APAC |
| **Mentingo** | https://github.com/Selleo/mentingo | MIT | 109 | 2026-11-18 | Self-hosted **AI-native LMS** with a built-in AI mentor and role-play, white-label and multi-tenant, Postgres + pgvector, one-click AWS Marketplace deploy. **Added p893.** Listed here *and* in `verticals/solutions.md` because it is genuinely both. **Its significance is the licence: an MIT LMS.** This KB's first structural finding is that the platforms clients run are copyleft — Mentingo is the counter-example, and therefore the shortest route to a closed, branded derivative. Corporate L&D and compliance training, not K-12. | EMEA — Poland |
| **canvas-mcp** (Sachdev) | https://github.com/vishalsachdev/canvas-mcp | MIT | 334 | 2026-11-18 | MCP server exposing Canvas LMS — courses, assignments, submissions — as agent tools. | North America — USA |
| **BloomTutor** | https://github.com/Li-Evan/BloomTutor | MIT | 319 | 2026-11-17 | Tutor that structures interaction around Bloom's taxonomy levels. | APAC |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | 282 | 2026-11-17 | Intelligent tutoring system with open problem banks and tutoring-effect instrumentation; built for A/B-testable learning research. | North America — UC Berkeley |
| **molly554/whiteboard-ai-tutor** | https://github.com/molly554/whiteboard-ai-tutor | MIT | 262 | 2026-11-17 | Whiteboard tutor with animated lessons and interactive playback. Created after Aug 2026 — one of the fastest-growing new entrants. | Global |
| **OpenPronounce** | https://github.com/OpenPronounce/OpenPronounce | MIT | 224 | 2026-11-09 | Open pronunciation assessment — the language-learning niche where open source is genuinely competitive with commercial APIs. 🔵 **p900: this base logged `halleck45/openpronounce` 5× in its `logged-not-shelved` ledger and nearly promoted it as a second row.** It is a **transfer alias of this repository** — byte-identical `README.md` (`sha256₁₂ a005d079f571`) — caught by the duplicate-subject gate before publication. **The rename mechanism that causes false ABSENCES in the ledger causes false DUPLICATES on the shelf**; both need the canonical name resolved first. | Global |
| **OpenTutor** | https://github.com/zijinz456/OpenTutor | MIT | 181 | 2026-11-17 | Open tutoring agent. | APAC |
| **canvas-mcp** (Cheng) | https://github.com/boyuchengz/canvas-mcp | MIT | 118 | 2026-10-27 | **Read-only** MCP server connecting Claude/ChatGPT to Canvas LMS. A second, independent `canvas-mcp` — read-only by design, which is the safer default for a student-data pilot. | North America |
| **Open TutorAI (CE)** | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 119 | 2026-06-26 | Community edition of a self-hostable tutor platform. Licence text carries an "All rights reserved" header over a BSD-style grant; SPDX confirms BSD-3-Clause. | EMEA |
| **japanese-tutor-mugi** | https://github.com/brian901106/japanese-tutor-mugi | MIT | 105 | 2026-10-28 | Second-language conversation tutor with a **Chinese-language interface teaching Japanese** — the tutor UI and the target language are different, and neither is English. Its design contract is the reusable part: the LLM returns **structured JSON Schema** output with the Japanese line and the native-language hint as *separate fields*, rendered by partial-JSON parsing so the reply streams as it arrives. **Added p898**, MIT byte-read (`main/LICENSE`, 1,068 B, `sha256₁₂ b349f14f3e8e`). The only repo in this table implementing the separate-fields contract. | APAC |
| **belajar-ngoding-byGanzu** | https://github.com/itsme-ganzu/belajar-ngoding-byGanzu | MIT | 66 | 2026-10-27 | **Bahasa Indonesia** Python-from-zero course with a personal AI tutor that drills reasoning rather than handing over answers. **Added p898**, MIT byte-read (`main/LICENSE`, 1,062 B, `sha256₁₂ 410186335243`); placed **APAC** on 30 Bahasa markers in a stripped README. 🔵 **The first Indonesian-language row in this table** — Indonesia is the fourth-largest school system in the world, and this is the only vernacular-Indonesian education repo the KB has verified. Small and young; read it as evidence of where vernacular supply is appearing, not as substrate. | APAC |
| **tutor-mcp** | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 107 | 2026-11-17 | MCP server that turns any LLM into an Intelligent Tutoring System — the ITS loop (learner model, next-item selection, graduated hints) exposed as **tools** rather than as an application. **Added p892.** The most actively developed member of the "tutor as an agent skill" cohort, and it was missing from the cohort p890/p891 measured — see `agents/trending.md`. | Global |
| **EduAgent** (`AI_Tutor_Release`) | https://github.com/Zenglian990/AI_Tutor_Release | MIT | 93 | 2026-11-10 | RAG tutor built specifically for **K-9** (grades 1–9), self-described as the first open-source RAG tutor targeted at that band in China. **Added p892.** Notable because it is **age-banded by design** — a product requirement under the UAE's under-13 prohibition and several US state statutes — and because it is retrieval-over-curriculum, not training-on-student-data. | APAC — China |
| **TeachMeCoding** | https://github.com/liangxiao777/TeachMeCoding | Apache-2.0 | 83 | 2026-10-30 | Local-first AI coding tutor: personalised roadmaps, lessons, hands-on practice with execution. | APAC |
| **aula** | https://github.com/luumlabs/aula | AGPL-3.0 | 67 | 2026-11-17 | Turns notes, slides and past exams into lessons. **AGPL — not usable in a closed derivative.** | Global |
| **Claw-ED** | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | 2026-09-19 | Local-first AI teaching assistant: editable lesson drafts, student materials and slides, generated from the teacher's own curriculum with a model of their choice. Self-described teacher-reviewed beta. **Teacher-facing**, which this table is otherwise thin on, and **local-first + bring-your-own-model**, which is the posture EMEA sovereignty procurement now asks for. **Caveat: trending on stars through Oct 2026 while its last commit is 2026-09-19** — read it as a design reference, not a dependency. Licence byte-read from `LICENSE@main` (`Copyright (c) 2026 EDUagent Contributors`). | Global |
| **moodle-mcp** | https://github.com/G36maid/moodle-mcp | MIT | 30 | 2026-10-20 | Second Moodle MCP server, and the **read-write** counterpart to `Faixiang/Moodle-MCP`: it operates courses, assignments, forums and grades, and serves files as markdown. **Added p893.** The read-only/read-write split across two MIT servers is the useful part — pilot on the read-only one, graduate to this when the client accepts write scope. | APAC — Taiwan |
| **usp-mcp** | https://github.com/CaioCastro1/usp-mcp | MIT | 28 | 2026-11-13 | Portuguese-language MCP server over Universidade de São Paulo's student systems: e-Disciplinas (Moodle) coursework and deadlines, course catalogue, refectory menus. **Added p893.** **This is the second LATAM-origin education agent this KB has verified, and at 28 ★ it is nearly 3× the first** (`warleysr/ankipa`, 10 ★) — see `agents/trending.md` for what that does to the standing regional finding. | LATAM — Brazil |
| **wassce-benchmark** | https://github.com/acheamponge/wassce-benchmark | MIT | 4 | 2026-04-07 | Benchmark evaluating open LLMs on the **WASSCE**, the school-leaving exam about two million West Africans sit each year. **Added p893.** Not an agent — an eval gate, like `pedagogy-benchmark`. **It is the only African-curriculum open evaluation asset this KB has found**, and it is the thing to measure against before any West African claim. Licence byte-read MIT. | EMEA — Africa |
| **wenflow** | https://github.com/wenflow-org/wenflow | MIT | 72 | 2026-11-12 | Writing-feedback workflow agent. | APAC |
| **wiki-rag** | https://github.com/moodlehq/wiki-rag | BSD-3-Clause | 54 | 2026-06-15 | **Moodle HQ's own** RAG service over Moodle documentation. Low stars, high significance: the Moodle organisation shipping a first-party retrieval agent. | EMEA — Moodle HQ |
| **ECNU EduWork** | https://github.com/ECNU/EduWork | MulanPSL-2.0 | 381 | 2026-11-18 | Education workflow agent. **Licence note:** Mulan Permissive Software License v2 is OSI-approved and permissive, but it is not MIT/Apache — check your client's approved-licence list. | APAC — ECNU, China |
| **socratic-workshop** | https://github.com/smashburger-dev/socratic-workshop | MIT | 24 | 2026-10-28 | Socratic tutoring delivered **as a skill inside a coding agent** (Claude Code / Codex): learn a topic by explaining it. | Global |
| **ls1intum/edutelligence** | https://github.com/ls1intum/edutelligence | MIT | 17 | 2026-11-17 | Umbrella suite of AI services for the Artemis learning platform. **The production-grade reference for "AI integrated into a real LMS"** — star count badly understates it. | EMEA — TU Munich |
| **pedagogy-benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | MIT | 13 | 2026-11-16 | Benchmark for the *pedagogical* ability of LLMs, as distinct from subject knowledge. An eval gate, not an agent. | Global |
| **Pyris** | https://github.com/ls1intum/Pyris | MIT | 12 | 2026-06-03 | LLM microservice behind Artemis's *Iris* tutor. Clean separation of the LLM tier from the LMS — the pattern to copy when the model layer must stay swappable. | EMEA — TU Munich |
| **ankipa** | https://github.com/warleysr/ankipa | MIT | 10 | 2026-11-07 | Pronunciation assessment as an Anki add-on; the "agent inside an existing study tool" pattern. 🔴 **Claim corrected `p907`: this row read "the only LATAM-origin education agent verified in this pass", which was already stale against `usp-mcp`, `bncc-mcp`, `mooose`, `GenPrompt Pre-ICFES 11` and three further rows in this same table.** `p904` corrected the LATAM *gap bullet* and left the claim inside this row standing. Counted this pass: **seven** LATAM-origin rows stood in this table before `p907`, across **two** countries (Brazil 6, Colombia 1) — **eight across three** with the Peru row added below. | LATAM — Brazil |
| **EDU AI Agent Suite** | https://github.com/virtualryder/edu-ai-agents | MIT (SPDX: NOASSERTION; licence text reads MIT) | 4 | 2026-10-10 | Eight reference agent workflows with deny-by-default authorisation, student-PII masking, human-in-the-loop enforcement and tamper-evident audit, aligned to FERPA, COPPA, IDEA/504 and ADA Title II. **Grading uses a deterministic rubric service, not an LLM** — which is what makes it legally usable in several US states. Targets Amazon Bedrock. Tiny and new; valuable as an architecture, not as a dependency. | North America |
| **ai-tutor-agent** | https://github.com/vulinh1704/ai-tutor-agent | MIT | 0 | 2026-11-16 | FastAPI + LangGraph tutoring starter: Socratic hints, rubric grading, session memory, offline demo mode; checks every draft for answer leaks. Zero stars — a skeleton to read, not a dependency. | APAC — Vietnam |
| **Socratic-Education-System** | https://github.com/HowieWang1121/Socratic-Education-System | MIT | 137 | 2026-05-03 | Socratic-method tutoring system whose README argues education is a right to be guaranteed rather than an obligation, and targets students without access to paid tutoring. **Restored p896** — it was carried on this shelf and deleted by the 2026-11-18 cleanup without appearing in that pass's own list of removals. At 137 ★ it is the eighth-largest education-native agent here. **Caveat: last push 2026-05-03**, so read it as a design reference. | APAC — China |
| **education-skills** | https://github.com/flysheep-ai/education-skills | MIT | 126 | 2026-01-30 | Collection of education-specific **agent skills** (teaching, tutoring and study-support tools packaged for a coding agent). **Restored p896.** 🔴 **The standing claim attached to this row — that it is the largest member of the "tutor as an agent *skill*" cohort, which "two passes recorded as topping out at 118 ★" — was refuted in p899 and is retained here only to mark the correction.** Measured 2026-11-18, the skill cohort runs to **`book-to-skill` at 38,369 ★**, with `Papermorph` (1,775), `learn-from-materials` (1,455), `Claudemy` (706) and `universal-examprep-skill` (396) all above it. The ceiling was an artefact of a star-ranked keyword leg, not a property of the cohort — see `898-G2` in `intel/open-gaps.md`. Idle since 2026-01-30. | APAC — China |
| **civil-ai** | https://github.com/zhangl1001/civil-ai | MIT | 41 | 2026-11-08 | **Local-first** adaptive tutoring agent reference implementation for **iOS and Web**, applied to civil-service exam preparation. **Restored p896.** Two things make it worth a row despite 41 ★: it is one of very few open tutors with a **native mobile** target, and local-first inference is the posture that satisfies California AB 1159 and EMEA sovereignty procurement without a data-processing argument. | APAC — China |
| **book-to-skill** | https://github.com/virgiliojr94/book-to-skill | MIT | 38,398 | 2026-11-08 | Turns a technical book, document folder or PDF into a packaged agent skill you can then study against. **Added p899 — and it is the third-largest repository in this entire KB**, behind only DeepTutor and OpenMAIC and nearly 4× LearnHarness. MIT byte-read (`LICENSE.md@master`, 1,068 B, `sha256₁₂ be9b04bccfb4`). 🔴 **It sat in this KB's own `logged-not-shelved` ledger with 28 recorded mentions and no row.** Read it as the canonical *courseware-compilation* pattern: the source material becomes the skill, so the model is constrained by the book rather than recalling it. | Unplaced — see note below |
| **Papermorph** | https://github.com/DozenTwelve/Papermorph | MIT | 1,783 | 2026-11-16 | Turns books and papers into animated, narrated, interactive web explainers. **Added p899.** MIT byte-read (`LICENSE@main`, 1,069 B, `sha256₁₂ 41857092247a`). 🟡 **Procurement caveat: the copyright line reads `Copyright (c) 2026 TedKaczynski`** — a pseudonym. The grant is valid on its face, but there is no identifiable holder to obtain a CLA, warranty or indemnity from, which several enterprise clients will refuse. Read the technique, vendor the code knowingly. | Global |
| **Study-Mate** | https://github.com/Miaotofu01/Study-Mate | MIT | 1,490 | 2026-11-17 | Study companion that plans a route through a subject, teaches it, and builds projects alongside the learner. **Added p899.** MIT byte-read (`LICENSE@main`, 1,064 B, `sha256₁₂ dc1997d82189`). Placed APAC on a stripped-README CJK score of **1,490 with spread 0.971** — dispersed prose, not a language switcher (see `compose/code/p899-origin-strip/`). | APAC |
| **learn-from-materials** | https://github.com/dmoshehun-prog/learn-from-materials | MIT | 1,455 | 2026-10-19 | Turns PDFs, books and papers into interactive learning webpages. **Added p899.** 🔵 **Lineage finding:** its `LICENSE.md` carries **two** copyright lines — *"Copyright (c) 2025 virgiliojr94"* then *"Copyright (c) 2026 learn-from-materials"* — so it is an acknowledged derivative of the `book-to-skill` row above. The two together are 39,824 ★ of one lineage that this KB had never shelved. | Global |
| **get-it** | https://github.com/beltromatti/get-it | Apache-2.0 | 1,169 | 2026-06-29 | *"Read it. See it. Get it."* — turns study material into visual explanation. **Added p899.** Apache-2.0 byte-read (`LICENSE@main`, 11,359 B, `sha256₁₂ d0622ead9e49`) — **patent grant included**, which no MIT row here carries. Built at **GDG AI Hack Milan 2026**, which is where the EMEA placement comes from (event, not language). **Caveat: last push 2026-06-29, nearly five months idle.** | EMEA — Italy |
| **Claudemy** | https://github.com/assafkip/claudemy | MIT | 708 | 2026-10-29 | Self-described open-source alternative to Udemy/Coursera, built as an agent skill. **Added p899.** MIT byte-read (`LICENSE@main`, 1,069 B, `sha256₁₂ 262b47ee1fff`, *"Copyright (c) 2026 Assaf Kipnis"*). | Global |
| **universal-examprep-skill** | https://github.com/ZeKaiNie/universal-examprep-skill | MIT | 397 | 2026-10-27 | Exam-cram coach with cross-session memory and **source-traced handouts specifically to suppress hallucination** — every claim is tied back to the uploaded material. Runs as a skill in Claude Code, Cursor, Codex or Antigravity. **Added p899.** MIT byte-read (`LICENSE@main`, 1,065 B, `sha256₁₂ 21f44893f051`). 🔴 **This KB's own ledger records it logged 34 times and never shelved** — the single most-logged unshelved row with a verified permissive grant. | APAC |
| **deep-student** | https://github.com/helixnow/deep-student | **AGPL-3.0** | 321 | 2026-11-18 | Local-first AI learning workbench. **Added p899.** AGPL-3.0 byte-read (`LICENSE@main`, 34,532 B, `sha256₁₂ 894342980454`). **Not usable in a closed derivative**; local-first is the posture EMEA sovereignty and California AB 1159 procurement ask for, so read it as the reference architecture for on-device study tooling. | Global |
| **freelingo** | https://github.com/artcc/freelingo | **AGPL-3.0** | 292 | 2026-11-17 | Self-hosted language learning with **local or cloud LLMs, CEFR-aligned study plans** and a conversation tutor. **Added p899.** AGPL-3.0 byte-read (`LICENSE@main`, 34,514 B, `sha256₁₂ ea94d5765c59`). CEFR alignment is the part to reuse: it is the European reference framework a public-sector language contract will specify by name. AGPL. | Global |
| **universal-diagnostic-tutor-skill** | https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill | MIT | 280 | 2026-11-11 | **Diagnosis-first** tutor for STEM and CS — it establishes what the learner has got wrong before selecting what to teach, with no mode switching. **Added p899.** MIT byte-read (`LICENSE@main`, 1,102 B, `sha256₁₂ a9ca00bcc7a5`). Placed APAC on CJK **1,564, spread 0.964**. The diagnosis-first contract is the same capability `LearnHarness` is credited with, at 1/36th the size and under MIT rather than AGPL. | APAC |
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
| **anki-mcp-server** | https://github.com/ankimcp/anki-mcp-server | MIT | 568 | 2026-11-07 | **Added p900 (logged 10×).** MCP server over **Anki**, putting a learner's real spaced-repetition deck behind an agent — read, create and schedule cards. 🔵 Pairs with `fsrs4anki-helper` in `repos/foundations.md`: the scheduler and the agent seam are both permissive | Global |
| **Educhain** | https://github.com/satvik314/educhain | MIT | 387 | 2026-05-29 | **Added p900 — and this base has NAMED it since its second education cycle without ever giving it a row (logged 14×, the 4th-most-logged address in the rebuilt ledger).** Generates MCQs, lesson plans and full courses from source content, including YouTube. 🟡 **Idle since 2026-05-29** — a stable library, not a tracked upstream | APAC — India |
| **bncc-mcp** | https://github.com/dfdb76/bncc-mcp | **MIT** (byte-read `main/LICENSE`, 1,218 B) | 14 | 2026-07-24 | **Added p904, from the Portuguese-language channel no pass had run.** MCP server exposing the **1,721 learning objectives of Brazil's Base Nacional Comum Curricular** as agent tools, so a tutor or lesson-planner can look up an official curriculum code instead of recalling it. 🔴 **Its SPDX field reads `NOASSERTION`; the byte-read grant is plain MIT** — one of three `NOASSERTION` corrections in this cluster (`agents/trending.md` `904-F4`). 🔵 **Why it earns a row at 14 stars:** it is the *second, independently maintained* MCP server over the same national curriculum (the first ships inside `bncc-dev/bncc-pacotes`), which is the two-maintainer split this KB recorded for Moodle in `intel/trends.md` **T13**, now arriving on a curriculum instead of an LMS. Pair it with `bncc-dev/bncc-dados` (the dataset, `repos/foundations.md`) and the hallucination gate in `compose/patterns.md` **P23**. 🟡 Last push 2026-07-24 — read it as a working reference, and pin a commit. | **LATAM — Brazil** |
| **canvas-lms-mcp** | https://github.com/bruchris/canvas-lms-mcp | **MIT** (`LICENSE@HEAD`, 1,069 B, byte-read p900) | 10 | 2026-11-17 | **Added p900.** **165 tools** over Canvas — courses, assignments, submissions, gradebook history, rubrics, New Quizzes (LTI), enrolments. 🔴 **Reached via a rename:** this base logged it as `algorithm0r/canvas-lms-mcp` 5×, which `search/repositories` reports as non-existent; the canonical owner is `bruchris` (see `900-G2`). 🔵 The deepest permissive agent seam onto AGPL Canvas in this file | Unplaced |
| **mooose** | https://github.com/matheussilvano/mooose | **Apache-2.0** (byte-read `main/LICENSE`, 11,358 B) | 5 | 2026-11-17 | **Added p904.** Open-source **ENEM essay grader** built on LangGraph, and the clearest *bring-your-own-model* design in this table: it ships adapters for OpenRouter (free tier), Gemini, Groq, **Ollama**, OpenAI and Claude, so the inference provider is a deployment decision rather than an architectural one. 🔵 **That is exactly the property `intel/trends.md` T6 says EMEA and LATAM procurement is starting to require** — sovereign or local inference without a rewrite — implemented by a two-person project rather than a platform vendor. Grades against the ENEM's five official competencies, which makes it a worked example of rubric-bound grading rather than free-text feedback. Apache-2.0, so it can enter a closed derivative. 🟡 18 open issues and 0 forks at 5 ★: a reference implementation and a starting point, not a dependency. | **LATAM — Brazil** |
| **GenPrompt Pre-ICFES 11** | https://github.com/CREARED-EDU-CO/GenPrompt-Pre-ICFES-11 | **AGPL-3.0** (byte-read `main/LICENSE`, 34,523 B) | 4 | 2026-09-19 | **Added p904 — the first Colombia-origin entry in this table.** Generates large numbers of distinct exam-preparation prompts for **Saber 11 / ICFES**, Colombia's national secondary-school examination, for use against any chatbot. 🔵 **Read it as the cheapest possible form of the national-exam pattern:** no model, no hosting, no data processing — prompt templates bound to a national assessment, which is why it works in schools with no AI budget at all. Maintained by an education organisation (`CREARED-EDU-CO`), not an individual. 🔴 **AGPL-3.0: deployable and forkable, not embeddable in a closed product.** | **LATAM — Colombia** |
| **Horus Taleeq 0.2 Base** | https://github.com/tokenaii/horus-taleeq-0.2b-base | **MIT** (`LICENSE@HEAD`, 1,079 B, byte-read p900) | *not in the search index* | — | **Added p900, and it answers a regional gap this base declared on the wrong side of itself.** An **Arabic-only small language model** — training code and reproducibility record — from **TokenAI**, *"a startup and nonprofit organization focused on open Arabic AI research"*. Scoped deliberately: base model only, no chat adapters, no teacher outputs, no private data. 🔵 `p899` recorded *"no supply-side leg for Africa or the Middle East"*; this was **logged 5× in its own ledger at the time**. 🟡 A base model is a starting point for continued pretraining, not a deployable tutor | EMEA — Middle East |
| **Mishkat** (`GT-MISHKATKIDS`) | https://github.com/SalehGNUTUX/GT-MISHKATKIDS | **GPL-3.0** | 3 | 2026-11-18 | Arabic-language learning system for ages 4-10 built on **inverted pedagogy: the child is the teacher**, re-teaching an amnesiac robot whose memory lights up as each lesson lands. The README names the mechanism outright — the **proteges effect**, *"we learn most deeply what we teach to others"* — and pairs it with a deliberate emotional design in which the child is the confident expert and the robot is the one who errs. **Added p903, from the Arabic-language channel this file had listed as untried.** 🔵 **Its delivery properties are why it earns a row at 3 stars: fully local, works offline, *no AI at runtime*, no cost, and the child's data never leaves the device** — shipped today as installable PWA, GNU/Linux AppImage/DEB/RPM and Android APK. That is the exact design this file criticises `EduNaija-LLM` for missing, and it is the only MENA-origin education agent found with a licence on any path. **GPL-3.0 (byte-read, 34,819 B): a reference implementation and a deployable system, not a component for a closed derivative.** Scoping caveat: the content sits in an explicit Islamic doctrinal frame with Qur'anic recitation as a first-class module — a feature for Gulf and North African work, a decision to make everywhere else. The architecture is portable independently of that content; see `compose/patterns.md` **P22**. | **EMEA — MENA, Arabic-language** |
| **AI-Skill Corretor de Redação ENEM** | https://github.com/migueldsants/AI-Skill-Corretor-Redacao-ENEM | **MIT** (byte-read `main/LICENSE`, 1,082 B) | 3 | 2026-09-07 | **Added p904.** Essay grading published as an **agent skill** rather than an application — the form this file tracks under *the tutor as an agent skill* below, appearing for the first time in Portuguese and bound to a national examination. By the same maintainer as `OpENEM` (`verticals/solutions.md`), which makes the pair a worked example of the same team shipping a platform and a skill over one curriculum. MIT, so it composes into a closed derivative. 🟡 3 ★, 0 forks: demo-kit material. | **LATAM — Brazil** |
| **GabirIA** | https://github.com/suellenferraz/Projeto-GabirIA | **MIT** (byte-read `main/LICENSE.md`, 1,085 B) | 3 | 2025-05-24 | **Added p904.** Study assistant for ENEM preparation. Included because its licence is byte-read MIT and its subject is a national examination; excluded from any recommendation because it is **18 months without a push** and its **README returns `404` on all three paths tried**, so the repository is readable only as code. 🟡 **Carried as evidence of the channel's shape, not as a starting point** — see `agents/trending.md` `904-F7`. | **LATAM — Brazil** |
| **nengdou AI review helper** | https://github.com/yinuoguan/nengdou-ai-review-helper-web | 🔴 **Apache-2.0 byte-read — GitHub SPDX says `MulanPSL-2.0`. Channels disagree.** (`main/LICENSE`, 11,356 B, `sha256₁₂ 43070e2d4e53`, opening `Apache License / Version 2.0, January 2004`) | 193 | 2026-04-29 | 能豆 — multi-subject AI homework-grading system for Chinese schools (Chinese, English, maths), automatic marking plus written feedback, on Vue 3 + Nest.js + MongoDB + DeepSeek. **Added p906, and it is the star ceiling of the entire Mandarin education channel.** 🔵 **The licence disagreement inverts the procurement answer and is the reason this row leads the cohort:** an SPDX-driven scanner routes it to legal review as Mulan PSL v2 (OSI-approved, permissive, but absent from many enterprise approved-licence lists), while the actual grant is **Apache-2.0 with its patent grant**, which is on every such list. Its licence file is byte-identical to `thinking-map`'s, which SPDX labels correctly. **Read the field, reject the software; read the bytes, ship it.** See `906-F4`. | APAC — China |
| **xl-frontend** (小鹿老师) | https://github.com/QwenStorm/xl-frontend | MIT (byte-read `master/LICENSE`, 1,060 B, `sha256₁₂ 3b0284114591`) | 50 | 2026-04-07 | K-12 AI education platform: AI paper composition, automatic homework marking, **essay marking**, OCR recognition of handwritten work and learning analytics, on Spring Boot + Vue 3. **Added p906.** The essay-marking and OCR pair is the part this table otherwise lacks — every other grading row here marks code or structured answers, not free prose on paper. 🟡 **Caveat: created and last pushed the same day, 2026-04-07** — a published snapshot, not a maintained project. Read the pipeline. | APAC — China |
| **tizhuang-agent-skills** | https://github.com/weishao2/tizhuang-agent-skills | MIT (byte-read `main/LICENSE`, 1,077 B, `sha256₁₂ 881348270e41`) | 42 | 2026-11-11 | 题庄 — packaged **agent skill** over a claimed 20-million-item K-12 past-paper bank: free registration, question sampling, textbook/chapter/knowledge-point retrieval, practice tests and AI paper composition. **Added p906.** 🔵 **Its significance is the shape, not the size: this is the question-bank-as-a-skill pattern**, the assessment counterpart to `book-to-skill`'s courseware compilation — the bank is the constraint, so the model selects items rather than inventing them. 🟡 The 20M figure is the project's own claim and is **not independently verified**; the bank is a hosted service behind the skill, so treat availability and terms as a dependency on a third party, not as something the MIT grant covers. | APAC — China |
| **econai-agent-platform** | https://github.com/ai-lingnan/econai-agent-platform | **AGPL-3.0** (byte-read `master/LICENSE`, 34,522 B, `sha256₁₂ 4df3c306ddda`) | 41 | 2026-07-17 | Economics and finance **course platform** where teachers publish assignments, students submit, and **two AI agents review each submission in parallel** before an automatic mark is issued. **Added p906.** 🔵 **The dual-agent parallel review is the reusable control:** two independent passes over the same work give a disagreement signal, which is the cheapest available proxy for grading reliability and the thing a human-in-the-loop rule can actually trigger on. **AGPL-3.0 — not usable in a closed derivative**; read it as the reference design. | APAC — China |
| **k12-smart-teacher** | https://github.com/shellery1988/k12-smart-teacher | MIT (byte-read `main/LICENSE`, 1,073 B, `sha256₁₂ 4c5f6e74a09b`) | 16 | 2026-06-29 | 智能老师辅导系统 — K-12 homework marking, **wrong-answer analysis, and generation of fresh analogous practice from the specific error made** (举一反三). **Added p906.** The error→targeted-practice loop is the pedagogically load-bearing step and is missing from every other grading row in this table, which stop at a mark and a comment. Small and MIT; read it as the loop, not as substrate. 🟡 Idle since 2026-06-29. | APAC — China |
| **ai-smart-homework-review** | https://github.com/wenliu3/ai-smart-homework-review | **MulanPSL-2.0** (byte-read `main/LICENSE`, 9,246 B, `sha256₁₂ 2a7ffa7fcf2e`, Chinese text, `license.coscl.org.cn/MulanPSL2`) | 11 | 2026-09-06 | Full-stack teaching-assistant platform on FastAPI + Vue 3 + LangChain: pluggable multi-model access, AI marking, teaching assistant and **document similarity/plagiarism checking**. **Added p906.** 🟡 **Licence note — and this row is the honest counterpart to the `nengdou` row above:** here Mulan PSL v2 is what the bytes actually say. It is OSI-approved and permissive, but it is **not** MIT/Apache and the authoritative text is **Chinese**, with the English version explicitly non-controlling on conflict. Check your client's approved-licence list and expect a translation question from counsel. | APAC — China |
| **SchoolConnect** | https://github.com/cculb/schoolconnect | **MIT** (byte-read `p907`, `LICENSE@main`, 1,071 B) | 4 | 2025-12-28 | **Added `p907`, and it is the first *guardian-persona* agent in this table.** Scrapes, stores and analyses a student's academic record from **PowerSchool Parent Portal** into SQLite, and exposes it over an **MCP server** so an agent can answer a parent's questions. 🔵 Every other row here serves a learner, a teacher or an institution; this one serves the **parent**, which is a buyer segment this KB had no supply evidence for. 🟡 Scraping a portal is brittle and may breach the district's terms — read `compose/patterns.md` **P26**'s governance note. Idle since 2025-12-28 | North America |
| **universidad-pacifico-mcp** | https://github.com/andrsnrua/universidad-pacifico-mcp | **ISC** (byte-read `p907`, `LICENSE@main`, 748 B) | 1 | 2026-10-06 | **Added `p907` — the first Peru-origin entry in this table, and it refutes a declared gap.** `p904` recorded *"no Argentine, Peruvian or Central American origin repository in any query"*; this is Peru. MCP server over **Universidad del Pacífico**'s Aula Virtual (Blackboard Ultra, `aulavirtual.up.edu.pe`): **70 tools, 5 prompts**, covering courses, syllabi, announcements, assignments and grades, attendance, a **local library** that extracts text from PDF/DOCX/PPTX/XLSX, and private exports. 🔵 Uses *"el acceso y los permisos de tu propia cuenta"* — no institutional key. Self-declared **"proyecto comunitario no oficial"**. 🔵 It was invisible to `p904` not because the Spanish channel is flat but because its description is Spanish *infrastructure* prose that never says "IA" or "educación" | LATAM — Peru |
| **ExamGuardian** | https://github.com/andbriha/ExamGuardian | **MIT** (byte-read `p907`, `LICENSE@main`, 1,065 B) | 0 | 2026-11-14 | **Added `p907` for its design discipline, not its size**, and it is the most *regulator-ready* proctoring code this KB has read. Self-hosted exam attempts with identity checks, saved answers, camera/screen evidence and **human review**. 🔵 **It separates the two things the EU AI Act cares about: "the academic score is calculated from answers; the integrity verdict is a separate examiner decision"**, and its README states *"an observation is a reason to inspect context, not a calibrated probability of cheating"*. 🔵 It also **enumerates what it does not implement** (automatic integrity scoring, speaker attribution, micro-earpiece recognition, immutable PDF signing). Exam monitoring is high-risk under the AI Act from **2 Dec 2027** — this is the posture `compose/patterns.md` **P4** prescribes, written down by its author. 🟡 Self-described pilot; accuracy and classroom-scale capacity *"require measured validation"* | EMEA |
| **interactive-learning** | https://github.com/geekjourneyx/interactive-learning | **MIT** (byte-read `p909`, `LICENSE@HEAD`, 1,069 B, `sha256₁₂ 02b7dc1969f4`, *"MIT License / Copyright (c) 2026 geekjourneyx"*) | 52 | 2026-04-10 | **Added `p909`, and it was named in this base's log since `p907` with no row in any delivery file** — `908-F1`'s log/delivery divergence landing inside the agent-*skill* cohort that `p896` had already recorded as twice-declared-flat against an incomplete roster. Turns any text, link, document or question into a **verifiable learning path**, then exports a shareable **HTML checkpoint card**. Installed into an existing agent with `npx skills add`, so there is **no front end to build** and the learner already has the client. Its own framing is the sharpest statement of this cohort's thesis on these shelves: *"总结器解决压缩，解决不了误解"* — **a summariser solves compression, not misunderstanding**; it tests whether the learner understood rather than re-explaining. 🟡 Idle since 2026-04-10, and at 52 ★ it does **not** move the cohort ceiling, remeasured this pass at **126 ★** (`flysheep-ai/education-skills`, up from the 125 ★ `p896` recorded). | APAC — China (Chinese-language README) |

🔵 **`80` rows in the table above, re-counted mechanically in `p907`** (`77` at the close of
`p906`; **`p907` added 3** — `SchoolConnect`, `universidad-pacifico-mcp` and `ExamGuardian`, all
three found by **global code search**, an instrument this base had recorded as unusable, and none of
them reachable by any repo-search query because their descriptions never say "AI" or "education".
`universidad-pacifico-mcp` is **the first Peru-origin row** and refutes a `p904` declared gap.) The
`p906` note is kept verbatim below because its lesson about drift is the reason the count is now
derived:

🔴 **`77` rows in the table above, counted mechanically in `p906`; `75` are agents and `2`
(`wassce-benchmark`, `pedagogy-benchmark`) are self-described eval gates rather than agents. The
figure previously stated here was `61`, and it was wrong before `p906` touched this file** — the
table held `71` rows when this pass opened it, so the prose had drifted `10` rows behind the data,
across several passes that each added rows and incremented the sentence by hand. The count is now
derived from the file rather than carried forward; **a pass that adds rows should re-count, not
add.** (**p906 added 6**, every one Mandarin-origin and every one previously logged-not-shelved, from the Chinese-language channel no pass had run: `nengdou-ai-review-helper-web`, `xl-frontend`, `tizhuang-agent-skills`, `econai-agent-platform`, `k12-smart-teacher` and `ai-smart-homework-review`. **This is the first pass to put a Chinese automated-grading cohort on this shelf**, a tier `repos/foundations.md` held as entirely Western; and `nengdou` is the first repository in this KB whose SPDX field is wrong in the *restrictive* direction — see `906-F4`.) (**p904 added 5**, all LATAM-origin, from the Spanish/Portuguese channel no pass had run: `bncc-mcp`, `mooose`, `GenPrompt-Pre-ICFES-11`, `AI-Skill-Corretor-Redacao-ENEM` and `GabirIA`. **This is the first pass to put a Colombia-origin row in this table, and it raises LATAM representation from one row to six.** Six further LATAM repositories were measured and **refused for having no licence on any of 12 byte-read paths** — including `namerico/antigravity-education-kit` at 6 ★, a modular Portuguese-language education agent framework, which is the most interesting thing this pass could not publish. See `agents/trending.md` `904-F7`.) (**p903 added 1** — `GT-MISHKATKIDS`, from the Arabic-language leg this file had carried as untried. That leg also produced Egypt's entire national curriculum as an agent-skill corpus, **and it is not in this table**: `revolover00/Bakloriya-AI-SKILLS` has **no licence on any of 12 byte-read paths**, so the p893 rule — this table carries only what a studio can actually build on — was applied rather than relaxed. It is reasoned about under the agent-*skill* heading below and in `agents/trending.md` `903-F2`.) (**p899 added 18** — the largest single-pass addition this table has made, and *not one of them came from a new web search*: every row above was already in this KB's own `agents/trending.md` history or its `logged-not-shelved` ledger, and was promoted only after a licence byte-read and a star measurement today. See `agents/trending.md` p899 for why that is a finding about this KB rather than about the ecosystem.)

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

## The per-institution LMS bridge (class `T30`) — restored and extended in `p908`

🔴 **Read this heading as a repair notice.** `p908` audited every line in this KB's two trending
logs that uses the words *"Promoted to"* against the file it names. **Of 30 distinct
repo → delivery-file promotion claims, 20 name a repository that is not in the file it was
promoted into.** Six of them were promoted into *this file* by `p798`
(`falkenslab/miyagi`, `nialvape/utn-mcp`, `HyNuwa/UniMCP`, `jamestesting0/tum-mcp`,
`kad-xyz/spbstu-mcp`, `simonseifert/merlin-mcp`) and were absent from it until this pass. The
cause is measured, not guessed: the `2026-11-17` (`p871`) rewrite of this file carried
**783 distinct repository addresses in, and 118 out**. Record:
[`promotion-audit.2026-11-19-p908.tsv`](../evidence/promotion-audit.2026-11-19-p908.tsv),
[`delivery-attrition.2026-11-19-p908.tsv`](../evidence/delivery-attrition.2026-11-19-p908.tsv).

Every row below was verified in `p908` on the two channels this base trusts
(`907-F2`): the grant was **byte-read from `raw.githubusercontent.com`** at the repository's
default ref, and stars / SPDX / `pushed_at` come from `gh api search/repositories`. Licence bytes
for all 36 addresses touched this pass:
[`licence-bytes.2026-11-19-p908.tsv`](../evidence/licence-bytes.2026-11-19-p908.tsv).

| Agent | Repo | Licence (byte-read) | ★ | Last push | Institution / system | Region | In `p908` |
|---|---|---|---|---|---|---|---|
| **education-agent-skills** | https://github.com/GarethManning/education-agent-skills | 🔴 **CC BY-SA 4.0** `1,230 B` | 1,000 | 2026-11-03 | 165 evidence-grounded skills for teachers and school leaders — **not software, and ShareAlike** (`T32`) | Global | restored |
| **TutorAI** (NTNU) | https://github.com/CogitoNTNU/TutorAI | **MIT** `1,140 B` | 39 | 2026-11-16 | NTNU — RAG tutor that cites the curriculum it answers from | EMEA 🇳🇴 | restored |
| **spbstu-mcp** | https://github.com/kad-xyz/spbstu-mcp | **MIT** `1,064 B` | 19 | 2026-11-10 | SPbPU — institutional Moodle (`dl.spbstu.ru`), university mail **and the national `openedu.ru`** | EMEA 🇷🇺 | restored |
| **Skolverket-MCP** | https://github.com/isakskogstad/Skolverket-MCP | **MIT** `1,093 B` | 13 | 2026-04-22 | Sweden's **National Agency for Education** open data — a *national* source, not a campus | EMEA 🇸🇪 | restored |
| **utn-mcp** | https://github.com/nialvape/utn-mcp | **ISC** `748 B` | 13 | 2026-11-13 | UTN — aula virtual (Moodle) **+ Sysacad**; the best credential hygiene in this cohort | LATAM 🇦🇷 | restored |
| **udesa-mcp** | https://github.com/changazo/udesa-mcp | **Apache-2.0** `10,173 B` | 4 | 2026-11-17 | Universidad de San Andrés Campus Virtual (Moodle); preview-then-confirm on every write | LATAM 🇦🇷 | restored |
| **UniMCP** | https://github.com/HyNuwa/UniMCP | 🟡 **MIT + inherited ISC, conjunctive** `1,980 B` | 1 | 2026-11-14 | Argentine universities — Moodle **+ SIU Guaraní**; Guaraní read-only | LATAM 🇦🇷 | restored |
| **siu-guarani-mcp** | https://github.com/jpmanson/siu-guarani-mcp | **MIT** `1,074 B` | 1 | 2026-08-10 | **SIU-Guaraní** *autogestión docente* — the SIS the Argentine national university system runs | LATAM 🇦🇷 | restored |
| **tum-mcp** | https://github.com/jamestesting0/tum-mcp | **MIT** `1,092 B` | 1 | 2026-11-18 | TU München — Moodle **+ Artemis** (autograder) + TUM Live + TUMonline | EMEA 🇩🇪 | restored |
| **merlin-mcp** | https://github.com/simonseifert/merlin-mcp | **MIT** `1,070 B` | 1 | 2026-11-16 | **Merlin** — SRCE's *national* Moodle tenancy for Croatian universities. Read-only; phone-approved sends | EMEA 🇭🇷 | restored |
| **TutorIA** | https://github.com/LabSirius/TutorIA | **MIT** `1,069 B` | 0 | 2026-10-27 | Universidad Tecnológica de Pereira — autonomous tutor for **rural** higher education in Risaralda | LATAM 🇨🇴 | restored |
| **miyagi** | https://github.com/falkenslab/miyagi | **MIT** `1,078 B` | 0 | 2026-11-18 | Moodle course assistant on the **teacher's** side: grades to the teacher's own rubric, staffs the forum | Global | restored |
| **agente-bncc-professores** | https://github.com/GuilhermeScarpini/agente-bncc-professores | **MIT** `1,074 B` | 0 | 2026-10-21 | Lesson plans and exams anchored to **BNCC** skill codes, semantic search, Gemini or DeepSeek | LATAM 🇧🇷 | restored |
| **campus-cli** | https://github.com/alejooroncoy/campus-cli | **ISC** (API) | 13 | 2026-11-18 | UPC Aula Virtual — **Blackboard Learn**, terminal + MCP | LATAM 🇵🇪 | 🆕 filed |
| **UJI-MCP** | https://github.com/Victor-Blasco/UJI-MCP | **MIT** `1,063 B` | 1 | 2026-11-05 | Universitat Jaume I aula virtual (Moodle) + Google Tasks; targets four different agent clients | EMEA 🇪🇸 | 🆕 filed |
| **mcp-uned** | https://github.com/kta41/mcp-uned | **MIT** `1,071 B` | 1 | 2026-10-18 | **UNED** (`agora.uned.es`) — Europe's largest distance university by enrolment | EMEA 🇪🇸 | 🆕 filed |
| **autonoma-cli** | https://github.com/Just253/autonoma-cli | **MIT** `1,064 B` | 1 | 2026-11-17 | Campus Virtual course listing and file download. 🟡 **Names no country** — not placed | — | 🆕 filed |
| **DUTIC-mcp** | https://github.com/JOSETRA44/DUTIC-mcp | **MIT** `1,066 B` | 0 | 2026-11-07 | **DUTIC** aula virtual (UNSA, Arequipa) — *"for AI agents and humans"* | LATAM 🇵🇪 | 🆕 filed |
| **udb-copilot** | https://github.com/franc1sc0sv/udb-copilot | **MIT** `1,066 B` | 0 | 2026-10-25 | **Universidad Don Bosco, El Salvador** — cited notes, the teacher's method, Moodle + mail, daily digest | LATAM 🇸🇻 | 🆕 **first Central America row in this base** |
| **poli** | https://github.com/SebasB76/poli | **MIT** `1,065 B` | 0 | 2026-11-16 | **ESPOL** (Ecuador) — the only **Canvas**-protocol bridge in this cohort | LATAM 🇪🇨 | 🆕 filed |
| **IAula-Virtual-Uleam** | https://github.com/VxGM/IAula-Virtual-Uleam | **MIT** `1,061 B` | 0 | 2026-11-17 | ULEAM (Ecuador) Moodle monitor — novedades, tareas, descargas, NotebookLM hand-off | LATAM 🇪🇨 | 🆕 filed |
| **tuaulavirtual-unam-mcp** | https://github.com/alanmagno1/tuaulavirtual-unam-mcp | **MIT** `1,067 B` | 0 | 2026-09-09 | **UNAM** *Tu Aula Virtual* (Moodle) — Latin America's largest university | LATAM 🇲🇽 | 🆕 filed |
| **CampusUNSA** | https://github.com/MarcoXMarquez/CampusUNSA | **MIT** `1,130 B` | 0 | 2026-11-19 | UNSA (Peru) — **offline-first PWA + WhatsApp/Telegram** assistant over Classroom and DUTIC Moodle, `@unsa.edu.pe` SSO | LATAM 🇵🇪 | 🆕 filed |
| **Skill-Moodle** | https://github.com/Group-Active-IA/Skill-Moodle | **MIT** `1,079 B` | 0 | 2026-09-24 | UTN TUP campus navigator — shipped as a **Claude Code skill**, not a server (`T22`, `T31`) | LATAM 🇦🇷 | 🆕 filed |
| **aulasvirtuales-toolkit** | https://github.com/alexFiorenza/aulasvirtuales-toolkit | **MIT** `1,070 B` | 0 | 2026-08-26 | UTN FRBA `aulasvirtuales` — tools *"to interact through agentic tools"* | LATAM 🇦🇷 | 🆕 filed |
| **campus-usc** | https://github.com/PabloPC05/campus-usc | **MIT** `1,066 B` | 0 | 2026-11-18 | Universidade de Santiago de Compostela Campus Virtual in the terminal | EMEA 🇪🇸 | 🆕 filed |

🟢 **Region movement from this section alone: LATAM `+13` institutional rows across seven countries
(🇦🇷 🇧🇷 🇨🇴 🇪🇨 🇲🇽 🇵🇪 🇸🇻), EMEA `+7` across six (🇩🇪 🇭🇷 🇳🇴 🇷🇺 🇸🇪 🇪🇸).** An institutional agent
names its university, so **it places itself** — no region inferred from a README, which is the
property that makes this class the cheapest regional evidence in the base.

🔴 **Three repositories from the same cohort were found, measured and *not* filed, because they
carry no licence at all**: `PedroCarassale/utn-mcp` (UTN FRLP Moodle, 1 ★),
`A-F-V-A/unihelp-mcp-a2a` (university service-desk triage in four agent architectures, 0 ★) and
`MoonquantCap/agentes-ia-ucema` (UCEMA, 3 ★). All three return `README` `200` — they are real and
unusable. 🟡 **Four of the seven bridges in `907-F4` were unlicensed too, so the unlicensed share of
this class is now `7 / 30`.** The pattern holds: a bridge written by one student for one campus is
not published as supply.

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
| **CrewAI** | https://github.com/crewAIInc/crewAI | MIT | 61,086 | Role-based multi-agent orchestration — maps cleanly onto instructor / tutor / grader / reviewer splits. |
| **LangGraph** | https://github.com/langchain-ai/langgraph | MIT | 45,129 | Graph-structured orchestration. The right primitive when a tutoring policy must be auditable: policy checks become explicit nodes. |
| **AI Engineering Hub** | https://github.com/patchy631/ai-engineering-hub | MIT | 42,007 | Not an agent: a large collection of worked agent projects. Useful as staff-upskilling material. |
| **STORM** | https://github.com/stanford-oval/storm | MIT | 31,911 | Generates cited, structured long-form articles. Repurposes well for courseware drafting. **Last push 2025-09-30 — effectively dormant;** pin a version. |
| **GPT Researcher** | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | 30,774 | Autonomous research agent with citation discipline — literature-review scaffolds in higher ed. |
| **OpenHands** | https://github.com/OpenHands/OpenHands | MIT | 93,766 | Coding agent; the practical choice for automating LMS plugin and migration work. 🔴 **Slug corrected in p896, and in the opposite direction to the earlier note.** `OpenHands/OpenHands` is the canonical repo (93,731 ★, pushed 2026-11-18); `All-Hands-AI/OpenHands` is a **rename alias** that `raw.githubusercontent.com` still serves, which is why earlier passes read it as canonical. The star count was recorded here as *unavailable* only because the alias was being queried. Org also ships https://github.com/OpenHands/software-agent-sdk (MIT). |
| **LibreChat** | https://github.com/LibreChat-AI/LibreChat | MIT | 47,327 | Multi-model chat front end with auth and per-user quotas; fastest route to a governed institutional chat tier. 🔴 **Slug corrected in p896**: `LibreChat-AI/LibreChat` is canonical (47,317 ★, pushed 2026-11-18); `danny-avila/LibreChat` is a rename alias. Same failure mode as the OpenHands row above — see `agents/trending.md` p896 for the gate that catches it. |

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

🟢 **`p903` found this form executed against a national curriculum, and it changes what the
1,000 ★ watch condition is measuring.** Every cohort member above is a *tool* — a tutor delivered as
an MCP server or a skill, ceiling **125 ★**. `revolover00/Bakloriya-AI-SKILLS` (6 ★, **unlicensed**,
28,402 KB, EMEA — Egypt) is the same delivery form carrying **Egypt's complete approved 2026/2027
curriculum: 300 units across the Baccalaureate, General Secondary, Preparatory and Primary stages.**
It ships **no application at all** — no server, no model, no framework. There is an `AGENTS.md`
routing guide at a raw URL, and a prompt the student pastes into *any* model, which then walks
`skills/<stage>/<grade>/<term>/<subject>/` by itself. Its anti-hallucination control is a
**corpus-scoping instruction**, not a retrieval system: *stay inside the syllabus, do not mix grades
or terms.*

🔵 **The reading this forces.** This file's standing verdict — *"shortens time-to-pilot and belongs
in the demo kit; it does not belong on a client roadmap yet"* — was derived from a cohort of tools,
and **stars are the wrong instrument for a corpus.** A curriculum corpus is used by the students who
need that curriculum; 6 stars from Egyptian secondary students is not the same signal as 6 stars on
a developer tool, and a 1,000 ★ threshold will never fire on a national-curriculum repository no
matter how many learners it serves. **The watch condition stays at 1,000 ★ for the tool cohort and
is the wrong test for the corpus form, which needs a different one: curriculum coverage and
maintenance recency.** On those, `Bakloriya-AI-SKILLS` reads as complete and current (300/300 units,
pushed 2026-11-09) — and **unusable**, because it carries no grant. The pattern that takes the
schema and discards the content is `compose/patterns.md` **P22**.

🔴 **`p909` makes it three times this cohort has been enumerated incompletely, and this time the
missing member was in the log the whole time.** `geekjourneyx/interactive-learning` (**MIT**,
**52 ★**, byte-read `LICENSE@HEAD`, 1,069 B, `sha256₁₂ 02b7dc1969f4`) has been named in
`agents/trending.md`, `repos/trending.md`, `intel/market.md` and `intel/open-gaps.md` since
`p907` — and had **no row in any delivery file** when `p909` opened them. `p908`'s own supply leg
listed it among repositories *"all four already held"*: held in the **log**, not in **delivery**.
That is `908-F1`'s divergence landing inside the one cohort `p896` had already flagged for roster
incompleteness, which makes it the third instance rather than a new class. 🟢 **It now has a row
in the table above.** It is the cohort's clearest *pedagogical* statement rather than its largest
member: it refuses to be a summariser, converting material into a **verifiable learning path**
with an exportable **HTML checkpoint card**, on the explicit thesis that *"a summariser solves
compression, not misunderstanding."* 🟡 At 52 ★ it does not approach the ceiling, which `p909` **remeasured at 126 ★**
(`flysheep-ai/education-skills`, MIT, pushed `2026-01-30` — up 1 from the 125 ★ `p896` recorded);
`ArnaudGuiovanna/tutor-mcp` also moved, 104 → **107 ★**. The **1,000 ★** watch condition is
untouched — the cohort remains an order of magnitude short.

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
- **LATAM is not thin — the channel was never searched. Rewritten p904, and this is the largest
  single correction this file has made to a standing claim.** Through `p903` this bullet read
  *"LATAM supply is thin and Brazil-only... for a LATAM engagement, expect to localise an APAC- or
  EMEA-origin agent"*, resting on two rows (`warleysr/ankipa` 10 ★, `CaioCastro1/usp-mcp` 28 ★).
  🔴 **No pass had ever run a Spanish- or Portuguese-language repository search.** `p904` ran 26
  such queries, including LATAM national-examination names, and the claim does not survive:
  **six LATAM-origin rows now sit in the table above** (`bncc-mcp` 14 ★ MIT, `mooose` 5 ★
  Apache-2.0, `GenPrompt-Pre-ICFES-11` 4 ★ AGPL-3.0 — **the first Colombia-origin entry** —
  `AI-Skill-Corretor-Redacao-ENEM` 3 ★ MIT, `GabirIA` 3 ★ MIT, plus `ankipa`), with
  `usp-mcp` and a **five-repository Brazilian curriculum-data cluster** in
  `repos/foundations.md` and two AGPL platforms in `verticals/solutions.md`.
  🔵 **The corrected claim is more useful than the one it replaces, and it is a sales
  observation rather than a supply one: LATAM open source builds against the two artefacts every
  school in a country shares — the national examination and the national curriculum.** ENEM essay
  grading, ENEM mock exams, Saber 11 prompt generation, and the BNCC published as verified open
  data with a DOI. What LATAM does *not* produce is the general-purpose tutor: the
  Spanish-language tutor channel tops out at **6 ★ and unlicensed**, the Portuguese at 3 ★.
  So the localisation advice inverts — **bring the tutor, adopt the curriculum spine** — and
  `compose/patterns.md` **P23** is written for exactly that shape.
  🟡 **Three things remain true and should be said to a client.** (1) These are small projects:
  largest 26 ★, median 9 ★. (2) **Spanish-speaking Latin America is still almost absent**: Mexico
  returned a **0 ★ ceiling** on `EXANI examen` and no repository in any of the 26 queries, and
  Argentina, Peru and Central America returned nothing; Colombia's single entry is AGPL and
  Chile's single entry (`HuemulSolutions/Enola-AI`, BSD-3-Clause, 1 ★) has not been pushed since
  **2024-12-31**. (3) LATAM edtech *company* searches still return firms, not repos (Teachy,
  Vetto, Ginia). **The gap moved from "LATAM" to "Spanish-speaking LATAM outside Colombia", which
  is a gap a studio can actually act on.**
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
- 🟢 **The Middle East supply gap: the channel named here as untried was run in `p903`, and the
  answer is not "nothing" — it is "populated, unlicensed, and capped at 6 stars" (rewritten p903).**
  The previous text read *"The untried channel is Arabic-language search (the `elimu` Swahili trick
  applied to `تعليم`); it was not run."* It has now been run, across four Arabic queries plus
  Persian, Hebrew and Turkish, with every licence byte-read on 12 candidate paths. Results:
  - 🟢 **Two MENA-origin education artefacts are real, and both were absent from this whole tree**
    (checked against all 5,790 repository references in it). `SalehGNUTUX/GT-MISHKATKIDS`
    (**GPL-3.0**, 3 ★, pushed 2026-11-18) is in the table above. The larger one is below.
  - 🔴 **The biggest find in the channel earns no row, for the same reason `EduNaija-LLM` earns
    none.** https://github.com/revolover00/Bakloriya-AI-SKILLS (**6 ★**, created 2026-10-17,
    pushed 2026-11-09, **28,402 KB**) is **Egypt's entire approved 2026/2027 curriculum across all
    four stages** — Egyptian Baccalaureate (78 units), General Secondary (102), Preparatory (42),
    Primary grades 1–6 (78): **300 units, its README's own table reporting "no chapter missing"** —
    decomposed per subject into `SKILL.md`, `glossary.md`, `patterns.md` (exam question patterns and
    solution keys), `cheatsheet.md` and a `chapters/` tree. **It has no licence on any of 12
    byte-read paths.** 28 MB of national curriculum content under default all-rights-reserved
    copyright cannot be vendored, redistributed or shipped in a client deliverable. What transfers
    is the **decomposition schema**, re-authored against a corpus the client owns or licenses.
  - 🟡 **The usable sub-channel is the exam name, not the education word.** `منصة تعليمية` returns
    3,468 hits and is unusable (developer awesome-lists); `تعليم` 2,302, `معلم` 1,828, `منهج` 728,
    all dominated by programming tutorials and certification memoirs — the same false-positive
    profile this file already graded for `JAMB`. **`الثانوية العامة` (525 hits) is what produced
    the Egyptian find.**
  - 🔴 **Saudi supply is now counted, and the count is the finding.** `قدرات تحصيلي` — the Qiyas
    battery — returns **12 repositories in total, every one at 0 ★ and every one unlicensed**,
    including the two on-target ones: https://github.com/ADELSPX/mawheb and
    `hjr24r7269-crypto/naqat`. Against the **demand** side this KB records for Saudi Arabia — 50 new
    curriculum units for 2026-27, **240,000 teachers in training** — twelve zero-star unlicensed
    repositories is **the sharpest build-not-adopt signal in this base.**
  - **Still nothing licensed from the Gulf, and nothing at all from the UAE on the supply side**
    in any of the four languages tried. Arabic is no longer an untried channel; **Urdu and
    Indonesian are**, and they are the next two to run.
- **No confirmed November 2026 *launch*.** The newest dated release artefact is OpenMAIC
  `v1.4.2` (2026-11-09). Re-checked in pass p890 across four global and four regional search
  legs: unchanged.
- **The "tutor as an agent skill" cohort has no traction.** The previous pass set a watch
  threshold of 1,000 ★. Remeasured in p890: the cohort maximum is **118 ★**
  (`boyuchengz/canvas-mcp`) and **not one member gained a single star** in the interval. The
  form shortens time-to-pilot and belongs in the demo kit; it does not belong on a client
  roadmap yet.
- **Open education agents originate from East-Asian and European universities — with one
  measured exception as of `p903`, and the exception is individual rather than institutional
  (rewritten p903).** p891 and p892 ran dedicated legs for Africa, the Middle East, Saudi Arabia and
  India and returned substantial policy evidence with **not one repository**; the previous text
  therefore read *"No open education agent originates from India, Africa or the Middle East."*
  **The Arabic-language leg falsifies that for the Middle East and North Africa.** Egypt produced
  `Bakloriya-AI-SKILLS` (6 ★, unlicensed, 300 curriculum units) and the MENA Arabic channel produced
  `GT-MISHKATKIDS` (GPL-3.0, 3 ★, pushed today). **India and the Gulf states remain unfalsified** —
  India mandates AI across Classes III–VIII from 2026–27 and Saudi Arabia is training 240,000
  teachers, and neither has produced a locatable open education agent in any pass or any language
  tried. 🔵 **The corrected pattern is sharper than the one it replaces, because the two exceptions
  share a shape:** both are **single-maintainer projects at 0 forks**, against the East-Asian and
  European entries that come out of named labs (HKU Data Intelligence Lab, Tsinghua, MIT Open
  Learning, Oak National Academy). So the finding is not that MENA produces nothing; it is that
  **MENA produces individuals and not institutions**, which is a different market: the asset to
  bring is the institutional engineering, not the pedagogy. 🔴 **The LATAM half of this comparison was retracted in `p904`:** the clause that stood here
  read *"with the standing LATAM result (`ankipa` 10 ★, `usp-mcp` 28 ★, both Brazil-only) that still
  defines the localisation market"*, and the Spanish/Portuguese channel falsified it — LATAM
  produces **institutions** (Profy Tecnologias Educacionais Ltda, `CREARED-EDU-CO`,
  `UnitedOpen-Source`) as well as individuals, which is the opposite of the MENA shape and is why
  the two regions need different offers. See the rewritten LATAM bullet below. It remains true that
  `compose/patterns.md` **P10** treats language and curriculum corpus as the swappable parts, and
  **P23** now shows what a client-owned curriculum spine looks like when it exists.
- **No locatable repository for `AcademiClaw`** (arXiv 2605.02661, students setting challenges
  for AI agents). Paper only. Recorded so a later pass does not re-chase it.

- **Global code search was run for the first time (`p907`), and its negative results matter as much
  as its finds.** The channel reaches *inside* repositories, so it finds education **interop**
  engineering that repo search cannot see — and it is **poisoned by security fuzzing wordlists**,
  which contain `moodle`, `canvas`, `qti`, `xapi` and `scorm` as dictionary entries, one token per
  line. Of the 212 novel repositories returned by a nine-query control batch on education standard
  tokens, the high-star tail was `LaTeX-Workshop` (12,416 ★), `xonsh` (9,704 ★), `fuzzDicts`
  (8,448 ★), `neomutt` (3,865 ★) and four more pentest dictionaries. **The education-native ceiling
  on this channel is 76 ★** (`swl10/pyslet`, and it has been dead since 2020). Full method and the
  exclusion rule in `agents/trending.md` `907-F3`.
- 🔴 **The generic agent-skill marketplaces have no education tier at all, and that is an
  opportunity rather than a gap in this file.** Probed `p907`: `sickn33/agentic-awesome-skills`
  (**49,962 ★**, MIT, 2,955+ skills) and `LeoYeAI/agent-master-skills` (**2,206 ★**, MIT, 2,700+
  skills). Their `curriculum` and `lesson plan` hits are incidental vocabulary in *marketing and
  product-design* skills — the returned paths are `skills/product-design-harness/`, `skills/offers/`,
  `skills/linkedin-profile-optimizer/SKILL.md`. **`tutor pedagogy` returns `0`.** The distribution
  channel for `intel/trends.md` **T26** exists, is permissive, is enormous, and is empty where
  education belongs.
- **Blackboard has no *licensed* row in this KB.** `p907` found exactly one piece of Blackboard
  agent code — https://github.com/bolgerru/blackboard-mcp (Trinity College Dublin, deadline
  tracker) — and it carries **no licence file**, so it is not shelved. The only Blackboard row
  anywhere in this base is the Peru row above, which reaches Blackboard Ultra through a university
  tenant rather than as a platform integration.
- **Argentina and Central America remain unrefuted** after `p907` refuted Peru. The channel that
  found Peru is code search; it should next be pointed at `aula virtual`, `campus virtual` and
  `sistema académico` tokens rather than at `educación` or `tutor`.

## Corrections made this pass

- 🔴 **`p907` — the `ankipa` row's claim was stale, and no pass had caught it inside the row.**
  That row read *"the only LATAM-origin education agent verified in this pass"*. It was already
  false when `p904` wrote six further LATAM rows into this same table: `usp-mcp` (Brazil, 28 ★),
  `bncc-mcp`, `mooose`, `GenPrompt Pre-ICFES 11` (Colombia), `AI-Skill Corretor de Redação ENEM`
  and `GabirIA`. `p904` corrected the LATAM **gap bullet** further down this file and left the
  sentence inside the row standing. 🔵 **Counted mechanically in `p907`: seven LATAM-origin rows
  before this pass, across two countries (Brazil 6, Colombia 1); eight across three with Peru
  added.** The lesson is the same one as the row-count drift: **a claim of uniqueness placed inside
  a row is invisible to the pass that falsifies it**, because that pass reads the gap list, not the
  rows.
- 🔵 **`p907` — the row count is re-derived, not incremented: `77` → `80`.** Per the `p906` rule
  recorded above.
- 🔴 **`p907` — `curl -sI https://github.com/OWNER/REPO` is not a usable existence check in this
  environment and must not be cited as one.** It returns `403` for every address, including three
  deliberately nonexistent controls. Existence in this KB is proved by `raw.githubusercontent.com`
  (`200` real / `404` absent, both controls run) plus the `search/repositories` measurement. See
  `agents/trending.md` `907-F2`.


- 🟢 **`p905` — star currency, and a reproducibility column added to the two flagship rows.**
  Re-measured 2026-11-18: `HKUDS/DeepTutor` **60,351 → 60,451**, `THU-MAIC/OpenMAIC`
  **43,889 → 43,899**. Both rows now carry what no pass had measured: whether the agent can be
  rebuilt from its own manifests. **Neither can.** `DeepTutor` declares 74 unique packages with
  **1 exact pin** across a three-level generated manifest tree whose root file is a 104-byte `-r`
  pointer; `OpenMAIC` declares 178 npm packages with no lockfile on any path probed. By contrast
  `openedx/openedx-platform` pins **311 of 311**. 🔵 The two measurements are orthogonal — the
  most-starred agents are the least vendorable — and the selection consequence is in
  `repos/foundations.md`, the trend in `intel/trends.md` **T28**, and the remediation tier in
  `compose/patterns.md` **P24**. Ledger:
  [`dep-grant-scan.2026-11-18-p905.tsv`](../evidence/dep-grant-scan.2026-11-18-p905.tsv).
- 🟡 **`p905` — a near-miss worth recording, because the guard that caught it is this page.** The
  `p905` dependency scan found `openedx/edx-platform` absent from `repo:` search but `200` on `raw`,
  and the first write-up called it a fresh instance of `p900`'s search-index-gap rule. **It is the
  `p896` rename**, already corrected on this page below: the canonical slug is
  `openedx/openedx-platform` (**8,244 ★**, AGPL-3.0, pushed 2026-11-18) and `raw` serves the old name
  only through GitHub's rename redirect. 🔵 **A `raw` `200` against a search `absent` has two causes
  — an index gap and a rename — and they call for opposite actions.** Distinguishing them costs one
  query against the suspected new name. New byte-identical pair recorded:
  `requirements/edx/base.txt` is **28,659 B** `sha256₁₂ 20f78eb076b4` on both names.

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
