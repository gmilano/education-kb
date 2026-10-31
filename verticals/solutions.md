---
industry: education
region: Global
updated: 2026-10-31
---

# Vertical education platforms (customisable with AI on top)

Real, deployed systems that run an institution's operations — the education
equivalent of Odoo for ERP. These are the systems a client already has, and the
systems an AI layer gets attached to.

## Education ERP / Student Information Systems

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
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
| OpenOlat | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 (README badge; sidebar unnamed) | 449 | EMEA | "Learning Management System OpenOlat," by **frentix GmbH, Switzerland**. A permissively licensed *institutional* LMS — rare, and one a commercial derivative could be built from. |
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
- **Mentingo's maturity is unverified beyond its metadata.** MIT, Poland, xAPI
  and SCORM are confirmed from the API and profile. Whether it can actually carry
  an institutional deployment — SSO, accessibility conformance, data residency,
  migration from Moodle — was **not** tested and should not be implied to a
  client from its presence on this page. 105 open issues on 31 forks is the one
  number that argues for caution.
