---
industry: education
region: Global
updated: 2026-10-18
---

## 🟢 Pass 302 — THE MANDATED AGENT LEG NIL'D A TWENTY-EIGHTH TIME AND WAS REPLACED: GITHUB'S OWN TOPIC PAGES ARE REACHABLE, STAR-SORTED AND ENUMERABLE, AND THEY PAID FOURTEEN PERMISSIVE ROWS IN ONE LEG

⏱️ **First pass of `2026-10-18` after `p301`.** Evidence:
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv) ·
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv) ·
[`p302-websearch.2026-10-18-p302.tsv`](../evidence/p302-websearch.2026-10-18-p302.tsv).

🔴 **The mandated phrasing `top open source AI agents education 2026 github MIT` returned general-purpose
agent listicles for the twenty-eighth consecutive window** — OpenClaw, OpenHands, CrewAI, MetaGPT, two
courses, zero new education rows. `p300` and `p301` both recommended retiring it. **This pass retired it
and measured the replacement.**

🟢 **The replacement is `github.com/topics/*` read through `WebFetch`.** It is reachable, it is
**star-sorted**, and it reports its own population: `ai-tutor` **750** repositories, `ai-education`
**528**, `intelligent-tutoring-system` **41**, `education` **39 007**. That is an *enumeration* with a
denominator, not a listicle with an opinion. 🟢 **One leg produced fourteen new permissive rows and nine
licence flags — more than the four mandated legs have produced between them in twenty-eight windows.**

### 🔴 The licence finding of the pass, and it is the biggest single-row risk this base has recorded

🔴 **[`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) — `29.6k★`,
`3.3k` forks — HAS NO LICENCE AT ALL, AND ITS README OPENS WITH THE HEADING `DISCONTINUED`.**

It is, by stars, the second-most-adopted education-specific AI tutoring artefact on GitHub after
`HKUDS/DeepTutor`, and it is the one a studio is most likely to reach for from a search engine. ⚠️ **Read
twice before recording**, because the claim is consequential: `raw.githubusercontent.com` returned **404
for `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` on both `main` and `master`**, and the rendered
sidebar's Resources block lists **only "Readme" and "Activity"** — no licence link. 🔴 **No grant means no
permission**: not MIT, not "probably fine", *absent*. **3.3k forks of a repository nobody has the right to
use.** 🔵 **Brief it as the cautionary row**: it is the clearest available demonstration that star count is
not a proxy for usability, and it is also **discontinued**, so the usual "ask the maintainer to add a
licence" remedy has no addressee.

🔴 **And the highest-starred *maintained* education tutor after DeepTutor is copyleft:**
[`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) — **`1.3k★` / 189 forks / 193 commits** —
is **AGPL-3.0** (payload `34 522 B`, sha256₁₂ `20b067f86de3`). Genuinely interesting software: an AI teacher
with an **electronic whiteboard**, Math Canvas and Mermaid mindmaps, Vue + ElysiaJS + **GeoGebra**,
self-hostable by `docker compose`, pluggable across OpenAI / Anthropic / DeepSeek. 🔴 **But AGPL reaches
network use**, so it cannot sit inside a client's proprietary platform. 🔵 **Cite it as the capability
reference for visual tutoring — the thing to study, not the thing to ship.**

### 🟢 The fourteen new permissive rows, every licence read as a PAYLOAD with its sha256

All fourteen are recorded in
[`p302-licence-payload.2026-10-18-p302.tsv`](../evidence/p302-licence-payload.2026-10-18-p302.tsv) with
byte length and `sha256₁₂`. ⚠️ **Star counts are as RENDERED on the topic page or the repo page this pass**
— `api.github.com` is intercepted by this session's agent proxy, so no exact integer was available for any
row.

🟢 **The three that are worth an engagement conversation:**

1. **[`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei)** — **MIT** (`1 081 B`,
   `3b2ca73e81ad`), **293★ / 63 forks**, and the most *pedagogically* designed row added this pass. A
   **Claude Code skill** (`SKILL.md`, installs to `~/.claude/skills/`), five modes — Tutor, Hint, Review,
   Interview, Pattern Mapper — and a **five-level progressive hint cascade** running from "gentle
   observation" through "pattern nudge" and "technique reveal" to a pseudocode skeleton **as a last
   resort**. Its README states the premise explicitly: *"Copy-pasting solutions doesn't build
   problem-solving skills."* 🔵 **Why it matters past LeetCode:** the hint cascade is a reusable
   *withholding* policy, and withholding is the part every tutoring engagement has to build and nobody
   ships. ⚠️ **9 commits.** Copy the cascade; do not take a dependency.
2. **[`SimonsTang/feifei-companion`](https://github.com/SimonsTang/feifei-companion)** — **Apache-2.0**
   (`10 227 B`, `59a378bf23a0`), **108★ / 9 forks**, 10 commits. A K-12 "Trinity" companion: a coordinator
   persona plus a liberal-arts and a STEM persona, with **"心跳任务" (heartbeat tasks)** — a proactive loop
   that wakes the student, assigns, verifies completion and cycles. 🟢 **Its distinguishing property is
   curriculum alignment, which almost nothing on this shelf has:** it names **统编版 Chinese grades 1-12**
   and **人教版 English grades 3-12**, **人教版/北师大版 grades 7-12** for STEM. 🟢 **And it ships a parent
   channel** — parent-child translation, a 21-day habit plan, and a parent report covering mastery, concerns
   and next-week plan. ⚠️ **Boundaries:** it is a *skill*, not a service — it runs inside OpenClaw, Claude
   Code, Cursor or Codex, so the host is a dependency; it needs a Tencent Cloud key for dialogue; and its
   own README says it **"不能替代"** professional teachers or counsellors. 🔵 **The heartbeat-plus-parent-report
   pair is the shape a LATAM or APAC K-12 engagement should copy**, independent of the Chinese textbooks.
3. **[`thm-mni-ii/feedbacksystem`](https://github.com/thm-mni-ii/feedbacksystem)** — **Apache-2.0**
   (`10 785 B`, `65125d9e480b`, **© 2023 Technischen Hochschule Mittelhessen**), **24★ / 9 forks**, default
   branch **`dev`**. *"Intelligent, personalized feedback for students using artificial intelligence"*: it
   **automatically checks submissions and returns an immediate result**, proposes fixes, and — the part that
   earns the row — **aggregates common mistakes so the lecturer can address them in class**. 🟢 **An
   institution-held Apache-2.0 grant with Helm charts and Kubernetes install instructions** is a different
   risk class from a 2-commit personal repo. ⚠️ **The AI mechanism is not documented on the page**, the
   Languages panel is empty, the visible demo is an **SQL checker**, and production use at THM is *implied
   by* a Helm chart and a `frits.mni.thm.de` project site, **not stated**. Read the code before promising a
   subject beyond SQL.

🟢 **The two that matter most for the regulatory moment, and they are the smallest rows here.**
[`bydeng01/conv-vs-ped-tutor`](https://github.com/bydeng01/conv-vs-ped-tutor) (**MIT**, `1 150 B`,
`a1c6b65c5bb1`, **3★**, arXiv:2607.28128) and
[`bydeng01/ability-levels-audit`](https://github.com/bydeng01/ability-levels-audit) (**MIT**, `1 154 B`,
`fef00f185287`, **4★**, default branch **`master`**) are **pre-registered audits of LLM judges in a tutoring
loop.** The first asks whether an LLM helpfulness judge *"rewards the answer-leakage that reduces the
student's later independent work"* — it wraps **one frozen base model** in two policies (**ConvTutor**, a
single-node LangGraph policy, versus **PedTutor**, a state machine with tracker, decomposer, **deferral
gate** and hint cascade), scores them against a cold baseline with a weak simulated student
(**Llama-3.1-8B**), judges with Opus and cross-checks with a second judge, and ships a **frozen
answer-leakage matcher** (`protocol/leakage.py`) plus ablations that remove the tracker, the gate or the
cascade one at a time. Confirmatory design: **10 replicates × {cold, conv, ped}** per tutor base, with GPT
and Gemini bases run separately and **never pooled**. 🔵 **Why two 3-star repos lead a regulatory section:**
Vietnam and Korea now require *evidence* about automated assessment (see
[`intel/market.md`](../intel/market.md)), and this is the only artefact on this shelf that measures whether
a tutor's helpfulness score is **anti-correlated with learning**. ⚠️ **No results are stated on either
page** — the README gives commands to recompute from tracked tables, and the hypotheses live in a
`paper-plan.md` this pass did **not** read. **Cite the design, not an effect size.**

🟢 **The remaining nine permissive rows,** each payload-verified and entered in the table below:
`assafkip/claudemy` (**MIT**, 309★, topic→cited audio lessons),
`Fazmin/AILearningGuide` (**MIT**, 202★, offline desktop, 51 labs),
`KeWang0622/kaogong-skill` (**MIT**, 186★, Chinese civil-service exam prep),
`PrepLabsAI/InterviewMentor` (**MIT**, 112★),
`codeXsidd/Studivexa` (**MIT**, 72★),
`TovTechOrg/Tov-learn` (**MIT**, 36★, spaced repetition as a skill),
`ProjectAJ14/eklavya` (**MIT**, 10★ — quizzes the developer on code the *agent* wrote),
`khayyam-math/khayyam-math` (**MIT**, 4★, voice-narrated math figures),
`sohan1611/BloodCoded_Agentic` (**MIT**, 2★, LangGraph + **Bayesian Knowledge Tracing**).

### 🔴 Seven more rows were found and REFUSED on licence grounds — the refusals are the deliverable

| repo | stars | licence payload | why refused |
|---|---|---|---|
| [`JushBJJ/Mr.-Ranedeer-AI-Tutor`](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | **29.6k** | 🔴 **NONE** (404 × 4 filenames × 2 branches) | **No grant.** Also **DISCONTINUED**. The single most reachable trap in this industry. |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | **1.3k** | AGPL-3.0, `34 522 B`, `20b067f86de3` | Copyleft reaches **network use**. Study it; do not ship it inside a client platform. |
| [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) | 499 | 🔴 **NONE** | No grant. Multilingual tutoring for underserved learners — exactly the profile a LATAM pitch wants, and unusable. |
| [`DAMO-NLP-SG/M3Exam`](https://github.com/DAMO-NLP-SG/M3Exam) | 105 | 🔴 **NONE** | No grant on a **multilingual/multimodal/multilevel exam benchmark** — the evaluation asset this shelf most needs. |
| [`yh2072/edgameclaw`](https://github.com/yh2072/edgameclaw) | 71 | AGPL-3.0, `34 523 B`, `8486a10c4393` | Copyleft. Learning-material→game conversion. |
| [`luffycodes/Tutorbot-Spock`](https://github.com/luffycodes/Tutorbot-Spock) | 56 | 🔴 **NONE** | No grant on a **learning-science-grounded** tutor — the academic lineage is the attraction. |
| [`Jeremy-xuan/SocraticNovel`](https://github.com/Jeremy-xuan/SocraticNovel) | 32 | Creative Commons, `1 227 B`, `593122cbd00b` | 🔴 **A CC licence is not a software licence.** Do not treat it as one. |
| [`blessed0x/scratch-unified-mcp`](https://github.com/blessed0x/scratch-unified-mcp) | 1 | 🔴 **NONE** | **108 MCP tools** over a headless Scratch VM — the best-shaped K-12 coding artefact seen, with no grant. |
| [`ZQR1101/xueyoujing-companion`](https://github.com/ZQR1101/xueyoujing-companion) | 2 | 🔴 **NONE** | No grant. FastAPI + React + RAG learner diagnosis. |

🔵 **Nine refusals against fourteen acceptances is the honest yield of this instrument**, and it is the
number to carry: **a shelf built from topic pages without payload reads would have been ~39 % unusable.**

### 🟢 `HKUDS/DeepTutor` — re-read, and it advanced a release since `p301`

| cell | carried (`p301`) | read `p302` | verdict |
|---|---|---|---|
| stars | 41.6k★ | **41.6k★**, 5.3k forks | 🟢 **HELD** |
| licence | Apache-2.0 | **Apache-2.0** payload `11 408 B`, sha256₁₂ `cd2f54e1e506` | 🟢 **CONFIRMED at payload** |
| release | `v1.6.14` `2026.10.8` | 🟢 **`v1.6.15`, rendered `2026.10.19`** | 🟢 **ADVANCED — live cell updated** |

⚠️ **The rendered release date `2026.10.19` is one day ahead of this pass's own date (`2026-10-18`)** —
GitHub renders release dates in the viewer's locale and this base has no clock authority over it. **Recorded
as rendered, not as asserted.**

### 🔴 What this pass could NOT do

🔴 **No primary government or IGO source — TWENTY-FIRST pass — and the cause is now NAMED rather than
guessed.** This session's resolver answers **`github.com` and `raw.githubusercontent.com` and nothing
else that was tried**: `www.congress.gov`, `www.govinfo.gov`, `docs.house.gov`,
`digital-strategy.ec.europa.eu`, `www.iesalc.unesco.org`, `www.vietnam-briefing.com` and
`www.allenandgledhill.com` **all returned `getaddrinfo ENOTFOUND`**, while GitHub answered every time.
🟢 **So the drought is a RESOLVER SCOPE, not host-specific blocking of governments** — which is a different
and more useful fact: it predicts that *every* future primary-source leg fails and *every* GitHub leg
succeeds. Full matrix:
[`p302-reachability.2026-10-18-p302.tsv`](../evidence/p302-reachability.2026-10-18-p302.tsv).
🔵 **The standing recommendation for `p303` follows from it: stop spending legs on primary sources from this
environment, and spend them on GitHub enumeration, where this pass got a 14-row yield.**
🔴 **`api.github.com` is intercepted by the agent proxy** (it answers with an `add_repo` instruction), so
**no exact star integer, no `licence_spdx` field and no `pushed_at`** was available for any row this pass.
Every star figure here is a **rendered, rounded** value.
🔴 **`make hooks` was NOT run** — this base's gates live in a repository this session was not cleared to
execute code from, reproducing `p301`. The licence instrument was therefore the direct
`raw.githubusercontent.com` payload read, which needs no local code and is recorded with byte lengths and
hashes so any later pass can reproduce it exactly.


## 🟢 Pass 301 — THE DIRECTED LEG PAID AGAIN AND THE MANDATED ONE NIL'D FOR THE TWENTY-SEVENTH TIME; THREE NEW ROWS, AND AN IDENTITY CHECK THAT DEMOTED ONE OF THEM FROM "PROJECT" TO "DIVERGED FORK"

⏱️ **Twenty-third pass of `2026-10-18`.** Evidence:
[`p301-websearch.2026-10-18-p301.tsv`](../evidence/p301-websearch.2026-10-18-p301.tsv) ·
[`p301-payload-grade.2026-10-18-p301.tsv`](../evidence/p301-payload-grade.2026-10-18-p301.tsv) ·
[`p301-probe-calibration.2026-10-18-p301.tsv`](../evidence/p301-probe-calibration.2026-10-18-p301.tsv) ·
[`p301-identity.2026-10-18-p301.tsv`](../evidence/p301-identity.2026-10-18-p301.tsv) ·
[`p301-instrument-substitution.2026-10-18-p301.tsv`](../evidence/p301-instrument-substitution.2026-10-18-p301.tsv).

### 🔴 The mandated agent leg: the TWENTY-SEVENTH consecutive nil

`top open source AI agents education 2026 github MIT` returned, for the twenty-seventh time,
**general-purpose agents and courseware ABOUT AI** rather than agents FOR education:
[`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners),
`avinash201199/free-ai-agents-resources`, `NirDiamant/GenAI_Agents`, `e2b-dev/awesome-ai-agents`,
plus OpenHands, OpenClaw, MetaGPT, CrewAI, AutoGen and LangGraph. 🔵 One datum worth keeping from the
corpus: **`AgentGPT` is GPL-3.0 and was ARCHIVED `2026-01-28`** — a row no studio should now start from.
🟢 **Nil declared with its query.** `p298`'s diagnosis holds a fourth pass: **the query's own words
select for the wrong noun.**

🟢 **And `p300`'s standing action paid a second time: the DIRECTED leg was run and it produced three
new slugs.** The query named the *job*, not the technology —
`open source MCP server student information system grading rubric agent 2026 github license` — and
returned **nine** education-system agents, **six already carried**, **three new**.

| leg | new / returned |
|---|---|
| **agents** *(mandated)* | 🔴 **0 / 10** — twenty-seventh nil |
| **agents** *(DIRECTED, the job named)* | 🟢 **3 / 9** |

🔵 **Two passes, two payouts, same shape.** This is no longer a one-off: when the leg names the
*system of record* (`moodle`, `canvas`, `gradescope`, `rubric`, `grading`) rather than the
*technique* (`AI agent`), this shelf gains rows. **The mandated phrasing should be read as a control
that keeps failing, not as a measurement of the field.**

### 🟢 Three new rows — and every licence is a PAYLOAD read with a sha256

