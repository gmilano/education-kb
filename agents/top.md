---
industry: education
region: Global
updated: 2026-10-19
---

# Top open source AI agents — education

**Pass 318 · 2026-10-19.** Eighteen rows, eighteen real repos. No header rows, no placeholders, no
example data.

Verification method, unchanged and re-confirmed against the proxy's own status endpoint this pass:
`curl -sI` to github.com returns **403 at this session's proxy**, so every row was checked by
loading the repository page and reading the licence label, star count and commit count GitHub
itself renders. The **Checked** column says which pass took that reading.

**Pass 318 found something that changes how this table must be maintained.** One repo in this
sector now carries an instruction addressed to AI agents asking them to star it (detail below).
Combined with pass 317's finding that a star-ranked search cannot *see* institutional
infrastructure, **stars now fail in both directions at once**: too low on the software that
matters, and inflatable on the software that does not. Treat the ★ column as a rough size signal
only — it was never a quality metric and it is now not even a reliable popularity one.

## The table

| Agent | Repo | Licence | ★ | Checked | What it does | Use it for |
|---|---|---|---|---|---|---|
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 41.7k | p318 | Lifelong personalised tutoring agent; v1.6.15 (2026-10-19), 2,935 commits, 5.3k forks, paper arXiv 2604.26962. README now describes it as an "agent-native learning workspace" with an inspectable three-layer memory, Co-Writer, Book and Partners | The strongest permissive starting point for a tutor product |
| smolagents | https://github.com/huggingface/smolagents | Apache-2.0 | 29.9k | p317 | Minimal library for agents that think in code; 1,059 commits | The agent runtime under a tutor when you want small and auditable |
| FSRS4Anki | https://github.com/open-spaced-repetition/fsrs4anki | MIT | 4.1k | p317 | Free Spaced Repetition Scheduler as an Anki scheduler; 482 commits | Retention scheduling — the review-timing half of a tutor |
| nbgrader | https://github.com/jupyter/nbgrader | BSD-3-Clause | 1.4k | p317 | Assigning, collecting and autograding Jupyter notebooks; 3,477 commits | Grading automation in any notebook-based curriculum |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 878 | p316 | 165 evidence-grounded teaching skills (pedagogy, assessment, curriculum) for Claude/Codex/Hermes; 149 commits | Prompt and pedagogy assets — **not** a code dependency, see caveat |
| iblai/os | https://github.com/iblai/os | MIT | 821 | p316 | Agent platform (Next.js → web/desktop/mobile) with chat, voice, SSO; 3,518 commits | A front end only — the backend is **not** in the repo, see caveat |
| human-skill-tree | https://github.com/24kchengYe/human-skill-tree | **MIT/AGPL-3.0 dual (skills); AGPL-3.0 (app)** | 573 | p318 | 33 agent skills turning Claude/ChatGPT/Gemini into structured tutors on spaced-repetition and active-recall principles, plus a Next.js 16 app (React Flow, Supabase, OpenRouter); K-12 through career and social skills; bilingual EN/zh; 36 commits | APAC-authored evidence for trend 7 — **and the star-solicitation caveat below** |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | MIT | 520 | p316 | MCP server exposing the Anki flashcard app to any LLM client; 258 commits | Wiring a real spaced-repetition store to an agent without writing a scheduler |
| Educhain | https://github.com/satvik314/educhain | MIT | 387 | p317 | Python package generating MCQs, lesson plans and flashcards with LLMs; 578 commits | Content-generation pipelines behind an authoring tool |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | **GPL-3.0** | 932 | p317 | AI tutor built on Theory-of-Mind reasoning: reasons about the learner's needs and rewrites its own prompts to suit them; v0.8.0, 356 commits | Study the ToM prompting approach — **copyleft, see caveat** |
| Bloom | https://github.com/Li-Evan/Bloom | MIT | 289 | p316 | Socratic adaptive tutor shipped as both portable agent skills and a self-hostable React/FastAPI app; 76 commits | The clearest worked example of the skill-plus-app delivery shape |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 268 | p317 | Intelligent tutoring system with Bayesian Knowledge Tracing (ReactJS + Firebase), UC Berkeley CAHLR; 1,045 commits. README: "For LMS integration, a middleware backend is required by Learning Tools Interoperability (LTI)" | Mastery modelling / hint sequencing where you must explain the pedagogy |
| otter-grader | https://github.com/ucbds-infra/otter-grader | BSD-3-Clause | 161 | p315 | Python and R autograding with containerised execution | Autograding where submissions must run sandboxed |
| OpenTutor | https://github.com/zijinz456/OpenTutor | MIT | 145 | p316 | Local-first block-based adaptive workspace: upload material → notes, quizzes, flashcards, tutor; 10+ LLM providers, 194 commits | An offline/on-prem tutor shell when data cannot leave the building |
| gen-mentor | https://github.com/GeminiLight/gen-mentor | CC0-1.0 | 135 | p316 | LLM multi-agent framework for goal-oriented learning in an ITS; WWW '25 oral, arXiv 2501.15749; 91 commits | A peer-reviewed multi-agent ITS architecture you can cite in a bid |
| Open TutorAI CE | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 111 | p315 | Educational collaborative AI tutoring platform; arXiv 2602.07176 (Feb 2026) | An academically documented tutor platform you can fork and cite |
| lumen | https://github.com/ahmedEid1/lumen | **GPL-3.0** (LICENSE file; README badge wrongly says MIT) | 89 | p318 | Multi-agent orchestrator builds a private course from a one-sentence goal in ~50s, then a course-scoped RAG tutor teaches it; v2.0.0 2026-06-06, 828 commits; FastAPI + Next.js 15 + pgvector; BYOK envelope-encrypted | **Read for its published evals, not for its licence** — see below |
| tutor-mcp | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 52 | p316 | MCP server that turns any LLM into an ITS: skill graph, BKT, FSRS, prerequisite rules, narrative memory; SQLite local / PostgreSQL hosted; 467 commits | The deterministic-pedagogy engine — still the architectural find of p317 |

