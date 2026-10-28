---
industry: education
region: Global
updated: 2026-10-28
---

# Education AI — current trends

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it: T4 and T5 updated, **two new trends (T11, T12)** added, and three declared gaps
narrowed. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/trends.md`](../archive/2026-10-27-p490-pre-rewrite/trends.md).

## T1 — Adoption is finished; institutional delivery is the gap

86% of students across 16 countries already use AI. In LATAM higher ed, **92% of students and
79% of faculty** use it, while **only 30% of students** say their institution's own AI use meets
expectations. K-12 teacher use doubled in a year (25% → 53%, RAND).

**Consequence:** nobody needs to be sold on AI tutoring. The buyable thing is the institution's
*sanctioned, integrated, governed* offering. Pitch delivery and governance, not capability.

## T2 — The education platform layer is copyleft, and this is now the binding constraint

Read from bytes this pass: of 16 foundational platforms, **3 are permissive**. Moodle (GPL-3.0),
Open edX (AGPL-3.0), Canvas (AGPL-3.0) — every incumbent is GPL or AGPL. Only OpenOlat
(Apache-2.0), Kolibri (MIT) and Oppia (Apache-2.0) permit a closed derivative.

**Consequence:** platform choice is a *licensing* decision before it is a technical one. If a
client wants hosted closed SaaS, the incumbent-LMS route is unavailable and the shortlist is
three repos long.

## T3 — "Open source" claims in this market are unreliable at the family level

This pass refuted, from bytes: `frappe/lms` is **AGPL-3.0, not MIT** as currently published;
`tutor-gpt` is **GPL-3.0**; `microsoft/autogen` serves **CC BY 4.0 at `LICENSE`** with the code
grant at `LICENSE-CODE`. Star figures were off by **31×** (`educhain`: 387, not ~12,000) and ~5×
(`OATutor`: 274, not ~1,500).

**Consequence:** never accept a license or a star count from a listicle, a vendor page, or this
KB's own history. Read the grant at a pinned SHA. The reader must anchor on the **title block** —
a body scan matches the GNU preamble's cross-reference and misgrades GPLv2 as LGPL (this pass's
own first run did exactly that).

## T4 — Regulation has split into four incompatible regimes, and that is a product requirement

| Regime | Mechanism | Live date |
|---|---|---|
| EU | risk tiers; **provider** carries conformity duties | Art. 50 marking **2 Dec 2026**; high-risk **2 Dec 2027** |
| South Korea | comprehensive mandatory AI Basic Act | **22 Jan 2026** |
| China | service filing + AI-content labelling | 988 services filed by **30 Jun 2026** |
| India | IT Rules: labels + provenance markers | **20 Feb 2026** |
| **Vietnam** | AI law **+ education named a high-risk sector** (Jul 2026 decision) | law **1 Mar 2026** |
| Japan | non-binding promotion | AI Basic Plan **14 Jul 2026** |
| US | state patchwork, no federal law | varies |
| LATAM | **no statute found** | — |

**Consequence:** jurisdiction behaviour (labelling, provenance, filing, oversight gates) belongs
in configuration, not in a fork per market.

🟢 **Updated `p491`: the count of regimes naming education specifically as high-risk is now two.**
The EU (Annex III) and **Vietnam** (July 2026 decision). South Korea's Basic Act carries a grace
period putting **penalties at roughly Jan 2027**. The regimes are diverging in *timing* as well as
in *mechanism*, which strengthens the configuration argument rather than weakening it.

## T5 — The EU deadline slipped 16 months and created a window

Regulation (EU) 2026/1744 (the Digital Omnibus) moved stand-alone high-risk education systems
from **2 Aug 2026 to 2 Dec 2027**. Article 50 transparency was *not* moved.

**Consequence:** a 14-month window to arrive conformant rather than remediate.

🟢 **Updated `p491` — the chronology is now firm, the primary read is still not done.** Ten
independent secondary sources converge: EP approval **16 Jun 2026**, Council adoption
**29 Jun 2026**, OJ publication **24 Jul 2026**, in force **27 Jul 2026**. What moved is
**Chapter III, Sections 1–3 of Regulation (EU) 2024/1689**; sandboxes move to **Aug 2027** and that
duty binds Member States. **Not moved:** Article 50, the prohibitions, the GPAI obligations.
🔵 `eur-lex.europa.eu` **does not resolve from this session's network**, so the OJ text remains
unread — convergent commentary is better evidence than p490's "secondary commentary", and still
not primary. Address for the next pass: `eur-lex.europa.eu/eli/reg/2026/1744/oj`. 🟡 Many guides,
**including a live DLA Piper update**, still describe the Omnibus as under negotiation — treat any
undated AI-Act guide as wrong by default.

## T6 — Emotion recognition in education is banned outright in the EU

Prohibited since **2 Feb 2025**. Not high-risk-with-conditions: **banned**.

**Consequence:** engagement-detection, attention-tracking and sentiment features — common in
proctoring and "engagement analytics" pitches — are not shippable in the EU at any price. Check
every roadmap for them before an EMEA pitch.

## T7 — Agent tool surfaces are arriving at the LMS boundary, unevenly

Canvas has a real, maintained MCP server ([`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp),
MIT, 309★) with ~102 tools, a published prompt-injection advisory (GHSA-hmr8-mvr2-mvw5), and —
notably — source that states a confirmation token does not prove a human approved anything.
Moodle and Open edX have no equivalent at a usable star floor.

**Consequence:** Canvas engagements can start at the agent layer. Moodle/Open edX engagements
must budget the connector as build work.

## T8 — Write-capable education agents are a real safety surface, not a hypothetical

`canvas-mcp`'s tool population distinguishes read-only from destructive hints explicitly, and a
prior first-hand read of its write tools found a subset carrying **none** of its three
write-safety mechanisms — one of which writes a grade.

**Consequence:** any education agent that can write grades, enrolments or feedback needs an
effect taxonomy, an operator allowlist and content-bound confirmation **designed in**. Grades are
a high-stakes decision under both EU high-risk rules and several US state laws.

## T9 — Offline-first is a regional differentiator, not a legacy feature

Kolibri (MIT) is the only permissive offline-first platform found. Rural LATAM, Africa and parts
of APAC cannot assume connectivity, and national programmes are exactly where the public money is.

**Consequence:** for ministry-scale LATAM/APAC work, offline capability plus MIT licensing makes
Kolibri the default base — a combination nothing else on the shelf offers.

## T10 — Market sizing in this sector is not currently usable

2026 estimates span **$6.4B–$12.3B** (~2×). Two figures this KB published are retired this pass
as unsupported: the "$42.48B by 2030 / 41.5% CAGR" pair, and "LATAM $1.5B → $4.2B" (contradicted
~12× by the only current regional sizing found). One widely-quoted $11B figure is called a
"final guess" by its own author.

**Consequence:** quote ranges with the firm named, or quote nothing. Never put a single
AI-in-education market number in a client deck without a primary source.

## T11 — The education-AI evaluation instruments now exist, and 🟢 **one of them is MIT** (`p493` correction)

