---
industry: education
region: Global
updated: 2026-11-17
---

# Top AI agents — education

**Pass `p878`, 2026-11-17** (eighth pass of the day). **`p878` turns discovery first-hand.**
`api.github.com/search/repositories` accepts full **discovery** queries — `topic:`,
`in:name,description`, `stars:>`, `pushed:>` — and not merely the `repo:` slug lookups `p875`
used it for. 44 English legs returned **546 measured repositories**; 12 further legs in **Spanish
and Portuguese** — never run by any previous pass — returned **304 more**. Three consequences for
this file:

- 🟢 **The grading category is no longer "one row because one row verified."** Two mature,
  permissive, actively maintained **platforms** perform automated grading at scale:
  **`ls1intum/Artemis`** (MIT, 832 ★, TUM) and **`autolab/Autolab`** (Apache-2.0, 808 ★, CMU).
  They are platforms rather than agents, so they are filed in `verticals/solutions.md` and
  `repos/foundations.md` — but a grading engagement that reads only this file now gets the wrong
  answer. See the pointer in **Grading & assessment agents** below.
- 🟢 **A new row class: institutional AI subsystems.** Artemis's AI is three config-gated
  microservices (**Iris**, **Athena**, **Hyperion**) shipped as separate MIT repositories, with
  *"instructors and tutors stay responsible for assessment decisions"* stated in the platform's own
  README. That is an EU AI Act posture expressed as architecture, and it is reusable independently
  of Artemis. New section below.
- 🔴 **`NOASSERTION` decides nothing, in either direction.** `p877` correctly caught a false
  permissive (PageLM). `p878` independently re-read the two standing education-side anomalies and
  **confirms `p877`**: `OpenOlat/OpenOlat` is byte-identical Apache-2.0, `Gego-K12/gegok12` is MIT.
  GegoK12's classifier abstention is now diagnosed exactly — its `LICENSE` carries an HTML comment,
  `<!-- SPDX-License-Identifier: MIT -->`, on line 3. **The one rule that covers both of this KB's
  licence errors: `spdx_id` screens, bytes decide.** A permissive claim needs bytes to confirm it;
  a `NOASSERTION` needs bytes to refute it.

🔴 **A blind spot in the measured census, named.** `openedx/edx-platform` returns `422` from the
search channel while `raw.githubusercontent.com` serves its AGPL-3.0 licence bytes — it exists and
is public, but **cannot be measured or discovered by this channel at all**, though its siblings
(`edx-ora2`, `edx-proctoring`, `openedx-aspects`) can. `p877` read `422` as a renamed-slug signal;
the error body says otherwise — *"the listed users and repositories cannot be searched either
because the resource does not exist or you do not have permission to view them."* **A repository
absent from the sweep is not evidence it does not exist.**

**Previous pass (`p877`), retained:** Pass `p877`, 2026-11-17** (seventh pass of the day). **`p877` is a grant audit, and it found
the most expensive class of error this KB can make: a repository published as `MIT` that is not
open source at all.** It also restores five build-safe agents that today's own `p871` rewrite
dropped out of this file.

> **🔴 `CaviraOSS/PageLM` IS NOT MIT. Its licence bytes are a bespoke, 8,563-byte "PageLM
> Community License": non-commercial only, redistribution "strictly prohibited", a
> revenue-sharing agreement required before any commercial use, and a Partial Use Clause under
> which using *"any portion, code snippet, algorithm, design pattern"* commercially triggers the
> whole commercial regime.** The grant is revocable and terminates automatically on breach.
> **A Globant engagement is Commercial Use by definition, so PageLM is unusable as a base** — it
> is removed from the agent table below and filed in `intel/measured-unusable.md`.
> 🔵 **This was never a relicensing event:** `LICENSE.md` has been bespoke since the repository's
> initial commit (`a3722a3`, 2025-08-31) and last changed 2025-10-05. The KB published `MIT` for
> fourteen months against bytes that never said it.

> **🔴 The star table in THIS FILE already flagged PageLM `NOASSERTION` and said "re-read the
> bytes before naming it in a proposal". The agent table two sections below it published `MIT`
> anyway.** The instruction and the error were in the same file, four screens apart. `p876`
> diagnosed this failure mode as T13 (*propagation*); `p877` is the case where it reached the
> client-facing column.

> **🔴 `p871`'s full rewrite silently dropped five verified, permissively licensed agents from
> this file — and `p876` then ran a discovery sweep and concluded "there is no hidden shelf".**
> The shelf was in this repository's own `archive/2026-11-17-p871-pre-rewrite/agents-top.md`.
> `p877` re-measured each one from scratch; **the licence hashes match the archived rows to the
> byte** (`BloomTutor` 1,069 B `7d574cf3632e`; `OpenTutor` 1,068 B `5352b4967982`;
> `open-tutor-ai-CE` 1,531 B). They are restored below, with fresh liveness.

> **🟢 T12 survives, independently re-tested — with an honest discount.** `p877` ran its own
> 16-leg star-ranked sweep on a different leg set from `p876`'s ten; **six legs returned
> `total_count=0` and tested nothing**, so the real evidence is **ten effective legs**,
> 94 unique repositories, 26 unknown to this KB.
> **Not one unknown repository was a build-safe education agent** — the MIT hits were a 2024
> coursework site, a 2023 university TA chatbot, a 2019 paper artifact, and two keyword
> collisions (autonomous driving, SQL Server tooling). `p876`'s conclusion holds; what was wrong
> was not the conclusion but the premise that this file held everything already found.

**Previous pass note (`p876`)** (sixth pass of the day). **`p876` adds no agent row and corrects
three addresses and one liveness claim.** It ran a ten-leg star-ranked **discovery** sweep —
the first this KB has been able to run, since `p875` only measured addresses it already held —
and the result is worth stating plainly:

> **🔴 A star-ranked discovery sweep across ten education queries returned 126 repositories, 47 of
> them new to this KB, and NOT ONE is an education agent.** They are `awesome-*` lists, curricula,
> prompt collections and, repeatedly, the same anti-propaganda repository that ranks for anything.
> **This is `intel/trends.md` T12 confirmed from the discovery side rather than the measurement
> side:** the reason this file has two large agents and a tail of zeroes is not that the KB has
> been looking in the wrong place. **There is no hidden shelf.** The legs are recorded in
> `repos/trending.md` `p876` so a later pass does not re-buy them.

