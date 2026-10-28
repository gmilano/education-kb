---
industry: education
region: Global
updated: 2026-10-28
---

# Compose patterns — concrete education AI recipes

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it with **`P491-1`**, which supersedes `P490-6`. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/patterns.md`](../archive/2026-10-27-p490-pre-rewrite/patterns.md).

Every component below is a row verified this pass in [`agents/top.md`](../agents/top.md),
[`repos/foundations.md`](../repos/foundations.md) or
[`verticals/solutions.md`](../verticals/solutions.md) — real repo, license read from bytes at a
pinned SHA.

**Read the licence column as a deployment constraint.** A pattern marked 🟢 can ship as a closed
hosted derivative. A pattern marked 🔴 cannot, and the obligation is named.

---

## P490-1 — Canvas agent assistant for US higher ed 🟢

**Why:** Canvas dominates US higher ed and is the only incumbent LMS with a maintained agent tool
surface. Fastest path to a working engagement in the largest market.

| Component | Repo | License | Role |
|---|---|---|---|
| Tool surface | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | Canvas tools + 8 agent skills over MCP. 🔴 **Pin `v1.16.0` or later** (`p492`) — see the amended threat model below. Tool count is self-inconsistent upstream (102 vs 128): **do not quote one.** |
| Agent loop | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | code-writing agent runtime |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | quizzes, lesson plans, flashcards |

**Wiring:** run `canvas-mcp` against the institution's Canvas API token → expose as MCP tools to a
`smolagents` agent → `educhain` generates assessment items that the agent writes back through
`canvas-mcp`'s content tools.

**Do this or it is negligent:** start from `canvas-mcp`'s **read-only** tool subset
(`get_*`/`list_*`), enable write tools individually through its operator allowlist, and put a human
gate on anything that writes a grade. Its own source makes the point to honour: *a confirmation
token does not prove a human approved anything.*

🔴 **Amended `p492` — the threat model above was right and is no longer sufficient.** This pattern
previously named **one** advisory as the threat model. `v1.16.0` publishes **four**, and two of them
are not covered by tool scoping at all:

| advisory | subject | what it defeats |
|---|---|---|
| `GHSA-7mj9-4mcg-hvhv` | **Canvas token handling** | 🔴 **Read-only tool scoping does not protect the token.** This pattern hands the server an *institutional* Canvas API token — scoping tools limits what the agent may call, not what a token-handling defect exposes. |
| `GHSA-7pp5-29mw-9jq3` | **local code sandbox** | 🔴 Code execution reachable from an agent loop driven by **student-authored text**. |
| `GHSA-hmr8-mvr2-mvw5` | **file content fencing** | The advisory this pattern already carried. Upstream's words are *file content fencing*, not "prompt-injection path". |
| `GHSA-qf6c-jv93-38gv` | Windows download permissions | Low relevance on Linux hosting; still live. |

**Three additions to the build, not optional:**

1. **Treat the Canvas API token as the primary asset, not the tool scope.** Issue a **dedicated
   service token** scoped to the pilot faculty, hold it in a secret manager the agent process
   cannot read, inject at request time, and **rotate on a schedule set before go-live**. Never the
   institution's admin token.
2. **Isolate the runtime.** With a published sandbox advisory and `smolagents` *writing and running
   code* in this very pattern, the agent process runs in its own container with **no ambient cloud
   credentials** and egress restricted to the Canvas host and the model endpoint.
3. **Pin and watch.** Pin `canvas-mcp` to `v1.16.0`+ by tag, subscribe to its advisories, and
   re-read them at every engagement checkpoint. 🟢 It **has** a `SECURITY.md` and discloses — which
   is why four advisories is a sign of a project worth depending on, not one to avoid. **An
   education MCP server with zero advisories is unexamined, not safe.**

🔵 **Also `p492`:** this pattern's base **drifted** — HEAD moved from this KB's pinned
`32e5d1ca0175` to `830bc2ef8389`, with the licence **byte-identical at both SHAs** (MIT, 1 071 B),
so the change is **code-only**. Pin by release tag rather than tracking `main`.

🔴 **`p494` — and it drifted again, inside a single pass's own window.** `830bc2ef8389` →
**`47394125364b`**, observed ~30 minutes apart in the same pass and stable across three reads.
Licence **byte-identical at all three SHAs** (MIT, 1 071 B, `sha1 491fb891a4cf`), so every move so
far is code-only. 🔴 **Two moves in ~24 hours makes this the most volatile dependency in this KB,
and it is this pattern's base.** The instruction above is therefore not a preference but a
requirement: **pin `v1.16.0` or later by tag, never a branch HEAD** — a HEAD pin on this repo is
stale before the engagement's first sprint review, and `git ls-remote` will report drift that is
merely upstream's normal cadence. 🟡 **Advisory caveat:** the **four** advisories named below were
read by `p492` at `v1.16.0` and were **not** re-read at `47394125364b`. On a repo moving this fast
and carrying a **token-handling** advisory, **re-read the advisory list at the tag you actually pin,
before you deploy** — do not inherit this KB's count.

**Licence note:** Canvas itself is AGPL-3.0, but you are **integrating over its API, not
modifying it** — no obligation attaches. All three components above are permissive. 🟢

**Scope:** 4–6 weeks to a governed pilot on one faculty.

---

## P490-2 — EU-conformant tutor where Globant is the provider 🟢

**Why:** under the EU AI Act the vendor is the **provider** and carries the conformity duties.
Education tutoring that touches assessment or admissions is high-risk. The Digital Omnibus moved
that deadline to **2 Dec 2027** — but Article 50 transparency still bites **2 Dec 2026**.

| Component | Repo | License | Role |
|---|---|---|---|
| LMS base | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | the only permissive full LMS; closed derivative permitted |
| Tutoring engine | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | graph-RAG lifelong tutoring |
| Mastery model | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | Bayesian Knowledge Tracing — an *auditable* learner model |
| Governance substrate | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | governed, authoritative knowledge with provenance |

**Wiring:** OpenOlat holds courses and enrolments → DeepTutor serves tutoring over course
material → OATutor's BKT maintains per-skill mastery as the explainable learner state → KSoR
holds the authoritative curriculum so every tutor claim is traceable to a source.

**Conformity work that is the actual deliverable:**
1. **Article 50 content marking by 2 Dec 2026** — mark every AI-generated artefact. Nearest
   real deadline.
2. **Human oversight** on assessment and progression decisions; BKT is chosen over an opaque
   model precisely because a learner model that determines an educational path must be explainable.
3. **Technical documentation + logging** from day one — provider duties, not retrofits.
4. 🔴 **Ship no emotion recognition, attention tracking or sentiment detection.** Banned in
   education in the EU since 2 Feb 2025. Audit the roadmap for it.

**Licence note:** all four permissive — closed hosted derivative is clean. 🟢

**Scope:** 10–14 weeks. Verify Omnibus dates against EUR-Lex before contracting.

---

## P490-3 — Offline-first ministry deployment for LATAM / APAC 🟢

**Why:** LATAM shows the highest measured individual adoption (56% of Brazilian secondary
teachers vs 36% OECD; 92% of LATAM HE students) against the weakest institutional delivery (30%
satisfaction). Public money sits in ministry programmes, and connectivity cannot be assumed.

| Component | Repo | License | Role |
|---|---|---|---|
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | offline-first, the only permissive one |
| Lesson structure | [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | explorations with misconception handling |
| Study-pack generation | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | source → quizzes + flashcards + SRS |
| SRS scheduling | [ankitects/anki](https://github.com/ankitects/anki) | AGPL-3.0 | **reference only — see note** |

**Wiring:** generate study packages **centrally, online** with `Skill-Anything` over the
ministry's approved curriculum → ship them into Kolibri's offline content channels → Oppia
explorations carry the interactive remediation → spaced repetition schedules review locally with
no network.

**The licence line that matters:** Kolibri, Oppia and Skill-Anything are permissive 🟢. **Anki is
AGPL-3.0** — use it as an *algorithm reference* and implement the scheduler, or accept the AGPL
obligation. Do not vendor Anki code into a closed deployment. 🔴

**Regional fit:** Portuguese/Spanish first. Align to the **UNESCO Observatory on AI in Education
for LATAM & the Caribbean** (launched 14 Apr 2026) and the **CONALEP/DGETI** centre-of-excellence
pilot in Mexico. Note there is **no LATAM AI statute** to sell conformity against — sell delivery.

**Scope:** 8–12 weeks per ministry pilot; content pipeline is the long pole, not the app.

---

## P490-4 — Jurisdiction-routing provenance layer for APAC 🟢

**Why:** APAC is the fastest-growing region (35.3% CAGR) with the least public resistance, but
four incompatible regimes. Content labelling is **mandatory in China and India**, absent in
**Japan**, and South Korea's AI Basic Act has been binding since **22 Jan 2026**. One product
must behave differently per market.

| Component | Repo | License | Role |
|---|---|---|---|
| Agent loop | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | runtime |
| Provenance / authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | source-of-truth + provenance records |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | material generation |
| Platform | [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | delivery |

**Wiring:** every generated artefact gets a KSoR provenance record at creation. A policy module
keyed on deployment jurisdiction then decides the output treatment:

| Market | Behaviour required |
|---|---|
| India | prominent AI label + provenance marker (live **20 Feb 2026**) |
| China | AI-content label + service **filing** before launch |
| South Korea | AI Basic Act obligations (binding **22 Jan 2026**) |
| Japan | no binding duty — label anyway, cost is zero |

**Beachhead:** South Korea for a compliance-first pitch (only comprehensive mandatory APAC law);
India for volume.

**Licence note:** all permissive. 🟢 **Scope:** 12–16 weeks across three markets.

---

## P490-5 — Policy-configurable K-12 assistant for the US patchwork 🟢

**Why:** ~34 states plus DC and Puerto Rico have AI guidance, and the enacted laws demand
*different* things. One assistant with per-district policy configuration beats 34 forks. There is
**no federal law** — H.R. 8747 advanced in committee only, so do not plan around it.

| Component | Repo | License | Role |
|---|---|---|---|
| LMS base | [Selleo/mentingo](https://github.com/Selleo/mentingo) | **MIT** | AI-native LMS; multi-tenant via Postgres RLS |
| Content generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | lesson plans, assessments |
| Mastery model | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT, explainable |
| Canvas bridge | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | where the district runs Canvas |

**Wiring:** `mentingo`'s Postgres **row-level security** is the load-bearing choice — tenant
isolation is enforced in the database, not in application code, so a district is a tenant and its
policy settings cannot leak across. Each tenant carries a policy record:

| Policy toggle | Driven by |
|---|---|
| Parent opt-out | Oklahoma **S.B. 1734** |
| AI-literacy standards + mandatory local policy | Idaho **S.B. 1227** |
| State guidance alignment | Maryland **S.B. 720** |
| Grade-band restriction (e.g. no genAI for K-6) | district rule — Katy ISD pattern |
| Human-oversight gate on high-stakes decisions | recurring across states |
| "Learning aid, not submitted work" | Columbia Law pattern (HE) |

**Licence note:** all four MIT 🟢 — closed hosted derivative is clean, which matters since this is
a SaaS-shaped product.

**Scope:** 6–10 weeks to a two-district pilot.

---

## P490-6 — Open education-AI evaluation harness (build, not compose) 🟡 **— superseded by `P491-1`**

🔵 **Superseded.** Its premise — that *no* education-AI evaluation instrument exists — was refuted
in `p491`: two real benchmarks exist, and they are **unlicensed**. Use **`P491-1`** below, which
keeps this pattern's scoring design but rebases the runtime on a permissive harness instead of
building one. Kept here because the component wiring below is still sound and the two patterns
differ only in their base.

**Why:** this is the sector's largest structural gap. Nobody can currently demonstrate that an AI
tutor improves outcomes. Buyers in all four regions are starting to ask, and EU high-risk
conformity will require evidence by **2 Dec 2027**.

| Component | Repo | License | Role |
|---|---|---|---|
| Ground-truth mastery | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT as the reference learner model |
| Item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | generate assessment items at volume |
| Curriculum authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | authoritative answer keys with provenance |
| Harness runtime | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | drive candidate tutors under test |
| Subject under test | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | first candidate |

**Wiring:** KSoR holds curriculum + answer keys → `educhain` generates held-out item banks →
`smolagents` drives each candidate tutor through simulated learner trajectories → OATutor's BKT
scores mastery gain against the key → report per-skill learning gain, not token overlap.

🟡 **Marked amber deliberately:** unlike P490-1 to P490-5 this composes no existing harness,
because none exists. It is a build on permissive parts. That is also why it is the strongest
differentiator in this file — and it would close the gap this KB has carried for dozens of passes.

**Licence note:** all permissive. 🟢 Could be published as open source as a credibility asset.

**Scope:** 10–14 weeks for v1 on one subject domain.

---

## P491-1 — Tutoring-quality eval harness on a permissive base 🟢 *(supersedes `P490-6`)*

**Why:** `p491` established that the instruments for measuring tutoring quality **exist and carry
no license** — [`mathtutorbench`](https://github.com/eth-lre/mathtutorbench) (45★, EMNLP 2025 Oral)
and [`TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) (0★, KAIST) both ship **no grant
file**, and MathTutorBench's README contradicts itself (`CC BY 4.0` badge vs `CC BY-SA 4.0` text,
neither a software grant). So the research is public and the **code and data are not takeable**.
That is a licensing blocker, not a scarcity one, and it has a clean route around it.

