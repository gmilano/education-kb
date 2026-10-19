---
industry: education
region: Global
updated: 2026-10-19
---

# Vertical platforms — education

**Pass 318 · 2026-10-19.** Nineteen platforms — the real systems a client is already running, or
would run, with AI built on top. **Checked** says which pass took the licence/star reading.

**New this pass: `openedx/openedx-ai-extensions`, and it is the most significant row this KB has
added in several passes** — not for its size (17 ★) but for who wrote it. It is the official
Open edX AI plugin, it lives under the `openedx` organisation, and it was built by **eduNEXT, a
Bogotá company**. That makes it the first **LATAM-authored** education-AI infrastructure this KB
has found in six passes of looking. Detail below, including why it is not yet usable.

Also new: two AI-native LMS platforms with real adoption (`frappe/lms`, `learnhouse`), and a
**licence-verification finding that should change how this KB sources candidates** — see the end.

| Platform | Repo | Licence | ★ | Checked | What it is | AI-on-top angle |
|---|---|---|---|---|---|---|
| BigBlueButton | https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.2k | p315 | Web conferencing purpose-built for virtual classrooms | Post-session agents: transcription, participation analytics, summary-to-LMS |
| Open edX | https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | p317 | LMS + Studio behind large-scale MOOCs and corporate academies; 68,824 commits. The older `openedx/edx-platform` URL redirects here | Agents as XBlocks or LTI tools; AGPL makes the network boundary non-negotiable |
| Moodle | https://github.com/moodle/moodle | GPL-3.0 | 7.5k | p317 | The world's most deployed open source LMS; 123,234 commits | **Ships its own core AI subsystem since 4.5 — read the Moodle note below before proposing a custom tutor** |
| Canvas LMS | https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | p316 | The open LMS by Instructure; 78,765 commits | Same AGPL discipline as Open edX — and see the Project Athena note below |
| frappe/lms | https://github.com/frappe/lms | AGPL-3.0 | 3.3k | p318 | "Easy to use, open source, Learning Management System" on the Frappe framework; 7,837 commits, 1.6k forks. Courses/chapters/lessons, batches with Zoom live classes, quizzes, PDF assignments, certificates | **No AI features in the product at all** — a clean, well-adopted LMS substrate for an external agent. Distinct from `frappe/education` below |
| LearnHouse | https://github.com/learnhouse/learnhouse | **AGPL-3.0 + separate Enterprise Licence** | 2.4k | p318 | "Next-gen Open Source learning platform"; 2,804 commits, 580 forks. Next.js/React/Tiptap over FastAPI/Postgres/Redis; block editor, assignments, discussions, analytics, certificates | **AI-native**: "context-aware AI for learning & teaching", AI-generated playgrounds/simulations, code execution with auto-grading in 30+ languages. Google Gemini + LlamaIndex in the stack. **Open-core — see caveat** |
| Sakai | https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | p317 | Learning, teaching, research and collaboration platform used in higher ed; 55,483 commits | ECL-2.0 is an Apache-2.0 derivative with an academic-attribution twist — the most permissive mature LMS core here |
| Kolibri | https://github.com/learningequality/kolibri | MIT | 1.2k | p318 | Offline-first learning platform for low-connectivity settings; 39,803 commits. Re-verified first-hand this pass | The only MIT general platform — AI can embed directly, but must run on-device or batch-sync. **README describes no AI features**; the platform is the delivery substrate, the agent is yours |
| Tutor | https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | p315 | Docker-based Open edX distribution | How you actually stand up Open edX in an engagement; the plugin system is the clean AI insertion point — and how `openedx-ai-extensions` installs |
| OpenEduCat | https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 889 | p315 | Education ERP on the Odoo framework — SIS, LMS, finance, HR, CRM | The Odoo-of-education: admin-side agents (enrolment, scheduling, fee chasing) rather than tutoring |
| Frappe Education | https://github.com/frappe/education | GPL-3.0 | 669 | p316 | School management system on the Frappe/ERPNext framework; 1,095 commits | ERPNext-shop clients already run the framework; GPL-3.0 confirmed from `license.txt`, not assumed |
| RosarioSIS | https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 647 | p316 | K-12 Student Information System (PHP + PostgreSQL/MySQL); 8,034 commits | A real, maintained open source SIS. **GPL-2.0** — the only v2 licence in this KB; keep agents external |
| OpenOLAT | https://github.com/OpenOLAT/OpenOLAT | **Apache-2.0** | 448 | p317 | Web-based LMS for teaching, learning, assessment and communication; 31,877 commits; frentix GmbH, from the University of Zurich's OLAT 7.1 | **The most permissively licensed mature LMS in this KB.** Agent code can link directly — no LTI boundary required. See P8 in `compose/patterns.md` |
| Richie | https://github.com/openfun/richie | MIT | 316 | p315 | Education-portal CMS (France Université Numérique) | MIT front end over an AGPL Open edX back end — the licence-safe catalogue/portal layer |
| freelingo | https://github.com/artcc/freelingo | AGPL-3.0 | 188 | p316 | Self-hosted AI language-learning platform: CEFR study plans, AI tutor, voice, flashcards, spaced repetition; 1,168 commits | A complete AI-native vertical to study or fork — AGPL, so fork consciously |
| H5P | https://github.com/h5p/h5p-php-library | GPL-3.0 | 151 | p315 | Interactive content types embedded in Moodle/Open edX/Canvas | Generate H5P content JSON with an agent; the renderer stays untouched, so GPL stays contained |
| mentingo | https://github.com/Selleo/mentingo | MIT | 96 | p316 | Open-source AI-native LMS with an AI mentor and role-play, self-hostable; 1,348 commits | The first MIT AI-native LMS in this KB — small, but licence-clean |
| Sunbird | https://github.com/Sunbird-Ed/SunbirdEd-portal | MIT | 41 | p315 | Portal of India's national digital-education stack | The base for an APAC public-sector engagement; see the caveat in `repos/foundations.md` |
| openedx-ai-extensions | https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | p318 | **Official Open edX AI plugin**, built by eduNEXT (Bogotá) as FC-111; 703 commits, 11 forks; docs v2.6.0 dated 2026-09-01. Multi-provider via **LiteLLM** (OpenAI, Anthropic, Gemini, local models); Learning + Authoring MFE integration, content summarisation, config-driven workflows, XBlock AI service registration | **LATAM-authored — and explicitly not production-ready.** See below |

