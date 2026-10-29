---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI Agents — Curated Shelf

**Pass `p526` · 2026-10-29.** Every row below was read first-hand from its GitHub
repository page during this pass. Star counts, licences and descriptions are as
served on 2026-10-29. No row is a header, a placeholder or an example.

> **Verification channel this pass:** `curl` against `github.com` and
> `api.github.com` returns **HTTP 403** from the session proxy for any repository
> not attached to the session, so repository pages were read through the
> page-fetch channel instead. That is a weaker channel than the API — it gives
> rounded star counts (`48.9k`, not `48,913`) and does not always render the
> Languages or Releases widget. Where a release number appears below it was read
> from the README, and it is marked as such.

## Shelf — 10 verified education agents

| Agent | Repo | Licence | Stars | Region (origin) | What it does |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 48.9k | APAC (Univ. of Hong Kong, HKUDS lab) | "Lifelong Personalized Tutoring." Multi-agent tutor with persistent learner memory, learning paths and mastery gates. Python backend + Next.js 16 front end. README names **v1.7.0, 2026.10.28**. The largest open-source education agent on any shelf. |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | 41.7k | APAC (Tsinghua University, MAIC group) | "Open Multi-Agent Interactive Classroom" — a one-click immersive classroom staffed by multiple agent roles (lecturer, peer, assistant). TypeScript / Next.js / React. README names **v1.3.0, 2026-10-29** adding a knowledge base and a "Pro workbench". |
| **k12-teacher-skills** | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 | 601 | North America (Anthropic, with Learning Commons) | Agent *skills* plus **eval rubrics** for K-12 teacher workflows. The rubrics matter more than the skills: they are a published yardstick for "is this agent pedagogically acceptable", which almost nothing else in this space ships. |
| **anki-mcp-server** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 538 | unplaced — no location on the org profile | MCP server exposing Anki (spaced repetition) to any MCP-speaking assistant. README gives version **0.27.0**. This is the retention half of a tutoring stack: the agent teaches, Anki makes it stick, and the learner keeps the deck. |
| **Educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | 387 | unplaced — no location on the author profile | Python package for generating educational content (MCQs, lesson plans, flashcards) with generative AI. README labels **v0.3.13 (October 2024)** as current, so treat it as a stable utility rather than an active project. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 308 | North America (author's org field: Univ. of Illinois Urbana-Champaign) | MCP server bridging assistants to **Canvas LMS**, with skills for both students and educators. README names **v1.16.0, October 2026**. Tool count is stated inconsistently on the repo page — "up to 102 tools" in About, "up to 128 tools" in the README. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 294 | unplaced this pass | Self-hostable private AI tutor: "reads how you actually learn and teaches the next lesson just for you." JavaScript. No releases cut. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America (UC Berkeley, CAHLR lab) | Open-source **Intelligent Tutoring System with Bayesian Knowledge Tracing**, ReactJS + Firebase. The one row on this shelf with a real, published mastery estimator rather than a prompt that claims to track mastery. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | **EMEA (Morocco** — stated on the org profile) | Community edition of an educational, collaborative AI platform; Python backend with a SvelteKit UI. 194 forks against 114 stars — unusually fork-heavy, which reads as deployment rather than stargazing. |
| **pedagogy-benchmark** | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | Global (org states an **LMIC** focus, no country) | Code for *"Benchmarking the Pedagogical Knowledge of Large Language Models"* — runs the **CDPK** and **SEND** benchmarks. Thirteen stars and the most useful repo here for a procurement conversation: it is how you answer "which model actually knows how to teach". |

**Licence split:** 8 × MIT, 2 × Apache-2.0, 1 × BSD-3-Clause — all buildable.
*(DeepTutor and k12-teacher-skills are the Apache-2.0 pair; Open TutorAI CE is the BSD row.)*

### Correction carried into this pass

Earlier passes on this base recorded **Open TutorAI CE as Apache-2.0**. The
repository page served **BSD-3-Clause** on 2026-10-29. BSD-3-Clause is still
permissive and still buildable, so nothing downstream changes, but the cell was
wrong and is now right.

## ⚠️ Licence traps — repos that look permissive and are not

These are education repositories a naive licence probe grades as buildable. They
are not. Each was read from the served licence text.

| Repo | Grades as | Actually | Why the trap works |
|---|---|---|---|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) · 2.1k★ | `MIT` | **Bespoke non-commercial** — the page badge itself reads *"PageLM Community License"* | The payload *opens* with the MIT sentence — *"Permission is hereby granted, free of charge…"* — then spends 8 KB taking it back: use limited to personal/educational/non-commercial research, **redistribution in source or binary form strictly prohibited**, and a **revenue-share agreement required before any commercial deployment**. A probe matching on body sentences sees MIT. A probe reading the **title line** sees the truth. |
| [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) | `unknown` | **Elastic-2.0** | 340★ higher-ed advising CRM and conversational platform. Elastic-2.0 forbids providing the product as a hosted/managed service — which is exactly what a studio engagement would do. Not usable as a base. |
| [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) · 5.1k★ | `CC-BY-4.0` | **CC-BY-NC-4.0** — the page badge reads `CC BY-NC 4.0` correctly, so this trap is **entirely probe-side** | The title line reads *"Attribution-**NonCommercial** 4.0 International"*; the body contains the BY-4.0 boilerplate. Dropping `NonCommercial` from the family name turns an unusable corpus into a usable one on paper only. |

**Rule for this base:** grade a licence from the **title block** of the licence
file, never from a sentence in the body, and never drop a `NonCommercial`
qualifier from a family name. Also check `LICENSE.txt` and `LICENSE.md`, not just
`LICENSE` — [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
(107.5k★) serves its grant at `LICENSE.txt` — and the repository page does **not**
name a licence type at all, so a probe reading one filename files a six-figure-star
asset as ungranted.

## What is still missing

Stated rather than left silent, because an unwritten gap looks like coverage:

- **No LATAM-origin education agent.** The region's open-source strength is in
  school management, not agents — see
  [portabilis/i-educar](https://github.com/portabilis/i-educar) in
  [`../repos/foundations.md`](../repos/foundations.md). Nothing on the agent legs
  this pass was LATAM-placed.
- **One EMEA-placed agent** (Open TutorAI CE, Morocco) against nine elsewhere.
- **No open-source agent for assessment integrity.** The credible tooling is
  classical, not agentic — [dodona-edu/dolos](https://github.com/dodona-edu/dolos)
  does code-similarity detection well and has no LLM in it.
- **No open-source SIS/advising agent under a permissive licence.** The only
  serious candidate found (`advisingapp`) is Elastic-2.0.
