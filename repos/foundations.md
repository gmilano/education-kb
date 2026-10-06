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
| [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | MIT (`LICENSE@main`) | production agentic-RAG — the missing middle between an agent demo and a deployed retrieval system |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | MIT (`LICENSE@main`) | AI-engineering track, trending through 2026 |

## Repos checked and deliberately not recommended

Recording these saves the next pass the probe.

| Repo | Finding |
|---|---|
| [microsoft/autogen](https://github.com/microsoft/autogen) | Maintenance mode, no new features; `LICENSE` at HEAD is CC-BY-4.0 (dual with MIT). Use `microsoft/agent-framework` instead. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0**, not MIT. Widely mis-reported as MIT by LMS comparison blogs. The license lives at `license.txt` (lowercase) — `LICENSE` returns 404, which is how the misreport propagates. |
| [cloudtoolbox/deeptutor](https://github.com/cloudtoolbox/deeptutor) | 7★ fork of `HKUDS/DeepTutor`. Correct Apache-2.0 license, no history. Pin the HKUDS origin. |
| [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | **Unlicensed.** 103★, 54 tools, v2.3.0 — and no `LICENSE` on any branch, no license statement in the README. Default copyright: all rights reserved. The most dangerous repo in this KB precisely because it looks mature. |
| [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) | **Unlicensed.** 38★, Python, no `LICENSE` on any branch, none in README. |
| [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) | **Unlicensed.** 8★, 5 commits. Recorded in an earlier cycle of this KB as "MIT, ~900★" — wrong on both counts. Withdrawn; see `agents/top.md`. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 **plus** a paid premium-plugin tier. Legally usable, commercially the worst shape on the shelf for reusable studio IP. |
| [planejaia/OpenMAIC-Brasil](https://github.com/planejaia/OpenMAIC-Brasil) | **404 — does not exist.** Surfaced by search as a Brazil-origin multi-agent classroom, v1.0.0 "released 2026-08-27". Every file 404s on four branches and the repo page returns HTTP 404. Recorded so the next pass does not chase it again. |
| [frappe/erpnext](https://github.com/frappe/erpnext) | GPL-3.0 at `license.txt` (lowercase) — usable, but listed here because it shares `frappe/lms`'s probe trap: `LICENSE` returns 404. |

## Method note

License probes need both axes — filename *and* extension. `LICENSE`,
`LICENSE.md`, `LICENSE.txt`, `license.txt`, `COPYING` and `COPYING.txt` are all
in live use across this shelf, and probing only `LICENSE` produces false
negatives (`frappe/lms` and `moodle/moodle` both hide from a single-path probe).
A badge or a comparison blog is not a license reading.

A licence probe also needs a third axis: **path depth**. `OS4ED/openSIS-Classic`
404s on every root-level candidate — `LICENSE`, `LICENSE.md`, `COPYING`,
`license`, `License.txt`, `GPL-LICENSE.txt` — while its real licence sits at
**`docs/License.txt`** (GPL-2.0), pointed to only by a Markdown link in the
README. So the probe order that actually works:

1. root filename × extension variants;
2. if all 404, **read the README for a licence link** before recording a gap;
3. follow that link and read the payload.

Skipping step 2 produces a false "unlicensed" verdict on a correctly licensed
project — the mirror image of the false-MIT error `frappe/lms` causes. Both
failure modes now have a live example. Only after step 3 fails is "unlicensed"
a finding: that is how `DMontgomery40/mcp-canvas-lms`, `loyaniu/moodle-mcp` and
`tutornew/OpenTutor` were confirmed above, each checked against eight filename
variants on three branches *and* its README.

Repo *location* needs the same care: `apereo/opencast` is a **404**, and the live
repository is `opencast/opencast` (ECL-2.0). An org-renamed project will fail a
reachability probe while the project itself is perfectly healthy — re-probe the
name before recording a gap. The converse also happens: `planejaia/OpenMAIC-Brasil`
is a confident search result for a repository that genuinely does not exist.
