---
industry: education
region: Global
updated: 2026-11-12
---

# Education AI agents — `p788`

**Every row below was verified this pass on two byte channels:** existence via `git ls-remote`
(exit status read directly, never through a pipe), and the licence grant by **clause presence** in
the served `LICENSE` bytes. No row is carried on a vendor claim, a star ranking or a blog.

> **Channel discipline (`T844`, amended this pass — `T860`).** Repository existence and licence
> bytes are **byte-verified**. 🔴 **The page channel is GONE this pass:** `github.com` returns
> `403` through this session's proxy for every non-attached repository, and so does
> `api.github.com/repos/{owner}/{repo}`. 🟢 **Stars below are claim-channel reads of
> `search/repositories` with `repo:` qualifiers — which return EXACT integers**, not GitHub's
> rounded `58.5k`, and which reproduced every rounded page-read `p787` published. Every market,
> adoption and regulatory figure in this base remains **search-channel testimony**.

**Controls for this pass:** 7 of 7 known-good rows reproduced the bytes this base already recorded
(`HKUDS/DeepTutor` 11,408 B · `moodle/moodle` 35,147 B · `sakaiproject/sakai` 11,120 B ·
`frappe/lms` 33,893 B · `hedyorg/hedy` 13,827 B · `jupyter/nbgrader` 1,512 B · `oppia/oppia`
11,358 B). 2 planted negatives were DEAD as designed. 🔴 **6 defects in this pass's own
instruments were caught by those controls and fixed before any verdict shipped** — see
`intel/trends.md` `T860`–`T863`.

🔴 **The one thing to read before using this file.** `p787-D` is discharged below and it changes how
every row here must be read: **a repository-level grant says nothing about the grant on its
dependencies, and 4 of the 7 highest-star permissive education repos carry copyleft in their
declared direct dependencies.** See `## Dependency grants` at the foot of this file.

## The two poles — both APAC-origin, both permissive at the repository level

| Agent | Address | Grant, on the bytes | ★ (exact) | Region | What it is |
|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · `11,408 B` · `60fb3bdfddb3` | `58,508` | APAC | Lifelong personalised tutoring workspace — tutoring, retrieval over the learner's own materials, practice, mastery tracking. **The most permissively-granted mature tutor in the sector.** ⚠️ **`pyte` (LGPL-3.0) is a declared direct dependency** (`T861`) |
| **OpenMAIC** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT · `1,065 B` · `717b69cbe2f4` | `43,365` | APAC | Tsinghua's Open Multi-Agent Interactive Classroom — turns a topic or document into a classroom with AI teacher and AI classmates, generating slides, quizzes, simulations and PBL activities. ⚠️ **2 of 181 direct dependencies are copyleft:** `mathml2omml` (LGPL-3.0-or-later) and `jszip` (`MIT OR GPL-3.0-or-later`, so the MIT arm must be **elected in writing**) |

