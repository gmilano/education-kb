---
industry: education
region: Global
updated: 2026-11-12
---

# Vertical platforms — real systems an AI layer can sit on top of — `p789`

The pattern that works in education is the Odoo pattern: **take a mature, deployed, customisable
platform that already holds the institution's data, and add agents at its edge.** Nobody replaces a
Student Information System in an engagement. The grants below decide *where* the AI code can live.

🔴 **New rule this pass, and it changes the last section of this file.** A permissive host is a
necessary condition for direct embedding, **not a sufficient one**: the host's **dependencies** must
be read too. `oppia/oppia` is Apache-2.0 and depends on an **AGPL-3.0** library; `learningequality/kolibri`
is MIT and depends on two LGPL ones (`T861`). **`Deps` below records the first-layer audit where one
was run; a blank cell means not audited, not clean.**

## Learning Management — the delivery layer

| Platform | Address | Grant, on the bytes | Deps | Region | Where an AI layer attaches |
|---|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 · `35,147 B` · `afbcc55fa1bd` | — | Global | The sector default — if a client has an LMS, assume this. 🔴 A plugin is a derivative work and must be GPL-3.0. 🟢 **Attach through LTI via Tsugi, or Moodle's web services API, and your code stays yours** |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · `35,136 B` · `d3a86602dcf7` | — | Global | MOOC-scale delivery; deploy with `overhangio/tutor`. 🔴 AGPL network clause — attach as an **XBlock across a service boundary**, never by linking |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 AGPL-3.0 · `34,520 B` · `1c9f0bb8013e` | — | North America | Dominant in US higher ed. 🟢 Strong LTI 1.3 support — the sanctioned attachment point |
| **D2L Brightspace** | proprietary SaaS — [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 **New this pass.** The third major North American LMS, and until now the only one with no attachment point in this base. The platform is proprietary; **the MCP server over it is MIT**, which is the whole point — attach, never replace |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | — | North America | 🟢 **Permissive and mature.** When a client wants a customised LMS they can own outright, this is the one that does not force disclosure |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `10,982 B` · `322e90dd5507` | — | EMEA | 🟢 The permissive choice for a European university, already trusted in Swiss and German HE |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 · `35,147 B` · `e137bded10b5` | — | EMEA | 🟢 **The strongest Spanish-language LMS footprint; widely deployed across LATAM ministries and universities** — the incumbent to integrate with, not displace |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 · `35,147 B` · `87a79b237fcc` | — | EMEA | German public-sector and university installs; SCORM-heavy |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 AGPL-3.0 · `33,893 B` · `45edbff87486` | — | APAC | Modern Indian-origin LMS; pairs with ERPNext and `frappe/education` for a full institution stack |
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 **MIT** · `1,097 B` · `fe298f54494c` | 🟡 **2 LGPL of 32** | Global | 🟢 **Still the platform for low-connectivity deployments** — offline-first, syncs when a link appears, runs on legacy hardware. First choice for rural LATAM, African and remote-APAC programmes. ⚠️ **Two LGPL dependencies**: dynamic linking is permitted so this remains usable, but the components must stay replaceable with source available |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 · `11,358 B` · `bbda308fd5db` | 🔴 **1 AGPL-3.0 of 171** | Global | Interactive lessons that behave like one-to-one tutoring, `7.0k★`. 🔴 **DO NOT ship as-is: `angular-shepherd` is AGPL-3.0 and a browser bundle is network delivery.** Replace or remove it, then embed freely |

## Student Information / School Management — where the institution's data actually lives

| Platform | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL · `8,241 B` · `46a5d7d40082` | Global | 🟢 **The closest thing to "Odoo for education"** — SIS + LMS + finance in one, on Odoo. LGPL permits dynamic linking, so a separate AI module is clean |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 LGPL-3.0 · `43,529 B` · `3ce3a7dc8ecb` | Global | The ERP base underneath. ⚠️ `T847`: the grant sits on line 3 behind a deferral |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 GPL-2.0 · `15,214 B` · `e4cd20a48bf1` | Global | 🟢 Mature SIS with strong **Spanish and French** localisation — the SIS that fits a LATAM or Francophone-African engagement |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 GPL-3.0 · `35,121 B` · `59334a28613f` | Global | School management and teaching in one system; common in international K-12 |
| **Frappe Education** | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0** · **`19 B`** · `61408d3da518` | APAC | Frappe's school-management module: admissions, programmes, fees, assessment. 🔵 **The shortest grant in this base and a real one** — the whole `license.txt` reads `License: GNU GPL V3` |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 GPL-3.0 · `34,916 B` · `447313109fdd` | APAC | Finance, HR and procurement for school groups |
| 🔴 **nextSIS** | [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | 🔴 **PROPRIETARY** · `39,890 B` · `60e422c7d93e` | Global | 🔴 **Named here only so it is not mistaken for an option.** All rights reserved. Previously filed in this base as merely "ungranted" |

## Assessment, content and classroom

| Platform | Address | Grant, on the bytes | Deps | Region | Note |
|---|---|---|---|---|---|
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | 🟢 **0 of 18** | Global | 🟢 **The permissive autograding core, and the cleanest audit in this file.** Release → collect → autograde → feedback, with a human-review step already in the model — exactly what EU Annex III, Korea's AI Basic Act and US state grading rules require |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | 🟢 BSD-3-Clause · `1,475 B` · `41fffb935326` | — | Global | Cohort-scale serving under nbgrader |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** · `1,105 B` · `fae8cc474484` | 🟢 **0 of 43** | North America | UC Berkeley Bayesian Knowledge Tracing — the mastery model. 🟢 Clean to the first layer |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | 🟢 **MIT** · `1,052 B` · `e722e959afd0` | — | North America | Khan Academy's exercise/question renderer — the content primitive for interactive items |
| **xAPI service** | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | 🟢 **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **New to this file, and it closes a real hole: a Learning Record Store under MIT.** Every "audit trail" claim in this base previously had to hand-roll its storage. Pair with [`xapi-validation`](https://github.com/LearningLocker/xapi-validation) (MIT, `1,070 B`) |
| **H5P** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 GPL-3.0 · `35,146 B` · `2d7f937a03c9` | — | EMEA | Interactive content types already embedded in Moodle and Canvas — generate *H5P content*, which is data, not derivative code |
| **edx-ora2** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 AGPL-3.0 · `35,135 B` · `0d60a779e29d` | — | Global | Open-response, peer and staff assessment — the rubric model to mirror |
| 🔴 **INGInious** | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · `34,764 B` · `98d56ade0351` | — | EMEA | Automated grading from UCLouvain — a real, mature European platform in the **regulated** surface. 🔴 AGPL **and** ⚠️ **SCOPE-LIMITED**: its licence covers *"most of the files"* and defers the rest to per-file notices. **Study it; do not vendor it** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | 🟢 **ECL-2.0** · `11,340 B` · `94aecba33ed9` | — | EMEA | 🟢 Permissive lecture capture — transcription, chaptering and summarisation attach naturally |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL · `7,652 B` · `13b55d45c046` | — | Global | Virtual classroom designed for teaching; LGPL allows dynamic linking |
| **MyScriptJS** | [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | 🟢 **Apache-2.0 (by reference)** · `570 B` · `968021fcc1f4` | — | EMEA | 🟢 Handwriting and **maths** input recognition, French origin — the input primitive for a maths tutor on a tablet. Rescued from this base's unusable class this pass |
| **Mahara** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 GPL-3.0 · `35,148 B` · `0881d0f9c2fe` | — | Global | ePortfolio — the natural home for skills-based credentialing |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | 🟢 BSD-3-Clause · `1,504 B` · `2d991b4832bb` | — | Global | Institutional repository for OER, theses and research output |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 AGPL-3.0 · `1,930 B` · `a5461e33e3db` | — | Global | The reference spaced-repetition scheduler. 🟢 For a permissive recurrence primitive instead, use [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) (BSD-3, `3,493 B`) |
| **ODK Collect** | [`getodk/collect`](https://github.com/getodk/collect) | 🟢 **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | 🟢 Offline mobile data collection — the field instrument for a readiness diagnostic or a baseline survey where connectivity fails |
| 🔴 **Metabase** | [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 **SPLIT BY DIRECTORY** · `855 B` · `6006cc9c65dd` | — | Global | Frequently the BI layer a client already runs over learning data. 🔴 **AGPL-3.0 outside `enterprise/`, Metabase Commercial License inside it.** Deploy it; do not vendor code out of it without deciding which side of the boundary you are on |

## 🟢 School operations — timetabling, substitution and behaviour (`p789`)

🟢 **New category this pass, and it is the one with the clearest architecture.** The permissive
supply here is **solvers plus approval gates**, not conversational agents — which means the AI layer
sits at the *edges* of a deterministic core, reading intent and explaining outcomes, never deciding
the schedule itself.

| Platform / component | Address | Grant | What an AI layer attaches to |
|---|---|---|---|
| 🟢 **Timefold** (via case study) | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | A **constraint solver** on Quarkus. The LLM turns plain-English policy into constraints and explains rejections; the solver produces the timetable |
| 🟢 **OR-Tools** (via Timable) | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | Clash-free, priority-aware scheduling with a Streamlit surface — the second independent solver |
| 🟢 **schoolflow-agent** | [`Zahraishag/schoolflow-agent`](https://github.com/Zahraishag/schoolflow-agent) | 🟢 MIT · `1,081 B` · `1b7481d92d0f` | **Disruption handling** — absences and substitutions — with a **human approval step** before any schedule is written |
| 🟢 **ClassCharts** (via agent) | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | 🇬🇧 A live UK homework/behaviour MIS, attached **read-only** on a parent account |
| 🟢 **D2L Brightspace** (via MCP) | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | 🟢 MIT · `1,200 B` · `a873478a6b4e` | The third major North American LMS, over MCP |
| 🔴 **School ERP** (via MCP) | [`NSK-394/schoolbridge-mcp`](https://github.com/NSK-394/schoolbridge-mcp) | 🔴 **ungranted** | **Role-based** agent access to attendance, fees and student records. 🔵 The right control surface, no grant — an upstream licence request |

🔴 **The caution this section exists to state.** Timetabling, attendance and safeguarding touch
children's personal data and, in the EU, sit close to the high-risk boundary when they feed
decisions about individuals. 🟢 The read-only attachment (`classcharts-agent`) and the approval gate
(`schoolflow-agent`) are not conveniences — **they are the two design choices that keep this
category deployable**, and both already exist in permissive code.

## Interop — the layer that makes all of the above composable

| Component | Address | Grant, on the bytes | Region | Why it matters |
|---|---|---|---|---|
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | 🟢 **Apache-2.0** · `10,273 B` · `f54555227df1` | Global | 🟢 **The single most useful licensing tool in this file.** Hosts LTI tools that any LMS can launch *across a process boundary* — so permissive or proprietary AI code serves Moodle, Canvas or Sakai **without becoming a derivative work of them** |
| **OOAPI** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 EUPL-1.2 · `13,827 B` · `d9c5b0a1a68d` | EMEA | 🟢 A **live** open education interop standard — courses, offerings, enrolments, results |
| **European Learning Model** | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 EUPL-1.2 · `13,865 B` · `9d7c5d220022` | EMEA | 🟢 **The European Commission's own** learning and credential data model — the vocabulary an EU public-sector client is most likely to be asked to speak. Rescued from the ungranted class this pass |
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 EUPL-1.2 · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms, `1,697★` |
| **Open WebUI** | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | 🟢 BSD-3-Clause · `2,819 B` · `b0e6098e9409` | Global | Self-hosted chat surface over a school-controlled model — the fastest data-resident front end |

## The rule this file exists to state — amended this pass

🟢 **An engagement's licensing posture is decided by where the AI code sits, not by which LMS the
client runs.** Three safe attachment points, in order of preference:

1. **LTI across a process boundary** (`csev/tsugi`, Apache-2.0) — works with Moodle, Canvas, Sakai,
   Open edX; your code never links to theirs. For D2L Brightspace, the equivalent is
   `brightspace-d2l-mcp` (MIT).
2. **The platform's web API / web services** — same boundary, no LTI ceremony.
3. **Generated content rather than generated code** — producing H5P or QTI items is authoring data,
   which carries none of the host platform's copyleft.

🔴 **Only embed directly when the host itself is permissive — AND its dependencies have been read.**
That second clause is new, and it is the whole point of `T861`:

| Host | Repo grant | First-layer deps | Embed directly? |
|---|---|---|---|
| `jupyter/nbgrader` | BSD-3 | 🟢 `0` of `18` copyleft | 🟢 **Yes** |
| `CAHLR/OATutor` | MIT | 🟢 `0` of `43` copyleft | 🟢 **Yes** |
| `learningequality/kolibri` | MIT | 🟡 `2` LGPL of `32` | 🟡 **Yes, with the LGPL components kept replaceable and their source available** |
| `oppia/oppia` | Apache-2.0 | 🔴 `1` **AGPL-3.0** of `171` | 🔴 **Not until `angular-shepherd` is removed or replaced** |
| `sakaiproject/sakai` · `OpenOLAT` · `opencast` | ECL-2.0 / Apache-2.0 | ⚪ not audited | 🟡 **Permissive at the root; audit before shipping** |

🔵 **And one more rule, from `T864`.** In education the **content** has a rights-holder and the
repository is the cheap part. Exam items, textbooks and curricula belong to ministries, universities
and publishers — `paes-mcp`'s MIT grant covers its code and explicitly not Chile's PAES papers, which
belong to DEMRE. **Read the scope clause. Ask who owns the content.**
