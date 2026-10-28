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
