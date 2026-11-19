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

**Latest sweep — `p922` (2026-11-19).** 🔴 **No remeasure of this file's rows and no new agent rows
— the forty-first consecutive nil at the agent layer**, and the budget went where `921-G5` said it
should. The eight mandated English legs returned **zero repositories** and **12 of 12 named facts
this base already holds**; the two substrate legs returned **18 repositories byte-read, 18 unseen**.
🟢 **What changed for this file is a rule, not a row.** `922-R1` — the role test `921-G3`
prescribed — is now binding on every tier verdict this base publishes: *the passing member must be
the tier's general artefact, not an adjacent single-purpose tool and not a catalogue, and a
copyleft pass is published as `DELIVERABLE — COPYLEFT`.* It re-grades Portuguese from DELIVERABLE
to **NOT**. 🔴 And `921-R1`, published one pass ago as the mechanism behind every tier verdict in
this base, **scored 4 of 10 against tiers chosen to break it and is retired** — along with the
successor `p922` pre-registered, which scored 1 of 4. See `agents/trending.md` `922-F1`/`922-F2`
and the twenty-tier table in `repos/foundations.md`.

**Latest sweep — `p921` (2026-11-19).** 🔴 **No remeasure of this file's rows this pass, and no
new agent rows — because the agent layer returned nothing again and the substrate layer returned
everything.** The four discovery legs were Turkish, Arabic, Indonesian and Indic *language
substrate*, not education agents: **16 repositories byte-read, 16 this base had never held**, against
the eight mandated English legs' **zero** (fortieth consecutive nil). 🟢 The result corrects a
sentence this file's companion shelf has carried since `p903` — *"at the agent tier in Arabic,
Persian, Hebrew and Turkish there is nothing to adopt"* — which is true **at the agent tier** and was
being read as the whole verdict: `ahmetaa/zemberek-nlp` is **1,379 ★, Apache-2.0 (byte-read; the
search channel says `NOASSERTION`), pushed 2026-11-17**. 🔵 **The operative rule for this file:
a tier verdict that does not name its layer is not a verdict** — see `agents/trending.md` `921-F3`
and `921-R1`.

**Latest sweep — `p919` (2026-11-19).** 🔴 **No full remeasure this pass — deliberately.** The `p918` sweep is hours old and `p894`'s cadence note stands: the largest intra-day move across ~30 tracked repos was +21 stars on a 60,000-star repo. Spot check only: `HKUDS/DeepTutor` **60,684** `Apache-2.0` (p918: 60,675). The budget went to `918-G7` instead, and it returned **14 repositories this base had never seen** against the global English leg's **zero** — the 39th consecutive nil at the top of the English-language shelf. New tier below: **Indonesia and Thailand**.

**Previous sweep — `p918` (2026-11-19).** 21 of 22 anchor rows re-resolved on `search`
([record](../evidence/shelf-remeasure.2026-11-19-p918.tsv)): `OpenHands/OpenHands` **93,816** `MIT`,
`microsoft/ai-agents-for-beginners` **80,443** `MIT`, `crewAIInc/crewAI` **61,093** `MIT`,
`HKUDS/DeepTutor` **60,675** `Apache-2.0` (p917: 60,661), `langchain-ai/langgraph` **45,154** `MIT`,
`THU-MAIC/OpenMAIC` **43,940** `MIT`, `patchy631/ai-engineering-hub` **42,021** `MIT`,
`withmarbleapp/os-taxonomy` **7,729** `ODbL-1.0`, `ls1intum/Artemis` **833** `MIT`,
`PrairieLearn/PrairieLearn` **533** `NOASSERTION`, `CAHLR/pyBKT` **292** `MIT`.
🔴 **`openedx/edx-platform` was absent on `search` for the third consecutive day** — `Validation
Failed` — while `raw.githubusercontent.com` serves `200` on `master/README.rst` *and*
`master/LICENSE`. Three days is not a transient; see `agents/trending.md` `918-F5`.

**Previous sweep — `p917` (2026-11-19).** All **199** addresses in this file re-probed.
`search/repositories` resolved **195**: `OpenHands/OpenHands` **93,811** `MIT`,
`microsoft/ai-agents-for-beginners` **80,437** `MIT`, `crewAIInc/crewAI` **61,093** `MIT`,
`HKUDS/DeepTutor` **60,661** `Apache-2.0` (p901: 60,405), `langchain-ai/langgraph` **45,152** `MIT`,
`THU-MAIC/OpenMAIC` **43,939** `MIT` (p901: 43,894), `patchy631/ai-engineering-hub` **42,021** `MIT`
(p901: 41,998). 🔴 **Three rows are live on `raw` and ABSENT on `search`** —
`DaRL-GenAI/instructional_agents` and `mitodl/open-learning-ai-tutor` return `total_count: 0` with
no error at all, `TokenAII/horus-taleeq-0.2b-base` returns `Validation Failed`, and all three serve
a `200` README. **`p916`'s `openedx/edx-platform` absence re-probed one day later and reproduced**,
in the same *loud* shape — so there are **two** absence shapes, not three, and the silent one is the
dangerous one. Rate on this shelf: **3 of 195 (1.5%)**. See `agents/trending.md` `917-F9`.

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
| **OpenPronounce** | https://github.com/OpenPronounce/OpenPronounce | 🔴 **AGPL-3.0 — CORRECTED `p913`, was published here as `MIT`** (byte-read `main/LICENSE`, 34,523 B, `sha256₁₂ 0d96a4ff68ad`; title line `GNU AFFERO GENERAL PUBLIC LICENSE / Version 3, 19 November 2007`) | 224 | 2026-11-09 | 🔴 **READ THE LICENCE BEFORE SCOPING THIS ROW.** It was carried as `MIT` and is **AGPL-3.0**: §13 imposes a **network-use source-disclosure obligation**, so offering this as a hosted pronunciation service means offering its source to the users of that service. `P1`, `P9` and `P16` all cite pronunciation or oral assessment — none of them can use this row as a *linked* component of a closed deliverable; it runs as a separate service or not at all (`G1`). Open pronunciation assessment — the language-learning niche where open source is genuinely competitive with commercial APIs. 🔵 **p900: this base logged `halleck45/openpronounce` 5× in its `logged-not-shelved` ledger and nearly promoted it as a second row.** It is a **transfer alias of this repository** — byte-identical `README.md` (`sha256₁₂ a005d079f571`) — caught by the duplicate-subject gate before publication. **The rename mechanism that causes false ABSENCES in the ledger causes false DUPLICATES on the shelf**; both need the canonical name resolved first. | Global |
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
| **bandup** | https://github.com/BaijayantaRoy/bandup | **MIT** (byte-read `p910`, `LICENSE@main`, 1,071 B, `sha256₁₂ c4411a4cb83b`) | 2 | 2026-08-22 | **Added `p910`, and it is this KB's first Singapore-origin agent.** Open-source AI **marking assistant for Singapore exam essays** — PSLE composition and A-Level General Paper. 🔵 The national-exam channel (`910-F1`) produced exactly two AI-native builds across ten markets and this is the licensed one. 🟡 2 ★ and single-author: treat as a reference implementation of the *rubric* rather than a dependency — its value is that the marking criteria are the Singapore ones, which no general grader encodes. | APAC — Singapore |
| **jlpt-n1-Yomitaku** | https://github.com/Mocas-12/jlpt-n1-Yomitaku | **MIT** (byte-read `p910`, `LICENSE@main`, 1,065 B, `sha256₁₂ b17ceb82d82e`) | 31 | 2026-11-13 | **Added `p910`.** JLPT N1 読解 (reading) trainer covering **all six official question types**, timed practice, and explanations **classified by the trap the item sets**. 🟢 The trap taxonomy is the transferable asset: it is item-level pedagogical metadata of the kind `P23`'s hallucination gate needs, and it is rare in open repositories. | APAC — Japan |
| **immersive-memorize** | https://github.com/metrovoc/immersive-memorize | **MIT** (byte-read `p910`, `LICENSE@main`, 1,074 B, `sha256₁₂ 51ae850d5688`) | 29 | 2026-11-18 | **Added `p910`.** Chrome extension that highlights unseen **JLPT** vocabulary in Netflix or custom subtitles and turns the sentence into a flashcard. 🟢 **Capture-at-point-of-encounter**: the card is built from media the learner chose, so the corpus is the learner's own and no licensed deck is redistributed — which is `910-F4`'s way out of the CC BY-NC problem. Pushed the day before this pass. | APAC — Japan |
| **edubot-backend** | https://github.com/AriusKing/edubot-backend | **MIT** (byte-read `p910`, `LICENSE@main`, 1,065 B, `sha256₁₂ c115ae89efc8`) | 0 | 2026-07-01 | **Added `p910`.** Express.js backend for an **HKDSE** study super-app (unified auth, content and progress). 🟡 0 ★ and unproven; carried because Hong Kong's co-termed ceiling is 17 repositories and this is the only one of them with a server-side architecture and a grant. | APAC — Hong Kong |
| **israeli-bagrut-psychometric** | https://github.com/peleg-jpg/israeli-bagrut-psychometric | **MIT** (byte-read `p910`, `LICENSE@main`, 1,150 B, `sha256₁₂ 2b20dde3e647`) | 0 | 2026-05-11 | **Added `p910`, first Israel-origin row.** Guides a learner through the **Bagrut** matriculation and the **Psychometric** entrance exam. 🔵 Its licence carries two copyright lines — `skills-il contributors` and the packager "(security vetting and distribution)" — which is a **provenance-aware grant**, the shape `P24`'s handover tier argues for and the only instance of it this tree has found in the wild. | EMEA — Israel |
| **topik-shortcut** | https://github.com/summeraprx/topik-shortcut | 🔴 **NO GRANT** (byte-read `p910`: 8-path ladder on `main`, all `404`; field `NULL`) | 1 | 2026-10-20 | **Added `p910` as a barred row, deliberately.** AI study tool for **TOPIK II** built from real past exams: OCR pipeline → Korean NLP → practice items. 🟢 Architecturally it is the most interesting thing in the Korean leg and the only AI-native TOPIK build found. 🔴 **No licence file, so it cannot be used, forked or vendored** — it is recorded so that a later pass does not re-discover it as a find, and so that a Korea engagement knows the capability exists and must be rebuilt. 🔵 Worth one email: a single `LICENSE` commit by its author would move it to the table above. | APAC — Korea |

