---
industry: education
region: Global
updated: 2026-10-06
---

# Vertical Platforms — Education

Real, deployed education systems that can be customised and extended with AI —
the equivalent of Odoo for ERP or OpenMRS for healthcare. Licenses read from each
repo's own payload on 2026-10-06.

**Read the license column before you plan the architecture.** Most of the
education platform shelf is copyleft. That is not a blocker, but it decides
whether your AI work is a plugin (and inherits the license) or a side-car (and
does not).

## Learning platforms

| Platform | Repo | License (read from payload) | Position |
|---|---|---|---|
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 (`COPYING.txt`) | Still the most widely deployed and most customisable open source LMS in 2026: 2,000+ plugins, 20-year community. The default incumbent you will meet in an engagement. |
| Open edX | [openedx/edx-platform](https://github.com/openedx/edx-platform) | AGPL-3.0 (`LICENSE`) | Built at Harvard/MIT scale. Strong assessment engine, cohorts, analytics. Used by edX, IBM, Microsoft. Pick it when the cohort is large and assessment is central. |
| Canvas LMS | [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 (`LICENSE`) | Dominant in North American higher ed. Ruby on Rails; needs real Rails operations capability to self-host. Best AI entry point is its API via MCP, not a fork. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 (`LICENSE`) | 30M+ users, unusually strong Spanish-language and LATAM institutional presence. The pragmatic choice for a Spanish-first public-sector deployment. |
| Sakai | [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** (`LICENSE`) | Higher-ed collaboration and learning environment. Educational Community License 2.0 is an Apache-2.0 derivative — **permissive**, and the only copyleft-free option among the traditional big LMSs. Underrated for this reason. |
| ILIAS | [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 (`LICENSE`) | Strong in German-speaking Europe, workplace training and SCORM-heavy compliance training. |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** (`license.txt`) | Modern, fast to deploy via Docker. **Commonly mis-reported as MIT** by LMS comparison articles — it is AGPL-3.0. Verified at `license.txt`; `LICENSE` is a 404, which is how the error spreads. |
| Kolibri | [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) | **MIT** (`LICENSE`) | Offline-first platform for teaching without internet. Default choice for low-connectivity, low-budget and equity-driven deployments. *(Earlier passes called this "the only fully permissive end-to-end platform on this shelf" — no longer true: see Mentingo below, MIT, and Oppia, Apache-2.0.)* |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** (`LICENSE`) | Authoring and delivery of interactive lessons with misconception handling built into the pedagogy. Permissive, and designed for learners with limited educational resources. |
| Mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** (`LICENSE`) | **Added third pass, 2026-10-06 — and it changes the shape of this shelf.** Self-hosted, multi-tenant, white-label LMS with a **built-in AI mentor**, built for corporate L&D, onboarding and compliance rather than academic use. 91★, 29 forks, TypeScript, maintained by Selleo (Poland). The second fully permissive end-to-end platform here and **the only AI-native one**. |
| Coursemology | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`, © 2023 Coursemology.org) | **Added fifth pass, 2026-10-06.** NUS-origin gamified LMS — Rails 8 API, React client, Keycloak auth, **15,802 commits**, 158★, 78 forks. "Currently supported by the AI Centre for Educational Technologies" and the host platform for Singapore's **Codaveri** AI programming tutor. The **third** fully permissive end-to-end platform here, the only one with a decade-scale commit history, and the strongest fit for **CS and programming teaching in higher education**. Read the concentration-risk note below before proposing it. |
| Sunbird | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) | **MIT** (`master/LICENSE`) | **Added sixth pass, 2026-10-06 — found in an earlier pass and never shelved here.** EkStep Foundation's platform, deployed as India's **DIKSHA** national school platform and recognised a **Digital Public Good**. **41★ / 317 forks / 38,046 commits** — a 7.7x forks-to-stars inversion. 18+ languages, NCERT/CBSE/SCERT curricula, 100+ micro-services. The **fourth** fully permissive end-to-end platform here and **the only one proven at nine-figure learner scale**; its 100+ services are the operational cost. Full entry at the end of this file. |

## Content, assessment and delivery components

| Component | Repo | License (read from payload) | Use |
|---|---|---|---|
| Open edX deployment | [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 (`LICENSE.txt`) | The Docker-native way to actually run Open edX. Do not hand-roll an edX deployment. |
| Open edX analytics | [openedx/openedx-aspects](https://github.com/openedx/openedx-aspects) | Apache-2.0 (`LICENSE`) | Learning analytics stack for Open edX — permissive even though the platform is AGPL. |
| H5P | [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 (`LICENSE.txt`) | Interactive content types; embeds in Moodle, Canvas and Drupal. The common currency of interactive exercises. |
| Anki | [ankitects/anki](https://github.com/ankitects/anki) | AGPL-3.0 (`LICENSE`) | Spaced repetition with a mature scheduling algorithm. Reference implementation for retention mechanics. |
| Open Badges validation | [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 (`LICENSE`) | Verifiable credentials and competency claims. |
| LTI 1.3 tool provider | [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 (`LICENSE`) | The permissive integration doorway into any of the copyleft platforms above. |
| Opencast | [opencast/opencast](https://github.com/opencast/opencast) | **ECL-2.0** (`LICENSE`) | Lecture capture and video management, widely deployed in higher ed. Permissive (Apache-2.0 derivative). Integrates with Moodle, Canvas and Sakai. |

## Administrative systems — SIS and education ERP

Added 2026-10-06 (second pass). The learning shelf above is only half the estate.
Admissions, enrolment, fees, attendance, examinations, library and HR run on a
*student information system* or an education ERP, and this is where a large share
of real institutional spend and automation work sits. Licences read from each
repo's own payload.

| Platform | Repo | Licence (read from payload) | Position |
|---|---|---|---|
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** (`LICENSE@master`) | Education ERP on the Odoo framework. Python, v19.0, 884★, 775 forks, 1,710 commits. Admissions, student info, courses, exams, finance, attendance, library, HR. **The licence is the point — see below.** |
| ERPNext | [frappe/erpnext](https://github.com/frappe/erpnext) | **GPL-3.0** (`license.txt@master`) | General ERP with an education module (students, programmes, fees, assessment). Same lowercase-`license.txt` trap as `frappe/lms`: a probe of `LICENSE` returns 404. |
| Gibbon | [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 (`LICENSE@main`) | School management: timetabling, attendance, markbook, pastoral care. Strong K-12 fit. |
| RosarioSIS | [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | **GPL-2.0** (`LICENSE@master`) | Student information system, PHP/PostgreSQL, strong multilingual support including Spanish — relevant to LATAM public sector. GPL-**2.0**, so it is not licence-compatible with GPL-3.0-only code. Check before combining. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (`docs/License.txt@master`) | Student information system: scheduling, grades, attendance, billing. Its licence lives in a **subdirectory**, not at the repo root — see the method note in `repos/foundations.md`. |
| Apache OFBiz | [apache/ofbiz-framework](https://github.com/apache/ofbiz-framework) | **Apache-2.0** (`LICENSE@master`) | Not education-specific, but a genuinely permissive ERP/CRM framework (Java). The fallback when an institution needs admin automation with no copyleft exposure and no Odoo dependency. |

### LGPL-3.0 is the middle path, and it changes the architecture menu

This KB has treated licences as binary: permissive, so build reusable IP; or
copyleft, so build a side-car. OpenEduCat's **LGPL-3.0** is a third position, and
the project chose it deliberately — LGPLv3 lets an institution extend the
platform with **proprietary modules** (an integration with a confidential research
system, licensed third-party content) without being forced to open-source those
modules.

**Consequence:** against an LGPL-3.0 platform, an in-tree-style *module* is a
viable commercial shape. You are not pushed to a side-car to protect your IP the
way Moodle (GPL-3.0) and Canvas/Open edX (AGPL-3.0) push you. Changes to
OpenEduCat's own LGPL files stay LGPL; a separate module linking against it need
not. On the admin side the menu is two options, not one — and OpenEduCat is a
live, maintained platform (884★, 775 forks, v19.0), not a curiosity.

**The boundary still has to be real.** LGPL's distinction between *modifying the
library* and *linking to it* is only as sound as your module boundary. Fork
OpenEduCat's own files and you are in LGPL territory for those files. Keep the
module separate, talk to it through documented interfaces, and the proprietary
part stays proprietary.

## Mentingo — the first MIT, AI-native LMS on this shelf, and what it breaks

Added in the third pass of 2026-10-06. Licence read from payload: **MIT**. It
deserves its own section because three of this KB's standing positions have to be
restated around it.

### Verified specification

| Axis | Value (2026-10-06) |
|---|---|
| Licence | **MIT**, read from `LICENSE`. Its own README states the intent plainly: *"MIT - modify, white-label and resell, no copyleft obligation"* |
| Scale | 91★, 29 forks, TypeScript |
| Maintainer | **Selleo** (Poland) — a product engineering company, building learning platforms since 2005. EMEA-origin |
| Target | Corporate L&D, employee onboarding, compliance training — **not** academic |
| Tenancy | Multi-tenant, white-label |
| AI | Voice **and** chat AI mentor running real-time role-play for sales, compliance and customer-support scenarios, **scored automatically**; automated grading of open-ended behavioural and problem-solving answers with actionable feedback; AI-assisted course generation from existing documentation |
| AI stack | Vercel AI SDK + OpenAI, LangChain, **pgvector** retrieval, **LiveKit** real-time voice, **Langfuse** tracing of every model call |
| LMS core | Course catalogues, lesson delivery, enrolment, learner progression, role-based access (admin / content creator / learner), group-based course-access inheritance, completion records, per-learner analytics, certificates with expiry and recertification |
| Interop | **SCORM 1.2 export**, OpenAPI/Swagger with a generated typed client, CSV and XLSX bulk import/export |
| Runtime | Node.js 22+, PostgreSQL 16 + pgvector, Redis, S3-compatible storage. One-click CloudFormation deployment from AWS Marketplace |

### What it breaks, and what it does not

**1. The licence menu on the platform layer is no longer "copyleft or side-car."**
This KB's central architectural finding — AI built inside a copyleft LMS inherits
that LMS's licence, so prefer the permissive side-car — was derived from Moodle
(GPL-3.0), Canvas and Open edX (AGPL-3.0). Against Mentingo there is no copyleft to
route around: you can fork the platform itself, extend it in TypeScript, brand it
and **resell** it. For an enterprise L&D engagement that is a different commercial
shape from everything else on this shelf, and a stronger one than the side-car,
because the deliverable is the whole product rather than an attachment to someone
else's.

**2. The "no permissive auto-grader" gap is narrowed, not closed.** Mentingo grades
open-ended behavioural and problem-solving answers automatically, under MIT. It
does **not** supply a rubric- or curriculum-aligned academic grader, and it changes
nothing about oversight: EU AI Act Annex III, the Oklahoma and Maryland statutes
and Korea's high-impact classification are indifferent to the licence. Keep the
human gate on consequential scores. See the narrowed gap statement in
`agents/top.md`.

**3. It is an L&D product, so do not mis-sell it into academia.** No SIS
integration, no LTI 1.3, no gradebook semantics for credit-bearing courses, no
institutional reporting. It exports **SCORM 1.2**, which is the L&D interchange
format, not an academic one. The honest framing: *for a corporate client,
Mentingo is a candidate platform; for a university, it is a reference
implementation and a component donor.*

### What to take from it even when you do not deploy it

Two engineering choices generalise to every pattern in this KB:

- **pgvector inside PostgreSQL instead of a separate vector database.** One fewer
  component to host, secure and keep in-region — which matters most in exactly the
  EMEA residency and LATAM cost scenarios where the component budget is tightest.
- **Langfuse tracing from day one.** Per-call cost, latency and actual model output,
  inspectable. This is an EU AI Act Annex III-shaped audit artefact produced as a
  by-product of normal operation rather than assembled as a compliance project.
  Wire it into the side-car patterns too.


## Added in the eighth pass of 2026-10-06 — the offline-first delivery tier, and why it is a platform question

Every platform on this page assumes a network. **The eighth pass found the tier
underneath that assumption**, and it changes the LATAM and MEA architecture
conversation from a feature trade-off into a platform selection.

### The constraint, now with numbers instead of adjectives

`LabSirius/TutorIA`'s requirements specification (**MIT**, Universidad
Tecnológica de Pereira, Colombia — see `agents/top.md`) states the rural-access
envelope as a **testable acceptance criterion**, which no platform page in this
KB previously had:

> **RNF-04** — *"Compatible con dispositivos con mínimo **2GB de RAM**;
> funcional con conectividad de **3G**."*

And it states the governing privacy regime for the same deployment:

> **RNF-05** — *"conforme a la **Ley 1581 de 2012 (Habeas Data)**"*, with
> **TLS** in transit and **AES-256** at rest.

**Use these two lines as the intake questions for any LATAM education platform
selection.** They are citable, institutionally authored, and permissively
licensed.

### The platform answer, which is Kolibri — and the reference implementation, which is new

| System | Repo | Licence (payload) | Role in this tier |
|---|---|---|---|
| **Kolibri** | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** (`master/LICENSE`, © 2021 Learning Equality and other contributors) | **The platform.** Purpose-built for schools with no reliable internet; the only permissive, maintained, genuinely deployed offline-first LMS on this page |
| Kolibri Studio | [learningequality/studio](https://github.com/learningequality/studio) | **MIT** (`master/LICENSE`, Foundation for Learning Equality) | Curriculum authoring and channel curation for Kolibri |
| Kolibri for Android | [learningequality/kolibri-installer-android](https://github.com/learningequality/kolibri-installer-android) | **MIT** (`master/LICENSE`, © 2023) | The 2 GB-RAM delivery target of RNF-04 |
| **EduFlow** | [caiuc/equipo-19-haCAIthon-2026](https://github.com/caiuc/equipo-19-haCAIthon-2026) | **MIT** (© 2026 CAi UC — **holder flagged**, see `agents/top.md`) | **Not a platform — a readable reference implementation** of the offline-sync pattern, 41 commits |
| RACHEL | *path unresolved* | **Unknown — not established** | Cited by EduFlow as prior art alongside Kolibri. **No file resolved on any probe** (`rachelproject/rachelplus`, `rachelproject/RACHELPlus`, `rachelproject/rachel`, `worldpossible/rachelplus` × `main`/`master`), so the canonical location was **not** established and no licence claim is made. Recorded so the next pass starts from the project's own site, not from a guessed repository path |

All three Learning Equality licences were **re-confirmed from payload this
pass**.

### What EduFlow contributes that Kolibri does not

Kolibri is the right platform and it is a large system. **EduFlow is ~41 commits
and shows the mechanism in a form an architect can read in an afternoon:**
teacher opens a room and shares a **6-character code**; the student downloads
the assignment while in signal — **~8 KB for 10 exercises**, because a maths
problem is text — solves it **entirely offline** with immediate correction via
**IndexedDB** plus a **Service Worker** app-shell cache, and answers **sync
automatically** on reconnection. FastAPI + Next.js PWA + Supabase.

Its own problem statement is the sharpest on this page: *"Las plataformas
educativas que existen — Khan Academy, Google Classroom, Kahoot — **asumen
conexión permanente**. En un colegio municipal con internet intermitente eso las
vuelve inservibles."*

### The selection rule this adds to the page

**If the deployment has intermittent connectivity, offline-first is a platform
decision and not a feature you add later.** Retrofitting sync onto a
network-assuming LMS means rebuilding its data layer; choosing Kolibri means
accepting its content model from day one. **Decide this before the LMS
shortlist, not after** — and note that this is the one tier of the education
platform shelf where the permissive option (**Kolibri, MIT**) is also the best
option, which is not true of the LMS tier (Moodle, Chamilo, ILIAS — all
copyleft) or the ERP tier (**OpenEduCat, LGPL-3.0**).

## The Kuali estate — one higher-ed consortium, three different licences

Added in the third pass of 2026-10-06. The admin shelf above was missing the
institutional-grade higher-education option, so this pass probed **Kuali** (formed
2004 on an Andrew W. Mellon Foundation grant, backed by 24+ universities).

| Repo | Product | Licence (read from payload) | Status |
|---|---|---|---|
| [KualiCo/rice](https://github.com/KualiCo/rice) | Kuali Rice — higher-ed application framework and middleware | **ECL-2.0** (`LICENSE.txt`) — **permissive** | 4★, 12 forks, Java. **Maintenance mode** by its own README: maintained for "security, bug fixes, and minor enhancements while its replacements are being developed" |
| [kuali/rice](https://github.com/kuali/rice) | same, older location | **ECL-2.0** (`LICENSE.txt`) | **DEPRECATED** — its README's first line points to `KualiCo/rice`. Pin the KualiCo location |
| [kuali/kfs](https://github.com/kuali/kfs) | Kuali Financial System | **AGPL-3.0** (`LICENSE`) | network copyleft |
| [kuali/kc](https://github.com/kuali/kc) | Kuali Coeus — research administration | **AGPL-3.0** (`license.txt`, lowercase) | network copyleft, **and** the lowercase-`license.txt` trap again |
| `kuali/student`, `KualiCo/student`, `kuali/coeus` | Kuali Student (the SIS) | — | **not reachable**: `README.md` 404s on all three. The SIS is not at the path its name implies |

**Two usable conclusions.**

**ECL-2.0 belongs on your permissive allowlist.** It is the Apache-2.0 text with
the patent grant narrowed to education, and it now appears three times on this
shelf — Sakai, Opencast and Kuali Rice. A licence filter that allowlists only
`MIT / Apache-2.0 / BSD` will **reject three genuinely permissive higher-education
platforms.** Fix the filter, not the finding.

**A consortium is not a licence.** "Kuali is ECL-2.0" is true of Rice and false of
KFS and Coeus. The diligence unit is the repository — never the foundation, the
vendor or the brand. This is the `frappe/lms` (AGPL) beside `frappe/erpnext` (GPL)
lesson, now in its harder form: here the **permissive** member is the one you meet
first in the documentation, so the optimistic reading is the one that sticks.

**And read the maintenance banner before the licence.** Rice is permissive *and*
parked. Permissive-but-parked is a real category: fine to vendor and fork, wrong to
present to a client as a living upstream. Recorded as qualified, not recommended.

## OpenMAIC — a permissive platform that generates the course, not just the tutoring

Added in the fourth pass of 2026-10-06. Every other platform on this shelf is a
**container** for content a human authored (Moodle, Canvas, Open edX, Mentingo).
[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) is the first entry that
**produces the content itself**, which puts it in a different column of the
selection table rather than in competition with the LMSs.

### Verified specification

| Axis | Value (read 2026-10-06) |
|---|---|
| Repo | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) |
| Licence | **MIT**, read from the `LICENSE` payload (© 2026 THU-MAIC) |
| Stars | **40.0k** — the largest permissive asset in this KB |
| Origin | **Tsinghua University** (THU-MAIC) |
| Version | **v1.2.0-rc.1**, pre-release, 2026-10-04 |
| Stack | TypeScript, Next.js, React, **PostgreSQL** |
| Input | a topic description, or an uploaded document |
| Output | slides, quizzes, interactive **HTML simulations**, project-based-learning scenes; **exports PPTX and interactive HTML** |
| Delivery | **AI teacher agent + AI classmate agents**, shared whiteboard, text-to-speech |
| Integration | exposed to agent workbenches (OpenClaw) — generate a classroom from a chat client or IDE |

### Why the v1.2.0 architecture change is the part that matters commercially

v1.2.0 moves generation **server-first with PostgreSQL persistence**, so a course
build **survives a closed browser tab or a server restart.** Everything else on
the agent shelf in this KB generates in-session.

Three consequences:

1. **It is the only generator here you can put behind a review queue without
   rebuilding its execution model.** A durable server-side job is already the right
   shape for the `WAITING_REVIEW` gate that trend 16 and the EU AI Act both
   require. Pattern **P11** does exactly this.
2. **PPTX and HTML export means the artefact outlives the platform.** A district
   that will not host a Chinese-origin application can still take the deck. That
   makes a **generate-then-export** engagement viable where a deployment is not.
3. **It composes with, rather than replaces, the LMS shelf.** OpenMAIC authors;
   Moodle, Canvas or Open edX deliver and record. Wire them with the MCP servers
   already catalogued in `agents/top.md`.

### The one thing to settle in week one

**It is MIT, and it is Chinese-origin.** The licence is clean and permissive —
there is no legal obstacle. But a public-sector buyer in EMEA or North America
will ask about provenance and data residency, and the honest answer is that
**generation is server-side**, so where that server runs is a decision, not a
default. Self-host it, pin a **reviewed fork**, and point inference at whatever
model the client's data-residency posture allows (the KB's sovereign and local
inference options apply unchanged). Raise this yourself in week one; do not let a
procurement reviewer raise it in week eight.

## AI integration surfaces, by strategy

Two ways to put AI on a platform, with different license outcomes:

**In-tree plugin — inherits the host license.** All three Moodle AI plugins
probed this pass are GPL-3.0: [moodle-block_openai_chat](https://github.com/Limekiller/moodle-block_openai_chat),
[moodle-local_aiquestions](https://github.com/yedidiaklein/moodle-local_aiquestions),
[moodle-qbank_genai](https://github.com/cgrevisse/moodle-qbank_genai). Use these
as references and as drop-in capability for a single client; do not use them as
the base of reusable studio IP.

**External side-car over MCP or LTI — stays permissive.**
[peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) (MIT)
and [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) (MIT,
102 tools, 8 agent skills, WCAG scanner) reach the same data from outside the
tree and keep their permissive license. This is the recommended shape for
anything Globant intends to reuse across engagements.

## Platform selection shortcut

| If the client… | Start from |
|---|---|
| already runs an LMS (most of them) | leave it alone; integrate via MCP / LTI 1.3 side-car |
| needs permissive IP with no copyleft exposure | Sakai (ECL-2.0), Oppia (Apache-2.0) or Kolibri (MIT) |
| has low or intermittent connectivity | Kolibri + ricecooker, fully MIT |
| is Spanish-first public sector in LATAM | Chamilo (GPL-3.0) — deployment and localisation work |
| needs assessment at cohort scale | Open edX via Tutor, plus openedx-aspects for analytics |
| is a Microsoft-stack enterprise L&D buyer | Moodle or Frappe LMS with a MAF-based side-car |
| needs admin/SIS automation (admissions, fees, exams) | OpenEduCat (LGPL-3.0) — and a proprietary module is a legitimate shape here |
| needs admin automation with zero copyleft exposure | Apache OFBiz (Apache-2.0) |
| is Spanish-first K-12 public sector needing an SIS | RosarioSIS (GPL-2.0) — note GPL-2.0, not 3.0 |
| is a corporate L&D / onboarding / compliance-training buyer | **Mentingo (MIT)** — fork it, white-label it, resell it; no copyleft to route around |
| needs permissive higher-ed middleware / workflow | Kuali Rice (**ECL-2.0**) at `KualiCo/rice` — permissive, but in maintenance mode |
| needs spaced-repetition / retention mechanics reached by an agent | `ankimcp/anki-mcp-server` (MIT, 53 tools) over Anki, or OpenTutor (MIT) for FSRS built in |
| needs a whole course generated from documents, not just a tutor | **OpenMAIC (MIT, 40.0k★)** — self-host a reviewed fork; put the gate of pattern P11 in front of it |
| needs generated teaching material but cannot host the generator | **OpenMAIC's PPTX / interactive-HTML export** — generate outside, deliver the artefact in the client's own LMS |
| needs to choose *which model* should teach | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT) — scores pedagogical knowledge, not task accuracy |
| teaches **programming or CS** in higher ed and wants to own the platform | **Coursemology (MIT)** — autograded assignments, gamification, 15,802 commits; accept the 158★ concentration risk, see below |
| needs teacher-side lesson plans and question banks, not a student tutor | **[microsoft/shiksha-copilot](https://github.com/microsoft/shiksha-copilot) (MIT)** — curriculum → lesson plan + assessments → DOCX/PPT/handouts, with a human-curator ingestion gate |
| is **CBSE/NCERT**-aligned and model-sovereignty constrained | **[Naitik-xd/CurriculumCraft-AI](https://github.com/Naitik-xd/CurriculumCraft-AI) (MIT)** — grades 9–12 on open-weight Gemma only; reuse its synthetic-generation copyright argument either way |
| must evidence **EU AI Act** conformity for an education system | **[AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) (MIT)** + an Annex III point 3 profile you write — pattern **P13** |

## Coursemology — the third permissive platform, and the first with a long commit history

**Added in the fifth pass of 2026-10-06.** Found by institution-first search, not
by topic page or star ranking, which is why four earlier passes missed it.

### Verified specification

| Axis | Value |
|---|---|
| Repo | [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) |
| Licence | **MIT**, read from `master/LICENSE` (© 2023 Coursemology.org). `main/LICENSE` is a 404 — the default branch is `master` |
| Scale | 158★, 78 forks, **15,802 commits** |
| Stack | Rails 8.0.5.1 API + React client + **Keycloak** authentication — three components, not one |
| Origin | National University of Singapore; Prof Ben Leong, NUS Computing |
| Current backing | "Currently supported by the **AI Centre for Educational Technologies**" (AICET) |
| AI today | **Codaveri**, AICET's personalised programming tutor, is deployed on coursemology.org — 30,000+ pieces of personalised feedback since 2024. **Codaveri itself is closed source** |
| Design centre | Gamified learning: autograded programming assignments, achievements, levels, experience points |

### Why it matters commercially

It resolves a tension that has run through this whole shelf. Every mature,
widely-deployed LMS here is GPL-family — Moodle, Open edX, Canvas, Chamilo,
ILIAS, Frappe LMS. Every permissive one has been either young (Mentingo, 91★),
offline-specialised (Kolibri) or authoring-focused (Oppia). Coursemology is the
first that is **both permissive and long-lived**: a client can fork it, rebrand
it, embed proprietary modules and resell it, with a codebase that has over
fifteen thousand commits behind it.

For a **programming or computer-science teaching** engagement it is the strongest
fit on this shelf, because that is what it was built for: the autograder,
submission handling and gamification are native, not bolted on.

### The risk, stated plainly

**158★ is a small contributor base for a platform of this size, and maintenance
is realistically NUS-dependent.** You are trading a copyleft obligation for a
concentration risk. Size that trade explicitly in week one:

- Will the client's own engineers maintain the fork? If not, Coursemology is the
  wrong answer and Moodle is the right one.
- Does the engagement need a plugin ecosystem? Moodle's 2,000+ plugins have no
  equivalent here.
- Is the Keycloak dependency compatible with the client's identity estate? This is
  not a single-container deployment.

### What AICET tells you about the AI layer

AICET's three products — **Codaveri** (programming tutor, 30,000+ feedback items
since 2024), **Softmark** (exam-script digitisation and concurrent team marking,
70,000+ scripts in 2025, now grouping similar answers with computer vision) and
**ScholAIstic** (multi-agent platform letting educators author their own
specialised chatbots; deployed in Social Work, Law and Nursing at NUS since June
2024) — are **all closed source**, all funded by Singapore's Smart Nation and
Digital Government Office, and all working with the **Ministry of Education**.

Two things follow:

1. **The reference architecture is validated and the implementation is not
   available.** A ministry-scale deployment of exactly the shapes this KB
   recommends — side-car tutor on an open LMS (P1), gated grading (P11),
   educator-authored agents (P8) — exists, works at 70,000-script scale, and
   cannot be forked. Cite it as proof the shape works; build the shape yourself.
2. **ScholAIstic is the most interesting of the three to replicate.** Educators
   authoring their own roleplay chatbots for professional-skills training, scaled
   across unrelated faculties, is a product shape with no permissive equivalent
   anywhere in this KB. Pattern **P8** (course materials → Agent Skills) is the
   closest thing here, and it stops short of letting a non-technical educator
   author and publish one.

## Sunbird — the fourth permissive platform, and the only one at nine-figure scale

Promoted to this file in the sixth pass of 2026-10-06. **It was found in an
earlier pass, recorded in `repos/trending.md`, and never shelved here** — so five
rebuilds of this file presented Moodle, Open edX, Canvas, Mentingo, OpenMAIC and
Coursemology without it. The filing failure is written up in `repos/trending.md`,
sixth pass, Finding 1.

### Verified specification

| Field | Value |
|---|---|
| Repo | [Sunbird-Ed/SunbirdEd-portal](https://github.com/Sunbird-Ed/SunbirdEd-portal) |
| Licence | **MIT**, read from `master/LICENSE` |
| Signals | **41★ · 317 forks · 38,046 commits** · not archived |
| Built by | **EkStep Foundation** (India) |
| Deployed as | **DIKSHA** — India's national school-education platform, run with NCERT/CIET |
| Status | **Digital Public Good**, recognised by the Digital Public Goods Alliance |
| Scale | README mission: *"improve learning outcomes for 200 million children across India"* |
| Localisation | **18+ languages**; **NCERT, CBSE and SCERT** curricula |
| Architecture | **100+ micro-services** offered as building blocks, not a monolith |

### Why it belongs on the shortlist

**It is the only platform on this shelf that is simultaneously MIT and proven at
national scale.** Coursemology's 15,802 commits made it this KB's "permissive LMS
with real history"; Sunbird has **38,046** and a deployment measured in hundreds
of millions of learners. For a ministry, state or large-system engagement, that
combination — permissive licence, DPG status, curriculum alignment already built,
multilingual by construction — is the strongest commercial position in this file.

**The forks-to-stars inversion is the signal to read.** 41 stars against **317
forks** is **7.7×**, the pattern an earlier pass established for infrastructure
that people deploy rather than admire. Judged on stars, Sunbird looks like a
hobby project; judged on forks and commits, it is the most-deployed platform here.

**It pairs directly with the sixth pass's language shelf.** Sunbird is already
18-language; `AI4Bharat/IndicTrans2` (MIT, 22 scheduled languages),
`Indic-TTS` (MIT, 13 languages) and `IndicWav2Vec` (MIT, ASR) are all MIT and all
from IIT Madras. **A Sunbird deployment and its language layer can be assembled
entirely from MIT components** — the only place in this KB where that is true of a
whole stack. See `repos/foundations.md` and pattern **P16**.

### The risks, stated plainly

- **The micro-service count is the cost.** 100+ services is an operations
  commitment, not a convenience. Scope the DevOps work explicitly; the
  `project-sunbird/sunbird-devops` repository (MIT, 62★ / 392 forks) exists
  precisely because this is the hard part.
- **It is built around Indian curricular structures.** NCERT/CBSE/SCERT alignment
  is a feature in APAC and **work to be undone** elsewhere. Do not propose it for a
  North America or EMEA engagement as a drop-in; propose Coursemology or Mentingo
  there.
- **41 stars means a thin public community relative to its scale.** Expect
  institutional documentation and ministry-grade deployment guides rather than
  Stack Overflow answers. Budget for reading source.

## Added in the seventh pass of 2026-10-06 — the Fedena question, closed properly

Earlier passes left this open, and it is worth closing because **Fedena is one of
the names a client will raise** when asked about open source school ERP: a
secondary source calls `projectfedena/fedena` *"the official GitHub repository"*
and attributes **Apache-2.0** to it, while the probe of that owner returned
nothing. This pass enumerated the owners.

| Owner | Does the tree resolve? | Licence payload |
|---|---|---|
| `projectfedena/fedena` — the "official" org per the secondary source | **No.** 404 on `README.md`/`readme.md` and on five licence filenames, across `main` and `master` | None readable |
| [`foradian/fedena`](https://github.com/foradian/fedena) — **Foradian, the vendor that built Fedena** | **Yes.** `README.md` 404s on every branch, but `master/config/routes.rb` and `master/Gemfile` return **200** — the Rails tree is there | **None.** 7 licence filenames probed across 8 branches |
| [`mazhar266/fedena`](https://github.com/mazhar266/fedena) — mirror, 5★ | **Yes**, on `master` only (`main` 404s) | **Apache-2.0 at `master/LICENSE.md`** — and `master/LICENSE` is **404** — plus `master/NOTICE`: *"Fedena — Copyright 2011 Foradian Technologies Private Limited"* |

**The answer, and it is more favourable than the earlier passes could show.** The
grant is **Apache-2.0 and it is the vendor's own**: the `NOTICE` file in the
mirror names **Foradian Technologies Private Limited** as the copyright holder,
and Apache-2.0 §4(d) is precisely the clause that requires that NOTICE to travel
with redistributions. So this is not a third party attaching a licence to someone
else's code — **it is Foradian's Apache-2.0 release, preserved in a mirror while
the vendor's own current GitHub org no longer carries the file.**

**What to do with it.** Fedena is usable under Apache-2.0. Vendor
`mazhar266/fedena@master`, record the commit SHA, and **keep copies of both
`LICENSE.md` and `NOTICE`** as read — the NOTICE is the part that makes the
provenance argument, and Apache-2.0 obliges you to carry it anyway. For a
*greenfield* engagement still prefer
[OpenEduCat](https://github.com/openeducat/openeducat_erp) (LGPL-3.0, 73+
modules): not because Fedena's licence is weak, but because an actively
maintained platform with a live upstream beats a 2011-era Rails codebase whose
grant survives only in a mirror. Choose Fedena when a client is already on it.

### Two method notes, and the first one is a correction to this pass

**1. A one-filename probe produces a false negative.** This pass initially read
`master/LICENSE` for the mirror, got **404**, and briefly concluded the grant had
gone. It had not — it is at **`LICENSE.md`**. The KB's standing discipline is a
filename *sweep* (this pass used 6–9 names across 2–8 branches) and the moment it
was shortcut to a single `curl`, it produced exactly the kind of confident
denial the third pass's `OpenTutor` correction warned about. **A 404 on one
filename is evidence about that filename.** Recorded here rather than quietly
fixed, because the near-miss is the useful part.

**2. Enumerate owners in both directions.** The third pass learned that a 404 on
one owner is not evidence about a project — a wrong withdrawal destroyed a true
finding. Fedena shows the same enumeration cutting the other way: **the "official"
org and the original vendor both carry no grant, and the mirror carries the
vendor's own.** Both errors come from treating `owner/name` as the project.
Enumerate the owners, read the NOTICE, then decide.

## The OER content layer — one row, and the licence is correct for the artefact

Net new to this KB in the seventh pass.

| Asset | Licence (payload) | ★ | Use |
|---|---|---|---|
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | **CC BY 4.0** (`main/LICENSE`, "Attribution 4.0 International") | ~392k | A curated index of free programming books and courses across many languages. **Content for enablement (P6), cited — never a dependency** |

**Why it is shelved here rather than rejected.** CC BY 4.0 is attribution-only:
no non-commercial clause, no share-alike. The *material* is therefore usable in a
commercial curriculum provided attribution travels with it. It is not a software
licence — and there is no software here to license, only a reading list.

**The contrast worth keeping.** This KB's fifth pass found that pedagogy
evaluation is *"published as research and licensed as content"* and treated that
as a defect — correctly, because a benchmark harness under CC BY-SA is code you
cannot vendor. Here the content licence is **right**, because the artefact really
is content. **Judge the licence against the artefact, not against a preference
ordering of licences.** A reading list under CC BY is well licensed; an
evaluation harness under CC BY is mis-licensed. Same licence, opposite verdict.
