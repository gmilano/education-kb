---
industry: education
region: Global
updated: 2026-11-13
---

# Foundational open-source repos for education

The platforms and libraries an education engagement actually builds on. **47
repos**, all verified from the rendered repository page (license field + star
count) — 34 across the four earlier passes on 2026-11-13, plus **the six-repo
Caliper Analytics layer and the seven-repo QTI assessment layer verified this
pass**. 🔴 **Where GitHub's
sidebar shows only a generic "License" link, the grant was read from the
`LICENSE` file itself. One row this pass turns entirely on that step**, and it is
the row that closes this file's standing Caliper gap.
Grouped by the job they do, because "foundational" in education means five
different layers: the LMS, the student record, the content format, the
learning-data/ML layer, and **the integration layer that mounts anything into
anything**.

License matters more here than anywhere else in this KB: the big three LMSs are
**AGPL-3.0 or GPL-3.0**, which governs what a studio can hand a client as a
derived product. The MIT/Apache/BSD/ECL rows are the ones that compose freely.

**What changed this pass (fifth pass, 2026-11-13):** **40 repos**, up from 34.
The analytics edge — the one interoperability edge this file declared had no
permissive implementation — **now has one**, and the four passes of failure had
a single cause. Both `1EdTech/caliper-js` and `IMSGlobal/caliper-js` return
**404**: 1EdTech's Sensor API reference code is **member-gated** (its own Best
Practice Guide says Contributing Members and Affiliates request GitHub access),
so the slug this KB kept guessing has no public repository. The permissive
implementation is **outside both orgs**:
`CarnegieLearningWeb/caliper-ts`, **MIT**, read from its `LICENSE` file because
the sidebar shows only a generic link. 🟢 **The method that worked and should
become this base's default: list an org's repositories with GitHub's own filter
(`github.com/orgs/<ORG>/repositories?q=<term>`) instead of guessing slugs inside
it.** See the new Caliper section below.

**What changed at the fourth pass (2026-11-13):** **34 repos**, up from 33.
One addition, and it is a correction rather than an increment:
`dmitry-viskov/pylti1.3` (MIT, 138 stars) is a **Python** LTI 1.3 Advantage
library, which falsifies this KB's standing claim that no Python LTI library
exists. That claim was load-bearing — `compose/patterns.md` built a mandatory
two-process architecture on it — so the correction propagates there too.

**What changed at the third pass:** this file previously declared "no open-source LTI
1.3 tool-provider library made the verified set" and called it greenfield.
**That gap is closed and the conclusion was wrong.** Four LTI 1.3 libraries
verified below, led by `ltijs` (Apache-2.0, 373 stars) implementing the full
LTI Advantage service set. Do not quote the old greenfield claim to a client.

## The integration layer — LTI 1.3 (added third pass, corrected fourth)

Build the AI tool once as an LTI 1.3 tool provider and it mounts in Moodle,
Canvas, Open edX, Sakai and ILIAS. This is the highest-leverage single
investment in an education engagement, and it does **not** need to be written
from scratch.

**Updated 2026-11-13 (fourth pass): there are now five, and one of them is
Python.** The previous edition of this file and of `compose/patterns.md` stated
that every verified LTI 1.3 library was Node, PHP or Elixir and that a Python
agent therefore had to sit behind a non-Python LTI front door. **That is wrong.**
`dmitry-viskov/pylti1.3` (MIT, 138 stars) implements the full LTI Advantage
service set in Python with Django and Flask adapters. Single-language Python
deployments are available; see the revised constraint note in
`compose/patterns.md`.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | 373 | **The reference implementation.** Node.js; covers launches, Deep Linking, Assignment and Grade Services, Names and Role Provisioning, and Dynamic Registration — the complete LTI Advantage surface. v7 is a full rewrite with a migration guide from v5. 86 forks. README thanks CourseKey for making "the certification process possible" but **does not itself claim LTI Advantage certification** — a fork, `edugatorlabs/ltijs`, is the one advertising certified status. Verify certification claims before repeating them to a client. |
| https://github.com/dmitry-viskov/pylti1.3 | MIT | 138 | **The Python answer — new this pass, and it overturns this KB's "no Python LTI" finding.** Full LTI Advantage: Assignments and Grades, Names and Roles **and** Deep Linking, with shipped adapters for **Django and Flask** (another framework needs only `OIDCLogin` and `MessageLaunch` reimplemented). It is a port of the `packbackbooks` PHP library below, so the two are architecturally aligned and a PHP-to-Python move is cheap. 84 forks. **Maintenance caveat, stated because it governs adoption:** GitHub **Releases is empty**, the newest PyPI version is **2.0.0**, and a third-party scanner reports the last publish at roughly three years ago — pin the version, vendor it, and budget for carrying security patches yourself. Even so, at 138 stars and 84 forks it is the second most-used library in this table after `ltijs`. |
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

