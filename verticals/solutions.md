---
industry: education
region: Global
updated: 2026-11-19
---

# Vertical solutions — education

Deployable systems, not libraries: things a client may already be running, or can stand up
in days, and that AI can be layered onto. All URLs and licences verified 2026-11-18 via
`raw.githubusercontent.com`.

Education's equivalent of "Odoo for ERP" is not one product but four categories: the LMS
(Moodle, Open edX, Canvas), the SIS (RosarioSIS, Gibbon, openSIS, i-educar), the repository
(DSpace, Koha, OJS) and the live-classroom stack (BigBlueButton, Opencast, OpenVidu). An
engagement usually touches at least two.

## Learning management systems

| Platform | Repo | Licence | Where it is strong | AI layering seam |
|---|---|---|---|---|
| **Moodle** | https://github.com/moodle/moodle | GPL-3.0 (`COPYING.txt`) | Everywhere; the default in EMEA and LATAM public education | Plugin API + LTI 1.3 tool. Moodle HQ's own https://github.com/moodlehq/wiki-rag (BSD-3-Clause) shows the first-party RAG pattern |
| **Open edX** | https://github.com/openedx/openedx-platform | AGPL-3.0 | Large-scale MOOCs, corporate academies | XBlocks (https://github.com/openedx/XBlock, **Apache-2.0**) and `edx-ora2` open-response grading. **Slug corrected p896** — `openedx/edx-platform` is a rename alias, not the canonical repo. |
| **Canvas LMS** | https://github.com/instructure/canvas-lms | AGPL-3.0 | North American higher ed | Rich REST API; https://github.com/vishalsachdev/canvas-mcp (MIT) exposes it to agents directly |
| **Artemis** | https://github.com/ls1intum/Artemis | MIT | CS/engineering programmes with automated code assessment | First-party AI tier already exists (`edutelligence`, `Pyris`) — **the lowest-friction permissive starting point** |
| **Kolibri** | https://github.com/learningequality/kolibri | MIT | Offline/low-bandwidth deployments | Offline-capable; pair with `ollama` for a fully disconnected tutor |
| **Chamilo** | https://github.com/chamilo/chamilo-lms | GPL-3.0 | LATAM, francophone Africa, Spain | LTI tool provider |
| **ILIAS** | https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | German-speaking EMEA, public sector, regulated training | Plugin slots, SCORM/LTI |
| **Sakai** | https://github.com/sakaiproject/sakai | ECL-2.0 | Research universities | LTI; ECL-2.0 is patent-clause Apache |
| **OpenOLAT** | https://github.com/OpenOLAT/OpenOLAT | Apache-2.0 | Switzerland, Germany, Austria | Permissive — under-used given its maturity |
| **Oppia** | https://github.com/oppia/oppia | Apache-2.0 | Foundational literacy/numeracy, emerging markets | Exploration framework with misconception modelling |
| **Frappe LMS** | https://github.com/frappe/lms | AGPL-3.0 | SMB/corporate training on the Frappe stack | Frappe app hooks; integrates with ERPNext |
| **Mentingo** | https://github.com/Selleo/mentingo | **MIT** (`LICENSE@main`, `Copyright (c) 2024 Selleo`) | Corporate L&D, onboarding and compliance training; white-label, multi-tenant | **No layering needed — the AI mentor is first-party.** Postgres + pgvector is already the retrieval substrate; one-click AWS Marketplace deploy |
| **Pupilfirst** | https://github.com/pupilfirst/pupilfirst | **MIT** — multi-grant, byte-read p899 (`LICENSE@master`, 1,684 B, `sha256₁₂ bda0aa6d49f2`) | Cohort-based, asynchronous programmes with review workflows and mentoring built in | 🔴 **Added p899, and it displaces a standing claim in this file.** This KB records **Mentingo (109 ★) as its counter-example to "the platforms clients run are copyleft"** — the first MIT LMS. **Pupilfirst is MIT and 982 ★, nine times larger.** Multi-grant: `docs/` is **CC-BY-SA-4.0**, client-side JavaScript is MIT, everything else MIT — so unlike PrairieLearn's superficially similar structure there is **no proprietary tier**, and unlike Open edX the client JS is not AGPL. 🟡 **Caveat that decides how to use it: last push 2025-12-09, ~11 months idle.** Read it as a permissive, complete, forkable codebase rather than an upstream to track. From **Pupilfirst Pvt. Ltd., India** — the only APAC-origin LMS in this table. |
| **Tutor** | https://github.com/overhangio/tutor | AGPL-3.0 | The de facto Open edX deployment/ops tool | Plugin system for injecting services into an Open edX cluster |
| **SmartKBS** | https://github.com/youufis/SmartKBS | **AGPL-3.0** (byte-read `master/LICENSE`, 34,833 B, `sha256₁₂ c017a2e33418`) | **Chinese K-12 — primary, junior and senior secondary.** Added `p906`, and it is the first Chinese-origin platform in this file. A general-subject **AI teaching platform** rather than an LMS with AI bolted on: item bank with intelligent paper composition, examinations, practice, homework with **automatic marking**, live classroom interaction (buzz-in, random questioning, polling, group discussion, collaborative whiteboard), roll-call and attendance, a 12-level title/points scheme, learning analytics and per-student growth records. Self-describes its worked examples as information technology and general technology subjects. **99 ★, pushed 2026-11-18** — actively developed. | 🔵 **It is the seam, which is the point:** the classroom-interaction and attendance tiers are the two things Moodle, Open edX and Canvas all push to third-party plugins, and here they are first-party next to the grading tier. 🔴 **AGPL-3.0 — a closed, branded derivative is not available**, so this is a deploy-and-extend or reference-architecture option, not a white-label one; Mentingo remains the only MIT platform in this file. 🟡 Single-maintainer, created 2026-05-26: treat continuity as a risk and read the 34,833 B licence as a filled-in appendix, not a modified grant. |

🔴 **Added `p907`, and it is an absence rather than a platform.** The table above covers Moodle,
Open edX, Canvas and the permissive cores — and **`D2L Brightspace` and `Blackboard`, two of the
four LMS platforms a higher-ed client is likely to already be running, had no row anywhere in this
KB's delivery files before this pass.** Neither is open source, which is why they never appeared on
an open-source shelf; but a vertical-solutions file exists to describe **what a client is already
running**, and on that test the omission was wrong.

What `p907` found, via global code search:

| Platform | Open source? | The seam that exists today | Licence |
|---|---|---|---|
| **D2L Brightspace** | 🔴 No — commercial | https://github.com/GuanmingQiao/POLITEMALL-MCP — MCP server over two Singapore polytechnic/ITE tenants (`lms.polite.edu.sg`, `nyplms.polite.edu.sg`), npm `@qiaoguanming/politemall-mcp` | **MIT** (byte-read) |
| **Blackboard (Ultra)** | 🔴 No — commercial | https://github.com/andrsnrua/universidad-pacifico-mcp — Universidad del Pacífico, Perú; **70 tools**, local document extraction, private exports | **ISC** (byte-read) |
| **Blackboard (classic)** | 🔴 No — commercial | https://github.com/bolgerru/blackboard-mcp — Trinity College Dublin, deadline tracker. 🔴 **No licence file: read only, do not copy** | 🔴 none |
| **PowerSchool** (SIS, parent-facing) | 🔴 No — commercial | https://github.com/cculb/schoolconnect — parent-portal extraction to SQLite + MCP server | **MIT** (byte-read) |

🔵 **The seam for a commercial LMS is the agent bridge, not a plugin** — and the published examples
reach the platform **as the signed-in person**, which needs no procurement and is also why they are
not deployable as-is. `compose/patterns.md` **P26** scopes the sanctioned build;
`intel/trends.md` **T30** has the cohort and the governance argument. 🟡 These are 0–2 ★ projects:
reference implementations for a tool surface, not systems to deploy.


**Added p893 — the copyleft rule now has a real exception.** Every other LMS in the table above
is GPL, AGPL or ECL. **Mentingo (109 ★, pushed 2026-11-18) is MIT**, licence byte-read, and it
is *AI-native* rather than AI-retrofitted: the mentor and role-play tiers ship with the
platform. That matters for exactly one question, and it is the question clients ask most —
*"can we brand this and keep it closed?"* On Moodle, Open edX or Canvas the answer is no without
an LTI/MCP separation. On Mentingo it is yes.

