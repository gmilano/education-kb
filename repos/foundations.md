---
industry: education
region: Global
updated: 2026-11-17
---

# Foundational repos — education

**Pass `p877`, 2026-11-17** (seventh pass of the day). **`p877` closes a declared gap that has
stood in this file since `p872`, and adds the largest permissive education repository the KB has
ever failed to shelve.**

> **🟢 THE "NO PERMISSIVE SIS" GAP IS CLOSED. [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12)
> is MIT** — byte-read on `main`, **1,150 B**, `sha256₁₂ b8694396d7dc`, first line `MIT License`.
> A full-featured school management system in **Laravel**, API-first, Dockerised, with companion
> Android parent and teacher apps. **113 commits in the last 12 months.** Every SIS this KB had
> until now (Gibbon GPL-3.0, openSIS GPL-by-README-only, RosarioSIS GPL-2.0) was copyleft.
>
> 🔵 **Why four passes missed it, and this is a new method lesson:** the GitHub API reports
> `NOASSERTION` for this repository, because **line 3 of its `LICENSE` is
> `<!-- SPDX-License-Identifier: MIT -->`** — an added line that breaks stock-text matching. The
> detector was never saying "no grant"; it was saying "not byte-identical to a template".

> **🔴 `NOASSERTION` CARRIES ZERO INFORMATION ABOUT THE GRANT, and `p877` proves it with three
> repositories in one pass that share the signal and share nothing else:**
>
> | Repository | GitHub says | Bytes say | Verdict |
> |---|---|---|---|
> | `Gego-K12/gegok12` | `NOASSERTION` | MIT + an SPDX comment line | 🟢 **Permissive — more usable than it looked** |
> | `wwrwbs/AI_AWE` | `NOASSERTION` | Apache-2.0 short-form + component manifest | 🟢 **Permissive — and the manifest is itself useful** |
> | `CaviraOSS/PageLM` | `NOASSERTION` | bespoke non-commercial "Community License" | 🔴 **Not open source at all** |
>
> Three identical signals, three different commercial answers. **The detector collapses "more
> permissive than it looks", "fine but annotated" and "not open source at all" into one token.**
> Registered as `intel/trends.md` **T14**. This is the mirror image of `p872`'s substring-grep
> lesson: that one produced false *alarms*, this one produces false *absences* — and a false
> absence is worse, because nobody re-checks a repository already written off.