| Component | Repo | License | Role |
|---|---|---|---|
| Harness runtime | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** (1,066 B @ `d6de81643928`) | task registry, model adapters, runners, reporting — 14,300★, the de-facto standard |
| Ground-truth mastery | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | BKT as the reference learner model |
| Item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | held-out item banks at volume |
| Curriculum authority | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | answer keys with provenance |
| Learner simulation | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | drive simulated learner trajectories |
| Subject under test | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | first candidate tutor |

**Wiring:** implement each pedagogical dimension as a **native `lm-evaluation-harness` task** —
that is the one decision that makes this reusable, because it inherits the harness's model
adapters, caching, reproducible task versioning and result format for free, and anything scored
this way is comparable against general-model baselines. Then: KSoR holds curriculum and answer
keys → `educhain` generates held-out item banks → `smolagents` drives simulated learner
trajectories against the candidate tutor → OATutor's BKT scores **per-skill mastery gain** against
the key → the harness emits the report. Score learning gain, never token overlap.

**The license line that makes this work — read it before writing any code:**

1. 🟢 **Every component above is MIT or Apache-2.0.** The output is a clean closed or open
   deliverable, your choice.
2. 🔴 **Do not vendor `mathtutorbench` or `TutorCaseBench` code or data.** No grant means no
   rights — not permissive-by-default. Cloning for private reading is one thing; shipping their
   code or redistributing their datasets in a client deliverable is another.
