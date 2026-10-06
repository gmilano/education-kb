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
| Kolibri | [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) | **MIT** (`LICENSE`) | Offline-first platform for teaching without internet. **The only fully permissive end-to-end platform on this shelf.** Default choice for low-connectivity, low-budget and equity-driven deployments. |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** (`LICENSE`) | Authoring and delivery of interactive lessons with misconception handling built into the pedagogy. Permissive, and designed for learners with limited educational resources. |

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
