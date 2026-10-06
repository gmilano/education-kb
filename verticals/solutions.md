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
| RACHEL | [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **CC BY-SA-NC — README only, no payload** | **RESOLVED in the ninth pass, and it is NOT shippable.** The org is `rachelproject`; `contentshell` *is* the RACHEL CMS. No licence payload across 8 filenames × 2 branches; the README declares *"Creative Commons - BY, SA, NC"* — a content licence over PHP software, carrying **NonCommercial**. Cite as prior art, never ship. See the ninth-pass section below |

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

## What the permissive platforms install — twenty-first pass of 2026-10-06

⚠️ **This file's job is to say which platforms can be customised with AI on top. That recommendation
has always rested on the platform's own licence. For the two permissive platforms measured this pass,
the platform's licence is not the whole answer.**

Measured first-hand from PyPI on 2026-10-06, depth 1. Instrument:
`compose/code/dependency-licence-closure/`.

| Platform | Platform licence | Direct deps | Closure verdict | What a deployment has to decide |
|---|---|---|---|---|
| **Oppia** | Apache-2.0 | **152** | 🔴 **REVIEW-STRONG** | `mutagen` is **`GPL-2.0-or-later`** (audio metadata). Clear that one path, or drop the feature that reaches it. 148 of 152 deps are clean |
| **Kolibri** | MIT | **32** | ⚠️ **REVIEW-WEAK** | 2 LGPL (`json-schema-validator`, `zeroconf-py2compat`) — linkable, shippable, but they travel with the offline bundle |
| **Mentingo** | MIT | **not measured** | ⚠️ **UNMEASURED** | pnpm **workspace root**: its root manifest carries only `devDependencies`, so the runtime closure is in `apps/*` and this pass did not reach it. ⚠️ **Unmeasured is not clean** |

🔵 **Why this belongs in the verticals file and not only in the agents file.** The copyleft platforms
here — Moodle GPL-3.0, Open edX and Canvas AGPL-3.0 — are *already* copyleft, so this KB's standing
advice is to keep Globant IP in an external side-car over LTI 1.3 or MCP. That advice is unchanged.
🔴 **What changes is the advice for the permissive platforms**, which were the escape hatch: *"pick
Kolibri or Oppia and you avoid the copyleft question entirely"* was the shortcut, and at depth 1 it is
**not quite true for either of them**. The escape hatch is still the right call — the obligations are
narrow and attach to specific features — but it is **narrow, not absent**, and a proposal that
promised "no copyleft anywhere" on an Oppia build would have been wrong.

⚠️ **Limits, so the table is not over-read:** depth 1 only (transitive deps unmeasured), linkage not
analysed, and `REVIEW-*` means *"look at this row"*, not *"violation"*. The one hard class,
`BLOCKER` (a non-commercial grant), **was not triggered by any platform on this shelf.**

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

## Added in the ninth pass of 2026-10-06 — RACHEL closed, and a ministry's estate as the public-sector reference

### RACHEL, resolved: the answer is NonCommercial

The eighth pass left RACHEL as *"path unresolved, no licence claim made."*
Starting from the project rather than a guessed path, the org is
**`rachelproject`** and the verdict is settled:

| System | Repo | Payload probe | Stated grant | Verdict |
|---|---|---|---|---|
| **RACHEL** (the CMS) | [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **none** — `LICENSE{,.md,.txt}`, `LICENCE{,.md,.txt}`, `COPYING`, `COPYRIGHT` × `main`/`master` | README: *"Creative Commons - BY, SA, NC"* | ❌ **NonCommercial on the software — not shippable** |
| RACHEL module template | [rachelproject/module-template](https://github.com/rachelproject/module-template) | **none** — same sweep | none found | ❌ no grant |

`contentshell` is RACHEL itself: *"The RACHEL Content Management System"*, the PHP
that serves and manages content on RACHEL devices (as of 2024, chiefly RACHEL 5).
Its only grant statement is a **content licence applied to software, carrying
NonCommercial**, with no payload to weigh against it.

**Why this is a platform finding and not just a licence note.** RACHEL's README
names its own dependency set: ZIM modules need **Kiwix**, and other modules need
**KA-Lite**, **Kolibri** or **Moodle**. So RACHEL is a *shell* over software this
page already shelves — and the shell is the one layer you cannot ship. Underneath
it, payload-verified this pass: `kiwix/kiwix-tools`, `kiwix/libkiwix` and
`kiwix/kiwix-android` are **GPL-3.0**, `openzim/libzim` is **GPL-2.0**, and
`learningequality/kolibri` is **MIT**.

**The selection rule the eighth pass wrote is unchanged, and now it has a
reason.** Kolibri was recommended on an absence of evidence about RACHEL; it is
now recommended on evidence. **Ship Kolibri. Cite RACHEL as prior art for
offline delivery in the proposal, and never as a component.** If offline
Wikipedia-class content is in scope, run **Kiwix as a separate process behind an
HTTP boundary** — the same side-car reasoning this page applies to MCP — so the
GPL obligation stays with Kiwix and off the client's codebase.

### The public-sector reference estate — UK Department for Education, MIT

New tier on this page. `DFE-Digital` is the UK Department for Education's
engineering org, and it operates **live national education services** in the open
under MIT (licences read from payload; full table and star counts in
`repos/foundations.md`):

| Service | Repo | Licence | What it is |
|---|---|---|---|
| Apply for teacher training | [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** | The national ITT application service |
| Teaching Vacancies | [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | National teaching job-listing service |
| Publish teacher training | [DFE-Digital/publish-teacher-training](https://github.com/DFE-Digital/publish-teacher-training) | **MIT** | Provider course publishing + candidate discovery |
| Register trainee teachers | [DFE-Digital/register-trainee-teachers](https://github.com/DFE-Digital/register-trainee-teachers) | **MIT** | Trainee registration for ITT placements |
| GIAS | [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** | The authoritative national schools register |
| Benchmarking & insights | [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** | School-to-peer-group metric comparison |

**Where this sits in the platform menu.** It is **not an LMS and not an SIS** —
it is the **administrative and workflow tier** of a national education system:
recruitment, registration, course publication, school registry, benchmarking.
Nothing here replaces Moodle, Kolibri, OpenEduCat or Kuali. What it provides is a
**reference estate**: a working, readable, permissively licensed implementation
of education workflow at country scale, maintained by a state.

**Three concrete uses in an engagement:**

1. **Public-sector proposals in EMEA.** The ministry question is always *"can we
   own, audit and exit this?"*. An MIT licence from a peer ministry is the
   strongest available answer, and it is a precedent rather than an argument.
2. **Domain models you will meet anyway.** GIAS and the ITT services encode the
   UK schools and teacher-training data model. Any UK engagement integrates with
   these; here they are, readable and reusable.
3. **The grounding layer for a reporting agent.**
   `education-benchmarking-and-insights` already does peer-group comparison —
   the data tier under any "how is my school performing" question, which is the
   natural thing to put an agent in front of.

**The asymmetry to lead with.** The DfE's administrative tier is production-grade
and MIT; its **AI** tier is five prototypes at **0–1★ with no licence payload**
(`rsd-ai-libs`, `sts-ai-support`, `ai-briefing-tool-prototype`,
`rsd-common-ai-services` — see `repos/foundations.md` for the rejections). One of
them, `rsd-ai-libs`, describes *"building and evaluating Azure AI Foundry agents
with guardrails, Azure AI Search, and **MCP server support**"* — a ministry
independently arriving at this KB's MCP side-car pattern, and leaving it
unlicensed at zero stars.

So the public-sector pitch is not *"you need a platform."* They built one. It is:
**"your administrative layer is a licensed national asset and your AI layer is
unlicensed prototypes — let us build the second on top of the first, under a
licence you already use."**

**Star-count warning specific to this tier.** These repositories sit at **5–38★**
because government services are *consumed*, not forked. On this page that is the
one place where low stars do **not** indicate low maturity — the opposite of the
reading this KB applies everywhere else, and the opposite of the trap in
`agents/top.md` where a 72★ repository turned out to be the ungranted one.

## Added in the tenth pass of 2026-10-06 — the integration tier is a scored line item, not plumbing

Every section above this one picks a **platform**. This one is about the layer
between the platform and whatever Globant builds on top of it, and it is here
because of a procurement number rather than a technology trend.

**CoSN: 39% of districts score interoperability in their RFP rubrics** (Tier 2,
corroborated, recorded in the ninth pass). A third of the North American K-12
buying market **assigns points** to how well a system exchanges roster and
activity data. That moves the integration layer out of the implementation plan and
into the bid.

### The standards, and which ones actually have permissive implementations

| Standard | What it carries | Permissive implementation shelf (payload-verified, tenth pass) |
|---|---|---|
| **LTI 1.3** (1EdTech) | Launching an external tool from inside an LMS, with identity and context | **Four**, across four runtimes — see below |
| **OneRoster 1.1 / 1.2** (1EdTech) | Rosters: orgs, schools, students, teachers, terms, enrolments | **One** (.NET), **rostering only** |
| **Caliper Analytics** (1EdTech) | Learning activity event streams | **None found on a permissive licence this pass** — and the search term is a homonym trap |
| **QTI** (1EdTech) | Assessment item and test interchange | Not swept this pass |

The runtime split for LTI 1.3 and OneRoster, with licences read from payload:

| Runtime | Repo | License |
|---|---|---|
| Node / TypeScript | [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) (373★) | Apache-2.0 |
| PHP (Moodle-side) | [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) (124★) | Apache-2.0 |
| Java / Spring Boot | [Unicon/tool13demo](https://github.com/Unicon/tool13demo) (27★) | Apache-2.0 |
| Java / Spring Security | [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) (25★) | Apache-2.0 |
| .NET | [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) (6★) | MIT |
| **Python** | **none found** | — |

### What this adds to platform selection

1. **The LMS choice now implies the integration runtime.** Moodle pulls toward the
   1EdTech PHP library; a Spring estate pulls toward `oxctl` or `Unicon`; a Node
   AI service pulls toward `ltijs`. That is a decision to make in week one
   alongside the platform, not after it.
2. **Python is where the AI layer lives, and there is no Python LTI 1.3 library
   here.** So the realistic shape is: tutoring/agent service in Python, LTI
   adapter in Node, PHP or the JVM, talking to each other over an internal API.
   **Budget for the adapter as a component**, and say so in the bid rather than
   discovering it in integration testing.
3. **OneRoster.NET does rostering only — the gradebook is not implemented.** If
   the rubric scores grade passback, this shelf does not cover it and the honest
   answer is a custom build against the spec.
4. **Caliper has no permissive implementation on this shelf, and the word is a
   trap.** `OneRoster OR Caliper OR "LTI 1.3" license:apache-2.0` returns **184
   repositories** dominated by `google/caliper` (deprecated Java
   micro-benchmarking, 818★) and `hyperledger-caliper/caliper` (blockchain
   benchmarking, 708★). If an RFP scores learning-analytics event streams, treat
   it as a build, not a selection.
5. **Pin `theopenem/OneRoster.NET`, not the identical copy.**
   [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) is also MIT and
   byte-identical (same `README.md` md5, same licence text, **same `theopenem`
   copyright holder**). One asset, two addresses.

### The offline-first stack gains its missing layer

The eighth pass made **Kolibri** the platform answer for offline-first delivery.
What it did not record is the component that makes the synchronisation work:
[learningequality/morango](https://github.com/learningequality/morango) — **MIT**,
15★, a pure-Python **peer-to-peer database replication engine for Django** with
**certificate-based authentication**, change tracking and data partitioning built
for low-bandwidth links, on SQLite or PostgreSQL.

This matters for platform selection because it is **separable**. A client who
needs offline-tolerant sync for an existing Django system does not have to adopt
Kolibri to get it — morango is usable on its own, under MIT. That is a smaller,
faster engagement than a platform migration, and it is now on the shelf.

**One warning inside the same organisation:**
[kolibri-design-system](https://github.com/learningequality/kolibri-design-system)
and [kolibri-server](https://github.com/learningequality/kolibri-server) returned
**no licence payload** under any of 20 probed URLs. Kolibri itself, `morango`,
`le-utils`, `studio` and `ricecooker` are MIT, read from payload. **The
organisation's posture does not license its repositories** — probe each one.

## Added in the eleventh pass of 2026-10-06 — nine platforms recovered from this repository's own archive, re-verified on their real default branch

All nine addresses below sit in `archive/2026-10-06-pre-reset/` and were dropped by
this repository's reset earlier on 2026-10-06 (172 real addresses lost; the audit is
in `repos/trending.md`). Each licence was re-read this pass from the repository's
payload, **on the branch the GitHub API reports as `default_branch`** — not a guessed
`main`/`master` pair, which is what made two of these look ungranted.

### The permissive end — what Globant can customise and redistribute

| Platform | Repo | Licence (read from payload) | ★ / forks | What it is, and what AI goes on top |
|---|---|---|---|---|
| **OpenOLAT** | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) (`master`) | ✅ **Apache-2.0** | 446 / 166 | Full Swiss LMS: course authoring, **assessment**, curriculum management, QTI, SCORM, lecture and roll-call. Java. Pushed 2026-10-06. **The most permissively licensed complete LMS in this KB** — Moodle is GPL-3.0 and Open edX is AGPL-3.0, so OpenOLAT is the only one you can extend without the copyleft conversation. AI layer: QTI item generation, assessment scoring, curriculum-gap analysis. |
| **Richie** | [openfun/richie](https://github.com/openfun/richie) (`master`) | ✅ **MIT** | 316 / 95 | Django CMS purpose-built for **education portals** — course catalogue, programmes, organisations, teacher pages — designed to sit *in front of* Open edX or Moodle rather than replace them. From **France Université Numérique**. AI layer: catalogue search, programme recommendation, multilingual course descriptions. **MIT at the portal tier is the cleanest place to put client-visible AI**, because the copyleft lives behind it in the LMS. |
| **Sunbird** | [project-sunbird/sunbird-lms-mw](https://github.com/project-sunbird/sunbird-lms-mw) · [sunbird-analytics](https://github.com/project-sunbird/sunbird-analytics) (`master`) | ✅ **MIT** | 6 / **41** · 3 / 28 | The stack under **India's DIKSHA** national platform: LMS middleware plus a learning-analytics framework. **The most permissive national-tier education stack this KB has recorded.** ⚠️ **Dormant** — middleware last touched 2024-08-30, analytics 2023-02-08, and `sunbird-learning-platform-devops` is **archived**. Forks (41) exceeding stars (6) is the signature of infrastructure that is *deployed* rather than starred. **Use as a licence-clean reference architecture; do not expect upstream patches.** |
| **Ed-Fi ODS/API** | [Ed-Fi-Alliance-OSS/Ed-Fi-ODS](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) (`main`) | ✅ **Apache-2.0** (`LICENSE.txt`) | 28 / 47 | Reference implementation of the **Ed-Fi** US K-12 data standard: an operational data store plus a REST API over a shared student-data model. C#. **The data tier a North American district RFP assumes you already speak** — see trend 26 and P24. AI layer: early-warning models, intervention targeting, anything that needs cross-system student records without a bespoke integration per source. |
| **OpenTutor** | [LEARNableLabs/opentutor](https://github.com/LEARNableLabs/opentutor) (`main`) | ✅ **MIT** | 0 / 0 | *"Compounding Deliberate Curiosity."* JavaScript, 72 open issues, created 2026-02-28, pushed 2026-10-02. **Measured at 0★.** Noted precisely because earlier KB cycles recorded an "OpenTutor" at ~900★ — **a different project of the same name.** Treated here as an early-stage MIT asset, not as an established platform. |

### The copyleft end — real platforms, and the clause decides the engagement

| Platform | Repo | Licence (read from payload) | ★ / forks | The delivery constraint, stated plainly |
|---|---|---|---|---|
| **LearnHouse** | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) (**`dev`**) | 🔴 **AGPL-3.0** | **2,320** / 564 | *"The next-gen open source learning platform for everyone."* Python + React, headless, explicitly AI-native. Pushed 2026-10-06 — the most actively developed AGPL platform here. ⚠️ **Network clause**: hosting a modified LearnHouse for a client triggers the obligation to offer the modified source **to its users**. Viable where the client accepts an open deliverable; fatal where they expect proprietary differentiation. ⚠️ Default branch is **`dev`**. |
| **CourseLit** | [codelitdev/courselit](https://github.com/codelitdev/courselit) (`main`) | 🔴 **AGPL-3.0** (`LICENSE.md`) | **1,269** / 260 | Course sales, digital downloads and blogging on a branded site — the open alternative to Teachable/Thinkific/Podia. TypeScript. Same network clause as above. **The right base for a client whose product *is* the open platform**, wrong for one reselling it. |
| **i-educar** | [portabilis/i-educar](https://github.com/portabilis/i-educar) (**`2.12`**) | 🔴 **GPL-2.0** (*"Version 2, June 1991"*) | **718** / **547** | *"O maior software livre de educação do Brasil."* A full school-management/SIS platform — enrolment, attendance, grades — Laravel/PHP, tagged `software-publico`. **The only genuine LATAM-origin education platform in this KB**, and with 547 forks it is the most-forked platform on these shelves. GPL-2.0 is **no network clause**: hosting a modified i-educar for a Brazilian municipality triggers nothing; **distributing** a modified binary or source does. For public-sector LATAM work, where the client often *wants* the source, this is close to ideal. ⚠️ Default branch is the version number **`2.12`**; `main` serves nothing, which is why a `main`+`master` probe reports this platform as ungranted. |
| **Obojobo** | [ucfopen/Obojobo](https://github.com/ucfopen/Obojobo) (`master`) | 🔴 **AGPL-3.0** | 72 / 35 | Next-generation course content delivered into an LMS over LTI. React + SlateJS. From the **University of Central Florida**. |
| **Materia** | [ucfopen/Materia](https://github.com/ucfopen/Materia) (`master`) | 🔴 **AGPL-3.0** | 52 / 41 | Embeddable learning widgets and educational games for LMS courses, also LTI-delivered. Same organisation; note that UCF's own LTI **template** (`cookiecutter-python-lti`) is **MIT** while its *applications* are AGPL-3.0. **An organisation's licence posture is not uniform across its repositories** — probe each one. |
| **OpenEMIS** | [openemis/core](https://github.com/openemis/core) (`main`) | 🔴 **GPL** — **version not read this pass** | — | Education management information system deployed at ministry tier. Recorded with the licence version explicitly open rather than guessed; resolve before it enters a proposal. |

### What this table changes about platform selection

The KB's standing advice has been Moodle (GPL-3.0) or Open edX (AGPL-3.0) with AI on
top. Two corrections:

1. **If copyleft is the blocker, the answer is OpenOLAT, not a negotiation.**
   Apache-2.0, 446★, full assessment and curriculum management, pushed the day of
   this pass. It has been absent from this KB's live files since the reset.
2. **If the engagement is LATAM public sector, i-educar's GPL-2.0 is a feature.**
   No network clause, 547 forks, Brazilian, already classified as `software-publico`.
   The licence that blocks a SaaS product is the licence a municipality asks for.

And one procurement note that spans both tables: **the portal tier is where
permissive licences survive.** Richie (MIT) in front, a copyleft LMS behind, and the
AI in the MIT layer — that is the pattern that lets a client keep what they paid for
without anyone misreading a clause.

## Added in the twelfth pass of 2026-10-06 — nine more platforms off the archive, on their real default branch

Branches from `git ls-remote --symref … HEAD`; licences from the
`raw.githubusercontent.com` payload on that branch, 2026-10-06.

### The permissive end — customise and redistribute

| Platform | Repo | Licence (payload) | ★ | Branch | What it is, and where it fits |
|---|---|---|---|---|---|
| **Pupilfirst** | [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | **MIT** (`master/LICENSE`) | **978** (280 forks) | `master` | 🆕 **A full LMS under MIT, at nearly 1,000★ — the largest permissive end-to-end platform this KB has recorded after Kolibri.** Built to run an **asynchronous online school**: learning through focused tasks, directed feedback, an iterative submit-review-resubmit workflow, and community interaction. Ruby on Rails. **Why it matters for engagements:** the other permissive platforms here are offline-first (Kolibri) or lesson-authoring (Oppia). Pupilfirst is the first permissive platform whose core model is **coached, reviewed project work** — which is the shape of corporate L&D, bootcamps and competency programmes, i.e. the shape of most of Globant's own education-adjacent demand. |
| **Sunbird (mobile + components)** | [Sunbird-Ed/SunbirdEd-mobile-app](https://github.com/Sunbird-Ed/SunbirdEd-mobile-app) | **MIT** (`main/LICENSE`) | 10 (**92 forks**) | `main` | **APAC / India.** The Cordova mobile client for the Sunbird stack, handling **both offline and online** consumption. TypeScript, **12,921 commits**. ⚠️ **Read the ratio, not the stars: 10★ against 92 forks.** This is a deployment artefact, not a GitHub-popularity artefact — forks are what national and state implementers create. Sunbird is already on this KB's shortlist as the nine-figure-scale platform; **this is the client address**, which the reset had dropped. |
| **Sunbird consumption components** | [Sunbird-Ed/SunbirdEd-consumption-ngcomponents](https://github.com/Sunbird-Ed/SunbirdEd-consumption-ngcomponents) | **MIT** (`master/LICENSE`) | not read this pass | `master` | Angular content-consumption components — the reusable player/renderer layer of the Sunbird client. |
| **Sunbird telemetry SDK** | [project-sunbird/sunbird-telemetry-sdk](https://github.com/project-sunbird/sunbird-telemetry-sdk) | **MIT** (`master/LICENSE`) | not read this pass | `master` | The telemetry SDK. Pairs with the xAPI chain in `repos/foundations.md`: Sunbird's own event model, MIT, at national scale. |
| **LibreTexts Conductor** | [LibreTexts/conductor](https://github.com/LibreTexts/conductor) | **MIT** (`master/LICENSE.md`) | 4 (3 forks) | `master` | **North America.** The platform behind LibreTexts' **Commons** catalogue, Campus Commons multi-tenancy, library integration, Meilisearch search, adoption reporting, and an **AI knowledge-base feature built on LangChain with vector embeddings**. TypeScript/React/Express/MongoDB. **Multi-tenant from a single codebase** — one deployment serving many institutions by configuration, which is exactly the shape a consortium or ministry engagement needs. |
| **LibreTexts LibreOne** | [LibreTexts/LibreOne](https://github.com/LibreTexts/LibreOne) | **MIT** (`main/LICENSE.md`) | not read this pass | `main` | The identity and account layer for the LibreTexts estate. The piece you need if Conductor is going to serve more than one institution. |
| **Edrys** | [edrys-org/edrys](https://github.com/edrys-org/edrys) | **MPL-2.0** (`main/LICENSE`, 16,725 B) | not read this pass | `main` | **Live-classroom platform** (remote labs, shared classroom modules). 🔴 **Corrected this pass: this is MPL-2.0, not the "abbreviated AGPL" an earlier pass recorded** — see `repos/foundations.md`. MPL-2.0 is **file-level** weak copyleft, so Edrys **can** sit inside a mixed-licence deliverable provided modified Edrys files stay MPL and are published. It was priced as unusable; it is usable with per-file discipline. |

### The copyleft and non-OSI end — real platforms, and the clause is the engagement

| Platform | Repo | Licence (payload) | Branch | What the clause does to the deal |
|---|---|---|---|---|
| **OpenEMIS Core** | [OpenEMIS/core](https://github.com/OpenEMIS/core) | **GPL-2.0** (`master/LICENSE`) | `master` | **Education Management Information System** — the ministry-level estate layer (schools, students, staff, institutions), the system UNICEF-supported deployments use. GPL-2.0: a modified OpenEMIS must be published under GPL-2.0, which for a **public-sector ministry client is usually a feature, not a cost** — the same argument pattern 28 makes for `i-educar` in Brazil. Price it as a public-good deliverable, not as lost IP. |
| **Edlib** | [cerpus/Edlib](https://github.com/cerpus/Edlib) | **GPL-3.0** (`master/LICENSE`) | `master` | **EMEA / Norway** (Cerpus). Content-authoring and sharing platform, the H5P-adjacent layer for interactive learning content. GPL-3.0 — a fork is a published fork. |
| **UDOIT** | [ucfopen/UDOIT](https://github.com/ucfopen/UDOIT) | **GPL-3.0** (`main/LICENSE`) | `main` | **North America** — University of Central Florida's **accessibility scanner for Canvas** courses: finds and helps fix WCAG issues in course content. GPL-3.0. Accessibility is a procurement requirement in US public education, and this is the installed-base tool. Pair it with the WCAG scanner already in `canvas-mcp` (MIT) when the deliverable must be permissive. |
| **OpenStax CMS** | [openstax/openstax-cms](https://github.com/openstax/openstax-cms) | **AGPL-3.0** (`main/LICENSE`) | `main` | The CMS behind OpenStax's open-textbook estate. AGPL-3.0 — **network-use copyleft**, so a hosted deployment triggers the source obligation. Content is separate: [openstax/osbooks-biology-bundle](https://github.com/openstax/osbooks-biology-bundle) is **Creative Commons**, which is correct for a textbook and useless as a code licence. Take the content, not the CMS. |
| **Nextcloud AI apps** | [nextcloud/assistant](https://github.com/nextcloud/assistant) · [nextcloud/context_chat](https://github.com/nextcloud/context_chat) | **AGPL-3.0** (`main/COPYING`) | `main` | **EMEA / Germany.** On-premises assistant and RAG-over-your-documents for a Nextcloud estate — the self-hosted European answer to a cloud AI assistant, and relevant wherever data residency binds. AGPL-3.0, and the licence sits in **`COPYING`**, not `LICENSE`. For a school or university already running Nextcloud this is a **deployment and integration** engagement, which AGPL does not obstruct; it obstructs shipping a proprietary derivative. |
| **Advising App** | [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | 🔴 **Elastic License 2.0** (`main/LICENSE`) | `main` | **Not open source.** Student-advising CRM for higher education. Elastic 2.0 **prohibits providing it as a managed service** and prohibits circumventing its licence keys. It looks open on GitHub and is not. Already recorded in pass 123; confirmed here from the payload. **Do not put it in a proposal as open source.** |
| **Leemons** | [leemonade/leemons](https://github.com/leemonade/leemons) | 🔴 **Composite / "Fair code"** (`main/LICENSE.md`) | `main` | **EMEA / Spain.** The payload opens *"Portions of this software are licensed as follows"* — an **open-core split by directory**, not one grant. Already recorded in pass 123. **Per-directory review before any reuse**; there is no single answer to "what licence is Leemons". |

### The Moodle AI plugin cluster, measured — 11 of ~16

Moodle's core is GPL-3.0 and an in-tree plugin inherits it. That is expected and is not
a finding. **What the sweep found is that the cluster is not uniformly licensed:**

| Licence state | Count | Repos |
|---|---|---|
| **GPL-3.0** (correct for in-tree) | 8 | [microsoft/o365-moodle](https://github.com/microsoft/o365-moodle) · [surlabs/AIChatForMoodle](https://github.com/surlabs/AIChatForMoodle) · [saylordotorg/moodle-local_ai_course_assistant](https://github.com/saylordotorg/moodle-local_ai_course_assistant) · [michael-milette/moodle-local_aiid](https://github.com/michael-milette/moodle-local_aiid) · [Universita-di-Ferrara/moodle-aiprovider_gemini](https://github.com/Universita-di-Ferrara/moodle-aiprovider_gemini) · [caiocarvalhofre/moodle-mod_maici](https://github.com/caiocarvalhofre/moodle-mod_maici) (**LATAM / Brazil**) · [moodlehq/moodle-tool_dataprivacy](https://github.com/moodlehq/moodle-tool_dataprivacy) (branch **`MOODLE_34_STABLE`**) · [Citolab/qti-convert](https://github.com/Citolab/qti-convert) |
| 🔴 **Ungranted** | 3 | `marcusgreen/moodle-tool_aiconnect` · `jeanlucio/moodle-local_aihub` · `alvarogregori/moodle-ai-graded-assignment` |

⚠️ **`moodle-ai-graded-assignment` is the one to notice.** AI-graded assignments is the
function trend 7 has flagged as the regulated frontier and the tooling gap since the
seventh pass. A plugin for it exists in the Moodle ecosystem and **carries no licence**.
It cannot be adopted, and that is a supply fact rather than a search failure — it was
probed on its real default branch against 30+ filename variants.

🆕 **And the licence-hygiene asymmetry is now visible as a pattern.** Across this pass's
66 archive addresses, **11 were ungranted** — and the ungranted set is concentrated in
exactly two places: **individual-maintainer LMS plugins** and **public-sector metadata
and vocabulary repositories** (FWU Germany, DG EMPL, DINI-AG-KIM, IMDA's evals
catalogue). The organisations whose output is *most* reusable in principle — ministries
and standards groups publishing vocabularies — are the ones least likely to attach a
grant. **For an EMEA public-sector engagement, "can we have a licence on this?" is a
cheap, early, high-leverage ask**, and one a client ministry can usually satisfy with a
single commit.

### The platform-selection table, updated

| If the client needs… | Take | Licence | Why |
|---|---|---|---|
| Coached, reviewed **project-based** learning at scale | **Pupilfirst** | **MIT** | Only permissive platform built around submit → review → resubmit. 978★. |
| **Offline-first** / low-connectivity delivery | **Kolibri** | MIT | Unchanged; still the equity-deployment base. |
| **National / state** scale with an existing implementer community | **Sunbird** | MIT | 92 forks on the mobile client; India-proven. |
| **Multi-tenant OER** for a consortium or ministry | **LibreTexts Conductor** + **LibreOne** | MIT | One codebase, many institutions, AI KB already wired. |
| **Live/remote-lab classrooms** | **Edrys** | MPL-2.0 | File-level copyleft only — mixed deliverable is fine. |
| **Ministry-level EMIS** | **OpenEMIS Core** | GPL-2.0 | Publishing the fork is acceptable, often preferable, for a public client. |
| **Interactive content authoring** | **Edlib** / H5P | GPL-3.0 | Fork is published. |
| A **student-advising CRM** | ⚠️ **not `advisingapp`** | Elastic 2.0 | Source-available, no managed service. Build on a permissive base instead. |

## Added in the thirteenth pass of 2026-10-06 — the fifth fully permissive platform, and the first AI-native one that is also sovereign-ready

| Platform | Repo | Licence (read from payload) | Position |
|---|---|---|---|
| **Open TutorAI (CE)** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** (`LICENSE`, 1,531 B — body text, **no title line**) | **Promoted onto this shelf this pass.** Personalised tutoring platform: multi-model conversation, **local RAG**, **voice / video / 3D-avatar modes**, per-learner assistant configured through structured onboarding, and **role-based access control**. Serves **Ollama** local models as well as OpenAI / Groq / Mistral. Python, 380 commits, **108★ / 192 forks**. From the **IRF-SIC Laboratory, Ibn Zohr University, Agadir, Morocco**, with Morocco's Ministry of Higher Education, the **Digital Development Agency** and the **CNRST** as funders. **Open core** — a paid Enterprise Edition adds theming, SLA and LTS. |

### Why this changes the shelf, and what it does not change

The permissive end of this shelf has been **four platforms** — Kolibri (MIT),
Oppia (Apache-2.0), Mentingo (MIT), Coursemology (MIT), plus Sunbird (MIT) at national
scale. Every one of them is a **platform that AI can be added to**. Mentingo was recorded
as *"the only AI-native one"*, and on a corporate-L&D footing that remains true.

Open TutorAI is the **fifth**, and it is a different proposition from all of them:

- 🟢 **AI-native and academic**, not AI-added and corporate. The tutoring loop,
  the retrieval layer and the avatar presentation are the product, not a plugin.
- 🟢 **Sovereign by construction.** It ships **local RAG** and serves **Ollama** in the
  same configuration surface as the hosted APIs. Every other AI-native option on this
  shelf requires the sovereign path to be *built*; here it is a setting. That makes it the
  shortest route to the EMEA data-residency posture this KB has been assembling by hand
  since pattern **P4**.
- 🟢 **RBAC is already there**, which is the unglamorous blocker that stops a pilot
  becoming an institutional deployment.
- 🟢 **It is a state-funded public-sector reference.** A Moroccan ministry, the DDA and the
  CNRST stand behind it. For a public-sector buyer in EMEA or LATAM, a sovereign-stack
  tutoring platform that a government already funds is a materially stronger reference than
  a vendor pilot.

What it does **not** change:

- ⚠️ **It is open core.** The CE is the base for a commercial Enterprise Edition. The
  BSD-3-Clause grant on the CE is unqualified and **this is not a directory carve-out like
  Langfuse's `ee/`** — but the roadmap is set by a party with an incentive to keep features
  above the line. Check which side of that line a client's must-haves fall on **before**
  proposing it, and record the answer.
- 🔴 **The copyright holder in the payload is not identifiable.** The licence reads
  *"Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev"*, and **R2D-dev
  appears in no public artefact of the project** — not the README, not the documentation,
  not the search index. The grant is real; the entity holding it is opaque. On a
  redistribution engagement that is the party an indemnity question routes to, so **raise
  it upstream before it reaches a contract**.
- ⚠️ **It is published as Apache-2.0 in third-party catalogues and it is BSD-3-Clause.**
  Both are permissive and both are on this KB's allowlist, so nothing architectural turns
  on the error — but a diligence pack that cites a catalogue instead of the payload will
  state the wrong licence, and the attribution clauses differ.
- ⚠️ **192 forks against 108 stars.** The twelfth pass established the reading: in the
  education layer, forks exceeding stars means **deployed as a base**, not watched. That is
  a point in its favour, and it also means a meaningful share of real-world use is in forks
  whose divergence nobody is tracking. **Pin a commit.**

### The platform-selection table, updated

| If the engagement is… | Start from | Licence posture |
|---|---|---|
| **Academic tutoring, AI-native, data must stay in-region** | **Open TutorAI CE** | 🟢 BSD-3-Clause — build and redistribute; verify the open-core line |
| Corporate L&D / onboarding / compliance, AI-native | Mentingo | 🟢 MIT |
| CS and programming teaching, higher ed | Coursemology | 🟢 MIT |
| Low connectivity, equity-driven, offline | Kolibri | 🟢 MIT |
| Interactive lessons with misconception handling | Oppia | 🟢 Apache-2.0 |
| National / nine-figure learner scale | Sunbird | 🟢 MIT (100+ services is the cost) |
| The incumbent is already there | Moodle / Canvas / Open edX | 🔴 Copyleft — **side-car via LTI or MCP**, never a fork |

## Added in the fourteenth pass of 2026-10-06 — the proprietary platforms a client already runs, and what their integration tier now costs

Every platform on this page up to here is one Globant can **deploy**: permissive ones to
customise and redistribute, copyleft ones whose clause decides the engagement. That framing
has a hole in it, and it is the most common engagement in higher education: **the client
already runs a proprietary LMS and is not replacing it.** Canvas, Brightspace, Blackboard
and Google Classroom are not on this shelf as platforms because they cannot be — and the
question a studio is actually asked is not *"what should we deploy"* but *"what can you build
against what we have."*

This pass measured that answer, platform by platform. The licence that matters is no longer
the platform's; it is **the licence of the integration tier**, and that tier is now large
enough to inventory.

### The integration tier, by platform

Measured with GitHub REST `total_count`, one platform name per query, 2026-10-06. Licences
read from each repository's own payload. Full rows in `agents/top.md` (fourteenth pass).

| Platform the client runs | Integration repos | Best permissive, payload-backed server | Verdict for a Globant engagement |
|---|---|---|---|
| **Canvas LMS** (Instructure) | **117** | `vishalsachdev/canvas-mcp`, **MIT**, 278★, up to 103 tools | 🟢 **Adopt.** Deepest tier in education. Pin the canonical repo against its forks. |
| **Moodle** (GPL-3.0 platform) | **86** | `peancor/moodle-mcp-server`, **MIT** — plus `1alexandrer/moodle-mcp`, MIT, 18★ 🆕 | 🟢 **Adopt, from outside the tree.** The MCP side-car is MIT precisely because it is not an in-tree plugin — the licence-boundary note in `agents/top.md` is the whole architecture. |
| 🆕 **Brightspace / D2L** | **23** | `RohanMuppa/brightspace-mcp-server`, **MIT**, 57★, on npm | 🟢 **Adopt.** New to this KB. A real tier: a feature-complete server on npm, an engineering-grade alternative with opt-in writes (`JhostinAleck/brightspace-mcp`, MIT) and an **Apache-2.0** option (`pranav-vijayananth/...`) where a client's policy wants the explicit patent grant. |
| 🆕 **Blackboard Learn / Ultra** | **5** | `nitsuah/bb-mcp`, **MIT**, 2★, **RBAC middleware** | ⚠️ **Thin — build on the best of five.** Large university install base, five repositories. `bb-mcp` is the one to start from: it is the only asset in the whole 98-address cluster that puts **role-based access control** in the MCP layer, which is the control an education deployment is audited on. |
| 🆕 **Google Classroom** | **17** | `faizan45640/google-classroom-mcp-server`, **MIT**, **6★** | 🔴 **Build.** The widest K-12 reach of any platform here and its best dedicated server has six stars. `Kimmahone/edu-workspace-mcp` (MIT) is the more useful starting point because it covers **Google Forms**, and Forms is where K-12 assessment actually lives. |
| **Open edX** (AGPL-3.0 platform) | **1** | — (`blend-ed/tutor-contrib-openedxmcp`, **AGPL-3.0**) | ⚠️ **Copyleft all the way down.** The one integration asset inherits the platform's AGPL. Already recorded; unchanged this pass. |
| 🔴 **PowerSchool** (dominant US K-12 SIS) | **0** | **none** | 🔴 **Empty tier.** `total_count: 0`. There is nothing to adopt, nothing to fork and nothing to compete with. |

### What this table changes about platform selection

🔵 **Integration depth is inversely related to engagement opportunity.** Canvas and Moodle
hold **203 of the 249** repositories measured. Everything a client is likely to ask for
against those two already exists under MIT, so the studio's value there is configuration,
governance and pedagogy — **not** the connector.

The money is in the thin and empty tiers, and they are the **K-12 administrative** ones:

- **Google Classroom and PowerSchool together cover most of US K-12**, and their open-source
  integration tier is 17 repositories and 0 repositories respectively.
- That tier's data is **student records, guardians, enrolment and accommodations** — i.e. the
  regulated surface. The reason it is empty is not that nobody wants it; it is that a
  hobbyist cannot get credentials to a district SIS. **An enterprise integrator can**, and
  that is the asymmetry.
- Price it as a build, not an adoption, and put the governance artefacts in the statement of
  work from day one (see P24 and P25 in `compose/patterns.md`).

### 🆕 The ministry tier — a national curriculum as a callable platform

New on this page and new to this KB: the platform is not an LMS but a **state education
authority's own API estate**, and in two Nordic countries it is already wrapped as an MCP
server.

| Authority | Wrapper | Licence (payload) | What it exposes |
|---|---|---|---|
| **Skolverket** — Swedish National Agency for Education (**EMEA**) | [isakskogstad/Skolverket-MCP](https://github.com/isakskogstad/Skolverket-MCP), 12★ | 🟢 **MIT** (`LICENSE`, 1,093 B) | *All* of Skolverket's open APIs: the **Läroplan / syllabus API**, the **Skolenhetsregistret** school-unit register, and the Planned Educations API. Published in the official MCP Registry. |
| **Udir** — Norwegian Directorate for Education (**EMEA**) | [3121n/nor-data-udir-mcp](https://github.com/3121n/nor-data-udir-mcp) | 🔴 **none** — 0 of 20 filenames, no manifest field | School (NSR) and kindergarten (NBR) registry data. |
| **Smartschool** — dominant LMS in Flemish education (**EMEA**, Belgium) | [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP), 5★ | 🟢 **MIT** (`LICENSE`, 1,069 B) | Platform integration with real release engineering: PyPI package, CI, codecov. |

⚠️ **Read the Skolverket copyright line before this goes in a proposal.** It says
**"Skolverket Syllabus MCP Contributors"**, not Skolverket. The MIT grant covers **the
wrapper**; the **agency's own terms govern the data** the wrapper returns. Two consequences
for an EMEA engagement: the code is safe to fork and ship, and the data terms are a separate
diligence item that the MIT licence does not answer.

🔵 **This is the reusable shape, and it generalises past Sweden.** A national curriculum
published as an open API, wrapped thinly under a permissive licence, turns
*"align this to the national curriculum"* from a consulting deliverable into a **tool call**.
It is the missing input to P15 (curriculum-aligned item generation) and the cleanest
instance yet of trend 13: the mandate specifies the architecture. **Udir is the counter-case
in the same region** — same idea, same quality of public data, no grant — so the pattern is
"check for a wrapper, expect to write one," not "a wrapper exists."

### The university tier, and the two APAC assets that prove it is a channel

The same shape one level down: a single institution's portal, wrapped permissively.

| Institution | Wrapper | Licence | Note |
|---|---|---|---|
| **Korea University** (KUPID portal), **APAC** | [SonAIengine/ku-portal-mcp](https://github.com/SonAIengine/ku-portal-mcp), 13★ | 🟢 **MIT** | Notices, library seat availability, weekly assignments. On PyPI. Korean-language README — and the thirteenth pass's **Korean-language query did not find it**; the platform name did. |
| **National Taiwan University** (NTU COOL), **APAC** | [kc0506/ntucool](https://github.com/kc0506/ntucool), 10★ | 🟢 **MIT** | One `cool` binary = CLI + MCP server + SDK, **plus a Claude Code plugin** shipping skills and commands. ⚠️ Self-declared **unofficial**. |

⚠️ **"Unofficial" is a diligence item, not a disqualifier** — but it is the one that decides
whether a university client can deploy it. An unofficial wrapper of an institution's own
portal depends on undocumented endpoints and on credentials the institution controls; it can
be broken by the institution at any time, deliberately. Fork it for the shape, then get the
integration sanctioned.

### 🔴 And the competition is now hosted, closed, and in the same catalogue

The MCP Registry census this pass (`repos/trending.md`, fourteenth pass) found **102
education-vocabulary servers, 71 of them with no source repository at all**. One of those 71
is **`com.moodlemcp/moodle`** — *"Connect your Moodle to AI assistants: courses, content,
grading and more"* — a **closed, hosted Moodle MCP endpoint competing directly with the 86
open repositories in that tier.** Others: `io.cubite/lms` (hosted LMS with SCORM/xAPI) and
`com.skillsail/mcp` (SCORM authoring and export).

🔵 **The strategic read, and it belongs on this page rather than in trends.** For two years
the open-source platform shelf competed with proprietary *platforms*. It now also competes
with proprietary **connectors to open platforms** — someone selling a hosted MCP endpoint in
front of the client's own Moodle. That is a thin, high-margin layer, and it is exactly the
layer a Globant deliverable occupies.

**So the pitch changes.** Against a hosted connector, the differentiator is not features; it
is the three things a client cannot get from an endpoint they do not host: **the code**, **the
deployment inside their own boundary**, and **the audit trail**. Lead with those, and keep
`langfuse` (MIT outside `ee/`) in the stack so the third one is produced automatically.

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS platform tier, and why none of it is permissive

This KB's platform shelf has been built around the **learning** platform — Moodle, Open edX,
Canvas, Sunbird, Coursemology, Mentingo, Kolibri. The administrative platform — the student
information system — had only OpenEduCat (LGPL-3.0, on Odoo), i-Educar and the Fedena
question. This pass measured the tier properly, because the fifteenth pass's SIS integration
work made the platform question unavoidable: *if we must integrate with a proprietary SIS,
is there an open one to deploy instead?*

**There is. It is substantial. And not one of it is permissive.**

### The tier, licence read from the payload on 2026-10-06

| Platform | ★ / forks | Licence (payload) | Default branch | Country / scope |
|---|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **644** / 391 | ⚠️ **GPL-2.0** (15,214 B) | 🔴 `mobile` | Global, PHP — full SIS: gradebook, attendance, scheduling, billing |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | **634** / 417 | ⚠️ **GPL-3.0** (35,121 B) | 🔴 `v31.0.00` | Global, PHP — school management platform |
| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | **345** / 286 | ⚠️ **GPL-2.0** (17,286 B, at `docs/License.txt`) | `master` | Global, PHP — multi-institution SIS |
| [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | *(already shelved)* | ⚠️ **GPL-2.0** (18,092 B) | 🔴 `2.12` | **LATAM** — Brazilian municipal SIS |
| [`OS4ED/openSIS-Responsive-Design`](https://github.com/OS4ED/openSIS-Responsive-Design) | — | 🔴 **no payload found** | `master` | sibling repo of the above |

🔴 **Four platforms, 1,600+ stars and 1,000+ forks between them, and the licence set is
`{GPL-2.0, GPL-3.0}` with one ungranted sibling. Zero MIT. Zero Apache. Zero BSD.**

### 🟢 This is the finding that explains the whole pass

The fifteenth pass found **24 permissive assets** in the SIS space (`agents/top.md`) and
**zero permissive SIS platforms**. That is not a coincidence, and it is the most useful
structural fact in this file:

> **You cannot fork an open SIS permissively, so all the permissive work happens at the
> edges.** The MIT supply is in clients, wrappers, timetable decoders, MCP servers and
> browser extensions — everything that *talks to* a student information system without
> *being* one.

🔵 **Which means the architecture decision is forced, and it is the same in every region:**

| If the client wants | The answer is | Licence reality |
|---|---|---|
| To **replace** a proprietary SIS with open source | RosarioSIS, Gibbon or openSIS | ⚠️ **GPL — plan for it.** A Globant-delivered module that is a derivative work must be published under the same terms. The Odoo/OpenEduCat LGPL-3.0 route remains the only middle path on this page. |
| To **add AI to** the SIS the client already runs | the integration tier (`agents/top.md`, `repos/foundations.md`) | 🟢 MIT/BSD on the code — 🔴 **and the vendor's ToU on the access.** See below. |
| To **avoid both constraints** | official API + your own code | 🟢 permissive OneRoster/Ed-Fi implementations, already shelved in the interoperability tier |

### ⚠️ The warning that outranks every licence on this page

For the **second** route above, the licence is not the binding constraint. A proprietary SIS
vendor's Terms of Use can forbid exactly the access an AI integration needs, regardless of
how the client library is licensed. Infinite Campus's ToU — quoted in full in
`agents/top.md`, Finding 2 — prohibits access *"by any means other than our publicly
supported interfaces (for example, scraping or using the content to train artificial
intelligence software)"*, and the one MIT-licensed MCP server for that platform states that
it violates it.

🔵 **Platform selection therefore acquired a new question this pass, and it goes before the
licence question:** *does the institution hold an API agreement with its SIS vendor?* If yes,
the integration route is open and the permissive shelf is usable. If no, the honest options
are the official API (procure it), an open SIS (accept the GPL), or a prototype that is
explicitly not a production path. **Run P26 before scoping either.**

### A platform-tier instrument finding — 3 of 5 default branches are not `main` or `master`

| Platform | Default branch |
|---|---|
| `GibbonEdu/core` | 🔴 **`v31.0.00`** — a version number |
| `portabilis/i-educar` | 🔴 **`2.12`** — a release series |
| `francoisjacquet/rosariosis` | 🔴 **`mobile`** — a feature name |

🔴 **The fourteenth pass found one agent-generated default branch and called `ls-remote
--symref` non-optional. This tier makes it unarguable: a probe that assumes `main` or
`master` returns 404 on the three highest-starred open SIS platforms in existence** and
writes all three down as ungranted. They are not; they are GPL, which is a very different
engagement from unlicensed.

🟢 **And one licence sat at `docs/License.txt`** (mixed case, in a subdirectory, with a
byte-order mark) — `OS4ED/openSIS-Classic`. No filename ladder in this KB would have found
it. **It was found by reading the README's own licence link**, which is a better instrument
than guessing filenames: it is one request, it is authoritative, and the maintainer wrote it
on purpose. Add it to the method ahead of the ladder.

---

## Added in the sixteenth pass of 2026-10-06 — the education-ERP shelf, and the grant that was hiding in a Python manifest

The mandatory vertical query (`open source platform education ERP CRM MIT Apache student
information system`) **passed for the first time in this KB's history** — it named platforms
instead of returning tutorials. Every candidate below was probed on its real default branch on
2026-10-06.

### The platforms, with their licences read correctly

| Platform | Repo | Branch | Licence (payload-verified) | ★ | What it is |
|---|---|---|---|---|---|
| 🟢 **Joanie** | [`openfun/joanie`](https://github.com/openfun/joanie) | `main` | 🟢 **MIT** (1,086 B, *"(c) 2021 France Université Numérique"*) | 30 | A **headless education ERP**: course enrolment/subscription, **payment**, and **certificate delivery**. From the same state-backed org as Richie. |
| 🟢 **eVaka** | [`espoon-voltti/evaka`](https://github.com/espoon-voltti/evaka) | `master` | **LGPL-2.1-or-later** — ⚠️ via **`LICENSES/`**, not `LICENSE` | 58 | **Finland's early-childhood-education ERP**, in production for the City of Espoo. Kotlin. Enrolment, placement, fee decisions, daily attendance. |
| 🟢 **treVaka** | [`Tampere/trevaka`](https://github.com/Tampere/trevaka) | `main` | **LGPL-2.1** (27,030 B — the full text) | 2 | eVaka adapted for the **City of Tampere**. Active 2026-10-06. 🔵 **Its existence is the finding: eVaka is a multi-municipality platform, not one city's internal tool.** |
| 🔴 **OdooEduERP** | [`JayVora-SerpentCS/OdooEduERP`](https://github.com/JayVora-SerpentCS/OdooEduERP) | `19.0` | 🔴 **AGPL-3.0** — ⚠️ declared in **`school/__manifest__.py`**, top level is NO-PAYLOAD | **157** | The most-starred open-source education ERP found this pass. Admissions, attendance, exams, library, transport, fees — on **Odoo**. Active 2026-10-03. |
| 🔴 **CybroOdoo EducationalERP** | [`CybroOdoo/EducationalERP`](https://github.com/CybroOdoo/EducationalERP) | `16.0` | 🔴 **GPL-3.0** (35,147 B) | 16 | A second Odoo education suite. Branch pinned to Odoo 16. |
| ⚠️ **Frappe edu** | [`nguyentrieu210/edu`](https://github.com/nguyentrieu210/edu) | `main` | 🟢 **MIT** (`license.txt`, 1,069 B) | 6 | Education ERP as a **Frappe app + Vue 3 SPA**. ⚠️ Self-described **"(demo)"**, created 2026-06-20 — a starting point, not a platform. |

### ⚠️ Read this before anyone proposes "the Odoo education ERP" to a client

**`OdooEduERP` reads as unlicensed to every instrument this KB owns, and it is AGPL-3.0.**

Its real default branch is `19.0` — neither `main` nor `master` — and there is **no licence
payload at the top level** on it. A probe returns NO-PAYLOAD, which in this KB's conventions
means *"ask upstream."* The grant is one directory down, in the Odoo module manifest:

    # school/__manifest__.py
    "license": "AGPL-3",

🔴 **This is the expensive direction to be wrong in.** A NO-PAYLOAD verdict invites a team to
proceed while an upstream ask is pending; the truth is a **network-copyleft** licence that
reaches any hosted deliverable built on it. 157★ and active last week means somebody *will*
propose it.

⚠️ **A staleness tell in the same file:** the branch is `19.0` and the manifest inside it still
declares `"version": "18.0.1.0.0"`. Verify which Odoo release it actually targets before
sizing any engagement.

🔵 **Generalised:** this is the third non-`LICENSE` grant location found in one pass (R's
`DESCRIPTION`, REUSE's `LICENSES/`, Odoo's `__manifest__.py`). **In the Odoo ecosystem the
module manifest is the licence of record, and the repository root is often silent.** Any
Odoo-based row in this KB must be probed at the module level.

### 🟢 Joanie is the row that changes the platform menu

This KB's existing shortcut says **MIT at the portal tier is the cleanest place to put
client-visible AI, because the copyleft lives behind it in the LMS** — the Richie
recommendation. Joanie extends that from *presentation* to **transaction**:

| Tier | Permissive option | Licence |
|---|---|---|
| Portal / catalogue | [`openfun/richie`](https://github.com/openfun/richie) | 🟢 **MIT** |
| **Enrolment, payment, certificates** | **[`openfun/joanie`](https://github.com/openfun/joanie)** | 🟢 **MIT** |
| LMS / delivery | Open edX (AGPL core, 🟢 **Apache-2.0 plugin SDK**) or Moodle (GPL-3.0) | copyleft |

🔵 **So the whole commercially sensitive surface — catalogue, checkout, credential — can be MIT,
with copyleft confined to course delivery.** Both halves come from **France Université
Numérique**, so they are designed to compose, and both are state-backed rather than
venture-backed. ⚠️ **Joanie is 30★ and issue-heavy (61 open)**: treat it as a solid foundation
to fork, not a turnkey product, and read `payment` integration code before promising a date.

### 🟢 eVaka — and why LGPL-2.1 is a *different* answer from LGPL-3.0 here

The page already argues that **LGPL-3.0 is the middle path** for administrative platforms:
link against it, keep your own modules proprietary, publish changes to the library itself.
eVaka is **LGPL-2.1-or-later**, which lands in the same architectural place — but note what
eVaka actually is:

* 🟢 **A production national-scale ECEC system.** Espoo is Finland's second-largest city, and
  **Tampere runs a derivative** — so the platform has survived being adapted by a second
  municipality, the single hardest test of a public-sector codebase.
* 🟢 **Early childhood is a tier this KB's platform shelf did not cover at all.** Every other
  platform here is K-12, higher-ed or L&D. Placement queues, fee decisions by income, daily
  attendance and statutory child-ratio compliance are a genuinely different domain.
* ⚠️ **The licence is not in `LICENSE`.** eVaka follows the **REUSE specification v3.0**: the
  1,001-byte `LICENSE` is a *pointer* that says, verbatim, *"never the original license
  texts"*, and the grant lives in `LICENSES/LGPL-2.1-or-later.txt` (verified, HTTP 200) plus
  per-file SPDX headers. A payload probe reads NO-GRANT or guesses from prose. **REUSE is an
  FSFE standard and is spreading through EU public-sector code — expect this shape again in
  exactly the region this matters for.**

⚠️ **AI integration point, stated honestly:** eVaka is an administrative system holding data
about **small children**. Under the EU AI Act the attractive automations here — placement
prioritisation, fee determination — are decisions about access to a public service for a
protected group. 🔵 **The defensible AI layer is assistive**: demand forecasting for placement
capacity, caseworker drafting with a human decision gate, anomaly review on attendance. **Not
automated placement.** Pattern `P11` (one oversight gate) is the shape; `P13` sets the
compliance profile.

### Platform selection shortcut — sixteenth-pass additions

| If the client is… | Take | Licence reality |
|---|---|---|
| A **European municipality running early-childhood education** | 🟢 **eVaka** (+ treVaka as the adaptation precedent) | LGPL-2.1-or-later — link, don't fork the core; grant is in `LICENSES/` |
| Selling **courses** and needing catalogue + checkout + certificates | 🟢 **Richie + Joanie** | 🟢 **MIT both** — the commercial surface is clean |
| Asking for **"the Odoo education ERP"** | ⚠️ **OdooEduERP, with the AGPL-3.0 conversation first** | 🔴 AGPL-3.0, declared in the module manifest — network copyleft reaches a hosted deliverable |
| A **Norwegian** institution needing curriculum alignment | 🟢 **Grep SPARQL endpoint** (`repos/foundations.md`) | 🟢 **NLOD — commercial use granted** |

---

## Added in the seventeenth pass of 2026-10-06 — the national-platform tier, and the first licence on this page whose problem is *delivery model*, not permission

Pass 15 found the SIS/MIS tier and reported that **none of it is permissive**. Pass 16 found the
education-ERP shelf. This pass found something the page has not had: **a complete national
platform estate, published by the state, under an OSI licence — where the blocker is neither
"closed" nor "copyleft" but *how you intend to deliver it*.**

### The tier, licence read from the payload on 2026-10-06

| Platform | Owner | Licence (payload-verified) | Scale | What it runs in production |
|---|---|---|---|---|
| **AOE — Avointen oppimateriaalien kirjasto** ([`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe)) | 🇫🇮 Finnish National Agency for Education | 🟡 **EUPL-1.2** (`aoe-web-backend/LICENSE` + `aoe-web-frontend/LICENSE`, 303 B each) | **6,829 commits**, HEAD 2026-10-06, TypeScript | **Finland's national library of open educational resources** (`aoe.fi`) — upload, describe, license-tag and search OER, with a full editorial metadata model. |
| **ePerusteet** ([`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet)) | 🇫🇮 same | 🟡 **EUPL-1.1** (631 B) | Java, active | **The national core curriculum and qualification requirements**, as a service rather than a PDF. |
| **Koski** ([`Opetushallitus/koski`](https://github.com/Opetushallitus/koski)) | 🇫🇮 same | 🟡 **EUPL-1.1** (653 B) | Scala, 23★ | **National study-records service**: every study right and completed qualification, one API. |
| **Ataru** ([`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru)) | 🇫🇮 same | 🟡 **EUPL-1.2** (295 B) | Clojure, 11★ | **The national admissions application engine** — generic form generation driving real intake. |
| **eHOKS** ([`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks)) | 🇫🇮 same | 🟡 **EUPL-1.1** (631 B) | Clojure | **Personal competence-development plans** for vocational learners. |
| **SS 12000 reference API** ([`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api)) | 🇸🇪 Swedish National Agency for Education | 🟢 **Apache-2.0** (11,339 B) | Java, 5★ | Not a platform — **the standard every Swedish school-administration system exchanges data through**, with a working implementation. |

### 🔴 Read this before anyone proposes "the Finnish stack, customised with AI" to a client

The EUPL is **OSI-approved open source** and nothing here is a permission problem. The problem is
that **EUPL copyleft reaches network delivery**, and almost every engagement this page describes
is network delivery.

| Delivery model the studio is actually proposing | EUPL consequence |
|---|---|
| **Call** AOE / Koski / ePerusteet APIs from an agent we build | 🟢 **No obligation.** Using a service is not distribution. This is the safe default and it is where the value is. |
| Deploy an **unmodified** instance for the client, on-prem or hosted | 🟢 Fine; ship the licence and the notices. |
| **Modify** it and run it as the client's **hosted** product | 🔴 **Copyleft triggers.** Art. 1 counts *"communication to the public"* — making functionality available to others, including over a network — as Distribution. Our modifications must be offered under the EUPL. **This is the AGPL shape, and most studio proposals land here.** |
| Modify it, combine with a GPL-3.0 / AGPL-3.0 / MPL-2.0 component, relicense the combined work | 🟡 **Permitted — Art. 5 compatibility list.** ⚠️ And the EC's own published discussion notes that because the compatible licence prevails on conflict, routing through **GPL-3.0** (which has no network clause) can **circumvent the SaaS obligation**. 🔴 **Do not sell this route.** It is documented, it is contested, and it is a question for the client's counsel, not for an architecture deck. |

🔵 **The honest sales line, and it is a better one than a fork would have been:** *"We do not
fork Finland's national services; we build the agent layer that calls them, and we can do that
because the state published the interfaces."* **That proposal has no copyleft exposure at all**,
and the national platform becomes an asset of the engagement rather than a licensing risk.

### 🟢 Why the Swedish row changes the platform menu differently

`dnp-ss12000-reference-api` is **Apache-2.0**, so it carries none of the above. It can go into a
closed, hosted product, and what it gives is the thing integration projects actually burn budget
on: **a national-standard conformant rostering/SIS data exchange, already implemented.**

⚠️ **The limit, stated plainly:** SS 12000 is **Swedish**. It is not an EU standard and not a
Nordic one by fiat. Whether the Finnish services can be reached through an SS 12000 shape — which
would turn one country's standard into a regional integration layer — **is not established in
this KB and should not be implied in a deck.**

### Platform selection shortcut — seventeenth-pass additions

- **Client wants a national OER library** → **AOE** is the only state-run, OSI-licensed one here.
  Call it or deploy it unmodified; do not fork it into a hosted product.
- **Client wants curriculum alignment in EMEA** → **Grep/NLOD (Norway)** if commercial reuse of the
  *data* is the requirement (NLOD grants it outright); **ePerusteet (Finland)** if the requirement is
  depth of the curriculum model. `P25` and `P27` in `compose/patterns.md`.
- **Client wants Swedish school-data integration** → **SS 12000 reference API**, Apache-2.0, lift it.
- **Client wants a learner-identity or study-records model to copy** → read **`oppijanumerorekisteri`**
  and **`koski`**; take the model, write your own code. Reading carries no obligation.
- 🔴 **Client wants to white-label a national platform as their SaaS** → **stop.** That is the one
  cell in the table above that is red, and it is the most common thing to be asked for.


## Added in the eighteenth pass of 2026-10-06 — the assessment delivery tier, and a national agency's service clients

**No new platform this pass.** `open source platform education LMS SIS MIT Apache 2026` returned
the shelf above — Open edX, Sakai, OpenOLAT, OpenEduCat — and nothing new. What it did return is a
**component tier that was never swept**, because the sweeps were organised by topic and these are
filed under a **standard**. Licences read from each repository's own payload on 2026-10-06.

### QTI 3 — assessment item delivery

This is the layer that sits *between* the LMS and the learner, and it is the one place where a
permissive component now carries **third-party conformance certification**.

| Component | Repo | Licence (read from payload) | Use |
|---|---|---|---|
| QTI 3 item player | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (`main/LICENSE`, © 2022-2024 Amp-up.io, LLC) | 🟢 **1EdTech Certified — QTI 3 Basic *and* Advanced "Delivery"**. The default. 30★ |
| QTI 3 item player, Vue 3 | [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (`main/LICENSE`, © 2024) | Same component for a Vue front end |
| QTI 3 toolchain | [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (`main/LICENSE.md`, © 2026 Longsight, Inc.) | 12 npm packages — parse, validate, render, **score**, and **migrate QTI 1.2 / 2.x → 3**. The migrator is the part nobody else ships |
| QTI 3 renderer, framework-neutral | [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (`main/LICENSE`, © 2026 AE Studio) | Full response processing, no framework commitment |
| QTI 3 HTML utilities | [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | **MIT** (`main/LICENSE`, © 2026 metyatech) | Smallest surface of the five |
| QTI 3 support, PHP | [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (`main/LICENSE`, © 2026 Kennisnet) | The permissive PHP path, where `oat-sa/qti-sdk` is GPL-2.0 |
| QTI item renderer (mature, copyleft) | [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | **GPL-3.0** (`main/LICENSE.md`) | 2,456 commits, 19★ — the most mature here. From **Citolab**, the software lab of **Cito**, the Dutch national assessment institute. ⚠️ README invites relicensing on request — read trends §43 before designing around the licence |
| QTI SDK, PHP | [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`master/LICENSE`) | From the TAO assessment platform. **GPL-2.0**, so **not compatible with GPL-3.0-only code** — the same trap as RosarioSIS above |

🔴 **Do not cite [`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components).** It is a
**stale fork** of the Citolab repository — identical root commit `de8b27b`, **79 commits behind**,
1★ against upstream's 19. Pin the upstream address.

### Kennisnet — clients for the Dutch national education services

**[Stichting Kennisnet](https://github.com/Kennisnet)** is the Netherlands' public agency for ICT in
education. Its repositories are not a platform; they are **clients for national services**, which is
a shape this shelf had no entry for. **29 repositories, nine probed: 6 MIT, 1 GPL-3.0, 2 ungranted.**

| Component | Repo | Licence (read from payload) | The national service it reaches |
|---|---|---|---|
| Edurep search client | [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | **MIT** (© 2015 Stichting Kennisnet) | **Edurep**, the national learning-resource index. 🟢 A national OER index you may query under a permissive client |
| Eduterm client | [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) | **MIT** (© 2018 Kennisnet) | **Eduterm**, the national curriculum vocabulary — **in Python** |
| LOM metadata | [`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) | **MIT** (© 2017 Kennisnet) | IMS-LOM records, read and write — **in Python** |
| NL-LOM profile | [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | **MIT** (© 2017 Stichting Kennisnet) | The Dutch national application profile of LOM — the worked example of how a country profiles a global standard |
| OAI-PMH harvesting | [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | **MIT** (© 2024 Kennisnet) | The protocol national repositories actually expose |
| QTI editor | [`Kennisnet/qti-editor-angular`](https://github.com/Kennisnet/qti-editor-angular) | 🔴 **NO-PAYLOAD** | Ungranted — **do not vendor** |
| Edurep transforms | [`Kennisnet/edurep-xslt`](https://github.com/Kennisnet/edurep-xslt) | 🔴 **NO-PAYLOAD** | Ungranted |

⚠️ **Nine of 29 probed**, chosen by stars and domain relevance. The estate's ungranted rate is
**sampled, not established** — carried as declared gap 5 of this pass.

### 🔵 What this adds to the shelf, stated as a rule

The platforms above are mostly **copyleft**, and that decides whether your AI work is a plugin or a
side-car. This tier is different: **assessment delivery and national-service clients are
overwhelmingly permissive**, and they sit exactly at the seam §34 identified — *education's reusable
IP lives at the plugin seam of copyleft platforms, not beside them.* **You will not get a permissive
LMS. You can get a permissive, certified assessment tier and a permissive metadata layer to bolt
onto the copyleft one you inherit.**

## Added in the nineteenth pass of 2026-10-06 — the assistive-technology tier, and the licence verdict that applies to all of it

This page exists for **real systems a client already runs or could run, that AI can be layered
onto**. The assistive-technology estate qualifies on both counts and was never on it: these are the
applications a disabled learner actually operates, they are deployed in schools today, and three of
the four are customisable. Licences read from each repository's own payload on
`raw.githubusercontent.com`, 2026-10-06; counts from the rendered page the same day.

### The tier

| Platform | Repo | Licence (read from payload) | ★ / forks | What it is, and where it sits |
|---|---|---|---|---|
| **Cboard** | [cboard-org/cboard](https://github.com/cboard-org/cboard) | 🔴 **GPL-3.0** (`master/LICENSE.txt`) | **759** | AAC communication board with symbols and text-to-speech, browser-based PWA. **33 languages, 3,400+ Mulberry symbols.** Backed by **UNICEF's Office of Innovation and Microsoft**; © Assistive Technology LLC. Used for cerebral palsy, intellectual disability and autism. 🟢 **The reference AAC deployment in LATAM and the one a ministry will already have heard of.** |
| **AsTeRICS Grid** | [asterics/AsTeRICS-Grid](https://github.com/asterics/AsTeRICS-Grid) | 🔴 **AGPL-3.0** (`master/LICENSE`) | **124 / 65** | AAC app with **offline support**, flexible input (switch, eye-gaze, touch), multilingual TTS, media and smart-home control. JavaScript. **AsTeRICS Foundation + UAS Technikum Wien, funded by the City of Vienna (2018–2025).** 🟢 **EMEA-placed, EU-funded, and offline-capable** — the shape a European municipal tender asks for. ⚠️ **AGPL-3.0: network use triggers source disclosure.** |
| **NVDA** | [nvaccess/nvda](https://github.com/nvaccess/nvda) | 🔴 **GPL-2.0-or-later, with two stated exceptions** (⚠️ `master/copying.txt`) | not read this pass | The dominant free screen reader on Windows, and therefore **the client against which a remediated LMS is actually tested**. ⚠️ **Licence filename note:** `copying.txt` is outside every shortlist this KB probes (`LICENSE*`, `LICENCE`, `COPYING`), so an 11-filename sweep over `main`/`master` reports NVDA as **ungranted** unless lowercase `copying.txt` is in the list. **Add it.** |
| **veraPDF** | [veraPDF/veraPDF-library](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL / MPL** (`LICENSE.GPL` + `LICENSE.MPL`) | not read this pass | The reference **PDF/A and PDF/UA validator**. ⚠️ **Both licence files are named outside every shortlist this KB probes** — `LICENSE.GPL` and `LICENSE.MPL`, present on `master` and on `integration`, absent from `main` — so an 11-filename sweep calls it ungranted while the grant is in the repository root. 🟡 **Invoke it as a CLI, do not vendor it** — then the dual licence stays outside the deliverable. |

### 🔴 The verdict that applies to every row above — do not propose forking any of them

**All four are copyleft, and that is not an accident of this sample.** Searched this pass by
standard, by assistive-technology topic, by AAC, by screen reader and by sign language: **no
permissive end-user assistive application was found in education.** The one apparent exception,
[`sign/translate`](https://github.com/sign/translate), is worse than copyleft — a **non-OSI,
entity-tiered licence** that grants educational institutions free use and **requires a separate
commercial licence for for-profit organisations**, i.e. the client is granted and the integrator is
not (`agents/top.md`).

🟢 **What to do instead, and it is the better business anyway.** The AT applications are the
*client's* deployment, not the studio's product. The permissive work sits **around** them:

1. **Remediate the estate they read.** An LMS, its course content, its PDFs and its ePubs have to
   be navigable by NVDA and by Cboard's switch input. That remediation pipeline is **Apache-2.0 and
   MIT** end to end (`repos/foundations.md`), and it is the deliverable in `compose/patterns.md` P36.
2. **Integrate, don't fork.** Cboard and AsTeRICS Grid both export and import board sets; an
   AI layer that *generates* symbol boards from a lesson plan and hands them over as data touches
   no GPL code. ⚠️ **Generating data for a GPL application does not make your generator GPL.
   Linking into it does.** Keep the boundary at the file format.
3. **Test against them.** NVDA is free and scriptable, so "verified with NVDA" is an evidence line
   a studio can produce at no licence cost — and it is the line that distinguishes a real
   conformance claim from a scanner report.

### Platform selection shortcut — nineteenth-pass additions

| If the client needs… | Take | Why |
|---|---|---|
| An AAC deployment a LATAM ministry will recognise | **Cboard** (GPL-3.0), unforked | UNICEF/Microsoft backing, 33 languages, PWA — deploy and configure, build the AI layer outside it |
| An AAC deployment for a European municipal tender | **AsTeRICS Grid** (AGPL-3.0), unforked | EU-funded, offline-capable, alternative input methods. ⚠️ AGPL on network use |
| To prove a remediated LMS actually works for a blind student | **NVDA** (GPL-2.0+) as a *test client* | Free, scriptable, and the screen reader the user actually has |
| To validate that a PDF is genuinely PDF/UA | **veraPDF** as a *CLI*, not a dependency | Dual-licensed; invoking it keeps the obligation out of the deliverable |
| **To produce** an accessible tagged PDF | 🔴 **Nothing permissive exists** | Searched and not found. Price the tagging as human labour (`repos/foundations.md`) |

---

## Added in the twentieth pass of 2026-10-06 — the transition bucket is a platform-selection input, and nobody had treated it as one

**From the transition-provision channel** (findings in `agents/trending.md`, trend **46** in
`intel/trends.md`, delivery in `compose/patterns.md` under **`P-TRANSITION-EVIDENCE`**).

🔵 **The question this adds to platform selection.** Every selection table in this file asks what a
platform *is* — its licence, its scale, its AI surface. None asks **which transition bucket the
client's deployment of it falls into**, and that is now the variable with the longest lever on cost:
it can be worth four years.

### The three buckets, and what each one makes of the same platform

| Bucket | Who is in it | What the regime gives them | What it costs to leave |
|---|---|---|---|
| **Already in service, public authority** | a ministry, a regional authority, a state university running Moodle, Open edX, Sunbird or an SIS with an AI module already live | 🟢 **EU: until 2030-08-02.** Vietnam: **2027-09-01** for education. Peru: a staged 1–4-year window from Sept 2025 | 🔴 **a change in design** — and the extension does not come back |
| **Already in service, private provider** | a tutoring company, a corporate L&D platform, a private school group | ⚠️ **EU: no extended date — 2027-12-02**, with only the design-stability route available while it lasts | the same change, with two months of runway instead of four years |
| **Not yet in service** | any new deployment, and **any significantly modified existing one** | 🔴 **nothing.** Full Annex III §3 obligations on the day it ships | — |

🔴 **The consequence for this file's own platform shortlist.** A platform is not "AI Act ready" or
not; **a deployment is.** Kolibri, Oppia, Mentingo, Coursemology, Sunbird and OpenMAIC all sit in
whichever bucket the client's circumstances put them in — and the identical technical choice carries
a 2030 date for a state university and a 2027-12-02 date for a private operator. ⚠️ **So record the
buyer's legal form in the selection note, next to the licence.** It is the second field that changes
the answer and the only one this file has never captured.

### What this changes about a platform *migration*

🔴 **A migration is a change in design by construction**, so the standard "move them off the legacy
SIS onto a permissive platform" engagement **forfeits the extension** on the high-risk functions it
carries — admissions scoring, automated grading, placement, proctoring.

🟢 **The sequencing that preserves it, and it is a real delivery option rather than a dodge:**
migrate the **non-high-risk** estate first — content delivery, rostering, administration,
accessibility remediation — and leave the high-risk decision functions on the frozen legacy system,
wrapped in the evidence tier, until the client is ready to pay for conformity on them deliberately.
⚠️ **This is the opposite of the usual advice**, which is to migrate the hard parts first while
budget exists, and the difference is worth stating to the buyer explicitly rather than deciding for
them.

🔵 **And one platform-level note that follows from Vietnam's Decision 33.** Its education category 1
is *"AI systems providing self-learning content using uncontrolled data sources"* — a **corpus**
test, not a decision test. ⚠️ **That catches an RAG tutor bolted onto any of the permissive
platforms on this page**, however benign its pedagogy, unless the corpus is enumerated and
controlled. 🟢 **The platform is not the exposure; the ingestion pipeline is** — which is why
`iterative/dvc` and `great-expectations/great_expectations` (see `repos/foundations.md`) now belong
in a platform conversation that used to be only about licences.
