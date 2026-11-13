---
industry: education
region: Global
updated: 2026-11-13
---

# Foundational open-source repos for education

The platforms and libraries an education engagement actually builds on. **30
repos**, all verified from the rendered repository page (license field + star
count) — 26 on 2026-11-13 plus **4 new LTI 1.3 libraries verified this pass**.
Grouped by the job they do, because "foundational" in education means five
different layers: the LMS, the student record, the content format, the
learning-data/ML layer, and **the integration layer that mounts anything into
anything**.

License matters more here than anywhere else in this KB: the big three LMSs are
**AGPL-3.0 or GPL-3.0**, which governs what a studio can hand a client as a
derived product. The MIT/Apache/BSD/ECL rows are the ones that compose freely.

**What changed this pass:** this file previously declared "no open-source LTI
1.3 tool-provider library made the verified set" and called it greenfield.
**That gap is closed and the conclusion was wrong.** Four LTI 1.3 libraries
verified below, led by `ltijs` (Apache-2.0, 373 stars) implementing the full
LTI Advantage service set. Do not quote the old greenfield claim to a client.

## The integration layer — LTI 1.3 (new this pass)

Build the AI tool once as an LTI 1.3 tool provider and it mounts in Moodle,
Canvas, Open edX, Sakai and ILIAS. This is the highest-leverage single
investment in an education engagement, and it does **not** need to be written
from scratch.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | **The reference implementation.** Node.js; covers launches, Deep Linking, Assignment and Grade Services, Names and Role Provisioning, and Dynamic Registration — the complete LTI Advantage surface. v7 is a full rewrite with a migration guide from v5. 86 forks. README thanks CourseKey for making "the certification process possible" but **does not itself claim LTI Advantage certification** — a fork, `edugatorlabs/ltijs`, is the one advertising certified status. Verify certification claims before repeating them to a client. |
| https://github.com/packbackbooks/lti-1-3-php-library | Apache-2.0 | 54 | **The PHP answer** — matters because Moodle and Chamilo are PHP shops. Validates launches from any LTI consumer and uses Names & Roles Provisioning for rosters and Assignment & Grades for grade writeback. 27 forks. |
| https://github.com/Simon-Initiative/lti_1p3 | MIT | 16 | Elixir library for LTI 1.3 **both as Tool and as Platform**. Built to support the Open Learning Initiative's next-generation platform, Torus — i.e. production provenance, not a toy. 4 forks. |
| https://github.com/lti-tool/lti-tool | MIT | 8 | **Serverless-native** LTI 1.3 toolkit (TypeScript) for AWS Lambda and Cloudflare Workers, Hono-first. OIDC, AGS, NRPS, Deep Linking, Dynamic Registration, JWT verification and nonce validation; pluggable storage (memory, DynamoDB, PostgreSQL, MySQL, Cloudflare D1). Early at 8 stars and its README is internally inconsistent about which frameworks are supported versus planned — but it is the only serverless-shaped option found. |

**Leads deliberately not tabled** (surfaced in search, not adopted):
`SanDiegoCodeSchool/lti-node-library` (MIT, metadata indicates ~7 years old —
likely stale, and its README admits only limited Assignment & Grade Services
support); `bnsoftware/lti-1p3-tool`, a PHP fork whose **own README says "you
should not use this library at this time"**; `stevenweathers/peregrine-lti`
(Go), explicitly pre-v1.0 with an unstable public API. None were
license-verified on the repository page this pass; treat all three as
unverified.

## The learner-record layer — xAPI Learning Record Stores (new this pass)

Every compose pattern in this KB instructs the agent to "emit xAPI", and until
this pass **no repo in this base implemented the thing that receives it**. Both
options below are **permissive**, which makes this the second fully build-safe
layer in the education stack after the LTI table — and unlike the LMS layer,
here the permissive option is also the leading one.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/yetanalytics/lrsql | Apache-2.0 | 144 | **The default choice.** SQL-based LRS: a persistent store for xAPI statements plus their attachments and documents. Verified DBMS matrix is broad and current — SQLite 3.42, **Postgres 14/15/16/17/18**, MariaDB 10.6–11.8, MySQL 8.0.44/8.4/9.5. **Apache-2.0 means the learner-record store can ship inside a client deliverable with no copyleft reach** — the only data-layer component in this KB for which that is true. 42 forks. |
| https://github.com/openfun/ralph | MIT | 51 | LRS **plus** a CLI for building learning-analytics pipelines **plus** a Python library for fetching, converting and serializing learning events. Pick it over SQL LRS when the engagement is *analytics*-shaped rather than *storage*-shaped, or when the agent layer is Python and you want one language end to end. Elasticsearch backend in its documented local setup. From **France Université Numérique** — EMEA public-education provenance, which is usable evidence in an EU data-sovereignty conversation. 19 forks. Releases section empty. |

