---
industry: education
region: Global
updated: 2026-11-18
---

# Foundational repos — education

The substrate an education engagement is built on. All URLs and licences verified
2026-11-18 via `raw.githubusercontent.com` (see `agents/top.md` for method and limits).

**Read the licence column before you promise anything.** Education's most important
platforms are copyleft: Open edX, Canvas and Moodle are AGPL-3.0/GPL-3.0. That is fine
for hosting and for plugins that stay separate, and it is a problem for a proprietary
derivative work. The permissive anchors — Artemis (MIT), Kolibri (MIT), Oppia
(Apache-2.0), OpenOLAT (Apache-2.0) — are the ones to reach for when a client needs to
keep the result closed. This distinction is the single most consequential fact in this
file.

🔴 **p899 corrected the single most dangerous row in this file, and the error was in the
direction that costs a client money.** `PrairieLearn/PrairieLearn` was published here as
**`MIT` · "Permissive and genuinely strong"**. It is **not MIT**: the Community Edition is
**AGPL-3.0**, and two directories — including **`apps/course-agent/`, which is the AI tier — are
proprietary Enterprise Edition requiring a paid subscription for production use**, with a clause
assigning your modifications to PrairieLearn, Inc. Both licence files were byte-read this pass.
**The correction is in the grading table below.** This is the third consecutive pass to find a
published grant wrong (`p897`: five of seven re-read rows; `p896`: `i-diario`), and the first to
find one wrong in a way that would survive review *because it looked permissive*.

🟢 **p899 also added five grading repos and opened an adaptive-learning section.** `Submitty`
(BSD-3-Clause, 807 ★, RPI) is the largest permissive grading **platform** in open source and was
absent from this file entirely; `otter-grader`, `webtech-network/autograder`,
`autograder-server` and `pawtograder/platform` complete the category; and **`CAHLR/pyBKT`
(MIT, UC Berkeley) gives this KB a learner-modelling primitive for the first time.** All six came
out of this KB's **own `logged-not-shelved` ledger and a description-filtered discovery leg** —
not from new search. See `repos/trending.md` p899.

**p894 restored four rows the 2026-11-18 rewrite had dropped** — `UniTime/unitime`,
`UniTime/cpsolver`, `GEOSOFT-GLOBAL/timetablely` and `agentscope-ai/OpenJudge` — each verified
in an earlier pass, re-measured today, and absent from this file until now. The method point is
in `repos/trending.md`: **diff a canonical table against the append-only history before
rewriting it**, because a verified finding that does not reach this file is not available to an
engagement.

## LMS and platform cores

| Repo | Licence | Role |
|---|---|---|
| https://github.com/openedx/openedx-platform | AGPL-3.0 | Open edX LMS & Studio. The reference large-scale MOOC/LMS core — **8,242 ★, pushed 2026-11-17**. 🔴 **Slug corrected in p896**: this is the canonical name and `openedx/edx-platform` is a rename alias. The earlier note in this row said the opposite; it was produced by probing the `main` branch of a repo whose default branch is `master`. Both names serve byte-identical files on `raw.githubusercontent.com`, so raw cannot tell them apart — only the search channel can. |
| https://github.com/moodle/moodle | GPL-3.0 (no root `LICENSE`; verified in `COPYING.txt`) | The world's most-deployed LMS. Huge plugin surface, which is where AI work actually lands. |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | Canvas. Dominant in North American higher ed; strong LTI and REST API. |
| https://github.com/ls1intum/Artemis | MIT | TU Munich's interactive learning platform with automated programming assessment. **The best permissive LMS core in education** — pair with `edutelligence`/`Pyris`. |
| https://github.com/learningequality/kolibri | MIT | Offline-first learning platform for low-connectivity deployments. Permissive, and the right core for rural LATAM, Africa and South Asia. |
| https://github.com/elimu-ai/webapp | MIT (`main/LICENSE`, byte-read 1,065 B) | **Restored p895, and the region corrected to EMEA.** Android content-and-app hosting platform for **early-grade literacy aimed at out-of-school children**; Sub-Saharan deployment (Tanzania/Kenya). **41 ★ but 67 forks** — a fork-heavy ratio that reads like deployment rather than stargazing — created 2016-01-02 and **pushed 2026-11-17**. **The only Africa-origin, permissively licensed education platform this KB has verified**, and the direct answer to the "nothing from Africa" gap in `agents/top.md`. It had been placed on this shelf by an earlier pass and was **deleted in the 2026-11-04 rewrite**; see `repos/trending.md` (p895). Pair with `appstore` (MIT, 29 ★) for **APK delivery with no app store and no network**. 🔴 **Do not carry over `elimu-ai/ml-authentication` (MIT, 16 ★): it is student login by on-device face recognition — biometric identification of children.** |
| https://github.com/oppia/oppia | Apache-2.0 | Interactive lesson platform with built-in pedagogy (explorations, misconception handling). |
| https://github.com/sakaiproject/sakai | ECL-2.0 | Sakai. Higher-ed LMS; ECL-2.0 is Apache-2.0 with an education-oriented patent clause. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | Strong in LATAM and francophone deployments. |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | Long-standing German/EMEA LMS, heavy in regulated and public-sector training. |
| https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 | Swiss-origin LMS. Permissive, enterprise-grade, under-used outside EMEA. |

## Interoperability and standards

