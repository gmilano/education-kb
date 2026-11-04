---
industry: education
region: Global
updated: 2026-11-04
---

# 🎯 AI agents — Education

> Open source AI agents for the education industry. Focus: MIT / Apache-2.0 / BSD — the licences Globant can build commercial derivatives on.
> Every row below was verified on 2026-11-04: existence via `git ls-remote --symref` (real default branch), licence by reading the grant payload from `raw.githubusercontent.com`, stars from the repository page.

## The agents — 10 verified rows

Ten rows. That is how many real, adopted, permissively-licensed education agents this base has verified — not a target, a count. Three were added on 2026-11-04 (p651): AI-Shifu, GenMentor and the **upstream** `tutor-mcp`.

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 55,000 | APAC | Lifelong personalised tutoring. Persistent student model across sessions, proactive check-ins, multi-mode delivery. The most-adopted education agent in open source. arXiv:2604.26962. University of Hong Kong (HKUDS). |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | 42,700 | APAC | Open Multi-Agent Interactive Classroom. Turns a topic or uploaded document into a live lesson delivered by AI teachers *and* AI classmates that speak, draw on a whiteboard and debate. Slides, quizzes, simulations, PBL. LangGraph orchestration. **v1.4.0 released 2026-11-04.** Tsinghua. |
| **Instructional Agents** | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | 490 | Global (unplaced) | Multi-agent ADDIE pipeline: syllabus → LaTeX slides → assessments, end to end. Roles: Teaching Faculty, Instructional Designer, TA, Coordinator. EACL 2026 Main. |
| **AI-Shifu** | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 | 331 | APAC | Course **authoring** plus adaptive delivery — a different job from tutoring. An instructor supplies expertise and teaching intent once; the system generates per-learner explanations, probing Q&A, and a course embeddable in a website or training portal. Docker self-hosting. Research Center of Intelligent Software Engineering, **Harbin Institute of Technology**. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 317 | Global (unplaced) | Canvas LMS MCP server exposing ~102–128 tools plus agent skills for students and educators. Works with Claude, Cursor, Codex. The cleanest path from an agent to a real institutional LMS. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 302 | Global (unplaced) | Private AI tutor built on Bloom's 2-sigma result for one-to-one instruction. Generates a course outline, then adapts each lesson to learner feedback and annotations. Runs as a Claude Code skill *or* a self-hosted web app. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | North America | Intelligent tutoring system with Bayesian Knowledge Tracing. ReactJS + Firebase, LTI for LMS integration, curated maths content library. UC Berkeley (CAHLR). Peer-reviewed, production-grade. |
| **GenMentor** | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 136 | Global (unplaced) | Goal-oriented tutoring: the learner states a goal, coordinated LLM agents refine it, measure the gap against the learner's background, schedule sessions, draft each session's reading and quiz, and update the profile from activity. WWW '25 Industry Track oral. ⚠️ `main` is a browser-only Next.js app; the paper's multi-agent Python implementation is on branch **`v0.1-demo`**. CC0 is a public-domain dedication, not a software licence — no patent or trademark grant. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | 116 | Global (unplaced) | Multimodal tutoring: voice, video and configurable 3D avatars. Docker-first, runs local LLMs via Ollama. arXiv:2602.07176. |
| **tutor-mcp** | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 96 | Global (unplaced) | MCP server that turns any LLM into an intelligent tutoring system: Bayesian Knowledge Tracing, FSRS spaced repetition, prerequisite skill graphs and a frozen scoring rubric behind one tool surface. The bridge between the mastery layer and any agent. **This is the upstream**; `kvnloo/tutor-mcp`, which this KB previously filed at 0★, is a fork of it. |

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
- **canvas-mcp** — the bridge layer. Any of the tutors above reaches real enrolment, assignment and grade data through an MCP server like this one.

## 🔴 Open gaps on this page — stated so they are not re-discovered

- **No permissively-licensed Moodle-side agent of comparable standing.** `canvas-mcp` covers Canvas at 317 ★; the Moodle equivalent at similar adoption and a permissive grant was not found this pass. Moodle is the dominant LMS in LATAM and much of EMEA, so this is a real hole in exactly the regions Globant sells into.
- **Five of ten rows are unplaced by region.** `instructional_agents`, `canvas-mcp`, `Bloom`, `open-tutor-ai-CE` and `gen-mentor` are filed `Global` because no documentary basis for a region was found — not because they are global projects. Owner-namespace and licence-copyright probes are weak placement channels; this is recorded as an informed gap, not inferred into a region.
- **The assessment gap has changed category: it is a licence gap, not a supply gap.** Earlier passes recorded no permissive assessment or grading agent and treated the supply as absent. p651 found two real ones — `mthatipamula/educational-assessment-ai-agent-platform` (rubric scoring with human review, sandboxed code grading) and the assessment workflow inside `virtualryder/edu-ai-agents` — and **neither carries a usable grant** (no licence file; truncated MIT). The builders exist and are not licensing their work. The fix is one upstream commit, not a new project; it is worth asking for.
- **Proctoring and assessment *integrity* remain genuinely unsupplied under a permissive licence.** This is the most regulated use case in education AI (EU AI Act high-risk; emotion recognition in schools banned since February 2025). Nothing found in any pass.
- **One region now has two placement channels and still almost nothing placed.** AI-Shifu was placed to APAC on its README's institutional attribution, and `thm-mni-ii/feedbacksystem` to EMEA on its licence payload's copyright line. Both channels are documentary and cheap. They still leave five of ten rows unplaced, because most repositories state neither. Author names and README language are deliberately **not** used: this base has measured that signal mis-placing lusophone and hispanophone projects.
