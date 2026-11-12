---
industry: education
region: Global
updated: 2026-11-12
---

# Foundational education repositories — `p787`

**The single most useful fact in this file:** in education, *the famous platforms are copyleft and
the permissive layer is narrow and specific.* Moodle, Open edX, Canvas, Chamilo, ILIAS, Frappe LMS
and ERPNext — the names a client will say out loud — are **GPL or AGPL**. The repositories Globant
can link into proprietary client code are a **different, smaller set**: Kolibri, Oppia, Sakai,
OpenOLAT, Opencast, Tsugi, Perseus, OATutor, JupyterHub/nbgrader and DSpace.

Every grant below was read this pass from the served `LICENSE` bytes by clause presence.
`sha` is the 12-char `HEAD` from `git ls-remote`.

## 🟢 Permissive — build on these, link them, ship them in client code

| Repo | Address | Grant, on the bytes | Region | Role |
|---|---|---|---|---|
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · `1,097 B` · `fe298f54494c` | Global | 🟢 **The most valuable permissive row in education.** Offline-first learning platform: curated openly-licensed content library, teacher tools, sync, runs on low-cost and legacy hardware, downloads once then works with no connectivity. `1.2k★`. Reported in use across 195 countries — the natural substrate for LATAM, African and rural-APAC engagements |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · `11,358 B` · `bbda308fd5db` | Global | Interactive lessons that behave like a one-to-one tutoring conversation; authoring plus delivery. `7.0k★` |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | North America | Full higher-ed LMS under the **Educational Community Licence 2.0 — an Apache-2.0 derivative**, so permissive. The only mature, permissively-granted university LMS in this base |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · `10,982 B` · `322e90dd5507` | EMEA | Swiss-origin university LMS, Apache-2.0. ⚠️ `10,982 B` is `375 B` short of the canonical Apache text — clause-verified as genuine Apache-2.0 (title + `Version 2.0, January 2004`), the deviation is in the trailing appendix. **The permissive LMS for an EMEA engagement** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | **ECL-2.0** · `11,340 B` · `94aecba33ed9` | EMEA | Lecture capture, processing and distribution at university scale; permissive |
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | **Apache-2.0** · `10,273 B` · `f54555227df1` | Global | 🟢 **The licence-firewall component.** Hosts **LTI** tools that plug into Moodle/Canvas/Sakai *across a process boundary*, so permissive or proprietary code can serve a copyleft LMS without linking to it. Canonical owner is `csev`; `tsugi/tsugi` is DEAD |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | **MIT** · `1,052 B` · `e722e959afd0` | North America | Khan Academy's exercise and question rendering engine — the content primitive for interactive assessment |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** · `1,105 B` · `fae8cc474484` | North America | UC Berkeley adaptive tutoring with Bayesian Knowledge Tracing. `279★` |
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | Global | 🟢 Assignment release, collection, **autograding** and feedback for notebooks. The most defensible autograding core available permissively |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** · `1,475 B` · `41fffb935326` | Global | Multi-user notebook serving — the cohort-scale delivery layer under `nbgrader` |
| **Jupyter Notebook** | [`jupyter/notebook`](https://github.com/jupyter/notebook) | **BSD-3-Clause** · `1,588 B` · `5662506ad194` | Global | The notebook surface itself |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | **BSD-3-Clause** · `1,504 B` · `2d991b4832bb` | Global | Institutional repository for theses, OER and research output |
| **Open WebUI** | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | **BSD-3-Clause** · `2,819 B` · `b0e6098e9409` | Global | Self-hosted LLM delivery surface; the quickest compliant front end for a school-hosted model |
| **LangGraph** | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · `1,072 B` · `b4cb0f19e3d8` | Global | Stateful agent graphs — the orchestration layer in most recipes here |
| **smolagents** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · `11,357 B` · `96f33faaf028` | Global | Minimal agent runtime where LangGraph is more than the engagement needs |

## 🔴 Copyleft — real, dominant, and a licensing decision before a line is written

| Repo | Address | Grant, on the bytes | Region | What the grant costs you |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `35,147 B` · `afbcc55fa1bd` | Global | The sector's default LMS. 🔴 Plugins are derivative works — a Moodle plugin must ship GPL-3.0. Keep proprietary logic behind LTI (`Tsugi`) or a web API |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · `35,136 B` · `d3a86602dcf7` | Global | 🔴 **AGPL: serving it over a network triggers source disclosure.** Latest community release line *Verawood* (June 2026, 22nd release) |
| **Tutor** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · `34,523 B` · `bca91d56136f` | Global | The standard Open edX Docker distribution. Canonical owner is `overhangio`; `openedx/tutor` is DEAD |
| **Open Response Assessment** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · `35,135 B` · `0d60a779e29d` | Global | Peer/self/staff assessment for Open edX. Correct address is `edx-ora2`; `openedx/openassessment` is DEAD |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · `34,520 B` · `1c9f0bb8013e` | North America | 🔴 Clause-verified **AGPL-3.0**, settling a conflict in the search channel, which also claimed ECL-2.0. The dominant North American higher-ed LMS |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · `35,147 B` · `e137bded10b5` | EMEA | Belgian/Spanish-origin LMS with the strongest Spanish-language footprint — heavily deployed across LATAM |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · `35,147 B` · `87a79b237fcc` | EMEA | German university LMS, strong in DACH public institutions |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `33,893 B` · `45edbff87486` | APAC | Indian-origin modern LMS on the Frappe stack |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **GPL-3.0** · `34,916 B` · `447313109fdd` | APAC | ERP backbone used for school finance/HR |
| **H5P core** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `35,146 B` · `2d7f937a03c9` | EMEA | Norwegian-origin interactive content types, embedded in Moodle and Canvas |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** · `35,121 B` · `59334a28613f` | Global | School management joined to teaching tools in one system |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · `15,214 B` · `e4cd20a48bf1` | Global | Student Information System with strong Spanish and French localisation — the SIS that fits LATAM deployments |
| **Mahara** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 **GPL-3.0** · `35,148 B` · `0881d0f9c2fe` | Global | ePortfolio. Canonical owner is `MaharaProject`; `mahara/mahara` is DEAD |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 **AGPL-3.0** · `1,930 B` · `a5461e33e3db` | Global | Spaced repetition; the reference implementation of the scheduling model tutors copy |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL** · `7,652 B` · `13b55d45c046` | Global | Virtual classroom built for teaching rather than meetings. LGPL is weaker than GPL — dynamic linking is permitted |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **LGPL-3.0** · `43,529 B` · `75447d905934` | Global | The ERP base under OpenEduCat. ⚠️ `T847`: states LGPL-3.0 on line 3 behind a deferral — a title-line-only probe mis-grades it |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL** · `8,241 B` · `46a5d7d40082` | Global | Odoo-based education ERP — SIS + LMS + finance in one. Same line-3 deferral pattern as Odoo |

## 🟡 EUPL — OSI-approved, copyleft, and the reason this pass fixed its probe

| Repo | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 **EUPL-1.2** · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms; `1,697★`. **The EMEA education anchor this base has** |
| **OOAPI specification** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 **EUPL-1.2** · `13,827 B` · `d9c5b0a1a68d` | EMEA | Open Education API — a **live** interop standard, where this base's Caliper/QTI/LTI cluster is its most dead cluster |

🔵 **`T849`, found on these two rows:** both serve an **identical `13,827 B`** licence, and the probe
graded both `GPL-?` — because **EUPL-1.2 names GPL-2.0, GPL-3.0, AGPL, EPL and CeCILL inside its
compatibility appendix**, and a title-line family check claims the first name it sees. A licence that
*lists other licences* must be matched **before** any family check. Fixed in the probe this pass;
copyleft controls (Moodle, Canvas, Frappe LMS, Anki, BigBlueButton) all still reproduce.

## Counts

| | Count |
|---|---|
| Foundational repos with a byte-verified grant | **35** |
| 🟢 **Permissive** (MIT · Apache-2.0 · BSD-3 · ECL-2.0) | **15** |
| 🔴 Copyleft (GPL · AGPL · LGPL) | **18** |
| 🟡 EUPL-1.2 | **2** |
| Dead addresses corrected to a live canonical owner | **4** — `tsugi/tsugi`→`csev/tsugi`, `openedx/openassessment`→`openedx/edx-ora2`, `mahara/mahara`→`MaharaProject/mahara`, `openedx/tutor`→`overhangio/tutor` |

🔴 **Still grant-less after a re-probe with this pass's language-aware gate** (`p786-E` carried
forward): [`formalms/formalms`](https://github.com/formalms/formalms),
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic),
[`Nutlope/llamatutor`](https://github.com/Nutlope/llamatutor),
[`flyboat403/k12-skills`](https://github.com/flyboat403/k12-skills) — all four ALIVE, none serving a
licence on 8 filenames × 3 branches. 🟢 **The language-aware gate did not rescue them, which
strengthens rather than weakens the verdict:** these are substantial and otherwise usable, so the
deliverable is an upstream licence request, not a permanent exclusion.
