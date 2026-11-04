---
industry: education
region: Global
updated: 2026-11-04
---

# 🎯 AI agents — Education

> Open source AI agents for the education industry. Focus: MIT / Apache-2.0 / BSD — the licences Globant can build commercial derivatives on.
> Every row below was verified on 2026-11-04: existence via `git ls-remote --symref` (real default branch), licence by reading the grant payload from `raw.githubusercontent.com`, stars from the repository page.

## The agents — 7 verified rows

Seven rows. That is how many real, adopted, permissively-licensed education agents this pass could verify — not a target, a count.

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 55,000 | APAC | Lifelong personalised tutoring. Persistent student model across sessions, proactive check-ins, multi-mode delivery. The most-adopted education agent in open source. arXiv:2604.26962. University of Hong Kong (HKUDS). |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | 42,700 | APAC | Open Multi-Agent Interactive Classroom. Turns a topic or uploaded document into a live lesson delivered by AI teachers *and* AI classmates that speak, draw on a whiteboard and debate. Slides, quizzes, simulations, PBL. LangGraph orchestration. **v1.4.0 released 2026-11-04.** Tsinghua. |
| **Instructional Agents** | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | **MIT** | 490 | Global (unplaced) | Multi-agent ADDIE pipeline: syllabus → LaTeX slides → assessments, end to end. Roles: Teaching Faculty, Instructional Designer, TA, Coordinator. EACL 2026 Main. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 317 | Global (unplaced) | Canvas LMS MCP server exposing ~102–128 tools plus agent skills for students and educators. Works with Claude, Cursor, Codex. The cleanest path from an agent to a real institutional LMS. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 302 | Global (unplaced) | Private AI tutor built on Bloom's 2-sigma result for one-to-one instruction. Generates a course outline, then adapts each lesson to learner feedback and annotations. Runs as a Claude Code skill *or* a self-hosted web app. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 276 | North America | Intelligent tutoring system with Bayesian Knowledge Tracing. ReactJS + Firebase, LTI for LMS integration, curated maths content library. UC Berkeley (CAHLR). Peer-reviewed, production-grade. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause | 116 | Global (unplaced) | Multimodal tutoring: voice, video and configurable 3D avatars. Docker-first, runs local LLMs via Ollama. arXiv:2602.07176. |

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

## 🔴 Corrections to rows this KB previously published

These are not new findings — they are errors in data this knowledge base was already serving. Each was re-measured first-hand this pass.

| Row | Was published as | Measured 2026-11-04 | Why it matters |
|---|---|---|---|
| `DaRL-GenAI/instructional_agents` | Apache-2.0 | **MIT** (payload 1,067 B, title `MIT License`) | Wrong grant named. Both are permissive, so the risk is low — but the cell was wrong. |
| `GeminiLight/awesome-ai-llm4education` | MIT, 1.5k ★ | **No licence file at all**, 221 ★ | A repo with no grant is *not* MIT. Building on it assumes a permission that was never given. Star count inflated 6.8×. |
| `mwasifanwar/eduadapt-ai` | MIT, ~150 ★ | **No licence file at all**, 26 ★ | Same defect: a false permissive grant. 26 stars is not an adopted project. Removed from this shelf. |
| `Open-TutorAi/open-tutor-ai-CE` | ~800 ★ | **116 ★** | Inflated 6.9×. Licence (BSD-3-Clause) was correct. |
| `HKUDS/DeepTutor` | 22k–24k ★ | **55,000 ★** | Understated by more than half. The row was stale, not wrong in kind. |

**The pattern:** two rows asserted a permissive licence that does not exist in the repository, and four of five star counts were wrong in the same direction (inflated) except DeepTutor. Star counts on this shelf should be treated as measured-on-date, never carried forward.

## 🟡 Found, real, and deliberately not filed

Recorded so a later pass does not re-spend the search — and so absence is not mistaken for a gap.

| Repo | Licence | Stars | Why not filed |
|---|---|---|---|
| [kvnloo/tutor-mcp](https://github.com/kvnloo/tutor-mcp) | MIT (1,073 B) | **0** | Genuinely interesting design — MCP server combining Bayesian Knowledge Tracing, FSRS spaced repetition, prerequisite skill graphs and a frozen scoring rubric. But zero stars, zero forks: no adoption, no external review. Watch it; do not start a client engagement on it. |

## Agents by function

### Personalised tutoring
- **DeepTutor** — the default choice. Persistent learner model is the differentiator; a session chatbot is not a substitute.
- **Bloom** — lighter, pedagogy-led, and it ships as a Claude Code skill, which makes it the fastest thing here to demo.
- **OATutor** — structured BKT tutoring with LTI. Choose it when the client wants explainable mastery estimates rather than free-form dialogue, especially in maths.
- **Open TutorAI CE** — the only one with voice + avatar out of the box.

### Classroom simulation
- **OpenMAIC** — unique on this shelf: it simulates *peers*, not just a tutor. AI classmates that disagree create discussion dynamics a one-to-one tutor cannot.

### Teaching-workload automation
- **Instructional Agents** — full ADDIE cycle to slides and assessments. The natural fit where a client has a shortage of instructional designers rather than a shortage of teachers.

### LMS integration
- **canvas-mcp** — the bridge layer. Any of the tutors above reaches real enrolment, assignment and grade data through an MCP server like this one.

## 🔴 Open gaps on this page — stated so they are not re-discovered

- **No permissively-licensed Moodle-side agent of comparable standing.** `canvas-mcp` covers Canvas at 317 ★; the Moodle equivalent at similar adoption and a permissive grant was not found this pass. Moodle is the dominant LMS in LATAM and much of EMEA, so this is a real hole in exactly the regions Globant sells into.
- **Four of seven rows are unplaced by region.** `instructional_agents`, `canvas-mcp`, `Bloom` and `open-tutor-ai-CE` are filed `Global` because no documentary basis for a region was found — not because they are global projects. Owner-namespace and licence-copyright probes are weak placement channels; this is recorded as an informed gap, not inferred into a region.
- **No open source assessment-integrity or proctoring agent found under a permissive licence.** This is the single most regulated use case in education AI (EU AI Act high-risk; emotion recognition in schools banned since February 2025), and open source supply appears absent. Verified absence would need a dedicated pass.