This reverses the shape of the sector's biggest gap. `p490` reported the tier as empty. Measured
from bytes this pass: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (45★,
**EMNLP 2025 Oral**, 3 teacher skills × 7 tasks) and
[`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) (0★, KAIST, 923 dialogues)
are real, serious, and **ship no license file at all**. MathTutorBench's README contradicts itself —
badge `CC BY 4.0`, closing line `CC BY-SA 4.0` — and **neither is a software grant**; Creative
Commons advises against CC licenses for code, and one of the two is copyleft.

🔴 **`p493` — the "not one of them is licensed" claim in this trend's title and body is false.**
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) is
**MIT** (1 064 B, `sha1 ac3710f1a312`, read at `21a43a395ab4`; sidebar and README agree). It is
education-specific and substantive: **1,143 questions from teacher-qualification exams**, split
**920 CDPK** (cross-domain pedagogical knowledge) and **223 SEND** (special educational needs and
disabilities), with harness support for *"100+ models"*, behind *Benchmarking the Pedagogical
Knowledge of Large Language Models* (`arXiv:2506.18710`). 🔵 **It was read by this KB on
`2026-10-18` and dropped from the shelf by `p490`'s rewrite** — so this trend was built on an
incomplete shelf, not on an incomplete sector. See [`agents/trending.md`](../agents/trending.md)
`p493`.

**Consequence, restated.** The tier is **small and under-starred, not unlicensed**:

- 🟢 **Takeable now:** `pedagogy-benchmark` — **MIT**, so the exam-derived item bank *and* the
  multi-model harness are usable as code and data, not merely readable as a paper.
  🔴 **13★, 5 commits, no security process** — a corpus and a baseline, not a maintained
  dependency.
- 🔴 **Still blocked by licensing:** `mathtutorbench` (45★) and `TutorCaseBench` (0★) ship no grant
  at all. Their papers are readable and their *task designs* reimplementable; their repositories
  are not usable. MathTutorBench's self-contradicting README (badge `CC BY 4.0`, closing line
  `CC BY-SA 4.0`) stands as recorded, and neither is a software grant.
- 🟢 **So the eval capability is no longer a build from nothing, and no longer a build from a bare
  runtime either.** Start from `pedagogy-benchmark`'s MIT items and harness, keep
  [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness)
  (**MIT**, 14,300★, 1,066 B) underneath, and implement the two unlicensed instruments' published
  task designs on top.

🟢 **Why this matters commercially, unchanged and now cheaper to reach:** this is still the
clearest open-source credibility asset in the sector, and EU high-risk conformity will demand
exactly this evidence by **2 Dec 2027**. `p493` moves the starting line, not the deadline.

## T12 — A national AI mandate is not a durable demand floor: South Korea de-mandated one

South Korea planned **mandatory AI digital textbooks from 2025**. Adoption sat **below 30% by
March**, and in **August 2026 the National Assembly stripped them of official textbook status.**
Meanwhile China runs the opposite experiment successfully — **AI compulsory from age six since
Sept 2025**, with provincial contact hours (**Beijing 8 h/year**; **Guangdong 6 h**, rising to
**1 h/fortnight in grades 10–11**).

**Consequence:** government mandates in this sector are reversible within roughly a year, and
low adoption is the mechanism that reverses them. Two things follow for public-sector work.
**Price and stage it to survive de-mandating** — no engagement economics that only clear if a
mandate persists for its full term. And **treat teacher adoption as the contractual risk**, not
procurement: Korea's mandate did not fail on policy or technology, it failed at under-30% uptake.
That makes change management and teacher training the load-bearing deliverable, which is also the
part most often cut from a bid to win it.

## Declared gaps

- **EMEA: adoption gap partly closed, vendor-share gap still open.** `p491` added European sizing
  (**$2.64B 2026 → $8.0B 2030, 31.9% CAGR**), the first named K-12 leaders (**Finland, Estonia,
  Netherlands**), and a governance contrast (**~70%** of institutions in Europe/NA have AI guidance
  vs **45%** in LATAM & the Caribbean). 🔵 Still **no vendor-by-vendor European market share** —
  searched again this pass, still absent.
- **APAC: mandate structure now documented, adoption rates and vendor share still missing.**
  `p491` added China's compulsory-subject mandate and provincial contact hours, Korea's textbook
  reversal, Japan's 2030 digital-textbook horizon and Vietnam's high-risk education classification.
  🔵 Still **no institution-level adoption rate** for China, India or Japan and **no edtech vendor
  share for any APAC market**.
- **LATAM: still no AI-in-education statute in force — now with the reason.** Brazil's
  **PL 2338/2023** passed the Senate **10 Dec 2024**, reached the Chamber **17 Mar 2025**, and is
  **still in special committee awaiting the rapporteur's report** as of Oct 2026; an end-May 2026
  plenary vote did not happen. 🟡 Whether it names education high-risk is **claimed by one vendor
  blog and unconfirmed** — the sources describing its risk tiers do not mention education. Mexico:
  nothing found, again.
- **No *usable* education-AI evaluation harness exists — restated, not closed.** See **T11**: the
  instruments exist and **carry no license**. This is still the largest structural gap in the sector
  and the clearest build opportunity; what changed is that the obstacle is now known to be
  licensing rather than absence, and a permissive runtime base (`lm-evaluation-harness`, MIT)
  has been identified.
- **No maintenance signal for any repo on these shelves.** Stars and license bytes are readable on
  this session's channels; **latest-commit dates are not** (`api.github.com` is 403 for unattached
  repos, and page fetches returned commit counts without dates on every repo tried this pass). No
  file in this KB can currently distinguish an actively maintained project from an abandoned one —
  which matters most for the small rows, where abandonment is likeliest.


## 🆕 `p492` — `2026-10-28` — two trends move from thesis to evidence

### 🔴 `T8` is now closed: write-capable education agents are a demonstrated safety surface

`T8` has argued since it was written that this is "a real safety surface, not a hypothetical."
**That argument is over.** [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) — the single
most deployable education-agent integration in this KB, and the base of pattern `P490-1` — now
publishes **four** security advisories in `v1.16.0`, where this KB had recorded **one**:

| advisory | subject | why it is the whole blast radius |
|---|---|---|
| `GHSA-7mj9-4mcg-hvhv` | **Canvas token handling** | The engagement hands this server an **institutional** Canvas API token. Read-only *tool* scoping does not protect the *token*. |
| `GHSA-7pp5-29mw-9jq3` | **local code sandbox** | Code execution reachable from an agent loop driven by **student-authored text**. |
| `GHSA-hmr8-mvr2-mvw5` | **file content fencing** | The one already carried — though upstream's words are *file content fencing*, not this KB's gloss of "prompt-injection path". |
| `GHSA-qf6c-jv93-38gv` | **Windows download permissions** | Low relevance on Linux hosting; still live. |

🟢 **The useful generalisation.** Four CVE-class advisories on a **309★, MIT, actively maintained,
security-policy-carrying** project is not a sign of a bad project — it is the **opposite**. It is
what a project looks like when it takes an exposed surface seriously and discloses. **The trend is
that the LMS agent boundary is now understood to be a security boundary**, by the maintainers
first. Treat any education MCP server with **zero** advisories as unexamined rather than safe.

🔴 **Operational rule this yields:** on an LMS agent integration, the **credential is the primary
asset**, not the tool scope. Scope tools *and* isolate the token. `P490-1` is amended accordingly.

### 🟢 `T2` holds, but the permissive numerator moved for the first time in three passes

`T2` ("the education platform layer is copyleft, and this is now the binding constraint") **stands
— 16 of 20 platforms are copyleft.** The correction is narrow and worth carrying:
[`apache/openmeetings`](https://github.com/apache/openmeetings) is **Apache-2.0** (51 425 B) at
**688★**, giving the **virtual-classroom** layer its first permissive option. The census goes
**19 → 20 platforms, 3 → 4 permissive**.

🔵 **It changes no conclusion.** No permissive **SIS** exists; no permissive **assessment/QTI**
engine exists; the only permissive **full LMS** is still `OpenOLAT`. And BigBlueButton (LGPL-3.0)
is **13×** OpenMeetings' size and stays the default. **The constraint is intact; one cell in it is
not as tight as this KB claimed.**

### 🟢 A new trend, `T13` — the education agent-skills tier is consolidating off hosted infrastructure

[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
(**917★**, `v3.1.0` dated **2026-10-22**) is **retiring its hosted public MCP service** in favour of
a **local MCP server**, with hosted access now gated behind an **auth token**. It ships composition
for **Claude, OpenAI Codex and Hermes Agent**, plus a portable ZIP edition — **165 skills across 20
domains**, of which domain 20 is **13 student-facing** skills.

**Two things to take from this:**

1. 🔴 **Its licence is `CC BY-SA 4.0` — content copyleft with ShareAlike, not a software grant.**
   ShareAlike propagates to *adapted* material, so lesson plans, rubrics and curriculum **derived**
   from these skills inherit the obligation. **Read it; do not ship it inside a proprietary
   deliverable.** That is a licence conclusion, not a quality judgement — the skills are
   evidence-graded and good.
2. 🟢 **The direction of travel is local, not hosted.** The largest education skills library in
   existence is moving *away* from a hosted endpoint. Anyone who demoed against the hosted MCP URL
   has a **migration**, not a config change. Design education-agent work for a **locally-run MCP
   server** by default.

### 🟢 Channel and method corrections (they belong in this file too)

- 🟢 **A standing gap in three files was overstated.** "No maintenance signal is available for any
  row" is **false for repos that tag releases** — release names and dates read fine via page fetch
  (`v1.16.0`, `v1.6.15` `2026-10-19`, `v3.1.0` `2026-10-22`, `v9.1.0`). **Liveness is readable.**
  Only untagged repos lack a signal.
- 🔵 **The `github.com` `curl` `403` is this session's own proxy access gate**, returning a JSON
  body that says so — **not** GitHub rate-limiting and **not** evidence a repo is missing. It
  carries zero information about existence. Open since `p472`, now diagnosed.
- 🔵 **Licence bytes must be measured with `curl -o file`.** `$(curl ...)` strips trailing newlines
  and undercounts by one byte, which **presents exactly as licence drift**. `p492` produced one
  byte of phantom drift this way before re-measuring. **Phantom drift is how a KB starts lying
  about licences.**
- 🔵 **Add lowercase `license` to every licence probe list.** `labmlai`'s MIT grant lives there, and
  a probe trying only `LICENSE`/`LICENSE.md` would call an MIT repo unlicensed.


## 🆕 `p493` — `2026-10-28` — a trend correction, and a method rule this KB needed

### 🔴 `T2`'s scope was too broad, and `T11` was simply wrong

Both corrections have one cause: **`p490`'s full-file rewrite of `agents/top.md`, and the earlier
rewrites of `repos/foundations.md`, deleted eight rows that previous passes had promoted** — with
no marker left behind, so the shelves then read as complete censuses. Full account and the
re-verified rows: [`agents/trending.md`](../agents/trending.md) `p493`.

| trend | published claim | `p493` |
|---|---|---|
| **`T2`** | "The education platform layer is copyleft, and this is now the binding constraint" | 🟡 **True of the LMS/SIS/assessment core only.** `OpenMAIC` (**MIT, 41,700★**, courseware), `open-tutor-ai-CE` (**BSD-3-Clause**, tutoring platform), `dolos` (**MIT**, integrity) and `pedagogy-benchmark` (**MIT**, evaluation) are all permissive and were all already in this KB. **Narrow the claim to the core; it is still true there and still binding there.** |
| **`T11`** | "not one of them is licensed" | 🔴 **False** — `pedagogy-benchmark` is MIT. Corrected in place above. |

🟢 **`T2`'s core survives and is worth restating precisely**, because the precise version is the
one that holds up in a client conversation: **the full LMS, the SIS and the assessment/QTI engine
are copyleft-bound** — `OpenOLAT` (Apache-2.0, 448★) is the only permissive full LMS, no permissive
SIS exists, no permissive QTI engine exists. Everything *above* that core now has a permissive
option. See [`repos/foundations.md`](../repos/foundations.md) `p493`.

### 🆕 `T14` — in this sector, a KB's own bookkeeping is a material source of error

Not a market trend; a trend in **how this KB fails**, recorded because it has now produced three
published falsehoods in two passes.

- `p492` declared a gap (Learning Commons licences unreadable) over evidence this KB had held since
  `p119`/`p120`. The pass searched the open web instead of `grep`-ing the repository it was editing.
- `p490`/`p491` published two "declared gaps" in `agents/top.md` that this KB's own trending log
  refuted: the permissive-agent gap (refuted by `OpenMAIC`, cited **51 times** in this KB's history)
  and the unlicensed-eval-tier gap (refuted by `pedagogy-benchmark`).
- `p492` reported the permissive platform numerator as `3 → 4` as though it were ecosystem
  movement, computed over a shelf missing eight promoted rows.

🔵 **Two rules, both cheap, both would have caught all three:**

1. **Before declaring a gap, `grep -ri` the subject across this repository.** A gap asserted over
   held evidence is worse than silence — it instructs the next pass not to look.
2. **A full-file rewrite must diff its promoted-row names against the version it replaces, and
   either carry each row forward or say why it was dropped.** The `archive/` copies make this a
   one-command check. 🔴 Without it, every rewrite is a silent data-loss event, and the shelf keeps
   reporting a census of this KB rather than of the sector.

## 🆕 `p494` — `2026-10-28` — a new trend, and two trends that need qualifying

Full narrative and reads: [`../agents/trending.md`](../agents/trending.md) `p494`;
[`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).