> **🟡 Three addresses in this file were canonical-stale, and the git protocol hid it.**
> `All-Hands-AI/OpenHands` → **`OpenHands/OpenHands`** (93,647★) and `danny-avila/LibreChat` →
> **`LibreChat-AI/LibreChat`** (47,237★). Both old addresses still answer `git ls-remote` and
> still serve correct licence bytes **via redirect**, so this KB's two-channel verification passed
> on them for passes on end. The detector is the search API's `422`. (`openedx/edx-platform` →
> `openedx/openedx-platform` is the third; it is cited elsewhere in this KB, and the rename was
> already in the trending log — it had simply never been propagated to the curated files.)

**Previous pass note (`p875`)** (fifth pass of the day). **`p875` adds NO row to this file and adds a
column instead** — the first adoption signal this KB has ever carried. After four passes declaring
star counts unmeasurable, the channel was found (`api.github.com/search/repositories`; see
`agents/trending.md` for why `p874` ruled it out). **78 addresses measured first-hand.**

> **The measurement reorders this file, and the finding is uncomfortable.** Two education-native
> agents have real user bases — **DeepTutor (59,972)** and **OpenMAIC (43,808)**. **Every other
> education-native agent listed below has fewer than 20 stars, and four have ZERO.** This file has
> been presenting a 60,000-star platform and a 0-star single-author repository in the same table,
> distinguished only by a maturity flag in prose. **The Adoption column makes that distinction
> unskippable.** Stars measure attention, not quality — but a 0-star repo has no community, no
> issue history and no evidence of a deployment, and that is a support-burden fact a client must
> hear before a statement of work is signed.

`p875` resolved four new addresses and promoted none: `withmarbleapp/os-taxonomy` (7,720 stars) is
**ODbL-1.0**, a share-alike *database* licence and not a software licence;
`patchy631/ai-engineering-hub` (41,955, MIT) is teaching material *about* AI, not an education
agent; `BlackyDrum/ai-tutor` (8, MIT) is the only MIT tutor found that speaks LTI and it is
**LTI 1.0, last pushed 2024**; `kevinnio/tutor` (15, MIT) is an agent skill with no LMS seam.
Reasons against each are in `agents/trending.md`.

> **🟢 OpenMAIC's licence is SETTLED — stop re-litigating it.** Three passes have re-checked it
> against sources that disagree. `p875` found the cause: the project **relicensed to MIT on
> 2026-06-28** (its own README changelog, `v0.3.0`), so every pre-July source — **including the
> project's own site `openmaic.io`, which still says AGPL-3.0** — describes a dead licence. A
> second mechanism compounds it: `kolbyzhu5/OpenMAIC`, a pre-relicence **AGPL-3.0 fork**, sits in
> the search index. Four channels now agree on **MIT**: licence bytes, no other licence file on
> the branch, the README badge and text, and SPDX detection.

> **🔴 Deployment hazard in OpenMAIC, from its own README.** Site-wide access is gated by a single
> `ACCESS_CODE` variable, and **unset is the default in `.env.example`**: `middleware.ts` then
> checks no credential and *"every route, the API included, is reachable… there is no second
> enforcement point."* A default OpenMAIC deployment in a school tenancy is a student-data
> exposure on day one. Any pattern shipping it must budget `ACCESS_CODE` provisioning and a second
> enforcement point — see `compose/patterns.md` **P12**.

**Previous pass note (`p874`):** resolved 10 addresses and added no row — 4 had no licence file, 1
reserved all rights, 3 were shelved, 1 was Gemini-API-dependent, 1 was not education. It
re-confirmed OpenMAIC against two sources that disagreed; `p875` has now explained why they did.

**Previous pass note (`p873`):** targeted `p872`'s declared gaps rather than re-verifying its
seventy addresses.
Every row below was verified by two channels:
existence via `git ls-remote https://github.com/<slug>` (an HTTP 200 on the git smart
protocol), and licence via the actual licence bytes fetched from
`raw.githubusercontent.com/<slug>/<resolved-default-branch>/<licence-file>`. The default
branch was resolved with `git ls-remote --symref ... HEAD` rather than assumed to be `main`
— four of the repos below do **not** use `main`, so a guessed path would have 404'd.

### Verification channels this run

| Channel | Result |
|---|---|
| `git ls-remote` (existence, default branch) | **open** — used for all rows |
| `raw.githubusercontent.com` (licence bytes) | **open** — used for all rows |
| `github.com` HTML | **403** — blocked, session GitHub scope |
| `api.github.com` | **403** — blocked, session GitHub scope |
| `gh` CLI (`gh api repos/...`) | **403** — git proxy: *"not in this session's authorized repository set"* (added by `p873`) |
| `gh api search/repositories` | **empty result set** — no star-ranked discovery (added by `p873`) |

> **No star counts appear in this file.** The star channel returned `403` across **four distinct
> routes** — `api.github.com`, `github.com` HTML, the `gh` CLI and the GitHub search API — for a
> **third consecutive pass**, so stars were **not measurable this pass** either. Prior
> pass `p870` recorded DeepTutor at `59,922★` from a star-ranked sweep it could run; that
> figure is its measurement, not this pass's, and is not restated here as fact. Writing a
> star count sourced from a blog is how this KB previously recorded inflated numbers.

## Measured adoption — new in `p875`

Read this before the tables below. Measured `2026-11-17` via `api.github.com/search/repositories`.
🔴 marks no push since 2026-06-01.

