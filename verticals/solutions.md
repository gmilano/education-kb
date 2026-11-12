---
industry: education
region: Global
updated: 2026-11-12
---

# Vertical platforms — real systems an AI layer can sit on top of — `p787`

The pattern that works in education is the Odoo pattern: **take a mature, deployed, customisable
platform that already holds the institution's data, and add agents at its edge.** Nobody replaces a
Student Information System in an engagement. The grants below decide *where* the AI code can live.

## Learning Management — the delivery layer

| Platform | Address | Grant, on the bytes | Region | Where an AI layer attaches |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 · `35,147 B` · `afbcc55fa1bd` | Global | The sector default — if a client has an LMS, assume this. 🔴 A plugin is a derivative work and must be GPL-3.0. 🟢 **Attach through LTI via Tsugi, or Moodle's web services API, and your code stays yours** |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · `35,136 B` · `d3a86602dcf7` | Global | MOOC-scale delivery; deploy with `overhangio/tutor`. 🔴 AGPL network clause — attach as an **XBlock across a service boundary**, never by linking |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 · `34,520 B` · `1c9f0bb8013e` | North America | Dominant in US higher ed. 🟢 Strong LTI 1.3 support — the sanctioned attachment point |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | North America | 🟢 **Permissive and mature.** When a client wants a customised LMS they can own outright, this is the one that does not force disclosure |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10,982 B` · `322e90dd5507` | EMEA | 🟢 The permissive choice for a European university, already trusted in Swiss and German HE |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 · `35,147 B` · `e137bded10b5` | EMEA | 🟢 **The strongest Spanish-language LMS footprint; widely deployed across LATAM ministries and universities** — the incumbent to integrate with, not displace |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 · `35,147 B` · `87a79b237fcc` | EMEA | German public-sector and university installs; SCORM-heavy |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 AGPL-3.0 · `33,893 B` · `45edbff87486` | APAC | Modern Indian-origin LMS; pairs with ERPNext for a full institution stack |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1,097 B` · `fe298f54494c` | Global | 🟢 **The platform for low-connectivity deployments** — offline-first, syncs when a link appears, runs on legacy hardware. MIT, so an AI layer can be embedded directly. First choice for rural LATAM, African and remote-APAC programmes |

## Student Information / School Management — where the institution's data actually lives

| Platform | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL · `8,241 B` · `46a5d7d40082` | Global | 🟢 **The closest thing to "Odoo for education"** — SIS + LMS + finance in one, on Odoo. LGPL permits dynamic linking, so a separate AI module is clean |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 LGPL-3.0 · `43,529 B` · `75447d905934` | Global | The ERP base underneath. ⚠️ `T847`: the grant sits on line 3 behind a deferral |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 · `15,214 B` · `e4cd20a48bf1` | Global | 🟢 Mature SIS with strong **Spanish and French** localisation — the SIS that fits a LATAM or Francophone-African engagement |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 GPL-3.0 · `35,121 B` · `59334a28613f` | Global | School management and teaching in one system; common in international K-12 |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 GPL-3.0 · `34,916 B` · `447313109fdd` | APAC | Finance, HR and procurement for school groups |

## Assessment, content and classroom

| Platform | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | Global | 🟢 **The permissive autograding core.** Release → collect → autograde → feedback, with a human-review step already in the model — which is exactly what EU Annex III and US state grading rules require |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause · `1,475 B` · `41fffb935326` | Global | Cohort-scale serving under nbgrader |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | 🟢 **MIT** · `1,052 B` · `e722e959afd0` | North America | Khan Academy's exercise/question renderer — the content primitive for interactive items |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 · `35,146 B` · `2d7f937a03c9` | EMEA | Interactive content types already embedded in Moodle and Canvas — generate *H5P content*, which is data, not derivative code |
| **edx-ora2** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 · `35,135 B` · `0d60a779e29d` | Global | Open-response, peer and staff assessment — the rubric model to mirror |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** · `11,340 B` · `94aecba33ed9` | EMEA | 🟢 Permissive lecture capture — transcription, chaptering and summarisation attach naturally |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL · `7,652 B` · `13b55d45c046` | Global | Virtual classroom designed for teaching; LGPL allows dynamic linking |
| **Mahara** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 GPL-3.0 · `35,148 B` · `0881d0f9c2fe` | Global | ePortfolio — the natural home for skills-based credentialing |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | 🟢 BSD-3-Clause · `1,504 B` · `2d991b4832bb` | Global | Institutional repository for OER, theses and research output |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 AGPL-3.0 · `1,930 B` · `a5461e33e3db` | Global | The reference spaced-repetition scheduler |

## Interop — the layer that makes all of the above composable

| Component | Address | Grant, on the bytes | Region | Why it matters |
|---|---|---|---|---|
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 **Apache-2.0** · `10,273 B` · `f54555227df1` | Global | 🟢 **The single most useful licensing tool in this file.** Hosts LTI tools that any LMS can launch *across a process boundary* — so permissive or proprietary AI code serves Moodle, Canvas or Sakai **without becoming a derivative work of them** |
| **OOAPI** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 EUPL-1.2 · `13,827 B` · `d9c5b0a1a68d` | EMEA | 🟢 A **live** open education interop standard — courses, offerings, enrolments, results. Where this base's Caliper/QTI/LTI cluster is mostly dead addresses, this one is maintained |
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 EUPL-1.2 · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms, `1,697★`; the EMEA education anchor |
| **Open WebUI** | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🟢 BSD-3-Clause · `2,819 B` · `b0e6098e9409` | Global | Self-hosted chat surface over a school-controlled model — the fastest data-resident front end |

## The rule this file exists to state

🟢 **An engagement's licensing posture is decided by where the AI code sits, not by which LMS the
client runs.** Three safe attachment points, in order of preference:

1. **LTI across a process boundary** (`csev/tsugi`, Apache-2.0) — works with Moodle, Canvas, Sakai,
   Open edX; your code never links to theirs.
2. **The platform's web API / web services** — same boundary, no LTI ceremony.
3. **Generated content rather than generated code** — producing H5P or QTI items is authoring data,
   which carries none of the host platform's copyleft.

🔴 **Only embed directly** — the one case where you may — when the host itself is permissive:
Kolibri (MIT), Sakai (ECL-2.0), OpenOLAT (Apache-2.0), Opencast (ECL-2.0), nbgrader (BSD-3).
