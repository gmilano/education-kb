---
industry: education
region: Global
updated: 2026-11-12
---

# Foundational education repositories — `p790`

**The single most useful fact in this file, carried:** in education, *the famous platforms are
copyleft and the permissive layer is narrow and specific.* Moodle, Open edX, Canvas, Chamilo,
ILIAS, Frappe LMS and ERPNext — the names a client will say out loud — are **GPL or AGPL**.

🟢 **`p790` adds one name to that list, and takes it off a different one.** [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS)
— a named **Student Information System** — was published by this base for two passes as
**`PROPRIETARY`**. It is **`GPL-3.0`**. Its `39,890 B` `license.txt` is a licence **anthology**
(§2 nextSIS's own full operative GPL-3.0, §3 **CodeIgniter**/EllisLab, §4 **Twitter Bootstrap**), and
the single `All rights reserved.` this base graded on sits at line `703`, inside EllisLab's section,
two lines above EllisLab's own grant of permission. 🟢 **The carried sentence therefore holds more
strongly, not less: the open SIS is copyleft too.** 🔴 And the correction is a method change —
**a licence file that quotes other licences cannot be graded by substring presence** (`T875`). Read
the tree, never a filename list:

```bash
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/OWNER/REPO /tmp/x
git -C /tmp/x ls-tree -r --name-only HEAD | grep -iE 'licen|copying|legal|terms|notice'
```

🟢 **`221` files enumerated, one match (`license.txt`, lowercase), no blobs downloaded.** `raw` is
case-sensitive, so a candidate-filename probe produces **false absences** — which is what both
`p789` and this pass's first instrument produced on this very row.

🔴 **The single most useful fact ADDED this pass (`T861`):** a permissive repository grant tells you
nothing about its dependencies, and **4 of the 7 highest-star permissive education repos carry
copyleft in their declared direct dependencies.** The `Deps` column below records the first-layer
audit where one was run. **A blank `Deps` cell means not audited, not clean.**

Every grant below was read this pass from the served `LICENSE` bytes by clause presence, with the
title found by scanning for a line that *is* a licence title at any depth (`T863`). `sha` is the
12-char `HEAD` from `git ls-remote`.

## 🟢 Permissive — build on these, link them, ship them in client code

| Repo | Address | Grant, on the bytes | Deps | Region | Role |
|---|---|---|---|---|---|
| **Kolibri** | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** · `1,097 B` · `fe298f54494c` | 🟡 **2 LGPL of 32** | Global | 🟢 **Still the most valuable permissive row in education.** Offline-first learning platform: curated openly-licensed content library, teacher tools, sync, runs on low-cost and legacy hardware, downloads once then works with no connectivity. `1,176★`, reported in use across 195 countries. ⚠️ **`zeroconf-py2compat` (LGPL-2) and `json-schema-validator` (LGPL)** — dynamic linking is permitted, so usable; the components must stay replaceable with source available |
| **Oppia** | [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** · `11,358 B` · `bbda308fd5db` | 🔴 **1 AGPL-3.0 of 171** | Global | Interactive lessons that behave like a one-to-one tutoring conversation. `7.0k★`. 🔴 **DO NOT ship as-is: `angular-shepherd` is AGPL-3.0, and a browser bundle is network delivery.** Remove or replace it first |
| **Sakai** | [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** · `11,120 B` · `593c74e1c7a5` | — | North America | Full higher-ed LMS under the **Educational Community Licence 2.0 — an Apache-2.0 derivative**, so permissive. The only mature, permissively-granted university LMS in this base |
| **OpenOLAT** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** · `10,982 B` · `322e90dd5507` | — | EMEA | Swiss-origin university LMS. ⚠️ `375 B` short of the canonical Apache text — clause-verified genuine, the deviation is in the trailing appendix. **The permissive LMS for an EMEA engagement** |
| **Opencast** | [`opencast/opencast`](https://github.com/opencast/opencast) | **ECL-2.0** · `11,340 B` · `94aecba33ed9` | — | EMEA | Lecture capture, processing and distribution at university scale; permissive |
| **Tsugi** | [`csev/tsugi`](https://github.com/csev/tsugi) | **Apache-2.0** · `10,273 B` · `f54555227df1` | — | Global | 🟢 **The licence-firewall component.** Hosts **LTI** tools that plug into Moodle/Canvas/Sakai *across a process boundary*, so permissive or proprietary code can serve a copyleft LMS without linking to it. Canonical owner is `csev`; `tsugi/tsugi` is DEAD |
| **Perseus** | [`Khan/perseus`](https://github.com/Khan/perseus) | **MIT** · `1,052 B` · `e722e959afd0` | — | North America | Khan Academy's exercise and question rendering engine — the content primitive for interactive assessment |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** · `1,105 B` · `fae8cc474484` | 🟢 **0 of 43** | North America | UC Berkeley adaptive tutoring with Bayesian Knowledge Tracing. `279★`. 🟢 **The cleanest dependency tree measured this pass** |
| **nbgrader** | [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | **BSD-3-Clause** · `1,512 B` · `91d5c12f989b` | 🟢 **0 of 18** | Global | 🟢 Assignment release, collection, **autograding** and feedback for notebooks. **The most defensible autograding core available permissively — and it audits clean to the first layer**, which is why `P788-1` rests on it |
| **JupyterHub** | [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | **BSD-3-Clause** · `1,475 B` · `41fffb935326` | — | Global | Multi-user notebook serving — the cohort-scale delivery layer under `nbgrader` |
| **Jupyter Notebook** | [`jupyter/notebook`](https://github.com/jupyter/notebook) | **BSD-3-Clause** · `1,588 B` · `5662506ad194` | — | Global | The notebook surface itself |
| **DSpace** | [`DSpace/DSpace`](https://github.com/DSpace/DSpace) | **BSD-3-Clause** · `1,504 B` · `2d991b4832bb` | — | Global | Institutional repository for theses, OER and research output |
| **Open WebUI** | [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | **BSD-3-Clause** · `2,819 B` · `b0e6098e9409` | — | Global | Self-hosted LLM delivery surface; the quickest compliant front end for a school-hosted model |
| **LangGraph** | [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | **MIT** · `1,072 B` · `b4cb0f19e3d8` | — | Global | Stateful agent graphs — the orchestration layer in most recipes here |
| **smolagents** | [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | **Apache-2.0** · `11,357 B` · `96f33faaf028` | — | Global | Minimal agent runtime where LangGraph is more than the engagement needs |
| **xAPI service** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **Rescued from this base's ungranted class.** An xAPI **Learning Record Store** service under MIT. This base called its Caliper/QTI/xAPI cluster "its most dead cluster"; the live, permissive half was filed as an absence. **This is the component an audit-trail claim actually needs** |
| **xAPI validation** `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | **MIT** · `1,070 B` · `13ffff748515` | — | Global | xAPI statement validation — rescued alongside the above |
| **eagle-aig** `NEW` | [`LIST-LUXEMBOURG/eagle-aig`](https://github.com/LIST-LUXEMBOURG/eagle-aig) | **Apache-2.0** · `11,358 B` · `99cecb066ecf` | — | EMEA | 🟢 **Luxembourg Institute of Science and Technology** — a national public research institute, permissively granted. Rescued from the ungranted class |
| **brightspace-d2l-mcp** `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 MCP server over **D2L Brightspace** — the third major North American LMS, and the first attachment point this base has for it |
| **ODK Collect** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | Offline mobile data collection — the field instrument for a readiness diagnostic where connectivity fails |
| **elimu-ai** (7 repos) `NEW` | [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) · [`appstore`](https://github.com/elimu-ai/appstore) · [`launcher`](https://github.com/elimu-ai/launcher) · [`model`](https://github.com/elimu-ai/model) · [`ml-authentication`](https://github.com/elimu-ai/ml-authentication) · [`ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) · [`ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | **MIT** · `1,065 B` each · shas in `agents/top.md` | — | EMEA | 🟢 **A 66-repository MIT African education ecosystem, pushed this week** — Android delivery without an app store, a shared data model, and **ML models for storybook reading level and recommendation**. 🔵 This base was already citing `elimu-ai` and had never placed it |
| **rrule** `NEW` | [`jkbrzt/rrule`](https://github.com/jkbrzt/rrule) | **BSD-3-Clause** · `3,493 B` · `9f2061febeeb` | — | Global | Recurrence rules — the scheduling primitive under timetabling and spaced review. 🔵 Grant served at `LICENCE`, the **British spelling**, which a US-spelling-only probe misses |
| **annotated DL implementations** `NEW` | [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT** · `1,082 B` · `db59a04a8a2c` | — | Global | Annotated paper implementations — a teaching corpus under a permissive grant. Rescued from the ungranted class |
| **MyScriptJS** `NEW` | [`MyScript/MyScriptJS`](https://github.com/MyScript/MyScriptJS) | **Apache-2.0 (by reference)** · `570 B` · `968021fcc1f4` | — | EMEA | Handwriting and maths-input recognition (French origin). 🟢 **Rescued: `p786` filed this `570 B` file as a "proprietary notice".** It is the standard Apache-2.0 grant-by-reference boilerplate, URL and AS-IS clause included. 🔴 **It was dismissed for being short — the exact error `T845` forbids** |

## 🟢 Permissive rows added this pass (`p789`)

| Repo | Address | Grant, on the bytes | Region | Why it is foundational |
|---|---|---|---|---|
| 🟢 **Timable** `NEW` | [`Nayak-indie/Timable`](https://github.com/Nayak-indie/Timable) | 🟢 Apache-2.0 · `11,357 B` · `c71d239df917` | Global | **OR-Tools** timetabling — a real constraint solver under a permissive grant. The scheduling primitive this base had no row for |
| 🟢 **school-timetable-timefold-case-study** `NEW` | [`paoloantinori/school-timetable-timefold-case-study`](https://github.com/paoloantinori/school-timetable-timefold-case-study) | 🟢 MIT · `1,081 B` · `12e2a597e655` | Global | **Timefold** solver on Quarkus, driven by coding agents — the reference wiring for `P789-1` |
| 🟢 **jp-k12-digital-ai-textbook** `NEW` | [`masa-san-jp/jp-k12-digital-ai-textbook`](https://github.com/masa-san-jp/jp-k12-digital-ai-textbook) | 🟢 MIT · `1,068 B` · `d7c583c9f444` | APAC 🇯🇵 | A `12`-grade curriculum tree aligned to the **next 学習指導要領** and the **UNESCO AI Competency Framework** — content infrastructure, not an app |
| 🟢 **classcharts-agent** `NEW` | [`shan8851/classcharts-agent`](https://github.com/shan8851/classcharts-agent) | 🟢 MIT · `1,066 B` · `65ef4f07f833` | EMEA 🇬🇧 | A **read-only** attachment to a live UK school MIS — this base's second EMEA LMS/MIS attachment point |

## 🟢 BSL-1.0 (Boost) — a licence family new to this base (`p789`)

| Repo | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| 🟢 **nextgen-learn** `NEW` | [`daddysystem/nextgen-learn`](https://github.com/daddysystem/nextgen-learn) | 🟢 **BSL-1.0 · `1,338 B` · `c9bff7573892`** | EMEA 🇿🇦 | Free **CAPS**-curriculum study site with an AI tutor |

🟢 **Boost-1.0 is permissive, OSI-approved, and in one respect *weaker* than MIT:** it waives the
attribution requirement for distribution in object-code-only form. Nothing in it restricts
commercial use, linking or relicensing of derivatives.
🔴 **It is also the pass's sixth instrument defect, and the reason it is called out here:**
**BSL-1.0 opens with MIT's exact sentence** — *"Permission is hereby granted, free of charge, to
any person or organization obtaining a copy"*. A phrase-matching probe grades it MIT. Only the
title separates them. 🔵 `BSL-1.0` must not be confused with the **Business Source License
(BUSL-1.1)**, which is *not* open source; the SPDX id `BSL-1.0` is Boost.

## 🔴 `T872` — The second dependency layer, and a first-layer audit is a screen not a clearance

🟢 **`ACTION p788-D` discharged, bounded, with the boundary stated first: layer 2 only.**
`jupyter/nbgrader` → **`18`** declared direct runtime dependencies (🟢 the exact count `p788`
recorded — a control on this channel) → **`65`** new transitive packages at layer 2.
Each grant read **PEP 639 `license_expression` first**, then classifiers, then the free-text field,
because `p788` recorded PEP 639 blindness as a defect; **`28` of the `65` are decided by
`license_expression`** and a classifier-only instrument would read them `UNDECLARED`.

| Package | Grant | Enters through | Effect |
|---|---|---|---|
| 🔴 **`certifi`** | **MPL-2.0** | 🔴 `requests` → `certifi` | 🟡 **File-level copyleft.** Triggers on modifying `certifi`'s own files; linking and redistribution are clean. Nobody modifies a CA bundle — **but the graph is no longer "no copyleft"** |
| 🔴 **`paramiko`** | **LGPL-2.1** (PEP 639) | 🔴 `jupyter-client` → `paramiko` | 🟡 **Weak copyleft, dynamic linking permitted.** 🔴 It arrives via `jupyter-client`, a *core* runtime dependency of every Jupyter-based grading stack — not an optional extra |
| 🟡 `pytest-ruff` | **UNDECLARED** | `setuptools` → `pytest-ruff` | 🔵 Build/test-time only. Recorded because an undeclared grant is a fact, not an omission |

🟢 **The other `62` are permissive** — MIT, BSD-2/3-Clause, Apache-2.0, ISC, PSF-2.0 — including
three SPDX **compound** expressions that are mis-read in opposite directions: `packaging` is
`Apache-2.0 OR BSD-2-Clause` (**an election**, both permissive), `prometheus-client` is
`Apache-2.0 AND BSD-2-Clause` (**cumulative — both apply**), and `jupyter-builder` is
`Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT`.

🟢 **Verdict for `P788-1`, which rests on `nbgrader`: it still holds, and its licensing claim is now
weaker and true.** What changes is the sentence a client is told — not *"the grading component's
dependencies are entirely permissive"*, which was true only of layer 1, but *"its graph includes
MPL-2.0 and LGPL-2.1 at layer 2, both weak copyleft, neither triggered by the way we deploy it."*

## 🔴 Copyleft — real, dominant, and a licensing decision before a line is written

| Repo | Address | Grant, on the bytes | Region | What the grant costs you |
|---|---|---|---|---|
| **Moodle** | [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 **GPL-3.0** · `35,147 B` · `afbcc55fa1bd` | Global | The sector's default LMS. 🔴 Plugins are derivative works — a Moodle plugin must ship GPL-3.0. Keep proprietary logic behind LTI (`Tsugi`) or a web API |
| **Open edX** | [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** · `35,136 B` · `d3a86602dcf7` | Global | 🔴 **AGPL: serving it over a network triggers source disclosure.** Community release line *Verawood* (June 2026, 22nd release) |
| **Tutor** | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **AGPL-3.0** · `34,523 B` · `bca91d56136f` | Global | The standard Open edX Docker distribution. Canonical owner is `overhangio`; `openedx/tutor` is DEAD |
| **Open Response Assessment** | [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · `35,135 B` · `0d60a779e29d` | Global | Peer/self/staff assessment for Open edX. Correct address is `edx-ora2`; `openedx/openassessment` is DEAD |
| **Canvas LMS** | [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** · `34,520 B` · `1c9f0bb8013e` | North America | Clause-verified AGPL-3.0, settling a search-channel conflict that also claimed ECL-2.0. The dominant North American higher-ed LMS |
| **Chamilo** | [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 **GPL-3.0** · `35,147 B` · `e137bded10b5` | EMEA | Belgian/Spanish-origin LMS with the strongest Spanish-language footprint — heavily deployed across LATAM |
| **ILIAS** | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **GPL-3.0** · `35,147 B` · `87a79b237fcc` | EMEA | German university LMS, strong in DACH public institutions |
| **Frappe LMS** | [`frappe/lms`](https://github.com/frappe/lms) | 🔴 **AGPL-3.0** · `33,893 B` · `45edbff87486` | APAC | Indian-origin modern LMS on the Frappe stack |
| **Frappe Education** `NEW` | [`frappe/education`](https://github.com/frappe/education) | 🔴 **GPL-3.0** · **`19 B`** · `61408d3da518` | APAC | Frappe's school-management module. 🔵 **The shortest grant in this base, and it is a real one:** the entire `license.txt` reads `License: GNU GPL V3`. 🔴 A probe matching only expanded licence names scores it `UNGRADED` (`T863`) |
| **ERPNext** | [`frappe/erpnext`](https://github.com/frappe/erpnext) | 🔴 **GPL-3.0** · `34,916 B` · `447313109fdd` | APAC | ERP backbone used for school finance/HR |
| **H5P core** | [`h5p/h5p-php-library`](https://github.com/h5p/h5p-php-library) | 🔴 **GPL-3.0** · `35,146 B` · `2d7f937a03c9` | EMEA | Norwegian-origin interactive content types, embedded in Moodle and Canvas |
| **Gibbon** | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **GPL-3.0** · `35,121 B` · `59334a28613f` | Global | School management joined to teaching tools in one system |
| **RosarioSIS** | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **GPL-2.0** · `15,214 B` · `e4cd20a48bf1` | Global | Student Information System with strong Spanish and French localisation — the SIS that fits LATAM deployments |
| **Mahara** | [`MaharaProject/mahara`](https://github.com/MaharaProject/mahara) | 🔴 **GPL-3.0** · `35,148 B` · `0881d0f9c2fe` | Global | ePortfolio. Canonical owner is `MaharaProject`; `mahara/mahara` is DEAD |
| **Anki** | [`ankitects/anki`](https://github.com/ankitects/anki) | 🔴 **AGPL-3.0** · `1,930 B` · `a5461e33e3db` | Global | Spaced repetition; the reference implementation of the scheduling model tutors copy |
| **BigBlueButton** | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **LGPL** · `7,652 B` · `13b55d45c046` | Global | Virtual classroom built for teaching rather than meetings. LGPL is weaker than GPL — dynamic linking is permitted |
| **Odoo** | [`odoo/odoo`](https://github.com/odoo/odoo) | 🔴 **LGPL-3.0** · `43,529 B` · `3ce3a7dc8ecb` | Global | The ERP base under OpenEduCat. ⚠️ `T847`: states LGPL-3.0 on line 3 behind a deferral. 🔵 `HEAD` moved from `75447d905934` since `p787` |
| **OpenEduCat** | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **LGPL** · `8,241 B` · `46a5d7d40082` | Global | Odoo-based education ERP — SIS + LMS + finance in one. Same line-3 deferral pattern as Odoo |
| **INGInious** `NEW` | [`INGInious/INGInious`](https://github.com/INGInious/INGInious) | 🔴 **AGPL-3.0** · `34,764 B` · `98d56ade0351` | EMEA | Automated-grading platform (UCLouvain, BE) — **directly in the regulated assessment surface**. ⚠️ **Also SCOPE-LIMITED:** its licence states *"most of the files … if it is not the case, this is clearly indicated in the files"*, so a per-file audit is required before any reuse |
| **OpenTreeMap otm-core** `NEW` | [`OpenTreeMap/otm-core`](https://github.com/OpenTreeMap/otm-core) | 🔴 **AGPL-3.0** · `35,366 B` · `b26aec8c9e7c` | North America | Newly graded out of the bespoke bucket; prose preamble before the title line |

## 🟡 EUPL — OSI-approved, copyleft, and the reason a prior pass fixed its probe

| Repo | Address | Grant, on the bytes | Region | Note |
|---|---|---|---|---|
| **Hedy** | [`hedyorg/hedy`](https://github.com/hedyorg/hedy) | 🟡 **EUPL-1.2** · `13,827 B` · `38d5db7214ff` | EMEA | Gradual programming language for classrooms; `1,697★`. A long-standing EMEA education anchor |
| **OOAPI specification** | [`open-education-api/specification`](https://github.com/open-education-api/specification) | 🟡 **EUPL-1.2** · `13,827 B` · `d9c5b0a1a68d` | EMEA | Open Education API — a **live** interop standard |
| **European Learning Model** `NEW` | [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 **EUPL-1.2** · `13,865 B` · `9d7c5d220022` | EMEA | 🟢 The **European Commission's own** learning/credential data model. Re-verified out of the ungranted class. 🔵 `13,865 B` against Hedy's `13,827 B` — **two EUPL-1.2 texts differing by `38 B`**, which is why length is never a verdict |

🔵 **`T849`, carried:** EUPL-1.2 **names GPL-2.0, GPL-3.0, AGPL, EPL and CeCILL inside its
compatibility appendix**, so a licence that *lists other licences* must be matched **before** any
family check. Verified again this pass: all copyleft controls still reproduce.

## 🔴 Not open source — measured this pass, reason on the bytes

| Address | Grant, on the bytes | Why it is barred |
|---|---|---|
| [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | 🔴 **PROPRIETARY** · `39,890 B` · `60e422c7d93e` | A named Student Information System with an all-rights-reserved grant. 🔵 Previously filed merely "ungranted". **A `39,890 B` licence is a long licence, not an open one** |
| [`metabase/metabase`](https://github.com/metabase/metabase) | 🔴 **SPLIT BY DIRECTORY** · `855 B` · `6006cc9c65dd` | AGPL-3.0 outside `enterprise/`, **Metabase Commercial License** inside it. 🟢 Reporting one family for this repo would itself be the error — the boundary is the fact. Common BI layer under learning-analytics dashboards |
| [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | 🔴 **PROPRIETARY** · `1,296 B` · `aa476a6a6a03` | Source-available multi-agent learning OS; now graded rather than `UNGRADED` |
| [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) | 🔴 **CC BY-NC-SA 4.0 (Spanish), SCOPE-LIMITED** · `362 B` · `9ed32d5c2577` | Spanish school-leadership regulation. 🔴 **This base's published reason was wrong** — see `T863`. NonCommercial bars a commercial deliverable, and the BOE/BOC statutory texts are excluded from the grant entirely |
| [`TarrySingh/…-Machine-Learning-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 🔴 **CC-NonCommercial** · `20,850 B` · `bac3481e8d78` | `4,025★`. NonCommercial cannot be cured by asking. 🔵 `HEAD` moved from `e66c269d4819` since `p786` |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) · [`1edtech/caliper-spec`](https://github.com/1edtech/caliper-spec) | 🔵 `UNGRADED` · `8,563 B` · `e1de68833d1c` / `12,402 B` · `1849e118b47a` | Bespoke *PageLM Community License* and 1EdTech consortium terms. 🟢 **`UNGRADED` is the correct verdict**, not a failure — forcing either into an OSI family is the error `T845`–`T849` keep catching |

## Counts

| | Count |
|---|---|
| Foundational repos with a byte-verified grant | **53** (was 48) |
| 🟢 **Permissive** (MIT · Apache-2.0 · BSD-3 · ECL-2.0 · **BSL-1.0**) | **29** (was 24) |
| 🔴 Copyleft (GPL · AGPL · LGPL) | **20** |
| 🟡 EUPL-1.2 | **3** |
| 🟢 **BSL-1.0 (Boost)** — new family this pass | **1** |
| 🔴 Not open source (proprietary · NonCommercial · split · bespoke) | **5** — 🟢 **`1` fewer: `nextSIS` is GPL-3.0, corrected this pass** |
| 🟢 **CC0-1.0** — new family this pass (`awesome-ia-sala-de-aula`), the most permissive grant in this base | **1** |
| 🟢 Permissive repos with a **first-layer** dependency audit | **4 of 53** — `nbgrader` 🟢, `OATutor` 🟢, `Kolibri` 🟡, `Oppia` 🔴 |
| 🟢 Permissive repos with a **second-layer** dependency audit | **1 of 53** — `nbgrader` 🟡 (`65` transitive packages, `2` weak-copyleft) |
| Dead addresses previously corrected to a live canonical owner | **4** — `tsugi/tsugi`→`csev/tsugi`, `openedx/openassessment`→`openedx/edx-ora2`, `mahara/mahara`→`MaharaProject/mahara`, `openedx/tutor`→`overhangio/tutor` |
| 🟢 Controls reproduced exactly before any verdict shipped | **10 of 10** (`p790`) · `3` planted negatives DEAD · 🔴 `7` defects found by those controls, `0` by inspection |

🔴 **Declared gaps added by `p790`:** the `jinlize-tech` set is **sampled, not swept** — `100` of its
`132` repositories were read for an SPDX id on the *claim* channel and only **`2` on the byte
channel**, so licence-byte agreement across the set is inferred from two identical shas
(`cfc7749b96f6`), not proven (`ACTION p790-D`). And `oppia/oppia`'s transitive closure is **still
unmeasured** while it remains the repository this base tells clients to embed and carries a known
layer-1 **AGPL-3.0** package (`ACTION p790-A`).

🔴 **Declared gaps on this file:** transitive depth `3+` is **unmeasured by design**; the npm-side
layer-2 graphs (`OATutor` `43` direct, `Oppia` `171` direct) were **not** re-audited this pass, and
Oppia's layer-1 AGPL-3.0 finding already governs that decision; and these are **declared ranges
from registry metadata, not resolved versions from a lockfile**, so a client's actual tree may differ.

🔴 **Still grant-less after a re-probe with this pass's variant-tolerant, locale-safe,
any-depth-title gate:** [`formalms/formalms`](https://github.com/formalms/formalms) `446a77a9b9cb`,
[`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) `8348cd069aa2`,
[`nestauk/skills-taxonomy-v2`](https://github.com/nestauk/skills-taxonomy-v2) `9e30d89157f7`,
[`Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) `59da726edd9b`.
🟢 **The improved gate rescued 8 other rows and did not rescue these four, which strengthens rather
than weakens the verdict:** they are not misread translations or short grants, they serve no licence
at all. 🔵 The deliverable is an upstream licence request, not a permanent exclusion — and
`SakaiXAPI-Provider` is worth asking for, because it is the Apereo bridge between the one
permissively-granted university LMS and the one permissively-granted learning-record store.
