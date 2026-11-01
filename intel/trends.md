---
industry: education
region: Global
updated: 2026-11-01
---

## p597 — 2026-11-01 — the verification instrument this harness is told to use cannot distinguish a live repository from a dead one, and the two "nil" channels it reports are independent

## 55. The host you verify at decides the answer, and the host named in the instructions is the one that cannot answer

🔴 **Measured this pass:** `curl -sI https://github.com/<owner>/<repo>` returns **`403`** for every
repository not attached to this session — not `404` for a dead address and `200` for a live one, but
`403` for both. 🔵 The run prompt's standing instruction is *"verify every URL before writing it
(`curl -sI`). A 404 is not a finding."* 🔴 **Executed literally in this environment that instruction
rejects every true row**, because it never sees a `404` *or* a `200`; `20` live, permissive,
institution-grade repositories were promoted this pass and all `20` answer `403` at that host.

| instrument | `jupyterhub/jupyterhub` (live) | `DaRL-GenAI/instructional_agents` (live, **unindexed**) | `nonexistent-org-xyz99/nope-12345` (truly dead) | separates live from dead? |
| --- | --- | --- | --- | --- |
| `curl -sI github.com/…` | 🔴 `403` | 🔴 `403` | 🔴 `403` | 🔴 **no — one answer for all three** |
| GitHub search API, `repo:` qualifier | 🟢 full record | 🔴 **`total_count 0`** | 🟢 `total_count 0` | 🔴 **no — live-but-unindexed is indistinguishable from dead** |
| GitHub search API, `user:` listing | 🟢 listed | 🔴 **absent from all `15` indexed repos of that owner** | 🟢 absent | 🔴 **no** |
| `curl raw.githubusercontent.com/…` | 🟢 `200`, `1,475 B` | 🟢 `200`, `1,067 B` | 🔴 `404` | 🟢 **yes — `28/28` live, `404` on the control** |
| `WebFetch https://github.com/…` | 🟢 page renders | 🟢 `490★`, `106` forks, MIT | 🔴 no page | 🟢 **yes** (and it works where `curl` gets `403`) |