## openedx-ai-extensions: the LATAM gap is no longer empty, and the row is still not shippable

Six passes of this KB have declared the same gap: **no LATAM-authored open source education
infrastructure.** Pass 318 found it, and in the least star-visible place possible.

`openedx/openedx-ai-extensions` is an `edx-platform` plugin housing tools and helpers for working
with AI. It sits under the **official `openedx` GitHub organisation**, is covered by the Open edX
maintainers programme, and its README states it was **"developed by edunext as part of FC-111"** —
FC-111 being an Open edX funded-contribution project. It has **703 commits** and its documentation
is published on `docs.openedx.org` at **version 2.6.0, changelog dated 2026-09-01** (1.0.0 was
2025-12-24). Architecture decision records cover dynamic workflow configuration, LLM caching
strategy and XBlock AI service registration. It installs through Tutor.

**eduNEXT is headquartered in Bogotá, Colombia.** Its co-founders, Felipe Montoya and Juan Camilo
Montoya, have been named Open edX core committers since at least the 2021 Core Contributor pledge,
and the company describes 12+ years of contribution to the platform. *(Provenance note: the Bogotá
location is sourced from a vendor-profile directory and the co-founder's own regional LinkedIn
profile, not from an official eduNEXT corporate page, which this session could not retrieve. The
Open edX core-committer relationship is documented in the Open edX wiki. Treat the headquarters as
well-supported, not primary-sourced.)*

**Three things a studio lead must hold at once:**

