---
industry: education
region: Global
updated: 2026-10-21
---

# Education — AI agents worth building on

**Pass 362 · 2026-10-21.** Every row below was checked first-hand: liveness and default
branch via `git ls-remote --symref`, and the licence **read from the payload** at
`raw.githubusercontent.com` — never from a badge, a README claim or GitHub's own
classifier. Where the classifier and the payload disagree, the payload wins and the
disagreement is recorded.

**Evidence:** [`mit-body-sweep`](../evidence/mit-body-sweep.2026-10-21-p362.tsv) ·
[`grant-corrections`](../evidence/grant-corrections.2026-10-21-p362.tsv) ·
[`author-key-rederivation`](../evidence/author-key-rederivation.2026-10-21-p362.tsv) ·
[`new-rows-bench`](../evidence/new-rows-bench.2026-10-21-p362.tsv) ·
[`regional-legs`](../evidence/regional-legs.2026-10-21-p362.tsv)

## 🔴 `p362`: three rows published as permissive are not, and the instrument that says so was already in this repository

🟢 **`make hooks` ran: 28/32 green on arrival, 32/32 on exit — and the four REDs were the
pass.** This
base has spent several passes sweeping **liveness** and **stars** — the two cheapest
channels — while the **grant** column went unexamined. 🔴 `p362` pointed this base's own
added-restriction classifier, [`p1054-mit-plus-clause`](../compose/code/p1054-mit-plus-clause/),
at **every live-shelf address that co-occurs with the token `MIT`** and the column broke
in three places.

| Sweep over 144 addresses | Count | What it means |
|---|---:|---|
| `MIT` | **115** | grant exact |
| `NOT-MIT-BODY` | **12** | 🟢 **adjacency, not error** — these lines merely *mention* MIT; 5 checked cell-by-cell (ISC, AGPL short-form, MIT-in-prose, OGL dual, AGPL+MIT split) and the shelves are **right on all five** |
| `NO-PAYLOAD` | **11** | 🟢 already flagged as no-grant rows on these shelves |
| `MIT-BODY-PLUS:unclassified-addition` | **3** | 🟢 **all three excesses read, all three benign** — see below |
| 🔴 `NOT-OPEN-SOURCE:added-restriction` | **3** | 🔴 **`QingdaoU/Judger`, `CaviraOSS/PageLM`, `Samkarya/online-exam-questions`** |

🔵 **The denominator is a superset by construction**, and it is stated so no successor
reads 144 as "the MIT cells": the extraction takes every address on a live-shelf line
that also carries the token `MIT` anywhere on it. That is why 12 came back
`NOT-MIT-BODY`, and why that number is **not** a defect count.

### 🔴 `CaviraOSS/PageLM` — the most consequential cell on this shelf was wrong, and this base had already measured it right

🔴 **The live cell read `MIT (LICENSE.md)` and added *"GitHub classifies this
`NOASSERTION`; the payload is stock MIT"*.** The second half is false. The payload at
`main/LICENSE.md` is **8 563 B of "PageLM Community License"**: permission is granted
only *"for **personal, educational, or non-commercial research purposes**"*, §3 is a
**Non-Commercial Use Restriction**, and §4 is a **Revenue Sharing Requirement** —
*"a revenue-sharing agreement **must be executed with the copyright holders prior to any
commercial distribution, deployment, public release, or commercial operation**"*. It
then applies itself *"in whole or in part"*, so **any code snippet, algorithm or design
pattern** of it inside a commercial product is Commercial Use.

🔴 **This is a regression, not a gap.** This base measured the same payload correctly
at `p123`/`p411` and committed the result:
[`p411-cession-identity-gate`](../compose/code/p411-cession-identity-gate/) records
`familia=NO-OSI (community license) usable=NO 8563 B sha256:c834209c5f33` and names the
clause pair *"no comercial + reparto de ingresos"*; `pass257-restriction-scan` records
*"`p255` caught `CaviraOSS/PageLM` only because PageLM recites the MIT grant verbatim"*.
🔴 **A later pass overwrote a correct verdict with the wrong one and wrote the cause of
the mistake into the cell** — *recites MIT verbatim* is precisely what *"the payload is
stock MIT"* is a misreading of. 🔵 At **2 035 ★** it was also wired into
`compose/patterns.md` Pattern 5 as an MIT component of a client deliverable; that
component is removed there this pass.

### 🔴 `Samkarya/online-exam-questions` — the shelf read the grant generously and the grant is not MIT's

