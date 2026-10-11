---
industry: education
region: Global
updated: 2026-10-11
---

# Education — foundational repos

**Pass 132, 2026-10-11.** p131's rows carried forward unchanged (they were verified hours earlier
in the same date window); 🔴 **one new row changes this page's headline recommendation and refutes
this page's own flagship gap** — see `README.md` → Pass 132, `P132-C`. These are the systems a
client already runs, or would sensibly adopt, and that AI work gets attached to. Licence is the
first column that matters: it decides whether Globant can ship a derivative at all.

🔴 **Read this before trusting a licence cell.** GitHub's `license.spdx_id` reports **`NOASSERTION`
("Other")** whenever its matcher does not recognise a `LICENSE` file as a known template. That is
*not* a finding of "no grant", and p130 published it as one. Where this KB has **read the payload**,
the payload wins and the cell below says so.

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
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The natural target for the administrative automation nobody else serves. 🔴 **Licence corrected by p131.** GitHub's API reports `NOASSERTION` and p130 published that as "review terms before use". This KB had already **read `master/LICENSE` in full — 8 241 bytes, genuinely LGPL-3.0** — and used that read to *retract* an even earlier "no grant" row. p130 reinstated the retracted claim by trusting the API field over its own evidence. **LGPL on an LGPL Odoo base: linking is fine, modifying the module itself carries reciprocity.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## The offline / low-connectivity stack (added by p132 — and it refutes this page's own gap)

🔴 **This page has carried, for several passes, that "the offline slot is the cleanest unclaimed
opportunity in this KB". It is not unclaimed.** It is occupied by the second-largest repository
anywhere in this KB.