1. **The gap is closed in the sense that mattered.** This KB's LATAM finding has been "high
   consumption, zero authorship" for five passes, with the Linux Foundation's 65%/46% figures for
   Mexico and Brazil as the backdrop. That sentence is now wrong. A Colombian company is the named
   author of the official AI extension layer for one of the world's two largest open source LMS
   platforms. **For a LATAM engagement this is a credibility asset before it is a technical one.**
2. **It is explicitly not usable in production.** The README states: *"This plugin is in active
   development and should not be used in production environments."* It is labelled Experimental
   throughout and self-describes as a proof-of-concept. Nothing in this KB's patterns should depend
   on it this quarter.
3. **It is AGPL-3.0**, like the platform it extends. So it changes nothing about the architectural
   boundary: Globant's own agent code still belongs on the far side of it.

**What to do with it now:** treat it as the reference for *how Open edX intends AI to be
extended* — the XBlock AI service registration pattern and the LiteLLM provider abstraction are
the platform's own answers, and building against those shapes is cheaper than inventing a parallel
one that the platform later contradicts. Track its releases. The moment it drops "experimental",
every Open edX engagement's AI integration estimate changes.

## Moodle ships its own AI subsystem now — check it before proposing a tutor

Moodle's core **AI subsystem** (since 4.5, documented through 5.3) is not a plugin a client has to
find; it is in the platform. Two concepts matter when scoping:

- **Providers** — in **Moodle 5.1** the documented set is **Azure AI, DeepSeek, Ollama API and
  OpenAI API**, with **DeepSeek new in 5.1**. Because the OpenAI API shape is the de facto
  standard, self-hosted gateways such as LiteLLM or LocalAI can be wired in through the OpenAI
  provider — which is the practical route to an on-premise Moodle deployment with no third-party
  data egress (and see the COPPA finding in `intel/market.md`, which makes that route a compliance
  requirement rather than a preference for US K-12).
- **Placements** — where AI actions surface in the UI. Secondary sources report **two core
  placements, the text editor and course support**; this could not be confirmed against the
  official placements documentation this pass and should be verified before it goes in a proposal.

*(Dating note: the Moodle 5.3 documentation is marked work-in-progress targeted at 2026-10-05, so
the 5.x docs are moving. Cite the version-specific docs page, not "Moodle docs".)*

**The commercial read is the same as Project Athena's.** The incumbent platform ships the obvious
AI feature for free to its installed base. Summarisation and a chat box inside Moodle are not a
deliverable any more. The deterministic pedagogy layer, the governance and audit layer, and
on-premise operation still are.

## The licence-verification finding — and it should change how candidates get sourced

Pass 318 sourced platform candidates partly from "best open source LMS 2026" comparison articles.
**Three of those articles' licence claims were checked first-hand and all three were wrong, all in
the same direction — overstating permissiveness:**

| Claimed in a comparison article | Actual, read off the repo | Delta |
|---|---|---|
| LearnHouse — "Apache-2.0" | **AGPL-3.0** plus a separate Enterprise Licence | Permissive → strong copyleft + open-core |
| Frappe Learning — "MIT licence with self-hosted data ownership" | **AGPL-3.0** (`frappe/lms`) | Permissive → strong copyleft |
| Forma LMS — "Apache 2.0" | **No LICENSE file in the GitHub repo at all** (37 ★, 7,494 commits, self-described "mirror repository") | Permissive → unlicensed; default copyright |

Together with `ahmedEid1/lumen` — whose README badge says MIT while its `LICENSE` file is GPL-3.0
(see `agents/top.md`) — that is **four licence misstatements verified in a single pass**, three of
them from secondary sources and one from a repo's own README.

**The rule this KB should now state explicitly: a licence is only ever read from the repository's
LICENSE file or the licence GitHub itself renders. Never from a comparison article, never from a
badge, never from a sidebar that shows a bare "License" link.** An engagement that inherits an AGPL
obligation because someone trusted a listicle is a legal problem, not a research one.

**`formalms/formalms` is therefore rejected**, not merely unverified: an unlicensed mirror of a
7,494-commit PHP LMS is unusable regardless of what forma.lms publishes elsewhere on its own site.

