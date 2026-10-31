---
industry: education
region: Global
updated: 2026-10-31
---

# Foundational open source repos for education

The substrate an education engagement builds on or integrates with. 🔴 **Star counts and metadata on this page do NOT come from the GitHub REST
index** — `api.github.com` answers **403** to this session, scoped to the harness
repository. `p571` flagged this header as false and it survived the pass that
flagged it; `p572` corrects it. Figures on rows added or re-read in the tenth pass
were read from the **rendered repository page**, and every licence from the
**grant file itself** over `raw.githubusercontent.com`. 🔵 Per `570-A`: a star or
commit count is a claim a repository makes about itself; the licence text, the
dependency manifest and the behaviour of the code are the only signals here that
an author cannot unilaterally manufacture.
**Licences on rows added or re-read in the fourth pass were read from the licence
file itself** over `raw.githubusercontent.com` (HTTP 200 from this session, while
`api.github.com` and `github.com` HTML are 403), with byte counts recorded;
older rows carry GitHub's licence determination and say so where it matters.

**Read the licence column before the star column.** The platforms of record are
overwhelmingly **copyleft** — the opposite of the agent layer. Two exceptions
have now been established, and one of them is new this pass and important.

## Tenth pass (`p572`, 2026-10-31) — 🟢 THE LTI 1.3 AND xAPI LAYER WAS MISSING FROM THIS KB ENTIRELY, AFTER BEING RE-FOUND BETWEEN `70` AND `123` TIMES EACH

🟢 **Ten rows added, `7` of them permissive, and the tier they form is the one
every LMS engagement bills for: the integration plumbing.**

🔴 **This base has seen `3,455` distinct GitHub addresses across its history and
placed `170` of them on a shelf page — `4.9 %`.** 🔵 A selective shelf is correct;
**what was sitting in the discard is not.** Ranked by how many times the base
re-found an address without ever shelving it, the head of the unshelved list was
`openedx/edx-platform` (`218×`), `openedx/XBlock` (`123×`),
`bruchris/canvas-lms-mcp` (`115×`), `ls1intum/Artemis` (`97×`),
`opencast/opencast` (`93×`), `francoisjacquet/rosariosis` (`92×`),
`frappe/erpnext` (`84×`), `GibbonEdu/core` (`83×`), `yetanalytics/lrsql` (`70×`).

🟢 **`11` of the `12` addresses tested were absent from every shelf page
*entirely* — not named in prose, not linked, absent.** Only `edx-platform` was a
pure linking defect. 🔵 **So the gap was in shelving, not in discovery: this base
found this material repeatedly and had no step that placed it.** Registered as
`572-A`.

### 🟢 The permissive integration tier, now placed

| layer | repo | licence | why it matters |
| --- | --- | --- | --- |
| LTI 1.3 (Python) | `dmitry-viskov/pylti1.3` | **MIT** | attach to any LMS without forking it |
| LTI 1.3 (PHP) | `packbackbooks/lti-1-3-php-library` | **Apache-2.0** | the Moodle-native side |
| xAPI store | `yetanalytics/lrsql` | **Apache-2.0** | where learning-analytics statements land |
| Open edX components | `openedx/XBlock` | **Apache-2.0** | permissive components on an AGPL platform |
| Canvas control | `bruchris/canvas-lms-mcp` | **MIT** | shelved in [`../agents/top.md`](../agents/top.md) |

🔵 **The XBlock/edx-platform split is the single most useful licence fact added
this pass**: `XBlock` is Apache-2.0, `edx-platform` is AGPL-3.0. Client course
components can stay permissive on top of a copyleft platform.

### 🔴 Two instrument defects in this base's own grant ladder, both proven and both fixed

🔴 **A `5`-filename × `2`-branch ladder returned `NOASSERTION` for `4` addresses
this pass. Two of those four were the instrument's fault.**

| address | ladder said | truth | cause |
| --- | --- | --- | --- |
| `openedx/XBlock` | NOASSERTION | **Apache-2.0**, 11,358 B | file is `LICENSE.TXT` — **uppercase extension**, and `raw` paths are case-sensitive |
| `frappe/erpnext` | NOASSERTION | **GPL-3.0**, 35,149 B | file is `license.txt` — **lowercase** — and the default branch is **`develop`**, not `main`/`master` |
| `deepseek-harness-java/teacher-workbench` | NOASSERTION | 🟢 **genuinely ungranted** | confirmed at **40 probes** |
| `0x454447415244/HandwritingRecognitionSystem` | NOASSERTION | 🟢 **genuinely ungranted** | confirmed at **40 probes** |

🔴 **A `50 %` false-`NOASSERTION` rate on this sample**, and the two it got wrong
were a `471★` Apache-2.0 framework and a `40.8k★` ERP. 🟢 **Fix applied and
re-run: `4` branches (`main`, `master`, `develop`, `trunk`) × `10` filenames
including case variants — both resolved, both genuine nulls held.** 🔵 Corroborates
`p558` from a different direction: that pass found `121 of 374` addresses 404 on a
`main`-only read because of *version* branches; this one finds the same class of
failure from *filename case* and a `develop` default. **Ask (`572-B`): the ladder
must vary case and branch, and `NOASSERTION` must never be published from fewer
than the full ladder.**

### 🟢 A control worth recording: the sidebar and the grant file agreed `7` of `7`

🟢 For `Artemis`, `opencast`, `lrsql`, `pylti1.3`, `lti-1-3-php-library`,
`canvas-lms-mcp` and `rosariosis`, the GitHub sidebar licence matched the
byte-for-byte grant read. 🔵 **So the sidebar is reliable for licence *identity*
— and `570-B`'s `word-atlas` plus this pass's `malaysia-uec-teacher-workflow`
prove it is still blind to licence *scope*.** The rule that survives both:
**trust the sidebar for which licence, never for what it covers.**

## Ninth pass (`p571`, 2026-10-31) — 🔴 zero new addresses, and the pass's whole value is a shelving defect: a tier this base FOUND at pass 85 never reached this page

🔴 **`derived foundations rows: **7**` added this pass, and not one is a new
address.** All seven were discovered by **pass 85 (`2026-10-09`)**, recorded in
[`../agents/trending.md`](../agents/trending.md) as *"An item-generation tier
exists now, 5 of 5 MIT"* — and then **never promoted to a shelf page.** Verified
against `HEAD` before this pass wrote anything:

| repo | on `agents/top.md` at HEAD | on this page at HEAD |
| --- | --: | --: |
| all seven item-generation rows | 🔴 **0** | 🔴 **0** |

🔴 **Meanwhile [`../compose/patterns.md`](../compose/patterns.md) `P-571-A` has
been shipping the opposite claim** — *"nothing permissive generates
psychometrically defensible items"* — with its item-authoring step left to a bare
model prompt. 🔵 **The base knew since pass 85; its shelf and its patterns did
not.** This is trend 11 (*a closed gap keeps being published*) in its mirror
image: **an open finding that never got published.** It is corrected below.

### ⚠️ What this pass did NOT find, stated plainly

🔴 **`topic:question-generation` is NOT a virgin axis, and any claim that it is
would be false.** Pass 85 bought it (**227 repositories** then, **241** now) and
`Gap 352` records it as **deliberately refused at ~30% precision** — a costed
decision, not an omission. This pass re-opened it and confirmed that decision:
re-reading its top twenty returned **zero addresses new to this base**. 🔴 **Nine
consecutive passes with no new address from `WebSearch`**, and this pass adds
**four topic axes with no new address either**
(`question-generation`, `essay-scoring`, `language-learning`, `mooc`).

### 🟢 The item-generation tier, now shelved

Grants below carry **two independent reads**: the byte count pass 85 recorded, and
a re-read this pass over `raw.githubusercontent.com`. 🟢 **Five of five re-read
rows matched the recorded byte count exactly** — which corroborates the earlier
reads and the instrument at the same time.

