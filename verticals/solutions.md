---
industry: education
region: Global
updated: 2026-10-31
---

# Vertical education platforms (customisable with AI on top)

Real, deployed systems that run an institution's operations — the education
equivalent of Odoo for ERP. These are the systems a client already has, and the
systems an AI layer gets attached to.

## 🆕 `p574` — twelfth pass, 2026-10-31 — 🟢 THE ASSESSMENT-DELIVERY AND ACCESSIBILITY VERTICAL, which this base has never held: **TAO** is the QTI platform of record and it is `GPL-2.0`

🔵 **Why this page needed it.** Every row above runs *teaching* or *records*. The
third system an institution actually operates is **assessment delivery** — the
thing that must survive an audit, an appeal and an accommodation request — and
this page held no row for it. 🔴 The adjacent obligation is dated: in the United
States `April 26, 2027` / `April 26, 2028` under the ADA Title II web rule, and in
the EU `EN 301 549` under the Web Accessibility Directive. See
[`../intel/market.md`](../intel/market.md).

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| **TAO** | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | **GPL-2.0-only** (licence file `18,025 B`; `composer.json` agrees) | — (unread) | EMEA | The **QTI-native** computer-based testing platform, OAT SA (Luxembourg). Item banking, delivery, proctored sittings, results. Used by ministries and exam boards; the reference implementation standards-conformance arguments are made against. 🔴 **GPL-2.0 — deploy it, do not vendor it.** |
| **TAO / QTI items** | [oat-sa/extension-tao-itemqti](https://github.com/oat-sa/extension-tao-itemqti) | **GPL-2.0** (licence file `18,025 B`) | — (unread) | EMEA | TAO's item authoring and rendering extension — the part that reads and writes **QTI** itself. 🟢 New to this base entirely: `0` mentions in `573` passes. |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | **GPL-3.0-only** (`35,147 B`; `package.json` **and** `composer.json` agree) | 117 | North America | The Universal Design Online content Inspection Tool: scans a **Canvas** course's content for accessibility defects and fixes them in place. University of Central Florida. 🟢 **The nearest thing to an off-the-shelf Title II remediation tool in open source.** |
| **Cboard** | [cboard-org/cboard](https://github.com/cboard-org/cboard) | **GPL-3.0-only** (`35,141 B`; `package.json` agrees) | 766 | Global | Browser-based **AAC** board with text-to-speech, used in classrooms for non-verbal learners. Deployed, multilingual, and the obvious host for an AI symbol-prediction layer. |

🔴 **All four are copyleft, and that is the finding, not an accident of
sampling.** The permissive supply in this layer is converters and browser
extensions (see [`../repos/foundations.md`](../repos/foundations.md)); the
*platforms* are GPL. 🔵 **The engagement shape that follows** is the one `p557`
established for the education-ERP vertical: **client-hosted, deployed unmodified,
customisation in separately licensed extensions, patches upstream.** It is a
services engagement, not a product one — and it is sellable precisely because the
deadline is the client's, not the vendor's.

🟢 **One existing row corrected on this page by a first-hand read:** `OpenOlat`'s
licence cell said *"Apache-2.0 (README badge; sidebar unnamed)"*. The licence file
at `master` is **`10,982 B` of Apache-2.0**, with a `14,712 B` `NOTICE.TXT`
alongside. The badge was right; it is now **measured**, which is the difference
between a citation and a claim.

## Eleventh pass (`p573`, 2026-10-31) — 🟢 THE SIS AXIS IS NOW MEASURABLY EXHAUSTED: `topic:student-information-system` (**187**) read 20 deep, **zero** new, and every platform-grade row was already on this page

🔵 **This is a completeness result, and it is the first one this page can
actually defend.** Earlier passes added SIS rows opportunistically. This pass
swept the axis GitHub itself names for the category and compared every top row
against this base's `3,168`-row address ledger.

| axis | repositories | rows read | new to this base |
| --- | --: | --: | --: |
| 🟢 [`topic:student-information-system`](https://github.com/topics/student-information-system) | **187** | 20 | 🟢 **0 — and that is the finding** |

🟢 **The three platform-grade rows in the axis's top 20 are all already shelved
here, with grants read first-hand in earlier passes:**
[francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis)
(649★, **GPL-2.0**), [academico-sis/academico](https://github.com/academico-sis/academico)
(410★, **MIT**), [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic)
(347★, **GPL-2.0**). 🟢 **So the claim this page could not previously make is now
measured: for open-source student information systems, this KB holds the
deployable population, not a sample of it.**

### 🔴 And the reason the axis looks bigger than it is

🔴 **Below ~300★ the axis is almost entirely student coursework, not software an
institution could run.** Rows 4–20 of the top 20 include a C# WPF desktop app
(20★), a Django "student data application" (15★), several PHP admin-panel
exercises (7–12★), two unofficial scraping APIs for commercial SIS products
(Follett Aspen, SRM University), and — tagged `student-information-system` — **a
bike-rental app for students near a university campus** (7★).

🔵 **Consequence for this page, stated as a rule:** the open-source SIS field has
a **hard floor at roughly 300★**, below which the tag stops denoting
institution-grade software. 🟢 **That floor is a genuine property of this
category and not of GitHub's star distribution generally** — compare
`topic:learning-management-system`, where this KB has shelved real platforms at
**10★**, **54★** and **102★** (`euron-open-lms`, `TutorLoom`, `Mentingo`). 🔴 **So
"sweep below the star floor", which this base adopted as a general rule in
`P-572-C`, is productive for LMS and agent axes and wasteful for SIS.** The rule
needs a per-axis qualifier, and this is the first counter-example measured.

### 🔵 What this means for an engagement

🟢 **The permissive/copyleft shape of the SIS layer is now settled and it is
uncomfortable:** of the three deployable systems, **two are GPL-2.0** — which
carries *no patent grant* and is *not* upgrade-compatible with GPL-3.0 code — and
the one **MIT** option (`academico`) is explicitly scoped to "small and medium
institutions". 🔴 **There is no permissively licensed, university-scale open-source
SIS.** That absence has now been tested against the correctly named axis rather
than inferred, and it is the single most important procurement fact on this page:
**a registrar-scale SIS engagement attaches to the client's existing system over
its API; it does not fork one.** Registered `573-B`.


## Tenth pass (`p572`, 2026-10-31) — 🟢 FIVE PLATFORMS ADDED, ONE OF THEM **MIT**, ALL FIVE RE-FOUND BETWEEN `83` AND `93` TIMES WITHOUT EVER BEING SHELVED

🟢 **`ls1intum/Artemis` is the headline: a full academic platform under MIT**,
from TU München, with the university named inside the grant itself. Every other
platform on this page is GPL-, AGPL-, LGPL- or ECL-licensed. 🔵 For a client who
wants to modify a platform and keep the modifications, Artemis is the only row
here that allows it.

🔴 **All five were absent from every shelf page in this KB** while this base's own
sweeps returned them `83`–`93` times each. The audit behind that number is
`572-A`, recorded in [`../repos/foundations.md`](../repos/foundations.md):
**`3,455` addresses seen across the base's history, `170` ever shelved.**

🟢 **Two platform categories this page was missing entirely are now filled:**
**lecture capture** (`opencast`, ECL-2.0) and a **true SIS** (`rosariosis`,
GPL-2.0 — enrolment, scheduling, attendance, billing, which is not what an LMS
does). 🟢 And the **ERP** the already-shelved `frappe/lms` is built on —
`frappe/erpnext`, `40.8k★` with an Education module — is now on the page beside it.

🔵 **Licence posture across this page, stated once so an engagement can read it
off:** `Artemis` **MIT** → fork freely · `opencast` **ECL-2.0**, `Sakai`
**Apache-2.0** → fork, mind the narrowed patent grant · `Odoo`/`OpenEduCat`
**LGPL-3.0** → link, don't modify · `Moodle`/`Gibbon`/`ILIAS`/`i-educar`/`ERPNext`
**GPL-2.0/3.0** → attach over API or LTI · `Open edX`/`Canvas`/`frappe-lms`
**AGPL-3.0** → §13 network source-offer obligation on any hosted deployment.

## Education ERP / Student Information Systems

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Artemis | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** (1,091 B ✅ first-hand; sidebar agrees) | 824 | EMEA | 🟢 **The most permissively licensed full academic platform in this KB, and it was absent from every shelf page while being re-found `97` times.** "Artemis - Interactive Learning with Automated Feedback": programming exercises with automatic assessment, quizzes, modelling, text and file-upload exercises, exam mode. 396 forks. 🟢 **Region is first-hand, not inferred: the grant's own copyright line reads *"Copyright (c) 2026 TUM Applied Education Technologies"*** — Technische Universität München, under `p571`'s institution-holder instrument. 🔵 **Compare the field: Moodle GPL-3.0, Open edX AGPL-3.0, Canvas AGPL-3.0, ILIAS GPL-3.0, Sakai Apache-2.0 — Artemis is MIT.** For a client that wants to ship a modified platform without publishing the modifications, this is the only row on this page that permits it outright. |
| Opencast | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (11,340 B ✅ first-hand; sidebar agrees) | 509 | EMEA | "The free and open source solution for automated video capture and distribution at scale." 260 forks. 🔵 **ECL-2.0 is the Educational Community License — an Apache-2.0 derivative, OSI-approved, whose patent grant is narrowed to the contributing institution's own claims** rather than Apache's broader grant. Permissive and buildable; the patent-clause difference is the one thing to put in front of a procurement lawyer. The lecture-capture layer nothing else on this page provides, and it was absent from every shelf while being re-found `93` times. |
| ERPNext | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (35,149 B ✅ first-hand, `develop/license.txt`) | 40,800 | APAC | "Free and Open Source Enterprise Resource Planning (ERP)." 13,400 forks — **the largest star count on this page by a factor of ten**, and it was absent from every shelf page. Ships an **Education** domain module (students, programs, enrolment, assessment, fees, instructors). India (Frappe Technologies). 🔴 Copyleft: attach over its REST API rather than fork, the same posture this KB takes to Odoo and i-educar. 🔵 **Its grant was invisible to this base's ladder until this pass: the file is lowercase `license.txt` and the default branch is `develop`.** The sibling `frappe/lms` (AGPL-3.0) was already shelved — the ERP it is built on was not. |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** (15,214 B ✅ first-hand, Version 2, `affero=0`) | 649 | Global | "RosarioSIS Student Information System for school management." 395 forks, PHP, with a GitLab mirror the README names as co-primary. 🔵 **A true SIS — enrolment, scheduling, grades, attendance, billing, discipline — which is a different product from an LMS and a category this page was thin on.** Widely deployed in Spanish- and French-speaking school systems; the project ships localisations including `es` and `fr`. 🔴 **GPL-2.0, not 3** — so it carries no patent grant and no §13, and it is *not* upgradeable-by-default. Attach, do not fork. Re-found `92` times, never shelved. |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | **GPL-3.0** (35,121 B ✅ first-hand — 🔴 **not AGPL**; sidebar agrees) | 636 | Global | "Gibbon is a flexible, open source school management platform designed to make life better for teachers, students, parents and leaders." 428 forks, PHP. 🔴 **This base's naive copyleft detector called it AGPL-3.0; the licence title line reads "GNU GENERAL PUBLIC LICENSE" and the three Affero mentions are GPL-3.0's own §13 cross-reference.** The distinction decides whether a hosted deployment owes source to its users — GPL-3.0 does not. Re-found `83` times, never shelved. |
| Odoo | [odoo/odoo](https://github.com/odoo/odoo) | **LGPL-3.0** (file, not sidebar) | 55,400 | EMEA | "Odoo. Open Source Apps To Grow Your Business." The canonical open-source ERP and the comparison point this KB is measured against. The sidebar names **no** licence; `LICENSE` on the default branch (`20.0`) states *"Odoo is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3)"*. A closed application may *link* it; modifications to Odoo itself stay open. This explains OpenEduCat's LGPL-3.0 by inheritance. Odoo SA is Belgian; the repository page does not state a location. |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3,400 | APAC | "Easy to use, 100% open source LMS." Built on the Frappe framework, so it inherits Frappe's ERP primitives. India. |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 902 | APAC | "Comprehensive Open Source ERP for Educational Institutes" — admissions, students, faculty, courses, exams, library, fees. **LGPL-3.0, not MIT/Apache**: linkable from closed applications, but modifications to it stay open. OpenEduCat's own website names Odoo as its underlying framework; the GitHub page never mentions Odoo. India. |
| i-educar | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | LATAM | *"Lançando o maior software livre de educação do Brasil!"* School management for Brazilian municipal education secretariats (*Secretarias de Educação*) and public schools. **The reference LATAM public-sector education platform** and the most important row here for a Brazilian government engagement. |
| Academico | [academico-sis/academico](https://github.com/academico-sis/academico) | **MIT** (licence file, 1,094 B) | 410 | Global | **The permissive education SIS this page spent three passes concluding did not exist.** "Laravel & Filament-based school management platform for small and medium institutions" — topic `student-information-system`, 151 forks, pushed 2026-10-30, copyright "Thomas Debay and project contributors". A client at this tier — language school, training institute, private school group — **can fork it, rebrand it and keep the derivative closed.** It is not a platform of record and should never be offered as a Moodle or OpenEduCat replacement at university scale; the 410★/151-fork ratio does say it is in real deployment rather than starred and abandoned. Region not stated; recorded Global. |
| Frappe Education | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** (resolved from `license.txt`) | 687 | APAC | "Open source education / school management system." Note it is **GPL-3.0, not AGPL-3.0** like Frappe's other projects, and not LGPL like its OpenEduCat neighbour. Copyleft either way: attach, do not fork. India. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (pinned) | 347 | North America | Web-based PHP/MySQL Student Information System. OS4ED (US). The README points to `docs/License.txt`, which is **GPL version 2, June 1991** — *not* GPL-3.0. The distinction is load-bearing: GPL-2.0 has no patent grant and is incompatible with GPL-3.0-only code. Default branch is `master`; there is no `main`. |

## Learning platforms used as the vertical system

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | The default institutional LMS worldwide; the vast plugin ecosystem is the customisation surface. Perth, Australia. |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0 + separate Enterprise Licence** | 2,400 | Global | "The Next-gen Open Source learning platform for everyone." Next.js / FastAPI / Postgres / Redis, 593 forks, ships "LearnHouse AI: The Teachers and Students copilot". **Added this pass.** The licence shape is the lesson: an AGPL core with features withheld under a commercial licence means the public repo is not the whole product — check feature parity before promising a self-hosted build. Maintainer Badr B. (`@swve`); country not stated. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | LMS built around ease of use and accessibility; notable francophone and LATAM deployments. |
| OpenOlat | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** (licence file `10,982 B`, read first-hand `p574`; `NOTICE.TXT` `14,712 B`) | 449 | EMEA | "Learning Management System OpenOlat," by **frentix GmbH, Switzerland**. A permissively licensed *institutional* LMS — rare, and one a commercial derivative could be built from. |
| Mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | 102 | **EMEA** | **The new permissive option, and the one to read carefully.** "Open-source AI-native LMS with AI Mentor & role-play. Self-hosted alternative to Moodle, Docebo, TalentLMS, Thinkific, Teachable and Open edX." TypeScript, 31 forks, pushed 2026-10-30. Ships **SCORM and xAPI**; white-label is a stated goal; topics include `corporate-training` and `compliance-training`, so the natural fit is **enterprise L&D rather than a university registrar**. Selleo's GitHub profile states **Poland**. MIT per the API. At 102★ with 105 open issues it carries adoption risk a Moodle install does not — but it is the only AI-native LMS a client can fork, rebrand and keep closed. |
| ULEARN | [safytech/ulearn](https://github.com/safytech/ulearn) | **MIT** (licence file, 1,066 B) | 701 | Global | **The largest MIT-licensed LMS located anywhere**, 299 forks. And the stack is the whole story: **Laravel 5.8 + React 16.9**, both long past end of life. Permissive and forkable in principle; in practice a fork is a framework-upgrade project before it is a product. Quote the upgrade or do not quote the platform. |
| Richie | [openfun/richie](https://github.com/openfun/richie) | **MIT** (licence file, 1,079 B) | 318 | **EMEA** | A Django **CMS for building education portals**, designed to front Open edX and Moodle course catalogues. 94 forks. **Region placed from the licence file's own copyright line — "GIP FUN MOOC"**, i.e. France Université Numérique, the same publisher as the MIT LRS `openfun/ralph`. The catalogue-and-marketing tier of an institution's estate, permissively licensed, from a European public publisher. |
| ibl.ai LMS | [iblai/lms](https://github.com/iblai/lms) | **MIT** (licence file, 1,063 B) | 208 | Global | "Skills intelligence platform — discover courses, track competencies, earn credentials, accelerate workforce development." Next.js 15 / React 19, created 2026-03-04. **The first open-source asset located for the digital-credentials and skills-pathway trend**, which had been carried for three passes on a single standards-body source. Workforce-development buyer, not a registrar. |
| TutorLoom | [pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom) | **Apache-2.0** (licence file, 11,362 B) | 54 | APAC | Self-hosted **multi-tenant** LMS: course builder, trainer and student portals, progress tracking. Django + React + Flutter, created **2026-10-07** — three weeks old. Explicitly `moodle-alternative` and `corporate-training`. One of only **two** Apache-2.0 repositories in the world under `topic:learning-management-system` above 50★. Region inferred from the publisher and **not stated on the repo**, so treat the placement as soft. Too young to carry an engagement. |
| Euron Open LMS | [euron-sde-team/euron-open-lms](https://github.com/euron-sde-team/euron-open-lms) | **MIT** (licence file, 1,132 B) | 10 | APAC | Created **2026-10-26** — five days old, and recorded as a watch item rather than an option. Course catalogue, HLS-video classroom, quizzes, reviewed assignments, **verifiable certificates**, Stripe **and Razorpay** billing with subscriptions, Terraform for AWS. **Two India signals**: the copyright holder is "ENGAGESPHERE TECHNOLOGY **PRIVATE LIMITED**" and the Razorpay integration is India-specific. 16 forks on 10★ at five days is an unusual ratio and worth re-reading next pass. |
| FreeLingo | [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0** | 217 | — | Self-hosted AI language-learning platform: local or cloud LLMs, CEFR study plans, AI tutor, voice conversation, flashcards, spaced repetition. Technically the most complete vertical language-learning stack found — and **AGPL-3.0**, so it is an adopt-as-is system, not a build-on base. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned. |

## Adjacent institutional systems

Not learning platforms, but always in the estate, and usually where an AI search
or discovery agent is actually pointed.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| DSpace | [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | The institutional repository — theses, datasets, faculty output, grey literature. **The only permissively licensed platform of record in this KB.** Java; LYRASIS (US non-profit). |
| Koha | [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | Integrated library system — catalogue, circulation, acquisitions. Contributions go through the project's **own bug tracker, not GitHub issues**. |

## Learning-analytics stack — a vertical system in its own right (new in the sixth pass)

**Every platform above is copyleft or near it, which is why this page's doctrine
is *attach, do not fork*.** The sixth pass found that the attach target with the
cleanest licence position is not an LMS at all — it is a **complete
learning-analytics stack, all MIT, all from one national public operator**, that
sits beside any of the platforms above and speaks a standard rather than touching
their code.

| Component | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| LRS (store) | [openfun/ralph](https://github.com/openfun/ralph) | **MIT** (`main/LICENSE.md`, 1,094 B) | 51 | EMEA | Learning Record Store: ingests **xAPI** statements from any LMS, tutor or agent. The system of record for learner activity. |
| Dashboards | [openfun/warren](https://github.com/openfun/warren) | **MIT** | 17 | EMEA | xAPI learning-analytics dashboards over the LRS. Pushed `2026-10-11` — the active component of the three. |
| Dashboards-as-code | [openfun/potsie](https://github.com/openfun/potsie) | **MIT** (`main/LICENSE.md`, 1,094 B) | 11 | EMEA | **Grafana** dashboard suite written in **Jsonnet**, so dashboards are generated, diffable and code-reviewed rather than clicked together. Pushed `2024-12-18` — stable, not active. |

🟢 **Why this belongs on a page about vertical systems.** All three grants were
read byte-for-byte in the sixth pass and all three name the same holder —
*"Copyright (c) 2020-present / 2021-present **France Université Numérique**"* —
the French national public operator that also publishes `richie`. That makes this
**the strongest institutionally placed EMEA row anywhere in this KB**: the region
is read off the grant, not inferred from language or timezone.

🟢 **The engagement shape.** A client on Moodle (GPL-3.0), Chamilo (GPL-3.0) or
OpenEduCat (LGPL-3.0) cannot have a closed derivative of their platform. They
*can* have a **closed, white-labelled analytics product** built on this stack,
attached over xAPI, with no platform code touched and no copyleft reaching the
deliverable. 🔵 `scorm-again` (MIT) and `ltijs` (Apache-2.0) are the other two legs
of the same doctrine; this is the one that answers *"and what do the dean and the
registrar actually look at?"*

⚠️ **Two honest caveats before it is quoted.** `potsie`'s last push is
**December 2024** — the Grafana suite is stable rather than maintained, and
Grafana itself is **AGPL-3.0**, so the *dashboards* are MIT while the *runtime
rendering them is copyleft*: ship it as a deployed service, not as a linked
component in a closed product. And at 51/17/11★ this is a small-community stack —
credible because of who publishes it, not because of its adoption numbers.

🔴 **Recorded against this KB's own error.** This stack was already in the
repository while [`../repos/trending.md`](../repos/trending.md) was still
publishing *"no open-source learning-analytics dashboard"*. The components were
never missing; the index was wrong. See `568-A` in
[`../intel/open-gaps.md`](../intel/open-gaps.md).

## Self-hosted measurement-first learning platform (new in the seventh pass)

🟢 **A platform class this page has never carried: one whose selling point is
that it *audits whether learning happened*, not that it delivers content.**
Found at `stars:<50` on the band `568-C` named — **1★, 1,313 commits, 4 authors**
since `2026-08-31`, counted with `git rev-list`.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| AI Learning OS (砚席) | [swsgbl/ai-learning-os](https://github.com/swsgbl/ai-learning-os) | ⚠️ **SPLIT — MIT root (`main/LICENSE`, 1,084 B) but `services/api/` carries AGPL-3.0 combination obligations.** See the carve-out below; **do not read this row as "MIT"** | 1 | **APAC** (by artefact, not by grant — see note) | Self-hosted, **server-authoritative** learning platform. Server owns timing, scoring and idempotent submission; **item projections exclude answers** (an "answer-isolation invariant"). An 11-stage learning-sprint state machine runs *contract → **equivalent pre/post test** → concept map → plan → core study → targeted practice → **transfer check** → post-test → report → spaced re-test*. Six-state mastery rule chain (3 independent pairs + 2 contextual + a delay/transfer pair) over **FSRS** scheduling. **Local ASR/TTS — the README states voice audio never leaves the machine.** BYOK multi-vendor LLM keystore (server-side encryption, last-4 display only, three-layer SSRF defence). Clients: Web PWA, Android, **HarmonyOS**. 🟢 **The part that matters for this KB:** a *learning-effect audit pipeline* with **CTT item analysis, mastery-simulation validity (publisher reports AUC 0.913), metacognitive calibration (gamma) and pre/post effect sizes — gated in CI.** |

### ⚠️ The licence carve-out, read from the publisher's own `NOTICE.md`

🔴 **A LICENSE-file read — this base's primary instrument — returns `MIT` for this
repository and that answer is dangerously incomplete.** `main/NOTICE.md` states
the split itself:

| scope | licence |
| --- | --- |
| `apps/android/`, `apps/harmony/`, `apps/web/`, `services/console/`, docs | 🟢 **MIT** |
| 🔴 **`services/api/`** | 🔴 **AGPL-3.0 combination obligation** |

🔴 **The mechanism is a single dependency, not a publisher's choice.**
`services/api` links **PyMuPDF (AGPL-3.0)** in-process to parse PDF textbooks.
`NOTICE.md` spells out AGPL-3.0 §13: *offer the service over a network and you
must give that service's users the complete corresponding source of your
deployment, modifications included.* Private local use does not trigger it.

🔴 **For Globant specifically this is a prohibition on the default path, not a
threshold.** A studio that hosts and operates a client's deployment of
`services/api` owes that deployment's source to its users — the same class of
finding as `Arize-ai/phoenix`'s Elastic License (`p568`), reached by a completely
different route.

🟢 **And the remedy is named, costed and small**, which is why this row is shelved
rather than rejected. `NOTICE.md` itself gives two exits: buy a commercial
PyMuPDF licence from Artifex, or **replace the parser**. The rest of
`services/api` is MIT-compatible by its own dependency table (FastAPI, SQLAlchemy,
Alembic, `py-fsrs`, `onnxruntime` all MIT; `rapidocr-onnxruntime` and CosyVoice
Apache-2.0; `httpx` BSD-3). **Swapping one PDF parser for a permissive one
(`pypdf`, BSD-3; `pdfplumber`, MIT) removes the AGPL obligation from the whole
platform.** That is a scoped engineering task, and it is the first thing to quote
on an engagement that wants this stack. Wired as `P-572-B`.

🔵 **On the region field, stated precisely.** The grant names *"AI Learning OS
contributors"* — **not an institution**, so this base's licence-holder instrument
(`p568`) does **not** place it. It is recorded **APAC on artefact evidence
instead**: a HarmonyOS / 深开鸿 client target, a `ChinaTextbook` catalogue
integration, and Chinese-language documentation throughout. 🔴 **Those are two
different grades of evidence and this page does not pretend otherwise** — see
`569-E`.

## Ninth pass (`p571`, 2026-10-31) — 🔴 two platform axes swept, no new platform; and `topic:mooc` is a large, correctly-named, nearly empty channel

🔴 **No row added.** Two axes never swept *for platforms* were opened —
[`topic:mooc`](https://github.com/topics/mooc) (**661** repositories) and
[`topic:language-learning`](https://github.com/topics/language-learning)
(**4.8k**) — and **every platform they returned is already on this page or on this
base**: `gazpachu/hypatia`, `INRIA/scikit-learn-mooc`,
`xiaochong0302/course-tencent-cloud`, `designfuchen/word-atlas`,
`mengxi-ream/read-frog`, `echo-loop/Echo-Loop`, `umlx5h/LLPlayer`.

🟢 **One grant newly read this pass:**
[`umlx5h/LLPlayer`](https://github.com/umlx5h/LLPlayer) is **GPL-3.0** at
**4,400★** — the media player for language learners carried on this page without a
licence column. ⛔ Copyleft; attach, do not fork.

### 🔵 The structural finding: a 661-repository axis named after a delivery model contains almost no delivery software

🔴 **Exactly two of `topic:mooc`'s top twenty are platforms, and both are
disqualified** — `gazpachu/hypatia` (**GPL-2.0**, 651★, README states the project
is *"currently in hibernation"*) and `xiaochong0302/course-tencent-cloud`
(**GPL-2.0**, 1,200★, already shelved). The other eighteen are:

- **Course materials and solution repositories** — `fastai/course-v3`,
  `INRIA/scikit-learn-mooc` (⚠️ **CC-BY-4.0**, a *content* licence on a code repo;
  EMEA/INRIA, France), Coursera assignment answers, algorithm-course sample code.
- 🔴 **Downloaders and attendance-automation scrapers** — `Foair/course-crawler`,
  `MoocDownloader/MoocDownloader`, and `cxOrz/chaoxing-signin`, which automates
  check-in on 学习通. **Tools built to extract from or game MOOC platforms, not to
  run them.**

🔵 **So an axis can be large, precisely named for the thing you want, and still
hold nothing shelvable — and that is a different result from an unswept axis.** 🟢
It is now measured rather than assumed, which is what stops a later pass buying it
again. 🔴 Note this is *not* the low-precision failure `P909` describes: `mooc`
is a single word but has **no meaning outside education**, so by `P923`'s
selection rule it should have been a good channel. **`P923` predicts precision,
not shelvability** — the rows are on-topic and still unusable.

🔴 **`topic:language-learning` (4.8k) yields no platform either, and its leaders
are consumer apps under copyleft** — `read-frog` **GPL-3.0** (10,200★),
`Echo-Loop` **AGPL-3.0** (4,600★), `LLPlayer` **GPL-3.0** (4,400★). ⛔ The AGPL row
is the one to flag to a studio that *hosts* client solutions: AGPL reaches a
hosted service, so it is a **prohibition, not a threshold**. 🟢 `word-atlas`
(3,500★) from that axis is **already on this page**, which serves as a negative
control confirming the sweep reached the right population.

## Eighth pass (`p570`, 2026-10-31) — no new platform qualified, and the content-grant lesson now belongs on this page

🔴 **Measured null, stated rather than left silent.** Four GitHub topic axes
never swept in 569 passes were queried this pass — `topic:rubric` (187 results),
`topic:spaced-repetition` (3.2k), `topic:academic-integrity` (121),
`topic:automated-grading` (49). 🔴 **None returned a vertical education platform.**
The eight new addresses they produced are **evaluation tooling and learning
apps**, shelved in [`../repos/foundations.md`](../repos/foundations.md). The
platform tier of this industry is not discoverable on capability axes — it is
found, as this page's own history shows, on `topic:lms`, `topic:sis` and
`topic:student-information-system` with a licence filter.

### 🔴 The finding this page must absorb: a content carve-out can live INSIDE the MIT file

🟢 `568-D` established the convention this page already applies — a single
`Licence` column plus an inline ⚠️ marker naming the carve-out. 🔴 **`p570` found
the sixth instance and a mechanism that defeats every check this base runs**, and
although the repository itself is a learning app rather than a platform, **the
mechanism is most dangerous here**, because a vertical education platform *ships
curriculum content* by definition.

[`designfuchen/word-atlas`](https://github.com/designfuchen/word-atlas)
(**3,500★ in six days**) carries `main/LICENSE` at **1,299 B** — standard MIT is
~1,068 — and the surplus is a `Scope:` clause in the MIT body itself:

> *"This license covers project code, original interface artwork, and technical
> documentation. Vocabulary learning content, third-party media, and generated
> recordings are governed separately by `CONTENT_LICENSE.md`."*

| scope | licence |
| --- | --- |
| code + UI design | **MIT** |
| Fraunces typeface | **SIL OFL 1.1** |
| wordlist (`data/`), illustrations, audio recordings | **CC BY 4.0** — *"to the extent of the rights the maintainers can grant"* |

🔴 **Three tiers, and the attribution-encumbered tier is the entire product
value.** 🔴 **Plus a disclosure that decides procurement:** the content was
produced by AI models — LLM text, image-model illustrations, **ElevenLabs
synthetic audio** — auto-validated and **not reviewed entry by entry**, supplied
as-is with **no accuracy warranty**, and the maintainers **hedge whether they
hold the rights they are granting.**

🔵 **The checklist item for every platform on this page, stated as a rule because
four separate mechanisms have now been catalogued:** a platform's grant must be
read for **four** carve-out shapes, and only the first is visible to a licence
API —

1. a **separate content licence** for datasets or curricula (`knowledge-graph`,
   `open-question-bank`);
2. a **per-directory** grant (`human-skill-tree`'s dual-licensed `skills/`);
3. an **obligation inherited from an in-process dependency**
   (`ai-learning-os`, AGPL-3.0 via PyMuPDF — *nobody chose it*);
4. 🆕 **a scope clause inside the permissive file's own body** (`word-atlas`) —
   which a `NOTICE` read, a per-directory check and a dependency audit **all
   miss**, because the file that limits the grant *is* the grant.

🔴 **The operational consequence for a client deliverable: if a platform ships
content, "MIT" on the repository is a statement about the code and about nothing
else, until the content tier has been read by name.**

## How to read this page

**The operations layer is copyleft almost without exception — but the exception
list has grown from three to nine, and that is this pass's correction.**
Permissive rows above: **Academico** (MIT, SIS), **ULEARN** (MIT, stale stack),
**Richie** (MIT, EMEA portal CMS), **ibl.ai LMS** (MIT, credentials),
**TutorLoom** (Apache-2.0, 3 weeks old), **Euron Open LMS** (MIT, 5 days old),
**OpenOlat** (Apache-2.0), **Mentingo** (MIT) and **DSpace** (BSD-3-Clause). Two
more permit linking from closed code (Odoo, OpenEduCat, LGPL-3.0). Everything
else — and every platform of record — is GPL or AGPL. Note what the permissive
list is made of: **one row above 700★, three created in the last eight weeks, and
one on an end-of-life framework.** Permissive and *ready* are different claims. The AI-on-top strategy is therefore
not a matter of taste — it is forced by licensing:

1. **Do not fork the platform of record.** Under GPL/AGPL the derivative must be
   released; under AGPL that triggers on network use, which is how these systems
   are always deployed.
2. **Attach across a standard boundary instead** — LTI 1.3 via `ltijs`, LMS data
   via MCP, telemetry via xAPI into an LRS. All permissive. See
   [`../repos/foundations.md`](../repos/foundations.md).
3. **Where a permissive substrate is genuinely required**, the choice is now
   buyer-shaped rather than scarce: **OpenOlat** (Apache-2.0, 449★) for an
   institution, **Academico** (MIT, 410★) for a small or medium school,
   training institute or language school needing an **SIS**, **Mentingo** (MIT,
   102★) for AI-native corporate L&D, **Richie** (MIT, 318★) for the catalogue
   and portal tier, **ibl.ai LMS** (MIT, 208★) where **credentials and
   competencies** are the point, and **DSpace** (BSD-3-Clause) for the
   institutional repository. None of them is a platform of record, and saying so
   is part of the recommendation.
4. **Check for a withheld-features licence.** `learnhouse` is AGPL **plus** an
   Enterprise Licence. A dual-licence core is the one shape that looks open in a
   licence column and is not open in a feature matrix.
5. **Deliver courseware over SCORM, not only over LTI.** `jcputney/scorm-again`
   (MIT, 362★ — see [`../repos/foundations.md`](../repos/foundations.md)) is a
   maintained SCORM 1.2 / 2004 runtime. Every platform on this page ingests
   SCORM; it is what procurement asks for by name. Three passes of this KB built
   the attach doctrine without it.

## Declared gaps

- **No MIT- or Apache-licensed education ERP/CRM comparison exists.** The
  prescribed search `open source platform education ERP CRM MIT Apache` returned,
  for the **fourth** pass running, OpenEduCat's own marketing glossary (ten
  localised copies of two glossary pages) plus general-purpose CRMs — none
  education-specific. The *commentary* gap is now a settled property of the
  channel.
- **"There is no permissively licensed education ERP" was stated too broadly
  last pass, and this pass corrects it.** The finding holds for **ERP at
  platform-of-record scale**: that category is LGPL (OpenEduCat, Odoo) or
  GPL/AGPL (Frappe ×2, i-educar, openSIS) without exception, and a client wanting
  a proprietary derivative at that scale still builds on a *general* permissive
  ERP framework. It does **not** hold one tier down: `academico-sis/academico`
  (**MIT**, 410★, 151 forks, `student-information-system`) is a permissively
  licensed, actively maintained education SIS for small and medium institutions.
  **The correction matters because of how the earlier version was phrased** — as
  a conclusion "firm enough to state as a finding rather than a gap". It was
  firm about the wrong scope. The search that found the counter-example was an
  index query (`topic:lms license:mit stars:>80`), not a web search; the web
  channel returned the same vendor glossary for the fourth time.
- **The ERP/CRM commentary gap reproduced for a fifth pass, with the same
  artefact.** `open source platform education LMS SIS MIT Apache` returned
  **nine of ten results from `openeducat.org`** — the same vendor comparison and
  glossary pages in ten localisations that passes two through four recorded. At
  five consecutive passes this is no longer worth re-running: **the web channel
  has one answer for this query and it is an advertisement.** Index queries
  (`topic:lms license:mit`) are the only channel that has ever returned a
  counter-example here.
- **One genuinely useful thing the web channel did surface: Sakai.**
  [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) is **Apache-2.0**,
  stewarded by the **Apereo Foundation**, and originated in a 2004 consortium of
  Michigan, Indiana, MIT and Stanford. It is already recorded in
  [`../repos/foundations.md`](../repos/foundations.md) and is **cross-referenced
  here deliberately**, because it is the one *institutional LMS of record* with a
  permissive licence — and this page's central doctrine ("do not fork the platform
  of record") has a real exception in it that a reader of this page alone would
  miss. The honest qualifier from the same sources: Sakai has a **smaller
  community and slower release cadence** than Moodle, which is why it is not the
  default recommendation despite the better licence.
- **Two licence facts worth pinning, since both circulate wrongly.** Open edX is
  **AGPL-3.0**, not Apache — the MIT-and-Harvard origin story leads people to
  assume otherwise, and the licence is the opposite of what that history
  suggests. Canvas publishes its core under **AGPL-3.0**. Both are attach-only.
  `dotLRN`, which appears in older academic literature as an MIT-origin LMS, was
  **not verified this pass** and should not be offered to anyone.
- **No LATAM education ERP outside Brazil** surfaced again this pass. `i-educar`
  remains the single LATAM row and it is Brazil-specific.
- **Nextcloud (files) and Jitsi (conferencing) are still unverified.** Real
  systems, commonly paired with the above, outside what has been checked.
- **Four of the nine permissive rows are too young or too stale to recommend,
  and the page should not be read as nine options.** `TutorLoom` is three weeks
  old, `euron-open-lms` five days, `ibl.ai LMS` eight months, and `ULEARN` runs
  on two end-of-life frameworks. The genuinely usable permissive set today is
  **OpenOlat, Academico, Richie, Mentingo and DSpace** — and only DSpace is a
  category leader.
- 🔴 **No vertical platform was discoverable on a capability axis — a null worth
  recording so it is not re-run.** Four never-swept axes (`topic:rubric`,
  `topic:spaced-repetition`, `topic:academic-integrity`,
  `topic:automated-grading`; denominators `187 / 3.2k / 121 / 49`) returned
  **zero** platforms. 🔵 **This is the mirror image of the fifth pass's
  capability-sweep finding:** sweeping by capability finds the *horizontal*
  supply and the *tooling*; the platform tier only answers to platform topics
  with a licence filter. **Both axes are required, and they return different
  layers** — do not substitute one for the other.
- 🔴 **A fourth carve-out mechanism now exists and the page's reading rule is
  updated above.** `word-atlas`'s grant is limited by a `Scope:` clause **inside
  the MIT file**, which no instrument this base runs would catch — not the
  licence API, not a `NOTICE` read, not a per-directory check, not a dependency
  audit. 🔵 **For this page the exposure is structural rather than incidental:
  every platform here that ships curriculum, item banks or media has the same
  surface**, and only `knowledge-graph`, `evaluators`, `open-question-bank` and
  `ai-learning-os` have actually been read for it. **The remaining rows are
  unread on their content tier**, and that is a stated gap rather than a clean
  bill.
- **Mentingo's maturity is unverified beyond its metadata.** MIT, Poland, xAPI
  and SCORM are confirmed from the API and profile. Whether it can actually carry
  an institutional deployment — SSO, accessibility conformance, data residency,
  migration from Moodle — was **not** tested and should not be implied to a
  client from its presence on this page. 105 open issues on 31 forks is the one
  number that argues for caution.