## The learner-record layer — xAPI Learning Record Stores (added third pass)

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

## The analytics layer — Caliper Analytics (new, fifth pass)

The fifth of the five interoperability edges, and the last one to get a
permissive implementation in this base. Caliper is the **1EdTech-native**
telemetry standard and is the one most often written into **North American
higher-ed** procurement; xAPI is the one with the better open stack. This
section exists so that an engagement contractually bound to Caliper has a named
starting point instead of a greenfield estimate.

**Read the licence column before the star column.** The Caliper field splits by
licence in a way that decides what can ship: exactly **one MIT sensor**, an
**Apache-2.0 analysis layer**, the 1EdTech reference lineage at **LGPL-3.0**, the
only LMS emitter at **GPL-3.0**, and the only event store **unlicensed**.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/CarnegieLearningWeb/caliper-ts | **MIT** (read from `LICENSE`: `MIT License` / `Copyright (c) 2021 Imagine Learning`; **the sidebar shows only a generic "License" link**) | 0 | **The only permissively licensed Caliper sensor found anywhere, and the row that closes this file's Caliper gap.** TypeScript implementation of the Caliper Sensor API — a port of `caliper-js`, which has **no public repository**. Entity factories for Assessment, AssessmentItem, Person, Session, SoftwareApplication and Membership; `createSessionEvent` / `createAssessmentEvent` in its examples. 225 commits on `main`, 1 fork, Releases empty. Default `dataVersion` is `http://purl.imsglobal.org/ctx/caliper/v1p1`, so **treat it as Caliper 1.1**. 🔴 **Three caveats that belong in the estimate:** it publishes to the **GitHub Package Registry** as `@imaginelearning/caliper-ts`, **not public npm**, so the build needs an `.npmrc` scoped to `@imaginelearning`; at **0 stars** it is a real library with no community, so budget to carry it; and its events and entities are generated by `caliper-code-generator` **from `caliper-net`, which is LGPL-3.0** — the output here carries an MIT grant, but read the generator's terms before regenerating. |
| https://github.com/open-lms-open-source/moodle-logstore_caliper | GPL-3.0 | 1 | **The only Caliper emitter for a real LMS, at any licence.** Moodle logstore plugin contributed by the Moodlerooms product team: a three-stage **Expander → Translator → Emitter** pipeline pushing Moodle log events to an event store through the Caliper Sensor API, **immediate or batched**, configured by Event Store URL, API key, send-immediately flag and batch size. Installs onto **Moodle 2.7+**. 66 commits, 7 forks, 7 open issues, Releases empty. 🟢 **GPL-3.0 is correct and harmless here, and that needs saying against this KB's own "do not fork the LMS" rule:** a Moodle plugin lives inside a GPL-3.0 host and is expected to be GPL-3.0; it does not reach the separately deployed MIT/Apache AI layer. `1EdTech/moodle-logstore_caliper` is a 13-commit fork of this repo — **use this upstream, not the fork.** |
| https://github.com/UnizinAnalytics/caliper-net-public | LGPL-3.0 | 0 | **The .NET reference sensor, and the broadest profile coverage in this table — read it even on a non-.NET engagement.** Implements the Sensor API across **nine Metric Profiles: Base, Session, Reading, Annotation, Assignable, Assessment, Assessment Item, Outcome and Media** — in practice the working definition of what a *complete* Caliper sensor covers, which is what you need to scope a build against. From **Unizin**, the US higher-education consortium: **North American provenance, which is exactly where Caliper gets specified.** It is also the origin of the `caliper-code-generator` that produces `caliper-ts`. No description, no releases. 🔴 LGPL-3.0 propagates on modification — extend by composition. |
| https://github.com/tl-its-umich-edu/caliper-php-public | LGPL-3.0 | 3 | **The reachable copy of the PHP reference sensor — and its own description is the primary evidence that the originals went away.** Verbatim from the repository: *"This fork of IMS Global's public release of caliper-php includes additional features needed at Univ. of Michigan. … **This had been archived, but has been unarchived following 1EdTech making its caliper-php private.**"* 🔴 **That is documentary confirmation, not inference: 1EdTech took `caliper-php` private, and a university un-archived its fork to keep it reachable** — which is exactly why four passes of slug-guessing returned 404s. Forked from `UnizinAnalytics/caliper-php-public`, so the chain is 1EdTech → Unizin → Michigan. PHP client implementing the Caliper Sensor API; U-M adds `Options::setHttpHeaders()`. Package versions 1.0.0 (IMS) / 1.0.1 (U-M) — **those are library versions, not Caliper spec versions, and the repo names no spec version.** 2 forks. Matters because Moodle and Chamilo are PHP shops. Sibling: `umich-caliper-php` (LGPL-3.0). 🔴 LGPL-3.0 propagates on modification. |
| https://github.com/tl-its-umich-edu/caliper-event-analysis | **Apache-2.0** | 1 | **The analytics half, permissively licensed — and the part a client actually buys.** Jupyter notebooks for analysing and visualising collected Caliper events, from a collaboration between University of Michigan Teaching & Learning and **U-M CSCAR**, its statistics consulting group. Not a sensor and not a store: it is the layer that turns emitted events into an answer. **Apache-2.0, so the notebooks can seed a client deliverable directly** — the only Caliper component other than `caliper-ts` for which that is true. 5 forks on 1 star: **more forked than starred, which for a notebook repo means people took it and used it.** 🔴 The repository page does not expose the notebooks' contents, so the analyses themselves are unverified — adopt the licence and the provenance, read the code before promising a dashboard. |
| https://github.com/open-ent/caliper | 🔴 **No license field shown — treat as all-rights-reserved** | 0 | **The only Caliper _event store_ found, and it cannot be adopted.** Open ENT module implementing **Caliper Analytics 1.2** — the newest version in this table — as **both** an event store (`POST`/`GET /ims/caliper/v1p2/events`, bearer-token auth) **and** a sensor forwarding Open ENT access and login events onward, mapped to `ToolUseEvent`/`Used` and `SessionEvent`/`LoggedIn` (activation, SMS and failed-login events are counted and excluded). Vert.x, SQL schema `caliper`, port 8174, **33 unit tests**. From **Open ENT**, the French regional *espace numérique de travail* platform — **EMEA public-education provenance, usable evidence in an EU data-sovereignty conversation.** 🔴 **Design reference only:** no licence on the page, and its README states the **Assessment, Grading, Forum and Media profiles are not implemented** because the ENT does not record those events. Worth a licence request. |