| Agent | Stars | Licence (SPDX) | Last push | Read |
|---|---:|---|---|---|
| **HKUDS/DeepTutor** | **60,007** (`p878`; was 59,972 in `p875`) | Apache-2.0 | 2026-11-15 | Real platform, real community. Safe to propose. |
| **THU-MAIC/OpenMAIC** | **43,823** (`p878`; was 43,808) | MIT ✅ | 2026-11-17 | Real platform, real community. Ship with the `ACCESS_CODE` hardening task. |
| ~~CaviraOSS/PageLM~~ 🔴 **REMOVED — NOT OPEN SOURCE** | 2,069 | 🔴 **"PageLM Community License"** — byte-read `LICENSE.md`, **8,563 B**, `sha256₁₂ c834209c5f33` | 2026-11-15 (alive, 55 commits/12mo) | 🔴 **The bytes were re-read, as this row instructed, and they are not MIT.** Non-commercial; redistribution prohibited; revenue-share required for commercial use; Partial Use Clause reaches a single snippet or design pattern. **Do not name it in a proposal at all.** See `intel/measured-unusable.md`. |
| CAHLR/OATutor | 282 | MIT | 2026-11-17 | Small but alive, peer-reviewed, accessibility-conformant. The credible academic option. |
| AI-for-Education/pedagogy-benchmark | 13 | MIT | 2026-11-16 → 🔴 **HEAD `2025-10-15`** | An eval harness, not a tutor — low stars are expected and not disqualifying. 🔴 **`p876` liveness correction: the `2026-11-16` push did not touch the default branch, whose last commit is `2025-10-15` — 398 days, `0` commits in 12 months.** It is still the right instrument to cite to a ministry (1,143 questions from real teacher-qualification exams); it is a **frozen** one. Say so in the proposal rather than implying an active leaderboard. |
| wwrwbs/AI_AWE (ArguLens) | **2** | 🟢 **Apache-2.0 — byte-read**, `LICENSE` **1,865 B**, `sha256₁₂ 4b5296db216d` | 2026-07-29 | 🟢 **`p877` licence correction: there IS a detectable licence and it is permissive.** The `NOASSERTION` came from the file's *shape*, not its absence — it is Apache-2.0 short-form **plus an in-file component manifest** (see below). Two stars still means paper artifact, not base: that half of the old verdict stands. |
| PritK99/WriteRight | **1** | MIT | 2024-11-19 🔴 | Reference implementation only, as this file already said. Confirmed. |
| littlecookie0722/AI-Teaching-Agent | **0** | MIT | 2026-08-23 | No community. Bespoke-from-zero risk profile. |
| vulinh1704/ai-tutor-agent | **0** | MIT | 2026-11-16 | A starter template, as flagged. Confirmed by adoption. |
| LabSirius/TutorIA | **0** | MIT | 2026-10-27 | 🟡 **Zero stars, and this one is not a weekend project** — it is a funded Colombian university deliverable. The maturity caveat below (docs-only `main`) is the operative fact; the star count corroborates that nobody outside the lab has used it. |
| **ls1intum/Artemis** | **832** | **MIT** — byte-read `main/LICENSE` | 2026-11-17 | 🟢 **New in `p878`.** A platform, not an agent, but it is the largest permissive education *system* in this KB and it grades. Ten years old, pushed on the day of measurement, OpenSSF Scorecard + Best Practices (project 14163). See `verticals/solutions.md`. |
| **autolab/Autolab** | **808** | **Apache-2.0** — byte-read `master/LICENSE` | 2026-11-11 | 🟢 **New in `p878`.** Carnegie Mellon's auto-graded course-management service. Created 2014-10-25. |
| **ls1intum/Apollon** | 106 | **MIT** | 2026-11-17 | 🟢 New in `p878`. UML modelling editor, standalone-capable. |
| **ls1intum/Ares** | 27 | **MIT** | 2026-11-03 | 🟢 New in `p878`. Secure sandboxed auto-grading execution (JUnit 5). The most liftable component found this pass. |
| **ls1intum/edutelligence** | 17 | **MIT** | 2026-11-17 | 🟢 New in `p878`. Iris / Athena / Hyperion AI microservice suite. |
| **ls1intum/Pyris** | 12 | **MIT** | 2026-06-03 | 🟢 New in `p878`. Standalone LLM microservice behind Iris. |
| **virtualryder/edu-ai-agents** | **4** | **MIT** — byte-read | 2026-10-10 | 🔴 New in `p878`. FERPA/COPPA/IDEA-504/ADA-aligned governed-agent reference. **Four stars — reference reading, not a dependency.** |
| 🔴 `openedx/edx-platform` | **unmeasurable** | AGPL-3.0 — byte-read via `raw.githubusercontent.com` | — | 🔴 **New in `p878`: returns `422` from the search channel and cannot be measured or discovered by it**, although it exists and is public and its sibling repos are indexed. The census has a named hole, and it is this KB's flagship LMS. |

🟡 **How to use this column.** It separates *support burden* from *engineering quality*. A 0-star
repo may be excellent code; it will still have no external contributors, no issue history and
nobody to escalate to. Price that into the engagement or choose a different base.

## Education-native agents

These are built for teaching and learning as their primary purpose.