### 🆕 `T15` — Agentic AI now has its own governance instrument, and it is voluntary by design

🟢 **The claim.** Governance of *agentic* systems has separated from governance of AI generally, and
the first instrument written specifically for it is **voluntary**. Singapore's IMDA launched the
**Model AI Governance Framework for Agentic AI** on **22 January 2026** at the World Economic Forum
— described across multiple independent firm notes as the world's first such framework — covering
**how much autonomy an agent is granted**, **how its actions are bounded and logged**, **how humans
stay meaningfully in the loop**, and **how accountability is assigned when several agents
interact**. **AI Verify** supplies the assurance side: process checks plus technical tests.

🔵 **Why this is a trend and not a single-country fact.** Every other regime this file tracks
governs AI by **what the system decides about a person** — EU Annex III by use case, Vietnam's
Decision 33 by sector, Korea's Basic Act by high-impact domain. `T15`'s instrument governs
**how much the system is allowed to do on its own**, which is an orthogonal axis. 🔴 **No
education-specific regime anywhere has an agent-autonomy provision**, so for a multi-agent education
product this is currently the **only** published rubric that addresses its actual architecture.

🟢 **Commercial reading — this is a sales asset, not a compliance burden.** `T4` holds that
regulation has split into incompatible regimes and that the differentiator is the human-oversight
gate. `T15` says that for the agentic layer, the gate is **voluntary and therefore demonstrable**:
a vendor can design to a published rubric and point at it, rather than argue an obligation down.
🔵 And per this KB's own (previously deleted) Singapore note, vendors selling into government and
banks **are expected to point to these frameworks** — so a voluntary instrument operates as a
**procurement gate**. Pricing consequence: an agentic-conformity workstream in Singapore is a
*demonstrable-conformance* deliverable, closer in shape to EMEA's provider-conformity sale than to
APAC's jurisdiction-routing sale.

🟡 **One claim deliberately not carried.** An academic commentary (`arXiv:2608.15417`) states the
framework *"requires each agent to carry a verifiable digital identity and an audit trail"* —
which conflicts with the voluntary standing every firm note describes. 🔴 **`arxiv.org` is
`connect_rejected` by this session's egress proxy**, so it cannot be checked here. Recorded as an
open conflict. **Do not tell a client the framework imposes an agent-identity requirement.**

🔴 **How `T15` came to be written is itself the evidence for `T14`.** This was not a discovery. The
Singapore posture was in this KB at `p315` and **`p315`'s own rewrite deleted it**; HEAD mentioned
Singapore exactly once, as a ban-support percentage. `T15` exists because this pass read the KB
against its own archive, not because a search surfaced something new.

### 🔴 `T4` needs qualifying: "build conformity once in EMEA shape" is only partly true

`T4` holds that regulation has split into four incompatible regimes and that this is a product
requirement — that stands and is strengthened. 🔴 **But the corollary this KB repeats — that an
EU-conformant assessment design transfers to the other high-risk jurisdiction with little rework —
is true for one of Vietnam's three education triggers and false for the other two.**

Vietnam's Decision `33/2026/QD-TTg` names **three** education system types. `p492` recorded one:

| trigger | transfers from an EU-conformant build? |
|---|---|
| automatic **assessment, grading or ranking** of students | 🟢 **yes** — same functional trigger as EU Annex III |
| self-learning content from **uncontrolled data sources** | 🔴 **no** — a **corpus-governance** obligation. An EU-conformant build has no corpus-provenance artefact to show, and the trigger fires on **retrieval design alone**, with no grading feature in the product |
| **biometric** monitoring of learner behaviour | 🔴 **no, and the regimes point in opposite directions** |

🔴 **The biometric divergence is the sharpest regulatory asymmetry in this file, and it belongs to
`T6` as much as to `T4`.** `T6` records that the EU **bans** emotion recognition in education
outright (live since 2 Feb 2025, narrow medical/safety exception). Vietnam **permits biometric
learner monitoring as a high-risk category** — i.e. allowed, subject to conformity duties. 🟢 **This
is not stricter-versus-looser along one axis; it is a feature that must be *absent* in one
jurisdiction and *documented and governed* in the other.** A single configuration cannot satisfy
both, and no amount of EMEA conformity work produces the Vietnamese artefact. **Treat biometric
learner monitoring as a build-time jurisdiction fork, never a runtime policy flag.**

