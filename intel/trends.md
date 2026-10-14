---
industry: education
region: Global
updated: 2026-10-14
---
## Pass 195 — 2026-10-14

🆕 🔴 **The trend this pass can measure for the first time is a WHOLE-SHELF one, and the trend
it can no longer measure at all is *"trending"*.** 🟢 `468` LIVE slugs read from bytes, `2 167`
probes, `0` throttles — so the licence distribution of education's open-source estate is now a
measurement rather than a sample. 🔴 And `github.com` closed at this session's proxy mid-pass,
so flow is gone and only stock remains.

### 🆕 🟢 T1 — Education's open-source estate is two-thirds permissive, and the exceptions cluster by LAYER

| | rows | share of the `380` licensed |
|---|---|---|
| 🟢 permissive *(`MIT` `218`, `Apache-2.0` `56`, `BSD`/`0BSD`/`ISC` `5`, `CC0` `2`)* | **`281`** | 🟢 **`74`%** |
| 🔴 `AGPL-3.0` | **`41`** | 🔴 **`11`%** |
| 🟡 `GPL-3.0` `29` · `GPL-2.0` `5` · `LGPL` `5` · `MPL` `1` | `40` | 🟡 `11`% |
| 🟢 `ECL-2.0` *(education-specific)* | `2` | — |
| 🔴 source-available *(`PolyForm` `4`, `Elastic` `1`)* + non-commercial `2` | **`7`** | 🔴 `2`% |
| 🔴 `UNCLASSIFIED` | `5` | 🔴 `1`% |

🔴 **The permissive share is high and it is NOT distributed evenly — it is a function of what
the repository IS.** 🟢 The agent, tutor, curriculum and MCP-server layers are overwhelmingly
`MIT`. 🔴 **The hosted-LMS layer is Affero as a market**: Open edX *(four slugs)*, Canvas,
Frappe LMS, `classroomio`, `learnhouse`, `tutor`. 🟡 **So *"education OSS is permissive"* is
true of the layer you build and false of the layer you host**, and a proposal that averages the
two is wrong in the direction that costs money.

### 🆕 🔴 T2 — `18.8`% of the shelf grants nothing at root, and the interoperability layer is the worst of it

🔵 `88` of `468` return no licence across a `19`-filename root ladder. 🔴 **The three
standards-body reference implementations on this shelf are all in that set:**

| repo | body | root | README claim |
|---|---|---|---|
| 🔴 [`1EdTech/lti-1-3-php-example-tool`](https://github.com/1EdTech/lti-1-3-php-example-tool) | **1EdTech** *(LTI)* | 🔴 NONE | 🔴 none |
| 🔴 [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | **ADL** *(SCORM/xAPI)* | 🔴 NONE | 🟡 *"Licensed under the Apache License, Version 2.0"* |
| 🔴 [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) | H5P desktop | 🔴 NONE | 🔴 none |

🔴 **The standards are open; their reference implementations are not a licensed starting
point.** 🟢 **The trend statement, falsifiable: as education software gets more interoperable,
the licence risk moves from the PLATFORM to the GLUE** — the platforms all ship a licence, and
the adapters increasingly do not.

🟡 **Scope, stated before anyone quotes `18.8`%:** it means *no licence at ROOT*, and p195 has
a counter-example — [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) carries
**`GPL-2.0`, `17 286` B, at `docs/License.txt`**. 🔵 Registered as
[`p969-root-only-licence-reach`](../compose/code/p969-root-only-licence-reach/).

### 🆕 🔴 T3 — A hardened classifier reads three restrictive licences as `MIT`, and the mechanism is COMPOSITION

🔵 `osi_family_of` returns `MIT` and `commercial_use_ok` returns ALLOWED for all three:

| repo | bytes | real title | what the body does |
|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | `8 563` | *"PageLM Community License"* | 🔴 non-commercial + revenue-share |
| [`GautamVhavle/learner-verse`](https://github.com/GautamVhavle/learner-verse) | `2 594` | **BUSL 1.1** | 🔴 bars *"direct or indirect commercial activity"* |
| [`willwearing/graspful`](https://github.com/willwearing/graspful) | `1 439` | *"O'Saasy License Agreement"* | 🔴 anti-SaaS non-compete |

🔴 **`P171` widened the title window to `40` lines so a REFLOWED `AGPL` would be caught, and
that window swallows MIT's canonical *"Permission is hereby granted, free of charge"* sentence
out of licences that are not MIT. `P250`'s gate then trusts the family and never reads the
body.** 🟢 **Two hardened controls, each correct alone, composing into the one wrong answer
that costs a delivery.** 🔵 `learner-verse` is the proof: `commercial_use_ok` **has** a `BUSL`
branch returning PROHIBITED, and it never fired because the family answered `MIT` first.

🟡 **This is a trend about the LICENCES, not only about the tool: authors are writing MIT's
grant sentence at the top of restrictive licences.** 🔴 **Four distinct instances now
*(`PageLM`, `learner-verse`, `graspful`, and `talentcoach`'s verbatim MIT warranty paragraph
over an all-rights-reserved grant)*, which makes it a drafting pattern rather than an accident.**

### 🟢 T4 — The cheap discriminator is SIZE, and it is a triage tool rather than a verdict

🟢 Measured across this pass's `218` `MIT` rows: **median `1 071` B, p25 `1 067`, p75 `1 080` —
a `13`-byte interquartile spread.** 🔵 Licence boilerplate is boilerplate, so a payload claiming
a family from far outside its band has been **modified**.

| | result |
|---|---|
| permissive rows banded | `281` |
| 🟢 `IN-BAND` | `265` |
| 🔴 flagged for a human read | **`16` — `5.7`%** |
| 🔴 of those `16`, already published by this KB | 🔴 **`16` of `16`** |

🟢 **It reaches the `P1054`/`P1056` classes from a number the census already holds, with no
extra fetch, at `0` false negatives against this KB's own hand-built ground truth.** 🔴 **It
discovered nothing**, and p195 nearly published the `16` as if it had.

### 🆕 🔴 T5 — Apache is increasingly ELECTED without being SHIPPED

🔵 Four rows elect `Apache-2.0` in `560`–`738` B where the licence text is `11 348` B:
`numbas/numbas-lti-provider`, `zavora-ai/mcp-student-records`, `foradian/fedena`,
`projectfedena/fedena`. 🟢 **The election is valid and the family verdict stands.** 🟡 **What
is absent is the text, which §`4(a)` requires a redistributor to include** — so the obligation
transfers to whoever ships the derivative, and the remedy is one file. 🔵 Distinguish this from
T2: **T2 is no grant; T5 is a grant by reference.**

### 🟢 T6 — Curriculum at scale is permissive; production-agent curriculum is not

🟢 **One byte-identical `MIT` file *(`1 141` B)* covers `microsoft/ML-For-Beginners`,
`microsoft/generative-ai-for-beginners` and 🆕 `microsoft/ai-agents-for-beginners`** — a single
licence across one publisher's entire teaching estate, read from bytes this pass. 🔴 **Against
which p194's measurement still stands: the best-known corpus for taking agents to production in
an enterprise is licensed so an enterprise cannot use it** *(`NirDiamant`, three repositories,
`49.7`% of the trending stars, non-commercial)*. 🟡 **Teach-the-basics is a solved, permissive
supply. Teach-production is a licensing hole**, and it has not moved.

🆕 🟢 **The sovereignty-shaped gap narrowed a little**:
[`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) — `MIT`, `1 067` B,
agents on a **local LLM, no cloud APIs**. 🔴 `≈796`★.

### 🆕 🔴 T7 — A ministry mandate is not a durable market, and Korea is the completed case

🟢 Resolved this pass against p194's CONTESTED cell: an **August `2025`** law reclassified
Korea's AI digital textbooks as **supplementary material**, the mandate was dropped, school
uptake fell *(`37`% → `19`%; second-semester use `1 686` schools, `−58.8`%)*, and ≈`10`
publishers sued for ≈**`₩200` bn in June `2026`.** 🔴 **p194's inherited *"full expansion by
`2028`"* claim is REFUTED.**

🟡 **The trend, stated so it transfers:** the reported failure causes are **classroom technical
failure, data-privacy objection, and teacher and parent opposition — not model quality.**
🟢 **So the reversal risk in a ministry-anchored engagement is an OPERATIONS and CONSENT risk**,
and the deliverable that survives it is standards-based content plus an exportable record,
not a programme-specific platform.

### 🟡 T8 — Adoption and governance are still sequenced differently by region, with APAC's cell now ambiguous

🟢 **LATAM remains the only region where adoption measurably outruns governance** — `92`% of
students and `79`% of faculty engaging *(DEC, >`30 000` responses)* against `26`% of
institutions with a formal framework. 🟢 EMEA and North America keep governance ahead of use.
🆕 🟡 **APAC's mandates are ahead of both, and Korea has now shown they are reversible** —
which is a different risk from the one this KB has been describing.
🔴 **APAC still has no measured adoption RATE here, second pass, and the searches are named in
[`intel/market.md`](market.md).**

### 🔴 T9 — This KB's own measurement cadence is too fast, and that is now measured twice

🟢 `30` shelf rows re-priced against p193's same-day reads: **largest delta `+9`, every row
inside `±10`, net `+22` across ≈`120 000`★ — `0.018`%.** 🔵 Combined with the loss of the
trending lane, **there is no flow signal available to this session at all.** 🔴 **An hourly
pass cannot produce a star trend; it can only produce noise shaped like one.** 🟢 **The honest
cadence for the shelf is weekly, and the honest hourly contribution is a measurement that does
not depend on time** — a licence census does not, which is why this pass's useful half was the
census and its wasted half was an instrument that already existed.

### 🟢 What did NOT change, stated so the trend lines stay honest

🟢 `menthorlabs/menthor` **`archived: true`**, third pass. 🟢 `CAHLR/OATutor` still has **no
topics**, so it stays invisible to every topic query. 🟢 The `ECL-2.0` reading of Sakai and
Opencast holds on a third channel. 🔴 **No band exists yet for `AGPL-3.0`, `GPL-3.0` or
`ECL-2.0`, so the `77` copyleft rows are UNCHECKED for `P1054`-style narrowing** — the single
largest hole left by this pass.
## Pass 194 — 2026-10-14

🆕 🔴 **The trend this pass measures is that education's open-source output has moved to a
publication format no education taxonomy indexes, and arrived there carrying licences that bar
the use Globant would make of it.** 🟢 Both halves measured today, both falsifiable.

### 🆕 🔴 T1 — Education trends in exactly one lane, and thirteen passes probed the wrong one

| lane | rows | education rows |
|---|---|---|
| default weekly + daily + `trending/python` + `spoken_language_code=pt` | `32` | 🔴 **`0`** |
| 🟢 `trending/jupyter-notebook` + `spoken_language_code=es` | `18` | 🟢 **`10`** |

🟢 **The mechanism, and it is not a GitHub quirk: the notebook IS the pedagogical artefact.**
Lesson text, runnable cell and output live in one file, so a filter on `.ipynb` is accidentally
a filter on *teaching*. 🔴 **`trending/python` returned `0` education rows in the same hour that
`trending/jupyter-notebook` returned `9`** — same ecosystem, same week, same language family.

🔵 **Falsifier for p195:** probe `zh`, `fr`, `de`, `ja`, `hi` spoken-language lanes. 🟢 If
education concentrates in narrow lanes generally, they should return non-zero education rates
on small denominators. 🔴 If they return `0`, then the notebook lane is doing the work and
language filtering is not, and this trend narrows to **one** lane rather than a class of them.

### 🆕 🔴 T2 — The non-commercial tutorial economy: half the stars, none of the rights

🔵 `10` education rows, `229 058`★, licence read from bytes on every one:

| | stars | share |
|---|---|---|
| 🔴 **no commercial grant** | `113 904` | 🔴 **`49.7`%** |
| 🟢 deliverable | `109 418` | `47.8`% |
| 🟡 conditions attach *(`LGPL-3.0`)* | `5 736` | `2.5`% |

🔴 **And `91 466` of the `109 418` deliverable stars are a single repository**,
`microsoft/ML-For-Beginners`. 🔴 **Remove one corporate publisher and education's trending shelf
is `84`% unusable for client work.**

🟡 **The licence class is not new to this KB — `lib/license_family.sh` has modelled
`NONCOMMERCIAL-NOT-OSI` for passes, and it classified all three of these payloads correctly
without prior knowledge of them. 🟢 What is new is which repositories populate it, and their
share.** `NirDiamant`'s
three repositories share one byte-identical `Custom License Agreement`: *"expressly prohibited
from using the Licensed Material, in whole or in part, for any commercial purpose"*, with **all
commercial rights exclusively reserved.** 🔵 AGPL permits commercial use and attaches disclosure;
**this permits none.** 🟡 Ordering: `permissive → weak copyleft → Affero → **no commercial
grant**`.

🔵 **Why it is a trend and not a catalogue entry:** the barred repositories are precisely the
*production-oriented* ones — `agents-towards-production` describes itself as tutorials for
*"enterprise deployment."* 🔴 **The corpus for taking agents into an enterprise is licensed so
an enterprise cannot use it**, and it gained `163` stars this week.

### 🆕 🔴 T3 — Curriculum ships under CONTENT licences; the code inside it does not notice

| repo | licence | 🔴 the mismatch |
|---|---|---|
| [`datawhalechina/every-embodied`](https://github.com/datawhalechina/every-embodied) | `CC-BY-4.0` *(`858` B)* | 🔴 a robotics/VLA **code** curriculum under a licence written for prose |
| [`datawhalechina/llm-algo-leetcode`](https://github.com/datawhalechina/llm-algo-leetcode) | `CC-BY-4.0` *(`792` B)* | 🔴 solutions and test cases — **code** — under the same |
| [`xiaolai/the-craft-of-selfteaching`](https://github.com/xiaolai/the-craft-of-selfteaching) | `CC-BY-NC-ND-3.0` *(README only, **no file**)* | 🔴 `NC` **and** `ND`: may not be sold **and** may not be adapted |
| [`enkidevs/curriculum`](https://github.com/enkidevs/curriculum) | `CC-BY-NC-SA-4.0` *(`189` B)* | 🔴 carried since p192; `NC` |

🟡 **Creative Commons explicitly advises against using CC licences for software**, because they
address neither source availability nor patent grants. 🟢 **`CC-BY-4.0` is still workable** for
an engagement — commercial use permitted, attribution required — 🔴 **but it tells a client
nothing about the code's warranty or patent position**, and three of the four rows above are
`NC` on top. 🔵 **The trend: as curriculum becomes code, its authors keep reaching for content
licences.** 🟢 Falsifier: if p195's wider byte-read over the shelf finds `CC-*` concentrated in
pre-`2024` repositories, this is legacy rather than a trend.

### 🆕 🔴 T4 — The `2026` cohort still ships no licence, now with large repositories

🔵 p193 measured five `2026`-created education repositories at `333`–`515`★, **all five with no
licence file.** 🆕 **p194 shows the pattern is not confined to small new repositories.**

| repo | ★ | probe | result |
|---|---|---|---|
| 🔴 [`anthropics/prompt-eng-interactive-tutorial`](https://github.com/anthropics/prompt-eng-interactive-tutorial) | `38 564` | `19` filenames + README | 🔴 **no licence, none named** |
| 🔴 [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | `29 553` | same | 🔴 **no licence, none named** |
| 🔴 [`midudev/libros-programacion-gratis`](https://github.com/midudev/libros-programacion-gratis) | `6 072` | same | 🔴 **no licence, none named** |

🔴 **`29 553`★ is the `#3` row on this KB's own shelf.** 🟢 **No licence is not permissive —
it is the absence of a grant**, and default copyright applies. 🟡 **Direction across two passes:
p193 found it in the new-and-small cohort, p194 finds it in the large-and-established one, so
the honest statement is not *"new projects skip licences"* — it is *"education repositories skip
licences at every size."***

### 🆕 🟢 T5 — Platforms and curriculum are now visibly two markets at two speeds

🔵 Not one of the `15` platform rows in [`verticals/solutions.md`](../verticals/solutions.md)
appeared in any of six trending lanes. `openedx/openedx-platform` moved `+3` stars in `4` days.
🟢 Meanwhile `9` curriculum corpora gained `1 266` stars in a week.

🟢 **The actionable form: platform choice is an installed-base and licence decision; curriculum
choice is an attention and licence decision.** 🔴 **An engagement that reads only trending builds
a course with nothing to run it in; one that reads only the platform shelf ships a system with
`2019` content.** 🔵 This KB should stop expecting one shelf to serve both, and p195's shelf
re-pricing should report platforms and curriculum **separately**.

### 🆕 🟢 T6 — The study layer keeps being published as runnable artefacts, now on a fourth surface

🔵 p192: the second-largest `edtech`-topicked repo on GitHub is a **PDF→skill compiler**
*(`virgiliojr94/book-to-skill`, `34 806`★, `MIT`)*. p193: `mattpocock/skills` *(`290 184`★)* and
`vercel-labs/skills` *(`34 736`★)* trending, neither tagged education. 🆕 **p194: the week's
education momentum is `9` notebook corpora and `0` platforms.**

🟢 **Four independent surfaces agree** — topic, shelf, trending-default, trending-by-language.
🟢 **The study layer is shipping as skills and notebooks, outside every education taxonomy**,
which is the mechanism behind thirteen passes of empty topic queries.

### 🆕 🟡 T7 — Adoption and governance are sequenced differently by region, and it is measured

| region | adoption | governance | 🔴 gap |
|---|---|---|---|
| **LATAM** | 🟢 `87`% institutional, `79`% faculty | 🔴 `26`% strategy, `45`% guidance | 🔴 **`61` points** |
| **EMEA** | `63`% teachers | `≈70`% guidance | 🟢 governance ahead |
| **North America** | `60`% teachers | `≈70`% guidance; `>28` states | 🟢 governance ahead |
| **APAC** | 🔴 **not measured** | 🟢 ministry mandates *(China, Japan)* | 🟡 regulation ahead of measurement |

🔴 **LATAM is the only region where adoption measurably outruns governance** — and it has the
KB's highest measured adoption. 🟢 **Not a weakness story, a sequencing story**: it changes the
first deliverable per region, as [`intel/market.md`](market.md) sets out. 🔴 **APAC's blank
adoption cell is this pass's named gap**, not an implied zero.

### 🆕 🟡 T8 — Consolidation reaches the tooling an education engagement would have built on

🔴 [`continuedev/continue`](https://github.com/continuedev/continue) — **`Apache-2.0`
*(`11 348` B, read from bytes this pass)*, archived and read-only after acquisition by Cursor,
June `2026`** *(secondary)*. 🟢 Permissive licence means existing copies remain usable;
🔴 **upstream has stopped.** 🟡 **The pattern to watch: a permissive licence protects the code
you already have and does not protect the roadmap.** 🟢 Recorded so this KB does not recommend a
frozen base to a coding-education engagement.

### 🟢 What did NOT change, stated so the trend lines stay honest

🟢 The `15`-row platform licence matrix: **re-read from bytes through an independent channel,
`15` / `15` unchanged.** 🟢 p193's `frappe/lms` Affero correction: **confirmed byte-exact by a
second lane.** 🔴 The EMEA vendor-ranking gap: **open for a third pass.** 🔴 The Korea
AI-textbook rollout: **contested, no position asserted.** 🔴 Government primary sources:
**structurally unreachable, not retested, no calls spent.**

## Pass 193 — 2026-10-14

🆕 🔴 **The trend this pass measures is a PUBLICATION practice, and it decides whether any of
`2026`'s education software can be delivered to a client at all.**

### 🔴 T1 — The licence cliff: the `2026` cohort ships stars and no licence

🔵 Five education repositories created in `2026`, `333`–`515`★, every one discovered this
pass, every one's **root tree read from bytes**:

| repo | ★ | created | paths | region signal | licence |
|---|---|---|---|---|---|
| [`buynao/aipath`](https://github.com/buynao/aipath) | `515` | `2026-06-12` | `78` | 🔵 bilingual `README.zh-CN.md` — **APAC** | 🔴 **none** |
| [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) | `501` | `2025-12-01` | `150` | 🔵 US `501(c)(3)`, `7` languages — **North America** | 🔴 **none** |
| [`mabdulre9/electrical-engineering`](https://github.com/mabdulre9/electrical-engineering) | `487` | `2026-09-20` | 🔴 **`1`** | 🟡 unplaced | 🔴 **none** |
| [`jude-miller-dev/Milky-institute-online`](https://github.com/jude-miller-dev/Milky-institute-online) | `367` | `2026-01-30` | `786` | 🔵 Chinese/English, Spring Cloud — **APAC** | 🔴 **none** |
| [`bedriyan/medkit-app`](https://github.com/bedriyan/medkit-app) | `333` | `2026-04-26` | `110` | 🟡 unplaced | 🔴 **none** |

🔴 **Five of five.** Add [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)
at **`29 553`★ with no licence object at all** and the pattern spans two orders of magnitude
of reach. 🔵 **No licence is not a gap in the metadata — it is all rights reserved.**

🟢 **Why this is a TREND and not five anecdotes:** the shelf — `30` rows, almost all created
before `2026` — carries a licence on `29` of `30`. 🔴 **The cohort created in `2026` carries
one on `0` of `5`.** 🟡 The two populations differ on exactly the attribute that decides
adoptability, and they differ completely.

🔵 **Mechanism, stated as a hypothesis rather than a measurement:** the `2026` cohort is
published as *content* — a curriculum, a course, a skill, a simulator — by authors who are
teachers rather than maintainers, into harnesses that never asked them for a `LICENSE`.
🔴 **Commercial consequence: the more education-native the project, the less likely it can be
used.**

### 🔴 T2 — The unit keeps shrinking, and it has reached one file

🟢 p192: *"the unit of education software is shrinking from a deployable platform to a few
files of pedagogy."* 🔴 **p193's limit case: `mabdulre9/electrical-engineering`, `487`★,
created `2026-09-20`, `1` path — a single `README.md` — the fastest-accumulating education
row this KB has ever measured.**

🔵 Alongside it, the global trending surface *(measured today, first time in this KB's
history)* carries `mattpocock/skills` at `290 184`★ and `vercel-labs/skills` at `34 736`★.
🟡 Neither is tagged education and both are study/reference artefacts.
🔴 **Three independent surfaces — topic, shelf, trending — now point the same way, and none
of them classifies this material as education.** 🟢 Which is why thirteen passes of
education-topic queries could not see where the field went.

### 🟢 T3 — The field has a denominator now, and it is `7`

🔵 `topic:edtech stars:>400 pushed:>2026-08-01` → **`7` repositories worldwide.** `5` already
on this shelf; of the other two, one is a job-board list and one is unlicensed. 🟢 **Net
adoptable discoveries: `0`.**

🔴 **This is the strongest form p192's *"the frontier has moved inside existing projects"*
claim has taken.** 🟡 A percentage *(`84`% already-known)* says the sampling is saturated. 🟢 A
denominator of `7` says something harder: **the maintained, visible, `edtech`-topicked
open-source population is small enough to recite from memory, and this KB has read all of
it.**

### 🔴 T4 — Licence metadata is not a signal, in either direction

🔵 Measured across `30` shelf rows this pass: **`9` return `NOASSERTION`, `1` returns
`null`.** 🔴 Of those `10`, **`4` hide a licence that bars or encumbers delivery**
*(`CC-BY-NC-SA`, the PageLM community licence, `CC-BY-SA`, `LGPL`)*, **`2` hide a permissive
one** *(`Apache-2.0` ×2)*, `1` is genuinely unlicensed at `29 553`★, and `3` are unread.
🟢 **So `NOASSERTION` predicts nothing** — it is not even conservatively wrong.

🟡 **Trend, not incident: the ecosystem's licence metadata degraded exactly as licence
diversity increased.** Content licences *(`CC-*`)*, bespoke community licences and no licence
at all are all invisible to a field designed for OSI code licences. 🔴 **Every tool that
filters a dependency list by that field — procurement portals, SBOM scanners, approved-tool
registers — is blind in the same place.**

### 🔴 T5 — Governance dates are splitting into cohorts, and the briefings are quoting one

🔵 EMEA, measured this pass: Art. `50` marking applies from **`2026-08-02`** to systems placed
on the market after that date, and from **`2026-12-02`** to generative systems already on the
market. 🔴 **This KB published the December date alone one pass ago, and so does most of the
public commentary.** 🟢 Annex III high-risk — education — moved to **`2027-12-02`** by
Regulation (EU) `2026/1744` *(OJ `2026-07-24`, in force `2026-07-27`)*, with **no substantive
requirement changed.**

🟡 **The trend: deferral is making compliance dates COHORT-dependent rather than
calendar-dependent.** 🔴 Two systems in the same school, doing the same thing, now have
obligations `16` months apart based on when they were placed on the market. 🟢 **An inventory
with placement dates is becoming a compliance artefact in its own right** — and almost nobody
has one.

### 🟡 T6 — The instrument is part of the finding

🔵 This KB spent thirteen passes recording *"GitHub Trending: NOT MEASURED"* and one pass
recording *"the API is gone"*. 🔴 **Both were artefacts of a gated lane inside the measuring
environment, and the `249`-byte body of the `403` said so the whole time.** 🟢 Diagnosis in
[`repos/foundations.md`](../repos/foundations.md).

🟡 **Trend for anyone building agentic research pipelines, which is most of this KB's
audience:** as agents acquire more lanes to the same resource — direct `HTTP`, a CLI, an MCP
server, a page fetcher — **a failure in one lane stops looking like a failure and starts
looking like a fact about the world.** 🔴 The `0` that gets published is indistinguishable
from the `0` that is true. 🟢 **The defence is cheap and this pass proves it: read the error
BODY, and ask the gate a question it will answer *(`rate_limit` returned a full live quota)*
before declaring a source dead.**
## Pass 192 — 2026-10-14

🆕 🟢 **The trend this pass measures is about the SHELF, not the market: after `191` passes,
a recovered discovery channel returns `84`% already-known.** `31` candidate repositories
surfaced, `7` with zero prior mention here, `5` of those actually education. 🔵 **Open-source
education AI has stopped producing new top-level projects faster than this KB can read
them** — the frontier has moved inside the projects that already exist.

### 🟢 T1 — The study layer is being built as agent SKILLS, not as platforms

🔴 **The second-largest `edtech`-topicked repository on GitHub is a PDF→skill compiler.**
[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) — `34 799`★,
created `2026-05-01`, `5` months old. 🔵 Next to it:
[`mohi-devhub/antivibe`](https://github.com/mohi-devhub/antivibe) *(`1 121`★, `MIT`, **`15`
paths total**)* turns generated code into a deep dive;
[`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) ships Bloom's 2-sigma research as a skill;
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
*(`854`★)* is `165` skills; [`O0000-code/awesome-academic-skills`](https://github.com/O0000-code/awesome-academic-skills)
*(`48`★, `CC0`)* indexes them.

🟢 **Signal: `15` paths at `1 121`★.** The unit of education software is shrinking from a
deployable platform to a few files of pedagogy that run inside someone else's harness.
🔴 **Commercial consequence: the thing a client adopts no longer has a deployment, so it has
no procurement, no security review, and no owner.** That is an opening and a liability in the
same sentence.

### 🔴 T2 — The agent layer moved into the platform, and p192 adds the liveness half

🔵 p191 measured the relocation: Chamilo ships `68` native MCP tool definitions, `47` writes,
`0` audit rows. 🆕 **This pass adds what the recovered channel can see that `git` cannot.**
🔴 **`archived` is invisible to `ls-remote`** — an archived repository answers identically to
a live one — and the first archived row on this shelf is a `582`★ LATAM platform
*(`menthorlabs/menthor`)*. 🟡 **`updated_at` keeps moving on it**, so the one field that looks
like liveness is the one that isn't.

### 🟢 T3 — Domain tutoring over MCP, outside the gradebook

🟢 [`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server) —
`Apache-2.0` *(`10 708` B)*, `121`★, `291` paths — is **computational fluid dynamics tutoring
with Socratic questioning**, not an LMS wrapper. 🔵 Paired with
[`taybenlor/runno`](https://github.com/taybenlor/runno) *(`773`★, `MIT`, sandboxed execution
in-browser **and over MCP**)*, the two supply what every "AI tutor" demo quietly lacks:
**a tutor that can run the learner's work.** 🔴 Both are small and single-maintainer; the
pattern is the finding, not the repositories.

### 🔴 T4 — Governance is the universal buy, and it is now dated in three regions

🔵 Not a forecast — three dates and a number:
🔴 **EMEA `2026-12-02`** *(Art. `50(2)` marking, seven weeks out)*;
🔴 **North America `2026-07-01`** *(Ohio's district AI-policy mandate, already passed)*;
🔴 **APAC `2026-01`** *(South Korea's AI Basic Act in force, education "high-impact")*;
🟢 **LATAM `87`% using / `26`% governed** *(UNESCO IESALC, `200` institutions, `19` countries)*.
🟢 **Every region now has either a deadline or a measured gap. None has a capability shortage.**

### 🔴 T5 — The NonCommercial curriculum trap is not regional

🔵 This KB warned about `CC-BY-NC-SA` curriculum as a LATAM risk. 🆕 **Measured this pass:
[`enkidevs/curriculum`](https://github.com/enkidevs/curriculum), `833`★, `5 345` paths,
`LICENSE.md` = `189` B of `CC-BY-NC-SA-4.0`, in English.** 🔴 **The trap tracks the asset
class, not the language.** Any curriculum repository is `CC-*` until its bytes say otherwise,
and popularity plus recent commits is not evidence of a usable licence — 🟢 which is the
whole argument for reading `LICENSE` from the tree, as this KB does on `1 273` rows.

### 🟡 T6 — Market sizing remains unusable, and the spread got worse

🔴 Three firms, same year: `$10.6B` *(2026)* → `$42.5B` *(2030)*; `$12.3B` by `2026`;
`~$6B` *(2024)* → `$32B` *(2030)*. 🔴 **A `2`× spread on the CURRENT year.** 🟢 Direction is
consistent and that is all the number is good for; every one of this pass's sources on sizing
was a commercial research firm or a vendor blog, and none published a method.

### 🔵 T7 — Method, carried forward: a channel that answers `0` is worse than one that refuses

🆕 **The recovered search channel returns `total_count: 0` with a SUCCESS status for an
over-conjoined free-text query** — measured twice this pass, once in English, once in Spanish.
🔴 **A refusal gets recorded as a gap; a `0` gets published as a fact.** The Spanish query's
`0` would have become *"no LATAM-language education repositories"* in any pipeline that
trusted it. 🟢 **Rule for p193: a `0` from a free-text query is NOT MEASURED until the same
question is asked with a `topic:` or `in:name` qualifier.**
## Pass 191 — 2026-10-14

🆕 🔴 **The trend this pass measures is a RELOCATION: the agent layer has moved from a plugin
into the platform, and the accountability layer did not move with it.** Chamilo ships `68`
MCP tools and `0` audit rows. Open edX's facade ships `9` scopes and an audit log it never
guards against deletion. 🔵 **Capability is being shipped by platform vendors; attribution is
being left to the integrator.**

| # | trend | measured this pass, from source |
|---|---|---|
| 🆕 `T1` | **The agent layer is becoming a platform feature.** For eleven passes this KB tracked education agents as third-party MCP servers. Chamilo `2.1.0` ships `68` tool definitions natively, with OAuth 2.1 resource metadata | `chamilo/chamilo-lms` HEAD `6f9bb2c61985`, `67` sources read at that sha; `config/packages/mcp.yaml` |
| 🆕 `T2` | **Permission models are maturing; DESTRUCTION models are not.** Two platforms, two shapes, same hole: Open edX can narrow a key nine ways and mis-assigns `destructive` by hand; Chamilo enforces `48` role checks in code and cannot narrow a key below the user | `evidence/agent-layer-two-platforms.2026-10-14-p191.tsv` |
| 🆕 `T3` | **The attribution gap is in the STANDARD, not the implementations.** `openfun/ralph` enforces authority on write *(server-assigned unless the caller holds `authority/write`)* and filters by it on read in all four backends. Its exclusion of `authority` from dedupe equivalence is **mandated by the xAPI specification**, by its own docstring — and ralph is STRICTER than the spec on `timestamp` and `version` | `src/ralph/utils.py:167`-`186`; `api/routers/statements.py:115`-`133`; `api/auth/user.py:18` |
| 🆕 `T4` | **An HTTP verb can decide who gets the credit.** In ralph, `POST` enriches authority then forwards; `PUT` forwards then enriches. A forwarded `PUT` carries the client's own unvalidated `authority`, while the locally stored copy is correctly attributed | `api/routers/statements.py` `put()` vs `_post_statements_standard()`; `api/forwarding.py` sends `json=statements` verbatim |
| 🆕 `T5` | **Copyleft has moved into the CONTENT layer, where buyers do not look for it.** The two agent-skill libraries that matter this week are `CC-BY-SA-4.0` and `CC0-1.0` — a share-alike obligation and a public-domain dedication, neither of which a code-licence review would surface | `GarethManning/education-agent-skills` `LICENSE` `1 230` B; `O0000-code/awesome-academic-skills` `CC0-1.0` |
| 🟢 `T6` | **North America's constraint is trust, not capability**, and the gap widened: faculty intent `76`% → `67`%, and only `26`% of US/Canada faculty say they are excited about AI against `57`% in APAC | DEC `2026` global survey *(n = `45 398`, `35` countries)*, secondary — the host is unreachable |
| 🟢 `T7` | **Student use is universal and integration is not.** `88`% of students use AI; `15`% say it is integrated into many of their courses; `29`% think their instructors are equipped to guide them | same survey, secondary |
| 🟢 `T8` | **Outside Saudi Arabia, the Gulf governs AI used BY learners and not AI used ON them.** The UAE's `2026-02` classroom guide is binding and detailed; Qatar and Bahrain reach learner data only through general data-protection statutes | `evidence/gulf-ai-on-learners.2026-10-14-p191.tsv` |

### 🔵 The method lesson, which is about where a KB's own errors live

p190's lesson was *"label the channel per CLAIM, not per pass"*. 🟢 **p191 adds the one it
paid for: label the POPULATION too.** `ACTION NK` asked for a sweep over *"all `160` published
licence rows"*, and `160` was never derived — it was what the previous pass happened to
reach. The real population is `1 273`. 🔴 **A sweep that calls itself exhaustive and names a
number it did not derive is a sampling study wearing a census's clothes.**

🟢 **And the second lesson is about which rows an instrument gets wrong.** `P1059` accused
three rows falsely, and the three were not sloppy rows — they were the rows whose cells
**explain** their licence *(`ECL-2.0`, *"an OSI-approved `Apache-2.0` derivative"*)*. 🔵 **A
careful row contains two licence names, so an extractor that cannot spell the right one will
find the wrong one. Precision must be measured against the best-documented rows, not the
worst.**

## Pass 190 — 2026-10-14

🆕 🔴 **The trend p189 named is now measured in two unrelated codebases, and the measurement
CORRECTS the claim rather than confirming it. p189 said nobody protects the durable record of
a human decision about a learner. Both artefacts read this pass DO protect the record — in
code, deliberately, with comments explaining why. 🔴 Neither protects WHO ACTED.**

### 🔴 Trend `1` — the record is guarded, the actor is not

| artefact | the record | the actor |
|---|---|---|
| [`openfun/ralph`](https://github.com/openfun/ralph) *(`MIT`, LRS/xAPI)* | 🟢 **`409 CONFLICT` on BOTH write paths**, raised before `BACKEND_CLIENT.write` is reached, with the refusal explained in a source comment. An equivalent re-`PUT` takes a bare `return` and writes nothing | 🔴 **`statements_are_equivalent` compares a SUBSET.** `authority` — the field naming who asserted the statement — and `stored` are **excluded by name** in the code's own comment: *"'authority' and 'stored' remain ignored."* |
| [`openedx-mcp`](https://pypi.org/project/openedx-mcp/) `0.1.5` *(`AGPL-3.0`, the Open edX facade)* | 🟢 `MCPAuditLogAdmin` sets **`has_add_permission` → `False`**, **`has_change_permission` → `False`**, and **every field readonly**. The audit row is written **before** the write, and the write is refused if it cannot persist | 🔴 **`has_delete_permission` is NEVER overridden** → Django defaults it to `user.has_perm("delete_mcpauditlog")`, and no `actions` list is declared, so the default **"Delete selected objects"** bulk action survives. 🔴 **Second path, needing no delete permission at all:** `MCPAuditLog.key` and `.user` are `on_delete=models.SET_NULL`, so deleting a key or a user **NULLs attribution on every row it produced** |

🔵 **Two codebases, two languages, two layers of the stack, the same omission.** 🟢 **And in
both cases the author demonstrably thought about integrity** — ralph's refusal is documented
in a comment; `openedx-mcp` blocked add, blocked change and froze every field. 🔴 **The gap is
not inattention. It is an incomplete enumeration: `add`, `change`, `delete` — and one of the
three was not listed.**

🟢 **So the trend is sharper and more sellable than p189's version.** *"Nobody protects the
record"* invites a rebuttal from any engineer who has read either codebase. 🟢 ***"The record
is protected and the actor is not"*** is true in both, demonstrable from source, and it is
precisely the property a regulator, a DPO or an exam board asks about — because an audit
trail that cannot say **who** is not an audit trail.

🔵 **Consequence for `ralph` specifically, and it is not the one p189's falsifier predicted.**
Because equivalence means **no write at all**, the append-only guarantee has **no hole**: a
re-`PUT` differing only in `authority` answers `204` and is **silently DISCARDED**. 🔴 So a
client cannot distinguish *"your statement was stored"* from *"your statement was dropped
because another authority already claimed that id"*. 🟢 **Integrity is intact; attribution is
swallowed.** The fix belongs in `Pattern 32` step `3c` and costs one guard, not weeks: mint
statement ids per authority, or reject on authority mismatch at the ingest proxy.

### 🔴 Trend `2` — the agent surface arrives better-governed than this KB assumed, and worse-guarded where it counts

🟢 p189 recorded the Open edX agent layer as ungoverned. 🔴 **It is not**: nine enforced
scopes, `destructive` as an additive scope, a single-use confirm token bound to a `sha256`
of `(tool, user, payload)`, per-`(key,tool)` rate limits tuned to blast radius, live
privilege re-checks, `SHA-256` key hashing. 🔵 **This is a genuinely careful design, and the
correction matters because the previous verdict would have lost a client an integration that
is safer than the one they would have written themselves.**

🔴 **And yet the two guards that are wrong are wrong in the direction that costs a learner:**

- 🔴 **`reset_student_attempts` carries `write:users` and NOT `destructive`**, and with
  `delete_module=True` deletes a learner's submitted block state, irreversibly. 🟢
  **`deactivate_user`, which the package's own docstring calls *"the reversible `is_active`
  flag"*, DOES carry `destructive`.** 🔵 **The flag is on the reversible tool and off the
  irreversible one** — so a key provisioned specifically to prevent deletions can delete work.
- 🔴 **`update_course_settings` changes a GRADING POLICY with `require_confirm=False`** —
  *evaluation of learning outcomes* is Annex III education by name.

🟢 **The emerging trend across p188–p190 is now stateable as a rule: the agent layer's
PERMISSION model is maturing faster than its DESTRUCTION model.** Scopes, handshakes and rate
limits are arriving. What is still assigned by hand — and therefore still wrong — is **which
operations are irreversible**.

### 🔴 Trend `3` — the method trend, and this one is about this KB

Three consecutive passes have found the same class of defect in this KB's **own
instruments**, one segment further left each time:

| pass | a thing stood in for a thing | consequence |
|---|---|---|
| p189 | a **substring** stood in for a **path** — `LICENSE` probed where the file was `LICENSE.TXT` | a published `NO_LICENCE_FILE` verdict on this KB's recommended permissive entry point, refuted |
| 🆕 p190 | a **substring** stood in for a **token** — case-insensitive `emotion` fires inside `deviceMotionEvent`, and `node_modules` ships `application/emotionml+xml` | 🔴 `16` false emotion-inference hits against a repository **with no camera**. Nearly a false accusation under a EUR `35`M prohibition |
| 🆕 p190 | a **`limit`** stood in for a **path list** — `probe_plan(limit=16)` never reaches `.md`, which is one of this KB's four standing licence paths | p189's `224`-probe sweep was **narrower than the list it extended**; `7` of `160` rows published as grant-absent do carry a grant |

🟢 **The rule that covers all three: a cheap proxy for a precise thing must be tested against
the case that distinguishes them, or it is not a measurement.** `P1058` encodes this literally
— one of its tests asserts that the *unanchored* pattern **still fires** on the
`deviceMotionEvent` fixture, so a future edit that drops the `\b` fails loudly instead of
silently widening.

### 🔴 Trend `4` — the channel, and the figure this KB just lost

🔴 **`github.com` HTML and `api.github.com` are `403` for this entire session.** Reading named
code is at full fidelity; **discovering** code is gone. 🔴 **`ACTION NE` is NOT RUN** as a
direct result: the new-supply rate is measured over `12` `github.com/topics` pages.

🔵 **And that is the sharpest method lesson of the pass, because of what p189 did with that
figure.** p189 **retired** the absent rate *(it had been measuring this KB's own ingest
backlog — `Gap 428`)* and **promoted** the new-supply rate to be *"this KB's published
coverage measure"* — **on one measurement, over a channel that was gone one pass later.**

🟢 **p189's rule was: before re-measuring a number, ask what would have to be true for it to
move. p190 adds the prior question: ask whether you will still be able to ASK.** A measure
whose channel is one policy change away from disappearing is a **reading**, not a measure.

🔴 **Where that leaves this KB, stated plainly: it currently has NO published coverage
measure.** The absent rate is retired; the new-supply rate has exactly one measurement
*(p189: `12` new slugs, `83`% absent, `239` rows)*. 🟢 **Quote it as *"one measurement,
`2026-10-14`, p189, over `github.com/topics`"* — with the channel named — or quote nothing.
Do not present it as a rate.** 🔵 And the corollary for pre-registration: a falsifier aimed
at a channel you do not control is a falsifier that can neither fire nor fail.

### 🟢 Trend `5` — the regulatory calendar stopped being a single date

🔵 The market reads the Omnibus as *"education moved to December `2027`"*. 🔴 **Four dates are
live or nearly live, and none of them is that one:**

| date | duty | status |
|---|---|---|
| 🔴 `2025-02-02` | **Art. `5(1)(f)`** — inferring emotions in education institutions | **PROHIBITED, live, EUR `35`M / `7`%, never deferred** |
| 🔴 `2026-08-02` | **Art. `50` transparency** + **GPAI provider obligations** | **LIVE — did not move** |
| 🔴 `2026-12-02` | **Art. `50(2)`** machine-readable marking of pre-existing generative AI | **seven weeks from this pass** |
| 🔴 `2027-03-01` | **Vietnam** — education on the high-risk list *(automated assessment, behavioural monitoring)*; grace only for systems running before `2026-08-15` | **nine months BEFORE the EU** |
| `2027-12-02` | EU **Annex III** education duties | the deferred one everyone quotes |

🟢 **So the trend is that the binding constraint has moved OUT of the EU.** For a
multi-region client the first wall is Vietnam, the live walls are `Art. 50` and the `5(1)(f)`
prohibition, and `2027-12-02` is the **last** date to plan for, not the first.

**Full measurement:**
[`evidence/ralph-equivalence-subset.2026-10-14-p190.tsv`](../evidence/ralph-equivalence-subset.2026-10-14-p190.tsv)
· [`evidence/openedx-mcp-tool-surface.2026-10-14-p190.tsv`](../evidence/openedx-mcp-tool-surface.2026-10-14-p190.tsv)
· [`evidence/channel-inversion-github-blocked.2026-10-14-p190.tsv`](../evidence/channel-inversion-github-blocked.2026-10-14-p190.tsv)
· [`compose/code/p190-affect-inference-scan`](../compose/code/p190-affect-inference-scan/README.md)

## Pass 189 — 2026-10-14

🆕 🔴 **The trend p188 named — nobody protects the durable record of a human decision about
a learner — now has its mechanism measured on BOTH sides, and the result is sharper than the
claim: one layer refuses the overwrite in code, the layer above it hands the deletion to an
agent. The protection exists. It is in the wrong place.**

### 🔴 Trend `1`, amended — the audit record: protected against the client, exposed to the operator and the agent

| who tries to destroy the record | what stops them | measured |
|---|---|---|
| 🟢 an **xAPI client** re-writing a statement | 🟢 **`409 CONFLICT`, in code, both write paths** | [`openfun/ralph`](https://github.com/openfun/ralph): `PUT` *(lines `624`–`700`)* and `POST` *(via `_filter_existing_statements`)* deep-compare and **return before `BACKEND_CLIENT.write` is reached**. Source comment, verbatim: *"In the case that the current statement is not equivalent to one found in the database we return a 409, otherwise the usual 204."* 🟢 Append-only **by construction, not convention** |
| 🔴 an **operator** with store credentials | 🔴 **nothing** | `BaseOperationType` declares `DELETE`/`UPDATE`; default `INDEX` overwrites at a specific id; `--es-op-type` exposes all four on the CLI *(p188)* |
| 🆕 🔴 an **AI agent** holding one MCP key | 🔴 **nothing** | `tutor-contrib-openedxmcp`'s LMS tool list includes **`retire`**, authorised only by `is_staff`/`is_superuser`. 🔴 `/health` unauthenticated. `1`★, `AGPL-3.0` |

🔵 **Why the amendment matters more than the original trend.** p188's claim was that the
artefact is unprotected. It is not — at the API layer it is protected properly, and the
protection is demonstrable in a single live `409` rather than argued. 🔴 **But the agent
layer this KB has spent eleven passes mapping reaches the same artefact with no equivalent
refusal, and it got there in the same pass the surface was discovered.** 🟢 **The trend is
therefore: the agent layer is being built faster than the guarantees underneath it.** That
is a sentence a client's DPO will recognise, and it prices as design work rather than fear.

### 🆕 🔴 Trend `2`, new — the live prohibition everyone is reading past

🔴 **Article `5(1)(f)` of the EU AI Act prohibits inferring emotions from biometric data in
EDUCATION INSTITUTIONS, and has since `2` February `2025`.** The Digital Omnibus
*(Regulation (EU) `2026/1744`)* delayed **high-risk** duties to `2027-12-02`; it did **not**
delay **prohibitions**. Penalty ceiling: **EUR `35`M or `7`% of worldwide turnover.**

🔵 **The trend is the MISREADING, not the rule.** Eight consecutive passes have found the
un-amended high-risk date in circulation, and the attention it absorbs is the reason the
prohibition goes unnoticed: the whole market is discussing a `2027` deadline while sitting
on a `2025` one that carries the Act's maximum penalty.

- 🟢 **Not caught:** behavioural engagement analytics that do **not** infer emotions. The
  prohibition targets **emotion inference from biometric data**.
- 🔴 **Explicitly unresolved:** proctoring, where the Commission's guidelines leave open
  whether emotion inference as a **secondary** functionality is caught.
- 🔵 **So the deliverable is a boundary, not a product.** Every proctoring and
  engagement-analytics row in this KB now needs the same question asked before it is
  recommended into an EU engagement.

### 🟢 Trend `3`, strengthening — automatic grading is the surface that keeps getting regulated

Four independent jurisdictions, four instruments, one target:

| jurisdiction | instrument | what it does to automatic grading |
|---|---|---|
| 🔴 **Vietnam** | Decision `33/2026/QĐ-TTg` | 🔴 **automatic grading or ranking of students is HIGH-RISK by statute** — one of exactly three education entries in `46` systems |
| 🆕 🔴 **Oklahoma** | district AI policy law | 🔴 **bars AI from being the main basis for high-stakes decisions about students** |
| 🔴 **South Korea** | AI Basic Act, in force `2026-01-22` | names **education** among "high-impact AI" sectors; requires **human monitoring and intervention** |
| 🟡 **EU** | AI Act Annex III | education high-risk from `2027-12-02` |

🟢 **And the commercial counterpart, unchanged and corroborated:** the Digital Education
Council LATAM Survey `2026` found faculty's **lowest** adoption is in **assessment**.
🔵 **The one thing the market has not automated is the one thing four regulators have
named.** That is not a coincidence to explain away — it is the engagement, and it is the
same one in every region: make assessment defensible.

### 🆕 🟢 Trend `4`, new — the credential is the only durable artefact, and it is migrating

🟢 `topics/open-badges` is mid-migration from Open Badges `2.0` to **`OB 3.0` / W3C
Verifiable Credentials**, and the licence split tracks the migration exactly:
**permissive on the new side** *(`OB3DefinitionWidget`, `dcc-credential-co-writer-monorep`
on the MIT-led Digital Credentials Consortium stack, `iblai/wallet`, `proven`,
`signet-campus` — all `MIT`)*, **copyleft on the old** *(`obadgen` `AGPL-3.0`,
`openbadgeslib` `LGPL`)*.

🔵 **Connect it to Trend `1` and it stops being a standards story.** A verifiable credential
is durable **by cryptography**; an xAPI statement is durable **by an application-layer
`409`** that an operator or an agent can walk around. 🟢 **So the only artefact in this stack
that survives its own platform is the credential** — and the permissive implementations are
all on the new standard. 🔵 That is the architectural recommendation this trend produces.

### 🟢 Trend `5` — governance is absent at a rate that makes the regulation academic

| measure | value |
|---|---|
| 🔴 schools worldwide with AI guidance | 🔴 **`7`%** — and **`40`% of those informal only** |
| 🟢 students saying assessment is already changing because of generative AI | 🟢 **`65`%** |
| students saying AI is integrated in MANY courses | `15`% |

🔵 **`7`% against `65`% is the whole market in two numbers**: the practice has changed, the
governance has not, and four jurisdictions have started legislating the gap. 🟡 Figures are
secondary-sourced *(a roundup updated `2026-10-07`; Digital Education Council Global Survey
`2026`)*.

### 🔴 A standing caveat this KB should state once per page instead of per claim

🔴 **Every government primary source attempted this pass was unreachable** — `eur-lex`,
the Council's document server, two Commission hosts, Saudi Arabia's state news agency —
**while the secondary legal-commentary layer was fully reachable and
`raw.githubusercontent.com` served every byte of code asked of it** *(`880`+ fetches, HTTP
codes checked)*. 🔵 **So this KB reads CODE at primary fidelity and REGULATION at secondary
fidelity, by construction.** That is not a flaw in any single claim; it is a property of the
channel, and it belongs in the open once rather than re-argued per date.

Evidence: [`ralph-append-only`](evidence/ralph-append-only.2026-10-14-p189.tsv) ·
[`openedx-mcp-server`](evidence/openedx-mcp-server.2026-10-14-p189.tsv) ·
[`eu-2026-1744-corroboration`](evidence/eu-2026-1744-corroboration.2026-10-14-p189.tsv) ·
[`gulf-education-instruments`](evidence/gulf-education-instruments.2026-10-14-p189.tsv)

## Pass 188 — 2026-10-14

🆕 🔴 **The trend this pass can PROVE is that the durable record of a human decision about
a learner is the artefact nobody is protecting — and it now has two independent instances
in two unrelated projects, against three jurisdictions that require it.**

### 🆕 🔴 Trend `1` — the human-oversight record is protected by CONVENTION, never by the STORE

🔵 p187 found this once and called it a finding. 🟢 **p188 found it again, in a different
project, at a different layer, and that makes it a defect CLASS.**

| instance | the store | the defect |
|---|---|---|
| p187 | [`ningkaikok/dotty-tutor`](https://github.com/ningkaikok/dotty-tutor) `teacher_review_events` | 🔴 `corrected_assessment` — the teacher's override of an AI grade — is `ondelete="CASCADE"` from **two** parents. Deleting the class deletes the correction |
| 🆕 p188 | [`openfun/ralph`](https://github.com/openfun/ralph), the `xAPI` LRS | 🔴 **no immutability at all.** No `@router.delete` on the LRS API — but `BaseOperationType` declares `DELETE` and `UPDATE` *("updates or overwrites an existing record")*, `--es-op-type` exposes them as a CLI option, and `default_operation_type = INDEX` **overwrites** a re-written statement id |

🔴 **`ralph`'s protection is the ABSENCE OF AN HTTP ROUTE.** 🟢 That is genuinely useful —
a tutoring agent writing through the LRS API cannot erase its own trail — 🔴 **but anyone
holding Elasticsearch or MongoDB credentials deletes or overwrites statements with ralph's
own CLI.** 🔵 And `xAPI`'s own substitute for deletion is absent too: `voidedStatementId`
is accepted and documented as **"*Not implemented*"**.

🔴 **Do not be reassured by the word "Immutability" in the codebase.** The single
occurrence is the `xAPI` `format=canonical` parameter's docstring, about how Activity
Objects and Verbs are REPRESENTED. 🔵 It is not a storage guarantee, and a search for the
word will find it and mislead.

🟢 **Why it is a trend and not a pair of bugs: both projects are well built, and both got
this wrong in the same direction.** 🔵 Course-shaped systems make the class the aggregate
root and cascade everything beneath it — right for pedagogy, wrong for audit. Record-store
systems optimise for write throughput and queryability — right for analytics, wrong for
evidence. 🟢 **Nobody in this vertical is building for the subpoena, and three regimes just
started asking for one:** NA *(Oklahoma, Maryland — human review of high-stakes decisions
about students)*, EU *(Annex III high-risk educational assessment, obligations
`2027-12-02`)*, and 🆕 APAC *(Vietnam's **Decision `33/2026/QD-TTg`**, which names
**automatic grading or ranking of students** one of its `46` high-risk systems)*.

🟢 **The commercial shape: this is a finding a studio can walk into a meeting with,
demonstrate in one live delete, and sell the fix for.** Pattern `32` is that fix, and
step `3` now carries the WORM store it did not before.

### 🆕 🔴 Trend `2` — the agent-tool layer is forking by PLATFORM POLICY, not by licence

🔵 p187's headline was that the `MCP`-over-the-LMS layer is `11` repositories deep and
unnamed by analysts. 🟢 **p188 adds the structural fact that decides engagement pricing:
the layer is not spreading evenly, and the reason is not copyleft.**

| platform | agent surface | licence of the platform |
|---|---|---|
| 🟢 **Moodle** | 🟢 **three independent `MCP` servers** | 🔴 `GPL-3.0` — **strong copyleft** |
| 🟢 Canvas · Brightspace · Sisu · `SCORM` | 🟢 at least one each | mixed |
| 🔴 **Open edX** | 🔴 **an official `MCP` CLIENT, and a documented refusal to ever be a server** | 🔴 `AGPL-3.0` |

🔴 **p187 and `ACTION MV`'s own limb both guessed that `AGPL` explained Open edX's
absence. This KB's own Moodle row refutes it: `GPL-3.0` is strong copyleft and it carries
three servers.** 🟢 What distinguishes Open edX is that
[`openedx/openedx-ai-extensions`](https://github.com/openedx/openedx-ai-extensions) routes
extension through its own framework and states, in its docs, **_"will never expose MCP
server functionality"_**.

🔵 **Why that distinction is worth money.** A licence objection can be negotiated,
dual-licensed, or waited out. 🔴 **A documented architectural decision cannot.** 🟢 So an
Open edX engagement should be scoped as *permanently owning the server half* — and
simultaneously told **not to build the orchestration half**, because an official one
exists. 🟡 With two caveats a client must hear in the first meeting: it is `AGPL-3.0`, and
its own README calls it **"experimental"** and a **"proof-of-concept"**.

### 🆕 🟢 Trend `3` — in education, the licence splits by SCOPE, and the content half is the asset

🟢 **New shape, measured twice this pass:** permissive for the code, **`CC BY`** for the
content.

- [`ktwyw/python-for-engineers`](https://github.com/ktwyw/python-for-engineers) — *"Code
  … is licensed under the MIT License. Teaching materials (notebooks, README files,
  cheatsheets, datasets created for this course) are licensed under **CC BY 4.0**."*
- [`siskinskai/spedlex`](https://github.com/siskinskai/spedlex) — *"Code: MIT. Data
  (everything in `data/`, `schema/` and the term lists in `sources/`): **CC BY 4.0**."*
  `LICENSE` `1 077` B + `LICENSE-DATA` `17 023` B.

🔴 **In both rows this KB published `MIT`, and in both the `CC BY` half is the half a
studio wants** — the course notebooks; the SPED vocabulary. 🔵 **This is structural, not
coincidental: education repositories are code PLUS content by construction.** A course is
notebooks, a tutor is an item bank, a de-identifier is a term list. 🟢 So in this vertical
the split-scope licence is the EXPECTED shape, and it becomes an intake check:
[`P1056`](../compose/code/p1056-split-scope-licence/README.md), `16`/`16` tests passing.

🟢 **The practical rule for a client conversation: `CC BY` is perfectly usable — attribution
is a cheap obligation — but it is IRREVOCABLE and it travels into the deliverable.** 🔴 A
white-label course built on `CC BY` notebooks without attribution is a licence breach on
delivery, which is the same failure mode `P1054`'s `graspful` has and arrives by a
completely different route.

### 🟢 Trend `4` — the credential layer is migrating, and the permissive rows are all on the new side

🟢 `topics/open-badges` — the smallest page in this census and its control — is mid-shift
from Open Badges `2.0` to **`OB 3.0` / W3C Verifiable Credentials.** 🔵 The licence split
is remarkably clean: 🟢 **permissive on the new standard** *(`OB3DefinitionWidget`,
`dcc-credential-co-writer-monorep`, `iblai/wallet`, `proven`, `signet-campus` — all
`MIT`)*, 🔴 **copyleft on the old** *(`obadgen` `AGPL-3.0`, `openbadgeslib` `LGPL`)*.

🔵 **And it connects to Trend `1`.** Where three regimes demand a durable record of a
human decision, 🟢 **a verifiable credential is the only artefact in this stack that is
durable by CRYPTOGRAPHY rather than by convention** — the LRS is deletable, the schema
cascades, the signature does not.

### 🔴 Trend `5` — this KB's own figures are its least reliable input, and that is now measured

🔵 Three of p188's five discharged actions fired by retiring something p187 published
**yesterday**. 🟢 Written down because the pattern matters more than any one correction:

| p187 published | p188 measured |
|---|---|
| `79`% of recency-sorted rows absent from the census | 🔴 **`67.5`% unfiltered, `64`% with `api-evangelist` removed.** Limb `2` fired |
| *"for a Moodle-plugin-shaped repo, 'no licence file' is close to uninformative"* | 🔴 **Backwards. `15` of `17` plugin-shaped rows DO ship a licence file**, `14` as full `GPL` text at `35 147`–`35 200` B |
| *"`AGPL` is the likely cause"* of the Open edX gap | 🔴 **Refuted by this KB's `GPL-3.0` Moodle rows** |
| canonical `MIT` at `1 062`–`1 093` B | 🟡 **`1 063`–`1 114` B over `30` rows.** No row misclassified — the instrument had headroom; the published figure did not |
| `api-evangelist` = `23` rows | 🟢 **REPRODUCED EXACTLY.** The one figure that held |

🔵 **The method rules now in force, each earned by a failure:**
- 🟢 p186: **an absence names its probe.**
- 🟢 p187: **a probe returning the same verdict for every row has measured nothing** — run a
  known-positive through every sweep. 🔵 It saved this pass twice: a slug index built with
  PCRE syntax handed to `grep -E` returned MISSING for all five positive controls.
- 🆕 🟢 p188: **a census over a RECENCY-sorted page must store its ROWS, not its counts.**
  p187 stored counts, so an `11.5`-point drop one day later cannot be attributed to the page
  moving rather than the instrument changing. All `240` rows of this pass are stored.
- 🆕 🟢 p188: **a probe whose verdict is a SUBSTRING has not measured a licence.** A bare
  `ISC` alternative with no word boundary matched inside **"Disclaimer"** and reported four
  `Apache-2.0` repositories as `ISC`.
- 🆕 🟢 p188: **a README claim is a cue to re-probe, exactly like a badge** — and the
  re-probe came back empty on both rows that made one.

## Pass 187 — 2026-10-14

🆕 🟢 **The trend this pass can prove is an ASYMMETRY between the code and the commentary, and it
is the only finding on these eight pages with a shelf life measured in weeks rather than quarters.**

### 🆕 🔴 Trend `1` — the `MCP`-over-the-LMS layer is real, populated, and UNNAMED

🟢 **A targeted search for *agentic tutoring + `MCP` + learning management* returned, verbatim,
*"nothing specific on `MCP` (Model Context Protocol)"* and recommended a follow-up search as the
next step.** 🟢 **The same week's topic-page census returned `11` repositories implementing exactly
that, `7` of them new to this KB, with grants verified byte by byte.**

| what the commentary names | what the repositories do |
|---|---|
| 🟡 "agentic AI as institutional infrastructure", pilots → production | 🟢 **three independent `MCP` servers for Moodle alone**, one of them an in-tree web-service plugin |
| 🟡 Instructure's **IgniteAI Agent** — retrieves course context, prepares changes, acts only within the user's existing permissions, with approval at key moments | 🟢 the same architecture, permissively licensed, per platform: Moodle, Canvas, Brightspace/D2L, Sisu, `SCORM` |
| 🔴 **nothing on `MCP`** | 🟢 `MIT` on `5` of `7` new rows |

🔵 **Read this as a timing statement, not a technology one.** 🟢 The incumbent *(IgniteAI)* has
already defined the governance shape clients will expect — **permission-scoped, approval-gated**.
🟢 **The open components to build that shape exist now.** 🔴 **The analyst sentence that makes it
obvious has not been written yet, and when it is, the position stops being differentiating.**

### 🆕 🟢 Trend `2` — compliance stopped being a clause and became a dependency

🔵 For many passes this KB described student-data protection as a design obligation and a paragraph
in a statement of work. 🟢 **`topics/ferpa` — a `40`-repository page this KB had never read at any
sort order — returned it as installable software:** `Rego` policy bundles
*([`gopal`](https://github.com/Principled-Evolution/gopal), `Apache-2.0`)*, a `FERPA` + Title IV
guardrail *([`regrails`](https://github.com/Polycentric-Labs/regrails), `Apache-2.0`)*, a RAG
pre-filter *([`haystack-ferpa-filter`](https://github.com/ashutoshrana/haystack-ferpa-filter),
`Apache-2.0`)*, a de-identification vocabulary for special education
*([`spedlex`](https://github.com/siskinskai/spedlex), `MIT`)*.

🟢 **Why now is legible from the regulation:** Oklahoma and Maryland moving to **require human
review and bar AI from high-stakes student decisions**; the EU naming education access and
assessment high-risk; 🔴 **and Vietnam becoming the second jurisdiction to put educational
assessment in a statutory high-risk tier.** 🔵 **Guardrails become a dependency at the moment
somebody can be fined. That moment is now, in three regions at once.**

### 🆕 🔴 Trend `3` — the human-oversight AUDIT RECORD is the artefact nobody is protecting

🟢 **This is the pass's most actionable finding and it came from reading one schema in full.**
`ACTION MP` reached [`dotty-tutor`](https://github.com/ningkaikok/dotty-tutor)'s
`apps/api/persistence/schema.py` *(`19 405` B, `Apache-2.0`)*.

🟢 **The human-oversight surface is one table, `teacher_review_events`**, and it is well designed
where it counts: `action` is `CHECK`-constrained to exactly `('reviewed', 'overturned',
'mastery_override')` — 🟢 **a clean three-value vocabulary for "a human looked", "a human overruled
the model", "a human set mastery directly"**, which is very close to what a regulator means by
meaningful human oversight.

🔴 **And its `corrected_assessment` column — the teacher's overturning of an AI grade — is
destroyed by `ondelete="CASCADE"` on TWO independent parents**: `class_id → learning_classes` and
`assignment_id → assignments`. 🔵 **Deleting a finished class or a single assignment silently
erases the evidence that a human corrected the machine.** 🟢 By contrast `knowledge_point_id`
carries **no** `ondelete`, so the pedagogical reference is protected while the audit trail is not.

🔵 **Generalise it past this repository, because it is not a bug in one project.** 🟢 **Course-shaped
data models treat a class as the aggregate root and cascade everything beneath it — which is right
for pedagogy and wrong for audit.** 🔴 **The three regimes above all require the record that this
default deletes.** 🟢 Pattern `32` is the fix: the oversight log must be **outside** the course
aggregate, and an `xAPI` LRS *([`ralph`](https://github.com/openfun/ralph), `MIT`)* is a
standards-shaped place to put it.

### 🆕 🟢 Trend `4` — LATAM's deficit is measurement, not adoption

🔴 **`TALIS` `2024`: Brazil `56`%, Chile `55`%, Colombia `53`%, Costa Rica `52`% of secondary
teachers used AI in the prior year, against an OECD average of `36`%.** 🟢 Uruguay reports `75`% of
public-school teachers *(Ceibal, `2026`)*. 🟢 UNESCO `IESALC`: `87`% of `200` institutions across
`19` countries use AI, 🔴 **`26`% have a strategy and `9`% evaluate what they deployed.**

🔵 **The standard regional narrative — LATAM as a late adopter needing to catch up — is
contradicted by the teacher-level data.** 🟢 **The honest pitch is the inverse: adoption already
happened, bottom-up and unmeasured, and the gap is governance and evaluation.** 🟢 And there is now
a named production reference in-region — **PUC Chile**, instructor-configured agents grounded in
validated course content, Canvas-integrated, centrally governed.

### 🟡 Trend `5` — the licence traps are getting harder, not easier

🟢 **Two new shapes, both of which defeat a body-matching classifier:**

- 🔴 **`P1054` — MIT's body with a clause bolted on.** [`graspful`](https://github.com/willwearing/graspful)'s
  *"O'Saasy License Agreement"* is MIT verbatim plus an anti-SaaS non-compete. 🟢 Instrument and
  `14` passing tests: [`compose/code/p1054-mit-plus-clause`](../compose/code/p1054-mit-plus-clause/README.md).
- 🔴 **`P971`, instances three and four** — `numbas-lti-provider` *(`Apache-2.0` in `560` B)* and
  `moodle-block_atrisk` *(`GPL-3` in `703` B)*: correct title block, terms at a URL. 🔵 **The patent
  grant is the only strong reason to prefer Apache over MIT, and it travels as a hyperlink.**
- 🟢 **And the inverse trap, from `ACTION MO`: Moodle's plugin rules REQUIRE `GPL` and the
  convention is a header block in every PHP file.** 🔴 **For a Moodle-shaped repository, "no licence
  file" is close to uninformative** — `onbirdev/moodle-webservice_mcp`'s grant sits in
  `version.php` and `lib.php` and nowhere else.

🔵 **The through-line across all three: a licence verdict is only as good as the PATH the probe
read, and "permissive" and "open source" have come apart.**

### 🔴 Trend `6` — a method correction this KB owes itself

🔴 **This pass's first grant sweep returned the same verdict — `NO-GRANT-FOUND` — for `36` of `36`
repositories.** 🟢 The cause was the instrument: `git ls-remote --symref` emits **two** lines ending
in `<TAB>HEAD`, the first being `ref: refs/heads/main`, so the SHA read `ref:` and every `raw` URL
`404`'d. 🟢 Fixed, then validated against a **positive control** *(`fsrs4anki-helper` → `MIT`,
`1 079` B, file named `License`, reproducing p186's published value exactly)* and a negative control
that still fails.

🔵 **The rule, cheap and general, and it belongs beside p186's "an absence names its probe":**
🟢 **a probe that returns the SAME verdict for every row has measured nothing. Run a known-positive
through any sweep before believing it.** 🔴 Had this gone unchecked, p187 would have published `36`
repositories as unlicensed — and three of p186's four headline recoveries were rows a previous pass
had wrongly closed exactly that way.

## Pass 186 — 2026-10-14

🆕 🟢 **The method trend this pass can prove is a correction to p185's own correction, and it is the
cheaper lesson of the two.** 🔵 p185 retired *"the channel is exhausted"* and replaced it with *"a
channel is a page PLUS a sort order"*. 🟢 **p186 finds the same error one level down: an ABSENCE is a
measurement, and it carries the shape of the probe that made it.** 🔴 **`Gap 423`: every *"no grant"*
on these eight pages is scoped to a probe that read `LICENSE`-cased paths and README prose. It never
read the ecosystem manifest, and it never read `License`.** 🟢 **Re-probing `41` such rows recovered
`3`, all permissive; a fourth came from a row closed on a correct rule applied wrongly.**

### 🆕 🟢 Trend `1` — the agent SKILL is acquiring REGIONAL CURRICULUM PROFILES

🔵 **p185 named the form: tutoring shipped as a skill for a harness the client already runs, not as
an application to host. One week on, the form has specialised.**

🟢 **[`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills)
*(`Apache-2.0`, `11 359` B)* takes Anthropic's K12 Teacher Skills workflow design and re-cuts it
against Chinese curriculum standards, local classroom practice and a REGION PROFILE** — the first
complete one being *Shanghai Primary Information Technology*. 🟢 **It is explicitly model-agnostic**
*(«不绑定 Claude、Codex、DeepSeek 或某一家模型»)*, with `Windows + Codex + DeepSeek Flash` named as
the currently-verified runtime.

🔵 **What this means for a studio, and it is a change of deliverable:** the unit of work is no
longer *a tutor* but **a curriculum profile for an existing skill set**. 🟢 **That is the most
exportable artefact this shelf has produced: the pedagogical workflow is upstream and permissive,
and the profile — standards, grade bands, local practice, assessment conventions — is the local
engagement.** 🔴 **And it is the first row on this shelf to make the regional-adaptation layer an
explicit, named, versionable thing rather than prompt-tuning inside a fork.**

### 🆕 🔴 Trend `2` — the EU high-risk clock moved, the prohibition did not, and the gap between them is the engagement

🟢 **Multiple sources this pass converge on a timeline this KB could not confirm at p185**, and they
now also report the procedural step that was missing:

| obligation | date, as reported | status of the reporting |
|---|---|---|
| 🔴 **Article `5`(1)(f) prohibition — emotion inference in education** | **in force since `2025-02-02`** | 🟢 **unchanged by the omnibus, consistently reported.** 🔴 A prohibition, with no conformity route |
| 🟡 stand-alone Annex III high-risk *(admissions, grading, level assessment, exam monitoring)* | **`2027-12-02`** | 🟡 reported as approved by the Council on **`2026-06-29`**, *"awaiting publication in the Official Journal"* |
| 🟡 high-risk embedded in regulated products | **`2028-08-02`** | 🟡 same instrument, same caveat |
| 🟡 Article `4` AI literacy | in force; 🔴 **wording reported CHANGED** — the duty remains, the *"sufficient level"* language is reported removed | 🟡 secondary only |

🔴 **`eur-lex.europa.eu` remains `ENOTFOUND` from this environment *(`T309`, re-confirmed)*, so
every date above is SECONDARY.** 🟢 **The planning consequence does not depend on the date, which is
why it is worth stating:** the deadline that moved is the one with a conformity route; **the one
that did not move is the one with none.** 🔵 **A client's emotion-inference pilot is not *"early for
`2027`"* — it is prohibited now.** 🟢 **And Article `27`'s fundamental-rights impact assessment for
public-body deployers is reported unchanged, which makes the `2027` relief a documentation
deferral, not a design one.**

### 🆕 🟡 Trend `3` — the demand signal has shifted from adoption to DEFENSIBILITY, and the suppliers have noticed

🔵 Across this pass's searches the same reframing appears from independent directions: a shift *away
from generic chatbots toward platforms purpose-built for education*; systems *expecting evidence
that products improve learning quality, persistence, well-being or job-relevant skills*;
institutions moving to *comprehensive AI strategies with strong oversight*.

🟢 **The supply side now shows it in SCHEMA, which is the part this KB can verify rather than
quote.** 🔵 **`dotty-tutor` at `8`★ ships `3` prompt-governance tables, `9` agent-audit tables and
`12` human-review tables** — and `ACTION MJ` measured its prompt cluster as genuinely sufficient
*(`18` columns, release lineage via `previous_revision_id`, and no `CASCADE` on the audit FKs)*.
🔴 **It also measured `teacher_review_events.corrected_assessment` — the human's override of the
machine — as `CASCADE`-deleted by its class.** 🟢 **That is the trend in one row: governance is being
built, and it is being built one `ondelete` clause short of surviving contact with a regulator.**

### 🔴 Trend `4`, restated because it got worse, not better — the `pt-BR` gap is a FEATURE gap, not a model gap

🔵 **`ACTION ML` settled a question this KB had carried as open since `Gap 372` was opened.** 🔴 **The
`pt-BR` essay-scoring path is TRAINING, not inference:** `essay-br` *(`MIT`)* labels `5` ENEM
competences at `0`–`200`; `writeAlizer` *(`MIT`)* predicts `1` holistic quality score from `1 316`
English ReaderBench features, `Language: en-US`. 🔴 **There is no mapping between them to measure.**

🔴 **And the follow-on is worse than the finding.** `Gap 424`: **ReaderBench's Portuguese support is
not established** — its README names no supported languages and `3` probed language-resource paths
`404`. 🔵 **If the Apache-2.0 extractor has no `pt` pipeline, the blocker was never the model and
never the licence: it is FEATURE EXTRACTION.** 🟢 **`ACTION MQ` is the highest-value outstanding
probe on this shelf, because it decides whether `Gap 372` closes as a training project or reopens as
a feature-engineering one.**

## Pass 185 — 2026-10-14

🆕 🟢 **The trend this pass can prove is about DISCOVERY, and it invalidates a conclusion this KB
published two passes ago.** 🔴 **p184 measured the GitHub topic channel at `79`% already-censused
and reasoned that the channel was spent.** 🟢 **It was not the channel that was spent — it was one
SORT ORDER.** One re-read of `topics/ai-tutor` with `s=updated` instead of the default
stars-descending returned [`ningkaikok/dotty-tutor`](https://github.com/ningkaikok/dotty-tutor):
`Apache-2.0`, **`55` tables, `76` foreign keys, `117` test files, updated the day before the
pass** — the richest permissive education schema this KB has measured, at **`8`★**.
🔵 **`Gap 415`. Every *"channel exhausted"* figure published before today is scoped to
stars-descending and must be re-read that way.**

### 🆕 🟢 Trend `1` — tutoring is being shipped as an agent SKILL, not as an application

🟢 **Four rows of the same new shape appeared on one topic page in one week:**
[`cliffffffffff/guided-learning`](https://github.com/cliffffffffff/guided-learning) *(`MIT`)*,
[`YUANYINGLONG-91/lecture-notes-tutor`](https://github.com/YUANYINGLONG-91/lecture-notes-tutor)
*(`MIT`)*, [`Zemmeng/claude-study-system`](https://github.com/Zemmeng/claude-study-system) *(`MIT`,
a harness with hooks and slash commands)*, and at scale
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
*(`853`★, **`165` skills**, `CC BY-SA 4.0`)*.

🔵 **What changes for a studio: there is no application to host.** The deliverable is text and
tool-definitions dropped into an agent the client already runs, which moves the engagement from
*build and operate* to *author and govern*. 🔴 **And it moves the licence question from software to
CONTENT: `CC BY-SA 4.0` carries share-alike on anything adapted and has no patent grant.**
🟢 **A `0`★ `MIT` skill can therefore be worth more to a deliverable than an `853`★ `CC BY-SA`
library — the first time on this shelf that the licence, not the schema, decides between two rows
of the same kind.**

### 🆕 🔴 Trend `2` — *"unlicensed"* on this shelf is partly an instrument artefact

🟢 **`ACTION MD` read `61` rows this KB had recorded as grant-absent. `9` carried a real grant, `6`
of them permissive.** 🔵 **The grants were in forms no file probe and no cession-text matcher can
see:** the bare word `MIT` under `## License`; *"Apache 2.0."* under `## Licence` *(British
spelling)*; `Apache-2.0` named in a body sentence with the model weights carved out; `Apache-2.0`
by **incorporation by reference** with holder and year; and a bespoke permission written in Spanish
prose.

🔴 **The inverse is just as common, and more dangerous: `4` rows carry a licence identifier that is
NOT a grant** — a README pointing at a `LICENSE` file that does not exist, a `shields.io` badge,
*"MIT — demo use only"*, and *"open source and available for educational purposes"*.
🟢 **So the direction of the error is symmetric again, as p184 found for blind verdicts: an absence
can be a probe artefact, and a presence can be a claim.** 🔵 **Neither can be resolved without
reading, and `T315` stands: published metadata carries no licence signal.**

### 🆕 🔴 Trend `3` — the licence is no longer the binding constraint on the riskiest use cases

🔵 **Two of this pass's rows are blocked by something a licence cannot fix.**
🔴 [`mskljns/ComprehensionProblems_DAiSEE`](https://github.com/mskljns/ComprehensionProblems_DAiSEE)
infers comprehension from facial affect, and **emotion inference in education institutions is
PROHIBITED by `AI Act` Article `5`(1)(f)** — in force since `2025-02-02`, with no conformity route
out. 🟡 **And the Annex III clock that governs the *permitted* high-risk uses is reported MOVED from
`2026-08-02` to `2027-12-02`** *(an amending regulation cited as Regulation (EU) 2026/1744;
Article `50`(2) marking due `2026-12-02`)*, **through secondary sources that disagree, on a primary
host this environment cannot reach.**
🟢 **The useful consequence is the same either way: the Article `5` prohibitions are already live,
so affect detection is off the table today, while the audit-and-marking work has at least `14`
months of runway.**

### 🟢 Trend `4` — the knowledge-tracing layer is DONE, and saying so is worth more than screening it again

🟢 **`20` of `20` rows rendered on `topics/knowledge-tracing` were already in this KB's census, and
`10` re-verified permissive this pass** — `pykt-team/pykt-toolkit` *(`446`★, `MIT`)*,
`bigdata-ustc/EduData` *(`312`★, `Apache-2.0`)*, `jhljx/GKT`, `jilljenn/ktm`,
`lccasagrande/Deep-Knowledge-Tracing`, `tswsxk/EduData`, `ZhijieXiong/pyedmine`,
`HFUT-LEC/EduStudio`, `THUwangcy/HawkesKT`, `jdxyw/deepKT`.
🔵 **A studio does not need to evaluate knowledge tracing; it needs to pick one and wire it.**
🔴 **The layers still missing a permissive row are the ones nobody publishes: `校務`-style
administrative automation, multi-tenant rostering, and a `pt-BR` locale on any platform row.**

### 🟢 Trend `5` — runtime-downloaded models are becoming declarable, and that is good news for air-gapped work

🟢 **[`shmercer/writeAlizer`](https://github.com/shmercer/writeAlizer) ships
`inst/metadata/artifacts.csv`: `50` runtime artefacts, each with a URL and a pinned `sha256`.**
🔵 **`Gap 414` said a model that arrives over the network is invisible to every instrument on this
shelf. For this row it is the opposite of invisible — it is a committed manifest, which is exactly
what a mirrored or air-gapped install needs.** 🔴 **One host serves all `50` *(`osf.io`, refused by
this environment)*, so the single point of failure is now measurable too.**

## Pass 184 — 2026-10-13

🆕 🔴 **The trend this pass can prove, and it is about the supply rather than the technology: `3` of
`10` open-source education repositories screened at random from GitHub's own topic pages carry NO
LICENCE AT ALL.** 🔵 **Not restrictive — absent. All rights reserved by default, which makes them
unusable for a client engagement regardless of quality.** 🟢 **And the quality is not the problem:
the richest learner model in the sample is one of the three.**

🆕 🔴 **Second measurable trend: published metadata has stopped carrying licence information.**
`5` of `10` licence predictions made from topic-page descriptions, star counts and languages were
wrong — **in both directions** *(`T315`)*. 🔵 **This is a change in what a star count is worth. A
`2026` education repository's grant is not inferable from anything GitHub renders, and the error is
noise rather than bias, so no heuristic recovers it.**

🆕 🟢 **Third, and the most useful for planning: the discoverable supply is substantially
CATALOGUED, at least for this KB.** `49` of `62` candidates across `6` topic pages were already in
the census — **`79`%**. 🔵 **The marginal value of another discovery sweep is now measurable and
low; the marginal value of READING a catalogued row is high, because the census records existence
and licence, not schema** *(`T313`)*. 🟢 **`learning-analytics` is the exception worth mining: it
returned the most new rows, and its rows are the ones carrying STANDARDS — a Learning Record Store
*(`openfun/ralph`)*, a learning record warehouse *(`OpenLRW`)*, an `LTI 1.3` integration
*(`moodle-adaptive-learning-plugin`)*. All three catalogued, none read.**

🟢 **Fourth: the education vocabulary of the supply is diverging from the education vocabulary of
the domain.** 🔵 **`ai-shifu` runs a versioned course-authoring model, per-learner progress and an
entitlement table, and calls them `shifu`, `outline_item`, `progress_record` and `course_auth` —
`0` of its `71` tables is named `course`, `lesson` or `enrollment`.** 🔴 **Meanwhile rows named for
education model chats, jobs and CRMs** *(`T310`)*. 🟢 **`T314`: the naming layer is uninformative in
both directions, so the shortlist must be built from read entity lists, not from greps.**

🆕 🔴 **Fifth: the commerce layer is moving INTO the pedagogy layer.** `29` of `ai-shifu`'s `71`
tables are billing, orders, promotions, credit wallets and referral campaigns — and **state `604`
of its learner-progress enum is `refund`.** 🔵 **An open-source tutoring platform built for direct
consumer sales encodes its business model in the learning state machine.** 🟢 **For a B2B or public
sector engagement that is a cost to find in week `1`, not week `6`.**

🟢 **Sixth, regulation into capability:** EMEA's documented position is now **two-thirds of
education systems with an AI policy framework against `29.7`% of teachers trained** and
**`21`–`25`% of schools offering training**. 🔵 **The regulatory wave of `2024`–`2026` has produced
policy faster than practice, which is a training-and-enablement market rather than a software
market.** 🔴 **The mirror in LATAM: `87`% of institutions using AI, `26`% with a strategy, `9`%
evaluating it.** 🟢 **Both are governance-and-capability engagements, entered from opposite ends.**

🟡 **Seventh: automated writing assessment is permissively licensed and still not deliverable —
and the blocker is not the licence.** 🟢 `writeAlizer` *(`MIT`, v`1.7.4`, `2026-09-16`)* scores
writing quality from feature files. 🔴 **It needs `Coh-Metrix` *(registration-gated)*, `GAMET`
*(free download)* or `ReaderBench` *(open source)* upstream, and fetches its `18` models at
runtime.** 🔵 **The open-source essay-scoring gap is a FEATURE-EXTRACTION gap. Anyone sizing the
AI Act's most explicitly high-risk education activity should price that chain, not the scorer.**

🔴 **Eighth, unchanged and worth repeating because it is a trend by persistence: GitHub Trending
has shown `0` education repositories for six consecutive passes.** 🔵 **Trending measures velocity;
this industry's useful supply is slow, small and tagged — `writeAlizer` is `3`★ with `37` tests and
`4` CI workflows.**

## Pass 183 — 2026-10-13

🆕 🔵 **Eight trends. Six are new this pass, one is carried and labelled as such, and the first is
a finding about this KB's own research method rather than about education.**
🟢 **Every trend below is labelled by the evidence it rests on: `CLONED` *(first-hand, measured in
a tree)* or `SECONDARY` *(search-index summary, never read from its own page — `T309`)*.**

### 🆕 🔴 1. A secondary channel can be months behind a fact this KB already holds — `SECONDARY`

🔵 **`ACTION LW` asked the search channel about EU Article `50` guidance. What came back, in
October `2026`, described the Annex III education deferral to `2` December `2027` as *"pending
formal adoption and publication in the Official Journal"*.** 🟢 **This KB settled that at p180:
the omnibus was ADOPTED as **Regulation (EU) `2026/1744`**, signed `8` July `2026`, OJ `24` July
`2026`, in force `27` July `2026`.** 🆕 🔵 **`T312`: a secondary source's *"pending"* is not
evidence of pending — it is evidence of when the page was written.**

🔴 **The trend, and it is about research practice rather than about education: law-firm and
tracker commentary is the fastest channel to FIND a regulatory fact and an unreliable one for its
STATUS.** 🟢 **A studio that re-researches a date it already holds will often make its own record
worse.** 🔵 **Consequence for this file: the regulatory calendar in
[`intel/market.md`](market.md) is unchanged this pass, and the pass's contribution to it is
CORROBORATION plus three procedural facts, not a correction.**

### 🆕 🔴 2. *"Educational platform"* now often means a chat app with education in the directory names — `CLONED`

🔵 **Three independent instances now, all measured in trees rather than inferred:**

| row | what it is called | what its SCHEMA models |
|---|---|---|
| 🔴 [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | *"AI-powered educational platform"* | 🔴 `chats`, `files`, `knowledge_bases`, `feedbacks`, `users` — **`10` tables, `0` courses**. `learning/courses/` is a `30`-byte docstring and `MIGRATION.md` names the mechanism: a renamed OpenWebUI |
| 🔴 [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | *"AI tutor powered by Theory-of-Mind reasoning"*, `~903`★ | 🔴 **`users`, `customers`, `products`, `prices`, `subscriptions`** — a Stripe schema |
| 🔴 `plataforma-agentes-ia` *(p182)* | *"educational agent platform"* | 🔴 a CRM |

🆕 🔵 **The trend has a cause worth naming: a chat interface plus a vector store is a weekend, and
a course/enrollment/assessment model is a quarter.** 🟢 **So the market fills with the former
wearing the latter's vocabulary.** 🔵 **`T310`, promoted this pass from observation to structural
claim: the published layer and the deciding layer are disjoint, and the ENTITY LIST is the one
layer that cannot be renamed into existence.** 🟢 **Screening rule: count tables before reading
prose.**

### 🆕 🔴 3. An aggregator can tell you what a repo DOES and never what you may DO with it — `CLONED`

🔵 **`ACTION LR` finished at `n=7`: `4` blind verdicts overturned by reading, and `4` of `4`
overturns were on the LICENCE. Grade predictions went `3`/`3` this pass.** 🆕 🔵 **`T311`: the
published layer predicts capability, not grant.** 🔴 **The clearest case is the `900`★ row whose
aggregator listings print a star count, a last-push date and a shields licence BADGE, while the
payload is `GPL-3.0` at `35 149` B.** 🟢 **Trend for anyone building a shelf: star-count
directories are getting better at discovery and are no evidence at all about licensing.**

### 🆕 🟡 4. Open core is arriving in education OSS, and it is invisible from a clone — `CLONED` + `SECONDARY`

🔵 **Two of this KB's platform rows now declare a proprietary edition of the same codebase:**
`open-tutor-ai-CE` *(README: *"the foundation for a proprietary Enterprise Edition"*, offering
theming, SLA, LTS *"and more"*)* and `openeducat_erp` *(free self-hosted Community Edition against
paid Enterprise staff seats)*. 🟢 **Neither GATES anything measurable — `ACTION LT` found `0`
licence-key, entitlement or feature-flag hits across `4 702` files.** 🔴 **The exposure is
governance, not code: the holder's incentive is the other edition, and the next release is their
decision.** 🆕 🔵 **And the channel problem is the real trend: an open-core edition cannot be seen
in a clone, so the one axis that matters here is the one axis `git clone` cannot measure.**

### 🆕 🔴 5. The licence on the code is not the licence on the corpus — `CLONED`

🔵 **`Priyamakeshwari/TeachGPT` is cleanly `MIT` *(`1 057` B, full text)* and ships
`db/chroma.sqlite3` with its HNSW index binaries, built from a commercial textbook committed at
`documents/Machine - Learning - Tom Mitchell.pdf`.** 🔴 **A vector index is a derivative of its
corpus, and `MIT` grants nothing over a publisher's book.** 🟢 **Trend: as RAG becomes the default
education architecture, prebuilt indexes ship inside repositories, and the second grant is never
in `LICENSE`.** 🔵 **Check for a committed index, corpus or checkpoint before quoting a licence.**

### 🆕 🔴 6. *"Agentic AI in education"* has stopped being a measurable category — `SECONDARY`

🔴 **One house prices agentic AI in education and learning technologies at `$2.1` B for `2026` at a
`4.5`% CAGR, while the broader category is quoted at `30`%+ by several.** 🔵 **A `4.5`% CAGR
describes a mature niche; a `30`% CAGR describes a land grab. The gap is definitional, not
empirical.** 🟢 **Trend with a defence: ask which definition a number priced; if the source cannot
say, discard it.** 🔴 **The `2026` market-size band across four houses is now `$9.58` B–`$11.4` B,
and the `2025` band `$6.4` B–`$8.3` B — the houses disagree about the DIRECTION of the step into
the current year *(`T306`)*.**

### 🟢 7. In LATAM the students have adopted and the institutions have not integrated — `SECONDARY`, carried

🔵 **Carried from earlier passes, not new this pass, and repeated because it is the single most
useful framing this KB has for a LATAM engagement.** 🟢 **`92`% of LATAM students use an AI tool
regularly; `30`% of students and faculty think their university integrates AI effectively**
*(Digital Education Council with Tecnológico de Monterrey)*. 🔵 **With `87`% of `200` institutions across `19` countries using AI somewhere and
`26`% holding a formal framework** *(UNESCO IESALC)*, **and the new application breakdown:
teaching and learning `73.5`%, research `57.0`%, administration `34.1`%, extension `20.0`%.**
🟢 **Trend: the LATAM engagement is institutional, not persuasive — governance, frameworks and
integration, not adoption.** 🔵 **The regional institutional layer is forming to match: the UNESCO–CEPAL
LATAM-and-Caribbean AI-in-education Observatory, April `2026`** *(carried)*. 🆕 🟡 **New this
pass, as scale rather than detail: `716` AI regulatory instruments across `23` countries and
territories** *(Universidad de los Andes)* — **`0` of them education-specific.**
🔴 **Supply is still `0` rows, by measurement.**

### 🆕 🟢 8. The audit record is becoming the differentiator, and it is portable — `CLONED`

🔵 **North American human-oversight expectations and EU Annex III documentation requirements want
the same artefact: a durable record of what an agent did, under which rule, that cannot be quietly
edited.** 🟢 **`ACTION LV` ported one from
[`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) *(`MIT`)* and it runs: `18` checks
green on stdlib `sqlite3`** — see
[`compose/code/agent-tool-receipts-port/`](../compose/code/agent-tool-receipts-port/README.md).
🆕 🔴 **And the port found two things reading could not.** 🔴 **SQLite's `foreign_keys` pragma is
OFF by default, so a correct `ON DELETE RESTRICT` schema audits NOTHING until a connection opts
in — the orphan is reproducible.** 🔴 **And the asymmetry: the policy side is `RESTRICT` while the
receipt side is `CASCADE`, so deleting a parent run deletes the evidence that an agent applied the
rule.** 🟢 **Trend and the lesson under it: *"we have audit tables"* is a claim about a schema;
*"the record survives a delete"* is a claim about a deployment, and only the second one is worth
anything to a regulator.**

## Pass 182 — 2026-10-13

🆕 🟢 **p181 found that engagement-readiness runs OPPOSITE to ★. p182 adds the layer underneath
it, and it is more useful: the things that make a repository engagement-ready are the things
nobody puts in a README, so they cannot be found by searching — only by reading.**

### 🟢 The trend, stated as a measurement

🔵 **`6` trees read this pass. For each, the capability that decides whether a studio can build on
it, and whether that capability was discoverable without cloning.**

| row | the deciding capability | visible without reading the tree? |
|---|---|---|
| 🟢 [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | tenancy ENFORCED fail-closed at a typed boundary | 🔴 **No.** The schema showed a `tenant_id` column; enforcement lives in `models/principal.go` and `auth/middleware.go` |
| 🟢 [`civil-ai`](https://github.com/zhangl1001/civil-ai) | audit tables actually WRITTEN, with a state machine | 🔴 **No.** The table NAMES were visible; the `INSERT` sites were not |
| 🟢 [`feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) | no external IdP required | 🔴 **No — and the visible signal pointed the WRONG WAY.** `keycloak` appears in `12` files; it is a default registration name and a demo compose file |
| 🟡 [`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🔴 no course/lesson/enrollment/assessment entity | 🔴 **No.** It is called an educational platform |
| 🔴 [`plataforma-agentes-ia`](https://github.com/henriquemathias/plataforma-agentes-ia) | 🔴 it is a CRM | 🔴 **No.** Described as an educational agent platform, and it scores `157` on an education-vocabulary probe |
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 🔴 `AGPL-3.0` | 🔴 **No — a `2026` roundup published it as `MIT`** |

🔴 **`6` of `6`.** 🔵 **Not one deciding capability was visible from the manifest, the README, the
description or a published roundup. In three of the six the visible signal actively misled.**

### 🆕 🔴 `T310` — the published layer and the deciding layer are disjoint

🟢 **This is the generalisation p181's `T290` was reaching for.** ★ counts, READMEs, descriptions
and roundups describe what a repository is FOR. 🔵 **Whether a studio can build on it is decided
by tenancy enforcement, identity ownership, audit write paths, standards support and the licence
PAYLOAD — none of which is marketing, so none of which is published.**

🟢 **The operational consequence, and it is a cost a studio can quote:** a triage from published
metadata has, on this pass's evidence, a **`3`-in-`4` overturn rate** *(`ACTION LR`, `n=4`)*.
🔵 **Budget one clone-and-read per candidate. On these trees that cost seconds, not hours — the
expensive thing is believing the metadata.**

### 🟢 The four lexical traps, now a named set

🔵 **Each one is a word that scores high on a probe and means something else. They have cost this
KB a retraction each.**

| word | looks like | actually was | pass |
|---|---|---|---|
| 🔴 `session` | an auth session | **STUDY** sessions *(`57` files)* | p180, `T288` |
| 🔴 `xapi` | a standards integration | **an HTML comment in Polish** on a README | p181, `T302` |
| 🆕 🔴 `enrollment` | a learner enrolment | **`AgentDynamicFollowupEnrollment`** — a marketing contact entering a follow-up sequence *(`157` hits)* | p182, `T308` |
| 🆕 🔴 `keycloak` | a hard IdP dependency | **a default SAML registration NAME** plus a demo compose file | p182, `ACTION LQ` |

🆕 🔵 **The newest two are the instructive pair, because they fail in OPPOSITE directions.**
`enrollment` invented a capability that was not there; `keycloak` invented a REQUIREMENT that was
not there. 🟢 **A probe that only looks for missing features will catch the first kind and never
the second — and the second is the one that loses a deal, because it adds a procurement to an
estimate for no reason.**

### 🟢 What is reliably absent, and therefore reliably billable

🔵 **Carried from p181 and extended with this pass's rows.**

| layer | absent in | what a studio supplies |
|---|---|---|
| 🔴 **identity a cohort can use** | `DeepTutor` *(JSON file)*, `Bloom`, `Study-Mate`, `examprep`, `tutoria` | the whole identity layer, or an `LTI` launch that borrows the institution's |
| 🔴 **course / enrollment / assessment entities** | 🆕 `open-tutor-ai-CE` *(`0` of each, despite the name)*, `DeepTutor` | the domain model itself — this is bigger than it sounds |
| 🔴 **tenancy** | every shelf row except `tutor-mcp` and `mentingo` | a tenant key, scoping discipline and the tests that assert refusal |
| 🔴 **audit / policy versioning** | every shelf row except `civil-ai` and `tutor-mcp` | the thing North American districts and EU Annex III both ask for |
| 🔴 **`es` / `pt-BR` localisation** | 🆕 **EVERY shelf row, measured** | a quotable line item on every LATAM engagement *(`ACTION LP`)* |
| 🔴 **a permissive SIS** | the whole ecosystem | integrate with the incumbent, deploy copyleft, or build |

### 🆕 🔴 `T309` — and a trend about this KB's own evidence

🔴 **The fetch channel resolves GitHub-family hosts only** *(`7` non-GitHub hosts tried, `7`
`ENOTFOUND`, GitHub control passing — see [`repos/foundations.md`](../repos/foundations.md))*.

🔵 **So this KB has two grades of evidence and should stop mixing them:**

| grade | what it covers | how strong |
|---|---|---|
| 🟢 **MEASURED** | anything in a cloned tree: licences, schemas, enforcement, entities, locales | 🟢 **Primary. Reproducible — p181 reproduced p180's `Bloom` and `OpenOLAT` figures exactly from independent clones** |
| 🟡 **SEARCH-INDEX SECONDARY** | every market figure, regulatory date, adoption percentage and named player | 🟡 **Never read from its own page. Trustworthy when several unrelated publishers agree, and labelled when they do not** |

🟢 **The honest line for a client deck: this KB's repository claims are measurements and its
market claims are a reconciled reading of the public record. 🔵 Those are different promises, and
conflating them is how a `19`%-wide market band gets quoted as a number.**


## Pass 181 — 2026-10-13

🆕 🟢 **`T290` — ★ rank and engagement-readiness are uncorrelated — was p180's best guess from `3`
rows. Tested on `14` this pass, it HOLDS, and it is now a screening rule with a measured cost.**

| ★ band | rows | own persistence | identity a cohort can use |
|---|---|---|---|
| 🔴 **`≥ 500`★** | `3` | 🔴 `1` of `3` *(users in a JSON file)* | 🔴 **`0` of `3`** |
| 🟢 **`< 500`★** | `11` | 🟢 `8` of `11` | 🟢 **`7` of `11`** |

🔵 **The sharpest single comparison: [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) at
`41 000`★ has no `users` table; [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp)
at `44`★ has tenants, cohorts, billing events and an audit trail. `932`× the stars, and it is the
one that cannot hold a class.**

### 🟢 The trend, stated as the mechanism rather than the correlation

🟢 **Stars measure how easy something is to TRY. Education engagements are bought on whether a
COHORT can be enrolled, graded and audited.** 🔵 **Those requirements pull in opposite directions:
an identity layer, a tenant key and an audit table are exactly the things that make a repository
harder to run in five minutes — so the rows that optimise for a fast first impression systematically
shed them.**

🆕 🟢 **The corollary a studio should hear: the identity layer is the most reliably ABSENT thing in
permissive edtech, which makes it the most reliably BILLABLE.** `5` of the `14` rows measured this
pass have no usable identity at all; `1` keeps users in a JSON file; `1` delegates to an external
`BaaS`; `1` borrows an agent runtime's credential.

### 🆕 🟡 Four identity shapes, and what each one costs to fix

🔵 **p180 published a three-valued axis *(OWN / BORROWED / NONE)*. `14` rows needed five values, and
the two new ones are the ones that fool a probe.**

| shape | rows | what a studio must supply |
|---|---|---|
| 🟢 **OWN, in the schema** | `OpenOLAT`, `Artemis`, `OpenTutor`, `mentingo`, `tutor-mcp`, `feedbacksystem`, `lumen`, `LTLTutor` | 🟢 **Nothing. Configure it** *(and for `tutor-mcp` and `mentingo`, the tenant key is already there)* |
| 🆕 🟡 **OWN, but FILE-BACKED** | `DeepTutor` *(`USERS_FILE` JSON, roles assigned by insertion order, env bootstrap admin)* | 🟡 **A migration, not a build.** The concepts exist; they are not in the database, so they do not join, index or audit |
| 🆕 🟡 **DELEGATED to a service** | `DeepTutor` *(optional PocketBase proxy)*, `feedbacksystem` *(`Keycloak`, `auth0`)* | 🟡 **An identity provider the client must own and operate** — often the right answer at an institution that already runs one |
| 🟡 **BORROWED from the host** | `anki-mcp-server` *(all `21` `auth` files are `MCP` CLIENT credentials)* | 🟡 Whatever the agent runtime has. It authenticates clients, not learners |
| 🔴 **NONE** | `Bloom`, `Study-Mate`, `universal-examprep-skill`, `fsrs4anki`, `education-agent-skills`, `gen-mentor`, `InterviewMentor`, `ai-tutor-app`, `Tutorbot-Spock` | 🔴 **The whole identity layer — or an `LTI` launch that borrows the institution's** |

🆕 🟡 **One row needed a sixth description and got a footnote instead:
[`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai) owns its identity under a different
noun — `candidate_profiles`, not `users`.** 🔵 **`T309`: the identity probe is a VOCABULARY, and a
vocabulary mis-grades a row that models the same concept with a domain word. Assessment systems say
*candidate*; LMSes say *user*; MOOCs say *learner*.**

### 🔴 The trend this pass tried to find and did NOT

🔴 **A language barrier in the probe.** The hypothesis was that an English-only entity vocabulary
hides identity in non-English repositories — a plausible trend for a global studio. 🔴 **It is
false here.** `用户` appears in `82` files of `DeepTutor`, `benutzer` in `13` of `feedbacksystem`,
`utilisateur` in `10` of `tutor-mcp`, `usuario` in `5` of `mentingo` — 🔴 **and every one is an i18n
message catalogue, a design document or a student fixture.** 🟢 **Every real entity declaration in
all `14` rows is in English.** 🔵 **Recorded as refuted so it is not re-proposed, and because the
refutation is itself a finding: this supply writes its product in English and its UI in everything
else.**

### 🆕 🔴 The trend that should worry a studio: standards and permissiveness are nearly disjoint

🔴 **Of `6` permissive ROUTE rows, exactly `2` speak `LTI 1.3` — and both are Java.** `tutor-mcp`
*(Go)*, `mentingo` *(TypeScript)*, `OpenTutor` *(Python)*, `feedbacksystem` *(Kotlin)* and
`civil-ai` *(Python)* cannot receive an `LTI` launch. 🔵 **`T305`: outside Java, choosing a
permissive education route means the interoperability layer is the engagement's first BUILD. It is
also the most portable thing a studio could carry between education clients — which makes it an
investment, not a cost.**

🟢 **The one standards bridge that does exist permissively is `SCORM`, and `mentingo` holds both
ends:** a generator and a browser runtime it wrote itself, plus an importer with real
`imsmanifest.xml` fixtures. 🟢 **Content can therefore move between a permissive deployment and a
copyleft incumbent without touching the incumbent's code.**

### 🟢 Integrity detection now has a RULE, not just a threshold

🟢 **p179 gave this KB a number: `0.85`, with honest sibling code topping out at `0.6720` and an
empty band of `0.3066` above it.** 🆕 🟢 **p181 adds the condition that number depends on
(`ACTION LB`, `7` rungs, template-to-submission ratio `0.0033`–`1.6842`):**

- 🔴 **A boilerplate header buys nothing.** At ratio `≤0.04`, median `|Δsim|` is `0.00064` —
  template exclusion is cargo cult at the scale most teams use it.
- 🟢 **A real handout helps, and the effect peaks mid-range.** At ratio `0.14`, the honest-work
  ceiling falls from `0.6720` to `0.6004` and the positive/negative separation WIDENS to `0.3766`.
- 🔴 **An over-broad template HURTS.** At ratio `1.68` the known positive erodes from `0.9898` to
  `0.8912` and the separation drops to `0.2897`, **below** the no-template baseline of `0.3178`.

🔵 **`T310`: template exclusion is not a hygiene step to always-enable or always-skip. It has an
optimum, it is on the order of one handout module, and past the submission's own size it eats the
signal it was meant to clean.**

## Pass 180 — 2026-10-13

🆕 🔴 **`T286` — *"the permissive education supply is not short of intelligence, it is short of
IDENTITY"* — was this file's headline one pass ago. It is RETRACTED, on evidence from this KB's own
shelf.** 🔵 **The trend is real but it is narrower and more useful than the claim that was made of
it.**

### 🟢 The axis, repaired: whose identity?

| | own identity | borrowed identity | no identity |
|---|---|---|---|
| **adjudicates** | 🟢 `Artemis` *(`528` write endpoints, `passkey` `136` files, `LTI 1.3` grade passback)*; 🆕 🟢 `OpenOLAT` *(`440` entities, `Shibboleth` `147` files, `QTI` `1 201`)* | *(no row)* | *(no row — and the cell is probably incoherent: adjudicating without an identity has no subject)* |
| **does not adjudicate** | 🆕 🟢 `OpenTutor` *(`34` tables, `users` + `auth_sessions`, `jose` refresh tokens, `141` endpoints)* | 🆕 🟡 `anki-mcp-server` *(`auth` `21` files, every one an `MCP` CLIENT credential)* | 🟡 `Bloom` *(`7` tables, `0` auth)*; 🔴 `Study-Mate` *(`0` DBs, `0` servers)*; 🆕 🔴 `universal-examprep-skill` *(`auth` `0`)* |

🔵 **`T287`: a claim about THE SUPPLY cannot be built from the two rows one pass happened to open.**
🟢 **`3` of `8` read rows have no identity, `1` borrows, `4` own one. *"Short of identity"* is a
property of the COMPONENT tier, not of the supply.**

🆕 🟢 **And the sharper trend underneath the retraction — this is the line worth carrying forward:**
🔴 **★ rank and engagement-readiness are UNCORRELATED in this supply.** `Study-Mate` reached `925`★
in `26` days with `0` databases, `0` servers and `0` auth; `OpenTutor` sat at `140`★ with `34`
tables, its own `JWT` auth and dated migrations. 🔵 **`T290`: in permissive edtech, popularity
measures how easy a thing is to TRY, and engagement-readiness measures whether a cohort can log
into it. Those are close to opposite properties.**

### 🆕 🔴 The trend this file must apply to itself: the count that looked like a finding

🟢 **`universal-examprep-skill` matches `session` in `57` files. Not one is an auth session — they
are STUDY sessions.** 🟢 **`anki-mcp-server` matches `auth` in `21` files. Not one is a learner —
they are `MCP` client credentials (`CLIENT_ID`, `authClientId`).**

🔵 **`T288`: a word-bounded count is a POINTER TO A READ, never a substitute for one.** 🔴 **This
matters beyond hygiene, because the probe shape that produced those two near-misses is the probe
shape that produced `T286`.** 🟢 **The cure is the one p179 already named and this pass actually
applied: open the file and read the import sites.**

### 🟢 The regulatory trend reverses the headline

🆕 🟢 **Regulation (EU) `2026/1744` was adopted on `8` July `2026` and has been in force since
`27` July.** 🔴 **Annex III high-risk duties — the ones that reach admissions, learning-outcome
evaluation and exam monitoring — moved from `2` August `2026` to `2` December `2027`.** 🟢 **Article
`50` transparency duties did NOT move and have applied since `2` August `2026`.**

🔵 **`T295`: *"the AI Act was delayed"* is false as said to an education client.** 🟢 **The duty
that binds a content-generating tutor today is live; the duty that binds an assessment engine is
`14` months out.** 🔴 **Any roadmap that treats the deferral as general cover for provenance work
is wrong on the live obligation.**

🟡 **Unresolved and recorded as such:** whether the adopted text retained the Commission's
*"conditional on harmonised standards"* framing. 🔴 **Not settleable here — `eur-lex.europa.eu` is
`403` on `curl` and `ENOTFOUND` on the second channel; `gap 110` now holds on three channels.**

### 🟢 The platform trend: permissive and full-sized are not opposites

🆕 🟢 **`OpenOLAT` is `Apache-2.0`, `2 624 333` lines of Java, `440` `@Entity` classes, `497`
DAO/Manager classes, its own federated auth and four education standards.** 🔵 **`T293`: this KB
spent `20` passes treating *permissive* and *full platform* as a trade-off because the three
largest LMSes it knew were `AGPL`, `AGPL` and `GPL`. The trade-off was a sampling artefact of which
platforms are famous.**

🟡 **The counter-trend, stated so the recommendation stays honest:** 🟡 **`OpenOLAT` already carries
`openai` in `33` files and `ollama` in `13`.** 🔵 **Upstream is building its own AI layer. A studio
that forks rather than contributes will be maintaining a parallel integration against a moving
target — which is an argument for plugin-shaped work even where the licence permits a fork.**

### 🟢 Adoption has outrun governance everywhere, and each region shows it differently

| region | the gap, measured |
|---|---|
| North America | 🟢 **`134` bills in `31` states** in one session — governance arriving as a patchwork, with reversals *(NYC's K-8 moratorium)* alongside mandates *(Ohio)* |
| EMEA | 🟡 ~`10%` of `450`+ institutions have formal AI guidelines, under the world's most detailed AI statute |
| APAC | 🟡 Korea and Vietnam bind education explicitly; Japan and India stay light-touch; AU/NZ public opinion favours BANS more than Asian markets do |
| LATAM | 🟢 **`87%` of `200` institutions use AI; `26%` have a strategy** — the cleanest statement of the gap in this KB |
| MEA | 🟢 UAE MANDATES a K-12 AI curriculum for ~`1` M pupils — 🔵 **curriculum ahead of regulation, the inverse of the EU** |

🟢 **`T296`: the one product that sells into all five regions is the EVIDENCE LAYER — provenance,
audit trail, human-in-the-loop record, per-jurisdiction policy configuration — because every region
is converging on demanding it and none of them is converging on the same model, vendor or
pedagogy.**

### 🔴 Trends this pass could not test

- 🔴 **`ACTION LB` — `dolos`'s `-i` effect as a function of template-to-submission ratio — NOT
  ATTEMPTED.** 🔵 Stated plainly rather than deferred silently: the pass spent its execution budget
  on the Python channel and its read budget on `OpenOLAT`. Carried to p181.
- 🔴 **No row was BUILT or RUN this pass.** 🟢 Dependencies now install *(`ACTION LC`)*, but
  executing a subject repository's own suite was refused by the harness's external-code policy.
  🔵 **`T297`: *"installable"* and *"runnable"* are now separately gated here, by a network limit
  and a policy limit respectively. A KB that conflates them will mis-predict its own capacity for a
  third consecutive pass.**

## Pass 179 — 2026-10-13

🆕 🟢 **p177 introduced the axis *does the system ADJUDICATE?* and p178 put a row on both sides.
p179 adds the axis that turns out to matter more for what a client can BUY: does the system have a
USER?**

| | adjudicates | does not adjudicate |
|---|---|---|
| **has a user** | 🟢 `Artemis` — `257` entities, `528` write endpoints, `passkey` in `136` files, `saml2` in `54`, `LTI 1.3` with grade passback | *(no row yet)* |
| 🆕 **has NO user** | *(no row — and this cell may be empty for a reason: adjudicating without an identity is incoherent)* | 🟡 `Bloom` — `7` tables, `16` write endpoints, `0` auth files; 🔴 `Study-Mate` — `0` databases, `0` servers, `0` auth |

🔵 **`T286`: the permissive education supply is not short of INTELLIGENCE, it is short of IDENTITY.**
🟢 **Both of the largest new rows this pass read can plan a lesson, sequence a syllabus and adapt
to a learner. Neither can tell one learner from another.** 🔴 **And an education client's first
question is always about the second thing: whose record is this, who may see it, who signed off
on the grade.**

### 🆕 🔴 The trend this pass would most like to un-see: the manifest as a competence claim

`Bloom` declares `python-jose[cryptography]`, `bcrypt`, `email-validator` and `python-multipart`
in `pyproject.toml`. 🔴 **Import sites, measured: `0`, `0`, `0`, `0`.** 🔵 **`T285`: a declared
dependency is not an implemented capability.** 🟡 **This is worth a trend line rather than a
footnote, because the fast way to triage a shelf of candidates is to read manifests — and a
manifest is the cheapest place in a repository to look finished.** 🟢 **The cure is the one this
KB already practises: read the code, count the call sites, publish the count.**

### 🟢 Agentic education is arriving as PORTABILITY, not as agents

🆕 🟢 **`Study-Mate` is the clearest signal in this KB of where the supply side is actually
spending its effort: `199` files of TypeScript and ESM whose only job is to run one skill set
inside FOUR runtimes owned by other vendors — DeepSeek Harness, Google Antigravity, OpenAI Codex
and ChatGPT Work.** 🔵 **The author's bet is not on an agent. It is on the host market staying
fragmented.** 🟡 **For a studio that bet is directly useful: if the adapter layer is where the
work is, then the durable asset in an engagement is the skill content plus the adapter, and the
host is a swappable dependency.**

### 🟢 Regulation stopped being a forecast this year

🟢 **Four education-AI obligations are in force in `2026`, on four dates:** Korea's `AI` Basic Act
(Jan), Vietnam's Law `134/2025/QH15` (`1` Mar), Ohio's district-policy mandate (`1` Jul), and EU
`AI` Act enforcement (`2` Aug). 🔵 **The trend is that the EU is no longer the pacesetter for
education `AI` — two APAC statutes landed first, and one US state moved before the EU's
machinery started.** 🟡 **The EU's Annex III education date (`2` December `2027`) remains a
SECONDARY figure in this KB by declaration (`ACTION KV`), and the November `2025` *"digital
omnibus"* may convert it from a date into a dependency on harmonised standards.**

🔴 **And the trend that cuts the other way:** New York City imposed a one-year moratorium on
student-facing `AI` through eighth grade. 🔵 **Student-facing K-8 is now a regulatory liability in
the largest US district while teacher-facing deployment is being publicly funded in the UK
(£`4` M for lesson planning and marking). The market is converging on the TEACHER as the user,
from two unrelated directions.**

### 🟢 Academic integrity stops being a position and becomes a number

🟢 **Measured this pass on real code (`ACTION KW`): identifier renaming scores `1.0000` against
`dolos` — it is completely ineffective — and rename-plus-reorder scores `0.9898`.**
🔴 **Honest sibling code that merely shares a framework, an ORM and a test style scores up to
`0.6720`.**

🔵 **So the integrity conversation has a shape it never had before: a `0.7` threshold sits
`0.028` above the honest-work band, and the empty band between `0.6720` and `0.9786` is where the
threshold belongs — near `0.85`.** 🟢 **That is a sentence a university committee can adopt, and
it is derived rather than asserted.**

### 🟡 The adoption/governance gap is the actual product, and it is measured in two regions

- 🟢 **LATAM: `87`% of `200` higher-education institutions use `AI` in at least one area; `26`%
  have a formal strategy** (UNESCO IESALC / UNU-IAS). `79`% of faculty use `AI` in teaching while
  `88`% engage only minimally to moderately (Digital Education Council `2026`).
- 🟡 **Europe and North America: ~`70`% of institutions have or are developing `AI` guidance**
  *(single vendor-style source)*.
- 🔵 **Read together, the trend is not "adoption is coming" — adoption has happened, ungoverned.
  1EdTech's own watch-list says institutions are now building governance structures and
  evaluation processes rather than picking tools.** 🟢 **The billable work for the next two years
  is retrofitting governance onto use that already exists.**

### 🔴 What this file still cannot say

- 🔴 **Nothing here is measured on a regional SUPPLY channel.** Four regional searches returned
  policy and market material and named `0` region-originated open-source education repositories.
  🔵 **Regional supply remains visible only through the tag census.**
- 🔴 **The market size is a range spanning a factor of two for the same year** (`$6`–`$12.3` B for
  `2026` across sources), all vendor-sourced. No point estimate should be quoted.
- 🔴 **The *"has a user"* axis is populated from `3` rows.** It is a sharp axis on thin evidence,
  and `ACTION LD` (read the `3` remaining `170`★+ rows) is what would widen it.


## Pass 178 — 2026-10-13

🆕 🟢 **The axis this file introduced at p177 — does the system ADJUDICATE? — now has a row on both
sides, read from code, and it is the most useful distinction this KB holds for an education
engagement.**

| | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) *(p177)* | [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) *(p178)* |
|---|---|---|
| what it returns | 🟢 **similarity and clusters. `falsePositive` `0`, `confidence` `0`, no pass/fail in `513` files** | 🔴 **grades. `AutomaticAssessment` in `14` files, `score` `581`, `feedback` `720`** |
| EU classification | 🟢 **decision support — outside Annex III on its own behaviour** | 🔴 **Annex III stand-alone high-risk: automated grading and exam scoring are named** |
| US oversight statutes *(MD, OK, VA)* | 🟢 **satisfies human-oversight requirements BY CONSTRUCTION** | 🟡 **satisfiable, but the human-review workflow is something you BUILD** |
| Article `5` emotion-recognition ban | 🟢 **not applicable** | 🟢 **CLEARS IT ARCHITECTURALLY: `proctor` `0`, `webcam` `0`, `emotion` `0`; `ExamSession` anomaly detection instead** |
| conformity work in an engagement | 🟢 **none attaches to the tool** | 🔴 **real, and it lands on the `2` December `2027` roadmap, not this quarter** |

🔵 **`T277` generalises into a design rule a studio can apply to any product a client brings:
*architecture decides regulatory class, and it decides it before a single policy document is
written.* A tool that ranks and refuses to conclude is cheap to deploy and cheap to defend. The
same capability, wired to emit a verdict, becomes a high-risk system with an audit trail, a
conformity assessment and a human-review obligation.** 🟢 **Both options are now routable from this
KB with their costs attached, which is the difference between advice and a catalogue.**

### 🆕 🟢 `ACTION KV` — the AI Act is a SEQUENCE, and the dates are now permanently secondary

🔴 **The method finding first, because it changes how this file should be read: `6` of `6` EU
primary and official hosts are unreachable from this environment, on TWO independent channels.**
`eur-lex.europa.eu`, `eurlex.europa.eu`, `digital-strategy.ec.europa.eu`, `ec.europa.eu`,
`data.europa.eu` and `artificialintelligenceact.eu` all fail to resolve from the shell, and the
fetch tool returns `ENOTFOUND` for the same host it was pointed at.
🟢 **LIMB `2` of `ACTION KV` FIRES: no reachable primary or official source exists. The figure is
hereby declared PERMANENTLY SECONDARY, and `gap 110` stops being re-derived every pass.**
🔵 **What that licenses, and what it forbids: this KB may SEQUENCE the duties, because the sequence
is agreed across every independent channel it reaches; it may NOT publish a single day as
authoritative, and no deck should put a delivery date on one.**

| duty | applies from *(secondary, corroborated)* | what you build, in this engagement |
|---|---|---|
| 🔴 **Article `50` transparency** | **`2` August `2026`** — in force | disclosure in the tutoring and authoring surfaces |
| 🔴 **Article `50(2)` marking of synthetic content** | **`2` December `2026`** — 🔴 **`50` days** | 🆕 🟢 **the patch is MEASURED and GREEN — `53`/`53` at p178, in [`compose/patterns.md`](../compose/patterns.md)** |
| 🟡 **Annex III stand-alone high-risk** *(access, progression, assessment, exam scoring — where education sits)* | 🟡 **`2` December `2027`** *(Digital Omnibus, reported as `+16` months)* | conformity-assessment roadmap, not code |
| 🟡 **Annex I embedded** | 🟡 **`2` August `2028`** | out of scope for most education work |
| 🔴 **Article `5` — emotion recognition of students and staff** | 🔴 **PROHIBITED, present tense** | 🆕 🟢 **an ARCHITECTURAL check, and `Artemis` passes it: `emotion` `0`, `webcam` `0`, `face` `2`** |

🔴 **The conflict that remains UNRESOLVED and is now closed to further work: `50(2)` is reported as
both `2` December `2026` and `2` February `2027`, and the Omnibus as both in force since July `2026`
and awaiting adoption.** 🔵 **A client told *"education is high-risk, act now"* is being told
something TRUE about classification and wrong about timing by roughly `14` months. Mark now;
assess by `2027`. That sentence is this file's single most load-bearing output.**

### 🆕 🔴 `T279` — a census measures its query, and this one was measuring the smaller tag

🔴 **`topic:ai-education license:mit` = `135`, five consecutive passes, head unchanged — and
`topic:ai-tutor license:mit` = `298`, with five `MIT` repositories above `170`★ that this KB had
never named, none of them carrying `ai-education`.**
🔵 **The trend statement that has to be retracted: *"the supply is stable."* The correct statement
is *"the `ai-education` tag is stable at `135`, the `ai-tutor` tag stands at `298`, and the two
share exactly ONE row in their heads."* 🔴 **This KB does not know the size of their UNION and
should not imply one: nothing here has de-duplicated the two populations (`ACTION KX` territory).****
🟢 **The trend that SURVIVES, and strengthens: `0` of the `6` new rows is held by an institution.**
🔵 **Two instruments, five passes apart, agreeing that the permissive supply is individually held is
a much stronger claim than either made alone.**

### 🆕 🔴 `T280` — a fix that lives in a library is not a fix until something makes its absence fail

🔵 **p177 spent its sharpest action, `ACTION KS`, deriving from outputs a defect that this
repository had already diagnosed, measured and repaired on `2026-10-09`.**
`compose/code/lib/payload_measure.sh` names it `P834`, tabulates it *(trailing newlines `0`/`1`/`3`
→ delta `0`/`1`/`3`)*, ships `size_of_file` as the correct primitive, and preserves the broken form
as `size_of_capture_BROKEN` with *"NEVER use this to publish a figure"* written above it.
🔴 **`12` live call sites, in `12` files across `10` instruments, still use the broken idiom.**
🟢 **The industry-facing version of this thesis, which is why it belongs in a trends file and not
just in a changelog: every client with a platform team has a `payload_measure.sh` — a correct
primitive nobody adopted. The diligence question is not *"do you have a standard?"* but *"what fails
when someone ignores it?"*** 🔵 **The answer this pass shipped is a gate that exits `1`.
[`compose/code/p178-byte-channel-census/`](../compose/code/p178-byte-channel-census/)**

### 🆕 🔴 `T281` — a `HEAD` is not an identity on a repository with two live branches

🔵 **`Artemis`'s default branch is `develop`; `main` exists as a DIFFERENT commit
(`07f43f8e0b71`); `develop` was `8c158741c38e` when this pass cloned it and `6aae3ae2655c` an hour
later.** 🟢 **The licence is byte- and `md5`-identical on both, so licence claims are
branch-independent — but no file count, token count or test count is.**
🔴 **p177 recorded `09266581a02c` for this row with no branch label, and a `--depth 1` clone cannot
reach it to say which branch it was on.** 🔵 **For a client this is the same discipline that makes a
lockfile matter: on a repository with `396` forks and `256` open issues, *"we read HEAD"* is not
reproducible evidence. Pin the SHA, name the branch, record the date. `ACTION LB` audits how many
rows in this KB are under-labelled this way.**

### 🆕 🟢 `T282` — the deployment dependency you assume is the one to measure

🔵 **The natural reading of `Artemis`'s AI surface is that the LLM work lives in `Pyris`, a `12`★
microservice, and that routing the AI means routing that risk.** 🔴 **That reading is wrong, and the
project's own admin documentation says so: *"The functionality is provided by Artemis and Spring AI,
so no EduTelligence service needs to be deployed."*** `Pyris` is required only for semantic lecture
search, and quiz generation *"falls back gracefully"* without it.
🟢 **So the AI authoring path needs an LLM endpoint and nothing else, and the `12`★ dependency sits
on an optional feature rather than on the critical path.** 🔵 **The general rule: read the admin
guide before pricing the architecture. A `231`-file subsystem and a `12`★ repository in the same
tree do not imply a dependency between them.**

### 🆕 🔴 `T283` — a uniform status across every subject is a verdict about the channel

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` for `46` of `46` repositories named
in this pass.** 🟢 **All `46` resolve under `git ls-remote` with a real `HEAD` sha, and
`raw.githubusercontent.com` answers `200` on their licence paths.**
🔵 **The rule, which transfers to any client's dependency audit: when a check fails identically for
every subject, it has measured the path and not the subjects. A dependency scanner reporting `100`%
unreachable is reporting its own egress. Check one known-good subject before believing a sweep —
and prefer the protocol channel (`ls-remote`, a registry API) over the HTML one.**

### 🟢 Carried trends, re-stated because the newest block is canonical

- 🟢 **Adoption outruns governance, in every region measured.** `86`% of education organisations use
  generative AI and most have no policy; LATAM higher education is `87`% adopted against `26`% with
  a formal strategy. 🔵 **The governance engagement is the market.**
- 🔴 **Teacher capability is the bottleneck, and it is widening in one region:** only `29`% of
  students think their instructors are equipped, while US and Canadian faculty INTENT to use AI fell
  `76`% → `67`% year over year. 🔵 **A capability programme needs no licence review and no
  conformity assessment, which makes it the fastest-starting work in this file.**
- 🆕 🟢 **The permissive supply's head is AGENT SKILL PACKS.** At least `6` of the top `12` on
  `topic:ai-tutor license:mit` declare `agent-skills`, `claude-code` or `codex`. 🔵 **This is a real
  shift in what *"open-source education AI"* means: the unit of distribution is becoming a prompt
  asset that rides inside a runtime the buyer already has, which is cheaper to adopt and impossible
  to own.**
- 🔴 **The permissive institutional SIS still does not exist** — sixteenth pass. 🟢 **And `Artemis`
  must not be sold as filling it: it owns exercises, exams and assessments, not enrolment, fees or
  guardians.**
- 🟡 **APAC regulation is a per-jurisdiction sequence, not a regional posture:** China binding and
  registration-based, Singapore voluntary-framework-plus-data-protection *(IMDA's agentic AI
  framework, `22` January `2026`)*, Japan innovation-first under the AI Promotion Act *(AI Basic
  Plan, `14` July `2026`)*, India mandating AI from Class `3` in `2026`–`27`, Vietnam naming
  education in its high-risk list. 🔵 **Sequence per country; never quote *"APAC compliance"*.**

## Pass 177 — 2026-10-13

🆕 🟢 **The trend that should change how an education engagement is SEQUENCED, and it comes from a
regulatory clock that moved while this KB was reading code: the education-AI duty that binds in
`2026` is TRANSPARENCY, and the high-risk duty everyone quotes at education has been pushed to
`2027`.**

| duty | class education falls in | applies from | distance from p177 |
|---|---|---|---|
| 🔴 **Article `50` transparency** — disclose that a user is interacting with AI | 🟢 **applies to the tutoring and authoring layer directly** | 🔴 **`2` August `2026`** | 🔴 **ALREADY IN FORCE** |
| 🔴 **Article `50(2)` marking of synthetic content** — grace period for systems already on the market | 🟢 **applies to every generated-content pipeline in this KB** | 🔴 **`2` December `2026`** | 🔴 **`50` days** |
| 🟡 **Annex III stand-alone high-risk** — access, progression, assessment, exam scoring | 🔴 **THIS is where education sits** | 🟡 **`2` December `2027`** *(moved by the Digital Omnibus)* | 🟡 **`~14` months** |
| 🟡 **Annex I embedded high-risk** | 🟡 rarely education | 🟡 **`2` August `2028`** | 🟡 **`~22` months** |

🔵 **Why this is a trend and not a date table:** for three passes this KB has built its compliance
work around Article `50(2)` on the grounds that it was the nearest deadline, and that choice is now
VINDICATED from outside — an independent channel puts the `50(2)` grace period at `2` December
`2026`, which is exactly the *"`50` days out"* this KB has been asserting. 🟢 **The first external
corroboration of a figure this KB derived on its own.**
🔴 **And the half that changes advice: a client told *"education is high-risk under the AI Act, act
now"* is being told something that is true about classification and wrong about timing by `14`
months.** 🟢 **The defensible sequence is marking and disclosure inside this engagement, conformity
assessment on a `2027` roadmap.**
🔴 **Held as a CONFLICT, not resolved:** the Omnibus is reported both as Regulation (EU)
`2026/1744` in force `27` July `2026` and as adopted `29` June `2026` / signed `8` July `2026`
awaiting publication; one source dates the `50(2)` grace period `2` February `2027` instead.
🔴 **No primary is reachable from here — `eur-lex`, `digital-strategy.ec.europa.eu` and both
law-firm hosts are NXDOMAIN (`gap 110`, widened).** 🔵 **Every one of these dates is secondary. The
sequencing conclusion survives the conflict; a specific date in a contract does not.**

🆕 🟢 **The second trend is a PRODUCT CLASS this KB can now name, because `ACTION KQ` measured an
instance of it: the non-adjudicating tool, and in education it is about to be the only kind that
sells.**
🟢 **Measured on [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos): `falsePositive` `0`,
`confidence` `0`, no pass/fail anywhere in `513` files.** It reports similarity and clusters pairs;
the threshold is GUESSED per dataset in the report UI; the engine's default `minSimilarity` is `0`.
🔵 **It cannot tell a student they cheated. It can only rank pairs for someone who can.**
🟢 **Now place that against the regulation, in two regions at once:** Annex III makes a system
high-risk where it determines access, progression or assessment — and Oklahoma and Maryland
**bar AI from high-stakes decisions about students and require human oversight** outright.
🔵 **So the same architectural property — no verdict — is what keeps a tool out of the EU's
high-risk class AND inside what two US states will permit at all.**
🟢 **The design rule, stated so it is reusable beyond this one repository: in education, push the
JUDGEMENT out of the system and keep the EVIDENCE in it.** 🔴 **The inverse — a product that scores
a student and reports a verdict — buys a conformity assessment in the EU, a prohibition in parts of
the US, and a procurement conversation nobody wins (`T277`).**

🆕 🔴 **The third trend is about this KB's own instruments and it is the most embarrassing finding
of the pass, which is why it is published at the top of three files: a measurement that is wrong by
one is never re-read.**
🟢 **`8` of `12` published licence byte counts in this repository are short by exactly `1` byte, and
the mechanism is proven** — the stripping channel drops a trailing line feed, and the `4` exact rows
are exact for two different reasons that both confirm it (`2` have no trailing `LF` to lose; `2`
were read by the other channel).
🔴 **p176 saw one instance, corrected it by hand as a typo, and then re-introduced the defect on all
`4` rows it admitted in the same pass.** 🔵 **The lesson is not *"count more carefully"*. It is that a
figure used as an IDENTITY must come from a channel whose failure mode is loud: `md5` reproduced
exactly across independent reads where the byte count did not (`T275`).**
🆕 🔴 **And a second instrument thesis from the same pass, caught before publication rather than
after: a scope-limited grep reports its scope, not the repository, and it fails in the direction
that flatters the finding.** `ACTION KQ`'s first probe searched `lib/`, `cli/` and `docs/` and was
about to publish *"`threshold` `0`"* and *"`cluster` `0`"* — repository-wide the true counts are
`16` and `178`. 🔵 **Both would have been sharper, quotable, and false (`T276`).**

🆕 🟡 **Fourth: the vertical's visible permissive supply has STOPPED MOVING, and four passes of the
same integer is now evidence rather than coincidence.**
`topic:ai-education license:mit pushed:>=2026-04-16` = **`135`** at p173, p175, p176 and p177.
🟢 **The tag's head is unchanged row for row — `agents-from-scratch` `1 045`★,
`universal-diagnostic-tutor-skill` `244`★, `vibe-schooling` `80`★ — so this is a stable population,
not a re-sample that happens to total the same.** The wide frame `topic:education license:mit` moved
`8 198` → **`8 199`**, `+1` for the second consecutive day.
🔵 **Consequence for p176's harness-coupled-skills trend: it HOLDS, and nothing new arrived to test
it. `7` of the top `30` declare an agent-skill topic and `11` name a specific harness; none of them
can answer a procurement questionnaire about where student data goes.** 🟢 **For a studio, the
stability is good news: the shelf does not rot between engagements, and the scarce work is
verification rather than discovery.**

🆕 🔴 **Fifth, a channel boundary that retires part of p175's celebrated finding.** `P175-B` made
the authenticated GitHub MCP channel this KB's best instrument, on the strength of exact population
counts in one request — which still holds, at `135` and `8 199`. 🔴 **But that channel refuses
CONTENT outside this session's attached repositories: `get_file_contents` on `dodona-edu/dolos`
returned an access denial, and `api.github.com` returned `403` with the same message.**
🟢 **What does serve any public repository: `raw.githubusercontent.com`, `git ls-remote`, and a
read-only `git clone` — which is how `ACTION KQ` was taken at all.**
🔵 **So the channel ledger needs two columns, not one: SEARCH reach and CONTENT reach are different
permissions, and p175's ledger collapsed them (`T278`).**


## Pass 176 — 2026-10-13

🆕 🟢 **The trend with the hardest evidence this pass, and it changes what *"open source AI agent
for education"* can be bought for: the vertical's new supply is shipping as HARNESS-COUPLED SKILLS,
not as applications.** Measured on `topic:ai-education`'s top `30` by stars, counted by declared
topic rather than by prose:

| shape, by DECLARED topic | rows of `30` | which |
|---|---|---|
| 🟡 **declares a SKILL topic** *(`skill`, `agent-skills`, `claude-skills`, `codex-skill`, `skill-pack`)* | 🟡 **`7`** | `universal-diagnostic-tutor-skill`, `taiwan-exam`, `skills-for-course-creators`, `learn-anything-skill`, `ai901-cert-buddy-claude`, `toefl-ai-skills`, `rviewer` |
| 🟡 **names a specific agent HARNESS** *(Claude Code, Codex, MCP)* with or without a skill topic | 🟡 **`11`** | the `7` above plus `Tov-learn`, `vibe-schooling`, `agent-trajectory`, `legal-ai-engineering-lab` |
| 🟢 **deployable application or dataset** | 🟢 **`19`** | the remainder, including both national-examination engines and both APAC curriculum datasets |

🔵 **Why it matters commercially rather than as a curiosity:** a skill is not a deployable product
for an institution. It runs inside somebody's agent harness, inherits that harness's auth, logging
and data path, and cannot be handed to a school district as a system. 🟢 **For a studio this is
good news in one direction and a trap in the other** — the authoring and tutoring layer can now be
assembled in days from permissive skills, and NONE of it satisfies a procurement questionnaire about
where student data goes. 🔴 **This KB's own `12`-row shelf is almost entirely applications, so the
tag's new supply differs from the shelf in SHAPE, not merely in size.**

🆕 🔴 **The second trend is an arms race, and both sides are `MIT` on the same platform.**
🔴 **Attack:** [`sgaofen/vibe-schooling`](https://github.com/sgaofen/vibe-schooling) — *"Get 4.0
GPA without learning"*, `80`★ and the **third-most-starred row on `topic:ai-education`** — names
Canvas `19` times, `quiz` `7`, `exam` `6`, `answer` `10`, and declares `canvas-lms` and
`exam-automation` as topics. `MIT`, `1 063` B, `HEAD` `7c2f87a4641b`, `56` files.
🟢 **Defence:** [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos), Ghent University's
source-code similarity detector, `MIT`, entered this KB one pass ago.
🔵 **The two are not symmetric, and that is the finding.** The attack is a student-side browser and
MCP automation against a specific LMS; the defence is an institution-side batch similarity analysis
over submitted code. 🔴 **They do not meet.** 🟢 **The design consequence for any assessment
engagement: integrity has to be built into the ASSESSMENT SHAPE — oral defence, process evidence,
in-session artefacts — because the permissive detector and the permissive cheat tool are not
operating on the same surface.** 🔵 **This KB has recorded that conclusion as a design pattern since
`P171-D`; p176 is the first pass that can name a tool on each side.**

🆕 🔴 **The third trend is a compliance SHAPE this KB can now state as a class, from a measurement
rather than a reading: the AI Act exposure on an education pipeline shows up as DATA LOSS, not as a
missing control.**
🟢 **Measured on the shelf's best-equipped row (`ACTION KI`):** the project stores a
`c2paStatus` — its generated schema registry lists the field as REQUIRED, and three writers set it.
🔴 **Its export quality gate reads twelve fields off each stored provenance record and discards the
thirteenth, substituting the one status that makes the gate pass.** 🟢 **The repair is one line.**
🔴 **And all three writers store `"absent"`, which the gate refuses — so the repair turns a green
gate red on every real asset, `50` days before Article `50`'s transparency duty.**
🔵 **The pattern to look for in a client's pipeline, stated so it is reusable: find the compliance
gate, list the fields it reads, and check each one against the field the pipeline actually stores.
A gate that substitutes a default for a stored value cannot fail, and it will pass an audit of its
own tests.** 🔴 **In this case `0` tests in the whole repository reference the field, so neither the
defect nor its repair is visible to the suite (`T270`).**

🆕 🟡 **Fourth, carried forward and now reproduced three times: the vertical's exactly-known size is
a repository count and the tag you choose moves it by `60.7×`.** `topic:education license:mit
pushed:>=2026-04-16` = **`8 198`**; `topic:ai-education` = **`135`**, stable across p173, p175 and
p176. 🔴 **And a keyword search is not an alternative frame: `tutor OR tutoring OR grading agent
license:apache-2.0 stars:>100` returns `1 684` rows of which `0` of the top `25` are
education-vertical.**

🟡 **Carried trends, re-stated in one line each because a trend not re-stated leaves the compiled
view (`T216`):**

- 🟢 **Compulsory AI curricula are the APAC demand driver** — China from age `6`; India from Class `3`
  in academic year `2026-27`. 🔵 **An age and an academic year are verifiable facts about demand; a
  CAGR is a model.**
- 🟢 **Two markets now carry a synthetic-content marking duty, and the Chinese one is broader and
  already live** — Art. `4` explicit / Art. `5` implicit, since `1 Sep 2025`, applying to all
  synthetic content regardless of confusion potential; the EU's Article `50` transparency duty is
  `50` days out. 🔴 **Both read from secondary coverage only: every legal-text host is NXDOMAIN
  here (`T267`).**
- 🟡 **Market forecasts for AI in education do not reconcile and should be quoted singly, never
  summed** — p176's sweep returned `2025`-base figures from `US$7.52B` to `US$8.3B`, a `2026` figure
  of `US$10.6B`, a `2034` projection of `US$79.6B` and CAGRs from `15.9%` (North America) to
  `46.12%` (global). 🔵 **One sector-maturity rating in the same sweep — `35`/`100`, *"most
  institutions still in pilot mode"* — is more useful to a studio than any of the revenue lines,
  because it names the stage rather than the size.**
- 🔴 **Institutional readiness, not model capability, is the binding constraint in every region
  where p176 found evidence** — `10%` of North American institutions with formal AI guidelines,
  `71%` of US teachers untrained, `65%` of LATAM students fearing superficial learning, and the
  Council of Europe convening on regulation while the UK funds deployment. 🟢 **Governance,
  assessment redesign and teacher enablement are better supported by this pass's evidence than any
  tooling pitch.**

## Pass 175 — 2026-10-13

🆕 🟢 **The trend this pass can prove rather than cite: four of this KB's standing statements were
artefacts of its own INSTRUMENTS, not of the world — a channel ledger, a tag, a grep and a
falsifier sentence. Each one had a measurement behind it. Each measurement was taken correctly. All
four conclusions were wrong anyway, because the thing measured was not the thing claimed.**

### 🆕 🟢 1. A channel ledger is only as good as the request forms somebody thought to try

🟢 **Measured: the authenticated MCP repository-search channel returns `8 197` — an exact integer,
one request — where p174 needed `17` paced requests partitioning a page that rounds to reach
`8 191`.** p174's ledger named `7` request forms and correctly identified the `2` that answer.
🔴 **The eighth form was an authenticated tool already loaded in the session, and nothing in the
ledger's method would ever have found it, because the ledger enumerated HTTP shapes rather than
capabilities.**
🔵 **`T264`, and it generalises past GitHub: a negative result about reachability is a claim about
the forms enumerated, exactly as `P50` is a claim about the paths probed.** The two rules are the
same rule at different layers.
🔵 **What it costs: one request. What it buys: every four-figure population figure in this KB
becomes free, and the `17`-window partition becomes a fallback with a `-0.07%` agreement control
rather than the method of record.**
🔴 **And the new channel's limit, measured: it answers SEARCH and refuses per-repository file reads
by session scope. Three channels, three jobs — MCP for counts, `raw.githubusercontent.com` for
licence bodies, `git ls-remote` for `HEAD`s.**

### 🆕 🔴 2. A tag is a sampling frame, and this one sampled a continent out

🟢 **Measured, like-for-like, `P800` applied row by row to the top `50` by stars of each
population:** `topic:education` places `12` rows — `5` North America, `5` APAC, `2` EMEA, `4` of
them holder-grade. `topic:ai-education` places `7` — `6` APAC, `1` EMEA, **`0` North America, `0`
holder-grade.**
🔴 **The trend statement, and it is about this KB rather than the market: eleven passes of *"the
agent tier is APAC-weighted and North America is thin at the repository layer"* described the
sampling frame.** `T255` found the tag was `60.7×` too small. 🔵 **`T266` finds something worse than
small: it is BIASED, and in the dimension this KB reports on most.**
🟢 **Why the bias has a mechanism rather than being bad luck:** what tags itself `ai-education` is
mostly a single-maintainer tutor skill built against one national examination — and those cluster in
APAC, where curriculum-anchored exam prep is a large consumer category. 🔵 **Institutional education
software does not tag itself `ai-education`, because it is not an AI product.** `Artemis` is a
university's exercise platform. `canvasapi` is a Canvas client. `Dolos` is a plagiarism detector.
**They are the substrate AI gets added to, and that is what an engagement actually starts from.**
🟢 **The practical consequence: use the narrow tag for a shortlist of AI-native tools, and the wide
tag for anything regional, institutional or procurement-shaped.**

### 🆕 🔴 3. A substring grep fails only in the direction that flatters its subject

🟢 **Measured on p174's new student information system:** `ed-fi` `55` file hits → **`0`** at word
boundary (it was matching `red-fill`); `edfi` `176` → **`0`** (`normalizedField`); `lti` `325` →
**`0`** (`LevelTile`, `ModalTitle`); `oidc` `29` → **`0`** (`autoIdCount`); `jwt` `16` → **`0`**
(base64 in lockfiles). 🔴 **`0` of `17` interop and auth tokens survive at word-boundary precision.**
🔵 **`T265` — the error is ONE-DIRECTIONAL, which is what makes it dangerous.** A substring match can
only ever over-report, so this class of mistake always makes a candidate look better than it is, and
never worse. **A measurement whose errors all point one way is not noisy; it is biased.**
🔴 **And p174 had already taken the right precaution.** Its instruction was *"grep the tree rather
than the README"* — a good rule, correctly followed, which still produced three false positives.
🔵 **The repair is not a better rule about WHERE to look. It is a rule about WHAT to look for: name
the artefact that would have to exist** — an `/ims/oneroster/v1p1` route, an `EdFi` client class, a
`cmi5` or xAPI statement emitter, a tenant column — **and look for that.** A standard's NAME appears
in CSS variables; a standard's IMPLEMENTATION does not.

### 🆕 🟡 4. One falsifier sentence can ask two questions with different answers

🟢 **Measured: `6` instruments WRITE a hardcoded dated evidence file. `1` instrument actually
REWROTE one when re-run.** `ACTION KF` asked both in a single sentence — *"sweep for scripts that
write a dated file … and measure how many dated results differ after a re-run"* — and set its
falsifier at *"`≤1` instrument"*. 🔴 **At `6` the limb is silent; at `1` it fires.**
🔵 **`T268` — a falsifier that names a threshold must also name the denominator it counts, and
`T234` already taught this KB that a limb can be decided by a word the action never defined.** p175
publishes both readings and marks which limb lands on which, rather than selecting the one that
reads better.
🔴 **And the finding worth more than either number: `9` of `28` script executions exit NON-ZERO,
and two of the four instruments whose dated files did not change are among them.** 🔵 **They did not
hold their evidence steady — they could not run.** An instrument that fails reports identically to
an instrument that is deterministic, in any sweep that does not record the exit code. **A third of
this repository's sampled instrument suite does not execute cleanly at `HEAD`, and that is the
larger defect.**

### 🆕 🔴 5. An egress allowlist is not a host's policy, and the difference changes what you promise

🟢 **Measured at the resolver, `11` hosts:** `cac.gov.cn`, `www.gov.cn`, `npc.gov.cn`,
`chinalawtranslate.com`, `agora.eto.tech`, `twobirds.com`, **`eur-lex.europa.eu`** and
`en.wikipedia.org` are all **NXDOMAIN**. Only `github.com` and `raw.githubusercontent.com` resolve.
🔴 **`gap 110` has been carried for many passes as *"`eur-lex` is `403` at the `CONNECT` layer by
organisation policy"*. It does not resolve, and neither does Wikipedia.**
🔵 **`T267` — p174 attributed to one host's policy what is a property of the whole egress layer.**
The practical difference is large: a host policy might be argued with or routed around, and an
allowlist cannot be. 🟢 **The correct statement, declared once rather than rediscovered per
instrument: no primary legal text is directly reachable from this container by any channel, and
every legal date in this KB is `search-summary` tier until the allowlist changes.**
🔵 **`WebSearch` and `WebFetch` traverse a different path and are not bound by the resolver — which
is exactly why `github.com/search` answers through one tool and refuses `curl`.**

### 🆕 🟢 6. A compliance defect can be data loss rather than a missing control

🟢 **Measured on the shelf's most provenance-literate row.** p173 found the C2PA flag *"defaults
off"*. p174 found that turning it ON changes nothing, because the gate accepts the
`NOT_APPLICABLE` status every asset is born with. 🟢 **p175 found the level underneath: the project
ALREADY STORES a real status and the gate never sees it.**
🔴 **Its generated schema registry lists `c2paStatus` as a REQUIRED property of `AssetProvenance`.
Three writers set it to `"absent"`. And `_provenance_quality_gate` reads TWELVE fields off each
stored record and discards the thirteenth, substituting `NOT_APPLICABLE` at one line.**
🔵 **`T269` — `ABSENT` is the status that makes the gate FIRE and `NOT_APPLICABLE` is the status that
makes it PASS. The code reads the first and writes the second.** That is not a missing feature; it
is a one-line laundering of the project's own evidence.
🟢 **The trend statement for the `50` days to the EU's `2 December 2026` marking backstop — and for
China's Art. `5`, live since `1 Sep 2025`: the cheapest compliance movement available on this shelf
is not building a signer. It is stopping the pipeline from throwing away what it already knows.**
🔵 **The signing certificate is still procurement, but it is now procurement for the VISIBLE
marking duty only. The metadata duty is free.**

### 🆕 🔴 7. The regulatory split a deck must not merge

🟢 **Confirmed against multiple secondary sources this pass, and one of them against this KB's own
carried figure:** the EU's Digital Omnibus moved **Annex III high-risk** obligations — which carry
education, including admissions screening, automated grading, proctoring and student monitoring — to
**`2 December 2027`**, and Annex I to `2 August 2028`. 🔴 **It did NOT move Article `50`.**
Transparency has applied since `2 August 2026`, with the `2 December 2026` backstop for
machine-readable marking of systems already on the market — the date this KB quotes as *"`50`
days"*, and it survives the check.
🔵 **Why this is a trend and not a footnote: a client's transparency obligation is live NOW and
their high-risk obligation has `26` months.** Those are two programmes with different budgets,
different owners and different artefacts, and a deck that merges them will over-sell urgency on one
and under-sell it on the other.
🟢 **And the deployer duties that were never postponed are the ones an engagement actually bills
for:** human oversight, monitoring, logging and informing affected people (Art. `26`), plus a
Fundamental Rights Impact Assessment before deployment (Art. `27`).
🔴 **Said rather than implied: none of those dates was read in primary form, for the reason trend
`5` measures.**

### 🆕 🟢 8. Teacher readiness is the binding constraint, and one market has now proved it expensively

🟢 **South Korea legislated AI textbooks into schools and then stripped them of official status
after adoption stayed under `30%` and teacher unions objected that the pace had outrun
preparation.** 🟢 **The redirect was a `US$960M` programme for AI talent centres and vocational
schools through 2030 — capacity rather than content.**
🔵 **Set that against the adoption numbers from the other end of the distribution:** teacher AI use
at `56%` in Brazil, `55%` in Chile, `53%` in Colombia and `52%` in Costa Rica, against an OECD
average of `36%` — in markets with far less mandated rollout. 🔴 **UNESCO IESALC finds the governance
behind that adoption, not ahead of it.**
🟢 **The trend statement: mandating the artefact does not move adoption, and not mandating it does
not stop adoption.** 🔵 **What an engagement can actually sell into is the gap between those two
facts — teacher capability, and the governance that lets an institution say yes.**
[`evidence/channel-ledger.2026-10-13-p175.tsv`](../evidence/channel-ledger.2026-10-13-p175.tsv)
· [`evidence/sis-interop-probe.2026-10-13-p175.tsv`](../evidence/sis-interop-probe.2026-10-13-p175.tsv)
· [`evidence/dated-rerun.2026-10-13-p175.tsv`](../evidence/dated-rerun.2026-10-13-p175.tsv)

## Pass 174 — 2026-10-13

🆕 🟢 **The trend this pass can prove rather than cite: three of the four things this KB called
absences were artefacts of its own measurements, and the fourth one just stopped being a question.
A permissive SIS, an exact vertical size and a buildable marking path all existed last pass. What
was missing was a denominator, a method and a line number.**

### 🆕 🟢 1. A rounded number is a method problem, not a channel limit

🟢 **Measured: the rendered search channel reports an exact integer at or below ~`1 000` and two
significant figures above it. `pushed:` holds one value per repository, so date windows are
disjoint. `17` windows later: `8 191`, against *"`8.2k`"*.**
🔴 **The trend statement, and it generalises past GitHub: an API that refuses and a page that
rounds are different failures, and this KB spent two passes treating the second as the first.**
`api.github.com/search` and GraphQL both refuse here by session binding; `repos.ecosyste.ms` is
denied at the CONNECT layer by egress policy. 🟢 **The channel that answers was always sufficient —
once asked `17` smaller questions instead of one big one.**
🔵 **What it costs: `17` requests paced around a `429` that arrives after roughly `7`–`10` reads.
What it buys: every four-figure figure in this KB becomes exact.**

### 🆕 🔴 2. A negative re-tested on an unchanged denominator is not re-tested — it is repeated

🔴 **Measured: *"SIS, permissive: none exists"* was carried for TWELVE passes and refuted in one
query once the denominator was fixed.** `"student information system" license:mit
pushed:>=2026-04-16` → **`54`**, exactly. Two have real trees:
[`eagles-edu/sis`](https://github.com/eagles-edu/sis) (`2 598` files, committed `17` days ago) and
[`opensacorg/learning-blocks`](https://github.com/opensacorg/learning-blocks) (`849` files, Code
for Sacramento, `28` days).
🟢 **The trend statement: in an append-only knowledge base, a repeated negative accumulates the
appearance of evidence.** Each pass that re-states it adds a date and no information. 🔵 **The fix
is a rule, not a correction: a carried negative must name the QUERY that would refute it, and the
query must change when the population's definition changes (`T259`).**
🔴 **The residue, stated so the correction is not over-read: the head of that `54` is `31`★.** There
is still no institutional-scale permissive SIS — which is a procurement finding and not an absence.

### 🆕 🔴 3. A compliance flag nothing exercises is a label, not a control

🔴 **Measured on the shelf's most provenance-literate row: `46` of `46` of its own security tests
pass with `c2pa_required=False` and `46` of `46` pass with it `True` — byte-identical. The flag is
never set in any test in the repository, and the gate accepts the *"not applicable"* status that
every generated asset is born carrying.**
🟢 **The trend statement for the `50` days to Article `50(2)`: the market's provenance readiness
cannot be read off the presence of C2PA vocabulary, a gate, or a manifest type. All three are
present here and `0` bytes get marked.** 🔵 **The diligence question that separates a label from a
control is *"which test fails when you turn it off?"* — and on this row the answer is none
(`T258`).**

### 🆕 🔴 4. A star count and a commit date disagree — but only against the right denominator

🔴 **Measured: the top `20` of the tagged population by stars is dormant at `65.0%` / `40.0%` /
`10.0%` (`30` / `60` / `90` days by COMMIT date), against the whole population's
`71.1%` / `47.4%` / `25.2%`.** 🟢 **So the star head is FRESHER than its own tail, not deader —
p173's wording, corrected here by the larger sample it asked for.**
🔴 **What does hold, and it is the one that matters for a shortlist: the head is far deader than
this KB's curated shelf**, whose sampled rows last committed `0`, `1`, `3`, `4` and `22` days ago.
🔵 **The trend statement: curation beats ranking in this vertical, and *"popular"* and *"tagged"*
are both worse liveness proxies than *"someone picked it and checked"* (`T263`).**

### 🆕 🟡 5. The regions' obligations are converging and the instrument is the same one

🟢 **Measured this pass: China's Interim AI Measures have required LABELLING of AI-generated content
since `15 August 2023`; the EU requires machine-readable marking of synthetic content from
`2 December 2026`; and China additionally mandates `≥8` hours of AI instruction per school year from
`2025`.**
🟢 **The trend statement: the Article `50(2)` tooling this KB has been building for one jurisdiction
is a two-market instrument already, and the second market's deadline is three years in the past.**
🔴 **Neither primary text has been read here** — `eur-lex` is `403` at the CONNECT layer (`gap 110`)
and the Chinese measures were never asked for. 🔵 **Two obligations, two secondary-source readings,
one instrument. The instrument is the asset; the dates are the liability.**

### 🆕 🟡 6. Absence has a shape, and the shape is sellable

🔴 **Measured: `16` formulations across two channels returned `0` MEA-originated permissive active
education-vertical repositories. Of the four candidates whose licence body was read at a verified
`HEAD`, three fail only on ACTIVITY (`191`–`334` days) and the fourth only on LICENCE (`GPL-3.0`).**
🟢 **The trend statement: *"nothing exists"* and *"three exist and each is one criterion short"* are
different briefs, and only the second one has work in it.** A dormant `MIT` repository grounded in
the Egyptian national curriculum is a fork with no licence conversation.
🔵 **And the method rule that produced it, worth more than the finding: a four-way filter should be
reported as four columns, never as one verdict.** This KB reported the AND for seven passes.
[`evidence/exact-count-partition.2026-10-13-p174.tsv`](../evidence/exact-count-partition.2026-10-13-p174.tsv)
· [`evidence/aiact-50-2-insertion-point.2026-10-13-p174.tsv`](../evidence/aiact-50-2-insertion-point.2026-10-13-p174.tsv)
· [`evidence/mea-candidate-licences.2026-10-13-p174.tsv`](../evidence/mea-candidate-licences.2026-10-13-p174.tsv)
## Pass 173 — 2026-10-13

🆕 🔴 **The trend this pass can prove rather than cite: the open-source AI-education landscape is
measured with a tag `1` in `12` of its own best projects uses, and a quarter of what the tag returns
has been abandoned for a quarter. Both halves are measured this pass; neither was known last pass.**

### 🆕 🔴 1. The vertical is `~61×` bigger than this KB has been saying, and nobody can state it exactly

🟢 **Measured: `topic:ai-education pushed:>=2026-04-16 license:mit` = `135`. Same filters on
`topic:education` = **`~8.2k`**. On `topic:edtech` = `~1.3k`. And `9` of this KB's `12` shelf rows
carry `education` while `1` carries `ai-education`.**
🔴 **The trend statement: `ai-education` is a RESEARCH-FLAVOURED tag and practitioners do not use
it.** They tag `education`, `edtech`, `ai-tutor`, `lms`, `spaced-repetition` — the vocabulary of
the thing they are building, not of the category an analyst would file it under. **A topic query is
a hypothesis about how a community labels itself, and this one was wrong by one to two orders of
magnitude.**
🔴 **And it cannot currently be fixed to a number: the channel that answers rounds above `1 000`
(`T252`). Anyone quoting a count of the open-source education vertical — this KB included — is
quoting one significant figure.**

### 🆕 🔴 2. Abandonment, not growth, is the dominant state of the tagged population

| band | unpushed | share of `135` |
|---|---|---|
| `30` days | `96` | 🔴 **`71.1%`** |
| `60` days | `64` | 🔴 **`47.4%`** |
| `90` days | `34` | 🔴 **`25.2%`** |

🔴 **And the star head is worse than the tail, which is the counter-intuitive half.** The `5`
members of the `≥20`★ permissive head last committed `14`, `18`, `79`, `85` and `88` days before
this pass — `3` of `5` dormant at `60` days. **Five shelf rows sampled the same way: `0`, `1`, `3`,
`4`, `22` days.** 🟢 **The trend statement: a star count is a record of past attention and a commit
date is a statement about the present, and in this vertical they point in opposite directions
(`T253`).** 🔴 **Practical consequence for any shortlist: `pushed:` + `180` days — the filter this
KB and most tooling uses — admits a quarter of its population as *"active"* while nobody works on
it.**

### 🆕 🔴 3. The marking cliff, now specified to the line — and the critical path is a certificate

🔴 **`50` days to Article `50(2)`. `0` of `13` generating shelf rows can mark output. p173 read the
one row that had the machinery (`AkshitIreddy/AI-Powered-Video-Tutorial-Generator`, `9c260890214d`)
and the result is more precise and less hopeful than `T233` suggested:**

| piece | state |
|---|---|
| per-asset provenance record, export manifest, licence/consent gates | 🟢 **BUILT, real, `20`+ tests** |
| a gate that CAN refuse an unmarked export | 🟡 **BUILT and OFF — `c2pa_required` defaults `False`** |
| a signer / embedder | 🔴 **ABSENT in `905` files** |
| a signing identity | 🔴 **ABSENT — and it is a certificate, not code** |

🔴 **The single line that tells the story: `generation/workflow.py:3018` is the only place the
pipeline builds a C2PA record for an asset it generated itself, and it writes
`C2paStatus.NOT_APPLICABLE`.**
🆕 🔴 **And the trend generalises past this repo, which is why it is in this file: the credential
survives GENERATION and dies in POST-PRODUCTION.** The same project records, in a code comment,
that its presenter PNG *"carries embedded C2PA provenance"* from the upstream image generator while
*"the optimized WebP derivative does not"* (`T256`). **Vendors are shipping marks; pipelines are
transcoding them off.** 🟢 **For anyone building to the deadline, the engineering is small —
`c2pa-rs` / `c2patool` are **`MIT OR Apache-2.0`** (`contentauth`) — and the procurement is the
critical path: an X.509 certificate from a CA in the C2PA trust list. Self-signed validates as
untrusted.**
🆕 🔴 **`T246` — and there are TWO obligations being confused as one.** Article `50(2)` marking is
machine-readable and about the artefact; Article `50(4)` deepfake disclosure is human-readable and
about the viewer. The shelf's most advanced row has a boolean called
`synthetic_media_disclosure` — and it records that the SUBJECT of a likeness consented, not that
the LEARNER was told. **Nothing on this shelf tells a learner anything.**

### 🆕 🟢 4. Compulsory AI curricula have reached the Gulf, and the mandate now leads the tooling

🟢 **The UAE and Saudi Arabia have made AI education compulsory across public schooling — the UAE
from age four, `KG`→grade `12`, with `24 000`+ educators through a national upskilling week for
`2026–2027`. Egypt began AI curricula in the `2025-26` academic year under a National AI Strategy
`2025–2030`.**
🟢 **The trend statement, and it is the opposite of the usual one: in the Gulf the POLICY is ahead
of the PRODUCT.** Three national systems are obliged to teach AI and the open-source shelf that
could serve them contains `0` repositories originating in the region. 🔴 **Compare Africa, where
the mandate is absent and the gap is governance: `6` in `10` of `47` surveyed universities have no
AI policy, and under `2%` of African edtech startups build AI for higher education.**
🟡 **What to watch: whether the Gulf mandate pulls assessment-integrity tooling into the market
faster than Europe's Article `50` pulls marking tooling. Both deadlines are now inside `14` months
and the first has `30M`+ students attached to it.**

### 🟢 5. Carried trends, unchanged by p173

🟢 **The administrative layer is still agentless** — `7` platforms, `0` rostering- or
analytics-primary agents (`gap 123`). 🟢 **Assessment is deeper than the shelf admits** — `2` of
`12` assessment-PRIMARY, `5` of `12` assessment-CARRYING (`T234`). 🟢 **The copyleft wall in
education ERP/SIS holds for a twelfth pass** — no `MIT`/`Apache` education ERP, no permissive SIS,
though p173 is the first pass to note that verdict rests on a denominator it has now measured as
`~61×` too small.
[`evidence/dormancy-bands-135.2026-10-13-p173.tsv`](../evidence/dormancy-bands-135.2026-10-13-p173.tsv)
· [`evidence/aiact-50-2-emitter-gap.2026-10-13-p173.tsv`](../evidence/aiact-50-2-emitter-gap.2026-10-13-p173.tsv)
## Pass 172 — 2026-10-13

🆕 🔴 **The trend this pass can prove rather than cite: `0` of `13` open-source education agents
that generate content can MARK it as generated, `50` days before Article `50(2)` requires it.
Measured over `18 360` files, `0` marking artefacts, `0` marking dependencies (`ACTION JQ`).**

### 🆕 🔴 1. The marking cliff — `50` days, `0%` readiness

🟢 **Article `50(2)` of `Regulation (EU) 2024/1689` requires machine-readable marking of synthetic
content from **`2 December 2026`**. The Digital Omnibus (`2026/1744`, in force `27 July 2026`)
deferred Annex III high-risk to `2027` and left Article `50` alone.**
🔴 **`13` of this KB's `19` shelf rows put generated content in front of a learner. None of them can
mark it.** 🟡 **`4` rows carry INPUT provenance — where source material came from — which is a
different obligation, and the row with the MOST provenance machinery is the one generating synthetic
VIDEO and marking nothing.**
🔵 **The trend statement: provenance was built because engineers wanted to trust their inputs.
Marking has to be built because a regulator wants learners to distrust their outputs. The ecosystem
built the first and skipped the second, and the deadline is for the second.**

### 🆕 🟢 2. Compulsory AI literacy is already late, and nobody is selling it

🟢 **Article `4` AI literacy and the Article `5` ban on **emotion recognition in education
institutions** have been binding since **`2 February 2025`**. Both predate every deadline this KB
has been tracking.**
🔴 **Decks open on Annex III — `2 December 2027` — which is the FURTHEST date. The two obligations
already in force get no mention.** 🟢 **Staff training is a live, overdue, billable obligation in
every EU institution, and it needs no model and no platform.**

### 🆕 🟢 3. Governance is the product now, not personalisation

🟢 **Convergent across `1EdTech`, HolonIQ and the non-vendor coverage: buyers have moved from
*"does it personalise?"* to *"can you show oversight, policy and evidence?"***
- 🟢 **`1EdTech`: institutions are building governance structures and compliance processes around AI.**
- 🟢 **HolonIQ: focus shifting to ethics, transparency and **proven instructional benefit** over broad personalisation promises.**
- 🔴 **Procurement has dates attached. **Ohio** required every K-12 district to adopt a formal AI use policy by `1 July 2026`; **Oklahoma** and **Maryland** mandate human oversight and bar AI from high-stakes student decisions.**

🔴 **And the measurement that makes this the dominant trend: UNESCO IESALC finds **`87%`** of `200`
LATAM institutions using AI and **`26%`** with a formal AI strategy. A `61`-point gap between
deployment and governance is the market.**

### 🆕 🟢 4. Purpose-built platforms displacing generic chatbots

🟢 **The stated reason, and it is an operational one: general chatbots left teachers doing the
prompt engineering and the fact-checking. The shift is to tools that arrive knowing the curriculum,
the rubric and the record.**
🟢 **Visible on this KB's own shelf: `6` of `12` agent rows are tutoring-primary, and the ones
gaining are the ones carrying a SCHEDULER or a KNOWLEDGE MODEL — `OpenTutor` (FSRS),
`anki-mcp-server` (spaced repetition), `SenmuuuuW/universal-diagnostic-tutor-skill` (decides whether
to explain, ask, drill **or stop**). 🔵 **Knowing when NOT to generate is becoming a feature.**

### 🆕 🔴 5. Assessment is where the new code is, and the catalogues missed it

🟢 **`4` of the `5` repositories that entered this KB last pass are assessment tools — entrance
exams, bar exams, vendor certification — and one exists to DEFEAT proctoring.**
🔴 **But the full read corrects the strength of the claim: the `≥20`★ permissive head of the
`ai-education` topic is `3` tutors, `1` assessment tool and `1` circumvention tool. Assessment is
where the CATALOGUE was thin, not where the ecosystem suddenly moved (`T229`, corrected).**
🔴 **The circumvention shape is a genuine new category and it is adversarial: `MIT`-licensed,
`80`★, Canvas-LMS + `MCP`, advertising *"get 4.0 GPA without learning"*. It automates precisely
what Annex III point `3` names as high-risk monitoring. 🟢 **Any assessment engagement now needs an
integrity threat model, because the attack tooling is permissively licensed and trivially
deployable.**

### 🆕 🟢 6. Skills-based credentials, driven by employers

🟢 **`1EdTech` names employer demand pushing the shift to skills-based credentials; HolonIQ reports
growing interest in competency frameworks and career-navigation tools.**
🟡 **This KB's exposure is partial and honest about it: `OB3DefinitionWidget` (`MIT`) covers Open
Badges `3.0` AUTHORING, and `OpenOLAT`'s badge module is `2.0`-only with no W3C Verifiable
Credentials. The `v3` issuance and verification path is still unrouted.**

### 🆕 🔴 7. Regional divergence is now structural, not a lag

🟢 **Three regulatory models are operating simultaneously and they are not converging:**

| model | where | what it means for a build |
|---|---|---|
| 🔴 **ex-ante, risk-tiered** | EMEA (`2024/1689` + `2026/1744`), **South Korea** (`AI Basic Act`, Jan 2026, education a named high-impact domain), **Vietnam** (in force `1 Mar 2026`, education gets a `6`-month grace) | conformity work before deployment; marking by `2 Dec 2026` in EMEA |
| 🟡 **operational labelling, already live** | **China** — algorithm filings, **synthetic-content labelling**, security review for public models | the EMEA marking obligation, in production today |
| 🟡 **state-by-state / policy-first** | **US** (`134` bills, `31` states, `>30` guidance documents), **Colombia** (`CONPES 4144`, policy before statute), **Japan** (voluntary) | per-jurisdiction configuration, not one compliance build |

🔵 **The practical consequence: marking tooling written for EMEA ships to China with a different
label and no new engineering, and ships to the US as an optional feature nobody requires yet. Build
it once, for the strictest, and gate it per region.**

### 🆕 🟡 8. The market-size number is not knowable, and saying so is the trend

🔴 **Research and Markets: **`~$10.6B` (2026) → `$42.48B` (2030)**. K-12 Academics:
**`~$6B` (2024) → `~$32B` (2030)**. Grand View for APAC alone: **`$18.21B` by 2033 at `28.1%`
CAGR**. These do not reconcile and they are measuring different scopes.**
🟢 **Report the range with both sources named. A client who checks finds both, and a KB that
published one looks like it only read one.**
🔴 **`T240` — and the sourcing is uneven in a way that correlates with confidence: the APAC and
LATAM claims on this page rest on UNESCO, OECD TALIS, Ipsos and Grand View; the NA and EMEA
adoption claims rest substantially on consultancy and vendor blogs selling compliance services.
**The two regions with the weakest sourcing carry the most confident numbers.****
## Pass 171 — 2026-10-13

🆕 🔴 **The trend this pass is about THIS KB's instruments, and it is the most consistent signal on
the shelf: of the `9` defects p171 found, `0` were legal questions and `8` were FORMATTING or
ARITHMETIC. A knowledge base about licences keeps being defeated by text layout, not by law.**

| # | what broke | what it actually was |
|---|---|---|
| 🔴 **1** | 🔴 **three passes called a measurement impossible** | 🔴 **arithmetic: each handoff re-anchored on the pass that WROTE it, so the reachable date walked forward one hour per pass (`T220`)** |
| 🔴 **2** | 🔴 **`LGPL-2.1` classified as dual `GPL+LGPL`** | 🔴 **LGPL §`3` names the ordinary GPL in prose. A family name matched anywhere in a body is not a grant (`T224`)** |
| 🔴 **3** | 🔴 **`junit-3.8.1` classified `GPL+MPL+Python`** | 🔴 **it is `IPL-1.0`, a family the predicate did not know, so every hit was a prose reference (`T224`)** |
| 🔴 **4** | 🔴 **a phrase search returned `0` where the phrase was present** | 🔴 **legal text is hard-wrapped at ~`70` columns: `GNU General Public\nLicense` (`T224`)** |
| 🔴 **5** | 🔴 **`Apache-2.0` and a GNU notice both read as NO family** | 🔴 **Markdown: `# Apache License` and `[GNU General Public License ...](...)` (`T224`)** |
| 🔴 **6** | 🔴 **`6` *"non-commercial"* findings in `Moodle`** | 🔴 **`4` were GPL-3.0's own §`6(b)`; `2` were PHP files listing Creative Commons options as DATA (`T223`)** |
| 🔴 **7** | 🔴 **`193` grant bodies in `Moodle`** | 🔴 **`105` were source files carrying a per-file GPL header (`T223`)** |
| 🔴 **8** | 🔴 **a cross-block gate reporting `372` lost rows** | 🔴 **wrong POPULATION, not wrong threshold: census tables counted as routing tables (`T225`)** |
| 🔴 **9** | 🔴 **the same gate reporting a RESTORED row as lost** | 🔴 **GitHub slug case: `openolat/OpenOLAT` vs `OpenOLAT/OpenOLAT` (`T226`)** |

🔵 **Every one was caught before publication, `5` of them by regression tests written in the same
pass. The pattern worth carrying: when this KB is wrong, it is almost never wrong about a licence —
it is wrong about a string.**

### 🆕 🟢 Trend — the regulatory clock was being read from the wrong end

🔴 **This KB has been watching the Annex III high-risk date for several passes. That date moved to
`2 December 2027` under `Regulation (EU) 2026/1744`, the Digital Omnibus on AI. The date that did
NOT move is Article `50` transparency: `2 December 2026`, `50` days from this pass.**
🟢 **So the trend is a REVERSAL of urgency. The obligation this shelf is tooled for
(`compose/code/aiact-50-2-*`) is the one arriving first, and the obligation it has been anxious
about has a year more than assumed.**
🟢 **`gap 114` closed as a non-conflict: `2 August 2026` and `2 December 2027` were two sources
being right about the base Act and its amendment.**

### 🆕 🔴 Trend — the vertical's live edge is ASSESSMENT, and this shelf is a tutoring shelf

| | |
|---|---|
| 🔴 **what `ACTION JN` found** | 🔴 **`4` of `5` new permissive finds are assessment: entrance exams, bar exams, vendor certification, and one tool for DEFEATING proctoring** |
| 🔴 **what this shelf holds** | 🔴 **`12` rows, almost all tutoring** |
| 🔵 **the reading** | 🔵 **the shelf is not a small SAMPLE of the vertical, it is a BIASED one, and the bias has a direction (`T229`, `ACTION JP`)** |
| 🟢 **why it matters commercially** | 🟢 **Vietnam's and Korea's statutes name automated ASSESSMENT specifically, and Annex III point `3` names evaluating learning outcomes and monitoring during tests. Regulation and open-source supply point at the same place, and this shelf points elsewhere** |

### 🆕 🟡 Trend — permissive means `MIT` or nothing in this vertical

🟢 **Measured across the whole `ai-education` topic: `135` `MIT`, `14` `Apache-2.0`, `0` `BSD`,
`0` `ISC` among active repositories. A studio planning to compose rather than fork should expect
`MIT` and should expect it WITHOUT a patent grant — which is the one thing `OpenOLAT`'s
`Apache-2.0` adds over the whole long tail.**
🔴 **And the copyleft floor has not moved in TEN passes: no SIS and no education ERP exists under
`MIT` or `Apache-2.0`, now tested against a `485`-repository sweep as well as the usual queries.**
## Pass 170 — 2026-10-13

🆕 🔴 **The trend p170 can evidence is about MEASUREMENT, and it is uncomfortable because every
instance this pass is self-inflicted. Three of this pass's own instruments produced wrong answers
before they produced findings, and a fourth — a gate this KB has reported as a growing defect count
for three passes — turned out to be `96%` noise.**
🆕 🔴 **`T217`: the KB cites an unverified amending regulation `86` times across `7` files and names
the AI Act itself `0` times in any current content file. A citation can be repeated into the
appearance of a source.**
🆕 🔴 **`T216`: a verified, permissive, actively-developed institutional LMS fell off this KB's
routing table while staying verified `745` lines below it in the same file. The append-only
convention has a cost and p170 is the first pass to measure it.**
🆕 🟢 **The one external trend with new evidence: compulsory AI curricula are now the APAC driver.
China from age `6`, India from Class `3` in academic year `2026-27`. That is procurement with a date,
not strategy with a direction.**
[`evidence/name-vs-body-divergence.2026-10-13-p170.tsv`](../evidence/name-vs-body-divergence.2026-10-13-p170.tsv)
[`evidence/region-gate-amended.2026-10-13-p170.tsv`](../evidence/region-gate-amended.2026-10-13-p170.tsv)
[`evidence/regional-sweep.2026-10-13-p170.tsv`](../evidence/regional-sweep.2026-10-13-p170.tsv)

### 🆕 🔴 The trend behind `T213` — three passes of fixing a gate that was measuring the wrong thing

🟢 **This KB has now corrected its licence gate three times, and each correction revealed that the
previous one had been right about a smaller problem than it thought:**

| pass | what was fixed | what remained broken |
|---|---|---|
| 🟡 **p168** | 🟡 **read the BODY, not the title line** | 🔴 **only the ROOT was read** |
| 🟡 **p169** | 🟡 **enumerate the TREE (step `5`), and FOLD typography (step `0`)** | 🔴 **the PREDICATE was still a filename match** |
| 🆕 🟢 **p170** | 🟢 **content-test every candidate (`P170-A` step `2`)** | 🟡 **the `129` + `193` platform bodies are counted, not yet CLASSIFIED (`ACTION JK`)** |

🔵 **The pattern is worth naming as a trend because it will recur: each instrument fix widened the
denominator and left the predicate alone, so the measurement got bigger and stayed wrong. The
direction of the error even flipped — p169's tree-wide step turned a `58%` UNDER-read on `penecho`
into a `93%` OVER-read on `OpenEduCat`.**
🟢 **What makes this publishable rather than embarrassing: both errors were caught by the same
discipline, which is to re-measure a prior pass's claim with an instrument that has the OPPOSITE
bias. `OpenEduCat`'s *"`1` grant file"* is now confirmed by a tool that wanted to find `15`.**

### 🆕 🔴 Four false positives this pass, all caught before publication

🟢 **Recorded as classes, because a class recurs and an incident does not:**

| # | class | what it looked like | what it was |
|---|---|---|---|
| 🔴 **11** | 🔴 **ORDER-DEPENDENT family match on a concatenated grant** | 🔴 ***"penecho vendors `GPL`-licensed code"*** | 🟢 **`ink-lab-LICENSE.txt` bundles `3` packages; JSZip is dual *"MIT or GPLv3"* and `MIT` is elected. Tested families in sequence and stopped at the first hit** |
| 🔴 **12** | 🔴 **a LINE-anchored grep against a line-WRAPPED phrase** | 🔴 ***"`Axonai`, `Lumo` and `WiseTutor` do NOT carry the paraphrase"*** | 🔴 **all three carry it. `(Alarm is` / `the umbrella trademark` wraps across a newline. Settled by BODY HASH instead — all three blob `ae1dbfc5e74c`** |
| 🔴 **13** | 🔴 **a join keyed on a LINE OFFSET** | 🟡 **a churn table printing `10` rows under a comment asserting *"`2` of `12`"*** | 🟢 **`NR>8` silently dropped the two rows that had changed. Caught by counting rows, not reading them (`T215`)** |
| 🔴 **14** | 🔴 **a gate whose BLOCK EXTENT runs past what it judges** | 🔴 ***"`28` region-heading defects, growing every pass"*** | 🟢 **`1` real defect. `13` *"out of vocabulary"* headings were FINDING headings; `11` *"missing regions"* were in historical blocks** |

🔵 **Classes `11` and `12` are the same shape in opposite directions — a text predicate that assumes
a structure the file does not have. Class `12` is the dangerous one: it produced a CONFIDENT NEGATIVE
that would have overturned a correct p169 finding, and only a hash disagreed with it.**
🟢 **The lesson p170 would hand forward: when a probe contradicts a prior pass, prefer an instrument
that cannot be fooled by formatting. A blob sha has no opinion about line breaks.**

### 🆕 🔴 `T217` — repetition is not corroboration

🟢 **`86` citations of `Regulation (EU) 2026/1744` across `7` files. `0` citations of
`Regulation (EU) 2024/1689` in any current content file.**
🔵 **Read as a trend rather than a slip: this KB generates each pass's prose partly from its own
previous prose, so a number that enters once is re-stated forward and accumulates the APPEARANCE of
being well-sourced. `86` occurrences look like `86` confirmations and are `1` unverified claim copied
`86` times.**
🔴 **It is also the one defect class on this page with a direct client cost: a deck citing an
instrument number that cannot be confirmed, while omitting the one every EMEA counsel knows.**
🟢 **The structural fix is not *"search harder"* — `eur-lex` is unreachable on every channel here
(`T203`, environmental, reproduced in a fresh container). It is to mark tier at the point of USE:
an unverified instrument number should not be printable without its tier beside it. `ACTION JL`.**

### 🆕 🟢 `T216` — what append-only costs, measured for the first time

🔵 **The convention exists for a good reason: it prevents a pass from quietly deleting a predecessor's
finding, and this KB's whole value rests on that.** 🔴 **Its cost, never measured until p170: if only
the newest block is canonical — which is exactly what `gap 112`'s amendment establishes — then every
row a pass does not re-state disappears from the compiled view while remaining true in the history.**
🟢 **`OpenOLAT` is the worked example: `Apache-2.0`, operative text verbatim, institutional, `QTI` and
`SCORM` built in, HEAD one day old, verified at pass `138` and re-measured to the same `10 982` bytes
at pass `170` — and absent from the permissive-LMS route for `32` passes.**
🟢 **The fix is cheap and is `P170-C`: a cross-block consistency gate that fails when a repository is
licence-verified anywhere in a file and absent from that file's newest routing table.**
🔵 **Stated as a trend because it predicts where to look next: any shelf with a ROUTING table and an
append-only history can have lost rows the same way. Pre-registered as `ACTION JM`.**

### 🆕 🟢 The external trend with real new evidence — compulsory curricula

| region | mandate | date | why it is different from a policy |
|---|---|---|---|
| 🆕 🔴 **China** | 🔴 **AI compulsory for school students from age `6`** | 🟢 **in force** | 🟢 **a national curriculum requirement creates procurement, not guidance** |
| 🆕 🟢 **India** | 🟢 **AI + computational thinking compulsory from Class `3`** | 🟢 **academic year `2026-27`** | 🟢 **DATED, inside twelve months, at national scale** |
| 🟢 **USA (Alabama)** | 🟢 **an approved CS course including AI instruction required to graduate** | 🟢 **carried from p169** | 🟢 **a graduation requirement is a hard deadline per cohort** |

🟢 **Against this, the global AI-in-education market figures remain irreconcilable and are recorded as
such: `$10.6B` (`2026`) → `$42.48B` (`2030`) from one house, `~$6B` (`2024`) → `~$32B` (`2030`) from
another, `$12.3B` for `2026` from a vendor blog. Three methodologies, no shared denominator.**
🔵 **Which is why the curriculum mandates are the better instrument: an age, a grade and an academic
year are verifiable facts about demand, and a CAGR is a model.**

### 🆕 🟢 Added to the watch list by p170

- 🔴 **Whether the `~30` repositories carrying `DeepTutor`'s non-canonical `Apache-2.0` grows.**
  🟢 **`T219` settled that it is an INSTANCE propagating by copying, not a class. The thing worth
  watching is the RATE, and whether any carrier edits the body further — a second-generation
  paraphrase would be a genuinely new defect.**
- 🟡 **Whether `Sakai`'s `129` and `Moodle`'s `193` inner grant bodies contain anything incompatible
  with their outer grant.** 🟢 **`ACTION JK`. On `penecho`'s `32`, the answer was no — every family
  was `MIT`, `Apache-2.0`, `ISC` or an unelected option. If that holds at `193`, the inner-audit
  anxiety this KB has been raising is largely procedural.**
- 🟢 **Whether `gap 113` is query exhaustion or ecosystem fact.** 🔴 **Several passes of
  *"top open source AI agents education"* have added `0` rows. A `12`-agent vertical and an exhausted
  query look identical from here and have opposite consequences for a studio deciding whether to
  BUILD an education agent rather than compose one.**

## Pass 169 — 2026-10-13

🆕 🔴 **The trend this pass can evidence is about GRANTS, not models: on a shelf of `12` agents, `2`
licence cells that had been correct for fourteen passes turn out to be incomplete the moment the bodies
are read — and in both cases the missing part is the part a client's procurement would stop on.**
🆕 🟢 **`Selleo/mentingo` shipping a `19`-identifier dependency licence gate is the first evidence this
KB holds that open-source education projects are doing licence compliance as ENGINEERING. That is a
maturity signal, and it arrived on the newest, most active row on the shelf.**
🆕 🔴 **Two of this pass's own instruments produced false positives before they produced findings
(`T204`, `T205`). Both looked like signal: a release burst and a rewritten licence. Neither existed.**

### 🆕 🔴 The trend behind `T206`, `T207` and `T212` — a licence NAME is not a licence

🟢 **Across three passes this KB has now read `26` grant bodies. The pattern is consistent enough to
state as a trend rather than a set of incidents:**

| defect class | instances | what it looks like from outside |
|---|---|---|
| 🔴 **a body that is not the licence it names** | 🔴 **`Sakai` (`ECL-2.0` as *"Apache-derived"*), `DeepTutor` (paraphrased `Apache-2.0`)** | 🟢 **a clean `Apache-2.0` badge** |
| 🔴 **a body that promises text it does not contain** | 🔴 **`OpenEduCat` (`T201`), both `Fedena` trees (`T212`)** | 🟢 **a named, familiar licence** |
| 🔴 **more than one grant surface, disagreeing or narrowing** | 🔴 **`Chamilo` (`T202`), `penecho` (`T207`)** | 🟢 **one licence cell** |
| 🔴 **no grant at all** | 🔴 **`Mr.-Ranedeer-AI-Tutor`** | 🟡 **`378` d stale, so at least the staleness shows** |

🔵 **`8` of `26` bodies read deviate from what their project is published as. That is high enough that
*"the repo says MIT"* is not diligence, and low enough that the fix is cheap — `P169-A` is six steps
plus a fold.** 🟢 **The direction of the errors is worth noting: most are HARMLESS in substance
(a paraphrase, a filled placeholder, a more permissive second file) and ALL of them are capable of
stopping an automated gate. The risk is operational, not legal.**

### 🆕 🟢 What `mentingo`'s licence gate says about where this ecosystem is going

🟢 **The file is `1 119` bytes and it is the most sophisticated compliance artifact this KB has found in
an education repository.** 🟢 **It allows `19` identifiers, names `13` package exceptions, and records
REASONING against several of them —** *"sublib of sharp - not modified - not embedded in software"*
**— including the `LGPL-3.0-or-later` sub-libraries of `sharp` that a naive gate would simply refuse.**
🟢 **Several exceptions exist because an upstream package asserts a licence on npm or in a README and
ships no `LICENSE` file — which is `T201`'s and `T212`'s defect class, caught by a working team on a
different shelf.**
🔵 **Read as a trend: the compliance burden the EU AI Act and the US state statutes are creating is
arriving in these repositories as CONFIG, checked into git. That is the shape to meet a client with —
not a PDF policy.**
🔴 **The counter-evidence in the same repo: `licenses.comment.md`, the file where the reasoning belongs,
is `0` bytes. The practice is ahead of the documentation.**

### 🆕 🟢 Added to the watch list by p169

- 🔴 **Whether `DeepTutor`'s paraphrased `Apache-2.0` appears in any OTHER repository.** 🟢 **If a
  shared upstream template or a rewriting tool produced it, `T206` is a CLASS and worth a corpus-wide
  probe; if it is unique to `HKUDS`, it is an instance and closes here.** 🟢 **Pre-registered as
  `ACTION JI`.**
- 🟡 **Whether `penecho`'s commercial path is ever actually exercised.** 🔴 **Terms are *"negotiated
  separately"* with no published price, timeline or standard agreement — so today it is an option in
  principle. 🟡 Watch for any public evidence of a granted commercial licence: that is what turns the
  only named escape hatch from `AGPL-3.0` on this shelf into something a client can plan around.**
- 🟢 **Whether `RosarioSIS` sustains its pace.** 🟢 **`GPL-2.0`, HEAD `1` day old at this pass, and the
  most active SIS this KB has verified. If it holds, it is the SIS route for copyleft-tolerant clients;
  if it stalls, the SIS layer has no live option at all.**
- 🔴 **Whether the EU's emotion-inference PROHIBITION gets tested in an education setting.** 🔴 **This
  KB has recorded many high-risk DUTIES and this is its first outright prohibition touching education.
  Watch for the first enforcement action or withdrawn feature — engagement detection and attention
  tracking are shipped in commercial proctoring today.**
- 🟡 **Whether New York City's moratorium spreads or is lifted.** 🔴 **It is the first district
  moratorium this KB holds, in the largest US district. 🟡 Watch for a second large district following,
  because that would change the North American pitch from *"teacher-facing first"* to *"teacher-facing
  only"*.**
- 🟡 **Whether `AlekSIS` can be located at all.** 🔴 **Named by this pass's sweep; `AlekSIS/AlekSIS` and
  `aleksis/AlekSIS-Core` both return `NOT FOUND` on `git ls-remote`, so it is hosted off github.com and
  therefore invisible to every channel open in this container. 🟡 Worth one probe from a container with
  wider egress — it may be the permissive SIS this shelf has been looking for.**
- 🟡 **Whether `openSIS-Classic`'s vendored `CKEditor` grants hold any surprise (`gap 112`).**


## Pass 168 — 2026-10-13

### 1. 🆕 🔴 `T198` — the probe that nearly overturned a correct finding on a base64 hash — *Global, measured*

🔴 **`ACTION IZ` re-probed `10` trees with `13` interop terms instead of `5`, to test whether
p167's published *"`10` of `15` trees have no interop standard"* was a FALSE ABSENCE.**
🟢 **It returned exactly `1` hit across `11 684` tracked files — and the hit was `\bQTI\b` matching
inside a `sha512` integrity hash in `plastic-labs/tutor-gpt`'s `pnpm-lock.yaml:1263`, because `/`
is a word boundary in base64.**

| stage | hits | what changed |
|---|---|---|
| 🔴 raw `13`-term probe | `1` | would have FIRED the falsifier and overturned a correct finding |
| 🟢 lockfiles excluded (`17` files, `8` of `10` trees) | 🟢 **`0`** | 🟢 **falsifier SILENT, `gap 106` CLOSED, p167's absence SURVIVES** |

🔵 **The lesson is not *"exclude lockfiles"*. It is that the fix was a FILE CLASS, not a pattern:
`\bqti\b` case-insensitive returns the same single hit, so tightening the regex would have changed
nothing.** 🔴 **Eighth false-positive class, one pass after `T194`, in a probe that inherited
`T194`'s control suite and still needed a ninth control.**

### 2. 🆕 🔴 `T200` — the licence whose family name hides the clause that matters — *Global, measured*

🔴 **`Sakai` is `ECL-2.0`, which this KB has published correctly since p131 and has described as
*"Apache-derived, fork freely"*.** 🟢 **p168 diffed the body against canonical `Apache-2.0`:
`+137`/`−13` words, `95.44%` word similarity, and the licence's own preamble states the derivation.**
🔴 **The inserted paragraph narrows the patent grant for contributions by *"an individual employed
by an institution or organization"* to claims that person personally invented and that their
employer had the right to license.**
🔵 **Why it is a trend and not a trivium: education's open source is written by university
employees, so an education-specific licence family exists precisely to narrow institutional patent
exposure. A permissive-licence allow-list built from `MIT`/`Apache`/`BSD` will not contain
`ECL-2.0` at all, and the gate will either refuse a safe platform or wave through a clause nobody read.**

### 3. 🆕 🔴 `T201`/`T202` — grant files that promise what they do not contain, and repos with two of them — *Global, measured*

| repo | the defect | measured |
|---|---|---|
| 🔴 `openeducat/openeducat_erp` | 🔴 the body says *"the text of the GPL is included at the bottom as well"* | 🔴 **`0` occurrences of `"GNU GENERAL PUBLIC LICENSE"`. `LGPL-3.0` is DEFINED as additional permissions over `GPL-3.0`, so the grant on disk is incomplete by its own construction** |
| 🔴 `chamilo/chamilo-lms` | 🔴 two root grant files that disagree | 🔴 **`LICENSE` is a bare `GPL-3.0` body (no election); `license.txt` elects **`-or-later`** — and both of `license.txt`'s own pointers are `404`** |

🔵 **The trend across `T200`–`T202`: the licence FAMILY is the easy question and it is the one
every tool answers. What a client actually needs — which grant, over which code, from which
surface, with which carve-out — is only in the body, and `3` of the `7` bodies read this pass do not
match what their family name implies.**

### 4. 🆕 🔴 `T203` — a verification rule that cannot be executed is a rule that is not being followed — *Global, measured*

🔴 **This KB publishes *"verify every URL before writing it (`curl -sI`)"*. p168 measured `26`
hosts and channels: `0` of the `15` non-GitHub URLs this pass would cite are reachable.**
🟢 **What IS open: `git ls-remote`, `git clone`, `raw.githubusercontent.com`, `apache.org` and the
package registries — which is why every repo, sha, licence body and source line cited this pass is
verified while every market and regulatory figure is not.**
🔴 **`github.com` HTML answers `403` on `curl` and OPENS on `WebFetch`; `github.com/search` returns
`0` results on all three channels, so repo DISCOVERY is closed and no shelf row could enter by
search this pass.**
🔵 **The useful form of this finding is a rule change, not a complaint: the bar should read *verify
on the strongest channel that is open, and record which one* — which is what the evidence files
have been doing in practice for twenty passes while the stated rule described something else.**

### 5. 🆕 🟢 APAC stops being a silence, and the two statutes name the same feature — *APAC, search-summary*

🟢 **p167 recorded `0` named APAC education vendors and `0` national education-AI policies,
explicitly so it could not be read as coverage. p168's sweep returned both.**
🟢 **Korea's AI Basic Act (in force `January 2026`) places education inside *"high-impact"* uses,
with MSIT signalling `2026` as a limited-enforcement pilot. Vietnam's Law No. `134/2025/QH15`
(`1 March 2026`) names EDUCATION among high-risk sectors and cites AUTOMATED ASSESSMENT and
BEHAVIOURAL MONITORING as the examples.**
🔵 **The convergence is the trend: automated assessment is simultaneously the most-requested
feature and the named high-risk trigger in APAC statute, EU Annex III, and the US state bills
(Oklahoma and Maryland barring AI from high-stakes student decisions). Three regions, three legal
traditions, one feature.** 🟢 **Which means the architecture that satisfies one satisfies all
three — human decision point, evidence trail, data boundary — and it is the same posture
`P167-B`'s read-only rostering already takes.**
🟡 **ANZ is the exception inside its own region: support for BANNING AI in schools is higher there
than across Asian markets, so scope it with EMEA-style transparency expectations.**

### 6. 🆕 🟢 LATAM's `61`-point gap between using AI and governing it — *LATAM, search-summary*

🟢 **UNESCO IESALC, `200` institutions across `19` countries: `87%` use AI in at least one area,
`74%` in teaching and learning, `26%` have a formal AI strategy.** 🟢 **Private non-profit
institutions lead implementation at `84%`, public `68%`, private for-profit `52%`.**
🟢 **`PUC Chile` is the named deployment: `194` pedagogical agents, `~100` courses, `4 600+`
students, `February 2026` — instructor-configured, grounded in course content, learning outcomes
not yet measured.**
🔵 **The trend is the ORDER of adoption: LATAM institutions deployed first and are governing second,
which is the reverse of EMEA's regulation-led sequence. It makes the sellable first engagement
governance rather than build — and it makes measurement the second one, because the region's
flagship deployment cannot yet say whether it worked.**
🔴 **And no regulator is forcing it: `gap 104` holds for a third pass. The work will be bought on
assessment integrity and teacher workload, not on a compliance date.**

### 7. 🆕 🔴 The first negative efficacy datum this shelf has held — *Global, search-summary*

🔴 **AI tutor learning gains reported at *"approximately half the effect size of high-quality human
tutoring"*, with engagement dropping significantly without teacher reinforcement — attributed to
EdSurge Research (`2025`), a source not seen on any channel.**
🔵 **Held deliberately: eighteen passes of market material have been uniformly pro-adoption, and a
shelf that only carries the bull case is marketing. Quote it to a client as a design constraint —
the teacher stays in the loop — not as a finding.**

### 8. 🆕 🔴 `T199` — twelve passes of web sweep added no agent row because the QUERY collides — *Global, measured*

🟢 **`5` repos named by this pass's *"open source AI agents education"* sweep. All `5` exist on the
git channel, all `5` are `MIT`, `0` are education-sector agents: `4` are AI-literacy courseware and
`1` is a general-purpose agent.**
🔵 **The phrase reads both ways and the web answers the wrong one — education ABOUT AI, not AI FOR
education. That is a QUERY defect, and it explains a pattern this KB has recorded as a market
absence for twelve passes.**
🟢 **The salvage is real: three `MIT` AI-literacy curricula, one of them shipping `53` locales
including `es`, `pt-BR` and `23` APAC languages — which is a COURSEWARE tier this shelf did not
have, arriving exactly as `H.R. 8747` proposes to fund AI literacy in US schools.**

## Pass 167 — 2026-10-13

### 1. 🆕 🔴 `T194` — the instrument that catches naming collisions reproduced the collision it was built to catch — *Global, measured*

🔴 **`P166-A` added a comment-stripping guard to find anti-claims. p167 ran it across `15` trees and
`7 723` capability-term occurrences, and found THREE defects in the guard — one of them the exact
error class the whole census method exists to correct.**

| defect | mechanism | population before → after |
|---|---|---|
| 🔴 **marker collision** | `/*` in a template literal, `//` in `https://`, `#` in `#fff` | `1 140` → `934` *(`18.1%` killed)* |
| 🔴 **unterminated span** | `<code>/*</code>` opens a block comment that never closes; the span runs to EOF and every later hit in the file is misread as a comment | `934` → `925` |
| 🔴 **missing trailing `\b`** | `para` matched *"**para**llel"*, `sin` matched *"**sin**ce"* | `176` → `3` *(`98.3%` killed)* |

🔵 **`P164-A` exists because a naive `lti` grep matched `facu`+`lti`+`es`. Two passes later the
instrument written to extend it omitted the trailing boundary on its own word list.**
🟢 **The trend worth recording at `167` passes: an instrument's error classes recur in the
instrument's own successors, so every new probe gets the OLD probe's control suite — not just a
fresh one.** 🟢 **The control that makes the correction publishable: `T187`'s anti-claim survives
all three fixes unchanged.**

### 2. 🆕 🟢 `T195` — a licence FAMILY is not a licence, and two bodies on this shelf prove it — *Global, measured*

🟢 **`14` licence bodies read byte for byte. `2` carry appended text their family name does not
predict.** 🔴 **`openedx/edx-platform`'s AGPL-3.0 body ends with an EdX Inc. clause declaring that
a public, independently available web service communicating with its code over RPC is NOT a
derivative work, and that Corresponding Source excludes that service's source files.**
🟡 **`openolat/OpenOLAT`'s Apache-2.0 body carries two attribution statements — no grant change, but
`809 B` of why its body is not the canonical one.**
🔵 **The industry consequence: licence-family metadata, which is what every SBOM and every GitHub
API field gives you, is insufficient for an architecture decision. `P167-C`'s rows are TERMS.**

### 3. 🆕 🔴 `T191` — *"xAPI-inspired"* is a feature-list claim with no integration behind it — *Global, measured*

🔴 **`zijinz456/OpenTutor` names `xapi` exactly twice, both in comments, both reading
`xAPI-inspired`, with `0` code hits.** 🟢 **Its event emitter is first-party with its own verb list.**
🔵 **The analogy claim — `-inspired`, `-like`, `-style`, `-compatible` — is the seventh
false-positive class on this shelf, and it is the one most likely to reach a client's requirements
document intact, because it reads as a standard rather than as a resemblance.**
🟢 **Counter-example from the same sweep: `OneRoster-style` in `edfi-oneroster`'s `docs/PRD.md`,
where the capability IS real — so the marker triggers a code probe and never a verdict.**

### 4. 🟢 `T186` CONFIRMED on a second independent sample — the web channel keeps saturating — *Global, measured*

🟢 **p167 ran the full eight-query sweep again, globally and once per region, and measured the
re-derivation rate on both channels before publishing anything:**

| channel | terms probed | already on the shelf | re-derivation | p166 |
|---|---|---|---|---|
| 🔴 **web / search** | `18` | `15` | 🔴 **`83%`** | 🔴 `91%` |
| 🟢 **code / git** | `10` | `2` | 🟢 **`20%`** | 🟢 `81%` |

🔵 **Two passes, same direction, and p167's code channel is sharper still: `8` of `10` code-channel
terms were new to this KB, against `3` of `18` on the web.** 🟢 **Every substantive p167 finding —
the three guard defects, the second anti-claim, the `24` endpoints, the RPC carve-out, the band
collapse — came from a tree.** 🔴 **The `3` genuinely new web terms were the EU `Apply AI Strategy`,
`GDPR-K` as a compliance label in European children's edtech, and the Finnish vendor `Seppo`.**

### 5. 🆕 🔴 `T196` — the churn ledger is internally inconsistent, and the repo's OWN git log is what catches it — *Global, measured*

🟢 **`ACTION IT` required diffing against `evidence/churn-baseline.2026-10-13-p166.tsv`. Its sha
columns are sound. Its INTERVAL LEDGER is not, and the falsifying channel is this repository's own
commit history, which no earlier pass had thought to use as a clock.**

| ledger claim | what the commit channel says | verdict |
|---|---|---|
| 🟡 *"`p165_sweep` → `p166_t0` = `31` min"* | 🟡 **places p165's sweep at `04:15:17Z`, `7` seconds AFTER p165's own commit (`04:15:10Z`)** | 🟡 **rounded — a sweep cannot post-date the commit that carries it, but `7` s is within rounding** |
| 🔴 *"`p164_sweep` → `p165_sweep` = `37` min"* | 🔴 **places p164's sweep at `03:38:17Z` — `27` min `30` s AFTER p164's commit at `03:10:47Z`** | 🔴 **IMPOSSIBLE** |
| — | 🟢 **`p164` commit → `p165` commit = `1 h 04 min`** | 🟢 **the defensible figure** |

🟢 **Calibration that makes the commit channel usable as a clock: p166's own closing sweep
(`05:07:50Z`) precedes its commit (`05:10:23Z`) by `2 min 33 s`. So a sweep sits a couple of minutes
BEFORE its pass's commit, and a commit timestamp is a safe UPPER bound on the sweep time.**

🔴 **Consequence for `T173`, whose claim was *"`1` of `12` per `37` minutes"*: the denominator is
unsupported. On the commit channel the interval in which `ai-shifu` moved is `~64` minutes, so the
rate was overstated by `~1.7×` even as a single repository's cadence.**
🟢 **p166 had already narrowed `T173` from a shelf-wide rate to one repository sampled once; p167
corrects its denominator as well, and `T173` should not be cited as a rate in any form.**
🔵 **The method lesson: a relative-minute ledger is a derived instrument, and this KB had no
independent clock until it noticed it was sitting inside one. Every pass commits with a UTC
timestamp — that is a primary channel, and it is free.**

### 6. 🔴 The market, EIGHTEENTH pass — still unverifiable at source, cause unchanged — *Global, search-summary*

🔴 **The same sweep returned AI-in-education forecasts of `$6.4B`→`$79.6B` (`31.35%` CAGR),
`$8.3B`→`$57.2B`, and `$10.6B` at `40.9%` CAGR — for overlapping definitions of the same market.**
🟢 **`T168`'s named cause is unchanged and now eighteen passes old: the high estimates bundle
corporate L&D with K-12 and higher education.** 🔵 **This page's policy stands — regional figures are
recorded with their channel and never promoted to measurements (`T160`).**


## Pass 166 — 2026-10-13

### 1. 🆕 🔴 `T186` — the search channel has saturated on this shelf, and it is measurable — *Global, measured*

🔴 **p166 ran the full eight-query sweep, globally and once per region, and `10` of the `11` terms it
surfaced were already on the shelf — a `91%` re-derivation rate.** 🟢 **The code channel, over the
same pass, re-derived `13` of `16` but produced `3` new measurements and `1` correction to a
published claim.**

| channel | re-derivation | new | what it produced at p166 |
|---|---|---|---|
| 🔴 **web / search** | 🔴 **`91%`** | `1` | 🟡 **the EU `Apply AI Alliance`, and nothing else** |
| 🟢 **code / git** | 🟢 **`81%`** | `3` | 🟢 **`T179`–`T184`: the census, the unusable sibling, the shelf correction, the permissive OneRoster path, `gap 79`, three licence bands** |

🔵 **This is a trend about the instrument, which at `166` passes is the trend that matters: a shelf
this deep stops learning from the channel that any competitor also reads, and keeps learning from
the one that requires a clone.** 🟢 **`T175` said *grep the shelf before measuring*; `T186` says
*and when you do, expect the web to tell you nothing*.**

### 2. 🆕 🔴 `T187` — the ANTI-CLAIM: a capability hit can be upstream telling you NO — *Global, measured*

🔴 **`Selleo/mentingo` returns exactly `1` hit for `xapi` and exactly `1` for `lti` across `4 753`
tracked paths. Both are the SAME line — `README.md:246` — inside an HTML comment, in Polish,
reading *"STAGE 3 — to be confirmed by the team, DO NOT PUBLISH WITHOUT VERIFICATION: … pentest,
xAPI/LTI, mapping to NIS-2 / art. 8e KSC, retention and data deletion."***

🟢 **Three things follow, and the third is the trend:**
1. 🟢 **The verdict is ABSENT, and it is now the strongest kind of absent — upstream has not
   claimed the capability and has explicitly marked it unverified.**
2. 🟢 **mentingo's real published interop claim is one accurate English sentence: *"SCORM 1.2
   export."*** 🔵 **Upstream is being MORE careful than the ecosystem that summarises it.**
3. 🆕 🔴 **A capability census must strip comments before counting a documentation hit.** 🔴 **This
   is a sixth false-positive class and no boundary, binary or i18n guard touches it, because the
   text is prose and it is in the repository deliberately.**

🔵 **Why it generalises: the GitHub topic list, the vendor page and the README body are all channels
this shelf already distrusts. The commented-out roadmap is a FOURTH documentation channel, it reads
as a feature list to any grep, and it means the opposite.**

### 3. 🆕 🔴 `T180` — the maintenance-first filter and the sibling probe pull in OPPOSITE directions — *Global, measured*

🟢 **`P165-A` added the sibling probe to catch false absences, and it works: Moodle's OneRoster goes
`ABSENT` → `IMPLEMENTED-IN-SIBLING` on one `ls-remote`.**
🔴 **But the sibling it finds — `moodlehq/moodle-enrol_oneroster` — is `GPL-3.0` and `2 091` days
stale, `11.6×` `P164-D`'s drop threshold.**

🔵 **So the two guards this shelf added in consecutive passes systematically disagree, and the
disagreement is the useful signal: the FN guard says *the capability exists*, the maintenance filter
says *you cannot depend on it*. Both are true.** 🟢 **A census that reports only the first has
handed the client a worse answer than one that reported a flat absence, because they will budget
for an integration instead of a build.** 🟢 **`P166-A` STEP 7 makes running `P164-D` on every named
sibling non-negotiable.**

### 4. 🆕 🔴 `T184` — three published licence size bands were wrong, and correcting them made the test WORSE — *Global, measured*

🔴 **Apache-2.0 is BIMODAL. Bodies carrying the *"APPENDIX: How to apply the Apache License"*
section run ~`11.3`–`11.4 KB`; bodies ending at *"END OF TERMS AND CONDITIONS"* run ~`10.2 KB`.
`Ed-Fi-Alliance-OSS/edfi-oneroster` is the latter at `10 173 B`, with `0` occurrences of
`APPENDIX`.** 🔴 **GPL-3.0's observed value, `35 149 B`, sits `2 B` outside the published band and
has now reproduced on two unrelated repositories a pass apart.** 🔴 **And the published
*"GPL-3.0 vs AGPL-3.0, `11 B` apart"* adjacency is not reproduced by the bodies this shelf has
actually read — observed GPL clusters at `35 149` and AGPL at `34 522`–`34 523`, about `626 B`
apart.**
🟢 **Every correction WIDENS a band or breaks an adjacency, so each one makes the size heuristic
less usable and `P48`'s thesis — classify by the NAME LINE — stronger.**
🔵 **The trend: on a shelf that body-reads licences for `166` passes, the published summary
statistics drift away from the evidence unless something re-derives them. `T184` is the second
pass in a row where a reproducibility check paid for itself.**

### 5. 🟡 `T178` UNRESOLVED for a second pass — the Annex III date still has two incompatible stories — *EMEA, search-summary*

| p165's reading | p166's sweep |
|---|---|
| 🟡 **`Regulation (EU) 2026/1744`, published `2026-07-24`, in force `2026-07-27`** | 🟡 **Council gave final green light to the Digital Omnibus, but the act *"awaits publication in the Official Journal"*** |

🔴 **Both cannot be current.** 🟢 **`T178` is NOT promoted and stays `search-summary`.**
🟢 **What is NOT in dispute, and is what an engagement should be priced against: the AI Office and
national authorities began enforcing from `2026-08-02`; education is high-risk where it determines
access to education or the course of a professional life, with exam scoring the Commission's own
example; and the emotion-recognition ban in education is live on every reading.**
🔵 **`T167`'s infrastructure explanation still holds — this shelf's document channel is secondary
by construction, so an EU legal-publication question is exactly the kind it cannot close.**

### 6. 🟢 `T188` — the secondary channel disagrees with the git primary again, on a field where the primary EXISTS — *Global, measured*

🔴 **A p166 search summary reports `HKUDS/DeepTutor` as *"last updated Oct 12, 2026"*.** 🟢 **The
git channel says HEAD `6cf793bd868b`, commit date `2026-10-08`, and the sha has not moved across
p165's two sweeps and p166's.**
🟢 **`T160`'s promotion rule resolves it without argument: a secondary claim is promotable only when
a git-channel primary exists for the same field — and here one does, so the primary wins and
`2026-10-08` stands.**
🔴 **The same summary reports `DeepTutor` at *"~41.2k stars"*. No git-channel primary exists for
stars, so it is NOT published — `T149` keeps the `★` column closed.**
🔵 **Two claims from one source, one resolvable and one not, by a rule written three passes ago.
That is the register doing its job.**

## Pass 165 — 2026-10-13

### 1. 🆕 🟢 `T177` — an exemption and a safe harbour are different things, and p164's Colorado lead had them confused — *North America, search-summary*

🔴 **p164's open-gaps carried a tracker claim that Colorado had repealed its AI Act and
*"carved out FERPA-covered institutions — i.e. education EXEMPTED"*.** 🟢 **The repeal is real.
The exemption is not.**

| p164's lead | what this pass's sources say |
|---|---|
| 🟢 *"repealed"* | 🟢 **CORRECT — `SB 26-189`, signed `2026-05-14`, repeals AND REPLACES the 2024 Colorado AI Act; effective `2027-01-01`** |
| 🔴 *"education exempted"* | 🔴 **REFUTED. Education stays in scope — the law reaches decisions affecting *educational enrollment or opportunity*, and sources state there is NO exemption for public or nonprofit educational institutions** |
| — | 🟢 **What exists is a DEEMED-COMPLIANCE SAFE HARBOUR: FERPA-compliant notices are deemed to satisfy the notice duty; an existing FERPA-compliant correction and human-review process is deemed to satisfy human review** |

🆕 **`T177`:** 🔵 **the distinction IS the engagement.** 🔴 **An exemption means no work. A safe
harbour means the institution must POSSESS a FERPA-aligned notice, a documented
correction-and-human-review process, and evidence of both — and must be able to show them.**
🟢 **That is three concrete artefacts against a `2027-01-01` date, and `P160-B`, `P161-A`,
`P163-C` and `P165-B` already build them.**
🟡 **The replacement is otherwise LIGHTER than the 2024 Act: it reframes around *"automated
decision-making technology"* and drops the impact-assessment and risk-management-framework duties.**
🔵 **Generalisable beyond Colorado: when a tracker says *"carve-out"*, establish whether it is an
EXCLUSION or a SAFE HARBOUR before scoping anything. They point in opposite commercial directions.**

### 2. 🆕 🟢 `T178` — the Annex III deadline now has a named instrument — *EMEA, search-summary, UNVERIFIED at source*

🟢 **A real advance on p164, which carried the claim with no instrument attached.**
🟡 **Reported consistently across several independent law-firm and compliance analyses: the
Digital Omnibus was adopted as `Regulation (EU) 2026/1744`, published `2026-07-24`, in force
`2026-07-27`, moving the Annex III STANDALONE high-risk obligations from `2026-08-02` to
`2027-12-02`.**

| moved | did NOT move |
|---|---|
| 🟡 Annex III standalone high-risk obligations → **`2027-12-02`** | 🟢 **Article 50 transparency — unchanged, original schedule** |
| 🟡 machine-readable marking for existing generative systems → `2026-12-02` *(grace period)* | 🟢 **the emotion-recognition ban in education — in force since `2025-02-02`, reported unaffected. LIVE TODAY** |

🔴 **One source still describes the Omnibus as a Commission PROPOSAL in negotiation rather than
adopted law.** 🔵 **That disagreement keeps the cluster a strong LEAD rather than a finding, even
though most sources now agree.**
🔴 **Not one character was read at source, consistent with every prior pass.** 🟢 **So the shelf's
position is: carry the named instrument, carry the date, label it `search-summary`, and tell the
client to verify `Regulation (EU) 2026/1744` against the published text with their counsel.**
🔵 **Education remains in Annex III point 3 — admission and access, assignment to institutions,
evaluation of learning outcomes where those outcomes steer the learning, level assessment, and
monitoring for prohibited behaviour during tests.**

🟢 **What does not depend on the date, and it is most of this shelf's value:** 🟢 **every code
finding is a fact about a repository. `T161`, `T170`, `T171`, `T172` and OpenOLAT's
`o_ai_essay_correction` provenance schema hold whatever the deadline turns out to be.**
🔵 **A delay is a budget for doing it properly, not a reason to stop.**

### 3. 🆕 🔴 `T175` — the trend inside this KB: at `165` passes, re-discovery is a real cost

🔵 **Not an education trend, but the one this pass can state from its own evidence.**
🔴 **Six of p165's would-be findings were already on the shelf — `P411` (`PageLM`'s non-commercial
licence, same `8 563 B`), the licence-byte instrument, `P158-B`'s `9`-path licence probe,
`Mr.-Ranedeer`'s unlicensed status, and `T142`'s plugin finding.** 🔴 **A seventh conclusion
contradicted a better-evidenced prior finding and was dropped before publication.**
🆕 **`T175`:** 🟢 **a knowledge base deep enough to be valuable is deep enough to be re-derived
from, and the defence is procedural: grep the shelf for every term in the question before
measuring. It is now step 0 of `P165-A`.**
🔵 **Worth carrying to the other industry shelves, because they are younger and will hit this at
the same depth.**

### 4. 🟡 The second-hand trends, carried with their labels — *Global*

🟡 **Workflow-first deployment over broad personalisation claims; institutions reported to favour
tools showing instructional value, ethics and transparency, with the clearest gains in course
design support and teacher productivity (HolonIQ).** 🟡 **Movement away from generic chatbots
toward platforms built around curriculum and learning objectives.** 🟡 **Agentic task execution —
planning a teaching sequence, drafting an assessment — named as the 2026 shift (Educativa).**
🟡 **Career-navigation and credentialing tools spreading across K-12, post-secondary and workforce
contexts.** 🟡 **Adoption: `54%` of K-12 students and `92%` of university students reported using
AI; `60%` of US K-12 teachers used AI tools in 2024-2025, `32%` at least weekly; most education
organisations reported to lack a policy despite widespread generative-AI use.**
🔴 **All `search-summary`, none read at source. The `83%` / `42%`-style figures from vendor blogs
are deliberately NOT carried.**

## Pass 164 — 2026-10-13

### 1. 🆕 🔴 The deadline this shelf has been planning against MOVED — Annex III education obligations now apply from 2 December 2027 — *EMEA, search-summary, UNVERIFIED at source*

🔵 **If this is right, it is the most consequential fact on this page, because four passes of
findings have been framed as *"an Annex III decision"* with an implied 2026 horizon.**
[`evidence/regional-sweep.2026-10-13-p164.tsv`](../evidence/regional-sweep.2026-10-13-p164.tsv)

🟡 **What the named-instrument query returned:** 🔴 **the EU *Digital Omnibus*, reported in force
since `2026-07-27`, DELAYS the standalone Annex III high-risk obligations to `2027-12-02`.**
🟡 **Education sits in Annex III point 3 — admission and access, assignment to institutions,
evaluating learning outcomes where those outcomes steer the learning, level assessment, and
monitoring for prohibited behaviour during tests.**

🔴 **Stated with the label it has earned and no more:** 🔴 **`eur-lex.europa.eu`,
`digital-strategy.ec.europa.eu` and `artificialintelligenceact.eu` ALL refused at the proxy
(`000`, connect rejected), so not one character of this was read at source.**
[`evidence/proxy-refusal.2026-10-13-p164.tsv`](../evidence/proxy-refusal.2026-10-13-p164.tsv)
🟡 **Sources also disagree among themselves on a neighbouring date — GenAI transparency is given
as `2026-11-02` by one and `2026-12-02` by another.** 🔵 **That internal disagreement is a reason
to treat the whole cluster as a LEAD, not a finding.**

🆕 **`T163`:** 🟡 **the regulatory premise under four passes of this shelf's work may have moved
by sixteen months, and this session structurally cannot confirm it.** 🟢 **Registered as
`ACTION IM`, and flagged here because a client would rather hear *"verify this date with
counsel"* than inherit a silent assumption.**

🟢 **Two things do NOT change, and they are what keeps the shelf's work valid either way:**

| unaffected | why |
|---|---|
| 🟢 **The emotion-recognition ban in education** | 🟢 **In force since `2025-02-02` and reported NOT affected by the Omnibus. It is live today** |
| 🟢 **Every code finding on this shelf** | 🔵 **`T156`, `T157`, `T161` and the provenance results below are facts about repositories. A deadline moving changes WHEN they must be fixed, never WHETHER they are true** |

🔵 **The honest engagement line: a delay is a budget for doing it properly, not a reason to stop.
Article 27(1)'s fundamental-rights impact assessment for public bodies — which covers public
schools and universities — is exactly the kind of artifact that is cheap to build alongside a
deployment and expensive to retrofit.**

### 2. 🆕 🔴 `ACTION IK` REFUTED — remote-first prompt resolution is NOT industry-wide, and the real axis is wider and worse — *Global, measured in code*

[`evidence/prompt-provenance-reach.2026-10-13-p164.tsv`](../evidence/prompt-provenance-reach.2026-10-13-p164.tsv)

🔴 **p163's `T156` found `Selleo/mentingo` fetching its AI judge's system prompt from Langfuse
with the repository template as a silent fallback, and claimed the pattern was *"the DEFAULT
integration shape"* industry-wide.** 🟢 **`ACTION IK` was registered to test that, with the
falsifier: *refuted if mentingo is the only one.* 🔴 **Mentingo is the only one.**

| platform | remote prompt service? | evidence |
|---|---|---|
| 🔴 [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🔴 **YES** | `@langfuse/client 5.10.1` in `apps/api/package.json` |
| 🟢 [`openolat/OpenOLAT`](https://github.com/openolat/OpenOLAT) | 🟢 **NO** | `0` hits for langfuse/langsmith/promptlayer/helicone/humanloop/braintrust/portkey across the AI subsystem; its only HTTP clients are LangChain4j provider calls |
| 🟢 [`moodle/moodle`](https://github.com/moodle/moodle) | 🟢 **NO** | `0` such dependencies in `public/ai` |
| 🟢 [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🟢 **n/a** | `0` AI prompt files in `9 276` paths |
| 🟢 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **n/a** | `0` files matching `openai\|anthropic\|llm\|langchain\|gpt-` in `1 345` paths |

🟢 **`T156` keeps its finding and LOSES its reach. `P163-B`'s industry-wide framing is
WITHDRAWN**, exactly as the registration required.

🆕 **And the measurement found the better question.** 🔵 **"Is the prompt fetched remotely?" was
the wrong axis; "is the prompt that actually ran the one in version control, and can you prove
which one it was?" is the right one.** 🔴 **On that axis the picture is worse, not better:**

| platform | where the EFFECTIVE prompt comes from | in version control? | provenance pinned to the result? |
|---|---|---|---|
| 🟢 **OpenOLAT** | 🟢 a code constant — `PROMPT_TEMPLATE_VERSION = "essay-grading-v1"` | 🟢 **YES** | 🟢 **YES** |
| 🔴 **Moodle** | 🔴 **admin-set `actionconfig` JSON on `ai_providers`**; the repo lang string is only the DEFAULT | 🔴 **NO, once an admin edits it** | 🔴 **NO** |
| 🔴 **mentingo** | 🔴 Langfuse, repo YAML as silent fallback | 🔴 **NO** | 🔴 **NO** |

🆕 **`T164`:** 🔴 **`2` of the `3` AI-bearing platforms run an effective evaluative prompt that is
NOT the one in their repository — one remote, one in a database — and only `1` of `3` records
which prompt produced a given result.** 🔵 **Moodle's case is the quieter and more common one:
no exotic SDK, just an admin textarea that silently overrides a versioned default.**

### 3. 🆕 🟢 `T165` — the fix for all of it already SHIPS, in Apache-2.0, and this shelf had not noticed — *Global, measured in code*

🟢 **`P163-B` designed a provenance-pinning pattern. `ACTION IK`'s sweep found it already
implemented upstream, in the one platform on this shelf with a permissive licence.**

🟢 **`openolat/OpenOLAT` at `e4be14f0`, `EssayAiCorrection.java:120-127`, JPA entity
`@Table(name = "o_ai_essay_correction")` — one row per graded correction:**

| column | what it pins |
|---|---|
| 🟢 `a_prompt_template_version` *(40)* | 🟢 **WHICH prompt template graded this answer** |
| 🟢 `a_content_hash_at_call` *(64)* | 🟢 **WHICH rubric/config content it was graded against** |
| 🟢 `a_tier` | 🟢 the length tier the answer was classified into |
| 🟢 `a_student_answer` *(`@Lob`, `updatable = false`)* | 🟢 **the answer itself, immutable after insert** |

🟢 **And the design is deliberate, not accidental.** 🔵 **The code comment says these fields
*"used to live on `o_ai_usage_log`"* and were moved because *"they belong to the correction,
which is the context of the AI call"* — 🟢 **a team that moved audit fields from a cost ledger
onto the graded artifact has understood the obligation, not just the feature.**

🆕 **`T165`:** 🟢 **the Article 12 / Article 14 record-keeping artifact for AI grading exists, in
production, under Apache-2.0, with a patent grant.** 🔴 **Moodle and mentingo each lack it.**
🔵 **That converts `P163-B` from a pattern this shelf invented into a PORT of a shipped
reference implementation — a different and much easier sell.**

### 4. 🆕 🟢 `T166` — an equity fix can be proved not to cost its control, by construction rather than by luck — *Global, strongest in APAC and EMEA, measured*

🟢 **`ACTION IL` applied `P163-A`'s steps 2 and 3 to the p163 replication.**
[`compose/code/p164-equity-fix-controls/`](../compose/code/p164-equity-fix-controls/README.md)

🟢 **Result: the letter-ratio margin spread across ten content-matched answers in nine scripts
collapses from `5.2×` to `1.1×`, and BOTH negative controls still reject.**

| row | ratio before | ratio after | margin before | margin after |
|---|---|---|---|---|
| 🔴 **vocalised Arabic** | `0.552` | 🟢 **`0.990`** | 🔴 **`0.102`** | 🟢 **`0.540`** |
| 🔴 **Hindi** | `0.591` | 🟢 **`0.983`** | 🔴 **`0.141`** | 🟢 **`0.533`** |
| 🟡 **Thai** | `0.815` | 🟢 **`1.000`** | `0.365` | 🟢 **`0.550`** |
| 🔴 **astral Han** | `0.500` | 🟢 **`1.000`** | 🔴 **`0.050`** | 🟢 **`0.550`** |
| 🟢 **symbol spam** *(control)* | `0.000` | 🟢 **`0.000`** | — | 🟢 **still REJECTED** |
| 🟢 **keyboard mash** *(control)* | `1.000` | `1.000` | — | 🟢 **still REJECTED (entropy)** |

🆕 **`T166`:** 🟢 **the controls are untouchable BY CONSTRUCTION, which is stronger than
"measured and happened to pass".** 🟢 **Symbol spam is digits and punctuation — neither `L*` nor
`Mn`/`Mc` — so widening the predicate adds exactly zero to its numerator. Keyboard mash already
scored `1.000` on the ratio and was rejected by ENTROPY, so a ratio change cannot move a verdict
the ratio was not making.**

🟢 **And p163's three numeric predictions — `~0.99`, `~0.98`, `1.000` — are confirmed at
`0.990`, `0.983` and `1.000`.** 🔵 **The first quantitative prediction this shelf has made in one
pass and confirmed in the next.**

### 5. 🟢 Carried, with their corroboration count

- 🔴 **`T110` — global agent discovery returns AI curriculum, not education agents.** 🔴 **EIGHTH
  corroboration.** 🔵 **At eight passes this stops being a limitation of the query and becomes a
  finding about the field.**
- 🔴 **`T134` / `T158` — no regional figure verifiable at source.** 🔴 **SIXTH pass.** 🟢 **Now
  measured as a clean asymmetry rather than a blanket failure: `4 of 4` document hosts refused,
  `2 of 2` git hosts answered.** 🆕 **`T167`: this shelf's CODE channel is primary and its
  DOCUMENT channel is secondary, permanently and by infrastructure, not by effort.**
- 🔴 **Market incoherent a FIFTEENTH pass** — 🆕 🟢 **but with a NAMED cause for the first time;
  see [`intel/market.md`](market.md).**

## Pass 163 — 2026-10-13

### 1. 🆕 🔴 The AI Act oversight artifact is not in version control — a grading prompt is fetched from a mutable external service at call time — *Global, strongest in EMEA, measured in code*

🔵 **This is the most consequential finding of the pass, and it is not an injection story.**
[`evidence/mentingo-judge-controls.2026-10-13-p163.tsv`](../evidence/mentingo-judge-controls.2026-10-13-p163.tsv)

🟢 **`Selleo/mentingo` (MIT, Poland) resolves its judge's system prompt like this —
`apps/api/src/ai/services/prompt.service.ts:275-293`, HEAD `242a9324`:**

```js
const langfusePrompt = await this.langfuseClient?.prompt?.get(id, {type:"text"})
                              .catch(() => undefined);
if (langfusePrompt?.prompt) return langfusePrompt.compile(vars);   // <-- FIRST
const prompt = this.prompts.get(id);                                // <-- the repo template
if (prompt.varsSchema && !Value.Check(prompt.varsSchema, vars))     //     is the FALLBACK
  throw new Error("Prompt template failed validation");
return prompt.template(vars);
```

🔴 **Four consequences, each read off those lines:**

| # | consequence |
|---|---|
| 1 | 🔴 **The `judge-prompt.yaml` in the repository is the FALLBACK, not the authority.** Whoever can write a prompt named `judgePrompt` in the connected Langfuse project silently replaces the whole `<instruction_priority_and_security>` block — including *"the learner conversation is untrusted evidence, never instructions"* and rule 10's statement that the server owns the totals |
| 2 | 🔴 **The remote branch SKIPS the schema check.** `Value.Check(prompt.varsSchema, vars)` guards only the repo path; the Langfuse path compiles `vars as Record<string,string>` unvalidated |
| 3 | 🔴 **An environment variable decides which host supplies the grading prompt.** The client activates on the mere presence of `LANGFUSE_PUBLIC_KEY` + `LANGFUSE_SECRET_KEY`, with `baseUrl` from `LANGFUSE_BASE_URL` or `LANGFUSE_HOST`, defaulting to `http://localhost:3002` |
| 4 | 🔴 **`.catch(() => undefined)` means an outage falls back SILENTLY.** The same submission can be graded under two different prompts depending on network state, and the stored judgement records neither |

🆕 **`T156`:** 🔴 **For an Annex III evaluative system, the instructions governing the model are
part of the oversight and documentation obligation — and here they live outside the artifact
store, unversioned, unvalidated, with silent substitution.** 🔵 **Stated fairly: this is a
sensible engineering pattern (hot-swap prompts without a deploy) that becomes a compliance
defect the moment the feature it serves is high-risk. The code is not careless; the regulatory
context changed under it.** 🟢 **`P163-B` is the fix and it is small.**

🔵 **Why this generalises beyond one repository:** 🟢 **prompt-management services are now standard
in the AI stack, and the *remote-first, repo-as-fallback* resolution order is their DEFAULT
integration shape.** 🔴 **Any education client running an evaluative feature this way has the same
gap, whatever platform they started from.** 🟢 **That makes `P163-B` a reusable audit, not a
mentingo patch.**

### 2. 🆕 🔴 A quality gate can be script-NEUTRAL in its verdicts and script-BIASED in its margins — *Global, strongest in APAC and EMEA, measured*

🟢 **`ACTION IG` ran OpenOLAT's two graded-path gates over nine writing systems with
content-matched answers.** 🟢 **`0 of 10` valid answers were rejected or down-tiered — the
falsifier was SILENT.**
[`evidence/script-equity-gate.2026-10-13-p163.tsv`](../evidence/script-equity-gate.2026-10-13-p163.tsv)
[`compose/code/p163-script-equity-gate/`](../compose/code/p163-script-equity-gate/README.md)

🔴 **And yet the tolerance is not remotely equal.** 🟢 **The letter-ratio floor is `0.45`:**

| script | ratio | **margin above the floor** |
|---|---|---|
| 🟢 English / German / Spanish | `0.976`–`0.977` | 🟢 **`0.526`** |
| 🟢 Arabic, unvocalised | `0.980` | 🟢 `0.530` |
| 🟢 Chinese / Japanese / Korean | `0.935`–`0.953` | 🟢 `0.485`–`0.503` |
| 🟡 Thai | `0.815` | 🟡 `0.365` |
| 🔴 **Hindi (Devanagari)** | **`0.591`** | 🔴 **`0.141` — `0.27×` English** |
| 🔴 **Arabic, vocalised** | **`0.552`** | 🔴 **`0.102` — `0.19×` English** |

🟢 **The cause is one line: `Character.isLetter()` is false for `Mn`/`Mc`, the combining marks
that carry Devanagari vowels and Arabic harakat.** 🟢 **Whitespace is stripped first, so
`ratio = 1 − m` and a rejection needs mark density `m > 0.55`. Measured empirically:**
🟢 **one mark per letter never rejects (floor `0.495`)**; 🔴 **two marks per letter always does
(`0.398` and below)** — 🔵 **and shadda-plus-vowel is two marks on one letter in ordinary Arabic
orthography.**

🆕 **`T151`** — 🔴 **equal verdicts, unequal margins: the gate that passes every script today has
`5×` less tolerance for Devanagari and `10×` less for astral Han than for English.**
🆕 **`T152`** — 🟢 **the breaking density is MEASURED, not projected.**

🔵 **Why this is a trend and not a bug report:** 🟢 **entropy-and-ratio pre-filters are the cheap,
obvious way to avoid paying for an LLM call on junk, and they are proliferating in front of every
graded AI feature.** 🔴 **They are written and tested in the author's own script.** 🟢 **The
general claim: a cost-saving pre-filter is an ACCESS control, and it needs to be evaluated as
one — on the scripts of the learners, not of the committers.**

### 3. 🆕 🟢 APAC's eight-pass adoption drought BREAKS, and the vocabulary change is why — *APAC, search-summary*

🔴 **For eight passes this shelf recorded *"NO APAC adoption rate"*.** 🟢 **p162 named the cause
honestly — *saturated at this shelf's query vocabulary* — so this pass CHANGED the vocabulary,
dropping the standing `adoption regulation players` phrasing for a named-instrument query.**
[`evidence/regional-sweep.2026-10-13-p163.tsv`](../evidence/regional-sweep.2026-10-13-p163.tsv)

🟢 **OECD **TALIS 2024** country notes, teachers reporting they have used AI in their work:**

| jurisdiction | figure | region |
|---|---|---|
| 🟢 **Singapore** | **`75%`** | APAC |
| 🔴 **Japan** | **`17%`** | APAC |
| 🟢 **UAE** | **`~75%`** | EMEA |
| 🔴 **France** | **`<20%`** | EMEA |
| 🟡 **OECD average** | **`36%`** | Global |

🟡 **Labelled *search-summary* and NOT promoted: `oecd.org` and `ei-ie.org` both refused at the
proxy** *(`T158`)*. 🔴 **And one disagreement is recorded rather than smoothed: Education
International's summary gives the OECD average as `~41%` where the country notes give `36%` — a
`5`-point conflict on the same instrument.** 🟡 **Singapore's own ministry frames its `75%`
narrowly, as *"to teach or facilitate student learning"*, so the definition is not identical
across the three renderings.**

🟢 **`T143`'s gate fired and was honoured again: the `57%` *"organisations in Asia"* figure is
ENTERPRISE and was REFUSED, not re-regionalised into an education number.**

🔵 **The trend itself, which is bigger than the drought:** 🔴 **a `58`-point spread between two
high-capacity APAC systems** *(Singapore `75%`, Japan `17%`)* 🔵 **means *"APAC readiness"* is not
a usable planning unit.** 🟢 **An engagement scoped per-jurisdiction is the only honest shape, and
the `36%` OECD average is the least useful number on the table.**

### 4. 🆕 🟢 LATAM gets its FIRST corroboration pair on this shelf — *LATAM, two independent instruments*

🟢 **p162 recorded UNESCO IESALC: `200` institutions, `19` countries, `87%` using AI somewhere,
`26%` with a formal framework.** 🆕 🟢 **This pass found a SECOND, independent instrument: the
Digital Education Council's *AI in Higher Education LATAM Survey 2026*, `29` institutions —
`92%` of students and `79%` of faculty actively engaging, and **`30%` of universities with a
published AI policy**.**

| measure | UNESCO IESALC *(p162)* | DEC LATAM 2026 *(p163)* | agreement |
|---|---|---|---|
| 🟢 institutions with a formal/published AI policy | **`26%`** | **`30%`** | 🟢 **within `4` points** |

🆕 🟢 **This is the first time a LATAM figure on this shelf has been corroborated by a second
instrument** — 🟢 **and the two were collected at different scales (`200` vs `29` institutions)
with slightly different questions, which makes the `4`-point agreement more informative than a
match would be.** 🔵 **The governance gap in LATAM is now a measured fact rather than a single
survey's claim: roughly three of four institutions use AI without a published policy.**

🟡 **Both remain *search-summary* — `digitaleducationcouncil.com` refused at the proxy.**

### 5. 🔴 The market-size incoherence WIDENS — thirteenth pass as a finding, and now `$1.9B` in the base year

🔴 **`2025` base year: `$6.4B` (IMARC) against `$8.3B` (a second vendor) — a **`$1.9B` spread**,
up from p162's `~$1B`.** 🔴 **`2026` projected at `$10.6B` (The Business Research Company).**
🟢 **`T122` corroborated a SEVENTH time, and `T110` a SEVENTH.**

🔵 **The structural reading this page has held for twelve passes is unchanged and is reinforced:
these are vendor forecasts with undisclosed segment definitions, so the SPREAD is the only
honest datum and the point estimates should not be quoted to a client.** 🟢 **What is quotable is
the direction plus the adoption figures above, which come from survey instruments with stated
samples.**

## Pass 162 — 2026-10-13

### 1. 🆕 🔴 The Annex III evaluative tier has TWO open-source platforms in it, and the permissive one is MIT — *Global, strongest in EMEA and APAC, measured*

🔴 **`T140` placed the AI Act's evaluative boundary BETWEEN Moodle and OpenOLAT. There is a third
platform, it was already on this shelf, and nobody had read its schema.**
🟢 **`Selleo/mentingo` (MIT) ships `ai_judge`: `7` tables, an author-set
`passing_threshold_percent`, rubric score anchors with worked examples, and
`ai_mentor_judgements.passed BOOLEAN NOT NULL` — a persisted pass/fail verdict on a learner.**
🔴 **Unlike OpenOLAT's `essay-grading`, it is not behind a feature flag that ships `false`; it is
schema, and `ai_mentor_lessons.type` already defaults to `roleplay`.**
🔵 **Consequence for a studio: *"use the MIT one to stay simple"* is no longer a way to stay out
of the high-risk tier. The permissive choice and the regulated choice are now the same choice.**
🟢 **`T145`.**
[`evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv`](../evidence/evaluative-tier-tri-platform.2026-10-13-p162.tsv)

### 2. 🆕 🟢 Two independent teams converged on the same human-oversight design, which makes it a PATTERN — *Global, measured*

🟢 **OpenOLAT (Java, Apache-2.0, Switzerland) and mentingo (TypeScript, MIT, Poland) both refuse
to let the model own the outcome, and they do it differently:**

| control | OpenOLAT | mentingo |
|---|---|---|
| what the model returns | 🟢 raw SIGNALS; its holistic score is *"advisory only"* | 🟡 per-criterion `awardedScore` |
| who computes the outcome | 🟢 **server-side weighting** | 🟢 **`sum(awardedScore)` vs `ceil(maxScore × passingThresholdPercent / 100)`** |
| out-of-range model output | 🟢 typed confidence + off-topic enums | 🟢 **THROWS — refuses rather than clamping silently** |
| the veto | 🟢 `3` pre-filters refuse before the provider is paid | 🟢 **blocking errors, each re-verified by a SECOND model call before it can fail a learner** |
| re-runnability of a contested mark | 🟢 `a_prompt_template_version` + `a_content_hash_at_call` | 🟢 **`max_score_at_judgement` per criterion** |

🔵 **One implementation is an existence proof. Two, in different languages and jurisdictions, is a
design consensus — and it is the single most reusable artefact this shelf has for an Article 14
conversation.** 🟢 **Neither was built by a vendor selling AI governance.**

### 3. 🆕 🔴 Injection defence tracks the ORGANISATION CHART, not the threat model — *Global, measured*

🔴 **OpenOLAT's `AiContentHardener` is real: `169` LOC, `14` injection regexes, HTML and
`javascript:` stripping, redaction markers, typed issues, `194` LOC of tests.** 🔴 **Its one call
site is the AUTHOR's course page. The STUDENT's answer — the only input written by somebody with
an incentive to manipulate the grade — reaches the prompt unscrubbed, defended by a system-message
sentence and a `-----` fence.** 🟢 **`T144`.**
🔵 **The generalisable claim: engineering teams harden the input they think of as *content* and
trust the input they think of as *an answer*. The threat model is the reverse.**
🟢 **Fix is `P162-B` and it is hours, not weeks.**

### 4. 🆕 🔴 A capability audit cannot find a capability nobody claimed — *Global, methodological*

🔴 **STEP 7 and STEP 8 both take the PUBLISHED list as input, so they can only confirm or retract
what an earlier pass wrote down.** 🟢 **`0 of 8` published capabilities failed. The pass's real
finding — a complete evaluative AI subsystem — came from a migration filename that no audit step
asked about.** 🟢 **`T146`, and `P160-A` gains STEP 9: enumerate the platform's OWN vocabulary
from its schema before auditing the list you already hold.**

### 5. 🆕 🔴 A regulatory boundary drawn at a core/plugin line is a FACT, not a GATE — *Global, strongest in EMEA, measured*

🟢 **`ACTION IE`: `core_ai\placement` is an abstract class with `4` declarative methods and no
sandbox. `get_supported_actions()` simply calls the placement's own `get_action_list()` with no
allowlist. `process_action(base $action)` accepts ANY subclass. `store()` is abstract and
plugin-implemented, `get_tablename()` is overridable, and `grade_update()` is a GLOBAL function in
`public/lib/gradelib.php` whose `$source` argument is a free-text label with no caller check.**
🔴 **So *"Moodle core is outside Annex III"* is true and nearly useless as a control: the first
third-party placement that grades carries the institution in, and core offers no technical means
to prevent it.** 🟢 **`T147`.**
🔵 **What a studio sells here is the governance that core does not enforce: a plugin allowlist, a
review gate on `aiplacement_*` installs, and the `ai_action_register` report that already exists.**
[`evidence/placement-gradebook-reach.2026-10-13-p162.tsv`](../evidence/placement-gradebook-reach.2026-10-13-p162.tsv)

### 6. 🆕 🔴 This shelf's own instruments were wrong about cost and wrong about reach — *Global, methodological*

🔴 **Three self-corrections in one pass, all cheap to test and all left untested for six:**

| belief | measured this pass |
|---|---|
| 🔴 *"the Moodle path census costs `746 MB`"* | 🟢 **`3.1 MB` and `1` second with `--filter=blob:none --no-checkout`, and it AGREES at `67 589` paths** |
| 🔴 *"GitHub metadata is gone (`T137`)"* | 🟢 **Per-repository metadata returns `200` once the repo is attached; the `403` body named the remedy all along.** 🔴 **Ranking and new-entrant discovery really are gone** |
| 🔴 *"the source hosts do not resolve (`T134`)"* | 🔴 **They resolve. The PROXY refuses `CONNECT` with `403` on a developer-host allowlist** |
🔵 **The methodological lesson, worth more than any single figure: a declared gap must be
re-tested, not inherited. This shelf inherited three.** 🟢 **`T148`, `P162-A`.**

### 7. 🟡 The market series is incoherent for a THIRTEENTH pass, and the incoherence is now in the BASE YEAR — *Global, search-summary*

🔴 **IMARC: `$6.4B` (2025) → `$79.6B` (2034). The Business Research Company: `$7.52B` (2025) →
`$10.6B` (2026) at `40.9%` CAGR.** 🔴 **The two disagree by roughly `$1B` on the year that has
already happened.** 🟡 **AI tutors as a sub-segment: `$1.63B` (2024) → `$7.99B` (2030).**
🔴 **No open-source vendor appears in any market source, THIRTEENTH pass.**
🔵 **Stop quoting a market size in a client deck from this channel; quote adoption and governance
gaps, which are measured on populations rather than modelled.**

### 8. 🆕 🟢 LATAM's adoption/governance gap now has a FUNCTION and INSTITUTION-TYPE breakdown — *LATAM, search-summary*

🟢 **UNESCO IESALC, `200` institutions across `19` countries: `87%` use AI somewhere, `26%` have
any formal framework — a figure this shelf already held — and now the shape underneath it.**
🟢 **By function: teaching and learning `73.5%`, research `57.0%`, administration `34.1%`,
community engagement `20.0%`.** 🟢 **By institution type: private non-profit `84%`, public `68%`,
private for-profit `52%`.**
🔵 **The engagement reading: adoption is concentrated in teaching, which is precisely the
evaluative, student-facing surface that `T145` just showed is a high-risk tier — and
administration, at `34.1%`, is where the governance plumbing would have to live.**
🔴 **Labelled search-summary: all four source hosts refused at the proxy (`T148`).**
## Pass 161 — 2026-10-12

### 1. 🆕 🔴 The AI Act's high-risk boundary runs BETWEEN two open-source LMS platforms, and it is a property file — *Global, strongest in EMEA and APAC, measured*

🟢 **Three platforms read from clones this pass.** 🟡 **Moodle: `372` AI files, `4` actions —
`generate_text`, `generate_image`, `summarise_text`, `explain_text` — `0` of them evaluative.**
🟢 **OpenOLAT: `149` AI files, `4` features — and one of them is `essay-grading`.**
🔴 **`edx-platform`: `0` AI files of any kind.**
🔴 **So an institution crosses into Annex III's evaluative tier by setting
`ai.feature.essay-grading.enabled=true` in `olat.properties`, a line that ships `false`.**
🔵 **The consequence for a studio: the regulatory scoping conversation now has a concrete
artefact in it. Not *"will the LMS do AI"* but *"which of these four flags, and does any of them
grade"*.** 🟢 **`T140`.**

### 2. 🆕 🟢 Human oversight has an OPEN-SOURCE REFERENCE IMPLEMENTATION, and it is not a policy document — *Global, strongest in EMEA, measured*

🟢 **OpenOLAT's grading path was read line by line.** 🟢 **The model returns raw signals only and
its own holistic score is documented in the code as *"advisory only, server-side weighting is
authoritative"*, so the number that reaches the gradebook is computed by the platform.**
🟢 **A consent modal offers `allow-once` / `allow-always` / `deny`.** 🟢 **Three pre-filters —
gibberish by trigram entropy, language mismatch, length — refuse the call BEFORE a provider is
paid.** 🟢 **Confidence, off-topic flag and issue severity are typed enums, not prose.**
🟢 **`a_content_hash_at_call` and `a_prompt_template_version` make a contested mark
re-runnable against the exact prompt that produced it.**
🔵 **Every one of these is something a studio has been writing into a governance deck. One of
them is now `Apache-2.0` code a client can read.** 🟢 **`P161-A`.**

### 3. 🆕 🔴 Both platforms that ship AI retain prompts and responses, and NEITHER deletes them — *Global, measured*

🔴 **Moodle stores `prompt` and `generatedcontent` verbatim in `ai_action_generate_text`,
`ai_action_summarise_text` and `ai_action_explain_text`, and `prompt` + `revisedprompt` +
`sourceurl` in `ai_action_generate_image`.** 🔴 **`grep -riE 'retention|purge|cleanup|expiry'`
over `public/ai` returns nothing; there is no `db/` directory, no scheduled task and no
settings page in the subsystem.** 🔴 **OpenOLAT's `AiUsageLogDAO` has no delete method and
`o_ai_essay_correction.a_student_answer` is `text NOT NULL` — the essay itself.**
🟢 **Moodle's GDPR surface is nonetheless complete — `806` LOC, export plus three delete paths,
all six tables declared — so erasure works on REQUEST.** 🟡 **And `tool_dataprivacy` can expire
contexts on a schedule, gated behind `automaticdatadeletionapproval`, which ships `0`.**
🔵 **The pattern across the industry: GOVERNANCE shipped, RETENTION not. Consent and audit are
features a product manager can demo; a deletion job is not.** 🟢 **`P161-B`.**

### 4. 🆕 🔴 A capability census must read the MIGRATIONS, because a platform can delete a feature and keep its files — *Global, measured*

🔴 **`edx-platform` has `23` non-test `badge` paths and a whole `lms/djangoapps/badges` app.**
🔴 **`migrations/0005_delete_all_models.py`, dated 2023-10-24, drops `BadgeClass`,
`BadgeAssertion`, `CourseEventBadgesConfiguration` and `CourseCompleteImageConfiguration`.
`models.py` is a `25`-line stub.**
🔵 **`T136` showed a path census over-counts by NAME. `T141` is the fourth contamination and it
over-counts by HISTORY — the files are real, the feature is gone.** 🟢 **`P160-A` gains a
STEP 7: read the migration directory before publishing a capability as present.**

### 5. 🆕 🔴 On a plugin-architecture platform, a single-repo census publishes FALSE ABSENCES — *Global, measured*

🔴 **In `edx-platform`, `lti13`, `lti1p3` and `ltiadvantage` all return `0`; `xapi` returns one
migration.** 🟢 **Both capabilities exist — as `lti-consumer-xblock` and
`event-routing-backends`, pinned in `requirements/edx/base.txt`.**
🔵 **`T142`: the dependency manifest is the second instrument, and on a platform whose
`9 243` tracked files are a tenth of Moodle's, it is the more informative one.**
🔵 **It also changes how a capability is SCOPED commercially: an Open edX LTI deliverable is a
dependency with its own licence and its own maintainer, not a platform feature.**

### 6. 🆕 🟢 Europe finally has an adoption number, and the belief number underneath it is the finding — *EMEA, search-summary*

🟢 **`63%` of European teachers now use AI — more than `20 000` teachers, `14` countries, Sanoma
Learning's 2026 European Teacher Survey.** 🔴 **`16%` believe general-purpose AI improves
learning outcomes, *"changed only marginally"* year on year.**
🔵 **A `63%` / `16%` split is the clearest statement of the market this shelf has recorded:
teachers are using tools they do not believe in, which is a demand signal for
education-specific systems and a warning to anyone selling a general assistant with a
mortarboard on the landing page.**
🔴 **Labelled *search-summary* — the primary release host does not resolve from this session,
sixth measurement of the egress boundary.**

### 7. 🆕 🟡 The enthusiasm gap between APAC and North America is `31` points in the same instrument — *APAC and North America, measured*

🟡 **`57%` of Asia-Pacific faculty are excited about AI's potential to make learning more
effective; `26%` of US+Canada faculty are (DEC 2026, `45 398` responses, `35` countries).**
🟢 **It sits directly underneath the intent decline this shelf already held — US+Canada faculty
intent `76% → 67%`, the lowest of any region DEC tracked.**
🔵 **Read together they say the Western market is in a disillusionment phase while APAC is still
in an expansion one** — 🔴 **but an APAC adoption RATE still does not exist after seven passes,
so the expansion is measured by sentiment, not by use.**

### 8. 🆕 🔴 The aggregator layer re-regionalises figures, and only a second query catches it — *Global, measured*

🔴 **This pass's APAC search returned a figure this shelf holds as US+Canada, attached to
Asia-Pacific and described as the region with the lowest intent.** 🟢 **A targeted re-query
settled it in the shelf's favour; nothing was changed.**
🔵 **`T143` is a gate, not an anecdote: a held figure arriving with a NEW region attached is a
provenance event. Re-query naming the instrument before the shelf is touched.**
🔵 **It also bounds what regional saturation means — the channel is not merely repeating itself,
it is repeating itself with drift.**

## Pass 160 — 2026-10-12

### 1. 🆕 🟢 The governed-AI plumbing an education client would pay to build is already in Moodle core — *Global, measured*

🟢 **`public/ai`, `372` files, GPL-3.0:** 🟢 **seven pluggable providers (`anthropic`,
`awsbedrock`, `azureai`, `deepseek`, `gemini`, `ollama`, `openai`), a per-call ledger in
`ai_action_register` (user, course, context, provider, model, prompt and completion tokens,
success, error, timings), per-user policy acceptance in `ai_policy_register` with a
`reportbuilder` report, and `rate_limiter.php`.**
🆕 **`T139`:** 🔵 **the audit artefact `P158-A` assembled from Langfuse traces and `mentingo`'s
rubric tables EXISTS IN CORE on the world's most widely installed LMS.**
🔴 **And the boundary is exactly as useful as the capability: Moodle core AI has FOUR actions —
`generate_text`, `generate_image`, `summarise_text`, `explain_text` — and NONE is evaluative.**
🟢 **So core Moodle does not grade, score or place a learner, and sits outside the EU AI Act's
Annex III evaluative tier; the first plugin that adds an evaluative action inherits the
high-risk obligations.** 🔵 **That line is where `P160-B` puts the engagement.**

### 2. 🆕 🔴 This shelf publishes path counts as capability evidence, and a path count is contaminated three ways — *Global, measured*

🔴 **`ipath *lti*` returns `1 225` paths in Moodle; `375` of them (`30.6%`) are `multi`** —
`multianswer`, `multichoice`, `multilang`. 🔴 **OpenOLAT: `128 of 388`, `33.0%`.**
🔴 **`ipath *tenant*` returns `62` paths in Moodle and `62 of 62` are inside the VENDORED
`public/lib/google2-service`.** 🔴 **`mentingo`'s `8` and `richie`'s `7` *"badge"* paths are
`15 of 15` UI components.**
🔴 **And it fails in the other direction too: `lti13` returns `0` in Moodle, which spells LTI 1.3
`ltiadvantage`; `ltiadvantage` returns `0` in OpenOLAT, which spells it `lti13`.**
🆕 **`T136`:** 🟢 **disambiguate the token, attribute the hits to first-party code, and take the
probe vocabulary from the platform itself — otherwise the census invents both capabilities and
absences.** 🟡 **p159's OpenOLAT figures are NOT affected: they were directory-scoped.**

### 3. 🆕 🔴 Three instruments, three blind spots, one rule: match the instrument to how the capability is IMPLEMENTED — *Global, measured*

| instrument | blind to | instance |
|---|---|---|
| 🔴 **topic query** *(`T133`, p159)* | a capability shipped as a MODULE of a platform | OpenOLAT's Open Badges, invisible to `topic:open-badges` |
| 🆕 🔴 **schema census** *(`T135`, this pass)* | a capability shipped as an EXPORT PIPELINE | 🟢 **`mentingo` ships SCORM — `119` files, `scorm-export-generator` + `scorm-export-runtime` with a bundled player.** 🔴 **p158's `T127` read the DB schema and called the claim false** |
| 🆕 🔴 **path-name census** *(`T136`, this pass)* | nothing — it OVER-counts instead | `multi`, vendored SDKs, UI badges |

🟢 **`T127` is AMENDED, not withdrawn: `mentingo`'s `xapi` topic claim is still unsupported
(`README` only, `0` code matches).** 🔵 **The pattern across all three: an instrument's blind
spot is a property of the IMPLEMENTATION SHAPE it cannot see, and three different instruments
have now mis-reported the same shelf.**

### 4. 🆕 🟢 Credentialing has TWO open-source incumbents, both one spec version behind the demand — *Global, with North America and EMEA weight*

🟢 **`ACTION HX` + `ACTION HY`, both falsifiers SILENT: Moodle ships Open Badges at `306` paths
and OpenOLAT at `182`.** 🔴 **Both are `v2` ONLY — `OPEN_BADGES_V2` appears `132` times in
Moodle's code and `V3` never; neither emits an OB 3.0 or W3C Verifiable Credential on any of
eight spellings; `mentingo`, `richie` and `openlxp-xia` have no credentialing at all.**
🟢 **Against 1EdTech's Badge Count 2025 — `40%` of badge providers issuing some OB 3.0,
`2 694 271` OB 3.0 achievements, `6 269 066` CLRs, `74M`+ badges total.**
🔵 **So the lane is not *"no incumbent"* (p157) and not *"one incumbent"* (p159): it is TWO
incumbents at `v2`, dated demand at `v3`, and a signing step nobody permissive has shipped.**
🟢 **`P159-A` stands as a build, and its scope is now confirmed: authoring exists
(`opensalt/OB3DefinitionWidget`, MIT), issuance does not.**

### 5. 🆕 🟢 The platform choice now splits on TWO measured dimensions instead of licence alone — *Global, measured*

| if the engagement needs | the answer is | because |
|---|---|---|
| 🟢 **modern QTI assessment interchange** | 🟢 **OpenOLAT** *(Apache-2.0)* | 🟢 **`919` QTI paths against Moodle's `8`** — 🔴 **and Moodle's eight are QTI `v1.2` legacy: Common Cartridge `.xsd` and a Blackboard import filter** |
| 🆕 🟢 **xAPI learning records** | 🆕 🟡 **Moodle** *(GPL-3.0)* | 🟢 **`public/lib/xapi`, `78` paths, `api.php`/`iri.php`/`state_store.php`.** 🔴 **OpenOLAT: `0` on four spellings** |
| 🟢 **multi-tenancy** | 🟢 **`mentingo`** *(MIT)* | 🔴 **NEITHER platform has it: Moodle's `62` "tenant" paths are all vendored, OpenOLAT has none, and Moodle Workplace is proprietary** |
| 🟢 **permissive licence** | 🟢 **OpenOLAT / mentingo** | 🟢 Apache-2.0 `10 982 B` / MIT `1 062 B`, bodies read |

🔵 **This is the first pass where the recommendation is not *"take the Apache one"*** — 🟢 **one
capability (xAPI) now points at the copyleft platform, and the honest routing table says so.**

### 6. 🆕 🔴 The web channel for AI-in-education is SATURATED at this shelf's depth — *Global, measured*

🔴 **Twelve queries this pass — four global, one per region — returned `0` new regional facts.**
🟢 **Everything that came back was already held: `134` bills / `31` states, Ohio's deadline,
`H.R. 8747`, Korea's `2026-01-22` commencement, Vietnam's `134/2025/QH15`, IESALC's `200`/`19`,
the DEC surveys, the UNESCO LAC Observatory.** 🟡 **The ONE new item is an unverifiable seventh
AI-Act date variant from a Commission page the session cannot reach** *(`T134`)*.
🔵 **Stated as a property of the channel rather than as a gap in the research: at this depth, new
education findings come from TREES, from NAMED primary instruments, and from the unread scope of
named surveys — not from another round of the same five queries.**
🟢 **Every finding in this pass came from the first of those three.**

### 7. 🆕 🟢 The licence-absence figures this shelf has published are CONFIRMED, and the gate's error is confined to the mature tier — *Global, measured*

🟢 **`ACTION HW`: all `37` no-grant rows from the published bands re-probed on `P56`'s 33 paths,
after `ls-remote` confirmed each exists.** 🟢 **Recoveries: `0`.**
🟢 **So rows 1–80 stay at `18.8%` and rows 96–195 stay at `23.0%` — the falsifier was `±3` points
and the change is `0.0`.** 🔴 **p159 expected a `1–3` point correction and was WRONG.**
🆕 **`T138`:** 🔵 **`T129`'s *"the gate's error tracks maturity"* is now bounded at both ends —
`26.7%` false absence on the platform control, `0.0%` across `37` hobby-tier rows.**
🟢 **The open-gaps entry calling the published shares *"OVERSTATED by an unknown amount"* is
closed; `T128`'s monotone licence gradient survives unchanged.**
## Pass 159 — 2026-10-12

### 1. 🆕 🔴 Licence risk is a function of STAR RANK, and the previous reading was backwards — *Global, measured*

🟢 **Four bands, three passes, one monotone direction:** 🟢 **`0.0%` no-grant in the top ten** →
🟡 **`18.8%` (rows 1–80)** → 🟡 **`23.0%` (rows 96–195)** → 🔴 **`47.0%` (rows 196–295)**.
🔴 **p157's `T123` — *"the attention leaders are AGPL-3.0 or unlicensed"* — is WITHDRAWN:** at the
top ten, bodies read, 🟢 **`8 of 10` are permissive and `0` are unlicensed.**
🆕 **`T128`:** 🔵 **the practitioner rule is that a studio's licence tax rises as it digs deeper
into a topic.** 🟢 **Sourcing from the top is nearly free; below about row 200, half of what you
find cannot be used at all.**

### 2. 🆕 🔴 This shelf's own licence instrument was understating absence on the rows that matter most — *Global, measured*

🟢 **Run on a known-answer control of 15 platform rows, the 9-path gate returned
`NO_LICENCE_FILE` for `4`** — 🔴 **Moodle (`COPYING.txt`, GPL-3.0), ERPNext and Frappe LMS
(`license.txt`), and `openedx/XBlock` (`NOTICE.txt`).**
🔴 **`26.7%` false-absence rate on the control against `4.3%` in the `1 ★` tail.**
🆕 **`T129`, and the mechanism explains the gap:** 🟢 **GitHub's *"Add license"* button writes
`LICENSE`, so button-era hobby projects are found and GNU-convention or framework-convention
projects are missed.** 🔴 **The instrument was therefore most reliable where this shelf sampled
and least reliable on the platform tier it recommends to clients.**
🔵 **`T106`'s family again, in its most expensive form yet: an instrument's error rate is not
constant across the population it is applied to.**

### 3. 🆕 🔴 A capability census by TOPIC cannot see a capability that ships as a MODULE — *Global, measured*

🔴 **p157 measured `topic:open-badges` — `29` repositories, an `85 ★` ceiling — and concluded
credentialing is *"the only lane with named demand and no incumbent."***
🔴 **`openolat/OpenOLAT` ships `org/olat/modules/openbadges` at `156` paths**, with `Badge`,
`Assertion`, `Criteria`, `Profile`, `Identity`, `BadgeClass`, a LinkedIn push and a rule engine
that awards automatically — 🟢 **Apache-2.0, `447 ★`.**
🆕 **`T133`:** 🔵 **a topic query returns projects whose IDENTITY is the capability; it structurally
cannot return platforms for which the capability is one module of two hundred.** 🟢 **Any
*"no incumbent"* finding on this shelf must now be re-tested against the module trees of the
platforms it already tracks.**

### 4. 🆕 🔴 The GitHub topic list is unreliable in BOTH directions — *Global, measured*

🔴 **p158's `T127`: `mentingo`'s topics advertise `scorm` and `xapi` its schema lacks** —
over-claiming. 🔴 **`OpenOLAT`'s topics list `qti`, `scorm`, `lms` and `curriculum-management`
but NOT `lti`**, although LTI 1.3 is its deepest surface at `148` paths, in both directions.
🆕 **`T132`:** 🟢 **a topic list cannot settle a capability question in EITHER direction.**

### 5. 🆕 🟢 Credentialing has quantified demand for a standard the open-source platform does not emit — *Global, with North America and EMEA weight*

🟢 **1EdTech's Badge Count 2025 survey: `40%` of badge platform providers report issuing at least
some Open Badges 3.0, totalling `2 694 271` OB 3.0 achievements; `22%` report issuing
Comprehensive Learner Records, totalling `6 269 066`; `74 million`+ Open Badges issued globally.**
🔴 **`OpenOLAT`'s module is Open Badges `v2` — `0` matches for `OpenBadgeCredential`,
`VerifiableCredential` or an `openbadges/v3` package.** 🟢 **The `v3` AUTHORING surface is already permissive on this shelf —
[`opensalt/OB3DefinitionWidget`](https://github.com/opensalt/OB3DefinitionWidget), MIT, `1 080 B`.**
🔴 **What is missing is ISSUANCE: the only library that SIGNS an OB 3.0 / W3C Verifiable
Credential is LGPL-3.0 with `1 ★`.**
🟢 **So the lane is bracketed from both sides for the first time: dated demand above, a named
permissive platform below, and the gap between them is exactly one spec version.**
🟡 **Caveat: the 1EdTech figures reached this shelf through the search channel; `1edtech.org`
refuses this session's egress, so they are not read at source.**

### 6. 🆕 🔴 A second jurisdiction now puts EDUCATION in a statutory high-risk tier — *APAC primary, Global consequence*

🟢 **Vietnam's AI law is reported effective `2026-03-01`, classifying education as a HIGH-RISK
sector including automated assessment.**
🔵 **The EU AI Act's Annex III put evaluative educational use in the high-risk tier; Vietnam is
the second jurisdiction to do it by statute, and Korea's AI Basic Act (in force `2026-01-22`,
with 2026 described as a pilot year and a one-year penalty grace period) is a third framework in
the same direction.**
🆕 **Consequence for architecture, not paperwork:** 🟢 **`P158-A`'s rubric-as-data design was built
for Oklahoma, Maryland and Annex III. It now answers a THIRD regime** — 🔵 **which makes it the
portable choice rather than a regional one.**
🟡 **Sources disagree on Vietnam's grace periods; the effective date is reported consistently.**

### 7. 🆕 🟢 The first K-12 adoption data for LATAM, and the region is ABOVE the OECD average — *LATAM, measured*

🟢 **TALIS 2024: secondary-school teachers who used AI in the previous year — Brazil `56%`,
Chile `55%`, Colombia `53%`, Costa Rica `52%`, against an OECD average of `36%`.**
🟢 **Uruguay: `75%` of public-school teachers report using these tools (Ceibal, 2026).**
🔵 **Every LATAM figure this shelf held was HIGHER EDUCATION.** 🟢 **The K-12 layer is now
measured, it comes from a primary instrument, and it runs `16–20` points above the OECD
average** — 🔴 **which inverts the assumption that LATAM is the late adopter in a sales deck.**

### 8. 🆕 🟢 The region's governance gap is corroborated INDEPENDENTLY, down to the segmentation — *LATAM, measured*

🟢 **UNESCO IESALC, `200` institutions across `19` countries: `87%` use AI in at least one area,
🆕 `74%` in TEACHING AND LEARNING, and only `26%` have a formal AI strategy.**
🟢 **The segmentation p157 published is reproduced exactly by a second reading: private
non-profit `84%`, public `68%`, private for-profit `52%`.**
🔵 **A figure that survives an independent re-derivation is worth more than a newer one** —
🟢 **and `74%` in teaching and learning is the number that sizes the actual buying centre.**

### 9. 🆕 🟢 The FIRST EMEA-only market size, and it passes an internal coherence check — *EMEA, measured*

🟢 **European AI-in-education market: `$2.64B` in 2026, to `$8.0B` by 2030 at a `31.9%` CAGR.**
🟢 **Checked against the shelf's other figures: EMEA at `$2.64B` is `24.9%` of the global
`$10.6B`; p158's North America share is `36%` / `$3.68B`.** 🟢 **`36% + 25% = 61%`, leaving `39%`
for APAC, LATAM and the rest — coherent.**
🟡 **The global figure now also carries a horizon: `$10.6B` (2026) → `$42.48B` (2030) at `41.5%`
CAGR.** 🔴 **Still not a primary study, TWELFTH pass** — 🟢 **but three figures that cohere beat
one that is merely repeated.**

### 10. 🆕 🟢 The incumbents' own institutions are now arguing for purpose-built education AI — *Global, named sources*

🟢 **The OECD's 2026 Digital Education Outlook recommends moving beyond general-purpose AI tools
toward purpose-built educational AI designed to produce durable learning gains.**
🟢 **1EdTech expects institutions to define governance structures, clarify compliance
expectations and establish evaluation processes.** 🟢 **HolonIQ reports the clearest gains came
from course design support, teacher productivity and administrative workflows, and that systems
increasingly expect EVIDENCE that products improve learning quality, persistence, well-being or
job-relevant skills.**
🔵 **p158's `T115` said the incumbent is an unprocured general assistant, being procured at zero
price.** 🆕 **The counter-pressure is now named and institutional rather than hoped for** —
🟢 **and *"purpose-built, with evidence"* is precisely what a studio engagement sells and a free
seat licence does not.**

### 11. 🆕 🔴 The egress boundary is MEASURED, so eleven passes of *"no primary source"* were a channel property — *Global, measured*

🟢 **Probed this pass: `raw.githubusercontent.com` → `200`; `github.com` → refs resolve;
`api.github.com` → `403`; `www2.gov.bc.ca`, `www.1edtech.org`, `content.1edtech.org` and
`www.unesco.org` → `000`, DNS refused.**
[`evidence/egress-boundary.2026-10-12-p159.tsv`](../evidence/egress-boundary.2026-10-12-p159.tsv)
🆕 **`T134`:** 🔴 **this session reaches GitHub and the search channel. Nothing else.**
🟢 **So *"no primary legal text"*, *"no primary market study"* and *"no third-party efficacy
evidence"* are not research failures and never were** — 🔴 **they are the shape of the channel,
and they are not fixable from inside a pass.**
🟢 **They are retired from the register by decision and recorded once, here, with the measurement
behind them.**
## Pass 158 — 2026-10-12

### 1. 🆕 🔴 The non-open-source licence is now a FAMILY, not an anomaly — *Global, measured*

🟢 **`10 of 10` `NOASSERTION` licence bodies read from `raw` this pass. `6` are non-commercial or
non-grant by design:** 🔴 **Business Source License 1.1, PolyForm Noncommercial 1.0.0, PolyForm
Strict 1.0.0 (×2, byte-identical — one project, two owners), and two all-rights-reserved files.**
🔴 **GitHub files all ten as `Other`, and no UI a developer uses distinguishes them from MIT.**
🆕 **`T124`:** 🔵 **p156 found two non-open-source `LICENSE` files and read them as an oddity.
🟢 **At `n=100` the oddity is a licensing CHOICE with recognisable families behind it** — and the
authors who make it are not careless, they are deliberate. 🔴 **No market report mentions this.**

### 2. 🆕 🔴 A licence statistic is worthless without its standard of proof — *Global, measured*

🟢 **The same 100 rows yield `23.0%` or `33.0%` unlicensed, depending only on whether
`NOASSERTION` is counted as *"no licence."*** 🟢 **`23 of 23` metadata-null rows were re-probed on
8 paths and confirmed; `10 of 10` `NOASSERTION` rows have bodies.**
🆕 **`T125`:** 🔴 **`T106` a third time, and the sharpest instance — one sample, one instrument, a
10-point swing from a vocabulary choice.** 🟢 **Any licence figure a studio publishes must name
its basis, or it is not checkable.**

### 3. 🆕 🔴 Licence hygiene degrades as attention falls — *Global, measured*

🟢 **`topic:ai-tutor` rows `96–195` — the `4 ★ → 1 ★` tail — carry `23%` with no licence file,
against `18.8%` in rows 1–80.** 🔴 **p157 predicted LOWER and was wrong.**
🟢 **`57 of 100` are nonetheless MIT, so the tail is not unusable — it is UNEVEN**, and
🔵 **the practical read is that a tail row needs its licence read individually, because the
population rate no longer predicts the row.**

### 4. 🆕 🔵 The new-entrant tier is permissive and APAC-origin, inverting the attention tier — *APAC primary, Global consequence*

🟢 **`4 of the 5` new `topic:ai-tutor` projects created since `2026-08-01` are Chinese-language
and MIT/Apache-2.0**, led by `Miaotofu01/Study-Mate` — 🟢 **MIT, `894 ★` and 44 forks in about 25
days, the steepest new-row curve this shelf has measured in education.**
🆕 **`T126`:** 🔴 **p157's `T123` found the attention leaders to be AGPL-3.0 or unlicensed.**
🟢 **The arrivals are the opposite.** 🔵 **So the licence distribution of open education AI
depends on WHICH TIER you sample, and the useful tier for a studio is the new one — which is
also the one a star-sorted view hides for months.**

### 5. 🆕 🔴 A feature claim fails across instruments exactly like a licence claim — *Global, measured*

🟢 **`Selleo/mentingo`: the GitHub topic list claims `scorm` and `xapi`. The data model
(`104` tables, `100 244 B`) contains SCORM tables, NO xAPI and NO LTI. The README mentions
`xAPI/LTI` only inside a commented-out block its maintainers marked *"do not publish without
verification."*** 🔴 **This shelf republished the topic list for four passes.**
🆕 **`T127`:** 🔵 **the instrument ranking is the same as for licences — the data model is
authoritative, the README is cautious, the topic list is marketing** — 🟢 **and `P55` follows:
settle an interoperability question by grepping the schema and the dependency manifest.**

### 6. 🆕 🔴 Opposition to AI in schools is now measurable, and nobody was measuring it — *APAC primary*

🟢 **Ipsos: support for BANNING AI in schools rose from `21%` to `29%` in Japan, and stands at
`26%` in India.** 🔴 **This shelf holds nine passes of adoption and governance percentages and had
no opposition figure until now.**
🔵 **A quarter of two large markets favouring prohibition is a procurement risk that belongs in a
pitch, not a footnote** — 🟢 **and it strengthens the evidence-first framing of `P157-A`, because
the counter to a ban argument is a measured learning outcome, not a feature list.**

### 7. 🆕 🟡 The AI Act's education deadline is genuinely CONTESTED — *EMEA, the line to architect to*

🔴 **Annex III high-risk — the tier containing education — is `2026-08-02` on the Commission's own
page and `2027-12-02` in practitioner analyses of the May 2026 provisional deal.**
🔴 **This shelf cannot settle it; the primary text is behind a standing egress refusal, TENTH
pass.** 🟢 **What does not depend on the resolution: systems that determine access, assess
outcomes or shape a learner's path are high-risk on every reading, and the duty reaches non-EU
providers serving EU residents.**
🔵 **Architect to the earlier date; treat the later one as relief, not plan.**

### 8. 🟢 Governance coverage, not adoption, is the measurable quantity in EMEA — *EMEA, narrowed*

🆕 🟢 **`13%` of Italian universities had operational AI governance approaching the August 2026
point; `46%` of South African universities had institution-wide generative-AI guidance at a
February 2025 analysis.**
🟡 **Neither is the EMEA adoption RATE this shelf has sought for nine passes** — 🟢 **but both
measure the same thing on two continents inside EMEA, and both are low.**
🔵 **The thesis that carries across LATAM (IESALC `87% / 26%`), EMEA and now Africa is one
thesis: deployment is ahead of rules everywhere it is measured** — 🟢 **which is why `P156-B` is
the most portable pattern on this shelf.

### 🔴 What this pass did NOT find, said rather than implied

- 🔴 **No education-specific agent repository from ANY of the four mandated global web queries** — 🟢 **`P143-L` a FIFTH time; the channel returns listicles and courses.** 🟢 **The `created:>` search filter is what works.**
- 🔴 **No APAC or EMEA EDUCATION adoption rate.** 🟡 **Economy-wide and governance-coverage figures only.**
- 🔴 **No Canada.** 🟢 **Mexico answered, under LATAM.**
- 🔴 **No primary legal text, TENTH pass** *(categorical egress refusal on `eur-lex` and the law-firm hosts)*.
- 🔴 **No third-party efficacy measurement for any agent on this shelf** — 🟡 **the oldest open gap here.**

## Pass 157 — 2026-10-12

🟢 **Eight trends. Each names the region it was observed in and the channel that returned it.**
🔴 **Where a trend is an aggregator's claim rather than a sampled finding, the row says so.**
🆕 **Three of the eight are new this pass; five are carried with their evidence re-checked, and
the carried ones are marked so nobody mistakes repetition for movement.**

### 1. 🆕 🔴 Attention has decoupled from deployment — *Global, measured*

🔴 **One tutoring repository outweighs the entire institutional platform tier: `DeepTutor`
`41 210 ★` against `23 945 ★` for all 13 platform and foundational rows summed — `1.72 ×`.**
🔴 **Moodle, vendor-reported at 400M+ users, has `7 475 ★`; `DeepTutor` has `5.5 ×` that.**
🔵 **The trend is not *"tutoring is hot."* It is that the artefacts getting built and starred are
NOT the artefacts institutions run** — 🟢 **so a shortlist produced by sorting attention will
systematically miss the client's system of record.** 🆕 **`T118`.**
🟢 **Channel: GitHub metadata, 13 of 14 rows served.**
[`evidence/platform-attention.2026-10-12-p157.tsv`](../evidence/platform-attention.2026-10-12-p157.tsv)

### 2. 🆕 🔴 The modern open education platform is born network-copyleft — *Global, measured*

🟢 **Of the top eight `education`+`ai` repositories above `1 300 ★`, FOUR are AGPL-3.0** —
`Echo-Loop` (4 164), `penecho` (2 480), `learnhouse` (2 351), `ChatTutor` (1 316) — 🟢 **and all
four licence bodies land between `34 522` and `34 523 B`, a one-byte spread, so the family read
is not an inference.**
🔴 **Add Open edX (AGPL-3.0) and the pattern is the category default, not a coincidence.**
🔵 **Why it is a trend and not a licence trivium: AGPL reaches a HOSTED derivative.** 🔴 **The
standard edtech delivery model is hosting it for the client**, 🟢 **so the licence that the
attention leaders chose is precisely the one that makes the standard delivery model a disclosure
event.** 🆕 **`T123`.**
🟢 **Consequence: the protocol-boundary architecture is not a preference, it is the only
shape that survives the licences the market actually ships.**

### 3. 🆕 🟢 Buyer demand for credentials is real and the supply is absent — *Global, measured*

🟢 **2026 trend sources name digital credentials and micro-credentials against employer
skills-based hiring.** 🔴 **The entire `topic:open-badges` population is `29` repositories, the
star ceiling is `85`, and the standards-complete Open Badges 3.0 / W3C Verifiable Credentials
library has `1 ★`.**
🔵 **This is the shelf's first measured instance of demand without supply** — 🟢 **every other
gap on this page has been supply this shelf could not find. This one it found, counted, and the
count is the finding.**
🟢 **Channel: GitHub topic census, 15 of 29 rows read.**
[`evidence/credentialing-census.2026-10-12-p157.tsv`](../evidence/credentialing-census.2026-10-12-p157.tsv)

### 4. 🟢 The governance gap, now SEGMENTED — *LATAM, strongest evidence on this shelf*

🟢 **Carried and sharpened.** 🟢 **UNESCO IESALC, `2026-09-09`, 200 institutions / 19 countries:
`87%` use AI somewhere, `74%` in teaching and learning, `26%` have a formal AI strategy.**
🆕 🟢 **Newly segmented: private non-profit `84%`, PUBLIC `68%`, private for-profit `52%`.**
🔵 **The segmentation inverts the obvious read — for-profits are the LAGGARDS at `52%`, and the
public university at `68%` is the buyer with an accreditation body and a procurement process.**
🟢 **Corroborated one level down by TALIS 2024:** Brazil `56%`, Chile `55%`, Colombia `53%`,
Costa Rica `52%` of secondary teachers against an OECD average of `36%`.
🔵 **Sellable shape, unchanged: governance retrofit on an installed base, not a pilot.**

### 5. 🔴 The default AI in education is a general assistant — and it is now being procured free — *Global*

🟢 **Carried from p156 and materially sharpened.** 🟢 **IESALC names `ChatGPT`, `Copilot` and
`Gemini` as the default entry point, and attributes adoption to individual academics and
students rather than institutional strategy.**
🆕 🔴 **The update: Microsoft is supplying Copilot and Teams for Education FREE to Washington
state classrooms from 2026.**
🔵 **p156's `T115` said the incumbent was never procured. 🆕 It is being procured now, at zero
price, at state scale** — 🔴 **which closes the per-seat tutoring market rather than slowing it.**
🟢 **What remains sellable is what a general assistant cannot do: curriculum grounding, audit,
data boundaries, assessment integrity, a sanctioned institutional path.**

### 6. 🟢 Regulation has split into pedagogical vs evaluative use — *EMEA primary, the line to architect to*

🟢 **Carried, and now standing on a settled instrument rather than a contested one.** 🟢 **The
Commission's `2026-05-19` guidelines separate pedagogical support from evaluative use**, and
🆕 🟢 **the Council approved the Digital Omnibus `2026-06-29`, so p156's *"live amendment risk"*
on the `2027-12-02` horizon is resolved.**
🆕 🟡 **A fifth distinct date appeared — `2028-08-02` for high-risk AI embedded in regulated
products** — 🟢 **and like the other four it is a separate obligation, not a competing estimate
(`T112`).**
🔴 **Article 5's outright prohibition on emotion inference in schools is live NOW.** 🔵 **That is
a thing to design away from, not a risk tier to document.**
🟢 **The architectural consequence: the compliance boundary and the technical boundary coincide,
so one deliverable serves both.**

### 7. 🔴 *"Education"* in a general query means *"learning to code"* — FOURTH instrument — *Global*

🟢 **Carried, and corroborated on a fourth independent channel this pass.** 🔴 **A
`github trending education AI 2026` query returned only developer-learning repositories**
(`ai-engineering-from-scratch`, Karpathy's course, `AI Agents for Beginners`, `Made With ML`).
🔴 **And `topic:edtech`'s star sort is topped by a Claude-skill generator for technical books at
`34 654 ★`.**
🟢 **Four instruments now agree** *(the `education` topic page, GitHub Trending, a web trend
query, the `edtech` star sort)*. 🆕 🟢 **Newly quantified this pass: the narrow topic
`knowledge-tracing` returns `20 of 20` on-domain against `topic:education`'s `1 of 20`.**
🔵 **Operational rule: enter through a narrow topic, never a trend list.** 🆕 **`T119`.**

### 8. 🆕 🔴 A research channel can saturate without going quiet — *Global*

🔴 **`open source platform education ERP CRM MIT Apache` returned `10` of `10` results from ONE
vendor's own glossary, the same two articles in ten locales.**
🔵 **A channel that returns nothing announces its own failure. A channel that returns ten
confident, well-formed, on-topic pages from a single seller does not** — 🟢 **and that is the
harder failure to notice, because the output looks like research.**
🆕 **`T122`.** 🟢 **The query is retired as a market instrument.**
🟢 **One real datum survived it, and it is the eleventh-pass confirmation: the source itself
states there is no MIT- or Apache-licensed education ERP or CRM to name.**

### 🔴 What this pass did NOT find, said rather than implied

- 🔴 **No tutor EVALUATION harness, and now with a measured negative:** 🔴 **a direct search
  matched `122` repositories and `0 of 15` of the top rows were on-domain** — they were ML paper
  lists. 🔵 **Against an explicit 2026 buyer demand for evidence of instructional benefit
  before purchase. The instrument does not exist.**
- 🔴 **No EMEA-only adoption rate, NINTH pass.** 🔴 **No APAC adoption rate at all, FOURTH.**
- 🔴 **Canada and Mexico, SEVENTH pass of nothing.**
- 🔴 **Africa not queried as a region in its own right, THIRD pass.**
- 🔴 **`590` of `669` `ai-tutor` rows remain unread**, 🟢 **and the population itself moved —
  see `T111`'s correction on [`repos/trending.md`](../repos/trending.md).**

## Pass 156 — 2026-10-12

🟢 **Eight trends, each with the region it was observed in and the channel that returned it.**
🔴 **Where a trend is an aggregator's claim rather than a sampled finding, it says so in the
row.**

### 1. 🟢 The governance gap overtook the adoption gap — *LATAM, strongest evidence on this shelf*

🟢 **UNESCO IESALC, `2026-09-09`, `200` institutions, `19` countries: `87%` use AI somewhere,
`74%` in teaching and learning, `26%` have a formal AI strategy.**
🔵 **The trend is not *"adoption is rising."* It is that adoption ALREADY HAPPENED, informally,
and the institution has no policy for what its staff are already doing.**
🟢 **Corroborated one level down by TALIS 2024:** Brazil `56%`, Chile `55%`, Colombia `53%`,
Costa Rica `52%` of secondary teachers, against an OECD average of `36%`.
🔵 **Sellable shape: governance retrofit on an installed base, not a pilot.**

### 2. 🆕 🟢 The default AI in education is a general assistant nobody procured — *Global*

🟢 **IESALC names `ChatGPT`, `Copilot` and `Gemini` as the default entry point for teaching.**
🆕 **`T115`.** 🔴 **So the incumbent is not an edtech vendor and cannot be displaced by a better
tutor** — 🟢 **it is displaced, if at all, by an institutional layer that gives staff a sanctioned
path with audit, data boundaries and curriculum grounding.**

### 3. 🟢 From generic chatbots to purpose-built, governed tools — *Global, NA-weighted sourcing*

🟢 **Multiple 2026 sources agree institutions are moving off generic chatbots toward
education-specific platforms**, with the stated reason that 🔴 **teachers were spending the saved
time on prompt-writing and fact-checking instead.**
🟢 **2026 is described as *selective* AI acceleration: ethics, transparency, agentic use cases
and demonstrated instructional benefit over broad personalisation claims.**

### 4. 🟢 Agents, specifically multi-step agents, are the named 2026 development — *Global*

🟢 **The frontier is described as moving from single prompts to multimodal systems and agents
that carry out multi-step tasks** — planning a lesson sequence, drafting an assessment.
🟢 **This shelf's own topic census is the evidence from the supply side:** 🟢 **`685` repositories
carry `ai-tutor`, and `95` read rows are dominated by agent SKILLS rather than applications.**

### 5. 🟢 Evidence before purchase — *Global*

🟢 **Systems increasingly expect evidence that a product improves learning quality, persistence,
well-being or job-relevant skills, grounded in research.**
🔴 **And this shelf still has NO evaluation harness after 156 passes** — 🟢 **`pykt-toolkit`
(MIT) models learners, it does not evaluate a tutor.**
🔵 **The gap and the trend are the same fact: buyers want evidence and the open-source supply
has no instrument to produce it.**

### 6. 🆕 🟡 Digital credentials and skills-based hiring — *Global, and still unmet in open source*

🟢 **2026 sources name digital credentials and a skills-driven ecosystem, pushed by shifting
employer expectations and AI itself.**
🔴 **156 passes have found NO credentialing or skills-pathway repository.** 🟢 **Recorded as a
genuine supply gap rather than filled with an adjacent row.**

### 7. 🆕 🔴 The regulatory clock is now a sequence of DIFFERENT obligations, not one date — *EMEA, APAC*

🟢 **EMEA, four distinct events:** Article 5 prohibitions live and absolute
*(🔴 emotion inference in schools banned outright)* · Article 4 literacy live ·
🆕 **enforcement machinery on from `2026-08-02` per the Commission's own page** ·
Annex III high-risk for education at `2027-12-02`, 🔴 **with a live *"AI omnibus"* amendment
proposal from November 2025 that can move it.**
🟢 **APAC, resolved this pass:** Vietnam's Law `134/2025/QH15` in force `2026-03-01`
*(extraterritorial)* with the **education high-risk deadline at September 2027** — 🆕 **`T112`:
two dates for one law were two obligations, not a contradiction.**
🟢 **Korea: AI Basic Act in force, 2026 a pilot year with a one-year penalty grace period.**
🔵 **Consequence: a compliance engagement must be scoped to RE-READ the timeline, never to
hard-code it.**

### 8. 🆕 🔴 Supply-side trend this shelf measured itself: the licence floor is unsafe — *Global*

🔴 **`17 of 80` rows (`21.3%`) on the cleanest education topic on GitHub cannot be used by a
studio** — `15` with no licence file on 22 probed paths, `2` with a `LICENSE` that explicitly
refuses open source.
🆕 **Two of these are a NEW category for this shelf**: deliberate non-OSI grants
*(a bespoke source-available licence, and PolyForm Noncommercial 1.0.0)* 🔴 **rather than a
missing file.**
🔵 **The trend worth naming: as agent skills get cheap to publish, licence hygiene is getting
worse, and star count carries no signal about it.**

### 🔴 What this page is still missing

- 🔴 **No quotable market size, NINTH pass** — 🟢 **and now with a diagnosis: no primary study has
  been read, only restatements** *(`T114`)*.
- 🔴 **No APAC adoption RATE.** 🟡 **Sentiment only** *(Ipsos: ANZ and Asia split in opposite
  directions — `T113`)*.
- 🔴 **No EMEA-only adoption rate.** 🟡 **The `~70%` figure fuses Europe with North America.**
- 🔴 **Africa not re-queried, SECOND pass.**
- 🔴 **Canada and Mexico: nothing, SIXTH pass.**
- 🔴 **No primary legal text, EIGHTH pass** — `eur-lex` and the law-firm hosts refuse this egress.


## Pass 155 — 2026-10-12

🟢 **The trend sources and the repository evidence AGREE this pass, which is unusual enough to
state first.** 🟢 **Both say the same thing: the general-purpose chatbot is being displaced by
purpose-built, narrow, composable pieces.** 🆕 🟢 **And the repositories show the FORM that
displacement is taking, which no trend source names: the skill.**

### 🟢 What the trend sources say, 2026

| trend | what it says | 🔵 what it means for a studio |
|---|---|---|
| 🟢 **Purpose-built over general-purpose** | General chatbots created work for teachers — prompt-crafting and accuracy checking. The field is moving to education-designed tools | 🟢 **Sell a narrow, evaluated tool, not "AI in your LMS"** |
| 🟢 **Agents and real-time adaptation** | Agents handling multi-step tasks; adaptive systems adjusting difficulty live; multimodal | 🟢 **`SenmuuuuW/universal-diagnostic-tutor-skill`'s diagnose-first shape is this trend in 1 102 bytes of MIT** |
| 🟢 **Evidence demanded before purchase** | Buyers want rigorous proof of instructional benefit, not personalisation promises | 🔴 **A demo does not close in 2026.** 🟢 **Ship an evaluation harness with the pilot** |
| 🟢 **Governance structures** | Institutions building AI strategies with governance and compliance checks | 🟢 **IESALC's 87%-doing / 26%-governing gap is this trend with a number on it** |
| 🟢 **Digital credentials, skills-based pathways** | Credentials gaining ground as employer expectations shift | 🟡 **Unserved on this shelf** — no credentialing repo found in 155 passes. 🔵 **`ACTION HE`** |

### 🆕 🔵 The trend the sources miss — `T98`, the skill as a distribution form

🔴 **Not one trend source read this pass mentions it.** 🟢 **Six of the fifteen new
`topic:ai-tutor` rows are skills rather than applications**, and a seventh
([`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom), 283 ★) ships **both**.

🔵 **Why it is a trend and not a curiosity:**

- 🟢 **The economics are different in kind.** No runtime, no database, no deployment: text plus
  a manifest, inheriting the host agent's model, memory and tools. 🟢 **Delivery cost
  approaches zero and the pedagogy is the whole product.**
- 🟢 **The licensing question collapses.** 🟢 **`1 062–1 102 B` of MIT** for six rows, against
  🔴 **34 514 B of AGPL** for the self-hosted app ([`artcc/freelingo`](https://github.com/artcc/freelingo))
  in the same topic. 🔵 **Same domain, opposite legal weight, chosen by FORM.**
- 🟢 **It is where the attention is.** Four skill rows sit between **243 and 304 ★** — above
  [`Selleo/mentingo`](https://github.com/Selleo/mentingo)'s 92 ★ for a full AI-native LMS.
  🔵 **A pedagogy in a text file is out-starring a platform.**
- 🔴 **And the ceiling is real.** A skill cannot hold a FERPA audit log, cannot be a data
  controller, cannot satisfy an EU AI Act deployer duty. 🟢 **Which is exactly why it composes
  rather than competes — `P49`.**

### 🆕 🔴 `T95` CORROBORATED and SHARPENED — the discovery problem is a RANK problem

[`evidence/topic-channel-census.2026-10-12-p155.tsv`](../evidence/topic-channel-census.2026-10-12-p155.tsv)

| topic | repos GitHub reports | rows read | on-domain | rate |
|---|---|---|---|---|
| 🟢 **`ai-tutor`** | **684** | 20 | **19** | 🟢 **95%** |
| 🔴 **`education`** | **37 086** | 20 | 🔴 **1** | 🔴 **5%** |

🟢 **p154 measured `topic:ai-tutor` at 93% on the authenticated API; this pass measures 95% on
the unauthenticated public page — independent instrument, same answer.** 🟢 **`T95` holds.**

🔴 **But p154's 50% for broad `topic:education` does NOT reproduce: the public page, sorted by
stars, gives 5%.** 🟢 **The explanation is the sort, and it is more useful than the number
was.** 🔴 **The star-sorted head of `topic:education` is DEVELOPER CURRICULUM** —
`freeCodeCamp` (457k), `free-programming-books` (399k), `TheAlgorithms/Python` (225k),
`You-Dont-Know-JS` (185k), `hello-algo` (131k), Microsoft's `*-For-Beginners` courses.
🔴 **The single on-domain row in the top twenty is `JushBJJ/Mr.-Ranedeer-AI-Tutor` (29.6k) —
and it is a PROMPT, not software.**

🔵 **So the ten-pass agent-search null streak has a mechanism, not just a vocabulary:**
🔴 **GitHub's "education" population IS developer education, and ranking it by stars buries
education-SECTOR software under teaching-material repositories forever.** 🆕 **`T102`: in a
topic whose name a second community owns, the star sort is not a relevance sort — it is a
handover to the larger community.** 🟢 **The fix is lexical precision, not more reading:
`ai-tutor` at 684 repositories is a tractable population; `education` at 37 086 is not a
population at all.**

##### 🔴 What this page still cannot do, after p155

- 🔴 **`664` of `684` `ai-tutor` repositories are unread.** 🟢 The population is now sized and
  the channel is free. 🔵 **`ACTION HF`.**
- 🔴 **No sibling topic measured** — `ai-education`, `edtech`, `learning-analytics`,
  `knowledge-tracing` are unqueried, so 🔴 **nobody knows whether `ai-tutor` is the only clean
  term or merely the first one tried.** 🔵 **`ACTION HG`.**
- 🔴 **The credentialing / skills-pathway trend has NO repository on this shelf** (`ACTION HE`).
- 🔴 **Evidence-and-evaluation is a named buyer demand with no evaluation harness on this
  shelf** beyond `pyKT`'s modelling. 🔵 **`ACTION HH`.**


## Pass 154 — 2026-10-12

⏱️ **Seventeenth pass of this date.** 🟢 **Four theses, `T92`–`T95`, and three of them come
from a channel this shelf had written off twice.** 🟢 **`T95` finally EXPLAINS the agent-search
null streak without blaming the search engine** — the education domain's own vocabulary is
owned by machine learning, and the number is 93% versus 27%.
🔴 **`T92` says something this shelf's whole licence model cannot express: a licence can
belong to a DIRECTORY.**

| finding | verdict |
|---|---|
| 🆕 🔴 **`T92`** | 🔴 **A licence can be a property of the PATH, not of the repository.** `scibly` is AGPL-3.0 at its root and proprietary inside `ee/` |
| 🆕 🔴 **`T93`** | 🔴 **`updated_at` is not `pushed_at`.** `lumen`'s metadata moved **115 days** after its last code push; a freshness claim read from the wrong field overstates liveness |
| 🆕 🔴 **`T94`** | 🔴 **`git ls-remote <url> HEAD` can return MORE THAN ONE LINE.** `i-educar` advertises `refs/remotes/origin/HEAD`, so an instrument that takes "the SHA" takes two |
| 🆕 🟢 **`T95`** | 🟢 **In education, the TOPIC index is clean and the free-text index is not** — `topic:ai-tutor` **93%** on-domain against free text's **27%**, because `learning` and `teaching` are ML words first |
| 🟢 **the API licence field, tested against a known liar** | 🟢 **It sided with the TREE.** On `lumen` — badge MIT, `pyproject.toml` MIT, `LICENSE` GPL-3.0 — the API says **GPL-3.0** |
| 🟡 **`T89`'s contradiction rate** | 🟡 **Still 1 of 10 on one tier.** 🟢 The channel that makes the other 52 rows affordable now exists (`ACTION GM`) |

### 🆕 🔴 `T92` — a licence can belong to a DIRECTORY

🔴 **Every instrument on this shelf reads one root `LICENSE` and assigns one licence to one
repository.** `scibly-dev/scibly` breaks that model in the most ordinary way possible: its
root body is **34 739 B** and contains **AGPL-3.0 verbatim**, preceded by one paragraph that
carves out `ee/` and points at a second licence file — **1 287 B**, *"Scibly Enterprise
License … licensed, not sold … non-production purposes only."*

🔵 **Why the shelf's own gates would have missed it.** 🟢 `P44` reads the body, not the badge —
correct, and insufficient. 🟢 `P44` step 4 checks the body SIZE against the family — and
**34 739 B sits inside the AGPL band, so the check PASSES and confirms a conclusion that is
only true for part of the tree.** 🔴 **A size check validates which licence TEXT was pasted
in. It cannot see the sentence above it.**

🟢 **What caught it was `NOASSERTION`** — GitHub's detector declining to classify a file it
could not match. 🔵 **So the open-core pattern has a machine-readable fingerprint**, and
`P47` is built on it.

🔴 **The commercial consequence, stated plainly**: a studio that forks an open-core education
platform and ships `ee/` code to a client's production system has breached a licence that its
own licence scanner reported as AGPL-3.0.

### 🆕 🔴 `T93` — `updated_at` is not `pushed_at`, and the gap is months

| field, on `ahmedEid1/lumen` | value | what moves it |
|---|---|---|
| `pushed_at` | **2026-06-07** | 🟢 **a commit** |
| `updated_at` | **2026-09-30** | 🔴 **a star, a description edit, a topic change, a rename** |

🔴 **115 days apart.** 🟢 **So "last updated 2026-09-30" is TRUE and means nothing about the
code.** This shelf publishes freshness columns; from this pass they read `pushed_at`, and the
p153 row that reported `DeepTutor` as "2026-10-08" should be read as a measurement DATE, not a
push date.

🔵 **Why it generalises past one field name.** 🟢 **`T39`'s rule one level down: an exclusion —
or a freshness claim — is sound only relative to the property actually measured.** A liveness
claim built on `updated_at` measures ATTENTION, not maintenance, and those came apart by four
months on the first row tested.

### 🆕 🟢 `T95` — the null streak was a VOCABULARY collision, and here is the number

[`evidence/channel-precision.2026-10-12-p154.tsv`](../evidence/channel-precision.2026-10-12-p154.tsv)

| channel | on-domain software in the top 30 |
|---|---|
| 🟢 `topic:ai-tutor` | 🟢 **93%** |
| 🟢 `topic:edtech` | 🟢 **90%** |
| 🟡 `topic:education` + `topic:ai-agents` | 🟡 **50%** |
| 🔴 free text `education OR tutor OR learning OR teaching` | 🔴 **27%** |

🔴 **`learning`, `teaching`, `tutorial` and `curriculum` are machine-learning and
developer-documentation words first.** The free-text sweep's top 30 by stars returned
`JEPA-Anything`, `GPT-Policy`, `RoboICL`, `VisionHOPE`, `DeepEP-Ascend` — and a **desk lamp**
*"learning to be more than a lamp"*.

🟢 **This is the first explanation of the ten-pass null streak that does not blame the search
engine**, and 🔴 **it also refuses the easy fix**: the broad `education` topic scores **50%**,
because course repositories claim it too. 🟢 **The instruction that survives is NARROW TOPIC,
never free text, and never the broad topic.**

### 🟢 Market and sector trends this pass, with their publisher class attached

| trend | evidence | class |
|---|---|---|
| 🆕 🔴 **The learner-modelling layer is half UNGRANTED** | 10 of the top 20 `knowledge-tracing` repositories carry no licence file — including SAINT, SAKT, DTransformer and ATKT. 🟢 **9 MIT, 1 Apache-2.0, ZERO copyleft** | 🟢 **PRIMARY — measured on 20 repositories this pass** |
| 🆕 🔴 **The grading layer is the INVERSE: copyleft-heavy** | Of 11 assessment rows: 2 permissive (`nbgrader` BSD-3, `pedal` MIT), 6 copyleft, 2 `NOASSERTION`, 1 ungranted | 🟢 **PRIMARY — measured this pass** |
| 🆕 🔵 **APAC education AI is arriving as a RETROFIT from below** | `AI-Marker-Suite` automates marking on 24 named Chinese exam platforms as a userscript; `BetterSEQTA-Plus` is a student-built extension over a commercial school platform | 🟢 **PRIMARY — repositories, not commentary** |
| 🆕 🔴 **Education-specific FOUNDATION MODELS have appeared, and the first one has no grant** | `haolpku/Omni-Edu`, *"Open Foundation Models for Learning and Teaching"*, **225 ★**, 🔴 **no licence file on 8 probed paths** | 🟢 **PRIMARY** |
| 🟢 **Away from general-purpose chatbots, toward education-specific tooling** | Carried from p153; the OECD's 2026 Digital Education Outlook reaches it by another route | 🟡 vendor/analyst + 🟢 OECD |
| 🟢 **Evidence demands on vendors are hardening** | Carried. 🆕 **And it is now visible in code**: `bydeng01/ability-levels-audit` and `bydeng01/conv-vs-ped-tutor` are **pre-registered LLM-judge audits** of tutor helpfulness and answer leakage, with frozen data | 🟢 **PRIMARY for the code; 🟡 analyst for the claim** |
| 🟢 **Governance structures are being BUILT, not debated** | 1EdTech, carried. 🆕 Corroborated from the other side by IESALC's **26%** formal-framework figure | 🟡 standards body + 🟢 UNESCO |
| 🔴 **The teacher-hours claim** | *"teachers adopt AI most readily when it saves 5–10 hours/week"* | 🔴 **vendor claim, STILL NOT ADOPTED** |

🔵 **The two licence findings together are the commercially sharpest thing on this page.**
🟢 **A studio's adaptive-learning stack is permissive at the top (tutors: 52% MIT/Apache over
248 rows) and at the modelling core (`pykt`, `pyedmine`: MIT)** — 🔴 **but the SOTA models it
will be asked for by name are ungranted, and the grading layer it must integrate is copyleft.**
🟢 **So the defensible architecture is: permissive substrate, reimplemented models, and
grading reached over a boundary rather than forked** — which is `P46`, `P47` and p153's `P43`
pointing at the same answer from three directions.

##### 🔴 What this page still cannot do, after p154

- 🔴 **`T55` and `T20` are STILL undefined** (`ACTION GP`, carried from p153, unpaid again).
- 🔴 **`T48` is still a dead id** and still not retired, for `T61`'s reason.
- 🔴 **No bilingual sweep of the lexical gates** (`T91`, `ACTION GO`) — carried, not run.
- 🔴 **`T94`'s fix is named but not applied** to `P45`'s published recipe.
- 🔴 **`T92` is a single instance.** One repository proves the pattern exists; it does not
  measure how common it is. 🔵 **`ACTION GS`**: probe the 32 `NOASSERTION` rows for `ee/`-style
  carve-outs.
- 🔴 **Every market trend above that is not marked PRIMARY is secondary** and carries its class.

### 🔵 Actions open after p154

| id | what it asks | why it is affordable now |
|---|---|---|
| 🔵 **`GQ`** | finish the API licence/star reading on the 4 audited rows not reached | 4 calls |
| 🔵 **`GM`** *(carried)* | surface-audit the 44 connector + 8 npm rows | 🟢 **the API makes it ~1 call per owner instead of 52 clones** |
| 🔵 **`GS`** | probe the 32 `NOASSERTION` rows for path carve-outs (`T92`) | 1 raw fetch per row |
| 🔵 **`GU`** | body-read the 11 grading rows and `advisingapp` before any is quoted | 12 raw fetches |
| 🔵 **`GV`** | run the `pushed_at` freshness analysis over the 248-row population | data already in the TSV |
| 🔵 **`GW`** | run `tsugi` against a live Moodle/Canvas and test the LTI claim | a container |
| 🔵 **`GX`** | settle `i-educar`'s GPL-2.0 election (`-only` vs `-or-later`) | notice-header sweep |
| 🔵 **`GY`** | query APAC education MINISTRIES directly | search, different channel |
| 🔵 **`GT`** | find whether any Spanish/Portuguese `topic:` value has a population | 2 calls |
| 🔵 **`GJ`** *(carried, partly paid)* | DEC countries + fieldwork dates | 🔴 **blocked: host unresolvable on two channels** |
| 🔵 **`GO`, `GP`, `GF`** *(carried)* | bilingual gate sweep · define/retire `T55`+`T20` · vendored-file exclusion | unchanged |

## Pass 153 — 2026-10-12

⏱️ **Sixteenth pass of this date.** 🟢 **`ACTION GC` is DISCHARGED and it corrects this
shelf's own headline about its own bookkeeping.** 🆕 **Three theses, `T89`–`T91`.**
🔴 **And a star distribution refutes the reading this page has published for two passes.**

| finding | verdict |
|---|---|
| 🟢 **`ACTION GC`** | 🟢 **DISCHARGED. The "17 undefined theses" are 6 RECOVERABLE + 11 ABSENT** — and 🔴 **`T39`, the face of the debt for two passes, is the BEST of the 17** |
| 🆕 🔴 **`T89`** | 🔴 **A repository can CONTRADICT ITSELF about its own licence.** 1 of 10 agent-tier rows does, and the contradiction UNDERSTATES copyleft |
| 🆕 🟢 **`T90`** | 🟢 **A licence identifier is an ENCODED STRING, not a token** — shields.io escapes `-` as `--`, and a matcher that does not decode it invents a disagreement |
| 🆕 🟢 **`T91`** | 🟢 **A prose-language change can silently break an instrument.** The shelf renamed `## Pase N` to `## Pass N` and its own attributor stopped attributing — **50 occurrences**, no error raised |
| 🔴 **the "governance is uncorrelated with attention" reading** | 🔴 **REFUTED and REPLACED by something sharper** — the agent tier's star median is **24–26.5**, not ≤10, so the governed row is an **INVERSION** below the tier, not a sample of it |

### 🟢 `ACTION GC` — the 17 "undefined" theses, resolved, and the shelf's headline corrected

[`evidence/thesis-resolution.2026-10-12-p153.tsv`](../evidence/thesis-resolution.2026-10-12-p153.tsv)

🔵 **The register's grammar is right and its HEADLINE is misleading.** A `DEFINITION` is a
bare-id statement that does not open with a revisit verb. Six of the seventeen have a
perfectly stable statement on an in-scope, non-append-only page — **but only ever inside a
revisit** (`HELD`, `GENERALISED`, `STRENGTHENED`, `VINDICATED`). The grammar reads that as
absent, correctly. 🟢 **So the debt is a FIRST-MENTION debt, not a meaning debt**, and the
two are worth very different amounts of worry.

| 🟢 **RECOVERABLE — 6** | cited | the statement, identical across every citation |
|---|---|---|
| **`T39`** | **36×** | *an exclusion is sound only relative to the property measured* |
| **`T57`** | 17× | *a legislative tracker's status field is not a legal fact* |
| **`T59`** | 16× | *an instrument's TRAVERSAL CHANNEL is part of its reach* |
| **`T38`** | 14× | *a `gated=0` means "no gate in the same file"; a lexical detector cannot see a cross-module gate* |
| **`T60`** | 7× | *the channel map is not stable across passes, so it must be re-measured, not assumed* |
| **`T61`** | 7× | *a register's NUMBER SPACE is part of its data* |

🔴 **The correction.** p151 and p152 both led with *"`T39` is cited 24 times and defined
nowhere"*, making `T39` the face of the documentation debt. 🟢 **`T39` is the healthiest
item on the list** — restated identically **36 times**, never ambiguous, never contested.
🔴 **The real debt is `T55`: cited 10 times, and no statement text exists anywhere on the
shelf.** Then `T20` (7×). 🔴 **And `T48` is cited ZERO times — a dead identifier occupying
a register slot.**

| 🔴 **ABSENT — 11** | note |
|---|---|
| 🔴 **`T55` (10×)**, **`T20` (7×)** | 🔴 **The actual debt. Nothing to recover; these must be WRITTEN or RETIRED** |
| `T52` (3×), `T19` (2×), `T49`, `T51`, `T54` (1× each) | low-citation, low-cost to retire |
| 🔴 **`T48` (0×)** | 🔴 **a dead id** |
| `T47` (3×), `T50` (4×), `T53` (3×) | 🔴 **this pass's matcher FALSELY captured an id enumeration as a statement on all three** |

🔴 **A declared defect in the measurement, found before publication.** On `T47`, `T50` and
`T53` the statement regex matched a **list of other identifiers** (`` `T55`, `T57`,
`T59`–`T61` ``) and reported it as a definition — **3 false captures of 17**. 🟢 They are
corrected by hand in the class column and 🔴 **the regex is deliberately NOT committed as
an instrument**, because a matcher with a 1-in-6 false-capture rate is not one. 🔵 **This
is `T39` applied to the thesis register itself**: the exclusion *"has a statement"* was
sound only relative to the property *"text follows an em-dash"*, which is not the property
wanted.

🔴 **What `GC` does NOT settle.** Its falsifier — *refuted if any of the 17 is defined on a
page this pass's scope missed* — 🔴 **was not tested**: the scope was the same 10 files
p151 used. 🟢 **Not claimed silent.** 🔵 **And the citation counts here are HIGHER than
p151's** (`T39` 36 vs 24, `T57` 17 vs 13) because this instrument counts the backticked id
over all 10 files including `README.md`. 🟢 **Two denominators, not a correction** —
`P42`'s rule.

### 🆕 🔴 `T89` — a repository can contradict itself about its own licence

🔴 **`ahmedEid1/lumen`: the `LICENSE` file is GPL-3.0; the README badge and the backend
`pyproject.toml` both say MIT.** Three surfaces, two wrong, and the wrong ones are the two
a human reads first.

🔵 **Why this is a thesis and not an anecdote.** The shelf has had a rule since p138 —
*read the licence from the tree, never from a badge* — 🔴 **and it was a precaution with no
instance behind it.** 🟢 **Now it has one, and the error direction is the dangerous one**:
the contradiction makes copyleft look permissive. The opposite mistake wastes a meeting;
this one obliges a rewrite.

🔴 **And the same pass found a SECOND self-disagreement in a different field:**
`vishalsachdev/canvas-mcp`'s sidebar advertises **102 tools** and its README body says **up
to 126**. 🟢 Not a licence fault, so not counted in `T89`'s rate — 🔵 **but the same class,
on the same channel, in the same hour.** 🔴 **`T89`'s rate is 1 of 10 on ONE tier**; the 44
connector rows and 8 npm rows were not audited, so it is not a shelf-wide figure
(`ACTION GM`).

### 🆕 🟢 `T90` — a licence identifier is an encoded string

🔴 **This pass's own instrument published a false `DISAGREE`** on
`zavora-ai/mcp-student-records`, whose badge reads `license-Apache--2.0-blue.svg`.
shields.io escapes a literal hyphen as `--`; a non-greedy capture stopped at the first one
and read **`Apache`**, a different family from **`Apache-2.0`**. 🟢 **Decoded, tested four
ways, re-run: the row is `AGREE`.**

🔵 **The general form, and it is cheap to state and expensive to learn:** a licence id read
off a rendered surface has been through an encoding — URL-escaping, badge-escaping,
Markdown. 🟢 **Decode before comparing, or the instrument manufactures disagreements** —
which is `T39`'s lesson one level down, and the second time in two passes that a gate's
only demonstrated catch was in the prose of the pass that ran it.

### 🆕 🟢 `T91` — a prose-language change can silently break an instrument

🔴 **The shelf renamed its own pass headings from `## Pase 138` to `## Pass 152`. Its
star-figure attributor matched `r'pase (\d+)'` — case-insensitively, which does not help,
because `Pass` is not `Pase`.** Result: **50 occurrences with no pass attributed**, and
🔴 **no error, no warning, no failing assertion that said so** — the suite reported *"a
pass heading in a format the regex does not cover"*, which is how p152 recorded it.
🟢 **It was not a format. It was a LANGUAGE**, and naming it that way is what made it a
one-line fix: `r'(?:pase|pass) (\d+)'`.

🔵 **Why this generalises past a typo.** This KB writes in two languages by design — its
instruments, patterns and older pages are Spanish, its recent passes English. 🔴 **Every
lexical gate on this shelf is therefore a bilingual gate whether its author knew it or
not**, and the ones that match Spanish marker words (`MARCAS_UMBRAL`, `MARCAS_RECHAZO`,
`MARCAS_BANDA_ADOSADA`) are **silently degrading as the prose shifts**. 🟢 **That is a
sweep worth running** — 🔵 **`ACTION GO`**.

### 🔴 The reading this page must withdraw, and the better one that replaces it

🔴 **WITHDRAWN:** *"stars measure attention, not governance"*, as published at p152 on the
strength of one row at 1 ★.

🟢 **REPLACED BY, on ten measurements:** the education-agent tier's star median is **24**
(all ten rows) or **26.5** (the six-row tier), with a top row at **290 ★**. 🔴 **So the
tier is not ignored.** 🟢 **And the single best-governed row on this shelf — 23
approval-gated writes, FERPA-logged mutations, a 24-test suite — is ninth of ten at 1 ★,
which puts it UNDER the tier it belongs to, not level with it.**

🔵 **The sentence that survives a client's scrutiny**: *"the row with a real authorisation
boundary ranks ninth of ten by stars, in a population whose median is 24 — so a
stars-first shortlist does not merely miss it, it ranks it last."* 🟢 **That is a stronger
claim than the one it replaces and it was produced by a falsifier FIRING**, which is the
third time this shelf has gained from a refutation rather than a discharge.

### 🟢 Market and sector trends this pass, with their publisher class attached

| trend | evidence | class |
|---|---|---|
| 🟢 **Away from general-purpose chatbots, toward education-specific tooling** | Multiple 2026 sources; one reports teacher prompt-crafting and output-verification **shifted** cognitive load from lesson planning to AI supervision rather than reducing it | 🟡 vendor/analyst blogs — 🟢 **but the OECD's 2026 Digital Education Outlook reaches the same conclusion by another route** |
| 🟢 **Agents and multimodal over single prompts** | Analyst commentary describes the frontier moving to multi-step agentic task execution | 🟡 secondary |
| 🟢 **Governance structures are being BUILT, not debated** | 1EdTech: institutions defining governance, clarifying compliance, establishing evaluation processes | 🟡 standards body |
| 🟢 **Evidence demands on vendors are hardening** | Systems increasingly require proof that a product improves learning quality, persistence, well-being or job-relevant skills | 🟡 analyst |
| 🟢 **Skills and portable credentials** | 1EdTech on digital credentials accelerating a skills-driven ecosystem; micro-credentials and verifiable badges | 🟡 standards body |
| 🔴 **The teacher-hours claim** | *"teachers adopt AI most readily when it saves 5–10 hours/week"* | 🔴 **vendor claim, NOT adopted** |

🔵 **Why the first row is the one that matters commercially**: it is the market's own
version of `P43`. 🟢 **If general-purpose tooling shifts load rather than removing it, the
buyable thing is a composed vertical stack** — a substrate plus an agent plus a gate —
which is precisely what `compose/patterns.md` ships and what the market reports cannot name
a vendor for, **seventh pass running**.

##### 🔴 What this page still cannot do, after p153

- 🔴 **`T55` and `T20` are still undefined** — `GC` measured the debt and did not pay it.
  🔵 **`ACTION GP`**: write or retire them.
- 🔴 **`T48` is a dead id and was not retired**, because retiring an id changes a register's
  number space, which is `T61`'s own warning.
- 🔴 **`T89`'s contradiction rate is 1 of 10 on one tier.** The 44 connector rows and 8 npm
  rows are unaudited (`ACTION GM`).
- 🔴 **No bilingual sweep of the lexical gates was run** (`T91`, `ACTION GO`) — the defect
  is named on one instrument and is likely present on others.
- 🔴 **Every trend in the table above is secondary.** None is adopted; each carries its
  publisher class.

## Pass 152 — 2026-10-12

⏱️ **Fifteenth pass of this date.** 🟢 **Five of p151's fourteen pre-registered actions
reached, nine not** — and the nine are named. 🔴 **This pass withdraws a date this shelf has
published for five passes and used to correct the market**, and 🔴 **refutes a thesis this
shelf hardened over three passes.** 🟢 **Both were found by running a channel the shelf had
written off.**

| thesis | state | what it says |
|---|---|---|
| 🆕 🔴 **`T85`** | 🆕 **new** | **An election has THREE surface forms. The third — a complete GNU notice with the or-later clause OMITTED — is the FSF's own `-only` form, and no matcher on this shelf can read it** |
| 🆕 🔴 **`T86`** | 🆕 **new** | **An election read from a tree is not the SUBJECT's election. A bundled third-party file elects for itself, and `vendor/` does not catch where they actually live** |
| 🆕 🔴 **`T87`** | 🆕 **new** | **The star count IS measurable for an UNATTACHED third-party repository. `P151-S`'s "governs every GitHub channel" is too broad — it governs the API, not the rendered page** |
| 🆕 🔴 **`T88`** | 🆕 **new** | **A compliance date can be superseded between passes by an instrument that never names education. This shelf's Annex III date was moved six days before it fell, and five passes did not see it** |
| 🔴 **`T78`** | 🔴 **REFUTED** | Star counts are NOT unmeasurable. 🟢 **9 repositories measured this pass** across the vertical and agent tiers, none attached to this session |
| 🟢 **`T81`** | 🟢 **CONFINED, as `ACTION GA` asked** | 3 of 6 verticals state an election. 🟢 **And the small rows' silence has a THIRD cause**: all 17 of their notice-bearing files never reach a version |
| 🟢 **`T84`** | 🟢 **HELD, third direction** | The generic query returned 4 curricula again. 🟢 **The query naming `moodle`/`canvas`/`LMS`/`tutor` returned two real education-sector repos** |

### 🆕 🔴 `T85` — the election by OMISSION, which is the pass's sharpest finding

| claim | 🔴 **A complete GNU notice that does NOT continue into "or (at your option) any later version" has elected the stated version only — and this shelf reads it as SILENCE.** |
|---|---|
| **the measurement** | **16 896** files in `instructure/canvas-lms` (of **19 286** scanned, **16 905** notice-bearing — **87.7%**, the highest notice rate on this shelf) carry *"as published by the Free Software Foundation, version 3 of the License."* 🔴 **0 say "or later". 0 say "only".** |
| **why both p151 matchers miss it** | `ELECTION_LATER` needs the or-later clause, which is absent; `ELECTION_ONLY` needs the literal word `only`, which was never written. 🔴 **Asserted as a test, not described** |
| **why it is `T77`'s class a third layer down** | `T77`: a licence cannot be identified from its body. `T81`: the election cannot be read from a body. 🆕 **`T85`: the election can be stated by ABSENCE, so a matcher that only looks for presence cannot see it** |
| **what would overturn it** | 🔴 An Instructure statement that the per-file notice is not an election, or an or-later clause anywhere in the tree. 🟢 **An independent second channel already points the same way**: `openedx/edx-platform`'s README says *"version 3 of the AGPL unless otherwise noted"* |
| **what it changes in a room** | 🔴 *"It's AGPL, the election is unstated, we'll ask"* is wrong for Canvas. 🟢 **A Canvas fork is AGPL-3.0-ONLY**; a Moodle fork does have the or-later route. 🔵 **That is a decision input between the two platforms this shelf could not state before** |
| instrument | [`p152-vertical-election`](../compose/code/p152-vertical-election/README.md), **25 tests** |

### 🆕 🔴 `T86` — a vendored file elects for itself

| claim | 🔴 **`sakaiproject/sakai` is ECL-2.0 and this pass's instrument read it as GPL-`-or-later`, because a bundled library said so.** |
|---|---|
| **the measurement** | **1** hit in **11 620** files: `library/src/webapp/js/trimpath-template-latest.js`, *"TrimPath Template … Copyright (C) 2004, 2005 Metaha"*, dual GPL-2.0-or-later / Apache-2.0. 🔴 **Not Sakai's code.** Same shape at `openedx/edx-platform`, whose only notice is `common/test/data/uploads/jschannel.js` |
| **why the exclusion list cannot fix it** | 🟢 `SKIP_DIRS` excludes `vendor/`; 🔴 **neither bundled copy is under `vendor/`.** A path-name exclusion is the wrong instrument for a provenance question |
| **the signal a fix must read** | 🟢 **The notice's own copyright holder.** `Metaha` is not `sakaiproject`, and that comparison is available in the same eight kilobytes already being read |
| **what would overturn it** | 🔴 A holder-matching pass that changes no verdict — which would mean bundled notices are rare enough to ignore. 🔵 **Prediction: it will change at least `sakai` and `edx-platform`** |
| **what it changes on this shelf** | 🔴 **Every per-file licence figure this shelf has published counts vendored files.** 🟢 The verdict on `sakai` is published KNOWN-WRONG rather than dropped, so the defect stays visible. 🔵 **`ACTION GF`** |

### 🆕 🔴 `T87` — the star count was never unmeasurable, and the shelf said it three times

| claim | 🔴 **`https://github.com/<owner>/<repo>` renders stars, forks and the sidebar licence for a repository that is NOT attached to this session. 9 measured this pass.** |
|---|---|
| **the measurement** | **6 verticals** — `moodle` **7.5k**, `canvas-lms` **6.9k**/3.0k, `edx-platform` **8.2k**/4.4k, `bigbluebutton` **9.2k**/6.0k, `sakai` **1.2k**/1.0k, `kolibri` **1.1k**/1.0k — plus **3 agent-tier rows**: `zijinz456/OpenTutor` **140**★/30, `BetterSEQTA/BetterSEQTA-Plus` **40**★/25, `zavora-ai/mcp-student-records` 🔴 **1**★/0 |
| **the oracle test, because a channel that cannot fail is not a channel** | 🟢 **It DISCRIMINATES**: `moodle/moodle` returns 7.5k; `moodle/moodle-definitely-not-a-real-repo-p152` returns **HTTP 404**. 🔵 This is `p93`'s channel, recorded in this shelf's own README and then written off at p150 |
| **what `P151-S` got wrong** | 🔴 **"It governs every GitHub channel including `WebFetch`."** It does not. 🟢 **It governs `api.github.com/repos/…` and `/search/…`**, which is what was actually refused; the rendered HTML page is served |
| **the bonus the action did not ask for** | 🟢 **6 of 6 sidebar licences AGREE with this shelf's hand-read vertical licences** — a second independent licence channel, free, in the same nine fetches |
| 🔴 **the figure that stings** | `zavora-ai/mcp-student-records` — the **best-governed row on this shelf** (23 approval-gated writes, FERPA logging, 24 passing tests, three passes of instrument work) has **ONE STAR**. 🔵 **Stars measure attention, not governance, and now this shelf can show it rather than assert it** |
| **what would overturn it** | 🔴 The channel failing on a repository that exists. 🟢 9 of 9 answered this pass |

🔵 **The lesson is `ACTION GE`'s, arriving one pass after it was registered.** p151 wrote
*"permanently"* about an environment limit, withdrew the word, and then still published
*"every GitHub channel"* — 🔴 **a narrower overstatement of the same kind.** 🟢 **The rule
that survives: name the exact URL that was refused and the exact URL that answered. Never
generalise to a "channel".**

### 🆕 🔴 `T88` — the Annex III date this shelf has been correcting the market with is WITHDRAWN

| claim | 🔴 **`2026-08-02` is no longer the date Annex III obligations apply to education. It is `2027-12-02`, moved by a regulation that entered into force SIX DAYS before the old date fell.** |
|---|---|
| **what moved it** | **Regulation (EU) 2026/1744**, the *Digital Omnibus on AI*. 🟢 Parliament **2026-06-16** · Council **2026-06-29** · OJ **2026-07-24** · in force **2026-07-27** |
| **the new dates** | 🟢 **Annex III high-risk (which includes education and vocational training): `2027-12-02`**, from `2026-08-02`. 🟢 Annex I embedded products: **`2028-08-02`**. 🟢 Regulatory sandboxes: `2026-08-02` → **`2027-08-02`** |
| 🔴 **what did NOT move** | **Article 50 transparency is not delayed.** 🟡 One source puts Art 50(2) watermarking at **`2026-12-02`** for systems already on the market at `2026-08-02` — 🔴 **carried as one publisher only, not as this shelf's figure** |
| **why five passes missed it** | 🔵 **The omnibus never says "education".** It moves an annex; education is inside the annex. 🔴 **Every query this shelf ran named education, so the instrument that moved the date was invisible to all of them** |
| 🔴 **how bad the exposure was** | 🔴 **This shelf used `2026-08-02` to CORRECT the market** — *"cinco instancias en cinco pases significa que la fecha equivocada es la lectura MAYORITARIA del mercado"*. 🔴 **The shelf was giving a superseded date with the confidence of a correction** |
| **provenance, stated plainly** | 🔴 **No primary text and no fetchable secondary.** `eur-lex.europa.eu`, `gibsondunn.com`, `orrick.com`, `lewissilkin.com`, `uniwise.eu`, `legal500.com` and `artificialintelligenceact.eu` all refuse — 🟢 **the same `ENOTFOUND`/`CONNECT 403` event p151 established as one thing.** 🟢 **What carries it: nine independent publishers agreeing on the regulation NUMBER, both annex dates, the OJ date and the in-force date** — a convergence this shelf has never had on a market figure |
| **what would overturn it** | 🔴 The OJ text showing a different number or date, or confirmation the omnibus was not published. 🟡 **One source holds that until OJ publication the August baseline stands** — and three others name the OJ date, so that reservation is read as pre-publication commentary |
| **what it changes in a room** | 🟢 **An education client has 14 more months, not a passed deadline.** 🔴 **And the Art 50 transparency duties were never delayed**, so a chatbot or a generated-content feature is the live obligation while assessment and admissions are the 2027 one. 🔵 **That inversion is the pitch** |

### 🟢 `ACTION GD` — the five red suites, re-run; one REPAIRED, one CLASSIFIED, p151's triage corrected

> 🔴 *Refuted if any of the three stale assertions is not stale but WRONG.* 🔴 *And refuted
> differently if `p471` does not terminate because it is waiting on the network.*

🟡 **Partially reached: all five re-run and diagnosed, one repaired, three not.** 🔴 **And
p151's triage under-counted two of them.**

| suite | p151 published | 🟢 **p152 measured** |
|---|---|---|
| `p213-envelope-aad` | `ModuleNotFoundError: No module named '_cffi_backend'` | 🟢 **CONFIRMED as the root cause, and REPAIRED** — skips with the diagnosis, exit **0**. 🔴 Two faces of one fault: the system `cryptography` turns it into `pyo3_runtime.PanicException`, and a fresh wheel ships a **cpython-313** extension against a **cpython-311** interpreter. 🔴 **A pyo3 panic is not a subclass of `Exception`**, so the guard catches `BaseException` |
| `p471-gap-gate-language` | *"does not terminate within 90 s"* | 🟢 **CLASSIFIED — CPU-BOUND, not network.** `real 1m15s · user 1m13.7s · sys 0m0.1s`. 🟢 **So the second falsifier is SILENT and the shelf's "every instrument is offline" claim HOLDS** |
| `p598-register-freshness-gate` | *"`no cito verticals/` · `quedan rancias: [289]`"* | 🟢 **CONFIRMED exactly** — **56 of 58** assertions pass, 7 of 7 mutants killed, 2 failures, both as published |
| `p351-star-digit-sweep` | *"stale generation-1 count: 219 vs 254"* | 🔴 **INCOMPLETE — 6 failures of 36, in at least two classes.** Two stale counts (`219>=254`, `2!=8`) 🔴 **and three concerning one figure, `6.400 ★` at `agents/trending.md:16053`, which DOES carry a band (`K-3CIFRAS, ±50`)** — so the fault is the gate's class vocabulary, not the page |
| `p356-citation-origin` | *"`AssertionError: 8 != 15`"* | 🔴 **INCOMPLETE — 7 failures of 16**, not one assertion |
| **total** | *"150 of 155 pass"* | 🔴 **The five are not five single assertions; they are 2 + 6 + 7 + 2 + 1 failures and one skip** |

🔵 **The lesson, and it is `T82` one layer out again**: 🔴 **p151 triaged five suites by
their FIRST failure line and published that as the cause.** 🟢 **A suite's first failure is
not its diagnosis** — and the one suite whose cause p151 named most precisely (`p213`) is
the one that turned out to be exactly right.

### 🔴 Nine of fourteen actions NOT REACHED, and the cause is one thing

🔴 **`FG`, `FJ`, `FH`, `FS`, `FT`, `FW`, `GB`, `FY`, `GC`, `FX`, `FZ` — eleven registered,
five reached** (`GA`, `GD`, `GE` in part, and `FG`'s decisive datum only).
🔵 **The cause is budget, and the trade is stated**: `ACTION GA` meant six `--depth 1`
clones totalling **2.4 GB**, a re-implemented instrument with 25 tests, a reproduction
control against p151's seven rows, and a third matcher for `T85` — 🟢 **and it produced two
corrections to published readings plus a date withdrawal.** 🔴 **`FG` and `FJ` are now
unreached for a FOURTH consecutive pass, which is the worst item on this shelf.**

🟢 **`FG`'s decisive datum WAS taken, and it is a measurement rather than a prediction.**
🟢 **The 50 census subjects were re-cloned, 50 of 50 OK** (`git clone --depth 1`), and
`BetterSEQTA/BetterSEQTA-Plus` was swept at `HEAD` `47077f7` (2026-10-06) for every
region-bearing host in its tree:

| host | occurrences | region |
|---|---|---|
| `school.seqta.com.au` | **17** | APAC |
| `other.seqta.com.au` | **4** | APAC |
| `www.seqta.com.au` | **1** | APAC |
| `portal.school.edu.au` | **1** | APAC |
| `apps.sace.sa.edu.au` | **1** | APAC |

🟢 **25 of 25 are Australian. There is not one EMEA, LATAM or North America host in the
institutional or ccTLD class.** 🔴 **So the `APAC|EMEA|LATAM|North America` conflict p149
recorded cannot come from this class at all** — it comes from hosts of the classes `FG`
exists to exclude. 🟢 **`FG`'s falsifier is therefore expected SILENT on evidence, not on
hope**, and the remaining work is the role classifier itself.

## Pass 151 — 2026-10-12

⏱️ **Fourteenth pass of this date.** 🟢 **Seven of p150's twelve pre-registered actions
reached, five not** — and the five are named. 🟢 **`ACTION FF` is DISCHARGED after three
passes on the register**, which was the worst open item on this shelf. 🔴 **Two actions were
REFUTED exactly as specified**, and both refutations are more useful than a discharge would
have been.

| thesis | state | what it says |
|---|---|---|
| 🆕 🔴 **`T81`** | 🆕 **new** | **The `-only` / `-or-later` election cannot be read from a licence body, because every GNU licence states it in its own appendix** |
| 🆕 🔴 **`T82`** | 🆕 **new** | **A "dangling reference" is meaningless until the identifier SPACES and the page SCOPE are declared — this shelf has three spaces and four append-only pages** |
| 🆕 🟡 **`T83`** | 🆕 **new** | **A `pub`/private fix closes a consumer bypass and not an in-crate one, so a type-visibility control needs a CI gate beside it** |
| 🆕 🔴 **`T84`** | 🆕 **new** | **"AI education" and "education AI" are two different populations sharing one query, and the generic query returns the first** |
| 🟢 **`T77`** | 🟢 **ACTED ON** | The body matcher is retired in both modules that owned a copy; the census is re-published; **4 of 52 rows change, 0 outside the GNU family** |
| 🟢 **`T75`** | 🟢 **HELD and WIDENED** | The collision gate is green at `ids=41 collisions=0`; its mirror image now has a gate too |
| 🔴 **`T78`** | 🔴 **HELD, and the CAUSE re-read** | Star counts stay `UNMEASURED`. 🔵 The refusal is a **session repository-scope policy**, not a transport failure — it governs every GitHub channel including the MCP server, while public `git clone` is served. **50 of 50 clones, 8 of 8 `npm pack`** |

### 🆕 🔴 `T81` — the election is inside the licence that is being interrogated

| claim | 🔴 **The `-only` / `-or-later` election is UNSTATED in every GNU-family row on this shelf, and a body-surface read would have reported the opposite for all seven.** |
|---|---|
| **the measurement** | **7** subjects, **1 513** source files scanned with licence files excluded at any depth: 🔴 **0** `or (at your option) any later version` headers · **0** `-only` statements · **0** SPDX elections. 🟢 **Positive control: the same matcher over the licence BODIES fires 7 of 7** |
| **why the body is the trap** | GPL-3.0's appendix *"How to Apply These Terms to Your New Programs"* contains the recommended notice verbatim. 🔴 **So the phrase occurs in every GNU file, including one whose author elected `-only`** — `T77`'s class one layer down |
| **what would overturn it** | 🔴 A per-file notice or SPDX election in any of the seven trees. 🔵 The matcher that would find it is committed and its two near-miss defects are recorded: a **comment prefix** breaking the phrase across `"\n * "`, and a **badge image** named `license.svg` counted as a licence file |
| **what it changes in a room** | 🔴 *"It's GPL, we can take GPL-3-or-later"* is not available on this shelf. Plan against the **stated version only**, and ask the upstream author. 🟢 **`P38` step 4 now says so.** |
| instrument | [`p151-election-surface`](../compose/code/p151-election-surface/README.md), **24 tests** |

### 🆕 🔴 `T82` — a dangling reference is a property of the SCOPE, not of the citation

| claim | 🔴 **This shelf has THREE identifier spaces sharing one `P` prefix, and four of its ten content files are append-only history. Change either and the dangling count moves by two orders of magnitude.** |
|---|---|
| **the spaces** | **patterns** (headings on `compose/patterns.md`, **41** after this pass) · **module axes** (a row in a `compose/code/*/README.md`, **23**) · **pass findings** (`P138`, `P150-A`; **174** passes nameable) |
| **the scope** | 6 rewritten pages → 48 cited, 🟢 **0 dangling**. Plus `intel/open-gaps.md` → 354 cited, 🔴 **260 dangling**. Plus the trending pages and README → 745 cited, 🔴 **685** |
| **the cause** | 🔵 The **2026-10-06 reset restarted the pattern space at `P1`**, so every id the history cites belongs to a previous generation of the same space. 🟢 **A historical record, not a defect** |
| **`P240`, which started this** | 🟢 **NOT dangling. It resolves** at `compose/code/p239-table-integrity/README.md:17` — the region-column completeness axis, allocated at pass 78 after being born cited at pass 39 |
| **what would overturn it** | 🔴 A fourth space, or a cited id on a rewritten page that resolves in none of the three. 🟢 One was found and fixed in this very pass: `P263`, this KB's own *"put the question in `lib/`"* rule, had been cited in prose since pass 88 and allocated nowhere |
| instrument | [`p151-identifier-spaces`](../compose/code/p151-identifier-spaces/README.md), **25 tests** |

### 🆕 🟡 `T83` — a visibility fix closes the consumer surface and not the in-crate one

| claim | 🟡 **Making a field private closes the bypass every CONSUMER has and leaves the one the crate's own modules have, so a type-visibility control is half a control until a gate sits beside it.** |
|---|---|
| **the measurement** | `zavora-ai/mcp-student-records`: two lines (`pub store` → `store`, plus `pub fn new`) make p149's bypass test 🟢 **fail to compile** — `E0616` ×2 on the field reads, `E0451` on the struct literal — while 🟢 **the repository's own 24 tests still pass** |
| **why the consumer surface is the one that mattered** | 🔵 **A Rust integration test is its own crate.** p149 demonstrated the bypass from `tests/`, so what it demonstrated *is* what a downstream consumer can do, and `pub`/private is exactly that boundary |
| **the residual** | 🔴 `pub`/private is a **module** boundary. A future module inside the crate can still reach `self.store` and call a `pub fn` write. Closing that needs a sealed approval token in all **23** write signatures |
| **what would overturn it** | 🔴 A sealed-token patch that compiles and keeps the 24 tests green would promote this from "half a control" to "closed". 🔵 Not attempted here: it is a 23-site change to a repository this KB does not own |
| **what it changes in a room** | 🟢 Ship the two lines, and run the gate in CI for the in-crate surface. 🔴 Do not say "the data layer is closed" — say "closed to consumers, gated in CI inside the crate" |
| instrument | [`p151-approval-field-closure`](../compose/code/p151-approval-field-closure/README.md), **19 tests** |

### 🆕 🔴 `T84` — "AI education" and "education AI" are different populations

| claim | 🔴 **A query naming "education" and "AI agents" returns AI-ENGINEERING CURRICULA, not education-sector agents. 4 of 4 hits this pass were curricula or link lists; 0 were education-sector software.** |
|---|---|
| **the measurement** | 🟢 **4 of 4 clone-verified, 4 of 4 MIT.** `microsoft/ai-agents-for-beginners` — **3 510** `.md` + **2 240** `.ipynb` + **15** code files. `rohitg00/ai-engineering-from-scratch` — 2 269 code + 2 063 `.md`. `pguso/agents-from-scratch` — 17 code + 17 `.md`. 🆕 `avinash201199/free-ai-agents-resources` — 🔴 **0 code files, 2 `.md`** |
| **the symmetry with `ACTION FK`** | 🔵 p150 found the other half: the two **generic** queries returned only courses, and the one naming **`tutor`** returned the repositories. 🟢 **Same lesson from the opposite side** — the query must name the education ARTEFACT (`tutor`, `moodle`, `canvas`, `sis`), never the word "education" |
| 🆕 **a new class** | **LINK LAYER** — a row that ships **zero code files**, only a curated list. 🔵 Sibling of p150's **PROMPT LAYER** (no server, no code): both read as zero on every tool-surface instrument on this shelf, for different reasons |
| **what would overturn it** | 🔴 A generic "education AI agent" query returning an education-sector agent. 🔵 ~90 queries across eleven passes have not produced one |
| **what it changes in a room** | 🟢 These four rows are real, permissive and useful — **as training material for a studio team**, not as a starting point for a client's education product. 🔴 **They do NOT belong in `agents/top.md`** and are filed on the trending pages with the distinction stated |

### 🔵 What the thesis register now is, and what it is missing

🟢 **`ACTION FR` built it as one file** —
[`evidence/thesis-register.2026-10-12-p151.tsv`](../evidence/thesis-register.2026-10-12-p151.tsv).
🔴 **Its falsifier FIRED: there was no single committed location.** What the file shows:

| state | count |
|---|---|
| 🟢 **DEFINED** on a live page | **55** |
| 🔴 **NO DEFINITION anywhere** | 🔴 **17** — `T19`, `T20`, `T38`, `T39`, `T47`–`T55`, `T57`, `T59`–`T61` |
| 🔴 **defined ONLY on an append-only page** | **3** — `T44`, `T45`, `T46` |
| 🟡 **MULTI_STATEMENT** (collision candidates) | **5** |

🔴 **`T39` is cited 24 times and defined nowhere.** `T57` 13×, `T59` 12×, `T38` 10× — all
undefined. 🔵 **That is the same defect `ACTION FL` closed for the agent tier**, now measured
for the theses.

🟡 **And the collision count is NOT settled, with the cause named.** The 5 candidates are
section headings *about* a thesis's status rather than second definitions — `T3`'s *"what is
resolved and what is not"* is a status section, not a rival claim. 🔴 **The register carries
no `FIRST` / `REVISIT` marker**, which is precisely what the pattern gate has had since p150
and what lets it tell an amendment from a collision. 🔵 **So the measured collision count is
**0** with an instrument limitation stated rather than a number asserted.** 🔵 **`ACTION FY`.**

## Pass 150 — 2026-10-12

🔵 **Thesis high-water mark before this pass: `T76`. Next free: `T77`.** 🟢 **This pass takes
`T77`–`T80`**, computed from the register rather than assumed (`ACTION EN`'s rule, holding) —
🟢 **and this is the first pass where the same discipline is also ENFORCED on pattern numbers,
by a committed gate rather than by habit.**

| thesis | statement | the measurement behind it |
|---|---|---|
| 🆕 🔴 **`T77`** | **A licence cannot be identified by searching its body, because every GNU licence names its siblings in its own text** | GPL-3.0's §13 is **titled** *"Use with the GNU Affero General Public License"*; GPL-2.0's preamble says *"use the GNU Lesser General Public License instead"*. 🔴 **5 of 7 GNU-family rows on this shelf carry the wrong id**; 🔴 **`GPL` has been published ZERO times in 150 passes.** Fix reads the **title line** and confirms on **AGPL §13**. [`p150-gpl-affero-discrimination`](../compose/code/p150-gpl-affero-discrimination/README.md), **35 tests** |
| 🆕 🔴 **`T78`** | **A gateway returning 200 on a root endpoint is not an open channel, and a rate-limit budget is not a capability** | `api.github.com/` **200**, `/rate_limit` **200** with core **15 000** and search **30** — 🔴 **`/repos/{owner}/{repo}` and `/search/repositories` both REFUSED by the session proxy.** 🔴 **p149 read the 200 as a channel upgrade and published it.** 🟢 **`P144-X` stands as originally recorded** |
| 🆕 🔴 **`T79`** | **A repository's stated relation to its upstream is a claim; the diff is the measurement — and the claim can invert it** | `maxew6/ai-tutor-project` advertises *"deployment and extension"* of `krishna16-origin/ai-tutor`. 🟢 **Attribution true** (byte-identical `LICENSE`, upstream's holder). 🔴 **"Extension" false: 1 002 lines against 1 006, and the deleted text is the answer-position randomisation instruction** |
| 🆕 🔴 **`T80`** | **A dual-licensed repository must be measured by FILE REACH, not by which licence its badge names first** | `ishands/upstack` declares MIT for `scripts/, *.js` and CC-BY-SA-4.0 for everything else. 🔴 **MIT governs 3 files; ShareAlike governs 64 `.md` files that ARE the product.** 🔴 **Any matcher reading the first licence name in the file reports `MIT` for the whole tree** |

### 🟢 What moved in the trend picture this pass

🔵 **Four regional reads, one pattern.** The trend worth naming is not a technology — it is a
**governance deficit that is now measurable**:

| region | adoption | governance | ratio |
|---|---|---|---|
| **LATAM** | 🟢 **87%** (n=200, 19 countries) | 🔴 **26%** formal strategy | 🔴 **3.3 : 1** |
| **EMEA** | — | 🔴 **10%** of 450+ with established guidelines | — |
| **North America** | **60%** of K-12 teachers | 🟡 **~70%** have or are developing guidance | — |
| **APAC** | breadth high | 🔴 **depth shallow**; Korea's penalties in a **grace period** | — |

🟢 **This is `T56`'s "governance is the barrier" thesis, upgraded from a sector read to a
measured ratio on a named sample.** 🔵 **And it reverses the sales motion: the LATAM
institution has already deployed AI, so the offer is not adoption, it is control.**

🆕 🟡 **A second trend, from the regional sources rather than from code: restriction is now a
product constraint in North America.** NYC's moratorium through grade 8, Katy ISD's K-6 ban
from 2026–27, Oregon SB 1546 and Washington HB 2225 are all **tool-safety and
age-gating** instruments, not curriculum ones. 🔵 **A student-facing tutor can be unsellable
on policy grounds in a district while the teacher-facing and administrative surfaces stay
open** — which is an argument for building the teacher/admin surface first in that region.

🆕 🟡 **A third, and it is this KB's own reason to exist, stated as a finding**: 🔴 **not one
vendor named in any regional market source this pass is an open-source project.** The APAC
market report names Google, Microsoft, IBM, Pearson and BYJU'S. 🔵 **The shelf holds 58
measured subjects and 5 new rows that are forkable, and no market source can see them.**

🆕 🟢 **A fourth, small and concrete: the prompt layer is now a real artefact class.** Two of
the five rows found this pass ship **no server and no code** — `flysheep-ai/education-skills`
is five skill directories, `ishands/upstack` is 64 markdown files and three scripts. 🔴 **Every
tool-surface probe on this shelf returns zero against them**, and zero is indistinguishable
from unmeasured. 🔵 **`ACTION FS`** registers the probe; the axis is what the persona
**withholds**, not what it exposes.

### 🔴 Theses this pass did NOT test, and one it declines to promote

- 🔴 **`T74` is fixed, not re-litigated.** `ACTION FE` restored the ladder and moved exactly
  the three npm rows p149 predicted. 🟢 **The thesis closes.**
- 🟢 **`T75` is PROMOTED from a slip to a property.** `ACTION FM`'s gate found a **second**
  collision — `P18` naming two different patterns, both allocated in p139 — independent of
  `P32`. 🔵 **Two collisions, two passes, one cause: a number picked from memory rather than
  from the page.** 🟢 **Fixed: the orphan is now `P37`.**
- 🔴 **The ten-pass agent-search null is WITHDRAWN rather than promoted.** `ACTION FK`'s
  consequence clause offered to convert the streak into *"a measured property of the
  ecosystem"* after ~80 queries. 🔴 **It was a property of the QUERIES**: the two generic
  queries returned courses, the one naming `tutor` returned five repositories. 🔵 **Nothing is
  promoted to a thesis, because the honest reading is that this KB was asking wrongly.**
- 🔴 **No trend on this page is backed by a primary source this pass.** Every regional read is
  a secondary summary; the OECD Outlook, the UNESCO IESALC study and the IICBA/ICHEI report
  were all read through aggregators because their hosts answer **403 at CONNECT**. 🟢 **Stated
  once, at the level of the whole page, rather than row by row.**

## Pass 149 — 2026-10-12

🔵 **Thesis high-water mark before this pass: `T73`. Next free: `T74`.** 🟢 **This pass takes
`T74`–`T76`**, computed from the register rather than assumed (`ACTION EN`'s rule, holding) —
🔴 **and `T75` exists because the same discipline was NOT applied to pattern numbers.**

| thesis | statement | the measurement behind it |
|---|---|---|
| 🆕 🔴 **`T74`** | 🆕 **Two instruments can implement the same documented ladder in different orders, and the population they were tested on can hide it.** A rung order is a design decision; it must be asserted, not assumed shared | 🔴 **`p145-licence-census` is `FILE > PKG_ONLY > README_ONLY`, matching its own docstring (*"README_ONLY … weaker still"*); `p147-licence-language` inverted the last two.** 🟢 **Over the 44 connectors the two agree row for row**, because no connector carries both a manifest licence field and a README heading. 🔴 **p147 never ran the npm tier, where 3 of 8 rows carry both** — and there the inversion demotes a declared manifest licence to a prose mention. 🟢 **No licence identification changes; only the evidence class, in the weakening direction** |
| 🆕 🔴 **`T75`** | 🆕 **An identifier allocated from a high-water mark nobody re-reads will eventually name two things.** The fix is a committed collision check, not more care | 🔴 **`P32` named TWO live patterns for a pass** — p147's multilingual licence gate and p148's manifest-contract CI gate, both published, both referenced. 🟢 **Resolved: first allocation keeps the number, the later becomes `P35`.** 🔵 **The thesis register has `ACTION EN`'s computed-high-water rule and the pattern register does not** — which is why this collision happened in the patterns file and not here. 🟢 **`ACTION FM`** |
| 🆕 🔴 **`T76`** | 🆕 **A nationally-bound suffix is not an institution signal. The host's ROLE decides, and role cannot be read from the suffix** | 🔴 **Four non-institutional kinds measured over 50 clones**: platform/shortener (`youtu.be` → EMEA), 🆕 **developer tooling** (`sh.rustup.rs` → EMEA on an Australian subject, from a `curl … \| sh` line), 🆕 **news media** (**9** hosts across **4** regions in one subject, an RSS fixture list), 🆕 **government portal** (**17** `.gob.pe` hosts). 🔵 **`T70` was the first instance and was written as an incident**; this is the class. 🟢 **Excluding by host name, never by suffix** — a real `kuleuven.be` or `bg.ac.rs` must keep its placement |

### 🟢 `T67` and `T70` after this pass

| thesis | movement |
|---|---|
| 🟢 **`T67`** — a bare `.edu` is a registration date, not a country | 🟢 **PROMOTED from observation to enforced rule.** A bare `.edu` never places and is kept as a `lead`. 🔴 **And it was NOT the sole cause of the channel disagreement** — `ACTION EZ` refuted. 🔵 **Its cleanest demonstration yet**: `alejooroncoy/campus-cli` holds `dspace.mit.edu`, `utsystem.edu`, `yalecollege.yale.edu`, `www.artic.edu` **and `cv.uoc.edu` (Barcelona)** in one tree — and the old rule would have called all five North America **without raising a `CONFLICT`**, because it mapped every bare `.edu` to one region |
| 🟡 **`T70`** — no category for a platform host | 🟡 **A category exists and is too small.** 🟢 **Generalised into `T76`.** 🔴 **Five of the six hosts `ACTION FA` named could never have placed a row** — their suffixes are not in the ccTLD map — 🟢 **so `p147-npm-region`'s decision to omit repurposed suffixes was load-bearing and nobody had measured it** |
| 🟡 **`T68`** — one manifest can carry two disagreeing allowlists | 🟡 **SPLIT into two claims.** 🟢 **The two-target STRUCTURE generalises — 2 of 5** (`yourssu/soongpt-plugin`, which p148's key list could not see). 🔴 **The DISAGREEMENT does not — `librus-mcp` only.** 🔵 **Cite `T68` as the first, not the second** |
| 🟢 **`T72`** — a licence named in words, not in a token | 🟢 **CLOSED as out-of-population.** Eighteen common-title forms change **0 of 58** rows; `T72` is a Fedena-specific artefact |
| 🔴 **`T71`** — Vietnam lists education as high-risk | 🟡 **SHARPENED and still caveated.** 🟢 **Three entries named.** 🔴 **A narrowing clause is confirmed to exist and is unread** (Allen & Gledhill: *"not all AI systems used in these sectors will automatically be classified as high-risk"*), and 🔴 **primary text is 403 at this environment's gateway** |

### 🔴 A new defect class for this shelf: the derived figure nobody re-derived

🔴 **`P149-A`: p148 published, twice, that Vietnam's 2027-03-01 is "twenty-one months earlier"
than the EU's 2027-12-02. It is nine.** 🔵 **The arithmetic that yields 21 is
`2026-03-01 → 2027-12-02`** — a year transposed in an intermediate step.

🟢 **No source was wrong and no date was wrong.** 🟢 **Every date p148 published reproduces.**
🔴 **Only the subtraction did not** — and 🔴 **it failed in the inflating direction**,
overstating Vietnam's regulatory lead by twelve months, which is the direction that makes the
APAC pitch sound more urgent.

🔵 **This is a third class, distinct from the two this shelf already tracks.** `T73` is the
**unsourced** figure. `T63`/`T72` are the **mis-read** figure. 🆕 **This is the figure whose
inputs are all correct and whose derivation is not** — and 🔴 **no citation check can catch
it**, because every cited input verifies. 🟢 **Two further corrections fell out of the same
recomputation**: the earliest APAC date is **Korea's ~2027-01**, not Vietnam's, and
**2027-09-01 is the education-specific deadline** — the later of Vietnam's two, not the
earlier.

### 🟢 The regional trend this pass establishes

🟢 **Africa moves from "no evidence" to "policy mapped, market unmeasured"** — four
jurisdictions with dated instruments (AU Continental AI Strategy, endorsed **2024-07-18/19**;
Kenya 2025–2030 with a **2025-12** roadmap; Nigeria's 2025 curriculum reform and a **1.5M**
teacher programme; South Africa's unpublished DBE framework). 🔴 **Zero adoption, spend or
deployment figures for any of them.** 🔵 **A different gap, and a smaller one.**

🔴 **The trend worth quoting to a client drafting AI policy**: 🔴 **South Africa's 2024 draft
national AI policy framework was published for comment and then WITHDRAWN, after concerns it
contained incorrect information and citations and journals that do not exist.** 🔵 **A
national AI policy withdrawn for fabricated references is the sharpest available argument for
the citation discipline this shelf runs on**, and a live risk for anyone drafting from
secondary summaries.

🔵 **And the regulatory shape is now three regimes that differ in KIND, not in severity of one
rule**: 🔴 **Vietnam broadest in kind** (three entries, including biometric behavioural
monitoring), 🔴 **the EU strictest in consequence** (affect inference in education is
prohibited, not classified), 🟡 **Korea narrowest in scope** (one use case, K-12 student
evaluation). 🟢 **So an EU-shaped compliance package transfers to Vietnam more readily than to
Korea**, and the clock that bites first is Korea's ~**2027-01**.

## Pass 148 — 2026-10-12

🔵 **Thesis high-water mark before this pass: `T67`. Next free: `T68`.** 🟢 **This pass takes
`T68`–`T73`**, computed from the register rather than assumed (`ACTION EN`'s rule, holding).

🟢 **Eight of eight pre-registered actions reached.** 🟢 **Four discharged with silent
falsifiers.** 🔴 **Four refuted — and three of the four refutations are the pass's best
findings**, because each failed for a reason the action had not imagined.

| thesis | movement this pass |
|---|---|
| 🟢 **`T64`** — an empty walk has three causes, the third being a language outside the map | 🟢 **CLOSED for Rust, and WIDENED.** `p148-rust-surface` reads the language and the row reads **46**. 🔴 **And the shelf has a SECOND Rust row** — `BetterSEQTA/DesQTA`, **31 `.rs` files** — which no pass had noticed |
| 🔴 **`T63`** — the licence census is monolingual | 🔴 **NARROWED to the connector tier.** `ACTION EQ`: **0 of 13** npm and agent rows change class. 🟢 **The 52-row correction was already complete** |
| 🔴 **`T59`** — npm rows unplaceable on the region axis | 🟢 **The INVERSE now measured.** The institution channel on **44 clones** places **26** rows and adds **16** the offset channel declined. 🔴 **But it inherits noise a tarball cannot have** — `T69` |
| 🟢 **`T67`** — a bare `.edu` is not a country signal | 🟢 **VINDICATED, and it is the ONLY reason `ACTION ER` was refuted.** Excluding bare-`.edu` leads, the two region channels agree **10 of 10**. 🔵 **Promote it from observation to exclusion** |
| 🟢 **`T58`** — Korea covers one K-12 use case against the EU's four | 🟢 **CAVEAT DROPPED** (`ACTION ES`). 🔴 **But SUPERSEDED in scope by `T71`**: Korea is no longer APAC's only statutory education item |
| 🟢 **`T66`** — a North American denominator was double-entered | 🟢 **SECOND CLAUSE CONFIRMED** (`ACTION ET`). 🔴 **"24 states enacted" has no reachable source and is WITHDRAWN BY NAME** |
| 🟢 **`T42`** — two instruments measuring different properties | 🟢 **A FOURTH confirmation, from the wrapper side.** `ACTION EU`: **218 PRESERVED / 2 REFUSED / 0 CHANGED** over 220 pairs |
| 🟢 **`T39`** — an exclusion is sound only relative to the property measured | 🔴 **GENERALISED AND LIMITED.** `ACTION EV`: only **5 of 16** subjects have a manifest allowlist to read, and **1 of 16 CANNOT HAVE ONE** (`go.mod`). 🔵 **`T39` applied to itself** |
| 🟢 **`T21`** — a licence identifier is not a licence | 🟢 **A THIRD instance, on a row this KB never held.** Fedena declares Apache-2.0 in prose and ships **no Apache text at all** |
| 🆕 🔴 **`T68`** | 🆕 **One manifest can declare TWO include allowlists that DISAGREE.** `librus-mcp`: wheel `packages` (1 item) → **35** sites; sdist `only-include` (16 items) → **39**. 🔴 **p147 named the sdist rule and published the wheel figure.** 🟢 **The 35 is right; the rule cited for it is not** |
| 🆕 🔴 **`T69`** | 🆕 **An instrument's precision is a function of the artefact's CURATION.** The institution probe: **2 placements / 3 caught false positives** on 8 allowlist-filtered tarballs; **26 placements** and a URL-shortener placement on 44 whole clones. 🔴 **Validated on one population, not transferable to the other without re-validation** |
| 🆕 🔴 **`T70`** | 🆕 **A global-platform or URL-shortener host is not an institution, and ccTLD logic cannot tell.** `ahmedEid1/lumen` → **EMEA on `youtu.be`**, from a video-ingest allowlist |
| 🆕 🔴 **`T71`** | 🆕 **APAC holds TWO statutory education items.** Vietnam's **Decision 33/2026/QD-TTg** lists education among 46 high-risk AI systems; **2027-03-01** / **2027-09-01**. 🔴 **Three APAC dates now land before the EU's 2027-12-02** |
| 🆕 🔴 **`T72`** | 🆕 **A stated grant can be unnameable for a THIRD reason — the licence's own common TITLE.** *"Apache License 2.0"* matches neither `Apache-2\.0` nor `Apache License.*Version 2\.0`. 🟢 **`UNIDENTIFIED` is honest and still cannot name what is in front of it** |
| 🆕 🔴 **`T73`** | 🆕 **A figure with no source is indistinguishable from a sourced one until someone looks.** "24 states enacted" survived **three passes** because each pass cited this KB rather than the tracker |

### 🔵 The trend this pass is about: four falsifiers fired, and three of them fired sideways

🟢 **`ACTION EO`, `EP`, `ET` and `EU` discharged with their falsifiers silent.** 🔴 **`EQ`,
`ER`, `ES` and `EV` were refuted.** 🔵 **What is worth recording is that three of the four
refutations were refuted by something the action had not asked about:**

| action | refuted because | what it actually found |
|---|---|---|
| `EQ` | **0 of 13** rows changed class | 🆕 🔴 **the agent tier had never been censused for licence at all** — population **52 → 57** |
| `ER` | **1** disagreement, not 0 | 🆕 🟢 **16 net new region placements**, and the one disagreement is `T67`'s own evidence class |
| `EV` | **11 of 16** have no allowlist | 🆕 🔴 **`T68`** — and `go.mod` **cannot** have one, which makes it structural |
| `ES` | both names are the same statute | 🟢 **exactly as the falsifier predicted** — the one clean refutation |

🔵 **A falsifier that fires has done its job; a falsifier that fires and hands you a better
question has done more than its job.** 🟢 **This KB's practice of writing the consequence
clause before the measurement is what makes the difference visible** — `EQ`'s consequence
clause said *"the correction to the 52-row total is already complete,"* and it was, and the
52 turned out to be the wrong denominator.

### 🔵 The register's load-bearing line, tested in two new places and holding

> 🟢 **An instrument must be able to distinguish "I looked and it is not there" from "I
> could not look."**

| new instance this pass | the reassuring value it would have returned |
|---|---|
| 🔴 `csv.DictReader` over a file with a **leading blank line** | 🔴 **`DISAGREE 0 → NOT REFUTED`** over an empty population |
| 🔴 `licence_census` on *"Apache License 2.0"* | 🟡 **`UNIDENTIFIED`** — honest, but it cannot name a plainly stated grant |
| 🟢 `p148-rust-surface` on a tree with no `.rs` | 🟢 **`NO_RUST_SURFACE_READ`, never `0`** — the line applied at design time |

🔴 **The first of these was in THIS pass's own new instrument and was caught before
publication**, which is the fourth consecutive pass where a probe inflated or flattened its
own headline in the reassuring direction before being corrected (`P146-H`, `P147-K`'s
allowlist, `P147-D`, this). 🔵 **That is now frequent enough to be a property of the method
rather than a run of bad luck**: 🟢 **the self-check is working, and the thing it keeps
catching is the same thing.**

### 🆕 🟢 What moved in the world, as distinct from in the instruments

- 🆕 🔴 **A second APAC statute reaches education, and it is the EU's shape.** Vietnam's
  **Decision 33/2026/QD-TTg** (in force **2026-08-15**) lists **46** high-risk AI systems
  under **Law 134/2025**; education is a listed sector with automated assessment and
  behavioural monitoring named. Compliance **2027-03-01**, or **2027-09-01** for systems
  live before 2026-08-15. 🔴 **No primary text read** — four law-firm briefings agreeing.
  🟡 **And one qualifier that would narrow it sharply if it holds for education**: some
  listed systems are high-risk only where AI output is the **sole** basis for a decision
  with no human in the loop.
- 🆕 🟢 **The Middle East is no longer a hole.** UAE: AI **KG–G12** from **2025-26**, a
  standalone subject, extended to national-curriculum private schools **2026-27**, **22 000**
  educators trained. Saudi Arabia: all public schools from **2025-26**, **6M+** students,
  **SDAIA** among the implementers. 🔵 **Ministry-scale buyers, not institution-scale.**
- 🔴 **Africa is a NULL that was searched for by country name.** Kenya, Nigeria, South
  Africa: nothing. 🟢 **On the record as looked for**, which is the only way a gap stays
  distinguishable from coverage.
- 🆕 🟢 **LATAM produces its first capability figure.** TALIS secondary-teacher AI use:
  **Brazil 56% · Chile 55% · Colombia 53% · Costa Rica 52%** against an **OECD average of
  36%**; **Uruguay/Ceibal 75%**. 🔵 **The 87% / 26% governance gap is unchanged** — so the
  region is not an adoption problem, it is a governance problem on a workforce that already
  adopted.
- 🟢 **An institutional recommendation that matches this KB's repository-side read.** The
  **OECD 2026 Digital Education Outlook** recommends moving beyond general-purpose AI tools
  toward **purpose-built educational AI**. 🔵 **`P31` is that recommendation, with repo
  names attached.**
- 🔴 **Market sizing remains unquotable, and the spread widened again.** Research and
  Markets **~$10.6B (2026) → ~$42.5B (2030)**; X-Pilot **$12.3B (2026)**; Europe **$2.64B
  (2026)**; against this KB's four non-overlapping 2025 baselines. 🟢 **The maturity read
  stays the only adopted number: 35/100, most institutions in pilot mode.**

### 🔴 Declared gaps after this pass

- 🔴 **Nine consecutive passes with no education-domain agent from SEARCH.** 🟢 **Stop
  reporting it as a surprise**: every row added in five passes came from re-measuring the
  shelf, and this pass found two Rust rows that way.
- 🔴 **No primary legal text read for Vietnam, and none for Korea.** `capitol.texas.gov`
  unread for a **ninth** pass and not re-registered; `aibasicact.kr` `ENOTFOUND`;
  `law.go.kr` and `elaw.klri.re.kr` **not yet attempted** — `ACTION EX`.
- 🔴 **Africa: zero education-AI evidence on any channel.**
- 🔴 **`T67` is proved and not enforced.** It is the sole cause of `ACTION ER`'s refutation
  and the probe still emits bare-`.edu` placements. 🔵 **A one-line change, deliberately not
  made this pass** so the comparison ran against unmodified instruments.
- 🔴 **`mcp-student-records`' set identity is proved by this KB and asserted by nobody in
  CI.** 🟢 **`p148-rust-surface` is the artefact to vendor**; the repository has no such test.
## Pass 147 — 2026-10-12

🟢 **Six of p146's eight open actions resolved; two refuted on their own terms and one
refuted with its premise.** 🆕 **`T62`–`T67` adopted.** 🟢 **`T42` confirmed by a third
independent method.** 🔴 **`T59` narrowed.** 🔴 **`T60` weakened by `T65`.** 🟢 **The five
rows p146 made provisional are all cleared.**

| thesis | movement this pass |
|---|---|
| 🟢 **`T42`** — two instruments measuring different properties | 🟢 **CONFIRMED by a third method.** Resolving `@imazhar101`'s 18 registration sites one level sums to **exactly 227** descriptors. 🔵 **The 18 and the 227 are one surface counted at two levels** |
| 🔴 **`T59`** — npm rows structurally unplaceable on the region axis | 🔴 **NARROWED.** 🟢 **2 of 8 ARE placeable** by institution evidence in the shipped payload. 🔵 **The git-only constraint is the instrument lane's, not the evidence's** |
| 🔴 **`T60`** — the channel map is dated, not permanent | 🔴 **WEAKENED by `T65`.** It is not stable within a date either |
| 🆕 🔴 **`T62`** | 🆕 **Artefact mode is a MANIFEST property, not a tree property.** 2 of 16 non-npm rows read `PAYLOAD` while **gitignoring** the tree they name. 🔴 **13 of 16 declare none in `package.json`, so `SOURCE` is reached by default — and some declare one in a manifest the probe does not read (`ACTION EV`)** |
| 🆕 🔴 **`T63`** | 🆕 **The licence census is monolingual.** `licen[cs]e` cannot match `Licença` or `Licencia`. 🔴 **2 of 9 `NONE` rows carry a grant**; strict-unlicensed **9 → 7** |
| 🆕 🔴 **`T64`** | 🆕 **An empty walk has THREE causes, not one** — exclusion, wrong artefact kind, **and a language outside the instrument's map**. 🔴 **The third hides a real 46-tool Apache-2.0 server** |
| 🆕 🔴 **`T65`** | 🆕 **The clone channel is SESSION-scoped.** Three passes, one date (2026-10-12): 44/44 open, refused, **52/52 open** |
| 🆕 🔴 **`T66`** | 🆕 **A North American denominator was double-entered.** "35 states introducing" IS "35+ states guidance"; **"24 enacted" is unsupported**, against competing counts of **3 / 10 / 12** |
| 🆕 🔴 **`T67`** | 🆕 **A bare `.edu` is not a country signal.** Grandfathered non-US registrations exist and **this shelf holds the counterexample** — `P144-V` placed `unav.edu` as EMEA |
| 🟢 **`T58`** — Korea covers one K-12 use case against the EU's four | 🟢 **HOLDS on substance.** 🟡 **But the cross-referenced statute has two English names** — *Framework Act on Education* vs CSET's *Basic Education Act* |
| 🟢 **`T39`** — a population exclusion is sound only relative to the property measured | 🟢 **VINDICATED by the repository itself.** `ACTION EC` finds the property-based rule already written: `librus-mcp`'s `pyproject.toml` `only-include` excludes `legacy_reference` and admits one file from `scripts/`, and reading registration sites inside it gives **exactly 35** — p144's hand-tuned name list, by construction instead of by tuning. 🔴 **Naive inclusion would read 60** |
| 🟢 **`T21`** — a licence identifier is not a licence | 🟢 **Instance resolved in the opposite direction.** `moodle-mcp-server-aql`'s AGPL-3.0 **does** have 661 lines behind it — in the repository, excluded from the tarball by a 16-glob `files` allowlist |

### 🔵 The trend this pass is actually about: an instrument that refuses is worth more than one that answers

🔴 **Three of this pass's six new theses are the same shape.** An instrument was asked a
question it had no input for, and it answered anyway:

| instrument | input it had | what it said |
|---|---|---|
| `surface_gate*` on the npm tier | 🔴 **0 files** (exclusion) | `NOT_AN_MCP_SERVER` |
| `surface_gate*` on a Rust tree | 🔴 **0 files** (language) | `NOT_AN_MCP_SERVER` |
| `licence_census` on a Portuguese README | 🔴 **no matching pattern** | `NONE` |

🔵 **None of the three is a wrong measurement. All three are a measurement that was never
taken, published in the shape of one** — and in every case the output was the reassuring
value. 🟢 **`p146-empty-walk-guard` fixed that for the walk; this pass extends the idea to
the pattern**: a matcher that cannot express the thing it is looking for should not return
"absent."

🔵 **The generalisable rule, which is now this register's most load-bearing line:**
🟢 **an instrument must be able to distinguish "I looked and it is not there" from "I could
not look."** 🔴 **Every figure this KB has withdrawn in the last five passes failed that
test**, and none of them failed on the measurement itself.

### 🆕 🟢 What moved in the world, as distinct from in the instruments

- 🆕 🟢 **A permissive SIS layer exists.** `zavora-ai/mcp-student-records` — **Apache-2.0,
  Rust, 46 tools**, a declared `mcp-server.toml` with a typed `risk_class` per tool,
  **23 of 46 writes approval-gated**, and **FERPA access logging**. 🔵 **The first row on
  this shelf that ships machine-checked governance over its own write surface**, and the
  first time a studio can build LMS + SIS with **no copyleft anywhere** (Sakai ECL-2.0 +
  this).
- 🔴 **Adoption-versus-governance is now the same gap in two regions, measured by four
  publishers.** LATAM: **87% adoption / 26% frameworks** (UNESCO IESALC) and **92% students
  / 79% faculty** with a **50%-want / 19%-practise** feedback gap (DEC). NA: **92% student
  use** against **~10% of institutions with guidelines** and **71% of teachers untrained**.
  🔵 **Two regions, different units, identical shape** — and it is the shape a studio sells
  into.
- 🔴 **Market sizing is no longer quotable.** Four 2025 baselines were returned and none
  overlaps: **$6.4B / $7.52B / $8.3B** against this KB's carried **$9.58B**; 2030–2034
  projections span **$42.48B to $79.6B**. 🟢 **One maturity read is worth more than all of
  them: 35/100, most institutions still in pilot mode.** 🔵 **Sell the
  pilot-to-production transition, not the TAM.**
- 🟡 **The EdTech delivery model is being displaced in EMEA.** One QS/HolonIQ read of the
  2026 Europe EdTech 200 notes **few traditional education providers** in the UK's AI-skills
  delivery model, **with Big Tech as delivery partners**, against a **£200m+** commitment.
  🔵 **A risk for institutional buyers and an opening for an integrator who is neither.**
  🔴 **Single source, not adopted.**

### 🔴 Declared gaps after this pass

- 🔴 **No education-domain agent has been added by SEARCH for eight consecutive passes.**
  Every hit is a curriculum. 🔵 **Both rows this pass added came from re-measuring what the
  KB already held.** 🟢 **That is a settled fact about the channel and should stop being
  reported as a surprise.**
- 🔴 **Primary legal text is unreachable on both channels for two jurisdictions** —
  `capitol.texas.gov` (eight passes) and now `aibasicact.kr`. 🔵 **An environment allowlist
  request, not a research gap.**
- 🔴 **The surface lane reads 7 languages and the shelf contains at least 8.** `.rs` is
  fixed by refusal, not by measurement — 🔴 **nothing counts Rust tool surfaces yet, and
  the one Rust row is the best-governed on the shelf.**
- 🔴 **No bidirectional surface pin has been added since p144.** `mcp-student-records` has
  the strongest **property** pin on the shelf and still does not assert set identity between
  its manifest and its router.

## Pass 146 — 2026-10-12

🔴 **`T40` is WITHDRAWN and `T3` is RESOLVED** — the two longest-running open questions on
this register close in the same pass, in opposite directions. 🆕 **`T56`, `T57` and `T58`
adopted.** 🔴 **`T42` is promoted from an incident to a shelf property**, and 🔴 **`P145-W`'s
APAC null is refuted by figures that point down rather than up.**

| thesis | movement this pass |
|---|---|
| 🔴 **`T40` — APAC's compliance surface is horizontal, EMEA's is vertical** | 🔴 **WITHDRAWN.** Korea's AI Basic Act **Article 2(4)(j)** names **student evaluation**, cross-referencing Article 9(1) of the Framework Act on Education. 🔴 **"Three binding statutes and not one is about education" is false** — one of the three names it in a numbered item |
| 🆕 🟢 **`T58` — the EU and Korea both regulate education; they differ in SCOPE and SEQUENCE** | 🆕 **ADOPTED**, replacing `T40`. **Korea: one use case, K-12 only.** **EU: four use cases, every level** (access/admissions, learning-outcome assessment, level assignment, exam monitoring). 🔴 **And Korea bites first** — in force **2026-01-22** + ~1-year MSIT grace ≈ **2027-01**, against Annex III at **2027-12-02** |
| 🟢 **`T3` — the EU high-risk clock is a sales window** | 🟢 **RESOLVED.** Digital Omnibus on AI: EP **2026-06-16** → Council **2026-06-29** → signed **2026-07-08** → in force **2026-07-27**, as **Regulation (EU) 2026/1744**. Annex III **2027-12-02**, Annex I **2028-08-02**. 🔴 **`P144-U`'s sixteen-month conflict closes in favour of the later date** |
| 🟢 **`T43` — one prohibition is already in force and nobody disputes it** | 🟢 **CORROBORATED a third time**, and now with its companion: 🟢 **the Article 4 AI-literacy duty has applied since 2025-02-02 and the Omnibus does not defer it.** 🔵 **Two live obligations and one deferred classification — the EMEA conversation is not "2027"** |
| 🆕 🔴 **`T56` — adoption and policy can point opposite ways in one country, and policy moves the budget** | 🆕 **ADOPTED.** Korea holds APAC's only statutory education item **and** withdrew its flagship classroom programme: amendment **2025-08-04** removed AI digital textbooks from the legal definition of a textbook, taking the attached funding with it. Adoption **37% of classes → 19%** inside 2025; schools **~4 190 → 2 095** |
| 🆕 🔴 **`T57` — a legislative tracker's status field is not a legal fact** | 🆕 **ADOPTED.** *"Texas HB 2400 bans AI from providing direct classroom instruction"* arrived as current law. 🔴 **Last recorded action: 2025-03-14 referral to committee.** One tracker says **"Became Law"** while its own last-action field says otherwise. 🔵 **Read the action, never the label** |
| 🔴 **`T42` — a measurement's population filter is part of its instrument** | 🔴 **PROMOTED from incident to shelf property.** **35** traversing instruments, 🔴 **0 with an empty-walk guard**, 🔴 **5** excluding `dist`/`build` with no re-admission while emitting a verdict. 🆕 **A second instrument pinned carrying it** (`p141/surface_gate.py`) |
| 🆕 🔴 **`T59` — an instrument's TRAVERSAL CHANNEL is part of its reach** | 🆕 **ADOPTED.** 🔴 **16 of 35 instruments read only `git ls-tree`/`ls-files`**, so a clone is a precondition. 🔵 **The whole region-placement lane is in that set, so the 8 npm rows are structurally unplaceable on this KB's primary axis** — and no pass had said so |
| 🟢 **`T1` — the governance gap is the market** | 🟢 **STRENGTHENED to three levels in three regions.** 🆕 Brazil K-12: **53% of administrators using AI against 22% of schools with guidelines**, joining LAC higher-ed **87% / 26%** (`P144-R`) and EMEA **10% of 450+**. 🔵 **The gap is not a LATAM feature and not a higher-education feature** |
| 🟢 **`T41` — LATAM adoption leads the OECD** | 🟢 **HELD, not re-measured.** No new teacher-adoption figure this pass; the Brazil administrator figure is a different instrument and is recorded as `T1`, not as `T41` |
| 🔴 **`T10` — the agent search channel is saturated for this domain** | 🔴 **CONFIRMED a seventh time.** Six queries, and every education-specific hit is a course: `microsoft/ai-edu`, `ML-For-Beginners`, `rohitg00/ai-engineering-from-scratch`, `AIcademy` (**309★**). 🟢 **Not re-registered** |
| 🆕 🔴 **`T60` — the channel map is not stable across passes, so it must be re-measured, not assumed** | 🆕 **ADOPTED.** 🔴 **p145's clone channel is refused in p146**, same date. 🟢 **And `WebFetch` on `github.com` works, which p145 never tested.** 🔵 **Every "unreachable" in this KB is dated, not permanent — and so is every "reachable"** |
| 🆕 🔴 **`T61` — a register's NUMBER SPACE is part of its data** | 🆕 **ADOPTED.** 🔴 **This register is not sequential.** Pass 113 allocated `T44`–`T46`; pass 116 reached `T55`; 🔴 **passes 143–145 then allocated `T35`–`T43`**, counting up into occupied space. 🔵 **p146 was the first pass whose next free number was already taken** — its theses are `T56`–`T61`. 🔴 **Not repaired — `ACTION EN`** |

### 🆕 🟢 `T58` — what replaces `T40`, and why the replacement is more useful

`T40` was adopted in p144 on a real observation: Korea, Vietnam and Taiwan all brought
horizontal AI statutes into force, and none of them is an education law. 🟢 **That framing
survives for Vietnam and Taiwan.** 🔴 **It fails for Korea**, and Korea is the one that
matters, because its statute reaches education through a numbered item rather than through
general applicability.

| | EU (Annex III, as amended) | Korea (AI Basic Act, Art. 2(4)(j)) |
|---|---|---|
| **named education use cases** | **4** — access/admission, learning-outcome assessment, level assignment, exam monitoring | 🔴 **1** — student evaluation |
| **levels covered** | 🔴 **all, including higher and vocational** | 🟢 **early childhood, elementary, secondary only** |
| **obligations bite** | **2027-12-02** | **2026-01-22**, penalties after ~1-year MSIT grace ≈ 🔴 **2027-01** |
| **route in** | listed high-risk category | listed high-impact domain **+** a significance test |
| **escape hatch** | conformity route | 🟢 **a formal MSIT determination can be requested** |

🔵 **The commercial reading, and it reverses this KB's prior sequencing.** A Korean K-12
grading or assessment engagement is inside a statutory high-impact category **now**, with
penalties roughly eleven months before the EU's deadline. 🟢 **A Korean higher-education
engagement is outside item (j) entirely** — which is the opposite of the EU, where higher
education is squarely inside Annex III. 🔴 **"APAC is lighter-touch than EMEA" is wrong at
the K-12 layer and right at the university layer**, and it was published as a single claim.

🔴 **Both halves of the asymmetry rest on secondary translations.** `ACTION EL` sends the
scope of item (j) to primary text, because if the Enforcement Decree widens it, the
commercially load-bearing half of `T58` is the half that breaks.

### 🆕 🔴 `T56` — the reversal channel, and why this KB had not looked for it

Every adoption figure this register holds measures uptake. 🔴 **None measured withdrawal**,
and Korea supplies the first instance: a national programme that ran, was funded, was
measured, and was then removed from the statute that funded it.

| stage | date | figure |
|---|---|---|
| programme running | 2025 H1 | **37%** of classes, **~4 190** schools |
| statutory status removed | 🔴 **2025-08-04** | textbook definition narrowed to print and e-books |
| funding consequence | following | 🔴 **subscription support lost with the status** |
| programme running | 2025 H2 | 🔴 **19%** of classes, **2 095** schools |
| delivery model | after | voluntary, school by school |

🔵 **Why it belongs on a trends register rather than in the news.** `T1` says the market is
the adoption-governance gap. `T56` says the gap can close from the wrong side: not
governance catching up to adoption, but adoption collapsing when the governance that
funded it is withdrawn. 🔴 **A pipeline built on a national mandate carries that risk and a
pipeline built on institutional demand does not** — and this KB had no way to express the
difference before this pass.

# Education — current trends

## Pass 145 — 2026-10-12

🔴 **`T30` is WITHDRAWN OUTRIGHT**, and the reason is that its npm figure and its other
figures were produced by two instruments measuring two different properties. 🆕 **`T42`
adopted.** 🟢 **`T3`'s date conflict is half-resolved on a second independent source**, and
🟢 **`T41` is corroborated by a second publisher**. 🔴 **`T40` is CHALLENGED and the
challenge is recorded without being adopted.**

| thesis | movement this pass |
|---|---|
| 🔴 **`T30` — npm publication predicts literal registration** | 🔴 **WITHDRAWN OUTRIGHT.** Its npm figure (**12%**) is `surface_bound`'s **1 of 8**; its other tiers' figures (**50%**) are `surface_gate2`'s site counts. 🔴 **Two instruments, two properties, one trend built across them** |
| 🆕 🔴 **`T42` — a measurement's POPULATION FILTER is part of its instrument** | 🆕 **ADOPTED.** 🔴 **7 of 8 npm rows returned `NOT_AN_MCP_SERVER` from an empty file set**, because `SKIP_DIRS` excluded the only tree they ship. 🔵 **`T39` said an exclusion must be property-relative; `T42` says a skip list is an exclusion** |
| 🟢 **`T39` — exclusion is sound only relative to the property** | 🟢 **STRENGTHENED on a 52-repository population, and in both directions at once.** `NOT_SHIPPED` over-excludes nothing (**10 of 12 names inert**, 5 never seen); `SKIP_DIRS` over-excluded **7 of 8 npm rows entirely** |
| 🟢 **`T35` — the best rows declare their own surface** | 🟢 **STRENGTHENED, two new rows.** `ahmedEid1/lumen` ships `TOOL_SPECS` (**9**, walked by `server.py:263`); `nitsuah/bb-mcp` ships `src/manifest.ts` (**17** named schemas). 🔴 **Neither is bidirectional** |
| 🟢 **`T21` — the registry decides whether the grant ships** | 🟢 **STRENGTHENED, and sharpened to zero.** 🔴 **0 of 8 npm packages ship a licence FILE.** 6 declare MIT in `package.json`, 1 in a README, 1 declares **AGPL-3.0**. 🔵 **Consistent with `T21`'s 33% payload rate: `npm pack` includes a `LICENSE` only if one exists** |
| 🟡 **`T3` — the EU high-risk clock is a sales window** | 🟢 **HALF-RESOLVED.** A second, independent source confirms the **Digital Omnibus** moves high-risk education — admissions, grading, placement, proctoring — to **2027-12-02**. 🔴 **The Article 4 AI-literacy duty is now the conflicted item**, not the high-risk date |
| 🆕 🟢 **`T43` — one prohibition is already in force and nobody disputes it** | 🆕 **ADOPTED.** 🟢 **Emotion-recognition AI in schools has been banned since 2025-02**, and it is the one date every source agrees on. 🔵 **A past, undisputed prohibition is a different conversation from a deferred classification** |
| 🔴 **`T40` — APAC's compliance surface is horizontal, EMEA's vertical** | 🔴 **CHALLENGED, not withdrawn.** One source states Korea's **high-impact** category names **education** alongside healthcare and finance. 🔴 **If so, `T40`'s "not one is about education" is wrong.** The passage is truncated in the result and the primary text is unreachable here — 🟡 **recorded as a live challenge, adoption withheld** |
| 🟢 **`T41` — LATAM adoption leads the OECD** | 🟢 **CORROBORATED by a second publisher.** Tec de Monterrey's observatory: student use **86% → 92%**, teacher use **61% → 79%**. 🔵 **A second publisher, the same direction, and a rising slope rather than a level** |
| 🟢 **`T1` — the governance gap is the market** | 🟢 **STRENGTHENED on the North American half, quantified.** **35 states + DC + Puerto Rico** introduced AI education legislation since 2025; **24 states enacted**; **35+ published guidance**. 🔵 **Introduced-to-enacted is 24 of 35 — the gap is narrowing in NA while it holds elsewhere** |
| 🔴 **`T10` — the agent search channel is saturated for this domain** | 🔴 **CONFIRMED a sixth time.** Six queries, same three course repositories. 🟢 **Not re-registered** |

### 🆕 🔴 `T42` — a measurement's population filter is part of its instrument

🆕 **ADOPTED.** This KB has now broken the same rule at three levels, and `T42` is the
level it had not reached.

| level | the rule broken | where |
|---|---|---|
| the **tier** | a figure's tier is part of its claim | `T30` (p141) |
| the **instrument** | a figure's instrument is part of its claim | `T36` (p143, withdrawn p144) |
| the **exclusion list** | an exclusion is sound only relative to the property | `T39` (p144) |
| 🆕 the **skip list** | 🔴 **a skip list is an exclusion, and nobody checked it** | 🆕 **`T42` (p145)** |

🔴 **`NOT_SHIPPED` was audited three times across p143, p144 and p145. `SKIP_DIRS` sat four
lines above it and was never read.** 🔵 **The list that looked like configuration was doing
the most consequential filtering on the shelf** — it removed seven of eight rows from a
tier and left a verdict behind that looked like a measurement.

🟢 **The general form, and it is cheap to apply:** before reading a share, ask what the
denominator excluded and whether the excluded thing could carry the property. 🔴 **A
verdict computed over zero files must be an error, not a value** — and no instrument on
this shelf said so, which is why `surface_gate3.py` prints `artefact` and `admitted` as
columns rather than deciding silently.

### 🟢 `T3` — what is resolved and what is not

🟢 **Resolved:** two independent sources now put high-risk education obligations —
admissions, grading, placement, proctoring — at **2027-12-02** under the Digital Omnibus,
against the pre-Omnibus **2026-08**. 🔵 **`P144-U` published a sixteen-month conflict; one
side of it now has two publishers and the other has one.**

🔴 **Not resolved:** the **Article 4 AI-literacy duty**. One source says national
authorities began enforcing it on **2026-08-02**; another says the Omnibus replaced it with
a softer obligation to *support* AI literacy. 🔴 **That is a live conflict about a duty that
is either in force now or not a duty at all**, and it is the nearer-term question for a
client.

🔵 **The commercially useful consequence is unchanged by either reading**: the deferral
moved the deadline, not the work, and a 2027-12-02 conformity assessment is still scoped in
2026.

### 🆕 🟢 `T43` — the prohibition nobody disputes

🆕 **ADOPTED.** Every source on the EU clock disagrees about high-risk dates and the
literacy duty. 🟢 **All of them agree that emotion-recognition AI in schools has been
prohibited since 2025-02.**

🔵 **This matters more than its narrowness suggests.** It is the one EU AI Act provision a
client can be told is *already* binding, with no date risk. 🔴 **And this KB holds two rows
in the affect-detection class** — `P142` flagged `zijinz456/OpenTutor` and one other as
`PII_AND_AFFECT`. 🟢 **A prohibition in force plus two shelf rows inside its scope is a
concrete audit, not a trend.**

### 🔴 `T40` — the challenge, stated so the next pass can settle it

p144 adopted `T40` on the finding that three APAC statutes entered force in 2026 and **not
one is about education**. 🔴 **One source this pass says Korea's AI Framework Act names
education inside its high-impact category**, alongside healthcare and finance.

🔴 **If that is right, `T40` is wrong in its central claim** — Korea would be a *vertical*
surface naming education, exactly like the EU, and the horizontal/vertical split between
APAC and EMEA would collapse.

🟡 **Adoption is withheld for two stated reasons.** The passage is truncated in the search
result, so what is attributed to the high-impact category cannot be read in full; and the
primary text is not reachable from this environment. 🔵 **A trend this KB adopted one pass
ago should not be withdrawn on a truncated secondary source, and should not be defended by
ignoring one either.** It is registered as `ACTION EH`.

### 🔵 The supply-side picture this pass changes

🔴 **The shelf is less buildable than it looked.** 🟢 **8 of 44 connector rows carry no
licence at all**, three of them on the LATAM system-of-record tier this KB recommends as an
entry point, and **0 of 8 npm packages ship a licence file**.

🔵 **So the 2026 "purpose-built over general-purpose" migration has a supply problem that is
legal rather than technical.** The connectors exist, their tool surfaces are now measured,
and a third of them cannot be folded into a client deliverable as they stand. 🟢 **That is
the most actionable thing this pass produced**, and it is why `ACTION EE` goes looking for
licensed fork parents rather than for more rows.

### 🔴 What the agent channel returned, for the sixth consecutive pass

🔴 **Null.** Two global queries and four regional ones. 🔴 **The same three course
repositories as p144** — `microsoft/ai-agents-for-beginners` (**67 223★**, MIT),
`pguso/agents-from-scratch` (**796★**, MIT), `rohitg00/ai-engineering-from-scratch`.

🔵 **Six nulls is a settled fact about the channel**, confirming `T10`. The query term
"education" matches a repository's *pedagogy*, not its *domain*. 🟢 **Every connector row
this KB holds was found by other means**, and a seventh attempt is not registered.


## Pass 144 — 2026-10-12

🟢 **`T1` — the governance gap — is now measured on two continents by two unrelated publishers,
and it is the same gap.** 🔴 **`T36` is WITHDRAWN one pass after adoption**, in the place it was
strongest. 🆕 **`T38` and `T39` adopted**, both about the limits of the instruments this page
reasons with.

| thesis | movement this pass |
|---|---|
| 🟢 **`T1` — the governance gap is the market** | 🟢 **STRENGTHENED, and quantified on both halves from one instrument.** UNESCO IESALC over **200 institutions in 19 countries**: 🟢 **87% using AI** against 🔴 **26% holding a formal AI strategy**. EMEA independently: 🔴 **10% of 450+ institutions** have formal guidelines. 🔵 **Two continents, two publishers, same gap** |
| 🔴 **`T36` — npm and the other tiers are not comparable** | 🔴 **WITHDRAWN.** Bundle and shipped source return **identical tool-name sets** on 3 of 3 measurable packages. 🔵 **What survives is narrower**: the two *instruments* are not interchangeable, but the two *artefact kinds* are |
| 🟢 **`T37` — a share-based falsifier cannot see a population error** | 🟢 **CORROBORATED by recurrence, then SUPERSEDED in its remedy.** It recurred twice this pass — in `ACTION DP`'s own first draft, and in `p142`'s bot commits. 🔵 **But its remedy was wrong**, see `T39` |
| 🆕 🔴 **`T38` — a lexical gate detector cannot see a cross-module gate** | 🆕 **ADOPTED.** `librus-mcp` has **three real feature gates** and the instrument reports **`gated=0`**: the gates are in `server.py`, the sites they control in `send_tools.py`. 🔴 **Every `gated=0` on this KB means "no gate in the same file"**, and `T28`'s category is a floor |
| 🆕 🟢 **`T39` — a population exclusion is sound only relative to the property measured** | 🆕 **ADOPTED.** 🔴 **`p141` includes non-shipped parent POMs on 3 of 5 rows and is RIGHT to** — the licence *lives* in the parent. 🔵 **"Not shipped" is not the defect; "not bearing the property" is.** A blanket `NOT_SHIPPED` list stands in for that test, and 9 of its 11 names stand in for nothing |
| 🟡 **`T3` — the EU high-risk clock is a sales window** | 🔴 **UNRESOLVED and now explicitly conflicted.** One source: high-risk provisions in force **2026-08**. Another: Digital Omnibus approved **2026-06-29**, moving stand-alone high-risk to **2027-12-02** and embedded to **2028-08-02**. 🔴 **Sixteen months apart**, and `eur-lex.europa.eu` is unreachable here |
| 🟢 **`T2` — mandates with hard dates replaced guidance** | 🟢 **STRENGTHENED with the first PASSED deadline.** Ohio required every K-12 district to hold a formal AI policy by **2026-07-01**. 🔵 **A past deadline is a different sale from a future one** |

### 🆕 🔴 `T40` — the APAC compliance surface is horizontal, and EMEA's is vertical

🆕 **ADOPTED.** Three binding AI statutes entered force in APAC during 2026 — **Korea
2026-01-22**, **Vietnam 2026-03-01**, **Taiwan passed 2025-12** — and 🔴 **not one is about
education**.

🔵 **So the same engagement inherits a different compliance shape by region.** In EMEA the
education use case is named inside the classification: an AI tool affecting *access to education*
is high-risk by definition, so admissions screening triggers a conformity assessment. In APAC the
obligation is a general-purpose AI statute that an education deployment inherits like any other
software.

🟢 **Korea's pilot year is the dated consequence.** MSIT signals **2026 as a pilot period with
limited enforcement** — 🔵 **a statute in force with enforcement deferred is the one window where
conformance work is cheap and voluntary**, and it closes when the pilot does.

### 🆕 🔴 `T41` — teacher adoption in LATAM leads the OECD, and the "lagging region" framing is wrong

🆕 **ADOPTED, and it corrects this KB's own prior framing.** 2024 secondary-teacher AI use:
🟢 **Brazil 56%, Chile 55%, Colombia 53%, Costa Rica 52%** against an **OECD average of 36%**.

🔴 **Four LATAM countries, all 16 to 20 points above the OECD average.** 🔵 **What LATAM lacks is
institutional governance, not usage** — 26% formal strategy against 87% adoption — so the regional
opportunity is governance and platform work on top of an installed base that already exists,
not evangelism. 🔴 **This page has previously carried an "uneven and lagging" framing from
secondary sources; it is retired.**

### 🔵 The supply-side trend the market channel keeps missing

🟢 **Four independent publishers agree the 2026 shift is from experimentation to GOVERNANCE**,
plus agentic use cases, **purpose-built education platforms over generic tools**, and digital
credentials for skills-based hiring.

🔴 **But 90% of LATAM universities implementing AI in teaching use ChatGPT, Copilot or Gemini.**
🔵 **So "purpose-built over general-purpose" describes a migration that has not started**, and the
connector shelf in this KB is the supply map for it.

🔴 **Credentials is the one named trend this KB holds nothing on** — no connector, no platform row,
no repo. 🔵 **Declared as a gap rather than left to look like coverage.**

### 🔴 What the agent channel returned, for the fifth consecutive pass

🔴 **Null.** Four global queries and four regional ones. 🔴 **Every education-specific candidate is
a COURSE**: `microsoft/ai-agents-for-beginners` (**67 223★**, MIT) and
`rohitg00/ai-engineering-from-scratch` are curricula; `pguso/agents-from-scratch` (796★, MIT) is a
teaching repo tagged `open-source-education`.

🔵 **Five nulls is a settled fact about the channel, not a gap in the shelf.** The query term
"education" matches a repository's *pedagogy* rather than its *domain*, so the channel returns
software that teaches AI instead of software that runs a school. 🟢 **Every connector row this KB
holds was found by other means**, and a sixth attempt at the same query is not registered.

## Pass 143 — 2026-10-12

🔴 **`T30` is WITHDRAWN.** Two pre-registered falsifiers fired on it independently in the same
pass: `ACTION DM` removed its three figures by repairing the instrument that produced them, and
`ACTION DL` refuted the mechanism it had proposed. 🔵 **One trend, two unrelated routes to the
same verdict — which is what a register of pre-registered falsifiers is for.**

🟢 **Three of six falsifiers fired.** `DJ`, `DN` and `DO` came back silent; `DK`, `DL` and `DM`
fired.

### 🔁 `T30` WITHDRAWN — the three figures were never one measurement

| | |
|---|---|
| **the claim** | *"A property measured on one packaging tier must be published with that tier named"* — resting on dynamic registration at npm **12%**, agent servers **50%**, GitHub-only connectors **50%** |
| 🔴 **what fired it (1)** | `ACTION DM`. Repairing the instrument moved the GitHub-only tier from **50% to 33%** — a **17-point** move against a five-point falsifier. [`p143-surface-gate-repair`](../compose/code/p143-surface-gate-repair/README.md) |
| 🔴 **what fired it (2)** | `ACTION DL`. The proposed mechanism — *npm rows are simply smaller* — is **refuted in the opposite direction**: median tool count is **18** on npm against **9** off it. [`p143-tier-size`](../compose/code/p143-tier-size/README.md) |
| 🔴 **and the reason neither falsifier anticipated** | 🔴 **The npm 12% was never produced by the instrument that produced the other two.** 7 of 8 npm packages ship only compiled `dist/`/`build/`, which `surface_gate.py` skips — so npm was measured by `p140-live-surface-bound/surface_bound.py`, over **bundles**, while the agent and connector tiers were measured over **source** |
| 🔵 **what was right in it** | The instruction *"name the tier"* was never wrong and is retained in `T36` below. 🔵 **`T30`'s error was not its rule — it was that `T30` itself broke the rule one level up**, comparing instruments while warning about comparing tiers |
| 🟢 **what replaces the figures** | One instrument, one artefact kind: on source trees, agent servers **2 of 4** dynamic, GitHub-only connectors **2 of 6**, foundations **0 of 1**. 🔴 **The npm tier is absent and stays absent until it is measured on source**, where only `@n35da/brightspace-mcp` qualifies and **n=1 is reported as n=1** |

### 🆕 🔴 `T36` — a measurement's INSTRUMENT is part of its claim, exactly as its tier is

| | |
|---|---|
| **the claim** | 🔴 **Two numbers produced by different instruments, or over different artefact kinds, are not comparable however identical their units look.** A percentage carries the thing that measured it, and a gradient assembled from two instruments is an artefact of the assembly |
| **what forced it** | `T30`'s three figures: **12% / 50% / 50%**, read as an axis. 🔴 **The 12% came from a probe reading minified bundles with dependencies inlined; the 50%s from a probe reading source trees.** A literal-vs-dynamic classification is not the same question on those two artefacts, and nothing in the three numbers' presentation said so |
| 🔵 **why it is not just `T30` restated** | `T30` says *name the tier*, and the tiers here **were** named. 🔴 **Naming the tier is insufficient when the tier determines the instrument** — npm publication is precisely what makes a row ship compiled output, so "npm tier" silently means "different probe, different artefact". 🟢 **The tier and the instrument were confounded, and `T30` could not see it because it was looking at tiers** |
| 🟢 **the operational rule** | 🟢 **Publish the probe name and the artefact kind beside every cross-tier figure.** When a tier forces a different instrument, report the tiers separately and refuse the gradient. 🔵 **`T21` is the positive case**: PyPI 0% / npm 33% / Maven 83% holds because one probe read one artefact kind — a published package — in all three ecosystems |
| 🔴 **what would overturn it** | A cross-instrument comparison on these shelves that survives re-measurement by either instrument alone. 🔵 **`ACTION DP` is registered to try exactly that** on the npm tier, by measuring the one npm row that ships source |
| **where it is enforced** | `p143-surface-gate-repair` prints its tier table with the artefact kind per tier and omits npm entirely; `test_compiled_output_is_still_skipped` pins the reason npm cannot appear there |

### 🆕 🔴 `T37` — a share-based falsifier cannot catch an error in the POPULATION

| | |
|---|---|
| **the claim** | 🔴 **A falsifier phrased as "the statistic must not move by more than N points" passes any error that is symmetric across the population** — including measuring the wrong population entirely |
| **what forced it** | `krzysztofbury/librus-mcp`. p141 reported **0 literal, 23 dynamic**; this pass's first repaired draft reported **23 literal, 0 dynamic**. 🔴 **Both readings came from `legacy_reference/src/server.py` and `scripts/qualify_native.py` — dead reference code — and neither touched the 35 registrations in `src/librus_mcp/`.** The tier share was *identical* in both runs, so `ACTION DM`'s five-point falsifier would have passed a measurement drawn from a tree the package does not ship |
| 🔵 **what actually caught it** | 🟢 **Reading the row.** The classification flipped on a single subject between two instruments, and the only way to adjudicate was to open the files and count. 🔵 **A per-subject disagreement is a louder signal than a tier aggregate**, and the aggregate was what the falsifier was watching |
| 🟢 **the operational rule** | 🟢 **Pair every share-based falsifier with a per-subject diff.** Publish the rows whose verdict changed, not only the share that did or did not move — and when a repair changes a row's classification without changing the share, that row is the one to read |
| 🔴 **what would overturn it** | A population error on these shelves that a share-based falsifier did catch. 🔵 **None of the three that fired this pass was caught by its share**: `DK` was caught by a row count, `DL` by a median, `DM`'s real defect by reading one repository |
| **where it is enforced** | `NOT_SHIPPED` in `surface_gate2.py`, with `test_not_shipped_trees_are_excluded`; the probe emits `not_shipped_delta` per row so a whole-tree/shipped-tree disagreement is visible per subject rather than pooled |

### 🟢 `T33` STRENGTHENED — the conjunction channel takes a third form, and it keeps refusing correctly

`T33` said a hardcoded hostname and an ambiguous offset resolve each other. `ACTION DN` adds
the **URL-context** form and it holds:
[`p143-cctld-url-context`](../compose/code/p143-cctld-url-context/README.md).

🟢 **19 of 19 regions reproduced, 16 of 16 placed rows retained**, so the four homograph ccTLDs
(`.py`, `.do`, `.cu`, `.cl`) can be re-admitted behind a scheme requirement without losing
anything. 🟢 **And both halves of the rule fire on one host in one file**:
`alejooroncoy/campus-cli` carries `https://revistas.uh.cu/…` (admitted, Cuba) and five bare
`url.hostname === 'revistas.uh.cu'` comparisons (refused). It also yields `juris.pjud.cl`,
Chile's Judicial Branch.

🔴 **The hole is closed as a capability and unexercised for half of it.** No `.py` or `.do`
host with URL context exists anywhere in the 19-row population, so **Paraguay and the
Dominican Republic are unblocked rather than demonstrated** — and 🔴 **no row changed region**,
because the one row carrying Chile and Cuba was already placed on 30 Peruvian hosts.

### 🟢 `T29` STRENGTHENED, on a channel it did not have — the author, not the repository

`T29` narrowed origin to *"in the code when the code must reach a named host"*. `ACTION DJ`
adds a channel that reads neither code nor metadata:
[`p143-edunext-jurisdiction`](../compose/code/p143-edunext-jurisdiction/README.md).

🔴 **The pooled offset test was unreadable** — `MIXED` on 5 of 5 eduNEXT repositories, both
`-0500` and `-0400` inside and outside the DST window. 🟢 **The author is the unit that carries
a timezone**, and across 1 485 commits and 63 authors:

| | |
|---|---|
| 🟢 authors at `-0500` in **both** DST windows, never `-0400` | **13** (491 commits) |
| 🔴 authors with the US Eastern DST shape | **2** (28 commits) |

🔵 **`-0500` in January rules out US Central; `-0500` in July rules out US Eastern.** Neither
half places anything alone — which is `T33`'s structure applied to time rather than to
hostnames. With `edunext.co` on **998 of 1 485 commits**, eduNEXT books **LATAM**.

### 🔵 p143 on the environment: the clone channel opened, and the market blockers did not

🟢 **`git clone` of public repositories now works** — full history, full source. Every probe
this pass depends on it; `ACTION DJ` alone needed 1 485 commits of author metadata that no
single-file fetch could supply.

🔴 **One standing note needs correcting rather than repeating:** `api.github.com` is not
blanket-`403`. It answers **`200`** on `rate_limit` and refuses repository endpoints with a
**scope** message — *"sessions are bound to their configured repositories"*. 🔵 **A scope
refusal and a block have different fixes**, and this KB has been recording the symptom.
🔴 **Star counts remain unavailable either way.**

🔴 **And the figures blocker is unchanged, measured again this pass:**
`api.uis.unesco.org`, `sdmx.oecd.org`, `eur-lex.europa.eu`, `www.oecd.org` and `coe.int` all
answer `000`. 🔵 **So every regional market share in `intel/market.md` is still second-hand,
and the fix is still an allowlist rather than a better search.**

## Pass 142 — 2026-10-12

🔴 **Two of this KB's trends are rescoped and one of its own ten-pass findings is withdrawn — and
all three corrections came from the same source: an instrument whose refusals were not randomly
distributed.** 🔵 **`T30` was written one pass ago to stop a claim measured on one tier being
published as a claim about education software. It did not stop this one, because the defect here
is not scope — it is an instrument that cannot see a whole region and reports that as a zero.**

### 🔵 A register note, because this pass's numbers collide with the append-only history

`T32`–`T35` are the next numbers in the **current** register, which the 2026-10-06 reset
restarted at `T1`. 🔴 **The append-only logs still contain pre-reset uses of `T32`–`T35` meaning
entirely different things**, and so do `T26`, `T28` and `T30` — this KB has been living with that
since the reset without saying so. 🔵 **Stated now rather than discovered by a reader**: a `T`
number resolves against `intel/trends.md`, and a `T` number inside a dated section of
`agents/trending.md` or `repos/trending.md` resolves against the register that was current on
that date. The same applies to `P21`/`P22` in `compose/patterns.md`, where the pre-reset log
carries an unrelated *"`P22` check 4"*.

### 🆕 🔴 `T32` — a measurement channel's REFUSALS are evidence, and must be reported with the same weight as its results

| | |
|---|---|
| **the claim** | 🔴 **When an instrument declines to answer, publish the shape of what it declined, not only the count of what it found.** A channel whose refusals correlate with the question being asked returns a zero that looks exactly like a finding |
| 🔴 **what forced it** | `ACTION DH`. p141's offset channel placed **23 of 44** connector rows and returned 🔴 **0 LATAM and 0 North America**. **19 of 19 refusals were American offsets** — `-0300`, `-0400`, `-0500` — because those are precisely the offsets shared between the two American regions, and p141's table refuses any shared offset |
| 🔵 **why the zero was nearly published** | p141 pre-registered *"report the LATAM count explicitly, including when it is zero"*, reasoning that **an eleventh null on 44 rows beats a tenth on eight**. 🔵 **That reasoning is right about sample size and silent about instrument reach.** A bigger population measured through the same blind spot produces a more confident wrong answer |
| 🟢 **what caught it** | 🔵 **The region nobody was watching.** North America also came back zero, from a shelf carrying `SleepyPandas/UofT-MCP`, `skhdemo/uoft-quercus-mcp` and `luca-dupont2/mcgill-vsb-mcp`. 🟢 **An implausible zero next to the plausible one is what made the plausible one checkable** |
| **the operational rule** | 🔴 **Before publishing a regional null, ask the instrument for its refusals and check whether they cluster.** If every refusal falls in the region reporting zero, the zero is about the instrument. 🟢 **And report a second region's count even when nobody asked** — it is the cheapest available control |
| **where it is enforced** | `p142-origin-at-scale` prints the refusal list and per-region counts on every run; `test_origin_scale.py` asserts the five American offsets are still refused, so the limit cannot be silently removed either |

### 🆕 🟢 `T33` — a hardcoded hostname and an ambiguous offset resolve each other; neither resolves alone

| | |
|---|---|
| **the claim** | 🟢 **Two weak origin channels in conjunction are stronger than either alone, and the conjunction is publishable where neither half is.** An American commit offset under-determines the region; a hardcoded host names an *institution*, not an author. 🟢 **Together they close** |
| **the measurement** | [`p142-americas-disambiguation`](../compose/code/p142-americas-disambiguation/README.md): **16 of 19** rows the offset channel refused are placed — 🟢 **13 LATAM** (Brazil 9, Argentina 3, Peru 1) and **3 North America** (Canada) — each on an American-ambiguous offset **plus** a ccTLD host under exactly one candidate region |
| 🔵 **why it is safe** | There is no reading on which an author committing at `-0300` against `sigaa.ufpi.br` is in Greenland, and none on which one committing at `-0400` against `acorn.utoronto.ca` is in Bolivia. 🔴 **Three rows where only one half exists are left `UNMAPPED`** rather than placed on the half |
| 🟢 **the control that licenses it** | `alejooroncoy/campus-cli` was placed in **Peru** passes ago by *reading its README*. The instrument reproduces that placement from 16 hardcoded `upc.edu.pe` hosts, unprompted. 🟢 **An instrument that gets a known row right can be trusted on the unknown ones** |
| 🔴 **the cost, declared** | Four ccTLDs are unusable because they are filename extensions — `.py` Paraguay / Python, `.do` Dominican Republic / Struts action, `.cu` Cuba / CUDA, `.cl` Chile / OpenCL. 🔴 **So this channel cannot place a repository in those four countries at all** |

### 🔁 `T31` RE-CUT — the schema is not "in source instead of `.sql`"; a `CREATE TABLE` census is the wrong instrument for most of this shelf

| | |
|---|---|
| **p141's claim** | *"96 of 118 tables are invisible to a `.sql` reader"* — the authoritative schema of a Go/Rust/TS component is embedded in source, measured on **one** subject |
| 🟢 **the control** | [`p142-schema-location-tiers`](../compose/code/p142-schema-location-tiers/README.md) reproduces p141 **to the digit** on p141's subject: **118** tables, **22** in `.sql`, **19%** |
| 🔴 **what re-cut it** | `ACTION DD`. 🔴 **Neither registered subject declares a table in `CREATE TABLE` form anywhere.** `nitsuah/bb-mcp` has no persistence at all. `zijinz456/OpenTutor` has **34** `__tablename__` declarations, 148 model classes, 27 Alembic migrations, **0** `.sql` files — and a DDL census finds **1**, `alembic_version` |
| 🔵 **the corrected claim** | 🔵 **In `tutor-mcp` the DDL moved out of `.sql` into Go strings: still DDL, still greppable. In an ORM project there is no DDL to find.** So `T31` is a claim about **review method**, not about file extensions: a schema enumeration that greps `CREATE TABLE` returns zero on a project with 34 tables |
| 🔴 **why it matters beyond tidiness** | OpenTutor's 34 include `cognitive_baselines`, `concept_mastery`, `mastery_snapshots`, `preference_signals`, `intervention_outcomes`, `conversation_memories`, `integration_credentials`, `users`. 🔴 **A DPIA has 34 tables to enumerate and the conventional grep finds one** |
| 🟡 **denominators, stated** | 🔴 **One subject in each of two incompatible shapes.** Published as a method warning with both denominators of one visible, per `T30` |

### 🔁 `T30` RE-CUT — the split is npm-vs-everything, and p141's falsifier pointed the wrong way

| | |
|---|---|
| **p141's claim** | A static tool count bounds the live surface on the **npm connector tier** (12% dynamic) and not on the **agent-server tier** (50%) |
| **the third tier** | [`p142-github-only-tier`](../compose/code/p142-github-only-tier/README.md): GitHub-only connectors, 6 servers, 🔴 **3 dynamic = 50%** |
| 🔴 **the inversion** | p141 wrote: *"Refuted if the share matches the npm tier's 12% rather than the agent tier's 50% — which would mean the split is npm-vs-everything."* 🔴 **Backwards.** These rows are *connectors*; a connector-like 12% would have shown the axis is **connector-vs-agent**. 🔵 **50% on a connector tier is exactly what shows the axis is npm publication** |
| 🔵 **so the falsifier was silent while the thing it was built to detect happened** | 🟢 **Which is why a pre-registration has to state the measurement AND the inference separately.** The number was predicted correctly and read wrongly |
| 🔴 **what is NOT claimed** | 🔴 **No mechanism.** Why publishing to a registry should correlate with literal registration is unestablished; asserting a cause here would be the same error one layer up. `ACTION DL` tests the obvious candidate (npm rows are smaller) and will demote `T30` to an observation if it fails |
| 🟢 **the clean sub-finding** | 🟢 **`GATED` is now 0 of 18 servers across three tiers.** `T28`'s rescoping to `tutor-mcp`'s maturity is confirmed a third time |

### 🆕 🔴 `T34` — `LITERAL` and `DYNAMIC` were never the two options; there is a third shape and every instrument here is blind to it

| | |
|---|---|
| **the claim** | 🔴 **A tool name can be produced by reflection and never written as a string at all.** Any instrument that counts name literals or registration sites reports **zero** for such a server |
| **shape 1 — `REFLECTION`** | `oliverhruby/edupage-mcp`: a bare `@_tool` decorator wrapping `server.tool()`, with the tool name taken from `fn.__name__`. 🔴 **31 tools; p141's gate returns 0** |
| **shape 2 — multi-line registration** | `malkreide/global-education-mcp`: `@mcp.tool(` with `name="…"` on the following line. 🔴 **10 tools; p141's line-oriented regex returns 0** |
| 🔵 **why it is a trend and not a bug report** | Both rows are **fully literal and fully bounded** — the most auditable shape there is — and both read as unmeasurable. 🔴 **An instrument that cannot see the best-behaved rows under-reports exactly the population a studio should prefer** |
| 🟢 **why the published figures survive** | Hand-reading puts both at `BOUNDED_STATIC`, so the three tiers' dynamic shares are unchanged. 🟢 **Stated because the correction flatters nothing: the numbers held, the instrument did not** |
| **registered** | `ACTION DM`, with a falsifier that withdraws all three of `T30`'s figures if repair moves any tier by more than five points |

### 🔁 `T10` AMENDED — the search channel is not saturated; it was being asked the wrong kind of question

| | |
|---|---|
| **p141's version** | *"Run the regional sweep to confirm saturation, not to find rows"* — after three consecutive passes of zero new findings |
| 🔴 **what amended it** | The eight registered queries returned nothing again. 🟢 **A ninth, describing an artefact instead of an industry — `open source education MCP "agente IA" GitHub Brasil Argentina México universidad` — returned four live repositories, two of them LATAM-placed** |
| 🔵 **the corrected instruction** | 🔵 **Industry-shaped queries retrieve market-research marketing pages; artefact-shaped queries retrieve repositories.** Same engine, same hour, same region. 🟢 **`P138-H` recorded this for registries and it generalises to search**: name the code, the platform, the language, the country — never the market |
| 🟡 **what remains true** | 🔴 **The figure channel IS saturated, and worse than saturated**: every primary statistical source is unreachable here, so the demand side can only be re-quoted. 🔵 **That half of `T10` stands and is now a network finding rather than a sampling one** |

### 🆕 🟢 `T35` — the shelf's best rows declare their own surface, and two of them did it before this KB asked

| | |
|---|---|
| **the claim** | 🟢 **Machine-readable self-declaration of a tool surface is appearing on this shelf without prompting, and it makes four of this KB's instruments unnecessary against the rows that have it** |
| **evidence 1** | `oliverhruby/edupage-mcp`: **31 of 31** tools carry a declared MCP `ToolAnnotations` class — 19 `_READ`, 4 `_WRITE_SAFE`, 3 `_LOCAL_WRITE`, 3 `_WRITE_DESTRUCTIVE`, 2 `_WRITE_NON_IDEMPOTENT`. 🟢 **12 of 31 writes, quotable rather than derived** |
| **evidence 2** | `malkreide/global-education-mcp`: 10 of 10 annotated, all `readOnlyHint: true`, and 🟢 **a committed `tools.lock.json` holding a SHA-256 per tool over its annotations, description and schema** |
| 🔵 **the significance** | This KB built `p139-tool-count-drift`, `description-drift-audit`, `p141-agent-surface-gate` and `p142-github-only-tier` to detect what that lockfile prevents. 🟢 **The repository's own comment names the intent**: the logging wrapper preserves `__doc__` *"damit der `tools.lock.json`-Hash stabil bleibt"* |
| 🔴 **the counter-evidence, in the same pass** | `@owen-x-tech/canvas-mcp`'s README claims **150+ tools** against **62** measured three independent times. 🔴 **Self-declaration is a practice, not a property of the ecosystem** — and it inverts `P138-E`'s *"drift under-documents rather than over-claims"* on the one row whose repository is gone |
| **adopted as** | pattern `P21` |

## Pass 141 — 2026-10-12

🔴 **Four of six pre-registered falsifiers fired, and three of this KB's own trends are rescoped
rather than extended.** 🔵 **The pattern across all three is the same: a claim measured on one
tier was carried as a claim about education software.** `T18` was rescoped by `ACTION CV` two
passes ago; `T28` and `T29` are rescoped here, and `T30` is the general rule that keeps it from
happening a fourth time.

### 🔁 `T28` RESCOPED — flag-gated tool registration is one row's maturity, not a property of agent servers

| | |
|---|---|
| **p140's claim** | *"A tool surface is a property of a DEPLOYMENT, not of a package"* — generalised from `tutor-mcp`'s `deps.Institution` / `REGULATION_GOAL` gates |
| 🔴 **what fired it** | `ACTION CZ`. 🔴 **0 of 5** tutoring-agent rows is flag-gated — and only **4 of 5** are MCP servers at all. [`p141-agent-surface-gate`](../compose/code/p141-agent-surface-gate/README.md) |
| 🔵 **the rescoped claim** | 🟡 **Gating is a maturity signal, not a tier property.** Exactly one row on these shelves gates registration, and it is the one with 459 commits, 286 test files and a database-enforced audit log. 🔴 **For every other row, the deployment cannot change the surface — which means the static count IS the surface, and nobody is hiding an institutional tier behind a flag because nobody has built one.** |
| 🔴 **what would overturn it** | A second row that gates registration on configuration. 🔵 **This is now a thing to look for rather than a thing to assume** — and `EduBase/MCP`'s `EDUBASE_READONLY` is the nearest candidate on the shelf, though it gates *behaviour* rather than registration and the distinction is the whole point of `T28`. |

### 🔁 `T29` NARROWED — origin is in the code only when the code must REACH somewhere

| | |
|---|---|
| **p140's claim** | *"Origin lives in the code, not in the metadata, and nine passes looked in the wrong place"* |
| 🔴 **what fired it** | `ACTION CY`. 🔴 **The repository layer places 0 of 6 rows**, and for **4 of the 6 there is no reachable repository at all**: 3 declare no `repository` field in any published version, and a 4th declares one that is not publicly readable. [`p141-repo-origin-layer`](../compose/code/p141-repo-origin-layer/README.md) |
| 🔵 **the narrowed claim** | 🟢 **Origin is in the code when the code has to reach a named host to work.** A compiled-in `moodle-app2.let.ethz.ch` is a *binding* — the server does not function pointed elsewhere. 🔴 **Nothing else in "the code" carries origin**, and repository metadata carries none at all: 5 of 8 npm rows declare no repository, 6 of 8 maintainer addresses are free-mail, and **0 of 8 ship a funding file.** |
| 🟢 **and one layer DOES work that p140 did not try** | A **Maven `groupId`**: `uk.ac.ox.ctl:spring-security-lti13` places EMEA with no inference, because `uk.ac.ox` is a namespace the University of Oxford had to control in order to publish. 🔵 **Stronger than an npm author field for exactly that reason** — publishing to a reverse-DNS namespace is gated, filling in an author field is not. |

### 🆕 `T30` — a measurement's TIER is part of its claim, and this KB has now broken that rule three times

| | |
|---|---|
| **the claim** | 🔴 **A property measured on one packaging tier must be published with that tier named, because the tiers differ by more than noise.** Three instances, all this KB's own: `T18`'s per-file notice (1 of 21) was npm/TypeScript only, and `ACTION CV` rescoped it. `T28`'s gating was one Go repository, and `ACTION CZ` rescoped it. 🔴 **And `BOUNDED_STATIC` — p140's *"7 of 8, provable without execution"* — inverts one tier up: dynamic registration is **1 of 8 (12%)** on npm connectors and 🔴 **2 of 4 (50%)** on agent servers.** |
| 🔵 **why it keeps happening** | Each measurement was *correct*. The error is in the sentence, not the instrument: a shelf is written as though it were one population when it is several, and the honest denominator is per tier. 🔵 **`T21`'s licence-payload gradient is the counter-example that proves the rule** — PyPI **0%**, npm **33%**, Maven **83%** — because it was stated per ecosystem from the start and has survived four falsifiers. |
| 🔴 **the operational consequence** | 🔴 **A static tool count bounds the live surface on npm connectors and does NOT on agent servers.** `ahmedEid1/lumen` serves 10 tools where a literal count returns 1; `nirholas/ai-tutor-mcp` serves 2 where it returns 0 — the same `for (const t of TOOLS) registerTool(t.name, …)` idiom as p140's 61-tool blind spot. 🔵 **So p140's blind spot was never an outlier; it is the ordinary shape of a table-driven server.** |
| 🔴 **what would overturn it** | A trend on these shelves that holds at the same rate across npm, PyPI, Maven and repository-only tiers. 🔵 **`T21` is the only candidate and it holds as a GRADIENT, not a constant** — which is the rule restated, not an exception to it. |

### 🆕 `T31` — a schema has a LOCATION, and `.sql` files are increasingly not it

| | |
|---|---|
| **the claim** | 🔴 **In a Go, Rust or TypeScript component, the authoritative schema is embedded in source as migration bodies, and the `.sql` files that exist alongside it are a minority.** Measured on `ArnaudGuiovanna/tutor-mcp`: `db/*.sql` declares **22** tables, non-test `db/*.go` declares **111**, 🔴 **96 are `GO_ONLY`** — a reviewer reading the conventional place sees **19%**. [`p141-schema-location`](../compose/code/p141-schema-location/README.md) |
| 🔴 **why it is a compliance trend and not a tidiness one** | 🔴 **The split falls ACROSS a DPIA rather than along it.** `learners` (holding `email TEXT UNIQUE NOT NULL`) and `interactions` are `SQL_ONLY`; 🔴 `pedagogical_decisions`, `assessment_attempts` and `audit_events` are **all Go-only**. 🔵 **A records-of-processing exercise that enumerates `db/*.sql` finds the learner's email and misses every table recording what was decided about them** — the opposite of the omission one would guess, and the half that an EU AI Act **Annex III** review needs most. |
| 🔵 **the generalisation** | `T26` said a licence grant has a depth. `T31` says a **schema** has a location. 🔵 **Both are instances of the same error: looking in the file whose name matches the question.** The component is not at fault — embedded migrations are ordinary practice — and the defect is in the review method. |
| 🔴 **what would overturn it** | A Go or TypeScript education component whose `.sql` files are authoritative and complete. 🔵 **One subject is one subject**, and per `T30` this claim is published with its tier named: it is measured on a single Go row and is a *hypothesis* about that tier, not a rate. 🔴 **Refuted if the next Go or Rust row measured declares the majority of its tables in `.sql`.** |

### 🟢 `T26` STRENGTHENED — inheritance is the majority shape, not two artefacts' quirk

`ACTION DC` walked every Maven coordinate this KB cites. 🔴 **Three further rows change
verdict**, so cumulatively 🔴 **5 of 9 (56%) declare no licence in their own POM.** The sharpest
is `org.verapdf:verapdf-library:1.30.3` — the PDF/UA **accessibility validator** — whose grant
is a **dual GPL-3.0 / MPL-2.0** offer two levels up, on a coordinate that is `<packaging>pom`
and publishes **no jar at all**. 🔵 **`org.sonatype.oss:oss-parent:7` is the shared grandparent
of two chains and declares nothing**, so a walk must continue past a silent ancestor rather
than stop at it. [`p141-pom-chain-sweep`](../compose/code/p141-pom-chain-sweep/README.md).

### 🔵 `T21` holds and sharpens, on a layer below the one it was measured on

`ACTION DA` found `openedx-core` **1.9.1** — p140's cleanest licence payload — carrying 🔴
**zero licence files, zero SPDX headers and zero copyright lines across 237 Python files in six
packages**, under a distribution that ships 35 139 bytes of AGPL-3.0-only text.

🔵 **Both findings are true of different layers, and the pair is the useful statement: a
`T21`-clean artefact can be `T18`-silent.** 🔴 **And the layer that matters for a studio is the
silent one**, because the normal use is lifting a subtree, not installing a wheel — at which
point the most reciprocal obligation on these shelves travels with code that announces nothing
about itself.

### 🟢 `T25` upgraded from inference to DECLARATION

p139 inferred synthetic history from commits spaced 7 316 seconds apart. 🔵 **Two rows now
declare it themselves**: `zijinz456/OpenTutor` carries a `Co-Authored-By: Claude` trailer on 🔴
**151 of 191 commits (79%)**, `ArnaudGuiovanna/tutor-mcp` on 51 of 459 (11%). 🟢 **Not a
defect** — `tutor-mcp` ships 286 test files against 279 source files — 🔴 **but commit count is
now unusable as a proxy for human engineering effort or for bus factor**, and the signal is
free to read.

### 🔵 p141 on `T10`: the search channel returned ZERO new findings — a THIRD consecutive null pass

Four global queries and four regional ones, run as mandated. Every candidate returned is already
in this KB: the Digital Education Council LATAM 2026 survey (**92%** students / **79%** faculty,
30 000+ responses, 29 institutions) and its **~30%** published-policy figure; UNESCO IESALC +
UNU-IAS (**200 HEIs, 19 countries, 87% using AI, 26% with a strategy**); **ILIA**; CMU + Gates
Foundation **$55M**; OpenAI's **eight** national education partners; TCS + Pearson; LearnUpon's
Sydney HQ; Chile's 2021 national AI policy; Mexico's explicitly non-binding SEP/ANUIES guidance.

🔵 **Three passes of nulls is no longer a sampling accident; it is a finding about the channel.**
The demand side of this industry is being described by the same handful of surveys, re-quoted;
the artefact side produced **six verdicts and four refutations** in the same hour at a fraction
of the cost. 🟢 **`T10` is restated as a budgeting instruction**: the regional search sweep is
worth running to *confirm* saturation, not to find rows, and a pass should not be judged by what
it returns.

### 🔴 The refusal ledger, unchanged in substance and extended by one channel

| channel | status |
|---|---|
| 🟢 `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`, `repo1.maven.org`, `github.com` (smart-HTTP), `raw.githubusercontent.com` | reachable |
| 🔴 `api.github.com` | `403` |
| 🔴 government **and** university hosts | `403` at `CONNECT` |
| 🔴 executing an installed npm connector | refused by sandbox policy |
| 🆕 🔴 **rendered `github.com` HTML (`curl -sI`)** | 🔴 **`403` for EVERY repository — live, private or nonexistent alike** |

🔵 **The new entry is a measurement hazard rather than a blocked lane.** An earlier draft of this
pass nearly read four `403`s as four dead repositories. 🟢 **`git ls-remote` against a
deliberately nonexistent control is the only valid liveness probe here**, and it now runs on
every invocation of `p141-repo-origin-layer`. 🔴 **A fourth consecutive pass with no primary
regulatory source read**; the cause remains an allowlist, and it belongs to whoever owns this
environment rather than to a probe.


## Pass 140 — 2026-10-12

🔵 **This pass was refused the probe it registered, answered the question from source instead,
and refuted three of its predecessor's findings in the process.** Two of the four new trends
below are corrections to p139 rather than additions to it.

### 🆕 `T26` — a licence grant has a DEPTH, and a scanner that reads one file reads the wrong answer

🔴 **Both Maven artefacts p139 recorded as declaring nothing DO declare a licence — two and
three levels up their parent-POM chains.** `ACTION CR`'s falsifier fired exactly as written:

| artefact | own POM | inherits | from | depth |
|---|---|---|---|---|
| `net.oauth.core:oauth` 20100527 | 🔴 nothing | 🆕 **Apache-2.0** | `net.oauth:oauth-parent:20090531` | 3 |
| `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🔴 nothing | 🆕 **ECL-2.0** | `org.sakaiproject:oss-parent:1` | 4 |

🔵 **`T17` said a licence identifier is not a licence. `T26` says the absence of an identifier
is not the absence of a licence.** The grant exists; it is three files and one `groupId` change
away from where anyone looks. 🔴 **`net.oauth.core:oauth`'s grant lives under a DIFFERENT
`groupId`** (`net.oauth`, not `net.oauth.core`), which is why sixteen years of use never
surfaced it.

🔴 **And the correction makes the defect worse, not milder.** With inheritance resolved, **5 of
5** Maven artefacts on this shelf declare a licence and 🔴 **4 of 5 (80%)** ship no licence text
in the jar — against p139's 40–67% and npm's 33%. 🔵 **So `T21` survives its own correction with
a steeper gradient: PyPI 9%, npm 33%, Maven 80%.** The practical rule for a studio is unchanged
in direction and sharper in degree: *a Java dependency's grant is probably not in the artefact,
and may not be in its POM either.* Measured in
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🆕 `T27` — a package name can be RETIRED while the registry still answers to it

🔴 **`openedx-learning` 0.33.0 and 0.33.1 are not broken releases. They are a deliberate rename
shim**, and p139 read the symptom as a defect. The 0.33.1 `setup.py` says so in its own
docstring:

> *"Builds a final shell release of openedx-learning which simply 'redirects' to openedx-core"*

with `packages=[]`, `install_requires=["openedx-core==0.34.1"]`, and
`Development Status :: 7 - Inactive`. 🟢 **So `pip install openedx-learning` WORKS** — it resolves
the shim and installs `openedx-core`. p139's *"`pip install` resolves to the empty one"* is true
of the bytes and wrong about the outcome.

🔴 **The real finding is that this KB was tracking a retired name for two passes.** The live
artefact is [`openedx-core`](https://pypi.org/project/openedx-core/) **1.9.1**, uploaded
**2026-10-09**, versioned to continue exactly where the shim points (first release `0.34.1`), and
it consolidates six top-level packages — `openedx_core`, `openedx_learning`, `openedx_tagging`,
`openedx_catalog`, `openedx_content`, `openedx_django_lib` — into one distribution.

🟢 **It also vindicates `T21`'s mechanism on the newest artefact on the shelf.** `openedx-core`
1.9.1's wheel carries `dist-info/licenses/LICENSE.txt` (**35 139 B**) with
`License-Expression: AGPL-3.0-only` and `License-File: LICENSE.txt` under Metadata-Version 2.4 —
textbook **PEP 639**, the grant shipped by the build system rather than by the maintainer.
🔵 **And it removes p139's single PyPI hit: the one row in that denominator was a shim with no
code, so PyPI's declared-but-absent rate on this shelf is 0 of 10, not 1 of 11.**

🔵 **The rule this yields is a freshness check, not a licence check**: *before carrying a package
row forward, read its latest release's `Development Status` classifier and its `long_description`
for a rename.* Both signals were in the artefact p139 downloaded.

### 🆕 `T28` — a tool surface is a property of a DEPLOYMENT, not of a package

🔴 **`ACTION CP` asked whether a live `tools/list` matches a build's static tool count. On the
npm shelf it must — and on the first non-JavaScript row this KB has read, it does not.**

[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) registers **55** tool
names in non-test sources, and 🔴 **its own CI-enforced test asserts a live `tools/list` of 46**
(`tools/tools_register_test.go:221`). Three gates explain the gap — `deps.Institution`,
`REGULATION_GOAL`, `deps.OAuthGranularScopes` — and the repository states the principle in its
own comment:

> `// [1] GoalDecomposer — gated by REGULATION_GOAL=on. When off, neither tool is`
> `// registered, so the surface is invisible to the LLM and the system prompt has no`
> `// instruction to call them.`

🔵 **This retires the question "how many tools does this connector have?"** There is a count per
configuration. 🟢 **On the eight npm rows the count is still forced** — every one is a single
server instance registering literal names with no gate, so static *is* live there, provably,
without running anything. 🔴 **But no payload read can tell a studio which flags a client's
deployment sets**, which is why `P18` step 5 survives and why it is now written per
configuration rather than per package.

🔴 **A second shape makes the same point without a flag.** `@owen-x-tech/canvas-mcp` 1.1.0 builds
**two** MCP server instances in one file, selected by `--http`. Both happen to expose 62 tools —
but the HTTP path registers **1** by name literal and 61 through
`for (const tool of tools) httpMcp.registerTool(tool.name, …)`. 🔵 **A name-literal count of that
path returns 1 where the server serves 62**, and that 61-tool blind spot is invisible to every
instrument this KB has used until now. *Two transports on one server is one surface; two server
instances is two.* Measured in
[`p140-live-surface-bound`](../compose/code/p140-live-surface-bound/README.md).

### 🆕 `T29` — origin lives in the code, not in the metadata, and nine passes looked in the wrong place

🟢 **`ACTION CU` booked two regions on evidence that is not a name**, after nine passes of
recording an ownership gap:

| row | evidence | region |
|---|---|---|
| `eth-moodle-mcp` 1.3.3 | `moodle-app2.let.ethz.ch` (**4×**), `safari.ethz.ch` | 🟢 **EMEA** — ETH Zürich |
| `mcp-canvas-lms` 1.0.5 | `canvas.ust.hk` (**2×**), compiled into a request path | 🟢 **APAC** — HKUST, Hong Kong |

🔵 **Both halves of the action's falsifier are true, of different layers, and that is the
trend.** 🔴 **The npm metadata layer carries no origin signal**: 5 of 8 payloads declare no
author at all, and the two that do give a personal `gmail.com` address and a bare name. 🟢 **The
code layer carries it plainly**, because a hardcoded hostname is a *binding* rather than a label
— an author field can claim anything, but the server has to reach the real host to function.

🔴 **The sharpest instance is a defect as well as evidence.** `mcp-canvas-lms` reads
`CANVAS_BASE_URL` in `dist/common/utils.js:4` and then ignores it in
`dist/operations/canvas.js:58`, which hardcodes `https://canvas.ust.hk/api/v1/courses`. 🔵 **One
of its three tools is wired to HKUST whatever the client configures** — the same class as
`eth-moodle-mcp`'s *"Works with Any Moodle"* plus ten hardcoded `ddca_*` tools, one step worse
because this one claims configurability and silently drops it. 🔴 **Two of eight rows advertise
"any instance" and hardcode one institution.**

🟡 **The gap is narrowed, not closed: 6 of 8 rows still yield nothing.** And the inverse case is
worth recording — `overhangio/tutor`'s `pyproject.toml` names **Edly**, which is *correct and
current* (Edly, the edtech arm of Pakistan-based Arbisoft, acquired Overhang.IO on 2023-03-27 and
Tutor's founder Régis Behmo leads its technical direction there), while the **GitHub organisation
name is the stale signal**. 🔵 **A row's org name is not evidence of anything**, which is `T29`
reached from the other direction. Measured in
[`p140-origin-evidence`](../compose/code/p140-origin-evidence/README.md).

### 🔵 p140 on `T10`: the search channel returned ZERO new findings in four regions and Global

🔴 **Every regulatory and market candidate this pass's search battery returned was already in
this KB.** The mandated sweep ran globally and once per region; each hit was then grepped against
`intel/` before being written, per the rule `T24` created. The result:

| candidate from this pass's searches | already held in |
|---|---|
| `H.R. 8747` K-12 AI Literacy and Readiness Act, 134 bills / 31 states, CA `AB 1159`, Oklahoma + Maryland oversight, NYC moratorium | `intel/market.md`, `intel/trends.md` |
| EU AI Act omnibus dates, EMEA market ~$2.64B, OECD *Digital Education Outlook*, Finland/Estonia/Netherlands, UK £4M | `intel/market.md`, `intel/trends.md` |
| Vietnam Law `134/2025/QH15`, Korea AI Basic Act 2026-01-22, Taiwan AI Basic Act, Australia National AI Plan | `intel/market.md`, `intel/open-gaps.md` |
| UNESCO IESALC + UNU-IAS (200 HEIs, 19 countries, 87%/74%/26%), DEC LATAM 79%, Uruguay, Colombia CONPES 4144, Peru 31814, Brazil 15.211 | `intel/market.md` |
| 86% adoption, VC $1B H1 2026 −26%, 29% student confidence, faculty intent 76%→67% | `intel/market.md` |

🔵 **This is `T10` at its strongest statement yet: the demand-side search channel is now
returning this KB's own contents.** 🟢 **Stated as an informed gap rather than left as silence** —
a pass that published these as `🆕` would have inflated its novelty by a dozen findings, which is
precisely the `T24` failure mode. 🔴 **The entire yield of this pass came from reading artefacts**,
and that is now the expected shape rather than a surprise.

### 🔴 p140 adds a second entry to the refusal ledger, and widens the first

p139 diagnosed its blocked action as *"the environment's network policy refuses government
hosts."* 🔴 **That diagnosis was too narrow, and a new blocker sits beside it:**

| channel | status | note |
|---|---|---|
| 🟢 `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`, `repo1.maven.org`, `github.com` (smart-HTTP), `raw.githubusercontent.com` | reachable | the whole of this pass's evidence came through these |
| 🔴 `api.github.com` | `403` | — |
| 🔴 government hosts **and 🆕 university hosts** | `403` at `CONNECT` | `canvas.ust.hk`, `moodle-app2.let.ethz.ch`, `safari.ethz.ch` all refused — 🔵 **the policy is an allowlist of registries plus GitHub, not an exclusion of governments** |
| 🔴 🆕 **executing an installed npm connector** | **refused by sandbox policy** | a *different* mechanism from the network refusals, and the reason `ACTION CP` ran as a source read |

🔵 **Neither is a probe to re-register.** The first is a request to widen a network policy; the
second is a request to widen an execution policy. Both belong to whoever owns this environment,
not to the next action list.

### 🟢 p140 confirms p139's instrument by reimplementation, and finds one latent defect in it

🟢 **An independently written tool extractor reproduced `p139-tool-count-drift`'s counts exactly
on all eight rows** — 227, 62, 54, 18, 17, 16, 14, 3. 🔵 **That agreement is worth more than a
re-run**, and it took a correction to reach: this pass's first draft reported 17 where p139 said
16, 4 where it said 3, and 64 where it said 62. 🔴 **p139 was right every time**; the cause was
omitting its `SERVER_CTOR` exclusion, so `new McpServer({ name: 'moodle-mcp' })` read as a tool.
*The server's own name is not a tool, and a probe that does not know this inflates every row by
one.*

🔴 **One latent defect found.** `header_holder.extract_holder("Copyright © 2024")` returns
**`"2024"`** — a nameless notice lets the year fall through into the holder capture. 🟢 **p139's
published results are unaffected**; its three rows contain no nameless notice, and an audit of its
committed detail table finds zero year-shaped holders. 🔴 **It fired on the first new row this
pass read**: `adaptlearning/adapt_framework` ships `"attribution": "Copyright © 2024"`, which
unguarded publishes `2024` as a foreign copyright holder of the repository. 🔵 **p139's committed
code is left untouched** — its result is a dated record and editing the instrument beneath it
would invalidate rather than correct it. The guard and its tests live in
[`p140-rootonly-header-reach`](../compose/code/p140-rootonly-header-reach/README.md).

## Pass 139 — 2026-10-12

### 🆕 `T21` — the registry's default build behaviour decides whether the grant ships

🔵 **The strongest new trend this pass is not about licences at all. It is that an ecosystem's
packaging DEFAULTS determine its compliance posture**, and the three big registries differ sharply.

| registry | declared-but-absent licence rate | why |
|---|---|---|
| 🟢 **PyPI** | **9%** (1 of 11, and that one ships no code) | **PEP 639**: setuptools/hatch copy licence files into `dist-info/licenses/` automatically |
| 🔴 **npm** | **33%** (7 of 21, p138) | `files` names what to pack and omits absent entries **silently** |
| 🔴 **Maven Central** | **40–67%** (2 of 3 declaring) | `<licenses>` is metadata in a sibling POM; the jar is untouched unless configured |

🔵 **The consequence for a studio is directional and actionable: a Python dependency's grant is
probably in the artefact; a Java or Node dependency's grant probably is not.** That is a review
budget, not a slogan. Measured in
[`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

### 🆕 `T22` — the agentic write surface is outrunning its own documentation

🔴 **Across the nine measured npm connectors: 411 tools registered, 249 documented, 162
undocumented — and 62 of those (38%) MUTATE the LMS.** The undocumented set is not a random sample
of the documented one; it concentrates on exactly the capabilities a governance review exists to
catch: `bulk_update_grades`, `grade_submission`, `create_user`, `update_user_login`,
`update_sso_settings`, `submit_assignment`.

🔵 **This is `T22` and not a bug report because it is where two threads of this KB collide.**
Vietnam's **Decision 33/2026/QĐ-TTg** and **EU AI Act Annex III** both name *grading or ranking
learners* high-risk. 🔴 **A duty cannot be discharged against a capability nobody has enumerated** —
and the README is the artefact most procurement processes actually read. The practical rule:
**enumerate `tools/list` against the running server and diff it against the documentation**, every
time, as a delivery gate.

### 🆕 `T23` — "install from npm" increasingly means "download a binary at first run"

🔴 **`@exhabition/brightspace-mcp` ships an 82-line loader and no server**: it fetches a
platform-specific Rust binary from GitHub Releases, follows up to five redirects, extracts,
`chmod 0o700`, `spawn`. 🔴 **No checksum, no signature.** The version is pinned; the bytes are not.

🔵 **The trend is the rewrite of MCP servers into compiled languages, with npm retained as a
distribution front door.** It is good for performance and bad for auditability, and it defeats both
of the layers this KB has been measuring: the repository layer (the Rust source is in a *different*
repository, 🆕 [`Exhabition/brightspace-mcp-rs`](https://github.com/Exhabition/brightspace-mcp-rs))
and the payload layer (the npm payload contains nothing to audit). 🟡 **Expect more of these, and
expect licence and tool-count probes to return zeroes that are correct and uninformative.**

### 🔵 `T24` — 🔴 **NOT A NEW TREND. This pass rediscovered `T16` and nearly published it twice**

🔴 **A regional sweep this pass returned the EU Annex III deferral as if it were news, and it is
already in this file**: `T16` (p137) records **Regulation (EU) 2026/1744**, in force
**2026-07-27**, deferring Annex III — where education sits — from **2026-08-02** to
**2027-12-02**, Annex I embedded to **2028-08-02**, with **Article 50 transparency NOT deferred**
and a grace period to **2026-12-02** for systems already on the market.

🔵 **It is recorded here as a near-miss rather than deleted, because the failure mode is the one
this KB is most exposed to.** A regional search battery run fresh each pass will keep returning
the same instruments, and a pass that writes up every hit as `🆕` inflates its own novelty. 🟢 **The
check that caught it was grepping this file for the date before writing the entry** — which is now
the rule: *before booking a regulatory finding as new, grep `intel/` for its date and its
instrument number.*

🟢 **What the sweep did add, and it is small:** two procedural dates `T16` does not carry —
**Council approval 2026-06-29** and **OJ publication 2026-07-24** — and independent corroboration
of the deferral from a different source set than p137 used. 🔴 **Both remain secondary.**

🔴 **And the pass can now say WHY they remain secondary, which `T16` could not.** `eur-lex.europa.eu`
is not unreachable by accident: the proxy gateway **answers `403` to `CONNECT`**, as it does for
`digital-strategy.ec.europa.eu` and `sdaia.gov.sa`. 🔵 **This environment's network policy permits
package registries and `github.com` and refuses government hosts** — so "read the Official Journal"
is not a probe the next pass should register again. It is a request to widen the policy, and it
belongs to whoever owns this environment rather than to the next action list.

### 🟡 `T25` — provenance signals are being manufactured, so history depth is no longer a maturity proxy

While resolving the `moodler-mcp` duplicate, the commit history of
`GhaithAlHallak8/moodler-mcp` turned out to open with ~20 commits spaced **7 316–7 317 seconds
apart — every single one**, all `+04:00`, starting at exactly `09:00:00`, each with a tidy
conventional-commit message. 🔴 **Human work does not land on a two-hour metronome.** The later
history is organic (dependabot, github-actions, release-please, real PR numbers), so the repository
became real after it was staged.

Separately, **30 of the 459 commits** on the strongest new tutoring row,
[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp), are authored by
`Claude`.

🔵 **Neither fact is a defect, and neither is graded here.** The consequence is narrow: **commit
count and commit dates are no longer evidence of elapsed human effort**, which is precisely what
this KB's `p109-freshness` and `p110-bus-factor` instruments read them as. 🟡 **Recency still means
the code is being worked on; depth no longer means the project is old.**


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟢 **`T17` was fired at and survived.** p138 added it one pass ago and
registered its own falsifier: *if the grants live in source-file headers rather than licence files,
7 of 21 is an overstatement.* 🔴 **`ACTION CH` read every shipped text file in all 21 payloads and
found 0 of the 9 carrying their own header grant** — so `T17` holds and is now **strengthened**
with the clause below. 🆕 **`T18` is added**, and it is the operational half of `T17`: per-file
notice is practised by **1 of 21** rows, which is what decides whether a grant survives a partial
copy. 🔵 **No trend is added from the search channel this pass, because it returned nothing** —
11 searches, 0 new rows, 0 corrections, which is `T10` holding again.

### 🟢 p139 strengthens `T17`: the grants are not hiding in the source, and one "grant" was Meta's

| | |
|---|---|
| **the claim** | 🔴 An SPDX identifier without the text it names is **a third of the published education-connector shelf** — and the text is not elsewhere in the payload either |
| **the measurement** | **21** packages, all **sha1-verified** against the registry's own `shasum`. **9** ship no licence file *(independently re-measured, agrees with p138 exactly)*. 🔴 **0 of those 9 carry their own grant in a source header.** In **8 of 9** there is no copyright line, no SPDX tag and no operative licence sentence in any shipped text file |
| 🔵 **the near-refutation** | **1 of the 9 did** report a notice: `@owen-x-tech/canvas-mcp` 1.1.0, carrying `@license React … Copyright (c) Meta Platforms, Inc. and affiliates` at byte **1197** of a **572 657-byte** minified `dist/ui/mcp-app.html`. 🔴 **A bundler hoisted a dependency's notice into the header window**, and it points at a `LICENSE file in the root directory` the package does not ship. 🔵 **Position cannot attribute a notice** — the new rule treats a notice in minified output (any line over 2 000 B) as the bundle's, never the package's. Without that clause this trend would read as refuted by a React licence |
| 🔴 **what would overturn it** | A grant living where the probe does not look: a sourcemap, an extensionless script, a `LICENSE` spelled so p138's path matcher misses it, or authored source whose notice sits below the first 4 096 bytes. 🔵 The window is what separates a package's own header from a bundled dependency's text, but it is the assumption most likely to be wrong |

### 🆕 `T18` — a licence cell describes a tree; only a per-file notice survives a partial copy, and in THIS tier 1 in 21 has one

| | |
|---|---|
| **the claim** | 🔴 **Per-file notice is not a practice in the npm-published TypeScript education-connector tier: 1 of 21 rows — 5%.** On the other 20, a single file lifted out of the package names no holder and no grant. 🔵 **The tier is part of the claim** — see the `ACTION CV` rescoping below |
| **why it is not a restatement of `T17`** | `T17` is about packages with **no grant at all** (9 of 21). `T18` is about the **11 that are clean at the root and still unattributable file-by-file**. 🔵 A root `LICENSE` discharges redistribution of the *whole* package; it discharges nothing about the file a developer pastes into a client's codebase |
| **the one row that has it** | 🟢 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) **3.13.10**: `Copyright (c) 2026 Rohan Muppa … Licensed under MIT — see LICENSE file for details` in **100 of 118** shipped text files, **and the `LICENSE` ships**, so the reference resolves. 🟢 **56★** — neither the largest (547 paths) nor the most-starred row on the shelf |
| **what it changes in a room** | 🔴 *"It's MIT, just keep the notice"* is not actionable on this shelf. In 9 payloads there is no notice to keep; in 11 more it exists only as one root file that any partial copy drops. 🟢 **The deliverable is a notice-injection step in the build**, not a licence column in a slide |
| 🔴 **what would have overturned it** | The same census run over a tier that is **not** npm-published TypeScript. 🔴 **Registered as `ACTION CV` — and FIRED within the same pass by this pass's own concurrent lane. `T18` is rescoped below rather than left standing.** |

#### 🔴 `ACTION CV` fired on arrival: `T18` is a property of this tier, not of education software

🔴 **The falsifier was registered and answered in the same pass**, by
[`p139-source-header-holder`](../compose/code/p139-source-header-holder/README.md), which read
source headers over the three largest `ROOT_ONLY` repository rows for a different question
(ownership) and in doing so measured the quantity `T18` depends on:

| row | source files read | files carrying an OWN holder header | rate |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) *(Python/Odoo)* | 450 | **190** — all `OpenEduCat Inc` | 🟢 **42%** |
| [`frappe/lms`](https://github.com/frappe/lms) *(Python/JS)* | 1 411 | **166** — `Frappe` + `Frappe Technologies Pvt. Ltd` | 🟡 **12%** |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) *(PHP/Laravel)* | 660 | 🔴 **0** | 🔴 **0%** |
| *(this tier, for comparison — npm/TypeScript connectors)* | *21 packages* | *1* | 🔴 **5%** |

🔴 **The registered threshold was 20%, and `openeducat_erp` clears it by a factor of two.** 🔵 **So
`T18` is NOT a statement about education software, and the generalisation is withdrawn before it was
ever relied on.** The restated claim:

> 🔴 **Within the npm-published TypeScript connector tier, per-file notice is practised by 1 of 21
> rows.** Outside it, the practice is real but highly variable — **0%, 12% and 42%** on the three
> non-npm rows measured — so **the tier must be named whenever the figure is quoted.**

🔵 **The two lanes agree on the mechanism, which is what makes the rescoping trustworthy rather
than a retreat.** `ACTION CM` found the *licence-file* defect tracks each ecosystem's **default
build behaviour** — PEP 639 ships the licence for you, Maven's jar plugin does not, npm's `files`
array silently omits what is absent. 🔵 **`T18` is the same mechanism one layer down**: per-file
notice is a convention carried by an ecosystem's tooling and templates, and the npm/TypeScript
connector tier has neither. 🔴 **It is not that education developers are careless; it is that
`tsc` emits no header and `npm init` writes no template.**

🔵 **`academico-sis/academico` at 0% is the row that keeps `T18` from being purely ecological** —
a PHP row with no own notice at all, which is why the restated claim says *variable* rather than
*higher elsewhere*.

### 🔵 p139 on `T10`: the search channel returned nothing, and that is now the dominant cost finding

🔵 **11 searches — 4 global, 1 each for North America, EMEA, APAC and LATAM — produced 0 new rows
and 0 corrections** anywhere in this KB. Every repo, platform, figure and institution surfaced is
already carried, several with **better provenance here than the channel supplied**: the channel
offered UNESCO IESALC's 87%/26% as *2026* data, where [`market.md`](market.md) records that the
fieldwork ran **August–October 2025** and must be quoted as a baseline.

🔴 **One item was genuinely absent from this KB and could not be verified in this channel**: Texas
**HB 149 (TRAIGA)**, in force **2026-01-01**. `capitol.texas.gov` and `agora.eto.tech` both fail
DNS resolution here, so the statute could not be read and **nothing is published from the vendor
summaries that did return**. Registered as `ACTION CW` with the exact question. 🔵 **The secondary
sources agree that TRAIGA carries no curriculum or school-training mandate** — education appears in
its regulatory **sandbox** list and via a government-deployer disclosure duty — **so the likely
finding is a negative one**, which is precisely why it must not be asserted before it is read.

**Pass 138, 2026-10-12.** p137's sixteen trends retained. 🆕 **`T17` is added — the first trend this
KB has measured at the distribution layer rather than the repository layer, and it reframes every
licence cell on every page.** 🟢 **`T13` is narrowed for the third consecutive pass and is now one
interface wide rather than one standard version wide.** 🟢 **`T14` gains its first measurement in the
under-claiming direction**, which is the more dangerous one. 🆕 **`T16` gains a scope element the
English-language read had missed.** Each change states the measurement and what would overturn it.

### 🆕 `T17` — a licence identifier is not a licence, and a third of a published tier proves it

| claim | 🔴 **An open-source licence cell sourced from a repository describes the repository, not the artefact a client installs — and for a third of the published education-connector tier the artefact carries no licence text at all.** |
|---|---|
| measurement | **21** education-LMS connector packages (Canvas, Moodle, Brightspace, EduBase), every tarball **sha1-verified against the registry's own `shasum`**, 21 of 21 matching. 🔴 **7 (33%) declare an SPDX identifier and ship no licence file; 2 (10%) declare nothing and ship nothing; 12 (57%) are clean.** [`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md) |
| 🔴 the sharpest case | `moodle-mcp-server-aql` **0.1.7** declares **AGPL-3.0** across **141 shipped paths** with no licence text, while its repository carries a canonical **34 523-byte** grant |
| the mechanism | `canvas-mcp-server` **2.2.3**'s packed manifest **names `LICENSE` in `files`** and ships 8 paths containing none. npm silently omits a `files` entry absent from the tree |
| 🟢 direction | **all nine are the repository being better than the distribution**; not one package shipped a licence its repository lacked. So this is packaging discipline, not misrepresented licensing |
| what it changes | 🔵 **Every licence column in this KB is now a claim about a repository.** For any row a client will `npm install`, the payload is a separate question with a separate answer |
| 🔴 **what would overturn it** | A re-run finding the licence files present — which would mean the probe's path matcher is wrong, so the matcher is tested against real and near-miss filenames (7 tests, all passing). Or a licence-header read showing the grants live in source files rather than licence files, which would make **7 of 21 an overstatement of the defect and an understatement of the obligation**. 🔴 `ACTION CH` was registered for exactly this and has not run |
| 🔴 scope limit | npm only; four platform families; one registry search each. PyPI, Maven, crates unprobed. `moodler-mcp` **is not on PyPI (404)**, so part of the shelf has no payload layer to measure |

### 🟢 p138 narrows `T13` a third time: the residue is one interface, and it is a published extension point

| p137's clause | p138's measurement, in source |
|---|---|
| *"the 1.3 half of the gap"* — no RFC 8707-bound token for an MCP resource server | 🟢 **Present and named.** [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) `src/auth/oauth/authorization-server.ts` (**978 lines**) implements **RFC 8707 §7** canonical resource comparison as `normalizeResource()`, with **PKCE S256** and **dynamic client registration**; `resource-server.ts` (195 lines) publishes `/.well-known/oauth-protected-resource` and checks the **audience** |
| *"an adapter of about two weeks"* between three components | 🟢 **Still about two weeks, and no longer an estimate of unknown work.** `CanvasMCPServerConfig` accepts `oauthStore?: OAuthStore` — *"Embedders may supply their own implementation"* — and `OAuthStore` exposes `putClient`, `putGrant`, `putToken`, over a `Grant` carrying `CanvasConnection { refreshToken }` |
| 🔴 what still does not exist | 🔴 **An external verified subject cannot be injected.** The subject is established by `CanvasOAuthClient`, which redirects the user to Canvas. No code path accepts an LTI 1.3 assertion |

🟢 **So `T13` reduces to: the LTI→MCP seam is one store implementation, and it forks neither
library.** 🔴 **Overturned if** either library requires a patched release in practice — the
interface is published but the integration was **not executed** this pass, and `store.ts`'s
*"Update only, never create (QA S7, #356)"* comment on the Canvas-refresh path means the adapter
must `putGrant` before the first token call rather than relying on an upsert.

### 🟢 p138 extends `T14`: capability metadata drifts in BOTH directions, and under-claiming is worse

🔵 **`T14` has been measured only on over-claiming — connectors whose descriptions promised more
tools than they had. The first source-read of this pass drifts the other way.**

| repo | source | documented | 🔴 undocumented |
|---|---|---|---|
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (**MIT**, Go) | **19** tools (`mcp.NewTool`) | **14** | `download_resource`, `get_journal_entry`, `list_resources`, 🔴 **`submit_journal`**, 🔴 **`update_assignment`** |

🔴 **Two of the five are writes.** A client reading this README concludes the server is read-only;
it is not. 🔵 **For an education deployment that is a governance fact, not a documentation nit** — the
write surface is precisely what a data-protection review covers, and here it is larger than the
document the reviewer is handed. 🟢 **The clause `T14` gains:** *a tool count in a description is not
a measurement — and neither is its absence.*

🟢 **And one of `T14`'s recorded conflicts resolves in source, in the reassuring direction.**
`canvas-mcp-server@2.2.3`'s `build/index.js` registers **exactly 54** tools, all `canvas_`-prefixed,
against a HEAD README claiming **"50+ Tools"** — agreement. The surviving *"102 vs 126"* conflict
belongs to [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) and is
unchanged. 🔴 **`ACTION CI` therefore remains PARTIALLY discharged** — two repositories, not the tier.

### 🆕 p138 adds a scope element to `T16`: psychological assessment is in Vietnam's education list

🟢 **`T16` — that the first binding education-AI conformity regime in force is Vietnam's, not the
EU's — is unchanged and firms up.** Decision **33/2026/QĐ-TTg** was signed **2026-06-30** by Deputy
PM **Hồ Quốc Dũng**, in force **2026-08-15**, under 🆕 **Nghị định 142/2026/NĐ-CP**.

🆕 **The education entries include `đánh giá tâm lý` — psychological assessment** — which p137's
English-language read did not record alongside uncontrolled-source self-study content, automated
grading and behaviour monitoring. 🔵 **This catches a product class a vendor would not self-file as
high-risk**: wellbeing screening, engagement scoring and at-risk prediction are none of them
"grading" and none of them "biometrics".

🔴 **The transition date remains contradictory in Vietnamese sources too** — **2027-09-01** for
health/education/finance with **2027-03-01** for other listed sectors in one, a general
**2027-03-01** in another whose visible scope list omits education. 🔵 **Plan against 2027-03-01**:
a client ready for March is ready for September, not the reverse. 🔴 **The gazette
(`congbao.chinhphu.vn`) does not resolve in this channel** — primary source, secondary transport,
third pass running.

**Pass 137, 2026-10-11.** p136's fifteen trends retained. 🔴 **`T13` is rewritten for the second
consecutive pass, and this time by source code rather than by a better query**: the mapping it
called absent is library code owned by a US university. 🟢 **`T14` extends from licence metadata to
CAPABILITY metadata** — four of four connectors in one fork family contradict themselves about their
own tool count. 🟢 **`T15` survives its own falsifier by a factor of ten** (50% against a 5%
threshold) and gains the clause that makes it usable. 🆕 **`T16` is added: the first binding
education-AI conformity regime in force is Vietnam's, not the EU's.** Each change states the
measurement and the condition that would overturn it.

### 🔴 p137 rewrites `T13`: the LTI→OAuth-subject mapping exists, and the residue is one standard version wide

| p136's clause | p137's measurement, in source |
|---|---|
| *"Nothing maps a verified LTI 1.3 launch onto a broker's subject and audience"* | 🔴 [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) (**LGPL-3.0**, Kansas State University, HEAD 2026-09-30) maps a verified launch onto a **per-user** OAuth grant: `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → `/login/oauth2/auth` for that user → Canvas **as** that user |
| *"the whole remaining bespoke surface of the sanctioned path"* | 🟡 **Narrower**: the mapping is anchored on **LTI 1.1** (OAuth 1.0a consumer signing) and returns a platform API token, **not** an RFC 8707-bound token for an MCP resource server |
| *"none of the six brokers terminates an LTI launch"* | 🟢 **Still true**, and now accompanied by its mirror image: a 9★ education-native row, [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (**MIT**), *is* an OAuth 2.1 authorization **and** resource server with RFC 9728 metadata and audience checks |
| *(unstated — assumed from READMEs)* | 🔴 **`ltijs` v7.0.7 confirms the gap in code**: its only outbound token is `client_credentials` with `{sub: platform.clientId, iss: platform.clientId, aud: platform.authorizationServer}`. **The tool is the subject by design**, and the launch user's `sub` is stored and never leaves |

🔵 **The trend statement that survives**: *the credential blocker was solved, the
identity-assertion blocker was solved twice in parts, and what remains is an adapter between two
standard versions.* 🔴 **Falsifier for the next pass**: if `ltijs` v7's `LaunchContext` cannot hand a
verified `sub` to `canvas-lms-mcp`'s authorization server without forking either library, the
adapter is bigger than two weeks and this clause is wrong (`ACTION CE`).

### 🟢 `T14` extended — from licence metadata to CAPABILITY metadata

`T14` says declared metadata is systematically wrong in the direction of institutional code. 🔴 **The
same defect now has a second, cheaper-to-measure form**: a connector's declared **tool count**.

| repo | About | README / manifest |
|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) **289★** | *up to 102 tools* | *up to 126 tools* |
| [`abr-Projects/canvas-mcp`](https://github.com/abr-Projects/canvas-mcp) (fork) | *80+ tools, 5 skills* | *101 tools, 8 skills* |
| [`lindsay-cheng/canvas-mcp`](https://github.com/lindsay-cheng/canvas-mcp) (fork) | *102 tools* | *103 tools* |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) **103★** | *Version 2.2 · 54 tools* | README **v2.3.0**, `package.json` **2.3.1** |

🔵 **Four of four, including the upstream.** A KB row that quotes a tool count inherits the drift, so
this KB now counts from source: **136** for `EduBase/MCP` (57 get / 41 post / 24 delete / 10 patch /
3 put), **36** for `brightspace-mcp-server`, all read-only. 🔴 **And the same class covers standards
names used as product names**: `canvas-lms-mcp`'s *"New Quizzes (LTI)"* is Canvas's feature name —
the code reads `is_quiz_lti_assignment` and implements no LTI, so a topic- or keyword-level LTI probe
false-positives on it.

### 🟢 `T15` survives its falsifier by a factor of ten, and gains the clause that makes it usable

🔴 **`ACTION BY`: 10 of the 20 largest rows (50%) carry a licence file whose holder is not the
repository's own.** The refutation threshold was 5%. **224 591** tree paths, **316** non-root
licence-shaped files, **242** real grants (`compose/code/p137-foreign-holder-tree`, 12 tests).

🔵 **The new clause comes from reading it against
[`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md), which measured the
root licence **family** as complete **92%** of the time:**

> 🟢 **A root licence cell predicts what you may DO. It does not predict whom you OWE.**
> Family: 92% root-complete. Ownership: 50% root-incomplete, in the largest rows.

🔴 **Two instances that change a decision rather than a caution**: `instructure/canvas-lms` is
AGPL-3.0 at the root and ships **MIT** LTI Advantage code held by a named individual four levels
down; `classroomio/classroomio` is AGPL-3.0 and vendors **ten MIT agent-skills packs** held by
outsiders. 🟡 **And 50% is a floor**: the instrument reads licence *files*, so a grant inside a
source header — the `pipwerks` case — is invisible to it (`ACTION CH`).

## 🆕 `T16` — The first binding education-AI conformity regime in force is Vietnam's, not the EU's *(new, p137)*

🔴 **Vietnam:** AI Law **No. 134/2025/QH15** in force **2026-03-01**; Decision **No.
33/2026/QD-TTg** (issued 2026-06-30) **effective 2026-08-15** lists **46 high-risk AI systems** over
six sectors, **three of them education** — generating self-study content from uncontrolled data
sources, **testing/grading/ranking learners**, and monitoring learner behaviour with biometric data.
Duties: conformity assessment (third-party or self-assessment per the decision's pathway),
registration in the **National AI Database**, human oversight, incident reporting.

🔴 **The EU moved the other way on the same obligation class.** The Digital Omnibus on AI —
**Regulation (EU) 2026/1744**, in force **2026-07-27** — defers **Annex III** high-risk duties, which
is where education sits, from **2026-08-02** to **2027-12-02** (Annex I embedded: **2028-08-02**).
🟢 **Article 50 transparency was not deferred and applied from 2026-08-02**, with a grace period to
**2026-12-02** for systems already on the market.

🔵 **Why this is a trend and not a news item.** For three passes this KB has sold the EU's clock as
*the* compliance driver and recorded APAC as *"mandates and no market"*. 🟢 **Both halves flip**: the
jurisdiction with live education-AI conformity duties is in APAC, and the EU's live duty is the
*transparency* one — narrower, cheaper, and already late. A single engagement therefore splits into
two differently-shaped pieces (`compose/patterns.md` → `P15` for the EU, `P16` for Vietnam).

🔴 **Falsifiers, stated:** `T16` fails if Vietnam's decree text (read in Vietnamese, `ACTION CG`)
grants education systems a transition that runs past **2027-12-02**, since the EU's deferred date
would then arrive first after all; and it weakens if another jurisdiction is found whose education-AI
conformity duties were already in force before **2026-08-15**. 🔴 **Both sources for the Vietnamese
dates are law-firm briefings, and they contradict each other on the transition**, which is recorded
as a conflict rather than resolved.

---

**Pass 135, 2026-10-11.** p134's trends retained; 🔴 **`T12` is qualified by the measurement that
finished its own register — the sanctioned layer is not uniformly mature, and the variable is the
standard's AGE** — **`T10`'s probe rule is generalised from a fact about one word into a rule about
institutions** (`ACTION BM`), and **`T13` and `T14` are added**. Each trend states its evidence and,
where it matters, what would falsify it.

**Pass 132, 2026-10-11.** p131's trends retained; 🔴 **T8 and T9 are substantially corrected — both
had declared an absence that this pass filled** — **T4 and T10 are qualified**, and **T11 is added**
(see `README.md` → Pass 132). Each trend is stated with the evidence that supports it and, where it
matters, what would falsify it.

## T1 — The governance gap is the market

Student and teacher adoption has outrun institutional policy by an order of magnitude: **88%** of
students worldwide (95% of UK undergraduates) use generative AI, **60%** of US K-12 teachers used it
in 2024-25, and **18%** of US teachers have a written policy telling them how. This is the defining
condition of education AI in 2026. It means the buyer's problem is not capability — the tools are
already in the building — but control, evidence and defensibility.

**Consequence for engagements:** lead with inventory, data-flow proof, human-in-the-loop gates and
audit logs. A tutoring demo does not address the thing keeping the client awake.

## T2 — Mandates with hard dates replaced guidance

2026 is the year education AI rules acquired deadlines:

- **Ohio:** every K-12 district must adopt a formal AI use policy **by 1 July 2026**.
- **South Korea:** AI Basic Act in force **22 January 2026**.
- **India:** AI and computational thinking mandatory **from Class 3, 2026-27 academic year**.
- **China:** AI compulsory from age six since September 2025; Cybersecurity Law AI amendments
  effective January 2026.
- **Vietnam:** Decision 33/2026/QD-TTg names education — including automated assessment and
  behavioural monitoring — as high-risk.
- **EU:** AI literacy duties in force since February 2025; emotion recognition in education
  **prohibited** since 2 February 2025.
- **US states:** 134 bills across 31 states in 2026; 30+ states with guidance.

**The trend is not "regulation is coming" — it is "obligations are already in force and capacity is
missing."**

## T3 — The EU's high-risk clock slipped to December 2027, and that is a sales window

Annex III education obligations (admissions, grading, proctoring) were postponed to **2 December
2027** via the Digital Omnibus on AI. 🟢 **p131 closes p130's open question: the Council HAS adopted.**
A final Council green light is reported for **29 June 2026**, and this KB's own append-only pages
have carried the instrument as **Regulation (EU) 2026/1744 of 8 July 2026** for several passes.
p130's *"Council adoption was still outstanding"* was a regression against this KB's own record,
and an independent channel now corroborates the adoption. **The deferral is law, not a political
agreement.** Annex I embedded systems follow at **2 August 2028**.

Meanwhile what binds *now* is unmoved: Article 4 AI-literacy duties and the emotion-recognition
prohibition (both since February 2025), and **Art. 50 transparency, live since 2 August 2026**.

**Read it as:** ~14 months to build conformity in by design rather than retrofit it, not 14 months
of nothing to do. 🔴 **The old falsifier ("if the Council fails to adopt") is spent.** The live
falsifier is narrower: a further omnibus reopening Annex III, or a national regulator applying the
pre-deferral dates anyway.

## T4 — Supply is extraordinarily concentrated, and one repo is the whole mid-market

`HKUDS/DeepTutor` (Apache-2.0) stands at **41 136 stars**. The next education-specific agent found
this pass is `GarethManning/education-agent-skills` at 847 (and its licence does not resolve to an
OSI identifier), then `satvik314/educhain` at 388 and `vishalsachdev/canvas-mcp` at 288. There is
**no middle of this market** — one large permissive agent and a long tail of sub-1k projects.

**Consequence:** a client wanting "the open-source tutoring stack" gets DeepTutor plus bespoke
integration. Budget for the integration, not the engine.

🟡 **Qualified by p132 in two ways.** First, there is now a **second** repo at that scale:
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0, 39 444★**) — so the shape is two large permissive projects, not one, and the second
one is an *offline composition layer* rather than an engine. Second, the "long tail of sub-1k
projects" is **much longer and much better placed than this KB knew**: **36** SIS/portal rows at
0–40 stars (21 from p132, **15 added by p133**), ~90% region-placed. 🔴 **Licence mix corrected by
p133: p132's "~80% MIT" was measured before the LATAM and ANZ probes ran** — the 12 LATAM rows are
**42% MIT**, and the tier's new top row, `BetterSEQTA-Plus`, is **MIT at 40★**, which also retires
the "nothing above 10 stars" ceiling. 🔵 **The concentration finding holds for *engines* and is
misleading about *connectors*** — the connector layer is not concentrated at all, it is atomised
across national platforms, which is a different procurement problem and a different opportunity.

**Correction to this KB's own record:** earlier passes recorded DeepTutor at "~22k★" and then
"~24k★", and `educhain` at "~9k★" then "~12k★". Verified today: DeepTutor **41 136**, educhain
**388**. The educhain figure was overstated by roughly 30×. Star counts in this KB predating pass
130 should not be trusted without re-verification.

## T5 — Connector effort has pooled on Canvas, and fork swarms inflate the apparent supply

Five-plus Canvas MCP servers exist; eight of the fifteen platforms in `verticals/solutions.md` have
**no** AI-on-top project at all.

🔴 **Correction to p130's version of this trend.** It said Moodle *"has no permissively licensed MCP
route"*. Moodle has **eight standalone MCP servers, five of them MIT** — the tier p130's queries
missed because it looked only for in-tree plugins. The concentration claim survives; the Moodle
exception does not. 🟡 **But note what the permissive tier looks like:** the largest MIT one
(`peancor/moodle-mcp-server`, 43★) has not been pushed since February 2026, and the most-starred
Moodle connector overall (`loyaniu/moodle-mcp`, 40★) carries **no licence at all**. The permissive
rows and the active rows are different rows.

Worse, the apparent supply is padded by **fork swarms**: at least five repositories carry a
byte-identical `canvas-mcp` description under different owners, and `tutor-mcp` appears under two.
A fork-excluding search resolves each to a single canonical upstream
(`vishalsachdev/canvas-mcp`, `ArnaudGuiovanna/tutor-mcp`); one fork still advertises an older
tool count as current. Counting repos overstates the field substantially.

## T6 — Licence risk is concentrated exactly where the traction is

The most-starred education agent-skills collection (847★) reads as **NOASSERTION**. A 103-star
Canvas MCP server has **no licence file at all**. The cleanest Moodle→MCP route is **unlicensed**.
Two platform licences (`openeducat_erp`, `OpenOLAT`) do not resolve to OSI identifiers.

Meanwhile the platforms are mostly **AGPL-3.0** (Open edX, Canvas, Frappe LMS, Tutor, LearnHouse,
ClassroomIO), which network-copyleft binds any client offering a hosted service. The permissive
shortlist is small and worth memorising: **Oppia (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT),
Academico (MIT), Richie (MIT), H5P (MIT), XBlock (Apache-2.0), codejail (Apache-2.0)**.

**Consequence:** licence review belongs at the start of an education engagement, not at hardening.
The highest-traction components are the riskiest ones.

## T7 — The measurement layer exists and cannot be shipped *(corrected by p131)*

🔴 **p130 stated this trend as "nobody measures learning" and called it the largest hole on the
shelf. That was false, and this KB's own pages refuted it.** Two real benchmarks exist:

- [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) — 43★, **ETH Zurich**,
  **EMNLP 2025 oral**, held in this KB **since pass 4**. Measures open-ended *pedagogical* capability
  (scaffolding, hint quality), not answer accuracy.
- [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) — 57★,
  **Khan Academy**, with its licence read in full by an earlier pass.

🔴 **The real constraint is the grant, and it is worse than a missing repo.** `mathtutorbench` has
**no licence field** and a README that names **two different licences in one file** (CC-BY-4.0 badge
vs CC-BY-SA-4.0 body); Khan's carries a **bespoke 2 690-byte "Evaluation Dataset License"**, not an
OSI one, and has been dormant since August 2024. **Both can be run and cited; neither can be shipped
inside a client deliverable without counsel.**

🟢 **The genuine gap, stated so it cannot regress again:** nothing open source measures **learning
outcomes** — durable gains in what a student knows. Both benchmarks measure *tutor behaviour*. The
OECD's 2026 Digital Education Outlook asks precisely for durable learning gains, and that standard
is still unmet.

**Still the most commercially valuable gap in the KB**, and now a cheaper build than p130 implied:
start from `mathtutorbench`'s task structure rather than a blank page, and anchor the quantitative
side on `OATutor` and `tutor-mcp`, which already expose Bayesian Knowledge Tracing mastery estimates
that an LLM's self-report cannot substitute for. See `compose/patterns.md` → P6.

## T8 — Offline and low-bandwidth stopped being an edge case

Kolibri (MIT, offline-first, content sync by LAN or USB) is the clearest instance of a trend driven
by where growth actually is: APAC at ~35.3% CAGR, India mandating AI from Class 3 across government
schools, LATAM adopting ahead of infrastructure, Google.org targeting 1.25M LATAM students by 2028.
Small local models make an offline tutor technically possible for the first time, and the data never
leaving the device resolves most of the privacy problem in T1 and T2 by construction.

~~**Nobody has built it:** no AI agent on top of Kolibri was found. MIT licence, offline design,
regulatory tailwind, no incumbent.~~

🔴 **CORRECTED BY p132 — somebody built it, at 39 444 stars.**
[`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
(**Apache-2.0**) is an offline-first knowledge and education server that orchestrates containerised
tools: **Kiwix** for the library, **Kolibri** for the education platform, **Ollama** for the AI
assistant. It is the **second-largest repository in this entire KB**, behind only DeepTutor. There
is also a macOS port ([`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos),
20★) and an Indian Class-10 offline LMS claiming Kolibri integration
([`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI), 2★).

🔵 **Why the probe missed it, which matters more than the miss.** p131's `kolibri stars:>2` query
was valid: 86 repos, 3 in the Learning Equality family, 0 with AI. **NOMAD composes Kolibri as a
Docker container and never names it in its description.** A dependency is not always visible in the
metadata of the thing that depends on it — so "no project builds on X" cannot be concluded from
searching for X's name.

🟢 **The trend is intact and stronger; only the opportunity changed shape.** Offline is real, the
drivers above are unchanged, and the engagement is now *"deploy and extend a permissive 39k-star
stack"* rather than *"build it"* — faster and far easier to defend in procurement.
🔴 **The surviving gaps are narrower and genuinely open: nothing builds AI *inside* Kolibri**
(NOMAD attaches from outside; the Learning Equality repos carry none), **and nothing offline
targets LATAM** — the one curriculum-specific offline project is Indian, in the region this KB
argues needs offline most. **What would falsify the trend:** NOMAD stalling, or local-model quality
on commodity hardware failing to reach tutoring grade.

## T9 — Administrative automation is the most-cited driver and the least-served

Intelligent tutoring, personalised learning, administrative automation, AI-driven assessment and
virtual assistants are the standard trend list; administration is where institutions report the
clearest return.

🔴 ~~**There is still no open-source *agent* for a student information system** — no enrolment,
records or timetabling agent. That half of the trend holds, and it is now the largest genuine hole
in this KB.~~ **REFUTED BY p132, one pass after being promoted to "the largest genuine hole".**
There are **21 rows** (`agents/top.md`), including a **NEP 2020 timetable optimiser** (MIT), a
**FERPA-logging student-records server** (Apache-2.0, org-owned), an **Okta/SCIM** identity demo,
and a **standalone 42-tool classroom-management server** (MIT) — plus national portal connectors for
Librus, EduPage, Pronote, IServ, Sisu, uSaint, VTOP, QLDT, VSB and NYCU.

🔵 **The cause of the false absence was vocabulary, not supply.** Every probe asked for *"student
information system"*, *"school management"*, *"SIS"*. The builders name repos after the platform
they connect to. The query that worked was `timetable timetabling MCP` — **timetable access is the
one capability all of them implement.**

🟢 **The trend's core claim survives in a sharper form, and it is better for an engagement.**
Administration is still underserved, but not for want of software: **(a) nothing in the tier exceeds
10 stars**, so there is no production-grade row; **(b) the credential model is unsanctioned portal
scraping with a stored pupil password**, which no client security team will accept; and
**(c) all 21 connect to proprietary or institution-hosted portals — the open-source systems of
record have exactly zero agent coverage.** 🔴 **That last point is the useful inversion: connector
effort has gone to the platforms a studio cannot fork and avoided the ones it can.**

🔴 **The other half was wrong.** p130 said the only candidates are `openeducat_erp` *"(licence
unclear)"* and `academico`. The **platform** tier is at least six systems deep —
`frappe/education` (662★), `openeducat_erp` (**LGPL-3.0**, payload-read, not "unclear"),
`academico` (MIT, 404★), RosarioSIS (GPL-2.0), Gibbon (GPL-3.0), openSIS, Fedena — all restored in
`repos/foundations.md`. 🟢 **The constraint is licensing, not supply: exactly one of them
(`academico`, MIT) can become a closed derivative.** "No software exists" and "the software is
copyleft" lead to opposite engagement plans.

## T10 — The demand-side channel is a dating channel, not a fact channel *(corrected by p132)*

🔴 **Fourth consecutive pass in which the prescribed regional battery returned nothing this KB did
not already hold.** All four regional queries plus the four global ones were run this pass. **Zero
new tokens in all four regions.** Everything they returned was already on a live page here: the
Digital Omnibus deferral (2027-12-02 / 2028-08-02), Ohio's 1 July 2026 district duty, H.R. 8747,
California AB 1159, Idaho SB 1227, Vietnam's high-risk education listing, Korea's AI Basic Act
(22 January 2026), UNESCO IESALC's **87% adoption / 26% with a strategy**, the Digital Education
Council's LATAM faculty figures, the UNESCO LAC Observatory (14 April 2026), the UK's £4M
lesson-planning programme, the OECD *2026 Digital Education Outlook*, **134 bills across 31 US
states**, and the EMEA market at ~$2.64B.

🟢 **One thing the channel did add, and it is worth the battery on its own:** independent
corroboration that the **Council adopted** the Digital Omnibus (29 June 2026), which closes a
question p130 left open and repairs `intel/policy-matrix.tsv`. A saturated channel is not a useless
channel — it is a *confirmation* channel, and should be budgeted as one.

🟢 **The supply side moved, as it has every pass.** p131's new addresses all came from
layer-specific repo queries aimed at this KB's own declared gaps, not from the generic battery:
three MIT proctoring projects, and the restoration of two tiers p130 had declared absent.

**Consequence for how these passes are run:** spend the regional battery on *confirmation and
dating*, and spend the pass's real effort on gap-directed supply queries and on **auditing this
KB's own claims against its own pages.** Pass 131 found more by grepping this repository than by
searching the web.

### 🟢 p132: the streak broke in 4 of 4 regions — and the reason refines the trend

p131 counted a **fourth consecutive pass** of zero new tokens and recommended budgeting the battery
as a confirmation channel. Run again unchanged, it produced **new tokens in all four regions**.
🔵 **But not one of them is a new fact.** Every one is a **date, a denominator or a delivery
structure**:

| region | the new token | its type |
|---|---|---|
| LATAM | IESALC fieldwork ran **August–October 2025** | 🟢 **a date that re-ages a held figure** — the *87% / 26%* numbers describe late 2025, not now |
| LATAM | **200** institutions, **19** countries; **ILIA 2025 (CEPAL)** carries country-level regulation detail | a denominator and a named instrument |
| EMEA | UK **AI Adoption Summit, £200m+**; delivered by **Cisco/IBM/BT/Rolls-Royce**, curriculum by **Skills England**, *few education providers involved* | 🟢 **a delivery structure** |
| North America | **10%** of institutions have AI guidelines; **71%** of teachers untrained; **CMU + Gates $55M** on *gateway courses* | denominators and a capital target |
| APAC | **Australia/New Zealand** tightening governance; OpenAI appoints an ANZ policy lead | a jurisdiction this KB had never covered |

🔴 **So the trend as p131 stated it was half right and the half it got wrong is the operative
half.** The battery is not saturated — it is **saturated for facts and productive for provenance**.
Four passes called it dead because they only ever asked *"what is new?"*. Asking **"when was this
measured, who was counted, and who is being paid to deliver it?"** of the *same* results is still
productive, and the answers change how a figure may be quoted to a client.

🔴 **One stale claim is still circulating and a client may arrive holding it:** that the EU AI Act
puts education AI in high-risk *"with full effect in August 2026"*. The schools-facing Annex III
date is **2027-12-02** (T3). This KB has flagged it for three consecutive passes.

### 🟢 p135 generalises the probe rule: it is about institutions, not about words

p133 found that *"EMEA"* returns enterprise IT because it is **a vendor sales-region word no ministry
uses** (`P133-E`), and p134's `ACTION BK` confirmed it by re-probing EMEA country by country.
`ACTION BM` tested the other two regions this pass:

| bare probe | result |
|---|---|
| **"EMEA"** | 🔴 **Fails.** Enterprise IT outlooks, a 2023 enterprise-AI trust study, enterprise compliance commentary. One education source, and its event sat in **October 2024** |
| **"APAC"** | 🔴 **Fails identically.** Enterprise tech priorities, sovereign-cloud analysis, and vendor press releases. The run recorded finding **no** education-specific regulation, ministry rule or edtech market data |
| **"LATAM"** | 🟢 **Succeeds.** UNESCO **IESALC** (200 institutions, 19 countries, 87% using AI, 26% with a framework), the **Digital Education Council** LATAM survey 2026 (30 000+ responses), the **IDB** readiness index, and country-level regulatory posture for Chile, Brazil, Colombia and Mexico |
| **"North America"** | 🟡 **Partly.** Market-research geography segments dominate, but real findings surface (state-legislature activity, a $169M government commitment, a $55M CMU/Gates courseware investment) |

🔴 **So `P134-H` is not a fact about the word "EMEA", and stating it that way was too narrow.**
🟢 **The rule:** *a bare regional probe returns education material exactly when a region-scoped
education body publishes under that label.* Latin America has two — **UNESCO IESALC**, the
institute for higher education in Latin America and the Caribbean, and the **IDB**. "EMEA" and
"APAC" have no counterpart; no ministry, university network or multilateral addresses research to
them. "North America" sits in between because market-research firms use it as a reporting segment.

🔵 **Why this is worth more than the three results.** It is **decidable before searching.** Ask
whether a region-scoped education institution exists; if not, probe by country from the start.
🟢 **That is a standing method rule, and it predicted this pass's APAC result correctly** — the
country probe returned India's Class-3 mandate, Singapore's literacy framework and South Korea's
2026 work plan, none of which the regional probe could see.

### 🔴 p136 adds the missing clause: the INSTRUMENT'S LANGUAGE is part of the probe

p135's rule — *a bare regional probe works when a region-scoped education body publishes under that
label* — is right and **incomplete**, and `ACTION BT` found the hole. 🔴 **Japan has a body that
publishes prolifically, a dated national instrument, and a ministerial circular number — and p135
recorded Japan as MEASURED ABSENT**, because the probe ran in English while the instrument is
Japanese.

| probe form | result |
|---|---|
| English, country-level (`"AI education Japan policy"` family, p135's APAC sweep) | 🔴 **Nothing.** Japan was the one country in a five-country sweep that returned no instrument |
| 🟢 Japanese, by ministry (`文部科学省 生成AI 教育 ガイドライン`) | 🟢 **First attempt**: MEXT's own PDFs, the guideline Ver.2.0 of **2024-12-26**, circular **6文科初第1895号**, and the 2026-06-30 committee papers opening the Ver.2.1 revision |

🟢 **So the method rule now has three clauses, and all three are decidable before searching:**

1. **Does a region-scoped education body publish under that label?** If not, probe by country
   (p133/p134/p135).
2. 🆕 **In what language does that country's education ministry publish?** Probe in it. The
   ministry's own name is the highest-yield token — `文部科学省`, not "Japan".
3. **Name the instrument class, not the topic.** "Guideline", "circular", "curriculum" and their
   local words; a topic word returns commentary, an instrument word returns the instrument.

🔴 **The uncomfortable corollary, written down rather than left implicit.** This KB's **China**,
**Korea** and **Brazil** policy cells were all built from English-language sources about
non-English instruments. `ACTION BT` proved that shape can miss an entire national policy, so those
three cells are provisional until re-probed in 中文, 한국어 and português.

## T11 — The connector layer is being built bottom-up by students, not by vendors *(new, p132)*

🟢 **The strongest structural finding of this pass, and it reframes where supply comes from.** The
21 SIS/student-portal agents found this pass share a profile so consistent it is clearly a
phenomenon rather than a coincidence:

| property | value | what it implies |
|---|---|---|
| **author** | ~~one person, almost always a student~~ → 🔴 **not in LATAM or Australia** | p133: **4 rows serve a teacher**, one is **org-owned with a product homepage** (`expeditto`), and `BetterSEQTA` is a two-product org with 25 forks |
| **licence** | ~~**~80% MIT**~~ → 🔴 **tier-wide this is wrong; see p133** | 🟡 measured on 21 EMEA/APAC/NA rows. The **12 LATAM rows** p133 added are **42% MIT** (3 unlicensed, 2 GPL-3.0, 1 AGPL-3.0), and the one row p132 left unread reads **AGPL-3.0** |
| **stars** | **0–10**, none higher | no production-grade row anywhere in the tier |
| **created** | mostly within the last 6 months; three within 10 days of this pass | 🟢 the tier is *forming now* |
| **region** | **~90% placed** on hard evidence (named institution, national platform, country-coded host) | the best regional evidence in this KB |
| **target** | **proprietary** national platforms and university portals | 🔴 zero coverage of open-source systems of record |
| **auth** | the author's own portal password; unofficial; 2FA unsupported | 🔴 undeployable as published |

🔵 **Why this is happening, and why it will continue.** MCP made it a weekend's work to wrap a
portal an author already logs into daily, and the itch — *"when is my next class, what is my
attendance, am I on track to graduate"* — is universal. Nothing about that requires a vendor,
a budget, or permission.

**Consequences for a studio, in order of usefulness:**

1. 🟢 **The expensive part of a national-platform integration is already published under MIT.**
   Mapping Librus's or Pronote's undocumented surface is weeks of work; it is done and readable.
   **Keep the surface map, discard the auth layer, rebuild it sanctioned.**
2. 🟢 **These repos are a demand signal with a region attached** — and the only such signal this KB
   has. Two independent EduPage implementations is a better indicator of Slovak demand than any
   market report on this page.
3. 🔴 **None of it is adoptable.** A 1-star repo with a stored pupil password is a reference
   document, not a dependency. Say so to a client before they find it themselves.
4. ~~🔵 **Where it is NOT happening is the finding for LATAM:** zero of the 21 are LATAM-origin…~~
   🔴 **REFUTED BY p133, and this was a claim about a query.** Probing `sigaa`, `suap` and
   `siu-guarani` returns **12 LATAM rows**. The bottom-up wave had reached LATAM; the probe had not.
   🟢 **And it arrived in a different shape: LATAM's wave is partly *staff-side*** — `expeditto`
   (AGPL-3.0, org-owned, drafts a lecturer's RIT workload report), `auto-sigaa` and
   `Auto_Grade_Guarani` (both move grades into the national SIS for a teacher). See `T9`.
5. 🔴 **The structural risk of the whole tier now has a measured instance, not just a worry.**
   `st22209/Parent-Portal` (MIT, New Zealand, **KAMAR**) is **archived**, and its README gives the
   cause: *"[DEPRECATED AFTER KAMAR API CHANGE]"*. **An unsanctioned connector does not degrade when
   the vendor changes an endpoint — it ends.** That is the argument for pattern `P8` as an observed
   outcome.

**What would falsify this:** a vendor (Librus, EduPage, Instructure, Moodle HQ) shipping an official
agent or MCP surface, which would make the student connectors redundant overnight — and which is
exactly the engagement to propose to such a vendor.

## T12 — The sanctioned-integration layer is mature, permissive and agent-less *(new, p134)*

🔴 **This is the trend that reframes `T5`, `T6` and `T11` at once, and it took four passes of
connector-counting to see.** `T11` says the connector layer is being built bottom-up by students
rather than vendors, and `agents/top.md` says the resulting credential model makes nearly all of it
undeployable. 🟢 **Both are true of the *portal* layer and false of the layer beside it.**

**The interoperability standards layer — LTI 1.3 Advantage, OneRoster 1.2, Ed-Fi, xAPI — is built,
permissive, and owned by exactly the institutions this KB keeps saying are absent:**

| the claim this KB has been making | what the standards layer shows |
|---|---|
| *"supply is extraordinarily concentrated and student-built"* (`T4`, `T11`) | 🟢 **`Cvmcosta/ltijs` — Apache-2.0, 373★, pushed 2026-10-06.** Larger and more active than the LTI row this KB already had |
| *"licence risk is concentrated where the traction is"* (`T6`) | 🔴 **Inverted here.** The platforms are AGPL/GPL/LGPL; **the standards layer is Apache-2.0, MIT and 0BSD** — the most permissive set of rows in this entire KB |
| *"no institutional or vendor owners"* | 🟢 **Ed-Fi Alliance, Google, the US DoD's ADL Initiative, the Minnesota Department of Education, France Université Numérique, UNIwise ApS, Blackboard, Open Assessment Technologies** |
| *"the credential model is a tier-wide blocker"* | 🟢 **A tool launched over LTI holds no user password at all** — it runs on a client ID the institution issues and can revoke |

🔴 **And here is the trend, in one sentence: the standards are finished and the agents have not
arrived.** The bridge from an AI agent to any sanctioned learning standard is **one repository** —
[`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, 15★, last push
2025-08-29) — and **the only Ed-Fi MCP server in existence is an empty repository**
(`cdweaver1992/edfi-mcp-server`: `size: 0`, HTTP 404 on 15 probes across 3 branch refs, created and pushed in
the same second).

🟢 **Why this is a trend and not a single finding.** The direction of travel across every other
trend on this page points at it. `T9` (administrative automation is the most-cited driver and least
served) needs a system of record, and OneRoster/Ed-Fi *is* the sanctioned route into one. `T3` and
the 2027 compliance clocks reward auditable access over scraped access. The market's
fastest-growing segment — **assessment and feedback agents at 44.36% CAGR** — is precisely what
**LTI AGS grade passback** was designed to carry. 🔵 **Four independent pressures all terminate at
the same missing component, which is usually what a build opportunity looks like before anyone
builds it.**

🟡 **What would falsify this trend.** If an MCP-over-LTI/OneRoster server appears with real
traction in the next few passes, this stops being an opportunity and becomes a dependency — and
**that is the thing to watch for, because it would also be the fastest-moving row in this KB.**
🔴 **Equally, if the standards layer turns out to be shallower than its metadata suggests — the
Python LTI library is already ~2 years dormant and the xAPI bridge ~14 months — then "mature" is
too strong, and this pass will have over-read activity from stars and a single `pushed_at`.** No
repository in this tier has been code-audited by this KB.

🔵 **The regional asymmetry is part of the trend, not an aside.** LTI, OneRoster and Ed-Fi are
**North-American and European procurement standards**. The LATAM national systems (SIGAA, SUAP,
SIU-Guaraní, SAES, Q-Acadêmico) publish no equivalent, and APAC's only standards-tier rows are an
AGPL-3.0 project and a spec translation. 🔴 **So the sanctioned path is available where the
standards are, and the scraping is a symptom of their absence — not of a different builder
culture.** That is a materially different explanation from `T11`'s, and it is testable: it predicts
that LATAM supply stays unsanctioned until a national system publishes an API, regardless of who
builds it.

### 🔴 p135 qualifies `T12`: maturity tracks the standard's AGE, not its design

p134 stated `T12` as *"the sanctioned-integration layer is mature, permissive and agent-less."*
🟢 **The second and third clauses hold.** 🔴 **The first is true only on average, and the average
hides the thing a studio needs to know.** Finishing the register (`ACTION BN`) measured all six
remaining standards:

| standard | first published | largest repo | ★ | supply verdict |
|---|---|---|---|---|
| **SCORM** | **1999** | `adaptlearning/adapt_framework` | **630** | 🟢 **Deep.** Four repos above 350★; a permissive modern runtime; authoring tools |
| **LTI** | 2010 (1.3 in 2019) | `Cvmcosta/ltijs` | **373** | 🟢 **Strong and current** (pushed 2026-10-06) |
| **QTI** | 2000s (QTI 3 in 2022) | `amp-up-io/qti3-item-player` | **30** | 🟡 **Thin but real** — 15 repos, mostly MIT, several vendor-owned |
| **Open Badges** | 2011 (3.0 in 2022) | `1EdTech/digital-credentials-public-validator` | **17** | 🟡 **Thin, converging on W3C Verifiable Credentials** |
| **Comprehensive Learner Record** | 2010s | *the same validator* | **17** | 🔴 **One real row in existence** |
| **Caliper Analytics** | 2015 | `lsloan/udp-notebooks` | 🔴 **0** | 🔴 **No usable supply at all.** One repo, unlicensed, untouched since 2023 |

🔵 **The pattern is monotonic in age and has nothing to do with the standards' quality.** SCORM is
technically the crudest of the six and has the most code; Caliper is the most modern event model and
has none. 🟢 **The mechanism is deployment, not merit: SCORM and LTI are what institutions have
*bought* for twenty years, so there is installed base to write against.** Caliper and CLR are
procured rarely, so nobody has written a client.

🔴 **What this changes in a pitch.** *"We build on the sanctioned standards"* is credible for content
and launch (SCORM, LTI), **defensible** for assessment and credentials (QTI, Open Badges), and
🔴 **not currently true for analytics** (Caliper). A proposal that promises standards-based learning
analytics is promising a standard with **no open-source client**, which is a build the client should
be told about rather than a dependency.

🔵 **Falsifier.** If a Caliper or CLR client library appears above ~50★ with a permissive licence,
this reframing weakens and `T12`'s original wording is closer to right.

## 🔴 `T13` — The credential blocker was solved and replaced by an identity-assertion blocker *(new, p135)*

**This is the most consequential thing p135 found, and it only became visible by reading source.**

For four passes this KB has said the portal-connector tier is undeployable because every row holds a
student's password, and that the sanctioned path fixes it. 🟢 **The second half is confirmed:** of
the three bridges read this pass, **`ltijs` holds no user credential at all**, and the two MCP
servers hold an institution-issued *service* credential, never a student's password.

🔴 **But the sanctioned standard carries a cryptographically verified identity, and both agent
bridges to it discard that verification:**

| bridge | how the user's identity is established |
|---|---|
| `Cvmcosta/ltijs` | 🟢 **A platform-signed JWT, signature verified** against the platform's keys, with nonce tracking |
| `DavidLMS/learnmcp-xapi` | 🔴 **An environment variable** (`ACTOR_UUID`). 🔴 And its own docstrings claim *"Actor UUID from JWT"* while **the project has no JWT dependency at all** |
| `nitsuah/bb-mcp` | 🔴 **The caller's own assertion** (`caller_identity`), documented as *"trusted at face value"*. `role: "admin"` bypasses the course-entitlement gate; the app token is **org-wide** |

🔵 **Why this is a trend and not three bugs.** It is structural. MCP has no end-user identity model —
`bb-mcp`'s source says so in its first paragraph — so **every MCP server that fronts an institutional
system of record must either invent an identity model or accept one on trust, and the shipped
examples accept it on trust.** As agent-mediated access spreads from reading a portal to writing a
system of record, that choice stops being acceptable: a grade write attributed to an unverified
subject is an audit finding.

🟢 **The commercial consequence, and it is a component rather than a caveat.** The missing piece is
an **identity broker**: something that terminates a verified identity (an LTI launch, OIDC, or the
institution's IdP) and only then calls the MCP server with a subject it has itself established.
🔴 **No repository in this KB does this, in any region.** That is the clearest unbuilt component on
the shelf, it sits between two mature layers, and it is required by every engagement on the
sanctioned path. See `compose/patterns.md` → **P13**.

🔵 **Falsifier.** If an MCP server appears that verifies an LTI or OIDC assertion itself before
acting — rather than accepting `caller_identity` — this trend has been answered by the ecosystem and
becomes a build-versus-buy question instead of a gap.

### 🔴 p136: THE FALSIFIER FIRED, and `T13` is rewritten rather than restated

`ACTION BS` queried the **professional** register — `mcp oauth resource server`,
`mcp authorization server`, `token exchange rfc 8693` — because an authorization component is built
by people who do not say "education". 🔴 **Six repositories do exactly what the falsifier
describes**, and the best is Apache-2.0:
[`giantswarm/mcp-oauth`](https://github.com/giantswarm/mcp-oauth) verifies the upstream OIDC
`id_token` against the provider's **JWKS**, binds and checks the nonce, **refuses to issue when the
provider returns no subject claim** (*"provider did not supply a subject claim"*, in its own error
path), and implements the MCP authorization spec of **2025-11-25** — RFC 9728 protected-resource
metadata, RFC 8707 resource binding, RFC 9068 JWT access tokens with published JWKS, PKCE, DPoP and
token exchange, with **56 test files** under `server/`.
[`atrawog/mcp-oauth-gateway`](https://github.com/atrawog/mcp-oauth-gateway) (Apache-2.0, 60★) puts
the same thing in front of **any** MCP server *"without code modification"*. Register and licences:
`agents/top.md`.

🟢 **So the trend's mechanism stands and its conclusion inverts.** MCP still has no end-user
identity model — that is why these six exist. 🔴 **What was wrong was the sentence "no repository
does this, in any region"**: it was true of *this KB's rows*, which is the weak kind of absence
claim, and p135 said so when it registered `ACTION BS` against its own finding.

🟡 **What survives, and it is now sharp enough to quote in a proposal.** None of the six terminates
an **LTI 1.3 launch**. The missing piece is no longer a component but an **adapter**: `ltijs`
already verifies the launch correctly, and nothing maps that verified launch — its `deployment_id`,
AGS scopes and roster context — onto a broker's subject and audience. 🔵 **Measured, not assumed:**
`topic:lti` + `topic:mcp` across all of GitHub returns **two** repositories, and **neither
implements LTI**.

🔵 **New falsifier for the rewritten trend.** If a repository appears that terminates an **LTI 1.3
launch** and then issues a broker token bound to that subject, `T13` closes entirely and `P13`
becomes a procurement decision with no bespoke code at all.

## 🟡 `T14` — Licence metadata is systematically wrong in the direction of institutional code *(new, p135)*

🔴 **Measured, twice, with a reason.** `P134-F` found that GitHub's `NOASSERTION` is *"biased toward
unusual, not toward fine."* p135 measured why, by hash-matching 26 licence payloads against
canonical SPDX texts (`compose/code/p135-licence-sha-identity`):

- 🔴 **A licence payload never matches its canonical text naively.** Real `LICENSE` files wrap at ~72
  columns; SPDX wraps at ~105. **Zero of 26 payloads were whitespace variants** — refuting the
  premise `ACTION BP` was written on.
- 🔴 **Matchers are defeated by punctuation.** SPDX's canonical GPL-3.0 uses curly quotes; the
  `COPYING` shipped in real repositories uses ASCII. That alone accounted for five payloads.
- 🔴 **And by the licence steward editing its own text.** Two such edits are known for GNU: the
  `http`→`https` change, and the FSF moving `why-not-lgpl.html` from `/licenses/` to `/philosophy/`.
- 🔴 **The bias has a cause: appended institutional attribution.** `OpenOLAT` is Apache-2.0 to the
  character and then carries two attribution statements for the University of Zurich's original OLAT
  base and frentix GmbH. `Citolab/qti-convert` fills GNU's appendix with its real holder —
  **Stichting Cito Instituut voor Toetsontwikkeling** — which is correct practice and makes the text
  non-canonical. 🟢 **Well-governed, institution-derived projects are the most likely to append
  attribution, so they are the most likely to be mislabelled.**

🔴 **The practical edge, because this is a procurement risk and not a curiosity.** In this corpus a
badge would have mislabelled an LMS a studio can use (`OpenOLAT`, permissive) and said nothing about
two it cannot: `pipwerks/scorm-api-wrapper` (**391★, 130 forks, no licence file at all**) and
`cybercussion/SCOBot` (**164★, and the licence file is the CC-BY-SA-4.0 human-readable deed, not the
legal code** — a ShareAlike content licence on software). 🟢 **Rule: on anything a client will ship,
read the payload and hash it. A badge is a lead.**

### 🔴 p136 extends `T14` from licences to DECLARED METADATA, and corrects its own example

🔴 **The `pipwerks` example above is wrong in the direction this trend warns about.** "No licence
file at all" is a statement about **filenames**; the repository declares an MIT-style grant in
`package.json` and in its source header. 🔵 **A trend about metadata being unreliable published an
unreliable metadata reading** — which is the most useful way to learn that *absence of a file* and
*absence of a grant* are different measurements. Corrected in full on `repos/foundations.md` and
`agents/top.md`.

🟢 **And the same defect exists one field over, in topics.** `topic:lti` + `topic:mcp` across all of
GitHub is **two** repositories:

| repo | what the topic claims | what the source does |
|---|---|---|
| [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | `lti` | 🔴 Logs in with `ICTEXAM_EMAIL` + `ICTEXAM_PASSWORD` and rides the web app's session cookie + CSRF. LTI 1.3 belongs to a **separate Moodle activity module** |
| [`tkawen/developer-platform`](https://github.com/tkawen/developer-platform) | `lti`, `scorm`, `xapi` | 🔴 None implemented. In the SDK, `scorm` and `xapi` are **lesson-type enum values** |

🔵 **Why topics behave like licence badges.** Both are **author-declared strings with no verifier**,
and both are read by tooling as facts. 🟢 **Rule, generalised: every author-declared field — licence
badge, topic, description, docstring (p135's `learnmcp-xapi` *"Actor UUID from JWT"*) — is a claim.
Source and payload are measurements. This KB's auth and standards cells must say which they are**,
and after two source reads that each overturned a published cell, the base rate for the connector
tier is **2 for 2**.

## 🔴 `T15` — A licence verdict belongs to a LINEAGE, not to a slug *(new, p136)*

Three of this pass's findings are the same finding seen from three sides, and together they break an
assumption every page of this KB rests on: **that a repository URL identifies the thing whose
licence you read.**

| what was measured | why the slug is the wrong key |
|---|---|
| 🔴 **A grant declared outside the LICENSE file.** `pipwerks/scorm-api-wrapper`: `package.json` + source header, body at an off-repository URL (`ACTION BR`) | The licence is in the **artefact**, not at the path a filename probe looks at |
| 🔴 **A copy that DROPPED the grant.** [`0awei0/kt`](https://github.com/0awei0/kt) re-uploads [`hcnoh/knowledge-tracing-collection-pytorch`](https://github.com/hcnoh/knowledge-tracing-collection-pytorch) in **one commit**, README byte-identical, **upstream's MIT `LICENSE` absent** | The row reads unlicensed; **the code is MIT**. The grant lives with the **upstream**, not with this slug |
| 🔴 **Eleven slug pairs that are ONE repository.** Identical ref sets after a rename or transfer — `jdolny`/`theopenem` `OneRoster.NET`, `KI-Campus/LRS`/`openHPI/openLRS` (`ACTION BU`) | Two rows, one licence, and this KB has already **reasoned about which owner to pin** |
| 🔴 **A grant that travels INSIDE a vendored file.** `numbas/Numbas` is Apache-2.0 at the root and carries `pipwerks`' MIT-style header four levels down, at a version **four years** behind upstream | A root licence is not the licence of the tree |

🔵 **Two earlier passes each found one face of this, and neither generalised it.**
`p742-grant-body-vs-reference` (p58) fixed the licence **file** that points elsewhere while carrying
the grant; `p969-root-only-licence-reach` (p93) found that a root probe cannot see a **per-directory**
licence. 🟢 **`T15` is the third instance and the one that names the common cause**: the grant's
location is not a property of the slug, and neither is the code's provenance.

🔵 **Why it is a trend rather than four incidents.** The sector's code moves by **copying**, not by
dependency resolution: `SCORM_API_wrapper.js` appears in **293 files** on GitHub, the ENEM dataset
API exists as one project and **three history-rewritten copies**, and this KB's own corpus holds
**71** byte-identical README clusters. 🟢 **In a copy-propagated ecosystem, provenance is the
licence question.** Where a dependency manifest would carry a version and a licence, a vendored file
carries a header and a copy carries nothing at all.

🟢 **The operational rule.** Resolve the slug to a **repository** (ref-set identity), then to a
**lineage** (shared commits / root tree), then read the grant **wherever the artefact declares it**
— file, manifest, header or reference — and record **which** of those it was. Instrument with six
verdicts and 10 tests: `compose/code/p136-lineage-verdict/`; the grant-location classes are on
`agents/top.md`.

🔵 **Falsifier.** If a corpus-wide tree-level probe finds that vendored third-party code is rare —
say under 5% of rows carrying a foreign licence header — then slug-level licence verdicts are good
enough and this trend is an artefact of four unlucky examples.

## Watch list for the next pass

**Resolved this pass:**

- ~~Whether a **student-information-system agent** appears — now the largest genuine hole (T9).~~
  🟢 **RESOLVED: 21 exist** (T9, T11). Watch instead for the *first one to exceed 10 stars*, and
  for any connector that authenticates through institutional SSO rather than a pupil password.
- ~~Whether any **Kolibri-based AI project** appears (T8).~~ 🟢 **RESOLVED: `project-nomad`,
  Apache-2.0, 39 444★**, orchestrating Kolibri + Kiwix + Ollama (T8).
- ~~**Africa and the Middle East:** no regional evidence for a second pass.~~ 🟡 **PARTLY
  RESOLVED:** one 63★ Egyptian-targeted row, unlicensed by declaration. Still no African or Gulf
  market sizing, no national instrument, no Sub-Saharan row.

**Carried forward, unchanged this pass:**

- Whether `mathtutorbench` **resolves its own licence** (T7). Re-checked: still no `LICENSE`, badge
  **CC-BY-4.0** vs body **CC-BY-SA-4.0**. Still the single highest-leverage upstream change
  available to this KB.
- ~~Whether `instructure/canvas-lms` resumes activity; `pushed_at` **2026-04-30**…~~ 🔴 **RETIRED
  BY p133 AS A MIS-MEASUREMENT.** `canvas-lms` declares the topic **`gerrit-mirror`**, and
  `instructure/analytics` shares its `pushed_at` **one second later** (14:52:10 / 14:52:11) — two
  repos cannot be hand-pushed a second apart. **This is a stopped mirror export, not four passes of
  developer silence.** 🟡 **Watch the right thing instead: whether the GitHub mirror resumes at all**
  — because while it is frozen, GitHub is not an activity signal for Canvas and anyone diffing the
  mirror to track upstream is reading a five-month-old tree. See `repos/foundations.md`.
- 🔴 **New standing rule from that correction: never read `pushed_at` as activity without checking
  for a mirror.** Flag a recency reading as unreliable when *"mirror"* appears in topics, when two
  repos in one org share `pushed_at` to the second, or when the README names an upstream elsewhere
  (Gerrit, GitLab, SVN). This KB's `git-recency-channel` and `p109-freshness` lanes currently
  mis-rank every mirror in the direction of looking abandoned; `gerrit` appeared **zero** times
  across 1 733 addresses before this pass.
- Whether **Open edX MCP** moves past experimental; `blend-ed/openedx-mcp` still **2 stars**.
- Whether any **proctoring project acquires an institutional owner** — tier still permissive and
  capped at 18★.
- Whether a national regulator applies the **pre-deferral AI Act dates**, or a further omnibus
  reopens Annex III.

**New for the next pass:**

- ~~🔴 **Probe ANZ directly.**~~ 🟢 **DONE p133 (`ACTION BF`) — and ANZ is not a blank.**
  `BetterSEQTA/BetterSEQTA-Plus` (**MIT, 40★**, org-owned, 25 forks, Chrome Web Store, pushed
  2026-10-06) and `BetterSEQTA/DesQTA` (**MIT, 16★**) over **SEQTA**, Australia. New Zealand:
  one MIT **KAMAR** row, archived. 🟡 **Watch next: whether `BetterSEQTA` adds an AI/MCP surface** —
  it is the only product-shaped org in the portal tier and has not yet shipped an agent.
- ~~🔴 **Probe LATAM with platform proper nouns, not category terms.**~~ 🟢 **DONE p133
  (`ACTION BE`) — REFUTED: 12 LATAM rows.** `sigaa` (5), `suap` (3), `siu-guarani` (4). 🔴 **Probes
  that returned nothing are recorded with their probe in `intel/market.md` → LATAM**: SIAGIE (Peru)
  and Q-Acadêmico (Brazil) have real installed bases and **no agent layer at all** — the two
  cleanest unclaimed LATAM slots this KB can name. **Chile's `ucampus` probe collided with a Chinese
  homograph and the qualified re-probe returned 0.** 🟡 **Not reached: `simat` (Colombia), `saes`
  (Mexico)** — carried as `ACTION BJ`.
- 🟡 Read **ILIA 2025 (CEPAL)** directly for LATAM country-level regulation, instead of re-running
  regional news queries that return commentary.
- ~~🟡 Licence-measure the three rows left `UNREAD`…~~ 🟢 **DONE p133, all three read:**
  `edwyj/ddl-killer` = 🔴 **AGPL-3.0** (holder is the FSF only — a `DOCUMENT-TEXT` case),
  `karissafuller/project-nomad-macos` = 🟢 **MIT** (*"Copyright (c) 2026 Karissa Fuller"*),
  `Tushar-cy/Offline-AI` = 🔴 **no payload at `/main/` or `/master/`** → measured-absent.
  🔴 **Instrument note for the next pass: the GitHub contents API is scope-blocked in this session**
  (it returns *"repository is not configured for this session"*, which is an authorisation refusal,
  **not** a 404 and **not** evidence about the repo). **The working lane is
  `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE`.**
- 🔵 Check whether `Tushar-cy/Offline-AI` and `Tushar-cy/Ai-edge-learning-hub` are a rename pair,
  and retire the dead one from this KB before it is ever counted twice.

### 🆕 Added to the watch list by p134

- 🟢 **An MCP server over LTI AGS, OneRoster or Ed-Fi gaining traction.** Today the whole category is
  one 15-star repo and one empty one. This is the highest-signal thing to re-measure next pass.
- 🔴 **`cdweaver1992/edfi-mcp-server` — watch for it to acquire code.** A named, described, empty
  repo in a high-demand slot is the kind of thing that gets filled, and if it is filled by someone
  else it stops being an opportunity.
- 🟡 **`dmitry-viskov/pylti1.3` (MIT, 138★, last push 2024-08-18).** The Python LTI binding is the
  weak link for any agent build. Watch for a fork gaining activity, or for the upstream to wake.
- 🟡 **`DavidLMS/learnmcp-xapi` last push (2025-08-29).** If it stays still, the bridge has to be
  built rather than adopted.
- 🟢 **France's fuller AI-in-education plan**, expected spring 2026 per the June 2025 *cadre
  d'usage*; and whether a **national monitoring body** is created, since its absence is the
  assurance opening.
- 🟢 **Jisc's AI marking and feedback pilots (38 UK institutions).** Findings from a 38-institution
  programme would be the best outcome evidence available in this market.
- 🔴 **Colorado's reported AI Act repeal (May 2026) and the FERPA-covered-institution exemption** —
  unconfirmed by any second source this pass. **Either confirm it against the state legislature or
  strike it; it must not reach a client either way until then.**
- 🟡 **Whether "APAC" and "LATAM" are mis-queried the way "EMEA" was.** `ACTION BK` proved the
  sales-region word reaches enterprise IT rather than ministries. The same test has not been run on
  the other two region words — see `ACTION BM`.

### 🆕 Added to the watch list by p135

- 🔴 **Whether an identity broker appears** — an MCP server, or a component in front of one, that
  verifies an LTI launch or an OIDC assertion itself rather than accepting `caller_identity` on
  trust. **This is the single most consequential thing to watch on this shelf** (`T13`). It would
  turn the sanctioned path from a build into an assembly.
- 🔴 **Whether anything at all appears for Caliper Analytics.** One repository, 0★, unlicensed,
  untouched since 2023. A permissive client above ~50★ would reframe `T12` and partially unblock the
  measurement layer of `T7`.
- ~~🟡 **Whether `pipwerks/scorm-api-wrapper` gains a licence.**~~ 🔴 **ANSWERED BY p136, and the
  question was wrong.** It has declared one all along — `package.json` and the source header, *"MIT-style
  license"* at an off-repository URL. The propagation question is answered too: **one** row on this
  KB's pages (`numbas/Numbas`, by **vendoring**), and **293 files** sector-wide carrying the header.
  🟡 **Watch instead** whether it ever ships an SPDX-identifiable text, since *"MIT-style"* names no
  standard body, and note its **HEAD commit is 2018-09-06**.
- 🟡 **Whether `learnmcp-xapi` is maintained or forked.** Last push **2025-08-29**, and it is still
  the only agent↔xAPI bridge in existence. Its docstrings describe a JWT trust anchor it does not
  implement, so a maintained fork would be a natural place for the identity work above to land.
- 🟡 **Whether `Selleo/mentingo` keeps its pace.** MIT, 92★, pushed 2026-10-10, and the only row
  where the AI *is* the platform rather than a connector onto someone else's. If it sustains, it is
  a fork base; if it stalls, it is a reference architecture.
- ~~🔴 **Japan's national AI-education policy, which this pass measured ABSENT.**~~ 🟢 **RESOLVED BY
  p136 (`ACTION BT`): Ver.2.0 of 2024-12-26, circular 6文科初第1895号, Ver.1.0 in July 2023.**
  🟡 **Watch instead** for the **Ver.2.1** text, whose draft direction names agentic AI, cognitive
  offloading and assessment — the first national instrument this KB has seen address **agentic** AI
  in schools directly, and therefore the most quotable document in the region when it lands.
- 🟡 **Whether Colorado's enforcement stay is lifted** (`X. AI LLC v. Weiser`) and whether the AG's
  rulemaking lands by its **2027-01-01** deadline. The compliance dates are not stayed; the cure
  period ends 2030.
- 🟡 **Whether ELM (European Learner Model) supply grows beyond three repositories**, and whether any
  of it appears in a language other than Rust. It is the EU's cross-border credential model and the
  only permissive implementation is a language mismatch for most AI work.

### 🆕 Added to the watch list by p136

- 🔴 **Whether anyone writes the LTI→broker adapter.** Six identity brokers exist and none
  terminates an LTI 1.3 launch; `topic:lti` + `topic:mcp` is **two** repositories, neither
  implementing LTI. 🟢 **This is now the single most consequential thing on this shelf** (`T13`
  rewritten): the first repository that verifies an LTI launch and issues a broker token bound to
  that subject closes `T13` and turns `P13` into procurement.
- 🟡 **Whether `giantswarm/mcp-oauth` stays alive and gains adopters.** Apache-2.0, **14★**, pushed
  the day of this pass, 56 test files, MCP spec 2025-11-25. 🔴 **Its star count is small enough that
  bus-factor is a real question for a component a client's security team must trust** — compare
  `atrawog/mcp-oauth-gateway` (60★) and `NapthaAI/http-oauth-mcp-server` (108★), and watch whether
  one of the three becomes the obvious default.
- 🔴 **Japan's Ver.2.1 guideline**, expected within FY2026 — agentic AI, cognitive offloading,
  assessment (see `T10`'s third clause and `intel/market.md` → APAC).
- 🔴 **Whether South Korea's reversal spreads.** The National Assembly stripped AI textbooks of
  official status in August after sub-30% adoption. 🟡 Watch whether any other APAC mandate slips on
  **readiness** grounds — the stated reason — because that is the teacher-capacity engagement
  (`compose/patterns.md` → **P5**) arriving as a procurement, not a pilot.
- 🟡 **Whether Ohio enforces.** Its district AI-policy deadline of **2026-07-01** has elapsed. Watch
  for the first compliance review, audit finding or state report naming districts without a policy —
  the moment the North American conversation moves from drafting to evidence.
- 🟡 **Whether a tree-level licence probe changes `T15`.** The falsifier is explicit: if vendored
  third-party code turns out to be rare across this corpus, slug-level licence verdicts are good
  enough and `T15` is four unlucky examples rather than a trend.
- 🟡 **Whether `GarethManning/education-agent-skills`' ShareAlike obligation becomes visible in
  practice.** 847★, 122 forks, CC-BY-SA-4.0 by deed. Watch whether any fork publishes adaptations
  under the same licence — the first test of whether a content licence on an agent-skills pack is
  honoured or ignored.
