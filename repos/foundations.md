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

15 rows, all verified on 2026-10-06. Four further infrastructure rows were added in
the third pass of the same day — see the section below.

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

## Added in the third pass of 2026-10-06

Four infrastructure rows, each probed this pass. Three of them exist because
`Selleo/mentingo` (MIT) demonstrated a leaner sovereign stack than the one this KB
had been assembling by hand — see `verticals/solutions.md`.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | **PostgreSQL License** (`LICENSE`) — permissive, BSD-like | retrieval | Vector similarity search **inside PostgreSQL**. Removes a whole component from a sovereign deployment: no separate vector database to host, secure, back up and keep in-region. Where this KB previously reached for a dedicated vector store, reach for this first. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | **MIT, with a carve-out** (`LICENSE`) — see the warning below | LLM observability | Traces every model call with cost, latency and the actual output. In a high-risk education deployment this is the **audit trail produced as a by-product of normal operation**, rather than as a separate compliance project. The single highest-leverage addition to every pattern in this KB. |
| [livekit/livekit](https://github.com/livekit/livekit) | **Apache-2.0** (`LICENSE`) | real-time voice | WebRTC infrastructure for spoken practice, oral assessment and role-play. The permissive path to voice tutoring, which is otherwise a proprietary-API-shaped problem. |
| [KualiCo/rice](https://github.com/KualiCo/rice) | **ECL-2.0** (`LICENSE.txt`) — permissive | higher-ed middleware | Application framework, workflow and eDocLite document routing built for and by the higher-education community. Java, 4★, 12 forks. **In maintenance mode** by its own README — vendor and fork it, do not present it as a living upstream. Full estate breakdown in `verticals/solutions.md`. |

### Two licence warnings on the rows above

**Langfuse is MIT *except* its `ee/` directories, and the copyright holder is now
ClickHouse, Inc.** The `LICENSE` payload is explicit: content under `ee/`,
`web/src/ee/` and `worker/src/ee/` is governed by a separate enterprise licence at
`ee/LICENSE`; everything outside those paths is MIT Expat. The copyright line reads
**"Copyright (c) 2023-2026 ClickHouse, Inc."** Two consequences: a repo-level "MIT"
badge is **not** sufficient diligence on an open-core project — the carve-out is by
*directory*, so the probe has to read the payload and the paths, not the badge. And
the copyright holder on a dependency can change under you between passes, which
nothing in a licence probe will flag. Build against the MIT paths, exclude `ee/`
from any vendored copy, and record the holder as well as the licence.

**pgvector is under the PostgreSQL License, not MIT, Apache-2.0 or BSD by name.**
It is permissive and BSD-like, and a naive allowlist that string-matches
`MIT|Apache|BSD` will reject it. Together with ECL-2.0 (Sakai, Opencast, Kuali
Rice) that is **four** genuinely permissive licences this KB relies on that a
three-name allowlist throws away. The allowlist for an education engagement is:
**MIT, Apache-2.0, BSD (2/3-clause), ECL-2.0, PostgreSQL License, ISC** — and read
the payload for carve-outs before trusting any of them.

## Added in the fourth pass of 2026-10-06

Channels new to this KB: **paper-to-repository tracing** (arXiv, ACL Anthology)
and a **GitHub-organisation sweep**. Licences read from each repository's own
`LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in a build |
|---|---|---|---|
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** (`LICENSE`, © 2026 THU-MAIC) | **40.0k** | **The content-generation spine.** Tsinghua's Open Multi-Agent Interactive Classroom: topic or document → slides, quizzes, HTML simulations and PBL scenes, delivered by AI teacher + AI classmate agents with TTS and a shared whiteboard; exports PPTX and interactive HTML. v1.2.0-rc.1 (2026-10-04) is **server-first with PostgreSQL persistence**, so generation survives a closed tab or restart. TypeScript / Next.js / React. |
| [AI-for-Education/fabdata-llm](https://github.com/AI-for-Education/fabdata-llm) | **MIT** (`LICENSE`) | 9 | Multi-provider LLM interface and chatbot management. A small, readable alternative to a heavyweight gateway when the deployment has to stay auditable. Python. |
| [AI-for-Education/fabdata-parsedoc](https://github.com/AI-for-Education/fabdata-parsedoc) | **MIT** (`LICENSE`) | 2 | Document text extraction, parsing and summarisation — the ingest stage ahead of any content pipeline. Python. Pair with or compare against `opendatalab/MinerU` already on this shelf. |
| [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** (`LICENSE`) | 12 | **Model-selection instrument.** Scores LLMs on *pedagogical knowledge* using teacher-qualification exam questions, rather than on task accuracy. The only thing on this shelf that answers "which model should teach this?" with evidence. Python. |
| [AI-for-Education/voice-ai-evaluation-framework](https://github.com/AI-for-Education/voice-ai-evaluation-framework) | **MIT** (`LICENSE`) | 1 | Evaluation harness for **voice** interfaces — the modality that binds where literacy, device cost or bandwidth do. Python. |

**Star counts, stated plainly.** OpenMAIC is a flagship at 40.0k★. The four
`AI-for-Education` libraries are **1–12★ research-grade code** and should be read
and vendored deliberately, not pinned as if they were maintained infrastructure.
They are listed because this KB had **no permissive entry at all** for pedagogical
model selection or voice evaluation, and because they are the **first
Africa-placed repositories it has recorded** — the organisation's work is built
for **Sierra Leone's MBSSE** and for **Uganda** (Luganda).

**One sibling in that organisation is not usable:**
[`Luganda-linguistic-benchmarks`](https://github.com/AI-for-Education/Luganda-linguistic-benchmarks)
has **no `LICENSE` payload** (`README.md` 200, `LICENSE` 404). Five MIT siblings do
not license the sixth.

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
| [kuali/kfs](https://github.com/kuali/kfs) | **AGPL-3.0** (`LICENSE`). Kuali Financial System. Same consortium as the permissive Kuali Rice — the licence is per repository, not per foundation. |
| [kuali/kc](https://github.com/kuali/kc) | **AGPL-3.0** (`license.txt`, lowercase). Kuali Coeus research administration. Third live instance of the lowercase-`license.txt` probe trap, after `frappe/lms` and `frappe/erpnext`. |
| [kuali/rice](https://github.com/kuali/rice) | Correct licence (ECL-2.0) but **DEPRECATED** by its own README, which points to `KualiCo/rice`. Pin the KualiCo location. |
| `kuali/student`, `KualiCo/student`, `kuali/coeus` | **Not reachable** — `README.md` 404s on all three. Kuali Student (the SIS) is not at the path its name implies; recorded so the next pass does not re-probe these. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **AGPL-3.0**, 563★. Competency skill tree, K-12 to career. Reference for competency-graph design only. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 156★. Self-hosted AI language learning. |
| [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | **GPL**, 88★. Learner-owned course generation. |
| [yh2072/edgameclaw](https://github.com/yh2072/edgameclaw) | **AGPL-3.0**, 71★. Game-based course conversion. |
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | **Unlicensed**, 61★. Its README's licence section reads only *"This project is open source and available for educational purposes"* — prose that imitates a grant. No licence, no holder, no redistribution right. |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | **Unlicensed**, 24★. No `LICENSE` and no licence mention anywhere in the README. |

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

**A fourth axis, added 2026-10-06 (third pass): the OWNER.** A 404 or an
unlicensed verdict on `owner/name` is evidence about *that owner's repository
only* — never about the project. The second pass of 2026-10-06 withdrew this KB's
OpenTutor entry after probing `tutornew/OpenTutor` (8★, unlicensed) and the real
project was `zijinz456/OpenTutor` (**MIT, 130★, FSRS 4.5, 12 blocks, LOOM knowledge
graph**) all along. Every other probe lesson in this file guards against a false
*positive*; that one was a **false negative that deleted a true finding**, which is
the more expensive direction because the result is a confident denial rather than a
wasted probe. So: **before withdrawing an entry, enumerate the owners publishing
under that project name.** A withdrawal needs a stronger probe than an addition.

**A fifth axis: the DIRECTORY.** An open-core project can be permissive at the root
and proprietary in a subtree. `langfuse/langfuse` is MIT except `ee/`,
`web/src/ee/` and `worker/src/ee/`, which carry a separate enterprise licence — and
its copyright holder is now ClickHouse, Inc. A repo-level licence badge cannot
express that. Read the payload, note the carve-out paths, and record the copyright
holder alongside the licence so a change of holder between passes is visible.

Repo *location* needs the same care: `apereo/opencast` is a **404**, and the live
repository is `opencast/opencast` (ECL-2.0). An org-renamed project will fail a
reachability probe while the project itself is perfectly healthy — re-probe the
name before recording a gap. The converse also happens: `planejaia/OpenMAIC-Brasil`
is a confident search result for a repository that genuinely does not exist —
**re-probed on 2026-10-06 it still 404s on all four** candidate branches (`main`,
`master`, `develop`, `v1.0.0`).

**Two rules added in the fourth pass of 2026-10-06, because that last example was
read wrongly for three passes.**

1. **A 404 on a suffixed name obliges you to query the base name before you record
   a gap.** `OpenMAIC-Brasil` is absent; **`OpenMAIC` is not.** The upstream is
   [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — **MIT, 40.0k★,
   Tsinghua University** — now the largest permissive asset in this KB and listed
   on the core shelf above. This KB carried the absence as evidence through three
   passes while a forty-thousand-star implementation of the same idea sat one query
   away.
2. **A repository name is not a provenance claim.** `-Brasil`, `-India`, `-LATAM`
   are strings an author typed. Attribute region from the **owner account, the
   commit history or the README** — never from the slug. The no-LATAM-origin gap
   was partly argued from this filename; it has since been re-established on
   channels that do not depend on one, including a Spanish/Portuguese-language
   search (see `agents/top.md`).

**And sweep the organisation behind any interesting repository.** Topic pages rank
by stars, so they structurally hide small orgs: the `AI-for-Education` sweep in the
same pass returned six repositories, five MIT, that no topic page had ever shown
this KB — and they are the only Africa-placed code it holds.
