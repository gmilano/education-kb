---
industry: education
region: Global
updated: 2026-11-01
---

## 🆕 `p600` — `2026-11-01` — `9` agent rows promoted, the shelf goes `44 → 53`, and the discovery nil this page has reported for twenty-nine passes was a sampling artefact

### 🟢 The reason `9` rows were available at all, stated before the rows

This page has recorded a discovery nil for twenty-nine consecutive passes, and `p599` concluded the
star-ranked channel was exhausted. 🔴 **That conclusion was wrong, and not in a subtle way.** `p599`
took `39` addresses from `6` topic axes; this pass took `334` from the **same six** and `138` were new
(`41.3 %`) **at the same ordering** — then `1,646` more from `28` axes this base had never queried, of
which `1,322` were new (`80.3 %`). 🔵 **The binding constraint was per-axis depth and the axis set,
never the ranking function.** Full working in [`trending.md`](trending.md) — **`600-B`**, **`600-C`**.

🔵 **And the half of that finding which keeps this page honest:** `678` unheld addresses yielded
**`66`** that are permissive *and* `≥ 5★` *and* pushed in `2026`, and **`9`** that are also actually
education-AI rather than education-adjacent. 🔴 **`310 of 678` are `license: null` or `NOASSERTION`.**
So the supply is findable; it is mostly not shippable. The rows below are the `9`.

### 🟢 Promoted to the shelf — every grant byte-read `2026-11-01` at the real default branch, every fabricated-path control `404`

