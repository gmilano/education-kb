---
industry: education
region: Global
updated: 2026-10-11
---

# Education — AI agents shelf

**Pass 134, 2026-10-11.** 🔴 **This pass did not add a connector to the tier this shelf is built
around — it found the tier that makes most of that one unshippable, and it has been missing from
this KB the whole time.** Every row in the 36-row portal tier below authenticates by holding a
student's password against a platform that never sanctioned it, and this page has correctly called
that a tier-wide blocker for three passes. 🟢 **The sanctioned alternative is not a research
project: it is a mature, permissive, actively-maintained standards stack — `ltijs` (Apache-2.0,
**373★**, pushed 2026-10-06), `pylti1.3` (MIT, 138★), OneRoster SDKs owned by **Google** and the
**Ed-Fi Alliance**, and an Ed-Fi line maintained by a **US state department of education**.** This
shelf carried exactly **one** row from that world (`instructure/ims-lti`, MIT, 203★, in
`repos/foundations.md`) and never connected it to the blocker.

🔴 **And the one thing that stack is missing is the thing this KB exists to find.** The bridge from
an *agent* to a *sanctioned standard* is **one repo** — `DavidLMS/learnmcp-xapi` (MIT, 15★) — and
the only Ed-Fi MCP server in existence, `cdweaver1992/edfi-mcp-server`, is **an empty repository**:
`size: 0`, HTTP 404 on all 15 probes (5 candidate entry points × `HEAD`/`main`/`master`), created
and pushed in the same second.
🟢 **That is the sharpest engagement-shaped finding on this page: the standards are built, the
agents are built, and almost nobody has wired the two together.**

