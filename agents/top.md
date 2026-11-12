---
industry: education
region: Global
updated: 2026-11-12
---

# Education AI agents — `p787`

**Every row below was verified this pass on two byte channels:** existence via `git ls-remote`
(exit status read directly, never through a pipe), and the licence grant by **clause presence**
in the served `LICENSE` bytes. No row is carried on a vendor claim, a star ranking or a blog.

> **Channel discipline (`T844`, carried):** repository existence and licence bytes are
> **byte-verified**. Star counts are **page-channel** reads of github.com and are rounded exactly
> as GitHub renders them. Every market, adoption and regulatory figure in this base is
> **search-channel testimony** — labelled as such wherever it appears.

**Controls for this pass:** 4 of 4 known-good rows reproduced the bytes this base already
recorded (`HKUDS/DeepTutor` 11,408 B · `moodle/moodle` 35,147 B · `sakaiproject/sakai` 11,120 B ·
`frappe/lms` 33,893 B). 2 planted negatives (`zzz-not-a-real-org-xyz/nope-nope`,
`Priyamakeshwari/TeachGPT`) were DEAD as designed. **3 defects in this pass's own probe were
caught by those controls and fixed before any verdict shipped** — see `intel/trends.md` `T847`–`T849`.

## The two poles — both 40k+ stars, both APAC-origin

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **DeepTutor** | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · `11,408 B` · `60fb3bdfddb3` | `58.5k` | APAC | Lifelong personalised tutoring workspace — tutoring, retrieval over the learner's own materials, practice, mastery tracking. `v1.7.2` tagged `2026.11.6`. **The most permissively-granted mature tutor in the sector** |
| **OpenMAIC** | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | MIT · `1,065 B` · `717b69cbe2f4` | `43.4k` | APAC | Tsinghua's Open Multi-Agent Interactive Classroom — turns a topic or document into a classroom with AI teacher and AI classmates, generating slides, quizzes, simulations and PBL activities. `v1.5.0-rc.1` news `2026-11-10`. ⚠️ **Bundled `packages/mathml2omml` is LGPL-3.0-or-later** — the repo grant is MIT but that workspace package is not; isolate it or run it out of process |