The layer that decides whether your AI work can be sold twice. Build against these and the
same agent ships into Canvas, Moodle and Open edX.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | LTI 1.3 / Advantage tool provider in Node. The standard way to expose an AI tool to any compliant LMS. |
| https://github.com/tsugiproject/tsugi | Apache-2.0 | PHP LTI framework from the author of the IMS LTI spec. |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 | Ed-Fi operational data store — the K-12 data standard across most US states. Essential for any North American K-12 engagement. |
| https://github.com/1EdTech/openbadges-validator-core | Apache-2.0 | Open Badges validation; the credentialing/micro-credential layer, 61 ★. **Last push 2025-11-04 (379 days idle)** — the spec is stable, but expect to maintain this yourself. |
| https://github.com/Citolab/qti-components | GPL-3.0 | QTI 3 web components for assessment item rendering. Copyleft — keep it at arm's length in a proprietary build. |
| https://github.com/apereo/cas | Apache-2.0 | Central Authentication Service. The SSO incumbent in higher education. |
| https://github.com/Faixiang/Moodle-MCP | MIT | **Added p893.** Zero-dependency MCP server over the Moodle Web Service API — **read-only**. The MCP counterpart to LTI: where `ltijs` ships your tool *into* the LMS, this exposes the LMS *to* an agent. |
| https://github.com/G36maid/moodle-mcp | MIT | **Added p893.** Read-**write** Moodle MCP — courses, assignments, forums, grades, files-as-markdown. The graduation step from the read-only server above. |
| https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | **Added p893.** Open edX staff/superuser admin as an MCP facade (Ulmo), native platform APIs only. Vendor-maintained, not a foundation project — see `agents/top.md`. |
| https://github.com/openedx/XBlock | Apache-2.0 | **Restored p896.** The Open edX component framework — 471 ★, pushed 2026-11-16. **This is the permissively licensed extension point of an AGPL platform**, and therefore the seam where a studio ships a learning component into Open edX without inheriting AGPL on its own code. Licence byte-read from `master/LICENSE.TXT` (uppercase `.TXT`, which this KB's 8-path probe missed). |
| https://github.com/openedx/xblock-sdk | Apache-2.0 | **Restored p896.** Workbench and worked example XBlocks — 69 ★, pushed 2026-11-16. The development harness for the row above: build and test a component without standing up a full Open edX. |
| https://github.com/instructure/common-cartridge-viewer | MIT | **Restored p896.** Instructure's own browser viewer for **IMS Common Cartridge** packages — 95 ★, pushed 2026-11-04. Content migration between LMSs runs through Common Cartridge; this is first-party, permissive and the fastest way to inspect what a client's export actually contains. |
| https://github.com/longsightgroup/qti3 | **MIT** — byte-read p900 (`LICENSE.md@HEAD`, 1,071 B) | **Added p900, out of this base's own ledger (logged 10×).** Renders **and scores** QTI 3 assessment items: TypeScript core, native Web Component player, React/Preact adapters, plus conversion tooling for older QTI. **Zero third-party runtime dependencies** in the core engine and CLI. 🔵 The permissive counterpart to `Citolab/qti-components` (GPL-3.0) one row above — **if a client needs a proprietary assessment player, this is the row.** 🔴 Not in the search index, so stars are unmeasurable (`900-G2`) |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard | Apache-2.0 | **Added p900 (logged 12×).** The **data standard** itself — 47 ★, pushed 2026-11-18 — where the row above is its operational data store. Low stars, high institutional weight: this is the interoperability substrate US K-12 districts contract against |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | **Added p900 (logged 12×).** LTI 1.3 Advantage tool in **Python** — the gap between `ltijs` (Node) and `tsugi` (PHP). 🟡 **138 ★ and last pushed 2024-08-18, 27 months idle.** Read it as a reference implementation to vendor, not an upstream to track |
| https://github.com/jcputney/scorm-again | MIT | **Added p900 (logged 5×).** Modern **SCORM** JavaScript runtime — 367 ★, pushed 2026-11-17. 🔵 SCORM is the format a client's *existing* content is already in; this is how agent-generated courseware ships into a legacy LMS without re-authoring it |
| https://github.com/ucfopen/canvasapi | MIT | **Added p900 (logged 8×).** Python wrapper for the Canvas LMS API from the University of Central Florida — 682 ★, pushed 2026-04-16. 🔵 **A permissive seam onto an AGPL-3.0 platform**, which is precisely the posture `compose/patterns.md` prescribes for Canvas work |
| https://github.com/digitalcredentials/learner-credential-wallet | **MIT** — byte-read p900 (`LICENSE@HEAD`, 1,091 B) | **Added p900 (logged 6×).** Cross-platform iOS/Android wallet for **verifiable learner credentials**, built to the MIT Digital Credentials Consortium specification. 🔵 Also published at `openwallet-foundation-labs/learner-credential-wallet` with a **byte-identical licence** — the project has moved under the **OpenWallet Foundation (Linux Foundation)**, so track that address for governance and this one for history |

## Registrarial and scheduling

**Added p894, and it corrects an absence rather than adding a nicety.** `agents/top.md` has
named the registrarial layer — enrolment, timetabling, transcripts, financial aid — as this
KB's clearest build-vs-adopt gap for four passes. The *agent* tier is genuinely missing. The
*platform* is not, and it is permissive: it was verified and licence-hash-checked by an earlier
pass, then lost from the canonical files in the 2026-11-18 rewrite. Re-measured and restored
here.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/UniTime/unitime | Apache-2.0 (`LICENSE@master`, payload `11,357 B`) | **Apereo UniTime** — university course and exam timetabling plus student scheduling, 360 ★, pushed 2026-11-17. Runs standalone or interfaces with an existing SIS. **The most permissively licensed, actively maintained registrarial system this KB has found**, and the substrate `compose/patterns.md` **P12** builds an agent tier over. |
| https://github.com/UniTime/cpsolver | **LGPL-3.0** | The constraint solver underneath UniTime, 84 ★, pushed 2026-10-14. **Licence trap:** the platform is Apache-2.0 and the component is LGPL-3.0, so a static link pulls the weaker grant into scope. Keep it behind a process or service boundary in a closed derivative. |
| https://github.com/GEOSOFT-GLOBAL/timetablely | MIT | Small-scale permissive timetable generator, 27 ★. **Pushed 2026-08-17 — three months idle.** The MIT option when UniTime is too heavy; read it as a starting point, not a dependency. |

## Adaptive learning and learner modelling — added p899

The capability every tutor in `agents/top.md` is described as lacking, available as libraries.
**This section did not exist before p899**, which is why `pyBKT` sat in this KB's own
`logged-not-shelved` ledger with 15 recorded mentions and no row.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/CAHLR/pyBKT | **MIT** (`LICENSE@master`, 1,132 B, `sha256₁₂ ad0c7a38bf01`, *"Copyright (c) 2021 Computational Approaches to Human Learning"*) | **Bayesian Knowledge Tracing** and its standard extensions, 292 ★, pushed 2026-11-02. The canonical open implementation of the model that estimates *"has this learner mastered this skill yet"* from a response history — the learner-state primitive that `LearnHarness` is praised in `agents/top.md` for having and that nothing else in that table implements. From **UC Berkeley CAHLR** (Zachary Pardos et al., author emails `@berkeley.edu`), the same lab as `OATutor`, with the original xBKT work shared with MIT CSAIL. MIT-licensed, C++-accelerated, callable from a Python agent in one import. **Pair it with any tutor in `agents/top.md` to replace a vibes-based "do they know it" judgement with a fitted model.** |
| https://github.com/pykt-team/pykt-toolkit | MIT | **Added p900 (logged 5×).** **Deep-learning knowledge tracing, with a benchmark harness** — 462 ★, pushed 2026-10-18. 🔵 The row above is classical Bayesian Knowledge Tracing; this is the neural half **and the standard way to show a client that your learner model beats the classical baseline rather than asserting it.** Together they close the capability every tutor in `agents/top.md` is described as lacking |

## Learning analytics (xAPI / LRS)

Where the evidence for "did the AI actually help" has to live.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/yetanalytics/lrsql | Apache-2.0 | SQL-backed Learning Record Store, 144 ★, pushed 2026-11-14. Permissive, actively maintained — **the default LRS pick**, and the only one of the four here that is both. |
| https://github.com/davidpesce/moodle-logstore_xapi | **GPL-3.0** | **Restored p896.** The Moodle plugin that emits **xAPI statements from Moodle's own logstore** into an LRS — 83 ★, pushed 2026-10-29. This is the missing first leg of every Moodle analytics build: without it the LRS above has nothing to ingest. GPL-3.0, like Moodle itself — it is a plugin *inside* the platform, so the copyleft is expected and contained. |
| https://github.com/openedx/openedx-aspects | Apache-2.0 | **Restored p896.** **Aspects** — the first-party analytics stack for Open edX (10 ★, pushed 2026-11-16). Permissive, unlike the AGPL platform it reports on. |
| https://github.com/openfun/ralph | MIT | xAPI/LRS toolbox from France Université Numérique. |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 | Reference LRS from ADL, who authored xAPI, 335 ★. **Last push 2025-11-14 (369 days idle)** — useful as a spec reference, not as a production dependency. |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | Widely deployed LRS, 587 ★. **Do not start new work here: last push 2024-05-30, 902 days idle.** Copyleft as well. Use `lrsql` instead. |
| https://github.com/agentscope-ai/OpenJudge | Apache-2.0 | **Added p894.** Unified LLM/agent evaluation and quality-reward framework, **1,113 ★, pushed 2026-11-18** — permissive and the most actively maintained evaluation substrate in this file. It **judges agents, not learners**, which is exactly why it belongs here and not in `agents/top.md`: it is the harness under `compose/patterns.md` **P7**'s efficacy tier, and https://github.com/AI-for-Education/pedagogy-benchmark (MIT, 13 ★) is the education-specific rubric you run *on* it. Generates rubrics from data or zero-shot. |
| https://github.com/adlnet/xapi-spec | Apache-2.0 | **Added p900 (logged 9×).** **The xAPI specification itself**, from ADL — 954 ★, last pushed 2025-07-03. Normative text rather than an implementation: the document an LRS integration is *checked against*. 🟡 A frozen spec is not an abandoned repo — but confirm the version before citing it |

