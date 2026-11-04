---
industry: education
region: Global
updated: 2026-11-04
---

# 🎯 AI agents — Education

> Open source AI agents for the education industry. Focus: MIT / Apache-2.0 / BSD — the licences Globant can build commercial derivatives on.
> Every row below was verified on 2026-11-04: existence via `git ls-remote --symref` (real default branch), licence by reading the grant payload from `raw.githubusercontent.com`, stars from the repository page.

## The agents — 12 verified rows

Twelve rows. That is how many real, permissively-licensed education agents this base has verified — not a target, a count. Three were added at p651 (AI-Shifu, GenMentor and the **upstream** `tutor-mcp`); two at p652: **OmniEdu**, which is a new *layer* rather than another tutor, and **moodle-mcp**, which closes — partially, and with its scale stated — the longest-standing declared gap on this page.

Read the stars column as measured-on-date and nothing more. Two rows here are below 100★ and one is at 27★; they are filed because they are the only permissive thing that does their job, and each says so in its own cell.

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 55,000 | APAC | Lifelong personalised tutoring. Persistent student model across sessions, proactive check-ins, multi-mode delivery. The most-adopted education agent in open source. arXiv:2604.26962. University of Hong Kong (HKUDS). |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | 42,700 | APAC | Open Multi-Agent Interactive Classroom. Turns a topic or uploaded document into a live lesson delivered by AI teachers *and* AI classmates that speak, draw on a whiteboard and debate. Slides, quizzes, simulations, PBL. LangGraph orchestration. **v1.4.0 released 2026-11-04.** MIT only since **v0.3.0 (2026-06-28)**; prior licence not named in the repository. ⚠ Builds an **LGPL-3.0-or-later** workspace package — see the licence note below. Tsinghua. |
| **OmniEdu** | [haolpku/Omni-Edu](https://github.com/haolpku/Omni-Edu) | **Apache-2.0 (code only)** | 590 | APAC | 🟢 **New layer, not another tutor: the education-domain foundation model an agent runs on.** 4B / 9B / 27B, each in BF16 and FP8, trained for subject competence, curriculum grounding, diagnostic reasoning and pedagogical scaffolding on 69,999 instruction examples / 15.96M supervised response tokens from 100+ sources. Backbones Qwen3.5-4B-Base, Qwen3.5-9B-Base, Qwen3.8-27B. Ships the `omniedu` PyPI toolkit with a 12-benchmark eval suite. 27B self-reports the leading open-weight results on K12-Bench (63.12 EM / 76.69 F1), MathFish (85.89), EDUMATH MaC (86.95) and MathTutorBench Scaffold (78.74). arXiv:2609.23088. Peking University + UCAS + Zhongguancun Academy. ⚠ **The Apache-2.0 grant covers the code; the weights' licence is named nowhere in the repository.** Read the model card before deploying weights. |
| **Instructional Agents** | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | 490 | Global (unplaced) | Multi-agent ADDIE pipeline: syllabus → LaTeX slides → assessments, end to end. Roles: Teaching Faculty, Instructional Designer, TA, Coordinator. EACL 2026 Main. |
| **AI-Shifu** | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 | 331 | APAC | Course **authoring** plus adaptive delivery — a different job from tutoring. An instructor supplies expertise and teaching intent once; the system generates per-learner explanations, probing Q&A, and a course embeddable in a website or training portal. Docker self-hosting. Research Center of Intelligent Software Engineering, **Harbin Institute of Technology**. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 317 | Global (unplaced) | Canvas LMS MCP server exposing ~102–128 tools plus agent skills for students and educators. Works with Claude, Cursor, Codex. The cleanest path from an agent to a real institutional LMS. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 302 | Global (unplaced) | Private AI tutor built on Bloom's 2-sigma result for one-to-one instruction. Generates a course outline, then adapts each lesson to learner feedback and annotations. Runs as a Claude Code skill *or* a self-hosted web app. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | North America | Intelligent tutoring system with Bayesian Knowledge Tracing. ReactJS + Firebase, LTI for LMS integration, curated maths content library. UC Berkeley (CAHLR). Peer-reviewed, production-grade. |
| **GenMentor** | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 136 | Global (unplaced) | Goal-oriented tutoring: the learner states a goal, coordinated LLM agents refine it, measure the gap against the learner's background, schedule sessions, draft each session's reading and quiz, and update the profile from activity. WWW '25 Industry Track oral. ⚠️ `main` is a browser-only Next.js app; the paper's multi-agent Python implementation is on branch **`v0.1-demo`**. CC0 is a public-domain dedication, not a software licence — no patent or trademark grant. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | 116 | Global (unplaced) | Multimodal tutoring: voice, video and configurable 3D avatars. Docker-first, runs local LLMs via Ollama. arXiv:2602.07176. |
| **tutor-mcp** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 96 | Global (unplaced) | MCP server that turns any LLM into an intelligent tutoring system: Bayesian Knowledge Tracing, FSRS spaced repetition, prerequisite skill graphs and a frozen scoring rubric behind one tool surface. The bridge between the mastery layer and any agent. **This is the upstream**; `kvnloo/tutor-mcp`, which this KB previously filed at 0★, is a fork of it. |
| **moodle-mcp** | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | **27** | Global (unplaced) | 🟢 **The permissive Moodle-side bridge this page has declared missing in every prior pass.** Rust on the official MCP SDK (`rmcp`), 163 commits, 22 tools — identity, courses, assignments (read *and* submit), forums, files-as-markdown, grades, schedule, messaging, quiz attempts — plus a `call_ws_function` escape hatch onto any Moodle web service. States validation live against **Moodle 3.7 → 5.x**. **27★ is not adoption and this cell does not pretend otherwise**: it is the most-reviewed member of a field whose ceiling is 27 stars, and it is an adopt-and-harden base, not an install. ⚠ Do not reach for `thc1006/moodle-mcp`, which ranks higher in search and is a 0★ fork 43 commits behind this. |

### Licence payloads read this pass

| Repo | Default branch | Grant file | Bytes | Family |
|---|---|---|---|---|
| HKUDS/DeepTutor | `main` | `LICENSE` | 11,408 | Apache-2.0 |
| THU-MAIC/OpenMAIC | `main` | `LICENSE` | 1,065 | MIT |
| DaRL-GenAI/instructional_agents | `main` | `LICENSE` | 1,067 | MIT |
| vishalsachdev/canvas-mcp | `main` | `LICENSE` | 1,071 | MIT |
| Li-Evan/Bloom | `main` | `LICENSE` | 1,069 | MIT |
| CAHLR/OATutor | `main` | `LICENSE` | 1,105 | MIT |
| Open-TutorAi/open-tutor-ai-CE | `main` | `LICENSE` | 1,531 | BSD-3-Clause (custom copyright line, 3 clauses + no-endorsement) |
| ai-shifu/ai-shifu | `main` | `LICENSE.txt` | 11,342 | Apache-2.0 — canonical **−15 B**, fully explained: the appendix placeholder `[yyyy] [name of copyright owner]` (32 ch) is filled in as `2024 ai-shifu.com` (17 ch). Genuine, unmodified terms. |
| GeminiLight/gen-mentor | `main` | `LICENSE` | 7,048 | CC0 1.0 Universal |
| ArnaudGuiovanna/tutor-mcp | `main` | `LICENSE` | 1,073 | MIT |
| haolpku/Omni-Edu | `main` | `LICENSE` | 11,358 | Apache-2.0 — stock, unmodified, appendix placeholders left in place. **Code only**; README: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* |
| G36maid/moodle-mcp | `main` | `LICENSE` | 1,064 | MIT — `Copyright (c) 2026 G36maid`, matching the namespace. The fork at `thc1006/moodle-mcp` carries **this same copyright line**, which is how the fork was caught before publication. |
| THU-MAIC/OpenMAIC → `packages/mathml2omml/LICENSE` | `main` | `LICENSE` | 7,652 | 🔴 **LGPL-3.0-or-later** — inside the MIT repository above. `package.json` declares `"license": "LGPL-3.0-or-later"` for `mathml2omml` v0.5.0, the root manifest declares it `"workspace:*"`, and `build:packages` compiles it as step one. |

## 🔴 The licence unit is the dependency graph, not the repository

Three of this page's rows carry a permissive badge over a tree that contains obligations the badge does not mention. All three were read at first hand at p652.

| Row | Badge | What is actually in the tree | What it means |
|---|---|---|---|
| **OpenMAIC** (42.7k★) | MIT | `packages/mathml2omml` is **LGPL-3.0-or-later** (7,652 B payload; `"license"` field verbatim in its `package.json`), declared `"workspace:*"` in the root manifest and built as the **first step** of `build:packages`. `packages/pptxgenjs` is MIT and fine. | A deliverable built from OpenMAIC **links an LGPL-3.0-or-later component**. Stated precisely, because over-reaction is the risk in both directions: LGPL-3.0 is not the GPL and does not make the whole application copyleft. It does require that the component stay *replaceable* with its source available, and "or-later" means a client cannot freeze the version of the terms. For a bundled, transpiled JS component in a shipped web app, replaceability is an engineering requirement, not a formality. Workable — but it must be designed in, and the licence badge gives no hint of it. |
| **OmniEdu** (590★) | Apache-2.0 | The payload is stock Apache-2.0 and covers the **code**. The README grants nothing for the weights: *"Model weights and third-party datasets and benchmarks retain their respective licenses."* Backbones are Qwen. | The artefact a client actually deploys — the weights — has **no named grant anywhere in the repository**. `huggingface.co` does not resolve under this session's network policy, so the cards could not be read. The toolkit and training code are unambiguously usable; the weights are an open question. |
| **open-moodle** (not filed, 0★) | MIT | Depends on **PyMuPDF (AGPL-3.0)** for PDF text extraction, stated in its own README. | An AGPL dependency in a network-served agent is the most consequential copyleft on this shelf. The dependency sets the obligation, not the repository. |

**The rule:** reading `LICENSE` is necessary and not sufficient. Read the manifests — `package.json`, `pyproject.toml`, `Cargo.toml` — and for a model, read the weight card. Four of the five grant-defect classes this base has catalogued would pass a licence-badge check.

## 🔴 Corrections to rows this KB previously published

These are not new findings — they are errors in data this knowledge base was already serving. Each was re-measured first-hand this pass.

| Row | Was published as | Measured 2026-11-04 | Why it matters |
|---|---|---|---|
| `kvnloo/tutor-mcp` | "MIT, **0 ★**, no adoption, no external review — watch it; do not start a client engagement on it" | **A fork.** The repository page states "forked from ArnaudGuiovanna/tutor-mcp". The upstream has **96 ★ / 13 forks**; the fork has 0 / 0. | The verdict was right about the address and wrong about the project. Both carry an identical 1,073 B MIT payload and an identical description, so every channel this KB measures agreed — only the fork notice separates them, and it lives on the page. The upstream is now filed above. `intel/trends.md` **T9** cited the 0-star figure as evidence that knowledge tracing is commercially immature; **that specific evidence is withdrawn** (the broader claim stands on pyKT 457★ and OATutor 276★). |
| `DaRL-GenAI/instructional_agents` | Apache-2.0 | **MIT** (payload 1,067 B, title `MIT License`) | Wrong grant named. Both are permissive, so the risk is low — but the cell was wrong. |
| `GeminiLight/awesome-ai-llm4education` | MIT, 1.5k ★ | **No licence file at all**, 221 ★ | A repo with no grant is *not* MIT. Building on it assumes a permission that was never given. Star count inflated 6.8×. |
| `mwasifanwar/eduadapt-ai` | MIT, ~150 ★ | **No licence file at all**, 26 ★ | Same defect: a false permissive grant. 26 stars is not an adopted project. Removed from this shelf. |
| `Open-TutorAi/open-tutor-ai-CE` | ~800 ★ | **116 ★** | Inflated 6.9×. Licence (BSD-3-Clause) was correct. |
| `HKUDS/DeepTutor` | 22k–24k ★ | **55,000 ★** | Understated by more than half. The row was stale, not wrong in kind. |

**The pattern:** two rows asserted a permissive licence that does not exist in the repository; four of five star counts were wrong in the same direction (inflated) except DeepTutor; and one row measured the wrong address entirely. Star counts on this shelf should be treated as measured-on-date, never carried forward.

🟢 **And the counter-result, from p651:** every one of the seven licence payloads above was re-read from bytes one pass after being measured, and all seven reproduced exactly; DeepTutor (55.0k ★) and OpenMAIC (42.7k ★) both re-measured to the published figure. The inflation was in values *carried forward from an unverified pipeline*, not in measurement itself. **Measured-and-dated holds; carried-forward does not.**

## 🟡 Found, real, and deliberately not filed

Recorded so a later pass does not re-spend the search — and so absence is not mistaken for a gap.

| Repo | Licence | Stars | Why not filed |
|---|---|---|---|
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **CC BY-SA 4.0** (1,230 B) | **949** | The highest-starred novel education-agent asset found by this base, and the licence is the reason it is not above. 165 skills across 20 domains in Agent Skills format plus an MCP server with 157 tools and 165 prompts. **ShareAlike**: a derivative skill library must itself be CC BY-SA, which rules out folding it into a proprietary deliverable. Usable as-is with attribution — not usable as a base for closed IP. It is also content and prompts, not software. |
| [virtualryder/edu-ai-agents](https://github.com/virtualryder/edu-ai-agents) | **modified MIT** (832 B) | 4 | Shaped exactly like this KB's governance gap (8 governed Bedrock workflows, deny-by-default authz, PII masking, human-in-the-loop, tamper-evident audit, FERPA/COPPA/IDEA-504/ADA-aligned) and disqualified twice over. 4 stars is not adoption; and the payload carries MIT's permission and notice paragraphs verbatim then **replaces MIT's limitation-of-liability paragraph** with a bespoke disclaimer — "IN NO EVENT SHALL THE AUTHORS … BE LIABLE" appears nowhere in the file. Read it for the workflow taxonomy, not for the code. |
| [mthatipamula/educational-assessment-ai-agent-platform](https://github.com/mthatipamula/educational-assessment-ai-agent-platform) | **no licence file** | — | The closest match this base has found to its own declared assessment gap: standards-aligned item authoring with RAG and self-review, rubric scoring with human review, sandboxed code grading. No grant file on any probed filename, so there is no permission to build on it. |
| [luffycodes/Tutorbot-Spock](https://github.com/luffycodes/Tutorbot-Spock) | **no licence file** | 56 | Learning-science-grounded tutoring chatbot. No grant on any of eight probed filenames on the real default branch. |
| [Micel357/Edu-mentor-AI](https://github.com/Micel357/Edu-mentor-AI) | **no licence file** | — | **LATAM-placed on documentary evidence** — Portuguese-language multi-agent pedagogical system from the Residência Tecnológica at Porto Digital, Recife, Brazil, Accenture-mentored, named in its own README. Real, placed, and unusable: no grant. |
| [kvnloo/tutor-mcp](https://github.com/kvnloo/tutor-mcp) | MIT (1,073 B) | **0** | A **fork** of `ArnaudGuiovanna/tutor-mcp`, which is now filed above at 96★. Kept in this table only so the address this KB previously published resolves to the right explanation. |
| [thc1006/moodle-mcp](https://github.com/thc1006/moodle-mcp) | MIT (1,064 B) | **0** | 🔴 **A fork of `G36maid/moodle-mcp`, 43 commits behind it, and the top search result for "Moodle MCP server".** Caught before publication at p652 by the cheapest channel available: the copyright line inside its own grant payload reads `G36maid`, not `thc1006`. A copyright holder who is not the namespace owner is a fork signal readable from `raw.githubusercontent.com` with one `curl` — in front of the fork notice, which needs a page fetch. |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | **AGPL-3.0 (34,523 B)** | 1 | Open-core, not permissive. Paid "Premium Plugins" (Advanced Reporting, User Analytics, User Directory, Compliance Pack) sold separately with terms not stated. 🔴 **Secondary summaries mischaracterise this as a bespoke source-available licence** — "free use, modify the source, but no closed-source competing repackaging". That is AGPL-3.0's terms restated in marketing language, and for a network-served agent AGPL is the heaviest copyleft on this shelf. |
| [GhaithAlHallak8/moodler-mcp](https://github.com/GhaithAlHallak8/moodler-mcp) | MIT (1,072 B) | 4 | Real and well-shaped — browser SSO to a locally-stored token, student writes and teacher grading **off by default** behind env flags — and 4 stars is not adoption. Worth watching; it has the safest default posture in the Moodle field. Instructor tools are self-described experimental. |
| [AnonymousOnyx22/moodle-student-mcp](https://github.com/AnonymousOnyx22/moodle-student-mcp) (0★, TypeScript, read-only), [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) (0★, Go, MCP+REST), [duck-5/moodle-mcp](https://github.com/duck-5/moodle-mcp) (0★, Python, OpenAPI bridge, Tel Aviv University config), [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) (0★, Python, read-only, ⚠ AGPL PyMuPDF dep) | all MIT (1,063–1,088 B) | 0 | The rest of the permissive Moodle field, measured so the search is not re-spent. All four grants read from bytes. None has external review. Recorded because **the shape of the field is the finding** — see the gap note below. |
| [microsoft/LLM-Rubric](https://github.com/microsoft/LLM-Rubric) | MIT (1,141 B) | 45 | Permissive, credible owner, **not education**. Rubric dimensions answered by an LLM, then calibrated to human judges' ratings by a small neural network; validated on dialogue systems (naturalness, conciseness, citation quality). ACL 2024. The calibration-to-human-raters mechanism is the transferable part and the nearest permissive primitive to this base's assessment gap. |
| [jacobphillips99/protorubric](https://github.com/jacobphillips99/protorubric) | 🔴 **self-contradictory** | 0 | YAML/code rubrics, LLM-as-judge, dependent multi-step requirements. **The payload is 11,357 B of Apache-2.0; the README's licence section says MIT.** Two grants in one repository is an unresolved permission, not a permissive project. |

## Agents by function

### Personalised tutoring
- **DeepTutor** — the default choice. Persistent learner model is the differentiator; a session chatbot is not a substitute.
- **Bloom** — lighter, pedagogy-led, and it ships as a Claude Code skill, which makes it the fastest thing here to demo.
- **OATutor** — structured BKT tutoring with LTI. Choose it when the client wants explainable mastery estimates rather than free-form dialogue, especially in maths.
- **Open TutorAI CE** — the only one with voice + avatar out of the box.
- **GenMentor** — goal-first rather than curriculum-first: the learner names an outcome and the agents work backwards to a session plan. Choose it when the client's learners are adults with a job-shaped goal, not students following a syllabus.

### Classroom simulation
- **OpenMAIC** — unique on this shelf: it simulates *peers*, not just a tutor. AI classmates that disagree create discussion dynamics a one-to-one tutor cannot.

### Teaching-workload automation
- **Instructional Agents** — full ADDIE cycle to slides and assessments. The natural fit where a client has a shortage of instructional designers rather than a shortage of teachers.
- **AI-Shifu** — the authoring end rather than the delivery end: capture a subject expert's intent once, generate an adaptive course from it, embed it in the client's own portal. Apache-2.0, so the generated product can be commercial.

### Mastery and retention
- **tutor-mcp** — the only row here that packages Bayesian Knowledge Tracing *and* FSRS spaced repetition behind a single MCP tool surface. It is the bridge between the mastery layer (`pykt-toolkit`, `fsrs-rs` in `repos/foundations.md`) and any agent above. See `compose/patterns.md` **P6**.

### LMS integration
- **canvas-mcp** — the bridge layer for Canvas, which dominates North American higher education. Any of the tutors above reaches real enrolment, assignment and grade data through an MCP server like this one. 317★.
- **moodle-mcp** — the same job for Moodle, which dominates LATAM and much of EMEA. 27★. The asymmetry between those two numbers is the single most actionable fact on this page; see the gap note below.

### Model layer
- **OmniEdu** — the only row here that is not an agent. When a client needs the *model* to know the curriculum rather than the *prompt* to carry it — sovereign deployment, offline deployment, or K-12 subject grounding that a general model guesses at — this is the base. The 9B FP8 checkpoint is ~11 GiB, which puts curriculum-grounded tutoring on a single GPU. Gate on the weight licence first.

## 🔴 Open gaps on this page — stated so they are not re-discovered

- 🟢 **The Moodle gap is restated, and it is a different kind of gap than this page has been recording.** Every prior pass declared that no permissively-licensed Moodle-side agent was found. p652 searched the category properly and found **seven, all MIT, in five languages** — and the entire field tops out at **27★**, against `canvas-mcp`'s **317★** for the same job on Canvas. So: **not a supply gap; a consolidation and adoption gap.** Six of the eight Moodle servers measured have ≤4 stars; none has external review at any meaningful scale. The consequence for an engagement is the opposite of what "no permissive agent exists" implied — the move is to adopt `G36maid/moodle-mcp` and harden it upstream, which is weeks of work, not to build from zero. The ~12× investment asymmetry against the LMS that dominates LATAM and EMEA, and in favour of the one that dominates North American HE, is itself a finding: open source has invested in Canvas-shaped institutions. Full measured field in `agents/trending.md` (p652); engagement shape in `compose/patterns.md` **P8**.
- **Six of twelve rows are unplaced by region.** p652 added one placed row (OmniEdu → APAC, on the paper's institutional attribution: Peking University, UCAS, Zhongguancun Academy) and one unplaced (`moodle-mcp`, whose author states no institution). The ratio has not improved, and the reason is unchanged: most repositories state neither an institution nor a jurisdiction, and author names and README language are deliberately **not** used as placement channels because this base has measured that signal mis-placing lusophone and hispanophone projects.
- **Five of ten rows are unplaced by region.** `instructional_agents`, `canvas-mcp`, `Bloom`, `open-tutor-ai-CE` and `gen-mentor` are filed `Global` because no documentary basis for a region was found — not because they are global projects. Owner-namespace and licence-copyright probes are weak placement channels; this is recorded as an informed gap, not inferred into a region.
- **The assessment gap is now a three-pass, two-strategy finding, which makes it a property of the field rather than of the searching.** Earlier passes recorded no permissive assessment or grading agent. p651 found two real education-specific ones — `mthatipamula/educational-assessment-ai-agent-platform` and the assessment workflow inside `virtualryder/edu-ai-agents` — and **neither carries a usable grant** (no licence file; truncated MIT). p652 searched the adjacent category instead, general rubric-scoring libraries, and found exactly one permissive and credible option, `microsoft/LLM-Rubric` (MIT, 45★) — **which is not education-specific at all**, plus `protorubric`, whose payload says Apache-2.0 while its README says MIT. **Restated:** there is no permissively-licensed, education-specific assessment agent at any adoption; there is one permissive general rubric primitive worth pointing at education, whose transferable idea is calibrating LLM rubric scores against human raters. This is the one place on this shelf where building beats adopting.
- **Proctoring and assessment *integrity* remain genuinely unsupplied under a permissive licence.** This is the most regulated use case in education AI (EU AI Act high-risk; emotion recognition in schools banned since February 2025). Nothing found in any pass.
- 🟢 **The model layer below the agents has opened, and it changes what "offline" and "sovereign" cost.** Until p652 every row on this page was an application that called somebody's general model. `OmniEdu` is a K-12-grounded model family in three sizes with FP8 checkpoints 37–44% smaller than BF16 — the 9B at ~11 GiB, the 27B at ~28 GiB. That moves curriculum-grounded tutoring onto single-GPU, in-jurisdiction, no-egress hardware, which is the architecture both EMEA public education and Sub-Saharan African deployments actually require. The gap that remains is specific and gating: **the weights carry no named licence in the repository**, and `huggingface.co` does not resolve under this session's network policy, so the cards are unread. Nobody should deploy the weights on this page's authority.
- **One region now has two placement channels and still almost nothing placed.** AI-Shifu was placed to APAC on its README's institutional attribution, and `thm-mni-ii/feedbacksystem` to EMEA on its licence payload's copyright line. Both channels are documentary and cheap. They still leave five of ten rows unplaced, because most repositories state neither. Author names and README language are deliberately **not** used: this base has measured that signal mis-placing lusophone and hispanophone projects.