| Agent | Repo | Licence | Default branch | What it does |
|---|---|---|---|---|
| **DeepTutor** | https://github.com/HKUDS/DeepTutor | Apache-2.0 | `main` | Self-hosted lifelong tutoring agent from HKUDS (HKU Data Science lab). Grounds tutoring in the learner's own documents via LightRAG retrieval, tracks skill mastery, generates learning paths, narrated video lessons and question-bank practice. Ships a CLI "agent-native interface", desktop builds, Anki and calendar export, Kiwix offline-archive ingest, and an `EduHub` skills community. Release `v1.7.3` dated 2026-11-16 — weekly cadence. |
| **OpenMAIC** | https://github.com/THU-MAIC/OpenMAIC | MIT | `main` | Multi-agent classroom from Tsinghua's MAIC lab. Generates a complete course — AI teacher plus AI classmate agents — from a topic or an uploaded document, with project-based learning (PBL v3), a foldered knowledge base with `@`-mention, course-level undo, and export to PPTX and HTML. Release `v1.5.0-rc.3` dated **2026-11-17** (today). Server-first: generation survives a closed tab. |
| **OATutor** | https://github.com/CAHLR/OATutor | MIT | `main` | Open adaptive tutoring system from UC Berkeley's CAHLR. Intelligent-Tutoring-System design using **Bayesian Knowledge Tracing** for mastery estimation; React, deployable to static pages with no backend; LTI middleware for LMS integration. **Section 508 / WCAG compliant** — the only row here with a published accessibility conformance document. Peer-reviewed (CHI '23, doi:10.1145/3544548.3581574). |
| **Pedagogy Benchmark** | https://github.com/AI-for-Education/pedagogy-benchmark | MIT | `main` | Not a tutor — the **evaluation harness for tutors**. 1,143 questions drawn from real teacher-qualification exams, split into CDPK (920, cross-domain pedagogical knowledge) and SEND (223, special educational needs and disabilities). Runs 100+ models, public leaderboards, paper arXiv:2506.18710. This is how you defend a tutoring claim to a ministry or a university procurement board. |
| **AI Teaching Agent** | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | `main` | Instructor-side rather than learner-side: generates labs, exams, grading workflows and presentations with structured DSLs, human review, sandboxed evaluation, and CLI/MCP tools, local-first. **Maturity flag:** its own README states automatic-grading productisation is frozen, so treat grading as incomplete. |
| **ai-tutor-agent** | https://github.com/vulinh1704/ai-tutor-agent | MIT | `main` | FastAPI + LangGraph starter for tutoring agents: Socratic hinting, rubric-based grading with structured output, session memory, offline demo mode. **Maturity flag: a starter template, not a product** — useful as a skeleton for a bespoke engagement, not as a platform. |
| **TutorIA** | https://github.com/LabSirius/TutorIA | MIT | `main` | **New in `p873` — the first verified LATAM-origin education-native agent in this KB.** Autonomous tutor for **rural higher education in Risaralda, Colombia**, from Grupo Sirius at Universidad Tecnológica de Pereira; built to run inside **Open edX**. v2 backend: **Ollama-default inference via the OpenAI-compatible interface** (`llama3.2`), **pgvector + `nomic-embed-text` RAG**, an Open edX→PostgreSQL sync gateway on APScheduler, and pedagogical prompt templates held in the database. Tag `informe-minciencias-2026-09` — a funded deliverable reported to Colombia's science ministry. **Maturity flag, and it is the operative fact: `main` contains documentation only. The code is on `feature/refactor-to-v2-requirements`, it is backend-only, and the React frontend, Open edX plugin and test suite its README describes do not exist in any branch.** See below. |
| **BloomTutor** 🟢 **RESTORED `p877`** | https://github.com/Li-Evan/BloomTutor | **MIT** — byte-read `main/LICENSE`, **1,069 B**, `sha256₁₂ 7d574cf3632e`, holder © 2026 Li Zhengping | `main` | **313★ / 44 forks. The single best-evidenced permissive tutor in this file after the two large platforms, and it was dropped by `p871` without a stated reason.** A personal tutor built explicitly on **Bloom's 2-sigma** framing: generates a structured syllabus, delivers **one lesson at a time**, reads the learner's annotations and feedback, and re-tailors the next lesson. Ships **both** a self-hosted web app (`backend/`, `frontend/`, `docker-compose.yml`) **and** a Claude Code skill (`.claude-plugin/`), plus a browser `extension/`, `integrations/` and `THIRD_PARTY_NOTICES.md`. 🟢 **Liveness re-measured `p877` by bare clone: HEAD `2026-11-17` (today), 84 commits in 12 months — the entire history is within the year.** Bilingual `README`/`GUIDE` (EN + zh). Filed **Global**: the holder name and Chinese-language docs are language evidence, not market evidence. |
| **OpenTutor** 🟢 **RESTORED `p877`** | https://github.com/zijinz456/OpenTutor | **MIT** — byte-read `main/LICENSE`, **1,068 B**, `sha256₁₂ 5352b4967982`, holder © 2026 Zijin Zhang | `main` | **181★ / 47 forks.** A **block-based adaptive learning workspace that runs locally**: upload any material → AI-generated notes, quizzes, flashcards and an adaptive tutor, self-hosted, **10+ LLM providers**. 🟢 **Liveness `p877`: HEAD `2026-11-16`, 292 commits in 12 months** — the most actively developed small agent in this file. Engineering signals are unusually strong for this shelf: `.pre-commit-config.yaml`, `.gitleaks.toml`, `.secrets.baseline`, `.coveragerc`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`. 🔴 **Region REFUSED, not Global** (`p870`): the commit-identity channel returned `gmail.com` 42/50 and `anthropic.com` 6/50 — placeholder and AI-assistant identities, which carry no affiliation. **Do not cite a region for this row.** 🔵 Canonical among its fork set: `zijinz456/` supersedes `Pranjulcr7/OpenTutor` by ancestry, and `tutornew/OpenTutor` (8★, no licence) is a different project that a 2026 web sweep wrongly credited with this one's prominence. |
| **Whiteboard AI Tutor** 🟢 **RESTORED `p877`** | https://github.com/molly554/whiteboard-ai-tutor | **MIT** — byte-read `main/LICENSE`, **1,089 B**, `sha256₁₂ ed7406a62bcb` | `main` | **216★ / 8 forks. Take it for the PROTOCOL and the BENCHMARK, not for the app — its own README says *"It is not a hosted tutoring app."*** Animated whiteboard lessons with interactive playback, and a published comparison of **Claude, Gemini and DeepSeek across 288 generation runs and 64 blueprints**. In-tree and load-bearing: `protocol/`, `bench/`, `scenarios/`, `results/`, `player/`, `audit.html`. 🟡 **Maturity flag, measured `p877`: 6 commits total** — a squashed or very young history, so treat the benchmark as a published artefact rather than a maintained leaderboard. Bilingual (EN + zh). |
| **Open TutorAI (CE)** 🟢 **RESTORED `p877`** | https://github.com/Open-TutorAi/open-tutor-ai-CE | **BSD-3-Clause** — byte-read `main/LICENSE`, **1,531 B**, `sha256₁₂ 57c341d09920` | `main` | **118★ / 196 forks** — note the fork-to-star ratio, the highest in this file, which reads as classroom and downstream-deployment use rather than spectating. Community edition of an educational collaborative AI platform; substantial repo (`CHANGELOG.md`, `MIGRATION.md`, `TROUBLESHOOTING.md`, `SECURITY.md`, `Caddyfile.localhost`, `AGENTS.md`). 🔴 **Read past line 2 of the LICENSE before judging it:** the file opens *"Copyright (c) 2023-2025 Mohamed El hajji On behalf of all R2D-dev / All rights reserved."* — **that phrase is the BSD preamble, not a retraction**; the grant below it is BSD-3-Clause. This KB has twice mis-graded it (once as CC BY-NC-SA) on a two-line read. 🟡 **Liveness `p877`: HEAD `2026-06-26`, 91 commits in 12 months but none in ~5 months** — usable and permissive, but do not promise upstream responsiveness. |
| **education-skills** 🟢 **RESTORED `p877`** | https://github.com/flysheep-ai/education-skills | **MIT** — byte-read `main/LICENSE`, **1,068 B**, `sha256₁₂ 23b91d7c0aef`, holder © 2026 flysheep-ai | `main` | **125★ / 24 forks.** Not an agent and not a platform — a **skills pack**: a collection of teaching and tutoring Claude Code skills (教育类 Claude Code Skills 集合), organised as five subject tutors for the Chinese **gaokao** (`gaokao-chinese-tutor`, `-english-`, `-science-`, `-liberal-arts-`, `-general-tech-`) plus `package-skills.sh` and `PACKAGING.md`. 🟡 **Liveness `p877`: HEAD `2026-01-29`, 4 commits total** — effectively frozen. **Its value is as a worked example of exam-aligned pedagogical prompt packaging under a permissive licence, not as a dependency.** Filed **Global** on the same language-is-not-market rule as BloomTutor. |

