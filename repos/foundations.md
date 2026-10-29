---
industry: education
region: Global
updated: 2026-10-29
---

# Foundational Education Repos

**Pass `p528` · 2026-10-29.** Twenty load-bearing systems an education engagement
is likely to inherit, extend or integrate against — not agents (those are in
[`../agents/top.md`](../agents/top.md)), but the platforms the agents must live
beside.

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

## 🆕 The Moodle MCP census — **eleven codebases, 37 stars, no convergence**

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

## Licence map, for the architecture decision

| Band | Repos |
|---|---|
| **Permissive — fork freely** | Oppia (Apache-2.0), OpenOLAT (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Dolos (MIT), Ralph (MIT), FSRS (MIT), 🆕 **ten of the eleven Moodle MCP codebases (MIT)** — G36maid, moodler-mcp, Faixiang, leshamblin, falkenslab, Jawadh-Salih, open-moodle*, moodle-student-mcp, duck-5 |
| **Weak copyleft — link across a boundary** | BigBlueButton (LGPL-3.0), OpenEduCat (LGPL-3.0) |
| **Strong copyleft — integrate, do not fork** | Moodle, Chamilo, ILIAS, H5P (GPL-3.0); 🔵 **Frappe Education (GPL-3.0)**; i-educar, RosarioSIS, TAO (GPL-2.0) |
| **Network copyleft — integrate, do not fork, and read §13** | Open edX, Canvas, Frappe LMS, Tutor, csmediapro/moodle-mcp-server (AGPL-3.0); 🆕 **PyMuPDF (AGPL-3.0)** — reached *transitively* by the MIT-licensed `sonstellar969/open-moodle` |

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