| Repo | Licence (file) | ★ | Region | Build-on? | What it adds |
| --- | --- | --: | --- | --- | --- |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (1,070 B ✅ first-hand, `master/LICENSE`; sidebar agrees) | 138 | Global | ✅ permissive | 🟢 **"LTI 1.3 Advantage Tool" — the integration standard, in Python, under MIT.** Seen `95×` in this base's history and never shelved. Every engagement that attaches AI to Moodle / Canvas / Open edX / Blackboard without forking it goes through LTI 1.3, and this is the permissive Python implementation of it. 84 forks. |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | **Apache-2.0** (11,343 B ✅ first-hand, `master/LICENSE.md`) | 54 | North America | ✅ permissive | "A library used for building IMS-certified LTI 1.3 tool providers in PHP." 🟢 **The PHP side of the same standard — which is the side Moodle is written in.** Seen `75×`, never shelved. Packback is a Chicago company. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | **Apache-2.0** (11,357 B ✅ first-hand, `main/LICENSE`) | 144 | North America | ✅ permissive | 🟢 **"A SQL-based Learning Record Store" — the xAPI backbone, Apache-2.0.** 2,276 commits, 41 forks, Clojure. Learning analytics engagements need somewhere to put statements; this is the permissive place. Seen `70×` (plus `85×` for the sibling `yetanalytics/lrs`), never shelved. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** (11,358 B ✅ first-hand, `master/LICENSE.TXT`) | 471 | North America | ✅ permissive | 🟢 **"Framework for building custom learning components that run in the Open edX LMS!"** — and the licence split is the commercially decisive fact: **XBlock is Apache-2.0 while `edx-platform` itself is AGPL-3.0**, so a client's own course components can be built and kept under a permissive grant without the platform's network copyleft reaching them. 🔴 Seen `123×`, never shelved. 🔵 Its grant was invisible to this base's own ladder until this pass — the file is `LICENSE.TXT`, **uppercase extension**, and `raw.githubusercontent.com` paths are case-sensitive. |
| [githubharald/CTCDecoder](https://github.com/githubharald/CTCDecoder) | **MIT** (1,071 B ✅ first-hand, `master/LICENSE.md`) | 838 | EMEA | ✅ permissive | CTC decoding algorithms — best path, beam search, lexicon search, prefix search, token passing. **62 commits since `2017-10-09`** (3,036-day span). Deps are `numpy`, `editdistance`, `pytest` only — **licence surface clean**. The decode stage of any handwritten-work marking pipeline. |
| [githubharald/WordDetector](https://github.com/githubharald/WordDetector) | **MIT** (1,071 B ✅ first-hand, `master/LICENSE.md`) | 276 | EMEA | ✅ permissive | Detects handwritten words by classic image processing — no model to train, no GPU. Deps `numpy`, `opencv-python`, `scikit-learn`, `matplotlib`, `path` — **all permissive, surface clean**. The segmentation stage: it turns a scanned worksheet into word crops. |
| [arthurflor23/handwritten-text-recognition](https://github.com/arthurflor23/handwritten-text-recognition) | **MIT** (1,074 B ✅ first-hand, `master/LICENSE`) | 308 | Global | ✅ permissive | Handwritten Text Recognition — **3,645 commits over a 2,700-day span**, by far the most substantial history in this tier. 🔵 Deps include `tensorflow`, `mlflow` (both Apache-2.0) and `openai` (MIT) — permissive, but the `openai` dependency means the default path calls a **paid external API**, which is a data-residency question in schools, not a licence one. |
| [githubharald/DeslantImg](https://github.com/githubharald/DeslantImg) | ⚠️ **MIT grant (1,071 B) / GPL-3.0 SURFACE** — see note | 156 | EMEA | ⚠️ **link-only** | Deslanting: sets slanted handwriting upright before recognition. 🔴 **`master/LICENSE.md` is a clean 1,071 B MIT — and `requirements.txt` pins `Py-BOBYQA>=1.3`, which is GPL-3.0 (verified first-hand: 35,147 B, title "GNU GENERAL PUBLIC LICENSE", Version 3).** Py-BOBYQA is imported in-process for the deslanting optimisation, so **distributing a combined work triggers GPL-3.0 on it**. GPL-3.0 has no §13 network clause, so *hosting* a service is not itself the trigger — *shipping client code* is. 🟢 **Third instance of this mechanism in this KB** (after `ai-learning-os`/PyMuPDF and `text2text`), reached by a third independent route. 🔵 Use `WordDetector` + `CTCDecoder` instead: same author, same pipeline, permissive all the way down. |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🔴 **BSD-3-Clause** (1,531 B ✅ first-hand; sidebar agrees) — **CORRECTION** | 114 | Global † | ✅ permissive | "An open-source project designed to provide an educational and collaborative AI-powered platform." 195 forks. 🔴 **This base's own rotation history recorded this project as `Apache2` (`education_cycle3`). It is not: the grant is BSD-3-Clause** — "All rights reserved" plus the three numbered conditions including non-endorsement — and **two independent reads agree** (grant body + GitHub sidebar). 🔵 **Why the correction has commercial weight rather than being pedantry: BSD-3-Clause carries no express patent grant, Apache-2.0 does.** For a studio taking procurement questions from a university, that is the difference between two answers. Holder is an individual ("Mohamed El hajji On behalf of all R2D-dev"), so region stays `Global †` under `569-E`'s grade convention. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** (35,136 B ✅ first-hand, title reads "GNU AFFERO GENERAL PUBLIC LICENSE") | 8,200 | North America | ⚠️ **network copyleft** | "The Open edX LMS & Studio, powering education sites around the world!" 4,400 forks. 🔴 **Shelved here to close a linking defect, not because the platform is new to this KB: it is named `15×` across shelf prose and this is the first time its address appears on any shelf page.** The harness's own bar is that every row carry a real repo URL; a project named in prose without one cannot be checked, cloned or licence-probed by anyone downstream. 🔴 AGPL-3.0 §13 means a hosted deployment must offer source to its users — the reason this KB routes integrations through LTI/XBlock rather than forks. |
| [patil-suraj/question_generation](https://github.com/patil-suraj/question_generation) | **MIT** (1,068 B ✅ re-read, *"Copyright (c) 2020 Suraj Patil"*) | 1,100 | Global | ✅ permissive | The axis's **reference implementation** — answer-aware and multitask QA-QG as a HuggingFace `pipeline`. The most-starred permissive generator; recorded *"unplaced"* at pass 85. |
| [ramsrigouthamg/Questgen.ai](https://github.com/ramsrigouthamg/Questgen.ai) | **MIT** (1,077 B ✅ re-read, *"Copyright (c) 2020 Ramsri Goutham Golla"*) | 952 | ⚠️ see note | ✅ permissive | 🟢 **Ships item *types*, not one task**: MCQ with distractors, boolean (yes/no), FAQ, paraphrase, answer prediction. T5 + sense2vec. Closest to what an assessment unit orders. |
| [asahi417/lm-question-generation](https://github.com/asahi417/lm-question-generation) | **MIT** (1,065 B ✅ re-read, *"Copyright (c) 2024 asahi417"*) | 366 | Global | ✅ permissive | 🟢 **The multilingual row.** `pip install lmqg`; question **and answer** generation in **9 languages** (`en/fr/ja/ko/ru/it/es/de/zh`), HuggingFace checkpoints, **ACL 2023** system-demonstration paper, 385 commits. ⚠️ **No Portuguese.** |
| [artitw/text2text](https://github.com/artitw/text2text) | 🟡 **MIT + rider** (`master/LICENSE.txt`, **1,325 B**, CRLF, *"Copyright (c) artitw"* — no year) | 305 | Global | ⚠️ **read the rider** | Multilingual text-to-text toolkit (tokenisation, embeddings, BM25/TF-IDF search, translation, language id). 🔴 **`Gap 353`/`P922`'s dependency-closure rider, read verbatim this pass** — three lines appended after the MIT warranty clause: *"This open source software utilizes other open source components with their own licensing agreements. As the consumer of this software, you agree to abide by the licensing requirements set forth by the respective components used."* 🔵 **Not a field-of-use restriction and not a copyleft trigger** — it is an acknowledgement that the grant does not cover the dependency tree, which is true of every package but is here made contractual. ⚠️ It means **the dependency closure must be cleared separately**; the row is usable, the diligence is not optional. 🟢 The rest of this pattern does not need it — skip the row if that clearance is not budgeted. |
| [AMontgomerie/question_generator](https://github.com/AMontgomerie/question_generator) | **MIT** (1,073 B ✅ re-read, *"Copyright (c) 2020 Adam Montgomerie"*) | 298 | Global | ✅ permissive | Long-form prose → QA pairs, with an answer-aware evaluator that **ranks** generated questions. Over-generate then rank. |
| [KristiyanVachev/Leaf-Question-Generation](https://github.com/KristiyanVachev/Leaf-Question-Generation) | **MIT** (1,073 B ✅ re-read, *"Copyright (c) 2018 Kristiyan Vachev"*) | 139 | Global | ✅ permissive | 🟢 **Distractor generation** — MCQs *with wrong-answer options*. The step a general LLM does worst, and exactly what `itembank lint` rejects on. |
| [PragatiVerma18/MLH-Quizzet](https://github.com/PragatiVerma18/MLH-Quizzet) | **MIT** (1,069 B) | 97 | Global | ✅ permissive | 🟢 **Takes teacher PDFs** and emits a quiz — the only row whose input is the artefact a teacher already has. |

⚠️ **One unresolved region conflict, recorded rather than silently picked.** Pass
85 placed `Questgen.ai` as **APAC**. Its licence file names
**"Ramsri Goutham Golla"** — an **individual** — and this base's `p570` instrument
places a repository **only when the holder is an institution**. 🔵 The two rules
disagree: the `p570` instrument says `Global`, pass 85's placement says `APAC`,
and the repository page states no location. **Left as a flagged conflict for a
later pass to resolve at source; do not quote the region to a client.**

🔴 **The licence trap on this axis, already paid for once by this base.**
[`KristiyanVachev/Question-Generation`](https://github.com/KristiyanVachev/Question-Generation)
is **GPL-3.0** (35,149 B) at **495★** — the **same author** as the MIT `Leaf` row
above, with **3.5× the stars**. A star-sorted sweep returns the copyleft sibling
first. Pass 85 recorded this under `P171` alongside three more GPL-3.0 rows of
**identical 35,148 B payload**, and warned that a `grep -i Affero` classifier
calls 4 of 4 of them AGPL and is **wrong 4 of 4 times**.

### 🔴 `topic:essay-scoring` is a tag-variant decoy — and that is the one genuinely new finding on this page

| tag | population | ★ ceiling | permissive grants | status |
| --- | --: | --: | --: | --- |
| 🟢 `topics/automated-essay-scoring` | **35** | — | 🟢 **8** (incl. `doheejin/ProTACT`, **BSD-3-Clause**) | **swept at pass 84, 100% precision** |
| 🔴 `topic:essay-scoring` 🆕 | 🔴 **17** | 🔴 **34** | 🔴 **0 shelvable** | 🆕 swept `p571` |

🔵 **The same capability splits across two tags, and the shorter variant is the
near-empty one.** Had `p571` swept only `topic:essay-scoring`, it would have
concluded *"no permissive AES exists"* — **contradicting this base's own pass-84
record of eight permissive grants.** 🟢 **The rule: when a capability has a
hyphenated long-form tag and a short-form tag, sweep the LONG form.** The short
form collects the abandoned and the unlicensed.

🟡 **What the 17 add that pass 84 did not already hold: nothing shelvable, and one
regional corroboration.** Three are Brazilian/Portuguese-language ENEM-adjacent
(`IC-Redacoes-UTFPR/CorrecaoRedacao` — already on this base — plus
`renan-aalmeida/AES_Enem_Competencia5` and `DaviSantos-23/Reda-o`, **both
re-probed this pass, both with no licence grant**) and three are Korean. 🔵 That
reproduces this base's standing LATAM finding — *the Portuguese essay-scoring tier
is **ungranted**, not absent* (`Gap 235`) — on a second, independent tag.

## Eighth pass (`p570`, 2026-10-31) — two structural results, and one of them is a warning about this base's newest rule

🟢 **`derived foundations rows: **9**` added this pass** — seven in a new layer
below, two in placements.

🟢 **Result 1: the evaluation layer was never missing. Its vocabulary was.**
Six consecutive passes closed with *"no education-specific agent observability or
regression tooling was found"*, searching `evaluation`, `benchmark` and
`observability` under `topic:education`. 🔴 **The axis those assets actually live
on is [`topic:rubric`](https://github.com/search?q=topic%3Arubric), which answers
`187` results and which 569 passes never queried** — `topic:rubric` appeared
**zero** times in every live page of this base. 🟢 **Seven of its top ten are new
addresses**, all granted, and they are shelved in the new layer below. 🔵 **The
generalisable lesson, and it will repeat in every other industry base on this
harness: a six-pass absence can be a property of the search vocabulary rather
than of the field. This base measured the star floor at `p569` and the topic
vocabulary at `p570`, and both times the absence dissolved.**

🔴 **Result 2: the admission rule this base adopted ONE PASS AGO is gameable, and
the first never-swept axis produced the counterexample.** `p569` moved the
tooling layer from a star gate to a **commit-count** gate, because a star floor
was discarding this base's best rows. 🔴 **`CurveAhoead/ScoreRune` reads 35★ and
`2,137` commits dated from `2014-06-10` — and the history is synthetic.** A star
gate needs other people; **a commit gate needs a loop**, so commit count is
*cheaper* to forge than the signal it replaced. 🟢 An instrument now exists,
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass and validated against two real controls. See `570-A`
and the layer note below.

## Platforms of record

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8,200 | North America | ⛔ copyleft | The Open edX LMS & Studio. Python + JavaScript. The reference MOOC-scale platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | ⛔ copyleft | The world's most-deployed LMS. Note the region: Moodle HQ is in Perth, **Australia** — commonly misfiled as EMEA because of its European install base. |
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 7,000 | Global | ✅ permissive | Free online learning platform built around structured, explorable lessons. Python, Angular, Google App Engine. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | North America | ⛔ copyleft | "The open LMS by Instructure, Inc." Dominant in North American higher ed, and the platform the strongest verified agent ecosystem attaches to (see [`../agents/top.md`](../agents/top.md)). |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0 + separate Enterprise Licence** | 2,400 | Global | ⛔ copyleft **and** dual-licensed | "The Next-gen Open Source learning platform for everyone." Next.js/FastAPI/Postgres/Redis, 593 forks, includes "LearnHouse AI: The Teachers and Students copilot". **Added this pass, as a correction:** the African-education search returned a **0★ fork** of this repo under an African organisation name; the real project is this one, maintained by Badr B. (`@swve`), country not stated. The licence shape is the thing to carry forward — AGPL core with features held back under a commercial licence means the open repo is not the whole product. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | ECL-2.0 | 1,200 | North America | ✅ permissive | Platform for learning, teaching, research and collaboration. ECL-2.0 is an Apache-2.0 derivative written for academic consortia — permissive, with a patent clause tuned for universities. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | Global | ✅ permissive | "The offline app for universal education." The reference choice for low- or no-connectivity deployments. Python + JavaScript. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1,100 | EMEA | ⛔ copyleft | The Docker-based Open edX distribution. In practice this, not raw `openedx-platform`, is how Open edX actually gets deployed. France. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | ⛔ copyleft | LMS focused on ease of use and accessibility. Strong francophone and LATAM install base. |
| [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | 102 | **EMEA** | ✅ permissive | **The licence exception that changes the EMEA answer.** "Open-source AI-native LMS with AI Mentor & role-play. Self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX." TypeScript, 31 forks, created 2024-08-01, pushed 2026-10-30. Ships **SCORM and xAPI** and is explicitly white-label. Maintained by **Selleo**, a software company whose GitHub profile states its location as **Poland**. MIT confirmed via the API (`license.spdx_id: MIT`). At 102★ it is not a platform of record — but it is the only AI-native LMS found that a client can fork, rebrand and keep closed. |

### Permissive platforms one tier down — new in the fourth pass

Not platforms of record. These are **actively maintained, permissively licensed
education platforms at the small-and-medium-institution tier**, which is where
the "no permissive substrate exists" finding stops being true.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [safytech/ulearn](https://github.com/safytech/ulearn) | **MIT** (file, 1,066 B) | 701 | Global | ⚠️ permissive, **stale stack** | "ULEARN — Open Source (FREE) LMS script." 299 forks. **The largest MIT-licensed LMS located anywhere.** Laravel **5.8** + React **16.9** — both long past end of life, so a fork is a framework-upgrade project before it is a product. Quote an upgrade estimate or do not quote it. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | **MIT** (file, 1,094 B, "Thomas Debay and project contributors") | 410 | Global | ✅ permissive | "Laravel & Filament-based school management platform for small and medium institutions." 151 forks, pushed 2026-10-30, topic **`student-information-system`**. **The permissive education SIS this KB spent three passes concluding did not exist.** The 410★/151-fork ratio is the signature of a system in real deployment. Current stack, unlike `ulearn`. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** (file, 1,079 B, **"Copyright (c) 2018-present GIP FUN MOOC"**) | 318 | **EMEA** | ✅ permissive | A Django **CMS for building education portals**, designed to front Open edX and Moodle catalogues. 94 forks. **Region placed from the licence file itself:** GIP FUN MOOC is France Université Numérique — the same publisher as `openfun/ralph` below. Two MIT components, one French public publisher. |
| [iblai/lms](https://github.com/iblai/lms) | **MIT** (file, 1,063 B, "ibl.ai") | 208 | Global | ✅ permissive | "Skills intelligence platform — discover courses, track competencies, earn credentials, and accelerate workforce development." Next.js 15 / React 19, created 2026-03-04. **The first open-source asset located for the digital-credentials and skills-pathways trend**, which had been single-source commentary for three passes. |
| [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** (file, 11,362 B) | 54 | APAC | ✅ permissive, very young | Self-hosted **multi-tenant** LMS — course builder, trainer and student portals, progress tracking. Django + React + Flutter, created **2026-10-07**. Explicit `moodle-alternative` and `corporate-training`. Region inferred from the publisher, **not stated on the repo**. |
| [Azure/Moodle](https://github.com/Azure/Moodle) | **MIT** (file, 1,090 B, "Microsoft Corporation") | 185 | Global | ✅ permissive tooling | Not a platform: **MIT deployment tooling for scalable Moodle clusters on Azure**. 187 forks on 185★, i.e. consumed as a template. Worth citing to a client as the attach-don't-fork doctrine practised by Microsoft against a GPL-3.0 platform. |

**The population, with a denominator — because scarcity claims need one.**
`topic:learning-management-system license:apache-2.0 stars:>50` returns **2
repositories in the world**: `TutorLoom` (54★, three weeks old) and
`AcademicsToday/academicstoday-django` (Apache-2.0 confirmed from `LICENSE.md`,
11,358 B, 220★, **created 2015**, effectively stale).
`topic:lms license:mit stars:>80` returns **15**, and the topic is polluted —
it includes `SWE-agent` (20,693★, a coding agent), `tompazourek/Colourful` (298★,
a .NET **colour-space** library, "LMS" as in cone response) and `freeitsm` (118★,
ITSM). **Six of those fifteen are education platforms.** So the whole permissive
LMS population above 50★ is roughly **eight repositories**, the largest is 701★
on an end-of-life stack, and Moodle alone carries 7,600★ under GPL-3.0.

⚠️ **One archived trap.** [`microsoftarchive/Learn-LTI`](https://github.com/microsoftarchive/Learn-LTI)
— MIT, 132★, 52 forks, an LTI tool surfacing the Microsoft Learn catalogue inside
an LMS — is **archived**. It looks exactly like the component an engagement would
reach for, it is permissive, and it is dead. The `microsoftarchive` org name is
the only warning on the URL.

## Interoperability and analytics layer

Where the permissive licences live, and the layer an AI integration actually
touches.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | North America | ✅ permissive | The xAPI specification: how systems communicate learner activity. The vocabulary any learning-analytics or agent-telemetry design should speak. ADL Initiative (US). |
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 | 373 | Global | ✅ permissive | Turns an application into a full **LTI 1.3** tool provider: launches, Deep Linking, Assignment & Grade Services, Names and Role Provisioning, Dynamic Registration. **Still the single most important repo on this page for a Globant engagement** — the sanctioned, licence-clean way to attach new software to a copyleft LMS without touching its code. Brazilian maintainer. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 153 | EMEA | ⛔ copyleft | The H5P interactive-content runtime. **Licence correction carried forward:** earlier passes recorded H5P as MIT. It is **GPL-3.0**. Norway. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | **MIT** (file, 1,072 B, "Jonathan Putney") | 362 | Global | ✅ permissive | "A modern SCORM JavaScript runtime library" — **SCORM 1.2, SCORM 2004 and cross-frame**, tagged `offline-first`. 85 forks, pushed 2026-10-30. **New in the fourth pass, and it closes a hole this KB never named:** three passes built the attach doctrine on LTI, MCP and xAPI and omitted **the standard the installed base actually ingests**. xAPI is the better specification; SCORM is the incumbent, it is what corporate L&D procurement asks for by name, and it is what `Selleo/mentingo` ships alongside xAPI. A permissive, maintained SCORM runtime means Globant-built courseware can be delivered into a client's existing LMS **without touching the LMS and without an xAPI migration project first.** |
| [openfun/ralph](https://github.com/openfun/ralph) | MIT | 51 | EMEA | ✅ permissive | Learning Record Store for learning analytics; consumes xAPI statements. The permissive LRS option. France Université Numérique — same publisher as `richie` above. |
| [openfun/warren](https://github.com/openfun/warren) | **MIT** | 17 | EMEA | ✅ permissive | **xAPI learning-analytics dashboards — the layer this page spent five passes recording as absent.** Same operator as `ralph` and `potsie`; pushed `2026-10-11`. **Added in the sixth pass**, and not because it was found: it was already recorded in [`trending.md`](trending.md) while the fifth-pass summary on that same page was still publishing *"no open-source learning-analytics dashboard"*. France Université Numérique. |
| [openfun/potsie](https://github.com/openfun/potsie) | **MIT** (`main/LICENSE.md`, 1,094 B) | 11 | EMEA | ✅ permissive | **Grafana dashboard suite for learning analytics**, written in Jsonnet — so the dashboards are generated, reviewable and diffable rather than clicked together in a UI, which is what makes them deliverable as code. Last pushed `2024-12-18`: stable rather than active. Grant read byte-for-byte in the sixth pass, *"Copyright (c) 2021-present **France Université Numérique**"*. |

## Content, standards and evaluation layer (new this pass)

The layer that answers *"is what the agent produced actually any good, and does
it match the curriculum?"* — and the layer where licences stop being binary.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | ⚠️ **split: code MIT, datasets "By data publisher"** | 164 | Global | ⚠️ conditional | "The data layer for smarter educational AI" — enriched datasets linking academic standards, curricula, learning progressions and instructional guidance under one schema, reachable via browser explorer, agent plugins, local files, a REST API **and an MCP server**. Run by Learning Commons (`learningcommons.org`), country not stated. **Licence mechanics matter here:** the API reports `NOASSERTION` because the file is `LICENSE.md` and because the grant is split — README badges read "License for Knowledge Graph code: MIT" and "License for Knowledge Graph datasets: By data publisher", and **some datasets are gated**. The code is safe; each dataset must be cleared individually. |
| [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | ⚠️ **three-tier split: code MIT · prompts CC BY 4.0 · two corpora CC BY-NC-SA 4.0** | 87 | Global | ⚠️ **conditional — the corpora are non-commercial** | "Evaluation for AI outputs against trusted educational rubrics" — research-backed rubrics for scoring generated instructional content. TypeScript, 17 forks, pushed 2026-10-31. ~~**The only rubric-scoring asset located in this KB**~~ — 🔴 **struck `2026-10-31` (`p570`): the `topic:rubric` sweep returned seven further granted rubric-scoring assets, four of them Apache-2.0. The claim was true of this base's search vocabulary, not of the field. See the rubric layer below.** Still the natural quality gate in front of any content-generating agent, and still the only one carrying a peer-reviewed education corpus. **Licence RESOLVED in the fourth pass** by reading `main/LICENSE.md` (1,615 B), after three passes carried it as unresolved. It grants: *evaluator **code** → MIT*; *evaluator **content**, i.e. the prompts and settings → CC BY 4.0*; ***Annotated CLEAR Corpus** → CC BY-NC-SA 4.0*; ***Annotated PERSUADE 2.0 Corpus** → CC BY-NC-SA 4.0*. **The code and the rubric prompts are commercially usable with attribution; the two annotated corpora are NC and cannot ship in a billable deliverable or a commercial regression suite.** The upstream originals (CommonLit's CLEAR Corpus, PERSUADE 2.0) are themselves CC BY-NC-SA 4.0, so there is no cleaner version upstream to substitute — an engagement must bring its own corpus. Note the direction: this is the **inverse** of its sibling `knowledge-graph` (code MIT / data by publisher). |
| [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | **Apache-2.0** (file, 11,323 B — see note) | 21 | Global | ✅ permissive | **Efficacy measurement, and the only asset in five passes that narrows the evaluation gap.** *"Tool for Education Research with RAndomized COnTrolled TriAls"* — an **LTI plug-in to the LMS** that differentiates the contents of online assignments into experimental treatment variations and assigns students randomly between them. It also carries the ethics apparatus that makes that legal in a school: **informed consent hidden from the teacher**, non-consenting participants filtered out of result summaries and exports, and student identifiers stripped from exports. Java, 9 forks, branch **`development`**, created 2021-05-10, pushed 2026-10-29. **Be precise about what it is:** this measures *"did this intervention change outcomes"* under randomisation — it is **not** runtime monitoring and will not tell you a deployed tutor has drifted. ⚠️ Its `LICENSE` is unmodified Apache boilerplate with the template placeholders intact (`Copyright {yyyy} {name of copyright owner}`), so the grant **names no licensor**; the `NOTICE` credits Oxford University for LTI cookie-handling code. Origin not establishable from this session, recorded Global. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | ✅ permissive | 1,143 questions from real teacher-qualification exams — CDPK (920, general pedagogy) and SEND (223, special needs). Measures whether a model knows how to *teach*, not whether it knows the subject. |

## Rubric and evaluation layer (new in the eighth pass — the axis 569 passes never swept)

The layer that answers *"did the agent's output meet the standard, and can I
prove it again next Tuesday?"* — the **regression** half of the evaluation gap
this base has published as open for six consecutive passes.

🟢 **Why it was missing.** Every prior sweep looked for `evaluation`, `benchmark`
or `observability` **under `topic:education`** and returned nothing. The assets
are tagged by **capability**, on
[`topic:rubric`](https://github.com/search?q=topic%3Arubric) — **187 results**,
and a string that appeared **zero times** in every live page of this base before
this pass. 🔴 **The gap was a vocabulary artefact, exactly as the star floor was
a sort artefact at `p569`.**

🔵 **What this layer is and is not.** None of these is an education-specific
*drift detector*; the honest gap statement below is narrower than it was, not
closed. What they are is **scoring machinery you can pin, version and re-run** —
which is the missing half of pattern `P-568-K`, whose regression suite has had to
be hand-rolled because `learning-commons-org/evaluators` cannot ship its corpora
commercially.

| Repo | Licence | ★ | Commits | Region | Build-on? | What it is |
| --- | --- | --: | --: | --- | --- | --- |
| 🆕 [alphadl/AdaRubrics](https://github.com/alphadl/AdaRubrics) | **Apache-2.0** (`main/LICENSE`, 10,761 B — ⚠️ **no copyright line**, see note) | 368 | 50 | Global | ✅ permissive | 🟢 **The pick of this layer, and the first asset in this base that evaluates an *agent trajectory* rather than a finished artefact.** Adaptive dynamic rubric evaluation: the rubric is generated and adapted per task instead of being fixed in advance, which is what makes it applicable to a tutoring *session* — a multi-turn interaction whose quality is not visible in any single response. Python, pushed `2026-08-24`, 50 commits from `2026-02-22`, 2 authors. 🔵 **Why it matters for an engagement:** every tutor in this KB is a multi-turn agent, and until this row the only evaluation assets here scored **single generated documents**. ⚠️ Pre-adoption: 368★ is real traction for a research artefact and is not an install base. |
| 🆕 [Sion612/rubrictrail](https://github.com/Sion612/rubrictrail) | **Apache-2.0** (`main/LICENSE`, 11,324 B — ⚠️ no copyright line) | 130 | 45 | Global | ✅ permissive | Local-first assignment planner that keeps **evidence links** from a rubric criterion back to the work that satisfies it. TypeScript, `v0.2.0`, 45 commits `2026-08-12`→`2026-08-31`, single author. 🔵 **The audit-trail shape**, and the only row here that models the *criterion → evidence* link explicitly — which is what an accreditation review or an AI Act Annex III evaluation file actually has to produce. 🔴 **Dormant two months**; read it as a design reference, not a dependency. |
| 🆕 [AI9Stars/LLM-Rubrics-Survey](https://github.com/AI9Stars/LLM-Rubrics-Survey) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 methanechen") | 71 | 17 | Global | ✅ permissive | Survey and bibliography of rubric use across the LLM lifecycle — rubrics as evaluation criteria, as training signal and as reward. **Not a runtime**: shelved because it is the literature map for this layer, and because it is the cheapest way to brief a client's academic stakeholder that rubric-based evaluation is a methodology with a corpus behind it rather than a consultant's invention. |
| 🆕 [OpenEnvision/AutoRubric-as-Reward](https://github.com/OpenEnvision/AutoRubric-as-Reward) | **Apache-2.0** (`main/LICENSE`, 10,757 B — ⚠️ no copyright line) | 58 | 27 | Global | ✅ permissive | Auto-generated rubrics used as the **reward signal** for training — turning implicit preference data into explicit, inspectable criteria. Python, 3 authors, `2026-05-06`→`2026-09-25`. 🔵 **Relevant where a client wants a tutor tuned to its own pedagogy** rather than to generic helpfulness: the rubric becomes the spec, and the spec is readable by the teaching lead instead of buried in a preference dataset. |
| 🆕 [AndrewNgGirl/SkillLens](https://github.com/AndrewNgGirl/SkillLens) | **MIT** (`main/LICENSE`, 1,079 B, "Copyright (c) 2026 SkillLens contributors") | 44 | 12 | Global | ✅ permissive | Self-hosted web tool for **scoring and reviewing agent skills**. 🟢 **Directly relevant to this KB's central structural finding** — that *15 of the 25 agents* on [`../agents/top.md`](../agents/top.md) have no runtime and ship as markdown skill bundles. If the deliverable is a prompt contract, the quality gate must score prompt contracts, and this is the only asset found that does. 🔴 **12 commits over 12 days in May 2026 and nothing since**: the idea is the asset here, not the code. |
| 🆕 [hanskepper/SMART-GRADE](https://github.com/hanskepper/SMART-GRADE) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 HANS KEPPER") | 3 | **200** | **EMEA†** | ✅ permissive | 🟢 **The first African-origin education asset in this base with a verified permissive grant**, and a row a star gate discards outright: **3★ against 200 commits** (`2026-07-08`→`2026-10-09`). Progressive web app tracking grades across subjects, terms and *sequences* — **`séquence` is the Cameroonian/francophone-African school reporting period**, not a generic term, and the schema is built around it rather than around semesters. 🔵 **Why this row is worth more than its stars:** three passes hunted African supply and found an **org-name trap** (`AFRICAN-AI-NETWORK/learnhouse`, a 0★ fork) and an **ungranted** hackathon entry (`tujifunze-agent`). This is neither — it is a small, granted, commit-dense artefact built against a real national school calendar. ⚠️ **It is a gradebook, not AI**: the value is the curriculum-calendar schema to build on, and the provenance. 🔴 **`EMEA†` is a schema artefact, not a geography claim — see the region note below.** |
| 🔴 [CurveAhoead/ScoreRune](https://github.com/CurveAhoead/ScoreRune) | **Apache-2.0** (`main/LICENSE`, 11,358 B — ⚠️ no copyright line) | 35 | ⛔ **2,137 — SYNTHETIC, see `570-A`** | Global | ⚠️ **code yes, history no** | 🔴 **Carried as a warning, and it is the most important row on this page.** A **deterministic** rubric engine for reviewing AI responses, Python + C# runtimes — on substance an excellent fit for this layer, because *deterministic* is precisely what a regression gate needs and what `itembank` independently chose for scoring. 🔴 **But its git history is fabricated.** `2,137` commits dated `2014-06-10`→`2026-09-06`, and all four plausibility checks fire: commits per year run `117,141,150,155,161,165,170,175,181,185,185,198` — **monotonic, 1.69× max:min across 12 years**, where the real control `philchalmers/mirt` runs `1,111,349,658,411,…,91` at **658×**; **408 of 408 pre-2017 commits carry Conventional Commits prefixes**, a convention that postdates them; **author date equals committer date on all 2,137 commits** (real control: 19 divergent); and **the repository's first commit is `refactor: evidence kinds`** — a repository cannot begin by refactoring. 🟢 **The ~154 commits dated 2026 look genuine and the code appears real**: use the code on its merits, cite **35★ / 2 authors / three months** as its provenance, and **never quote the 2,137**. Evidence: [`../evidence/history-plausibility.2026-10-31-p570.tsv`](../evidence/history-plausibility.2026-10-31-p570.tsv). |

🔴 **Rejected from this layer:**
[`tc-imba/canvas-auto-rubric`](https://github.com/tc-imba/canvas-auto-rubric)
(33★) — **no grant** at 5 filenames × 3 branches, **and** last pushed
`2022-12-27`. Doubly disqualified; logged so no successor re-triages it.

### 🔴 The region note this layer forces, and it is a schema finding

🔴 **Region is structurally unrecoverable from an Apache-2.0 grant, and this base's
placement rule does not say so.** The standing rule (`p568`) is *"the licence
file's copyright line places a repository when the holder is an institution"*.
🔴 **Apache-2.0's template has no copyright line to fill** — its only occurrence
of the word is the boilerplate definition *"'Licensor' shall mean the copyright
owner…"*. **Four of four** Apache rows above were probed and **none carries a
holder**. 🔵 So the rule is **licence-family-dependent**: recoverable for MIT and
BSD, where the holder line is part of the text an author must edit; **never**
recoverable from Apache-2.0, regardless of whether the holder is an institution.
This is why five of seven new rows here are `Global`. Registered as `570-C`.

🔴 **And `EMEA†` on `SMART-GRADE` is the closed vocabulary failing visibly.**
The artefact is **Cameroonian**. The permitted values are
`North America | EMEA | APAC | LATAM | Global`, so Sub-Saharan Africa resolves to
**EMEA** — the same bucket as Germany and the Netherlands. 🔵 **The consequence is
not cosmetic: this base publishes EMEA counts that are read as market
measurements, and they silently conflate Western European public-sector
procurement with African school IT.** The `†` marks artefact-grade evidence per
`569-E`; the Africa conflation is registered separately as `570-E`. **The country
is in the prose because the field cannot hold it.**

## Content-production layer (new in the fourth pass)

Not education projects. Horizontal tools that the industry's highest-volume
artefact — lecture decks, courseware, interactive texts — is actually built from.
**This layer was invisible to four passes of sweeping because every sweep filtered
on an education topic and none of these carries one.**

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | **MIT** (file, 1,069 B, on both `main` and `master`) | **71,498** | Global | ✅ permissive | **The largest permissively licensed repository anywhere in this knowledge base** — 1.4× DeepTutor, 1.7× OpenMAIC. "AI turns documents or topics into real, native PowerPoint decks — with native shapes, transitions and animations, data-backed charts and tables on demand, audio narration from speaker notes, and support for your own `.pptx` templates." Python, **5,578 forks**, created 2025-12-10, pushed 2026-10-30. **Why it belongs here:** `.pptx` is the format schools and universities actually exchange; *"support for your own `.pptx` templates"* is institutional branding compliance, which is what normally kills generated-content pilots; and audio narration from speaker notes is a lecture-capture path for free. Deliberately **not** on the agent shelf — it is not an education agent. ⚠️ **Provenance unverified:** 71,498★ and the owner profile cannot be read from this session, so **no region is assigned**. For a component this central, check it independently before client-facing use. |
| [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (file, 1,069 B) | 1,034 | Global | ✅ permissive | "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created **2026-10-03** — 1,034★ in four weeks. Topics include **`scorm`** and `interactive-textbook`, so pair it with `scorm-again` to deliver into an existing LMS. Also shelved as an agent in [`../agents/top.md`](../agents/top.md). ⚠️ Copyright line is a pseudonym. |
| [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** (file, 1,069 B, "Assaf Kipnis") | 557 | Global | ✅ permissive | Topic in, **course of 2-minute audio lessons with cited sources** out; web research plus ElevenLabs TTS. Python, 67 forks, created 2026-10-14. The only content generator in this KB that **starts** from citation provenance rather than retrofitting it. |

**How to use this layer honestly.** These produce *artefacts*, not *assessed
learning*. Nothing here knows whether the deck it generated is pedagogically
sound or on-syllabus — which is exactly what the evaluation layer above is for,
and why pattern **P-569-B** wires a quality gate between them rather than
shipping generator output directly.

## Document-ingestion layer (new in the fifth pass — the capability sweep)

The fourth pass closed with an instruction to itself: *sweep by capability
(`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`), not by industry
topic.* **This is what that sweep returned, and it is the largest layer in this
KB by an order of magnitude.** Every education engagement begins with the
client's existing material — textbooks, past papers, lecture PDFs, scanned
worksheets — and **none** of these tools carries an education topic, which is why
five passes of industry-topic sweeping never saw them.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | **Apache-2.0** (file, 11,376 B) | **92,024** | APAC | ✅ permissive | *"Turn any PDF or image document into structured data for your AI."* The highest-starred asset in this entire knowledge base. Strongest **Chinese-language and handwriting** OCR in open source, which is the deciding factor for scanned worksheets and handwritten exam scripts. Pushed 2026-09-16; **11,594 forks**, 259 open issues. Baidu's PaddlePaddle organisation (China). |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | ⚠️ **Apache-2.0 + commercial thresholds** — read the note | **82,860** | APAC | ⚠️ conditional (thresholds are far above any education engagement) | *"Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows."* Strong on **formulas, tables and multi-column academic layout** — i.e. STEM textbooks, the hardest input in education. **6,857 forks**, branch **`master`**, pushed 2026-10-31. **The licence is a shape this KB had not catalogued.** GitHub reports `NOASSERTION`; `master/LICENSE.md` (3,301 B) reads *"MinerU is licensed under Apache License 2.0 and is subject to the additional terms below"*, then adds: **(1)** a separate commercial licence is required above **100 million MAU or USD 20 million monthly revenue**; **(2)** an **attribution obligation** — any online service built on MinerU must state prominently, in the interface or public documentation, that MinerU is used; **(3)** automatic termination of all rights if either is breached. **For Globant the thresholds are irrelevant and clause 2 is not** — it is a deliverable requirement that must reach the client's product team, not just legal. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (file, 11,358 B) | **77,267** | Global | ✅ permissive | The reference OCR engine, LSTM-based, **100+ languages**, **10,879 forks**, pushed 2026-10-28. Runs fully offline on commodity hardware with no model licence and no inference bill — which is why it, and not a hosted vision model, is the realistic answer for ministry and offline-first work (see pattern `P-568-F`). |
| [docling-project/docling](https://github.com/docling-project/docling) | **MIT** (file, 1,072 B) | **69,909** | Global | ✅ permissive | *"Get your documents ready for gen AI."* **The pick of this layer for most education work, and on licence grounds as much as technical ones: MIT, where its larger rivals are Apache-with-terms or Apache.** PDF, DOCX, **PPTX**, XLSX and HTML → clean markdown or JSON with layout and **table structure** preserved. Python, 5,222 forks, pushed 2026-10-31. `main/LICENSE`: *"Copyright The Docling Contributors"* — a collective holder, so **no region is assigned**, though the project is widely associated with IBM Research and is now under the LF AI & Data Foundation; neither is verifiable from this session and neither is asserted here. |
| [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | **Apache-2.0** (file, 11,358 B) | **30,129** | Global | ✅ permissive | *"PDF Parser for AI-ready data. **Automate PDF accessibility.** Open-source."* The differentiator is in its topics: `accessibility`, `a11y`, `pdf-accessibility` and **`eaa`** — the **European Accessibility Act**. Java, **2,881 forks**, pushed 2026-10-30. **This is the only asset in this KB that addresses accessibility compliance as a product feature**, and accessibility conformance is a procurement gate in EMEA public education that nothing else here answers. See pattern `P-570-B`. |
| [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | **Apache-2.0** (file `LICENSE.md`, 11,360 B) | 15,651 | Global | ✅ permissive | Open-source ETL for LLMs: 20+ document types into a uniform structured form, with first-class LangChain integration. The **pipeline** choice rather than the single-document choice — right when a client hands over a repository of mixed legacy material rather than a textbook. 1,377 forks. |

## Narration, speech and retention layer (new in the fifth pass)

The accessibility and language side of the same sweep. Education's two
highest-volume accessibility requirements — **read-aloud** and **captions** — are
served entirely by permissive horizontal tooling.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [supertone-oss-archive/supertonic](https://github.com/supertone-oss-archive/supertonic) | **MIT** (file, 1,070 B, "Supertone Inc.") | 13,757 | APAC | ⚠️ **ARCHIVED — read before shelving** | *"Lightning-Fast, On-Device, Multilingual TTS — running natively via ONNX."* Bindings for Swift, Kotlin/Java, C++, C#, Go, Rust, Node, Python, Flutter and **WebGPU**; 1,566 forks. On-device multilingual TTS with an MIT grant is close to ideal for offline read-aloud. **But the `archived` flag is `true`** — the organisation is literally named `supertone-oss-archive`. The grant is clean and perpetual and the code still runs; **there will be no fixes, no security patches and no new languages.** Fork it deliberately or not at all. *The only reason this row is honest is that the `archived` field was checked — stars and licence both look excellent.* |
| [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | **MIT** (file, 1,070 B) | 8,165 | Global | ✅ permissive | TTS, STT and speech-to-speech on **Apple Silicon** via MLX. The practical choice when the client's constraint is "it must run on the teacher's MacBook", which in private-school and university faculty estates is common. Pushed 2026-10-31. |
| [denizsafak/abogen](https://github.com/denizsafak/abogen) | **MIT** (file, 1,069 B) | 6,179 | Global | ✅ permissive | *"Generate audiobooks from **EPUBs, PDFs** and text with **synchronized captions**."* Kokoro-82M under the hood. **Synchronised captions are the whole point**: a caption track is simultaneously an accessibility deliverable, a search index and a transcript, and this produces all three from the material a client already owns. The shortest path from "here is our textbook" to an accessible audio course. |
| [collabora/WhisperLive](https://github.com/collabora/WhisperLive) | **MIT** (file, 1,085 B, "Vineet Suryan, **Collabora Ltd.**") | 4,339 | **EMEA** | ✅ permissive | Near-real-time Whisper: live transcription and captioning of lectures, with TensorRT and OpenVINO backends. **Region placed from the licence file's own copyright line** — Collabora Ltd. is a UK company. Live captioning is an accessibility obligation in most EMEA higher-education estates. |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | **MIT** (file, 1,071 B) | 4,637 | Global | ✅ permissive | *"The python library for real-time communication."* The plumbing a **spoken** tutor needs — WebRTC audio in and out with STT/TTS hooks — rather than another model. The missing piece between a text tutor and a conversational one. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (file, 1,079 B) | 4,119 | Global | ✅ permissive | The **Free Spaced Repetition Scheduler** — a modern, ML-fitted replacement for SM-2, used as Anki's scheduler. **The retention layer's algorithm, permissively licensed**, where `anki-mcp-server` on the agent shelf only gives an agent control of the Anki *application*. 165 forks, 8 open issues. Build FSRS in; do not invent a review schedule. |

## Assessment and item-bank layer (new in the sixth pass)

The layer that decides whether a generated question may be put in front of a
student. **Five passes looked for an item *generator* and recorded a gap; the
sixth found the *gate* instead**, which is the artefact an exam board actually
buys and the one the EU AI Act's Annex III evaluation category needs evidence of.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [onionviolet/itembank](https://github.com/onionviolet/itembank) | **MIT** (`main/LICENSE`, 1,068 B, "Copyright (c) 2026 onionviolet") | 3 | Global | ✅ permissive | **The pick of this layer, and it would have been discarded by a star gate: 3★ against 1,175 commits on `main`.** "Author, validate and render exam-style question banks in markdown. A machine-checkable contract for LLM-authored questions." Local-first — nothing leaves the machine but an optional update check. `itembank lint` **blocks on error** per item number (each distractor must explain when it *would* be correct; answer-position skew; select-count against keyed-count; duplicate stems) and `itembank guard` **fails CI** if real banks are committed. **Scoring is deterministic with no model in the path**: short-answer items are *never* auto-graded and stay pending for rubric marking, `fill` is all-or-nothing, `check` runs learner code against hidden cases, and the README states model output is never accepted as a score. Retention is **FSRS** — the same scheduler as `fsrs4anki` below. Exports **Anki TSV, GIFT, answer-key TSV**; key-free JSON session protocol (`start`/`next`/`submit`/`report`/`teach`) built for agents. ⚠️ **Read the limits:** QTI/CASE/SCORM interchange is explicitly backburner — the README says it *"waits for a named consumer"* — the MCP surface is labelled "Phase 999.3" and unshipped, and the wider "course workspace" is not yet runnable. Python-dominant with a Rust `src-tauri/` shell. Holder is a handle; recorded Global. |
| [sudazc/open-question-bank](https://github.com/sudazc/open-question-bank) | ⚠️ **split: code + docs MIT, bank content NOT granted** (1,063 B, "Copyright (c) 2026 sudazc") | 0 | Global | ⚠️ conditional | Schema, validation and rule-based test assembly (`组卷`), TypeScript, 108 commits. **Shelved for its licence shape rather than its traction**, which is near zero. The README is explicit that MIT covers **the framework code and its documentation only**: permission to use, modify or redistribute **a bank's content** is set by that bank's own `bank.yaml` and source-licence fields, and the framework grant conveys none of it. ⚠️ **The default licence for a new bank is a placeholder reading `"TBD - not for publication"`** — so a bank authored with this tool is unpublishable until someone sets it. README states online practice and learning records are not yet implemented. Chinese-language; the grant names a handle, so **not placed** — this page does not place an artefact on its language. |
| [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | **Apache-2.0** (11,346 B) | 203 | APAC | ✅ permissive | Model zoo of **cognitive diagnosis** models — IRT, MIRT, DINA, NCDM and others — from a named university group (USTC). **Be precise about what it does and does not do:** cognitive diagnosis infers *what a learner knows* from responses; it does **not calibrate items**. It is the live, permissive, education-specific half of the psychometrics layer, and the calibration half is the gap (see below). Last pushed 2024-10-25. |
| 🆕 [DaniyalMlk/calibrate](https://github.com/DaniyalMlk/calibrate) | **MIT** (`main/LICENSE`, 1,064 B, "Copyright (c) 2026 Daniyal"); **`package.json` `"license": "MIT"` agrees** | 0 | Global | ✅ permissive | 🟢 **This row closes the calibration gap this layer published for six passes, and a star gate would have discarded it: 0★ against 214 commits** (`2026-09-07` → `2026-10-30`, single author, counted with `git rev-list`). A **dependency-free TypeScript** adaptive-testing engine — `dependencies` and `peerDependencies` are both **absent from the manifest**, verified, so there is **no transitive licence surface at all** (4 devDeps, all permissive). What it implements, from its own README and roadmap: dichotomous **and** polytomous response models (**graded response, partial credit, generalized partial credit**, mixed banks in one bank), ability estimators, **maximum-information item selection**, stopping rules, **item-parameter estimation two ways — joint and marginal maximum likelihood, with JML's structural bias named and demonstrated against MML on the same responses**, **four linking methods** for putting two calibrations of an anchor on one metric, **differential item functioning**, person-**misfit** scanning, and score→ability conversion tables with standard errors. A browser interface draws the posterior, response curves, information curves and bank coverage live. ⚠️ **Read the adoption risk and say it to a client: version `0.1.0`, not yet published to npm** (the README says phases 1–21 are complete *"bar the publish itself"*), **one author, 0 stars, no independent validation.** The code is the evidence; the project is eight weeks old. Holder is an individual, so **Global**. |
| 🆕 [finite-sample/guess](https://github.com/finite-sample/guess) | **MIT** — 🔴 **not from the licence file**: `master/LICENSE` is **52 B** and names no licence (`YEAR: 2015` / `COPYRIGHT HOLDER: Gaurav Sood and Ken Cor`). 🟢 **`master/DESCRIPTION` reads `License: MIT + file LICENSE`** | 3 | **North America** | ✅ permissive | R package, `Imports:` **empty**. *"Adjust estimates of learning for guessing"* — standard guessing corrections plus **latent class models that use informative pre-post test transitions** to separate real learning from guessing on closed-ended items. 🟢 **The measurement counterpart to `calibrate`:** `calibrate` tells you what an item is worth, `guess` tells you whether an observed gain is real. Live (`2026-10-30`) on a 2016 codebase — 19 commits over ten years, so **stable rather than active**; read it as a method implementation, not a maintained platform. 🔵 **Placed `North America` on a channel new to this base:** `DESCRIPTION`'s `Authors@R` carries `mcor@ualberta.ca` — **University of Alberta** — where the copyright line names only two individuals. See `569-D`. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** (1,079 B) | 4,119 | Global | ✅ permissive | **FSRS** as an algorithm rather than an application — the modern spaced-repetition scheduler. Carried forward from the fifth pass's capability sweep and repeated here because it is the retention component both `itembank` and `braiinz-education` independently chose. |

🟢 **What this layer could not do six passes ago, and can now.** Every pass from
the second to the sixth closed this section with the sentence *"there is no
permissive, live, education-specific item **calibration** asset"*. 🔴 **That
sentence is retired as of `2026-10-31` (`p569`), and it was retired by searching
the one place the sort could not reach** — `topic:psychometrics` at `stars:<50`,
where [`DaniyalMlk/calibrate`](https://github.com/DaniyalMlk/calibrate) sits at
**0★ with 214 commits**. 🔵 **The gap was never a supply gap. It was a sort
artefact**, and that is twice in two passes that this base's own shortlisting
method, rather than the field, manufactured an absence (`568-A`, `568-C`).

⚠️ **What is still genuinely missing, stated narrowly so it stays true.** The
layer is now complete *in capability* and thin *in assurance*:

- 🔴 **No calibration asset here has adoption evidence.** `calibrate` is `0.1.0`,
  one author, 0★, unpublished to npm; `itembank` is 3★. **Both are credible on
  their commit histories and neither is credible on its install base.** For a
  high-stakes engagement — the EU AI Act Annex III evaluation category, or any
  exam board — that is a real procurement objection and this page does not paper
  over it. The mitigation is engineering, not more searching: wire `calibrate`'s
  MML output against a known-good reference (the stale-but-MIT
  [`eribean/girth`](https://github.com/eribean/girth), or R's `mirt`) and keep
  the comparison as the evidence the stars cannot supply. Wired as `P-572-A`.
- 🟢 **`569-D` RAN, AND THE R TIER IS NOW PLACED — the largest regional movement
  in this base in several passes.** `569-D` asked a successor to *"re-probe the R
  tier"* on `DESCRIPTION`'s `Authors@R`, after `p569` placed one row that way.
  **Nine rows probed, `7` carry `DESCRIPTION`, `6` place from an institutional
  email domain in the grant's own author field:**

  | Repo | `Authors@R` / `Maintainer` domain | Named entity | Region |
  | --- | --- | --- | --- |
  | [`dexter-psychometrics/dexter`](https://github.com/dexter-psychometrics/dexter) | `jesse.koops@cito.nl` | **Cito**, the Dutch national testing institute (Arnhem, NL) | 🟢 **EMEA** |
  | [`yrosseel/lavaan`](https://github.com/yrosseel/lavaan) | `Yves.Rosseel@UGent.be` | **Ghent University** (BE) | 🟢 **EMEA** |
  | [`cran/TAM`](https://github.com/cran/TAM) | `robitzsch@ipn.uni-kiel.de` | **IPN Leibniz Institute for Science and Mathematics Education**, Kiel (DE) | 🟢 **EMEA** |
  | [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | `cpyles@berkeley.edu` | **UC Berkeley** Division of Computing & Data Science | 🟢 **North America** |
  | [`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) | `sterett.mercer@ubc.ca` | **University of British Columbia** (CA) | 🟢 **North America** |
  | [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | gmail — 🔴 grant places nothing | 🟡 `Title:` reads *"…Brazilian Education Data from **INEP**"*, Brazil's national education-statistics institute; README is Portuguese | 🟡 **LATAM†** |
  | [`philchalmers/mirt`](https://github.com/philchalmers/mirt) | `rphilip.chalmers@gmail.com` | individual | Global |

  🟢 **Three EMEA placements in one probe, and `dexter`'s holder is a national
  public assessment operator** — the same institutional class as France
  Université Numérique, and the strongest EMEA provenance asset this base holds.
  🔴 **Read what this does and does not change:** this base has been publishing
  *"EMEA gained no placed row"* for three consecutive passes, and the rows were
  **already in-tree and already read** — only their region was blank. **The
  supply did not change; the instrument did.** An EMEA engagement can now be
  shown locally-published, permissively granted psychometrics from three
  countries.
  🔵 **`educabR` is `LATAM†`** — artefact-grade per `569-E`, since the grant names
  an individual and only the package's purpose places it.
- 🔴 **But `569-D`'s proposed generalisation does NOT hold, and this pass
  measured the limit.** `569-D` asked for the rule to read *"a named legal entity
  in the grant **OR in a prescribed manifest field** (`DESCRIPTION`'s
  `Authors@R`, `package.json`'s `author`)"*. 🟢 The R half works: **7 of 7**
  CRAN-shaped repositories carry `DESCRIPTION` with an author email, **because
  CRAN mandates the field.** 🔴 **The npm half does not: of 7 new rows probed for
  `package.json`, 5 have none at all and the 2 that do name no author** —
  `rubrictrail`'s only locating field is a `sion612.github.io` homepage, which
  places nothing. 🔵 **So manifest-placement yield is a property of the packaging
  ecosystem's policy, not of manifests**: it works wherever a registry *enforces*
  authorship (CRAN, and by the same logic Debian, CPAN, CRAN-like archives) and
  fails wherever authorship is optional (npm, PyPI without metadata discipline).
  Restate the rule that way or it will be applied to npm and read as an absence.
  Registered as `570-D`.
- 🔴 **The stale permissive libraries are still stale** and are now useful as a
  *baseline* rather than as a dependency:
  [`eribean/girth`](https://github.com/eribean/girth) (127★, MIT, last pushed
  **2022-09-09**), [`inuyasha2012/pypsy`](https://github.com/inuyasha2012/pypsy)
  (242★, MIT, **2018-11-16**).
  [`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) (114★,
  Java, CTT + IRT) still carries **no licence file at five filenames across three
  branches**. The R options remain copyleft (`lavaan` GPL-2+, `blavaan` GPL-3) —
  except `guess`, above, which is MIT and is now shelved.
- 🟡 **[`joakimwallmark/irtorch`](https://github.com/joakimwallmark/irtorch) was
  already read, and this base asked for it again.** `568-B`'s ask was *"probe
  `irtorch` for liveness and grant"*;
  [`../repos/trending.md`](../repos/trending.md) already recorded it as **MIT**
  (`main/LICENSE.txt`, 1,073 B), **v0.5.5 · 2026-08-24 · 26 releases**, *"freshest
  in tier"*, last commit `2026-10-19`. 🔴 **A second instance of `568-A`'s own
  failure mode, inside the very pass that registered `568-A`** — see `569-A`.

🟢 **So the sentence to give a client changed this pass.** Not *"you will have to
build item calibration"* but *"item authoring, gating, calibration, equating and
guessing-correction are all available permissively, and all of it is pre-adoption
software you must validate before you stake an exam result on it."* Those are
different engagements, and only one of them was true last pass.

## Lecture-video layer (new in the sixth pass — the fifth pass's `topic:video` ask)

**The sweep ran and the result is thin, which is itself the finding:** there is no
open-source lecture-video product to adopt, and there *is* a well-understood
four-stage pipeline to assemble — slides → page images → narration script → TTS
and mux. Every stage has a permissive component already on this page.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [galaxyproject/video-lectures](https://github.com/galaxyproject/video-lectures) | **MIT** (`master/LICENSE`, 1,071 B, "Copyright (c) 2024 Galaxy Project") | 2 | Global | ✅ permissive | **The reference pipeline and the only institutionally held row on this axis.** Pandoc turns `src/*.md` into HTML slides plus a hands-on document; `wkhtmltoimage` extracts one image per slide; `extract-script-from-html.js` pulls the narration text; `ari` muxes images and script into a narrated video; Yarn/Jake orchestrates. 67 commits on `master`, forked from `jxtx/covid-lessons`. ⚠️ **It terminates in Amazon Polly and the Jakefile needs AWS credentials** — swap the TTS stage before quoting it to any data-residency-constrained client. |
| [jhudsl/ari](https://github.com/jhudsl/ari) | **MIT** — declared in `DESCRIPTION` (`License: MIT + file LICENSE`); the `LICENSE` file is a **40 B stub** | — | North America | ✅ permissive | The narration-and-assembly **engine** under the row above, an R package from the **Johns Hopkins Data Science Lab** — a named institution, which is what places it. ⚠️ Its grant is **not readable from `LICENSE`**: the CRAN idiom this page already records puts the licence in `DESCRIPTION` and leaves `LICENSE` holding only a year and a holder. |
| [Changochen/slide-to-video](https://github.com/Changochen/slide-to-video) | **MIT** (1,070 B, "Copyright (c) 2024 Yongheng Chen") | — | Global | ✅ permissive | PDF deck plus a plain-text script, slides split on a `NEWSLIDE` marker, out to a narrated video. **The one row on this axis that can run with no cloud TTS at all** — it supports optional local voice cloning, which makes it the default pick for an offline or sovereignty-constrained engagement. |
| [htlin222/slides-to-video](https://github.com/htlin222/slides-to-video) | **MIT** (1,065 B, "Copyright (c) 2026 htlin222") | — | Global | ✅ permissive | ImageMagick page images → **model-generated speaker notes** → TTS → `ffmpeg`. The only row that *drafts* the narration rather than requiring a finished script, which is the stage a content team actually wants automated. |

🟢 **The substitution that makes this layer deliverable.** Three of the four rows
end in a proprietary cloud TTS. The permissive replacements are already shelved in
the narration layer below: [`denizsafak/abogen`](https://github.com/denizsafak/abogen)
(**MIT**, and it emits **synchronised captions** — an accessibility deliverable,
and the European Accessibility Act is a procurement gate across EMEA public
education), [`Blaizzy/mlx-audio`](https://github.com/Blaizzy/mlx-audio) (**MIT**,
Apple Silicon), and [`supertone-oss-archive/supertonic`](https://github.com/supertone-oss-archive/supertonic)
(**MIT**, on-device, ⚠️ **archived** — the grant is perpetual, the patches are not).

⛔ **Explicitly not shelved:** `harry0703/MoneyPrinterTurbo` (MIT, 136,744★) stays
rejected on the fourth pass's reasoning — it is short-form social video, not
lecture content, and its star count makes it the most likely thing on this axis to
be mis-offered as courseware tooling.

## Deck and document generation — extending the fourth pass's layer

The fourth pass found `ppt-master` (MIT, 71,498★) through a listicle. The
capability sweep confirms it sits in a **cohort**, which matters because
single-repo dependencies on a 71k★ project with unverifiable provenance are a
risk a client will ask about.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --: | --- | --- | --- |
| [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | **Apache-2.0** (file, 11,375 B) | 32,854 | Global | ✅ permissive | *"The first and best Office suite purpose-built for AI agents to read, edit and automate"* — DOCX, XLSX, PPTX from a CLI. The **agent-facing** alternative to `ppt-master`'s generate-from-scratch model: it edits the client's existing documents in place, which is what "update our 400 lesson plans" actually requires. C#, single binary, no Office install needed; 2,234 forks, created 2026-03-15. |
| [dream-num/univer](https://github.com/dream-num/univer) | **Apache-2.0** (file `dev/LICENSE`, 10,173 B) | 22,832 | Global | ✅ permissive | *"The Office Harness for AI Agents"* — embeddable spreadsheets, docs, slides and canvas as an SDK. Branch **`dev`**. Use when the deliverable is an **in-product editing surface** (a worksheet the student fills in) rather than a file. |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | **Apache-2.0** (file, 11,345 B) | 11,418 | Global | ✅ permissive | *"Free, open-source AI Office suite"* — Docs, Sheets, Slides, PDF, Markdown and HTML editors, **local-first**, LibreOffice-backed. Pairs with `PAIDEIA` for a fully offline authoring stack. |
| [tw93/Kami](https://github.com/tw93/Kami) | **MIT** (file, 1,061 B) | 12,173 | Global | ✅ permissive | *"Layout rules and templates that let AI agents export PDF, PPTX…"* — **typesetting quality**, which is the usual reason generated courseware looks unusable to a teacher. The cheapest fix for the "it works but it looks wrong" objection. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** (file, 1,070 B) | **75,894** | Global | ✅ permissive | Not a tool — **courseware**. A full AI-engineering curriculum, 13,381 forks, #1 on GitHub Trending 2026-05-24. **MIT means a client's internal academy can fork, rebrand and extend it**, which is the single fastest route to a credible AI-upskilling programme and is worth more to a corporate-L&D buyer than any generator on this page. Rejected from the agent shelf (see [`../agents/top.md`](../agents/top.md)) because it has no learner model. |

**How this layer changes the economics.** The content-production layer generates;
this layer **ingests what the client already owns**. That ordering is the
commercial point: an engagement that starts by generating new material competes
with the client's own faculty, while one that starts by ingesting the existing
textbook, past papers and lecture notes is **migration work**, which is easier to
scope, easier to value and impossible for the client to do with a chatbot
subscription. Pattern **P-570-A** wires the two together.

## The LMIC supply side — `AI-for-Education` (closes a three-pass gap)

Three consecutive passes of this KB declared: *"no African education platform or
agent repository appears anywhere."* That gap is now closed, and the thing that
closed it is an organisation rather than a repository.

[**AI-for-Education**](https://github.com/AI-for-Education) describes itself as
*"Empowering Education in LMIC's with AI"* and *"a collaborative hub for
developing and sharing AI tools and resources aimed at revolutionizing education
in low and middle-income countries (LMICs)."* Site `ai-for-education.org`.
**Location is not stated** on the profile, so the organisation is recorded as
EMEA on the balance of its one published benchmark paper and contact domain, and
that inference is flagged rather than hidden.

**19 repositories; 10 are MIT** (confirmed by querying GitHub's licence index,
`license:mit org:AI-for-Education`). The ones that matter:

| Repo | Licence | ★ | What it is, and why it closes the gap |
| --- | --- | --- | --- |
| [lesson-plan-parse-mbsse](https://github.com/AI-for-Education/lesson-plan-parse-mbsse) | MIT | 1 | **Sierra Leone's Ministry of Basic and Senior Secondary Education (MBSSE)** publishes Maths and Language Arts lesson plans as PDFs; this converts them to structured JSON and cleans them with an LLM. One star, and it is the most important row on this page for an African engagement: it is **real ministry curriculum, parsed, in the open, under MIT**. |
| [luganda-linguistic-benchmarks](https://github.com/AI-for-Education/luganda-linguistic-benchmarks) | — | 0 | Linguistic benchmarks for **Luganda** (Uganda). Evidence that African-language evaluation assets exist at all. |
| [global-proficiency-framework](https://github.com/AI-for-Education/global-proficiency-framework) + [gpf-alignment](https://github.com/AI-for-Education/gpf-alignment) | — / MIT | 0 / 1 | Digitising the **Global Proficiency Framework** and automating alignment to it. GPF is the cross-country learning-standards frame used where no rich national standard exists — the LMIC analogue of US state standards. |
| [nemoasr-android](https://github.com/AI-for-Education/nemoasr-android) | — | 1 | On-device ASR on Android (Kotlin). Speech recognition **without connectivity** is the binding constraint in low-bandwidth classrooms; this is the only repo in this KB that addresses it. |
| [voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | MIT | 1 | Evaluation harness for voice AI — the modality that works where literacy or devices do not. |
| [fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | MIT | 9 | The org's own LLM client library, 10 forks. The plumbing the rest depends on. |
| [edu-qurating](https://github.com/AI-for-Education/edu-qurating) | MIT | 3 | Quality rating of educational content. |
| [primerpro](https://github.com/AI-for-Education/primerpro) | — | 0 | Python port of PrimerPro decodability functions — early-reading text levelling. |

**How to read this honestly.** This is a **supply side measured in single-digit
stars**. It is not a market; it is a toolkit, and most of it is pre-1.0. But it
is MIT-licensed, it is pointed at named African ministries and languages, and it
is the only thing of its kind located in three passes of searching. For an
engagement in sub-Saharan Africa it is the starting point. For a commercial
engagement anywhere else, the GPF-alignment and decodability work is reusable
wherever a client lacks a rich standards corpus.

## Adjacent systems of record

Not learning platforms, but systems an institution already runs — and what an AI
search or discovery agent is usually pointed at.

| Repo | Licence | ★ | Region | Build-on? | What it is |
| --- | --- | --- | --: | --- | --- |
| [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | ✅ permissive | "(Official) The DSpace digital asset management system that powers your Institutional Repository." Java. **The most permissively licensed platform of record anywhere in this KB** — confirmed in the sidebar and in `LICENSE` on `main` ("BSD 3-Clause License, Copyright (c) 2002-2021, LYRASIS"). LYRASIS is a US non-profit. |
| [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | ⛔ copyleft | "Koha is a free software integrated library system (ILS)." Uses its **own bug tracker rather than GitHub issues** — relevant to any contribution plan. Origin not stated on the repository page. |

**Why DSpace matters more than its star count suggests.** Every other platform of
record in education is GPL or AGPL. DSpace is BSD-3-Clause, so the one category
where a client *can* own a proprietary derivative is the institutional
repository — theses, datasets, faculty output, grey literature. That is also the
corpus a RAG research agent most wants.

## What this means in practice

A client on Moodle, Open edX, Canvas or Chamilo cannot have AI features delivered
as a proprietary fork — AGPL/GPL forbid it on any hosted-service reading. The
licence-clean routes are:

- **Attach across a standard boundary.** **LTI 1.3** (`ltijs`, Apache-2.0) to
  launch a tool inside the LMS and write grades back; **MCP** (the servers in
  [`../agents/top.md`](../agents/top.md), MIT) for agent read access; **xAPI →
  LRS** (`xAPI-Spec` Apache-2.0, `ralph` MIT) for telemetry without touching
  platform internals; and — **new in the fourth pass** — **SCORM**
  (`scorm-again`, MIT) to deliver courseware *into* the platform the way the
  installed base already ingests it. All four are permissive. This remains the
  default, and it now covers content delivery as well as launch, read and
  telemetry.
- **Or replace the substrate, which is newly possible.** `Selleo/mentingo` (MIT,
  Poland) is an AI-native LMS with xAPI and SCORM built in and white-labelling as
  a stated goal. At 102★ it carries adoption risk a Moodle install does not —
  but it is the first time this KB can offer a permissive substrate instead of
  only a permissive boundary.
- **Gate the output.** `learning-commons-org/evaluators` for rubric scoring and
  `pedagogy-benchmark` for pedagogical knowledge are the two verified ways to
  show a client that generated instructional content was *measured* and not just
  generated. Both are small; both are the only options.

## Declared gaps

- **No permissive platform of record exists at Moodle/Open edX scale.** Still
  true, now bounded on three sides and **measured**. It holds for the **LMS of
  record** category. It does **not** hold for the **institutional repository**
  (DSpace, BSD-3-Clause, category leader), it is **weakening** for the
  **AI-native LMS** niche (`mentingo`, MIT, 102★), and as of this pass it does
  **not** hold at the **small-and-medium-institution SIS** tier
  (`academico`, MIT, 410★, 151 forks). The denominator is now on the record: the
  entire permissive LMS population above 50★ is about **eight repositories**.
  A client needing a permissive substrate at *university* scale still assembles
  rather than adopts; a language school, training institute or private school
  group no longer has to.
- ~~**No African-origin repo appears anywhere on this page.**~~ **Closed, with the
  qualification stated above:** `AI-for-Education` is an LMIC-focused
  organisation with MIT tooling built against Sierra Leonean curriculum and
  Ugandan language data, but its own **location is not stated** and its repos are
  0–13★. African *artefacts* are mapped; African-*domiciled* publishers are not.
  That is the next pass's question, and it should be asked on GitHub's index, not
  the open web — which is what finally worked here.
- ~~**`NOASSERTION` is not the same as "no licence".**~~ **Closed as a question
  and promoted to a catalogue.** Both `learning-commons-org` repos reported
  `NOASSERTION`; both are now read first-hand and they are **different** split
  grants — `knowledge-graph` is code-MIT / data-per-publisher, `evaluators` is
  code-MIT / prompts-CC-BY-4.0 / **corpora-NC**. `digitalinnovationone/dio-agent`
  (2,750★) returns no `license` field at all and has no file on either branch:
  genuinely unlicensed. `24kchengYe/human-skill-tree` (586★) matched no licence
  filter and is **AGPL-3.0 on `master` with a dual-licensed `skills/`
  directory**. **Four distinct states behind one ambiguous API value, plus a
  branch-name trap.** The rule that resolves all of them is now executable from
  this session: **read the file, on every filename, on every branch.**
- **The instrument that made this possible is new and should be used
  deliberately.** `raw.githubusercontent.com` returns HTTP 200 here;
  `api.github.com` and `github.com` HTML return 403; MCP `get_file_contents` is
  **repo-scoped** and refuses third-party repositories; `search_users` exposes no
  `location`. Twenty-one licence files were read this pass. **Region, by
  contrast, got harder** — owner country is unobtainable by any available route,
  so new rows are placed only from licence-file copyright holders (which is how
  `richie` was placed to EMEA), publisher or payment-stack signals (flagged as
  inferred), or left **Global**.
- **Licence defects cluster in the agent layer.** Across three passes: platforms
  state copyleft clearly and accurately; agents claim MIT in prose with no file
  (`mcp-canvas-lms`), ship share-alike content licences on code-shaped artefacts
  (`Auto-Empirical-Research-Skills`, CC BY-SA 4.0, 4,843★), or state nothing at
  2,750★. The substrate is honest; the fast-moving layer is not.
- ~~**No open-source learning-analytics *dashboard* was located**, only the LRS
  (`ralph`) that feeds one. The presentation layer of learning analytics appears
  to be entirely commercial; not re-verified this pass.~~ 🔴 **STRUCK
  `2026-10-31` (`p570`) — and this is `568-A`'s THIRD live instance, on a third
  page.** `p568` refuted this sentence by shelving
  [`openfun/warren`](https://github.com/openfun/warren) and
  [`openfun/potsie`](https://github.com/openfun/potsie), both **MIT**, both from
  **France Université Numérique**. `p569` struck the copy on
  [`trending.md`](trending.md):179 **and left this one standing.** 🔵 **The
  mechanism is the measured cost of `569-A`'s own residual:**
  `ingest/absence-claims.py` reports and cannot gate, its `27` narrow-tier
  collisions were never triaged into a baseline, and so a claim its own author
  had already refuted survived a further pass on a page nobody re-read.
  **An instrument that reports is worth exactly as much as the triage nobody
  ran.** The gap register's entry is `569-A`; its first ask is now overdue twice.
- ~~**Horizontal tooling is systematically under-covered.**~~ **Swept and closed
  on the fifth pass — and the prediction was an understatement.** The fourth pass
  guessed the blind spot hid "document parsers, TTS pipelines, assessment-item
  generators and video tooling". The capability sweep returned **sixteen
  permissively licensed repositories, five of them above 30,000★ and three above
  69,000★** — `PaddleOCR` (92,024), `MinerU` (82,860), `tesseract` (77,267),
  `ai-engineering-from-scratch` (75,894), `docling` (69,909), `OfficeCLI`
  (32,854), `opendataloader-pdf` (30,129). **The horizontal layer is larger than
  the entire education-specific supply in this KB combined**, and it had been
  invisible for four passes to a filter nobody questioned. Two sub-gaps remain
  open: **assessment-item generators** returned nothing permissive and
  education-specific, and **video tooling** was not swept (`MoneyPrinterTurbo`,
  MIT, 136,744★, surfaced incidentally and is short-form social video, not
  lecture content — it is not shelved and should not be treated as courseware).
- **The generalisable lesson, since it will recur in every other industry KB:**
  a sweep filtered on an industry topic measures *how a repository markets
  itself*, not what it does. The tools an industry runs on are usually tagged by
  **capability**, because their authors are selling to everyone. Sweep both axes
  or report an undercount.
### Added on the eighth pass (`p570`)

- 🔴 **The evaluation gap is NARROWER, not closed, and the narrow statement is
  the useful one.** Seven granted rubric-scoring assets now exist on this page.
  **None of them is a runtime drift detector.** What a client can now be told:
  *"you can pin, version and re-run a rubric-based quality gate over your tutor's
  outputs and over its multi-turn trajectories, with permissive code"* — which
  was not true last pass. What remains untrue: *"you will be alerted when the
  deployed tutor degrades."* `evidentlyai/evidently` (Apache-2.0) remains the
  generic pick for that and is not education-aware. **Seventh consecutive pass
  with no education-specific runtime monitor; this is still the clearest unmet
  build opportunity in the industry.**
- 🔴 **A commit count is now a claim this base must verify, not a datum it may
  read.** `p569` made commit density the admission signal for this layer;
  `p570` found a `2,137`-commit synthetic history on the first never-swept axis.
  [`../ingest/history-plausibility.py`](../ingest/history-plausibility.py) is
  committed and runs; **its four checks cost one shallow clone per candidate and
  should run before any row is admitted on commit density.** The instrument
  reproduces its founding case and passes two real controls (`mirt`, `dexter`).
  🔵 **Generalises past education: any base on this harness that shortlists on
  commit count inherits this exposure.**
- 🔴 **Four of four Apache-2.0 rows name no licensor.** Not a defect in any one
  repository — Apache-2.0's template simply has no copyright line, and GitHub's
  "Apache-2.0" determination is correct in every case. **It means region is
  unrecoverable from an Apache grant by construction**, and it means the
  `terracotta` observation this base recorded as a one-off trap is in fact the
  normal case for that licence family. See `570-C`.
- 🔴 **The closed region vocabulary has no Africa value, and this base's EMEA
  counts are therefore not a market measurement.** `SMART-GRADE` (Cameroon) is
  recorded `EMEA†` because the five permitted values leave nowhere else to put
  it. 🔵 **State the grade and the country whenever an EMEA count is quoted**, or
  an African school-IT artefact and a German research institute read as the same
  market. Registered as `570-E`. The field is not the place to fix this — the
  vocabulary is closed on purpose and inventing `Africa` would break every
  downstream filter; the fix is the `†` marker plus the country in prose.
- 🔴 **`568-A` has now recurred on three separate pages across three passes.**
  The learning-analytics-dashboard sentence struck above was refuted by `p568`,
  struck on one page by `p569`, and survived on this one. **The instrument that
  catches this class exists and does not gate**, because `569-A`'s triage of the
  27 collisions into a baseline was not done at `p569` and was not done here
  either — this pass spent its budget on discovery and verification. 🔵 **It is
  now the oldest cheap unfinished item in this base and it should be the next
  pass's first action, before any search leg runs.**
- **`ulearn`'s maturity is unassessed beyond its stack.** 701★ MIT is the largest
  permissive LMS found and Laravel 5.8 is five major versions behind. Nobody
  should be told it is a starting point without an upgrade estimate attached.