## Assessment, grading and academic integrity

| Repo | Licence | Role |
|---|---|---|
| https://github.com/PrairieLearn/PrairieLearn | 🔴 **NOT MIT — multi-grant, open-core. Corrected p899.** CE is **AGPL-3.0**; `apps/prairielearn/src/ee/` **and `apps/course-agent/`** are **proprietary Enterprise Edition**; all client-side JavaScript is AGPL; only the portions copyright University of Illinois are MIT | Randomised, auto-graded problem generation, 533 ★, pushed 2026-11-18. Still the strongest open assessment engine for STEM — but this file published it as *"MIT · Permissive"* for an unknown number of passes and that is a **procurement-grade error in the dangerous direction**. Byte-read `LICENSE@master` (37,237 B, `sha256₁₂ 548cbfae567a`) states: *"The PrairieLearn Community Edition (CE) consists of all content outside of the above mentioned `apps/prairielearn/src/ee/` and `apps/course-agent/` directories and is licensed under the GNU Affero General Public License."* 🔴 **The AI agent is the proprietary part.** `apps/course-agent/LICENSE` (2,538 B, `sha256₁₂ cfd0235081fa`) is the EE licence: production use requires *"a valid PrairieLearn Enterprise Edition subscription"*, and it assigns ownership of your modifications — *"PrairieLearn, Inc. and/or its licensors retain all right, title and interest in and to all such modifications and/or patches"*. A studio that built a client's AI assessment tier on `apps/course-agent/` on the strength of the old row would have shipped unlicensed production code **and** signed the client's modifications over to a third party. Use the CE under AGPL, keep the EE directories out of the build, and treat `grader-python-v2` (MIT, below) as the permissive seam. |
| https://github.com/Submitty/Submitty | **BSD-3-Clause** (`LICENSE.md@main`, 1,542 B, `sha256₁₂ c123708cb4ef`, *"Copyright (c) 2014-2026 Submitty team"*) | **Added p899 — the largest permissive full grading PLATFORM in open source, and it was absent from this file.** 807 ★, pushed 2026-11-18, twelve years of continuous development out of the **Rensselaer Center for Open Source Software, Dept of Computer Science, RPI** (origin read from the README, not inferred). Homework submission + automated grading + TA/manual grading + rubrics in one deployable system. **BSD-3-Clause is the most permissive licence in this section** — unlike Autolab (Apache-2.0, comparable scope) it carries no patent clause, and unlike PrairieLearn above it has no enterprise carve-out at all. This is the default answer when a client needs an open grading platform they can close a derivative of. |
| https://github.com/ucbds-infra/otter-grader | **BSD-3-Clause** (`LICENSE@master`, 1,560 B, `sha256₁₂ 6af203d41a01`, *"Copyright (c) 2019, UC Berkeley Division of Data Sciences"*) | **Added p899.** Python **and R** autograding, 162 ★, pushed 2026-11-14. Grades locally, in a container, or by submitting through Canvas/Gradescope, so it is the autograder that does **not** require you to adopt a platform — the complement to `nbgrader` above rather than a competitor. From the same university as `pyBKT` and `OATutor`. |
| https://github.com/webtech-network/autograder | **Apache-2.0** (`LICENSE@main`, 11,357 B, `sha256₁₂ c71d239df917`) | **Added p899.** Configurable autograding that also generates feedback, 66 ★, pushed 2026-11-08. Small, current and patent-granting; the lightest permissive option when Submitty is too much system. |
| https://github.com/eecs-autograder/autograder-server | **LGPL-3.0** (`LICENSE.txt@master`, 7,652 B, `sha256₁₂ b96e8c21c928`) | **Added p899, and carried as a worked example of a star-ranked trap.** The University of Michigan EECS autograder. 🔴 **The repo a search ranks first is the wrong one:** `eecs-autograder/autograder.io` has **81 ★ and no licence file at all** — it is the documentation and issue tracker. The actual server is this repo at **9 ★**, and the frontend `eecs-autograder/ag-website-vue` (LGPL-3.0, 4 ★). LGPL-3.0: linkable from a closed derivative, not forkable into one. |
| https://github.com/pawtograder/platform | 🔴 **GPL-3.0-or-later — SPDX says `NOASSERTION`. Corrected p899.** Byte-read `LICENSE@main` (658 B, `sha256₁₂ 61d7698783f4`): *"This program is free software… under the terms of the GNU General Public License… either version 3 of the License, or (at your option) any later version."* | **Added p899.** CI-based autograder + Q&A + courseops, 22 ★, pushed 2026-11-18 — positioned as an open GitHub-Classroom replacement for CS courses. New and small; **strong copyleft**, so read it for the GitHub-Actions-as-grader pattern rather than as substrate. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause (1,370 ★) | Assignment release/collect/autograde for notebooks. The data-science course standard. |
| https://github.com/autolab/Autolab | Apache-2.0 | CMU's autograding platform with secure job execution. |
| https://github.com/autolab/Tango | Apache-2.0 | **Restored p896.** Autolab's **standalone RESTful autograding service** — 49 ★, pushed 2026-10-21. The row above is the platform; this is the execution tier on its own, which is the piece you actually want when grading has to be called from something that is not Autolab (an LTI tool, an agent, a CI job). |
| https://github.com/PrairieLearn/grader-python-v2 | MIT | **Restored p896.** First-party Python grader image for PrairieLearn, pushed 2026-11-18. **1 ★ — carried for provenance, not popularity**: it is maintained by the same organisation as the engine above, which is the distinction this file draws between a small first-party repo and a small personal one. |
| https://github.com/ls1intum/Ares | MIT | Automated programming-exercise assessment library behind Artemis. |
| https://github.com/openedx/edx-ora2 | AGPL-3.0 | Open-response assessment: peer, self and staff grading workflows. The natural seam for an AI grading assist. |
| https://github.com/openedx/codejail | Apache-2.0 | Sandboxed untrusted-code execution. **Use this (or Ares) before you let an agent run student code.** |
| https://github.com/Udayraj123/OMRChecker | MIT | OMR/bubble-sheet scanning. Unglamorous and high-value in LATAM, India and Africa where paper exams dominate. |
| https://github.com/dodona-edu/dolos | MIT | **Added p900 (logged 11×).** **Source-code plagiarism detection**, language-agnostic, from **Ghent University** — 358 ★, pushed 2026-11-16. 🔵 **Academic-integrity work that does not surveil the student**: it compares submissions to each other after the fact, so it carries none of the EU AI Act Annex III exposure that proctoring does (see the `edx-proctoring` row above) |
| https://github.com/openedx/edx-proctoring | AGPL-3.0 | Proctoring integration. **Regulatory flag:** exam monitoring is an EU AI Act Annex III high-risk use case (obligations from 2 Dec 2027). |

## Notebook-native teaching and assessment — added `p902`

🔵 **Why this section exists.** This file held `nbgrader` and `jupyterhub` and nothing else from the
Jupyter estate. The five repos below returned **zero hits across every live file** before `p902`. For
CS, data-science, engineering and quantitative social-science courses — the ones that actually buy
automated assessment — this is the delivery substrate. **None of them self-describe as education
software**, which is why `{education}`-qualified discovery legs never surfaced them (same blind spot
as `jitsi/jitsi-meet` in `verticals/solutions.md`; see `repos/trending.md` `902-R1`).