Two cautions before it displaces Artemis as the default permissive pick. It is **corporate L&D,
not K-12 or higher ed** — there is no gradebook-of-record, no SIS integration and no
accreditation story. And at 109 ★ with a single vendor (Selleo) behind it, the governance risk
is the mirror image of Moodle's: permissive licence, thin community. **Use it where the client
wants a product; use Artemis or OpenOLAT where the client wants an institution.**

## Student information systems and school ERP

The weakest category for AI today and therefore the strongest opportunity.
`verticals` note: 🔴 **Corrected p900 — GegoK12 is no longer the only MIT-licensed SIS here,
and it is no longer the largest.** This file carried *"GegoK12 is the only MIT-licensed SIS
verified here"*; **`academico-sis/academico` is MIT, 413 ★ and was pushed 2026-11-18**, against
GegoK12's 57 ★ and last push 2026-09-23. It was in this base's own `logged-not-shelved` ledger
for an unknown number of passes. 🔵 **Both remain true answers to "can the client keep the
derivative closed"** — Academico for an actively maintained core, GegoK12 for a K-12-shaped
data model — and the honest reading is that the permissive SIS option was understated, not
absent.

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Academico** | https://github.com/academico-sis/academico | **MIT** | **Added p900** — 413 ★, pushed 2026-11-18, out of this base's own ledger. School management on **Laravel + Filament**: enrolments, courses, attendance, invoicing. Aimed at **small and medium institutions**, not districts — so it does not displace RosarioSIS on scale, it displaces it on **licence**. 🔵 Filament is an admin-panel framework, which means the CRUD surface an AI tier would otherwise have to build is already generated; the layering seam is a Laravel service plus Filament actions |
| **GegoK12** | https://github.com/Gego-K12/gegok12 | MIT | K-12 school ERP/SIS, PHP/Laravel. Permissive licence verified in repo, confirming the vendor's claim. |
| **RosarioSIS** | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | Students, grades, scheduling, attendance, billing, discipline, food service. PHP + PostgreSQL/MySQL. Active. |
| **Gibbon** | https://github.com/GibbonEdu/core | GPL-3.0 | Full school platform, strong in international schools across APAC. |
| **openSIS Classic** | https://github.com/OS4ED/openSIS-Classic | 🔴 **GPL-2.0 — resolved p897.** Byte-read at **`master/docs/License.txt`** (17,286 B, `sha256₁₂ 224ac3d403e3`); the `README.md` links it. GitHub's SPDX still reports `NONE` because the file is not at the repository root, and this KB previously recorded it as *"none declared"* for the same reason. **The licence is known; it is strong copyleft.** Fine to deploy and host for a client; a proprietary derivative is not. | Long-standing web SIS from OS4Ed, 351 ★, pushed 2026-10-26. |
| **i-Educar** | https://github.com/portabilis/i-educar | GPL-2.0 | **Brazilian public-education SIS**, built around Brazilian regulatory requirements. The default SIS starting point for a LATAM public-sector engagement. |
| **OpenEduCat** | https://github.com/openeducat/openeducat_erp | LGPL-3.0 (byte-verified p891 from `LICENSE@master`; the GitHub API reports `NOASSERTION` because the file is a preamble plus the GPL text, not an SPDX-matchable template) | Education ERP built **on Odoo** — admissions, fees, LMS, library in one. |
| **Odoo** | https://github.com/odoo/odoo | LGPL-3.0 | The general ERP underneath OpenEduCat; the actual "Odoo for education" answer is Odoo plus OpenEduCat. |
| **Frappe Education** | https://github.com/frappe/education | GPL-3.0 (`license.txt`: "License: GNU GPL V3") | Education module on the ERPNext/Frappe stack. |
| **UniTime** | https://github.com/UniTime/unitime | **Apache-2.0** (`LICENSE@master`) | **Restored p894.** Apereo university **course and exam timetabling plus student scheduling**, 360 ★, **pushed 2026-11-17**. Runs standalone or interfaces with an existing SIS. **The one permissive, actively maintained system in this category** — and the answer to the registrarial gap at the platform layer. Its solver https://github.com/UniTime/cpsolver is **LGPL-3.0** (84 ★): keep it behind a service boundary in a closed derivative. |
| **Timetablely** | https://github.com/GEOSOFT-GLOBAL/timetablely | MIT | **Restored p894.** Automated timetable generator, 27 ★ — the small-scale permissive alternative to UniTime. **Pushed 2026-08-17, three months idle;** a starting point, not a dependency. |
| **i-Diário** | https://github.com/portabilis/i-diario | **AGPL-3.0** — 🔴 **byte-read correction, p896** | **Restored p896.** The teacher-facing *diário de classe* (class register: attendance, marks, lesson records) companion to **i-Educar** above, from the same Brazilian publisher — 117 ★, pushed 2026-10-14. 🔴 **GitHub reports `NOASSERTION` and the licence is AGPL-3.0**: the `LICENSE` file is the **Affero GPL in Portuguese translation** (*"LICENÇA PÚBLICA GERAL AFFERO GNU"*, 35,326 B), which GitHub's SPDX matcher cannot recognise. An engagement that read the API field alone would treat the strongest copyleft in this file as "licence unknown". **Together with i-Educar this is the most complete open Brazilian public-school stack.** |
| **Gestão Escolar** | https://github.com/Antonio-Neves/Gestao-Escolar | MIT | **Restored p896.** Python/Django school-management system, 50 ★, pushed 2026-10-12, Portuguese-language. Self-described as in development. **The only MIT-licensed LATAM-origin school system this KB has verified** — thin, but it is the permissive option in a category where the mature Brazilian systems are GPL and AGPL. |

**Rejected this pass, recorded so it is not re-proposed (p892).** A fresh search for
open-source school ERP returned **Fedena** in a licence comparison table under **Apache-2.0**,
alongside OpenEduCat and openSIS. It verifies as neither usable nor maintained:
https://github.com/projectfedena/fedena has **547 ★**, SPDX **`NONE`**, **no `LICENSE`,
`LICENSE.md`, `LICENSE.txt` or `COPYING` on `main` or `master` (404 on all eight)**, and a last
push of **2020-05-18** — roughly 2,375 days idle. No licence file means **all rights reserved**.
The comparison table's Apache-2.0 claim has no basis in the repository. See `repos/trending.md`
for the method note: this is the second aggregator-sourced licence error caught in two passes.

**That p892 negative result is retired (p894), and it was wrong in all three of its clauses.**
It read: *"The category is small, static, and copyleft or licence-unclear end to end... the
platform layer beneath the missing registrarial AI agent is not moving either."* **UniTime is
360 ★, Apache-2.0, and was pushed 2026-11-17.** The error was not a bad measurement — an
earlier pass had verified UniTime and hash-checked its Apache payload — it was that the finding
never reached this file, and the 2026-11-18 rewrite dropped it. The p892 leg then re-derived an
absence from a table that had already lost the counter-example. **Method consequence, recorded
in `repos/trending.md`: diff a canonical table against the append-only history before rewriting
it, and before concluding a category is empty.**

**What survives, better specified.** The opportunity note at the top of this section stands and
sharpens: **the registrarial gap is an agent tier, not a platform.** Timetabling, exam
scheduling and student scheduling have a permissive, maintained substrate; enrolment decisioning,
transcripts and financial aid still have nothing, and financial-aid decisioning is EU Annex III
high-risk. See `compose/patterns.md` **P12**.

## Assessment and grading platforms — added p899

Deployable grading systems, as distinct from the grading *libraries* in `repos/foundations.md`.
**This section did not exist before p899**, which is why `p894` was able to record automated
grading as a category with nothing in it — see `repos/trending.md` p899 for how that artefact
was produced.