🟡 The live cell called it *"stock MIT text whose copyright line appends a
contradiction"* and concluded *"MIT's operative text grants the permissions regardless
of the reserved-rights phrase"*. 🔴 **The text is not MIT's.** The payload is titled
**"ExamOven Non-Commercial Open Source License (ENCOSL), Version 1.0, April 2026"**
(2 118 B) and grants use *"for personal, educational, and non-commercial purposes"*
only. §2: **"Commercial use ... is strictly prohibited for all parties EXCEPT for
ExamOven (https://examoven.com) and its authorized owners/affiliates."** It also carries
a contributor assignment: opening a pull request grants ExamOven a perpetual commercial
licence to the contribution. 🔵 **The reserved-rights phrase was never the problem** —
the narrowing is in the operative sentence, two lines above it.

### 🟢 And the other half, because a sweep that only reports hits is not a measurement

🟢 **Three rows came back `MIT-BODY-PLUS` and all three stay `MIT`** — the excess was
read rather than assumed:

| Row | Bytes | What the excess actually is |
|---|---:|---|
| [`AnonymousOnyx22/brightspace-d2l-mcp`](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 1 200 | an upstream attribution note (*"Portions of this software are derived from brightspace-mcp-server"*) |
| [`ls1intum/Ares2`](https://github.com/ls1intum/Ares2) | 1 345 | a long institutional holder line (TUM, Research Group of Applied Education Technologies) |
| [`nvaes/CEB`](https://github.com/nvaes/CEB) | 1 240 | 🟡 a French note that the **CEB papers themselves** remain the property of the Fédération Wallonie-Bruxelles and are *not* distributed with the software — **MIT on the code, no grant on the content** |

🔵 **The `nvaes/CEB` line is worth keeping as a shape rather than a footnote.** A
permissive grant on a curriculum tool whose *assessment content* is reserved is the
education-specific form of the code/data split, and it is the third instance on this base
after `learning-commons-org/evaluators` and `oaknational/oak-curriculum-ontology`.

## 🔴 `p362`: a grant inherited from a SIBLING repository, and no channel ever said MIT

🔴 **[`QingdaoU/Judger`](https://github.com/QingdaoU/Judger) (496 ★) was published as
`MIT` on three shelves and its payload is the Star And Thank Author License.** Read at
its real default ref, `newnew/LICENSE`, 1 823 B: MIT's permission paragraph verbatim,
then **"And wait, the most important, you shall star/+1/like the project(s) ... and then
thank the author(s)"**, then a forking clause forbidding deletion or modification of the
copyright and project-url sections. 🔴 **That is an obligation MIT does not contain, so
the row is not permissive and not OSI open source.**

🔵 **The mechanism is new to this base and it is worth more than the row.** Nothing ever
told this base that `Judger` was MIT:

| Channel | What it says about `QingdaoU/Judger` |
|---|---|
| 🔴 the payload at `newnew/LICENSE` | **SATA** — 1 823 B |
| 🔴 GitHub's own classifier (index) | **`NOASSERTION`** / *"Other"* |
| 🟢 the SIBLING, `QingdaoU/OnlineJudge` | **MIT** — 1 085 B at `master/LICENSE`, read this pass as the control |

🟢 **So the `MIT` came from the organisation, not from a file.** `QingdaoU/OnlineJudge`
is genuinely MIT and remains the tier's recommendation; `Judger` is its sandbox, by the
same team, in the same org — and it ships a different grant. 🔴 **An org-sibling
inference is not a payload read**, and this base has no gate that can tell the two apart,
because every grant instrument it owns takes *bytes* and answers correctly when it gets
them.

🟢 **Proof that it would have answered correctly: it does.** `p1054-mit-plus-clause`,
built at `p187` for exactly this class, returns
`MIT-BODY-PLUS:unclassified-addition` / `is_usable_permissive: False` on the SATA
payload. 🔴 **It was never run on this row.** The row was shelved at `p356`; five passes
of liveness and star sweeps followed, and not one of them read a grant.

### 🔴 And the refusal it does produce is a byte accident, so `p362` repaired the instrument

🔴 **SATA's verdict came from the size limb alone — 673 B of excess, with ZERO vocabulary
hits.** `RESTRICTION_TERMS` knows *compete*, *SaaS*, *non-commercial*; SATA says **star**
and **thank**. 🔴 Measured on a payload that abridges the MIT body by about as much as
SATA adds (`fixtures/sata-mit-inband-1072.synthetic.txt`, **1 072 B, inside the
1 020–1 150 B band**): the verdict was **`MIT`** and `is_usable_permissive` was
**`True`** — publishable as permissive. 🟢 **Closed in the instrument, not excused in the
shelf:** SATA's phrases are now named `RIDER_ANCHORS`, both fixtures are pinned, and five
controls were added — including the in-band case and a false-positive control proving the
word *star* in ordinary prose does not fire. `test_mit_plus.py`: **39/39**, up from 34.

## 🟡 `p362`: three published author figures do not re-derive, and one refutes `p349`'s direction

🟢 `gate-author-key` was RED on arrival over **22 unkeyed author figures** on the live
shelves. 🔴 **Annotating them `%ae` would have been a guess**, so all 12 identifiable
rows were re-cloned and re-counted first.

| Row | Published | Derived (`%ae`) | Verdict |
|---|---|---|---|
| [`The-Burnes-Center/a-iep`](https://github.com/The-Burnes-Center/a-iep) | 836 commits, 7 authors | **1 281 commits, 12 authors** | 🔴 **not reproducible under any convention** — `--no-merges` 1 173, `--first-parent` 351, `%an` 12. Its last commit is **2026-10-14**, *before* the pass that published 836, so this is not staleness |
| [`edificeio/entcore`](https://github.com/edificeio/entcore) | 21 authors | **139 (`%ae`)** over **11 714 commits**, `%an` 142 | 🔴 **low by a factor of six**, on the row `intel/trends.md` §26 rests on. 🟢 Its commit date (2026-10-20) was right, and the correction strengthens that trend rather than weakening it |
| [`Neutralmilkzzz/moodle-cli-hku`](https://github.com/Neutralmilkzzz/moodle-cli-hku) | 344 commits, 4 authors | **356 commits** (`--no-merges` 301), **5 (`%ae`)**, `%an` 4 | 🔴 **neither figure re-derives**: 4 is the `%an` key, and 344 matches no convention at this HEAD. 🟡 1 of the 5 addresses is `noreply@anthropic.com` — 10 commits |
| [`shaheeranser/exam-proctor`](https://github.com/shaheeranser/exam-proctor) | 25 commits, 1 author | 25 commits, **2 (`%ae`)**, `%an` 1 | 🟢 commits exact; 🔴 the author figure is the **`%an`** key; 2 of 25 commits sit on the privacy-masked address |
| the other 9 rows | — | — | 🟢 **exact under `%ae`** |

🔵 **So the audit is 13 figures re-derived: 9 exact, 4 corrected** — and the four failures
have three different causes. A **mis-keyed** count (`moodle-cli-hku`, `exam-proctor`), a
**non-reproducible** one (`a-iep`), and one off by **6×** that reads like a
contributors-list figure rather than a commit read (`entcore`). 🔴 **Not one of them is
dormancy**, so no liveness sweep and no star sweep could ever have found them.

🔴 **`p349`'s directional claim is refuted by a counter-example.** Its hazard note says
*"`%an` runs 1–9 BELOW `%ae`"*, measured over eight rows. 🟢 On
[`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam) the order **inverts**
— `%an` **5**, `%ae` **4** — because there one person commits under two names from a
single address, while on `moodle-cli-hku` one person commits from two addresses under a
single name. 🔵 **So the two keys are not ordered, they are different questions**, and a
successor cannot convert between them in either direction. Registered as `ACTION ZZ-bn`.

## 🟢 `p362`'s discovery legs — the index is saturated against this corpus, with a number

🔴 **The four prescribed global legs and the four regional ones returned ZERO facts and
ZERO addresses this base does not already carry** —
[`regional-legs`](../evidence/regional-legs.2026-10-21-p362.tsv) records each query and
what came back. 🟢 Stated rather than passed over, because an informed null result is the
only thing that distinguishes a saturated channel from an unrun one.

🟢 **The index legs did better, and the yield rate is the finding.** Six topic-anchored
`search_repositories` legs returned **41 in-domain candidates; 37 were CARRIED** and
**4 were new**. 🔵 At a 90 % carried rate this corpus is close to saturated on the
discovery axes this base knows how to spell — which is an argument for the *function*
legs `p356` introduced, not for more vocabulary.

🔴 **Two query-shape facts a successor should not re-buy, both measured this pass:**

1. 🔴 **An `OR`-group across `in:name,description,readme` drops the vertical qualifier.**
   `tutor OR teaching OR curriculum ... mcp` sorted by `updated` returned 28 572 matches
   whose first 40 were generic MCP and coding-agent repositories, **with no education row
   at all**. The same is true of `IEP OR "special education" ... agent` (84 481 matches,
   top rows: `rea`, `superpowers`, `hermes-agent`). 🟢 **`topic:` qualifiers and tight
   `in:name,description` phrases stayed on-domain in every leg.**
2. 🔴 **Logical operators do not apply to qualifiers at all.**
   `topic:special-education OR topic:iep` is **refused** by the API:
   *"The search contains only logical operators (AND / OR / NOT) without any search
   terms."* 🔵 So a multi-topic leg is **n separate calls**, and a successor budgeting one
   call per axis will silently under-cover.

### 🆕 The four new rows, benched before shelving

🟢 Each was re-cloned blobless and read on the commit channel; grants read from payload at
the default ref. Placement uses the timezone limb, with the `%ae` domain limb as the
second witness ([`new-rows-bench`](../evidence/new-rows-bench.2026-10-21-p362.tsv)).

| Row | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region | Bench, and what it is for |
| --- | --- | --- | --- | ---: | --- | --- |
| 🆕 Dhee | [tura-learn/Dhee](https://github.com/tura-learn/Dhee) | 🟢 **MIT** (1 071 B) | `main/LICENSE` | **32** | **APAC** (India) | 198 commits · 3 authors (`%ae`) · 2026-01-28 → **2026-10-18** · `+0530` on **198 of 198** commits, `314ecorp.com` on the keyed limb. 🟢 **A memory layer built FOR tutor agents** rather than a general agent-memory library — the layer `Pattern 10` had to assemble from `py-fsrs` plus glue |
| 🆕 montessori-skill | [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | 🟢 **MIT** (1 063 B) | `master/LICENSE` | **72** | **APAC** (China) | 8 commits · 1 author (`%ae`) · `+0800` on 8 of 8 · **5 files**. 🟢 **The first PERMISSIVE pedagogy skill-pack on this base** — 🔴 and at 5 files it is a reference, not a corpus: `education-agent-skills` carries 165 `SKILL.md` and is `CC-BY-SA-4.0` |
| 🆕 CodeSense | [XiaoCow666/CodeSense](https://github.com/XiaoCow666/CodeSense) | 🟢 **MIT** (1 067 B) | `main/LICENSE` | **4** | **APAC** (China) | 554 commits · 7 authors (`%ae`) · 2025-10-18 → **2026-10-09** · `+0800` on **554 of 554** · 640 files. 🟢 **Code evaluation + guided learning + restricted execution + learning analytics in one MIT platform** — and it matters more this pass than last, because `Judger` just left the permissive column |
| 🆕 educa-lrs | [digital-learning-gmbh/educa-lrs](https://github.com/digital-learning-gmbh/educa-lrs) | 🔴 **AGPL-3.0** (33 889 B) | `main/LICENSE.md` | **4** | **EMEA** (Germany) | 31 commits · 3 authors (`%ae`) · 2024-09-04 → **2025-11-13 (dormant ~11 months)** · `+0100` on 26 of 31, `schule-plus.com` 27 and `digitallearning.gmbh` 1 on the keyed limb. 🟡 **A second xAPI learning-record store, and the first placed in EMEA by its own vendor's commit channel** — AGPL, so reach it over its API |

🔵 **One named non-row, so it is not re-discovered:**
[`constantinmay/learntrace-skill`](https://github.com/constantinmay/learntrace-skill)
(4 ★, a USTC competition entry building traceable learning portfolios) is live on `main`
and has **no grant at any of eight probed paths** and **no `license` key in the index**.
**All rights reserved.**

🟢 **A fresh instance of `p361`'s §29, for free.** `educa-lrs` reads **three different
"recency" dates**: `pushed_at` **2026-03-19**, `updated_at` **2025-11-13**, and the last
commit on its default branch **2025-11-13**. 🔵 Here `pushed_at` runs *ahead* of both —
a push to a non-default branch — so the only field that answers *"is anyone still working
on this?"* remains the commit.

## 🟢 `p361`: the GitHub index is OPEN, and the inference that closed it for five passes was WRONG

🔴 **Passes 356–360 each recorded `api.github.com/search/*` **403** and concluded that a
credential scoped to one unrelated repository could not read anybody else's. The first
half of that is still true. The conclusion was not.** `p361` re-probed by `curl` and got
the same five answers: 🔴 `api.github.com/repos/*` **403** · 🔴 `api.github.com/search/*`
**403** · 🔴 `github.com` HTML **403** · 🔴 `codeload` **403**. 🟢 **Then it tried the
same query through the session's GitHub MCP tool and the index answered in full** —
stars, forks, default branch, topics, `archived`, `pushed_at`, SPDX classifier.

🔵 **The boundary is per-tool, not per-credential.** In the same session and on the same
credential, `search_repositories` answers for *any public repository* while
`get_file_contents` refuses anything outside the two attached repositories
(`gmilano/globant-kb`, `gmilano/education-kb`) with an explicit scope error. 🟢 **So
"the API is 403" was a statement about one transport, and five passes generalised it to
the index.** The lesson is cheap and reusable: *before recording a channel as closed,
enumerate the transports that reach it.*

🟢 **What that recovered, immediately.** The ★ column on this file and on
`repos/foundations.md` carried **78 cells reading `not re-derived`** — one per row that
no pass since `p355` could measure. 🟢 **`p361` measured **273 of the corpus's 277 addresses** at their published
spelling — 261 directly, 12 more once forks were un-excluded — and filled all 78 cells.** Of the **89** figures already published, **78
re-derive within ±2** and the **11** that moved are the youngest repositories on the
shelves, led by `xiaoyang111222/cn-math-taxonomy` at **+157 in one day** (3 days old).
🟢 **Zero corpus defects in the star column.** Every ★ figure on both files is now a
single measurement taken in this pass.

🔵 **One gate defect, caught before it was published, and worth stating.** `p361`'s first
star-diff took the *last numeric cell* in each row and accused
`vishalsachdev/canvas-mcp` of being published at **8** against a measured **302** — a
38× "defect". 🟢 **The row says `not re-derived`; the 8 came from a different table
counting agent skills.** The rule that works is the one `p360` arrived at from the other
direction: **key on the column, not on the shape of the token.** Re-run position-aware
against the `★` header, the diff reports **89 of 89 clean**.

## 🔴 `p361`: absence from the index is NOT evidence of death, and the mechanism is three-fold

🔴 **The index resolved 261 of this corpus's 277 addresses. A pass that took the other 16
for dead would have published 16 false deaths — 5.8 % of the base.** All 16 answer
`git ls-remote --symref`. 🟢 **`p361` established the mechanism for 15 of them by
designed test:**

| Mechanism | Count | Test that establishes it | Recovery |
|---|---:|---|---|
| 🔴 **Fork exclusion** — GitHub repo search omits forks by default | **12** | re-query with `fork:true`; all 12 return, all 12 carry `fork: true` | add `fork:true` |
| 🔴 **Repository rename** — old address 301s | **1** | `openedx/edx-platform` and `openedx/openedx-platform` return the **identical HEAD SHA** `7f01c42157d3` | index carries the new name only |
| 🔴 **Owner rename / transfer** — old owner 301s | **2** | `naiayti/TeachingKG` ≡ `Teaching-Knowledge-Graph/TeachingKG` (`9f8c0a3f6704`); `christophblessing/quiz-recap` ≡ `openHPI/quiz-recap` (`0927b556d2e4`) | search by repo name, not address |
| 🟡 **Unexplained** | **1** | `JeabtiE/jump-hackathon-demo` is live (`e03c5711c72f`), absent from the index under `fork:true` and absent by name | 🔴 **stated, not guessed** |

🟢 **This is why this base reads liveness on `ls-remote` and licences from `raw`.** The
index is a *discovery and ranking* instrument. It is not a liveness instrument, and
`p361` is the pass that can prove that rather than assert it.

## 🔴 `p361`: three "recency" fields, three different answers, and only one is a commit

🔴 **The index's `updated_at` is not recency, and neither is `pushed_at`.** Measured on
one address, `Apereo-Learning-Analytics-Initiative/OpenLRW`:

| Field | Value | What it actually tracks |
|---|---|---|
| `updated_at` (returned in minimal output) | **2026-08-04** | repository *metadata* events — stars, topics, watches |
| `pushed_at` (full output only) | **2025-09-12** | a push to *any* ref, including a tag or a branch delete |
| 🟢 `git log -1` on the default branch | **2020-02-06** | 🟢 **the last commit** |

🔴 **A 6½-year gap between the field a ranked search hands you and the truth.** Any shelf
built on `updated_at` would publish a project abandoned in 2020 as current. 🟢 **The
commit channel — `git log` over a `--filter=blob:none --depth=200` clone — stays the only
instrument on this base that answers "is this maintained".**

## 🟢 `p361`: a new instrument the liveness channel is structurally incapable of replacing

🟢 **`archived` is in the index and nowhere in `git`.** An archived repository is
read-only upstream: no issues, no PRs, no commits ever again — and it answers
`ls-remote` exactly like a healthy one. 🟢 **`p361` swept all 277 addresses for
`archived:true` (with `fork:true`, so forks were not silently skipped): 1 hit.**

🔴 **`zmievsa/autograder` is archived, and this base publishes it on
`repos/foundations.md` with no flag** — on the shelf whose stated purpose is *the systems
an engagement starts from*. 🔵 It is corrected on that file in this pass. 🟢 **One run of
a new instrument, one real defect, in a shelf that recommends building on it — and no
`ls-remote` sweep, however wide, could ever have found it.**

## 🟢 `p361`'s discovery legs — what ranked search returns that function words could not

🔴 **The eight prescribed web legs returned, again, almost nothing this base does not
hold** (see `intel/market.md` for the regional detail and the two exceptions). 🟢 **The
index did.** Ranked by stars within education topics, it surfaced **17 addresses absent
from this entire corpus**, all verified below first-hand — liveness, default branch and
licence read from payload on **2026-10-21**.

🔵 **Why these were invisible to five passes of web search:** every one of them ranks
*inside* a topic (`ai-tutor`, `edtech`, `education`+`mcp-server`) and nowhere near the
top of a general query for "best open source education AI". Ranked search inside a
taxonomy is a different instrument from a search engine, and this base had been denied
it since `p355`.

### 🆕 Agent-skill tutors — the tier ranked search found and prose search could not

| Agent | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region | What it is |
| --- | --- | --- | --- | ---: | --- | --- |
| Exam Cram Coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | 🟢 **MIT** | `main/LICENSE` | **312** | APAC | Exam-prep tutor that teaches **from the client's own slides with page citations** and crops figures. 🟢 Anti-hallucination by provenance, not by prompt — the citation *is* the guard |
| algo-sensei | [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | 🟢 **MIT** | `main/LICENSE` | **293** | North America | DSA/interview mentor that gives **progressive hints instead of solutions**. The closest thing on these shelves to a deliberate-practice harness for CS training |
| Diagnostic tutor | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | 🟢 **MIT** | `main/LICENSE` | **249** | APAC | 🟢 **Diagnosis-first**: no mode menu, no commands — it decides the next teaching step and checks understanding. The pedagogy is the control flow |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 🟢 **MIT** | `main/LICENSE` | **194** | APAC | 🟢 **China civil-service exam prep** (行测/申论/面试) with a wrong-answer book. A *credential-bound* vertical — the shape a national certification engagement takes |
| MindTrain | [shigella520/MindTrain](https://github.com/shigella520/MindTrain) | 🟢 **MIT** | `main/LICENSE` | **126** | APAC | Knowledge-training platform with **pluggable schedulers** and optional Anki/FSRS. Java — rare on this shelf, and it matters for JVM-shop clients |

### 🆕 LMS and portal reach — new addresses, and one with no grant at all

| Agent | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region | What it is |
| --- | --- | --- | --- | ---: | --- | --- |
| Shiori | [kaorii-ako/Shiori-v1](https://github.com/kaorii-ako/Shiori-v1) | 🟢 **MIT** | `master/LICENSE` — 🔴 not `main` | **46** | APAC | Google Classroom sync + SRS + an MCP server. 🟡 The only **Google Classroom**-native study agent found with a payload grant |
| brightspace-d2l-mcp | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | 🟢 **MIT** | `main/LICENSE` | **31** | North America | D2L/Brightspace MCP that **reconciles against what was already submitted** — second Brightspace address on this base, and the one that models state |
| Skolverket-MCP | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP) | 🟢 **MIT** | `master/LICENSE` — 🔴 not `main` | **13** | **EMEA** | 🟢 **Sweden's national education agency (Skolverket) open data over MCP** — curriculum, schools and statistics. A *statutory* data source, which is the scarcest kind of row on this base |
| campus-cli | [alejooroncoy/campus-cli](https://github.com/alejooroncoy/campus-cli) | 🟢 **ISC** | `main/LICENSE` | **11** | **LATAM** | 🟢 **Peru — UPC Aula Virtual (Blackboard Learn)** over CLI + MCP. 🔵 **First ISC grant in this corpus** (permissive, BSD-family, functionally equivalent to MIT for a client deliverable) |
| eklavya | [ProjectAJ14/eklavya](https://github.com/ProjectAJ14/eklavya) | 🟢 **MIT** | `main/LICENSE` | **12** | APAC | Quizzes the developer on the code the agent just wrote — local knowledge graph, spaced repetition, optional commit gate. 🔵 Corporate-upskilling, not schooling |
| dev-coach | [UltimaPhoenix/dev-coach](https://github.com/UltimaPhoenix/dev-coach) | 🔴 **AGPL-3.0** | `main/LICENSE` | **5** | EMEA | Same category as `eklavya` and the licence is the opposite: 🔴 **AGPL — reaching it from a hosted client deliverable triggers source obligations.** Read it, don't embed it |
| canvas-mcp (plyght) | [plyght/canvas-mcp](https://github.com/plyght/canvas-mcp) | 🔴 **NO GRANT** | 🔴 none at 10 probed paths; `package.json` has **no `license` field**; the README's `## License` section says only *"uses permissive open-source dependencies"* | **14** | Not placed | 🔴 **Unusable.** A statement about *dependencies* is not a grant on the work. Shelved as the worked example of the distinction |

### 🆕 Curriculum data and content — including one grant spelled the British way

| Agent | Repo | Licence (payload) | Grant read at | ★ 2026-10-21 | Region | What it is |
| --- | --- | --- | --- | ---: | --- | --- |
| Oak open-curriculum ecosystem | [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 **MIT** | 🔴 **`main/LICENCE`** — and `main/LICENSE` **404s** | **8** | **EMEA** | 🟢 **England's Oak National Academy curriculum as API + SDK + MCP app.** Pairs with the `oak-curriculum-ontology` this base already holds: ontology for meaning, this for access |
| ordkort | [silicq/ordkort](https://github.com/silicq/ordkort) | 🔴 **AGPL-3.0** | `main/LICENSE` | **12** | EMEA | FSRS flashcards for 60 languages, offline, no sign-up. 🔴 AGPL — fine as a product to deploy, wrong as a component to embed |
| leap-mcp | [sid-thephysicskid/leap-mcp](https://github.com/sid-thephysicskid/leap-mcp) | 🟢 **MIT** | `main/LICENSE` | **14** | North America | Topic → explainer video with Manim (3Blue1Brown-style) animation over MCP |
| Phys-MCP | [BlinkZer0/Phys-MCP](https://github.com/BlinkZer0/Phys-MCP) | 🟢 **MIT** | `main/LICENSE` | **10** | North America | Physics CAS/calculator over MCP — the subject-specific **tool** an agent calls instead of doing arithmetic in tokens |

🔵 **Read the `Grant read at` column, again.** Of the 17 addresses added this pass,
**3 do not put their grant where a tool would look**: two sit on `master` while the
ecosystem default is `main`, and Oak National's is spelled **`LICENCE`** with
`LICENSE` returning 404. 🔴 **A scanner that probes `main/LICENSE` and stops would report
all three as grantless — and one of them is a national curriculum body.**


---

## Tutoring and learning agents

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **41 972** | APAC | Agent-native tutoring with lifelong memory. Published by HKU Data Science lab (Hong Kong) |
| book-to-skill | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | MIT (`LICENSE.md`) | `master/LICENSE.md` | **35 553** | Not placed | Turns a technical book PDF into a Claude Code skill — ready to study, reference and use |
| PageLM | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **"PageLM Community License" — NOT open source** (8 563 B), corrected `p362` | `main/LICENSE.md` | **2 035** | Not placed | Community NotebookLM: course material → quizzes, flashcards, study guides. 🔴 **Non-commercial only, plus a revenue-sharing requirement for any commercial use, applying to the software *"in whole or in part"*.** Unusable in paid work. 🔵 The classifier's `NOASSERTION` was right and the cell that called this *"stock MIT"* was wrong |
| get-it | [beltromatti/get-it](https://github.com/beltromatti/get-it) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **1 125** | EMEA | "Read it. See it. Get it." multimodal explainer, built at GDG AI Hack Milan 2026 (Italy) |
| education-agent-skills | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **CC-BY-SA-4.0** (`LICENSE`) | `main/LICENSE` | **886** | EMEA | 165 evidence-grounded skills for teachers, school leaders and EdTech builders (UK). 🟡 Content licence, share-alike — not a code grant |
| educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT (`LICENSE`) | `main/LICENSE` | **387** | APAC | Course generation from source material incl. YouTube → structured course (India) |
| frametell | [sitor-ai/frametell](https://github.com/sitor-ai/frametell) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **357** | Not placed | Idea or source material → explainer video, driven by an AI director agent |
| Skill-Anything | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT (`LICENSE`) | `main/LICENSE` | **339** | APAC | Any source (PDF, video, web, audio, text) → interactive learning package with quizzes and flashcards |
| claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT (`LICENSE`) | `main/LICENSE` | **346** | Not placed | Open alternative to Udemy/Coursera: give it a topic, it researches and builds the course |
| ai-shifu | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 (`LICENSE.txt`) | `main/LICENSE.txt` | **327** | APAC | AI-led teaching and Q&A driven by typing; Chinese-language project |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT (`LICENSE`) | `main/LICENSE` | **290** | APAC | Private AI tutor that reads how a learner actually learns and sequences the next lesson |
| deep-student | [helixnow/deep-student](https://github.com/helixnow/deep-student) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **286** | Not placed | Local-first open AI learning workbench |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT (`LICENSE`) | `main/LICENSE` | **268** | North America | Open intelligent tutoring system with Bayesian Knowledge Tracing mastery. UC Berkeley CAHLR |
| learn-anything-with-AI | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | MIT (`LICENSE`) | `main/LICENSE` | **201** | Not placed | Reusable AI learning skill for project-driven mastery of a subject |
| freelingo | [artcc/freelingo](https://github.com/artcc/freelingo) | AGPL-3.0 (`LICENSE`) | `main/LICENSE` | **196** | EMEA | Self-hosted AI language learning with local or cloud LLMs, CEFR-aligned (Spain) |
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
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **302** | Not placed | Canvas LMS |
| moodle-mcp | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **1** | Not placed | Moodle |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT (`LICENSE`) | `main/LICENSE` | **53** | Not placed | Tutor (Open edX distribution) |
| openedx-mcp | [blend-ed/openedx-mcp](https://github.com/blend-ed/openedx-mcp) | **AGPL-3.0** (`LICENSE`, branch `master`) | `master/LICENSE` | **2** | Not placed | Open edX. 🔴 Copyleft — the only non-permissive row on this tier |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT (`LICENSE`) | `main/LICENSE` | **525** | Not placed | Anki spaced repetition |
| classroom-mcp | [sandraschi/classroom-mcp](https://github.com/sandraschi/classroom-mcp) | MIT (`LICENSE`, branch `master`) | `master/LICENSE` | **1** | Not placed | Google Classroom |
| canvas-lms-agent | [likr/canvas-lms-agent](https://github.com/likr/canvas-lms-agent) | MIT **at depth** — `canvas-lms-mcp/LICENSE` | `master/canvas-lms-mcp/LICENSE` | **0** | Not placed | Canvas. 🔴 Repository **root carries no grant**; the MIT text licenses the `canvas-lms-mcp` package, not the repository |
| mcp-brasil | [Mcp-Brasil/mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) | MIT (`LICENSE`) | `main/LICENSE` | **1 820** | **LATAM** | Brazilian public-data MCP; education datasets among them |
| 🆕 canvas-lms-mcp | [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | MIT (`LICENSE`, holder *Christian Bru*, 2026) | `main/LICENSE` | **10** | Not placed | Canvas. TypeScript. **The widest Canvas surface verified on this base — its README states 183 tools**; reads courses, assignments, submissions, rubrics and quizzes, and **grades and comments** |
| 🆕 moodle-mcp (Rust) | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT (`LICENSE`, holder *G36maid*, 2026) | `main/LICENSE` | **21** | Not placed | Moodle. **Rust**, published to `crates.io`, CI + Codecov in-tree. Goes beyond reading: uploads and submits work. README claims validation against Moodle 3.7–5.x |
| 🆕 canvas-lms-student-mcp | [AnonymousOnyx22/canvas-lms-student-mcp](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp) | MIT (`LICENSE`, 2026) | `main/LICENSE` | **0** | Not placed | Canvas, **read-only by construction** — 12 tools, cannot submit, edit or delete. 🟢 The only row on this tier whose *capability ceiling* is the safety argument |
| 🆕 gradescope-mcp | [Yuanpeng-Li/gradescope-mcp](https://github.com/Yuanpeng-Li/gradescope-mcp) | MIT (`LICENSE`, holder *Yuanpeng Li*, 2026) | `main/LICENSE` | **8** | Not placed | **Gradescope** — 34 tools: course management, batch grading, rubric CRUD. 🟢 **Every write tool is preview-first** and refuses to mutate without `confirm_write=True`. The first grading-capable row on this base whose safety argument is a *protocol*, not a ceiling |
| 🆕 elimu-mcp | [gabrielmahia/elimu-mcp](https://github.com/gabrielmahia/elimu-mcp) | MIT (`LICENSE`, holder *Gabriel Mahia*, 2026) | `main/LICENSE` | **0** | **EMEA** (Kenya) | Kenya's education system — school registry, KCSE/KCPE results, HELB loans, TVET programmes. 5 tools, on PyPI. 🔴 Read the two caveats below before quoting it to a client |
| 🆕 Canvas-Agent | [hughsibbele/Canvas-Agent](https://github.com/hughsibbele/Canvas-Agent) | MIT (`LICENSE`, holder *Hugh Koeze*, 2026) | `main/LICENSE` | **1** | Not placed | Canvas. A sixth independent Canvas address — the platform is now **over-supplied** on this tier, which is itself the finding |
| 🆕 moodle-cli-hku | [Neutralmilkzzz/moodle-cli-hku](https://github.com/Neutralmilkzzz/moodle-cli-hku) | 🟢 **MIT** (`LICENSE`) | `main/LICENSE` | **0** | **APAC** | Moodle. **A fourth Moodle row, and the most maintained one on this tier: 356 commits (`--no-merges` 301), 5 authors (`%ae`), 2026-03 → 2026-10-08.** 🔴 **Corrected `p362`: the published `344 commits, 4 authors` re-derives as neither** — 4 is the `%an` figure and one of the 5 addresses is `noreply@anthropic.com` (10 commits). Gives an agent deadlines, grades, course files and forum search. 🟡 **Read-only for remote use** by the author's own statement — the capability ceiling is the safety argument, as with `canvas-lms-student-mcp` |
| 🆕 moodle-ai-assistant | [microsoft/moodle-ai-assistant](https://github.com/microsoft/moodle-ai-assistant) | 🟢 **MIT** (`LICENSE`) | `main/LICENSE` | **5** | Not placed | Moodle. An **accelerator** for deploying an AI agent on Moodle, published in the **`microsoft`** organisation; its `local_aichat` component is `0.1.0`, **self-described alpha**. 🔵 Already carried on these shelves; re-verified first-hand at `p359` |

### 🟢 The Moodle connector gap closed this pass, and the row that looks like it closed it is the one to avoid

🔴 **A trade comparison in this pass's leg states plainly that "the Moodle options are
much thinner than the Canvas ones."** That was true of this base: one Moodle row
(`falkenslab/moodle-mcp`) against five Canvas addresses. 🟢 **It is now three Moodle
rows,** and the second-most prominent Moodle server in the leg is on the licence-flag
table instead of this one:
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)
calls itself open-source in its own README and its payload is **AGPL-3.0**.

🔵 **Why that matters more on this tier than on any other.** An MCP server is not a
library a client links — it is a **service the client's agent talks to over a network
socket**. AGPL's network clause is triggered by exactly that shape. A copyleft LMS
*platform* can be held at arm's length by reaching it over LTI or web services, which is
the rule governing every pattern on `compose/patterns.md`; a copyleft *connector* sits
**on the engagement's own side of that boundary**. 🟢 Of the three Moodle rows, the two
permissive ones are `falkenslab/moodle-mcp` (Node) and `G36maid/moodle-mcp` (Rust).

### 🔴 `elimu-mcp` is the first African row on this base, and its own README disqualifies it from the use it looks built for

🟢 It is MIT, live, published to PyPI, and it is the **only national-education-system
connector on this base for any African country** — Kenya's school registry, the KCSE and
KCPE examination results, HELB student loans and TVET programmes, behind five MCP tools.
🔵 On the closed region vocabulary that is **EMEA**, and it matters more than one row
usually would: see the regional note below.

🔴 **Two sentences in its own `README` decide how it can be used, and both are quoted
verbatim rather than paraphrased:**

> *"Feedback via GitHub Issues only — pull requests are not accepted."*

> *"Demo data is labeled DEMO and is not suitable for operational decisions."*

🔵 **Read those as two different kinds of cost.** The first is a **maintenance** cost:
MIT grants the right to fork, and the upstream will not take a patch back, so an
engagement that needs a fix owns a fork from the day it makes one. The second is the
serious one — **this is a connector shape, not a data source.** Quoting it to a Kenyan
client as a live registry integration would be wrong; what it supplies is the tool
surface and the schema, and the real credentials and endpoints are the engagement's to
obtain. 🟢 Stated here because nothing in the licence, the liveness or the star count
would ever have surfaced it: only reading the payload does.

## Assessment, integrity and learning analytics

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| Dolos | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT (`LICENSE`) | `main/LICENSE` | **353** | EMEA | Source-code plagiarism detection for programming assignments. Ghent University, Belgium |
| INGInious | [INGInious/INGInious](https://github.com/INGInious/INGInious) | **AGPL-3.0 — "most of the files"** (`LICENSE`) | `main/LICENSE` | **243** | EMEA | Secure automated exercise assessment. UCLouvain, Belgium. 🟡 The grant text itself scopes to *most* files — treat as mixed |
| pyedmine | [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT (`LICENSE`) | `main/LICENSE` | **82** | APAC | Educational data mining framework (knowledge tracing, exercise recommendation) |
| Ares2 | [ls1intum/Ares2](https://github.com/ls1intum/Ares2) | MIT (`LICENSE`) | `main/LICENSE` | **5** | EMEA | Automated grading / secure test execution. TU Munich chair of applied software engineering |
| pykt-toolkit | [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT (`LICENSE`) | `main/LICENSE` | **451** | APAC | Knowledge-tracing benchmark and model library |
| k12-teacher-skills | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **579** | North America | K-12 teacher skill pack |
| agent-skills | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **40** | North America | Education agent skills from Learning Commons |
| evaluators | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | **MIT for code**, stated in `LICENSE.md` prose | `main/LICENSE.md` | **86** | North America | Evaluators for educational AI output. 🟡 Split grant — the file is a licensing *statement*, not a stock licence |
| 🆕 OpenLRW | [jeffyding/OpenLRW](https://github.com/jeffyding/OpenLRW) | 🟢 **ECL-2.0** — Educational Community License v2.0 (`LICENSE`), Apache-2.0 with a narrowed §3 patent grant | `master/LICENSE` | **0** | **North America** | **The only address found that carries OneRoster *and* Caliper *and* xAPI in one learning-records warehouse.** 🔴 **92 commits, 2016-10 → 2018-01 — eight years stale**, and the GitHub topic page that surfaced it reports *"updated September 2025"*, which the commit channel refutes. 🔵 Shelved as a **schema reference**, not a dependency |

## 🆕 LATAM-origin agents — this base's first shelvable tier from the region

🟢 **New tier, `p358`, and it ends a three-pass absence.** `p356` called the LATAM hole a
supply gap, then refined it to a **tooling** gap; `p357` ran no LATAM leg at all and said
so. 🟢 **Both diagnoses were wrong, and the correction is in the next section: the tooling
exists in volume. Almost none of it is licensed.** These are the rows that are.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| 🆕 TutorIA | [LabSirius/TutorIA](https://github.com/LabSirius/TutorIA) | MIT (`LICENSE`, holder *Grupo Sirius*, 2026) | `main/LICENSE` | **0** | **LATAM** (Colombia) | 🟢 **The best-placed LATAM row on this base.** Autonomous tutor agent for **rural** higher education in Risaralda, built at Universidad Tecnológica de Pereira — **integrated inside Open edX**, Claude API as the language engine, TTS replies, animated avatar, teacher statistics panel, context persisted across sessions. Ships against real courses: Programación I (Python) and Introducción a la Matemática |
| 🆕 OpenPiar | [Dramoscuello/openpiar](https://github.com/Dramoscuello/openpiar) | **AGPL-3.0** (`LICENSE`) | `main/LICENSE` | **2** | **LATAM** (Colombia) | Manages the **PIAR** — *Plan Individual de Ajustes Razonables* — for students with disabilities or specific learning disorders, and emits the documents Colombian law requires. An AI pedagogical assistant proposes DUA adjustments from the student profile, the institution's PEI, the subject and the teacher-declared barriers. 🔴 Network copyleft |
| 🆕 OpenTest | [Riskbreaker2077/open-test](https://github.com/Riskbreaker2077/open-test) | MIT (`LICENSE`, holder *Camilo Moreno*, 2026) | `main/LICENSE` | **0** | Not placed (Spanish-language) | Classroom assessment on a **local server with no internet**: the teacher runs it on a laptop, tablets join over the school intranet, and **every student gets a different paper** — questions drawn at random from a shared bank, answer options shuffled. Node ≥22, `better-sqlite3`, vanilla JS, Windows installer, v1.8.1 |

🟢 **`OpenPiar` is the most regulation-grounded row on this entire base.** Its `readme`
cites the instruments it implements — **Decreto 1421 de 2017** (which makes the PIAR
mandatory for educational provision to people with disabilities), **Ley 2216 de 2022**
(inclusive education for specific learning disorders — dyslexia, ADHD, dyscalculia) and
**Decreto 1860 de 1994**. 🔵 That is the shape a public-sector engagement can actually be
sold against: not "AI for inclusion" but *the document this decree obliges you to
produce*. 🔴 Its AGPL-3.0 means the engagement deploys it for the client rather than
folding it into a product.

🔴 **A filename defect on the same row, in the class this base already tracks.** Its
README is at **`readme.md`**, lower-case, and `README.md` **404s**. That is the
`COPYING.txt` / `license.txt` lesson from `repos/foundations.md` one file over: a
successor whose reader assumes `README.md` will publish this project as undocumented
when it is the best-documented LATAM row here.

🟡 **`OpenTest` is deliberately left unplaced.** Its documentation, its UI and its
`LICENSE` holder are Spanish; no institution domain, national curriculum or
timezone evidence places it, and Spanish-language is **not** evidence of LATAM over
Spain. 🔴 A first attempt to place it by grepping country and curriculum markers
returned `9 × "men"` and `2 × "sep"` — both **substring hits inside ordinary Spanish
words**, not references to Colombia's MEN or Mexico's SEP. The instrument was wrong
before the answer was; the row stays `Not placed`.

## 🆕 Memory and scheduling agents — the layer that decides *when*, not *what*

🟢 **New tier, `p356`.** A `topic:spaced-repetition` leg returned **40 repositories**
and a coherent technical layer this base had measured and never shelved: agents whose
contribution is **scheduling the next review**, not generating content. The sector has
a de-facto standard — **FSRS**, the Free Spaced Repetition Scheduler — and it is MIT
at every rung, which makes it one of the cleanest things on this shelf to embed.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| Echo-Loop | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | **AGPL-3.0** | `main/LICENSE` | **4 226** | APAC | AI English listening/speaking trainer: intensive listening, shadowing, blind listening, retelling, spaced review. 🔴 Network copyleft |
| FSRS4Anki | [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT (`LICENSE`) | `main/LICENSE` | **4 111** | Not placed | The FSRS scheduler as an Anki add-on. Its own topics name `intelligent-tutoring-system` |
| engram | [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | MIT (`LICENSE`) | `main/LICENSE` | **1 457** | Not placed | Free-recall verification *with receipts* + FSRS scheduling; ships as an agent plugin |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT (`LICENSE`) | `main/LICENSE` | **1 116** | APAC | AI study partner: plans the route, teaches, builds a project alongside the learner |
| trane | [trane-project/trane](https://github.com/trane-project/trane) | **AGPL-3.0** | `master/LICENSE` | **848** | Not placed | Deliberate-practice engine over a mastery dependency graph (Rust). 🔴 Network copyleft |
| FSRS (the algorithm) | [open-spaced-repetition/free-spaced-repetition-scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) | MIT (`LICENSE`) | `main/LICENSE` | **729** | Not placed | The DSR-model specification itself — the thing to implement against |
| human-skill-tree | [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 🟡 **AGPL-3.0 notice + MIT for `skills/`** | `master/LICENSE` | **575** | APAC | 30+ skills from K-12 to career, built on cognitive science. 🟡 Split grant — see the flags below |
| py-fsrs | [open-spaced-repetition/py-fsrs](https://github.com/open-spaced-repetition/py-fsrs) | MIT (`LICENSE`) | `main/LICENSE` | **514** | Not placed | The embeddable Python scheduler. **This is the row to build on** |
| learn-anything | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | MIT (`LICENSE`) | `main/LICENSE` | **488** | Not placed | Recursive learning: Socratic deep-dives plus TDD-style exercises inside a coding assistant |
| learn-faster-kit | [hluaguo/learn-faster-kit](https://github.com/hluaguo/learn-faster-kit) | MIT (`LICENSE`) | `main/LICENSE` | **392** | Not placed | Learning coach: personalised syllabus, spaced repetition, progress tracking |

🔵 **Why this tier is worth more than its star counts.** Every tutoring agent on the
shelf above decides *what* to teach next and almost none decides *when* to return to
it. Retention is the outcome a client measures. [`py-fsrs`](https://github.com/open-spaced-repetition/py-fsrs)
(MIT) is a few hundred lines with a published algorithm behind it, and it drops into an
existing tutor without touching its content pipeline — see `compose/patterns.md`
Pattern 10.

## 🆕 Vernacular assessment agents — the EMEA and APAC analogue of the LATAM tier above

🟢 **New tier, `p360`, and it is the LATAM tier's method applied to two more languages.**
`p358` built the section above from Spanish and Portuguese **function words** aimed at
`github.com`. `p360` ran the same method in **French** and **Indonesian** to discharge
`ACTION ZZ-bf`. 🔴 **The headline is on `agents/trending.md` and it is a refutation**: the
grant rates come out at **31 %** (French) and **15 %** (Indonesian) against LATAM's 23 %,
so licence hygiene is **not** a regional property. These are the rows that carry a grant.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| 🆕 Ujian Sekolah | [naufaldi/teacher-exam](https://github.com/naufaldi/teacher-exam) | 🟢 **MIT** (holder *Naufaldi Rafif*) | `main/LICENSE` | **21** | **APAC** (Indonesia) | 🟢 **The best-benched row this pass: 435 commits, 4 authors (`%ae`), last 2026-10-14, live deployment.** 🔵 Re-derived `p362`, exact — and the row where `%an` (5) runs **above** `%ae` (4). One sentence — *"PPKn kelas 5, sumatif tengah semester, sila ke-3, 20 soal"* — becomes an **A4 print-ready exam**: mixed item types, answer key, and a teacher-facing *pembahasan* for every question, bound to **Kurikulum Merdeka** CP/TP by a "Penjaga Kurikulum" review step. React 19 + Effect-TS + Effect HttpApi. 🔴 **Core generation calls a hosted proprietary model** — the orchestration and the curriculum binding are reusable, the generator is not self-hostable |
| 🆕 EvalStudio | [ajjalti/EvalStudio](https://github.com/ajjalti/EvalStudio) | 🟡 **AGPL-3.0** | `main/LICENSE` | **0** | **EMEA** (French-language) | Exam authoring plus **computer-vision marking of scanned paper copies** — the half of assessment this base otherwise reaches only through digital-first tools, and the half most of the world's classrooms actually run on. 31 commits, 3 authors (`%ae`). 🔴 Network copyleft |
| 🆕 Open Quiz | [guillaume-behr/open-quiz](https://github.com/guillaume-behr/open-quiz) | 🟢 **MIT** (holders *Guillaume Behr · Théo Willem*) | `master/LICENSE` | **1** | **EMEA** (French-language) | Self-hostable quiz platform: teachers author, students sit, MCQ auto-marked and written answers routed to a human, with re-runnable practice banks. 240 commits, 5 authors (`%ae`). 🔵 **9 commits from `anthropic.com`** — the first row this base has shelved where the agent-assisted bench is visible in the commit channel |
| 🆕 Révision CEB | [nvaes/CEB](https://github.com/nvaes/CEB) | 🟢 **MIT** (holder *Nicolas Vaes*) | `main/LICENSE` | **0** | **EMEA** (🇧🇪 Belgium) | Splits the **official CEB** past papers — *Certificat d'Études de Base*, the Belgian end-of-primary examination — into individual items. 🟢 **Auto-marks only the checkbox items and says so, on the stated grounds that automatic marking of free text would be unreliable** — a more honest integrity posture than several better-funded rows on this shelf. 🟡 Thin bench: 5 commits, 1 author (`%ae`). 🟢 Placed on the `nvaestech.be` commit domain — a **ccTLD is the strongest placement channel used this pass** |
| 🆕 Tournesol scolaire | [diego-costanzo/tournesol-scolaire](https://github.com/diego-costanzo/tournesol-scolaire) | 🟢 **MIT** (holder *Diego Costanzo*) | `main/LICENSE` | **0** | **EMEA** (French / Italian curriculum) | *Cahier de textes* plus timetable and active revision, **zero-cloud and local-only by design** — the privacy posture a European school procurement asks for, from CM1 to the *Maturità*. 🔴 Thin: 8 commits, 1 author (`%ae`), last 2026-09-25. 🟡 **Placed from curriculum vocabulary alone** — the author's commit email is anonymised, so this is the weakest placement on the tier and is marked as such |

🔴 **Twelve live addresses from the same two legs carry no grant at all.** Named rather
than counted, because the fix is one file and it is not Globant's to make — for any one of
these, asking costs an email: `olibertrand/questionnapp`, `EDUQUEST2026-2027/EDUQUEST`,
`ProfFranco/check-app`, `quizbankorg/quizbank`, `Bendjou-art/Correct-QCM`,
`Solemntumult/EcoGes`, `NZOKOS06/gestion_school`,
`Emmanuel26-code/cahier-texte-numerique` (🔴 and its own description claims *"IA
intégrée"* — an AI-integrated lesson log with no licence), `kbma/gestion-scolaire`,
`mael12854/preau`, `twakew/e-rapor`, `nwmustofa/e-rts`.

🟢 **Two carry an agent session branch as their default ref** — `agnesmuthia/agnes_SKB2027`
on `claude/skb-physics-teacher-app-dxd1m3` and `Dirmankhan/latihan` on
`claude/admiring-galileo-1x383z`. 🔵 Read as a maturity signal, that is an agent session
nobody merged; read as a tooling hazard, it is the default-ref trap in a new shape.

### 🔴 The licensor anomaly, second species: the holder is a framework vendor and there is no upstream at all

🟢 **`p359` opened this class** with copies whose MIT names an upstream's holder —
`NelsonSpencer/canvas-mcp` naming Vishal Sachdev. 🔴 **`p360` found the shape that has no
upstream relationship whatsoever.**

| Address | Grant | Holder line | Verdict |
|---|---|---|---|
| 🆕 [`kinoarizu/ThisRaport`](https://github.com/kinoarizu/ThisRaport) | clean **MIT**, `master/license.txt` | 🔴 `Copyright (c) 2014 - 2019, British Columbia Institute of Technology` | 🔴 **grant-unresolved** — that is **CodeIgniter's** licence file |

🔴 **Every automated check returns green**: the path exists, the title line reads *The MIT
License (MIT)*, the family is OSI-permissive. 🔴 **And the named licensor wrote none of the
application** — a *framework dependency's* grant was shipped as the repository's own, so
the author's own code is arguably unlicensed. 🟢 Only the **holder line** catches it, the
field `ACTION ZZ-be` exists to key on.

🔵 Registered as **`ACTION ZZ-bj`**: when a holder line names a known framework or
foundation (BCIT/CodeIgniter, the Free Software Foundation, the Apache Software
Foundation) rather than any plausible author of the repository, grade the row
**grant-unresolved** rather than permissive. 🔴 *Refuted if no further row on these
shelves changes grade under that rule.*

🔴 **And the same channel has a worse failure on GPL-family rows.** `p359` recorded that
the holder comparison goes **blind** on Apache-2.0, whose boilerplate carries no holder.
🔴 **On AGPL-3.0 it does not go blind, it goes wrong:** six rows this pass returned
`Free Software Foundation, Inc. <http://fsf.org/>`, because the GPL text carries the FSF's
copyright on the *licence document* ahead of any project notice. 🔴 A comparison keyed
naively on that string reports **every AGPL row in this corpus as a copy of every other
one** — across the largest licence family on these shelves. 🟢 The fix is to skip the
licence document's own copyright line and read the project notice instead; folded into
`ACTION ZZ-be`, because it is the same instrument.

## 🆕 Item banks and rubric-bound grading

🟢 **New tier, `p356`,** from a `gradebook OR "question bank" OR "item bank"` leg. The
AI-native item bank — import a Word file or a photograph of a page, recognise the
formulae, match the knowledge point, generate the worked solution — is a real product
category and it is **almost entirely Chinese-language**.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| math-question-bank | [JudgePeach/math-question-bank](https://github.com/JudgePeach/math-question-bank) | **AGPL-3.0** | `main/LICENSE` | **332** | APAC | High-school maths item bank: live LaTeX rendering, LLM parsing and solving, formula OCR. 🔴 Network copyleft |
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
| 🆕 exam-proctor | [shaheeranser/exam-proctor](https://github.com/shaheeranser/exam-proctor) | 🟢 **Apache-2.0** (`LICENSE`) — grant published here for the first time at `p359` | `main/LICENSE` | **0** | **APAC** — `+0800`/`+0500` | 🟢 **The only proctoring address on this base that is an LTI 1.3 tool** — launches from inside Moodle, authors quizzes, passes grades back over AGS. 🔴 25 commits, **1 author**. 🔴 **Reference architecture only:** `p190` read its source — head pose, iris deviation, `face-api` identity → **GDPR Art. 9**, and clear of the **Art. 5(1)(f)** prohibition *by one unset MediaPipe default*. See `verticals/solutions.md` |
| 🆕 openproct | [OpenProct/openproct](https://github.com/OpenProct/openproct) | 🟢 **MIT** (`LICENSE`) | `main/LICENSE` | **2** | **APAC** | Self-hosted, privacy-first proctoring. 🔴 **4 commits, nothing since 2025-10-26** — read the maintenance note below before planning on it |

🔵 **The usable integrity story is not in this table.** Of five rows, one has no grant,
one has no identified licensor, and two are AGPL plugins to AGPL hosts. The row a
studio can actually ship on is [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos)
(MIT) on the shelf above — detect what the submission *is*, rather than surveil the
student taking it. That is a defensible recommendation and it is now evidence-backed.

#### 🟡 `p359`: the integration gap closed, the maturity gap did not, and one row looks like the answer

🔵 **There is no grant hole on this tier — `Gap 344` claimed one and `P131-D` refuted it
with four MIT rows, leaving a *maturity* gap. `p359` does not revive the licence claim.**

🟢 **What `p359` adds that is genuinely new is a grant and an integration shape.**
`shaheeranser/exam-proctor` — read as *source* by `p190` and never shelved — is
**Apache-2.0**, published here for the first time, **and an LTI 1.3 tool**, so it reaches
a GPL host across the protocol boundary, which none of `P131-D`'s standalone MIT web apps
can do. 🔴 **It is also one author and 25 commits**, so the maturity gap stands exactly
where `P131-D` left it: every permissive proctoring address on this base is one person's
project.

🔴 **And its licence is not its binding constraint, which is why `p190` left it off the
shelf.** Head pose, iris deviation and a `face-api` identity check mean **GDPR Art. 9**,
and it clears the **Art. 5(1)(f)** prohibition only because MediaPipe's
`outputFaceBlendshapes` is unset and defaults to `false` — **one line from a live
prohibition at EUR 35 M or 7 % of turnover.** 🟢 `p359` shelves it as a **reference
architecture with that tripwire in the row**, rather than leaving a verified Apache-2.0
LTI proctoring tool invisible to the next engagement. Full note on
`verticals/solutions.md`.

🟡 **And the second new row is a trap worth naming.** `OpenProct/openproct` looks like
the institution-backed answer the maturity gap is waiting for — stock MIT at
`main/LICENSE`, under an organisation account, positioned in its own README as a
self-hosted privacy-first alternative to the commercial proctoring vendors. 🔴 **And the
commit channel says it is a shell:** **4 commits, 2 authors (`%ae`), every one of them on
2025-10-26**, streams `+0530` and `+0000`. 🔴 **Nothing in the year since** — so the
secondary post that reported its activity as *"last recorded October 2025"* was right,
and the inference a reader draws from an org account plus a 2025 date is wrong.

🔵 **Both halves have to be published together.** A successor searching this tier for a
permissive row will find this one and stop, because MIT under an org account is exactly
the shape that ends a search. 🟢 **The recommendation does not change:** `dolos` (MIT)
for what the submission *is*, and `p359`'s addition to the exclusion list is not a
licence — it is a repository with four commits wearing an organisation's name.

## 🔴 🆕 Special education and IEP — a whole tier, and the worst-licensed one this base has measured

🟢 **This is a tier, not a row.** Two function legs — `IEP special education agent` and
`individualized education program open source` — returned **seven addresses, all seven
live, all seven absent from this corpus**. 🔵 That matters because the base has been
here before and got it wrong in the other direction: the claim this base files as
`T-p288b` was *"zero permissive for special education"*, and these shelves already
record it **CORRECTED** by **one row**: [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents)
is MIT and ships a `special-education-agent` among twelve specialists. 🔴 **The other
special-education row this base holds,
`eakarsu/ai-special-education-iep-compliance`, carries no grant in 21 files — re-confirmed
at `p359`** — so the corrected claim rests on a single permissive address, and `p359`'s
seven findings add exactly one more. 🟢 **So the claim below is
scoped to the seven addresses `p359` measured, not to the tier as a whole** — the base
already holds permissive special-education rows and they still stand.

| Agent | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | What it does |
| --- | --- | --- | --- | ---: | --- | --- |
| 🆕 iep-system | [dg13788/iep-system](https://github.com/dg13788/iep-system) | 🟢 **MIT** (`LICENSE`) | `main/LICENSE` | **1** | **APAC** | **The only permissive row on this tier.** Chinese-language IEP management for special-education schools: student records, assessments, a five-step IEP wizard, e-signatures. React / PHP / MySQL. 38 commits, 4 authors (`%ae`), `+0800` on all 38 |
| 🆕 a-iep | [The-Burnes-Center/a-iep](https://github.com/The-Burnes-Center/a-iep) | 🔴 **CC-BY-NC-4.0 — NonCommercial** (`LICENSE`) | `main/LICENSE` | **3** | **North America** | Serverless app that helps **parents** understand their child's IEP: OCR, multilingual translation, plain-language simplification. 1 281 commits, 12 authors (`%ae`), 2025-05 → 2026-10-14 — 🔴 **corrected `p362`; the published `836 / 7` re-derives under no convention** — 🟢 **by far the most maintained row on this tier** and 🔴 the one a paid engagement cannot touch |
| 🆕 special-education-rag (EduRAG) | [omerpanay/special-education-rag](https://github.com/omerpanay/special-education-rag) | 🔴 **no grant** — nothing at 7 probed paths | `main/` — none found | **0** | **EMEA** | Agentic teacher assistant with **IEP draft generation** over a RAG pipeline. 19 commits, 1 author (`%ae`), `+0300` on all 19 (Türkiye) |
| 🆕 IEP Ally | [boktoday/iep-agent-hermes-agent](https://github.com/boktoday/iep-agent-hermes-agent) | 🔴 **PolyForm Noncommercial 1.0.0** (`LICENSE`) | `main/LICENSE` | **0** | **APAC** | Local-first IEP **planning agent for parents**, built on Hermes Agent. 60 commits in a single day, `+1100` (Australia). 🔴 Second PolyForm row on this base after `mrgutierrezmario/lecture-note-app` |
| 🆕 SUMRY | [sumry-app/SUMRY](https://github.com/sumry-app/SUMRY) | 🔴 **no grant — and the README carries an MIT badge** (see flags) | 🔴 `main/` — none found | **0** | 🟡 Unplaceable | AI-assisted IEP platform: goal tracking, progress data. React / Supabase. 66 commits, 2 authors (`%ae`); stream splits `+0000`×38 / `-0600`×26, so the commit channel **cannot** place it |
| 🆕 IEP GEN | [JeabtiE/jump-hackathon-demo](https://github.com/JeabtiE/jump-hackathon-demo) | 🔴 **no grant** — nothing at 7 probed paths | `main/` — none found | 🔴 **not measurable** — `p361`'s one index-invisible address | **APAC** | Generates IEP goals and a materials list against the Thai A-B (ก-ฮ) curriculum, exports to an official document. JUMP THAILAND Hackathon 2026. 108 commits, `+0700` on all 108 — 🟢 the commit channel corroborates the README's country |
| 🆕 Rapid-IEP | [Pragmatic-Works/Rapid-IEP](https://github.com/Pragmatic-Works/Rapid-IEP) | 🔴 **no grant** — nothing at 7 probed paths | `main/` — none found | **2** | **North America** | Power Apps IEP paperwork workflow for a district or state agency. 🔴 **15 commits, all inside four days in June 2023 — dead for three years.** Named so no successor promotes it |

### 🔴 The measurement, and why this tier is the one to quote it on

🔴 **One of seven carries a grant a Globant engagement can build on.** Two are
explicitly noncommercial — not "unclear", but *written down as noncommercial* — and
four have no licence file at any of seven probed paths, which under default copyright
means all rights reserved.

🔵 **Why this tier and not another.** Special education is the highest-stakes,
highest-compliance, most clearly underserved function in the whole industry: an IEP is
a **statutory document** in the United States under IDEA, and its analogues carry force
of law in most of the jurisdictions on `intel/market.md`. 🟢 **The demand is not in
doubt and the supply exists** — `a-iep` has 836 commits and seven authors behind it.
🔴 **What does not exist is a grant.** The two best-maintained addresses on the tier are
the two that are noncommercial by construction, and a studio that finds them, reads
"open source", and plans a deliverable around either one has a problem that surfaces at
contract review rather than at build time.

🟢 **The usable recommendation is therefore a build, not an adoption** — and it is
specific, because `dg13788/iep-system` is MIT and covers exactly the records-and-wizard
half. See 🆕 **Pattern 16** on `compose/patterns.md`, which wires it to the permissive
parts this base already holds rather than to anything on this tier.

🔵 **One address deliberately not shelved.** The leg also returned
`The-Burnes-Center/a-iep`'s nearest commercial analogues and a Wikipedia article; and it
returned `eakarsu/ai-special-education-iep-compliance`, which this base **already
holds**. Recorded so the yield figure above is not read as a seven-row tier where a
successor expects nine.

## Curriculum and knowledge layers (what the agents reason over)

An agent is only as good as the curriculum model behind it. These are the data
assets — and they are where the licence traps live.

| Asset | Repo | Licence (read from payload) | Grant read at | ★ 2026-10-21 | Region | Substance |
| --- | --- | --- | --- | ---: | --- | --- |
| os-taxonomy | [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | **ODbL-1.0** (`LICENSE`) | `main/LICENSE` | **6 898** | Not placed | Open subject/skills taxonomy. Share-alike binds a derivative *database*, not a produced work |
| cn-math-taxonomy | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC-BY-NC-4.0 — NonCommercial** (`LICENSE`) | `main/LICENSE` | **1 861** | APAC | China K-12 maths + English knowledge graph, 人教版/课标-aligned: 1 244 nodes, 5 123 items, adaptive diagnosis. 🔴 **Not usable in a paid client engagement** |
| knowledge-graph | [learning-commons-org/knowledge-graph](https://github.com/learning-commons-org/knowledge-graph) | **MIT code / data is per-dataset** (`LICENSE.md`) | `main/LICENSE.md` | **161** | North America | Instructional-content + research data layer. 🔴 Datasets are labelled Open, Open+Gated or **Gated**; Gated content is **not** under CC BY 4.0 or CC0. Check the licence per download |
| bncc-dados | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | MIT (`LICENSE`) | `main/LICENSE` | **22** | **LATAM** | Brazil's BNCC national curriculum as verified open data: 1 721 learning objectives in JSON, SQLite and CSV |
| knowledge-import-pipeline | [clownjee/knowledge-import-pipeline](https://github.com/clownjee/knowledge-import-pipeline) | Apache-2.0 (`LICENSE`) | `main/LICENSE` | **18** | APAC | China compulsory-education textbook → AI knowledge extraction, interactive KG, vector retrieval, prerequisite graph, MCP query service |
| polymath | [aclascollege/polymath](https://github.com/aclascollege/polymath) | **ODbL-1.0** (database) + **CC-BY-SA-4.0** (authored text) | `main/LICENSE` | absent from default index | APAC | Curriculum taxonomy: disciplines, courses, prerequisites, degrees, skills, careers. Placed APAC by commit stream (+08:00) |
| 🆕 oak-curriculum-ontology | [oaknational/oak-curriculum-ontology](https://github.com/oaknational/oak-curriculum-ontology) | 🟢 **OGL-3.0** (`ontology/`, `data/`, `docs/`) + **MIT** (`scripts/`, workflows) — both read at `LICENSE.md` | `main/LICENSE.md` | **20** | **EMEA** | Oak National Academy's curriculum as a formal **OWL/SKOS** ontology, aligned to the **National Curriculum for England**. v0.1.3, early release; CI validates the ontology and generates distributions. 🟢 **The data grant permits commercial exploitation on attribution alone — no share-alike** |
| 🆕 curriculum_knowledge_graph | [devissaputra/curriculum_knowledge_graph](https://github.com/devissaputra/curriculum_knowledge_graph) | MIT (`LICENSE`, 2026) | `main/LICENSE` | **0** | Not placed | **Typed** curriculum graph: `PREREQUISITE_OF`, `TEACHES`, `ASSESSES`, `ALIGNS_WITH`, with entity-type constraints enforced per relation. Alignment diagnostics, path analysis, provenance, expert-review workflow |

### 🟢 EMEA gets its national-curriculum ontology, and the grant is better than the one this base already recommends

🟢 **`p356` published §9 of `intel/trends.md` — "curriculum-as-open-data is the real
moat, and it is regionally lopsided."** The lopsidedness was specific: Brazil had
[`bncc-dados`](https://github.com/bncc-dev/bncc-dados) (MIT, the full BNCC), China had
[`cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) (🔴 but
NonCommercial, so unusable in paid work), and **EMEA had no national curriculum as
structured data at all.** It does now, and the licence is the finding:

| | `os-taxonomy` (the general skeleton) | 🆕 `oak-curriculum-ontology` |
|---|---|---|
| Data grant | ODbL-1.0 | 🟢 **OGL-3.0** |
| Commercial use | ✅ | ✅ |
| Share-alike on a **derivative database** | 🟡 **Yes** | 🟢 **No** |
| Obligation | publish the derived database under ODbL | 🟢 **attribution string only** |
| Aligned to a statutory curriculum | ✗ | 🟢 National Curriculum for England (2014) |

🔵 **The consequence is a build decision, not a licence note.** A client's enriched
curriculum graph derived from `os-taxonomy` is a derivative database and ODbL reaches
it. The same graph derived from Oak's ontology carries one sentence of attribution —
*"Contains public sector information licensed under the Open Government Licence v3.0"* —
and nothing else. 🟢 **For a UK or EU education engagement that must ship a closed
curriculum model, Oak is now the correct base and `os-taxonomy` is the fallback.**
🟡 Scope honesty: Oak covers **England**, and is `v0.1.3` / early release. It is not a
pan-EMEA asset and this base does not publish it as one.

---

## 🆕 Lecture capture and transcription — the tier `p356` could not measure

🟢 **`ACTION ZZ-bb` is discharged, and both legs returned shelvable rows.** `p356`
recorded that its `lecture capture` and `curriculum ontology` legs returned nothing
usable, diagnosed the cause as **its own query syntax** (an unparenthesised `OR`
dissolving each leg into general AI), and — correctly — **recorded the tier as
unmeasured rather than absent**, registering the re-run as `ZZ-bb`.

🟢 **The diagnosis was right.** Re-run this pass as single-term queries on a different
instrument, the `lecture capture` leg returned the rows below and the
`curriculum ontology` leg returned the two curriculum rows above. 🔵 **Neither leg was
empty; `p356`'s restraint in not publishing an absence is what preserved the finding.**

| Component | Repo | Licence (read from payload) | Grant read at | Region | What it does |
| --- | --- | --- | --- | --- | --- |
| LectureLab | [helalaou/LectureLab](https://github.com/helalaou/LectureLab) | 🟢 MIT (`LICENSE`, 2026) | `main/LICENSE` | Not placed | Transcribes a recording and generates notes, flashcards and quizzes. **Study-material generation, not capture or distribution** |
| lecture-live | [PLus123456/lecture-live](https://github.com/PLus123456/lecture-live) | **GPL-3.0** (`LICENSE`) | `main/LICENSE` | Not placed | Self-hosted live transcription + multilingual translation, AI summaries, Q&A, searchable notes. Docker Compose with MySQL, Redis, Cloudreve |
| Cap | [CapSoftware/Cap](https://github.com/CapSoftware/Cap) | 🟡 **split: AGPLv3 overall, MIT for the `cap-camera*` / `scap-*` crates** | `main/LICENSE` + `main/licenses/LICENSE-MIT` | Not placed | Open-source Loom alternative; self-hostable screen recording with shareable links |
| CaptureFlow | [sardorml/captureflow](https://github.com/sardorml/captureflow) | 🟡 **split: AGPL-3.0-only overall, MIT for `packages/engine/`** | `main/LICENSE` + `main/packages/engine/LICENSE` | Not placed | Self-hostable screen recording with instant shareable links, built for Cloudflare |

🔵 **Read the split grants correctly, because both splits point the same way.** In each
case the **capture engine is MIT and the surrounding product is AGPL**, and the authors
say so explicitly — CaptureFlow's own notice states that combined distributions built
from the repository are distributed under the AGPL. 🟢 **So the reusable asset is the
engine, not the app.** An engagement that vendors `packages/engine/` or the
`cap-camera*` crates takes MIT code; one that forks the repository takes AGPL.

🔴 **The most capable row in this leg is not on the table and cannot be.**
[`mrgutierrezmario/lecture-note-app`](https://github.com/mrgutierrezmario/lecture-note-app)
is the closest thing in the leg to an institutional capture platform — Whisper
speech-to-text, incremental AI note generation, Q&A over transcripts *and slides*,
FastAPI + React + PostgreSQL + Docker, pluggable Ollama/Claude/Gemini/OpenAI providers,
multi-user accounts and RBAC. Its payload is **PolyForm Noncommercial 1.0.0**: usable
for study, research, charities and hobby work, and **commercial use requires a separate
licence from the copyright holder**. It is on the licence-flag table.

🟢 **What the tier means for an engagement.** [`opencast/opencast`](https://github.com/opencast/opencast)
remains the only institutional-grade capture-*and*-distribution system on this base; the
rows above are **not** replacements for it. What they are is the transcription-and-notes
layer that sits on top of it, and three of the four have a permissive component.

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
| `PageLM` | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **PageLM Community License — non-commercial + revenue share** (corrected `p362`) | `main/LICENSE.md` |
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
| 🆕 [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | *"an open-source MCP server"* in its own README; a trade roundup repeats the phrase | 🔴 **AGPL-3.0** (`main/LICENSE`, full 34 kB text) | **Network copyleft on a connector.** The README also names it *"the Moodle connector behind CSMediaPro's broader Agentic Query Layer (AQL)"* and links a product page and an npm package — an open-core posture, not a permissive grant. Excluded from the MCP tier for this reason |
| 🆕 [mrgutierrezmario/lecture-note-app](https://github.com/mrgutierrezmario/lecture-note-app) | a self-hosted Whisper + AI-notes lecture platform, FastAPI/React/Postgres/Docker | 🔴 **PolyForm Noncommercial 1.0.0** (`main/LICENSE`) | **Not OSI open source.** Study, research, charities and hobby use only; *"commercial use requires a separate license from the copyright holder."* The most capable row in the lecture-capture leg and the one a paid engagement cannot touch |
| 🆕 [foradian/fedena](https://github.com/foradian/fedena) | a vendor comparison in this pass's leg states Fedena is **Apache-2.0**, Ruby on Rails | 🔴 **no grant, and no tree** — live on `master`, and `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license.txt`, `LICENCE`, `LICENSE-MIT`, `README.md` and `Gemfile` **all 404** | **The Apache-2.0 claim is unverifiable at this address.** The repository resolves but serves nothing at any standard path. 🔵 Published as a refutation so no successor promotes the comparison's claim into a row |
| 🆕 [naiayti/TeachingKG](https://github.com/naiayti/TeachingKG) | cited from a *Semantic Web* journal paper on educational knowledge graphs | 🔴 **no licence file** — live on `main` with a README and no grant at any of eight probed paths | **All rights reserved.** Schema covers courses, skills, prerequisites and learning goals, and none of it can be used. 🔵 Peer-reviewed provenance is not a grant |
| 🆕 [GSU-CETLOE/lti1p3Library-php](https://github.com/GSU-CETLOE/lti1p3Library-php) | stock MIT at `main/LICENSE`, published by a **university** (Georgia State CETLOE) | 🟡 **MIT whose holder line is the unfilled template**: `Copyright (c) 2026 [Your Name / Organization]` | **Family certain, licensor absent.** Covers the LTI 1.3 tool side — Deep Linking 2.0, AGS, NRPS, framework-agnostic — so it is *technically* the cleanest small LTI library found this pass. 🔴 There is nobody to attribute, and attribution is MIT's only condition. Second instance of this class after `lebmatter/exampro` |
| 🆕 [oat-sa/lib-lti1p3-deep-linking](https://github.com/oat-sa/lib-lti1p3-deep-linking) | an **IMS-certified** LTI 1.3 Deep Linking library from the OAT/TAO assessment vendor | 🔴 **GPL-2.0** (`master/LICENSE`, *"Version 2, June 1991"*) | **Strong copyleft on a library** — worse for an engagement than the LGPL it is easy to mistake for. Certification is a conformance claim, not a grant. Reach TAO over a protocol boundary or use a permissive LTI library instead |
| 🆕 [blackboard/BBDN-LTI-Tool-Provider-Node](https://github.com/blackboard/BBDN-LTI-Tool-Provider-Node) | a reference LTI tool provider in the **Blackboard** GitHub organisation | 🔴 **no grant** — live on `master`, nothing at any probed path | **All rights reserved.** 🔵 The hazard here is *provenance*: a repository under a named LMS vendor's org reads as the safest thing in the leg, and a vendor sample with no `LICENSE` is exactly as unusable as a student project with none |
| 🆕 [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | the most complete K-12 assessment architecture in this pass's legs — standards-aligned item authoring with RAG and self-review, rubric scoring with human review, tutoring agent with persistent memory, sandboxed code grading, evals and observability | 🔴 **no grant** — live on `main`, nothing at any probed path | **All rights reserved.** 🔵 Named because its *architecture* is worth reading as a reference even where its code cannot be used — it is the shape `compose/patterns.md` already recommends, published by someone else and unusable |
| 🆕 [adriasantacreu/google-classroom-mcp](https://github.com/adriasantacreu/google-classroom-mcp) | a Google Classroom MCP server covering assignment creation, rosters and grading | 🔴 **no grant** — live on `master`, nothing at any probed path | **All rights reserved.** 🔴 Keeps the Google Classroom tier at exactly one usable row (`sandraschi/classroom-mcp`, MIT) despite two addresses existing |
| 🆕 [Samkarya/online-exam-questions](https://github.com/Samkarya/online-exam-questions) | an open JSON item bank with a schema, LaTeX and Markdown support | 🔴 **CORRECTED `p362`: not MIT at all.** The payload (2 118 B) is titled **"ExamOven Non-Commercial Open Source License (ENCOSL), Version 1.0, April 2026"** | 🔴 **Not usable in paid work.** The operative sentence grants use *"for personal, educational, and non-commercial purposes"* only, and §2 prohibits commercial use **"for all parties EXCEPT for ExamOven ... and its authorized owners/affiliates"** — an asymmetric carve-out for the licensor. A pull request also assigns ExamOven a perpetual commercial licence to the contribution. 🔵 `p359` read the reserved-rights phrase in the copyright line and treated the rest as stock MIT; the narrowing is two lines above it |
| 🆕 **`p359`** [sumry-app/SUMRY](https://github.com/sumry-app/SUMRY) | an MIT **shields.io badge** at the top of the README, and a `## License` section reading *"MIT License - See LICENSE file"* | 🔴 **there is no LICENSE file** — `LICENSE`, `LICENSE.md`, `license.txt`, `app/LICENSE` and `docs/LICENSE` all **404** | **All rights reserved.** 🔵 The sharpest instance yet of §14 of `intel/trends.md`: this row does not merely *badge* a missing grant, it **instructs the reader to go and read a file that does not exist**. Second occurrence of the shape after `reneverland/CBIT-AiExam-plus`, and on an **IEP** platform |
| 🆕 **`p359`** [The-Burnes-Center/a-iep](https://github.com/The-Burnes-Center/a-iep) | a public-interest IEP tool from a university civic-innovation centre, **1 281 commits, 12 authors (`%ae`)** — corrected `p362` from the published `836 / 7`, which re-derives under no convention | 🔴 **CC-BY-NC-4.0 — NonCommercial** (`main/LICENSE`) | **Not usable in paid work.** 🔵 Provenance is not a grant: a civic-tech lab optimising for public benefit has every reason to pick NonCommercial, and that reason is exactly what excludes it from a studio engagement |
| 🆕 **`p359`** [boktoday/iep-agent-hermes-agent](https://github.com/boktoday/iep-agent-hermes-agent) | *"a free, local-first IEP planning agent for parents"* | 🔴 **PolyForm Noncommercial 1.0.0** (`main/LICENSE`) | **Not OSI open source.** *Free* in the README means free of charge, not freely licensed. 🔴 **Second PolyForm row on this base**, which makes §18's "noncommercial source-available build" a class rather than an instance |
| 🆕 **`p359`** [philchalmers/mirt](https://github.com/philchalmers/mirt) | the standard multidimensional IRT package in R, cited across the psychometrics literature | 🔴 **no `LICENSE` file at root; the grant is `License: GPL (>= 3)` in `DESCRIPTION`** | 🟢 **Usable, and copyleft.** 🔵 Two separate hazards in one row: the grant lives in a **language-ecosystem manifest** (the CRAN shape this base recorded at `ACTION RS`), and when found it is **GPL-3.0-or-later** — fine for analysis run beside a deliverable, wrong for anything linked into one |
| 🆕 **`p359`** [Joe-Hall-Lee/PSN-IRT](https://github.com/Joe-Hall-Lee/PSN-IRT) | **AAAI 2026 Oral** — IRT applied to LLM benchmarking | 🔴 **no grant** — nothing at 7 probed paths, `main`, 4 commits | **All rights reserved.** 🔵 Third instance on this base of peer-reviewed provenance without a grant, after `naiayti/TeachingKG` |
| 🆕 **`p359`** [mainlp/llm-psychometrics](https://github.com/mainlp/llm-psychometrics) | code for *"Do LLMs Give Psychometrically Plausible Responses in Educational Assessments?"*, from a named university NLP lab (MaiNLP, `+0200`) | 🔴 **no grant** — nothing at 7 probed paths, `main`, 4 commits | **All rights reserved.** 🔴 **With `PSN-IRT` and `mirt`, that is three of three psychometrics addresses `p359` probed carrying no usable permissive grant** — and psychometrics is the measurement layer every assessment claim on these shelves ultimately rests on |
| 🆕 **`p359`** [pedrosoale/tempo-docente](https://github.com/pedrosoale/tempo-docente) | Brazilian education data — BNCC, SAEB, SARESP — *"com fonte oficial"*, 51 commits, `-0300` on all 51 | 🔴 **no grant** — nothing at 7 probed paths | **All rights reserved.** 🔵 Published as the counter-example to its own neighbourhood: `bncc-dev` ships the same kind of Brazilian curriculum data under **MIT code + CC BY 4.0 data** with per-record provenance. 🟢 **The LATAM licensing gap `p358` measured is not a regional norm — it is a long tail beside one well-governed publisher** |
| 🆕 **`p359`** [SayvaBR/assistente-ped](https://github.com/SayvaBR/assistente-ped) | a Brazilian pedagogical assistant whose issue tracker is working on BNCC Computação provenance | 🔴 **no grant** — nothing at 7 probed paths, 6 commits on one day, `-0300` | **All rights reserved.** 🔵 Named because its **issue #24** is a public, dated record of a Brazilian team adopting `bncc-dev`'s provenance model — useful intelligence about the BNCC stack's uptake even though the repository itself is unusable |
| 🆕 **`p359`** [HernanDiaz/moodle-local_aigrader](https://github.com/HernanDiaz/moodle-local_aigrader) | *"AI Grader Pro"* — AI-assisted Moodle assignment grading, human always in the loop, 74 commits, `+0200` | 🟢 **GPL-3.0-or-later** (`main/LICENSE`) — the grant text, not a badge; the file also enumerates bundled third-party licences under `thirdparty/vendor/` | 🟢 **Correctly licensed and correctly excluded from the permissive tiers.** A Moodle plugin under GPL-3.0-or-later is the *expected* answer — Moodle itself is GPL-3.0 — so this row is here as a **recommendation shape**, not a warning: reach it as a plugin inside the client's GPL estate, never vendored into a studio deliverable |
| 🆕 **`p359`** [OpenProct/openproct](https://github.com/OpenProct/openproct) | stock **MIT** under an **organisation** account; a self-hosted privacy-first proctoring alternative | 🟢 **MIT is real** (`main/LICENSE`) — 🔴 **and the repository is 4 commits, 2 authors (`%ae`), all on 2025-10-26 — nothing in the year since** | 🟡 **Not a licence flag — a maintenance flag, filed here because it will be mistaken for one of these rows' opposite.** The grant is clean; there is no software behind it yet. 🔵 This base has no other category for *"permissive and empty"*, and the omission is how a successor ends up recommending it |
| 🆕 **`p359`** [jeffyding/OpenLRW](https://github.com/jeffyding/OpenLRW) | the one OneRoster + Caliper + xAPI warehouse found; a GitHub **topic page** reports it *"updated September 2025"* | 🟢 **ECL-2.0** (`master/LICENSE`) — permissive, Apache-2.0 with a narrowed patent grant — 🔴 **and the commit channel reads 2016-10-17 → 2018-01-16** | 🟡 **Grant fine, currency not.** 🔴 **The finding is the channel:** a topic page's "updated" date is not a commit date, and `p359` is the first pass on this base to catch that surface lying. Use the schema; do not deploy the code |

## 🔴 🆕 A new anomaly class: the grant is valid, the *licensor* is somebody else

🟢 **Every anomaly this base has recorded so far is a question about which licence
applies.** This one is not. The grant is a clean, unmodified MIT licence, read from the
payload, at the expected path. The defect is **whose name is in it.**

[`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp) is live on
`main` with MIT at `main/LICENSE`. The copyright line reads **`Copyright (c) 2025 Vishal
Sachdev`** — the holder of [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp),
a row this base has carried for passes. Read side by side, the two READMEs share the
header image path, the badge block, and this HTML comment:

```
<!--mcp-name: io.github.vishalsachdev/canvas-mcp-->
```

🔴 **That is the MCP *registry identifier*, and the copy publishes the original's.** Its
install line is `npx skills add vishalsachdev/canvas-mcp` — pointing at upstream.

🔴 **And it is stale, measurably.** Three addresses in this pass's leg describe the same
project at three different sizes:

| Address | Tools claimed | Agent skills |
|---|---:|---:|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — **upstream** | 🟢 **up to 126** | 8 |
| [`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp) — copy | 99 | 8 |
| a trade listing of "the most active option" | 🔴 80+ | 🔴 5 |

🔵 **Why this belongs on a shelf and not in a footnote.** A function-shaped search for
"Canvas MCP server" returns all three, and nothing in the *licence* channel separates
them: all three are MIT, all three are live, all three verify. The signal that separates
them is **the copyright holder and the registry identifier** — two fields this base
reads on every pass and had never compared *across* rows.

🟢 **The engagement consequence is concrete.** Installing by registry identifier resolves
to upstream regardless of which page was found, so the copy is harmless to an installer
and **costs 27 tools to anyone who vendors the tree.** Attribution also travels: a
deliverable built from the copy must credit Vishal Sachdev, whose name the copy's own
`LICENSE` carries.

🔵 Recorded as **`ACTION ZZ-bc`**: on the next pass with an index, compare `LICENSE`
copyright holders across every row sharing a slug stem, and publish any row whose
holder names a different repository's owner. 🟡 Only `canvas-mcp` was checked this
pass — the class is established, its extent is not measured, and this base does not
guess at it.

## 🟢 `ACTION ZZ-bc` discharged — and it never needed the index it was registered against

`p357` found that [`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp)
is a copy of `vishalsachdev/canvas-mcp` whose own `LICENSE` names the upstream owner,
and registered **`ZZ-bc`**: *on the next pass with an index, compare `LICENSE` copyright
holders across every row sharing a slug stem.*

🟢 **`p358` has no index and discharged it anyway, because the copyright holder is a field
on the payload channel.** The `LICENSE` file carries it, `raw.githubusercontent.com`
serves it, and it never required search. 🔵 **That is the transferable lesson:** `ZZ-bc`
sat one pass waiting on an instrument it did not need. A successor registering an action
should name **the field it has to read**, not the channel that happened to be shut.

Seven rows sharing a slug stem, holder read from the payload:

| Row | Holder in its own `LICENSE` | Verdict |
|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | Vishal Sachdev, 2025 | 🟢 self-consistent — **upstream** |
| [`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp) | **Vishal Sachdev**, 2025 | 🔴 names another repository's owner — **copy** |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | Christian Bru, 2026 | 🟢 self-consistent — **upstream** |
| [`algorithm0r/canvas-lms-mcp`](https://github.com/algorithm0r/canvas-lms-mcp) | **Christian Bru**, 2026 | 🔴 names another repository's owner — **copy, newly found** |
| [`AnonymousOnyx22/canvas-lms-student-mcp`](https://github.com/AnonymousOnyx22/canvas-lms-student-mcp) | AnonymousOnyx22, 2026 | 🟢 self-consistent |
| [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | Falkenslab, 2026 | 🟢 self-consistent |
| [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | G36maid, 2026 | 🟢 self-consistent |

🟢 **The holder field predicted a stale fork in two cases out of two.** Both copies were
then measured against their upstreams from the README payload, and both are behind:

| Upstream | Tools | Copy | Tools | Copy is behind by |
|---|---:|---|---:|---:|
| `vishalsachdev/canvas-mcp` | **126** | `NelsonSpencer/canvas-mcp` | 99 | **27 tools** |
| `bruchris/canvas-lms-mcp` | **183** | `algorithm0r/canvas-lms-mcp` | 165 | **18 tools** |

🔵 **So the divergent-holder test is worth keeping as a standing check, and this is the
argument for it.** Nothing in the *licence* separates these rows — all four are MIT, live
and verifying. Nothing in the *description* separates them either:
`algorithm0r/canvas-lms-mcp` and `bruchris/canvas-lms-mcp` publish the **same sentence**
about reading courses, assignments, submissions, rubrics and quizzes. The holder field is
the only cell that separates upstream from copy, and in both cases the copy costs an
engagement that vendors it real capability — 27 tools, then 18.

🟡 **The class is now established on two instances and its extent is still unmeasured.**
Seven rows were compared, not the whole shelf, and the comparison only reaches rows that
*share a slug stem* — a copy that renames itself is invisible to it. Registered as
**`ACTION ZZ-be`**: implement the holder comparison as a gate over every published row,
keyed on the holder string rather than the slug, so a renamed copy is caught too.

## 🔴 One carried row is off-domain and should not be on an education shelf

[`Egonex-AI/Understand-Anything`](https://github.com/Egonex-AI/Understand-Anything)
is live and genuinely MIT (`LICENSE`, holders Yuxiang Lin / Infinite Universe, Inc.),
and at ~87 k ★ it is the largest address this base has carried on this shelf. Read
first-hand this pass, it is **a plugin for AI coding tools that maps a codebase or
document set into an interactive graph** — a developer comprehension tool. It is not
an education agent, and its star count has been inflating this shelf's apparent
education supply. Recorded here as a correction rather than deleted silently.

## 🟢 What changed on `p359` — a function leg found a whole tier, and the tier has no licences

🔵 **`p359` had no GitHub index either** (fourth consecutive pass). Discovery ran on web
search aimed at `github.com` with **function words**; verification ran on the usual
`ls-remote` + payload pair; placement ran on a **third** channel this pass added, `git
log` over a blobless shallow clone. 🟢 **Forty addresses probed first-hand, not one star
measured, and every new row placed in a region.**

| What | Count |
|---|---:|
| addresses probed first-hand | **40** |
| 🟢 live on `git ls-remote --symref` | **39** |
| 🔴 dead — published as a refutation, not a row | **1** |
| 🟢 absent from all eight published shelves | **16** |
| 🔵 of those, absent from this repository entirely | **15** |
| 🔵 of those, read as source by `p190` and never shelved | **1** |
| 🟢 new rows placed in a region by the commit channel | **15 of 16** |
| 🔴 of the 16: **no grant at any probed path** | **8** |
| 🔴 of the 16: explicitly **noncommercial** | **2** |
| 🟡 of the 16: **copyleft** | **1** |
| 🟢 of the 16: **permissive** | **5 — 31 %** |
| 🟢 corpus liveness gate: addresses swept / live | **236 / 236** |
| 🟢 grant-path gate: cells checked / agreeing with live default branch | **240 / 240** |

### 🔴 The finding: the no-grant shape is organised by FUNCTION, not by region

🟢 **`p358` measured the LATAM licensing gap at 23 % permissive against 74 % elsewhere
and called it regional.** `p359` ran legs aimed at *functions* rather than places, and
the permissive rate came back at **31 % — within a few points of the LATAM figure, from
legs that never mentioned a region.**

| Function leg | New addresses | Permissive | No grant at all |
|---|---:|---:|---:|
| Special education / IEP | **7** | **1** | 4 *(+2 noncommercial)* |
| Psychometrics / IRT | **3** | **0** | 2 *(+1 GPL in a manifest)* |
| LATAM education data | **2** | **0** | **2** |
| Proctoring | **2** | 2 🟡 *(one 4 commits, one Art. 5 tripwire)* | 0 |
| Moodle AI layer | **2** | 1 | 0 *(1 GPL-3.0-or-later)* |
| Learning-records warehouse | **1** | 1 *(ECL-2.0, 8 yrs stale)* | 0 |

🔵 **Read the first three rows together.** Special education, psychometrics and
regional curriculum data are **12 of the 16 addresses and 1 of the 5 permissive
grants.** 🟢 **What they share is not a region — it is that each is produced by somebody
who is not shipping software for a living:** a special-education teacher, a university
NLP lab, a researcher with an AAAI oral, a civic-innovation centre, a ministry-adjacent
data volunteer. 🔴 **A `LICENSE` file is a distribution habit, and these producers are
not distributors.** The three legs that *did* return permissive grants — proctoring,
Moodle plugins, learning-records infrastructure — are the three aimed at **tooling
built to be deployed by somebody else.**

🟢 **This supersedes nothing `p358` measured and reframes what it means.** The LATAM
number was real; it was not *regional*. LATAM's supply is weighted toward exactly these
producer types, and `p359` has the control case inside the same region: `bncc-dev`
publishes Brazilian curriculum data under **MIT + CC BY 4.0 with per-record
provenance**, while `pedrosoale/tempo-docente` and `SayvaBR/assistente-ped` publish the
same kind of Brazilian data with **no grant at all**. 🔵 Same country, same month, same
subject matter, opposite licensing — because one is a company and two are not.
Promoted to §22 of `intel/trends.md`.

### 🔴 What `p359` searched and did not find

🟢 **An informed gap, stated so silence is not mistaken for coverage.**

- 🔴 **No OneRoster MCP server exists.** The `OneRoster` leg returned six learning-record
  addresses and a pull request; the only MCP servers on it were the two `learnmcp-xapi`
  siblings this base already holds. **Rostering is the one interoperability standard
  with no agent connector at all.**
- 🔴 **No SCORM result of any kind**, across a leg that named it explicitly alongside
  `LTI tool` and `proctoring`. The leg returned nine addresses and not one touched
  SCORM. 🔵 `compose/patterns.md` Pattern 6 targets legacy SCORM estates; it still rests
  on the carried inventory, and `p359` adds nothing to it and found nothing against it.
- 🔴 **No open-source IRT-calibrated LLM grader.** Three papers pair IRT with LLM short-answer
  grading; the code for the closest one has no licence, and the IRT libraries that *are*
  permissive (`joakimwallmark/irtorch`, MIT, committed 2026-10-19; `eribean/girth`, MIT but
  untouched since 2022-01-30 — both already held)
  contain no grading layer. **The join is unbuilt, and it is a genuine build
  opportunity rather than an adoption one.**
- 🟡 **EMEA returned three addresses and no policy.** Every EMEA regulatory fact the
  prescribed leg produced — the 2 Aug 2026 high-risk enforcement date, the AI omnibus
  in effect 27 Jul 2026, the UK £4 m lesson-planning programme, the Finland/Estonia/
  Netherlands leaders — is already on `intel/market.md`. The region's `p359` yield is
  supply only: Türkiye, Germany and a `+0200` Moodle plugin.

## 🟢 What changed on `p358` — the LATAM gap is a **licensing** gap, and it is now measured

🔵 **`p358` had no GitHub index either** (third consecutive pass). Discovery ran on web
search aimed at `github.com` with **function words**; verification ran on the usual
`ls-remote` + payload pair. 🟢 **Thirty-five addresses probed first-hand, not one star
measured.**

| What | Count |
|---|---:|
| addresses probed first-hand | **35** |
| 🟢 live on `git ls-remote --symref` | **32** |
| 🔴 dead — published as refutations, not rows | **3** |
| grants read from the payload | **17** |
| 🔴 live with **no grant at any probed path** | **15** |
| 🟢 new rows published | **10** |
| 🔴 new licence-flag rows | **6** |
| 🟢 carried rows re-probed for `ZZ-bc` | **7** |

### 🔴 The finding: three passes have mis-named the LATAM gap, and the payload channel says what it actually is

`p356` called it a supply gap, then refined it to a **tooling** gap — *"Spanish-language
assessment content exists in volume; what does not exist is a Spanish-language item bank,
autograder or judge."* `p357` ran no LATAM leg and said so plainly.

🟢 **`p358` ran sixteen LATAM addresses through the payload channel and the tooling is
there.** An item bank for Colombia's Saber Pro, a BNCC-aligned municipal assessment
platform, four ENEM platforms, an n8n autograder with RAG over open answers, a Mexican
*Nueva Escuela Mexicana* school platform, a PAES preparation platform for Chile, a
Socratic tutor agent, a programming-education platform with an AI tutor. 🔴 **Of the
thirteen that are live, three carry a licence.**

| Leg | Live addresses | Grant read from payload | Grant rate |
|---|---:|---:|---:|
| 🔴 **LATAM (Spanish / Portuguese)** | **13** | **3** | 🔴 **23 %** |
| 🟢 Everything else this pass (LTI, MCP, assessment, Africa) | **19** | **14** | 🟢 **74 %** |

🔴 **So the gap is not supply and not tooling. It is licence hygiene**, and the ten
unlicensed live addresses are these: `DVLASZ/banco-preguntas-saberpro` (Saber Pro item
bank), `Jairh1294/Auto-Grader` (🔴 **a search snippet in this pass's leg states it is
MIT; the payload says there is no grant at any path** — the claim is refuted, not
carried), `joao-paulo-yudi/StudyENEM`, `quero-edu/100-questoes-enem`,
`Doutii/enem_online`, `MarcioMoJr/HelpEnem-`, `juanseisaacs/walter.Ia` (Colombian MEN
curriculum, ages 5–10), `helmerpersonal-escuela/nemia-escolar` (Mexico, Nueva Escuela
Mexicana), `leoparoli/EduCode`, `BrayanG877/ia-educativa-reto`. 🔵 Every one is
**all rights reserved** until its author adds a file.

🟢 **Why this is a better finding than "nothing found", and what an engagement does with
it.** Three consequences, none of which follow from a supply gap:

1. 🟢 **The absence is cheap to fix and the fix is not Globant's to make.** A supply gap
   needs a build; a missing `LICENSE` needs one file from an author who already published
   their work publicly and plainly intends it to be used. For a LATAM engagement that
   wants `banco-preguntas-saberpro`'s item bank, **asking is a real option** and costs an
   email.
2. 🔴 **Until then the shape of the risk inverts.** A copyleft row is usable with care; an
   unlicensed row is usable not at all, and it is the *more* dangerous kind because
   nothing on the landing page says so. 🔵 This base has recorded that hazard eight times
   on other shelves (`CBIT-AiExam-plus`, `fedena`, `TeachingKG`…); what is new is that in
   one region it is **the majority case**.
3. 🟢 **The three licensed rows carry the region.** `TutorIA` (MIT, inside Open edX),
   `OpenPiar` (AGPL-3.0, Colombian inclusion law) and `OpenTest` (MIT, offline LAN
   assessment) are the LATAM tier above, and the market note on `intel/market.md` places
   them against the region's own adoption numbers.

🟡 **What this pass did not establish.** Sixteen addresses is not a census, the legs ran
in Spanish and Portuguese only, and **no comparable count exists for any other region's
native-language supply** — the 74 % comparator is this pass's *English-language* legs,
which is a different population and not a controlled one. 🔵 The 23 %/74 % split is a
real measurement of two samples and **not** evidence that LATAM authors license less
carefully than authors elsewhere; it could as easily reflect project age or venue.
Registered as **`ACTION ZZ-bf`**: run the same function-word legs in a third language
(German, French, Hindi or Mandarin) and compare the grant rate before anyone treats
licence hygiene as a regional property.

### 🟢 EMEA gains its first African rows, and the closed vocabulary is why that needed saying

🔴 **Every EMEA row on this base before this pass was European** — Belgium ×2, Germany,
Italy, Spain, UK, Portugal, Switzerland. 🔵 `region` is a closed five-value field, so
**Kenya is EMEA**: the *A* in the acronym has been carrying nothing. `elimu-mcp` (Kenya's
national education system over MCP) and `Moha-abshir/SMS` (a Kenyan CBC school management
system, MIT — see `verticals/solutions.md`, where it bears directly on this base's
"no permissive education ERP" finding) are the region's first two.

🔴 **The Gulf and MENA leg returned no open-source supply and that is recorded as a
measured absence.** The leg returned a real and well-documented market — **Alef
Education** reaching 33 000 students across 28 UAE private schools (February 2026) and
25 000 educators trained in seven weeks with Microsoft through the Ministry of Education,
ADEK, KHDA and SPEA — and **not one open repository**. 🟢 That is a commercial-incumbent
finding, not a supply finding, and it belongs on `intel/market.md`; on this shelf it is
an absence with a named cause.

## 🟢 What changed on `p357` — a weaker discovery channel, and two tiers `p356` could not reach

🔵 **`p357` had no GitHub index.** Its credential is scoped to one unrelated repository,
so discovery ran on **web search** and verification ran on the usual `ls-remote` +
payload pair. 🟢 **Nine addresses were added, every one live and licence-read
first-hand**; not one star was measured.

| What | Count |
|---|---:|
| addresses probed first-hand | **28** |
| 🟢 live on `git ls-remote --symref` | **25** |
| 🔴 dead — published as refutations, not rows | **3** |
| grants read from the payload | **21** |
| 🔴 live with **no grant at any probed path** | **3** |
| 🟢 new rows published | **9** |
| 🔴 new licence-flag rows | **4** |

🟢 **`ACTION ZZ-bb` discharged, and `p356`'s restraint is what made it worth
discharging.** Both the `lecture capture` and `curriculum ontology` legs returned
shelvable rows, confirming `p356`'s diagnosis that the empty legs were **its own query
syntax** rather than an absent supply. Had `p356` published "no lecture-capture supply",
this pass would have had to retract it; because it published *unmeasured*, this pass
simply measured it.

🔴 **Three addresses described in detail by sources in this pass's legs do not exist.**
`fh-yarbouh/oak-curriculum-ontology` was described down to its serialisation formats
(RDF, OWL, SKOS, SHACL) and its licence pair (MIT + OGL-3.0) — and `ls-remote` returns
nothing. 🟢 **The project is real and the owner was wrong**: it is
[`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology),
found by re-probing the organisation name, and every detail checked out at the correct
address. `schooltool/schooltool` and `gegok12/gegok12` are also dead, and no substitute
was found for either. 🔵 **A 404 is not a finding, and a detailed description of a 404
is not one either** — but a wrong *owner* on a real project is recoverable, and worth
one more probe before an absence is published.

---

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

| Region | Placed rows on this shelf | Change on `p358` |
|---|---:|---|
| **APAC** | **21** | — |
| EMEA | **8** | 🟢 **+1 — `elimu-mcp` (Kenya): the region's first AFRICAN row** |
| North America | 6 | — |
| **LATAM** | **4** | 🟢 **+2 — `TutorIA`, `OpenPiar` (both Colombia): the first LATAM rows added since `p350`** |
| 🔵 Not placed | **38** | +3 — `OpenTest`, `gradescope-mcp`, `Canvas-Agent` |

🟢 **`ACTION ZZ-bd` discharged, and it caught this pass's own first draft.** `p357`
registered it after noticing that a census counting every table with a `Region` column
**counts the distribution table too** — its first column holds the five region names, so
each bucket gains exactly one. 🟢 `p358` implemented the guard as written: the census
skips any table whose `Region` header sits in **column 0**. It reports
`rows excluded by the ZZ-bd self-table guard: 5` — the trap `p357` predicted, sprung and
caught.

🔴 **And the derivation corrected a figure this pass had already written down.** The
first draft of the table above claimed **EMEA 9, +2**, counting `elimu-mcp` *and*
`Moha-abshir/SMS`. The census says **8**: `Moha-abshir/SMS` is a platform row and lives on
`verticals/solutions.md`, not on this shelf, and *"placed rows on this shelf"* does not
reach it. 🔵 That is `ACTION ZZ-aw`'s class caught in the act — a distribution asserted
from memory of what the pass did, rather than derived from the file it describes — and
the only reason it did not ship is that `ZZ-bd`'s instrument was built before the table
was trusted.

🔴 **A defect in this base's own instrument, found while deriving the table above and
published because it would have survived another pass.** A census script that counts
every table with a `Region` column **counts this table too** — its first column holds
the five region names, so each bucket gains exactly one. The first derivation this pass
returned `APAC 22 · EMEA 8 · NA 7 · LATAM 3 · Not placed 36`: **every bucket inflated
by one, uniformly**, which is precisely the shape that reads as plausible rather than
as broken.

🟢 **`p356`'s published figures were correct.** Excluding the self-row, the pre-`p357`
state was `APAC 21 · EMEA 6 · NA 6 · LATAM 2 · Not placed 27` — matching `p356`'s prose
on all five buckets. 🔵 So this is not a correction to a published number; it is a
**trap recorded before it was fallen into**, and the uniformity is the tell: a real
distribution shift does not move five buckets by one each. Registered as
**`ACTION ZZ-bd`** — any census target must exclude the table it is writing into.

- **APAC** is now the densest region on this shelf by a wide margin — **21 rows**, up
  from 11 one pass ago. China, Hong Kong, India, Korea, Bangladesh and Iran all have
  first-party education software, and the eight rows added this pass are *infrastructure*
  (item banks, judges, graders), not demos.
- **EMEA** holds **8**, concentrated in university assessment tooling (Belgium ×2,
  Germany, Italy, Spain, UK), and gains Iran and Portugal on `repos/foundations.md`.
  🟢 **`p358` changes the region's composition, not just its count:** every prior EMEA
  row is European, and `elimu-mcp` (Kenya) is the first African one. EMEA's *A* had been
  carrying nothing on this shelf for 357 passes.
  🟢 **`p357`'s addition changes the region's character, not just its count:** every
  prior EMEA row is *assessment* software, and
  [`oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) is
  the region's first **curriculum data asset** — and the first anywhere on this base
  whose data grant allows commercial use with no share-alike.
- **North America** holds 6, concentrated in the standards/skills/evaluator layer.
  🔴 **A correction while deriving this:** the sentence this replaces claimed **6** NA
  rows while the tables underneath it carried **5**. `p356` adds `edx-proctoring`, so
  the published figure is now 6 *and true*; it was off by one before. Nothing binds a
  **distribution** stated in prose, which is `ACTION ZZ-aw`'s shape on a third quantity.
- 🟢 **LATAM now places 4** rows — `mcp-brasil` and `bncc-dados` (Brazil, both MIT),
  joined on `p358` by `TutorIA` (MIT) and `OpenPiar` (AGPL-3.0), **both Colombia**. The
  region doubles, and for the first time it holds a *tutoring agent* and a
  *statutory-compliance* tool rather than only public-data connectors.
  🔴 **The paragraphs below are `p356`'s and `p357`'s reading of this gap, and `p358`
  refutes the diagnosis in both of them** — the gap is licence hygiene, not supply and
  not tooling. See *"What changed on `p358`"* above for the 23 %/74 % measurement. They
  are kept rather than deleted because the sequence of wrong names for this gap is
  itself the record.
- 🔵 *`p356`/`p357` on the same gap, superseded:* 🔵 Stated plainly because an unchanged number across two passes looks like a
  re-confirmation and is not one: `p356`'s function-word leg is the last measurement of
  this gap, and it stands unrepeated, not re-verified.
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
