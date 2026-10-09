---
industry: education
region: Global
updated: 2026-10-09
---

# Education — AI agents shelf

**Pass 90, 2026-10-09.** Every row below was resolved this pass with a two-step ladder:
existence and default branch from `git ls-remote --symref` (authoritative), then the **licence read from the
payload** at `raw.githubusercontent.com/<slug>/<SHA>/<file>`, pinned to the resolved commit SHA — never from
a GitHub badge and never from a blog. Two-sided control passed: an invented slug resolved `ABSENT`, and
`moodle/moodle` returned `COPYING.txt` at **35 147 B**, byte-identical to the six prior passes that measured it.
Instrument: `compose/code/grant-ladder-v2/ladder.sh`.

**Method note that corrects earlier passes.** `curl -sI https://github.com/<slug>` is useless under this
session's egress proxy: it returns **403 for a real slug and an invented slug alike**, and with `-sI` it prints
only the proxy's own `200 Connection Established` line, which earlier passes mistook for a live page. `api.github.com`
is likewise 403 for both. Neither can discriminate; neither is used. Star counts come from GitHub topic and repo
pages read this pass and are labelled as such. **A `—` in the ★ column means not read this pass. It never means zero.**

## The shelf

### Platform-grade AI (production, named deployments)

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `main` · `6cf793b` | 41.0k | **APAC** (HKU Data Science lab) | The reference agent-native tutoring workspace. Real agent loop with `web_search`/`rag`/`exec`/`consult_subagent` tools, MCP servers, **multi-engine RAG** (LlamaIndex, PageIndex, GraphRAG, LightRAG) and a **three-layer file-backed memory** (L1 traces → L2 summaries → L3 synthesis). An `ask_user` tool lets a turn pause for clarification — the pedagogically correct primitive. |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | **MIT** · 1 091 B · `develop` · `760e2e1` | 816 | **EMEA** (TU München, AET group) | **The most important row on this shelf and the one prior passes missed.** A production university platform, MIT, with three named LLM subsystems: **Iris** (virtual tutor giving hints and leading questions), **Athena** (feedback suggestion for text, modelling and programming exercises) and **Hyperion** (AI-assisted exercise authoring on Spring AI). All optional and config-gated. MIT + production + AI-native is a combination this shelf previously asserted did not exist. |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD** · 1 531 B · `main` · `196c547` | ~107 (snippet) | 🔵 unplaced | Permissive, peer-reviewed (arXiv 2602.07176), Ollama and OpenAI-compatible, **local RAG over course materials**. The BSD grant makes it the cleanest base for a closed client deliverable. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Selleo, Poland) | AI-native LMS; vendor documents an AI Mentor with Teacher / Mentor / Roleplay modes and generation of course structure, lessons and materials. Open-core boundary still unverified. |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | **MIT** · 1 092 B · `main` · `38adb1e` | — | **APAC** (India) | Content and assessment generation from arbitrary sources; the long-standing generator row on this shelf. |