| Platform | Repo | Licence | Where it is strong | AI layering seam |
|---|---|---|---|---|
| **Anubis** | https://github.com/AnubisLMS/Anubis | **MIT** | **Added p900** — 383 ★, pushed 2026-09-15, from **NYU**. A distributed LMS built for one job: **automating computing-science courses**. Per-student cloud IDEs, autograding and submission pipelines, deployed on Kubernetes | The IDE *is* the seam — an agent that sees the student's live workspace rather than only their final submission. 🔵 **The only platform in this file where formative feedback can be given mid-attempt**, which is what every tutor in `agents/top.md` claims to want and cannot reach through an LMS API |
| **Submitty** | https://github.com/Submitty/Submitty | **BSD-3-Clause** (`LICENSE.md@main`, 1,542 B, `sha256₁₂ c123708cb4ef`) | University CS and engineering courses; submission + autograding + TA/manual grading + rubrics in one system. 807 ★, pushed 2026-11-18, developed at **RPI / Rensselaer Center for Open Source Software** since 2014 | **The permissive anchor of this category.** No patent clause, no enterprise carve-out, no copyleft — the one grading platform a client can take a closed derivative of. Layer an AI rubric-assist on the manual-grading tier, leaving the deterministic autograder untouched (which is what keeps it defensible — see `agents/top.md`, `EDU AI Agent Suite`) |
| **PrairieLearn (CE)** | https://github.com/PrairieLearn/PrairieLearn | 🔴 **AGPL-3.0 Community Edition + proprietary Enterprise Edition. NOT MIT — corrected p899** | Randomised, auto-graded STEM problem generation; the strongest assessment *engine* here. 533 ★, pushed 2026-11-18 | 🔴 **Read the licence note in `repos/foundations.md` before planning anything.** `apps/course-agent/` — the AI tier — is **Enterprise Edition and requires a paid subscription for production use**, with a clause assigning your modifications to PrairieLearn, Inc. Build the AI seam **outside** the EE directories, against the AGPL CE, and host rather than redistribute |
| **Autolab** | https://github.com/autolab/Autolab | Apache-2.0 | CMU's autograding platform with secure job execution | Patent-granting and permissive; pair with `autolab/Tango` (Apache-2.0) when grading must be called from something that is not Autolab |
| **Pawtograder** | https://github.com/pawtograder/platform | 🔴 **GPL-3.0-or-later** — SPDX reports `NOASSERTION`; byte-read p899 (`LICENSE@main`, 658 B, `sha256₁₂ 61d7698783f4`) | Positioned as the open **GitHub Classroom replacement** for CS courses: Actions-based autograding, rubrics, office hours, gradebook. 22 ★, pushed 2026-11-18 | New and small. **Strong copyleft** — read it for the CI-as-grader pattern, do not plan a closed derivative |

🔵 **Category note.** Three of the four are university-built (RPI, UIUC, CMU) and that is the
durability signal, not the star counts. **Only Submitty and Autolab are safe for a closed
derivative**; PrairieLearn and Pawtograder are host-only.

## Repositories, libraries and scholarly publishing

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **DSpace** | https://github.com/DSpace/DSpace | BSD-3-Clause | Institutional repository standard, 1,115 ★. **The most permissive major system in this file.** |
| **Koha** | https://github.com/Koha-Community/Koha | GPL-3.0 | The incumbent open-source integrated library system. |
| **Open Journal Systems** | https://github.com/pkp/ojs | GPL-3.0 | Scholarly publishing; very heavily used in LATAM academia. |

## Live classroom, video and lecture capture

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Jitsi Meet** 🆕 | https://github.com/jitsi/jitsi-meet | **Apache-2.0** | `30,255★` / `8,134` forks, pushed `2026-11-18`. Licence byte-read (`master/LICENSE`, `12,596 B`, `sha256₁₂ eae52e200cd8`). **The largest permissive live-classroom platform in open source**, and a finished conferencing *application* — self-hostable, mature, with its own mobile SDKs. Added `p901` after an audit against an external curated index found it absent from all 6,494 slugs in this base. Prefer it over OpenVidu when the client wants a working classroom; prefer OpenVidu when they want to *build* one from WebRTC primitives. Not an education project — it is general conferencing that education deploys, which is why every `{education}`-qualified search leg missed it. |
| **BigBlueButton** | https://github.com/bigbluebutton/bigbluebutton | LGPL | Purpose-built virtual classroom with Moodle/Canvas integrations. The incumbent. |
| **Opencast** | https://github.com/opencast/opencast | ECL-2.0 | Lecture capture and video management at university scale. Pipe output into `faster-whisper`. |
| **OpenVidu** | https://github.com/OpenVidu/openvidu | Apache-2.0 | WebRTC platform; permissive, build-your-own-classroom. |
| **Flat** | https://github.com/netless-io/flat | MIT | `6,443★`, pushed `2026-11-10`. Interactive online classroom with whiteboard. **APAC-origin (China), MIT** — the strongest *copyleft-free* option when the client needs MIT specifically. (Through `p900` this row read "strongest permissive option in this category"; **`p901` corrected that** — Jitsi Meet is Apache-2.0 at `30,255★`. Flat remains the pick when MIT is a hard requirement or when the whiteboard is the product.) |
| **Marsha** | https://github.com/openfun/marsha | MIT | LMS-embedded video management from France Université Numérique. |

## Notebook-native classroom — added `p902`

Deployable systems for the courses where the *artefact the student submits is executable*. This
category was absent from this file, and it is the one category where the permissive option is the
incumbent rather than the exception.

| Platform | Repo | Licence | Where it is strong | AI layering seam |
|---|---|---|---|---|
| **BinderHub** 🆕 | https://github.com/jupyterhub/binderhub | **BSD-3-Clause** (`main/LICENSE`, `1,522 B`, `sha256₁₂ 611f531642d5`) | `2,673★`, pushed `2026-11-14`. Any course whose content is a git repo: students get a running environment from a URL, with **no install day and no lab image**. The lightest-weight classroom in this file | Kubernetes-native, so the AI tier is a sidecar service the notebook calls; content stays a repo, so a curriculum agent can open a pull request against it |
| **JupyterHub** | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | The authenticated, persistent-storage case — institutional deployments with per-student state | Services API and per-user servers; an assistant runs as a Hub service with the student's own scope |
| **nbgallery** 🆕 | https://github.com/nbgallery/nbgallery | **MIT** (`master/LICENSE`, `1,071 B`, `sha256₁₂ 7900749dcb3b`) | `150★`, pushed `2026-10-22`. Sharing, search, usage analytics and **automated health checks** over a notebook corpus — a notebook LMS in all but name | Permissive and small enough to fork outright. The health-check runner is a natural place to hang an agent that *repairs* a broken notebook rather than just flagging it |

🟢 **This is the one tier in this file with no copyleft problem.** Environment (`binderhub`, BSD-3),
auth and persistence (`jupyterhub`, BSD-3), sharing (`nbgallery`, MIT), assignment flow (`nbgrader`,
BSD-3), deterministic marking (`nbval`, BSD-3) and content-as-text (`jupytext`, MIT) are **all
permissive, with no enterprise carve-outs** — compare the LMS table above, where the incumbents are
AGPL/GPL. 🔵 **Delivery consequence: a client in a CS or data-science faculty can be given a
classroom whose derivative they own outright**, which is not true of any Moodle or Open edX
engagement. The library tier is in `repos/foundations.md`; the wiring is `compose/patterns.md` **P22**.

## Study tools, practice and assessment delivery

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Anki** | https://github.com/ankitects/anki | AGPL-3.0 | Spaced repetition at scale. Pair with https://github.com/open-spaced-repetition/fsrs4anki (MIT) for the FSRS scheduler and https://github.com/warleysr/ankipa (MIT) for pronunciation scoring. |
| **PrairieLearn** | https://github.com/PrairieLearn/PrairieLearn | MIT | Randomised auto-graded assessment delivery. Deployable product and library both. |
| **Autolab** | https://github.com/autolab/Autolab | Apache-2.0 | CMU autograding platform with secure execution. |
| **CTFd** | https://github.com/CTFd/CTFd | Apache-2.0 | Capture-the-flag platform — the practical delivery vehicle for cybersecurity curricula. |
| **OMRChecker** | https://github.com/Udayraj123/OMRChecker | MIT | Scans paper bubble sheets. High value anywhere exams are still on paper. |
| **Teaching-Open** | https://github.com/open-scratch/teaching-open | Apache-2.0 | Scratch-based programming teaching platform (APAC/China origin). |
| **OpENEM** | https://github.com/migueldsants/OpENEM | **AGPL-3.0** (byte-read `main/LICENSE`, 34,523 B) | **Added `p904` — LATAM, Brazil.** Open platform for **ENEM** preparation (Brazil's national upper-secondary examination, taken by millions annually): question bank, mock exams and study tooling. 9 ★, 14,201 KB, pushed **2026-11-13**, 0 open issues. 🔵 **Deploy it where the brief is national-exam preparation at public-system scale** — the artefact every school in the country shares, and the thing LATAM open source actually builds against (`agents/top.md`, LATAM bullet). Its maintainer also publishes the essay-grading **agent skill** in `agents/top.md`, so platform and agent can be taken from one source. 🔴 **AGPL-3.0: deployable and forkable, not embeddable in a closed product** — if the client needs a proprietary derivative, take the pattern and not the code. |
| **microHelium** | https://github.com/UnitedOpen-Source/microHelium | **AGPL-3.0** (byte-read `master/LICENSE`, 34,523 B) | **Added `p904` — LATAM, Brazil.** Laravel + Vue **online judge and ICPC-style contest system** with a practice mode and teaching-language support including Portuguese. Created **2017**, pushed **2026-11-13**, 4 ★, 2 forks, 18,955 KB, 24 open issues — 🔵 **nine years of maintenance is the finding**, against a channel whose median project is months old. Sits beside `Autolab` and `PrairieLearn` as automated-execution assessment, with the contest and practice framing that fits computing education and olympiad programmes. 🔴 **AGPL-3.0.** |

