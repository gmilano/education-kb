---
industry: education
region: Global
updated: 2026-11-17
---

# Foundational repos — education

**Pass `p875`, 2026-11-17** (fifth pass of the day). **`p875` closes the star gap and uses it to
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
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | `master` | **xAPI Learning Record Store.** Where learner interaction telemetry lands so that a tutoring agent's effect can actually be measured rather than asserted. 🔴 **`p875`: 587 stars, LAST PUSH 2024-05-30 — 18 months dormant. This is the measurement layer the whole "prove the tutor worked" pitch depends on, and it is unmaintained. No maintained permissive LRS was found to replace it; budget a maintained fork or fall back to the LMS gradebook.** |
| https://github.com/openedx/openedx-aspects | Apache-2.0 | `main` | Open edX's learning-analytics stack (Aspects). Apache-2.0 and reusable even outside an Open edX deployment. |
| https://github.com/jupyter/nbgrader | BSD | `main` | Assignment release, collection and autograding for Jupyter notebooks. The standard autograder in university CS and data-science courses. |
| https://github.com/jupyterhub/jupyterhub | BSD | `main` | Multi-user notebook hosting — the substrate for every hands-on technical course delivered in a browser. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | `main` | **FSRS** — the modern free-spaced-repetition scheduler. MIT-licensed, empirically validated memory model. If your product claims retention, this is the algorithm to use instead of inventing a review schedule. |

## Curriculum structure — new in `p875`

The layer that tells a tutoring agent *what comes before what*. Without it, "personalised learning
path" is a prompt, not a data structure.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/withmarbleapp/os-taxonomy | 🔴 **ODbL-1.0** | `main` | **A 1,590-topic children's curriculum graph with 3,221 prerequisite edges** — the prerequisite relation is the part that is hard to build and expensive to buy, and this is the only open one this KB has found. **7,720 stars, last push 2026-11-16** — real traction, actively maintained. 🔴 **Read the licence before you plan around it: Open Data Commons ODbL is a share-alike *database* licence, not a software licence.** Using it to drive a service is fine; **publishing a derived or extended database triggers share-alike obligations on that database.** It is therefore *not* in the MIT/Apache class this KB otherwise prefers and must never be filed as permissive. The safe pattern is to consume the graph as reference data behind a service and keep client-specific curriculum extensions in a separate store you do not redistribute. |

🟡 **Gap this exposes rather than closes:** there is **no permissive** open curriculum graph. If a
client needs to own and redistribute a prerequisite taxonomy, it is bespoke work — and `os-taxonomy`
is still the best thing to read first when scoping it.

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
| https://github.com/argilla-io/argilla | Apache-2.0 | `develop` | Human feedback and dataset curation, oriented to SME review — fits teacher-in-the-loop validation. |
| https://github.com/wwrwbs/AI_AWE | Apache-2.0 | `main` | **ArguLens** — automated essay scoring with feedback. Enters the foundations layer because its **scorer is a grade-independent LightGBM model over 31 explicit linguistic/discourse features**, not an LLM: a reproducible, inspectable score is the only kind that survives an appeal or a high-risk conformance review. **v0.1.0, research-grade; corpus is US middle-school English (Persuade 2.0)** — re-fitting on local graded essays is required work, not polish. See `agents/top.md`. |

**33 verified foundational repos** (31 from `p871`, plus `openedx/edx-ora2` recorded as the
canonical address and `wwrwbs/AI_AWE` added by `p872`).

## Declared gaps

- **The permissive/copyleft split is the central licence fact of this vertical.** The AI
  substrate above is almost entirely MIT/Apache-2.0, and the standards plumbing is mixed, but
  the *platform* layer (see `verticals/solutions.md`) is overwhelmingly GPL/AGPL. A Globant
  engagement should expect to build permissive AI services that **integrate with** copyleft
  platforms over LTI/xAPI rather than forking them.
- **No open-source student-information system with a permissive licence was found.** Both
  verified SIS options (Gibbon GPL-3.0, openSIS-Classic GPL) are copyleft, and
  `OS4ED/openSIS-Classic` has **no licence file in its repository at all** — its GPL claim
  appears only in the README. Flagged, not treated as a clean grant.
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
