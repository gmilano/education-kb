---
industry: education
region: Global
updated: 2026-11-13
---

# Education vertical platforms — real systems to customize AI on top of

The education equivalent of "Odoo for ERP". These are the systems institutions
already run; an AI engagement almost always means **adding an agent layer to one
of these**, not replacing it. All licenses and star counts verified from the
repository page (2026-11-13, with the LTI and Moodle-MCP rows verified this
pass).

## The decision that governs every education engagement

**Do not fork the LMS.** Seven of the eight significant open-source LMS
platforms are GPL-3.0 or AGPL-3.0 (only Sakai is permissive, ECL-2.0). A fork
makes the client's derived platform copyleft. Instead mount the AI layer as an
**LTI 1.3 tool** or an **MCP server** against the platform's API, keep that
layer MIT/Apache, and emit **xAPI** or **Caliper** events so the institution can
report on it. Every pattern in `compose/patterns.md` follows this shape.

**Update (fifth pass, 2026-11-13): there is now a third mounting surface, and it
is the one that reaches the student record.** Where the incumbent system is built
on a **general-purpose platform**, the agent surface may already exist as a
*platform* connector rather than an education one. **OpenEduCat is Odoo addons,
and Odoo has two mature MCP servers whose tools take the model name as a
parameter** — so the leading open-source education ERP is agent-reachable today
with no education-specific code. See the SIS table below. 🔵 **The general rule
to carry into any engagement: before concluding a platform has no agent surface,
check the platform it is *built on*.**

**Both halves of that sentence now have verified implementations.** LTI 1.3:
`Cvmcosta/ltijs` (Apache-2.0, 373 stars, full LTI Advantage). MCP: Canvas via
`canvas-mcp` (MIT, 324) and — new this pass — **Moodle via `Faixiang/Moodle-MCP`
(MIT, 206)**. The previous edition of this file said Moodle had no significant
MCP server. It does.

## Learning management — the host systems

| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |
|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.6k | Global, strongest in EMEA, LATAM, APAC public education | Mature plugin API; LTI 1.3; web services REST API. **MCP now available: `Faixiang/Moodle-MCP` (MIT, 206) read-only; `falkenslab/moodle-mcp` (MIT) ~260 tools via browser SSO; `MarcosNahuel/moodle-mcp` (MIT) idempotent content publishing** |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | MOOCs, corporate academies, national platforms | **`openedx-ai-extensions`** is the official AI plugin point; XBlocks; deploy via `tutor`. MCP only via `openedx-mcp` (AGPL-3.0, 3 stars) |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | North American higher ed (dominant) | Rich REST API + LTI 1.3; **`canvas-mcp` (MIT, 324) — README claims up to 128 tools, sidebar says 102** |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 | 3.4k | SMB/corporate training, India | Frappe framework hooks; shares a stack with ERPNext |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Research universities | **Permissive license** — the one platform a studio can extend without copyleft reaching the product. `Simon-Initiative/lti_1p3` (MIT, Elixir) comes from adjacent higher-ed work |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LATAM, francophone Africa, Spain | Web services API; accessibility-first. PHP — pair with `packbackbooks/lti-1-3-php-library` (Apache-2.0) |
| ILIAS | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | German-speaking EMEA, vocational and public sector | Plugin slots; SCORM/xAPI |

## The integration layer — build once, mount everywhere

| Library | Repo | License | Stars | Use when |
|---|---|---|---|---|
| ltijs | https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | Default choice. Node.js, full LTI Advantage (launches, Deep Linking, AGS, NRPS, Dynamic Registration) |
| lti-1-3-php-library | https://github.com/packbackbooks/lti-1-3-php-library | Apache-2.0 | 54 | The client is a PHP shop (Moodle, Chamilo); roster via NRPS, grade writeback via AGS |
| lti_1p3 | https://github.com/Simon-Initiative/lti_1p3 | MIT | 16 | Elixir stack, or you need to act as **Platform** as well as Tool |
| lti-tool | https://github.com/lti-tool/lti-tool | MIT | 8 | Serverless target (Lambda, Cloudflare Workers); early but the only one of its shape |

## Student information systems and institutional ERP

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | **SIS + LMS + finance as Odoo modules** — the literal "Odoo for education", and **the only open-source SIS with a working agent surface (new finding, fifth pass)**. 789 forks; branch/tag `19.0`; modules `openeducat_core`, `_admission`, `_exam`, `_fees`, `_attendance`, `_timetable`, `_parent`, `_library`, `_activity`, `_assignment`, `_classroom`, `_facility`. **Because it is Odoo addons, it is reachable by a generic Odoo MCP server** — `erpipe-org/mcp-odoo` (MIT, 433★, three-call gated writes) or `ivnvxd/mcp-server-odoo` (MPL-2.0, 415★, per-model allowlist in a companion module) — so `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` need no new connector. 🔴 **Architecturally verified, not yet run against a live instance (`Gap 286`).** If the client already runs Odoo this is now the shortest path **by a wide margin**. |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 707 | **New this pass.** Admissions, fees, scheduling, exams, attendance on the Frappe framework. **The one-framework play: pair with `frappe/lms` (AGPL-3.0) and ERPNext for SIS + LMS + ERP on a single stack** — but the two halves carry *different* licenses (GPL-3.0 vs AGPL-3.0), which matters the moment anything is network-served. License read from `license.txt`, not GitHub's sidebar. Strong India/SMB footprint. |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | K-12 school management; widely deployed in LATAM, Spanish/French/Portuguese localization in core. |
| Gibbon | https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible school management; strong in international K-12 schools. |
| openSIS Classic | https://github.com/OS4ED/openSIS-Classic | GPL (README) | 351 | Student information system; commercial editions available from OS4ED. |