| repo | licence | stars | origin | why it is foundational |
|---|---|---|---|---|
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 **Apache-2.0** | **39 444** | unplaced | **Offline-first knowledge and education server**: Wikipedia, thousands of books, courses, maps and optional local AI, all on hardware the client owns with no internet required. Architecturally a **Docker orchestration layer over containerised tools** — **Kiwix** powers the Information Library, **Kolibri** powers the Education Platform, **Ollama** powers the AI Assistant (the installer provisions Ollama on the host; an external OpenAI-compatible endpoint is also supported). 🟢 **Permissive, so a client can ship a derivative.** 850 commits, updated the day of this pass. |
| [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 **UNREAD** | 20 | unplaced | macOS / Apple Silicon port, bundling Ollama, Open WebUI, Kiwix, Kolibri and FlatNotes. Useful as a single-machine pilot before committing to the Docker stack. Licence not measured this pass. |
| [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) | 🟡 **UNREAD** | 2 | **APAC (India)** | Offline LMS for Class 10 Maths and Science on the Indian curriculum: FastAPI + React + RAG over structured chapter data with a local Ollama model, gamified quizzes, LAN-only operation, and a claimed Kolibri integration. 🔴 **Duplicate pair** with [`Tushar-cy/Ai-edge-learning-hub`](https://github.com/Tushar-cy/Ai-edge-learning-hub) (same owner, byte-identical description). Small, but the only row that targets a *named national curriculum* offline. |

🔵 **Why eleven passes missed it, and why the probe was not at fault.** p131 ran `kolibri stars:>2`,
got 86 repos, correctly resolved 3 to the Learning Equality family and 0 with AI. **The probe was
valid; the conclusion was false.** NOMAD *composes* Kolibri as a container and never names it in
its description — the dependency appears only in the README architecture. **A dependency is not
always visible in the metadata of the thing that depends on it.**

🟢 **What this changes for an engagement.** The low-connectivity offer stops being *"build an
offline tutor"* and becomes *"deploy and extend an Apache-2.0 stack that already composes content,
library and local inference"* — faster, cheaper and far more defensible in a procurement
conversation. Kolibri (MIT) remains the right content layer; what changed is that the integration
around it already exists. See `compose/patterns.md` → P2.

## Administrative automation — the first optimiser (added by p132)

| repo | licence | stars | origin | what it gives you |
|---|---|---|---|---|
| [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | Conflict-free academic timetable generation under **India's NEP 2020**: electives, faculty availability, courses, rooms, balanced workloads, scenario simulation, manual overrides, exports, and a natural-language interface over MCP. 🟢 **The "most-cited driver, least-served tier" finally has a repo, and it is an optimiser rather than an LLM wrapper.** 🔴 One star — a reference design, not a dependency. |

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

## The system-of-record tier (restored by p131)

p130's declared gaps said *"`openeducat_erp` (licence unclear) and `academico` (small) are the whole
field."* 🔴 **They are not.** This KB read a system-of-record tier in an earlier pass and p130's
rewrite dropped it. Restored here, because "there is no open-source SIS" and "every open-source SIS
is copyleft" are completely different briefings for a client.

| repo | licence | why it matters | the catch |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | **NOASSERTION** (API) — read terms | **662★**, pushed 2026-10-05, 454 forks. Full school management on Frappe: students, programmes, fees, assessment. Sits beside ERPNext finance/HR with no integration work. | Licence does not resolve to an OSI identifier via the API; GPL-3.0 in the Frappe family's own documentation. **Read `LICENSE` before committing** — this is exactly the row class p130 got wrong. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886★. The Odoo-based ERP; the broadest functional coverage of the tier. | Odoo module, so you inherit the Odoo ecosystem *and* its constraints. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | **404★**, pushed 2026-10-07. Laravel/Filament. **The only permissive SIS**, so the only forkable base for a closed client product. Carries the topic `student-information-system`. | Small, and aimed at small-to-mid institutions rather than a university of record. |
| **RosarioSIS** | GPL-2.0 | A genuine student information system with real deployments. | GPL-2.0 — the most restrictive option here. |
| **Gibbon** | GPL-3.0 | School platform with a long institutional track record. | GPL-3.0 reciprocity. |
| **openSIS** / **Fedena** | copyleft / mixed | Named in this KB's earlier reads of the tier; both long-lived. | Neither is permissive; verify the current edition's terms, since both have had commercial forks. |

🔵 **Provenance of the four rows without links.** RosarioSIS, Gibbon, openSIS and Fedena are
carried from **this KB's own earlier read of the tier** (`agents/trending.md:5160`, which recorded
`RosarioSIS mobile@899f6da` GPL-2.0, `Gibbon v31.0.00@683d2c4` GPL-3.0 and `OpenEduCat 19.0@1c95cef`
LGPL-3.0 at specific commits). 🔴 **They were NOT re-verified this pass and are deliberately listed
without links** — a row this pass did not measure does not get presented as one it did. Re-verify
before quoting them to a client; the three linked rows above were verified this pass and are in
`evidence/verified-repos.2026-10-11-p131.tsv`.

**The honest summary for a client:** there are **at least six** open-source systems of record. Exactly
**one** (`academico`, MIT) can become a closed derivative; one more (`openeducat_erp`, LGPL-3.0)
permits linking without reciprocity. The rest are GPL-family. 🔴 **So the gap is not supply — it is
that the system-of-record tier is almost entirely copyleft**, which is a licensing conversation at
the start of an engagement, not a missing-software conversation.

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release. 🟢 **And if the constraint
is connectivity rather than licensing, start from `Crosstalk-Solutions/project-nomad`
(Apache-2.0, 39 444★) instead of assembling the stack yourself** — it already composes Kolibri,
Kiwix and a local model, and it is permissive enough to fork.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia
  (Apache-2.0) and Sakai (ECL-2.0) are the permissive options and neither is a drop-in replacement
  for either. 🟢 **SURVIVES.**
- ~~**No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.~~ 🔴 **REFUTED by p131** — see the system-of-record tier
  above: at least six systems, read by an earlier pass and dropped by p130's rewrite. 🟢 **The
  surviving gap is that the tier is almost entirely copyleft, with `academico` (MIT) the lone
  permissive base — and that no AI *agent* targets any of them** (`agents/top.md`).
- **Canvas is the quietest major platform** (last push 2026-04-30, ~5 months) 🔴 **and it is now
  ~5.5 months quiet, unchanged on re-check this pass.** Worth raising explicitly before
  recommending it as an actively developed base — it is still the richest API surface in the
  sector, which is why every connector targets it.
- ~~**Three Kolibri-family repos, zero AI on any of them.** A valid re-probe this pass
  (`kolibri stars:>2` → 86 repos) resolves the family to three Learning Equality repos; the other
  83 are name collisions. **The offline slot is still the cleanest unclaimed opportunity in this
  KB** (`intel/trends.md` → T8).~~ 🔴 **REFUTED BY p132.** The family resolution was right —
  [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, 1 141★),
  [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192★),
  [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
  (52★) — **and the conclusion drawn from it was wrong.**
  [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
  (**Apache-2.0, 39 444★**) runs Kolibri as its education container beside Kiwix and Ollama, and
  does not contain the string `kolibri` in its description. 🟢 **The surviving gaps are narrower and
  real: (a) no AI project builds *inside* Kolibri itself** — NOMAD orchestrates it from outside and
  the Learning Equality repos carry no AI; **(b) nothing offline targets LATAM.** The one
  curriculum-specific offline row found is Indian (`Tushar-cy/Offline-AI`), and LATAM — where this
  KB argues offline is a first-class requirement rather than an edge case — has none.
  🟡 **Also note a new collision source: Aleph Alpha ships a 78B model called "Kolibri".**
