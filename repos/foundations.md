---
industry: education
region: Global
updated: 2026-11-04
---

# 🏗️ Foundational repos — Education

> The bases to build on. Verified 2026-11-04: existence via `git ls-remote --symref`, licence by reading the grant payload, stars from the repository page.
> **Read the licence column before the stars column.** Half the deployable surface in education is copyleft, and in this industry that is the constraint that decides the engagement model.

## Foundations — 12 verified rows

| Repo | Licence | Stars | Default branch | Why it is a foundation |
|---|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 8,200 | `master` | The LMS behind edX (Harvard + MIT). MOOC-scale, Python/Django. Extend via XBlock rather than forking the platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | `main` | The most deployed LMS on earth. Mature plugin ecosystem and a built-in AI subsystem (4.5+) with pluggable providers including local Ollama. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,200 | **`develop`** | 🟢 **The permissive production learning platform.** Offline-first teaching and learning with no Internet requirement — content delivery, learner progress, coach tooling. 1.0k forks. The one platform-class row on this page that permits a closed derivative, and the correct base for low-connectivity deployment. ⚠️ Default branch is `develop`. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | 471 | `master` | The component SDK for Open edX — and the one permissively-licensed piece of that stack. This is the correct entry point for putting an agent inside Open edX. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | **457** | `main` | PyTorch knowledge-tracing library: benchmarked deep KT models over standard datasets and prediction scenarios. The reference implementation of the field. |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | `main` | Intelligent tutoring system with Bayesian Knowledge Tracing, LTI integration and a curated maths content library. UC Berkeley. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | **4,100** | `main` | The Free Spaced Repetition Scheduler for Anki: a scheduler that sets review timing and an optimiser that machine-learns the parameters from a learner's own review history. 🟢 **The algorithm ships inside Anki itself from v23.10** — the highest-adoption permissive education algorithm on this shelf, and the only one already proven at consumer scale. |
| [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** | 456 | `main` | FSRS in Rust: scheduler, parameter optimiser, simulation, SM-2 migration helpers, cost-policy trainer. Bindings for C, Python, Node.js, Dart and PHP in sibling repositories. This is the **embeddable engine** — the piece you link into a product. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** | 905 | **`19.0`** | Education ERP on the Odoo stack: admissions, academics, finance, HR. LGPL-3.0 is **weaker copyleft than everything else on this page** — linking from separately-licensed code is permitted provided the LGPL portion stays replaceable, which makes this a materially easier licensing position than Moodle or Open edX. ⚠️ Default branch is a bare version number and `20.0` already exists; resolve the branch, never hardcode it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | `master` | CMS for education portals on Django + React. Powers national MOOC portals. MIT, so maximum freedom on the front end. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | — | `master` | Lightweight LMS with deep institutional adoption across Spanish-speaking LATAM. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | — | `master` | Institutional HE LMS, Java/Spring. Educational Community License 2.0 — an Apache-2.0 derivative with a patent clause scoped to education. |

### Licence payloads read this pass

| Repo | Grant file | Bytes | Family |
|---|---|---|---|
| openedx/edx-platform | `LICENSE` | 35,136 | GNU Affero GPL v3 |
| moodle/moodle | `COPYING.txt` | 35,147 | GNU GPL v3 |
| openedx/XBlock | `LICENSE.TXT` | **11,358** | Apache-2.0 — canonical (11,357 B) **plus one prepended blank line**. Measured p651; the cell was previously blank. A byte-equality Apache test fails on this row, cosmetically. |
| pykt-team/pykt-toolkit | `LICENSE` | 1,066 | MIT |
| CAHLR/OATutor | `LICENSE` | 1,105 | MIT |
| openfun/richie | `LICENSE` | 1,079 | MIT |
| chamilo/chamilo-lms | `LICENSE` | 35,147 | GNU GPL v3 |
| sakaiproject/sakai | `LICENSE` | 11,120 | Educational Community License v2.0 |
| open-spaced-repetition/fsrs4anki | `LICENSE` | 1,079 | MIT |
| open-spaced-repetition/fsrs-rs | `LICENSE` | 1,509 | BSD 3-Clause |
| learningequality/kolibri | `LICENSE` | 1,097 | MIT |
| openeducat/openeducat_erp | `LICENSE` | 8,241 | GNU LGPL v3 (LGPLv3 text with the GPL appended beneath it) |

## 🔴 Corrections to rows this KB previously published

| Row | Was published as | Measured 2026-11-04 | Why it matters |
|---|---|---|---|
| `openedx/edx-platform` | **Apache-2.0** | **AGPL-3.0** (payload 35,136 B, `GNU AFFERO GENERAL PUBLIC LICENSE`; GitHub sidebar agrees; README states "version 3 of the AGPL") | **The most consequential error in this knowledge base.** Apache-2.0 permits a closed proprietary derivative; AGPL-3.0 requires source disclosure *to network users*. A studio that scoped an Open edX engagement from the old cell would have mispriced the licensing position of the whole deliverable. This error was published in three separate files. |
| `sakaiproject/sakai` | Apache-2.0 | **ECL-2.0** (payload 11,120 B) | ECL-2.0 is Apache-derived and permissive in practice, but it is a distinct licence with a narrower patent grant. Not interchangeable in a contract. |
| `chamilo/chamilo-lms` | GPL-2.0 | **GPL-3.0** (payload 35,147 B) | Version matters for compatibility: GPL-2.0-only and GPL-3.0 are mutually incompatible when combining code. |
| `pykt-team/pykt-toolkit` | 1.2k ★ | **457 ★** | Inflated 2.6×. Licence (MIT) was correct. |
| `openedx/XBlock` | 468 ★ | 471 ★ | Accurate. Recorded because it is the one star count on this shelf that held. |

## 🟢 Repaired — the row was removed from the wrong address

| Row | Status |
|---|---|
| `OpenEduCat-Inc/OpenEduCat` → **`openeducat/openeducat_erp`** | The removal was correct; the conclusion drawn from it was not. The old address is genuinely **HTTP 404** and three candidate renames (`OpenEduCat-Inc/openeducat_erp`, `openeducat/OpenEduCat`, `OpenEduCat-Inc/OpenEduCat-Community`) also fail to resolve. A **fourth** address, not among those tried, resolves on `ls-remote` with real adoption: **905 ★ / 787 forks**, LGPL-3.0 read from an 8,241 B payload, default branch `19.0`. The previous pass concluded "this KB no longer holds a verified open source education ERP" — that statement is **withdrawn**. The ERP slot is occupied, at adoption, on the most workable copyleft terms on this page. |

🔴 **Two defects inside the repaired row, both invisible to a licence-name lookup:**

1. **The grant delegates copyright attribution to a file that is not in the repository.** `LICENSE` opens *"For copyright information, please see the COPYRIGHT file."* `COPYRIGHT` returns **404** on branch `19.0`. The LGPL-3.0 terms themselves are complete and unambiguous; what is missing is the holder identification the grant points at.
2. **There is no safe way to hardcode the branch.** The default is the bare version `19.0`; `20.0` already exists; `master` also exists. Hardcoding `main`/`master` builds the wrong thing or nothing, and hardcoding today's default silently keeps building the old major. Resolve with `git ls-remote --symref` at build time.

🔵 **The lesson for this base, not for OpenEduCat:** "three plausible renames also 404" was treated as sufficient to declare a project gone. It is not. A rename probe searches the space a reader *imagines*; it does not search the space that exists. One search against the project's own name returned the live address immediately.

## Why these repos

### The LMS bases — and the licence split that matters
Moodle (GPL-3.0) and Open edX (AGPL-3.0) are the deployable universe **for institutional course management**. Neither is permissive. Kolibri (MIT) is permissive but is a different class of system — offline-first learning delivery, not enrolment-and-gradebook at institutional scale. Pick by what the client actually needs to run, not by licence alone. The practical consequence for the two copyleft bases:

- **Moodle, GPL-3.0** — plugins are derivative works and must be GPL-3.0 on distribution. A plugin *operated as a service* for one client triggers no distribution, so client-specific work is normally fine; a product sold to many is not.
- **Open edX, AGPL-3.0** — the network clause bites. Running a modified Open edX as a SaaS obliges you to offer modified source to its users. **Build in XBlocks (Apache-2.0), not in platform forks**, and the obligation stays contained.

This is the single most important architectural fact on this page, and it is why `openedx/XBlock` matters out of proportion to its 471 stars.

### Knowledge tracing (pyKT)
The standard toolkit for modelling what a learner knows: predicts future performance, exposes skill gaps, drives adaptive sequencing. At 457 stars it is a research-grade library, not a platform — budget integration effort accordingly.

### Tutoring systems (OATutor)
MIT, peer-reviewed, LTI-integrated, with real content. The low-risk starting point when a client wants explainable mastery estimates rather than open-ended dialogue.

### Permissive front end (Richie)
MIT and decoupled, so the learner-facing portal can be built and sold without inheriting LMS copyleft. Useful as the presentation layer over a GPL/AGPL core.

## 🔴 Open gaps on this page

- 🔴 **A claim this page published is withdrawn.** This page asserted that "there is no permissively-licensed, production-grade open source LMS". **`learningequality/kolibri` is MIT, 1.2k ★ / 1.0k forks, and production-grade** — the payload was read at p651. The accurate statement is narrower: *there is no permissive platform of the Moodle/Open edX class*, i.e. institutional course management with enrolment at scale, gradebook, SIS integration and a large plugin ecosystem. That remains true and is why the XBlock containment pattern matters. But for offline-first learning delivery there is a permissive, adopted platform, and engagements in low-connectivity markets should start from it rather than from a copyleft base. See `verticals/solutions.md` for the full correction and why the error persisted across passes.
- 🟢 **The permissive surface did grow in one specific place: review scheduling.** `fsrs4anki` (MIT) and `fsrs-rs` (BSD-3-Clause) close a hole this page has carried from the start — the base had knowledge tracing (does the learner know X?) and nothing for scheduling (when should they see X again?). FSRS is the rare case of a permissive education algorithm already in mainstream production software rather than awaiting integration.
- **Star counts for `richie`, `chamilo-lms` and `sakai` have not been re-measured.** Their licences were read from bytes; the star cells stay blank rather than carry forward an unverified figure. p651 did not close this either — it is a third consecutive pass leaving these three blank, and it is cheap to fix.
- **`openedx/edx-platform`, `moodle/moodle` and `openedx/XBlock` star counts are also carried from the p650 measurement**, not re-measured at p651. Only the licence payloads were re-read this pass (and all reproduced byte-exactly).