🔴 **Agent surface across the SIS row, stated plainly because it decides which
client you can serve this quarter.** **OpenEduCat: yes**, via the Odoo
connectors above. **Frappe Education and Frappe LMS: unknown and worth one
search** — they sit on the Frappe framework, which is the next place to look for
the same generic-connector trick, and nobody has checked. **RosarioSIS
(PHP/Postgres) and Gibbon (PHP/MySQL): no agent interface and no generic
connector of the Odoo kind** — searched by project name this pass, nothing
returned. Those two are the genuinely unserved incumbents, and they are
precisely the ones that dominate **LATAM K-12** (RosarioSIS) and
**international K-12** (Gibbon). 🔵 **Engagement reading: a LATAM K-12 client on
RosarioSIS is a build; a private-education or India/LATAM SMB client on
OpenEduCat is a configuration.**

## Content, delivery and classroom

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| Kolibri | https://github.com/learningequality/kolibri | **MIT** | 1.2k | Offline-first learning platform. The right base for low-connectivity deployments (rural LATAM, Sub-Saharan Africa, remote APAC). Permissive. |
| Oppia | https://github.com/oppia/oppia | **Apache-2.0** | 7.0k | Interactive lesson "explorations" with built-in misconception handling. Permissive and substantial. |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | The de facto interactive-content format; renders inside Moodle, Canvas, Open edX. |
| Khan Perseus | https://github.com/Khan/perseus | **MIT** | 1.6k | Khan Academy's exercise editor/renderer. MIT — drop real exercise rendering into any product. |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Virtual classroom with LTI into Moodle/Canvas; recordings feed transcript pipelines. |
| Opencast | https://github.com/opencast/opencast | ECL-2.0 | 511 | Lecture capture at scale — the upstream source for transcript/summarization agents. |
| Anki | https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition scheduling; the algorithm is the asset for retention features. |

## Teaching, grading and learning-data infrastructure

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| JupyterHub | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user notebooks; the standard for CS/data-science teaching. |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assignment release and autograding for notebooks. **The grading substrate to wrap an agent around.** |
| pyKT | https://github.com/pykt-team/pykt-toolkit | **MIT** | 461 | Deep knowledge-tracing benchmarks — real mastery estimation to pair with an LLM tutor. |
| ODK Collect | https://github.com/getodk/collect | Apache-2.0 | 805 | Offline Android form collection; used for education field assessment at national scale. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | Apache-2.0 (README) | 2 | Essay scoring + label-aware feedback, locally deployable. Prototype scale, but the only open grading *system* found. |
| TAO | https://github.com/oat-sa/tao-core | GPL-2.0 | 64 | **New this pass — the one assessment *platform* with real item banking that a client may already be running.** Long-standing open e-testing system. 🔴 **Two constraints decide whether it fits: the open-source edition is QTI 2.2-based, not QTI 3, and it ships no Results Management** — a QTI 3 contract or a reporting requirement lands outside it. GPL-2.0: a host to extend, not a base to embed. |
| QTI 3 item player | https://github.com/amp-up-io/qti3-item-player | **MIT** | 30 | **New this pass — the delivery surface for assessment, and the only QTI repo claiming conformance certification** (QTI 3 Basic *and* Advanced "Delivery"). 🔴 Vue 2.6, which is end-of-life. Pair with `LongsightGroup/qti3` (MIT) for authoring, scoring and migration — **no single repo does both**. |
| Caliper spec | https://github.com/1edtech/caliper-spec | IMS spec-document license | 22 | Learning analytics event spec. Implement it; do not vendor the repo. **Implementations now exist — see the two rows below and `repos/foundations.md`.** |
| caliper-ts | https://github.com/CarnegieLearningWeb/caliper-ts | **MIT** (read from `LICENSE`; sidebar shows only a generic link) | 0 | **New this pass — the only permissively licensed Caliper sensor found anywhere.** TypeScript Sensor API, Caliper **1.1**. 🔴 Published to the **GitHub Package Registry** as `@imaginelearning/caliper-ts`, not public npm, and 0 stars — budget to carry it. |
| Moodle Caliper logstore | https://github.com/open-lms-open-source/moodle-logstore_caliper | GPL-3.0 | 1 | **New this pass — the only Caliper emitter for a real LMS, at any licence.** Moodle logstore plugin: Expander → Translator → Emitter, immediate or batched, Moodle **2.7+**. 🟢 GPL-3.0 is correct for a Moodle plugin and does **not** reach a separately deployed MIT/Apache AI layer. |