## OpenOLAT remains the crack in the copyleft-platform rule

Unchanged from pass 317 and still the most useful single fact in this file for a greenfield or
EMEA-sovereign engagement: **`OpenOLAT/OpenOLAT` is Apache-2.0 with 31,877 commits** — a mature,
institution-grade LMS from frentix GmbH (Switzerland), based on the University of Zurich's OLAT
7.1. It is the only **EMEA-authored, EMEA-maintained, permissively licensed** LMS here, which lands
directly on the EMEA sovereignty requirement in `intel/market.md`.

**Read the licence file, not the sidebar.** The sidebar shows a bare "License" link with no name;
the `LICENSE` file is the full Apache-2.0 text followed by two provenance statements crediting the
University of Zurich's OLAT Zentrum and the OpenOLAT community/frentix GmbH. **Those are
NOTICE-tradition attribution statements, not additional licence terms** — the grant is Apache-2.0.

It is the one real LMS where this KB's standing architectural tax — agent code on the far side of
an LTI boundary — is **optional**. See **P8** in `compose/patterns.md`. Do not oversell it: 448 ★
against Moodle's 7.5k is not market share, and no client is migrating off Canvas to it.

## Canvas, Project Athena, and the competitive read

**Instructure announced Project Athena on 2026-07-22** — an AI study coach grounded in the
student's own Canvas course context, the first project of its "Instructure Foundry" venture,
positioned as coaching "toward mastery, not answers". It was described as under development; one
secondary report of a 7,000-student deployment at Hinds Community College could not be confirmed
against Instructure's own release and should not be repeated to a client.

The read for a studio lead: **the incumbent LMS vendor is building exactly pattern P1 natively**,
and with Moodle's core AI subsystem the same is now true at the other end of the market. Course
grounding is table stakes. Sell the deterministic pedagogy layer, the governance and audit layer,
and on-premise/offline operation.

## The licence split, recounted over 19

Permissive: **MIT (4 — Kolibri, Richie, mentingo, Sunbird)**, **Apache-2.0 (1 — OpenOLAT)**,
**ECL-2.0 (1 — Sakai, Apache-derived)** = **6 of 19**.
Copyleft: GPL-2.0 (1), GPL-3.0 (3), LGPL-3.0 (2), **AGPL-3.0 (7 — Open edX, Canvas, Tutor,
freelingo, frappe/lms, LearnHouse, openedx-ai-extensions)** = **13 of 19**.

The three platforms added this pass are all AGPL, so the ratio moved *against* permissiveness
(6/16 → 6/19) even as the agent tier moved with it. **The structural fact is unchanged and was
reinforced, not weakened, by this pass: the platform tier is copyleft; the agent tier is not.**

The consequence is concrete and identical in every region: **put Globant's agent code on the far
side of a network boundary** — LTI 1.3 tool, external service, MCP server, webhook consumer — not
inside the platform process. AGPL in particular reaches network use of a *modified* platform, so
leaving Canvas, Open edX or Moodle unmodified and talking to it over LTI keeps Globant's work
separately licensed. `pylti1.3` (MIT) is the repo that makes this practical, and
`repos/foundations.md` now names its alternatives.

## Declared gaps

- **No MENA- or Africa-originated open source platform** found. The region has the clearest named
  players of any in this KB — Alef Education, Classera, Abwaab, EIDU — and **all of them are
  proprietary.** That is a finding, not an absence: in MEA the open source story is deployment of
  global platforms and the AI layer is commercial. Note that the **UAE was first in the world with
  a nationwide mandatory K-12 AI curriculum (May 2025)**, so the demand signal is real and the
  supply is closed-source.
- **No LATAM-originated *platform*** at this tier. The LATAM finding this pass is an *extension
  layer* for a North-American-origin platform, which is a real change but not the same thing.
  Public-sector LATAM deployments still run on the platforms above, notably Kolibri.
- **Blackboard/Anthology and D2L Brightspace are closed source** and so correctly absent, but they
  are LMS incumbents a client may be running. Integration is LTI 1.3 either way.