### What this does and does not change

🟢 **All five interoperability edges now have a permissive implementation.**
🔴 **The analytics edge is not equivalent to the other four**, and an engagement
must be priced on the difference:

| | xAPI (learning record) | Caliper (analytics) |
|---|---|---|
| Permissive **store** | 🟢 `yetanalytics/lrsql` — **Apache-2.0, 144★**, Postgres 14–18 / MariaDB / MySQL / SQLite | 🔴 **None.** The only store found is **unlicensed** |
| Permissive **sensor / client** | 🟢 `openfun/ralph` (MIT, 51★) + `DavidLMS/learnmcp-xapi` (MIT, 16★) | 🟡 `caliper-ts` (MIT, **0★**, GitHub Package Registry only) |
| **LMS** emitter | 🟡 via plugins and xAPI wrappers | 🟢 `moodle-logstore_caliper` (GPL-3.0, Moodle 2.7+) |
| Reference layer | 🟢 public | 🔴 **member-gated** (1EdTech Contributing Members / Affiliates) |

🟢 **Revised recommendation, replacing this file's "Caliper is a build, price it
as one":** where the client is **free to choose, still choose xAPI** — the store
asymmetry above is the whole reason. Where a contract **names Caliper**, the
honest answer is no longer "no open starting point." It is: **an MIT sensor, a
GPL-3.0 Moodle emitter, an Apache-2.0 analysis layer, and a complete
nine-profile reference to scope against — but you write the event store.**
That is a materially smaller and differently shaped project than greenfield.
Written up as pattern `P11`.

