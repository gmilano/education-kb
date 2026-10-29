---
industry: education
region: Global
updated: 2026-10-29
---

# Foundational Education Repos

**Pass `p534` · 2026-10-29.** Load-bearing systems an education engagement is
likely to inherit, extend or integrate against — not agents (those are in
[`../agents/top.md`](../agents/top.md)), but the platforms, standards and
toolkits the agents must live beside.

🔴 **The count in this sentence was stale and is now stated as arithmetic rather
than asserted.** This header read *"Pass `p532` · **Fifty-eight**"* while `p533`
filed **eleven** further rows below it without touching it — so the headline
number was wrong for a whole pass, in the one place a reader looks first.
🟡 By pass arithmetic the figure is **fifty-eight + eleven (`p533`) + three
(`p534`) = seventy-two**; it is *derived*, not recounted, because several
sections here are **censuses** (the Moodle MCP census alone covers 222
addresses) and a row count and a "load-bearing system" count are not the same
quantity. 🔵 A recount against an explicit rule for what counts is `Gap 534-E`
— and until it runs, no total on this page should be quoted.

> 🟢 **`p530` adds a layer this file did not have: the e-learning standards
> implementations.** Twelve repos — SCORM runtimes, xAPI learning record stores,
> LTI frameworks, knowledge-tracing libraries and autograders. 🔴 **None of them
> is new to this base.** Every one was already in its append-only history, some
> across twenty passes, and none had ever reached a curated file. They surfaced
> only once `Gap 529-A`'s index existed
> ([`../ingest/address-ledger.py`](../ingest/address-ledger.py)).
>
> 🔵 **Why this layer decides engagements.** An institution does not buy a tutor;
> it buys something that plugs into the LMS it already runs. These twelve are how
> you plug in, and **eleven of the twelve are MIT, Apache-2.0 or BSD** — against
> a platform-core layer below that is almost entirely copyleft. 🔴 **The
> permissive surface of this sector is the integration layer, not the
> platforms.**
>
> 🔴 **One retrieval failure worth naming, because the search channel stated it
> as a capability gap.** Asked for an open-source grader this pass, generic
> search replied *"I found no open-source agent that grades students."* This base
> already owned **three permissive autograders totalling 2 337★**. The gap was
> never in the world.

> 🆕 **`p529` changed one section of this file and nothing else — the same
> section, again, and this time the correction runs the other way.** The GitHub
> search API became reachable this pass (see
> [`../agents/top.md`](../agents/top.md)), and it reports **`total_count: 222`**
> for the Moodle MCP field. `p528`'s census of eleven was not a census; it was a
> sample of what a search engine surfaced. 🔴 **The ceiling, the star total and
> the licence spread are all corrected below.** The platform-core and
> administration rows above were not re-read this pass except where the API
> corroborated them — `fsrs4anki` (**MIT, 4,119★**), `openeducat_erp` (**LGPL**,
> 900★ / **782 forks**) and `rosariosis` (**GPL-2.0**, 648★) all **confirmed**.

