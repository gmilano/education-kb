---
industry: education
region: Global
updated: 2026-11-17
---

# Foundational repos — education

**Pass `p871`, 2026-11-17.** Same two-channel verification as `agents/top.md`: existence via
`git ls-remote`, licence via the licence bytes on the **resolved** default branch. No star
counts — that channel returned `403` this session.

These are the load-bearing pieces an education build sits on: the standards plumbing that
makes a tool interoperable with institutional systems, and the AI substrate that makes it
work. The standards layer matters more here than in most verticals — an education tool that
cannot speak LTI, xAPI/Caliper, QTI or Ed-Fi cannot be bought by a school district.

## Education standards & interoperability

This is the layer that gets a Globant build past institutional procurement.

| Repo | Licence | Branch | Why it is foundational |
|---|---|---|---|
| https://github.com/Cvmcosta/ltijs | Apache-2.0 | `master` | **LTI 1.3 / LTI Advantage tool provider in Node.** The single most reusable piece of plumbing in education software: implement it once and your agent launches as a tool inside Moodle, Canvas, Open edX, Blackboard and D2L with grade passback. Permissive — safe to embed. |
| https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS | Apache-2.0 | `main` | **Ed-Fi Operational Data Store + API.** The de-facto K-12 data standard in US school districts. Apache-2.0, so a district-facing analytics or early-warning agent can build directly on it. |
| https://github.com/1EdTech/openbadges-validator-core | Apache-2.0 | `develop` | Open Badges validation from the standards body itself (1EdTech, formerly IMS Global). The verification half of any credentialing or micro-credential build. |
| https://github.com/Citolab/qti-components | GPL-3.0 | `main` | **QTI 3 web components** — standards-compliant assessment item rendering. Copyleft: fine for a self-hosted institutional deployment, a problem for a proprietary distributed product. |
| https://github.com/edx/edx-ora2 | AGPL-3.0 | `master` | **Open-response assessment** — rubrics, peer assessment, self assessment, staff grading. Given that no mature OSS grading *agent* exists (see `agents/top.md` gaps), this is the realistic production substrate for AI-assisted grading. AGPL: network-use triggers source obligations. |
| https://github.com/LearningLocker/learninglocker | GPL-3.0 | `master` | **xAPI Learning Record Store.** Where learner interaction telemetry lands so that a tutoring agent's effect can actually be measured rather than asserted. |
| https://github.com/openedx/openedx-aspects | Apache-2.0 | `main` | Open edX's learning-analytics stack (Aspects). Apache-2.0 and reusable even outside an Open edX deployment. |
| https://github.com/jupyter/nbgrader | BSD | `main` | Assignment release, collection and autograding for Jupyter notebooks. The standard autograder in university CS and data-science courses. |
| https://github.com/jupyterhub/jupyterhub | BSD | `main` | Multi-user notebook hosting — the substrate for every hands-on technical course delivered in a browser. |
| https://github.com/open-spaced-repetition/fsrs4anki | MIT | `main` | **FSRS** — the modern free-spaced-repetition scheduler. MIT-licensed, empirically validated memory model. If your product claims retention, this is the algorithm to use instead of inventing a review schedule. |

## Document & media ingestion — the real bottleneck in education AI

Education content arrives as PDFs, scanned worksheets, lecture video and textbooks. Ingestion
quality, not model quality, is what usually determines whether a tutoring build works.

| Repo | Licence | Branch | Role |
|---|---|---|---|
| https://github.com/docling-project/docling | MIT | `main` | Document parsing to structured output (IBM-originated, now a Linux Foundation AI project). MIT, strong on tables and layout — the default first choice for curriculum and textbook ingestion. |
| https://github.com/datalab-to/marker | Apache-2.0 | `master` | PDF → markdown with high fidelity on equations and tables. Strong on STEM textbooks where Docling's maths handling is not enough. |
| https://github.com/opendatalab/MinerU | Apache-2.0 **+ extra terms** | `master` | High-quality PDF extraction including formulas. **Flag:** `LICENSE.md` adds terms on top of Apache-2.0 — read them before commercial use. |
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

**31 verified foundational repos.**

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
  real address is `opencast/opencast`. Recorded so the dead address is not re-imported.