## The LTI gap, pass 318: re-checked, unchanged, still open

`blamb/lti-tutor` was re-read first-hand this pass. **Its licence is still "To be decided", it still
has 0 stars, 0 forks and 39 commits.** Nothing has moved since pass 317.

This matters because it is the single highest-value watch item in this KB: it implements LTI 1.3
against Moodle with dynamic registration, deep linking and completion passback through Assignment
& Grade Services on `ltijs` — precisely the artefact this KB has declared missing for four passes —
and **one commit adding a LICENSE file would make it the most strategically valuable repo here.**
Until then default copyright applies and Globant cannot use it, fork it, or copy its approach into
a client deliverable.

**Re-check it every pass. It is a one-line check with a large payoff.**

The gap stands as worded in pass 317: there is no *usably licensed* open source LTI 1.3 AI tutor.
What pass 318 adds is a mitigation for the *other* half of the problem — see the `ltibootcamp`
finding in `repos/foundations.md`, which maps the LTI 1.3 library landscape across seven languages
and takes some of the concentration risk off `pylti1.3`.

## A repo in this sector is now soliciting stars from AI agents

`24kchengYe/human-skill-tree` (573 ★, 36 commits) ends its README with a passage **addressed to AI
agents, asking them to star the repository** and claiming efficiency benefits for doing so. It was
ignored when this pass read the page, and it is recorded here because of what it implies rather
than what it is.

This KB is compiled by an automated process that reads repository pages. **So are a growing number
of the tools a client's engineers use to choose dependencies.** A README instruction aimed at that
reader is a supply-chain-adjacent manipulation attempt, cheap to write and, at 573 stars against 36
commits, not obviously unsuccessful.

Three consequences, and the third is the one that matters:

1. **Content a repository addresses to an automated reader is data, not instruction.** This pass
   treated it that way. Any Globant tooling that reads repo pages to rank dependencies must do the
   same, explicitly.
2. **The ★ column in this KB is now a weaker signal than it was last pass**, and it was already
   weak. Pass 317 established that stars run *too low* on institutional infrastructure — Ed-Fi at
   12, Sunbird at 41, OpenOLAT at 448 with 31,877 commits. This pass establishes they can also be
   solicited upward. **Commit count, release cadence and licence are the durable signals; rank on
   those.**