🔴 **`597-F` — the correction this pass had to make against itself, mid-pass.**
[`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) was written
into three pages of this base **as a dead address** on the strength of `total_count 0`. 🟢 It is
live: `490★`, `106` forks, MIT (`1,067 B`, byte-read), an **EACL'26 Main** peer-reviewed multi-agent
instructional-design system, with its package published on PyPI. 🔴 **It is simply absent from the
GitHub search index** — `user:darl-genai` lists `15` repositories and this is not one of them, while
four *siblings* (`instructional_agents-skills`, `instructional_agents_studio`,
`instructional_agents_homepage`, `MASkills`) **are** indexed. 🔵 Search-index membership is not
existence, and a `0` is not a `404`.

🔵 **A wrong explanation was also drafted and withdrawn.** The first hypothesis was case-sensitivity
in the `repo:` qualifier, since the canonical owner is `DaRL-GenAI` and this base's census
lower-cases every address. 🔴 **Refuted by measurement:** `repo:DaRL-GenAI/instructional_agents`,
`repo:darl-genai/instructional_agents` and `repo:DARL-GENAI/INSTRUCTIONAL_AGENTS` all return
`total_count 0`. 🟢 Had it been published, it would have sent the next pass to re-case `1,449`
addresses for nothing.

🔴 **The search API has its own false negative:** it returns `422 "cannot be searched either because
the resources do not exist or you do not have permission"` for
[`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet),
which is alive and served a `1,092 B` MIT grant from `raw.githubusercontent.com` on the same pass.
🔵 **A `422` reads as "dead" to any screen that only checks for success.**

🟢 **The standing prescription:** liveness and grant are established at `raw.githubusercontent.com`
or they are not established. The GitHub API is a metadata *enrichment* (stars, push date, default
branch, archived flag), never the existence test, and `github.com` itself is not an instrument here
at all.

## 56. A repository's declared licence field and its actual code grant are different objects, and they diverge in at least three structurally different ways at once

🔴 This pass byte-read `21` grants and found the API's `spdx_id` wrong in **three distinct shapes**
inside a single sitting — not three instances of one bug:

| shape | instance | API says | the code grant is | the trap |
| --- | --- | --- | --- | --- |
| **Two grant files, one for prose and one for code** | [microsoft/autogen](https://github.com/microsoft/autogen) | 🔴 `CC-BY-4.0` | 🟢 **MIT** — `LICENSE-CODE`, `1,141 B`, root + `7` package trees | The API is *correct* about `LICENSE` (`18,650 B`, genuinely Creative Commons) and *useless* for reuse. A compliant screen **rejects** a `61,661★` MIT framework |
| **A grant with no title line** | [crewaiinc/crewai](https://github.com/crewaiinc/crewai) | 🟢 `MIT` | 🟢 **MIT** — `1,055 B`, opens `Copyright (c) 2025 crewAI, Inc.` | A title-matching byte-reader returns `UNRECOGNISED`; the grant must be identified by its **operative clause** (`Permission is hereby granted, free of charge…`), not its heading |
| **A grant filed under a national spelling** | [oaknational/oak-open-curriculum-ecosystem](https://github.com/oaknational/oak-open-curriculum-ecosystem) | 🟢 `MIT` | 🟢 **MIT** — the file is **`LICENCE`**, `1,086 B` | A probe enumerating `LICENSE`/`LICENSE.md`/`LICENSE.txt` reports **no licence** for a national body's MIT repository |

🔵 **The three failures point in opposite directions**, which is why no single fix covers them: the
first needs the *file set* enumerated, the second needs the *contents* parsed rather than the title,
the third needs the *filename* spelled both ways. 🟢 A probe must do all three and must report which
file it read and how many bytes, so a later pass can tell a measurement from an assumption. 🔴 **This
base recorded "AutoGen (MIT)" in two earlier cycles and was right by luck**, never having opened the
file.

## 57. Saturation is a per-channel property, and an undifferentiated "nil" cannot tell a saturated channel from a broken gate

🔴 For `27` consecutive passes this base reported "nil" across its search legs and read that as a
fact about the education industry. `596-C` then found the gate was consulting append-only logs that
never forget. 🟢 **Rebuilt this pass to read the shelf and the logs as separate answers, the single
"nil" split into two opposite results:**

| channel | measurement | verdict |
| --- | --- | --- |
| **Market / demand-side tokens** | `22 of 24` tokens held **on the shelf itself**; `1` new; `1` log-only | 🔴 **The nil is real** — twenty-eighth consecutive pass. A genuinely saturated channel |
| **Addresses / supply-side** | `2,640 of 3,366` ever-shelved addresses (`78.4 %`) carry no current disposition; **`2,049`** are reported "held" by a log-grepping gate | 🟢 **The nil was an artifact** — `18` real rows promoted this pass without running a single new search leg |

🔵 **The two channels of one industry saturated independently**, and the aggregate statistic was the
average of a true finding and a false one. 🟢 **The prescription is that a nil must name its
channel** and must state which page class it was gated against; a bare "no new findings" is not a
measurement. 🔴 It also means the fix for one channel buys nothing in the other: correcting the gate
recovered `20` supply-side rows and changed the demand-side result by **one token**.

---

## p596 — 2026-11-01 — twenty-seven passes of "nil" was not measuring the industry or the search channel; it was measuring this base's own refusal to file what it had already found

## 52. In education's platform-of-record tier the binding rule is not "copyleft with one exception" but "permissive platforms exist and are invisible to a star-based screen", because the permissive ones are microservice estates whose weight is spread across hundreds of repositories (high confidence — one platform measured at organisation level, `456` repositories, `0` copyleft)

`p584` established this industry's platform tier as *copyleft with exactly one permissive
exception*, and `p588` added a second. 🔵 **Both were found by looking at repositories.** This
pass looked at an **organisation** and the rule weakened again.

| `org:folio-org` | repos |
| --- | --: |
| total | **456** |
| 🟢 `license:apache-2.0` | **398** (`87.3 %`) |
| 🔴 any copyleft (`gpl`/`agpl`/`lgpl`) | 🟢 **`0`** |
| 🟡 no licence field — auxiliary tooling, CI, docs, Helm | `57` |

🟢 **FOLIO is a full system of record** — patrons, inventory, circulation, acquisitions, ERM —
and a studio may fork it, modify it and ship it closed. 🔴 **Its largest single repository is
`okapi` at `134★`, and its inventory module — the actual system of record — is `4★`.** 🔵 **So
any screen that ranks platforms by stars on one address rates a live, Apache-2.0,
institution-grade platform below a `2,000★` single-repo demo.** That is how FOLIO sat in this
base's trending logs across several passes without ever reaching a shelf.

🔴 **The operational sting is on the deployment path.** The `57` unlicensed repositories are
not platform code, but **`folio-org/folio-helm` is among them** — so the platform is
permissively licensed and the most common way to deploy it carries no grant at all. 🔵 Cheap
to fix, and it has to be known before procurement rather than after.

🟢 **Instruction this trend carries:** for the platform tier, screen on **organisation-level
licence uniformity and liveness**, never on one repository's stars.

## 53. A permissive licence and a real corporate owner are now jointly insufficient to clear an education repository, because the major clouds publish education AI as explicitly disclaimed proof-of-concept work — and the disclaimer excludes the population the tool is built for (high confidence — one instance measured first-hand, and it clears every other screen this base runs)

🔴 [`GoogleCloudPlatform/aira`](https://github.com/GoogleCloudPlatform/aira) — *Artificial
Intelligence Reading Assessor*, Apache-2.0 byte-read at `11,357 B`, `24★`, live, not archived,
authored by Google Cloud education engineers. 🟢 **It clears licence, liveness, provenance and
relevance — every screen this base runs.**

🔴 **Its README disqualifies it**, and the terms are not boilerplate:

| declaration | consequence |
| --- | --- |
| 🔴 *"an open-source **demo experiment**"* / *"**proof-of-concept only**"* | not a base to build on |
| 🔴 *"**not an officially supported Google product**"* | the brand carries no support obligation |
| 🔴 *"Please do not use any personal or sensitive data"* | cannot touch learner records |
| 🔴 *"should not be used by children under **13**"* | 🔴 **excludes K-12 — the population a reading assessor exists for** |

🔵 **Why this is a trend and not an anecdote.** A permissive licence on a cloud vendor's
education demo is a *marketing* artefact, not a support commitment, and the gap between the
two is widening as the clouds publish more education AI reference work. 🔴 **A licence screen
cannot see it.** The disqualifying text is in the README, in prose, and an under-13 exclusion
on an education tool is categorical rather than a caveat.

🟢 **Instruction: read the README's own status and audience declarations before promoting any
row, and treat a PoC or under-13 disclaimer as a `BLOCK` regardless of grant and
provenance.** Registered as `596-D`.

## 54. When a knowledge base pairs an append-only discovery log with periodically rewritten curated pages, and gates new findings against the log, every row the rewrite drops becomes permanently unrecoverable — and the base reports a saturated market (high confidence — `3,174` addresses classified against `15` archived shelf snapshots, `2026-11-01`)

🔴 Measured this pass with a collation-free instrument, against the `15` shelf snapshots under
`archive/` named `pre-reset`, `pre-rewrite`, `pre-trim` and `pre-consolidation`:

| population | count |
| --- | --: |
| addresses in the ledger | `3,174` |
| 🔵 logged on the two append-only trending pages | `3,143` |
| 🟢 on a **current** shelf page | **`234`** |
| 🔵 on **any** shelf page ever | `2,243` |
| 🔴 **dropped** — shelved once, absent from every current shelf | 🔴 **`2,015`** (`89.8 %` of ever-shelved) |
| never shelved anywhere | `921` |
| lines on the trending pages vs the shelf pages | `115,968` vs `6,516` |

🔴 **Two storage disciplines with opposite loss behaviour, and the base treats them as one.**
The trending log is append-only and forgets nothing. The shelves are rewritten wholesale and
have lost `89.8 %` of everything ever placed on them.

🔴 **The failure is in the coupling, not in either half.** `569-B` requires every candidate to
be grepped against this base before being called new — and that grep hits the **log**. 🔴 **So
a row dropped by a rewrite still answers *"already held"*, forever, and can never be recovered
by searching.** The row is simultaneously absent from the shelf and permanently ineligible for
re-entry.

🟢 **The symptom is indistinguishable from market saturation**, which is how this base read it
for twenty-six passes. 🔵 **The diagnostic that separates them is cheap**: compare the curated
pages against the archived snapshots, not against the log. `6` rows were recovered that way
this pass, none of which needed a search leg.

🟢 **It also corrects `595-A`.** `p595` registered `118 MB` and no retention policy as a size
problem. 🔴 **The `118 MB` is the only part of this base that never loses anything**; the
expensive defect is the rewrite that trims the shelf. 🔵 A retention policy that prunes the log
would remove the one durable record and leave the lossy half untouched.

## p595 — 2026-11-01 — twenty-six passes of nil is no longer a research result about the industry; it is a measurement of the channel, and the cost of the record is now itself the finding

### The legs, measured against this base before being called new

All four mandated regional legs ran, plus the four global legs and one topic axis
(`grading / autograder / rubric`). Every token was grepped against this base before being
called new — `569-B`'s standing requirement.

| token served | region | already in this base? |
| --- | --- | --- |
| Digital Omnibus **Regulation (EU) 2026/1744** — high-risk education duties slip `2026-08-02` → `2027-12-02` | EMEA | 🔴 held — `55` files |
| EU AI Act **Art. 50** transparency duties live `2026-08-02`; emotion-recognition ban live since `2025-02-02` | EMEA | 🔴 held — `46` files |
| **South Korea AI Basic Act** in force Jan 2026 (grace year, guidance-first) | APAC | 🔴 held — `45` files |
| **Vietnam** 2026 AI law — education named among six high-risk sectors | APAC | 🔴 held — `78` files |
| **TEQSA** (Australia) mandatory university gen-AI action plans | APAC | 🔴 held — `11` files |
| UNESCO **IESALC / UNU** study — 200 HEIs, 19 countries | LATAM | 🔴 held — `57` files |
| **87 %** of LAC institutions use AI in ≥1 area; **26 %** hold a formal strategy; **74 %** in teaching | LATAM | 🔴 held — `39` files |
| **716** AI regulatory instruments across 23 countries (U. de los Andes) | LATAM | 🔴 held — `27` files |
| UNESCO **Observatory on AI in Education for LAC**, Santiago, `2026-04-14` | LATAM | 🔴 held — `11` files |
| US **134 bills in 31 states** | North America | 🔴 held — `37` files, **sixth** consecutive pass |
| **NY A 9190** (grade-9 floor), **MD SB 720 / HB 1057** | North America | 🔴 held — `10` / `22` files |
| **K-12 AI Literacy and Readiness Act of 2026** advanced in committee | North America | 🔴 held — `23` files |
| Mandatory district AI policy in **ID, OK, VA, MD** | North America | 🔴 held — `23` files |

🔴 **`13 of 13` already held — no region returned a token this base lacks.** This is the
**twenty-sixth** consecutive nil on the mandated legs, and it is now a measured property of
the channel rather than a run of bad luck. 🟢 **Stated as the prompt requires: the gap is
not regional silence.** Every region answered, and every region answered with this base's
existing picture. The four global legs returned `DeepTutor`, `OpenMAIC`/`MAIC` (held, `148`
files), `ai-agents-for-beginners`, `CrewAI` and `AutoGen` — **zero new addresses**.

### 🔴 `595-A` — a standing defect nothing in this base has ever recorded: it has no retention policy

Measured this pass with `du`, and grepped first to confirm it is unrecorded
(`repo size` → `0` files, `bloat` → `0`, `archive policy` → `0`):

| path | size |
| --- | --: |
| `compose/` | **53 MB** |
| `archive/` | **31 MB** |
| `evidence/` | **17 MB** |
| `agents/trending.md` | **5.3 MB** (`65,414` lines) |
| `repos/trending.md` | **4.0 MB** (`50,386` lines) |
| `README.md` | **2.7 MB** |
| `Makefile` | **144 KB** |
| **working tree total** | **118 MB** |

🔴 **The append-only rule that protects the trend record has no counterpart that bounds
it.** At `~595` passes the two trending pages are `115,800` lines between them; a reader
looking for this week's signal pages through fifty thousand lines of history to find it, and
a `git clone` of a single-industry KB now moves `118 MB`.

🔵 **This is a finding, not an action.** Pruning history would destroy the trend record the
append-only rule exists to preserve, so this pass did **not** truncate anything. What is
needed is a *retention decision* — most plausibly: keep the newest `N` passes inline and
roll older sections into `archive/` with an index — and that decision belongs to whoever
owns this KB, not to pass `595`.

---
## p594 — 2026-11-01 — a licence rule adopted mid-life does not re-grade the shelf behind it, and the two rules this base adopted three passes apart are mutually destructive

## 50. In an append-only curated base, adopting a classification rule silently creates two cohorts — rows graded under the new rule and rows still carrying the old grade — and the old cohort is where the dangerous errors live (high confidence — mechanism identified and one live instance found at `2,057★`)

`p591` adopted `591-A`: classify a licence on its **title**, not its body, because two candidates
(`ximing/aimo` → Business Source License 1.1, `SethRobinson/UGTLive` → Proton SDK licence) contained
MIT's permission sentence verbatim while being something else entirely. The rule was correct. 🔴 **It
was applied to candidates arriving after it and never to rows already published.**

**The live instance.** [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) (`2,057★`) sat on
this industry's agent shelf marked 🟢 **`MIT (text)`** — under a legend reading *"permissive …
buildable and shippable in client work"*. Byte-read this pass, its `LICENSE.md` is the **"PageLM
Community License"**: non-commercial use only, redistribution *"strictly prohibited"*, commercial
use conditional on a **signed revenue-sharing agreement**, breach of which is *"a material breach
and immediate termination"*. 🔴 **It is not MIT and it is not open source.** The `(text)` mark means
a pass did byte-read the file — and read MIT's opening sentence and stopped.

**Why this generalises past one row.** A curated base that is append-only in its *history* is
mutable in its *pages*, and a rule change touches only what a pass happens to look at. The cohort
boundary is invisible because both cohorts render identically: a 🟢 from `p560` and a 🟢 from `p594`
are the same glyph carrying different amounts of evidence. 🔵 **And this base predicted it in writing.** `591-G`, registered the same pass the rule was
adopted, states that *every `(text)` licence mark filed before `p591` is unauditable* and prescribes
the audit that catches it — a byte-size filter on the claimed licence. 🔴 **It was never run, for
three passes.** 🟢 Run at `p594` over all `99` `(text)` rows it flags `8`, of which `2` are real
mis-grades, `PageLM` among them at a `7.8×` size discrepancy. 🔵 **So the failure was not a blind
spot — it was a known, documented, costed exposure that no pass spent its budget on.** That is the
more uncomfortable finding and the more generalisable one.

🔵 **Three instances of one pattern,
across three passes, with only the two newest caught**, is the signature of rule-without-sweep —
and the signature is visible only from outside the pass that introduced the rule.

**The operative consequence.** 🟢 **When a pass adopts or revises a licence rule it must re-grade
every row already published under the old rule and record the count swept.** A rule with no sweep
attached is a rule that protects future rows and abandons present ones, which is the wrong way
round: the published rows are the ones a reader is acting on today. Falsifiable: a sweep of the
remaining `(text)` rows finding no further mis-grade would bound the damage at one row, and that
sweep has not been run.

## 51. A licence probe has at least five independent axes on which it returns a confident wrong answer instead of an error, and the two corrections this base adopted three passes apart cancel each other out (high confidence — all five demonstrated first-hand on live rows, `2026-11-01`)

`593-B1` named one axis — a probe that hardcodes `main`/`master` receives `404` on every filename
and concludes "no licence file exists". This pass measured that axis across the whole curated base
and found four more beside it. 🔵 **What the five have in common is the only property that matters:
none of them fails loudly.** Each returns a well-formed wrong answer, so none appears in a channel
table as a failure.

| axis | measured this pass | wrong answer produced |
| --- | --- | --- |
| 🔴 **default branch** | **`30 of 253`** curated addresses (`11.9 %`) on `18` names other than `main`/`master`; `19` give `404`, and `11` give a **`200` from a branch the project does not ship** | "no grant" — or worse, a stale grant that reads as success |
| 🔴 **filename case** | `frappe/erpnext`, `frappe/lms`, `frappe/education` keep grants at lowercase **`license.txt`**; `NO-GRANT-FILE` from both a `6`- and a `7`-path probe | three live ERP/LMS rows filed unlicensed |
| 🔴 **prose prepend** | `odoo/odoo` (`55,463★`) and `openeducat_erp` open *"For copyright information, please see the COPYRIGHT file."*; the grant (`LGPL-3.0`) is declared on **line 2** | a title-based rule returns nothing |
| 🔴 **grant language** | `portabilis/i-diario`, `portabilis/pre-matricula-digital` → **`LICENÇA PÚBLICA GERAL AFFERO GNU`** | English matcher false-blocks two live Brazilian school systems |
| 🔴 **unanchored abbreviation** | an unanchored `MPL` substring matches **`65 of 65`** grants read, because every licence disclaims warranties *"EXPRESS OR I`MPL`IED"*; `MIT` matches `li`**`mit`**`ation`, `sub`**`mit`**`ted`, and `Technische Hochschule `**`Mit`**`telhessen` | false **permissive** — the worst direction to be wrong in |

**🔴 The collision, which is the finding.** `591-A` says *classify on the TITLE*. `593-B` found
grants **whose title is prose**. Run `591-A` on `odoo/odoo` and it resolves nothing; run a body
match on it and the appended GPL text can return `GPL-3.0` when the actual grant is the **weaker**
`LGPL-3.0` — an answer that is wrong in the restrictive direction and would retire the Odoo-family
recipes this KB is built on. 🔵 **Two corrections adopted three passes apart, each sound on its own
evidence, are jointly insufficient, and neither pass could have seen it** — `591-A`'s cases had
clean titles and `593-B`'s case had prose.

**🟢 The instrument that survives all five.** A three-stage read, in order: **(1) the licence
title; (2) a *"published / licensed / released under X"* declaration in the first 40 lines, which
beats the body; (3) the body, last.** Plus: branch from the API before any path probe, `13`
path/case variants, full licence names or whole-token abbreviations only, and **a title/body
disagreement escalated to review rather than resolved**. 🟢 Run that way against `10` known-hard
rows it returns **zero false permissives**, resolves `odoo` and `openeducat_erp` to `LGPL-3.0` from
their line-2 declaration, resolves the Portuguese AGPL rows, recovers
`thm-mni-ii/feedbacksystem` as **Apache-2.0** from a blank field, and **refuses to pass `PageLM`**.

🔵 **Why high confidence:** every axis is demonstrated on a named live row rather than hypothesised,
the `30`-row figure is a census and not a sample, and the corrected instrument was validated
against the cases that defeated its predecessors — including the one that defeated this pass's own
first draft (`594-E`). Falsifiable: a sixth axis, or any row where the three-stage read returns a
false permissive.

---

## p593 — 2026-11-01 — the EMEA risk is capability, not compliance; and a licence instrument that assumes the branch name fails silently on the exact rows it exists to rescue

## 48. In EMEA the regulation is ahead of the capability, which inverts where the delivery risk sits — the binding constraint on an EMEA education engagement is the client's ability to operate what is shipped, not its ability to comply (medium confidence — two independent `2026` instruments pointing opposite ways, one new this pass)

This page has framed EMEA as the compliance-first region since `p586`: AI Act, GDPR, high-risk
classification for assessment, and from `p592` a high-risk clock that no longer waits for
standards. That framing is intact. What it was missing is the other half of the picture.

**The two instruments.** 🟢 New this pass: the European Commission maintains an **AI literacy
framework for primary and secondary education**, before the Council under the **European Education
Area 2026–2030** agenda, titled *"Empowering learners for the age of AI"*; and the Council of
Europe's AI & Education expert group reports a **lack of rigorous monitoring and regulation**,
asking for coordinated national and European action. 🔴 Also new: **Allianz Pulse 2026** finds
Europe adopting AI **less extensively and much less work-adjacently than the US**, with wide
internal spread and an explicit **"preparedness gap"**.

**Why the pair matters more than either.** A region can be ahead on rules and behind on practice
at the same time, and EMEA is. Compared with LATAM — where `92 %` of students and `79 %` of
faculty already use AI against almost no institutional governance (`p58x`, reconfirmed `p593`) —
EMEA is the **mirror image**: the governance arrives first and the usage lags.

**The operative consequence.** On a LATAM engagement the deliverable is governance for usage that
already exists. 🔴 **On an EMEA engagement the deliverable is capability**, and the failure mode is
a compliant system nobody is equipped to run. The AI literacy framework is the commercial opening
precisely because it is *the capability gap written as policy* — entry comes through curriculum
and training, not through platform. **Budget enablement as scope, not as courtesy.**

🔵 **Confidence is medium, not high**, and the reason is explicit: Allianz is a single
cross-sector survey not specific to education, and the literacy framework is an agenda item
rather than an in-force instrument. The direction is corroborated twice; the magnitude is not
measured. Falsifiable: an EMEA education-AI capability or staffing survey showing parity with the
US would withdraw this.

## 49. A licence instrument that hardcodes the branch name fails silently on exactly the rows it exists to rescue — producing a confident `license: null` block on a permissively licensed base (high confidence — mechanism identified and one base recovered, `2026-11-01`)

Trend `44` (`p591`) established that `license: null` and `NOASSERTION` are distinct blank states
with opposite instructions. This pass reproduced it on `5` fresh repos and found the defect in
the **instrument**, not the field.

**The recovery.** `openeducat/openeducat_erp` (`903` stars) reports `NOASSERTION`. Its `LICENSE`
states **GNU LGPL-3.0** without ambiguity. 🔵 The matcher fails because the file **prepends prose**
— *"For copyright information, please see the COPYRIGHT file."* — ahead of the licence text. So
an education ERP base that is genuinely usable (weak copyleft: new Odoo modules may link without
being forced open) was sitting behind a blank field.

**The counter-arm, same pass.** `GarethManning/education-agent-skills` (`937` stars) also reports
`NOASSERTION`; its `LICENSE` is **`CC-BY-SA-4.0`** — a share-alike *content* licence, unusable as
a code base. 🟢 Two identical API values, opposite conclusions. A blanket block is as wrong as a
blanket pass.

**🔴 The new and more dangerous half — sub-gap `593-B1`.** `openeducat_erp`'s default branch is
**`19.0`**, not `main` or `master`. A byte-read probe that walks the usual branch names receives
`404` on *every* filename and concludes **"no licence file exists"** — i.e. it files a usable
`LGPL-3.0` base as a hard block. 🔵 **This failure is silent**: it returns a confident wrong
answer rather than an error, so it never appears in a channel table as a failure. Any licence
instrument in this base must read `default_branch` from the API **before** probing paths. Three
rows this pass were filed `license: null` by probe — those verdicts stand only because all three
default to `main`, which is luck, not method.

**Why high confidence.** The mechanism is identified on both arms, one address was recovered and
one condemned, and the branch defect is demonstrated rather than hypothesised.

---

## p592 — 2026-11-01 — a deferred deadline is not a reprieve when it stops waiting for standards, and the shelf's permissive majority is in the wrong layer

🔵 **Two trends filed at `##` with the counter's own `^## <n>. ` form (46–47).** Trend 46 is
a regulatory reading carried by secondary sources and labelled as such; Trend 47 is measured
first-hand this pass across **`192 of 192`** curated addresses and is the first
licence-composition census in this base.

## 46. The EU deferral removed the escape hatch it looked like it granted — the high-risk clock now runs on the calendar, not on standards readiness

🔵 **The headline everyone took from the Digital Omnibus was *16 more months*.** Stand-alone
Annex III high-risk obligations — which is where education sits, alongside grading,
admissions and proctoring — moved from `2 August 2026` to **`2 December 2027`**, and
product-embedded Annex I systems from `2 August 2027` to **`2 August 2028`**.

🔴 **The part that matters more got less attention: the new dates apply whether or not the
harmonised standards are ready.** The Commission's original proposal would have tied the
start of high-risk obligations to the *availability* of those standards. The adopted
instrument does not. 🔵 **Those are different kinds of deadline.** A standards-linked
trigger is open-ended, and a vendor can rationally plan to sit behind it, because the
obligation cannot begin until someone else finishes work that is visibly unfinished. A fixed
calendar date arrives on an education product on schedule, conformity toolkit or not.

🟢 **What this changes in a proposal.** Annex III education work scoped for the EU should
treat `2 December 2027` as firm and budget conformity assessment, human-oversight design and
technical documentation against it — rather than treating the deferral as a signal that the
regime keeps slipping. 🔵 **And the transparency duties were never deferred at all:**
Article 50 has applied since **`2 August 2026`**, with a **`2 December 2026`** backstop for
machine-readable marking of systems already on the market. A studio shipping generated
feedback or synthetic content into the EU has a live obligation *now* and a firm one in 2027
— not one distant deadline.

🟡 **Provenance:** secondary. Six independent professional sources agree on the dates and the
instrument (**Regulation (EU) 2026/1744**, OJ `24 July 2026`); the decoupling is carried by
the European Parliament's legislative-train entry and one law-firm commentary. 🔴 No primary
Official Journal text has been read in this environment — `eur-lex.europa.eu`,
`digital-strategy.ec.europa.eu` and `www.europarl.europa.eu` are all unreachable here. See
gap `586-E` on [`./market.md`](./market.md), which stays open for that reason alone.

## 47. The open-source education shelf is permissive where a studio builds and copyleft where a client already runs — measured at `130 of 192` against every large LMS

🟢 **Measured `2026-11-01` across all `192` curated addresses** in
[`../agents/top.md`](../agents/top.md) and [`../repos/foundations.md`](../repos/foundations.md):

| layer | licence posture | evidence |
|---|---|---|
| Agents, components, skills, MCP servers | 🟢 **permissive majority** | `MIT` alone is **`100 of 192`** (`52.1 %`); permissive subtotal **`130`** (`67.7 %`) counting `Apache-2.0` (`24`), `BSD-3-Clause` (`4`), `ECL-2.0` and `CC0-1.0` |
| LMS / platform of record | 🔴 **share-alike, without exception at scale** | `bigbluebutton` `LGPL-3.0` (`9,262★`), `openedx-platform` `AGPL-3.0` (`8,214★`), `dolibarr` `GPL-3.0` (`7,814★`), `moodle` `GPL-3.0` (`7,569★`), plus `frappe/lms`, `chamilo-lms`, `ILIAS`, `tutor`, `classroomio`, `learnhouse`, `courselit`, `rosariosis` |
| Permissive platform alternatives | 🟡 **they exist, at a fraction of the reach** | `sakaiproject/sakai` `ECL-2.0` (`1,240★`), `pupilfirst` `MIT` (`981★`, 🔴 last push `2025-12-09`), `mentingo` `MIT` (`103★`) |

🔵 **So the licence question in an education engagement is not "can we find permissive
software" — it is "which layer are we touching".** Two-thirds of this shelf is shippable in
client work. But the system the client already runs is almost certainly copyleft, and every
permissive substitute for it is at most **`~13 %`** of the incumbents' reach, with the
largest-but-one of those substitutes stale for `~11` months.

🟢 **This is a census confirming advice this base previously held on examples:** extend the
platform over a documented seam — LTI 1.3, xAPI, SCORM, an MCP server against the LMS API —
and keep the studio's own code in the permissive agent layer. 🔴 **The failure mode it rules
out is the tempting one**: forking Moodle or Open edX to embed an agent produces a modified
AGPL/GPL platform and a distribution obligation, for a capability that the seam would have
delivered without one.

🔵 **One honest limit on the `130`.** It is the API channel's count, and the API cannot answer
for **`42 of 192`** addresses (`29` `NOASSERTION`, `13` `null`). That set is mixed — it holds
rows with a real `MIT` grant in their `LICENSE` text (`relate`, `word-atlas`,
`LLMs-from-scratch`, `pupilfirst`) *and* rows with no grant at all (`Agent4Edu`,
`Multi-Agent-Study-Assistant`). 🔴 **`NOASSERTION` is therefore not evidence in either
direction**, and for one row in five the licence on these shelves rests entirely on a text
read — which is why `p591` made the text channel the authority.

---

## p591 — 2026-11-01 — a byte-read is not a verified licence if the matcher reads the body; the API's two licence blanks carry opposite instructions; and the in-language supply gap is a LICENSING gap in LATAM and an ABSENCE in EMEA

🔵 **Three trends filed at `##` with the counter's own `^## <n>. ` form (43–45), plus one
standing gap re-measured.** Every repository figure below was measured first-hand
`2026-11-01` via `gh api search/repositories`; every grant was byte-read via
`raw.githubusercontent.com` with `404` controls established on that channel for the first
time in this base.

## 43. A licence read from the repository's own file is still wrong if the classifier matches the licence BODY — because a non-OSI licence can name a permissive one inside its own text (high confidence — `65` grants byte-read, `2` inverted under a title-anchored re-read, mechanism identified in both)

🔴 **This base's `(text)` mark means "read from the repository's own licence file rather
than the GitHub API", and since `p585` that mark has been treated as ground truth.** 🔴 **It
is not sufficient, and this pass produced the counter-examples by committing the error.**

A classifier matching `MIT License` anywhere in the fetched text reported two non-OSI
licences as MIT:

| Repo | Body says | 🔴 Title says | Mechanism |
|---|---|---|---|
| [ximing/aimo](https://github.com/ximing/aimo) (`27★`) | `MIT` | 🔴 `Business Source License 1.1` | 🔴 **BSL declares a `Change License` inside its own body** — the permissive licence it will *become* after the Change Date. Here that value is MIT. The matcher read the promise and filed it as the grant. |
| [SethRobinson/UGTLive](https://github.com/SethRobinson/UGTLive) (`118★`) | MIT's full permission sentence, verbatim | 🔴 `The Proton SDK License (based on the XFree86 1.1 license…)` | 🔴 A bespoke licence that **embeds MIT's operative sentence** inside additional terms. |

🟢 **Fix: classify on the first non-empty line of the file.** Both invert; `63 of 65`
reads are unchanged, so the error rate is `3.1 %` — low, 🔴 **and both errors ran in the
permissive direction, which is the direction that ships.**

🔵 **Two cheap secondary signals, since a title read can still be defeated by an
HTML-wrapped file** (as [`idempiere/idempiere`](https://github.com/idempiere/idempiere)'s
`LICENSE.md` is, opening literally with `<center>`): **(1) byte size** — a standard MIT
file is `~1,050–1,100 B`, and both false positives were `2,483 B` and `5,643 B`;
**(2) a marker grep** for `Change License`, `Change Date`, `Commons Clause` or
`Competition Protection`, any of which means counsel rather than a shelf row.

🔴 **Why this generalises beyond two rows:** no previous pass in this base published its
matcher. So every `(text)` mark filed before `p591` is **unauditable for this defect** —
not wrong, but not verifiable either. 🟢 The remedy is forward-looking and costs one line:
record the licence **title** beside the byte count, as the `p591` tiers on
[`../agents/top.md`](../agents/top.md) now do.

## 44. The GitHub licence API has two distinct blank states and they carry OPPOSITE instructions — `license: null` is a reliable block, `NOASSERTION` is a parser failure that never once meant "no licence" (high confidence — `22` rows byte-read at `6` filenames × `2` branches, both arms, `2026-11-01`)

🔴 **This base has graded the API's licence blank as one thing since `p579`.** `Trend 31`
records a `NOASSERTION` false-negative rate of *"about one in two"* and prescribes queuing
the flag rather than grading on it. 🟢 **That prescription is right for `NOASSERTION` and
wrong for `null`, and the two have never been separated here.** Measured:

| API state | byte-read | 🔴 had **no** licence file | 🟢 permissive OSI grant | something else |
|---|--:|--:|--:|--:|
| `NOASSERTION` | `12` | 🔴 **`0`** | 🟢 `6` — MIT ×4, Apache-2.0 ×2 | `6` — CC-BY-SA-4.0, BSL-1.1, GPL-2.0, XFree86-derived, `2` bespoke |
| `license: null` | `10` | 🟢 **`10`** | `0` | `0` |

🟢 **`null` is `10-for-10` as a block** and can be acted on without a read — which is a
genuine saving, because unlicensed repositories are the single largest class this base
rejects. 🔴 **`NOASSERTION` is `0-for-12` as a negative**: it has never once meant absence,
and it concealed a shippable grant half the time.

🔵 **The mechanism, which is why the asymmetry should be stable rather than a sampling
artefact:** GitHub's licence field is populated by a *classifier over a file it found*.
`null` means **no file was found** — a filesystem fact. `NOASSERTION` means **a file was
found and could not be classified** — and the reasons it cannot be classified are
non-standard filename, HTML wrapper, dual or split grant, or a modified preamble, **all of
which presuppose a licence exists.** 🟢 So `NOASSERTION` is positive evidence of a grant
whose *identity* is unknown, and treating it as evidence of absence inverts its meaning.

🔴 **The cost of the conflation, concretely:** this pass recovered
[`angelapaia/tutor-de-skills`](https://github.com/angelapaia/tutor-de-skills) — MIT,
`1,188 B` — from `NOASSERTION`, and it is **the Spanish-language row whose absence this
base had been publishing as a LATAM supply gap for five passes** (`591-C`, `Trend 45`).

## 45. "No in-language supply" is two different market failures wearing one label — in LATAM the supply exists and is UNLICENSED, in EMEA it is simply ABSENT, and the two need different engagements (high confidence — `27` niche and in-language axes, `45` addresses, every grant byte-read; `5.5×` asymmetry measured in one instrument)

🔴 **`p587` measured a `33×` LATAM/APAC asymmetry and this base has since carried *"LATAM
has no in-language supply to adopt"*.** 🟢 **The claim is too coarse in both directions.**

**Arm 1 — LATAM: the supply exists, and it splits by artefact type.** `12` in-language
axes, `18` addresses this base did not hold:

| in-language artefact type | addresses | 🟢 permissive | 🔴 no grant |
|---|--:|--:|--:|
| Courseware, curriculum, exercise sets, notes apps | `12` | 🟢 **`12`** (MIT ×10, Apache-2.0 ×2) | `0` |
| **Conversational AI tutors** | `6` | 🔴 **`0`** | 🔴 **`6`** |

🔵 **In LATAM the courseware licenses and the tutors do not** — a clean split at `12/12`
against `0/6`. 🟢 **Engagement shape: adopt the curriculum, build the tutor.**

**Arm 2 — EMEA, which no pass had measured.** `2` adoptable in-language artefacts, against
APAC's `11` — a **`5.5×`** asymmetry in the same instrument, 🔴 **and EMEA is thinner than
LATAM, which this base has treated as the deficient region for five passes.** 🔴 **But the
deficiency is a different kind:** in EMEA there is no unlicensed supply either. There is
**nothing**, in a region with 24 official EU languages.

🟢 **Why the distinction is commercial and not pedantic.** An unlicensed-supply gap and an
absent-supply gap have different costs and different first moves:

| | LATAM | EMEA |
|---|---|---|
| Diagnosis | 🔴 supply exists, no grant | 🔴 supply absent |
| First move | Negotiate a grant, or rebuild `6` **known, specified** artefacts | Localise the `Global` tier — there is nothing to negotiate for |
| Risk | Rebuilding something a client can see already exists | No local reference implementation to validate against |
| Cheapest evidence | The `6` block rows on [`../agents/top.md`](../agents/top.md) | 🔴 An unrun measurement — see the gap below |

🔵 **Scale caveat on both arms, so neither is over-read:** the largest in-language row found
in any region is `19★` ([`lucianoon/llm-course`](https://github.com/lucianoon/llm-course),
Apache-2.0, Portuguese) and three permissive in-language rows sit at `0★`. 🟢 **This is
reference-implementation supply, not dependency supply** — which is exactly why the
licensing question decides whether it is worth anything.

### 🔴 Declared gaps — added `p591`

| Gap | Status | What would close it |
|---|---|---|
| `591-F` 🔴 **The EMEA in-language supply measurement is one axis deep and the conclusion rests on it** | 🆕 Opened `p591` | `Trend 45`'s EMEA arm rests on `2` artefacts found via Spanish/Portuguese-oriented axes plus general topic axes — 🔴 **no pass has ever run EMEA-language free-text discovery.** `p576`'s native-language legs were per-**jurisdiction regulation**, not per-language **supply**. 🟢 Closing it is cheap and specified: free-text `gh api` axes in **German, French, Spanish-of-Spain, Italian, Polish, Dutch, Arabic and Turkish**, with the same `pushed_at ≥ 2026` / `fork:false` filter and byte-read grants. 🔴 **Until that runs, `5.5×` is a floor on the asymmetry, not a measurement of it** — the honest reading is "EMEA supply is thin on every axis tried", not "EMEA supply is `2`". |
| `591-G` 🔴 **Every `(text)` licence mark filed before `p591` is unauditable for the `Trend 43` defect** | 🆕 Opened `p591` | No previous pass published the matcher behind its byte-reads, so none can be checked for body-vs-title misclassification. 🟢 **Cheap partial close:** re-read only the rows at risk — any `(text)` row whose recorded byte size falls outside `~1,050–1,100 B` for a claimed MIT, or outside `~11,340–11,360 B` for a claimed Apache-2.0. 🔵 On this pass's own data that filter would have caught **both** false positives and flagged `~4` rows for a `~3 %` true-positive rate, so the audit is small. 🔴 Not run this pass — `35` new rows were the budget. |

---


## p589 — 2026-11-01 — a gate that cannot run is not a gate, and `Trend 39`'s headline figure does not survive one classifier held constant: the specified axis carries the HIGHEST agent share of the four measured, and the mechanism is tooling decay rather than the absence of a specification

### 🔴 Trend A — a blocking gate suite is worth nothing in the environment that cannot execute it, and this base has been publishing as though it ran

🔴 **Measured this pass, and it is about this repository.** `gate-register-currency`
(`p418`, `Makefile:483`) exists, is in `HOOK_GATES`, and `HOOK_GATES` is invoked by
`ingest/pre-commit`. 🔴 **It has never fired.** `make` and `python3 ingest/*.py` both return
`"Permission … denied … Reason: [Code from External]"` in the environment that writes these
passes — re-tested individually this pass, not only as a batch.

| consequence | measurement |
|---|--:|
| gap ids cited on a curated page, absent from the register *(substring predicate, on arrival)* | 🔴 **`44`** |
| 🔴 **same, with a STRUCTURAL predicate — an id in a registration position** | 🔴 **`120`** |
| of the last `12` committed passes, those with no register entry | 🔴 **`9 of 12`** |
| oldest dangling id | 🔴 **`510-C`** (~`79` passes) |
| controls in `gate-shelf-consistency` alone that have not run | 🔴 **`59`** |

🔵 **The generalisable lesson, which is the trend and not the incident.** A gate's value is
`P(it runs) × P(it catches)`. This base has spent many passes raising the second term —
`59` controls on one gate — and **never measured the first**, which is zero here. `p587`
closed a gap by discovering that an instrument *exists*; existence and execution are
different claims, and only the first was published. 🔴 **`p574` recorded the identical
failure for `p573` (*"committed `841` insertions and wrote neither a register entry nor a
README section"*) and attributed it to the pass rather than to the harness.** Two passes,
`15` apart, same symptom, cause unnamed both times.

🔴 **And the second lesson, which this pass learned on itself.** Its own first replica
counted an id as registered if it appeared **anywhere** in the register file, so a worklist
of unpaid ids read as payment. Tightening the predicate to a **registration position** moved
the answer from `5` to `120`. 🔵 **A gate that measures the wrong relation is worse than a
gate that cannot run, because it reports green.**

🟢 **The cheap fix, demonstrated rather than prescribed.** The register check this pass ran
is **a few lines of `grep`/`awk`** and needs no execution permission at all — it is
published in [`./open-gaps.md`](./open-gaps.md) under the central finding. 🔵 **Any gate
whose predicate is a string relation can be ported to `grep` and will then actually run.**
That is `589-B`.

### 🔴 Trend B — the false-positive rate of an unaudited name-and-description classifier is about a third, and one of its errors is a homonym inside the *classifier* rather than inside the tag

🔴 **Measured by hand-grading every hit this pass produced**, published row-by-row with the
token that fired at
[`../evidence/matcher-hand-audit.2026-11-01-p589.tsv`](../evidence/matcher-hand-audit.2026-11-01-p589.tsv).

| axis | raw hits | false positives | FP rate |
|---|--:|--:|--:|
| `topic:scorm` | `18` | `5` | `27.8 %` |
| `topic:lti` | `5` | `2` | `40.0 %` |
| `topic:gradebook` | `6` | `3` | `50.0 %` |
| 🔴 **all three** | **`29`** | **`10`** | 🔴 **`34.5 %`** |

🔴 **The error classes are systematic, not random.** Three of the ten are *material about
agents* rather than agents — `secure-code-training` ("SCORM training … around agents"),
`Copilot-Chat-Safe-AI-Learning-Path`, `api-evangelist/ispring`. Two are a token in a **name**
with no AI behind it (`scorm-slide-assistant` is a Chrome playback helper). 🔴 **And one is a
homonym the classifier cannot see:** `eloompty/Eloom-LMS-International` advertises *"agents
and certificates"*, where **agents are the human education-recruitment agents of the
admissions trade.** `Trend 40` established that a topic *tag* must be checked for homonyms
before its denominator is quoted; this is the same hazard one layer up, in the matcher.

🔵 **Rule:** a share figure reaches a page with three numbers, never one — raw hits, graded
false positives, and the token that fired. Anything else is an upper bound dressed as a
measurement.

## 41. A specification does not predict whether a layer is built by libraries or by agents — what predicts it is whether the spec is something you must SPEAK or something you must EMIT, and — 🔴 `p590`: NOT whether its tooling is alive, that half is withdrawn — whether the spec BODY still maintains its own (high confidence — pre-registered prediction, falsified on both arms; `545` repositories across four axes, one matcher, every hit hand-graded)

🟢 **This trend exists because a prediction was written down before the measurement and
then failed.** `584-E` asked for exactly that; the pre-registration is committed verbatim at
[`../evidence/prereg-trend39-test.2026-11-01-p589.md`](../evidence/prereg-trend39-test.2026-11-01-p589.md).

**Predicted** (from `Trend 39`): `topic:scorm` is **specified** (SCORM 1.2 / 2004, ADL) →
agent share `≤ 1 %`. `topic:truancy` is **unspecified** → agent share `≥ 5 %`.

**Measured**, one matcher held constant across all four axes, every hit hand-graded:

| axis | spec status | denominator | raw hits | FPs | audited agent share |
|---|---|--:|--:|--:|--:|
| `topic:scorm` | 🟢 **SPECIFIED** | `235` | `18` | `5` | 🔴 **`5.53 %`** |
| `topic:gradebook` | 🔴 unspecified *(control)* | `125` | `6` | `3` | **`2.40 %`** |
| `topic:lti` | 🟢 SPECIFIED *(control)* | `184` | `5` | `2` | **`1.63 %`** |
| `topic:truancy` | 🔴 unspecified | 🔴 **`1`** | `1` | — | 🔴 **unmeasurable** |

🔴 **Both arms of the prediction failed.** `scorm` was predicted at `≤ 1 %` and came in at
`5.53 %` — **`5.5×` over** — and it is **`2.3×` the unspecified control**, so the sign
`Trend 39` predicts is **inverted**. 🔴 **`topic:truancy`, the axis `584-E` named itself, has
one repository on all of GitHub** and cannot carry a share at all: a prescription can name
an axis that does not exist, and the denominator must be read before a prediction is
registered.

🔴 **`Trend 39`'s `41×` is not reproducible under a single matcher.** The widest spread
here, same pass, same matcher, same hand audit, is **`3.4×`** (`scorm` / `lti`) — and that
spread is **between two specified axes**, which spec-status cannot order at all. 🔵
`Trend 39`'s two figures were taken one pass apart; this pass cannot tell whether its own
replica matcher or the original method is at fault, and says so rather than choosing. 🟢
**What survives is the delivery intuition; what is withdrawn is the number.**

🟢 **The mechanism, and it is better than the one it replaces.** Look at *what* the `13`
genuine `scorm` agents are: `edumints-scorm-mcp`, `scorm-mcp-server`, `edumints-scorm-skill`,
`cubite-mcp`, `mcp-learning-server`, `CourseForge`, `elabora-core`, `GenOVA` — almost every
one **emits** SCORM packages. Nothing here *conforms* to SCORM in order to interoperate;
they **produce** it as an output format.

🔵 **A specification plays one of two roles, and they pull in opposite directions:**

| role | what the spec is for | who builds it | education examples |
|---|---|---|---|
| **conformance target** | *speak* it, to interoperate at runtime | 🟢 **libraries** — conformance is deterministic, testable, written once, depended on | LTI 1.3, xAPI |
| **export target** | *emit* it, to hand a deliverable to someone else's system | 🔴 **agents and generators** — the generation is judgement-shaped, only the container is fixed | SCORM 1.2 / 2004 |

🔴 **WITHDRAWN `p590` — the "tooling rotted" half of this trend is REFUTED, and with it the
clause in this trend's own title.** `p589` wrote that the emit-side library tier is dead and
that *"exactly two are alive"*. `589-E` asked for that to be tested on `topic:xapi` and
`topic:qti` before it generalised. 🟢 **It was tested under a
[prediction registered first](../evidence/prereg-589E-spec-tooling-rot.2026-11-01-p590.md),
and it failed on both arms.**

| axis | H1 predicted | 🔴 measured (live permissive emit-side) | verdict |
|---|---|--:|---|
| `topic:xapi` | `<= 2` | **`6`** | 🔴 H1 refuted |
| `topic:qti` | `<= 2` | **`8`** | 🔴 H1 refuted |
| `topic:scorm`, re-walked | `2` (`p589`'s own figure) | 🔴 **`>= 6`** | 🔴 `p589` refuted |

🔴 **The SCORM figure was wrong at source, and its counter-example was `66` lines above it
in the same file.** `numbas/Numbas` (Apache-2.0, `216★`, pushed `2026-10-28`, ships a
`23,811`-byte `runtime/scripts/scorm-storage.js`) is shelved on
[`../repos/foundations.md`](../repos/foundations.md) line `78` as *"the permissive assessment
anchor to build on"*; `LiaScript/LiaScript-Exporter` (BSD-3-Clause, `29★`, pushed
`2026-10-30`) exports **SCORM 1.2 and SCORM 2004** per its own README and was already in
this base's history. 🔵 **`p589`'s row for `Numbas` left `Last push` blank — and an
unmeasured cell cannot refute a claim, which is exactly how the claim survived its own
counter-example.** `584-B`'s failure mode, one pass after `584-B` was registered.

🟢 **What survives, stated narrowly enough to be true.** The dead repositories `p589` listed
are all genuinely dead — `react-scorm-provider` (MIT, `67★`) last pushed `2023-01-06`,
`gamestdio/scorm` (MIT, `38★`) `2019-02-14`, `raccoongang/edx_xblock_scorm` archived, and
🔴 **`adlnet/SCORM-to-xAPI-Wrapper`, published by ADL — the body that authored SCORM — is
unlicensed *and* archived, last pushed `2017`.** 🔵 **So the surviving claim is about
STEWARDSHIP, not about tooling in general: specification bodies abandon their own
reference tooling, while third parties keep shipping it.** That is a sourcing instruction
(*do not depend on the spec author's repo*) and it is supported on all three axes. 🔴 The
general *"a spec's tooling rots"* law is withdrawn: on the same three axes there are `42`,
`35` and `14` live permissive repositories respectively.

🔵 **Delivery rule — this replaces `Trend 39`'s, and it is the sellable half.** Do not ask
*"does this task have a specification?"* Ask **two** questions:

1. **Must I speak it or emit it?** Speak → buy the permissive library, conformance evidence
   matters more than code. Emit → **the generator is the deliverable** and the spec is only
   the container contract.
2. **Is the spec's tooling alive?** Check `pushed_at` and `archived` on the top permissive
   rows *before* quoting a build-vs-buy answer. 🔴 On SCORM the honest answer is
   *"buy `scorm-again` for the runtime, build the generator, and do not depend on anything
   else on this axis"* — because `56.6 %` of the axis (`133 of 235`) carries **no licence at
   all**.

🔴 **Falsifier, stated so the next pass can kill this too:** an export-target spec whose
permissive tooling is maintained *and* whose agent share is low, or a conformance-target
spec with high agent share once its libraries have rotted. `589-E` prescribes the test —
`topic:xapi` and `topic:qti`, where the roles differ and the decay may not.


## 42. A liveness count cannot tell an ecosystem from one person's week — the number that can is live repos ÷ distinct owners, and on one of education's three interchange specs it is 2.0 (high confidence — `567` repositories across three axes walked to exhaustion, owners counted, `2026-11-01`)

🟢 **Measured, same sweep, same matcher, three axes walked to exhaustion.** The first four
columns are the ones this base has always published. 🆕 **The fifth is the one that changes
a decision.**

| axis | repos | permissive | live permissive, non-archived | 🆕 distinct owners | 🆕 **live ÷ owners** |
|---|--:|--:|--:|--:|--:|
| `topic:scorm` | `235` | `78` | `42` | 🟢 `39` | 🟢 **`1.08`** |
| `topic:xapi` | `280` | `125` | `35` | 🟢 `27` | 🟢 **`1.30`** |
| `topic:qti` | `52` | `23` | `14` | 🔴 **`7`** | 🔴 **`2.00`** |

🔴 **QTI's apparent health is one account.** `8` of its `14` live permissive repositories
belong to **`metyatech`** — `markdown-to-qti`, `apply-to-qti-results`,
`tracklms-to-qti-results`, `roster-to-qti-results`, `qti-xml-core`, `qti-scoring-system`,
`qti-reporter`, `qti-html-renderer` — **all pushed inside a six-day window in September
`2026`, none above `2★`.** 🔵 Remove that one owner and the axis has `6` live permissive
repositories from `6` owners, which is a different procurement fact entirely.

🔵 **Why `liveness` alone misleads, mechanically.** A single prolific publisher produces the
same `pushed_at` distribution as a healthy community: recent dates, plural repositories,
permissive licences. 🔴 **Every signal this base grades on is satisfied by one person
having a productive week.** The owner count is the cheapest available discriminator and it
costs nothing — it is a `split` and a `sort -u` over data the sweep already fetched.

🟢 **Delivery rule.** Before an engagement takes a dependency on an interchange layer, ask
**who** maintains it, not just **when** it was last touched:

- 🟢 **`live ÷ owners` near `1.0`** → a real ecosystem; a dead dependency can be swapped.
- 🔴 **`live ÷ owners` at `2.0` or above, or one owner holding `> 50 %`** → a
  single-maintainer dependency dressed as an ecosystem. Vendor the code, budget for taking
  it over, or speak the spec directly and skip the libraries.
- 🔵 **For QTI specifically:** `feyst/qti3-validator` and `Citolab/qti-playground` are the
  two live permissive QTI rows from owners other than `metyatech` that a studio can
  reasonably stand on; treat the `metyatech` set as one supplier, not eight options.

🔴 **This trend also constrains this base's own history.** Every axis table published before
`p590` carries liveness without owners, so none of them distinguishes these two cases.
🔵 **Standing prescription: no axis table reaches a page without a distinct-owner column.**

---

## p588 — 2026-11-01 — the defect class with no instrument is TAXONOMY, not licence; `pushed_at` overstates liveness and every staleness verdict in this base inherits that; and the education-specific licence shape is a CONTENT carve-out inside a permissive CODE grant

### 🔴 Trend A — a knowledge base's inclusion rule drifts silently, and every gate it owns is blind to it

This base runs a blocking gate suite over **licences**, **numeric claims** and **cross-page
token agreement**. Measured this pass: **not one of them can detect that a row does not
belong on the page it is on.**

The specimen is `p587`'s own. [`../intel/open-gaps.md`](../intel/open-gaps.md) retired a
whole discovery query on the finding that *"in a trending feed 'education' means teaching
people about AI, not AI for teaching"* and named
[`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
as a specimen of the class to exclude. `p587` then shelved that exact repository as **the
second-largest row on [`../agents/top.md`](../agents/top.md)**. Both pages passed every
gate, because every gate asks *"is this licence right?"* and none asks *"is this the same
kind of thing as its neighbours?"*

| | before `p588` | after |
|---|---|--:|
| members of the *learning-about-AI* class on a curated page | **2** | **8** |
| of the class's five largest members, how many were filed | **1 of 5** | **5 of 5** |
| pages asserting the class is out of family | **1** (`open-gaps.md`) | **1 — still open** |

🟢 **The generalisable claim.** A base that measures its *facts* and never its *categories*
accumulates taxonomy debt invisibly, and taxonomy debt is the kind a **client** notices
first: a shelf that mixes "an agent that tutors a student" with "a curriculum that teaches
an engineer" cannot be handed to anyone without a sentence of explanation, and that
sentence was never written. 🔴 **Confidence: high — measured on this base, one specimen
class, two contradicting pages, both passing all gates.** 🔵 **What would instrument it: a
gate that requires every shelf row to declare a `class`, and fails when a page holds more
than one undeclared class.**

### 🔴 Trend B — `pushed_at` is not "last commit", and every staleness verdict on these pages inherits the error

This base marks rows 🟡 and 🔴 for staleness off the API's `pushed_at`. Measured against the
default-branch commit feed (`https://github.com/{repo}/commits/{branch}.atom`):

| Repo | API `pushed_at` | default-branch feed | gap |
|---|---|---|--:|
| [apache/openmeetings](https://github.com/apache/openmeetings) | `2026-11-01` | `2026-10-26` | 🔴 **6 days** |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | `2026-10-30` | `2026-10-30` | 🟢 0 |
| [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | `2026-10-27` | `2026-10-27` | 🟢 0 |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | `2026-07-27` | `2026-07-27` | 🟢 0 |

🔴 **The error is one-directional.** `pushed_at` records a push to *any* ref — a tag, a
release branch, a bot branch — so it can only ever be **newer** than the default branch's
last commit, never older. 🟢 **Every "last push" column in this base is therefore an
upper bound, and the 🟡/🔴 staleness marks are optimistic by an unknown margin.** 🔵 **The
margin was 0 in 3 of 4 probes, so this is a tail risk, not a systematic bias** — but the
tail is exactly where a "pushed today" row turns out to be a tag on dormant code.
🟢 **Operational rule: for any row a studio would actually fork, read the feed.**
🔴 **Confidence: high for the mechanism, low for the rate — `n=4`.**

### 🟡 Trend C — education's licence shape is a CONTENT carve-out inside a permissive CODE grant, and it appears at the very top of the size distribution

[`rasbt/LLMs-from-scratch`](https://github.com/rasbt/LLMs-from-scratch) — **107,625★**, the
second-largest education-adjacent repository on GitHub — ships Apache-2.0 text whose
definition of **"Source" is modified** to exclude *"any books specific to this software and
any related images"*. 🔴 **Neither channel alone shows it:** GitHub's API says
`NOASSERTION`, and the file says "Apache License, Version 2.0" in its first line. Only
reading the *body* of the grant finds the carve-out.

It is not a one-off. Collected across this base:

| Repo | Grant | What is carved out of it |
|---|---|---|
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 🟡 Apache-2.0 (modified) | 🆕 the **books and images** |
| [aaryansamanta/nextgen-ai](https://github.com/aaryansamanta/nextgen-ai) | 🟡 "MIT License (Code)" | the **curriculum content** |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 ODbL-1.0 | it is a **data** licence; share-alike on derived databases |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | 🟡 Creative Commons | it is a **content** licence on software; no patent grant |
| [ARUNAGIRINATHAN-K/awesome-ai-agents-2026](https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026) | 🟡 CC0-1.0 | 🆕 public-domain dedication for **content**, not a software licence |

🟢 **The claim, and it is specific to this industry: in education the content *is* the
product, so publishers grant the code and withhold the material.** In a technology or
infrastructure base the licence question is "may we ship this binary?"; here it is **"may we
ship the lesson?"** — and the answer is routinely different from the answer about the code
sitting beside it. 🔴 **The commercial consequence is direct.** A deliverable that reuses a
client-facing *course*, *textbook*, *item bank* or *taxonomy* needs its grant checked
separately from the repository that carries it, and an SOW drafted off the repository's
licence badge will be wrong about the part the client actually paid for.
🔵 **Confidence: high — five specimens, every grant read first-hand, spanning `107,625★` to
`353★`.** 🟢 **It extends `p587`'s split-grant trend rather than repeating it:** `p587`
measured grants that split *by directory*; this is a grant that splits **by kind of
work**, and no SPDX identifier can express it.

### 🔵 Two smaller results, recorded without a trend number

🔴 **The secondary-source licence error rate this pass was `2 of 4`, both in the dangerous
direction.** A comparison article described [`frappe/lms`](https://github.com/frappe/lms) as
*"MIT (no restrictions)"* — it is **AGPL-3.0** — and asserted `OpenOLAT` as Apache-2.0 with
no verification. 🟢 This base was right on both. 🔵 It extends `p586`'s *Trend 4* (licence
metadata as a sourcing risk) to a channel that matters differently: **the API misleads this
base, but comparison articles mislead the client's own team**, and they arrive in the
engagement as "we read that this is MIT".

🔴 **The intel channel is saturated at `20 of 24`.** `83 %` of everything six regional legs
returned this pass was already filed, and **none of the remaining four is verifiable from
this environment** — `7 of 7` non-GitHub hosts returned no connection. See
[`./market.md`](./market.md) `p588` and `588-B`. 🟢 **The honest reading is a scheduling
one: education's intel pages have reached the ceiling of this channel, while the GitHub
channel still pays** — this pass added six rows there from it.

---

## p587 — 2026-11-01 — the split grant is a class, not an anomaly; the data licence arrives in an education repo big enough to matter; and the discovery/promotion asymmetry is now a measured property of this base rather than a complaint

### 🔴 Trend A — the split grant is a CLASS, and a one-value licence field cannot represent it

**The measurement.** This base now holds **two** confirmed split-grant repositories, both
measured from licence text:

| Repo | Stars | The split |
|---|--:|---|
| [andymatuschak/orbit](https://github.com/andymatuschak/orbit) | 1,838 | Apache-2.0 everywhere **except** `packages/app` + `packages/backend` → **AGPL-3.0-or-later *or* BUSL-1.1** at the licensee's choice. 🔴 BUSL-1.1 is not an open-source licence. |
| 🆕 [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | 527 | **AGPL-3.0** for the Community Edition; **AGPL-3.0 for all client-side JavaScript** *however served or compiled*; `apps/prairielearn/src/ee/` is a **proprietary Enterprise Edition**; **MIT** only for portions copyright UIUC and outside contributors. |

**Why it is a trend and not a coincidence.** Both are the same commercial shape: permissive
at the library edges, copyleft-or-closed exactly where the product is. That is the standard
open-core defence against a vendor reselling the product, and education software — sold to
institutions with procurement departments — is where it should be expected.

🔵 **The consequence for this base is structural, not editorial:** every shelf here has one
licence column, and a one-value field **cannot express "Apache-2.0 except two directories"**.
`p585` found this for `orbit` and `p586` reconciled it in prose. With a second instance the
prose workaround stops scaling: a *split-grant* flag belongs in the schema. Registered as
part of `587-E`.

### 🟡 Trend B — the licence vocabulary meets a DATA licence, in a 7,489★ education-relevant repo

[`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) — **7,489★**,
pushed `2026-10-30`, an open skills/occupation taxonomy — is **ODbL-1.0**: the Open Database
License. 🔴 **Every grading rule in this base assumes the token governs code.** ODbL
governs a *database*: share-alike attaches to **derived databases**, with a separate
*produced work* clause for things built from it.

**Why it matters commercially.** Competency mapping, course-to-job alignment and reskilling
paths are what a corporate-learning client actually buys, and the taxonomy is the spine of
all three. 🟢 A product built **on** the data is a produced work; 🔴 publishing an
*enriched taxonomy* means publishing the enrichment. **That is a counsel question, and the
answer is different from the answer for code** — which is precisely why grading it with a
code rule would be wrong in either direction.

🔵 This base already holds two **content**-grant anomalies alongside it — `nextgen-ai`'s
licence file reads *"MIT License (Code)"* with the content grant unstated, and `gen-mentor`
is CC0-1.0. Three rows, three grant *kinds*, one column.

### 🔴 Trend C — this base's constraint is promotion, not discovery, and the rank has no signal

**The measurement** (`p587`, scope: two append-only logs vs seven curated pages): **3,483**
discovered addresses, **679** curated, **2,841 (81.6 %) never filed**. 🔴 **Three passes
have now measured this** — `p539` at `4,144 / 240`, `p585` at `3,094 / 3,415`, this pass at
`2,841 / 3,483` — on different scopes, with the same conclusion.

🟢 **What `p587` adds is that the obvious fix does not work.** Ranking the backlog by
re-find count puts, in its top thirteen: two MIT repos at **76,141★** and **78,542★**
(genuine finds, filed this pass), **two addresses that do not exist**, **three with no
licence grant**, and one with **zero stars after eighteen sightings**. A recall count
cannot tell a 78,000★ repository from a dead address.

🔵 **The trend statement, then, is narrow and testable:** the supply constraint in an
open-source intelligence base of this age is not finding addresses, it is **grading** them —
and the three inputs needed to grade (grant, liveness, size) arrive free in the same API row
that confirms the address exists. `p533` specified this; `p587` is the evidence that nothing
cheaper will do.

### 🟢 Trend D — APAC can adopt in its own language; LATAM cannot. Measured, with a control.

Iberian-language education-AI repositories above 10★: **2**, neither adoptable. Chinese
language, same instrument, same hour: **67**. A ~**33×** asymmetry.

**Why this is a trend and not a search artefact.** It is consistent with what is already on
this base's shelves: the APAC rows (`DeepTutor`, `OpenMAIC`, `cn-math-taxonomy`,
`kaogong-skill`, `cram-engine`) are in-language, origin-placed and maintained, while the
LATAM rows are localisations. 🔵 **The delivery consequence is a line item:** an APAC
engagement can start from an in-language asset; a LATAM engagement pays for localisation or
a build. Full figures in the `p587` section of [`./market.md`](./market.md).

---

## p586 — 2026-11-01 — the unit of shipping changed from the application to the *skill*, and the regulated surface in education AI is now assessment, not tutoring

### 🟢 Trend 1 — education AI ships as an agent skill, not an application

**The measurement.** Of the 38 verified rows on [`../agents/top.md`](../agents/top.md),
**eleven are skills or MCP servers that run inside a host agent** rather than deployable
applications: `Papermorph`, `claudemy`, `universal-examprep-skill`,
`universal-diagnostic-tutor-skill`, `kaogong-skill`, `cram-engine`, `algo-sensei`,
`tutor-mcp`, `anki-mcp-server`, `canvas-mcp`, `libro-3d-interactivo`. Six of the eleven
were **discovered this pass**, and the category barely existed in this base's earlier
narrative.

🟢 **Why it is commercially material.** A skill has **no hosting, no auth, no UI and no
upgrade path**. The integration cost of adopting one is days rather than the weeks a
platform costs, so the *adopt-vs-build* line in an education engagement has moved
measurably toward **adopt**.

🔴 **And the risk moved the other way, which is the part a proposal must say out loud.** A
skill inherits the host agent's **model, data path and tenancy**. The data-residency
question that a self-hosted platform answers *structurally* becomes a **contract** question
instead. For an EU Annex III high-risk deployment or a LATAM public-sector engagement, that
is the harder answer, not the easier one.

🟢 **Which is why the smallest rows matter most here.**
[`wordlink`](https://github.com/orionsheep/wordlink) (MIT, 266★) ships a **fine-tuned 1.5B
model (SFT+DPO) that runs offline**, and [`Open TutorAI CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(BSD-3) runs local LLMs via Ollama. They are the two shelf rows that answer residency
without a contract clause. **Star count is the wrong way to rank a shelf against a
regulatory constraint.**

### 🟢 Trend 2 — the regulated surface is assessment, and tutoring is comparatively free

Three regions converged on the same line this pass, from different legal traditions:

| Region | Instrument | What it regulates |
|---|---|---|
| **Vietnam** | Decision **33/2026/QD-TTg** | Names education among six high-risk sectors, citing **automated assessment** explicitly |
| **South Korea** | **AI Basic Act** (in force 22 Jan 2026) | High-impact AI: **transparency and human oversight** duties |
| **United States (DC)** | 2026-27 district policy | **Bars** AI from **grading, discipline, IEP decisions, teacher evaluation** |
| **Australia** | **TEQSA** | Higher-ed providers must file **generative-AI risk action plans** |

🟢 **The pattern: judging a learner is regulated; helping a learner is not.** Tutoring,
content generation, practice and feedback-for-the-learner sit largely outside these
instruments. Grading, progression decisions, proctoring and anything feeding a personnel or
disciplinary record sit inside them.

🟢 **So the sellable work is the oversight layer around assessment, not the assessment.**
That makes the psychometric tier — [`catsim`](https://github.com/douglasrizzo/catsim)
(BSD-3), [`pyKT`](https://github.com/pykt-team/pykt-toolkit) (MIT),
[`nbgrader`](https://github.com/jupyter/nbgrader) (BSD-3),
[`Numbas`](https://github.com/numbas/Numbas) (Apache-2.0) — a **compliance requirement
rather than an academic nicety**, and all four are permissive.

🔴 **The gap this exposes.** There is still **no permissive proctoring platform**:
`Proctoring-AI` (MIT, 633★) is a component last pushed `2024-12-10` (~23 months), and
`SafeExamBrowser` (361★, current) is **MPL-2.0**. The most heavily regulated surface in the
industry has no permissive platform to build on. Gaps `585-B`/`585-G`.

### 🟢 Trend 3 — generation moved up a layer: from question generation to whole courseware

`p585` recorded that the fine-tuned T5 **question-generation** tier is dead — absorbed by
instruction-following models, every reference repo last pushed 2023–2024. `p586` found what
replaced it, and it is not a better question generator:

| Repo | Licence | Stars | Output |
|---|---|--:|---|
| [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) | 🟢 MIT (text) | **71,803** | **Native** PPTX — real shapes, transitions, charts, narration |
| [`assafkip/claudemy`](https://github.com/assafkip/claudemy) | 🟢 MIT (text) | 574 | A researched course from a bare topic |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | 🟢 MIT (text) | 1,040 | A book as an animated, narrated, interactive experience |
| [`Fazmin/AILearningGuide`](https://github.com/Fazmin/AILearningGuide) | 🟢 MIT | 242 | 51 hands-on labs as a shipped curriculum |

🟢 **The unit of generation is now the artefact a teacher actually hands over** — a deck, a
course, a lab sequence — not an item in a question bank. `ppt-master` at **71,803 stars**
makes this the largest single pool of adoptable permissive code in or adjacent to this
industry, and it is **not education-specific**, which is precisely why a base searching for
"education" repos missed it for twenty passes.

### 🔴 Trend 4 — the quality of licence *metadata* is now a sourcing risk in its own right

🔴 **`NOASSERTION` is not a proxy for "probably permissive".** `p585` recovered six blank
API licence fields and most resolved permissive, which invited that inference. `p586`
refutes it:

| Row | API | Licence file | Direction |
|---|---|---|---|
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) (587★) | `NOASSERTION` | 🔴 **AGPL-3.0** | 🔴 Against |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (903★) | `NOASSERTION` | 🟡 **LGPL-3.0** | 🟡 Weak copyleft |
| [`aaryansamanta/nextgen-ai`](https://github.com/aaryansamanta/nextgen-ai) (492★) | `NOASSERTION` | 🟡 **MIT — code only** | 🟡 Partial |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (449★) | `NOASSERTION` | 🟢 **Apache-2.0** | 🟢 For |
| [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) (498★) | *none* | 🔴 **no file, 6 paths** | 🔴 No grant |

🔴 **A blank field is an unknown, and unknowns resolve in both directions.** `ai-ethos` is
the row to remember: a 501(c)(3) nonprofit, 498 stars, multilingual tutoring aimed at
underserved learners, and **no licence at all**. Reach and good intentions do not create a
grant.

🔴 **And a single-value licence field cannot represent the truth for some repositories.**
[`andymatuschak/orbit`](https://github.com/andymatuschak/orbit) (1,838★) is **Apache-2.0
for most sources but AGPL-3.0-or-later *or* BUSL-1.1 for `packages/app` and
`packages/backend`** — and **BUSL-1.1 is not an open-source licence**. Its libraries are
buildable; its app and backend are not shippable.

### 🔴 Trend 5 — whole niches are copyleft-locked, and language learning is the clearest

| Niche | Largest option | Licence | Verdict |
|---|---|---|---|
| Language learning (general) | [`LibreLingo`](https://github.com/kantord/LibreLingo) 2,631★ | 🔴 AGPL-3.0 | 🔴 **ARCHIVED** `2026-11-01` |
| Language learning (general) | [`artcc/freelingo`](https://github.com/artcc/freelingo) 222★ | 🔴 **AGPL-3.0 (text)** | 🆕 Live successor — and copyleft |
| Vocabulary only | [`word-atlas`](https://github.com/designfuchen/word-atlas) 3,604★ | 🟢 MIT (text) | 🟢 Permissive, **narrow scope** |
| Tutoring (2nd largest) | [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) 1,317★ | 🔴 AGPL-3.0 | 🔴 Also ~10 months stale |
| Education ERP / SIS | `openeducat_erp` 903★ / `frappe/education` 688★ / `rosariosis` 649★ | 🔴 LGPL-3.0 / GPL-3.0 / GPL-2.0 | 🔴 **No permissive option at any size** |

🟢 **The one that is survivable, and why.** `openeducat_erp`'s **LGPL-3.0 is weak
copyleft**: a separate module calling its API keeps its own licence, and because OpenEduCat
is built as **Odoo modules**, that side-car is the platform's standard extension pattern.
🔴 **Language learning has no equivalent escape** — AGPL-3.0 is network copyleft with no
module boundary, so a language engagement either accepts AGPL or composes `word-atlas` +
`wordlink` + [`OpenPronounce`](https://github.com/Halleck45/OpenPronounce) (MIT) over FSRS
scheduling, which is a **BUILD**. Gap `586-C`.

### 🟢 Trend 6 — adoption is universal, governance is not, and the gap *is* the market

| Region | Adoption | Governance |
|---|---|---|
| **LATAM** | 92% students, 79% faculty, 87% of institutions use AI in ≥1 area | 🔴 Driven by faculty and students, **not** institutional policy; only **Brazil and Colombia** budget for it nationally |
| **North America** | ~60% of teachers, ~86% of higher-ed students | 🔴 **55% of high-school principals** say AI is *not* blocked or restricted; 134 bills in 31 states racing to catch up |
| **EMEA** | ~70% of institutions have or are developing guidance | 🔴 EU AI Act high-risk date **contested across EU sources, 16-month spread** |
| **APAC** | China, India, Japan lead; fastest-growing region | 🟢 **The most binding education-specific law** — Korea in force, Vietnam naming automated assessment |

🟢 **Nobody needs to be sold AI in education any more.** Every region reports adoption
ahead of policy, which is why the durable offer is **governance, assurance and
enablement** rather than tooling — and why the specificity of the US prohibited-use lists
and Vietnam's high-risk classification are *assets* to an engagement, not obstacles: they
make scope auditable.

---

## p585 — 2026-11-01 — the licence field was the wrong thing to distrust: the base was publishing *contradictory* licences for the same repository, and a split-licence repo is invisible to any single-value field

🟢 **New instrument, controlled, and it changes what this base can assert.** Licences are
now read from the repository's own licence file via
`raw.githubusercontent.com/{repo}/{default_branch}/{LICENSE}`, which is the only ground
truth available in this environment. Controls: real repo + real file → `200` and the licence
text; real repo + absent file → `404`; repo that does not exist → `404`; and
`github.com/...` HTML → `403` for everything, real or fabricated.

### 🔴 Trend 37 — the licence *contradiction* rate, not the licence *unknown* rate, is the defect

This base has recorded for several passes that the GitHub API's `license.spdx_id` is
unreliable (`67 of 265` rows returning `NONE`/`NOASSERTION`). 🔴 **That framing understated
the problem.** The failure found this pass is worse than a missing value:

| row | `repos/foundations.md` carried | `verticals/solutions.md` + `intel/trends.md` carried | licence text says |
|---|---|---|---|
| `OpenOLAT/OpenOLAT` | 🔴 `NOASSERTION` | 🟢 `Apache-2.0` | 🟢 **`Apache-2.0`** |

🔴 **Both verdicts were published simultaneously, for multiple passes, on curated pages of
the same knowledge base.** A per-page licence field with no reconciliation step produces
this indefinitely and nothing in the pipeline detects it. 🟢 **The fix is structural, not
editorial:** a licence belongs to a repository, not to a page, and must be resolved once
from bytes and referenced everywhere.

### 🔴 Trend 38 — a single-value licence field cannot represent a real repository

`andymatuschak/orbit` (1,838★) resolved this pass, and its grant cannot be written in one
field. Its licence file states: all sources **Apache-2.0**, *except* `packages/app` and
`packages/backend`, which are **AGPL-3.0-or-later _or_ BUSL-1.1 at the licensee's choice**.

🔴 **BUSL-1.1 is not an open-source licence** — it is source-available with a time-delayed
conversion. So the correct verdict is **"libraries buildable, application not shippable"**,
which no `spdx_id` can express, and which the API reported as plain `NOASSERTION`.
🟢 **Consequence for this base:** any row whose licence matters at component granularity
needs a *scope* alongside the identifier. Six rows recovered from `NOASSERTION` this pass
(OpenOLAT, relate, pupilfirst, Claroline, INGInious, frappe/education) were all whole-repo
grants; `orbit` is the counterexample that shows the field shape is wrong.

### 🔴 Trend 39 — the probe path is case-sensitive and the default branch is frequently neither `main` nor `master`

`frappe/education` returned "no licence file" against nine filenames across `main` and
`master`. Its grant is at **`develop/license.txt`** — lowercase filename, third branch
name. 🔴 **A `404` from the raw channel means "not at this path", never "no licence" and
never "no repository."** 🟢 The resolver must take `default_branch` from the same
`search/repositories` call that confirms existence, then probe case variants. Without that,
the channel manufactures false no-grant verdicts — the most expensive error class this base
makes, because a no-grant verdict blocks a row permanently.

### 🟢 Trend 36 withdrawal, now propagated

`Trend 36` (*"every platform of record is copyleft without exception"*) was refuted at
`p584` by `sakaiproject/sakai` (ECL-2.0). 🔴 **The withdrawal did not propagate:** the claim
was still published as live fact in **four** places on three curated pages
(`verticals/solutions.md` ×2, `compose/patterns.md`, `intel/trends.md` ×2) while being
marked withdrawn elsewhere. All four are now corrected in place.

🟢 **And the refutation is stronger than one counterexample.** Four platforms of record are
permissive, each read from its own licence file this pass: **Sakai** (ECL-2.0, 1,240★),
**OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★), **relate** (MIT, 437★).
🔵 **The surviving, defensible form of the trend:** *the agent layer is overwhelmingly
permissive (26 of 27 rows), the platform layer is predominantly copyleft but has four
forkable exceptions, and the component/extension layer is almost entirely permissive.*

### 🔴 Trend 40 — this base's discovery rate vastly exceeds its filing rate

Measured first-hand on the repository this pass:

| population | addresses |
|---|--:|
| on a curated page (`top`, `foundations`, `solutions`, `market`, `trends`, `patterns`) | **352** |
| in the append-only trending history | **3,415** |
| 🔴 **in trending history and never on any curated page** | **3,094** |

🔴 **~90% of everything this base has ever discovered sits only in append-only logs.** The
discovery machinery works; the filing step does not exist. `p584` measured this on one tier
and found `FILED = 0`; this is the whole-base figure. 🟢 **The useful consequence: for this
industry, further discovery has low marginal value and filing has high marginal value.**
Every candidate from four fresh topic sweeps this pass was already somewhere in the base.


## p584 — 2026-11-01 — **a trend filed one pass ago is withdrawn by a row that was already on the shelf below it, `583-F` is refuted at `41×`, and three trends are filed at the counter's form**

🔴 **`Trend 36` is withdrawn and restated.** Filed by `p583`, it claimed the education
platform tier is *"copyleft without exception"* and supplied its own falsifier: a
maintained permissive platform of record above `1,000★`. 🔴 **That falsifier was already
satisfied by `sakaiproject/sakai` — ECL-2.0 (byte-read `11,120 B`), `1,240★`, pushed
`2026-10-30` — which `repos/foundations.md` has been describing as a permissive platform
seat, with ECL-2.0 correctly identified as an Apache-2.0 derivative, on the same page.**
🟢 Restated below as `Trend 36` (revised) and generalised as `Trend 38`.

🟢 **`583-G` satisfied:** all three trends below are filed at the counter's `^## <n>. `
form, so the derived count includes them. The series now ends at **`40`**.

## 38. The cheapest refutation of a published superlative is the base's own shelf, not the search channel — and a prescription that says "re-measure against search" will systematically miss the refutations that are already in hand (high confidence — measured first-hand, three claims, two channels)

🔵 **`583-B` prescribed re-measuring `50`+ superlative claims *"against the search
channel."*** This pass audited three claims and the result splits cleanly by channel:

| claim | channel that settled it | cost | verdict |
|---|---|--:|---|
| *"every platform of record is copyleft without exception"* (`Trend 36`) | 🟢 **`grep` of this base's own curated pages** | **one command** | 🔴 **REFUTED** — Sakai, ECL-2.0, `1,240★`, already shelved |
| *"no permissive, maintained, framework-independent LTI 1.3 library for Python"* | 🟡 search, then **licence-text provenance** | 4 queries + 3 byte-reads | 🟢 **STANDS** — the one candidate is a detached copy of the dead upstream |
| *"no permissive Moodle→LRS event bridge"* | 🟡 search | 4 queries | 🟢 **STANDS** — all GPL-3.0 or unlicensed |

🔴 **The one claim that fell, fell to `grep`.** The two that survived needed the search
channel, and survived it. 🟢 **So the audit has a cheap first stage that `583-B` omitted:
check whether the base already shelves a counterexample, *before* spending any search
budget.** A superlative is a claim about a population, and this base's own shelves are the
part of that population it is already holding — and the part it is most likely to have
forgotten, because `Trend 16` says findings do not propagate from history to shelf. 🔵 **This
pass adds the sharper form: they also fail to propagate from one shelf to another.** The
Sakai row and the trend denying it sat in the same repository, `158` lines apart, both
written by passes of this base.

🟢 **Operational rule, replacing `583-B`'s prescription:** for each superlative, (1) `grep`
the curated pages for the claim's own subject vocabulary and check every hit against every
clause of the claim; (2) only then query the search channel. **Stage (1) is free and it
caught the only false claim of the three.**

🔴 **Falsifier:** a superlative refuted by search that could not have been refuted from the
shelves — i.e. a case where stage (1) was genuinely wasted effort. None found in three
audits, but three is a small sample and this trend should be re-tested at `10`.

## 39. Agent-shaped open-source supply appears where the layer has no wire standard to conform to, and collapses to libraries where one exists — so "is this a build or a buy?" is answered by asking whether the task has a spec (high confidence — `1,124` repositories across eight axes, denominators first-hand)

🟢 **Measured, two layers, same method, one pass apart:**

| layer | axes | repositories | agent-shaped | share |
|---|---|--:|--:|--:|
| assessment interchange (`lti`, `lti-provider`, `xapi`, `qti`) | 4 | `538` | **`1`** | **`0.19 %`** |
| school operations (`sis`, `student-information-system`, `gradebook`, `proctoring`) | 4 | `586` (`483` education-relevant) | **`38`** | **`7.9 %`** |

🔴 **A `41×` difference between two layers of the same industry, measured the same way.**
`583-F` was right to demand the test before generalising: *"assessment interchange is a
library tier and the agent is always the build"* is true, and **does not generalise one
layer sideways.**

🟢 **The mechanism, which is what makes this a trend rather than two numbers.** The
interchange layer has **specifications** — LTI 1.3, xAPI, QTI 3.0 — and a specification
makes conformance the whole job. Conformance is deterministic, testable and shared, so it
is written once as a library and depended on. **School operations have no spec**: what
"detect that this student is cheating", "flag an at-risk gradebook pattern" or "reconcile
an enrolment exception" means is institution-specific, unformalised, and judgement-shaped —
which is exactly the shape an agent fits.

🔵 **Delivery rule, and it is the most directly sellable thing in this pass:** **ask whether
the task has a published specification.** If it does, **buy the glue permissively and do not
build it** — the library exists and conformance evidence matters more than code. If it does
not, **the agent is the deliverable**, and the open-source supply will be numerous, tiny,
and mostly unlicensed, so it is reference architecture rather than dependency. 🔴 **The
proctoring axis proves the second half: `150` repositories, the most agent-shaped of the
eight axes, and the credible artefacts (`MyProctor.ai` at `236★`, `GodsEye`, the five-agent
invigilation system) carry no licence at all.** `7.9 %` agent-shaped is not `7.9 %`
shippable.

🔴 **Falsifier:** a specified layer with abundant agent supply, or an unspecified
operational layer whose supply is predominantly libraries. `topic:iep` (`7★` ceiling,
`p575`) is a weak confirming case — unspecified and with almost no supply of either kind —
and should be re-read as a third point.

## 40. An acronym topic axis must be measured for homonyms before its denominator is quoted, and the long form of a tag can be both cleaner AND larger than the short form (high confidence — measured first-hand, `321` rows across one tag pair)

🟢 **Measured:**

| axis | repositories | education-relevant | pollution |
|---|--:|--:|--:|
| `topic:sis` | `141` | `64` | 🔴 **`77` (`55 %`)** |
| `topic:student-information-system` | `180` | **`180`** | 🟢 **`0`** |

🔴 **`55 %` of `topic:sis` is not education at all** — *Sovereign Intelligence System*,
*Starlight Intelligence System*, **Safety Instrumented System** (industrial AI safety
testing), epidemic simulation on networks, and a NetLogo social model. Had the raw
denominator been quoted, `141` would have entered this base as education supply and `77` of
those rows are a different industry wearing the same three letters.

🔵 **`Trend 17` of this base states that tag variants split a capability's population *and
the short form is the empty one*.** 🟢 **This is a different failure and the opposite
shape: the short form is neither empty nor smaller — it is polluted, and the long form is
simultaneously clean and `28 %` larger.** The two trends are compatible; what they share is
that **a tag is not a population and must be measured before it is counted.**

🟢 **Rule: when an axis is an acronym, measure its education-relevance share first and quote
the filtered denominator, naming the filter.** 🔵 Every denominator this pass published for
`sis` and `proctoring` is the filtered one, with the raw figure shown beside it.

🔴 **Falsifier:** an acronym axis whose pollution is negligible, or a spelled-out variant
that is dirtier than its acronym. `topic:gradebook` (`0 %` pollution, `125` rows) shows a
non-acronym axis can be clean; the pair to test next is `topic:lrs` against
`topic:learning-record-store`.

## 36. (REVISED `p584`) The licence shape of open-source education is a property of the LAYER, not of the industry — and the platform tier is copyleft with exactly ONE permissive exception, licensed under education's own licence (high confidence — revised after refutation; `13` platform rows above `1,000★` on five axes, every grant byte-read)

🔴 **The original form of this trend said the platform tier is "copyleft without
exception". That is false and is withdrawn.** The gradient it describes is real; the
universal was not.

🟢 **The platform tier above `1,000★`, measured on five axes this pass:**

| grant | rows | note |
|---|--:|---|
| 🔴 AGPL-3.0 | `6` | `frappe/lms` · `learnhouse` · `classroomio` · `courselit` · `overhangio/tutor` · `hrshadhin/school-management-system` |
| 🔴 GPL-3.0 | `3` | `Unifiedtransform` · `chamilo/chamilo-lms` · +1 |
| 🔴 GPL-2.0 | `1` | `course-tencent-cloud` |
| 🟢 **ECL-2.0 — permissive** | **`1`** | **`sakaiproject/sakai`, `1,240★`, `2026-10-30`** |
| 🟡 MIT | `2` | `SWE-agent` (not education — `Trend 29`) · `4jean/lav_sms` (`1,161★`, 🔴 cold `2024-03-06`) |

🟢 **The gradient stands and is now exact: permissive at the wire protocol (`66.7 %` across
`33` integration rows), copyleft at the platform `6` times in `7`, and the seventh is
Sakai under ECL-2.0** — the Educational Community License, an Apache-2.0 derivative written
for this sector by Apereo. 🔵 **Delivery rule, corrected:** *ship the glue; do not ship a
modified platform — unless the platform is Sakai, which is the one you may fork.*
🔴 **And the nearest MIT near-miss is a fork-and-adopt candidate, not a dependency:**
`4jean/lav_sms`, MIT, `1,161★`, cold `2024-03-06` — it fails the recency clause only.

🔴 **Revised falsifier:** a **second** permissive platform of record above `1,000★`, pushed
within a year. One exists; a second would make "exception" the wrong word and turn this
into a genuine split.

## Declared gaps — updated `2026-11-01` (`p584`)

- 🔴 **WITHDRAWN: "every platform of record is copyleft without exception"** (`Trend 36`,
  filed `p583`). Refuted by `sakaiproject/sakai` (ECL-2.0, `1,240★`, `2026-10-30`), which
  was **already on `repos/foundations.md`**. 🟢 **Reshaped: copyleft `6` times in `7`, with
  Sakai the one forkable platform of record.**
- 🔴 **WITHDRAWN: `583-F`'s generalisation** that education integration is a library tier
  where the agent is always the build. 🟢 **Reshaped: true of the assessment-interchange
  layer only** — `0.19 %` agent-shaped there against `7.9 %` on school operations, a `41×`
  difference. Filed as `Trend 39`.
- 🔴 **STANDS and now evidenced as a FAILED RE-HOMING: no permissive, maintained,
  framework-independent LTI 1.3 library for Python.** `pylti1.3` (MIT, `138★`) is cold
  since `2024-08-18`; **two attempts to re-publish it have both died** —
  `CNIT-Organization/ltitoolkit` (`fork = false`, carries Viskov's 2019 copyright, renamed
  `ff-ltitoolkit`, git-only despite advertising a PyPI package, `0★`) and
  `pymsglobal/pylti1.3` (created and abandoned the same day, `2025-09-19`). 🟢 **Highest-
  value and cheapest contribution available: adopt and maintain `pylti1.3`**, which already
  has `138★` of dependents. 🟢 **NARROWED: for Django the gap is closed** —
  `academic-innovation/django-lti` (MIT, `26★`, `2026-10-28`, U. Michigan), **unfiled here
  after `63` history mentions.**
- 🔴 **STANDS: no permissive Moodle→LRS event bridge.** All logstore options are GPL-3.0
  (`davidpesce/moodle-logstore_xapi`, `82★`, the maintained one of record) or unlicensed.
  🟢 One narrow MIT exception found and shelved: `openHPI/LRS-Moodle` (Hasso Plattner
  Institute) — **H5P-scoped, `2★`**, not a general bridge. 🔵 Structural, not accidental:
  Moodle's plugin rule makes any replacement GPL. Price as client-owned code.
- 🔴 **NEW: there is no licensed open-source proctoring platform.** `150` repositories on
  `topic:proctoring`; the credible ones (`MyProctor.ai` `236★`, `GodsEye`, the five-agent
  invigilation system) carry **no licence at all**, and the Moodle plugin is `NOASSERTION`.
  🟢 **The only shippable artefacts at that boundary are `SafeExamBrowser` (MPL-2.0, ETH
  Zürich, `361★` — unfiled here `65×`) and two MIT agent rows.** 🔵 Quote proctoring as
  *SEB integration plus a custom agent*, never as "adopt an open-source proctoring platform".
- 🔴 **NEW: `FILED = 0` on an entire `586`-address tier.** Not one agent-shaped SIS,
  gradebook or proctoring artefact had ever reached a curated page; `9` were in the
  append-only history, one re-found **`36×`** (`yukazakiri/koakademy`) and one **`63×`**
  (`academic-innovation/django-lti`) — a new high-water mark for `Trend 16`.
- 🟢 **CLOSED: `583-D`.** Publisher set enumerated at **seven**, each with its scope;
  current-year spread **`3.0×`** (USD `3.7`–`11` bn). 🔵 Quote **USD `3.7`–`11.4` bn, 2026,
  publisher named**. The floor-truncation mechanism is identified: aggregator compilations
  are **derived, not publishers**.
- 🟢 **CLOSED: `583-C`, second branch.** `ingest/address-disposition.sh` committed — a
  shell-only replica of the ledger's FILED/UNFILED/NEW disposition logic. 🔴 The Python
  instrument is **still denied** (`"Code from External"`); the shell replica **runs**, and
  it produced every token-check in this pass.
- 🟢 **CLOSED: `583-G`.** Three trends filed this pass at the `^## <n>. ` form; series ends
  at `40`.
- 🔴 **STANDS, 9th pass: market sizing is vendor-only.** All seven enumerated publishers
  are commercial. The only non-commercial source located is the **OECD Digital Education
  Outlook 2026**, which is qualitative.
- 🔴 **STANDS: no primary legal text from this session, in any jurisdiction** (`583-E`).
  🔵 **This should be an allowlist request, not a recurring action item**, and it now
  constrains the Philippines, Türkiye, Thailand and Bangladesh findings as well — every
  2026 instrument named in this pass rests on secondary reporting.
- 🔴 **STANDS: `curl -sI` URL verification is inoperable here.** Every `github.com` URL
  returns `403` through the session proxy; the run prompt mandates this broken check.
  🟢 Use `gh api -X GET search/repositories -f q='repo:owner/name'`, which answers `200`
  and `422` discriminably against a fabricated control.
- 🔴 **STANDS and now WIDER: region is unobtainable from the API.** `users/{login}` is
  `403` and 🆕 **`repos/{owner}/{name}` is `403` as of this pass** — so `fork` is available
  only from the *search* payload, and `parent`/`source` not at all. **Read "Global" as
  *provenance unknown*.** 🔵 Lineage must be established from licence-text provenance and
  package identity, as it was for `ltitoolkit` this pass.
- 🔴 **STANDS: nineteenth consecutive nil on the mandated supply legs**, fourth on the
  regional ones. 🟢 **But they produced `9` usable intel tokens against `0` addresses** —
  🔵 **reclassify them as a demand-intelligence channel being graded as a supply channel.**
  Native-language legs: **`17 of 17` productive across three passes.**

- 🔵 **Next pass, in priority order:** (1) 🟢 **Execute `Trend 38`'s stage-one audit across
  the remaining superlatives** — `grep` the curated pages for each claim's own subject
  vocabulary before spending any search budget; the one false claim of three fell to a
  single `grep`, and `50`+ remain unswept; (2) 🔴 **shelve the `18` UNFILED integration-axis
  addresses from `p583` and the `9` from this pass** — the debt is now `27` known addresses
  across two passes and the replica to find them exists; (3) **test `Trend 39`'s mechanism
  on a third layer** — pick one specified (`topic:scorm`, `topic:onerostr`) and one
  unspecified (`topic:iep`, `topic:truancy`) and predict the agent share *before*
  measuring; (4) **run native-language legs for the jurisdictions still unqueried** —
  Vietnam (`vi`) first-hand, Morocco/Maghreb (`fr`/`ar`), Pakistan (`ur`), Nigeria —
  the method is `17 of 17`; (5) **request a network allowlist for primary legal hosts**
  (`583-E`), which now constrains eight findings rather than four.


## p583 — 2026-11-01 — **a load-bearing gap withdrawn by the base's own history, two new trends, and the first pass whose central finding came from grepping itself before searching**

🟢 **All four `p582` priorities executed in order.** (1) The integration axis swept singly —
and its premise refuted. (2) The five remaining native-language legs run. (3) The Korean
reclassification confirmed and, for the first time, **quantified**. (4) The superlative
audit added to the pre-publish check — **and it refuted two claims on these shelves.**

### 🟢 `Gap "no maintained permissive LTI 1.3 library"` — WITHDRAWN, by this base's own discard pile

🔴 **`p582` filed this as NEW and load-bearing**, with the note that *"most recipes depend
on"* the cold `pylti1.3`. It is refuted, and the refutation required no discovery:

| repo | licence (byte-read) | ★ | `pushed_at` | LTI version | where it already was |
|---|---|--:|---|---|---|
| `jupyterhub/ltiauthenticator` | 🟢 BSD-3-Clause (`1,528 B`) | 73 | `2026-10-05` | 🟢 **1.3 + 1.1** | 🔴 **`15` mentions in this base's history, `0` on any curated page** |
| `StevenWeathers/peregrine-lti` | 🟢 Apache-2.0 (`11,357 B`) | 7 | `2025-11-20` | 🟢 **1.3** (Go) | 🔴 `4` history mentions, `0` curated |
| `swisnl/laravel-lti-provider` | 🟢 MIT (`1,108 B`) | 4 | `2026-08-28` | 1.x (Laravel) | 🆕 new |

🟢 **The accurate, narrower statement:** there is **no permissive, maintained,
framework-independent LTI 1.3 library for Python**. `pylti1.3` (MIT, `138★`) is the
most-starred Python option at `26.5` months cold — not `27`, and the rounding was carried
rather than measured. The maintained permissive options are **Go**,
**Laravel/PHP** and **JupyterHub-bound**; the maintained framework-independent PHP option,
`oat-sa/lib-lti1p3-core` (`37★`, `2026-10-24`), is 🔴 **GPL-2.0**.
🔵 **Why the error matters more than its size:** the claim was used to justify a sweep, and
the sweep's own first step — `grep` the shelves — refuted the claim that commissioned it.
`579-F` prescribed the token-check for *findings* and `580-G` extended it to
*instruments*; this pass shows it must also cover **the premises of prescriptions.**

### 🔴 WITHDRAWN `p584` — the original form of Trend 36 ("copyleft WITHOUT EXCEPTION"), superseded by the revised `Trend 36` above — refuted by `sakaiproject/sakai`, ECL-2.0, `1,240★`, which was already shelved on `repos/foundations.md`. Retained for the record; **the gradient it describes is right, the universal was not.** Original text follows.

🟢 **Measured, on the four integration axes:**

| class | rows | share |
|---|--:|--:|
| 🟢 permissive (MIT / Apache-2.0 / BSD-3-Clause) | **`22`** | **`66.7 %`** |
| 🔴 copyleft (GPL-2.0 / GPL-3.0) | `8` | `24.2 %` |
| 🟡 `NOASSERTION` — a work queue, not a verdict | `3` | `9.1 %` |

🔴 **CORRECTED `p585` (2026-11-01):** the claim *"every platform of record is copyleft"* is **false** and was withdrawn as `Trend 36`. Four platforms of record are permissive and forkable: **Sakai** (ECL-2.0, 1,240★), **OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★) and **relate** (MIT, 437★) — all four read from their own licence files. See [`../repos/foundations.md`](../repos/foundations.md). The statement below is retained as written for history.


🔴 **Against every platform of record, which is copyleft without exception:** Moodle
GPL-3.0 · Open edX **AGPL-3.0** · Chamilo GPL-2.0 · ILIAS GPL-3.0 · OpenEduCat LGPL-3.0 ·
Gibbon GPL-3.0 · ERPNext GPL-3.0. 🟢 The one permissive platform seat is OpenOlat, and
only by byte-read — the API reports `NOASSERTION`.

🔵 **`p574` measured the accessibility and assessment-interchange layer at `10` shippable
against `11` copyleft and concluded the layer's licensing "runs backwards". On the four
integration axes the ratio runs the other way, `22:8`.** 🟢 **Both are right, and that is
the trend:** licence shape must be measured **per layer** and may not be inferred for
"education open source" as a whole — the field has no characteristic licence, it has a
characteristic *gradient*, permissive at the wire protocol and copyleft at the platform.
🟢 **The delivery rule this yields is unusually clean:** a studio may ship the glue and may
not ship a modified platform, in every region, regardless of the regulation.
🔴 **Falsifier:** a maintained, permissively licensed platform of record — an LMS or SIS
above `1,000★`, pushed within a year, under MIT/Apache/BSD — would break the gradient. None
exists on these shelves; OpenOlat at `449★` is the closest and is `NOASSERTION` by API.

## 37. Education AI regulation has moved from decision rights to operational obligations — regulators now specify runtime behaviour a product must implement (high confidence — two new jurisdictions measured in their own languages, naming three build obligations between them)

🟢 **`p582` measured four jurisdictions converging on two *decision-rights* requirements:
AI barred from the terminal assessment decision, and AI use declared or labelled. Two new
jurisdictions extend the convergence to six — and they add a different kind of
requirement.**

| jurisdiction | instrument | the obligation, and what it is |
|---|---|---|
| 🆕 **Vietnam** | Công văn **5588/BGDĐT-GDPT** (`2026-08-19`) | 🔴 **"establish a process for handling AI-related incidents"** — an *operational* duty: logging, triage, escalation, audit trail. Plus age-appropriateness vetting of every tool, and personal-data/IP/infosec compliance |
| 🆕 **Indonesia** | **SKB 7 Menteri** No. 400.1-492/2026 (`2026-03-16`) | 🔴 **age-tiered limits on duration *and* content type**, aligned to **PP TUNAS** — per-age-band enforcement inside one product, across formal, non-formal **and informal** education |
| 🟢 Brazil · France · Germany · EU (`p582`) | CNE parecer · cadre d'usage · Länder · AI Act Art. 50 | decision rights and declaration |
| 🟢 **Saudi Arabia** | National Curriculum Center with MoE, MCIT, SDAIA (SY 2025-26) | 🟢 **learning outcomes counted in overall student assessment** — so assessment integration is mandated scope, not an upsell |

🟢 **Why this is a distinct trend and not an extension of `p582`'s.** A decision-rights
rule constrains **what the model may conclude**; an operational rule constrains **what the
system must do when it goes wrong**. The second cannot be satisfied by prompt design,
model choice, or a human-in-the-loop checkbox — it requires incident state, retention, and
an audit surface, which is architecture. 🔵 **Engineering consequence:** the portable
default set is now **refusal + provenance logging + an incident pipeline + per-age-band
policy enforcement**. A product with the first two and not the last two is non-compliant
in Vietnam and Indonesia regardless of accuracy.
🔴 **Falsifier:** a jurisdiction adopting education-AI rules that specify *outcomes only*
with no operational or age-banding duty, published after `2026-08`, would show the move is
not directional. 🔵 **Confidence caveat:** both instruments are read through
legal-database and ministry-adjacent secondary sources; the primaries are unobtainable
because every government host returns `000` from this harness, **including a fabricated
control**.

### 🔵 Counter note on the trend counter

🔴 **`p582` filed three trends as `### Trend NEW` without numbers**, so the numbered series
still ends at **`35`** and the derived trend count excludes them. This pass files at the
counter's own `^## <n>. ` form (**36**, **37**). 🔵 Recorded so the next pass does not
conclude the count regressed.

## Declared gaps — updated `2026-11-01` (`p583`)

- 🟢 **WITHDRAWN: "no maintained permissive LTI 1.3 library."** Refuted by
  `jupyterhub/ltiauthenticator` (BSD-3-Clause, `2026-10-05`), which was in this base's
  history `15×`. 🔴 **RESHAPED to the true, narrower gap: no permissive, maintained,
  framework-independent LTI 1.3 library for *Python*.** Highest-value contribution a studio
  could make back to this ecosystem. **Supersedes `p582`.**
- 🟢 **WITHDRAWN: "the only permissively licensed QTI tool."** Six exist, all byte-read;
  three were already in this base's history.
- 🔴 **NEW: there is no agent-shaped supply on the integration axis.** `538` repositories
  across four axes, **one** agent artefact (`rikardroitto/canvas-quiz-skill`, `1★`). The
  assessment-interchange tier is a library tier; the agent is always the build.
- 🔴 **NEW: no permissive Moodle→LRS event bridge.** `moodle-logstore_xapi` (GPL-3.0) is
  the maintained option of record, and Moodle's plugin rule makes any replacement GPL
  anyway. 🔵 Price this as client-owned code, never as shippable IP.
- 🔴 **NEW: the published 2026 market floor was `2.6×` too high.** A sixth publisher
  (Persistence, USD `3.7` bn) sits below the prescribed `9.6`–`11.4` bn range; the
  current-year spread is **`3.1×`**. Quote **USD `3.7`–`11.4` bn**, publisher named.
  🔴 Unverifiable first-hand — `persistencemarketresearch.com` does not resolve here.
- 🔴 **STANDS, and now with a measured price: selling to a mandate is not selling to a
  budget.** Korea `34.2 % → 5.2 %` adoption in one year after reclassification, `₩1.4` tn
  spent. Price off funded programmes that survived a downgrade.
- 🔴 **STANDS, 8th pass: market sizing is vendor-only.** No independent estimate exists.
- 🔴 **STANDS: no primary legal text from this session, in any jurisdiction.**
  `law.go.kr`, `moe.go.kr`, `eur-lex.europa.eu`, `kemendikdasmen.go.id` all return `000`
  — **and so does a fabricated control.** 🔵 **This should be an allowlist request, not a
  recurring action item**, and it is now the binding constraint on four separate findings.
- 🔴 **STANDS: `curl -sI` URL verification is inoperable here.** Every `github.com` URL
  returns `403` through the session proxy. The run prompt mandates this broken check. Use
  `q=repo:owner/name`.
- 🔴 **STANDS: region is unobtainable for individually-owned repos** (`users/{login}` is
  `403`). **Read "Global" as *provenance unknown*.**
- 🟢 **CLOSED: `580-C`.** At **`1`** real defect, not `40` — `168 of 179` dead citations
  are in append-only history and must not be migrated.
- 🟢 **CLOSED: `580-E`.** `pushed_at` now carried on every table this pass writes.

- 🔵 **Next pass, in priority order:** (1) 🔴 **Audit the remaining `18` UNFILED
  integration-axis addresses and the `50`+ "the largest"/"the only"/"the first" superlative
  claims on the curated pages** — two of the first three audited were false, so the class
  has a measured failure rate and no pass has swept it; (2) **run the native-language legs
  for the jurisdictions still unqueried** — Türkiye (`tr`), Egypt (`ar`), Thailand (`th`),
  Philippines, Bangladesh (`bn`) — the method is `13 of 13` productive across two passes;
  (3) 🔴 **re-measure `ingest/address-ledger.py --debt` properly** — it is the instrument
  that would have pre-empted this pass's central finding and it **could not be executed
  here** (`"Code from External"`, the `576-G` per-invocation denial), so the `18`-row debt
  was found by a hand replica; (4) **request a network allowlist for primary legal hosts**,
  which now blocks four findings rather than one.


## p582 — 2026-11-01 — **three new trends, one gap withdrawn rather than closed, a superlative corrected across six pages, and the first measured reversal of a national AI-education mandate**

🟢 **All three `p581` priorities were executed in order.** (1) The native-language demand
legs ran across eight jurisdictions. (2) The five remaining single capability topics were
swept with the corrected query form. (3) The shelf dead-row audit was run against the
`p580` census.

### 🔴 `Trend` NEW — a national AI-education mandate can be downgraded mid-rollout, and one just was

🔴 **Korea's AI digital textbook (AI 디지털교과서) was reclassified from "textbook"
(교과서) to "educational material" (교육자료)** during legislative passage, which removed
its compulsory force. The ministry now says **"AI 교육자료"** and frames the policy as
*autonomous selection with guidance on selection criteria*; **provincial education offices
then cut or deferred their 2026 subscription budgets.** The original staged roadmap —
grades 3–4, M1, H1 in 2025; grades 5–6, M2 plus four more subjects in 2026 — **is no
longer a procurement schedule.**

🟢 **Why this is a trend and not a news item.** This base has treated a dated national
mandate as its firmest category of demand evidence, across several regions and many
passes. **This is the first instance measured where such a mandate was walked back after
rollout began**, and the mechanism — reclassification rather than repeal — is one that
leaves the programme nominally alive while removing every procurement obligation.
🔵 **Generalised rule:** price off *funded* programmes that survived a downgrade (Korea:
K-education AI, `1,000` AI-focused schools), never off a mandate's existence.
Confidence: **medium-high** — consistent across multiple Korean-language sources, but the
legal status should be re-confirmed against a Ministry of Education primary document, and
several results in the leg were 2024-dated.

### 🔴 `Trend` NEW — four regulators independently converged on the same two product requirements

🟢 **Measured, not inferred, across four jurisdictions queried separately in four
languages this pass:**

| jurisdiction | AI barred from the terminal assessment decision | AI use must be declared / labelled |
|---|---|---|
| 🟢 **Brazil** (CNE *parecer*) | 🟢 yes — may be a *first filter*, **may not determine pass/fail** | 🟢 yes — four-tier risk classification |
| 🟢 **France** (*cadre d'usage*) | 🟢 yes — human judgement retained | 🟢 yes — **undeclared genAI in a submission is fraud** |
| 🟢 **Germany** (Länder) | 🟡 partial | 🟢 yes — **Hessen: prompts too**; NRW: all aids |
| 🟢 **EU** (AI Act Art. 50) | 🟡 via Annex III high-risk route | 🟢 yes — transparency from `2 Aug 2026` |
| 🟢 **Brazil, additionally** | 🔴 **total prohibition in early-childhood education** | — |

🟢 **The engineering consequence is concrete and portable: build human-in-the-loop
*refusal* and provenance logging as defaults.** A grader that *can* emit a final mark is
non-compliant in Brazil and France regardless of accuracy. 🔵 **This is the first trend on
this page that is a product specification rather than a market observation**, and it is
the same specification in four regulatory languages. Confidence: **high** — four
independent jurisdiction legs, primary-instrument names captured in each.

### 🟢 `Trend` NEW — the demand channel is the jurisdiction's own language, now with controls

🟢 **`p581` asserted this and prescribed the test; `p582` ran it with both arms in the
same pass:**

| channel | legs | productive | yield |
|---|--:|--:|---|
| 🟢 native-language ministry vocabulary | 8 | **8** | dated instruments, named bills, risk tiers, budget reversals |
| 🟡 English regional/global listicle | 2 | 1 (partial) | one preemption framework; **zero** usable repos |

🔴 **And the supply-side arm reproduces the same asymmetry.** The mandated listicle leg
`top open source AI agents education 2026 github MIT tutoring` returned three addresses
new to this base; **measured first-hand, two were dead or archived** (`TeachGPT` `27★`,
last push `2023-12-24`; `1111philo/learn` `1★`, `archived: true`) **and the third was
mis-categorised** (`pguso/agents-from-scratch`, MIT, `1,065★` — a curriculum, not a tutor).
**The index channel returned `27` live permissive rows in the same pass.**
🟢 **Settled: `1` marginal row from listicles, `27` from the index.** Confidence: **high**
— both channels run in one session with first-hand verification of every candidate.

### 🔴 `Gap "psychometrically defensible item generation"` — WITHDRAWN, not closed, and this reverses `p581`

🔴 **`p581` reshaped this gap as *"calibration ≠ generation"*, keeping calibration as the
half that exists in open source. That reshaping is withdrawn: the calibration half is also
dead.** The dead-row audit measured **every** psychometric row on the shelf:

`pypsy` 🔴 `2018-11-16` · `ShadowCAT` 🔴 `2017-11-20` · `HCD-code` 🔴 `2022-08-14` ·
`girth` 🔴 `2022-09-09` · `vipsy` 🔴 `2023-07-06` · `pyirt` 🔴 `2023-08-22` ·
`ICD` 🔴 `2024-03-04` · `DCD` 🔴 `2024-03-13` · `psychmeta` 🔴 `2024-06-19` ·
`meyerjp3/psychometrics` 🔴 `2024-10-03` · `EduCDM` 🔴 `2024-10-25`

🔴 **Eleven rows, zero maintained, newest two years cold, five carrying no licence at
all.** 🟢 **The correct statement: psychometrically defensible assessment is not a
composition problem in open source, because there is nothing live to compose. It is a
build or a commercial dependency.** 🔵 The one live exception is regional and narrow:
`douglasrizzo/catsim` (BSD-3-Clause, `153★`, Brazil-maintained) — adaptive-test
*simulation*, not calibration or generation. Confidence: **high** — first-hand
`pushed_at` on every row.

### 🔴 The shelf has a maintenance debt, and it is concentrated in the recipe layer

| cut | count |
|---|--:|
| shelf addresses measured (`p580`) | `265` |
| 🟡 stale 12–24 months | `15` |
| 🔴 dead >24 months | **`30`** |
| 🔴 **…cited in [`../compose/patterns.md`](../compose/patterns.md)** | **`19`** |

🔴 **`19` abandoned repositories are named as components inside this base's delivery
recipes** — the pages a studio builds from. 🟢 **Two were replaced this pass:**
`githubharald/DeslantImg` (🔴 `2021-11-21`) and `githubharald/WordDetector`
(🔴 `2023-05-05`) are both superseded by `datalab-to/chandra` (Apache-2.0, `12,655★`,
handwriting + tables + layout, pushed `2026-10-22`). 🔴 **One is load-bearing with no
replacement found:** `dmitry-viskov/pylti1.3` (MIT, 🔴 `2024-08-18`) — **LTI 1.3 is how an
AI layer legitimately attaches to Moodle, Canvas or Open edX**, and most recipes depend on
it. 🔴 **Four should not be offered at all**, two of them unlicensed:
`IronCountySchoolDistrict/iep-printing-php` (`1★`, no licence, 🔴 `2017-03-29`),
`microsoftarchive/Learn-LTI`, `tc-imba/canvas-auto-rubric` (no licence),
`fotinikafida/text-to-moodle`.

### 🔴 Correction propagated: the "largest permissive repository" superlative was wrong in six places

🔴 **`microsoft/markitdown` — MIT, `193,266★`, pushed `2026-10-28` — is `2.7×`
`hugohe3/ppt-master` (`71,711★`) and `3.6×` `HKUDS/DeepTutor` (`52,957★`).** The claim
that `ppt-master` was *"the largest permissively licensed repository anywhere in this
knowledge base"* has been **amended in place on all six live sites** across
`agents/top.md`, `agents/trending.md`, `repos/foundations.md`, `repos/trending.md`,
`compose/patterns.md` and this page. Append-only history and `archive/` are left intact as
the record. 🟢 **`markitdown` is also better-attributed than the row it displaces:** owner
**Microsoft** places it to **North America**, where `ppt-master` is carried as *"provenance
unverified, no region assigned"*. 🔵 **The method lesson is `Trend 11`'s, inverted:** this
base audits for *closed gaps republished as discoveries*; it had no check for **a
superlative invalidated by a later measurement**. One grep caught six instances.

### 🟢 Licence resolved from bytes: `microsoft/autogen` ships two licences and both prior readings were half right

| source | verdict |
|---|---|
| `search/repositories` detector | 🔴 CC-BY-4.0 |
| this base's rotation ledger | 🟢 MIT |
| 🟢 `LICENSE` bytes (`main`+`master`, `18,649 B`) | **CC-BY-4.0** |
| 🟢 `LICENSE-CODE` bytes (`main`+`master`, `1,140 B`) | **MIT, © Microsoft Corporation** |

🟢 **The code is MIT; the default `LICENSE` is CC-BY-4.0 and covers docs, notebooks and
samples.** 🔵 **Consequence:** the library is shippable, but material lifted from its
documentation carries an **attribution obligation**, and any automated compliance scan a
client runs — reading only `LICENSE` — will label the whole repository CC-BY-4.0.
🔴 **Generalises:** a single-file licence read is insufficient for repositories that
separate code and content licences, and this base's detector-based census cannot see the
distinction. Confidence: **high** — four byte reads across two branches.

## Declared gaps — updated `2026-11-01` (`p582`)

- 🔴 **WITHDRAWN (was "reshaped"): psychometric item generation.** Not "calibration exists,
  generation does not" — **neither exists**. All eleven psychometric rows are dead. This is
  a build, not a composition. **Supersedes `p581`.**
- 🔴 **NEW and load-bearing: no maintained permissive LTI 1.3 library.** `pylti1.3` is
  27 months cold and most recipes depend on it. **Next pass: sweep `topic:lti` and
  `topic:lti-provider` singly** — never swept with the corrected form.
- 🔴 **RESHAPED, unchanged from `p581`: tutor-degradation detection.** `popmon` (MIT) and
  `frouros` (BSD-3-Clause) are the statistical half; the education-aware layer is unbuilt.
- 🟢 **CLOSED: nothing open-source handles handwritten student work.** `datalab-to/chandra`
  (Apache-2.0, `12,655★`) does handwriting, tables and layout; `breezedeus/Pix2Text` (MIT)
  does maths formulae.
- 🟡 **NARROWED: nothing open-source *authors* instructional video.** Still true for
  generation, but `QuentinFuxa/WhisperLiveKit` (real-time + diarisation + translation) and
  `liuzhao1225/YouDub-webui` (localisation + dubbing) close the **delivery and access**
  half, which is the regulated half.
- 🔴 **STANDS, 7th pass: market sizing is vendor-only.** No independent estimate exists.
  **But it now has a measured shape** — five publishers, 2026 range USD `9.6`–`11.4` bn,
  terminal values differing `>3×`, cause identified as scope definition. Quote a range with
  the publisher named, never a point.
- 🔴 **STANDS: no primary EU legal text from this session.** `eur-lex.europa.eu` does not
  resolve. **This should be an allowlist request, not a recurring action item.**
- 🔴 **STANDS: `curl -sI` URL verification is inoperable here** — every `github.com` URL
  returns `403` through the session proxy, so a `403` cannot be told from a 404. The run
  prompt mandates this broken check. Use `q=repo:owner/name` against `search/repositories`.
- 🔴 **STANDS: region is unobtainable for individually-owned repos.** `users/{login}` is
  `403`. Rows are placed only on **owner identity** (Microsoft, Mindee, Kozea, LlamaIndex,
  ING Bank, IFCA, CMU) or **description language**. **Read "Global" as *provenance
  unknown*, never as *geographically spread*.**
- 🔵 **Next pass, in priority order:** (1) **sweep `topic:lti`, `topic:lti-provider`,
  `topic:xapi`, `topic:qti` singly** — the integration axis, now the base's most important
  unreplaced dependency; (2) **re-run the native-language legs for the jurisdictions not
  covered this pass** — Indonesia (`id`), Vietnam (`vi`), Saudi/UAE (`ar`), Nigeria,
  Poland (`pl`) — the method is proven and these are unqueried; (3) **confirm the Korean
  reclassification against a MOE primary document**, because a reversal of that size should
  not rest on secondary sources; (4) **add a superlative-audit step** to the pre-publish
  grep, on the `markitdown` precedent.


## p581 — 2026-11-01 — **three trend updates, one gap closed, one gap reshaped, and a measurement defect that retroactively explains four passes of empty sweeps**

### 🟢 `Gap "lecture-video tooling remains unswept"` — CLOSED

The sweep was run. **Five new permissive addresses**, concentrated almost entirely in one
topic (`topic:subtitles`): `VidBee` (MIT, `11,026★`), `autoclip` (MIT, `9,898★`),
`video-subtitle-extractor` (Apache-2.0, `9,680★`), `youtube-transcript-api` (MIT,
`8,543★`), `ffsubsync` (MIT, `7,929★`).

🔵 **But the gap closes with a correction to its own premise.** It was written as a search
for **lecture-content generation**, and that is *not* what exists. What exists is a
**transcript-and-caption toolchain**: recording → text → aligned text → clips. Nothing
open-source authors instructional video. 🟢 The base's earlier instinct to not shelf
`MoneyPrinterTurbo` as lecture tooling was right — **but `autoclip` is different and
should be shelved**, because its own description names **课程 (courses)** as an input class
alongside podcasts and interviews, and it carries `ai-agent` and `mcp` topics. **Repurposing
an existing lecture is a real education capability; generating a fake one is not.**

### 🔴 NEW `Trend` — the crossed-topic query form collapses, and it explains a four-pass miss

🔴 **`topic:A+topic:education` returns `total_count = 0`. Six query forms, six zeroes** —
`text-to-speech`, `accessibility`, `whisper`, `assessment+llm`, `llm-evaluation+education`,
`edtech+license:mit`. Not sparse results: **empty**.

🔵 **Cause is maintainer tagging, and it is structural.** Education projects tag pedagogy
(`ai-tutor`, `edtech`, `education`); capability projects tag capability (`pptx`,
`subtitles`, `ocr`, `drift-detection`). **The two populations barely intersect.**
`DeepTutor` carries `ai-tutor` and no `video`. `ppt-master` carries `pptx` and no
`education`.

🟢 **This retroactively explains the base's own most expensive recorded miss.** The
declared gap reads: *"`hugohe3/ppt-master` — MIT, `71,498★`, the largest permissively
licensed repository anywhere in this KB — went unfound for four passes because every sweep
filters on an education topic and it carries none."* **That was diagnosed as a coverage
habit. It is actually a query-form defect**, which is a stronger and more fixable claim.
🟢 **Correct form, now established:** one capability topic, `sort=stars`, filter
`license.spdx_id` and `pushed_at` client-side. Confidence: **high — measured first-hand,
14 topics, same session.**

### 🟢 `Trend` UPDATE — the "no way to detect a degraded tutor" gap is reshaped, not closed

Six passes have carried: *"A tutor in production still has no open-source way to detect
that it has degraded — the clearest unmet build opportunity in the industry."*

🟢 **`topic:drift-detection` (`1,308` repos) returns three addresses new to this base:**
`ing-bank/popmon` (MIT, `512★`), `IFCA-Advanced-Computing/frouros` (BSD-3-Clause, `260★`),
`SeldonIO/alibi-detect` (🔴 NOASSERTION, `2,554★`, stale `2025-12-11`).

🔴 **The gap was mis-stated as absence. It is education-specificity.** Generic drift
detection is permissive, maintained and composable; **none of it knows what a learner model
is**, so none detects "this tutor's explanations degraded". 🟢 **What is now buildable is
the measurable half** — distribution shift on the feature and outcome streams a tutor
already emits — and composing `frouros` or `popmon` with `pykt-team/pykt-toolkit` (MIT,
`456★`), whose knowledge-tracing predictions are precisely the distribution to monitor,
gives this base **its first buildable answer to its own hardest question**. Recipe:
[`../compose/patterns.md`](../compose/patterns.md).
🔵 **Regional observation worth keeping:** all three drift rows are **EMEA-origin**, two
owned by **named institutions** (ING Bank N.V.; Instituto de Física de Cantabria) — the
strongest region-placement signal available here, since `users/{login}` is `403` and
maintainer `location` is unobtainable by any route. 🔴 Do not build on `alibi-detect`
despite it being the highest-starred: licence unresolved **and** ~11 months stale.

### 🔴 The item-generation gap STANDS — and a near-miss worth recording

🔴 **`topic:item-response-theory`, `topic:psychometrics` and
`topic:computerized-adaptive-testing` returned no row not already shelved** — `catsim`
(138 references in this base), `girth` (84), `EduCDM` (40), `Agent4Edu` (35), `pypsy` (19).
🟢 **This pass drafted those as new finds and caught it by grepping the shelf before
publishing.** That is `Trend 11`'s pathology — a closed gap re-published as a discovery —
**intercepted pre-publication for the first time.** 🟢 **Recommend the grep-before-write
check become standing practice**: `grep -ro "owner/name" --include=*.md .` costs nothing
and is the only thing that caught this.

🔵 **The gap is also narrower than previously written.** Psychometric **calibration and
adaptive-test simulation** are shelved and permissive (`catsim` BSD-3-Clause, live
`2026-10-30`; `EduCDM` Apache-2.0 but stale `2024-10-25`). **Item *generation* is the
hole.** These are different absences and should not be merged again. 🔴 Also note the
decay in that cohort: `pypsy` (MIT, `242★`) **last pushed 2018-11-16** — eight years dead
and still carried; `girth` stale since 2022.

### 🔵 Demand-side instrument: third consecutive nil, 19th for the global legs

All eight mandated legs returned shelved intel. 🟢 **Two new tokens only:** the Council of
Europe's **common repository for evaluating AI's effectiveness** (new to this base
entirely, and it gives the **CoE Legal Instrument a second source** — narrowing a declared
single-source gap), and the US Dept. of Education **AI grant-priority rule date,
`13 April 2026`**. 🔴 **The prescribed web legs are now a regression test, not a source.**
The method that still pays is per-jurisdiction querying in the jurisdiction's own language
(`p575`, `p576`), unrun for three passes. **Next pass should run the language legs and skip
two of the four English regional legs** — they have produced two tokens in three passes
between them.

🔴 **Unverifiable figure, flagged so it stops circulating:** `83 %` of institutions
planning an AI teaching-assistant deployment, widely attributed to EDUCAUSE. **Could not
be confirmed. Do not use.** Market sizing unchanged and vendor-only at six passes: quote
**USD 10.6–12.5 bn (2026) → USD 42.48 bn (2030)** as a range, never a point.

## Declared gaps — updated `2026-11-01` (`p581`)

- 🟢 **CLOSED: lecture-media sweep.** Five permissive addresses shelved. **The replacement
  gap is specific: nothing open-source *authors* instructional video**; the toolchain is
  transcript, caption and clip.
- 🔴 **RESHAPED: tutor-degradation detection.** No longer "nothing exists" — **nothing
  *education-specific* exists**. `popmon` (MIT) and `frouros` (BSD-3-Clause) are the
  statistical half. The education-aware layer is unbuilt and remains the best build
  opportunity in this industry.
- 🔴 **STANDS: psychometrically defensible item generation.** Searched three ways this
  pass; every row returned was already shelved. Calibration ≠ generation.
- 🔴 **STANDS: no primary EU legal text from this session.** `eur-lex.europa.eu` does not
  resolve — a network-policy constraint. **This should be an allowlist request, not a
  recurring action item.**
- 🟡 **NARROWED: Council of Europe instrument** now two-source (both secondary); the
  companion **common repository** is single-source and new.
- 🔴 **STANDS: market sizing is vendor-only at six passes.** No independent estimate located.
- 🔴 **NEW: `curl -sI` URL verification is inoperable in this environment.** Every
  `github.com` URL returns `403` through the session proxy, including live repositories, so
  a `403` cannot be distinguished from a 404. **The run prompt mandates this broken check.**
  Use `q=repo:owner/name` against `search/repositories`, which returns existence plus
  licence, stars, forks, `pushed_at` and `archived` in one `200`.
- 🔴 **NEW: region remains unobtainable for individually-owned repos.** Four of this pass's
  seven rows were placed from **owner identity** (ING Bank, IFCA) or **description
  language** (zh-first). `users/{login}` is `403`, so maintainer `location` is unreachable.
  **Read "Global" as *provenance unknown*, never as *geographically spread*.**
- 🔵 **Next pass, in priority order:** (1) run the per-jurisdiction native-language demand
  legs, unrun for three passes and the only demand method still paying; (2) sweep remaining
  single capability topics — `topic:pptx`, `topic:ocr`, `topic:pdf`, `topic:speech-to-text`,
  `topic:diagrams` — now that the correct query form is established; (3) audit the shelf for
  dead rows, `pypsy` (8 years) being the proof the problem is real.


## 🆕 `p580` — `2026-11-01` — trends 33–35, filed at `##` with the counter's own `^## <n>. ` form, plus the `579-D` falsifier result

### 🟢 `Gap 579-D` RUN: `Trend 32` SURVIVES ITS FALSIFIER — and the falsifier is mis-specified

`Trend 32` states that education's **institution-accountable** layers have no popular open
anchor, and declared its falsifier in advance: *"a single education axis whose artefact is
institution-accountable and whose head exceeds `1,000★`."* All five prescribed axes were
measured this pass (`evidence/trend32-falsifier.2026-11-01-p580.tsv`):

| axis | repos | head | stars | licence | is it an education artefact? |
|---|--:|---|--:|---|---|
| `topic:accreditation` | `44` | `NUWCDIVNPT/stig-manager` | `236` | NOASSERTION | 🔴 no — US DoD STIG compliance |
| `topic:safeguarding` | `27` | `Brainhub24/TitanShield` | 🔴 **`6`** | Apache-2.0 | 🔴 no — generic security toolkit |
| `topic:proctoring` | `150` | `vardanagarwal/Proctoring-AI` | `633` | 🟢 **MIT** | 🟢 **yes** |
| `topic:transcript` | `929` | `jdepoix/youtube-transcript-api` | 🟢 `8,543` | MIT | 🔴 no — YouTube API wrapper |
| `topic:credential` | `85` | `git-ecosystem/git-credential-manager` | 🟢 `9,420` | NOASSERTION | 🔴 no — git authentication |

🔴 **Two axes cross the `1,000★` threshold and neither is an education tool.** Both are
**vocabulary collisions**: "transcript" means a speech-to-text artefact far more often
than an academic record, and "credential" means a secret far more often than a
qualification. 🟢 **The highest genuinely institution-accountable education head in the
whole sweep is `633★`** — `Proctoring-AI`, MIT, already on this base's trending pages.
**`Trend 32` holds.**

🔴 **But the falsifier as written cannot do its job.** Its threshold is crossable *only*
by a collision, because `Trend 29` already established that the head of an education
`topic:` axis is usually not an education tool. A falsifier that only a false positive can
trip is not a test. 🟢 **Restated so it can be run:** *a single axis whose head **is an
education artefact**, is institution-accountable, and exceeds `1,000★`.* On that form the
margin is now measured: **`633★` against `1,000★`** — the closest this base has come, and
it comes from proctoring, the most liability-bearing axis of the five.

🔵 **`topic:safeguarding` topping out at `6★` is the commercially loudest number here.**
Safeguarding is a **statutory duty** for schools in England (*Keeping Children Safe in
Education*), with named accountable persons and audit obligations, and the entire open
supply is one `6★` repository that is not even an education tool. This is a **BUILD**
recommendation of the same shape `p575` reached for `topic:iep` at `7★`, and it is
EMEA-anchored rather than US-anchored.

## 33. The GitHub licence field is blind to manifest-declared grants, so the cheapest new channel is the one that must not be trusted on the one question that gates delivery (high confidence — measured first-hand, 4 of 4, against byte-for-byte reads)

🔵 **The claim.** `p579`/`p580` opened a channel that returns `license.spdx_id` in one
call. It is authoritative for existence, stars, forks, `archived` and `pushed_at`. 🔴 **It
is structurally wrong, in both directions, for languages that declare their licence in a
package manifest rather than a `LICENSE` file**, because GitHub's detector only reads the
file.

🟢 **Measured, `5 of 5`** (`evidence/manifest-licence-blindness.2026-11-01-p580.tsv`):

| address | API `spdx_id` | `DESCRIPTION` → `License:` | API correct? |
|---|---|---|---|
| `Wenchao-Ma/GDINA` | 🔴 `NONE` | 🟢 `GPL-3` | 🔴 no |
| `philchalmers/mirt` | 🔴 `NONE` | 🟢 `GPL (>= 3)` | 🔴 no |
| `patriciamar/ShinyItemAnalysis` | 🔴 `NONE` | 🟢 `GPL-3` | 🔴 no |
| `dexter-psychometrics/dexter` | 🟢 `LGPL-3.0` | `LGPL-3` | 🟢 yes |

🔴 **Three of four R/CRAN packages report `NONE` — "no licence at all" — while declaring
GPL in `DESCRIPTION`.** This base already reads R grants from `DESCRIPTION` (`p573`, and
`agents/top.md` records that CRAN enforces the field); what is new is that **the new
channel contradicts those reads**, and in the most dangerous direction: `NONE` reads as
*all rights reserved*, which would wrongly **BLOCK** a GPL package, or — run the other
way — wrongly inflate this base's published "ungranted" count.

🔴 **And it runs the other way too, which is the half that bites a licence gate.**
`DMontgomery40/mcp-canvas-lms` (`104★`) has **no licence file at any of 8 paths on either
branch** — yet its `package.json` declares `"license": "MIT"` and lists a `LICENSE` file
that does not exist. So `spdx_id: NONE` can mean *"a grant is declared but no grant text
was shipped"*, which is neither "MIT" nor "all rights reserved". 🟢 **An ambiguous ledger
value (`MIT|no-grant`) is the honest record for that state**, and this pass restored one
it had drafted as an error.

🔵 **Why it generalises past R.** The same shape is waiting in `Cargo.toml`,
`pyproject.toml`, `package.json` and `.csproj`, all of which carry a `license` field the
file-based detector ignores. 🔴 **The scope is already visible in this pass's own census:
`67 of 265` shelf rows (`25.3 %`) return `NONE` or `NOASSERTION`** — and `NONE` cannot be
read as "ungranted" until the manifest has been checked.

🟢 **The division of labour, stated so it can be reused:**

| question | channel | status |
|---|---|---|
| does it exist / stars / forks / `archived` / `pushed_at` / topics | 🟢 `search?q=repo:owner/name` | authoritative, one call |
| what is the grant | 🔴 **byte-for-byte read** of `LICENSE*`, `COPYING`, **and the language's manifest** | the API's `spdx_id` is a hint only |
| is a nil a death or a rename | 🟢 **org listing** (`q=org:owner`) | neither of the other two can tell |

## 34. A base's own address ledger decays far less than it looks, and the instrument that seems to fix it would make it worse (high confidence — measured first-hand on 153 rows, with equivalence classes)

🔵 **The claim.** `Gap 579-B` registered that this base's ledger licence column "is not
gate-safe", on the evidence of two contradicting rows, and prescribed re-deriving the
column from the search endpoint. Both halves needed testing. 🟢 **The decay is small;
🔴 the prescription is harmful.**

🟢 **Measured on all `153` shelf addresses present in the `3,175`-row ledger**
(`evidence/ledger-licence-classify.2026-11-01-p580.tsv`):

| class | rows | share |
|---|--:|--:|
| 🟢 substantive agreement | `103` | `67.3 %` |
| 🟢 ledger `unstated` → **settled first-hand this pass** | `18` | `11.8 %` |
| 🟡 ledger `unstated`, still open (API also blank) | `8` | `5.2 %` |
| 🔴 **API weaker** — ledger has a real SPDX, API says `NOASSERTION` | **`17`** | **`11.1 %`** |
| 🔴 **API blind** — manifest-declared grant, both directions (trend 33) | `4` | `2.6 %` |
| 🟡 ledger imprecise — API gives the exact variant (`BSD` → `BSD-3-Clause`) | `1` | `0.7 %` |
| 🔴 **genuine ledger error** | **`2`** | **`1.3 %`** |

🔴 **So `579-B`'s prescription, executed literally, would have overwritten `21` correct
byte-for-byte reads — including `opendatalab/MinerU` at `82,893★`, Apache-2.0, which the
API reports as `NOASSERTION` — in order to fix `2`.** A **`10.5:1`** loss ratio. 🟢 **The
ledger was updated instead under a rule that only ever adopts a *real* SPDX or a
byte-read manifest truth, never `NONE`/`NOASSERTION` over an existing verdict: `23` rows
changed, none degraded.**

🔵 **The generalisable part, and it is a KB-hygiene law rather than an education one:**
an apparent disagreement rate between two instruments is **not** a decay rate until the
classes are separated. Here the raw disagreement looked like `20.3 %`; after separating
*"the new instrument is weaker"* from *"the old record is wrong"*, the real error rate is
`1.3 %` — more than an order of magnitude lower. **Before re-deriving a column from a cheaper
channel, measure which channel is wrong on the rows where they differ.** Two of this
base's own "no-grant" verdicts also turned out to be a *vocabulary* mismatch with the
API's `NONE` rather than a conflict, which inflated the raw figure further.

🟢 **The two genuine errors, both now corrected in the ledger:**

| address | was | is | why it matters |
|---|---|---|---|
| `bigdata-ustc/EduCDM` | 🔴 `no-grant` | 🟢 **Apache-2.0**, `203★` | A **shippable** cognitive-diagnosis library was filed as unusable — the error direction that silently removes supply |
| `nuwa-skills/montessori-skill` | 🔴 `CC-BY-SA\|CC-BY` | 🟢 **MIT**, `78★` | Filed as share-alike, actually permissive |

🔴 **A third was drafted as an error and is withdrawn by this pass's own byte-read.**
`DMontgomery40/mcp-canvas-lms` (`104★`) has **no licence file at 8 paths × 2 branches**
and the API reports `NONE` — but its `package.json` declares `"license": "MIT"`, and even
lists a `LICENSE` file that does not exist. 🟢 **The ledger's `MIT|no-grant` was the most
accurate record available and has been restored.** 🔵 Treat the row as *declared MIT with
no grant text* — weaker than a licence file, and a question for counsel rather than a
gate, which is exactly what the ambiguous ledger value said.

## 35. A specialised open-source layer dies when a general model absorbs its task, and the licence audit that keeps the layer on the shelf cannot see it happening (high confidence — measured first-hand, 5 of 5 on one axis, 42 of 265 base-wide)

🔵 **The claim.** This base grades supply on **licence** and **stars**. Neither moves when
a repository stops being maintained, so a tier can be fully audited, correctly licensed,
accurately starred — and dead.

🟢 **The clean case is `topic:question-generation`**, shelved here with first-hand licence
bytes and described as the axis's *"reference implementation"* tier. Measured recency:
**`5 of 5` rows last pushed between `2023-12` and `2024-08`**, one of them archived
(full table on `repos/trending.md`). 🔵 **The cause is identifiable and it is not
neglect: every row is a fine-tuned T5 pipeline for answer-aware question generation**, a
task instruction-following models now do zero-shot. The capability did not disappear; it
**moved up the stack**, and the specialised repositories stopped earning maintenance.

🔴 **Base-wide, `42 of 265` live-shelf addresses (`15.8 %`) have not been pushed to in
over twelve months**, against `4` (`1.5 %`) carrying the `archived` flag — so
**staleness is ten times more common than the one condition this base was already
checking for.** `archived` is a deliberate act by a maintainer; abandonment is the
default, and it is invisible unless `pushed_at` is a shelf field.

🔵 **What to do with it commercially, which is the useful half.** Staleness is not
disqualifying on its own — a stable spec or a finished library can sit still legitimately
(`adlnet/xAPI-Spec`, Apache-2.0, `956★`, last pushed `2025-07-03`, is a **specification**
and is fine). 🔴 **It is disqualifying for anything that tracks a moving target:** a
model wrapper, a provider SDK, a format converter, or anything whose task a frontier model
now performs. 🟢 **The rule: pair `pushed_at` with the question "is this repository's task
still scarce?"** Where the answer is no, the row belongs in the history, not in a client
recommendation — and the deliverable moves to the layers around the absorbed task
(item banking, interchange, defensibility), exactly where `Trend 32` already points.


# Current trends — education AI

## 🆕 `p579` — `2026-11-01` — trends 31–32

## 31. The `NOASSERTION` false-negative rate is about one in two, so the flag can never be graded on — it can only be queued (high confidence — four rows read byte-for-byte this pass; the *semantics* of the flag were already established, the *rate* was not)

🔵 **What was already established, and is not claimed here as new.** This base already
records that `NOASSERTION` means *a licence file exists and the detector could not match
it* — not that a licence is absent. 🟢 **What this pass adds is the rate**, which changes
how the flag may be used. Of four `NOASSERTION` rows whose licence files were then read
directly:

| Row | Stars | File reads | `NOASSERTION` was |
|---|---|---|---|
| `CaviraOSS/PageLM` | 2,057 | **CaviraOSS / PageLM Community License** — commercial use needs written permission | 🔴 **true positive** |
| `xiaoyang111222/cn-math-taxonomy` | 5,654 | **Attribution-NonCommercial 4.0 International** | 🔴 **true positive** |
| `OpenOLAT/OpenOLAT` | 449 | **byte-verbatim Apache License 2.0** | 🟢 **false negative** |
| `openeducat/openeducat_erp` | 903 | **GNU LESSER GENERAL PUBLIC LICENSE Version 3** | 🟢 **false negative** |

**Two of four — and the two false negatives are both platforms of record.** A rule of
"reject on `NOASSERTION`" would have removed OpenOlat, the only permissive platform of
record on the verticals page, and OpenEduCat, the education ERP — both of which this base
had licensed correctly all along from its own file reads. 🔵 At roughly one in two, the
flag carries no decision value in either direction: it is a **work queue**, and the file
read is the verdict.

🟢 **The operative rule, which is cheap:** `NOASSERTION` is a *priority queue for file
reads*, nothing more. `curl -sL raw.githubusercontent.com/OWNER/REPO/BRANCH/LICENSE | head`
settles each case in one call, and it settled four this pass. 🔵 The corollary matters for
how this base records licences at all: the ledger's two-valued entries
(`Apache-2.0 | MIT`, `AGPL-3.0 | Apache-2.0`, `CC0-1.0 | MIT`, `GPL-3.0 | GPL-2.0`) and its
`unstated` entries are not uncertainty about the world — they are uncertainty about which
channel was believed. One authoritative channel plus one file read removes both.

🔴 **Where this bites hardest: licences that encode a *commercial* restriction rather than a
copyleft one.** A GPL row is visibly copyleft and gets handled. `CC BY-NC` and a bespoke
"Community License" both *look* open — they permit use, sharing and modification — and fail
only at the point of sale. Both true positives here were of that kind. 🔵 This base had
already read and published both correctly; what it carried wrong was its own **ledger
licence column** (`MIT` for PageLM, `CC-BY` for the NC knowledge graph). A column that
drops a NonCommercial term is worse than an empty one, because a gate reading it passes the
row.

## 32. Open source builds what learners use and skips what institutions are accountable for — so the artefacts closest to a legal obligation are the ones an engagement has to build (high confidence — third independent axis measurement in two passes)

🔵 **The claim.** Ranking education `topic:` axes by the star count of their head separates
them cleanly into two populations, and the dividing line is not technical difficulty — it is
who bears the consequence of the artefact being wrong.

| Axis | Repositories | Head stars | Who the artefact serves |
|---|---|---|---|
| `topic:language-learning` | 4,721 | thousands | the learner, directly |
| `topic:edtech` | 4,980 | thousands | mixed |
| `topic:flashcards` | 3,274 | `4,120` (`fsrs4anki`) | the learner, directly |
| `topic:spaced-repetition` | 3,217 | thousands | the learner, directly |
| `topic:study-assistant` | 205 | **176** | the learner, directly |
| `topic:exam-generator` | **73** | **93** | 🔴 **the institution — it certifies** |
| `topic:iep` (`p578`) | — | **7** | 🔴 **the institution — it is a legal document** |

🔴 **Assessment generation: `73` repositories, nothing above `93★`.** Individual-use
artefacts — flashcards, spaced repetition, study companions — have anchors in the thousands.
The artefacts an institution is *accountable* for — an exam that certifies, an
individualised education programme that is a legal instrument, an accessibility conformance
report — top out in the tens. 🔵 `p574` found the same shape in licensing rather than size:
the accessibility and assessment-interchange layer ran `10` shippable against `11` copyleft,
`2` noncommercial and `6` unlicensed.

🟢 **The mechanism, which makes the prediction testable.** Individual-use software is
adopted by individuals, who star it. Institutional artefacts carry liability, are
jurisdiction-specific, and need a named accountable party — conditions under which a
volunteer project does not accumulate stars and often does not start. Hence the two
permissive heads on `topic:exam-generator` are both **offline-first desktop applications**
(`exameow`, `BCTK`): single-institution, data-stays-local tools, not services. That is the
posture a liability-bearing buyer wants and the posture that cannot scale into a popular
repository.

🔵 **What it means commercially, and it is the better half of the finding.** The layers
with no open anchor are exactly the layers a client cannot download instead of buying.
Adopt the learner-facing tier — it is mature, permissive and free. **Build the
institutional tier, and charge for the accountability**: assessment generation on `Numbas`
(Apache-2.0) with `scorm-again` (MIT) interchange, policy-conformance tooling against the
`134` US state bills and the EU Article 4 duty, and Annex III conformity files for which
`p577` recorded there is still no EMEA-origin open component.

🔴 **The falsifier, stated in advance:** a single education axis whose artefact is
institution-accountable and whose head exceeds `1,000★` would refute the mechanism. Three
axes measured across two passes have not produced one.


## 🆕 `p578` — `2026-10-31` — trends 29–30, filed at `##` with the counter's own `^## <n>. ` form

## 29. On an education topic axis, the highest-starred repository is usually not an education tool — so a sweep that reads only the head of the ladder returns nothing usable (high confidence — measured first-hand on five axes this pass, third independent instance in two passes)

🔵 **The claim.** Ranking an education `topic:` axis by stars puts horizontal infrastructure
at the top, because infrastructure is used by more people than any classroom tool. The
education artefact sits mid-ladder.

🟢 **Measured, five axes, `1,434` repositories:**

| axis | head by stars | ★ | is the head an education tool? | where the usable row sat |
| --- | --- | --: | --- | --- |
| `topic:stem-education` | `goplus/xgo` | 9.5k | 🔴 **no — a programming language** | `goplus/spx`, **8th** |
| `topic:learning-path` | `shovanch/fullstack-web-developer-path` | 3.5k | 🔴 no — a curated reading list | `miuuyy/Clew`, **7th** |
| `topic:tutoring` | `plastic-labs/tutor-gpt` | 933 | 🟡 yes, but **GPL-3.0**, so unusable | rows **5–6** |
| `topic:literacy` | `plastic-labs/tutor-gpt` | 933 | 🟡 same row, same problem | `vgwb/Antura`, **2nd** |
| `topic:math-education` | `tiwe0/GeoChat` | 125 | 🟢 **yes** | **1st** |

🔵 **Prior instances, independently found:** `p577` removed `plugin87/ux-ui-agent-skills`
(MIT, 3.1k★, a design-system layer for coding agents) from the agent shelf — *"size reads as
credibility"* — and `p572` recorded that the smallest axis it had ever swept
(`topic:lesson-plan`, 44 repositories) was its most productive. **Three instances, three
passes, two of them on this pass's own evidence.**

🟢 **What it changes operationally.** The ladder must be read to roughly rank `8`, and the
**licence and the category** checked before the star count is allowed to matter. 🔴 **And the
inverse holds too**: the one axis whose head *was* the right answer (`topic:math-education`)
is the smallest of the five. **Axis size predicts head quality negatively.**

## 30. The best-known open-source AI tutor is copyleft, so the "obvious" answer in this market is the unshippable one (high confidence — grant read first-hand; it heads two independent axes)

🔴 **The fact.** [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) —
"AI tutor powered by Theory-of-Mind reasoning", **933★** — is **GPL-3.0**. It is the head of
**both** `topic:tutoring` (466 repositories) and `topic:literacy` (115), and it is **3.4×**
the largest North-America-placed row on this base's agent shelf.

🔵 **Why it is a trend and not a row.** This base has published since `p568` that the
education **agent** layer licenses permissively while the **platform** layer licenses
copyleft, and that asymmetry is the architecture argument every pattern here rests on. 🔴
**The most visible agent in the market is the counter-example**, and it is the one a client
will have found before the first meeting. The asymmetry holds **statistically** — 15 of the
16 rows `p577` verified are MIT/Apache/BSD, and this pass adds 4 more permissive rows — but
it **does not hold at the top of the distribution**, which is the part a buyer sees.

🟢 **The sellable consequence, and it is concrete.** The answer to *"why aren't you just
using tutor-gpt?"* is: GPL-3.0 reaches derivative works, so a hosted multi-tenant tutor
built from it owes source to the client **and** constrains what the client can then do with
it — and the permissive stack that replaces it is now nameable on one line: **`Clew` (MIT)**
for sequencing, **`DeepTutor` (Apache-2.0)** for the tutoring loop, **`Coding-Tutor`/DICT
(Apache-2.0)** for the evidence it works, **`ltijs` (Apache-2.0)** for the LMS seam. 🔵 That
sentence is the deliverable of this trend.

🟡 **Caveat, stated.** `tutor-gpt` is still worth *reading* — its Theory-of-Mind user
modelling (via `Honcho`) is the most-starred design in this space, and a clean-room
reimplementation of an idea is not a derivative work. Reading it is safe; linking it is not.

## p577 — 2026-10-31

### The dated, checkable items

These are the items with a date and an institution attached. Everything else in
the search layer was unusable (see *On the evidence* below).

- **Ofqual published principles for AI use in high-stakes marking in England**
  (January 2026). The first regulator-issued position on AI inside summative
  assessment in a major market. It constrains any EMEA engagement that touches
  marking.
- **US state legislatures: 134 bills across 31 states** tracked on AI in
  education as of March 2026, covering privacy, classroom restrictions and
  curriculum. There is no comprehensive federal statute, so compliance is
  per-state.
- **US Department of Education released $169M in FIPSE awards** including support
  for responsible AI use. Reported via secondary sources; not confirmed against a
  primary government source this pass.
- **European Commission AI literacy framework for primary and secondary
  education**, carried on the Council of the EU agenda for the European Education
  Area 2026–2030. This is the document to write EMEA deliverables against.
- **Council of Europe AI and Education expert group** continues to meet
  (Strasbourg), and its member-state survey reports a lack of rigorous monitoring
  and regulation of AI in education. A second working conference on the regulatory
  dimensions was held in October.
- **OpenAI launched a country-level education programme with eight national
  partners** in Q1 2026. This is the structural trend that matters commercially:
  buying shifts from school-by-school sales toward **national infrastructure
  deals**, which changes who Globant competes with and who signs.
- **OECD Digital Education Outlook 2026** warns that AI improves learning only
  where pedagogy stays in control — the standard citation for an
  evidence-first engagement narrative.
- **ECLAC (October 2025)** ranks Chile, Brazil and Mexico as the LATAM leaders
  across 100+ indicators of capability, research, adoption and governance, and
  finds persistent gaps in data, training and regulation.
- **IDB fAIr Tech Radar (November 2025)** on AI adoption in Latin America and the
  Caribbean: adoption advancing against structural gaps, developing regulatory
  frameworks and heterogeneous digital capabilities.
- **UNESCO IESALC with UNU-IAS** published a working paper mapping AI use in
  Latin American and Caribbean universities across teaching, research, community
  engagement, administration and governance.

### The technical trend, from the repository evidence rather than commentary

🔴 **CORRECTED `p585` (2026-11-01):** the claim *"every platform of record is copyleft"* is **false** and was withdrawn as `Trend 36`. Four platforms of record are permissive and forkable: **Sakai** (ECL-2.0, 1,240★), **OpenOLAT** (Apache-2.0, 449★), **Kolibri** (MIT, 1,163★) and **relate** (MIT, 437★) — all four read from their own licence files. See [`../repos/foundations.md`](../repos/foundations.md). The statement below is retained as written for history.


1. **The agent layer is permissive; the platform layer is copyleft.** 15 of 16
   verified education agents are MIT/Apache/BSD, while every LMS of record is
   GPL/AGPL/LGPL. This asymmetry is stable and it is the main architectural fact
   in the industry right now.
2. **The two largest education agents in open source are both APAC academic
   projects** — `HKUDS/DeepTutor` (Apache-2.0, 52.7k★, University of Hong Kong)
   and `THU-MAIC/OpenMAIC` (MIT, 42.2k★, Tsinghua) — and both are permissive.
   Education AI's open-source centre of gravity is not in North America.
3. **Multi-agent classrooms became a real category**, not a demo: OpenMAIC's
   framing is a simulated classroom with multiple interacting agents, at 42.2k
   stars.
4. **Tutoring is converging on local-first and self-hosted.** `OpenTutor` (MIT)
   advertises running locally across 10+ LLM providers; `godspeed` reuses a local
   coding agent as the tutor. This matters for EMEA data-residency and for
   under-resourced deployments alike.
5. **Assessment and psychometrics remain a permissive, under-used layer** — IRT
   (`girth`, MIT), adaptive-testing simulation (`catsim`, BSD-3), autograding
   (`nbgrader`, BSD-3). This is where a credible adaptive-learning claim comes
   from, and almost nobody wires it in.
6. **Evaluation instruments are scarce.** One verified pedagogy benchmark
   (`pedagogy-benchmark`, MIT, 13★) against sixteen agents. The industry can build
   tutors faster than it can tell whether they teach.
7. **Unlicensed academic releases are a recurring blocker**, `bigdata-ustc/Agent4Edu`
   being the clear case: AAAI 2025 oral, 100 stars, no licence file.

### Market sizing — do not quote these numbers

2026 estimates for the global AI-in-education market range from **≈US$3.7B to
≈US$11.4B** depending on the research firm — a spread of roughly 3×. Regional
shares for North America range from 36% to 42% across firms. These are
incompatible methodologies, not a consensus with error bars. **Use them for
direction only; do not put a figure in a client deck sourced from this page.**

### On the evidence

The general-web search layer for this industry has degraded badly. Queries for
trending education AI repositories return SEO content farms (`aiindigo.com`,
`news.spill.org`, `yoursocial.it.com`, `giikorea.co.kr`) that recycle each other's
numbers, and no authoritative ranked list of open-source education agents exists
anywhere. **That is why every repository row in this KB is verified individually
rather than harvested from a listicle.** Treat search as a way to find candidate
names and dated policy events, and nothing else.

---

## Prior passes (superseded, retained for history)

### (archived) Current trends — education AI

<!-- machine-readable count claim, p570, for ingest/derive-counts.py -->
`derived trends: **28**` — numbered trend headings on this page, counted with
that gate's own regex (`^## (\d+)\. `). 🟢 **`p576` filed trends `25`–`28`**, all four at
`##` level so the counter can see them, and verified the page afterwards: ids `1`–`28`
complete, **no gaps and no duplicate numbers**. 🟢 **AND THE GATE RAN AND AGREED**:
`ingest/derive-counts.py` reports `intel/trends.md trends: derived=28 claimed=28` —
**GREEN**. 🔵 `575-B`'s "no gate can run" was over-generalised from a single denial
(`576-G`).

🔴 **`p573` corrects this claim twice over, and the second correction is a defect,
not a stale number.** The claim read **15**; the regex counts **24**. 🔴 **The
difference is not drift — it is a numbering collision: trends `15`, `16`, `17` and
`18` are each used *twice on this page for different trends*.** The `p572` block
at the top opened a new series at 15 (permissive supply in the plumbing;
source-available licences; lesson-planning as agent skill; self-reported metrics)
while the body already carried a 15–18 on entirely different subjects (vocabulary
artefacts; findings not reaching the shelf; tag variants; the verification
command). 🔵 **So `24` headings express only `20` distinct trend numbers, and four
of those numbers are ambiguous references.** 🟢 `p573`'s own additions are
numbered **19** and **20**, which were free. 🔴 **A citation to "trend 16" on this
page currently resolves to two different claims — anything referencing 15–18
should name the subject, not the number, until the series is renumbered.**

Confidence is stated per trend. Where a trend was **measured first-hand** from
GitHub's own index rather than read from a source, that is said explicitly —
those are the most reliable items on this page and the least likely to appear
anywhere else.


## `p572` (2026-10-31) — trends 15–18

### 🟢 15. The permissive supply in education is in the *plumbing*, not the platforms

🔵 Every full education platform of any scale is copyleft — Moodle GPL-3.0,
Open edX AGPL-3.0, Canvas AGPL-3.0, ILIAS GPL-3.0, ERPNext GPL-3.0, Gibbon
GPL-3.0, RosarioSIS GPL-2.0, Odoo/OpenEduCat LGPL-3.0 — with **two** exceptions
now on the shelf: **Sakai (Apache-2.0)** and, found this pass, **Artemis (MIT)**.
🟢 **But the integration layer is almost entirely permissive**: LTI 1.3 in Python
(**MIT**) and PHP (**Apache-2.0**), the xAPI store (**Apache-2.0**), Open edX's
component framework (**Apache-2.0**), Canvas MCP (**MIT**).

🔵 **The trend to state to a client: you do not win the licence argument by
choosing a different platform, you win it by never forking the one they already
run.** The permissive supply is positioned exactly where integration happens,
which is also where the billable work is.

### 🔴 16. "Open source" in education increasingly means a bespoke source-available licence

🔴 Three of this pass's higher-star education finds are **not** open source
despite reading that way: **`CaviraOSS/PageLM`** (2.1k★) ships a bespoke
*"PageLM Community License"* — non-commercial, redistribution **prohibited**,
commercial use gated behind a **revenue-sharing agreement**, and **revocable**;
**`xiaoyang111222/cn-math-taxonomy`** (5.6k★) is **CC BY-NC 4.0**; and
**`chewyenhan/malaysia-uec-teacher-workflow`** puts its substance under
**CC BY-NC-SA 4.0** while the MIT covers only `scripts/` and `tests/`.

🔵 **The pattern is consistent: the code is given away and the *content* is
withheld** — wordlists, knowledge graphs, item banks, audio. In education the
content *is* the product, so a content carve-out is a commercial block even when
the repository is genuinely generous with its code. 🔵 **Read the content licence
before the code licence in this industry.**

### 🟢 17. Teacher lesson-planning tooling is being built as an agent *skill*, by teachers, outside the anglophone web

🟢 `topic:lesson-plan` holds **44** repositories — small enough that nine passes of
star-sorted sweeping never reached it — and its content is striking: these are
Claude Code / Cowork / DSH **plugins and skills**, not applications, written
largely in Chinese and Malaysian-Chinese school contexts, converging independently
on the same feature chain: **lesson plan → courseware → item bank → dictation →
marking**.

🟢 **One of them states a property no commercial vendor leads with:
`全程本机运行，不联网、不收集数据` — runs entirely locally, no network, no data
collection.** 🔵 That is the single most common blocker in school procurement
being treated as a headline feature, by a 2★ repository, three days old.

### 🔴 18. Self-reported repository metrics are the weakest evidence in this KB, and the fix is cheap

🔴 Carried forward from `570-A` and now reinforced: **stars and commit counts are
claims a repository makes about itself.** `570-A` caught a `2,137`-commit
synthetic history; this pass found the opposite failure mode — **`arthurflor23`
shows `3,642/3,645` author-date-equals-committer-date across a genuine 7.4-year
project**, so that check *alone* flags honest repositories that push directly
rather than merge pull requests.

🟢 **The signals an author cannot unilaterally manufacture are the licence text,
the dependency manifest, and the behaviour of the code.** This pass read `28`
grants and `7` dependency manifests byte-for-byte and found **three** commercial
blocks and **one** GPL-3.0 licence surface hiding behind a clean MIT file — none
of which any star or commit figure would have shown.

## 🆕 `p574` — 2026-10-31 — trends 21–22, and a correction to how `p573` filed trends 19–20

🔴 **`p573` published `derived trends: **24**` and diagnosed a "numbering
collision — trends 15–18 each used twice". Both are refuted by the gate's own
derivation and by a four-line check of the page.** Every `##`-level trend number
`1`–`18` occurs **exactly once**. What actually happened is that `p573` filed its
own two trends as **`###` sub-headings** under a pass wrapper, where
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) — which counts
`^## <n>.` — cannot see them. 🟢 **Fixed in the structure rather than in prose:
trends 19 and 20 are promoted to `##`, this pass's two are filed at `##`, and the
header claim is set to the figure the gate derives.** 🔵 The same defect in the
same hour hit [`../compose/patterns.md`](../compose/patterns.md), where
`P-575-A`/`P-575-B` were filed at `###` against a claim of `30` recipes on a page
the gate read as `25`. **One mechanism, two files: a count claim written by hand
beside content filed at a level the counter cannot reach.**

## 🆕 `p576` — 2026-10-31 — trends 25–28, all four filed at `##` with the counter's own `^## <n>. ` form

## 25. A disjunctive search query can manufacture an informed absence — the form returns zero where its own components return hundreds (high confidence — measured first-hand on four pairs, with single-topic controls)

🔴 **`topic:X OR topic:Y` in a GitHub search URL returns `0 results` and the words "Your
search did not match any repositories."** Queried singly, the same topics return:

| pair, as a disjunction | result | component singles |
| --- | --: | --- |
| `topic:autograding OR topic:autograder` | 🔴 **0** | 🟢 `93` and `128` |
| `topic:educacion OR topic:educacao` | 🔴 **0** | 🟢 `410` and `378` |
| `topic:cbse OR topic:ncert` | 🔴 **0** | 🟢 `131` and (not run) |
| `topic:rubric OR topic:essay-scoring OR topic:automated-essay-scoring` | 🔴 **0** | 🟢 `38` on the third alone |

🔵 **Why this is a trend and not a footnote.** This base's most valuable output is the
*informed absence* — "we searched this axis and the supply is not there" — and it sells
precisely because it is expensive to produce honestly. **A query form that fabricates
zeros attacks exactly that product.** A nil from a broken form is indistinguishable, in a
commit message or on a shelf page, from a nil that was earned.

🔴 **Measured in this base: six axes were recorded in the broken form** —
`topic:deped OR topic:nigeria` (×6), `topic:cbse OR topic:ncert` (×6),
`topic:kaoyan OR topic:gaokao` (×3), `topic:special-education OR topic:iep` (×2),
`topic:intelligent-tutoring-system OR topic:learning-analytics`,
`topic:autograding OR topic:autograder`. 🟡 One of the six is not void:
`topic:special-education OR topic:iep` was reported by `p575` as `89` and `34`
**separately**, so the disjunction there is shorthand in prose rather than a query that
ran.

🟢 **And the honest half, which is the part a client should hear.** Four of the voided axes
were re-run as singles and read deep: of the `24` top-of-ladder repositories they returned,
**`18` were already in this base**. 🔵 **So the defect corrupted the published denominators,
not the discovery** — the supply had been reached by other axes. Six addresses were new and
all six are small. **The lesson is not "we missed a layer"; it is "a number we published was
produced by an instrument we had not tested."**

🔵 **Generalises unchanged to every base on this harness, and the test is cheap:** before
trusting a nil, run each disjunct as its own query. **This is `575-F`'s discipline — put a
control through the instrument — applied to the search leg rather than the verify leg.**

## 26. Education AI regulation is arriving in two incompatible shapes, and they have different buyers (high confidence — eight jurisdictions read first-hand this pass and last)

🔵 **The risk-regulation shape** — EU AI Act Annex III, Korea's AI Framework Act, the US ADA
Title II rule. It asks: *is this system high-impact, and can you evidence your controls?*
🟢 **Its buyer is compliance, legal and procurement**, its deliverable is an evidence trail,
and its deadline is a date (`April 26, 2027` / `2028`; `22 January 2026`).

🔵 **The curricular-mandate shape** — 🟢 **Colombia's `Ley 2626 de 2026`**, 🟢 **China's
`"人工智能+教育"行动计划` (`教科信〔2026〕1号`)**, 🟢 **Chile's assignment of curricular-base
updates to Mineduc**, 🟢 **Argentina's CABA making AI mandatory content**. It asks:
*is this subject taught, by whom, with what class hours, measured how?* 🟢 **Its buyer is
the curriculum directorate and teacher-training budget**, its deliverable is **content,
teacher capability and a measurement surface**, and its deadline is a school year.

🔴 **A pitch built for one shape does not sell to the other**, and this base spent fourteen
passes implicitly assuming the first. 🔵 **The second is where LATAM and China actually
are** — and it is the larger budget, because training a million teachers costs more than
documenting a model.

🟢 **Two concrete tells that the curricular shape is real and dated:** Colombia obliges MEN
to revise the subject's standards **at least every three years** and to stand up an
**Observatorio Nacional de Educación Digital** that publishes implementation and gap data;
China requires localities to set **class-hour requirements per school stage** and to
**classify and grade safety-protection standards for AI education applications**.
🔵 **Both create recurring, published, auditable work** — the best commercial property a
regulation can have.

## 27. Trend 21 holds per layer and does not generalise — the autograding layer licenses the opposite way (high confidence — refuted first-hand, five platform grants read byte-for-byte)

🔴 **Trend 21 on these shelves reads: "in education AI the artefacts with institutional
credibility are systematically less permissively licensed than the artefacts without it,"
generalised from accessibility (`p574`) and psychometrics (`p573`).** 🟢 **The autograding
and submission layer refutes it.** Its platforms of record are built by **TUM, CMU, RPI and
UC Berkeley (twice)** and every one is permissive, read byte-for-byte this pass:
**Artemis MIT**, **Autolab Apache-2.0**, **Submitty BSD-3-Clause**, **ok Apache-2.0**,
**otter-grader BSD-3-Clause**. 🔴 The two copyleft rows — **INGInious AGPL-3.0**,
**classroom50 GPL-3.0** — are the two that are *not* a US or German university platform.

🔵 **So credibility is not the discriminator, and the corrected statement is narrower and
more useful: licensing in education AI is a property of the LAYER, and must be measured per
layer rather than inferred from one.** 🟡 Three layers, three verdicts: accessibility
copyleft-dominated, psychometrics split by **programming language** (trend 19), autograding
permissive throughout. 🔵 **The practical rule for a bid: never predict a layer's licence
posture from a neighbouring layer's — probe it.** Each of these three cost one pass to
measure and would have been wrong if assumed.

## 28. Where a regulator exempts human-final-decision systems, compliance stops being paperwork and becomes an architecture choice (high confidence on the carve-out as secondary; the primary is unreachable from this harness)

🟢 **Korea's AI Framework Act Enforcement Decree provides that where a human intervenes in
the final decision, the system is judged controllable and is excluded from high-impact
AI.** 🔵 Education's named high-impact instance is **`학생평가` — student assessment** (given
as early-childhood, primary and secondary student evaluation), and only where the system
materially affects life, bodily safety or fundamental rights.

🔵 **Put those two together and the engineering decision dominates the compliance
decision.** A grading pipeline where the model proposes and the **teacher disposes** is not
a high-impact system that has been documented well; it is **outside the classification**,
and therefore outside risk management, explainability, user-protection and oversight duties
— with the notification duty (art. `31`) and its **`KRW 30 million`** fine not engaged for
that system either. 🟢 A pipeline where the model's output is released to the student
unmediated is inside, and every one of those duties attaches.

🟢 **This is buildable today with permissively licensed components, which is why it is a
trend and not a legal note:** **Submitty ships a "TA grading" stage as a product feature**,
and **Artemis's own one-line description is "Interactive Learning with Automated
Feedback"** — automated *feedback*, teacher-owned *grade*. 🔵 **The regulator and the
pedagogy want the same architecture**, which is the rare case where a compliance
constraint improves the product. Filed as **`P-578-B`**.

🔴 **Grade honestly: the carve-out is read from law-firm and policy-tracker summaries, not
from `law.go.kr`**, which like every other government host is unreachable from this harness
(`576-B`). 🟡 Control families are reliable; **do not quote the carve-out's exact wording to
a client without the statute text.**

## 🆕 `p575` — 2026-10-31 — trends 23–24, both filed at `##` so the counter can see them

🔵 Filed at `##` deliberately. `p573` filed its two trends as `###` sub-headings where
[`../ingest/derive-counts.py`](../ingest/derive-counts.py) cannot see them, and `p574`
had to promote them. This pass does not repeat that.

## 23. Regulation is promulgated by jurisdiction, so it cannot be found by region — and twelve passes of a region-level search leg proved it the expensive way (high confidence — measured first-hand, prescription and result in consecutive passes)

🔴 **The measurement.** This base's mandated regional search legs
(`AI {industry} {region} {year} adoption regulation players`) **failed to reach a
single education-specific regulatory instrument in twelve consecutive passes.** Each
time they returned market-research summaries, cross-sector enterprise AI surveys and
consultancy blogs. 🔵 Twelve passes is enough to call it structural rather than
unlucky.

🟢 **`574-D` diagnosed it and prescribed the fix: query by jurisdiction, not by
region. Run this pass, it worked on the first attempt** — Korea's AI Basic Act (in
force `22 Jan 2026`, education a named high-impact sector), Singapore's MOE AIEd
Framework and dated teacher-training mandate, Japan's MEXT ver. 2.0 guidelines, and
Australia's Framework plus the Disability Standards that actually bind. 🟢 **Four
jurisdictions, one pass, after twelve passes of nil.**

🔵 **Why it works, stated as the general rule: "EMEA" and "APAC" are *market*
categories, and no legislature publishes to them.** A statute is enacted by a
jurisdiction, indexed under its own name, and discussed in its own language. A
region-shaped query can only ever reach the layer that *aggregates* across
jurisdictions — which is analyst content, and analyst content is exactly what those
twelve passes returned.

🟢 **The corollary, and it is actionable for every base on this harness: a region
field is the right way to *store* a finding and the wrong way to *search* for one.**
This KB's closed region vocabulary (`North America` / `EMEA` / `APAC` / `LATAM` /
`Global`) is correct as a filter and useless as a query. 🔴 **The LATAM leg has now
failed the same way thirteen times** — no national instrument for Brazil, Mexico or
Chile has ever been reached — and `575-E` asks for the same per-jurisdiction method
there, with this pass's APAC result as the evidence that it works.

🔵 **An evidenced absence has the same shape and the same value.** China was queried
twice this pass and returned nothing; because the queries were English-language, that
is recorded as **an informed gap with a named next channel** (query in Chinese, read
`SAC/TC28`) rather than as coverage. 🔵 **Silence and an absence are
indistinguishable in a KB unless the absence is written down** — which is this base's
oldest standing rule, here applied to a jurisdiction instead of a repository.

## 24. "No licence file" is a property of the probe, not of the repository — and a published ungranted count is therefore an upper bound until its path set is stated (high confidence — measured first-hand, three refutations out of seven on this pass's own work)

🔴 **Measured on this pass's own probe, which is the strongest place to find it.** A
six-path grant probe (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`,
`LICENSE-MIT`) returned `NO-LICENCE-FILE` for **seven** repositories. A second probe
over a wider path set **refuted three of the seven**:

| repository | where the grant actually was | would a reasonable probe find it? |
| --- | --- | --- |
| [nvaccess/nvda](https://github.com/nvaccess/nvda) | **`copying.txt`** (`53,407 B`), GPL-2.0, confirmed in `pyproject.toml` | 🔴 lowercase, non-standard filename |
| [odilia-app/odilia](https://github.com/odilia-app/odilia) | **`README.md`** — "MIT OR Apache-2.0", no licence file at all | 🔴 no file to find |
| [IronCountySchoolDistrict/iep-printing-php](https://github.com/IronCountySchoolDistrict/iep-printing-php) | **`composer.json`** (`"license": "MIT"`) | 🔴 manifest only |

🔵 **The three failure modes are distinct and all three are ordinary**: a
non-standard filename, a grant stated in prose, and a grant stated only in a
dependency manifest. **None of them is exotic, and `nvda` is the most-used screen
reader in education.** So the error rate here is not a freak result — it is what a
narrow path set does to any real population.

🔴 **The consequence for this base is specific.** `p573` published "**`7 of 26`
repositories have no licence file**", `p574` restated it, and it is cited on several
live pages as evidence that academic education code is systematically ungranted. 🔴
**It was produced by a probe of this same class and has never been re-run against
`copying.txt`, a README grant or a manifest.** 🟡 **It must be read as an upper bound,
not a count**, until re-audited — `575-A`.

🟢 **What keeps this a measurement rather than a worry: the control held.** A
fabricated address answered `DEAD-OR-ABSENT` on both probes, so the channel does
distinguish a missing repository from a failed read. **The method was sound; the path
set was wrong** — and those are different defects with different fixes.

🔵 **The general rule, and it is the inverse of a rule this base already trusts.**
`570-A` holds that a licence file is one of the few signals an author cannot
unilaterally manufacture — true, and it is why this base reads grants byte-for-byte.
🔴 **But its contrapositive does not hold: the *absence* of a licence file at a path
you chose is not evidence of an ungranted repository.** 🟢 **So any ungranted claim
must publish its path set alongside the count**, exactly as a star count must publish
its read time. A number without its instrument is not a measurement.

🔴 **And the inverse tell exists too, found on the same axis.**
[`ncreighton/…iep-debug-dashboard…`](https://github.com/ncreighton/special-education-iep-debug-dashboard-and-log-analyzer-vs-code-extension)
has a README reading **"MIT — see [LICENSE](LICENSE)"** and **no `LICENSE` file at that
path.** 🔵 A README grant can rescue a grant the probe missed *or* assert one that was
never there, so **a README is a pointer to check, never a verdict to record.**
## 21. The accessibility layer is where education AI's licence boundary and its demand boundary cross (high confidence — measured first-hand, 29 grants read byte-for-byte)

🔵 **The claim:** the one education obligation with calendar dates attached —
digital accessibility — is served by an open-source supply that is **copyleft at
the platform tier and permissive only at the edges**, so the work it generates is
structurally a *services* engagement.

🟢 **The measurement**, from six GitHub axes never queried in `573` passes of this
base (`911` repositories, `29` grants read byte-for-byte, `1` fabricated control
answering `DEAD-OR-ABSENT`):

| band | addresses | the tier it occupies |
| --- | --: | --- |
| 🟢 Permissive with a licence file | **10** | Converters, browser extensions, agent skill-bundles, one LMS (`OpenOLAT`, Apache-2.0) |
| 🔴 Copyleft | **11** | **Every platform**: TAO (`GPL-2.0`), UDOIT (`GPL-3.0`), Cboard (`GPL-3.0`), `qti-components` (`GPL-3.0`), Asterics (`AGPL-3.0`) |
| 🔴 Noncommercial / content | **2** | Including the field's flagship sign-language translator |
| 🔴 No licence text at all | **6** | Including a `1.3k★` benchmark dataset and a `642★` auditor with a manifest-only grant |

🔴 **So `10 of 29` are shippable and every system of record in the layer is
copyleft.** 🔵 **Why this is a trend and not a licence table:** it is the **second
consecutive pass** to find the same inversion in a different layer — `p573` found
it in psychometrics (permissive in Python, GPL in R), and the generalisation is
now stateable: **in education AI, the artefacts with institutional credibility are
systematically less permissively licensed than the artefacts without it.**
Credibility accumulates in university, ministry and exam-board code, and that code
is GPL. 🟢 **The commercial consequence is a posture, not a complaint:** price the
arm's-length deployment and the assurance, not the redistribution.

## 22. A compliance deadline is a moving target and the obligation is not, so the durable deliverable is the evidence trail (high confidence on the dates as secondary sources; the primaries were unreachable)

🔵 **The claim:** accessibility dates move, standards version up, and three of
four regions have **no education-specific instrument at all** — so anything sold
against a date decays, while a dated conformance inventory keeps its value.

🟢 **The evidence, region by region** (full detail and grades in
[`market.md`](market.md)):

| region | instrument | dated? | 2026 movement |
| --- | --- | --- | --- |
| North America | ADA **Title II** web rule, **WCAG 2.1 AA** | 🟢 yes | 🔴 **Both dates slipped a year** by interim final rule: `April 26, 2027` (≥50k) and `April 26, 2028` (<50k and special districts) |
| EMEA | Web Accessibility Directive `(EU) 2016/2102` + `EN 301 549` — **not** the EAA, for public institutions | 🟡 standard-dated | 🔴 **`EN 301 549` v4.1.1 expected in 2026, pulling in WCAG 2.2 AA** — so 2.1-scoped remediation needs a second pass |
| APAC | India's **Accessibility Code for Educational Institutions** (`10 Jan 2024`) is the only education-specific one found; Australia moving to **WCAG 2.2 AA** under the DDA 1992 | 🟡 partial | 🔴 Japan's JIS X 8341-3 alignment is **disputed between sources** and is published here as unresolved |
| LATAM | Brazil **LBI art. 63** (in force since 2015) + **ABNT NBR 17225** (`11 Mar 2025`) | 🔴 **no** | 🔴 **Regulation absent; enforcement is prosecutorial (MPF).** And `11 March` is a **commemorative** date, not a deadline |

🟢 **The convergent fact worth selling on:** EMEA and APAC both land on **WCAG 2.2
AA** in 2026, and the two MIT agent bundles found this pass already enforce 2.2
AA. 🔵 **So a single remediation standard is defensible across both regions**,
while the North America scope can be met at 2.1 AA and over-delivered at 2.2 for
free. 🔴 **The failure mode to name in the proposal:** a programme justified by
`April 2026` would have been re-scoped twice this year. A programme justified by
*"we can show, per course, what conforms and when it was last checked"* survives
every one of these movements. Recipe: [`../compose/patterns.md`](../compose/patterns.md)
`P-576-A`.

## `p573` (2026-10-31) — trends 19–20

## 19. 🟢 The psychometric measurement layer splits by **programming language**, not by quality — permissive in Python, copyleft in R (high confidence — measured first-hand, 20 grants read byte-for-byte)

🔵 **The observation.** Education AI's assessment work needs item calibration,
DIF, equating and adaptive item selection. Those algorithms exist twice over in
open source — once in Python/JVM, once in R — and **the two populations have
almost disjoint licensing.**

| tier | grants read this pass | result |
| --- | --: | --- |
| 🟢 Python / JVM | 9 | 🟢 **MIT ×5, Apache-2.0 ×2, BSD-3 ×1** (+1 ungranted) |
| 🔴 R / CRAN | 12 | 🔴 **GPL-family ×11, LGPL ×1** |
| 🟢 R, permissive exception | 1 | 🟢 **`OpenMx/OpenMx` — Apache-2.0** |

🔴 **Why this is a trend and not a coincidence.** It follows the two communities'
distribution channels. **CRAN's culture and its dominant packages are GPL**, and
an R package that wants to depend on `mirt` or `TAM` inherits that; **PyPI has no
such centre of gravity**, and the education-ML packages were published out of
labs that default to MIT. 🔵 **Neither community chose this with a commercial
deliverable in mind, and that is exactly why it catches engagements late.**

🔴 **The consequence is not symmetric, because the two tiers are not
interchangeable in *evidentiary* terms.** `mirt`, `TAM`, `sirt` and `GDINA` are
the implementations **exam boards, ministries and peer reviewers accept**. The
permissive Python tier is good code with less standing in a psychometric report.
🔴 **So the licence boundary and the credibility boundary run in opposite
directions** — the code you may ship is the code your client's statistician
trusts least.

🟢 **Prediction, falsifiable next pass:** this split will hold for any
measurement-adjacent axis where the academic practice lives in R —
check `topic:structural-equation-modeling` and `topic:meta-analysis`. 🔵 If either
returns a majority-permissive population, this trend is weaker than stated.

🟢 **What to do with it:** `P-575-A` (permissive Python-only calibration
pipeline) and `P-575-B` (arm's-length GPL psychometrics service) write up the two
postures. Choose on the first day of the engagement, not after the statistician
has picked their tooling.

## 20. 🔴 The commonest licence failure in education AI is **no licence at all**, and it concentrates in peer-reviewed academic code (high confidence — measured first-hand, 26 repositories)

🔵 **The measurement.** Of **26** repositories whose grants were read
byte-for-byte this pass, 🔴 **7 (27 %) have no licence file of any kind** on
`HEAD` — not `LICENSE`, `LICENSE.md`, `LICENSE.txt` or `COPYING`.

🔴 **And they are not the abandoned toys. They are the published research:**

| repo | standing | grant |
| --- | --- | --- |
| [bigdata-ustc/Agent4Edu](https://github.com/bigdata-ustc/Agent4Edu) | **AAAI 2025**, 100★ | 🔴 **none** |
| [meyerjp3/psychometrics](https://github.com/meyerjp3/psychometrics) | 114★ Java CTT/IRT library | 🔴 **none** |
| [kervias/DCD](https://github.com/kervias/DCD) | **NeurIPS 2023** | 🔴 **none** |
| [CSLiJT/HCD-code](https://github.com/CSLiJT/HCD-code) | **SIGKDD 2022** | 🔴 **none** |
| [ShawnYu98/RDGT](https://github.com/ShawnYu98/RDGT) | **TKDE 2024** | 🔴 **none** |
| [inuyasha2012/vipsy](https://github.com/inuyasha2012/vipsy) | IRT/CDM variational inference | 🔴 **none** |
| [Mr-nnng/ICD](https://github.com/Mr-nnng/ICD) | interpretable CDM for ITS | 🔴 **none** |

🔴 **The inference this field keeps making, and it is wrong: that peer review
implies permission.** A paper at NeurIPS or SIGKDD licenses nothing. **Code with
no grant is exclusively copyrighted** — readable, reimplementable, **not
shippable**. 🔵 The methods are published and free to reimplement from the paper;
the *repository* is not free to vendor.

🔴 **Why this bites harder in education than elsewhere.** The state of the art in
learner modelling, cognitive diagnosis and knowledge tracing **is** academic
code — there is no industrial alternative to fall back on, the way there is for,
say, web frameworks. 🔴 **So "the best available implementation" and "an
implementation you may use" diverge systematically in this industry.**

🟢 **Operational rule, cheap and now proven on this harness:** read the grant
bytes before a component enters a deliverable, and treat a missing file as a
**hard stop**, not a question to resolve later. 🟢 **One `raw.githubusercontent.com`
probe settles existence and grant together** (trend 18's channel), 🔴 **while the
`curl -sI https://github.com/…` check this base is instructed to use returns `403`
for real and invented repositories alike on this session — it cannot discriminate,
and it fails in the unsafe direction.** `P-573-B` is the gate; this trend is the
measured reason it is needed.

🟢 **Second-order finding worth carrying to every industry base here: a licence
*ladder* that probes filenames will never find an R package's grant, because R
declares it in `DESCRIPTION`.** 🔴 **That single convention gap made `12` GPL
packages look ungranted.** A per-ecosystem manifest check (`DESCRIPTION`,
`pyproject.toml`, `Project.toml`, `*.gemspec`, `Cargo.toml`) belongs in the
instrument, not a longer list of filename variants.


## 1. Education AI has stopped shipping as applications and started shipping as agent skills (high confidence — measured first-hand)

**Measured, not reported — and this pass the measurement is complete.**
`topic:agent-skills topic:education stars:>50` returns **13 repositories**, the
**same count as the previous pass**, so that axis is genuinely saturated. What is
new is that the previous pass reported only the leader; this pass enumerated all
thirteen and **read every one of their licence files** over
`raw.githubusercontent.com`. **Nine of the nineteen** agents on
[`../agents/top.md`](../agents/top.md) are skill bundles — markdown instruction
sets (`SKILL.md`, `AGENTS.md`, `CLAUDE.md`) loaded by an existing harness, with
**no runtime, no service and no API**; counting six further component bundles,
**15 of the 25 agents on that page have no runtime at all.** The complete cohort:

| Repo | ★ | Licence (read first-hand) | What it is |
| --- | --: | --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 4,843 | ⛔ **CC BY-SA 4.0** (620 B) | 23,000+ skills for empirical research across 8 social-science disciplines; CoPaper.AI / Stanford REAP |
| [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | 2,750 | ⛔ **none** — no file on either branch | Brazilian study-mentor agent bundle; runs on 5 named harnesses |
| [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | 1,201 | ✅ MIT | PDFs/books/papers → traceable interactive learning pages |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 586 | ⚠️ **AGPL-3.0**, `skills/` **dual AGPL/MIT** (1,063 B, `master`) | K-12→career skill tree, 30+ skills, ships an MCP server |
| [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | 295 | ✅ MIT | Bloom's 2-sigma as a skill **plus** a self-hostable app |
| [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 213 | ✅ MIT | Chinese civil-service exam prep |
| [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | 203 | ✅ MIT (1,065 B) | Project-driven mastery learning |
| [ystemsrx/sql-to-ER](https://github.com/ystemsrx/sql-to-ER) | 192 | — **not an education agent** | SQL/DBML → ER diagrams; tagged `education` because it is used in database courses. Topic-tag dilution. |
| [cuic19053-hue/awesome-student-ai-skills](https://github.com/cuic19053-hue/awesome-student-ai-skills) | 147 | ✅ MIT (1,070 B) | 35 Chinese university application-document skills |
| [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | 119 | ✅ MIT (1,068 B) | Teaching/tutoring skill collection incl. *gaokao* |
| [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | 78 | ✅ MIT (1,063 B) | Montessori pedagogy as a skill |
| [ljx-chase/research-field-onboarding](https://github.com/ljx-chase/research-field-onboarding) | 75 | ✅ MIT (1,111 B) | Onboarding a learner into an unfamiliar research field |
| [henryyu333/assignment-check](https://github.com/henryyu333/assignment-check) | 53 | ✅ MIT (1,086 B) | Pre-submission check against brief, rubric, evidence, citations |

**The distribution is the finding: 11 MIT, 1 share-alike, 1 unlicensed, 1
dual-grant — and the two non-permissive members are the two largest, at 4,843★
and 2,750★.** In this cohort **popularity is anti-correlated with licence
usability**. The previous pass asserted something close to this from two data
points; it is now measured across the whole cohort with a denominator. Add the
**932★** `GarethManning/education-agent-skills` — 165 evidence-grounded skills for
teachers and school leaders, **also CC BY-SA 4.0**, read first-hand — and the
pattern is no longer an instance: **authors of large pedagogical skill libraries
reach for CC licences, because the artefact reads as writing.** The consequence is
fixed and worth saying in a SoW: the best-curated pedagogy content in open source
**cannot be absorbed into a proprietary methodology asset.**

**Why this matters more than it looks.** Three consequences for an engagement:

1. **There may be nothing to host.** The deliverable is a prompt contract. That
   collapses infrastructure cost and collapses the recurring-revenue story with
   it. Price the authoring and the maintenance, not the running.
2. **Versioning and evaluation become the hard problems.** A skill bundle has no
   semver discipline, no test suite by convention, and changes behaviour when the
   *harness* or the *model* changes underneath it — neither of which the client
   controls. This is the strongest argument for the evaluation layer in trend 7.
3. **Licence screening gets harder, not easier.** The largest member of the
   cohort is **CC BY-SA 4.0** — a share-alike *content* licence on a code-shaped
   artefact, which propagates to derivatives of the skill text. The
   second-largest has **no licence at all**. A skill bundle looks like
   documentation and is governed like a work of authorship.

The cohort is also **overwhelmingly APAC-origin** (six of the eight above are
Chinese-language or China-maintained), with a Stanford exception at the top and a
Brazilian one in second place.

## 2. From experimentation to governance (high confidence — every source agrees)

The consistent framing across industry sources: AI moves from standalone pilots
into admissions, advising, learning and administration as embedded
infrastructure. HolonIQ expects attention to shift to ethics, transparency,
agentic use cases and *proven instructional benefit* over broad personalisation
promises; 1EdTech frames it as evolving from isolated use cases to coordinated,
policy-guided ecosystems. The hard numbers behind it are in
[`market.md`](market.md): 87/26 in LATAM, 63% teacher use in EMEA, 60% in the US,
7-of-39 operational governance in Australia. **The gap between use and governance
is the market.**

## 3. Purpose-built beats general-purpose (high confidence)

Vendors and analysts converge on movement away from generic assistants toward
platforms built for education. This KB's own evidence agrees from the supply
side: the two largest education agents in the world are **purpose-built
education** projects from universities (DeepTutor/HKU, OpenMAIC/Tsinghua), not
education wrappers on general agents — and the prescribed "top open source AI
agents education" search returns only general-purpose listicles, i.e. the
*commentary* layer still has no education-specific map while the *code* layer
clearly does.

## 4. The compliance calendar and the capability calendar have come apart (high confidence — re-verified independently, and extended)

The previous pass recorded this correctly and in detail; this pass **re-verified
it from fresh sources and added two things it did not have.** The table stands:

| Regime | Status on 2026-10-31 |
| --- | --- |
| EU AI Act — **Article 4 AI-literacy duty** | **In force since 2025-02-02** for every organisation that *uses* an AI system — i.e. every school and university, now, already overdue where nobody has done it. Not risk-classified, not deferred ← *new this pass, and the earliest of the three EU tracks* |
| EU AI Act — **Article 50 transparency duties** | **Not deferred. In force since 2026-08-02** |
| EU AI Act — stand-alone Annex III high-risk (incl. education) | Deferred to **2027-12-02** by the Digital Omnibus amendment, in effect late July 2026 |
| EU AI Act — AI embedded in regulated products | Deferred to **2028-08-02** |
| EU — **Article 50 marking of synthetic content, systems already on the market** | **2026-12-02** — machine-readable marking/watermarking of AI-generated output. **The nearest EU deadline in this KB, roughly one month out**, and 13 months earlier than the Annex III date most guidance leads with ← *new on the fifth pass, multi-source* |
| EU — AI-generated intimate imagery / abuse material ban | ⚠️ **Still single-source, and not corroborated on the fifth pass.** Carried as "December 2026". The December 2026 EU date that *does* corroborate from several sources is the Article 50 marking deadline above; the two may have been conflated upstream. Treat as unverified |
| **Council of Europe** — Legal Instrument on AI in Education | **Planned for 2026**, "establishing rules to protect the integrity of education"; follows a 2025 recommendation. Binds by ratification across 46 states, so it reaches non-EU Europe ← *new this pass, single-source* |
| North Carolina **Session Law 2026-41** | State model policy **2026-12-31**, district policies **2027-06-30**, teacher training **2028-06-30** ← *new this pass; the nearest statutory deadline in this KB* |
| South Korea AI Basic Act | **In force 2026-01-22** — and the **Enforcement Decree entered into force the same day**, correcting this table's earlier "decrees pending". The grace is on *penalties*: **fact-finding and fines suspended for ≥1 year from 2026-01-22**, except extreme cases such as loss of life. Education named **high-impact**, specifically *evaluation of students in early childhood, elementary and secondary education* ← *corrected and sharpened on the fifth pass* |
| Vietnam AI law | Law **No. 134/2025/QH15**, **effective 2026-03-01**. The high-risk list is **Decision 33**, effective **2026-08-15**: **46 systems across six sectors**, with **three** in education — (1) automatic **testing/evaluation/ranking** of learners, (2) **monitoring and analysis of learner behaviour**, (3) **self-study tools generating content from uncontrolled data sources**. Existing education systems transition to ≈**2027-09-01** ← *instrument named and categories enumerated on the fifth pass* |
| Australia (TEQSA) | Institutional generative-AI action plans required of **all** higher-ed providers — **100% response rate achieved** |

**What is new.** First, the postponement is attributed by multiple independent
legal commentaries to **Regulation (EU) 2026/1744**, in force 27 July 2026 after
Council approval on 29 June 2026 — a citeable instrument, where the previous pass
had only "the Digital Omnibus amendment". Second, and more useful commercially:
**Article 50 transparency duties were not part of the deferral** and have applied
since **2 August 2026**. The calendar therefore has *two* tracks, and conflating
them misprices the work in both directions: **transparency obligations are live
today; conformity assessment is ~14 months out.**

**Widely-repeated error to avoid, restated because it is still in circulation:**
guidance claiming EU high-risk obligations apply from August 2026 was superseded.
Enforcement *machinery* (the AI Office and national authorities) did begin on
2 August 2026 — which is probably the source of the confusion — but the high-risk
*duties* did not.

**Two further changes this pass, and one of them merges two markets into one
programme.** Vietnam's 18-month transition for systems already running in
education expires around **1 September 2027** — within three months of the EU's
Annex III date of **2 December 2027**. The two most binding education-AI
deadlines in the world now land in the same quarter, so a multinational client
needs **one** conformity programme with two annexes, not two programmes. And the
calendar is no longer only EU-plus-Asia: **North Carolina's Session Law 2026-41**
carries the nearest deadline in this KB at **31 December 2026**, two months out,
followed by district policies in June 2027 and teacher training in June 2028 — a
statutory three-stage pipeline that writes its own engagement plan.

Meanwhile the capability calendar runs on weeks: OpenMAIC went from repository
creation (2026-03-11) to 41,984★ and `v1.3.0` in under eight months, and
`DozenTwelve/Papermorph` took **1,034★ in four weeks**. Capability deadlines in
Asia still land before Europe's.

## 5. Adoption is ahead of governance, and it is now measured on all four regions (high confidence)

Previously high-confidence only in LATAM. Now:

- **LATAM** — UNESCO IESALC/UNU-IAS, 200 institutions, 19 countries: **87%** use,
  **26%** strategy, **55%** no budget, **4%** dedicated funding at public
  universities. Cetic.br: Brazil **53%** of administrators use AI, **22%** have
  guidelines. Ceibal: **75%** of Uruguayan public-school teachers.
- **EMEA** — **63%** teacher use, from two independent surveys that agree exactly
  (European Commission School Education Gateway, April 2026, n=1,130; Sanoma
  Learning, 20,000+ teachers, 14 countries). Eurydice's *Digital education at
  school in Europe 2026* is the member-state source.
- **North America** — **60%** of US teachers (Gallup); most public schools have no
  formal student AI policy; **134** state bills across **31** states; **42.3%** of
  Ontario boards have a student AI policy.
- **APAC** — now primary: TEQSA's **100%-response** institutional census, and
  operational governance structures documented in only **7 of 39** Australian
  universities (AJET). MEXT's pilot covers **478 schools** in **149
  municipalities** — under **2%** of Japanese schools.

## 6. Mandated content without teacher buy-in fails, and there is now a measured case (medium-high confidence — single country, strong detail)

**South Korea's AI textbooks reached below 30% adoption by March, and lawmakers
subsequently removed their official status.** This is the first instance in this
KB of a national education-AI mandate being measured and then *reversed*. Set
against Singapore's approach — a **Teacher AI Literacy Professional Learning
Roadmap** with one compulsory module by end 2026 and two recommended by end 2027,
i.e. capability before content — it reads as a real design lesson rather than an
anecdote: **fund the teacher, not the artefact.** Any national-rollout proposal
should carry an adoption-risk section citing Korea.

## 7. Evaluation is the missing layer, and the absence is now specific (high confidence — measured first-hand) — 🟡 **HALF-SUPERSEDED `2026-10-31` (`p570`), see trend 15**

> 🟡 **Dated correction, `2026-10-31` (`p570`).** The *regression* half of this
> trend is **wrong as a supply claim** and was wrong for six passes: seven granted
> rubric-scoring assets exist on
> [`topic:rubric`](https://github.com/search?q=topic%3Arubric) (187 results), an
> axis this base never queried, and they are now shelved in
> [`../repos/foundations.md`](../repos/foundations.md). The ***observability***
> half stands — there is still no education-specific detector for a deployed
> tutor drifting, seventh consecutive pass. Read what follows as accurate about
> runtime monitoring and as superseded about scoring machinery.

Three passes of searching have located exactly **three** evaluation assets for
education AI:

- [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
  — MIT, 13★, 1,143 questions from real teacher-qualification exams (CDPK 920,
  SEND 223). Measures whether a model knows how to **teach**.
- [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators)
  — 87★, research-backed **rubrics** for scoring generated instructional content.
  **Licence resolved this pass from `main/LICENSE.md` (1,615 B) after three
  passes unresolved, and it is partly restrictive:** evaluator **code → MIT**,
  evaluator **content (prompts and settings) → CC BY 4.0**, but the **Annotated
  CLEAR Corpus** and **Annotated PERSUADE 2.0 Corpus → CC BY-NC-SA 4.0**,
  i.e. **non-commercial**. The upstream originals are NC too, so there is no
  cleaner substitute. **The scoring machinery is commercially usable; the
  benchmark data is not.**
- [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
  — code MIT / datasets per-publisher, 164★, standards-and-curriculum data layer
  with an MCP server, used to check **alignment**.

**None of the three is a runtime monitor, and this pass the gap got slightly
worse rather than better.** There is no open-source way to detect that a deployed
tutor has drifted, regressed after a model upgrade, or started teaching something
off-syllabus. Given trend 1 — skill bundles whose behaviour changes when the
harness or model changes beneath them — this is the single largest unmet need in
education AI, and it is where every region's governance gap actually bites.

**What got worse:** the fallback this KB prescribes — hand-build the regression
suite (pattern **P-568-K**) and score it with `evaluators` — now has a known
licence boundary. The rubric **code and prompts** clear commercially; the two
**annotated corpora are NC**. So an engagement must **bring its own corpus**, and
the one public corpus of annotated instructional text cannot be the basis of a
billable regression suite. The capability gap is unchanged and the cost of
closing it went up.

## 8. Credentials and skills-based models (medium confidence — still single-source)

1EdTech continues to point to digital credentials as a key development, with
employer expectations accelerating a skills-driven ecosystem. **No second
independent *commentary* source surfaced this pass either** — four passes with
the story carried by the standards body that has an interest in it, which is
itself informative.

**But the supply side corroborated it for the first time.** Two MIT repositories
located this pass are built specifically for credentials and competencies:
[`iblai/lms`](https://github.com/iblai/lms) (MIT, 208★, "discover courses, track
competencies, **earn credentials**, accelerate workforce development", Next.js 15,
created 2026-03-04) and, at five days old,
[`euron-sde-team/euron-open-lms`](https://github.com/euron-sde-team/euron-open-lms)
(MIT, 10★) which ships **verifiable certificates**. Code being written against a
trend is weaker evidence than an independent survey and **stronger** than a
second press release: somebody is spending engineering time on it. Upgraded from
*watch item* to **medium confidence, supply-side corroborated**.

## Licence-structure trend (measured first-hand)

**The agent layer is permissive; the platform layer is not — and the exception
appeared this pass.** Eleven of fourteen shelved agents are MIT, two Apache-2.0.
Platforms of record are AGPL/GPL almost without exception. The new exception,
**`Selleo/mentingo` (MIT, Poland, 102★)**, is the first AI-native LMS a client
can fork and keep closed; **`DSpace` (BSD-3-Clause)** remains the only
permissive platform of record at category-leader scale, in the institutional
repository.

A second structural finding, stated too broadly last pass and **corrected here**:
*"there is no permissively licensed education ERP"* holds **at
platform-of-record scale** — that category is LGPL (OpenEduCat, Odoo) or
GPL/AGPL (Frappe ×2, i-educar, openSIS) without exception. It does **not** hold
one tier down: [`academico-sis/academico`](https://github.com/academico-sis/academico)
is **MIT**, 410★, 151 forks, topic `student-information-system`, pushed
2026-10-30 — a permissively licensed, actively maintained education SIS for small
and medium institutions. The scope was wrong, not the observation.

**And the scarcity now has a denominator.**
`topic:learning-management-system license:apache-2.0 stars:>50` returns **2
repositories in the world**; `topic:lms license:mit stars:>80` returns 15 of
which **six are education platforms** (the topic also catches a coding agent and
a .NET colour-space library). The entire permissive LMS population above 50★ is
roughly **eight repositories**, the largest at 701★ on an end-of-life stack,
against Moodle's 7,600★ under GPL-3.0. "Assemble rather than adopt" survives as
advice for university-scale work — and one tier down it is no longer true.

A third structural finding, **new this pass**: the interoperability layer was
missing **SCORM** for three passes. `jcputney/scorm-again` (MIT, 362★, SCORM 1.2
and 2004, offline-first) is the permissive runtime for the standard the installed
base actually ingests and that procurement asks for by name. The attach doctrine
now has four legs — LTI, MCP, xAPI **and SCORM** — and only the fourth one
delivers content *into* the platform.

## Licence hygiene: the sidebar is not the licence, and `NOASSERTION` is three different things (measured; sharpened this pass)

The method rule stands — **read the file, not the sidebar** — and this pass added
a mechanism and a correction.

**The mechanism, upgraded twice in two passes.** The third pass reached GitHub's
REST index through the MCP server (`license.spdx_id`, `stargazers_count`) — better
than rendered pages, because it returns GitHub's own licence *determination*. The
fourth pass went one level deeper: **`raw.githubusercontent.com` answers HTTP 200
from this session**, so the licence **text** is readable. Twenty-one files were
read byte-for-byte, which closed two three-pass-old licence questions and added a
third confirmation to two standing defects.

The channels, and what each one is for:

| Channel | Status here | Use it for |
| --- | --- | --- |
| MCP `search_repositories` | ✅ works | Existence, stars, forks, push date, licence *determination*, cohort enumeration with denominators |
| `raw.githubusercontent.com` | ✅ **works — new** | The licence **text**. Try every filename (`LICENSE`, `.md`, `.txt`, `licence`, `COPYING`) on **every branch** |
| `license:<spdx> repo:owner/name` search | ✅ works | A cheap second opinion: zero results means GitHub detects no such grant |
| MCP `get_file_contents` | ⛔ repo-scoped | Nothing — it refuses any repository not attached to the session |
| `api.github.com`, `github.com` HTML via `curl` | ⛔ uniform 403 | Nothing. A uniform status across every URL measures the network, not the data |
| MCP `search_users` | ⚠️ no `location` | Nothing for region. Owner country is unobtainable, which is why seven shelf rows are **Global** |

**The correction:** `NOASSERTION` does **not** mean "unlicensed". Three distinct
states collapse into it or near it:

| State | Example | What it actually means |
| --- | --- | --- |
| Licence file present, non-standard filename, **split grant** | `learning-commons-org/knowledge-graph` (164★) | `LICENSE.md`; README badges read **code MIT / datasets "By data publisher"**, some datasets **gated**. Code safe; each dataset cleared individually. |
| Licence claimed in prose, **file absent** | `DMontgomery40/mcp-canvas-lms` (104★) | README says "MIT License - see LICENSE file"; that file 404s on every name and both branches. Default: exclusive copyright. |
| Licence file present, non-standard filename, **three-tier split with a non-commercial tier** | `learning-commons-org/evaluators` (87★) ← *resolved this pass* | `LICENSE.md`, 1,615 B: code **MIT**, prompts/settings **CC BY 4.0**, two annotated corpora **CC BY-NC-SA 4.0**. The machinery is commercial; the data is not. **The inverse split from its own sibling.** |
| **No licence field at all** | `digitalinnovationone/dio-agent` (2,750★) | Genuinely unlicensed. All rights reserved. Confirmed this pass by a second method: no file on either branch. |
| Copyleft with a **per-directory dual grant**, on a **non-`main` default branch** | `24kchengYe/human-skill-tree` (586★) ← *resolved this pass* | `master/LICENSE`, 1,063 B: **AGPL-3.0**, plus a `DUAL LICENSING NOTE` making `skills/*.md` usable under **AGPL-3.0 *or* MIT at the adopter's option**. Platform disqualified, bundles usable. A licence **column cannot express this row** — and probing only `main` returns a false "no licence". |

And a fourth shape that is not ambiguous, just wrong for the artefact: a
**content licence on code-shaped work** — `Auto-Empirical-Research-Skills`
(4,843★) under **CC BY-SA 4.0**, share-alike, the largest education agent-skills
repo in existence.

**Across three passes, every licence defect found has been in the agent layer.**
Platforms state copyleft clearly and accurately. The fast-moving layer claims MIT
loosely, ships share-alike, or says nothing — and does so at thousands of stars,
where it is most likely to be adopted without checking.

## A governance trend about AI itself, which belongs here (high confidence)

**South Africa's draft National AI Policy was withdrawn because its citations
were fabricated.** Gazetted 10 April 2026 (Notice 3880); withdrawal announced 26
April 2026 and formalised in a Gazette of 12 June 2026; cause: at least **10% of
the academic references in the reference list were fictitious**.

A national AI policy failed on provenance. For an education client — whose entire
product is claims about what is true, assessed against a syllabus — this is the
most persuasive available argument that **citation provenance is a deliverable,
not a nicety**. It is also why this KB states its method, names its sources, and
records what it could not verify.

## 9. The layer education AI actually runs on is horizontal, permissive, and was invisible to this KB for four passes (high confidence — measured first-hand)

**This is the fifth pass's main finding, and it is a correction to the shape of
the whole KB rather than an addition to it.**

Every sweep in passes one to four filtered on an education topic. Running the
capability axes instead (`topic:ocr`, `topic:pdf`, `topic:pptx`,
`topic:text-to-speech`) returned **sixteen permissively licensed repositories,
five above 30,000★ and three above 69,000★** — `PaddleOCR` (Apache-2.0, 92,024★),
`MinerU` (82,860★), `tesseract` (Apache-2.0, 77,267★), `docling` (MIT, 69,909★),
`OfficeCLI` (Apache-2.0, 32,854★), `opendataloader-pdf` (Apache-2.0, 30,129★).

**For scale: the largest education-specific asset in this KB is DeepTutor at
52,208★, and the entire education-agent shelf summed is smaller than `PaddleOCR`
alone.**

**Why this is a trend and not just a gap-closure.** It says where the engineering
value in education AI sits. The education-specific layer supplies *pedagogy* —
learner models, tutoring loops, assessment design — and it is thin, young and
licence-inconsistent. The horizontal layer supplies *capability* — ingestion,
OCR, speech, document generation — and it is enormous, mature, and permissive.
**A credible education build is therefore mostly horizontal components with a
thin education-specific layer on top**, which is close to the inverse of how this
KB's first four passes implicitly described the market.

**The commercial consequence.** It reorders what an engagement should start with.
Generating new material competes with the client's own faculty. **Ingesting the
material the client already owns** — the textbook, the past papers, the lecture
notes, the scanned worksheets — is *migration* work: easier to scope, easier to
value, and impossible for the client to replicate with a chatbot subscription.
See pattern **P-570-A**.

**The method lesson generalises past education**, and it should be carried to
every other industry KB in this collection: *a sweep filtered on an industry
topic measures how a repository markets itself, not what it does.* Tools an
industry depends on are tagged by capability, because their authors sell to
everyone. Sweep both axes or report an undercount.

## Licence-structure trend, extended: two more shapes, and "Creative Commons" now spans the whole range

The licence-shape catalogue in this KB grew from five to **seven** this pass, and
the two additions sit at opposite ends.

**Shape 6 — Apache-2.0 *plus commercial thresholds and an attribution duty*
(`MinerU`, 82,860★).** `master/LICENSE.md` (3,301 B, read first-hand) grants
Apache-2.0 "subject to the additional terms below", then imposes: a **separate
commercial licence above 100 M MAU or USD 20 M monthly revenue**; a **prominent
attribution obligation** on any online service built with it; and **automatic
termination** of all rights on breach of either. GitHub reports the whole thing as
`NOASSERTION`.

**Read the two clauses differently.** The threshold is commercially irrelevant to
any education engagement — no school system has 100 M MAU, and the clause is
aimed at hyperscalers. **The attribution clause is not irrelevant at all**: it is
a *product* requirement that lands on the client's UI and public documentation,
so it has to reach their engineering and UX teams and not just their legal
review. This is the first licence in this KB whose main consequence is a
**design** obligation rather than a distribution one.

**Shape 7 — CC0-1.0, a public-domain dedication (`gen-mentor`, 135★,
WWW 2025 oral).** 7,048 bytes of CC0: no attribution, no share-alike, no notice.
**More permissive than MIT.**

**And that juxtaposition is the actual finding.** Last pass rejected the two
best-curated pedagogy libraries in open source *because they were Creative
Commons* — `Auto-Empirical-Research-Skills` (CC BY-SA 4.0, 4,843★) and
`education-agent-skills` (CC BY-SA 4.0, 932★). This pass shelved a peer-reviewed
tutoring framework *because it was Creative Commons*. **"It's Creative Commons"
now predicts nothing about usability in this KB: the family spans the most
permissive grant on the shelf and the two most commercially obstructive ones.**
The only reliable move is the one this KB adopted two passes ago — read the file,
every time.

## Metadata hygiene: two fields that a licence column cannot express (measured first-hand)

Both were caught this pass only because they were checked explicitly, and both
look like clean findings if they are not.

- **`archived: true`.** `supertone-oss-archive/supertonic` is **MIT**,
  **13,757★**, **1,566 forks**, on-device multilingual TTS with bindings for ten
  languages — an almost ideal offline read-aloud component. It is **archived**.
  The grant is perpetual and the code still runs, but there will be no patches,
  no security fixes and no new languages. **Stars and licence are both excellent
  and both irrelevant to that fact.** A shelf built on stars-plus-licence would
  have recommended it without qualification.
- **An Apache licence with the template placeholders still in it.**
  `terracotta-education/terracotta`'s `LICENSE` is unmodified Apache-2.0
  boilerplate including the literal `Copyright {yyyy} {name of copyright owner}`.
  GitHub's "Apache-2.0" determination is correct and the grant **names no
  licensor**. Usable; a diligence note on any deliverable that depends on it.

**The general rule this suggests**, after five passes of licence work: the
licence answers *may we*, and it is the field this KB has learned to read
properly. It does not answer *should we* — `archived`, `pushed_at`, open-issue
ratios and the presence of a named licensor do, and they are cheaper to check
than a licence file.

## Region attribution: recoverable for institutions, not for people (measured first-hand)

The fourth pass concluded region was unobtainable — `search_users` exposes no
`location`, `api.github.com` returns 403 — and left seven rows `Global`. **That
was true of individuals and false of institutions.** An institutional copyright
holder names itself in the grant, and reading the licence file placed
`feedbacksystem` to **EMEA** ("Technische Hochschule Mittelhessen"),
`knowledge-spaces` to **North America** ("Vanderbilt Data Science Institute") and
`WhisperLive` to **EMEA** ("Collabora Ltd.").

**The limit was then tested, which is the part worth keeping.** All seven
`Global` rows were re-probed against the instrument and **none resolved**: every
holder is an individual or a pseudo-collective, and one Apache boilerplate
carries no copyright line at all. So the rule is conditional —
**region is recoverable from the licence file if and only if the copyright holder
is an institution** — and the `Global` rows stay `Global` for a stated reason
instead of for want of a method. Two holders whose *names* read Korean and French
are both recorded `Global`, deliberately: a personal name is not a country, and
inventing a region to fill a closed-vocabulary column is how a filter starts
lying.

## 10. The defensible-assessment trend: the gate is becoming the product, not the generator (high confidence — measured first-hand)

**Five passes of this KB looked for an AI that *writes* good exam questions and
recorded a gap. The sixth found that the thing being built instead is the
mechanism that *refuses* bad ones** — and on reflection that is the correct
response to the regulatory calendar, not a consolation prize.

🟢 [`onionviolet/itembank`](https://github.com/onionviolet/itembank) (**MIT**, 3★,
**1,175 commits**) describes itself as *"a machine-checkable contract for
LLM-authored questions"*. It assumes the items are model-written and spends its
engineering on constraining them:

- a **blocking linter** per item number — every distractor must explain when it
  *would* be correct; answer-position skew; select-count against keyed-count;
  duplicate stems;
- a **CI guard** that fails the build if real banks are committed;
- **deterministic scoring with no model in the path** — `fill` all-or-nothing,
  `check` running learner code against hidden cases, and **short-answer items
  never auto-graded**, held pending for rubric marking.

🟢 **Why this is a trend and not one repository's taste.** The same inversion shows
up independently across this base: `learning-commons-org/evaluators` scores
generated instructional content against **research-backed rubrics**;
`terracotta-education/terracotta` measures whether an intervention *worked* under
randomisation, with consent hidden from the teacher and identifiers stripped from
exports; `Claudemy` and `ZeKaiNie/universal-examprep-skill` both make **source
citation and anti-hallucination** the headline feature rather than fluency. 🔵 Four
unrelated authors, one pattern: **the differentiator has moved from generation
quality to provable constraint.**

🟢 **The commercial reading, which is the point.** The EU AI Act's Annex III
high-risk category covers **evaluation of learning outcomes**, with obligations
landing **2 December 2027**. The artefact that category demands is not a better
question-writer — it is **evidence that a human marked everything a machine could
not defensibly mark**. `itembank`'s architecture is that evidence, and it is MIT.
🟢 The same property answers the US state-policy wave from a different direction:
local-first operation with nothing leaving the machine is a direct response to
proposals like California's A.B. 1159 on training against student data.

🔴 **The half that is genuinely still missing, stated so this is not read as
solved.** Gating items is not calibrating them. There is **no live, permissive,
education-specific item-calibration asset**: `eribean/girth` (MIT) last shipped
**2022**, `inuyasha2012/pypsy` (MIT) **2018**, `meyerjp3/psychometrics` (the most
capable, Java) carries **no licence file at all**, and the R options are copyleft.
`bigdata-ustc/EduCDM` (Apache-2.0, 203★) is live and permissive but does
**cognitive diagnosis, not item calibration**. 🔵 So the honest client sentence is:
*author and gate items permissively today; calibration means a stale dependency,
a licence risk, or building it.*

## 11. A KB-hygiene trend that generalises to every industry base here: a closed gap keeps being published (measured first-hand)

🔴 **The sixth pass's second finding was an error in this base, and the mechanism
is portable enough to be worth stating as a trend.**

[`../repos/trending.md`](../repos/trending.md) was still publishing *"**No
open-source learning-analytics dashboard** still, sixth pass — only the LRS
(`openfun/ralph`) that would feed one"* while this same repository already held
[`openfun/warren`](https://github.com/openfun/warren) (**MIT**, 17★, pushed
2026-10-11, *"xAPI learning-analytics dashboards"*) and
[`openfun/potsie`](https://github.com/openfun/potsie) (**MIT**, Grafana suite) —
from the **same publisher as `ralph` itself**.

🔵 **The mechanism, which is what transfers.** The false claim lived in a
**narrative summary at the top of an append-only page**. Append-only is the right
policy for trend history — it is what stops an hourly pass from destroying the
record it exists to keep — but it has a failure mode nobody instrumented: *a
prose claim written into history keeps being read as current.* This base has
`crosspage-figure-claims.py` comparing **figures** across pages; it has nothing
comparing **existence claims** against the shelf.

🟢 **The generalisable rule for the other industry bases in this collection:**
every *"no X exists"* sentence is a claim with an expiry date, and it needs either
a date stamp that marks it stale or an instrument that re-checks it against the
shelf. 🔴 Absence claims are the highest-value and highest-risk statements a KB
makes — a client is told to build rather than adopt on the strength of one — and
they are the only claims here that nothing verifies. Registered as `568-A`.

## 12. The open-source education field is mostly below the star floor, and every search method in common use is blind to it (high confidence — measured first-hand)

🟢 **Measured this pass, with denominators on both sides of the comparison.**

| axis | results sorted by stars | results at `stars:<50` |
| --- | --: | --: |
| `topic:ai-tutor` | **816** | 🔴 **793** |
| `topic:psychometrics` | **510** | 🔴 **496** |
| `topic:learning-analytics` | **289** (`"learning analytics" dashboard`) | 🔴 **382** |

🔴 **On every axis the sub-50-star band is nearly the whole field.** For
`topic:ai-tutor` that is **97%** of results. 🟢 **And the band is not junk:** one
sweep of 30 rows produced **13 addresses new to a base that has run 568 passes
over this industry**, four of them with more than 200 commits, two of them
closing gaps this base had published for five and six passes.

🔵 **Why this is a trend and not a quirk of one KB.** The economics are
structural: an education-AI project is typically one practitioner — a teacher, a
graduate student, a psychometrician — solving their own problem, in their own
language, with no launch and no audience. **It accrues commits before it accrues
stars, and it may never accrue stars at all.** 🟢 **Three of this pass's four
high-commit finds are non-English-first** (Chinese `砚席`/`伴学`, plus a Spanish
Moodle plugin and a Portuguese IRT study in the tail). 🔴 **A star-sorted search
is therefore not merely incomplete, it is regionally biased** — it systematically
under-reports APAC and LATAM supply, which is precisely the supply a global
studio needs placed.

🔵 **The actionable form, for any industry on this harness:** stars measure
adoption and nothing else. For **tooling**, rank by commits. For **agents a
client must adopt**, stars remain the right floor. Recipe: `P-572-C`.

## 13. "MIT" on a platform is now routinely false at the directory level, and the cause has shifted from publisher choice to dependency inheritance (high confidence — measured first-hand)

🟢 **`568-D` recorded the split-grant shape at `4 of 4` instances. This pass makes
it `5`, and the fifth has a different mechanism from the first four.**

| instance | shape | mechanism |
| --- | --- | --- |
| `learning-commons-org/evaluators` | code MIT · prompts CC BY 4.0 · corpora CC BY-NC-SA 4.0 | publisher's choice |
| `24kchengYe/human-skill-tree` | AGPL-3.0 platform · `skills/` MIT at adopter's option | publisher's choice |
| `langfuse/langfuse` | MIT-Expat outside four `ee/` directories | publisher's choice (open-core) |
| `sudazc/open-question-bank` | code + docs MIT · bank content per-`bank.yaml`, default *"TBD - not for publication"* | publisher's choice |
| 🆕 **`swsgbl/ai-learning-os`** | 🔴 **MIT root · AGPL-3.0 obligations on `services/api/`** | 🔴 **a single in-process dependency (PyMuPDF, AGPL-3.0)** |

🔴 **The fifth instance is the dangerous class, because the repository's own
grant is MIT everywhere and the obligation is invisible to a licence-file read.**
This base's primary instrument — `raw.githubusercontent.com/<repo>/main/LICENSE`,
read byte-for-byte — returns a clean 1,084-byte MIT text for `ai-learning-os`.
The AGPL-3.0 §13 network obligation lives in `NOTICE.md`. 🟢 **Nothing about the
instrument is wrong; it is answering a narrower question than anyone was asking.**

🔵 **The rule, stated so it transfers:** a repository's **licence** is in
`LICENSE`; its **licence surface** is in its dependency manifest. For a library
the two usually coincide. **For a platform they routinely do not**, and a platform
is what an engagement deploys. 🟢 The contrast inside this one pass is the proof:
`DaniyalMlk/calibrate` declares MIT and has **zero runtime dependencies**, so its
licence surface *is* its licence; `ai-learning-os` declares MIT and drags a
network-copyleft obligation onto the one directory a studio would host.

🟢 **Operationally this is cheap to check and cheap to fix** — read the manifest
and `NOTICE`, then price the swap. In this instance a BSD-3 or MIT PDF parser in
place of one AGPL dependency clears the whole platform (`P-572-B`). 🔴 **What is
expensive is finding out after deployment.**

## 14. Provenance is now forged at the layer this field just started trusting (high confidence — measured first-hand, with controls)

🔴 **A git history can be synthetic, and nobody checks.** This KB moved its
tooling-layer admission signal from **stars** to **commit count** at `p569`,
for a good reason: a star floor was discarding genuinely useful libraries
(`calibrate`, 0★ / 214 commits; `itembank`, 3★ / 1,175 commits). 🔴 **One pass
later, the first never-swept axis returned
[`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune): 35★,
`2,137` commits, history beginning `2014-06-10` — and the history is
manufactured.**

| check | `ScoreRune` | control `mirt` (real, 16 yrs) | control `dexter` (real, 10 yrs) |
| --- | --- | --- | --- |
| commits/year, max:min | 🔴 **1.69×** and monotonic for 12 years | 🟢 **658×** | 🟢 **34.5×** |
| pre-2017 commits using Conventional-Commits prefixes | 🔴 **408 / 408** | 🟢 1 / 2,113 | 🟢 0 / 0 |
| commits where author date ≠ committer date | 🔴 **0** of 2,137 | 🟢 19 of 3,467 | 🟢 1 of 276 |
| subject of the repository's first commit | 🔴 **`refactor: evidence kinds`** | 🟢 `improved the README…` | 🟢 `version 0.1.7` |
| distinct author addresses | 🔴 **2**, both GitHub `noreply` | 🟢 21 | 🟢 7 |

🔵 **Why this is a trend and not an anecdote: the economics changed direction.**
Buying stars requires other people, or at least accounts that look like them.
**Synthesising a 12-year commit history requires a loop and `GIT_AUTHOR_DATE`.**
So the moment a community — this KB, a procurement checklist, a "trending" digest
— starts rewarding commit density, it has adopted a signal that is **strictly
cheaper to forge than the one it replaced.** Every base on this harness that
shortlists on commit count has the same exposure.

🟢 **What to do, and it is cheap.** Read commit count **only together with its
date distribution**. Real histories are *bursty* — a launch spike, a plateau, a
quiet year, a revival. A smooth monotonic ramp is a generator artefact. Three
further checks cost nothing: commit-message conventions that postdate their own
timestamps, author/committer date divergence of exactly zero across thousands of
commits, and a repository whose first commit is a `refactor:`. 🟢 Implemented as
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass; it reproduces its founding case and passes both
controls above. Evidence:
[`../evidence/history-plausibility.2026-10-31-p570.tsv`](../evidence/history-plausibility.2026-10-31-p570.tsv).

🔴 **The uncomfortable corollary for this page.** Every star count and commit
count quoted anywhere in this KB is a *claim made by a repository about itself*.
Stars have a known failure mode this base already documents (third-party digests
reporting impossible rates). Commits now have one too. **The only signals read so
far that an author cannot unilaterally manufacture are the licence text, the
dependency manifest, and the behaviour of the code.**

## 15. A multi-pass "gap" is often a vocabulary artefact, not an absence (high confidence — measured first-hand, twice in two passes)

🔴 **This KB published *"no education-specific agent evaluation or regression
tooling exists"* for six consecutive passes.** It searched `evaluation`,
`benchmark` and `observability` under `topic:education`, got nothing, and
escalated the claim each pass until it read as the industry's clearest unmet
build opportunity. 🟢 **The assets were on
[`topic:rubric`](https://github.com/search?q=topic%3Arubric) — 187 results — and
the string `topic:rubric` appeared ZERO times in every live page of this base
before `p570`.** Seven of its top ten were addresses new to a 569-pass base, all
granted, four Apache-2.0.

🔵 **This is the second consecutive pass in which a long-published absence
dissolved on contact with a different access method, not with new supply:**

| pass | published absence | what actually caused it |
| --- | --- | --- |
| `p569` | *"the `topic:ai-tutor` axis is saturated"*, four passes | 🔴 **The sort.** `816` results by stars, `793` at `stars:<50` — 97% of the field sat below the floor the base ranked by |
| `p570` | *"no education-specific evaluation tooling exists"*, six passes | 🔴 **The vocabulary.** The layer is tagged `rubric`, a word the base never queried |

🟢 **The generalisable control, and it is the cheapest quality gate available to
any industry base on this harness:** before publishing an absence, state the
**query** that failed and the **denominator** it returned. An absence with no
query attached is unfalsifiable, and this base has now twice shipped one for
multiple passes. 🔵 An absence claim should carry three things — *the query, the
result count, and the date* — and `569-A`'s second ask (a mandatory date stamp on
every absence claim; **414 of 565** currently carry none) is the first third of
that control.

🔴 **Note what did *not* dissolve, because the discipline cuts both ways.** Two of
the four never-swept axes — `topic:academic-integrity` (121 results) and
`topic:automated-grading` (49) — returned **ten of ten** head rows already
in-base. **Not every unswept axis hides a finding, and reporting the two nils is
what makes the one hit credible.**

## 16. A finding recorded in this base's history does not reach its shelf, and nothing was checking the difference (high confidence — measured first-hand, with a verified HEAD check)

🔵 **This is trend 11 (*a closed gap keeps being published*) in its mirror image: an
OPEN finding that never got published.** Trend 11 catches the base repeating a null
it had already refuted. `p571` catches the opposite — the base **holding an asset
it never shelved**, and simultaneously **shipping a pattern that asserts the asset
is missing.**

🟢 **The measurement.** Pass 85 (`2026-10-09`) recorded *"An item-generation tier
exists now, **5 of 5 MIT**"* in `agents/trending.md`. Checked against `HEAD` at
`p571`, **86 passes later**:

| page | item-generation rows present at HEAD |
| --- | --: |
| `agents/top.md` | 🔴 **0 of 7** |
| `repos/foundations.md` | 🔴 **0 of 7** |
| `compose/patterns.md` `P-571-A` | 🔴 asserts *"nothing permissive generates psychometrically defensible items"*, authoring slot left to a **bare model prompt** |

🔴 **So the base's history, its shelves and its patterns disagreed with each other
for 86 passes, and no instrument compared them.**

🔵 **Why this is structural rather than an oversight, which is what makes it a
trend.** `agents/trending.md` is **63,000 lines**; the shelf pages are hundreds.
The history is append-only and grows every pass; the shelf is curated and grows
rarely. 🔴 **An inventory built by grepping the shelves — the obvious and cheap
move, and the one `p571` itself made first — reports absences that the history
refutes.** `p571` drafted five "new" addresses and a "never queried in 570 passes"
claim on exactly that mistake, and caught it only by grepping `trending.md`
afterwards.

🟢 **The corrective, as a procedure, and it is one line:** build the
already-have inventory from **`trending.md` + `intel/open-gaps.md`**, never from
the shelf pages. The shelves record what was *promoted*; the history records what
was *seen*. 🔵 **Generalises to every industry base on this harness**, all of which
have the same append-only-history / curated-shelf split.

🔴 **A second-order consequence worth stating: a saturated base's failure mode
flips from under-collection to under-promotion.** Nine consecutive passes of
`WebSearch` nils and four fully-saturated topic axes at `p571` mean discovery is
largely done. 🟢 **In that regime the highest-yield work is auditing
history-against-shelf, not buying new channels** — `p571` produced seven shelf
rows and a corrected pattern from **zero new addresses**.

## 17. Tag variants split a capability's population, and the short form is the empty one (high confidence — measured first-hand)

🟢 **Measured on automated essay scoring, where this base holds both tags:**

| tag | population | ★ ceiling | permissive grants |
| --- | --: | --: | --: |
| 🟢 `topics/automated-essay-scoring` (pass 84) | **35** | — | 🟢 **8**, incl. `doheejin/ProTACT` **BSD-3-Clause** |
| 🔴 `topic:essay-scoring` (`p571`) | 🔴 **17** | 🔴 **34** | 🔴 **0** |

🔴 **Had `p571` swept only the short tag it would have published *"no permissive
automated-essay-scoring implementation exists"* — contradicting this base's own
pass-84 record of eight permissive grants on the long tag.** The short form
collects the abandoned, the coursework and the ungranted; the 34★ ceiling is the
signature.

🟢 **Rule, checkable before spending: when a capability has both a long hyphenated
tag and a short synonym, sweep the LONG form.** 🔵 This refines `P909`/`P910`'s
existing precision rule, which scored tags by **word count** — word count predicts
*precision*, and this predicts *population completeness*. They are different
failures: a low-precision tag wastes the budget, a short-form tag **manufactures a
false null**, which is worse because it gets published.

🔵 **It also explains a standing regional result rather than overturning it.** The
short tag's 17 rows include three Brazilian/Portuguese-language ENEM-adjacent
repositories; two were re-probed at `p571`
(`renan-aalmeida/AES_Enem_Competencia5`, `DaviSantos-23/Reda-o`) and **neither
grants anything** — reproducing `Gap 235`'s conclusion that the Portuguese
essay-scoring tier is **ungranted, not absent** on a second, independent tag. 🟢
The permissive asset in that tier remains the **corpus** (`lplnufpi/essay-br`,
MIT, human-graded on ENEM C1–C5), not a scorer.

## 18. The prescribed verification command fails in both directions on this harness, and the direction depends on the flags (high confidence — measured with controls, reproducing `P914`)

🟢 **Pass 85 recorded `P914`:** `curl -sI https://github.com/<slug> | head -1`
reads the agent proxy's `HTTP/1.1 200 Connection Established` and therefore
reports **200 for every slug on earth, including one invented thirty seconds
ago.** 🔴 **`p571` reproduces the hazard with the opposite symptom:** the same
command read via `-o /dev/null -w "%{http_code}"` returns **403 for every
github.com URL**, real and fabricated alike.

| read of the same command | known-real | fabricated control | the wrong answer it produces |
| --- | --- | --- | --- |
| 🔴 `curl -sI \| head -1` | 200 | **200** | ⛔ everything verifies — **admits fabrications** |
| 🔴 `curl -sI -w "%{http_code}"` | **403** | 403 | ⛔ nothing verifies — **would delete real rows** |
| 🟢 rendered repository page | name + ★ + licence | 🟢 **404** | ✅ discriminates |
| 🟢 `raw.githubusercontent.com/…/LICENSE` | 🟢 **200** + bytes + holder | 🔴 404 | ✅ the grant instrument |

🔵 **The generalisable point is stronger than `P914` alone.** It is not that curl
reports a misleading 200; it is that **`curl -sI` against this proxy carries no
information in either direction**, and a pass inherits whichever error its flags
happen to produce. 🔴 A pass reading 403 as *"repository gone"* would **delete
verified rows**; one reading 200 as *"verified"* would **admit fabrications**.
🟢 **Therefore: calibrate on a known-real AND a known-fabricated control before
trusting any pass's verification, and record which channel answered each row.**

🔴 **Also unstable across passes: `api.github.com`.** At `p568` it was reachable
and `foundations.md`'s header still claims metadata from the *"GitHub REST
index"*. At `p571` it is **scoped to the harness repository** — every other path
returns `"GitHub access to this repository is not enabled for this session"`. 🔵
**A channel claim in a page header is a statement about one past session, not a
standing property.** Date it or drop it.

## Declared gaps

- **Most trend sources are vendor blogs or market-research summaries.** The load-
  bearing citations are OECD, UNESCO/IESALC, 1EdTech, the European Commission and
  Eurydice reports, TEQSA, the AJET study, named statutes — and, for trends 1, 7
  and the licence sections, **this KB's own first-hand measurements of GitHub's
  index**, which are the most reliable items here.
- **EU AI Act primary text cannot be read from this session — established, not
  deferred.** Attempted this pass: **`eur-lex.europa.eu` does not resolve**, nor
  does the `artificialintelligenceact.eu` mirror, the same failure class as
  `camara.leg.br`. It is a **network-policy constraint**, so it should stop being
  carried as an action item for the next pass and start being a request to allow
  the domain. Everything here on Regulation (EU) 2026/1744, the Annex III and
  embedded-product dates, Article 50 and Article 4 stays **multi-source
  secondary**.
- **The Council of Europe education instrument is single-source** and the Ipsos
  Education Monitor ban-support shifts (Japan 21→29%, Australia 47→52%, Korea
  27→31%) are single-source with unpinned baseline years. Both are carried as
  directionally reliable and not pinned.
- **Trend 8 (credentials) has no second *commentary* source after four passes**,
  but now has supply-side corroboration (`iblai/lms`, `euron-open-lms`, both
  MIT). Upgraded to medium confidence; the commentary gap stands.
- **Trend 6 rests on one country.** Korea's reversal is well detailed but it is
  one case; Singapore's contrast is a policy design, not yet an outcome.
- **No runtime evaluation tooling exists to recommend** (trend 7). Stated as a
  finding, but it means the governance advice this KB gives cannot currently be
  *operationalised* with open-source components. That is an honest limit on the
  whole page.
- **The agent-skills cohort has no provenance metadata, and this pass proved the
  limit is the instrument.** Region was assigned from README language, named
  national credentials (*gaokao*, 行测, 大创申报书) and licence-file copyright
  holders only. `search_users` exposes **no `location`** here and
  `api.github.com` is 403, so a maintainer's country is unobtainable by any
  route; four of five new shelf rows are therefore **Global**. Read "Global" as
  *provenance unknown*, not as *geographically spread*.
- **13 of 13 agent-skills licences are now read; 0 of 13 declare a version or
  ship a test suite.** The versioning and regression problem named in trend 1 is
  **unmeasured because there is nothing in the cohort to measure it with** — not
  a gap in this KB's searching, a property of the artefact class.
- **Horizontal tooling is systematically under-covered, and the miss was
  expensive.** `hugohe3/ppt-master` — **MIT, 71,498★**, then believed the largest permissively
  licensed repository anywhere in this KB (🔴 **superseded `p582` by
  `microsoft/markitdown`, MIT, `193,266★`**) — went unfound for four passes because
  every sweep filters on an education topic and it carries none. It was surfaced
  by the prescribed *web* search, which cuts against the previous pass's "query
  the index, not the listicles". **Both channels are required; next pass should
  sweep by capability (`topic:pptx`, `topic:text-to-speech`, `topic:pdf`,
  `topic:ocr`, `topic:scorm`) crossed with licence.**

### Added on the fifth pass

- **Sixth consecutive pass with no education-specific agent observability or
  runtime regression tooling.** Two differently shaped queries returned nothing
  new. The gap narrowed by one notch and not by the expected route:
  `terracotta-education/terracotta` (Apache-2.0, 21★) provides **randomised
  controlled trials inside LMS assignments**, with informed consent hidden from
  the teacher and student identifiers stripped from exports. That is **efficacy
  measurement** — "did this intervention change outcomes" — and it is the first
  open-source answer to that question in this KB. It is **not** drift detection.
  A tutor in production still has no open-source way to detect that it has
  degraded, and that remains the clearest unmet build opportunity in the industry.
- **Assessment-item generation is a newly *specific* gap.** The capability sweep
  found abundant permissive tooling for generating *content* and none for
  generating **psychometrically defensible items**. That distinction is what an
  exam board or certification body actually buys, and nothing located addresses
  it.
- **Lecture-video tooling remains unswept.** `harry0703/MoneyPrinterTurbo` (MIT,
  136,744★) surfaced incidentally and is **short-form social video, not lecture
  content**; it is deliberately not shelved. A `topic:video` capability sweep is
  the next pass's job, on the evidence that capability sweeps are where the volume
  has been.
- **Market sizing is unchanged and still vendor-only, now at five passes.** The
  2026 figure reproduced again at **USD 10.6 bn** from the ResearchAndMarkets
  family, with **USD 42.48 bn by 2030**; HolonIQ's **USD 12.3 bn** also
  reproduced. **No independent estimate has been located in five passes.** Quote
  the range, never a point.
