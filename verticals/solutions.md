---
industry: education
region: Global
updated: 2026-10-19
---

## 🟢 Pass 310 — INTEGRITY IS NOT A VERTICAL PLATFORM AND NOBODY SHOULD SELL IT AS ONE: `111` REPOSITORIES, `0` PLATFORMS, AND THE INSTITUTION ALREADY OWNS THE SYSTEM OF RECORD

⏱️ **Pass 310 of `2026-10-19`.** Evidence:
[`p310-licence-probe.2026-10-19-p310.tsv`](../evidence/p310-licence-probe.2026-10-19-p310.tsv) ·
[`p310-supply-census.2026-10-19-p310.tsv`](../evidence/p310-supply-census.2026-10-19-p310.tsv).

### 🔴 A declared nil, with its denominator

**Twenty rows read off the `academic-integrity` axis; not one is a platform.** They are
detectors, engines, benchmarks, skills, a browser front end and four proctoring prototypes. 🔵
**That is the correct shape for this problem and not a gap to fill**: integrity attaches to the
LMS, the SIS and the assessment tool an institution **already runs**, and this base already
tables the doorways to six of them (Canvas, Moodle, Google Classroom/Workspace, Brightspace/D2L,
Blackboard Ultra, Open edX — see [`agents/top.md`](../agents/top.md)).

🔴 **Stated as the negative it is:** *no open-source integrity PLATFORM exists on this axis*,
measured over 20 of 111 repositories, **and this base is not recommending one be built.**

### 🟢 The one row with a platform shape, and why it is a reference rather than a base

