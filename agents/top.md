---
industry: education
region: Global
updated: 2026-10-29
---

# Education AI Agents — Curated Shelf

**Pass `p528` · 2026-10-29.** Fourteen real agents, every row read first-hand.
No row is a header, a placeholder or an example.

> **`p528` is a same-day second pass** — `p527` committed at 11:58 UTC, this one
> ran from 12:47. Nothing on a star counter moves in fifty minutes, so this pass
> spent its budget on two things instead: **promoting addresses this base had
> already verified and never shelved**, and **finishing the Moodle census**.
> The headline is uncomfortable and it is the useful kind:
> 🔴 **the supply problem this pass was promotion, not discovery.** Two addresses
> the base verified itself — [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem)
> (`p420`, 24 Oct, recorded verbatim as *"the one new address worth shelving"*)
> and [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills)
> (`p466`/`p492`/`p520`, **926★**) — were absent from this shelf, **and the first
> of them directly contradicted the LATAM gap note printed below it.** Both are
> now on the file. See [§ Promotion debt](#-promotion-debt--what-p528-actually-fixed).

> **Verification channel — improved this pass, and it matters.** `curl` to
> `github.com` and `api.github.com` still returns **HTTP 403** from the session
> proxy for any repository not attached to the session, so star counts remain
> **rounded page values** (`49.0k`, not `49,013`). But
> **`raw.githubusercontent.com` is *not* blocked.** Every licence below was
> therefore read from **the licence file's own title block**, fetched directly —
> not from the sidebar badge, and not from a search result. That is the stronger
> channel for the one field this base keeps getting burned on, and it is what
> turned up the new trap in [§ Licence traps](#-licence-traps--repos-that-look-permissive-and-are-not)
> and resolved the question `p526` left open on `frappe/education`.
>
> 🆕 **`p528` adds one step in front of that probe: confirm the repository
> resolves at all.** Fetch `README.md` on `main` *and* `master` before grading a
> licence. A repo that 404s on every path is **not** "ungranted" — it is **not
> there**, and filing it as ungranted puts a phantom in the census. This caught
> one this pass: see [§ Not ungranted — absent](#-not-ungranted--absent).

## Shelf — 14 verified education agents

| Agent | Repo | Licence (title block) | Stars | Region (origin) | What it does |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | **49.0k** | APAC (Univ. of Hong Kong, HKUDS lab) | "Lifelong Personalized Tutoring." Multi-agent tutor with persistent learner memory, learning paths and mastery gates. README names **v1.7.0, 2026.10.28**. 6.1k forks. The largest open-source education agent on any shelf. |
| **OpenMAIC** | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT | **41.8k** | APAC (Tsinghua University, MAIC group) | "Open Multi-Agent Interactive Classroom" — a one-click immersive classroom staffed by multiple agent roles (lecturer, peer, assistant). TypeScript / Next.js / React. News section names **v1.3.0, 2026-10-29**. 6.5k forks. |
| **k12-teacher-skills** | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 | 601 | North America (Anthropic, with Learning Commons) | Agent *skills* plus **eval rubrics** for K-12 teacher workflows. The rubrics matter more than the skills: they are a published yardstick for "is this agent pedagogically acceptable", which almost nothing else in this space ships. 108 forks. |
| **anki-mcp-server** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 538 | unplaced — no location on the org profile or in the copyright line | MCP server exposing Anki (spaced repetition) to any MCP-speaking assistant. README gives **0.27.0**. This is the retention half of a tutoring stack: the agent teaches, Anki makes it stick, and the learner keeps the deck. |
| 🆕 **lineage-skill** | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | Apache-2.0 | **462** | APAC — *inferred*, see note | "Distill videos, PDFs, transcripts, and notes into **source-backed** teacher Agent Skills." Ingests course video, audio, PDF and notes and emits a Skill that teaches in short lessons, questions the learner, marks the answers and tracks review over time. **70 forks.** The highest-starred *new* row this pass, and the only agent on this shelf whose output is traceable to the source material it was built from. |
| **Educhain** | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | 387 | **APAC (India)** — *newly placed*, see note | Python package for generating educational content (MCQs, lesson plans, flashcards) with generative AI. README labels **v0.3.13 (October 2024)** current, so treat it as a stable utility rather than an active project. 76 forks. |
| **canvas-mcp** | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 308 | North America (author's org field: Univ. of Illinois Urbana-Champaign) | MCP server bridging assistants to **Canvas LMS**, with skills for both students and educators. README names **v1.16.0, October 2026**, a security release. Tool count is still stated inconsistently — "up to 102 tools" in About, "up to 128 tools" in the README. 100 forks. |
| **Bloom** | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 294 | **APAC** — *newly placed, inferred*, see note | Self-hostable private AI tutor: "reads how you actually learn and teaches the next lesson just for you." Python/FastAPI + React. Packages Benjamin Bloom's 1984 2-sigma result as a Claude Code skill plus a web app. 44 forks, no releases cut. |
| **OATutor** | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America (UC Berkeley — copyright line reads *"Zachary A. Pardos (@zpardos) - CAHL research lab"*) | Open-source **Intelligent Tutoring System with Bayesian Knowledge Tracing**, ReactJS + Firebase. Still the one row on this shelf with a real, published mastery estimator rather than a prompt that claims to track mastery. 164 forks. |
| **Open TutorAI CE** | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | **EMEA (Morocco** — stated on the org profile) | Community edition of an educational, collaborative AI platform; Python backend with a SvelteKit UI. **194 forks against 114 stars** — unusually fork-heavy, which reads as deployment rather than stargazing. |
| 🆕 **Claw-ED** | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | MIT | 63 | unplaced — no country stated | "Local-first AI teaching assistant for editable lesson drafts, student materials, and slides", working from the teacher's own curriculum files and chosen model. Page states **v9.18.2026.1 · Beta**, explicitly **single-teacher-per-instance, not multi-tenant**, student-facing features labelled experimental. 15 forks. Honest about its own scope, which is rarer here than capability. |
| 🆕 **ai-tutor-app** | [towardsai/ai-tutor-app](https://github.com/towardsai/ai-tutor-app) | Apache-2.0 | 34 | unplaced | "Agentic RAG tutor for applied AI, LLMs, RAG, and Python: a LangGraph agent (FastAPI + Next.js)", grounded in a curated course and library corpus, with LangSmith tracing. 5 forks. Small, but it is the cleanest **readable reference implementation** of corpus-grounded tutoring on this shelf — the architecture, not the content, is the asset. |
| 🆕 **corretor-enem** | [dsvi-b/corretor-enem](https://github.com/dsvi-b/corretor-enem) | MIT | 7 | 🟢 **LATAM (Brazil)** — product and ground truth; author's own country not stated | ENEM essay grader across the **five official competencies** (0–200 each, 0–1000 total), *agent-agnostic*: no API, no ML, no model weights. Calibrated against a local SQLite corpus of **11,147 real essays already marked by examiners** (Essay-BR). Methodology credited to Silva & Araujo (**UFPE**, 2024); corpora to `rafaelanchieta/essay` and `lplnufpi/essay-br`. 1 fork, 11 commits, no release. **Promotion owed since `p420` (24 Oct) and not paid until now.** |
| **pedagogy-benchmark** | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | **EMEA origin + LATAM data** — *newly placed*, see note | Code for *"Benchmarking the Pedagogical Knowledge of Large Language Models"* — runs the **CDPK** (Cross-Domain Pedagogical Knowledge) and **SEND** (Special Educational Needs and Disabilities) benchmarks. Thirteen stars, no About line, and still the most useful repo here for a procurement conversation: it is how you answer *"which model actually knows how to teach"* rather than *"which model knows the subject"*. |

**Licence split:** **9 × MIT, 4 × Apache-2.0, 1 × BSD-3-Clause** — all fourteen
buildable, every cell read from the licence file's title block.
*Apache-2.0: DeepTutor, k12-teacher-skills, lineage-skill, ai-tutor-app. BSD-3-Clause: Open TutorAI CE.*

### Region notes — what is read, and what is inferred

The distinction is the point. An inferred placement is still better than silence,
but it must not be quoted as if it were stated.

- 🟢 **Stated on the page or in the copyright line:** DeepTutor (HKUDS, HKU),
  OpenMAIC (THU-MAIC, Tsinghua), k12-teacher-skills (Anthropic), canvas-mcp
  (UIUC), OATutor (UC Berkeley CAHL lab), Open TutorAI CE (Morocco).
- 🟡 **Educhain → APAC (India).** *Newly placed this pass.* The page states no
  location; the **licence file's copyright line reads
  `Copyright (c) 2024-2025 Educhain (https://educhain.in)`**. The `.in` domain is
  the only locational evidence, and it came out of the licence file — which is
  the direct payoff of reading licences at source rather than off a badge.
- 🟡 **Bloom → APAC.** *Newly placed this pass.* Inferred from the README being
  Chinese-first Socratic tutoring and from DashScope (Alibaba Cloud) given as the
  example model provider. No country field anywhere; copyright reads
  `Li Zhengping`.
- 🟡 **lineage-skill → APAC.** Inferred: README is in Chinese with an English
  translation alongside, and the acknowledgments name **Datawhale** and
  **LINUX DO**, both Chinese communities. No country stated.
- 🟡 **pedagogy-benchmark → EMEA origin, LATAM data.** *Newly placed this pass,
  and the most interesting placement on the shelf.* The licence file reads
  `Copyright (c) 2025 Fab Inc`; Fab Inc and AI-for-Education.org are a UK-founded
  advisory and non-profit pair working on AI in education for **LMICs**. The
  repository page separately credits the **Chilean Ministry of Education's
  Agencia de la Calidad de la Educación and CPEIP** for the exams the benchmark
  is built from. So the code is EMEA and **the pedagogical ground truth is
  Chilean**. The UK origin is reported, not read off the repo; the Chilean
  attribution *is* on the repo.
- 🟢 🆕 **corretor-enem → LATAM (Brazil).** The strongest placement on the shelf
  and the only one where the *artefact itself* is the evidence rather than a
  domain name or a README language. The grader encodes **ENEM's five official
  competencies**, the corpus is **11,147 essays already marked by Brazilian
  examiners**, and the methodology is credited to **UFPE**. The author's own
  country is nowhere on the page — and it does not need to be: a product this
  tightly bound to one national examination is placed by what it does.
  🔵 **Worth separating for the regional filter:** this is *origin*, not just
  data. `pedagogy-benchmark` is EMEA code over Chilean data; `corretor-enem` is
  **Brazilian code over Brazilian data**, and it is the first of those on this
  base.
- ⚪ **Genuinely unplaced:** anki-mcp-server, Claw-ED, ai-tutor-app.

**Regional balance, stated plainly:** 4 APAC · 3 North America · 2 EMEA (one of
them with Chilean data) · 🆕 **1 LATAM** · 3 unplaced. Still APAC-weighted at the
top by a very wide margin — DeepTutor and OpenMAIC alone hold **90.8k of the
shelf's ~93k stars** — but the "no LATAM-origin agent" line that stood for seven
passes is **retired this pass**, and it was retired from this base's own records
rather than from a search. See
[§ What is still missing](#what-is-still-missing).

## ⚠️ Licence traps — repos that look permissive and are not

Education repositories a naive licence probe grades as buildable. They are not.
Every row re-read from the **licence file's title block** this pass.

| Repo | Grades as | Actually | Why the trap works |
|---|---|---|---|
| 🆕 [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) · 91★ | `MIT` | **GPL-3.0** | **New this pass, and the cheapest trap on the list to fall into: the repository contradicts itself.** The sidebar says `GPL-3.0`; the **README badge says `License: MIT`**. The licence file's title block reads `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`. **GPL-3.0 wins** — a README badge is a claim, a licence file is the grant. A "learner-owned" platform (private courses, course-scoped cited RAG, BYOK keys, 40 forks) that cannot be shipped inside a proprietary deliverable. |
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) · 2.1k★ | `MIT` | **Bespoke non-commercial** — title line reads *"# PageLM Community License"* | The payload *opens* with the MIT sentence — *"Permission is hereby granted, free of charge…"* — then spends 8 KB taking it back: use limited to personal/educational/non-commercial research, **redistribution in source or binary form strictly prohibited**, and a **revenue-share agreement required before any commercial deployment**. A probe matching on body sentences sees MIT. A probe reading the **title line** sees the truth. Re-confirmed this pass — and note the grant is at **`LICENSE.md`**, not `LICENSE`. |
| [canyongbs/advisingapp](https://github.com/canyongbs/advisingapp) · 340★ | `unknown` | **Elastic-2.0** (title block: *"Elastic License 2.0"*) | Higher-ed advising CRM and conversational platform. Elastic-2.0 forbids providing the product as a hosted/managed service — which is exactly what a studio engagement does. Not usable as a base. |
| [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) · 5.1k★ | `CC-BY-4.0` | **CC-BY-NC-4.0** — this trap is **entirely probe-side**; the page badge is correct | The title line reads *"Attribution-**NonCommercial** 4.0 International"*; the body carries the BY-4.0 boilerplate. Dropping `NonCommercial` from the family name turns an unusable corpus into a usable one on paper only. |

### 🆕 A fourth verdict band: **granted, but not under a code licence**

Not mislabelled, not ungranted — **granted under a licence that was never meant
for software.** This band had no home on the shelf before this pass, which is how
the largest education-agent repository this base tracks stayed off the file.

| Repo | Stars | Licence (title block) | Verdict |
|---|---|---|---|
| 🆕 [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **926** · 130 forks | **Creative Commons Attribution-ShareAlike 4.0 International** | 🟡 **Usable, with a condition most engagements will not accept.** 165 evidence-grounded skills across 20 domains for teachers, school leaders and EdTech builders; the bundled MCP server exposes **157 tools and 165 prompts**; `v3.1.0`, **22 Oct 2026**, which retired the public hosted MCP service in favour of a portable edition. Claude, Codex and Hermes. Author Gareth Manning, *"20 years of international education experience across 27 countries"*, no country or institution stated — **unplaced**. |

**Why this is its own band and not a trap row.** CC BY-SA 4.0 is a real grant and
an honest one — the README calls it *"Open. Forkable. Share alike."* — but it is a
**content** licence. Three consequences a studio has to price before it forks:

1. 🔴 **ShareAlike propagates to adaptations.** Derive a client's skill library
   from these skills and the derivative is owed to the public under BY-SA. That
   is the opposite of what a bespoke-deliverable engagement assumes.
2. 🔴 **No patent grant and no contributor licence**, unlike Apache-2.0. For a
   library whose output is used in assessment and admissions decisions, the
   absence is not academic.
3. 🟡 **The code/content line is undrawn.** The repository ships a working MCP
   server *and* 165 prose skills under a single content licence. Which half the
   grant covers is not stated anywhere on the page.

🔵 **The rule this band adds:** a permissive-looking badge is not the question.
**Ask what the licence was written to cover.** `MIT` on a corpus and `CC BY-SA` on
a server are both category errors, and only the second one is currently common.

### 🆕 The other failure mode: stars but **no grant at all**

Not mislabelled — **ungranted**. No licence file at any common path
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `license.txt`, `LICENCE`, `COPYING`) on
`main`, `master` or `develop`. Without a grant, default copyright applies and the
code **cannot be used**, however open it looks. These are not shelf rows and not
trap rows; they are a third category this base had not written down.

| Repo | Stars | What the repo says instead | Verdict |
|---|---|---|---|
| [A-R007/Multi-Agent-Study-Assistant](https://github.com/A-R007/Multi-Agent-Study-Assistant) | **64** | Sidebar shows **no licence**. README's own License section says only *"This project is open source and available for educational purposes."* | ⛔ **Ungranted.** That sentence names no licence, grants no rights and would not survive five minutes of client legal review. The most substantial repo in this category — 6 agents, adaptive roadmaps, RAG Q&A, 15 forks. |
| [idoforgod/Vibe-learning-AgenticWorkflow](https://github.com/idoforgod/Vibe-learning-AgenticWorkflow) | 25 | Resources shows a **"License" link that anchors into the README**, not to a licence file. No licence type named anywhere. | ⛔ **Ungranted.** The sidebar link is the trap: it renders exactly like a real licence entry. |
| [tosuki/moodle-mcp](https://github.com/tosuki/moodle-mcp) | — | A search result described this repo as *"MIT licensed."* **No licence file exists.** | ⛔ **Ungranted** — and a reminder that a search summary is not a verification channel. |
| [bobuel/bloom-taxonomy-quiz-builder-skill](https://github.com/bobuel/bloom-taxonomy-quiz-builder-skill) | 3 | Nothing. | ⛔ **Ungranted.** |
| 🆕 [henriquebotelhogomes/educacao](https://github.com/henriquebotelhogomes/educacao) | 0 | "Mentora AI" — a Socratic RAG tutor with a learning-gap radar, Next.js + FastAPI. README present on `master`, no licence section. | ⛔ **Ungranted.** Probed on `main` and `master` across six paths. The repository resolves; the grant does not exist. |
| 🆕 [Fatima0923/AssessmentAI](https://github.com/Fatima0923/AssessmentAI) | 0 | Multi-agent LLM essay-evaluation pipeline with human-in-the-loop review. README present on `main`. | ⛔ **Ungranted** — and it sits squarely in the one capability gap this base has carried longest, which is what makes the missing grant expensive rather than merely untidy. |

### 🆕 Not ungranted — **absent**

| Address | What a search result said about it | What the probe found |
|---|---|---|
| 🔴 `belentani7/aprende-brasil` | A search summary described it in confident detail: *"plataforma educativa brasileña interactiva con tutor IA"*, a tutor named **"Nilo"**, an **offline LLM fallback**, **205 modules**, React + FastAPI + SQLite. | ⛔ **The address does not resolve.** `README.md` returns 404 on `main` and on `master`; the repository page returns **HTTP 404**. **No such repository.** |

🔴 **This is the third time this base has recorded a search summary describing a
repository it cannot confirm exists** — after `tosuki/moodle-mcp` ("MIT licensed",
no licence file: that one is real and ungranted) and the **ArguLens** paper
mis-attributed to `wwrwbs/AI_AWE` (`p527`). The pattern is now specific enough to
name: 🔵 **the richer the detail in a search summary, the more it needs an
existence probe** — 205 modules and a named tutor is exactly the texture that
reads as first-hand and was not.

**Rules for this base**, extended this pass:

1. Grade a licence from the **title block** of the licence file, never from a
   sentence in the body, and never drop a `NonCommercial` qualifier.
2. Check `LICENSE.md`, `LICENSE.txt` and `license.txt`, not just `LICENSE`.
   [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) (107.5k★)
   serves its grant at **`LICENSE.txt`** and the page names no licence type — a
   probe reading one filename files a six-figure-star asset as ungranted. Read
   this pass: it is **Apache-2.0**. PageLM's grant is at `LICENSE.md`; Frappe's at
   `license.txt`.
3. 🆕 **When the README badge and the sidebar disagree, the licence file decides.**
   (`ahmedEid1/lumen`.)
4. 🆕 **"No licence file" is a finding, not a blank.** Record it as ungranted;
   a missing grant is a harder blocker than a bad one, because there is nobody
   to negotiate the exception with.
5. 🆕 **Probe that the repository resolves before grading its grant.** `README.md`
   on `main` and `master`. A 404 everywhere means *absent*, not *ungranted* —
   see [§ Not ungranted — absent](#-not-ungranted--absent).
6. 🆕 **Read the dependency licences, not only the repository's.**
   [sonstellar969/open-moodle](https://github.com/sonstellar969/open-moodle) is
   **MIT** and its own page states that its PDF-extraction dependency
   **PyMuPDF is AGPL-3.0**. A repo-level probe grades it buildable; the shipped
   artefact carries network copyleft. The grant you ship is the *union* of the
   grants you link.
7. 🆕 **Ask what the licence was written to cover.** CC BY-SA on a skills library
   is a real grant with a ShareAlike condition and no patent clause — a fourth
   verdict band, not a pass and not a trap. See
   [§ A fourth verdict band](#-a-fourth-verdict-band-granted-but-not-under-a-code-licence).

## What is still missing

Stated rather than left silent, because an unwritten gap looks like coverage.

- 🔴 **No credible MCP server for Moodle — the sector's largest LMS.** ⚠️ **The
  shape of this gap is corrected this pass, and the correction matters more than
  the gap.** `p527` wrote that eight search results *"resolve to ~three
  codebases"*. They do not. The census now holds **thirteen addresses — twelve
  probed first-hand this pass**, the thirteenth (`triffon/moodle-mcp`) carried
  from `p527` as a confirmed duplicate — and they resolve to
  **eleven independent codebases plus two forks**, in **four languages**
  (Rust ×1, Python ×4, TypeScript/Node ×2, Go ×1, two unread), with tool counts
  from **8 to ~230**
  — and **the entire field sums to under 40 stars.** So the finding is not
  absence, it is 🔴 **fragmentation with no convergence**: ten of eleven
  codebases are **MIT**, nobody has above 27★, and no two agree on a tool
  vocabulary. Full census in
  [`../repos/foundations.md`](../repos/foundations.md). 🟢 **This makes the build
  *more* attractive, not less** — consolidating nine permissive implementations
  is a cheaper start than a greenfield bridge. The old reading, kept because the
  ceiling is unchanged: `thc1006/moodle-mcp` (0★) is a
  fork of [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) (**27★**,
  MIT, the lineage's real head), and `triffon/moodle-mcp` carries
  `Copyright (c) 2026 Falkenslab` — i.e. it is
  [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) (2★, MIT).
  The most visible one,
  [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server)
  (1★), is **AGPL-3.0** and read-only. Compare **canvas-mcp at 308★**. Moodle has
  the sector's largest install base and plugin ecosystem and **no serious agent
  bridge** — the clearest build opportunity on this base. See
  [`../compose/patterns.md`](../compose/patterns.md).
- 🟢 🆕 **"No LATAM-origin education agent" is RETIRED — and it should have been
  retired on 24 October.** [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem)
  (**MIT**, 7★) is LATAM-origin **code**: Brazilian examination, Brazilian corpus,
  Brazilian methodology. `p420` verified it, called it *"the one new address worth
  shelving"*, and no later pass either shelved it or recorded a reason not to —
  while this file went on printing *"the LATAM contribution is data, not code"*
  for seven passes. 🔴 **The gap was not in the supply. It was in this base.**
  🆕 A second LATAM artefact, verified this pass and **not** shelf-grade:
  [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional)
  ("EduRAG", **MIT**, **0★**) — agentic RAG for Brazilian grades 1–4, grounded in
  **MEC** documents (BNCC `EF01`–`EF04`, PCNs across six subjects), with
  page-level citations, BNCC-code identification, a **Self-RAG** hallucination
  check, LangGraph + ChromaDB + `bge-m3` + Ollama, an MCP server and **Giskard**
  evaluation. It is a university course's final project with no stars — so it is
  a **reference implementation, not a dependency**, and it is the cleanest one
  this base has seen for *"ground a teacher agent in a national curriculum."*
  🟡 **So the LATAM gap is now about maturity, not existence:** the region's two
  verified agent-leg artefacts total **7 stars and 0 releases**. What remains
  pre-release:
  [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent) ("Manu",
  MIT, **0★**) is a Brazilian-Portuguese voice maths tutor on LiveKit Agents
  covering 1st grade to university, README states *"in development"*, no public
  deployment, ENEM-aligned, and it wires in Brazilian crisis lines (190, CVV 188)
  — thoughtful, and not yet a thing you can build on.
  [`H1bertto/professor-agent`](https://github.com/H1bertto/professor-agent) (MIT)
  is likewise early. **The region's shipped open-source strength remains school
  management, not agents** — see
  [portabilis/i-educar](https://github.com/portabilis/i-educar) in
  [`../repos/foundations.md`](../repos/foundations.md). The LATAM contribution on
  the *agent* legs this pass is **data, not code**: the Chilean exams behind
  `pedagogy-benchmark`.
- 🟡 **Two EMEA-placed agents** (Open TutorAI CE in Morocco; pedagogy-benchmark's
  UK origin) against four APAC.
- 🟡 🆕 **Assessment integrity: the gap moves from "nothing permissive" to
  "nothing adopted", and the sharpest signal this pass is a deletion.**
  🔴 [`AIEd-Innovations/assessment_agent`](https://github.com/AIEd-Innovations/assessment_agent)
  (**Apache-2.0**, 0★) was the one open agent doing grading *and* integrity
  together. **PR #19, *"Remove the integrity check: the agent only grades"*,
  merged to `main` on 27 Oct 2026** — it strips the anomaly-detection LLM call
  (`agents/anomaly_detector.py`, `prompts/anomaly_detection.txt`), the anomaly
  report log, the `GET /anomalies` endpoint and the `anomaly_report` result
  field; an integrity risk **no longer routes a submission to review**. The
  stated payoff is one LLM call per submission instead of two. 🔵 **Read it as
  the economics of the gap, not as one team's choice:** integrity doubled the
  inference cost and was the half that got cut. 🟢 Two MIT candidates now exist
  and **both sit at 0★ / 0 forks** —
  [`sonowalvaibhav/gradeops`](https://github.com/sonowalvaibhav/gradeops)
  (handwritten-answer VLM grading, JSON rubrics, TA override dashboard, and
  plagiarism detection that compares two submissions for *shared anomalous
  logic and identical erroneous reasoning* — the right primitive) and
  [`biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent`](https://github.com/biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent)
  (fully local, **zero external APIs**, from-scratch logistic regression for
  explainable cheating-risk with an evidence breakdown for human review rather
  than a verdict — the right posture for the EU's 2 Dec 2027 high-risk band).
  ⚠️ Both are single-author student projects with self-reported metrics, and the
  proctoring repo contradicts itself on its own test count (**94** under
  Performance Metrics, **344** under Quick Start). **Signals, not dependencies.**
  The older reading still holds for anything production: the credible tooling is
  classical, not agentic —
  [dodona-edu/dolos](https://github.com/dodona-edu/dolos) does code-similarity
  detection well and has no LLM in it. Automated *scoring* is likewise thin:
  [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) (Apache-2.0, **2★**) is a
  Qwen-classifier-plus-LightGBM essay scorer. ⚠️ A search result attributed the
  arXiv **ArguLens** paper (2608.17356) to this repository; **the repository
  mentions neither ArguLens nor any arXiv paper**, and its citation URL is still
  a `<your-org>` placeholder. The attribution is **unverified** — do not repeat it.
- 🔴 **No open-source SIS/advising agent under a permissive licence.** Unchanged.
  The only serious candidate (`advisingapp`) is Elastic-2.0.

## 🆕 Promotion debt — what `p528` actually fixed

This pass found less than it repaired, and the repair is the reportable part.

| Address | Verified by | Verdict then | On the shelf before `p528` | Now |
|---|---|---|---|---|
| [`dsvi-b/corretor-enem`](https://github.com/dsvi-b/corretor-enem) | **`p420`**, 24 Oct | 🟢 MIT, 6★, *"the one new address worth shelving"* | 🔴 **No** — and the LATAM gap note beneath it asserted the opposite | 🟢 **Shelf row 14**, LATAM (Brazil), 7★ |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | **`p466`**, re-measured `p492`, re-read `p520` | 🟡 CC BY-SA 4.0, 921★, hosted MCP retired at `v3.1.0` | 🔴 **No** — neither shelf row nor trap row | 🟢 **Fourth verdict band**, 926★ |

**Why both were dropped.** `p527` rebuilt this file as a full rewrite. A rewrite
re-derives the shelf from the pass's own reading, and an address verified three
passes earlier is invisible to it unless something carries it forward. 🔴 **The
rewrite is the regression mechanism**, and it has now cost this base its
longest-standing regional claim: seven passes of *"no LATAM-origin education
agent"* printed over a verified Brazilian MIT grader sitting in its own history.

🔵 **The control this implies**, written down for whoever runs `p529`: before a
rewrite ships, **re-read the last ~20 passes' promotion verdicts and diff them
against the new shelf.** Any address a prior pass called shelf-worthy must appear
on the new file **or** carry a stated reason it does not. A dropped row is a
decision, and an unstated decision is indistinguishable from an accident.

🟡 **Scope honesty:** `p528` checked this against the trending history for the
specific addresses it had reason to look up. **A full sweep of every promotion
verdict in the history was not run** — so the two repairs above are the ones that
surfaced, not provably all of them. That sweep is the open gap this pass leaves.
