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

## Added in the fifth pass of 2026-10-06

**Channel: institution-first search** — funding bodies, ministries, universities
and research groups, queried by name in English and Spanish. All licences read
from each repository's own `LICENSE` payload via `raw.githubusercontent.com`.

| Repo | Licence (read from payload) | ★ | Role in the stack |
|---|---|---|---|
| [Coursemology/coursemology2](https://github.com/Coursemology/coursemology2) | **MIT** (`master/LICENSE`, © 2023 Coursemology.org) | **158** · 78 forks · **15,802 commits** | **LMS core, permissive.** NUS-origin gamified learning platform: Rails 8 API, React client, Keycloak auth. "Currently supported by the AI Centre for Educational Technologies" and the deployment host for Singapore's **Codaveri** programming tutor. The one MIT LMS in this KB with a decade-scale commit history |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | **MIT** (`main/LICENSE`, 2026) | 8 · 2 forks · 98 commits | **Compliance scaffolding.** Six-tier risk classifier over the Act's decision tree, **61 conformity checklist items** (risk management, data governance, documentation, human oversight), **8 document templates**. CLI + zero-dependency TypeScript SDK + client-only Next.js UI. **No education content** — supply the Annex III point 3 profile yourself (pattern P13) |
| [compl-ai/compl-ai](https://github.com/compl-ai/compl-ai) | **Apache-2.0** (`main/LICENSE`) | not read this pass | **Compliance measurement.** ETH Zurich framework pairing a technical interpretation of the AI Act with a generative-model benchmarking suite. Use it for the evidence the checklist above asks for |
| [crpf-mitadt/Indian-AI-for-Education](https://github.com/crpf-mitadt/Indian-AI-for-Education) | **CC0-1.0** (`main/LICENSE`) | not read this pass | **Regional index, not a dependency.** Curated map of Indian education AI: datasets, models, ASR, TTS, OCR, machine translation, infrastructure, benchmarks, research. CC0 means the map is free of attribution obligations; **every item it indexes still needs its own payload probe** |

### Coursemology is the licence answer to the Moodle question

This KB's platform shortcut has sent "needs permissive IP with no copyleft
exposure" to Frappe LMS and Kolibri, because Moodle, Open edX, Chamilo, Sakai and
ILIAS are all GPL-family. Coursemology changes that answer for **higher-education
and CS-teaching** engagements specifically:

| | Moodle / Open edX | Coursemology |
|---|---|---|
| Licence | GPL-3.0 / AGPL-3.0 family | **MIT** |
| Client fork, rebranded and resold | copyleft obligations attach | **no copyleft exposure** |
| Commit history | very large | **15,802 commits** |
| Community size | enormous | **158★ — small, and that is the real risk** |
| AI integration today | plugin / XBlock side-car | AICET's Codaveri already runs on it, closed source |

**The honest trade.** You swap a copyleft obligation for a **maintenance
concentration risk**: 158★ means a small contributor base and, realistically,
NUS-dependent maintenance. Take Coursemology where the client wants to own and
rebrand the platform outright and has engineering capacity; stay on Moodle or Open
edX where community breadth and plugin supply matter more than licence purity.
Do not present it as a drop-in Moodle replacement — its data model and its Keycloak
dependency are not Moodle's.

### A licence warning that applies per model, not per repository

[aisingapore/sealion](https://github.com/aisingapore/sealion) (424★) is the
substrate anyone would reach for to build a Southeast Asian education layer, and
it has **no `LICENSE` payload** at any probed path. Its README §Licensing says
the project embraces MIT "as much as possible; however, the exact licensing terms
may vary depending on the underlying base model's restrictions" — Llama3-derived
variants carry **commercial-use restrictions**, Gemma-derived variants carry
different terms again — and directs you to each model's **Hugging Face model
card**.

**So: clear rights per model, per release, before a SEA sovereign-model education
engagement is scoped.** A repository-level licence check on `sealion` returns
nothing, and a studio that stops there will have cleared nothing at all.

## Added in the sixth pass of 2026-10-06 — the speech and language substrate

Every tutor elsewhere in this KB is, by default, **mute and monolingual**. This
shelf is the layer that fixes that, and before this pass the KB had **no entry for
it at all**. Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page. Discovery narrative in `agents/trending.md`, sixth pass.

### Speech — recognition, synthesis, diarization

| Repo | Licence (payload) | ★ / commits | Role |
|---|---|---|---|
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | **Apache-2.0** (`master/LICENSE`) | **15.1k** / 2,092 | **The headline addition.** STT **+** TTS **+** speaker diarization **+** VAD in one permissive tree, running **with no Internet connection** on Android, iOS, HarmonyOS, Raspberry Pi, RISC-V and x86 servers, with bindings for 12 languages. Replaces four dependencies with one and is the component the offline-first pattern was missing |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | **MIT** (`master/LICENSE`) | 25.7k / 267 | **The ASR to deploy.** CTranslate2 reimplementation of Whisper — faster, lower memory, same weights |
| [openai/whisper](https://github.com/openai/whisper) | **MIT** (`main/LICENSE`) | **110k** / 171 | The reference implementation and the accuracy baseline to quote |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | **BSD** (`main/LICENSE`) | — | **Word-level timestamps** plus diarization. The timestamps are what turn a transcript into a *fluency measure* — see P17 |
| [speechbrain/speechbrain](https://github.com/speechbrain/speechbrain) | **Apache-2.0** (`main/LICENSE`) | 11.9k / **10,611** | PyTorch toolkit: 200+ training recipes over 40+ datasets, 20 speech and text tasks. The bridge when a language needs a model trained rather than downloaded |
| [espnet/espnet](https://github.com/espnet/espnet) | **Apache-2.0** (`master/LICENSE`) | 10.0k / **27,378** | End-to-end speech toolkit with the deepest recipe archive here. First stop for a language nothing off-the-shelf covers |
| [huggingface/parler-tts](https://github.com/huggingface/parler-tts) | **Apache-2.0** (`main/LICENSE`) | 5.6k / 199 | Prompt-controllable TTS — the voice is described in text, so register can be tuned per age group without retraining |
| [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) | **Apache-2.0** (`main/LICENSE`) | — | Full speech + LLM training stack where GPUs are available |
| [pytorch/audio](https://github.com/pytorch/audio) | **BSD** (`main/LICENSE`) | — | Audio primitives underneath the above |
| [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | **MPL-2.0** (`main/LICENSE.txt`) | 2.3k / **5,309** | Voice cloning and XTTS-class synthesis, **actively maintained** at Idiap Research Institute (Switzerland). PyPI `coqui-tts`. **Use this, not the 46.1k★ original** — see the warnings below |

### Language — translation and local-language models, placed by region

| Repo | Licence (payload) | ★ / commits | Region | Coverage |
|---|---|---|---|---|
| [AI4Bharat/IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | **MIT** (`main/LICENSE`) | 478 / 124 | APAC | Translation across **all 22 scheduled Indian languages**, with script unification across Devanagari, Perso-Arabic and others |
| [AI4Bharat/Indic-TTS](https://github.com/AI4Bharat/Indic-TTS) | **MIT** (`master/LICENSE.txt`) | 406 / 58 | APAC | TTS in **13** languages: Assamese, Bengali, Bodo, Gujarati, Hindi, Kannada, Malayalam, Manipuri, Marathi, Odia, Rajasthani, Tamil, Telugu |
| [AI4Bharat/IndicWav2Vec](https://github.com/AI4Bharat/IndicWav2Vec) | **MIT** (`main/LICENSE`) | 121 / 131 | APAC | ASR pretrained on **40** Indian languages; fine-tuned for Bengali, Gujarati, Hindi, Marathi, Nepali, Odia, Tamil, Telugu, Sinhala, plus Kannada and Malayalam |
| [AI4Bharat/IndicLLMSuite](https://github.com/AI4Bharat/IndicLLMSuite) | **MIT** (`master/LICENSE`) | — | APAC | Data and recipe suite for building Indic LLMs |
| [AI4Bharat/Shoonya](https://github.com/AI4Bharat/Shoonya) | **MIT** (`master/LICENSE`) | 72 / 69 | APAC | *"Open source platform to annotate and label data at scale."* The **human-in-the-loop stage** every pattern in this KB specifies, and the only shelved tool that implements it |
| [SunbirdAI/salt](https://github.com/SunbirdAI/salt) | **Apache-2.0** (`main/LICENSE`) | 15 / 303 | EMEA | **Uganda.** Translation (~25k sentences), ASR (~5k) and **studio-recorded TTS data (~5k, professional voice actors)** across English (Ugandan/Kenyan accents), **Luganda, Swahili, Ateso, Lugbara, Acholi, Runyankole**. Two AfricaNLP papers |
| [masakhane-io/masakhane-mt](https://github.com/masakhane-io/masakhane-mt) | **MIT** (`master/LICENSE`) | 327 / 645 | EMEA | **Africa-wide.** Machine translation from a 1,000-participant, 30-country community. **226 forks against 327 stars** — a deployment signal, not a vanity one |
| [masakhane-io/masakhane-ner](https://github.com/masakhane-io/masakhane-ner) | **Apache-2.0** (`main/LICENSE`) | — | EMEA | Named-entity recognition for African languages |
| [Polygl0t/Polygl0t](https://github.com/Polygl0t/Polygl0t) | **Apache-2.0** (`main/LICENSE`) | 27 / 379 | EMEA | **University of Bonn** Polyglot initiative. LLM training/eval foundry, FineWeb-2 pipeline, "support for thousands of languages." Home of **Tucano 2** (0.5–3.7B Portuguese, arXiv 2603.03543) |
| [Nkluge-correa/Tucano](https://github.com/Nkluge-correa/Tucano) | **Apache-2.0** (`main/LICENSE`) | 86 / 29 | LATAM *(origin)* | Portuguese-native open LLM suite, peer-reviewed in *Patterns* ([10.1016/j.patter.2025.101325](https://doi.org/10.1016/j.patter.2025.101325)). **Archived 2026-02-24** — still usable, no longer developed. Successor is the Bonn-hosted row above |

### Five licence warnings on the rows above — read before selecting any of them

**1. Piper relicensed, and the permissive version is frozen.**
[rhasspy/piper](https://github.com/rhasspy/piper) is **MIT** (`master/LICENSE.md`,
© 2022 Michael Hansen), 11.3k★ — and **archived read-only since 2025-10-06**, its
notice pointing to [OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl),
which is **GPL-3.0** (`main/COPYING`). Piper is the offline-TTS default of Home
Assistant and NVDA and runs on a Pi 4, so it is the natural reach for low-cost
classroom voice. **There is no option that is both permissive and maintained.**
Deliberately **not shelved above**: use `sherpa-onnx` (Apache-2.0) or
`idiap/coqui-ai-TTS` (MPL-2.0) instead, and reach for Piper only with the
frozen-vs-copyleft trade made explicitly and in writing.

**2. The 46.1k★ Coqui repository is not the live one.**
[coqui-ai/TTS](https://github.com/coqui-ai/TTS) is **MPL-2.0** and **unmaintained**
— the company wound down. The Idiap fork shelved above has **5,309 commits against
the original's 4,668**. Depend on the fork; cite the original only for history.

**3. SeamlessM4T is non-commercial — a hard reject.**
[facebookresearch/seamless_communication](https://github.com/facebookresearch/seamless_communication)
carries **Attribution-NonCommercial 4.0 International** in `main/LICENSE`. It is
the first result for "open source multilingual speech" and **cannot be used in
billable work**. Compose Whisper (MIT) + IndicTrans2 (MIT), or sherpa-onnx
(Apache-2.0), to reach the same capability.

**4. SEA-LION has no repository-level grant, by design.**
[aisingapore/sea-lion](https://github.com/aisingapore/sea-lion) has **no `LICENSE`
payload** (3 branches × 6 filenames probed). Its README states the terms *"may
vary depending on the underlying base model's restrictions"* — Llama-derived
variants may carry Meta's commercial restrictions — and directs you to each
HuggingFace **model card**. **The licence is a property of the checkpoint, not the
project**, so an APAC engagement must review it per model file and **re-review on
every checkpoint change**. Not shelved as a dependency for this reason.

**5. An unlicensed catalogue is still unlicensed.**
[AI4Bharat/indicnlp_catalog](https://github.com/AI4Bharat/indicnlp_catalog) has
**no `LICENSE` payload** despite five MIT siblings in the same organisation. Use
it to *find* resources; probe every resource it names. (Same shape as
`AI-for-Education/Luganda-linguistic-benchmarks` in the fourth pass — and note
that `SunbirdAI/salt` above is the **Apache-2.0 answer to that specific
rejection**, covering Luganda and five more Ugandan languages.)

### Why this shelf changes the architecture, not just the feature list

Three consequences worth stating, because they are not obvious from the table:

- **Voice stops being a proprietary-API-shaped problem.** `sherpa-onnx` alone
  delivers STT, TTS, diarization and VAD under Apache-2.0 on embedded hardware.
  Spoken practice, oral assessment and role-play become deployable where there is
  no connectivity and no per-token budget.
- **Mother-tongue instruction becomes a permissive capability in two regions.**
  India (22 languages, MIT) and Uganda/Africa (6 Ugandan languages Apache-2.0,
  plus Masakhane's continental MT, MIT) can be served from the shelf. **Elsewhere
  it cannot** — see the regional honesty note in `intel/market.md`.
  **⚠️ SUPERSEDED by the seventh pass of 2026-10-06: it is at least three
  regions.** ASEAN has a permissive layer across **Vietnamese, Thai, Malay and
  Indonesian** — `underthesea` (Apache-2.0, 1.8k★), `pythainlp` (Apache-2.0,
  1.2k★, 6,649 commits), `malaya` + `malaya-speech` (both MIT) and `nusa-crowd`
  (Apache-2.0, 143 datasets). See the seventh-pass section below. The sixth pass
  reached "two regions" by searching for sovereign **models** and finding
  SEA-LION unlicensed; the toolkits were one query away in another language.
- **Masakhane licenses three repositories three ways** — MIT, Apache-2.0 and GPL
  inside one owner. The fourth pass's rule was "five MIT siblings do not license
  the sixth." The stronger rule: **sibling licences need not even share a
  class.** Probe every repository, every time.

## Added in the seventh pass of 2026-10-06 — the ASEAN language substrate, and trend 21 falsified

**Channel new to this KB this pass: native-language search.** Earlier passes
searched in English and, in the fourth pass, Spanish and Portuguese. This pass
searched in **Japanese, Korean, Arabic and Bahasa/Thai/Vietnamese**. The sixth
pass had closed with a clean, falsifiable claim — *"mother-tongue AI is a
two-region capability"*, India and Africa, with ASEAN explicitly named as the
place where *"the nearest thing, SEA-LION, has no repository-level licence at
all."*

**That claim is wrong, and this is the shelf that falsifies it.** ASEAN has a
permissive, self-hostable language layer covering **five languages across four
countries**, most of it Apache-2.0, some of it with more commits than anything
on the India shelf. It was invisible to six passes because **SEA-LION is a
sovereign *model* and these are language *toolkits*** — a different noun, and
nobody had searched for the noun.

Licences read from each repository's own `LICENSE` payload via
`raw.githubusercontent.com` on 2026-10-06; star/fork/commit counts read from the
repository page the same day. **13 repositories probed, 13 resolved.**

### Language — ASEAN, placed by country

| Repo | Licence (payload) | ★ / forks / commits | Country | Coverage |
|---|---|---|---|---|
| [undertheseanlp/underthesea](https://github.com/undertheseanlp/underthesea) | **Apache-2.0** (`main/LICENSE`) | **1.8k** / 307 / 1,276 | **Vietnam** | The largest asset on this shelf. 13 Vietnamese tasks — sentence segmentation, text normalization, **diacritics restoration**, word segmentation, POS, chunking, NER, classification, sentiment, language detection, dependency parsing, translation and TTS. **v9.3.0 rebranded the project to an "Open-source Agentic AI Toolkit"** with multi-provider agent support (OpenAI, Azure OpenAI, Anthropic Claude, Google Gemini) layered over the Vietnamese NLP core |
| [PyThaiNLP/pythainlp](https://github.com/PyThaiNLP/pythainlp) | **Apache-2.0** (`main/LICENSE`) | **1.2k** / 304 / **6,649** | **Thailand** | *"Thai natural language processing in Python."* Sentence, word and **subword** tokenization — the hard problem in a script with no spaces — plus POS tagging, romanization and **IPA transliteration**, spelling correction, soundex, collation, number-to-text, and a `thainlp` CLI. v5.3.8, Python 3.9+, self-declared **"Project Status: Active."** The deepest commit history of any language toolkit in this KB outside the general speech shelf |
| [malaysia-ai/malaya](https://github.com/malaysia-ai/malaya) | **MIT** (`master/LICENSE`, © 2018 huseinzol05) | 530 / 141 / 961 | **Malaysia** | *"Natural-Language-Toolkit library for bahasa Malaysia, powered by PyTorch."* NER with a named-entity framework, POS, sentiment, emotion, subjectivity, language detection and normalization. Pretrained models on HuggingFace (`mesolitica`); docs at `malaya.readthedocs.io` |
| [malaysia-ai/malaya-speech](https://github.com/malaysia-ai/malaya-speech) | **MIT** (`master/LICENSE`, © 2020 HUSEIN ZOLKEPLI) | 291 / 51 / 755 | **Malaysia** | *"Speech-Toolkit library for Malaysian language, powered by PyTorch."* The **only ASEAN-placed permissive speech toolkit** found; ships a `malay_vits` TTS path. Pair with `sherpa-onnx` for the offline runtime |
| [IndoNLP/nusa-crowd](https://github.com/IndoNLP/nusa-crowd) | **Apache-2.0** (`master/LICENSE`) | 292 / 64 / 992 | **Indonesia** | *"A collaborative project to collect datasets in Indonesian languages."* **143 registered datasets** behind standardized dataloaders, built by a credited multi-institution consortium; paper *NusaCrowd: Open Source Initiative for Indonesian NLP Resources* ([arXiv:2212.09648](https://arxiv.org/abs/2212.09648)). Contributors earn **co-authorship by contribution points** — a governance model worth copying for a ministry corpus engagement |
| [indobenchmark/indonlu](https://github.com/indobenchmark/indonlu) | **Apache-2.0** (`master/LICENSE`) | — (not read this pass) | **Indonesia** | Indonesian natural-language-understanding benchmark — the evaluation half of the row above |

### Read this shelf honestly — three qualifications

- **None of it is education-specific.** Exactly like AI4Bharat on the India
  shelf, these are general-purpose language toolkits. They make a mother-tongue
  tutor *possible*; they do not make one. The pedagogy layer is still yours to
  build, which is the opportunity (**P19**).
- **Only one covers speech.** `malaya-speech` is the single ASEAN-placed
  permissive speech toolkit here. Thai, Vietnamese and Indonesian have the
  **text** layer and no local **voice** layer, so spoken practice in those three
  languages routes through the general shelf — `sherpa-onnx` (Apache-2.0) or
  Whisper/faster-whisper (MIT) — and must be accuracy-tested per language rather
  than assumed.
- **Two of these are corpora-and-recipes, not runtimes.** `nusa-crowd` and
  `indonlu` give you data and evaluation; they are not something you deploy. Size
  the engagement accordingly.

### One more licence warning, and the first measured counter-example to it

[malaysia-ai/malaysian-dataset](https://github.com/malaysia-ai/malaysian-dataset)
— **no `LICENSE` payload** (2 branches × 6 filenames probed), and at **345★** it
is the organisation's **second most-starred repository**, ahead of
`malaya-speech`. Its two code siblings are both MIT. **Not shelved. Not
shippable.**

This is the **second time this KB has found the pattern in the same shape**: the
sixth pass recorded `AI4Bharat/indicnlp_catalog` as unlicensed among five MIT
siblings. Two independent organisations, two regions, and in both the repository
without a grant is the **data/catalogue** one while the **code** repositories are
permissive. A tempting rule follows — *the data layer is where the grant goes
missing* — and this pass **measured its counter-example in the same sweep**:
`IndoNLP/nusa-crowd` is a dataset hub of 143 corpora and it is **Apache-2.0**.

**So state it as a prior, not a law: on a data or catalogue repository, assume no
grant until the payload says otherwise — and probe it, because one in three
cedes.** The operational rule is unchanged and now carries three instances
instead of one: **probe every repository, every time, and probe the dataset
sibling separately from the code.**

## Added in the eighth pass of 2026-10-06 — the LATAM language substrate, and where it stops

The seventh pass falsified "mother-tongue AI is a two-region capability" by
searching ASEAN for language **toolkits** instead of sovereign **models**. The
eighth pass ran the same move at the one gap this KB called its firmest: **no
LATAM-origin permissive education project.**

**The move works at the majority-language layer and fails at the indigenous
layer — and it fails for a reason this shelf has seen before in MEA.**
Licences read from each repository's own `LICENSE` payload.

### Language — Spanish and Portuguese, permissive and real

| Repo | Licence (payload) | ★ / forks / commits | What it is |
|---|---|---|---|
| [neuralmind-ai/portuguese-bert](https://github.com/neuralmind-ai/portuguese-bert) | **MIT** (`master/LICENSE`, © 2020 NeuralMind — Fabio Capuano de Souza, Rodrigo Nogueira, Roberto de Alencar Lotufo) | **886** / 139 / 20 | **BERTimbau** — BERT-Base and BERT-Large for **Brazilian Portuguese**, trained on **BrWaC** for 1M steps with whole-word masking. State of the art on NER, STS and RTE at publication. **Brazil-origin, and the first Brazil-origin permissive asset on this shelf** |
| [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | **Apache-2.0** (`master/COPYING`) | — | Offline ASR for 20+ languages including **Spanish and Portuguese**, Raspberry-Pi-class hardware, Python/Java/C#/Node bindings. Permissive, maintained — **global-origin, not LATAM** |

`speechbrain/speechbrain` (Apache-2.0) on the sixth-pass shelf remains the
bridge when a language needs a model **trained** rather than downloaded.

### Language — indigenous languages of the Americas: the capability is there, the grant is not

| Repo | Licence state (payload) | Coverage |
|---|---|---|
| [Llamacha/IWSLT2023_Quechua_data](https://github.com/Llamacha/IWSLT2023_Quechua_data) | ⚠️ payload **Apache-2.0**, README **CC BY-NC-ND 3.0** — **scope conflict, see below** | **Peru** — ~1h40m aligned Quechua–Spanish speech + pointers to 60h transcribed Siminchik audio. Southern Quechua |
| [pywirrarika/naki](https://github.com/pywirrarika/naki) | **GPL-3.0** (`master/LICENSE`) | Curated NLP research and engineering index for Native American languages |
| [AmericasNLP/americasnlp2021](https://github.com/AmericasNLP/americasnlp2021) | **No `LICENSE` payload** | Shared task — **Aymara** (6,531 pairs), **Nahuatl** (16,145), **Quechua** (125,008) |
| [AmericasNLP/americasnlp2022](https://github.com/AmericasNLP/americasnlp2022) | **No `LICENSE` payload** | Second probed edition |
| [AmericasNLP/americasnlp2023](https://github.com/AmericasNLP/americasnlp2023) | **No `LICENSE` payload** | Third probed edition |
| [AmericasNLP/americasnlp2024](https://github.com/AmericasNLP/americasnlp2024) | **No `LICENSE` payload** — 404 at root **and** in both task subdirectories | MT into indigenous languages, **plus Shared Task 2: "Creation of Educational Materials for Indigenous Languages"** — sentence-transformation and fill-in-the-blank exercise generation, data and baselines shipped. **No root `README.md`; existence confirmed via `master/ST1_MachineTranslation/README.md`** |
| [monirome/asr-indigenous-languages](https://github.com/monirome/asr-indigenous-languages) | **No `LICENSE` payload** | Fine-tuned ASR: **Quechua, Guaraní, Bribri, Kotiria, Wai'khana** |
| [UBC-NLP/IndT5](https://github.com/UBC-NLP/IndT5) | **No `LICENSE` payload** | Text-to-text transformer for **10** indigenous languages |
| [aoncevay/mt-peru](https://github.com/aoncevay/mt-peru) | **No `LICENSE` payload** | *"Peru is Multilingual, Its Machine Translation Should Be Too?"* |
| [aoncevay/quechua-nlp](https://github.com/aoncevay/quechua-nlp) | **No `LICENSE` payload** | Standard Southern Quechua data for NLP |
| [Llamacha/IWSLT2025_Quechua_data](https://github.com/Llamacha/IWSLT2025_Quechua_data) | **No `LICENSE` payload** | The 2025 edition — **same organisation, licensed 2023 and not 2025** |
| [jnehring/awesome-low-resource-languages](https://github.com/jnehring/awesome-low-resource-languages) | **No `LICENSE` payload** | Endangered / low-resource language resource index |

**Ten of twelve carry no grant at all.** **AmericasNLP** — the flagship academic
venue for the indigenous languages of the Americas — has run **four probed
editions (2021, 2022, 2023, 2024) without a `LICENSE` file in any of them**, and
its 2024 edition ships the one task on this shelf that is **explicitly an
education task**: *"Creation of Educational Materials for Indigenous
Languages"*, with data and baseline scripts and no grant. The same author
(`aoncevay`) licensed neither of two repositories; the same organisation
(`Llamacha`) licensed one edition and not the next.

### ⚠️ The `Llamacha` scope conflict — it defeats this shelf's own method

Every licence on this shelf is read from the repository's own `LICENSE` payload.
Do that to `Llamacha/IWSLT2023_Quechua_data` and you get **complete, unambiguous
Apache-2.0** from `main/LICENSE`.

**The README says otherwise:**

> All audio recordings are property of Siminchikkunarayku and Llamacha.
> This work is licensed under a Creative Commons
> **Attribution-NonCommercial-NoDerivs 3.0 Unported License**.

**NonCommercial and NoDerivs — unusable in commercial client work.** The Apache
file plausibly covers the repository's scripts; the **data**, which is the only
reason to clone it, is NC/ND.

**This is a third licence trap, distinct from the two this KB already tracks.**
`p184` catches a holder foreign to the project. The seventh pass's
MathTutorBench case catches a file that contradicts itself internally. This is
**a correct, complete licence file applied to the wrong scope.**

**Rule for this shelf, from this pass forward: for any repository whose value is
data, audio, a corpus or model weights, the payload is necessary and not
sufficient.** Read the README's licence section too, and treat the
**asset-scope** statement as controlling for the asset.

### Why this shelf matters even though most of it is unusable

**Because it is the exact layer a regional tutor needs next, and it is one
`LICENSE` file per repository away from being usable.**

`LabSirius/TutorIA`'s own **RNF-10** specifies Colombian Spanish for v1.0 *"con
posibilidad futura de soportar **lenguas nativas**"*. Latam-GPT lists indigenous
languages as roadmap. So the demand is written down in two places, and the
supply — corpora, ASR for five languages, MT, benchmarks, a T5 for ten
languages — **already exists, funded and published.** What is missing is
redistribution rights.

**This is the MEA diagnosis in a second region.** The seventh pass concluded of
MEA: *"the binding constraint is not interest, funding or capability — it is
licensing hygiene. Three `LICENSE` files would change the regional answer."*
That sentence is now true of the LATAM indigenous layer word for word, and the
eighth pass found a **remedy that works prospectively**: a submission rule in a
university event's terms produced **20 licensed repositories in eight hours**
(see `agents/top.md`, the CAi UC holder warning, and `intel/market.md`).

**For an engagement:** a Quechua or Guaraní tutor is blocked on **data rights,
not on modelling**. Budget the licence conversation with Llamacha,
Siminchikkunarayku and the AmericasNLP organisers as a project line item, not an
afterthought — and note that `vosk-api` (Apache-2.0) plus `speechbrain`
(Apache-2.0) give you a permissive *pipeline* into which licensed data can be
dropped the moment it exists.

## Added in the ninth pass of 2026-10-06 — a ministry's MIT estate, and the offline stack's real licence shape

Channel: the **funder and procurement channel** and its government twin, the
**education-ministry engineering organisation**. Nine passes had swept
hackathons, universities, ministries *by name*, funding bodies, GitHub topic
pages and academic papers. **None had swept a ministry's own GitHub org.**

### The UK Department for Education estate — government-grade, production, MIT

`DFE-Digital` is the UK Department for Education's engineering org. It runs
**live national education services** in the open, under MIT. Licences read from
payload:

| Repo | Licence | ★ | Lang | Role |
|---|---|---|---|---|
| [DFE-Digital/apply-for-teacher-training](https://github.com/DFE-Digital/apply-for-teacher-training) | **MIT** (`main/LICENCE`) | 38 | Ruby | The national service for applying to teacher-training courses |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** (`main/LICENSE`) | 27 | Ruby | National teaching job-listing service |
| [DFE-Digital/get-into-teaching-app](https://github.com/DFE-Digital/get-into-teaching-app) | **MIT** (`master/LICENCE`) | 25 | Ruby | Teacher-recruitment site and candidate journey |
| [DFE-Digital/publish-teacher-training](https://github.com/DFE-Digital/publish-teacher-training) | **MIT** (`main/LICENSE`) | 12 | Ruby | Provider course publishing + candidate discovery |
| [DFE-Digital/register-trainee-teachers](https://github.com/DFE-Digital/register-trainee-teachers) | **MIT** (`main/LICENCE`) | 12 | Ruby | Trainee registration for initial-teacher-training placements |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** (`main/LICENCE`) | 9 | C# | GIAS — the national schools register |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** (`main/LICENSE`) | 5 | C# | Compares one school's metrics against similar institutions |

### What this estate is good for, stated precisely

**It is administrative software, not AI, and it closes no AI gap in this KB.**
Taken for what it is, it is the first thing of its kind on these shelves:

1. **Reference architecture for education workflow at national scale.** Five of
   the seven are Ruby services that have run a country's teacher pipeline.
   For an EMEA public-sector engagement, *"here is how a ministry built this, and
   you may read and reuse the code"* is a stronger opening than a vendor demo.
2. **Schemas you will have to integrate with anyway.** GIAS is the UK's
   authoritative schools register; `register-trainee-teachers` and
   `publish-teacher-training` encode the ITT domain model. Any UK education
   engagement meets these data structures eventually — and here they are, MIT.
3. **A benchmarking component with the right shape.**
   `education-benchmarking-and-insights` does school-to-peer-group comparison —
   the data layer under any "how is my school doing" analytic, and the natural
   grounding source for a reporting agent.
4. **Procurement credibility.** An MIT licence from a ministry is the cleanest
   possible answer to the public-sector question *"can we actually own and audit
   this?"*

**What it is not:** none of it is AI, none of it is a tutor, and its star counts
(5–38★) reflect government repos that are consumed as services rather than
forked. **Do not read low stars as low maturity here** — these are production
systems for a national education system. It is the one place in this KB where
the star signal is actively misleading in the *opposite* direction to usual.

### ⚠️ The licence-filename warning that changes this KB's method

**Four of these seven grants are in a file spelled `LICENCE`.** Pattern **P22**'s
gate lists that spelling; **no recorded sweep in this KB has ever run it.** Every
probe set written down across nine passes — `LICENSE`, `LICENSE.md`,
`LICENSE.txt`, `COPYING`, `license.txt` — **matches none of these four files.** With the old set,
`apply-for-teacher-training`, `get-into-teaching-app`,
`register-trainee-teachers` and `get-information-about-schools` would all have
been recorded as **ungranted**. They are MIT.

**The probe set is now `LICENSE{,.md,.txt}`, `LICENCE{,.md,.txt}`, `COPYING`,
`COPYRIGHT`, `license.txt`, both branches.** Any earlier pass's "no grant"
verdict on a Commonwealth, MEA or ministry-adjacent repository should be treated
as **unconfirmed until re-probed** — those are exactly the repositories that
spell it the British way.

### Measured rejections from the same organisation

| Repo | ★ | Why rejected |
|---|---|---|
| `DFE-Digital/gias-query-tool` | 17 | **No licence payload.** The SQL query layer over GIAS — the most immediately useful tool in the org, and ungranted. Sixth pass running in which the most-reached-for asset of a sweep has no grant |
| `DFE-Digital/rsd-ai-libs` | 0 | **No payload.** *".NET library for building and evaluating Azure AI Foundry agents with guardrails, Azure AI Search, and MCP server support"* — a ministry building MCP agent tooling, which corroborates trend 4; unusable as code, citable as a signal |
| `DFE-Digital/sts-ai-support` | 1 | No licence shown on the org listing; not individually payload-probed |
| `DFE-Digital/ai-briefing-tool-prototype` | 0 | Non-production prototype; no licence shown |
| `DFE-Digital/rsd-common-ai-services` | 0 | Provisioning scaffolding; no licence shown |

**The asymmetry is the strategic finding:** the DfE's **administrative** tier is
production-grade and MIT; its **AI** tier is prototype-grade and unlicensed. A
consultancy's opening in EMEA public-sector education is therefore *not* "you
need a platform" — they built one — but **"your AI layer is five unlicensed
prototypes at zero stars, and your administrative layer is a licensed national
asset; let us build the first on top of the second."**

### The offline delivery stack, licence shape corrected

The eighth pass built the offline-first tier around Kolibri and EduFlow but could
not resolve RACHEL. Resolved this pass, and the stack's licensing is not what the
page implied:

| Repo | Payload | Licence | Usable? |
|---|---|---|---|
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `develop/LICENSE` | **MIT** | ✅ re-confirmed — the platform answer |
| [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft — see below |
| [kiwix/libkiwix](https://github.com/kiwix/libkiwix) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [kiwix/kiwix-android](https://github.com/kiwix/kiwix-android) | `main/COPYING` | **GPL-3.0** | ⚠️ copyleft |
| [openzim/libzim](https://github.com/openzim/libzim) | `main/COPYING` | **GPL-2.0** | ⚠️ copyleft, and GPL-2.0 ≠ GPL-3.0 for compatibility |
| [rachelproject/contentshell](https://github.com/rachelproject/contentshell) | **none** | README: *"Creative Commons - BY, SA, NC"* | ❌ **NonCommercial — do not ship** |

**Three warnings on that table:**

1. **RACHEL is out.** `contentshell` *is* RACHEL — the PHP CMS that serves
   content on RACHEL devices — and its only licence statement is a **content
   licence with NonCommercial, applied to software**, with no payload to weigh
   against it. Creative Commons advises against CC for software; either reading
   (unlicensed, or NC) stops a commercial deliverable. **Cite RACHEL as prior
   art for offline delivery; ship Kolibri.**
2. **The ZIM layer is GPL, and that is an architecture decision, not a
   footnote.** Offline Wikipedia/Wikibooks content ships as ZIM, and the entire
   reference implementation — `libzim` (GPL-2.0), `libkiwix`, `kiwix-tools`,
   `kiwix-android` (GPL-3.0) — is copyleft. You may deploy it; you may not
   statically link it into a proprietary client deliverable without taking the
   obligation. **Keep Kiwix as a separate process behind an HTTP boundary** —
   exactly the side-car reasoning this KB already applies to MCP — and the
   client's own code stays unencumbered.
3. **GPL-2.0 and GPL-3.0 in one dependency tree** (`libzim` vs `libkiwix`) is a
   combination to raise with counsel if anything is being linked rather than
   invoked. Process separation makes the question moot, which is a second reason
   for the side-car.

## Added in the twenty-first pass of 2026-10-06 — no new rows, and a second licence on the existing ones

🔵 **This pass adds no foundational repositories, and the reason is structural rather than a dry
sweep.** The declared-dependency channel does not discover projects; it **re-prices the ones already
here**. Every row on this shelf carried one licence — its own. The rows below now carry a second: the
licence of **what they install**.

⚠️ **The platform channel was re-probed and remains saturated**, verified by grep rather than
assumed: OpenEduCat, Open edX, Moodle, Sakai, OLAT/OpenOLAT, Chamilo, Gibbon, Frappe, `.LRN` all
already shelved. The one name new to the result set, **`CK-ERP`** — a 32-module education / ERP / CRM
/ MRP system — is recorded here as a **measured non-finding**: the most recent release note in the
result set is from **2010** and it is Drupal-6 era. 🔴 **Abandonware, not a shelf candidate.**

### What the foundation shelf installs

| Foundation row | Its licence | Direct deps | Closure verdict |
|---|---|---|---|
| `oppia/oppia` | Apache-2.0 | **152** | 🔴 **REVIEW-STRONG** — `mutagen` is `GPL-2.0-or-later`; `certifi` MPL-2.0; `orjson` `MPL-2.0 AND (Apache-2.0 OR MIT)`; `azure-cognitiveservices-speech` `Other/Proprietary License`. **148 of 152 clean** |
| `LearningEquality/kolibri` | MIT | **32** | ⚠️ **REVIEW-WEAK** — 2 LGPL rows, 2 unreadable. ⚠️ Measurable only via `[dependency-groups] base`; both canonical fields answer "nothing" and both are wrong |
| `huggingface/smolagents` | Apache-2.0 | 6 | 🟢 **CLEAN** — the smallest permissive surface on the shelf, now verified on both layers |
| `microsoft/agent-framework` | MIT | 1 | ⚠️ **CLEAN but uninformative** — `agent-framework-core[all]==1.20.0`; the closure is one level down |

🟢 **The operational consequence for foundation selection:** where two foundations are otherwise
comparable, **the one with the smaller declared surface is the cheaper one to clear legally**, and
that is now a measured property rather than an instinct. smolagents at 6 declared dependencies and
Oppia at 152 are not the same procurement task even when both say Apache-2.0.

### 🔴 The evidence tooling the twentieth pass went looking for is still absent — and now so is one more layer

⚠️ **The twentieth pass recorded zero occurrences of `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn` and `AIF360`.** 🔴 **A dependency-licence
audit is the same shape of missing instrument one layer further down:** this KB can now resolve a
licence per dependency, but it has **no SBOM layer** — no `syft`, no `cyclonedx`, no
`pip-licenses`/`license-checker` row anywhere on the shelf. 🔵 **Recorded as a declared gap with a
named next step rather than as a new row, because this pass did not verify any of those tools against
an education deployment and will not shelf what it has not read.**

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

## Added in the tenth pass of 2026-10-06 — the interoperability tier, and the sync engine under the offline platform

Two shelves this pass, both payload-verified, both arriving from a demand signal
rather than from a search for interesting code.

**All licences below were read from the repository's own payload** via
`raw.githubusercontent.com`, probed across **10 filenames × 2 branches**
(`LICENCE`/`LICENSE`/`licence`/`license`/`COPYING`, `.md` and `.txt` variants, on
`main` and `master`). The probe was validated against 6 known-payload controls
first; **6 of 6 resolved.** Star counts read from the rendered repository page the
same day.

### The interoperability tier — because 39% of district RFPs score it

The ninth pass found the procurement number: **39% of districts score
interoperability in their RFP rubrics** (CoSN, Tier 2). That makes the integration
layer a **scored deliverable**, not plumbing — and this is the entire permissive
shelf for it, split by runtime.

| Repo | License (read from payload) | ★ (2026-10-06) | Runtime | What it is |
|---|---|---|---|---|
| [Cvmcosta/ltijs](https://github.com/Cvmcosta/ltijs) | Apache-2.0 (`master/LICENSE`) | 373 | Node / TypeScript | Turns an application into a fully integratable **LTI 1.3 tool provider**. The highest-starred genuine LTI project, and the default when the AI layer is a Node service. |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | Apache-2.0 (`master/LICENSE`) | 124 | PHP | LTI 1.3 library published by **the standards body itself**. The reference implementation; the natural pairing when the LMS is Moodle. |
| [Unicon/tool13demo](https://github.com/Unicon/tool13demo) | Apache-2.0 (`master/LICENSE`) | 27 | Java / Spring Boot | LTI 1.3 tool in Spring Boot, from a long-standing higher-ed systems integrator. **The JVM entry point** — which is the stack most enterprise education clients already run. |
| [oxctl/spring-security-lti13](https://github.com/oxctl/spring-security-lti13) | Apache-2.0 (`master/LICENSE.txt`) | 25 | Java / Spring Security | LTI 1.3 for Spring Security, built on its OAuth2 support. Use this one when the client already has a Spring Security estate and wants LTI inside it rather than beside it. |
| [theopenem/OneRoster.NET](https://github.com/theopenem/OneRoster.NET) | **MIT** (`master/LICENSE`) | 6 (8 forks) | .NET | OneRoster 1.1 and 1.2 client. OAuth2 for 1.2, consumer credentials for 1.1. **Rostering calls only — gradebook is not implemented**, which is a scope limit to check against the rubric before you promise it. |

**Three warnings on this shelf.**

1. **Pin the right OneRoster.NET.** [jdolny/OneRoster.NET](https://github.com/jdolny/OneRoster.NET)
   is **also MIT** (`master/LICENSE`) and serves a byte-identical `README.md`
   (md5 `110b2e3439d86b6055821de382d90d61`, 2,048 bytes) and byte-identical
   licence text. **Both licences name `theopenem` as holder.** One asset, two
   addresses; the fork direction is **not established** in this environment
   (`github.com` → 403 to `curl`, no fork banner in the rendered page). Pin
   `theopenem`, whose owner matches the copyright line.
2. **"Caliper" is a homonym and it will waste a sweep.** `OneRoster OR Caliper OR
   "LTI 1.3" license:apache-2.0` returns **184 repositories**, led by
   `google/caliper` (818★, deprecated Java micro-benchmarking) and
   `hyperledger-caliper/caliper` (708★, blockchain benchmarking). Four of the top
   eight have nothing to do with 1EdTech Caliper Analytics. **The result count is
   not the ecosystem size.**
3. **There is no Python LTI 1.3 library on this shelf.** Node, PHP, Java and .NET
   are covered. Python — where almost all of the AI tutoring code in this KB is
   written — is not. In practice this means the tutoring service talks to a
   thin LTI adapter in another runtime, or the integration becomes a custom
   build. It is also the clearest open-source contribution opening this KB has
   found in the interoperability layer.

### The Learning Equality substrate — the sync engine, not just the app

This KB has recommended offline-first delivery for three passes while recording
the *application* (Kolibri) and not the machinery under it. The organisation holds
**238 repositories**. Probed this pass:

| Repo | License (read from payload) | ★ (2026-10-06) | What it is |
|---|---|---|---|
| [learningequality/morango](https://github.com/learningequality/morango) | **MIT** (`master/LICENSE`) | 15 (23 forks) | **Pure-Python peer-to-peer database replication engine for Django.** Marks chosen application models syncable; **certificate-based authentication** protecting data privacy and integrity; change-tracking and data-partitioning constructs designed for low-bandwidth links; works on **SQLite and PostgreSQL**. Branch `release-v0.9.x`. Built for Kolibri, **usable independently** — this is the component that makes an offline-first architecture real rather than aspirational. |
| [learningequality/le-utils](https://github.com/learningequality/le-utils) | **MIT** (`main/LICENSE.txt`) | not read this pass | Constants and utilities shared across Kolibri, Ricecooker and Studio. The shared vocabulary layer; required by anything that generates Kolibri channels. |

**And the two that came back ungranted, inside that same organisation:**

| Repo | License probe result | Consequence |
|---|---|---|
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | **no payload** (20 URLs) | Vue design system. Repository exists (`main/README.md` resolves). **Do not ship client UI from it** on the assumption that the org is MIT. |
| [learningequality/kolibri-server](https://github.com/learningequality/kolibri-server) | **no payload** (20 URLs) | Performance and caching access layer for Kolibri with multi-core support. **The repository exists** — its README is `main/README.rst`, not `README.md`. **No licence payload under any of 20 URLs.** Treat as unlicensed until a payload is read. |

**Two of four new probes in the MIT-friendliest organisation on these shelves came
back ungranted.** An organisation's licence posture is not inherited by its
repositories. "They're the Kolibri people" is not a licence.

**A scope concern raised and refuted.** `learningequality/studio`
([repo](https://github.com/learningequality/studio), already on these shelves)
declares `Copyright (c) 2021 Foundation for Learning Equality (internal apps)`.
A parenthetical qualifier inside a copyright line is exactly the shape this KB
treats as a possible narrowed grant. **Full text read this pass: the permission
body is standard, unmodified MIT with no field-of-use restriction.** The
parenthetical annotates the holder, not the grant. **Full MIT** — recorded so the
next pass does not re-litigate it.

### Why these two shelves belong on the same page

Morango answers *how the data gets there* when connectivity is intermittent. The
LTI/OneRoster tier answers *how it gets into the systems the client already runs*,
against a rubric that scores exactly that. Together they are the two ends of a
delivery that an RFP can actually score — and both ends are permissive, which is
the whole reason this file exists.

## Added in the eleventh pass of 2026-10-06 — the evaluation layer, and the Python protocol layer

Licences read from each repository's own payload on `raw.githubusercontent.com` on
2026-10-06; metadata (stars, forks, `default_branch`, `fork`, `pushed_at`) from the
GitHub REST search API, reachable this pass through the session's GitHub MCP server.

**All four rows are reinstatements of addresses this repository's own reset dropped
earlier the same day** — they are in `archive/2026-10-06-pre-reset/`. See
`repos/trending.md` for the 172-address audit.

### The evaluation layer — the one infrastructure tier this KB had been describing as missing

| Repo | Licence (read from payload) | ★ (2026-10-06) | Forks | Why it is foundational |
|---|---|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | **MIT** (`main/LICENSE`) | **2,945** | 779 | **Inspect**, from the **UK AI Security Institute**. A general LLM-evaluation framework: datasets → solvers → scorers, with model-graded evals, tool use and multi-turn dialog built in, and third-party Python packages able to add scoring and elicitation techniques. **This is the harness.** An education engagement supplies the dataset and the rubric; it should not supply the runner, the logging, the sandboxing or the scoring plumbing. Pushed on the day of this pass. |
| [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | **Apache-2.0** (`main/LICENSE.md`) | 355 | 72 | **Moonshot**, from the **AI Verify Foundation** (Singapore IMDA's AI-testing community). Benchmarking **and red-teaming** of any LLM application in one modular tool. The red-team half has no permissive equivalent in this KB, and for an education deployment — where the adversary is a bored fifteen-year-old with unlimited attempts — it is not optional. Pushed on the day of this pass. |

**Why both, rather than one.** Inspect measures whether the system is *right*;
Moonshot measures whether it can be made to *misbehave*. Education buyers in every
region this KB tracks now ask for both, and the two licences (MIT and Apache-2.0) are
compatible with each other and with a commercial deliverable. **Neither ships any
education content** — which is exactly why they are in `foundations.md` and the
benchmarks are not.

### The protocol layer — Python

| Repo | Licence (read from payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (`master/LICENSE`, 1,070 B) | **138** | `master` | `PyLTI1p3` — **LTI 1.3 Advantage** tool implementation with Django and Flask adapters. Most AI tutoring code in this KB is Python, and LTI 1.3 is how it reaches a learner inside an institution's LMS. ⚠️ **Last push 2024-08-18**: treat as a stable protocol library, pin the version, and budget for maintaining your own fork if the spec moves. |
| [Pearson-Advance/openedx-lti-tool-plugin](https://github.com/Pearson-Advance/openedx-lti-tool-plugin) | **Apache-2.0** (`main/LICENSE`) | 5 | `main` | Makes an **Open edX** instance act as an LTI 1.3 *tool*, so an existing Open edX estate can be consumed by another institution's LMS rather than replaced. Pushed 2026-09-11. |

### A probe-set correction that belongs in this file

Every licence in `foundations.md` is read from a payload URL, and a payload URL needs
a branch. The tenth pass probed `main` and `master`. **Read `default_branch` from the
API instead**: this pass found a 2,320★ platform on `dev` (`learnhouse`), a 718★
platform on `2.12` (`portabilis/i-educar`) and one repository on
`deployment/playstore`. On a `main`+`master` probe all three read as **ungranted**,
and two of them are merely **copyleft** — a delivery constraint, not an absence.

## Added in the twelfth pass of 2026-10-06 — the xAPI/LRS tier, the Ed-Fi stack, and the Apache-2.0 seam inside an AGPL platform

Every branch below came from `git ls-remote --symref … HEAD` and every licence from the
`raw.githubusercontent.com` payload on that branch, on 2026-10-06. No licence here was
taken from a sidebar, a badge or an organisation-level assumption — the
`aiverify-foundation` rows are the reason why: two repositories in that organisation are
Apache-2.0 and a third, in the same org, carries no licence at all.

### The row that changes platform strategy — Open edX's plugin SDK is Apache-2.0

| Repo | Licence (payload) | ★ | Branch | Why it is foundational |
|---|---|---|---|---|
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** (`master/`**`LICENSE.TXT`**) | **470** | `master` | The **XBlock SDK** — the component and plugin API every Open edX course component is written against. Python. |

**This matters out of proportion to the row.** Open edX's platform core
(`openedx/edx-platform`) is **AGPL-3.0**, and this KB has correctly priced the platform
as copyleft since its first pass. But the surface a studio actually writes on — a
client-specific interactive component, an AI tutor delivered inside a course, a
proctoring or analytics side-car — is an **XBlock**, and the XBlock SDK is
**Apache-2.0**. A component built against it is **your** component: Globant can build,
keep and redistribute it without inheriting the platform's AGPL obligations, provided it
stays a plugin and is not linked into the platform tree. The LATAM `TutorIA`
specification already on this KB's agent shelf specifies exactly this shape — *"delivered
as an Open edX XBlock/plugin"* — and this row is the licence evidence that the shape is
sound.

⚠️ **The boundary is the deliverable, not the repository.** AGPL-3.0 reaches anything
that becomes part of the platform process in a way that creates a derivative work; it
does not reach a separately licensed plugin consumed through a published plugin API. Get
the packaging reviewed before you promise a client a proprietary component — the
distinction is the whole engagement, and it is a legal review, not a licence-file read.

*Found at `LICENSE.TXT` — uppercase extension. A nine-name lowercase probe reports this
repository as ungranted; see the 13th failure mode in `agents/top.md`.*

### The xAPI / LRS tier — the learning-analytics half, recovered

The eleventh pass declared the learning-analytics side of the interoperability tier
behind a membership, on the evidence of Caliper. **That is true of Caliper and false of
xAPI.** xAPI's tooling is permissive and alive:

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [adlnet/lrs-conformance-test-suite](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** (`master/LICENSE`) | **77** (52 forks) | `master` | **The conformance instrument.** Node.js suite that tests an LRS against the **MUST** requirements of the xAPI specification. From **ADL** (Advanced Distributed Learning, the US Department of Defense initiative that authored xAPI). This is how you *prove* an analytics deliverable conforms rather than asserting it — and in a procurement where interoperability is a scored line item (trend 28), a conformance run is the evidence. |
| [adlnet/xapi-profiles](https://github.com/adlnet/xapi-profiles) | **Apache-2.0** (`master/LICENSE`) | **60** (33 forks) | `master` | The **xAPI Profiles specification** — structure, communication and processing — plus context, library and ontology files. ADL also runs a public profile index at `xapi.vocab.pub`. The vocabulary layer: what a statement *means*, not just how it is transported. |
| [yetanalytics/xapipe](https://github.com/yetanalytics/xapipe) | **Apache-2.0** (`main/LICENSE`) | 17 (9 forks) | `main` | **LRSPipe** — xAPI statement forwarding and middleware, governed directly by xAPI Profiles. Clojure. ⚠️ **The product name is not the repository name**: `yetanalytics/lrspipe` is a 404 and this KB recorded that false negative twice. Pin the address, not the brand. |
| [pelotech/xapi-lrs](https://github.com/pelotech/xapi-lrs) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | An LRS implementation. The store at the end of the pipe. |

**What this adds up to:** a permissive xAPI chain exists end to end — **profile**
(vocabulary) → **pipe** (transport and transformation) → **LRS** (store) →
**conformance suite** (proof). All four are MIT or Apache-2.0. An analytics deliverable
can be built, kept and redistributed by Globant on this chain. **Caliper cannot be, and
xAPI can** — and the two standards are not interchangeable, so this is a design decision
to make at proposal time, with the licence as one of the inputs.

### The Apereo learning-analytics tier — permissive, under a licence the filter misses, and dormant

| Repo | Licence (payload) | ★ | Branch | State |
|---|---|---|---|---|
| [Apereo-Learning-Analytics-Initiative/OpenLRS](https://github.com/Apereo-Learning-Analytics-Initiative/OpenLRS) | **ECL-2.0** (`master/LICENSE`) | 47 (38 forks) | `master` | 🔴 **Archived by the owner on 2019-01-31, read-only.** Superseded by OpenLRW; the README says all new development moved there. |
| [Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor](https://github.com/Apereo-Learning-Analytics-Initiative/LearningAnalyticsProcessor) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |
| [Apereo-Learning-Analytics-Initiative/OpenDashboard-api](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-api) | **ECL-2.0** (`master/LICENSE`) | not read this pass | `master` | Dormant. |

🆕 **ECL-2.0 is the Educational Community License 2.0, and it belongs in this KB's
permissive set.** It is **OSI-approved** and it is **Apache-2.0 with one modification**:
the patent grant is narrowed so that a contributing university licenses patents only for
the contributed work, not across its whole portfolio — written precisely so that
universities could contribute to open source without their technology-transfer offices
blocking it. For redistribution and commercial use it behaves like Apache-2.0.

**This is trend 15 — "permissive is a bigger set than MIT, Apache, BSD" — with the
education sector's own licence as the example.** A `license:mit OR license:apache-2.0`
filter rejects the entire Apereo estate, and Apereo is the consortium behind Sakai and
much of higher education's shared infrastructure. **Add `ECL-2.0` to the permissive
allow-list.**

⚠️ **And then do not adopt these three anyway.** The licence is fine; the code has been
read-only since January 2019. They are a **reference architecture and a vocabulary
source**, and the live permissive alternative is the ADL/Yet Analytics xAPI chain above.
The useful lesson is the licence, not the repositories.

### The Ed-Fi stack — Apache-2.0, and the US K-12 data standard

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) | **Apache-2.0** (`v6.2.0/LICENSE`) | 46 (13 forks) | 🆕 **`v6.2.0`** | The **Ed-Fi Data Standard** — the schema that enables interoperability among US K-12 education data systems. Latest release v6.2.0, which is also the default branch. |
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | **OneRoster** over Ed-Fi — rostering interoperability, the 1EdTech standard that *did* stay open. |
| [Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-Clever-Integration) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Integration with **Clever**, the rostering provider most US districts actually run. The bridge between the standard and the installed base. |

**Why this is the North America procurement asset.** US K-12 procurement increasingly
scores interoperability directly (trend 26, trend 28), and Ed-Fi is the standard those
rubrics name. The schema, the OneRoster bridge and the Clever integration are all
**Apache-2.0**. ⚠️ **The MCP side-car is gone**: `Ed-Fi-Alliance-OSS/Ed-Fi-SDK-MCP` is
recorded in this repository's archive and no longer resolves. Agent access to Ed-Fi over
MCP is a **build**, and it is a well-shaped, small one — the schema is published and
permissive.

*The default branch here is `v6.2.0`. This is the cleanest example in the KB of why the
branch must be read rather than guessed: the Apache-2.0 licence of the US K-12 data
standard is invisible to a `main`+`master` probe.*

### The interoperability tier — Python and Java LTI 1.3, measured exhaustively

The tenth pass declared *"no Python LTI 1.3 library exists on the permissive shelf"*;
the eleventh pass refuted it from this repository's own archive. This pass **measured the
whole tier** with the MCP search API — `lti 1.3 advantage language:Python` →
**`total_count: 4`**, which is the complete set, not a page of it:

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **MIT** (1,070 B) | **138** (83 forks) | `master` | **The only viable one.** Django and Flask adapters. ⚠️ **51 open issues**, last push 2024-08-18. |
| [blackboard/BBDN-lti-1p3-tool-example](https://github.com/blackboard/BBDN-lti-1p3-tool-example) | **Apache-2.0** (`main/LICENSE`) | 1 | `main` | 🆕 **Blackboard's own** Python/Flask LTI 1.3 example with AWS deployment. A vendor-authored reference — useful for reading how a major LMS expects a tool to behave. Last updated 2022. |
| [glenn-watt/lti-1p3-reference-tool](https://github.com/glenn-watt/lti-1p3-reference-tool) | **MIT** (`main/LICENSE`) | 0 | `main` | 🆕 Flask reference tool implementing **OIDC, JWKS validation, AGS, NRPS and Deep Linking from first principles**. 0★ and three months old, so it is **code to read**, not a dependency — but it is the only one that covers all four LTI Advantage services explicitly. |
| [CNIT-Organization/ltitoolkit](https://github.com/CNIT-Organization/ltitoolkit) | **MIT** (`main/LICENSE`) | 0 | `main` | 🆕 PyPI-published LTI 1.3 Advantage toolkit. 0★. |

🔴 **The Python-shaped hole in trend 28 is one library deep, and this is the exact
measurement of it.** Four repositories exist in the world; one has more than one star;
that one has 51 open issues and has not been pushed since August 2024. **If an
engagement's LMS integration is on the critical path, budget for maintaining a fork of
`pylti1.3` from the start.** That is not a risk to flag later — at `total_count: 4` it is
the baseline condition of the tier.

**The Java side is healthier, and it is EMEA-placed:**

| Repo | Licence (payload) | ★ | Branch | Verdict |
|---|---|---|---|---|
| [UOC/java-lti-1.3-provider-example](https://github.com/UOC/java-lti-1.3-provider-example) | **MIT** (`master/LICENSE`) | 8 (12 forks) | `master` | **EMEA / Spain** — a working LTI Advantage tool webapp built on the LTI libraries of the **Universitat Oberta de Catalunya**, a large European distance-learning university. The Java counterpart to `pylti1.3`, carrying a European institution's own production lineage. |

### The assessment-standards tier — QTI, and an ISC licence from a commercial vendor

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [pie-framework/pie-qti](https://github.com/pie-framework/pie-qti) | 🆕 **ISC** (`master/LICENSE`, © 2026 **Renaissance Learning**) | 4 (1 fork) | `master` | **QTI player for 2.1, 2.2 and 3.0**, plus bidirectional QTI ↔ PIE transforms with a CLI for batch conversion. Ships an item player and a multi-item assessment player. TypeScript. |
| [Citolab/qti-convert](https://github.com/Citolab/qti-convert) | **GPL-3.0** (`main/LICENSE`) | not read this pass | `main` | QTI conversion tooling from **Cito** (the Dutch national assessment institute). Real and maintained — but GPL-3.0, so a conversion step built on it is a copyleft deliverable. |

🆕 **ISC belongs on the permissive allow-list too.** It is OSI-approved and functionally
equivalent to MIT — a two-clause permission grant with no added conditions — just shorter.
A `license:mit OR license:apache-2.0 OR license:bsd` filter misses it.

**And note who holds the copyright: Renaissance Learning**, a commercial assessment
vendor, publishing a QTI player under ISC. Trend 7 has called assessment "the regulated
frontier and the tooling gap" for eleven passes. The gap is narrower than that on the
**standards-conformance** side: a permissive QTI player exists, at 4★, from a vendor
with a real assessment business. It is still wide on **AI-generated grading**, where
`license:apache-2.0` + automated rubric grading measures **`total_count: 0`** this pass
and the only permissive answer in this KB remains `Selleo/mentingo` (MIT).

### Classroom-discourse and research infrastructure

| Repo | Licence (payload) | ★ | Branch | What it gives you |
|---|---|---|---|---|
| [stanfordnlp/edu-convokit](https://github.com/stanfordnlp/edu-convokit) | **MIT** (`main/LICENSE`) | 117 (16 forks) | `main` | Stanford NLP: anonymise → annotate → analyse classroom talk. Full entry in `agents/top.md`. |
| [EduNLP/EduCoder](https://github.com/EduNLP/EduCoder) | **MIT** (`main/LICENSE`) | 3 | `main` | Human-vs-LLM transcript annotation workspace. Full entry in `agents/top.md`. |
| [jupyterhub/jupyterhub-deploy-teaching](https://github.com/jupyterhub/jupyterhub-deploy-teaching) | **BSD** (`master/LICENSE`) | not read this pass | `master` | 🆕 **Absent from every earlier pass of this KB**, live or archived, except one archive mention. Reference deployment of **JupyterHub for a teaching environment** — the standard way CS and data-science courses give every student a server-side notebook. BSD. The infrastructure layer under any coding-course engagement. |
| [aiverify-foundation/aiverify](https://github.com/aiverify-foundation/aiverify) | **Apache-2.0** (`main/LICENSE`) | 98 (32 forks) | `main` | **APAC / Singapore** — AI governance *testing framework* from the **AI Verify Foundation** under **IMDA**, validating AI systems against internationally recognised principles through standardised tests. The compliance-evidence instrument for an APAC deployment, built by the regulator's own foundation. |
| [aiverify-foundation/aiverify-developer-tools](https://github.com/aiverify-foundation/aiverify-developer-tools) | **Apache-2.0** (`main/LICENSE`) | not read this pass | `main` | Plugin and test-widget development kit for AI Verify. How you add an **education-specific** test to a government-recognised harness. |
| [aiverify-foundation/moonshot-data](https://github.com/aiverify-foundation/moonshot-data) | **Apache-2.0** (`main/LICENSE.md`) | not read this pass | `main` | Test assets, datasets, metrics and attack modules for Moonshot (the red-teaming/benchmark harness already on this shelf). |
| `aiverify-foundation/LLM-Evals-Catalogue` | 🔴 **ungranted** | — | `main` | **No licence file**, under 30+ name variants on the real default branch. A catalogue of LLM evaluations — the index, not the code. **Treat as reading material, cite it, do not vendor it.** Three repos in one government foundation's organisation: two Apache-2.0, one ungranted. |

### One correction to this KB, with the payload as evidence

The 123rd-pass note in `repos/trending.md` records:

> *"Discrepancia registrada sin normalizar: el `LICENSE` de `edrys` mide 16.724 B y la
> AGPL íntegra mide ~34–35 KB en este corpus — es AGPL ABREVIADA."*

🔴 **`edrys-org/edrys` is `MPL-2.0`, not an abbreviated AGPL.** Read this pass from
`main/LICENSE` (16,725 B): the first line is **`Mozilla Public License Version 2.0`**,
and the full MPL-2.0 text is ~16.7 KB — the size is not a truncated AGPL, it is a
complete MPL. The only occurrence of "Affero" in the file is inside **MPL §1.12's
secondary-licence definition**, which names the LGPL and AGPL as compatible licences.
That boilerplate is what a substring search found.

**This changes the delivery constraint, not just the label.** MPL-2.0 is **file-level
weak copyleft**: modified MPL files must stay MPL and be published, but the work can be
combined with proprietary code in a larger program without that program becoming MPL.
AGPL would have added a network-use obligation that MPL has none of. `edrys` — a
live-classroom platform — is therefore **usable in a mixed-licence deliverable** with
per-file discipline on the files you touch. It was priced as unusable.

**The method lesson is the general one:** a size comparison identifies a *discrepancy*,
and only the first line of the payload identifies a *licence*. Size told pass 123 to look
again, which was right; it then answered the question it had only raised.

## Added in the thirteenth pass of 2026-10-06

One row, and it is on this shelf rather than the education shelf for a reason.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [bonafe/inteligencia-aberta](https://github.com/bonafe/inteligencia-aberta) | **MIT** (`LICENSE`) | reference architecture | **Not education software.** A Brazilian civic-analysis agent platform (Bonafé · Américo, 2★, Python) whose *stack* is the one this KB keeps assembling by hand for a sovereign deployment: **FastAPI + LangGraph + PostgreSQL + Qdrant, in Docker, multi-tenant, deployable locally and federating across machines**. Read it as a **worked reference for the LATAM sovereign pattern**, not as a component to ship. Its design goals — end-to-end source traceability, user control over what is shared, voice and natural-language access for low-literacy users — are the same requirements an education deployment under LATAM constraints carries, written out by someone who shipped them. |

### Why a 2★ repository is worth a row

Because this shelf's job is to answer *"what do we build on"*, and the scarce thing in a
sovereign education build is not a component — every component here is permissive and
available — it is a **worked wiring of them that someone has already debugged**. This KB
has four patterns (P4, P5, P26, P32) that specify a LATAM or data-residency stack
component by component. `inteligencia-aberta` is an independent implementation of
substantially that stack, by Brazilian authors, under MIT, with the traceability
requirement treated as a first-class design goal rather than an afterthought.

⚠️ **The star count is the correct signal to ignore here, and the fork count is the one to
watch.** It has **2 stars and 0 forks** — nobody has deployed it. Use it as a design
reference and a code read; do not present it to a client as a maintained dependency.

### What this pass did not add, and why

🔴 **No new serving, orchestration or retrieval layer was found.** The mandatory
infrastructure query (`open source platform education ERP CRM MIT Apache`) returned
**OpenEduCat, RosarioSIS, openSIS, Gibbon and Fedena** — *five returned, five already
inventoried on the SIS/ERP shelf in `verticals/solutions.md`*. That is the **fourteenth
consecutive pass** in which the generalist infrastructure query has returned zero new
rows, and it is now safe to say what that means: **the foundational layer for an education
build is saturated and stable.** The scarcity has moved entirely to the education-specific
layer above it, which is where the last several passes have correctly been spending their
probes.

🔴 **The non-GitHub forge channel could not be opened.** `codeberg.org`, `gitee.com` and
the European Commission's Joinup/OSOR catalogue are all **unreachable from this
environment** (403 at the egress proxy). Every licence fact on this shelf rests on
`raw.githubusercontent.com`, which is the only code-hosting payload this environment can
read. Two named Codeberg education projects were surfaced and **deliberately not shelved**,
because they could not be payload-verified. Full measurement in `agents/trending.md`,
Finding 4.

## Added in the fourteenth pass of 2026-10-06 — the sandbox layer, and the index that is not a shelf

One infrastructure row, and it is the highest-starred find of the whole pass. It arrived
through the platform-name channel (`agents/trending.md`, fourteenth pass) as a by-product:
searching for education platform integrations surfaced the layer underneath the one thing
education software does that no other industry's software does — **run a student's code**.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [taybenlor/runno](https://github.com/taybenlor/runno) | **MIT** (`LICENSE`, 1,106 B; © Benjamin Taylor) | code sandbox | **773★.** Runs code in many languages inside a **WebAssembly/WASI sandbox** — in the browser with no server, or in Node. Four published packages, all **MIT on npm**: `@runno/runtime` 0.10.0 (web components for runnable examples), `@runno/sandbox` 0.10.2 (secure sandbox for Node and other JS runtimes), `@runno/wasi` 0.10.0 (isomorphic WASI runner) and 🆕 **`@runno/mcp` 0.10.6 — the sandbox exposed as an MCP server**. |

### Why this is a foundations row and not a curiosity

Every CS-education pattern in this KB has had the same unsolved component: **where does the
student's code run?** The existing answers on this shelf are JupyterHub (a multi-user server
per cohort) and OpenHands (a coding agent with its own sandbox). Both are servers you operate.

Runno moves execution **into the learner's browser**, which changes three things an education
engagement is costed and audited on:

- **Data residency becomes trivial for the execution step.** Student code never reaches a
  server, so there is no execution-side transfer to document in an EMEA deployment. The
  sovereignty argument this KB makes with Ollama for inference, Runno makes for execution.
- **Per-seat cost goes to zero and scales with the cohort's own devices.** No container per
  student, no idle notebook servers — the LATAM and offline-first cost constraints in P5
  apply to execution too, and this is the component that answers them.
- 🆕 **`@runno/mcp` makes the sandbox agent-callable**, which is the piece that was missing:
  a tutor agent can now *execute* a learner's submission and reason about the actual output
  rather than predicting it. Pair it with the auto-grading assets in `agents/top.md`
  (fourteenth pass) and the grading loop has a real execution step under a permissive licence.

⚠️ **Two limits to state before it enters a proposal.** WASI sandboxing covers languages
with a WASI target — check the language a client's curriculum actually teaches against the
published package list rather than assuming coverage. And a browser sandbox is **not** an
anti-cheat boundary: it protects the host from the code, not the assessment from the student.
For proctored assessment the execution still belongs server-side.

### The MCP Registry — an index this KB now uses, and what it is not

`registry.modelcontextprotocol.io` is reachable here and was measured first-hand this pass
(method, traps and counts in `repos/trending.md`, fourteenth pass). It belongs on this page
only as a **channel**, never as a dependency:

- **11,505 unique servers** across 31,300 version rows — a record is not a server, and the
  figure is a **floor** because the page loop ended early.
- **102 education-vocabulary servers, of which 71 (70%) ship no source repository.** It is a
  catalogue of hosted endpoints with open-source entries mixed in, not a source shelf.
- 🔴 Its `?q=` parameter returns **HTTP 200 and the unfiltered page** — a silent no-op. Do
  not quote a count from it.
- 🔴 One listed server's repository **no longer exists**. A registry entry is not an
  existence proof; `ls-remote` still is.

**The rule for this page:** the registry is a good place to *find* candidates and a
disqualifying place to *source* them. Nothing enters this shelf from a registry listing
without an `ls-remote` resolution and a licence payload on its real default branch.

## Added in the fifteenth pass of 2026-10-06 — the SIS/MIS client layer, and why it belongs in *this* file

The assets found this pass are not education products and they are not agents. They are the
**client libraries that speak a student information system's protocol** — the layer an
education agent stands on when the engagement is administrative rather than instructional.
Full rows, stars and country placement in `agents/top.md` (fifteenth pass). This file records
what they are *for*, and the two things that decide whether you may use them.

Licences read from each repository's own payload on 2026-10-06; default branches confirmed
with `ls-remote --symref`.

### The layer, by protocol family

| Repo | Licence (payload) | Language | Speaks to |
|---|---|---|---|
| [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** | Python | PRONOTE (FR) |
| [`python-webuntis/python-webuntis`](https://github.com/python-webuntis/python-webuntis) | **BSD-2-Clause** | Python | WebUntis (DE/AT) |
| [`aydenp/PowerSchool-API`](https://github.com/aydenp/PowerSchool-API) | **MIT** | Node.js | PowerSchool (US) |
| [`dougpenny/PyPowerSchool`](https://github.com/dougpenny/PyPowerSchool) | **MIT** | Python | PowerSchool (US) |
| [`grantholle/powerschool-api`](https://github.com/grantholle/powerschool-api) | **MIT** | PHP | PowerSchool (US) |
| [`magister-api/magister`](https://github.com/magister-api/magister) | **MIT** | PHP | Magister 6 (NL) |
| [`elisaado/somtoday.js`](https://github.com/elisaado/somtoday.js) | **MIT** | TypeScript | SOMtoday (NL) |
| [`ivmelo/suap-api-php`](https://github.com/ivmelo/suap-api-php) | **MIT** | PHP | SUAP (BR) |
| [`Projeto-SIAC/suap-wrapper`](https://github.com/Projeto-SIAC/suap-wrapper) | **MIT** | Node.js | SUAP (BR) |
| [`PucaVaz/sigaa-tools`](https://github.com/PucaVaz/sigaa-tools) | **MIT** | Python | SIGAA (BR) |
| [`untisapi/untis4j`](https://github.com/untisapi/untis4j) | ⚠️ **LGPL-3.0** | Java | WebUntis (DE/AT) |
| [`shinyquagsire23/InfiniteCampusAPI`](https://github.com/shinyquagsire23/InfiniteCampusAPI) | ⚠️ **WTFPL v2** | Java | Infinite Campus (US) |

🟢 **Ten of the twelve are MIT or BSD, and together they cover six countries in four
protocol families.** Measured by *placed* permissive infrastructure, this is the broadest
single shelf this KB has added in one pass.

### ⚠️ Two warnings, and the second one is the reason this shelf is not a green light

**1. The licence is not the binding constraint here. The vendor's Terms of Use is.**

Every library above talks to a **proprietary, closed SIS**. The MIT grant covers the client
code; it says nothing about whether you may call the endpoint. The tier documents this
itself — `GeovaneSchmitz/sigaa-api` describes itself as *"uma biblioteca de **Web
Scraping**"*, `kc0506/ntucool` as *"**unofficial** … use it at your own risk"*, and
`chrischall/infinitecampus-mcp` quotes Infinite Campus's ToU forbidding access *"by any
means other than our publicly supported interfaces (for example, scraping or using the
content to train artificial intelligence software)"* before stating that it does exactly
that. Full treatment in `agents/top.md`, Finding 2; the gate that operationalises it is
**P26** in `compose/patterns.md`.

🔵 **The practical rule: these libraries are excellent for a prototype, a migration, or a
one-off data rescue the institution itself authorises — and they are not a production
integration path unless the institution holds an API agreement with its vendor.** When it
does, the same libraries become legitimate, because the institution's own credentials and
contract cover the access. **The asset is fine. The access needs paperwork.**

**2. Three licence shapes on this shelf would fail an automated allowlist, two of them
wrongly.**

- ⚠️ **`WTFPL v2`** (`shinyquagsire23/InfiniteCampusAPI`, 474 B payload, Sam Hocevar
  copyright) — maximally permissive in effect, **not OSI-approved**, and rejected by name by
  many corporate allowlists. Usable in substance; expect to justify it, and expect some
  clients to refuse it on the name alone.
- ⚠️ **`LGPL-3.0`** (`untisapi/untis4j`) — the middle path this KB already documents for
  OpenEduCat: dynamic linking keeps your code yours, modifications to the library itself must
  be published.
- 🔴 **`CC BY-NC-SA 4.0`** (`Jona-Zwetsloot/Somtoday-Mod`) — **NonCommercial. Not usable in
  client work at all**, and a content licence applied to software besides.

⚠️ **And read these families with the shared classifier, not a fresh one.** This pass's
from-scratch probe script mislabelled four payloads on this shelf as
Creative Commons/NonCommercial — three GPL-3.0 and one AGPL-3.0 — because GPL-3.0 §6 contains
the word *"noncommercially"*. 🟢 **`compose/code/lib/license_family.sh` already gets all of
them right**, because it gates the Creative Commons branch on a CC marker before reading
NonCommercial as an attribute. **Source the library.** See `agents/top.md`, method note 2.

### The costliest absences on this shelf

| Repo | ★ | Why it matters |
|---|---|---|
| [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **214** | The JavaScript WebUntis client, highest-starred ungranted asset in the tier. 6 filenames probed on `master`: **nothing**. |
| [`Litarvan/pronote-api`](https://github.com/Litarvan/pronote-api) | 192 | The multi-language PRONOTE API. **Ungranted.** `pronotepy` (MIT, 241★) is the answer for Python. |
| [`IFRN/suapi`](https://github.com/IFRN/suapi) | 28 | ⚠️ Published by the **federal institute that operates SUAP** — and ungranted, while an individual's client is MIT. One file, one commit, a public institution: **the most answerable upstream ask in this pass.** |
| [`NCSIS/InfiniteCampus-Vendor-Integration`](https://github.com/NCSIS/InfiniteCampus-Vendor-Integration) | 13 | Vendor-integration PowerShell, ungranted. |

🔵 **Pattern across all four: the ungranted assets cluster at the *most useful* layer** — the
general-purpose client and the official-institution publication — while the permissive ones
are language-specific ports and student tools. The same shape this KB recorded in the Canvas
MCP cluster, now reproduced in a completely different tier.

### What this adds to the architecture menu

The interoperability tier added in the tenth pass (OneRoster, Ed-Fi, xAPI/LRS) and this
client layer answer the **same** question by **different** routes, and the difference is
entirely about who authorised the access:

| Route | Grant on the code | Grant on the data | Use it for |
|---|---|---|---|
| **Official API** (OneRoster / Ed-Fi, permissive implementations already shelved) | permissive | **the institution's contract with its vendor** | 🟢 production |
| **SIS client library** (this shelf) | permissive (10 of 12) | ⚠️ **none — often contrary to vendor ToU** | prototype, migration, authorised rescue |

🟢 **Read together, they are the strongest architectural recommendation this KB can make for
an administrative engagement: prototype on the client library to prove the workflow in days,
then ship on the official API path.** The prototype is cheap and the production path is
contractual, and conflating them is how an engagement discovers in month three that its
integration was never licensable.

---

## Added in the sixteenth pass of 2026-10-06 — the national curriculum tier, and a licence family this KB had no row for

The ministry channel (`repos/trending.md`, sixteenth pass) produced an infrastructure tier this
KB has described as *assumed* in two patterns and never shelved: **the national curriculum, as
a machine-readable service, with a written commercial grant.**

### The curriculum-data tier

| Repo | Branch | Licence (read from payload) | Bytes | What it gives you |
|---|---|---|---|---|
| [`Utdanningsdirektoratet/Grep_SPARQL`](https://github.com/Utdanningsdirektoratet/Grep_SPARQL) | `main` | 🟢 **NLOD** (`LICENSE.md`) — **commercial use granted in writing** | 1,783 | Norway's national curriculum (**LK20**) as **queryable RDF over a SPARQL endpoint, in production since 7 Dec 2020**. Competence aims, subjects, programmes, cross-curricular topics — addressable, not scraped. |
| [`Utdanningsdirektoratet/KL06-LK20-public`](https://github.com/Utdanningsdirektoratet/KL06-LK20-public) | `master` | 🔴 **NO-PAYLOAD** (30+ filename variants) | 0 | Documentation of the revised **Grep-data interface** for the LK20 reform, plus example files. The live service's own docs are in the repo wiki. |
| [`fnshr/kyo-kan`](https://github.com/fnshr/kyo-kan) | `master` | 🟢 **CC0-1.0** | 6,555 | Japan's **MEXT official kanji-by-grade tables** (*gakunenbetsu kanji haitōhyō*) as structured open data. Small, and the only MEXT-derived asset found. |
| [`NKAmapper/school2osm`](https://github.com/NKAmapper/school2osm) | `master` | 🟢 **CC0-1.0** | 6,555 | Extracts every school from Norway's **National School Register (NSR)**. An institution roster, free of restriction. |

### The education-microdata tier (LATAM)

| Repo | Branch | Licence (read from payload) | ★ | What it gives you |
|---|---|---|---|---|
| [`SidneyBissoli/educabR`](https://github.com/SidneyBissoli/educabR) | `main` | 🟢 **MIT** — ⚠️ declared in **`DESCRIPTION`**, not `LICENSE` | 15 | **CRAN** package v1.2.0.9000. Download + process **INEP** microdata: Censo Escolar, ENEM, SAEB, Censo da Educação Superior, ENADE, ENCCEJA, IDD, CPC, IGC, CAPES, FUNDEB. **Eleven national instruments behind one MIT API.** |
| [`Mcp-Brasil/mcp-brasil`](https://github.com/Mcp-Brasil/mcp-brasil) | `main` | 🟢 **MIT** (1,072 B) | 1,805 | 70 Brazilian public APIs as MCP tools, 13 of them education. 🟢 **Canonical — identity settled in the seventeenth pass** (root-commit comparison; `dasgltd/mcp-brasil` is a 0★ fork of this address). |
| [`inepdadosabertos/api`](https://github.com/inepdadosabertos/api) | `master` | 🔴 **GPL-2.0** (18,025 B) | 45 | Civil-society open-data API over INEP. ⚠️ **Created 2014** — treat as reference, not as a dependency, and note it is *not* INEP's own. |
| [`lucasmation/microdadosBrasil`](https://github.com/lucasmation/microdadosBrasil) | `master` | 🔴 **NO-PAYLOAD** | 174 | Reads Brazilian public microdata (CENSO, PNAD). The most-starred of this group and the one you cannot use. |

### 🟢 NLOD belongs on this KB's permissive allow-list — in the data tier

The twelfth pass added **ECL-2.0** and **ISC** to the allow-list because the standard
"MIT/Apache/BSD" filter rejected two licences that are permissive in substance. **NLOD is the
same correction, one tier down: it governs data, not code.**

Quoted from the payload (the licence ships bilingually, Norwegian and English):

> *"You are allowed to copy and make available, change and/or merge data sets described here
> with other data sets, and **to use them for commercial purposes**."*

| NLOD condition | What it costs a Globant deliverable |
|---|---|
| Attribution in a prescribed string — *"Contains data under NLOD, made available on data.udir.no"* | 🟢 A footer line. |
| **The Udir logo may not be used** without a separate agreement | 🟢 Trivial — and a trap only if a designer drops a ministry crest into a client deck to imply endorsement. |
| Data must not be presented misleadingly, distorted or misrepresented | 🟢 Already required by the EU AI Act transparency duties this KB tracks. |
| No liability for errors in the data | ⚠️ Real: a curriculum-alignment claim you make is **yours**, not the ministry's. Budget a validation step. |
| **No share-alike. No non-commercial clause.** | 🟢 **This is the whole point.** The output is yours to license as you wish. |

⚠️ **Read the boundary precisely, because it is easy to overclaim.** NLOD grants the **data**.
`Grep_SPARQL` is *documentation of an endpoint* — there is no substantial codebase to vendor.
The SPARQL client, cache, mapping layer and item generator are yours to write or to take from
the permissive shelves above.

### The public-sector application tier — permissive, and read correctly

| Repo | Branch | Licence (read from payload) | What it is |
|---|---|---|---|
| [`Utdanningsdirektoratet/PAS2-Public`](https://github.com/Utdanningsdirektoratet/PAS2-Public) | `master` | 🟢 **Apache-2.0** (11,325 B) | The openly published portion of Norway's **national exam administration system**. A ministry's production exam code, patent-granted. |
| [`Utdanningsdirektoratet/designsystem`](https://github.com/Utdanningsdirektoratet/designsystem) | `main` | 🟢 **MIT** (1,079 B) | The directorate's design system, on top of `digdir/designsystemet`. Active 2026-10-02. **A government-grade accessible component set for education UIs.** |
| [`Utdanningsdirektoratet/xmldataimport`](https://github.com/Utdanningsdirektoratet/xmldataimport) | `master` | 🟢 **MIT** (1,079 B) | Loads XML test data into SQL Server for data-driven automated tests. |
| [`Utdanningsdirektoratet/PAS-scoop-public`](https://github.com/Utdanningsdirektoratet/PAS-scoop-public) | `master` | 🟢 **Apache-2.0** (11,357 B) | Scoop bucket for the PAS toolchain. |
| [`Utdanningsdirektoratet/VFKL`](https://github.com/Utdanningsdirektoratet/VFKL), `VFKL_rebase` | `main` | 🟢 **MIT** (1,063 B) | ⚠️ **Both archived**, and the copyright holder is **Altinn** (Norway's national digital platform), not Udir — a cross-agency reuse worth knowing about, and a holder-mismatch of the kind `p184` exists to catch. |
| [`Utdanningsdirektoratet/pifu`](https://github.com/Utdanningsdirektoratet/pifu) | `master` | 🔴 **NO-PAYLOAD** | **PIFU** — Norway's person-data/rostering flow spec for education. ⚠️ **The interoperability tier's Norwegian entry, and it is ungranted.** |

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

The tenth pass shelved the interoperability tier and the twelfth pass the xAPI/LRS tier, both
on the finding that **39% of district RFPs score interoperability**. Both shelves were built
from *vendor-neutral standards bodies*. This one is built from **a state**, and it answers a
question those could not:

🔵 **In Norway, "curriculum-aligned" is a verifiable claim rather than a marketing one** — there
is a government endpoint to align *against*, and a licence that lets you bill for the
alignment. In every other country this KB covers, P15 and P16 have had to **assume** such a
source exists. ⚠️ **The sixteenth pass measured that it usually does not:** France publishes
teachers' material and no ministry estate, Japan publishes PDFs plus a CC0 kanji table, the
Gulf publishes nothing findable. **Norway is the exception that shows what the other four are
missing** — and `P25` is written so the Norwegian case is the reference implementation and the
others are a documented substitution.

---

## Added in the seventeenth pass of 2026-10-06 — a national standard you can lift, and a national estate you cannot

The channel was the **ministry tier as `org:`**. Two agencies had an estate; they split along a
line that decides how each one enters an engagement.

### 🟢 The permissive row — a national interoperability standard, Apache-2.0

| Repository | Branch | Licence (payload-verified) | ★ | Why it belongs on this shelf |
|---|---|---|---|---|
| [`Skolverket/dnp-ss12000-reference-api`](https://github.com/Skolverket/dnp-ss12000-reference-api) | `main` | 🟢 **Apache-2.0** (`LICENSE`, 11,339 B, full text) | 5 | **Reference implementation of SS 12000**, the Swedish national standard for information exchange between school administration systems — published by the national agency itself, Java, permissive. 🟢 **The rostering/SIS-interop layer this KB has been missing a permissive entry for:** `p230-rostering-layer-axis` exists because every prior candidate on that layer was copyleft, vendor-hosted or ungranted. |

🔵 **Why one row matters more than its star count.** Everything else this KB shelves on the
student-data layer is either a *platform* (which you adopt whole) or a *client* for someone's
proprietary API. A **standard with a permissive reference implementation** is the third thing:
you can implement it, ship it inside a closed product, and the other end of the wire is a
national specification rather than a vendor's roadmap. ⚠️ **5★ is not a maturity signal here** —
a reference implementation of a national standard is used by integrators who do not star it.

### 🟡 The Finnish estate — nine of 188, read correctly, and shelved with a condition

**`org:Opetushallitus` has 188 public repositories, all live on the day they were read.** Nine
payloads read from the real default branch (**six are `master`**):

| Repository | Branch | Licence (payload-verified) | ★ | Layer it supplies |
|---|---|---|---|---|
| [`Opetushallitus/eperusteet`](https://github.com/Opetushallitus/eperusteet) | `master` | 🟡 **EUPL-1.1** (631 B) | 3 | **National core curriculum + qualifications** (ePerusteet). Finland's analogue of Norway's Grep. |
| [`Opetushallitus/koski`](https://github.com/Opetushallitus/koski) | `master` | 🟡 **EUPL-1.1** (653 B) | 23 | **National study records** — qualifications and study rights in one service. |
| [`Opetushallitus/aoe`](https://github.com/Opetushallitus/aoe) | `main` | 🟡 **EUPL-1.2** (303 B ×2, **in subdirectories**) | 0 | **National OER library** (`aoe.fi`), 6,829 commits. |
| [`Opetushallitus/ataru`](https://github.com/Opetushallitus/ataru) | `master` | 🟡 **EUPL-1.2** (295 B) | 11 | **Admissions application forms** — generic form generation. |
| [`Opetushallitus/organisaatio`](https://github.com/Opetushallitus/organisaatio) | `master` | 🟡 **EUPL-1.1** (631 B) | 4 | **Register of providers and institutions** — the join key for the rest. |
| [`Opetushallitus/oppijanumerorekisteri`](https://github.com/Opetushallitus/oppijanumerorekisteri) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **National learner identity** (learner-number registry). |
| [`Opetushallitus/ehoks`](https://github.com/Opetushallitus/ehoks) | `master` | 🟡 **EUPL-1.1** (631 B) | 1 | **Personal competence-development plans** (vocational). |
| [`Opetushallitus/suorituspalvelu`](https://github.com/Opetushallitus/suorituspalvelu) | `main` | 🟡 **EUPL-1.2** (652 B) | 0 | **Attainment service** (2025, newest). |
| [`Opetushallitus/valtionavustus`](https://github.com/Opetushallitus/valtionavustus) | `master` | 🟡 **EUPL-1.1** (652 B, **(c) 2026**) | 8 | **State-grant administration** for providers. |

🔴 **179 of the 188 are unread, not absent.** This table is a sample chosen by stars and by
domain relevance, and it should be read as such.

### ⚠️ The condition on the Finnish rows, stated once and precisely

**The EUPL is OSI-approved, so these are open source.** What makes them different from every
other row on this shelf is **where the copyleft reaches**:

| Question | Answer |
|---|---|
| May we read, study, run and modify it? | 🟢 Yes. |
| May we **call these services** from our own agent over their APIs? | 🟢 **Yes, and the licence is irrelevant to that** — calling is not distribution. |
| May we fork it into a **hosted** client product and keep our changes closed? | 🔴 **No.** EUPL Art. 1 assimilates *"communication to the public"* to distribution, so **SaaS delivery triggers the copyleft, AGPL-style**. |
| May the combined work be relicensed? | 🟡 **Yes — EUPL Art. 5 carries a compatibility list** (GPL-2.0/3.0, AGPL-3.0, LGPL, MPL-2.0, EPL, CeCILL, OSL). ⚠️ Compatible-licence terms *prevail on conflict*, and the EC's own discussion notes the SaaS obligation can be circumvented that way. **Do not build a commercial plan on that route without counsel.** |

🔵 **The shelving rule this produces:** the Finnish estate belongs on this shelf as a **domain
model and an integration target**, not as a starting codebase. It is the most complete public
description of how a national education system's data actually fits together — curriculum,
provider register, learner identity, study records, attainment, plans, grants — and reading it
is free of licence consequence. **Forking it into a hosted product is the one move that is not.**

### 🔴 And the instrument cannot see any of it

`grep -c -i eupl compose/code/lib/license_family.sh` → **0**. Traced through the code (it could
not be executed this pass), every payload above lands on `UNCLASSIFIED`: the EUPL ships as a
**300–650 B grant notice with no title block**, and the classifier is a title-block classifier by
design. 🟢 **Until a grant-notice anchor exists, these nine rows are the only EUPL rows this KB
can defend, because they were read by hand.** That work is instruction 1 for the next pass.


## Added in the eighteenth pass of 2026-10-06 — the certified assessment tier, and a national agency's metadata layer

**Channel new to this KB this pass: the standards-body conformance register** — searching by
**standard + conformance certification** rather than by topic, star count, funder or institution.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com`
on 2026-10-06. Star counts, where given, were read the same day via `WebFetch`; cells that say
*not read this pass* say so rather than carrying an inferred number.

### QTI 3 — assessment item delivery, and the first externally certified permissive asset in this KB

Trend 28 swept LTI 1.3, OneRoster and Caliper and recorded **QTI as "not swept"**. Swept now, and
it is the **best-served** standard on the permissive shelf, not the worst.

| Repo | Licence (read from payload) | ★ / forks | Why it matters for an education engagement |
|---|---|---|---|
| [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | **MIT** (`main/LICENSE`, © 2022-2024 Amp-up.io, LLC) | 30 / 6 | 100% JavaScript QTI 3 item player, **1EdTech Certified for QTI 3 Basic *and* Advanced "Delivery" conformance**. 🟢 The only asset in this KB that is **both permissive and third-party certified** — fork it, brand it, and the conformance claim in the bid is somebody else's audit, not your assertion |
| [`amp-up-io/qti3-item-player-vue3`](https://github.com/amp-up-io/qti3-item-player-vue3) | **MIT** (`main/LICENSE`, © 2024 Amp-up.io, LLC) | not read this pass | Vue 3 build of the same component. Use when the client front end is already Vue |
| [`longsightgroup/qti3`](https://github.com/longsightgroup/qti3) | **MIT** (`main/LICENSE.md`, © 2026 Longsight, Inc.) | 5 / 2 | TypeScript reference implementation — **667 commits, 12 npm packages**: parsing, validation, rendering, **scoring**, and **migration from QTI 1.2 / 2.x into QTI 3**. The migrator is the part nobody else ships, and legacy item banks are the reason most assessment projects stall |
| [`agencyenterprise/qti-3-player`](https://github.com/agencyenterprise/qti-3-player) | **MIT** (`main/LICENSE`, © 2026 AE Studio) | not read this pass | Framework-agnostic npm renderer with full response processing. The neutral option when the front-end framework is not yet chosen |
| [`metyatech/qti-html-renderer`](https://github.com/metyatech/qti-html-renderer) | **MIT** (`main/LICENSE`, © 2026 metyatech) | not read this pass | QTI 3.0 item HTML rendering utilities. Smallest surface of the five |

#### Two QTI assets that are **not** permissive — read this before the architecture, not after

| Repo | Licence (read from payload) | The constraint |
|---|---|---|
| [`Citolab/qti-components`](https://github.com/Citolab/qti-components) | **GPL-3.0** (`main/LICENSE.md`) | 19★ / 10 forks, **2,456 commits** — the most mature renderer here, and copyleft. Citolab is the software lab attached to **Cito**, the Netherlands' national assessment institute. ⚠️ Its README states: *"the licensing is GPLv3 — if you want to use it in another way, feel free to ask!"* The **payload is GPL-3.0** and the **holder advertises negotiability**. That is an *invitation to dual-license*, it is invisible to any payload-reading classifier, and it is a **conversation to have before you design around the licence**. See trends §43 |
| [`oat-sa/qti-sdk`](https://github.com/oat-sa/qti-sdk) | **GPL-2.0** (`master/LICENSE`) | PHP SDK from the TAO assessment platform. **GPL-2.0, not 3.0** — so it is **not licence-compatible with GPL-3.0-only code**. Same trap as `francoisjacquet/rosariosis` in `verticals/solutions.md`. Check before combining |

🔴 **And one fork that nearly entered this shelf as a public-body asset.**
[`Kennisnet/qti-components`](https://github.com/Kennisnet/qti-components) (1★, 0 forks) is **forked
from `Citolab/qti-components`** — identical root commit `de8b27b`, **2,377 commits against
upstream's 2,456, so 79 behind**. Caught by running `git clone --filter=blob:none --no-checkout`
**before the row was written**. Pin the Citolab address; do not cite the Kennisnet one.

### Kennisnet — the Dutch national education-ICT agency, metadata and vocabulary layer

**[Stichting Kennisnet](https://github.com/Kennisnet)**, the Netherlands' public agency for ICT in
education, publishes **29 repositories**. Nine probed this pass: **6 MIT, 1 GPL-3.0** (the stale
fork above), **2 NO-PAYLOAD**. These are the layer an AI content pipeline needs and that nobody
should write twice.

| Repo | Licence (read from payload) | Layer | Why it matters for an education engagement |
|---|---|---|---|
| [`Kennisnet/pylom`](https://github.com/Kennisnet/pylom) | **MIT** (`master/LICENSE`, © 2017 Kennisnet) | metadata — **Python** | Reads and writes **IMS-LOM** learning-object metadata records. 🟢 **A permissive Python library for an education standard** — see the correction to trend 28 below |
| [`Kennisnet/py-eduterm-client`](https://github.com/Kennisnet/py-eduterm-client) | **MIT** (`master/LICENSE`, © 2018 Kennisnet) | curriculum vocabulary — **Python** | Client for **Eduterm**, the Dutch curriculum-vocabulary service. The curriculum-alignment tool call of P29, already written, in the language the agents are written in |
| [`Kennisnet/php-qti3`](https://github.com/Kennisnet/php-qti3) | **MIT** (`main/LICENSE`, © **2026** Kennisnet) | assessment | QTI 3 support library, **published this year**. The permissive PHP path into QTI, where `oat-sa/qti-sdk` is GPL-2.0 |
| [`Kennisnet/phpNLLOM`](https://github.com/Kennisnet/phpNLLOM) | **MIT** (`master/LICENSE`, © 2017 Stichting Kennisnet) | metadata | **NL-LOM**, the Dutch national application profile of LOM. The worked example of how a country profiles a global metadata standard |
| [`Kennisnet/phpEdurepSearch`](https://github.com/Kennisnet/phpEdurepSearch) | **MIT** (`master/LICENSE`, © 2015 Stichting Kennisnet) | discovery | Client for **Edurep**, the national learning-resource search index. A national OER index with a permissive client is a **content source you may query without a licence negotiation** |
| [`Kennisnet/OaiPmh`](https://github.com/Kennisnet/OaiPmh) | **MIT** (`main/LICENSE`, © 2024 Kennisnet) | harvesting | OAI-PMH implementation — the protocol national repositories actually expose |
| [`Kennisnet/qti-editor-angular`](https://github.com/Kennisnet/qti-editor-angular) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | authoring | QTI editor. **Ungranted — do not vendor it** |
| [`Kennisnet/edurep-xslt`](https://github.com/Kennisnet/edurep-xslt) | 🔴 **NO-PAYLOAD** (`main`+`master` × 6 filenames, all 404) | transforms | Edurep XSLTs. **Ungranted** |

⚠️ **Nine of 29 probed, chosen by stars and domain relevance.** The estate's ungranted rate is
**sampled, not established** — the same shortfall pass 17 declared for Opetushallitus's 188
repositories, and it is carried as a declared gap rather than rounded off.

### 🔵 The correction this section forces on trend 28

Trend 28 concluded that the permissive shelf has a **"Python-shaped hole"** — *"Python, where
essentially all of the AI tutoring and agent code in this KB is written, is not [served]."*

**Half of that survives.** There is still **no permissive Python LTI 1.3 library**, which is the
claim trend 28 actually measured. But `pylom` and `py-eduterm-client` are **MIT Python libraries
for education standards**, so Python *is* served for **metadata and curriculum vocabulary**.

🟢 **The hole is LTI-shaped, not Python-shaped — and that makes the contribution opening cheaper,
not smaller.** It is one protocol, with a procurement-scored buyer already attached (39% of US
districts score interoperability in the RFP rubric). Corrected in place in `intel/trends.md` §28.

## Added in the nineteenth pass of 2026-10-06 — the conformance-engine tier, which nineteen passes never recorded

**Channel: the regulatory-citation channel** — sweeping for implementations of the exact technical
standard a binding rule names (WCAG 2.1 AA, WCAG 2.2 AA, EN 301 549, PDF/UA) rather than by topic.
Every licence below was read from the repository's own payload on `raw.githubusercontent.com` on
2026-10-06, across `main` / `master` / `develop` and 7–11 filename variants. Star and fork counts
were read from the rendered repository page the same day (`api.github.com` is 403 here).

**Why these belong in *foundations* and not in trending:** none of them is new, none is
education-specific, and that is the point — they are the deterministic substrate that every
accessibility claim in a client deliverable has to rest on, and this KB's accessibility work so far
recorded the **agent** layer (`Community-Access/accessibility-agents`, MIT) without the engines
underneath it. An agent that reports WCAG findings with no engine beneath it is producing an
opinion, not evidence.

### The permissive engines — Apache-2.0 and MIT

| Repo | Licence (read from payload) | ★ / forks | What it gives you |
|---|---|---|---|
| [IBMa/equal-access](https://github.com/IBMa/equal-access) | **Apache-2.0** (`master/LICENSE`) | **780 / 108** | IBM Equal Access Accessibility Checker. **Nine packages** in one repo: `accessibility-checker-engine` (the rules), `accessibility-checker` (Node), `accessibility-checker-extension` (browser devtools), **`java-accessibility-checker`**, `cypress-accessibility-checker`, `karma-accessibility-checker`, `vitest-accessibility-checker`, `rule-server`, `report-react`. JavaScript. 🟢 **The pick when the deliverable must run in the client's CI**, and the only engine here with a **JVM** binding — which matters on a Java LMS estate. |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | **Apache-2.0** (`main/LICENSE`) | **30.9k / 9.8k** | Audits pages for accessibility alongside performance and best practices. **Runs locally and sends nothing to a remote server** — which is what makes it quotable under an EMEA data-residency clause. CLI, Node module, or Chrome DevTools. 🟡 Its a11y category is axe-core-derived and deliberately partial: a gate, not an audit. |
| [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web) | **MIT** (`main/LICENSE`, © Microsoft Corporation) | **955 / 182** | Chrome/Edge extension for assessing web accessibility. TypeScript. 🟢 **The differentiator is the guided assessment workflow** — it walks a human through the criteria a scanner cannot decide, which is the half of a conformance claim that automation cannot produce. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | **Apache-2.0** (`main/LICENSE`) | **76.8k / 10.8k** | OCR engine, **100+ languages**, LSTM line recogniser. Outputs plain text, **hOCR**, **ALTO**, **PAGE**, PDF and text-only PDF. 🟢 **The entry point for scanned textbooks** — and the structured output formats are what make a downstream tagging step possible at all. ⚠️ Latest tagged release on the page is **5.0.0 (2021-11-30)** while development continues on `main`; pin a distribution package rather than the tag. |

### The weak-copyleft engines — usable, with two obligations

| Repo | Licence (read from payload) | ★ / forks | The obligation |
|---|---|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | ⚠️ **MPL-2.0** (`master/LICENSE`) | **7.6k / 954** | Accessibility engine for automated web UI testing; **WCAG 2.0, 2.1 and 2.2 at A, AA and AAA**, multi-locale, 5,586 commits on `develop`. 🟢 **MPL-2.0 is file-level copyleft: using it unmodified as a dependency does not reach the studio's own files.** ⚠️ **Two things do bite** — it must appear in the client's SBOM with its licence, and **editing a rule file puts that file under MPL-2.0 with source-disclosure attached**. Tune through configuration, never by patching rules. 🔵 **This is the engine inside every MIT accessibility agent in this KB** (`accessibility-agents` declares `@axe-core/cli`; `a11ymcp` declares `axe-core` and `@axe-core/puppeteer` at runtime), so the inheritance is not optional — it is the shelf. |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | ⚠️ **MPL-2.0** (`main/LICENSE`) | **34.9k / 2.4k** | Adds an OCR text layer to scanned PDFs, deskews, and emits **PDF/A**. Python; Linux/macOS/Windows/FreeBSD. Wraps Tesseract. 🟢 Same file-level reasoning as axe-core — invoke it as a tool and nothing propagates. 🔴 **Read the limit precisely: a searchable PDF is not an accessible PDF.** It produces no tags, no reading order and no structure, so it does **not** satisfy PDF/UA. |

### 🔴 The gap this tier makes visible — validation is served, remediation is not

| Need | Permissive option | Status |
|---|---|---|
| Scan web content against WCAG | equal-access (Apache-2.0), axe-core (MPL-2.0), Lighthouse (Apache-2.0) | 🟢 **Well served** |
| Guide the manual half of a claim | accessibility-insights-web (MIT) | 🟢 Served |
| OCR a scanned textbook | Tesseract (Apache-2.0) | 🟢 Served |
| Make a scanned PDF searchable | OCRmyPDF (MPL-2.0) | 🟡 Served, and **not the same thing** as accessible |
| **Validate PDF/UA** | [veraPDF/veraPDF-library](https://github.com/veraPDF/veraPDF-library) | 🔴 **Dual GPL / MPL** — `LICENSE.GPL` and `LICENSE.MPL`, ⚠️ **filenames outside every shortlist this KB probes** (present on `master` and `integration`, absent from `main`), so an 11-filename sweep reports it ungranted while the grant is in the root |
| **Produce tagged, accessible PDF/UA** | — | 🔴 **Nothing permissive found.** Searched PDF/UA remediation, tagged PDF, structure tagging, accessible PDF generation |
| Reference the **EN 301 549** clause set | — | 🔴 **Nothing** except an MIT adapter to a paid API (`agents/top.md`) |

🔵 **The rule this yields for a proposal:** everything up to *"here is a per-criterion finding with
evidence"* can be built on Apache-2.0 and MIT with two MPL-2.0 tools invoked unmodified. Everything
past *"and here is the remediated PDF"* is **human labour on a copyleft validator**. ⚠️ **Scope and
price the document estate separately from the web estate.** They look like one deliverable in a
statement of work and they are not.

### 🟢 Why this shelf changes a conclusion rather than lengthening a list

This KB has recorded, across several passes, that permissive education supply collects at the
*edges* of platforms it may not fork. The conformance tier is the clearest instance yet and it
inverts the usual complaint: **the measuring layer is permissive and the end-user application layer
is copyleft** (`cboard` GPL-3.0, `AsTeRICS-Grid` AGPL-3.0, `pa11y` LGPL-3.0, `nvda` GPL-2.0+ in
`copying.txt` — see `verticals/solutions.md`). 🟢 **Since the billable work is remediating the
client's own estate rather than shipping an assistive application, the half a studio needs is the
half that is permissive.** That is a better position than this KB has been able to report for any
other tier in education, and it is worth stating plainly in a capability deck.

---

## Added in the twentieth pass of 2026-10-06 — the evidence tier, which every transition article actually asks for

**Channel new to this KB this pass: the transition-provision channel** — reading each
binding instrument's **transitional article** instead of its entry-into-force date. Full
findings in `agents/trending.md`; the regional consequences in `intel/market.md`; the
delivery recipe in `compose/patterns.md` **P28**.

The channel produced a supply question this KB had never asked. Every transition regime
found this pass discharges on an **artefact**, not on a date:

| Regime | What the extension is conditional on | The artefact that proves it |
|---|---|---|
| **EU AI Act Art. 111** | the design of the high-risk system **remaining unchanged** | a versioned, dated record that the deployed system is the same system |
| **Vietnam** Decree 142/2026/ND-CP | a **transition plan** filed on the one-stop portal | the plan, plus the inventory behind it |
| **Vietnam** Decision 33/2026/QĐ-TTg, education category 1 | self-learning content **not** drawn from *"uncontrolled data sources"* | dataset provenance and validation records |
| **EU Annex III §3** (admissions, assessment, placement) | bias and accuracy obligations | fairness measurements over the decision, retained |
| **EMEA, per the nineteenth pass** | 🔴 **no harmonised standard cited under the EAA**, so no presumption of conformity | evidence is the *only* route — there is no standard number to point at |

🔴 **Nineteen passes recorded none of the tooling that produces these artefacts.** Grep
confirmed it before this shelf was written: `mlflow`, `dvc`, `evidently`, `whylogs`,
`great_expectations`, `croissant`, `OpenLineage`, `fairlearn`, `AIF360` — **zero
occurrences across all eight files.** The KB had the obligations and the pedagogy, and
nothing in between.

### The shelf — all licences read from the repository's own payload on 2026-10-06

Stars and descriptions read from each repository page the same day via `WebFetch`
(`github.com` is 403 to `curl` through this environment's proxy; `raw.githubusercontent.com`
is not). **Ten rows, all verified.**

| Repo | Licence (payload path) | ★ / forks | Lang | What it does, and why an education engagement needs it |
|---|---|---|---|---|
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | **Apache-2.0** (`LICENSE.txt`) | 28.3k / 6.4k | Python | *"The open source AI engineering platform for agents, LLMs, and ML models."* Model registry with versioned stages. **This is the Art. 111 instrument**: the registry is what lets you state, with dates, that the system in service is the system that was placed in service. |
| [iterative/dvc](https://github.com/iterative/dvc) | **Apache-2.0** (`LICENSE`) | 15.9k / 1.3k | Python | *"Data Versioning and ML Experiments."* Versions the **corpus** alongside the model, in Git. The answer to Vietnam's *"uncontrolled data sources"* trigger is a hash, and this produces it. |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | **Apache-2.0** (`LICENSE`) | 11.9k / 1.9k | Python | *"Always know what to expect from your data."* Declarative data validation. Turns "the curriculum corpus is controlled" from an assertion into a suite that fails a build. |
| [evidentlyai/evidently](https://github.com/evidentlyai/evidently) | **Apache-2.0** (`LICENSE`) | 8.0k / 946 | Python | ML **and LLM** observability — evaluate, test and monitor any AI-powered system or pipeline. The regression baseline the nineteenth pass said a remediation contract has to ship. |
| [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) | **Apache-2.0** (`LICENSE`) | 2.9k / 912 | Python | Fairness metrics for datasets and models, explanations for them, and bias-mitigation algorithms. Annex III §3 is **admissions, assessment and placement** — decisions about people. |
| [whylabs/whylogs](https://github.com/whylabs/whylogs) | **Apache-2.0** (`LICENSE`) | 2.8k / 145 | Python | Data logging that emits **statistical profiles rather than raw records** — visibility into data quality over time with privacy-preserving collection. The shape that survives a student-data rule (see California **AB 1159**). |
| [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) | **Apache-2.0** (`LICENSE`) | 2.7k / 540 | Java | *"An Open Standard for lineage metadata collection."* A generic model of run, job and dataset entities. Lineage as a **standard**, so the evidence outlives your pipeline choice. |
| [fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) | **MIT** (`LICENSE`) | 2.3k / 522 | Python | *"A Python package to assess and improve fairness of machine learning models."* The **MIT** option on this shelf — the one with no notice obligation at all. |
| [NannyML/nannyml](https://github.com/NannyML/nannyml) | **Apache-2.0** (`LICENSE`) | ★ not read this pass | Python | Post-deployment performance estimation **without ground-truth labels**. Education's labels arrive a term or a year late; this is the tier that does not wait for them. |
| [mlcommons/croissant](https://github.com/mlcommons/croissant) | **Apache-2.0** (`LICENSE.md`) | 907 / 125 | Python | *"A high-level format for machine learning datasets."* Dataset metadata as a published format — the interchange layer for a provenance claim a regulator or a ministry can read. |

### Measured rejections from the same sweep

Recorded so a later pass does not re-probe them as options.

| Repo | Licence (payload) | Verdict |
|---|---|---|
| [deepchecks/deepchecks](https://github.com/deepchecks/deepchecks) | 🔴 **AGPL-3.0** (`LICENSE`) | Reject for reusable IP. Testing and validation for ML and LLM systems — capable, and the network clause reaches a hosted validation service. |
| [sodadata/soda-core](https://github.com/sodadata/soda-core) | 🔴 **Elastic License 2.0** (`LICENSE`) | Reject. **Not OSI-approved**; the payload opens *"Elastic License 2.0 … Acceptance: By using the software, you agree to…"*. A data-quality tool whose own licence is the risk it would be bought to manage. |

### Read this shelf honestly — three qualifications

🔵 **None of these is an education project.** This is general-purpose MLOps and
responsible-AI tooling. It earns a place in an education KB for one reason: the
transition articles found this pass are discharged by artefacts, and nothing already on
this KB's shelves produces them. ⚠️ **Do not present this tier as education IP** — present
it as the plumbing under a billable education-specific rubric, exactly as P27 treats
`inspect_ai`.

⚠️ **The fairness pair is a measurement tool, not a compliance verdict.** AIF360 and
Fairlearn compute metrics; which metric is the *right* one for an admissions decision is a
legal and pedagogical judgement that has to be made and documented per engagement. A
dashboard of eleven fairness metrics with no stated choice among them is not evidence.

🟢 **The licence shape of this tier is unusually clean** — nine of ten permissive, eight
Apache-2.0 and one MIT, every one read from its own payload. That is a better result than
the platform tier, the assistive tier or the language tier has ever returned in this KB,
and it means the evidence layer is the one part of an Annex III delivery with no licence
negotiation in it at all.

## Added in the twenty-second pass of 2026-10-06 — the interoperability layer, found on a forge this KB had never searched

Channel: the **GitLab REST API v4** (discovery + metadata + payload). Controls, limits and the
detector-error table are in `agents/top.md`; the instrument is in
`compose/code/gitlab-api-channel/`. 25 search terms → **534 unique projects** → the rows below are
the ones that are *infrastructure* rather than product.

🟢 **Why this shelf cared about the sweep at all:** trend 28 of this KB records an
**interoperability hole** — the standards (xAPI, LTI, 1EdTech) are scored line items in
procurement, and the permissive implementations were missing. **Three of the rows below are
standards plumbing**, and they were invisible to every previous pass because every previous pass
searched one forge.

| Repo | Licence (read from payload) | ★ · last activity | Placement | Why it is a foundation |
|---|---|---|---|---|
| [`kbarbounakis/eduapi`](https://gitlab.com/kbarbounakis/eduapi) | ⚠️ **LGPL-3.0** (`LICENSE`; GitLab's detector says `other`) | 0 · 2026-05-15 | ⚠️ EMEA *(README names **Universis**; Greece inferred)* | **An implementation of the 1EdTech EduAPI specification**, built for the **Universis** Greek higher-education student-information project. The first EduAPI implementation in this KB. ⚠️ **LGPL-3.0** — the middle path this KB already documents for Odoo/OpenEduCat: link against it, do not fold it into a proprietary binary |
| [`eduplex-api/cake-api-xapi-proxy`](https://gitlab.com/eduplex-api/cake-api-xapi-proxy) | 🟢 **MIT** (`LICENSE`) | 0 · 2026-08-31 | ⚠️ **unplaced** — no country evidence in repo or README | PHP proxy that forwards **xAPI** statements to an **LRS**, as a CakePHP plugin over `cake-rest-api`. Tiny, single-purpose, permissive — the cheapest way to put a compliant statement pipe in front of an LRS when the LMS cannot speak xAPI itself |
| [`TIBHannover/oer/wordpress-oersi-plugin`](https://gitlab.com/TIBHannover/oer/wordpress-oersi-plugin) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | EMEA (Germany) | WordPress integration of **OERSI**, the German higher-education **search index for Open Educational Resources**, with Elasticsearch indexing. From **TIB Hannover** (the German National Library of Science and Technology) — a public-institution-maintained OER discovery layer, MIT, actively committed |
| [`adaptive-learning-engine/adlete-packages`](https://gitlab.com/adaptive-learning-engine/adlete-packages) | 🟢 **MIT** (`LICENSE`) | 1 · **2026-10-02** | ⚠️ EMEA *(inferred)* | ADLETE adaptive-learning engine, monorepo of components; sibling `adaptive-learning-engine/moodle/adleteh5p` binds it to **H5P** inside Moodle. Full entry in `agents/top.md` |
| [`travo-cr/travo`](https://gitlab.com/travo-cr/travo) | 🟢 **BSD-3-Clause** (`LICENSE`) | 8 · **2026-10-06** | EMEA (France) + NA (Québec) | Assignment-distribution and grading infrastructure over **any** GitLab instance, **nbgrader**-integrated. Pairs with [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) (BSD-3-Clause, 1.4k★, v0.9.6 of 2026-09-30) already on this shelf. PyPI `travo` 2.1.1 |
| [`learntech-rwth/omilaxr-ecosystem/v2/omilaxr`](https://gitlab.com/learntech-rwth/omilaxr-ecosystem/v2/omilaxr) | 🔴 **AGPL-3.0** (`LICENSE`) | 1 · 2026-07-03 | EMEA (Germany) | **OmiLAXR** — authoring framework for modular **learning-analytics modules in XR** (VR/AR), from RWTH Aachen's Learning Technologies group. 🔴 Recorded and **excluded from delivery** on licence; kept because it is the only XR-learning-analytics framework this KB has located at all |
| [`particify/dev/foss/arsnova-lms-connector`](https://gitlab.com/particify/dev/foss/arsnova-lms-connector) | 🟢 **MIT** (`LICENSE`) | 3 · 🔴 **2022-09-12** | EMEA (Germany) | Proxy exposing **course-membership data from LMSs under one unified API** — from the ARSnova/Particify audience-response project. 🔴 **The first row in this KB marked dead by measurement rather than by inference:** `last_activity_at` is four years old. Read it as a design, not a dependency |
| [`git-classrooms/git-classrooms`](https://gitlab.com/git-classrooms/git-classrooms) | 🟢 **MPL-2.0** (`LICENSE`, detector agrees) | 3 · 2026-06-16 | ⚠️ **unplaced** (namespace only) | GitHub-Classroom-equivalent for self-hosted GitLab. ⚠️ **A publish-only mirror**: its own description points upstream to a GitHub repository, so the GitLab copy is a *host*, not the project. MPL-2.0 is file-level copyleft — usable alongside proprietary code, not inside the same file |

### ⚠️ The REUSE rows — where the root `LICENSE` is a map and not a grant

| Repo | Root `LICENSE` | The real licence set, enumerated from `/repository/tree?path=LICENSES` |
|---|---|---|
| [`oer/emacs-reveal`](https://gitlab.com/oer/emacs-reveal) | **517 B** REUSE pointer | **4**: `GPL-3.0-or-later`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC0-1.0` |
| [`oer/oer-reveal`](https://gitlab.com/oer/oer-reveal) | **516 B** REUSE pointer | **6**: the same four plus `LicenseRef-MIT-HEH-JL`, `LicenseRef-MIT-JL` — two **custom references**, which SPDX permits and no classifier can resolve |

🔵 **Pass 107 had already rejected `oer/emacs-reveal` on licence and kept it as a design.** What is
new is that the licence **set** is now enumerated rather than sampled: an OER toolchain splits
**code under GPL-3.0-or-later** from **content under CC-BY/CC-BY-SA/CC0**, and a `LicenseRef-`
entry means the project wrote its own terms. 🔴 **For this KB's method the consequence is blunt:
on a REUSE repository, reading the root payload — the rule that bought twenty passes of accuracy —
returns a notice board.** The answer lives in `LICENSES/` and in per-file SPDX headers, and only a
tree listing finds it.

### 🔴 What this sweep did **not** find, with the denominator attached

534 unique projects, 25 terms, one forge. **Not found, searched for explicitly:**

| Looked for | Terms used | Result |
|---|---|---|
| a permissive **LTI 1.3 tool provider** | `lms ai`, `learning management system`, `student information system` | 🔴 **0** — the LTI-shaped hole of trend 28 is still open on a second forge |
| a permissive **knowledge-tracing / BKT-IRT** library | `knowledge tracing`, `adaptive learning`, `learning analytics` | 🔴 **0** — `OATutor` (MIT) and the ADLETE engine above remain the only mastery assets in this KB |
| an **MCP server for education** on GitLab | `education agent`, `edtech ai`, `classroom ai` | 🔴 **1 candidate, unusable** — `sheikhcoders/interleaved-learning-mcp` carries **no licence payload at all**. Every education MCP server this KB holds is still GitHub-hosted |
| a **LATAM-origin** education project | all 25 terms | 🔴 **1 LATAM-plausible of 534**, and its placement is an inference from Portuguese-language naming, not a declaration — see `intel/market.md` |
