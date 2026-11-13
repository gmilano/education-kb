---
industry: education
region: Global
updated: 2026-11-13
---

# Education vertical platforms — real systems to customize AI on top of

The education equivalent of "Odoo for ERP". These are the systems institutions
already run; an AI engagement almost always means **adding an agent layer to one
of these**, not replacing it. All licenses and star counts verified 2026-11-13
from the repository page.

## The decision that governs every education engagement

**Do not fork the LMS.** Seven of the eight significant open-source LMS
platforms are GPL-3.0 or AGPL-3.0 (only Sakai is permissive, ECL-2.0). A fork
makes the client's derived platform copyleft. Instead mount the AI layer as an
**LTI 1.3 tool** or an **MCP server** against the platform's API, keep that
layer MIT/Apache, and emit **xAPI** or **Caliper** events so the institution can
report on it. Every pattern in `compose/patterns.md` follows this shape.

## Learning management — the host systems

| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |
|---|---|---|---|---|---|
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.6k | Global, strongest in EMEA, LATAM, APAC public education | Mature plugin API; LTI 1.3; web services REST API |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | MOOCs, corporate academies, national platforms | **`openedx-ai-extensions`** is the official AI plugin point; XBlocks; deploy via `tutor` |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | North American higher ed (dominant) | Rich REST API + LTI 1.3; **`canvas-mcp` (MIT) gives agents 102 tools** |
| Frappe LMS | https://github.com/frappe/lms | AGPL-3.0 | 3.4k | SMB/corporate training, India | Frappe framework hooks; shares a stack with ERPNext |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Research universities | **Permissive license** — the one platform a studio can extend without copyleft reaching the product |
| Chamilo | https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LATAM, francophone Africa, Spain | Web services API; accessibility-first |
| ILIAS | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | German-speaking EMEA, vocational and public sector | Plugin slots; SCORM/xAPI |

## Student information systems and institutional ERP

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | **SIS + LMS + finance as Odoo modules** — the literal "Odoo for education". If the client already runs Odoo, this is the shortest path. |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | K-12 school management; widely deployed in LATAM, Spanish/French/Portuguese localization in core. |
| Gibbon | https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible school management; strong in international K-12 schools. |
| openSIS Classic | https://github.com/OS4ED/openSIS-Classic | GPL (README) | 351 | Student information system; commercial editions available from OS4ED. |
| ERPNext (education context) | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | For institutional finance/HR alongside academics, the Odoo/Frappe ERP families are the two realistic bases. |

## Content, delivery and classroom

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| Kolibri | https://github.com/learningequality/kolibri | **MIT** | 1.2k | Offline-first learning platform. The right base for low-connectivity deployments (rural LATAM, Sub-Saharan Africa, remote APAC). Permissive. |
| Oppia | https://github.com/oppia/oppia | **Apache-2.0** | 7.0k | Interactive lesson "explorations" with built-in misconception handling. Permissive and substantial. |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | The de facto interactive-content format; renders inside Moodle, Canvas, Open edX. |
| Khan Perseus | https://github.com/Khan/perseus | **MIT** | 1.6k | Khan Academy's exercise editor/renderer. MIT — drop real exercise rendering into any product. |
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Virtual classroom with LTI into Moodle/Canvas; recordings feed transcript pipelines. |
| Opencast | https://github.com/opencast/opencast | ECL-2.0 | 511 | Lecture capture at scale — the upstream source for transcript/summarization agents. |
| Anki | https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition scheduling; the algorithm is the asset for retention features. |

## Teaching, grading and learning-data infrastructure

| Platform | Repo | License | Stars | Notes |
|---|---|---|---|---|
| JupyterHub | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user notebooks; the standard for CS/data-science teaching. |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assignment release and autograding for notebooks. **The grading substrate to wrap an agent around.** |
| pyKT | https://github.com/pykt-team/pykt-toolkit | **MIT** | 461 | Deep knowledge-tracing benchmarks — real mastery estimation to pair with an LLM tutor. |
| ODK Collect | https://github.com/getodk/collect | Apache-2.0 | 805 | Offline Android form collection; used for education field assessment at national scale. |
| Caliper | https://github.com/1edtech/caliper-spec | IMS spec-document license | 22 | Learning analytics event spec. Implement it; do not vendor the repo. |

## Standards that make the above interchangeable

| Standard | Why it decides the architecture |
|---|---|
| **LTI 1.3 / LTI Advantage** | Build the AI tool once as an LTI tool provider and it mounts in Moodle, Canvas, Open edX, Sakai, and ILIAS. Highest-leverage single investment in an education engagement. |
| **xAPI** | Learner-activity telemetry; what an agent should emit so the institution can report on it. |
| **Caliper Analytics** | The 1EdTech-native alternative to xAPI; common in North American higher ed. |
| **QTI** | Assessment item interchange — matters as soon as item banks must move between systems. |
| **SCORM** | Legacy but ubiquitous in corporate and vocational training; still the delivery format many EMEA/APAC clients require. |

## Declared gaps

- **No permissively licensed LMS at deployment scale** except Sakai. Surface
  this constraint in week one of any engagement that needs a proprietary
  derived platform.
- **MCP coverage is thin and uneven.** Canvas has a strong MIT MCP server
  (`canvas-mcp`, 324 stars, 102 tools). Open edX has only `openedx-mcp`
  (AGPL-3.0, **3 stars** — reference only). **Moodle has no significant MCP
  server in this window** despite being the most-deployed LMS in the world.
  That is the clearest build opportunity in this file.
