---
industry: education
region: Global
updated: 2026-10-17
---

# Foundational repos — Education

> The layer below the agents: platforms, standards, assessment engines and learner-model
> libraries that an engagement builds *on* rather than *with*. Licences read first-hand from
> each repository's `LICENSE` payload on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv) —
> the later pass adds 13 payload-verified repositories, refutes two published permissive claims
> (forma.lms, Fedena) and **retracts this file's own LATAM gap**.

## Permissive foundations (MIT / Apache-2.0 / BSD)

| Repo | Licence | Stars | Why it is a foundation |
|------|---------|-------|------------------------|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | **Interactive learning with automated feedback**, from TUM Applied Education Technologies. Programming, quiz, modelling and text exercises with automatic assessment and an integrated CI runner. The strongest MIT-licensed teaching platform found this pass — production-grade and university-maintained. **Pass 266:** it ships three *config-gated* AI subsystems — **Iris** (LLM tutor, [`ls1intum/Iris`](https://github.com/ls1intum/Iris), MIT), **Pyris** (the LLM microservice behind it, [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris), MIT) and **Athena** (feedback suggestion, [`ls1intum/Athena`](https://github.com/ls1intum/Athena), **licence UNVERIFIED — no payload**), plus **Hyperion** (AI exercise authoring, not a separate repo). Config-gated matters: the platform runs identically with AI off, which is the posture an EU AI Act high-risk classification wants. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | MIT | 4.1k | FSRS, the modern spaced-repetition scheduler. The highest-adoption learning-science component in open source. Pair with [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) (BSD-3-Clause) for a Rust core you can embed. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 450 | The reference PyTorch knowledge-tracing benchmark library: standard datasets, standard splits, comparable baselines. If a client asks "can you predict what this student knows", this is the honest starting point. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT | 352 | Source-code plagiarism detection (UGent). In the GenAI era this is no longer a niche: it is the integrity layer every coding course now needs. |
| [bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData) | Apache-2.0 | 313 | Education datasets plus download/preprocess tooling. Removes the first two weeks of any learner-modelling project. |
| [ZhijieXiong/pyedmine](https://github.com/ZhijieXiong/pyedmine) | MIT | 82 | Knowledge tracing **plus** cognitive diagnosis **plus** exercise recommendation in one library. Broader than pyKT where the deliverable is a recommender, not a predictor. |
| [HFUT-LEC/EduStudio](https://github.com/HFUT-LEC/EduStudio) | MIT | 78 | Unified library for student cognitive modelling, with a configuration-driven pipeline. Good for sweeping many models when the client wants a comparison, not a bet. |
| [numbas/Numbas](https://github.com/numbas/Numbas) | Apache-2.0 | 215 | Maths and science e-assessment: randomised questions, algebraic marking, SCORM-packaged output. Apache-2.0 makes it embeddable in a commercial deliverable. **Pass 266:** 215★, 4,209 commits, 130 forks, **Newcastle University** School of Maths, Stats & Physics (README-quoted → EMEA-origin). Tests run **entirely in the browser** — a Python 3 compiler producing a JavaScript runtime — so no student submission need leave the device. That answers a data-residency objection structurally rather than contractually. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | — | Framework for building **LTI** tools that plug into any compliant LMS. The sanctioned way to put an AI tool inside Moodle/Canvas/Open edX without forking the LMS. |
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | — | The xAPI (Experience API) specification itself. The vocabulary for "what did this learner actually do" across systems. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | — | SQL-backed **Learning Record Store** for xAPI. The missing piece between an agent that observes learning and a model that needs training data. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | — | Modern SCORM 1.2 / 2004 and AICC runtime. Most institutional content is still SCORM; this is how an agentic front end keeps reading it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | MOOC portal CMS (Django + React) from France Université Numérique. MIT means the client's catalogue front end is genuinely theirs. |
| [openfun/marsha](https://github.com/openfun/marsha) | MIT | — | Video management for education, same FUN-MOOC provenance. The companion to Richie when the course is video-first. |
| [academico-sis/academico](https://github.com/academico-sis/academico) | MIT | — | Student information system (Laravel): enrolment, attendance, results. MIT SIS data is the input every dropout-prediction model needs. |
| [haxtheweb/haxcms-php](https://github.com/haxtheweb/haxcms-php) | Apache-2.0 | — | HAX authoring/CMS for web-component-based course content. Content as components survives an LMS migration; content as LMS pages does not. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 *(README-stated — see note)* | — | The component API for Open edX. The entry point for putting an agent inside an Open edX course. |

| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | 6.9k | Full online learning platform built for low-resource contexts: structured lessons, built-in formative feedback, learner-progress model. **17,004 commits** on `develop`. The highest-adoption *permissively licensed* complete learning platform located by this KB — larger than Artemis and larger than every education agent except DeepTutor. |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1.4k | *"A system for assigning and grading notebooks."* **Autograding that already exists.** This file previously declared that no high-adoption open-source grading option was found; nbgrader is 1.4k stars, BSD-3-Clause and the default in university data-science teaching. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1.2k | *"the offline app for universal education"* — a complete learning platform that runs with **no internet connection**, syncing when a link appears. **39,803 commits.** MIT, which makes it the second permissive complete platform in this KB and the only one designed for intermittent connectivity. The natural base for rural LATAM and low-bandwidth APAC deployments. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | Apache-2.0 | 808 | *"Course management service that enables auto-graded programming assignments."* Initially developed by students at **Carnegie Mellon University** per its README. Apache-2.0 autograding with a course-management shell around it — the permissive counterpart to Artemis. |
| [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** | 41 ⚠️ | **India's national education stack — the APAC-origin platform this KB said did not exist.** The codebase under **DIKSHA**, run by NCERT/Ministry of Education. README: *"next-generation scalable open-source learning solution for teachers and tutors"*, mission *"improve learning outcomes for 200 million children across India"*. **38,046 commits, 317 forks — against 41 stars.** ⚠️ **Do not read the star count as adoption**: ministry-funded digital public infrastructure accrues commits, forks and deployments but almost no stars, which is precisely why star-sorted search never surfaced it. Backend: [`project-sunbird/knowledge-platform`](https://github.com/project-sunbird/knowledge-platform) (MIT). Mobile: [`Sunbird-Ed/SunbirdEd-mobile-app`](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) (MIT). |
| [oppia/oppia-android](https://github.com/oppia/oppia-android) | Apache-2.0 | — | The Android client beside `oppia/oppia`. Pairs with `learningequality/kolibri` (MIT) wherever mobile-first, low-connectivity delivery is the actual constraint rather than an afterthought. |

**21 permissive foundation rows** (17 from pass 264, 4 added and payload-verified in pass 265).

> **Note on XBlock:** the repository's `README.rst` states *"The code in this repository is
> licensed the Apache 2.0 license unless otherwise"* and points at `LICENSE.txt`, but that
> path did not serve a payload on the raw paths tried this pass. The licence is therefore
> **README-stated, not payload-read** — the weakest evidence grade in this file, and marked
> as such rather than quietly promoted.

## Copyleft foundations — real, but priced

| Repo | Licence | Why you still care |
|------|---------|--------------------|
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 *(in `COPYING.txt`, not `LICENSE`)* | The world's most deployed LMS and the largest plugin ecosystem in education. GPL is survivable because the integration point is a plugin boundary. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | MOOC-grade platform behind edX. **This base previously published Apache-2.0 for this repo — that was wrong, and the error mattered**: AGPL's network clause is exactly the kind of obligation a hosted-deployment engagement must price in from day one. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 *(prior cell said GPL-2.0)* | Lightweight LMS with deep LATAM public-sector deployment. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | The institutional LMS of the German-speaking EMEA market. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | School management / SIS. Attendance and behaviour data — the signal dropout models actually run on. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | K-12 student information system, light footprint, widely self-hosted. |
| [Vacademy-io/vacademy_platform](https://github.com/Vacademy-io/vacademy_platform) | AGPL-3.0 | Modern e-learning platform with assessment management. AGPL network clause applies. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | **Brazilian school-management system, and the LATAM-origin foundation this file previously said did not exist.** Originally built by the *prefeitura de Itajaí (SC)* and published on the Brazilian federal **Portal do Software Público in 2008** for Secretarias de Educação nationwide. 719 stars, **34,948 commits**, last commit **2026-10-14**. Laravel/PHP. Government provenance is exactly what Brazil's digital-sovereignty guidance asks for. |
| [portabilis/i-diario](https://github.com/portabilis/i-diario) | AGPL-3.0 | The teacher-facing portal for i-Educar (*portal do professor*), last commit **2026-10-09**. **Note for legal review: the licence payload in this repo is a Portuguese translation of the AGPL-3.0 text, not the FSF's English original.** FSF translations are unofficial; cite the English AGPL-3.0 in any SOW. AGPL's network clause applies to a hosted deployment. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 | Lecture capture and academic video management, university-consortium maintained. ECL-2.0 is Apache-derived and OSI-approved but scopes its patent grant to educational use — the same distinction this KB flagged on Sakai. |
| [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0 | Autograding platform from UCLouvain. The EMEA counterpart to Autolab, at an AGPL price. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | **GPL-3.0** | Interactive content types (the H5P authoring ecosystem embedded in Moodle, Canvas and Drupal). **H5P is widely cited — including in earlier Globant KB cycles — as MIT. The PHP library's payload is GPL-3.0.** Content authored *with* H5P is yours; the library you ship is not permissive. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | Web conferencing built for teaching (breakouts, whiteboard, LMS integrations). LGPL means linking is survivable; modification is not free. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 | School ERP on the Frappe stack: admissions, fees, assessment. The Frappe/ERPNext alternative to OpenEduCat's Odoo lineage. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | Frappe Learning. AGPL network clause; pairs with `frappe/education` when the client is already on ERPNext. |
| [OpenBoard-org/OpenBoard](https://github.com/OpenBoard-org/OpenBoard) | GPL-3.0 | Interactive-whiteboard software (Geneva-origin) with pt-BR localisation. Classroom-front-end, not server-side; GPL is rarely a problem for a desktop deployment. |

## What to reach for, by job

- **"Put an AI tutor inside our existing LMS"** → `tsugi` (LTI) or `openedx/XBlock`. Do not fork the LMS.
- **"Automatically assess student work"** → `Artemis` for programming and modelling, `Numbas` for maths.
- **"Tell us which students are at risk"** → `academico` or `GibbonEdu` for the data, `pykt-toolkit` or `pyedmine` for the model, `lrsql` + `xAPI-Spec` for the event stream.
- **"Make retention stick"** → `fsrs4anki` / `fsrs-rs`. Spaced repetition is the one intervention with a scheduler worth reusing instead of inventing.
- **"We must prove academic integrity"** → `dolos`.
- **"Our content is all SCORM"** → `scorm-again`, and keep the content where it is.
- **"Grade programming work automatically"** → `autolab/Autolab` (Apache-2.0) for a course-management shell with autograding, `jupyter/nbgrader` (BSD-3) where the work is notebooks, `Artemis` (MIT) where feedback matters more than marks. All three permissive; none of them an agent.
- **"Our learners lose connectivity"** → `learningequality/kolibri` (MIT). Offline-first is an architecture, not a setting, and retrofitting it onto a server-rendered LMS is a rebuild.
- **"Brazilian municipal or state network, sovereignty-first"** → `portabilis/i-educar` (GPL-2.0) for the SIS and `i-diario` (AGPL-3.0) for the teacher portal, both actively maintained in October 2026, both already inside the federal software-public lineage. Keep studio code on the permissive side of an LTI or API boundary.

## Declared gaps — and three retractions

### Retracted: "no LATAM-maintained foundational repo identified"

**This was wrong, and it was wrong in the direction that costs the studio most.**
[`portabilis/i-educar`](https://github.com/portabilis/i-educar) is a Brazilian school-management
system with **34,948 commits**, a commit from **2026-10-14**, origin in the *prefeitura de
Itajaí (SC)*, and publication on the **Portal do Software Público** of the Brazilian federal
government in 2008. Its teacher portal `i-diario` committed on **2026-10-09**. The region does
publish this layer; this KB had not looked in Portuguese.

The accurate, narrower claim: **no LATAM-origin *permissively licensed* foundation and no
LATAM-origin *agent* has been identified.** i-Educar is GPL-2.0 and i-Diário is AGPL-3.0 — the
LATAM supply exists and arrives copylefted, which is a pricing question, not an absence.

### Retracted: "no high-adoption open-source grading option"

`jupyter/nbgrader` (BSD-3-Clause, 1.4k) and `autolab/Autolab` (Apache-2.0, 808, CMU-origin)
are both higher-adoption than every education *agent* in this KB except DeepTutor. What does
not exist is a grading **agent**; autograding **platforms** are permissive, mature and
boring — which is the correct thing to put in front of a regulator.

### Retracted in pass 266: "no APAC-origin education platform"

Pass 265 narrowed its APAC conclusion to this one remaining gap and briefed integration work
on the strength of it. **[`Sunbird-Ed/SunbirdEd-portal`](https://github.com/Sunbird-Ed/SunbirdEd-portal)
is MIT, 38,046 commits, 317 forks, and is the stack beneath DIKSHA** — India's national school
education platform under NCERT. APAC publishes the platform layer, at national scale, under the
most permissive licence this KB tracks.

**Why it hid for 265 passes, stated as a method defect rather than bad luck:** every leg this
base runs sorts GitHub topic listings **by stars**, and `SunbirdEd-portal` has **41**.
Ministry-funded digital public infrastructure is used by system integrators and education
departments, not by developers who star repositories. The instrument cannot see this class of
code at all.

| | Sunbird | A star-findable agent |
|---|---|---|
| Stars | **41** | 300 – 41,500 |
| Commits | **38,046** | 21 – 12,437 |
| Forks | **317** | 1 – 395 |

**Standing instruction for later passes:** rank the *platform* layer by **commits and forks**,
and probe national-programme names by hand (DIKSHA/Sunbird, i-Educar, Kolibri, Me Capacito,
Ceibal). Also note the slug trap: `Sunbird-Ed/sunbird-ed-portal` does **not** resolve — the
live slugs are camel-case, and a kebab-case guess returns nothing that looks any different
from absence.

### Still open

- **Permissive complete platforms are at least three deep, not one** *(superseded in pass 266 — see the corrected count below)*. **OpenOLAT** (Apache-2.0),
  **Kolibri** (MIT) and **Oppia** (Apache-2.0) are now all payload-verified; see
  [`verticals/solutions.md`](../verticals/solutions.md) for how they differ in scope. The
  previous "exactly one candidate" framing understated the shelf and should not be repeated in
  a pitch. Everything else at full-LMS scale is still GPL or AGPL.
- **Star counts marked `—`** were not re-verified this pass; the licence was. An unverified
  number is left blank rather than carried forward from a prior pass, because carried-forward
  numbers are how this base previously published "pykt 1.2k" for a 450-star repository.
- **~~No LATAM-maintained foundational repo identified.~~ — struck in pass 266 as an
  internal contradiction.** This bullet survived in "Still open" while the *top of this same
  section* retracted exactly that claim on the evidence of `portabilis/i-educar` (34,948
  commits, commit 2026-10-14). Both statements were published in the same file on the same
  day. The accurate version: **LATAM publishes this layer and it arrives copylefted** —
  i-Educar is GPL-2.0, i-Diário AGPL-3.0. What is still missing is a LATAM-origin
  **permissively licensed** foundation. Chamilo, often cited for its deep LATAM public-sector
  footprint, is European-maintained (Belgium/Spain) and GPL-3.0.
- **Cross-shelf consistency is now a required check.** Two contradictions were found *inside
  this base* in pass 266 — this bullet, and `agents/top.md` declaring the grading category
  empty while line 21 of this file carried an MIT automated-feedback platform. Both were
  falsifiable with one `grep`, not more searching. **Before republishing any declared gap,
  grep the other shelves for its own counter-evidence.**
- **Permissive platform count, corrected again:** with **Sunbird** (MIT) and **Artemis** (MIT)
  the permissive complete-platform shelf is **five** deep — OpenOLAT, Kolibri, Oppia, Sunbird,
  Artemis — not three and certainly not one. Each prior count was published as if final.