## Low-connectivity and offline deployment

The category that decides whether a rural LATAM, African or South Asian engagement is
deliverable at all.

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Internet-in-a-Box** | https://github.com/iiab/iiab | GPL-2.0 | Turnkey offline server bundling Kiwix, Kolibri and more onto low-cost hardware. |
| **Kiwix** | https://github.com/kiwix/kiwix-tools | GPL-3.0 | Offline Wikipedia and ZIM content serving. |
| **Project NOMAD** | https://github.com/Crosstalk-Solutions/project-nomad | Apache-2.0 | Offline-first knowledge/education server. Permissive alternative to the above. |
| **Kolibri** | https://github.com/learningequality/kolibri | MIT | See LMS table — designed offline-first from the start. |
| **elimu.ai** | https://github.com/elimu-ai/webapp | MIT (byte-read `main/LICENSE`, 1,065 B) | **Restored p895; region EMEA.** Early-grade literacy for **out-of-school children**, Sub-Saharan (Tanzania/Kenya). 41 ★ / **67 forks**, pushed **2026-11-17**. **Africa-origin and permissive — the only such platform this KB has verified.** The component that matters here is https://github.com/elimu-ai/appstore (MIT, 29 ★): **installs and updates APKs with no app store and no network**, which is a harder problem than offline content and is already solved. `launcher` (MIT, 9 ★) enforces an EGRA/EGMA path. 🔴 **Exclude `ml-authentication` (face-recognition student login — biometric identification of children).** 🟡 Licence and metadata verified; **source not read** (`Gap 486-J`). |
| **Mishkat** (`GT-MISHKATKIDS`) | https://github.com/SalehGNUTUX/GT-MISHKATKIDS | **GPL-3.0** (byte-read `main/LICENSE`, 34,819 B) | **Added `p903` — EMEA, MENA, Arabic-language.** Ages 4–10, and the only system in this file that runs **no inference at runtime at all**: its own header declares *fully local, works offline, no AI at runtime, no cost, the child's data never leaves the device*. Ships **today** (pushed 2026-11-18) as an installable offline PWA, GNU/Linux `AppImage`/`DEB`/`RPM`, and Android `APK` — 3 ★, 358,758 KB, most of it local Qur'anic recitation audio. 🔵 **Deploy it where connectivity and per-seat inference cost are the binding constraints and the brief is early childhood**: there is no API bill, no egress, and nothing to sign a DPA over, which also makes it the cleanest answer in this file to a child-data regulator. Pedagogy is inverted — the child teaches an amnesiac robot (the protégé effect) — so it is a *complement* to Kolibri and elimu.ai, not a substitute: they deliver curriculum, this one drills consolidation through teaching. 🔴 **GPL-3.0: deployable and forkable, not embeddable in a closed product.** Scoping caveat: explicit Islamic doctrinal frame with Qur'an recitation as a first-class module — a feature for Gulf and North African deployments, a decision to make elsewhere. The architecture is portable independently of the content; `compose/patterns.md` **P22** is how to reuse it. |

## Supporting platform services

| Platform | Repo | Licence | Notes |
|---|---|---|---|
| **Apereo CAS** | https://github.com/apereo/cas | Apache-2.0 | SSO incumbent in higher ed. Where you enforce per-role access to an AI tier. |
| **phpCAS** | https://github.com/apereo/phpCAS | Apache-2.0 | **Restored p896.** The **PHP** CAS client, 802 ★ — the one that matters for Moodle. The row above is the server; this is how your tool actually joins the institution's existing SSO. **Pushed 2026-06-30; pin it.** |
| **java-cas-client** | https://github.com/apereo/java-cas-client | Apache-2.0 (byte-read; API says `NOASSERTION`) | **Restored p896.** JVM CAS client, 949 ★, pushed 2026-11-16. |
| **Aspects** | https://github.com/openedx/openedx-aspects | Apache-2.0 | **Restored p896.** First-party Open edX analytics — permissive, unlike the platform. |
| **Richie** | https://github.com/openfun/richie | MIT | Course catalogue/marketing CMS for Open edX. |
| **JupyterHub** | https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | Multi-user computational classrooms. |
| **Appsmith** | https://github.com/appsmithorg/appsmith | Apache-2.0 | Builds the teacher review queue that makes human-in-the-loop real rather than aspirational. |

## Mobile clients — permissive, and separable from their copyleft servers (restored in `p896`)

The most commercially useful licence asymmetry in this file. **Moodle, Open edX and Oppia are
GPL or AGPL on the server and permissive on the phone.** A studio can therefore ship a branded,
closed mobile experience over a copyleft platform the client already runs — which is exactly the
engagement shape that otherwise dies on the licence review. These rows were carried here and
deleted by the 2026-11-18 cleanup.

| Client | Repo | Licence | Server licence | Note |
|---|---|---|---|---|
| **Moodle App** | https://github.com/moodlehq/moodleapp | **Apache-2.0** | Moodle is GPL-3.0 | 1,007 ★, pushed 2026-11-17, **maintained by Moodle HQ itself**. The largest permissive first-party artefact in the Moodle ecosystem. Licence byte-read at `main/COPYING.txt`. |
| **Open edX Android** | https://github.com/openedx/openedx-app-android | **Apache-2.0** | Open edX is AGPL-3.0 | 38 ★, pushed 2026-11-09. |
| **Open edX iOS** | https://github.com/openedx/openedx-app-ios | **Apache-2.0** | Open edX is AGPL-3.0 | 31 ★, pushed 2026-10-30. |
| **Oppia Android** | https://github.com/oppia/oppia-android | Apache-2.0 | Oppia is Apache-2.0 | 422 ★, pushed 2026-11-18. Offline-capable by design — the mobile half of the low-connectivity brief. |

## Proctoring and exam integrity — restored in `p896`, and read the prohibition first

🔴 **Regulatory position before the rows, because it decides whether any of them can ship.**
Under the EU AI Act, *inferring emotions* in an education institution is not a high-risk
practice to be managed in 2027 — it is a **prohibited practice, in force since 2 February
2025**, outside narrow medical and safety grounds. Exam-access and assessment proctoring is
*separately* Annex III high-risk (obligations from 2 December 2027). So an EMEA proctoring build
has a hard floor: **no affect, stress or "suspicion" inference at all**, today. The open repos
below are near-uniformly built on webcam behaviour analysis, which is the capability the
prohibition targets.

| Tool | Repo | Licence | Stars / last push | Note |
|---|---|---|---|---|
| **OpenProctor** | https://github.com/kamlendras/OpenProctor | **AGPL-3.0** | 16 ★ · 2025-05-28 | The largest of them, and **idle for 18 months**. AGPL on top of the regulatory problem. |
| **pariksha** | https://github.com/SriSatyaLokesh/pariksha | **AGPL-3.0** | 0 ★ · 2026-11-07 | Active but single-author. |
| **sudosylabs/proctor** | https://github.com/sudosylabs/proctor | **AGPL-3.0** | 0 ★ · 2026-11-16 | Active but single-author. |
| **Proctora** | https://github.com/amaanwarsi/Proctora | MIT | 3 ★ · 2026-04-07 | The only permissive one. |
| **Online-Proctoring-system** | https://github.com/code-by-abrar/Online-Proctoring-system | MIT | 0 ★ · 2026-09-19 | Student project. |
| **ganesh-786/Proctor** | https://github.com/ganesh-786/Proctor | MIT | 0 ★ · 2025-06-09 | Idle. |