## The assessment-interchange layer — QTI (new to this file, fifth pass)

QTI is named in almost every education procurement document, and until this pass
this file's gap list said **"no open-source QTI item-bank toolchain surfaced."**
🔴 **That bullet was stale by many passes and is removed.** The KB's research log
(`intel/open-gaps.md`) had already measured this layer in depth — and this base
**ships a tested QTI artefact of its own** at
`compose/code/p533-qti3-template-emitter/` (43 assertions, 0 failures, 19
negative controls, 11 of 11 mutations detected). Seven repos verified fresh from
the rendered page this pass and promoted into this file, so the operational
shelf matches what the research log already knew.

**The architecture fact that governs a QTI engagement: scoring, item banking and
*certified delivery* live in different repos.** No single project has all three,
so the shape is always a pair.

| Repo | License | Stars | Notes |
|---|---|---|---|
| https://github.com/oat-sa/tao-core | GPL-2.0 | 64 | **The only full assessment *platform* here — TAO, the long-standing open e-testing system, with real item banking.** Highest star count in this table and the one a client may already run. 37 forks, Releases empty, no QTI version stated on this repo. 🔴 **Two constraints that decide whether it fits:** the open-source edition is **QTI 2.2-based, not QTI 3**, and it ships **no Results Management** — so a QTI 3 contract or a reporting requirement both land outside it. GPL-2.0, so it is a host to extend, not a base to embed. |
| https://github.com/amp-up-io/qti3-item-player | **MIT** | 30 | **The delivery half, and the only repo in this table claiming conformance certification.** 100% JavaScript QTI 3 item player aligned to the 1EdTech QTI v3 Best Practices guide, with stated **QTI 3 Basic *and* Advanced "Delivery" conformance** plus some elective capabilities. Item state via `endAttempt` / `suspendAttempt` / `scoreAttempt`; catalog/glossary events with dynamic rebinding; 14 colour themes. 596 commits, 6 forks, Releases empty. 🔴 **Built on Vue 2.6, which is end-of-life** — the integration cost is a Vue 2 island in a modern front end, and that belongs in the estimate. |
| https://github.com/LongsightGroup/qti3 | **MIT** (© 2026 Longsight, Inc.) | 6 | **The authoring, scoring and migration half — the broadest QTI toolkit found, and the one this KB has already contributed work toward.** 12 npm packages: core parsing and scoring, browser player, React and Preact adapters, CLI, fixtures, conformance, accessibility, PNP, **writer (with an item-bank package writer)**, **migrator** (QTI 1.2 and 2.x → 3) and **transcoder** (QTI 3 → 1.2 / 2.1 / 2.2 / Canvas / Moodle). Tracks the **QTI 3.0.1 ASI item profile**, 19 interaction types. 3 forks, Releases empty, changelog at 0.13.0. 🔴 **Known limit, measured by this KB and not by its README:** `packages/writer` **cannot emit `qti-template-declaration` / `qti-template-processing`**, so *parametric* item variants cannot be authored on it even though `packages/core` fully executes them (real `randomInteger` draw over `min`/`max`/`step`, answer keys derived from the draw, constraint retry up to 100 restarts). 🟢 **The fix already exists in this repository** — `compose/code/p533-qti3-template-emitter/` regenerates two upstream fixtures node-for-node, and `writer-contribution.ts` is written in the host project's idiom. It is **MIT, so this is a contribution, not a procurement** — and it has **not been sent upstream** (`Gap 240`). Deliberately not opened unprompted: it is an outward action. |
| https://github.com/Citolab/qti-components | GPL-3.0 | 18 | QTI item renderer as **web components**, "easy to use and highly customizable". 10 forks. 🔴 **Not adoptable yet and its own README says so:** the status badge reads *"WIP — initial development is in progress, but there has not yet been a stable, usable release suitable for the public."* It also **never names a QTI version**. Web components are the most framework-neutral shape in this table, so it is the one to re-check next pass — but GPL-3.0 plus no stable release is two reasons not to build on it now. |
| https://github.com/pie-framework/pie-qti | **MIT** | 4 | **The conversion bridge.** QTI 2.1 / 2.2 / 3.0 players plus bidirectional **QTI ↔ PIE** transforms, with a CLI and IMS Content Package support. QTI → PIE accepts 2.1 and 2.2 (3.0 is downconverted to the 2.2 vocabulary on ingest); PIE → QTI exports 2.2 and can emit content packages. 1 fork. 🔴 **Its README states the players are "not yet fully conformant or certified" and the transform framework is "under active development"** — use it for migration work, not delivery. |
| https://github.com/examplary/qti | **MIT** | 2 | **The smallest useful piece: packaging.** TypeScript library to build and parse **IMS Content Packages** containing QTI tests and items — QTI **3.0 by default and 2.1 supported, with automatic version detection on parse**. Parses both ZIP packages and raw XML strings. 0 forks, Releases empty. Does no rendering, scoring or storage, which is why it composes cleanly with anything above it. |
| https://github.com/agencyenterprise/qti-3-player | **MIT** | 3 | **Admitted for its honesty, not its coverage — and it is a useful negative control.** Framework-agnostic QTI 3 renderer with React, Vue and vanilla wrappers, XML validation against the QTI 3.0 schema, response processing with conditional logic, outcome variables, inline and modal feedback, MathML via user-supplied MathJax 2/3/4. 🔴 **Its README states plainly what it does *not* do: no scoring, no test structure (single items only), choice interactions only, basic expressions only (`match`, `correct`), no adaptive behaviour.** 1 fork. **Not adoptable for assessment** — listed because a README this candid is the cheapest way to see what "renders QTI" does and does not buy, and because the other players in this table are not all this explicit. |

