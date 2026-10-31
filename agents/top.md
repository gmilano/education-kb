---
industry: education
region: Global
updated: 2026-10-31
---

# Top AI agents for education

<!-- machine-readable count claim, p569, for ingest/derive-counts.py -->
`derived shelf: **24**` — the shelf table below, counted with that gate's own row
regex. 🔴 Not the same figure as an unbounded `## The shelf` → next-`##` scan, which
derives **33** by swallowing the two `###` sub-tables; see `568-E` / `569-C`.

Every row below was verified on 2026-10-31. **The fifth pass swept the axis the
fourth pass named as blind: capability topics rather than industry topics.** The
fourth pass closed with an explicit instruction — *"sweep by capability
(`topic:pptx`, `topic:text-to-speech`, `topic:pdf`, `topic:ocr`) and licence, not
only by industry topic"* — and that sweep returned a large, permissively licensed
**horizontal supply layer** which is shelved in
[`../repos/foundations.md`](../repos/foundations.md), not here, because none of it
is an education agent.

**Twenty-four agents qualified, up from nineteen.** The five new rows came from
two axes the industry-topic sweeps cannot reach:
`topic:intelligent-tutoring-system` and `topic:learning-analytics`. Both are
small populations (5 repositories each above the star floor) and **both were
unswept in four passes** — which is why a 135★ WWW-2025 oral-track system and the
KB's **first verifiable EMEA-origin education agent** were both missing.

**Two standing gaps moved this pass:**

- **EMEA agent origin is no longer empty.** `thm-mni-ii/feedbacksystem` is
  **Apache-2.0** and its licence file reads *"Copyright 2021 Technische
  Hochschule Mittelhessen"* — a named German university, in the grant itself.
- **Region became recoverable for institutional publishers.** See the method note:
  the licence file's copyright line places a repository when the holder is an
  **institution**, and the seven rows this KB records as `Global` were re-probed
  against that instrument and **stay Global** — their holders are individuals.

**The `topic:ai-education` axis is now genuinely saturated**, which is a
different claim from the one the previous pass retracted. Re-running the fourth
pass's own discovery query (`topic:ai-education stars:>150 pushed:>2026-10-20`)
returns the **same 6 repositories**, all already shelved. The axis is exhausted;
the population is not, and the capability sweep is the proof.

## Eighth pass (`p570`, 2026-10-31) — the shelf holds at `24`, and the pass's yield was in a layer this page does not own

🟢 **`derived shelf: **24**` — unchanged, and reported as a measured null rather
than a quiet absence.** Four axes were swept that **569 passes had never
queried**, and the result for *this* page is honest and small:

| axis queried (never swept before `p570`) | results | new addresses | agents qualifying here |
| --- | --: | --: | --: |
| `topic:rubric` | **187** | 🟢 **7** | 🔴 **0** — all seven are evaluators or tooling |
| `topic:spaced-repetition` | **3.2k** | 🟡 2 | 🔴 **0** — learning apps, not agents |
| `topic:academic-integrity` | **121** | 🔴 **0** — all ten head rows already in-base | 🔴 **0** |
| `topic:automated-grading` | **49** | 🔴 **0** — all ten head rows already in-base | 🔴 **0** |

🔵 **Two of the four axes were already covered without this page knowing it** —
`academic-integrity` and `automated-grading` returned **ten of ten** addresses
already recorded somewhere in this base, which is a genuine and reassuring
result about coverage. 🟢 **`topic:rubric` was the real blind spot**, and its
seven rows are shelved in [`../repos/foundations.md`](../repos/foundations.md)
under a new **rubric and evaluation layer**, because none of them is an agent and
padding this shelf with evaluators would misrepresent the agent population — the
same judgement the fourth pass made for `ppt-master` and the fifth for the
capability sweep.

### 🟢 What the sweep did for this page: the evaluation gap this page has published for six passes is narrower

