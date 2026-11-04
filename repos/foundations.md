---
industry: education
region: Global
updated: 2026-11-04
---

# 🏗️ Foundational repos — Education

> The bases to build on. Verified 2026-11-04: existence via `git ls-remote --symref`, licence by reading the grant payload, stars from the repository page.
> **Read the licence column before the stars column.** Half the deployable surface in education is copyleft, and in this industry that is the constraint that decides the engagement model.

## Foundations — 15 verified rows

| Repo | Licence | Stars | Default branch | Why it is a foundation |
|---|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 8,200 | `master` | The LMS behind edX (Harvard + MIT). MOOC-scale, Python/Django. Extend via XBlock rather than forking the platform. **Re-measured p652: 8.2k ★ / 4.4k forks — reproduces.** |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | `main` | The most deployed LMS on earth. Mature plugin ecosystem and a built-in AI subsystem (4.5+) with pluggable providers including local Ollama. **Re-measured p652: 7.6k ★ / 7.7k forks — reproduces.** 🔵 The only row on this shelf with *more forks than stars*, which is a fair description of what Moodle is: not a project people watch, a codebase institutions take copies of. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | **449** | `master` | 🟢 **The permissive institutional LMS — the row that withdraws this page's longest-standing claim.** Institutional course management (courses, enrolment, assessment, QTI testing, portfolio, curriculum management) under **Apache-2.0**, so a closed derivative is permitted. **167 forks / 32,210 commits**, release branches `OpenOLAT_18.0` → `OpenOLAT_21.1`, latest tag `OpenOLAT_21.1.2`. Java/Spring, Hibernate 7.4.14, descended from the University of Zurich's OLAT 7.1, maintained by frentix GmbH (Zurich) — EMEA on the evidence of its own grant payload. 🟢 **The LLM plumbing is already in `pom.xml`**: `langchain4j` 1.23.0 (Apache-2.0) with `-open-ai`, `-anthropic` and `-embeddings`, alongside Apache Lucene. ⚠ One copyleft item in 270 dependencies — the optional MySQL Connector/J (GPL-2.0 + FOSS Exception); use the in-tree PostgreSQL driver (BSD-2-Clause) for a closed derivative. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,200 | **`develop`** | 🟢 **The permissive production learning platform.** Offline-first teaching and learning with no Internet requirement — content delivery, learner progress, coach tooling. 1.0k forks. The one platform-class row on this page that permits a closed derivative, and the correct base for low-connectivity deployment. ⚠️ Default branch is `develop`. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | 471 | `master` | The component SDK for Open edX — and the one permissively-licensed piece of that stack. This is the correct entry point for putting an agent inside Open edX. **Re-measured p652: 471 ★ / 231 forks — reproduces exactly.** |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | **457** | `main` | PyTorch knowledge-tracing library: benchmarked deep KT models over standard datasets and prediction scenarios. The reference implementation of the field. |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | `main` | Intelligent tutoring system with Bayesian Knowledge Tracing, LTI integration and a curated maths content library. UC Berkeley. |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki) | **MIT** | **4,100** | `main` | The Free Spaced Repetition Scheduler for Anki: a scheduler that sets review timing and an optimiser that machine-learns the parameters from a learner's own review history. 🟢 **The algorithm ships inside Anki itself from v23.10** — the highest-adoption permissive education algorithm on this shelf, and the only one already proven at consumer scale. |
| [open-spaced-repetition/fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs) | **BSD-3-Clause** | 456 | `main` | FSRS in Rust: scheduler, parameter optimiser, simulation, SM-2 migration helpers, cost-policy trainer. Bindings for C, Python, Node.js, Dart and PHP in sibling repositories. This is the **embeddable engine** — the piece you link into a product. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | **LGPL-3.0** | 905 | **`19.0`** | Education ERP on the Odoo stack: admissions, academics, finance, HR. LGPL-3.0 is **weaker copyleft than everything else on this page** — linking from separately-licensed code is permitted provided the LGPL portion stays replaceable, which makes this a materially easier licensing position than Moodle or Open edX. ⚠️ Default branch is a bare version number and `20.0` already exists; resolve the branch, never hardcode it. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | **318** | `master` | CMS for education portals on Django + React. Powers national MOOC portals. MIT, so maximum freedom on the front end. 94 forks. 🟢 Star cell measured at p652 after three passes blank.
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | **1,000** | `master` | Lightweight LMS with deep institutional adoption across Spanish-speaking LATAM. 567 forks. 🟢 Star cell measured at p652 after three passes blank. |
| [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | **MIT** | **41,100** | `main` | 🟢 **The largest permissive education asset this base has found — and it is curriculum, not software.** 93+ runnable projects on LLMs, RAG, agents and MCP, tiered beginner (22) / intermediate (48) / advanced (23), plus an `ai-engineering-roadmap` learning path. 6.6k forks, 554 commits. Filed deliberately with its nature stated: **the AI-literacy mandates this KB tracks create demand for curriculum, and a client cannot buy curriculum from a tutoring agent.** MIT means a Globant derivative can be commercial and closed — the decisive contrast with `education-agent-skills` (949★, CC BY-SA 4.0 ShareAlike, declined at p651). See `compose/patterns.md` **P10**. |
| [microsoft/LLM-Rubric](https://github.com/microsoft/LLM-Rubric) | **MIT** | 45 | `main` | 🟡 **The nearest permissive primitive to this base's assessment gap, and it is not an education tool.** A hand-written rubric defines dimensions; an LLM answers each question; a small neural network calibrates those outputs against human judges' ratings to predict an overall score. Validated on dialogue systems (naturalness, conciseness, citation quality). ACL 2024, Microsoft, 9 forks, 22 commits. **45★ is research-grade adoption and the row says so** — it is filed because *calibration to human raters* is the transferable mechanism, and because every education-specific grader found in three passes is unlicensed or self-contradictory. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | **1,200** | `master` | Institutional HE LMS, Java/Spring. Educational Community License 2.0 — an Apache-2.0 derivative with a patent clause scoped to education. ~1.0k forks; README describes `master` as "the most current development release, Sakai 24". 🟢 Star cell measured at p652 after three passes blank. |

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
| patchy631/ai-engineering-hub | `LICENSE` | 1,066 | MIT — `Copyright (c) 2024 patchy631` |
| microsoft/LLM-Rubric | `LICENSE` | 1,141 | MIT — `Copyright (c) Microsoft Corporation.` |
| 🔴 frappe/education | `license.txt` | **19** | **Not a licence.** Entire contents: `License: GNU GPL V3`. `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` all 404 on the real default branch (`develop`). Intent is unambiguous; the grant is nineteen bytes with no permission paragraph, no conditions, no warranty disclaimer and no copyright holder. **Not filed as a foundation** — see `repos/trending.md` (p652). |
| open-spaced-repetition/fsrs4anki | `LICENSE` | 1,079 | MIT |
| open-spaced-repetition/fsrs-rs | `LICENSE` | 1,509 | BSD 3-Clause |
| learningequality/kolibri | `LICENSE` | 1,097 | MIT |
| OpenOLAT/OpenOLAT | `LICENSE` | **10,982** | Apache-2.0 — nine substantive sections all present and unmodified. Canonical **−375 B**, fully explained: the `APPENDIX` (boilerplate instructions, not terms) is replaced by two provenance statements naming the University of Zurich OLAT Zentrum and frentix GmbH. |
| langchain4j/langchain4j | `LICENSE` | **11,357** | Apache-2.0 — byte-exact canonical. Read because it is OpenOlat's in-tree LLM layer and therefore part of that row's licence position. |
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

- 🔴 **The same claim is now withdrawn twice, and at p653 it is withdrawn entirely.** This page first asserted *"there is no permissively-licensed, production-grade open source LMS"*; p651 narrowed that to *"there is no permissive platform of the Moodle/Open edX class"* after Kolibri (MIT, 1.2k ★) turned out to be a production offline-first platform. **The narrowed claim is also false. `OpenOLAT/OpenOLAT` is Apache-2.0 (10,982 B read from bytes), 449 ★ / 167 forks / 32,210 commits, and is institutional course management** — courses, enrolment, assessment, QTI, portfolio, curriculum management, the LMS of record across much of German-speaking European higher education. There is no surviving version of this claim and this page should stop making it. 🔵 **The instrument was the problem, not the search.** Every pass ranked the platform shelf by stars; OpenOlat's star:commit ratio is **1:72**, so an adoption-ordered channel buries it beneath tutorial repositories. This page already knew that institutional software is under-starred — it says so about Moodle's forks exceeding its stars — and did not apply the lesson to its own ranking. The row came back from a **licence-first** query, not an adoption-first one. What survives, and still shapes most engagements: the platform a client *already runs* is almost always copyleft, so XBlock containment and out-of-tree agents remain the common case; OpenOlat changes the **greenfield** choice, not the installed base. But for offline-first learning delivery there is a permissive, adopted platform, and engagements in low-connectivity markets should start from it rather than from a copyleft base. See `verticals/solutions.md` for the full correction and why the error persisted across passes.
- 🟢 **The permissive surface did grow in one specific place: review scheduling.** `fsrs4anki` (MIT) and `fsrs-rs` (BSD-3-Clause) close a hole this page has carried from the start — the base had knowledge tracing (does the learner know X?) and nothing for scheduling (when should they see X again?). FSRS is the rare case of a permissive education algorithm already in mainstream production software rather than awaiting integration.
- 🟢 **Closed at p652: the three blank star cells.** `richie` **318**, `chamilo-lms` **1.0k**, `sakai` **1.2k**, all measured from the repository page on 2026-11-04 after three consecutive passes of this page flagging it as cheap and not doing it. The flag was right about the cost: it took one batch.
- 🟢 **Closed at p652: the three carried star cells.** `edx-platform` (8.2k), `moodle` (7.6k) and `XBlock` (471) were carried from p650 and are now re-measured. **All three reproduce**, and so does `kolibri` (1.2k ★, MIT, default branch `develop`) from p651. **Four re-measures, four reproductions, including one unusual default branch.** That confirms p651's diagnosis: this KB's historic inflation came from values carried forward out of an unverified pipeline, not from faulty measurement. The discipline worth keeping is re-measuring on a stated date — not avoiding numbers.
- 🔴 **A fifth grant-defect class, found at p652: a grant that names a licence instead of being one.** `frappe/education` carries a **19-byte** `license.txt` reading `License: GNU GPL V3` and nothing else, with all four conventional filenames 404 on its real default branch (`develop`). Catalogued alongside the four classes this base already holds — grant absent while a README asserts permissiveness; grant complete but delegating to a missing `COPYRIGHT`; grant complete but contradicted by the README (`protorubric`: Apache-2.0 payload, MIT README); and grant complete and permissive but not covering the artefact that matters (`Omni-Edu`: Apache-2.0 code, unnamed weight licence). **Four of the five would pass a licence-badge check.** The lesson is not "read LICENSE" — this page already does that — it is **read the manifests, and for a model read the weight card.**
- 🟡 **The licence split on this page is now 11 permissive rows against 4 copyleft — and at p653 it finally does help where it matters.** Counted from the table: 9 rows are MIT, Apache-2.0 or BSD-3-Clause, plus `sakai` under ECL-2.0, an Apache-2.0 derivative; the 4 copyleft rows are `edx-platform` (AGPL-3.0), `moodle` and `chamilo-lms` (GPL-3.0) and `openeducat_erp` (LGPL-3.0). **Until p653 this ratio was misleading and was recorded here so it would not be quoted as good news** — all 4 copyleft rows were *platforms*, and the permissive majority was libraries, components, a scheduler, a model and curriculum. **That caveat no longer holds in full.** `OpenOlat` is a permissive row that *is* a platform of the institutional class, so the accurate statement is now: for institutional course management at scale the options are AGPL-3.0, GPL-3.0, LGPL-3.0, ECL-2.0 **or Apache-2.0**. The remaining asymmetry is ecosystem, not licence — Moodle's plugin marketplace and installed base have no permissive equivalent, and that is what should be priced, rather than the licence. What *has* changed is that the permissive surface now extends across three non-platform layers — the model (`Omni-Edu`, Apache-2.0 code), the scheduler (`fsrs-rs`, BSD-3-Clause; `fsrs4anki`, MIT), and the curriculum (`ai-engineering-hub`, MIT) — so a commercial deliverable can be assembled permissively **around** a copyleft platform the client already runs. That is the actual engagement shape, and `compose/patterns.md` P2, P3 and P7 are built on it.