| Repo | Licence | Role |
|---|---|---|
| https://github.com/jupyterhub/binderhub | **BSD-3-Clause** (`LICENSE@main`, 1,522 B, `sha256₁₂ 611f531642d5`; SPDX agrees) | **Added p902.** 2,673 ★, pushed 2026-11-14. Turns a git repo into a running, reproducible notebook environment on demand. **The zero-install route to a student environment** — no lab image, no install day, and the course content stays a repo. Pairs with `jupyterhub` (which this file already holds) for the authenticated, persistent case. |
| https://github.com/nbgallery/nbgallery | **MIT** (`LICENSE@master`, 1,071 B, `sha256₁₂ 7900749dcb3b`, `MIT License` title line; SPDX agrees) | **Added p902.** 150 ★, pushed 2026-10-22. Notebook sharing, search, usage analytics and automated health checks — **a notebook LMS in all but name**, and permissive, which none of the LMS tier in `verticals/solutions.md` is except Artemis, Kolibri, Mentingo and Pupilfirst. Small star count; read it as a working reference implementation. |
| https://github.com/computationalmodelling/nbval | 🟡 **BSD-3-Clause — SPDX says `NOASSERTION`.** Byte-read `LICENSE@master` (1,910 B, `sha256₁₂ 1dbc744b78bb`): the file has **no title line at all**, and the grant is resolved from clause structure — redistribution + binary-reproduction + no-endorsement. Copyright **University of Southampton, UK** | **Added p902.** 453 ★, pushed 2025-09-17. A `pytest` plugin that validates a notebook against its stored outputs. 🟢 **This is deterministic marking of a notebook with no model in the loop** — the tier to put *under* an AI grading assist, so the mark is reproducible and the AI only writes feedback (the `P17` split). 🔴 **A bare-substring licence grader calls this MIT** (`MIT` is inside `LIMITED`); see `repos/trending.md` `902-N2`. |
| https://github.com/parmentelat/nbautoeval | 🔴 **CC-BY-SA-4.0 — a content licence on executable code.** Byte-read `LICENSE@master` (289 B, `sha256₁₂ 1bb69236081f`): *"made available through a Creative Common Licence CC BY-SA 4.0"*. SPDX says `NOASSERTION`. **`(c) 2017 — Inria — Thierry Parmentelat`** | **Added p902 as a flagged row.** 20 ★, pushed 2024-12-11. In-notebook auto-graded exercises. 🔴 **Do not take this as a dependency:** CC-BY-SA-4.0 carries **no patent grant** and its **ShareAlike reaches derivative works**, so an exercise bank built on it cannot stay closed. Use it as a pattern reference. Second instance in this KB of a non-software licence on software, after `withmarbleapp/os-taxonomy` (ODbL) in `agents/top.md`. |
| https://github.com/mwouts/jupytext | **MIT** (`LICENSE@main`, `MIT License` title line, *"Copyright (c) 2018-2026 Marc Wouts"*) | **Added p902.** 🔴 **Stars: unmeasurable** — `gh api search/repositories` returns `422` for this repo while `raw` returns `200` (the false-absence class, `902-F3`). Recorded as unmeasurable rather than guessed. Notebooks as plain text: **the reason course content can live in git, be diffed, and be reviewed in a pull request** instead of being a blob. The precondition for treating a curriculum as code. |
| https://github.com/pyta-uoft/pyta | 🔴 **GPL-3.0** (`LICENSE@master`, 35,141 B, `sha256₁₂ 589ed823e9a8`, GNU GPL title line; SPDX agrees) | **Added p902.** 109 ★, pushed 2026-11-17, **University of Toronto**. Static analysis written to *teach*: the same errors a linter reports, phrased for a beginner. 🟡 **Strong copyleft** — invoke it as a separate process over student code, do not link it into a closed product. |

🟢 **The permissive spine of this section is `binderhub` (BSD-3) + `nbgrader` (BSD-3) + `nbval`
(BSD-3) + `jupytext` (MIT) + `nbgallery` (MIT)** — a complete environment / assignment / marking /
version-control / sharing stack with no copyleft and no carve-outs. The two flagged rows
(`nbautoeval`, `pyta`) are the ones to read rather than ship. Wired up end to end in
`compose/patterns.md` **P21**.

## Content authoring and pipelines

| Repo | Licence | Role |
|---|---|---|
| https://github.com/h5p/h5p-php-library | GPL-3.0 | H5P interactive content. Ubiquitous across Moodle and Open edX. |
| https://github.com/Khan/perseus | MIT | Khan Academy's exercise/question rendering framework. Permissive. |
| https://github.com/learningequality/studio | MIT | Kolibri Studio — curriculum authoring and channel curation. |
| https://github.com/learningequality/ricecooker | MIT | Content-import pipeline into Kolibri channels. |
| https://github.com/learningequality/le-utils | MIT | Shared constants and format definitions for the Kolibri ecosystem. |
| https://github.com/openfun/richie | MIT | Course-catalogue/marketing CMS for Open edX. |
| https://github.com/openfun/marsha | MIT | Video management for LMS-embedded teaching. |
| https://github.com/h5p/h5p-interactive-video | MIT | **Restored p896.** H5P's interactive-video content type — 267 ★, pushed 2026-11-17. 🟢 **The licence inversion worth knowing**: `h5p-php-library` above is **GPL-3.0**, but the individual H5P *content types* are **MIT**. A studio that needs a permissive interactive-content pipeline can compose the MIT component repos instead of embedding the GPL host library. (No licence file at any of 12 candidate paths; SPDX from the search channel only — treat this row's licence as the weakest-evidence one in this file.) |
| https://github.com/h5p/h5p-course-presentation | MIT | **Restored p896.** Slide-based presentation content type, 57 ★, pushed 2026-11-11. |
| https://github.com/h5p/h5p-audio-recorder | MIT | **Restored p896.** Learner audio capture, 36 ★, pushed 2026-11-17 — the input half of any pronunciation or oral-assessment build (pair with `OpenPronounce` in `agents/top.md`). |
| https://github.com/h5p/h5p-speak-the-words | MIT | **Restored p896.** Speech-answered questions, 12 ★, pushed 2026-11-17. |
| https://github.com/h5p/h5p-cli | MIT | **Restored p896.** H5P command-line tooling — 79 ★, pushed 2026-10-31. The piece that makes content generation **scriptable**, which is what turns an authoring agent into a pipeline rather than a demo. |

## Document and media ingestion

Course material arrives as PDFs, slide decks and lecture recordings. This is where most
education RAG projects actually fail.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/docling-project/docling | MIT | Document parsing to structured form. Strong on PDF layout, tables and reading order. |
| https://github.com/datalab-to/marker | Apache-2.0 | PDF to Markdown at high fidelity, including equations. |
| https://github.com/opendatalab/MinerU | Apache-2.0 | PDF extraction with strong CJK and formula handling — notably better than Western-trained alternatives on APAC textbooks. |
| https://github.com/Unstructured-IO/unstructured | Apache-2.0 | Broad-format ingestion into chunked, embeddable records. |
| https://github.com/SYSTRAN/faster-whisper | MIT | Fast CTranslate2 Whisper inference. The practical choice for lecture transcription at volume. |
| https://github.com/openai/whisper | MIT | Reference speech-to-text weights and code. |

## Model serving, retrieval and memory