🔵 **The honest read: there is no adoptable open proctoring platform, and that is the finding.**
The category tops out at 16 ★ with the largest entry dormant, while `openedx/edx-proctoring`
(AGPL-3.0, in `repos/foundations.md`) remains the only institution-maintained option. For an EU
engagement the defensible product is **integrity by assessment design** — randomised item
generation (`PrairieLearn`), authenticated submission over CAS, and auditable human review
(`Appsmith`) — not behavioural surveillance. That is a studio position worth stating to a client
before they ask for a proctoring pilot.

## Curriculum data and learning-content assets

**Added in pass p890.** Not platforms, but deployable/extensible content assets — and the
category where this KB's MIT/Apache/BSD screen needs a different question asked, because a
*data* licence is not a *software* licence.

| Asset | Repo | Licence | Note |
|---|---|---|---|
| **os-taxonomy** | https://github.com/withmarbleapp/os-taxonomy | **ODbL-1.0** | Open curriculum graph for children's learning, 7,724 ★, pushed 2026-11-17. **Licence warning:** the Open Database Licence carries a **share-alike obligation on derived databases**. Extend the taxonomy and the extension may have to be published under ODbL. Excellent as a reference or an input; **not** a base for a proprietary curriculum data asset without counsel. |
| **jiangshan-map** | https://github.com/DeanChensj/jiangshan-map | GPL-3.0 | 江山时序 — interactive historical atlas of China, 403 BCE to present, 18 dynasties, with quiz modes. 7,708 ★, pushed 2026-11-18. The largest new education *content application* found. APAC-origin. GPL-3.0 blocks a closed derivative; deployable as-is. |

**Pattern worth noting.** Content assets in education are increasingly published under data or
copyleft licences while the *tooling* stays permissive — the inverse of the platform/tooling
split in this KB's headline fact. Licence triage therefore has to be run per artefact class,
not once per engagement.

**63 platforms and content assets, all URL- and licence-verified**, counted programmatically
across this file's tables (`UniTime` and `Timetablely` were restored in p894). **15 were restored
in `p896`** — four mobile clients, six proctoring tools, two Brazilian school systems, two CAS
clients and the Open edX analytics stack — after the shelf-vs-history diff showed they had been
deleted from this file by the 2026-11-18 cleanup rewrite without being listed as removals. All
re-measured today on both channels.

## What you inherit when you deploy one of these — measured `p905`

A vertical platform is chosen on features and deployed with its dependency tree. This section records
the second half, byte-read from each platform's manifests on its real default branch.

| Platform | Licence | Direct deps you take on | Rebuildable from its manifests? | Third-party grants disclosed? |
|---|---|---|---|---|
| **Moodle** | GPL-3.0 | **316 resolved** composer packages + 73 npm | 🟢 yes (`composer.lock`) | 🔴 none |
| **Open edX** (`openedx/openedx-platform`) | AGPL-3.0 | **311** Python | 🟢 **yes — 311/311 exactly pinned** | 🔴 none |
| **Canvas LMS** | AGPL-3.0 | **348** npm + gems | 🔴 no lockfile on paths read | 🔴 `COPYRIGHT` is its own AGPL notice |
| **Sakai** | ECL-2.0 | **272** Maven modules | 🟡 Maven resolution | 🔴 none |
| **OpenOLAT** | Apache-2.0 (byte-read, see below) | **183** Maven dependencies | 🟡 Maven resolution | 🔴 none |
| **Gibbon** | GPL-3.0 | **355 resolved** composer packages | 🟢 yes (`composer.lock`) | 🔴 none |
| **OpenEduCat** | LGPL-3 (addon manifest) | **5 Odoo core modules** (`board`, `hr`, `web`, `website`, `contacts`) | n/a — inherits Odoo | 🔴 none |
| **Odoo** (`20.0`) | LGPL-3.0-only | **60** Python | 🔴 unpinned | 🔴 `COPYRIGHT` names zero deps |
| **Tutor** (Open edX distro) | AGPL-3.0 | **28** Python | 🟡 partial | 🔴 none (`dependabot.yml` only) |

🔵 **Two practical consequences for an engagement.**

1. **The licence answer a client's procurement office wants is not in any of these repositories.**
   Not one of the nine discloses the grants of what it bundles, while Moodle and Gibbon alone resolve
   316 and 355 packages. Budget a dependency-grant scan (`scancode-toolkit`, Apache-2.0 — retrieved
   for this purpose at `p531`) as a **named first-week task**, and say so in the proposal rather than
   answering it during an audit.
2. **Rebuildability differs by platform and decides the exit clause.** Open edX, Moodle and Gibbon
   can be handed over as a pinned artefact. Canvas, Odoo and the two flagship tutors cannot, from
   their manifests alone — the lockfile is work the studio does, and it belongs in the estimate —
   scoped as `compose/patterns.md` **P24**.

### OpenOLAT's Apache-2.0, byte-read for the first time (`p905`)

OpenOLAT is this base's main recommendation for a client who needs a **proprietary derivative** of a
full LMS, and its grant had never been read. `master/LICENSE` is **10,982 B**
(`sha256₁₂ 6dbc5b605ed0`) against canonical Apache-2.0 at **11,358 B** (`cfc7749b96f6`).

- 🟢 **All nine numbered sections present and verbatim** — every operative grant (§2 copyright,
  §3 patent, §4 redistribution, §5 contributions) plus §6–§9. **Verdict Apache-2.0 holds; the
  recommendation stands, now on evidence.**
- 🔴 `END OF TERMS AND CONDITIONS` is **absent** and the APPENDIX is removed; two
  **"Additional license statement"** provenance paragraphs (University of Zurich / OLAT Zentrum;
  frentix GmbH / OLAT 7.1) take their place. They grant nothing and restrict nothing.
- 🔴 **Say both of these before a legal review, not after.** A scanner hashing `LICENSE` against
  canonical Apache-2.0 will flag it, GitHub's own detector already reports `NOASSERTION` for exactly
  this reason, and a reviewer meeting the words *"Additional license statement"* inside a licence
  file will stop and ask.

## Restored in `p908`, plus `p907`'s deferred appliance row

🔴 This file carried **280 distinct repository addresses into the `2026-11-17` (`p871`) rewrite and
89 out** ([`delivery-attrition.2026-11-19-p908.tsv`](../evidence/delivery-attrition.2026-11-19-p908.tsv)).
Four of the rows below were named in trending-log promotion claims pointing at
`verticals/solutions.md` and were absent from it. The fifth is the row `p907` measured and explicitly
deferred. Grants byte-read in `p908`.

| Platform | Repo | Licence (byte-read) | ★ | Last push | Where it is strong | AI layering seam |
|---|---|---|---|---|---|---|
| **Apache OpenMeetings** | https://github.com/apache/openmeetings | **Apache-2.0** (`50,907 B`) | 691 | 2026-11-16 | Self-hosted **live classroom**: rooms, whiteboard, polls, recording. Apache-governed, so the licence will not move | 🟢 The **recording** is the seam: transcript → per-student summary → assessment items. Permissive end to end, which no other live-classroom row in this file is. 🔵 SPDX reports `NOASSERTION`; the `50,907 B` payload opens *"Apache License"* |
| **Open TutorAI (CE)** | https://github.com/Open-TutorAi/open-tutor-ai-CE | **BSD-3-Clause** (`1,531 B`, three numbered conditions read) | 119 | 2026-06-26 | Avatar-fronted tutoring platform, Community Edition | Pedagogy and persona are configuration, so the seam is the model backend. 🟡 Last push `2026-06-26` — **five months quiet**; verify maintenance before it anchors a build |
| **ClassroomIO** | https://github.com/classroomio/classroomio | 🔴 **AGPL-3.0** (`34,523 B`) | 1,748 | 2026-11-18 | Customer-training / academy platform — the *corporate* academy shape, not K-12 | 🔴 **AGPL is network copyleft: hosting a derivative as a service triggers the source obligation.** Usable as a deployed platform, unusable as the base of a closed product |
| **FenixEdu Academic** | https://github.com/FenixEdu/fenixedu-academic | 🔴 **LGPL-3.0** (`7,652 B`) | 175 | 🔴 **2023-06-14** | A full open **SIS** — degrees, enrolment, curricular plans — built and run at IST Lisbon (EMEA 🇵🇹) | 🔴 **Three and a half years without a push.** Filed as a *reference data model* for European registrarial structure, **not as a deployment target**. The honest use is reading its domain model, not running it |
| **TurnKey Canvas** | https://github.com/turnkeylinux-apps/canvas | 🔴 **no licence file** (`README.rst` `200`; Canvas itself is AGPL-3.0) | 13 | 2026-11-16 | Pre-built **Canvas LMS appliance** — the fastest path to a running Canvas for a demo or a pilot | 🟡 The appliance *build scripts* carry no grant; the platform it installs is AGPL. Fine for a time-boxed evaluation environment, not a distribution base. **`p907` measured and deferred this row; `p908` read it and files it with the licence gap stated** |