🔵 **One method note, since it cost this KB the whole tier.** The probe that found it was
`grade passback`, and then `lti 1.3 advantage`, `oneroster` and `ltijs` — **the professional
register of the people who do this work for a living.** Not the category term (`SIS`), not the
capability term (`timetable`, which found p132's 21 rows), and not a national platform noun
(which found p133's 15). It is a **fourth, distinct vocabulary**, and it is the one that reaches
the institutional and vendor-owned supply. See clause 5 at the foot of this page.


**Pass 132, 2026-10-11.** p131's rows retained; 🔴 **an entire tier is ADDED below — the one this
KB had declared its largest hole.** *"No agent targeting a student information system"* is refuted
by **21 rows** (see `README.md` → Pass 132, `P132-A`). p131's own rows were verified hours earlier
in the same date window and are **carried forward unchanged** rather than re-measured; everything
new on this page was measured this pass and is recorded with its instrument in
`evidence/verified-repos.2026-10-11-p132.tsv`. Rows are ordered by how useful they are to a studio
engagement, not by stars.

🔵 **One method note, because it is the whole finding.** The probe that found the new tier was
`timetable timetabling MCP in:name,description` — **not** any query containing the words *student
information system*. The builders name repos after the platform they connect to, never after the
category, so the analyst's vocabulary cannot reach them at any star threshold.

## How these rows were verified (and one instrument that does not work here)

- **Working instrument:** GitHub repo search via the session's GitHub tool. It returns the
  authoritative `license.spdx_id`, `stargazers_count`, `pushed_at`, `archived` and `fork` fields.
- **Working instrument:** fetching the rendered `github.com` repository page, used to confirm
  licence wording, releases and fork parentage.
- **BROKEN instrument — do not trust it in this environment:** `curl -sI https://github.com/<repo>`
  returns **HTTP 403 for every URL**, real or not. A control request for the deliberately
  nonexistent `zzz-not-a-real-org-9981/zzz-not-real-9981` also returned 403. **A 403 here is not
  evidence of anything**, so `curl -sI` cannot be used to tell a real repo from a typo. The KB's
  standing instruction to verify with `curl -sI` does not work from this runner; use repo search.
- The GitHub REST API for arbitrary repositories (`api.github.com/repos/...`) is blocked for this
  session, as is the `gh` CLI search path. Repo search is the only endpoint that reaches repos
  outside the session's own scope. 🔵 **p132 adds:** the session's GitHub *file-read* tool is scoped
  to this KB's own repositories and returns `Access denied` for any third party, so a licence
  **payload** must be read over the fetch lane at
  `raw.githubusercontent.com/<owner>/<repo>/<branch>/LICENSE`. **That lane works** and produced two
  licence corrections this pass.
- 🔴 **BROKEN QUERY FORM — added by p132: `OR` is not honoured as a boolean in repo search.** It
  does not union two narrow sets; it collapses into a broad match.
  `oneroster OR ed-fi MCP agent in:name,description` returned **69 812** results (the global
  MCP-agent population) and `swahili OR yoruba OR amharic education in:name,description` returned
  **248 136** (the global `education` population). 🔴 **So a count from this instrument is evidence
  of nothing until the query form is checked — a zero, a 69 812 and a 248 136 can all be
  artefacts of form rather than measurements of a field.**

## Agents

| agent | repo | licence | stars | last push | region of origin | what it actually does |
|---|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** | **41 136** | 2026-10-08 | APAC (HKUDS, Hong Kong) | Lifelong personalised tutoring agent. By far the largest education-specific agent in open source, and permissively licensed — the default starting point for a tutoring engagement. |
| **educhain** | [`satvik314/educhain`](https://github.com/satvik314/educhain) | **MIT** | 388 | 2026-10-09 | unplaced | Python package that generates educational content (lesson plans, question banks, MCQs) with an LLM. Useful as a content-generation library inside a larger system. **Caveat:** the repo publishes no GitHub releases and its README's own version history stops at v0.3.13 (October 2024). |
| **canvas-mcp** | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | 288 | 2026-10-11 | unplaced | Canvas LMS MCP server — courses, assignments, submissions, rubrics, quizzes, grading — exposed as agent tools. **The canonical repo of a fork swarm** (see the fork warning below). |
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | **MIT** | 264 | 2026-10-11 | North America (CAHLR lab, UC Berkeley) | Intelligent tutoring system with Bayesian Knowledge Tracing over a ReactJS + Firebase stack. The reference implementation when a client wants *auditable* mastery estimates rather than an LLM's opinion. |
| **moodle-ai-skill-navigator** | [`Berserk-hub150/moodle-ai-skill-navigator`](https://github.com/Berserk-hub150/moodle-ai-skill-navigator) | GPL-3.0 | 222 | 2026-09-29 | unplaced | Moodle plugin adding AI tutoring, quiz generation, mind maps and RAG over course materials. The most-starred *in-Moodle* AI plugin found. GPL-3.0 — copyleft, consistent with Moodle itself. |
| **GenMentor** | [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | 133 | 2026-10-08 | unplaced | LLM multi-agent framework for goal-oriented learning in an ITS; the code behind a WWW 2025 industry-track paper. CC0 is a public-domain dedication — usable, but it carries no patent grant, unlike Apache-2.0. |
| **tutor-mcp** | [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** | 44 | 2026-10-10 | unplaced | Go MCP server that gives any LLM durable learner state: BKT mastery, review scheduling, session memory, misconceptions, and auditable pedagogical decisions. LMS-agnostic, so it pairs with any connector below. Self-described alpha. |
| **claude-moodle-dev** | [`SaadRahman01/claude-moodle-dev`](https://github.com/SaadRahman01/claude-moodle-dev) | **MIT** | 39 | 2026-06-22 | unplaced | Not a learner-facing agent: a toolkit of agent skills for *building* Moodle plugins (XMLDB, Hooks API, PHPUnit, Behat, privacy/GDPR, accessibility). Relevant to delivery velocity on a Moodle engagement. |
| **ideas** | [`ideas-edu/ideas`](https://github.com/ideas-edu/ideas) | **Apache-2.0** | 28 | 2026-09-05 | EMEA (Utrecht University, NL) | Feedback services for intelligent tutoring systems — domain reasoners that produce step-level hints for maths/logic exercises. Haskell. Narrow, old-school, and genuinely rigorous where LLM feedback is unacceptable. |
| **canvas-lms-mcp** | [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | **MIT** | 9 | 2026-10-10 | unplaced | Second, independent Canvas MCP implementation (read courses/assignments/submissions/rubrics, grade and comment). Small, but a useful cross-check against the canonical one. |
| **campus-cli** | [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) | ISC | 11 | 2026-10-11 | **LATAM (Peru)** | CLI + MCP server over **Blackboard Learn** — the only Blackboard connector in this KB, and the only LATAM-origin education agent found. Targets UPC's Aula Virtual (Universidad Peruana de Ciencias Aplicadas); Canvas and Moodle are on its roadmap. ISC is permissive (BSD-equivalent). |
| **openedx-mcp** | [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | AGPL-3.0 | 2 | 2026-08-28 | unplaced | Open edX admin/authoring operations as an MCP facade, reusing the platform's own `is_staff`/`is_superuser` checks per request. **Experimental — 2 stars.** Listed because it is the only Open edX MCP path found, not because it is ready. |

### Student-information-system agents — the tier this KB called its largest hole

🔴 **This KB carried *"no agent targeting a student information system"* for several passes and
promoted it to "the largest genuine hole on this shelf" in p131. It is refuted.** There are at
least **twenty-one** rows, listed below and in
`evidence/verified-repos.2026-10-11-p132.tsv`.

🔵 **Why no previous pass found them: the field is named after platforms, not after the category.**
Searches for *"student information system"*, *"school management"* and *"SIS"* cannot reach repos
called `librus-mcp`, `edupage-mcp`, `mcp-pronotes`, `iserv-mcp`, `sisu-mcp`, `soongpt-plugin`,
`vtop-bhopal-mcp`, `qldt-hanu-mcp`, `mcgill-vsb-mcp` or `nycu` — none of which contain the
analyst's words. The probe that worked was `timetable timetabling MCP in:name,description`, because
**timetable access is the one capability every one of them implements.**

🔴 **Read the shape of this tier before recommending any of it.** These are overwhelmingly
*one-person connectors to the author's own institution*, created within the last six months, at 0–10
stars. The licences are good and the maturity is near zero. **Nothing here is a product; the value
is that the integration work against ten national platforms has already been scouted.**

🔴 **Qualified by p133 — the sentence above was true of the 21 rows p132 had, and the tier is
bigger than that.** Running the LATAM and ANZ probes added **15 rows**, and they break three of
p132's generalisations about this shelf:

| p132's claim about the tier | what p133's rows show |
|---|---|
| *"the builders are students and parents… **no procurement story whatsoever**"* | 🔴 **4 rows automate a *teacher's* obligation**, and one is org-owned with a product homepage — see the staff-facing subsection below |
| *"**~80% MIT**"* | 🔴 **The LATAM slice is 42% MIT** (5 of 12), with 3 unlicensed, 2 GPL-3.0 and 1 AGPL-3.0. Staff-side builders in this region reach for copyleft |
| *"nothing here is a product"* | 🟡 **One exception:** `BetterSEQTA` ships two MIT products (40★ + 16★) with a Chrome Web Store listing, an org, 25 forks and a push this week |

🔵 **The honest generalisation is the one p132 itself reached for: a claim about "every tier
measured" is only a claim about the tiers you queried — and that now applies to p132's own tier
description.**

#### Generic / platform-independent — the forkable ones

| agent | repo | licence | stars | region | what it actually does |
|---|---|---|---|---|---|
| **classroom-mcp** | [`sandraschi/classroom-mcp`](https://github.com/sandraschi/classroom-mcp) | **MIT** | 1 | unplaced | 🟢 **Architecturally the most reusable row in this tier, and the only one not bound to an institution.** Standalone (SQLite, no external DB): students and classes, assignments with per-student score/time/mastery tracking, courses and sequenced modules with learning objectives, courseware, **teaching-agent roles (lecturer, tutor, grader, designer)**, and AI curriculum generation against **CEFR/JLPT** frameworks. ~42 MCP tools plus a REST API. 🔴 **1 star.** Treat as a reference design to read, not a dependency to adopt. |
| **mcp-student-records** | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | 🟢 **Apache-2.0** (payload-read) | 1 | North America | Full SIS surface in **Rust** — students, courses, enrolment, grades and rubrics, attendance, guardians, transcripts, analytics — with **FERPA access logging** built in. 🟢 **The only organisation-owned row in the tier** (holder: *"Copyright 2026 Zavora AI"*), and the only one that treats the audit trail as a feature. 🔵 **Licence corrected this pass:** GitHub's API says `NOASSERTION`; the payload is Apache-2.0 carried as the **~745-byte notice block** without the licence body, which is what defeats GitHub's matcher. |
| **sis-demo** | [`barneslardo/sis-demo`](https://github.com/barneslardo/sis-demo) | 🔴 **no licence field** | 1 | unplaced | The **identity and rostering** angle nothing else covers: Okta OIDC/SAML, OAuth 2.0 API, **SCIM** provisioning, and an MCP server over the top. Unusable as published, but the only worked example of agent access governed by enterprise SSO rather than a scraped student password. |
| **AI-Based-Timetable-Generation-System** | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | 🟢 **The administrative-automation agent this KB said did not exist.** Generates conflict-free academic timetables under **India's NEP 2020** — electives, faculty availability, courses, rooms, balanced workloads — with scenario simulation, manual edits, exports and a natural-language interface over MCP. Optimisation, not chat. |

#### Institution- and nation-bound portal connectors

These bind to a specific national school platform or university portal. **Region is stated
evidence** — a named institution, a national system, a country-coded homepage — not an inference.

| agent | repo | licence | stars | region | platform it connects to |
|---|---|---|---|---|---|
| **BetterSEQTA+** | [`BetterSEQTA/BetterSEQTA-Plus`](https://github.com/BetterSEQTA/BetterSEQTA-Plus) | **MIT** | **40** | **APAC (Australia)** | 🟢 **The largest and only product-shaped row in this tier.** **SEQTA Learn**, the Australian school platform: a Chrome/Firefox extension (published on the Chrome Web Store) rewriting the SEQTA interface — timetable, assessments, dark mode, redesign. **Org-owned** (`BetterSEQTA`), **25 forks**, pushed **2026-10-06**. Added p133 (`ACTION BF`). |
| **sigaa-calendar** | [`Agso-o/sigaa-calendar`](https://github.com/Agso-o/sigaa-calendar) | 🟡 **GPL-3.0** | **20** | **LATAM (Brazil)** | **SIGAA**, the SIS of Brazil's federal universities: extracts deadlines and timetables straight into Google Tasks/Calendar. Go. Pushed **2026-10-09**. 🟡 Copyleft — read before forking. Added p133. |
| **sigaa-caiu** | [`trindadetiago/sigaa-caiu`](https://github.com/trindadetiago/sigaa-caiu) | **MIT** | 19 | **LATAM (Brazil)** | **SIGAA** — TypeScript. Added p133. |
| **siu-guarani-promedio** | [`juliancasaburi/siu-guarani-promedio-extension`](https://github.com/juliancasaburi/siu-guarani-promedio-extension) | **MIT** | 17 | **LATAM (Argentina)** | **SIU-Guaraní**, the SIS of the Argentine university consortium: grade-average visualisation over academic history. Chromium/Firefox extension. Added p133. |
| **SigaaUI** | [`RubsNeto/SigaaUI`](https://github.com/RubsNeto/SigaaUI) | **MIT** | 16 | **LATAM (Brazil)** | **SIGAA** — open-source extension modernising *Portal do Discente*, grades and enrolment screens. Added p133. |
| **DesQTA** | [`BetterSEQTA/DesQTA`](https://github.com/BetterSEQTA/DesQTA) | **MIT** | 16 | **APAC (Australia)** | **SEQTA** ported to a native desktop app (Svelte). Same org as `BetterSEQTA-Plus` — 🟢 **the only two-product line in the tier.** Added p133. |
| **QuantoFalta** | [`MatheusMach/QuantoFalta`](https://github.com/MatheusMach/QuantoFalta) | 🔴 **no licence** | 9 | **LATAM (Brazil)** | **SIGAA** absence counter per subject. Created **and** pushed 2026-10-08 — three days old at this pass. Added p133. |
| **siu-guarani** (seats) | [`despedite/siu-guarani`](https://github.com/despedite/siu-guarani) | 🟡 **GPL-3.0** | 8 | **LATAM (Argentina)** | **SIU-Guaraní** — scraper that watches for free course seats. Added p133. |
| **docker-guarani** | [`SIU-Toba/docker-guarani`](https://github.com/SIU-Toba/docker-guarani) | 🔴 **no licence** | 4 | **LATAM (Argentina)** | 🟢 **The only row in this tier owned by the SIS vendor itself** — `SIU-Toba` is the Argentine university consortium's own org. Docker containers for Guaraní. 🔴 **Dormant since 2017 and unlicensed**, so not a usable counterparty today — but it is the named counterparty `P8`/`P9` need. Added p133. |
| **Parent-Portal (KAMAR)** | [`st22209/Parent-Portal`](https://github.com/st22209/Parent-Portal) | **MIT** | 2 | **APAC (New Zealand)** | **KAMAR**, the New Zealand school SIS, via a CLI (PyPI `kmrpp`). 🔴 **ARCHIVED, and the README states the cause: *"[DEPRECATED AFTER KAMAR API CHANGE]"*.** The tier's only worked example of what a vendor-side API change does to an unsanctioned connector. Added p133 (`ACTION BF`). |
| **academic-tracker-mcp** | [`joojdev/academic-tracker-mcp`](https://github.com/joojdev/academic-tracker-mcp) | **MIT** | 0 | **LATAM (Brazil)** | **SUAP** (*Sistema Unificado de Administração Pública*), the SIS of Brazil's federal institute network — MCP server over the author's own academic record. 🟢 **The first LATAM row this KB ever placed in this tier.** Added p133. |
| **suap-mcp** | [`frjunioalves/suap-mcp`](https://github.com/frjunioalves/suap-mcp) | 🔴 **no licence field** | 0 | **LATAM (Brazil)** | **SUAP** — independent second Python implementation. 🔵 Two independent SUAP connectors is the same demand signal EduPage gives in EMEA. Added p133. |
| **librus-mcp** | [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | 🟡 **MIT (2.x)**; `legacy_reference/` is **GPL-3.0-only** | **10** | **EMEA (Poland)** | **Librus Synergia**, the dominant Polish school platform: grades, messages, attendance, homework, timetables, announcements. 🔴 **Mixed-licence repo — a fork must exclude `legacy_reference/` or inherit GPL-3.0.** Unofficial, not affiliated with Librus; no 2FA support. |
| **DAU-buddy** | [`Piyushtanwani/DAU-buddy`](https://github.com/Piyushtanwani/DAU-buddy) | 🔴 **no licence** | 7 | **APAC (India)** | Dhirubhai Ambani University (DA-IICT) — timetables, library catalogue, faculty directory. Second-largest row of the tier and unusable as published. |
| **vtop-bhopal-mcp** | [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) | **Apache-2.0** | 4 | **APAC (India)** | VIT Bhopal's **VTOP** portal: attendance, marks, timetable, exams, grades, plus bunk/OD calculators. Created 2026-10-02 — nine days old at this pass. |
| **soongpt-plugin** | [`yourssu/soongpt-plugin`](https://github.com/yourssu/soongpt-plugin) | **MIT** | 3 | **APAC (South Korea)** | Soongsil University **uSaint** via `rusaint`: course search, timetable planning and **graduation-requirement checking** — the only row that reasons about degree progress. Org-owned (`yourssu`). |
| **edupage-mcp** | [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | **MIT** | 3 | **EMEA (Slovakia)** | **EduPage**, the Slovak/Czech school platform. The most complete connector of the tier: timetables, grades, homework, daily summary, **meal ordering**, multi-school discovery, role-aware student switching and **2FA**. |
| **ddl-killer** | [`edwyj/ddl-killer`](https://github.com/edwyj/ddl-killer) | 🔴 **AGPL-3.0** (payload-read, p133) | 3 | **APAC (China)** | Student planner for Chinese universities — timetables, tasks and deadlines in one schedule, AI-assisted scheduling, MCP access, Web/Android sync. Created **2026-10-10**. 🔴 **Licence measured by p133 and it is the most restrictive in the tier: the payload is the full AGPL-3.0 text, and the only copyright line in it is the Free Software Foundation's — a `DOCUMENT-TEXT` holder with no program-specific licensor.** Network copyleft on a student-data connector: do not fork into client work. |
| **mcgill-vsb-mcp** | [`luca-dupont2/mcgill-vsb-mcp`](https://github.com/luca-dupont2/mcgill-vsb-mcp) | **MIT** | 2 | **North America (Canada)** | McGill **VSB**: timetable data, conflict checks and schedule generation *without browser automation* — an API path rather than a scraper. |
| **edupage-mcp** (second) | [`mhlavac/edupage-mcp`](https://github.com/mhlavac/edupage-mcp) | **MIT** | 1 | **EMEA (Slovakia)** | Independent second EduPage implementation — a useful cross-check, and evidence that EduPage demand is real rather than one person's itch. |
| **mcp-pronotes** | [`HAL-XP/mcp-pronotes`](https://github.com/HAL-XP/mcp-pronotes) | **MIT** | 1 | **EMEA (France)** | **Pronote**, the dominant French school platform: grades, timetables, homework, absences. |
| **ibu-mcp** | [`Haris0059/ibu-mcp`](https://github.com/Haris0059/ibu-mcp) | 🟢 **MIT** (payload-read) | 1 | **EMEA (Bosnia)** | International Burch University: grades, attendance, exams, tuition, notifications. Region is hard evidence — homepage `mine.ibu.edu.ba`, topic `bosnia`. Holder *"Haris Skeledzija"*. |
| **sisu-mcp** | [`ink-waffle/sisu-mcp`](https://github.com/ink-waffle/sisu-mcp) | 🔴 **no licence field** | 1 | **EMEA (Finland)** | **Sisu (Funidata)**, the Finnish higher-education SIS: attainments, enrolments, timetables, plans. 🔴 **Written for *any* Sisu deployment rather than one university — the broadest reach of the bound connectors, and unusable as published.** Same owner as `ink-waffle/moodle-mcp`, also unlicensed and already flagged below: **this author ships unlicensed education connectors as a pattern.** |
| **nycu** | [`zyx1121/nycu`](https://github.com/zyx1121/nycu) | **MIT** | 1 | **APAC (Taiwan)** | National Yang Ming Chiao Tung University portal, E3 LMS, timetable and attendance, packaged as a Claude Code / Codex plugin. |
| **UofT-MCP** | [`SleepyPandas/UofT-MCP`](https://github.com/SleepyPandas/UofT-MCP) | **MIT** | 1 | **North America (Canada)** | University of Toronto Timetable Builder API. |
| **qldt-hanu-mcp** | [`qxbao/qldt-hanu-mcp`](https://github.com/qxbao/qldt-hanu-mcp) | **GPL-2.0** | 1 | **APAC (Vietnam)** | **QLDT**, Hanoi University's student management system. 🔴 **The only copyleft row in the tier** — and note the jurisdiction: Vietnam's **Decision 33/2026/QD-TTg names education, including automated assessment and behavioural monitoring, as high-risk** (`intel/market.md` → APAC). |
| **ntnu-mcp** | [`MartinSA04/ntnu-mcp`](https://github.com/MartinSA04/ntnu-mcp) | **MIT** | 0 | **EMEA (Norway)** | NTNU course data on Cloudflare Workers: catalogue search, schedules, **grade statistics**, course comparison, conflict checks. The only remote/edge-deployed row. |
| **iserv-mcp** | [`chenning42/iserv-mcp`](https://github.com/chenning42/iserv-mcp) | **MIT** | 0 | **EMEA (Germany)** | **IServ**, a German school platform: parent letters, timetables, **sick notes**. 🔵 Note the user it serves — a *parent*, not a student or teacher. The only row on that surface. |
| **uoft-quercus-mcp** | [`skhdemo/uoft-quercus-mcp`](https://github.com/skhdemo/uoft-quercus-mcp) | **MIT** | 0 | **North America (Canada)** | University of Toronto **Quercus** — a Canvas deployment — plus Timetable Builder tools. Belongs to the Canvas connector family as much as to this tier. |
| **vsuet-timetable-api-mcp** | [`fakelag28/vsuet-timetable-api-mcp`](https://github.com/fakelag28/vsuet-timetable-api-mcp) | **MIT** | 0 | **EMEA (Russia)** | VSUET (ВГУИТ) timetable client library plus MCP server. |

#### 🟢 Staff- and teacher-facing administrative agents *(new, p133 — the user p132's tier did not have)*

🔴 **Every row above serves a student or a parent. These four serve the person being paid.** They
turned up only in the LATAM and ANZ probes, which is why p132 — whose 21 rows were EMEA/APAC/NA —
concluded the tier had *"no procurement story whatsoever."*

| agent | repo | licence | stars | region | whose work it removes |
|---|---|---|---|---|---|
| **expeditto** | [`fabrica-de-inovacao/expeditto`](https://github.com/fabrica-de-inovacao/expeditto) | 🟡 **AGPL-3.0** | 1 | **LATAM (Brazil, IFMA)** | 🟢 **The strongest signal in this subsection.** Drafts a lecturer's **RIT** — the workload report Brazilian federal institutes require — from **SUAP**, as a CLI *and* an MCP server. **Org-owned** (*Fábrica de Inovação*), product homepage, pushed **2026-10-08**. Tagline: *"seu segundo expediente, resolvido"* — your second shift, solved. 🔴 **AGPL-3.0: read it as a reference design, do not fork it into client work.** |
| **auto-sigaa** | [`filipecalegario/auto-sigaa`](https://github.com/filipecalegario/auto-sigaa) | **MIT** | 9 | **LATAM (Brazil)** | Pushes a spreadsheet of grades into **SIGAA** so a teacher does not retype them. 🟢 **MIT, and the cleanest thing to fork in this subsection.** |
| **Auto_Grade_Guarani** | [`eugeborzone/Auto_Grade_Guarani`](https://github.com/eugeborzone/Auto_Grade_Guarani) | 🔴 **no licence** | 0 | **LATAM (Argentina)** | The same job against **SIU-Guaraní**. 🔵 **Two countries, two national systems, one identical unmet need — that is the finding, not the star count.** |
| **AI-Based-Timetable-Generation-System** | [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | *(also listed above)* Conflict-free timetabling under **NEP 2020** — the registrar's job, not the student's. |

🟢 **Why this subsection matters more than its stars.** `intel/trends.md` **T9** has said for several
passes that administrative automation is the most-cited adoption driver and the least-served layer.
🔵 **These rows are the first addresses this KB can put against it** — and all four do the same
narrow thing: **move grades or workload into a system of record that a human was otherwise
retyping.** That is a scoped, auditable, non-pedagogical first engagement, in a jurisdiction where
automated *assessment* is the regulated activity and data *entry* is not.

🔴 **But note the licence shape before pitching it:** of the four, **two are MIT, one is AGPL-3.0 and
one is unlicensed.** The most mature and most institutional of them (`expeditto`) is the one that
cannot be forked.

#### 🔴 The credential model is a tier-wide blocker, not a per-repo caveat

Nearly every bound connector above authenticates **as the student or parent, with their own portal
username and password**, against a platform that has not sanctioned it. `librus-mcp` states plainly
that it is *"an unofficial integration, not affiliated with Librus"* and **does not support accounts
with interactive two-factor authentication** — which means the ones that work are the ones with 2FA
switched off.

**What that means for an engagement, concretely:**

- **Do not deploy any of these as-is into a client estate.** A stored portal password is a
  credential-custody problem the client's security team will reject, and correctly.
- **It is a GDPR processing relationship with no contract.** These connectors read grades,
  attendance and absence records — personal data about children in the K-12 cases (Librus, EduPage,
  Pronote, IServ) — with no data-processing agreement and no lawful-basis analysis anywhere in sight.
- 🟢 **The sanctioned path already exists in this tier:** `barneslardo/sis-demo` shows agent access
  via **Okta OIDC/SAML + SCIM**, and `zavora-ai/mcp-student-records` shows **FERPA access logging**.
  Neither is mature, but together they describe the architecture a client can actually buy.
- 🟢 **Read these repos as integration intelligence, then rebuild the auth layer.** The API surface
  mapping is the expensive part and it is done; the credential model is the part to throw away.

##### 🟡 Qualified by p134: "nearly every" is right, "every" would not be — and the repos say which is which

🔴 **p134 ran `blackboard learn mcp` and got seven rows, where this KB carried one.** The tier's
auth model does **not** split by guesswork: **the repos declare it in their own descriptions and
topics**, and on this platform the split is three ways.

| repo | licence | ★ | last push | auth model, as the repo states it |
|---|---|---|---|---|
| [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) | **MIT** | 2 | **2026-10-11** | 🟢 **Blackboard Learn REST API**, HTTP or stdio, with **RBAC middleware for role-based access control**. *"Built for educational platform AI integrations."* 🟢 **The only row in the whole 43-row connector population that ships an access-control layer as a feature.** |
| [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp) | **MIT** | 1 | 2026-09-18 | Blackboard Learn **Ultra**: courses, content, files, grades, deadlines. 2 forks. |
| [`NiccoloSalvini/mcp-blackboard-ucsc`](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) | **MIT** | 0 | 2026-09-21 | 🟢 Explicitly *"over the **public REST API**"*. |
| [`P1ckle3/blackboard-mcp`](https://github.com/P1ckle3/blackboard-mcp) | 🔴 **no licence** | 0 | 2026-07-28 | 🟢 **Okta SSO** against **University of Queensland** Blackboard — **APAC (Australia)**. 🟢 **The second worked example of enterprise SSO in this KB**, after `barneslardo/sis-demo`, and unlike that one it is against a real institution. 🔴 Unlicensed, so unusable as published. |
| [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) | ISC | **11** | **2026-10-11** | **LATAM (Peru)** — unofficial CLI + MCP for UPC *Aula Virtual*. 🟢 **Region is now hard evidence, not inference: the repo carries the topic `peru`** (with `blackboard-learn`, `mcp-server`, `upc`) and the homepage `campuscli.com`. Pushed hours before this pass. |
| [`karkarkins/BlackboardAssistantMCP`](https://github.com/karkarkins/BlackboardAssistantMCP) | 🔴 **no licence** | 0 | 2025-09-09 | 🔴 Self-declared: *"**scrapes**, organizes, and contextualizes academic course data"*. |
| [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | 🔴 **no licence** | 0 | 2026-09-23 | 🔴 Self-declared by **topic**: `web-scraping`. |

🟢 **So the precise claim, which is more useful than the blanket one:** *where the platform vendor
publishes a REST API, the connectors use it* — four of these seven go through Blackboard's public
API or Okta SSO rather than a stored portal password. 🔴 **Where the vendor publishes nothing —
Librus, EduPage, Pronote, IServ, SIGAA, SUAP, SIU-Guaraní — every connector scrapes, because there
is no other door.** The blocker is therefore **a property of the platform, not of the builders**,
and that reframes the sales conversation: on Canvas, Blackboard, Moodle and Open edX there is a
sanctioned path today; on the national K-12 platforms there is a vendor to negotiate with
(`compose/patterns.md` → **P8**).

🔵 **One honest caveat on that reframing:** "uses the REST API" is read from the repos' own
descriptions and topics, not from their code. This pass did not audit a single implementation. A
repo that says *public REST API* and ships a password prompt would look identical from here.

### 🟢 Standards-native agents and tooling — the sanctioned alternative *(new, p134)*

🔴 **Read this tier against the credential-model blocker two sections below, because it is the
answer to it.** Everything here talks to an LMS or SIS through a published interoperability
standard — **LTI 1.3 Advantage** (launch + AGS grade passback + NRPS rosters), **OneRoster 1.2**
(rostering), **Ed-Fi** (the US K-12 data standard) or **xAPI** (learning records). A tool launched
over LTI is *invited in by the platform*, with a client ID the institution issued and can revoke.
No stored student password, no scraping, no breakage when a vendor changes an endpoint.

🟢 **It is also the best-licensed and best-owned tier in this entire KB**, and the only one with
vendor and government holders.

#### The LTI 1.3 layer — how an AI tool gets launched from inside any compliant LMS

| agent / library | repo | licence | stars | last push | origin / holder | what it gives you |
|---|---|---|---|---|---|---|
| **ltijs** | [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (payload-read, 11 361 B) | **373** | **2026-10-06** | unplaced (holder *"Carlos Vinícius Monteiro Costa"*) | 🟢 **The reference LTI 1.3 tool provider, and the largest row in this tier by a wide margin.** "Turn your application into a fully integratable LTI 1.3 tool provider" — OIDC launch, Deep Linking, AGS grade passback, NRPS. 🔴 **This is the single most important repo p134 adds to this KB:** it is 1.8× the stars of the LTI row the KB already had, it was pushed five days before this pass, and it is permissive with a named holder. First-party database plugins: [`ltijs-sequelize`](https://github.com/Cvmcosta/ltijs-sequelize) (Apache-2.0, pushed 2026-09-29). |
| **pylti1.3** | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (payload-read, 1 070 B; holder *"Dmitry Viskov"*) | **138** | 2024-08-18 | unplaced | The Python equivalent, framework-agnostic (Django/Flask). 🔴 **Dormant: last push 2024-08-18, ~2 years** — the only maturity caveat in this subsection, and it matters because Python is where the agent frameworks are. Use it, pin it, expect to maintain it. |
| **lti1p3 (Laravel)** | [`xcesaralejandro/lti1p3`](https://github.com/xcesaralejandro/lti1p3) | **MIT** | 11 | 2025-01-03 | unplaced | Laravel integration for LTI 1.3 + Deep Linking. 🟡 Its own description says *"without LTI Advantage"* — so **no AGS grade passback**. Launch only. |
| **wordpress-lti-1-3** | [`3iPunt/wordpress-lti-1-3`](https://github.com/3iPunt/wordpress-lti-1-3) | **Apache-2.0** | 6 | 2023-07-11 | **EMEA (Spain)** | LTI 1.3 Advantage on WordPress. Relevant where a client's content estate is WordPress rather than an LMS. |
| **BBDN-lti-1p3-tool-example** | [`blackboard/BBDN-lti-1p3-tool-example`](https://github.com/blackboard/BBDN-lti-1p3-tool-example) | **Apache-2.0** | 1 | 2023-11-13 | **North America — 🟢 VENDOR-OWNED (Blackboard's own org)** | Python/Flask LTI 1.3 tool with AWS deployment. 🟢 **Low stars, high procurement value: it is the platform vendor's own worked example**, which is the artefact a client's security review asks for. Sibling: [`BBDN-LTI-Adv-Node`](https://github.com/blackboard/BBDN-LTI-Adv-Node) (Node/React, 14★, **no licence field**, 2020). |
| **ltikit-sdk** | [`Liberate-Labs/ltikit-sdk`](https://github.com/Liberate-Labs/ltikit-sdk) | 🟢 **MIT** (payload-read; holder *"alasim"* — an individual, despite the org name) | 0 | **2026-10-07** | unplaced | LTI 1.3 SDK for Canvas/Moodle SSO, grade passback and deep linking. Four days old at this pass. A skeleton, not a dependency. |
| **lti-1.3-node-nextjs-starter** | [`paurushrai/lti-1.3-node-nextjs-starter`](https://github.com/paurushrai/lti-1.3-node-nextjs-starter) | **MIT** | 2 | 2026-06-17 | unplaced | `ltijs` backend + Next.js 14 front end, Dynamic Registration, PostgreSQL. 🟢 **The fastest honest start for a PoC** — it is a template over `ltijs` rather than a reimplementation. Sibling: [`lti-1p3-nextjs-starter`](https://github.com/paurushrai/lti-1p3-nextjs-starter) (MIT, MongoDB). |
| **lti-1p3-reference-tool** | [`glenn-watt/lti-1p3-reference-tool`](https://github.com/glenn-watt/lti-1p3-reference-tool) | **MIT** | 0 | 2026-06-18 | unplaced | Python/Flask, *"implemented from first principles"* — OIDC, JWKS validation, AGS, NRPS, Deep Linking. Useful for **reading**, to understand what the libraries above hide. |
| **ltitoolkit** | [`CNIT-Organization/ltitoolkit`](https://github.com/CNIT-Organization/ltitoolkit) | **MIT** | 0 | 2026-08-05 | unplaced | Python LTI 1.3 Advantage toolkit, published to PyPI. |

#### OneRoster 1.2 — rostering without a scraped password

🟢 **Two rows here are owned by organisations a client has heard of, and both are permissive.**

| agent / library | repo | licence | stars | last push | origin / holder | what it gives you |
|---|---|---|---|---|---|---|
| **edfi-oneroster** | [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (payload-read, 10 173 B) | 6 | **2026-10-09** | **North America — 🟢 the Ed-Fi Alliance's own org** | Serves a **OneRoster 1.2 API from an Ed-Fi ODS database**. 🟢 **The single most procurement-friendly row in this KB:** the standards body's own bridge between the two US K-12 data standards, permissive, 5 forks, pushed two days before this pass. 🔵 Holder class **DOCUMENT-TEXT** — the payload carries no copyright line. |
| **oneroster-integration-conformance-tests** | [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** (payload-read, 11 357 B) | 7 | 2026-07-30 | **North America — 🟢 Google's own org** | Conformance tests for a OneRoster integration. 🟢 **This is how you prove to a client that your rostering connector is correct**, and it is maintained by the vendor whose Classroom estate they probably run. |
| **oneroster-ts** | [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (payload-read, 711 B — *"BSD Zero Clause License"*) | 10 | 2026-05-11 | unplaced (holder *"Bjorn Pagen"*, a **noreply** address, despite the org name) | TypeScript SDK for the 1EdTech OneRoster API. 🟢 **0BSD is the most permissive licence anywhere in this KB — it drops even the attribution requirement**, so a derivative needs no notice at all. 🟡 Weigh that against a single-individual holder on an org-named repo. |
| **oneroster-import** | [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import) | 🟡 **GPL-2.0** | 8 | 2026-07-16 | **EMEA (Luxembourg — Open Assessment Technologies, the TAO vendor)** | Vendor-owned OneRoster import. 🟡 Copyleft; read before forking. |
| **libre-oneroster** | [`bgwdotdev/libre-oneroster`](https://github.com/bgwdotdev/libre-oneroster) | 🔴 **AGPL-3.0** | 5 | 2025-04-26 | unplaced | OneRoster server + CLI in **Rust**. 🔴 Network copyleft — do not offer it as a hosted service without reciprocal source release. |
| **roster-hub** | [`lepo-project/roster-hub`](https://github.com/lepo-project/roster-hub) | 🔴 **AGPL-3.0** | 4 | 2024-03-01 | **APAC (Japan)** | Roster-management system on OneRoster. The only APAC-origin row in this subsection. |

🔵 **Dormant but permissive, if you need a language binding:** [`vossenv/oneroster-python`](https://github.com/vossenv/oneroster-python)
(MIT, 11★, 2020), [`bgwdotdev/go-oneroster`](https://github.com/bgwdotdev/go-oneroster) (MIT, 8★, 2020),
[`jdolny/OneRoster.NET`](https://github.com/jdolny/OneRoster.NET) (MIT, 6★, 2023),
[`gotranseo/oneroster`](https://github.com/gotranseo/oneroster) (Apache-2.0, Swift, 2023),
[`TCI/OneRoster`](https://github.com/TCI/OneRoster) (MIT, 4★, pushed 2026-09-11 — the freshest of these).
🔴 [`ridencww/uniroster-server`](https://github.com/ridencww/uniroster-server) (MIT, 6★) is **archived**.

#### Ed-Fi — and the empty repository at the centre of it

| agent / library | repo | licence | stars | last push | origin / holder | what it gives you |
|---|---|---|---|---|---|---|
| **MDE-Ed-Fi-ODS-API-SDK** | [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) | 🔴 **no licence field** | 0 | 2026-04-14 | **North America — 🟢 the Minnesota Department of Education's own org** | C# client SDK for the Minnesota Ed-Fi ODS API. 🟢 **A US state education agency maintaining public code is the strongest institutional signal in this KB.** 🔴 **And it carries no licence, so it cannot be built on** — the recurring shape of this whole KB: the best-owned rows are the worst-licensed. |
| **tha-edfi-runner** | [`tha-guy-nate/tha-edfi-runner`](https://github.com/tha-guy-nate/tha-edfi-runner) | 🔴 **MIT *plus* an added visible-attribution clause** (payload-read, 1 351 B; holder *"Nathan Wright"*) | 0 | **2026-10-04** | unplaced | Typed, pipeline-friendly Python wrapper over the Ed-Fi ODS REST API (PyPI). 🔴 **Read the licence before shipping this in a client deliverable.** GitHub reports `NOASSERTION` and **GitHub is right**: the payload is MIT with an extra clause requiring *"a visible link to either the GitHub repository or the PyPI package page"* in any publicly available application or service. That is a **user-visible obligation in the client's product**, not a notice in a THIRD-PARTY file. See `P134-F`. |
| **edfi-mcp-server** | [`cdweaver1992/edfi-mcp-server`](https://github.com/cdweaver1992/edfi-mcp-server) | 🔴 **no licence field** | 1 | 2026-02-17 | unplaced | 🔴 **THE REPOSITORY IS EMPTY. There is no Ed-Fi MCP server.** Its description promises *"Model Context Protocol (MCP) server for Ed-Fi ODS/API integration"*; search reports **`size: 0`**; and the raw lane returns **HTTP 404 for all 15 probes — 5 candidate entry points (`README.md`, `.gitignore`, `package.json`, `index.js`, `src/index.ts`) across all three of `HEAD`, `main` and `master`**; and it was **created and pushed within the same second** (`2026-02-17T19:54:46Z` / `:47Z`) and never touched again. 🟢 **Listed deliberately, as a name to recognise and not install** — and as the measurement behind this pass's headline gap. |
| **edfi-via-kubernetes** | [`xmarcosx/edfi-via-kubernetes`](https://github.com/xmarcosx/edfi-via-kubernetes) | **Apache-2.0** | 1 | 2022-04-22 | unplaced | Deploys the Ed-Fi API/ODS/Admin App to GKE with Cloud SQL. Dormant, but the only infrastructure-as-code path found. Sibling for Cloud Run: [`esegrave/edfi`](https://github.com/esegrave/edfi) (Apache-2.0). |

#### 🟢 xAPI / Learning Record Store — the one real agent↔standard bridge

| agent / library | repo | licence | stars | last push | origin / holder | what it gives you |
|---|---|---|---|---|---|---|
| **learnmcp-xapi** | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 15 | 2025-08-29 | unplaced | 🟢 **The most important small repo in this KB.** An **MCP server that lets an AI agent record and retrieve learning activities through an xAPI-compliant Learning Record Store.** 🔵 **Why it matters out of all proportion to 15 stars:** every other agent on this shelf reads a *portal*, as that portal's user. This one reads and writes a *standard*, into a store the institution owns. It is the architecture the credential-model blocker has been asking for, and it is the only instance of it. 🔴 **Last push 2025-08-29 — ~14 months.** Treat as a reference design with a maintenance plan attached. |
| **warren** | [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | 17 | **2026-10-11 (the day of this pass)** | **EMEA (France — France Université Numérique)** | Visualisation toolkit for learning analytics over xAPI. 🟢 **Same national-scale owner as [`openfun/richie`](https://github.com/openfun/richie)**, already in `repos/foundations.md` — so this KB now has **two** MIT rows from a French public education operator, and this one was pushed today. The dashboard layer for anything built on an LRS. |
| **MasterObjectModel** | [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | **Apache-2.0** | 12 | 2025-07-03 | **North America — 🟢 the ADL Initiative (US DoD), who authored xAPI** | An xAPI *profile* describing how a learner's activity is tracked across their whole lifetime in a training estate. The governing body's own modelling guidance. 🔴 Sibling [`adlnet/xapi-lab`](https://github.com/adlnet/xapi-lab) (MIT, 38★ — the most-starred row in this subsection) is **ARCHIVED**. |
| **jupiter** | [`Transcordia/jupiter`](https://github.com/Transcordia/jupiter) | **MIT** | 11 | 2015-04-19 | unplaced | An LRS supporting **both xAPI and Caliper**. 🔴 Dormant since 2015 — listed because it is the only row this pass found that implements Caliper at all. |
| **LearningRecordStore-xapi** | [`ZanichelliEditore/LearningRecordStore-xapi`](https://github.com/ZanichelliEditore/LearningRecordStore-xapi) | **MIT** | 9 | 2022-06-21 | **EMEA (Italy — Zanichelli Editore, a publisher)** | Validates xAPI statements and ships them to S3. A small, real, publisher-owned LRS ingest path. |
| **SakaiXAPI-Provider** | [`Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider`](https://github.com/Apereo-Learning-Analytics-Initiative/SakaiXAPI-Provider) | 🟡 **NOASSERTION** | 11 | 2021-03-25 | **North America (Apereo)** | xAPI provider for **Sakai**, whose platform row (ECL-2.0) is already in `repos/foundations.md`. 🟡 Licence unread this pass. |

🔵 **Also found, unplaced and dormant:** [`webtech-uos/nodejs-lrs`](https://github.com/webtech-uos/nodejs-lrs)
(MIT, 9★, 2014, Universität Osnabrück), [`nicolaasmatthijs/xapicaliper`](https://github.com/nicolaasmatthijs/xapicaliper)
(no licence, 9★, 2016 — converts activities to **both** xAPI and Caliper statements), and
[`elc-gh/xAPI-Spec_ja`](https://github.com/elc-gh/xAPI-Spec_ja) (the Japanese translation of the
xAPI spec, by the **e-Learning Consortium Japan** — APAC's only row here).

#### 🔴 What this tier does NOT give you, stated precisely

🟢 **Do not read this subsection as "the problem is solved."** It is not, and the shape of what is
missing is the engagement:

- **The libraries are integration plumbing, not agents.** `ltijs` will get your tool launched and
  your grade posted. It contains no pedagogy, no model call and no agent loop. The AI is still yours
  to build; what you no longer have to build is the part a client's security team will audit.
- 🔴 **The agent↔standard bridge is one 15-star repo with a 14-month-old last push.** That is the
  gap, restated as a build: an MCP server over LTI AGS and OneRoster, with the auth model from
  `barneslardo/sis-demo` (Okta OIDC/SAML + SCIM) and the audit logging from
  `zavora-ai/mcp-student-records` (FERPA). Every piece exists separately. See
  `compose/patterns.md` → **P11**.
- 🟡 **LTI gets you into the LMS, not into the SIS.** Grade passback writes to the LMS gradebook.
  Pushing to a *system of record* — the thing the LATAM teacher-facing rows actually do — is
  OneRoster/Ed-Fi territory, and that is where the institutional owners are and the agents are not.
- 🔴 **Nothing in this tier is placed in LATAM or APAC except two AGPL-3.0 rows and a spec
  translation.** The sanctioned stack is overwhelmingly North-American and European in origin. For
  a LATAM engagement the national systems in `verticals/solutions.md` publish no comparable
  standard, which is exactly why the LATAM supply is scrapers. That is an informed gap, not an
  unexamined one.

### Moodle connectors — the tier p130 declared absent

p130's declared gaps said *"no Moodle MCP server with a clear permissive licence"*. **That is
wrong, and this KB had already established it is wrong.** Moodle's web-service API is reachable
from a *standalone* MCP server, which needs no in-tree plugin and therefore inherits no GPL
obligation at all. p130 searched for in-Moodle plugins and web-service plugins and missed the
standalone tier.

| agent | repo | licence | stars | last push | what it actually does |
|---|---|---|---|---|---|
| **moodle-mcp-server** | [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | **MIT** | 43 | 2026-02-22 | The permissive Moodle connector. Standalone MCP server over Moodle's web-service API. **Verified at pass 30 of this KB as the licence-boundary exemplar** — MIT while in-tree Moodle plugins are GPL-3.0 — and re-verified this pass by repo search (`license.spdx_id = MIT`). Two independent instruments agree. **Caveat:** last push 2026-02-22, the quietest row here, and it publishes no tags. |
| **ictexam-mcp** | [`ictinnovations/ictexam-mcp`](https://github.com/ictinnovations/ictexam-mcp) | **MIT** | 17 | 2026-09-07 | Exam authoring, delivery, gradebooks and item analysis as MCP tools, with **writes off by default**. A corporate holder (ICT Innovations) and an LTI path, which makes it the most procurement-friendly assessment connector on the shelf. |
| **moodle-mcp** (template) | [`1alexandrer/moodle-mcp`](https://github.com/1alexandrer/moodle-mcp) | **MIT** | 18 | 2026-04-21 | MCP server *template* for Moodle — the cleanest starting skeleton rather than a finished product. |
| **moodle-mcp** (dev-facing) | [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | **MIT** | 8 | 2026-06-06 | Not learner-facing: gives an agent live access to moodledev.io docs, the Hooks API, capabilities, XMLDB and the Moodle Jira tracker. Pairs with `claude-moodle-dev` below for delivery velocity. |
| **mydy-lms-helper** | [`Deeptanshuu/mydy-lms-helper`](https://github.com/Deeptanshuu/mydy-lms-helper) | **MIT** | 7 | 2026-09-29 | APAC (D.Y. Patil, India). TUI **and** MCP server over a Moodle-based institutional LMS: attendance, courses, assignments, grades, materials. A worked example of a single-institution deployment. |

**Unlicensed Moodle connectors — do not build on these:** [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp)
(**no licence field**, 40★ — the second-largest by stars and unusable as published),
[`haanhtuandev/vgu-mcp`](https://github.com/haanhtuandev/vgu-mcp) (**none**, 10★, Go, Vietnamese-German
University) and [`ink-waffle/moodle-mcp`](https://github.com/ink-waffle/moodle-mcp) (**none**, 6★).
The pattern on this tier is consistent: **the permissive ones are not the most-starred ones.**

### Evaluation and benchmark layer — p130 called this "the largest hole on the shelf"

**It is not a hole. It exists, it has been in this KB since pass 4, and the real constraint is
narrower and worse: neither member carries a usable grant.**

| benchmark | repo | licence | stars | last push | origin | what it measures |
|---|---|---|---|---|---|---|
| **MathTutorBench** | [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | 🔴 **no licence field at all** | 43 | 2026-08-27 | **EMEA (ETH Zurich, Learning & Reasoning in Education)** | Open-ended **pedagogical** capability of LLM tutors — scaffolding, hint quality, not answer accuracy. **EMNLP 2025 oral.** The closest thing to a real tutoring benchmark in open source. 🔴 **Its README states two different licences in one file** (badge: CC-BY-4.0; body: CC-BY-SA-4.0) and no `LICENSE` payload resolves, so its terms are genuinely indeterminate. |
| **Tutoring Accuracy Dataset** | [`Khan/tutoring-accuracy-dataset`](https://github.com/Khan/tutoring-accuracy-dataset) | 🔴 **bespoke "Evaluation Dataset License"** (NOASSERTION) | 57 | 2024-08-29 | North America (**Khan Academy**) | Dataset + paper *"LLM Based Math Tutoring: Challenges and Dataset"* — where LLM tutors go wrong on maths. Read in full by an earlier pass: a **2 690-byte custom licence**, not an OSI one. 🔴 **Dormant: last push 2024-08-29, ~2 years.** |

**What this means for an engagement, stated precisely:** you can *run* both against a candidate
tutor and *cite* the results, and you cannot ship either one's data inside a client deliverable
without reading those terms with counsel. The honest claim is **"the measurement layer exists and
is unshippable"**, not "it does not exist". The evaluation harness a client needs is still a build
— but it is a build that starts from two real benchmarks, not from nothing. See `compose/patterns.md` → P6.

### Academic-integrity / proctoring tier — permissive, and uniformly immature

This KB has carried a standing claim that the proctoring tier has **zero permissive rows**. That
claim is false. There are at least four MIT rows; the real finding is that **none of them is
institution-backed and none exceeds 18 stars**, against an EU high-risk class that binds
2027-12-02.

| repo | licence | stars | last push | what it is |
|---|---|---|---|---|
| [`RakeshBabuGajula/Exam_Intellect`](https://github.com/RakeshBabuGajula/Exam_Intellect) | **MIT** | 18 | 2026-10-05 | The largest permissive row. Live exam-observation dashboard: computer vision + speech recognition, real-time alerts, session tracking, automated feedback. Multi-agent. |
| [`VIJAYAPANDIANT/online-examination-system`](https://github.com/VIJAYAPANDIANT/online-examination-system) | **MIT** | 11 | 2026-08-19 | 🆕 Full exam platform with AI proctoring; React/Vite + Spring Boot, Dockerised, multi-language code execution. The most complete *platform* of the four. |
| [`singhrajvardhan/SecureExam-Platform`](https://github.com/singhrajvardhan/SecureExam-Platform) | **MIT** | 10 | 2026-04-17 | 🆕 PHP. Face tracking, tab-switch monitoring, auto-proctoring. |
| [`vishal017/cheatshield`](https://github.com/vishal017/cheatshield) | **MIT** | 8 | 2025-04-03 | 🆕 The most interesting *architecture* of the four — YOLOv5 object detection, MTCNN faces, **YAMNet audio**, PyQt5 shell. 🔴 **Stale: last push 2025-04-03, ~18 months.** |

🔴 **Read the EU constraint before proposing any of these.** Behavioural monitoring in education is
Annex III high-risk from **2027-12-02**, and anything that infers *emotion* in an education setting
is **prohibited outright and has been since 2025-02-02** (AI Act Art. 5). Three of the four rows
above do affect/behaviour-adjacent inference by construction. The permissive licence is the easy
part; the deployability check is `intel/policy-matrix.tsv`.

### Licence flags — read before building

| repo | flag | consequence |
|---|---|---|
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **NOASSERTION** (GitHub reads the licence as "Other"), 847 stars | The single most-starred education *agent-skills* collection found — 165 evidence-grounded skills for teachers, leaders and EdTech builders, spanning pedagogy, learning science, curriculum and assessment. **But the licence is not an OSI-recognised identifier**, so terms must be read before any client reuse. Do not assume permissive. |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | **No licence file at all**, 103 stars | A 54-tool Canvas MCP server with real traction and **no grant of rights**. Absent a licence, default copyright applies and Globant cannot build on it. Prefer `vishalsachdev/canvas-mcp` (MIT). |
| [`onbirdev/moodle-webservice_mcp`](https://github.com/onbirdev/moodle-webservice_mcp) | **No licence field**, 17 stars | Implements MCP as a Moodle *web-service plugin* and is listed on marketplace.moodle.com, which makes it architecturally the cleanest Moodle→MCP route found. Unlicensed as published; ask the author before use. |
| [`blend-ed/openedx-mcp`](https://github.com/blend-ed/openedx-mcp) | AGPL-3.0 | Network copyleft. Fine inside a client's own estate, a problem if the client intends to offer it as a hosted service without reciprocal source release. |
| [`GeminiLight/gen-mentor`](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | Public-domain dedication, no express patent grant and no warranty disclaimer of the Apache-2.0 kind. Legal review prefers Apache-2.0 for client deliverables. |

### Fork-swarm warning — `canvas-mcp` and `tutor-mcp`

Web search for Canvas MCP servers returns **at least five repositories carrying a byte-identical
description** ("Canvas LMS MCP server — up to 102 tools and 8 agent skills for students &
educators. Works with Claude, Cursor, Codex, and 40+ agents"): `vishalsachdev`,
`YeetingWaterbottle`, `papatistos`, `fdis111` and others. The same pattern appears for `tutor-mcp`
under both `kvnloo` and `ArnaudGuiovanna`.

GitHub repo search **excludes forks by default**. Running the fork-excluding search returns only
`vishalsachdev/canvas-mcp` and only `ArnaudGuiovanna/tutor-mcp`; every other owner of an identical
description is therefore a fork. One of those forks (`fdis111`) still advertises "80+ tools and 5
agent skills, v1.1.0" — an older state presented as current.

**Rule for later passes:** when two repos share a description, resolve the canonical one with a
fork-excluding search before writing a row. Citing a fork hands a client a stale dependency with
no upstream.

## Declared gaps — restated, because three of p130's four were refuted by this KB's own pages

🔴 **Two of p130's four declared gaps were not gaps.** They are struck through below with what
refutes them, because a false absence is more expensive than a missing row: it tells a studio there
is nothing to start from when there is.

- ~~**No education-specific agent-evaluation or learning-outcome benchmark** in open source. This is
  the largest hole on the shelf.~~ 🔴 **REFUTED.** `eth-lre/mathtutorbench` (43★, ETH Zurich, EMNLP
  2025 oral) has been in this KB **since pass 4**; `Khan/tutoring-accuracy-dataset` (57★) had its
  bespoke 2 690-byte licence read in full by an earlier pass. 🟢 **The surviving gap is narrower and
  sharper: the benchmark layer carries no usable grant** — one repo has no licence field, the other
  a custom non-OSI one. And neither measures *learning outcomes*; both measure tutor behaviour.
  **"No outcome benchmark" is defensible. "No benchmark" was not.**
- ~~**No Moodle MCP server with a clear permissive licence.**~~ 🔴 **REFUTED.**
  `peancor/moodle-mcp-server` is **MIT** with 43★ and was verified by this KB at **pass 30** as the
  licence-boundary exemplar; `ictexam-mcp`, `1alexandrer/moodle-mcp`, `SaadRahman01/moodle-mcp` and
  `mydy-lms-helper` are MIT too. 🟢 **The surviving gap is maturity and ownership, not licence:**
  the permissive Moodle connectors are individually owned, the largest has not been pushed since
  February 2026, and the most-starred one of all (`loyaniu/moodle-mcp`, 40★) has no licence at all.
- **No LATAM-origin education agent above 11 stars.** 🟢 **SURVIVES.** `alejooroncoy/campus-cli`
  (ISC, 11★, Peru) is still the only one, and it is one person's university tool. An informed gap,
  not an absence of demand — see `intel/market.md`.
- ~~**No agent targeting a student information system** (enrolment, records, timetabling).
  Administrative automation, the most-cited adoption driver, still has no open-source **agent**.
  That is the largest genuine hole on this shelf now.~~ 🔴 **REFUTED BY p132 — and this was the
  gap this KB had just promoted to "the largest genuine hole".** There are **21 rows**, tabled
  above: `librus-mcp` (MIT, 10★, Poland), `DAU-buddy` (7★, India), `vtop-bhopal-mcp` (Apache-2.0,
  India), `soongpt-plugin` (MIT, Korea), `edupage-mcp` ×2 (MIT, Slovakia), `mcp-pronotes` (MIT,
  France), `iserv-mcp` (MIT, Germany), `sisu-mcp` (Finland), `ibu-mcp` (MIT, Bosnia), `nycu` (MIT,
  Taiwan), `qldt-hanu-mcp` (GPL-2.0, Vietnam), `ntnu-mcp` (MIT, Norway), `mcgill-vsb-mcp` +
  `UofT-MCP` + `uoft-quercus-mcp` (MIT, Canada), `vsuet-timetable-api-mcp` (MIT, Russia),
  `classroom-mcp` (MIT, standalone), `mcp-student-records` (Apache-2.0, FERPA logging),
  `sis-demo` (SCIM/Okta), `AI-Based-Timetable-Generation-System` (MIT, NEP 2020) and `ddl-killer`
  (China). 🔵 **Cause of the false absence: the category term is absent from the field.** No query
  containing *"student information system"* can reach a repo called `librus-mcp`.
  🟢 **Three narrower gaps survive and are worth more than the one they replace:**
  **(a) nothing in the tier exceeds 10 stars**, so there is no production-grade row;
  **(b) the credential model is unsanctioned portal scraping** with a stored student password —
  see the blocker note above, and `sis-demo` and `mcp-student-records` for the two partial answers;
  **(c) no row touches an open-source system of record.** All 21 connect to *proprietary or
  institution-hosted* portals; `openeducat_erp`, `frappe/education`, `academico`, RosarioSIS and
  Gibbon still have **zero** agent coverage (`repos/foundations.md`).
- 🆕 **No permissive proctoring project with an institutional owner.** Four MIT rows exist (above);
  the largest is 18★ and all four are individual projects. Against an Annex III high-risk class
  binding 2027-12-02, this is the tier an EMEA client will ask for and the shelf cannot supply at
  production grade.

## How a row gets onto this page (rule added by p131)

🔴 **Repo search is authoritative for METADATA and blind to PAYLOAD.** It returns
`license.spdx_id`, stars, `pushed_at` and the fork flag correctly. It cannot tell you what a
`LICENSE` file actually grants when GitHub's matcher reports `NOASSERTION` ("Other"), and it cannot
see an address that an earlier pass found with a different query.

**So, before declaring anything absent:** grep this KB's own append-only pages for the class first.
Three of p130's four declared gaps would have failed that grep in under a second. A full rewrite
that re-derives every page from one instrument discards everything the KB established with the
others.

## The vocabulary rule (added by p132, and it outranks the rule above)

🔴 **Grepping this KB would NOT have saved `P132-A`.** The SIS-agent gap was not a row this KB had
and forgot — it was a field this KB had never been able to see, because **every probe for it was
built from the analyst's vocabulary and the field is named in the builders' vocabulary.** No star
threshold and no amount of internal grepping fixes that.

**So, before declaring a CLASS absent, name the class three ways and probe all three:**

1. **the category term** — *"student information system"*, *"proctoring"*, *"benchmark"*;
2. **the capability every member must implement** — *timetable*, *attendance*, *grade passback*
   (this is the one that worked: `timetable timetabling MCP` found 21 rows that `SIS` could not);
3. **the proper nouns of the market** — the platform and vendor names a practitioner in that
   country would use: Librus, EduPage, Pronote, IServ, Sisu, uSaint, VTOP, Quercus, Blackboard.

🔵 **Probe 3 is where regional supply hides.** A tier that looks empty from a global English query
is often fully populated under ten national platform names — and those rows come with their region
already attached as evidence, which is the thing this KB most often lacks.

### 🔴 Clause 4, added by p133: a proper noun is only a probe if it is not a homograph

p133 ran probe 3 for LATAM and ANZ and it worked — **15 rows, 12 of them LATAM, a region this KB had
declared empty four times.** 🔴 **But two probes failed, and they failed in the opposite direction
from `P132-A`: the proper noun was not proper enough.**

| probe | intended | returned |
|---|---|---|
| `ucampus` | **U-Campus**, Universidad de Chile | a **Chinese** *u校园* homework tool (GPL-2.0, 34★) and an Indian campus-food app |
| `ucampus chile universidad` | same | 🔴 **0** |
| `seqta` | **SEQTA**, Australia | the real SEQTA rows **plus** genomics (`SeqTagger`, `SeqTagQA`) |

**So, when probing by platform name:**

4. **Carry a country or vendor qualifier as a named control, and check the top hits are in the right
   language and sector.** A bare noun that returns a populated page in the wrong language has told
   you nothing about your market. 🔴 **If the bare probe returns noise and the qualified probe
   returns zero, report "no evidence found for this platform" — never a row count, and never a
   regional zero.** Chile is recorded that way in `intel/market.md`, with both probes named.

🔵 **Both failure modes have the same root and it is worth stating once:** a search result is a fact
about the query. `P131-E` found it with a multi-term zero, `P132-A` with a category term that reached
nothing, `P133-E` with a proper noun that reached the wrong field. **Every regional or tier-level
absence in this KB must name the probe that produced it, or it is not a finding.**

### 🔴 Clause 5, added by p134: name the class in the PROFESSIONAL register too

p132 established that a category term cannot reach a field named by platform. p133 established that
a platform noun can reach the wrong field. 🔴 **p134 found a fourth register, and it is the one that
reaches the institutional and vendor-owned supply this KB most wants and most lacks.**

| register | example probe | what it reached |
|---|---|---|
| 1. the **category** term | `student information system` | 🔴 nothing — p132's 21 rows were invisible to it |
| 2. the **capability** every member implements | `timetable timetabling MCP` | 🟢 p132's **21 rows** |
| 3. the **proper nouns** of the market | `sigaa`, `suap mcp`, `siu-guarani`, `seqta` | 🟢 p133's **15 rows** (and `P133-E`'s homograph failures) |
| 4. 🆕 the **standard / professional** register | `grade passback`, `lti 1.3 advantage`, `oneroster`, `ltijs`, `xapi` | 🟢 p134's **tier above** — including the only **vendor-owned** (Blackboard, UNIwise, OAT) and **government-owned** (Ed-Fi Alliance, Minnesota DoE, ADL, France Université Numérique) rows in this KB |

🔵 **Why register 4 reaches owners the other three cannot.** Registers 1–3 are the vocabulary of
*users* — a category an analyst invented, a capability a student wants, a portal a university runs.
Register 4 is the vocabulary of **the standards an institution procures against**. Vendors and
public bodies publish code named for the standard they conform to, because conformance is the
thing they are selling. 🔴 **So a tier that looks like it is built entirely by students may simply
have been queried entirely in students' words** — which is what happened here for ten passes.

🔴 **And register 4 has its own failure mode, new this pass: tokenizer fragmentation.** A hyphenated
standard name is split and matched as substrings of unrelated words.

| probe | returned |
|---|---|
| `ed-fi in:name,description` | 🔴 **24 061** results, topped by `FizzBuzzEnterpriseEdition` (23 898★), `filerobot-image-editor`, `FireRed-Image-Edit`, `Mastering-Python-for-Finance-Second-Edition`, `next-firebase-auth-edge` |
| `edfi ods api in:name,description` | 🟢 **6** rows, every one a genuine Ed-Fi project |

🔵 **The hyphen is not a token boundary that protects you — it is one that betrays you.** `ed` and
`fi` each match inside *Edition*, *Edit*, *ReFinED* and *edge*. **Before reporting a count from a
hyphenated or two-letter standard name, run the unhyphenated form and a qualifier and compare the
two counts.** A four-order-of-magnitude gap between them means the first probe measured the
English language, not the field.

🔴 **A second register-4 hazard, also new: relevance pollution under `sort=stars`.** `xapi learning`
sorted by stars returns, at ranks 1–6, anti-government propaganda repositories carrying 3 258,
2 038, 371, 211, 202 and 127 stars. **The first genuine row is rank 7.** Sorting a broad query by
stars ranks incidental high-star matches above the entire field. **Read past the head of the list,
or the single most-starred "finding" will be unrelated to education.**

## 🔴 Gaps this page declares after p134

🟢 **Two gaps on this page are retired by the tier above, and the replacements are narrower, which
is the point.**

- ~~**The portal-connector tier's credential model makes the whole tier undeployable, and the
  sanctioned path is immature** (`sis-demo`, `mcp-student-records`, *"neither is mature"*).~~
  🔴 **RETIRED AS STATED.** The sanctioned path is not immature — it is **`ltijs` at Apache-2.0 and
  373★, `pylti1.3` at MIT and 138★, OneRoster bridges owned by Google and the Ed-Fi Alliance, and an
  Ed-Fi line maintained by a US state department of education.** 🟢 **The surviving gap is one layer
  up and far more actionable: the standards are mature and the AGENT BINDING TO THEM IS ONE REPO**
  (`DavidLMS/learnmcp-xapi`, MIT, 15★, last push 2025-08-29), **and the only Ed-Fi MCP server is an
  empty repository.** That is a build with every dependency already chosen.
- ~~**`campus-cli` is the only Blackboard connector.**~~ 🔴 **REFUTED.** There are **seven**, four of
  them MIT, and four reach the platform through its public REST API or Okta SSO rather than a stored
  password.
- **No standards-native row originates in LATAM.** 🟢 **SURVIVES, and it now has a mechanism rather
  than a shrug:** the sanctioned tier is North-American and European because **Ed-Fi, OneRoster and
  LTI are North-American and European procurement standards.** SIGAA, SUAP, SIU-Guaraní, SAES,
  Q-Acadêmico and SIAGIE publish no equivalent, so LATAM supply is scrapers by necessity. The one
  named counterparty remains `SIU-Toba` (`verticals/solutions.md`).
- 🆕 **No conformance-tested connector for anything but OneRoster.** `googleworkspace/oneroster-integration-conformance-tests`
  is the only test suite found that proves an integration correct. There is no equivalent for LTI
  AGS, for Ed-Fi, or for any of the 43 portal connectors — so "it works" is currently a developer's
  assertion in every engagement this KB can supply.
- 🆕 **Nothing in the standards tier has been code-audited by this KB.** Every auth claim above is
  read from a description or a topic. `P134-G`'s three-way split is a claim about what seven repos
  *say*, and a repo that says *public REST API* while shipping a password prompt is indistinguishable
  from here. **This is the first gap in this KB that can only be closed by reading source, not by
  running a better query.**