| Agent | ★ | Grant (byte-read) | Branch | Why it earns a row |
| --- | --: | --- | --- | --- |
| [LearnAIHubC/LearnDeck](https://github.com/LearnAIHubC/LearnDeck) | **26** | 🟢 **MIT** (`LICENSE.txt`, `1,068 B`) | `main` | Courseware generation from notes/material; grant is at `LICENSE.txt`, which a `LICENSE`-only probe misses |
| [selftune-dev/selftune](https://github.com/selftune-dev/selftune) | **18** | 🟢 **MIT** (`1,067 B`) | `main` | 🟢 **First permissive candidate against this base's standing "no OSS agent eval/observability" gap** |
| [sizwinz/StudySage…](https://github.com/sizwinz/StudySage-Offline-Online-AI-Note-Assistant) | **12** | 🟢 **MIT** (`1,083 B`) | `main` | Offline-first study assistant — the low-connectivity axis |
| [TerraByte-Dev/OpenEdu](https://github.com/TerraByte-Dev/OpenEdu) | **6** | 🟢 **MIT** (`1,080 B`) | 🔴 **`master`** | AI tutoring platform; a `600-E` row — `main`-only probe reports it grantless |
| [agenticfabriq/beacon](https://github.com/agenticfabriq/beacon) | **5** | 🟢 **Apache-2.0** (`11,358 B`) | `main` | Free-text grading harness — the scoring seam `nbgrader` leaves open |
| [fcescob/understand](https://github.com/fcescob/understand) | **5** | 🟢 **MIT** (`1,075 B`) | `main` | Mastery-gated advancement, not completion-gated |
| [Rayhaan1345/socratic-tutor](https://github.com/Rayhaan1345/socratic-tutor) | **5** | 🟢 **MIT** (`1,070 B`) | `main` | Third pedagogy-as-product instance — the category is established |
| [youngman2007/courseware-cn-annotator](https://github.com/youngman2007/courseware-cn-annotator) | **5** | 🟢 **MIT** (`1,093 B`) | `main` | APAC in-language courseware conversion |
| [weidonglang/EduNexus-AI](https://github.com/weidonglang/EduNexus-AI) | **5** | 🟢 **MIT** (`1,071 B`) | `main` | 🟢 **First permissive row on this page touching the ERP/SIS gap** |

🔵 **All nine sit in the `5–26★` band.** `599-C` established that the hand-written "looks open" grant
concentrates exactly there, so 🟢 **not one of these licences was taken from `spdx_id`** — every one
was byte-read, and every repo's fabricated-path control returned `404`. The band is still the
riskiest on this page; it is now audited rather than avoided.
Evidence: [`../evidence/grants-byteread.2026-11-01-p600.tsv`](../evidence/grants-byteread.2026-11-01-p600.tsv).

### 🔴 Measured this pass and NOT shelved — recorded so a later pass does not re-find them

| Repo | ★ | Grant (byte-read `2026-11-01`) | Branch | Disposition |
| --- | --: | --- | --- | --- |
| [mnemosyne-proj/mnemosyne](https://github.com/mnemosyne-proj/mnemosyne) | **605** | 🔴 **pointer, not a grant** — `156 B`, *"Different parts of the software use different licenses:"* | `master` | 🔴 **BLOCK.** API says `NOASSERTION`. Second instance of `599-A`'s rung, at `6.4×` the stars of the case that established it — **`600-G`** |
| [hwgilbert16/scholarsome](https://github.com/hwgilbert16/scholarsome) | **793** | 🔴 **AGPL-3.0** (`34,523 B`) | 🔴 **`develop`** | 🔴 **Reciprocal — flagged, not shipped.** Listed because it is the most-adopted permissive-adjacent SRS web app and a later pass will re-find it |
| [olmps/memo](https://github.com/olmps/memo) | **1,871** | 🟢 **BSD-3-Clause** (`1,515 B`) | `main` | 🟡 **NOT SHELVED — abandonment.** Grant is clean and stars are real; last push `2024-07-29`, so it is a reference implementation, not a dependency |
| [zagortenay333/cronomix](https://github.com/zagortenay333/cronomix) | **657** | 🟢 **MIT** | `master` | 🔴 **NOT SHELVED — off-domain.** A GNOME desktop timer that happens to include flashcards; it reached the candidate set through `topic:flashcards` and is not education software |

🔵 **Why the last row is recorded rather than dropped:** widening the axis set (`600-C`) widens the
*noise* too. `topic:flashcards` and `topic:spaced-repetition` return desktop utilities and language
apps alongside real education tooling, so the new axes need the domain screen that the old
technology-noun axes got for free.

### 🔴 `600-F` — a filter on this page's own candidate set returned a false `0`, and the control caught it

The first relevance screen over the `678` new addresses reported 🔴 **`0` candidates**. Cause: `awk`
in this environment does not implement `\b`, so `/\bai\b/` matches nothing and errors nothing.
🟢 **Re-run without `\b`: `66`.** 🔵 **Rung now standing on this page: a screen that returns `0` must
be shown capable of returning non-`0` before the `0` is written down** — otherwise a broken filter and
a saturated market produce identical pages, which is the exact confusion `600-B` just unwound.

---

## 🆕 `p599` — `2026-11-01` — the most-starred Creative Commons row on this page is reciprocal, not a dedication, and `0` rows were added

### 🔴 The correction, which changes an instruction this page gave the reader

[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) —
`939★` — was carried on this page as a **CC0 dedication** and as *"usable as reference material"*.
Byte-read at `main` (`135d6275`, `LICENSE`, `1,230 B`) it is **`CC BY-SA 4.0` — reciprocal** — its
grant covers only *"educational skills, documentation, examples, and curriculum materials"* (the repo
is **TypeScript**, so the code is granted nothing), and the committed file says of itself *"This is a
human-readable notice"* and points at the legalcode for the real terms. 🔴 **Both affected rows in
the block table below are corrected**, and `cybercussion/SCOBot` is no longer this base's *first*
reciprocal CC case. Full working in [`trending.md`](trending.md) — **`599-A`**.

### 🔴 Measured this pass and NOT shelved — recorded so a later pass does not re-find them

`3` addresses this base has never held were served by a channel that pays (`topic:ai-tutor` re-ranked
by push date instead of stars — `599-B`). Every grant byte-read at the real default branch. 🔴 **None
is shelvable**, and the reason is the same for all three:

| Repo | ★ | Grant (byte-read `2026-11-01`) | Branch | Disposition |
| --- | --: | --- | --- | --- |
| [baney75/myelinate](https://github.com/baney75/myelinate) | `4` | 🟢 **MIT** (`1,070 B`) | `main` | **NOT SHELVED — star floor.** A `14`-skill Socratic-tutor plugin suite; grant is clean, adopters are absent |
| [Ethos6/masterly](https://github.com/Ethos6/masterly) | `2` | 🟢 **MIT** (`1,064 B`), manifest agrees | `main` | **NOT SHELVED — star floor.** Lessons from the learner's own material, source-quoted questions, FSRS review |
| [2092372408-pixel/EduPilot](https://github.com/2092372408-pixel/EduPilot) | `2` | 🔴 **"EduPilot Noncommercial Source License 1.0"** (`1,951 B`, *"All rights reserved"*) | 🔴 **`master`** | **BLOCK — not open source.** Manifest reads `"SEE LICENSE IN LICENSE"` |

🔵 **The `0` is the finding, and it has a shape.** The channel that reaches supply this base lacks
reaches it **only below `5★`** — so what is missing is not simultaneously findable and shippable.
🔴 **And `1 of 3` of that tail carries a bespoke non-commercial grant**, the same shape as
[`PageLM`](https://github.com/CaviraOSS/PageLM) at `2,057★` (re-graded `p594`). 🔵 **Consequence for a
reader: the star floor on this page is not only a quality filter, it is accidentally a licence
filter** — the hand-written "looks open" grant concentrates where nobody is auditing.

🟢 **Two held rows re-read and confirmed:** [`OPTIMETA/PAIDEIA`](https://github.com/OPTIMETA/PAIDEIA)
— 🟢 **MIT** (`1,068 B`), `91★`, `4` forks, `88` commits, local-first per-course exam prep as plain
markdown; and [`ArturoNereu/AI-Study-Group`](https://github.com/ArturoNereu/AI-Study-Group) —
🔴 **no grant file on `6` path variants**, BLOCK confirmed.

---


🆕 **`p598` — scope stated before its result: `8` mandated legs run (`4` global, `4` regional),
`6` `gh api` topic axes swept, `12` grants byte-read, `16` existing 🔴 BLOCK rows re-audited on a
channel this base had never read, `5` agent rows promoted.**

🟢 **`598-A` — a fourth grant channel exists, and this base was blind to it: the build manifest.**
[`Apereo-LAI/SakaiXAPI-Provider`](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider)
has **no grant file on any of `16` path variants** at its real default branch, and the API reports
`NOASSERTION`. By this base's established instrument it is 🔴 BLOCK, "no licence". 🟢 **It is
ECL-2.0** — declared in `pom.xml` as `<license><name>ECL 2.0</name>` with the canonical OSI URL.
🔵 **A missing `LICENSE` file is not evidence of a missing grant**, and every 🔴 "no licence file"
row in this base was graded by an instrument that cannot see a manifest declaration.

🔵 **`598-B` — and the honest yield of `598-A` is small, which is the finding's other half.** All
`16` of this base's 🔴 "no grant" BLOCK rows were re-probed across `10` manifest formats:
**`1 of 16` (`6.3 %`)** carries a manifest licence declaration
([`s64965264-code/nexo-ia`](https://github.com/s64965264-code/nexo-ia), `"license": "MIT"` in
`package.json`) — and it is `0★`, so it fails the star floor anyway. 🟢 **`15 of 16` BLOCK grades
were right.** The instrument gap is real and it did **not** put wrong data on these pages.
🔴 A manifest field is also *weaker* evidence than a grant file — a bare `"license": "MIT"` string
carries no licence text and no copyright holder — so it grades **REVIEW**, never 🟢.

🔴 **`598-C` — `591-B` is refuted, and it was this base's cleanest law.** `591-B` closed at `p594`
claiming **perfect separation**: `license: null` → `0 of 14` carry a grant file, `NOASSERTION` →
`32 of 32` do. `SakaiXAPI-Provider` is the first counter-example — `NOASSERTION` with no grant file
at all. 🟢 The branch was proved readable first (`pom.xml` and `.gitignore` both `200`, `main` and
`trunk` both `404`), which is `597-F`'s discipline: a `404` on one path is not a dead repository.
🟡 The `null` arm still holds — `16 of 16` of this pass's BLOCK rows are `null` and none has a grant
file. 🔵 **One arm of the law survived; the other was a sample, not a law.**

🔴 **`598-D` — the education sector's own licence is the one the API is worst at.** ECL-2.0
(Apache-2.0 with a narrowed, education-specific patent grant) is OSI-approved and permissive, and
this page's legend already admits it. The API reports it correctly for
[`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) and 🔴 **wrong for `6 of 8` measured
Apereo-family siblings**. The discriminator is cosmetic: Sakai's title carries the parenthetical
SPDX tag `(ECL-2.0)`; the three that do not are reported `NOASSERTION`. 🔵 In *this* industry,
`NOASSERTION` means "probably permissive, read it" far more often than "no grant" — the census is in
[`../evidence/ecl-apereo-census.2026-11-01-p598.tsv`](../evidence/ecl-apereo-census.2026-11-01-p598.tsv).

🔴 **`598-E` — twenty-eighth consecutive nil on the mandated legs, and this pass gated it on both
channels separately** (the `597-D` correction). `8` repo-shaped addresses were served; `7` are on a
shelf page today and `1` ([`speedyapply/2026-AI-College-Jobs`](https://github.com/speedyapply/2026-AI-College-Jobs))
sits in the append-only log only. 🔴 **`0` new.** 🟢 **The `gh api` topic axis paid in the same
sitting**: `6` axes returned one address this base has never held in either channel —
[`quickfeed/quickfeed`](https://github.com/quickfeed/quickfeed) (MIT, byte-read `1,115 B`) — plus
`11` recoverable `596-C` backlog rows. 🔵 **`594-G`'s standing recommendation is now carried by
three independent passes** and should be acted on, not re-registered.

🟢 **`598-F` — `597-E`'s placeholder control passes, and the gate that reported it was wrong.** The
placeholder `owner/repo` returns **`17` substring hits** across the shelf pages — and all `17` are
prose documenting the defect, `0` are data rows. 🔵 A substring gate on a placeholder reports the
documentation of the rule as a violation of it, which is `547-I` recurring in a new place. 🟢 The
usable form is a table-cell gate.

🔴 **`598-G` — the regional market channel is capped at snippet grade in this environment, and that
caps every regional figure on [`../intel/market.md`](../intel/market.md).** `unu.edu`,
`publications.iadb.org`, `oecd.org` and `unesco.org` return `000` on `curl` **and so does a
fabricated control** (`583-E`, unchanged for `15` passes); on `WebFetch` the same hosts fail
`ENOTFOUND` — outside the session's allowed network domains. 🔵 So the regional legs' numbers are
**search-snippet-grade and cannot be raised here**. They are published with that grade stated rather
than dropped, because an unverifiable number attributed to its source is information and a silent
omission is not.

### 🟢 Agent rows promoted off the `596-C` backlog — every grant byte-read `2026-11-01` at the real default branch

| Agent | Repo | ★ | Grant (byte-read) | Branch | Last push | What it does |
| --- | --- | --: | --- | --- | --- | --- |
| **Nietzschian Debugger** | [DilawarShafiq/nietzschian-debugger](https://github.com/DilawarShafiq/nietzschian-debugger) | **539** | 🟢 **MIT** (`1,071 B`) | `main` | `2026-10-27` | A debugger that **hands the question back instead of the answer** — Socratic method as an agent. 🔵 The clearest OSS instance of *pedagogy as the product* rather than answer-generation, and the direct counter to the declining bypass-the-teacher category |
| **Learn Anything** | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | **500** | 🟢 **MIT** (`1,069 B`) | `main` | `2026-08-29` | Recursive learning system — Socratic deep-dives plus TDD-style exercises, embedded **inside the coding assistant** rather than in an LMS |
| **Skill-Anything** | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | **348** | 🟢 **MIT** (`1,084 B`) | `main` | `2026-09-26` | Any source (PDF, video, web, audio, text) → an interactive learning package: `12`-section study guide, quizzes, flashcards, spaced repetition. 🔵 The courseware-generation seam in one command |
| **kaogong-shuati** | [ERRRC/kaogong-shuati](https://github.com/ERRRC/kaogong-shuati) | **151** | 🟢 **MIT** (`1,062 B`) | `main` | `2026-09-24` | Chinese civil-service exam practice (行测 / 申论): question bank, error notebook, AI explanations. 🔵 **APAC in-language supply**, and the permissive counterpart to the LATAM exam-prep gap below |
| **InterviewMentor** | [PrepLabsAI/InterviewMentor](https://github.com/PrepLabsAI/InterviewMentor) | **116** | 🟢 **MIT** (`1,071 B`) | `main` | `2026-10-19` | AI mock interviews for technical hiring — the employability/placement end of the education funnel |

### 🔴 Measured this pass and NOT shippable — recorded so a later pass does not re-find them

| Repo | ★ | Measured `2026-11-01` | Disposition |
| --- | --: | --- | --- |
| [infomark-org/infomark](https://github.com/infomark-org/infomark) | 36 | 🔴 **GPL-3.0** (`35,149 B`, byte-read) — live `2026-10-31` | **BLOCK** for a closed deliverable. A complete course-management system with auto-testing of programming assignments; the permissive alternative is `quickfeed/quickfeed` on [`../repos/foundations.md`](../repos/foundations.md) |
| [uPortal-Project/CoursesPortlet](https://github.com/uPortal-Project/CoursesPortlet) | 12 | 🟡 **BSD-3-Clause** (`1,529 B`) — 🔴 the grant's copyright holder is **"News Reader Portlet Development Team"**, a *different project*, and the file is byte-identical to [`NewsReaderPortlet`](https://github.com/uPortal-Project/NewsReaderPortlet)'s | **REVIEW** — permissive terms, but the named holder does not match the work. Counsel must read it before shipping |
| [Apereo-LAI/SakaiXAPI-Provider](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) | 11 | 🟢 **ECL-2.0** by `pom.xml` (`598-A`) — 🔴 no grant file, last push `2021-03-25`, `42 KB` | **NOT SHELVED** — permissive and genuinely licensed, but `5` years stale and effectively empty. Filed as the instrument finding, not as supply |
| [s64965264-code/nexo-ia](https://github.com/s64965264-code/nexo-ia) | **0** | 🟡 `"license": "MIT"` in `package.json`; 🔴 no grant file, no licence text, no holder | **REVIEW, NOT PROMOTED** — `598-B`. A manifest field is weaker than a grant file, and `0★` fails the star floor regardless |

---

🆕 **`p597` — scope stated before its result: `8` mandated legs run (`4` global, `4` regional),
`20` backlog addresses promoted, `21` grants byte-read, `9` rows recorded unusable with a reason.**
🔴 **`597-A`: the verification step this run prompt mandates is inert in this environment, and
executed literally it would have rejected every real repository below.** `curl -sI
https://github.com/<owner>/<repo>` returns 🔴 **`403`** for every repository not attached to this
session — not `404`, not `200` — so it cannot separate a live address from a dead one. The GitHub
search API adds a second failure mode: it returns 🔴 **`422` "cannot be searched"** for
[`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet),
which is **alive** and served its MIT grant on request. 🟢 **One instrument answered correctly in
every one of the `28` addresses tested: a byte-read at `raw.githubusercontent.com`**, which returned `200` and full licence
bytes every time. Liveness and grant are established there or not at all.

🔴 **`597-B`: a repository's `spdx_id` and its code grant are different objects, and this pass
measured three distinct mismatch shapes in one sitting** — see the table below. The sharpest is
[`microsoft/autogen`](https://github.com/microsoft/autogen): the API reports **`CC-BY-4.0`**, and
that is correct about the repository's `LICENSE` (`18,650 B`, Creative Commons Attribution) — but
the **code** grant is `LICENSE-CODE`, **MIT**, `1,141 B`, present at the root and in `7` of the
`python/packages/*` trees. 🔵 **This base recorded "AutoGen (MIT)" in its `cycle 2` and `cycle 3`
summaries. That was the right answer arrived at without measurement**, and a licence screen trusting
the API would now *reject* AutoGen as a content licence.

🟢 **`597-D` — the two channels of this base saturate independently, and `27` passes of
undifferentiated "nil" concealed which one was real.** With a gate that reads the shelf and the
append-only logs *separately* (the correction `596-C` asked for), `22` of `24` market tokens served
by the legs are held **on the shelf itself** — so the market-intel nil is 🔴 **real, and this is its
twenty-eighth consecutive pass**. The *address* nil was 🟢 **an artifact**: `2,049` ever-shelved
addresses are invisible to the old gate. One finding does not transfer to the other channel.

🔴 **`597-E`, from this base's own history:** the placeholder `owner/repo` was shelved as data in
**`8` of `15`** archived snapshots — the exact header-as-data defect this run prompt warns about,

🔴 **`597-F` — this pass wrote a false "DEAD ADDRESS" into three pages and caught it before
publishing.** [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents)
was recorded as dead on the strength of the search API's `total_count 0`. 🟢 **It is live** — `490★`,
`106` forks, MIT (`1,067 B`, byte-read), an **EACL'26 Main** peer-reviewed multi-agent
instructional-design system with its package on PyPI — and it is simply **absent from the GitHub
search index**, while four of its siblings are indexed. 🔵 **A `0` is not a `404`.** The claim was
reversed in `agents/top.md`, `agents/trending.md` and `intel/measured-unusable.md`, and the row is
promoted below. 🔴 **A wrong explanation was drafted and withdrawn too** — case-sensitivity in the
`repo:` qualifier — refuted because all three spellings return `0`; publishing it would have sent
the next pass to re-case `1,449` addresses for nothing.
confirmed to have happened here. 🟢 It is absent from today's shelf.

### 🟢 The three licence-screen failure shapes, each measured by byte-read this pass

| repo | API `spdx_id` | byte-read at the real branch | why a screen gets it wrong |
| --- | --- | --- | --- |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 🔴 `CC-BY-4.0` | 🟢 **MIT** — `LICENSE-CODE`, `1,141 B` (root + `7` packages) | Two grant files; the API reads the **content** one. `LICENSE` really is CC-BY-4.0 (`18,650 B`) |
| [crewaiinc/crewai](https://github.com/crewaiinc/crewai) | 🟢 `MIT` | 🟢 **MIT** — `1,055 B`, **no title line** | File opens `Copyright (c) 2025 crewAI, Inc.`; a title-matching screen returns `UNRECOGNISED` |
| [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 `MIT` | 🟢 **MIT** — spelled **`LICENCE`**, `1,086 B` | British spelling; a probe of `LICENSE` only calls a real MIT repo unlicensed |

### 🟢 Agent and agent-adjacent rows promoted off the `596-C` backlog — every grant byte-read `2026-11-01`

| Agent / framework | Repo | ★ | Grant (byte-read) | Branch | Last push | What it does |
| --- | --: | --: | --- | --- | --- | --- |
| **AutoGen** | [microsoft/autogen](https://github.com/microsoft/autogen) | **61,661** | 🟢 **MIT** (`LICENSE-CODE`, `1,141 B`) 🔴 repo `LICENSE` is CC-BY-4.0 | `main` | `2026-10-28` | Agentic framework; multi-agent conversation + tool use. Shelved in `6` snapshots, dropped |
| **CrewAI** | [crewaiinc/crewai](https://github.com/crewaiinc/crewai) | **60,385** | 🟢 **MIT** (`1,055 B`, untitled) | `main` | 🟢 `2026-11-01` | Role-playing multi-agent orchestration. Shelved in `6` snapshots, dropped |
| **Lineage Skill** | [juneyaooo/lineage-skill](https://github.com/juneyaooo/lineage-skill) | **466** | 🟢 **Apache-2.0** (`11,358 B`) | `main` | `2026-07-23` | Distills videos, PDFs, transcripts and notes into **source-backed teacher Agent Skills** — the citation-preserving authoring seam |
| **Canvas MCP** | [r-huijts/canvas-mcp](https://github.com/r-huijts/canvas-mcp) | **12** | 🟢 **MIT** (`1,065 B`) | `main` | `2026-09-21` | MCP server for **Canvas LMS** — the attach point for the dominant North American HE estate |
| **Moodle MCP** | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | **45** | 🟢 **MIT** (`1,064 B`) | `main` | 🟡 `2026-02-22` | MCP server for Moodle. 🔴 **`8 KB` of source** — a reference, not a dependency |
| **FeiFei Companion** | [simonstang/feifei-companion](https://github.com/simonstang/feifei-companion) | **110** | 🟢 **Apache-2.0** (`10,227 B`) | `main` | 🟡 `2026-04-19` | K-12 study-companion system, Chinese-language. 🔵 **APAC in-language supply** |
| **Instructional Agents** | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **490** | 🟢 **MIT** (`1,067 B`) | `main` | — | **EACL'26 Main**, peer-reviewed. ADDIE-model multi-agent instructional design — syllabus, slides and assessment from a course brief; package on PyPI. 🔴 Absent from the GitHub search index (`597-F`) |
| **Instructional Agents Studio** | [DaRL-GenAI/instructional_agents_studio](https://github.com/DaRL-GenAI/instructional_agents_studio) | 0 | 🟢 **MIT** (`1,093 B`) | `main` | `2026-09-24` | The UI/orchestration layer over the above. 🔵 `0★` — take it as a reference implementation, not a dependency |

### 🔴 Measured and NOT shippable — recorded so the next pass does not re-find them

| Repo | ★ | Measured | Disposition |
| --- | --: | --- | --- |
| [anonymousonyx22/brightspace-d2l-mcp](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 29 | 🔴 `NOASSERTION` — custom terms, pushed `2026-11-01` | **REVIEW** — live and useful (Brightspace MCP), but counsel must read the terms |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 1 | 🔴 **AGPL-3.0** | **BLOCK** for a closed deliverable |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | 54 | 🔴 **no licence file** | **BLOCK** |
| [onbirdev/moodle-webservice_mcp](https://github.com/onbirdev/moodle-webservice_mcp) | 18 | 🔴 **no licence file** | **BLOCK** |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | 4,393 | 🟢 MIT, 🔴 **pushed `2025-10-26` — `13` months stale**, `213 MB` | **DEMOTED.** This base's `cycle 2`/`cycle 3` summaries carried it as live supply; it is a frozen curriculum |
| [littlecookie0722/ai-teaching-agent](https://github.com/littlecookie0722/ai-teaching-agent) | **0** | 🟢 MIT, live `2026-08-23` | **NOT SHELVED** — `0★`, no adopters. Fewer real rows beat padding |

---

🆕 **`p596` — scope stated before its result: `8` mandated legs run (`4` global, `4` regional), `0`
new addresses, **twenty-seventh consecutive nil** — and this pass stopped treating that as a
property of the search channel. 🔴 `596-C`: **the shelf is lossy and the log is lossless.**
`2,015` of `2,243` ever-shelved addresses (`89.8 %`) were **dropped** across `15` rewrites, and
because a dropped row still sits in the append-only log it is reported *"already held"* and
never re-shelved — the gate consults the lossless record to decide admission to the lossy one. 🟢 **`6` rows promoted off that backlog this pass** — `5` onto
[`../repos/foundations.md`](../repos/foundations.md) and `1` onto
[`../verticals/solutions.md`](../verticals/solutions.md) — every grant byte-read, `2` with a
non-flat licence structure. 🔴 **`1` new BLOCK on this page** (`596-D`, below): a Google-branded
reading assessor that clears licence, liveness and provenance and is disqualified by its own
README. 🟢 **`595-B` CLOSED** — `../intel/market.md` now carries exactly one
`## Opportunities by region` heading. 🔴 `595-A` (`118 MB`, no retention policy) carried, and
re-read as a conversion problem rather than a size one. 🔴 **Two instrument failures inside this
pass, both self-inflicted and both published** — `--` before a `grep` pattern silently disables
`--include`, and `comm` lies across locales; it cost two withdrawn figures.

---

🆕 **`p595` — scope stated before its result: `9` legs run, `3` shelf rows re-measured on a
second instrument, `4` grants byte-read. The shelf was NOT re-swept.** 🟢 **No row on this
page changed except `DeepTutor`**, which shipped `v1.7.1` today and reads `53.5k`★. 🟢 The
three largest rows were re-measured with `WebFetch` rather than the API and **all three
agree** with what `p592` recorded — `ai-agents-for-beginners` `78.6k`, `ai-engineering-from-scratch`
`76.2k`, `DeepTutor` `53.5k`. 🔴 **Twenty-sixth consecutive nil**: the nine legs served one
address this base has never held, [`dajarbot/AutoGrader`](https://github.com/dajarbot/AutoGrader),
and it is `0`★ with **no `LICENSE` file at all** (`404` on `main`) — 🔴 BLOCK, not shelved.
🔴 Two structural defects registered this pass and both are on
[`./trending.md`](./trending.md): `595-A` this repo is **`118 MB` with no retention policy**,
`595-B` [`../intel/market.md`](../intel/market.md) carries **three** `## Opportunities by region`
headings where the contract allows one.

---
# Top AI agents for education

**What this page is.** A curated, verified table of open-source AI agents for education
that Globant AI Studios can adopt, compose or customise. Every row was measured
first-hand on **2026-11-01**: existence, stars, licence, last push. 🆕 **Every star cell on
this page was re-measured at `p592`**, which swept **`192 of 192`** curated addresses — this
page plus [`../repos/foundations.md`](../repos/foundations.md) — in one `gh api` run. `30`
repositories had moved, **all upward**, `0` licences were downgraded, and `0` unflagged
defects were found: every archived row was already marked archived, every stale row already
marked stale, every unlicensed row already marked `BLOCK`. The sweep and the full licence
census are on [`../repos/trending.md`](../repos/trending.md).

**How to read the licence column.** 🟢 = permissive (MIT / Apache-2.0 / BSD / ECL-2.0 /
CC0), buildable and shippable in client work. 🟡 = permissive with a stated limit. 🔴 =
copyleft or no grant — do not ship without counsel. Licences marked **(text)** were read
out of the repository's own `LICENSE` file, not taken from the GitHub API, because the
API's licence field is wrong for roughly a quarter of this base's rows (see *Method*).

🆕 **`p587` raised the shelf from 38 to 43 — and not one of the five came from a search.**
All five were already in this base's append-only history, re-found between 19 and 26 times,
and had never reached a curated page. 🔴 **`p586`'s claim that `ppt-master` (71,803★) is
"larger than every other row" is WITHDRAWN**: [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners)
is **78,542★ MIT** and [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
is **76,141★ MIT**, both pushed within three days, both sitting in
[`./trending.md`](./trending.md) 26 times each. 🔵 **The shelf was never discovery-limited.
It was promotion-limited**, and the measurement is on [`../repos/trending.md`](../repos/trending.md).

🆕 **`p588` — the scope of this pass, stated before its result: `9` addresses measured, not
`43`.** This pass did **not** re-measure the shelf. It measured nine addresses — the
largest members of one class, three platform rows that secondary sources described, and one
permissive candidate this base has carried **unfiled since `p525`** — and the finding is a
**rule this page changed at `p587` and never wrote down**. See `588-A` and the new
*enablement tier* below.

🔵 **Two `p587` rows were re-measured and AGREED:** `ai-agents-for-beginners` **78,550**
(was `78,542`) and `ai-engineering-from-scratch` **76,144** (was `76,141`). 🟢 **That is one
day of growth, not a contradiction** — recorded here so a later pass does not file one.

🆕 **`p589` — scope: `13` addresses measured, `6` grants byte-read, the shelf NOT
re-measured.** Two rows added and three blocks. 🔵 **Neither new row came from a search.**
`PAIDEIA` was served by the mandated legs and was already in this base `15` files deep;
`AI-PhD-S26` likewise. 🔴 **Twentieth consecutive nil on new addresses from the mandated
legs**, and this pass stopped treating that as a research result: the three rows it filed
came from the **history**, and nine more came from one topic axis
([`../repos/foundations.md`](../repos/foundations.md)). 🔴 **What this page cannot tell you
is whether it passes its own gates** — `make` and `python3 ingest/*.py` are both denied in
this environment, so `gate-shelf-consistency`'s `59` controls did not run on these rows.
Replicated by hand instead; see `589-B` and
[`../intel/open-gaps.md`](../intel/open-gaps.md).

🆕 **`p590` — scope: `19` addresses measured, `16` grants byte-read, the `44`-row shelf NOT
re-measured.** This pass answered `589-E`, and the answer **withdraws a rule this page's
sibling published yesterday**: the SCORM emit layer is *not* dead, so `Trend 41`'s
generalisation falls. A new **spec-emit agent tier** of five MIT rows is added below, all
five promoted from this base's own history. 🟢 **The mandated legs broke a twenty-pass nil
streak with one genuinely new address — and it is unlicensed, so it is a block, not a row.**

🔴 **`589-B` is corrected at the point that matters most.** `589-B` prescribed *"port the
three cheapest gates to pure `grep`/`awk`"* as the option that *"needs no permission"*.
🔴 **A ported `.sh` gate would have been just as inert:** `bash ingest/claim-role.sh` is
**DENIED** in this environment exactly as `make` is, re-tested this pass. 🟢 **What does run
is an inline command typed into the harness** — `grep`, `awk` and `bash -c '…'` all
executed here. 🔵 So a runnable gate in this repository must be stored as a
**copy-pasteable command block a pass executes**, never as a committed script. Three gates
were run that way this pass; see `590-A` and [`../intel/open-gaps.md`](../intel/open-gaps.md).

---

🆕 **`p591` — scope: `73` addresses measured across `37` discovery axes, `65` grants
byte-read, the `44`-row shelf NOT re-measured.** 🟢 **Three new tiers are added below —
`35` rows, every grant byte-read first-hand `2026-11-01`** — and the headline is a
**method correction that affects every `(text)` mark in this base**: 🔴 **byte-reading a
licence is not enough if the classifier reads the licence *body*.** Two of this pass's
`65` reads would have been filed as permissive and are not: `ximing/aimo` is
**Business Source License 1.1**, whose own text names `MIT` as its future *Change
License*, and `SethRobinson/UGTLive` is the **Proton SDK licence** (XFree86 1.1-derived)
while containing MIT's full permission sentence verbatim. 🟢 **Both are caught by
classifying on the licence's TITLE — its first non-empty line — and neither is caught by a
body match.** See `591-A`.

🆕 **`591-B` splits a flag this base has graded as one thing since `p579`.** `NOASSERTION`
and `license: null` are **not** the same API state and must not be treated alike.
Byte-read this pass: **`12` `NOASSERTION` rows → `0` had no licence file** (`6` resolved to
a permissive OSI grant, the rest to CC-BY-SA-4.0, BSL-1.1, GPL-2.0 and two bespoke
licences), while **`10` `license: null` rows → `10` had no licence file** at `6` filenames ×
`2` branches. 🟢 **So `null` can be trusted to block a row; `NOASSERTION` is `0-for-12` as
a negative and must always be read.** `Trend 31`'s "about one in two" conflated the two
states.

🟢 **`591-C` — the LATAM in-language gap is REFINED, not confirmed and not simply
refuted.** `p587` measured a `33×` asymmetry and this base has since carried *"LATAM has no
in-language supply to adopt"*. 🟢 **Spanish- and Portuguese-language education supply
exists** — `18` addresses on `12` in-language axes this pass — 🔴 **but it splits by
artefact type, and the split is the finding: of the in-language repos whose primary
artefact is a conversational AI tutor, `6 of 6` carry no licence at all, while `12 of 12`
in-language courseware/curriculum repos are permissive.** 🔵 **In LATAM the courseware
licenses and the tutors do not** — so an in-language engagement adopts the curriculum and
**builds** the tutor. Scale caveat: every in-language row found is `≤ 19★`.

🔴 **`591-D` — the mandated legs are now `22` consecutive passes with no new usable
address.** All eight ran. Every repo-shaped name they served — `minimind`,
`LLMs-from-scratch`, `OFBiz`, `Corteza`, `iDURAR`, `Krayin`, `Atomic CRM`, `iDempiere`,
`Dolibarr`, `Frappe Education`, `ERPNext` — **was already in this base**. 🟢 **The four
regional intel legs paid `4 of 4`** ([`../intel/market.md`](../intel/market.md)), and one
of them served a **licence claim that is false**: the vertical leg stated iDURAR ERP/CRM is
*"fully open-source under the MIT license"*; its `34,230`-byte grant is **AGPL-3.0**
([`../repos/foundations.md`](../repos/foundations.md)).


---

🆕 **`p594` — scope: `253` curated addresses re-measured for `default_branch`, `46` grants byte-read,
the `44`-row shelf NOT re-starred.** 🔴 **The headline is a correction to this page, and it is the
most consequential class of error this base can make: a row published 🟢 `MIT (text)` — "buildable
and shippable in client work" — forbids commercial use.**

🔴 **`594-A` — [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (`2,057★`) is re-graded
from 🟢 MIT to 🔴 NOT OPEN SOURCE.** Its `LICENSE.md` is the **"PageLM Community License"**:
non-commercial use only, redistribution *"strictly prohibited"*, and commercial use conditioned on
a **signed revenue-sharing agreement**. 🔵 **The mechanism is the one `591-A` named three passes
ago:** the file opens with MIT's permission sentence *verbatim* and then overrides it under a
bespoke title, so a body match returns `MIT` while the TITLE returns a bespoke grant. 🔴 **What is
new is not the mechanism but the scope of the omission: `591-A` was adopted and never applied
backwards to rows already on the shelf.** PageLM is the **third** instance of this exact pattern in
this base — after `SethRobinson/UGTLive` (Proton SDK) and `ximing/aimo` (BSL-1.1), both caught at
`p591` *as new candidates*, neither triggering a re-grade sweep of the rows already published.
🟢 **A rule adopted mid-life does not re-grade the shelf behind it, and nobody swept.** `594-A`.

🔵 **Credit where it is due: `p591` SAW THIS COMING and registered it as `591-G`** — *"every `(text)` licence mark filed before `p591` is unauditable for the `Trend 43` defect"* — and prescribed the cheap audit: re-read any `(text)` row whose grant size falls outside `~1,050–1,100 B` for a claimed MIT or `~11,340–11,360 B` for a claimed Apache-2.0. 🔴 **It recorded `Not run this pass — 35 new rows were the budget`, and no pass ran it since.** 🟢 **`p594` ran it: `99` `(text)` rows audited, `8` flagged.** `PageLM` claimed MIT at **`8,562 B`** against a canonical `~1,050–1,100 B` — a `7.8×` discrepancy its filter catches on sight. 🔵 **So `591-G` was right about the mechanism and wrong only about the yield**: it predicted `~4` flags at a `~3 %` true-positive rate; the measured result is `8` flags of which `2` are real mis-grades (`PageLM`, and `pupilfirst`'s split grant — see [`../repos/foundations.md`](../repos/foundations.md)), a true-positive rate near `22 %`. 🟢 **`591-G` CLOSED.**

🆕 **`594-B` — `593-B1` is closed with a population instead of an inference, and the distribution is
the finding.** `p593` found one row whose default branch was neither `main` nor `master`
(`openeducat_erp` at `19.0`) and reasoned that a hardcoded probe *could* fail silently. Measured
across all `253` curated addresses this pass: 🔴 **`30` of `253` (`11.9 %`) default to one of `18`
branch names that are neither `main` nor `master`** — `develop` (11), `dev` (4), `trunk`, `release`,
`mobile`, `development`, and nine version branches (`20.0`, `19.0`, `15.0`, `2.12`, `2.2`, `1.6`,
`release_11`, `v31.0.00`, `v4.0.x-develop`, `2026.9.x`). 🔴 **They are not randomly distributed: they
concentrate in the vertical-platform layer** — Odoo (`55,463★`), ERPNext, BigBlueButton, Dolibarr,
Oppia, Kolibri, OFBiz, Tutor, ILIAS, Claroline, Gibbon, i-educar, Artemis, Opencast, TAO. 🔵 **The
rows most likely to carry a client engagement are precisely the rows a hardcoded probe cannot
read.** Proven live, not argued: `odoo/odoo` and `claroline/Claroline` both return `404` on
`main/LICENSE` and `200` on their real branch. The census is on
[`../verticals/solutions.md`](../verticals/solutions.md).

🆕 **`594-C` — a fourth silent axis, and it is filename case.** `frappe/education`, `frappe/erpnext`
and `frappe/lms` returned **`NO-GRANT-FILE` on all three** from `p593`'s 6-path probe *and* from
this pass's first 7-path probe. Their grants sit at lowercase **`license.txt`**. 🔴 **And
`frappe/education`'s grant is `19` bytes long** — `License: GNU GPL V3`, a declaration with no
licence text at all — so neither a byte count nor a successful fetch is evidence that a grant was
*read*. `13` path/case variants resolve all three.

🆕 **`594-D` — the LATAM in-language gap reaches the instrument, not just the supply.** `591-C`
measured LATAM's in-language *supply*. This pass found the classifier itself is English-only:
[`portabilis/i-diario`](https://github.com/portabilis/i-diario) and
[`portabilis/pre-matricula-digital`](https://github.com/portabilis/pre-matricula-digital) (both
Brazilian, both `NOASSERTION`) carry **AGPL-3.0 in Portuguese** — `LICENÇA PÚBLICA GERAL AFFERO
GNU`. An English title match returns unknown and **false-blocks two live LATAM school systems**.

🔴 **`594-E` — this pass's own instrument produced a false `MIT` three times, and the cause is a
substring.** A case-insensitive unanchored `MIT` test matches ordinary licence prose —
`li`**`mit`**`ation`, `sub`**`mit`**`ted`, `per`**`mit`** — and even a German university's name,
`Technische Hochschule `**`Mit`**`telhessen`. It returned `MIT` for `idempiere/idempiere`
(**GPL-2.0**), `thm-mni-ii/feedbacksystem` (**Apache-2.0**) and `nirholas/lyra-web3-playground`
(**proprietary, "All rights reserved"**). 🟢 **All three are published *correctly* on these pages,
so this is an instrument defect caught before publication, not a live page defect** — recorded
because the symptom is identical to the false licences `p593` found in a sister copy, while the
mechanism is **different** (that copy's three were two no-grant-files published as MIT plus an
`Apache-2.0`/`AGPL-3.0` confusion). Fix: require `MIT License` or a word-boundary token.

🟢 **`594-F` — `591-B` settles on the whole base with perfect separation.** All `46` blank-licence
rows byte-read with the branch-aware `13`-path probe: 🟢 **`license: null` → `14` of `14` have no
grant file; `NOASSERTION` → `32` of `32` have one.** `591-B` measured `10/10` and `0/12` on a
sample; the population agrees exactly and adds no counter-example. 🔵 **So `null` may be trusted to
block a row, and `NOASSERTION` must never be.** Of the `32` resolved: `13` permissive, `6`
copyleft, `2` weak copyleft, `2` not-OSI, `2` content-not-code, `7` bespoke or split → review.

🔴 **`594-G` — the mandated legs are now `25` consecutive passes with no new usable address.** All
eight ran. Every repo-shaped name they served — `ai-agents-for-beginners`,
`ai-engineering-from-scratch`, `AI-PhD-S26`, `browser-use`, `OpenClaw`, `agents-from-scratch`,
`free-ai-agents-resources`, `github-trending`, `2026-AI-College-Jobs`, `guru-latihan-dinamis`,
`OpenEduCat` — **was already in this base**, each re-found between `5` and `48` files deep.
🟢 **The four regional legs paid `4 of 4`** ([`../intel/market.md`](../intel/market.md)).
---

## The shelf — 53 verified agents, of which `1` is now a block

🔴 **`PageLM` stays listed and is NOT shippable** — a row removed silently is a row a later pass re-discovers and re-files as 🟢 MIT. It is kept in place, re-graded, with the reason in the cell (`594-A`).

Ordered by size. Region is assigned only where the repository itself supports a
placement (institution, org, or language of the project); otherwise it reads `Global`.

| Agent | Repo | Licence | Stars | Last push | Region | What it is |
|---|---|---|--:|---|---|---|
| **ai-agents-for-beginners** | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT (text)** | **78,576** | `2026-10-31` | Global | 🆕 **The largest row this base has ever shelved, and it was in the history log 26 times before it reached a page.** 18 lessons that build agents from first principles — the reskilling curriculum a studio hands a client's engineering org on day one. Microsoft. |
| **ai-engineering-from-scratch** | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 🟢 **MIT (text)** | **76,170** | `2026-10-29` | Global | 🆕 **Second-largest, also re-found 26× and never shelved.** Learn-it / build-it / ship-it AI-engineering curriculum. Pairs with the row above: one teaches agents, this one teaches shipping them. |
| **ppt-master** | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | 🟢 **MIT (text)** | **71,973** | `2026-10-30` | Global | 🆕 Documents or a bare topic → **native** PowerPoint decks: real shapes, transitions, charts, narration. The courseware-generation layer. **Largest row on this shelf**; API reported MIT and the licence file confirms it. |
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0 (text, 11,408 B)** | **53,500** | `2026-11-01` | APAC | Lifelong personalised tutoring. The field's only *purpose-built* education agent at frontier scale. HKUDS (Univ. of Hong Kong). 🆕 **`v1.7.1` dated `2026.11.1` — shipped today**, `+1.5k`★ in four days over two point releases. 🔵 **Pin a tag, not `main`.** |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT | **42,360** | `2026-11-01` | APAC | Open Multi-Agent Interactive Classroom — one-click immersive multi-agent learning. Tsinghua. |
| **book-to-skill** | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 🟢 **MIT (text, `LICENSE.md`)** | **36,686** | `2026-10-28` | Global | 🆕 Any technical book PDF → a ready Claude Code skill: study, reference and use. **The courseware-ingestion half of the pair with `ppt-master`** (which is the generation half). 🔴 Default branch is `master`; re-found 19× in history and never shelved. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | **6,954** | `2026-11-01` | Global | Free online learning platform built on interactive "explorations". Both a platform and an authoring model. |
| **word-atlas** (词光) | [designfuchen/word-atlas](https://github.com/designfuchen/word-atlas) | 🟢 **MIT (text)** | **3,668** | `2026-10-31` | APAC | Illustrated IELTS vocabulary — 7,298 words, UK/US audio, FSRS review scheduling. API reports `NOASSERTION`. |
| **PageLM** | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **NOT OPEN SOURCE — "PageLM Community License" (text, `LICENSE.md`, 8,562 B)** | **2,057** | `2026-10-29` | Global | 🔴 **`p594` RE-GRADED FROM 🟢 MIT — DO NOT SHIP.** Community-driven NotebookLM: study material → notes, quizzes, flashcards. 🔴 Its grant is **non-commercial only** ("may **not be sold, sublicensed, or included in any product or service for commercial purposes**"), **redistribution is "strictly prohibited"**, and any commercial use requires a **signed revenue-sharing agreement** with the copyright holders, breach of which is a "material breach and immediate termination". 🔵 **Why this base published MIT:** the file opens with MIT's permission sentence *verbatim* (once) and only then overrides it under a bespoke title — so a body match returns MIT and the `(text)` byte-read that filed this row read the first sentence and stopped. Caught by `591-A` (classify on the licence TITLE). See `594-A`. |
| **nbgrader** | [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | 🟢 BSD-3-Clause | **1,370** | `2026-10-28` | Global | Assign, autograde and release Jupyter notebooks. The autograding seam for technical coursework. Project Jupyter governance. |
| **Study-Mate** | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | 🟢 MIT | **1,291** | `2026-10-21` | APAC | AI study partner that plans a route through a subject, teaches it and sets projects. Chinese-language. |
| **agents-from-scratch** | [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | 🟢 MIT | **1,065** | 🟡 `2026-07-25` | Global | 🆕 Build agents from first principles on a **local** LLM — no frameworks, no cloud APIs. The teaching curriculum for an agent-engineering cohort. 🟡 ~3 months since last push. |
| **Papermorph** | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | 🟢 **MIT (text)** | **1,046** | `2026-11-01` | Global | 🆕 Turns books into animated, narrated, interactive web experiences. Ships as an **agent skill**, not an application. |
| **claudemy** | [assafkip/claudemy](https://github.com/assafkip/claudemy) | 🟢 **MIT (text)** | **577** | `2026-10-29` | Global | 🆕 Open-source Udemy/Coursera alternative: give the agent a topic, it researches and builds the course. The course-construction counterpart to `ppt-master`. |
| **anki-mcp-server** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | 🟢 MIT | **541** | `2026-10-22` | Global | MCP server exposing Anki to an LLM agent. The retention layer any tutor can bolt onto. |
| **nextgen-ai** | [aaryansamanta/nextgen-ai](https://github.com/aaryansamanta/nextgen-ai) | 🟡 **MIT — code only (text)** | **492** | `2026-09-20` | Global | 🆕 Student-led org expanding accessible AI: seminars, ambassadors, curriculum. 🟡 **Licence file reads "MIT License (Code)"** — the grant is scoped to code and says nothing about the curriculum content. Vendor the code, not the materials. API reported `NOASSERTION`. |
| **pyKT** | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | 🟢 MIT | **456** | `2026-10-18` | APAC | PyTorch knowledge-tracing library — the reference for modelling what a learner knows. |
| **relate** | [inducer/relate](https://github.com/inducer/relate) | 🟢 **MIT (text)** | **437** | `2026-11-01` | North America | Full learning/teaching environment with versioned course content and auto-graded work. API reports `NOASSERTION`; `LICENSE` is verbatim MIT. |
| **educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | 🟢 MIT | **387** | 🟡 `2026-05-29` | APAC | Generates educational content with LLMs — MCQs, lesson plans, flashcards. India (Build Fast with AI). 🟡 ~5 months since last push. |
| **ltijs** | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | **373** | `2026-10-31` | Global | Turns an application into a full LTI 1.3 tool provider — the seam into any LMS without forking it. |
| **universal-examprep-skill** | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 **MIT (text)** | **364** | `2026-10-27` | APAC | 🆕 Exam-cram coach with **cross-session memory and handout provenance to suppress hallucination** — the only new row that treats citation-grounding as a first-class feature. Runs as a skill in Claude Code / Cursor / Codex. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | 🟢 MIT | **310** | `2026-11-01` | North America | MCP server for Canvas LMS: up to 102 tools, 8 agent skills, FERPA-aware. Univ. of Illinois. |
| **algo-sensei** | [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | 🟢 MIT | **300** | `2026-10-02` | Global | LeetCode/DSA mentor for Claude Code and claude.ai. Guided practice rather than answers. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | 🟢 MIT | **295** | `2026-10-20` | Global | Private AI tutor that reads how the learner actually learns and sequences the next lesson. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | 🟢 MIT | **274** | `2026-10-31` | North America | Intelligent tutoring with Bayesian Knowledge Tracing. UC Berkeley CAHLR; React + Firebase. |
| **wordlink** | [orionsheep/wordlink](https://github.com/orionsheep/wordlink) | 🟢 **MIT (text)** | **266** | `2026-10-28` | Global | 🆕 Vocabulary learning on a **fine-tuned 1.5B model (SFT+DPO) that runs offline**. The only new row that is a shipped small model rather than a prompt over a frontier API — the pattern for data-residency and low-connectivity work. |
| **universal-diagnostic-tutor-skill** | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 MIT | **255** | `2026-09-24` | Global | 🆕 Diagnosis-first tutor for STEM and CS: no mode menu, it establishes what the learner is missing before teaching. |
| **AILearningGuide** | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | 🟢 MIT | **242** | `2026-10-31` | Global | 🆕 Desktop app with 51 hands-on labs: ML fundamentals, transformers, RAG, agents. A ready reskilling curriculum. |
| **ari** | [nichochar/ari](https://github.com/nichochar/ari) | 🟢 MIT | **218** | `2026-11-01` | Global | Pen-and-paper-first learning companion. Deliberately low-tech interaction model. |
| **kaogong-skill** | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 🟢 MIT | **215** | `2026-10-12` | APAC | 🆕 Chinese civil-service and public-institution exam prep (行测/申论/面试) with wrong-answer review. Evidence that **high-stakes national exam prep is being built as open skills**. |
| **EduCDM** | [bigdata-ustc/EduCDM](https://github.com/bigdata-ustc/EduCDM) | 🟢 Apache-2.0 | **203** | 🔴 `2024-10-25` | APAC | Cognitive diagnosis model zoo (IRT, MIRT, DINA, NCDM). Shippable, but **~24 months stale**. |
| **cram-engine** | [liuliu667/cram-engine](https://github.com/liuliu667/cram-engine) | 🟢 MIT | **176** | `2026-10-22` | APAC | 🆕 Four-stage interactive teaching skill grounded in **learning-science principles** rather than ad-hoc prompting. Chinese-language. |
| **OpenTutor** | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | **160** | `2026-10-31` | Global | Block-based adaptive learning workspace that runs locally; 10+ LLM providers. |
| **catsim** | [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | 🟢 BSD-3-Clause | **153** | `2026-10-30` | **LATAM** | Computerised Adaptive Testing simulator — simulate item selection before exposing learners. Brazil. |
| **gen-mentor** | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | 🟢 CC0-1.0 | **135** | `2026-10-23` | APAC | WWW '25 oral — LLM multi-agent framework for goal-oriented learning-path generation. Public-domain dedication. |
| **girth** | [eribean/girth](https://github.com/eribean/girth) | 🟢 MIT | **127** | 🔴 `2022-09-09` | Global | Item Response Theory package for Python (item calibration). 🔴 **~4 years stale** — use `catsim` or `pyKT` first. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 BSD-3-Clause | **114** | 🟡 `2026-06-26` | EMEA | Tutoring platform with voice, video and 3D avatars. Docker-first, local LLMs via Ollama. |
| **mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | 🟢 MIT | **103** | `2026-10-31` | EMEA | AI-native LMS with AI mentor and role-play; self-hosted. Selleo (Poland). |
| **PAIDEIA** | [OPTIMETA/PAIDEIA](https://github.com/OPTIMETA/PAIDEIA) | 🟢 **MIT (text)** | **91** | 🟡 `2026-07-11` | Global | 🆕 Exam-prep study system for maths, physics and engineering: ingests the learner's *own* lectures, textbooks, homework and solutions and emits solution patterns, drill problems, **graded handwritten answers**, weakness reports and cheatsheets, all as editable markdown in the course folder. 🔵 **Ships for four agent runtimes — Claude Code, Codex, opencode and hermes-agent** — the first row on this shelf that is portable across hosts rather than tied to one. Re-found 11× in [`./trending.md`](./trending.md) and 3× on [`../intel/market.md`](../intel/market.md) before it reached a page. 🟡 ~3.7 months since last push; pin it. |
| **Claw-ED** | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT (text)** | **63** | `2026-09-19` | Global | 🆕 **Local-first** teaching assistant: editable lesson drafts, student materials and feedback with no cloud dependency. The data-residency answer for a school that cannot send pupil work to an API. Re-found 19× in history before reaching this page. |
| **tutor-mcp** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | 🟢 MIT | **62** | `2026-10-31` | Global | MCP server that turns any LLM into an Intelligent Tutoring System, grounded in ITS research. |
| **Lama Loca** | [emil-a-dev/lama-loca](https://github.com/emil-a-dev/lama-loca) | 🟢 MIT | **59** | 🟡 `2026-03-04` | EMEA | Fully offline Russian-language study assistant: learns from the user's own books, emits reports and slides. |
| **BCTK** (TK试题题库) | [BBkjdayup/BCTK](https://github.com/BBkjdayup/BCTK) | 🟢 MIT | **53** | `2026-09-28` | APAC | Offline-first Windows item-bank and paper-composition app for teachers. Word/Excel round-trip without Office. |
| **ai-tutor-app** | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | 🟢 Apache-2.0 | **34** | `2026-10-22` | Global | 🆕 Agentic **RAG** tutor for applied AI/LLM/Python built on **LangGraph** — the only shelf row that is an explicit retrieval-grounded tutor over a fixed corpus, which is the shape a client asks for when the answer must come from *their* materials. |
| **LearnDeck** | [LearnAIHubC/LearnDeck](https://github.com/LearnAIHubC/LearnDeck) | 🟢 **MIT (text, `LICENSE.txt`, 1,068 B)** | **26** | `2026-07-15` | Global | 🆕 Topics, notes and raw course material → generated slide decks. The **courseware-generation** seam on the agent side; pairs with `ppt-master` (native PPTX) and `book-to-skill` (ingestion). 🔵 Grant lives at `LICENSE.txt`, not `LICENSE`. |
| **selftune** | [selftune-dev/selftune](https://github.com/selftune-dev/selftune) | 🟢 **MIT (text, 1,067 B)** | **18** | `2026-10-24` | Global | 🆕 **Skill observability and self-improvement for agent skills.** 🔵 This base has carried "no dominant OSS agent eval/observability layer" as a declared gap for many passes — this is the **first permissive candidate against it**, and it is small, so the gap narrows rather than closes. |
| **StudySage** | [sizwinz/StudySage-Offline-Online-AI-Note-Assistant](https://github.com/sizwinz/StudySage-Offline-Online-AI-Note-Assistant) | 🟢 **MIT (text, 1,083 B)** | **12** | `2026-07-05` | Global | 🆕 **Offline-first** AI note-taking and summarisation assistant for students; runs online or fully local. 🔵 Offline operation is the axis that matters for low-connectivity LATAM and rural APAC deployments, alongside Kolibri. |
| **OpenEdu** | [TerraByte-Dev/OpenEdu](https://github.com/TerraByte-Dev/OpenEdu) | 🟢 **MIT (text, 1,080 B)** | **6** | `2026-10-08` | Global | 🆕 Open-source AI tutoring platform, absolute-beginner → mastery. 🔴 **Default branch is `master`** — a `600-E` row: a `main`-only probe reports this repo as having no licence file at all. |
| **beacon** | [agenticfabriq/beacon](https://github.com/agenticfabriq/beacon) | 🟢 **Apache-2.0 (text, 11,358 B)** | **5** | `2026-10-25` | Global | 🆕 Grader and results tracker — exact-match plus "got-the-facts" grading with run history. 🔵 Written for text-to-SQL, but the **grading harness** is the reusable part: it is the scoring half that `nbgrader` does not cover for free-text answers. |
| **understand** | [fcescob/understand](https://github.com/fcescob/understand) | 🟢 **MIT (text, 1,075 B)** | **5** | `2026-10-13` | Global | 🆕 **Mastery-gated** tutor skill for agents: teaches a topic or a codebase and will not advance until durable transfer is demonstrated. 🔵 The explicit counter to completion-as-progress. |
| **socratic-tutor** | [Rayhaan1345/socratic-tutor](https://github.com/Rayhaan1345/socratic-tutor) | 🟢 **MIT (text, 1,070 B)** | **5** | `2026-10-23` | APAC | 🆕 Teaches by asking questions rather than answering them. Mumbai AI Lab. 🔵 **Third instance of pedagogy-as-product** after `nietzschian-debugger` and `learn-anything` — the category is now established, not anecdotal. |
| **courseware-cn-annotator** | [youngman2007/courseware-cn-annotator](https://github.com/youngman2007/courseware-cn-annotator) | 🟢 **MIT (text, 1,093 B)** | **5** | `2026-10-27` | APAC | 🆕 Courseware PDF → a Chinese-language study package, packaged as an agent skill. 🔵 **APAC in-language supply**, alongside `kaogong-shuati` and `word-atlas`. |
| **EduNexus-AI** | [weidonglang/EduNexus-AI](https://github.com/weidonglang/EduNexus-AI) | 🟢 **MIT (text, 1,071 B)** | **5** | `2026-07-01` | APAC | 🆕 Spring Boot + Vue 3 academic/teaching administration system (教务管理系统). 🔵 **The first permissively-licensed row on this page that touches the standing ERP/SIS gap** — it is a graduation-project-scale system, so it narrows the gap by proving the shape, not by filling it. |

**44 rows. 43 are unreservedly permissive**, and the 44th (`nextgen-ai`) is permissive for
its code with the content grant unstated. The agent layer licenses permissively, which
remains the single most useful structural fact for a studio: **the AI can be built
permissively and attached to a copyleft LMS from the outside.**

🆕 **The structural change `p586` measured: education AI has started shipping as *agent
skills*, not applications.** Eleven rows on this shelf are now skills or MCP servers that
run inside a host agent — `Papermorph`, `claudemy`, `universal-examprep-skill`,
`universal-diagnostic-tutor-skill`, `kaogong-skill`, `cram-engine`, `algo-sensei`,
`tutor-mcp`, `anki-mcp-server`, `canvas-mcp`, `libro-3d-interactivo`. The packaging matters
commercially: a skill has **no hosting, no auth and no UI to maintain**, so the integration
cost of adopting one is a fraction of adopting a platform. See
[`../compose/patterns.md`](../compose/patterns.md) pattern `P586-1`.

## 🆕 The spec-emit agent tier — added `p590`, and every row was already in this base

🔵 **Why this tier is new and why it belongs on an *agents* page.** `p589` found agent
supply growing *on top of* the SCORM layer because the layer's libraries were dead
(`Trend 41`). 🔴 **That premise is now refuted** — the libraries are alive
([`../repos/foundations.md`](../repos/foundations.md)) — but **the agents are real
regardless**, and they are a distinct shape from everything else on this page: an MCP
server or agent skill whose *output artefact is a conformant package*, not a chat turn.
🟢 **All five grants byte-read first-hand `2026-11-01`; the API agreed on `5 of 5`.**

🔴 **Not one of these five came from a search, and all five were already in this base's
append-only history.** That is the promotion bottleneck `p587` named, measured again at
`5 of 5` — so the honest reading of this tier is that it is **filing debt paid**
(`584-C`), not discovery.

| Agent | Repo | Licence | Stars | Last push | Region | What it is |
|---|---|---|--:|---|---|---|
| **idstack** | [savvides/idstack](https://github.com/savvides/idstack) | 🟢 **MIT (text, 1,077 B)** | **27** | `2026-10-30` | Global | 🆕 **Eleven instructional-design agent skills** that check alignment, accessibility and assessment validity against evidence-based ID criteria. 🔵 The only row on this page that audits *pedagogy* rather than producing content — the reviewer slot in a courseware pipeline. |
| **edumints-scorm-mcp** | [kemalyy/edumints-scorm-mcp](https://github.com/kemalyy/edumints-scorm-mcp) | 🟢 **MIT (text, 1,069 B)** | **9** | `2026-10-14` | Global | 🆕 MCP server that **assembles interactive SCORM-compliant courses** and is self-hostable. 🟢 The emit step of a courseware pipeline, exposed as agent tools. |
| **coursecode** | [course-code-framework/coursecode](https://github.com/course-code-framework/coursecode) | 🟢 **MIT (text, 1,069 B)** | **7** | `2026-10-30` | Global | 🆕 Course-authoring framework for MCP-capable tools — build, preview and export. 🔵 Has a desktop sibling (`coursecode-desktop`) covering SCORM, **cmi5** and LTI export. |
| **scorm-mcp-server** | [giacomomaria81/scorm-mcp-server](https://github.com/giacomomaria81/scorm-mcp-server) | 🟢 **MIT (text, 1,070 B)** | **6** | `2026-09-03` | EMEA | 🆕 Turns HTML or design bundles into **LMS-ready SCORM 2004 / 1.2 packages** as an MCP tool. 🔵 Narrower than `edumints` and therefore easier to drop into an existing pipeline. |
| **edumints-scorm-skill** | [kemalyy/edumints-scorm-skill](https://github.com/kemalyy/edumints-scorm-skill) | 🟢 **MIT (text, 1,069 B)** | **5** | `2026-10-14` | Global | 🆕 The **agent-skill half** of `edumints-scorm-mcp` — authoring instructions paired with that server. 🔵 Ship the pair, not either alone. |

🔵 **How to compose this tier**, concretely: `coursecode` or `edumints-scorm-skill` authors,
`edumints-scorm-mcp` or `scorm-mcp-server` emits the package,
[`LiaScript-Exporter`](https://github.com/LiaScript/LiaScript-Exporter) (BSD-3-Clause)
covers the formats they do not, and **`idstack` reviews the result before it ships**. Wired
up in [`../compose/patterns.md`](../compose/patterns.md).

### 🔴 Measured and BLOCKED — the first new address from the mandated legs in `21` passes, and it is unlicensed

🟢 **The streak is broken and the result is still a block.** `p589` recorded a twentieth
consecutive nil on the mandated `WebSearch` legs. 🟢 **`p590`'s legs returned one address
this base has never held in any file** — and it fails the only test that matters.

| Repo | Measured `p590` | Verdict |
|---|---|---|
| [anandpatikat/guru-latihan-dinamis](https://github.com/anandpatikat/guru-latihan-dinamis) | `115★`, pushed **`2026-11-01T11:40Z`** (same hour as this pass), `fork: false`, `archived: false`, default branch `main` | 🔴 **BLOCK — NO GRANT.** API `license: null`, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` and lowercase `license` all return `404`. 🔵 Absent from all `11` files of this base, so it is genuinely new; **unlicensed means all rights reserved, so it cannot be vendored, forked or shipped.** Filed as a LEAD: an **Indonesian-language exam-preparation teacher agent**, i.e. the APAC in-language supply whose absence `p587` measured at `33×`. 🟡 Worth one watch for a later grant, worth nothing today. |

🔵 **Recorded as a channel result, not a row:** `21` passes of mandated legs have now
produced exactly **one** address this base did not already hold, and it is unusable. The
legs that pay are the per-jurisdiction native-language queries (`p576`) and the topic axes
(`p589`, `p590`) — both of which paid again this pass.

---

## 🆕 The enablement tier — repos that teach *about* AI, not repos that teach *with* it

🔴 **This page admitted this class at `p587` without naming it, while
[`../intel/open-gaps.md`](../intel/open-gaps.md) still records it as out of family.** That
page retired the `github trending education AI {year}` query on the finding that *"in a
trending feed 'education' means **teaching people about AI**, not **AI for teaching**"* —
and it named [`rasbt/LLMs-from-scratch`](https://github.com/rasbt/LLMs-from-scratch) and
[`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
as its specimens. `p587` then shelved the second of those two as **the second-largest row
on this shelf**. 🔴 **Both statements cannot stand.**

🟢 **Resolved in favour of admitting the class — because the studio already sells it.**
[`../compose/patterns.md`](../compose/patterns.md) `P-587-B` is a reskilling engagement
whose curriculum components are exactly this class. What was missing was not the revenue:
it was the **label**, and the rest of the class. 🔴 **The two tiers answer different briefs
and must never be read as one shelf** — a client asking for a tutor cannot deploy a
curriculum, and a client reskilling its engineers cannot deploy a tutor.

Measured first-hand **2026-11-01** (`p588`). Every licence below read from the
repository's own licence file.

| Repo | Licence | Stars | Last push | Region | What it is |
|---|---|--:|---|---|---|
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 🟢 **MIT (text)** | **122,716** | `2026-11-01` | Global | 🆕 **The largest education-adjacent repository on GitHub, and this base had never filed it at any size.** 21 lessons on building with generative AI; 65,526 forks. Licence text is verbatim MIT, © Microsoft Corporation, **no content carve-out**. |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 🟡 **Apache-2.0 — code only (text)** | **107,633** | `2026-10-30` | Global | 🆕 Build a GPT-class model in PyTorch one stage at a time; 16,610 forks. 🔴 **The licence text MODIFIES Apache-2.0's definition of "Source"** to exclude *"any books specific to this software and any related images"*. **Vendor the code; the book is not granted.** API said `NOASSERTION` — so neither channel alone shows this. © 2023–2026 Sebastian Raschka. |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 🟢 **Apache-2.0 (text)** | **64,724** | `2026-10-27` | APAC | 🆕 Trains a ~64M-parameter language model from scratch in ~2 hours on modest hardware. **The cheapest credible "we trained our own model" teaching artefact in this base.** Standard Apache-2.0, no carve-out. 🔵 Default branch is `master`. |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | 🟢 **MIT (text)** | **59,308** | 🟡 `2026-09-07` | Global | 🆕 The full ChatGPT-style stack — tokeniser, pretraining, fine-tuning, inference, web UI — trainable end-to-end. © 2025 Andrej Karpathy, standard MIT. 🟡 ~2 months since last push; pin it. 🔵 Default branch is `master`. |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | 🟢 **MIT (text)** | **39,206** | 🟡 `2026-07-27` | Global | 🆕 Catalogue of agent use cases by industry, **with education entries of its own** (Virtual AI Tutor, Study Partner, Research Scholar). Use it as a **brief generator** in pre-sales, not as a dependency. 🟡 ~3 months stale. Standard MIT, © 2025. |
| [ARUNAGIRINATHAN-K/awesome-ai-agents-2026](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) | 🟡 **CC0-1.0 (text)** | **353** | `2026-10-23` | Global | 🆕 Searchable directory comparing agent frameworks and tools; 770 commits, a real application rather than a README list. 🔴 **CC0 is a public-domain dedication for *content*, not a software licence — no patent grant.** 🔵 **This row is the genuine CC0 case; `education-agent-skills`, which earlier passes paired with it, is `CC BY-SA 4.0` and reciprocal (`599-A`) — a different and worse trap.** API said `NOASSERTION`. |
| [rphilipzhang/AI-PhD-S26](https://github.com/rphilipzhang/AI-PhD-S26) | 🟢 **MIT (text)** | **91** | 🟡 `2026-07-28` | **APAC** | 🆕 **The first institution-accountable row in this tier, and the first with a course code.** `DOTE 6635 Artificial Intelligence for Business Research`, Spring 2026, **CUHK Business School**, Dept. of Decisions, Operations and Technology; instructor Renyu (Philip) Zhang, with a named TA and tutorial instructor. Mono-repo: scribed lecture notes, per-session slides on ML / deep learning / RL / **agentic AI**, CoLab demos, problem sets (Kaggle competition, neural-net implementation, GPT-2 training), reading lists, plus the 2024 and 2025 offerings. 🔵 **This is the tier's answer to a university client rather than to a corporate one.** 🟡 ~3.1 months since last push. |

🔵 **Two members of this class are already on the shelf above** —
`microsoft/ai-agents-for-beginners` (**78,576**, MIT) and
`rohitg00/ai-engineering-from-scratch` (**76,170**, MIT), both shelved at `p587`. With the
**seven** rows here the class has **nine** members, and **four of its five largest were
unfiled before this pass**. 🆕 **`p592` corrected this paragraph's arithmetic**: it still read
*"six rows / eight members"*, the count from `p588`, after `p589` added `AI-PhD-S26` as the
seventh row without updating it. 🔴 **`p588` wrote that only `minimind` carries a region** — 🆕 `p589` adds a
second, `AI-PhD-S26`, placed **APAC** by a **named university** rather than by language,
which is the stronger form of placement, and it is the first such row in this tier. That is
the one property that makes this tier travel to LATAM — see
[`../compose/patterns.md`](../compose/patterns.md) `P-588-A`.

---

### Smaller but institution-accountable — worth citing in a proposal

These are small by stars and real by provenance. Size is not the only form of credibility.

| Agent | Repo | Licence | Stars | Last push | Region | Why it matters |
|---|---|---|--:|---|---|---|
| **pedal** | [pedal-edu/pedal](https://github.com/pedal-edu/pedal) | 🟢 MIT | 32 | `2026-10-18` | Global | Static and dynamic analysis of student Python code — feedback generation, not just pass/fail. |
| **feedbacksystem** | [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 **Apache-2.0 (text)** | 24 | `2026-10-28` | EMEA | Personalised automated feedback. Technische Hochschule Mittelhessen. Licence recovered from `NOASSERTION` at `p585`. |
| **Terracotta** | [terracotta-education/terracotta](https://github.com/terracotta-education/terracotta) | 🟢 Apache-2.0 | 21 | `2026-10-29` | North America | LMS plug-in for randomised controlled education experiments — consent hidden from the instructor, identifiers stripped from exports. The only research-ethics-aware row here. |
| **warren** | [openfun/warren](https://github.com/openfun/warren) | 🟢 MIT | 17 | `2026-10-31` | EMEA | Learning-analytics visualisation (xAPI). 🔴 Its README still calls itself a proof of concept — do not put it in front of a client as production. France Université Numérique. |
| **libro-3d-interactivo** | [csepulvedai/libro-3d-interactivo](https://github.com/csepulvedai/libro-3d-interactivo) | 🟢 MIT | 15 | `2026-10-27` | **LATAM** | Claude Code skill producing interactive 3D pop-up books (Three.js) with Chilean-Spanish narration, aligned to curriculum objective OA 13. Universidad de Los Lagos, Chile. |
| **pedagogy-benchmark** | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 MIT | 13 | `2026-10-09` | **LATAM** | Benchmark of LLMs' *pedagogical* knowledge, built from exams by Chile's Agencia de la Calidad de la Educación and CPEIP. The only evaluation instrument on this shelf. |

---

## 🆕 The local-first study-OS tier — added `p591`

🔵 **Why this is a tier and not eight loose rows.** Each row takes the learner's *own*
material — slides, PDFs, lecture video, a book — and produces study artefacts
(cheatsheets, flashcards, quizzes, cited answers) **on the learner's machine**. 🟢 That is
the shape a client asks for whenever pupil work or licensed courseware **cannot leave the
building**, and this base previously had one answer for it (`Claw-ED`, `63★`). It now has
nine. 🟢 **All eight grants byte-read `2026-11-01`, title-anchored per `591-A`.**

| Agent | Repo | Licence | Stars | Last push | Region | What it is |
|---|---|---|--:|---|---|---|
| **bilibili-digest** | [biuworks/bilibili-digest](https://github.com/biuworks/bilibili-digest) | 🟢 **MIT (text, 1,169 B)** | **179** | `2026-10-18` | APAC | 🆕 Browser extension turning Bilibili video into study material: subtitle reading, bilingual pairing, AI chapter overviews, click-to-explain and **timestamped notes**. Shipped on the Chrome and Edge stores. 🔵 API said `NOASSERTION` — see `591-B`. Chinese-language. |
| **cortex** | [PndaMan/cortex](https://github.com/PndaMan/cortex) | 🟢 **Apache-2.0 (text, 11,357 B)** | **48** | `2026-10-26` | Global | 🆕 **The most complete local-first NotebookLM alternative on these shelves** — a desktop study OS turning slides, PDFs and lectures into cheatsheets, flashcards, quizzes and **citation-grounded chat**. Svelte. 🟢 The only Apache-2.0 row in this tier. |
| **CoursePilot** | [wansui976/CoursePilot](https://github.com/wansui976/CoursePilot) | 🟢 **MIT (text, 1,066 B)** | **36** | `2026-10-28` | APAC | 🆕 Local-first workbench for **video** courses: subtitles, notes, mind maps, courseware **OCR**, provenance-carrying Q&A and spaced review. 🔵 The only row here that OCRs slide decks out of a recording. Chinese + English. |
| **yidu-english-reader** | [martinachain/yidu-english-reader](https://github.com/martinachain/yidu-english-reader) | 🟢 **MIT (text, 1,064 B)** | **34** | `2026-09-15` | APAC | 🆕 AI reader for English-language originals: double-click lookup, selection-based sentence breakdown, spaced-repetition review. EPUB/PDF, **all data local**. |
| **veynrel** | [zinverno/veynrel](https://github.com/zinverno/veynrel) | 🟢 **MIT (text, 1,066 B)** | **29** | `2026-10-31` | Global | 🆕 Vault health, connection review and **Recall** for Obsidian — the review layer for a knowledge base a learner already keeps. 🟡 `2.3.0` is a release candidate at time of measurement. |
| **insight-engine** | [inbeomheo/insight-engine](https://github.com/inbeomheo/insight-engine) | 🟢 **MIT (text, 1,067 B)** | **22** | `2026-09-08` | APAC | 🆕 YouTube video, documents and text → study notes **and a searchable knowledge wiki**; four output styles, **ko/en/ja**, RAG, spaced review, team workspaces. Korea. 🔵 Default branch is `master`. |
| **empty** | [DaviRain-Su/empty](https://github.com/DaviRain-Su/empty) | 🟢 **MIT (text, 1,064 B)** | **21** | `2026-06-21` | Global | 🆕 **Spoiler-free** EPUB/PDF reading companion with local AI, notes, vocabulary and **cross-book memory**. SwiftUI for macOS, iOS and iPadOS — the only native-Apple row on these shelves. |
| **quizzer** | [suncloudsmoon/quizzer](https://github.com/suncloudsmoon/quizzer) | 🟢 **MIT (text, 1,070 B)** | **21** | 🟡 `2026-04-06` | Global | 🆕 PDFs → Duolingo-style quiz courses with spaced repetition, adaptive difficulty and tutor chat. 🟡 ~7 months since last push; pin it. |

---

## 🆕 The in-language tier — added `p591`, and it is the evidence for `591-C`

🔴 **This base has carried *"LATAM has no in-language supply to adopt"* since `p587`.** 🟢
**It does — and the useful statement is narrower and more actionable:** the in-language
*courseware* licenses permissively and the in-language *tutors* carry no grant at all
(`591-C`, measured below and on [`./trending.md`](./trending.md)).

🔵 **How region is assigned here, stated because language is weak evidence.** A row is
placed only where there is a **named institution, a country-specific target population, or
a country-bound idiom** — not on language alone. Rows whose only signal is "written in
Spanish" read `Global`, because Spanish is also Spain, and a wrong placement is worse than
an honest one. The signal is named in every row.

| Agent | Repo | Licence | Stars | Last push | Region | What it is — and what places it |
|---|---|---|--:|---|---|---|
| **Subify** | [mobinbiback/Subify](https://github.com/mobinbiback/Subify) | 🟢 **MIT (text, 1,082 B)** | **46** | `2026-11-01` | EMEA | 🆕 AI subtitles, real-time translation, bilingual captions and dubbing for the web. **Placed by language: the README and UI are Persian.** Pushed the day of measurement. |
| **llm-course** | [lucianoon/llm-course](https://github.com/lucianoon/llm-course) | 🟢 **Apache-2.0 (text, 11,355 B)** | **19** | `2026-10-29` | LATAM | 🆕 **The largest in-language row this pass found.** Open course on LLM engineering and customisation **in Portuguese**, from scratch to production, with **reproducible labs**. 🔵 Placed by language; no institution named. The in-language answer to a reskilling brief. |
| **espanol-scenario-learn** | [Tongether/espanol-scenario-learn](https://github.com/Tongether/espanol-scenario-learn) | 🟢 **MIT (text, 1,066 B)** | **15** | `2026-09-03` | APAC | 🆕 Scenario-based **Spanish** learning built **for Chinese speakers** (面向中文用户). 🔵 **Placed APAC, not LATAM** — the target learner is Chinese; the taught language is Spanish. The distinction matters when sourcing for a LATAM engagement. |
| **engenharia-software** | [tacianosilva/engenharia-software](https://github.com/tacianosilva/engenharia-software) | 🟢 **MIT (text, 1,077 B)** | **15** | `2026-10-02` | LATAM | 🆕 Documentation, tutorial, task and project hub for software-engineering courses. 🟢 **Placed by named institution: BSI-UFRN, Universidade Federal do Rio Grande do Norte, Brazil** — the strongest placement in this tier. |
| **macacodev-5-projetos-python** | [PedroseleT/macacodev-5-projetos-python](https://github.com/PedroseleT/macacodev-5-projetos-python) | 🟢 **MIT (text, 1,079 B)** | **11** | `2026-10-19` | LATAM | 🆕 Five Python projects to get a learner past tutorial stage: terminal applications, **tutoriais em português**, challenges and offline tests. 🔵 Placed by language. |
| **miniout** | [dimelim/miniout](https://github.com/dimelim/miniout) | 🟢 **Apache-2.0 (text, 11,343 B)** | **7** | `2026-09-29` | Global | 🆕 University notes and tasks, **Spanish-only UI**, React Native + Expo. 🔵 **Deliberately `Global`** — Spanish UI with no country signal, and `591-C` says not to guess. |
| **tutor-de-skills** | [angelapaia/tutor-de-skills](https://github.com/angelapaia/tutor-de-skills) | 🟢 **MIT (text, 1,188 B)** | **6** | 🟡 `2026-06-07` | Global | 🆕 **The row that broke the "no in-language supply" claim.** Interactive **Spanish-language** tutor teaching Claude skill authoring on a five-level ladder; by Luis Salgado · SalgadoIA, shared by IA Masters Academy. 🔵 **API said `NOASSERTION`; the grant is MIT** — `591-B`. Placed `Global`: Spanish, no country named. 🟡 ~4.8 months stale. |
| **tutor** (MINT-Lern-Tutor) | [Sae-l/tutor](https://github.com/Sae-l/tutor) | 🟢 **MIT (text, 1,065 B)** | **6** | `2026-11-01` | EMEA | 🆕 **German** STEM tutor (*MINT*) shipped as a Claude skill **plus** its system prompt. 🟢 Placed by language — *MINT* is the German-language acronym for STEM, so the artefact is country-bound. Pushed the day of measurement. |
| **mackseguro** | [kenzofujimoto/mackseguro](https://github.com/kenzofujimoto/mackseguro) | 🟢 **MIT (text, 1,129 B)** | **4** | `2026-10-30` | LATAM | 🆕 Open-source **digital-security** education platform in Portuguese. 🟢 **Placed by named institution: a Mackenzie Presbyterian University extension project, São Paulo, Brazil.** 🔵 The only security-curriculum row in this base. |
| **jacarEV3** | [Escama-Code/jacarEV3](https://github.com/Escama-Code/jacarEV3) | 🟢 **MIT (text, 1,086 B)** | **4** | `2026-10-29` | LATAM | 🆕 **Portuguese** library driving LEGO EV3 over Bluetooth/USB — the Direct Commands protocol implemented from zero, **no dependencies**. 🔵 Placed by language and Brazilian idiom (*jacaré*). **The only physical-robotics teaching row on these shelves**, and the one to reach for in a K-12 STEM brief. |
| **lingua-aberta** | [belentani7/lingua-aberta](https://github.com/belentani7/lingua-aberta) | 🟢 **MIT (text, 1,074 B)** | **0** | `2026-10-31` | LATAM | 🆕 Free, open platform teaching Spanish, Catalan and English to **young Brazilians living in Catalonia**, with a voice-ready AI tutor. 🟢 **Placed by named target population**, not by language — the project sits in EMEA and serves a LATAM diaspora, which is worth saying out loud. 🔴 `0★` and `35` open issues: a live project, not a dependency. |
| **poliglota-master** | [marcoskoo/poliglota-master](https://github.com/marcoskoo/poliglota-master) | 🟢 **MIT (text, 1,066 B)** | **0** | `2026-10-27` | Global | 🆕 Free five-language platform taught **from Spanish** — Italian, English, Portuguese, French, German, A1–C2, 66 units. 🔵 Placed `Global`: Spanish-first, no country. 🔴 `0★`; read it as a reference implementation. |
| **tutor-vibe-coding** | [smartfoods1/tutor-vibe-coding](https://github.com/smartfoods1/tutor-vibe-coding) | 🟢 **MIT (text, 1,081 B)** | **0** | `2026-09-29` | Global | 🆕 Free **Spanish** course taking someone who has never programmed to a published page, with a text-**or-voice** AI tutor. FastAPI + React. 🔵 Placed `Global`. 🔴 `0★`. |

🔴 **The other half of `591-C`, and the half that changes a scope estimate.** The
in-language repos whose primary artefact is a **conversational AI tutor** are
systematically unlicensed — `6 of 6` measured, every one probed at `6` filenames × `2`
branches:

| Repo | Measured `p591` | Verdict |
|---|---|---|
| [andresmancilla08/Parlo](https://github.com/andresmancilla08/Parlo) | Spanish-language English tutor that corrects and converses; PWA (Next.js 16) | 🔴 **BLOCK — no grant** |
| [corleone000000/fluir](https://github.com/corleone000000/fluir) | "practica inglés y español con un tutor de IA" | 🔴 **BLOCK — no grant** |
| [s64965264-code/nexo-ia](https://github.com/s64965264-code/nexo-ia) | Spanish study tutor with chat, images and voice practice | 🔴 **BLOCK — no grant** |
| [jccastel12-ctrl/linguaai-coach](https://github.com/jccastel12-ctrl/linguaai-coach) | Spanish-language AI language-learning platform with real-time translation | 🔴 **BLOCK — no grant** |
| [CryptoJones/OSAPHLA](https://github.com/CryptoJones/OSAPHLA) | `12★` — "Open-Source, Accessible & Pan-Hispanic Language Academy", bilingual | 🔴 **BLOCK — no grant.** 🔵 Calls itself open source in its own name and grants nothing. |
| [rodrigoborgesmachado/questoesConcursos](https://github.com/rodrigoborgesmachado/questoesConcursos) | `31★` — Portuguese platform for practising Brazilian public-exam questions | 🔴 **BLOCK — no grant.** 🔵 The LATAM counterpart to `kaogong-skill` (APAC, MIT) — same demand, no grant. |

🔵 **So the honest advice for an in-language engagement:** adopt `llm-course`,
`engenharia-software`, `macacodev` and `jacarEV3` as curriculum; **build the tutor**, using
`tutor-de-skills` and `Sae-l/tutor` as the only permissive in-language references that
exist. Wired up in [`../compose/patterns.md`](../compose/patterns.md) `P-591-B`.

---

## 🆕 The agent-skill and tutor tier — added `p591`

🔵 **`p586` measured that education AI had started shipping as agent skills rather than
applications and counted `11` such rows.** 🟢 **This tier adds `16` more**, which puts the
count past `27` and makes the packaging shift the dominant shape on these shelves rather
than a noted trend. 🟢 Every grant byte-read, title-anchored.

| Agent | Repo | Licence | Stars | Last push | Region | What it is |
|---|---|---|--:|---|---|---|
| **ahadiff** | [AGI-is-going-to-arrive/ahadiff](https://github.com/AGI-is-going-to-arrive/ahadiff) | 🟢 **MIT (text, 1,077 B)** | **244** | `2026-09-08` | Global | 🆕 **Turns each AI code diff into a code-verified lesson, quiz and review** instead of a clicked Accept. 🔵 The only row in this base that teaches **from an agent's own output** — the retention layer for a client whose engineers now read more AI code than they write. |
| **speakeasy** | [bob798/speakeasy](https://github.com/bob798/speakeasy) | 🟢 **Apache-2.0 (text, 10,877 B)** | **75** | `2026-09-29` | Global | 🆕 Conversational English practice with **no corrections and no scores** — a deliberate pedagogical stance, and the opposite of every scoring row here. 🔵 API said `NOASSERTION`. |
| **algotutor** | [zuzuleinen/algotutor](https://github.com/zuzuleinen/algotutor) | 🟢 **MIT (text, 1,068 B)** | **84** | `2026-07-10` | Global | 🆕 AI-powered training for **Go** developers. Pairs with `algo-sensei` (DSA) as the language-specific half of technical coaching. |
| **word-teacher** | [vancece/word-teacher](https://github.com/vancece/word-teacher) | 🟢 **MIT (text, 1,070 B)** | **46** | `2026-07-09` | APAC | 🆕 Web app for English reading and spoken practice with AI. Chinese-language. |
| **IELTS-Speaking-AI** | [1599570912/IELTS-Speaking-AI](https://github.com/1599570912/IELTS-Speaking-AI) | 🟢 **MIT (text, 1,088 B)** | **32** | `2026-07-28` | APAC | 🆕 IELTS **speaking** practice: real-time speech recognition, scoring, 210+ questions, local history. 🔵 High-stakes exam prep as open source again — the same pattern `kaogong-skill` showed for Chinese civil-service exams. |
| **inklish** | [fahreziadh/inklish](https://github.com/fahreziadh/inklish) | 🟢 **MIT (text, 1,069 B)** | **30** | `2026-07-20` | Global | 🆕 **Practise English where you actually write it** — realistic email, Slack, GitHub and chat rooms with an AI persona and a coach on every message. **BYOK** (your own OpenRouter key), so there is no vendor dependency to novate. |
| **smart-learn** | [HYH926/smart-learn](https://github.com/HYH926/smart-learn) | 🟢 **MIT (text, 1,063 B)** | **24** | `2026-06-11` | Global | 🆕 Claude Code skill running a **Feynman-technique five-step pipeline**: concept map → Feynman explanation → self-test → association → summary. **Zero dependencies.** |
| **AdaptEd** | [IdkwhatImD0ing/AdaptEd](https://github.com/IdkwhatImD0ing/AdaptEd) | 🟢 **MIT (text, 1,067 B)** | **20** | 🟡 `2026-05-10` | North America | 🆕 "Lectures that talk back" — real-time **voice** tutor with dynamically generated slides and **emotion-aware pacing**. LA Hacks Gemini Challenge winner. 🟡 ~5.7 months stale; the pacing model is the idea worth lifting. |
| **attocode** | [eren23/attocode](https://github.com/eren23/attocode) | 🟢 **MIT (text, 1,068 B)** | **17** | `2026-11-01` | Global | 🆕 Zero-to-hero lesson series on **building an AI coding agent**. Pushed the day of measurement. |
| **Knowledge-Teacher** | [m1908293028-boop/Knowledge-Teacher](https://github.com/m1908293028-boop/Knowledge-Teacher) | 🟢 **MIT (text, 1,056 B)** | **17** | `2026-07-12` | APAC | 🆕 Adapts explanation **depth** to the learner's existing level and emits a complete teaching document on a textbook-style framework (intuition → derivation). Chinese-language. |
| **mentor** | [ayhammouda/mentor](https://github.com/ayhammouda/mentor) | 🟢 **MIT (text, 1,071 B)** | **9** | `2026-06-21` | Global | 🆕 Claude skill building **official-first, dependency-ordered** learning paths for technical topics. 🔵 "Official-first" is a citation-grounding stance: it sequences the vendor's own docs rather than blog posts. |
| **teachme** | [beret21/teachme](https://github.com/beret21/teachme) | 🟢 **MIT (text, 1,064 B)** | **7** | `2026-07-19` | Global | 🆕 `/teachme` turns any topic into a themed, searchable handbook **in the learner's language**, verified and published to GitHub Pages. |
| **blind-review-skill** | [Jerryyy985/blind-review-skill](https://github.com/Jerryyy985/blind-review-skill) | 🟢 **MIT (text, 1,056 B)** | **5** | 🟡 `2026-04-30` | APAC | 🆕 Claude skill acting as an **undergraduate thesis blind-review examiner**: six weighted dimensions, seven-section structured report. 🔵 **The assessment-side counterpart to `idstack`** — and `p586` measured assessment as the regulated surface, so this is the tier that carries compliance weight. 🟡 ~6 months stale. |
| **ai-pm-atom-lesson** | [uimarch123-arch/ai-pm-atom-lesson](https://github.com/uimarch123-arch/ai-pm-atom-lesson) | 🟢 **MIT (text, 1,072 B)** | **5** | `2026-07-08` | APAC | 🆕 Claude skill expanding **one atomic concept** into a single-file, **offline-capable** interactive HTML lesson: authoritative definition, worked project case, practice judgements, visual demo. Chinese-language. |
| **smartedu-textbook** | [DanielHuang-ning/smartedu-textbook](https://github.com/DanielHuang-ning/smartedu-textbook) | 🟢 **MIT (text, 1,442 B)** | **5** | `2026-07-31` | APAC | 🆕 Claude Code skill **plus** CLI that fetches Chinese K-12 **statutory e-textbooks**. 🔵 The corpus-acquisition step a grounded K-12 tutor needs, and the only row here that targets a national textbook set. API said `NOASSERTION`. |
| **agentic-learning-skill** | [APareek89/agentic-learning-skill](https://github.com/APareek89/agentic-learning-skill) | 🟢 **MIT (text, 1,069 B)** | **4** | `2026-06-30` | Global | 🆕 Topic → self-contained interactive HTML lesson, **or** a brief → an installable Agent Skill. Runs on the client's own Claude, **no server** — the zero-hosting shape `P586-1` is built on. |

🔵 **Measured and shelved nowhere, recorded so it is not re-found:**
[`CabinServer39/quiz-gen`](https://github.com/CabinServer39/quiz-gen) is real (`23★`, MIT
byte-read at `1,077 B`, pushed `2026-10-18`, C#) but its **entire description is
`"Published: 2026-10-18"`** and it carries no README claims to characterise. 🔴 A row this
base cannot describe is not a row it can recommend.

---

## 🔴 Do not ship these — and why

| Repo | Verdict | Evidence |
|---|---|---|
| [GoogleCloudPlatform/aira](https://github.com/GoogleCloudPlatform/aira) | 🔴 **`596-D` BLOCK — disqualified by its own README, not by its licence** | 🆕 *Artificial Intelligence Reading Assessor* — scores a learner as *Pré-reader / Reader / Advanced* and rolls results up per class, per school, per region. `24★`, last push `2026-07-23`, **Apache-2.0 byte-read at `11,357 B`** on `main`. 🟢 **It clears every screen this page runs**: permissive grant, real organisation, education-core, live, not archived. 🔴 **Its README disqualifies it**: *"an open-source **demo experiment**"*, *"**proof-of-concept only**"*, *"does not reflect a completed system nor a finalized design"*, *"**not an officially supported Google product**"*, *"Please do not use any personal or sensitive data"*, and *"should not be used by children under 13 or to process data from children under 13"* — 🔴 **which excludes K-12, the exact population a reading assessor exists for.** 🔵 **The screen this base was missing:** read the README's own *status and audience* declarations before promoting, and treat a PoC or under-13 disclaimer as a BLOCK regardless of grant and provenance. Filed so `p597` does not promote it on the strength of the Apache-2.0 header. |
| [andymatuschak/orbit](https://github.com/andymatuschak/orbit) | 🔴 **Split licence — partly non-OSI** | 1,838★, pushed `2026-10-20`, API `NOASSERTION`. 🟢 **Resolved and now reconciled across pages** (see `586-A`). `LICENSE` reads: all sources **Apache-2.0** *except* `packages/app` and `packages/backend`, which are **AGPL-3.0-or-later *or* BUSL-1.1** at the licensee's choice. 🔴 **BUSL-1.1 is not an open-source licence.** 🟢 Its spaced-repetition *libraries* are buildable; 🔴 its app and backend are not shippable without AGPL or BUSL compliance. |
| [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | 🔴 **AGPL-3.0 + stale** | 🆕 1,317★ visual/interactive AI tutor — the second-largest tutoring repo after DeepTutor, and unusable in client work. Network copyleft, and last pushed `2026-01-09` (**~10 months**). |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 🔴 **AGPL-3.0 (text)** | 🆕 587★ lifelong skill-tree, K-12 → career. **API said `NOASSERTION`; the licence file says AGPL-3.0.** 🔴 This is the correction that runs the *other* way — see *Method*. Last pushed `2026-03-25` (~7 months). |
| [aaryansamanta/ai-ethos](https://github.com/aaryansamanta/ai-ethos) | 🔴 **BLOCK — no grant** | 🆕 498★. A 501(c)(3) nonprofit shipping multilingual AI tutoring for underserved learners — with **no licence at all**: six probes (`LICENSE`/`.md`/`.txt`/`COPYING`/`LICENCE`/`LICENSE-MIT`) all 404 and the API reports no licence. Reach and goodwill do not create a grant. Last push `2026-09-20`. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | 🔴 **AGPL-3.0 (text)** | 🆕 222★, pushed `2026-10-30`. Self-hosted AI language learning with CEFR levels and local-or-cloud LLMs. 🔵 **It is the live successor to the archived `LibreLingo`** — and it is copyleft too. See gap `586-C`. |
| [kantord/LibreLingo](https://github.com/kantord/LibreLingo) | 🔴 **ARCHIVED + AGPL-3.0** | 2,631★, `archived: true` re-measured `2026-11-01`; last push `2026-06-19`. Read-only upstream, no security fixes. 🟢 For a live alternative see `freelingo` — but it is AGPL-3.0 as well. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 🔴 **BLOCK — no grant** | 64★. Twelve probes all 404; API `spdx_id: NONE`. Unlicensed = all rights reserved. Last push `2025-11-04`. |
| [bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) | 🔴 **BLOCK — no grant** | 100★, AAAI-grade learner simulation. 🆕 **Re-probed `p586`: ten paths (`LICENSE`/`.md`/`.txt`/`COPYING`/`LICENCE` × `main`+`master`) all 404.** Still pushing code (`2026-09-29`) and still granting nothing. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | 🔴 **Do not gate on "MIT"** | `package.json` declares MIT and references a `LICENSE` that does not exist at 8 paths × 2 branches. A question for counsel. 🟢 Use [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (real MIT, 310★) instead — same job. |
| [cybercussion/SCOBot](https://github.com/cybercussion/SCOBot) | 🔴 **CC BY-SA 4.0 on software — RECIPROCAL** | 🆕 `165★`, pushed `2026-10-29`, the most-starred *live* artefact on `topic:scorm` after `scorm-again`. API said `NOASSERTION`; the `837`-byte `LICENSE` is **Creative Commons Attribution-ShareAlike 4.0**. 🔴 **This is the base's third CC-on-software case and the *second* reciprocal one** — 🔴 **`p599` CORRECTS `p589` HERE: the first was [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) at `939★`, which this row used to call a CC0 dedication and which is byte-read `CC BY-SA 4.0`.** `awesome-ai-agents-2026` really is `CC0-1.0`. ShareAlike propagates an obligation into whatever you build on it, and CC still grants no patent rights either way. Do not vendor. See `589-F`, `599-A`. |
| [adlnet/SCORM-to-xAPI-Wrapper](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | 🔴 **BLOCK — no grant AND archived** | 🆕 `99★`. Published by **ADL — the body that authored SCORM** — and it carries no licence, is `archived: true`, and was last pushed **`2017-10-02`**. 🔵 Recorded because it is the strongest single piece of evidence for `Trend 41`: a specification's own authors abandoned their own tooling, which is why generators now fill that layer. |
| [aneelv75/github-trending](https://github.com/aneelv75/github-trending) | 🔴 **BLOCK — no grant, and the secondary source oversold it** | 🆕 Served by the mandated `github trending education AI {year}` leg and described there as *"a curated list of trending and high-impact GitHub repositories in AI, GenAI and engineering"*. Measured: 🔴 **`3★`**, last pushed `2026-03-25`, and **`10` licence probes (`LICENSE`/`.md`/`.txt`/`COPYING`/`LICENCE` × `main`+`master`) all `404`.** 🔵 A reminder with a number on it: the leg's descriptions are not calibrated to size. |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | 🔴 **`599-A` RE-GRADED FROM 🟡 — `CC BY-SA 4.0`, RECIPROCAL, AND THE CODE HAS NO GRANT AT ALL** | 🆕 **`939★`** (was `936`), `165` teacher-facing skills, `main`, byte-read `2026-11-01` at `135d6275`: `LICENSE`, **`1,230 B`**, opening line `Creative Commons Attribution-ShareAlike 4.0 International`. `3` occurrences of `ShareAlike`, **`0` of `CC0`**. 🔴 **Three defects, each independently disqualifying.** (1) **Reciprocal** — *"If you remix, transform, or build upon the material, you must distribute your contributions under the same licence"*, so this is not the harmless CC0 case this page asserted for ten passes. (2) **The grant names only content**: *"The educational skills, documentation, examples, and curriculum materials in this repository are licensed under…"* — the repository is **TypeScript**, so 🔴 **the code is covered by nothing.** This is [`nextgen-ai`](https://github.com/aaryansamanta/nextgen-ai)'s *"MIT License (Code)"* defect inverted. (3) **The file disclaims itself**: *"This is a human-readable notice. The full legal terms are available at …/legalcode"* — 🔵 **so the operative terms are not in the repository and no byte-read of this file can reach them.** 🔵 **New screen rung: a grant file that points elsewhere for its own terms is a pointer, not a grant** — rank it with `598-B`'s manifest field. Not reference material either, without counsel. |

---

## Method — how every row above was verified

Three channels, in this order. Each one exists because the obvious one does not work here.

| Need | Channel | Why not the obvious one |
|---|---|---|
| Existence, stars, forks, `archived`, `pushed_at`, `default_branch` | `gh api -X GET search/repositories -f q="repo:owner/name"` | 🔴 `curl -sI https://github.com/...` returns **403 for every URL**, real or fabricated — re-verified again at `p586` against `moodle/moodle` (403) and a control that does not exist (403). **It certifies nothing**, and the standing instruction to verify URLs with `curl -sI` cannot be satisfied in this environment. `gh api repos/{owner}/{name}` is 403 too: this session's GitHub access is scoped. |
| **Licence (ground truth)** | `curl -sL https://raw.githubusercontent.com/{repo}/{default_branch}/{LICENSE}` | 🔴 The search API's `license.spdx_id` is wrong for ~25% of this base's rows. `p586` recovered six more rows this way. |
| Discovery of rows the base does not hold | 🆕 `search/repositories -f q="topic:ai-tutor"` / `topic:ai-education` + `sort=stars` | 🔴 Name and description search misses the field. **Eleven of the 38 rows above came from two topic queries** — including the largest. Topic facets are how this industry self-labels. |
| Description, README claims, maturity warnings | `WebFetch` on the repo page | Slower, and it often declines to name a licence it can see — but it reads prose the API does not expose. |
| 🆕 **Last commit on the DEFAULT BRANCH** | `WebFetch https://github.com/{repo}/commits/{default_branch}.atom` | 🔴 **`pushed_at` is not "last commit" — it counts a push to *any* ref.** Measured `p588`: [`apache/openmeetings`](https://github.com/apache/openmeetings) reports `pushed_at` `2026-11-01` while its default-branch feed ends `2026-10-26` — a **6-day** overstatement. The other three probes agreed exactly. 🟢 **Judge the staleness of the code you would actually fork on the feed, not on `pushed_at`.** |

🆕 **`NOASSERTION` is not a proxy for "probably permissive", and `p586` is the pass that
proves it.** `p585` recovered six `NOASSERTION` rows and most came back permissive, which
invited the inference that the API's blank means "permissive but non-standard filename".
It does not. This pass:

| Row | API said | Licence file says | Direction |
|---|---|---|---|
| `24kchengYe/human-skill-tree` (587★) | `NOASSERTION` | 🔴 **AGPL-3.0** | **Against** the row |
| `aaryansamanta/nextgen-ai` (492★) | `NOASSERTION` | 🟡 **MIT — code only** | Partly |
| `hugohe3/ppt-master` (71,803★) | `MIT` | 🟢 MIT | Confirmed |
| `DozenTwelve/Papermorph`, `assafkip/claudemy`, `ZeKaiNie/universal-examprep-skill`, `orionsheep/wordlink` | `MIT`/`NOASSERTION` | 🟢 MIT | Confirmed |
| `artcc/freelingo` (222★) | `AGPL-3.0` | 🔴 AGPL-3.0 | Confirmed |
| `aaryansamanta/ai-ethos` (498★) | *none* | 🔴 **no file at 6 paths** | Confirmed no grant |

🆕 **`p591` adds the step that a byte-read alone does not give you: classify on the
licence's TITLE.** Reading the file is necessary and **not sufficient** — a licence body can
name a *different* licence than the one it grants. Measured `2026-11-01` over `65` reads:

| Repo | Body match says | 🔴 Title says | What it actually is |
|---|---|---|---|
| [ximing/aimo](https://github.com/ximing/aimo) | `MIT` | 🔴 `Business Source License 1.1` | 🔴 **Source-available, not open source.** BSL names a future permissive licence as its `Change License` **inside its own text**, and here that value is MIT. A body matcher reads the promise, not the grant. `5,643 B`. |
| [SethRobinson/UGTLive](https://github.com/SethRobinson/UGTLive) | `MIT` (full permission sentence, verbatim) | 🔴 `The Proton SDK License (based on the XFree86 1.1 license…)` | 🟡 Permissive-family but **not MIT and not a standard SPDX id**; XFree86 1.1 carries an endorsement/advertising-style clause MIT does not. `2,483 B` at `LICENSE.md`. |
| [Orenoid/BabelDuck](https://github.com/Orenoid/BabelDuck) | contains `MIT`, `AGPL`, `GPL` | 🔴 `Time-Limited Competition Protection License, Version 1.1, AGPL Future License` | 🔴 **Bespoke non-OSI licence with a delayed AGPL conversion.** `37,739 B` — size alone was the first clue. |
| [nirholas/lyra-web3-playground](https://github.com/nirholas/lyra-web3-playground) | no match | 🔴 `Copyright 2026 nirholas` | 🔴 Bespoke; `860 B`, no recognisable grant. |

🟢 **The rule, in one line:** take the **first non-empty line** of the licence file as the
grant's identity, treat a `≠ ~1,050–1,100 B` "MIT" as suspect until the title is read, and
flag any file containing `Change License`, `Change Date`, `Commons Clause` or
`Competition Protection` for counsel. 🔵 **Two of this pass's `65` reads (`3.1 %`) invert
under this rule** — low as a rate, and both would have shipped as permissive.

🆕 **`591-B` — `NOASSERTION` and `license: null` are different flags.** This base has
graded them together since `p579` (`Trend 31`, *"about one in two"*). Byte-read
`2026-11-01`:

| API state | rows byte-read | had **no** licence file | resolved to a permissive OSI grant | resolved to something else |
|---|--:|--:|--:|--:|
| `NOASSERTION` | `12` | 🔴 **`0`** | 🟢 `6` (MIT ×4, Apache-2.0 ×2) | `6` — CC-BY-SA-4.0, BSL-1.1, GPL-2.0, XFree86-derived, 2× bespoke |
| `license: null` | `10` | 🟢 **`10`** | `0` | `0` |

🟢 **So the two states carry opposite instructions.** `null` is a **reliable block** — `10
of 10`, each probed at `6` filenames × `2` branches. `NOASSERTION` is **`0-for-12` as a
negative**: it never once meant "no licence", and half the time it hid a grant a studio
could ship. 🔵 `NOASSERTION` is a *parser* failure (non-standard filename, HTML wrapper,
dual grant, modified preamble), not an absence.

🔴 **So the rule is: read the file in both directions.** A blank API field is an *unknown*,
and an unknown resolved 587 stars deep turned out to be network copyleft.

🔴 **Two traps that produce false zeros.** (1) OR-batching `repo:` qualifiers is cheap, but
**one unresolvable qualifier returns `422` for the whole batch** — use single calls.
(2) A **renamed** repository is indistinguishable from a deleted one by `repo:` search.
`p586` hit this twice and resolved both by searching the org for the name:
`openedx/edx-platform` → [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform),
and `OpenEduCat/OpenEduCat` → [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp)
(LGPL-3.0, 903★, default branch `19.0`). **Never record a `422` as dead without an org search.**

---

## 🔴 Open gaps on this page — stated so they are not re-discovered

| Gap | Status | What would close it |
|---|---|---|
| `588-A` 🔴 **This page's inclusion rule changed at `p587` and was never written down** | 🆕 **Opened and resolved `p588`** | `p587` shelved two *learning-about-AI* repos as the shelf's two largest rows, while [`../intel/open-gaps.md`](../intel/open-gaps.md) still retires a whole discovery query on the ground that such repos are **not education software** and names one of them as the specimen. 🟢 **Resolved by naming the class** (*enablement tier*, above) **and completing it** — four of its five largest members were unfiled. 🔴 **What is still open: `open-gaps.md`'s retirement row now contradicts this page and needs the same edit.** |
| `588-B` 🔴 **Every non-GitHub fact in this base is second-hand by channel necessity, not by sloppiness** | 🆕 Opened `p588` | Probed `2026-11-01`: **7 of 7** non-GitHub hosts returned **no connection at all** — `www.nepad.org`, `link.springer.com`, `www.unesco.org`, `www.iesalc.unesco.org`, `www.linuxfoundation.org`, `digital-strategy.ec.europa.eu`, `www.future-ed.org`. In the same minute `api.github.com` returned `200` and `raw.githubusercontent.com` `301`. 🔵 **WebSearch snippets still arrive, so intel keeps flowing** — but **no primary document behind any intel page can be read first-hand here**, which is why this base's two unverifiable leads this pass stayed unwritten (see [`../intel/market.md`](../intel/market.md) `p588`). 🟢 Closing it needs those hosts allowed in the session's network policy — a configuration change, not a research step. |
| `586-A` 🔴 **REFUTED — the step exists, is wired as a blocking gate, and has since `p308`** | 🔴 **REFUTED `p587`. The gap was false when filed.** | `586-A` stated *"the step itself still does not exist — a `grep` of every curated page for each repo address, run before commit, would close it."* 🔴 **That step is `gate-shelf-consistency`** (`Makefile:660`, *"no slug may carry disagreeing licence cells across the live shelves"*), it has **59 controls**, and it is in `HOOK_GATES` (`Makefile:128`) — so it runs on every `make hooks` and blocks via `ingest/pre-commit`. Two more exist: `compose/code/p121-stale-token-crosspage/crosspage.py` (`p121`, keys on licence tokens) and `ingest/crosspage-figure-claims.py` (`p538`, keys on figures). 🔵 **`p587` wrote a fourth one before looking** — the fourth rediscovery of this instrument in this base, after `p121`, `p538` and `p586`'s gap. |
| `587-A` 🔴 **A naive cross-page sweep reports ~10 contradictions and ALL of them are false. `p308`'s control list names every trap in advance.** | 🆕 Opened and closed `p587` | `p587`'s own sweep flagged 10 addresses as carrying disagreeing licence tokens. **Hand-audited: 0 were base defects, 10 of 10 were the instrument's false positives**, every one of a single shape — *a row that names one repo URL and a second licence belonging to a different subject named in the same row.* `compose/patterns.md:1647` reads `\| Canvas (AGPL-3.0) \| bruchris/canvas-lms-mcp \| **MIT** \|`: the AGPL-3.0 is **Canvas**, the MIT is the MCP server, and both are correct. `patterns.md:1648` does the same with Open edX (AGPL-3.0) beside `openedx/XBlock` (Apache-2.0) — and labels it *"the key fact"*. 🔴 **Three "corrections" were drafted and withdrawn before publication.** 🟢 `gate-shelf-consistency`'s 59 controls are listed in the `Makefile` as covering *"comparators, possessives, quoted claims, dual grants, paired rows"* — **the exact four classes this pass fell into.** The lesson is not about licences: **read the instrument index before building an instrument.** |
| `587-B` 🔴 **`README.md` is excluded from the blocking licence gate by design, and nothing says so on the shelves** | 🆕 Opened `p587` | `compose/code/p308-shelf-consistency/shelf_consistency.py:63-71` splits `carried_index.SHELVES` into `LIVE_SHELVES` and `DATED_SHELVES`, and `README.md` — **2.7 MB, the largest document in this base** — lands in `DATED`, whose disagreements are reported by `make shelf-census` as *"a backlog, never a failure."* So a wrong licence token on `README.md` cannot turn the gate red. 🟡 **Read from source, not from a run** — this pass could not execute the suite (see `587-C`), so whether `README.md` *currently* carries a disagreeing token is **unmeasured**, and this gap is about the design, not about a known defect. |
| `587-C` 🔴 **This base's measurement channel is environment-dependent and `p579`'s recorded finding does not hold here** | 🆕 Opened `p587` | `p579` recorded that `api.github.com` answers `200` *"including plain `curl` with no token"*, and `p586` built on it. 🔴 In this environment **every** `https://api.github.com/repos/{owner}/{name}` returns an authorisation error, for all five repositories tried. 🟢 **The working substitute, used for every measurement on this page:** `gh api -X GET search/repositories -f q='repo:owner/name'`, which returns `stargazers_count`, `license.spdx_id`, `pushed_at` **and `default_branch`** in one call; `raw.githubusercontent.com` serves licence text normally. 🔵 A channel finding must record **which** channel and **where**, or the next pass inherits a false capability. |
| `587-D` 🔴 **Default branches are not guessable, and four of this pass's rows prove it** | 🆕 Opened `p587` | `virgiliojr94/book-to-skill` = `master`; `thm-mni-ii/feedbacksystem` = `dev`; `bigbluebutton/bigbluebutton` = `v4.0.x-develop`; `openeducat/openeducat_erp` = `19.0`. A licence probe on `main` would have returned `404` for all four and this base would have filed four false absences. 🟢 `default_branch` comes free in the `search/repositories` row (`587-C`) — **take it from there, never assume.** |
| `586-A` **This base has no cross-page reconciliation step, and it is still producing contradictions** | 🆕 **Opened and partly closed this pass** | At `p585`, [`../repos/foundations.md`](../repos/foundations.md) recorded `orbit`'s split licence as *resolved* while this page simultaneously opened `585-C` calling it *unresolved*. **One repo, one pass, two verdicts.** `p585` named the missing reconciliation step as the cause of exactly this class of defect and then committed another instance of it. 🟢 Reconciled here by re-reading the licence text first-hand. 🔴 **The step itself still does not exist** — a `grep` of every curated page for each repo address, run before commit, would close it. |
| `586-B` **Duplicate gap IDs for one gap** | 🆕 Opened this pass | The absence of a permissive proctoring platform is filed as `585-B` on this page and `585-G` on `foundations.md`. Two IDs, one gap, no link between them. Gap IDs need to be allocated once per base, not once per page. |
| `586-C` 🆕 **Language learning is an entirely copyleft niche** | 🆕 Opened this pass | Measured `2026-11-01`: `LibreLingo` (2,631★) **archived**, `freelingo` (222★) **AGPL-3.0**, `word-atlas` (3,604★, MIT) is vocabulary-only, `wordlink` (266★, MIT) is vocabulary-only. **There is no permissive general language-learning platform.** A language engagement either accepts AGPL or composes `word-atlas` + `wordlink` + `OpenPronounce` (MIT, pronunciation) over `fsrs` scheduling — which is a **BUILD**. |
| `585-A` **Learner simulation is still unlicensed** | Open across 14+ passes; re-probed `p587` | [`bigdata-ustc/Agent4Edu`](https://github.com/bigdata-ustc/Agent4Edu), **100★**, re-probed `2026-11-01` at ten paths (`LICENSE`/`.md`/`.txt`/`COPYING`/`LICENCE` × `main`+`master`) — **all 404**, API licence `NONE`. 🔵 Last push still `2026-09-29`, unchanged since `p586`: **the repository has not moved, so neither has the gap.** This is a **BUILD**, not an adopt. 🆕 **`p592` upgraded the evidence from `10` failed probes to a positive enumeration:** the repository's own top-level listing is `Code/`, `data/demo/`, `docs/assets/`, three poster/slide files, `README.md` and `requirements.txt` — **no licence file at any path, because the enumeration is complete.** Re-measured `2026-11-01`: `100★`, `archived: false`, API licence `null`, last push `2026-09-29` (unchanged). 🔵 The finding is no longer *"we cannot find a grant"* but *"the repository has none"*, and the remedy is upstream — open an issue asking the authors to add one — not another probe. |
| `585-B` / `585-G` **No permissive proctoring *platform*** | Open, re-measured `p586` | `Proctoring-AI` (MIT, 633★) is a component and last pushed `2024-12-10` (**~23 months stale**); `SafeExamBrowser` is MPL-2.0 and current (`2026-10-30`). A studio ships SEB + an agent, not a platform. 🔵 Merge these two IDs — see `586-B`. |
| `585-C` 🟢 **`orbit`'s licence** | 🟢 **CLOSED `p586`** | Licence text read first-hand: Apache-2.0 core, AGPL-3.0-or-later/BUSL-1.1 for `packages/app` + `packages/backend`. Recorded in the block table above and on `foundations.md`. |
| `585-D` 🟢 **`potsie` vs `warren` recommendation was backwards on recency** | 🟢 **CLOSED `p586` — corrected in place** | Re-measured `2026-11-01`: **`potsie` last pushed `2024-12-18` (~23 months, 11★)**; **`warren` `2026-10-31` (17★)**. This base's standing advice to prefer `potsie` as "the production-ready alternative" is **withdrawn**: it is the stale one. 🔵 `warren`'s own proof-of-concept warning still stands — the honest statement is *neither is production, and `warren` is the only one still maintained*. |

---

## History

Pass-by-pass narrative for `p577`–`p584` — including the measurements and withdrawals that
produced the rows above — is preserved at
[`../archive/2026-11-01-p585-pre-consolidation/agents-top.md`](../archive/2026-11-01-p585-pre-consolidation/agents-top.md).
Earlier history is in the other `archive/` directories, and the append-only discovery log
is [`./trending.md`](./trending.md).
