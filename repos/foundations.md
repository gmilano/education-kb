---
industry: education
region: Global
updated: 2026-10-29
---

# Foundational Education Repos

**Pass `p527` · 2026-10-29.** Twenty load-bearing systems an education engagement
is likely to inherit, extend or integrate against — not agents (those are in
[`../agents/top.md`](../agents/top.md)), but the platforms the agents must live
beside.

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

## 🆕 The Moodle MCP lineage — recorded so nobody re-discovers it as eight projects

Moodle is the largest LMS in the sector and has **no credible agent bridge.**
Every candidate was licence-probed and page-read this pass. Written out because
a search for "Moodle MCP" returns eight results that look like eight projects:

| Repo | Licence | Stars | What it actually is |
|---|---|---|---|
| [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | **MIT** | **27** | **The lineage's real head** — the only one with any traction. Courses, assignments, forums, grades, files-as-markdown. Links to `moodle.ntnu.cc`. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT (`© G36maid`) | 0 | **A fork of the above**, stated on the page. Rust, 22 tools (20 + 2 escape hatches), README claims validation against Moodle 3.7 → 5.x. The copyright line gives the lineage away. |
| [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | MIT | 2 | Browser-driving server; README claims **~230 tools** for Moodle 4.5/5.x. ⚠️ A search summary said 140 — the README says about 230. Neither is verified by use. |
| [triffon/moodle-mcp](https://github.com/triffon/moodle-mcp) | MIT (`© Falkenslab`) | — | **Same code as `falkenslab`** — identical copyright holder, identical description. Not an independent project. |
| ⚠️ [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | **AGPL-3.0** | 1 | The most *visible* in search results and **the one that is not permissive.** TypeScript, read-only by design ("never modifies Moodle data"). AGPL-3.0 on an integration server that a hosted deliverable would call is a licence decision, not a detail. |
| [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) · [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) · [duck-5/moodle-mcp](https://github.com/duck-5/moodle-mcp) | MIT | low single digits | Independent small implementations. |
| ⛔ [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) | **none** | — | Described in a search result as "MIT licensed". **No licence file at any common path.** Ungranted. |

**The read:** eight search results, roughly **three real codebases**, a 27★
ceiling, and the most-surfaced option under AGPL-3.0. Against
[canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) at **308★** for the
*smaller* install base. This is the gap, and it is a build, not a fork.

## Licence map, for the architecture decision

| Band | Repos |
|---|---|
| **Permissive — fork freely** | Oppia (Apache-2.0), OpenOLAT (Apache-2.0), Sakai (ECL-2.0), Kolibri (MIT), Dolos (MIT), Ralph (MIT), FSRS (MIT), G36maid/moodle-mcp (MIT) |
| **Weak copyleft — link across a boundary** | BigBlueButton (LGPL-3.0), OpenEduCat (LGPL-3.0) |
| **Strong copyleft — integrate, do not fork** | Moodle, Chamilo, ILIAS, H5P (GPL-3.0); 🔵 **Frappe Education (GPL-3.0)**; i-educar, RosarioSIS, TAO (GPL-2.0) |
| **Network copyleft — integrate, do not fork, and read §13** | Open edX, Canvas, Frappe LMS, Tutor, csmediapro/moodle-mcp-server (AGPL-3.0) |

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
- 🔴 **No credible Moodle MCP server.** See the lineage table above. The sector's
  biggest LMS, a 27★ ceiling.
- **No APAC-origin platform core surfaced on the platform legs this pass.** APAC's
  open-source strength in education is on the *agent* legs (DeepTutor, OpenMAIC,
  lineage-skill, Educhain) — see [`../agents/top.md`](../agents/top.md). Moodle's
  Perth origin is historical and its governance is now global.
- **No LATAM-origin platform beyond i-educar and RosarioSIS's localisation.**
