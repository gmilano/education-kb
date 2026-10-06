---
industry: education
region: Global
updated: 2026-10-06
---

# Foundational Repos — Education

Infrastructure Globant can build an education solution *on top of*. These are not
education products; they are the permissively licensed layers underneath one.
Licenses read from each repo's own `LICENSE` payload on 2026-10-06.

## Core stack

15 rows, all verified this pass.

| Repo | License (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | MIT (`LICENSE`) | model serving | Runs open-weight models on-prem or on a classroom server. This is the answer to EMEA data-residency and to LATAM connectivity/cost constraints — student data never leaves the institution. |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | MIT (`LICENSE`) | agent framework | Typed, validated agent outputs. When an assessment decision must be defensible, a schema-checked output beats free text. |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | MIT (`LICENSE`) | orchestration | Graph-structured, checkpointed agent state. The checkpoints double as the audit trail a high-risk education deployment needs. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | MIT (`LICENSE`, body text — no title line) | orchestration | Role-based multi-agent teams; maps cleanly onto tutor / assessor / reviewer separations. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | MIT (`LICENSE`) | coding agents | For the build itself and for CS-education use cases where students need a sandboxed coding agent. |
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | agent framework | Python + .NET. The right default for clients already on a Microsoft stack, and the successor path off AutoGen. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | agent framework | Smallest auditable surface of the frameworks here. |
| [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | Apache-2.0 (`LICENSE.md`) | document ingestion | Turns textbooks, PDFs and scanned curricula into structured text. This is the front door of every content-generation pipeline in `compose/patterns.md`. |
| [jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub) | BSD-3-Clause (`LICENSE`, modified-BSD body) | lab environment | Multi-user notebook serving for a cohort. The standard way to hand 200 students an identical environment. |
| [jupyter/notebook](https://github.com/jupyter/notebook) | BSD-3-Clause (`LICENSE`) | lab environment | The notebook itself. |
| [LearningEquality/ricecooker](https://github.com/LearningEquality/ricecooker) | MIT (`LICENSE`) | content pipeline | Python framework for packaging arbitrary content into Kolibri channels. The ETL half of the offline-first pattern. |
| [LearningEquality/studio](https://github.com/LearningEquality/studio) | MIT (`LICENSE`) | content authoring | Curriculum authoring and channel curation that feeds Kolibri. |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | Apache-2.0 (`LICENSE`) | LMS integration | LTI tool-provider implementation. The permissive doorway into a copyleft LMS — see the license-boundary note in `agents/top.md`. |
| [1EdTech/openbadges-validator-core](https://github.com/1EdTech/openbadges-validator-core) | Apache-2.0 (`LICENSE`) | credentialing | Open Badges validation. Relevant to the skills-economy trend: competency claims a third party can verify. |
| [opencast/opencast](https://github.com/opencast/opencast) | ECL-2.0 (`LICENSE`) | lecture capture | Video capture, processing and delivery for universities. ECL-2.0 is an Apache-2.0 derivative, so it is **permissive** — the recorded-lecture corpus it produces is the natural input to the P2 ingestion pipeline. |

## Teaching-content repos (for enablement, not for production)

| Repo | License (read from payload) | Note |
|---|---|---|
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 18 lessons, 76.5k★ |
| [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | MIT (`LICENSE`) | the GenAI prerequisite track |
| [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | Apache-2.0 (`LICENSE.txt`) | builds a GPT-class model in PyTorch; >100k★ class resource |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | Apache-2.0 (`LICENSE`) | roadmap + notebooks |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | agent track |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | APAC-origin, large cohort programme |

## Repos checked and deliberately not recommended

Recording these saves the next pass the probe.

| Repo | Finding |
|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Maintenance mode, no new features; `LICENSE` at HEAD is CC-BY-4.0 (dual with MIT). Use `microsoft/agent-framework` instead. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0**, not MIT. Widely mis-reported as MIT by LMS comparison blogs. The license lives at `license.txt` (lowercase) — `LICENSE` returns 404, which is how the misreport propagates. |
| [cloudtoolbox/deeptutor](https://github.com/cloudtoolbox/deeptutor) | 7★ fork of `HKUDS/DeepTutor`. Correct Apache-2.0 license, no history. Pin the HKUDS origin. |

## Method note

License probes need both axes — filename *and* extension. `LICENSE`,
`LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING` and `COPYING.txt` are all
in live use across this shelf, and probing only `LICENSE` produces false
negatives (`frappe/lms` and `moodle/moodle` both hide from a single-path probe).
A badge or a comparison blog is not a license reading.

Repo *location* needs the same care: `apereo/opencast` is a **404**, and the live
repository is `opencast/opencast` (ECL-2.0). An org-renamed project will fail a
reachability probe while the project itself is perfectly healthy — re-probe the
name before recording a gap.