🔴 **Licence trap recorded by this KB and worth repeating here, because it defeats
every sidebar check:** [`Learnosity/learnosity-qti`](https://github.com/Learnosity/learnosity-qti)
**carries different licences on different branches** — `master` is **MIT**
(1 067 B) while `develop`, **its default branch**, is **GPL-2.0** (18 264 B).
🟢 **Re-confirmed fresh this pass:** the repository landing page shows
**`develop`** as the default branch and **"GPL-2.0 license"** in the sidebar
(26 stars, 22 forks, *"Convert QTI 2.1 Assessment Items to and from Learnosity
Item and Question JSON"*), and its README states the package is GPL-2.0 — so
**the permissive `master` grant is invisible to every landing-page check.**
**On any QTI repo, confirm the branch the licence was read from before quoting
it.** 🔴 Note also that it converts **QTI 2.1**, not QTI 3 — it is a migration
tool, not a delivery component.

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
  `DavidLMS/learnmcp-xapi` on the agent side); **Caliper now has six verified
  implementations too (fifth pass, see the analytics section above)** — but no
  permissively licensed *store*, so **xAPI remains the lower-risk choice
  wherever the client has no prior contractual commitment**.
- **QTI** — assessment item interchange. Matters the moment a client wants to
  move an item bank between systems.
- **SCORM** — legacy but ubiquitous in corporate and vocational training; still
  the delivery format many EMEA/APAC clients require.

## Declared gaps

- **The Caliper gap is CLOSED, and what replaced it is narrower and sharper
  (fifth pass).** This file previously said Caliper "has no verified open
  implementation here" and that a Caliper-bound engagement had "no open starting
  point in this base — that is a build, and it must be priced as one." **Both
  sentences are withdrawn.** Six implementations are now tabled above, led by
  `CarnegieLearningWeb/caliper-ts` (**MIT**). 🔴 **What survives as a real gap is
  one component, not the standard: there is no permissively licensed Caliper
  event store** — the only store found (`open-ent/caliper`, Caliper 1.2, Vert.x,
  33 unit tests) carries **no licence**. That is `Gap 287`, it is genuinely a
  build, and it is the one line item to price. Everything around it — sensor,
  LMS emitter, analysis notebooks, nine-profile reference — now exists.
- **Caliper's reference layer is behind consortium membership, and that is a
  procurement fact, not a search failure.** `1EdTech/caliper-js` and
  `IMSGlobal/caliper-js` both **404**; 1EdTech's Best Practice Guide advertises
  Sensor API reference code in Java, JavaScript, PHP, Python, Ruby and .NET and
  states that **Contributing Members and Affiliates can request GitHub access**.
  🟢 **And there is now documentary confirmation rather than inference:**
  `tl-its-umich-edu/caliper-php-public`'s own description reads *"This had been
  archived, but has been unarchived following **1EdTech making its caliper-php
  private**."* **A university un-archived its fork specifically because the
  upstream was withdrawn.**
  🟢 **The workaround is reliable: the public releases were forked by
  universities and consortia, and the forks are indexed where the originals are
  not** — `tl-its-umich-edu/caliper-php-public`, `umich-caliper-php`,
  `UnizinAnalytics/caliper-net-public`. 🔴 **No Caliper Python or Ruby
  implementation is publicly reachable** from any org listing checked this pass.
  **xAPI has no equivalent gate**, which is a reason to prefer it beyond the
  licence table.
- **Caliper version matters and should be asked about in week one.**
  `caliper-ts` defaults to **v1.1**. The only **v1.2** implementation found is
  the **unlicensed** `open-ent/caliper`. A client whose contract names Caliper
  **1.2** is further from this shelf than one naming 1.1 — establish which
  version the contract specifies before estimating.
- **No permissively licensed full LMS exists at scale.** Every LMS with real
  deployment is GPL/AGPL except Sakai (ECL-2.0). A client who needs a
  proprietary derived platform cannot start from Moodle, Canvas, or Open edX —
  that constraint should be surfaced in week one, not month three.
- 🔴 **DEFECT FIXED (fifth pass): this gap list previously still carried "No LTI
  1.3 library in Python … A Python LTI 1.3 tool-provider library remains
  genuinely greenfield", while the header and the LTI section of this same file
  recorded the fourth pass's correction that it exists.** A file that contradicts
  itself sells the contradiction, and the gap list is the part that gets read
  into a proposal — this one would have quoted a client for a library already
  shipping. **The accurate statement:** `dmitry-viskov/pylti1.3` (**MIT, 138
  stars, 84 forks**) implements the full LTI Advantage service set in Python with
  Django and Flask adapters, so **single-language Python deployments are
  available and the forced two-process architecture is no longer forced.**
  🔴 **The residual risk is maintenance, not existence:** Releases is empty,
  newest PyPI version is **2.0.0**, and a third-party scanner puts the last
  publish at roughly three years ago — pin the version, vendor it, and budget to
  carry security patches.
- 🔴 **DEFECT FIXED (fifth pass): this list carried "No open-source QTI
  item-bank toolchain surfaced … it needs a dedicated search" while
  `intel/open-gaps.md` had measured the QTI layer across several passes and this
  repository ships a tested QTI emitter at
  `compose/code/p533-qti3-template-emitter/`.** The dedicated search had been
  done; its results had never reached this file. **Seven QTI repos are now
  tabled above**, five of them MIT. 🔵 **The general lesson, because this is the
  second stale bullet fixed in this file today:** findings that land only in the
  research log do not reach a proposal. When a pass closes a gap, it must delete
  the bullet in the operational file, not only record the closure.
- **What is genuinely still open in QTI is narrow and named.** `Gap 240`: the
  parametric-variant emitter this base built and tested for
  `LongsightGroup/qti3`'s `writer` package **has not been contributed upstream**;
  it needs someone with a working `qti3` checkout to run the project's own suite
  (third-party dependencies are not installable in this environment) and to
  validate against the official ASI schema (`purl.imsglobal.org` is
  proxy-blocked). 🔴 **And no repo in the table joins certified delivery to
  authoring and scoring** — `qti3-item-player` is certified but delivery-only;
  `qti3` authors and scores but claims no certification. **Every QTI engagement
  is therefore a pairing exercise, and that is the estimate to write.**