### Composable agents and protocol surface

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** · 1 074 B · `main` · `ed6774d` | 510 | 🔵 unplaced | Exposes Anki to any MCP client. **Spaced repetition becomes a tool call** — the cheapest way to give an agent durable retention mechanics instead of reimplementing them. |
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** · 1 073 B · `main` · `3708287` | 44 | 🔵 unplaced | Go MCP server that turns any LLM into an intelligent tutoring system. Model-agnostic by construction, which is what a studio wants when the client dictates the model. |
| [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | **Apache-2.0** · 11 386 B · `main` · `1b7fbe0` | 31 | 🔵 unplaced | Agentic RAG tutor built on LangGraph — a readable reference for the orchestration layer rather than a product. |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **MIT** · 1 094 B · `main` · `f88f69f` | 17 | 🔵 unplaced | Knowledge graph + local LLM + **Bayesian skill tracking**. One of very few rows carrying an explicit learner model rather than relying on prompt context. |

### The 2026 category: the agent *skill* as the unit of delivery

A genuinely new shape this pass. A large and fast-moving share of `topics/ai-tutor` is no longer applications
but **skills for agent harnesses** — markdown-plus-scripts packages that run inside Claude Code and similar
hosts. They carry no UI, no hosting and no database, and they are overwhelmingly MIT. For a studio this is the
lowest-cost delivery vehicle that exists: pedagogy as a versioned artefact, not a product.

| skill | grant (payload · bytes · ref · SHA) | ★ | region | scope |
|---|---|---|---|---|
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | **MIT** · 1 064 B · `main` · `2cd8393` | 771 | 🔵 unplaced | Self-study agent: plans learning paths, explains concepts, guides projects |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | **MIT** · 1 065 B · `main` · `b9e84f5` | 303 | 🔵 unplaced | Slide-based teaching, quizzing, **cross-session memory** |
| [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) | **MIT** · 1 081 B · `main` · `25ea970` | 286 | 🔵 unplaced | DSA mentor with progressive hints and mock interviews |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | **MIT** · 1 069 B · `main` · `b391898` | 285 | 🔵 unplaced | Adaptive tutor that selects the next lesson from observed learner behaviour |
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | **MIT** · 1 102 B · `main` · `075c189` | 242 | 🔵 unplaced | **Diagnosis-first** tutoring for STEM/CS — assesses before teaching |
| [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | **MIT** · 1 083 B · `main` · `c85ca76` | 166 | **APAC** (China, civil-service exams) | Jurisdiction-specific exam coaching |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** · 1 068 B · `main` · `f0142f2` | 137 | 🔵 unplaced | **Local-first**; notes, quizzes, flashcards from uploaded material |
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | **MIT** · 1 068 B · `main` · `b4c9352` | 107 | 🔵 unplaced | A *collection* of teaching/study skills — the bundle pattern |

### LATAM

Placed rows, not a gap. Both found by querying in Portuguese and Spanish rather than in English — the
single highest-yield move for this region, confirmed again this pass.

| row | grant (payload · bytes · ref · SHA) | ★ | region | note |
|---|---|---|---|---|
| [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) | **MIT** · 1 085 B · `main` · `bbeea5a` | — | **LATAM** (Brazil, pt-BR) | Interactive pt-BR platform, **205 modules**, AI tutor "Nilo" with optional OpenAI-compatible LLM and an **offline local fallback**; React + FastAPI + SQLite. MIT end to end. |
| [`programadores-obreros/Agente-editor-inet`](https://github.com/programadores-obreros/Agente-editor-inet) | 🔴 **GPL-3.0** · 35 149 B · `main` · `0fa7298` | — | **LATAM** (Argentina, INET) | Teaching agent for Arduino/ESP32 in Argentine technical schools; runs **offline, double-click**. Pedagogically excellent, 🔴 copyleft — integrate, do not absorb. |

## Negatives and licence flags — read before you quote a blog

These are the rows most likely to be mis-stated elsewhere. Each was read from the payload this pass.

| row | what is widely claimed | what the payload says |
|---|---|---|
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | listed in roundups as a permissive open tutor (~932★) | 🔴 **GPL-3.0**, 35 149 B, `main` · `5c2f924`. Not permissive. |
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 a widely-cited LMS comparison lists it as **MIT** | 🔴 **AGPL-3.0**. `LICENSE` is absent; `license.txt` (lowercase, 33 893 B) is the AGPL. The blog claim is false. |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | "MIT" | 🟡 **Split grant.** `LICENSE` is **CC-BY-4.0** (18 650 B); `LICENSE-CODE` is **MIT** (1 141 B). The code grant is MIT — cite the file, not the repo. |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 567★, prominent on `topics/ai-tutor` | 🔴 **AGPL-3.0** (1 134 B — a short-form AGPL grant, unusual). |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | self-hosted language tutor, 164★ | 🔴 **AGPL-3.0**. Self-hosting does not imply a permissive grant. |
| [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | learner-owned AI education platform, 88★ | 🔴 **GPL-3.0** |
| [`yh2072/edgameclaw`](https://github.com/yh2072/edgameclaw) | material → game-based course, 71★ | 🔴 **AGPL-3.0** |
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 62★, six specialised agents | 🔴 **No licence payload** in 17 candidate filenames. No usable grant. |
| [`LAION-AI/Desktop_BUD-E`](https://github.com/LAION-AI/Desktop_BUD-E) | LAION educational voice assistant, 43★ | 🔴 **No licence payload** in 17 candidate filenames. |

🔴 **Standing rate, measured across all 92 slugs resolved this pass: 6 carry no licence payload at all.**
That is ~1 in 15 — better than pass 87's 1-in-3 for fresh `ai-tutor` rows, because this pass weighted
established repos more heavily. The sampling difference is the explanation; the earlier figure is not withdrawn.

## What this shelf still does not have

- 🔵 **Checkers, not generators.** The shelf is dense with content *generators* and nearly empty of tools that
  *audit* instructional quality, alignment or accessibility. The only accessibility checker found is
  [`ucfopen/UDOIT`](https://github.com/ucfopen/UDOIT) — 🔴 **GPL-3.0**, and not AI-driven. A targeted search for
  AI accessibility/alignment checkers in education returned nothing usable this pass. **Written down as a gap, not glossed.**
- 🔵 **Region placement.** 14 of the agent rows above are honestly **unplaced** — the publisher's country could
  not be established from the repo this pass. That is recorded rather than guessed.
- 🔵 **Learner models.** Only `adaptive-knowledge-graph` (Bayesian) and `Bloom` carry an explicit learner model.
  Nearly everything else relies on the context window, which is not a mastery estimate.

*Prior pass content for this file is preserved in git history at commit `457eaba` and earlier; it is not duplicated here.*