🔵 **Why `terracotta` is in [`repos/foundations.md`](../repos/foundations.md) and not here.** Its
promotion claim named both files. It is an **LTI tool that runs randomised controlled trials inside
someone else's LMS** — it is instrumentation for proving an intervention worked, not a platform a
client would deploy as their learning environment. One row, in the file where an engagement would
actually look for it.

## Who actually buys this in EMEA — measured `p909`

A platform shortlist is only useful if it is pointed at the buyer, and for Europe this base had
named **no** buyer and **no** vendors. `p909` closes that with a denominator and a named cohort.

🔵 **The buyer is national, not the school.** An analysis of **390 public AI-in-education tenders
across 25 countries** finds **central government ran 124** of them; **individual schools, school
trusts and colleges ran 11**. A platform strategy aimed at per-school procurement in Europe is
aimed at roughly 3% of the public money. 🟡 Two independent searches carried this figure; no
primary source could be fetched (see below).

🟢 **The UK is the concrete, named instance — and it ships an open specification.** The **AI
Tutoring Tools Pioneer Programme** (Find a Tender notice `056738-2026`) awarded **8 contracts of
£300,000 each**, £2.4m in total, to **Medly AI, Zero Gravity Tech, Learn Anything Education,
Flint, Pearson Education, ElevenLabs, Eedi and Google UK**. Scope: **Years 9–10**, English, maths,
science and modern foreign languages, aimed at pupils from underrepresented backgrounds. Awards
summer 2026; national availability is a **2027 ambition, not a deadline**.

🔵 **The clause that matters for a studio: the standard co-designed under these contracts is owned
by DSIT/i.AI and will be shared with the wider market.** That is a public tutoring specification
arriving ahead of the products that must meet it — the same position `T9` describes, where the
buyer writes the spec and the integrator who read it first wins. 🟡 **One secondary source reports
six winners from 53 applications** instead of eight awards; the eight-award figure comes from the
tender notice's awardee listing and is the one carried here. The conflict is recorded, not
resolved.

🔴 **Two EMEA programmes that did *not* survive corroboration, and are therefore not platform
rows.** Poland's AI-lab framework (**12,000 kits** — 8,000 primary, 4,000 secondary — six
suppliers, early 2026) and France's **P2IA** (six AI services tested in classrooms since January
2026) each appeared on **one** source and **failed a second, targeted search that returned nothing
on either**. They are open leads, with the failed query recorded so the next pass does not
re-derive the absence.

🔴 **Channel limit, stated plainly.** `WebFetch` failed DNS (`ENOTFOUND`) on every primary source
tried this pass — `lumination.ai`, `algoritmos.uniandes.edu.co`, `acento.com.do` — because those
hosts are outside this session's allowed network domains. **No primary-source channel existed**,
so every figure in this section rests on search snippets and is labelled with how many
independent searches carried it. Nothing here was promoted to a table row.

## National-examination delivery platforms — added `p910`

🔵 **Why these are here and not in `repos/foundations.md`.** They are *applications a client can
stand up*, not libraries to compose with. 🔴 **And the honest framing first: this is the weakest
platform tier in this file.** `p910` measured the national-exam channel across 14 markets and
found **no SIS, no LMS and no exam platform of institutional scale** — 255 live repositories,
63.9% with no `LICENSE` at all, 46% with zero stars (see [`repos/trending.md`](../repos/trending.md)
`p910`). The four rows below are the permissive applications that exist. They are small. Their
value is that the **national exam format is already encoded in them**, which is the part a studio
would otherwise spend a discovery phase reconstructing.

| Platform | Repo | Licence (byte-read `p910`) | ★ · last push | Where it is strong | AI layering seam |
|---|---|---|---|---|---|
| **hanabira.org** | https://github.com/tristcoil/hanabira.org | 🟢 **MIT** — `main/LICENSE`, 1,061 B, `sha256₁₂ fb81a218ce1c` | 436 ★ · 🔴 2025-03-26 | **Self-hostable Japanese *and* Korean learning portal**: vocabulary, grammar, reading, spaced review. Self-hosting is a stated goal, so the deployment story is already written — and it covers **two** national-exam markets (JLPT, TOPIK) in one codebase. | 🟢 The grammar and reading surfaces are where a tutor agent attaches; the review scheduler is where `fsrs4anki`'s FSRS-6 replaces whatever is built in. 🔴 **20 months idle** — treat as a fork base and budget the upgrade, not as a maintained upstream. |
| **cat-snbt-skd** | https://github.com/DeJavi08/cat-snbt-skd | 🟢 **MIT** — `main/LICENSE`, 1,077 B, `sha256₁₂ e6e7edb3e2b8` | 1 ★ · 2026-09-03 | **CAT (Computer-Assisted Test) simulator for Indonesia's SNBT/UTBK *and* the CPNS civil-service SKD** — the two highest-stakes exams in the country, in one delivery engine with the real timing and scoring rules. | 🟢 The item bank is the seam: keep the CAT engine, feed it generated items, and add explanation generation on review. 🟡 1 ★ — adopt the **exam-rule encoding**, expect to rewrite the UI. |
| **DSE-ICT-Master** | https://github.com/SISUBEN/DSE-ICT-Master | 🟢 **MIT** — `main/LICENSE`, 1,065 B, `sha256₁₂ c20159ff7a53` | 1 ★ · 🔴 2025-12-17 | **HKDSE ICT** study platform with paper-structured practice. Hong Kong's co-termed ceiling is 17 repositories; this is the one with a grant and a platform shape. | 🟢 Subject-scoped, so it is a template: the DSE paper structure generalises across subjects once the item source is swapped. |
| **BillyStreet HKDSE Math Mock** | https://github.com/Goodbilly/BillyStreet-HKDSE-Math-Mock-Platform | 🟡 **MIT grant text, 1,059 B, `sha256₁₂ cd35957e7f35` — but the copyright holder line reads `GitHub, Inc.`** (`910-G2`) | 0 ★ · 🔴 2025-11-17 | **HKDSE Mathematics Paper 1 / Paper 2 mock platform** — the exam's two-paper split encoded in the delivery flow. | 🟡 The grant is MIT and the named licensor is a company that does not own the work — an unedited template default. Usable in substance; **expect counsel to stop on it**, so get the holder line corrected upstream before it goes into a client build. |