## Teaching-as-a-skill — the packaging shift of this window

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **agent_skills** (`socratic-tutor`) | [`janestreet/agent_skills`](https://github.com/janestreet/agent_skills) | MIT · `1,120 B` · `7c6715c29548` | `6.6k` | North America | Jane Street's skill set; the `socratic-tutor/` skill turns an LLM into a strict tutor — diagnostic, skill map with levels 0–5, one question at a time, spaced review, final assessment. **Tutoring shipped as a skill directory, not an application.** `2` commits. Canonical owner is `janestreet`; `jane-street/agent_skills` is DEAD |
| **china-k12-teacher-skills** | [`myvipbackup2/china-k12-teacher-skills`](https://github.com/myvipbackup2/china-k12-teacher-skills) | Apache-2.0 · `11,359 B` · `f1c6c4420e7d` | `3` | APAC | China-localised K-12 teacher skills with curriculum-aware lesson planning |

## Tutors and adaptive engines

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **OATutor** | [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | MIT · `1,105 B` · `fae8cc474484` | `279` | North America | UC Berkeley (CAHLR) adaptive tutoring with **Bayesian Knowledge Tracing** mastery estimation; React, optional Firebase logging. The mastery model most recipes here are missing |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | MIT · `1,068 B` · `cfe41f874290` | `175` | Global | Block-based adaptive learning workspace that runs locally — upload material → notes, quizzes, flashcards, adaptive tutor. 3 specialist agents (Tutor, Planner, Layout), 10+ LLM providers. ⚠️ **`cosark/OpenTutor` is a FORK of this repo at `0★` — do not cite it as a second project** |
| **Learning-Agent-System** | [`VaishnaviSingh-Analyst/Learning-Agent-System`](https://github.com/VaishnaviSingh-Analyst/Learning-Agent-System) | MIT · `1,086 B` · `fb2da327c928` | — | Global | LangGraph tutor on Ollama: checkpointed learning paths, tiered 5-3-2 assessment, a 70% pass bar, Feynman-style re-teaching |
| **no-vibe** | [`rizukirr/no-vibe`](https://github.com/rizukirr/no-vibe) | MIT · `1,065 B` · `5b8cb2f6d072` | `48` | Global | Turns a coding agent into a tutor that reads the learner's level and adapts — pedagogy applied to the agent rather than the content |
| **learnharness** | [`amosblomqvist/learnharness`](https://github.com/amosblomqvist/learnharness) | 🔴 **AGPL-3.0** · `34,523 B` · `cb25c8e49b85` | — | Global | Agent harness for learning difficult subjects. 🔴 **Copyleft: network-use triggers source disclosure.** Usable as a reference or a separately-deployed service, **not** as a library inside client code. Origin not determinable from the account name, so filed Global rather than guessed |

## Assessment and grading

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **GradeAI** | [`orancs11/GradeAI`](https://github.com/orancs11/GradeAI) | MIT · `1,061 B` · `93bd8bebe253` | `4` | Global | Automated grading that removes repetitive assessment work from teachers. Small, but the grant is clean and the scope is exactly what EU Annex III and several US states now regulate |
| **instructional_agents** | [`DaRL-GenAI/instructional_agents`](https://github.com/DaRL-GenAI/instructional_agents) | MIT · `1,067 B` · `f835eb45f508` | — | Global | Multi-agent generation of instructional material and courseware |

## Curriculum- and institution-specific — the rows a global studio actually needs

| Agent | Address | Grant, on the bytes | ★ | Region | What it is |
|---|---|---|---|---|---|
| **TutoriasITA** | [`Frangersal/TutoriasITA`](https://github.com/Frangersal/TutoriasITA) | MIT · `1,077 B` · `3184f6e7f75a` | `7` | LATAM | Institutional tutoring system, **Tecnológico Nacional de México, Campus Acapulco** |
| **TutorLSM** | [`ftrujillo36/TutorLSM`](https://github.com/ftrujillo36/TutorLSM) | Apache-2.0 · `11,357 B` · `ae26aa487282` | `0` | LATAM | **Mexican Sign Language (LSM)** learning and practice — accessibility supply in Spanish, permissively granted |
| **paes-mcp** | [`goyanedelv/paes-mcp`](https://github.com/goyanedelv/paes-mcp) | **MIT (Spanish text)** · `2,018 B` · `84e7f6106b38` | `0` | LATAM | MCP server over an open repository of Chile's **PAES** university-admission test. ⚠️ All four MIT clauses present **in Spanish** — see `T848`: an English-only clause probe scored this `UNGRADED` and would have dropped it. A translated grant is valid but is weaker evidence than the canonical English text; confirm with the maintainer before building on it |
| **teams-facultad-mcp** | [`Matias-Sanmiguel/teams-facultad-mcp`](https://github.com/Matias-Sanmiguel/teams-facultad-mcp) | MIT · `1,088 B` · `17b51f4db2b0` | `0` | LATAM | Local MCP server over Teams Educación — coursework, announcements, documents |
| **meta-cv-hktn-edu-agent** | [`Moses-Githinji/meta-cv-hktn-edu-agent`](https://github.com/Moses-Githinji/meta-cv-hktn-edu-agent) | MIT · `1,081 B` · `15fab99e0d0b` | `2` | EMEA | Teaching agent built for **Kenya's CBC curriculum** — the only artefact in this base tied to an African national curriculum |
| **VeryMath-textbook-copilot** | [`VeryMath/VeryMath-textbook-copilot`](https://github.com/VeryMath/VeryMath-textbook-copilot) | Apache-2.0 · `11,338 B` · `1183af0d8197` | `21` | APAC | Textbook pane beside a coding-agent pane: explanations, exercises, mind maps, knowledge graphs, LaTeX courseware |
| **Math-Modeling-Agent-Flow** | [`mantou6666/Math-Modeling-Agent-Flow`](https://github.com/mantou6666/Math-Modeling-Agent-Flow) | MIT · `1,067 B` · `69b2a4f15995` | `28` | APAC | Four-stage Solver→Paper pipeline for the CUMCM / MCM-ICM modelling competitions |
| **xuelian-agent** | [`llwand1/xuelian-agent`](https://github.com/llwand1/xuelian-agent) | MIT · `1,062 B` · `956783be029f` | — | APAC | Chinese-language study agent |

## Agent-adjacent infrastructure this base composes with

| Component | Address | Grant, on the bytes | ★ | Region | Role |
|---|---|---|---|---|---|
| **mcp-regulated-ai-compliance** | [`uchit/mcp-regulated-ai-compliance`](https://github.com/uchit/mcp-regulated-ai-compliance) | Apache-2.0 · `12,227 B` · `72e4b0734bcc` | — | Global | MCP compliance layer — the piece every regulated-deployment recipe here needs for Art. 27 FRIA evidence |
| **ai-agents-for-beginners** | [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | MIT · `1,141 B` · `4bcf574c06d3` | `79.5k` | Global | 18-lesson agent course. Curriculum, not a runtime — the fastest onboarding path for a studio squad |
| **agents-course** | [`huggingface/agents-course`](https://github.com/huggingface/agents-course) | Apache-2.0 · `11,357 B` · `9b3d6b3887bc` | — | Global | Hugging Face agents course |
| **ai-engineering-hub** | [`patchy631/ai-engineering-hub`](https://github.com/patchy631/ai-engineering-hub) | MIT · `1,066 B` · `042aeb506738` | ~`40k` | Global | Tutorial collection graded beginner→advanced. ★ is search-channel, not page-read |

## 🔴 Probed this pass and NOT usable

| Address | Finding | Why it is barred |
|---|---|---|
| [`tahseenparray1/agentic-rag-tutor`](https://github.com/tahseenparray1/agentic-rag-tutor) | ALIVE · `5160dde7e7d7` · **no `LICENSE` on any of 8 filenames × 3 branches** | 🔴 **No grant served.** The search channel recommended it as a grading-agent starting point; it carries no licence at its root. An ungranted repo is a question for its maintainer, not a usable dependency |
| [`cosark/OpenTutor`](https://github.com/cosark/OpenTutor) | ALIVE · MIT · `1,068 B` · fork of `zijinz456/OpenTutor` at `0★` | 🔴 **Not a distinct project.** The search channel returned it alongside the parent with identical prose, which is how a fork becomes a phantom second finding |
| [`jane-street/agent_skills`](https://github.com/jane-street/agent_skills) | **DEAD** | 🔴 The plausible-looking hyphenated spelling of a real org. Canonical is `janestreet/agent_skills` |

## Counts for this pass

| | Count |
|---|---|
| Agents listed with a byte-verified grant | **23** |
| of which **permissive** (MIT / Apache-2.0) | **22** |
| of which copyleft, flagged | **1** (`learnharness`, AGPL-3.0) |
| Placed **LATAM** | **4** |
| Placed **APAC** | **6** |
| Placed **North America** | **2** |
| Placed **EMEA** | **1** |
| Placed **Global** | **10** |
| Probed and rejected | **3** (1 ungranted, 1 fork, 1 dead address) |

🔴 **EMEA agent supply is the base's thinnest region and it is a measured gap, not an absence of
search.** One EMEA-placed education agent exists here (Kenya's `meta-cv-hktn-edu-agent`). The query
`open source education AI agent Europe EMEA Germany France Netherlands 2026 github sovereign`
returned **sovereign-LLM infrastructure and compliance commentary only** — OpenEuroLLM, Germany's
SOOFI, the Netherlands' GPT-NL, Apertus, Teuken, Mistral, Haystack — and **no European-origin
education agent repository**. Europe is building the substrate and not the education layer on top
of it. See `intel/market.md` → *Opportunities by region* → EMEA.