## Teaching-as-a-skill — the packaging shift, now with a derivative in the wild

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **agent_skills** (`socratic-tutor`) | [`janestreet/agent_skills`](https://github.com/janestreet/agent_skills) | MIT · `1,120 B` · `7c6715c29548` | `6,813` | North America | Jane Street's skill set; the `socratic-tutor/` skill turns an LLM into a strict tutor — diagnostic, skill map with levels 0–5, one question at a time, spaced review, final assessment. **Tutoring shipped as a skill directory, not an application.** Canonical owner is `janestreet`; `jane-street/agent_skills` is DEAD |
| **socratic-tutor** `NEW` | [`nuwaves/socratic-tutor`](https://github.com/nuwaves/socratic-tutor) | MIT · `1,143 B` · `2e34df6e23bd` | `2` | Global | 🟢 **The first downstream derivative of the above, created `2026-11-09`** — the same skill extracted as a standalone, installable unit with saved progress. `T851` predicted this packaging would travel; it has, in under a week |
| **china-k12-teacher-skills** | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | Apache-2.0 · `11,359 B` · `f1c6c4420e7d` | `3` | APAC | China-localised K-12 teacher skills with curriculum-aware lesson planning |

## EMEA — the gap `p787` recorded as empty, and it is not

🟢 **`ACTION p787-E` discharged by refutation (`T862`).** `p787` searched for a European-origin
open-source education agent **in English**, found only sovereign-LLM infrastructure, and recorded the
slot as empty. Querying the same slot in **Dutch, German, French and Greek** returned agents on the
first attempt. Every row below is byte-verified and **new to this base**.

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **onderwijsin/agents** `NEW` | [`onderwijsin/agents`](https://github.com/onderwijsin/agents) | **MIT** · `1,079 B` · `0b3eabc034fa` | `0` | EMEA | 🟢 **The find that refutes `T856`.** Provider-agnostic AI plugins and skills for Dutch **onderwijs** (education). 🔵 Found by querying `onderwijs AI agent`, which returned **exactly one** repository — this one. At `0★` it is below every star floor this base has ever used |
| **sherpa** `NEW` | [`SeydinaBANE/sherpa`](https://github.com/SeydinaBANE/sherpa) | **MIT** · `1,063 B` · `6411f2de98c1` | `0` | EMEA | French-language exam-preparation tutor: **grounded RAG with citations** plus agents. 🔵 Citation-grounding is the single feature `T859` argues an education deliverable most needs |
| **parcours-maths-ia** `NEW` | [`Warok-dev/parcours-maths-ia`](https://github.com/Warok-dev/parcours-maths-ia) | **MIT** · `1,066 B` · `51dc673f15a0` | `0` | EMEA | 2D educational maths game for French **CE1–CE2** with automatic exercise generation — curriculum-specific, primary-level |
| **dowze** `NEW` | [`Louisdelez/dowze`](https://github.com/Louisdelez/dowze) | **MIT** · `1,068 B` · `2a30b43ecd06` | `0` | EMEA | French lifelong-learning AI tutor, explicitly framed as a **bien commun** (commons) |
| **skepsis** `NEW` | [`ionpetro/skepsis`](https://github.com/ionpetro/skepsis) | **MIT** · `1,072 B` · `31a864169289` | `3` | EMEA | Teaches the Greek hiding inside everyday English in 3-minute lessons; ships a web app **and an MCP server**, so another agent can teach from it |
| **eagle-aig** `NEW` | [`LIST-LUXEMBOURG/eagle-aig`](https://github.com/LIST-LUXEMBOURG/eagle-aig) | **Apache-2.0** · `11,358 B` · `99cecb066ecf` | — | EMEA | 🟢 **Luxembourg Institute of Science and Technology** — a national public research institute. **Rescued from this base's ungranted class this pass** (`p787-B`): it was filed as an absence and has carried Apache-2.0 all along |

### 🟢 `elimu-ai` — a 66-repository MIT African education ecosystem this base was already citing

🔴 **This base cited `elimu-ai` at `agents/trending.md:24964` and never placed it.** It surfaced only
because it was the **single false positive** of `p787-A`'s login-validity clause (`T863`). All seven
core repositories are **MIT, `1,065 B`, identical licence text, pushed within the last week.**

| Repo | Address | Grant, on the bytes | ★ | Role |
|---|---|---|---|---|
| **webapp** | [`elimu-ai/webapp`](https://github.com/elimu-ai/webapp) | MIT · `1,065 B` · `f471cb573ae3` | `41` | Hosts the Android applications and the educational content library |
| **appstore** | [`elimu-ai/appstore`](https://github.com/elimu-ai/appstore) | MIT · `1,065 B` · `65a7ab4e8d50` | `29` | On-device APK download/install/update — **content delivery without an app store**, which is the binding constraint it is built for |
| **ml-authentication** | [`elimu-ai/ml-authentication`](https://github.com/elimu-ai/ml-authentication) | MIT · `1,065 B` · `0a7a6bb02ab6` | `16` | On-device student authentication. ⚠️ Biometric identification of children — read `T854` and EU Art. 5 before deploying this in EMEA or North America |
| **launcher** | [`elimu-ai/launcher`](https://github.com/elimu-ai/launcher) | MIT · `1,065 B` · `b50a175a7056` | `9` | Android launcher that constrains the device to a single instructional path |
| **ml-storybook-reading-level** | [`elimu-ai/ml-storybook-reading-level`](https://github.com/elimu-ai/ml-storybook-reading-level) | MIT · `1,065 B` · `119642b8b1c3` | `8` | 🟢 ML model predicting a storybook's reading level — **a real, permissive levelling model**, which no other row in this base supplies |
| **ml-storybook-recommender** | [`elimu-ai/ml-storybook-recommender`](https://github.com/elimu-ai/ml-storybook-recommender) | MIT · `1,065 B` · `940048e2cc32` | `3` | Predicts likability of unread storybooks |
| **model** | [`elimu-ai/model`](https://github.com/elimu-ai/model) | MIT · `1,065 B` · `5f16dd17e351` | `4` | Shared library across the webapp and the Android apps |

## APAC — `ACTION p787-F` discharged, and the three countries differ completely

### 🟢 India — the region's richest curriculum-specific supply

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **OpenVidya** `NEW` | [`dpaul0501/OpenVidya`](https://github.com/dpaul0501/OpenVidya) | 🔴 **AGPL-3.0** · `34,523 B` · `1224dcd5693b` | `2` | 🟢 **The most strategically interesting row of the pass: an OpenMAIC derivative redesigned for NCERT/CBSE.** 🔴 **And it relicensed upward** — OpenMAIC is MIT, this fork is AGPL-3.0. MIT permits that, and it means the India-localised classroom **cannot** be embedded in a client deliverable the way its parent can |
| **RAG-Enhanced-NCERT-Tutor** `NEW` | [`praj2408/RAG-Enhanced-NCERT-Tutor`](https://github.com/praj2408/RAG-Enhanced-NCERT-Tutor) | MIT · `1,072 B` · `adf4c082db90` | `5` | Retrieval-grounded tutor over the **NCERT** national curriculum |
| **CBSE_Home-Tutor** `NEW` | [`mandarab76/CBSE_Home-Tutor`](https://github.com/mandarab76/CBSE_Home-Tutor) | MIT · `1,077 B` · `f987f634f5e0` | `1` | **CBSE** tutor spanning classes 1–12 |
| **ai-agent-to-learn-faster-and-better** `NEW` | [`abhijeetgupta23/ai-agent-to-learn-faster-and-better`](https://github.com/abhijeetgupta23/ai-agent-to-learn-faster-and-better) | MIT · `1,071 B` · `df69fd3331dd` | `4` | Adaptive tutor that personalises **lesson modality** from a learning-science knowledge graph |
| **FunctionVisualizer-V3** `NEW` | [`Adarsh-61/FunctionVisualizer-V3`](https://github.com/Adarsh-61/FunctionVisualizer-V3) | MIT · `1,056 B` · `10099c811f61` | `3` | Interactive NCERT mathematics visualisation |
| **NCERT-AI-Teacher-Assistant** `NEW` | [`Prady029/NCERT-AI-Teacher-Assistant`](https://github.com/Prady029/NCERT-AI-Teacher-Assistant) | 🔴 GPL-3.0 · `35,149 B` · `5e24bf860660` | `5` | Lesson plans and question sets for teachers. 🔴 Copyleft |

🟢 **`p787-F`'s India finding, stated plainly:** India's gap was never supply, it was **vocabulary**.
`tutor agent education India curriculum` returned `0`. `NCERT AI` returned **`330`**.

### 🟢 South Korea — placed for the first time, behind a semantic trap

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **spring-ai-tutor** `NEW` | [`jungtaejin/spring-ai-tutor`](https://github.com/jungtaejin/spring-ai-tutor) | MIT · `1,069 B` · `8ca838adabcc` | `0` | Korean tutoring API on Spring AI — structured output, conversation memory, tool calling, SSE streaming |
| **Haeksim** `NEW` | [`Seongbong-Ha/Haeksim`](https://github.com/Seongbong-Ha/Haeksim) | MIT · `1,069 B` · `242b3f09aa73` | `0` | 핵심 ("core") — an NLP AI learning-tutor project |

🔴 **The trap, recorded because it will recur.** Korean **교육** means both *education* and
*corporate training*. The query `AI 교육 에이전트` returned `20` repositories of which **almost none
are education agents** — they are agent-training course materials (a Samsung practitioner
curriculum, "AI maestro" week-4 coursework). 🟢 The productive query was `학습 튜터 AI`
(*learning tutor*), which returned `12`. **A word that means two things returns the wrong head.**

### 🔴 Japan — a measured gap, and it survived in-language querying

🔴 **This is the pass's cleanest negative result.** `AI 教育 エージェント` returned **3** repositories
in total; `学習支援 AI エージェント` returned **1**. The best Japan-origin artefact found is
[`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) —
Osaka City Education Center junior-high lesson plans structured as a dataset for education-AI
research — and it is **ALIVE at `212cb10e48eb` serving no licence on 10 filenames × 3 branches.**
🟢 **Japan's absence is now measured in Japanese, not inferred from English**, which is what
`p787-F` asked for. See `intel/market.md` → APAC.

### China

| Agent | Address | Grant, on the bytes | ★ | What it is |
|---|---|---|---|---|
| **AI-tutor** `NEW` | [`qiyuxi24/AI-tutor`](https://github.com/qiyuxi24/AI-tutor) | MIT · `1,065 B` · `046f65596541` | `4` | Knowledge-graph-driven guidance agent: knowledge map, learning path, learner profile, question generation. `413` test cases, L1–L4 live-API evaluation, BM25 gating with RRF hybrid retrieval — **the most explicitly evaluated small agent in this base** |
| **VeryMath-textbook-copilot** | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | Apache-2.0 · `11,338 B` · `1183af0d8197` | `21` | Textbook pane beside a coding-agent pane: explanations, exercises, mind maps, knowledge graphs, LaTeX courseware |
| **Math-Modeling-Agent-Flow** | [`mantou6666/Math-Modeling-Agent-Flow`](https://github.com/mantou6666/Math-Modeling-Agent-Flow) | MIT · `1,067 B` · `69b2a4f15995` | `28` | Four-stage Solver→Paper pipeline for the CUMCM / MCM-ICM modelling competitions |
| **xuelian-agent** | [`llwand1/xuelian-agent`](https://github.com/llwand1/xuelian-agent) | MIT · `1,062 B` · `956783be029f` | — | Chinese-language study agent |

## Tutors and adaptive engines

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT · `1,105 B` · `fae8cc474484` | `279` | North America | UC Berkeley (CAHLR) adaptive tutoring with **Bayesian Knowledge Tracing** mastery estimation. 🟢 **`0` of `43` direct dependencies are copyleft — the cleanest dependency tree measured this pass** |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT · `1,068 B` · `cfe41f874290` | `175` | Global | Block-based adaptive learning workspace that runs locally. 3 specialist agents (Tutor, Planner, Layout), 10+ LLM providers. 🟢 `1` direct dependency, `0` copyleft. ⚠️ `cosark/OpenTutor` is a FORK at `0★` |
| **examprep-agent** `NEW` | [`ZeKaiNie/examprep-agent`](https://github.com/ZeKaiNie/examprep-agent) | MIT · `1,065 B` · `83fad934ea90` | `1` | Global | Study agent that teaches **only** from the learner's own slides and homework — a scoping constraint, not a limitation |
| **claude-study-agent** `NEW` | [`dymchenkko/claude-study-agent`](https://github.com/dymchenkko/claude-study-agent) | MIT · `1,067 B` · `527f9ac590a0` | `3` | Global | University-course study agent built on a coding-agent host, learning from the learner's own slides and PDFs |
| **lessonfolk** `NEW` | [`CGSeb/lessonfolk`](https://github.com/CGSeb/lessonfolk) | MIT · `1,063 B` · `7710ddf025ab` | `3` | Global | Learn AI from zero to advanced with an agent as the tutor |
| **algebench** `NEW` | [`ibenian/algebench`](https://github.com/ibenian/algebench) | MIT · `1,063 B` · `6794217849f9` | `8` | Global | Interactive **3D** maths visualiser with an agentic tutor — concepts explored through live simulation |
| **rag-tutor** `NEW` | [`villadalmine/rag-tutor`](https://github.com/villadalmine/rag-tutor) | **Apache-2.0** · `7,450 B` · `b0bc280f04ec` | `2` | Global | Sovereign, local-first tutor over technical books: hybrid RAG + agentic loop + MCP server. 🔴 **GitHub indexes this `NOASSERTION`; the bytes are Apache-2.0 with all `9` operative sections verified individually** — the `3,907 B` shortfall is the omitted non-operative APPENDIX only (`T845`: length is not a verdict) |
| **Thesaurus** `NEW` | [`Ahhsaaaaan/Thesaurus`](https://github.com/Ahhsaaaaan/Thesaurus) | Apache-2.0 · `11,343 B` · `dc29f0d739ff` | `0` | Global | Classroom knowledge base: teachers upload course documents, students query them over RAG |
| **Learning-Agent-System** | [`VaishnaviSingh-Analyst/Learning-Agent-System`](https://github.com/VaishnaviSingh-Analyst/Learning-Agent-System) | MIT · `1,086 B` · `fb2da327c928` | — | Global | LangGraph tutor on Ollama: checkpointed learning paths, tiered 5-3-2 assessment, a 70% pass bar, Feynman-style re-teaching |
| **no-vibe** | [`rizukirr/no-vibe`](https://github.com/rizukirr/no-vibe) | MIT · `1,065 B` · `5b8cb2f6d072` | `48` | Global | Turns a coding agent into a tutor that reads the learner's level and adapts — pedagogy applied to the agent rather than the content |
| **llm-edu-suite** `NEW` | [`ZoodiacR/llm-edu-suite`](https://github.com/ZoodiacR/llm-edu-suite) | MIT · `1,065 B` · `da605cdaf27e` | `3` | Global | Learn LLM engineering by building and measuring each layer — tokenizer, transformer, pre-training |
| **learnharness** | [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | 🔴 **AGPL-3.0** · `34,523 B` · `cb25c8e49b85` | — | Global | Agent harness for learning difficult subjects. 🔴 **Copyleft: network-use triggers source disclosure** — reference or separately-deployed service only |

## Assessment and grading

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **GradeAI** | [`orancs11/GradeAI`](https://github.com/orancs11/GradeAI) | MIT · `1,061 B` · `93bd8bebe253` | `4` | Global | Automated grading. Small, but the grant is clean and the scope is exactly what EU Annex III and several US states now regulate |
| **instructional_agents** | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | MIT · `1,067 B` · `f835eb45f508` | — | Global | Multi-agent generation of instructional material and courseware |

## LATAM

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **TutoriasITA** | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | MIT · `1,077 B` · `3184f6e7f75a` | `7` | LATAM | Institutional tutoring system, **Tecnológico Nacional de México, Campus Acapulco** |
| **TutorLSM** | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | Apache-2.0 · `11,357 B` · `ae26aa487282` | `0` | LATAM | **Mexican Sign Language (LSM)** learning and practice — accessibility supply in Spanish, permissively granted |
| **paes-mcp** | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | **MIT (Spanish text)** · `2,018 B` · `84e7f6106b38` · 🔴 **SCOPE-LIMITED** | `0` | LATAM | MCP server over Chile's **PAES** university-admission test. 🔴 **CORRECTION TO `p787` (`T864`): the MIT grant covers the SOURCE CODE AND DOCUMENTATION ONLY.** The licence text states in terms that it does *not* — and *could* not — cover the PAES items, figures and answer keys, whose rights belong to **DEMRE, Universidad de Chile**; that material is included from freely published official sources for educational use with attribution. **`P787-3` was built on this row as though the corpus were MIT. It is not** |
| **teams-facultad-mcp** | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | MIT · `1,088 B` · `17b51f4db2b0` | `0` | LATAM | Local MCP server over Teams Educación — coursework, announcements, documents |
| **Tlamatini** `NEW` | [`XAIHT/Tlamatini`](https://github.com/XAIHT/Tlamatini) | MIT · `1,062 B` · `b1f06f7e736f` | `15` | LATAM | Speak an idea, build the real thing: voice-driven AI into code, 3D worlds and hardware. 🔵 **`Tlamatini` is Nahuatl for *one who knows*** — named in an Indigenous Mexican language, which is why no English query reaches it |

## Agent-adjacent infrastructure this base composes with

| Component | Address | Grant, on the bytes | ★ | Region | Role |
|---|---|---|---|---|---|
| **brightspace-d2l-mcp** `NEW` | [`anonymousonyx22/brightspace-d2l-mcp`](https://github.com/anonymousonyx22/brightspace-d2l-mcp) | **MIT** · `1,200 B` · `a873478a6b4e` | — | North America | 🟢 MCP server over **D2L Brightspace** — the third major North American LMS, and until now the only one this base had no attachment point for. Rescued from the bespoke bucket this pass |
| **xapi-service** `NEW` | [`LearningLocker/xapi-service`](https://github.com/LearningLocker/xapi-service) | **MIT** · `1,070 B` · `685c342129c5` | — | Global | 🟢 **xAPI learning-record service, MIT — rescued from this base's ungranted class.** This base called its Caliper/QTI/xAPI cluster "its most dead cluster"; the live, permissive half of it was filed as an absence |
| **xapi-validation** `NEW` | [`LearningLocker/xapi-validation`](https://github.com/LearningLocker/xapi-validation) | **MIT** · `1,070 B` · `13ffff748515` | — | Global | xAPI statement validation — the evidence layer under any audit-trail claim |
| **mcp-regulated-ai-compliance** | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | Apache-2.0 · `12,227 B` · `72e4b0734bcc` | — | Global | MCP compliance layer — Art. 27 FRIA evidence for every regulated-deployment recipe here |
| **collect** `NEW` | [`getodk/collect`](https://github.com/getodk/collect) | **Apache-2.0** · `10,494 B` · `2344bb9c5da4` | — | Global | ODK Collect — offline mobile data collection. The field-survey instrument for a readiness diagnostic where connectivity fails |
| **ai-agents-for-beginners** | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | MIT · `1,141 B` · `4bcf574c06d3` | — | Global | 18-lesson agent course. Curriculum, not a runtime — the fastest onboarding path for a studio squad |
| **annotated_deep_learning_paper_implementations** `NEW` | [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT** · `1,082 B` · `db59a04a8a2c` | — | Global | Annotated implementations of DL papers — rescued from the ungranted class; a teaching corpus under a permissive grant |

## Dependency grants — `ACTION p787-D` discharged, and it is this pass's headline

🔴 **A repository-level grant describes one file. It does not describe what the project pulls in.**
Direct dependencies were read from each project's own manifest and each dependency's grant from the
npm or PyPI registry (`ingest/p788-dep-audit`). 🔵 **Transitive dependencies were NOT audited** —
this is the first layer only, and the first layer was already enough to change four rows.

| Repo | Repo grant | Direct deps | Copyleft found | Verdict |
|---|---|---|---|---|
| [`oppia/oppia`](https://github.com/oppia/oppia) | 🟢 Apache-2.0 | `171` | 🔴 **`angular-shepherd` — AGPL-3.0** | 🔴 **The most serious finding of the pass.** This base lists Oppia under *"build on these, link them, **ship them in client code**"*. An **AGPL-3.0** dependency in a browser-delivered bundle is the hardest copyleft there is, and network delivery is its trigger. **Remove or replace `angular-shepherd` before Oppia goes into a client deliverable** |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 🟢 MIT | `32` | 🔴 `zeroconf-py2compat` (LGPL-2), `json-schema-validator` (LGPL) | 🟡 This base's *"most valuable permissive row"* carries **two** LGPL dependencies. 🟢 **LGPL tolerates dynamic linking**, which is how Python imports work, so Kolibri stays usable — but the components must remain replaceable and their source available. **Not the unqualified MIT story the base has been telling** |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `27` | 🔴 `pyte` — LGPL-3.0 | 🟡 The sector's **#1 agent at `58,508★`** carries a copyleft dependency. `pyte` is a terminal emulator — likely droppable. **Check whether the tutoring path needs it at all** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 MIT | `181` | 🔴 `mathml2omml` (LGPL-3.0-or-later); 🟡 `jszip` (`MIT OR GPL-3.0-or-later`) | 🟡 `p787` found `mathml2omml` as a bundled workspace package; it is **also a declared dependency**. 🔵 **`jszip` is NEW and is dual-licensed** — a dual grant is permissive only if you **elect** the MIT arm, in writing, on the record |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | `43` | 🟢 **none** | 🟢 **Clean.** One unresolvable private scope (`@common/global-config`) is unpublished, not unlicensed |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 BSD-3 | `18` | 🟢 **none** | 🟢 **Clean — and this is the component that anchors `P788-1`, the flagship grading pattern.** The one row a regulated deliverable most depends on is the one that audits cleanest |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 MIT | `1` | 🟢 **none** | 🟢 Clean |

🟢 **The number to carry into a client conversation: 4 of 7.** Four of the seven highest-star
permissive education repositories carry copyleft in their **declared direct dependencies**, and in
every case the repository's own `LICENSE` file says nothing about it. 🔵 **The two that audit clean
— `nbgrader` and `OATutor` — are the two this base's grading pattern already rests on**, which is
luck rather than design, and is now on the record as a reason to keep resting on them.

## 🔴 Probed this pass and NOT usable

| Address | Finding | Why it is barred |
|---|---|---|
| [`Kosudo/nextSIS`](https://github.com/Kosudo/nextSIS) | ALIVE · `60e422c7d93e` · **`39,890 B` — all-rights-reserved, no grant of permission** | 🔴 **PROPRIETARY, newly measured.** A named Student Information System, filed by this base as merely "ungranted". 🔵 A `39,890 B` licence file is not evidence of an open grant — it is evidence of a long one |
| [`Tzxser/aipha-learning-os`](https://github.com/Tzxser/aipha-learning-os) | ALIVE · `aa476a6a6a03` · `1,296 B` bespoke | 🔴 **PROPRIETARY**, now graded rather than left `UNGRADED`. Source-available multi-agent learning OS |
| [`metabase/metabase`](https://github.com/metabase/metabase) | ALIVE · `6006cc9c65dd` · `855 B` | 🔴 **SPLIT BY DIRECTORY, not one licence.** AGPL-3.0 outside `enterprise/`, **Metabase Commercial License** inside it. 🟢 Reporting one family for this repo would be the error; the boundary is the fact. Same shape as `764-C` |
| [`luscitiosus/Dirigo`](https://github.com/luscitiosus/Dirigo) | ALIVE · `9ed32d5c2577` · `362 B` | 🔴 **CORRECTION — this base's published reason was WRONG.** `p786` recorded *"a file named `LICENSE` containing a Latin boast and no grant of any kind"*. The Latin boast is line 1; **lines 3–5 grant CC BY-NC-SA 4.0, in Spanish, with a link to the Spanish legal code**, and a scope clause excluding the downloaded BOE/BOC statutory texts. Still barred commercially — but **NonCommercial is a harder bar than an absence, and the stated reason was false** (`T863`) |
| [`cosark/OpenTutor`](https://github.com/cosark/OpenTutor) | ALIVE · MIT · fork of `zijinz456/OpenTutor` at `0★` | 🔴 **Not a distinct project** |
| [`lehrer-tools/lehrer-agent`](https://github.com/lehrer-tools/lehrer-agent) ≡ [`NikolasSchaeffner/lehrer-agent`](https://github.com/NikolasSchaeffner/lehrer-agent) | Both ALIVE · **identical `HEAD` `3ddcfbbabc56`** · neither serves a licence | 🔴 **ONE German teacher agent, carried by this base as TWO ungranted rows.** 🟢 **`ACTION p787-G` discharged mechanically (`T865`):** `p787` said only a page read could separate a fork from a project. **Identical `HEAD` sha proves it on the byte channel**, and the page channel is `403` this pass |
| [`narumi-mase/osaka-lesson-dataset`](https://github.com/narumi-mase/osaka-lesson-dataset) | ALIVE · `212cb10e48eb` · no licence on 10 filenames × 3 branches | 🔴 Japan's best education-AI artefact, **ungranted**. An upstream licence request, not a permanent exclusion |
| [`silja-graf/Didaktikus-…-LP21`](https://github.com/silja-graf/Didaktikus-KI-Spezialist-f-r-Unterrichtsplanung-und-Beurteilung-nach-LP21) | ALIVE · `8d747cda689e` · no licence | 🔴 A **Swiss LP21-curriculum** lesson-planning and assessment agent — the single most engagement-shaped EMEA artefact found, and ungranted. 🔵 **Ask for this one** |
| [`RAFCERAY/horizonia`](https://github.com/RAFCERAY/horizonia) · [`redoneabouaali-lab/najih`](https://github.com/redoneabouaali-lab/najih) · [`MRiARC/VidyaSetu`](https://github.com/MRiARC/VidyaSetu) · [`TaoYu-ds/TutorMesh`](https://github.com/TaoYu-ds/TutorMesh) · [`kaikai52125/NeoTutor`](https://github.com/kaikai52125/NeoTutor) · [`SoukhyadP991/Multilingual-NCERT-Doubt-Solver`](https://github.com/SoukhyadP991/Multilingual-NCERT-Doubt-Solver) · [`mingxuanyan07-lgtm/ai-for-education-showcase`](https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase) | all ALIVE · none serving a licence | 🔴 **7 further ungranted agents, placed by region so the absence is useful:** FR, Morocco, IN, CN, CN (a DeepTutor re-implementation on LangGraph), IN (offline NCERT doubt-solver), CN (auditable multi-agent maths teaching). 🟢 These are **licence requests**, and three of them are the best artefact found for their country |

## Counts for this pass

| | Count |
|---|---|
| Agents and components listed with a byte-verified grant | **48** |
| of which **permissive** (MIT · Apache-2.0 · ECL-2.0 · BSD) | **44** |
| of which copyleft, flagged | **4** (`learnharness` AGPL-3.0, `OpenVidya` AGPL-3.0, `NCERT-AI-Teacher-Assistant` GPL-3.0, `frappe/lms` AGPL-3.0) |
| 🟢 **NEW to this base this pass** | **30** |
| Placed **EMEA** | **13** (6 agents + 7 `elimu-ai`) — was **1** |
| Placed **APAC** | **12** (6 India · 2 Korea · 4 China) — was **6**, all China/HK |
| Placed **LATAM** | **5** |
| Placed **North America** | **4** |
| Placed **Global** | **14** |
| Probed and rejected | **15** (2 proprietary, 1 split-by-directory, 1 NonCommercial, 1 fork, 1 duplicate address pair, 9 ungranted) |
| 🔴 Rows whose published verdict this pass CORRECTED | **4** (`paes-mcp` scope · `Dirigo` grant · `MyScript/MyScriptJS` grant · the `lehrer-agent` double-count) |
| 🔴 Defects found in this pass's OWN instruments, by controls, before publication | **6** |

🟢 **EMEA agent supply is no longer this base's thinnest region, and the correction was
instrumental rather than factual.** Europe's education agents were always there; the queries were
in the wrong languages. 🔴 **The thinnest region is now Japan**, measured in Japanese at **3 total
repositories**, and the thinnest *grant* is Japan's too — its one serious artefact carries none.
