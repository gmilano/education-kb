---
industry: education
region: Global
updated: 2026-10-31
---

# Top AI agents for education

Every row below was verified on 2026-10-31. **This pass changed the verification
method:** licence and star count are read from the **GitHub REST API** (via the
`search_repositories` MCP tool, `minimal_output: false`), which returns
`license.spdx_id` and `stargazers_count` as GitHub itself computes them. Earlier
passes of this KB recorded the API as proxy-blocked and fell back to reading
rendered repo pages; it is reachable this run, and it is strictly better —
GitHub's own licence detector is the thing being quoted, not a sidebar
rendering. Where a repo's README disagrees with the API, both readings are given.

**Fourteen agents qualified, up from six.** The jump is a method artefact as much
as a market one: searching GitHub's index directly (`topic:ai-tutor`,
`topic:agent-skills topic:education`) surfaces a population that no listicle
covers. Three candidates were rejected and are listed with reasons.

## The shelf

| Agent | Repo | Licence | ★ | Region | What it is |
| --- | --- | --- | --: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 52,167 | APAC | Lifelong personalised tutoring; multi-agent pipelines over LLM + RAG. Python, 6,388 forks, created 2025-12-28, pushed 2026-10-31. Data Intelligence Lab, University of Hong Kong. **Still the largest education agent on GitHub.** |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,981 | APAC | **The most consequential new row in this KB.** "Open Multi-Agent Interactive Classroom" — turns a topic or uploaded documents into an interactive lesson with AI teachers *and* AI classmates: slides, quizzes, simulations, speech, whiteboard, live discussion. Exports PPTX, single-file offline HTML, or classroom ZIP. TypeScript (Next.js 16/React 19), 6,502 forks, `v1.3.0` dated 2026-10-29. Created **2026-03-11** — 42k★ in under eight months. `LICENSE` reads "MIT License, Copyright (c) 2026 THU-MAIC"; contact domain is `tsinghua.edu.cn`. |
| DIO Agent | [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | ⛔ **NO LICENCE** — see note | 2,750 | LATAM | **The first LATAM-origin education agent found in three passes, and it cannot be built on.** A study-mentor agent bundle: `AGENTS.md`, `CLAUDE.md`, and `skills/` with one `SKILL.md` per skill (study planning, hinting without answering, concept explanation, web search, portfolio review, career guidance). Runs on Claude Code, Codex, OpenCode, Antigravity, Hermes. 347 forks, created 2026-05-27. README is Portuguese; org links `dio.me`, a bootcamp/`formações` platform. **Licence defect, verified by two methods:** the API returns **no `license` field at all** and the repo page names none. Default is exclusive copyright. Fork and read, do not ship. |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1,280 | APAC | Self-study companion agent: builds a route through a subject, teaches it, and sets projects, with spaced repetition. JavaScript, 60 forks, created 2026-09-17. Chinese-language. |
| learn-from-materials | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | MIT | 1,201 | APAC | Turns PDFs, books and papers into interactive learning webpages that stay traceable to the source and carry quizzes and notes. Python, 109 forks, created 2026-09-08. The closest thing on the shelf to a document-to-course pipeline. |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 539 | Global | MCP server giving an agent control of **Anki**, the spaced-repetition flashcard system. TypeScript, 39 forks, created 2025-09-29. The retention layer: the one verified way to hand an agent a real SRS scheduler instead of reimplementing one. Origin not stated. |
| SocialCoach | [GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach) | Apache-2.0 | 463 | Global | Social-emotional learning by role-play: conflict handling and communication skills with personalised feedback. TypeScript, 60 forks, created 2026-09-03. The only verified **SEL** agent found; SEL is a budget line in K-12 that no other row addresses. Origin not stated. |
| Exam Cram Coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 364 | APAC | Exam-prep tutor that teaches **from the instructor's own slides with page citations**, crops figures, and quizzes from real homework. Explicitly engineered against hallucination (`anti-hallucination` topic) and to run on small cheap models. Python, created 2026-06-24. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 310 | North America | The most established Canvas LMS MCP server. Sidebar: "up to 102 tools and 8 agent skills"; README has said 128. Python, 101 forks, created 2025-02-28. Ships agent skills including pre-semester course audit and accessibility auditor. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 295 | APAC | Socratic private tutor that reads how a learner actually learns; Bloom's 2-sigma research packaged as an agent skill **plus** a self-hostable FastAPI/React app. 44 forks, created 2026-03-10. The clearest instance of the skill-and-app dual shape (see [`../intel/trends.md`](../intel/trends.md)). |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America | Intelligent tutoring system with **Bayesian Knowledge Tracing**, React + Firebase. 164 forks — the highest fork-to-star ratio on the shelf, which is what a teaching-materials project looks like in use. Published at CHI '23. Owning org CAHLR; a UC Berkeley connection is indicated by the authors, not stated on the repo page. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT | 213 | APAC | High-stakes civil-service exam preparation (行测/申论/职测/综应), including a wrong-answer review loop. Python, created 2026-04-06. Shelved as the reference example of **one named credential, fully modelled** — the shape a client asks for by name. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 158 | Global | Block-based adaptive learning workspace that runs **locally**: upload material, get notes, quizzes, flashcards and an adaptive tutor, over 10+ LLM providers, with a knowledge graph. Python/TypeScript, 38 forks. **Star-count correction:** an earlier cycle of this KB recorded OpenTutor at ~900★; the API says **158**. The earlier figure was wrong. |
| Pedagogy Benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | Not a tutor — an **evaluator**. 1,143 questions from real teacher-qualification exams: CDPK (920, general pedagogy) and SEND (223, Special Educational Needs and Disabilities). Code for *Benchmarking the Pedagogical Knowledge of Large Language Models*. Its parent organisation is the LMIC-focused supply side this KB spent three passes failing to find — see [`../repos/foundations.md`](../repos/foundations.md). |

### Carried with a known defect

| Agent | Repo | Licence | ★ | Region | Note |
| --- | --- | --- | --: | --- | --- |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ⛔ MIT claimed in README only — **no LICENSE file** | 104 | North America | Canvas LMS MCP server, `v2.2`, 54 tools, containerised. **Defect re-confirmed this pass by a second, independent method:** querying GitHub's own licence index (`license:mit repo:DMontgomery40/mcp-canvas-lms`) returns **zero results**, so GitHub detects no MIT grant either. Earlier passes established the same thing by 404-ing every licence filename on both branches. Two methods now agree. Prefer `vishalsachdev/canvas-mcp`. |
| moodle-mcp | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | 27 | APAC | Rust MCP server operating Moodle: courses, assignments, forums, grades, files-as-markdown. Validated against Moodle 3.7 → 5.x. Only Rust implementation found. No defect — listed here because at 27★ and created 2026-10-12 it is too young to carry an engagement alone. |

## Why this shelf is shaped the way it is

**The agent layer is permissive; the platform layer is not.** Of the fourteen
shelf rows, **11 are MIT, 2 Apache-2.0, and 1 has no licence at all**. Every platform of record
these agents attach to is copyleft, with two exceptions now documented in
[`../repos/foundations.md`](../repos/foundations.md). The integration surface is
buildable; the substrate mostly is not forkable on commercial terms. The
composition pattern that follows is in [`../compose/patterns.md`](../compose/patterns.md).

**Education AI has stopped shipping as applications.** **Six of fourteen** shelf
rows are **agent skills** — markdown instruction bundles loaded by an existing
harness (Claude Code, Codex, OpenCode, Cursor, Antigravity) rather than
deployable services: `dio-agent`, `Study-Mate`, `learn-from-materials`,
`Exam Cram Coach`, `Bloom` and `kaogong-skill`. `Bloom` ships as a skill **and**
a self-hostable app, which is the hybrid shape to expect next.
This is the single biggest change since the previous pass and it is measured, not
reported: `topic:agent-skills topic:education stars:>50` returns 13 repositories,
led by one at 4,843★. Consequences for an engagement are in
[`../intel/trends.md`](../intel/trends.md); the short version is that the
"product" a client now adopts may be a prompt contract, with no runtime to host
and no API to version.

**Origin has concentrated in APAC.** Of the fourteen shelf rows, **seven are
APAC** — and the two largest (52k★, 42k★) are both Chinese-university projects,
HKU and Tsinghua. The rest: **Global 3, North America 2, LATAM 1 (unlicensed),
EMEA 1 (13★)**. Adding the two defect-table rows below puts North America at 3
and APAC at 8. An engagement sourcing from this shelf is sourcing from APAC
whether or not it intends to.

**MCP is still the integration shape, but no longer the dominant one.** Two shelf
rows are MCP servers (`canvas-mcp`, `anki-mcp-server`), and so are both rows in
the defect table (`mcp-canvas-lms`, `moodle-mcp`) — four of the sixteen agents on
this page. Where an agent must *reach into* a system of record, assume MCP; where
it must *teach*, assume a skill bundle.

## Rejected this run, with reasons

| Candidate | Why it is not on the shelf |
| --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | **4,843★ — would be the third-largest row — and rejected on licence.** A library of 23,000+ agent skills for empirical research across eight social-science disciplines, maintained by CoPaper.AI from Stanford REAP (North America). The README badge reads **"License: CC BY-SA 4.0"** — a *content* licence with share-alike. Derivatives of the skill text must be released under the same terms, which is the opposite of what a client wants from a billable methodology asset. The most valuable rejection on this page: it is the largest education agent-skills repo in existence and it is share-alike. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 217★. Self-hosted AI language-learning platform (CEFR plans, voice conversation, flashcards, spaced repetition, local or cloud LLMs) — technically a good fit and licence-disqualified for a proprietary derivative. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned to it. Recorded so the next pass does not re-discover it. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **Licence unresolved**, 586★. "AI-Powered Skill Tree for Lifelong Human Learning", 30+ skills K-12 → career, cognitive-science framing, ships an MCP server. Queried against GitHub's licence index for both MIT and Apache-2.0: **neither matches**, so it is not permissively licensed as far as GitHub can tell. Genuinely interesting design; needs its licence file read before it can be shelved. **Priority watch item.** |
| [AFRICAN-AI-NETWORK/learnhouse](https://github.com/AFRICAN-AI-NETWORK/learnhouse) | **A 0★ fork, and the trap this pass nearly fell into.** It surfaced as the leading hit for an African education-AI search and the organisation name reads as African supply side. It is a fork of [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) (**AGPL-3.0** plus a separate Enterprise Licence, 2.4k★, maintainer Badr B. / `@swve`, country not stated), with 0 stars and 1 fork and no stated African content. The African signal is the **org name only**. Same failure mode as the `NelsonSpencer/canvas-mcp` fork rejected on the previous pass: an organisation name is not provenance. |
| [profitsylivester-ux/tujifunze-agent](https://github.com/profitsylivester-ux/tujifunze-agent) | **MIT (README), 0★, 11 commits, no releases, empty Languages panel.** LangGraph + MCP + Qwen 2.5 decision-support agent tracking multi-term learner trajectories and producing cited plain-language student profiles with human-in-the-loop oversight. Built for the **African Agentic AI Design Challenge, Education track**; "Tujifunze" is Swahili; no country stated. Below the shelf bar, but **logged as a watch item and as evidence**: it is the first African-context education agent this KB has located in three passes, and its design — citations plus mandatory human review over learner records — is the right shape for ministry work. |

## Method note — how URLs were verified this pass, and why not with `curl`

Every repository URL on this page was confirmed to exist by a **GitHub REST API
lookup** (`search_repositories` with `repo:owner/name`), which returns the repo's
id, licence, star count and push date — existence plus metadata in one call. In
addition, the 22 rows carried over from earlier passes were re-confirmed live in
two bulk queries.

**`curl -sI` does not work from this session and must not be used as the check.**
A sweep of all 57 github.com URLs on this page returned **HTTP 403 for every
single one**, including `moodle/moodle` and `odoo/odoo`. That is the session's
outbound HTTPS proxy refusing raw requests to github.com, not a statement about
any repository. A pass that treated those 403s as findings would have deleted
the entire KB. **If `curl` returns a uniform status for every URL, the check is
measuring the network, not the data** — switch to the API.

## Declared gaps

- **No published ranking of education AI agents exists.** The prescribed search
  `top open source AI agents education 2026 github MIT` returned, for the third
  consecutive pass, general-purpose agent listicles with an education angle
  bolted on, plus one aggregator that misreported licences. This shelf is
  assembled from GitHub's own index because there is nothing to copy. The
  practical lesson is now firm: **query the index, not the listicles.**
- ~~**LATAM: no LATAM-origin education agent qualified.**~~ **Closed, with a
  sting.** Two prior passes searched in English and in Spanish/Portuguese prose
  and concluded the absence was real. It was not — it was a *search-surface*
  gap. Querying GitHub directly with Portuguese and Spanish terms
  (`tutor OR educación OR educacao OR escola OR aprendizaje IA agente stars:>20`)
  returned [`digitalinnovationone/dio-agent`](https://github.com/digitalinnovationone/dio-agent)
  at **2,750★** — larger than every North American row on this shelf. It is
  **unlicensed**, so the finding is simultaneously a closure and a new blocker.
  Correction to this KB's record: the earlier "two independent search strategies
  support this gap" was overconfident. Both strategies searched the *web*; neither
  searched the *index*.
- **EMEA agent origin is still effectively empty.** The one EMEA row
  (`pedagogy-benchmark`, 13★) is an evaluator, not a tutor. The previous pass's
  only EMEA candidate, `braiinz94/braiinz-education`, remains 0★ alpha. For EMEA
  engagements the *agent* layer is imported; the *platform* layer is now local
  and permissive — see `Selleo/mentingo` (MIT, Poland) in
  [`../repos/foundations.md`](../repos/foundations.md).
- **Three rows have no stated geographic origin** (`anki-mcp-server`,
  `SocialCoach`, `OpenTutor`) and are recorded as **Global** rather than guessed
  at. Region is a closed vocabulary here; inventing a value to fill a column is
  how a filter starts lying.
- **Two shelf candidates remain licence-unresolved** (`human-skill-tree` 586★,
  `Auto-Empirical-Research-Skills` 4,843★ CC BY-SA 4.0) and one shelved row is
  licence-defective (`mcp-canvas-lms`). Across three passes, **licence defects
  cluster in the agent layer, not the platform layer** — platforms state
  copyleft clearly; agents claim MIT loosely, or say nothing.
- **Star counts for the two leaders move by thousands per week.** DeepTutor read
  52,167 and OpenMAIC 41,981 at 09:40 UTC on 2026-10-31, both from the API, both
  pushed that same day. Any figure here is a timestamped reading, not a level.
- **No education-specific agent *observability* or *regression* tooling was
  found.** `pedagogy-benchmark` (knowledge) and `learning-commons-org/evaluators`
  (rubric scoring, licence-unresolved) are the only evaluation assets located;
  neither is a runtime monitor. A tutor in production has no open-source way to
  detect that it has drifted. This is the clearest unmet build opportunity on the
  page.
