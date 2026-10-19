---
industry: education
region: Global
updated: 2026-10-19
---

# Top open source AI agents — education

**Pass 316 · 2026-10-19.** Fifteen rows, fifteen real repos. No header rows, no placeholders, no
example data.

Verification method, unchanged from pass 315: `curl -sI` to github.com returns **403 at this
session's proxy**, so every row was checked by loading the repository page and reading the licence
label, star count and commit count GitHub itself renders. The **Checked** column says whether that
reading happened in *this* pass (p316) or earlier the same day (p315).

Star counts move; treat them as a size signal, not a metric.

## The table

| Agent | Repo | Licence | ★ | Checked | What it does | Use it for |
|---|---|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 41.7k | p316 | Lifelong personalised tutoring agent; v1.6.15 (2026-10-19), 2,935 commits, paper arXiv 2604.26962 | The strongest permissive starting point for a tutor product |
| smolagents | https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p315 | Minimal library for agents that think in code | The agent runtime under a tutor when you want small and auditable |
| FSRS4Anki | https://github.com/open-spaced-repetition/fsrs4anki | MIT | 4.1k | p315 | Free Spaced Repetition Scheduler as an Anki scheduler | Retention scheduling — the review-timing half of a tutor |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | p315 | Assigning, collecting and autograding Jupyter notebooks | Grading automation in any notebook-based curriculum |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 878 | p316 | 165 evidence-grounded teaching skills (pedagogy, assessment, curriculum) for Claude/Codex/Hermes; 149 commits | Prompt and pedagogy assets — **not** a code dependency, see caveat |
| iblai/os | https://github.com/iblai/os | MIT | 821 | p316 | Agent platform (Next.js → web/desktop/mobile) with chat, voice, SSO; 3,518 commits | A front end only — the backend is **not** in the repo, see caveat |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT | 520 | p316 | MCP server exposing the Anki flashcard app to any LLM client; 258 commits | Wiring a real spaced-repetition store to an agent without writing a scheduler |
| Educhain | https://github.com/satvik314/educhain | MIT | 387 | p315 | Python package generating MCQs, lesson plans and flashcards with LLMs | Content-generation pipelines behind an authoring tool |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 289 | p316 | Socratic adaptive tutor shipped as both portable agent skills and a self-hostable React/FastAPI app; 76 commits | The clearest worked example of the skill-plus-app delivery shape |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 268 | p315 | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase), UC Berkeley CAHLR | Mastery modelling / hint sequencing where you must explain the pedagogy |
| otter-grader | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | 161 | p315 | Python and R autograding with containerised execution | Autograding where submissions must run sandboxed |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 145 | p316 | Local-first block-based adaptive workspace: upload material → notes, quizzes, flashcards, tutor; 10+ LLM providers, 194 commits | An offline/on-prem tutor shell when data cannot leave the building |
| gen-mentor | https://github.com/GeminiLight/gen-mentor | CC0-1.0 | 135 | p316 | LLM multi-agent framework for goal-oriented learning in an ITS; WWW '25 oral, arXiv 2501.15749; 91 commits | A peer-reviewed multi-agent ITS architecture you can cite in a bid |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 111 | p315 | Educational collaborative AI tutoring platform; arXiv 2602.07176 (Feb 2026) | An academically documented tutor platform you can fork and cite |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 52 | p316 | MCP server that turns any LLM into an ITS: skill graph, BKT, FSRS, prerequisite rules, narrative memory; SQLite local / PostgreSQL hosted; 467 commits | **The find of this pass** — see below |

## tutor-mcp is the most consequential new row

Everything this KB has argued for three passes — that the LLM should explain while a deterministic
engine decides, that mastery estimation (BKT) and retention scheduling (FSRS) are the real
differentiators — `ArnaudGuiovanna/tutor-mcp` implements in one MIT-licensed server with 467
commits. Its own README states the principle as **"Generative teaching. Deterministic pedagogy."**

It ships the skill graph, BKT, FSRS, prerequisite gating and a cross-session narrative memory layer,
runs over stdio with SQLite locally or HTTPS + OAuth + PostgreSQL in an institutional profile, and
speaks MCP, so Claude Code, Claude Desktop, ChatGPT, Gemini CLI and others are clients for free.

**What it does not do: any LMS integration.** The README names no LTI, SCORM or xAPI support. The
gap this KB has declared for three passes — no open source agent speaks LTI natively — is
unchanged; tutor-mcp moves the pedagogy problem off the critical path and leaves the integration
problem exactly where it was.

## Caveats a studio lead should read before quoting any of these