Pair either one with `DavidLMS/learnmcp-xapi` (MIT, 16 stars — see
`agents/top.md`), the MCP server that lets an agent read and write these records
directly. That three-repo stack — LRS + MCP server + agent — is written up as
pattern `P9`.

## Learning platforms (LMS / MOOC)

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/openedx/openedx-platform | AGPL-3.0 | 8.2k | Open edX LMS & Studio. **Formerly `openedx/edx-platform`** — that path now serves this repo; use this name. Stewarded by the nonprofit Harvard and MIT founded. |
| https://github.com/moodle/moodle | GPL-3.0 | 7.6k | The world's most deployed LMS. Plugin architecture is the integration surface. |
| https://github.com/instructure/canvas-lms | AGPL-3.0 | 6.9k | The open LMS by Instructure; dominant in North American higher ed. Pair with `canvas-mcp` for agent access. |
| https://github.com/frappe/lms | AGPL-3.0 | 3.4k | Modern, lightweight LMS on the Frappe framework. Fastest to stand up of the group. |
| https://github.com/overhangio/tutor | AGPL-3.0 | 1.1k | Docker-based Open edX distribution. In practice this is *how* you deploy Open edX. |
| https://github.com/sakaiproject/sakai | ECL-2.0 | 1.2k | Higher-ed teaching/research/collaboration suite. **ECL-2.0 is Apache-2.0 with a patent clause tuned for universities** — permissive, and the friendliest license in this table. |
| https://github.com/chamilo/chamilo-lms | GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility; strong LATAM and francophone footprint. |
| https://github.com/ILIAS-eLearning/ILIAS | GPL-3.0 | 510 | Long-lived German LMS; heavy use in EMEA public sector and military/vocational training. |

## Student information systems and institutional ERP

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/openeducat/openeducat_erp | LGPL-3.0 | 911 | SIS + LMS + finance modules as Odoo apps. The "Odoo for education" answer. |
| https://github.com/frappe/education | GPL-3.0 | 707 | **New this pass.** Education suite on the Frappe framework: admissions, fees, scheduling, exams, attendance. Shares a stack with `frappe/lms` (AGPL-3.0) and ERPNext, so a Frappe client can run SIS + LMS + ERP on one framework. **License read from `license.txt` ("GNU GPL V3") because GitHub's sidebar shows only a generic License link** — and note it differs from `frappe/lms`, which is AGPL-3.0. Branches version-15.1 / 15.2 / 16 / develop; Releases empty. |
| https://github.com/francoisjacquet/rosariosis | GPL-2.0 | 654 | RosarioSIS student information system for school management. Widely used in LATAM K-12. |
| https://github.com/GibbonEdu/core | GPL-3.0 | 638 | Flexible open-source school management platform. |
| https://github.com/OS4ED/openSIS-Classic | GPL (per README) | 351 | openSIS student information system. Sidebar shows no license badge; GPL claim comes from the README. |