### 🟢 `T14` gains a second mode: a later pass can blunt a sharper finding

`T14` holds that in this sector a KB's own bookkeeping is a material source of error. `p493`
established the first mode — **a full-file rewrite silently drops promoted rows**. This pass adds
two more, both observed:

1. 🔴 **Rewrites drop *prose*, and prose loss is undetectable.** A dropped row can be found by
   `grep`-ing a repo URL, which is how `p493` found eight. **A dropped paragraph has no key to grep
   for** — nobody knows to look for a fact the file no longer mentions. `market.md`, `trends.md` and
   `patterns.md` are mostly prose and all have been rewritten in full.
2. 🔴 **A later pass can overwrite a precise finding with a blunter one and file the precise one as
   the defect.** `p492` resolved Vietnam's deadlines into a conditional table (the date depends on
   **when the system went live**, not what it does). `p493` re-read a secondary source that flattened
   that conditional into a single grace date, found the flat version disagreed with the KB, and
   flagged **the KB's correct entry** as unquotable, deferring it to this pass. This pass's
   independent read confirms `p492` term by term.

🔵 **Rule, as transferable as `p493`'s grep rule:** before filing a contradiction between a new read
and a KB entry, **read that entry's own pass note first.** And before a full-file rewrite, diff the
*prose* against the archive copy, not just the tables — 🔴 **this KB currently has no mechanism that
would catch a deleted paragraph, and that is the open gap this trend names.**


## 🆕 `p495` — `2026-10-28` — one new trend, and one existing trend gains its missing demand-side leg

### 🆕 `T15` — The agent surface on an incumbent system is where the security debt lands, and it lands fast

🟢 **Evidence, first-hand this pass.** [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) —
the only maintained agent surface on an incumbent LMS this KB has found, **309★**, MIT — published
**four security advisories on a single day (`2026-10-25`)**: two **High** (a sandbox escape at CVSS
**7.8** via `child_process` in `execute_typescript`; a prompt-injection path from course content to
**data disclosure and grade change**), one Moderate (**Canvas bearer token sent to a URL chosen by
the file-storage host**), one Low. 🟢 **All four patched at `v1.16.0`.**

🔵 **The trend is not "this repo is risky."** It is that **the integration layer inherits the
authority of the system it integrates with, and none of its defences.** Every advisory here is a
consequence of the agent holding a Canvas instructor token and reading attacker-reachable content:
course material a student can edit becomes an instruction channel, and a grade-write tool becomes
the payload. 🔴 **An LMS has decades of permission hardening; a six-month-old MCP server fronting it
has none of it, and the token does not care which side of the boundary it is on.**

🔴 **Three generalisations this KB will apply to every future integration row:**

1. 🔴 **A version string is not a patch.** `v1.16.0` closes the sandbox escape **only on
   Node.js ≥ 22.18**, because the fix is Node's permission model. **Right version on an old runtime
   = unpatched, reported as patched.** This is invisible to a lockfile audit.
2. 🔴 **The published fix may leave the worst path open, in writing.** The `1.16.0` advisory itself
   states that egress blocking is best-effort and **executed code can still reach the caller's
   token.** 🔵 So the mitigation that matters is **removing the capability** (disable
   `execute_typescript`) and **shrinking the credential** (scoped, short-lived token) — not upgrading.
3. 🔵 **Advisory counts must be re-read, not inherited.** `p492` recorded four IDs; `p494` flagged
   that an un-re-read count on a fast-moving repo is the one number not allowed to age; `p495`
   re-read it and the count **held at four** — but severities, CVSS and patched versions had **never**
   been read, and those are the fields that decide a deployment. **A stale count is a risk; an
   un-read severity is a bigger one.**

🔵 **Commercially this is a reason to be the integrator, not a reason to avoid the layer.** A client
cannot assess this on their own: it took a release-tag read, four advisory reads and a runtime
check to arrive at a deployable posture. 🟢 **That posture is now written down as
[`../compose/patterns.md`](../compose/patterns.md) `P495-1`** — which is a billable artefact, and is
the kind of thing an AI Studio sells that a tutor demo does not.

### 🟢 `T9` (offline-first is a regional differentiator) — the demand-side leg it was missing

`T9` and `P490-3` have been argued almost entirely from **regulation** — sovereignty rules,
data-residency, jurisdictional divergence. 🟢 **This pass's APAC return supplies a procurement
argument instead:** Forrester reads that **60% of firms and governments in major markets such as
India and China will integrate locally developed large language models**, with **education named as
a target sector**.

🔵 **Why this strengthens `T9` rather than merely repeating it.** A regulatory driver can be
repealed — `T12` already records South Korea **de-mandating** a national AI mandate, which is this
KB's own counter-example to regulation as a durable demand floor. 🟢 **A procurement *preference*
for locally developed models is not repealed; it is a buying habit.** So the architectural
requirement `T9` prescribes — **model-portability as a first-class design property**, not a
deployment detail — now has a reason to exist in jurisdictions **where no rule requires it**.
🔴 **Design consequence, unchanged but better supported: never bind a pattern to a single hosted
model.** Which is also the standing criticism of `naufaldi/teacher-exam` (MIT harness, hosted
proprietary generator) on this KB's own trending shelf.

### 🟡 `T10` (market sizing is not usable) — holds, fifth pass, with fresh contradictions

🔴 The mandated trends query returned, in one sweep: **$3.7B in 2026 → $14.1B by 2033** (Persistence),
**$10.6B in 2026 at 40.9% CAGR** (The Business Research Company), **$11.4B in 2026** (GII), and a
North America figure given once as **~$951M (2024) → ~$2.3B (2029)** and once as **"USD 26.32 MN"**.
🟢 **`T10` stands: these are marketing pages, they do not agree within a factor of three, and no
pass should quote a single figure to a client.** 🔵 Quote the **direction and the regional ordering**
instead — and in LATAM, quote the **adoption-versus-governance contrast** (`92%` student engagement
against `~30%` institutional policy coverage) which is measured, sourced and far more persuasive
than a sizing estimate.

### 🔴 Trend-adjacent method note: a trend this KB loses is a trend that never existed

🟢 `p494` proved a full-file rewrite drops prose; `p495` found a **second instance** — LATAM's
adoption instrumentation present in the KB's history and README but **absent from
`intel/market.md`**. 🔴 **This file is mostly prose and has been rewritten in full.** 🟢 **Four of its
load-bearing claims are therefore now registered in `make gate-prose-claims`** — including `T15`'s
Node floor and the EMEA adoption-rate gap — so a later rewrite that drops them **fails the build**
instead of looking like coverage.



## 🆕 `p496` — `2026-10-28` — a trend number used twice, and a new trend about the layer with the worst licence hygiene

### 🔴 Bookkeeping defect: **`T15` names two different trends**

🔴 **Found by counting headings, not by reading prose.** This file contains two sections both
numbered `T15`:

| heading | pass | subject |
|---|---|---|
| `### 🆕 T15 — Agentic AI now has its own governance instrument, and it is voluntary by design` | `p494` | a governance instrument |
| `### 🆕 T15 — The agent surface on an incumbent system is where the security debt lands, and it lands fast` | `p495` | security debt at the agent surface |

🔴 **Consequence, and it is live rather than theoretical: every cross-file reference to "`T15`" in
this KB is now ambiguous**, including the ones in `agents/top.md` and `compose/patterns.md`.
`T13` and `T14` were each introduced inside a pass section the same way, so the numbering has no
single registry to collide against — which is how `p495` reached `T15` without noticing `p494` had
taken it.

🟢 **Resolution, chosen to avoid breaking existing references.** Neither section is renumbered —
renaming them would silently invalidate every citation already written. Instead both are
**disambiguated by suffix** from here on:

- **`T15-GOV`** — the voluntary agentic-AI governance instrument (`p494`).
- **`T15-SEC`** — security debt at the agent surface of an incumbent system (`p495`).

🔵 **And the next free number is `T16`**, used below. 🔴 **Standing instruction: a pass introducing a
trend must `grep -n "^## T\|^### 🆕 \`\?T" intel/trends.md` first.** This is `T14` applying to
itself — the defect was in the registry, not in anyone's reading.

