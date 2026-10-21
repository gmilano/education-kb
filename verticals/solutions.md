---
industry: education
region: Global
updated: 2026-10-21
---

# Education — vertical platforms to customise with AI

**Pass 357 · 2026-10-21.** Real, deployed systems that an engagement can extend, in the
sense that Odoo is extensible for ERP or OpenMRS for healthcare. All verified first-hand
**2026-10-21** (liveness + default branch via `git ls-remote --symref`, licence read
from payload). 🔴 `p357` ran without an authenticated GitHub index, so it measured no
stars; verification is unchanged.

The column that decides engagement shape is **Licence reach**: whether AI added on
top can stay in a closed client deliverable, or whether the copyleft of the host
platform reaches it.

---

## Core platforms

| Platform | Repo | Licence | Licence reach for AI built on top | Where it fits |
|---|---|---|---|---|
| **Moodle** | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 (`COPYING.txt`) | 🟡 A **plugin** is a derivative work → GPL-3.0. An **external agent** talking over web services / LTI stays separate | The default K-12 and HE LMS worldwide. Largest installed base; plugin API is the integration surface |
| **Open edX** | [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 🔴 AGPL — network use triggers source obligations. Extend via **XBlock** or stay out-of-process | Large-scale HE, MOOCs, corporate academies. Deploy with [tutor](https://github.com/overhangio/tutor) |
| **Canvas LMS** | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 🔴 AGPL. Build as an **LTI 1.3 tool**, not a fork | Dominant HE LMS in North America. 🟡 The public mirror last pushed **2026-04-30** — ~6 months stale; treat GitHub as reference, not upstream |
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 🟢 **None.** Fork freely into closed deliverables | Offline-first. The right base for low-connectivity deployments — rural LATAM, Sub-Saharan Africa, remote APAC |
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 🟢 **None** | Swiss-built HE LMS. The only full-featured *permissive* HE platform on this shelf |
| **Chamilo** | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 🟡 Plugin = derivative | Accessibility- and ease-of-use-focused. Strong Spanish/French-language support; real LATAM and EMEA public-sector deployments |
| **Sakai** | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 🟢 **Permissive** (Apache-2.0 derivative with an education patent clause) | Research-university collaboration + learning environment |
| **Frappe LMS** | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 (`license.txt`) | 🔴 AGPL | Modern LMS on the Frappe framework — pairs with ERPNext for an institution-wide stack (India-origin) |
| **ClassroomIO** | [classroomio/classroomio](https://github.com/classroomio/classroomio) | AGPL-3.0 | 🔴 AGPL | Customer/partner training academies for SaaS companies — the corporate-learning vertical |
| **ELMS Learning Network** | [elmsln/elmsln](https://github.com/elmsln/elmsln) | GPL-3.0 (`LICENSE.md`) | 🟡 Plugin = derivative | Distributed course-delivery ecosystem (Penn State origin) |
| **Moodle App** | [moodlehq/moodleapp](https://github.com/moodlehq/moodleapp) | 🟢 **Apache-2.0** (`COPYING.txt`) | 🟢 **None** | The official mobile client — **permissive while core is GPL-3.0**. White-labelled branded learner apps are a clean, licence-safe deliverable |

## Administration — SIS and ERP

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 (branch `19.0`) | 🟡 LGPL — dynamic linking stays separate; a fork does not | Education ERP on **Odoo**: admissions, fees, timetabling, library, hostel. The Odoo module ecosystem comes with it. This is the education analogue of "Odoo for ERP" |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 (branch `mobile`) | 🟡 Module = derivative | K-12 student information system: enrolment, grades, attendance, scheduling, billing. Multilingual with strong Spanish/Portuguese support — practical for LATAM public-sector K-12 |
| **Learner Credential Wallet** | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT** | 🟢 **None** | Verifiable credentials / digital diplomas under OpenWallet Foundation. The build target for skills-based hiring work |
| 🆕 **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 (🔴 `docs/License.txt`) | 🟡 Module = derivative. **GPL-2.0, not 3.0** — do not assume GPL-3.0 compatibility | K-12 SIS with parent and teacher portals, gradebook, report cards and transcripts. The second mature K-12 SIS on this shelf alongside RosarioSIS, and a genuine alternative when a client needs portals rather than Spanish localisation |
| 🆕 **FenixEdu Academic** | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | 🟡 LGPL — dynamic linking stays separate | **Higher-education** SIS from Instituto Superior Técnico, Lisbon: curricular plans, enrolment, degrees, theses. The HE counterpart to the two K-12 systems above, and the only European university SIS on this shelf |
| 🆕 **ERPNext** | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (🔴 `develop/license.txt`) | 🔴 **GPL-3.0 — strongest copyleft on this tier.** A custom app is a derivative; reach it over its **REST API**, not as a Frappe app | Full institution-wide ERP — finance, HR, procurement, assets — with an education module. Pairs with [`frappe/lms`](https://github.com/frappe/lms) for a single-vendor teaching-plus-administration stack. India-origin |

### 🔴 There is no permissive education ERP, and that is this pass's most expensive finding

🟢 **Every row on this tier is copyleft** — LGPL-3.0, GPL-2.0, GPL-3.0 — and the one
permissive row (Learner Credential Wallet) is a credential wallet, not an
administration system. `p357` ran a leg specifically to break that, because a
permissive education ERP would be the most valuable address on this shelf: it would let
a studio **fork** an admin system into a closed deliverable instead of building one.

🔴 **All three candidates the leg returned are unusable, and none for a licence
reason:** `foradian/fedena` (claimed Apache-2.0) is live and serves **nothing** at any
standard path; `gegok12/gegok12` (claimed MIT) **does not exist**; and
`schooltool/schooltool` is dead. See `repos/foundations.md` for the probe detail.

🟢 **So the engagement guidance is settled rather than pending**, and it is the opposite
of a gap:

1. **Closed admin deliverable → it is a build.** Price it as one. There is no
   permissive base to fork, and a successor meeting the Fedena or GegoK12 claim in a
   roundup should read this paragraph before costing a fork.
2. **Can accept copyleft on the admin tier → `openeducat_erp` (LGPL-3.0)** remains the
   recommendation, because LGPL permits dynamic linking: AI modules can stay separate
   works. It is also the closest true analogue to "Odoo for ERP" — it *is* Odoo.
3. **Already on Frappe → reach ERPNext over its REST API.** GPL-3.0 reaches a Frappe
   app; it does not reach a separate service calling the API.

## Content, media and delivery

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **H5P** | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) · [h5p/h5p-cli](https://github.com/h5p/h5p-cli) | GPL-3.0 core / 🟢 **MIT** CLI | 🟢 Tooling on the **CLI** is unencumbered; code linked into the library is GPL | ~50 interactive content types that embed in Moodle, Canvas and Open edX. The fastest route to AI-generated interactive exercises inside an existing LMS |
| **Opencast** | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (branch `develop`) | 🟢 **Permissive** | Lecture capture, video pipeline, scheduled recording. The ingestion point for transcript- and video-based AI |
| **BigBlueButton** | [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 (branch `v4.0.x-develop`) | 🟡 LGPL | Virtual classroom with whiteboard, breakouts, recording. Integrates with Moodle and Canvas |
| **Marsha** | [openfun/marsha](https://github.com/openfun/marsha) | 🟢 **MIT** | 🟢 **None** | LTI learning-content management system from France Université Numérique — drop-in video/content provider for any LTI host |
| **Hyperbook** | [openpatch/hyperbook](https://github.com/openpatch/hyperbook) | 🟢 **MIT** | 🟢 **None** | Interactive teaching books from markdown. Good fit for AI-generated courseware that must stay editable by teachers |
| **JupyterHub** | [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | 🟢 **BSD-3-Clause** | 🟢 **None** | Multi-user notebooks for CS/data-science teaching. Pair with [ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) for LMS single sign-on |

## Assessment and integrity

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **Judge0** | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | 🟡 Use **as a service over its API** and the boundary holds | Sandboxed code execution in 60+ languages. The execution backend for any programming-assessment or coding-tutor build |
| **INGInious** | [INGInious/INGInious](https://github.com/INGInious/INGInious) | AGPL-3.0, *"most of the files"* | 🔴 AGPL, and 🟡 **mixed** — the grant text itself scopes to most, not all | Secure automated exercise assessment (UCLouvain). Mature grading platform |
| **Dolos** | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | 🟢 **MIT** | 🟢 **None** | Source-code plagiarism detection (Ghent). The integrity layer for AI-era programming courses — and newly relevant now that students submit agent-assisted code |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | GPL-3.0 | 🟡 Derivative if forked | Accessibility inspection of LMS course content. Directly serviceable against EU accessibility and US Section 508 obligations |
| **scorm-again** | [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | 🟢 **None** | Modern SCORM 1.2 / 2004 JS runtime. The bridge for the enormous installed base of legacy SCORM corporate content |

## 🆕 Code-execution and online-judge platforms

🟢 **New section, `p356`.** Last pass this shelf had exactly one way to run student
code — `judge0`, GPL-3.0, over its API. There are at least fifteen, and **the largest
permissive one is bigger than the copyleft one everybody reaches for first.**

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **QingdaoU OnlineJudge** | [QingdaoU/OnlineJudge](https://github.com/QingdaoU/OnlineJudge) | 🟢 **MIT** | 🟢 **None.** Fork into a closed deliverable | **The recommendation.** A complete judge — Vue + Django + Docker, submissions, contests, problem bank, admin — at 6 552 ★ and MIT. White-label it for a client coding academy |
| **QingdaoU Judger** | [QingdaoU/Judger](https://github.com/QingdaoU/Judger) | 🟢 **MIT** (branch `newnew`) | 🟢 **None** | The seccomp execution sandbox alone, on its own MIT grant. Use it when the surrounding platform is already built and only safe execution is missing |
| **Judge0** | [judge0/judge0](https://github.com/judge0/judge0) | GPL-3.0 | 🟡 Service over HTTP keeps the boundary | 60+ languages behind a REST API. Still the fastest thing to stand up; the licence is the cost |
| **Hydro** | [hydro-dev/Hydro](https://github.com/hydro-dev/Hydro) | AGPL-3.0 | 🔴 AGPL — network use triggers source obligations | Multi-tenant, high-performance, plugin architecture. The right base for an institution running many courses and contests — if the client can accept AGPL |
| **DMOJ** | [DMOJ/online-judge](https://github.com/DMOJ/online-judge) · [DMOJ/judge-server](https://github.com/DMOJ/judge-server) | AGPL-3.0 | 🔴 AGPL | Django contest platform plus a separate judging backend. Clean split between web tier and executor |
| **Sharif Judge** | [mjnaderi/Sharif-Judge](https://github.com/mjnaderi/Sharif-Judge) | AGPL-3.0 (branch `Version-1`) | 🔴 AGPL | 🟢 **Built for COURSES, not contests** — assignments, deadlines, per-student feedback. Closest in shape to what a university client actually asks for |
| **Otter-Grader** | [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** | 🟢 **None** | Autogrades **Python and R notebooks**, with containerised execution and LMS export. Pairs with JupyterHub for data-science teaching |
| **HUSTOJ** | [zhblue/hustoj](https://github.com/zhblue/hustoj) | GPL-2.0 | 🟡 Derivative if forked | The long-running PHP/C++ judge; very low deployment footprint |

🔵 **Pick on the licence, then on the shape.** For a closed client deliverable the path
is **QingdaoU OnlineJudge (MIT)** or **Judger (MIT) inside your own platform**. For an
institution that will run it themselves and publish nothing, Hydro's plugin
architecture is the better engineering. For a *course* rather than a contest, Sharif
Judge is the only row built for it — and it is AGPL, so it stays the client's
deployment, not the studio's product. Wired end-to-end in `compose/patterns.md`
Pattern 9.

---

## 🔴 Platforms to exclude, and why

| Platform | Repo | Why excluded |
|---|---|---|
| Advising App | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** — source-available, not OSI. Globant **cannot offer it as a managed or hosted service**. Capable AI student-advising product; wrong licence for studio delivery |
| Caliper spec | [1EdTech/caliper-spec](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS specification document licence** — not software. Implement the standard; do not vendor the document |
| cn-math-taxonomy | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC-BY-NC-4.0** — NonCommercial. Excellent China K-12 curriculum graph, unusable in paid engagements |
| 🆕 CBIT-AiExam-plus | [reneverland/CBIT-AiExam-plus](https://github.com/reneverland/CBIT-AiExam-plus) | 🔴 **No grant at all.** The README carries an MIT badge; the `LICENSE` it links to **404s**, as do four other rungs. The most complete AI examination platform found this pass and it is all-rights-reserved until its author adds a file |
| 🆕 MathCyclus (Lingxi) | [JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant](https://github.com/JinLingxi/MathCyclus---Lingxi-Question-Bank-Assistant) | 🔴 **Grant exists only as a prose sentence in the README.** A claim, not a licence file — cheap for the author to fix and not safe to assume |
| 🆕 Anti-proctoring tooling | [`Batlez/CloakBox`](https://github.com/Batlez/CloakBox) · `SunnyCOdet/ofradr` | 🔴 **Not education software.** Both are high-starred results in the `proctoring` leg and both exist to **defeat** exam monitoring. Named here so a successor running that leg does not mistake them for supply |

## 🟢 The permissive shortlist

When a client needs AI inside a closed deliverable, these are the platforms whose
licences do not reach it:

**Platforms:** OpenOLAT (Apache-2.0) · Kolibri (MIT) · Sakai (ECL-2.0) ·
Moodle App (Apache-2.0)
**Interop:** scorm-again · ltijs · pylti1.3 · CACCL · Marsha · ltiauthenticator (all MIT/Apache/BSD)
**Content:** H5P CLI · Hyperbook · JupyterHub
**Assessment:** Dolos · Ares2 · 🆕 **QingdaoU OnlineJudge** · 🆕 **QingdaoU Judger** · 🆕 **Otter-Grader**
**Scheduling:** 🆕 py-fsrs · 🆕 fsrs4anki · 🆕 FSRS (algorithm)
**Credentials:** Learner Credential Wallet
**Curriculum data:** 🆕 **oak-curriculum-ontology** (OGL-3.0 data + MIT code — 🟢 the
only curriculum asset on this base with commercial use and **no** share-alike)
**LMS connectors:** 🆕 **bruchris/canvas-lms-mcp** · 🆕 **G36maid/moodle-mcp** ·
🆕 **AnonymousOnyx22/canvas-lms-student-mcp** · falkenslab/moodle-mcp (all MIT)
**Lecture capture:** 🆕 **LectureLab** (MIT) · 🟡 the MIT *engines* inside Cap and
CaptureFlow — never their AGPL applications

🔴 **Nothing on this shortlist is an ERP or an SIS.** That absence is measured, not
unexamined — see the ERP note above.

Everything else on this shelf is GPL/AGPL/LGPL and should be reached **over a
protocol boundary** — LTI 1.3, web services, or MCP — rather than forked. That
boundary choice is the single most consequential architectural decision in an
education engagement, and it is a licence decision before it is a technical one.
