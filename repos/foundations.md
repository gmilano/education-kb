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