- **`iblai/os` is open-core, not open source in the useful sense.** MIT, 821 ★, 3,518 commits — and
  its README says plainly: *"ibl.ai/os requires the ibl.ai backend platform for authentication, AI
  agent APIs, and data services. The backend is not included in this repository."* You can read and
  fork the client; you cannot self-host the product. It is in the table because it is a good
  reference front end and because a client who has heard "ibl.ai is MIT" needs this corrected.
- **`education-agent-skills` is CC BY-SA 4.0 — ShareAlike, and a content licence, not a code
  licence.** 878 ★ of genuinely useful pedagogy assets, but derivative teaching material must be
  released under the same terms. That is a live constraint on a client deliverable and belongs in
  the licence inventory before anyone pastes a skill into a proposal.
- **`gen-mentor` is CC0-1.0.** A public-domain dedication, so usable, but it is a paper-companion
  release (91 commits) with no warranty culture around it. Cite the architecture; do not take the
  dependency.
- **`Educhain` is 387 ★** — earlier passes of this KB recorded "~12k ★", which was wrong. Small and
  slow-moving: fine as a content helper, not a platform bet.
- **`DeepTutor` is the outlier in both directions.** 41.7k ★ and a release on 2026-10-19 make it the
  most active permissive tutor codebase in the sector; that velocity makes pinning a version
  mandatory. It now also has a paper (arXiv 2604.26962), which earlier passes did not record.
- **`Bloom`, `OpenTutor` and `anki-mcp-server` are small but honest.** 76, 194 and 258 commits
  respectively. They are reference shapes and composable parts, not platforms.
- **The three graders are BSD-3-Clause, not MIT.** Permissive, but the attribution clause is real.

## Dropped from the table this pass

- **`Ebimsv/AITutorAgent` (MIT, 15 ★, 4 commits)** carried a row in pass 315 as a "reference shape
  only" for the LangGraph tutorial → Q&A → evaluation loop. `tutor-mcp` is the same shape with 467
  commits, a real licence and a running server. Keeping a 4-commit repo in a table a client might
  read is a risk with no remaining upside. Removed; recorded in `agents/trending.md`.

## Rejected after verification — recorded so the next pass does not re-find them

- **`luffycodes/Tutorbot-Spock` — NO LICENCE FILE.** 56 ★, 8 commits, and genuinely notable work
  (CLASS, EMNLP 2023, arXiv 2305.13272; Pedagogical Alignment of LLMs, EMNLP 2024, arXiv 2402.05000).
  With no licence, default copyright applies and Globant cannot use it. **Read the papers, not the
  repo.**
- **`artcc/freelingo` — AGPL-3.0, 188 ★.** A real self-hosted AI language-learning platform, and a
  good one; it is in `verticals/solutions.md` as a platform, not here, because AGPL puts it on the
  copyleft side of this KB's architectural line.

## Licence split

MIT (8 — FSRS4Anki, iblai/os, anki-mcp-server, Educhain, Bloom, OATutor, OpenTutor, tutor-mcp),
BSD-3-Clause (3 — nbgrader, otter-grader, Open TutorAI CE), Apache-2.0 (2 — DeepTutor, smolagents),
CC0-1.0 (1 — gen-mentor), CC BY-SA 4.0 (1 — education-agent-skills).

**13 of 15 carry a permissive *software* licence Globant can build on commercially.** The two
exceptions are content/dedication licences (CC BY-SA 4.0, CC0-1.0) and are flagged in the caveats.
This remains the opposite of the platform tier in `verticals/solutions.md`, which is predominantly
copyleft — the split is the single most important structural fact about this industry's open source.

## What was searched and not found

- **No region-specific tutoring agent, again.** Searched specifically for education agents authored
  in EMEA, APAC and LATAM. The agent tier remains US/EU/China-authored or unplaced. Notably, several
  of the highest-starred repos under GitHub's `ai-tutor` topic are Chinese-language agent *skills*
  (`Miaotofu01/Study-Mate` 1.1k ★, `KeWang0622/kaogong-skill` 189 ★,
  `SimonsTang/feifei-companion` 108 ★) — APAC presence exists at the skill layer, not the platform
  layer. Regionally placed open source in this sector still sits in the *platform* tier (Sunbird for
  India, Richie for France, Kolibri across the global south).
- **No credible open source agent for assessment integrity / AI-detection.** Searched again this
  pass. What exists on GitHub is student-project proctoring (YOLO/OpenCV/MTCNN pipelines, Electron
  kiosk browsers), much of it stale or unlicensed, plus MOSS-style code-plagiarism detectors. No
  mature, adopted project. **Fourth consecutive pass declaring this gap** — and the published
  evidence on AI-text detection accuracy argues it should stay a gap rather than be filled.
- **No open source LTI 1.3 *agent*.** `pylti1.3` (MIT) remains the only solid library; tutor-mcp
  confirms the pattern by shipping MCP and no LTI. The glue is yours to write in every engagement.