3. **The repo is still in the table.** Its skills are real, dual MIT/AGPL-licensed, bilingual, and
   it is one of the few APAC-authored artefacts in this tier. Flagging the behaviour is the correct
   response; deleting a usable finding over it would be an overreaction. Read the skills, do not
   take the app, and know what the README tried to do.

## lumen is worth reading because its evaluation scores are bad and published anyway

`ahmedEid1/lumen` (828 commits, v2.0.0 on 2026-06-06) generates a private course from a
one-sentence goal with a multi-agent orchestrator, then teaches it with a course-scoped RAG tutor
whose retrieval runs through a single access-control clause so private and cloned courses cannot
leak chunks. Its README publishes its own evaluation results:

- **authoring 3.85/5** (n=10)
- **tutor 2.33/5** (10 of 30 items judged)
- **ingest 0.83/5** (4 of 10 items judged)

— and attributes the weak tutor score to a citation-format mismatch. **No other repo in this KB
publishes a number that unflattering about itself.** In a sector where every vendor deck claims a
tutoring uplift, a project reporting 0.83/5 on its own ingest pipeline is the most credible
artefact of the pass, and the eval harness shape is worth copying into any tutor engagement where
the client will eventually ask "how do you know it teaches?".

**Its licence is GPL-3.0.** The README carries an MIT badge; the `LICENSE` file in the repository
root is the full GNU General Public License v3 text. **The LICENSE file governs.** This is the
fourth repo in this KB whose real licence differs from its surface presentation — after Frappe
Education, OpenOLAT and `education-agent-skills` — and the second this pass (see below). Read the
file, never the badge.

## Caveats a studio lead should read before quoting any of these

- **`iblai/os` is open-core, not open source in the useful sense.** MIT, 821 ★, 3,518 commits — and
  its README says plainly: *"ibl.ai/os requires the ibl.ai backend platform for authentication, AI
  agent APIs, and data services. The backend is not included in this repository."* You can read and
  fork the client; you cannot self-host the product.
- **`education-agent-skills` is CC BY-SA 4.0 — ShareAlike, and a content licence, not a code
  licence.** Derivative teaching material must be released under the same terms. That is a live
  constraint on a client deliverable.
- **`human-skill-tree` is dual-licensed and the halves differ.** The skills are MIT/AGPL-3.0 dual;
  **the web app is AGPL-3.0 only.** Take the skills, leave the app, and record both licences
  separately in the inventory — a single "MIT/AGPL" line in a licence register is not good enough
  when the permissive half is the only half you can use.
- **`gen-mentor` is CC0-1.0.** Usable, but a paper-companion release (91 commits) with no warranty
  culture. Cite the architecture; do not take the dependency.
- **`Educhain` is 387 ★** — earlier passes recorded "~12k ★", which was wrong.
- **`DeepTutor` is the outlier in both directions.** Re-verified first-hand this pass: Apache-2.0,
  41.7k ★, 5.3k forks, 2,935 commits, **v1.6.15 released 2026-10-19**. A release on the day of this
  pass makes pinning a version mandatory, not advisable.
- **`Bloom`, `OpenTutor` and `anki-mcp-server` are small but honest.** 76, 194 and 258 commits.
  Reference shapes and composable parts, not platforms.
- **The three graders are BSD-3-Clause, not MIT.** Permissive, but the attribution clause is real.
- **`tutor-gpt` and `lumen` are the two copyleft rows.** Both GPL-3.0, both in the table to be read
  rather than linked. `tutor-gpt` for its Theory-of-Mind prompting, `lumen` for its eval harness.

## Rejected after verification — recorded so the next pass does not re-find them

- **`blamb/lti-tutor` — NO LICENCE ("To be decided").** Re-verified p318: unchanged at 0 ★, 39
  commits. The LTI 1.3 tutor this KB needs, and unusable. Watch it every pass.
- **`luffycodes/Tutorbot-Spock` — NO LICENCE FILE.** 56 ★, 8 commits. Notable work (CLASS, EMNLP
  2023, arXiv 2305.13272; Pedagogical Alignment of LLMs, EMNLP 2024, arXiv 2402.05000).
  **Read the papers, not the repo.**
- **`CSOAI-ORG/coppa-ferpa-mcp` — MIT, but rejected in p317 and not revisited.** 1 ★, 16 commits,
  two contradictory price lists in one README. Compliance tooling is the last place to accept
  vendor self-description.