| Repo | Licence | Role |
|---|---|---|
| https://github.com/ollama/ollama | MIT | Local model serving. The enabler for data-residency and on-premise school deployments. |
| https://github.com/vllm-project/vllm | Apache-2.0 | High-throughput serving for campus-scale concurrency. |
| https://github.com/BerriAI/litellm | **MIT, except `litellm/enterprise/`** (byte-verified p891: the root `LICENSE` grants MIT to everything *outside* `litellm/enterprise/`, which carries its own separate licence — this is why the API reports `NOASSERTION`). Use the OSS paths and do not vendor the enterprise directory. | Unified gateway across providers, with per-key budgets. **Per-course and per-student cost caps are a procurement requirement in education, not a nicety.** |
| https://github.com/qdrant/qdrant | Apache-2.0 | Vector database with payload filtering — needed to scope retrieval to one course or cohort. |
| https://github.com/chroma-core/chroma | Apache-2.0 | Lightweight vector store; fine for per-course corpora. |
| https://github.com/HKUDS/LightRAG | MIT | Graph-augmented RAG. Fits curricula, where prerequisite structure is a graph. |
| https://github.com/infiniflow/ragflow | Apache-2.0 | Document-understanding-first RAG engine with a usable ingestion UI. |
| https://github.com/deepset-ai/haystack | Apache-2.0 | Mature RAG/search orchestration framework. |
| https://github.com/mem0ai/mem0 | Apache-2.0 | Persistent memory layer — the mechanism behind "the tutor remembers what this learner struggled with". |
| https://github.com/temporalio/temporal | MIT | Durable workflow execution. Grading runs and term-long tutoring loops need to survive restarts. |

## Usage metering, cost attribution and portability

**Added in pass p890**, prompted by the Jisc / Universities UK / GuildHE / Association of
Colleges joint statement asking AI suppliers for granular per-institution usage and cost data,
data portability and no vendor lock-in (see `intel/trends.md` T9 and `compose/patterns.md` P8).
`litellm` above supplies per-key budget caps; this tier supplies attribution and export.

| Repo | Licence | Note |
|---|---|---|
| https://github.com/traceloop/openllmetry | Apache-2.0 | OpenTelemetry-native LLM tracing, 7,541 ★, pushed 2026-11-18. **The default pick:** OTel means usage data lands in whatever observability stack the institution already runs, which is itself the portability answer — nothing is captive, so nothing has to be migrated on exit. |
| https://github.com/Helicone/helicone | Apache-2.0 | Gateway-level logging and cost attribution, 6,287 ★, pushed 2026-11-17. |
| https://github.com/openlit/openlit | Apache-2.0 | OTel-native LLM observability with cost tracking, 3,088 ★, pushed 2026-11-17. |
| https://github.com/langfuse/langfuse | **Split — see note** | Much the largest at 37,577 ★ (pushed 2026-11-18), and SPDX reports `NOASSERTION`, so the grant was read as text: **"MIT Expat" for the core, with a separate enterprise licence covering `ee/`, `web/src/ee/`, `worker/src/ee/` and `packages/shared/src/server/ee/`**. The copyright line now reads **"Copyright (c) 2023-2026 ClickHouse, Inc."** — ownership has changed hands. Usable, but it needs licence diligence before it enters a client deliverable, and the permissive grant covers less than the repository. |

**None of these is education-aware.** They model users and projects, not institutions,
faculties, courses and cohorts. Mapping them onto an academic hierarchy with LTI 1.3-derived
context is build work — and, per P8, the most defensible small piece of studio IP this pass
identified.

## Evaluation, labelling and quality

| Repo | Licence | Role |
|---|---|---|
| https://github.com/EleutherAI/lm-evaluation-harness | MIT | Standard LLM benchmark harness; extend it with subject-specific tasks. |
| https://github.com/promptfoo/promptfoo | MIT | Prompt/LLM regression testing in CI. The gate that keeps a tutor from regressing between releases. |
| https://github.com/HumanSignal/label-studio | Apache-2.0 | Human annotation across modalities — rubric calibration, grading gold sets. |
| https://github.com/argilla-io/argilla | Apache-2.0 | Feedback collection and dataset curation with domain experts (here: teachers). |
| https://github.com/AI-for-Education/pedagogy-benchmark | MIT | Pedagogical-ability benchmark. Pairs with the harness above as an education-specific eval gate. |
| https://github.com/acheamponge/wassce-benchmark | MIT | **Added p893.** Open LLMs scored against the **WASSCE**, the West African school-leaving exam ~2 million candidates sit annually. The only African-curriculum open eval asset found in four regional legs. Small (4 ★) and last pushed 2026-04-07 — a starting corpus, not a maintained harness. |

## Other infrastructure

| Repo | Licence | Role |
|---|---|---|
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | Multi-user notebook serving. The computational-teaching backbone. |
| https://github.com/jupyterhub/zero-to-jupyterhub-k8s | Apache-2.0 | Kubernetes deployment path for JupyterHub at class scale. |
| https://github.com/jupyterhub/nbgitpuller | BSD-3-Clause | Distributes course materials into student notebook environments. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | FSRS spaced-repetition scheduler. A real, evidence-backed learning algorithm to pair with an agent instead of inventing a review schedule. |
| https://github.com/appsmithorg/appsmith | Apache-2.0 | Low-code internal tooling — teacher review queues and human-in-the-loop consoles without a bespoke front end. |
| https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | Offline-first knowledge/education server. Relevant to the same low-connectivity brief as Kolibri. |
| https://github.com/learningequality/morango | MIT | **Restored p896.** The **peer-to-peer database replication engine** under Kolibri (Django, SQLite + PostgreSQL) — 15 ★, pushed 2026-11-17. Low stars, high leverage: it is how learner records sync between devices and a server **without continuous connectivity**, which is the actual hard part of a rural deployment. Reusable on its own. |
| https://github.com/instructure/instructure-ui | MIT (`master/LICENSE.md`, byte-read 1,175 B) | **Restored p896.** Instructure's own accessible component library — 487 ★, pushed 2026-11-18. 🟡 **GitHub reports `NOASSERTION`; the licence text is MIT.** Build Canvas-adjacent interfaces that look native without touching the AGPL platform. |
| https://github.com/openedx/paragon | Apache-2.0 | **Restored p896.** The Open edX design system — 141 ★, pushed 2026-11-17. Same role as the row above, on the other platform, and also permissive while its platform is not. |
| https://github.com/mitodl/ol-infrastructure | BSD-3-Clause | **Restored p896.** MIT Open Learning's **production infrastructure-as-code** — 59 ★, pushed 2026-11-18. The only open artefact this KB has found that shows how a large university actually *runs* Open edX in production rather than how to install it. |
| https://github.com/apereo/java-cas-client | Apache-2.0 (`master/LICENSE`, byte-read 2,321 B) | **Restored p896.** CAS client for JVM applications — 949 ★. 🟡 GitHub reports `NOASSERTION`; the text is Apache. Institutional SSO is the first integration question in every higher-ed engagement. |
| https://github.com/apereo/phpCAS | Apache-2.0 | **Restored p896.** CAS client for PHP — 802 ★. The one that matters for **Moodle**, which is PHP. **Pushed 2026-06-30**, so pin it. |
| https://github.com/jitsi/jitsi-meet | Apache-2.0 (`master/LICENSE`, byte-read 12,596 B, `sha256₁₂ eae52e200cd8`) | **Added `p901`.** Self-hostable live-classroom and conferencing platform — **30,255 ★ / 8,134 forks**, pushed 2026-11-18. **The largest permissive synchronous-delivery platform in open source**, and the only row in this file that was found by auditing against a *third-party* curated index rather than by search — it never self-describes as education, so every `{education}`-qualified leg missed it. Pairs with the LMS rows for the synchronous half of a blended deployment. See `repos/trending.md` `901-R1`. |

**110 foundational repos, all verified** (**109 through `p900`; `jitsi/jitsi-meet` added in `p901`**), counted programmatically across the fourteen sections
of this file rather than asserted — the previous standing figure of "47" was stale and nobody
had recounted it. **34 of the 109 were restored in `p896`** from
`archive/2026-11-18-pre-cleanup/repos-foundations.md`, after a shelf-vs-history diff showed they
had been carried on this shelf, deleted by the 2026-11-18 cleanup rewrite, and left unrecorded in
that pass's own list of removals. Every restored row was re-measured today on both channels;
**none of them 404s.** Raw diff: `evidence/shelf-vs-history-diff.2026-11-18-p896.tsv`.