3. 🟢 **Reimplement the *task designs* from the papers** (arXiv 2502.18940 for MathTutorBench;
   TutorCaseBench's 5 challenge types). Benchmark methodology published in a paper is readable and
   reimplementable; that is what papers are for. Cite both.
4. 🟢 **Ask the authors to add a license.** Both are academic groups (ETH LRE, KAIST kixlab) and an
   MIT or Apache-2.0 grant is usually a five-minute decision nobody got around to. An upstream
   license would convert this whole pattern from a build into a compose — the highest-leverage
   email in this file.

**Why it is worth building anyway:** EU high-risk conformity needs **evidence of educational
efficacy** by **2 Dec 2027** (`P490-2`), and no buyer in any region can currently get it. A
published, permissively-licensed tutoring-eval harness is a credibility asset that also doubles as
the measurement layer under every other pattern here.

**Scope:** 8–12 weeks for v1 on one subject domain — shorter than `P490-6`'s 10–14, because the
runtime, model adapters and reporting are no longer yours to write.

---

## Patterns deliberately **not** offered

- **Nothing on Moodle or Open edX at the agent layer.** Neither has an MCP/tool surface at a
  usable star floor; the connector is unbudgeted build work. Use P490-1 (Canvas) where possible
  and price the connector explicitly otherwise.
- **No closed SaaS on an incumbent LMS fork.** Moodle is GPL-3.0; Open edX, Canvas, Frappe LMS,
  Tutor **and LearnHouse** (`p491`, 2,400★) are **AGPL-3.0** — hosting a modified copy owes source
  to users. Only OpenOlat, Kolibri, Oppia and mentingo support that shape.
- **Nothing on `frappe/education`** (`p491`, 682★) despite it being a genuine school-management
  base: its grant is a **19-byte stub** naming GPL v3 with no license text, so it is copyleft *and*
  its paperwork will not survive a client's legal review. Named so the omission is visible.
- **Nothing built on an unlicensed benchmark.** `mathtutorbench` and `TutorCaseBench` are the two
  best education-AI instruments in existence and **neither can be composed** — see `P491-1`.
- **No closed SIS or assessment product.** Every SIS found (`rosariosis` GPL-2.0, `GibbonEdu`
  GPL-3.0, `openeducat_erp` LGPL-3.0) and the only real assessment engine (`tao-core` GPL-2.0)
  are copyleft. There is no permissive base — it is a ground-up build.
- **Nothing using `ChatTutor` (AGPL-3.0) or `tutor-gpt` (GPL-3.0)** in a hosted commercial
  pattern, despite both being capable. Named here so the omission is visible rather than silent.


## 🆕 `P492-1` — Grading assistant whose arithmetic the model never touches 🟢

**Why:** every high-risk education regime now converging on the same functional trigger —
**automated assessment or ranking of learners** (EU Annex III; Vietnam Decision `33/2026/QD-TTg`,
3 education systems of 46) — demands demonstrable human oversight from the **provider**. And
[`intel/market.md`](../intel/market.md) establishes that **for a Globant-built education AI system,
Globant is the provider.** The cheapest way to fail a conformity assessment is to let an LLM
compute a grade total.

| Component | Repo | License | Role |
|---|---|---|---|
| Reference design | [vulinh1704/ai-tutor-agent](https://github.com/vulinh1704/ai-tutor-agent) | MIT | 🔵 **read, do not depend** (0★, 13 commits) — the rubric/leak-guard/thread architecture below |
| Agent runtime | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **MIT** (1 072 B, `sha1 73a6ebe3bd93` @ `eb8ec111b3e9`) | explicit per-session thread with checkpointed state |
| Rubric item generation | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | generates the rubric criteria and assessment items |
| LMS write-back | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | **`v1.16.0`+**, write tools behind a human gate |
| Quality harness | [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 🔴 **no software grant** | 🔵 measure against it; **do not vendor it** — see [`agents/top.md`](../agents/top.md) |

**Wiring — the whole point is the split:**

1. `educhain` emits the **rubric** (criteria + weights + max points) as data, reviewed by a human
   **once per assignment**, then frozen and version-pinned.
2. The model is asked for **per-criterion structured output only** — a score and a feedback string
   per criterion, validated against the frozen rubric schema with Pydantic. **A response that does
   not validate is rejected and retried, never coerced.**
3. 🟢 **The total is computed in Python from the validated per-criterion scores.** The model is
   never asked for, and never shown, a total. This is the single load-bearing decision.
4. **Socratic mode gets the answer-leak guard:** a draft hint that reveals the answer is
   regenerated under a stricter instruction; if it still leaks, a safe canned hint replaces it.
   Hints escalate one level at a time.
5. Session state is an **explicit LangGraph thread** (SQLite for a pilot), so every grade carries a
   replayable trace — which is what an oversight duty actually asks for.
6. `canvas-mcp` writes the grade back **only after a human gate**, per `P490-1`'s amended rules
   (dedicated scoped token, isolated runtime, pinned release).

**What makes this conformant rather than merely careful:** the arithmetic is deterministic and
auditable, the rubric is human-approved before any student is graded, every score decomposes to a
criterion with a rationale, and the trace is replayable. 🟢 **An EU-conformant build of this
transfers to Vietnam with little rework** — the functional trigger is the same, which is why this
KB's standing advice is to build conformity **once, in EMEA shape, and reuse it**.

🔴 **Do not propose the reference repo as a dependency.** One author, 13 commits, zero stars, no
security process. Its value is that it is a **1 071-byte MIT grant over an architecture worth
copying** — the first open implementation of advice this KB has given for several passes without
being able to point at code.

🔵 **Honest gap:** `mathtutorbench` measures tutoring quality and **ships no software licence**
(its own README names two different Creative Commons variants, neither a software grant). Use it as
an **external yardstick you run against**, never as vendored code. There is still **no usable
open-source education-AI evaluation harness** — see `T11`.

**Scope:** 5–7 weeks to a governed pilot on one course, including the rubric-freeze workflow and
the oversight trace. Add 2–3 weeks if the conformity documentation is a deliverable.

---

## 🆕 `P493-1` — The first end-to-end **all-permissive** education stack 🟢

**Why:** every stack this KB has been able to propose crossed a copyleft boundary somewhere —
usually at the platform layer, which is why `T2` called that *the binding constraint*. `p493`
restored eight addresses that earlier passes had promoted and later rewrites deleted (see
[`agents/trending.md`](../agents/trending.md) `p493`), and with them **a complete stack exists in
which every component is MIT, Apache-2.0 or BSD-3-Clause.** For a client who cannot accept
copyleft — a commercial derivative, a hosted multi-tenant product, an OEM arrangement — this is the
difference between "we must talk about AGPL" and "we do not".

| Component | Repo | License | ★ | Role |
|---|---|---|---|---|
| Courseware / classroom | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | 41,700 | Topic or document → multi-agent interactive lesson: slides, quizzes, project-based work |
| Teacher workflow | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | **Apache-2.0** | 595 | Lesson planning + differentiation skills **with their eval rubrics** |
| Teacher workflow (twin) | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | **Apache-2.0** | 40 | Consortium-side payloads + `evals/` rubrics for pedagogy, rigour, format, scaffolding |
| Tutoring platform | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | Collaborative tutoring platform where ChatTutor (AGPL-3.0) was the only option |
| Quality gate | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | **MIT** | 13 | 1,143 teacher-exam items (920 CDPK / 223 SEND), 100+ models |
| Eval runtime | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | **MIT** | 14,300 | the harness `pedagogy-benchmark` runs on |
| Academic integrity | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | 355 | Source-code plagiarism detection; 3,865 commits |
| Delivery — offline | [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | 1,200 | runs without connectivity |
| Delivery — no app | [Orenda-Project/rumi-platform](https://github.com/Orenda-Project/rumi-platform) | **Apache-2.0** | 18 | WhatsApp, 15 languages |
| Institutional layer *(only if needed)* | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | 448 | enrolment, roles, gradebook — **the only permissive full LMS** |

**Wiring:** `OpenMAIC` generates the courseware and runs the classroom experience → the two
teacher-skill packs drive lesson planning and differentiation at the teacher's desk (a skill pack
has **no runtime**, so nothing is hosted and no data-residency posture attaches to it) →
`open-tutor-ai-CE` carries the 1:1 tutoring surface → `dolos` sits on submitted code →
`pedagogy-benchmark` on `lm-evaluation-harness` runs as a **release gate in CI**, not as a one-off
report → `Kolibri` or `rumi-platform` carries delivery where connectivity is not assumable →
`OpenOLAT` underneath **only** where the engagement genuinely needs enrolment, roles and a
gradebook.

**Do this or it is negligent:**

1. 🔴 **`OpenMAIC` is not an LMS and must not be sold as one.** Nothing on its page claims
   enrolment, a gradebook, SIS integration or institutional roles. If the client needs those, the
   permissive answer is `OpenOLAT` beneath it — and if they need a **SIS** or a **QTI exam
   engine**, 🔴 **there is no permissive option at all** and the copyleft conversation is
   unavoidable. Say that in week one, not at UAT.
2. 🔴 **Pin every component by SHA or release tag and re-read the licence bytes at that pin.** This
   pattern's own evidence is why: `p493` found eight promoted rows deleted from this KB's shelves,
   and `p492` found `canvas-mcp` drifted with its licence byte-identical at both SHAs. Pins read at
   `2026-10-28`: `OpenMAIC` `70859b42e714` (MIT, 1 065 B), `k12-teacher-skills` `31fd6dbb0c07`
   (Apache-2.0, 11 357 B), `open-tutor-ai-CE` `196c547291da` (BSD-3-Clause, 1 531 B), `dolos`
   `74b101785bad` (MIT, 1 084 B), `pedagogy-benchmark` `21a43a395ab4` (MIT, 1 064 B),
   `agent-skills` `8b0599c24469` (Apache-2.0, 10 173 B), `rumi-platform` `f2d62af1eb82`
   (Apache-2.0, 11 287 B).
3. 🔴 **Honour BSD-3-Clause's third condition.** `open-tutor-ai-CE` forbids using the copyright
   holder's or contributors' names to endorse or promote a derivative without written permission.
   **Do not put "built on Open-TutorAI" in client-facing marketing** without that permission —
   attribution in the NOTICE file, yes; endorsement in a pitch deck, no. 🔵 This is the one
   obligation in the stack that bites *marketing* rather than *engineering*, which is exactly why
   it gets missed.
4. 🔴 **Three components are single-digit-to-low-double-digit★ and must be treated as corpora, not
   dependencies.** `pedagogy-benchmark` (13★, 5 commits), `rumi-platform` (18★),
   `Shiksha-Copilot` (9★) have no community and no security process. **Vendor the code into the
   engagement repository**, do not take a live dependency, and budget to maintain it yourself.
   `OpenMAIC` (781 commits), `dolos` (3,865 commits) and `Kolibri` are the three that can carry a
   real dependency.
5. 🟢 **Run `pedagogy-benchmark` before the pilot and keep the baseline.** It is the only licensed
   education-specific instrument available (see [`intel/trends.md`](../intel/trends.md) `T11`), and
   the **SEND** subset (223 items) is the only readable signal in this KB on special-educational-needs
   competence — the population where an unevaluated tutor does the most harm and where procurement
   asks the hardest questions.
6. 🟢 **Keep the human-oversight gate even though nothing here is formally high-risk yet.**
   `Shiksha-Copilot`'s shipped design — **every generated artefact routed to a teacher for review
   before classroom use** — is the pattern to copy, and `P492-1`'s rule stands: **the model never
   does the arithmetic on a grade.** This is what EU Annex III will require of a *provider* from
   **2 Dec 2027**, what Oklahoma S.B. 1734 appears to require of districts before the **2027-28**
   school year (see [`intel/market.md`](../intel/market.md) `p493`), and what Vietnam's decision
   keys its high-risk tier to.

**Licence note:** 🟢 **No copyleft anywhere in the stack**, including the optional LMS layer. The
one component to keep out is this KB's most-cited education skill pack,
[`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) —
**CC-BY-SA-4.0**, re-confirmed at 1 230 B this pass. 🔴 **ShareAlike on a content licence reaches
the derived curriculum, not just the code**, which would relicense the client's teaching materials.
Reference it; do not vendor it.

**Regional fit:** 🟢 **APAC strongest** — `OpenMAIC` (China), `Shiksha-Copilot` (India),
`rumi-platform` (Pakistan) are all regional in origin. 🟢 **LATAM** — pair with `Kolibri` and
`rumi-platform` against the **33-point Argentine socio-economic access gap** `p493` records, and note
there is still **no LATAM-origin component** at usable scale. 🟢 **EMEA** — `dolos` (Belgium) and
`open-tutor-ai-CE` (Morocco) are in-region, and the all-permissive property is what makes a
provider-grade conformity build sellable as product rather than as services. 🟡 **North America** —
the skill packs are NA-origin, but `P490-1` remains the faster route into US higher ed because
Canvas is the incumbent and has the only maintained agent surface.

**Scope:** 10–12 weeks to a governed pilot with an evaluation baseline. 🔵 Longer than `P490-1`
(4–6 weeks) because `OpenMAIC` is a courseware engine rather than an integration into an incumbent
LMS — **you are standing up a stack, not instrumenting one that exists.** Add 3–4 weeks if an
`OpenOLAT` institutional layer is in scope.

## 🆕 `P494-1` — APAC agentic education build with a Vietnam/Singapore jurisdiction fork 🟢

**Why:** `P490-4` offers a jurisdiction-routing provenance layer for APAC, and its premise is that
China's binding rules, India's labelling duty, Japan's promotion posture and Singapore's voluntary
assurance cannot be satisfied by one configuration. 🔴 **That premise had one of its four
jurisdictions deleted from this KB** — the Singapore posture was held at `p315` and removed by
`p315`'s own rewrite (see [`../intel/market.md`](../intel/market.md) `p494`). Restoring it, plus
`p494`'s reading of Vietnam's full education scope, changes what the APAC build actually has to
produce. 🟢 **Two of Vietnam's three high-risk education triggers do not transfer from an
EU-conformant design, and Singapore's agentic framework asks four questions no education regime
asks.** This pattern is `P493-1`'s all-permissive stack with those obligations built in.

**Base stack:** unchanged from [`P493-1`](#-p493-1--the-first-end-to-end-all-permissive-education-stack-) —
[`OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) (MIT, `70859b42e714`) for courseware and the
classroom, [`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3-Clause,
`196c547291da`) for 1:1 tutoring, [`dolos`](https://github.com/dodona-edu/dolos) (MIT,
`74b101785bad`) on submitted code,
[`pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) (MIT, `21a43a395ab4`)
on [`lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) (MIT) as the CI
release gate, [`Kolibri`](https://github.com/learningequality/kolibri) (MIT) and
[`rumi-platform`](https://github.com/Orenda-Project/rumi-platform) (Apache-2.0, `f2d62af1eb82`) for
delivery. 🟢 **No copyleft anywhere**, which is what makes the conformity artefacts below sellable
as product rather than as services.

### 🔴 The three Vietnam triggers, and what each one costs to build

Decision `33/2026/QD-TTg` (issued **30 Jun 2026**, in force **15 Aug 2026**) names **three**
education system types. This KB recorded one until `p494`.

| trigger | transfers from an EU build? | artefact you must produce |
|---|---|---|
| automatic **assessment, grading or ranking** of students | 🟢 **yes** — same functional trigger as EU Annex III | `P490-2`'s conformity pack, reused as-is |
| self-learning content from **uncontrolled data sources** | 🔴 **no** | a **corpus provenance manifest** — see below |
| **biometric** monitoring of learner behaviour | 🔴 **no, opposite direction** | a **build-time fork** — see below |

**1. 🔴 The corpus trigger fires on retrieval design alone.** A RAG tutor over an unvetted corpus is
high-risk in Vietnam **with no grading feature anywhere in the product**. This is a
corpus-governance obligation and an EU-conformant build produces nothing that answers it. Concretely,
in `open-tutor-ai-CE`'s retrieval path and `OpenMAIC`'s document-ingest path:

- **Pin the corpus and hash it.** One manifest row per document: source URL or acquisition route,
  licence, retrieval date, SHA-256, and the human who approved it. Vendor the manifest into the
  engagement repository next to the index.
- **Gate retrieval to the manifest.** Reject at query time any chunk whose document id is not in the
  manifest, and fail closed. An index rebuilt from a crawl that was never approved is the exact
  failure the trigger describes.
- 🔵 **This is cheap if done at week one and near-impossible to retrofit**, because the provenance of
  documents already embedded is not recoverable from the vector store.

**2. 🔴 Biometrics is a build-time fork, never a runtime policy flag.** The EU **prohibits** emotion
recognition in education outright (live since **2 Feb 2025**, narrow medical/safety exception —
`T6`); Vietnam **permits biometric learner monitoring as a high-risk category**, i.e. allowed subject
to conformity duties. 🟢 **The feature must be *absent* in one jurisdiction and *documented and
governed* in the other.** A feature flag does not satisfy the EU prohibition — the capability's
presence in a shipped artefact is the problem, not its default state. **Two build targets, one
codebase, and the EU target must not compile the module.** 🔵 This is the sharpest regulatory
asymmetry in this KB and the one most likely to be mistaken for a configuration question.

**3. 🟡 Which deadline applies depends on when the system went live, and the new-build answer is
single-sourced.** Education, healthcare and finance systems **in operation before 15 Aug 2026** have
until **1 Sep 2027**; other listed sectors have until **1 Mar 2027**. `p492` reports that a system
first operated **within six months after** 15 Aug 2026 falls back to **1 Mar 2027** — 🔴 **that row
rests on a single vendor compliance tracker and is expressly unconfirmed against the official
text.** **Plan to 1 Mar 2027**, because the error direction is safe that way, but 🔴 **do not put
either date in a contract before someone reads Decision 33's official text** (`english.luatvietnam.vn`
is subscriber-gated and does not open from this session). **Name that read as a deliverable in week
one.**

### 🟢 Singapore: four questions, four artefacts, and a voluntary gate worth designing to

IMDA's **Model AI Governance Framework for Agentic AI** (launched **22 Jan 2026**, voluntary, with
**AI Verify** as the assurance side — `T15`) asks the four questions a multi-agent education system
actually has to answer. 🔵 **Because it is voluntary, it is demonstrable** — design to the rubric and
point at it, rather than arguing an obligation down. And per this KB's restored Singapore note,
vendors selling into government and banks **are expected to point to these frameworks**, which makes
it a **procurement gate**.

| framework axis | artefact in this stack |
|---|---|
| **how much autonomy the agent is granted** | A written capability inventory per agent role in `OpenMAIC`'s multi-agent classroom: what each may read, generate, and persist. 🔴 **No agent gets write access to a gradebook** — `P492-1`'s rule, and the one that survives every regime here |
| **how actions are bounded and logged** | Structured per-action log (agent id, tool, inputs, outputs, timestamp) retained for the engagement's audit window. 🔵 The same log discharges Vietnam's human-review evidence, so build it once |
| **how humans stay meaningfully in the loop** | [`microsoft/Shiksha-Copilot`](https://github.com/microsoft/Shiksha-Copilot)'s shipped design (MIT, 9★): **every generated artefact routed to a teacher for review before classroom use.** Copy the shape; vendor the code, do not depend on it |
| **accountability when several agents interact** | A named owner per agent role and a single escalation path. 🔴 This is the axis most multi-agent demos have nothing to say about, and the one a Singapore procurement reviewer will ask about first |

🟢 **And the arithmetic rule is the one thing every regime in this file agrees on.**
[`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) (MIT, `5511bf6dc707`,
🔴 **0★, 13 commits — a reference design, not a dependency**) is the only implementation this KB can
hand an engineer: per-criterion structured output validated against the rubric, **totals computed in
Python, never by the model**, plus an answer-leak guard. **Copy both mechanisms into the engagement
repository.**

### Do this or it is negligent

1. 🔴 **Decide the biometric question before the first sprint, not at UAT.** It determines whether
   you have one build target or two, and retrofitting the EU target means removing a module from a
   shipped artefact and re-certifying it.
2. 🔴 **Produce the corpus provenance manifest from the first ingested document.** Provenance is not
   recoverable from a vector store after the fact.
3. 🔴 **Pin every component by SHA or release tag and re-read the licence bytes at that pin.**
   `p493` found eight promoted rows deleted from this KB's own shelves, and `canvas-mcp` has now
   drifted **twice in ~24 hours** — `32e5d1ca0175` → `830bc2ef8389` → `47394125364b`, the last move
   observed **inside a single pass's window**, licence byte-identical throughout. 🔵 **The rule that
   follows: pin a release tag wherever upstream publishes one, and treat a HEAD SHA as a dated
   observation rather than a pin.** Pins as read `2026-10-28` are listed in `P493-1`; the components
   in this pattern were all re-resolved at that date and only `canvas-mcp` moved.
4. 🔴 **Treat `pedagogy-benchmark` (13★), `rumi-platform` (18★), `Shiksha-Copilot` (9★) and
   `ai-tutor-agent` (0★) as corpora, not dependencies.** Vendor them; budget to maintain them.
5. 🟢 **Run `pedagogy-benchmark` before the pilot and keep the baseline**, including the **SEND**
   subset (223 items) — the population where an unevaluated tutor does most harm and where
   procurement asks hardest.
6. 🔴 **Do not claim an agent-identity requirement for Singapore.** An academic commentary
   (`arXiv:2608.15417`) asserts the framework requires verifiable per-agent digital identity and an
   audit trail; that conflicts with its voluntary standing and 🔴 **`arxiv.org` is
   `connect_rejected` by this session's proxy**, so it is unverified. Build the audit log because it
   is good practice and discharges Vietnam's evidence need — **not because Singapore mandates it.**
7. 🔴 **Honour BSD-3-Clause's third condition** on `open-tutor-ai-CE`: attribution in `NOTICE`, yes;
   **"built on Open-TutorAI" in a pitch deck, no**, absent written permission.

**Regional fit:** 🟢 **APAC-native** — `OpenMAIC` (China), `Shiksha-Copilot` (India),
`rumi-platform` (Pakistan) are in-region by origin. 🟡 **Do not carry an "APAC is permissive"
framing into Australia or New Zealand** — `p493` records ANZ showing *higher* support for banning AI
in schools than the seven APAC markets at 23–31%, an EMEA-like public mood. 🔵 **The corpus manifest
and the action log are jurisdiction-neutral and transfer to EMEA and LATAM engagements unchanged**,
which is the part of this pattern worth reusing even where Decision 33 does not apply.

**Scope:** 12–14 weeks to a governed pilot — `P493-1`'s 10–12 plus 2 weeks for the corpus manifest
and the action-log schema. 🔴 **Add 4–6 weeks if the biometric fork is in scope**, and resolve that
question in week one, because it is the only item here that cannot be parallelised.


## 🆕 `P495-1` — Hardened Canvas agent deployment 🟢 *(amends `P490-1`; supersedes its pin and its tool list)*

🔴 **Why this exists.** `P490-1` recommends [`canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp)
as the Canvas agent surface and that recommendation **stands** — it is still the only maintained
agent surface on an incumbent LMS this KB has found. 🔴 **But `p495`'s first-hand advisory read makes
the deployment details non-optional**: below `v1.16.0` the base ships **two High** advisories, and
`v1.16.0` itself is only patched **on Node.js ≥ 22.18** while its advisory states in writing that
**executed code can still reach the caller's Canvas token**.

### The stack

| role | component | licence | pin | note |
|---|---|---|---|---|
| LMS agent surface | [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | MIT *(`1 071 B`, `sha1 491fb891a4cf`)* | 🔴 **tag `v1.16.0` = `b3f06c76e43569f10f8f11833b4eb4ba2ee478ba`** | **never branch HEAD**; HEAD `47394125364b` is unreleased code above the newest tag |
| runtime | Node.js | — | 🔴 **≥ 22.18** | the sandbox fix *is* Node's permission model; older Node = unpatched |
| tutor / RAG core | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 *(see the licence caveat in [`../agents/top.md`](../agents/top.md))* | `a31d82624c27` | 🟢 5 passes byte-stable |
| quality gate | [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | MIT | — | 1,143 teacher-exam items; 🔴 do not cite its arXiv abstract until a human opens it (`arxiv.org` is proxy-refused) |
| integrity | [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT | `74b101785bad` | plagiarism detection, the most-maintained address on the permissive shelf |

### Wiring — the five hardening steps, in order

1. 🔴 **Pin the tag, not the branch.** `pip install canvas-mcp==1.16.0`, or check out
   `b3f06c76e43569f10f8f11833b4eb4ba2ee478ba`. **Record the tag in the client's SBOM**, because that
   is the only artefact that lets anyone later say which advisories were closed at ship time.
2. 🔴 **Assert the runtime, in CI, as a build failure.** `node -v` → must be **≥ 22.18**. A version
   check here is not hygiene: it is the difference between the sandbox being enforced and the
   version string merely claiming it is. **Do this before any functional test**, because every
   functional test passes either way.
3. 🔴 **Disable `execute_typescript` at the server's tool registry**, and assert its absence in the
   agent's tool list at startup. The `1.16.0` advisory states egress blocking is best-effort and
   **executed code can still access the caller's Canvas token** — so the only complete mitigation
   is that the capability is not exposed. 🔵 Nothing in `P490-1`'s use case (course Q&A, assignment
   lookup, submission summaries) needs code execution.
4. 🔴 **Scope and time-box the Canvas token.** `GHSA-7mj9-4mcg-hvhv` has the bearer token sent to a
   URL **chosen by the file-storage host** on upload confirmation. Use the narrowest Canvas
   developer-key scopes that satisfy the tool list, short expiry, rotation, and **never an
   admin-scoped token for an instructor-facing agent.**
5. 🔴 **Treat course content as hostile input.** `GHSA-hmr8-mvr2-mvw5` is a student editing course
   content to instruct the instructor's assistant, reaching **grade change**. `1.13.0` added a write
   allowlist and message previews; `1.16.0` marks `read_course_file` contents untrusted. 🔵 **Keep
   both**: no write tool reachable on a first call, and a human preview on any grade-affecting
   action. **Log every write with the prompt that produced it** — which is also what satisfies
   Singapore's agentic-AI framework (action logging, human-in-the-loop placement, accountability
   across agents) per [`../intel/market.md`](../intel/market.md), and is reusable as evidence rather
   than as overhead.

### What this pattern is worth saying out loud to a client

🔵 **The deployable posture here cost a release-tag read, four advisory reads, a CVSS read and a
runtime check** — none of which a university IT department will do before installing an MCP server
someone demoed to them. 🟢 **That gap is the engagement.** The sellable artefact is not the tutor:
it is **a pinned, hardened, logged integration with a written risk register**, on an MIT base the
client can keep.

🔴 **Say the residual risk plainly, because it does not go away with the patch:** an agent holding an
instructor's Canvas token and reading student-editable content is a real attack surface. The
mitigation is capability-removal and credential-scoping, and the **audit log is the control that
makes the remaining risk detectable** rather than deniable.

### 🟡 Honest limits of this recipe

- 🔴 **`v1.16.0` is the newest tag AND the minimum safe one.** There is no headroom: the next
  advisory has no released fix to point at. **Re-read the advisory page before each client ship** —
  do not inherit this pass's count of four.
- 🟡 **Advisory severities were read from the GitHub advisory pages, not from CVE records.** The
  CVSS vector is published for `GHSA-7pp5-29mw-9jq3` (7.8) and **not** for the other three.
- 🔴 **`DeepTutor`'s licence caveat and `pedagogy-benchmark`'s unread paper are unchanged** and both
  need a human (`arxiv.org` is **proxy-refused** from this session, permanently — `p494`/`p495`).