| Platform | Repo | Licence | Stack | Read honestly |
|---|---|---|---|---|
| **SOHAM-3T/LMS** | [SOHAM-3T/LMS](https://github.com/SOHAM-3T/LMS) | 🟢 **MIT** `1 070` · `2c087a8a4bf5` | TypeScript, full-stack | A quiz LMS with auth, plagiarism detection and percentile scoring, **3★**. 🔵 Table it as a **reference implementation of the integrity-inside-the-LMS pattern**, not as a platform to deploy. At 3★ nobody is maintaining it for you |

### 🟢 The deployable integrity layer is a COMPONENT over the platform the client has

| Component | Repo | Licence | Attaches to |
|---|---|---|---|
| Matching engine | [NoplagLabs/noplag-engine](https://github.com/NoplagLabs/noplag-engine) | 🟢 Apache-2.0 | **Self-hosted** — the submission store of any LMS |
| AI-text signal | [Imalwayshere/Open-Detector](https://github.com/Imalwayshere/Open-Detector) | 🟢 MIT | A model you fine-tune on the institution's corpus |
| Citation verification | [constructorfabric/reference-audit](https://github.com/constructorfabric/reference-audit) | 🟢 Apache-2.0 | `.bib`/`.pdf` in the submission pipeline |
| Agent-side integrity | [sunilgentyala/aegis-integrity](https://github.com/sunilgentyala/aegis-integrity) | 🟢 MIT | **MCP** — the assistant the student or marker already uses |
| Assessment diagnosis | [sam-illingworth/Integrity-Debt-Audit](https://github.com/sam-illingworth/Integrity-Debt-Audit) | 🟢 MIT | The assessment design itself, before any tooling |

🔵 **Read the last row against the other four.** Four of them inspect the *submission*; one
inspects the *assessment*. With `62 %` of students using AI and `18 %` of teachers holding any
guidance, the submission-side tools are policing a gap that the assessment-side tool is designed
to close. **Lead an integrity pitch with assessment redesign and attach detection to it** —
never the reverse.

### 🔴 The proctoring sub-vertical: four prototypes, zero deployable

**None of the four camera/keystroke rows can be used**, and for four *different* reasons —
a zero-byte `LICENSE`, a proprietary notice, and two with no grant at any probed path. 🔵
**Every one of them would survive a "has a licence file / has stars / is active" screen**, which
is why the vertical shelf states it here: **if a client asks for open-source proctoring, the
honest answer today is that there is no permissively licensed, maintained option on this axis**,
and the engagement is a conformity screen over the commercial stack they already bought (see
[`intel/market.md`](../intel/market.md), EMEA).

## 🟡 Pass 309 — THE ASSESSMENT VERTICAL WAS ALREADY ON THESE SHELVES; WHAT WAS MISSING IS THAT ITS THREE PLATFORM ROWS ARE ALL COPYLEFT AND NONE OF THEM IS AI-NATIVE

⏱️ **Pass 309 of `2026-10-19`, following `p308` of `2026-10-19`.** Evidence:
[`p309-payload-pin.2026-10-19-p309.tsv`](../evidence/p309-payload-pin.2026-10-19-p309.tsv) ·
[`p309-payload-pin-PRE-FIX.2026-10-19-p309.tsv`](../evidence/p309-payload-pin-PRE-FIX.2026-10-19-p309.tsv) ·
[`p309-root-commit-identity.2026-10-19-p309.tsv`](../evidence/p309-root-commit-identity.2026-10-19-p309.tsv) ·
[`p309-supply-census.2026-10-19-p309.tsv`](../evidence/p309-supply-census.2026-10-19-p309.tsv).

🟢 **The `grading` topic's three platform-scale rows are all CARRIED** — `make carried` says so,
and that is the supply test working rather than a gap:

| platform | slug | stars | what it is | AI in the loop? |
|---|---|---|---|---|
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | `1.4k` | assigning and grading Jupyter notebooks | 🔴 **no** |
| **RELATE** | [`inducer/relate`](https://github.com/inducer/relate) | `437` | course and homework LMS | 🔴 **no** |
| **INGInious** | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | `243` | automated exercise assessment running the course's own tests | 🔴 **no** |

🔴 **`0` of the three declares an AI grading path**, and this base's own `3`-row licence census
on the axis ([`repos/foundations.md`](../repos/foundations.md)) is `4`-to-`1` copyleft. 🔵 **So
the AI assessment layer is a BUILD on a copyleft host, not a pick** — which is the opposite of
the tutor layer, where `p308`'s [`Selleo/mentingo`](https://github.com/Selleo/mentingo) (MIT,
AI-native, self-hosted) exists and refuted the standing *"forced architecture"* conclusion.

🟡 **Stated as the bounded claim it is:** none of the three was re-probed for a licence payload
this pass — they are carried from earlier passes, and `INGInious` appears under **three** slugs
in this base's evidence store (`INGInious/INGInious`, `UCL-INGI/INGInious`, `JuezUN/INGInious`),
which is `p308`'s root-commit question and is **not** settled here. → `ACTION p309-R` item 3.

## 🔴 Pass 308 — THE "FORCED ARCHITECTURE" WAS ALREADY REFUTED AT THE LMS LAYER BY A ROW ON THIS BASE'S OWN SHELF, AND THREE PASSES WENT LOOKING FOR THE BREAK SOMEWHERE ELSE

⏱️ **Pass 308 of `2026-10-19`.** Evidence:
[`p308-payload-pin.2026-10-19-p308.tsv`](../evidence/p308-payload-pin.2026-10-19-p308.tsv) ·
[`p308-shelf-census.2026-10-19-p308.tsv`](../evidence/p308-shelf-census.2026-10-19-p308.tsv) ·
[`p308-regional.2026-10-19-p308.tsv`](../evidence/p308-regional.2026-10-19-p308.tsv).

### 🔴 The finding of the pass for this file, and it cost nothing but a `grep`

🟢 **`p305` recorded a FORCED ARCHITECTURE:** *"every permissive row is a COMPONENT (1★–135★);
every platform-scale system of record is AGPL or GPL."* 🟢 **`p306` refined it at the
credentialing layer and concluded the nil was *"a property of the LMS LAYER, not of
education."*** 🟢 **`p307` broke it at the TUTORING layer with
[`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE)
(BSD-3-Clause).**

🔴 **It was already broken at the LMS layer, by a row this base has carried for roughly a
hundred and forty passes.**

| row | licence, read as bytes | scale | what it is |
|---|---|---|---|
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** — payload `LICENSE`, **1 062 B**, `sha256₁₂` `ceb97717de1f`, `© 2024 Selleo` | **96★ / 30 forks**, **1 348 commits**, TypeScript | 🟢 **A self-hosted, AI-native LMS.** Built-in **AI Mentor**; corporate L&D, onboarding and compliance training; **SCORM 1.2 real and bidirectional**; white-label; k6 performance suite; AWS Marketplace CloudFormation listing with **no software charge** |

🔴 **This base's own words, at [`agents/trending.md`](../agents/trending.md) line 6587:**
*"**AI-native LMS, SCORM + xAPI, white-label, MIT** — positioned explicitly against
Moodle/Docebo/Open edX. **A permissive LMS exit** that did not…"* 🔴 **And line 5972: *"**AI-native
LMS under MIT**."*** 🔴 **And line 3894 names it as the one exception to a star-count rule in so
many words: *"the only exception is `Selleo/mentingo` at `96`★, already carried."***

🔵 **So the sentence that refutes the standing conclusion was on the shelf while the conclusion
was being written, refined, and partially retracted across three passes.** 🟢 **`make claims
TOKEN=mentingo` returns **68 mentions** in that one file.** 🔴 **No pass ran it against its own
conclusion.** → `T-p308b`, and `ACTION p308-R` item 1.

### 🔵 What the row actually changes, stated carefully, because the rule was not simply wrong

🟡 **`p305`'s rule conflated two axes, and `mentingo` separates them:**

| axis | `mentingo` |
|---|---|
| **SCOPE** — is it a system of record? | 🟢 **Yes.** A full LMS: enrolment, courses, SCORM runtime, reporting |
| **SCALE** — is it adopted at platform scale? | 🔴 **No.** `96★ / 30 forks` sits inside `p305`'s own component band (1★–135★) |

🟢 **So `p305`'s rule is true as stated about STARS and false as understood about ARCHITECTURE.**
🔵 **A studio cannot tell a client *"the only permissive option is a component"* — there is a
permissive system of record. 🔴 **It can and must tell them the adoption base is small:** `96★`
against Moodle's install count is not a like-for-like alternative, and the honest pitch is
*"permissive and self-hosted, with a thin community"*, not *"the open Moodle."*

### 🟢 And the monetisation mechanism REFINES `T-p307f` rather than confirming it

🟢 **`p307` concluded from `open-tutor-ai-CE` that the mechanism is OPEN-CORE: *"open-core picks
permissive because the moat is the EE"* — a proprietary Enterprise Edition to sell.**

🔴 **`mentingo` has no proprietary edition.** Its README sells **managed hosting** (*"We run
Mentingo for you,"* flat tiered subscription), **commercial support** (7-day go-live, custom
builds, a two-week trial sprint), and an **AWS Marketplace listing that charges nothing for the
software**. 🟢 **The code is MIT all the way down.**

> 🟢 **The generalisation: a vendor picks a permissive licence when its moat is anything that is
> NOT the code.** 🔵 **An Enterprise Edition is one such moat; OPERATION — hosting, SLA,
> implementation — is another, and it is the one that leaves nothing behind a paywall.**
> 🔴 **A commons-defending system of record still picks copyleft** (`frappe/lms`,
> `instructure/canvas-lms`, `codelitdev/courselit`, `hpi-schul-cloud/schulcloud-server` — all
> AGPL-3.0, all re-pinned this pass). → `T-p308b`.

🔴 **What goes in the proposal, not discovered later:** 🟡 **`30 forks against 96 stars`** is a
normal ratio, unlike `open-tutor-ai-CE`'s inverted `193/111`. 🔴 **Named adopters: none.** The
page gives no user, learner or deployment count — only a k6 suite for sizing. 🔵 **`p179`/`p180`
of this base already retracted an `xAPI`/`LTI` claim for this repo: `SCORM 1.2` is real and
bidirectional, `xAPI` and `LTI` are NOT implemented.** 🟢 **Quote SCORM; do not quote xAPI.**

### 🟢 The copyleft systems of record, all re-pinned by TITLE this pass

🔵 **`ACTION p307-R` item 2 over this file's platform tier. Every cell held.**

| platform | payload | family |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | `license.txt` **33 893 B** | 🟢 **AGPL-3.0** — settled by bytes at `p306` and by title twice at `p307`; 🔵 **not re-litigated, per `ACTION p307-R` item 7** |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | `LICENSE.md` **34 143 B** `9c0cb21c26d8` | 🟢 **AGPL-3.0** |
| [`hpi-schul-cloud/schulcloud-server`](https://github.com/hpi-schul-cloud/schulcloud-server) | `LICENSE` **34 520 B** `e7ae8b5da177` | 🟢 **AGPL-3.0** |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `LICENSE` **18 092 B** on 🔴 **`2.12`** | 🟢 **GPL-2.0** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | `COPYING.txt` **35 147 B** `c3bc1fd94148` | 🟢 **GPL-3.0** |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `LICENSE` **35 121 B** on 🔴 **`v31.0.00`** | 🟢 **GPL-3.0** |
| [`formalms/formalms`](https://github.com/formalms/formalms) | 🔴 **NO-PAYLOAD** — root tree enumerated, 21 entries, no licence-named blob | 🟡 **GPL-2.0 established at `p214`.** 🔴 **A 2026 open-source-LMS review calls it Apache-2.0; this file REFUSES that claim and the refusal stands** |

🟢 **One platform-tier row to flag for the gate's census:** `formalms`' Apache-2.0 reading is a
**third-party review's claim that this shelf refutes**, and the new consistency gate's DATED
census surfaces it as a disagreement. 🔵 **It is not one — it is a correctly recorded refusal —
and it is the clearest example of why that census is a reading list and not a defect list.**

### 🔴 A vertical platform the regions now demand, and no row serves it

🔴 **Oklahoma's `S.B. 1734` requires a parental OPT-OUT from student-facing AI tools *with no
academic penalty*,** before the 2027-28 school year
([`p308-regional`](../evidence/p308-regional.2026-10-19-p308.tsv)). 🔵 **That is not a policy
line, it is an architectural requirement: the platform must deliver the SAME course, assessed
the same way, with the AI path disabled per student.**

🔴 **No platform row on this shelf declares a per-learner AI opt-out.** 🟢 **The nearest
mechanism is `open-tutor-ai-CE`'s RBAC plus its human-in-the-loop review step, and `mentingo`'s
SCORM runtime** — a SCORM package is assessed identically whether or not an agent helped author
it, which is the cleanest opt-out-safe delivery path this base carries. → `P93`.
🟡 **Declared as an informed gap, with an exact denominator: `0` of this file's platform rows.**

## 🟢 Pass 307 — THE "FORCED ARCHITECTURE" BREAKS AT THE TUTORING LAYER: A BSD-3-CLAUSE, SELF-HOSTABLE TUTORING PLATFORM AT 111★ / 193 FORKS, AND THE MECHANISM IS OPEN-CORE RATHER THAN GEOGRAPHY

⏱️ **Pass 307 of `2026-10-19`.** Evidence:
[`p307-new-supply.2026-10-19-p307.tsv`](../evidence/p307-new-supply.2026-10-19-p307.tsv) ·
[`p307-payload-pin.2026-10-19-p307.tsv`](../evidence/p307-payload-pin.2026-10-19-p307.tsv).

### 🟢 A new platform row, and it is the one this file has been missing

| platform | licence, read as bytes | scale | what it is |
|---|---|---|---|
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** — payload `LICENSE`, **1 531 B**, `sha256₁₂` `fa56a9650ca4`, **stock, no added clause** | **111★ / 193 forks**, 380 commits on `main` | 🟢 **Self-hostable AI tutoring platform.** Python + SvelteKit; Docker Compose first-class (bundled Ollama container, or any OpenAI-compatible endpoint — LMStudio, GroqCloud, Mistral, OpenRouter); local RAG with pluggable web search; adaptive tutoring, personas and avatars; voice and video modes; **RBAC**; **a human-in-the-loop framework for evaluating LLM responses**; PWA; UI in **Arabic, French and English** |

🟢 **Why this row changes the file's standing conclusion.** `p305` recorded a **forced architecture** —
*"every permissive row is a COMPONENT (1★–135★); every platform-scale system of record is AGPL or GPL"* —
and `p306` refined it once already, at the credentialing layer. 🔴 **`p307` breaks it at the TUTORING
layer, which is the layer the rule was written about.** 🔵 **A client can now be offered a tutoring
platform that is permissive, self-hosted and customisable, with no copyleft to price and no service
isolation to engineer.**

🔵 **And the mechanism is not geography or institution type — it is MONETISATION.** The CE's own README
names a proprietary **Enterprise Edition** (custom theming and branding, SLA support, LTS). 🟢 **Open-core
picks permissive because the moat is the EE.** 🔴 **A commons-defending system of record picks copyleft.**
🟡 **One observation at this layer; recorded as a mechanism, not yet a rule** → `T-p307f`.

🔴 **What the studio must put in the proposal, not discover later:**

- 🔴 **The EE is proprietary.** Theming, SLA and LTS sit behind it. 🟢 **Everything above is in the CE**,
  but a client told *"it is open source"* without that sentence will hear *"supported"*.
- 🟡 **`193 forks against 111 stars` is an inverted ratio** — forks exceeding stars reads as a codebase
  being taken and changed rather than watched. 🔵 **Consistent with a self-hosted deployable; also
  consistent with coursework.** 🔴 **Two rendered integers, one reading, not independently verified.**
- 🟢 **The human-in-the-loop response-evaluation framework is the feature that matters for EMEA**, and it
  is the one to demo where `§ 6 DUVO` applies: 🔴 **Baden-Württemberg bans AI from AWARDING grades**
  (`p306`), and a platform with a built-in review step is architecturally on the right side of that line.
- 🟢 **Arabic + French + English as first-class UI languages** makes this the only row on these shelves
  that is directly deployable in Maghreb, Gulf and francophone-Africa engagements.

### 🟢 The copyleft map of this vertical, corrected

🔴 **Three of the rows this file described as AGPL are GPL-3.0**, read from the payload's title line
(detail on [`agents/top.md`](../agents/top.md) and [`repos/foundations.md`](../repos/foundations.md)):

| layer | row | licence, title-read | hosting a client deployment |
|---|---|---|---|
| system of record | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** (`33 893 B`, `license.txt`) | 🔴 **§ 13 applies** — serving IS distribution |
| system of record | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** (`34 520 B`) | 🔴 **§ 13 applies** |
| tutoring | [`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) | 🟡 **GPL-3.0** (`35 148 B`) — corrected `p307` | 🟢 **No network clause. Hostable.** |
| tutoring | [`IgorFonck/logicits`](https://github.com/IgorFonck/logicits) | 🟡 **GPL-3.0** (`35 149 B`) — corrected `p307` | 🟢 **Hostable.** |
| tutoring | [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 🟡 **GPL-3.0** (`35 149 B`) — new `p307` | 🟢 **Hostable.** |
| tutoring | [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 🟢 **BSD-3-Clause** (`1 531 B`) | 🟢 **No obligation beyond attribution.** |

🔵 **The shape that falls out: copyleft concentrates in the SYSTEM OF RECORD and thins out as you move
toward the learner.** 🟢 **`p306`'s layer rule survives; what changes is that the tutoring layer is no
longer the AGPL trap this file described.**

### 🟢 Settled, and not re-litigated

🟢 **[`frappe/lms`](https://github.com/frappe/lms) is AGPL-3.0** — re-confirmed this pass by title line
(`GNU AFFERO GENERAL PUBLIC LICENSE Version 3`), on `license.txt`, on the `develop` branch.
🔵 **The conflict row this file carries is CORRECT as a conflict record: `MIT` is the refuted secondary
claim, `AGPL-3.0` is the payload.** 🔴 **Not re-opened.**
🔵 **The education ERP/CRM nil** (`p304`, licensor-confirmed, OpenEduCat LGPLv3) — **recorded, not
re-run**, per `ACTION p306-R` item 7.
🔵 **Proctoring stays filed here as a platform FEATURE rather than a studio build**, and
[`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) is now payload-pinned
**MIT `1 071 B` `e4ecd14cc886`** rather than sidebar-pinned.

## 🟢 Pass 306 — THE 26th LMS NIL IS SETTLED BY PAYLOAD RATHER THAN BY SOURCES, AND IN THE SAME PASS THE NIL IS SHOWN TO BE A PROPERTY OF THE LMS LAYER ONLY: CREDENTIALING HAS PERMISSIVE PLATFORMS

⏱️ **Pass 306 of `2026-10-19`.** Evidence:
[`p306-licence-payload.2026-10-19-p306.tsv`](../evidence/p306-licence-payload.2026-10-19-p306.tsv).

### 🟢 `ACTION p305-R` item 3 DISCHARGED — Frappe Learning is AGPL-3.0, and the conflict is closed by bytes

🔴 **`p305` recorded the single cheapest high-value probe available to this pass: *"Frappe Learning's
licence CONFLICTS across sources (MIT vs AGPL-3.0) and no payload was read… if it is genuinely MIT it is
the first permissive platform-scale LMS in 25 draws."*** 🟢 **The payload was read.**

| repo | path | bytes · sha256₁₂ | verdict |
|---|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | `license.txt` *(lower-case — not on the usual ladder)* | 🔴 **33 893** · `db1a87ba81e8` | 🔴 **AGPL-3.0** |

🔴 **The MIT claim is REFUTED at the payload.** 🟢 **26th consecutive nil on a permissive platform-scale
LMS — and the first one settled by first-hand bytes rather than by a licensor's glossary (`p304`,
OpenEduCat) or by conflicting secondary sources.**

🔵 **Two by-products worth keeping.** The file is at **`license.txt`**, lower-case, which several of this
base's filename ladders do not probe — 🟡 **a near-miss false absence on a repository this base has
discussed for two passes.** And at **33 893 B** it is a **fifth distinct AGPL-3.0 payload length**
(against 34 519 · 35 116 · 35 148 · 35 149) — 🟢 **further confirmation that length identifies nothing**
(`T-p306d`).

### 🟢 The finding that changes what the nil MEANS

🔴 **For 26 draws this base has recorded "no permissive platform-scale system" and allowed it to stand for
the vertical.** 🟢 **It is true of the LMS layer and FALSE one layer across.**

| layer | the platform-scale systems | licence | permissive option? |
|---|---|---|---|
| 🔴 **LMS / SIS — system of record** | Moodle · Open edX · **Frappe Learning** *(settled this pass)* · OpenEduCat *(LGPLv3, licensor-confirmed `p304`)* · Koha | 🔴 GPL / AGPL / LGPL | 🔴 **NO — 26 draws** |
| 🟢 **credentialing — the record of ACHIEVEMENT** | [walt-id/waltid-identity](https://github.com/walt-id/waltid-identity) **319★** · [learner-credential-wallet](https://github.com/digitalcredentials/learner-credential-wallet) **89★** · [open-attestation](https://github.com/Open-Attestation/open-attestation) *(Singapore GovTech)* · [cert-issuer](https://github.com/blockchain-certificates/cert-issuer) | 🟢 **Apache-2.0 / MIT** | 🟢 **YES — four** |

🟡 **Credentialing is not uniformly permissive** —
[`openedx/credentials`](https://github.com/openedx/credentials) (AGPL-3.0, 35 116 B `28bc942b8134`) and
[`edubadges/edubadges-server`](https://github.com/edubadges/edubadges-server) (AGPL-3.0, 34 519 B
`91b65277959e`, the Dutch SURF programme) are copyleft. 🟢 **The point is that here a studio CHOOSES;
in the LMS layer it does not** → `T-p306b`, `P86`, `P87`.

🔵 **So the honest briefing line changes from *"education platforms are copyleft"* to *"the system of
record is copyleft; the achievement record need not be."*** 🟢 **Which is also the commercially better
line, because the achievement record is where the 2026 demand is** (`intel/market.md`: 1EdTech's
employer-side gap).

### 🟡 A platform-selection constraint that outranks licence, restated with a second instance

🔴 **`p305` recorded that a clean grant does not make a prohibited practice deployable** (EU AI Act
Art 5(1)(f), emotion inference, in force `2025-02-02`). 🟢 **`p306` finds a second, and it bites far more
platform selections.**

🔴 **Baden-Württemberg — `§ 115b Abs. 9 Schulgesetz` + `§ 6 DUVO`, in force `2024-10-10`: an AI
application may not award grades or make other essential school decisions, and Art. 9 GDPR
special-category data may not be processed in AI applications.** 🟢 **Permitted: supporting the individual
learning path, e.g. differentiated exercises.**

🔵 **Why this is a VERTICALS question.** Automated grading is not something a studio usually writes — **it
is a feature the LMS or an add-on already ships**, and it is typically on by default. ⚠️ **So the
constraint applies at PLATFORM SELECTION and configuration time, before any custom code exists.**
🟢 **The question to ask of a candidate platform in a German engagement is not "what licence" but "can
automated grade assignment be turned off, and can you prove it stayed off".**

🟡 **Provenance: ministry pages as rendered in search plus one independent aggregator; the Gesetzblatt
text was not opened** (`intel/market.md`).

### 🔵 Not re-litigated this pass

- 🔵 **The education ERP/CRM nil** — `p304` settled it licensor-confirmed (OpenEduCat, LGPLv3).
  **Recorded, not re-run**, per `ACTION p305-R` item 6.
- 🔵 **Proctoring stays filed here rather than on the agent shelf** — a platform feature, not a studio
  build. 🟢 **`p306`'s screen refines the regime: [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI)
  (MIT, 633★) does gaze, mouth-open, person and phone detection and infers NO emotion, so Art 5(1)(f)
  does not reach it** — ⚠️ **Annex III high-risk and biometric-data duties still do.** See
  [`agents/top.md`](../agents/top.md).
- 🔴 **`concentricsky/badgr-server` is UNRESOLVED, not AGPL.** The repo address 404s (Badgr is now
  operated by Instructure as Canvas Credentials); a secondary source says AGPL-3.0; **no payload was
  read, so no verdict is carried.**

## 🔴 Pass 305 — TWENTY-FIFTH NIL ON A PERMISSIVE EDUCATION ERP/CRM, NOT RE-LITIGATED — AND A CONSTRAINT THAT OUTRANKS LICENCE WHEN CHOOSING A PLATFORM TO BUILD ON

⏱️ **Pass 305 of `2026-10-19`.** Evidence:
[`p305-regional.2026-10-19-p305.tsv`](../evidence/p305-regional.2026-10-19-p305.tsv) ·
[`p305-prohibited-practice.2026-10-19-p305.tsv`](../evidence/p305-prohibited-practice.2026-10-19-p305.tsv) ·
[`p305-licence-payload.2026-10-19-p305.tsv`](../evidence/p305-licence-payload.2026-10-19-p305.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` nil'd for the TWENTY-FIFTH time.** 🟢 **`p304`
settled this licensor-confirmed — OpenEduCat's own glossary pages state `LGPLv3` and confirm it is built on
Odoo — so `p305` records the nil and does NOT re-litigate a settled finding.** 🔵 **An independent draw this
pass agrees and adds nothing: Open edX is **AGPLv3**, Moodle **GPL**, Canvas community edition **AGPLv3**,
Sakai **ECL-2.0** (permissive), OpenOlat **Apache-2.0** (permissive), and the sources conflict on Frappe
Learning (**MIT** in one, **AGPL-3.0** in another) — ⚠️ **recorded as a CONFLICT, not resolved, because no
payload was read for it this pass.**

🟢 **`p304`'s correction stands and is the right frame for this file:** *"what is missing is a permissive
SYSTEM OF RECORD; the permissive platforms are the ones AROUND it"* — `Ed-Fi-ODS` (Apache-2.0),
`learningequality/studio` (MIT) and `uPortal` (Apache-2.0) are all permissive **and** platform-scale.

### 🔴 The finding that outranks the licence question when choosing a platform

⚠️ **For any EMEA deployment, a platform's AFFECT features decide admissibility before its licence does.**
🔴 **EU AI Act Article 5(1)(f) prohibits AI inferring emotions in educational institutions and has applied
since `2025-02-02`** — public and private, all levels, in-person and online, **no consent exception**,
medical/safety carve-out only.

🟢 **Why this is a verticals question and not an agents question: proctoring and engagement-analytics are
PLATFORM features, shipped by the LMS or an LMS add-on, not things a studio writes.** 🔵 **Proctoring tools
are the named example in the Commission's guidance, and that guidance reportedly leaves open whether
emotion inference as a **secondary** functionality is in scope — so a platform that ships
"attention insights" as a minor dashboard widget is exactly the arguable case.**

🔴 **The concrete demonstration is on this base's own shelf, and its licence is clean:**
[`mskljns/Intelligent_Tutor_ComprehensionProblems_DAiSEE`](https://github.com/mskljns/Intelligent_Tutor_ComprehensionProblems_DAiSEE)
is **MIT, 1 060 B, `c744c1abbfbb`** and infers engagement/frustration/confusion/boredom from **facial Action
Units**. 🟢 **A clean MIT grant does not make a prohibited practice deployable** → **`P84`** carries the
screen and the response-data substitution.

### 🟢 Platform-adjacent rows admitted this pass

| Plataforma / componente | Repo | Licencia | bytes · sha256₁₂ | Rol en un stack educativo |
|---|---|---|---|---|
| **Feedbacksystem** | [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | **Apache-2.0** | 10 785 · `65125d9e480b` | 🟢 **Personalised-feedback service run in production by a German university.** Sits BESIDE the LMS rather than replacing it — which is the only shape that works against an AGPL system of record, since it avoids linking into it |
| **tutor-mcp** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | 1 073 · `1e05c9440068` | 🟢 **The integration seam.** MCP in front of the tutoring layer means the LMS's licence never reaches the studio's code — the AGPL-isolation shape `P85` and `p303`'s AGPL pricing both depend on |
| **gen-mentor** | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 7 048 · `a2010f343487` | 🟢 **Goal-oriented learning-path generation with NO licence condition at all** — safe to embed in a client tree that must stay proprietary |
| **peolatsi** | [ocala/peolatsi](https://github.com/ocala/peolatsi) | **Apache-2.0** | 11 357 · `c71d239df917` | 🟡 Virtual-lab pattern (electronics) monitored by CTAT tutoring. 1★ — a reference shape for lab-based verticals, not a product |

### 🔴 Refused for this file

- 🔴 **[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)** —
  **877★**, **CC BY-SA 4.0**, 1 230 B `f952182df4eb`. 🔴 **The biggest teaching-asset library in the
  vertical, and ShareAlike reaches the derived CURRICULUM** — which in an education engagement is the
  deliverable itself. 🟢 Commercial use IS permitted; the cost is relicensing the client's curriculum
  → **`P85`** isolates it in three zones.
- 🔴 **[`ShuyunYuan/talentcoach`](https://github.com/ShuyunYuan/talentcoach)** — **842 B reserved grant**,
  `76d0b7213617`. **Refutes `p304`'s `bytes < 400` rule.**
- 🟡 **Frappe Learning** — **licence CONFLICT across sources (MIT vs AGPL-3.0), no payload read.**
  🔵 **Registered as the cheapest high-value payload probe available to `p306`: if it really is MIT it
  would be the first permissive platform-scale LMS this base has found in 25 draws.**

### 🟢 The size rule, restated with this pass's evidence

🟢 **`p303`'s rule holds: PERMISSIVE and PLATFORM-SCALE are nearly disjoint in education.** 🔵 **`p305` adds
the mechanism from the other end — the permissive rows admitted this pass are 1★ to 135★ and every one of
them is a COMPONENT (a feedback service, an MCP seam, a path generator, a lab pattern), while every
platform-scale system of record in the vertical is AGPL or GPL.** ⚠️ **So the architecture is forced, not
chosen: an AGPL system of record with permissive components around it, joined over a network interface.**
🟢 **That is why [`tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) is the most valuable 51★ row on
these shelves — it is the seam that makes the forced architecture buildable.**


## 🔴 Pass 304 — TWENTY-FOURTH CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM, AND THIS TIME THE LICENSOR SAYS SO ITSELF — PLUS AN INDEPENDENT MEASUREMENT OF THIS FILE'S OWN SIZE RULE

⏱️ **Pass 304 of `2026-10-19`.** Evidence:
[`p304-websearch.2026-10-19-p304.tsv`](../evidence/p304-websearch.2026-10-19-p304.tsv) ·
[`p304-starcells.2026-10-19-p304.tsv`](../evidence/p304-starcells.2026-10-19-p304.tsv) ·
[`p304-licence-payload.2026-10-19-p304.tsv`](../evidence/p304-licence-payload.2026-10-19-p304.tsv) ·
[`p304-reachability.2026-10-19-p304.tsv`](../evidence/p304-reachability.2026-10-19-p304.tsv).

### 🔴 The nil, now licensor-confirmed rather than third-party-labelled

🔴 **`open source platform education ERP CRM MIT Apache` returned nothing permissive for the TWENTY-FOURTH
consecutive window.** 🟢 **What changed is the quality of the refusal, not the result.** Every prior pass
recorded OpenEduCat's `LGPLv3` from a third-party label or a GitHub sidebar. **This window the search
returned OpenEduCat's OWN glossary pages, in six languages, and they state it:**

| claim | source quality this window | reading |
|---|---|---|
| **OpenEduCat is `LGPLv3`** | 🟢 **the licensor's own website** (`openeducat.org` glossary, `en`/`fr`/`pt-BR`/`ar`/`de`/`zh`/`es`) | 🔴 **NOT permissive.** The 24-pass nil now rests on the vendor's own words |
| OpenEduCat is built on the **Odoo framework** | 🟢 licensor's own page | 🔴 **inherits Odoo's licence position** — the ERP layer is not escapable by swapping the education module |
| MIT and Apache-2.0 are permissive; Apache adds an **explicit patent grant** | 🟡 vendor glossary, restating general knowledge | 🔵 **Notable only because the licensor plainly understands the distinction and chose otherwise** |

🔵 **This is the strongest form this finding has taken in 24 passes, and it should now be briefed as settled
rather than as "not yet found": there is no permissive education ERP/CRM, and the market's leading open
candidate says so itself.** ⚠️ **The remaining uncertainty is Odoo's own licence text, which this
environment still cannot fetch** — recorded as an open item, not as a doubt about the LGPL finding.

### 🟢 The size rule, measured a second way — and the two measurements agree

🟢 **This file's thesis across 23 passes: permissive education software exists in abundance, but only BELOW
the platform scale.** 🟢 **`p304` tested it with an instrument that has nothing to do with licences — the
fork-to-star ratio of the ten platform-tier rows read this pass** (full table on
[`repos/foundations.md`](../repos/foundations.md)). **The two measurements line up exactly:**

| tier | fork : star | rows | licence position |
|---|---|---|---|
| 🟢 **PLATFORM SCALE — forked to deploy** | **≥ 0.95** | [`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) 1.71 (Apache-2.0) · [`studio`](https://github.com/learningequality/studio) 1.47 (**MIT**) · [`OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) 1.29 (⚠️ unlabelled) · [`uPortal`](https://github.com/uPortal-Project/uPortal) 0.97 (Apache-2.0) | 🟡 **mixed — and this is the crack in the size rule** |
| 🔴 **BELOW PLATFORM SCALE — starred to read** | **≤ 0.30** | `nbgrader` 0.25 (BSD-3) · `schulcloud-server` 0.27 (⚠️ unlabelled) · `apply-for-teacher-training` 0.29 (MIT) | 🟢 permissive, and not systems of record |

🟢 **The size rule survives but needs one amendment, and `p304` can state it precisely: the absence is not
of permissive platform-scale SOFTWARE — it is of permissive platform-scale *SYSTEMS OF RECORD*.**
🔵 **Look at the top band: `Ed-Fi-ODS` (Apache-2.0), `studio` (MIT) and `uPortal` (Apache-2.0) are all
permissive AND all genuinely forked-to-deploy at platform scale.** 🔴 **But not one of them is a school's
system of record:**

- 🟢 **`Ed-Fi-ODS`** is a **data standard and operational data store** — it is what systems of record
  *report into*, which is why 48 forks against 28★ is the highest deployment-per-watcher ratio in the
  table. 🔵 **Apache-2.0, state-level, and the single best permissive foundation on this file for an
  administrative engagement.**
- 🟢 **`learningequality/studio`** is **content authoring** for Kolibri — 🟢 **MIT, +20★ this window, 314
  forks** — it manufactures curriculum, it does not enrol students.
- 🟢 **`uPortal`** is an **aggregating portal** — Apache-2.0, 278 forks against 286★, near parity — it
  presents other systems' data.

⚠️ **The SIS/MIS slot specifically — enrolment, roles, gradebook of record — remains copyleft or
unlabelled across every row this base has read: OpenEduCat (LGPLv3, licensor-confirmed), openSIS (GPL-2.0),
Moodle (GPL-3.0), Open edX (AGPL-3.0), `schulcloud-server` and `OpenEMIS-Core` (both unlabelled in the
sidebar).** 🔵 **So the correct brief is not "there is no permissive platform." It is: the permissive
platforms are the ones AROUND the system of record — the data store, the authoring tool, the portal — and
the system of record itself is where the copyleft sits.** 🟢 **That is an actionable architecture, not a
gap: build permissively around a copyleft core you do not modify.** **Pattern `P81` below.**

### 🟡 A measured caution for anyone reading licences off this file

⚠️ **3 of the 10 platform-tier pages read this pass render NO licence label in the GitHub sidebar** —
`PrairieLearn`, `schulcloud-server`, `OpenEMIS-Core` — **although all three have a `License` link or a
`LICENSE` file in the tree.** 🔴 **A 30% sidebar miss rate on exactly the tier this file is about.**
🟢 **"No licence shown" is not "no licence", and on this file it must be read as "unpinned, go to the
payload."**

🔴 **And a new defect class to carry into any vertical due-diligence: the RESERVED GRANT.**
[`ai-shifu/skills`](https://github.com/ai-shifu/skills) ships a **279 B** file named `LICENSE` that reads
*"All rights reserved… provided for viewing and evaluation only."* 🔴 **It passes a filename check, a
length sanity check and a `Copyright (c)` grep, and grants nothing.** 🟢 **Rule: `bytes < 400` on a licence
file is a red flag, not a short MIT** — every permissive template this base has read falls in 1 060–1 180 B.

### 🔴 What this pass did NOT establish on this file

🔴 **No new vertical platform row.** 🔵 **Correctly so, not a nil through idleness:** the leg `p303` directed
at `ai-education` page 3 returned **applications and courses only** — the five admitted rows are
agent-shaped and went to [`agents/top.md`](../agents/top.md). **No platform candidate appeared at any point
in ranks 41–60.**
🔴 **Odoo's own licence text is still unread** — the publisher channel is closed (23rd pass,
`CONNECT tunnel failed, 403`, not re-tested per `p303`). **The LGPL finding for OpenEduCat does not depend
on it; the inheritance claim does.**
🔴 **No code, deployment or test suite was read** in any platform row; deployment stories come from rendered
READMEs, and fork counts are an intent proxy rather than an install base.

## 🔴 Pass 303 — TWENTY-THIRD CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM — BUT FOUR PERMISSIVE *SELF-HOSTABLE* ROWS ARRIVED, AND THEY CONFIRM THE SIZE RULE THIS FILE HAS BEEN CIRCLING

⏱️ **Pass 303 of `2026-10-18`.** Evidence:
[`p303-websearch.2026-10-18-p303.tsv`](../evidence/p303-websearch.2026-10-18-p303.tsv) ·
[`p303-licence-payload.2026-10-18-p303.tsv`](../evidence/p303-licence-payload.2026-10-18-p303.tsv) ·
[`p303-topic-paging.2026-10-18-p303.tsv`](../evidence/p303-topic-paging.2026-10-18-p303.tsv) ·
[`p303-reachability.2026-10-18-p303.tsv`](../evidence/p303-reachability.2026-10-18-p303.tsv).

🔴 **The mandated phrasing ran and nil'd for the twenty-third time.** Query:
`open source platform education ERP CRM MIT Apache student information system`. Returned **OpenEduCat**
(**LGPL-3.0**, confirmed by the vendor's own glossary page), **openSIS**, **Kuali** — all already on this file.
🟢 **This pass's search sources state the conclusion themselves**, which is new: they report *no MIT- or
Apache-licensed education ERP exists to name*, rather than offering a candidate that then fails verification.
🔵 **The engagement conclusion is unchanged and `p301`'s measurement stands: the education platform layer is
copyleft by constitution.** Do not look for a permissive replacement for Moodle or Open edX. **Integrate with
the copyleft platform across a process boundary and keep permissive code in the agent and service tiers.**

### 🟢 The size rule, now stated as a rule because this pass tested it from the other direction

🔵 **Observation across 23 passes: permissive education software exists in abundance — but only BELOW the
platform scale.** This pass adds **four permissive, genuinely self-hostable rows**, and *not one of them is a
platform a school would run as its system of record*:

| repo | licence (payload, `sha256₁₂`) | ★ | deployment story | what it is NOT |
|---|---|---|---|---|
| [`liuwenji007/regulus-academy`](https://github.com/liuwenji007/regulus-academy) | 🟢 **Apache-2.0** `11 357 B` `c71d239df917` | 9 | **Self-hosted**, Go; **PDF import**, knowledge tree, knowledge graph, coach loop | Not an SIS: no enrolment, no roles, no gradebook of record |
| [`liunor/nlp-agent`](https://github.com/liunor/nlp-agent) | 🟢 **MIT** `1 073 B` `ef01967408a8` | 10 | Teaching platform with dialogue, practice, content **and service observability** | Single-subject (NLP); a teaching service, not an institutional platform |
| [`MadsDoodle/Career-Navigator`](https://github.com/MadsDoodle/Career-Navigator) | 🟢 **MIT** `1 072 B` `a10c8ca82807` | 17 | TypeScript; **Resume → Skill Gap → path** career lifecycle | Not a student information system; a guidance layer |
| [`clduab11/thinkrank`](https://github.com/clduab11/thinkrank) | 🟢 **MIT** `1 071 B` `699170d0cb87` | 28 | TypeScript; collaborative ranking + gamified AI | ⚠️ Promotional README; capability unverified — read the code first |

🟢 **`regulus-academy` is the most engagement-relevant of the four**, because **self-hosting plus local PDF
ingest** is exactly the combination a data-residency-constrained client asks for — and it answers Vietnam's
Decision 33 first education system (content from *uncontrolled* sources) on its face, since the sources are
files the institution supplies. ⚠️ **9★, Go, single author. A starting point, not a product.**
🟢 **`liunor/nlp-agent` is the only row on this file whose own description names observability**, which is
what an SLA needs and what nothing else in this tier offers.

🔵 **So the rule to brief: in education, PERMISSIVE and PLATFORM-SCALE are nearly disjoint.** The permissive
tier tops out at a deployable *service*; the moment software becomes a system of record for an institution, it
was built by a public body or consortium and it is GPL, AGPL or LGPL. **Architect for that split rather than
fighting it.**

### 🔴 The licence line through the platform-shaped rows that failed

🔴 **[`fenago/LearnGraph`](https://github.com/fenago/LearnGraph) — `14★` — PHANTOM GRANT.** Its README says
`MIT License - See LICENSE file for details.` and **the file does not exist**: 18 probes (6 filenames ×
`main`/`master`/`dev`) all 404, and GitHub's sidebar Resources block lists only Readme and Activity. 🔵 **For
this tier specifically the lesson is procedural: a platform evaluation that reads the README's licence
section instead of the licence payload will clear this repository for a client build.** It is a Graph-RAG
learner model with 39 psychometric domains and ZPD sequencing — good enough design that someone will want it.
**Brief the design; take nothing.** 🟢 The repo is active, so asking the author to commit the referenced file
is a real remedy.

🔴 **[`LeParisien-dev/EduAI`](https://github.com/LeParisien-dev/EduAI) — `2★` — no grant** (all probes 404).
A full-stack *"intelligent LMS"* proof of concept, i.e. platform-shaped by intent. Unusable.

🔴 **[`lemos999/ailey-bailey-canvas`](https://github.com/lemos999/ailey-bailey-canvas) — `20★` — CC BY-NC-SA
4.0** (payload `14 770 B`, `sha256₁₂` `5d9d28313854`), opening *"Copyright (c) 2025 fewweekslater(Ray You).
All rights reserved."* 🔴 **NonCommercial is the hardest exclusion this file records — harder than AGPL.**
🔵 **State the difference clearly in a briefing, because it is routinely muddled:** AGPL **prices** a hosted
deployment (you may ship it; you must publish your modifications), whereas **NonCommercial forbids the
engagement itself** — there is no compliance posture that makes a paid client deployment permissible. 🟢 Its
dual-persona design (empathetic coach + critical inquirer) is a *design idea*, which no licence withholds.

🔴 **[`brownplt/LTLTutor`](https://github.com/brownplt/LTLTutor) (🔴 **GPL-3.0**, `35 148 B` `8b1ba204bb69`, Brown
University) and [`IgorFonck/logicits`](https://github.com/IgorFonck/logicits) (🔴 **GPL-3.0**, `35 149 B`
`3972dc9744f6`)** — 🔴 **both CORRECTED `p307` from `AGPL-3.0`** — two more **university-held, copyleft** teaching systems. 🔵 **Fourth and fifth instances of
this file's standing pattern: the institution-built teaching system is copyleft.** That is now a count, not an
impression.

### 🟢 Platform-tier state — one carried row re-pinned, and the content/code licence distinction made explicit

🟢 **[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)** —
**CC BY-SA 4.0**, payload `1 230 B`, `sha256₁₂` `f952182df4eb`, © 2026 Gareth Manning, **877★** (carried at
873★). **First payload pin for this row**, and the licence text was read in full.

🔵 **It matters to this tier because of WHAT it licenses.** The grant covers *"the educational skills,
documentation, examples, and curriculum materials in this repository"* — it is a **content** licence over a
corpus of 165 teacher-facing skills, and it **explicitly permits commercial use and adaptation**. 🔴 **The
price is ShareAlike: derivative curriculum must carry CC BY-SA 4.0.** 🔵 **So the distinction a client's legal
team will ask about, stated once:** embedding this corpus in a proprietary platform is fine as *infrastructure*
— the ShareAlike obligation attaches to the **adapted materials**, not to the platform code that serves them.
Keep adapted curriculum in a separately licensed repository and the problem is tractable. ⚠️ **If the
deliverable IS the curriculum, BY-SA makes it non-exclusive — the client cannot sell it as proprietary
content.** That is a commercial-model conversation to have early, not a technical blocker.

### 🔴 What this pass could NOT do

🔴 **No permissive education ERP, SIS or CRM — twenty-third consecutive nil.** Stated as a property of the
sector rather than a search failure, and **this phrasing should be retired**: 23 windows asking explicitly for
MIT and Apache have produced zero. A future pass should ask instead *which copyleft platform has the best
integration surface*, which is the question an engagement actually faces.
🔴 **No primary source — twenty-second consecutive pass.** `curl` gets **`CONNECT tunnel failed, response
403`** from the agent proxy on every non-GitHub host; `WebFetch` gets `ENOTFOUND`. 🔵 **A network policy on
hosts that resolve, not a missing DNS record** — correcting `p302`'s resolver-scope reading. Matrix:
[`p303-reachability.2026-10-18-p303.tsv`](../evidence/p303-reachability.2026-10-18-p303.tsv).
🔴 **No Moodle, Open edX, Canvas or Sakai release was checked this pass.** Every statement about the major
platforms on this file is **carried**, not re-verified — including their version numbers. Treat the copyleft
platform inventory as last verified at `p302`.
🔴 **`api.github.com` is authenticated but repo-scoped**, `/search/repositories` refused by name; **no exact
star integers for any row on this file.**
🔴 **`thm-mni-ii/feedbacksystem`'s AI mechanism remains unread** (open since `p302`): Helm chart present,
Languages panel empty, visible demo still only an **SQL checker**.
🔴 **`make hooks` was NOT run** — third consecutive pass.

## 🔴 Pass 302 — TWENTY-SECOND CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM — AND THE TWO NEW SELF-HOSTABLE PLATFORMS FOUND THIS PASS LAND ON OPPOSITE SIDES OF THE LICENCE LINE

⏱️ **Pass 302 of `2026-10-18`.** Evidence:
[`p302-websearch.2026-10-18-p302.tsv`](../evidence/p302-websearch.2026-10-18-p302.tsv) ·
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv) ·
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv).

🔴 **The mandated phrasing ran and nil'd for the twenty-second time.** Query:
`open source platform education ERP CRM MIT Apache student information system`. Returned **OpenEduCat**
(**LGPL-3.0**), **OpenSIS** (GPL-2.0), **RosarioSIS** (GPL-2.0), **Frappe Education / ERPNext**, **GegoK12**,
**Fedena**, **SchoolTool** — **every single one already on this file**, and the two the sources *called*
permissive are the two this base has already examined most closely.

🔵 **This is no longer a search failure; it is a finding about the tier, and `p301` already measured it:
the education platform layer is COPYLEFT BY CONSTITUTION.** Twenty-two passes of a phrasing that explicitly
asks for MIT and Apache have produced no permissive education ERP, SIS or CRM, because the sector's
platforms were built by public institutions and consortia that chose GPL/AGPL/LGPL deliberately. 🟢 **The
engagement conclusion is unchanged and is the correct one: do not look for a permissive platform to
replace Moodle or Open edX — integrate with the copyleft platform across a process boundary and keep the
permissive code in the AGENT tier**, which is where every row this pass added actually sits.

### 🔴 The licence line, drawn through the two new self-hostable platforms

🔴 **[`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) — a genuine self-hostable teaching
platform, and AGPL-3.0.** Payload `LICENSE` **34 522 B**, sha256₁₂ `20b067f86de3`. **1.3k★ / 189 forks /
193 commits.** It is a platform by every test this file uses: client + server, **PostgreSQL**
(`DATABASE_URL`), **`docker compose up -d`**, a Node/Bun development path, Vue + Vite + ElysiaJS +
**GeoGebra**, object storage for uploads, and provider-pluggable models (**OpenAI / Anthropic / DeepSeek**)
configured per deployment (`MODEL_API_KEY`). Its capability is the one this tier has never had: *"an AI
teacher equipped with the ability to use an electronic whiteboard"* — **Math Canvas** and Mermaid
**mindmaps**, on the stated premise that text-only chat conveys little in STEM.

🔴 **And AGPL-3.0 reaches network use, which is exactly how a teaching platform is delivered.** Hosting it
for a client triggers the obligation on the hosted service, not merely on redistribution. 🔵 **So its place
on this file is as the CAPABILITY REFERENCE for visual tutoring — the system to study and to demo — and the
build-it-yourself target is [`khayyam-math/khayyam-math`](https://github.com/khayyam-math/khayyam-math)
(**MIT**, payload `1 079 B`, `4068e5e09efd`), which does voice-narrated math figures permissively at
prototype scale.** ⚠️ **A hosted instance exists at `chattutor.app` on the user's own key** — useful for a
demo, and **not** a basis for a client deployment.

🟢 **[`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem) — Apache-2.0, and it is the
permissive platform-tier row this pass actually adds.** Payload `LICENSE` **10 785 B**, sha256₁₂
`65125d9e480b`, holder **© 2023 Technischen Hochschule Mittelhessen**. **24★ / 9 forks**, default branch
**`dev`**. It qualifies for this file rather than the agent shelf because it ships a **deployment**: **Helm
charts and Kubernetes** production install instructions, a THM-hosted project site (`frits.mni.thm.de`),
Gradle + Java 11 build. Function: **automatically checks student submissions and returns an immediate
result**, suggests fixes, and **aggregates recurring mistakes for the lecturer to address in class**.

🔵 **Why it matters to this tier specifically:** every grading and feedback capability this file has found
has been **inside** a copyleft platform — `ls1intum/Artemis` (MIT, but a whole platform),
`Submitty/Submitty`, `PrairieLearn/PrairieLearn`, `autolab/Autolab`. 🟢 **`feedbacksystem` is a permissive,
separately deployable feedback service with its own Helm chart**, so it can sit *beside* Moodle or Open edX
instead of being adopted wholesale. ⚠️ **Boundaries:** the AI mechanism is **undocumented** on the page, the
Languages panel is **empty**, the visible demo is an **SQL checker**, and production use at THM is **implied
by a Helm chart, not stated**. It is a **24-star** project from a university lab — brief it as a credible
starting point with an institutional copyright holder, **not** as a proven product.

### 🔴 The K-12 platform gap this pass can now specify exactly

🔴 **[`blessed0x/scratch-unified-mcp`](https://github.com/blessed0x/scratch-unified-mcp) — no licence at
all** (`LICENSE`/`.md`/`.txt`/`COPYING` absent on `main` and `master`). A **headless Scratch VM exposed over
MCP with 108 tools** letting an agent build, test and publish Scratch projects. 🟢 **Scratch is the most
widely deployed primary-school programming environment in the world**, and this is the only artefact this
base has seen that puts it behind an agent. 🔴 **1★ and no grant — unusable.** 🔵 **Recorded as a specified
gap rather than a row: a permissively licensed headless-Scratch-over-MCP server is a tractable build, and
there is no alternative on this file.**

### 🟢 Platform-tier state, unchanged and restated for briefing

The tier remains **copyleft at its core and permissive only at the edges**:
**AGPL/GPL** — `moodle/moodle` (GPL-3.0), `openedx/edx-platform` (AGPL-3.0), `instructure/canvas-lms`
(AGPL-3.0), `chamilo/chamilo-lms`, `ILIAS-eLearning/ILIAS`, `francoisjacquet/rosariosis` (GPL-2.0),
`os4ed/openSIS-Classic` (GPL-2.0), `GibbonEdu/core` (GPL-3.0), `Vacademy-io/vacademy_platform` (AGPL-3.0),
`HugeCatLab/ChatTutor` (AGPL-3.0, **new this pass**).
**LGPL** — `openeducat/openeducat_erp` (LGPL-3.0, the Odoo-based education ERP; **LGPL is separated from
AGPL on this file deliberately** — linking is permitted, so an AI layer beside it is viable where an
Open edX fork is not).
**Permissive** — `learningequality/kolibri` (MIT, and the offline deployment reference),
`sakaiproject/sakai` (Apache-2.0), `ls1intum/Artemis` (MIT), `thm-mni-ii/feedbacksystem` (Apache-2.0,
**new this pass**).

🔵 **Briefing line that follows from twenty-two nils:** *the platform is the client's and it is copyleft;
what Globant builds and owns is the agent and the evaluation layer beside it.* Every row added in `p302`
is consistent with that split.

### 🔴 What this pass could NOT do

🔴 **No primary source — twenty-first consecutive pass — and the cause is now named**: this session's
resolver answers `github.com` and `raw.githubusercontent.com` and returned **`getaddrinfo ENOTFOUND`** for
every other host tried (`www.congress.gov`, `www.govinfo.gov`, `docs.house.gov`,
`digital-strategy.ec.europa.eu`, `www.iesalc.unesco.org`, `www.vietnam-briefing.com`,
`www.allenandgledhill.com`). It is a **resolver scope**, not governments being blocked. Matrix:
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv).
🔴 **`api.github.com` is proxy-intercepted**, so every star count on this file's new rows is **rendered and
rounded**, and no `licence_spdx` field was available to cross-check a payload reading.
🔴 **No platform's own site was reachable** — `chattutor.app` and `frits.mni.thm.de` were **not** fetched, so
both deployment claims rest on the repositories' own READMEs.
🔴 **`make hooks` was NOT run** (this session was not cleared to execute this base's code), reproducing
`p301`. Licence readings were done directly against `raw.githubusercontent.com` with byte lengths and
hashes recorded for reproduction.
🔵 **`p303` recommendation, third consecutive registration:** retire the mandated ERP/CRM phrasing. Twenty-two
runs, zero permissive hits, and `p301` + `p302` have now both explained *why* the tier is constituted that
way. Replace it with a leg that asks which **copyleft** platforms expose a **stable integration surface**
(LTI 1.3, xAPI, Caliper, MCP), because that is the question an engagement actually turns on.

## 🔴 Pass 301 — TWENTY-FIRST CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM — AND THIS PASS STOPPED ASKING AND MEASURED THE PLATFORM TIER INSTEAD: ELEVEN COPYLEFT PLATFORMS PINNED, LGPL SEPARATED FROM AGPL

⏱️ **Twenty-third pass of `2026-10-18`.** Evidence:
[`p301-websearch.2026-10-18-p301.tsv`](../evidence/p301-websearch.2026-10-18-p301.tsv) ·
[`p301-payload-grade.2026-10-18-p301.tsv`](../evidence/p301-payload-grade.2026-10-18-p301.tsv) ·
[`p301-instrument-substitution.2026-10-18-p301.tsv`](../evidence/p301-instrument-substitution.2026-10-18-p301.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — the TWENTY-FIRST consecutive nil.** 🟢 **Nil
declared with its query and its corpus:** **OpenEduCat** (**LGPL-3.0**, built on the Odoo framework),
**ERPNext**'s education module (licence unstated anywhere in the corpus), **Apache OFBiz**
(Apache-2.0 — a business suite, **not** education), plus **Grocy** (MIT, a household tool) and
**Huly** (Apache-2.0, not education). 🔵 **Five candidates, zero that are both permissive and
education.**

🟢 **The vendor-glossary syndication `p299` and `p300` measured reproduces a third time** — the
OpenEduCat property again supplied multiple slots of the ten. 🔵 **`T-p299c`'s locale-syndication law
is now three passes deep on this leg.**

### 🔵 Twenty-one nils is an answer. This pass spent the budget on the question behind it instead

🔴 **The leg keeps asking "is there a permissive education ERP?" and the answer keeps being no.** What
a studio actually needs is not another nil — it is **the boundary around each platform it will meet on
site.** 🟢 **So `p301` graded the platform tier at payload.** Eleven of this base's platform rows now
carry a byte count and a hash rather than a label:

| platform | licence *(payload, read `p301`)* | bytes | sha256₁₂ | what the boundary means |
|---|---|---|---|---|
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 🔴 **AGPL-3.0** | 36 983 | `f3fba75145cf` | network copyleft — assessment engine stays a **service**, never vendored |
| [`hpi-schul-cloud/schulcloud-server`](https://github.com/hpi-schul-cloud/schulcloud-server) | 🔴 **AGPL-3.0** | 34 520 | `76a97c878c9c` | the German state school cloud — integrate, do not fork |
| [`Vacademy-io/vacademy_platform`](https://github.com/Vacademy-io/vacademy_platform) | 🔴 **AGPL-3.0** | 34 523 | `0d96a4ff68ad` | e-learning platform; same constraint |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** *(at `LICENSE.md`)* | 34 143 | `281e174e4d5f` | 🟢 **byte-exact against the carried cell** |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | 🔴 **AGPL-3.0** | 34 524 | `8d56b405468a` | 🟢 **byte-exact against the carried cell** — the only Open edX MCP path, and it is AGPL |
| [`OpenBoard-org/OpenBoard`](https://github.com/OpenBoard-org/OpenBoard) | 🔴 **GPL-3.0** | 35 147 | `8ceb4b9ee5ad` | interactive whiteboard; desktop, so no network clause |
| [`Tangerine-Community/Tangerine`](https://github.com/Tangerine-Community/Tangerine) | 🔴 **GPL-3.0** *(at `LICENSE.txt`)* | 35 147 | `8ceb4b9ee5ad` | offline assessment at national scale — **keep behind an API** |
| [`pressbooks/pressbooks`](https://github.com/pressbooks/pressbooks) | 🔴 **GPL-3.0** *(at `LICENSE.md`, branch `dev`)* | 35 147 | `8ceb4b9ee5ad` | open-textbook publishing |
| [`ucsd-ets/openedx-caliper-tracking`](https://github.com/ucsd-ets/openedx-caliper-tracking) | 🔴 **GPL-3.0** | 35 149 | `3972dc9744f6` | Caliper analytics for Open edX |
| [`oat-sa/package-tao`](https://github.com/oat-sa/package-tao) | 🟡 **LGPL** | 18 027 | `a45d0bb572ed` | 🟢 **LGPL, NOT GPL** — a closed application may **link** against it |
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🟡 **LGPL** *(branch `develop`)* | 18 025 | `a01259a1b522` | 🟢 same — the most permissive terms in the assessment-platform tier |

### 🟢 The finding a studio can act on: TAO is LGPL, and that is not what "copyleft" implied

🔵 **This base has carried the `oat-sa` rows inside the general copyleft group.** 🟢 **At payload they
are `LGPL` — 18 027 B and 18 025 B, the GNU *Lesser* text, holder *"1989, 1991 Free Software
Foundation, Inc"*.**

🔴 **That is a materially different engagement.** Under AGPL-3.0, a hosted assessment service built on
`PrairieLearn` obliges source release to every user over the network. Under **LGPL**, a proprietary
application may **link** against the TAO libraries and keep its own code closed, provided the TAO
parts stay replaceable and their own changes are published. 🟢 **For a client that wants a QTI-capable
assessment platform inside a commercial product, `oat-sa` is the row to start from — and nothing on
this shelf said so until the payload was read.**

⚠️ **The grade's limit, stated:** the payload names the **Lesser** licence family; **this pass did not
establish whether it is LGPL-2.1 or LGPL-3.0**, and the obligations differ. The 18 KB size and the
*"1989, 1991"* holder line point to the **2.1** lineage, but that is an inference, not a read.
**Pin the version before contracting on it.**

### 🟢 And the QTI tier around it is permissive, which is the pairing that matters

🟢 **The standards-side tooling a TAO engagement needs is MIT or Apache at payload:**
[`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) (**MIT**, 1 076 B,
`7faa621251d7`) · [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player)
(**MIT**, 1 066 B, `9e8db37a05d0`, holder *AE Studio*) ·
[`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) (**MIT**, 1 066 B,
`5bb49280d709`) · [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer)
(**MIT**, 1 067 B, `83e89f7df45d`) · [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground)
(**MIT**, 1 070 B, `3a9fde8de919`) · [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert)
(**Apache-2.0**, 11 357 B, `c71d239df917`) ·
[`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti) (**MIT**, 1 097 B, `d95343578cb4`) ·
[`davemckain/qtiworks`](https://github.com/davemckain/qtiworks) (**BSD-3-Clause**, 2 058 B,
`a5c692f12090`, holder *University of Edinburgh*, at `LICENSE.txt`) ·
[`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) (**MIT**, 1 066 B, `27fb6d463569`,
holder *Kennisnet* — the Dutch education-ICT public body).

🔵 **So the shape of a buildable assessment engagement is now pinned end to end:** **permissive item
authoring, rendering and conversion** in front of a **copyleft platform kept behind an API** — and the
one platform that may be *linked* rather than merely called is **TAO**.

### 🔴 The LMS/SIS rows that serve no grant at all

🔴 [`OpenEMIS/OpenEMIS-Core`](https://github.com/OpenEMIS/OpenEMIS-Core) — **NO-PAYLOAD** on `master`,
confirming the carried cell. 🔵 This base already records *why* that matters: OpenEMIS is the
education-management system most associated with **ministry-level deployment**, and it is the one a
studio cannot price.
🔴 [`LearnPress/learnpress`](https://github.com/LearnPress/learnpress) — **NO-PAYLOAD** on `develop`,
confirming the carried finding that its two **root manifests disagree with each other**.
🔴 [`openstax/os-webview`](https://github.com/openstax/os-webview) and
[`meyerjp3/psychometrics`](https://github.com/meyerjp3/psychometrics) — **NO-PAYLOAD**.
🟢 **CORRECTED `p304`: `meyerjp3/psychometrics` IS GRANTED — `Apache-2.0`, on TWO independent channels.**
Its `pom.xml` (branch `master`, 3 752 B, sha256₁₂ `54d5d8152efb`) carries
`<licenses><license><name>The Apache Software License, Version 2.0</name>…<distribution>repo</distribution>`,
and its README states *"The library is licensed under the Apache License, Version 2.0."*
🔴 **The sentence this replaced — *"IRT and BKT code with no grant is a dependency no client can accept"* —
was wrong, and wrong in the expensive direction: it told a reader to refuse a usable Apache-2.0
psychometrics library.** 🔵 **`p276` had already established that a grant can live in a manifest; the probe
that produced this cell ran only the filename ladder. `gate-enumeration` caught it the moment `p304` ran
the hooks, after three passes in which they were not run.** ⚠️ **There is still NO `LICENSE` file at any
ladder name and NO sidebar label** — so the row is **MANIFEST-GRANTED, not payload-pinned**, and that is a
weaker pin than a file. **Name the manifest and the README together when citing it.**

⚠️ **`NO-PAYLOAD` here means the filename ladder found nothing** — this pass's probe omitted the
shared instrument's README-link arm, which is exactly how `p300` found `OS4ED/openSIS-Classic`'s grant
at `docs/License.txt`. **Treat each as UNRESOLVED, not as unlicensed.**

### 🔴 What this pass could NOT do

🔴 **`make hooks` and the repository's own `probe_payload.sh` were DENIED by the sandbox**
(*"Code from External"*); no standing gate ran against this file. See
[`intel/trends.md`](../intel/trends.md) `T-p301a`.
🔴 **The LGPL version (2.1 vs 3.0) on both `oat-sa` rows is UNREAD.**
🔴 **ERPNext's licence was not resolved** — the corpus never stated it, and no payload was read for
it. It remains the one plausible education-ERP candidate this base has never graded.
🔴 **Twenty-one nils and the leg is unchanged.** The recommendation registered for `p302` is to
**retire the mandated ERP/CRM phrasing** and spend the slot on **named national SIS deployments**,
which is where this tier's real rows have come from.


## 🔴 Pass 300 — TWENTIETH CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM, AND THE LEG RETURNED ONE VENDOR'S GLOSSARY IN TEN LANGUAGES — THE SAME ARTEFACT `p299` MEASURED

⏱️ **Twenty-second pass of `2026-10-18`.** Evidence:
[`p300-websearch.2026-10-18-p300.tsv`](../evidence/p300-websearch.2026-10-18-p300.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — the TWENTIETH consecutive nil.** 🟢 **Nil
declared with its query, and this time the corpus is worth naming because it replicates `p299`
exactly:** of ten slots, **every one** was an **OpenEduCat glossary page** — the same two articles
(*"Open-Source ERP Framework"*, *"what is open source software"*) served at **`ar`, `fr`, `pt-BR`,
`zh`, `de`, `es`** and the bare path. 🔵 **Ten results, two documents, one vendor.**

🟢 **This is `T-p299c`'s locale-syndication law confirmed on a second, different leg** — `p299`
measured it on the EMEA regional query and on this one; `p300` reproduces both. **A law that predicts
the next observation is worth more than one that explains the last.**

### 🔴 And the vendor's own glossary settles the question the leg was asked

🔵 **The content, read rather than dismissed:** OpenEduCat is built on the **Odoo** framework, reusing
its ORM, web framework, reporting engine and security model — and 🔴 **it is licensed `LGPL-3.0`**,
which the glossary itself describes as applying copyleft to the library while permitting closed
applications to link against it.

🔴 **So the twentieth nil is not an absence of candidates — it is a correct negative.** The most
visible open-source education ERP in the corpus **is copyleft, by its own documentation**, and
`p295`-`p299`'s reading of this layer stands: **the education ERP/CRM layer has no permissive
option**, and the honest advice remains this file's oldest — **integrate at the boundary, do not
fork.** 🟢 That advice now has code under it (`p298`'s LTI row set) and, as of this pass, a
**credentialing** boundary too.

### 🟢 What this file gains instead: the layer a registrar actually contracts about

🟢 **Twelve credentialing rows landed on
[`repos/foundations.md`](../repos/foundations.md) this pass** (the layer stood at **one**), and three
of them matter at *this* file's altitude — the platform level, where a client asks *"what runs in
front of my student information system?"*

| boundary | the permissive option, as of `p300` | what it replaces |
|---|---|---|
| **learner-held credential** | [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) — MIT, **89★**, iOS **and** Android, 1 309 commits | a vendor badge portal |
| **verification, embeddable** | [`digitalcredentials/verifier-core`](https://github.com/digitalcredentials/verifier-core) (MIT, engine) behind [`verifier-plus`](https://github.com/digitalcredentials/verifier-plus) (MIT, app) | a hosted verify-this-certificate page |
| **EU ↔ US format bridge** | [`impierce/credential-converter`](https://github.com/impierce/credential-converter) — Apache-2.0, Rust, **OBv3 ↔ ELM/Europass** | a bespoke mapping project |

🔵 **Why these belong in a platform conversation and not only a repository list:** credentialing is
the one layer where the **institution of record** is the customer, the **standard** is fixed
(OBv3 / W3C VC), and the incumbent is usually a hosted vendor whose lock-in is the credential itself.
🟢 **All three rows above are permissive and payload-verified**, so a studio can put the learner's
credential beyond the vendor's reach without touching the copyleft LMS at all.

🔴 **The counter-example to carry with them:**
[`issuebadge/mcp-server`](https://github.com/issuebadge/mcp-server) is **MIT** and was **rejected**,
because the certificates are minted by a **hosted commercial issuer** behind an `ISSUEBADGE_API_KEY`.
🔵 **An MIT grant over a thin client to somebody else's service is not an open platform** — and at
this file's altitude that distinction is the whole job.


## 🔴 Pass 299 — NINETEENTH CONSECUTIVE NIL ON A PERMISSIVE EDUCATION ERP/CRM, AND THE ONE EMPTY CELL IN `p298`'s BOUNDARY TABLE IS NOW EXPLAINED RATHER THAN DECLARED

⏱️ **Twenty-first pass of `2026-10-18`.** Evidence:
[`p299-websearch.2026-10-18-p299.tsv`](../evidence/p299-websearch.2026-10-18-p299.tsv) ·
[`p299-caliper-layer.2026-10-18-p299.tsv`](../evidence/p299-caliper-layer.2026-10-18-p299.tsv).

🔴 **The mandated ERP/CRM leg returned its nineteenth consecutive nil, and the corpus artefact
`p298` measured has got worse by one slot.** `open source platform education ERP CRM MIT Apache`
returned **nine** result slots, of which 🔴 **six are `openeducat.org` glossary pages in six different
languages** — `es`, `fr`, `ar`, `zh`, `de`, `pt-BR`. `p298` measured five of nine in five languages.
🔵 **Same page, same vendor, one more locale.** The remaining slots are two `openalternative.co`
category listings and one further glossary page from the same domain. **No source in the corpus states
OpenEduCat's own licence** — including OpenEduCat's own glossary, which lists MIT and Apache-2.0 only
as examples of what an OSI licence is.

🔴 **Nothing was promoted and nothing was invented.** One more pass, one more declared nil, with the
query and the slot-by-slot corpus in the evidence TSV.

### 🟢 The Caliper cell: from "zero rows, declared" to "zero rows, and here is why"

`p298` left exactly one empty cell in the boundary table below and labelled it *"NOTHING. Still zero
rows. Declared, not glossed."* 🟢 **`ACTION PG-3` sent `p299` after it, and the cell is no longer a
gap in this base's reading — it is a property of the layer.**

🔴 **Every Caliper reference client library has been withdrawn from public view.**
`IMSGlobal/caliper-php-public`, `IMSGlobal/caliper-ruby-public`, `Brightspace/ims-caliper-python`,
`1EdTech/caliper-python` and `1EdTech/caliper-java` **all return `404`**. The University of Michigan's
fork, [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public),
states the cause in its own description: it **"has been unarchived since 1EdTech made the upstream
`caliper-php` private."**

🔴 **What is left in public is copyleft, archived, or a toy.** The only permissive artefact in the
entire layer is [`1EdTech/CaliperBootcamp`](https://github.com/1EdTech/CaliperBootcamp) — MIT, **20
commits**, described by its own README as a proof of concept with a **demo-only OAuth2 flow that
"must not be used in production."** Everything load-bearing is `LGPL-3.0` or `GPL-3.0`, and two of
those are archived. The spec repository itself, [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec),
carries **`Other`** in the org listing and has **no `LICENSE` file at `master`** at all.

🔵 **So the recommendation for a client who needs standards-shaped analytics events is now a
decision, not a blank:**

| option | what it costs | when to pick it |
|---|---|---|
| 🟢 **Use xAPI instead of Caliper** | nothing — it is permissive end to end | 🟢 **The default.** [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) (Apache-2.0) for the vocabulary, [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) (MIT) to prove the store, [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) (Apache-2.0) to store and move, [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) (MIT) if the stack is PHP |
| 🟡 **Take the copyleft** | `LGPL-3.0` on the PHP sensor, `GPL-3.0` on the Open edX and Moodle emitters — and two of the four are archived | Only when the client's own Caliper endpoint is contractually fixed |
| 🔴 **Implement the spec yourself** | a specification whose grant is **`Other`** and whose reference code is gone | 🔴 **Price this as bespoke protocol work, never as "standards integration"** |

🔴 **Do not brief Caliper as an equal alternative to xAPI on open-source terms.** On this evidence it
is not one. 🔵 **This is the first time a standard has failed this base's integration test not on
technical grounds but because the vendor-neutral body closed its own source** — and it is the
sharpest available illustration of why *"integrate, do not fork"* needs a permissive surface to land
on before it is advice at all.

### 🟢 The boundary table, updated — assessment is now armed end to end

`p298` armed **playback** and **packaging** at the QTI boundary and said so. `p299` adds **authoring,
conversion, rendering and a full delivery engine**, so the assessment row is no longer a partial
answer:

| boundary you must cross | permissive component added `p299` *(all on [`repos/foundations.md`](../repos/foundations.md))* | licence | runtime |
|---|---|---|---|
| **Author items in the first place** | [`metyatech/markdown-to-qti`](https://github.com/metyatech/markdown-to-qti) *(Markdown → QTI 3.0)* · [`sonyccd/qti-playground`](https://github.com/sonyccd/qti-playground) *(edit + live preview)* | 🟢 MIT | TypeScript · browser |
| **Get items out of a vendor** | [`rolfis/qti-convert`](https://github.com/rolfis/qti-convert) *(Canvas QTI export → JSON / .docx)* | 🟢 Apache-2.0 | Python |
| **Build and parse packages** | [`examplary/qti`](https://github.com/examplary/qti) *(QTI 3.0 + 2.1, both directions)* | 🟢 MIT | TypeScript |
| **Render and deliver** | [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) *(QTI 2.1 engine + JQTI+ + MathAssess, **2 087 commits**)* | 🟢 BSD-3-Clause | Java |
| | [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) · [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) ⚠️ `choice-interaction` only, no scoring | 🟢 MIT | browser |
| | [`pie-framework/pie-qti`](https://github.com/pie-framework/pie-qti) *(QTI 2.1/2.2/3.0 + QTI ↔ PIE transforms)* ⚠️⚠️ **pre-1.0, not certified, not for high-stakes delivery** | 🟢 MIT | TypeScript |
| **Their content is SCORM, not QTI** | [`S4-NetQuest/react-scorm-provider`](https://github.com/S4-NetQuest/react-scorm-provider) *(React ↔ SCORM API)* | 🟢 MIT | React |
| | [`raccoongang/edx_xblock_scorm`](https://github.com/raccoongang/edx_xblock_scorm) *(SCORM 1.2/2004 inside Open edX)* 🔴 **archived 2023-11-27** | 🟢 Apache-2.0 *(payload-read)* | Open edX XBlock |
| **Carry events out — xAPI** | [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) *(profiles spec)* | 🟢 Apache-2.0 | spec |
| | [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) *(prove the LRS)* | 🟢 MIT | NodeJS |
| | [`php-xapi/client`](https://github.com/php-xapi/client) + [`php-xapi/model`](https://github.com/php-xapi/model) | 🟢 MIT | PHP |
| | [`EscolaLMS/LRS`](https://github.com/EscolaLMS/LRS) — 🟢 **the only `cmi5` row in this base** | 🟢 MIT | Laravel / PHP |
| **Analytics events — Caliper** | 🔴 **STILL ZERO, and now explained above rather than declared.** Use xAPI | — | — |

🔵 **The sales consequence, stated plainly.** A client handed an assessment migration can now be told
which permissive component does each step, in which runtime, and **where the three warnings are**
(`pie-qti` is not exam-grade, `qti-3-player` supports one interaction type, `edx_xblock_scorm` is
archived). 🔴 **That is a different conversation from "QTI is open" — and the one empty cell in the
table is the one a client will hear about from a competitor first, so say it yourself.**


## 🟢 Pass 298 — THE EIGHTEENTH NIL ON A PERMISSIVE EDUCATION ERP/CRM, AND THE "INTEGRATE, DO NOT FORK" INSTRUCTION THIS FILE HAS GIVEN FOR 297 PASSES FINALLY HAS CODE UNDER IT

⏱️ **Twentieth pass of `2026-10-18`.** Evidence:
[`p298-promotion-gap.2026-10-18-p298.tsv`](../evidence/p298-promotion-gap.2026-10-18-p298.tsv).

🔴 **The mandated vertical leg is nil for the EIGHTEENTH consecutive pass**, and the corpus `p297`
described as *"a single SEO estate"* has now been measured twice. `open source platform education ERP
CRM MIT Apache` returned **five `openeducat.org` glossary URLs — the same page in Spanish, French,
Arabic, Brazilian Portuguese and Chinese** — plus a CRM-directory tag page, a vendor "knowledge
collection" blog, **a Drupal mailing-list post from July 2010** announcing CK-ERP 0.30.1, and an
academic paper about using an ERP as a *teaching environment for operations management*.

🔵 **The shape of the nil has changed and it is worth recording precisely.** `p297` measured **10 of
10** slots on one vendor's domain. `p298` measures **5 of 9** — and **the half that is not the vendor
is older and further off-topic than the vendor's own pages.** A sixteen-year-old mailing-list post and
a paper about teaching *with* an ERP are what this query reaches once the SEO estate is subtracted.
🔴 **There is no corpus here. Eighteen passes is enough: `ACTION PG-3` should run this phrasing once as
a control, or not at all.**

🔴 **One claim in the result set was REFUSED rather than carried.** A directory listing described *"an
AI-native CRM/ERP foundation, 80% already built, MIT licensed"* **without naming the repository**. An
unnamed slug cannot be read, and this file's own history is the reason to refuse it: `p296` caught a
2026 comparison publishing [`frappe/lms`](https://github.com/frappe/lms) as *"MIT"* when its sidebar
says **AGPL-3.0**. 🟡 **Apache OFBiz** also surfaced as a generic ERP — correctly licensed, and **not
an education product**. Neither reaches this table.

### 🟢 What this pass actually adds: the integration boundary, permissively armed in six runtimes

🔴 **This file has told every client the same thing since it was written: reach Moodle (GPL-3.0),
Canvas (AGPL-3.0) and Open edX (AGPL) *at the integration boundary*, and keep the studio deliverable
on the permissive side of it. The instruction was right. The code for it was not on these shelves.**
Before `p298` the entire boundary was one row — [`tsugi`](https://github.com/tsugiproject/tsugi),
Apache-2.0, **PHP only** — with **zero** QTI rows, **zero** OneRoster implementations and **zero**
Caliper rows.

| boundary you must cross | permissive component *(all read `2026-10-18`, all on [`repos/foundations.md`](../repos/foundations.md))* | licence | runtime |
|---|---|---|---|
| **Launch your tool from their LMS** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 Apache-2.0 | Node / TypeScript |
| | [`1EdTech/lti-1-3-php-library`](https://github.com/1EdTech/lti-1-3-php-library) *(the standards body's own)* · [`tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 Apache-2.0 | PHP |
| | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 MIT | Python — Django / Flask |
| | [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | 🟢 BSD-3-Clause | JupyterHub |
| **Move their assessment items** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) *(play QTI 3)* · [`instructure/qti`](https://github.com/instructure/qti) *(read legacy QTI 1.2 / 2.1)* | 🟢 MIT | browser · Ruby |
| | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) *(build + validate QTI 3 packages)* | 🟢 MIT | PHP |
| **Roster their students** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) *(OneRoster 1.2 over an Ed-Fi ODS)* | 🟢 Apache-2.0 | .NET |
| | [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) ⚠️ adds non-standard `PUT` writes | 🟢 MIT | Go |
| **Carry their learning events out** | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) *(store)* + [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) *(forward, Profile-filtered, resumable)* | 🟢 Apache-2.0 | JVM |
| **Their content is SCORM** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 MIT | browser |
| **Analytics events (Caliper)** | 🔴 **NOTHING. Still zero rows.** Declared, not glossed — `ACTION PG-3` | — | — |

🟢 **Why this changes a sales conversation rather than just a shelf.** The standing advice used to
arrive with a single implementation language attached: *integrate, do not fork — in PHP*. A Node, Go,
Python or notebook-first engagement had to either stand up PHP or quietly fork something. 🔵 **The
boundary is now crossable from the runtime the client already runs**, which is the difference between
an architectural recommendation and a deliverable.

🔵 **And the vendor-licence split is the clearest evidence this boundary is the real one.**
**Instructure publishes [`instructure/qti`](https://github.com/instructure/qti) under MIT while
[`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) is AGPL-3.0.** The company that
owns the copyleft platform ships its interchange tooling permissively. 🟢 **Quote that in a
procurement meeting: the licence boundary this file has drawn for 297 passes is the same one the
platform vendor draws itself.**

### 🔴 The ERP/CRM measurement, restated after eighteen passes

**There is no permissively-licensed education ERP/CRM.** `p297` stated it; `p298` confirms it on a
corpus that has visibly thinned. 🟢 **What `p298` adds is that the permissive layer's shape is now
fully mapped:** the system-of-record layer is **copyleft, open-core or Odoo-dependent, without
exception** — and the **interchange** layer around it is **permissive, standards-based and, as of this
pass, complete in six runtimes except for Caliper.** 🔵 **So the honest architecture for a client who
needs a permissive system of record is unchanged — build on
[`Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) and accept that no ERP exists to start
from — but the integration surface around it no longer has to be written from scratch.**

## 🟢 Pass 297 — THE SEVENTEENTH NIL ON A PERMISSIVE EDUCATION ERP/CRM, AND THIS TABLE FINALLY GAINS A PERMISSIVELY-LICENSED LMS ANYWAY

⏱️ **Nineteenth pass of `2026-10-18`.** Evidence:
[`p297-promotion-gap.2026-10-18-p297.tsv`](../evidence/p297-promotion-gap.2026-10-18-p297.tsv).

🔴 **The mandated vertical leg is nil for the SEVENTEENTH consecutive pass, and the saturation `p293`
measured is now total in a new way: every one of the ten result slots resolved to ONE vendor's
domain.** The leg `open source platform education LMS SIS MIT Apache 2026` returned **ten
`openeducat.org` URLs** — the same vendor's comparison page in eight languages, plus two glossary
pages. 🔵 **There is no longer a corpus here to search; there is a single SEO estate.** Recorded so the
next pass spends the budget elsewhere.

🟡 **What the vendor's own pages restate, carried as vendor-sourced:** the groupings
*course-centric* (Moodle, Open edX), *institutional* (Sakai, ILIAS), *open-core* (Canvas LMS),
*lightweight* (Chamilo) and *integrated education ERP* (OpenEduCat); that **OpenEduCat is the only
option combining LMS + SIS + fees on one database** (its own product, and `p293` recorded its **Odoo
dependency**); and Moodle's own statistics of **400M+ users across ~150 000 sites**. ⚠️ Vendor
restatement, not an independent reading — and `p296` caught this exact corpus publishing
`frappe/lms` as MIT when its sidebar says **AGPL-3.0**.

🟢 **This table gains a row anyway, and it closes a gap every previous pass on this file has had to
apologise for: THE FIRST PERMISSIVELY-LICENSED LMS HERE.**
[`AnubisLMS/Anubis`](https://github.com/AnubisLMS/Anubis) — **MIT**, **382★ · 54 forks · 1 638
commits · `main`**, **NYU Tandon** named in its README — was promoted out of
[`p989`'s orphan list](../compose/code/p989-sha-identity-fork/promotion-gap-permissive-orphans.txt),
**not** out of the leg.

🔴 **Why that matters on THIS file specifically.** Every other platform row here carries a licence
conversation: **Moodle** GPL-3.0, **Canvas** AGPL-3.0 (network clause), **Open edX** AGPL,
**OpenEduCat** dual-licensed on top of Odoo. The standing advice has therefore been *"integrate, do
not fork."* 🟢 **Anubis is the first row where forking is a legitimate option** — with two honest
boundaries: it is scoped to **computing-science courses** (not a Moodle replacement), and operating it
means **operating Kubernetes**. **Price the operations, not the licence.**

🔵 **The ERP/CRM gap is unchanged and is now stated as a measurement rather than a nil.** After
seventeen passes: **there is no permissively-licensed education ERP/CRM.** The permissive layer in
education is **tooling** (autograding, standards, credentialing, evaluation — six new rows across this
pass); the **system-of-record layer is copyleft, open-core, or Odoo-dependent, without exception.** A
studio that needs a permissive system of record must **build on `Ed-Fi-ODS`** (already on
[`repos/foundations.md`](../repos/foundations.md)) and accept that **no ERP exists to start from.**

## 🔴 Pass 296 — the SIXTEENTH nil on a permissive education ERP/CRM, and a widely-republished "MIT" LMS claim died at the sidebar

⏱️ **Eighteenth pass of `2026-10-18`.** Evidence:
[`p296-promotion-gap.2026-10-18-p296.tsv`](../evidence/p296-promotion-gap.2026-10-18-p296.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — nil for the sixteenth consecutive pass.**
No permissive education ERP/CRM exists to find that this shelf does not already carry. The leg
returned nine vendor and comparison blogs, every one of them a 2026 "best open source LMS" ranking,
and **their licence columns are the finding.**

### 🔴 `frappe/lms` is `AGPL-3.0`. A 2026 LMS comparison published it as MIT, and this shelf nearly carried it

The leg's top results included a ranked comparison listing **Frappe LMS as *"MIT licensed"***, aimed
at *"tech SMBs and nonprofits"*. Read first-hand this pass:

| cell | secondary source claimed | read `p296`, `2026-10-18` |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) licence | **`MIT`** | 🔴 **`AGPL-3.0`** *(sidebar/About)* — and **the string `MIT` does not occur on the page at all** |
| stars / forks / commits | — | `3.3k★` · `1.6k` forks · **`7 828` commits** |
| default branch | — | ⚠️ **`develop`**, not `main` |

🔵 **The error is not cosmetic and it is not conservative.** `AGPL-3.0` reaches through **network
use**: a hosted multi-tenant deployment for a client triggers source obligations over the whole
combined work. A studio that took the comparison blog's column at face value would have scoped a
"permissive LMS" engagement onto the single most copyleft-exposed shape there is — **a hosted LMS.**
`frappe/lms` was already on this shelf, correctly; what `p296` adds is the **refutation of the claim
now circulating about it**, so the next reader who arrives holding that blog has the answer here.

⚠️ **Same leg, same failure mode, three more times.** The comparisons also listed **Forma LMS** as
Apache-2.0 in one article and LGPL in another; **OpenOlat** as Apache-2.0 *(unverified this pass — the
targeted follow-up leg returned nothing on its licence at all)*; and **Fedena** as Apache-2.0, which
this shelf's `p276` already settled on different grounds. 🔴 **Not one of the nine blogs cited a
`LICENSE` file.** The standing rule holds and is now evidenced four times in one pass: **a licence
column in a comparison article is a claim, not a grade.**

🔵 **The one real gain this pass is on the other shelves, not this one.** Five permissive substrates
were promoted onto [`repos/foundations.md`](../repos/foundations.md) — including
[`autolab/Autolab`](https://github.com/autolab/Autolab), a **course-management platform with
automatic programming-assignment grading (CMU, 808★, 2 179 commits)**. ⚠️ It is **not** an ERP/CRM and
does not close this leg's nil, but it is the closest thing to an administrative *platform* this base
has shelved permissively, and a reader who arrives at this file looking for one should be sent there.
Its grant is **`README-ONLY`** grade — see the note on that row before it becomes a dependency.

## 🔴 Pass 294 — the fifteenth consecutive nil on a permissive education ERP/CRM, and for once it is a nil with FOUR VERIFIED NEGATIVES

⏱️ **Sixteenth pass of `2026-10-18`.** Evidence:
[`p294-websearch.2026-10-18-p294.tsv`](../evidence/p294-websearch.2026-10-18-p294.tsv) ·
[`p294-pin-grant.2026-10-18-p294.tsv`](../evidence/p294-pin-grant.2026-10-18-p294.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — FIFTEENTH consecutive nil.** The leg's
own summary states it: *"no single product that clearly combines education ERP, CRM, and an MIT or
Apache license."*

🟢 **What is different this pass is the shape of the nil.** Fourteen passes recorded that nothing
came back. This one read every candidate's grant **at a pin** and disqualified it on its **payload**:

| candidate | grant, read FIRST-HAND at a pin | education claims in README | verdict |
|---|---|---|---|
| [`ONLYOFFICE/CommunityServer`](https://github.com/ONLYOFFICE/CommunityServer) | **Apache-2.0**, `11 357 B`, sha256₁₂ `c71d239df917` | **0 tokens / 6 262 B** | 🔴 Collaboration suite. Not ERP, not CRM, not education |
| [`ChurchCRM/CRM`](https://github.com/ChurchCRM/CRM) | **MIT**, `1 076 B`, sha256₁₂ `82ad0787803a` | **0 tokens / 5 703 B** | 🔴 Membership management. The closest permissive *analogue*, not an education CRM |
| Frappe CRM | 🔴 **AGPL-3.0**, per the leg's own source | — | 🔴 Copyleft. Matters precisely because it is hosted for others |
| "AI-native CRM/ERP foundation", "self-hosted CRM" (MIT, per listings) | 🔴 **no slug named by any source** | — | 🔴 Not probeable. A listing without a path is not a finding |

🔵 **Four permissive repositories exist and none of them is an education platform** — a stronger
statement than *"nothing came back"*, and the one a studio can act on.

### 🟡 OpenEduCat — the Odoo dependency, now stated by the vendor itself

🟢 `OpenEduCat`'s **own glossary** says the product runs on **Odoo's framework**, which supplies
accounting, CRM and HR, with the education layer (students, courses) added on top. 🔴 **Vendor
marketing, so ATTRIBUTED** — but it is the vendor conceding the dependency, which is the direction
that matters. 🟢 The grant is unchanged and read first-hand: **`LGPL-3.0`**, `8 241 B`, sha256₁₂
**`528f84036800`**, on branch **`19.0`** — an Odoo-version branch, not `master`, which `p293`
corrected against `p292`.

🔵 **The consequence for an engagement, unchanged and worth restating:** the education verticals are
copyleft end to end — OpenEduCat `LGPL-3.0`, Moodle `GPL-3.0`, Open edX `AGPL-3.0`, Frappe CRM
`AGPL-3.0`, ERPNext `GPL-3.0`. 🔴 **A permissive education ERP does not exist to be found**; the
permissive layer is what a studio *adds* — the agent tier, which is MIT/Apache almost without
exception.

### 🔴 The vertical layer this pass did NOT reach

🔴 **No primary ministry or government platform source, for the sixteenth pass.** `moe.gov.sg`,
`asean.org`, `gov.br/mec` and now `unu.edu`, `educationforallinindia.com`, `conference.acuass.org`
and `nm-aist.ac.tz` all answer **`000`** through the agent proxy. 🔵 And `p294` established that
**`000` cannot be read as a verdict on those hosts at all**: an invented hostname returns the same
code and earns the same proxy-ledger entry. See
[`p798`](../compose/code/p798-proxy-refusal-ledger/README.md).

## 🟡 Pass 293 — the permissive education ERP/CRM leg is NIL for the FOURTEENTH pass, and the vendor itself now confirms why — plus a CORRECTION to a carried row's branch

⏱️ **Fifteenth pass of `2026-10-18`.** Evidence:
[`p293-websearch.2026-10-18-p293.tsv`](../evidence/p293-websearch.2026-10-18-p293.tsv) ·
[`channel-conflict.2026-10-18-p293.tsv`](../evidence/channel-conflict.2026-10-18-p293.tsv).

### 🔴 The leg, and the vendor-domain saturation is now TOTAL

`open source platform education ERP CRM MIT Apache` returned **10 of 10** results from
`openeducat.org`'s own glossary, in **six languages** (`ar`, `fr`, `pt-BR`, `zh`, `de`, `es`).
🔵 `p283` first recorded this phrasing drifting onto vendor domains; at `p293` there is nothing
else left on the page.

🟢 **And the vendor answers the question against itself.** OpenEduCat's own glossary page
explains that **MIT and Apache-2.0 are permissive** and that **OpenEduCat uses LGPLv3** — i.e.
the single most prominent education-ERP vendor in this channel states in its own words that it is
*not* the thing the leg is looking for. 🔵 That is the most informative form this nil has taken
in fourteen passes: not *"nothing found"* but *"the category's leading open platform is
copyleft, by its own documentation"*. Named alongside it: Moodle, Koha, LibreOffice, Linux —
🟢 all carried, none new, and `make carried SLUG=openeducat/openeducat_erp` returns `CARRIED`.

### 🔴 CORRECTION to `p292`: OpenEduCat's default branch is `19.0`, not `master`

`p292` read the community `LICENSE` at a pin and got the right answer by the right method. 🔴 But
it wrote: *"The default branch is `master`: `/main/LICENSE` answers `404`, which is evidence about
the branch name"*.

| claim | state at `p293`, first-hand |
|---|---|
| the lesson — *"the `404` is evidence about the BRANCH NAME"* | 🟢 **STANDS.** `P1057` on a third axis, and correct |
| the branch name itself, `master` | 🔴 **WRONG. It is `19.0`** — `git ls-remote --symref` returns `ref: refs/heads/19.0\tHEAD`. An **Odoo-version** branch, which is what an Odoo-based product would use |
| `LICENSE` at pin `2670adb20457`, **8 241 B**, sha256₁₂ **`528f84036800`**, LGPL-3.0 | 🟢 **CONFIRMED EXACTLY**, and the same blob is served at the current HEAD `46a5d7d40082` — the grant has not moved between the two pins. Classifier: `LGPL-3.0`, title line **@94**, **§13 absent** |
| the README channel, which `p292` did not read | 🟢 **`AGREE`** — the README states LGPL-3.0 too. Posture **`BUILD-ON`** for the community half |

🔵 **Why the miss is worth a paragraph and not just a fix.** `p292` had the method for reading a
*name* from the channel — it used the symref method on other slugs in the same pass — and here it
**inferred** `master` from a `404` instead. That is the same error as the four guessed `tokenaii`
slugs in the same pass: 🔴 **guessing a name the channel will tell you.** Two instances, one root
cause, one hour apart. `p293`'s oracle exists because of it.

### 🔴 The Enterprise boundary, still the open half

🟢 `p292`'s dual-licence correction **stands and is the important half for a studio**: Community
is **LGPL-3.0**, **Enterprise is proprietary and agreement-gated**, forbidding publishing,
distributing, sublicensing or selling copies, with the community text dated *"Effective: January
1, 2024"*. 🔴 That Enterprise boundary is a **web page**, not a committed payload, so it stays
`ATTRIBUTED` — a licence claim cannot be pinned when it is not in a repository. 🔴 Odoo's own
grant beneath it is still unprobed.

### 🟢 What a studio takes from fourteen nils

🔵 **Stop shopping for a permissive education ERP; it is not there, and the vendor says so.** The
engagement shape these shelves keep arriving at is unchanged and now better evidenced: take the
**copyleft platform as the system of record** — Moodle, Open edX, OpenEduCat Community — and keep
the **AI layer and the decision record** as separate, permissively-licensed components over an
HTTP/LTI boundary. 🔴 The licence risk lives at that boundary, not in the platform, and the
`DANGLING-CLAIM` found elsewhere this pass is a reminder of what to check before building on
anything: a README that asserts a grant no file serves.

## 🟡 Pass 292 — the permissive education ERP/CRM leg is NIL for the THIRTEENTH pass, and the leg's own rediscovery produced a real CORRECTION to a carried row

⏱️ **Fourteenth pass of `2026-10-18`.** Evidence:
[`p292-websearch.2026-10-18-p292.tsv`](../evidence/p292-websearch.2026-10-18-p292.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — no new permissive platform,
thirteenth pass running.** **10 of 10** results were vendor-glossary or directory pages —
`openeducat.org`'s own glossary in five languages, plus `openalternative.co` and a listicle.
The vendor-domain saturation `p283` first measured on this exact phrasing is unchanged.

🟢 **All three platforms the leg named are ALREADY CARRIED, and the index says so rather than
this pass asserting it:** `make carried SLUG=openeducat/openeducat_erp` returns **`CARRIED`**.
OpenEduCat (education ERP on Odoo), ERPNext (GPL-3.0) and Twenty (BSL-1.1, non-OSI) all sit on
these shelves already. 🔵 Two further results advertised an unnamed *"MIT CRM/ERP"* and could
not be resolved to a slug — **not findings**.

### 🟢 The correction: OpenEduCat is DUAL-licensed, and a one-line LGPL entry loses the half that matters

🔴 **What a bare *"LGPL-3.0"* entry does not say.** Read this pass from the project's own
sources: `github.com/openeducat/openeducat_erp`'s README states **LGPL-3.0** with the text in
its `LICENSE` file — but `doc.openeducat.org/legal/legal.html` adds that this covers the
**Community Edition only**, and that the **Enterprise Edition is under a separate PROPRIETARY
licence** whose terms restrict use to a valid OpenEduCat Enterprise Agreement and **forbid
publishing, distributing, sublicensing or selling copies**. The community-licence page dates its
LGPL-3.0 text *"Effective: January 1, 2024"*.

| what you take | grant | what it means for a build |
|---|---|---|
| OpenEduCat **Community Edition** | 🟡 **LGPL-3.0** | copyleft on the module, not on the application that calls it; the usual LGPL care about linking and modification applies |
| OpenEduCat **Enterprise Edition** modules | 🔴 **proprietary, agreement-gated** | 🔴 **cannot be vendored, redistributed or sublicensed.** A client already running Enterprise is a *contract* conversation, not a licence one |
| the Odoo platform underneath | 🔴 **not re-verified this pass** | stated as unread rather than assumed — a separate grant with its own community/enterprise split |

### 🟢 …and the community half is now READ AT THE PIN, not attributed

🟢 **Upgraded within the same pass.** `p291`'s method applied directly — `git ls-remote` for the
SHA, then the payload at that SHA, never at `HEAD` and never at a branch name:

| slug | read at | payload | family | verdict |
|---|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | pin `2670adb20457` | `LICENSE`, **`200`**, **8 241 B**, sha256₁₂ **`528f84036800`** | 🟡 **LGPL-3.0** | 🟢 **`GRANTED-AT-PIN`** |

🔵 The family is assigned by this base's **shared** classifier
(`compose/code/lib/license_family.sh`, `P237`) over the payload's **title block** — not by eye
and not by a body grep, which is `P171`'s standing defect. The payload opens *"For copyright
information, please see the COPYRIGHT file."* and its title block carries **GNU LESSER GENERAL
PUBLIC LICENSE / Version 3, 29 June 2007**.

🔴 **One trap worth recording, because it would have produced a false absence:** the default
branch is **`master`**, not `main`. `/main/LICENSE` answers **`404`** — and that `404` is
evidence about **the branch name**, not about the grant. This is `P1057`'s lesson on a third
axis: after path spellings and repository slugs, **branch names**.

🔴 **What is still NOT read, stated rather than rounded off.** The **Enterprise** boundary is a
**web page** (`doc.openeducat.org/legal/legal.html`), not a committed payload, so the
proprietary half stays 🟡 **ATTRIBUTED** — first-party, since it is the project's own legal
page, but not a file anyone has read at a commit. And **Odoo's own grant was not probed this
pass**: stated as unread rather than assumed. Evidence:
[`openeducat-grant-at-pin.2026-10-18-p292.tsv`](../evidence/openeducat-grant-at-pin.2026-10-18-p292.tsv).

🔵 **Why this is worth a correction rather than a shrug.** This shelf exists so a studio can
tell, before quoting, what it may ship. *"OpenEduCat — LGPL-3.0"* reads as **one** permissive-ish
answer; the truth is a **boundary**, and the boundary is where a customisation engagement either
is or is not redistributable. 🔴 The thirteenth nil on *new* platforms is therefore not the
pass's only vertical result — **an existing row got more accurate**, which on a shelf this old
is worth more than a fourteenth listicle.

## 🔴 Pass 291 — the permissive education ERP/CRM leg is NIL for the TWELFTH consecutive pass, and this time the result set refuted the leg's own premise

⏱️ **Thirteenth pass of `2026-10-18`.** Evidence:
[`p291-websearch.2026-10-18-p291.tsv`](../evidence/p291-websearch.2026-10-18-p291.tsv).

🔴 **`open source platform education ERP CRM MIT Apache` — no new permissive platform, twelfth
pass running.** The result set was once more openeducat.org's own multilingual glossary plus
generic ERP/CRM listicles.

🟢 **Two licence datums are worth keeping precisely because they argue against the leg:**

| candidate the leg surfaced | licence | permissive? |
|---|---|---|
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `GPL-3.0` | 🔴 no — copyleft |
| [`twentyhq/twenty`](https://github.com/twentyhq/twenty) | `BSL-1.1` | 🔴 no — source-available, with commercial/SaaS limits |
| OpenEduCat *(already carried)* | `LGPL-3.0` | 🔴 no — and the **vendor's own page** says so |

🔵 **Read together with the eleven passes before it, that is a structural answer rather than a
run of bad luck:** the education ERP/CRM layer that exists is **copyleft or source-available**,
and the permissive layer a studio can build on sits *above* it — adapters, skills and agent
configurations against platforms the school already runs, which is where `p290`'s skill-adapter
finding and this pass's seven `MIT` segments both landed.

🟡 Licences above are **as reported by the result set**, not payloads this pass read. They are
recorded as a direction for the next verticals leg, not promoted to verified rows.

## 🟢 Pass 290 — the vertical that matters this pass is not a platform, it is the SKILL ADAPTER LAYER to the platforms a school already runs

⏱️ **Twelfth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`submodule-grant-boundary.2026-10-18-p290.tsv`](../evidence/submodule-grant-boundary.2026-10-18-p290.tsv).

🔴 **Mandated verticals leg: no new permissive education ERP/CRM, ELEVENTH consecutive pass.**
The entire result set was `openeducat.org`'s own glossary in seven languages. 🟢 One datum kept
from the vendor's own page: **OpenEduCat is LGPLv3** — not MIT, not Apache. The vendor itself
rules out the licence class the leg asks for. OpenEduCat and Odoo are both already carried
below, and nothing on this shelf changes on their account.

### 🔵 What DID move: an MIT inventory of the systems of record, named one by one

🔵 **Why this belongs on the verticals shelf rather than the agent shelf.** This shelf exists to
answer *"what functioning system do we start from?"* For 290 passes the answer has been a
**platform** — Moodle, Open edX, OpenEduCat, Gibbon. [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents)
and [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) answer a
different and more common engagement shape: **the client is not replacing their platform.**
They ship `skills/<tool>/SKILL.md` adapters aimed at the commercial systems a school or
university already runs, each declaring the env vars it needs.

| segment | systems of record with an MIT skill adapter | grant |
|---|---|---|
| **K-12** | **PowerSchool** (SIS) · **Google Classroom** · **Google Workspace for Education** · **NWEA MAP** · **i-Ready** · **Edulastic** · **Khan Academy** · **ClassDojo** · **ParentSquare** · **Frontline** · **EBSCO** · Canvas | 🟢 **MIT**, read first-hand at the pinned commit `54ee9d91eecd` |
| **Higher education** | **Banner** (SIS) · **Canvas** (LMS) · **Slate** (admissions) · **Workday** · **EAB Navigate** · **Civitas Learning** · **Handshake** · **Salesforce Education Cloud** · **ServiceNow** · **Blackbaud Raiser's Edge** | 🟢 **MIT**, read first-hand at the pinned commit `1a2d898bbd04` |

🔴 **Read what this is before costing an engagement on it.** Each adapter is a `SKILL.md`
declaring a name, a description and a single-line `metadata` naming its env vars — **an
interface declaration, not a client**. There is no application code, no build and no tests in
either repository; the README says so in its own words. 🟢 **The value is the enumeration**: it
is a worked, MIT-licensed answer to *"which systems does an education agent have to speak to"*,
for both segments, and it names **Slate**, **Banner**, **EAB Navigate**, **Civitas Learning**,
**NWEA MAP** and **i-Ready** — commercial systems of record this shelf had never named.
🔴 **Every one of them is proprietary**: the adapter is MIT, the system it reaches is not, and
each needs its own contract, credentials and API terms. That is a per-engagement procurement
question, not a licence question, and it is the real schedule risk.

🟡 **The platform question it does NOT answer.** None of these adapters replaces Moodle or
Open edX, and none is a system of record itself. A client with **no** SIS still needs the
platform rows below.

### 🟢 And the measurement layer under them, new this pass

| component | grant | role in a vertical build |
|---|---|---|
| 🟢 [`cedanl/student-signal`](https://github.com/cedanl/student-signal) | **MIT**, 1 078 B | 🇳🇱 Turns SIS extracts into a **ranked risk list** with precision/recall reported at each invitation threshold. The honest half of a retention product: it quantifies how many of the students you invite will be false positives, **before** anyone is contacted |
| 🟡 [`jknowles/EWStools`](https://github.com/jknowles/EWStools) | **GPL-3.0 only**, 35 156 B | 🇺🇸 The **reference design** a state agency actually shipped (Wisconsin DEWS). 🔴 Dormant since `2016-02-03` — port the method, never the package |

# Vertical solutions — Education

> Real, running platforms a studio engagement can start from and put an agentic layer on
> top of — the Odoo-for-ERP pattern applied to education. Licences read first-hand from
> payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds three platforms, kills two that vendor comparisons recommend, and takes
> the permissive-LMS count from one to three. Extended by
> [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv) — pass 267
> **corrects this file's own claim that Canvas is "commercial SaaS, not a base to build on"**
> (its source is AGPL-3.0, 78,765 commits), and adds a European public-sector school platform, an
> e-testing platform and an offline assessment platform.

## 🟢 Pass 289 — THE PLATFORM SHELF GAINS A LAYER THAT IS NOT A PLATFORM: THE **CURRICULUM ITSELF**, CEDED AND ADDRESSABLE

⏱️ **Eleventh pass of `2026-10-18`.** Evidence:
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv) ·
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../evidence/curriculum-authority-egress.2026-10-18-p289.tsv).

🟢 Four passes asked *"can an agent reach this platform"*. This pass asks the question one layer
down: **once the agent is in, what is it allowed to teach?** A platform licence clears the
*software*. The **curriculum** is a separate grant, held by a separate body, and until this pass
no row on this shelf named one.

| layer | example | licence | who holds it |
|---|---|---|---|
| LMS / platform | Moodle, Canvas, Open edX | GPL-3.0 / AGPL-3.0 | the software project |
| integration | MCP servers (`p267`, `p268`, `p288`) | MIT…none | the server's author |
| **curriculum content** | **National Curriculum for England via Oak** | 🔵 **OGL v3.0 (restated)** | 🔴 **a national agency — NOT the platform, NOT the integrator** |

🔴 **A studio that clears Moodle and Canvas has cleared nothing about the lessons.** That is
the whole reason this row exists.

### 🟢 The vertical row

| platform | platform licence | agent reach | content grant | permissive? |
|---|---|---|---|---|
| **Oak National Academy Open Curriculum** | 🟢 **MIT** — API (`0eeb9d32caed`), SDK/MCP (`02c5a8e84229`), plugins (`e90b3e1c8e94`) | 🟢 **MCP, public beta** (`mcp.thenational.academy/mcp`) + SDK + ontology | 🔵 **OGL v3.0**, commercial use **explicit** in payload | 🟡 **code yes; content is OGL, which is permissive-equivalent for use but is a RESTATEMENT here** |

⚠️ **Two operational conditions, both read first-hand and both easy to miss.** The API needs a
**free API key on request**, and the ecosystem repo **does not accept external PRs** — so the
pattern is *consume the service and own your client*, not *fork the platform*.

### 🔴 The grant shape, because it changes what "customizable" means

`ACTION p289` grades this content layer as a **`RESTATEMENT`**: the payload paraphrases OGL
v3.0 and points at `nationalarchives.gov.uk` for the authoritative text — a host measured
**`POLICY-REFUSED`** from this environment along with **11 other** licensing authorities
(12/12, two independent egress paths).

🔵 **So the vertical recipe for a content layer differs from the one for a platform.** For
Moodle you read the platform's own licence and you are done. For a curriculum you get
**three** artefacts that must agree: the publisher's restatement, the authority's text, and
the per-asset exemptions — and here **only the first is readable**. Record the bound in the
engagement; do not fold it into "OGL, fine".

🔴 **And the attribution the shelf must ship is the prescribed one, not the friendly one.**
`DATA-LICENSE.md` L19 prescribes `"Contains public sector information licensed under the Open
Government Licence v3.0."`; L54 of the same file asks for `"Oak National Academy"`. All three
Oak licence files carrying a summary block do this. **Ship both strings.**

### 🟢 What a studio gets, concretely

The **ontology and structure** — 50 948 key learning points, 11 207 misconceptions, 7 432
prerequisite edges, 160 progression threads, **38 SHACL shapes** — are commercially clear
under the payload's own words. 🟡 What is not clear from the payload is the exemption for
*"third party rights Oak National Academy is not authorised to license"*: that is a **per-asset
clearance**, and an engagement that ships Oak's **graph** is on much firmer ground than one
shipping Oak's **media**.

## 🟡 Pass 288 — the MCP-addressable platform set gains BLACKBOARD, and it is the first entrant whose integration layer carries no grant

⏱️ **Tenth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p288.tsv`](../evidence/verified-repos.2026-10-18-p288.tsv) ·
[`p288-websearch.2026-10-18-p288.tsv`](../evidence/p288-websearch.2026-10-18-p288.tsv).

🟢 **The platform shelf's real question is no longer "can this platform be customized" but
"can an agent reach it".** Four passes have answered that for the permissive and copyleft LMS
set; this pass answers it for the proprietary one.

| platform | platform licence | agent reach | permissive server available |
|---|---|---|---|
| Moodle | GPL-3.0 | MCP (`p267`) | 🟢 yes |
| Canvas LMS | AGPL-3.0 | MCP (`p267`) | 🟢 yes |
| Google Classroom / Workspace for Education | 🔴 proprietary SaaS | MCP (`p268`) | 🟢 7 of 8 servers probed |
| Open edX | AGPL-3.0 | MCP (carried) | 🟡 AGPL-3.0 only (`blend-ed/openedx-mcp` + `tutor-contrib-openedxmcp`) |
| **Blackboard Learn** | 🔴 **proprietary** | **MCP (`p288`)** | 🔴 **none — all three community servers unusable or copyleft-free** |
| OpenEduCat | LGPL-3.0 | ERP modules | 🟡 copyleft |
| Kolibri | MIT | offline-first | 🟢 yes |

🔴 **Blackboard is the shape a studio should expect more of:** a proprietary platform with a
documented REST API, a handful of enthusiastic community MCP wrappers, and **not one of them
carrying a grant you can ship**. `nitsuah/bb-mcp` (already carried) wraps the Learn REST API
with RBAC middleware; `yoyoconnor/BlackboardMCP` is read-only by design and serves no grant;
`anastasasenov/bbmcps` **claims MIT in its `readme.md` and has no licence payload in any of
its 9 files**.

🟢 **The vertical recipe therefore inverts.** For Moodle or Canvas the studio adopts a server
and customizes it. For Blackboard the studio **owns a thin server against the published REST
API** and treats every community repo as a *design reference* — which is exactly what `P41` in
[`compose/patterns.md`](../compose/patterns.md) specifies, including the authorization
posture to copy from Open edX's plugin (re-check the platform's own staff/superuser flags
live on every request, never cache a role).

### 🔴 No new customizable platform this pass

The mandated verticals leg returned Apache OFBiz, Huly, Krayin, Aureus ERP, Atomic CRM,
ERPNext, Dolibarr, iDempiere, Compiere and Twenty. 🔴 **None is education-specific under a
permissive grant**; the single system in the leg that names Education among its verticals is
**ERPNext, and it is GPL-3.0**. Twenty is **source-available (AGPL-3.0 / BSL-1.1), not open
source** — recorded explicitly, because a vendor comparison in the same leg listed it beside
genuinely open systems. The tables below are unchanged.

## 🔴 Pass 287 — no new platform, and the pass found the thing that actually governs a platform engagement: the CURRICULUM's licence, not the platform's

⏱️ **Ninth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p287.tsv`](../evidence/verified-repos.2026-10-18-p287.tsv) ·
[`p287-websearch.2026-10-18-p287.tsv`](../evidence/p287-websearch.2026-10-18-p287.tsv).

🔴 **The mandated vertical leg added nothing, and names its returns so the nil is checkable:**
`OpenEduCat` (already shelved), **ERPNext GPL-3.0**, **Twenty CRM BSL-1.1**
(*source-available, not open source*). 🟢 **Nine passes of this query in ten; the finding is
about the supply.** There is still no education ERP/CRM under MIT or Apache that this base can
locate, and `p286`'s break came from a **directed** leg, not this one.

### 🟢 The pass's real platform finding is a CONSTRAINT this shelf never had a row for

🔵 **`avps82/mentar` (AGPL-3.0, 839 files) ships a country strategy, and it is a licensing
decision wearing product clothing:**

> `AU = ACARA (CC BY)`, `IN/SG/US = GENERIC packs (no claimed alignment)`

🟢 **Read it the right way round and it is the most reusable thing in this pass.** The project
does not ship Australian alignment because Australia is a priority market; it ships Australian
alignment because **ACARA publishes the Australian curriculum under CC BY**. Everywhere the
national curriculum is *not* openly licensed, it ships **generic packs and withholds the
alignment claim**.

🔴 **So "curriculum-aligned" is not a feature a studio can promise per engagement — it is
BOUNDED BY THE HOST COUNTRY'S CURRICULUM LICENCE**, and that is a question none of the
platforms on the shelf below answers. Moodle's GPL, Open edX's AGPL and Canvas's AGPL govern
the **code**; the alignment claim is governed by a **ministry's copyright page**.

🟡 **What this shelf can say today, and what it cannot:**

| 🟢 established this pass | 🔴 NOT established, and registered as a gap |
|---|---|
| **Australia: ACARA is CC BY** — alignment claimable, per `mentar`'s audit | 🔴 The curriculum licence for **every other** market this base has probed. 🇹🇿 `twiga` grounds on Tanzania Institute of Education material and `p286` did **not** record TIE's licence; 🇬🇭 `edubot-africa` on NaCCA; 🇵🇰 `PrepifyAI` on FBISE/Punjab board textbooks; 🇧🇩 Progga on NCTB; 🇮🇳 `gurukul-ai` on NCERT |
| **The remedy exists and is cheap**: withhold the alignment claim and ship generic content | 🔴 **Whether NCERT/FBISE/NaCCA/TIE/NCTB permit derivative aligned content at all.** A ministry copyright page is a **primary source** and none has been read by this base |

🔵 **This is the fourth time a `p28x` pass has found that the binding constraint sits one layer
away from where the shelf was looking** — and the first time the layer is a *government's
copyright page* rather than a repository's `LICENSE`. **Ranked for `p288`: read five ministry
curriculum licences as primary sources.** It is a day's reading and it would let this shelf say
which markets support an alignment claim, for every engagement rather than one.

### 🔴 The tier trap, stated as a platform question because that is where it lands

🔴 **`mentar`'s grounding source is Khan Academy under `CC BY-NC-SA`, and its own audit says
the quiet part:** cleared for *"the non-commercial local pilot"*, 🔴 **"does NOT clear the
Phase-3 paid hosted tier."**

🔵 **Every platform on the shelf below can be stood up for a pilot on content that cannot ship
in the product.** The platform's licence does not change between those two phases; **the
content's does the work**, and `SA` makes it worse rather than better — a redistributed
adaptation of NC content **inherits** NC. 🟢 **The engagement-shaped version:** the pilot that
wins the client and the deliverable that bills them may not be able to use the same corpus, and
the discovery phase is where that has to be found, not the build.

See [`compose/patterns.md`](../compose/patterns.md) **`P40`** for the two-corpus recipe this
implies, and [`intel/trends.md`](../intel/trends.md) `T-p287a`.

## 🟢 Pass 286 — the EIGHT-PASS vertical nil is BROKEN, by a directed leg rather than the mandated one

⏱️ `2026-10-18`, eighth pass. Evidence:
[`regional-intake.2026-10-18-p286.tsv`](../evidence/regional-intake.2026-10-18-p286.tsv).

🔴 **The mandated verticals leg returned its eighth consecutive nil** — `OpenEduCat` is already
shelved, `ERPNext` is GPL-3.0 and general-purpose, `Twenty` is BSL-1.1. 🟢 **The shelf gains a row
anyway, from the Indonesian directed leg**, which is the third pass running where that is the only
channel that extends anything.

| platform | repo | licence (payload `2026-10-18`) | region | what it is |
|---|---|---|---|---|
| **SekolahYuk** | [`Jahirrrr/sekolahyuk-app`](https://github.com/Jahirrrr/sekolahyuk-app) | 🟢 **MIT**, root `LICENSE` 1 064 B | **APAC** (🇮🇩) | *"Aplikasi pembelajaran Sekolah Gratis dan Open Source"* — a free, open-source school learning application. 🟢 **The only permissive grant among seven Indonesian addresses probed**, and the only Kurikulum-Merdeka-era platform on this shelf a studio may bill against |

### 🔴 The Indonesian platform a studio must NOT start from, and it is the best-built one

[`sira313/rapkumer`](https://github.com/sira313/rapkumer) is a working alternative to Indonesia's
official **e-Rapor** report-card system, with an AI generator for learning scopes and objectives
derived from **BSKAP** learning outcomes — the most platform-shaped artefact the leg returned.
🔴 **Its grant is a bespoke `RAPKUMER LICENSE`, 3 140 B, in Indonesian, and §3
`LARANGAN PENGGUNAAN KOMERSIAL` prohibits commercial use in any form** — naming, explicitly, paid
access, charging for installation or support **as the product**, and inclusion in a commercial
service. Written permission from the holder is required for any of it.

🔵 **Two details worth carrying, because they are unusually well drafted and this base's
instruments are not built for either.** §5 **splits the licence's scope**: it covers the source and
**five named static assets**, while everything else under `static/` *"follows its own copyright
holder"* — the monorepo scope problem of `P34`, written by the author rather than discovered by an
auditor. §6 carves out `src/lib/icons/` as **Feather Icons, MIT**. 🔴 And this base's restriction
scanner reads the whole body as **`no-family-no-restriction`**, because its vocabulary is English
(`T-p286b`).

🔵 **The shelf's standing rule, restated with a non-English instance:** a vertical is a starting
point only if its grant permits the engagement. `rapkumer` is **prior art and a design reference** —
read it to learn what Indonesian report-card compliance requires, then build clean.

## 🟡 Pass 284 — the platform shelf is unchanged for a seventh pass, and the leg said so explicitly

⏱️ `2026-10-18`, sixth pass. Evidence: [`p284-websearch.2026-10-18-p284.tsv`](../evidence/p284-websearch.2026-10-18-p284.tsv).

🟢 **The vertical leg returned one platform and it is already here.** `OpenEduCat` (LGPL-3.0, on
Odoo), with its module list reproduced as this shelf carries it — student records, attendance, fees,
timetables, exams, LMS, parent portal, plus an enrolment CRM. 🔴 **The leg returned nothing MIT or
Apache**, in its own words: *"It did not return anything on MIT- or Apache-licensed education
platforms."* That matches what this shelf has said for seven passes: **the education platform layer
is copyleft, and the permissive layer sits above it as agents and MCP servers**, not as platforms.

🟡 **One lead, registered rather than shelved: the `Kuali Foundation`** — higher-education **ERP, SIS
and research administration**, which is the thinnest column on this shelf. 🔴 Not added: the source
is **undated** (it names Compiere and Openbravo beside it), **no repository, ref or grant payload was
read**, and Kuali's association with a move to a commercial entity makes *"open foundation, therefore
permissive"* exactly the **parent-inference** grade this base ranks weakest. Resolving it costs one
`git ls-remote` and one payload read; it is in the backlog in [`../README.md`](../README.md).

🔵 **Why a seventh consecutive nil is worth a heading.** The platforms a studio customises for an
education client — Moodle, Open edX, Canvas, Kolibri, OpenEduCat, Sakai, BigBlueButton, H5P — are a
**stable, essentially closed set**, and seven passes of searching have added none. 🟢 That stability
is a planning asset: the integration surface a studio learns this year is the one it will still be
integrating against next year. **The volatility in this industry is in the agent layer, not the
platform layer** — and this base's own numbers say the agent layer has been still for ten passes
too, which makes the whole stack unusually predictable to quote against.

## 🟢 Pass 283 — the platform shelf is unchanged, and that is now a measured statement rather than an absence of news

⏱️ `2026-10-18`, fifth pass. Evidence: [`repo-identity.2026-10-18-p283.tsv`](../evidence/repo-identity.2026-10-18-p283.tsv) · [`ladder-case-audit.2026-10-18-p283.tsv`](../evidence/ladder-case-audit.2026-10-18-p283.tsv) · [`p283-websearch.2026-10-18-p283.tsv`](../evidence/p283-websearch.2026-10-18-p283.tsv).

🔵 The global vertical leg returned **OpenEduCat, Open edX, Canvas, Moodle, Sakai, OpenOLAT,
Forma LMS, Chamilo and ILIAS**. 🟢 **All nine are already on this shelf.** The two licence
disagreements the sources carried — Sakai as *Apache-2.0* vs *ECL-2.0*, Open edX as *AGPL-3.0* vs
*"Apache-2.0 for some components"* — are **both already adjudicated here from payload**, which is
the shelf doing its job: a secondary source's confusion is not new information.

🟢 **Identity verified, not assumed.** Every live address on this shelf was resolved with
`git ls-remote` this pass as part of the 138-address census: **138 distinct HEADs, 0 collisions,
0 unreachable.** The Sunbird stack's `ls1intum/Pyris` entry and the diagram note explaining that
`ls1intum/Iris` is an alias of it both survive the new `make gate-identity` unchanged — prose and
indented diagrams are not rows, which is control `C7`.

## The platform shelf

> 🟢 **Copyright-holder census (`p281`).** Every `GPL`/`AGPL`/`LGPL` row on this shelf was fetched at
> payload and read for a filled licence appendix: **5 of 35 readable grants name a holder, 30 do
> not.** 🔵 **What that means when a client's legal review asks "who grants this?"** — for the 30,
> *nobody is named in the licence*, and the answer has to be built from the commit history or the
> project's governance page, not quoted from the payload. 🟢 The platforms that **do** name a
> counterparty are [`GibbonEdu/core`](https://github.com/GibbonEdu/core) (`2010 Gibbon Foundation`),
> [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) (`2025 GegoSoft Technologies`) and
> [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) (`PrairieLearn, Inc.`
> with the `University of Illinois Board of Trustees`). 🔴 **An unfilled appendix is not a defect and
> not a risk** — verbatim text is the normal way to ship copyleft; it is simply a question the
> payload cannot answer. Evidence:
> [`copyleft-holder-regrade.2026-10-18-p281.tsv`](../evidence/copyleft-holder-regrade.2026-10-18-p281.tsv).


| Platform | Repo | Licence | Stack | Where it fits |
|----------|------|---------|-------|---------------|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(`COPYING.txt`)* | PHP + MySQL/PostgreSQL | The default LMS of public education worldwide. Has a **first-party AI subsystem since 4.5** — provider-pluggable, so a client can point it at OpenAI, Azure, or a local Ollama/vLLM endpoint. Start here for K-12 and public universities. 🟢 **Pass 273 — the agent doorway into Moodle is permissive, which this file did not say.** Beyond the first-party AI subsystem, Moodle is now **MCP-addressable under MIT**: [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) (**MIT**, 40 tools + `ws_raw`, teacher-side **writes**, upsert-by-`idnumber`, any Moodle 4.x/5.x) and [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (**MIT**, Go, student-side). ⚠️ **The licence boundary is the write path, not the wrapper:** the writes go through a companion Moodle `local_` plugin, so the **deployed combination is GPL-3.0** — no network clause, so hosting is unaffected, but a *distributed* Moodle image carrying it ships as GPL-3.0. 🔵 **So the GPL-3.0 in this cell is the licence of the whole engagement, and that was already true before the agent arrived** — the MCP layer adds no new copyleft reach. See `P23`. |
| 🆕 **eLeDia.ai Suite free** | [eledia/moodle-elediaai-suite-free](https://github.com/eledia/moodle-elediaai-suite-free) | 🔴 **GPL-3.0-or-later** *(root `LICENSE` 35 149 B = full GPL-3.0 text; each plugin carries its own 1.1–1.2 KB `either version 3` grant — payload read `2026-10-18`)* | PHP (Moodle plugins) | 🟢 **The agentic layer for Moodle, shipped by a vendor, as seven installable plugins** — the single most complete instance on this shelf of the pattern this file exists to describe. `block_elediaai_tutor` (tutor chat in course + dashboard) · `local_elediaai_chatengine` (threads, streaming) · `local_elediaai_core` (feature registry, **quota**, **audit**) · `local_elediaai_sources` (course content → knowledge base via **17 extractor subplugins**: assign, book, data, feedback, folder, glossary, h5pactivity, imscp, label, lesson, page, …) · `local_literag` (🟢 **local RAG on Moodle's own full-text search — no external service**, the data-residency answer for EU public sector) · `local_aitransparency` (🟢 **marking of AI-generated content**) · `webservice_elediamcp` (🟢 **MCP connector: Moodle tools for AI assistants**). ⚠️ **eLeDia GmbH, Berlin; GitHub is a MIRROR of their GitLab, so PRs are not accepted there.** ⚠️ **Licence boundary:** GPL-3.0-or-later with **no network clause** — hosting a modified Moodle is unaffected, but a *distributed* image carrying these plugins ships as GPL-3.0-or-later. Same boundary as the Moodle row above, so **the engagement's licence does not change by adopting it**. 🔵 **Fourth MCP-addressable LMS surface in this base and the first vendor-shipped, in-tree, payload-verified one**; and `local_aitransparency` is **the first production component that implements the AI Act Art. 50(2) marking duty this base's own instruments measure**. 🔴 **EMEA-placed (DE).** |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** — 🟢 **RIDER-CLEARED at payload, pass 272** *(`master/LICENSE`, 10,982 B; `TERMS AND CONDITIONS` byte-identical to upstream; the 375 B shortfall vs stock is the optional APPENDIX replaced by two attribution notes — University of Zurich / frentix GmbH — carrying no restriction. See `T39`)* | Java | **The only Apache-2.0 full LMS found this pass.** Swiss-maintained, used across German-speaking higher education. If procurement rules out copyleft, this is the shelf — and it is the single most under-used finding in this file. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | Python/Django + React | MOOC-scale, the platform behind edX. Extend through [XBlock](https://github.com/openedx/XBlock) (Apache-2.0), never by forking core. **The AGPL network clause applies to hosted deployments** — price it before the SOW, not after. |
| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | Java/Spring + Angular | Interactive learning with **automated feedback** and an integrated exercise runner (TUM Applied Education Technologies; 819★, 12,437 commits, self-hosted by universities in several countries — 🔴 **re-read `p295`: `817★` / `395` forks / `12,440` commits, branch `develop`. The stars went DOWN while the commits advanced**). The permissive choice when the deliverable is assessment rather than content delivery. **Pass 266 — the AI layer is already built and config-gated:** **Iris** (LLM tutor, MIT), **Pyris** (LLM microservice, MIT), **Athena** (feedback suggestion, 🟢 **MIT at metadata grade since p275** — 12 of 14 manifests), **Hyperion** (AI exercise authoring on Spring AI, no separate repo). "Config-gated" is the commercially important word — the same deployment runs with AI off, so a high-risk EU AI Act classification can be met by configuration rather than by re-architecture. |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | TypeScript | **AI-native LMS**, self-hosted, positioned against Docebo/TalentLMS. Ships an AI mentor with voice role-play and auto-scoring, an AI course builder that converts policy documents into courses, open-ended answer grading, **Langfuse tracing of model calls**, an **MCP endpoint**, and bring-your-own-key. The closest thing to a 2026-native corporate L&D starting point under MIT. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | Odoo (Python) | Education **ERP**: admissions, SIS, gradebook, library, fees — the Odoo-for-education pattern. Active branches for Odoo 17.0 / 18.0 / 19.0. **The repo path this base previously published (`OpenEduCat-Inc/OpenEduCat`) is a 404; this is the canonical one.** |
| 🆕 **GegoK12** | [Gego-K12/gegok12](https://github.com/Gego-K12/gegok12) | 🟢 **MIT** *(`main/LICENSE`, `1 150` B — payload read, diffed against stock, zero riders, `p274`)* — ⚠️ **core only** | PHP 8.4 + Laravel | 🟢 **The permissive school ERP / SIS this file has said for nine passes does not exist** — and this base **refused it twice**, both times after probing `gegok12/gegok12`, **a slug that does not resolve** (`T44`). **Where it fits:** the Odoo-for-education pattern at **MIT** instead of LGPL-3.0, so the agentic layer and the deliverable carry no copyleft at all — the one row on this shelf where that is true of an *administrative* system rather than an LMS. ⚠️ **Open-core: 26 of 38 modules free, 12 Pro modules sold separately. Scope the modules in the SOW** (`T20`, failure mode 3). 🔵 **Adoption evidence is its fork network, not its stars:** 98 forks, near-zero fork stars, institution-shaped names across **India, Indonesia, Vietnam** (`P933`). ⚠️ **Deployment-placed APAC; origin not established** |
| 🆕 **Lumen** | [ahmedEid1/Lumen](https://github.com/ahmedEid1/Lumen) | 🔴 **GPL-3.0** *(`main/LICENSE`, `35 149` B, `p274`)* — ⚠️ **its README badge says MIT** | Python/FastAPI + React | **Agentic e-learning platform, shipped to production (`2.0.0`).** A one-sentence goal becomes a **learning brief**, an authoring orchestrator builds a private multi-module course, a **course-scoped RAG tutor** answers with lesson citations and a **visible tool-call trace**, and courses can be published, moderated and remixed with server-written provenance. BYOK across four providers, envelope-encrypted. **Ships an MCP server in the official registry** (`io.github.ahmedEid1/lumen`). 🔵 **Where it fits:** the closest thing on this shelf to the *whole* reference architecture this KB recommends — authoring + RAG tutor + agent trace + BYOK — in one readable codebase. 🔴 **But the licence is GPL-3.0, not the MIT its badge claims**, so treat it as a **reference implementation and an integration target across an HTTP boundary**, not as a code base for a proprietary deliverable. **Ask upstream which grant is intended** (`T27`) |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | PHP | Lightweight LMS with the deepest LATAM public-sector footprint of any platform here. The pragmatic base for ministry-scale work in Spanish-speaking markets. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | PHP | The institutional LMS of German-speaking EMEA (DE/CH/AT), with a strong assessment module and the compliance posture that market expects. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | Java/Spring | North American higher-ed consortium LMS. **Prior cell said Apache-2.0; the payload is the Educational Community License 2.0** — Apache-derived and OSI-approved, but with patent-grant language scoped to educational use. A real distinction for a commercial deliverable. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | PHP | School management / SIS: timetabling, attendance, behaviour, pastoral records. Complements rather than replaces an LMS. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | PHP | K-12 SIS, light enough for a single school to self-host. |
| **Richie + Marsha** | [openfun/richie](https://github.com/openfun/richie) · [openfun/marsha](https://github.com/openfun/marsha) | MIT · MIT | Django + React | Course catalogue portal and education video platform from France Université Numérique. MIT, EMEA-origin, nationally proven. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | Docker-first | Multimodal tutoring platform: voice, video, configurable 3D avatars, local LLMs via Ollama. **Licence re-confirmed this pass** — the payload is the verbatim BSD-3 form; its opening *"All rights reserved"* belongs to that form and is not a reservation. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | Python/Angular | *"A free, online learning platform to make quality education accessible for all."* 6.9k stars, **5.8k forks** *(forks re-read `p295`; never previously published — a fork count this close to the star count is the deployment signature this KB reads on Submitty and Ed-Fi)*, **17,004 commits**. Structured lessons with formative feedback built into the lesson model rather than bolted on. **The second Apache-2.0 complete platform in this KB** and the highest-adoption permissive one. Its lesson structure is the cleanest place to attach a tutoring agent without touching an LMS. |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | Python/Django + Vue | *"the offline app for universal education."* 1.2k stars, **1.0k forks** *(re-read `p295`; never previously published)*, **39,803 commits**. Runs fully **offline** and syncs opportunistically — built for schools with intermittent power and bandwidth. **MIT, which makes it the first permissive full platform in this KB that is not Apache-2.0.** The right base for rural LATAM, low-bandwidth APAC and anywhere a prompt cannot assume a network. |
| **Sunbird** | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) · [project-sunbird/knowledge-platform](https://github.com/project-sunbird/knowledge-platform) | **MIT** · **MIT** | Java/Angular + mobile | **India's national education stack, and the APAC-origin platform this KB spent 265 passes declaring absent.** The codebase beneath **DIKSHA** (NCERT / Ministry of Education); README mission: *"improve learning outcomes for **200 million children across India**"*. **38,046 commits, 317 forks — and 41 stars**, which is why star-sorted search never found it. Modular by design: portal, `knowledge-platform` backend, [mobile app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). **MIT at national scale is the single most permissive large-platform option in this file** — for an APAC public-sector engagement it is the installed-base answer the way i-Educar is in Brazil. ⚠️ Slug trap: `Sunbird-Ed/sunbird-ed-portal` does not resolve; the live slugs are camel-case. |
| **Numbas** | [numbas/Numbas](https://github.com/numbas/Numbas) | **Apache-2.0** | Python 3 compiler → JS runtime | **E-assessment that executes entirely in the browser** (Newcastle University; 215★, 4,209 commits). Randomised questions, algebraic marking, SCORM-packaged output. Not a full LMS — it is the assessment engine you drop *into* one. Its architecture is the selling point under GDPR or a data-residency rule: **the submission never leaves the device**, so residency is satisfied structurally rather than by a processing agreement. |
| **i-Educar + i-Diário** | [portabilis/i-educar](https://github.com/portabilis/i-educar) · [portabilis/i-diario](https://github.com/portabilis/i-diario) | GPL-2.0 · **AGPL-3.0** | Laravel/PHP | **The Brazilian public-sector stack.** School management (SIS) plus a teacher portal, originally built by the *prefeitura de Itajaí (SC)* and published on the federal **Portal do Software Público in 2008**. 719 stars, 34,948 commits, last commits **2026-10-14** and **2026-10-09**. For a Brazilian municipal or state network this is the installed-base answer, and its provenance matches MEC's sovereignty framing exactly. **Legal note:** i-Diário's licence payload is a *Portuguese translation* of AGPL-3.0, not the FSF English text — cite the English original. |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | Ruby on Rails + React | **The market-leading LMS of North American higher education — and its source is published.** *"The open LMS by Instructure, Inc."* **78,765 commits** (2.1x Kolibri, 6.3x Artemis), 6.9k★, 3.0k forks. ⚠️ **This file previously listed Canvas under "not on the shelf" as "commercial SaaS, not a base to build on". That was wrong** — see the correction below. The practical posture barely changes, but the *reason* does: you stay out of core because of the **AGPL-3.0 network clause**, not because the code is closed. Integrate through the Canvas API, LTI (`tsugi`), or [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (**MIT**) — an **AGPL platform with an MIT doorway**. |
| **TAO** | [oat-sa/package-tao](https://github.com/oat-sa/package-tao) · [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **GPL-2.0** · GPL-2.0 | PHP (Composer) | Open-source **e-testing** platform for authoring and delivering assessments — *"created by the University of Luxembourg"*, maintained by **Open Assessment Technologies** (README-quoted → EMEA-origin). The assessment platform to know where the deliverable is *high-stakes testing* rather than coursework, which is where Artemis and Numbas stop. **GPL-2.0 is the most restrictive licence on this shelf for a commercial deliverable** — it is not even AGPL-compatible — so the boundary is the delivery API, not the engine. ⚠️ **Secondary sources routinely attach famous international assessment programmes to TAO; the README claims none, and this KB asserts none.** |
| **Schul-Cloud** | [hpi-schul-cloud/schulcloud-server](https://github.com/hpi-schul-cloud/schulcloud-server) · [hpi-schul-cloud/nuxt-client](https://github.com/hpi-schul-cloud/nuxt-client) | **AGPL-3.0** · AGPL-3.0 | Node/NestJS + Nuxt | **The European public-sector school platform this shelf was missing.** *"Schulcloud-Verbund-Software-Server"* — **16,192 commits**, 81★ — a German school-cloud stack built around data-protection-first school IT, which is the posture EMEA procurement actually tests for. The counterpart to Sunbird (APAC) and i-Educar (LATAM) in the public-sector lane. ⚠️ **Provenance is org-handle grade only** — the handle is `hpi-schul-cloud` and the README links `dbildungscloud.dev`, but **it names no ministry, funder or Land**; do not brief it as a federal programme. ⚠️ The GitHub sidebar shows a License link **with no label**; the payload is the only licence evidence. AGPL network clause applies to hosting. |
| **Tangerine** | [Tangerine-Community/Tangerine](https://github.com/Tangerine-Community/Tangerine) | **GPL-3.0** | Angular/PouchDB-CouchDB | **Offline-first *assessment* and data collection for low-resource settings** — **8,064 commits**, 70★. Runs on tablets and phones with no connectivity and syncs when a link appears; built originally for early-grade reading and maths. **The missing half of the offline lane:** Kolibri (MIT) delivers content offline, Tangerine measures learning offline. Logo is a registered trademark of **RTI International**. ⚠️ README claim, not independently verified: *"5 million+ assessments across 65 countries and 80+ organisations"* — **no country list is served**, so no named deployment is asserted. |
| **Kolibri Studio** | [learningequality/studio](https://github.com/learningequality/studio) | **MIT** | Python/Django + Vue | *"Content curation tools for Kolibri"* — **15,493 commits**, 193★, 312 forks. The authoring and publishing half of the offline stack: builds content channels Kolibri imports, **remixes channels against national curricula and special-needs requirements**, and authors learning pathways and assessments. Shelved because a Kolibri deployment without Studio is a reader with no content pipeline — and the pipeline is where a ministry engagement's actual work sits. *MIT: the copyright line carries an "(internal apps)" parenthetical; the grant clauses are unmodified standard MIT.* |
| **Koha** | [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 *(`main/LICENSE`, 35,151 B)* | Perl + MySQL/MariaDB | **The world's most deployed open-source integrated library system (ILS)** — 594★, the adjacent system of record in virtually every academic-library engagement: catalogue, circulation, acquisitions, patrons, OPAC. **Added in pass 271, and the reason it was missing is recorded rather than quietly fixed:** it has been carried on `repos/trending.md` and `agents/trending.md` for several passes and never reached this shelf, which is the one a studio reads when it needs something to stand up. Licence re-measured blind this pass and it **agrees to the byte**. 🔵 **Where the AI layer goes:** Koha's catalogue is the cleanest authority file for a retrieval index in a university engagement — subject headings and holdings are already curated, so a RAG layer over Koha starts from librarian-maintained metadata instead of scraped text. ⚠️ GPL-3.0: keep the deliverable on the API side of the boundary. |
| **H5P** *(content authoring)* | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · [tunapanda/h5p-standalone](https://github.com/tunapanda/h5p-standalone) · [sr258/scorm-h5p-wrapper](https://github.com/sr258/scorm-h5p-wrapper) | 🔴 **GPL-3.0** *(`master/LICENSE.txt`, 35,146 B)* · 🟢 **MIT** *(1,077 B)* · 🟢 **MIT** *(1,073 B)* | PHP core; JS player | **Interactive content types — the authoring ecosystem embedded inside Moodle, Canvas and Drupal**, so it is already present in most incumbent estates. **Not a standalone platform; a subsystem** — shelved here because it is a running component a client already has, not an app to deploy. 🔴 **The licence is per-repository and that is the whole point** *(discharges `ACTION PW`)*: the **authoring core is GPL-3.0** and there is **no permissive H5P authoring server**; the MIT rows are **playback** (`h5p-standalone`) and **SCORM packaging** (`scorm-h5p-wrapper`). `Lumieducation/Lumi` (desktop) is **AGPL-3.0**. 🔵 **So the buildable move is to generate H5P content and play it through the MIT runtime**, never to fork the GPL authoring core. ⚠️ Path trap: `master/LICENSE` is a **404**, `master/LICENSE.txt` is a **200**, and the default ref is `master`. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | `AGPL-3.0` *(`license.txt` — lowercase **and** `.txt` — `33 893` B, payload read `p276`)* | Frappe/Python + Vue | **A modern course platform on the Frappe stack** (courses, batches, live classes, quizzes, certificates, programmable via the Frappe API). 🔴 **Carried as `LIVE-NOGRANT` — *"no payload at eleven filenames"* — until `p276` enumerated the tree.** ⚠️ **Licence boundary:** `AGPL-3.0` reaches users over a network, so client-proprietary code must sit **outside** the deployment — call it as a separate service over the REST API, never as a Frappe app in the same bench. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| **LearnPress** | [LearnPress/learnpress](https://github.com/LearnPress/learnpress) | `GPL-3.0-or-later` *(`composer.json` + `readme.txt` `License: GPLv3`, read `p276`; **no `LICENSE` file** in 1 985 paths)* | WordPress plugin (PHP) | **The WordPress route into LMS work** — the lowest-friction platform when a client already runs WordPress. 🟢 **`p276` discharged this base's own hypothesis** that the grant lives in a plugin header channel invisible to filename probes. ⚠️ Copyleft, and the add-on ecosystem is commercial. |
| **nextSIS** | [Kosudo/nextSIS](https://github.com/Kosudo/nextSIS) | `GPL-3.0` *(`license.txt`, `39 890` B composite — nextSIS + CodeIgniter + Bootstrap — payload read `p276`)* | PHP / CodeIgniter | **A student information system, and an early-stage one** — the README says early development, and 0★. 🔴 **Carried as *"NO GRANT, 17 filenames probed"*; the grant was at `license.txt` all along.** ⚠️ **Not a starting point today** — shelved so the *licence* refusal is not what carries the exclusion. The honest reason is maturity. |
| 🆕 **Anubis** | [AnubisLMS/Anubis](https://github.com/AnubisLMS/Anubis) | 🟢 **MIT** *(sidebar, read `p297`)* | Python/Flask + Kubernetes, React front end | **The first PERMISSIVELY-licensed LMS on this table, promoted at `p297` — every other platform row here is GPL, AGPL or open-core.** *"Distributed LMS for automating Computing Science Courses From NYU"* — **382★ · 54 forks · 1 638 commits · `main`.** A student **GitHub repo per assignment**, pushes trigger tests, **results visible before the deadline**; one-click browser **Cloud IDEs**; and *"Insights"*, which infers topic understanding from submission and test-result **timestamps**. Named deployment: **NYU Tandon**, several semesters. 🔵 **Where it fits:** scoped to **computing-science courses** — it is not a Moodle replacement, and that narrowness is the point. For a CS faculty engagement it is the only row here a studio can **fork and ship without a copyleft or open-core conversation**. ⚠️ Operating it means operating **Kubernetes**; price that, not the licence. |

**24 platform rows, all licence-verified from payload** (13 from pass 264, 4 in pass 265, 5 added in
pass 267, **2 in pass 271**). Pass 267's five came from **commit-ranking and hand-probing named programmes**, not from
a topic listing — four of the five have under 200 stars and over 8,000 commits each.

## Not on the shelf — and why

| Candidate | Verdict |
|-----------|---------|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **Excluded.** Ships a bespoke *PageLM Community License*: non-commercial only, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"* without written permission. **This base's own `evidence/verified-repos.2026-10-15-p213.tsv` grades it `MIT`.** That cell is wrong and a studio acting on it would have shipped unlicensed code to a client. |
| `OpenEduCat-Inc/OpenEduCat` | **Dead.** Repository page returns 404 and no raw path serves a payload. Replaced above by `openeducat/openeducat_erp`. |
| ~~Canvas / Instructure~~ | 🔴 **CORRECTED IN PASS 267 — this verdict was wrong.** This row read *"Commercial SaaS, not a base to build on."* [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) serves an **AGPL-3.0 payload (34,520 bytes)** and has **78,765 commits** — it is the largest education codebase in this KB and it is **open source**. Canvas is now on the platform shelf above. **What this error would have cost:** a North America engagement briefed to treat the market-leading LMS as a closed incumbent to migrate *off*, when the available move is to deploy or extend it and keep the deliverable outside the AGPL boundary. Instructure's **hosted service** is commercial; its **code** is not closed, and this file conflated the two. |
| Blackboard / Anthology | Commercial, closed. Genuinely not a base to build on — the incumbent to integrate with or migrate off. See [`intel/market.md`](../intel/market.md). |
| [OpenEMIS/OpenEMIS-Core](https://github.com/OpenEMIS/OpenEMIS-Core) | **Not shelved — and the reason is worth more than the row would be.** OpenEMIS is the education-management system most associated with *ministry-level* deployment, so pass 267 probed it by hand. What is reachable is a **32-commit Docker packaging repository, 7★, with no licence on any of 76 path/ref combinations, no label in the page sidebar, and no ministry or country named in its README.** Application source not located. **Ministry provenance is not established — do not brief it as a public-sector reference.** |
| [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn) | **Not shelved — split licence, not a single grant.** 12,061 commits and a genuinely strong problem-driven assessment system, but the payload partitions the tree: Community Edition AGPL-3.0, `apps/prairielearn/src/ee/` an **Enterprise Edition under separate terms**, **all client-side JavaScript** AGPL-3.0, UIUC and outside-contributor portions MIT. The sidebar shows a License link **with no label**. Usable with legal review; **not** shelvable under one licence cell. |
| [RunestoneInteractive/rs](https://github.com/RunestoneInteractive/rs) | **Not shelved — MIT over a commercial dependency.** The grant is MIT, but the payload's first paragraph excepts the **Handsontable** component, which is **commercial software** requiring a compliance contact, plus two textbook texts under their own terms. The shape that passes a licence audit and fails procurement. |
| **Plan Ceibal (Uruguay)** | **Nothing to shelve, verified.** LATAM's most-cited national edtech programme: its `ceibal` GitHub organisation exists and states *"This organization has no public repositories"*, with no public members. Its platforms are **not open code**. A Ceibal-adjacent engagement is **integration, not adoption** — and briefing it as an open-source national stack (the way Sunbird genuinely is) would be wrong. |
| [formalms/formalms](https://github.com/formalms/formalms) (forma.lms) | **Excluded on licence, after being recommended to us.** A 2026 open-source-LMS review lists forma.lms as **Apache-2.0**. Its licence payload — `html/license.txt` — is the **GNU GPL, Version 2**. The project is alive (last commit 2026-07-17) and perfectly usable; it is simply *not* the permissive LMS that comparison implied, and it does not change the permissive count. |
| Fedena ([foradian/fedena](https://github.com/foradian/fedena), [projectfedena/fedena](https://github.com/projectfedena/fedena)) | **Excluded on abandonment.** Vendor comparisons still name Fedena as *the* Apache-2.0 education ERP/SIS. Both repositories are live pages over dead code: `foradian/fedena`'s last commit is **2012-10-12**, the community fork's is **2016-07-20** (message: *"emptying content"*). There is also no licence payload — Apache-2.0 is stated in `README.markdown` and `NOTICE` only. A Rails 2 application last touched in 2016 is not a starting point. 🔵 **`p276` read that `NOTICE` at payload for the first time** — HTTP 200, `680` B, the verbatim Apache-2.0 grant, in **both** repositories — and **upheld the abandonment dates independently** (`2016-07-20` / `2012-10-12`, re-derived from the commit graph, not re-quoted). ⚠️ **The wording *"no licence payload"* is retired on this row:** a `NOTICE` served at 200 with 680 bytes of grant text **is** a payload, and this base's own enumeration gate classes `NOTICE` as a candidate grant — so the sentence put the shelf at odds with the instrument. The accurate statement is **Apache-2.0, stated in `NOTICE` and `README.markdown`, with no `LICENSE` file in the tree.** 🟢 **The exclusion is unchanged and now rests on one reason instead of two: a Rails 2 application last touched in 2016 is not a starting point.** [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| [os4ed/openSIS-Classic](https://github.com/os4ed/openSIS-Classic) | 🟢 **RESOLVED in pass 275 — GPL-2.0, read at payload.** Carried as *"licence unverified"* for multiple passes on the strength of a 19-path x 4-ref probe. **The grant is at `docs/License.txt`** — HTTP 200, **17 286 B**, verbatim *GNU General Public License, Version 2, June 1991*, all 12 numbered terms plus the *"How to Apply These Terms"* appendix present, so the instrument is complete and **rider-cleared** per `T39`. A second copy of the same instrument sits at `docs/LICENSE.rtf` (200, 61 575 B). 🔴 **The ladder never tried `docs/License.txt`** — mixed case plus `.txt`, under `docs/` — so all 76 of its probes were structurally guaranteed to miss. Found by **enumerating the tree** (`git ls-tree -r` over a blobless clone: 5 656 files, 22 licence-like paths, 20 of them vendored ckeditor/PhpSpreadsheet/htmlpurifier). The commonly-cited GPL-2.0 claim was right; this base can now say so because it has **read** it. ⚠️ GPL-2.0 is **copyleft on distribution** — the shelving reason is now the licence's reach, not the licence's absence. |

## How to add AI on top

### Pattern A — Moodle AI subsystem (public education, lowest friction)
Moodle has shipped a provider-pluggable AI subsystem since **4.5**; **5.0** added `Explain`
and AI Reports, and **5.1** added DeepSeek support plus **per-course and per-activity
enable/disable** — which is precisely the granularity an EU AI Act compliance story needs.
Point the subsystem at a local Ollama/vLLM endpoint and no student prompt leaves the
institution. Vendor sources describe a 5.2 standardized subsystem and a 5.3 LTS in
October 2026; treat those specific version claims as **vendor-sourced and unconfirmed**
against Moodle's own release notes.

> Core Moodle still has **no** AI question generation, **no** conversational practice and
> **no** AI over SCORM content. Those three absences are the studio's billable surface.

### Pattern B — LTI tool, not a fork (works against any compliant LMS)
Build the agent as an LTI 1.3 tool with [`tsugi`](https://github.com/tsugiproject/tsugi)
(Apache-2.0), [`pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) (MIT) or
[`lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) (Apache-2.0).
The tool stays permissively licensed and the client's GPL/AGPL LMS stays untouched — this is
how you keep a copyleft platform from colouring the deliverable.

### Pattern C — XBlock inside Open edX (MOOC and corporate)
`openedx/XBlock` is Apache-2.0 and is the sanctioned extension point. The AGPL obligation
attaches to `edx-platform` itself, so keeping the agent in an XBlock is both the cleanest
architecture and the cleanest licence boundary.

### Pattern D — start AI-native (corporate L&D)
`Selleo/mentingo` (MIT) already has the agent, the tracing and the MCP endpoint. When the
client has no LMS legacy to protect, starting here beats retrofitting Moodle.

### Pattern E — offline-first, where the network is the constraint
`learningequality/kolibri` (MIT) is a complete platform that assumes no connectivity, so the
agent has to follow it: a quantised model served locally (Ollama) against Kolibri's own content
channels, with `fsrs4anki`-style scheduling for retention and sync-on-contact for telemetry.
Nothing in this stack is copylefted and nothing in it requires a data centre — which is the
only honest architecture for rural deployments in LATAM and low-bandwidth APAC.

### Pattern F — the Brazilian municipal network, sovereignty by construction
`i-educar` (GPL-2.0) holds enrolment, attendance and results; `i-diario` (AGPL-3.0) is where
teachers already work. Build the AI layer **outside both**, as a service the portals call over
HTTP/LTI, and the copyleft stays on the platform side of the boundary while the studio's model
code, prompts and evaluation harness stay permissive. The pitch writes itself: federal
software-public provenance, Brazilian maintainers, local inference, no student prompt leaving
the municipality.

### Pattern G — Sunbird for APAC public-sector scale (MIT, national precedent)

```
Sunbird-Ed/SunbirdEd-portal (MIT) + project-sunbird/knowledge-platform (MIT)
  └── already proven at DIKSHA scale under NCERT
  └── agent layer attaches at the knowledge-platform API, not in the portal
       ├── tutoring: ls1intum/Pyris (MIT) pointed at the course content store
       │            (the tutor is named "Iris"; ls1intum/Iris is an ALIAS of this repo — p282)
       ├── assessment: numbas/Numbas (Apache-2.0) embedded, browser-side execution
       └── learner model: pykt-toolkit (MIT) over Sunbird telemetry
  └── MIT throughout — no copyleft obligation anywhere in this stack
```

Why this pattern and not "import a Western LMS": a ministry that already runs DIKSHA has the
platform, the content pipeline and the political precedent. The engagement is the **agent
layer over an existing national deployment**, which is a far shorter path than a migration —
and every component above is MIT or Apache-2.0, so nothing in it forces source disclosure.

**The licence point worth putting in a pitch:** Sunbird, Iris, Pyris, Numbas and pykt are all
permissive. This is the only full stack in this file with **no copyleft component at all**.

### Pattern H — Canvas, through an MIT MCP server, not a fork *(new in pass 267)*

The highest-frequency North American situation in this file, and the one it previously had no
answer for: **the client already runs Canvas.**

1. **Leave `instructure/canvas-lms` alone.** It is AGPL-3.0 with 78,765 commits. A fork is both a
   copyleft obligation and a maintenance commitment against the fastest-moving codebase in
   education open source.
2. **Reach it with [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
   (MIT, 295★, 1,026 commits, v1.14.0 Oct 2026)** — 102–126 tools plus 8 agent skills over the
   Canvas API, speaking MCP to whatever assistant the client runs. **MIT, so the deliverable
   stays yours.**
3. **Put the pedagogy in a component that is also permissive** — [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris)
   (MIT) for the LLM pipeline with RAG over instructor material, or `tutor-mcp` (MIT) for a
   constrained tutoring loop.
4. **Grade with BSD-3, not with the LMS** — [`Submitty`](https://github.com/Submitty/Submitty) or
   [`otter-grader`](https://github.com/ucbds-infra/otter-grader), the latter of which already ships
   a **Canvas autograder adapter**.
5. **Keep the AGPL boundary at the network edge.** You call Canvas's API; you never link its code.
   Nothing in your deliverable derives from an AGPL work, and that is a sentence a client's legal
   team can check.

**Why this is the pattern and not a variation:** every licence in the delivered stack is MIT or
BSD-3, the only copyleft component is the one the client already owns and operates, and no
migration is proposed. **Where the client runs Moodle instead,** the equivalent doorway is
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) — **AGPL-3.0,
open-core, 10 free tools, 1★** — or Moodle Web Services directly. Price the Moodle variant higher;
its MCP surface is roughly 1/300th as adopted as the Canvas one.

## Declared gaps

- **Retracted twice: "permissive LMS options are one deep" → three → now five.** With
  **Sunbird** (MIT, national scale) and **Artemis** (MIT, assessment-first) the permissive
  shelf is **five** deep. Each previous count was published as though settled; the pattern is
  the lesson. The original three: **OpenOLAT**
  (Apache-2.0, institutional/higher-ed, Java), **Oppia** (Apache-2.0, structured-lesson
  delivery, highest adoption at 6.9k) and **Kolibri** (MIT, offline-first). They are not
  interchangeable — OpenOLAT is the one that behaves like an institutional LMS, Oppia is
  lesson-delivery, Kolibri is offline-first distribution — so the honest pitch is *"three
  permissive candidates, each strong at a different job"*, not *"exactly one"*. Everything
  else at full-LMS scale remains GPL or AGPL.
- **Two platforms that comparison sites recommend do not survive verification.** forma.lms is
  GPL-2.0 (published as Apache-2.0) and Fedena has been abandoned for a decade. Both were
  recommended to this KB *this pass*, by 2026-dated sources. The shelf is only as good as the
  last payload read.
- **RETRACTED in pass 266: "no APAC-origin platform on the shelf."** **Sunbird is MIT, has
  38,046 commits, and is the stack under DIKSHA** — a national deployment serving Indian school
  education under NCERT. It is now on the shelf above. This was the last surviving piece of
  this base's "APAC is supply-poor" framing, and it is gone: APAC publishes at the agent layer
  (DeepTutor, 41.5k★, University of Hong Kong), the research layer (EduData, EduStudio) **and**
  the platform layer (Sunbird, MIT, national scale).
  **The failure was instrumental, not empirical.** Star-sorted GitHub topic search is
  structurally blind to ministry-funded code: Sunbird has **41 stars against 38,046 commits**,
  so no amount of re-running the same query could have surfaced it. Rank the platform layer by
  **commits and forks**; probe national programmes by name. The earlier note that APAC
  engagements imply "localisation, not a different base" now reads the other way round for
  India specifically — the base **is** national, and the work is the agent layer on top (see
  Pattern G).
- **Star counts are deliberately absent from this file.** Platform choice here turns on
  licence, stack and deployment footprint; carrying unverified star numbers forward is how
  the errors corrected above were introduced.

### Added in pass 267

- **This file published a wrong verdict about the largest open-source LMS in its own market, for
  266 passes.** Canvas was in "not on the shelf" as *"commercial SaaS, not a base to build on"*.
  Its source is **AGPL-3.0 with 78,765 commits.** 🔵 The generalisable lesson is not "check
  Canvas": it is that **"commercial product" and "closed source" are different claims**, and this
  file merged them. Any other vendor-named row deserves the same payload test — the "incumbent to
  migrate off" framing is exactly where this error hides.
- **The permissive full-platform count is unchanged at five** (OpenOLAT, Oppia, Kolibri, Sunbird,
  Artemis). Pass 267 added five platform rows and **not one of them is permissive**: Canvas
  AGPL-3.0, TAO GPL-2.0, Schul-Cloud AGPL-3.0, Tangerine GPL-3.0 — with **Kolibri Studio (MIT)**
  the single exception, and it is a companion to a platform already shelved rather than a new one.
  🔵 **Worth stating plainly because it cuts against the trend of recent passes:** the permissive
  *agent and component* layer keeps growing, while **the complete-platform layer is still mostly
  copyleft**. Five permissive platforms is the number, and commit-ranking did not raise it.
- **The offline lane is now covered end to end, at two different prices.** Kolibri (**MIT**)
  delivers content with no network; **Tangerine (GPL-3.0)** measures learning with no network.
  Pairing them gives a complete low-connectivity deployment, but the assessment half carries
  copyleft — so the integrity of the "offline-first is a licence-free lane" claim in
  [`intel/trends.md`](../intel/trends.md) (T11) holds **only for delivery**, not for assessment.
- **Public-sector platforms now exist on this shelf for three regions** — Sunbird (APAC, MIT),
  i-Educar/i-Diário (LATAM, GPL-2.0/AGPL-3.0), Schul-Cloud (EMEA, AGPL-3.0) — **and still none for
  North America**, where the public-sector code found this pass is a UK-style *service* layer
  (`DFE-Digital`, MIT) rather than a platform. That is the remaining regional hole in this file.
  **🔴 RETRACTED IN PASS 268 — and it was never a hole, it was a shelving failure.** See
  *Added in pass 268* below: the **Ed-Fi** stack is Apache-2.0, North American, and has been
  carried as *the only permissive system of record* in this base's own gap register for roughly
  200 passes. The honest correction is narrower than the retraction, though: North America
  publishes an **interoperability and system-of-record layer**, not a platform. The sentence
  should never have said "none"; it should have said **"a different layer."**
- 🟢 **CLOSED in pass 275:** `os4ed/openSIS-Classic` is **GPL-2.0, read at payload** (`docs/License.txt`, 17 286 B). It was never unverifiable — the 19-path x 4-ref ladder simply never tried that path. Tree enumeration found it in one pass;
  `OpenEMIS`'s application source was not located; and no LATAM-origin *permissively licensed*
  platform exists — Uruguay's Ceibal, probed by hand this pass, **publishes no code at all**.

### Pattern I — Ed-Fi as the system of record for a North American engagement *(new in pass 268)*

**When the client is a US district, a state education agency, or a vendor selling into them.**
This is the pattern that was missing while this file said North America had no public-sector base.

| layer | component | licence |
|-------|-----------|---------|
| Data model | [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** |
| System of record | [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) + [`Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | **Apache-2.0** |
| New builds | [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | **Apache-2.0** |
| Agent surface over the LMS beside it | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** |
| Learner event stream | [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) + [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) | **Apache-2.0** |

🟢 **Why this composes cleanly:** every layer is permissive, so the deliverable has no copyleft
boundary anywhere — which is the thing an AGPL-first market (Canvas, Open edX) otherwise denies.
The agency's students are already modelled in Ed-Fi, so the integration is *conformance*, not
mapping.

🔴 **Three prices to quote from the register, not the README:**
1. **DMS adoption is a re-platforming with a data migration**, stated normatively in
   `docs/PRD-v8.0.md` (`Gap 303`). Never price it as an in-place cutover.
2. **DMS provisioning is create-only** (`Gap 314`). An AI deliverable that writes anything back —
   a predicted risk flag, an AI-assisted grade, generated evidence — is a **data-model extension
   and a re-provision**. The cheap route is to write AI-generated evidence into the **LRS**
   instead and leave the system of record alone.
3. **OneRoster is absent from DMS v8.0** (`Gap 309`) while native OneRoster 1.2 shipped in the
   **ODS/API 7.3.2** line. Say which line you are quoting. 🆕 **`p298` adds the bridge rather than
   just the warning:** [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
   (**Apache-2.0**, 151 commits, `main`) **serves a OneRoster 1.2 API off an Ed-Fi ODS** across Data
   Standards **4.0, 5.x and 6.1** — so a client on the ODS/API line can speak OneRoster to a vendor
   today, from a permissive grant, **without waiting on DMS.** For a non-.NET estate,
   [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) (MIT, Go, MongoDB) is the
   alternative — ⚠️ it adds non-standard `PUT` create/update/upsert beyond OneRoster's read-only `GET`
   surface, so name which surface the SOW promises.

⚠️ **Do not brief a state count.** Neither Ed-Fi README names a state or an agency; the 14-state
list is third-party, and the South Carolina department page that would settle it **did not resolve
from this environment**. Quote the licence (payload-read) and let the client's own procurement
confirm their state's status.

### Pattern J — Code.org's engine without Code.org's curriculum *(new in pass 268)*

**When the client must deliver a K-5 or K-12 AI/CS literacy mandate.** Four jurisdictions now
mandate AI instruction (`Gap 367`), and this is the shape of the only honest answer.

- ✅ **Reuse under Apache-2.0:** [`code-dot-org/code-dot-org`](https://github.com/code-dot-org/code-dot-org)'s
  **platform** — 215,796 commits of lesson delivery, progress tracking, classroom management and
  block-based programming environment. This is a genuinely enormous permissive engine.
- 🔴 **Do NOT plan to reuse:** the lessons, videos, artwork, characters, sounds, logos or fonts.
  The payload confines them to *"Code.org's own web site, mobile applications, or social media
  channels ... without modification or embedding in another format"*, and the `NOTICE` shows why
  Code.org could not grant them anyway — the engaging activities are **licensed entertainment IP**
  (Minecraft, Star Wars, Frozen, Ice Age, Angry Birds, Plants vs. Zombies, Gumball, The Bad Guys),
  plus **Font Awesome Pro**.
- 🟢 **So the engagement is content origination on a free engine**, and the budget belongs in
  instructional design and localisation, not in platform build. 🔵 **Say this in the first
  meeting.** A client who has seen Code.org assumes the curriculum comes with the code; the
  licence says the opposite, and discovering that after the SOW is signed is the expensive way.


### Pattern K — an MEA ministry mandate, where there is no regional platform to start from *(new in pass 269)*

🔴 **State the absence first, because it is the whole shape of the engagement.** Pass 269 ran the
Kenya / Nigeria / South Africa / Egypt legs this base specified in pass 267 and never executed.
**There is no African or Middle Eastern education platform on this shelf, and pass 269 did not find
one.** What it found instead:

- **Two African-context education agents, both serving NO GRANT** —
  [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South Africa, Grades 8–12,
  **pre-licence**: the README still carries *"Add the project's chosen license here before
  publishing"*) and [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria, no
  payload on 19 paths and no `license` field in `package.json`).
- **Two named national systems that are unreachable rather than absent** — Nigeria's **Naija Teacher
  AI** (UNESCO SDG4 case study, offline-first, target **1.5M teachers by Q3 2026**) **states no
  licence**; Kenya's **Kytabu SOMANASI** is **proprietary**.
- **One piece of Africa-engaged permissive code, already on this base's shelves** —
  [`AI-for-Education/lesson-plan-parse-mbsse`](https://github.com/AI-for-Education/lesson-plan-parse-mbsse)
  (**MIT**, Sierra Leone MBSSE national lesson plans → structured JSON, corpus shipped) —
  **research-grade, a method rather than a dependency.**

🟢 **So the platform layer is imported and the national layer is built.** The stack is
`kolibri` (**MIT**, offline-first, 39,803 commits) for delivery, `instructional_agents` (**MIT**,
EACL'26) for teacher-facing authoring, `Claw-ED` (**MIT**) for local-first drafting, `lineage-skill`
(**Apache-2.0**) for provenance, and `Tangerine` (**GPL-3.0** ⚠️, 5M+ assessments across 65
countries per its README) **deployed beside the deliverable, never linked into it**, where national
assessment is in scope. The per-country work — parsing the national curriculum into structure,
language, teacher capability — is the billable part and the part that does not port.

🔵 **Entry point differs by country, and getting it wrong wastes the first meeting.** Kenya and Egypt
have **national anchors** (the KDEAP rollout; the UNESCO teacher-competency framework of
**2026-06-03**), so a ministry conversation has an instrument to attach to. **South Africa has no
national instrument at all** — its Draft National AI Policy 2026 was **abrogated on 2026-04-27** —
while **North-West University became the first SA university with an official AI policy in January
2026**. **Enter South Africa at institution level.** Full recipe: [`compose/patterns.md`](../compose/patterns.md) `P19`.

⚠️ **And two things not to say.** Egypt's delivery platform is reported three different ways
(**QUREO** / the Japanese **Kiryo** / a **Sprix** contract approved January 2026) — **brief the
framework, not the vendor.** And every regional figure here is **secondary-source grade**: `p268`
established the non-GitHub DNS failure as environmental, and no ministry document was read.

## Pass 280 — no new permissive platform for a sixth pass, and the one candidate the leg returned has no readable licence

🔵 **Evidence:** [`p280-inbound-raw.2026-10-18-p280.txt`](../evidence/p280-inbound-raw.2026-10-18-p280.txt)
*(the platform leg, verbatim)*.

🔴 **The mandated platform leg returned what this shelf already holds**, and the comparison pages it
surfaced were mostly one vendor's own site:

| what the leg named | this shelf's position |
|---|---|
| **Moodle** — GPLv3, most widely deployed, **LMS-only, no integrated SIS** | 🟢 CARRIED. `p273` established the plugin door is permissive; the core is GPL-3.0 |
| **Open edX** — AGPLv3, originated at **MIT and Harvard**, now stewarded by **Axim Collaborative** | 🟢 CARRIED |
| **Richie** (MIT) and **Aspects** (Apache-2.0), both built on Open edX | 🟢 CARRIED — components, not platforms |
| 🟡 **OpenEduCat** — the **only** LMS **+ SIS** combination the leg found, *"consolidates LMS, SIS, fees and parent app on one database"* | 🔴 **the source does not state its licence**, and the pages describing it are **its own**. 🔵 Not shelved as a licence on a vendor's self-description — the question for `p281` is a payload read, not another search |

🔵 **The structural point a studio needs is unchanged and was restated by this leg from the other
side:** the deployed platforms in this industry are **copyleft** (Moodle GPL-3.0, Open edX AGPL-3.0),
and the permissive surface is in the **extension points** — plugins, XBlocks, MCP servers, design
systems. 🟢 **That is where this base's build-on tier lives, and it is a consequence of the licence
map rather than a preference.**

### 🔵 A deployment constraint for every platform on this shelf, from three jurisdictions

**China** (MOE's 2025 generative-AI guide), **Brazil** (`Parecer CNE/CP nº 15/2026`, pending
homologation) and **Singapore** (teacher roadmap, `p279`) independently prohibit or withhold
**autonomous generative-AI use by the youngest learners** — primary pupils, up to the 5th year, and
P1–P3 respectively. 🟢 **For a platform integration this is a routing requirement**: the pupil-facing
surface must be able to run **teacher-mediated**, with the teacher as requester, per class or per year
group. 🔴 **No platform on this shelf ships that as a built-in mode** — Moodle and Open edX both have
the role model to express it, which makes it buildable rather than blocked.

## Pass 279 — no new permissive platform for a fifth pass, and the hardest procurement mandate on this shelf was legislated away

🟡 **The mandated platform query returned this base's own shelf.** Moodle, Open edX, Sakai, ILIAS,
Canvas, Chamilo and OpenEduCat all came back; **every one is already here**, and `make carried` was run
on each **before** the nil was written up. 🔴 **Fifth consecutive pass with no new permissive
platform** — and, as in `p278`, the results carried **no licence detail at all**, so nothing in them
could have been shelved on their authority anyway. 🔵 **One genuine gap in the search itself: no
open-source SIS comparison exists to be found.** `OpenEduCat` was the only result described as an
education ERP, which is why the SIS question on this shelf keeps resolving to it.

### 🔴 The platform decision that changed is a POLICY one, and it removes a mandate

**Korea reclassified AI digital textbooks out of "textbook" status** — amendment to the Elementary and
Secondary Education Act, reported **August 2025** — so **adoption is optional**: Korean and home
economics are excluded, social studies and science **delayed to 2027**, the review for 2026-year
products **halted**, and **~10 publishers sued the government in June 2026 for roughly KRW 200bn**.
Full detail in `intel/trends.md` `T62`.

🟢 **Why that belongs on a PLATFORM shelf.** A procurement mandate is what makes a vertical platform
buyable at national scale, and this one evaporated in under two years with its vendors in court.
🔵 **So sequence a platform recommendation against what an institution may CHOOSE** — which is what
every row on this shelf is already scoped for, since a self-hostable open platform survives a mandate
reversal and a proprietary national programme does not.

### 🟢 Where a platform engagement has a dated hook instead

| jurisdiction | hook | what it implies for the platform choice |
|---|---|---|
| 🟢 **Singapore** | **every** primary/secondary/JC teacher must finish MOE AI modules by **end-2027**, **module 1 by end-2026** | 🔴 **the student channel runs on MOE's own tools on SLS** — so the platform work is teacher-facing and institutional, not classroom delivery |
| 🟢 **India** | **CBSE Circular Acad-15/2026**, Classes **III–VIII**, session **2026-27** | 🔴 **AI is NOT a standalone subject** — computational thinking is woven across subjects, so the need is cross-curricular content and assessment inside an existing LMS, not a new one |
| 🟡 **Canada (Ontario)** | no province-wide guidance, but a **Ministry-mandated AI PD day (2026-04-17)**, plus **Bill 194 (2024)** binding school boards | 🟢 the buyer is the **board**; the first deliverable is policy and training on whatever platform they already run |

⚠️ **Unchanged and still un-dischargeable here:** the **Canvas Free-for-Teacher** discontinuation
remains unverified — `instructure.com` and `community.canvaslms.com` are both unreachable from this
environment, on **both** fetch channels *(`T61`)*. **Do not promise a zero-cost Canvas environment in
a proposal.**

---

## Pass 278 — four platforms on this shelf declare MIT in a manifest while committing AGPL-3.0, and a client's own CI will wave all four through

🔵 **Evidence:** [`channel-conflict.2026-10-17-p278.tsv`](../evidence/channel-conflict.2026-10-17-p278.tsv)
*(14 slugs, both channels, pinned refs)*. Instrument:
[`compose/code/p278-channel-conflict/`](../compose/code/p278-channel-conflict/), wired into
`make hooks` as `make gate-conflict`.

🟢 **`p121` measured this in October 2026 and the measurement REPRODUCES six days on, to the byte.**
Every one of these is a platform or platform-shaped product a studio could be asked to build on:

| platform | manifest declares | committed payload, **re-read this pass** | direction |
|---|---|---|---|
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 🟢 **MIT** (`package.json`) | 🔴 **AGPL-3.0**, `LICENSE` **34,523 B** | 🔴 **permissive over network copyleft** |
| [`codelitdev/courselit`](https://github.com/codelitdev/courselit) | 🟢 **MIT** (`package.json`) | 🔴 **AGPL-3.0**, `LICENSE.md` **34,143 B** | 🔴 **permissive over network copyleft** |
| [`tadreeb-lms/tadreeblms`](https://github.com/tadreeb-lms/tadreeblms) | 🟢 **MIT** (`composer.json`) | 🔴 **AGPL-3.0**, `LICENSE` **34,523 B** | 🔴 **permissive over network copyleft** |
| [`leemonade/leemons`](https://github.com/leemonade/leemons) | 🟢 **MIT** (`package.json`) | 🔴 **"Fair Code License" v1.0**, `LICENSE.md` **10,830 B** — **€100,000 past 1,000 users + 5%** | 🔴 **permissive over billed** |
| [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | 🟢 **MIT** (`package.json`) | 🔴 **`CC-BY-NC-SA-4.0`**, `LICENSE.md` **1,891 B** | 🔴 **permissive over NON-COMMERCIAL** |

🔴 **One of those rows is a CORRECTION to `p121`, not a reproduction.** `p121` recorded
`cccareers/open-source-curriculum`'s payload as *"🟡 **CC-BY** family"* and typed the direction
*"permissive over attribution-share"*. **The payload read first-hand this pass is `CC-BY-NC-SA-4.0` —
non-commercial.** 🔵 **"Attribution-share" reads as "ship it with credit"; NC forbids the client
deliverable outright.** On a **curriculum** repository — precisely the kind of asset a studio reuses in
a training engagement — that gloss is the expensive kind of wrong. **Corrected on this shelf and in
`repos/trending.md`.**

🔵 **What a studio must take from this, stated as a rule rather than a list.** `p121` named the
mechanism and it has not changed: **every licence gate in a client's CI reads the MANIFEST.**
`npm ls --json`, `pip-licenses`, most SBOM generators and most SCA scanners report the declared field.
On these five addresses that gate returns *"permissive, pass"* and the copyleft, the €100,000 or the
non-commercial bar **ships undetected into the deployment**. 🟢 **The intake rule: a manifest licence
field is a HINT; the committed licence file, on the default branch, at a pinned SHA, is the GRANT.**

🟢 **And it is a standing check now, not a census.** `p121`'s table was built by hand at one moment
with each verdict typed per row; `make gate-conflict` re-derives **all ten** published directions from
their own family cells on every run, so a typed verdict can no longer drift from the evidence beside
it. 🔵 `make conflict-sweep SLUGS=f` is the online half and stays out of `hooks`.

⚠️ **Scope, stated plainly: this changes nothing about what Globant may build on.** Four of the five
were already excluded as copyleft or billed, and they remain excluded — **for the reason that is
actually true**, which is the point `p276` made about refusing an engagement correctly. The permissive
full-platform count is **unchanged at five** (OpenOLAT, Oppia, Kolibri, Sunbird, GegoK12).

🟡 **Fourth consecutive pass with no new permissive platform.** The global platform query returned this
base's own answer: **GegoK12**, MIT, already shelved since `p274`. `make carried SLUG=Gego-K12/gegok12`
returns `CARRIED` and was run **before** the leg was written up — the check `p277`'s conflict claim
skipped. See [`p278-websearch.2026-10-17-p278.tsv`](../evidence/p278-websearch.2026-10-17-p278.tsv),
leg 11.

## Pass 277 — no new permissive platform exists to find, and the free Canvas door this shelf's sequencing assumes may have closed

🟡 **An informative nil, stated with the query that produced it.** Leg 11 ran
`open source student information system LMS 2026 Apache MIT license self-hosted`. 🔴 **No MIT platform
was located, and the only clear Apache-2.0 LMS returned was `OpenOLAT` — which this shelf already
payload-verified at `p272`** (`master/LICENSE`, 10,982 B). Everything else returned was copyleft and
already here: **RosarioSIS, Gibbon, Moodle, Chamilo** (GPL), **Open edX** and **Canvas** (AGPL).

🔵 **So the headline of this shelf is unchanged, and now it is unchanged *after* a deliberate attempt to
change it:** `OpenOLAT/OpenOLAT` remains **the only permissive full LMS on this base**, and the
permissive full-platform count stays at **five** (OpenOLAT, Oppia, Kolibri, Sunbird, GegoK12). **Three
consecutive passes have searched for a sixth and not found one.** That is now a property of the
ecosystem rather than a gap in this shelf's coverage.

⚠️ **One licence claim deliberately NOT shelved:** **Forma LMS** was returned as **Apache-2.0 by one
source and GPL by another**. This shelf does not carry a licence it has not read, and neither source is
a payload. **Left off entirely rather than tabled with a question mark** — a row with a disputed licence
is worse than no row, because only the row gets copied into a proposal.

### 🔴 The claim that would cost something if true: Canvas Free-for-Teacher

**A secondary source states that Canvas *Free-for-Teacher* — Instructure's hosted free tier — was
permanently discontinued in May 2026.**

⚠️ **GRADE: SECONDARY, UNVERIFIED, AND UNVERIFIABLE FROM HERE.** `instructure.com` is
**DNS-unresolvable in this sandbox** (`getaddrinfo ENOTFOUND`, reproduced via two different tools);
only `github.com` and `raw.githubusercontent.com` resolve. **It is recorded, not asserted.**

🔵 **Why it is recorded at all, rather than dropped as unverifiable.** It does not touch a licence — the
AGPL-3.0 payload of [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) is read and
unaffected — but it touches **this base's own recommended sequencing**. `compose/patterns.md` tells a
studio to *"stand up `canvas-mcp` read-only against a sandbox"*, and `P28`/`Pattern H` make Canvas the
shortest path to a live client system precisely because the doorway is cheap. 🔴 **If the free hosted
tier is gone, the cheap sandbox is gone with it**, and the first week of that engagement becomes either
a self-hosted AGPL deployment (**78,765 commits** — not a week) or a commercial trial the client has to
sponsor.

🟢 **What does NOT change either way, and should be said so the uncertainty is bounded:** the **two MIT
doorways** stand on their own payloads —
[`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) and
[`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) — and **a client that
already runs Canvas needs no free tier at all.** 🔵 **The exposure is narrow and specific: it is the
*unsponsored pilot*, the demo built before a client has committed an environment.** `p278` with egress
should settle it in one fetch, and until then **do not promise a zero-cost Canvas environment in a
proposal.**

## Pass 276 — three platforms were excluded by a licence verdict that was never a reading, and Fedena's exclusion now rests on the right reason

**Working 30 rows of `p275`'s enumeration queue put three real platforms back on this shelf** — not by
finding them, but by reading the grants that were always in their trees:
[`evidence`](../evidence/tree-enumeration.2026-10-17-p276.tsv).

| platform | the verdict that kept it off this shelf | what the tree actually serves |
|---|---|---|
| **Frappe LMS** | *"`LIVE-NOGRANT` — no payload at eleven filenames"* | `license.txt` — `AGPL-3.0`, `33 893` B |
| **nextSIS** | *"NO GRANT — 17 filenames probed on `master`"* | `license.txt` — `GPL-3.0`, `39 890` B |
| **LearnPress** | *"no payload / 24"* | `composer.json` `GPL-3.0-or-later` + `readme.txt` `License: GPLv3` |

🔵 **All three are copyleft, so none of them changes what Globant can build on.** That is exactly why the
correction matters: **an engagement must be refused for the reason that is true.** A platform excluded as
*"ungranted"* gets revisited the moment someone finds a licence; a platform priced as `AGPL-3.0` with a
stated boundary is a decision that holds.

### 🔵 Fedena: the exclusion is unchanged and now rests on one reason instead of two

This file said two things about Fedena in two places, **336 lines apart**: row 71 recorded that
Apache-2.0 *"is stated in `README.markdown` and `NOTICE`"*, while the later audit row called the same
claim **NOT ESTABLISHED**. 🔴 **`p276` read that `NOTICE` at payload — HTTP 200, `680` B, the verbatim
Apache-2.0 grant, in *both* repositories — so the claim is established by the project itself**,
independently of the competitor comparison page `p272` correctly distrusted. 🔵 **The reasoning was right
and the verdict was wrong: refusing a *claim* is not the same as refusing its *source*.**
🟢 **The abandonment dates were re-derived from the commit graph rather than re-quoted** (`2016-07-20`,
`2012-10-12`) and they **hold** — and they were always the whole reason to exclude Fedena.

🔴 **`p274` found this exact shape for `Bloom` and recorded that `T29`, `T34` and `T37` all miss an
intra-file qualitative contradiction. This is the second instance, in a different file, still uncaught.**

### ⚠️ A scope distinction this shelf now has to carry

`learningequality/kolibri-server`'s grant is `debian/copyright` — **DEP-5**, `GPL-2+`, whose `Files:`
stanzas name **five packaging paths**. That is a packaging grant, not a blanket repository grant, and a
shelf that records one licence per row cannot express it. Recorded here rather than flattened.


## Pass 275 — `openSIS-Classic`'s grant was read, after being declared unreadable for multiple passes

⏱️ **Twenty-first pass of `2026-10-17`.** Evidence:
[`tree-enumeration.2026-10-17-p275.tsv`](../evidence/tree-enumeration.2026-10-17-p275.tsv) ·
[`verified-repos.2026-10-17-p275.tsv`](../evidence/verified-repos.2026-10-17-p275.tsv).

🟢 **`os4ed/openSIS-Classic` = GPL-2.0, read first-hand at `docs/License.txt`** (HTTP 200, **17 286 B**,
verbatim *GNU GPL Version 2, June 1991*; all 12 numbered terms plus the *"How to Apply These Terms"*
appendix, so the instrument is complete and **rider-cleared** per `T39`; a second copy of the same
instrument at `docs/LICENSE.rtf`, 200, 61 575 B).

🔴 **This base said, five times across three shelves, that the payload did not exist.** It did. The
`19-path × 4-ref` ladder tried `docs/LICENSE`; the file is **`docs/License.txt`** — mixed case *and*
`.txt` *and* under `docs/`. An earlier cell recorded *"no payload in **17 filenames**"*; the 17 did not
include it. All five occurrences are corrected, and the two on the **append-only** `repos/trending.md`
are annotated in place with a dated supersede marker rather than rewritten.

⚠️ **The shelving reason changes rather than disappears.** openSIS is **copyleft on distribution**, so
scope an engagement on the licence's **reach** — not, as this base had it, on a missing grant. 🔵 It
remains **excluded from the zero-copyleft stack (`P22`)**, and is now a *known* GPL-2.0 option rather
than an unknown.

🔵 **Still open on this shelf, and now measured:** `Open-TutorAi/open-tutor-ai-CE`, both `fedena`
slugs, and **124 negative licence verdicts across this base** rest on a path ladder rather than an
enumeration (`make gate-enumeration` prints the queue). `GegoK12`'s MIT core stands as `p274` corrected
it — and the stale *"NOT ESTABLISHED"* restatement that sat further down this file is reconciled with it.

## Pass 274 — this shelf gains an MIT administrative platform, and the reason it was missing is a slug

⏱️ **Twentieth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p274.tsv`](../evidence/verified-repos.2026-10-17-p274.tsv) ·
[`p274-websearch.2026-10-17-p274.tsv`](../evidence/p274-websearch.2026-10-17-p274.tsv).

🟢 **Two rows added, and neither came from a discovery.** One came from **re-probing a refusal** and one
from **grepping this base's own census**.

| row | licence at payload | why it was not here |
|---|---|---|
| **GegoK12** | 🟢 **MIT**, `1 150` B | 🔴 **Refused twice on a slug that does not exist.** `gegok12/gegok12` fails `ls-remote` exactly as a nonexistent repo does; the real slug is `Gego-K12/gegok12`. The refusal recorded *"no payload on 15 path/ref combinations"* — **15 probes against a string, reported as thoroughness** |
| **Lumen** | 🔴 **GPL-3.0**, `35 149` B | 🟡 **Held in this base's `p195` licence census and never promoted to a shelf** — the `T34`/`T25` species again. Its README's **MIT badge** is the reason it matters: a reader would mis-price it in the permissive direction |

### 🔵 What the two rows change about this shelf's shape

🔴 **Before this pass every *administrative* system here was copyleft** — OpenEduCat LGPL-3.0, i-Educar
GPL-2.0, Gibbon/RosarioSIS GPL, Koha GPL-3.0 — while the permissive options were all **LMS or
assessment** (OpenOLAT, Artemis, Mentingo, Kolibri). 🟢 **GegoK12 breaks that pattern: MIT, on the SIS
/ ERP layer**, which is the layer a district or a ministry actually owns and the one where this base's
`P22` zero-copyleft engagement previously had no answer at all.

⚠️ **With two prices named rather than buried:** the Pro modules are commercial (so the *free* feature
set is what MIT covers), and the fork evidence places **deployment** in APAC, not **origin**. 🔵 **For a
LATAM or EMEA public-sector bid this is a reference architecture with live institutional deployments
behind it, not a regional incumbent** — which is the honest way to cite it.

🟢 **And one negative result from the same leg, worth more than it looks:** **not one** of the SIS/ERP
platforms the leg returned describes **any AI feature**. **The administrative layer of education software
has no AI in it.** That is this base's standing thesis — platform as installed base, agent as the
deliverable — **confirmed from outside the base for the first time**, by a survey of the category that
was not looking for it.
## Pass 272 — the permissive LMS recommendation is now rider-cleared, and two vendor licence claims died at payload

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) *(5 repositories)*.

🟢 **`OpenOLAT` is the single most load-bearing row on this shelf** — it is what this file tells a studio
to use when procurement rules out copyleft, so its grant deserves more than a licence label.
`p272` read the payload and found **10,982 B against stock Apache-2.0's 11,357 B**. 🔵 **A *short* Apache
file is the shape of a rider**, and `p252` found a real **Commons Clause** on a row this base had blessed
for four passes. 🟢 **Diffed: the whole terms section is byte-identical to upstream; the missing span is the
optional APPENDIX, replaced by provenance notes with no legal effect.** Recommendation stands and is now
**rider-cleared**, not merely licence-labelled. The generalisation is `T39`.

### 🔴 Two platforms a vendor comparison recommends, both refuted at payload

The brief's SIS/ERP leg surfaced two permissive claims. **Neither survived.**

| platform | the claim, and who makes it | `p272` verdict |
|---|---|---|
| **GegoK12** | *"free core is free forever under the MIT licence; 26 of 38 modules free, 12 Pro modules $100–$250"* — a vendor listing | 🟢 **ESTABLISHED — corrected in `p274`, and this cell was still carrying the refutation 40 lines below that correction (fixed in `p275`).** The grant is **MIT**, read at payload: [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) `main/LICENSE`, HTTP 200, **`1 150` B**, zero rider keywords. 🔴 The earlier *"NOT ESTABLISHED — no licence payload on 15 path/ref combinations"* was **15 probes against a string**: the slug `gegok12/gegok12` does not exist and fails `ls-remote` identically to any nonexistent repository (re-confirmed in `p275`'s positive-control sweep, `rc=128`). ⚠️ **The open-core caveat still stands and is the reason to scope carefully:** **MIT core plus paid modules** (26 of 38 free, 12 Pro at \$100–\$250) means the grant covers a *subset* of the product a client is shown. Shelvable on the licence; scope on the module split. |
| **Fedena** | Apache-2.0, per a comparison page | 🔴 **NOT ESTABLISHED, and this independently reproduces `p265`'s refutation.** `p272` adds *why the false claim circulates*: the page asserting Apache-2.0 is **openeducat.org — a direct competitor's comparison**. ⚠️ **A licence claim sourced from a rival vendor is not a licence.** 🔴 **REFUTED `p276`, and the file contradicted itself for several passes:** row 71 of **this same file** has been stating that Apache-2.0 *"is stated in `README.markdown` and `NOTICE`"* while this cell, **336 lines below it**, called the same claim *NOT ESTABLISHED*. `p276` read the `NOTICE` at payload — HTTP 200, `680` B, verbatim Apache-2.0 grant, in **both** repositories — so the claim is **established by the project itself**, independently of any comparison page. 🔵 **The reasoning here was right and the verdict was wrong:** a licence claim sourced from a rival vendor is indeed not a licence, but refusing the *claim* is not the same as refusing the *source*, and the project's own tree answered it all along. 🔵 **`p274` found this exact shape for `Bloom`** (tabled in one tier, declared unresolvable 168 lines below) **and recorded that `T29`, `T34` and `T37` all miss an intra-file qualitative contradiction. Second instance, same file, still uncaught —** `p277` should build that check rather than find a third. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |

🟢 **One claim did survive, and it beat its own source.** `academico-sis/academico` — already shelved
here — is served **MIT at payload (1,094 B)** while the comparison page that surfaced it says the licence
*"is not named"*. **The first-hand read was better than the aggregator in the one case the aggregator was
hedging.** That is the asymmetry worth keeping: aggregators are wrong in both directions, and only the
payload settles it.

⚠️ **Unchanged by this pass:** the permissive full-platform count stays at **five**, and **no education ERP
under MIT or Apache-2.0 has been located** — now tested from a second channel (`p271` tested it from the
platform/ERP leg, `p272` from the SIS/school-management leg) with the same result.

## Pass 271 note — two real platforms were on the other shelves and not on this one

🔴 **This shelf was missing two licence-verified, actively maintained systems that the base already
held elsewhere**, and the omission is recorded as a defect rather than silently patched:

| platform | where it already lived | why the absence counted |
|---|---|---|
| **Koha** (GPL-3.0, 594★, ILS) | `repos/trending.md`, `agents/trending.md` | the shelf a studio reads for *"what can we stand up"* did not list the most-deployed open-source library system |
| **H5P** (GPL-3.0 core + MIT playback) | `repos/foundations.md`, `repos/trending.md` | present in most incumbent Moodle/Canvas estates already, so it is an integration surface on nearly every engagement |

🟢 **Both were checked against this file's own "Not on the shelf — and why" table first — neither was
there**, so neither had been excluded on judgement. 🔵 **This is `T34`'s defect class on the verticals
shelf**: the datum existed, the file that needed it did not have it, and nothing in either file
contradicted the other, so no `grep` for a *disagreement* would have found it. **The check that finds it
is asking, of each shelf, "what should be here that is held somewhere else?"**

🟢 **The H5P row also discharges the register's `ACTION PW`** by doing what it asked — naming the
repository in the cell. The MIT-vs-GPL "conflict" was **two repositories with two grants**, so both
prior cells were right and the defect was the project-level cell. **Every multi-repository project on
this shelf now needs its repository named**, and the commercially load-bearing consequence is stated in
the row: **there is no permissive H5P authoring server**, so a deliverable generates content and plays
it through the MIT runtime rather than forking the GPL core.

🔵 **No other platform rows changed, and the three generic platform/ERP/SIS legs returned nothing new
for the sixth consecutive pass** — including an explicit negative worth keeping: **no education ERP
under MIT or Apache-2.0 was located.** The permissive end of this shelf remains **OpenOLAT**
(Apache-2.0), **Oppia** (Apache-2.0), **Kolibri** (MIT, on `develop`), **Sunbird** (MIT), **Artemis**
(MIT), **Richie + Marsha** (MIT) and **Numbas** (Apache-2.0). ⚠️ One leg returned ten results from a
**single vendor's glossary** across ten localised URLs — *ten results, one source*, which is `T33`'s
single-aggregator failure in a different channel.

🟢 **New in `intel/market.md` and relevant to a Dutch engagement off this shelf:** the Netherlands has a
**dated** AI-literacy mandate — `kerndoelen digitale geletterdheid`, AI literacy explicit, **primary +
lower-secondary**, legally official **2027-08-01**, inspected from **2031**. See new pattern **`P21`**,
which wires it to **Moodle** and the **MIT** H5P runtime rather than to the GPL authoring core.

## Pass 270 note — what the platform shelf does and does not cover, after the EMEA re-verification

🟢 **No platform rows were added this pass, and none needed changing.** The only supply leg run
(`Gap 367`'s Spanish limb) returned nine repositories, eight of them university student course
portfolios and the ninth already held. The three generic platform/ERP/SIS legs were **deliberately
not re-run** — `p269` measured them saturated across four consecutive passes and instructed that
they be spent last. **This file's shelf is stable, and that is a measurement, not an omission.**

🔴 **But pass 270 found the shelf's sharpest gap by looking at what a national government actually
bought.** Estonia — the one EMEA jurisdiction where national-scale deployment is a *measured fact*
rather than a plan — has **~half of its 20,000 upper-secondary students** on an **OpenAI-partnered
proprietary platform** (Education and Research Minister **Kristina Kallas** to *Politico*, **May
2026**). 🔵 **Every platform on the shelf above is open source, and the country that moved fastest
in Europe did not pick one of them.**

🟢 **That is not an argument that the shelf is wrong — it is the sales argument for the shelf**, and
it has a number attached. The **Sanoma Learning 2026 European Teacher Survey** (>20,000 teachers,
14 countries) found **63% of European teachers using AI** and **only 16% believing general-purpose
AI improves learning outcomes** (`T28`). **A proprietary general-purpose platform is exactly what
84% of them are unconvinced by.** The platforms here — **Moodle** (GPL-3.0, with its
provider-pluggable AI subsystem since 4.5), **Open edX**, **Canvas** (AGPL-3.0 at source),
**Kolibri** (MIT **on `develop`**, 404 on `main` — the ref matters, `p269`) — are the ones that can
be bound to a client's own curriculum and assessment rules, which is the thing the general-purpose
tool cannot do.

⚠️ **One category correction, so this file is not read as offering something it does not.**
[`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia) (**CC BY-SA 4.0**, verified at
payload this pass) appears in `agents/trending.md`, `repos/trending.md` and new pattern **`P20`** —
but it does **not** belong on this shelf and has not been added to it. **It is a prompt/knowledge
framework (schemas + prompts for LOMLOE programaciones), not a running platform**: GitHub detects no
language in it, and it is 0 stars at 50 commits. **This shelf is for systems a client can stand up
and put an agent on top of.** `OpenDidactia` is read as a specification, never deployed — see `P20`
for the ShareAlike boundary that distinction rests on.