## The TU Munich Artemis estate — permissive teaching infrastructure, restored in `p896`

`agents/top.md` carries `edutelligence` and `Pyris`, and this file carries `Artemis` and `Ares`,
because TU Munich is the one university shipping a **permissively licensed, production** teaching
stack. The rest of that estate was on this shelf and was dropped by the 2026-11-18 cleanup. It is
the only worked example in open source of an LMS, its AI services, its native clients and its
deployment automation all under MIT.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/ls1intum/Apollon | MIT (`main/LICENSE`, byte-read 1,091 B) | **UML modelling editor** — 106 ★, pushed 2026-11-18. The largest of the restored TUM rows. Embeddable diagram editing with a model you can grade programmatically, which is what makes **diagram assessment** tractable at all. |
| https://github.com/ls1intum/artemis-android | MIT | Native Android client for Artemis, 13 ★, pushed 2026-11-18. |
| https://github.com/ls1intum/artemis-ios | MIT | Native iOS client for Artemis, 13 ★, pushed 2026-11-16. |
| https://github.com/ls1intum/artemis-ansible-collection | MIT | Ansible collection that deploys Artemis, 8 ★, pushed 2026-11-18. **Read this before quoting a self-hosting estimate.** |
| https://github.com/ls1intum/standardized-competency-catalog | MIT | Standardised competency catalogue, 1 ★, pushed 2026-03-01. Small, but it is the vocabulary a competency-aware tutor needs and most projects invent badly. |

## Integration code written by the institutions that run the platforms — restored in `p896`

A distinct and under-used class: not products, but the glue universities wrote for their own
estates and published. It is the closest thing to seeing a client's problem already solved, and
every row is permissive or ECL.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/UniversityOfHelsinkiCS/sis-importer | MIT (byte-read 1,111 B) | **Student-information-system importer** — the SIS seam this KB repeatedly calls its largest gap, written by a university that had to solve it. 1 ★, pushed 2026-11-16. |
| https://github.com/UniversityOfHelsinkiCS/suoritustarkistin | MIT | Completion/credit-registration service against the SIS, pushed 2026-11-17. |
| https://github.com/UniversityOfHelsinkiCS/sis-ns-manager | Apache-2.0 | SIS namespace management, pushed 2026-11-10. |
| https://github.com/KTH/canvas-api | MIT | KTH's Node.js client for the **Canvas** API, 10 ★, pushed 2026-11-16. Maintained against a live production estate. |
| https://github.com/AaltoGIS/classroom-grader | BSD-3-Clause | Aalto's grading automation, pushed 2026-11-09. |
| https://github.com/kyoto-u/comfortable-sakai | Apache-2.0 | Kyoto University's browser extension improving **Sakai** usability, 25 ★. 🔴 **Last push 2023-03-15** — carried as evidence of the pattern, not as a dependency. |
| https://github.com/cilt-uct/sakai-skin-vula | ECL-2.0 (byte-read 11,120 B) | University of Cape Town's Sakai theme (*Vula*), pushed 2026-06-03. **The one African university estate this KB has found publishing its LMS integration code**, and it is properly licensed. |
| https://github.com/cilt-uct/tsugi-migrate-to-brightspace | Apache-2.0 | UCT's LTI-based migration tooling toward Brightspace, pushed 2026-10-22. Migration is the commonest real engagement; this is someone's actual migration. |
| https://github.com/cilt-uct/tsugi-request-gradebook-upload | Apache-2.0 | UCT LTI tool for gradebook upload requests, pushed 2026-10-06. |

## Teaching-grade reference implementations — restored in `p896`

Not education *platforms*: systems built to be **read** by students. They matter to a studio for
one reason — when an engagement includes curriculum, these are the permissively licensed
artefacts a course can be built around, and they are maintained by the departments that teach it.

| Repo | Licence | Role |
|---|---|---|
| https://github.com/cmu-db/bustub | MIT (byte-read 1,075 B) | Carnegie Mellon's educational RDBMS — **5,171 ★**, pushed 2026-11-13. The largest restored row in this file by an order of magnitude, and the reference artefact for database teaching worldwide. |
| https://github.com/RWTH-OS/eduOS-rs | Apache-2.0 | RWTH Aachen's teaching operating system in Rust — 493 ★, pushed 2026-10-04. |

## Gaps and caveats

- **`openedx/XBlock` and `openedx/xblock-sdk` exist but are not in the tables above.**
  `openedx/XBlock/master/README.rst` returns `200`, so the repos are real, but no licence
  file could be fetched by any name tried, so we will not assert a licence. Treat the XBlock
  SDK as available and confirm its licence directly before use.
- 🟢 **Both "no root licence file" repos are now resolved, and neither was unlicensed (p897).**
  `moodlehq/moodleapp` grants **Apache-2.0** at **`main/COPYING.txt`** (11,358 B, byte-read) —
  genuinely different from Moodle core's GPL-3.0, so still do not assume the app inherits the
  platform's licence, but the grant is explicit rather than detector-inferred.
  🔴 **`OS4ED/openSIS-Classic` is GPL-2.0, not licence-unclear.** Its `README.md` links the full
  text and it is really there, at **`master/docs/License.txt`** (17,286 B, `sha256₁₂ 224ac3d403e3`).
  The earlier "nothing in the repo says so" was this KB's probe set failing, not the repo:
  **every path we try is at the repository root**, and openSIS keeps its grant one directory down.
  GPL-2.0 is still strong copyleft — the deployment advice in `verticals/solutions.md` is
  unchanged — but *"get written clarification"* is no longer the reason; the licence is known.
- 🟡 **Method fix (p897): extend the licence probe with a `docs/` prefix.** The probe set grew from
  8 to 12 filenames in p896 after `COPYING.txt`/`LICENSE.TXT` misses; openSIS shows the remaining
  axis is **directory, not filename**. Trying `docs/License.txt`, `doc/`, `legal/` and `LICENSES/`
  against each branch would have found it on the first pass. Until that runs, a `NO-LICENSE-FILE`
  in the appendix means *"not at the root"*, and must not be read as *"unlicensed"*.
- 🔴 **The Frappe family carries three different licences, and the popular write-ups get it wrong.**
  Byte-read p897: **`frappe/frappe` is MIT** (the low-code *framework*, 11,120 ★),
  **`frappe/lms` is AGPL-3.0** (33,893 B of verbatim AGPL text, 3,429 ★), and
  **`frappe/education` is GPL-3.0** (a 19-byte `license.txt` reading only *"License: GNU GPL V3"*).
  Several 2026 "best open-source LMS" comparisons list **Frappe LMS as MIT**; that is the
  framework's licence attached to the wrong repo. For a client who needs to keep a derivative
  closed, the distinction is the whole decision — **AGPL-3.0 is network-triggered copyleft.**
- **`projectfedena/fedena` is not a candidate, despite third-party tables listing it as
  Apache-2.0 (p892).** SPDX `NONE`, no licence file under any of four names on either branch,
  last push 2020-05-18. All rights reserved and abandoned. Recorded here and in
  `verticals/solutions.md` so it is not re-proposed.
- **No open-source student information system qualifies as a *foundation*.** The SIS options
  (RosarioSIS, openSIS, Gibbon, i-educar, GegoK12) are in `verticals/solutions.md` — they are
  deployable products, not libraries to build on. There is no Ed-Fi-grade open SIS core.
- **Star counts and last-push dates are measured** via batched `repo:` qualifiers against
  `gh api search/repositories`; see `agents/top.md` for method. 🟢 **The three repos previously
  recorded here as unretrievable were rename aliases, resolved in `p896`** —
  `openedx/openedx-platform` (8,242 ★), `OpenHands/OpenHands` (93,731 ★) and
  `LibreChat-AI/LibreChat` (47,317 ★). A slug that serves `200` on `raw.githubusercontent.com`
  but returns 0 hits from a `repo:` qualifier has been renamed, because raw follows GitHub's
  rename redirects and search does not. **169 of 172 live slugs in this KB resolve on both
  channels; those three were the only failures and all three are now resolved.**

