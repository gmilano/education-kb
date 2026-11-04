---
industry: education
region: Global
updated: 2026-11-04
---

# 🏗️ Foundational repos — Education

> The bases to build on. Verified 2026-11-04: existence via `git ls-remote --symref`, licence by reading the grant payload, stars from the repository page.
> **Read the licence column before the stars column.** Half the deployable surface in education is copyleft, and in this industry that is the constraint that decides the engagement model.

## Foundations — 8 verified rows

| Repo | Licence | Stars | Default branch | Why it is a foundation |
|---|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **AGPL-3.0** | 8,200 | `master` | The LMS behind edX (Harvard + MIT). MOOC-scale, Python/Django. Extend via XBlock rather than forking the platform. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | `main` | The most deployed LMS on earth. Mature plugin ecosystem and a built-in AI subsystem (4.5+) with pluggable providers including local Ollama. |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | 471 | `master` | The component SDK for Open edX — and the one permissively-licensed piece of that stack. This is the correct entry point for putting an agent inside Open edX. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | **457** | `main` | PyTorch knowledge-tracing library: benchmarked deep KT models over standard datasets and prediction scenarios. The reference implementation of the field. |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | `main` | Intelligent tutoring system with Bayesian Knowledge Tracing, LTI integration and a curated maths content library. UC Berkeley. |
| [openfun/richie](https://github.com/openfun/richie) | MIT | — | `master` | CMS for education portals on Django + React. Powers national MOOC portals. MIT, so maximum freedom on the front end. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | — | `master` | Lightweight LMS with deep institutional adoption across Spanish-speaking LATAM. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL-2.0** | — | `master` | Institutional HE LMS, Java/Spring. Educational Community License 2.0 — an Apache-2.0 derivative with a patent clause scoped to education. |

### Licence payloads read this pass

| Repo | Grant file | Bytes | Family |
|---|---|---|---|
| openedx/edx-platform | `LICENSE` | 35,136 | GNU Affero GPL v3 |
| moodle/moodle | `COPYING.txt` | 35,147 | GNU GPL v3 |
| openedx/XBlock | `LICENSE.TXT` | — | Apache-2.0 |
| pykt-team/pykt-toolkit | `LICENSE` | 1,066 | MIT |
| CAHLR/OATutor | `LICENSE` | 1,105 | MIT |
| openfun/richie | `LICENSE` | 1,079 | MIT |
| chamilo/chamilo-lms | `LICENSE` | 35,147 | GNU GPL v3 |
| sakaiproject/sakai | `LICENSE` | 11,120 | Educational Community License v2.0 |

## 🔴 Corrections to rows this KB previously published

| Row | Was published as | Measured 2026-11-04 | Why it matters |
|---|---|---|---|
| `openedx/edx-platform` | **Apache-2.0** | **AGPL-3.0** (payload 35,136 B, `GNU AFFERO GENERAL PUBLIC LICENSE`; GitHub sidebar agrees; README states "version 3 of the AGPL") | **The most consequential error in this knowledge base.** Apache-2.0 permits a closed proprietary derivative; AGPL-3.0 requires source disclosure *to network users*. A studio that scoped an Open edX engagement from the old cell would have mispriced the licensing position of the whole deliverable. This error was published in three separate files. |
| `sakaiproject/sakai` | Apache-2.0 | **ECL-2.0** (payload 11,120 B) | ECL-2.0 is Apache-derived and permissive in practice, but it is a distinct licence with a narrower patent grant. Not interchangeable in a contract. |
| `chamilo/chamilo-lms` | GPL-2.0 | **GPL-3.0** (payload 35,147 B) | Version matters for compatibility: GPL-2.0-only and GPL-3.0 are mutually incompatible when combining code. |
| `pykt-team/pykt-toolkit` | 1.2k ★ | **457 ★** | Inflated 2.6×. Licence (MIT) was correct. |
| `openedx/XBlock` | 468 ★ | 471 ★ | Accurate. Recorded because it is the one star count on this shelf that held. |

## 🔴 Removed — the row does not exist

| Row | Status |
|---|---|
| `OpenEduCat-Inc/OpenEduCat` | **HTTP 404.** `git ls-remote` fails to resolve it and the repository page returns 404. Three plausible renames (`OpenEduCat-Inc/openeducat_erp`, `openeducat/OpenEduCat`, `OpenEduCat-Inc/OpenEduCat-Community`) also fail to resolve. This KB was serving it as a live education-ERP foundation with "3M+ users / 100+ countries". Removed from the foundations and verticals shelves. The *product* OpenEduCat may well still exist commercially — the GitHub address this KB published does not. |

## Why these repos

### The two LMS bases — and the licence split that matters
Moodle (GPL-3.0) and Open edX (AGPL-3.0) are the deployable universe. Neither is permissive. The practical consequence:

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

- **There is no permissively-licensed, production-grade open source LMS.** Every LMS verified this pass is GPL, AGPL or ECL. Any Globant engagement that assumed a permissive LMS core was mis-scoped. The permissive surface in education is confined to components (XBlock), libraries (pyKT), front ends (Richie) and agents — not platforms.
- **Star counts for `richie`, `chamilo-lms` and `sakai` were not re-measured this pass.** Their licences were read from bytes; the star cells are left blank rather than carried forward from an unverified figure.