### 🆕 `T16` — The layer with the highest legal exposure in education has the **worst licence hygiene**, and the two facts are connected

🟢 **Measured this pass, from bytes.** Discovery produced **eight addresses absent from all 5,547
files** in this KB, all in special education and rubric grading. The grant split:

| grant at pinned SHA | count | addresses |
|---|---|---|
| 🟢 **MIT** | **3** | `jscott5811/IEP-and-Section-504-Plans-Skill` (1 068 B), `rtwergrfh-cmyk/iep` (1 080 B), `SahilC/AutomaticEssayGrading` (1 074 B) |
| 🔴 **no licence at six filenames** | **5** | `SudhanvaJ-bit/project-samarth`, `kennedyraju55/essay-grader`, `avivkatz1/easy-iep`, `victor-lubn/Special-Education-Planning`, `marckurniawan/essay-scoring-project` |

🔴 **Five of eight — 62.5% — carry no grant**, each confirmed with `README.md → 200` at the same SHA
so the tree was demonstrably reached. **Compare the general education-agent layer, where this KB's
permissive tier is concentrated but real** (`DeepTutor` 46.0k Apache-2.0, `OpenMAIC` 41.7k MIT).
🔵 **The special-education layer inverts that: supply exists, grants do not.**

🟢 **The mechanism, and it is the part worth briefing.** These are the repositories of **practitioners
and parents**, not of labs or vendors — a special-education teacher, a district employee, a family
advocate, shipping 1 to 32 commits to solve their own problem. 🔴 **People in that position publish
to help, and a licence file is an artefact of intending redistribution.** So the layer governed by
the *strictest* statutes — **IDEA**, **Section 504**, **FERPA**, Illinois **SOPPA**, India's **RPwD
Act** — is also the layer where almost nothing can lawfully be reused.

🔴 **Why this is a commercial trend and not a curiosity.** The failure mode is specific: a search
returns a tool that does exactly what a district needs, it is public on GitHub, the engagement
assumes "open source", and **there is no grant** — so the build is unlicensed from day one, in the
one domain where a compliance review is certain to happen. 🔵 **`T3` ("open source" claims are
unreliable at the family level) said the *family* is often misstated. `T16` is sharper and worse:
here there is often no licence at all**, and this pass caught the search channel asserting
*"MIT-licensed"* for `kennedyraju55/essay-grader`, which has none.

🟢 **What to do with it on an engagement:** treat this layer as **read-only reference** by default.
The three MIT assets are knowledge packs and a deterministic renderer — they compose
([`P496-1`](../compose/patterns.md)) but they do not add up to a product. 🔴 **There is no
special-education platform, open or permissive, at all** (see
[`../verticals/solutions.md`](../verticals/solutions.md) `p496`), so the system of record stays the
district's and Globant builds beside it.

### 🟢 `T9` (offline-first is a regional differentiator) — its cleanest instance yet, and it is not regional