🔵 **`87` rows in the table above, re-counted mechanically in `p910`** (`81` at the close of
`p909`; **`p910` added 6** — five from the **national-examination English-metadata channel**
(`910-F1`), which is `906-G2`'s named instrument running for the first time, plus one **barred**
row kept visible on purpose. The six span four markets this table had thin or no coverage of:
**Singapore and Israel are first-ever rows**, Hong Kong gains its first server-side build, and
Korea's entry is the ungranted one, which is the honest shape of that market.)

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

## National-examination agents — the six markets `906-G2` named, added `p911`

🟢 **Every grant below was byte-read on the default branch resolved from the search channel**
(`ingest/p880-licence-byteread.sh`, `2026-11-19`), and **one of the nineteen resolved on `master`**
(`lindnerju/ePaeko`) — the `884-G2` default-branch fix paying for the second consecutive pass.
🔴 **These are small.** The largest is `23 ★` and most are `0`–`3 ★`: `911-F3` measures that this
tier has **no concentration at all** — `4` of `205` education-context repositories clear `100 ★`
across all fourteen terms. 🔵 **Read them as reference implementations and starting points for a
named market, not as products to adopt** — which is precisely what a studio entering Nigeria,
Kenya, Chile, Colombia or an Indian state board needs and did not have in this KB before.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **Jambora** | https://github.com/edunelsonit/Jambora | Apache-2.0 (11,357 B · `c71d239df917`) | 1 | 2026-03-24 | AI-powered CBT application for Nigeria's JAMB. 🟢 **The most commercially relevant row in this section**, because WAEC and NECO are moving the WASSCE to full computer-based testing with **essay components** in 2026 (`intel/market.md` EMEA) — this is an open starting point aimed at exactly that transition. 🔵 Standard unmodified Apache-2.0 payload, byte-identical to three other rows promoted this pass. | EMEA — Nigeria |
| **NAIJASCHOLAR** | https://github.com/ALIYUAAM10/NAIJASCHOLAR | MIT (1,082 B · `6fd3e72cd64d`) | 1 | **2026-11-19** | Free, open-source exam prep for Nigerian students across JAMB, WAEC and NECO. 🟢 **Pushed on the day of this pass** — the clearest evidence for `911-F3`'s claim that this tier is *live and ungranted* rather than abandoned, and this one **is** granted. | EMEA — Nigeria |
| **KCSE-predictor** | https://github.com/001kenji/KCSE-predictor | Apache-2.0 (11,357 B · `c71d239df917`) | 1 | 2026-01-05 | Predicts likely examination topics by analysing **20+ years of KCSE past papers**. 🔵 **The method is the asset, not the prediction**: a longitudinal corpus of a national board's own papers is the input a studio needs for item generation and blueprint analysis, and Kenya's National AI Strategy 2025–2030 puts higher-education institutions at the centre of implementation (`intel/market.md` EMEA). 🟡 No published accuracy evaluation — treat the predictive claim as unvalidated. | EMEA — Kenya |
| **ICFES-Exam-Engine** | https://github.com/theteacherbot/ICFES-Exam-Engine | MIT (1,067 B · `95927f6f69fa`) | 0 | 2026-08-01 | Generates Saber 11 / ICFES-style assessments. 🟢 **The first Colombian examination agent this KB has ever carried**, and `911-F4` finds Colombia has the deepest permissive exam tier of the four LATAM markets measured — ahead of both Brazil and Mexico, which inverts the order market size would suggest. | LATAM — Colombia |
| **paes-ensayos** | https://github.com/matmiidu/paes-ensayos | MIT (1,065 B · `db233fe3a19a`) | 0 | 2026-08-12 | Configurable PAES mock exams: the user chooses the test, the content axes and the number of items. 🟢 **The first Chilean `PAES` row in this KB.** 🔵 Chile is also the region's most advanced regulator — National AI Policy since 2021 with a law in discussion — so a Chilean engagement has both an open starting point and a published compliance target. | LATAM — Chile |
| **Study-assistant** | https://github.com/Reethureddy8/Study-assistant | MIT (1,069 B · `ff3eb0698f8a`) | 2 | 2026-10-28 | Grounded RAG study assistant over **NCERT Class 9 Science** that **cites its sources**. 🟢 **Citation-grounding is the property that matters here**, not the size: it is the acceptance test `P23` is built around and the control India's own coverage says is missing. | APAC — India |
| **RAG-Enhanced-NCERT-Tutor** | https://github.com/praj2408/RAG-Enhanced-NCERT-Tutor | MIT (1,072 B · `8a909947f61b`) | 6 | 🔴 2024-10-20 | AI tutor over the NCERT curriculum. 🔴 **Two years without a push** — carried as a worked reference for the retrieval layer over NCERT material, **not** as a maintained dependency. | APAC — India |
| **Ncert__RAG__Chatbot** | https://github.com/MichealQuelazar/Ncert__RAG__Chatbot | MIT (1,075 B · `13908cd9b08e`) | 1 | 🔴 2025-12-18 | Full-stack application turning NCERT textbooks into a conversational tutor. 🟡 Self-described as production-ready at `1 ★` with no push in eleven months; the **full-stack shape** is the useful part. | APAC — India |
| **Sanshodhan** | https://github.com/datastiltskin/Sanshodhan | MIT (1,073 B · `909fd4f320c0`) | 1 | 2026-10-21 | **A `git diff` for NCERT textbooks across editions** — shows what changed in the national curriculum over time. 🟢 **The most original artefact in this section and the one with no equivalent anywhere in this KB.** 🔵 **Why it matters commercially**: every curriculum-aligned product this KB scopes (`P22`, `P23`, `P29`) silently assumes the curriculum is static. India's AI-and-computational-thinking rollout changes the syllabus from Class 3 in 2026-27 and Classes 9–10 in 2027-28, so **curriculum drift is a live maintenance cost**, and this is an instrument for measuring it. | APAC — India |
| **ePäko** | https://github.com/lindnerju/ePaeko | MIT (1,086 B · `5a44d126d2e6`, on `master`) | 3 | 🔴 2024-01-24 | Interactive tool for choosing Abitur examination subjects (`Prüfungsfachwahl`). 🟡 **Germany's only promotable row from this channel, and it is a form-logic helper rather than an AI agent** — which is itself the finding: the `Abitur` leg returned the pass's worst collision rate and just `7` nominal hits when co-termed (`911-F2`), so German examination supply is **unreachable on this channel**, not merely absent. | EMEA — Germany |

🔴 **Ten rows, and the number is the finding rather than a shortfall.** `14` terms × `2` query forms
returned `491` distinct repositories and `205` with education context; `32` carried a permissive
licence *field*; `19` were byte-read; `10` are agents worth a row here and `9` went to
`repos/foundations.md` and `verticals/solutions.md`. 🔵 **Fewer real rows beat padding** — and the
funnel from `637,622` nominal hits to `10` published agent rows is the honest cost of this channel.

## Ethiopia's national-examination tier — added `p912`, discharging `911-G4`

`911-G4` registered Ethiopia as a market that **surfaced by accident and was never queried**: two
Ethiopian artefacts arrived on `p911`'s South-African `matric` legs, which is a homonym, not a
channel. It is queried now — five terms, bare and co-termed, `43` distinct repositories — and the
result is the **most ungranted and lowest-ceiling market this KB has measured** (`912-F3`).

🟢 **Every grant below was byte-read on the resolved default branch with
`ingest/p912-grant-family.sh`**, this pass's corrected authority instrument — not with
`p880-licence-byteread.sh`, which `912-F2` measures getting two of this cohort's five granted
repositories wrong. Per-row evidence: `evidence/p912-grant-family.2026-11-19-p912.tsv`.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **Ethio-Adaptive-Learning** | https://github.com/DeepBlue-dot/Ethio-Adaptive-Learning | Apache-2.0 (11,357 B · `c71d239df917`) | 7 | 2026-05-31 | AI-driven adaptive learning for Ethiopia's Grade 12 national examination, in TypeScript. 🟢 **The ceiling of the entire Ethiopian cohort at `7 ★`** and the only row in it above `3`. 🔵 Standard unmodified Apache-2.0 payload — byte-identical to `Jambora` and `KCSE-predictor` above, which is what a stock `LICENSE` from GitHub's picker looks like. 🟡 **A diverged copy exists**: `abm74/Ethio-Adaptive-Learning` carries the byte-identical licence file but a **different HEAD** (`336bf17` vs `3ad39ba`, `git ls-remote --symref`, `2026-11-19`), so it is a fork with its own commits, **not** a fold-duplicate — do not collapse the two. | EMEA — Ethiopia |
| **ethioexam** | https://github.com/ElnatanAnbelu/ethioexam | MIT (1,072 B · `fba331165d0b`) | 0 | 2026-09-20 | **Offline** practice application for the Grade 9–12 Natural Science national examination (names both ESSLCE and EUEE). 🟢 **The offline property is why it earns a row at `0 ★`**: it is the only artefact in this cohort built for the constraint that actually governs Ethiopian deployment, and it belongs to the same class as `kolibri` and `iiab` in `verticals/solutions.md` — low-connectivity delivery — rather than to the tutor class. | EMEA — Ethiopia |
| **eaes-bot** | https://github.com/robelasefa/eaes-bot | MIT (1,067 B · `cb1a9de3b176`) | 1 | 2026-09-16 | Telegram bot that tracks EAES examination results and notifies students when they publish. 🔵 **The delivery surface is the finding, not the code** (`T22`): where a board publishes results as a web drop and candidates have no institutional account, the **messaging channel is the product**, and this is the cheapest worked example of it this KB holds. | EMEA — Ethiopia |

🔴 **Three rows out of 43 repositories, and the posture behind them is the commercial answer.**
`81.4%` of the cohort carries **no licence file at all**, `70%` sit at **zero stars**, **none**
clears `100 ★`, and the ceiling is `7`. 🟡 **It is not abandonment**: `40%` were pushed on or after
`2026-09-01` and three within the seven days to `2026-11-19`. 🔵 **So Ethiopia is a build, and the
build has a named substrate** — EUEE/ESSLCE past papers and the adaptive shape `Ethio-Adaptive-Learning`
already demonstrates — but **nothing here is a dependency**. Measured in
`evidence/p912-ethiopia-rows.2026-11-19-p912.tsv`; legs in `evidence/p912-ethiopia-legs.2026-11-19-p912.tsv`.

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

## Skill-packaged teaching agents and generic LMS bridges — added `p914`

Fourteen addresses added. Discovery channel: `gh api search/repositories` over seven
education-shaped queries bounded by `pushed:>2026-09-01`; grant adjudicated by
**`ingest/p913-grant-authority.sh`** (the corrected authority), byte-read on the resolved
branch. Metrics and grants per row:
`evidence/p914-new-supply-metrics.2026-11-19-p914.tsv`,
`evidence/p914-new-supply-grants.2026-11-19-p914.tsv`.

🔵 **Two channels, 24 addresses, zero family disagreements** on the 16 rows where the API named
a licence. That is not a contradiction of `p913`'s 15.4% change rate: `p913` re-adjudicated
*published cells* graded by a defective instrument, and this pass measured *fresh* addresses with
the corrected one. The channels disagree about **old verdicts**, not about bytes.

| Agent | Repo | Licence (byte-read `p914`) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **teacher-to-skills** | https://github.com/JuneYaooo/teacher-to-skills | **Apache-2.0** (`main/LICENSE`, 11,358 B, `sha256₁₂ cfc7749b96f6`) | 486 | 2026-11-07 | Distils a *named human teacher's* material into a source-backed agent skill that teaches until the learner is independent. Python. The retrieval contract is "source-backed", so the citation trail is a first-class output rather than a prompt instruction. | APAC — China |
| **WordLink** | https://github.com/orionsheep/wordlink | **MIT** (`main/LICENSE`, 1,093 B, `sha256₁₂ b0f3e0f68927`) | 427 | 2026-11-05 | Vocabulary learning on a **fine-tuned 1.5B model (SFT + DPO) that runs offline in the browser**. TypeScript. 🟢 The only row in this cohort that ships its own trained weights and needs no inference vendor at all. | APAC — China |
| **moodle-ai-skill-navigator** | https://github.com/Berserk-hub150/moodle-ai-skill-navigator | 🔴 **GPL-3.0** (`main/LICENSE`, 35,153 B, `sha256₁₂ ebdc0e5b7005`) | 279 | 2026-11-07 | Moodle plugin: tutoring, quiz generation, mind maps and RAG over course material. PHP. The most featured AI Moodle plugin measured in this base — and copyleft, which for a Moodle plugin is the *expected* posture, not a trap. | EMEA/Global — Moodle plugin estate |
| **AILearningGuide** | https://github.com/Fazmin/AILearningGuide | **MIT** (`main/LICENSE`, 1,081 B, `sha256₁₂ e29ef713b542`) | 259 | 2026-11-15 | Desktop app, **58 labs** across ML fundamentals, transformers, RAG, agents, fine-tuning and quantisation. TypeScript. Curriculum-as-application: the labs are the product, not documentation around one. | Global |
| **cram-engine** | https://github.com/liuliu667/cram-engine | **MIT** (`main/LICENSE`, 1,064 B, `sha256₁₂ c33ea68946e4`) | 181 | 2026-10-22 | Exam-cram skill built on **explicit learning-science stages** — four-phase interactive teaching under a hard time budget. Chinese-language. 🟢 States its pedagogy as the architecture, which is what `P23`'s acceptance test needs. | APAC — China |
| **SelfSemester** | https://github.com/munitkala/SelfSemester | **MIT** (`main/LICENSE`, 1,081 B, `sha256₁₂ f5fe104e348d`) | 108 | 2026-11-16 | Turns any subject into a **full scheduled, graded course** — built *and marked* by the user's own agent runtime. **Rust**, Windows. Created 2026-11-04: 108 ★ in twelve days. | Global |
| **brightspace-mcp-server** | https://github.com/RohanMuppa/brightspace-mcp-server | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 047079fbd491`) | 68 | 2026-11-18 | MCP server for **D2L Brightspace**, stated to work with *any* school rather than one tenant. TypeScript. 🟢 **This closes the seam `verticals/solutions.md` recorded for D2L**, which until now had only `POLITEMALL-MCP` — a two-system Singapore-specific bridge. See `T42`. | North America — D2L's core market |
| **claude-moodle-dev** | https://github.com/SaadRahman01/claude-moodle-dev | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ df0b3e71710c`) | 42 | 2026-06-22 | Moodle **development** toolkit for coding agents: skills for XMLDB, Hooks API, PHPUnit, Behat, AMD, privacy/GDPR and security review. Python. Not a learner tool — it is the tier that makes a Moodle plugin engagement go faster, and it is permissive while Moodle is not. | Global |
| **Tov-learn** | https://github.com/TovTechOrg/Tov-learn | **MIT** (`master/LICENSE`, 1,064 B, `sha256₁₂ 092d389ac156`) | 36 | 2026-09-29 | Tutor skill with **spaced repetition**, personalised project examples and a visual progress dashboard. PowerShell. | EMEA — Israel |
| **chemdraw-mcp** | https://github.com/jurimaxam-dotcom/chemdraw-mcp | **Apache-2.0** (`main/LICENSE`, 11,358 B, `sha256₁₂ cfc7749b96f6`) | 32 | 2026-11-18 | MCP server that draws **structures, reactions, mechanisms, peptides and proteins locally**. Python. The first STEM-notation generator in this base: chemistry teaching needs a renderer, not a chat turn, and local rendering keeps student work off a vendor. | Global |
| **SOLA** (`moodle-local_ai_course_assistant`) | https://github.com/saylordotorg/moodle-local_ai_course_assistant | 🔴 **GPL-3.0** (`main/LICENSE`, 35,149 B, `sha256₁₂ 3972dc9744f6`) | 21 | 2026-11-19 | *Saylor Online Learning Assistant* — AI learning-coach Moodle plugin. PHP. 🟢 **Published by Saylor Academy itself**, a named non-profit provider, not by an individual. Pushed *today*. See `T42`: the institution-published limb. | North America — Saylor Academy |
| **liu-xiaoyan-skill** | https://github.com/tong666-bit/liu-xiaoyan-skill | **MIT** (`master/LICENSE`, 1,068 B, `sha256₁₂ 8626b7112026`) | 21 | 2026-10-09 | CET-4/6 and postgraduate-entrance English coach: reading evidence, listening review, long-sentence parsing, essay marking, revision plan. Styled after a named Chinese test-prep teacher, explicitly unofficial. | APAC — China |
| **ku-portal-mcp** | https://github.com/SonAIengine/ku-portal-mcp | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ aa35608133a4`) | 13 | 2026-10-03 | MCP server for **Korea University**'s KUPID portal *and* Canvas: notices, schedules, library seats, assignments, grades. Python. First Korean campus bridge in this base; the library-seat call is a reminder that the useful campus agent is mostly not academic. | APAC — South Korea |
| **ieee-mcp** | https://github.com/danieltyukov/ieee-mcp | **MIT** (`master/LICENSE`, 1,071 B, `sha256₁₂ fc20bfdfe931`) | 7 | 2026-11-14 | MCP server for **IEEE Xplore** — search, cite and read, with no IEEE API key, full text resolved **through the user's own university subscription**. TypeScript. 🔵 Same credential posture as `T30`: entitlement stays with the learner, so procurement is not on the critical path. | Global |

### 🔴 Refused this pass — four addresses that would have passed a star filter

| Repo | ★ | Why it is not in the table above |
|---|---|---|
| https://github.com/aaryansamanta/AI-Ethos | **497** | 🔴 **No licence payload.** 16 names over 3 branches, all `404`; API SPDX `NONE`. The highest-starred find of the pass, a 501(c)(3) delivering multilingual tutoring to underserved learners — and nothing in it can be redistributed. |
| https://github.com/jeremy-xuan/SocraticNovel | 32 | 🔴 **CC BY-NC-SA 4.0** (1,227 B, `sha256₁₂ 593122cbd00b`). **NonCommercial** — unusable in a client deliverable at any tier. An instance of `T32`. |
| https://github.com/vincenzo-afk/KingstonConnect | 41 | 🔴 **No licence payload** (16×3 ladder, all `404`). College management platform with an embedded StudyGPT. |
| https://github.com/Piyushtanwani/DAU-buddy | 7 | 🔴 **No licence payload** (16×3 ladder, all `404`). Campus MCP server for DA-IICT, India. |

### 🟡 Admitted with the grant split named — and `p640`'s size band earned its keep

Both rows below carry an **MIT title line outside the 1,000–1,250 B band**, which is exactly the
condition `p640` wrote the band to catch. The authority flagged both as `MIT-TITLE-OUT-OF-BAND`;
reading the payload confirmed a split grant in both. 🟢 **Two for two — a positive control for the
band, recorded because this base has never had one.**

| Repo | ★ | Payload | What the split actually is |
|---|---|---|---|
| https://github.com/aaryansamanta/NextGen-AI | 491 | 1,327 B · `31d2ea3bba94` | **MIT for source code only.** Brand assets, team photos, videos, logos and the top-level PDFs in `website/img`, `website/video` are reserved © NextGenAI and require written contact before reuse. 🟢 The *code* is usable; the org's identity material is not, which is the correct and unremarkable posture — it is only a trap for a scanner that reports one licence per repo. |
| https://github.com/Andiii208/seu-handbook-skill | 55 | 1,497 B · `965a0edb5701` | 🔴 **MIT on the code, CC BY-NC-SA 4.0 on `references/` and `data/`** — the Southeast University student handbook text, which *is* the product. The skill's whole value is the clause-level handbook corpus, and that corpus is **NonCommercial**. Ship the retrieval code, re-author the corpus, or do not ship. A textbook instance of `T25`, now with the MIT band as its detector. |

## Oral reading fluency, degree audit and advising agents — added `p916`

🔴 **The first four rows exist in a tier this base published as a *void*.** `P17`'s oral-reading-fluency
void was declared at the sixth pass and "reproduced exactly" as recently as `p890` at
`total_count = 4`. It was an artefact of query shape: `oral reading fluency assessment` AND-matches
four terms and returns **4**; `"reading fluency"` returns **102**. Every row below fails that AND on
a word, not on substance — `ReadPulse` even carries the phrase *"oral reading fluency"* verbatim and
is excluded because it says *"Assesses"* and not *"assessment"*. See `agents/trending.md` `916-F3` —
and note that *nothing about the tier changed*, only the question. Every grant below is byte-read on
the resolved branch with `ingest/p913-grant-authority.sh`; every **Origin** is from a byte-read
`README`, never from an owner name (`912-F4`), and where the README carries no country signal the
cell says so rather than guessing.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **Poodll ReadAloud** | https://github.com/justinhunt/moodle-mod_readaloud | 🔴 **GPL-3.0-or-later — and there is no licence file.** Byte-read over 16 filenames × 3 branches: `404` on every one. The grant is in the `README` (*"License: GNU GPL v3 or later"*) **and in the full GNU header block of `version.php`, `lib.php` and `mod_form.php`**. See `916-F2` — 🟢 **independently reproduced `p917`** by `ingest/p917-header-layer.sh`, which discharges `916-G2` and makes this the general rule for the ecosystem: *for a Moodle plugin, `version.php` is the grant authority, not `LICENSE`* (2 of 2 plugins measured) | 6 | **2026-10-28** | Guided reading-fluency + comprehension activity for Moodle: student listens, practises line by line, reads aloud; **speech recognition scores words-per-minute and accuracy automatically**, then an optional comprehension quiz. The only actively-developed artefact in the tier | Global (Moodle plugin) |
| **AIRFluTe** | https://github.com/OSU-slatelab/AIRFluTe | 🟢 **Apache-2.0** | 3 | 2022-12-08 | *An Intelligent Reading Fluency Teacher.* Streaming deep models fine-tuned on **children's** speech; real-time visual tracking plus a teacher model that prompts with synthesised voice on a hard word | **North America** — Ohio State SLaTe lab (from README) |
| **LEPIC** | https://github.com/JambuOverflow/lepic | 🔴 GPL-3.0 | 7 | 2021-07-11 | Android/iOS app for teachers and literacy professionals: upload a student's read-aloud recording, mark the errors, get duration and words-per-minute. **Won the ICSE 2021 Student Contest on Software Engineering** | **LATAM** — Brazil, University of Pará (from README) |
| **ReadPulse** | https://github.com/dungnotnull/ReadPulse-AI-Agent | 🟢 **MIT** | 3 | 2026-09-15 | Virtual reading-specialist **voice agent** on AssemblyAI; assesses a read-aloud in conversation. Three months old — read it as a reference implementation, not an upstream | 🟡 not placed — README carries no country signal |
| **DegreeWorks CLI** | https://github.com/Aaryan-Kapoor/degreeworks-cli | 🟢 **MIT** | 5 | 2026-10-08 | Read-only CLI over **Ellucian DegreeWorks** that *"lets an AI agent build your exact semester schedule"* from real sections. 🔵 **Textbook `T30`**: a bridge to a commercial registrarial system, built per-institution on the **user's own credentials**, needing no institutional consent | **North America** — Kennesaw State (from README) |
| **Compass** | https://github.com/Kanjo-Elkamira-Ndi/Compass | 🟢 **MIT** | 11 | 2026-08-12 | *"Turns a standard student information system into an AI-powered academic advisor."* The advising tier's only permissive, currently-maintained agent | **EMEA** — **Cameroon** (from README). 🟢 The second Africa-origin row this base holds, after `elimu-ai` |

🔵 **Why the advising pair matters more than its star counts.** `degreeworks-cli` and `Compass`
bracket the same problem from opposite ends: one reaches *into* a commercial SIS/degree-audit
product on the student's own login, the other sits *on top* of whatever SIS an institution runs.
Both are MIT. For an engagement where the client's registrarial system is a vendor product with no
agent story — which is most of them — these are the two shapes available, and `P12`'s
UniTime-based pattern is the third.

🔴 **What this table does not contain.** No APAC-origin row. Eleven discovery legs produced none,
which is a statement about these eleven angles and not about APAC supply — `p906` measured a full
Mandarin tier at scale. It is written down because an unstated absence reads as coverage.

## Study, recall and grading-bridge agents — added `p915`

Nine addresses from twelve discovery legs (angles distinct from `p914`'s seven), every grant
byte-read on the resolved branch with `ingest/p913-grant-authority.sh`. The cohort's centre of
gravity is **spaced repetition** and **the grading bridge** — not the chat tutor.

🔴 **Two rows in this table are copyleft and the reason is structural, not incidental.** See `T42`:
`anki-mcp-server-addon` runs *inside* an AGPL-3.0 host and inherits its grant, while the same
owner's `anki-mcp-server` — which talks to Anki from outside the process — is MIT. The process
boundary is the licence boundary.

| Agent | Repo | Licence (byte-read `p915`) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **LearnKit** | https://github.com/ctrlaltwill/LearnKit | **MIT** (`main/LICENSE.md`, 1,068 B, `sha256₁₂ 38a90d0f7738`) | 185 | 2026-10-31 | Turns an **Obsidian vault** into a study system: flashcards, spaced repetition, review queue and analytics over notes the learner already wrote. TypeScript. 🔵 No content ingestion step — the corpus is the learner's own notes, which sidesteps the content-licence trap `T25` describes | Global |
| **flashcards-open-source-app** | https://github.com/kirill-markin/flashcards-open-source-app | **MIT** (`main/LICENSE`, 1,070 B, `sha256₁₂ 0e319ca9aaa9`) | 119 | 2026-11-19 | AI-generated flashcards for daily study across **iOS, macOS, Android and web** — exam prep and vocabulary. TypeScript. The only cross-platform-native row in this cohort | Global |
| **anki-mcp-server-addon** | https://github.com/ankimcp/anki-mcp-server-addon | 🔴 **AGPL-3.0** (`main/LICENSE`, **227 B**, `sha256₁₂ 34b58d896fdb`) — a **by-reference** grant, see `T43` | 104 | 2026-11-17 | An **Anki addon** implementing an MCP server, so an agent reaches the live deck from inside the application rather than over a side channel. Python. 🔴 **Inherits AGPL-3.0 from Anki itself; may not be bundled in a closed deliverable.** Use the MIT `anki-mcp-server` row above for that | Global |
| **true-recall** | https://github.com/pieralukasz/true-recall | **MIT** (`main/LICENSE`, 1,070 B, `sha256₁₂ 23444362494b`) | 68 | 2026-11-16 | Native spaced repetition for **Obsidian**: AI-generated cards, **FSRS v6** scheduling, image occlusion, retention analytics. TypeScript. 🟢 The most current scheduler generation measured in this base | Global |
| **studiamo** | https://github.com/NaEs25/studiamo | 🔴 **AGPL-3.0** (`main/LICENSE`, 33,880 B, `sha256₁₂ f0c3e444e06d`) | 27 | 2026-10-30 | Turns YouTube videos, PDFs and notes into active-recall flashcards with spaced repetition, **fact verification** and Telegram delivery. Python. 🔵 The fact-verification stage is what `P23`'s hallucination gate asks for, shipped as a pipeline step | 🟡 EMEA — Italian-language project name; **origin inferred from naming, not verified** |
| **ProcrastiLearn** | https://github.com/Vladyslav-Soldatenko/ProcrastiLearn | **Apache-2.0** (`master/LICENSE`, 11,351 B, `sha256₁₂ 45386cd5bf35`) | 24 | 2026-11-01 | Android app that **gates chosen apps** (TikTok and the like) behind flashcard reps — opening a gated app triggers a full-screen review. Kotlin. 🔵 Distribution mechanism rather than content: the intervention is placed where the attention already is | Global |
| **Exam_Intellect** | https://github.com/RakeshBabuGajula/Exam_Intellect | **MIT** (byte-read on `ExamIntellect/LICENSE`, 1,075 B, `sha256₁₂ a4e58d1074c9`; the identical payload is also on `master`) | 19 | 2026-10-15 | AI proctoring dashboard: live exam monitoring, student analytics, automated feedback. Python. 🟡 **There is no `main` branch** — content lives on `master` and on a second branch named `ExamIntellect` (both return 200), so a clone or submodule pin that assumes `main` will fail. 🔵 Measured, because `p915`'s grant ladder resolved it on the `ExamIntellect` branch and the default-branch assumption would have been wrong either way | Global |
| **gradescope-mcp** | https://github.com/Yuanpeng-Li/gradescope-mcp | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 29d0f3f4463a`) | 8 | 2026-11-12 | 🟢 **The first Gradescope bridge in this base.** MCP server letting an agent **grade against a rubric**, review regrade requests and manage assignments. Python. 🟢 **Every write is previewed before it is applied** — the human-in-the-loop control Oklahoma SB 1734 and `T1`'s grading statutes require, shipped as a default rather than written into a policy document. `P35` is built on it | North America — Gradescope's core market |
| **Chinese-Teaching-AI-Agent** | https://github.com/forgemorrow/Chinese-Teaching-AI-Agent | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 2e7ffdde3eb5`) | 8 | 2026-11-14 | Lesson-prep assistant for **K-12 Chinese-language teachers**, built on Streamlit with the MiMo/Anthropic SDK. Python. 🔵 Teacher-facing rather than learner-facing, and in-language — the shape `T29` found the vernacular supply tier to be missing | APAC — China |

🔴 **Three addresses were refused this pass and the refusals are recorded, not discarded.**
`narender-rk10/MyProctor.ai-…-PROCTORING-SYSYTEM` (**237 ★** — the pass's highest-starred find)
carries **no licence payload** on 16 filenames × 3 branches; `bahfahh/engram-quest` (33 ★) ships a
**bespoke `Engram Quest Plugin License Version 1.1, November 2026`** (2,701 B), which is not an OSI
grant; and `vosslab/vosslab-skills` (6 ★) is **unverifiable** — `search/repositories` reports it as
MIT while every licence filename returns `404` and the per-repository endpoint returns `403` under
this session's scoping. 🔵 The third is the one with a method consequence: **a search-reported
licence is not an independent second channel.** Full audit in `agents/trending.md` `915-F7`.

## Maths tutoring with retrieval — added `p917`

One row, and the ratio behind it is the finding. **28 discovery legs this pass produced exactly one
new education-specific agent.** The other eleven promotions are credential *infrastructure*
(`repos/trending.md` `917-R1`). New supply in this field is arriving as infrastructure, not as
agents, and this file should say so rather than pad.

| Agent | Repo | Licence (byte-read) | Stars | Last push | Origin | What it does |
|---|---|---|---|---|---|---|
| **llm-math-education** | https://github.com/DigitalHarborFoundation/llm-math-education | **MIT** (`main/LICENSE`, 1,073 B) | 47 | 2026-11-14 | **North America** — `digitalharbor.org` in `pyproject.toml` | Retrieval-augmented generation for **middle-school mathematics**: question answering and *hint* generation, with the retrieval corpus separated from the generator so a district can swap in its own curriculum |

🔵 **Why the hint path matters more than the answer path.** This base's grading and tutoring tiers
are full of systems that produce an answer; `llm-math-education` is built to produce a *hint*, which
is the output an intelligent-tutoring deployment actually needs and the one `CAHLR/OATutor`'s
scaffolded-hint design already assumes. It composes with OATutor's BKT mastery estimates without
either project knowing about the other — see `compose/patterns.md`.

🟡 **Placed on the manifest layer, not the README.** Its README carries no country signal at all.
The placement comes from an institutional e-mail domain in `pyproject.toml`, via the new
`ingest/p917-affiliation-manifest.sh`. That instrument's first cut was wrong in two ways and both
are recorded at `917-F6`: a consumer mail host (`gmail.com`, `posteo.me`) is not an affiliation, and
an npm version string (`pkg@1.0.1.patch`) is not an e-mail address.

## APAC vernacular education agents — added `p918`, discharging `917-G3`

🔴 **Tier verdict: `PRESENT — NOT DELIVERABLE`** under the threshold published in
`repos/trending.md` `918-R1` (≥ 50 ★ · a byte-read grant that is not `NONE` · pushed within
180 days). The estate is **157 repositories this base had never seen**, found by querying in
Mandarin, Japanese, Korean and Vietnamese rather than English — and its best permissive member is
**36 ★ and 383 days idle**. Every row below is real, and **none is adoptable as a dependency.**

🔵 **Read this table for the requirement, not for the code.** It is the first direct evidence in
this KB of what APAC teachers and institutions are actually building, in their own idiom — including
an **admissions advisor**, the category `README.md` names as the largest build-vs-adopt gap in the
industry and for which this base has found no open agent anywhere in the world.

| Agent | Repo | Licence (byte-read `p918`) | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| **AI-Course-Generator** | https://github.com/GitHubDaily/AI-Course-Generator | **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 5297e38c125c`) | 36 | 2025-11-01 | Teacher-facing course-outline and teaching-content generation, built on the **iFlytek Xingchen** agent platform. 🟡 **The highest-starred permissive, byte-read education agent in the entire APAC vernacular estate — and 383 days idle** | APAC (China) |
| **AI-LaBuddy** | https://github.com/kenoharada/AI-LaBuddy | **MIT** (1,067 B, `sha256₁₂ 807c3b4466ec`) | 22 | 2023-07-02 | Automates and streamlines research-laboratory tasks with LLMs and deep learning. 🔴 Three years idle — the *higher-education research lab* use case, which no other row in this file addresses | APAC (Japan) |
| **Dawn** | https://github.com/jetyu/Dawn | **Apache-2.0** (11,340 B, `sha256₁₂ bef48216cd56`) | 14 | 2025-07-20 | Spring Boot + Vue.js teaching platform with AI-assisted instruction built in. 🔵 The only **Apache-2.0** row in this tier — a patent grant, where the rest are MIT | APAC (China) |
| **AI-EduForge** | https://github.com/hapince-code/AI-EduForge | **MIT** (1,072 B, `sha256₁₂ 0a83fabb2ba6`) | 6 | 2026-05-11 | K-12 teacher resource generation: lesson PPTs, React interactive courseware, PDF test papers, textbook-aligned material. 🔵 **Multi-artefact output from one brief** — closer to the teacher's actual workflow than any single-artefact generator in this file | APAC (China) |
| **heuristic-learning-system** | https://github.com/SNOOPY-alt/heuristic-learning-system | **MIT** (1,067 B, `sha256₁₂ f0012497d3e1`) | 6 | 2025-05-04 | Heuristic guided-tutoring system built on the **Dify** platform. 🔵 Evidence that the vernacular tier builds on a *platform* rather than raw model calls — and 🔴 Dify is not OSI-permissive, so the harness is not inheritable with the agent | APAC (China) |
| **ai-admissions-platform** | https://github.com/cxkzai/ai-admissions-platform | **MIT** (1,065 B, `sha256₁₂ 811e88db2038`) | 5 | 2026-07-02 | Multi-role **AI admissions-advisor** platform for small and medium training institutions, v1 focused on K-12 coding education. 🔵 **The admissions gap, addressed — in Chinese, at 5 ★.** Read it as a requirements document for the studio IP `README.md` argues is the most defensible in the industry | APAC (China) |
| **course-tutor** | https://github.com/uczltw6/course-tutor | **MIT** (1,082 B, `sha256₁₂ f4f4a2cdaa54`) | 5 | 2026-04-23 | Course teaching-assistant workbench that **distils a named teacher's instructional style**, with local pre-processing to cut token spend. 🔵 Two ideas this file has not recorded elsewhere: style transfer from a specific instructor, and cost as a design constraint | APAC (China) |
| **MathMind** | https://github.com/MathMindCanvas/MathMind | **MIT** (1,071 B, `sha256₁₂ 0773606d562e`) | 5 | 2026-02-26 | Maths teaching aid combining a drawing canvas, geometric computation and AI assistance | APAC (China) |
| **Montessori-Agentic-AI-Tutor** | https://github.com/mousam100/Montessori-Agentic-AI-Tutor | **MIT** (1,064 B, `sha256₁₂ a1adc7ed2fc0`) | 2 | 2026-05-20 | **Safeguarding-aware** agentic tutor for Montessori-inspired personalised education, pairing learner-level adaptation with a teacher view. 🔵 The only row in this file that treats **safeguarding as an architectural concern** rather than a policy note | APAC (India) |

🔴 **Refused from this tier — the two most-starred repositories the legs returned.**
`liyupi/ai-code-helper` (**769 ★**) and `ophiraShen/EasyDS` (**43 ★**) both return
`NO-LICENCE-FILE-FOUND` across 25 candidate filenames on 3 branches. They are the top of the
measured estate and they are **ungranted**, which is `T34` landing again: in the vernacular tier,
popularity and licence hygiene move in opposite directions. `ai-code-helper` is additionally a
*programming-career* project, not an education one — a reminder that a vernacular leg buys recall
at the cost of precision.

🔵 **Languages that returned nothing.** `pendidikan AI agen belajar` (Bahasa Indonesia) → **0** and
`การศึกษา AI` (Thai) → **0**; `शिक्षा AI` (Hindi) and `教育 AI エージェント` (Japanese) → **3** each.
These are **declared nil results, not unsearched regions** — Indonesia and Thailand have no
vernacular open education-agent supply reachable on this channel at all, against an APAC demand
picture (~86% South-East Asian teacher use) that `intel/market.md` records as large. Japanese supply
is found by `学習 支援 AI` (**60**) and not by the loanword shape, which is `T45` reproducing inside
a single language.

## Indonesia and Thailand — `918-G7` discharged, added `p919`

🔴 **`p918` recorded ZERO supply for both countries. For Indonesia that was a property of the query,
not of the world.** Re-asked on the **national curriculum programme** (`Kurikulum Merdeka`) and the
**teacher-facing artefact** (`modul ajar`, `guru`) instead of on `AI tutor Indonesia`, the channel
returned **10 repositories, none previously seen by this base**. Both channels on every row;
[record](../evidence/apac-id-th-supply.2026-11-19-p919.tsv).

🔴 **0 of 10 pass `918-R1`** (≥ 50 ★ · byte-read grant ≠ `NONE` · pushed within 180 days). The tier is
**`PRESENT — NOT DELIVERABLE` at the agent layer** — Indonesia is the fourth consecutive vernacular
tier to answer that way.

| Agent | Repo | Licence | ★ | Last push | What it does | Origin |
|---|---|---|---|---|---|---|
| GURU / Arjuna Quiz Engine | https://github.com/anandpatikat/guru-latihan-dinamis | 🔴 **none — no licence file on any probed path, on either branch** | 115 | 2026-11-19 | Generates printable curriculum-aligned assessments for Indonesian teachers. The most-starred Indonesian education agent this base has found — **and it is ungranted, so it cannot be built on** | Indonesia (LATAM-style community publishing; roadmap through 2026–27 is the author's target, not delivered scope) |
| Kurikulum-AI | https://github.com/JMLcommunity/Kurikulum-AI | 🟢 MIT (1,081 B, `sha256₁₂ 879619fd1e3d`, byte-read `p919`) | 46 | 🔴 **2020-06-14** | An AI curriculum in Bahasa Indonesia — teaching *material*, not an agent. Idle 6.4 years | Indonesia |
| modul-ajar-generator | https://github.com/NgodingCik/modul-ajar-generator | 🔴 **CC BY-NC 4.0** (17,688 B, `sha256₁₂ 2b275bb77aa6`, byte-read `p919`) — **noncommercial, and a *content* licence applied to a web application** | 2 | 2026-05-17 | Lesson-module (RPP) generator for PAUD/TK teachers. 🔵 This is what a **true** noncommercial positive looks like — the term is in the licence's name; see `919-F3` | Indonesia |
| kurikulum-merdeka-asesmen-skills | https://github.com/y4zh/kurikulum-merdeka-asesmen-skills | 🟢 MIT (1,065 B, `sha256₁₂ 1e41d9c6af01`, byte-read `p919`) | 0 | 2026-11-17 | Agent **skills** for lesson modules, assessment writing and exam conversion, split by school level. 🔵 The best permissive grant in the Indonesian tier, and the one asset here worth reading — it is already packaged in the shape this file names in *"the tutor as an agent skill"* | Indonesia |
| ebook-generator | https://github.com/dikkayulianto/ebook-generator | 🟢 MIT (1,070 B, `sha256₁₂ ceb34bc8f5b0`, byte-read `p919`) | 0 | 2026-11-19 | Generates ebooks from source material | Indonesia |

🔴 **Five further Indonesian repositories were measured and are not given rows: they are 0 ★ *and*
carry no licence file at all** — `ianbandanesse24-ai/Project-Guru-Digital-2026`,
`eldorray/modulajar-ai`, `odifunan4-ux/Guruku-ID`, `msjasukses/kurikulum`,
`adrianatiwi06-collab/edtech-kurikulum-merdeka`. 🟡 **`eldorray/modulajar-ai`'s README states MIT and
there is no `LICENSE` file on any probed path** — the claim is unbacked and the repository is
ungranted in fact. A README is not a grant.

### Thailand — the nil reproduces at the agent layer and collapses one layer down

🔴 **No open-source Thai education agent exists on this channel**, after the same reshaped method
(`ONET`, `TCAS`, `ระบบการศึกษา`). That nil is **informed**, not silent. 🟢 **The language substrate
underneath it is deliverable**, which is a different and more useful answer:

| Asset | Repo | Licence | ★ | Last push | Layer | `918-R1` |
|---|---|---|---|---|---|---|
| PyThaiNLP | https://github.com/PyThaiNLP/pythainlp | 🟢 Apache-2.0 (11,357 B, `sha256₁₂ b40930bbcf80`, byte-read `p919`) | 1,175 | 2026-11-13 | substrate | 🟢 **PASS** |
| thai2transformers | https://github.com/vistec-AI/thai2transformers | 🟢 Apache-2.0 (11,357 B, `sha256₁₂ 58d1e17ffe51`, byte-read `p919`) | 125 | 🔴 2023-11-06 | models | ❌ recency |
| OpenThaiGPT | https://github.com/OpenThaiGPT/openthaigpt | 🟢 Apache-2.0 (595 B, `sha256₁₂ b2a8a8f529b3`, byte-read `p919`) — 🔴 the search channel reports `NOASSERTION` for this repo; the two channels disagree and the bytes win | 121 | 🔴 2023-05-26 | models | ❌ recency |

🔵 **Why the substrate matters more here than elsewhere: Thai is written without spaces between
words.** A tutor that marks free-text Thai answers cannot tokenise them with whitespace, so a
segmenter is not an optimisation, it is a precondition. `PyThaiNLP` is the maintained permissive one.

🔵 **The rule this produced.** `918-R1` is applied **per layer**, not per region, and the layer is
published with the verdict — otherwise *"tier empty"* is ambiguous between *nothing here* and
*nothing to fork, and a maintained stack to build on*. See `repos/trending.md` `919-R1`.

## Mexico — measured for the first time in `p920`, discharging `919-G6`

`919-G6` recorded that **Mexico had never been measured**: two consecutive North America legs
returned no Mexican source, and this base's "North America" was the United States plus one Canadian
employment-law reference. Four Spanish-language legs were run in the `917-F1`/`919-F5` shape —
the **national curriculum programme** and the **teacher-facing artefact**, not topic words:
`Nueva Escuela Mexicana`, `planeación didáctica`, `CONALEP`, `telesecundaria`
([record](../evidence/mx-supply.2026-11-19-p920.tsv)).

| Measure | Value |
|---|---|
| Distinct repositories returned | **74** |
| 🟢 Previously unseen by this base | **74 — all of them** |
| 🔴 **Largest repository in the entire Mexican supply** | **2 ★** |
| Carrying any licence on the search channel | **4 of 74** |
| 🔴 Passing `918-R1` (≥ 50 ★ · grant ≠ `NONE` · pushed within 180 days) | **0** |

Eight were byte-read for their grant: `arenasarmando1510-creator/LUMO_Engine` (MIT, 1,082 B),
`Eltruko/planeatron` (MIT, 1,078 B), `azcayel-glitch/Simulador-docentes-IA-NEM` (MIT, 1,071 B) and
`Staryuc2209/Propuestas-Formativas` (**CC0-1.0**, 7,048 B — a *content* dedication on pedagogical
material, which is the honest licence for what it is); the other four —
`serviciosinformaticos132-dot/planeanem-ia`, `lalotg/nemapp`, `ybridondanger/aulyx.mx`,
`adrianavilananez-code/gestor-docente` — carry **no licence file on any probed path**.

🔴 **Mexico is the fifth consecutive vernacular tier to come back `PRESENT — NOT DELIVERABLE`, and
it is the most extreme one measured.** Indonesia's leader was 115 ★ (`919-F5`); the Mandarin,
Japanese, Korean and Vietnamese tiers topped out at 36 ★ (`918-F2`); **Mexico's is 2 ★.** The demand
signal is unmistakable and entirely uncommercialised: these are working teachers publishing
*planeación didáctica* generators aligned to the Nueva Escuela Mexicana for their own classrooms,
several of them pushed within the last month.

🔵 **What this means for a Mexican engagement, and how it differs from Thailand.** `919-R1` says to
grade the agent layer and the substrate layer separately. For Thai and Japanese that split is
load-bearing because the language itself needs a tokeniser nobody else ships. **Spanish does not**:
the substrate layer for a Mexican engagement is the global one this base already holds, so unlike
Thailand there is no second shelf to fall back to and no second shelf that is needed. **Build the
agent; adopt the Nueva Escuela Mexicana vocabulary** — the *campos formativos* and *ejes
articuladores* that every one of these 74 repositories encodes by hand, and which is the part a
foreign-built tutor gets wrong.

## What we searched for and did not find

Recording gaps because an unrecorded gap looks exactly like coverage.

- 🔴 **APAC produced nothing shelvable this pass, and that is stated rather than left as silence.**
  Of `p917`'s **17** promotion candidates, **zero** placed APAC on any channel — not the README, not
  a packaging manifest, not an institutional e-mail domain. The WebSearch leg for the region was
  not empty (EdTech Hub's ~86% teacher-use figure for Southeast Asia, the Philippines' DepEd
  `AGAP.AI` national programme launched January 2026), so the gap is **not** low AI activity: it is
  that the activity is not arriving as permissively-licensed public repositories this base can
  place. `917-G3`.

- 🟢 **The `OpenLiteracy` void CONFIRMED in a shape its original did not use (new `p917`).** This is
  the one of `p890`'s four remaining voids that survived re-measurement: `OpenLiteracy` → **0**,
  `"open literacy"` → **2**, `early literacy screener assessment` → **0**. The two hits are an AR
  Chinese character-recognition app with no grant and a newsroom *source-protection* literacy kit —
  neither is education literacy. 🔵 The other three voids were **refuted** by shape change alone
  (`agents/trending.md` `917-F1`), so a void that holds under a *different* instrument is now the
  only kind this file will publish.

- 🔴 **The five national examination boards `911-G1` named have all registered their GitHub
  namespace and published nothing into it (new `p912`).** `911-G1` prescribed the org channel as
  the cheap next probe — *"enumerate `WAEC`, `JAMB`, `KNEC`, `DEMRE` and `CENEVAL` as GitHub orgs
  before searching by acronym again"*. Run, on two channels, with a negative control:
  **`WAEC`, `KNEC`, `CENEVAL` and `NABTEB` all exist on GitHub and all four hold `0` public
  repositories**; `JAMB` is in the search index and also empty. 🔴 **`DEMRE`, `NECO` and `UNEB`
  resolve to accounts that are not the boards** — `demre` is a personal account holding a Next.js
  template and a movie app, `neco` is a Ruby PBX and ticketing shop whose every repository dates
  from 2009–2010, `UNEB` is a single `0 ★` hackathon repository idle since 2014. 🔵 **"Present and
  silent" is a better fact than "not found"**, and it is the one to take into a board conversation:
  the institution has already claimed its name on the platform, so the ask is publication, not
  onboarding. 🟡 **And the probe cannot be run on the channel this KB uses** — see `912-F1`:
  `search/repositories -f q='user:WAEC'` returns the **same `422` as a nonexistent owner**, so the
  prescribed enumeration needs the profile-page channel to mean anything. Evidence:
  `evidence/p912-board-owner-channel.2026-11-19-p912.tsv`.

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

## Corrections made in `p913`

- 🔴 **`OpenPronounce/OpenPronounce` was published here as `MIT` and is `AGPL-3.0`.** Byte-read
  `main/LICENSE`, **34,523 B**, `sha256₁₂ 0d96a4ff68ad`, title line
  `GNU AFFERO GENERAL PUBLIC LICENSE / Version 3, 19 November 2007` — the canonical AGPL-3.0 text at
  its canonical length. 🔴 **This is the most commercially consequential cell this base has
  corrected**, because the error ran in the *dangerous* direction: AGPL-3.0 **§13 imposes a
  network-use source-disclosure obligation**, so a hosted pronunciation service built on this row
  owes its source to that service's users, and the cell said the opposite. `P1`, `P9` and `P16` all
  cite pronunciation or oral assessment. 🔵 Run `G1` before scoping any of them against this row;
  it is usable as a **separate service**, not as a linked component of a closed deliverable.
- 🟢 **Three Mandarin rows re-confirmed rather than changed, and the instrument is the reason.**
  `ECNU/EduWork` and `wenliu3/ai-smart-homework-review` already carried **MulanPSL-2.0** here from
  `p906`'s byte-reads, and `p913` independently reproduced both from the title line with a detector
  the previous two authority instruments did not have — `p880` and `p912` both report these payloads
  `UNKNOWN-TEMPLATE` (see `913-F5`). 🔵 **The cells were right and the authority could not see
  them**, which is the same asymmetry `913-F1` found in the GNU family and the reason gate
  `913-G1` now exists.
- 🟡 **`yinuoguan/nengdou-ai-review-helper-web` — the recorded channel conflict is resolved in favour
  of the SPDX field.** This row reads *"Apache-2.0 byte-read — GitHub SPDX says `MulanPSL-2.0`.
  Channels disagree."* `p913` byte-read `main/LICENSE` at **9,247 B** and the title line is the
  **Mulan Permissive Software License v2**; the 11,356 B Apache payload the conflict was recorded
  against is not what that path serves now. 🔵 The row is left **flagged rather than rewritten**,
  because two passes have read two different payloads at one address and that is a *provenance*
  question, not a licence question. Registered as `913-G5`.
- 🔵 **`summeraprx/topik-shortcut` — the `NO GRANT` cell stands, and is now corroborated.** `p910`
  reached it on an 8-path ladder; `p913`'s 16-name × 3-branch sweep also returns no payload. **Two
  independent absence sweeps, same answer.**

## What `p913` searched for and did not find — the 38th consecutive nil supply leg

All eight prescribed legs ran (four global, four regional) plus two dedicated Ethiopian legs.
🔴 **Not one returned a repository this shelf does not already hold**, and this is stated rather than
left silent because an unrecorded absence reads exactly like coverage.

- **Global legs** (`top open source AI agents education 2026 github MIT`,
  `github trending education AI 2026`, `open source platform education ERP CRM MIT Apache`,
  `AI education industry trends 2026`) surfaced `HKUDS/DeepTutor`, `LearnHarness`,
  `geekjourneyx/interactive-learning`, `SirhanMacx/Claw-ED`, `TapXWorld/ChinaTextbook`,
  `microsoft/ai-agents-for-beginners`, `OpenEduCat` and `eduTrac SIS`. 🔴 **Every one is already on
  this shelf or in `verticals/solutions.md`.** `Nous Hermes` was named as an education candidate by
  one aggregator with **no education-specific evidence**, and is not promoted on that basis.
- **Regional legs** returned **demand-side corroboration, not supply.** The one exception paid
  heavily: the **Ethiopian** legs produced the first demand-side measurement of that market
  (`intel/market.md` EMEA, `T39`, `P32`).
- 🟡 **Two LATAM facts are new and are recorded in `intel/market.md`**: an **EdTech Hub / Fundación
  Ceibal** partnership on AI in education (September 2026), and a **second independent estimate of
  the LATAM university governance gap** — *"roughly 30% of Latin American universities have
  published AI-use policies"* — which **converges** with IESALC's 26%-formal-strategy figure this
  base already carries. 🔵 Two instruments, two samples, four points apart: recorded as
  **corroboration**, not averaged.
- 🔴 **The channel limit, re-stated:** `aiagentsdirectory.com` claims to track *21+ open-source
  education AI agents* and the search channel returns the claim without the list. **This base has
  never been able to read that index**, and it is the single most likely location of supply this
  shelf is missing. Registered as `913-G6`.


## Corrections made in earlier passes

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