**8 education-native rows.** That is what verified; the table is not padded to a round
number. See the declared gap below on what is missing.

### TutorIA — why it is listed, and exactly what you get if you clone it

It is listed because it answers a question this KB had been answering with an absence: *is anyone
in LATAM building an education-native agent, or does the region only deploy other people's?* A
Colombian public university shipping an **MIT-licensed** tutoring agent aimed at **rural,
low-connectivity higher education**, with a **named pedagogical director** and a reporting
obligation to a national science ministry, is the counter-example. For a Spanish-language
engagement its pedagogical framing, language and deployment context already match the brief —
which is worth more than maturity at the proposal stage.

It carries a flag because **a clone of its default branch ships nothing runnable**:

| Address | Branch | Contents |
|---|---|---|
| `LabSirius/TutorIA` | **`main` (default)** | `README.md`, `CONTRIBUTING.md`, `LICENSE`, `docs/`. `backend/`, `frontend/`, `docker-compose.yml`, `.env.example` **all 404** |
| `LabSirius/TutorIA` | `feature/refactor-to-v2-requirements` | **The v2 backend** — `backend/app/{main,config}.py`, `routers/chat.py`, `services/rag_service.py`, `gateways/openedx_gateway/sync_service.py`, `requirements.txt`, `docker-compose.yml` |
| `Sof1SP/tutorIA` (**the address its own README's `git clone` line points at**) | `main`, `dev` | **No code in either** — `README.md` + `LICENSE` only. Also MIT |

Also note: **the README is behind the code.** It describes Anthropic Claude API + Microsoft Azure;
`backend/app/config.py` defaults to **local Ollama** with Claude retained only as an optional
fallback, and the startup log states *"provider routing active; default: ollama"*. The default
inference path is **local and sovereign** — no learner text leaves the institution unless someone
configures it to. Requirement IDs (**RF-21** prompt templates, **RF-22** Open edX sync, **RF-23**
provider routing) are traceable to the project's requirements document, which is the kind of
engineering a ministry audit can follow, and the code carries honest `TODO(tech-debt)` comments
about its own Alembic migration debt.

**Treat it as a collaboration target and a regional reference, not as a base to promise a delivery
date on.** The highest-value contribution Globant could make to it is small and obvious: the
frontend, the Open edX plugin and the test suite that its README already specifies.

## Grading & assessment agents

`p871` recorded this category as empty. It is not — `p872` found and verified one real
permissive system. The table is one row long because one row verified.

🟢 **`p878` changes the answer this section gives, without adding a row to it.** The two repos
below are the only permissive grading *agents* this KB has verified, and both are small. But
automated grading at production scale now exists under permissive licences as **platform**
functionality: **`ls1intum/Artemis`** (MIT, 832 ★) builds, tests and statically analyses programming
submissions automatically and combines manual assessment with **feedback suggestions** via
`Athena`; **`autolab/Autolab`** (Apache-2.0, 808 ★, CMU) is a course-management service built around
auto-graded programming assignments. 🔵 **If the engagement is "grade programming work at scale,"
start from one of those platforms, not from the two rows below.** If it is "score free-text essays,"
the rows below are still the state of the permissive art — and still small. Full entries in
`verticals/solutions.md`; recipe in **P17**.

| Agent | Repo | Licence | Default branch | What it does |
|---|---|---|---|---|
| **ArguLens** | https://github.com/wwrwbs/AI_AWE | Apache-2.0 | `main` | Automated essay scoring **with label-aware feedback** for argumentative essays. Scores 1–6, labels every sentence as `claim`/`data`/`counterclaim`/`rebuttal`, and generates written feedback. Three decoupled parts: a fine-tuned **Qwen2.5-7B LoRA** discourse classifier (`infer/infer_qwen.py`), a **grade-independent LightGBM scorer over 31 linguistic/discourse features** (`scoring_pipeline/scorer.py`) — not an LLM — and a feedback generator on local Qwen2.5-14B-Instruct via vLLM (`feedback/`). Gradio UI with batch upload and JSON/CSV/Markdown export; `hf`/`vllm`/`api` backends; `pytest` suite. Paper arXiv:2608.17356 (18 Aug 2026). |
| **WriteRight** | https://github.com/PritK99/WriteRight | MIT | `main` | Minimal MIT essay scorer (1–10 across several criteria). Lightly maintained — a reference implementation to read, not a base to build on. |

🟢 **`p877` — what the ArguLens `LICENSE` actually contains, and why it matters commercially.**
The 1,865-byte file is Apache-2.0 short-form **followed by a component manifest** — which is why
GitHub returns `NOASSERTION` on an otherwise clean permissive grant. The manifest is the useful
part, because it discloses what you would and would not be allowed to ship:

| Component | Grant as stated in-file | Consequence for a build |
|---|---|---|
| Project source, **LoRA adapters**, LightGBM scorer | Apache-2.0 | Shippable. The adapters being in-scope is the unusual and valuable part. |
| `TextComplexityToolkit` (vendored under `essay_score/scoring_pipeline/`) | **MIT** | Shippable; vendored in-tree, so no resolution step. |
| `TAALED` (inside the toolkit) | "permissive; see notice" | 🟡 Not named to an SPDX id — read it before redistribution. |
| **Qwen2.5-7B-Instruct** base model | Apache-2.0, **obtained separately from Hugging Face; NOT redistributed** | You must acquire the weights yourself; they are not in the grant you receive here. |
| **Persuade 2.0 corpus** | original **academic-use** licence, **NOT redistributed** | 🔴 **The training corpus is academic-use.** Re-fitting on client data is not optional polish — it is how you avoid inheriting a non-commercial data grant. |

🔴 **The file also carries an explicit bias NOTICE, and it should be quoted into any assessment
proposal rather than paraphrased:** AES systems *"may exhibit biases inherited from their training
data (e.g., Persuade 2.0 consists of US middle-school argumentative essays)"* and the software is
*"intended for research and assistive use, not for high-stakes automated decisions without human
oversight."* Under the EU AI Act, **scoring exams is Annex III high-risk** — so the upstream
author's own notice and the regulator's classification agree, and a human-review gate is mandatory
either way. See `compose/patterns.md` **P2** and **P4**.


**Why ArguLens is worth the attention and the dozen other "AES" repos are not.** The score comes
from a **feature-based LightGBM model, not a language model**. That makes it inspectable,
reproducible, and defensible on appeal — which is precisely what every automated-decision regime
demands: Brazil's LGPD right to review of automated decisions, the EU AI Act high-risk tier for
assessment, and Vietnam's Decision 33/2026/QD-TTg. "The model said 4" cannot be defended to an
appeals board; "these 31 measured features produced 4, and here is the same result on re-run" can.

**Maturity flags — read before proposing it.**

- **v0.1.0 and early.** Adapter weights ship as a separate GitHub release asset, and the README
  states adapter weights must be published before public release.
- **README scopes it to "research and assistive" use** and says high-stakes decisions require
  human oversight. Honour that: wire it behind a human override, never as the deciding step.
- **Corpus is Persuade 2.0** — US middle-school argumentative essays, academic-use with
  attribution, not redistributed (prepared locally via `prepare_persuade.py`). The README's own
  bias and generalisation warning applies to any other learner population, and **doubly to any
  non-English deployment**: nothing in this system has been shown to transfer to Spanish or
  Portuguese, which is exactly the LATAM engagement case. Re-fitting the scorer on local graded
  essays is a required work item, not an optional refinement.
- **Dependency chain is clean:** code/adapter-config/scorer Apache-2.0; vendored
  `TextComplexityToolkit` MIT (wraps TAALED, QuanSyn, L2SCA/neosca, spaCy); Qwen2.5 base
  Apache-2.0; spaCy model MIT/CC. The closed-source TAMMI/TAALES/TAASSC tools are deliberately
  excluded, so there is no proprietary dependency to license.

## General-purpose agents composable into education builds

Education-native projects are thin above the tutoring layer, so most real engagements
compose a general agent framework. These were verified on the same two channels this run.

| Agent / framework | Repo | Licence | Default branch | Education role |
|---|---|---|---|---|
| **LibreChat** | https://github.com/LibreChat-AI/LibreChat | MIT | `main` | Multi-model chat front end with per-user auth, agents and RAG. The usual choice when an institution needs a self-hosted, model-agnostic assistant it can put in front of students without sending data to a vendor. |
| **OpenHands** | https://github.com/OpenHands/OpenHands | MIT | `main` | Coding agent. In education: autograding harnesses, scaffold generation for CS courses, and migration work on legacy LMS plugins. |
| **LangGraph** | https://github.com/langchain-ai/langgraph | MIT | `main` | Stateful graph orchestration. The control layer where a pedagogical policy (hint ladders, mastery gates, escalation to a human teacher) is expressed as explicit nodes you can audit. |
| **CrewAI** | https://github.com/crewAIInc/crewAI | MIT | `main` | Role-based multi-agent orchestration — maps cleanly onto teacher / tutor / assessor / moderator role splits. |
| **gpt-researcher** | https://github.com/assafelovic/gpt-researcher | Apache-2.0 | `main` | Cited multi-source report generation; used for literature-review scaffolding and course-material drafting. |
| **STORM** | https://github.com/stanford-oval/storm | MIT | `main` | Stanford OVAL. Generates Wikipedia-style grounded articles from scratch with citations — a strong base for curriculum and explainer drafting with a traceable source trail. |

🟡 **`p876` corrected two addresses in the table above.** LibreChat is now
`LibreChat-AI/LibreChat` (**47,237★**, MIT, pushed 2026-11-17) and OpenHands is now
`OpenHands/OpenHands` (**93,647★**, MIT, pushed 2026-11-17). The previous addresses
(`danny-avila/`, `All-Hands-AI/`) are redirects: they clone, they serve licence bytes, and
`api.github.com/search/repositories?q=repo:<old>` returns **`422 Validation Failed`** — which is
the only signal this KB has that a slug has stopped being canonical. 🔵 **A verification method
built on bytes alone is structurally blind to a rename.**

## Institutional AI subsystems — new in `p878`

Not tutors, and not frameworks. These are the **AI microservices of a production university
platform**, published as separate MIT repositories and usable on their own. They are listed here
because they are the only education AI code in this KB that was **built to be governed**: the
platform that ships them states that they are *"optional, configuration-gated integrations"* and
that *"instructors and tutors stay responsible for assessment decisions."*

| Component | Repo | Licence (byte-read) | ★ | Pushed | What it does |
|---|---|---|---:|---|---|
| **Edutelligence** (Iris / Athena / Hyperion) | https://github.com/ls1intum/edutelligence | **MIT** | 17 | 2026-11-17 | The AI microservice suite for Artemis. **Iris** is the learner-facing tutor; **Athena** generates *feedback suggestions* for human tutors on text and modelling exercises; **Hyperion** is the newest member. Python. |
| **Pyris** | https://github.com/ls1intum/Pyris | **MIT** | 12 | 2026-06-03 | The standalone LLM microservice behind Iris. Smaller surface than `edutelligence`; useful if you want the LLM seam without the suite. |
| **Ares** | https://github.com/ls1intum/Ares | **MIT** | 27 | 2026-11-03 | **Secure sandboxed execution for auto-graded Java.** A JUnit 5 extension — the piece every auto-grading build needs and almost nobody writes safely. Reusable with no Artemis dependency. |
| **Apollon** | https://github.com/ls1intum/Apollon | **MIT** | 106 | 2026-11-17 | UML modelling editor. Drives Artemis's modelling exercises; ships standalone (`Apollon_standalone`) and as a VS Code extension. |

🔵 **Why `Athena` is the architecturally interesting one.** It produces **feedback *suggestions* for
a human assessor** rather than grades. That is precisely the design the EU AI Act's Annex III
treatment of grading pushes towards (see **T11**), and precisely what DC's 2026-27 guidance and
Florida's opt-out rule assume (see `intel/market.md`, North America). **Most open-source grading
code in this KB assumes the model decides. This one assumes a person does, and makes the model
argue for a decision.** For any engagement in a regulated jurisdiction that is the cheaper posture
to defend.

🟡 **Maturity, stated honestly.** 12–106 stars each. These are components of an 832-star platform,
not independent products — adopt them with the platform, or read them as reference designs and
budget the integration. The sandbox (`Ares`) is the one most likely to be worth lifting on its own.

🔴 **One flagged non-dependency, for reference reading only.**
**https://github.com/virtualryder/edu-ai-agents** — **MIT** (byte-read) — is the only repository
found this pass built explicitly around **FERPA / COPPA / IDEA-504 / ADA Title II**, with
deny-by-default authorisation, student-PII masking, human-in-the-loop enforcement and a
tamper-evident audit trail, as eight reference workflows on Amazon Bedrock. **It measures 4 stars
and was last pushed 2026-10-10.** Secondary coverage presented it as a notable release; the
measurement does not support that. **Read it as a compliance checklist for P15. Do not depend on
it.**

## Licence flags — read before proposing any of these to a client

| Project | Nominal licence | The actual constraint |
|---|---|---|
| **Open WebUI** | "Open WebUI License" | BSD-3-clause text **plus an added clause 4**: altering, removing or replacing Open WebUI branding is prohibited unless the deployment has **≤50 end users in any rolling 30 days**, or you hold written permission or an enterprise licence. Read the bytes: this is *not* plain BSD. A white-labelled campus deployment above 50 users is a material breach. |
| **MinerU** | **"MinerU Open Source License"** — Apache-2.0 + additional terms | **Terms read by `p872`.** A separate **commercial licence** is required above **100M MAU** or **USD 20M monthly revenue** (consolidated with affiliates), plus an **online-service attribution obligation**. Neither threshold binds a normal institutional deployment; the attribution obligation binds any hosted service immediately. This is the KB's one genuine "Apache-2.0 plus terms" case. |
| **MultiAgent-AI-Teaching-Assistant** | **none** | `github.com/YoussefMohAttia/MultiAgent-AI-Teaching-Assistant` exists but has **no licence file on its default branch**. No licence means no grant — Globant cannot build on it. Recorded so no later pass re-imports it from a blog listing. |
| **EduTwin Africa** | **none** | `github.com/muskvdc/EduTwin-Africa` — curriculum-aware tutor with RAG, bounded multi-agent collaboration and guardrails, scoped to **South African Grades 8–12**. Exists on `main`; **no `LICENSE`, `LICENSE.md` or `COPYING`**. Africa-origin and legally unusable as it stands. Found by `p873`. |
| **multiagent-ai-tutor** | **none** | `github.com/giovanayngrid-gk/multiagent-ai-tutor` — Brazilian, Portuguese-language, LangChain + Llama 3 via local Ollama + Streamlit. Exists on `main`; **no licence file**. Found by `p873`. |
| **educational-agents** | **none** | `github.com/nifalconi/educational-agents` — Spanish-language teaching library with LATAM Spanish identifiers, from a *Niñas Pro* agents course. Exists on `main`; **no licence file**. Found by `p873`. |
| **Lenda AI** | **claimed Apache-2.0, unverifiable** | Self-describes as an Apache-2.0 LATAM-built open-source tutor (v0.1). **Not listed in this KB:** `lenda.ai` does not resolve from this session, no independent coverage exists, and `git ls-remote` found nothing at four plausible namespaces. **A licence claim on a project page is not a licence.** |
| **Frappe LMS** | **AGPL-3.0**, not MIT | Multiple 2026 LMS listicles state Frappe LMS is MIT. The licence bytes at `frappe/lms@develop/license.txt` are **GNU Affero GPL v3**. Corrected this pass. |
| **OpenProctor** | **AGPL-3.0**, not MIT | `github.com/kamlendras/OpenProctor` is listed as MIT in secondary sources. The licence bytes on `main` are **AGPL-3.0**. Corrected `p872`. |
| **os-taxonomy** | **ODbL**, not a code licence | `github.com/withmarbleapp/os-taxonomy` exists, but its `LICENSE` is the **Open Data Commons Open Database Licence** — share-alike on derived *databases*. It is a curriculum dataset, not permissive code. Do not file it beside MIT/Apache repos. |
| **Any Apache-2.0 repo** | *not* "Apache-2.0 + additional terms" | **Method warning.** Apache-2.0 §5 contains the phrase *"without any additional terms or conditions"*, so a substring grep for `additional terms` false-positives on **100%** of Apache-2.0 projects. `p872` hit this on seven repos (DeepTutor, agents-course, ltijs, Ed-Fi-ODS, oppia, OpenOlat, openedx-aspects) and **discarded the flag rather than publishing it**. MinerU remains the one genuine case, because its `LICENSE.md` adds substantive prose terms. Licence characterisation requires reading the bytes, not matching a substring. |

## Declared gaps — searched and not found

An informed gap is information; silence looks identical to coverage. `p873` moved the two
regional-origin gaps that had stood longest; what remains is stated as precisely as the evidence
allows.

- ~~**No mature open-source grading / assessment agent exists.**~~ **CLOSED by `p872`.**
  **ArguLens** (`wwrwbs/AI_AWE`, Apache-2.0, arXiv:2608.17356) is real, verified, decomposed and
  permissive. It is **v0.1.0 and research-grade**, and its corpus is US middle-school English —
  so the honest statement is now *"a permissive grading system exists and needs hardening and
  re-fitting"*, not *"nothing exists"*. `edx-ora2` (AGPL-3.0) remains the production substrate
  for the human-workflow half; ArguLens is the scoring half. **Still an open build opportunity
  for Globant — but now as hardening a real base, which is a far cheaper proposal than greenfield.**
- **No permissively licensed open-source proctoring platform exists — now evidenced, not assumed.**
  `p872` verified two real candidates and **both are AGPL-3.0**: `sudosylabs/proctor` (Go+React,
  the most complete) and `kamlendras/OpenProctor`. Copyleft is workable for a single
  institution's self-hosted deployment and unusable in a distributed product. Given that the EU
  has moved proctoring into the high-risk tier and Vietnam now lists biometric learner monitoring
  as a high-risk education system, the strategic answer is more likely **assessment redesign than
  better proctoring**.
- **No education-native agent carries an accessibility conformance statement except OATutor.**
  Still true after a dedicated `p873` search leg, but the gap now has an **architectural answer**
  rather than just a single fallback. `CAHLR/OATutor` (MIT) remains the only agent in this file
  with a published conformance document. What `p873` adds is that the **platform** layer has
  conformance even where the agent layer does not: **Moodle core and its mobile app are stated to
  be WCAG 2.2 AA certified** (vendor claim, Open LMS — unverifiable from this session, so treat as
  a claim to request the VPAT/ACR for, not as a fact). The consequence for a bid is concrete:
  **put the agent behind a conformant platform's UI over LTI 1.3 rather than shipping your own
  front end**, and the conformance story rides on the platform. Note also that the obligation is
  tightening — the **European Accessibility Act has applied since 28 June 2025**, and the next
  **EN 301 549** revision aligning it to WCAG 2.2 AA is reported as due in the Official Journal in
  late 2026 (secondary-sourced; all EU primary sources are unreachable from this session). And the
  standard failure mode is not the platform at all: an accessible platform routinely serves
  inaccessible embedded content — the SCORM package, the PDF workbook, the generated slide deck.
  **An AI content generator is a content generator: whatever it emits inherits the conformance
  obligation.** See `compose/patterns.md` **P10**.
- **Star counts unmeasurable for the third consecutive pass, now across four routes** —
  `api.github.com`, `github.com` HTML, the `gh` CLI (*"not in this session's authorized repository
  set"*) and `gh api search/repositories` (empty set). This is a session scope, not a GitHub
  outage. Not inferred from blogs: secondary sources this pass offered ~48.9k, ~54k and ~59.9k for
  the same project within three weeks, which is exactly why none of them is recorded. No star
  figure appears anywhere in this KB.
- **Every non-GitHub host is unreachable from this session**, on both `curl` (`000`) and `WebFetch`
  (`ENOTFOUND`): `arxiv.org`, `aclanthology.org`, `doi.org`, `sciencedirect.com`, `unesco.org`,
  `eur-lex.europa.eu`, `data.consilium.europa.eu`, `europarl.europa.eu`, `edworkingpapers.com`,
  `multistate.us`, `ipsos.com`, `lenda.ai`. So **repository facts and document facts in this KB
  sit on different evidential footings**: repos are read first-hand (existence, branch, tags,
  licence bytes, source files), while every paper, survey and regulatory date is a search engine's
  summary of a page that cannot be opened. Flagged wherever it matters. These hosts would need
  allowing in the session's network settings.
- ~~**No LATAM-origin education-native agent surfaced.**~~ **CLOSED by `p873`.** **TutorIA**
  (`LabSirius/TutorIA`, **MIT**, Universidad Tecnológica de Pereira, Colombia) is verified, listed
  above, and publicly funded. `p872`'s refinement — *"LATAM's contribution is a sovereign
  foundation model, not an education agent"* — **is retired as wrong.** Both are true at once, and
  they stack: **Latam-GPT** (CENIA-led, launched **10 Feb 2026**, Llama-3.1-70B base, 230B+ words
  of Spanish/Portuguese including education sciences, open weights under the `latam-gpt` Hugging
  Face org, **corpus gated behind a CENIA-evaluated request and an NDA** — so "open source"
  describes the weights, not the data) is the model layer, and TutorIA is an agent layer that
  already defaults to a locally served model. The residual gap is **maturity, not existence**:
  TutorIA is a backend in progress, so LATAM-origin OSS is real but not yet production-grade.
- **Africa-origin education agents exist, and not one of them has a licence.** `p873` resolved
  three Global-South tutors with **no licence file on their default branch** — `muskvdc/EduTwin-Africa`
  (South African Grades 8–12), `giovanayngrid-gk/multiagent-ai-tutor` (Brazil, Portuguese) and
  `nifalconi/educational-agents` (LATAM Spanish). No licence means no grant, so all three are
  legally unusable however good the code is. **The discriminating variable appears to be funding:**
  the one regional project that *is* licensed, documented and branch-managed (TutorIA) is the one
  with a national science ministry behind it. Two further Africa-origin research systems —
  **EduNaija AI Tutor** (AfricaNLP 2026; Nigerian curriculum; English/Yoruba/Hausa/Igbo) and
  **AFRILANGTUTOR** (Findings of EMNLP 2026, arXiv:2604.20996) — claim open releases but **no
  repository address could be resolved** and `aclanthology.org`/`arxiv.org` are unreachable from
  this session. Recorded as leads; **no address has been invented.** Next pass: try Hugging Face.
- **Education-native OSS origin is still concentrated** in East Asian university labs (HKUDS/HKU,
  THU-MAIC/Tsinghua) and US universities (CAHLR/Berkeley). TutorIA widens the map; it does not
  change the centre of gravity.
- **No agent in this file has published learning-outcome evidence for itself.** `p872` found the
  trial literature (see `intel/trends.md` **T9**) and none of it evaluates any repo named here.
  The largest trial — 2,379 undergraduates — found a **negative** effect from course-integrated
  AI tutor access. Treat every efficacy claim in this file as a capability description, not an
  outcome claim.