> **🔴 [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
> — Apache-2.0, 43,849★, 4,526 forks, 813 commits in 12 months — appeared in ZERO curated files
> before this pass.** It is the **second-largest education-native repository in this entire KB**,
> behind only DeepTutor, and it sat only in sweep logs and archives. Added below, to
> `verticals/solutions.md`, and wired into `compose/patterns.md` **P5**, whose offline stack was
> built without it.

**Previous pass note (`p876`)** (sixth pass of the day). **`p876` is a propagation audit, not a
discovery pass**, and it closes the gap `p875` opened one pass earlier — *in the same pass that
`p875`'s own sweep had already measured the answer*.

> **🟢 THE LRS GAP IS CLOSED. `p875` wrote "no maintained permissive LRS exists" into four files
> while its own sweep table (`agents/trending.md`, leg `xAPI learning record store stars:>15`)
> listed three.** Two of them are permissive **and** maintained:
> **`yetanalytics/lrsql`** (Apache-2.0, 144★, **67 commits in the last 12 months**) and
> **`openfun/ralph`** (MIT, 52★, from France Université Numérique, with **native Open edX
> tracking-log → xAPI converters in-tree**). Both are now rows in the new *Learning analytics &
> telemetry* section below. 🔵 **The method lesson: this KB's discovery channel is ahead of its
> curated shelf. A finding that is measured and not propagated is not yet knowledge** — it is a
> line in an 84,000-line log that the next proposal will not read.

> **🔴 AND THE DORMANCY WAS UNDERSTATED BY 2.5 YEARS.** `p875` recorded LearningLocker as *"18
> months"* dormant from its `pushed_at` field. **Its default branch's last commit is
> `2021-11-16` — 1,827 days, five years.** `p876` re-measured every address in this file by
> cloning it (`--filter=blob:none --bare`) and reading `git log -1 HEAD`, which is the branch a
> clone actually gives you. **83 of 83 clones succeeded.** See `repos/trending.md` `p876` for the
> full divergence table and two further stale rows this caught.

**Previous pass note (`p875`)** (fifth pass of the day). **`p875` closes the star gap and uses it to
audit this file rather than to decorate it.** 78 addresses measured first-hand via
`api.github.com/search/repositories` — the channel four passes called impossible (see
`repos/trending.md` for how it was found). The measurement produced **three corrections to this
file that no licence check could have produced**:

> **🟡 1. A duplicated address, now collapsed.** This file carried **two rows for the same
> project** — `edx/edx-ora2` and `openedx/edx-ora2` — because `p872` added the current org without
> removing the legacy one. The measurement settles which to keep: **only `openedx/` resolves in
> the GitHub search index** (64 stars, AGPL-3.0, last push 2026-11-13), while `edx/` returns
> nothing, even though both still resolve over the git protocol via redirect. 🔵 *The git protocol
> follows renamed-org redirects, so an existence check passes on a stale address long after it
> stops being canonical — which is exactly how a duplicate survives a licence-and-existence
> audit.* One row now, `openedx/`.

> **🔴 2. The xAPI layer is unmaintained, and it is the one this KB's measurement pitch rests on.**
> 🟢 **`p876`: the second half of this item — "no maintained permissive LRS" — is WITHDRAWN as
> wrong; see the banner above. The first half is CONFIRMED and sharpened: the dormancy is five
> years, not 18 months.** Original `p875` text retained below for the record.
> `LearningLocker/learninglocker` (587 stars) **has not been pushed since 2024-05-30 — 18
> months**. `intel/trends.md` T9 argues that *measurement* is the defensible deliverable in this
> vertical, and the Learning Record Store that every such pattern routes telemetry into is
> dormant. **`p875` did not find a maintained permissive LRS and does not invent one.** Any
> engagement promising measurement must either budget "we operate this fork" into the statement of
> work, or use the LMS's native gradebook and accept the weaker evidence. **This is now the
> highest-value unfilled slot in the education open-source stack.**

> **🟡 3. Two more foundations are quiet.** `1EdTech/openbadges-validator-core` (61 stars, last
> push 2025-11-04) — from the standards body, so more likely *finished* than abandoned, but do not
> present it as actively developed. `stanford-oval/storm` (31,901 stars, last push 2025-09-30) —
> **high stars, 14 months idle; stars and liveness are independent signals** and this file should
> not let one stand in for the other.

A licence mismatch worth carrying to a client conversation: **`OpenOlat/OpenOlat` and
`BerriAI/litellm` both return `NOASSERTION` from GitHub's SPDX detector** while their licence bytes
read Apache-2.0 and MIT. The byte-read is authoritative — the cause is almost certainly a modified
licence header — **but a client's counsel will run the automated check and get `NOASSERTION`.
Brief them before they ask.** Full table in `repos/trending.md`.

**Previous pass note (`p874`):** added `moocupv/lti-ai-grader` to the standards layer and
established that star counts had failed across nine routes. `p875` supersedes that diagnosis: the
failure was an egress allowlist for non-GitHub hosts **plus** a wrong generalisation about GitHub
itself. `moocupv/lti-ai-grader` measures **0 stars** — consistent with its listing as a component
to harvest rather than a project to adopt.

`p872` re-resolved every load-bearing address in this file through `git ls-remote --symref` and
found **four of eleven do not default to `main`**. Branch column corrected below where it was
wrong, and `openedx/` recorded as the live org for `edx-ora2`.

These are the load-bearing pieces an education build sits on: the standards plumbing that
makes a tool interoperable with institutional systems, and the AI substrate that makes it
work. The standards layer matters more here than in most verticals — an education tool that
cannot speak LTI, xAPI/Caliper, QTI or Ed-Fi cannot be bought by a school district.

## Education standards & interoperability

This is the layer that gets a Globant build past institutional procurement.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | `master` | **LTI 1.3 / LTI Advantage tool provider in Node.** The single most reusable piece of plumbing in education software: implement it once and your agent launches as a tool inside Moodle, Canvas, Open edX, Blackboard and D2L with grade passback. Permissive — safe to embed. |
| https://github.com/moocupv/lti-ai-grader | Apache-2.0 | `main` | **The first verified permissive AI grader that actually speaks the LTI seam.** From MOOC UPV (Universitat Politecnica de Valencia, Spain — EMEA-origin). An LLM grader that posts grades back to an LMS, *tested with Open edX and Moodle*; configurable grading prompts, Gemini or any OpenAI-compatible API, multi-language templates, and a private/public file split that keeps logic and secrets out of the web root. Tag `excel-v1.0`. **Caveat that governs how to use it: it is LTI 1.1 (OAuth 1.0a), the deprecated generation — not 1.3.** Take its grading core and prompt configuration, and swap the transport for `ltijs` above to get a 1.3/Advantage launch with AGS passback. Added by `p874`; licence byte-read on `main`. |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 | `main` | **Ed-Fi Operational Data Store + API.** The de-facto K-12 data standard in US school districts. Apache-2.0, so a district-facing analytics or early-warning agent can build directly on it. |
| https://github.com/1EdTech/openbadges-validator-core | Apache-2.0 | `develop` | Open Badges validation from the standards body itself (1EdTech, formerly IMS Global). The verification half of any credentialing or micro-credential build. |
| https://github.com/Citolab/qti-components | GPL-3.0 | `main` | **QTI 3 web components** — standards-compliant assessment item rendering. Copyleft: fine for a self-hosted institutional deployment, a problem for a proprietary distributed product. |
| https://github.com/openedx/edx-ora2 | AGPL-3.0 | `master` | **Open-response assessment** — rubrics, peer assessment, self assessment, staff grading. Given that no mature OSS grading *agent* exists (see `agents/top.md` gaps), this is the realistic production substrate for AI-assisted grading. AGPL: network-use triggers source obligations. **64 stars, last push 2026-11-13** (`p875`). **`p875` collapsed the duplicate `edx/` row that stood here:** both org forms resolve over the git protocol via redirect, but only `openedx/` resolves in the GitHub search index, so `openedx/` is the single canonical address this KB carries. |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | `master` | **xAPI Learning Record Store.** 🔴 **SUPERSEDED by `p876` — do not start here.** 587 stars. `pushed_at` reports `2024-05-30`, but the **default branch's last commit is `2021-11-16` — 1,827 days**, and there are **0 commits in the last 12 months**. Copyleft *and* five years cold. Retained in this file only so that a later pass does not re-import it from a listicle. **Use `yetanalytics/lrsql` or `openfun/ralph` below.** |
| https://github.com/openedx/openedx-aspects | Apache-2.0 | `main` | Open edX's learning-analytics stack (Aspects). Apache-2.0 and reusable even outside an Open edX deployment. |
| https://github.com/jupyter/nbgrader | BSD | `main` | Assignment release, collection and autograding for Jupyter notebooks. The standard autograder in university CS and data-science courses. |
| https://github.com/jupyterhub/jupyterhub | BSD | `main` | Multi-user notebook hosting — the substrate for every hands-on technical course delivered in a browser. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | `main` | **FSRS** — the modern free-spaced-repetition scheduler. MIT-licensed, empirically validated memory model. If your product claims retention, this is the algorithm to use instead of inventing a review schedule. |

## Learning analytics & telemetry (xAPI) — new in `p876`

This section exists because `intel/trends.md` **T9** argues that *measurement* is the defensible
deliverable in this vertical, and until this pass the only Learning Record Store this KB carried
was copyleft and five years dead. Every row was verified on four channels this pass: existence and
default branch via `git ls-remote --symref`, licence **bytes** from `raw.githubusercontent.com`,
stars/SPDX via `api.github.com/search/repositories`, and **liveness via a blobless bare clone and
`git log -1 HEAD`** — not the `pushed_at` field, which is what produced the error above.

| Repo | Licence | Branch | Stars | HEAD | Commits/12mo | Why it is foundational |
|---|---|---|---|---|---|---|
| https://github.com/yetanalytics/lrsql | Apache-2.0 (11,357 B) | `main` | 144 | 2026-11-14 | **67** | **Yet Analytics SQL LRS — the maintained permissive LRS, and the default recommendation.** A full xAPI LRS (statements, attachments, documents, per xAPI spec Part 3) over ordinary SQL: **SQLite embedded, Postgres 14–18, MariaDB 10.6–11.8, MySQL 8.0–9.5**. Ships a Docker image, **OIDC support** (with an Auth0 setup guide), a TLS/HTTPS guide, a documented AWS deployment, and a "Reactions" rules engine for triggering on statement patterns. Clojure. Latest tags `v0.9.14`, `v1.0.0-pre_ui_testing`. **This is the row that replaces LearningLocker in P1, P7 and P9.** |
| https://github.com/openfun/ralph | MIT (1,094 B) | `main` | 52 | 2026-10-12 (`v5.1.0`) | 18 | **The EMEA, public-sector, Open edX-native option — and the only MIT one.** From **OpenFUN (France Université Numérique)**, the consortium that operates France's national Open edX platform. Three things in one: an **LRS HTTP API** (FastAPI, `src/ralph/api/`, with **basic *and* OIDC auth** and statement forwarding), a **CLI** for building data pipelines, and a **library**. 🟢 **Verified in-tree, not from the README: `src/ralph/models/edx/` holds event models and `converters/` for Open edX tracking logs, alongside `src/ralph/models/xapi/`** — so Open edX telemetry becomes xAPI without writing the mapping yourself. Ships a **Helm chart** (`src/helm/ralph/`) and a PyPI package (`ralph-malph`). Community support runs through **ESUP**, the French higher-education consortium. |
| https://github.com/adlnet/ADL_LRS | Apache-2.0 (11,357 B) | `master` | 335 | 2025-11-14 | 0 | **The reference implementation, from the body that wrote the specification** — ADL, authors of xAPI. Python/Django. 🟡 **Liveness flag: 0 commits in the last 12 months.** Treat it as the conformance *reference* to test against and read, not as the production substrate: for that, use `lrsql`. Highest star count of the three, which is reputation rather than momentum. |

**How to choose between them.** Take **`lrsql`** by default — it is the most active (67 commits in
12 months against ralph's 18), it speaks four DBMS families so it drops into whatever the
institution already runs, and Apache-2.0 carries an explicit patent grant. Take **`ralph`** when
the deployment is **Open edX** (its converters are the work you would otherwise do by hand), when
the client is **European public sector** and a French public-consortium provenance plus MIT is
worth more than raw commit velocity, or when the pipeline matters as much as the store. **Neither
is a drop-in for LearningLocker's dashboards** — Learning Locker bundled a reporting UI, and these
are stores and pipelines. Budget the visualisation layer explicitly (Aspects/Superset, or Grafana
over Postgres); do not let a statement of work imply dashboards come free.

## Curriculum structure — new in `p875`

The layer that tells a tutoring agent *what comes before what*. Without it, "personalised learning
path" is a prompt, not a data structure.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-1.0** | `main` | **A 1,590-topic children's curriculum graph with 3,221 prerequisite edges** — the prerequisite relation is the part that is hard to build and expensive to buy, and this is the only open one this KB has found. **7,720 stars, last push 2026-11-16** — real traction, actively maintained. 🔴 **Read the licence before you plan around it: Open Data Commons ODbL is a share-alike *database* licence, not a software licence.** Using it to drive a service is fine; **publishing a derived or extended database triggers share-alike obligations on that database.** It is therefore *not* in the MIT/Apache class this KB otherwise prefers and must never be filed as permissive. The safe pattern is to consume the graph as reference data behind a service and keep client-specific curriculum extensions in a separate store you do not redistribute. |

🟡 **Gap this exposes rather than closes:** there is **no permissive** open curriculum graph. If a
client needs to own and redistribute a prerequisite taxonomy, it is bespoke work — and `os-taxonomy`
is still the best thing to read first when scoping it.

## Permissive institutional platforms — new in `p877`

Rows measured first-hand this pass: existence and default branch by `git ls-remote --symref`,
licence by byte-read on `raw.githubusercontent.com`, traction by `search/repositories`, liveness
by blobless bare clone (`git log -1 HEAD`), per the `p876` method.

| Repo | Licence (byte-read) | Branch | ★ | HEAD | Commits/12mo | Why it is here |
|---|---|---|---:|---|---:|---|
| https://github.com/Crosstalk-Solutions/project-nomad | **Apache-2.0** (10,778 B) | `main` | **43,849** | 2026-11-08 | **813** | **Offline-first knowledge and education server** — Wikipedia, thousands of books, courses, maps and **optional local AI**, all served from one box with no internet. Apache-2.0, Dockerised, `collections/`, `admin/`, `install/` in-tree, semantic-release. **4,526 forks** is the number that matters: forks of an appliance repo are deployments, not stars. This is the natural substrate for every ministry equity programme and rural-school bid in `compose/patterns.md` **P5**, and it is permissive where Internet-in-a-Box (LGPL) and Kiwix (GPL-3.0) are not. |
| https://github.com/Gego-K12/gegok12 | **MIT** (1,150 B, `sha256₁₂ b8694396d7dc`) | `main` | 57 | 2026-06-25 | 113 | **The first permissive student-information system in this KB** — closes the standing gap below. Laravel/PHP, **API-first by design** (`api.md` in-tree), `Dockerfile` + `docker-compose.yml`, `lang/` for localisation, plus separate Android **parent** and **teacher** apps. 🟡 **Low stars and HEAD five months cold** — this is a small project, and it should be proposed as *a permissive base you will own and extend*, not as a mature product with a community behind it. Its value is the licence: it is the only SIS here you can fork, rebrand and ship inside a proprietary deliverable. 🔴 GitHub reports `NOASSERTION`; the bytes say MIT. |

## Document & media ingestion — the real bottleneck in education AI

Education content arrives as PDFs, scanned worksheets, lecture video and textbooks. Ingestion
quality, not model quality, is what usually determines whether a tutoring build works.

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/docling-project/docling | MIT | `main` | Document parsing to structured output (IBM-originated, now a Linux Foundation AI project). MIT, strong on tables and layout — the default first choice for curriculum and textbook ingestion. |
| https://github.com/datalab-to/marker | Apache-2.0 | `master` | PDF → markdown with high fidelity on equations and tables. Strong on STEM textbooks where Docling's maths handling is not enough. |
| https://github.com/opendatalab/MinerU | **"MinerU Open Source License"** (Apache-2.0 + additional terms) | `master` | High-quality PDF extraction including formulas. **Flag sharpened by `p872` — the terms were read, not just noted.** `LICENSE.md` is titled *MinerU Open Source License* and states MinerU is Apache-2.0 **"subject to the additional terms below"**. Those terms include: (1) **a separate commercial licence is required** once you and your affiliates, consolidated, exceed **100 million MAU** *or* **USD 20 million monthly revenue**; and (2) an **online-service attribution obligation**. For a normal institutional education deployment neither threshold binds, so MinerU is usable — but the attribution obligation applies immediately to any hosted service, and the thresholds must be checked before embedding it in a product sold at scale. |
| https://github.com/Unstructured-IO/unstructured | Apache-2.0 | `main` | Broad-format ingestion (docx, pptx, html, email). Useful for the long tail of institutional file formats. |
| https://github.com/openai/whisper | MIT | `main` | Lecture and classroom speech-to-text. MIT weights and code. |
| https://github.com/SYSTRAN/faster-whisper | MIT | `main` | CTranslate2 reimplementation — several times faster, materially cheaper for transcribing a full semester of lecture capture. |

## Retrieval, orchestration & serving substrate

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/HKUDS/LightRAG | MIT | `main` | Graph-augmented RAG. Worth naming explicitly: it is the retrieval engine **inside DeepTutor**, so adopting DeepTutor means adopting LightRAG. MIT. |
| https://github.com/infiniflow/ragflow | Apache-2.0 | `main` | Document-understanding-centric RAG engine with a usable ingestion UI — good fit where institutional staff, not engineers, curate the corpus. |
| https://github.com/deepset-ai/haystack | Apache-2.0 | `main` | Mature, composable RAG/agent pipelines. Apache-2.0 and stable API — the conservative choice for a multi-year institutional contract. |
| https://github.com/BerriAI/litellm | MIT | `main` | One OpenAI-shaped API across providers, with per-key budgets and rate limits. In education this is the cost-control and model-swap seam: a ministry that mandates a sovereign model later changes one config, not the application. |
| https://github.com/ollama/ollama | MIT | `main` | Local model serving. The answer to "student data must not leave the building" and to low-connectivity deployments. |
| https://github.com/vllm-project/vllm | Apache-2.0 | `main` | High-throughput serving. What you run when a whole cohort hits the tutor during one lab session. |
| https://github.com/qdrant/qdrant | Apache-2.0 | `master` | Vector store, Apache-2.0, self-hostable. |
| https://github.com/chroma-core/chroma | Apache-2.0 | `main` | Lighter vector store; fast to stand up for a pilot. |
| https://github.com/mem0ai/mem0 | Apache-2.0 | `main` | Persistent memory layer — the difference between a chatbot and a tutor that remembers a learner across a term. |
| https://github.com/temporalio/temporal | MIT | `main` | Durable workflow execution. Education workloads are long-running and bursty (term-long learning paths, overnight batch grading); Temporal is what keeps them correct across restarts. |

## Evaluation & data quality — how an education claim gets defended

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/promptfoo/promptfoo | MIT | `main` | Prompt/model regression testing and red-teaming. Education needs this for safeguarding checks on learner-facing output. |
| https://github.com/EleutherAI/lm-evaluation-harness | MIT | `main` | Standard academic benchmark harness — the credible way to report model capability to an academic buyer. |
| https://github.com/HumanSignal/label-studio | Apache-2.0 | `develop` | Human annotation, including rubric-scoring interfaces for building graded gold sets. |
| https://github.com/argilla-io/argilla | Apache-2.0 | `develop` | Human feedback and dataset curation, oriented to SME review — fits teacher-in-the-loop validation. 🟡 **`p876` liveness flag, new and not caught by any previous pass: `pushed_at` reports `2026-11-16` (yesterday), but the default branch `develop` last moved `2025-08-05` and has `0` commits in 12 months.** It looks maintained in every star-and-push sweep this KB has ever run and is not. Usable — it is a mature tool — but do not promise upstream fixes. |
| https://github.com/wwrwbs/AI_AWE | Apache-2.0 | `main` | **ArguLens** — automated essay scoring with feedback. Enters the foundations layer because its **scorer is a grade-independent LightGBM model over 31 explicit linguistic/discourse features**, not an LLM: a reproducible, inspectable score is the only kind that survives an appeal or a high-risk conformance review. **v0.1.0, research-grade; corpus is US middle-school English (Persuade 2.0)** — re-fitting on local graded essays is required work, not polish. See `agents/top.md`. |

**36 verified foundational repos** — `p876` adds `yetanalytics/lrsql`, `openfun/ralph` and `adlnet/ADL_LRS`.

**Previous count:** 33 (31 from `p871`, plus `openedx/edx-ora2` recorded as the
canonical address and `wwrwbs/AI_AWE` added by `p872`).

## Declared gaps

- **The permissive/copyleft split is the central licence fact of this vertical.** The AI
  substrate above is almost entirely MIT/Apache-2.0, and the standards plumbing is mixed, but
  the *platform* layer (see `verticals/solutions.md`) is overwhelmingly GPL/AGPL. A Globant
  engagement should expect to build permissive AI services that **integrate with** copyleft
  platforms over LTI/xAPI rather than forking them.
- ~~**No open-source student-information system with a permissive licence was found.**~~
  🟢 **CLOSED by `p877`: [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) is MIT at the
  bytes** (1,150 B, `sha256₁₂ b8694396d7dc`) — a Laravel, API-first, Dockerised school management
  system with companion Android apps, 113 commits in 12 months. It is **small** (57★) and its HEAD
  is five months old, so the gap closes on *licence*, not on *maturity*: the honest statement to a
  client is "the only permissive SIS base exists and you would be adopting it, not joining it."
  The copyleft options remain what they were — Gibbon GPL-3.0; RosarioSIS GPL-2.0 (default branch
  **`mobile`**); and `OS4ED/openSIS-Classic` has **no licence file in its repository at all**, its
  GPL claim appearing only in the README, so that one is still not a clean grant.
- 🔵 **A `NOASSERTION` from the GitHub licence API is not evidence of anything** — see the T14 table
  at the top of this file. `p877` found one permissive-with-an-added-line, one
  permissive-with-a-manifest and one genuinely proprietary repository behind the same token. **Any
  row this KB ever wrote off as "no licence" on API evidence alone must be re-read at the bytes
  before it is treated as unusable.**
- `apereo/opencast-admin-interface` **does not exist** (`git ls-remote` returned nothing). The
  real address is `opencast/opencast`, and `p872` adds its default branch: **`develop`**, not
  `main`, licence **ECL-2.0**. A clone pinned to `main` fails outright.
- **Non-`main` default branches are the single most productive source of wrong data in this KB,
  and `p873` makes the case worse in kind.** `p872` found four of eleven audited addresses not
  defaulting to `main` — `opencast`, `oppia` and `kolibri` → `develop`; `edx-ora2`, `ltijs`,
  `OpenOlat` and `sakai` → `master`. `p873` adds **`francoisjacquet/rosariosis`, whose default
  branch is `mobile`** — a *feature* name that no heuristic would guess and nothing in the address
  hints at. State it as a hard rule: **never construct a `raw.githubusercontent.com` path from an
  assumed branch; resolve it with `git ls-remote --symref <url> HEAD` first.** A guessed `main`
  404s, the 404 reads as *"no licence file"*, and *"no licence file"* gets published as
  **"no grant — cannot build on it"**. That one shortcut would have libelled RosarioSIS's licence
  this pass and `opencast`'s last pass; phantom licences and phantom absences, the two most
  expensive wrong-data classes here, both come from it.
- **A second class of branch error: the code may not be on the default branch at all.** `p873`'s
  headline find, **`LabSirius/TutorIA`** (MIT, Colombia — see `agents/top.md`), has a default
  branch holding **documentation only**; its backend lives on `feature/refactor-to-v2-requirements`,
  and the address its own README tells you to clone (`Sof1SP/tutorIA`) has **no code in any
  branch**. Existence, licence and default branch can all verify cleanly on a repository that
  would still ship nothing. For any repo proposed as a *build base*, confirm a load-bearing source
  file resolves — not just `LICENSE`.
- **A substring grep cannot characterise a licence.** `p872` tried to automate the
  "Apache-2.0 + additional terms" check and got a **100% false-positive rate** on Apache-2.0,
  because §5 of the licence contains the phrase *"without any additional terms or conditions"*.
  Seven clean repos were flagged; the flag was **discarded rather than published**.
  `opendatalab/MinerU` remains the single genuine case in this KB, because its `LICENSE.md` adds
  substantive terms in prose. Automate existence and branch resolution; read the bytes for
  licence meaning.
- **No permissively licensed proctoring component exists at the foundations layer either.**
  The two real candidates found by `p872` are both AGPL-3.0 — see `verticals/solutions.md`.