## Standards that make the above interchangeable

| Standard | Why it decides the architecture |
|---|---|
| **LTI 1.3 / LTI Advantage** | Build the AI tool once as an LTI tool provider and it mounts in Moodle, Canvas, Open edX, Sakai, and ILIAS. Highest-leverage single investment in an education engagement — and `ltijs` means you do not write it from scratch. |
| **xAPI** | Learner-activity telemetry; what an agent should emit so the institution can report on it. |
| **Caliper Analytics** | The 1EdTech-native alternative to xAPI; common in North American higher ed. **Updated fifth pass: six implementations now verified — an MIT sensor, a GPL-3.0 Moodle emitter, an Apache-2.0 analysis layer and LGPL-3.0 reference sensors — but NO permissively licensed event store, and 1EdTech's reference code is member-gated.** Free choice → still xAPI. Contract names Caliper → you write the store and nothing else. Ask which Caliper **version**: the only 1.2 implementation found is unlicensed. |
| **QTI** | Assessment item interchange — matters as soon as item banks must move between systems. **Updated fifth pass: seven implementations verified, five of them MIT — but scoring, item banking and *certified delivery* live in different repos, so every QTI engagement is a pairing exercise.** `qti3-item-player` (MIT) is certified delivery-only; `LongsightGroup/qti3` (MIT) authors, scores and migrates but claims no certification. 🔴 Confirm which **branch** a QTI licence was read from: `Learnosity/learnosity-qti` is MIT on `master` and GPL-2.0 on its default `develop`. |
| **SCORM** | Legacy but ubiquitous in corporate and vocational training; still the delivery format many EMEA/APAC clients require. |

## Declared gaps

- **No permissively licensed LMS at deployment scale** except Sakai. Surface
  this constraint in week one of any engagement that needs a proprietary
  derived platform.
- **MCP coverage is no longer absent for Moodle — it is fragmented.** Seven
  Moodle MCP servers verified, 1–206 stars, licenses split MIT/GPL/AGPL, and no
  two agree on tool surface or auth model (web-service token vs interactive
  browser SSO vs companion plugin). Canvas, by contrast, has consolidated on
  one 324-star MIT server. **Open edX remains the real gap**: `openedx-mcp`
  (AGPL-3.0, 3 stars) is the only option and it is reference-grade at best.
- 🟢 **SIS MCP: CLOSED for OpenEduCat, corrected again 2026-11-13 (fifth
  pass).** The fourth-pass correction below said SIS servers exist "but not for
  any SIS in this table." **That is now withdrawn too.** OpenEduCat **is in this
  table** and is reachable by a generic Odoo MCP server (`erpipe-org/mcp-odoo`,
  MIT, 433★; `ivnvxd/mcp-server-odoo`, MPL-2.0, 415★), because it is Odoo addons
  and those servers address models by name. 🔴 **Architecturally verified, not
  run (`Gap 286`).** What stays true: **RosarioSIS and Gibbon have neither an
  agent interface nor a generic connector** — they are the unserved rows, and
  they are the LATAM K-12 and international K-12 incumbents respectively.
  🔵 **The method worth institutionalising: when a vertical system has no agent
  surface, check the general-purpose platform underneath it.**
- **SIS MCP servers exist — but not for any SIS in this table. Superseded by the
  bullet above; kept for the record (fourth pass).** The previous three editions of this file said "no
  MCP server for any SIS" and called it a confirmed absence. That claim was
  **over-generalized and is now withdrawn.** Two verified MCP servers do reach a
  student information system: `oliverhruby/edupage-mcp` (MIT, 4 stars, **31
  tools**) over **EduPage**, the SIS used across Slovakia and Czechia, and
  `sukhrobyangibaev/mcp_hemis_student` (MIT, 0 stars) over **HEMIS**, the
  higher-education SIS used by Uzbek universities. **What remains true, and is
  the sharper statement:** OpenEduCat, RosarioSIS, Gibbon, openSIS and
  `frappe/education` — every *open-source* SIS in this table — still have **no**
  agent interface. The integration is happening against **national proprietary
  SIS products with captive markets**, built by individual developers, not
  against the open-source platforms a studio would deploy. Two consequences for
  an engagement: the topology is proven (so `P8` is no longer greenfield), and
  **EduPage's server reaches the SIS through a community library on undocumented
  endpoints** — a pattern to learn from, not a dependency to ship.
- **The learning-record store, by contrast, is now solved and permissive.** New
  this pass: `yetanalytics/lrsql` (Apache-2.0, 144) and `openfun/ralph` (MIT,
  51) as LRS implementations, with `DavidLMS/learnmcp-xapi` (MIT, 16) as the
  agent interface. **An LRS is not an SIS** — it holds learning *activity*, not
  the student record — so this closes the telemetry gap and leaves the advising
  gap exactly where it was.