[`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) (MIT, 1 080 B, `sha1 fb30401f6782`)
runs **entirely in the browser with no server and no AI service** — rules-only IEP→plain-language
rendering. 🟢 **Offline by construction rather than by configuration**, which is the strongest form
of the `T9` argument this KB holds.

🔵 **And it extends `T9` past its regional framing.** This file has argued offline-first as a
*LATAM/APAC connectivity* differentiator. Here the driver is **data sensitivity in a high-income
market**: an IEP is among the most protected records a school holds, and a tool that never transmits
it answers the egress objection **architecturally instead of contractually**. 🟢 **So offline-first
is now two arguments — connectivity where bandwidth is the constraint, and non-egress where privacy
law is** — and the second one sells in North America and EMEA.

### 🟡 `T10` (market sizing is not usable) — holds, sixth pass, with the contradiction inside one query

🔴 A single mandated trends query returned **three figures for the same year**: **$3.7bn**,
**$10.6bn** and **$11.4bn** for 2026, with CAGRs from **15.9%** to **46.12%**, plus disagreement on
the leading segment (one source: higher education largest; another: K-12 at **45.62%**). 🟢 **`T10`
does not need restating so much as it needs the replacement**, which this pass has: the
**governance gap**, now measured independently in two regions — **26%** of LATAM institutions with a
formal AI strategy, **10%** of North American institutions with formal AI guidelines. 🔵 **Two
instruments, two sources, one conclusion**, and unlike the dollar figures it has been stable across
passes.

## 🆕 `p497` — `2026-10-28` — a new trend, `T16` qualified, and the registry grep from `p496` **fails on its own file**

### 🔴 The standing instruction's own grep misses a trend

`p496` left this file a standing instruction: *"a pass introducing a trend must
`grep -n "^## T\|^### 🆕 \`\?T" intel/trends.md` first."* 🟢 **Run, as instructed.** It returns
`T1`–`T12`, `T14`, `T15` (twice), `T16` — and **not `T13`**.

🔴 **`T13` exists.** It is at line 255, headed
`### 🟢 A new trend, \`T13\` — the education agent-skills tier is consolidating off hosted
infrastructure`. The pattern requires `🆕` immediately after `###`; `T13`'s heading uses `🟢` and
the words *"A new trend,"* before the number, so the registry check **cannot see it**.

🔴 **Consequence:** a pass obeying `p496`'s instruction exactly would read the highest number as
`T16` and could reasonably conclude `T13` was free — reintroducing the precise collision `p496`
spent a section resolving. 🟢 **Fix, and it replaces the old instruction:**

> `grep -no "T[0-9]\+" intel/trends.md | sort -u -t: -k2` — pattern-free, so heading decoration
> cannot defeat it.

🟢 **Run before being recommended** — because proposing an unverified checker is the defect this
section is about. Output:

```
T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T137 T148
```

🟢 **`T13` is visible (7 occurrences), the full `T1`–`T18` range resolves, and the `T1xx` series from
[`agents/trending.md`](../agents/trending.md) shows up too** — which is a bonus: the checker surfaces
the second registry's numbers, so a future collision between the two ranges would be visible at the
moment a trend is introduced.

🔵 **This is `T14` applying to itself for the second consecutive pass.** `p496` found the registry
defective and wrote a checker with the same class of defect: **a validator built from the convention
it is validating inherits the convention's blind spots.** The replacement greps for the *number*,
never the decoration. 🔵 **Note also that this KB runs two independent trend registries** — `T1`–`T17`
in this file, and a `T1xx` series in [`agents/trending.md`](../agents/trending.md) (`T137`, `T148`).
They do not collide today because the ranges are disjoint, but nothing enforces that.

### 🟡 `T16` needs qualifying after one pass

`T16` (`p496`) states that the layer with the highest legal exposure in education has the **worst
licence hygiene**, from a sample where **five of eight** new addresses carried no grant.

🔴 **This pass's sample points the other way.** Three new addresses in the same high-exposure
territory — the EU Annex III functions — split: **`ASUCICREPO/Admissions-AI-Agent` MIT**,
**`TaiRuiQu/oh-my-paper` MIT**, and the only unlicensed one a **2★ handwriting script** sitting
*below* the regulated layer rather than in it.

🟡 **`T16` is therefore downgraded from a sector characteristic to a sample observation.** Eleven
addresses across two passes support neither direction. 🟢 **What survives, and is worth carrying to a
client:** licence hygiene in this sector's long tail is **unpredictable per repository and
uncorrelated with how regulated the function is** — which is the operational reason every row in
this KB is read from bytes rather than from a badge, a listicle or an API field.

### 🆕 `T17` — This KB's enumeration of *ranked* education-AI supply is ~95% complete, so discovery spend should move to drift and function queries

🟢 **Measured, not asserted.** Five ranked discovery axes run through a star-ordered channel this KB
had declared unavailable: `topic:ai-tutor`, `topic:ai-education`, `topic:knowledge-tracing`,
`topic:student-information-system`, `topic:proctoring`+`topic:automated-grading`. **59 addresses
pulled, 56 already on these shelves — 94.9%.** Census:
[`saturation-census.2026-10-28-p497.tsv`](../evidence/saturation-census.2026-10-28-p497.tsv).

🔴 **The two axes that *are* this sector returned zero.** `topic:ai-tutor` and `topic:ai-education`,
at every star level down to 100★, produced **nothing** this KB does not hold; several hits appear in
**200+ files** here.

🟢 **All three new addresses came from the administrative layer** — proctoring, grading, admissions.
`p496` reached the same place from `IEP`/`accommodations`/`rubric`. **Two passes, independent query
sets, one answer.**

**Consequences, which are budget decisions:**

1. 🔴 **Ranking legs are spent.** The brief's keyword-and-star queries have returned nothing new for
   **six** consecutive passes, and this pass shows that is a property of the supply, not of the
   query — a *better* ranking channel found the same ceiling.
2. 🟢 **Function-shaped administrative queries are the only productive discovery channel.** Spend
   there: placement, scheduling, degree audit, credentialing, attendance, early-warning, accessibility.
3. 🟢 **Re-verification now outranks discovery.** With supply enumerated, the KB's value is in pins,
   licence bytes, security floors and drift — where `p495` (a security floor), `p496` (a reader
   defect) and this pass (`rosariosis`'s `mobile` default ref) each found something real.

🔵 **Scope limit, stated so this does not harden into dogma.** 94.9% is saturation **of the ranked,
starred, topic-tagged population**. It says nothing about repositories that are new, untagged,
unstarred or not in English — and `oh-my-paper`, found this pass at **1★** with a Chinese-language UI
on a `v2` default branch, is exactly the kind of address this measurement cannot see.

### 🆕 `T18` — The four functions regulators designate as high-risk are the four with the thinnest open-source supply

🟢 **The convergence is this pass's commercial finding.** Every regime examined names substantially
the same functions: the EU AI Act **Annex III point 3** (admissions, grading, placement, exam
proctoring); **Vietnam's Decision 33/2026/QD-TTg** (education among six high-risk sectors, naming
automated assessment); US states legislating district AI policy over the same decisions.

🔴 **Supply, measured against that list** ([`verticals/solutions.md`](../verticals/solutions.md)
`p497`):

| designated function | permissive open-source supply |
|---|---|
| Admissions | 🔴 **one** asset, **5★**, found `p497` (MIT, ASU) — and it is AWS-Bedrock-bound |
| Grading | 🟡 thin — `oh-my-paper` (MIT, 1★); `dolos` is MIT and maintained but detects plagiarism, not grades |
| Placement | 🔴 **nothing**, in any pass |
| Exam proctoring | 🔴 **nothing permissive** out of **145** repositories on `topic:proctoring` |

🟢 **Read together with `T5`** (the EU's 16-month slip to **2 December 2027**) **this is the sector's
clearest build signal**: a dated compliance runway on functions where there is almost nothing to
buy, fork, or compose. 🔴 **And the inverse warning:** a client who expects to *assemble* an
admissions or proctoring capability from open source will not find the parts. Price those as builds.
Recipe: [`compose/patterns.md`](../compose/patterns.md) `P497-1`.

---

## 🆕 `p498` — `2026-10-28` — a new trend about licence *text*, `T17` **refuted**, `T3` promoted from pattern to replicated property, and `T10` given its decisive measurement

### 🔴 `T17` — **refuted by this pass's own measurement**

🔵 `p497` published `T17`: *"this KB's enumeration of **ranked** education-AI supply is ~95%
complete, so discovery spend should move to drift and function queries."* It rested on 59 ranked
addresses across five topic axes, **56 already shelved**.

🔴 **One axis `p497` did not run — `topic:edtech` `stars:>400` — returns 13 ranked addresses of
which 9 are absent from every shelf: 69.2% novelty against `T17`'s 5.1%.** And the axis was not
unknown: **`p480` censused `topic:edtech` ≥50★ at 64 repositories, six passes earlier, and never
enumerated them.**

🔴 **`T17` is withdrawn as a trend.** It measured the five axes `p497` chose, not ranked supply.
🟢 **What survives is narrower and still useful:** the axes that name this sector directly
(`topic:ai-tutor`, `topic:ai-education`, `topic:knowledge-tracing`) *are* enumerated, and `p497`'s
finding that productive discovery now comes from **function-shaped** queries (proctoring, grading,
admissions, IEP) held again this pass — every new address came from a generic-platform axis or a
function axis, none from a sector-named one. 🔵 **The correct standing instruction is not "ranked
discovery is finished" but "ranked discovery on sector-named topics is finished; generic and
function axes are not, and at least 51 counted rows remain unread" (`Gap 498-A`).**

### 🔴 `T19` — Education-AI licence **text** is edited in the field, and the edits are inside the operative body

🔵 `T3` says *"open source" claims in this market are unreliable at the family level* — a repo
calling itself Apache may be AGPL, a repo calling itself open source may carry a bespoke licence.
🔴 **`T19` is a layer beneath that: the family is right and the text has been changed.**

🟢 **The instance, this pass:** [`beltromatti/get-it`](https://github.com/beltromatti/get-it)
(1 138★, live) ships an Apache-2.0 payload with **five words deleted from §6 *Trademarks***. The
canonical safe harbour *"reasonable and customary use in describing the origin of the Work"* becomes
*"describing the origin of the Work"*. Graded against two independent canonical payloads
(`menthorlabs/menthor` 11 337 B; `huggingface/smolagents` 11 357 B).

🟢 **It is not the first.** `p488` found [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor)
carrying **three one-word insertions inside Apache's `TERMS AND CONDITIONS`** plus an overwritten
appendix, and `freelingo` carrying a genuinely altered GNU payload. 🔴 **Three instances across
three unrelated repositories is a pattern, not a trio of accidents.**

🔴 **Why it is invisible.** `get-it`'s payload is **22 bytes longer** than the canonical one it
deviates from — its appendix copyright line adds ~54 B while the deletion removes ~28 B. **A
size check clears it. A badge clears it. A search-API `license` field clears it.** Only a
normalised comparison of the operative span against a known-good payload catches it, and this base
has no retained canonical set (`Gap 498-B`).

🟢 **The product consequence for a studio:** licence review on an education-AI dependency cannot be
*"what licence is it"*. It has to be *"is this licence's operative text the text we think it is"*.
That is one `git cat-file` and one diff per dependency, and it is cheap enough to put in CI. 🔴 What
is not cheap is discovering at contract stage that a trademark carve-out your client-facing
materials rely on was edited out by an upstream author who almost certainly did not mean anything
by it.

### 🟢 `T3` is promoted: the permissive/non-commercial split is a **replicated** property, not a pattern

🔵 `p479` measured a **complete** population — all 22 repositories in a 30-day ≥30★ `topic:education`
census — and found the **two** non-commercial rows were **exactly the two curriculum-and-content
repositories**.

🟢 **`p498` reproduces it on a disjoint population.** Of eight addresses graded from
`topic:edtech` `stars:>400`:

| class | rows | grants |
|---|---|---|
| 🟢 code / tooling | `book-to-skill`, `Papermorph`, `claudemy`, `get-it`, `menthor`, `frametell` | **MIT ×3, Apache-2.0 ×2, AGPL-3.0 ×1 — every one an OSI licence** |
| 🔴 **content / curriculum** | `cn-math-taxonomy`, `PageLM` | 🔴 **CC BY-NC 4.0** and a bespoke **"PageLM Community License"** — **both non-commercial** |

🔴 **Two independent populations, same boundary, no exceptions in either.** 🔵 **The planning
consequence is firm enough to put in a proposal: budget to *build* the curriculum model and the
item bank; expect to *acquire* the tooling.** The reverse assumption — that content is the
commodity and tooling the hard part — is how an education engagement discovers in month three that
its knowledge graph cannot ship.

### 🔴 `T10` gets its decisive measurement — and it is internal to one publisher

🔵 `T10` says market sizing in this sector is not currently usable, resting on cross-publisher
disagreement. 🔴 **The stronger argument needs no second publisher.** MarketsandMarkets puts **North
America at $951 M in 2024**; North America is widely put at **36–42 %** of this market; that implies
a **global $2.3–2.6 B in 2024** — an order of magnitude below the **$9.58 B** figure this KB carried
for 2026, and ~**100×** above its own "Rest of Latin America" series when set against this base's
carried LATAM figure.

🟢 **`T10` therefore hardens from "the publishers disagree" to "the figures are not arithmetically
compatible with their own regional components".** 🟢 Both carried figures are withdrawn as data on
[`intel/market.md`](market.md) this pass. Quote a range with a publisher, or quote a demand signal.

### 🟡 `T2` qualified — the copyleft platform layer has **two non-interoperable families**, not one

🔵 `T2` calls the copyleft platform layer *the binding constraint*. 🟢 `p498` measures a constraint
**inside** it: [`portabilis/i-educar`](https://github.com/portabilis/i-educar) (🇧🇷 municipal SIS,
live at 2026-10-22) and [`formalms/formalms`](https://github.com/formalms/formalms) are both
**GPL-2.0 with no *or-later* election in their source notices — GPL-2.0-only**.

🔴 **GPL-2.0-only and GPL-3.0 do not combine.** So the copyleft column on
[`verticals/solutions.md`](../verticals/solutions.md) is not one pool of mutually-compatible
platforms: `moodle` / `chamilo` / `ILIAS` (GPL-3.0) sit on one side and `i-educar` / `formalms`
(GPL-2.0-only) on the other, and code cannot move between them. 🔵 **For a Brazilian municipal SIS
engagement this is week-one information**, and no previous pass stated it.

### 🟢 `T7` gains its strongest instance — and the agent surface is a **kill switch**, not just a hook

🔵 `T7` says agent tool surfaces are arriving at the LMS boundary, unevenly. 🟢 `p498`'s code read of
[`learningequality/kolibri`](https://github.com/learningequality/kolibri) (HEAD `08e3ecace444`,
2026-10-27) finds the most deployable instance yet: **21 in-tree plugins**, a plugin that mounts its
own URLs and its own DRF API via `KolibriPluginBase.url_module` / `api_url_module`, **21
`api_urls.py`** surfaces, four out-of-tree plugins shipped as precedent (including an **OIDC
provider**), and 🔴 **zero native LLM integration** to displace.

🟢 **The part that matters for procurement:** plugins are enabled and disabled **from the CLI or a
UI** and through `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`.
🔵 **An AI surface the deploying institution can switch off with one environment variable and no
rebuild is a different regulatory object from one compiled into the platform** — it is an
AI-Act-friendly posture that falls out of the architecture rather than being engineered onto it.
🔴 The constraint to design around: hooks are singletons (`KolibriHookMeta(SingletonMeta)`,
`HookSingleInstanceError`) — **one registration per hook**, so two vendors shipping into one
deployment will collide.

### 🔴 Declared gaps on this file

- 🔴 **`T19` rests on three instances across three repositories, all found incidentally.** Nobody has
  measured the **rate** of operative-body edits across an education corpus. `Gap 488-T` asked for
  exactly this and it is still unmeasured — this pass added a third instance instead of a rate.
- 🔴 **`Gap 488-Q` failed a second time.** No 2026 APAC teacher-adoption figure. The ANZ-vs-Asia
  split remains measured on ban-support sentiment.
- 🔴 **`Gap 484-J` not narrowed.** The EMEA leg named Africa and the Middle East in the query and
  returned no instrument, figure or player for either. **"EMEA" on these shelves means Europe.**
- 🟡 **`T11`, `T12`, `T16` were not re-tested this pass.** Carried unchanged.

---

## 🆕 `p499` — `2026-10-28` — **🔴 `T19` IS NARROWED HARD BY THE MEASUREMENT IT ASKED FOR: licence text is NOT "edited in the field" at any measurable rate — 0 of 64 grants on these shelves are materially altered, and two of `p498`'s three claimed instances were a circulating template variant, not edits. 🟢 `T2`'s binding constraint is RE-SCOPED: the copyleft problem is real at the platform layer and FALSE at the integration layer above it. 🆕 `T20` and `T21`.**

### 🔴 `T19` — narrowed from a field practice to a single confirmed instance

`T19` (`p498`) reads: *"Education-AI licence **text** is edited in the field, and the edits are
inside the operative body."* It rested on three instances — `DeepTutor`, `freelingo`, `get-it` —
and `Gap 488-T` conceded the **rate was never measured**.

🟢 **The rate is now measured.** 76 census rows re-fetched at pinned SHAs, 64 gradeable against a
retained canonical set, operative span graded word-by-word
([`repos/trending.md`](../repos/trending.md) `p499`):

| | n | share |
|---|---|---|
| operative body **IDENTICAL** to canonical | 46 | 71.9% |
| deviant **but** the payload is a *different licence* (nearest-neighbour mislabel) | 8 | 12.5% |
| deviant **but** only appended provenance prose, no terms added | 2 | 3.1% |
| deviant **but** a benign vintage / URL / heading variant | 5 | 7.8% |
| deviant **but** a third-party **template** variant shared across unrelated repos | 3 | 4.7% |
| 🔴 **materially altered grant** | **0** | **0.0%** |

🔴 **And `p498`'s instance count is over by one.** `DeepTutor`'s Apache deviation — "submitted to
**the** Licensor", "received by **the** Licensor", §4(d) "excluding **any** notices" — appears
**identically on three repositories, two of them unrelated** (🇭🇰 `HKUDS/DeepTutor`, its derivative
`3yangyang9/DeepTutor-AILearning`, and 🇵🇰 `Orenda-Project/rumi-platform`). 🔵 **An author's edit does
not replicate across unrelated repositories; a template generator's output does.**

🟢 **`T19` restated as the evidence supports it:** *education-AI licence payloads deviate from
canonical often (28.1%) and almost always harmlessly — fill-ins, vintages, appended attribution,
circulating templates. **One** material alteration is confirmed base-wide (`beltromatti/get-it`'s
five-word §6 deletion). The commercial risk is **not** that grants are routinely edited; it is that
a single edited grant is **undetectable without a canonical set**, and one existed.*

🔵 **The method rule that falls out, and it is reusable:** a deviation found on **≥2 unrelated**
repositories is evidence of a shared upstream text. Only a deviation **unique to one project** is a
candidate alteration. `get-it` passes that test; `DeepTutor` does not.

### 🟢 `T2` re-scoped — the copyleft constraint is layer-specific, and the layer that matters is permissive

`T2` reads: *"The education platform layer is copyleft, and this is now the binding constraint."*
🟢 **True of the platform layer and false one layer up**, which changes what it implies.

| layer | licence picture | can a closed derivative ship? |
|---|---|---|
| **Incumbent LMS** (Moodle, Open edX, Canvas) | 🔴 GPL-3.0 / AGPL-3.0 / AGPL-3.0 | 🔴 no |
| 🟢 **Interoperability standards** (`tsugi` Apache-2.0 377★, `scorm-again` MIT 360★) | 🟢 **permissive** | 🟢 **yes** |
| 🟢 **Credentials / competency** (`iblai/lms` MIT) | 🟢 permissive | 🟢 yes |
| 🟢 **Authoring / client** (`haxcms-php` Apache-2.0, `tutors` MIT, `pytogether` MIT) | 🟢 permissive | 🟢 yes |
| 🟢 **Spaced repetition** (`mnemo` Apache-2.0, FSRS flashcards MIT) | 🟢 permissive | 🟢 yes |

🟢 **The correct strategic sentence is: you cannot close the LMS, but you can close everything you
build against it** — because **LTI is a network protocol, not linking**, so a tool speaking LTI to
an AGPL host is a separate work. 🔵 `T2`'s pessimism cost this KB real ground: it pushed engagements
toward `OpenOlat` (448★) and away from the installed base, when the installed base was always
reachable over a permissive integration layer. 🟢 Operationalised as `P499-1`.

🔴 **What `T2` keeps:** fork a Moodle plugin or an Open edX XBlock and the copyleft reaches you.
The constraint is real; it is just **narrower than this file has been stating.**

### 🆕 `T20` — In education, permissiveness tracks *position in the stack*, not project age or size

Across 29 foundational platforms now read from bytes, licence choice is **predicted by layer**:
systems of record are copyleft; the protocol, credential, authoring and client layers are
permissive. 🟢 This is not a size or recency effect — `tsugi` (377★) and `scorm-again` (360★) are
permissive and mature, while `Materia` (52★, 2013) is AGPL-3.0.

**Why it holds:** copyleft was chosen by the 2000s-era institutional platforms to keep public-sector
forks public. The layers built *since* exist to be embedded in someone else's product, and
embedding is what copyleft prevents. 🔵 **Consequence:** when scoping, ask *which layer* before
asking which project. The licence is mostly determined once the layer is fixed, which makes
licensing a **design decision taken early**, not a procurement surprise found late.

🔴 **Caveat, recorded:** the 15.8% → 37.9% permissive share this pass reports moved because `p499`
chose to look at layers nobody here had sampled. **That is a selection effect** (`Gap 499-I`); the
*direction* is evidence, the *magnitude* is not.

### 🆕 `T21` — "Grant by reference" is spreading, and it breaks every licence instrument including this base's

Three rows now ship a `LICENSE` file that **contains no grant** — only a pointer:

| repo | file | bytes | content |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | `license.txt` | **19** | `License: GNU GPL V3` |
| [`codeforlife-education/rapid-router`](https://github.com/codeforlife-education/rapid-router) | `LICENSE.md` | **121** | *"Find our license here"* + link |
| [`codeforlife-education/codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal) | `LICENSE.md` | **121** | same file |

🔴 **Three failures at once.** (1) GitHub's licence API reports a **declared** SPDX id with no text
behind it. (2) A byte-reading instrument — including this base's — finds a payload, grades it
against canonical, and produces a nonsense verdict (`frappe/education`: "−164 words"). (3) For
**GPL specifically**, conveying the work without a copy of the License is a problem under the
licence's own terms.

🟢 **Instrument requirement:** a grant payload must be classified **pointer / partial / full**
*before* it is graded, and a pointer must return "unresolved", not a diff. 🔵 This is adjacent to
`Gap 499-B` (no "unknown licence" verdict) and both come from the same omission: **the instrument
has no way to decline.**

🔵 **Commercially:** a pointer grant is not a blocker, it is a **diligence item** — the real licence
usually exists in a sibling repository or a `COPYRIGHT` file, as `openeducat_erp` does. **Resolve
it before an engagement; do not refuse the row and do not trust the API badge.**

### 🔵 A method finding about this base's own instruments, recorded as a trend because it will recur

🔴 **Two successive forms of `p499`'s own licence instrument deleted operative text**, and neither
was detectable from its own output:

| form | what it silently deleted | what exposed it |
|---|---|---|
| strip any line beginning `copyright` | GPL-3.0 §2's *"…for the term of copyright on the Program, and are irrevocable…"* | a **uniform −22-word "deletion" across 14 independent GPL/AGPL projects** |
| also accept a bare word after `copyright` (to catch `Copyright (c) Microsoft Corporation.`) | GPL-2.0 §1's wrapped *"copyright notice and disclaimer of warranty; keep intact all the"* | `formalms` §1 read **word-for-word canonical** by hand |

🟢 **Both were caught only by a control whose answer was already known** — which is precisely what
`Gap 498-M` says has never been done to a gate on this base. 🔵 **The generalisation: an instrument's
own output cannot validate it.** A plausible number is the expected output of a broken instrument.
Every gate needs a known-good **and** a known-bad input before its results are believed.

### 🆕 Declared gaps — `p499` (trends)

| gap | statement | cost to close |
|---|---|---|
| 🟡 **`Gap 499-J`** | `T20` is asserted on **29 rows of this shelf**, not a sample of the sector. Layer assignment was also done by hand, by me, and layers are not a defined taxonomy anywhere in this repo. | one pass, define the layers |
| 🟡 **`Gap 499-K`** | `T21` rests on **three instances**, two of which are the same organisation (`codeforlife-education`). That is really **two independent instances**. "Spreading" is not yet supported. | one pass, sweep for small grant payloads |
| 🔴 **`Gap 499-L`** | `T19`'s narrowing depends on my **hand classification of 18 diffs** (`Gap 499-F`). The headline *"0 of 64 materially altered"* is not reproducible by code in this repo, so a later pass cannot re-derive it without repeating my judgement. | one pass, encode the four classes |
| 🟡 **`Gap 499-M`** | `T2`'s re-scoping claims **LTI is arm's-length, not linking**, and therefore that AGPL does not reach an LTI tool. 🔴 **That is my reading of the licence and the standard, not legal advice and not a cited authority.** It is load-bearing for `P499-1`'s whole premise. | needs counsel, not a pass |

---

## 🆕 `p500` — `2026-10-28` — two new trends, and one of this file's own claims re-grounded

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten.

## T13 — The licence question has moved from the code to the data

**This is the new one, and it changes how to vet an education-AI component.** Two rows resolved
this pass carry **permissive code and restricted data**:

| Repo | Code | Data |
|---|---|---|
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 **MIT** | 🔴 prompts **CC BY 4.0**; annotated **CLEAR** and **PERSUADE 2.0** corpora **CC BY-NC-SA 4.0 — non-commercial** |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🟢 **MIT** | 🔴 licensed **per dataset**, per download — not uniform |

For an **evaluation** instrument the corpus *is* the product: an MIT rubric evaluator with
non-commercial reference corpora cannot be shipped in a paid engagement on the strength of its code
licence. The same split is what makes `knowledge-graph` unshelvable as data while shelvable as code.

**Consequence:** a two-column licence check — code **and** data — on every education-AI component.
A single SPDX field, which is what GitHub shows and what most curation reads, cannot express this
and will read as green. `Gap 500-E` carries the open commercial question.

## T14 — Mandate and prohibition arrive together, and the gap between them is the work

The 2026 pattern across regions is not adoption versus resistance. It is **the same authority doing
both at once**:

- 🇦🇪 **UAE** mandates AI teaching **KG → Grade 12** across all government schools *and* publishes
  **25 classroom prohibitions** including a **ban for students under 13**; reported teacher uptake
  is **48%**.
- 🇺🇸 **Oklahoma SB 1734** would require every district to adopt a written AI policy *and* bar AI as
  the **primary basis for grading or discipline**. **NYC** runs a moratorium on student-facing AI
  through grade 8 while US teacher use sits near **60%**.
- 🇪🇺 The **EU** treats education **access and assessment** as **Annex III high-risk** — permitted,
  conditioned, and dated (**2 December 2027**).

**Consequence for an engagement:** the deliverable is not a tutor. It is the **enforcement surface**
— age gating, per-district prohibition configuration, human-in-the-loop on grading and discipline,
and an audit trail of which model touched which student artefact — plus the teacher training that
closes a 48%-uptake gap under a full mandate. Capability is assumed; **governed delivery is bought.**

## T15 — Africa's constraint is language, not policy

First pass with named African instruments on these shelves. Ethiopia's Ministry of Education is
building a cross-level framework with **UNESCO** (begun May 2026) and testing teacher
lesson-planning AI; South Africa's **draft** National AI Policy 2026 names STEAM curricula and
community AI centres. 🔴 **The reported practical obstacle in Ethiopia is that models handle
Amharic and Afaan Oromo far less reliably than English.**

**Consequence:** on an African education engagement, scope **model and corpus capability in the
language of instruction before anything else**, and assume offline-capable delivery
([`Wakoma/Lokal`](https://github.com/Wakoma/Lokal), Kolibri). A curriculum-policy framing will
produce a product that does not work in the classroom it was bought for. 🔵 Kenya and Nigeria
remain **unmeasured** here despite an explicit by-country query.

## 🟢 `T2` re-grounded — the copyleft constraint now has a measured denominator

`T2` has said since `p491` that the education platform layer is copyleft and that this is the
binding constraint. It now has a rate rather than an impression. Of the **31** rows in the
`topic:edtech` 50–400★ band still absent from every curated shelf:

| | n |
|---|---|
| 🔴 copyleft (AGPL-3.0, GPL-3.0/2.0, LGPL-2.1, MPL-2.0, CERN-OHL-S-2.0) | 11 |
| 🔴 no resolvable grant at any root path | 6 |
| 🔴 dormant (no push since 2024 or earlier) | 9 |
| 🟢 permissive **and** live | **4** |

**25 of 31 are unusable for reasons that no amount of curation changes.** `T2` is correct and the
constraint is tighter than "mostly copyleft" suggested: on this axis the permissive-and-live yield
is **7.7%**.

## 🔴 `T11` — the claim about unlicensed evaluation instruments needs its third correction

`T11` originally held that **no** education-AI evaluation instrument is licensed. `p493` falsified
it once ([`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark),
MIT). `p500` falsifies the weaker successor claim too: `learning-commons-org/evaluators` is **MIT**
code. 🔴 **But the honest statement is narrower than "licensed instruments exist":** the licensed
ones are licensed **in their code and restricted in their corpora** (see `T13`). The tier has
permissive *software* and non-commercial *reference data*.

