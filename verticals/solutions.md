---
industry: education
region: Global
updated: 2026-10-21
---

# Education — vertical platforms to customise with AI

**Pass 360 · 2026-10-21.** Real, deployed systems that an engagement can extend, in the
sense that Odoo is extensible for ERP or OpenMRS for healthcare. All verified first-hand
**2026-10-21** (liveness + default branch via `git ls-remote --symref`, licence read
from payload). 🔴 `p359` ran without an authenticated GitHub index (fourth consecutive
pass), so it measured no stars; verification is unchanged. 🟢 Every address on this shelf
was part of a **236-address corpus liveness sweep: 236 live, 0 dead.**

🟡 **`p358` put a crack in this shelf's most expensive finding** — `p357`'s *there is no
permissive education ERP* — with `Moha-abshir/SMS`. That still stands, qualified: the
exception is small and the rule holds at the scale an engagement needs.

🔴 **`p359` adds a second kind of crack, and it is a warning rather than an
opportunity.** This shelf has always separated rows by **licence reach**. `p359` found a
row whose licence reach is **none** — stock MIT, organisation account, exactly the shape
that ends a search — behind which there are **four commits**. 🟢 **So this pass adds a
second column to the judgement this shelf exists to support: a permissive grant with no
software behind it is not a platform**, and `verticals/solutions.md` is precisely where
that mistake would be made. See the proctoring note below.

🟢 **`p360` adds a platform family with procurement behind it, which is this shelf's
scarcest kind of row.** France's **ENT** — an AGPL-3.0 school portal serving millions of
pupils per *région*, with a commit the day before this pass — is shelved below. 🔵 It also
sharpens the `p359` caution above: the ENT rows are the opposite shape to a permissive
grant with four commits behind it, and holding both on one shelf is what makes the
**licence reach** column decidable.

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

## 🆕 National school portals — the ENT tier, `p360`

🟢 **This shelf's premise is Odoo-for-ERP or OpenMRS-for-healthcare: a real, deployed
system an engagement extends rather than builds.** France's **ENT** (*Espace Numérique de
Travail*) is that, for school administration and the parent/pupil/teacher portal, and it
had no row here for 359 passes.