> 🆕 **`p528` changed one section of this file and nothing else.** The Moodle MCP
> census below was re-probed from scratch — existence first, then the licence
> file's title block — and `p527`'s reading of that field ("roughly three real
> codebases") is **corrected to eleven**. The platform-core rows were not
> re-read this pass and carry `p527`'s verification; their dates and digests are
> `p527`'s, not this pass's.

> **Every licence in this file was re-read this pass from the licence file's own
> title block**, fetched from `raw.githubusercontent.com` (reachable, while
> `github.com` and `api.github.com` return HTTP 403 through the session proxy).
> Star counts remain rounded page values. This changed one cell, and it was the
> cell `p526` flagged red — see the Frappe Education row.

> **Licence reality for this sector, stated plainly and confirmed again:** the
> mainstream education platforms are **copyleft**, not permissive. Moodle is
> GPL-3.0, Open edX and Canvas are AGPL-3.0. A targeted search for a mainstream
> Apache/MIT LMS returned none. This is not a gap in the research — it is the
> shape of the market, and it drives the architecture: **build permissive agents
> that integrate across a process or network boundary** (LTI, xAPI, REST, MCP)
> rather than forking an AGPL core and inheriting its obligations.

## Platform cores

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9.3k | "A complete web conferencing system for virtual classes." README names **BigBlueButton 4.0**; default branch `v4.0.x-develop`. The default synchronous-classroom layer, already integrated into Moodle, Canvas and Open edX. LGPL is the friendliest copyleft here. |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | AGPL-3.0 | 8.2k | The Open edX LMS + Studio authoring core. *(`openedx/edx-platform` now redirects here — use the `openedx-platform` address.)* The reference choice for MOOC-scale and large corporate-training deployments. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7.6k | "The world's open source learning platform." PHP, `main` branch, 123k+ commits. **Largest plugin ecosystem in the sector by a wide margin** — which makes the plugin boundary the cheapest place to attach anything new, and makes the missing Moodle MCP server (see below) the loudest gap on this base. |
| [oppia/oppia](https://github.com/oppia/oppia) | **Apache-2.0** | 7.0k | "A free, online learning platform to make quality education accessible for all." Python + Angular on App Engine. **The largest permissively licensed learning platform found** — the one core on this shelf a studio can fork without copyleft consequences. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | AGPL-3.0 | 6.9k | "The open LMS by Instructure, Inc." Dominant in North American higher ed. Caveat worth repeating to any client: the open-source codebase is **not** equivalent to Instructure's full commercial feature set. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3.4k | "Easy to Use, 100% Open Source Learning Management System." Title block read this pass: `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`. Lighter and newer than Moodle, sitting on the Frappe/ERPNext stack — the natural LMS when the client already runs Frappe for administration. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1.2k | Higher-ed teaching, research and collaboration platform. Title block: `Educational Community License, Version 2.0 (ECL-2.0)` — an Apache-2.0 derivative with a patent-grant tweak for academic consortia, **permissive in practice**. Page lists 25.2 and 23.5 as community-supported. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1.2k | "The offline app for universal education." Python + JS, `develop` branch, ~39.8k commits. **The only MIT-licensed full learning platform on this shelf**, and the only one designed for intermittent or absent connectivity — the deciding constraint for LMIC and rural deployments in LATAM, Africa and South/Southeast Asia. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | AGPL-3.0 | 1.1k | "The Docker-based Open edX distribution designed for peace of mind." In practice nobody should deploy Open edX by hand; this is the supported path, and the plugin system is where customisation belongs. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; install docs reference **v2.0.3**. Strong footprint in Spanish- and French-speaking deployments with small or no technical staff — relevant for LATAM public-sector work. |

## Administration, records and integrity

| Repo | Licence | Stars | Why it is foundational |
|---|---|---|---|
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | "Comprehensive Open Source ERP for Educational Institutes", built as Odoo modules; branch `19.0`. Admissions, timetabling, attendance, fees, library, hostel. The ERP counterpart to the LMS cores above. |
| 🔵 [frappe/education](https://github.com/frappe/education) | **GPL-3.0** — *resolved this pass* | 685 | "Open source education / school management system." **`p526` left this red:** the repository page renders no licence type and a `license.txt` is present but unnamed. Fetched directly this pass, the file is three lines of front matter — `--- / License: GNU GPL V3 / ---` — so it is **GPL-3.0**: strong copyleft, *not* permissive, and **not the same licence as Frappe LMS**, which is AGPL-3.0. Two apps, same stack, two different copyleft regimes; a deliverable spanning both inherits both. 472 forks. |
| [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | **LATAM anchor.** School-management software described on its own page as "the largest free education software in Brazil" — originally built by the municipal government of **Itajaí, Santa Catarina**, released on the Brazilian federal Public Software Portal in 2008, now stewarded by Portábilis. Any Brazilian public-sector education engagement meets this system. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 648 | "RosarioSIS Student Information System for school management." PHP/PostgreSQL, modular, widely deployed in small and mid-size schools; strong Spanish/French/Portuguese localisation. Origin is not stated on the repo page. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | **EMEA anchor.** German non-profit-governed LMS, branch `release_11`. The usual choice for compliance-heavy European public-sector and government training, where governance provenance matters as much as features. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 449 | **EMEA, permissive.** Swiss web-based LMS covering teaching, learning, assessment and communication. Apache-2.0 plus a European governance story is a rare combination on this shelf — the best base for an EMEA engagement that needs to ship proprietary extensions. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | "Source code plagiarism detection" — finds similar or modified solutions to programming exercises. Copyright line reads `Team Dolos <dolos@ugent.be>`, i.e. **Ghent University (EMEA)** — read from the licence file, not inferred. No LLM in it, and that is the point: assessment-integrity findings have to be explainable to an appeals board. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | Framework-independent PHP library for H5P interactive content; grant at **`LICENSE.txt`**. H5P is the de facto interoperable format for interactive exercises across Moodle, Canvas, Open edX and Drupal — the cheapest way to make generated content portable. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | QTI-standard computer-based assessment core. The right base when items must interoperate with national testing infrastructure. |
| [openfun/ralph](https://github.com/openfun/ralph) | **MIT** | 51 | "The ultimate Learning Record Store (and more!) for your learning analytics." Python/FastAPI/Pydantic; copyright line reads `France Université Numérique` (**EMEA**). Fifty-one stars and genuinely load-bearing: it is the **xAPI/LRS seam** where agent-generated learning events get stored in a standard shape instead of a vendor's private table. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | 4.1k | FSRS (Free Spaced Repetition Scheduler). The retention primitive — use it instead of inventing a review interval, because the scheduling problem is solved and the solution is permissive. |

## 🆕 The Moodle MCP census — 🔴 **222 addresses, not eleven; ceiling 52★ and ungranted**

> 🔴 **`p529` correction, read this before the table.** The heading of this
> section used to read *"eleven codebases, 37 stars, no convergence"*. The API
> reports **222** matching addresses; `p529` read the **top 80 by stars**, which
> alone total **352★**. The field's ceiling is **not** `G36maid` at 27★ — it is
> [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) at **52★**, and
> ⛔ **it has no licence file** (no `license` key from the API; no file at five
> paths on `main`). The permissive ceiling is
> [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server),
> **MIT, 45★**, last pushed **22 Feb 2026**. Licence spread over the 80 read:
> **MIT 44 · none 18 · GPL-3.0 7 · `NOASSERTION` 4 · Apache-2.0 4 · AGPL-3.0 2 ·
> WTFPL 1** → **60% permissive, 27.5% with no usable grant** — not *"ten of
> eleven MIT"*.
>
> 🔵 **And the conclusion changes with the number.** `p528` recommended
> consolidating eleven codebases. **You cannot consolidate 222 repositories whose
> purpose is to be institution-specific** — 14 of the top 26 bridge one named
> university each, and LATAM and APAC ship five apiece while **North America
> ships none**. The asset is a **bridge generator**, not a merged bridge. Full
> census, regional placement and reasoning in
> [`trending.md`](trending.md); the recipe is `P558` in
> [`../compose/patterns.md`](../compose/patterns.md).
>
> ⚠️ **The table below is `p528`'s thirteen-address census, kept as-is**, because
> its tool counts and read/write analysis are first-hand and the API exposes
> neither. **Read it as a deep sample of the field, not as the field.**

⚠️ **This section is corrected and widened this pass.** `p527` wrote that the
Moodle MCP field is *"eight search results, roughly three real codebases"*. That
was wrong, and it was wrong in the direction that matters: the field is not
small, it is **fragmented**. `p528` probed **twelve addresses first-hand** —
existence first (`README.md` on `main` and `master`), then the licence file's
title block — for a census of **thirteen**. ⚠️ The thirteenth,
`triffon/moodle-mcp`, is **carried from `p527`** as a confirmed duplicate of
`falkenslab` and was *not* re-probed this pass; its row is marked. The thirteen
resolve to **eleven independent codebases plus two forks**.

| Repo | Licence (title block) | Stars | Lang | Tools | Reads / writes |
|---|---|---|---|---|---|
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** | **27** | Rust (`rmcp`) | 22 (20 typed + 2 escape hatches, opt-in via `MOODLE_ENABLE_WS_FUNCTION`) | Web Services; courses, assignments, forums, grades, files-as-markdown. **Verified live against Moodle 3.7, 4.5 and 5.2** — the only one on this list that names three tested versions. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT (`© G36maid`) | 0 | Rust | 22 | ⛔ **Fork of the above**, stated on the page; the copyright line confirms it. |
| 🆕 [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | **MIT** (`© Ghaith AlHallak`) | 3 | Python 3.14+ | **40** (32 read / 8 write) | Writes **off by default** behind two separate flags (`MOODLER_ALLOW_STUDENT_WRITES`, `MOODLER_ALLOW_TEACHER_GRADING`); destructive calls require `confirm=true`. Playwright/Chromium sign-in, SQLite cache, ships as a `.mcpb` bundle. 🟢 **The best-governed write model in the census.** |
| 🆕 [Faixiang/moodle-mcp](https://github.com/Faixiang/moodle-mcp) | **MIT** | 2 | Python 3.8+, **stdlib only** | 8 | Read-only against Moodle (the one exception, `moodle_download_week`, writes to local disk). Single `server.py`, zero dependencies, docs in 10 languages, verified against Moodle 4.3.6. ⚠️ `v1.3.0` dated 2026-10-27 — **and all four changelog entries, 1.0.0 through 1.3.0, carry that same date.** Treat the version history as a self-claim. ⚠️ Its own "Why this exists" section still says *"six read-only tools"* against a table of eight. |
| 🆕 [leshamblin/MoodleMCP](https://github.com/leshamblin/MoodleMCP) | **MIT** | 2 | Python 3.10+, FastMCP | **70 claimed / 67 counted** | Read *and* write, with the clearest safety story: read-only by default, writes confined to `MOODLE_DEV_COURSE_WHITELIST`, `MOODLE_PROD_ALLOW_WRITES=false` recommended, token in a local `.env`. Writes cover grading, enrolment, messages and forum posts. |
| [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | **MIT** | 2 | — | **~230 claimed** | Drives a logged-in **browser session** rather than Web Services; README claims grading-with-rubrics and quiz construction for Moodle 4.5/5.x. ⚠️ Largest tool claim in the census and the least verifiable; a search summary said 140, the README says ~230, **neither is verified by use.** |
| [triffon/moodle-mcp](https://github.com/triffon/moodle-mcp) | MIT (`© Falkenslab`) | — | — | ~230 | ⛔ **Same code as `falkenslab`** — identical copyright holder and description. Not an independent project. |
| 🆕 [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** | 0 · 2 forks | **Go** | 14 | 13 read + `submit_assignment` (write) + `login`. Also exposes a REST mode for ChatGPT and Gemini. Student-facing. README examples use a `uom.lk` domain (University of Moratuwa, **Sri Lanka**) — 🟡 *inferred*, not stated. |
| 🆕 [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) | **MIT** — 🔴 **but see the dependency** | 0 | Python | 14 | Read-mostly CLI + MCP server; SQLite FTS5 search. 🔴 **Its own page states that PyMuPDF, its PDF-extraction dependency, is AGPL-3.0.** A repo-level licence probe grades this buildable; the shipped artefact carries network copyleft. ⚠️ Also notes its `moodle_mobile_app` token *can* permit writes on some sites — so "read-only" here is a property of the deployment, not of the code. |
| 🆕 [AnonymousOnyx22/moodle-student-mcp](https://github.com/AnonymousOnyx22/moodle-student-mcp) | **MIT** | 0 | TypeScript / Node 20+ | 12 | Read-only by construction — *"can never submit, edit or delete anything."* States *"Not affiliated with Moodle Pty Ltd."* |
| [duck-5/moodle-mcp](https://github.com/duck-5/moodle-mcp) | **MIT** | not read | — | — | Independent small implementation; existence and grant re-confirmed `p528`, star count not read. |
| ⚠️ [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** (title block: *"GNU AFFERO GENERAL PUBLIC LICENSE"*) | 1 | TypeScript / Node | — | The most *visible* in search results and **the one that is not permissive.** Read-only by design, no plugin install needed. AGPL-3.0 §13 on an integration server a hosted deliverable calls is an architecture decision, not a detail. |
| ⛔ [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) | **none** | — | — | — | A search result called it *"MIT licensed."* Repository **resolves**; **no licence file at any of six common paths on `main`.** ⛔ Ungranted — `p527`'s call, re-confirmed this pass. |

**The read, corrected.** Thirteen addresses, **eleven independent codebases**,
**four languages**, tool counts spanning **8 → ~230**, and **37 stars in total
across every codebase whose counter was read this pass** — less than one eighth
of [canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) alone (**308★**), for
the *larger* install base.

🟢 **Ten of the eleven independent codebases are MIT.** That is the finding that
changes the build decision. The gap is not a licensing problem and not an
absence — it is 🔴 **a convergence problem**: no two of these agree on a tool
vocabulary, nobody is above 27★, and the one project with real traction is
written in Rust while the mass of the field is Python.

🔵 **So the build is a consolidation, not a greenfield.** The pieces to take, all
MIT, all verified this pass: **G36maid's typed-tool surface and tested version
matrix**, **moodler-mcp's two-flag write gate with `confirm=true`**,
**leshamblin's course-whitelist boundary**, **Faixiang's zero-dependency
posture**. The thing none of them has is a **shared tool vocabulary** — and that,
not another server, is what would make this the sector's bridge. See
[`../compose/patterns.md`](../compose/patterns.md) **P553**.

⚠️ **One caveat on the whole census:** every star count here is a rounded page
value read through the session proxy, and every tool count is the repository's
own claim. Three of them contradict themselves on that claim (Faixiang 6 vs 8,
leshamblin 70 vs 67, falkenslab 140 vs ~230). **Tool counts in this field are
marketing, not measurement.**

## 🆕 Standards, records and assessment — the integration layer (`p530`)

Grants read from the licence file's own title block; counters exact from the API
this pass. **Passes unfiled** is from
[`../evidence/address-ledger.tsv`](../evidence/address-ledger.tsv) — how many
distinct passes described the address before anything filed it.

| Repo | Licence | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [adlnet/xAPI-Spec](https://github.com/adlnet/xAPI-Spec) | Apache-2.0 | 956 | — | The xAPI specification itself, from US DoD ADL — the vocabulary every learning-record claim in this sector is written against. 402 forks. 🟡 Apache-2.0 on a *specification document* is deliberate, not a category error: the patent grant is the point. |
| [yetanalytics/lrsql](https://github.com/yetanalytics/lrsql) | Apache-2.0 | 144 | 🔴 **19** | A SQL-backed xAPI Learning Record Store. Clojure, runs on Postgres/SQLite. **This is where agent-generated learning events belong** — an institution will ask where the data lands, and an LRS is the standards-compliant answer. |
| [adlnet/ADL_LRS](https://github.com/adlnet/ADL_LRS) | Apache-2.0 | 334 | — | ADL's own reference LRS, Python. 156 forks. 🟡 Pushed **2025-11-14** — the reference implementation, not the one to deploy; `lrsql` is the live option. |
| [jcputney/scorm-again](https://github.com/jcputney/scorm-again) | MIT | 361 | 🔴 **20** | A modern SCORM JavaScript runtime (SCORM 1.2 / 2004 / AICC), offline-first, cross-frame. TypeScript. **The bridge to every legacy course package an institution already owns**, and the reason an AI layer need not discard existing content. |
| [tsugiproject/tsugi](https://github.com/tsugiproject/tsugi) | Apache-2.0 | 377 | 🔴 **14** | LTI tool framework — build a tool once, launch it inside Moodle, Canvas, Sakai or Open edX. 267 forks. **The cheapest route to putting an agent inside an LMS an institution will not replace.** |
| [packbackbooks/lti-1-3-php-library](https://github.com/packbackbooks/lti-1-3-php-library) | Apache-2.0 (`LICENSE.md`) | 54 | — | IMS-certified LTI 1.3 tool-provider library, PHP. 🔴 **A fork, so GitHub repository search does not return it** — see shelf rule 10. Certification is what matters here, not the star count. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 | 471 | 🔴 **15** | The Open edX component SDK: the supported way to add a custom learning component to an AGPL-3.0 platform **without touching the platform's code**. 231 forks. 🔵 Note the grants differ — the SDK is Apache-2.0 while the core is AGPL-3.0. |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | MIT | 291 | — | Bayesian Knowledge Tracing and extensions, from Berkeley's CAHLR — the same lab behind [OATutor](https://github.com/CAHLR/OATutor) on the agent shelf. C++ core with Python bindings. **Mastery estimation that a faculty board will accept**, because it predates the LLM era and has a literature. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | 453 | — | pyKT: benchmark library for deep knowledge tracing, with standard datasets and prediction scenarios. **The way to show an adaptive claim is measured rather than asserted.** |
| [jupyter/nbgrader](https://github.com/jupyter/nbgrader) | BSD-3-Clause | 1 370 | — | Assigning and grading Jupyter notebooks — release, collect, autograde, manual-grade, return feedback. 345 forks. **The highest-starred permissive grading system in this sector.** |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | BSD-3-Clause | 806 | — | Homework submission, automated grading and TA grading, from RPI. **1 118 forks against 806 stars** — a deployment-heavy system, i.e. institutions actually run it. |
| [ucbds-infra/otter-grader](https://github.com/ucbds-infra/otter-grader) | BSD-3-Clause | 161 | — | Python *and* R autograding, container-based, from Berkeley Data Science. The lighter alternative to Submitty when only the grading half is wanted. |

🔴 **What this layer does not contain: an agent.** Every row above is
infrastructure an agent would *drive*. The composition is in
[`../compose/patterns.md`](../compose/patterns.md).

## 🆕 Serving the course — the JupyterHub deployment family (`p531`)

🔴 **This is the single largest coherent layer this base has ever been missing,
and it was not missing from the world — it was missing from this file.** Every
row below sat in an `archive/` snapshot and **nowhere in the live corpus**: they
are part of the **349** addresses `Gap 530-A` measured as dropped by a rewrite.
`p531` read the grant of all 349 first-hand and these came back **BSD-3-Clause,
every one**, title block `BSD 3-Clause License · Copyright (c) 2016/2017,
Project Jupyter Contributors`.

🔵 **Why it is foundational and not plumbing.** This file already carries
[`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (1 370★) — how you
*grade* notebooks. It carried nothing about how a university *serves* them to
500 students, authenticated out of the LMS they already log into, on hardware
they already have. That is the whole gap between a notebook demo and a course,
and it is **nine live repositories, 2 309★, all permissive**.

| Repo | Licence | Stars | Forks | Last push | What it is for |
|---|---|---|---|---|---|
| [jupyterhub/kubespawner](https://github.com/jupyterhub/kubespawner) | **BSD-3-Clause** | **611** | 308 | 2026-10-27 | Spawns each student's notebook server as a Kubernetes pod. **The default answer for a cohort of any size**, and the one that makes per-student resource limits a config value rather than a project. |
| [jupyterhub/dockerspawner](https://github.com/jupyterhub/dockerspawner) | **BSD-3-Clause** | **543** | 305 | 2026-10-27 | The same, in Docker containers on one host. 🟢 The right choice for a single-department pilot, and the cheapest credible demo in this layer. |
| [jupyterhub/oauthenticator](https://github.com/jupyterhub/oauthenticator) | **BSD-3-Clause** | **443** | 367 | 2026-10-27 | OAuth2 sign-in — Google, GitHub, Globus, generic OIDC. The institutional-identity half for any tenant that already runs SSO. |
| [jupyterhub/ldapauthenticator](https://github.com/jupyterhub/ldapauthenticator) | **BSD-3-Clause** | **214** | 177 | 2026-08-20 | LDAP/AD sign-in. 🔵 Named separately because in public-sector and EMEA university estates **this, not OAuth, is what the directory speaks**. |
| [jupyterhub/ltiauthenticator](https://github.com/jupyterhub/ltiauthenticator) | **BSD-3-Clause** | 73 | 55 | 2026-07-01 | 🔴 **The row that connects this layer to the rest of the file.** Launch the hub *from inside Moodle, Canvas or Brightspace* over LTI, so the student never sees a second login. Known to this base since `p13` and described in **13 separate passes** without ever being filed. |
| [jupyterhub/batchspawner](https://github.com/jupyterhub/batchspawner) | **BSD-3-Clause** | **207** | 137 | 2026-07-17 | Spawns into Slurm/PBS/LSF batch queues. **The HPC route** — the deciding row wherever the client's compute is a research cluster, which in higher education it usually is. |
| [jupyterhub/systemdspawner](https://github.com/jupyterhub/systemdspawner) | **BSD-3-Clause** | 101 | 45 | 2026-10-24 | systemd units with real resource limits, no container runtime. The answer when Docker is not permitted on the box. |
| [jupyterhub/wrapspawner](https://github.com/jupyterhub/wrapspawner) | **BSD-3-Clause** | 65 | 60 | 🟡 2025-08-16 | Lets the *student* pick a spawner/profile at launch. 🟡 Fourteen months stale — read it, pin it, do not assume maintenance. |
| [jupyterhub/sudospawner](https://github.com/jupyterhub/sudospawner) | **BSD-3-Clause** | 52 | 39 | 2026-08-05 | Spawns as the student's own Unix user via a narrow sudo rule. The shape a university's own sysadmins will ask for. |

🔴 **Two members of the family are archived by their owner and are read-only
history:** [`jupyterhub/yarnspawner`](https://github.com/jupyterhub/yarnspawner)
(19★, Hadoop/YARN) and
[`jupyterhub/jupyterhub-tutorial`](https://github.com/jupyterhub/jupyterhub-tutorial)
(**202★**). 🔵 The second is worth naming precisely because it is the thing a
reader would reach for first: **the official deployment tutorial is archived**,
so an engagement should budget its own runbook rather than cite that one. 🟡
[`jupyterhub/kerberosauthenticator`](https://github.com/jupyterhub/kerberosauthenticator)
(12★, BSD-3-Clause, live) completes the authenticator set for Kerberos estates.

## 🆕 The LTI libraries this base has described 55 times and never filed (`p531`)

🔴 **`p530` built the integration layer above and filed the PHP LTI library
while leaving the Node and Python ones unfiled.** These are the **#1 and #2
most-described unfiled permissive addresses in the entire live corpus**, by the
base's own ledger:

| Repo | Licence | Stars | Forks | Passes unfiled | Why it is foundational |
|---|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | **Apache-2.0** | **373** | 86 | 🔴 **28** | *"Turn your application into a fully integratable LTI 1.3 tool provider."* TypeScript/Node. **The reference implementation of the Node LTI stack** — the one an agent written in TypeScript attaches to any LMS with. Pushed 2026-10-13. |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** | **138** | 84 | 🔴 **27** | LTI 1.3 Advantage tool for Python, with Django/Flask adapters. 🟢 The Python counterpart, and therefore the one that sits in front of a Python agent without a language boundary. Pushed 2026-09-10. |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** | 6 | 3 | 11 | Dependency-light, framework-neutral TypeScript reference implementation of **QTI 3** assessment items. 🔵 QTI is how an assessment moves between systems; this is the only permissive, current QTI 3 implementation this base has found. |
| [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET) | **MIT** | 6 | 8 | 12 | OneRoster API client. 🔵 OneRoster is **rostering** — the standard a district uses to tell a tool who is in which class. Thin, .NET-only, and the only permissive client on record. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | **Apache-2.0** | 61 | 31 | 12 | Open Badges validation, Python, **from the standards body itself**. The credential half: if a deliverable issues badges, this is what says whether they are well-formed. |
| [Apereo-Learning-Analytics-Initiative/OpenLRW](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRW) | **ECL-2.0** | 62 | 25 | 12 | Apereo's Learning Record Warehouse — Caliper/xAPI ingestion with a OneRoster-shaped model. 🟡 ECL-2.0 behaves as permissive (Apache-2.0 with an academic patent tweak), which this base has already graded on `sakaiproject/sakai`. |

## 🆕 Assessment science, and the licence-compliance instruments (`p531`)

| Repo | Licence | Stars | Forks | What it is for |
|---|---|---|---|---|
| [douglasrizzo/catsim](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** | **153** | 37 | **Computerised Adaptive Testing** simulator: item-response theory, item selection, ability estimation, stopping rules. 🟢 **The only permissive CAT/IRT implementation on this base**, and the thing that separates "an LLM asks harder questions" from a defensible adaptive assessment. Author in Brazil — **LATAM-origin psychometrics**. Pushed 2026-10-28. |
| [open-spaced-repetition/fsrs.js](https://github.com/open-spaced-repetition/fsrs.js) | **MIT** | **180** | 14 | FSRS — the scheduler that superseded Anki's SM-2. The retention half of any tutoring deliverable, as a library rather than a prompt. |
| [VienDinhCom/supermemo](https://github.com/VienDinhCom/supermemo) | **MIT** | **337** | 24 | SM-2 in JS/TS. 🔵 Filed beside FSRS deliberately: SM-2 is simpler, auditable in an afternoon and still what a client's existing flashcard data was scheduled with. |
| [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | **Apache-2.0** (code) · 🟡 **CC-BY-4.0** (licence datasets) | **2 656** | 831 | 🔴 **`Gap 528-C` closes here, with a retrieval instead of a build.** Its own README states it *"detects licenses, copyrights, package manifests, **direct dependencies**"* and *"can process packages, build manifest and lockfile formats"* — which is exactly the dependency-grant enumerator `528-C` had scoped as new work for four passes. 🟡 **Read the dual grant before shipping:** the engine is Apache-2.0, the reference licence data is CC-BY-4.0, so redistributing the rule set carries attribution duties. |
| [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | **Apache-2.0** | **2 109** | 393 | The orchestrated form of the same job: an *Analyzer* that *"determines the dependencies of projects and their metadata, abstracting which package managers are actually being used"*, plus an Evaluator for policy-as-code. 🟢 Pick `ort` when the client wants a **gate in CI**; pick `scancode` when they want the **evidence**. |
| [anchore/syft](https://github.com/anchore/syft) | **Apache-2.0** | **9 792** | 1 031 | SBOM generation from images and filesystems (SPDX, CycloneDX). The deployed-artefact view, where the other two read the source tree. |

🔵 **Five of the six rows above came out of a drop set, and the sixth off the
live promotion queue** — `catsim` had been described in **10** separate passes
and never filed; `ort`, `syft`, `fsrs.js` and `supermemo` are in the **349**
archive-only addresses `p531` triaged; `scancode` is in `archive-drops`, the
691-row looser bound. 🔴 **Four licence/SBOM instruments — `scancode`, `ort`,
`syft`, [`CycloneDX/cyclonedx-cli`](https://github.com/CycloneDX/cyclonedx-cli)
(Apache-2.0, 552★) — were owned, dropped, and then re-scoped as a build.** That
is `Gap 528-C`'s whole history, and it is a retrieval failure, not a supply gap.

## 🆕 Two platform rows the drop set also returned (`p531`)

| Repo | Licence | Stars | What it is |
|---|---|---|---|
| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | **MIT** | **823** | *"Interactive Learning with Automated Feedback"*, from **TU München**. Programming, modelling, text and quiz exercises with automated assessment and an exam mode, in production across European universities. 🔴 **MIT, 823★, 395 forks, pushed today — and this base had no row for it.** The strongest permissive assessment platform in EMEA, and the natural alternative to bolting autograding onto Moodle. Ansible collection: [`ls1intum/artemis-ansible-collection`](https://github.com/ls1intum/artemis-ansible-collection) (MIT). |
| [opensacorg/learning-blocks](https://github.com/opensacorg/learning-blocks) | **MIT** | 6 | 🟢 **A second permissive Student Information System.** `p529` published *"zero permissive SIS"*; `p530` falsified it with `academico-sis/academico` (MIT, 409★). This is the third reading: the field is small and thin, but it is **not empty and not copyleft-only**. 22 forks against 6★ — more forks than stars, the signature of a system people deploy rather than star. Python. Pushed 2026-09-21. |

## 🆕 The LMS agent-bridge layer completes — Blackboard was the hole (`p532`)

Every row below came off the **ranked** promotion queue
([`../evidence/promotion-queue.2026-10-29-p532.tsv`](../evidence/promotion-queue.2026-10-29-p532.tsv)),
not off a search, and every grant was read this pass from the licence file's own
title block over `raw.githubusercontent.com`.

> 🔴 **The hole this closes.** This base has carried a Canvas bridge since `p490`
> (`canvas-mcp`, MIT, 308★), filed a Brightspace bridge at `p531`
> (`brightspace-mcp-server`, MIT, 60★), and censused the Moodle MCP field twice
> — while saying nothing about **Blackboard Learn**, which is one of the four
> LMS platforms a Western higher-ed engagement actually meets. The bridge
> existed, MIT-licensed, and this base had described it in **8 separate
> passes**.
>
> 🟡 **Read the star counts honestly.** `bb-mcp` is **2★** and
> `MarcosNahuel/moodle-mcp` is **1★**. These are not adopted projects; they are
> *correct starting points with a permissive grant*, which in this layer is the
> scarce thing — `p529` measured the Moodle MCP field at **222 addresses with a
> 52★ ceiling that is ungranted**. A studio forks one of these; it does not
> depend on it.

| Repo | Licence (title block) | Stars | Passes unfiled | Why it is foundational |
|---|---|---|---|---|
| [nitsuah/bb-mcp](https://github.com/nitsuah/bb-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 nitsuah` (1 063 B, `e024d09e682a`) | 2 | 🔴 **8** | **The Blackboard Learn bridge this shelf had no row for.** A *standalone* MCP server wrapping the Blackboard Learn REST API — its README argues the case explicitly: *"the integration logic lives here, not in the client… build it once, use it everywhere."* Any MCP client (Claude Desktop, Cursor, agent-board) attaches unchanged. 🔵 With this row the agent-bridge layer covers **all four** major LMS platforms: Canvas, Brightspace, Moodle and Blackboard. |
| [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | 🟢 **MIT** — `MIT License · Copyright (c) 2026 Italicia` (1 065 B, `f27341a8425b`) | 1 | 🔴 **9** | **The most capable Moodle MCP this base has read, and the field's own census said the ceiling was ungranted.** Wrapper **v0.5.2** + a companion Moodle plugin **v0.5.0**, exposing **40 high-level facades** plus one `ws_raw` escape hatch, over Moodle Web Services, with *idempotency guarantees* — its README claims ~80% of a course teaching workflow operable from an agent. 🟡 Spanish-language file paths and an `Italicia` copyright; **no country stated**, so unplaced. |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 🟢 **MIT** — `MIT License · Copyright (c) Microsoft Corporation` (1 141 B, `c2cfccb812fe`) | 🔴 **78.1k** | 🔴 **23** | **Courseware, not an agent — and filed here for exactly that reason.** 18 lessons on building AI agents, with runnable Python on Microsoft Agent Framework and Foundry. For an education engagement this is the *reference curriculum artefact*: the thing to fork when a client wants an AI-literacy track with working code, and the thing to point at when asked what a well-structured 18-lesson technical course looks like. 🔴 **The single largest promotion debt in this base's history** — described in 23 passes, filed in none until now. |

## 🆕 The materiality-ranked queue's first eleven rows (`p533`)

Every row below came off
[`../evidence/promotion-queue.2026-10-29-p533.tsv`](../evidence/promotion-queue.2026-10-29-p533.tsv)
— the queue `Gap 532-B` asked for, gated on grant and liveness and ranked by
**measured** stars rather than by how often this base had mentioned the address.
Grants marked 🟢 were read this pass from the licence file's own title block over
`raw.githubusercontent.com`; the rest are API SPDX ids, flagged as such per shelf
rule 8.

> 🔴 **The queue's own headline: recall ranked an unusable address first and the
> largest permissive asset in this sector eighteenth.** See
> [`trending.md`](trending.md). The three A-band rows below had been described in
> this base **5, 7 and 7 separate passes** and filed in none.

| Repo | Licence | Stars | What it is, and why it is here |
|---|---|---|---|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 🟢 **BSD-3-Clause** (`main/LICENSE.md`) | 🔴 **458,181** | *"freeCodeCamp.org's open-source codebase and curriculum."* 🔴 **The largest permissive asset this base has ever touched, by a factor of 32 over the next-largest unfiled address**, and it sat at recall rank 18. 🟡 **Read what it is before costing it in:** this is a **curriculum plus the platform that delivers it**, not a library — the reusable parts are the curriculum corpus, the challenge/test format and the certification model. BSD-3-Clause means all of it may be reused with attribution. 🔵 For an engagement that needs *content* rather than a tutor, this is the starting point, and `Gap 533-C` is the note that stars alone would overstate it. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 🟢 **MIT** (`main/LICENSE`) | **14,372** | *"A framework for building, orchestrating and deploying AI agents and multi-agent workflows."* The successor line to AutoGen and Semantic Kernel. 🔵 Filed on the foundations leg rather than the agent shelf because it is **horizontal** — nothing in it is education-specific — but it is the orchestration layer most of this base's multi-agent patterns (`P549`, `P553`, `P558`) actually need, and it is MIT. |
| [frappe/frappe](https://github.com/frappe/frappe) | 🟢 **MIT** (`master/LICENSE`) | **11,024** | *"Low code web framework for real world applications, in Python and JavaScript."* 🔴 **The licence distinction this base has needed since `p526`:** the **framework** is MIT, while **Frappe Education and Frappe LMS on top of it are GPL-3.0 and AGPL-3.0** respectively (see the licence map below). So the platform is copyleft and the thing underneath it is not — which means a studio can build an education app *on Frappe* without inheriting Frappe Education's grant. 🔵 That is a genuinely different architecture decision from the one the licence map implied while only the apps were filed. |
| [autolab/Autolab](https://github.com/autolab/Autolab) | 🟢 **Apache-2.0** (`master/LICENSE`) | 808 | *"Course management service that enables auto-graded programming assignments."* From **Carnegie Mellon**. 🟢 **The autograder layer, which this base had no row for at all** — and it is permissive, which the rest of the layer is not (see `judge0` below). Ruby on Rails, with language-agnostic grading in containers. 🔵 Pairs directly with `Artemis`/`EduTelligence` as the North American analogue of the same idea; see `P567`. |
| [uPortal-Project/uPortal](https://github.com/uPortal-Project/uPortal) | 🟢 **Apache-2.0** (`master/LICENSE`) | 287 | *"Enterprise open source portal built by and for the higher education community."* Java. 🔵 The **student-facing front door** — the layer that aggregates LMS, SIS, calendar and announcements into one authenticated surface. For an engagement where the ask is *"one place where the student sees everything, with an agent in it"*, this is the permissive host, and nothing else on this base occupies that position. |
| [judge0/judge0](https://github.com/judge0/judge0) | 🔴 **GPL-3.0** (`master/LICENSE`) | **4,498** | *"Robust, fast, scalable, and sandboxed open-source online code execution system for humans and AI"* — its own topics include `ai-agent-tools` and `ai-agents`. 942 forks. 🔴 **Copyleft, and filed here anyway because the architecture answer is specific:** GPL-3.0 is **not** AGPL-3.0, so running Judge0 as a **separate self-hosted network service** that a proprietary deliverable calls over HTTP does not pull copyleft onto the deliverable, where `classroomio` (AGPL-3.0) would. 🔵 **Any agent that grades, runs or tests student code needs a sandbox, and this is the field's default one.** Deploy it beside the product, never inside it. |
| [webtech-network/autograder](https://github.com/webtech-network/autograder) | 🟢 **Apache-2.0** (`main/LICENSE`) | 62 | *"Flexible, Consistent and Powerful Autograding Tool that grades and generates feedback."* 🟢 The permissive, small-footprint alternative to the two rows above when the ask is grading *with feedback* rather than a full course-management system. |
| [opensalt/opensalt](https://github.com/opensalt/opensalt) | 🟢 **MIT** — 🔴 **ledger carried `GPL-3.0\|Apache-2.0`; corrected this pass** | 47 | *"Standards Alignment Tool."* Authoring, hosting and aligning academic standards (CASE/CFItem). 🔵 This is the repository that makes *"which standard does this question assess?"* answerable as data rather than as a prompt — the same job `corretor-enem` does for ENEM and `bncc-dev` for the BNCC, generalised. 🟢 **The grant correction matters:** it moved from "copyleft, check carefully" to permissive on one title-block read. |
| [1EdTech/OpenCASE](https://github.com/1EdTech/OpenCASE) | `Apache-2.0` (API) | 11 | *"Implementations of CASE Server and Editor"*, from **1EdTech** itself — the standards body. The reference implementation behind the row above. |
| [Ed-Fi-Alliance-OSS/Data-Management-Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) | `Apache-2.0` (API) | 12 | *"Code and design documentation for the Ed-Fi API Platform, successor to the Ed-Fi ODS/API."* 🔵 **North America's K-12 data-interoperability layer**, and the successor generation of it — the row to start from when an engagement's first problem is *"the student data is in six systems."* Its sibling [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, 6★) serves a **OneRoster 1.2** API over an Ed-Fi ODS, and [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) (🟢 **MIT**, `master`) is the .NET client — 🔴 **one of the three addresses the API silently dropped this pass**, see shelf rule 14. |
| [open-edge-platform/education-ai-suite](https://github.com/open-edge-platform/education-ai-suite) | 🟢 **Apache-2.0** (`main/LICENSE`) | 2 | *"The Education AI Suite is a collection of open-source reference applications."* 🔵 **Two stars and worth more than its band suggests**, which is why `Gap 533-C` exists: this is **Intel's** `open-edge-platform`, so it is edge-and-on-premise reference architecture under a permissive grant, pushed **2026-10-29**. For `P565` (the disconnected classroom) and for any EMEA sovereignty engagement, vendor-backed on-prem reference code is scarcer than stars. |

🟡 **Also measured, also unfiled, and deliberately *not* promoted:**
[`tl-its-umich-edu/my-learning-analytics`](https://github.com/tl-its-umich-edu/my-learning-analytics)
(Apache-2.0, 37★, Univ. of Michigan — a learning-analytics dashboard, useful but
not a foundation), [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player)
(MIT, 30★, QTI 3 item player — a renderer, listed under the standards leg
already), and the three `learning-commons-org` repositories
([`knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
164★, [`evaluators`](https://github.com/learning-commons-org/evaluators) 87★),
which return **`NOASSERTION`** and so are **not yet graded** — per shelf rule 8
that means *the title block has not been read*, not that a grant exists. 🔴 They
are the highest-starred ungraded addresses left on the queue and the obvious
first read for `p534`.

## 🆕 `p534` — the institutional AI toolchain, off `Gap 533-A`'s org enumeration

`Gap 533-A` said this base's "is it filed?" test matches on the **address**, so
an institution that ships its platform in one repository and its intelligence in
another reads as *filed* the moment the platform is. 🟢 **Nine orgs already
cited on these pages were enumerated this pass** —
[`../evidence/org-layer-diff.2026-10-29-p534.tsv`](../evidence/org-layer-diff.2026-10-29-p534.tsv)
— and the three rows below are what came back that belongs on *this* page rather
than on the agent shelf. Grants read first-hand from the licence file's title
block, bytes and sha256 recorded in
[`../evidence/grant-reads.2026-10-29-p534.tsv`](../evidence/grant-reads.2026-10-29-p534.tsv).

| Repo | Licence (title block) | Stars | Fitness | Why it is foundational |
|---|---|---|---|---|
| 🆕 [mitodl/agent-kit](https://github.com/mitodl/agent-kit) | 🟢 **BSD-3-Clause** — `BSD 3-Clause License · Copyright (c) 2026, Tobias Macey` (1 499 B, `8afd1cd502a7`, `main` `431fde4`) | 5 | `infrastructure` | **The agent platform a real university's AI team actually runs.** Three `witan` packages — `witan-council` (work coordination), `witan-code` (a code graph for coding agents) and `witan-core` (shared memory) — plus the `agent-config-kit` CLI, reusable skills (`creating-skills`, `dependency-updates`, `deploy-verification`), custom agent definitions for **Claude Code and GitHub Copilot**, MCP install helpers (`witan-council`, `witan-code`, `toolhive-swe`) and six environment profiles. **551 commits**, docs on Read the Docs. 🔵 Education logic lives in [`mitodl/learn-ai`](https://github.com/mitodl/learn-ai); *this* is the plumbing under it, and BSD-3-Clause makes it the most permissively licensed institutional agent toolkit on this base. |
| 🆕 [Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC) | 🟢 **Apache-2.0** (11 357 B, `c71d239df917`, `main` `d42adc2`) | 🔴 0 | `reference-implementation` | *"Prompts, Skills, Hooks, Agents, etc. for use in the Ed-Fi Alliance software development lifecycle."* 🔵 Its value is **whose** SDLC it is: Ed-Fi governs the data standard that US K-12 student records move on, so this is the standards body publishing how it uses agents on its own codebase — a citable precedent for the governance conversation, which is the part of an education engagement that has no open-source answer anywhere else on this page. 🔴 Zero stars, pushed 2026-09-08. |
| 🆕 [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | 🟢 **MIT** — `MIT License · Copyright (c) 2025 AI Agents from Scratch Contributors` (1 091 B, `f78cc6bf1d57`, `main` `da3f9df`) | **~1.1k** (page-rounded) · 262 forks | `curriculum` | **Twelve lessons building an agent from a single local LLM call** — text in/out, tools, the agent loop, memory, planning, **evals and telemetry** — with no frameworks, no cloud APIs and no hidden reasoning. Topics include `ai-education` and `open-source-education`. 🔴 **Filed as a `curriculum`, and the distinction is the point:** there is nothing here to deploy for a client. It ramps a studio team, on a local model, without an API budget. 🔴 **It is also the only new address generic web search has produced in seven passes** — and the search snapshot's **796★** against the page's **~1.1k** is a ~38 % disagreement, which is why no star figure on these pages is search-sourced. |

## 🆕 `p534` — a register claim this base has **refuted**, recorded rather than restored

🔴 **`make gate-prose-claims` reports `NO-PERMISSIVE-PLATFORM` as `CLAIM-LOST`**
— *"a declared gap that three patterns choose their base on"* — and asks this
file to carry the sentence **"No permissive education platform exists"**.

🟢 **It is recorded here as RETIRED, not restored, because this base's own
shelves disprove it.** Three permissive full learning platforms are filed on
this page:

| Platform | Grant | Stars |
|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | 🟢 **Apache-2.0** | 7.0k |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** | 449 |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** | 1.2k |

plus [sakaiproject/sakai](https://github.com/sakaiproject/sakai) under
**ECL-2.0**, an Apache-2.0 derivative that is permissive in practice.

🔵 **Why this is written down instead of simply dropped.** `p494` established
that a deleted claim is indistinguishable from coverage — so the honest
discharge of a refuted claim is a **dated retraction in the file that owed it**,
naming the evidence that killed it. 🔴 **And the register row should now be
retired**, because a gate that demands a false sentence will eventually be
satisfied by someone re-asserting it. → noted in
[`../intel/open-gaps.md`](../intel/open-gaps.md) under `Gap 534-I`.

## Licence map, for the architecture decision

| Band | Repos |
|---|---|
| **Permissive — fork freely** | 🆕 **freeCodeCamp (BSD-3-Clause, 458k★)**, 🆕 **frappe/frappe (MIT)**, 🆕 **microsoft/agent-framework (MIT)**, 🆕 **Artemis + EduTelligence (MIT, TU München)**, 🆕 **Autolab (Apache-2.0, CMU)**, 🆕 **uPortal (Apache-2.0)**, 🆕 **webtech-network/autograder (Apache-2.0)**, 🆕 **opensalt (MIT)**, Oppia (Apache-2.0), OpenOLAT (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Dolos (MIT), Ralph (MIT), FSRS (MIT), 🆕 **ten of the eleven Moodle MCP codebases (MIT)** — G36maid, moodler-mcp, Faixiang, leshamblin, falkenslab, Jawadh-Salih, open-moodle*, moodle-student-mcp, duck-5 |
| **Weak copyleft — link across a boundary** | BigBlueButton (LGPL-3.0), OpenEduCat (LGPL-3.0) |
| **Strong copyleft — integrate, do not fork** | Moodle, Chamilo, ILIAS, H5P (GPL-3.0); 🔵 **Frappe Education (GPL-3.0)** — 🆕 but **`frappe/frappe`, the framework underneath it, is MIT**, so the copyleft is in the app, not the platform; i-educar, RosarioSIS, TAO (GPL-2.0); 🆕 **Judge0 (GPL-3.0)** — 🟢 **deploy it as a separate network service and the copyleft does not reach your deliverable**, because GPL-3.0 has no §13 |
| **Network copyleft — integrate, do not fork, and read §13** | Open edX, Canvas, Frappe LMS, Tutor, csmediapro/moodle-mcp-server (AGPL-3.0); **PyMuPDF (AGPL-3.0)** — reached *transitively* by the MIT-licensed `sonstellar969/open-moodle`; 🆕 **classroomio/classroomio (AGPL-3.0, 1,735★)** — the contrast that makes the Judge0 row's distinction concrete |

🔴 \* **`open-moodle` is MIT and still lands in the network-copyleft row in
practice**, because it links AGPL-3.0 PyMuPDF for PDF extraction. 🔵 **The rule:
the grant you ship is the union of the grants you link** — a repo-level licence
probe cannot see this, and this is the first instance of it recorded on the
platform legs.

AGPL-3.0 §13 reaches users interacting over a network, which is precisely the
hosted-SaaS shape most engagements want. **The integration seams — LTI 1.3, xAPI
via Ralph, H5P content, Canvas/Moodle REST, MCP servers — are where permissive
code belongs.**

## Searched and not found

- **No mainstream Apache/MIT-licensed LMS** beyond Oppia and OpenOLAT. Searched
  explicitly again; the sector is copyleft and that is the finding.
- **No permissively licensed SIS.** Every student-information system found is
  GPL-2.0 or GPL-3.0 — and `frappe/education`, the one genuinely unresolved cell
  on this file, resolved to **GPL-3.0** this pass rather than to something
  permissive. The AI-native advising option
  ([canyongbs/advisingapp](https://github.com/canyongbs/advisingapp)) is
  Elastic-2.0 and unusable as a hosted base.
- 🔴 **No credible Moodle MCP server — but not for lack of attempts.** See the
  census above: **eleven independent codebases, ten of them MIT, 37 stars
  between them, a 27★ ceiling** on the sector's biggest LMS. 🔵 Corrected from
  `p527`, which read the same field as *"roughly three real codebases."*
- 🆕 🔴 **No shared tool vocabulary for Moodle.** Eight tools in one server, ~230
  in another, and no two naming the same operations the same way. This is the
  actual missing artefact, and it is a specification rather than a product.
- **No APAC-origin platform core surfaced on the platform legs this pass.** APAC's
  open-source strength in education is on the *agent* legs (DeepTutor, OpenMAIC,
  lineage-skill, Educhain) — see [`../agents/top.md`](../agents/top.md). Moodle's
  Perth origin is historical and its governance is now global.
- **No LATAM-origin platform beyond i-educar and RosarioSIS's localisation.**
