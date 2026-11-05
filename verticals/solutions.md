---
industry: education
region: Global
updated: 2026-11-05
---

# 🏭 Vertical platforms — Education

> Real, running systems that a client may already have, or that can be stood up and then extended with an agentic layer.
> Model: start from something that already works, add agents on top. Verified 2026-11-04 via `git ls-remote --symref` + licence payload read.

## Platforms — 31 verified rows

| Platform | Repo | Licence | Branch | Stack | Use case |
|---|---|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `main` | PHP + MySQL/PostgreSQL | The universal LMS: K-12, higher ed, corporate. Built-in AI subsystem since 4.5. Dominant in LATAM and much of EMEA. |
| **Open edX** | [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | `master` | Python/Django + React | MOOC scale, corporate academies, national platforms. Extend via XBlock. |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (1,097 B) | **`develop`** | Python/Django + Vue | 🟢 **The permissive production learning platform this KB has repeatedly declared does not exist.** "The offline-first platform for teaching and learning with technology without requiring the Internet." **1.2k ★ / 1.0k forks.** Learning Equality. Content delivery, learner progress and coach tooling that run with **no connectivity at all** — the decisive capability in Sub-Saharan Africa, rural South Asia and the Pacific. ⚠️ Default branch is `develop`; release lines are `release-v0.19.x` / `release-v0.20.x`. |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `master` | PHP | Lightweight LMS, strong public-sector adoption in Spanish-speaking LATAM. |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | `master` | Java/Spring | Institutional HE LMS, mostly North American universities. |
| **OpenOlat** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** (10,982 B) | `master` | Java / Spring / Hibernate 7.4 | 🟢 **The permissive institutional LMS this KB has stated in three files does not exist.** Full institutional course management — courses, enrolment, assessment, QTI tests, portfolio, curriculum management — under **Apache-2.0**, so a closed proprietary derivative is permitted. **449 ★ / 167 forks / 32,210 commits**; live release branches `OpenOLAT_18.0` → `OpenOLAT_21.1`, latest tag `OpenOLAT_21.1.2`. Forked from the University of Zurich's OLAT 7.1 in 2011 by frentix GmbH (Zurich); deep adoption in German-speaking EMEA higher education. 🟢 **Ships an LLM subsystem in-tree**: `langchain4j` 1.23.0 (canonical Apache-2.0, 11,357 B) with `langchain4j-open-ai`, `langchain4j-anthropic` and `langchain4j-embeddings`, plus Apache Lucene for search. ⚠ The only copyleft item in 270 declared dependencies is the **optional** MySQL Connector/J (GPL-2.0 + Universal FOSS Exception) — see the dependency note below. |
| **ILIAS** | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | `release_11` | PHP | Robust LMS with deep adoption in German-speaking EMEA (DE/AT/CH), incl. public sector and military training. |
| **Gibbon** | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | `v31.0.00` | PHP + MySQL | School management / SIS: enrolment, timetabling, academic records. Complements Moodle rather than competing. |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** (15,214 B) | **`mobile`** | PHP + PostgreSQL | Student Information System: scheduling, grades, attendance, billing. **651 ★ / 397 forks.** Licence version read from the payload's own version line at p651, no longer inferred from size. ⚠️ The default branch is `mobile`, among 44 branches that are otherwise version numbers — a default `git clone` does not give you the release line. A GitLab mirror is the project's other home. |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | `develop` | Python (Frappe) | Modern course platform on the Frappe/ERPNext stack — the realistic path when a client already runs ERPNext. |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) | **MIT** | `master` | Django + React | Course-catalogue / MOOC portal CMS. The only permissive platform-level row here. |
| **Veo LMS** | [veolms/veolms](https://github.com/veolms/veolms) | **AGPL-3.0** | `main` | — | Newer actively-developed OSS LMS. Listed for awareness; AGPL-3.0 rules out a proprietary derivative. |
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (8,241 B) | **`19.0`** | Python / Odoo | **Education ERP** — admissions, academics, finance, HR — on the Odoo stack. **905 ★ / 787 forks.** The "Odoo-for-education" slot, and the easiest copyleft position on this shelf: LGPL permits linking from separately-licensed code provided the LGPL portion stays replaceable. ⚠️ Default branch is a bare version; `20.0` exists. ⚠️ `LICENSE` delegates copyright to a `COPYRIGHT` file that returns 404. |
| **openSIS** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (at `docs/License.txt`) | `master` | PHP + MySQL | Student Information System, single or multi-institution in one installation. **349 ★ / 289 forks.** ⚠️ **No grant file at any of fifteen root filenames and no licence named on the repository page** — the terms exist only at `docs/License.txt`, reachable via a README link. Every automated root-filename probe calls this repository licence-nil; it is not. |
| **GegoK12** | [Gego-K12/gegok12](https://github.com/Gego-K12/gegok12) | **MIT** (1,150 B) | `main` | PHP / Laravel | School-management ERP, API-first, mobile-app ready. **55 ★ / 107 forks** — forks at 2× stars, the signature of software people deploy rather than follow. Low absolute adoption, but it is the **only education-administration row here that permits a closed derivative**. |
| **Oppia** | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** (11,357 B) | **`develop`** | Python / Angular / Google App Engine | 🟢 **New at p655, and the highest-adoption permissive platform on this shelf: 6,974 ★.** Structured-lesson delivery built on *explorations* — branching lessons whose feedback responds to the **specific misconception** a learner's answer reveals, rather than marking it wrong. Built for learners with low prior attainment and low bandwidth; deployed via NGO and ministry partnerships in India, Sub-Saharan Africa and Brazil, with an Android client. **Apache-2.0 permits a closed, client-branded derivative.** ⚠️ **Default branch is `develop`.** Where it fits: the pedagogy slot Moodle does not fill — Moodle hosts content, Oppia *is* the instructional design. |
| **Mentingo** | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** (1,062 B) | `main` | NestJS 10 / TypeScript / Drizzle / PostgreSQL 16 + pgvector / Redis / BullMQ; Remix + React front end | 🟢 **New at p655, and the only row on this shelf where multi-tenancy, white-labelling *and* the agent are all core rather than plugins.** Corporate L&D, onboarding and compliance training, with a **voice-and-chat AI mentor running scored role-play** instead of slide-watching, plus a scenario-based assessment engine, certificate recertification with expiry, SCORM export and six shipped UI languages. AI layer read from the manifest this pass: Vercel AI SDK (`ai` 7.0.148, `@ai-sdk/openai` 4.0.8, `@ai-sdk/workflow` 2.0.80), `langchain` 0.3.34, pgvector retrieval, LiveKit voice, Langfuse tracing. 1,397 commits / 32 forks. Selleo (Poland) — **EMEA**. **106 ★ is low and this cell says so**; it is here because MIT + multi-tenant + white-label + agent-in-core is the exact shape of a Globant-built client-branded deliverable, and nothing else on this page is that shape. |
| **JupyterHub** | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** (1,474 B) | `main` | Python; Docker / Kubernetes spawners | 🟢 **New at p655.** Not an LMS and should not be sold as one — it is the **delivery substrate for technical curriculum**: one isolated, authenticated, resource-limited environment per learner, with LTI auth so an existing LMS stays the front door. **8,362 ★**, the highest-adoption permissive platform-class row this programme has filed. Pairs with `jupyter/nbgrader` (BSD-3-Clause, 1,370 ★) for assign → collect → autograde → feedback. For any CS, data-science, analytics or bootcamp engagement this is the base, and the whole chain is BSD-3-Clause. See `compose/patterns.md` **P15**. |
| **H5P** | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** (35,146 B) | `master` | PHP | 🟢 **New at p656.** The interactive-content standard of the sector: ~50 content types (interactive video, branching scenarios, drag-and-drop, quizzes) that embed natively in Moodle, Canvas, Brightspace, Drupal and WordPress. **154 ★**, pushed 2026-11-04. If a client authors interactive learning content, this is very likely what they author it in. 🔴 **GPL-3.0 — integrate, do not fork.** |
| **H5P for Node** | [Lumieducation/H5P-Nodejs-library](https://github.com/Lumieducation/H5P-Nodejs-library) | 🔴 **GPL-3.0** (35,146 B) | `master` | TypeScript | 🟢 **New at p656.** The maintained server-side H5P implementation for JavaScript stacks — player, editor, content storage, and the route to running H5P outside PHP. **207 ★**, pushed 2026-10-29. The practical choice when the agent layer is Node and the content must stay H5P. |
| **Lumi** | [Lumieducation/Lumi](https://github.com/Lumieducation/Lumi) | 🔴 **no grant file** | `master` | Electron / JavaScript | 🟢 **New at p656.** H5P as a desktop application — authors interactive content offline, exports to any H5P host. **196 ★**, pushed 2026-10-28. 🔴 **`LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`, `LICENCE` and `license.txt` all 404 on the real default branch.** The upstream libraries are GPL-3.0, so assume GPL and do not ship a derivative on the strength of an unstated grant. A sixth instance of this KB's grant-defect classes. |
| **Adapt Framework** | [adaptlearning/adapt_framework](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** (35,129 B) | `master` | JavaScript / Backbone | 🟢 **New at p656.** Responsive HTML5 course authoring that outputs **SCORM and xAPI** packages — the highest-adoption open source authoring tool on this shelf at **632 ★**, pushed 2026-11-02. Pairs with `jcputney/scorm-again` (MIT) on the player side and `yetanalytics/lrsql` (Apache-2.0) on the telemetry side: **the authoring tool is copyleft, the pipes around it are not.** |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | 🔴 **GPL-3.0** (35,147 B) | `main` | PHP / Symfony + JavaScript | 🟢 **New at p656 — and the only accessibility row this KB has ever shelved.** Scans Canvas course content for WCAG defects, explains each one and fixes many in place. University of Central Florida → **North America**. **117 ★**, 78 forks, pushed 2026-11-04. 🔴 **This is the installed-base answer to the April 2026 ADA deadline for large US public institutions, and it is GPL-3.0** — a client-operated deployment, never a Globant product. See `intel/market.md` → North America. |
| **TAO** | [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | 🔴 **GPL-2.0** (18,025 B) | **`develop`** | PHP | 🟢 **New at p656.** Standards-based (**QTI**) computer-based assessment and delivery — the platform behind national and international large-scale testing programmes, including PISA-adjacent work. **64 ★**, pushed 2026-11-04. Low stars, heavyweight institutional adoption: the signature of software that is deployed under contract rather than starred. ⚠️ **GPL-2.0-only — do not combine in one work with GPL-3.0 code** (see the licence table below). |
| **Numbas** | [numbas/Numbas](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** (11,357 B) | `master` | JavaScript | 🟢 **New at p656, and the permissive exception on the assessment half of this shelf.** Browser-based e-assessment with randomised questions, algebraic answer marking and partial credit; packages to SCORM. **216 ★**, 129 forks, pushed 2026-10-28. **Newcastle University runs and maintains it for its own teaching** — production university software. Also on `repos/foundations.md`. **EMEA** provenance. |
| **Learning Locker** | [LearningLocker/learninglocker](https://github.com/LearningLocker/learninglocker) | 🔴 **GPL-3.0** (35,141 B) | `master` | JavaScript / Node | 🟢 **New at p656 — listed as a warning, not a recommendation.** The LRS that defined the category and the one a client is most likely to already be running. **584 ★** and 🔴 **dormant since 2024-05-30, `archived: false`** so GitHub's staleness signal never fires. Copyleft *and* unmaintained. **Migrate to `yetanalytics/lrsql` (Apache-2.0, live) rather than extending this.** |
| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | 🟢 **MIT** (1,091 B) | 🔴 **`develop`** | Java / Spring + TypeScript | 🟢 **New at p657 — and it is the most capable permissive platform on this shelf, which was not true yesterday.** Institution-scale interactive learning with **individual feedback**: programming, text, modeling, quiz and file-upload exercises; competencies, learning paths and analytics (**Atlas**); institutions self-host. **826 ★ / 395 forks, pushed 2026-11-05, tag `10.3.1`.** Built and operated by **TUM** for its own teaching. 🟢 **AI is in-tree and configuration-gated — `Iris` (LLM tutor), `Athena` (feedback suggestion), `Hyperion` (AI exercise authoring on Spring AI)** — so unlike every other platform row here, the agent layer is not something Globant must add. ⚠️ Default branch `develop`. |
| **Autolab** | [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** (11,324 B) | `master` | Ruby / Rails | 🟢 **New at p657.** Course management built around **auto-graded programming assignments**, from **Carnegie Mellon**. 808 ★ / 234 forks, pushed 2026-11-03. Pair with `autolab/Tango` (Apache-2.0), the standalone REST service that executes untrusted student code in isolation — usable on its own with any stack. |
| **Submitty** | [Submitty/Submitty](https://github.com/Submitty/Submitty) | 🟢 **BSD-3-Clause** (1,542 B) | `main` | PHP | 🟢 **New at p657.** Submission, automated grading **and TA/manual grading** from **Rensselaer Polytechnic Institute**. **805 ★ / 1,119 forks** — more forks than stars, the Moodle signature of software institutions copy rather than watch. Pushed 2026-11-05, tag `v26.10.04`. 🔵 **Its first-class manual-grading workflow is the human decision boundary that DC OSSE and NY A 9190 require**, rather than a feature to retrofit. |
| **INGInious** | [INGInious/INGInious](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** (34,764 B) | `main` | Python | 🟢 **New at p657, listed as a boundary.** Secure, automated exercise assessment running the institution's own tests, from UCLouvain; live (pushed 2026-11-04), 243 ★. 🔴 **Network copyleft — deploy unmodified behind its own boundary, never fork into a deliverable.** 🔵 The GitHub API reports it `NOASSERTION`; the payload is unambiguous Affero. |
| **CourseLit** | [codelitdev/courselit](https://github.com/codelitdev/courselit) | 🔴 **AGPL-3.0** (34,143 B) | `main` | TypeScript / Next.js | 🟢 **New at p657, listed as a warning.** Create and sell courses and digital downloads on a branded site — the highest-adoption platform read this pass at **1,295 ★**, pushed 2026-11-03, and **Affero**, so a white-label client product is exactly what it forbids. If a client names it, the answer is `Mentingo` (MIT) or `Artemis` (MIT). |

### Licence payloads read this pass

| Repo | Grant file | Bytes | Family |
|---|---|---|---|
| moodle/moodle | `COPYING.txt` | 35,147 | GNU GPL v3 |
| openedx/edx-platform | `LICENSE` | 35,136 | GNU Affero GPL v3 |
| chamilo/chamilo-lms | `LICENSE` | 35,147 | GNU GPL v3 |
| sakaiproject/sakai | `LICENSE` | 11,120 | Educational Community License v2.0 |
| OpenOLAT/OpenOLAT | `LICENSE` | **10,982** | Apache-2.0 — **all nine substantive sections present and unmodified** (copyright grant, patent grant, redistribution, trademarks, warranty disclaimer, liability limitation, accepting warranty). Canonical **−375 B** and fully explained: the `APPENDIX: How to apply the Apache License to your work` — boilerplate *instructions*, not terms — is removed and replaced with two provenance statements. 🟢 Those statements are also this row's **region channel**: the payload itself names *"the OLAT Zentrum at the University of Zurich"* and *"initiated by frentix GmbH"*, which places the row in EMEA on documentary evidence rather than inference. |
| ILIAS-eLearning/ILIAS | `LICENSE` | 35,147 | GNU GPL v3 |
| GibbonEdu/core | `LICENSE` | 35,121 | GNU GPL v3 |
| francoisjacquet/rosariosis | `LICENSE` | 15,214 | GNU GPL **v2** — read from the payload's `Version 2, June 1991` line, not inferred |
| frappe/lms | `license.txt` | 33,893 | GNU Affero GPL v3 |
| openfun/richie | `LICENSE` | 1,079 | MIT |
| veolms/veolms | `LICENSE` | 34,523 | GNU Affero GPL v3 |
| openeducat/openeducat_erp | `LICENSE` | 8,241 | GNU LGPL v3 |
| OS4ED/openSIS-Classic | **`docs/License.txt`** | — | GNU GPL v2 — **no root grant file exists** |
| Gego-K12/gegok12 | `LICENSE` | 1,150 | MIT |
| learningequality/kolibri | `LICENSE` | 1,097 | MIT — holder line `Copyright (c) 2021 Learning Equality and other contributors`; no country stated, so the row is left unplaced |
| h5p/h5p-php-library | `LICENSE.txt` | 35,146 | GNU GPL v3 |
| Lumieducation/H5P-Nodejs-library | `LICENSE` | 35,146 | GNU GPL v3 |
| 🔴 Lumieducation/Lumi | — | — | **No grant file.** Six root filenames probed on `master` (`LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`, `LICENCE`, `license.txt`) — all 404. Upstream H5P libraries are GPL-3.0; assume GPL |
| adaptlearning/adapt_framework | `LICENSE` | 35,129 | GNU GPL v3 |
| ucfopen/UDOIT | `LICENSE` | 35,147 | GNU GPL v3 |
| oat-sa/tao-core | `LICENSE` | 18,025 | GNU GPL **v2** — version read from the payload's own header, on default branch `develop` |
| numbas/Numbas | `LICENSE` | **11,357** | Apache-2.0 — byte-exact canonical |
| LearningLocker/learninglocker | `LICENSE` | 35,141 | GNU GPL v3 |

## 🟢 Repaired — the ERP slot is occupied after all

| Row | Previously published as | Status 2026-11-04 (p651) |
|---|---|---|
| `OpenEduCat-Inc/OpenEduCat` → **`openeducat/openeducat_erp`** | "Education ERP, LGPL-3.0, 3M+ users / 100+ countries, Odoo-based" | The old address is genuinely **404** and three candidate renames also fail — but a **fourth** address, not among those tried, resolves with **905 ★ / 787 forks** and an 8,241 B LGPL-3.0 payload on default branch `19.0`. Filed above. |

**Consequence, revised:** the previous pass's statement that "this KB no longer holds a verified open source education ERP" is **withdrawn**. It does, at adoption, under LGPL-3.0 — which is a better licensing position for a client engagement than `frappe/lms` (AGPL-3.0), the substitute that was recommended in its place.

🔵 **What this base should take from it:** "three plausible renames also 404" was treated as sufficient evidence that a project was gone. A rename probe only searches the space a reader imagines. The live address came back from a single search on the project's own name. Declaring a project dead needs a name search, not just an address walk.

## 🔴 The licensing reality of this shelf — read before scoping

**Of twenty-six platform rows: fifteen are copyleft, nine are permissive, one is weak copyleft (OpenEduCat, LGPL-3.0) and one ships no grant file at all (Lumi).** The permissive nine are **Numbas** (Apache-2.0), **OpenOlat** (Apache-2.0), **Oppia** (Apache-2.0), **JupyterHub** (BSD-3-Clause), **Kolibri** (MIT), **Richie** (MIT), **GegoK12** (MIT), **Mentingo** (MIT) and **Sakai** (ECL-2.0, Apache-derived).

🔴 **Correction filed at p656: the sentence above previously read "Ten of fifteen platform rows are copyleft. Five are permissive" — a count that went stale at p655**, when Oppia, Mentingo and JupyterHub were added to the table and the summary beneath it was not updated. Recounted from the licence cells on 2026-11-04. 🔵 **The direction of the error is worth noting: the shelf was *more* permissive than its own summary claimed, so this page was under-selling the buildable surface rather than over-selling it** — the failure mode a reader is least likely to catch, because an under-claim never contradicts the table.

🔴 **The headline claim on this page falls a second time, and this time it falls completely.** p651 corrected *"there is no permissively-licensed, production-grade open source LMS"* to the narrower *"there is no permissive platform of the **Moodle / Open edX class**"* — institutional course management, as against Kolibri's offline-first delivery. **That narrower claim is also wrong, and is withdrawn at p653.** `OpenOLAT/OpenOLAT` is **Apache-2.0** (10,982 B payload read from bytes on 2026-11-04; all nine substantive sections present), **449 ★ / 167 forks / 32,210 commits**, with live release branches from `OpenOLAT_18.0` to `OpenOLAT_21.1` — and it is squarely in the institutional class: courses, enrolment, assessment and QTI testing, portfolio, curriculum management, the LMS of record in much of German-speaking European higher education, descended from the University of Zurich's OLAT.

🔵 **Why this base missed it for seven passes, stated so the channel gets fixed and not just the row.** Every pass measured the *most-starred* LMS repositories and generalised from them. OpenOlat has **449 stars and 32,210 commits** — a star:commit ratio of 1:72, against Moodle's 7.6k:~100k. A star-ordered channel ranks it below two dozen tutorial repositories. The signal that would have caught it is the one this page already records about Moodle (*more forks than stars — a codebase institutions take copies of, not a project people watch*): **institutional software is under-starred by construction, so a star floor is the wrong instrument for the platform shelf.** The row was found this pass from a licence-first query — "Apache LMS" — not an adoption-first one.

🔴 **A headline claim this KB has published in three files needs correcting, and this is the correction.** The claim was: *"there is no permissively-licensed, production-grade open source LMS."* **`learningequality/kolibri` is MIT (1,097 B payload read at p651), 1.2k ★ / 1.0k forks, and is a production learning platform.** The claim as written was wrong.

The accurate version, stated carefully because the distinction decides engagements:

- 🔴 ~~**There is no permissive platform of the Moodle / Open edX class.**~~ **Withdrawn at p653.** There is one: **OpenOlat, Apache-2.0.** What remains true is narrower and worth stating precisely, because it still decides most engagements: *the LMS the client already runs* is almost always copyleft — Moodle and Chamilo dominate LATAM and much of EMEA K-12, Canvas and Blackboard dominate North America, and neither of those facts changes because a permissive alternative exists. `compose/patterns.md` P2 and P3 therefore remain the common case. What changes is that there is now a **greenfield** option: when the client is *choosing* a platform rather than extending one, Apache-2.0 institutional course management is on the table, and with it a closed derivative. See **Pattern F** below and `compose/patterns.md` **P11**.
- ⚠ **One honest qualifier on OpenOlat, measured not assumed.** 449 ★ is real adoption for institutional software but it is not Moodle's ecosystem: there is no third-party plugin marketplace of Moodle's scale, and the contributor base is concentrated around frentix GmbH. Scope it as *a platform with a vendor behind it that happens to be Apache-2.0*, not as a community ecosystem. The licence is the differentiator; the ecosystem is not.
- **But there is a permissive platform for *learning delivery*, and it is the right base for a specific and commercially real segment:** offline-first, low-connectivity, device-resident deployment. Kolibri covers content delivery, learner progress and coach tooling, under MIT, with no connectivity requirement — and a proprietary derivative is permitted.

🔵 **Why the error was easy to make and worth recording:** every pass asked "is there a permissive LMS?", measured the institutional LMS field, found it uniformly copyleft, and generalised. Kolibri is not an institutional LMS and so never entered the comparison — the question's framing excluded the answer. It surfaced at p651 only because an EMEA-Africa opportunity needed an offline-first base and the search was for *that*, not for a licence.

Richie remains a portal CMS, GegoK12 a 55-star school-administration system, and Sakai's ECL-2.0 carries a patent grant scoped narrowly to education. This is how an engagement must be structured:

| Licence | What it permits | Engagement model it supports |
|---|---|---|
| **MIT / Apache-2.0 / BSD / ECL-2.0** | Proprietary derivative, closed distribution | Product, resale, closed IP. At platform level this now means **OpenOlat** (Apache-2.0, **institutional course management** — new at p653), **Kolibri** (offline-first delivery), **Richie** (portal), **GegoK12** (administration) — and the whole agent layer |
| **GPL-3.0** (Moodle, Chamilo, ILIAS, Gibbon) | Derivatives must be GPL **when distributed** | Client-operated deployment and bespoke plugins are fine; a multi-client closed product is not |
| **AGPL-3.0** (Open edX, Frappe LMS, Veo) | Network use counts as distribution — modified source owed to **users** | Managed-service / SaaS delivery is directly affected. Keep modifications in permissively-licensed plug-in points (XBlock) or accept disclosure |
| **GPL-2.0** (RosarioSIS, openSIS) | As GPL-3.0, but **incompatible with GPL-3.0 code** when combining | Fine standalone; do not link GPL-2.0-only SIS code with GPL-3.0 LMS code in one work |
| **LGPL-3.0** (OpenEduCat) | Linking from separately-licensed code is permitted provided the LGPL portion stays **replaceable** | The most workable copyleft on this shelf. Extend via Odoo modules and keep the LGPL core swappable; proprietary modules alongside are defensible |

The practical rule: **put the IP in the agent layer, not in the platform fork.** Agents (MIT/Apache, see `agents/top.md`), XBlocks (Apache-2.0), the portal (Richie, MIT) and the retention engine (`fsrs-rs`, BSD-3-Clause) are where proprietary value can live. The LMS core stays stock.

## How to add AI on top

### Pattern A — Moodle + agent layer (best fit: LATAM public sector, EMEA K-12)
```
Moodle (GPL-3.0)
  └── AI subsystem (4.5+): pluggable provider — Ollama for data-residency, or a hosted model
  └── Moodle Web Services (REST)
       └── MCP server  ──►  tutor agent (DeepTutor / Bloom / OATutor)
```
Keep the agent out-of-tree and talk to Moodle over REST. Nothing you write becomes a GPL derivative, and the client keeps a stock, upgradable Moodle.

🟢 **p652 named the MCP server in that diagram, which was a placeholder in every prior pass.** The permissive Moodle-side field was searched properly and it exists — **seven MIT servers in five languages** — but the whole category tops out at **27★**, against `canvas-mcp`'s **317★** for the identical job on Canvas.

| Option | Licence | Stars | Scope | Verdict for this pattern |
|---|---|---|---|---|
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT (1,064 B) | **27** | Rust, 163 commits, 22 tools, read **and** write, `call_ws_function` escape hatch to any Moodle web service, states validation against Moodle 3.7 → 5.x | 🟢 **The base.** Most tools, most commits, broadest version claim, the only one with real write coverage plus an escape hatch. Adopt and harden; do not treat 27★ as production-ready. |
| [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | MIT (1,072 B) | 4 | Python, 75 commits. Browser SSO → locally-stored token. Student writes and teacher grading **off by default** behind env flags | 🟡 **The safest default posture in the field**, and 4★ is not adoption. Borrow its permission model even if you build on the Rust one. |
| 4 further MIT servers | MIT | 0 | TypeScript (read-only by construction), Go (MCP + REST mode), Python (OpenAPI 3.1 bridge), Python (14 tools + CLI) | Not bases. Measured so the search is not re-spent; full table in `agents/trending.md` (p652). |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0 (34,523 B)** | 1 | Open-core; paid Premium Plugins sold separately | ❌ **Not for this pattern.** The whole point of Pattern A is keeping your code out of the GPL's reach; an AGPL agent *is* the network-served component, so it defeats the containment. Secondary write-ups describe its terms as a bespoke "no closed-source repackaging" licence — that is plain AGPL restated in marketing language. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT | 0 | — | ❌ A **fork** of `G36maid/moodle-mcp`, 43 commits behind, and the top search result for the query. Caught by the copyright line in its own grant payload reading `G36maid`. |

⚠ **Two things to scope honestly in a proposal.** First, the agent bridge for Moodle is an **adopt-and-harden** input, not an install — budget upstream contribution, a security review of the token handling, and your own integration tests against the client's Moodle version. Second, the ~12× open-source investment asymmetry between the Canvas and Moodle agent layers is structural, not temporary: it means **Pattern C is cheaper than Pattern A today**, and a client in LATAM or EMEA running Moodle is paying for that asymmetry. Say so rather than pricing Pattern A as if it were Pattern C.

### Pattern B — Open edX + XBlock (best fit: corporate academies, national platforms)
```
Open edX (AGPL-3.0)  ← unmodified
  └── XBlock (Apache-2.0)  ← your code lives here
       └── agent backend (MIT/Apache) outside the platform
```
This is the licence-safe shape for Open edX. Modifying the platform itself pulls AGPL network-disclosure onto a managed service; an XBlock plus an external backend does not.

### Pattern C — Canvas (commercial LMS) + MCP
```
Canvas LMS (client's existing SaaS)
  └── canvas-mcp (MIT, 317★) — ~102–128 tools
       └── agent (Claude / Cursor / Codex clients)
```
No platform licence question at all, because the LMS is not ours to modify. The fastest route to a working pilot where the client already runs Canvas.

### Pattern E — Offline-first, permissive all the way down (Sub-Saharan Africa, rural South Asia, Pacific)
```
Kolibri (MIT)  ← the platform itself is permissive: a closed derivative is allowed
  └── local model via Ollama (MIT) on the device or a classroom server
  └── fsrs-rs (BSD-3-Clause) — review scheduling computed on-device
       └── sync when connectivity appears; nothing required in between
```
This is the only pattern on this page with **no copyleft component anywhere**, and the only one that works with no connectivity. It matches the architecture African edtech builders have already converged on — offline-capable, student data resident on the device — which is both a connectivity response and a trust posture. It is also the one pattern where Globant can ship a closed product end to end.

### Pattern F — Permissive institutional LMS, agents in-tree (greenfield HE, EMEA public sector) 🟢 new at p653
```
OpenOlat (Apache-2.0)          ← the platform itself is permissive: closed derivative allowed
  └── langchain4j 1.23.0 (Apache-2.0, already in the pom)
        ├── langchain4j-open-ai      ──► any OpenAI-compatible endpoint
        │                                 (Ollama / vLLM on in-jurisdiction hardware)
        ├── langchain4j-anthropic
        └── langchain4j-embeddings   ──► embeddings computed in-process
  └── Apache Lucene (Apache-2.0, already in the pom) ← semantic search, no egress
  └── PostgreSQL JDBC 42.7.14 (BSD-2-Clause)  ← NOT MySQL: see the note below
```

**What makes this pattern different from every other one on this page:** it is the only one where **the institutional LMS itself is permissive and the AI plumbing is already in the tree**. Patterns A, B and C all exist to hold proprietary work *outside* a platform that cannot absorb it. Here there is nothing to hold outside — an agent can live in-tree, in the same build, and the deliverable can still be closed.

🟢 **The LLM subsystem is not a roadmap item; it is declared in `pom.xml`.** `langchain4j` 1.23.0 with the OpenAI, Anthropic and embeddings modules, verified by reading the manifest at first hand on 2026-11-04. The practical consequence for a data-residency engagement: **`langchain4j-open-ai` speaks the OpenAI-compatible wire protocol, which Ollama and vLLM both serve** — so an in-jurisdiction, no-egress deployment needs a configuration change and an endpoint, not a code fork and not a new dependency. There is no `langchain4j-ollama` module in the tree and it is not needed for that path.

🔴 **The one dependency that decides whether a closed derivative is actually clean.** Of 270 declared dependencies, exactly one is copyleft: **MySQL Connector/J** (`com.mysql:mysql-connector-j` 26.10.0), which is **GPL-2.0 with the Universal FOSS Exception**. The exception permits combination with OSI-approved open source licences including Apache-2.0 — but it does **not** cover a closed proprietary derivative, which is the entire point of choosing this platform. The fix is already in the tree and costs nothing: **PostgreSQL JDBC 42.7.14 (BSD-2-Clause) is a first-class supported backend.** Specify PostgreSQL in the proposal and the tree is permissive end to end.

Verified absent, because in a Java LMS these are the usual killers and their absence is what makes the above true: **no iText** (AGPL-3.0), **no JasperReports** (LGPL). Hibernate is at **7.4.14** and hibernate-validator at **9.1.6** — both Apache-2.0 eras, not the old LGPL-2.1 Hibernate.

⚠ **Scope it honestly.** Java/Spring/Hibernate is a heavier integration skill-set than PHP-Moodle or Python-Open edX, and the contributor base is concentrated around one vendor. Pattern F buys a licence position, not a cheaper build.

### Pattern G — Corporate L&D, closed and client-branded (best fit: EMEA and North America enterprise) 🟢 new at p655
```
Mentingo (MIT) — fork it, brand it, ship it closed
  ├── AI mentor already in core: Vercel AI SDK + LangChain + pgvector retrieval
  ├── LiveKit voice → scored role-play (sales, compliance, support scenarios)
  ├── Langfuse tracing → the audit trail the compliance buyer asks for
  └── multi-tenant + white-label in core → one deployment, many client brands
       └── EU-only deployment is a configuration choice: Postgres + S3-compatible store in-region
```
**Why this pattern is new and not a variant of F.** Pattern F (OpenOlat) serves *institutional higher education*. This serves **corporate L&D**, which is a different buyer, a different sales cycle and — decisively — a buyer who expects the vendor's own brand on the product. Moodle (GPL-3.0), Open edX (AGPL-3.0) and Canvas (AGPL-3.0) all make a closed, rebranded derivative impossible or awkward; **MIT makes it a non-question**. The trade is adoption: 106 ★ means you are hardening a young codebase, not installing a mature one. Scope the hardening explicitly.

### Pattern H — Technical curriculum, BSD all the way down (best fit: bootcamps, CS faculties, data-science academies) 🟢 new at p655
```
JupyterHub (BSD-3-Clause)        ← per-learner isolated environment, LTI into the client's LMS
  └── nbgrader (BSD-3-Clause)    ← release → collect → autograde → manual grade → feedback
       ├── deterministic tests score what is checkable
       └── microsoft/LLM-Rubric (MIT) scores what is not — calibrated against human raters
            └── Ollama (MIT) or vLLM for the model, in the client's own network
```
**No copyleft component anywhere, and every piece has a decade of production use.** This is the second pattern on this page with a fully permissive chain (Pattern E is the other), and the first one that covers *assessment*. State the boundary to the client plainly: nbgrader grades submitted work deterministically; it does not establish **who** submitted it, and no permissive proctoring tool was found in four passes of searching.

### Pattern I — Launch over LTI, record over xAPI, never fork the platform (best fit: any client with an incumbent LMS) 🟢 new at p656

The pattern that makes the other eight safe to sell. Every pattern above eventually asks the same two questions — *how does our thing appear inside the LMS the client already runs,* and *how do we prove it worked* — and until p656 this shelf answered neither.

1. **Get in over LTI 1.3, not through a fork.** `tsugiproject/tsugi` (Apache-2.0) for PHP, `dmitry-viskov/pylti1.3` (MIT) for Python, `jupyterhub/ltiauthenticator` (BSD-3-Clause) when the destination is a notebook. One integration launches inside Moodle, Canvas, Brightspace, Open edX, Sakai and OpenOlat. 🔵 **The licence consequence is the whole point: an LTI tool is a separate work that the LMS merely launches, so a GPL-3.0 Moodle or an AGPL-3.0 Open edX imposes nothing on it.** This is the same boundary P3 draws around XBlocks, generalised to every platform at once.
2. **Keep the client's content where it is.** `jcputney/scorm-again` (MIT) plays their existing SCORM 1.2 / 2004 / AICC / cmi5 packages. If they author in H5P or Adapt, both are **GPL-3.0 — integrate, never fork**; call their APIs and ship nothing derived from them.
3. **Record every interaction to a permissive LRS.** `yetanalytics/lrsql` (Apache-2.0) behind `RusticiSoftware/TinCanJS` (Apache-2.0) on the content side, against the statement shapes in `adlnet/xAPI-Spec` (Apache-2.0). Actor, verb, object, result, timestamp — per learner, per attempt. 🟢 **This is the deliverable that turns a pilot into a renewal**, and it is what `compose/patterns.md` P5 has been selling as "governance and measurement" without naming a component.
4. **Assess with the permissive option where the subject allows it.** `numbas/Numbas` (Apache-2.0) for mathematical and quantitative work; `oat-sa/tao-core` (GPL-2.0) only where QTI compliance is contractually required, and then client-operated.
5. **Accessibility is a client-operated deployment, not a product.** `ucfopen/UDOIT` (GPL-3.0) is the only real tool. Deploy it in the client's estate, bill the remediation work, ship no derivative.

**Licence position end to end:** steps 1–4 are Apache-2.0 / MIT / BSD-3 and can carry proprietary work. Steps 2 (authoring) and 5 (accessibility) are copyleft and stay stock. **Timeline 4–6 weeks** on top of an existing engagement; it is plumbing, and the components are small.

🔴 **Scope the single point of failure explicitly.** `lrsql` is the only live permissive LRS in existence — `learninglocker` is GPL-3.0 and dormant since 2024-05-30, `adlnet/ADL_LRS` is ~12 months quiet. Name that dependency in the proposal.

### Pattern J — Artemis: the platform where the agents are already in the tree (best fit: CS / engineering faculties, technical academies, greenfield HE) 🟢 new at p657

Every other pattern on this page is *platform + agent layer Globant builds*. This one is not, and that changes the proposal.

```
ls1intum/Artemis (MIT, 826★, branch `develop`, tag 10.3.1)   ← self-hosted by the institution
  ├── exercises: programming · text · modeling (Apollon, MIT) · quiz · file upload
  ├── Atlas: competencies, learning paths, learning analytics
  ├── Iris      → LLM tutor: hints and leading questions, never answers
  ├── Athena    → suggests feedback on text / modeling / programming submissions
  ├── Hyperion  → AI-assisted exercise authoring (Spring AI)
  └── ls1intum/Pyris (MIT) ← the LLM microservice seam: point it at the CLIENT's
                              Ollama / vLLM / sovereign endpoint, not a public API
```

**What Globant sells here is not the AI.** It is: deployment on the client's infrastructure, LTI integration so the incumbent LMS stays the front door, migration of real existing exercises, **calibration of Athena's feedback suggestions against the client's own graders with the agreement statistic reported honestly**, the appeals workflow, and grader training. ⚠️ **All three AI subsystems are configuration-gated and off by default — which is the feature to lead with** in an EU or Korean procurement: the institution can evidence exactly which AI is enabled, for which cohort, with a human in the loop on every consequential decision.

⚠️ **Scope honestly against `Mentingo` and `OpenOlat`.** Artemis is built for *assessed technical coursework at a university*. It is not a corporate L&D product (that is `Mentingo`, MIT) and not a general institutional LMS with curriculum management and portfolios (that is `OpenOlat`, Apache-2.0). Proposing it for a corporate academy would be a mis-scope.

### Pattern K — Spoken-language assessment on a permissive stack (best fit: LATAM and APAC language programmes, corporate English training) 🟢 new at p657

The layer this KB had never touched, and it replaces a metered cloud API with an on-premise component.

```
learner records a target sentence
  └── Halleck45/OpenPronounce (MIT, 184★)  ← phoneme-level score, mispronounced words in IPA,
        │                                     per-word confidence, pitch + energy curves. CPU-only.
        ├── Kyubyong/g2p (Apache-2.0, 936★)        ← English: what the learner SHOULD produce
        ├── CUNY-CL/wikipron (Apache-2.0, 376★)    ← the same, for hundreds of other languages
        └── liguozheng-ac/japanese-speech-xray (MIT, 177★) ← pitch-accent languages need prosody,
                                                              not just a phone string
  └── launch over LTI (Pattern I) · record each attempt to yetanalytics/lrsql (Apache-2.0) over xAPI
```

**The commercial argument is a line item the client already pays.** `OpenPronounce`'s own author positions it as a self-hosted alternative to **Azure Pronunciation Assessment** — so the pitch is a metered per-utterance cloud cost replaced by a CPU container inside the client's estate, which is simultaneously the cost case and the **EMEA data-residency** case (voice is biometric-adjacent personal data; keeping it on-premise removes a transfer question rather than answering it).

⚠️ **Two boundaries to state in writing.** First, `OpenPronounce` is **184 ★ with a single maintainer** — pilot it against the client's own recordings before it is in a proposal, and note that the better-known project in this layer (`ai-pronunciation-trainer`, 525 ★) is **AGPL-3.0** and therefore cannot be the deliverable. Second, **phoneme scoring is not fluency assessment** and is not a CEFR level; do not let a proposal imply it replaces a human oral examiner.

### Pattern D — SIS + LMS split
Moodle or Open edX handles learning; the administrative system handles enrolment, timetabling, records and fees. Administrative agents (scheduling, at-risk alerting, enrolment triage) belong on the administrative side, where the data actually lives.

Four verified options, and the licence is what should decide between them:

| Option | Licence | Choose it when |
|---|---|---|
| **OpenEduCat** (905★) | LGPL-3.0 | The client wants a full ERP (finance and HR, not just records) or already runs Odoo. Weakest copyleft here — extend via Odoo modules, keep the LGPL core replaceable. ⚠️ resolve the branch; the default is `19.0` and `20.0` exists. |
| **Gibbon** (GPL-3.0) | GPL-3.0 | K-12 school management with strong timetabling; client-operated deployment. |
| **RosarioSIS** (651★) | GPL-2.0 | Lean PHP/PostgreSQL SIS. ⚠️ default branch is `mobile`; check out a version branch. 🔴 GPL-2.0-only code cannot be combined into one work with GPL-3.0 code. |
| **GegoK12** (55★) | **MIT** | The client needs a closed derivative of the administrative layer. The only row that permits one — at the cost of much lower adoption. |

🔴 **Searched at p652 and deliberately not added: `frappe/education`**, the education module of the Frappe/ERPNext stack — the obvious fifth candidate for this slot, and it fails on grant quality rather than on function.

| Channel | Reading 2026-11-04 |
|---|---|
| `git ls-remote --symref` | 🟢 resolves; real default branch is **`develop`** — not `main`, not `master` |
| `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` on `develop` | 🔴 **404 on all four** |
| `license.txt` on `develop` | 🔴 **19 bytes.** Entire contents: `License: GNU GPL V3` |

**A file that names a licence is not a licence.** There is no permission paragraph, no conditions, no warranty disclaimer, no copyright holder and no version pinning beyond "V3" — and GPL-3.0's own terms require the notice and full text to accompany the work. Frappe's intent is obvious and nobody will be surprised by it. But the question a client's legal review asks is what the grant *says*, and here the answer is nineteen bytes, so this slot stays at four verified options. If an engagement needs the Frappe stack, the fix is one upstream commit and it is worth asking for.

For every copyleft option the out-of-tree rule is unchanged: agents talk to the system over its API, in a separate process.