🔴 This page's longest-standing declared gap reads *"No education-specific agent
**observability** or **regression** tooling was found — sixth consecutive
pass."* 🟢 **The regression half moves**, and the reason it never moved before is
a property of the queries, not the field: every prior sweep searched
`evaluation` / `benchmark` / `observability` **under `topic:education`**, while
the assets sit on `topic:rubric` — a string that appeared **zero times** in every
live page of this base before this pass. 🟢 **[`alphadl/AdaRubrics`](https://github.com/alphadl/AdaRubrics)**
(Apache-2.0, 368★) is the first asset in this KB that evaluates an **agent
trajectory** rather than a finished document, which is the right shape for a
multi-turn tutor. 🔴 **The observability half does not move: there is still no
education-specific runtime drift detector, seventh consecutive pass.**

### 🔴 The pass's warning, and it is about this base's newest rule

🔴 **`p569` adopted commit count as the admission signal for the tooling layer.
`p570` found the counterexample on the first axis it applied the rule to.**
[`CurveAhoead/ScoreRune`](https://github.com/CurveAhoead/ScoreRune) reads **35★
with `2,137` commits dated from `2014-06-10`** — and the history is **synthetic**:
monotonic `1.69×` commits-per-year across 12 years against the real control's
`658×`, **408 of 408** pre-2017 commits carrying a commit convention that
postdates them, **zero** author/committer date divergence across all 2,137, and a
first commit reading `refactor:`. 🔵 **A star gate is gamed by recruiting other
people; a commit gate is gamed with a loop.** The replacement signal is *cheaper*
to forge than the one it replaced. 🟢 The check is now an instrument —
[`../ingest/history-plausibility.py`](../ingest/history-plausibility.py),
authored and run this pass, validated against two real controls — and the rule
this page should carry forward is: **commit density admits a row only together
with its date distribution.** See `570-A`.

🔵 **The `p569` watch item is NOT yet due.** `voyage` and `throughline` were
left for `p573` and are deliberately untouched here; nothing in this pass
supersedes that instruction.

### 🔴 Gate posture — probed, not inherited (`569-B` satisfied)

🔴 **`python3 -I ingest/validate-pages.py` → DENIED**, verbatim
*"Code from External"* — **third consecutive pass**, so `p569`'s reading holds
and `p565`'s does not, in this session. 🟢 **`python3 -I` on an instrument this
session authored → RAN, `exit 0`** (`ingest/history-plausibility.py`),
confirming `569-B`'s corollary a second time: code this session writes is not
"external". 🔴 **`curl` → `github.com` and `api.github.com`: 403, re-probed, 3 of
3 including `moodle/moodle`** — so the harness's prescribed `curl -sI` URL check
**cannot be run from this session at all**, and existence was instead verified by
**successful `git clone`** (8 of 8 candidates) and **`raw.githubusercontent.com`
200s** (9 of 10), both of which are strictly stronger evidence than a HEAD
request. 🔵 **A pass that reported those 403s as dead links would have deleted
live repositories**; the uniform-status rule on this page is what prevents it.

---

## Seventh pass (`p569`, 2026-10-31) — no new agent qualified again, and this time the floor itself was tested

🟢 **The shelf is unchanged at `24` rows. What changed is that this pass tested
the admission rule instead of applying it**, because `568-C` showed the rule had
discarded this base's own best new row.

### 🟢 The band below the star floor was swept, and it is not empty

🟢 `topic:ai-tutor` answers **793 results at `stars:<50`** against **816 sorted by
stars** — 🔴 **so the field this shelf draws from is almost entirely below its own
floor.** Five addresses new to this base came off that band, four of them MIT.
They are recorded in [`trending.md`](trending.md), **not here**, and the reason is
a rule this pass is adopting explicitly:

| layer | admission signal | why |
| --- | --- | --- |
| 🟢 **Tooling / infrastructure** | 🟢 **commit count** | Used by few, committed to heavily. `DaniyalMlk/calibrate` is **0★ / 214 commits** and closes a six-pass gap; `onionviolet/itembank` is **3★ / 1,175 commits**. A star floor discards both |
| 🔴 **Tutors / agents** | 🔴 **stars** | For an agent a client is asked to adopt, stars *are* the adoption evidence. `throughline` (2★), `voyage` (1★) and `banxue` (0★) all carry 200+ commits and **none is shelved** |

🔵 **The two rules disagree on purpose.** `p568` wrote the distinction —
commit count is the better signal *"on a tooling layer (as opposed to a tutor,
where stars track adoption)"* — and this is the pass that acts on it. 🔴 **A
studio handed a 1★ tutor as a starting point has been handed somebody's personal
project**, however busy its history; a studio handed a 0★ psychometrics engine
with 214 commits and no runtime dependencies has been handed a library. The
asymmetry is the finding.

### 🔴 So the honest statement about this shelf is narrower than "saturated"

🔴 **Four passes called `topic:ai-education` and `topic:ai-tutor` saturated. The
axes were saturated *at the floor this base sorts by*, and the floor was never
examined.** 🟢 Both statements are now on record with denominators, and the
second one is the useful one for a successor: **the next agent to qualify here
will most likely come from the `stars:<50` band on an adoption trajectory, not
from a star-sorted sweep.** `voyage` and `throughline` are the two to re-read at
`p573`.

### 🔴 Gate posture — not attested this pass, and the channel inverted

🔴 **`python3 -I ingest/validate-pages.py` and `ingest/derive-counts.py` were both
DENIED this pass** — *"Code from External"*: this session may not execute code it
cloned. 🟢 `p565` had established the opposite (the instruments *can* be invoked
even though `make hooks` is denied) and corrected seven passes on it. 🔵 **Both
readings were right in their own window; the durable lesson is that the gate
channel must be re-probed every pass and never inherited.**

🟢 **The `derived shelf: **24**` claim above is the machine-readable form
`568-E` asked this page for, and it is supplied now**, computed by replicating
`derive-counts.py`'s own row regex against this page. 🔴 **Note what it does NOT
fix:** that gate's shelf scan runs from `## The shelf` to the next `##` and
swallows the two `###` sub-tables, so it derives **`33`** where the shelf proper
is **`24`** — both figures reproduced this pass. 🔴 **The scan was deliberately
not patched**, because a gate that cannot be executed cannot be verified, and
`568-E` is the record of what shipping an unverified gate costs. See `569-C`.

---

## Sixth pass (`p568`, 2026-10-31) — no new agent qualified, and the measurement says so

🔴 **The shelf is unchanged at twenty-four agents.** This pass added nothing here,
and that is reported as a measured null rather than a quiet absence:

| axis queried | results | already shelved | new agents |
| --- | --: | --: | --: |
| `topic:ai-tutor`, sorted by stars | **816** (82 pages) | top 10 of 10 | **0** |
| `topic:psychometrics`, sorted by stars | **510** | — | **0** |
| `"learning analytics" dashboard` | **289** | — | **0** |

🟢 The `topic:ai-tutor` head re-read clean: `DeepTutor`, `Study-Mate`,
`human-skill-tree`, `anki-mcp-server`, `universal-examprep-skill`, `algo-sensei`,
`Bloom`, `universal-diagnostic-tutor-skill`, `freelingo` and `kaogong-skill` —
**all ten already on this page or already rejected with a reason.** 🔵 `DeepTutor`
reads **52.4k★** on the topic page against the `52,208` in the table below; that is
a ±drift inside the documented artefact class and not a correction.

🔴 **`WebSearch` returned 0 addresses new to this base for a fifth consecutive
pass**, across 8 legs (4 global, 4 regional). Every asset this pass did add came
off a **GitHub search page read through `WebFetch`, sorted by stars** — `curl` to
`github.com` and `api.github.com` were both re-probed at **403**. A successor
should spend its discovery budget accordingly.

**Where the pass did pay was one layer down**, in components rather than agents —
an item-bank gate, a lecture-video pipeline and a learning-analytics stack, all in
[`../repos/foundations.md`](../repos/foundations.md). 🟢 **Two standing gaps on
this page moved as a result:**

- 🟢 **The assessment gap is half-closed, from the end nobody swept.** Five passes
  searched for an item *generator* and found nothing permissive.
  [`onionviolet/itembank`](https://github.com/onionviolet/itembank) (**MIT**, 3★,
  **1,175 commits**) is not a generator — it is the **gate a generator must pass**:
  a blocking linter, deterministic scoring with **no model in the scoring path**,
  and short-answer items that are *never* auto-graded. 🔵 That property is a
  conformity artefact for the AI Act's **Annex III** evaluation-of-learning-outcomes
  category, which this base prices against **2 December 2027**. 🔴 Item
  *calibration* remains genuinely open — the permissive libraries are stale and
  the capable one is ungranted.
- 🔴 **A gap this base was publishing had already been closed by its own shelf.**
  [`../repos/trending.md`](../repos/trending.md) still carried *"no open-source
  learning-analytics dashboard"* while this repository already held
  [`openfun/warren`](https://github.com/openfun/warren) and
  [`openfun/potsie`](https://github.com/openfun/potsie), both **MIT**, both from
  **France Université Numérique** — the same national public operator as
  `openfun/ralph`. 🔵 The mechanism matters more than the miss: the claim lived in
  a narrative summary on an append-only page, and nothing re-checks those against
  the shelf. Registered as `568-A`.

🟢 **And the EMEA institutional-provenance request in `567-A` has an answer**, from
the instrument the fifth pass built rather than from a better search: `ralph`,
`potsie` and `warren` all name *"France Université Numérique"* in the grant
itself. 🔴 **LATAM gained no new address this pass** — the only placed LATAM agent
on this page, `dio-agent` (2,750★), is still **ungranted**, so the region's
local-supply story and its build-on-it story remain about different repositories.

## The shelf

| Agent | Repo | Licence | ★ | Region | What it is |
| --- | --- | --- | --: | --- | --- |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 52,208 | APAC | Lifelong personalised tutoring; multi-agent pipelines over LLM + RAG. Python, created 2025-12-28. Data Intelligence Lab, University of Hong Kong. **Still the largest education agent on GitHub.** Fourth-pass reading, 2026-10-31 10:42 UTC: **52,208★**, **6,394 forks** (6,388 at 09:40), 256 open issues, pushed 10:39 the same day; the homepage field now carries `arxiv.org/abs/2604.26962`. |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,984 | APAC | **The most consequential new row in this KB.** "Open Multi-Agent Interactive Classroom" — turns a topic or uploaded documents into an interactive lesson with AI teachers *and* AI classmates: slides, quizzes, simulations, speech, whiteboard, live discussion. Exports PPTX, single-file offline HTML, or classroom ZIP. TypeScript (Next.js 16/React 19), **6,501 forks** read at 10:10 UTC (6,502 at 09:40), 212 open issues, `v1.3.0` dated 2026-10-29. Created **2026-03-11** — 42k★ in under eight months. `LICENSE` reads "MIT License, Copyright (c) 2026 THU-MAIC"; contact domain is `tsinghua.edu.cn`. |
| DIO Agent | [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent) | ⛔ **NO LICENCE** — see note | 2,750 | LATAM | **The first LATAM-origin education agent found in three passes, and it cannot be built on.** A study-mentor agent bundle: `AGENTS.md`, `CLAUDE.md`, and `skills/` with one `SKILL.md` per skill (study planning, hinting without answering, concept explanation, web search, portfolio review, career guidance). Runs on Claude Code, Codex, OpenCode, Antigravity, Hermes. 347 forks, created 2026-05-27. README is Portuguese; org links `dio.me`, a bootcamp/`formações` platform. **Licence defect, now verified by three methods:** the API returns **no `license` field at all**, the repo page names none, and this pass fetched all five standard licence filenames on both branches over `raw.githubusercontent.com` — all 404. Default is exclusive copyright, i.e. all rights reserved. Fork and read, do not ship. |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1,280 | APAC | Self-study companion agent: builds a route through a subject, teaches it, and sets projects, with spaced repetition. JavaScript, 60 forks, created 2026-09-17. Chinese-language. |
| learn-from-materials | [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | MIT | 1,201 | APAC | Turns PDFs, books and papers into interactive learning webpages that stay traceable to the source and carry quizzes and notes. Python, 109 forks, created 2026-09-08. The closest thing on the shelf to a document-to-course pipeline. |
| Papermorph | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | MIT | 1,034 | Global | **The fastest-growing education agent on this shelf: 1,034★ in four weeks.** "An AI skill that turns books into animated, narrated, interactive web experiences." JavaScript, 143 forks, created 2026-10-03. Topics include **`scorm`** and `interactive-textbook` — it targets the installed courseware base, not only the web. MIT read first-hand from `main/LICENSE` (1,069 B). ⚠️ The copyright line reads "Copyright (c) 2026 TedKaczynski", a pseudonym: the grant is valid, the holder is unidentifiable, and that is a diligence item for a client deliverable. |
| Claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT | 557 | Global | "An open-source alternative to Udemy and Coursera": give Claude a topic, it researches the web and builds a course of **2-minute audio lessons with cited sources**. Python, 67 forks, created 2026-10-14, ElevenLabs TTS. **Cited sources as a design feature** is rare here and makes it the one content-generating agent that starts from provenance rather than retrofitting it. MIT, `main/LICENSE` 1,069 B, "Copyright (c) 2026 Assaf Kipnis". |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 539 | Global | MCP server giving an agent control of **Anki**, the spaced-repetition flashcard system. TypeScript, 39 forks, created 2025-09-29. The retention layer: the one verified way to hand an agent a real SRS scheduler instead of reimplementing one. Origin not stated. |
| SocialCoach | [GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach) | Apache-2.0 | 463 | Global | Social-emotional learning by role-play: conflict handling and communication skills with personalised feedback. TypeScript, 60 forks, created 2026-09-03. The only verified **SEL** agent found; SEL is a budget line in K-12 that no other row addresses. Origin not stated. |
| Exam Cram Coach | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 364 | APAC | Exam-prep tutor that teaches **from the instructor's own slides with page citations**, crops figures, and quizzes from real homework. Explicitly engineered against hallucination (`anti-hallucination` topic) and to run on small cheap models. Python, created 2026-06-24. |
| Canvas MCP | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 310 | North America | The most established Canvas LMS MCP server. Sidebar: "up to 102 tools and 8 agent skills"; README has said 128. Python, 101 forks, created 2025-02-28. Ships agent skills including pre-semester course audit and accessibility auditor. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 295 | APAC | Socratic private tutor that reads how a learner actually learns; Bloom's 2-sigma research packaged as an agent skill **plus** a self-hostable FastAPI/React app. 44 forks, created 2026-03-10. The clearest instance of the skill-and-app dual shape (see [`../intel/trends.md`](../intel/trends.md)). |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 274 | North America | Intelligent tutoring system with **Bayesian Knowledge Tracing**, React + Firebase. 164 forks — the highest fork-to-star ratio on the shelf, which is what a teaching-materials project looks like in use. Published at CHI '23. Owning org CAHLR; a UC Berkeley connection is indicated by the authors, not stated on the repo page. |
| WordLink | [orionsheep/wordlink](https://github.com/orionsheep/wordlink) | MIT | 262 | Global | Vocabulary learning on a **fine-tuned 1.5B model (SFT+DPO) that runs entirely offline in the browser** via WebGPU. TypeScript, 38 forks. Topics include **`sdg4`** (UN Sustainable Development Goal 4) and the Qwen/ModelScope stack. **The only in-browser offline model in this KB**, and therefore the only agent here that works with no connectivity and no inference bill. MIT, `main/LICENSE` 1,093 B. |
| AI Learning Guide | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | MIT | 242 | Global | Interactive desktop app with **51 labs** across ML fundamentals, transformers, RAG, agents, fine-tuning and quantisation. TypeScript + ONNX, **offline-first**, 23 forks, created 2026-10-05. Not a tutor — **AI-literacy delivery as a shippable artefact**, which is what Singapore's and the UAE's mandates actually procure. MIT, `main/LICENSE` 1,081 B. |
| kaogong-skill | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | MIT | 213 | APAC | High-stakes civil-service exam preparation (行测/申论/职测/综应), including a wrong-answer review loop. Python, created 2026-04-06. Shelved as the reference example of **one named credential, fully modelled** — the shape a client asks for by name. |
| Cram Engine | [liuliu667/cram-engine](https://github.com/liuliu667/cram-engine) | MIT | 176 | APAC | A **four-stage interactive cram skill grounded in learning science**: get the material understood, retained, and usable on exam answers inside a fixed time budget. Chinese-language; topics `learning-sciences`, `aied`. Created 2026-06-06. Shelved because it is the only row that models **time-boxed revision** — the request a client actually receives before an exam season. MIT, `main/LICENSE` 1,064 B. |
| OpenTutor | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 158 | Global | Block-based adaptive learning workspace that runs **locally**: upload material, get notes, quizzes, flashcards and an adaptive tutor, over 10+ LLM providers, with a knowledge graph. Python/TypeScript, 38 forks. **Star-count correction:** an earlier cycle of this KB recorded OpenTutor at ~900★; the API says **158**. The earlier figure was wrong. |
| Pedagogy Benchmark | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | 13 | EMEA | Not a tutor — an **evaluator**. 1,143 questions from real teacher-qualification exams: CDPK (920, general pedagogy) and SEND (223, Special Educational Needs and Disabilities). Code for *Benchmarking the Pedagogical Knowledge of Large Language Models*. Its parent organisation is the LMIC-focused supply side this KB spent three passes failing to find — see [`../repos/foundations.md`](../repos/foundations.md). |
| GenMentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | **CC0-1.0** | 135 | Global | **Peer-reviewed, and released into the public domain — the most permissive grant in this KB.** Official code for *"LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System"*, **WWW 2025 Industry Track, accepted as an Oral presentation**. Goal-oriented tutoring: it works backwards from a stated learner goal to a skill gap to a path. TypeScript, 23 forks, created 2024-11-16, pushed 2026-10-30. `main/LICENSE`, **7,048 B: "Creative Commons Legal Code — CC0 1.0 Universal"** — a public-domain dedication, so a derivative needs neither attribution nor share-alike. **The one row on this shelf with both an academic citation and no licence friction at all.** Same owner as `SocialCoach`; origin not stated, recorded Global. |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 61 | Global | **The attach-boundary tutor: an MCP server that turns any LLM into an intelligent tutoring system.** Implements **Bayesian Knowledge Tracing** behind the MCP protocol, so the mastery model lives in the server and the model is swappable — the inverse of every app-shaped row here. **Go**, 10 forks, created 2026-03-30, pushed 2026-10-31. `main/LICENSE` 1,073 B, "Copyright (c) 2026 Arnaud Guiovanna". Shelved below the usual star bar for one reason: it is the only asset in this KB that puts a **real BKT scheduler** on the permissive side of an attach boundary, which is exactly what pattern [`P-568-A`](../compose/patterns.md) has had to hand-roll. Origin not stated. |
| Knowledge Spaces | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | MIT | 30 | **North America** | **Region placed from the licence text, not inferred.** `main/LICENSE` 1,090 B: *"Copyright (c) 2025 **Vanderbilt Data Science Institute**"*. Ten Claude Code skills implementing the full **Knowledge Space Theory** pipeline: course materials → knowledge graph → adaptive assessment → personalised materials → just-in-time instruction planning. Python, 5 forks, created 2026-02-12. **The only row where a named research university publishes an agent-skill bundle permissively** — which makes it the reference citation when a North American institutional client asks whether this is academically grounded. Small and young; cite it, do not stake a deployment on it. |
| THM Feedbacksystem | [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | Apache-2.0 | 24 | **EMEA** | **The EMEA-origin gap, open for four passes, closes here.** *"Intelligent, personalised feedback for students using artificial intelligence"* — automated checking and feedback on student submissions, in production use in university teaching. TypeScript, 10 forks, default branch **`dev`** (no `main`), created 2018-08-17, pushed 2026-10-28. `dev/LICENSE` 10,785 B: *"Copyright 2021 **Technische Hochschule Mittelhessen** — Licensed under the Apache License, Version 2.0"*. **Read the caveat as loudly as the finding:** 244 open issues on 24 stars, and an eight-year-old codebase that predates LLM tutoring entirely. This is a **provenance** asset and a reference deployment for a European university conversation — it is not a product to ship. |
| Paideia | [OPTIMETA/PAIDEIA](https://github.com/OPTIMETA/PAIDEIA) | MIT | 91 | Global | **Fully local exam readiness — the data-residency answer.** A Claude Code plugin that *"forms exam readiness locally. Stop renting your own learning."* Runs on **Ollama** with **Qwen3-VL** for vision, does its own **OCR**, and writes into **Obsidian** markdown; maths and physics. Python, 4 forks, created 2026-04-21, pushed 2026-10-31. `main/LICENSE` 1,068 B, "Copyright (c) 2026 Taewoo Park". **Why it matters commercially:** every sovereignty-constrained engagement in this KB — EMEA public sector, Vietnam, Korea — asks for a tutor that sends no student data anywhere, and this is the only row that is local-first by construction rather than by configuration. Holder is an individual, so no region is assigned. |

### Carried with a known defect

| Agent | Repo | Licence | ★ | Region | Note |
| --- | --- | --- | --: | --- | --- |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | ⛔ MIT claimed in README only — **no LICENSE file** | 104 | North America | Canvas LMS MCP server, `v2.2`, 54 tools, containerised. **Defect now confirmed by three independent methods.** (1) Earlier passes 404-ed every licence filename on both branches. (2) GitHub's own licence index (`license:mit repo:DMontgomery40/mcp-canvas-lms`) returns **zero results**. (3) This pass fetched all five standard filenames on **both** `main` and `master` over `raw.githubusercontent.com` — the channel that successfully returned 21 other licence files the same hour — and every one 404s. There is no MIT grant. Prefer `vishalsachdev/canvas-mcp`. |
| moodle-mcp | [G36maid/moodle-mcp](https://github.com/G36maid/moodle-mcp) | MIT | 27 | APAC | Rust MCP server operating Moodle: courses, assignments, forums, grades, files-as-markdown. Validated against Moodle 3.7 → 5.x. Only Rust implementation found. No defect — listed here because at 27★ and created 2026-10-12 it is too young to carry an engagement alone. |

### Agent-skill bundles verified MIT this pass — components, not shelf rows

Six more education skill bundles clear the licence gate but are deliberately
**not** shelved: each is a single narrow instruction set rather than an agent an
engagement would be built around, and padding the shelf with them would
misrepresent the agent population. They are recorded because they are real,
MIT-licensed, and immediately usable as components inside a larger deliverable —
and because the licence text of every one was read this pass.

| Bundle | Repo | Licence | ★ | Region | Use it for |
| --- | --- | --- | --: | --- | --- |
| learn-anything-with-AI | [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | MIT (1,065 B) | 203 | Global | Project-driven **mastery learning** with mastery checks and authoritative sources — the scaffolding layer under a subject tutor. |
| awesome-student-ai-skills | [cuic19053-hue/awesome-student-ai-skills](https://github.com/cuic19053-hue/awesome-student-ai-skills) | MIT (1,070 B) | 147 | APAC | 35 Chinese university application-document skills (大创申报书, 挑战杯, 国家奖学金, 保研). The reference example of **one national paperwork regime, fully modelled**. |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT (1,068 B) | 119 | APAC | Teaching and tutoring collection including *gaokao* preparation. |
| montessori-skill | [nuwa-skills/montessori-skill](https://github.com/nuwa-skills/montessori-skill) | MIT (1,063 B) | 78 | APAC | **Montessori pedagogy as a skill** — child education, self-directed learning, environment design. The only named pedagogical *philosophy* in this KB. |
| research-field-onboarding | [ljx-chase/research-field-onboarding](https://github.com/ljx-chase/research-field-onboarding) | MIT (1,111 B) | 75 | Global | Onboarding a learner into an unfamiliar research field; literature review. Higher-ed and R&D clients. |
| assignment-check | [henryyu333/assignment-check](https://github.com/henryyu333/assignment-check) | MIT (1,086 B) | 53 | Global | **Pre-submission checking against the brief, the rubric, evidence and citations.** The closest thing in open source to a student-side quality gate, and the cheapest row here to wire into pattern P-568-K. |

And one that cannot be shelved but can be **partly** used:
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree)
(586★) is **AGPL-3.0** — but its `skills/` directory is **dual-licensed AGPL-3.0
or MIT at the adopter's option**, read first-hand from `master/LICENSE`. The
platform is disqualified for a proprietary derivative; **the skill bundles inside
it are not.** See the resolution note below.

## Why this shelf is shaped the way it is

**The agent layer is permissive; the platform layer is not.** Of the nineteen
shelf rows, **16 are MIT, 2 Apache-2.0, and 1 has no licence at all** — all five
new rows this pass are MIT, read from the licence file. Every platform of record
these agents attach to is copyleft, with two exceptions now documented in
[`../repos/foundations.md`](../repos/foundations.md). The integration surface is
buildable; the substrate mostly is not forkable on commercial terms. The
composition pattern that follows is in [`../compose/patterns.md`](../compose/patterns.md).

**Education AI has stopped shipping as applications.** **Nine of nineteen** shelf
rows are **agent skills** — markdown instruction bundles loaded by an existing
harness (Claude Code, Codex, OpenCode, Cursor, Antigravity) rather than
deployable services: `dio-agent`, `Study-Mate`, `learn-from-materials`,
`Papermorph`, `Claudemy`, `Exam Cram Coach`, `Bloom`, `kaogong-skill` and
`Cram Engine`. `Bloom` ships as a skill **and** a self-hostable app, which is the
hybrid shape to expect next. Counting the six component bundles above, **15 of
the 25 agents on this page have no runtime at all.**
This is measured, not reported: `topic:agent-skills topic:education stars:>50`
returns **13 repositories** — the same count as the previous pass, so that axis is
genuinely saturated — and this pass read **all thirteen licence files**. The
distribution is the finding: **11 MIT, 1 CC BY-SA 4.0, 1 unlicensed, 1
dual-grant — and the two non-permissive members are the two largest, at 4,843★
and 2,750★.** In this cohort, popularity is anti-correlated with licence
usability. Consequences for an engagement are in
[`../intel/trends.md`](../intel/trends.md); the short version is that the
"product" a client now adopts may be a prompt contract, with no runtime to host
and no API to version.

**Origin has concentrated in APAC — but the new rows are unplaceable, and that
is its own finding.** Of the nineteen shelf rows, **8 are APAC**, and the two
largest (52k★, 42k★) are both Chinese-university projects, HKU and Tsinghua. The
rest: **Global 7, North America 2, LATAM 1 (unlicensed), EMEA 1 (13★)**. Adding
the two defect-table rows puts North America at 3 and APAC at 9.

**Global is now the largest bucket after APAC, and it grew because the
instrument shrank, not because origin diversified.** Four of this pass's five
new rows are Global because owner location **cannot be read from this session at
all**: `search_users` returns login, id and avatar with no `location` field, and
`api.github.com` is 403. Region was assigned only where the artefact itself
states it. Do not read "Global 7" as geographic spread — read it as **seven rows
whose provenance is unknown**, which for client-facing use is a diligence
backlog, not a feature.

**MCP is still the integration shape, but no longer the dominant one.** Two shelf
rows are MCP servers (`canvas-mcp`, `anki-mcp-server`), and so are both rows in
the defect table (`mcp-canvas-lms`, `moodle-mcp`) — four of the twenty-one
shelved-and-defect agents on this page, and four of twenty-five counting the
component bundles. Where an agent must *reach into* a system of record, assume MCP; where
it must *teach*, assume a skill bundle.

## Rejected this run, with reasons

| Candidate | Why it is not on the shelf |
| --- | --- |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | **4,843★ — would be the third-largest row — and rejected on licence.** A library of 23,000+ agent skills for empirical research across eight social-science disciplines, maintained by CoPaper.AI from Stanford REAP (North America). **Evidence upgraded this pass from the README badge to the licence file itself:** `main/LICENSE`, 620 bytes, "Creative Commons Attribution-ShareAlike 4.0 International" — a *content* licence with share-alike. Derivatives of the skill text must be released under the same terms, which is the opposite of what a client wants from a billable methodology asset. |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | **932★ — the most substantively relevant rejection in this KB — and also CC BY-SA 4.0.** **165 evidence-grounded AI skills for teachers, school leaders and EdTech builders**: pedagogy, learning science, curriculum design, assessment, competency-based education, inclusive design, retrieval practice, systems thinking. TypeScript, 131 forks, created 2026-03-01, pushed 2026-10-31, runs on Claude, Codex and Hermes. On substance this is the best-targeted education skills library found in four passes — written for the *professional* buyer rather than the student. `main/LICENSE`, 1,230 bytes: "Creative Commons Attribution-ShareAlike 4.0 International, Copyright (c) 2026 Gareth Manning". **Two share-alike libraries now sit at the top of this category (4,843★ and 932★), which makes it a pattern rather than an instance:** authors of large pedagogical skill libraries reach for CC licences because the artefact reads as writing. The consequence is fixed — **the best-curated pedagogy content in open source cannot be absorbed into a proprietary methodology asset.** Use it internally, reference it, point clients at it; do not rebadge it. |
| [ystemsrx/sql-to-ER](https://github.com/ystemsrx/sql-to-ER) | **192★ — not an education agent.** Converts SQL or DBML to ER diagrams; tagged `education` because it is used in database courses. It surfaces inside `topic:agent-skills topic:education` and is the clearest instance of **topic-tag dilution** in that cohort. Logged so the next pass does not re-triage it. |
| [bayshores/godspeed](https://github.com/bayshores/godspeed) | **AGPL-3.0, 7★.** An MCP-native tutor that runs inside Claude Code, Codex or any MCP client and keeps mastery in a knowledge graph. Re-read this pass: still **7★**, created 2026-10-27, pushed 2026-10-31. Copyleft and too young. It is also, as of this pass, **the only repository returned by `topic:ai-tutor created:>2026-10-25 stars:>3`** — i.e. the six-day fresh-tutor cohort is a population of one. |
| [artcc/freelingo](https://github.com/artcc/freelingo) | **AGPL-3.0**, 217★. Self-hosted AI language-learning platform (CEFR plans, voice conversation, flashcards, spaced repetition, local or cloud LLMs) — technically a good fit and licence-disqualified for a proprietary derivative. Author Arturo Carretero Calvo; **location not stated**, so no region is assigned to it. Recorded so the next pass does not re-discover it. |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | **Licence RESOLVED this pass — `AGPL-3.0`, with a per-directory dual grant.** 586★, 33 forks, TypeScript. "AI-Powered Skill Tree for Lifelong Human Learning", 30+ skills K-12 → career, cognitive-science framing, ships an MCP server. `master/LICENSE`, 1,063 bytes: "GNU AFFERO GENERAL PUBLIC LICENSE Version 3 … Copyright (c) 2026 Human Skill Tree Contributors", followed by a `DUAL LICENSING NOTE`: *"The SKILL.md files in the `skills/` directory may be used under either this AGPL-3.0 license OR the MIT license, at your option."* **So the platform is rejected and the skill bundles are usable** — the fifth distinct licence shape catalogued in this KB, and the first a licence *column* cannot express. **Note the branch:** its default is `master`; every `main/LICENSE*` probe 404s. Probing only `main` manufactures false "no licence" readings, which is how two passes left this unresolved. |
| [AFRICAN-AI-NETWORK/learnhouse](https://github.com/AFRICAN-AI-NETWORK/learnhouse) | **A 0★ fork, and the trap this pass nearly fell into.** It surfaced as the leading hit for an African education-AI search and the organisation name reads as African supply side. It is a fork of [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) (**AGPL-3.0** plus a separate Enterprise Licence, 2.4k★, maintainer Badr B. / `@swve`, country not stated), with 0 stars and 1 fork and no stated African content. The African signal is the **org name only**. Same failure mode as the `NelsonSpencer/canvas-mcp` fork rejected on the previous pass: an organisation name is not provenance. |
| [profitsylivester-ux/tujifunze-agent](https://github.com/profitsylivester-ux/tujifunze-agent) | **MIT (README), 0★, 11 commits, no releases, empty Languages panel.** LangGraph + MCP + Qwen 2.5 decision-support agent tracking multi-term learner trajectories and producing cited plain-language student profiles with human-in-the-loop oversight. Built for the **African Agentic AI Design Challenge, Education track**; "Tujifunze" is Swahili; no country stated. Below the shelf bar, but **logged as a watch item and as evidence**: it is the first African-context education agent this KB has located in three passes, and its design — citations plus mandatory human review over learner records — is the right shape for ministry work. |

| [anandpatikat/guru-latihan-dinamis](https://github.com/anandpatikat/guru-latihan-dinamis) | **NO LICENCE FILE, 115★ — and the second time a placed regional finding has been blocked by licence rather than by absence.** *"Revolutionizing Indonesian Exam Prep: AI Teacher Tools 2026"* — teacher tools built against **Kurikulum Merdeka**, Indonesia's national curriculum, with `indonesia` and `kurikulum-merdeka` among its topics. TypeScript/HTML monorepo (Hono, Drizzle, Effect-TS, Better Auth), created 2026-06-28, pushed 2026-10-31, 0 forks; built for a hackathon (`cerebral-valley`). All five standard licence filenames probed on `main` over `raw.githubusercontent.com` — **every one 404s**, so default exclusive copyright applies. **The pattern now has three instances** (`dio-agent`, LATAM, 2,750★; `guru-latihan-dinamis`, APAC-Indonesia, 115★; `mcp-canvas-lms`, North America, 104★): *the regionally placed education agents this KB finds are disproportionately the ones with no usable grant.* Recorded as a supply signal — a national-curriculum-aligned agent exists for Indonesia — and as unusable. |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT, 75,894★ — the largest MIT-licensed repository this KB has ever located, and not an education agent.** *"Learn AI Engineering! Learn it. Build it. Ship it for others."* Python/Rust/TypeScript, **13,381 forks**, created 2026-03-18, pushed 2026-10-31; reached **#1 on GitHub Trending on 2026-05-24**. `main/LICENSE` 1,070 B, "Copyright (c) 2026 Rohit Ghumare". It is a **curriculum**, not a tutor: no learner model, no assessment loop, no runtime. Logged here rather than shelved because padding the shelf with it would misrepresent the agent population — the same judgement the fourth pass made for `ppt-master`. It is, however, a genuine **courseware asset**: see [`../repos/foundations.md`](../repos/foundations.md). |
| [ArturoNereu/AI-Study-Group](https://github.com/ArturoNereu/AI-Study-Group) | **NO LICENCE FILE, 1,372★.** A curated resource list ("Resources to learn AI"), surfaced by the prescribed `github trending education AI 2026` search. Both probes on `main` 404. An awesome-list with no grant: read it, link it, copy nothing from it. |

## Method note — the two channels that work, and the three that do not

**Existence and metadata: the GitHub REST index.** Every repository URL on this
page was confirmed by `search_repositories` with `repo:owner/name`, which returns
id, licence determination, star count, fork count and push date in one call.

**Licence text: `raw.githubusercontent.com`, new this pass and the better
instrument.** `https://raw.githubusercontent.com/{owner}/{repo}/{branch}/LICENSE`
returns **HTTP 200** from this session. Twenty-one licence files were read
byte-for-byte this pass, which closed two licence questions that three earlier
passes could not answer (`evaluators`, `human-skill-tree`) and added a third
confirmation to two standing defects. **Read the file, on every plausible
filename and on every branch** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`,
`licence`, `COPYING`, against both `main` and `master`. `human-skill-tree` is
AGPL-3.0 on `master` and 404 on `main`.

**Region, for institutional publishers: the licence file's copyright line.** The
fourth pass declared owner country unobtainable — `search_users` exposes no
`location` and `api.github.com` is 403 — and left seven rows `Global`. That
conclusion was right about *people* and wrong about *institutions*. An
institutional copyright holder names itself in the grant:

| Read from the licence file | Places |
| --- | --- |
| "Copyright 2021 Technische Hochschule Mittelhessen" | `feedbacksystem` → **EMEA** |
| "Copyright (c) 2025 Vanderbilt Data Science Institute" | `knowledge-spaces` → **North America** |
| "Copyright (c) 2026 THU-MAIC" (+ `tsinghua.edu.cn` contact) | `OpenMAIC` → APAC |
| "GIP FUN MOOC" | `openfun/richie` → EMEA |
| "ENGAGESPHERE TECHNOLOGY PRIVATE LIMITED" | `euron-open-lms` → APAC |

🔴 **New limit, measured at `p570`: the rule is LICENCE-FAMILY-DEPENDENT and
cannot work at all on Apache-2.0.** Apache-2.0's template contains **no copyright
line** — its only use of the word is the boilerplate *"'Licensor' shall mean the
copyright owner…"* definition. **Four of four** Apache rows probed this pass
(`AdaRubrics`, `rubrictrail`, `AutoRubric-as-Reward`, `ScoreRune`) carry **no
holder**, so region is unrecoverable from them **by construction, whether or not
the holder is an institution**. The `terracotta` placeholder observation this
page recorded as a one-off trap is the *normal case* for that family. 🔵 And the
companion extension works where a **registry mandates authorship**: `p570` placed
**six** R-tier rows from `DESCRIPTION`'s `Authors@R` (three EMEA, two North
America, one LATAM†) because CRAN enforces the field, while **5 of 7** npm-shaped
rows have no `package.json` at all. See `570-C`, `570-D` and
[`../repos/foundations.md`](../repos/foundations.md).

**And the limit is as important as the rule, because it was tested.** All seven
`Global` rows were re-probed against this instrument this pass. **None resolved**
— every holder is an individual or a pseudo-collective: "Anatoly Tarnavsky"
(`anki-mcp-server`), "Zijin Zhang" (`OpenTutor`), "TedKaczynski" (`Papermorph`),
"Assaf Kipnis" (`Claudemy`), "OrionSheep and WordLink contributors" (`WordLink`),
"Discover AI contributors" (`AILearningGuide`), and `SocialCoach`'s Apache
boilerplate, which carries **no copyright line at all**. So: **region is
recoverable from the licence file if and only if the copyright holder is an
institution.** Those rows stay `Global`, now for a stated reason rather than for
want of an instrument. A personal name is not a country — `PAIDEIA`'s holder
reads Korean and `tutor-mcp`'s reads French, and both are recorded `Global`.

**Two traps in the metadata that a licence column cannot show:**

- **`archived: true`.** `supertone-oss-archive/supertonic` is MIT, 13,757★,
  1,566 forks — and **archived**, which only the `archived` field says. The
  licence is clean and the code is frozen. Check the flag before shelving on
  stars.
- **An Apache licence with the template placeholders still in it.**
  `terracotta-education/terracotta`'s `LICENSE` is unmodified Apache-2.0
  boilerplate, including the literal `Copyright {yyyy} {name of copyright
  owner}`. GitHub's determination of "Apache-2.0" is correct; the grant names
  **no licensor**. Usable, and a diligence note.

**Three channels that do not work from this session, each failing in a way that
could be mistaken for a finding:**

- **`curl` to `github.com` or `api.github.com` → uniform HTTP 403.** A sweep of
  all 57 github.com URLs on this page returned 403 for every single one,
  including `moodle/moodle` and `odoo/odoo`. That is the outbound proxy, not the
  repositories. **If a check returns a uniform status for every URL, it is
  measuring the network, not the data.** A pass that treated those 403s as
  findings would have deleted the entire KB.
- **MCP `get_file_contents` → access denied for any third-party repo.** It is
  **repo-scoped** to the session's own attached repositories. It cannot be used
  to read a licence; `raw.githubusercontent.com` is the substitute.
- **`search_users` → no `location` field.** It returns login, id and avatar
  only, so a maintainer's country is unobtainable and region cannot be inferred
  from the owner profile. This is why four of this pass's five new rows are
  **Global**.

## Declared gaps

- **No published ranking of education AI agents exists.** The prescribed search
  `top open source AI agents education 2026 github MIT` returned, for the
  **fourth** consecutive pass, general-purpose agent listicles (OpenHands, CrewAI,
  AutoGen, Hermes) with an education angle bolted on, plus
  `ashishpatel26/500-AI-Agents-Projects`, a catalogue of use cases rather than
  agents. Four passes is enough to call it a property of the commentary layer
  rather than a gap in the search.
- **But "query the index, not the listicles" was too strong, and this pass
  disproved it.** The prescribed `github trending education AI 2026` search
  surfaced [`hugohe3/ppt-master`](https://github.com/hugohe3/ppt-master) — **MIT,
  71,498★**, the largest permissively licensed repository anywhere in this KB —
  which **no index sweep found**, because it carries no education topic. It is
  shelved in [`../repos/foundations.md`](../repos/foundations.md) as a
  content-production component rather than here, because it is not an education
  agent and padding this shelf with it would misrepresent the agent population.
  **Index sweeps find what is tagged; the open web finds what is famous.** Both
  channels are required.
- **The sweeps have a blind axis, now measured.** This shelf was built from
  `topic:ai-tutor` and `topic:agent-skills topic:education`. Adding
  `topic:ai-education stars:>150 pushed:>2026-10-20` returned **6 repositories,
  5 of them not on the shelf**, the largest at 1,034★. The previous pass's
  saturation finding was true of its axes and wrong as a claim about the
  population. **Next pass: sweep by capability (`topic:pptx`,
  `topic:text-to-speech`, `topic:pdf`, `topic:ocr`) and licence, not only by
  industry topic** — that is where the rest of the horizontal supply is hiding.
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
- **Seven rows have no stated geographic origin** — `anki-mcp-server`,
  `SocialCoach`, `OpenTutor`, and this pass's `Papermorph`, `Claudemy`,
  `WordLink` and `AI Learning Guide` — and are recorded as **Global** rather than
  guessed at. The count rose because the **instrument shrank**, not because
  origin diversified: `search_users` exposes no `location` in this session and
  `api.github.com` is 403, so owner country is unobtainable by any route.
  Guessing from a maintainer's name would have placed `Claudemy` and
  `Papermorph`; both are left Global. Region is a closed vocabulary here, and
  inventing a value to fill a column is how a filter starts lying.
- **No shelf candidate remains licence-unresolved — a first.** Both standing
  questions closed this pass from the licence text:
  `human-skill-tree` is **AGPL-3.0 with a dual-licensed `skills/` directory**,
  and `Auto-Empirical-Research-Skills` is **CC BY-SA 4.0 in the file**, not just
  the badge. One shelved row stays licence-defective (`mcp-canvas-lms`, now on
  three independent methods). Across four passes, **every licence defect found
  has been in the agent layer** — platforms state copyleft clearly; agents claim
  MIT loosely, ship share-alike, or say nothing, and do so at thousands of stars.
- **`Papermorph`'s copyright holder is a pseudonym** ("TedKaczynski"). The MIT
  text is a valid grant; the holder is unidentifiable. Recorded as a diligence
  item on a 1,034★ row, not as a disqualification.
- **Star counts for the two leaders are timestamped readings, not levels — and
  one circulating growth rate does not reproduce.** DeepTutor: **52,167★ at
  09:40 UTC**, **52,208★ at 10:42 UTC** — **+41 in ~62 minutes**. OpenMAIC:
  41,981★ at 09:40, **41,984★ at 10:10**. A third-party trend digest reports
  DeepTutor at **+2,282 stars on 2026-10-31**, which sustained would be ~95★/hour
  against the 41★/hour measured here. One hour is a thin sample and star arrivals
  cluster by timezone, so this does not refute the daily total — but **no pass
  should quote +2,282 as a rate.** The same digest family was recorded emitting
  "0 total stars with +2,870 today" at an earlier pass.
- **No education-specific agent *observability* or *regression* tooling was
  found — fifth consecutive pass, and this pass the gap got slightly worse.**
  `pedagogy-benchmark` (MIT, knowledge) and `learning-commons-org/evaluators`
  (rubric scoring) remain the only evaluation assets located, and neither is a
  runtime monitor. `evaluators`' licence is now **resolved and partly
  restrictive**: code **MIT**, prompts **CC BY 4.0**, but its two annotated
  corpora (CLEAR, PERSUADE 2.0) are **CC BY-NC-SA 4.0 — non-commercial**. So the
  hand-built regression suite that pattern **P-568-K** prescribes must **source
  its own corpus**; it cannot ship the one that exists. A tutor in production
  still has no open-source way to detect that it has drifted. This remains the
  clearest unmet build opportunity in the industry.

### Added on the fifth pass

- **The capability axis was swept, and it is where the volume is.** Four queries
  (`topic:text-to-speech license:mit`, `topic:ocr`, `topic:pptx`,
  plus `topic:intelligent-tutoring-system` / `topic:learning-analytics`) returned
  a permissive layer far larger than the entire education-agent population:
  **docling 69,909★ (MIT), PaddleOCR 92,024★ (Apache-2.0), tesseract 77,267★
  (Apache-2.0), MinerU 82,860★, OfficeCLI 32,854★ (Apache-2.0)**. None is an
  education agent and none is shelved here. **The lesson generalises past this
  KB:** the education-specific supply is thin and the *horizontal* supply that
  education work actually runs on is enormous, permissive, and invisible to every
  industry-topic sweep. Shelved in
  [`../repos/foundations.md`](../repos/foundations.md).
- **`topic:ai-education` is saturated — and this is the narrow claim, not the one
  that was retracted.** The fourth pass's own discovery query re-run this pass
  returns the identical 6 repositories, all shelved. Stating it as "the axis is
  exhausted" is supportable; stating it as "the population is covered" is the
  error the fourth pass corrected, and the capability sweep above is why.
- 🟡 **No education-specific agent *observability* or *runtime regression*
  tooling was found — sixth consecutive pass.** 🟢 **Half-superseded `2026-10-31`
  (`p570`): the *regression* half is now supplied** by the `topic:rubric` layer in
  [`../repos/foundations.md`](../repos/foundations.md) — seven granted assets,
  including the first that scores an **agent trajectory** (`AdaRubrics`,
  Apache-2.0, 368★). 🔴 **The *observability* half stands, seventh consecutive
  pass:** nothing education-specific detects a deployed tutor drifting. Read the
  original sentence below as true of its date and half-true now. Two differently shaped queries returned
  nothing new: a text search for evaluation/benchmark assets under
  `topic:education` returned **0 results**, and the ITS/learning-analytics sweeps
  surfaced no monitor. **But the gap is now one notch less absolute**, and the
  asset that narrows it is not an AI tool:
  [`terracotta-education/terracotta`](https://github.com/terracotta-education/terracotta)
  (**Apache-2.0**, 21★, Java) is an **LTI-attached randomised-controlled-trial
  platform** for education research — random assignment, treatment variation
  inside real assignments, consent hidden from the teacher, non-consenting
  participants filtered from exports, identifiers stripped. That is **efficacy
  measurement**, not drift detection: it answers "did this intervention work",
  which no other asset in this KB does, and it still does not answer "has the
  tutor in production degraded since Tuesday". Both are needed; one now exists.
- **The regional-supply finding sharpened into something uncomfortable.** Across
  five passes, the education agents this KB has managed to place in a region are
  **systematically the licence-defective ones** — `dio-agent` (LATAM, 2,750★, no
  licence), `guru-latihan-dinamis` (Indonesia, 115★, no licence),
  `mcp-canvas-lms` (North America, 104★, no licence file). The regionally
  *placeable* and the legally *usable* sets barely intersect, and the reason is
  structural: regional provenance is easiest to read off hackathon and community
  projects, which are the least likely to have had a licence conversation. **For
  a client this means the local-supply story and the build-on-it story are
  usually about different repositories**, and conflating them is the most
  expensive mistake available on this page.