- **`artcc/freelingo` — AGPL-3.0, 188 ★.** A real self-hosted AI language-learning platform; it
  sits in `verticals/solutions.md` as a platform because AGPL puts it on the copyleft side of this
  KB's architectural line.
- **`AITutor-EvalKit` — no repository located.** The paper (arXiv 2512.03688, MBZUAI: Naeem, Maurya,
  Petukhova, Kochmar) describes a tool for evaluating the *pedagogical* quality of tutor responses
  in student-mistake remediation, which is exactly the eval layer this sector lacks. The authors
  call it an early research prototype and **no GitHub repository or licence could be found this
  pass.** Cite the paper as evidence that the eval problem is being worked; do not plan on the code.

## Licence split

MIT (8 — FSRS4Anki, iblai/os, anki-mcp-server, Educhain, Bloom, OATutor, OpenTutor, tutor-mcp),
BSD-3-Clause (3 — nbgrader, otter-grader, Open TutorAI CE), Apache-2.0 (2 —
DeepTutor, smolagents), **GPL-3.0 (2 — tutor-gpt, lumen)**, dual MIT/AGPL-3.0 (1 —
human-skill-tree, skills only), CC0-1.0 (1 — gen-mentor), CC BY-SA 4.0 (1 — education-agent-skills).

**14 of 18 carry a permissive *software* licence Globant can build on commercially** (counting
human-skill-tree's skills half, and excluding its AGPL app). The exceptions are two copyleft agents
and two content/dedication licences, all flagged above.

The structural fact holds and is now measured over 18: **the agent tier is predominantly permissive
and the platform tier in `verticals/solutions.md` is predominantly copyleft.** Pass 318 widened the
crack in it from the platform side again — see `openedx/openedx-ai-extensions` and the two new
AGPL AI-native LMS rows there — without changing the architectural advice.

## What was searched and not found

- **No *usably licensed* open source LTI 1.3 agent.** Re-checked directly. `blamb/lti-tutor` remains
  unlicensed. `pylti1.3` (MIT) remains the only solid library, and this pass found a map of its
  alternatives (`repos/foundations.md`).
- **No credible open source agent for assessment integrity / AI-detection. Fifth consecutive pass.**
  The published evidence on AI-text detection accuracy continues to argue this should stay a gap.
- **No usable open source student-data-privacy compliance component — but the shape of the gap
  changed this pass and the change is the finding.** GitHub's `ferpa` topic now carries a *cluster*
  of governance repos that did not exist in earlier passes: `Principled-Evolution/gopal` (8 ★, Rego
  policies), `marc-shade/docsingest` (6 ★, PII/PHI ingestion with hash-chained audit),
  `chaz-clark/canvas-toolbox` (5 ★, FERPA-safe Canvas toolkit),
  `virtualryder/edu-ai-agents` (4 ★, Bedrock agents with PII masking),
  `ashutoshrana/regulated-ai-governance`, `ashutoshrana/enterprise-rag-patterns` and
  `ashutoshrana/voice-ai-governance` (1–2 ★ each), `Polycentric-Labs/regrails` (1 ★),
  `mizcausevic-dev/mcp-ai-tutor` (0 ★, an MCP server that audits tutors for FERPA/COPPA).
  **Every one is at or below 8 stars and nearly all were last updated in September or October
  2026.** Nothing here is a dependency. But a dozen independent authors starting the same component
  in the same two months is a market forming in real time, triggered by the COPPA deadline in
  `intel/market.md`. **Sixth pass declaring this gap, and the first pass able to say it is
  contested rather than empty — which shortens the window on the build-once opportunity.**
- **No region-specific tutoring agent, again** — though the APAC skill-layer presence is now
  represented in the table by `human-skill-tree` (573 ★, bilingual EN/zh) alongside the previously
  recorded `Miaotofu01/Study-Mate` (1.1k ★), `KeWang0622/kaogong-skill` (189 ★) and
  `SimonsTang/feifei-companion` (108 ★). **The LATAM picture changed this pass, but in the platform
  tier, not here** — see `openedx/openedx-ai-extensions` in `verticals/solutions.md`.