| Platform | Repo | Licence | Licence reach | Where it fits |
| --- | --- | --- | --- | --- |
| **entcore** — ENT kernel | [edificeio/entcore](https://github.com/edificeio/entcore) | 🟡 **AGPL-3.0** (`master/LICENSE`, © Édifice) | 🔴 **Network copyleft reaches a fork.** 🟢 Does **not** reach a separate service that talks to its HTTP API | A **régional** school portal: identity, messaging, timetable, the statutory *cahier de textes*, attendance, the competency record. Both *premier* and *second degré* from one core |
| Cahier de textes module | [OPEN-ENT-NG/cahier-de-textes](https://github.com/OPEN-ENT-NG/cahier-de-textes) | 🟡 AGPL-3.0 (`dev/LICENSE`) | 🔴 as above | The statutory lesson log — per-session lessons, homework, attachments, annual archival |
| Présences module | [OPEN-ENT-NG/presences](https://github.com/OPEN-ENT-NG/presences) | 🟡 AGPL-3.0 (🔴 `dev/LICENCE`) | 🔴 as above | Attendance and absence workflow |
| Compétences module | [OPEN-ENT-NG/competences](https://github.com/OPEN-ENT-NG/competences) | 🟡 AGPL-3.0 (🔴 `dev/LICENCE`) | 🔴 as above | Competency-based assessment — the *livret scolaire* data model |
| Exercizer module | [open-ent/exercizer](https://github.com/open-ent/exercizer) | 🟡 AGPL-3.0 (🔴 `master/LICENCE`) | 🔴 as above | Interactive exercises — MCQ, cloze, ordering; auto- and/or hand-marked |

🟢 **Deployment evidence, which is what this shelf exists to require.** Unlike the single-
author rows this shelf has had to warn about, the ENT stack has procurement behind it:

| Claim | Figure | Source quality |
|---|---|---|
| **ONE & NEO**, Hauts-de-France (Édifice) | **2.7 M users**, **5 790 institutions**, **>1 M daily connections**; contract renewed 2023 for four years | 🟡 Vendor self-reported (Édifice reference page) |
| **OpenENT** (CGI's ENT build) | **2 M pupils and students**, **1 700+ schools** | 🟡 Vendor self-reported, undated page (c. 2020) |
| ENT coverage, French public **primary** schools | 🔴 **62 %** | 🟢 IGÉSR inspectorate report, 15 Jul 2025, via Banque des Territoires |
| Fragmentation | 🔴 a family with children in école, collège and lycée can face **three different ENT solutions**; the report recommends territorial harmonisation and ÉduConnect | 🟢 Same IGÉSR report |

🟢 **That last pair is the engagement thesis, and it is an EMEA one.** A platform with
millions of users per région, a statutory data model, **62 % primary coverage** and a
government inspectorate asking for harmonisation is an integration and migration market,
not a greenfield one. 🔴 **It is also AGPL-3.0**, so the shape is a service beside the
portal, not a fork of it — see `compose/patterns.md`.

🟡 **Two cautions this shelf is the right place for.** The `entcore` README specifies
**JSE 7** and a clone URL on a decommissioned host while the code took a commit on
**2026-10-20** — price discovery from the tree, not the docs. And of four `entcore`
addresses, 🟢 `edificeio/entcore` is canonical, `opendigitaleducation/entcore` is **the
same repository** (identical 158-ref list), `OPEN-ENT-NG/entcore` is a single-branch
mirror one commit behind, and 🔴 `open-ent/entcore` is **five months stale**.

## Administration — SIS and ERP

| Platform | Repo | Licence | Licence reach | Where it fits |
|---|---|---|---|---|
| **OpenEduCat** | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 (branch `19.0`) | 🟡 LGPL — dynamic linking stays separate; a fork does not | Education ERP on **Odoo**: admissions, fees, timetabling, library, hostel. The Odoo module ecosystem comes with it. This is the education analogue of "Odoo for ERP" |
| **RosarioSIS** | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 (branch `mobile`) | 🟡 Module = derivative | K-12 student information system: enrolment, grades, attendance, scheduling, billing. Multilingual with strong Spanish/Portuguese support — practical for LATAM public-sector K-12 |
| **Learner Credential Wallet** | [openwallet-foundation-labs/learner-credential-wallet](https://github.com/openwallet-foundation-labs/learner-credential-wallet) | 🟢 **MIT** | 🟢 **None** | Verifiable credentials / digital diplomas under OpenWallet Foundation. The build target for skills-based hiring work |
| 🆕 **openSIS Classic** | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL-2.0 (🔴 `docs/License.txt`) | 🟡 Module = derivative. **GPL-2.0, not 3.0** — do not assume GPL-3.0 compatibility | K-12 SIS with parent and teacher portals, gradebook, report cards and transcripts. The second mature K-12 SIS on this shelf alongside RosarioSIS, and a genuine alternative when a client needs portals rather than Spanish localisation |
| 🆕 **FenixEdu Academic** | [FenixEdu/fenixedu-academic](https://github.com/FenixEdu/fenixedu-academic) | LGPL-3.0 | 🟡 LGPL — dynamic linking stays separate | **Higher-education** SIS from Instituto Superior Técnico, Lisbon: curricular plans, enrolment, degrees, theses. The HE counterpart to the two K-12 systems above, and the only European university SIS on this shelf |
| 🆕 **ERPNext** | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (🔴 `develop/license.txt`) | 🔴 **GPL-3.0 — strongest copyleft on this tier.** A custom app is a derivative; reach it over its **REST API**, not as a Frappe app | Full institution-wide ERP — finance, HR, procurement, assets — with an education module. Pairs with [`frappe/lms`](https://github.com/frappe/lms) for a single-vendor teaching-plus-administration stack. India-origin |
| 🆕 **School Management System (SMS)** | [Moha-abshir/SMS](https://github.com/Moha-abshir/SMS) | 🟢 **MIT** (`main/LICENSE`, holder *Mohamed Abshir*, 2026) | 🟢 **None.** Fork into a closed deliverable | 🟢 **The first permissive administration row on this shelf.** Multi-role school management built for **Kenya's Competency-Based Curriculum (CBC)**: TypeScript 5.3, React 18, Node 20, Drizzle ORM, PostgreSQL 16, Tailwind. 🟡 Single-author and young — read the qualification below before it displaces `openeducat_erp` in a proposal |

### 🟡 `p358`: there is now **one** permissive administration row, and it does not change the recommendation

🟢 **`Moha-abshir/SMS` is real, live, and genuinely MIT** — holder *Mohamed Abshir*,
2026, read from `main/LICENSE`. It is a multi-role school management system built
against **Kenya's CBC**, on a current stack (TypeScript/React/Node/Drizzle/PostgreSQL).
🟢 On the closed region vocabulary it is **EMEA**, and with `elimu-mcp` it gives that
region its first African rows anywhere on this base.

🔴 **A correction to this pass's own source before the row is used.** The search leg that
surfaced it described a *"Flask + SQLite web app, Tkinter desktop app, Android app,
M-Pesa payments, bilingual SMS, report card PDFs"* with 240 tests. 🟢 **Read first-hand,
the README describes none of that** — no Flask, no Tkinter, no M-Pesa. The snippet had
conflated this repository with a different Kenyan school-ERP project in the same leg.
🔵 The lesson is the one this base keeps relearning: **a snippet describes a repository
it has not opened**, and the payload is the only channel that settles it. Nothing was
published from the snippet; the row above states only what the README states.

🟡 **And it does not displace `openeducat_erp`.** The honest comparison:

| | `openeducat_erp` | `Moha-abshir/SMS` |
|---|---|---|
| Licence | LGPL-3.0 | 🟢 **MIT** |
| Scope | admissions, fees, timetabling, library, hostel, **plus the whole Odoo module ecosystem** | school management for one national curriculum |
| Maturity | a vendor-backed product on Odoo | 🔴 **single author, 2026, no deployment evidence found** |
| Fork into a closed deliverable | 🟡 LGPL reaches a fork | 🟢 **yes** |

🟢 **So the guidance splits rather than flips.** For an institution-wide ERP,
`openeducat_erp` remains the recommendation and `p357`'s "price it as a build" still
holds — one young single-author system is not an ERP. 🟢 For a **narrow, K-12,
school-administration deliverable that must stay closed**, `Moha-abshir/SMS` is now the
first base on this shelf that permits it, and a Kenyan or East African engagement gets
the curriculum alignment for free. 🔵 Registered as **`ACTION ZZ-bh`**: re-probe this row
next pass for commit activity and contributor count before any proposal rests on it.

### 🔴 `p357`: there is no permissive education ERP — the finding this pass qualifies

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
| 🆕 **exam-proctor** | [shaheeranser/exam-proctor](https://github.com/shaheeranser/exam-proctor) | 🟢 **Apache-2.0** (`main/LICENSE`, read `p359`) | 🟢 **None** — 🔴 **but see the Art. 5 note: the binding constraint on this row is not its licence** | **An LTI 1.3 tool that launches from inside Moodle**, authors quizzes, guards the browser, passes grades back over AGS. Dockerised with MinIO + Caddy. 🟢 **The only proctoring row on this base that reaches the LMS over a protocol boundary.** 🔴 25 commits, **1 author**, 2026-07-05 → 2026-10-11. 🔴 **`p190` read its source: head pose, iris deviation and `face-api` identity checks — GDPR Art. 9, and clear of the Art. 5 prohibition by one unset default** |
| 🆕 **openproct** | [OpenProct/openproct](https://github.com/OpenProct/openproct) | 🟢 MIT | 🟢 None | 🔴 **Not a platform — 4 commits, 2 authors, all on 2025-10-26, nothing since.** Listed only so a successor who finds "MIT, organisation account, privacy-first proctoring" does not stop here |

### 🟡 `p359`: the permissive proctoring row that is *architecturally* different — and `Gap 344`'s survivor is still the right worry

🔵 **State the record first, because the cheap version of this finding is already
refuted.** `Gap 344` once claimed the proctoring tier had **zero permissive rows**;
`P131-D` refuted that with four MIT addresses and recorded that **the gap survives as a
maturity gap, not a licence gap** — largest 18 ★, all individually owned, none
institution-backed. 🟢 **That framing still holds, and `p359` does not disturb it.**

🟢 **What [`shaheeranser/exam-proctor`](https://github.com/shaheeranser/exam-proctor)
adds is architecture, and `p359` adds its grant.** It is the only proctoring address on
this base that is an **LTI 1.3 tool**: it launches from inside Moodle — a GPL-3.0 host —
across the protocol boundary, authors quizzes in the tool, and passes grades back over
AGS. 🔵 Compare the two first-party alternatives: `openedx/edx-proctoring` and
`eLearning-BS23/moodle-quizaccess_proctoring` are **both AGPL plugins inside AGPL/GPL
hosts** — correct for the host, wrong for a studio deliverable. The four MIT rows
`P131-D` found are standalone web apps that do not reach a client's LMS at all.

🟢 **`p359`'s contribution to this row is the licence and the placement, and nothing
else about it is new to this base.** Its grant was never published here: **Apache-2.0,
read from `main/LICENSE` this pass.** Commit channel: 25 commits, **1 author**, `+0800`
and `+0500`, 2026-07-05 → 2026-10-11 → **APAC**.

### 🔴 And the reason this row was read before and never shelved — which is the thing to quote, not the licence

🔴 **`p190` read this repository's source at a pinned `HEAD` and found head pose
(yaw/pitch), iris deviation and a `face-api` **identity consistency** check.** Its
verdict, carried in `compose/code/p190-affect-inference-scan/`:

- 🔴 **GDPR Art. 9.** Biometric identity checking is special-category processing. A
  lawful basis under Art. 9(2) is required before a single frame is captured, and
  "legitimate interests" is not one of them.
- 🔴 **Clear of the EU AI Act Art. 5(1)(f) prohibition by one unset default.** MediaPipe's
  `outputFaceBlendshapes` is not set, and it defaults to `false`. 🔴 **Setting that one
  line moves the deliverable from a `2027-12-02` Annex III duty into a LIVE prohibition
  at EUR 35 M or 7 % of worldwide turnover.**
- 🔴 **Both face models are fetched at runtime** from `cdn.jsdelivr.net` and
  `storage.googleapis.com` — so the model can change without the repository changing, and
  no source review of the repo can see that.

🟢 **So the recommendation is precise rather than enthusiastic.** `exam-proctor` is the
**reference architecture** for LMS-integrated invigilation — read its LTI wiring, its AGS
grade passback and its Docker topology. 🔴 **It is not a row to deploy into an EU
engagement as it stands**, and the reason is a config default and a CDN fetch, not its
Apache-2.0 grant. 🔵 Pattern 12 on `compose/patterns.md` already holds the
process-evidence alternative for exactly this situation.

🔴 **Read the integrity recommendation with all of it, because it has not changed.**
Proctoring surveils the student; `dodona-edu/dolos` (MIT, Ghent University — 🟢 the one
institution-backed integrity row) inspects what the submission *is*. 🟢 **`dolos` remains
the first recommendation.** 🔵 And per §16 of `intel/trends.md`, invigilation is a
requirement the detection market's own customers are increasingly withdrawing.

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
| 🆕 ElewaSTEM | [ondinookello96/elewastem](https://github.com/ondinookello96/elewastem) | 🔴 **No grant at any probed path.** Offline-first multilingual AI STEM tutor targeting **16+ African languages** — the most interesting *shape* in the Africa leg and legally untouchable. Hackathon-origin, so its capability claims are also unverified |
| 🆕 AI-CONNECT-AFRICA | [EccentricIvan/AI-CONNECT-AFRICA](https://github.com/EccentricIvan/AI-CONNECT-AFRICA) | 🔴 **No grant at any probed path.** Fully on-device learning platform (bundled Gemma 3 1B) for schools with no connectivity; updates ship by **USB drive or school LAN**. 🔵 Named because its *architecture* answers a real constraint this shelf cares about — see `Kolibri` (MIT) for the same constraint with a licence |
| 🆕 nemia-escolar | [helmerpersonal-escuela/nemia-escolar](https://github.com/helmerpersonal-escuela/nemia-escolar) | 🔴 **No grant at any probed path.** Mexican school platform aligned to the **Nueva Escuela Mexicana** — planning, assessment, family communication. One of ten unlicensed LATAM addresses this pass measured; see `agents/top.md` |
| 🆕 educational-assessment-ai-agent-platform | [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | 🔴 **No grant at any probed path.** The most complete K-12 assessment architecture found this pass — RAG item authoring with self-review, rubric scoring with human review, sandboxed code grading, evals and observability. 🔵 Read it as a reference design; none of it can be used |

## 🟢 The permissive shortlist

When a client needs AI inside a closed deliverable, these are the platforms whose
licences do not reach it:

**Platforms:** OpenOLAT (Apache-2.0) · Kolibri (MIT) · Sakai (ECL-2.0) ·
Moodle App (Apache-2.0)
**Interop:** scorm-again · ltijs · pylti1.3 · CACCL · Marsha · ltiauthenticator (all MIT/Apache/BSD)
**Content:** H5P CLI · Hyperbook · JupyterHub
**Assessment:** Dolos · Ares2 · 🆕 **QingdaoU OnlineJudge** · 🆕 **QingdaoU Judger** · 🆕 **Otter-Grader** ·
🆕 **shaheeranser/exam-proctor** (Apache-2.0 — 🟢 LTI 1.3, the only proctoring row that
stays outside the host's copyleft; 🔴 **reference architecture only** — GDPR Art. 9, and
clear of the Art. 5 prohibition by one unset MediaPipe default)
**Learning records:** 🆕 **pelotech/xapi-lrs** · 🆕 **yetanalytics/lrsql** ·
🆕 **adlnet/ADL_LRS** · 🆕 **Larissa** (all Apache-2.0) · 🆕 **DavidLMS/learnmcp-xapi**
(MIT) · 🆕 **jeffyding/OpenLRW** (ECL-2.0 — 🔴 **schema only, dead since 2018**)
**Psychometrics:** 🆕 **joakimwallmark/irtorch** (MIT, 🟢 live) · 🆕 **eribean/girth**,
🆕 **girth_mcmc**, 🆕 **variational-IRT** (MIT, 🔴 all stale ≥4 years)
**Special education:** 🆕 **dg13788/iep-system** (MIT) — 🔴 **one permissive row out of
seven addresses measured; see `agents/top.md` §Special education before quoting this
tier to a client**
**Scheduling:** 🆕 py-fsrs · 🆕 fsrs4anki · 🆕 FSRS (algorithm)
**Credentials:** Learner Credential Wallet
**Curriculum data:** 🆕 **oak-curriculum-ontology** (OGL-3.0 data + MIT code — 🟢 the
only curriculum asset on this base with commercial use and **no** share-alike)
**LMS connectors:** **bruchris/canvas-lms-mcp** · **G36maid/moodle-mcp** ·
**AnonymousOnyx22/canvas-lms-student-mcp** · falkenslab/moodle-mcp ·
🆕 **Yuanpeng-Li/gradescope-mcp** · 🆕 **hughsibbele/Canvas-Agent** ·
🆕 **gabrielmahia/elimu-mcp** (Kenya — 🟡 read its DEMO-data caveat) (all MIT)
**LTI 1.3 libraries:** 🆕 **iamlucasb/lti-core** (TypeScript) · 🆕 **DecoyLex/ltix**
(Elixir) · ltijs · pylti1.3 · CACCL — 🔴 **never** `oat-sa/lib-lti1p3-deep-linking`
(GPL-2.0) or `GSU-CETLOE/lti1p3Library-php` (MIT with no licensor named)
**School administration:** 🆕 **Moha-abshir/SMS** (MIT — 🟡 single-author, Kenya CBC)
**LATAM:** 🆕 **LabSirius/TutorIA** (MIT, Colombia, inside Open edX) ·
🆕 **Riskbreaker2077/open-test** (MIT, offline LAN assessment)
**Lecture capture:** 🆕 **LectureLab** (MIT) · 🟡 the MIT *engines* inside Cap and
CaptureFlow — never their AGPL applications

🟡 **One row on this shortlist is now a school-administration system** —
`Moha-abshir/SMS`, added `p358`. 🔴 **Nothing on it is an institution-wide ERP**, and that
absence is measured, not unexamined — see the ERP note above for why the distinction
decides how a proposal is priced.

Everything else on this shelf is GPL/AGPL/LGPL and should be reached **over a
protocol boundary** — LTI 1.3, web services, or MCP — rather than forked. That
boundary choice is the single most consequential architectural decision in an
education engagement, and it is a licence decision before it is a technical one.
