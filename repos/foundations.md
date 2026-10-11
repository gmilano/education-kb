---
industry: education
region: Global
updated: 2026-10-11
---

# Education — foundational repos

**Pass 130, 2026-10-11.** Full rewrite. These are the systems a client already runs, or would
sensibly adopt, and that AI work gets attached to. Every row verified this pass via GitHub repo
search (licence, stars, last push, fork flag). Licence is the first column that matters: it decides
whether Globant can ship a derivative at all.

## The platforms

| repo | licence | stars | last push | origin | why it is foundational |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | **9 241** | 2026-10-10 | North America (Blindside Networks, Canada) | The open virtual-classroom stack: WebRTC audio/video, whiteboard, breakouts, recordings. LGPL means linking is fine; modifying the library itself carries reciprocity. The place live-session AI (transcription, attention, summarisation) attaches. |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **8 195** | 2026-10-10 | North America (Open edX / Axim) | The LMS + Studio behind MOOC-scale deployments. **Renamed:** this repo was `openedx/edx-platform`; the old URL still resolves and the README says "formerly known as edx-platform". Write the new name — earlier passes of this KB cite the old one. |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | **7 473** | 2026-10-09 | APAC (Moodle HQ, Perth, Australia) | The most deployed LMS in the world, ~2 000 plugins. **Important for delivery:** this GitHub repo is a *public mirror* of `git.moodle.org` — pull requests do not go here, and it publishes no GitHub releases. Contribution goes through Moodle's own tracker and git server. |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | **6 863** | 2026-04-30 | North America (Instructure, US) | The dominant LMS in North American higher ed and the one with the richest third-party API surface — which is why every MCP connector on the agent shelf targets Canvas first. Note the last push is 2026-04-30, the quietest of the major platforms. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | **6 845** | 2026-10-11 | Global (Oppia Foundation) | An online learning platform built around structured, explorable lessons with built-in misconception handling. **The only major education platform under a permissive licence** — so the one a client can fork into a closed product without reciprocity. Underrated for exactly that reason. Android client: [`oppia/oppia-android`](https://github.com/oppia/oppia-android) (Apache-2.0, 418). |
| [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | **3 299** | 2026-10-11 | APAC (Frappe, India) | Modern, actively developed LMS on the Frappe framework — so it sits next to Frappe/ERPNext finance and HR data without integration work. The strongest APAC-origin platform here. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2 336 | 2026-10-11 | unplaced | Next-generation learning platform, Python/Next.js, AI features first-class rather than bolted on. Young, fast-moving. |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | AGPL-3.0 | 1 717 | 2026-10-11 | unplaced | Education platform aimed at companies running cohort training. Relevant to corporate-L&D engagements rather than academic ones. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1 237 | 2026-10-09 | North America (Apereo Foundation) | Long-lived Java academic LMS. ECL-2.0 is Apache-2.0 with an educational-community patent tweak — **permissive**, and the licence most people misread as restrictive. Strong fit where a client already runs Java/Oracle estate. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | 1 127 | 2026-10-08 | EMEA (Overhang.IO, France) | The Docker-based Open edX distribution — in practice *the* supported way to stand up and upgrade Open edX. A large first-party plugin ecosystem, all AGPL-3.0: `tutor-mfe` (micro-frontends), `tutor-cairn` (real-time analytics), `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. If the engagement is Open edX, it is a Tutor engagement. |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 141 | 2026-10-10 | Global (Learning Equality) | Offline-first learning platform for low- and no-connectivity classrooms; content syncs by LAN or USB. **MIT-licensed**, which with its offline design makes it the single best base for rural LATAM, African and South Asian deployments. Content tooling: [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192). |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1 009 | 2026-10-10 | EMEA (Chamilo Association, Belgium) | LMS built around ease of use and accessibility, with real institutional adoption in Francophone Europe and Spanish-speaking LATAM. The most LATAM-relevant of the EMEA-origin platforms. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | **NOASSERTION** | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The closest thing to a student information system in open source, which makes it the natural target for the administrative automation nobody else serves. **Licence reads as "Other": review terms before use.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## Supporting infrastructure

| repo | licence | stars | what it gives you |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 470 | The component framework for custom learning activities inside Open edX. Permissively licensed even though the platform around it is AGPL — so a custom XBlock is the lowest-friction way to put an AI activity inside Open edX. |
| [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | 476 | Sandboxed execution of untrusted code. Directly reusable wherever an agent runs learner-submitted or model-generated code — an auto-grader for programming courses, for instance. |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 354 | Modern SCORM/AICC/xAPI runtime in TypeScript. The bridge between legacy courseware a client already owns and anything new. |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 316 | Django/React CMS for building course catalogues and education portals in front of Open edX. From France Université Numérique, so it is proven at national scale in EMEA. |
| [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | 263 | The H5P interactive-content family (Norway); the Moodle binding is [`h5p/moodle-mod_hvp`](https://github.com/h5p/moodle-mod_hvp) (GPL-3.0, 157). The standard way to ship interactive activities into an existing LMS. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 404 | Laravel/Filament school-management platform for small and mid-size institutions. MIT, so the most forkable administrative base here. |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | 203 | LTI tool-provider/consumer library. LTI is how an external AI tool gets launched from inside any compliant LMS — the integration path that avoids touching platform source, and therefore avoids AGPL reciprocity entirely. |

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia and Sakai
  are the permissive options and neither is a drop-in replacement for either.
- **No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.
- **Canvas is the quietest major platform this pass** (last push 2026-04-30, ~5 months). Worth
  re-checking next cycle before recommending it as an actively developed base.