🔴 **Barred, and named so the absence is not read as coverage.** Jordan's most complete Tawjihi
platform ([`jacoubsmairat/TawjihiQuiz`](https://github.com/jacoubsmairat/TawjihiQuiz) — full
question-bank management) carries **no licence file**, and neither do the two Malaysian KSSM
applications. Singapore's machine-readable **MOE 2021 Primary Mathematics syllabus**
([`davidzbot/singapore-primary-math-syllabus`](https://github.com/davidzbot/singapore-primary-math-syllabus))
is **CC BY-NC 4.0** while GitHub's field says `NOASSERTION` — **NonCommercial, so it is barred from
a paid engagement**, and the syllabus spine must be re-authored (`compose/patterns.md` **P29**).

## National-examination delivery — the CBT tier, added `p911`

🔵 **Why this section exists next to `p910`'s**: `p910` added national-examination *platforms* from
the APAC/EMEA-UK terms. This is the **computer-based-testing delivery** tier from the six markets
`906-G2` named, and it is concentrated almost entirely in **Nigeria** — because Nigeria is the one
market in this pass with a **dated national CBT transition** behind it (WAEC and NECO to full
computer-based WASSCE, objective *and* essay, reported for May–June 2026; `intel/market.md` EMEA).

| Platform | Repo | Licence | ★ | Last push | What it is |
|---|---|---|---|---|---|
| **cbt-app-updates** | https://github.com/Kirchhoff-dev/cbt-app-updates | 🟢 MIT (1,071 B · `9f194f984482`) | 1 | **2026-11-14** | **Offline** JAMB, WAEC and Post-UTME CBT simulator spanning 30+ subjects. 🟢 **Offline is the feature, not a limitation**: the CBT-centre proprietors' own objection to Nigeria's transition is the cost of networked computers in schools, so an offline-capable simulator is aimed at the actual constraint. Pushed five days before this pass. |
| **TTL_CBT** | https://github.com/idrismukthar/TTL_CBT | 🟢 MIT (1,087 B · `30062651a966`) | 1 | 2026-01-09 | School examination platform for **termly internal** exams rather than the national board. 🔵 **The institutional rung below the board** — a school's own assessment cycle is where a studio can deliver without a ministry procurement, and it is the same software shape. |
| **cbt-app** | https://github.com/Toochidennis/cbt-app | 🟢 MIT (1,073 B · `093eb2efcb60`) | 1 | 2026-01-10 | JAMB CBT **desktop** application. 🟡 Carried as the third independent Nigerian implementation of the same requirement — three permissive CBT codebases from one market is a signal about demand, not about quality. |
| **SIMIC** | https://github.com/Dramoscuello/simic | 🟢 Apache-2.0 (11,357 B · `c71d239df917`) | 2 | 2026-07-23 | Open-source platform for **generating, administering and analysing** assessments (Spanish). 🟢 **The most complete LATAM assessment platform this KB has found**, and it covers the full item lifecycle rather than practice delivery alone. 🔵 Pairs with `theteacherbot/ICFES-Exam-Engine` (`agents/top.md`) as generator plus delivery for a Colombian engagement. |

🔴 **What is not here, stated so a later pass does not re-search it:** **no board-grade examination
delivery or marking platform** was found under any licence for WAEC, NECO, KNEC, PAES, EXANI or the
Abitur. The four rows above are **candidate simulators and an assessment platform**; the
national-delivery tier is a **build**, and that is the finding rather than a gap in the search
(`911-G1`).

## The examination boards themselves — measured `p912`, and they are registered and empty

`p911` added the national-examination **delivery** tier above and registered `911-G1`: no
board-grade examination delivery or marking platform exists under any licence. `p912` probed the
boards directly, because a board that publishes its own platform would be the thing to adopt.

| Board | Market | GitHub namespace | Public repositories | What a studio should read into it |
|---|---|---|---|---|
| **WAEC** — West African Examinations Council | Nigeria, Ghana, Sierra Leone, Gambia, Liberia | 🟢 exists | 🔴 **0** | The board running the WASSCE's move to full CBT with essay components in 2026 (`intel/market.md` EMEA) publishes **nothing**. The CBT tier serving it is entirely third-party and permissive — four independent Nigerian implementations in `p911` — so **integration is with a board that has no public interface**. |
| **NECO** — National Examinations Council | Nigeria | 🔴 taken by an unrelated account | 🔴 n/a | `github.com/neco` is a Ruby PBX and ticketing shop last touched in 2010. A probe that trusted the search index would have reported **5 repositories** for Nigeria's examinations council. |
| **NABTEB** — National Business and Technical Examinations Board | Nigeria | 🟢 exists (as `NabTeb`) | 🔴 **0** | The technical-and-vocational board, named here for the first time in this KB: same posture. |
| **JAMB** — Joint Admissions and Matriculation Board | Nigeria | 🟢 exists, indexed | 🔴 **0** | `edunelsonit/Jambora` (Apache-2.0) in `agents/top.md` is a **third party** building for JAMB, not JAMB building. |
| **KNEC** — Kenya National Examinations Council | Kenya | 🟢 exists | 🔴 **0** | Kenya's `KNEC` examination-management system in `p911` was a **live and ungranted third-party Django build**, and the board itself publishes nothing — so the licence-request candidate `p911` named has no upstream to defer to. |
| **CENEVAL** — Centro Nacional de Evaluación para la Educación Superior | Mexico | 🟢 exists | 🔴 **0** | Reinforces `p911`'s Mexico finding from the other side: Mexico's examination supply is one student repository **and** its evaluation centre publishes nothing. |
| **DEMRE** | Chile | 🔴 taken by an unrelated personal account | 🔴 n/a | `github.com/demre` holds a Next.js site template, a movie app and a profile config. Chile's PAES supply is `matmiidu/paes-ensayos` (MIT) and nothing from the body that sets the examination. |
| **UNEB** — Uganda National Examinations Board | Uganda | 🟡 ambiguous | 🔴 1, idle since 2014 | A single `0 ★` `unhackthon` repository. Treat as unclaimed. |

🟢 **The commercial reading is the opposite of discouraging.** Every board in the table has either
claimed its namespace or had it claimed by someone else, and **not one has published a platform,
an API client, a question schema or a results format**. There is no incumbent open artefact to
displace and no board-published interface to conform to, which means the integration surface is
defined by whoever builds it first — and `compose/patterns.md` **`P30`** scopes that build.
🔴 **The risk is the mirror image**: with no published schema, every CBT implementation in `p911`'s
Nigerian cluster is integrating against an **undocumented** target, so portability between boards
cannot be assumed and should be priced. Evidence:
`evidence/p912-board-owner-channel.2026-11-19-p912.tsv`.


### 🔴 Re-measured in `p913` with a committed classifier — and four of the eight cells above were not supportable

`912-G2` registered the instrument this section needed: an owner's affiliation must be adjudicated
from its repositories' **payloads**, never from its name matching an acronym (`912-F4`). It is now
committed as **`ingest/p913-owner-affiliation.sh`** and it carries a negative control
(`zzqqxxnotanowner913zz`, a name chosen not to exist) that runs on **every** invocation; the script
refuses to emit if the control does not behave. Running it produced a correction to the table above.

🔴 **The owner channel has three states, not two, and `p912` published the wrong one for four
boards.** `gh api search/repositories -f q="user:X"` answers:

| Channel response | What it means | Reachable? |
|---|---|---|
| **HTTP 422** `Validation Failed` — *"the listed users and repositories cannot be searched either because the resources do not exist **or** you do not have permission to view them"* | X does **not** exist, or is invisible to this token. **Not** "registered and empty." | 🟢 yes — p913's negative control returns exactly this |
| **HTTP 200**, `total_count` **0** | X **exists** and publishes nothing. *This* is "registered and empty." | 🟢 yes — `jamb`, `moe-ethiopia` |
| **HTTP 200**, `total_count` **N>0** | X exists and is occupied → adjudicate the payloads | 🟢 yes — `moodle` (12), `neco` (5), `demre` (4) |

| Board | `p912` published | `p913` measured | Verdict |
|---|---|---|---|
| **WAEC** | 🟢 exists / 0 repositories | **HTTP 422** | 🔴 `ABSENT-OR-INVISIBLE` — **not established as registered** |
| **NABTEB** (`NabTeb`) | 🟢 exists / 0 repositories | **HTTP 422** | 🔴 `ABSENT-OR-INVISIBLE` |
| **KNEC** | 🟢 exists / 0 repositories | **HTTP 422** | 🔴 `ABSENT-OR-INVISIBLE` |
| **CENEVAL** | 🟢 exists / 0 repositories | **HTTP 422** | 🔴 `ABSENT-OR-INVISIBLE` |
| **JAMB** | 🟢 exists, indexed / 0 | **HTTP 200, `total_count` 0** | 🟢 `REGISTERED-EMPTY` — **the only board whose "registered and empty" cell was supportable** |
| **NECO** | taken by an unrelated account | **HTTP 200 / 5**, 2 READMEs read, **0 of 10** domain terms in metadata or prose | 🟢 `OCCUPIED-UNRELATED` — confirms `p912` |
| **DEMRE** | taken by an unrelated account | **HTTP 200 / 4**, 2 READMEs read, **0 of 10** | 🟢 `OCCUPIED-UNRELATED` — confirms `p912` |
| **UNEB** | 🟡 ambiguous, 1 idle repository | **HTTP 200 / 1**, **0 READMEs readable**, 0 of 10 | 🟡 `OCCUPIED-UNRELATED`, **on metadata alone** — the instrument reports `readmes_read=0`, so the absence claim here rests on the description and topics only |
| `moe-ethiopia` (ministry, not a board) | 0 repositories (`intel/market.md`) | **HTTP 200 / 0** | 🟢 `REGISTERED-EMPTY` — `p912`'s cell was right |
| `NEAEA` (Ethiopia's examinations agency) | "does not resolve as an owner at all" | **HTTP 422** | 🟢 confirms `p912` |

🔴 **How this got published, and it is the part worth carrying.** `p912` **used the distinction
correctly in one file and conflated it in another, in the same pass.** `intel/market.md` says
*"`moe-ethiopia` resolves on the search index with `0` repositories; `NEAEA` does not resolve as an
owner at all"* — that is exactly the 200/0-versus-422 distinction, applied correctly. The table
above then recorded `🟢 exists / 0 public repositories` for four boards that return **422**.
🔵 `gate-shelf-consistency` could not catch it because that gate compares **licence** cells across
files; **owner-state cells are not gated at all**. Registered as `913-G2`.

🔴 **`p912`'s named second owner channel does not work here, and it fails in the worst possible
shape.** `p912` records *"plain HTTPS GET of the GitHub profile page"* as a second, independent
owner channel. In this environment the session's git proxy answers **every** `github.com/<anything>`
with an identical **403** JSON body (`"sessions are bound to their configured repositories"`), 249
bytes — for `moodle`, for `waec`, and for the nonexistent control alike. 🔵 **A channel that returns
one answer for every input corroborates nothing**, and because the body is well-formed JSON rather
than a transport error it reads like a result. It must not be cited as a second channel in this base
again.

🟢 **The commercial reading changes, and in a direction that matters.** `p912` concluded that *"every
board in the table has either claimed its namespace or had it claimed by someone else."* Measured:
**three** are demonstrably occupied by unrelated parties, **one** (JAMB) is demonstrably registered
and empty, and **four are not established as registered at all.** Two consequences:
🔴 **An unregistered namespace for a national examination board is an impersonation exposure**, not a
neutral fact — a studio building a board-facing integration should expect to advise the board to
claim it, and should not publish under a name that implies board endorsement. 🔵 **And there is no
intent signal to read**: "the board registered a namespace" was the closest thing this section had
to evidence of institutional intent, and for four of the five it is withdrawn. The conclusion that
**there is no incumbent open artefact to displace** survives intact and is now better supported, not
worse. Evidence: `evidence/p913-owner-affiliation.2026-11-19-p913.tsv`,
`evidence/p913-owner-ethiopia.2026-11-19-p913.tsv`.

## Commercial-LMS seams — re-measured `p914`, and the D2L seam is closed

The table earlier in this file records, for each commercial LMS a client may already run, the open
bridge that exists against it. One of those rows was the weakest in the file: D2L Brightspace's
only bridge was `GuanmingQiao/POLITEMALL-MCP`, a **two-system, Singapore-specific** adapter.

| Platform | Open source? | Seam as at `p914` |
|---|---|---|
| **D2L Brightspace** | 🔴 No — commercial | 🟢 **Closed this pass.** https://github.com/RohanMuppa/brightspace-mcp-server — **MIT** (`main/LICENSE`, 1,068 B, `sha256₁₂ 047079fbd491`), 68 ★, pushed 2026-11-18, TypeScript. States it works with **any** school rather than one tenant. `POLITEMALL-MCP` remains the better reference for a *Singapore* engagement because it already speaks to two national systems. |
| **Canvas** | 🔴 No — commercial for the hosted product; `instructure/canvas-lms` is AGPL-3.0 | Unchanged — `vishalsachdev/canvas-mcp` (MIT, 334 ★) and `boyuchengz/canvas-mcp` (MIT, 118 ★), plus `SonAIengine/ku-portal-mcp` (MIT, 13 ★, added `p914`) which speaks Canvas **and** a Korean campus portal in one server |
| **Blackboard (Ultra / classic)** | 🔴 No — commercial | Unchanged — `andrsnrua/universidad-pacifico-mcp` (ISC), `bolgerru/blackboard-mcp` |
| **PowerSchool** (SIS) | 🔴 No — commercial | Unchanged — `cculb/schoolconnect` (MIT), parent-facing only |
| **Moodle** (self-hosted, GPL-3.0 — listed here for the plugin estate, not as a commercial product) | 🟢 Yes | 🆕 `Berserk-hub150/moodle-ai-skill-navigator` (**GPL-3.0**, 279 ★) and `saylordotorg/moodle-local_ai_course_assistant` (**GPL-3.0**, 21 ★, published by Saylor Academy). Both copyleft — correct for a Moodle plugin, and both therefore outside a closed deliverable. `SaadRahman01/claude-moodle-dev` (**MIT**, 42 ★) is the permissive piece: it is the *development* toolkit, not the shipped plugin |

🔵 **Why the D2L row matters more than its star count.** Brightspace is a North American and
Canadian higher-ed incumbent, and this base's North America leg has repeatedly recorded the buyer
as policy-driven and procurement-gated. A tenant-agnostic MIT bridge is the difference between
"we can demo against your LMS" and "we can demo against a Singapore polytechnic's". It is 68 ★ and
nine days from its last push — treat it as a credible starting point to be read, not as a
dependency to pin. See `compose/patterns.md` `P33`.

## Honest gaps

- **Unlicensed content corpora are the biggest trap in this category (added p891).** The largest
  education-tagged repo on GitHub, https://github.com/TapXWorld/ChinaTextbook (**84,728 ★**), has
  **no `LICENSE` or `COPYING` file on either `main` or `master`** — all four candidate paths
  return 404, and the GitHub API reports licence `NONE`. No licence means **all rights
  reserved**, and the contents are third-party-copyright PDF textbooks rather than code. It is
  larger than every platform in this file and usable in none of them. **Byte-read the licence of
  any content asset before it reaches a client deck** — curriculum corpora are where star count
  and usability diverge most sharply.

  **A second region, measured p895.** The highest-star African education repo this KB has found is
  https://github.com/Seunope/aloc-endpoints (**223 ★**, pushed 2026-11-17), a Nigerian
  **past-questions API** — self-described *"20,000 past questions API end points for POST-UTME,
  UTME, WASSCE, NECO"* — and it has **no licence on any of 8 candidate paths**
  (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` × `main`/`master`, all 404). Same shape as
  `ChinaTextbook` on a different continent: the most useful-looking asset in the category is the
  least usable, and it carries **third-party exam copyright on top of the licence absence**.
  **The rule generalises: for content, byte-read the licence *and* ask who owns the payload.**

- **No open-source education CRM — restated p899 with the measurement that sharpens it.**
  Student-recruitment and alumni CRM remains proprietary (Salesforce Education Cloud, Ellucian),
  and a studio can either build on a general open CRM or accept proprietary integration.
  🔴 **But the nearest thing is no longer "not found" — it is found and barred, which is a
  different fact.** https://github.com/canyongbs/advisingapp ("Advising App" by Canyon GBS) is an
  **AI conversational assistant for student advising and student success**, 339 ★, pushed
  2026-11-18 — exactly the registrarial/advising agent tier this file records as missing. It is
  **Elastic License 2.0**, byte-read p899 (`LICENSE@main`, 3,860 B, `sha256₁₂ 48255018b41f`):
  **source-available, not open source**, and it specifically forbids providing the software to
  third parties as a managed service — a direct description of what a studio does for a client.
  GitHub's SPDX field reports only `NOASSERTION`. **The category has an incumbent; it is just not
  one Globant can build on.** Recorded in `intel/measured-unusable.md`.
- **No open-source proctoring product worth deploying.** `openedx/edx-proctoring` is an
  integration shim, and the standalone candidates in earlier passes of this KB were
  student projects. Given that exam monitoring is EU AI Act Annex III high-risk, the absence
  of a credible, auditable open option is itself a market signal.
- **No open-source financial-aid or admissions-decisioning platform.** Also Annex III
  high-risk in the EU. Same signal, stronger.