## Appendix — verified metrics table (2026-11-18)

Measured, not asserted. Stars and SPDX licence from `gh api search/repositories`
(batched `repo:` qualifiers); licence text independently read from
`raw.githubusercontent.com`. `SPDX` of `NOASSERTION` means GitHub's detector could not
classify the licence file — usually a modified or dual licence — and the text column is
then the one to trust. No repo in this set is archived.

| Repo | ★ | SPDX | Licence text read | Last push | Days idle |
|---|---|---|---|---|---|
| `ollama/ollama` | 187,466 | MIT | MIT | 2026-11-18 | 0 |
| `openai/whisper` | 113,086 | MIT | MIT | 2026-08-31 | 79 |
| `vllm-project/vllm` | 97,125 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `infiniflow/ragflow` | 94,355 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `opendatalab/MinerU` | 83,893 | NOASSERTION | Apache-2.0 | 2026-11-16 | 2 |
| `docling-project/docling` | 70,725 | MIT | MIT | 2026-11-18 | 0 |
| `mem0ai/mem0` | 69,158 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `BerriAI/litellm` | 63,462 | NOASSERTION (API) | **MIT except `litellm/enterprise/` — byte-verified p891** | 2026-11-18 | 0 |
| `crewAIInc/crewAI` | 61,058 | MIT | MIT | 2026-11-18 | 0 |
| `HKUDS/DeepTutor` | 60,165 | Apache-2.0 | Apache-2.0 | 2026-11-15 | 3 |
| `odoo/odoo` | 55,884 | NOASSERTION | LGPL | 2026-11-18 | 0 |
| `langchain-ai/langgraph` | 45,093 | MIT | MIT | 2026-11-18 | 0 |
| `Crosstalk-Solutions/project-nomad` | 43,902 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `THU-MAIC/OpenMAIC` | 43,856 | MIT | MIT | 2026-11-18 | 0 |
| `patchy631/ai-engineering-hub` | 41,974 | MIT | MIT | 2026-11-01 | 17 |
| `appsmithorg/appsmith` | 41,268 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `datalab-to/marker` | 40,969 | Apache-2.0 | Apache-2.0 | 2026-11-14 | 4 |
| `HKUDS/LightRAG` | 40,754 | MIT | MIT | 2026-11-18 | 0 |
| `qdrant/qdrant` | 35,619 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `ankitects/anki` | 32,874 | NOASSERTION | AGPL-3.0 | 2026-11-17 | 1 |
| `stanford-oval/storm` | 31,906 | MIT | MIT | 2025-09-30 ⚠️ | 414 |
| `assafelovic/gpt-researcher` | 30,768 | Apache-2.0 | Apache-2.0 | 2026-11-12 | 6 |
| `chroma-core/chroma` | 29,709 | Apache-2.0 | Apache-2.0 | 2026-11-13 | 5 |
| `HumanSignal/label-studio` | 28,724 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `promptfoo/promptfoo` | 27,399 | MIT | MIT | 2026-11-18 | 0 |
| `deepset-ai/haystack` | 27,040 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `SYSTRAN/faster-whisper` | 26,844 | MIT | MIT | 2026-11-12 | 6 |
| `temporalio/temporal` | 24,466 | MIT | MIT | 2026-11-18 | 0 |
| `Unstructured-IO/unstructured` | 15,762 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `EleutherAI/lm-evaluation-harness` | 14,498 | MIT | MIT | 2026-11-04 | 14 |
| `apereo/cas` | 11,403 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `bigbluebutton/bigbluebutton` | 9,282 | LGPL-3.0 | LGPL | 2026-11-18 | 0 |
| `jupyterhub/jupyterhub` | 8,368 | BSD-3-Clause | OTHER | 2026-11-05 | 13 |
| `moodle/moodle` | 7,620 | GPL-3.0 | NO-LICENSE-FILE | 2026-11-17 | 1 |
| `oppia/oppia` | 6,998 | Apache-2.0 | Apache-2.0 | 2026-11-18 | 0 |
| `instructure/canvas-lms` | 6,918 | AGPL-3.0 | AGPL-3.0 | 2026-11-10 | 8 |
| `CTFd/CTFd` | 6,917 | Apache-2.0 | Apache-2.0 | 2026-11-10 | 8 |
| `netless-io/flat` | 6,443 | MIT | MIT | 2026-11-10 | 8 |
| `argilla-io/argilla` | 5,204 | Apache-2.0 | Apache-2.0 | 2026-11-16 | 2 |
| `open-spaced-repetition/fsrs4anki` | 4,142 | MIT | MIT | 2026-08-14 | 96 |
| `frappe/lms` | 3,429 | AGPL-3.0 | AGPL-3.0 | 2026-11-18 | 0 |
| `OpenVidu/openvidu` | 2,146 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `iiab/iiab` | 2,053 | GPL-2.0 | LGPL | 2026-11-13 | 5 |
| `jupyterhub/zero-to-jupyterhub-k8s` | 1,727 | NOASSERTION | Apache-2.0 | 2026-11-15 | 3 |
| `Khan/perseus` | 1,600 | MIT | MIT | 2026-11-18 | 0 |
| `OpenHands/software-agent-sdk` | 1,406 | MIT | MIT | 2026-11-18 | 0 |
| `jupyter/nbgrader` | 1,370 | BSD-3-Clause | **BSD-3-Clause — byte-read p897** (`main/LICENSE`, 1,512 B, `sha256₁₂ 3a83d5b8e22c`, *"Copyright (c) 2014 Project Jupyter Contributors"*) | 2026-11-03 | 15 |
| `sakaiproject/sakai` | 1,240 | ECL-2.0 | ECL-2.0 | 2026-11-17 | 1 |
| `Udayraj123/OMRChecker` | 1,196 | MIT | MIT | 2026-09-04 | 75 |
| `learningequality/kolibri` | 1,179 | MIT | MIT | 2026-11-18 | 0 |
| `overhangio/tutor` | 1,133 | AGPL-3.0 | AGPL-3.0 | 2026-11-17 | 1 |
| `DSpace/DSpace` | 1,115 | BSD-3-Clause | BSD | 2026-11-13 | 5 |
| `pkp/ojs` | 1,058 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `chamilo/chamilo-lms` | 1,025 | GPL-3.0 | GPL-3.0 | 2026-11-18 | 0 |
| `kiwix/kiwix-tools` | 1,006 | GPL-3.0 | GPL-3.0 | 2026-11-09 | 9 |
| `moodlehq/moodleapp` | 1,006 | Apache-2.0 | **Apache-2.0 — byte-read p897** (`main/COPYING.txt`, 11,358 B, `sha256₁₂ cfc7749b96f6`). The `NO-LICENSE-FILE` here was the root-only probe, not the repo. | 2026-11-17 | 1 |
| `openeducat/openeducat_erp` | 913 | NOASSERTION (API) | **LGPL-3.0 — byte-verified p891** | 2026-11-16 | 2 |
| `ls1intum/Artemis` | 832 | MIT | MIT | 2026-11-18 | 0 |
| `autolab/Autolab` | 808 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `portabilis/i-educar` | 727 | GPL-2.0 | LGPL | 2026-11-13 | 5 |
| `frappe/education` | 712 | NOASSERTION | 🔴 **GPL-3.0 — byte-read p897** (`develop/license.txt`, **19 B**: the whole file is the string *"License: GNU GPL V3"*). A declaration, not a grant text — see the Frappe note above the table. | 2026-10-30 | 19 |
| `francoisjacquet/rosariosis` | 654 | GPL-2.0 | GPL-2.0 | 2026-11-16 | 2 |
| `GibbonEdu/core` | 641 | GPL-3.0 | GPL-3.0 | 2026-11-18 | 0 |
| `open-scratch/teaching-open` | 637 | Apache-2.0 | Apache-2.0 | 2026-07-06 | 135 |
| `Koha-Community/Koha` | 602 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `LearningLocker/learninglocker` | 587 | GPL-3.0 | GPL-3.0 | 2024-05-30 ⚠️ | 902 |
| `PrairieLearn/PrairieLearn` | 533 | NOASSERTION | MIT | 2026-11-18 | 0 |
| `opencast/opencast` | 513 | ECL-2.0 | ECL-2.0 | 2026-11-18 | 0 |
| `ILIAS-eLearning/ILIAS` | 512 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `instructure/instructure-ui` | 487 | NOASSERTION | MIT | 2026-11-18 | 0 |
| `openedx/codejail` | 477 | Apache-2.0 | Apache-2.0 | 2026-11-16 | 2 |
| `OpenOLAT/OpenOLAT` | 452 | NOASSERTION | Apache-2.0 | 2026-11-17 | 1 |
| `ECNU/EduWork` | 378 | MulanPSL-2.0 | **MulanPSL-2.0 AND MIT** — p886 byte-read **re-confirmed p897**: `main/LICENSE` 9,233 B `sha256₁₂ eb7a1d713eb9` (木兰宽松许可证, 第2版) **and** `main/LICENSE-MIT` 1,085 B `sha256₁₂ dc719b536b8f`. | 2026-11-18 | 0 |
| `tsugiproject/tsugi` | 377 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `Cvmcosta/ltijs` | 373 | Apache-2.0 | Apache-2.0 | 2026-11-11 | 7 |
| `OS4ED/openSIS-Classic` | 351 | NONE | 🔴 **GPL-2.0 — byte-read p897** at **`master/docs/License.txt`** (17,286 B, `sha256₁₂ 224ac3d403e3`, BOM + *"GNU GENERAL PUBLIC LICENSE Version 2, June 1991"*). **Not unlicensed** — the grant is one directory down. | 2026-10-26 | 23 |
| `adlnet/ADL_LRS` | 335 | Apache-2.0 | Apache-2.0 | 2025-11-14 ⚠️ | 369 |
| `vishalsachdev/canvas-mcp` | 334 | MIT | MIT | 2026-11-18 | 0 |
| `openfun/richie` | 318 | MIT | MIT | 2026-11-18 | 0 |
| `Li-Evan/BloomTutor` | 313 | MIT | MIT | 2026-11-17 | 1 |
| `CAHLR/OATutor` | 282 | MIT | MIT | 2026-11-17 | 1 |
| `jupyterhub/nbgitpuller` | 237 | BSD-3-Clause | BSD | 2026-11-02 | 16 |
| `OpenPronounce/OpenPronounce` | 221 | MIT | MIT | 2026-11-09 | 9 |
| `learningequality/studio` | 212 | MIT | MIT | 2026-11-18 | 0 |
| `zijinz456/OpenTutor` | 181 | MIT | MIT | 2026-11-17 | 1 |
| `h5p/h5p-php-library` | 156 | GPL-3.0 | GPL-3.0 | 2026-11-10 | 8 |
| `openfun/marsha` | 152 | MIT | MIT | 2026-11-17 | 1 |
| `yetanalytics/lrsql` | 144 | Apache-2.0 | Apache-2.0 | 2026-11-14 | 4 |
| `openedx/paragon` | 141 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `IIC2233/Syllabus` | 129 | NONE | **Confirmed unlicensed p897** — 42 root probes (3 branches × 14 filenames) plus the `docs/` prefix, all 404. ⛔ No grant: course material from PUC Chile, not reusable code. | 2026-11-17 | 1 |
| `flysheep-ai/education-skills` | 125 | MIT | MIT | 2026-01-30 ⚠️ | 292 |
| `Open-TutorAi/open-tutor-ai-CE` | 118 | BSD-3-Clause | 🟢 **BSD-3-Clause, verbatim — byte-read p897** (`main/LICENSE`, 1,531 B, `sha256₁₂ 57c341d09920`). Three numbered clauses + the standard disclaimer, unmodified; only the copyright line is custom (*"Mohamed El hajji On behalf of all R2D-dev"*). **The SPDX channel was right and this column was wrong.** | 2026-06-26 | 145 |
| `ls1intum/Apollon` | 106 | MIT | MIT | 2026-11-17 | 1 |
| `instructure/common-cartridge-viewer` | 95 | MIT | MIT | 2026-11-04 | 14 |
| `wenflow-org/wenflow` | 72 | MIT | MIT | 2026-11-12 | 6 |
| `openedx/edx-proctoring` | 69 | AGPL-3.0 | AGPL-3.0 | 2026-11-17 | 1 |
| `openedx/edx-ora2` | 64 | AGPL-3.0 | AGPL-3.0 | 2026-11-13 | 5 |
| `1EdTech/openbadges-validator-core` | 61 | Apache-2.0 | Apache-2.0 | 2025-11-04 ⚠️ | 379 |
| `Gego-K12/gegok12` | 57 | NOASSERTION | MIT | 2026-09-23 | 56 |
| `moodlehq/wiki-rag` | 54 | BSD-3-Clause | BSD | 2026-06-15 | 156 |
| `openfun/ralph` | 52 | MIT | MIT | 2026-11-17 | 1 |
| `learningequality/ricecooker` | 32 | MIT | MIT | 2026-11-02 | 16 |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` | 28 | Apache-2.0 | Apache-2.0 | 2026-11-17 | 1 |
| `ls1intum/Ares` | 27 | MIT | MIT | 2026-11-03 | 15 |
| `Citolab/qti-components` | 18 | GPL-3.0 | GPL-3.0 | 2026-11-17 | 1 |
| `ls1intum/edutelligence` | 17 | MIT | MIT | 2026-11-17 | 1 |
| `AI-for-Education/pedagogy-benchmark` | 13 | MIT | MIT | 2026-11-16 | 2 |
| `ls1intum/Pyris` | 12 | MIT | MIT | 2026-06-03 | 168 |
| `warleysr/ankipa` | 10 | MIT | MIT | 2026-11-07 | 11 |
| `learningequality/le-utils` | 7 | MIT | MIT | 2026-11-02 | 16 |
| `virtualryder/edu-ai-agents` | 4 | NOASSERTION | MIT | 2026-10-10 | 39 |
| `LMS-COMPASSO/lms` | 1 | MIT | MIT | 2026-11-17 | 1 |
| `Abdulrahman-hayatu/lessonplan-ng` | 0 | Apache-2.0 | Apache-2.0 | 2026-10-28 | 21 |
| `bishoynabilanis/jessica` | 0 | MIT | MIT | 2026-11-18 | 0 |
| `mayuribagga/ai-worksheet-maker` | 0 | MIT | MIT | 2026-10-26 | 23 |
| `vulinh1704/ai-tutor-agent` | 0 | MIT | MIT | 2026-11-16 | 2 |

⚠️ = no push in over nine months. **Maintenance risk, flagged explicitly:**

- **`LearningLocker/learninglocker`** (587 ★) — last push 2024-05-30, 902 days idle.
- **`stanford-oval/storm`** (31,906 ★) — last push 2025-09-30, 414 days idle.
- **`1EdTech/openbadges-validator-core`** (61 ★) — last push 2025-11-04, 379 days idle.
- **`adlnet/ADL_LRS`** (335 ★) — last push 2025-11-14, 369 days idle.
- **`flysheep-ai/education-skills`** (125 ★) — last push 2026-01-30, 292 days idle.

