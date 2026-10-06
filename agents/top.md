---
industry: education
region: Global
updated: 2026-10-06
---

# AI Agents — Education

Open source AI agents and agent-adjacent tooling for education. Focus on MIT /
Apache-2.0 / BSD, the licenses Globant can build on and redistribute to clients.

**Verification method (2026-10-06):** every license below was read from the
repository's own `LICENSE` payload via `raw.githubusercontent.com`, not from a
listing sidebar, a badge, or a blog post. Star counts and descriptions were read
from the repository page the same day. `api.github.com` is not reachable from
this environment (403, session-scoped), so star counts come from the rendered
page; where a count was not read this pass, the cell says so rather than
carrying a stale or inferred number.

## Agents and tools

12 rows, all verified this pass.

| Agent | Repo | License (read from payload) | ★ (2026-10-06) | What it does |
|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 (`LICENSE`) | 40.8k | Agent-native lifelong tutoring. Two-layer plugin model (single-shot Tools + multi-stage Capabilities), exposed via CLI, WebSocket API and Python SDK. Per-learner TutorBot workspaces with persistent memory. Latest release v1.6.13 (2026-10-04). Python. |
| AI Agents for Beginners | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT (`LICENSE`) | 76.5k | 18-lesson course on building AI agents; code samples now target Microsoft Agent Framework. The default enablement asset for client-staff upskilling. |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 (`LICENSE`) | 29.7k | Barebones library for agents that think in code. Small surface area makes it the cheapest framework to audit for a high-risk education deployment. |
| Microsoft Agent Framework (MAF) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | MIT (`LICENSE`) | 14.0k | Building, orchestrating and deploying agents and multi-agent workflows, Python and .NET. Ships migration guides *from* AutoGen and Semantic Kernel. |
| Oppia | [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 (`LICENSE`) | 6.8k | Online learning platform for authoring interactive lessons ("explorations") with built-in misconception handling. One of only three permissively licensed full platforms in this KB. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT (`LICENSE`) | 278 | Canvas LMS MCP server: up to 102 tools and 8 agent skills for students, educators and learning designers. Includes a 20-check WCAG accessibility scanner and bulk-grading tools. Works with 40+ MCP clients. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT (`LICENSE`) | 264 | Intelligent tutoring system with Bayesian Knowledge Tracing, from CAHLR at UC Berkeley. Published at CHI '23 with a follow-up in PLOS ONE. ReactJS + Firebase. The auditable mastery model in this list. |
| Educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT (`LICENSE`) | 388 | Python package for generating educational content with generative AI — MCQs, open-ended items, lesson plans, flashcards. |
| Kolibri | [LearningEquality/kolibri](https://github.com/LearningEquality/kolibri) | MIT (`LICENSE`) | 1.1k | Offline-first learning platform for teaching and learning without an internet connection. The only fully permissive end-to-end platform here; the basis of the equity-deployment pattern. |
| Moodle MCP Server | [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | MIT (`LICENSE`) | not read this pass | MCP server exposing Moodle data to agents from *outside* the Moodle tree — which is why it is MIT while in-tree Moodle plugins are GPL-3.0 (see the license-boundary note below). |
| Hugging Face Agents Course | [huggingface/agents-course](https://github.com/huggingface/agents-course) | Apache-2.0 (`LICENSE`) | not read this pass | Open course on building agents with Hugging Face tooling. Pairs with the Microsoft course for a two-track enablement curriculum. |
| learn-agentic-ai | [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT (`LICENSE`) | not read this pass | Agentic-AI curriculum used at large scale by the Panaversity / GIAIC programme in Pakistan — a rare APAC-origin education asset in this space. |

## The license boundary that decides your architecture

This is the single most reusable finding in this KB, and it is measured, not
inferred:

| Piece | Where it runs | License read from payload |
|---|---|---|
| [Limekiller/moodle-block_openai_chat](https://github.com/Limekiller/moodle-block_openai_chat) | in-tree Moodle plugin | GPL-3.0 |
| [yedidiaklein/moodle-local_aiquestions](https://github.com/yedidiaklein/moodle-local_aiquestions) | in-tree Moodle plugin | GPL-3.0 |
| [cgrevisse/moodle-qbank_genai](https://github.com/cgrevisse/moodle-qbank_genai) | in-tree Moodle plugin | GPL-3.0 |
| [peancor/moodle-mcp-server](https://github.com/peancor/moodle-mcp-server) | external process, talks to Moodle over its web API | **MIT** |
| [IMSGlobal/LTI-Tool-Provider-Library-PHP](https://github.com/IMSGlobal/LTI-Tool-Provider-Library-PHP) | external tool provider | **Apache-2.0** |

**Consequence:** AI built *inside* a copyleft LMS inherits that LMS's license.
The same capability built as an external service reached over LTI 1.3 or MCP
stays permissive and stays reusable across client engagements. Prefer the
side-car. This drives pattern P1 in `compose/patterns.md`.

## Corrections to earlier passes

- **AutoGen is no longer a starting point.** [microsoft/autogen](https://github.com/microsoft/autogen)
  (61.3k★) is explicitly in **maintenance mode**: *"AutoGen is now in maintenance
  mode. It will not receive new features or enhancements and is community managed
  going forward. New users should start with Microsoft Agent Framework."* Its
  `LICENSE` at HEAD is now **CC-BY-4.0** (the repo is dual CC-BY-4.0 / MIT), not
  the plain MIT recorded in earlier cycles. Earlier education cycles listed
  AutoGen as a top agent at ~60k★ — that recommendation is withdrawn in favour of
  MAF.
- **DeepTutor's canonical repo is `HKUDS/DeepTutor`.** Searching for it surfaces
  forks and mirrors first: `cloudtoolbox/deeptutor` (7★), `lucadeg/DeepTutor` and
  `q-qp-p/HKUDS-DeepTutor` all carry the same description and the same Apache-2.0
  license but none of the history. Pin the HKUDS origin.

## Declared gaps — searched this pass, nothing found

An informed gap is information; silence looks exactly like coverage.

- **No permissive open source auto-grader exists.** A GitHub repository search for
  automated grading / assessment agents returned no credible permissive project,
  matching the zero-result finding of the previous pass. Every assessment recipe
  in this KB therefore keeps a human in the scoring loop — which is also what the
  EU AI Act high-risk rules and the Oklahoma/Maryland human-oversight statutes
  require. Do not promise an autonomous grader to a client.
- **No LATAM-origin open source education agent found.** Chamilo has deep
  Spanish-language and LATAM deployment but is EU-origin and GPL-3.0. The regional
  opportunity is deployment and localisation, not upstream code.
- **APAC sovereign models are base models, not education agents.** Sarvam AI,
  SEA-LION, Sahabat AI, ILMU, HyperCLOVA X Think and NTT Sarashina are
  foundation models; none ships an education agent layer. `learn-agentic-ai` is
  the one APAC-origin education asset found.
- **No open source EU AI Act compliance toolkit specific to education** surfaced
  this pass. The compliance work in pattern P4 is assembled from general-purpose
  parts (typed outputs, checkpointed audit trails, explainable mastery models).
