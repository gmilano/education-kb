---
industry: education
region: Global
updated: 2026-10-28
---

# Education platforms you can customise with AI on top

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it with two platform rows read from bytes and a resolved Fedena entry. Pre-p490
sections remain in
[`archive/2026-10-27-p490-pre-rewrite/solutions.md`](../archive/2026-10-27-p490-pre-rewrite/solutions.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

The "Odoo for education" question, answered by layer. Each row is a real, deployed system with a
license read from bytes at a pinned SHA — see
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## Pick by layer

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| **LMS — mass market** | [Moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | Largest installed base; 2,000+ plugins. A Moodle plugin is the lowest-friction way to ship AI into an existing institution. |
| **LMS — higher ed / MOOC** | [Open edX](https://github.com/openedx/edx-platform) | AGPL-3.0 | 8,200 | University and workforce standard. Deploy via [Tutor](https://github.com/overhangio/tutor) (AGPL-3.0), not by hand. |
| **LMS — North America HE** | [Canvas LMS](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6,900 | Dominant in US higher ed. Has a real MCP server already: [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) (MIT, 309★). |
| **LMS — permissive** | [OpenOlat](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 448 | **The only permissive full LMS found.** Pick this when the client needs a closed derivative. |
| **LMS — offline-first** | [Kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,200 | Runs without connectivity. Decisive for rural LATAM/Africa/APAC and for national programmes. |
| **LMS — ease of use** | [Chamilo](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | Francophone + LATAM public sector. |
| **LMS — DACH** | [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | German universities and public sector; SCORM-strong. |
| **LMS + AI mentoring** | [mentingo](https://github.com/Selleo/mentingo) | **MIT** | 100 | Small, modern, AI-native, multi-tenant via Postgres RLS. The best permissive *starting codebase* rather than a migration target. |
| **LMS — modern/greenfield** | [LearnHouse](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2,400 | **New `p491`.** "Next-gen" course and content platform, modern stack. Larger than Kolibri or Chamilo by stars and previously missing from this KB. 🔴 AGPL — not a closed-SaaS base. Default branch `dev`. |
| **SIS / school mgmt (Frappe)** | [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared)* | 682 | **New `p491`.** Admissions, students, programmes, fees on the Frappe stack. 🔴 Grant is a **19-byte stub** naming GPL v3 with no license text — family is GPL-3.0, paperwork is incomplete. **Not the same license as `frappe/lms` (AGPL-3.0).** |
| **Education ERP** | [OpenEduCat](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | Admissions, fees, library, hostel, timetable — on Odoo. This is the literal Odoo answer. |
| **SIS (K-12)** | [RosarioSIS](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | Enrolment, scheduling, grades, attendance, billing. |
| **School management** | [Gibbon](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | Teacher/student/parent/leadership workflows. |
| **Assessment / exams** | [TAO](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based testing. The only substantial open assessment engine. |
| **Interactive content** | [H5P](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | 50+ interactive content types; embeds into Moodle, Canvas, Open edX. |
| **Virtual classroom** | [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,300 | Live classes with whiteboard and breakouts. **LGPL — linking allowed**, the friendliest copyleft here. |
| **Structured lessons** | [Oppia](https://github.com/oppia/oppia) | **Apache-2.0** | 6,900 | Lesson "explorations" with built-in misconception handling. Permissive. |
| **Spaced repetition** | [Anki](https://github.com/ankitects/anki) | AGPL-3.0 | 32,300 | Reference SRS scheduler. Use as the algorithm reference even where the code can't ship. |
| **Interactive classroom / courseware** | [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | **41,700** | 🟢 **New row `p493`** (restored — see below). Topic or document → multi-agent interactive lesson with slides, quizzes, project work. **The largest permissive asset in this file by 4×.** 🔴 **Not an LMS**: no enrolment, gradebook or SIS integration. Pair it with Kolibri or OpenOlat for the institutional layer. |
| **Tutoring platform — permissive** | [open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | 🟢 **New row `p493`** (restored). The permissive answer where ChatTutor (AGPL-3.0) was the only option. 194 forks against 114★ — deployment, not stargazing. |
| **Academic integrity** | [Dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | 🟢 **New row `p493`** (restored). Source-code plagiarism detection; **3,865 commits**, Ghent University. The layer this file previously left empty — and the one every client asks about the moment a tutor can write code. |
| **Teacher workflow (skills)** | [k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** | 595 | 🟢 **New row `p493`** (restored). Four K-12 teacher skills **plus eval rubrics**, co-developed with Learning Commons; consortium-side twin at [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) (Apache-2.0, 40★). 🔵 A skill pack has no runtime — nothing to host, no data residency posture. |
| **Tutoring evaluation** | [pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 13 | 🟢 **New row `p493`** (restored). 1,143 teacher-exam questions (920 CDPK / 223 SEND), 100+ models, `arXiv:2506.18710`. 🔴 13★ — a corpus and baseline, not a dependency. |
| **Low-bandwidth delivery** | [rumi-platform](https://github.com/Orenda-Project/rumi-platform) | **Apache-2.0** | 18 | 🟢 **New row `p493`** (restored). **WhatsApp**-delivered learning, 15 languages, 847 commits (Pakistan / Taleemabad). No app, no browser — the delivery surface below even Kolibri's. |
| **Lesson planning** | [Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) | **MIT** | 9 | 🟢 **New row `p493`** (restored). MSR India, VELLM, with Sikshana Foundation. **Every artefact is routed to a teacher for review before classroom use** — a shipped implementation of the human-oversight gate. |

## The decision that actually matters on an engagement

**Does the client need to host a modified platform for third parties?**

- **No** (internal use, or they run it themselves) → any row above works. GPL/AGPL obligations
  are satisfied by their own deployment. Take Moodle or Open edX for installed base.
- **Yes, and it must stay closed** → **only three rows survive**: OpenOlat (Apache-2.0),
  Kolibri (MIT), Oppia (Apache-2.0), plus `mentingo` (MIT) as a greenfield base. Everything
  else forces source release to users over a network (AGPL) or to recipients (GPL).
  🔵 **`p491` added two platforms and this shortlist did not change** — both newcomers are
  copyleft. Three passes of platform discovery have not produced a fourth permissive LMS, which is
  itself the answer to "shouldn't we keep looking?".

**The AGPL trap specifically:** Open edX, Canvas, Frappe LMS, Tutor, Anki **and LearnHouse** are
AGPL-3.0.
A Globant-hosted SaaS built on any of them owes source to its users. This is routinely missed
because listicles print "open source" without the family — and in `frappe/lms`'s case print
"MIT" outright, which this pass refuted from bytes.

## AI-on-top integration surfaces that already exist

Don't build the connector — these are real:

| Surface | Repo | License | Reaches |
|---|---|---|---|
| Canvas tool API for agents | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | Canvas LMS; ~102 tools + 8 agent skills |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | MCQs, lesson plans, flashcards |
| Source → study package | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | PDF/video/web/audio → quizzes + SRS |
| Mastery modelling | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | Bayesian Knowledge Tracing |
| Moodle plugin API | — | GPL-3.0 (plugin inherits) | 2,000+ plugin ecosystem; note the plugin is a derivative |
| Eval runtime for tutors | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | MIT | 14,300★. Generic LLM eval; **the only permissive base for a tutoring-quality harness** — the education-specific benchmarks are unlicensed (see [`agents/top.md`](../agents/top.md)) |

## Declared gaps

- **No permissive SIS and no permissive assessment engine exist** (see
  [`repos/foundations.md`](../repos/foundations.md)). For a closed SIS or exam product, there is
  no open base — it is a build.
- **No MCP server for Moodle or Open edX reached a usable star floor.** Canvas is the only
  incumbent LMS with a real, maintained agent tool surface. For Moodle/Open edX, the connector
  is engagement work.
- ~~**`Fedena` (claimed Apache-2.0 SIS) could not be resolved.**~~ 🟢 **Resolved `p491`:** two real
  repos ([`projectfedena/fedena`](https://github.com/projectfedena/fedena) 547★,
  [`foradian/fedena`](https://github.com/foradian/fedena) 4★), **neither carrying a license file**.
  The Apache-2.0 claim comes from a README sentence, not a grant. Still not carried as a row — now
  for an evidenced reason rather than an unresolved one.
- **No maintenance signal is available for any row in this file.** Stars and license are readable;
  the latest-commit date is not, on any channel open to this session. A row's presence here means
  *it exists and its license is known*, **not** *it is actively maintained* — do not let a layer
  table imply currency it cannot support.


## 🆕 `p492` — `2026-10-28` — the virtual-classroom layer gains a permissive option

Evidence: [`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv).

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| **Virtual classroom — permissive** | [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** | 688 | Video conferencing, IM, **whiteboard**, collaborative document editing; media via Kurento. Release `v9.1.0` (a security release), ASF governance. **The only permissively-licensed conferencing platform in this file.** |

🔵 **This does not replace the BigBlueButton row above.** BigBlueButton (LGPL-3.0, 9,300★) is
**13× larger** and stays the default for live classes; LGPL already permits linking. Reach for
OpenMeetings only in the narrow case where the deliverable must **ship modified platform source
inside a proprietary product** — the one case LGPL's linking allowance does not cover. At 688★,
treat it as a **considered fallback**, and verify its Kurento dependency first.

### 🔴 Amendment to the Canvas agent-surface row

The [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) entries above remain correct that
it is MIT and the only maintained agent tool surface on an incumbent LMS. 🔴 **Two things changed
this pass:** its HEAD **drifted** to `830bc2ef8389` (licence byte-identical at both SHAs, so
code-only), and `v1.16.0` publishes **four** security advisories where this KB recorded one —
including **Canvas token handling** (`GHSA-7mj9-4mcg-hvhv`) and a **local code sandbox**
(`GHSA-7pp5-29mw-9jq3`). **Pin `v1.16.0` or later, and treat the institutional Canvas API token —
not the tool scope — as the primary asset to protect.** See
[`compose/patterns.md`](../compose/patterns.md) `P490-1`, amended this pass. 🟡 Its tool count is
self-inconsistent upstream (description 102, README 128) — **do not quote a number to a client.**

### 🟢 The "no maintenance signal" caveat above is now too strong

This file states that "no maintenance signal is available for any row." **Release dates are
readable** via page fetch — `openmeetings v9.1.0`, `canvas-mcp v1.16.0` (Oct 2026). Repos that tag
releases **can** be shown to be live; only untagged ones cannot. Next pass should carry a release
date per row.


## 🆕 `p493` — `2026-10-28` — seven layers gained a permissive option, and none of them is a new discovery

Reads: [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).
Mechanism: [`agents/trending.md`](../agents/trending.md) `p493`.

🔴 **Every row added to the table above was already in this KB** — read, licence-measured, and
recorded as promoted — and then deleted by a full-file rewrite of the shelf files, with no marker
left behind. **This section is a repair, not a find.** Saying so matters: two consecutive passes
have now moved the permissive count, `p492` by discovery (`apache/openmeetings`) and `p493` by
repair, and reading them as one trend would be wrong.

### 🟢 The decision tree in this file changes shape

The question this file says *actually matters* — **"does the client need to host a modified
platform for third parties?"** — was decisive because an AGPL platform at the bottom of the stack
contaminated the whole engagement. That is still true **for the LMS/SIS/assessment core**. It is no
longer true for everything above it.

| layer | before `p493` | after `p493` |
|---|---|---|
| Full LMS | OpenOlat (Apache-2.0) or accept copyleft | **unchanged** — OpenOlat is still the only permissive full LMS |
| SIS | 🔴 no permissive option | 🔴 **unchanged** — none exists |
| Assessment / QTI | 🔴 no permissive option (TAO, GPL-2.0) | 🔴 **unchanged** — none exists |
| Interactive classroom | *not offered* | 🟢 **OpenMAIC (MIT, 41,700★)** |
| Tutoring platform | ChatTutor (AGPL-3.0) | 🟢 **open-tutor-ai-CE (BSD-3-Clause)** |
| Academic integrity | *not offered* | 🟢 **Dolos (MIT)** |
| Teacher workflow | *not offered* | 🟢 **k12-teacher-skills (Apache-2.0)** |
| Evaluation | 🔴 "nothing licensed exists" | 🟢 **pedagogy-benchmark (MIT)** |
| Virtual classroom | BigBlueButton (LGPL-3.0) | OpenMeetings (Apache-2.0), `p492` |
| Low-bandwidth delivery | Kolibri (MIT, offline) | 🟢 **+ rumi-platform (Apache-2.0, WhatsApp)** |

🟢 **Practical consequence:** a client who cannot accept copyleft is no longer pushed onto
OpenOlat-or-nothing for the whole stack. Build the AI layers permissively — courseware, tutoring,
integrity, teacher workflow, evaluation — and confine the copyleft decision to the LMS/SIS/assessment
core, where it is genuinely unavoidable. 🔴 **And confine it honestly:** if the engagement needs a
student information system or a QTI exam engine, there is still no permissive option and the
AGPL/GPL conversation cannot be avoided. That is a four-pass consistent result.

Wired end-to-end as [`compose/patterns.md`](../compose/patterns.md) `P493-1`.

## 🆕 `p494` — `2026-10-28` — no layer changes; one grant re-pinned, one jurisdiction restored

Reads: [`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).
Narrative: [`../agents/trending.md`](../agents/trending.md) `p494`.

🟢 **The layer table above is unchanged.** `p493`'s seven newly-permissive layers hold, and no
platform read this pass showed drift.

🟢 **The tutoring-platform layer's copyleft option is now grant-pinned by bytes, not by tag.**
[`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) re-read first-hand at
`7d9e9052bc5a`: **AGPL-3.0**, `LICENSE`, **34 522 B**, `sha1 3cd688cb1bd7` — **byte-identical** to
this KB's earlier read. 🔴 **The consequence is unchanged and now defensible from the payload rather
than from a sidebar label: AGPL reaches across the network, so hosting ChatTutor for a client
triggers source obligations on the hosted service.** 🟢 The permissive answer in this layer remains
[`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3-Clause, 1 531 B,
`196c547291da`) — **with its third condition honoured**: attribution in `NOTICE`, yes; *"built on
Open-TutorAI"* in client-facing marketing, **no**, absent written permission.

### 🔵 A deployment-posture input this file had lost

An APAC regulatory posture relevant to **how** these platforms get deployed was deleted from
[`../intel/market.md`](../intel/market.md) by `p315`'s rewrite and is restored this pass: **Singapore's
Model AI Governance Framework, its generative-AI framework, its Model AI Governance Framework for
Agentic AI (IMDA, 22 Jan 2026) and AI Verify are all voluntary — but vendors selling into government
and banks are expected to point to them**, which makes a voluntary instrument a **procurement gate**.

🟢 **Why it matters when picking a platform rather than a model.** The agentic framework asks how much
**autonomy** an agent is granted, how its actions are **bounded and logged**, where the **human** sits,
and who is **accountable when several agents interact**. 🔵 **Those are platform properties, not model
properties** — a platform that cannot emit a per-action log, or that has no place to put a teacher
review step, cannot be made conformant by swapping the model underneath it.
[`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)'s shipped design — every
generated artefact routed to a teacher before classroom use — remains the shape to copy at this layer.
Full build guidance: `P494-1` in [`../compose/patterns.md`](../compose/patterns.md).


## 🆕 `p495` — `2026-10-28` — the Odoo answer is byte-verified, and the Canvas surface gets a version floor

### 🟢 `OpenEduCat` — the Education-ERP row, read from the payload

This file's **Education ERP** row has carried `OpenEduCat` as LGPL-3.0 on a shelf tag. 🟢 **Read
first-hand this pass and confirmed**: LGPL-3.0, **`8 241 B`**, `sha1 2979df12244d`, at pin
`46a5d7d40082` (stable). 🔵 It remains *"the literal Odoo answer"* — admissions, fees, library,
hostel, timetable, on Odoo — and it remains the right base for a LATAM administration engagement,
where [`../intel/market.md`](../intel/market.md) `p495` now places the numeric opening (UNESCO
IESALC: administration adoption **34.1%**, against teaching & learning at **73.5%**).

🔴 **One defect found in the grant itself, and it changes the paperwork on an engagement.** Line 1
of its `LICENSE` reads *"For copyright information, please see the COPYRIGHT file"* — and
`COPYRIGHT` returns **`404`**. LGPL-3.0 requires preserving copyright notices; **the repository
points that obligation at a file that does not exist.** 🔵 **Do:** ship the `LICENSE` verbatim, cite
the pin as provenance, and request the `COPYRIGHT` file from the maintainers in writing. **Do not**
reconstruct attribution from commit metadata.

### 🔴 Amendment to the Canvas agent-surface row — a **version floor**, not a preference

The Canvas integration surface in this file is [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp).
🔴 **It now carries a hard minimum**, read first-hand this pass:

| constraint | value | why |
|---|---|---|
| minimum version | 🔴 **`v1.16.0`** (= `b3f06c76e435`) | **all four** published advisories are patched there; **two are High** (`GHSA-7pp5-29mw-9jq3`, CVSS **7.8**, sandbox escape; `GHSA-hmr8-mvr2-mvw5`, prompt injection → data disclosure / **grade change**) |
| pin style | 🔴 **the release tag, never branch HEAD** | HEAD (`47394125364b`) is **unreleased code above the newest tag**, and no `v1.17.0` exists |
| runtime | 🔴 **Node.js ≥ 22.18** | the `1.16.0` sandbox fix works via **Node's permission model**; on an older Node the advisory is **not actually closed** while the version string says it is |
| tool posture | 🔴 **disable `execute_typescript`** | the advisory states as **unfixed**: egress blocking is best-effort and **executed code can still reach the caller's Canvas token** |
| credential | 🔴 **scoped, short-lived Canvas token** | `GHSA-7mj9-4mcg-hvhv` (Moderate): the bearer token is sent to a URL **chosen by the file-storage host** |

🔵 **Read the shape of this, not just the rows.** This is the **only maintained agent surface on an
incumbent LMS** this KB has found, so it stays the recommended integration point — but the honest
posture is *"deploy it pinned, hardened and with the code-execution tool off,"* not *"deploy it."*
The full recipe is [`../compose/patterns.md`](../compose/patterns.md) **`P495-1`**.

### 🔴 Declared gap — the vertical-platform query returns no permissive platform, third pass running

🔴 The brief's `open source platform education ERP CRM MIT Apache` query returned **no MIT- or
Apache-licensed education platform** again: `OpenEduCat` (LGPL-3.0), `Apache OFBiz` (Apache-2.0 but
not education), generic MIT CRMs (not education), `CK-ERP` (2010, dead). 🟢 **Structural conclusion,
now stable across three independent passes: in this layer the mature systems are copyleft, and the
engagement question is which obligation the client can carry** — which is what this file's decision
tree already asks. Registered as `NO-PERMISSIVE-PLATFORM` in the `p495` claim register so a later
rewrite cannot quietly drop it.



## 🆕 `p496` — `2026-10-28` — the special-education layer has **no platform**, and that is the finding

🔴 **No layer in this file changes, and the platform query returned one vendor for the third pass
running** (nine `openeducat.org` pages in eight languages, no second platform). The LGPL-3.0 reading
`p495` byte-verified stands.

🆕 **What is new is a layer this file never had: special education.** Discovery this pass produced
eight addresses in it (see [`../agents/top.md`](../agents/top.md) `p496`), and the shape of what
exists is the useful part for an engagement:

| layer | what exists | permissive answer |
|---|---|---|
| IEP / §504 **knowledge packs** (law, sources, checklists) | three, all MIT | 🟢 [`jscott5811/IEP-and-Section-504-Plans-Skill`](https://github.com/jscott5811/IEP-and-Section-504-Plans-Skill) **(US federal)**, [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) (California), [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) (Arizona K-8) |
| IEP **rendering / plain-language output** | one, MIT, **deterministic** | 🟢 [`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) |
| IEP **drafting pipeline** (multi-agent, retrieval, compliance gate) | one, **no grant** | 🔴 **none** — `SudhanvaJ-bit/project-samarth` is a read-only reference design |
| special-education **platform / system of record** | 🔴 **nothing**, open or permissive | 🔴 **none** |

🔴 **So the honest brief for a special-education engagement is: there is no platform to customise.**
Every MIT asset in this layer is a *knowledge pack* or a *renderer*. The system of record stays
whatever the district already runs, and Globant's build sits beside it. 🔵 **That is the opposite of
this file's usual answer** — for LMS, ERP and virtual-classroom work the advice is "customise a real
platform". Here there is no platform, and saying so early is worth more than a shortlist.

### 🟢 A deployment posture this file has never been able to offer: **zero-AI, zero-server**

[`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) — **MIT**, 1 080 B,
`sha1 fb30401f6782` at `264786ddb518` — converts an IEP PDF into one-page plain-language sheets per
adult (classroom teacher, paraprofessional, substitute, family), plus optional accommodation and
goal-data trackers. 🟢 **It runs entirely in the browser: no server, no AI service, rules only.**
Prints in English or Spanish.

🔵 **Why this matters more than its 0★ and 1 commit suggest.** The hardest objection in a
special-education engagement is not accuracy, it is **data egress** — IEPs are among the most
sensitive records a school holds. A tool that never transmits the document answers that objection
*architecturally* rather than contractually. 🟢 **It is also the cleanest instance of `T9`
(offline-first as a differentiator) this KB holds**, because it is offline by construction rather
than by configuration.

🔴 **Three limits to state before anyone proposes it:**
- **Mixed licensing.** Project code MIT; bundled `pdf.js` **Apache-2.0**; Nunito font **SIL OFL
  1.1**. 🔵 The font licence is the one a compliance review will stop on — OFL restricts
  *renaming* the font, which matters if the output is rebranded for a district.
- **Spanish is partial, and upstream says so.** The classifier works in English only; Spanish IEPs
  are read by rules, and translation uses a built-in phrase list of **~150 common accommodations and
  services**, so many items still need a human translator. 🔴 **Do not sell it as bilingual.**
- **1 commit, 0★, no release tags.** No maintenance signal exists. Treat it as a **seed to fork**,
  never as a dependency to track.

### 🔴 Amendment to this file's Canvas row — unchanged, and restated because it is a floor

No new advisory data this pass. The `canvas-mcp` version floor from `p495` stands in full:
**`v1.16.0` = `b3f06c76e435`**, which patches all four advisories including two High (one at CVSS
**7.8**), **requires Node.js ≥ 22.18** for the sandbox fix to be real, and leaves the caller's Canvas
token reachable by executed code as a declared-unfixed residual. 🟢 HEAD stable for a second
consecutive pass (`47394125364b`), so the pin is a security decision, not a drift workaround.

### 🔴 Declared gaps

- 🔴 **No permissive education ERP/SIS platform** — the mandated platform query has now returned
  none for **three** consecutive passes. `openeducat_erp` (**LGPL-3.0**) by elimination.
- 🔴 **No open special-education system of record**, permissive or copyleft. New gap, declared this
  pass, and it is a supply fact rather than a search artefact: the function-shaped queries that
  found eight application-layer addresses found **zero** platforms.
- 🔵 **No AI-on-top integration surface exists for any special-education system.** The Canvas/Moodle
  surfaces this file catalogues have no counterpart here — there is nothing to attach an agent to.

## 🆕 `p497` — `2026-10-28` — the **admissions / grading / proctoring** layer, which is where the regulator looks and where this file had nothing

Evidence: [`licence-and-stars.2026-10-28-p497.tsv`](../evidence/licence-and-stars.2026-10-28-p497.tsv).
Narrative: [`agents/trending.md`](../agents/trending.md) `p497`. Recipe:
[`compose/patterns.md`](../compose/patterns.md) `P497-1`.

### 🔴 The layer this file was missing, and why it is the expensive one

This file picks a platform **by layer** — LMS, SIS, ERP, assessment, conferencing. The layers it
covers are the ones that *hold* data. 🔴 **The four functions the EU AI Act singles out as high-risk
are not layers in this table at all** — they are *decisions* made on top of it:

**EU AI Act Annex III point 3** designates education AI as high-risk for **admissions**, **grading**,
**placement**, and **exam proctoring**. 🔵 Secondary citation — `eur-lex.europa.eu` is `ENOTFOUND`
from this session (`p495`), so the instrument text has not been read here.

🟢 **This is the commercially useful cut of this file**, because those four decisions are exactly
where a client needs a conformance story and exactly where the open-source supply is thinnest.

| Annex III function | best open-source starting point | licence | state of supply |
|---|---|---|---|
| **Admissions** | [`ASUCICREPO/Admissions-AI-Agent`](https://github.com/ASUCICREPO/Admissions-AI-Agent) | **MIT** (1 123 B, `sha1 8a0aae668604`) | 🔴 **One asset, 5★, found `p497`.** Arizona State University's AI Cloud Innovation Centre. Reference architecture only — AWS Bedrock AgentCore, so the MIT grant covers orchestration, not a portable runtime |
| **Grading** | [`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) (MIT, `refs/heads/v2`), [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) (MIT, plagiarism), [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) (GPL, assessment platform) | mixed | 🟡 Thin but real. `oh-my-paper` is 1★; `dolos` at 3,865 commits is the maintained one but detects plagiarism rather than grades |
| **Placement** | — | — | 🔴 **Nothing.** No open-source placement/streaming system found in any pass |
| **Exam proctoring** | [`SafeExamBrowser/seb-win-refactoring`](https://github.com/SafeExamBrowser/seb-win-refactoring) (357★), [`vardanagarwal/Proctoring-AI`](https://github.com/vardanagarwal/Proctoring-AI) (633★) | 🔴 **neither permissive** | 🔴 `topic:proctoring` holds **145** repositories and produced **no permissive asset** this pass. For a designated high-risk function |

### 🟢 What to tell a client, by layer

- **Admissions.** There is one MIT reference design and it is a university's, not a vendor's. 🟢 Read
  the adviser-handoff boundary in it — the design decision that keeps a human in the loop on the
  decision itself is the one that carries the Annex III story. Re-implement on your own runtime
  rather than inheriting Bedrock AgentCore.
- **Grading.** 🔴 **Never let the model do the arithmetic** — that is `P492-1` and it stands. Compose
  `oh-my-paper`'s marking flow or build fresh, with scoring in deterministic code.
- **Placement.** 🔴 Greenfield. Price it as a build.
- **Proctoring.** 🔴 The honest answer is that the permissive supply does not exist. Safe Exam
  Browser is the credible institutional system and it is copyleft; plan on deploying it **alongside**
  rather than embedding it, or accept the licence.

### 🔵 The ERP question, settled

Asked explicitly this pass: **no permissively-licensed education ERP exists.** ERPNext GPL-3.0,
Dolibarr GPL-3.0, Odoo Community LGPL-3.0, OpenEduCat LGPL-3.0; Apache OFBiz is Apache-2.0 but ships
no education domain model. 🟢 For a closed derivative at the ERP layer: **build the domain model, or
take LGPL-3.0 and keep the Odoo modules separable.** Full reasoning:
[`repos/foundations.md`](../repos/foundations.md) `p497`.

### 🔴 Branch refs for rows in this file

[`rosariosis`](https://github.com/francoisjacquet/rosariosis)'s default ref is
**`refs/heads/mobile`** and [`openeducat_erp`](https://github.com/openeducat/openeducat_erp)'s is
**`refs/heads/19.0`** — both rows in this KB's platform tables. A deployment script that clones
without resolving the symref gets the wrong tree or no tree. Five variants now recorded:
[`branch-ref-census.2026-10-28-p497.tsv`](../evidence/branch-ref-census.2026-10-28-p497.tsv).

---

## 🆕 `p498` — `2026-10-28` — a platform this file calls unusable is **GPL-2.0**, and the one permissive platform turns out to be a **host**

### 🔴 Correction — `formalms` is licensed, and this file said otherwise

🔵 This file has carried [`formalms/formalms`](https://github.com/formalms/formalms) as a
vertical platform with no usable grant, and `Gap 488-L` asked `p498` to mark it unusable. 🟢 **The
opposite edit is the correct one.**

| | |
|---|---|
| grant | 🟢 **GNU GPL version 2, June 1991** |
| at | `html/license.txt` — 18 346 B · blob `e823963cd437` |
| and at | `html/lib/System/license/license_english.txt` — 15 146 B · blob `b6e1c33e0499`, **plus Italian, Spanish, French, German, Portuguese, Croatian, Bosnian and Tamil**, with an `index.html` to serve them |
| at the repository root | 🔴 **nothing** — which is every previous probe's entire answer |
| ref / HEAD / activity | `master` · `446a77a9b9cb` · last commit **2026-07-17** (🟡 three months stale) |
| 🔴 *or-later* election | **none found** — 0 PHP files in the tree cite the GPL. **GPL-2.0-only.** |

🔴 **Shelf verdict, corrected: `formalms` is a GPL-2.0-only LMS, not an ungranted one.** 🟡 It is
still not a recommendation — three months without a commit, and `Gap 489-L` already warned its 0.70
fork-per-star cannot tell a live deployment from historical forks. **But "unusable, no licence" was
wrong**, and a studio that refused it on this file's say-so refused it for a reason that does not
exist.

🔵 **The transferable lesson for this layer specifically:** an institutional platform that serves its
own licence to end users through its web UI has no reason to keep a copy at the repository root.
**A root-only licence probe is systematically blind to exactly the platforms this file is about.**

### 🔴 The GPL-2.0-only boundary, now measured on two platform rows

| platform | grant | *or-later* elected? | combines with GPL-3.0 code? |
|---|---|---|---|
| 🇧🇷 [`portabilis/i-educar`](https://github.com/portabilis/i-educar) — municipal SIS, ref `2.12`, HEAD `435649b0474f`, last commit **2026-10-22** 🟢 live | GPL-2.0 (root `LICENSE`) | 🔴 **no** — 0 of its PHP files | 🔴 **no** |
| 🇮🇹 [`formalms/formalms`](https://github.com/formalms/formalms) | GPL-2.0 (`html/license.txt`) | 🔴 **no** | 🔴 **no** |

🔴 **Say this in week one of a Brazilian municipal engagement.** `i-educar` is live and maintained,
and it is **GPL-2.0-only**. It cannot take GPL-3.0 code, and the GPL-3.0 platforms on this
file — [`moodle`](https://github.com/moodle/moodle), [`chamilo`](https://github.com/chamilo/chamilo-lms),
[`ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) — cannot take its. The two copyleft families on
this shelf are **not interoperable**, and nothing on this file said so before.

🟡 Read from PHP source notices only; neither tree was read exhaustively for a prose election
(`Gap 498-C`).

### 🟢 `learningequality/kolibri` is an extension host, not a content sink

🔵 This file lists Kolibri as the offline-first delivery platform and the **only permissive**
institutional option. `p498` read its code at HEAD `08e3ecace444` (ref `develop`, last commit
2026-10-27) and the integration surface is larger than this file has claimed.

| surface | what is actually there |
|---|---|
| 🟢 **plugin registry** | `kolibri/plugins/` — **21 in-tree plugins**. A plugin is a Django app with a `kolibri_plugin` module; enabling it adds its apps to `INSTALLED_APPS`. |
| 🟢 **own API** | `KolibriPluginBase` exposes `url_module` and `api_url_module` — a plugin mounts **its own URLs and its own DRF API**. **21 `api_urls.py`** across the tree. |
| 🟢 **runtime kill switch** | plugins enable/disable **from the CLI or a UI**, and via `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`. **No rebuild to turn the AI off.** |
| 🔴 **hook singletons** | `KolibriHook` / `KolibriHookMeta(SingletonMeta)` / `HookSingleInstanceError` — **one registration per hook.** Two vendors shipping plugins into one deployment will collide. |
| 🟢 **third-party precedent** | four out-of-tree plugins ship in the repo as `python_packages/`: `kolibri-oidc-provider-plugin`, `kolibri-sentry-plugin`, `kolibri-sync-extras-plugin`, `kolibri-context-translation-plugin`. **OIDC provider as a plugin** — the extension surface reaches authentication. |
| 🔴 **native AI** | **none.** One keyword hit across 3 071 Python/Vue/JS files and it is a false positive (*"transformers"* in a Django `from_db_value` comment, `kolibri/core/content/viewsets/import_metadata.py:152`). |

🟢 **The "no native AI surface" verdict on this row is now a code read at a 2026-10-27 commit**, not
the Apr-2026 secondary comparison `Gap 488-N` objected to. For this row, `Gap 488-N` is closed.

🔵 **The consequence for this file's decision table:** on the permissive path you are not limited to
pre-baking content and importing it. You can ship an **in-platform AI surface** as a plugin, with
the institution holding the off switch, and without forking core. That is a materially better offer
than "generate centrally, import offline", and it is the only permissive route to it on this file.

### 🟡 The institutional layer's permissive count does not move

🔵 Three passes have now ended with the same answer and this one makes four:
[`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) (Apache-2.0) remains the only permissive full LMS,
`kolibri` (MIT) the only permissive offline platform, and 🔴 **there is still no permissive SIS and
no permissive QTI exam engine.** `formalms`'s re-grading adds a GPL-2.0 LMS to the copyleft column;
it does not add a permissive option. The copyleft conversation on SIS and exams remains unavoidable.

---

## 🆕 `p499` — `2026-10-28` — the "Odoo for education" answer gains a permissive integration layer

**Pass `p499` — reads of 2026-10-28.** This section **extends** the file. Licences read from bytes
at pinned SHAs and graded on the operative-span instrument
([`evidence/canonical/MANIFEST.tsv`](../evidence/canonical/MANIFEST.tsv)); full reads in
[`new-rows-licence-bytes.2026-10-28-p499.tsv`](../evidence/new-rows-licence-bytes.2026-10-28-p499.tsv).

### 🟢 The layer this table was missing

Every row in "Pick by layer" above is a **system of record** — it holds the students, courses and
grades. None of them is the thing you actually write. 🟢 **The integration layer is now on the
shelf, and it is permissive at both standards:**

| Layer | Platform | License | ★ | Why this one |
|---|---|---|---|---|
| 🟢 **LTI tool framework** | [Tsugi](https://github.com/tsugiproject/tsugi) | **Apache-2.0** | 377 | 🟢 **The way into an LMS you do not own.** LTI + IMS Global + Common Cartridge. Works against Moodle, Canvas, Open edX, Blackboard, D2L. **Apache-2.0, so the tool you build stays closed even against an AGPL host.** |
| 🟢 **SCORM / CMI runtime** | [scorm-again](https://github.com/jcputney/scorm-again) | **MIT** | 360 | 🟢 SCORM 1.2 + 2004 + CMI, cross-frame. The courseware-packaging boundary, MIT. Active 2026-10-26. |
| 🟢 **LMS — permissive, new** | [TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** | 52 | 🟢 Second permissive full LMS after OpenOlat — multi-tenant, Django + React. 🔴 **Three weeks old; watch row, not a deployment choice** (`Gap 499-H`). |
| **Skills / credentials** | [iblai/lms](https://github.com/iblai/lms) | **MIT** | 208 | Competency tracking and digital credentials — the layer every workforce-reskilling engagement needs and that had no permissive option here. |
| **Course authoring / microsites** | [HAXcms](https://github.com/haxtheweb/haxcms-php) | **Apache-2.0** | 130 | Course microsite CMS, PHP. Pushed 2026-10-28. |
| **Teaching lab — code** | [pytogether](https://github.com/SJRiz/pytogether) | **MIT** | 261 | Browser-based collaborative Python IDE, real-time. Drop-in for a programming classroom. |
| **Widgets / games over LTI** | [Materia](https://github.com/ucfopen/Materia) | 🔴 AGPL-3.0 | 52 | Embeddable widgets and games. Same UCF stable as UDOIT/Obojobo. 🔴 Hosted derivative must share. |
| **Offline-first services** | [Lokal](https://github.com/Wakoma/Lokal) | **MIT** | 53 | Offline content + local network services. Pairs with Kolibri for low-connectivity deployments. |
| **Spaced repetition — permissive** | [Mnemo](https://github.com/onemnemo/mnemo) | **Apache-2.0** | 122 | 🟢 See the correction below. |

### 🟢 A standing recommendation in this file is now obsolete

The table above carries **Anki (AGPL-3.0)** with the note *"Reference SRS scheduler. Use as the
algorithm reference even where the code can't ship."* 🟢 **That constraint is lifted.** There are
now **two permissive spaced-repetition implementations** read from bytes:
[`onemnemo/mnemo`](https://github.com/onemnemo/mnemo) (**Apache-2.0**, operative IDENTICAL) and
[`kirill-markin/flashcards-open-source-app`](https://github.com/kirill-markin/flashcards-open-source-app)
(**MIT**, operative IDENTICAL, **FSRS** scheduling). 🔵 Anki stays on the shelf as the reference
implementation, but **"the code can't ship" is no longer the end of the sentence** — for SRS
specifically, permissive code now exists.

### 🔵 `formalms` re-graded a second time, and the grade holds

`p498` re-graded [`formalms/formalms`](https://github.com/formalms/formalms) from "no readable
grant" to **GPL-2.0** after finding the payload at `html/license.txt` rather than the repository
root. 🟢 `p499` graded **both** of its GPL-2.0 payloads on the operative instrument (`Gap 498-D`):
**2 489 operative words each, identical diff signatures**, differing from canonical only by the
**1991-vintage FSF transcription** ("Library" for "Lesser", "Franklin St" for "Franklin Street").
🟢 **GPL-2.0 confirmed. Neither payload is truncated or altered** — the 3 200-byte spread between
them is the omitted *How to Apply These Terms* appendix. 🔴 Its staleness is unchanged and still
disqualifying for a new engagement: last commit **2026-07-17** (`Gap 498-E`).

### 🔴 Refused this pass, with reasons

| Platform | ★ | Why refused |
|---|---|---|
| [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) | 71 | 🔴 **No root grant at any of six probed paths.** School-management software with unified communications — would otherwise fit the SIS layer. |
| [`codeforlife-education/codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal) | 54 | 🔴 **121-byte `LICENSE.md` containing only a link.** UK Code for Life schools platform. |
| [`codeforlife-education/rapid-router`](https://github.com/codeforlife-education/rapid-router) | 60 | 🔴 Same 121-byte pointer. Blockly game for ages 5–11. |
| [`studentinsights/studentinsights`](https://github.com/studentinsights/studentinsights) | 135 | 🟡 MIT and clean, but **last push 2024-08-27** — over two years stale. Code for America school-data platform; recorded, not recommended. |

---

## 🆕 `p500` — `2026-10-28` — the permissive LMS row is re-verified, and the student-success layer turns out to be closed

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Reads:
[`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv).

### 🟢 `OpenOlat` — the "only permissive full LMS" claim survives a byte re-read

This file's single most consequential row is [OpenOlat](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0, 448★), because it is the one row that lets an engagement ship a **closed hosted
derivative** of a university-grade LMS. Re-read from bytes at pinned SHA `cd91a957ea2e`
(**10 982 B**): 🟢 **Apache-2.0 confirmed, operative body materially unaltered.** The +99-word
residual against the apache.org canonical form is two appended attribution paragraphs (OLAT
Zentrum, University of Zurich; frentix GmbH) and adds **no condition**.

An independent 2026 vendor round-up also lists OpenOlat as Apache-2.0 — 🟢 **that claim is
correct**, unlike the same genre's **Fedena** claim, which `p491` refuted from bytes. Vendor
licence columns are right about half the time here; the byte read is what decides.

### 🔴 The student-success / advising layer has no permissive option

This is a **new gap in this file's layer map**, and a commercially important one. Student success,
advising and retention is one of the most frequently bought education-AI capabilities. The leading
open-ish implementation:

| Layer | Platform | Licence | ★ | Verdict |
|---|---|---|---|---|
| 🔴 **Student success / advising** | [advisingapp](https://github.com/canyongbs/advisingapp) (Canyon GBS) | 🔴 **Elastic License 2.0**, 3 860 B `4449f765bdd0` | 340 | **Source-available, not open source.** Forbids providing the software to third parties as a hosted service — i.e. it forbids the delivery model an engagement would use. |

🔴 **Consequence for an engagement:** there is **no permissive advising/student-success platform**
to customise. The buildable route is an agent layer over the SIS/LMS you already have — see
[`compose/patterns.md`](../compose/patterns.md) `P500-1` — not a fork of this row. GitHub reports
this repository as `NOASSERTION`, so the restriction is invisible from the API.

### 🟢 Registerable at the content/assessment layer

| Layer | Platform | Licence | ★ | Why this one |
|---|---|---|---|---|
| 🟢 **Live classroom response / quizzing** | [realtime-quiz-framework](https://github.com/ably-labs/realtime-quiz-framework) | **Apache-2.0** | 77 | Permissive base for synchronous whole-class response: fan-out, mid-round joins, scoring. Pair with an LMS for roster and gradebook. |
| 🟡 **AI output QA against rubrics** | [learning-commons-org/evaluators](https://github.com/learning-commons-org/evaluators) | 🟢 code **MIT** / 🔴 corpora **CC BY-NC-SA 4.0** | 87 | Rubric-based QA for generated instructional content (Text Complexity, Feedback, Standards Alignment, Durable Skills). Deploy the **code**; the shipped annotated corpora are **non-commercial** (`Gap 500-E`). |


## 🆕 `p501` — `2026-10-28` — **🔴 THE 6-PATH LICENCE PROBE THIS FILE REASONS WITH PRODUCES FALSE "NO GRANT" VERDICTS, AND THE PROOF IS THE BIGGEST PLATFORM IN THE ERP LAYER: [`frappe/erpnext`](https://github.com/frappe/erpnext) reads `NONE-OF-6-PATHS` and ships **GPL-3.0 at `license.txt`** — lowercase name, lowercase extension, a combination the probe set omits. 🟢 The alumni / advancement CRM layer gains its first row (**CiviCRM, AGPL-3.0, read from bytes**). 🔴 A dedicated query for an **MIT or Apache education ERP** returns none, and the one Apache-2.0 candidate named cannot be resolved to a repository, so it is REFUSED rather than recorded. 🔴 And a published ERPNext version figure is stale by twenty minor releases.**

Reads: [`wide-probe.2026-10-28-p501.tsv`](../evidence/wide-probe.2026-10-28-p501.tsv),
[`licence-bytes-verticals.2026-10-28-p501.tsv`](../evidence/licence-bytes-verticals.2026-10-28-p501.tsv).

### 🔴 The probe, first — because it invalidates verdicts already in this file

| repo | 6-path verdict | 22-path verdict |
|---|---|---|
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 `NONE-OF-6-PATHS` | 🟢 **GPL-3.0**, `license.txt`, **35 149 B**, blob `f288702d2fa1`, at `9afbfa0a67d2` |
| [`0xff-r4bbit/watchmetype`](https://github.com/0xff-r4bbit/watchmetype) | `NONE` | 🔴 **`NONE` confirmed** across 22 forms |
| [`choudaryhussainali/MCQ_Grading_Bot`](https://github.com/choudaryhussainali/MCQ_Grading_Bot) | `NONE` | 🔴 **`NONE` confirmed** across 22 forms |

The missing combination is **`license.txt`** — this base probed `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING`, `LICENCE` and bare `license`, i.e. it varied *case* and *extension*
**separately but never together**.

🔴 **This file carries at least one verdict reached with the narrow set:**
[`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) is recorded as
*"**No root grant at any of six probed paths**"* and placed in the unusable tier on that basis.
🔵 **That verdict is now unsafe** — not refuted, unsafe. 🔵 Probe width has also varied: an earlier
pass on [`repos/trending.md`](../repos/trending.md) records a row probed at **ten** paths
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license`, `COPYING`, each on `main` **and** `master`) —
🔴 **and `license.txt` is in neither the six-path nor the ten-path set.** A 22-path re-probe of every
`NONE` row is `Gap 501-F`, and until it runs, *"no grant"* on this base means *"no grant at whichever
width that pass happened to use"*, which no file records. 🔵 **The rule:** a negative result from a probe is a statement about the probe's coverage
first.

### 🟢 The alumni / advancement CRM layer — first row

| platform | repo | licence (read at SHA) | layer |
|---|---|---|---|
| **CiviCRM** | [`civicrm/civicrm-core`](https://github.com/civicrm/civicrm-core) | 🔴 **AGPL-3.0**, 34 524 B, blob `1489b7244859`, at `8c7822486842` | constituent / alumni / donor CRM — **the layer above the SIS**, where advancement, alumni events and donor campaigns live |

🔵 **Why it belongs in an education KB:** the layer it occupies is the one a university actually buys
after the LMS and SIS are settled, and this file had **nothing** in it. 🔴 **AGPL-3.0 is the hardest
constraint in this file.** It reaches across the network: hosting a modified CiviCRM for a client
triggers source obligations toward that client's users. `T2`'s re-scoping does **not** rescue this
one — a CRM is not reached over LTI, so there is no arm's-length integration boundary to hide
behind. **Customise it for a client who will host it themselves and accept the grant; do not build a
hosted commercial derivative.**

### 🔴 There is no MIT or Apache education ERP, and the one candidate is refused

A dedicated query (`open source platform education ERP CRM SIS MIT Apache 2026`) returned the layer
this file already holds, and **confirmed the licence posture rather than changing it**:

| platform | licence as returned | already on this file |
|---|---|---|
| OpenEduCat | **LGPL-3.0** | 🟢 yes |
| Frappe Education | **GPL-3.0** | 🟢 yes |
| RosarioSIS | **GPL-2.0** | 🟢 yes |
| Gibbon | **GPL-3.0** | 🟢 yes |
| Dolibarr (not education-specific) | **GPL-3.0** | 🟢 yes |
| ERPNext | **GPL-3.0** 🟢 *now read from bytes this pass* | 🟢 yes |
| CiviCRM | **AGPL-3.0** 🟢 *read from bytes this pass* | 🆕 added above |

🔴 **One Apache-2.0 candidate was named and is REFUSED, not recorded.** The search returned a
*"University Management System (UMS), Apache-2.0, Java desktop and client-server university
administration"* — fees, teacher assignment, exam records. 🔴 **No owner/repo slug was given and
none was resolvable**, and this base does not write a row it cannot pin to a SHA. 🔵 Guessing a slug
is how a 404 becomes a KB entity. Registered as `Gap 501-J`: a named platform with a plausible
licence and no resolvable address is a **lead**, not a finding.

🟢 **So the standing answer on this file is confirmed by a query aimed squarely at overturning it:
the education ERP/SIS layer is copyleft, with no permissive option at the platform tier.** The
permissive work is **above** it — the LTI and integration layer `p499` established (`tsugi`
Apache-2.0, `scorm-again` MIT) and the practice-level agents on
[`agents/top.md`](../agents/top.md). 🔵 That is `T20` holding for a third pass.

### 🔴 A version figure in circulation is stale by twenty minor releases

The query returned ERPNext's *"most recent stable release… August 2026 (v16.32.3)"*. 🔴 **Measured
from the repository's own tags this pass: `v16.52.0`, `v16.52.1` — the `v16.52.x` line.** The cited
figure is **twenty minor versions behind**.

🔵 **Consequence for this file's version floors:** `P498-1` and `P499-2` pin Kolibri to a release
after `Gap 498-G`; the same discipline has to apply to every platform row, and the channel to use is
`git ls-remote --tags`, **not** a search result. A search-sourced version number has no shelf life.


## 🆕 `p502` — `2026-10-28` — **the layer that makes an LMS auditable, and nobody sells it**

This shelf has carried the platforms (Moodle, Canvas, Open edX, Chamilo, ILIAS, OpenOLAT, TAO,
OpenEduCat) for ~35 passes. 🔴 **Every one of them is a system of record for *enrolment and content*
and none of them is a system of record for *what an AI did and who reviewed it*.** That second record
is what the EU AI Act's Art. 26, Oklahoma's grading bar and LATAM's 26%-with-a-strategy finding all
require — and it is a separate, standards-defined layer: **xAPI / cmi5 / Caliper**.

🟢 **It is real, permissive, and customisable in exactly the sense this shelf means** — the same way
Odoo is an ERP you build on top of:

| Platform | Licence (bytes at the pinned SHA) | ★ | Mainline | What you bolt onto it |
|---|---|---|---|---|
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** — 11,356 B `58853eb8199b` | **144** | 🟢 **2 d** `6159416` | 🟢 **The Odoo of this layer.** SQL-backed LRS, runs on SQLite for a pilot and Postgres for an institution; put an agent's review-and-approval events in it and the audit trail is a query |
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** — 11,357 B `1128f8f91104` | **334** | 🔴 **502 d** `efa045e` | The US DoD reference LRS. 🔴 **Cite it, do not build on it** |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | **Apache-2.0** — 11,357 B `1128f8f91104` | 59 | 🔴 281 d `806c0ba` | **cmi5** player + test suite — the launch-and-track profile that replaces SCORM. Pairs with this shelf's SCORM rows |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** — 1,045 B `f1083e4aa47d` | 78 | 🔴 419 d `5bc232d` | 🟢 The **acceptance gate**. Run it against whatever you ship and a procurement office has its answer |
| [`openfun/ralph`](https://github.com/openfun/ralph) | MIT *(carried, `p467`)* | 51 | 🟢 16 d `91fef11` | LRS + ingestion CLI, **EMEA** (France Université Numérique) |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** — 1,093 B `14a2c9fcad08` | 17 | 🔴 **708 d** `839fcbb` | The dashboard half. 🟢 **Fork-and-own: MIT, unmaintained, under a dated legal requirement** |

🔵 **Why this belongs on the *verticals* shelf and not only in intel:** the LMS platforms here are
mostly **copyleft** (`T2`'s binding constraint — Moodle GPL-3.0, Canvas and Open edX AGPL-3.0,
Chamilo GPL-3.0). 🟢 **The record layer is the one tier of the education stack that is permissive at
the top of its own star ranking**, so a client deliverable can contain it outright. That inverts the
usual recommendation: don't fork the LMS, integrate with it over LTI and own the record layer.

🔴 **Regional reality, stated as measured:** five of the six rows are North American and the two EMEA
rows are one organisation. **No APAC or LATAM record-layer platform was found** on the channel used
(`Gap 502-E` names the channel and its blind spots — non-English naming and non-GitHub forges).

## 🆕 `p503` — `2026-10-28` — **two platform rows that have been in this base's history for months with no platform row, both read from bytes, and both copyleft — plus the interop claim this file has never checked against its source**

Reads: [`licence-bytes.2026-10-28-p503.tsv`](../evidence/licence-bytes.2026-10-28-p503.tsv),
[`promotion-audit.2026-10-28-p503.tsv`](../evidence/promotion-audit.2026-10-28-p503.tsv).
Narrative: [`agents/trending.md`](../agents/trending.md) `p503`.

### 🟡 Customisable platforms — copyleft, so the grant decides the engagement shape

| Layer | Platform | Licence @ pinned SHA | ★ | What it is | Region basis |
|---|---|---|---|---|---|
| 🟡 **Self-hosted language learning** | [`artcc/freelingo`](https://github.com/artcc/freelingo) | 🔴 **AGPL-3.0**, 34 514 B `269feb00c09a` (blob `128919466b58`, sha256₁₆ `ea94d5765c590b11`), 9 tokens from canonical | 210 | Full platform, not a component: CEFR study plans, an AI tutor, **voice conversations**, flashcards and spaced repetition, with **local or cloud** inference (`ollama` in its own topics), shipped as `docker-compose`. FastAPI + Next.js. | **EMEA** — CEFR is the Council of Europe's framework and the author's site is a Spanish-language personal domain |
| 🟡 **Assessment-item bank** | [`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank) | 🔴 **AGPL-3.0**, 34 523 B `135b78b0f22c` (blob `be3f7b28e564`, sha256₁₆ `0d96a4ff68ad6d4b`), 6 tokens from canonical | 358 | The layer every tutor on these shelves assumes and none supplies: a **question bank** with live LaTeX rendering, LLM parsing/solving and **formula OCR** for ingesting paper items. Localised to Chinese senior-secondary maths. | **APAC** — Chinese-language artefact, 高中 (senior secondary) curriculum scope |

🔴 **Both are AGPL-3.0, and for these two that is a deployment question, not a packaging question.**
A hosted deployment for a client triggers §13: the modified source must be offered to the users who
interact with it over the network. 🟢 **Shelf rule, same as `MoodleNet`/`Openki` above: viable where
the client accepts an AGPL estate or runs it internally; not viable as a component inside a
proprietary product.** For the freelingo shape specifically, the **local-inference** posture
(`ollama`) is what survives a ministry data-residency clause — see `T1`/`T13`.

🔵 **Why neither is in the permissive table:** this file's permissive tier is for platforms Globant
can fork into client IP. 🔴 Neither can be. They are here because the alternative — leaving a
210★ voice-capable tutor platform and the only OCR-capable item bank on these shelves **unrecorded**
— is the failure mode `Gap 502-C` named: *graded and unshelved*.

### 🔴 `OpenEduCat`'s interoperability claim — sourced, and marked as the vendor's own

This file's **Education ERP** row (line 34) and `p501`'s byte-read establish the licence
(**LGPL-3.0**). What has never been recorded is what the platform claims to *interoperate* with,
which is the question a client asks second:

| claim | as published by | status here |
|---|---|---|
| **LTI 1.3** tool support | `openeducat.org` solution pages | 🔴 **vendor-sourced, unverified** — no repository artefact read |
| **OneRoster** + **Ed-Fi** roster sync for SIS integration | `openeducat.org` | 🔴 vendor-sourced, unverified |
| **SCORM / xAPI** content support, Shibboleth SSO | `openeducat.org` | 🔴 vendor-sourced, unverified |
| Pricing | `openeducat.org` | 🔴 **internally inconsistent** — one comparison page lists *Free + $69–$1 119/yr*, a solutions page *Enterprise from $19 per staff user* |

🔵 **Recorded as claims, not capabilities**, and with the reason: a single-vendor domain supplied
**every** result for the query *"open source platform education LMS SIS ERP MIT Apache 2026
self-hosted"* — nine of nine results were `openeducat.org` pages in eight languages, the same
single-source pattern `p501` already flagged on this row. 🟢 **If an engagement depends on LTI 1.3
or OneRoster in OpenEduCat, the module must be read in the repository first** — this base has an
LTI corpus (`Cvmcosta/ltijs`, `1EdTech/lti-1-3-php-library`, `Harvard-University-iCommons/django-lti`)
to compare against. Registered as `Gap 503-F`.