## Content, authoring and delivery

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/ankitects/anki | AGPL-3.0 | 32.8k | Spaced-repetition engine. License read from the `LICENSE` file — GitHub's sidebar does not name it. The scheduling algorithm is the reusable asset. |
| https://github.com/bigbluebutton/bigbluebutton | LGPL-3.0 | 9.3k | Web conferencing built for virtual classes; LTI into Moodle/Canvas. |
| https://github.com/oppia/oppia | Apache-2.0 | 7.0k | Free online learning platform with interactive explorations. **Apache-2.0 — permissive and substantial.** |
| https://github.com/Khan/perseus | MIT | 1.6k | Khan Academy's exercise question editor and renderer. **MIT** — the cleanest way to get real exercise rendering into a product. |
| https://github.com/learningequality/kolibri | MIT | 1.2k | Offline-first learning platform for low-connectivity settings. **MIT**, and the reference implementation for offline education. |
| https://github.com/opencast/opencast | ECL-2.0 | 511 | Automated lecture capture and video distribution at scale. |
| https://github.com/h5p/h5p-php-library | GPL-3.0 | 155 | Framework-agnostic H5P interactive content library. H5P is the de facto interactive-content format across Moodle/Canvas/Open edX. |
| https://github.com/learningequality/kolibri-design-system | No license shown | 53 | Kolibri's design system. Listed for completeness; **no license on the page**, so treat as unlicensed until confirmed. |

## Learning data, ML and assessment infrastructure

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/jupyterhub/jupyterhub | BSD-3-Clause | 8.4k | Multi-user Jupyter server. The backbone of university CS/data-science teaching. |
| https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | Assigning and autograding notebooks. **The autograding layer to wrap an agent around.** |
| https://github.com/pykt-team/pykt-toolkit | MIT | 461 | pyKT: benchmark library for deep-learning knowledge-tracing models. **MIT** — the quantitative learner-modelling layer that LLM tutors usually lack. |
| https://github.com/getodk/collect | Apache-2.0 | 805 | Android app for offline form data collection; used for education field surveys and assessment at scale in low-connectivity regions. |
| https://github.com/openedx/openedx-ai-extensions | AGPL-3.0 | 17 | Open edX plugin housing AI tools and helpers. Early (17 stars) but it is the *official* AI extension point for Open edX. |
| https://github.com/1edtech/caliper-spec | IMS Global Specification Document License | 22 | Caliper Analytics spec — organizing and exchanging learning activity data. **Spec-document license, not a software license**: implement the spec, do not vendor the repo. |

## Interoperability standards worth knowing (not all are code repos)

- **LTI 1.3 / LTI Advantage** (1EdTech) — how any tool mounts inside Moodle,
  Canvas, Open edX, Sakai, ILIAS. **Implementations now verified above**; see
  the LTI table rather than planning a from-scratch build.
- **xAPI (Experience API)** and **Caliper Analytics** — the two learning-event
  telemetry standards. Emit one of them from any agent you build, or the
  institution cannot report on it. **As of this pass xAPI has verified open
  implementations in this KB** (`yetanalytics/lrsql`, `openfun/ralph`, and
  `DavidLMS/learnmcp-xapi` on the agent side); Caliper still has only its spec
  repo, so **xAPI is the lower-risk choice wherever the client has no prior
  contractual commitment**.
- **QTI** — assessment item interchange. Matters the moment a client wants to
  move an item bank between systems.
- **SCORM** — legacy but ubiquitous in corporate and vocational training; still
  the delivery format many EMEA/APAC clients require.

## Declared gaps

- **Caliper has no verified open implementation here — new gap this pass, opened
  by closing the xAPI one.** `1edtech/caliper-spec` carries a spec-document
  license, not a software license. Caliper is the 1EdTech-native option and is
  most often specified in **North American higher ed**, so an engagement
  contractually bound to Caliper rather than xAPI has **no open starting point
  in this base**. That is a build, and it must be priced as one.
- **No permissively licensed full LMS exists at scale.** Every LMS with real
  deployment is GPL/AGPL except Sakai (ECL-2.0). A client who needs a
  proprietary derived platform cannot start from Moodle, Canvas, or Open edX —
  that constraint should be surfaced in week one, not month three.
- **No LTI 1.3 library in Python.** The verified set is Node/TypeScript (×2),
  PHP, and Elixir. Since almost every AI agent layer in this KB is Python
  (DeepTutor, educhain, Faixiang's Moodle MCP, AI_AWE, pyKT), the standard
  architecture is forced into a two-process shape: Python agent service behind a
  Node or PHP LTI front door. Worth knowing before estimating. A Python LTI 1.3
  tool-provider library remains genuinely greenfield.
- **No open-source QTI item-bank toolchain surfaced.** QTI is named in every
  procurement document and no foundational repo for it reached this set.
  Unverified this pass rather than confirmed absent — it needs a dedicated
  search.