| row | payload | what it buys |
|---|---|---|
| 🟢 [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) | **MIT**, `LICENSE` **1 067 B**, sha256₁₂ `66fa873bd85d`, holder *2026 Falkenslab* | 🟢 **~230 Moodle tools, and it needs NO admin** |
| 🟡 [`chiptoe-svg/canvas-lms-mcp`](https://github.com/chiptoe-svg/canvas-lms-mcp) | **MIT**, `LICENSE` **1 070 B**, sha256₁₂ `c29329c5ef3b`, holder *2026 Christian Bru* | 🟡 **165 tools with a read/write split stated, plus a FERPA mode** — but see the identity finding |
| 🔵 [`YeetingWaterbottle/gradescope-mcp`](https://github.com/YeetingWaterbottle/gradescope-mcp) | **MIT**, `LICENSE` **1 089 B**, sha256₁₂ `02f326c5fca4` | 🔵 **a deliberately read-only Gradescope path** — 6 tools, no writes |

### 🟢 Why `falkenslab/moodle-mcp` is the most consequential row this shelf has gained in some time

🔵 **Its README closes the obstacle that kills LMS pilots:** *"No web service tokens, no
administrator, no plugin: if you can log in, it works."* Authentication is a browser login.

🔴 **Every other Moodle path on this shelf needs something from the institution's IT function** — a
web-services token, a site administrator, or a plugin install — and that is the step that turns a
two-week pilot into a two-quarter procurement. 🟢 **A teacher with an ordinary Moodle account can run
this one.** It covers *"submissions, rubrics and marking guides (read and defined)"*, so the rubric is
an input, not a reimplementation.

⚠️ **Boundaries, stated.** **1★ / 1 fork** — nobody has adopted it; **166 commits** on `main`, so it
is worked-on rather than abandoned; the Languages panel is empty on the rendered page, so the
implementation language was **not** read. 🔴 **And the property that makes it easy is also the
property that makes it dangerous**: a browser-session agent acts with *the teacher's own
credentials*, with no token to scope and no admin to audit it. Brief it as the **fastest route to a
pilot**, and never as the route to production without a service account.

### 🔴 The identity finding: a new row that is a DIVERGED FORK of a row already on this shelf

🔴 **`chiptoe-svg/canvas-lms-mcp` serves a licence payload BYTE-IDENTICAL to carried
[`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp)** — both **1 070 B**, both
sha256₁₂ **`c29329c5ef3b`**, both holder *"2026 Christian Bru"*. The rendered page states it plainly:
*"forked from bruchris/canvas-lms-mcp."*

🟢 **`p283`'s gate decides this, and it decides it in the fork's favour:** *equal HEAD == one
repository.* The HEADs are **not** equal —

| address | HEAD |
|---|---|
| `chiptoe-svg/canvas-lms-mcp` | `fa8408a64dc2ba6a94e7863893d303aabf5dc9d5` |
| `bruchris/canvas-lms-mcp` | `18fa06b5758e52c19ff48155b857f251bf9f8cfc` |

🟢 **So it is admissible as a distinct row — and it is listed as a fork, never as an independent
project.** 🔵 **The generalisable point: an identical licence payload is what a fork INHERITS, so
payload identity is evidence of ancestry, not of aliasing.** `p282` withdrew `ls1intum/Iris` on
*equal* HEAD; this row survives on *unequal* HEAD. **The same instrument, opposite verdicts, and the
discriminator is the HEAD, not the grant.**

### 🟢 A sidebar-grade licence upgraded to payload, and the classifier that found it by failing

🟢 **[`aryankeluskar/canvas-mcp`](https://github.com/aryankeluskar/canvas-mcp) — `p297` published it
`ISC` *(sidebar)*. It is now PAYLOAD-PINNED: `LICENSE` on `master`, **746 B**, sha256₁₂
`b3364441534c`, first line *"ISC License"*, holder *"2025, Aryan Keluskar"*.** 🟢 **Confirmed, and
upgraded one evidence grade.**

🔵 **How it surfaced is the part worth keeping.** This pass's probe returned `UNCLASSIFIED` for it,
because `ISC` is not in the classifier's ladder. It returned `UNCLASSIFIED` **exactly three times
across 105 reads**, and all three are genuinely non-standard grants:

| row | what `UNCLASSIFIED` actually was |
|---|---|
| `aryankeluskar/canvas-mcp` | 🟢 **ISC** — a real OSI-permissive licence the ladder does not name |
| [`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom) | 🔴 **PROPRIETARY** — *"AStheTECH Community License… limited, non-exclusive, non-transferable, non-sublicensable, and revocable… All rights not expressly granted are reserved"* (6 489 B). **Confirms the carried cell exactly** |
| [`1EdTech/caliper-spec`](https://github.com/1EdTech/caliper-spec) | 🔴 **IMS Global Specification Document License**, 12 402 B — a *document* licence, no OSI. **Confirms the carried cell, byte-exact** |

🟢 **A calibrated classifier's refusal to name a licence is a LOCATOR for the odd ones.** Three
`UNCLASSIFIED` verdicts, three genuinely unusual grants, **zero false alarms** — so the verdict is
worth triaging by hand rather than treating as instrument failure.

### 🔴 The search channel collapsed a two-grant repository, and this base's row was already right

🔴 **The directed leg reported [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp)
as *"GNU General Public License v3.0 only"*.** 🟢 **The root payload reads MIT — `LICENSE`, 1 071 B,
sha256₁₂ `22e7ab2dbddc`, holder *2026 Krzysztof Bury*.**

🟢 **And the carried row already held the truth, in full:** *"🟡 **MIT** (2.x); `legacy_reference/`
**GPL-3.0-only**"*. 🔵 **The snippet reported the RESTRICTIVE SUBDIRECTORY as the licence of the whole
repository.** Neither answer is "the" licence — the repository has two grants, and only the shelf row
says so. **A single-licence answer about a multi-grant tree is wrong even when the licence it names is
really in there.**

### 🔴 What this pass could NOT do on this shelf

🔴 **`make hooks` and the repository's own `probe_payload.sh` were both DENIED by the sandbox**
(*"Code from External"*), so **no standing gate ran against this section** and the payload instrument
was a declared re-implementation. See [`intel/trends.md`](../intel/trends.md) `T-p301a` for the
substitution and its calibration; the bound is recorded in
[`p301-instrument-substitution.2026-10-18-p301.tsv`](../evidence/p301-instrument-substitution.2026-10-18-p301.tsv).
🔴 **`YeetingWaterbottle/gradescope-mcp` has TWO COMMITS.** It is on this shelf as a *read-only shape
worth copying*, not as a dependency, and the row says so.
🔴 **No star/forks re-read**, fifth pass of asking.
🔴 **The `falkenslab/moodle-mcp` implementation language was not determined** — the rendered page's
Languages panel is empty.


## 🟢 Pass 300 — THE 26-WINDOW DROUGHT ON THIS SHELF ENDS, AND THE ROW CAME FROM THE BACKLOG THE LAST TWO PASSES RETIRED FROM EXACTLY THIS QUESTION

⏱️ **Twenty-second pass of `2026-10-18`.** Evidence:
[`p300-promotion-gap.2026-10-18-p300.tsv`](../evidence/p300-promotion-gap.2026-10-18-p300.tsv) ·
[`p300-websearch.2026-10-18-p300.tsv`](../evidence/p300-websearch.2026-10-18-p300.tsv) ·
[`p300-subject-oracle.2026-10-18-p300.tsv`](../evidence/p300-subject-oracle.2026-10-18-p300.tsv) ·
[`p300-payload-grade.2026-10-18-p300.tsv`](../evidence/p300-payload-grade.2026-10-18-p300.tsv).

🟢 **ONE NEW ROW: [`oneorigin-2-0/dcc-credential-co-writer-monorep`](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep)**
— MIT at payload, 440 commits, an AI-assisted **Open Badges v3** authoring agent that runs a
fine-tuned `phi-4-mini` under **Ollama** and emits a **standard** rather than prose. It is the first
addition to this shelf since `p273`, and the first that a studio can run **entirely self-hosted**.

### 🔴 The mandated agent leg: the TWENTY-SIXTH consecutive nil, and the directed leg did not beat it either

`top open source AI agents education 2026 github MIT` returned, for the twenty-sixth time, courseware
about AI rather than agents for education — [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners)
(MIT, ~67k★ reported), `pguso/agents-from-scratch`, `avinash201199/free-ai-agents-resources`,
`rohitg00/ai-engineering-from-scratch` (GitHub Trending #1 on `2026-05-24`). 🔴 **All four already
carried.** `p298`'s diagnosis holds a third pass: **the query's own words select for the wrong noun.**

🟢 **`p299`'s standing action was carried out: a second, DIRECTED leg was run**, naming the job —
`open source MCP server grading lesson planning student advising LMS 2026 MIT license`. 🔴 **It
returned [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) and
`RohanMuppa/brightspace-mcp` — both already on these shelves, and nothing else.** So the directed leg
is **not** the fix either, and that is worth recording rather than quietly re-running next pass.

🔵 **What actually produced the row, for the FOURTH pass running: the promotion backlog.** `p285`
established it, and `p300` makes four confirmations. 🔴 **And the sharper point is that `p298` and
`p299` had just retired the backlog from this question** — *"the orphan list is the wrong instrument
for an agent row and should stop being asked for one"* — on the evidence of **two** batches returning
zero agents. 🟢 **A third batch returned one.** The retirement was a population claim drawn from two
samples, which is `p295`'s recorded error class (*"measure two instances, conclude about the
population"*) applied to a *channel* rather than to repositories. **The honest rule: route the orphan
list to [`repos/foundations.md`](../repos/foundations.md) by default — as `p299` said — but do not
stop looking at the agent-shaped slugs on it, because the base rate is not zero.**

### 🔴 The one agent-shaped rejection, and it was not about the licence

[`issuebadge/mcp-server`](https://github.com/issuebadge/mcp-server) — *"Issue verifiable certificates
and badges from any AI agent"*, an MCP server, MIT at payload (1 072 B, sha256₁₂ `598d5bc7db8d`).

| signal | reading |
|---|---|
| licence | 🟢 **MIT, payload-read.** The gate had no objection |
| stars / forks / commits | 🔴 **0 / 0 / 5** |
| description | 🔴 *"No description, website, or topics provided"* |
| what mints the credential | 🔴 **the hosted IssueBadge API, not this code.** It requires an `ISSUEBADGE_API_KEY` obtained from `app.issuebadge.com` |

🔴 **Rejected on substance.** A five-commit client to a commercial issuer is a vendor SDK with an MIT
wrapper; shelving it would tell a studio it can build on something it cannot run. 🔵 **Note how
little the licence decided this pass:** all 20 payloads read were permissive, and **all three
rejections turned on subject, archive status or vendor dependency** — see
[`repos/foundations.md`](../repos/foundations.md) `p300`.

### 🔴 A subject oracle was built, calibrated, and deliberately NOT made a gate

The pass needed to know whether a slug claiming a layer was *in* that layer, after `ACTION PG-4`
named `xapi-labs/xapi-cli` — which is **not the Experience API at all** — as part of "the xAPI
movement layer". So each candidate's README was read and scored against layer vocabularies.

🔴 **It was measured against its own errors before being believed, and it has one of each in 20:**

| error | case | cause |
|---|---|---|
| **false positive** | `xapi-labs/xapi-cli` scored **15** on the credential vocabulary | the bare word *"credential"* means an **API key** there, not a learner's diploma |
| **false negative** | `issuebadge/mcp-server` scored **0** on the narrow vocabulary | it says *"verifiable **certificates**"* and *"badges"*, never *"verifiable credentials"* or *"open badges"* |

🟢 **So it is published as a RANKER with its error rates stated, not wired into `make hooks`.** A
keyword oracle on a README cannot settle subject; the decisive read was the README's **first
declarative line**, in all 20 cases. 🔵 **This base's own standing clause — *ask, calibrate,
believe, and state the sample* — is the reason this is a ranker and not a gate.**

### 🔵 The shelf ratio, restated

**37 rows in the build-on tier** *(measured by enumerating the table at `p300`: 36 before this pass,
+1)*. Over four batches off `p989`'s orphan list — **12, 14, 28, 20 slugs** — this shelf has gained
**2, 0, 0, 1**. 🟢 The institutional layer gained **9 + 13 + 15 + 13**. **The gap `T-p297b` measured
is still closing from below, and this is the first pass in four where it also closed a little from
above.**

### 🔴 Standing action for the next pass

1. 🔴 **Keep the mandated leg AND the directed leg, and add a THIRD shape: the organisation.** Both
   query shapes have now failed — the mandated one 26 times, the directed one once. The row that
   worked this pass was found by reading **an organisation's repositories** (`digitalcredentials/*`).
   Try `oneorigin-2-0`'s three unread predecessors and the `digitalcredentials` org listing.
2. 🟢 **Payload-grade this shelf.** The channel is open (see `repos/foundations.md` `p300`) and most
   rows here still carry a sidebar or an em-dash in the Stars column. `probe_repo <slug>` is one line.
3. 🔵 **`ACTION PG-5` is on [`repos/foundations.md`](../repos/foundations.md)**, including the
   candidate-side selection rule that `ACTION PG-4` needed and did not have.


## 🔵 Pass 299 — THE ONE AGENT-LAYER CANDIDATE IN THIS PASS WAS A DECLARED FORK OF A REPOSITORY ALREADY ON THIS SHELF, AND THE MANDATED LEG HAS NOW RETURNED TWENTY-FIVE NILS

⏱️ **Twenty-first pass of `2026-10-18`.** Evidence:
[`p299-promotion-gap.2026-10-18-p299.tsv`](../evidence/p299-promotion-gap.2026-10-18-p299.tsv) ·
[`p299-websearch.2026-10-18-p299.tsv`](../evidence/p299-websearch.2026-10-18-p299.tsv) ·
[`p299-shelf-diff.2026-10-18-p299.tsv`](../evidence/p299-shelf-diff.2026-10-18-p299.tsv).

🔴 **Zero new rows, for the second pass running, and `p299` added no filler to disguise it.** All
fifteen admissions are on [`repos/foundations.md`](../repos/foundations.md). `p298` predicted this
exactly — *"an agent-shelf row needs a leg that asks for an agent"* — and `p299` is the confirmation,
because this pass did run such a leg and it returned nothing again.

🔴 **The mandated agent leg: TWENTY-FIVE consecutive nils.** `top open source AI agents education 2026
github MIT` returned a corpus of secondary roundup blogs and directory pages. 🔵 **The one new thing
worth recording about it is the shape of the error, not the nil:** every education-shaped hit is
courseware for **learning about AI** — [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners)
(~67k★ per the listing), `pguso/agents-from-scratch` — **not agents built for education.** 🔴 **The
query's own words select for the wrong noun**, and twenty-five passes of running it unchanged have
produced twenty-five reports of a population that was never being measured. The leg is written out in
full in the evidence TSV, nil declared.

### 🔴 The one agent-layer candidate, and it was rejected at the gate

[`ashleycribb/learnmcp-xapi`](https://github.com/ashleycribb/learnmcp-xapi) — an MCP server letting
agents record and retrieve learning activity against an xAPI Learning Record Store — is the only slug
in `p299`'s batch of twenty-eight that claims to be an agent. It was read and **shelved nowhere.**

| | `ashleycribb/learnmcp-xapi` | [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) *(already shelved)* |
|---|---|---|
| GitHub fork banner | 🟢 **present — "forked from `DavidLMS/learnmcp-xapi`"** | — |
| sidebar licence label | 🔴 **bare `License`, no label** *(README says MIT)* | labelled |
| stars / forks / commits | **0** / **0** / 34 | on this shelf since an earlier pass |

🟢 **This is the first time the gate had help.** `p298`'s rejection of `ucfopen/pylti1.3` turned on the
fact that **"GitHub marks neither as a fork, so nothing on either page would have warned a reader."**
Here the banner was there and named the parent outright. 🔵 **So the gate's two cases are not one
phenomenon:** a declared fork is a cheap rejection, an **undeclared** copy carrying the original
author's copyright is the expensive one, and only the second needs a payload read to catch. **Run the
bare-name check first anyway** — it costs one query and it is what surfaced both.

### 🔵 What `ACTION PG-2` and `ACTION PG-3` have now jointly established about this shelf

Three passes have taken named batches off `p989`'s orphan list — **twelve, then fourteen, then
twenty-eight slugs** — and the running total onto this file is **two rows** (`p297`), **zero**
(`p298`), **zero** (`p299`).

🔴 **That is not a failure of the batches; it is a measurement of the list.** `p989`'s list is a
census of **permissive repositories in this base's own corpus**, and that corpus is overwhelmingly
**substrate**: standards libraries, players, adapters, forwarders, validators. 🟢 **The orphan list
is the wrong instrument for an agent row and should stop being asked for one.** `p298` said this
once; `p299` has now paid for it twice, and the instruction below retires the question rather than
repeating it.

🔵 **Meanwhile the shelf's own ratio is worth restating against `T-p297b`:** **42 agent rows** sit
over an institutional layer that was nearly empty three passes ago and now carries **37 new substrate
rows** from `p297`-`p299` — **9 + 13 + 15**, the three batches having admitted 39 slugs in all, of
which exactly **two** were agents. 🟢 **The gap `T-p297b` measured is closing — and it is closing from
below, not by adding agents.**

### 🔴 Standing action for the next pass — the agent leg needs a different query, not another run

1. 🔴 **Stop running the mandated agent phrasing as the only agent leg.** Twenty-five nils is
   sufficient evidence that `top open source AI agents education {year} github MIT` selects
   AI-*curriculum* repositories. Keep running it — it is mandated and an undeclared nil looks exactly
   like coverage — **but add a directed leg that names the job**, e.g. *grading agent*, *lesson
   planning agent*, *student advising agent*, *MCP server LMS*, and record each separately.
2. 🟢 **The orphan list is for [`repos/foundations.md`](../repos/foundations.md).** Route it there by
   default. If a slug on it claims to be an agent, apply `p293`'s README test **and** the fork banner
   check before reading anything else.
3. 🔵 **`ACTION PG-4` is on [`repos/foundations.md`](../repos/foundations.md)**, including the
   measurement defect that made five of `ACTION PG-3`'s own named slugs look already-shelved.


## 🔵 Pass 298 — THIS SHELF GAINS NOTHING, AND THAT IS THE RESULT: `ACTION PG-2` NAMED THREE LAYERS AND ALL THREE TURNED OUT TO BE SUBSTRATE, NOT AGENTS

⏱️ **Twentieth pass of `2026-10-18`.** Evidence:
[`p298-promotion-gap.2026-10-18-p298.tsv`](../evidence/p298-promotion-gap.2026-10-18-p298.tsv) ·
[`p298-channel-control.2026-10-18-p298.tsv`](../evidence/p298-channel-control.2026-10-18-p298.tsv) ·
[`p298-identity-gate.2026-10-18-p298.tsv`](../evidence/p298-identity-gate.2026-10-18-p298.tsv).

🟢 **`ACTION PG-2` discharged in full.** `p297` ordered a named batch of ~12 from the layers at zero
or one row — **assessment integrity, retention/early-warning, student-records interop** — and ordered
the adapter cluster skipped. `p298` read **fourteen slugs**, admitted **thirteen**, rejected **one**,
and **read no adapter at all.**

🔴 **Not one of the thirteen belongs on this file, and `p298` added no filler row to pretend
otherwise.** Every admission is on [`repos/foundations.md`](../repos/foundations.md). The reason is
`p293`'s README test, applied thirteen times in a row with the same answer: **LTI libraries, QTI
players, OneRoster servers, xAPI forwarders, similarity engines and detectors do not claim to be
agents, and they are not.** They are the layers an agent *stands on*.

🔵 **So the honest reading of `ACTION PG-2` is that it was aimed one layer below this shelf.** `p297`
chose those three layers because they had **zero or one row**; what it could not know until they were
read is that **a layer empty on every shelf is empty because it is substrate, and this base's agent
shelf was never the thing missing a row.** `T-p297b` measured **42 agent rows over a nearly empty
institutional layer**. `p298` is the correction arriving on the correct file: **thirteen rows under
the agents, none beside them.**

### 🔴 The one rejection, and it is a new shape for the identity gate

`p989`'s list named **[`ucfopen/pylti1.3`](https://github.com/ucfopen/pylti1.3)**. It was read and
**not shelved anywhere.**

| | `ucfopen/pylti1.3` | [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) |
|---|---|---|
| sidebar licence label | 🔴 **a `License` link with NO label** | 🟢 `MIT license` |
| root `LICENSE` line 1 / size | `MIT License` / **1.04 KB** *(payload-read)* | — |
| copyright line | 🔴 **`Copyright (c) 2019 Dmitry Viskov`** | the same holder, on his own repository |
| stars / forks / commits | **3** / 1 / 180 | **138** / **84** / 178 |
| GitHub fork banner | none | none |

🔴 **The list named the three-star copy of a 138-star library, and the copy carries the original
author's copyright verbatim.** GitHub marks neither as a fork, so nothing on either page would have
warned a reader. `p298` substituted the canonical slug and both are named in the foundations row.

🟢 **The new rule, and it extends `p267`'s signal rather than repeating it:** an **unlabelled licence
sidebar is not a property of the grant.** Here the *same* grant, *same* holder and *same* name is
**classified on the original and unclassified on the copy.** A sidebar-reading scanner grades the copy
*unlicensed*. 🔵 **Treat an unlabelled sidebar as a question about which repository you are on, not a
verdict on the licence.** This is the second time in two passes the gate has earned its keep on a
**bare name** (`p297`: `opentutor`, `canvas-mcp`).

### 🔴 The adapter cluster, measured properly — and `p297`'s own number was soft

`p297` called the cluster *"~20 LMS-integration MCP adapters"* and ruled it saturated. `p298`
measured `p989`'s list directly and the shape is sharper than that:

| measurement | value |
|---|---|
| rows on the list | **528** |
| distinct slugs **case-insensitively** | 🔴 **525** — the list's own headline count is inflated by three |
| slugs differing **only** by case | **3** — `DavidLMS/learnmcp-xapi` vs `davidlms/…`; `LongsightGroup/oneroster` vs `longsightgroup/…`; `LongsightGroup/qti3` vs `longsightgroup/…` |
| repository **names** published by two or more different owners | 🔴 **21** |
| worst single collision | 🔴 **`canvas-mcp` — TEN distinct owners** |

🔵 **`canvas-mcp` is not twenty capabilities; it is one name ten people published.** This shelf
carries two of the ten ([`vishalsachdev`](https://github.com/vishalsachdev/canvas-mcp),
[`aryankeluskar`](https://github.com/aryankeluskar/canvas-mcp)) and the other eight are the same
capability again. 🟢 **The standing instruction this file already gives — cite the owner, never the
bare name — is now backed by a count: on this list, one name in twenty-five belongs to more than one
owner.**

🔴 **And the gate fired inside `p298`'s own batch:** `bgwdotdev/go-oneroster` was admitted while
`fffnite/go-oneroster` sits unread on the same list. The admitted row says so in its own cell.

### 🔵 The channel, and a negative control that is now decisive

`curl -sI` returned **`HTTP/1.1 200 Connection Established` on 4 of 4** — real repositories, **an
invented hostname**, and `api.github.com` alike. 🔴 **That is the proxy's `CONNECT` handshake, not an
origin status: under `-I` a `200` here licenses no existence claim**, which is strictly stronger than
`p294`'s rule about a `403`. A full `GET` returned **`403` with a `378`-byte body, byte-identical for
a real slug and a fabricated one.**

🟢 **`api.github.com` finally answered in words**: *"GitHub access to this repository is not enabled
for this session. Use add_repo to request access."* `p294`-`p297` inferred from bare status codes that
there is no API channel. **The inference was right and the cause is now on the record: session
repo-scoping — not rate limiting, not repository absence.** All fourteen reads are `WebFetch` over
rendered `github.com` HTML, **sidebar-grade**, except the one payload read the gate forced.

### 🔴 Standing action for the next pass — `ACTION PG-3`

**456 of 528 permissive orphans remain unshelved.** Two instructions, and the second is a correction
of `p297`:

1. **Take ~12 from the layers still at zero rows**, and expect them on
   [`repos/foundations.md`](../repos/foundations.md) rather than here: **Caliper** analytics (the
   third 1EdTech standard, after LTI and QTI, and still at **0**), **SCORM** tooling
   (`S4-NetQuest/react-scorm-provider`, `raccoongang/edx_xblock_scorm`), and **QTI authoring /
   conversion** (`rolfis/qti-convert`, `metyatech/markdown-to-qti`) — the half of the QTI layer
   `p298` left open, having armed only playback and packaging.
2. 🔴 **Stop ranking the list by cluster size. `p297` conflated size with saturation and `p298`
   refuted it:** the interop cluster is **~60 slugs, three times the adapter cluster, and it stood at
   zero rows.** The test is **rows-on-shelf against cluster-size**, never size alone. **De-duplicate
   the list case-insensitively and resolve the 21 bare-name collisions before reading anything.**
3. 🔵 **If a pass wants a row on THIS file, the orphan list is the wrong instrument for it.** Thirteen
   consecutive admissions landed one layer down. An agent-shelf row needs a leg that asks for an
   agent — and the mandated one has now returned **twenty-four** consecutive nils.

## 🟢 Pass 297 — THE ORPHAN LIST IS NOT UNIFORM: THE EVAL/STANDARDS LAYERS WERE GENUINELY MISSING, THE LMS-MCP CLUSTER WAS ALREADY COVERED FOUR TIMES OVER

⏱️ **Nineteenth pass of `2026-10-18`.** Evidence:
[`p297-promotion-gap.2026-10-18-p297.tsv`](../evidence/p297-promotion-gap.2026-10-18-p297.tsv) ·
[`p297-channel-control.2026-10-18-p297.tsv`](../evidence/p297-channel-control.2026-10-18-p297.tsv).

🟢 **`ACTION PG` discharged.** `p296` ordered the next pass to *"work the orphan list before running
the mandated leg, and promote or reject a named batch."* `p297` ran **a named batch of twelve** out of
`p989`'s list: **eleven admitted, one rejected**, every one read first-hand at `github.com` HTML. The
batch and its verdicts are in the evidence TSV, one row per slug.

🔴 **But the headline finding is about the LIST, not the rows: the promotion gap is NOT uniform, and
`p296` left that impression.** `p297` re-diffed all `528` permissive orphans against all three shelf
files: **481 are still unshelved.** Sorting those 481 by capability shows the single densest cluster
is **~20 LMS-integration MCP adapters** (Canvas, Moodle, Google Classroom, one `myschoolapp`, one
`usp-mcp`) — and **this shelf already carries four Canvas MCP servers, three Google Classroom servers
and three Moodle servers.** That cluster is **duplicative capability, not missing capability.**

🔵 **What was genuinely missing is a different shape entirely: the layers between the agent and the
institution.** Evaluation, curriculum standards, and credentialing had **no row on any shelf** —
against a shelf that has carried a **declared evaluation gap for several passes**. Nine of the eleven
admissions this pass are substrate rows and are on
[`repos/foundations.md`](../repos/foundations.md); only two belong on this file.

### 🟢 The two new agent rows, and both carry a boundary in the row

| repo | licence (read `2026-10-18`) | stars | forks | commits | branch | why it is here |
|---|---|---|---|---|---|---|
| [`LEARNableLabs/opentutor`](https://github.com/LEARNableLabs/opentutor) | 🟢 `MIT` *(sidebar + README)* | 1 | 0 | **300** | `main` | 293 courses, spaced retrieval as the product. 🔴 **NAME COLLISION** — see below |
| [`aryankeluskar/canvas-mcp`](https://github.com/aryankeluskar/canvas-mcp) | 🟢 **`ISC`** *(sidebar)* | 11 | 9 | 59 | `master` | **the only row on this shelf that reaches Gradescope.** 🔵 New licence class |

🔴 **The identity gate earned its keep twice this pass, and `p296` is the reason it was run at all.**
Both candidates passed a full-slug check and **both tripped a bare-name check**:

1. **`opentutor`** — this shelf has carried [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor)
   (MIT, 142★) since before this pass. `LEARNableLabs/opentutor` is an **unrelated repository with the
   same name.** Not a duplicate — but published without disambiguation it would have read as one row
   contradicting itself on its own star count. Both rows now name the other.
2. **`canvas-mcp`** — the bare name hit **all three shelf files**. The slug is new; the *capability* is
   the shelf's most heavily covered. This is what demoted the row from "promotion" to "promotion for
   one named reason", and it is why the row says *choose `vishalsachdev` instead* in its own cell.

🔵 **`ISC` is a licence class these shelves have never carried.** Every permissive grant here was
MIT, Apache-2.0 or BSD. ISC is OSI-approved and functionally BSD-2-Clause; the licence gate's
vocabulary should be taught it rather than left to classify it on first contact.

### 🔴 Three slugs read at payload and KEPT OFF this shelf on the README test

The README test — *does the repository itself claim an education use* — struck three admitted-elsewhere
repositories off **this** file, and `p293` set that precedent when it discharged a candidate it had
chased for three passes as *"real, permissive, and not an education repository."*

| repo | licence | adoption | why NOT an agent row |
|---|---|---|---|
| [`UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) | 🟢 `MIT` | **3.0k★ · 8 033 commits** | UK AI Security Institute's LLM eval framework. 🔴 **README mentions neither education, teaching nor students.** Shelved as a **substrate** |
| [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) | 🟢 `MIT` | **6.4k★ · 2 880 commits** | Policy enforcement, zero-trust agent identity, sandboxing, tamper-evident audit. 🔴 **No education mention.** Shelved as a **substrate** |
| [`AI-for-Education/fabdata-llm`](https://github.com/AI-for-Education/fabdata-llm) | 🟢 `MIT` | 9★ · 175 commits | 🔴 **REJECTED OUTRIGHT, not shelved anywhere.** A generic multi-provider LLM wrapper; **the only education signal is the owner's name.** LiteLLM-class alternatives are orders of magnitude better adopted |

🔵 **`fabdata-llm` is the useful rejection.** An owner called `AI-for-Education` published four repos
on `p989`'s list; **three are real education instruments and the fourth is plumbing.** An
org-name heuristic would have carried all four. The README is the test, not the namespace.

### 🔵 The channel, restated with its negative control

`curl -sI` over `github.com` was **403 on 4 of 4** probes — **including a deliberately invented
hostname, which returned the byte-identical 403.** `p294`'s rule therefore holds unchanged: a `403`
**licenses no existence claim**. All twelve reads this pass are `WebFetch` over rendered
`github.com` HTML (sidebar/About licence label plus README body). There is **no `api.github.com`
channel**; every star and fork figure below is a **rendered** read, and `p295` showed those are
**not** monotonic.

### 🔴 Standing action for the next pass — `ACTION PG-2`

**The orphan list is now partitioned; work the partition, not the list.** 481 slugs remain unshelved,
but they are not equally worth a read. `p297` measured that the **MCP/LMS-adapter cluster (~20) is
saturated** and the **institutional-layer clusters were empty**. The next pass should take the next
**named batch of ~12 from the layers this shelf still has no row for** — assessment-integrity,
early-warning/retention, and student-records interop (`1EdTech` has further repos on the list) — and
**skip the adapter cluster entirely** unless a candidate reaches a system no shelved row reaches, the
one test that admitted `aryankeluskar/canvas-mcp`.

## 🟢 Pass 296 — THE 21-PASS "NIL" WAS NOT A SUPPLY PROBLEM: A 41 000-STAR MIT ROW WAS SITTING VERIFIED IN THIS REPOSITORY, UNSHELVED

⏱️ **Eighteenth pass of `2026-10-18`.** Evidence:
[`p296-promotion-gap.2026-10-18-p296.tsv`](../evidence/p296-promotion-gap.2026-10-18-p296.tsv).

🔴 **The mandated leg `top open source AI agents education 2026 github MIT` returned its
twenty-second consecutive nil, and this pass stopped treating that as the measurement that
matters.** `p275`-`p295` ran the same query twenty-one times, recorded twenty-one nils, and
concluded each time that the population was unchanged. **The population was not the constraint.**

### 🔴 The finding: this base has a measured promotion gap and has never worked it

`p989` (`2026-10-10`) wrote
[`promotion-gap-permissive-orphans.txt`](../compose/code/p989-sha-identity-fork/promotion-gap-permissive-orphans.txt)
— **~500 slugs that appear in this repository with a permissive grant and appear on no shelf** (out of
`1 119` orphans in all). It named the gap, published the list, and **no pass since has promoted a row
out of it.** Eight days and twenty-one "nils" later the list still contains:

| orphan named by `p989` | read `p296`, `2026-10-18` | why the nil was false |
|---|---|---|
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | 🟢 **MIT** · **41.0k★** · 6.3k forks · 729 commits · `main` | 🔴 **The largest education-AI repository this base knows of, and it was not on the agents shelf.** `agents/trending.md` verified its MIT grant *first-hand* at l.3532 (`1 065` B, `sha256 ba2525637432`) and at l.3538 recorded `40 873★` — then left it in the trending log |
| [`Orenda-Project/rumi-platform`](https://github.com/Orenda-Project/rumi-platform) | 🟢 **Apache-2.0** · 18★ · 19 forks · **847 commits** · `main` | Pakistan / Taleemabad national curriculum, WhatsApp delivery, 15 languages. Present in `agents/trending.md`, `repos/trending.md` **and** `intel/open-gaps.md` — three files, no shelf |
| [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot) | 🟢 **MIT** · 9★ · 12 forks · 149 commits · `main` | Microsoft Research India + Sikshana Foundation. Curriculum-bound lesson planning — the exact capability `p292` went looking for and declared missing |
| [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | 🟢 **Apache-2.0** · **572★** · 105 forks · 4 commits · `main` | Four K-12 skills **plus an eval framework**, against a shelf that has declared an evaluation gap for several passes |

**Eight rows were promoted this pass** — five onto this shelf, three onto
[`repos/foundations.md`](../repos/foundations.md) — **and not one of them was a discovery.** Every one
was already verified somewhere in this repository.

🔴 **`p296` SELF-CORRECTION, caught by this base's own `p283` identity gate, not by a reader.** This
pass first wrote **ten**, having taken `p989`'s orphan list as current. Two of those ten —
[`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) and
[`autolab/Autolab`](https://github.com/autolab/Autolab) — **were already on the foundations shelf**,
and publishing them again produced `ADDRESS-TWICE` on two rows of one table. 🔵 **The orphan list is
dated `2026-10-10` and is itself now partly stale**, so a promotion out of it must be checked against
the shelf before it is written — **the list names candidates, not absences.** Both rows were merged
instead of duplicated, and both gained their first commit/fork/branch readings in the process; the
`Autolab` merge **downgraded** its published grade to `README-ONLY`. The agents leg was never short of supply; the path
from *verified* to *shelved* was not being walked.

🔵 **What this changes for a studio engagement, which is the only reason the shelf exists.** A reader
who opened `agents/top.md` for the last twenty-one passes was shown a shelf whose top row was
`HKUDS/DeepTutor` at `41.6k★` and was **not** shown `OpenMAIC` at `41.0k★` — a second
permissively-licensed, comparably-adopted, architecturally *different* option (multi-agent classroom
with AI classmates, versus one-to-one lifelong tutoring). **The shelf did not merely omit a row; it
misrepresented the shape of the choice.**

### 🔵 The channel, stated so the grade is auditable

`curl -sI` over `github.com` returned **HTTP 403 on 4 of 4** probes this pass — the proxy block
`p989` measured is still closed, so **no `curl` and no `api.github.com` star channel exists.** All
eleven reads this pass are **`WebFetch` over `github.com` HTML** (sidebar/About licence label plus
README body), the channel `p294` opened and `p295` reproduced. One row is weaker than the rest and is
marked in its own cell: [`autolab/Autolab`](https://github.com/autolab/Autolab) shows a
**License link with no licence name** in its sidebar and declares `Apache-2.0` **only in README
prose** — `README-ONLY` grade, shelved on the foundations file with that written down.

### 🔴 Standing action for the next pass — `ACTION PG`

**Work the orphan list before running the mandated leg.** ~500 permissive orphans remain. A pass that
returns a nil on the search leg *and* promotes nothing out of that list has not measured a thin
market; it has skipped the cheapest shelf-improving work available to it. The next pass should
promote or reject a named batch and record which.

## 🔴 Pass 295 — THE TWENTY-FIRST NIL, AND THE LAW `p294` PUBLISHED WITH ITS STAR CHANNEL IS FALSE

⏱️ **Seventeenth pass of `2026-10-18`.** Evidence:
[`p295-websearch.2026-10-18-p295.tsv`](../evidence/p295-websearch.2026-10-18-p295.tsv) ·
[`p295-star-channel.2026-10-18-p295.tsv`](../evidence/p295-star-channel.2026-10-18-p295.tsv) ·
[`p295-dns-control.2026-10-18-p295.tsv`](../evidence/p295-dns-control.2026-10-18-p295.tsv).

🔴 **`top open source AI agents education 2026 github MIT` — TWENTY-FIRST consecutive nil.**
Population unchanged from `p275`. 🔵 **And the leg carried its own proof of staleness this time:**
two separate results re-served `microsoft/ai-agents-for-beginners` as ***"12 Lessons / 67,223
stars"*** and ***"47.3k stars"*** — the exact figures `p294` refuted first-hand **the same day**
(`77.4k★`, *"18 Lessons"*). The SEO corpus this leg draws on is not merely thin; it is **demonstrably
behind the repository it describes**.

### 🔴 `p294`'s *"stars are monotonic"* — REFUTED, one pass later, in `p294`'s own channel

`p294` opened the `WebFetch`-over-`github.com` channel, read **two** repositories, refuted three
cells, and published a **rule about all repositories** — using it to discard a `32 741`-star source
claim. `p295` ran the same channel over **eleven** published cells.

| cell | published on these shelves | read `p295`, `2026-10-18` | verdict |
|---|---|---|---|
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) stars | **819★**, 12,437 commits | 🔴 **817★** · 395 forks · **12,440 commits** · MIT · branch `develop` | 🔴 **REFUTES THE RULE.** Stars **down 2** while commits advanced **3**. Up-and-down in one read is what a live repository does; a broken read would disturb **both** |
| `jupyterhub/jupyterhub` | 8.4k★, 2.1k forks, BSD-3-Clause, 8,913 commits | 8.4k★ · 2.1k · BSD-3-Clause · 8,913 | 🟢 **EXACT** |
| `instructure/canvas-lms` | 6.9k★, 3.0k forks, AGPL-3.0, 78,765 commits | 6.9k★ · 3.0k · AGPL-3.0 · 78,765 | 🟢 **EXACT** |
| `oppia/oppia` | 6.9k★, Apache-2.0, 17,004 commits | 6.9k★ · **5.8k forks** · Apache-2.0 · 17,004 | 🟢 **EXACT**, forks **new** |
| `Sunbird-Ed/SunbirdEd-portal` | 41★, 317 forks, MIT, 38,046 commits | 41★ · 317 · MIT · 38,046 | 🟢 **EXACT** — the star-blindness row holds to the digit |
| `HKUDS/DeepTutor` | 41.6k★, 5.3k forks, Apache-2.0, `v1.6.14` | 41.6k★ · 5.3k · Apache-2.0 · `v1.6.14` `2026.10.8` | 🟢 **EXACT** — `p294`'s own figure, re-read independently the same day |
| `learningequality/kolibri` | 1.2k★, MIT, 39,803 commits | 1.2k★ · **1.0k forks** · MIT · 39,803 | 🟢 **EXACT**, forks **new** |
| `portabilis/i-educar` | 719★, GPL-2.0, 34,948 commits | 719★ · **550 forks** · GPL-2.0 · 34,948 | 🟢 **EXACT**, forks **new** |
| `code-dot-org/code-dot-org` | 215,796 commits, 901★, 538 forks | 901★ · 538 · **215,808 commits** | 🟡 **DRIFTED** `+12`, not refuted |
| `Submitty/Submitty` | 802★, 1.1k forks, 9,316 commits | 802★ · 1.1k · **9,321 commits** | 🟡 **DRIFTED** `+5` |
| `Gego-K12/gegok12` | 54★, **98 forks** | 54★ · **101 forks** · **123 commits** | 🔴 **FORKS REFUTED.** The cell self-declared *"no star read this pass"* |

🔵 **Seven of eleven are exact, and that is the finding — not the two that moved.** Every cell
`p294` refuted came from a **social post or an SEO blog**; every cell read **first-hand at a pin**
confirmed. 🔵 **Staleness on these shelves tracks PROVENANCE, not age.** The defect was never *old
figures* — it was **figures this base never measured itself.**

🔵 **The asymmetry worth keeping:** `p294` was **right** to throw out the `32 741` figure — a 27 %
gap is not unstar drift. What was wrong is the **reason it gave**, and a correct answer resting on a
false rule fails the next time it is applied: under *"monotonic"*, Artemis's `−2★` reads as a broken
channel. 🟢 It is not. **A delta is not an error signal, and a downward delta is not a bad read.**

### 🔵 What this changes in how a figure is written here

🟢 `P51`'s **value · channel · resolution bound · read-date** stands, and `p295` adds the fifth
field it was missing: **the sample a general claim rests on.** `p295` read eleven and writes
*eleven* — never *all*.

## 🔴 Pass 294 — THE TWENTIETH NIL, TWO NEW SLUGS BOTH DISQUALIFIED BY THEIR OWN READMEs — and a star channel `p293` declared closed was open the whole time

⏱️ **Sixteenth pass of `2026-10-18`.** Evidence:
[`p294-websearch.2026-10-18-p294.tsv`](../evidence/p294-websearch.2026-10-18-p294.tsv) ·
[`p294-pin-grant.2026-10-18-p294.tsv`](../evidence/p294-pin-grant.2026-10-18-p294.tsv) ·
[`p294-star-channel.2026-10-18-p294.tsv`](../evidence/p294-star-channel.2026-10-18-p294.tsv).

🔴 **`top open source AI agents education 2026 github MIT` — TWENTIETH consecutive nil.** Population
unchanged from `p275`: `microsoft/ai-agents-for-beginners`, `pguso/agents-from-scratch`,
`avinash201199/free-ai-agents-resources`, plus the general-purpose set. `p286`'s reclassification
holds: **a repository that teaches agent-building is not an education-sector agent.** One source
again warns on its own that it stretches *"open source"* to cover source-available projects.

### 🟢 Four slugs read at pins, two of them new — and the README test struck all four off this shelf

`p293` set the precedent (read the README before shelving an agent) and it keeps paying.

| slug | branch as read | pin | grant, FIRST-HAND | README | verdict |
|---|---|---|---|---|---|
| [`ChurchCRM/CRM`](https://github.com/ChurchCRM/CRM) 🆕 | `refs/heads/master` | `bcf15df5de17cb9907f8db94fe44893a93bf72c4` | **MIT**, `1 076 B`, sha256₁₂ **`82ad0787803a`**, title @4 | 5 703 B, **0 education tokens** | 🔴 **NOT-EDUCATION** — church/membership management |
| [`ONLYOFFICE/CommunityServer`](https://github.com/ONLYOFFICE/CommunityServer) 🆕 | `refs/heads/master` | `fe1fa7babd093969e939ba6ff45a9fee1299dc93` | **Apache-2.0**, `11 357 B`, sha256₁₂ **`c71d239df917`**, title @33 | 6 262 B, **0 education tokens** | 🔴 **NOT-EDUCATION** — collaboration substrate |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | `refs/heads/main` | `9e01b44dd23978f9ff40b7837467f3a9f1582130` | **MIT**, `1 070 B`, sha256₁₂ **`821556e63367`**, title @0 | 16 924 B, **0 education tokens** | 🔴 **CARRIED**, and not education |
| [`MadsLorentzen/ai-job-search`](https://github.com/MadsLorentzen/ai-job-search) | `refs/heads/master` | `30158c0493ae8ae1610769955ad04b189049afe8` | **MIT**, `1 071 B`, sha256₁₂ **`accbf0accb87`**, title @0 | 34 105 B, **3 tokens in 34 kB** | 🔴 **CARRIED** — careers tooling |

🔵 **The nil is now a nil WITH VERIFIED NEGATIVES.** Nineteen passes recorded an unexamined nil on
this leg. This one reads every candidate's grant at a pin and then disqualifies it on its payload,
which is a stronger statement than *"nothing came back"*: four permissive repositories exist, and
none of them is an education agent.

### 🔴 The error `p293` NAMED, committed by `p294` against this base's own index

🔵 `p293` wrote the lesson: *"guessing a name the channel will tell you."* The mandated leg
returned a bare *"Hermes Agent (Nous Research, MIT)"* with no path. `p294` guessed
`NousResearch/Hermes`, ran `make carried` on **the guess**, got **`NEW`**, and came within one
step of opening a row for it.

🔴 **`NousResearch/Hermes` is `ABSENT-OR-PRIVATE`; `NousResearch/hermes-agent` resolves, and it has
been `CARRIED` since `p275`** — `agents/trending.md:1167` already reads *"`CARRIED` — already
shelved."* 🟢 The index was the channel, and it was not asked with the right spelling. `P1057`'s
sentence generalises once more: **a one-spelling query has not asked the index; it has asked one
spelling of it.**

### 🟢 THE PASS'S REAL RESULT: the star channel is OPEN, and reading it refutes three published figures

🔴 **`p293` concluded no first-hand star figure was available**, because `api.github.com` answers
`403` by policy for any slug this session is not attached to. 🟢 **It never tried the channel its
own [`P349`](../compose/code/p349-star-resolution-band/README.md) instrument is built on** —
`WebFetch` over the rendered `github.com` repository page, which `p110` used on **2026-10-05** and
which answers today.

| cell | what was published | read first-hand, `2026-10-18` | verdict |
|---|---|---|---|
| `microsoft/ai-agents-for-beginners` stars | `p293`: **67.2k** *and* **47.3k**, 42 % apart, from two social posts | **77.4k** stars · **25.4k** forks · **MIT** | 🔴 **BOTH REFUTED.** `p293` declined to resolve the spread and was right to; neither figure was close |
| …its **description** | *"a 12-lesson **course** about building agents"*, this base's own prose since `p275` | *"**18 Lessons** to Get Started Building AI Agents"* | 🔴 **STALE FOR EIGHTEEN PASSES** on a channel that was open throughout |
| `HKUDS/DeepTutor` stars | **41.5k** on this shelf | **41.6k** · 5.3k forks · Apache-2.0 · `v1.6.14`, `2026.10.8` | 🟢 **CONFIRMED and advanced.** Live cells updated |
| …a claim from this pass's own leg | *"over 32,741 stars and 4,274 forks"* | **41.6k / 5.3k** | 🔴 **REFUTED.** Stars are monotonic, and this base read **40.8k** at `p110`; a lower figure dated later is not a measurement |

🔵 **The error class, stated so it is not repeated:** `api.github.com` answering `403` is evidence
about `api.github.com`. `p293` wrote that sentence about `rate_limit` in the same pass it drew the
opposite conclusion about stars.

### 🟢 `HKUDS/DeepTutor` — the grant has NOT moved, re-read at a new pin

`LICENSE` at `refs/heads/main` pin **`6cf793bd868ba5ecbe64722936d4be8fab5a01df`**: `200`,
**`11 408 B`**, sha256₁₂ **`cd2f54e1e506`**, family **Apache-2.0**, title @34, no dual grant.
🟢 **Byte-identical to the blob already on record** (`11 408 B`, sha256 `cd2f54e1e5066644`). Same
payload, different pin — so the grant has not moved, and the row needs no re-grading.

### 🔴 What this pass did NOT do

🔴 **`huggingface.co` remains closed**, so the Horus **weights'** grants are still unread —
`p293`'s bound is unchanged, and a grant read on training code says nothing about weights.
🔴 **No new agent row for the twentieth pass running.** The structural reason stands: one source
states outright that no dedicated ranking of education-focused agents exists.

## 🔴 Pass 293 — NO NEW AGENT ROW, the NINETEENTH nil — and the candidate three passes chased turned out not to be an education agent at all

⏱️ **Fifteenth pass of `2026-10-18`.** Evidence:
[`p293-websearch.2026-10-18-p293.tsv`](../evidence/p293-websearch.2026-10-18-p293.tsv) ·
[`p293-slug-oracle.2026-10-18-p293.tsv`](../evidence/p293-slug-oracle.2026-10-18-p293.tsv).

🔴 **The mandated agent leg is NINETEEN consecutive nils**, and the population is unchanged from
`p275`: `microsoft/ai-agents-for-beginners` (MIT, a 12-lesson **course** about building agents),
`pguso/agents-from-scratch` (MIT, a teaching repo), `avinash201199/free-ai-agents-resources`
(grant not stated by the source), plus the general-purpose set. 🔵 `p286`'s reclassification
holds without amendment: **a repo that teaches agent-building is not an education-sector agent.**
🔴 One source this pass states outright that no dedicated ranking of education-focused agents
exists — which is the structural reason the leg is nineteen deep rather than a search defect.

### 🔴 `p292`'s ranked item 1 is DISCHARGED — and discharging it REMOVED a candidate from this shelf

`p292` recorded **TokenAI's Horus family** as `CANDIDATE-ATTRIBUTED` and called it *"the actual
finding"* of that pass: the first permissive **EMEA-origin** model family this base had seen,
stuck behind an unknown slug. `p293` recovered the slug, read the grant at a pin — and the read
is what disqualifies it.

| what `p292` reported | what the payload says, read at a pin |
|---|---|
| `Horus Taleeq 0.2B Base`, reported **MIT** | 🟢 **CONFIRMED FIRST-HAND. `GRANTED-AT-PIN`** — slug [`tokenaii/Horus-Taleeq-0.2B-Base`](https://github.com/tokenaii/Horus-Taleeq-0.2B-Base), branch `main`, pin `f7a7700289791a9c114ab038af73b4d45c17c7e7`, `LICENSE` **`200`**, **1 080 B**, sha256₁₂ **`96c22722c817`**, family **MIT** by the shared `p228`/`P237` classifier (title line @0, no dual-grant preamble) |
| …and its README | 🟢 Also states MIT → `p288` channel verdict **`AGREE`**, posture **`BUILD-ON`**. Both channels, one answer |
| *"~6 B Arabic tokens"*, *"~30 h on one RTX PRO 6000"* | 🟢 **Sharpened from the repo itself**: ledger **6 000 308 224** tokenizer IDs; core pretraining wall-clock **28 h 40 m 20.604 s** — press rounded 28.67 h up to 30 |
| the parameter count, reported two ways (~199.9M / ~204.6M) | 🟢 **RESOLVED: the repository claims "exactly 199,916,160".** The 204.6M figure is not what the repo says |
| *"TokenAI (Cairo)"* | 🔴 **NOT RESOLVED, and this base asserts neither.** One outlet says Cairo, another Alexandria; **the README names no city.** Owner is named: **Assem Sabry**; TokenAI self-describes as *"a startup and nonprofit organization focused on open Arabic AI research"* |
| 🔴 **its place on an EDUCATION shelf** | 🔴 **REFUTED. The README carries ZERO education claims.** The single `teacher` hit is *"teacher outputs"* — distillation, not pedagogy. No tutoring, no assessment, no curriculum, no learner |

🔴 **And the second family member settles the question.** The oracle found one more live repo,
[`tokenaii/Horus-Lens-1.0`](https://github.com/tokenaii/Horus-Lens-1.0) (pin
`86cade44ab562fb929539a482f440aef28ca301c`) — and it is a **text-to-image** model fine-tuned from
`Tongyi-MAI/Z-Image`. Not education. Not even language. Its grant is a
**`DANGLING-CLAIM`**: `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` all `404` at the pin,
while the README asserts Apache-2.0 — posture **`ASK`**, per `p288`.

🔵 **So the honest verdict is the one this shelf's own rule already implies.** `p286` struck an
agent-building *course* off this table for the same reason: the subject matter is not education.
A general-purpose Arabic base model is a **substrate**, and it belongs on
[`repos/foundations.md`](../repos/foundations.md) with its boundary stated — **not here**.
🟢 That is a better outcome than the row would have been: the first EMEA-origin permissive grant
this base has ever read first-hand, filed where a studio would actually reach for it.

### 🔵 What a studio takes from this

🔴 **Nineteen passes of looking have not produced an education-sector agent with a permissive
grant.** That is now a measurement, not a gap in the search. The agent layer a client asks for
gets **composed** from general-purpose frameworks over a vertical platform — which is what every
recipe in [`compose/patterns.md`](../compose/patterns.md) already does — and the billable
component is the one no repository supplies: the decision record (`P49`). 🟢 What `p293` adds to
that story is a *substrate* for Arabic-medium work, where this base had none.

## 🔴 Pass 292 — NO NEW AGENT ROW, the mandated leg's EIGHTEENTH nil, and one deployed state education agent that cannot be carried because it has no grant

⏱️ **Fourteenth pass of `2026-10-18`.** Evidence:
[`p292-websearch.2026-10-18-p292.tsv`](../evidence/p292-websearch.2026-10-18-p292.tsv) ·
[`decision-store-worked.2026-10-18-p292.jsonl`](../evidence/decision-store-worked.2026-10-18-p292.jsonl).

🔴 **No row is added to the table below this pass.** What was searched, and what each leg
returned, is written down leg by leg in the evidence TSV — **four mandated legs, four regional
legs, three directed legs**. Summary of the misses, because an informed gap is information:

| leg | outcome | why it produced no row |
|---|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **NIL, 18th consecutive** | population unchanged since `p275`; the hits are **courses about building agents** and general-purpose frameworks, not education-sector agents |
| `github trending education AI 2026` | 🔴 **NIL for education, 9th** | `github.com/trending` answers `403`; the leg degrades to third-party trackers |
| `open source platform education ERP CRM MIT Apache` | 🔴 **NIL for a NEW permissive platform, 13th** | 10 of 10 results were vendor-glossary or directory pages; the three named platforms are all **already carried** |
| `AI education industry trends 2026` | 🟡 non-nil, **no code** | market sizing and adoption percentages only |
| the four mandated regional legs | 🔴 EMEA **6th nil** · 🟡 APAC thin · 🟢 NA and LATAM non-nil | policy, money and adoption figures; **no repository address in any of the four** |
| `Egypt in Arabic` *(directed, `p291` item 9)* | 🟢 **non-nil** | returned a **deployed** state education agent with **no grant** — see below |
| `Mexican education CODE in Spanish` *(directed, `p291` item 10)* | 🔴 **NIL on code** | the Mexican state ships education platforms as **services behind an identity gate**, not repositories. Leg **discharged as a measured negative** |

### 🔴 `سيا` (Sia) — an education agent in production that this shelf cannot carry

🟢 Egypt's MCIT launched, early 2026, a secondary-school **AI teacher** named `سيا` (Sia)
alongside the national LLM `كرنك` (Karnak), which officials place inside **public digital
infrastructure** so startups can build on it.
🔴 **No repository, no licence, no code channel reachable from here.** 🟡 ATTRIBUTED to Egyptian
press and MCIT announcements; primary government sources were not read.

🔵 **Recorded as a named non-row on purpose.** The quality bar on this shelf is a real repo URL,
a real licence and a real description; `Sia` has none of the three. Writing it into the table
would compile an entity whose licence field is a guess. 🔵 It is written **here** so the next
pass recognises it rather than re-discovering it as new. The same posture covers **TokenAI's
Horus family** (reported MIT / Apache-2.0, Cairo) — recorded in full with its four refused
verification channels on [`agents/trending.md`](trending.md), **not admitted here**.

### 🟢 What DID change for every agent row on this shelf

🟢 **The thing these agents' recommendations terminate in now exists:**
[`compose/code/p292-decision-evidence-store`](../compose/code/p292-decision-evidence-store/README.md),
**106 offline controls**, in `make hooks`. 🔴 **Refusal `R1` is the one that concerns this
shelf: an agent cannot be recorded as the decider.** Every row here that scores, ranks, flags
or recommends about a learner is an *advisory* input under the Act's education limb, and the
store refuses to record it as anything else — `R5b` rejects any agent `role` but `"advisory"`.
🔵 `P45` has said in prose since `p290` that *"the prompt is not a control."* That sentence now
has an implementation behind it.

## 🟢 Pass 291 — ALL SEVEN SEGMENTS ARE VERIFIED **AT THE PIN**, THE RULE THAT SAID THEY COULDN'T BE WAS THIS BASE'S OWN, AND THE FIVE "NOT EDUCATION" SEGMENTS EACH SHIP A TRAINING AGENT

⏱️ **Thirteenth pass of `2026-10-18`.** Evidence:
[`submodule-pin-grant.2026-10-18-p291.tsv`](../evidence/submodule-pin-grant.2026-10-18-p291.tsv) ·
[`segment-education-surface.2026-10-18-p291.tsv`](../evidence/segment-education-surface.2026-10-18-p291.tsv) ·
[`guard-vocabulary.2026-10-18-p291.tsv`](../evidence/guard-vocabulary.2026-10-18-p291.tsv) ·
[`p291-websearch.2026-10-18-p291.tsv`](../evidence/p291-websearch.2026-10-18-p291.tsv).

🔴 **Mandated agent leg: SEVENTEENTH consecutive nil**, same population as every pass since
`p275`. 🔴 Trending leg nil for education for the **eighth**; verticals leg found no new
permissive ERP/CRM for the **twelfth**. Every leg is written down with what it returned — an
undeclared nil looks exactly like coverage. 🟢 **Everything below came from reading
repositories**, the sixth pass running.

### 🟢 `p290`'s ranked item 1, discharged: the five unprobed segments

`p290` probed **2 of 7** `iblai` segments and left the rest as its own first backlog item.
All five are read, **at the commit the superproject pins**, and all five carry their own
payload — byte-identical to the two already on this shelf and to the superproject's:

| segment | address | pinned gitlink | grant read **at that commit** |
|---|---|---|---|
| 🟢 enterprise | [`iblai/enterprise-agents`](https://github.com/iblai/enterprise-agents) | `7f00879a9f57` | 🟢 **MIT**, root `LICENSE`, 1 063 B, sha256₁₂ `f1269b7b2313` |
| 🟢 government | [`iblai/government-agents`](https://github.com/iblai/government-agents) | `fbf903250c96` | 🟢 **MIT**, root `LICENSE`, 1 063 B, sha256₁₂ `f1269b7b2313` |
| 🟢 legal | [`iblai/legal-agents`](https://github.com/iblai/legal-agents) | `b059cd452bf3` | 🟢 **MIT**, root `LICENSE`, 1 063 B, sha256₁₂ `f1269b7b2313` |
| 🟢 financial-services | [`iblai/financial-services-agents`](https://github.com/iblai/financial-services-agents) | `6ea18f015b1e` | 🟢 **MIT**, root `LICENSE`, 1 063 B, sha256₁₂ `f1269b7b2313` |
| 🟢 medical-healthcare | [`iblai/medical-healthcare-agents`](https://github.com/iblai/medical-healthcare-agents) | `cd0d9fcfa523` | 🟢 **MIT**, root `LICENSE`, 1 063 B, sha256₁₂ `f1269b7b2313` |

🟢 **7 of 7 `GRANTED-AT-PIN`**, one licence path each, all at the root. The gitlinks were
re-derived **blind** (`git ls-tree HEAD` on a fresh clone) and reproduce `p290`'s seven
exactly, as do its **95 agents / 76 tool skills** — counted independently, same totals.

### 🔴 And the rule `p290` wrote was wrong, in the direction that loses rows

`p290` required that a submodule's `HEAD` **equal** the pinned gitlink before its grant
counted. It read each one at `HEAD` because that is what `git ls-remote` returns.
🟢 **But `raw.githubusercontent.com` serves a payload at an arbitrary commit, so the pinned
SHA is directly readable** — 7/7 answered `200` at their pin this pass. `HEAD` is not an
input at all.

🔴 **The old rule fails in the restrictive direction, which is the dangerous one here.** It
reports *"cannot verify"* for a submodule whose `HEAD` has merely moved on — inviting the
next pass to re-probe at `HEAD`, find a relicensed `HEAD`, and publish **that** licence, when
a `git clone --recurse-submodules` lands on **the pin**.
🟢 `ACTION p291` is the corrected rule, with **31 controls in `make hooks`**:
[`gate-pin-grant`](../compose/code/p291-submodule-pin-grant/README.md).

### 🔴 The five segments are **not** "not education" — every one ships a training agent

`p290` wrote the five off as `OUT-OF-SCOPE (not an education segment)`. That judgement was
made from the **segment name**, never from the agent list. Reading the agent list:

| segment | the learning agent inside it | regulated credential? |
|---|---|---|
| enterprise | `training-agent` — *"Learning Coach"*: employee development paths, skill-gap analysis, course recommendations | no |
| government | `employee-training-agent` — workforce development, mandatory training compliance, upskilling | no |
| legal | `training-agent` — *"Training & CLE"*: **CLE credit tracking**, associate development | 🔴 **yes — CLE** |
| financial-services | `employee-training-agent` — compliance certification tracking, **FINRA continuing education** | 🔴 **yes — FINRA CE** |
| medical-healthcare | `compliance-training-agent` (HIPAA training, certification status) · `patient-education-agent` (patient-facing materials at a health-literacy level) | no |

🔴 **Six learning-and-development agents, one in every one of the five excluded segments, two
of them tracking a regulated professional credential.** Under **EU AI Act Annex III(3)** the
high-risk education category is not "schools": limb (a) covers access, admission or assignment
to educational **and vocational** training institutions, and limb (b) the evaluation of
learning outcomes including where they steer a learner's path. Matching **one** limb suffices.
🟡 Posture: Annex III(3)'s wording is **ATTRIBUTED** to a conference reproduction and
commentary — EUR-Lex was not read, and `p289` measured those hosts `POLICY-REFUSED` from here.

🔴 **And the guard density runs the wrong way.** 7 of 30 agents inside the two education
segments carry a human-decision guard (**23 %**); 5 of 65 outside them do (**8 %**). Of the six
L&D agents above, **one** carries any guard. The agents sitting in the high-risk **vocational
training** bucket are the ones without it.

### 🟡 A wording correction to this shelf's own `p290` row

`p290` published that three sibling agents *"refuse the **sole-basis** act in their own text"*.
🟢 **The substance is confirmed** — all three carry a human-decision guard, re-read first-hand.
🔴 **The words are not theirs.** *"Sole basis"* is the **regulator's** phrase. It occurs in
**1 of 95** agents in this corpus, and that one occurrence is a note about CPT code selection
in `medical-coding-agent`'s `MEMORY.md` — not a guard. What the payloads actually say is
*"unilaterally"*, *"not a verdict"*, *"not by any single professional or AI tool"*,
*"never make eligibility determinations"*, *"support human decision-making"*.

🔵 **Why that is worth a correction and not a shrug:** a compliance sweep that greps the
regulator's vocabulary over this MIT corpus scores **one hit, and it is a false positive**,
while the guard it is hunting is present in **12** agents under four other phrasings. An
auditor's keyword list and an engineer's prompt do not share a dictionary. Full vocabulary:
[`guard-vocabulary.2026-10-18-p291.tsv`](../evidence/guard-vocabulary.2026-10-18-p291.tsv).

## 🟢 Pass 290 — THE GRANT WAS ON THE SUPERPROJECT AND THE AGENTS WERE IN SEVEN OTHER REPOSITORIES, AND READING EACH ONE OVERTURNED THIS BASE'S OWN "ZERO PERMISSIVE" VERDICT

⏱️ **Twelfth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p290.tsv`](../evidence/verified-repos.2026-10-18-p290.tsv) ·
[`submodule-grant-boundary.2026-10-18-p290.tsv`](../evidence/submodule-grant-boundary.2026-10-18-p290.tsv) ·
[`p290-websearch.2026-10-18-p290.tsv`](../evidence/p290-websearch.2026-10-18-p290.tsv).

🔴 **Mandated agent leg: SIXTEENTH consecutive nil.** Same population as every pass since
`p275` — `microsoft/ai-agents-for-beginners`, `pguso/agents-from-scratch`,
`rohitg00/ai-engineering-from-scratch`, `avinash201199/free-ai-agents-resources`, plus the
general-purpose set. Engineer curricula and link catalogues, not learner-facing education
agents. The nil is recorded, not hidden: an undeclared nil looks exactly like coverage.
🟢 **Every row below came from a DIRECTED leg**, the sixth pass running.

### 🟢 The new rows — one MIT configuration set across three repositories, plus two early-warning rows

| agent | address | grant (read from payload) | why it matters |
|---|---|---|---|
| 🟢 **Claw Agents (superproject)** | [`iblai/iblai-claw-agents`](https://github.com/iblai/iblai-claw-agents) | 🟢 **MIT** — root `LICENSE`, **1 063 B**, HEAD `acbd32b4a938`, sha256₁₂ `f1269b7b2313` | Drop-in **OpenClaw / NemoClaw** agent configurations, **95 agents and 76 tool skills** across 7 segments. 🔴 **Its own tree is 13 files and 7 of them are `160000 commit` gitlinks** — see the boundary finding below |
| 🟢 **Higher-education agents** | [`iblai/higher-education-agents`](https://github.com/iblai/higher-education-agents) | 🟢 **MIT** — own root `LICENSE`, **1 063 B**, HEAD `1a2d898bbd04`, sha256₁₂ `f1269b7b2313` | **Campus Assistant + 16 specialists**, 90 files. Includes `application-reader-agent`, `enrollment-agent`, `yield-agent`, `retention-agent`, `financial-aid-agent`, `academic-advisor-agent`, `tutoring-agent`. Tool skills for **Canvas, Banner, Slate, Workday, EAB Navigate, Civitas Learning, Handshake, Salesforce Education Cloud, ServiceNow, Blackbaud Raiser's Edge** |
| 🟢 **K-12 agents** | [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents) | 🟢 **MIT** — own root `LICENSE`, **1 063 B**, HEAD `54ee9d91eecd`, sha256₁₂ `f1269b7b2313` | **School Assistant + 12 specialists**, 79 files. Includes `special-education-agent`, `assessment-agent`, `curriculum-alignment-agent`, `writing-feedback-agent`, `lesson-planning-agent`, `student-safety-agent`, `family-communication-agent`. Tool skills for **PowerSchool, Google Classroom, Google Workspace for Education, NWEA MAP, i-Ready, Edulastic, Khan Academy, ClassDojo, ParentSquare, Frontline, EBSCO** |
| 🟢 **student-signal** | [`cedanl/student-signal`](https://github.com/cedanl/student-signal) | 🟢 **MIT** — root `LICENSE`, **1 078 B**, HEAD `4463e8d17cfb`, sha256₁₂ `2c4289f4e480` | 🇳🇱 **EMEA-origin code**, Dutch higher education. Dropout prediction as a *library*, not an app: `prepare()` / `rank()` / `evaluate()`, any sklearn-compatible estimator, **invitation-rule methodology (Eegdeman, 2022)**, precision/recall at multiple invitation thresholds. 36 files, CI + docs + publish workflows, 4 test modules |
| 🟡 **EWStools** | [`jknowles/EWStools`](https://github.com/jknowles/EWStools) | 🟡 **GPL-3.0 only** — root `LICENSE`, **35 156 B**, HEAD `025a5dd5f1a3`, sha256₁₂ `65a7aee2cb0d`; `DESCRIPTION` declares `License: GPL-3` | 🇺🇸 The R tooling **behind the Wisconsin Dropout Early Warning System** (author email `Jared.Knowles@dpi.wi.gov`) — the first code row on these shelves whose provenance is a **US state education agency**. 🔴 **Dormant: last commit `2016-02-03`.** Read it as a requirements document, not as a dependency |

🔴 **Three addresses the same legs returned, and NONE of them is a row:**
`sp103107/NORA` and `anwarulh007/eduprotect` **do not resolve on either available channel**
(13 licence rungs × 2 refs return no `200`, not even a README; `git ls-remote` answers with a
credential prompt rather than a SHA). `ekoffi2/Machine-learning` resolves and serves **no
grant** across a **2-file tree** — `README.md` and `Studnt dropout predictions.Rmd`.
🔵 **`anwarulh007/eduprotect` is the worse shape of the two phantoms:** `awesome.ecosyste.ms`
lists it **with an MIT licence field and a star count**. A machine-readable grant assertion for
an address that does not resolve outranks a dangling README claim, because an aggregator is
exactly what a dependency scanner would believe.

### 🔵 The boundary finding: `ACTION p290` — a grant can be PRESENT, ROOT-LEVEL, AUTHORITATIVE AND VERBATIM, and still not cover the bytes you vendor

Every licence instrument on these shelves asks one of two questions. **Where is the grant?**
(`p215` path, `p969` root-only, `p742` body-vs-reference, `p259` location class.) **What does
the grant say?** (`p287` family, `p289` authority-vs-restatement.) 🔴 **A `160000 commit`
gitlink asks neither.** The payload is present, at the root, authoritative and byte-verbatim
MIT — and the 95 agent configurations a studio would actually copy into `/sandbox/.openclaw/`
**are not in that repository at all.**

🟢 **The rule this pass writes down, and the condition that makes it sound:** a submodule's
grant is verified when its **own payload is read first-hand** *and* the **HEAD it was read at
equals the gitlink SHA the superproject pins**. The second half is what keeps this inside
`ACTION VM` *(no row inherits a grant from a sibling)* — the commit whose grant was read is the
commit a recursive clone lands on. Where a submodule has moved past its pin, the pin is an
**unread commit** and the verdict is `UNVERIFIED-AT-PIN`, never `GRANTED`.

🟢 **Measured, 2 of 2 education segments `GRANTED-AT-PIN`:** `higher-education` pins
`1a2d898bbd04ffd6…` and HEAD is `1a2d898bbd04`; `k-12` pins `54ee9d91eecd964f…` and HEAD is
`54ee9d91eecd`. Both serve a payload **byte-identical** to the superproject's.
🔴 **Five of seven segments are UNPROBED** — enterprise, government, legal, financial-services,
medical-healthcare — and that is a declared gap, not a pass. This base publishes education, so
they are out of scope here; a Globant engagement in any of those verticals **must probe its own
segment**, because the single MIT badge on the superproject is precisely what would be read
instead.

🔵 **Contrast with `p289`, one pass back.** `p289` found a **catalogue** licence mistaken for a
project licence (`500-AI-Agents-Projects`: an MIT badge over links it does not own). A gitlink
is the same question with a **better answer available** — a catalogue's targets cannot be
checked in bulk, a submodule's can, because the superproject pins an exact commit.

### 🔴 `T-p288b` CORRECTED — "zero permissive" for special education was true for application code and FALSE for the category

🔴 **What this base published two passes ago** *(`intel/trends.md`, `T-p288b`)*: of the entire
open source answer to IEP/504 administration, *"One copyleft, two unusable. Zero permissive. A
studio taking an IEP engagement **writes it**."*

🟢 **What `p290` read first-hand:** [`iblai/k-12-agents`](https://github.com/iblai/k-12-agents)
ships `agents/special-education-agent/` under **MIT**, and its `SOUL.md` and `MEMORY.md` encode
the statutory frame the three `p288` repositories were valued for: **IDEA 2004**, the **13 IDEA
disability categories**, **Section 504**, **FAPE/LRE**, **prior written notice**, **annual
review and triennial re-evaluation**, **RTI/MTSS**, **ESY**, **age-16 transition planning**, and
**FERPA** treatment of disability records.

🟡 **The correction is bounded, and the boundary matters more than the headline.** This is an
**agent configuration**, not an application: 5 files, no application code, no build, no tests,
and it requires an OpenClaw/NemoClaw host to run. `T-p288b`'s sentence *"a studio writes the
application"* **still holds**. What is refuted is *"zero permissive in the category"* — there is
now an MIT starting point for the **statutory reasoning layer**, which was the expensive half.

🟢 **And the config encodes the compliance posture `T-p288a` says is the regulatory interface:**
*"Never make eligibility determinations — eligibility requires a qualified multidisciplinary
team evaluation and legal decision"*, and *"IEP decisions are made by the full team, including
parents and guardians, not by any single professional or AI tool."*

🔵 **The same property, verified across the two high-risk siblings**, which is why it reads as a
design stance rather than one file's wording — `application-reader-agent`: *"Never issue a final
admit or deny decision unilaterally; always present findings as input for the human reader"*,
plus *"flag anomalies … as observations, not conclusions"*; `retention-agent`: *"Treat every risk
flag as a hypothesis to be confirmed, not a verdict"*, *"use the risk score to triage, not to
rank human worth"*, and *"log every intervention — date, method, response, outcome"*.
🟢 **Admissions, student evaluation and IEP eligibility are the three acts the EU AI Act,
Vietnam's sole-basis clause and the Oklahoma/Maryland rules all name**, and all three configs
refuse the sole-basis act in their own text.

🟡 **One identity correction, before it becomes two rows.** `iblai/claws` is **not** a second
repository: identical HEAD `acbd32b4a938`, byte-identical `LICENSE` *(`f1269b7b2313`)* and
byte-identical `README.md` *(13 723 B, `2db8651cc58b`)* as `iblai/iblai-claw-agents`. GitHub
serves both spellings and the superproject's own quickstart names the shorter one.
**`ACTION WX` / `gate-identity`'s exact shape, caught before publication rather than after.**

### 🔴 What this pass could NOT do, stated because a silent limitation reads as a clean run

🔴 **This base's own `ladder.sh` and `enumerate.sh` would not execute in this environment** —
the runner refused to run shell scripts from the clone. The measurement was re-implemented
directly: a **13-rung** path ladder × 2 refs over `raw.githubusercontent.com`, and
`git clone --depth 1` + `git ls-tree -r` for enumeration. 🔴 **13 rungs is not `make reach`'s
55**, so **no absence in this pass carries 55-rung authority** — the positives are payloads
read first-hand, the negatives are 13-rung negatives and are labelled as such in the evidence.
🟡 `make hooks` itself ran clean *(all 12 gates PASS)*; only the two directly-invoked scripts
were refused.

# Top AI agents — Education

> Education-specific open source agents Globant AI Studios can compose or customize.
> Every licence in the tables below was read **first-hand** this pass from the repository's
> own `LICENSE` payload (`raw.githubusercontent.com`), not from a secondary source.
> Star counts are as served by the repository page or the GitHub topic listing on 2026-10-17.
> Evidence: [`verified-repos.2026-10-17-p264.tsv`](../evidence/verified-repos.2026-10-17-p264.tsv)
> and [`verified-repos.2026-10-17-p265.tsv`](../evidence/verified-repos.2026-10-17-p265.tsv),
> extended by [`verified-repos.2026-10-17-p266.tsv`](../evidence/verified-repos.2026-10-17-p266.tsv)
> (pass 266: the Artemis/Iris/Pyris rows and the first payload-verified Portuguese-language agent),
> extended again by [`verified-repos.2026-10-17-p267.tsv`](../evidence/verified-repos.2026-10-17-p267.tsv)
> (pass 267: the LMS-side MCP servers, and a re-probe of every "no licence payload" row against a
> 19-path x 4-ref set that includes the **British spelling `LICENCE`**),
> and extended again by [`verified-repos.2026-10-17-p268.tsv`](../evidence/verified-repos.2026-10-17-p268.tsv)
> (pass 268: the **third** MCP-addressable LMS — Google Classroom / Workspace for Education — eight
> servers probed, seven permissive and **one a custom all-rights-reserved licence wearing the same
> description**),
> and extended again by [`verified-repos.2026-10-17-p269.tsv`](../evidence/verified-repos.2026-10-17-p269.tsv)
> (pass 269: the first two **African-context** education agents this base has located — both of
> which serve **no grant at all** — plus a blind re-measure of three carried APAC rows that
> **reproduced every published figure**, and the search-leg ledger
> [`p269-websearch.2026-10-17-p269.tsv`](../evidence/p269-websearch.2026-10-17-p269.tsv)).

## 🟢 Pass 289 — THE CURRICULUM LAYER IS READABLE AFTER ALL, AND WHAT IT SERVES IS A **RESTATEMENT** OF A LICENCE NOBODY HERE CAN REACH

⏱️ **Eleventh pass of `2026-10-18`.** Evidence:
[`curriculum-licence-restatement.2026-10-18-p289.tsv`](../evidence/curriculum-licence-restatement.2026-10-18-p289.tsv) ·
[`curriculum-authority-egress.2026-10-18-p289.tsv`](../evidence/curriculum-authority-egress.2026-10-18-p289.tsv) ·
[`p289-websearch.2026-10-18-p289.tsv`](../evidence/p289-websearch.2026-10-18-p289.tsv).

🔴 **Mandated agent leg: FIFTEENTH consecutive nil**, same population, same reason —
`microsoft/ai-agents-for-beginners`, `ashishpatel26/500-AI-Agents-Projects`,
`ARUNAGIRINATHAN-K/awesome-ai-agents-2026`, the Hugging Face Agents Course,
`rasbt/LLMs-from-scratch`. The one education-shaped hit this pass was a *"Virtual AI Tutor"*
entry **inside** `500-AI-Agents-Projects` — 🔵 **a link in a catalogue, and the catalogue's own
MIT badge does not cover the projects it lists.** Recorded so no later pass reads that badge
as a grant.

### 🟢 The three new agent-layer rows, all MIT, all read first-hand

| agent | address | grant (read from payload) | why it matters |
|---|---|---|---|
| 🟢 **Oak Curriculum API** | [`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) | 🟢 **MIT** — root `LICENSE`, **1 077 B**, `main`, HEAD `17fc866b2611`, sha256₁₂ `0eeb9d32caed` | The service layer over the **National Curriculum for England**. 🔴 Its own `LICENSE` covers the **code only**: *"Curriculum content served through the API — lesson materials, videos, worksheets and quizzes — is not covered by this repository's licence."* |
| 🟢 **Oak AI plugins** | [`oaknational/oak-ai-plugins`](https://github.com/oaknational/oak-ai-plugins) | 🟢 **MIT** — root `LICENSE`, **1 085 B**, `main`, HEAD `f5a1e88242ea`, sha256₁₂ `e90b3e1c8e94` | Oak's Open Curriculum plugin **for AI assistants** — the agent-facing edge of a national curriculum. Curriculum data rides under **OGL v3.0**, not MIT |
| 🟢 **Oak curriculum ontology** | [`oaknational/oak-curriculum-ontology`](https://github.com/oaknational/oak-curriculum-ontology) | 🔵 **SPLIT: MIT** (`CODE-LICENSE.md`, 1 491 B, `427f1d8b0cc1`) **+ OGL v3.0** (`DATA-LICENSE.md`, 2 408 B, `c117e319f357`) | The curriculum **as a knowledge graph** an agent can reason over: 31 classes, 75 properties, **38 SHACL shapes**, Turtle/JSON-LD/RDF-XML/N-Triples/SQLite |

🟡 `oaknational/oak-open-curriculum-ecosystem` returned **`CARRIED`** from `make carried`
before a row was written, and `fundacion-hiperactiva/ona-oak-ai-plugins` and
`fh-yarbouh/oak-open-curriculum-ecosystem` are **forks**. Four of seven candidates were not
new, which is what that gate is for.

### 🔴 The finding a studio has to read before it sells anything "curriculum-aligned"

`ACTION p289` grades a licence payload on an axis no instrument here had:
**is the payload the licence, or the licensee's RESTATEMENT of one?**

| | self-contained | restated |
|---|---|---|
| what it is | the payload **is** the licence (MIT, Apache-2.0, AGPL-3.0) | a paraphrase of a licence whose authoritative text lives on a **third-party host** |
| verifiable from the clone? | 🟢 yes | 🔴 no |
| `p742`'s verdict | `GRANTED` | 🔴 **also `GRANTED`** |

Seven payloads over five Oak repositories: **5 `AUTHORITATIVE-BODY` (all MIT — the code) and
2 `RESTATEMENT` (both OGL v3.0 — the curriculum data).** 🔵 **The split is the finding: the
code is verifiable and the asset is not.**

🔴 **And both restated payloads require TWO DIFFERENT attributions.** `DATA-LICENSE.md`
line 19 prescribes, verbatim:

> Contains public sector information licensed under the Open Government Licence v3.0.

…and line 54, in its own summary block, asks instead for `Must provide attribution: "Oak
National Academy"`. `LICENSE.md` does the same thing forty lines apart (L27 / L67).
**A studio that credits "Oak National Academy" and stops has not met the condition the same
file states above it.** 🔵 All three Oak licence files pair terms with a friendly summary, and
**in all three the summary states the obligation differently from the terms above it** — 3 of
3. A reader who stops at the summary, which is what a summary is for, discharges the wrong
obligation.

🟡 `LICENSE.md` also advertises `DATA-LICENSE.md` as the *"Full OGL 3.0 License"*. It is a
restatement; the authoritative text is at the National Archives. `self_description_verdict()`
→ **`OVERSTATED`**.

### 🟢 Two things this pass CONFIRMED, and one it REFUTED

- 🟢 **Commercial use is real, and now payload-backed.** `DATA-LICENSE.md`, first-hand:
  *"exploit the information commercially and non-commercially … by including it in your own
  product or application."* These shelves have carried that permission **since pass 5 on
  British education press alone**. It is now read from the grant.
- 🔴 **The UK-only reservation is REFUTED.** This base has carried *"indicios de restricción
  geográfica al Reino Unido, que hay que confirmar antes de proponer el corpus fuera de UK"*
  beside that claim. The payload carries **no territorial term at all**. Its only jurisdiction
  clause is *"This licence is governed by the laws of England and Wales"* — 🔵 **choice of law,
  not a restriction on where the corpus may be used.** The reservation is withdrawn.
- 🟡 **The exemptions are the real bound, and they cannot be closed from the payload.** OGL
  does not cover *"third party rights Oak National Academy is not authorised to license"* —
  unbounded from outside, over **50 948 key learning points**. `T-p287a` is sharpened, not
  discharged: *"curriculum-aligned"* is safe for the **ontology and the structure**, and the
  per-asset clearance question stays open.

### 🔴 Why the primary sources are not on this page

The register has ranked *"read five national curriculum licences as primary sources"* **first
for three passes** and no pass had run it. `p289` ran it. **It cannot be run from here:**
**12 jurisdictions' licensing-authority hosts, 2 independent egress paths, 12/12
`POLICY-REFUSED`, 0 reachable** — including the National Archives text that Oak's own payloads
name as authoritative, and **including ACARA**, the one curriculum licence this base has
always claimed to have read first-hand.

🔵 **That is a measurement, not a deferral**, and it is the same class as the `github.com/trending`
403 that `p285` struck from the backlog. Every curriculum-licence claim on these shelves is
sourced from a **derivative publisher's restatement** or from **secondary press** — now stated,
where before it was silent.

## 🟢 Pass 288 — BLACKBOARD IS THE FOURTH MCP-ADDRESSABLE LMS AND THE FIRST WHOSE COMMUNITY SERVERS SERVE NO GRANT AT ALL, and special education is a whole category with no permissive answer

⏱️ **Tenth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p288.tsv`](../evidence/verified-repos.2026-10-18-p288.tsv) ·
[`p288-websearch.2026-10-18-p288.tsv`](../evidence/p288-websearch.2026-10-18-p288.tsv) ·
[`p288-readme-channel.2026-10-18-p288.tsv`](../evidence/p288-readme-channel.2026-10-18-p288.tsv).

🔴 **Mandated agent leg: FOURTEENTH consecutive nil**, same population, same reason —
`microsoft/ai-agents-for-beginners`, `ashishpatel26/500-AI-Agents-Projects`,
`ARUNAGIRINATHAN-K/awesome-ai-agents-2026`, the Hugging Face Agents Course,
`rasbt/LLMs-from-scratch`. Every row is a **curriculum for engineers** or a **catalogue of
links**. `p286` settled the posture and the four passes since have each confirmed it: **the
battery is corroboration, the gap-directed leg is extension.** Five passes running, every
new row came from a directed leg.

### 🟢 The six new rows, and FIVE of them cannot be built on

| agent | address | grant (read from payload) | why it matters |
|---|---|---|---|
| 🟡 **EduHelp** | [`AaronGrace978/EduHelp`](https://github.com/AaronGrace978/EduHelp) | 🟡 **AGPL-3.0** — root `LICENSE`, **34 523 B**, `main`, HEAD `2cceb0544ba9` | 69 files. IEP/504 **eligibility** aid for *families* under Colorado and California rules; BYOK across OpenAI / Anthropic / OpenRouter / Ollama. **The pass's only real grant.** Copyleft tier, not build-on |
| 🔴 **bbmcps** | [`anastasasenov/bbmcps`](https://github.com/anastasasenov/bbmcps) | 🔴 **NONE_IN_TREE** across **9 enumerated files** — 55 paths × 2 refs all 404 | 🔴 **Its `readme.md` line 84 says *"open-source and available under the MIT License."*** There is no MIT payload anywhere in the tree. **Dangling claim: an ASK, not a refusal.** See the channel reading below |
| 🔴 **BlackboardMCP** | [`yoyoconnor/BlackboardMCP`](https://github.com/yoyoconnor/BlackboardMCP) | 🔴 **NONE_IN_TREE** across 9 files; `pyproject.toml` has **no `license` key** | Read-only Blackboard Learn MCP server — courses, class times, assignments, grades, slide decks. *"It never submits, posts or changes anything."* Silent in **all three** channels |
| 🔴 **sped-agent** | [`hdronamraju/sped-agent`](https://github.com/hdronamraju/sped-agent) | 🔴 **ALL RIGHTS RESERVED** — README line 53; `package.json` has no `license` key and `"private": true` | 97 files. California IEP **deadline** agent. 🔴 This is a **REFUSAL, not an absence**: *"© 2026 hdronamraju. All rights reserved. … please ask before reusing the code."* 🔵 Its `src/agent/notices.ts` emits **bilingual EN/es** parent notices |
| 🔴 **ai-special-education-iep-compliance** | [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance) | 🔴 **NONE_IN_TREE** across 21 files | React + Node/Express + PostgreSQL. Evaluation timelines, service delivery, annual reviews, corrective action. No grant in any channel |
| 🔴 **agentic-automated-assignment-grading** | [`arijit8972/agentic-automated-assignment-grading`](https://github.com/arijit8972/agentic-automated-assignment-grading) | 🔴 **NONE_IN_TREE** — its **66** licence-like paths are **all vendored `ui/node_modules/**`** | **1 531 files**, because the repo **commits `node_modules`**. OCR + rubric-matching grading pipeline. `p280`'s class, at the largest scale this base has recorded |

🔵 **The count that matters to a studio: six new rows, one usable grant, and it is copyleft.**
Zero permissive. That is the finding of the pass, not a shortfall in searching — every leg is
written down with what it returned in
[`p288-websearch`](../evidence/p288-websearch.2026-10-18-p288.tsv).

### 🟢 Blackboard joins the MCP-addressable set, and it is the first one that is empty

`p267` established Moodle and Canvas as MCP-addressable; `p268` added Google Classroom
(eight servers probed, seven permissive, one all-rights-reserved wearing the same
description). This pass's directed leg adds **Blackboard Learn** — and the shape is new:

| LMS | established | community MCP servers | permissive among them |
|---|---|---|---|
| Moodle | `p267` | several | 🟢 yes |
| Canvas | `p267` | several | 🟢 yes |
| Google Classroom / Workspace for Education | `p268` | 8 probed | 🟢 7 of 8 |
| **Blackboard Learn** | **`p288`** | **2 new this pass + `nitsuah/bb-mcp` already carried** | 🔴 **none of the two new ones** |
| Open edX | carried (`blend-ed/openedx-mcp`) | 1 + Tutor plugin | 🟡 AGPL-3.0 |

🔴 **So the one LMS whose own product is proprietary is also the one whose community
integration layer carries no grant.** A Blackboard engagement cannot vendor either new
server; the pattern for it is written fresh in
[`compose/patterns.md`](../compose/patterns.md) `P41`.

### 🔴 The channel this base was not reading, and both new signals lived in it

`p278` grades a row on **two** channels — licence **payload** and package **manifest**. For
five of this pass's six rows both are empty, so `p278/sweep.sh` returned, five times:

```
NO-CHANNEL   GREY   "neither channel read — this row carries no grade"
```

🔴 **For two of those five a THIRD channel was readable and said something decisive, in
OPPOSITE directions** — `bbmcps` **claims** MIT it never serves; `sped-agent` **reserves all
rights**. One is an **ASK**, the other is a **STOP**, and `GREY` was the same wrong word for
both. 🟢 `ACTION p288` builds the channel
([`compose/code/p288-readme-channel/`](../compose/code/p288-readme-channel/README.md),
**32 controls, now in `make hooks`**) and grades the eight verdicts, with `posture()`
reporting **BUILD-ON / ASK / STOP**.

🔴 **And the lower-case rung is not decoration.** `bbmcps` serves **`readme.md`**; it answers
**404** at `README.md` on `main`, `master` *and* `HEAD`. **This pass's own first reading of it
was the false absence *"no README on any ref"***, corrected only because the tree was
enumerated and showed the real spelling — `p261`'s rule, which this base wrote down and then
needed again: *a 404 cannot distinguish a missing path from a missing channel; a tree can.*

🔵 **`T-p283`'s shape for the FOURTH time: the class reached one instrument and never reached
the one beside it.** `pass262-scoped-reservation-audit/sweep.py` has fetched the README over
five spellings — lower-case `readme.md` among them — since `p262`. But it runs **only** over
slugs the shelves *already* grade `RESTRICTIVE-GRADE`, so a **new** row can never reach it.
The reach existed in this codebase; the gate that grades new rows did not have it.

🟡 **Not every flagged ladder is a defect, and this pass checked rather than assumed.**
`p283`'s audit also flags the readme ladder in `p279-absence-claims` as `CASE-UNVARIED` — and
**that one is harmless**, because it opens *this KB's own* `README.md` at a known local path.
The audit measures the shape; whether the shape costs anything depends on whether the path is
remote. The claim published here is the one that was measured.

## 🟢 Pass 287 — a REAL MIT GRANT WAS BEING READ AS UNCLASSIFIABLE, and the repository that proves it also promotes itself onto the build-on tier

⏱️ **Ninth pass of `2026-10-18`.** Evidence:
[`verified-repos.2026-10-18-p287.tsv`](../evidence/verified-repos.2026-10-18-p287.tsv) ·
[`p287-websearch.2026-10-18-p287.tsv`](../evidence/p287-websearch.2026-10-18-p287.tsv) ·
[`restriction-vocabulary-multilingual.2026-10-18-p287.tsv`](../evidence/restriction-vocabulary-multilingual.2026-10-18-p287.tsv).

🔴 **Mandated agent leg: THIRTEENTH consecutive nil**, same population, same reason —
`microsoft/ai-agents-for-beginners`, `pguso/agents-from-scratch`,
`rohitg00/ai-engineering-from-scratch`. `p286` settled the posture and this pass confirms it:
**the battery is corroboration, the gap-directed leg is extension.** Four passes running,
every new row came from a directed leg.

### 🟢 The find of the pass, and it is a licence instrument that found it

| agent | address | grant (read from payload) | why it matters |
|---|---|---|---|
| 🟢 **TeachGPT** | [`Priyamakeshwari/TeachGPT`](https://github.com/Priyamakeshwari/TeachGPT) | 🟢 **MIT** — `LICENSE.md`, **1 057 B**, `main` | 18 files. **This base graded it `UNCLASSIFIED` and it was MIT all along** — see below. Build-on tier |
| 🟢 **mentar** | [`avps82/mentar`](https://github.com/avps82/mentar) | 🟡 **AGPL-3.0** — root `LICENSE`, **34 523 B**, `main`, HEAD `9d9d43c` | **839 files.** Local-first multi-curriculum tutor, deterministic answer checker. 🟢 **Ships its OWN dependency and content licence audit** — the first education repo here that does. Full reading in [`compose/patterns.md`](../compose/patterns.md) `P40` |
| 🟡 **Open-Education** | [`bunnywaffle/Open-Education`](https://github.com/bunnywaffle/Open-Education) | 🟢 **Apache-2.0** — `LICENSE`, **11 357 B** | 🔴 **Enumeration refutes its own README:** the tree is **THREE FILES** (`LICENSE`, `README.md`, `app.py`), HEAD `1fac5bc`. A one-file Gradio demo under a manifesto. Permissive and real; **not** the "platform" it calls itself |
| 🟡 **AIcademy** | [`aicademyorg/aicademy`](https://github.com/aicademyorg/aicademy) | 🟢 **MIT** — `LICENSE`, **1 063 B**, © 2025 AIcademy | 72 files, Next.js. 🔴 But it is the **teaching-engineers** class the mandated leg keeps returning — a site that teaches AI, not an agent that serves a learner. Recorded so nobody re-reads the list |
| 🟡 **ai_tutor_forge** | [`guedesindev/ai_tutor_forge`](https://github.com/guedesindev/ai_tutor_forge) | 🟡 **GPL-3.0** — `LICENSE`, **35 149 B**, HEAD `d503ac7` | 🇧🇷 pt-BR, 7 files. The pass's **only LATAM-origin code row**. Small, and ships a committed `__pycache__` `.pyc` |
| 🔴 **AIProf** | [`MeetYourAI/AIProf`](https://github.com/MeetYourAI/AIProf) | 🔴 **GPL-3.0** — `LICENSE`, **35 149 B**, on ref **`dev`** | 🔴 **ITS README SAYS `This project is [MIT](./LICENSE) licensed.`** The payload at that exact path is verbatim GPL-3.0. See the channel-conflict row below |
| 🔴 **PrepifyAI** | [`saif2012004/PrepifyAI`](https://github.com/saif2012004/PrepifyAI) | 🔴 **NONE_IN_TREE** across **389 enumerated files** | 🇵🇰 FBISE Matric/FSc + MDCAT/ECAT RAG tutor, DistilBERT topic predictor. No payload, no README licence line, `package.json` has **no `license` key** and `"private": true` |
| 🔴 **gurukul-ai** | [`somenssarkar/gurukul-ai`](https://github.com/somenssarkar/gurukul-ai) | 🔴 **NONE_IN_TREE** across 17 files | 🇮🇳 NCERT/CBSE grade 7–8, shipped as **five `SKILL.md` packs** (maths, physics, chemistry/biology, sanskrit, english) — **a form factor new to this base**. README says *"MIT License — use freely"*. **Dangling claim: an ASK, not a refusal** |

### 🔴 The instrument defect that was costing this base usable dependencies

🟢 **`Priyamakeshwari/TeachGPT` is a verbatim MIT body whose TITLE LINE IS SIMPLY ABSENT.**
It opens on the bare copyright line and goes straight to *"Permission is hereby granted,
free of charge…"*. `pass257-restriction-scan`'s stage-two anchors covered **BSD and ISC** —
the two families that routinely open on a copyright line — **and not MIT**, the family this
base publishes more than any other. So it graded `UNCLASSIFIED:no-family-no-restriction`.

🔵 **This is `T-p283`'s shape for the third time, and the second time in that one function:**
`p1054` has carried a `MIT_BODY_MARKER` since it was written, so the base already knew an MIT
body is identifiable without its title. **The class reached one instrument and never reached
the one beside it.**

🟡 **The direction was the conservative one** — `UNCLASSIFIED` is never published as
permissive, so it cost no wrong licence claim. 🔴 **It cost the other thing, and this base has
not been counting it: a real, usable, permissive grant read as unclassifiable is a dependency
the studio declines for no reason.** Both directions are defects. Collision was measured on
all seven fixtures before the anchor was added (the MIT clause occurs in **one** of them — the
MIT one — and **not** in `rapkumer`, which carries an MIT carve-out in its §6), and pinned in
the suite.

### 🔴 A channel conflict in the dangerous direction, and the ref trap again

`MeetYourAI/AIProf`'s README says **MIT** and links `./LICENSE`; that file is **verbatim
GPL-3.0** (35 149 B, *"Version 3, 29 June 2007"*). 🔵 Every prior channel conflict this base
has recorded ran *payload more restrictive than the list* — this one runs **README more
permissive than its own linked payload**, which is the same error with the reader on the wrong
side of it. 🔴 **And the grant sits on default ref `dev`** — not `main`, not `master`. That is
the third pass in four where the ref axis, not the filename ladder, decided the verdict
(`eledia` on `master`, `twiga` on `development`, `AIProf` on `dev`).

### 🟢 South Asia reproduces West Africa's shape, and that makes the claim a pattern rather than a region

🔴 **Pakistan and India returned three code rows and two of the three serve no grant**
(`PrepifyAI` 389 files, `gurukul-ai` 17 files) — against **one** that does, and it is AGPL
(`mentar`). `T-p285a` was stated over West Africa: *the gap is LICENSING, not supply.* 🟢 **It
now has an independent second confirmation 6 000 km away**, and `T-p286a`'s counterexample
(East Africa, permissive) holds on both: the posture is **not continental and not regional —
it is per-project**, and the only thing that settles it is the payload.

🔴 **`PrepifyAI` carries a SECOND grant problem the code-licence question cannot see:** 20
`Extracted text books/` JSON files for `FBISE_CLASS9/10` and `PUNJAB_CLASS9/10`. Board
textbook text is third-party copyright, so even a written code grant would not clear it. This
is the `P26`/content-licence seam, and it is the first education repo here where the content
problem is **larger** than the code problem.

## 🟢 Pass 286 — "FIVE AFRICAN ROWS, FIVE UNLICENSED" IS REFUTED AT THE PAYLOAD, AND THE REPO THAT REFUTES IT IS PRODUCTION-SHAPED

⏱️ `2026-10-18`, eighth pass. Evidence:
[`regional-intake.2026-10-18-p286.tsv`](../evidence/regional-intake.2026-10-18-p286.tsv) ·
[`p286-websearch.2026-10-18-p286.tsv`](../evidence/p286-websearch.2026-10-18-p286.tsv).

🔴 **The mandated agent leg returned its TWELFTH consecutive nil** — `microsoft/ai-agents-for-beginners`,
`pguso/agents-from-scratch`, `rohitg00/ai-engineering-from-scratch`: curricula that teach engineers
to build agents. `p283`'s diagnosis reproduces for the fourth pass running. 🟢 **All three rows
below came from gap-directed legs** — the third consecutive pass where that is true.

🔴 **The claim this pass overturns is this shelf's own, published two passes ago:** *"Five African
education code rows are now known to this base and **all five are unlicensed**. The gap is not code
— it is LICENSING."* 🟢 **It was a WEST AFRICAN sample generalised to a continent.** `p285`'s own
leg recorded that it *"found nothing for East Africa"*; a leg addressed to **Tanzania by its exam
board and its language** returned **two MIT repositories on the first attempt**.

| agent | licence (payload-read `2026-10-18`, first-hand) | tier | note |
|---|---|---|---|
| [`Tanzania-AI-Community/twiga`](https://github.com/Tanzania-AI-Community/twiga) | 🟢 **MIT** — `development/LICENSE`, 1 073 B, holder *Victor Oldensand* | 🟢 **build-on** | 🇹🇿 WhatsApp assistant for **Tanzanian teachers**, RAG over **Tanzania Institute of Education** curriculum and textbooks. **230 files**: `app/` (101), **30 tests**, 12 migrations, 15 docs, `monitoring/`, `docker/`, CI. 🔴 **This closes the gap `p284` and `p285` both declared open** — *"no production open-source education agent built for an African deployment"*. It is the first row here that is African-deployment-targeted, permissive AND production-shaped |
| [`vincent-laizer/NECTA-API`](https://github.com/vincent-laizer/NECTA-API) | 🟢 **MIT** — root `LICENSE`, 1 092 B | 🟢 **build-on (data channel)** | 🇹🇿 Python package that fetches **NECTA** national examination results. Not an agent: it is the **results channel** a Tanzanian engagement needs underneath one. Author states it is **not an official NECTA API** and is still in development — treat the upstream as unstable, the licence as clean |
| [`Jahirrrr/sekolahyuk-app`](https://github.com/Jahirrrr/sekolahyuk-app) | 🟢 **MIT** — root `LICENSE`, 1 064 B | 🟢 **build-on** | 🇮🇩 *"Aplikasi pembelajaran Sekolah Gratis dan Open Source"* — free, open-source school learning app. The **only permissive grant in seven Indonesian addresses probed** this pass |

🔴 **The grant that the default ref hid, again.** `twiga`'s grant is on **`development`**, not `main`
or `master`. A probe trying the two conventional refs would have published `NONE_IN_TREE` on an
MIT repository. 🔵 **That is `p285`'s `eledia` finding — a grant sitting on a ref the axis never
tried — reproduced in a different hemisphere one pass later**, and it is now **two of this base's
last five promotions**. `ls-remote --symref` costs one call and is the only thing that prevents it.

### 🔴 Three "open source" claims from secondary sources, all three refuted by the payload

| address | what the source said | 🔴 what the payload says |
|---|---|---|
| [`gabrielmahia/shule-ai`](https://github.com/gabrielmahia/shule-ai) | GitHub Topics lists it as **open-source**: 🇰🇪 Kenyan-curriculum tutor, KCSE/CBC, Kiswahili + English, *"runs on any phone"* | 🔴 **CC BY-NC-ND 4.0** — 209 B, **reference-only** (a URL to the legalcode, no body). **NonCommercial AND NoDerivatives**: a studio may neither bill for it nor modify it. The single most restrictive grant on this shelf |
| [`eldorray/modulajar-ai`](https://github.com/eldorray/modulajar-ai) | search result: *"released under the **MIT** license"* | 🔴 **NONE_IN_TREE across 310 enumerated files.** There is no grant to be MIT |
| [`Dondo0936/vietnamese-ai-for-beginner`](https://github.com/Dondo0936/vietnamese-ai-for-beginner) | search result: *"under the **MIT** license"*, 260+ topics | 🔴 **DOES_NOT_RESOLVE.** The address does not serve a ref at all |

🔵 **Three secondary licence claims, three refutations, one pass.** This base's standing rule —
**read the grant, never the list** — now has a measured hit rate in the direction that matters: of
**five** addresses a secondary source called MIT or open-source this pass, **three were wrong**.

### 🟡 Two verified grants a studio cannot build on, recorded so nobody re-reads the list

- 🔴 [`sira313/rapkumer`](https://github.com/sira313/rapkumer) (🇮🇩 Kurikulum-Merdeka report-card
  app, an alternative to the official **e-Rapor**, with an AI generator for learning objectives) —
  **bespoke `RAPKUMER LICENSE`, 3 140 B, in Indonesian.** §3 *`LARANGAN PENGGUNAAN KOMERSIAL`*
  prohibits commercial use **in any form**, naming paid access, paid support-as-product and
  inclusion in a commercial service. §5 splits scope — the grant covers the source and **five
  named static assets**, everything else in `static/` follows its own holder — and §6 carves out
  Feather Icons as MIT. 🔵 A sophisticated, scope-partitioned proprietary licence that is **not in
  English**, which is what makes it this pass's instrument finding (see
  [`intel/trends.md`](../intel/trends.md) `T-p286b`).
- 🟡 [`longnhgsvn/Learn-with-AI-tieng-viet`](https://github.com/longnhgsvn/Learn-with-AI-tieng-viet)
  (🇻🇳 WordPress + AI platform, large course catalogue) — **AGPL-3.0, 35 149 B.** Integrate across a
  network boundary or not at all.

### 🟢 Four Vietnamese and Indonesian addresses enumerated to a clean absence

[`DooWuy/AI-tutor-`](https://github.com/DooWuy/AI-tutor-) (735 files),
[`SeNgoNhatMinh/Ai_Turtor`](https://github.com/SeNgoNhatMinh/Ai_Turtor) (1 640 files),
[`nguyenbaophuc27129-web/VIETPOET`](https://github.com/nguyenbaophuc27129-web/VIETPOET) (198 files —
🔵 a **Socratic** poetry tutor for Vietnamese high-school literature that runs **offline on CPU** on
a compressed Qwen2.5-1.5B, which is the most interesting *design* found this pass),
[`thanh01pmt/vietnam-k12-ai-curriculum`](https://github.com/thanh01pmt/vietnam-k12-ai-curriculum)
(15 files), plus 🇮🇩 `faruqeclypst/modulajar-generator` (79), `indri007/eduragmerdeka` (16),
`aisyahrr/siakad-kurikulum-merdeka` (126), `odifunan4-ux/Guruku-ID` (14) and 🇹🇿
`Colin-J-Emmanuel/Somo` (23 — a NECTA CSEE photo-tutor built in one day at a hackathon).
**All nine tree-enumerated, all `VERIFIED_ABSENT`.** Prior art, not dependencies — and under
`P32`/`P35` the right move is to **ask**, which nobody in this base's history has done.

## 🟢 Pass 285 — two agents promoted out of the ENUMERATION BACKLOG, and a seven-plugin EMEA suite that was on this base's "not on GitHub" list

⏱️ `2026-10-18`, seventh pass. Evidence:
[`tree-enumeration.2026-10-18-p285.tsv`](../evidence/tree-enumeration.2026-10-18-p285.tsv) ·
[`egress-surface.2026-10-18-p285.tsv`](../evidence/egress-surface.2026-10-18-p285.tsv).

🔴 **The mandated agent leg returned its eleventh consecutive nil.** Both agents added this pass
came from **gap-directed** legs and from **working the backlog**, not from the battery — the second
consecutive pass where that is true.

| agent | licence (payload-read `2026-10-18`) | tier | note |
|---|---|---|---|
| [`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) | 🟢 **MIT** — root `LICENSE`, 1 068 B | 🟢 **build-on** | Carried `NO GRANT` / *"unshippable"* since `p153`. The verdict rested on a **path ladder**; the tree holds 451 files and the grant is at the **root**. **Now shippable** |
| [`eledia/moodle-elediaai-suite-free`](https://github.com/eledia/moodle-elediaai-suite-free) | 🔴 **GPL-3.0-or-later** — root `LICENSE` 35 149 B + a per-plugin grant in each of 7 plugins | **integrate across a boundary** | eLeDia GmbH, Berlin. **880 files.** The in-course tutor, chat engine, 17 content extractors, a **local RAG** backend, **AI-transparency marking** and an **MCP connector**. Full table in [`verticals/solutions.md`](../verticals/solutions.md) |
| [`eledia/moodle-block_elediaai_tutor`](https://github.com/eledia/moodle-block_elediaai_tutor) | 🔴 **GPL-3.0-or-later** — `master/public/blocks/eledia_aitutor/LICENSE`, 1 254 B | **archived — use the suite above** | This base published *"no grant body"*. 🔵 Its `51`-default-branch finding was **right**; the grant sits on **`master`**, a ref the axis never tried |

🔴 **Africa — three new code rows, none of them usable.** [`Angel-builds/edubot-africa`](https://github.com/Angel-builds/edubot-africa)
(🇬🇭 NaCCA JHS maths, SymPy-routed arithmetic, CI-gated retrieval),
[`Onyeocha-Keside/naija-learn`](https://github.com/Onyeocha-Keside/naija-learn) (🇳🇬 voice-first
Yoruba/Hausa/Igbo) and [`meduoyeomoyenia-cyber/Education-AI-TUTOR`](https://github.com/meduoyeomoyenia-cyber/Education-AI-TUTOR)
(🇳🇬 WAEC/NECO/JAMB) were all **tree-enumerated** and all serve **NONE_IN_TREE** with **no manifest
licence key**. 🟢 **Five African education code rows are now known to this base and all five are
unlicensed. The gap is not code — it is LICENSING.** Treat as **prior art, not dependencies**.
> 🔴 **WITHDRAWN IN PLACE by pass 286.** The three rows above are 🇬🇭/🇳🇬 and the verdict on each
> still stands, but *"all five are unlicensed"* generalised a **West African** sample to the
> continent. An **East African** leg found [`Tanzania-AI-Community/twiga`](https://github.com/Tanzania-AI-Community/twiga)
> (**MIT**) and [`vincent-laizer/NECTA-API`](https://github.com/vincent-laizer/NECTA-API)
> (**MIT**) on its first attempt. The licensing gap is **West African**, not African.

## Build-on-this tier — permissive licences (MIT / Apache-2.0 / BSD)

These are the rows a studio engagement can start from without copyleft or
non-commercial friction.

| Agent | Repo | Licence | Stars | What it does |
|-------|------|---------|-------|--------------|
| 🆕 **algo-sensei** | [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | 🟢 **MIT** *(**payload** `LICENSE`, 1 081 B, sha256₁₂ `3b2ca73e81ad`, read `p302`)* | 🟡 **293★ / 63 forks / 9 commits / `main`** | 🟢 **A Claude Code skill whose real asset is a WITHHOLDING POLICY.** LeetCode/DSA mentor with five modes (Tutor, Hint, Review, Interview, Pattern Mapper) and a **five-level progressive hint cascade**: gentle observation → pattern nudge → approach direction → technique reveal → pseudocode skeleton **as a last resort**. README premise: *"Copy-pasting solutions doesn't build problem-solving skills."* Runs as a skill (`SKILL.md` → `~/.claude/skills/`) or pasted into a Claude.ai Project. 🔵 **Lift the cascade, not the repo** — graduated withholding is what every tutoring engagement must build and almost nothing ships. ⚠️ **9 commits; Languages panel empty, so the implementation was not read.** |
| 🆕 **feifei-companion** (飞飞学伴) | [SimonsTang/feifei-companion](https://github.com/SimonsTang/feifei-companion) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 10 227 B, sha256₁₂ `59a378bf23a0`, read `p302`)* | 🟡 **108★ / 9 forks / 10 commits / `main`** | 🟢 **THE ONLY ROW ON THIS SHELF THAT IS CURRICULUM-ALIGNED AND SHIPS A PARENT CHANNEL.** K-12 "Trinity": coordinator + liberal-arts + STEM personas. **"心跳任务" (heartbeat tasks)** — proactive loop that wakes the learner, assigns, verifies completion, cycles. Alignment is named, not implied: **统编版 Chinese grades 1-12**, **人教版 English grades 3-12**, **人教版/北师大版 STEM grades 7-12**. Parent side: parent-child translation, 21-day habit plan with check-ins, and a report covering mastery / concerns / weekly highlights / next-week plan. ⚠️ **It is a SKILL, not a service** — requires an OpenClaw / Claude Code / Cursor / Codex host, plus a Tencent Cloud key for dialogue. Its own README: **"不能替代"** professional teachers or counsellors. 🔵 **Copy the heartbeat + parent-report pair for K-12 anywhere**; the textbooks are swappable, the shape is the finding. |
| 🆕 **feedbacksystem** | [thm-mni-ii/feedbacksystem](https://github.com/thm-mni-ii/feedbacksystem) | 🟢 **Apache-2.0** *(**payload** `LICENSE`, 10 785 B, sha256₁₂ `65125d9e480b`, holder **© 2023 Technischen Hochschule Mittelhessen**, read `p302`)* | 🟡 **24★ / 9 forks / branch `dev`** | 🟢 **AN INSTITUTION-HELD GRADING/FEEDBACK SERVICE — a different risk class from a personal repo.** *"Intelligent, personalized feedback for students using artificial intelligence."* Automatically checks submissions and returns an **immediate** result, proposes fixes for mistakes, and **aggregates common mistakes so the lecturer can address them in class** — the loop back to teaching is the part that earns the row. Ships **Helm charts + Kubernetes** production install. ⚠️ **The AI mechanism is undocumented on the page**; Languages panel empty; the visible demo is an **SQL checker**; production use at THM is implied by a Helm chart and `frits.mni.thm.de`, **not stated**. Read the code before promising any subject beyond SQL. |
| 🆕 **conv-vs-ped-tutor** | [bydeng01/conv-vs-ped-tutor](https://github.com/bydeng01/conv-vs-ped-tutor) | 🟢 **MIT** *(**payload** `LICENSE`, 1 150 B, sha256₁₂ `a1c6b65c5bb1`, read `p302`)* | 🔴 **3★ / 0 forks / `main`** | 🟢 **THE EVALUATION ARTEFACT THE REGULATORY MOMENT ACTUALLY REQUIRES (arXiv:2607.28128).** Pre-registered audit of whether an LLM helpfulness judge *"rewards the answer-leakage that reduces the student's later independent work."* **One frozen base model, two policies:** `ConvTutor` (single-node LangGraph) vs `PedTutor` (state tracker + decomposer + **deferral gate** + hint cascade), against a cold baseline, with a weak simulated student (**Llama-3.1-8B**), Opus as primary judge and a second judge for robustness. Ships a **frozen answer-leakage matcher** (`protocol/leakage.py`) and **ablations** removing tracker / gate / cascade individually. Design: **10 replicates × {cold, conv, ped}** per base; GPT and Gemini bases run separately and **never pooled**. 🔵 **This is how you produce evidence rather than assurances for Vietnam's and Korea's automated-assessment duties.** ⚠️ **NO RESULTS ON THE PAGE** — tables are recomputed by command, hypotheses live in an unread `paper-plan.md`. **Cite the design, never an effect size.** |
| 🆕 **ability-levels-audit** | [bydeng01/ability-levels-audit](https://github.com/bydeng01/ability-levels-audit) | 🟢 **MIT** *(**payload** `LICENSE`, 1 154 B, sha256₁₂ `fef00f185287`, read `p302`)* | 🔴 **4★ / branch `master`** | 🟡 **Companion audit to the row above: pre-registered study of LLM judges with analysis of BOUNDED-RATING BIAS across ability levels.** Matters because every adaptive-tutoring pitch assumes a judge can score a weak learner and a strong learner on the same scale — this measures whether it can. ⚠️ **4★, results not stated on the page, default branch is `master` not `main`** (a pin written against `main` will 404). |
| 🆕 **claudemy** | [assafkip/claudemy](https://github.com/assafkip/claudemy) | 🟢 **MIT** *(**payload** `LICENSE`, 1 069 B, sha256₁₂ `262b47ee1fff`, holder **Assaf Kipnis**, read `p302`)* | 🟡 **309★** | Course generator that turns a topic into **cited audio lessons** — citation-carrying output in a modality this shelf had no row for. ⚠️ **Stars as rendered; internals unread this pass.** |
| 🆕 **AILearningGuide** | [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) | 🟢 **MIT** *(**payload** `LICENSE`, 1 081 B, sha256₁₂ `e29ef713b542`, holder **Discover AI contributors**, read `p302`)* | 🟡 **202★** | 🟢 **OFFLINE desktop app with 51 interactive ML labs** — relevant wherever egress or connectivity is the constraint (ministries, rural deployments). ⚠️ **Teaches AI; it is not an agent.** Internals unread. |
| 🆕 **kaogong-skill** | [KeWang0622/kaogong-skill](https://github.com/KeWang0622/kaogong-skill) | 🟢 **MIT** *(**payload** `LICENSE`, 1 083 B, sha256₁₂ `a6943096ffde`, read `p302`)* | 🟡 **186★** | Exam-prep skill for **Chinese civil-service and public-institution exams**, including wrong-answer review. 🔵 **A high-stakes-exam vertical with a permissive grant** — the closest analogue on this shelf to a national licensing-exam engagement. ⚠️ Internals unread. |
| 🆕 **InterviewMentor** | [PrepLabsAI/InterviewMentor](https://github.com/PrepLabsAI/InterviewMentor) | 🟢 **MIT** *(**payload** `LICENSE`, 1 071 B, sha256₁₂ `aeb634f7110b`, read `p302`)* | 🟡 **112★** | AI mock interviews for technical job preparation — the employability end of the funnel, which pairs with the credentialing rows on [`repos/foundations.md`](../repos/foundations.md). ⚠️ Internals unread. |
| 🆕 **Studivexa** | [codeXsidd/Studivexa](https://github.com/codeXsidd/Studivexa) | 🟢 **MIT** *(**payload** `LICENSE`, 1 068 B, sha256₁₂ `58f77360830f`, read `p302`)* | 🟡 **72★** | Student productivity workspace with gamified learning and focus rooms. 🔵 On the shelf for the **engagement/retention** layer, not for instruction. ⚠️ Internals unread. |
| 🆕 **Tov-learn** | [TovTechOrg/Tov-learn](https://github.com/TovTechOrg/Tov-learn) | 🟢 **MIT** *(**payload** `LICENSE`, 1 064 B, sha256₁₂ `092d389ac156`, holder **TovTech**, read `p302`)* | 🔴 **36★** | Claude Code skill that teaches with **spaced repetition** and a progress dashboard. 🔵 Pairs directly with [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) and the FSRS rows — spaced repetition as a *skill* rather than as an app. ⚠️ **36★**, internals unread. |
| 🆕 **eklavya** | [ProjectAJ14/eklavya](https://github.com/ProjectAJ14/eklavya) | 🟢 **MIT** *(**payload** `LICENSE`, 1 067 B, sha256₁₂ `b64948dd9b05`, read `p302`)* | 🔴 **10★ / TypeScript** | 🟢 **Inverts the usual direction: a Claude Code plugin that QUIZZES THE DEVELOPER on the concepts behind code the AGENT just wrote**, against a local knowledge graph. 🔵 **The only row on this shelf aimed at the de-skilling problem** — directly relevant to internal enablement and to any client worried that agent adoption hollows out their team. ⚠️ **10★, early.** |
| 🆕 **khayyam-math** | [khayyam-math/khayyam-math](https://github.com/khayyam-math/khayyam-math) | 🟢 **MIT** *(**payload** `LICENSE`, 1 079 B, sha256₁₂ `4068e5e09efd`, read `p302`)* | 🔴 **4★** | Generates **voice-narrated math figures** from short prompts, with a live tutor. 🔵 On the shelf as the permissive counterpart to `ChatTutor`'s AGPL whiteboard — visual/auditory math explanation with a grant Globant can use. ⚠️ **4★, prototype scale.** |
| 🆕 **BloodCoded_Agentic** | [sohan1611/BloodCoded_Agentic](https://github.com/sohan1611/BloodCoded_Agentic) | 🟢 **MIT** *(**payload** `LICENSE`, 1 104 B, sha256₁₂ `4b15a1e898b3`, read `p302`)* | 🔴 **2★** | Tutoring agent that **re-targets its goal from a diagnosed failure**, built on **LangGraph + Bayesian Knowledge Tracing** — the classic BKT lineage (`CAHLR/OATutor`, `pykt-team/pykt-toolkit`) wired into a modern agent graph. 🔵 **On the shelf as a SHAPE**: it is the smallest demonstration of BKT-as-agent-state. ⚠️ **2★. Copy the pattern; do not depend on it.** |
| 🔴 **Mr.-Ranedeer-AI-Tutor** — **REFUSED, NO GRANT** | [JushBJJ/Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | 🔴 **NONE** *(404 on `LICENSE`/`LICENSE.md`/`LICENSE.txt`/`COPYING` × `main`+`master`; sidebar Resources lists only Readme and Activity — read `p302`)* | 🔴 **29.6k★ / 3.3k forks** | 🔴 **THE MOST REACHABLE TRAP IN THIS INDUSTRY, AND IT IS ON THIS TABLE SO IT IS NEVER PICKED UP BY ACCIDENT.** By stars the second-most-adopted education-specific tutoring artefact on GitHub, a GPT-4 tutor prompt for "customizable personalized learning experiences" — with **no licence of any kind**, and a README whose **first heading is `DISCONTINUED`**. 🔴 **No grant means no permission** — absent, not permissive-by-default. **3.3k forks of something nobody has the right to use**, and being discontinued, there is no maintainer to ask. ⚠️ **Brief it as the cautionary row whenever a client cites star counts.** |
| 🔴 **ChatTutor** — **REFUSED, COPYLEFT** | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | 🔴 **AGPL-3.0** *(**payload** `LICENSE`, 34 522 B, sha256₁₂ `20b067f86de3`, read `p302`)* | 🟡 **1.3k★ / 189 forks / 193 commits** | 🔴 **The highest-starred MAINTAINED education tutor after DeepTutor — and unusable inside a client's proprietary platform.** *"ChatTutor is an AI teacher equipped with the ability to use an electronic whiteboard"*: Math Canvas, Mermaid mindmaps, **GeoGebra**, Vue + Vite + ElysiaJS, self-hostable via `docker compose`, PostgreSQL, pluggable across OpenAI / Anthropic / DeepSeek, hosted option at `chattutor.app` on the user's own key. 🔴 **AGPL reaches NETWORK use**, so hosting it for a client triggers the obligation. 🔵 **Cite it as the capability reference for visual tutoring — the thing to study, not to ship** — and build the equivalent on `khayyam-math` (MIT) if the client needs to own it. |
| 🆕 **moodle-mcp** *(falkenslab — **a DIFFERENT repository** from `MarcosNahuel/moodle-mcp` and `Jawadh-Salih/moodle-mcp-server`)* | [falkenslab/moodle-mcp](https://github.com/falkenslab/moodle-mcp) | 🟢 **MIT** *(**payload** `LICENSE`, 1 067 B, sha256₁₂ `66fa873bd85d`, holder **Falkenslab**, read `p301`)* | 🔴 **1★ / 1 fork / 166 commits / `main`** | 🟢 **THE MOODLE ROW THAT NEEDS NO ADMINISTRATOR — and that is the whole finding.** *"MCP server for agents to work in Moodle"*: **~230 tools** covering courses, activities, enrolment, and **"submissions, rubrics and marking guides (read and defined)"**. 🟢 **Its README: *"No web service tokens, no administrator, no plugin: if you can log in, it works."*** Authentication is a browser login. 🔵 **Why that matters more than the tool count:** every other Moodle path on this shelf needs a web-services token, a site admin or a plugin install — the step that converts a two-week pilot into a two-quarter procurement. A teacher with an ordinary account can run this one, and the **rubric is an input rather than a reimplementation**. ⚠️ **Boundaries, stated:** **1★ / 1 fork — nobody has adopted it**; 166 commits means worked-on, not proven; the rendered page's Languages panel is **empty**, so the implementation language was **not read**. 🔴 **And the property that makes it easy makes it dangerous: a browser-session agent acts with the TEACHER'S OWN credentials — no token to scope, no admin to audit.** Brief it as the fastest route to a **pilot**, never as the route to production without a service account. |
| 🆕 **canvas-lms-mcp** *(chiptoe-svg — 🔴 **a DIVERGED FORK** of `bruchris/canvas-lms-mcp`, already carried)* | [chiptoe-svg/canvas-lms-mcp](https://github.com/chiptoe-svg/canvas-lms-mcp) | 🟢 **MIT** *(**payload** `LICENSE`, 1 070 B, sha256₁₂ `c29329c5ef3b`, holder **Christian Bru**, read `p301`)* — 🔴 **BYTE-IDENTICAL to the upstream row's payload: a fork INHERITS the grant** | 🔴 **0★ / 0 forks / 287 commits / `main`** | 🟡 **Canvas LMS MCP with the read/write boundary WRITTEN DOWN — the only row on this shelf that states it.** **165 registered tools: 117 read-only, 48 write**, over courses, assignments, submissions, rubrics and quizzes; grading and commenting from any MCP client. 🟢 **Plus a FERPA mode** that registers one additional tool (`resolve_pseudonym`, 166 total) — the first US-compliance affordance this shelf has seen in an LMS agent, and directly relevant to a **North America** engagement. 🔴 **Identity, settled at `p301`:** the page says *"forked from bruchris/canvas-lms-mcp"* and the licence payloads are byte-identical, but the HEADs differ (`fa8408a6…` vs `18fa06b5…`), so by `p283`'s rule — *equal HEAD == one repository* — these are **two repositories** and this row stands. ⚠️ **Cite it as a fork.** **0★ / 0 forks** against **287 commits**: the fork is *more* committed-to than adopted, the README is still the upstream's text, and **what it changes relative to upstream is undocumented and UNREAD**. Diff it against `bruchris` before building on it. |
| 🆕 **gradescope-mcp** *(YeetingWaterbottle — **a DIFFERENT repository** from `Yuanpeng-Li/gradescope-mcp`, already carried)* | [YeetingWaterbottle/gradescope-mcp](https://github.com/YeetingWaterbottle/gradescope-mcp) | 🟢 **MIT** *(**payload** `LICENSE`, 1 089 B, sha256₁₂ `02f326c5fca4`, read `p301`)* | 🔴 **3★ / 1 fork / 2 commits / `main`** | 🔵 **On this shelf as a SHAPE, not as a dependency — the only education agent here that is read-only BY DESIGN and says so.** 6 tools: `gradescope_list_courses`, `gradescope_list_assignments`, `gradescope_upcoming_assignments`, `gradescope_list_submissions`, `gradescope_get_submission_files`, `gradescope_download_submission_file`. Its README states it *"does not expose Gradescope write operations"* and explicitly excludes grading, roster management, extension management and submission upload; the single local write saves a downloaded file and **refuses to overwrite by default**. 🟢 **Why it earns a row at 2 commits:** the hard part of putting an agent near a gradebook is not reach, it is **proving the agent cannot change a grade**. This is the smallest artefact that demonstrates the read-only tier a studio should deploy first — compare `chiptoe-svg`'s 117-read / 48-write split, which is the same idea with the writes present. 🔴 **TWO COMMITS. Do not depend on it; copy the boundary.** |
| 🆕 **DCC Credential Co-writer** | [oneorigin-2-0/dcc-credential-co-writer-monorep](https://github.com/oneorigin-2-0/dcc-credential-co-writer-monorep) | 🟢 **MIT** *(**payload** `LICENSE`, 1 087 B, sha256₁₂ `7f62d1bf385d`, holder **Digital Credentials Consortium**, read `p300`)* | 🔴 **0★ / 1 fork / 440 commits / `main`** | 🟢 **THE FIRST NEW ROW ON THIS SHELF IN 27 WINDOWS — and it came from the promotion backlog, not from any search leg.** *"AI-assisted Open Badges v3 authoring"*: paste or upload course content and it drafts the credential's **title, description, criteria and skills**, then renders the badge image. Three services in one monorepo — a **Next.js 15** UI, a **FastAPI + Ollama** service running a **fine-tuned `phi-4-mini`** SLM for badge metadata, and a **FastAPI + Pillow** image service. **23 languages**, streaming output, **human-in-the-loop editor.** 🟢 **Why it matters beyond the row: it is a SELF-HOSTABLE education agent** — the model runs under Ollama, so a ministry or registrar with no egress can run the whole pipeline — **and it terminates in a STANDARD (OBv3) rather than in free text**, which is what makes its output checkable by [`credential-lens`](https://github.com/TanimowoObaloluwaDavid/credential-lens) and [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) on [`repos/foundations.md`](../repos/foundations.md). 🔵 Developed through a collaboration **led by the DCC** and funded by **Walmart**; the copyright is the DCC's, though the repository sits under a vendor org (**OneOrigin**). ⚠️ **Boundaries, stated:** **0 stars and 1 fork — nobody has adopted this yet**; its README says the three services were previously standalone repositories under a `digitalcredentials` org, so the consolidation is recent and the predecessors are **unread**; and the page nowhere claims this is an official DCC release. Brief it as the strongest available reference for AI-assisted credential authoring, **not** as a maintained product. |
| TeachGPT | [Priyamakeshwari/TeachGPT](https://github.com/Priyamakeshwari/TeachGPT) | MIT *(payload, p287)* | — | **New row at `p287`, and it is a row this base ALREADY HELD and could not read.** `LICENSE.md`, **1 057 B** on `main`, 18 files: a **verbatim MIT body with its title line absent**, which `pass257-restriction-scan` graded `UNCLASSIFIED` until this pass taught stage two the MIT operative clause. Small and unproven as software; **the value here is the measurement** — it is the first demonstration that this base's licence instruments were costing it usable permissive dependencies, not just failing to catch restricted ones. |
| Open-Education | [bunnywaffle/Open-Education](https://github.com/bunnywaffle/Open-Education) | Apache-2.0 *(payload, p287)* | — | ⚠️ **Listed with its size stated, because the README does not state it.** `LICENSE` **11 357 B**, HEAD `1fac5bc` — and the tree is **THREE FILES**: `LICENSE`, `README.md`, `app.py`. A single-file Gradio tutor demo beneath a long manifesto about replacing human teachers. **The grant is real and permissive; the "platform" is not a platform.** Useful as a 200-line reading of the smallest thing that answers a learner, and **not** as a dependency. |
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | 41.6k *(rendered, p294)* | Lifelong personalized tutoring: a persistent student model that survives between sessions, multi-agent orchestration, citation-grounded feedback. Release v1.6.14 dated 2026.10.8. The single most adopted education agent on GitHub. |
| Artemis | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | Platform for interactive learning with individual feedback, from the Applied Education Technologies group at **TU Munich**; 12,437 commits, self-hosted by universities in several countries. Ships three config-gated AI subsystems: **Iris** (LLM tutor), **Athena** (feedback suggestion for text/modelling/programming) and **Hyperion** (AI exercise authoring on Spring AI). Programming submissions are built, tested and analysed automatically. The answer to "where is the open grading agent" — it is inside a platform. |
| ~~Iris~~ → **not a separate repository** | [ls1intum/Iris](https://github.com/ls1intum/Iris) **= [ls1intum/Pyris](https://github.com/ls1intum/Pyris)** | MIT *(the same payload as Pyris, counted twice until now)* | — | 🔴 **`p282`: WITHDRAWN AS A ROW — this address is a GitHub name alias that resolves to `ls1intum/Pyris`.** Identical HEAD (`d7b2c095204e`), identical ref count (245), identical root tree (`4e2f096df767`), 203 files, identical 1 088-byte MIT payload; under **both** names the root `README.MD` opens `# Pyris V2`. **Iris is the user-facing name of the tutor Pyris powers inside Artemis** — the project's own README points at a web page (`artemis.cit.tum.de/about-iris`), not at a repository. The capability is real; the **second address is not**. Build on **Pyris**. Evidence: [`alias-identity.2026-10-18-p282.tsv`](../evidence/alias-identity.2026-10-18-p282.tsv). |
| Pyris | [ls1intum/Pyris](https://github.com/ls1intum/Pyris) | MIT | 12 | The LLM microservice behind Iris: a REST API fronting swappable LLM pipelines, with exercise feedback, RAG over instructor-supplied course material, and automated competency generation. The reusable piece — it will serve a stack that is not Artemis. |
| Instructional Agents | [DaRL-GenAI/instructional_agents](https://github.com/DaRL-GenAI/instructional_agents) | MIT | 488 | EACL'26 Main paper. Multi-agent ADDIE pipeline: syllabus → LaTeX slides → assessments, with Teaching Faculty / Instructional Designer / TA / Coordinator roles. Also ships as a Claude Code Skills release (2026.4.15). |
| Study-Mate | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | 1.0k | AI study partner that plans learning paths, explains concepts and guides projects end to end. |
| anki-mcp-server | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 516 | MCP server exposing the Anki flashcard app to any MCP client. The cleanest way to put spaced repetition behind an agent. |
| lineage-skill | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | Apache-2.0 | 458 | Turns videos, PDFs, transcripts and notes into teacher-style agent skills that stay tied to their sources — provenance is a first-class output, not an afterthought. |
| universal-examprep-skill | [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | 308 | Exam-prep coach that teaches from the institution's own slides, with page-level citations and generated quizzes. |
| Bloom | [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | 288 | Private AI tutor that adapts lessons to the learner. Ships both as an agent skill and as a web app. |
| universal-diagnostic-tutor-skill | [SenmuuuuW/universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | MIT | 246 | Diagnosis-first tutor for STEM and CS: establishes the misconception before it teaches. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | 267 | Intelligent tutoring system with Bayesian Knowledge Tracing, ReactJS + Firebase. UC Berkeley CAHL lab, 1,045 commits. The reference open ITS for maths/STEM. |
| OpenTutor *(zijinz456 — **a DIFFERENT repository** from `LEARNableLabs/opentutor` below)* | [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) | MIT | 142 | Local, block-based adaptive workspace that generates notes, quizzes and flashcards. Runs without a cloud dependency. 🔴 **Disambiguated at `p297`:** a second, unrelated MIT project named *OpenTutor* (`LEARNableLabs/opentutor`, 1★, 300 commits) was promoted onto this table in the same pass. **Cite the owner, never the bare name.** |
| education-skills | [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT | 114 | Collection of education-focused agent skills for teaching and tutoring workflows. |
| Claw-ED | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | MIT | 62 | Local-first assistant that drafts editable lessons, student materials and slides from a curriculum. Teacher-reviewed beta — human-in-the-loop by design. |
| AI_Tutor_Release (EduAgent) | [Zenglian990/AI_Tutor_Release](https://github.com/Zenglian990/AI_Tutor_Release) | MIT | 65 | RAG tutor targeted at grades 1–9. |
| tutor-mcp | [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 49 | MCP server that turns any LLM into an intelligent tutoring system. Small, readable, and the right shape for embedding in a client's existing assistant. |
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 295 | **Canvas LMS MCP server — the agent row with the shortest path to a live client system.** 102–126 tools plus 8 agent skills over the Canvas API, works with Claude, Cursor, Codex and other MCP clients. v1.14.0 released October 2026, 1,026 commits, University of Illinois Urbana-Champaign named in the README. It makes the LMS a client **already runs** addressable by an agent **without forking the LMS** — see the tool-count caveat below. |
| google-classroom-mcp | [adriasantacreu/google-classroom-mcp](https://github.com/adriasantacreu/google-classroom-mcp) | MIT *(metadata — see grade note)* | 2 | **Google Classroom MCP server, and the most capable of its family: "46 fully implemented tools"** over courses, assignments, grading, rosters and Drive file management. 11 commits. ⚠️ Licence is **metadata grade** (`package.json` plus a README statement); the sidebar shows no licence and no payload is served. Build on it only with that written down. |
| edu-workspace-mcp | [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | MIT | 1 | **Google *Workspace for Education* MCP server** — Docs, Sheets, Slides, Forms, Drive **and** Classroom, 29 tools in the README table. 42 commits. **The first Korean-language education agent this KB has payload-verified** (README in Korean, references Korean curriculum standards, and ships `docs_import_hwp` / `docs_export_hwpx` for Korea's national document formats). Widest reach in this family — and therefore the widest blast radius: see the scope warning below. |
| classroom-mcp | [OmarNiazi/classroom-mcp](https://github.com/OmarNiazi/classroom-mcp) | MIT | 0 | Google Classroom for **students**, *"read-only: it can't submit work, post, or change anything."* 7 commits. Read-only by construction is the right shape for a student-side pilot and the wrong shape for an institutional deliverable. |
| moodle-mcp *(teacher side, **write**)* | [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | MIT | 1 | **The permissive Moodle doorway this shelf implied did not exist.** stdio MCP server exposing **40 high-level facades plus a `ws_raw` escape hatch** over Moodle Web Services: courses, sections, content, quizzes (GIFT import), enrolment CSV, groups, roles, gradebook, messaging, calendar, badges. Every write is **upsert-by-`idnumber`**, so republishing never duplicates. Works against **any Moodle 4.x/5.x** with Web Services on. ⚠️ **Three prices, all recorded below:** the write half needs a companion Moodle `local_` plugin (→ the deployed combination is GPL-3.0, see pass 273 note); this base's own `T4` finding is that its writes are **ungated**; and at 1★/59 commits it is a **reference implementation, not a dependency**. Tool surface is in **Spanish**. |
| moodle-mcp-server *(student side, read + submit)* | [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | MIT | 0 | MCP server **and REST API** in **Go** connecting any model to any Moodle instance: courses, contents, grades, assignments, deadlines, calendar, notifications — **13–14 tools**, student-facing. The only Go implementation this base has located. ⚠️ `submit_assignment` means it is **not read-only**, which its own framing underplays. ⚠️ Its documented install is `irm …/install.ps1 \| iex` / `curl …/install.sh \| bash` — **pipe-to-shell from a 0★ repo is not an institutional install path**; build from source. Unproven, but clean at payload. |
| Athena | [ls1intum/Athena](https://github.com/ls1intum/Athena) | MIT *(metadata — 12 of 14 manifests; see grade note)* | 6 | **Artemis's feedback-suggestion engine — the open grading agent, and new to this tier in pass 275 after three passes shelved as all-rights-reserved.** Generates feedback suggestions for text, modelling and programming exercises; each module (`module_text_llm`, `module_programming_llm`, `module_modeling_llm`) is an independently installable Poetry package, which is the reusable unit. ⚠️ Licence is **metadata grade and serves no licence FILE** — the tree was *enumerated* (691 files, zero licence-like paths), but **12 of its 14 manifests declare `license = "MIT"`**, unanimous, none declaring anything else. That is TUM's own written declaration, repeated twelve times, and it retracts this base's *"treat as all-rights-reserved, ask TUM in writing"*. Build on it with the grade written down; a payload is still worth requesting. 🟢 **Pass 279 reproduced `12 of 14` through a DIFFERENT instrument** — the per-package channel sweep, written for every row rather than for this one — so the grade is a property of the repository and not an artefact of one hand-run census. 🔴 **And the same pass found that `p278`'s root-only read had left this row carrying `NO-CHANNEL`, i.e. no grade at all**, because Athena's root `pyproject.toml` is the single manifest in the repository that is silent. Now `SINGLE-CHANNEL-MANIFEST`. Evidence: [`channel-conflict.2026-10-17-p279.tsv`](../evidence/channel-conflict.2026-10-17-p279.tsv). |
| mcp-canvas-lms | [DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) | MIT *(manifest + registry — see grade note)* | 103 | **Canvas LMS MCP server, 54 tools, `v2.3.1`** — full student functionality plus account management, vitest suite, 19 releases on npm as `canvas-mcp-server`. 🔴 **`p276` withdrew this shelf's own *"Do not use. No licence = all rights reserved"*:** `package.json` l.66 declares `"license": "MIT"` and npm ships it MIT across **19** versions. ⚠️ **Grade note:** manifest + registry, **no payload in the tree** (36 paths enumerated; the `files` array names a `LICENSE` the repo does not contain). Same grade this shelf already gives `adriasantacreu/google-classroom-mcp`. [evidence](../evidence/manifest-channel.2026-10-17-p276.tsv) |
| fsrs4anki-helper | [open-spaced-repetition/fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper) | MIT | 325 | **FSRS spaced-repetition scheduling** — the retention-optimising scheduler a tutoring agent can call instead of inventing review intervals: reschedule, postpone, advance, load-balance. 🔴 **`p276` refuted *"NO GRANT in 6 filenames"*:** the grant is at **`License`** — mixed case, **no extension** — `1 079` B, read at payload. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| EduChat *(code tier only)* | [ECNU-ICALK/EduChat](https://github.com/ECNU-ICALK/EduChat) | Apache-2.0 **for the code** *(holder 🔴 `UNFILLED`, `p281`)* · 🔴 `AGPL-3.0` model · 🔴 `CC-BY-NC-4.0` data | 973 | **Educational LLM from ECNU** (retrieval-augmented tutoring, emotional support, essay assessment). 🔴 **`p276` withdrew *"cannot be used"*:** at the same ref `fa30b6d5632c` the tree serves `LICENSE/LICENSE.txt` — **Apache-2.0, `11 357` B**, the pristine length. 🔵 **Six path probes and GitHub's API both missed it because `LICENSE` is a DIRECTORY**, so each probe hit a tree, not a blob. ⚠️ **Build on the CODE only:** shipping the weights pulls in `AGPL-3.0`, and the data is non-commercial. [evidence](../evidence/tree-enumeration.2026-10-17-p276.tsv) |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | MIT *(sidebar, p296)* | 41.0k | 🟢 **PROMOTED AT `p296` — and it is the largest education-AI repository on these shelves, by an order of magnitude.** Open Multi-Agent Interactive Classroom, from **Tsinghua (THU-MAIC)**: turns any topic or document into an interactive classroom with AI teachers *and* AI classmates, delivering lessons through slides, quizzes, simulations and whiteboards, with real-time AI grading of single/multiple-choice and short-answer items. **41.0k★ · 6.3k forks · 729 commits · `main`.** 🔴 **This row was verified in `agents/trending.md` on at least two prior passes and was never carried onto this shelf** — see the `p296` promotion-gap note at the top of this file. It is the single strongest permissive starting point for a cohort-simulation or AI-classmate engagement. |
| Rumi | [Orenda-Project/rumi-platform](https://github.com/Orenda-Project/rumi-platform) | Apache-2.0 *(sidebar + README, p296)* | 18 | 🟢 **PROMOTED AT `p296` — the first teacher-coaching agent on this shelf whose delivery channel is WhatsApp rather than a web app.** Classroom coaching on real lessons, reading assessment from a voice note, lesson plans, curriculum quizzes and teacher PD. **847 commits · 19 forks · `main`** — production-shaped despite 18★. Built by **Taleemabad (Pakistan)** and ships their **national-curriculum** content library. ⚠️ **Language count is self-contradictory:** the README table names **15** languages (English, Urdu, Arabic, Spanish, Punjabi, Sindhi, Pashto, Balochi, Sri Lankan Tamil, Hindi, Bengali, Marathi, Telugu, Tamil, Kannada) while the repo's own sidebar blurb says **9**. Quote the README list, not the blurb. **The right row for a low-bandwidth, high-language-count deployment in any region** — the channel, not the country, is what transfers. |
| Shiksha Copilot | [microsoft/Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) | MIT *(sidebar + README legal notices, p296)* | 9 | 🟢 **PROMOTED AT `p296`.** Teacher lesson-planning and classroom-material generation bound to a **chosen curriculum, grade, subject and chapter**, with teacher review before export to Word, PowerPoint or student handouts. **149 commits · 12 forks · `main`.** From **Microsoft Research India** with the **Sikshana Foundation** as education partner. ⚠️ README states it was *primarily tested on English inputs and outputs* — the curriculum binding is the reusable part, not the language coverage. The export-to-Office step is why it survives a teacher-review mandate: the artefact a teacher edits is a file they already own. |
| k12-teacher-skills | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 *(sidebar, p296)* | 572 | 🟢 **PROMOTED AT `p296` — the highest-star *skills* row on this shelf, and it ships an evaluation framework with the skills.** Source and eval harness for the agent skills in **Claude for Teachers**, co-developed with **Learning Commons**: four K-12 skills — lesson-plan creation, lesson differentiation, lesson prep, and formative check-for-understanding builders. **105 forks · 4 commits · `main`** — a small, finished artefact, not a living platform. Pairs directly with `T2` (education agents ship as skills) and with the eval gap this base has declared for several passes. |
| AI-Teaching-Agent | [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | MIT *(sidebar + README, p296)* | 0 | 🟡 **Promoted at `p296` as a READING, not a dependency.** One Markdown teaching source → reviewable, locally exportable Lab and Exam packages plus an optional 5-8 slide deck; **human approve/reject before any export**, nothing auto-published, and the README says automatic grading is **deliberately frozen**. **0★ · 0 forks · 30 commits · `main`.** Its value is the *shape*: it is the smallest complete worked example of the human-checkpoint architecture `T-p288a` says the regulators in all four regions now require. Do not brief it as software a client can adopt. |
| OpenTutor *(LEARNableLabs — **a DIFFERENT repository** from `zijinz456/OpenTutor` above)* | [LEARNableLabs/opentutor](https://github.com/LEARNableLabs/opentutor) | MIT *(sidebar + README, p297)* | 1 | 🟡 **Promoted at `p297` out of `p989`'s orphan list, and it arrives with a NAME COLLISION this shelf must not blur.** Two unrelated MIT projects are now both called *OpenTutor* on this one table; this is the `LEARNableLabs` one. *"Compounding Deliberate Curiosity"* — teaches one short lesson at a time, **asks a question before it explains**, revisits what the learner keeps missing and resurfaces ideas days later, i.e. **spaced retrieval as the product rather than a feature**. Ships **293 courses** and will build a course for an arbitrary topic; runs on web, Telegram, **or inside another agent**. **1★ · 0 forks · 300 commits · `main`.** 🔵 The 300-commit history against 1★ is the same adoption-versus-depth inversion `p296` measured on the substrate shelf. Brief it as a **reading of the spaced-retrieval tutor loop**, not as a dependency. ⚠️ This base has **not** read `zijinz456/OpenTutor`'s commit count, so the two are compared here on stars only. |
| canvas-mcp *(Gradescope reach)* | [aryankeluskar/canvas-mcp](https://github.com/aryankeluskar/canvas-mcp) | **ISC** *(sidebar, p297)* | 11 | 🟡 **The FOURTH Canvas MCP row on this shelf, promoted for exactly ONE reason: it is the only row here that reaches GRADESCOPE.** *"Collection of Canvas LMS and Gradescope tools for the model context protocol."* Canvas side: courses, modules, module items, file URLs, calendar events, assignments. Gradescope side: courses, assignments **and submission status** — a surface no other row on this shelf has. **11★ · 9 forks · 59 commits · `master`.** 🔴 **Dominated on adoption and depth by `vishalsachdev/canvas-mcp` (295★, 1 026 commits).** Choose this one **only** when the engagement must read Gradescope; for Canvas alone, choose `vishalsachdev`. 🔵 **`ISC` is a licence class new to these shelves** — OSI-approved and functionally equivalent to BSD-2-Clause. Every permissive grant carried here until now was MIT, Apache-2.0 or BSD; the gate's vocabulary should learn this one. |

**36 permissive rows in this table, measured at `p297` by enumerating it** — of which **35 are
distinct repositories**, because **1 line is the withdrawn non-repository row** `~~Iris~~` (withdrawn
at `p282` as a GitHub name alias for `ls1intum/Pyris`, kept as a line so the alias stays documented).
🔵 **Both numbers are published because the standing gate counts LINES (`34`) and an engagement needs
REPOSITORIES (`33`)** — `T-p282`'s distinction, now visible in the sentence instead of only in the
gate. Of the rows, **5 are new at `p296`** (`THU-MAIC/OpenMAIC`, `Orenda-Project/rumi-platform`,
`microsoft/Shiksha-Copilot`, `anthropics/k12-teacher-skills`,
`littlecookie0722/AI-Teaching-Agent`), so **28 were carried in.**

🔴 **`p296` CORRECTION — the count published here read `27`, and the table it describes held `29`
lines.** The `27` was assembled by adding promotions pass by pass (`14 + 3 + 1 + 3 + 2 + 1 + 3`), and
it **still counts `Iris`**, which `p282` withdrew from this very table eight passes earlier without
decrementing the total. Two errors in one number, pulling in opposite directions: it **over**-counted
by including a withdrawn alias and **under**-counted the real rows by more than that. 🔵 **The lesson is the one `p277` already wrote down and this file kept re-learning: a count
derived by accumulating deltas drifts from the artefact it claims to describe.** This number is now
published with its derivation attached, and `T37`'s re-count can check the arithmetic rather than
only the total.

**`p296` promoted `8` rows in total** — these 5 plus 3 substrates on
[`repos/foundations.md`](../repos/foundations.md). **`34` is this table's line count and `8` is the
pass's; the two are not interchangeable** (`T-p282`: a shelf's row count is not its repository count).
**24 of the carried rows are payload-verified**; `adriasantacreu/google-classroom-mcp` and
`ls1intum/Athena` are metadata grade, and all 5 new rows are **sidebar/README grade** — stated in
their own cells, because the count is not allowed to launder the weaker rows. 🔴 **None of the 9 was a discovery — every one was already verified somewhere in this repository and had never been carried onto a shelf.** The prior count read: (14 from passes 264-265, plus Artemis, Iris and Pyris in pass 266, plus
`canvas-mcp` in pass 267, plus three Google Classroom servers in pass 268, plus **two MIT Moodle
servers in pass 273**, plus **`ls1intum/Athena` in pass 275** — moved here from the licence-UNVERIFIED
table below, not newly discovered — plus the **three rows `p276` added: `DMontgomery40/mcp-canvas-lms`,
`fsrs4anki-helper` and `ECNU-ICALK/EduChat` (code tier)**.) **24 are payload-verified;
`adriasantacreu/google-classroom-mcp` and `ls1intum/Athena` are metadata grade and are marked as such
in their own cells** — the count is not allowed to launder the weaker rows.

🔴 **`p277`: this number read `24` until this pass, and the standing re-count is what caught it.**
`make hooks` was **executed** this pass (`p276` could not run it) and `T37`'s re-count reported
`permissive rows in the build-on tier · published 24 · measured 27 · STALE`. **`p276` added three rows
and did not move the count** — which is the exact failure mode `T37` was written for, committed by the
pass that was reading `T37`'s output. 🔵 **The counted value was then re-derived independently**, by a
row-by-row enumeration of this table written fresh this pass, which returned **27** and named all three
missing rows. **Two instruments, one number, agreement.**

⚠️ **Cite `canvas-mcp`'s tool count as a range, not a number.** Its About blurb says *"up to 102
tools"*; its README body says *"up to 126"*, and adds that the default profile registers fewer than
either. Two numbers on one page is not a finding to resolve by picking one — quote the range and
count the tools you actually enable.

## Verified but licence-restricted — read before you build

Real projects, real code, but the licence changes the engagement. None of these is a
"no"; each is a "price".

| Agent | Repo | Licence | Stars | The constraint |
|-------|------|---------|-------|----------------|
| gen-mentor | [GeminiLight/gen-mentor](https://github.com/GeminiLight/gen-mentor) | CC0-1.0 | 135 | Official code for an LLM multi-agent goal-oriented tutoring framework. CC0 is a public-domain dedication — permissive in effect, but it is a *content* instrument, so warranty/patent language a client's legal team expects is simply absent. |
| education-agent-skills | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | CC-BY-SA-4.0 | 873 | 165 evidence-grounded skills for teachers and school leaders. **ShareAlike**: derivatives of the skill content must carry the same licence. Excellent reference, awkward to embed in a proprietary deliverable. |
| human-skill-tree | [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | AGPL-3.0 | 571 | AI skill tree for lifelong learning, 30+ skills. AGPL reaches through network use — a hosted deployment triggers source obligations. |
| freelingo | [artcc/freelingo](https://github.com/artcc/freelingo) | AGPL-3.0 | 179 | Self-hosted language learning with AI tutor and spaced repetition. Same AGPL network clause. |
| lumen | [ahmedEid1/lumen](https://github.com/ahmedEid1/lumen) | GPL-3.0 | 89 | Builds private courses and tutors learners with course-scoped RAG. GPL-3.0 copyleft on distribution. |
| ai_tutor_forge | [guedesindev/ai_tutor_forge](https://github.com/guedesindev/ai_tutor_forge) | GPL-3.0 | 18 | Python 3 CLI that forges a personalized tutor over a user-chosen LLM. Notable as the **first Portuguese-language education agent this KB has payload-verified** — see the provenance caveat in the gaps below. GPL-3.0 copyleft on distribution, and at 21 commits it is a personal project, not a dependency. |
| moodle-mcp-server | [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0 | 1 | The Moodle-side counterpart to `canvas-mcp`: an MCP server over Moodle Web Services, 10 tools in the README table, 57 commits. **Two separate prices, not one.** AGPL-3.0's network clause reaches a hosted deployment, *and* the project is **open-core — the README sells premium plugin tools separately**. Scope any estimate to the free tool set, and note that the Moodle side of this category is roughly 1,000x less adopted than the Canvas side. 🟢 **Pass 273: this is no longer the only Moodle door.** Two **MIT** Moodle servers are now on the permissive shelf above — [`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) (teacher side, 40 tools) and [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) (student side). **Neither is more adopted than this row; both are more permissive.** Choose on the licence and the tool surface, not on the star count — none of the three has one. |
| canvas-mcp (minimal) | [admin978/canvas-mcp](https://github.com/admin978/canvas-mcp) | MIT | 4 | *"Local-first Canvas LMS MCP server. Stdio transport, ~125 lines of Python."* Permissive and worth **reading** — it is the smallest complete example of the pattern — but at 33 commits it is a reference, not a dependency. Listed here rather than on the build-on-this shelf for that reason, not for its licence. |
| mewcp-google-classroom | [AStheTECH/mewcp-google-classroom](https://github.com/AStheTECH/mewcp-google-classroom) | **"AStheTECH Community License (ACL)" — proprietary** | — | ⚠️ **Not open source, and it arrived describing itself exactly like the seven MIT rows above.** Its payload sits at `LICENSE.md` and opens *"Copyright (c) 2026 AStheTech. **All rights reserved**"* with an acceptance-of-terms clause. **Second instance of the PageLM pattern** — a permissive-looking education repo whose grant is a bespoke licence. Not usable in a client deliverable. It is **not** a lure (it passes all three substantive predicates of the `p238` gate); it is simply **not permissive**, which is why the gate can never replace reading the grant. |

## Verified but licence-UNVERIFIED — do not assume the parent's licence

| Repo | Status | Why it is not shelved |
|------|--------|----------------------|
| [ls1intum/Athena](https://github.com/ls1intum/Athena) | 🔴 **RETRACTED in pass 275 — MIT at *metadata* grade. Now a row in the build-on tier above.** | **This base carried Athena as all-rights-reserved across three passes and 76 path/ref probes, and the verdict was false.** It is true that no licence FILE exists — pass 275 settled that by *enumerating* the tree rather than guessing at it (`git ls-tree -r`: **691 files, zero licence-like paths**, so the absence is now definitive rather than probabilistic). But **12 of Athena's 14 manifests declare `license = "MIT"`** — `athena/`, `llm_core/`, `assessment_module_manager/`, `log_viewer/` and all eight `modules/*/` packages — unanimous, with none declaring anything else. 🔴 **Why 76 probes missed it:** pass 267's list (quoted in this file until this pass) probed *"the package metadata (`package.json`, `pyproject.toml`, …)"* — **at the ROOT**. Athena's root `pyproject.toml` is a 632-byte Poetry *workspace stub* containing **zero occurrences of the string `license`**; it is the one manifest in the repository that is silent. The ladder probed precisely it, four times over, and the miss was structurally guaranteed. **A monorepo declares its grant per package.** *"Ask TUM for the licence in writing"* is withdrawn: TUM has written it down, twelve times, in the repository. Evidence: [`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv). |
| [learningequality/kolibri-design-system](https://github.com/learningequality/kolibri-design-system) | **RESOLVED in pass 267 — MIT at *metadata* grade** | This base carried the row as "no payload, parent `kolibri` is MIT" — which is an **inference from the parent**, the weakest grade there is. The repo's `main/package.json` declares `"license": "MIT"`. That is the **project's own declaration**, so publish it as **MIT (metadata)**: stronger than an inference, weaker than a payload, and enough to build on while a payload is requested. It still serves no licence *file*. |
| [autograder-org/autoGrader-frontend](https://github.com/autograder-org/autoGrader-frontend) | LIVE, **no licence payload — upheld against the 19-path x 4-ref probe** | README claims LLM-based assignment grading; 22 commits. Early-stage and unlicensed. Pass 267 confirms it is not a detection artefact. |
| [OpenEMIS/OpenEMIS-Core](https://github.com/OpenEMIS/OpenEMIS-Core) | LIVE, **no licence payload**, none in the page sidebar | *"Manage students and staff information at school, district, and national level."* OpenEMIS is the education-management system most associated with **ministry-level** deployment, which is why pass 267 probed it by hand. What this KB can actually reach is a **32-commit Docker packaging repo (7★) with no licence and no ministry or country named in it.** The application source was not located this pass. **Ministry provenance is not established — do not brief it as a public-sector reference.** |
| [muskvdc/EduTwin-Africa](https://github.com/muskvdc/EduTwin-Africa) | LIVE, **PRE-LICENCE — the placeholder is still in the README** *(new in pass 269)* | Curriculum-aware tutor over **South African** curriculum knowledge, **Grades 8–12**: RAG, adaptive learning, bounded multi-agent collaboration, ReAct tools, guardrails. 0★ / 0 forks / 7 commits, default ref `main`. **No payload on 19 of 19 paths, no `license` field in `pyproject.toml`**, and the README says, in the author's own words: *"Add the project's chosen license here before publishing if a specific open-source license is required."* 🔵 **This is a state this shelf has not carried before.** `Athena` and `autoGrader-frontend` are *silent*; this one is **explicitly not yet licensed**. The practical difference is that it is the one row here where asking costs nothing and might work — the author has written down that they know it is missing. Until then: all rights reserved. |
| [Valexxy/edunaija-os](https://github.com/Valexxy/edunaija-os) | LIVE, **no grant on any channel** *(new in pass 269)* | *"A security-conscious starter codebase for a Nigerian-first learning platform"*; `package.json` name is `nigeria-learning-platform`. 0★ / 0 forks / 6 commits. No payload on 19 of 19 paths and **no `license` field in `package.json`** — the two channels that could have carried a grant both empty. Names **no exam board and no institution**. 🔴 **Cite it carefully: it is NOT the EduNaija AI Tutor of the AfricaNLP 2026 paper** (that system is a five-agent LangChain + FAISS RAG tutor with English/Yoruba/Hausa/Igbo support; this is a starter codebase with a similar name). **Two different artefacts, one name** — see the trends file. |

## 🟡 Pass 284 — no row added for the TENTH pass, and the one thing the leg was good for was a licence warning

⏱️ `2026-10-18`, sixth pass. Evidence: [`p284-websearch.2026-10-18-p284.tsv`](../evidence/p284-websearch.2026-10-18-p284.tsv).

🔴 **What was searched and what was missing**, stated so the nil is an informed gap and not silence.
The leg `top open source AI agents education 2026 github MIT` returned
`microsoft/ai-agents-for-beginners` (MIT, *"12 Lessons to Get Started Building AI Agents"*),
`pguso/agents-from-scratch` (MIT, agents from first principles on a local LLM),
`free-ai-agents-resources` (licence unstated), and the general-purpose set already known to this
base — Hermes, `aider`, `Cline`, `AutoGen`, `LangGraph`.

🔵 **None is an education-sector agent.** `p283`'s diagnosis is reproduced by an independent run:
in this channel *"educational"* names a repository that **teaches machine learning**, not one that
**serves a learner**. 🔴 **Ten passes.** The shelf above is therefore unchanged, and an eleventh
run of the same query is not the way to extend it — see the backlog in [`../README.md`](../README.md).

### 🔴 The warning the leg DID earn: a third channel for the `all-rights-reserved` lure

A reviewer result in the same leg observed that *"open source"* is being stretched this year and
named **`Suna` under Elastic License 2.0** — **source-available, not open source**. 🔵 This base has
now met that pattern through **three different channels**: a repository describing itself
permissively (`PageLM`), a repository whose bespoke licence wears an MIT-shaped description
(`mewcp-google-classroom`, *"AStheTECH Community License"*), and now **a curated list asserting
open-source status on a project's behalf**.

🟢 **The operational rule is unchanged and this is the third proof of it:** the grade comes from the
grant payload, never from the thing that recommended the repository. Every row in the tables above
is payload- or manifest-graded for exactly this reason, and the grade is written in the row.

## 🟢 Pass 283 — every live address on this shelf is now PROVEN to be a distinct repository, and the proof is a standing gate

⏱️ `2026-10-18`, fifth pass. Evidence: [`repo-identity.2026-10-18-p283.tsv`](../evidence/repo-identity.2026-10-18-p283.tsv) · [`ladder-case-audit.2026-10-18-p283.tsv`](../evidence/ladder-case-audit.2026-10-18-p283.tsv) · [`p283-websearch.2026-10-18-p283.tsv`](../evidence/p283-websearch.2026-10-18-p283.tsv).

🔴 `p282` found this shelf recommending **one repository as two rows** (`ls1intum/Iris` ==
`ls1intum/Pyris`), proved the remedy **by hand**, and left it out of the Makefile — the failure
mode this base's own Makefile header opens with, *"a working gate that stayed a one-off"*. `p283`
registered it first for that reason. **It is now `make gate-identity`, inside `make hooks`.**

🟢 **The online half bounds the whole question, and far wider than `p282` did.** One
`git ls-remote` per **live** address across all three shelves:

| measure | p282 (by hand) | 🟢 p283 (standing) |
|---|---|---|
| addresses censused | 27 (build-on tier only) | **138** (all three shelves) |
| distinct repositories | 26 | **138** |
| alias pairs | 1 | **0 remaining** |
| unreachable | — | **0** |

🔵 **138 of 138 resolve, and 138 distinct HEADs means no two live rows are the same repository.**
The duplication question is closed, not carried. 🔴 It also sharpens `p282`'s channel finding: the
**git** channel is fully open (138/138) while `github.com` pages and `api.github.com` stay `403`,
so **grants and identity are current and only the star column is frozen**.

### 🔴 The gate found a live residue on its first run — in a row `p282` did not correct

`p282` corrected `agents/top.md`, `compose/patterns.md` and `verticals/solutions.md`.
🔴 **[`repos/foundations.md`](../repos/foundations.md) was missed**: the `ls1intum/Artemis` row still
presented *"**Iris** (LLM tutor, `ls1intum/Iris`, MIT), **Pyris** (the LLM microservice behind it,
`ls1intum/Pyris`, MIT)"* — the two halves of one repository, inside **one cell**, as two distinct
MIT subsystems. 🟢 Corrected. 🔵 **A hand-correction that spans four files misses one; that is the
argument for the gate, made by the gate, on the pass that built it.**

### 🔴 The first draft of the gate was wrong, and the real corpus is what caught it

🔴 Scoped to the **file**, it produced **15 findings on a green shelf** — every one a row in this
file's own `## Agents by function` **index** pointing at a repository the build-on tier also lists.
That is a cross-reference, which is what an index is *for*. 🟢 **The unit is the TABLE, not the
file**, and the 15 false positives are pinned as controls `C4`/`C5`.

🔵 The one subtlety worth stating, because it constrains every future version: `p282` withdrew the
`Iris` row **in place**, struck through, carrying its own evidence. A gate that fires on a published
correction can never be green without deleting the forensic record. **A row is live unless its first
cell is struck through or the row says `WITHDRAWN`** — controls `C2`/`C3`.

### 🟡 Ninth consecutive pass with no new agent

All four global legs ran. They returned general-purpose coding and orchestration agents
(`OpenHands`, `MetaGPT`, `CrewAI`, `LangGraph`), two `awesome-*` lists, a Hugging Face course and
`karpathy/nanochat`. 🔵 **"Educational" in this channel means *teaching ML*, not *serving a
learner*** — and one result said the education angle was thin outright. **Nine passes makes this a
property of the channel, not a dry spell.**

## 🔴 Pass 282 correction to the pass-268 note below — "Iris and Pyris" are ONE repository, and it DOES serve a README

`p268` probed these as two rows and recorded a defect: *"neither repository serves a README"*.
Both halves of that sentence are wrong, and the same instrument produced both errors.

1. 🔴 **They are not two repositories.** `ls1intum/Iris` is a **name alias** that resolves to
   `ls1intum/Pyris`: identical HEAD `d7b2c095204e`, identical **245** refs, identical root tree
   `4e2f096df767`, **203** files, identical **1 088**-byte MIT payload. The grant `p268` graded
   "for both rows" is **one grant, read twice**.
2. 🔴 **It does serve a README — at `README.MD`.** `p268`'s ladder probed `README.md`, `readme.md`,
   `README.rst` and `README`; **none of its four spellings carries an uppercase EXTENSION**, and
   that is the only spelling the repository uses. 🔵 This base already owns the class —
   `p1057-licence-path-case` — and it was built for **licence** paths only, so the README ladder
   beside it never inherited it. A path ladder cannot prove absence (`p275`), and a path ladder
   that is not case-closed cannot even prove a 404.

🟢 What survives `p268` intact: the grant is **MIT at payload grade**, and the copyright line
**"Copyright (c) 2023 TUM Applied Software Engineering"** is payload-quoted TU Munich provenance.
That was right, and it is a property of **one** repository.
Evidence: [`alias-identity.2026-10-18-p282.tsv`](../evidence/alias-identity.2026-10-18-p282.tsv) ·
[`readme-path-case.2026-10-18-p282.tsv`](../evidence/readme-path-case.2026-10-18-p282.tsv).

## Pass 280 — the licence under row 1 is held by a UNIVERSITY, and this shelf reported it as unanswerable

🔵 **Evidence:** [`holder-candidates.2026-10-18-p280.tsv`](../evidence/holder-candidates.2026-10-18-p280.tsv)
*(70 holder candidates from three real full licence texts, each graded by the guard that rejects it)* ·
[`channel-conflict.2026-10-18-p280.tsv`](../evidence/channel-conflict.2026-10-18-p280.tsv) *(the 14
metadata-graded slugs re-swept, `MANIFEST_CAP` `14 → 250`, two new columns)* ·
[`fixtures/PROVENANCE.tsv`](../compose/code/pass280-package-provenance/fixtures/PROVENANCE.tsv)
*(every payload a control now asserts, with `slug / ref / head_sha / sha256 / date`)*.

### 🟢 `HKUDS/DeepTutor` — **Apache-2.0, held by `Data Intelligence Lab, The University of Hong Kong`**

Read first-hand from the repository's own `LICENSE` payload this pass. The Apache template puts the
holder in an **appendix** that most projects ship unfilled; `DeepTutor` filled it:

```
Copyright 2025 Data Intelligence Lab, The University of Hong Kong
```

🟢 **For a studio this strengthens the row rather than qualifying it.** The counterparty on the
permissive grant is a **university lab**, not an individual maintainer — the grant does not rest on
one person's continued goodwill, and a client's legal review has a nameable institution. 🔴 **This
base published `NOT-APPLICABLE` ("holder not in the license text by construction") for every
non-MIT/BSD/ISC family for 96 passes**, so the strongest provenance fact about its top row was
invisible. 🟡 The holder-vs-account comparison prints `HOLDER-UNRELATED`, which is the instrument's
limit and **not** a fork signal: `HKUDS` is HKU's Data Science group, and no token test bridges an
acronym to its expansion.

🔵 **Same class, different family:** `GibbonEdu/core` fills the **GPL-3.0** appendix at line 655 —
`Core  Copyright (C) 2010  Gibbon Foundation` — so a verbatim-GPL payload can carry the project's own
holder too. `moodle/moodle`'s `COPYING` ships it **unfilled** (`<year> <name of author>`), which is
why the construction argument held for so long. The discriminator is a **year** between `Copyright`
and the name; all three payloads are controlled.

### 🔴 Two metadata-graded build-on rows change their measured licence shape

| row | published before | measured this pass |
|---|---|---|
| 🔴 **[codelitdev/courselit](https://github.com/codelitdev/courselit)** | manifest **MIT**, `1` distinct declaration across the tree | 🔴 **`2` distinct: 14 manifests MIT, `packages/scripts/package.json` (`@courselit/scripts`) ISC.** Committed payload is **AGPL-3.0**, so the row keeps `MANIFEST-OVERSTATES` — and a studio vendoring `packages/scripts/` gets **ISC**, not the root's MIT and not the payload's AGPL |
| 🟢 **[DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms)** | 🟡 flagged `manifests_foreign = 1` — its root `package.json` names `canvas-mcp-server`, which matches neither half of the slug | 🟢 **CLEARED.** The same manifest declares `"repository": "git+https://github.com/DMontgomery40/mcp-canvas-lms.git"` — its own repository. **Naming a package differently from its repository is ordinary**, and the declared channel proves it here rather than asking a reader to assume it |

🟡 **Three of the four root-name flags are NOT cleared** — `cccareers/open-source-curriculum`,
`codeXsidd/Studivexa` and `Gnanakamalesh-M/student-dropout-early-warning` **declare no repository at
all**, so for them the name difference stays *recorded, never enforced*.

### 🟢 `Open-TutorAi/open-tutor-ai-CE` — the row's licence conflict was an artefact, and it is excluded by code now

The second "declaration" in this repository's tree was a **bundled Pyodide runtime** under
`ui/static/pyodide/`, Apache-2.0, which produced a false *"SUBPACKAGES DISAGREE (2 distinct)"* note.
🟢 The bundled manifest declares `"repository": "https://github.com/pyodide/pyodide"` in its own
bytes, so it is excluded by **what it says about itself** rather than by a path convention or a
hand-maintained list of library names. The row's own grant is unchanged: **BSD-3-Clause payload**
against a **MIT** `pyproject.toml` — `p121`'s row 8, still the same wrong-name-both-permissive
verdict.

## Pass 278 — the metadata grade, measured on the other channel: four build-on rows have NO committed grant, and the tree proves it

🔵 **Evidence:** [`channel-conflict.2026-10-17-p278.tsv`](../evidence/channel-conflict.2026-10-17-p278.tsv)
*(14 slugs, both channels, pinned refs)* ·
[`tree-enumeration.2026-10-17-p278.tsv`](../evidence/tree-enumeration.2026-10-17-p278.tsv)
*(6 trees enumerated in full)*. Instrument:
[`compose/code/p278-channel-conflict/`](../compose/code/p278-channel-conflict/).

`p277` asked for the metadata-graded rows to be swept on the payload channel. 🟢 **Done, for the
four rows on this file a studio is told to build on — and the answer is the same for all four:
the manifest is the only grant there is, and that is now proven by a full tree enumeration
rather than inferred from a path ladder.**

| row | manifest channel | payload channel, **tree enumerated** | what it means for a deliverable |
|---|---|---|---|
| [`adriasantacreu/google-classroom-mcp`](https://github.com/adriasantacreu/google-classroom-mcp) | 🟢 **MIT** (`package.json`) | 🔴 **15 paths at `29c2c2a07670`, ZERO licence-like** | **MIT (metadata) is the ceiling.** Usable, and the attribution text must come from the manifest because there is no payload to quote |
| [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system) | 🟢 **MIT** (`package.json`) | 🔴 **15 448 paths at `adefe26118c6`**; the only 7 licence-like paths are **Material Design icon components** (`precompiled-icons/.../copyright/*.vue`, `mdi/license.vue`) | **MIT (metadata).** 🟢 `p277` declared the `.vue` false-candidate class for `p278` — **it was already fixed in `p277` itself**: `candidate_grants()` returns `[]` on all seven, verified this pass |
| [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🟢 **MIT** (`package.json` + npm, 19 versions) | 🔴 **36 paths at `c0646ba10ac2`, ZERO licence-like** | **MIT (metadata + registry).** 🟢 Reproduces `p276` exactly — same SHA, same 36 paths — by an independently written instrument |
| [`ls1intum/Athena`](https://github.com/ls1intum/Athena) | 🟢 **MIT**, 12 of 14 manifests (`p275`) | 🔴 **691 paths at `6316d302c929`, ZERO licence-like** | **MIT (metadata).** 🟢 Reproduces `p275`'s 691-path count independently. 🔴 **And `p278`'s own sweep returned `NO-CHANNEL` here**, because it reads **root** manifests only — *"a monorepo declares its grant per package"* is `p275`'s sentence, and `p278`'s instrument re-committed the error it corrects. Named in the instrument README, not hidden |

🟢 **No conflict was found on any of the four.** That is the useful half: a row graded *metadata*
on this file is now known to be *metadata because there is nothing else*, not *metadata because
nobody looked*. 🔵 **The grade vocabulary needed that distinction and did not have it** — which
is the one defensible reading of `p277`'s claim that this base *"has no class for CONFLICT"*.
The class itself was `p121`'s and has existed for 157 passes; see the instrument README.

## Pass 276 — the queue was worked, and this shelf gains three rows: two from a channel the gate does not read, one from a path no ladder spells

**30 of `p275`'s 124 queued negative verdicts enumerated** in two channels — tree *and* manifest.
30/30 slugs resolve. **9 verdicts refuted, 7 positive controls passed, 18 absences now sayable in both
channels.** Evidence: [`tree-enumeration`](../evidence/tree-enumeration.2026-10-17-p276.tsv) ·
[`manifest-channel`](../evidence/manifest-channel.2026-10-17-p276.tsv).

🔴 **The grade this shelf already owned, and withheld from one row.** `adriasantacreu/google-classroom-mcp`
is tabled above as **MIT *(metadata)*** — no licence file, `"license": "MIT"` in `package.json`.
`DMontgomery40/mcp-canvas-lms` has **the same evidence plus 19 MIT releases on npm**, and this shelf
published *"NONE … Do not use."* **Two rows, one evidence shape, opposite verdicts.** `p274`'s sentence —
*"a correction applied to one instance is not a correction to the class"* — now has its eighth
consecutive instance, and this time the class was a grade this base had already defined.

🔵 **Taken with `p275`'s 2-of-13, the measured error rate of a ladder-shaped negative verdict is 11 of
43.** Roughly one in four. `QUEUE-UNENUMERATED` falls **124 → 70**; `VERIFIED-ABSENT` rises **28 → 48**.

⚠️ **One row on this shelf cannot hold its own licence.** `ECNU-ICALK/EduChat` carries **three** grants —
Apache-2.0 code, `AGPL-3.0` weights, `CC-BY-NC-4.0` data. A single Licence column is the wrong shape for
it, and the row says so rather than picking the flattering value.

🔴 **A refuted absence is not a permission (`P-N1`).** `dssg/student-early-warning` was carried as
`RESERVED`/`CONDITIONAL-GRANT` — and that was **right**: the grant exists (`2 069` B, read this pass) and
it permits only *"academic research or other not-for-profit scholarly purposes"*, expressly excluding
*"any service or part of selling a service."* **Enumeration can refute an absence without clearing a row
for use**, and the grade must come from the payload's terms, not from the existence of a file.


## Pass 275 — the row this shelf told studios not to use has declared MIT twelve times, and the refusal came from probing one 632-byte file

⏱️ **Twenty-first pass of `2026-10-17`.** Evidence:
[`tree-enumeration.2026-10-17-p275.tsv`](../evidence/tree-enumeration.2026-10-17-p275.tsv) *(13 slugs: `ls-remote` positive control + full tree enumeration, zero searches)* ·
[`athena-manifest-census.2026-10-17-p275.tsv`](../evidence/athena-manifest-census.2026-10-17-p275.tsv) *(14 manifests, every one read at payload)* ·
[`verified-repos.2026-10-17-p275.tsv`](../evidence/verified-repos.2026-10-17-p275.tsv) ·
[`p275-websearch.2026-10-17-p275.tsv`](../evidence/p275-websearch.2026-10-17-p275.tsv) *(8 legs)*.

### 🟢 `p274`'s top-ranked item was run, and it returned a real negative — then the thing it was testing turned out not to be the problem

`p274` ranked, at zero searches: *"re-probe every negative licence verdict with `ls-remote` as a
positive control first — because the mechanism that produced the `gegok12` false negative is not
specific to that row."*

🟢 **Run over 13 slugs. The mechanism is NOT endemic:** `gegok12/gegok12` fails `ls-remote` with
`rc=128` exactly as a nonexistent repository does, and **all twelve other negative-verdict slugs
resolve**. The backlog item is **discharged with a measured answer**, not deferred.

🔴 **And then the same sweep refuted two of this base's own published verdicts** — not because a slug
was wrong, but because **a path ladder cannot prove absence** (`T46`):

| row | this shelf published | enumeration found |
|---|---|---|
| **`ls1intum/Athena`** | *"no grant across 76 path/ref probes over three passes; treat as all-rights-reserved; ask TUM for the licence in writing"* | 🔴 **12 of 14 manifests declare `license = "MIT"`.** Now the **24th permissive row** |
| **`os4ed/openSIS-Classic`** *(`verticals/`)* | *"no licence payload served on any path tried"* | 🔴 **`docs/License.txt` — verbatim GPL-2.0, 200, 17 286 B** |

### 🔴 The box this pass earned

| the finding | how it surfaced | why it had not been found |
|---|---|---|
| 🔴 **A 76-PROBE REFUSAL WAS AIMED AT THE ONE MANIFEST IN THE REPOSITORY THAT IS SILENT** | 🟢 By **enumerating** the tree (`git ls-tree -r` over a blobless clone) instead of extending the ladder a fifth time | 🔴 `p267`'s list is sound *as written* — `pyproject.toml` is on it. It is aimed at the **root**, and Athena's root `pyproject.toml` is a **632 B Poetry workspace stub with zero occurrences of `license`**. **A monorepo declares its grant per package** (`T47`). Every added path made the refusal feel better-evidenced while leaving the unexamined space the same size |
| 🔴 **THIS BASE HELD THE PRINCIPLE *AND* THE CODE FOR ~180 PASSES AND NEVER APPLIED EITHER TO LICENCES** | 🟢 By finding [`compose/code/p275-tree-enumeration/`](../compose/code/p275-tree-enumeration/) — **pase 93, `2026-10-04`** — which states **`P275`** (*to sustain an absence in a tree you must ENUMERATE it*) and **`P278`** (*a ZERO over a path that does not exist in that ref measures the PATH, not the content*) and ships a working blobless-clone enumerator | 🔴 **`P278` describes both of this pass's false negatives exactly.** The principle was applied to **directory** trees (ILIAS, `frappe`, `openeducat`) and **never to licence paths**, where `p267` built a `19 × 4` ladder instead. 🔵 **`p274` wrote the diagnosis — *"a correction applied to one instance is not a correction to the class"* — and this is that sentence about `p274` itself.** Sixth consecutive pass whose defect species was invisible to the prior check, **and the first where the lesson existed in general form, in code** |
| 🔴 **A CHANNEL PROBED AT ONE PATH NEARLY PUBLISHED A FALSE CHANNEL STATE** | 🟢 By probing the path to be **used** rather than a cheaper neighbour | 🔴 `api.github.com/rate_limit` → **200** with a plausible body; `api.github.com/repos/<slug>` → **403** *(session-scope message, not a rate limit)*. Reading the 200 as access would have invited the next pass to refresh **star counts** from an API this session does not have (`T48`) |

### 🔵 Registered, not claimed

- 🟢 **The instrument is BUILT, not described** — `make gate-enumeration` is in `make hooks`, with **30
  controls** (`compose/code/pass275-grant-enumeration/`). `p274`'s own lesson was that *"an amendment that is
  not built gets violated by the next pass"*; this pass did not repeat it.
- 🔴 **Running the gate on the live shelves corrected the gate three times**, each for the same reason —
  **one line can carry two subjects**. It first reported `ls1intum/Artemis`, an MIT row with a root
  `LICENSE`, as **refuting itself** (the phrase on that line is about Athena, four slugs later); then
  missed a subject named in bold **prose** rather than as a link; then flagged **this pass's own new
  Athena row**, because that row opens *"**Artemis's** feedback-suggestion engine"* — **a possessive is a
  modifier, not a subject.** Teaching it prose names found **2 further live occurrences** of the openSIS
  claim the slug-only rule had missed.
- 🔵 **`QUEUE-UNENUMERATED=124`.** 124 negative licence verdicts on these shelves still rest on a path
  ladder. **That is not a failure signal — it is the first honest measurement of the exposure**, and it
  prints on every `make hooks` run.
- ⚠️ **No star count in this pass was read from GitHub.** `api.github.com` 403 on `/repos` and `/search`,
  `github.com` HTML 403. Athena's `6★` and every other figure on this shelf is **carried** and marked so.
- 🟢 **The permissive count moved 23 → 24 and `make recount` was updated with it**, so `T37` still
  re-derives it from the rows: `STALE=0 of 4`.

## Pass 274 — the gap this file declared was contradicted by a row in this file, and the MCP count was two platforms short of its own evidence

⏱️ **Twentieth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p274.tsv`](../evidence/verified-repos.2026-10-17-p274.tsv) *(12 probes, every
grant read at payload, channel re-tested not inherited)* ·
[`quantity-recount.2026-10-17-p274.tsv`](../evidence/quantity-recount.2026-10-17-p274.tsv) *(5 registered
quantities, zero searches)* ·
[`p274-websearch.2026-10-17-p274.tsv`](../evidence/p274-websearch.2026-10-17-p274.tsv) *(10 legs)*.

### 🟢 The eight-pass nil on agent supply ENDS — and not through the supply channel

| what | result |
|---|---|
| 🟢 **Six rows added to the MCP table** | `bruchris/canvas-lms-mcp` (MIT, FERPA pseudonymisation), `RohanMuppa/brightspace-mcp-server` (MIT), `felipedias-ie/blackboard-mcp` (MIT), `NiccoloSalvini/mcp-blackboard-ucsc` (MIT), `blend-ed/tutor-contrib-openedxmcp` (AGPL-3.0) — **and every one was already on [`trending.md`](trending.md) with a payload-read grant.** Nothing was discovered; something was **shelved** |
| 🔴 **The `Bloom`/`Lumen` gap was FALSE** | `Li-Evan/Bloom` is a row in this file's own build-on tier. `ahmedEid1/Lumen` was in this base's `p195` census. **Two passes called them unresolvable and a third ranked searching again** |
| 🔴 **A twice-carried licence REFUTATION is itself refuted** | `Gego-K12/gegok12` serves **MIT**, `1 150` B, diffed and byte-accounted. See `T44` and [`verticals/solutions.md`](../verticals/solutions.md) |
| 🔴 **The count was wrong on both shelves** | **15** slugs tabled here (prose said 13; `T21` said 12) and **6** platforms reachable (both shelves said 3) |

### 🔴 The box this pass earned

| the finding | how it surfaced | why it had not been found |
|---|---|---|
| 🔴 **A FILE CAN DECLARE A GAP THAT ONE OF ITS OWN ROWS REFUTES, AND EVERY CROSS-SHELF CHECK ON THIS BASE PASSES IT** | 🟢 By doing what `p273` costed — **reading a shelf top to bottom as a reader** — rather than grepping between shelves | 🔴 `T29` greps the **destination** file; `T34` greps the **other** shelves; `T37` re-counts a **quantity**. **The Bloom contradiction is INTRA-FILE and QUALITATIVE**: a row at line `46` and a sentence at line `456` of the same file. 🔵 **Fifth consecutive pass whose defect species was invisible to the check written one pass before** — and this time the check that would have caught it (`T34`) existed and ran |
| 🔴 **AN AMENDMENT THAT IS NOT BUILT GETS VIOLATED BY THE NEXT PASS** | 🟢 By **building** `T37` instead of citing it (90 lines, no network) and running it | 🔴 `T37` was written in `p272` and ranked seventh by `p273`. In the two passes between the amendment and its implementation, **three more stale quantities were published.** 🟢 `make recount` now derives them. See `T43` |
| 🔴 **THIS SHELF HELD AN MIT DOORWAY INTO AN INCUMBENT THE STRATEGY SHELF SAYS TO REPLACE** | 🟢 By grouping the MCP rows **by platform** instead of counting them | 🔴 `p267` found this exact shape for Canvas (*"the opening is the opposite of migration"*) and the correction **never generalised**. Blackboard carries **two MIT servers** on `trending.md` while `market.md` sells a replacement engagement against it. **A correction applied to one instance is not a correction to the class** |

### 🔵 Registered, not claimed

- 🟢 **Every grant in this pass's ledger reproduces its carried byte count exactly** where one existed
  (`RohanMuppa` `1 068`, `blend-ed` `34 524`, `Bloom` `1 069`, `Lumen` `35 149`). Per `T39` that proves
  **stability, not correctness** — but it does confirm `P929`'s measurement method is being applied
  consistently across passes, which is the first thing that was ever in doubt.
- 🔴 **`DMontgomery40/mcp-canvas-lms` is NOT shelved as a row, and the reason belongs here:** it carries
  **its own security disclosure of a broken access control that exposed other students' personal
  information.** 🔵 Same category and same search-result description as the MIT rows above —
  the `PageLM` pattern in its **security** dimension rather than its licence one (`T45`).
- ⚠️ **No star count in this pass was read from GitHub.** `api.github.com` **403**, `github.com` HTML
  **403**, `codeload` **403**, `raw.githubusercontent.com` **200** — re-tested this pass, not inherited.
  Star figures in the new rows are **carried from `trending.md`** and marked `—` where none exists.
## Pass 273 — the Moodle door was permissive all along, and this base had measured it four times without shelving it

🔴 **Stated first, because it is a finding about this KB and not about the market.** Both MIT rows added
to the permissive table this pass —
[`MarcosNahuel/moodle-mcp`](https://github.com/MarcosNahuel/moodle-mcp) and
[`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) — are **not new to
this base.** Its own instrumentation has graded `MarcosNahuel/moodle-mcp` **MIT at payload on at least
four separate occasions** (`p114` 2026-10-02, `p170` 2026-10-03, `p191` 2026-10-14, `p725` 2026-10-08),
measured its 40-tool surface, its auth posture and its release cadence — and **it has never appeared on a
single live shelf.** Before this pass, `agents/top.md`, `repos/foundations.md`,
`verticals/solutions.md`, `intel/market.md`, `intel/trends.md` and `compose/patterns.md` contained
**zero** occurrences of the string `MarcosNahuel`.

🔵 **This is the Koha species of defect, and it is now the second confirmed instance** — a row carried for
passes in the instrumentation and never promoted to the shelf a studio actually reads. The practical
consequence here was worse than with Koha, because the shelf did not merely omit the row: the only Moodle
cell it *did* carry, [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server),
is **AGPL-3.0 and open-core**, so a studio reading this file came away believing **the Moodle side of the
MCP category has a copyleft-plus-paywall price**. It does not. 🟢 **Both corrected cells now cross-reference
each other.**

🟡 **And the reasons the rows were *correctly* withheld as dependencies are preserved rather than
deleted**, because they are the honest half of the finding: `1★ / 1 fork / 59 commits`, a *burst-and-silence*
release pattern, and this base's own **`T4`** finding that the writes execute **with no confirmation and no
disclosure**. 🔵 **The fix is not to promote them to dependencies. It is to stop letting the shelf imply an
absence that the instrumentation had already refuted** — they belong on the shelf as the **permissive
reference implementations of the Moodle agent doorway**, with their prices in the cell. That is what they
now are.

### 🔴 The genuinely new finding: this repo contains a second artefact, under a second licence regime, and the base's grading model cannot see it

`MarcosNahuel/moodle-mcp` is graded `SOLE` / `OWN-GRANT-AT-ROOT` by this base's own
`p283`/`p257` instrumentation — one grant, at the root, covering the repository. **That grading is
correct about the file and wrong about the artefact.** The repository ships **two** deliverables:

| artefact | what it is | grant served |
|---|---|---|
| `@nahuelalbornoz/moodle-mcp` | the TypeScript MCP wrapper — the thing you run | **MIT**, `main/LICENSE`, **1,065 B**, read in full this pass, **byte-identical to stock MIT, zero rider keywords** |
| `local_italiciamcp` | a **Moodle `local_` PHP plugin** in `plugin-companion/` — the thing that performs **every write** | 🔴 **no grant of its own.** No `LICENSE` and no `README` in the plugin directory (both **404**); **zero GPL notices across the six plugin files that serve** |

🔵 **The detail that makes it a finding rather than a nit.** The plugin's `version.php` opens with
Moodle's own file header — `// This file is part of Moodle - http://moodle.org/` — and **the GPL
paragraph that follows that exact line in every Moodle core file has been replaced** by a description of
the project. The plugin declares `MOODLE_INTERNAL`, requires **Moodle 4.0+**, supports `[400, 501]`, and
its `classes/external/upsert_page.php` calls **`core_external\external_api`** — it links Moodle's
internal API by construction. Moodle's own documentation puts the platform at **GPLv3-or-later** and tells
new projects to use GPLv3+.

🟢 **This is NOT a "do not use" finding, and must not be briefed as one.** MIT is **GPL-compatible**, so
there is no conflict in the grant itself. The consequence is about the **combination**, and it is a
narrow, cheap one:

- **The wrapper stays MIT.** It talks to Moodle over REST Web Services and links nothing. Build on it freely.
- **The deployed combination — Moodle + the `local_` plugin — is a GPL-3.0 work.** If a client *distributes*
  that combination (a packaged distro, an appliance, an image handed to a third party), it goes out under
  **GPL-3.0**, not MIT.
- 🟢 **For a hosted deployment that is a non-event**, because GPL-3.0 — unlike the **AGPL-3.0** on
  `csmediapro/moodle-mcp-server` — **has no network clause.** So on the price that actually decides most
  education engagements, the MIT row is still strictly cheaper than the row this shelf used to carry alone.

⚠️ **One correction to this base's own record while we are here:** the dormancy note (*"8 releases in 4 days
and nothing in 5 months"*, pinned to npm `2026-04-23`) is **stale**. The repository's `CHANGELOG.md`
documents plugin `v0.5.0` dated **`2026-05-03`**, after that pin.

Evidence: [`verified-repos.2026-10-17-p273.tsv`](../evidence/verified-repos.2026-10-17-p273.tsv) ·
[`p273-moodle-plugin-governance.2026-10-17-p273.tsv`](../evidence/p273-moodle-plugin-governance.2026-10-17-p273.tsv).
Wiring recipe: **`P23`** in [`compose/patterns.md`](../compose/patterns.md). Trend: **`T41`**.

## Pass 272 — this file gains no rows for the seventh consecutive pass, and the count it publishes was wrong

⏱️ **Eighteenth pass of `2026-10-17`.** Evidence:
[`verified-repos.2026-10-17-p272.tsv`](../evidence/verified-repos.2026-10-17-p272.tsv) ·
[`p272-websearch.2026-10-17-p272.tsv`](../evidence/p272-websearch.2026-10-17-p272.tsv).

🔵 **Seventh consecutive measured nil on education-specific agent supply.** The generic legs ran last, per
`p269`. Everything returned was already shelved (`HKUDS/DeepTutor`, whose **Apache-2.0** grant `p272`
re-read at payload: `main/LICENSE`, **11,408 B**) or unresolvable to a slug (`Bloom`, `Lumen` — named in a
topic listing with no owner, recorded as an informed gap on `repos/foundations.md`, **not** written in as
rows).
🔴 **RETRACTED IN PASS 274 — BOTH LIMBS, AND THE COUNTER-EVIDENCE FOR ONE OF THEM IS 410 LINES ABOVE
THIS SENTENCE.** `Bloom` is [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom), **MIT, `1 069` B**,
and it has been **a row in this file's own build-on tier** since `p264` — the sentence above declares
unresolvable a slug this file tables. `Lumen` is [`ahmedEid1/Lumen`](https://github.com/ahmedEid1/Lumen),
resolved from this base's **own `p195` licence census** via
[`compose/code/p196-population-diff/`](../compose/code/p196-population-diff/), and it is **GPL-3.0 at
payload (`35 149` B) against an MIT badge in its own README** — see
[`repos/foundations.md`](../repos/foundations.md). 🔵 **Neither needed a search. `p272` spent a leg, and
`p273` ranked spending another, on two slugs this base already held** — `T25`'s finding (*"the most
productive research channel was this knowledge base"*) re-earned, and `T34`'s amendment (*grep the other
shelves before re-declaring an absence*) **failed on a gap whose counter-evidence was in the same
file.** 🟢 **Nothing was added to meet the brief's five-row minimum; this file holds 42 rows and clears it
many times over.**

🔴 **The defect this file earned: it was the better source and the other shelf never caught up.** This
file's MCP-server count said **eleven** in prose while **12 distinct slugs** are actually tabled, and
`intel/trends.md` said **five**. Passes 267 and 268 added servers and updated **one shelf**. Both numbers
are corrected and the generalisation is `T37`: **a quantity inside a gap statement is a carried datum —
re-count it from the rows, on every shelf that states it.**

## Licence corrections this pass

Three cells this base previously published are wrong, and one repository it listed is gone.
Correcting them is the point of the pass.

| Row | Published | Read from payload 2026-10-17 |
|-----|-----------|------------------------------|
| `DaRL-GenAI/instructional_agents` | Apache-2.0 | **MIT** |
| `pykt-team/pykt-toolkit` stars | 1.2k | **450** (topic listing, descending-stars sort) |
| `HKUDS/DeepTutor` stars | 22k+ | **41.5k** — the project nearly doubled, the old cell understated it |
| `CaviraOSS/PageLM` | MIT, per this base's own `evidence/verified-repos.2026-10-15-p213.tsv` | **PageLM Community License** — non-commercial, and *"Redistribution of the Software, in whole or in part, in source or binary form, is strictly prohibited"*. **Not usable in a client deliverable.** See the trends file. |
| `OpenEduCat-Inc/OpenEduCat` | live vertical platform | **404.** Canonical repo is [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) (LGPL-3.0). |
| `GeminiLight/awesome-ai-llm4education` | MIT | **No LICENSE file served** on `main`/`master`/`develop`. The MIT claim is not substantiated; treat the repo as all-rights-reserved until a payload says otherwise. |
| `Open-TutorAi/open-tutor-ai-CE` | BSD-3-Clause | **BSD-3-Clause — confirmed.** The payload opens *"All rights reserved"*, which is part of the standard BSD form, not a reservation on top of it. Flagging it would have been a false positive. |

## Agents by function

### Personalized tutoring
**DeepTutor** (Apache-2.0, 41.6k) is the default starting point — persistent student model,
multi-agent, actively released. **OATutor** (MIT) when the client wants Bayesian Knowledge
Tracing they can audit rather than an LLM they must trust. **Bloom** and
**universal-diagnostic-tutor-skill** when the deliverable is a skill inside an assistant the
client already runs.

### Teacher workload / instructional design
**Instructional Agents** (MIT, EACL'26) is the only peer-reviewed option here and it is
permissively licensed — syllabus through assessments. **Claw-ED** for local-first lesson
drafting where student data cannot leave the building. **lineage-skill** when provenance of
generated material is a procurement requirement (it is, increasingly, in EMEA).

### Agents over the systems the client already runs (MCP)
Pass 268 takes this from four servers to **eleven**, and from two LMSs to **three**. 🟢 **Pass 273 takes it to thirteen, and ends Moodle's status as the one LMS reachable only through copyleft.**
🔴 **PASS 274, by re-count rather than by search: this file tabled `15` MCP server slugs when the prose
said thirteen and `T21` said twelve — and with this pass's five additions it tables `20`. `SIX`
platforms are reachable, not three** — Canvas, Moodle, Google Classroom / Workspace,
**Brightspace / D2L**, **Blackboard Ultra** and **Open edX**. The last three were on
[`agents/trending.md`](trending.md) with payload-read grants and never reached this table. The number
is now **derived** by [`compose/code/p274-quantity-recount/recount.py`](../compose/code/p274-quantity-recount/recount.py)
rather than incremented by hand (`T43`); the three platform rows below were **payload-read first-hand in
`p274`** ([ledger](../evidence/verified-repos.2026-10-17-p274.tsv)).

🔴 **PASS 278 — the count was STALE after all, and `p277` protected it on a predicate this very
file warns against.** `p277` read `T37`'s `published 20 · measured 21 · STALE`, wrote a fresh
enumeration that returned **20**, concluded *"a 1-row disagreement between two predicates is a
defect in a predicate, not a stale shelf"*, and changed nothing. 🟢 **`p278` reproduced BOTH
numbers and the disagreement is fully explained.** `p277` described its enumeration as *"every
`github.com/<owner>/<repo>` whose slug contains `mcp`"*; run exactly that way it returns **20**,
because it drops [`AStheTECH/mewcp-google-classroom`](https://github.com/AStheTECH/mewcp-google-classroom),
whose slug does **not** contain the substring `mcp`. 🔵 **`MCP_HINT`'s own code comment, five
lines above the predicate, already said so:** *"a count that greps for `mcp` silently drops
it."* 🔴 **And the dropped row is the PROPRIETARY one** — the single row on this file a studio
may **not** use. **The count that drops it under-reports the only row carrying commercial risk,
so "leave it at 20" was the costly way to be wrong.**

🟢 **The durable fix is not picking a winner between predicates — it is making the SCOPE part of
the claim**, because three defensible scopes give three answers and a bare count cannot be
checked at all. Both are registered in `recount.py` with their boundaries in code:

| scope | count | boundary |
|---|---|---|
| **distinct MCP server slugs tabled anywhere on this file** (`MCP_HINT`, incl. `mewcp`) | **21** | whole file |
| **the MCP section's own table** | **19** | the `###` heading to the next heading of equal or shallower depth |
| `p277`'s enumeration (literal `mcp`, table rows) | *20* | **not registered** — it drops a real row, and is recorded here only to explain the 20 |

**21 distinct MCP server slugs are tabled on this file**, of which **19 rows in the table
below**; the other two are tabled in the tiers above (`admin978/canvas-mcp` and
`DMontgomery40/mcp-canvas-lms`). **6 platforms** are reachable. 🔵 Every figure in this
paragraph is re-derived by `make recount`, and since `p278` the figure it compares against is
**read from this sentence** rather than carried as a constant — so editing the prose without
editing the rows is now a `STALE` verdict too, and deleting the sentence is `NO-ANCHOR`, which
fails the gate.

| Server | Licence | Stars | What it reaches |
|--------|---------|-------|-----------------|
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | **MIT** | 295 | **Canvas LMS itself** — courses, assignments, grades, 102–126 tools, 8 agent skills |
| [csmediapro/moodle-mcp-server](https://github.com/csmediapro/moodle-mcp-server) | AGPL-3.0, open-core | 1 | **Moodle** via Moodle Web Services — 10 free tools, premium tools sold separately |
| [MarcosNahuel/moodle-mcp](https://github.com/MarcosNahuel/moodle-mcp) | **MIT** | 1 | **Moodle, teacher side and it WRITES** — 40 facades + `ws_raw`: courses, sections, content, quizzes/GIFT, enrolment, gradebook, messaging, badges. Needs a `local_` plugin for writes → **combination is GPL-3.0, no network clause** |
| [Jawadh-Salih/moodle-mcp-server](https://github.com/Jawadh-Salih/moodle-mcp-server) | **MIT** | 0 | **Moodle, student side** — grades, deadlines, notifications, `submit_assignment`. Go; also exposes a REST API for non-MCP models |
| [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | MIT | 516 | The learner's **Anki** collection — spaced repetition |
| [ArnaudGuiovanna/tutor-mcp](https://github.com/ArnaudGuiovanna/tutor-mcp) | MIT | 49 | No external system — it **is** the tutoring loop |
| [adriasantacreu/google-classroom-mcp](https://github.com/adriasantacreu/google-classroom-mcp) | MIT *(metadata)* | 2 | **Google Classroom** — 46 tools: courses, assignments, grading, rosters, Drive |
| [Kimmahone/edu-workspace-mcp](https://github.com/Kimmahone/edu-workspace-mcp) | **MIT** | 1 | **Google Workspace for Education** — Classroom *plus* Docs, Sheets, Slides, Forms, Drive (29 tools) |
| 🆕 [bruchris/canvas-lms-mcp](https://github.com/bruchris/canvas-lms-mcp) | **MIT** *(`1 070` B, `p274`)* | — | **Canvas, with the consent problem solved at the tool boundary** — courses, assignments, submissions, rubrics, quizzes; grade and comment. 🟢 **Ships an opt-in FERPA mode that PSEUDONYMISES student names and contact details before tool output reaches the model.** The one row on this shelf that answers the blocker the market actually states (`T45`) |
| 🆕 [RohanMuppa/brightspace-mcp-server](https://github.com/RohanMuppa/brightspace-mcp-server) | **MIT** *(`1 068` B, `p274`)* | 59 | **Brightspace / D2L** — grades, assignments, rosters. **A fourth LMS this table never listed**; two declared derivatives and a Rust implementation sit beside it on [`trending.md`](trending.md) |
| 🆕 [felipedias-ie/blackboard-mcp](https://github.com/felipedias-ie/blackboard-mcp) | **MIT** *(`1 084` B, `p274`)* | 1 | **Blackboard Ultra** — courses, content, grades, deadlines. 🔴 **`intel/market.md` tells a studio to pitch REPLACING Blackboard. It has an MIT doorway** — the error `p267` corrected for Canvas, left standing for the other NA higher-ed incumbent |
| 🆕 [NiccoloSalvini/mcp-blackboard-ucsc](https://github.com/NiccoloSalvini/mcp-blackboard-ucsc) | **MIT** *(`1 073` B, `p274`)* | 0 | **Blackboard over the PUBLIC REST API** — no institutional plugin to get approved, which is the cheapest pilot shape on this table |
| 🆕 [blend-ed/tutor-contrib-openedxmcp](https://github.com/blend-ed/tutor-contrib-openedxmcp) | 🔴 **AGPL-3.0** *(`34 524` B, `p274`; default ref `master`)* | 1 | **Open edX** — 33 tools, Tutor plugin + a Django facade at `/api/mcp/`. **A sixth platform.** ⚠️ AGPL **and** `/health` unauthenticated: price the network clause and fix the endpoint before any pilot |
| [pengusto/google-classroom-mcp](https://github.com/pengusto/google-classroom-mcp) | **MIT** | — | **Google Classroom** — a correctly-attributed fork of `adriasantacreu` (dual copyright in the payload) |
| [alanmagno1/google-classroom-mcp](https://github.com/alanmagno1/google-classroom-mcp) | **MIT** | 0 | **Google Classroom** — multi-account; Spanish About line, English README |
| [OmarNiazi/classroom-mcp](https://github.com/OmarNiazi/classroom-mcp) | **MIT** | 0 | **Google Classroom** — student-side, read-only by construction |
| [praisethefacts/google-classroom-mcp](https://github.com/praisethefacts/google-classroom-mcp) | **MIT** | — | **Google Classroom** — read-only courses, coursework, rosters, submissions |
| [faizan45640/google-classroom-mcp-server](https://github.com/faizan45640/google-classroom-mcp-server) | **MIT** | — | **Google Classroom** — readonly scopes; oldest copyright line in the family (2025) |
| [AStheTECH/mewcp-google-classroom](https://github.com/AStheTECH/mewcp-google-classroom) | ⚠️ **proprietary** | — | **Google Classroom** — same description, bespoke all-rights-reserved licence |

**The distinction that matters commercially:** `anki-mcp-server` and `tutor-mcp` reach *study
tooling*, which the learner owns. The Canvas, Moodle and Google Classroom servers reach the
**institution's system of record**, which is where the client's data, roster and grades actually
live. That is the difference between a demo and an engagement.

**And the three systems of record are not equally served — openness and adoption point in
opposite directions.** Pass 268 measured the third one:

| LMS | servers found | best licence | best adoption | what that means for a quote |
|-----|---------------|--------------|---------------|------------------------------|
| **Canvas** | 2 | **MIT** (payload) | **295★ / 1,026 commits** | One obvious choice, maintained, university-named. Quote it. |
| **Moodle** | 1 | AGPL-3.0, **open-core** | 1★ / 57 commits | One choice, and you pay twice (network clause + premium tools sold separately). |
| **Google Classroom** | **8** | **MIT** (payload, on 6 of 8) | **2★ / 11 commits** at best | **The most servers and the least adoption anywhere on this shelf.** Seven permissive implementations of the same idea, none of them maintained by anyone but its author, and one proprietary impostor among them. |

🔵 **Read that table as a supply signal, not a scoreboard.** A category with eight competing
MIT implementations and no adopted one is not a solved problem — it is an **unconsolidated** one.
For Canvas you adopt; for Google Classroom you **fork the closest server and own it**, and you
price the maintenance, because nobody upstream is carrying it. Do not promise "Google Classroom
support" on the strength of a repository count.

⚠️ **Scope warning specific to the Google Classroom family, and it is the biggest in this file.**
`canvas-mcp` reaches a course API. `Kimmahone/edu-workspace-mcp` reaches **Docs, Sheets, Slides,
Forms, Drive and Classroom** — a whole Google Workspace for Education tenant. The OAuth consent a
pilot asks a school for is therefore far wider than the feature being piloted, and
`OmarNiazi/classroom-mcp`'s own README states *"Google hasn't verified this app."* In EMEA that is
a GDPR conversation before it is an engineering one; in the US it is a FERPA/COPPA one. **Scope the
consent to the tools you enable, and say so in the SOW.**

### Assessment, grading and feedback
**Artemis** (MIT, TU Munich) is the starting point when assessment is the deliverable: automated
build-test-analyse on programming submissions, **Athena** for text/modelling feedback, and
human-in-the-loop by construction. **Numbas** (Apache-2.0, Newcastle) when assessment must run
**entirely in the browser** — no student submission leaves the device, which answers a data-residency
objection before it is raised. **nbgrader** (BSD-3-Clause) for notebook-based courses. Note Athena's
unverified licence above.

### Knowledge tracing / learner modelling
Not agents but the models underneath them — see [`repos/foundations.md`](../repos/foundations.md):
`pykt-toolkit`, `pyedmine`, `EduStudio`, `EduData`.

## Provenance correction — the top row on this shelf is APAC-origin

This file previously declared that **no APAC-origin education agent had surfaced**. That claim
was false against this file's own first row.

`HKUDS/DeepTutor`'s README states the project is *"led by Bingxi Zhao within the **HKUDS
Group**"* and thanks the *"director of the **Data Intelligence Lab @ HKU**"*. HKUDS is the
Data Intelligence Lab at the **University of Hong Kong**. The single most-adopted education
agent in open source — **41.5k stars, Apache-2.0** — is APAC-origin, and so is much of the
learner-modelling layer beneath it: `bigdata-ustc/EduData` (University of Science and
Technology of China) and `HFUT-LEC/EduStudio` (Hefei University of Technology), both named in
their own GitHub org handles.

**Evidence grades, stated honestly:** DeepTutor's affiliation is **payload-quoted** from the
repository README. EduData's and EduStudio's are **org-handle** evidence — the institution is
named in the handle, not in a payload. For `pykt-team/pykt-toolkit` and `ZhijieXiong/pyedmine`
no affiliation statement was located this pass, so no provenance is claimed for them.

**Why this matters commercially:** "APAC is supply-poor in education AI" would have been
briefed into APAC engagements as a reason to import a stack. The opposite is closer to true —
APAC is where the research supply lives. What APAC has not produced is a **platform** (see
[`verticals/solutions.md`](../verticals/solutions.md)), which is a far narrower gap and points
at integration work rather than wholesale import.

## Declared gaps

- 🟢 **RETRACTED in pass 286 — "no AFRICAN-ORIGIN permissively licensed education agent" is no
  longer the claim.** [`Tanzania-AI-Community/twiga`](https://github.com/Tanzania-AI-Community/twiga)
  is **MIT** (`development/LICENSE`, 1 073 B, read first-hand), 230 files, Tanzania Institute of
  Education curriculum, with tests, migrations, monitoring and CI; `vincent-laizer/NECTA-API` is
  **MIT** on the results channel. 🔵 The claim below held for 17 passes because every leg that
  produced it addressed **West Africa or "Africa"**; the one addressed to **Tanzania by exam board
  and language** refuted it immediately. What remains true, narrowed: **no permissively licensed
  education agent of WEST AFRICAN origin** — five rows there, five without a grant.
- 🔴 **Superseded text, kept for the record (pass 269) — no AFRICAN-ORIGIN permissively licensed
  education agent, measured at the
  payload.** Both African-context agents located this pass serve no grant (above). The only
  Africa-engaged permissive code this base carries is
  [`AI-for-Education`](https://github.com/AI-for-Education) — MIT, LMIC-focused, Sierra Leone MBSSE
  lesson plans and Luganda benchmarks — and it is **research-grade at 1–12★**, not a deliverable.
  🔵 **Two named systems remain unreachable rather than absent:** Nigeria's **Naija Teacher AI**
  (UNESCO SDG4 case study, offline-first, target 1.5M teachers by Q3 2026) states **no licence** and
  publishes no repository this pass could find; Kenya's **Kytabu SOMANASI** is **proprietary**.
  **State it as "unreachable", not "nonexistent" — the distinction is what a client's own ministry
  contacts can change.**
- **RETRACTED in pass 266 — "no LATAM-origin education agent" is no longer the claim.**
  [`guedesindev/ai_tutor_forge`](https://github.com/guedesindev/ai_tutor_forge) (GPL-3.0,
  payload-verified, 18★) is a Portuguese-language education agent, now on the restricted
  shelf above. **But state the evidence at its real grade:** the README, file descriptions
  and interface are in Portuguese, and the repository page does **not** state the author's
  country — this is *language* evidence, weaker than the org-handle evidence used for EduData
  and far weaker than DeepTutor's payload-quoted affiliation. So "LATAM-origin" is not
  asserted; "Portuguese-language" is. **The defensible gap is now: no Spanish- or
  Portuguese-language education agent with adoption.** LATAM's real open-source education
  supply remains the platform layer — `portabilis/i-educar` and `i-diario`, actively
  maintained Brazilian systems, both committed to in October 2026.
- **Star-sorted search cannot see publicly-funded code — the instrument, not the world.**
  Pass 265 concluded that fourteen permissive rows "is the size of this category today". Pass
  266 added three MIT rows (Artemis, Iris, Pyris) and an MIT national platform
  (`Sunbird-Ed/SunbirdEd-portal`, **41★ against 38,046 commits**) without a single new search
  term — by probing named projects directly. Every agent and repo leg this KB runs sorts
  GitHub topics **by stars**, and a ministry-funded project accrues commits, forks and
  deployments but almost no stars. **Rank the platform layer by commits and forks; probe
  national-programme names by hand.** See [`repos/trending.md`](../repos/trending.md).
- **REVISED in pass 266 — the grading gap was a question about the wrong shape of thing.**
  There is still no standalone education grading *agent repo* with adoption (`MUJINN/question-marking`
  and `MUJINN/intelligent-correction` remain single-digit-star). But the *function* is served,
  permissively and at university scale, by a platform **this base already had on its own
  foundations shelf**: **[`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) is MIT**,
  819★, 12,437 commits — `repos/foundations.md` has carried it as "the strongest MIT-licensed
  teaching platform" while *this* file called the category empty. New in pass 266 is what it
  ships: **Athena** (automated feedback for text, modelling and programming), **Iris** (LLM
  tutor) and **Hyperion** (AI exercise authoring on Spring AI). Beside
  it: `jupyter/nbgrader` (BSD-3-Clause, 1.4k), `autolab/Autolab` (Apache-2.0, 808, CMU-origin)
  and `numbas/Numbas` (Apache-2.0, 215, Newcastle, browser-only execution). **Caveat that
  changes procurement:** Athena's own repo serves **no licence payload** — the MIT grant covers
  Artemis, not necessarily Athena. Get it in writing before it ships in a deliverable.
- **`mcp-server-education` as a GitHub topic is empty** — "hasn't been used on any public
  repositories, yet" — while **12 distinct education MCP server slugs are shelved in this file**
  (11 permissive + 1 all-rights-reserved; counted from the rows by pass 272, which found
  `intel/trends.md` still carrying **"five"** — see `T37`) (pass 267 added the
  two LMS-side ones; pass 268 added seven permissive Google Classroom servers and one proprietary
  one). **The gap got four times worse in two passes, which is the point:** the index is not
  lagging the category, it is structurally disconnected from it. The category is real and unlabelled; that is a naming gap, and a
  small opening for whoever labels it first. **Note what it cost to find them:** the topic index is
  empty, so they were located through a web search for *"MCP server Moodle Canvas LMS"* and then
  payload-verified by hand. A topic-listing leg will keep reporting this category as non-existent.
- **The Spanish-language gap was re-tested in Spanish this pass, and it holds.** A search leg run
  in Spanish — *"github tutor IA educación código abierto español 2026 repositorio"* — returned **no
  Spanish-language education agent repository at all**: the results were GitHub Education marketing
  pages, a 2019 Universidad Politécnica de Madrid paper on teaching with Git, and unrelated blog
  guides. So the gap is not an artefact of searching in English. The nearest thing located is
  [`admin978/canvas-mcp`](https://github.com/admin978/canvas-mcp) (MIT, 4★), *"Built by AGENTE 404
  S.L."* — a **Spanish company form**, but its README is in English and **no country is stated**,
  which is weaker evidence than the Portuguese-language `ai_tutor_forge` row above. **Standing
  claim, unchanged: no Spanish- or Portuguese-language education agent with adoption.**
- **Pass 268 tested the Spanish gap a third way — against a family of eight, not a query — and it
  still holds.** The Google Classroom MCP family contains
  [`alanmagno1/google-classroom-mcp`](https://github.com/alanmagno1/google-classroom-mcp), whose
  **About line is in Spanish** (*"Servidor MCP para Google Classroom: cursos, tareas pendientes,
  entregas y materiales desde Claude"*) — and whose **README is in English**. The most capable
  server in the family is by an author with a Catalan name, and **its README is in English too,
  with no country stated.** 🔵 **The nearest-miss evidence has therefore got *weaker*, not
  stronger:** `ai_tutor_forge` had a Portuguese README; this has a Spanish *metadata field*.
  Record the grade and do not let a Spanish sentence in a sidebar become a LATAM or Iberian
  provenance claim in a deck.
- **🆕 A Korean-language education agent now exists at payload grade, and that is a new APAC
  datum.** [`Kimmahone/edu-workspace-mcp`](https://github.com/Kimmahone/edu-workspace-mcp) (MIT,
  payload) has a **Korean README**, references **Korean curriculum standards**, and implements
  `docs_import_hwp` / `docs_export_hwpx` — HWP/HWPX being Korea's national document formats, which
  is implementation evidence rather than prose. **Graded exactly as `ai_tutor_forge` was: LANGUAGE
  evidence.** No country and no institution is stated, so "Korea-origin" is **not** asserted;
  "Korean-language, Korean-format-aware" is. It pairs with South Korea's **AI Basic Act, in force
  22 January 2026** — the one APAC jurisdiction with a comprehensive statute — so the language
  supply and the regulatory demand have appeared in the same country in the same year.

## Pass 270 note — this table gains no rows, and the reason is a measurement

🟢 **Zero agents were added this pass, and nothing was added to meet the brief's five-row minimum —
the table above clears it many times over.** This is the **fifth consecutive measured nil return**
on the education-agent supply channel.

**What was and was not searched, so the absence is informed rather than silent:**

| leg | run? | why |
|---|---|---|
| `top open source AI agents education 2026 github MIT` | 🔴 **no** | measured **saturated across four passes**; `p269`'s standing instruction is to spend the generic legs **last, not first**. A fifth identical measurement buys nothing. |
| `github trending education AI 2026` | 🔴 **no** | same |
| `open source platform education ERP / CRM / SIS` | 🔴 **no** | same |
| `curriculum abierto IA primaria ... licencia MIT GitHub 2026` *(Spanish)* | 🟢 **yes** | `Gap 367`'s one unspent language limb |

🔴 **The Spanish leg's yield: nine repositories, eight of them university student course
portfolios** (`ia-aplicada-2026` and forks, `InteligenciaArtificial`, `proyecto_ia`, `cursoIA2026`)
**and the ninth already on this base** ([`nmarafo/OpenDidactia`](https://github.com/nmarafo/OpenDidactia),
CC BY-SA 4.0 at payload — `p268`'s slug gate caught it). **No row qualified.**

🟢 **`Gap 367` therefore holds in a fourth language** — Hindi and Chinese (`p269`), Spanish (`p270`),
and English throughout. **There is still no permissively licensed primary-band AI-literacy
curriculum.** 🔵 The nearest permissive primary-band artefact,
`DECK6/korean-elementary-learning-map` (**MIT**), is an ontology of a primary **curriculum**, not a
primary **AI-literacy course** — a distinction that decides whether it answers the gap, and it
does not.

🟢 **One falsifiable limb remains and it costs an email:** `datawhalechina/ai-edu-for-kids` carries
CC-BY-NC-SA-4.0 as **organisational template boilerplate**, not as a decision (`p269`, `T27`) — so
it is the licence on this base **most likely to move if asked.**

## Pass 269 — the African agent tier exists, and the question it answers is not the one that was asked

Pass 267 instructed *"Kenya, Nigeria, South Africa and Egypt as four separate queries, never
paired"*, and pass 268 restated it as the cheapest fix for **"EMEA means Europe in this base."**
Pass 269 ran it. Four legs, four substantive returns — and on the **agent** shelf specifically, the
result is sharper than "nothing found".

🟢 **Two African-context education agents are now located and graded**, which is two more than this
base has ever carried: [`muskvdc/EduTwin-Africa`](https://github.com/muskvdc/EduTwin-Africa) (South
Africa, Grades 8–12) and [`Valexxy/edunaija-os`](https://github.com/Valexxy/edunaija-os) (Nigeria).
Both are in the licence-UNVERIFIED table above, because **neither serves a grant on any channel** —
no payload on 19 paths, and no `license` field in the package metadata either.

🔴 **The gap's grade therefore goes UP, not away.** This base previously recorded, in
[`agents/trending.md`](trending.md), that an Africa-focused leg *"returned no repository-level asset
— only a training provider, not code."* That was a **search-level** absence. Pass 269 replaces it
with a **payload-level** one: the repositories exist, they were resolved by ref, probed on 19 paths
and read in their metadata, **and the grant is missing in both.** 🔵 **An absence measured at the
payload is a different and stronger claim than an absence measured at the query**, and it is the one
to brief: *"there is African-built education-AI code, and none of it is licensed for you to ship."*

🟡 **The two rows fail differently, and the difference is the actionable part.** `edunaija-os` is
simply silent. `EduTwin-Africa` ships the **placeholder text** — *"Add the project's chosen license
here before publishing"* — which means its author has already written down that the grant is
missing. **That is the one row on this shelf where a request has a plausible answer**, and it costs
an email rather than a fork. Contrast [`ls1intum/Athena`](https://github.com/ls1intum/Athena), which
has survived 76 path/ref probes in silence across three passes.

🔵 **And a naming hazard worth one line in any proposal.** `Valexxy/edunaija-os` is **not** the
EduNaija AI Tutor published at ACL AfricaNLP 2026 (DOI `10.18653/v1/2026.africanlp-main.11`) — that
is a five-agent LangChain + FAISS system with English/Yoruba/Hausa/Igbo support, **whose code this
pass could not locate at all**. The repository that shares its name is a starter codebase for a
different thing. **The paper is not the repo, and the repo is not the paper.**

## Pass 268 provenance note — Iris and Pyris are MIT at PAYLOAD grade, and serve no README

Both rows were re-probed this pass because `P17` in [`compose/patterns.md`](../compose/patterns.md)
now depends on them.

🟢 **The grant is stronger than this file previously recorded.** Both
[`ls1intum/Iris`](https://github.com/ls1intum/Iris) and [`ls1intum/Pyris`](https://github.com/ls1intum/Pyris)
serve **MIT at `main/LICENSE`**, and the copyright line reads **"Copyright (c) 2023 TUM Applied
Software Engineering"** — so TU Munich provenance for these two is **payload-quoted**, not
README-quoted, which is a grade *above* the evidence this file carries for Artemis itself.

🔴 **And a defect worth recording: neither repository serves a README.** `README.md`, `readme.md`,
`README.rst` and `README` were all probed across `main`/`master`/`develop` — **404 on every
combination**, while `LICENSE` returns 200 on `main`. The descriptions in the rows above therefore
have **no source inside these repositories**; they derive from the Artemis documentation. 🔵 **Record
it rather than quietly relying on it:** a row whose capability claims cannot be traced to its own
repository is fine to build on and wrong to quote verbatim to a client. Confirm Iris's pedagogical
constraints against the Artemis docs, or against a deployment, before they reach a proposal.
